"""Secuencias docentes de la Educación de Personas Jóvenes y Adultas (EPJA, Fase C).

Todo lo oficial sale de `sources/epja-programas.json`, extraído de los programas de estudio EPJA publicados en
Currículum Nacional: por asignatura, cuatro módulos obligatorios con horas, cuatro actividades de desempeño por
módulo con su frase oficial, objetivos de aprendizaje (OA) nucleares, conocimientos esenciales y horas.

Cada ACTIVIDAD DE DESEMPEÑO es un «objetivo» del snapshot (16 por asignatura), con código estable
`EPJA-<SIGLA4>-<NB1|NB2|NM1|NM2|NM1y2>-OAD-NN`, donde NN = (módulo - 1) * 4 + n.º de desempeño (01 a 16).
El número de clases de cada objetivo son las horas pedagógicas del desempeño (no un número fijo): es un dato
del programa, no una decisión de este proyecto. Agregar una asignatura es solo agregar datos: la clave de la
fuente (por ejemplo `LECO_NB1`) y el snapshot (ver `C:\\dev\\_trabajo-cuadernos\\epja\\LEEME_EPJA.md`).

Los títulos de las clases son una derivación mecánica del desempeño oficial y de sus conocimientos esenciales; el
programa oficial es la fuente, y la progresión en clases es organización pedagógica interna, no una unidad oficial.
El dominio docente es «adultez»: situaciones de trabajo, familia, trámites, dinero, salud y vecindario, con lenguaje
respetuoso y sin suponer una escolaridad distinta de la del nivel.
"""
from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

try:
    import grade_three_middle_remaining_lessons as base
except ImportError:  # importado como paquete (tests)
    from scripts import grade_three_middle_remaining_lessons as base

ROOT = Path(__file__).resolve().parents[1]
SOURCE_PATH = ROOT / "sources/epja-programas.json"
SNAPSHOT = base.SNAPSHOT
SITE = "https://www.curriculumnacional.cl"
EPJA_ORDERS = {17, 18, 19, 20}

#: curso del snapshot: (course_order, nombre)
COURSES = {
    "epja-basica-n1": (17, "EPJA · Educación Básica Nivel 1 (1.º a 4.º básico)"),
    "epja-basica-n2": (18, "EPJA · Educación Básica Nivel 2 (5.º y 6.º básico)"),
    "epja-media-n1": (19, "EPJA · Educación Media Nivel 1 (1.º y 2.º medio)"),
    "epja-media-n2": (20, "EPJA · Educación Media Nivel 2 (3.º y 4.º medio)"),
}
#: sufijo de la clave del programa -> cursos donde se imparte (las instrumentales, Artes Visuales y Filosofía de media
#: se declaran para los dos niveles: mismo código y misma secuencia en ambos cursos)
LEVEL_TAGS = {
    "NB1": ("epja-basica-n1",),
    "NB2": ("epja-basica-n2",),
    "NM1": ("epja-media-n1",),
    "NM2": ("epja-media-n2",),
    "NM1y2": ("epja-media-n1", "epja-media-n2"),
}
LEVEL_LABEL = {"NB1": "Básica N1", "NB2": "Básica N2", "NM1": "Media N1", "NM2": "Media N2", "NM1y2": "Media N1 y N2"}
PRIOR_LEVEL = {
    "NB1": "su experiencia de vida y de trabajo",
    "NB2": "el Nivel 1 de Educación Básica de la modalidad y su experiencia de vida y de trabajo",
    "NM1": "la Educación Básica de la modalidad (o su equivalente) y su experiencia de vida y de trabajo",
    "NM2": "el Nivel 1 de Educación Media de la modalidad y su experiencia de vida y de trabajo",
    "NM1y2": "su experiencia de vida y de trabajo y lo que ya conoce de la asignatura",
}
LEVEL_CONTINUITY = {
    "NB1": "Este nivel no supone escolaridad previa: parte de lo que cada persona ya sabe por su vida y su trabajo.",
    "NB2": "Retoma lo trabajado en el Nivel 1 de Educación Básica de la modalidad y lo que cada persona ya sabe por su vida y su trabajo.",
    "NM1": "Retoma lo trabajado en la Educación Básica de la modalidad (o su equivalente) y la experiencia de vida y de trabajo de cada persona.",
    "NM2": "Retoma el Nivel 1 de Educación Media de la modalidad y la experiencia de vida y de trabajo de cada persona.",
    "NM1y2": "Se trabaja en los dos niveles de Educación Media de la modalidad y no supone una escolaridad distinta de la del nivel en que se cursa.",
}

# ---------------------------------------------------------------------------------------------------------------------
# Perfiles por asignatura (pedagógicos, no oficiales): vocabulario, errores frecuentes y escenas de la vida adulta.
# ---------------------------------------------------------------------------------------------------------------------
PROFILES_BY_SIGLA = {
    "LECO": {
        "continuity": "Retoma la lectura, la escritura y la conversación que las personas ya usan en su vida diaria (avisos, mensajes, boletas, formularios).",
        "vocabulary": "tema, idea principal, texto, propósito, destinatario, oración, párrafo, vocabulario, fuente confiable, opinión",
        "misconceptions": ("creer que leer rápido o en voz alta es lo mismo que comprender", "quedarse con un detalle suelto y no con la idea que organiza el texto", "dar por cierta una información sin revisar quién la publica y para qué"),
        "scenes": ("leer un aviso o un mensaje del trabajo", "completar un formulario de un trámite", "leer una indicación de salud o una receta", "escribir un mensaje a un familiar", "participar en una reunión de vecinos", "buscar información sobre un servicio"),
    },
    "MATE": {
        "continuity": "Retoma los números, las medidas y los datos que las personas ya usan al comprar, medir, repartir y calcular en su vida diaria.",
        "vocabulary": "cantidad, número, operación, estimación, medida, perímetro, área, tabla, gráfico, comprobación",
        "misconceptions": ("aplicar una operación sin entender qué pregunta el problema", "creer que el resultado es correcto porque lo dio la calculadora, sin estimarlo", "confundir una cantidad con el código o el orden de un número"),
        "scenes": ("calcular precios y vuelto en una compra", "medir un espacio de la casa o del lugar de trabajo", "repartir gastos del hogar", "leer una boleta de luz o de agua", "organizar turnos y horarios de trabajo", "leer un gráfico de un diario"),
    },
    "CNAT": {
        "continuity": "Retoma lo que las personas ya saben del cuerpo, la salud, los alimentos, la energía y el ambiente por su vida y su trabajo.",
        "vocabulary": "observación, pregunta, evidencia, variable, modelo, sistema, salud, ambiente, energía, conclusión",
        "misconceptions": ("tratar una creencia o un consejo popular como evidencia", "cambiar varias condiciones a la vez y concluir igual", "confundir una correlación con una causa"),
        "scenes": ("leer la etiqueta de un alimento o un remedio", "cuidar la salud de la familia", "ahorrar energía en la casa", "separar y reducir residuos", "prevenir riesgos en el trabajo", "informarse sobre el clima o el agua de la zona"),
    },
    "HGCS": {
        "continuity": "Retoma la historia vivida por las personas, sus familias y su territorio, y los derechos y deberes que ejercen en la comunidad.",
        "vocabulary": "fuente, época, territorio, causa, consecuencia, perspectiva, derecho, deber, ciudadanía, patrimonio",
        "misconceptions": ("explicar un hecho histórico con una sola causa", "juzgar el pasado solo con los valores de hoy", "tratar una fuente como la verdad completa y neutral"),
        "scenes": ("conversar con una persona mayor de la familia sobre el pasado", "leer un documento o una foto antigua del barrio", "informarse para votar o participar", "conocer los derechos del trabajo", "ubicarse en un mapa de la región", "participar en una organización vecinal"),
    },
    "INGL": {
        "continuity": "Parte del inglés que las personas ya encuentran en la calle, el trabajo y los medios (carteles, envases, canciones, mensajes).",
        "vocabulary": "propósito, palabra clave, significado, pronunciación, pregunta, respuesta, frase útil, cognado, contexto, repetición",
        "misconceptions": ("traducir palabra por palabra en vez de entender el sentido", "esperar hablar perfecto antes de intentar comunicarse", "creer que no se puede aprender inglés de adulto"),
        "scenes": ("leer un cartel o un envase con palabras en inglés", "presentarse y pedir algo de forma sencilla", "entender instrucciones de un aparato", "escuchar una canción o un mensaje", "completar un formulario sencillo", "buscar información en inglés para el trabajo"),
    },
    "LELI": {
        "continuity": "Retoma la lectura, la escritura y la conversación de la vida diaria y del trabajo, y las lleva a textos más extensos y a la literatura.",
        "vocabulary": "texto, género, propósito, audiencia, argumento, interpretación, recurso, evidencia textual, revisión, voz propia",
        "misconceptions": ("resumir un texto en vez de interpretarlo", "opinar sin apoyarse en lo que dice el texto", "corregir solo la ortografía sin revisar las ideas y la organización"),
        "scenes": ("leer una noticia y discutirla en el trabajo", "escribir una carta o un correo formal", "compartir un cuento o una canción de la familia", "preparar un discurso breve", "participar en un club de lectura del barrio", "redactar un currículum"),
    },
    "AVIS": {
        "continuity": "Retoma las imágenes, los colores y los objetos que las personas ya observan, hacen y usan en su vida diaria.",
        "vocabulary": "imagen, color, forma, composición, técnica, materialidad, intención, contexto, proceso, autoría",
        "misconceptions": ("creer que el arte es solo para quienes tienen talento", "copiar un modelo sin tomar decisiones propias", "confundir gusto personal con apreciación fundamentada"),
        "scenes": ("decorar o mejorar un espacio de la casa", "observar afiches y murales del barrio", "registrar una fiesta o tradición familiar", "diseñar un letrero para un negocio", "visitar una exposición o un centro cultural", "reutilizar materiales para crear"),
    },
    "FILO": {
        "continuity": "Retoma las preguntas sobre la vida, el trabajo y la convivencia que las personas ya se hacen por su experiencia.",
        "vocabulary": "pregunta, concepto, argumento, razón, ejemplo, objeción, perspectiva, valor, decisión, diálogo",
        "misconceptions": ("confundir una opinión sin razones con un argumento", "atacar a la persona en vez de examinar su idea", "creer que filosofar es tener una respuesta única y definitiva"),
        "scenes": ("decidir entre dos opciones difíciles en el trabajo", "conversar un desacuerdo en la familia", "preguntarse qué es una vida buena", "debatir una norma del barrio", "reflexionar sobre la justicia en un caso cotidiano", "pensar el sentido del trabajo"),
    },
    "PECO": {
        "continuity": "Retoma la forma en que las personas ya ordenan tareas, siguen instrucciones y usan aparatos digitales en su vida diaria.",
        "vocabulary": "problema, paso, secuencia, instrucción, condición, repetición, dato, patrón, error, algoritmo",
        "misconceptions": ("creer que pensar de forma computacional exige saber programar", "dar instrucciones ambiguas y suponer que se entienden", "no probar la solución antes de darla por buena"),
        "scenes": ("seguir las instrucciones de una receta o un aparato", "ordenar las tareas de la semana", "organizar una lista de clientes o de gastos", "usar una aplicación del celular para un trámite", "detectar un error en un procedimiento del trabajo", "explicar a otra persona cómo hacer algo paso a paso"),
    },
    "RPSO": {
        "continuity": "Retoma las responsabilidades que las personas ya asumen con su familia, su trabajo y su comunidad.",
        "vocabulary": "responsabilidad, compromiso, derecho, deber, consecuencia, convivencia, colaboración, respeto, diálogo, bien común",
        "misconceptions": ("creer que la responsabilidad es solo cumplir órdenes", "pensar que los derechos y los deberes son cosas separadas", "evitar el diálogo ante un conflicto en vez de abordarlo"),
        "scenes": ("repartir tareas en la familia", "cumplir un compromiso en el trabajo", "resolver un conflicto con un vecino", "participar en una junta de vecinos", "cuidar un espacio común", "apoyar a una persona que lo necesita"),
    },
    "EMEM": {
        "continuity": "Retoma lo que las personas ya saben de vender, hacer y buscar trabajo por su experiencia laboral.",
        "vocabulary": "oportunidad, idea, cliente, costo, precio, plan, empleabilidad, currículum, entrevista, habilidad",
        "misconceptions": ("creer que emprender es solo tener una buena idea y no planificar", "no calcular los costos antes de fijar un precio", "pensar que la experiencia de vida no cuenta como experiencia laboral"),
        "scenes": ("armar un currículum con la propia experiencia", "preparar una entrevista de trabajo", "evaluar una idea de negocio pequeño", "fijar el precio de un producto o servicio", "conocer los derechos del trabajo", "buscar ofertas de empleo y capacitación"),
    },
    "EFIN": {
        "continuity": "Retoma las decisiones de dinero que las personas ya toman todos los días: gastar, ahorrar, endeudarse y proteger a la familia.",
        "vocabulary": "ingreso, gasto, presupuesto, ahorro, deuda, interés, crédito, seguro, riesgo, meta financiera",
        "misconceptions": ("creer que sin ahorrar un monto grande no vale la pena ahorrar", "firmar un crédito sin comparar el costo total", "confundir una necesidad con un deseo al presupuestar"),
        "scenes": ("armar el presupuesto mensual del hogar", "comparar créditos antes de endeudarse", "revisar una cuenta o una boleta", "planificar un ahorro para una meta", "entender un seguro o la previsión", "detectar una oferta engañosa o un fraude"),
    },
}
DEFAULT_PROFILE = {
    "continuity": "Retoma lo que las personas ya saben de la asignatura por su vida y su trabajo.",
    "vocabulary": base.VOCABULARY["adultez"],
    "misconceptions": None,
    "scenes": ("en el trabajo", "en la familia y el hogar", "en un trámite o servicio público", "al manejar el dinero", "en el cuidado de la salud", "en el barrio y la comunidad"),
}

# ---------------------------------------------------------------------------------------------------------------------
# Lectura de la fuente oficial
# ---------------------------------------------------------------------------------------------------------------------
_SOURCE = json.loads(SOURCE_PATH.read_text(encoding="utf-8")) if SOURCE_PATH.exists() else {"programas": {}}
PROGRAMS: dict[str, dict] = _SOURCE.get("programas", {})

_VERBS = {
    "analiza": "analizar", "analizan": "analizar", "argumentan": "argumentar", "caracteriza": "caracterizar",
    "comparan": "comparar", "comprenden": "comprender", "comunican": "comunicar", "construyen": "construir",
    "contrasta": "contrastar", "crean": "crear", "desarrollan": "desarrollar", "describen": "describir",
    "dialogan": "dialogar", "diseñan": "diseñar", "distinguen": "distinguir", "elabora": "elaborar",
    "elaboran": "elaborar", "escriben": "escribir", "evalúa": "evaluar", "evalúan": "evaluar", "explica": "explicar",
    "explican": "explicar", "exponen": "exponer", "expresan": "expresar", "formulan": "formular",
    "fundamentan": "fundamentar", "gestionan": "gestionar", "identifican": "identificar", "inventan": "inventar",
    "investigan": "investigar", "justifican": "justificar", "leen": "leer", "narran": "narrar", "observan": "observar",
    "organizan": "organizar", "participan": "participar", "planifican": "planificar", "presentan": "presentar",
    "realizan": "realizar", "reelaboran": "reelaborar", "reflexionan": "reflexionar", "representan": "representar",
    "resuelven": "resolver", "seleccionan": "seleccionar", "sintetizan": "sintetizar", "varían": "variar",
    "aplican": "aplicar", "ordenan": "ordenar", "expresa": "expresar", "identifica": "identificar",
    "resuelve": "resolver", "elige": "elegir", "eligen": "elegir", "usan": "usar", "utilizan": "utilizar",
    "reconocen": "reconocer", "interpretan": "interpretar", "calculan": "calcular", "miden": "medir",
    "producen": "producir", "proponen": "proponer", "debaten": "debatir", "comentan": "comentar",
    "relacionan": "relacionar", "clasifican": "clasificar", "registran": "registrar", "recopilan": "recopilar",
    "valoran": "valorar", "explora": "explorar", "exploran": "explorar", "conocen": "conocer",
}
_CUTS = re.compile(r"[;:]|, | por medio de| mediante| a partir de| con el fin| de acuerdo| según| considerando| aplicando| utilizando")
_FUNCTION_WORDS = {"de", "del", "la", "el", "los", "las", "y", "o", "a", "en", "con", "para", "un", "una", "que", "su", "sus", "al", "por", "como"}
_VERBS.update({
    "caracterizan": "caracterizar", "construye": "construir", "definen": "definir", "diseña": "diseñar",
    "formula": "formular", "indaga": "indagar", "internalizan": "internalizar", "investiga": "investigar",
    "modelan": "modelar", "plantea": "plantear", "propone": "proponer", "proyectan": "proyectar",
    "reconoce": "reconocer",
})
_VERBS.update({
    "comunica": "comunicar", "distingue": "distinguir", "expresarse": "expresarse",
    "infiere": "inferir", "presentarse": "presentarse", "relaciona": "relacionar", "selecciona": "seleccionar",
})
_VERBS.update({
    "compara": "comparar", "discuten": "discutir", "experimentan": "experimentar", "llevan": "llevar",
    "transfieren": "transferir",
})
_UNKNOWN_VERBS: set[str] = set()


def _slugify(text: str) -> str:
    plain = "".join(c for c in unicodedata.normalize("NFD", text.lower()) if unicodedata.category(c) != "Mn")
    return re.sub(r"[^a-z0-9]+", "-", plain).strip("-")


def split_key(key: str) -> tuple[str, str]:
    """`LECO_NB1` -> (`LECO`, `NB1`)."""
    sigla, tag = key.rsplit("_", 1)
    if tag not in LEVEL_TAGS:
        raise ValueError(f"{key}: el sufijo debe ser uno de {', '.join(LEVEL_TAGS)}")
    return sigla, tag


def objective_code(key: str, module: int, performance: int) -> str:
    """Código estable del objetivo: EPJA-<SIGLA>-<NIVEL>-OAD-NN, con NN = (módulo - 1) * 4 + desempeño."""
    sigla, tag = split_key(key)
    if not 1 <= performance <= 4:
        raise ValueError(f"{key}: el desempeño {performance} del módulo {module} excede el formato NN = (módulo - 1) * 4 + desempeño")
    return f"EPJA-{sigla}-{tag}-OAD-{(module - 1) * 4 + performance:02d}"


def subject_slug(key: str, program: dict | None = None) -> str:
    """Carpeta de la asignatura: distinta de la del currículo escolar regular (que tiene otros programas)."""
    program = program or PROGRAMS[key]
    _sigla, tag = split_key(key)
    name = program.get("slug") or _slugify(re.sub(r"\s+y\s+", " ", program["asignatura"]))
    return f"{name}-epja-{tag.lower()}"


def subject_name(key: str, program: dict | None = None) -> str:
    program = program or PROGRAMS[key]
    return f"{program['asignatura']} · EPJA {LEVEL_LABEL[split_key(key)[1]]}"


def _infinitive(phrase: str) -> str:
    """Pasa a infinitivo el verbo inicial y los verbos coordinados («y aplican», «, leen») que estén en la tabla."""
    words = phrase.split()
    if not words:
        return phrase
    first = words[0].rstrip(",:;")
    low = first.lower()
    if low in _VERBS:
        words[0] = _VERBS[low].capitalize()
    elif not re.search(r"(ar|er|ir)$", low) and not first.startswith("¿"):
        _UNKNOWN_VERBS.add(first)
    for index in range(1, len(words)):
        previous = words[index - 1]
        bare = words[index].rstrip(",:;.")
        if (previous in ("y", "e") or previous.endswith(",")) and bare.lower() in _VERBS:
            words[index] = words[index].replace(bare, _VERBS[bare.lower()], 1)
    return " ".join(words)


def _topic(phrase: str) -> str:
    clean = _infinitive(re.sub(r"\s+", " ", phrase).strip().rstrip("."))
    first = clean
    for match in _CUTS.finditer(clean):
        before = clean[: match.start()]
        weak = match.group()[0] in ",;:"
        if match.start() < (25 if weak else 18) or (match.group().startswith(",") and re.search(r" como \S+( \S+)?$| por ejemplo", before)):
            continue  # un corte muy corto o dentro de una enumeración dejaría un título sin sentido
        first = before
        break
    truncated = len(first) > 90
    if truncated:
        first = first[:90].rsplit(" ", 1)[0]
    words = first.split()
    if truncated and len(words) > 4 and words[-2] in ("y", "e"):
        words = words[:-2]  # no dejar un verbo coordinado a medio decir
    while len(words) > 3 and words[-1].lower().strip(",;:") in _FUNCTION_WORDS:
        words.pop()
    first = " ".join(words).rstrip(",;:")
    return first[0].upper() + first[1:]


def unknown_verbs() -> list[str]:
    """Verbos iniciales que no están en la tabla de infinitivos (para revisar al agregar una asignatura)."""
    return sorted(_UNKNOWN_VERBS)


def objective_description(key: str, module: dict, performance: dict, program: dict | None = None) -> str:
    """Frase oficial del desempeño + OA nucleares + conocimientos esenciales + horas, solo con textos de la fuente."""
    program = program or PROGRAMS[key]
    text = re.sub(r"\s+", " ", performance["frase"]).strip()
    parts = [text if text.endswith((".", "?", "!")) else text + "."]
    oa = []
    for number in performance.get("oa", []):
        statement = program.get("oa_texto", {}).get(str(number))
        if statement:
            oa.append(f"OA {number}: {statement.strip()}")
    if oa:
        parts.append("Objetivos de aprendizaje nucleares: " + " ".join(item if item.endswith(".") else item + "." for item in oa))
    essentials = [re.sub(r"\s+", " ", item).strip() for item in performance.get("ce", []) if item.strip()]
    if essentials:
        parts.append("Conocimientos esenciales: " + " ".join(item if item.endswith(".") else item + "." for item in essentials))
    if performance.get("horas"):
        parts.append(f"Horas pedagógicas: {performance['horas']}.")
    return " ".join(parts)


def _entries() -> dict[str, dict]:
    """Un registro por actividad de desempeño de todas las asignaturas de la fuente."""
    found: dict[str, dict] = {}
    for key, program in PROGRAMS.items():
        _sigla, tag = split_key(key)
        seen: dict[str, str] = {}
        for module in program["modulos"]:
            for performance in module["desempenos"]:
                code = objective_code(key, module["modulo"], performance["num"])
                if code in found:
                    raise ValueError(f"código repetido: {code}")
                topic = _topic(performance["frase"])
                if topic.lower() in seen:  # misma frase oficial en dos desempeños: se distingue por su conocimiento esencial propio
                    previous = {c.split(":")[0] for c in seen[topic.lower()]}
                    own = [c.split(":")[0].strip() for c in performance.get("ce", []) if c.split(":")[0] not in previous]
                    label = own[0].lower().rstrip(".") if own else f"módulo {module['modulo']}, desempeño {performance['num']}"
                    topic = f"{topic} ({label})"
                seen[topic.lower().split(" (")[0]] = performance.get("ce", [])
                found[code] = {
                    "key": key, "tag": tag, "module": module, "performance": performance, "program": program,
                    "topic": topic, "count": performance.get("horas"),
                }
    return found


ENTRIES = _entries()


def class_count(code: str) -> int | None:
    """Clases del objetivo = horas pedagógicas de su actividad de desempeño (None si no es EPJA)."""
    entry = ENTRIES.get(code)
    if entry is None:
        return None
    if not isinstance(entry["count"], int) or not 2 <= entry["count"] <= 9:
        raise ValueError(f"{code}: horas del desempeño fuera de 2 a 9 ({entry['count']!r}); revisar la fuente")
    return entry["count"]


def phase_plan(code: str, phases: list) -> list | None:
    """Fases del catálogo para un objetivo EPJA (None si el código no es EPJA); `phases` es la lista PH del generador."""
    count = class_count(code)
    if count is None:
        return None
    plan = base.STAGE_PLANS["adultez"][count]
    extended = [
        phases[0], phases[1],
        ("Modelar paso a paso", "mostrar el procedimiento con un caso de la vida diaria y pensar en voz alta"),
        phases[2],
        ("Practicar de forma independiente", "ensayar sin apoyo y autocorregirse con una pauta"),
        phases[5], phases[4],
        ("Explicar a otra persona", "comunicar lo aprendido con las propias palabras"),
        phases[6],
    ]
    return [extended[index] for index in plan]


def snapshot_records(keys: list[str] | None = None) -> list[dict]:
    """Registros del snapshot (uno por curso y asignatura) para las claves pedidas; sin claves, todas las de la fuente."""
    records = []
    for key in keys or sorted(PROGRAMS):
        program = PROGRAMS[key]
        _sigla, tag = split_key(key)
        objectives = []
        for module in program["modulos"]:
            for performance in module["desempenos"]:
                objectives.append({
                    "code": objective_code(key, module["modulo"], performance["num"]),
                    "description": objective_description(key, module, performance, program),
                    "axis": f"Módulo {module['modulo']}: {module['gran_idea'].strip().rstrip('.')}",
                    "prioritized": False,
                    "url": program["pagina"],
                })
        for course_slug in LEVEL_TAGS[tag]:
            order, course_name = COURSES[course_slug]
            records.append({
                "course": course_name, "course_slug": course_slug, "course_order": order, "course_url": program["pagina"],
                "subject": subject_name(key, program), "subject_slug": subject_slug(key, program), "subject_url": program["pagina"],
                "coverage": "formacion-epja",
                "approach": "partir de situaciones de la vida adulta (trabajo, familia, trámites, dinero, salud, vecindario) y de lo que cada persona ya sabe, con apoyo oral y gráfico cuando se necesite",
                "evidence": "producción breve, oral, escrita o gráfica, que muestre lo aprendido en una situación de la vida diaria",
                "objectives": objectives,
            })
    return records


# ---------------------------------------------------------------------------------------------------------------------
# Secuencias docentes
# ---------------------------------------------------------------------------------------------------------------------
SUBJECT_PROFILES: dict[str, dict] = {}
RECORDS: dict[str, dict] = {}
for _record in SNAPSHOT["records"]:
    if _record["course_order"] not in EPJA_ORDERS:
        continue
    for _objective in _record["objectives"]:
        _entry = ENTRIES.get(_objective["code"])
        if _entry is None:
            raise RuntimeError(f"{_objective['code']}: el snapshot trae un objetivo EPJA que no está en sources/epja-programas.json")
        _sigla, _tag = split_key(_entry["key"])
        _profile = PROFILES_BY_SIGLA.get(_sigla, DEFAULT_PROFILE)
        SUBJECT_PROFILES.setdefault(_record["subject_slug"], {
            "domain": "adultez",
            "continuity": f"{_profile['continuity']} {LEVEL_CONTINUITY[_tag]}",
            "vocabulary": _profile["vocabulary"],
            "misconceptions": _profile["misconceptions"],
            "scenes": _profile["scenes"],
        })
        RECORDS[_objective["code"]] = {
            "slug": _record["subject_slug"], "subject": _record["subject"], "axis": _objective["axis"],
            "description": _objective["description"], "url": _objective["url"],
            "count": class_count(_objective["code"]), "topic": _entry["topic"], "tag": _tag,
        }


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    record = RECORDS[code]
    entry = ENTRIES[code]
    sequence = base.build_sequence_from_record(code, record, SUBJECT_PROFILES[record["slug"]], PRIOR_LEVEL[record["tag"]])
    module, performance = entry["module"], entry["performance"]
    phrase = re.sub(r"\s+", " ", performance["frase"]).strip()
    indicators = [f"Actividad de desempeño {performance['num']} del módulo {module['modulo']}: {phrase}"]
    indicators += [re.sub(r"\s+", " ", item).strip() for item in performance.get("ce", [])[:2]]
    indicators = [item if item.endswith(".") else item + "." for item in indicators]
    sequence["official_alignment"] = {
        "units": [
            f"Módulo {module['modulo']} ({module['horas']} horas): {module['gran_idea'].strip()}",
            f"Actividad de desempeño {performance['num']} ({performance['horas']} horas pedagógicas = {record['count']} clases)",
        ],
        "indicators": (indicators + [f"{focus}." for focus in sequence_focuses(sequence)])[:3],
        "indicator_origin": "Actividad de desempeño y conocimientos esenciales del programa de estudio EPJA oficial; la distribución en clases es organización pedagógica interna, no una unidad oficial.",
        "source": record["url"],
    }
    return sequence


def sequence_focuses(sequence: dict) -> list[str]:
    return [lesson["title"] for lesson in sequence["lessons"]]


SEQUENCES = {code: True for code in RECORDS}
