#!/usr/bin/env python3
"""Build the repository's printable curriculum collections.

The PDFs intentionally compile the navigational and pedagogical guides rather
than duplicating every detailed OA file.  Every OA link remains clickable and
points to the canonical Markdown source on GitHub.
"""

from __future__ import annotations

import argparse
import hashlib
import re
import unicodedata
from dataclasses import dataclass
from pathlib import Path
from urllib.parse import quote

import reportlab
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (
    BaseDocTemplate,
    Frame,
    PageBreak,
    PageTemplate,
    Paragraph,
    Preformatted,
    Spacer,
    Table,
    TableStyle,
)
from reportlab.platypus.tableofcontents import TableOfContents
from xml.sax.saxutils import escape


ROOT = Path(__file__).resolve().parents[1]
DOCS = ROOT / "docs"
OUTPUT = ROOT / "output" / "pdf"
REPOSITORY_URL = "https://github.com/vladimiracunadev-create/chilean-school-learning-path"
PAGES_URL = "https://vladimiracunadev-create.github.io/chilean-school-learning-path"

LEVELS = [
    "1-basico",
    "2-basico",
    "3-basico",
    "4-basico",
    "5-basico",
    "6-basico",
    "7-basico",
    "8-basico",
    "1-medio",
    "2-medio",
    "3-medio",
    "4-medio",
]
LEVEL_LABELS = {
    "1-basico": "1° básico",
    "2-basico": "2° básico",
    "3-basico": "3° básico",
    "4-basico": "4° básico",
    "5-basico": "5° básico",
    "6-basico": "6° básico",
    "7-basico": "7° básico",
    "8-basico": "8° básico",
    "1-medio": "1° medio",
    "2-medio": "2° medio",
    "3-medio": "3° medio",
    "4-medio": "4° medio",
}

INK = colors.HexColor("#17342A")
GREEN = colors.HexColor("#17643A")
MINT = colors.HexColor("#EAF4EE")
GOLD = colors.HexColor("#D89A2B")
PAPER = colors.HexColor("#FBFAF5")
MUTED = colors.HexColor("#5A6962")
LINE = colors.HexColor("#C9D7CF")
WHITE = colors.white

FONT_DIR = Path(reportlab.__file__).resolve().parent / "fonts"
FONT_LICENSE_PATH = FONT_DIR / "bitstream-vera-license.txt"
pdfmetrics.registerFont(TTFont("Vera", str(FONT_DIR / "Vera.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Bold", str(FONT_DIR / "VeraBd.ttf")))
pdfmetrics.registerFont(TTFont("Vera-Italic", str(FONT_DIR / "VeraIt.ttf")))
pdfmetrics.registerFont(TTFont("Vera-BoldItalic", str(FONT_DIR / "VeraBI.ttf")))


def current_document_release() -> str:
    """Return the dated label that also drives the public changelog summary."""
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
    match = re.search(r"^## (\d{4}-\d{2}-\d{2}) [·—-] (.+)$", changelog, flags=re.MULTILINE)
    if not match:
        raise RuntimeError("CHANGELOG.md no contiene una primera entrada fechada")
    return f"{match.group(1)} · {match.group(2).strip()}"


@dataclass(frozen=True)
class PdfJob:
    filename: str
    title: str
    subtitle: str
    sources: tuple[Path, ...]


class CurriculumDocTemplate(BaseDocTemplate):
    """Document template with outline entries and a generated table of contents."""

    def __init__(self, filename: str, *, title: str, release_label: str):
        self.release_label = release_label
        super().__init__(
            filename,
            pagesize=A4,
            leftMargin=18 * mm,
            rightMargin=18 * mm,
            topMargin=19 * mm,
            bottomMargin=18 * mm,
            title=title,
            author="Trayectoria Escolar Chile",
            subject=f"Planificación curricular chilena · {release_label}",
            creator="chilean-school-learning-path",
            invariant=1,
            pageCompression=1,
        )
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="content",
        )
        # Draw the footer after flowables so tables or continuation frames cannot cover it.
        self.addPageTemplates(PageTemplate(id="main", frames=[frame], onPageEnd=self._decorate_page))

    def _decorate_page(self, canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(GREEN)
        canvas.setLineWidth(0.7)
        canvas.line(18 * mm, 14 * mm, A4[0] - 18 * mm, 14 * mm)
        canvas.setFillColor(MUTED)
        canvas.setFont("Vera", 7.5)
        release_date = self.release_label.split(" · ", 1)[0]
        canvas.drawString(18 * mm, 9.5 * mm, f"Trayectoria Escolar Chile · {release_date}")
        page = f"Página {canvas.getPageNumber()}"
        canvas.drawRightString(A4[0] - 18 * mm, 9.5 * mm, page)
        canvas.restoreState()

    def afterFlowable(self, flowable):
        bookmark = getattr(flowable, "_bookmark", None)
        if not bookmark:
            return
        title = getattr(flowable, "_toc_title", "")
        level = getattr(flowable, "_toc_level", 0)
        self.canv.bookmarkPage(bookmark)
        self.canv.addOutlineEntry(title, bookmark, level=level, closed=level > 0)
        self.notify("TOCEntry", (level, title, self.page, bookmark))


def clean_text(value: str) -> str:
    replacements = {
        "\u00a0": " ",
        "\u2010": "-",
        "\u2011": "-",
        "\u2012": "-",
        "\u2013": "-",
        "\u2014": "-",
        "\u2212": "-",
        "\u2190": "<-",
        "\u2192": "->",
        "\u2191": "^",
        "\u2193": "v",
        "\u2026": "...",
        "\ufe0f": "",
    }
    for old, new in replacements.items():
        value = value.replace(old, new)
    return "".join(
        char
        for char in value
        if unicodedata.category(char) != "So" or char in {"°", "©", "®"}
    ).strip()


def repository_link(target: str, source: Path) -> str:
    if re.match(r"^(?:https?|mailto):", target):
        return target
    if target.startswith("#"):
        return f"{REPOSITORY_URL}/blob/main/{source.relative_to(ROOT).as_posix()}{target}"
    path_text, separator, fragment = target.partition("#")
    resolved = (source.parent / path_text).resolve()
    try:
        relative = resolved.relative_to(ROOT).as_posix()
    except ValueError:
        return f"{REPOSITORY_URL}/tree/main"
    suffix = f"#{quote(fragment, safe='-_')}" if separator else ""
    return f"{REPOSITORY_URL}/blob/main/{quote(relative, safe='/._-')}{suffix}"


TOKEN_RE = re.compile(r"(\[[^\]]+\]\([^)]+\)|\*\*[^*]+\*\*|`[^`]+`)")


def inline_markup(value: str, source: Path) -> str:
    value = clean_text(value)
    parts: list[str] = []
    position = 0
    for match in TOKEN_RE.finditer(value):
        parts.append(escape(value[position : match.start()]))
        token = match.group(0)
        if token.startswith("["):
            link_match = re.match(r"\[([^\]]+)\]\(([^)]+)\)", token)
            assert link_match
            label, target = link_match.groups()
            href = escape(repository_link(target, source), {'"': '&quot;'})
            parts.append(f'<link href="{href}" color="#17643A"><u>{escape(clean_text(label))}</u></link>')
        elif token.startswith("**"):
            parts.append(f"<b>{escape(clean_text(token[2:-2]))}</b>")
        else:
            parts.append(f'<font name="Courier" color="#304F42">{escape(clean_text(token[1:-1]))}</font>')
        position = match.end()
    parts.append(escape(value[position:]))
    return "".join(parts)


def first_heading(path: Path) -> str:
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("# "):
            return clean_text(line[2:])
    return path.stem.replace("-", " ").title()


def make_styles():
    styles = getSampleStyleSheet()
    return {
        "cover_title": ParagraphStyle(
            "CoverTitle",
            parent=styles["Title"],
            fontName="Vera-Bold",
            fontSize=29,
            leading=34,
            textColor=INK,
            alignment=TA_LEFT,
            spaceAfter=10,
        ),
        "cover_subtitle": ParagraphStyle(
            "CoverSubtitle",
            parent=styles["Normal"],
            fontName="Vera",
            fontSize=13,
            leading=19,
            textColor=MUTED,
            spaceAfter=12,
        ),
        "section": ParagraphStyle(
            "Section",
            parent=styles["Heading1"],
            fontName="Vera-Bold",
            fontSize=20,
            leading=24,
            textColor=INK,
            spaceBefore=0,
            spaceAfter=12,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=styles["Heading2"],
            fontName="Vera-Bold",
            fontSize=14,
            leading=17,
            textColor=GREEN,
            spaceBefore=12,
            spaceAfter=6,
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=styles["Heading3"],
            fontName="Vera-Bold",
            fontSize=11,
            leading=14,
            textColor=INK,
            spaceBefore=9,
            spaceAfter=4,
        ),
        "body": ParagraphStyle(
            "Body",
            parent=styles["BodyText"],
            fontName="Vera",
            fontSize=8.6,
            leading=12.2,
            textColor=colors.HexColor("#22332B"),
            spaceAfter=5,
        ),
        "bullet": ParagraphStyle(
            "Bullet",
            parent=styles["BodyText"],
            fontName="Vera",
            fontSize=8.4,
            leading=11.8,
            leftIndent=12,
            firstLineIndent=-7,
            textColor=colors.HexColor("#22332B"),
            spaceAfter=2.5,
        ),
        "quote": ParagraphStyle(
            "Quote",
            parent=styles["BodyText"],
            fontName="Vera-Italic",
            fontSize=8.4,
            leading=12,
            leftIndent=10,
            rightIndent=6,
            borderColor=GOLD,
            borderWidth=0,
            borderLeft=2,
            borderPadding=7,
            backColor=colors.HexColor("#FFF8E8"),
            textColor=colors.HexColor("#4B4B3F"),
            spaceAfter=6,
        ),
        "code": ParagraphStyle(
            "Code",
            fontName="Courier",
            fontSize=6.7,
            leading=9,
            leftIndent=5,
            rightIndent=5,
            backColor=colors.HexColor("#EEF3F0"),
            borderPadding=6,
            spaceAfter=6,
        ),
        "toc_heading": ParagraphStyle(
            "TocHeading",
            parent=styles["Heading1"],
            fontName="Vera-Bold",
            fontSize=18,
            leading=22,
            textColor=INK,
            spaceAfter=10,
        ),
        "small": ParagraphStyle(
            "Small",
            parent=styles["BodyText"],
            fontName="Vera",
            fontSize=7.5,
            leading=10.5,
            textColor=MUTED,
            spaceAfter=4,
        ),
        "table_cell": ParagraphStyle(
            "TableCell",
            parent=styles["BodyText"],
            fontName="Vera",
            fontSize=7.2,
            leading=9.4,
            textColor=MUTED,
            spaceAfter=0,
        ),
        "table_header": ParagraphStyle(
            "TableHeader",
            parent=styles["BodyText"],
            fontName="Vera-Bold",
            fontSize=7.2,
            leading=9.4,
            textColor=WHITE,
            spaceAfter=0,
        ),
    }


def table_widths(rows: list[list[str]], available: float) -> list[float]:
    columns = max(len(row) for row in rows)
    maxima = []
    for column in range(columns):
        lengths = [len(clean_text(row[column])) if column < len(row) else 0 for row in rows[:120]]
        maxima.append(max(8, min(max(lengths, default=8), 55)))
    total = sum(maxima)
    minimum = (20 if columns <= 5 else 17 if columns == 6 else 12) * mm
    reserved = minimum * columns
    if reserved >= available:
        return [available / columns] * columns
    variable = available - reserved
    return [minimum + variable * value / total for value in maxima]


def markdown_story(path: Path, styles: dict, available_width: float) -> list:
    lines = path.read_text(encoding="utf-8").splitlines()
    story: list = []
    paragraph: list[str] = []
    code: list[str] = []
    in_code = False
    table_rows: list[list[str]] = []
    skipped_first_h1 = False

    def flush_paragraph():
        if paragraph:
            joined = " ".join(part.strip() for part in paragraph)
            story.append(Paragraph(inline_markup(joined, path), styles["body"]))
            paragraph.clear()

    def flush_table():
        if not table_rows:
            return
        rows = [row for row in table_rows if not all(re.fullmatch(r":?-{3,}:?", cell.strip()) for cell in row)]
        table_rows.clear()
        if not rows:
            return
        columns = max(len(row) for row in rows)
        padded = [row + [""] * (columns - len(row)) for row in rows]
        data = []
        for row_index, row in enumerate(padded):
            style = styles["table_header"] if row_index == 0 else styles["table_cell"]
            data.append([Paragraph(inline_markup(cell, path), style) for cell in row])
        table = Table(data, colWidths=table_widths(padded, available_width), repeatRows=1, hAlign="LEFT")
        table.setStyle(
            TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), GREEN),
                    ("TEXTCOLOR", (0, 0), (-1, 0), WHITE),
                    ("FONTNAME", (0, 0), (-1, 0), "Vera-Bold"),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("GRID", (0, 0), (-1, -1), 0.35, LINE),
                    ("ROWBACKGROUNDS", (0, 1), (-1, -1), [WHITE, PAPER]),
                    ("LEFTPADDING", (0, 0), (-1, -1), 3.5),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 3.5),
                    ("TOPPADDING", (0, 0), (-1, -1), 3),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ]
            )
        )
        story.extend([table, Spacer(1, 5)])

    for raw_line in lines:
        line = raw_line.rstrip()
        if line.startswith("~~~") or line.startswith("```"):
            flush_paragraph()
            flush_table()
            if in_code:
                story.append(Preformatted(clean_text("\n".join(code)), styles["code"], maxLineLength=112))
                code.clear()
            in_code = not in_code
            continue
        if in_code:
            code.append(line)
            continue
        if line.startswith("|") and line.endswith("|"):
            flush_paragraph()
            table_rows.append([cell.strip() for cell in line.strip("|").split("|")])
            continue
        flush_table()
        if not line.strip():
            flush_paragraph()
            continue
        heading = re.match(r"^(#{1,6})\s+(.+)$", line)
        if heading:
            flush_paragraph()
            depth, title = len(heading.group(1)), re.sub(r"\s+\{#[^}]+\}\s*$", "", heading.group(2))
            if depth == 1 and not skipped_first_h1:
                skipped_first_h1 = True
                continue
            style = styles["h2"] if depth <= 2 else styles["h3"]
            story.append(Paragraph(inline_markup(title, path), style))
            continue
        if line.startswith(">"):
            flush_paragraph()
            story.append(Paragraph(inline_markup(line.lstrip("> "), path), styles["quote"]))
            continue
        bullet = re.match(r"^\s*[-*]\s+(.+)$", line)
        numbered = re.match(r"^\s*(\d+)\.\s+(.+)$", line)
        if bullet or numbered:
            flush_paragraph()
            if bullet:
                marker, text = "•", bullet.group(1)
            else:
                marker, text = f"{numbered.group(1)}.", numbered.group(2)
            story.append(Paragraph(f"{marker} {inline_markup(text, path)}", styles["bullet"]))
            continue
        if re.fullmatch(r"\s*---+\s*", line):
            flush_paragraph()
            story.append(Spacer(1, 5))
            continue
        paragraph.append(line)
    flush_paragraph()
    flush_table()
    if code:
        story.append(Preformatted(clean_text("\n".join(code)), styles["code"], maxLineLength=112))
    return story


def bookmark_name(path: Path, index: int) -> str:
    digest = hashlib.sha1(path.as_posix().encode("utf-8")).hexdigest()[:10]
    return f"section-{index:03d}-{digest}"


def build_pdf(job: PdfJob) -> None:
    styles = make_styles()
    destination = OUTPUT / job.filename
    release_label = current_document_release()
    document = CurriculumDocTemplate(str(destination), title=job.title, release_label=release_label)
    story: list = [
        Spacer(1, 27 * mm),
        Paragraph("TRAYECTORIA ESCOLAR CHILE", styles["small"]),
        Spacer(1, 5 * mm),
        Paragraph(escape(job.title), styles["cover_title"]),
        Paragraph(escape(job.subtitle), styles["cover_subtitle"]),
        Paragraph(f"Corte documental: {escape(clean_text(release_label))}", styles["small"]),
        Spacer(1, 7 * mm),
        Table(
            [
                [Paragraph("ALCANCE", styles["small"]), Paragraph("FUENTE", styles["small"])],
                [
                    Paragraph(f"{len(job.sources)} documentos canónicos", styles["body"]),
                    Paragraph("Repositorio main · enlaces OA clicables", styles["body"]),
                ],
            ],
            colWidths=[document.width * 0.48, document.width * 0.52],
            style=TableStyle(
                [
                    ("BACKGROUND", (0, 0), (-1, 0), MINT),
                    ("BOX", (0, 0), (-1, -1), 0.7, GREEN),
                    ("INNERGRID", (0, 0), (-1, -1), 0.35, LINE),
                    ("VALIGN", (0, 0), (-1, -1), "TOP"),
                    ("LEFTPADDING", (0, 0), (-1, -1), 8),
                    ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                    ("TOPPADDING", (0, 0), (-1, -1), 7),
                    ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                ]
            ),
        ),
        Spacer(1, 10 * mm),
        Paragraph(
            "Compilación de guías pedagógicas e índices. Las fichas OA detalladas se abren desde los enlaces del documento. "
            "La revisión profesional humana continúa pendiente según el estado editorial del repositorio.",
            styles["quote"],
        ),
        Spacer(1, 8 * mm),
        Paragraph(f'<link href="{PAGES_URL}" color="#17643A"><u>{PAGES_URL}</u></link>', styles["small"]),
        PageBreak(),
        Paragraph("Contenido", styles["toc_heading"]),
    ]

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOC0",
            fontName="Vera",
            fontSize=9,
            leading=13,
            leftIndent=0,
            firstLineIndent=0,
            textColor=INK,
            spaceBefore=3,
        )
    ]
    story.extend([toc, PageBreak()])

    for index, source in enumerate(job.sources):
        if index:
            story.append(PageBreak())
        title = first_heading(source)
        heading = Paragraph(escape(title), styles["section"])
        heading._bookmark = bookmark_name(source, index)
        heading._toc_title = title
        heading._toc_level = 0
        story.append(heading)
        relative = source.relative_to(ROOT).as_posix()
        story.append(
            Paragraph(
                f'Fuente: <link href="{REPOSITORY_URL}/blob/main/{quote(relative, safe="/._-")}" '
                f'color="#17643A"><u>{escape(relative)}</u></link>',
                styles["small"],
            )
        )
        story.extend(markdown_story(source, styles, document.width))

    story.extend(
        [
            PageBreak(),
            Paragraph("Aviso de la tipografía incrustada", styles["section"]),
            Paragraph(
                "Los subconjuntos tipográficos usados en este archivo proceden de Bitstream Vera. "
                "Se reproduce a continuación el aviso que acompaña a la distribución de ReportLab.",
                styles["body"],
            ),
        ]
    )
    license_notice = FONT_LICENSE_PATH.read_text(encoding="utf-8").split("Copyright FAQ", 1)[0]
    for block in re.split(r"\n\s*\n", license_notice):
        compact = " ".join(line.strip() for line in block.splitlines())
        if compact:
            story.append(Paragraph(escape(clean_text(compact)), styles["small"]))

    document.multiBuild(story)


def level_sources(level: str) -> tuple[Path, ...]:
    folder = DOCS / level
    return (folder / "README.md",) + tuple(sorted(path for path in folder.glob("*.md") if path.name != "README.md"))


def subject_groups() -> dict[str, tuple[Path, ...]]:
    groups: dict[str, list[Path]] = {}
    for level in LEVELS:
        for path in sorted((DOCS / level).glob("*.md")):
            if path.name != "README.md":
                groups.setdefault(path.stem, []).append(path)
    return {slug: tuple(paths) for slug, paths in sorted(groups.items())}


def complete_sources(catalog_path: Path) -> tuple[Path, ...]:
    top_level = [
        ROOT / "README.md",
        ROOT / "CURRICULUM.md",
        ROOT / "LEARNING_PATHS.md",
        ROOT / "TEACHING_GUIDE.md",
        ROOT / "METHODOLOGY.md",
        ROOT / "QUALITY_STANDARD.md",
        ROOT / "EDITORIAL_STATUS.md",
        ROOT / "ROADMAP.md",
        ROOT / "OFFICIAL_REFERENCES.md",
        ROOT / "LICENSING.md",
        ROOT / "DATA-LICENSE.md",
        ROOT / "ASSET_LICENSES.md",
        ROOT / "ATTRIBUTION.md",
    ]
    docs_root = [path for path in sorted(DOCS.glob("*.md")) if path != catalog_path]
    grades = [path for level in LEVELS for path in level_sources(level)]
    return tuple(top_level + docs_root + [catalog_path] + grades)


def build_jobs(catalog_path: Path | None = None) -> list[PdfJob]:
    catalog_path = catalog_path or DOCS / "PDFS.md"
    basic = tuple(path for level in LEVELS[:8] for path in level_sources(level))
    media = tuple(path for level in LEVELS[8:] for path in level_sources(level))
    jobs = [
        PdfJob(
            "educacion-basica-completa.pdf",
            "Educación Básica completa",
            "Guías de 1° a 8° básico, organizadas por nivel y asignatura.",
            basic,
        ),
        PdfJob(
            "ensenanza-media-completa.pdf",
            "Enseñanza Media completa",
            "Guías de 1° a 4° medio, organizadas por nivel y asignatura.",
            media,
        ),
    ]
    for slug, sources in subject_groups().items():
        subject_name = first_heading(sources[0]).split(" · ")[0]
        jobs.append(
            PdfJob(
                f"por-asignatura-{slug}.pdf",
                f"{subject_name} - compilación completa",
                f"Guías disponibles para {len(sources)} nivel{'es' if len(sources) != 1 else ''}.",
                sources,
            )
        )
    for level in LEVELS:
        sources = level_sources(level)
        jobs.append(
            PdfJob(
                f"por-nivel-{level}.pdf",
                f"{LEVEL_LABELS[level]} completo",
                "Índice del nivel y todas sus guías de asignatura.",
                sources,
            )
        )
    jobs.append(
        PdfJob(
            "trayectoria-escolar-completa.pdf",
            "Trayectoria Escolar Chile - compilación completa",
            "Documentación transversal, índice curricular y 149 guías de asignatura de 1° básico a 4° medio.",
            complete_sources(catalog_path),
        )
    )
    if len(jobs) != 49:
        raise RuntimeError(f"Se esperaban 49 exportaciones PDF y se definieron {len(jobs)}")
    return jobs


def relative_pdf_link(filename: str) -> str:
    return f"../output/pdf/{filename}"


def write_catalog(jobs: list[PdfJob], destination: Path) -> None:
    aggregate = jobs[:2]
    subject_jobs = [job for job in jobs if job.filename.startswith("por-asignatura-")]
    level_jobs = [job for job in jobs if job.filename.startswith("por-nivel-")]
    complete = jobs[-1]
    lines = [
        "# PDFs para descarga",
        "",
        "Las **49 compilaciones PDF** se generan desde las guías canónicas del repositorio. Incluyen tabla de contenido, numeración, enlaces clicables a las fichas OA y los avisos de estado editorial.",
        "",
        "Cada portada y sus metadatos muestran el corte documental tomado de la primera entrada fechada de `CHANGELOG.md`. La CI comprueba inventario, versión, metadatos, fuentes únicas, enlaces y lectura de cada PDF. No compara sus bytes entre sistemas operativos: el motor tipográfico puede producir contenedores distintos con el mismo contenido, incluso con dependencias fijadas.",
        "",
        "> Los PDF compilan índices y guías pedagógicas. Las 2.823 fichas OA detalladas permanecen como fuente canónica en Markdown y HTML; cada entrada del PDF enlaza a su ficha para evitar duplicar el repositorio completo en cada agrupación.",
        "",
        "## Compilaciones generales",
        "",
        "| Alcance | Descarga |",
        "|---|---|",
    ]
    for job in aggregate:
        lines.append(f"| {job.title} | [Descargar PDF]({relative_pdf_link(job.filename)}) |")
    lines.extend(
        [
            f"| Todo el programa y la documentación | [Descargar PDF completo]({relative_pdf_link(complete.filename)}) |",
            "",
            "## PDF por nivel",
            "",
            "| Nivel | Descarga |",
            "|---|---|",
        ]
    )
    for job in level_jobs:
        lines.append(f"| {job.title.removesuffix(' completo')} | [Descargar PDF]({relative_pdf_link(job.filename)}) |")
    lines.extend(["", "## PDF por asignatura o denominación curricular", "", "| Asignatura | Niveles incluidos | Descarga |", "|---|---:|---|"])
    for job in subject_jobs:
        lines.append(
            f"| {job.title.removesuffix(' - compilación completa')} | {len(job.sources)} | [Descargar PDF]({relative_pdf_link(job.filename)}) |"
        )
    lines.extend(
        [
            "",
            "## Reproducibilidad y alcance",
            "",
            "Ejecuta `python scripts/export_pdfs.py` después de regenerar el programa. La CI vuelve a crear las 49 salidas, valida su contenido y exige que los demás artefactos derivados no presenten diferencias.",
            "",
            "Los PDF mantienen la separación de derechos descrita en [Licencias](../LICENSING.md): convertir a PDF no modifica la licencia ni la procedencia de cada componente.",
            "",
        ]
    )
    destination.write_text("\n".join(lines), encoding="utf-8")


def validate_outputs(jobs: list[PdfJob]) -> None:
    from pypdf import PdfReader

    release_label = current_document_release()
    expected = {job.filename for job in jobs}
    actual = {path.name for path in OUTPUT.glob("*.pdf")}
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        raise RuntimeError(f"Inventario PDF incorrecto; faltan={missing}, sobran={extra}")
    for job in jobs:
        path = OUTPUT / job.filename
        reader = PdfReader(path)
        if len(reader.pages) < 3:
            raise RuntimeError(f"{path.name} tiene menos de tres páginas")
        if len(reader.outline) != len(job.sources):
            raise RuntimeError(
                f"{path.name} tiene {len(reader.outline)} marcadores para {len(job.sources)} fuentes"
            )
        if path.stat().st_size >= 100 * 1024 * 1024:
            raise RuntimeError(f"{path.name} supera el límite de 100 MiB")
        if reader.metadata.title != job.title:
            raise RuntimeError(f"Metadatos de título incorrectos en {path.name}")
        if reader.metadata.author != "Trayectoria Escolar Chile":
            raise RuntimeError(f"Metadatos de autor incorrectos en {path.name}")
        if release_label not in (reader.metadata.subject or ""):
            raise RuntimeError(f"Versión documental ausente de los metadatos en {path.name}")
        if reader.metadata.creator != "chilean-school-learning-path":
            raise RuntimeError(f"Metadatos de creador incorrectos en {path.name}")
        first_text = " ".join((reader.pages[0].extract_text() or "").split())
        if clean_text(job.title) not in clean_text(first_text):
            raise RuntimeError(f"La portada de {path.name} no contiene el título")
        if clean_text(release_label) not in clean_text(first_text):
            raise RuntimeError(f"La portada de {path.name} no contiene la versión documental")
        for page_number, page in enumerate(reader.pages, start=1):
            stream = page.get_contents().get_data()
            if b"Trayectoria Escolar Chile" not in stream[-1500:]:
                raise RuntimeError(
                    f"El pie de página no es la última capa visual en {path.name}, página {page_number}"
                )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--validate-only", action="store_true", help="Valida los 49 PDF existentes sin regenerarlos")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    catalog_path = DOCS / "PDFS.md"
    jobs = build_jobs(catalog_path)
    if not args.validate_only:
        OUTPUT.mkdir(parents=True, exist_ok=True)
        write_catalog(jobs, catalog_path)
        for index, job in enumerate(jobs, start=1):
            print(f"[{index:02d}/{len(jobs)}] {job.filename}")
            build_pdf(job)
    validate_outputs(jobs)
    print(f"PDF verificados: {len(jobs)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
