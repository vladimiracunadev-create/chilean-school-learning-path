"""Alignment audit of student notebooks against the official OA and the planned class title.

For each lesson with a notebook it measures (a) how much of the official OA statement and of
the class title (content words, by 5-letter stem) is actually present in the notebook, and
(b) whether the explanation is readable for the grade (average sentence length), plus a few
pedagogical smells. It does NOT judge disciplinary accuracy: it ranks lessons so a person
reads the weakest ones first. Output: docs/ANALISIS_ALINEACION.md (check with no arguments,
refresh with --write).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parent
sys.path.insert(0, str(HERE))

import student_lessons as sl  # noqa: E402
import validate_student_lessons as validator  # noqa: E402

REPORT = ROOT / "docs" / "ANALISIS_ALINEACION.md"
MIN_COVERAGE = 0.5
LOW_OA = 0.34
MAX_SENTENCE_WORDS = {1: 16, 2: 18}
STOP = set("""para como entre desde hasta sobre cuando donde porque también algunos algunas
otros otras cada esta este estos estas mediante usando utilizando través según
forma manera nivel clase tema parte partir hacia puede pueden mismo misma
del las los una unos unas por con sin que son era ser más muy sus""".split())
SMELLS = (
    (re.compile(r"\bdepende\b", re.I), "respuesta «depende» en ejercicio cerrado"),
    (re.compile(r"\bpor ejemplo\b", re.I), "respuesta abierta «por ejemplo»"),
)


def stems(text: str) -> set[str]:
    plain = unicodedata.normalize("NFD", text.lower())
    plain = "".join(c for c in plain if unicodedata.category(c) != "Mn")
    return {w[:5] for w in re.findall(r"[a-zñ]{5,}", plain) if w not in STOP and w[:5] not in STOP}


def official(path: Path, number: int) -> tuple[str, str]:
    text = path.read_text(encoding="utf-8")
    oa = re.search(r"## Qué se debe aprender\s+>\s*(.+)", text)
    title = re.search(rf"^### Clase {number} de \d+: (.+?)(?: \{{#|$)", text, re.M)
    return (oa.group(1) if oa else ""), (title.group(1) if title else "")


def notebook_text(content: dict) -> str:
    parts = [content["use"], *content["explain"], *(f"{a} {b}" for a, b in content["vocab"])]
    for example in content["worked"]:
        parts += [example["title"], example["problem"], *example["steps"], example["answer"]]
    for item in sl.all_questions(content):
        parts += [item["q"], item["a"], item["why"]]
    parts += [content["open_task"]["statement"], content["open_task"]["example"]]
    return " ".join(parts)


def sentence_length(content: dict) -> float:
    sentences = [s for s in re.split(r"[.!?]+\s", " ".join(content["explain"])) if s.strip()]
    return sum(len(s.split()) for s in sentences) / max(1, len(sentences))


def analyse(level_prefix: str) -> list[dict]:
    sl.load_all()
    rows = []
    for (oa_code, number), content in sorted(sl.REGISTRY.items()):
        path = validator.curriculum_file(oa_code)
        if path is None or not path.relative_to(ROOT).parts[1].startswith(level_prefix):
            continue
        oa_text, title = official(path, number)
        wanted = stems(f"{oa_text} {title}")
        have = stems(notebook_text(content))
        coverage = len(wanted & have) / len(wanted) if wanted else 1.0
        title_wanted = stems(title)
        title_cov = len(title_wanted & have) / len(title_wanted) if title_wanted else 1.0
        smells = []
        for question in sl.closed_exercises(content):
            for pattern, label in SMELLS[:1]:
                if pattern.search(question["a"]):
                    smells.append(label)
        rows.append({
            "code": oa_code, "number": number, "title": title, "coverage": coverage, "title_cov": title_cov,
            "sentence": sentence_length(content), "smells": sorted(set(smells)),
            "subject": path.relative_to(ROOT).parts[2],
        })
    return rows


MANUAL_1 = [
    "### Segunda lectura crítica de las 691 clases",
    "",
    "Después de la validación automática, cada una de las 691 clases de 1.º básico fue releída de principio a fin por un segundo lector (asistido por IA, independiente de quien la escribió), que la contrastó con el texto del OA y el título de la clase en el currículo del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional: se usó el texto oficial reproducido en cada ficha.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 83 | Dato falso sobre la derecha y la izquierda; centímetros y operaciones de 2.º básico en OA 18 y otros; contradicciones internas entre explicación y ejemplos; respuestas falsas en patrones y familias de operaciones. |",
    "| Lenguaje y Comunicación | 131 | Conteos de palabras erróneos; datos falsos en textos (gatos que no nadan, osos pescando en invierno); definiciones y terminología silábica; léxico difícil sin definir; ejercicios de oralidad ambiguos. |",
    "| Ciencias Naturales | 49 | Conclusiones no justificadas por los datos; cifras de seres vivos eliminadas o hechas cualitativas; datos de ejemplo rotulados; operaciones de otro nivel; avisos de seguridad. |",
    "| Historia, Geografía y Ciencias Sociales | 68 | Edades calculadas sin considerar el mes; voto femenino (1934 y 1949 son leyes, no el día en que votaron); restas de años fuera de nivel; fechas de casos inventados; ambigüedades de mapas. |",
    "| Inglés | 69 | Inglés incorrecto o antinatural; estructuras de otro nivel; vocabulario usado sin enseñarse; explicaciones en español falsas; expresiones del OA agregadas (/s/-/z/, I want, Here). |",
    "| Lengua y Cultura de los Pueblos Originarios | 129 | Conteos de sílabas y palabras; afirmaciones culturales no seguras eliminadas o generalizadas; frase inventada retirada; preguntas que jerarquizaban identidad; aritmética de otro nivel. |",
    "| Educación Física y Salud | 48 | Riesgos motores (retroceder de espaldas); equivalencias falsas («dos brazos» = 2 m); cifras de salud generalizadas; ejercicios imposibles de practicar. |",
    "| Orientación | 35 | Lenguaje de las clases de cuerpo y protección ajustado («no es tu culpa», nada es un secreto); ambigüedades; operaciones de otro nivel; seguridad con tijeras. |",
    "| Música | 29 | Conteos de pulsos y sílabas erróneos; contradicciones entre consigna y ejemplo; objetos de vidrio y martillo reemplazados por opciones seguras. |",
    "| Artes Visuales | 24 | Multiplicaciones y restas de años de otro nivel; datos de obras dudosos; ambigüedades. |",
    "| Tecnología | 26 | Instrucciones de seguridad incorrectas; respuesta contraria a lo enseñado; multiplicaciones; software ficticio rotulado. |",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados en una pasada posterior:** Inglés OA 03 (contraste /w/-/th/) y OA 07 (ocupaciones y comida); Tecnología OA 03 (fibras y plásticos) y OA 06 (tipos de software); Historia (restas de años de cuatro cifras reemplazadas por comparación, orden y saltos cortos).",
    "- **Lenguaje:** OA 17 y OA 09 piden obras completas y poemas de autor; el cuaderno usa textos originales breves por derechos de autor. Queda abierto.",
    "- **Lengua y Cultura de los Pueblos Originarios:** las clases de lengua se practican sólo con castellano y el saludo «mari mari»; el aprendizaje de la lengua real queda en manos del educador o educadora tradicional.",
    "",
    "Todos los contenidos que requieren especialista, incluida la verificación contra el Programa de Estudio oficial, siguen listados en [Revisión profesional pendiente](REVISION_PENDIENTE_CUADERNOS.md).",
    "",
]

MANUAL_2 = [
    "### Segunda lectura crítica de las 721 clases",
    "",
    "Cada una de las 721 clases de 2.º básico (las 20 de Matemática OA 01 a 05 escritas antes y las 701 restantes) fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y con el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 93 | Materiales que no existían en el cuaderno (tablas y tarjetas «de este cuaderno»); billetes de $10 y $100 inexistentes; multiplicaciones, divisiones y años de cuatro cifras fuera de nivel; error ilustrado sin sentido; saltos que cruzaban la decena que la clase prohibía; restas de reloj de 24 horas sin enseñar la regla. |",
    "| Lenguaje y Comunicación | 149 | Regla de diptongo falsa («ciudad»); «g fuerte» contraria a la enseñanza tradicional; palabras y conteos erróneos; dato falso sobre aves en Chile; estructuras no enseñadas; enunciados que daban la respuesta; textos que podían herir (tartamudez, edad, familia). |",
    "| Ciencias Naturales | 57 | Datos biológicos falsos (piel de anfibios, escorpión diurno, «las branquias sacan el aire»); caracol sin concha; estaciones con fechas aproximadas; hielo en vaso de vidrio; veleta con alfiler. |",
    "| Historia, Geografía y Ciencias Sociales | 72 | Respuestas con más de una válida (países de referencia); anacronismo de los videos; piñones atribuidos a todos los mapuche; seguridad ante temblor y tsunami; términos usados sin definir. |",
    "| Inglés | 68 | Inglés incorrecto («has a bread»); conteos de palabras falsos; estructuras no enseñadas (do you like, here you are); prueba de «vibra la garganta» engañosa; regla a/an con excepciones. |",
    "| Lengua y Cultura de los Pueblos Originarios | 116 | Eliminadas o generalizadas fechas y ceremonias (We Tripantu, Tapati, Año Nuevo, Pachamama, machi, yatiri); asociaciones de arte con pueblos; variante «cuyén» de ortografía no segura; afirmación histórica generalizada; aritmética de otro nivel. |",
    "| Educación Física y Salud | 47 | Volteo sin supervisión; alfombra y libro como superficies resbalosas; pulso y respiración poco realistas; riesgo de caminar hacia atrás; protocolo inconsistente ante un compañero herido; contradicciones de datos en las metas. |",
    "| Orientación | 35 | Divisiones y multiplicaciones fuera de nivel; ejercicio alarmante sobre secretos reemplazado; doble negativo; supuestos sobre la composición de la familia; datos de higiene y sueño como recomendaciones generales. |",
    "| Música | 29 | Respuesta de ejemplo que no cambiaba el pulso; confusión entre vocal y altura del sonido; pieza que no calzaba con la respuesta; enunciado subjetivo de más suave a más fuerte. |",
    "| Artes Visuales | 24 | Actividad que contradecía sus criterios; ejercicios sobre lo no enseñado (óvalos); ambigüedades de enunciado; obras reales sustituidas por tipos de obra seguros. |",
    "| Tecnología | 31 | Falso «las imágenes propias no tienen derechos de autor»; relleno que no tapa un dibujo; instrucciones de seguridad; software ficticio rotulado. |",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Lenguaje (grupo «dr», anécdota, experiencia personal y relato de hechos, carta, cuento folclórico frente a cuento de autor, lectura independiente); Historia (chango, rapa nui y huilliche, inmigración oriental, patrimonio de más regiones, río, océano, isla y ciudad); Artes (textiles, herramientas digitales, tipos de obra local, latinoamericana y universal); Ciencias (hábitat del mamífero); Matemática (preguntas estadísticas, números cercanos a 1.000); Educación Física (niveles, juegos individuales y colectivos).",
    "- **Abiertos:** Artes OA 04 pide observar al año 10 obras locales o chilenas, 10 latinoamericanas y 10 universales, y el cuaderno solo puede describirlas (imágenes reales y derechos los aporta el docente); Música OA 03 nombra obras con derechos que no se reproducen; Lenguaje OA 06 y 22 piden poemas y cuentos reales de autor o tradicionales; Lengua y Cultura de los Pueblos Originarios: relatos, textos y oraciones reales en lengua indígena y eventos o técnicas propias de cada pueblo los aporta el educador o educadora tradicional; software educativo (Matemática OA 03, 09 y 12) es opcional en el OA y no se puede entregar en el cuaderno; Ciencias OA 02 (moluscos y miriápodos) y vocabulario «endémico» de OA 05 requerirían clases nuevas.",
    "- **Decisiones que dependen del programa oficial:** reloj de 24 horas o a. m./p. m. (Matemática OA 18), equivalencia 1 m = 100 cm (OA 19) y aristas y vértices del cubo (OA 16); no se pudo contrastar con el texto vigente.",
    "- **Criterio distinto entre asignaturas, a revisar por especialista:** Historia mantiene las celebraciones y ceremonias de los pueblos (ngillatun, We Tripantu, Año Nuevo Andino, Tapati, Hain, Pachamama) como fichas generales, porque el OA 01 pide creencias y fiestas; Lengua y Cultura las eliminó por no poder afirmarlas con seguridad.",
    "",
]

MANUAL_3 = [
    "### Segunda lectura crítica de las 757 clases",
    "",
    "Cada una de las 757 clases de 3.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional; solo un lector confirmó el teléfono 147 en ChileAtiende.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 112 | Ejes que no parten de 0 mal descritos; error de ejemplo no plausible (5:100); dinero imposible (precios terminados en 5); aritmética fuera de nivel (2.500 − 2.000, divisiones por decenas); definición de vértice que contradecía el cono; prisma triangular fuera del OA; ejercicios copiados del ejemplo resuelto; material irrealizable (328 tapas). |",
    "| Lenguaje y Comunicación | 157 | 17 actividades abiertas sin su texto; orden alfabético erróneo; inferencia que el texto decía literalmente; unos 30 ejercicios abiertos pasados a cerrados; expresiones que podían leerse como burla; supuestos sobre la familia; nombre de una persona real en un libro ficticio. |",
    "| Ciencias Naturales | 55 | Estambres «en el centro» de la flor; prueba no justa (dos variables a la vez); mito del cartón de huevos; mano como material opaco; eco sin superficie lejana; aritmética fuera de nivel; seguridad al mirar eclipses. |",
    "| Historia, Geografía y Ciencias Sociales | 72 | Ciudadanía ateniense mal definida; carreras de carros atribuidas al anfiteatro; acueducto definido solo como puente; Atenas y Esparta «en el mismo país»; teléfono 147 verificado y afirmación no comprobable retirada; fuentes sin fecha tratadas como «la más nueva». |",
    "| Inglés | 69 | Calcos del español (I change my idea); «in the hospital» sobre un médico; glosas erróneas (sleep tight, desk); estructuras no enseñadas; respuesta que contradecía la consigna (an frente a a); enunciados que daban la respuesta. |",
    "| Lengua y Cultura de los Pueblos Originarios | 116 | 33 ejercicios aritméticos triviales puestos para el verificador reemplazados; «ruka» pasó a «casa mapuche»; afirmaciones culturales generalizadas; conteos erróneos; atribución falsa de una ficha a la educadora; estereotipos del ejemplo retirados. |",
    "| Educación Física y Salud | 48 | Cifras de pulso y respiración sin número que lograr; visión periférica mal enseñada; «salto mortal» retirado; escaleras, empujones y bebidas energizantes; contradicciones de metas; aritmética fuera de nivel. |",
    "| Orientación | 35 | Intimidad y consentimiento con excepción de salud explícita; origen de la vida en lenguaje sobrio; consumo de drogas con salida segura; supuestos sobre la familia; «copiar es copiar sin entender» falso. |",
    "| Música | 35 | Explicación de duración que daba 5 y no 4 pulsos; siglos con años de cuatro cifras retirados; datos de obras y autores generalizados; digitaciones de flauta agregadas; supuestos sobre abuelos. |",
    "| Artes Visuales | 25 | Ejercicios sobre lo no enseñado (semicírculo, cono, profundidad); regla de seguridad que contradecía su material (tierra); ocho supuestos sobre la familia; «mirete» sin definición. |",
    "| Tecnología | 33 | Tarea de reordenar frases ya ordenadas; ejemplo que cumplía «todos los criterios» con una punta que corta; «regar una vez por semana» retirado; reglas de seguridad de lijado, arcilla y cola; insumo ficticio rotulado. |",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Lenguaje (mitos, novelas, biografías, relatos históricos, cartas, catálogo digital, diccionario ilustrado, revistas y diarios, apoyos para exponer); Historia (legados griegos, arte romano, Greenwich, líneas de referencia); Ciencias (coníferas, hábitat del mamífero, efectos de la alimentación); Inglés (Easter, rimas, figuras y lugares); Música (reiteraciones, digitaciones de flauta, audición y creación); Matemática (minutos sueltos, números cercanos a 1.000, redes del cubo); Educación Física (giro de 180°, desmarque); Orientación (derecho a ser diferente, intereses propios, gestora de su vida).",
    "- **Abiertos:** Música OA 03 pide escuchar al menos 20 músicas y las fichas son escritas; Artes OA 04 pide 15 + 15 + 15 obras al año y las del cuaderno son inventadas; Lenguaje: mitos, leyendas, cuentos folclóricos y novelas reales con derechos de autor; Lengua y Cultura de los Pueblos Originarios: textos, oraciones y relatos reales en lengua indígena, que aporta el educador o educadora tradicional; software educativo, audio y video en varias asignaturas; Educación Física OA 04 (bicicleta y playa solo como contexto) y los pasos de danzas concretas.",
    "- **Decisiones que dependen del programa oficial:** si el prisma y la pirámide de base triangular son de 3.º (se retiró el prisma triangular y se dejó la pirámide), si los ejes que no parten de 0 y la hora de 24 horas son contenido del nivel, y si «moda» corresponde a 3.º (se usó «valor más frecuente»).",
    "",
]

MANUAL_4 = [
    "### Segunda lectura crítica de las 811 clases",
    "",
    "Cada una de las 811 clases de 4.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Varios lectores declararon que no pudieron resolver uno por uno todos los ejercicios.",
    "",
    "| Asignatura | Clases releídas | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 118 | 99 − 45 explicado como 56 (es 54); estimaciones que no calzaban (640 − 285 + 152); errores de división con resto que no cumplían la prueba; ejercicio sin solución (dos números de suma 700 con estimación 600); cuadrado de 6 cm² imposible; unos 30 ejercicios copiados del ejemplo resuelto; divisores de dos cifras y dividendos de tres cifras fuera del OA; comparación con 1/2 que no discriminaba; gráfico de ejes truncados descrito como «el doble». |",
    "| Lenguaje y Comunicación | 161 | Unas 30 preguntas cerradas sobre textos que nunca se entregaban; 4 mayúsculas contadas de más (cordillera); pingüinos «de lugares fríos» (falso para el de Humboldt); divisor de dos cifras fuera de nivel; salto lógico del queque; «coma tras de pronto» como obligatoria; «cuenta» como «cuento»; ordenaciones con dos soluciones; escenas de riesgo (río, pozo) y supuestos sobre la familia. |",
    "| Ciencias Naturales | 71 | Ruta del mensaje nervioso con el ojo y el oído pasando por la médula (falso); «núcleo de 3.440 km» ajustado para que sumara; globo que pesa más inflado; imán que levanta clips a distancia; hibernación de «días»; cuchara de plástico que se hunde; llave que sube el agua 20 mL; bolsa de plástico cerca de la cara. |",
    "| Historia, Geografía y Ciencias Sociales | 82 | Mesoamérica presentada solo como territorio maya; incas sin calendario por comparación; «allillanchu» como saludo; semáforo y vereda atribuidos a la municipalidad; presupuesto de escuelas decidido por el Congreso; río Tíber y «Educación Cívica» de otro nivel; siete ejercicios abiertos pasados a elección; «y sangre» en las ofrendas retirado. |",
    "| Inglés | 69 | Respuestas con dos opciones válidas (small o blue); estructuras no enseñadas (How old is he/she, Do they…); regla de I don't know incoherente; glosas faltantes (Mr., Dr., near, river); Easter definido solo como huevos; leche para un gato; «mariquita» por «chinita»; textos de escucha sin su guion. |",
    "| Lengua y Cultura de los Pueblos Originarios | 126 | Fichas, testimonios y textos que el ejercicio citaba y la clase no entregaba; «según el educador tradicional, su pueblo…» retirado; idea central equivocada en un relato de práctica; «antu» y «ruca» presentados como error de grafía; «espíritu enojado» en distractores; foto de un compañero en un afiche; conteos que no calzaban; unos 14 «Ordena…» con dos órdenes posibles. |",
    "| Educación Física y Salud | 49 | Correr de espaldas; dolor de rodilla resuelto con «cambiar a caminar»; giros de cuello y rodilla; pañuelo-cola con «sin contacto»; cemento mojado que «no resbala»; 55 usos de «persona de tu casa»; 60 min «de actividad» sin intensidad; contradicciones de metros y de tiempos de calentamiento. |",
    "| Orientación | 40 | Frutas y verduras contadas como dos grupos contra su explicación; comparación de Ema con Pablo en una clase que enseña a no etiquetar; campaña de «4 útiles» que presiona a familias; revisión de garganta como excepción de salud; 29 ejercicios de redacción libre pasados a elección; ejemplos de control o aislamiento reescritos. |",
    "| Música | 35 | Motivo de 5 pulsos dentro de secciones de 4; regla de variación ambigua; ejercicios cerrados con respuesta libre; supuesto de canción de cuna en el hogar; ejemplo de «misma idea» con dos lecturas. |",
    "| Artes Visuales | 25 | Resumen del relato de Trentren Vilu y Kaikai Vilu reducido a lo general; Caleuche y cerámica diaguita sin afirmaciones que el cuaderno no puede sostener; obras del OA 04 rotuladas como inventadas; «la lana es pesada» y «la plasticina se ensucia» retirados; unos 73 ajustes entre ambigüedades y distractores absurdos. |",
    "| Tecnología | 35 | Insumos no entregados (plan del atril, letra de la diapositiva); sumas puestas para el verificador cambiadas por cálculos con sentido; carpeta con símbolos contra la regla de nombres; direcciones inventadas terminadas en .cl pasadas a .example; «girasoles siguen al Sol» matizado; hojas de cálculo y diagramas integrados en clases existentes. |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "Los lectores confirmaron que en el repositorio el texto oficial citado bajo varios OA de 4.º no coincide con el título y las etapas de sus clases: Lenguaje OA 11 a 18 (por ejemplo, el OA 11 cita «escribir frecuentemente» y sus clases enseñan diccionario y orden alfabético; el OA 16 cita «planificar la escritura» y sus clases tratan la letra legible), y Lengua y Cultura de los Pueblos Originarios OA 10 a 16 (el OA 10 cita relatos fundacionales y sus clases tratan tiempo y espacio). Los cuadernos siguieron el título de la clase y repartieron el contenido del OA dentro de las clases existentes. Conviene corregir esa asignación en el currículo; no se hizo aquí porque exige el Programa de Estudio.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Lenguaje (ortografía b-v, h, ay/hay/ahí y acentuación del OA 21; diario de vida); Matemática (decena de mil; fracciones con denominador 12 y 100); Historia (escritura y construcciones mayas, extensión azteca, sociedad en la tabla comparativa, ubicación frente a los océanos); Inglés (partes de la casa, lugares de la ciudad, presentar a otros, acciones en curso); Tecnología (hoja de cálculo y diagramas); Educación Física (base a pequeña altura, elementos de la cueca); Orientación (aceptar las emociones ajenas, vínculo entre sexualidad y origen de la vida).",
    "- **Abiertos:** Lenguaje OA 11 (no hay clase que enseñe a escribir con frecuencia como hábito) y OA 15 (letra clara solo como criterio); Música OA 03 (escuchar al menos 20 músicas, sin audio) y OA 05 (creación con alturas); Artes OA 04 (15 + 15 + 15 obras reales al año, las del cuaderno son inventadas) y OA 03 (fotografía, imágenes digitales y software); Tecnología OA 05 (no se enseña a usar un programa real de hojas de cálculo); software geométrico y educativo en Matemática (OA 17, 23, 24 y 26); Lengua y Cultura de los Pueblos Originarios: relatos fundacionales, cosmovisión, textos y oraciones en lengua indígena (educador o educadora tradicional); Inglés: audio, video y discriminación auditiva de /s/-/z/ y /w/-/th/.",
    "- **Decisiones que dependen del programa oficial:** divisores de dos cifras y factores de dos cifras en Matemática (se usaron factores de dos cifras y divisor de un dígito); convención de coordenadas y de 12:00 p.m. / 00:00 (convenciones didácticas del cuaderno); si las inecuaciones usan números naturales; clases de OA 11 a 18 de Lenguaje y OA 10 a 16 de Lengua y Cultura cuyos títulos no corresponden a su texto de OA.",
    "",
]

MANUAL_5 = [
    "### Segunda lectura crítica de las 844 clases",
    "",
    "Cada una de las 844 clases de 5.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios; los lectores sí lo intentaron, y varios advirtieron que no pudieron recalcular cada cifra con herramienta.",
    "",
    "| Asignatura | Clases | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 115 | Unos 20 ejercicios idénticos al ejemplo resuelto de su clase en OA 01 a 11 y otros tantos en OA 12 a 23; «5.060.000 > 5.600.000 porque el 6 está más a la izquierda» (falso); denominador común mayor que 12 «no hace falta» (falso: 1/3 + 1/5); giro de 180° con fórmula algebraica y números negativos de 7.º; «el doble de 7 más 3» con dos lecturas; rectángulo de vértices (1,2), (4,2), (4,5), (1,5) que era un cuadrado; regla de «poco posible» con casos no clasificados; contextos poco creíbles (agua de un colegio, carrera de 12 a 38 s). |",
    "| Lenguaje y Comunicación | 166 | Unos 190 ejercicios de OA 02 a 08 que citaban un texto («el faro», «el poema de la lluvia») que el enunciado no entregaba; cuentos de Nico y Lía ausentes en OA 16; conteos erróneos (22 palabras y no 19, resumen de 30 palabras contra la regla de un tercio); «pájaro / rápido» como asonante y «papel / miel» como asonante (es consonante); nombre «Marta Lagos» igual al de una persona real; estereotipo de género en la caleta; unos 25 ejercicios de OA 18 a 26 idénticos al ejemplo resuelto; «salto» como palabra que el corrector corregiría; escena de un cable eléctrico arreglado sin adulto; «grábate» en una actividad oral. |",
    "| Ciencias Naturales | 64 | Glóbulos rojos comparados con células nerviosas «en una gota de sangre»; virus «no es célula porque es más pequeño»; absorción solo en el intestino delgado contra la clase; cargador sin uso con consumo sobreestimado; tocar ampolletas encendidas «si hay adulto»; tabla de mareas con una hora de caminata a las 21:00; pregunta que sugería beber agua de río; «bajo 200 m todo es oscuro»; «promedio» no enseñado; siete ejercicios que repetían cifras del ejemplo. |",
    "| Historia, Geografía y Ciencias Sociales | 106 | Voto femenino sin precisar (1935 municipal y 1949 todas las elecciones) y convención de los derechos del niño sin fecha; «maratón» para 5 km y Quellón «pueblo pesquero»; cifras de consumo de agua y luz irreales; mensaje de sismo que invertía el consejo («corre al cerro» contra «no hay maremoto»); «adobe y teja bastan para reconocer un edificio colonial» (falso); «Magallanes llegó a la India»; «universidad solo en Perú»; citas atribuidas a Las Casas y Guamán Poma que eran resúmenes; fundación con nombre real; obras de arte coloniales y relieve sin cobertura, agregados. |",
    "| Inglés | 71 | «There is some milk» como poca cantidad; rima ten/again; glosa «stand in a line» como «ponte de pie»; estructuras no enseñadas (has, wakes, does, played); «Can a bird fly?» contra el pingüino de la misma clase; jirafa «vive en la jungla»; familias y abuelas en diálogos; diálogos, ilustraciones y canciones del OA sin ejercicio, agregados; 8 respuestas aritméticas planas pasadas a cálculo verificado. |",
    "| Lengua y Cultura de los Pueblos Originarios | 135 | Ritos y costumbres inventados (silencio para recordar el relato, dar gracias al primer pasto, agradecer a la tierra y a las manos) cambiados por prácticas neutras; «según el educador tradicional dijo que chaltumay se usa para…» retirado; «mari mari significa que todos somos hermanos» y el distractor «mapusur» retirados; huerto donde «se dice ko / chaltumay al traer agua»; 14 ejercicios abiertos con varias respuestas pasados a cerrados; conteos que no calzaban con el texto (6 oraciones y no 7); «los pueblos indígenas aportan…» generalizado. |",
    "| Educación Física y Salud | 49 | Carreras de 20 m en espacios de 4×3 y 3×3 m; calcetines por vuelta que contradecían el circuito; zapateado y escobillado con 8 tiempos (tienen 4); básquetbol en «tres pasos y pase» (regla de balonmano); polera lavada «cada 2 usos»; botella «compartida» contra «no compartas»; sumas de pulsos sin sentido; pedazos de globo reventado sin advertencia. |",
    "| Orientación | 41 | «Para» como límite ante un contacto en línea contradiciendo «no respondas»; encuentro con alguien conocido solo en línea «con un adulto»; foto íntima descrita de forma explícita; «nadie puede mirar tu cuerpo» sin la excepción del control de salud; estereotipo asociado al país de origen; «habla con la familia» como único factor protector; «mayoría simple» definida como mayoría relativa; datos de drogas con matices de legalidad suavizados. |",
    "| Música | 35 | Ejemplo que pedía 6 músicas y listaba 3 («faltan 12»); criterios 3 de 5 que pasaban a 5 con un solo cambio; tambor grave que «sube»; obra citada sin lugar de baile; melodía de práctica sin ritmo; «¿qué dos preguntas ayudan a conocer el contexto?» con cuatro respuestas válidas; más de 20 menciones a «adulto de tu casa». |",
    "| Artes Visuales | 27 | Forma abierta definida como «contorno cerrado con una abertura»; trabajos C y D con «materiales similares» siendo témpera y papel con pegamento; «gris» como color frío; «menos agua para evitar grumos»; «las sombras no eran negras» sin matiz; tijeras «con el filo hacia adentro»; «ángulo normal» no definido; «cambian tres elementos, ¿cuántos?». |",
    "| Tecnología | 35 | Sumas sin sentido (fichas de tres pruebas, puntajes de cuatro evaluadores) cambiadas por diferencias; puerta de 200 cm a escala 1:2 en una hoja y ranura de 25 cm con pieza de 24 cm que «no encaja»; asas probadas con 5 y 9 kg; perforador sobre paredes de caja; empate de 8 puntos sin criterio; fotos de compañeros sin permiso de todos; «solo 2 de 30 pueden pagarlo» supone la situación económica de las familias. |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "A diferencia de 4.º básico, los lectores de 5.º no hallaron un desajuste que obligara a cambiar el contenido: los títulos de clase del plan son etapas genéricas (por ejemplo «Reconocer propósito y desafío», «Situar pueblo, territorio y fuente», «Definir necesidad, usuario y criterio»), repetidas en todos los OA de la asignatura, y los autores repartieron el contenido del OA dentro de ellas. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Historia (obras de arte coloniales, relieve de Chile, seguridad en hogar, escuela y espacios públicos); Inglés (diálogos del OA 05, ilustraciones del OA 08, canciones del OA 09); Lengua y Cultura (la lengua que corresponde a cada pueblo, en OA 09); Lenguaje (relato en OA 24; comparación de interpretaciones de una descripción de actividad en OA 30); Orientación (pubertad: maduración de los órganos sexuales; ejemplo de burla por pertenecer a un pueblo originario en el OA 06).",
    "- **Abiertos:** Lenguaje OA 30 (testimonio y descripción de actividad solo se reconocen y se comparan, no se planifican paso a paso), OA 01 (prosodia y lectura en voz alta requieren oír al estudiante) y OA 03, 23 y 25 (obras reales, teatro y películas, que elige el docente); Música OA 03 (escuchar al menos 15 músicas y las obras de Chávez, Guastavino y Satie, sin audio) y OA 04 (digitación de flauta y guitarra, práctica real de instrumentos); Artes OA 04 (50 obras al año, las del cuaderno son descripciones), OA 03 (fotografía, video y diseño digital con programa real); Tecnología OA 05 y 06 (programas reales de presentación, hoja de cálculo y procesador de textos; solo se usa la suma); Matemática OA 06, 07, 18 y 20 (calculadora con computador, software geométrico y educativo) y representaciones pictóricas descritas con texto; Inglés (escucha real, pronunciación y producción oral, formato audiovisual); Lengua y Cultura de los Pueblos Originarios: lengua, pronunciación, textos y relatos reales de cada pueblo (LF01 a LF06, LR y LS) con educador o educadora tradicional, y el solapamiento entre LR05 y LS05; Educación Física (danzas de las demás zonas, solo se enseña la cueca); Ciencias (cuadernos sin experimento ni microscopio real, científicos como Galvani, Ampère, Ohm, Joule y Tesla fuera del OA 08).",
    "- **Decisiones que dependen del programa oficial:** acento diacrítico (dé/de, sé/se, más/mas, aún/aun fuera de las clases), vatios, Wh y kWh en Ciencias OA 11, definición de trapecio como un solo par de lados paralelos, «obra universal» como obra fuera de Chile y Latinoamérica, y la regla numérica de «poco posible» (1 o 2 resultados entre muchos), que es una convención del cuaderno.",
    "",
]

MANUAL_6 = [
    "### Segunda lectura crítica de las 876 clases",
    "",
    "Cada una de las 876 clases de 6.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios.",
    "",
    "| Asignatura | Clases | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 98 | Seis ejercicios idénticos al ejemplo resuelto o a la caja de errores frecuentes; «cuántos ángulos iguales» falso con rectas perpendiculares; «complemento» usado para 180° contra complementario de 90° en otro OA; «puerta contra la pared = 180°» no seguro; triángulo 2-2-3 con ángulo de 100° (97°); datos de ejemplo que daban dos modas o no decían cuántos sectores eran rojos; división de decimales por un decimal, que el OA nombra, agregada en OA 07; desigualdad triangular mal enunciada. |",
    "| Lenguaje y Comunicación | 176 | Orden alfabético con ñ mal explicado (la ñ decide en la 5.ª letra); «5 comas» en un texto de 3; «irrompible» como «i- + rompible» (es ir-); «afable es lo contrario de tímido»; «previsible» con «-ble»; «pinta» por escondida; actividades abiertas que citaban un cuento que solo estaba en otros ejercicios (OA 16); figuras literarias dudosas (hipérbole, onomatopeya); aritmética escrita como texto pasada a cálculo verificado; fogata «con ayuda de su papá» cambiada por amasar pan. |",
    "| Ciencias Naturales | 78 | «Un ovario libera un óvulo por ciclo» precisado; recorrido masculino contado con 5 estructuras (enseña 4); energía del carnívoro invertida; «gas invisible porque sus partículas son transparentes»; hielo derretido 8 veces por debajo de lo plausible; orden de estados por separación de partículas falso para el agua; «ilegales» para marihuana y cocaína; «las mareas no dependen del Sol»; sublimación inversa y desertificación usadas sin enseñarlas. |",
    "| Historia, Geografía y Ciencias Sociales | 116 | Pisagua ubicada al sur de Iquique; «dos de los tres patrimonios tienen reconocimiento UNESCO» (uno); «en el altiplano casi no llueve»; una misma persona diputada y concejala a la vez; tribunal que revisa «una ley muy injusta»; fuentes «resumen» usadas como primarias; perspectiva mapuche inventada rotulada de modo que parecía testimonio real; «zonas poco ocupadas» sin mencionar a los pueblos que vivían allí; ser tricontinental como «rasgo único»; soberanía y recurso usados sin definir; relieve agregado en OA 11. |",
    "| Inglés | 74 | Cinco palabras con /r/ y no cuatro; adivinanza con 3 pistas y no 2; «fifty hundred»; «eat bread and tea»; «Penguins live in cold places» (hay pingüinos en Chile); estructuras usadas antes de enseñarse (went, ate, saw, easier, fewer, so); módulo de OA 11 y 12 sobrescrito por error y reescrito; piscina con el lunes sin decir; ejercicios aritméticos sin valor reemplazados. |",
    "| Lengua y Cultura de los Pueblos Originarios | 144 | «Dos de los tres patrimonios» con UNESCO; «colonos en 1900» cuando la memoria decía «antes de 1900»; 328 ejercicios A/B con la A siempre correcta, 168 reordenados; «chocolate (náhuatl)» (etimología discutida) cambiado por «chicle»; «marimari» presentado como error de «mari mari»; ciclo lunar de 29 días como dato; ficha con permiso contradicha por un ejercicio; supuestos sobre la familia («tu abuela», «tu pulsera»); aritmética trivial. |",
    "| Educación Física y Salud | 50 | Pausa activa «cada 45 min en 180» que daba 4 y son 3; dos toallas de 6 cm contra la regla de 10 cm; pausas de bebida cada 15–20 min contra ejercicios de 30; material insuficiente (3 vasos para 6 piezas, «no se usa ningún material» con pelota); supuestos sobre la familia; peso corporal: balanza y «pesa tu peso» retirados. |",
    "| Orientación | 41 | Orden de los pasos ante grooming contradictorio entre ejercicios (decir no, guardar pruebas, bloquear, contar); testigo que confrontaba al agresor; recibir una foto íntima sin indicar no reenviarla; encuentros con desconocidos en línea; «lo íntimo se cuenta solo si uno quiere» que podía leerse como fomento del secreto; «una ofensa repetida es discriminación» (es hostigamiento); «hibernan los osos» (Chile no tiene osos). |",
    "| Música | 35 | Melodía que rompía dos reglas con pregunta de una; 2/4 con dos respuestas válidas; «la lenta» para 80 pulsos contradiciendo los rangos de la clase; accelerando calculado a tempo fijo; ficha de orquesta sin compositor clasificada como tradición escrita; «tu abuela canta»; aritmética trivial recalculada por el verificador. |",
    "| Artes Visuales | 27 | Oscurecer con «azul oscuro»; mural de Siqueiros clasificado como espacio público (está en un interior escolar); interpretación de «Las dos Fridas» con causalidad sin lógica; aguja de bordado sin punta roma; ejercicios cerrados sin opciones; sumas de puntos antes de enseñarse. |",
    "| Tecnología | 37 | «Cuánto sobra» sin dar el largo del material; rango en mm sin tolerancia; regla «mejorar el criterio con menos puntos» contra «la seguridad va primero»; «tela de papel»; «algunas familias no pueden pagar»; frase con coma extra que daba tres errores y no dos; plagio y derechos de autor sin matiz. |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "Como en 5.º, los títulos de clase del plan son etapas genéricas («Reconocer propósito y desafío», «Situar pueblo, territorio y fuente», «Ubicar en tiempo y espacio»…), repetidas en todos los OA de la asignatura. Los autores repartieron el contenido del OA entre las clases y los lectores comprobaron que lo enseñado calza con el OA. En Matemática, además, el insumo y la consigna de cada clase son una plantilla que no corresponde al OA (por ejemplo «Tarjetas numéricas 29, 145, 147» en teselados), por lo que se ignoraron. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Matemática (división de decimales por un decimal, OA 07); Historia (relieve de las cuatro regiones representativas, OA 11); Inglés (sonido /r/ en OA 02).",
    "- **Abiertos:** software geométrico, educativo y de presentación (Matemática OA 03, 04, 05, 12, 15, 20 y 23; Tecnología OA 05, 06 y 07); audio, video y formato audiovisual (Inglés, Lenguaje OA 26, Música); lectura en voz alta y fluidez real (Lenguaje OA 01); obras completas, plan lector y relatos históricos reales (Lenguaje OA 03, 04, 06 y 23); las 50 obras al año (Artes OA 04, el cuaderno describe unas 10 con texto) e imágenes; práctica de herramientas de taller (Tecnología OA 03); producción en lengua indígena, lenguajes artísticos propios del pueblo y lengua y relatos reales (Lengua y Cultura, con educador o educadora tradicional); pruebas de 50 y 100 m y danzas del norte, sur e Isla de Pascua (Educación Física); investigación experimental real (Ciencias OA 01, 09 y 13); elección de curso y voluntariado reales (Historia OA 22 y 23); biblioteca, buscador e internet reales (Lenguaje OA 09 a 12).",
    "- **Decisiones que dependen del programa oficial:** definición de isósceles como «exactamente dos lados iguales», ángulos suplementarios, umbrales de «pocas» y «muchas» repeticiones, 100 °C como punto de ebullición sin ajuste por altura, y las convenciones propias del cuaderno (rangos de tempo, escala de esfuerzo 0 a 10, regla de palabras desconocidas por cada 100).",
    "",
]

MANUAL_7 = [
    "### Segunda lectura crítica de las 719 clases",
    "",
    "Cada una de las 719 clases de 7.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios. Las fichas de actitud y la asignatura de Lengua Indígena de 7.º son integración transversal y no llevan cuaderno propio.",
    "",
    "| Asignatura | Clases | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 83 | Enunciados imposibles («tres enteros de valor absoluto menor que 4 y menores que −1», solo hay dos; una reducción lineal incorrecta que coincide en dos puntos); dato irreal de 69 cuadritos completos y 20 partidos en un círculo de radio 5 (son 60 y 28); mediana de 7,5 cm en un triángulo de 9, 8 y 6 cm que no existe; pares ordenados «(7,5)» que en Chile se leen como decimal, ahora «(7, 5)»; piso −3 fuera de un edificio que llegaba al −2; descomposición del paralelogramo «en trapecio y triángulo» no general; división de fracciones planteada como reparto; términos usados sin definir (mediana, hipotenusa, fracción irreducible, puntos porcentuales). |",
    "| Lengua y Literatura | 147 | Rima y asonancia con diptongos revisadas vocal por vocal; contradicciones entre regla y explicación («al menos 3 evidencias» contra «dos o tres»); eje de un gráfico que hacía parecer «el triple» lo que era 2,5 veces; «decido» en una lista de participios mal formados; texto con coma «que sobra» que era válida; «reímos» y verbos en -ar con la misma forma en presente y pasado; respuestas Sí/No sesgadas (50 No contra 16 Sí) reformuladas; homófonos y tildes verificados; alternativas absurdas reescritas. |",
    "| Ciencias Naturales | 72 | Abstinencia y preservativo en una misma lista con «el único que reduce ITS»; ventana fértil calculada del 9 al 15 cuando con ovulación el día 16 es del 11 al 17; términos de biología usados antes de enseñarlos (estrógenos, anticuerpos, páncreas, insulina); ciclo del aire y estaciones precisados (el verano austral es de fines de diciembre a fines de marzo); leche agria «por el sabor»; seis casos de riesgo cerrados en «avisar a un adulto»; datos de tectónica y volcanes sin imprecisión. |",
    "| Historia, Geografía y Ciencias Sociales | 113 | La Moneda «terminado en 1805 por Toesca» (Toesca murió en 1799); «los aztecas cultivaban cacao» (lo recibían como tributo); «chocolate» como palabra náhuatl de etimología discutida; cirílico atribuido directamente a Cirilo y Metodio; fortalezas incas «al sur del Maule»; un dux vitalicio contado entre cargos temporales; fuentes «independientes» que repetían la misma noticia; ostracismo ejemplificado con un acusado; ciclos de refuerzo y equilibrio confundidos; andenes (OA 14), minoica, fenicia, olmeca y chavín (OA 04) agregados para cubrir el OA. |",
    "| Inglés (propuesta EN07) | 65 | «While Ana was cooking, her brother ___ music» con dos respuestas gramaticales; «has» sin considerar «have»; «going to» y «leather» usados sin enseñar; pasado irregular y comparativos sin regla; cinco palabras con /r/ y no cuatro; adivinanza con 3 pistas y no 2; «Penguins live in cold places» (hay pingüinos en Chile); módulo de OA 11 y 12 de 6.º reescrito tras una sobrescritura. |",
    "| Inglés (oficial IN07) | 80 | «table» presentado como cognado de «tabla» (falso amigo); torta de chocolate para un perro; «must» usado antes de enseñarlo; «Pia plays the violin every Thursday. Today is Friday» sin probar nada; «Dear Mr. Pedro Gonzalez»; «es obligatorio» el casco sin certeza legal; OA 11 reescrito tras una sobrescritura; colocaciones y «too much/too many» agregados para cubrir el OA 08. |",
    "| Educación Física y Salud | 25 | Ejemplo de respuesta que mandaba recoger vidrio; subir y bajar peldaños dentro de la casa; máquinas de ejercicio al aire libre; metas de 150 minutos semanales contra 30 diarios del OA; salto de 200 cm irreal; la plancha, «finta», «interceptar» y «golpe de calor» usados sin enseñar; supuestos sobre la familia («tu mamá», «tu hermano pequeño»). |",
    "| Orientación | 49 | Pasos ante grooming contradictorios («guardar el chat» contra no guardar imágenes íntimas); víctima o testigo enfrentando al agresor como primer paso; recibir una petición culpada; número de ayuda inventado (solo se usa 147); «cambios hormonales» sin enseñar; frase agresiva que podía leerse como asertiva; ejercicios de sueño con la respuesta en el paréntesis. |",
    "| Música | 30 | «Compás 1» de 16 unidades que sumaba 20; distancia 3 donde era 4; «2 minutos» para 36 tiempos de respiración; escala de niveles sin definir; «palmas» como medio sonoro y corporal a la vez; viola y violonchelo sin enseñar; «marchar» y «acto cívico» ambiguos. |",
    "| Artes Visuales | 29 | «El doble de grande, 2 y 4 tazas» (el volumen se multiplica por 8); engrudo secado en 20 minutos por capa; escultura de cartón de 3 m en una plaza contra una clase de cuidado; foto de una compañera «sin permiso de su familia»; «base al menos la mitad de la altura» como regla; plano medio contradicho por el cielo; «pieza de adolescente». |",
    "| Tecnología | 26 | Repartos que dejaban «sobra 0 cm²» cuando la consigna pedía usar los retazos; 20 ÷ 8 = 2,5 MB fuera de cifras enteras; criterio «peso» que chocaba con el «peso» de ponderación; rampa de cartón y madera para una silla de ruedas; «pincharse» con tijeras; «tu hermano de 6 años». |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Definir necesidad…», «Recognize purpose and context», «Situar pueblo, territorio y fuente»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. En Historia, Ciencias, Música, Educación Física, Orientación y parte de Lengua y Literatura los títulos sí coinciden con el contenido. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Matemática (valor de π y estimación del círculo en OA 11); Ciencias (anticoncepción general y métodos, cuidado de materiales); Historia (andenes y sistemas de cultivo en OA 14; minoica, fenicia, olmeca y chavín en OA 04; ecúmene, romanización, Euclides y Juegos Olímpicos); Inglés propuesta («I want / don't want» y «a few»); Inglés oficial (preguntar para clarificar, colocaciones y palabras compuestas del OA 08, «too much / too many», instructions).",
    "- **Abiertos:** software educativo, geométrico y de presentación (Matemática OA 03, 12, 15, 16, 18 y 19; Tecnología OA 04); audio, video y escucha (Inglés, Lengua y Literatura OA 20, Música); obras completas, plan lector, romances y lira popular reales, mitos de pueblos originarios (Lengua y Literatura OA 02, 05 y 06); reglas de ortografía literal completas (OA 19: faltan h, g/j, ll/y); sacrificios humanos y relaciones de género (Historia OA 08 y OA 15); anticoncepción de emergencia (Ciencias OA 02); esclavitud en Roma sin clase propia (OA 07); ortocentro y bisectrices en cuadriláteros (Matemática OA 12); pasos concretos de danza y gimnasia (Educación física OA 01); obras reales, imágenes y visitas a museos (Artes); mediciones y experimentos reales (Ciencias OA 07 a 15, Tecnología OA 02).",
    "- **Decisiones que dependen del programa oficial:** el listado de temas y obras del curso (Lengua y Literatura OA 02), la definición escolar de embrión y feto (semana 8), K = °C + 273 en Ciencias, la convención 1 GB = 1.000 MB, el estatus de los vectores libres y de «pocas» y «muchas» repeticiones, y las reglas propias del cuaderno rotuladas como tales (escala de esfuerzo, regla «6 por 6», rangos de palabras por minuto).",
    "",
]

MANUAL_8 = [
    "### Segunda lectura crítica de las 728 clases",
    "",
    "Cada una de las 728 clases de 8.º básico fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta cada ejercicio cerrado y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios. Las fichas de actitud y la asignatura de Lengua Indígena de 8.º son integración transversal y no llevan cuaderno propio.",
    "",
    "| Asignatura | Clases | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 77 | Ejemplo cuyo «error» no se veía (cilindro con r = 2 y h = 5 da 62,8 con la fórmula buena y con la mala); respuestas parecidas que confundían (13.000 y 5); definición de percentil que se contradecía con la regla del cuaderno y percentil 100 sin dato i+1; raíz cuadrada, cuadrantes en número romano y fórmula del ángulo interior usados sin enseñar; contar cuadritos del cuadrado inclinado sin pista; «completa la tabla» sin tabla; edades de «personas que conozcas» cambiadas por datos inventados; «interés compuesto» usado cuando la clase solo trata el simple. |",
    "| Lengua y Literatura | 155 | Clave errada (OA 15: la correcta era la b); aleteos del colibrí, miel por abeja obrera y «las abejas viven en colonias» (hay solitarias); murciélagos que polinizan (los de Chile son insectívoros); conservar alimentos «sin refrigerador»; fragmentos T1 a T5, el «Canto de Ilén» y «El reloj de Elisa» citados en preguntas sin estar en la clase; rima consonante y tópicos verificados; «hubo/hubieron», «entre tú y yo» y subjuntivo revisados; «tal vez» con ambos modos; «Hoy necesito: cuaderno» incorrecto tras verbo; «lápiz» como grave (es esdrújula); voseo «decís». |",
    "| Ciencias Naturales | 74 | Pared celular «solo vegetal» contra la clase de bacterias; inducción sin quitar la conexión a tierra; mito del celular encendido en la bencinera; lista de los 20 elementos solo en la clase 1 y usada en las clases 3 y 4; promedio ponderado y modelo de Thomson usados sin enseñar; datos de calentamiento del hielo incoherentes con una fuente constante; «los átomos no se ven» demasiado categórico; ejemplo de luz y burbujas que no sigue el inverso del cuadrado, rotulado como patrón de ejemplo. |",
    "| Historia, Geografía y Ciencias Sociales | 117 | Alta Navarra en 1512 y 1515; «leones» del grabado colonial que podían ser pumas; capitán neerlandés fechado en 1600 (1605); «6 artículos» frente a 8; IDH regional que no calzaba con el promedio ponderado; «más fuentes de soldados» falso (5 y 5); consumo definido contra intercambio; años en miles («1.818»); salmones presentados solo como ventaja; Leonardo y Miguel Ángel (OA 01), Zipoli, autos sacramentales y Sor Juana (OA 09) agregados para cubrir el OA. |",
    "| Inglés (propuesta EN08) | 65 | «The gym is behind the garden» y otros ordenamientos con más de una respuesta; «Reescribe con I would like to…» pasado a opción múltiple; el sonido inicial de «brother» pedido como /θ/; «I seen» al revés; «fifteen after four» y «ninetieth» de octubre; «by 5 p.m.» contra la voz pasiva; edad calculada que dependía del cumpleaños; «Bees make honey» generalizado; «quite» británico frente a estadounidense. |",
    "| Inglés (oficial IN08) | 80 | Texto con «three rooms» y cuatro salas; «sea bass» como corvina; «Owls hunt at night» y «Penguins live in cold places» generalizados; «tea bags» en el compost; biblioteca «open every day» y «closed on weekends»; «Paper Boat» que era un gorro; cadenas en las ruedas de una bicicleta; /t/ después de ch; regla «i antes de e» sin excepciones; título repetido con 7.º; colocaciones del OA 08 sin ejercicio, agregadas. |",
    "| Educación Física y Salud | 26 | Cuerda a la altura de la cabeza y entre sillas; 3 contra 3 con 2 o 3 personas; vóleibol de duplas sin cuatro personas; zonas de 3 m en una cancha de 6 m; meta de 150 minutos contra 30 diarios; «subió de 4 a 6 y bajó a 3»; materiales (globo, pared, caja) no entregados; ejemplos que no cumplían la consigna (2 materiales cuando se piden 3). |",
    "| Orientación | 49 | «Bórrala» ante una imagen íntima recibida, cambiado por no reenviar ni guardar la imagen y no borrar el chat; orden de pasos ante grooming (decir no, guardar captura, bloquear, contar a un adulto); distractores «911» y «112» que parecían líneas de ayuda (solo se usa el 147); amigo que bebió mucho dejado «solo»; «una vez no genera adicción» imprecisa; «Cesfam» sin definir; supuestos sobre la familia («tu mamá»). |",
    "| Música | 30 | Pedía qué acorde se siente más cerca del reposo cuando la clase solo enseña I y V; sección B igual a A en una forma ABA; «grados» contados de dos maneras (ahora «escalón»); motivo, puente, cifrados, soprano y bajo usados sin definir; síncopa pedida antes de enseñarse; homenaje a una persona fallecida cambiado; alternativas absurdas reescritas. |",
    "| Artes Visuales | 29 | Opción «segura» con hilos colgados a la altura de la cabeza; pegamento fuera de la lista de materiales; 2 obras de 70 cm en 360 cm con espacio decimal; ejemplo que cambiaba dos decisiones cuando la consigna dice una; «una instalación es temporal» y «los colores vivos transmiten energía» demasiado categóricos; supuesto de que los adultos mayores no tienen internet; altura de montaje de 150 cm como referencia, no como norma. |",
    "| Tecnología | 26 | Repartos de piezas por plancha con el cálculo regalado y el área mal contada (6000 ÷ 875 da 6,86); error relativo de 2,67 % fuera de cifras enteras; ejemplo de «impacto medio» cuando la consigna pide alto o bajo; pregunta de encuesta neutra, promedio y citar la fuente usados sin enseñar; 18 alternativas absurdas; tarea con un aparato conectado sin aviso de no abrirlo. |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Recognize purpose and context», «Definir necesidad, usuario y criterio», «Examinar un caso ficticio…»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. En Lengua y Literatura, Historia y Ciencias los títulos coinciden en general con el contenido. La clase 3 de OA 20 de Lengua y Literatura se titula «punto y coma», que no figura en el texto del OA, y se siguió el título del plan. Conviene que el currículo nombre el tema de cada clase; no se hizo aquí porque exige el Programa de Estudio.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Lengua y Literatura (tópicos literarios en OA 05); Historia (capacidad de transformar el mundo y expresiones culturales en OA 01, música y teatro barrocos en OA 09); Inglés oficial (preguntar para clarificar, colocaciones y palabras compuestas del OA 08); Inglés propuesta («I want / don't want» y «a few» en 7.º, y en 8.º la voz pasiva y who/which).",
    "- **Abiertos:** software educativo, geométrico y de simulación (Matemática OA 07, 09, 10, 12 a 15); audio, video, escucha, canciones y pronunciación real (Inglés, Lengua y Literatura OA 12 y 21, Música); obras completas, epopeyas y comedias reales y el plan lector (Lengua y Literatura OA 02, 06 a 08); ortografía literal completa (OA 20: faltan c/s/z, y/ll, x, mayúsculas, siglas); deícticos por nombre (OA 18); procesador de textos y diccionario en línea (Lengua y Literatura OA 16, Inglés); investigación experimental real y reactivos (Ciencias OA 06); entornos reales de práctica (Educación Física OA 01 y 04); rotaciones en el espacio y poliedros distintos del cubo y los prismas (Matemática OA 14); cuartiles con n impar y valores atípicos (OA 15); evangelización y roles de género con clase propia (Historia OA 11); formación del Estado nacional como clase propia (OA 19); pirámides de población y migración internacional (OA 21); patrimonio de pueblos originarios concreto (Artes OA 04).",
    "- **Decisiones que dependen del programa oficial:** regla de percentiles y cuartiles (i = p·n/100) y bigotes al mínimo y al máximo; π = 3 y 3,14; tarifa de $200 por kWh; sentido antihorario positivo; 6/8 como dos pulsos; «escalón» frente a grado; escala de esfuerzo 1 a 10 y reglas propias de cada clase en Educación Física; forma de contar «grados» de un intervalo.",
    "",
]

MANUAL_M1 = [
    "### Segunda lectura crítica de las 753 clases",
    "",
    "Cada una de las 753 clases de 1.º medio fue releída por un segundo lector (asistido por IA, distinto de quien la escribió) que la contrastó con el texto del OA y el título de la clase en la ficha del repositorio, resolvió por su cuenta los ejercicios cerrados y corrigió los defectos en el mismo archivo. **No es revisión profesional humana**, y no se abrieron los enlaces del Currículum Nacional. Los autores declararon que no resolvieron uno por uno todos sus ejercicios, y dos lectores (Inglés propuesta OA 01 a 10 e Inglés oficial OA 01 a 10) leyeron y comprobaron datos sin resolver cada ejercicio a ciegas; una tercera lectura independiente de los 19 bloques resolvió de nuevo cada ejercicio cerrado y corrigió unas 800 ediciones puntuales (ejercicios triviales, distractores absurdos, respuestas que se delataban, preguntas con más de una respuesta y solapes entre los dos Ingleses). Las fichas de actitud y la asignatura de Lengua Indígena son integración transversal y no llevan cuaderno propio.",
    "",
    "| Asignatura | Clases | Defectos corregidos (resumen de los informes) |",
    "|---|---:|---|",
    "| Matemática | 66 | Unos 60 ejercicios que repetían un ejemplo de la explicación o un ejemplo resuelto; error de estudiante mal descrito («2^-3 < 2^-5 porque −3 < −5» es falso); «semejantes» y «eje x» usados antes de enseñarse; pregunta de homotecia que no consideraba las rectas por el centro; «1.º A» con 30 estudiantes contra un ejemplo de 20; «menos de 0 errores»; juego con dinero cambiado por puntos; fila 4 del triángulo de Pascal ambigua. |",
    "| Lengua y Literatura | 143 | Diptongo «cui-da-do» en la fila equivocada; «ardilla» como diminutivo en -illa; «Completa con b o v» con respuesta g; saludo «Querida Ana,» aceptable pero usado como distractor; «sábado 10 + dos días» llegaba al lunes; mayúscula tras el saludo de una carta formal; unas 35 sumas triviales reemplazadas por ejercicios de contenido; unas 25 consignas abiertas pasadas a opción múltiple; citas de un poema no entregado; «el río se repite» que era falso; «cardal» y otros datos inseguros; termómetro doméstico con mercurio. |",
    "| Ciencias Naturales | 100 | Ejemplo de coincidencias de rasgos mal contado (0 y 0 donde eran 1 y 1); ala de ave y de murciélago presentadas como homólogas; géneros reales con conteos de especies inventados; tabla de temperatura y volumen que contradecía a otra; explicación de las estaciones con el invierno austral invertido; tabla de hipocentros que no calzaba con el ejercicio; Pitágoras y «infiltración», «kWh» usados sin enseñar; vela encendida en un frasco cerrado, espejo de vidrio y elástico estirado reemplazados por opciones seguras; pregunta sensible de evolución frente a creación reformulada. |",
    "| Historia, Geografía y Ciencias Sociales | 132 | Unas 150 consignas y contextos que citaban fuentes, cuadros o dossiers «de este cuaderno» sin traerlos; las mujeres «votaron» en 1934 y 1949 (obtuvieron el derecho); tabla con 800 inscritos de los que 500 sabían leer contra una regla que exige saber leer; ferrocarril a Temuco, primer censo de 1854 y «libre tránsito» imprecisos; África con 10 % de control europeo fechada en 1880 (1870); edad del voto de 1874 sin sustento; Brasil omitido en la abolición; «cambio climático» definido como variación natural; «militante comunista» anacrónico en 1905; ejercicio que pedía a un estudiante representar a un pueblo. |",
    "| Inglés (propuesta EN1M) | 65 | Ejercicios que repetían un ejemplo resuelto; «And ___» que aceptaba last y finally; «Although it is cheap, the bag is not strong» sin contraste real; ejemplos de respuesta que no calzaban con los datos; esquema «de la clase anterior» sin traerlo; shall presentado como futuro seguro; supuestos sobre la familia; texto de «School uniforms» con el mismo tema que el Inglés oficial; una opción A/B con doble coma. |",
    "| Inglés (oficial IN1M) | 80 | Opción «5–14 January» contra clave «5–16»; /tr/ y /dr/ explicados como si el español no los tuviera; -tion enseñado como /ʧ/ (es /ʃən/); orden de adjetivos usado sin enseñarse; razón errónea sobre «honest» y la h; inglés británico y americano mezclados en un pasaje (unificado en americano); contextos de museo, mercado y bicicletas idénticos a los de Inglés propuesta, cambiados. |",
    "| Educación Física y Salud | 28 | Pasar de «defensa a atacar» desde 2-2-1 llevaba a 1-2-2, no a 2-1-2; plan de baile que subía a 35 minutos con un máximo de 30; caminar de espaldas y círculos de cuello eliminados; pulso en la muñeca sin presionar el cuello; «me molestó la espalda» como razón para seguir con la plancha; alternativas de alimentación que sugerían restringirse; unas 20 alternativas absurdas. |",
    "| Orientación | 52 | Unas 130 preguntas de recuperación de tipo «¿X es Y, sí o no?» que regalaban la definición; afirmación de que todo contacto íntimo de un adulto con un menor es delito (no lo es a los 14 a 17 años); protocolo en línea con el orden «bloquear y luego guardar captura» (ahora guardar captura, bloquear, avisar); kiosco del colegio con sellos «ALTO EN»; ejemplo que suponía que Ema ya había pedido orientación; soldadura reemplazada por circuitos con pila y LED; Fono Niños 147 descrito como «atendido por profesionales» sin sustento. |",
    "| Música | 32 | Ejemplo y ejercicio que cambiaban tempo y volumen a la vez cuando la clase enseña a cambiar un solo rasgo; «la 1» como única respuesta cuando cumplían la 1 y la 4; patrón de golpes repetido del ejemplo resuelto; «compás fuerte» sin definir; «desafinar» usado para la pentatónica; empate de minutos entre dos estudiantes; «funeral» y «persona de la familia» cambiados. |",
    "| Artes Visuales | 29 | Doce puntos máximos donde dos criterios dan 6 (ahora 9 en tres criterios); cifras de rampa, muro y litros de pintura repetidas del ejemplo; «tallar» la matriz y libro cosido con aguja cambiados por cartón pegado y cordel; ficha de grabado sin tamaño; «saturado» sin definir. |",
    "| Tecnología | 26 | Ejemplos de respuesta que no calzaban con la consigna (6 criterios pedidos y 3 dados); promedio de 3,875 fuera de cifras enteras; ejercicio trivial «1 o 5»; afirmación categórica sobre derechos de autor suavizada; protocolo de seguridad digital completado con «no se borra el chat ni se reenvía una imagen íntima». |",
    "",
    "#### Desajuste entre el texto del OA y los títulos de las clases",
    "",
    "Los títulos de clase del plan son etapas genéricas, repetidas en todos los OA de cada asignatura (por ejemplo «Recognize purpose and context», «Definir necesidad, usuario y criterio»), y los autores repartieron el contenido del OA entre ellas. Los lectores comprobaron que lo enseñado calza con el OA. Casos señalados: Tecnología OA 01 avanza hacia priorizar e idear aunque el OA pide identificar oportunidades; los tres entornos de Tecnología OA 05 (natural, construido y digital) y las cuatro «dimensiones de la experiencia humana» de Lengua y Literatura OA 02 son interpretación de los autores, no texto del OA; la clase 6 de Educación Física OA 03 se dedicó a ingesta y gasto calórico.",
    "",
    "#### Vacíos de cobertura frente al OA",
    "",
    "- **Cerrados dentro de las clases existentes:** Inglés oficial (excepción «question» /tʃ/ en OA 02); Inglés propuesta (caracterización del personaje en OA 04); Inglés oficial OA 14 (cuento y resumen).",
    "- **Abiertos:** software educativo y geometría dinámica (Matemática OA 04, 05, 08, 09, 11, 14 y 15); audio, video, canciones, noticieros y pronunciación real (Inglés, Lengua y Literatura OA 19 y 21, Música); obras completas del programa y plan lector (Lengua y Literatura OA 01, 02, 06 y 07; el Lazarillo de Tormes en OA 03); cuentos, artículos y diario personal (Inglés propuesta OA 11); narraciones y exposiciones orales como formatos (Inglés propuesta OA 01); mitos, leyendas y novelas adaptadas (Inglés propuesta OA 04); técnica real por deporte, RCP y maniobras de atragantamiento (Educación Física OA 01 y 04); segmento circular de 120° (Matemática OA 06, exige trigonometría de 2.º medio); lupa e instrumentos ópticos (Matemática OA 08); aportes de científicos en Ciencias OA 02; salitre y guano como exportaciones (Historia OA 10); flujos del Estado con subsidios y gasto público (Historia OA 19); casos de quechua, colla, diaguita, atacameño, kawéskar y yagán (Historia OA 24); procesador de textos y diccionario en línea (Lengua y Literatura OA 15, Inglés); institutos locales de protección y sexualidad integral más allá de lo general (Orientación OA 02 y 03).",
    "- **Decisiones que dependen del programa oficial:** notación en unidades de duración (corchea = 1) y términos «compás fuerte» y «densidad» de Música; formato de cita acordado `(Apellido, año, v. N)` de Lengua y Literatura; ortografía de «kawéskar» y «yagán»; fórmulas de pendiente de rampa 1 en 12 y alturas de montaje de 150 cm de Artes Visuales como referencia; rango 60 a 80 % de la frecuencia cardíaca máxima estimada de Educación Física.",
    "",
]


LEVELS = (("1-basico", 1, MANUAL_1), ("2-basico", 2, MANUAL_2), ("3-basico", 3, MANUAL_3), ("4-basico", 4, MANUAL_4), ("5-basico", 5, MANUAL_5), ("6-basico", 6, MANUAL_6), ("7-basico", 7, MANUAL_7), ("8-basico", 8, MANUAL_8), ("1-medio", 9, MANUAL_M1))


def section(level_prefix: str, grade: int, manual: list[str]) -> list[str]:
    label = f"{grade}.º básico" if grade <= 8 else f"{grade - 8}.º medio"
    rows = analyse(level_prefix)
    limit = MAX_SENTENCE_WORDS.get(grade, 20)
    flagged = [r for r in rows if (r["coverage"] < LOW_OA and r["title_cov"] < MIN_COVERAGE) or r["sentence"] > limit or r["smells"]]
    by_subject: dict[str, list[dict]] = {}
    for row in rows:
        by_subject.setdefault(row["subject"], []).append(row)
    out = [
        f"## {label}",
        "",
        f"Criterio de marca: cobertura del OA menor que {int(LOW_OA * 100)} % **y** del título menor que {int(MIN_COVERAGE * 100)} %, o explicación con oraciones de más de {limit} palabras en promedio, o respuestas «depende» en ejercicios cerrados.",
        "",
        "### Resumen por asignatura",
        "",
        "| Asignatura | Clases | Cobertura media del OA y título | Clases marcadas |",
        "|---|---:|---:|---:|",
    ]
    for subject, items in sorted(by_subject.items()):
        mean = 100 * sum(r["coverage"] for r in items) / len(items)
        marked = sum(1 for r in items if r in flagged)
        out.append(f"| {subject} | {len(items)} | {f'{mean:.0f}'} % | {marked} |")
    out += ["", f"**Clases marcadas para lectura prioritaria ({label}):** {len(flagged)} de {len(rows)}.", ""]
    out += manual
    if flagged:
        out += [f"### Clases marcadas de {label}", "", "| OA | Clase | Título planificado | Cobertura OA | Cobertura título | Oración media | Señales |", "|---|---:|---|---:|---:|---:|---|"]
        for row in sorted(flagged, key=lambda r: (r["coverage"], r["code"])):
            out.append(f"| {row['code']} | {row['number']} | {row['title'][:60]} | {100 * row['coverage']:.0f} % | {100 * row['title_cov']:.0f} % | {row['sentence']:.1f} | {'; '.join(row['smells']) or '—'} |")
        out.append("")
    return out


def report() -> str:
    out = [
        "# Análisis de alineación con el OA oficial",
        "",
        "Este análisis contrasta cada cuaderno con el **texto oficial del OA** y con el **título de la clase planificada**: mide qué parte de sus términos de contenido aparece realmente en el cuaderno, la longitud media de las oraciones de la explicación y algunas señales pedagógicas débiles. **No** juzga exactitud disciplinar: ordena las clases para que una persona lea primero las más débiles. Se regenera con `python scripts/audit_alignment.py --write`.",
        "",
        "**Límite de la medida.** Es una heurística de triage por coincidencia de términos: sobre-marca, sobre todo en Inglés, donde el título planificado es metalenguaje docente («Connect prior knowledge») que no aparece en un cuaderno para estudiantes, y en las clases de Lengua y Cultura, cuyo título lleva rótulos de método. Una marca no prueba un defecto; una ausencia de marca no prueba exactitud.",
        "",
    ]
    for level_prefix, grade, manual in LEVELS:
        out += section(level_prefix, grade, manual)
    return chr(10).join(out)


def main(argv: list[str]) -> int:
    text = report()
    if "--write" in argv:
        REPORT.write_text(text, encoding="utf-8", newline="\n")
        print("Análisis de alineación escrito.")
        return 0
    if not REPORT.exists() or REPORT.read_text(encoding="utf-8") != text:
        print("docs/ANALISIS_ALINEACION.md no está sincronizado; ejecuta audit_alignment.py --write")
        return 1
    print("Análisis de alineación sincronizado.")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
