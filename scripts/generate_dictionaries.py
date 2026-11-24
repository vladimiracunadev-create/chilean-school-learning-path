#!/usr/bin/env python3
"""Genera los diccionarios de español e inglés por nivel en docs/diccionarios/.

Fuentes: scripts/dict_data_es_NN.py y scripts/dict_data_en_NN.py (un par por nivel, NN = 01..12).
Uso:
    python scripts/generate_dictionaries.py          # escribe los Markdown
    python scripts/generate_dictionaries.py --check  # solo valida los datos
"""
from __future__ import annotations

import importlib
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
OUT = ROOT / "docs" / "diccionarios"
sys.path.insert(0, str(HERE))
DATA = HERE  # carpeta con dict_data_*.py; se cambia con --data-dir

LEVELS = {
    "01": ("1-basico", "1.º básico"), "02": ("2-basico", "2.º básico"), "03": ("3-basico", "3.º básico"),
    "04": ("4-basico", "4.º básico"), "05": ("5-basico", "5.º básico"), "06": ("6-basico", "6.º básico"),
    "07": ("7-basico", "7.º básico"), "08": ("8-basico", "8.º básico"), "09": ("1-medio", "1.º medio"),
    "10": ("2-medio", "2.º medio"), "11": ("3-medio", "3.º medio"), "12": ("4-medio", "4.º medio"),
}
# Diccionarios para personas jóvenes y adultas (EPJA): solo inglés, un archivo por nivel de la modalidad.
EPJA_LEVELS = {
    "epja-nb2": ("epja-basica-n2", "EPJA Educación Básica Nivel 2 (5.º y 6.º básico)"),
}
ES_WORD_FIELDS = 8
ES_VERB_FIELDS = 10
EN_WORD_FIELDS = 9
EN_VERB_FIELDS = 9


def previous_note(slug: str, filename: str) -> str:
    order = [s for s, _ in LEVELS.values()]
    i = order.index(slug)
    if i == 0:
        return "Es el primer nivel: aquí empieza el vocabulario."
    prev = order[i - 1]
    name = dict(LEVELS.values())[prev]
    return (f"Las palabras de los niveles anteriores siguen vigentes y están en sus propios diccionarios "
            f"(por ejemplo, [{name}](../{prev}/{filename})); aquí solo aparecen las palabras nuevas.")


def fold(text: str) -> str:
    """Clave de orden: sin tildes, sin mayúsculas; la ñ va justo después de la n."""
    text = text.lower().replace("ñ", "n~")
    return "".join(c for c in unicodedata.normalize("NFD", text) if unicodedata.category(c) != "Mn")


def rows(block: str, fields: int, label: str) -> list[list[str]]:
    out = []
    for number, line in enumerate(block.strip().splitlines(), 1):
        if not line.strip():
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) != fields:
            raise SystemExit(f"{label} línea {number}: se esperaban {fields} campos y hay {len(parts)}: {line[:60]}")
        if any(not p for p in parts):
            raise SystemExit(f"{label} línea {number}: hay un campo vacío: {line[:60]}")
        out.append(parts)
    return out


def check_syllables(rows_, label: str) -> None:
    """Las sílabas unidas deben reconstruir la palabra (salvo siglas y símbolos, que se leen por letras)."""
    import re
    clean = lambda t: re.sub(r"[^a-záéíóúüñ]", "", t.lower())
    bad = [r[0] for r in rows_ if clean(r[1]) != clean(r[0]) and not (r[0].isupper() or r[0] in {"pH", "rayos X"})]
    if bad:
        raise SystemExit(f"{label}: sílabas que no reconstruyen la palabra: {bad[:10]}")


def esc(text: str) -> str:
    return text.replace("|", "\\|")


def letter_of(word: str) -> str:
    first = fold(word)[0]
    return first.upper() if first.isalpha() else "#"


def spanish(module, label: str) -> str:
    words = sorted(rows(module.PALABRAS, ES_WORD_FIELDS, label + " palabras"), key=lambda r: (fold(r[0]), r[2]))
    verbs = sorted(rows(module.VERBOS, ES_VERB_FIELDS, label + " verbos"), key=lambda r: fold(r[0]))
    keys = [(r[0].lower(), r[2]) for r in words]
    if len(keys) != len(set(keys)):
        dupes = sorted({k for k in keys if keys.count(k) > 1})
        raise SystemExit(f"{label}: palabras repetidas con la misma clase: {dupes}")
    verb_names = [r[0].lower() for r in verbs]
    if len(verb_names) != len(set(verb_names)):
        raise SystemExit(f"{label}: verbos repetidos")
    check_syllables(words, label)
    check_syllables([[r[0], r[1]] for r in verbs], label)
    return render_spanish(words, verbs, module.NIVEL)


def render_spanish(words, verbs, nivel_slug: str) -> str:
    nivel = next(name for slug, name in LEVELS.values() if slug == nivel_slug)
    prev_note = previous_note(nivel_slug, "espanol.md")
    lines = [
        f"# Diccionario de español · {nivel}", "",
        "[Volver a los diccionarios](../README.md) · "
        f"[Ver el diccionario de inglés de {nivel}](ingles.md)", "",
        f"Este diccionario reúne **{len(words)} palabras nuevas** y **{len(verbs)} verbos nuevos** que una persona de {nivel} "
        f"necesita para leer, escribir y conversar con seguridad. {prev_note} Cada palabra tiene su separación en sílabas, "
        "una explicación sencilla, sinónimos (palabras parecidas), antónimos (palabras opuestas) y una oración de ejemplo. "
        "Los verbos muestran cómo cambian en presente, pasado y futuro.", "",
        "> **Importante:** es una selección propia de este proyecto, escrita con palabras sencillas. "
        "No es un listado oficial del Ministerio de Educación ni reemplaza al diccionario de la Real Academia Española. "
        "Un guion (-) significa que no hay sinónimo o antónimo sencillo para este nivel.", "",
        "## Cómo usarlo", "",
        "1. Busca la palabra por su letra inicial en la sección alfabética.",
        "2. Lee el significado y repite la oración de ejemplo en voz alta.",
        "3. Para un verbo, ve a la sección **Verbos** y mira sus tres tiempos.",
        "4. Escribe tus propias oraciones con las palabras nuevas.", "",
        "## Palabras por orden alfabético", "",
    ]
    by_letter: dict[str, list] = {}
    for row in words:
        by_letter.setdefault(letter_of(row[0]), []).append(row)
    for letter in sorted(by_letter):
        lines += [f"### {letter}", "", "| Palabra | Sílabas | Clase | Significado | Sinónimos | Antónimos | Ejemplo |", "|---|---|---|---|---|---|---|"]
        for w, syl, cls, mean, syn, ant, ex, _tema in by_letter[letter]:
            lines.append(f"| **{esc(w)}** | {esc(syl)} | {esc(cls)} | {esc(mean)} | {esc(syn)} | {esc(ant)} | {esc(ex)} |")
        lines.append("")
    lines += [
        "## Verbos", "",
        "El pasado se muestra con «ayer» y el futuro con «mañana», siempre para él o ella. "
        "Algunos verbos cambian mucho (por ejemplo, **ir**: voy, va, fue, irá); fíjate en ellos.", "",
        "| Verbo | Sílabas | Significado | Yo (hoy) | Él o ella (hoy) | Él o ella (ayer) | Él o ella (mañana) | Sinónimos | Antónimos | Ejemplo |",
        "|---|---|---|---|---|---|---|---|---|---|",
    ]
    for inf, syl, mean, yo, el, ayer, man, syn, ant, ex in verbs:
        lines.append(f"| **{esc(inf)}** | {esc(syl)} | {esc(mean)} | {esc(yo)} | {esc(el)} | {esc(ayer)} | {esc(man)} | {esc(syn)} | {esc(ant)} | {esc(ex)} |")
    lines += ["", "## Palabras por tema", ""]
    by_theme: dict[str, list[str]] = {}
    for row in words:
        by_theme.setdefault(row[7], []).append(row[0])
    for theme in sorted(by_theme, key=fold):
        names = sorted(dict.fromkeys(by_theme[theme]), key=fold)
        lines.append(f"- **{theme.capitalize()}** ({len(names)}): " + ", ".join(names) + ".")
    lines.append("")
    return "\n".join(lines)


def english(module, label: str) -> str:
    words = sorted(rows(module.PALABRAS, EN_WORD_FIELDS, label + " words"), key=lambda r: (fold(r[0]), r[1]))
    verbs = sorted(rows(module.VERBOS, EN_VERB_FIELDS, label + " verbs"), key=lambda r: fold(r[0]))
    keys = [(r[0].lower(), r[1]) for r in words]
    if len(keys) != len(set(keys)):
        raise SystemExit(f"{label}: palabras repetidas con la misma clase: {sorted({k for k in keys if keys.count(k) > 1})}")
    return render_english(words, verbs, module.NIVEL)


def render_english_epja(words, verbs, nivel_slug: str) -> str:
    nivel = next(name for slug, name in EPJA_LEVELS.values() if slug == nivel_slug)
    lines = [
        f"# Diccionario de inglés · {nivel}", "",
        "[Volver a los diccionarios](../README.md)", "",
        f"Este diccionario reúne **{len(words)} palabras nuevas** y **{len(verbs)} verbos nuevos** en inglés para personas jóvenes y adultas "
        "que estudian Inglés en la Educación de Personas Jóvenes y Adultas (nivel A1 a A2): vocabulario de trabajo, trámites, "
        "familia, barrio, transporte, comida y salud sencilla. Las palabras básicas comunes (colores, números, familia cercana, rutinas simples, "
        "verbos como go, eat o work) NO se repiten aquí: ya están en los diccionarios de [1.º básico](../1-basico/ingles.md) a "
        "[6.º básico](../6-basico/ingles.md) y de los niveles siguientes. Cada entrada trae la traducción al español, la pronunciación, "
        "el significado explicado en español y una oración de ejemplo con su traducción.", "",
        "> **Sobre la pronunciación:** la columna «Cómo suena» es una aproximación escrita para quien habla español; "
        "la sílaba que se dice más fuerte va en MAYÚSCULAS. La columna IPA usa el alfabeto fonético internacional con la "
        "variante estadounidense. Ninguna de las dos reemplaza escuchar a un hablante nativo o una grabación: "
        "este proyecto todavía no incluye audio.", "",
        "> **Importante:** es una selección propia de este proyecto, escrita por IA y sin revisión de especialistas en enseñanza de idiomas. "
        "No es un listado oficial del Ministerio de Educación ni reemplaza a un diccionario publicado. Las oraciones de ejemplo son inventadas.", "",
        "## Cómo usarlo", "",
        "1. Busca la palabra por su letra inicial.",
        "2. Lee cómo suena y repítela en voz alta tres veces.",
        "3. Lee la oración de ejemplo en inglés y luego en español.",
        "4. Inventa una oración parecida sobre tu trabajo, tu familia o tu barrio.", "",
        "## Palabras por orden alfabético", "",
    ]
    return _english_body(lines, words, verbs)


def render_english(words, verbs, nivel_slug: str) -> str:
    if any(slug == nivel_slug for slug, _ in EPJA_LEVELS.values()):
        return render_english_epja(words, verbs, nivel_slug)
    nivel = next(name for slug, name in LEVELS.values() if slug == nivel_slug)
    prev_note = previous_note(nivel_slug, "ingles.md")
    lines = [
        f"# Diccionario de inglés · {nivel}", "",
        "[Volver a los diccionarios](../README.md) · "
        f"[Ver el diccionario de español de {nivel}](espanol.md)", "",
        f"Este diccionario reúne **{len(words)} palabras nuevas** y **{len(verbs)} verbos nuevos** en inglés para {nivel}. "
        f"{prev_note} Cada entrada trae la traducción al español, la pronunciación, el significado explicado en español "
        "y una oración de ejemplo con su traducción.", "",
        "> **Sobre la pronunciación:** la columna «Cómo suena» es una aproximación escrita para quien habla español; "
        "la sílaba que se dice más fuerte va en MAYÚSCULAS. La columna IPA usa el alfabeto fonético internacional con la "
        "variante estadounidense. Ninguna de las dos reemplaza escuchar a un hablante nativo o una grabación: "
        "este proyecto todavía no incluye audio.", "",
        "> **Importante:** es una selección propia de este proyecto. No es un listado oficial del Ministerio de Educación "
        "ni reemplaza a un diccionario publicado.", "",
        "## Cómo usarlo", "",
        "1. Busca la palabra por su letra inicial.",
        "2. Lee cómo suena y repítela en voz alta tres veces.",
        "3. Lee la oración de ejemplo en inglés y luego en español.",
        "4. Inventa una oración parecida con otra palabra de la lista.", "",
        "## Palabras por orden alfabético", "",
    ]
    return _english_body(lines, words, verbs)


def _english_body(lines, words, verbs) -> str:
    by_letter: dict[str, list] = {}
    for row in words:
        by_letter.setdefault(letter_of(row[0]), []).append(row)
    for letter in sorted(by_letter):
        lines += [f"### {letter}", "", "| English | Clase | IPA | Cómo suena | En español | Significado | Ejemplo | Traducción |", "|---|---|---|---|---|---|---|---|"]
        for w, cls, ipa, fig, es, mean, ex_en, ex_es, _tema in by_letter[letter]:
            lines.append(f"| **{esc(w)}** | {esc(cls)} | {esc(ipa)} | {esc(fig)} | {esc(es)} | {esc(mean)} | {esc(ex_en)} | {esc(ex_es)} |")
        lines.append("")
    lines += [
        "## Verbos", "",
        "Cada verbo se muestra en su forma base y en pasado simple. Fíjate: en inglés el verbo casi no cambia con la persona; "
        "con **he**, **she** e **it** se agrega una «s» (**runs**, **eats**).", "",
        "| Verb | IPA | Pasado | Pasado en español | En español | Él o ella hoy | Significado | Ejemplo | Traducción |",
        "|---|---|---|---|---|---|---|---|---|",
    ]
    for base, ipa, past, past_es, es, el, mean, ex_en, ex_es in verbs:
        lines.append(f"| **{esc(base)}** | {esc(ipa)} | {esc(past)} | {esc(past_es)} | {esc(es)} | {esc(el)} | {esc(mean)} | {esc(ex_en)} | {esc(ex_es)} |")
    lines += ["", "## Palabras por tema", ""]
    by_theme: dict[str, list[str]] = {}
    for row in words:
        by_theme.setdefault(row[8], []).append(row[0])
    for theme in sorted(by_theme, key=fold):
        names = sorted(dict.fromkeys(by_theme[theme]), key=fold)
        lines.append(f"- **{theme.capitalize()}** ({len(names)}): " + ", ".join(names) + ".")
    lines.append("")
    return "\n".join(lines)


def main(argv: list[str]) -> int:
    global DATA
    check_only = "--check" in argv
    if "--data-dir" in argv:
        DATA = Path(argv[argv.index("--data-dir") + 1]).resolve()
        sys.path.insert(0, str(DATA))
    summary = []
    seen_es: dict[tuple[str, str], str] = {}
    seen_en: dict[tuple[str, str], str] = {}
    problems: list[str] = []
    for code, (slug, name) in LEVELS.items():
        es_name, en_name = f"dict_data_es_{code}", f"dict_data_en_{code}"
        if not (DATA / f"{es_name}.py").exists() or not (DATA / f"{en_name}.py").exists():
            continue
        es_mod, en_mod = importlib.import_module(es_name), importlib.import_module(en_name)
        for r in rows(es_mod.PALABRAS, ES_WORD_FIELDS, ""):
            key = (r[0].lower(), r[2])
            if key in seen_es:
                problems.append(f"español {name}: «{r[0]}» ({r[2]}) ya estaba en {seen_es[key]}")
            seen_es.setdefault(key, name)
        for r in rows(es_mod.VERBOS, ES_VERB_FIELDS, ""):
            key = (r[0].lower(), "verbo")
            if key in seen_es:
                problems.append(f"español {name}: verbo «{r[0]}» ya estaba en {seen_es[key]}")
            seen_es.setdefault(key, name)
        for r in rows(en_mod.PALABRAS, EN_WORD_FIELDS, ""):
            key = (r[0].lower(), r[1])
            if key in seen_en:
                problems.append(f"inglés {name}: «{r[0]}» ({r[1]}) ya estaba en {seen_en[key]}")
            seen_en.setdefault(key, name)
        for r in rows(en_mod.VERBOS, EN_VERB_FIELDS, ""):
            key = (r[0].lower(), "verb")
            if key in seen_en:
                problems.append(f"inglés {name}: verbo «{r[0]}» ya estaba en {seen_en[key]}")
            seen_en.setdefault(key, name)
        es_text = spanish(es_mod, es_name)
        en_text = english(en_mod, en_name)
        n_es = len(rows(es_mod.PALABRAS, ES_WORD_FIELDS, "")), len(rows(es_mod.VERBOS, ES_VERB_FIELDS, ""))
        n_en = len(rows(en_mod.PALABRAS, EN_WORD_FIELDS, "")), len(rows(en_mod.VERBOS, EN_VERB_FIELDS, ""))
        summary.append((slug, name, n_es, n_en))
        if not check_only:
            folder = OUT / slug
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "espanol.md").write_text(es_text, encoding="utf-8", newline="\n")
            (folder / "ingles.md").write_text(en_text, encoding="utf-8", newline="\n")
    epja_summary = []
    for code, (slug, name) in EPJA_LEVELS.items():
        en_name = f"dict_data_en_{code.replace('-', '_')}"
        if not (DATA / f"{en_name}.py").exists():
            continue
        en_mod = importlib.import_module(en_name)
        for r in rows(en_mod.PALABRAS, EN_WORD_FIELDS, ""):
            key = (r[0].lower(), r[1])
            if key in seen_en:
                problems.append(f"inglés {name}: «{r[0]}» ({r[1]}) ya estaba en {seen_en[key]}")
            seen_en.setdefault(key, name)
        for r in rows(en_mod.VERBOS, EN_VERB_FIELDS, ""):
            key = (r[0].lower(), "verb")
            if key in seen_en:
                problems.append(f"inglés {name}: verbo «{r[0]}» ya estaba en {seen_en[key]}")
            seen_en.setdefault(key, name)
        en_text = english(en_mod, en_name)
        epja_summary.append((slug, name, len(rows(en_mod.PALABRAS, EN_WORD_FIELDS, "")), len(rows(en_mod.VERBOS, EN_VERB_FIELDS, ""))))
        if not check_only:
            folder = OUT / slug
            folder.mkdir(parents=True, exist_ok=True)
            (folder / "ingles.md").write_text(en_text, encoding="utf-8", newline="\n")
    if not summary:
        print("No hay datos de diccionarios.")
        return 1
    if problems:
        print(chr(10).join(problems))
        print(f"{len(problems)} palabras repetidas entre niveles")
        return 1
    if not check_only:
        write_index(summary, epja_summary)
    for slug, name, n_es, n_en in summary:
        print(f"{name}: español {n_es[0]} palabras + {n_es[1]} verbos · inglés {n_en[0]} palabras + {n_en[1]} verbos")
    for slug, name, n_w, n_v in epja_summary:
        print(f"{name}: inglés {n_w} palabras + {n_v} verbos")
    return 0


def write_index(summary, epja_summary=()) -> None:
    lines = [
        "# Diccionarios por nivel: español e inglés", "",
        "[Volver al README principal](../../README.md) · [Glosario del proyecto](../GLOSARIO.md)", "",
        "Para cada nivel, de 1.º básico a 4.º medio, hay dos diccionarios que crecen año a año: uno de **español** "
        "(significado, sílabas, sinónimos, antónimos y tiempos verbales) y uno de **inglés** "
        "(traducción, pronunciación, significado en español y ejemplos). Cada nivel retoma lo del anterior y suma palabras nuevas.", "",
        "> **Alcance:** son selecciones propias del proyecto para apoyar el aprendizaje. No son listados oficiales del Ministerio "
        "de Educación, no están revisados por especialistas en lingüística o en enseñanza de idiomas y la pronunciación escrita "
        "es aproximada. Se publican nivel por nivel; los niveles que faltan aparecen como pendientes.", "",
        "| Nivel | Español: palabras + verbos nuevos | Inglés: palabras + verbos nuevos | Acumulado (es / en) | Abrir |", "|---|---:|---:|---:|---|",
    ]
    done = {slug: (name, n_es, n_en) for slug, name, n_es, n_en in summary}
    cum_es = cum_en = 0
    for slug, name in LEVELS.values():
        if slug in done:
            _n, n_es, n_en = done[slug]
            cum_es += n_es[0] + n_es[1]
            cum_en += n_en[0] + n_en[1]
            lines.append(f"| {name} | {n_es[0]} + {n_es[1]} | {n_en[0]} + {n_en[1]} | {cum_es} / {cum_en} | [Español]({slug}/espanol.md) · [Inglés]({slug}/ingles.md) |")
        else:
            lines.append(f"| {name} | pendiente | pendiente | - | en preparación |")
    if epja_summary:
        lines += [
            "", "## Educación de Personas Jóvenes y Adultas (EPJA)", "",
            "Para las personas que estudian Inglés en la modalidad EPJA hay un diccionario propio, de **inglés**, con vocabulario adulto "
            "(trabajo, trámites, familia, barrio, transporte, comida y salud sencilla). No repite las palabras de los diccionarios de "
            "1.º básico a 4.º medio: las palabras básicas comunes están en los diccionarios de 1.º a 6.º básico. Mismo alcance que los demás: "
            "selección propia, sin revisión de especialistas y con pronunciación aproximada, sin audio.", "",
            "| Nivel | Inglés: palabras + verbos nuevos | Abrir |", "|---|---:|---|",
        ]
        for slug, name, n_w, n_v in epja_summary:
            lines.append(f"| {name} | {n_w} + {n_v} | [Inglés]({slug}/ingles.md) |")
    lines.append("")
    (OUT / "README.md").write_text("\n".join(lines), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
