"""Generate the curriculum catalog, index, and 192 class guides from one source."""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CURRICULUM = ROOT / "curriculum"

LEVELS = [
    {
        "number": 1,
        "name": "Fundamentos",
        "purpose": "reconocer conceptos, activos, titulares y fuentes antes de recomendar una acción",
        "practice": "clasificar un caso breve y separar hechos, supuestos y preguntas abiertas",
        "evidence": "ficha de análisis con fuente primaria y conclusión acotada",
    },
    {
        "number": 2,
        "name": "Aplicación",
        "purpose": "aplicar reglas a repositorios, contenidos y canales de distribución concretos",
        "practice": "resolver un escenario con alternativas, obligaciones y criterio de aceptación",
        "evidence": "decisión reproducible con matriz y archivos de cumplimiento",
    },
    {
        "number": 3,
        "name": "Ingeniería",
        "purpose": "convertir decisiones en arquitectura, automatización y evidencia de release",
        "practice": "diseñar un control que detecte una desviación sin sustituir el juicio humano",
        "evidence": "control ejecutable, prueba negativa y registro de excepción",
    },
    {
        "number": 4,
        "name": "Gobierno y especialización",
        "purpose": "gobernar riesgo, casos transfronterizos y decisiones de alto impacto",
        "practice": "defender una recomendación ante revisión técnica, de negocio y jurídica",
        "evidence": "memo ejecutivo con riesgos, responsables, vencimientos y escalamiento",
    },
]

SUBJECTS = [
    {
        "slug": "fundamentos-derecho-autor",
        "name": "Fundamentos de derecho de autor",
        "frame": "El análisis parte del activo, la titularidad y el acto que se pretende realizar; la licencia es una autorización dentro de ese mapa.",
        "risk": "confundir acceso público con permiso o atribuir derechos a quien no los controla",
        "topics": [
            "Idea, expresión y originalidad", "Autoría y titularidad", "Derechos morales y patrimoniales",
            "Reproducción, adaptación y distribución", "Duración y dominio público", "Cita, enseñanza y otras excepciones",
            "Obras por encargo y relación laboral", "Obras en colaboración y colectivas", "Adaptaciones, traducciones y colecciones",
            "Cadena de titularidad y evidencia", "Análisis multijurisdiccional", "Controversia y preservación de pruebas",
        ],
    },
    {
        "slug": "licencias-software",
        "name": "Licencias de software",
        "frame": "Cada familia combina concesiones, condiciones, exclusiones y remedios; la versión exacta importa.",
        "risk": "elegir por popularidad o resumir licencias distintas como si fueran equivalentes",
        "topics": [
            "Anatomía de una licencia", "MIT y BSD", "Apache-2.0 y concesión de patentes",
            "GPL y fuente correspondiente", "LGPL y bibliotecas", "MPL y copyleft por archivo",
            "AGPL y servicios de red", "Excepciones y licencias secundarias", "Open source frente a source-available",
            "Cambio de licencia y consentimiento", "Dual licensing y modelo comercial", "Selección y memo de decisión",
        ],
    },
    {
        "slug": "compatibilidad",
        "name": "Compatibilidad y composición",
        "frame": "Compatibilidad significa poder cumplir simultáneamente las condiciones aplicables a una combinación y distribución concretas.",
        "risk": "declarar compatible una lista de licencias sin describir enlace, modificación ni entrega",
        "topics": [
            "Qué significa compatibilidad", "Permisiva con permisiva", "Permisiva con copyleft",
            "Copyleft fuerte y débil", "Enlace estático, dinámico e IPC", "Plugins, procesos y límites de componente",
            "Código generado y plantillas", "Snippets y ejemplos", "Frontend, backend y artefactos combinados",
            "Contenedores y distribuciones agregadas", "Remediación de incompatibilidades", "Dictamen de arquitectura y licencia",
        ],
    },
    {
        "slug": "dependencias-terceros",
        "name": "Dependencias y terceros",
        "frame": "La procedencia y la versión conectan cada componente con sus obligaciones y avisos verificables.",
        "risk": "auditar solo dependencias directas o perder licencias y avisos durante el empaquetado",
        "topics": [
            "Dependencias directas y transitivas", "Build, desarrollo y runtime", "Lockfiles y versión efectiva",
            "Avisos de copyright", "Archivos NOTICE", "Vendoring y forks",
            "Paquetes abandonados o sin licencia", "Assets, fuentes e iconos", "SDK, API y términos externos",
            "Revisión de actualización", "Sustitución y aislamiento", "Registro consolidado de terceros",
        ],
    },
    {
        "slug": "contenido-creative-commons",
        "name": "Contenido y Creative Commons",
        "frame": "El contenido exige delimitar obra original, material incorporado, adaptación, colección y atribución.",
        "risk": "aplicar una licencia Creative Commons a software o material de terceros sin autoridad",
        "topics": [
            "Las seis licencias Creative Commons", "Atribución TASL", "ShareAlike y compatibilidad",
            "NonCommercial y contexto", "NoDerivatives y adaptaciones", "CC0 y dominio público",
            "Traducciones y localización", "Colecciones y obras derivadas", "Imágenes, audio y video",
            "Recursos educativos abiertos", "Publicación en LMS y web", "Paquete editorial auditable",
        ],
    },
    {
        "slug": "datos-bases",
        "name": "Datos y bases de datos",
        "frame": "Datos, selección, estructura, documentación y acceso pueden tener condiciones distintas.",
        "risk": "suponer que todo dato factual puede recopilarse, redistribuirse o reutilizarse sin límites",
        "topics": [
            "Hechos, estructura y compilación", "Procedencia y linaje", "Consentimiento y finalidad",
            "CC0 y licencias abiertas", "Open Data Commons", "Datos públicos y términos de portal",
            "Datos personales y minimización", "Datos sensibles y de menores", "Scraping, acceso y contrato",
            "Mezcla y transformación de datasets", "Publicación y data card", "Retiro, corrección y trazabilidad",
        ],
    },
    {
        "slug": "inteligencia-artificial",
        "name": "IA, corpus y modelos",
        "frame": "Código, corpus, checkpoints, pesos, configuración, documentación y salidas son artefactos diferentes.",
        "risk": "trasladar automáticamente la licencia de un componente a todo el sistema de IA",
        "topics": [
            "Mapa de artefactos de IA", "Corpus de entrenamiento", "Etiquetas y anotaciones",
            "Licencias de modelos y pesos", "Código de entrenamiento e inferencia", "Model cards y data cards",
            "RAG y documentos recuperados", "Embeddings y bases vectoriales", "Salidas y revisión humana",
            "Términos de proveedores", "Evaluación de procedencia a escala", "Expediente de modelo",
        ],
    },
    {
        "slug": "marcas-identidad",
        "name": "Marcas e identidad",
        "frame": "Las marcas protegen signos que distinguen origen; una licencia de copyright no concede automáticamente su uso.",
        "risk": "crear confusión sobre afiliación, edición oficial o respaldo del titular",
        "topics": [
            "Función de una marca", "Nombre, logo y trade dress", "Uso referencial y atribución",
            "Búsqueda preliminar", "Clasificación de productos y servicios", "Política de uso de marca",
            "Forks y nombres derivados", "Dominios y redes sociales", "Coexistencia y autorización",
            "Marca en comunidades open source", "Observancia y evidencia", "Estrategia de portafolio de marca",
        ],
    },
    {
        "slug": "patentes-propiedad-industrial",
        "name": "Patentes y propiedad industrial",
        "frame": "Patentes, diseños y otros títulos requieren novedad, alcance territorial y estrategia distinta del copyright.",
        "risk": "confundir publicación, licencia de código y libertad para operar con ausencia de riesgo de patente",
        "topics": [
            "Invención frente a obra", "Novedad y divulgación", "Reivindicaciones y alcance",
            "Concesiones de patente en licencias", "Cláusulas de represalia", "Búsqueda de estado de la técnica",
            "Software y patentabilidad por jurisdicción", "Diseños industriales", "Modelos de utilidad",
            "Freedom to operate", "Estrategia de publicación defensiva", "Escalamiento de riesgo de patente",
        ],
    },
    {
        "slug": "contratos-secretos",
        "name": "Contratos y secretos empresariales",
        "frame": "Contratos y medidas de confidencialidad pueden definir derechos y obligaciones que no aparecen en la licencia pública.",
        "risk": "publicar información confidencial o aceptar términos incompatibles con la distribución prevista",
        "topics": [
            "Contrato, licencia y política", "NDA y alcance", "Secreto empresarial y medidas razonables",
            "Cesión y licencia de derechos", "Garantías e indemnidades", "Limitación de responsabilidad",
            "SaaS, API y términos de servicio", "Procurement y componentes externos", "Licenciamiento comercial",
            "Terminación y efectos", "Registro de autorizaciones", "Negociación basada en riesgos",
        ],
    },
    {
        "slug": "contribuciones-comunidad",
        "name": "Contribuciones y comunidad",
        "frame": "Un proyecto sostenible define qué derechos recibe, cómo acepta aportes y cómo cambia sus reglas.",
        "risk": "acumular contribuciones sin una cadena clara para corregir o relicenciar el proyecto",
        "topics": [
            "Inbound y outbound", "Developer Certificate of Origin", "Contributor License Agreement",
            "Política de contribución", "Firmas y trazabilidad", "Bots y contribuciones automatizadas",
            "Gobierno de mantenedores", "Cambio de licencia comunitario", "Código de terceros en pull requests",
            "Fundaciones y neutralidad", "Archivo y sucesión del proyecto", "Auditoría de contribuciones",
        ],
    },
    {
        "slug": "spdx-sbom-reuse",
        "name": "SPDX, SBOM y REUSE",
        "frame": "Los estándares hacen intercambiable la evidencia, pero su calidad depende del inventario y contexto de origen.",
        "risk": "tratar un SBOM incompleto o un identificador detectado como decisión jurídica final",
        "topics": [
            "Identificadores SPDX", "Expresiones AND y OR", "Excepciones SPDX",
            "Anatomía de un SBOM", "SPDX como formato de SBOM", "CycloneDX y alcance complementario",
            "REUSE a nivel de archivo", "Copyright y licencia por ruta", "Generated files y vendoring",
            "Calidad y cobertura del inventario", "Firma y procedencia del artefacto", "Expediente interoperable de release",
        ],
    },
    {
        "slug": "automatizacion-policy-code",
        "name": "Automatización y policy as code",
        "frame": "La automatización verifica hechos observables y deriva el resto a una decisión con responsable.",
        "risk": "convertir una heurística o escáner en aprobación automática sin revisar falsos negativos",
        "topics": [
            "Qué puede automatizarse", "Estados aceptar, revisar y bloquear", "Esquemas y validación",
            "Detección de archivos sin licencia", "Cambios de dependencias en PR", "Reglas por ruta y artefacto",
            "Excepciones con vencimiento", "Pruebas negativas de política", "Evidencia en CI",
            "Integración con release", "Observabilidad del cumplimiento", "Diseño de un gate defendible",
        ],
    },
    {
        "slug": "distribucion-release",
        "name": "Distribución y release",
        "frame": "Las obligaciones se evalúan sobre lo que efectivamente recibe o puede usar otra persona.",
        "risk": "revisar el repositorio y olvidar binarios, instaladores, imágenes, apps o paquetes publicados",
        "topics": [
            "Uso interno frente a distribución", "Distribución de código fuente", "Binarios e instaladores",
            "Contenedores e imágenes base", "Paquetes y registries", "Aplicaciones móviles y tiendas",
            "SaaS y acceso remoto", "Firmware y dispositivos", "Documentación y bundles offline",
            "Fuente correspondiente y ofertas", "Avisos visibles al usuario", "Checklist y expediente de release",
        ],
    },
    {
        "slug": "gobernanza-auditoria",
        "name": "Gobernanza, auditoría e incidentes",
        "frame": "Un programa maduro asigna decisiones, conserva evidencia, mide deuda y aprende de incidentes.",
        "risk": "tener documentos correctos sin responsables, revisión periódica ni capacidad de respuesta",
        "topics": [
            "RACI de licenciamiento", "Política y estándar", "Registro de decisiones",
            "Métricas de cobertura y deuda", "Muestreo y auditoría", "Due diligence",
            "Excepciones y aceptación de riesgo", "Incidente de licencia", "Contención y remediación",
            "Adquisiciones y M&A", "Programa OpenChain", "Capstone de gobierno",
        ],
    },
    {
        "slug": "chile-internacional",
        "name": "Chile y contexto internacional",
        "frame": "Las licencias globales operan sobre derechos territoriales, contratos y procedimientos locales.",
        "risk": "generalizar una regla extranjera o una excepción sin comprobar su vigencia y contexto en Chile",
        "topics": [
            "Sistema chileno de propiedad intelectual", "Ley 17.336 y derechos de autor", "Registro en el DDI",
            "Excepciones de cita y enseñanza", "Ley de propiedad industrial", "INAPI y marcas",
            "Patentes y diseños en Chile", "Tratados y convenios relevantes", "Software, contratos y empleo",
            "Transferencias y operación internacional", "Conflicto de leyes y foro", "Memo chileno con fuentes primarias",
        ],
    },
]


def slugify(value: str) -> str:
    normalized = unicodedata.normalize("NFKD", value).encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]+", "-", normalized.lower()).strip("-")


def build_catalog() -> list[dict[str, object]]:
    classes: list[dict[str, object]] = []
    class_id = 1
    for level in LEVELS:
        start = (int(level["number"]) - 1) * 3
        for subject_index, subject in enumerate(SUBJECTS, start=1):
            for topic in subject["topics"][start : start + 3]:
                slug = f"class-{class_id:03d}-{slugify(topic)}"
                classes.append(
                    {
                        "id": class_id,
                        "code": f"LIP-{class_id:03d}",
                        "topic": topic,
                        "subject": subject["name"],
                        "subject_id": subject_index,
                        "level": level["number"],
                        "level_name": level["name"],
                        "outcome": f"{level['purpose'].capitalize()} en el tema «{topic}».",
                        "practice": f"{level['practice'].capitalize()} aplicado a «{topic}».",
                        "evidence": level["evidence"],
                        "path": f"curriculum/level-{level['number']:02d}/{slug}/README.md",
                    }
                )
                class_id += 1
    return classes


def class_markdown(item: dict[str, object], subject: dict[str, object], level: dict[str, object]) -> str:
    root = "../../../"
    return f"""# {item['code']} — {item['topic']}

| Campo | Valor |
|---|---|
| Asignatura | {item['subject']} |
| Nivel | {item['level']} · {item['level_name']} |
| Tema | {item['topic']} |
| Resultado | {item['outcome']} |
| Evidencia | {item['evidence']} |

## Por qué importa

{subject['frame']} En esta clase el foco es **{item['topic']}**. El error que se busca prevenir es
{subject['risk']}.

## Pregunta rectora

¿Qué hechos debes poder probar antes de tomar una decisión sobre **{item['topic']}**, y qué parte de
la respuesta depende del activo, del titular, del uso o de la forma de distribución?

## Método

1. Delimita el activo, versión y commit analizados.
2. Identifica titular, fuente y texto aplicable; conserva enlace y fecha.
3. Describe el acto previsto y quién recibirá el resultado.
4. Separa permiso, obligación, restricción, excepción y supuesto.
5. Compara al menos una alternativa y documenta por qué se descarta.
6. Formula la decisión con responsable y fecha de revisión.

## Práctica guiada

{item['practice']} Usa un repositorio o artefacto real y adjunta una fuente primaria. Si falta
evidencia, marca el punto como `PENDIENTE` o `CUARENTENA`; no completes la respuesta por intuición.

## Criterio de aceptación

- el activo y el acto están descritos sin ambigüedad;
- la fuente enlazada respalda la regla aplicada;
- hechos y supuestos aparecen separados;
- la conclusión indica alcance, responsable y próxima revisión;
- la evidencia entregada corresponde a: **{item['evidence']}**.

## Autoevaluación

1. ¿Qué cambiaría si no hubiera distribución?
2. ¿Qué dato faltante podría invertir la conclusión?
3. ¿Qué parte puede comprobar una herramienta y cuál exige juicio humano?

## Referencias y continuidad

- [Fuentes oficiales]({root}OFFICIAL_REFERENCES.md)
- [Matriz de decisión]({root}docs/DECISION_MATRIX.md)
- [Playbook de implementación]({root}docs/IMPLEMENTATION_PLAYBOOK.md)
- [Volver al currículo]({root}CURRICULUM.md)
"""


def curriculum_markdown(classes: list[dict[str, object]]) -> str:
    lines = [
        "# Currículo completo", "",
        "## 192 clases · 16 asignaturas · 4 niveles", "",
        "Cada clase corresponde a un único **tema**, una **asignatura** y un **nivel**. El catálogo",
        "JSON y las páginas de clase se generan desde `scripts/generate_curriculum.py`; la CI comprueba",
        "que no exista drift entre las tres superficies.", "",
    ]
    for level in LEVELS:
        lines.extend([
            f"## Nivel {level['number']} — {level['name']}", "",
            f"**Propósito:** {level['purpose']}.", "",
            "| Clase | Asignatura | Tema | Evidencia |", "|---:|---|---|---|",
        ])
        for item in classes:
            if item["level"] == level["number"]:
                lines.append(
                    f"| [{item['code']}]({item['path']}) | {item['subject']} | {item['topic']} | {item['evidence']} |"
                )
        lines.append("")
    lines.extend([
        "## Criterio de finalización", "",
        "El programa se completa con un expediente reproducible: inventario, titulares, fuentes,",
        "compatibilidad, avisos, decisiones, excepciones, pruebas y riesgos abiertos. Haber leído las",
        "clases sin producir la evidencia de cada nivel no satisface el criterio.", "",
    ])
    return "\n".join(lines)


def main() -> None:
    classes = build_catalog()
    CURRICULUM.mkdir(exist_ok=True)
    (CURRICULUM / "catalog.json").write_text(
        json.dumps({"schema_version": 1, "class_count": len(classes), "subjects": len(SUBJECTS), "levels": len(LEVELS), "classes": classes}, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    (ROOT / "CURRICULUM.md").write_text(curriculum_markdown(classes), encoding="utf-8")
    by_name = {subject["name"]: subject for subject in SUBJECTS}
    by_level = {level["number"]: level for level in LEVELS}
    for item in classes:
        target = ROOT / str(item["path"])
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(class_markdown(item, by_name[item["subject"]], by_level[item["level"]]), encoding="utf-8")
    print(f"Generated {len(classes)} classes across {len(SUBJECTS)} subjects and {len(LEVELS)} levels.")


if __name__ == "__main__":
    main()

