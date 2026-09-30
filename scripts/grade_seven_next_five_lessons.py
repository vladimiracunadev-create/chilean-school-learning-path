"""Developed seventh-grade sequences for the next five requested subjects.

The module covers Science, History, English, Physical Education and Visual
Arts.  Profiles are derived from the checked-in MINEDUC snapshot, while the
classroom situations, progressions and common misconceptions are original to
this repository.  Generated Markdown and HTML must be rebuilt with
``generate_school_program.py``.
"""
from __future__ import annotations

import json
from pathlib import Path

try:
    from grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from grade_three_science_history_lessons import _lesson as inquiry_lesson
    from grade_four_remaining_lessons import build_transversal_integration as base_integration
except ImportError:
    from scripts.grade_three_arts_pe_english_indigenous_lessons import _lesson as applied_lesson
    from scripts.grade_three_science_history_lessons import _lesson as inquiry_lesson
    from scripts.grade_four_remaining_lessons import build_transversal_integration as base_integration


ROOT = Path(__file__).resolve().parents[1]
SNAPSHOT = json.loads((ROOT / "sources/mineduc-curriculum-snapshot.json").read_text(encoding="utf-8"))
TARGET_SLUGS = {
    "ciencias-naturales",
    "historia-geografia-ciencias-sociales",
    "ingles",
    "educacion-fisica-salud",
    "artes-visuales",
}


def _entry(topic: str, facets: str, anchor: str, misconception: str) -> dict:
    return {
        "topic": topic,
        "facets": [part.strip() for part in facets.split("|")],
        "anchor": anchor,
        "misconception": misconception,
    }


CONTENT = {
    # Ciencias Naturales
    "CN07 OA 01": _entry("Sexualidad, pubertad, afectividad y responsabilidad", "Distinguir cambios de la pubertad sin estereotipos|Relacionar dimensiones biológicas, afectivas y sociales|Examinar respeto, consentimiento y cuidado mutuo|Tomar decisiones responsables sin exposición personal", "siluetas y tarjetas de casos ficticios sobre pubertad, vínculos respetuosos y decisiones de cuidado, con preguntas anónimas y protocolo escolar", "reducir la sexualidad a cambios físicos, imponer experiencias o asumir que todas las personas viven la pubertad de la misma manera"),
    "CN07 OA 02": _entry("Formación de un nuevo individuo y reproducción humana", "Representar ciclo menstrual y ventana fértil sin usar calendarios personales|Relacionar fecundación, implantación y desarrollo inicial|Distinguir embrión, feto y etapas de gestación|Explicar responsabilidad reproductiva con fuentes sanitarias", "modelo secuencial, calendario didáctico ficticio y tarjetas de fecundación, implantación, desarrollo embrionario y fetal", "presentar el ciclo como idéntico en todas las personas, confundir fecundación con implantación o convertir probabilidades en certezas"),
    "CN07 OA 03": _entry("Infecciones de transmisión sexual y prevención informada", "Distinguir agente, transmisión y manifestaciones|Comparar ITS sin asociarlas a identidades|Examinar prevención, consulta y tratamiento desde fuentes vigentes|Evaluar información y mitos con cuidado de la privacidad", "fichas sanitarias didácticas de VIH, hepatitis B, herpes y otras ITS, rutas de transmisión ficticias y una matriz de fuente, evidencia y límite", "creer que una ITS siempre es visible, estigmatizar personas o presentar una medida preventiva como protección absoluta"),
    "CN07 OA 04": _entry("Barreras defensivas del cuerpo humano", "Reconocer barreras primarias|Modelar respuesta innata o secundaria|Modelar respuesta adaptativa o terciaria|Relacionar memoria inmunológica y vacunación|Integrar las defensas sin convertir el modelo en una copia literal", "modelo por capas de piel, inflamación, células defensivas, anticuerpos y memoria inmunológica, junto con un caso ficticio de ingreso de un patógeno", "imaginar las defensas como murallas independientes o atribuir a los antibióticos la eliminación de cualquier agente"),
    "CN07 OA 05": _entry("Virus, bacterias y hongos", "Comparar estructura y escala|Contrastar formas de reproducción|Distinguir condiciones de vida y dependencia|Examinar efectos beneficiosos y perjudiciales|Construir una comparación que declare límites", "micrografías atribuidas, modelos a distinta escala y tarjetas de estructura, reproducción, hábitat y efecto de virus, bacterias y hongos", "tratar a todos los microorganismos como dañinos, usar la misma escala o clasificar virus como bacterias pequeñas"),
    "CN07 OA 06": _entry("Microorganismos y biotecnología", "Reconocer usos alimentarios de microorganismos|Explicar aplicaciones ambientales|Examinar aplicaciones productivas o sanitarias|Relacionar condiciones, proceso y producto|Evaluar beneficios, riesgos y límites", "diagramas de fermentación, compostaje, biorremediación y producción biotecnológica con organismos, condiciones, producto y control claramente identificados", "suponer que biotecnología significa solo modificación genética o que cualquier crecimiento microbiano es seguro y beneficioso"),
    "CN07 OA 07": _entry("Fuerzas gravitacionales, de roce y elásticas", "Formular una pregunta medible sobre fuerzas|Diseñar una comparación controlada|Medir y representar fuerza o movimiento|Distinguir gravedad, roce y elasticidad en los resultados", "dinamómetros escolares, bandas elásticas, bloques sobre superficies distintas y masas seguras, con tabla de variable independiente, respuesta y controles", "cambiar masa y superficie al mismo tiempo, confundir fuerza con movimiento o concluir desde una sola medición"),
    "CN07 OA 08": _entry("Presión en sólidos, líquidos y gases", "Relacionar fuerza y área de contacto|Explorar presión con profundidad en líquidos|Reconocer presión de gases y atmósfera|Explicar aplicaciones cotidianas con un modelo de partículas", "bloques con caras de distinta área, recipiente transparente con salidas a varias alturas y jeringas sin aguja de uso exclusivo experimental", "confundir presión con fuerza total, afirmar que actúa en una sola dirección o extrapolar el modelo sin considerar sus límites"),
    "CN07 OA 09": _entry("Tectónica de placas y actividad geológica", "Relacionar capas terrestres y movimiento de placas|Leer patrones de sismos y volcanes en mapas|Distinguir límites convergentes, divergentes y transformantes|Explicar el caso de Chile sin presentarlo como excepción|Usar evidencia para evaluar el modelo", "mapas mundiales superpuestos de placas, sismos y volcanes, perfiles de límites y una ampliación de las placas de Nazca y Sudamericana", "imaginar placas flotando sobre lava líquida, creer que los continentes son las placas completas o explicar cada sismo del mismo modo"),
    "CN07 OA 10": _entry("Actividad volcánica, consecuencias y riesgo", "Distinguir magma, lava, gases y ceniza|Relacionar propiedades del magma con estilos eruptivos|Examinar efectos naturales y sociales|Tomar decisiones de prevención desde mapas oficiales", "modelo seccionado de volcán, registros didácticos de viscosidad y gases, mapa ficticio de amenaza y tarjetas de rutas y zonas seguras", "usar un volcán de bicarbonato como modelo completo, tratar peligro y riesgo como sinónimos o improvisar recomendaciones de emergencia"),
    "CN07 OA 11": _entry("Ciclo y transformación de las rocas", "Reconocer rasgos de rocas ígneas, sedimentarias y metamórficas|Relacionar enfriamiento, sedimentación, presión y temperatura|Construir un ciclo sin inicio obligatorio|Explicar transformaciones y escalas temporales|Revisar alcances del modelo", "muestras o fotografías atribuidas de rocas, tarjetas de procesos y un tablero no lineal para conectar fusión, enfriamiento, meteorización, compactación y metamorfismo", "memorizar tres cajas aisladas, creer que toda roca recorre una única secuencia o confundir roca con mineral"),
    "CN07 OA 12": _entry("Clima terrestre como sistema dinámico", "Relacionar energía solar, latitud y estaciones|Modelar circulación atmosférica y oceánica|Examinar relieve, altitud y cercanía al mar|Distinguir tiempo, clima y variabilidad|Integrar factores en una explicación multicausal", "mapas de radiación, temperatura, corrientes oceánicas y relieve, más datos ficticios de dos localidades chilenas a igual latitud", "explicar clima por un solo factor, confundir tiempo atmosférico con clima o atribuir estaciones a la distancia al Sol"),
    "CN07 OA 13": _entry("Comportamiento de los gases", "Observar compresibilidad y expansión|Relacionar presión y volumen|Relacionar temperatura y volumen o presión|Representar resultados con modelo de partículas|Argumentar desde datos y condiciones seguras", "jeringas sin aguja, globos, recipientes con agua templada y fría, termómetro escolar y tablas para registrar presión cualitativa, volumen y temperatura", "afirmar que las partículas aumentan de tamaño, calentar recipientes cerrados o cambiar más de una variable sin advertirlo"),
    "CN07 OA 14": _entry("Sustancias puras, mezclas y métodos de separación", "Distinguir sustancia pura y mezcla|Comparar mezclas homogéneas y heterogéneas|Elegir propiedades útiles para separar|Planificar una separación segura|Registrar resultados y pérdidas|Aplicar criterios a una mezcla nueva", "muestras didácticas de sal, arena, agua, aceite y limaduras encapsuladas, junto con tamiz, filtro, imán protegido y diagramas de evaporación sin calentar en aula", "clasificar solo por apariencia, suponer que homogéneo significa puro o elegir un método sin relacionarlo con una propiedad"),
    "CN07 OA 15": _entry("Cambios físicos y químicos de la materia", "Observar cambios sin concluir de inmediato|Distinguir indicadores de cambio químico|Comparar cambios reversibles y formación de sustancias|Diseñar una prueba con control|Argumentar la clasificación con evidencias y límites", "secuencias de derretimiento, disolución, oxidación y reacción segura previamente registrada, con tabla de estado inicial, evidencia, producto y reversibilidad", "usar reversibilidad como criterio único, confundir cambio de estado con reacción o asegurar una sustancia nueva solo por un cambio de color"),

    # Historia, Geografía y Ciencias Sociales
    "HI07 OA 01": _entry("Hominización y poblamiento humano", "Ubicar etapas y escalas temporales|Examinar evidencia arqueológica y biológica|Relacionar adaptación, cultura y ambiente|Explicar migraciones y poblamiento sin una línea de progreso", "línea de tiempo a escala, mapas de desplazamiento y fichas de hallazgos con fecha, lugar, tipo de evidencia e incertidumbre", "representar la evolución como una escalera hacia personas actuales o convertir diferencias biológicas en jerarquías humanas"),
    "HI07 OA 02": _entry("Revolución agrícola, sedentarización y complejidad social", "Comparar caza-recolección y producción de alimentos|Relacionar domesticación y sedentarización|Examinar excedentes, intercambio y especialización|Analizar cambios sociales y desigualdad|Construir una explicación multicausal", "mapas de centros tempranos de domesticación, inventarios ficticios de aldeas y fuentes arqueológicas sobre vivienda, cultivo, almacenamiento e intercambio", "presentar la agricultura como progreso instantáneo, universal e inevitable o suponer que eliminó la movilidad"),
    "HI07 OA 03": _entry("Estados tempranos, poder y organización social", "Distinguir aldea, ciudad y Estado|Relacionar administración, tributo y obras|Examinar legitimación política y religiosa|Analizar jerarquías y formas de trabajo|Explicar poder sin reducirlo a una sola causa", "planos urbanos, registros de tributo traducidos, códigos y representaciones de autoridad de distintas civilizaciones con procedencia visible", "suponer que todos los primeros Estados fueron iguales o que religión y política pueden separarse con categorías actuales"),
    "HI07 OA 04": _entry("Primeras civilizaciones en perspectiva comparada", "Ubicar civilizaciones en tiempo y espacio|Comparar ambiente y asentamientos|Contrastar organización, tecnología e intercambio|Reconocer diferencias internas y contactos", "mapas y líneas de tiempo paralelas de Mesopotamia, Egipto, China, India, Mediterráneo oriental y América temprana, con fuentes breves", "mezclar épocas, presentar civilizaciones como bloques homogéneos o usar una única civilización como medida de las demás"),
    "HI07 OA 05": _entry("Mediterráneo antiguo como espacio de intercambio", "Caracterizar el espacio mediterráneo|Trazar rutas y productos|Relacionar navegación, ciudades y contactos|Inferir circulación de ideas y técnicas|Explicar oportunidades y límites geográficos", "mapa físico y de rutas del Mediterráneo con puertos, vientos estacionales, distancias y tarjetas de productos, alfabetos, técnicas y relatos", "describir el mar como frontera vacía, atribuir los intercambios a un solo pueblo o afirmar que la geografía determinó todas las decisiones"),
    "HI07 OA 06": _entry("Democracia ateniense, participación y exclusiones", "Ubicar instituciones y actores|Explicar participación ciudadana|Reconocer mujeres, extranjeros y personas esclavizadas excluidas|Comparar con otras formas de gobierno|Evaluar semejanzas y diferencias con el presente", "esquema de instituciones atenienses, perfiles ficticios de habitantes y fragmentos traducidos con autor y contexto", "equiparar Atenas con una democracia actual, llamar ciudadanos a todos sus habitantes o celebrar la participación sin examinar exclusiones"),
    "HI07 OA 07": _entry("Civilización romana y legado mediterráneo", "Distinguir república, expansión e imperio|Relacionar derecho y administración|Examinar ejército, caminos e infraestructura|Analizar lengua, ciudadanía y religión|Evaluar continuidad, cambio y apropiación del legado", "mapas de expansión en fechas distintas, ley traducida, plano de caminos y ciudades, inscripción y fuentes de actores con posiciones diversas", "presentar Roma como una sociedad uniforme, confundir legado con copia intacta o atribuir la expansión solo a superioridad militar"),
    "HI07 OA 08": _entry("Canon cultural de la Antigüedad clásica", "Reconocer qué se entiende por canon|Analizar filosofía, historia, arte y literatura desde fuentes|Examinar ciudadanía y centralidad humana|Identificar exclusiones y transmisiones posteriores|Debatir por qué el canon se construye y revisa|Elaborar una interpretación fundamentada", "selección atribuida de textos, obras, edificios e ideas griegas y romanas junto con una ficha sobre conservación, traducción y selección posterior", "tratar el canon como lista natural e inmutable, separar obras de su contexto o presentar Grecia y Roma como únicas fuentes culturales"),
    "HI07 OA 09": _entry("Formación de la Europa medieval", "Ubicar fragmentación del Imperio romano occidental|Examinar pueblos germánicos y reinos|Relacionar herencia grecorromana y cristianismo|Reconocer continuidades regionales|Explicar una conformación plural", "mapas de Europa entre los siglos IV y IX, cronología y fuentes breves romanas, cristianas y germánicas con contexto", "hablar de caída como desaparición total, imaginar una Europa homogénea o describir a los pueblos germánicos como un único grupo"),
    "HI07 OA 10": _entry("Sociedad medieval y orden estamental", "Comprender visión cristiana y temporalidad|Analizar estamentos y relaciones de dependencia|Examinar vida rural y urbana|Reconocer diversidad y movilidad limitada", "esquema de estamentos contrastado con fuentes sobre campesinado, nobleza, clero, mujeres, ciudades y minorías", "presentar la Edad Media como inmóvil y oscura, convertir un esquema estamental en descripción de cada persona o omitir diversidades regionales"),
    "HI07 OA 11": _entry("Europa, Bizancio e Islam medieval", "Ubicar espacios y cronologías conectadas|Comparar organización y vida urbana|Examinar intercambios científicos, comerciales y culturales|Analizar convivencia y conflicto|Contrastar perspectivas de una relación|Construir una explicación sin jerarquías civilizatorias", "mapas de rutas y ciudades, fuentes europeas, bizantinas e islámicas traducidas, y fichas de comercio, ciencia, religión y conflicto", "reducir las relaciones a guerra religiosa, tratar cada mundo como homogéneo o atribuir conocimientos a una sola dirección de influencia"),
    "HI07 OA 12": _entry("Transformaciones europeas desde el siglo XII", "Explicar crecimiento urbano|Relacionar comercio, ferias y rutas|Examinar gremios y nuevas actividades|Analizar universidades y circulación de saberes|Relacionar cambios rurales, urbanos y políticos", "plano de ciudad medieval, estatuto gremial traducido, rutas comerciales, registro de feria y cronología de universidades", "suponer que ciudad y campo evolucionaron por separado, llamar moderna a toda innovación o describir el cambio como repentino"),
    "HI07 OA 13": _entry("Civilizaciones maya y azteca", "Ubicar periodos y territorios|Examinar agricultura y adaptación ambiental|Analizar organización política y urbana|Comparar tecnologías, intercambio y conocimiento|Reconocer diversidad interna y límites de las fuentes", "mapas temporales, planos urbanos, sistemas agrícolas y fuentes arqueológicas y escritas sobre mayas y mexicas con denominaciones contextualizadas", "mezclar mayas y aztecas, congelarlos en una única época o explicar sus logros mediante categorías de superioridad"),
    "HI07 OA 14": _entry("Tawantinsuyu: organización, expansión y diversidad", "Ubicar expansión y regiones|Analizar caminos, administración y reciprocidad|Examinar estrategias de integración y dominio|Reconocer pueblos, resistencias y negociaciones|Explicar unidad y diversidad con múltiples fuentes|Revisar el concepto de imperio", "mapa del Tawantinsuyu, red vial, quipus como fuente material, crónicas contextualizadas y casos de comunidades incorporadas de maneras distintas", "presentar al Imperio inca como unidad sin tensiones, equiparar reciprocidad con ausencia de poder o tomar una crónica colonial como mirada neutral"),
    "HI07 OA 15": _entry("Culturas maya, azteca e inca", "Examinar arte, arquitectura y escritura|Comparar conocimientos matemáticos y astronómicos|Relacionar religión, política y vida cotidiana|Analizar agricultura y tecnologías|Comunicar similitudes sin borrar diferencias", "dossier atribuido de calendarios, arquitectura, códices, quipus, arte, cultivos y relatos para comparar sin mezclar tiempos ni territorios", "usar una lista de rasgos intercambiables, llamar primitivas a tecnologías distintas o reducir cultura a monumentos"),
    "HI07 OA 16": _entry("Confluencia de legados en América Latina", "Reconocer múltiples raíces culturales|Rastrear una expresión con fuentes|Examinar cambios, apropiaciones y resistencias|Relacionar patrimonio y vida presente", "casos latinoamericanos de lengua, alimentación, música, arquitectura o celebración con fuentes indígenas, africanas, europeas y contemporáneas identificadas", "buscar un origen puro, presentar mestizaje como proceso sin violencia o generalizar una expresión a toda América Latina"),
    "HI07 OA 17": _entry("Límites al poder en Atenas y Roma", "Identificar instituciones y normas|Examinar distribución y control del poder|Reconocer ciudadanía y exclusiones|Comparar mecanismos atenienses y romanos|Evaluar alcances sin proyectar instituciones actuales", "diagramas de instituciones atenienses y romanas, leyes traducidas y casos ficticios de decisiones públicas", "llamar separación de poderes a cualquier reparto institucional o suponer que las limitaciones protegían por igual a toda la población"),
    "HI07 OA 18": _entry("Conceptos políticos clásicos, medievales y actuales", "Contextualizar ciudadanía y democracia|Comparar derecho y república|Examinar municipio y gremio|Relacionar continuidades y cambios conceptuales", "tarjetas de concepto con fuentes de época y situaciones actuales sobre ciudadanía, democracia, derecho, república, municipio y gremio", "definir conceptos fuera de contexto, buscar equivalencias exactas o afirmar continuidad solo porque se conserva una palabra"),
    "HI07 OA 19": _entry("Diversidad cultural y enriquecimiento social", "Distinguir diversidad y desigualdad|Analizar aportes sin folclorizar|Examinar condiciones de inclusión|Argumentar el valor de la diversidad con casos", "casos históricos y actuales de circulación de conocimientos, lenguas, prácticas y artes con voces y autorías identificadas", "valorar la diversidad solo por beneficios instrumentales, hablar por grupos ajenos o ignorar discriminación y relaciones de poder"),
    "HI07 OA 20": _entry("Convivencia y conflicto entre culturas", "Reconocer formas de contacto|Comparar cooperación, intercambio y conflicto|Examinar poder, resistencia y negociación|Debatir principios para la convivencia actual|Fundamentar sin juzgar el pasado solo desde el presente", "pares de fuentes sobre intercambios, fronteras, alianzas y conflictos en civilizaciones estudiadas, más un caso ciudadano ficticio", "reducir contactos a armonía o guerra, atribuir una sola voz a cada cultura o usar analogías presentes sin explicar sus límites"),
    "HI07 OA 21": _entry("Adaptación humana y transformación del medio", "Observar condiciones ambientales|Relacionar recursos, tecnología y organización|Comparar respuestas de sociedades distintas|Explicar adaptación sin determinismo|Evaluar costos y límites", "mapas, reconstrucciones y datos de agricultura, agua, vivienda y movilidad en sociedades estudiadas", "afirmar que el ambiente decide la cultura, confundir adaptación con pasividad o celebrar una transformación sin examinar consecuencias"),
    "HI07 OA 22": _entry("Impactos recíprocos entre sociedad y ambiente", "Identificar una intervención humana|Rastrear efectos ambientales y sociales|Comparar escalas temporales y espaciales|Examinar respuestas y responsabilidades|Construir una explicación sistémica", "diagramas de cuenca, uso de suelo y ciudad con datos ficticios, además de dos escenarios de intervención y sus consecuencias", "atribuir un impacto a una sola causa, confundir correlación con causalidad o suponer que una medida beneficia por igual a todas las personas"),
    "HI07 OA 23": _entry("Investigación de problemáticas medioambientales", "Delimitar una pregunta investigable|Seleccionar fuentes y datos confiables|Organizar causas, actores y escalas|Comparar alternativas y sus efectos|Elaborar una propuesta fundamentada", "miniarchivo sobre agua, energía, residuos o cambio climático con mapa, serie de datos, fuente institucional, voz comunitaria ficticia y material sin autor", "investigar un tema demasiado amplio, copiar soluciones universales o presentar una propuesta sin responsables, evidencia ni posibles efectos"),

    # Inglés
    "IN07 OA 01": _entry("Listening for general and explicit meaning", "Recognize text type and purpose|Identify the main idea|Locate explicit details|Connect speakers, actions and setting|Show comprehension with evidence", "short authorized announcements, conversations, descriptions and stories with a listening grid for purpose, main idea and detail", "translate every word, answer from the image alone or treat one unknown word as failure"),
    "IN07 OA 02": _entry("Key words, chunks, connectors and sounds in listening", "Notice frequent chunks|Track sequence connectors|Recognize thematic vocabulary|Use stress and sound clues|Combine clues to reconstruct meaning", "two short recordings or teacher-read scripts containing first, next, finally, because and or, plus a visible but incomplete word bank", "collect isolated words without reconstructing meaning or judge comprehension by accent imitation"),
    "IN07 OA 03": _entry("Topic, details and relationships in oral texts", "Identify topic and situation|Locate specific people, places and actions|Recognize cause, sequence or contrast|Infer a speaker's purpose cautiously|Support an answer with two oral clues", "a two-speaker interview and a short report about a fictional school project, replayed for different listening purposes", "guess a speaker's intention without clues or confuse a remembered detail with the main idea"),
    "IN07 OA 04": _entry("Strategies for listening comprehension", "Predict from title and context|Listen once for gist|Listen again for a question|Use visual and linguistic clues|Check and revise a prediction", "an unfamiliar but accessible audio script with title, three images, planned pauses and a before-during-after listening card", "treat prediction as the answer, replay without a purpose or expect to understand every word"),
    "IN07 OA 05": _entry("Clear multimodal oral presentation", "Define purpose and audience|Organize an opening, ideas and close|Use images that add meaning|Speak from key words rather than read|Rehearse and improve clarity", "fictional topic cards, a three-slide paper storyboard, timing cards and a short checklist for message, evidence, voice and visual support", "read every word from a slide, add decorative images or equate fluency with speed"),
    "IN07 OA 06": _entry("Strategies for interaction and oral fluency", "Prepare useful chunks|Open and sustain a turn|Ask for clarification|Paraphrase or use gesture|Respond and repair meaning", "information-gap cards, clarification stems and fictional profiles that require genuine questions and answers without personal data", "recite a dialogue without listening, penalize pauses or use gesture without attempting shared meaning"),
    "IN07 OA 07": _entry("Personal response to read or heard texts", "Select a meaningful idea|Express a preference or reaction|Connect safely to another text or fictional case|Discuss different responses|Support a reaction with evidence", "a short story or interview with choice cards for oral, visual, dramatic or written response and sentence stems that can be faded", "say I like it without textual support or require students to disclose private experiences"),
    "IN07 OA 08": _entry("Language functions in speaking", "Exchange information and quantities|Describe people, places and actions|Express obligation, possibility and preference|Narrate past events and future plans|Combine functions in a real interaction", "picture scenes, schedules, quantities and fictional event cards with a functional language bank rather than a full script", "complete grammar drills without a communicative purpose or demand perfect forms before allowing interaction"),
    "IN07 OA 09": _entry("Reading for general and explicit meaning", "Recognize format and purpose|Identify the main idea|Locate explicit information|Connect text and visual elements|Answer with a cited clue", "short authorized webpages, messages, articles and infographics printed without accounts, tracking or personal data", "read aloud accurately without constructing meaning or copy a sentence without linking it to the question"),
    "IN07 OA 10": _entry("Understanding non-literary English texts", "Read descriptions and instructions|Interpret procedures and notices|Examine advertising purpose|Compare information across formats|Use text features to solve a task", "a fictional event notice, a safe procedure, a product-free advertisement and a brief article sharing one topic", "treat every non-literary text as neutral information or ignore headings, diagrams and audience"),
    "IN07 OA 11": _entry("Understanding literary English texts", "Follow setting, characters and events|Recognize conflict and response|Notice sound, image or humour|Infer a theme cautiously|Compare two literary forms", "an original short story, comic strip and four-line poem with a common motif and a glossary limited to essential words", "summarize events without interpreting, confuse narrator and author or force one correct theme"),
    "IN07 OA 12": _entry("Strategies for reading comprehension", "Set a reading purpose|Preview and predict|Reread for a precise question|Infer vocabulary from context|Summarize and check understanding", "one accessible text annotated only with title, image and paragraph numbers, plus strategy cards for before, during and after reading", "use every strategy as a checklist, look up every word or keep a prediction after the text contradicts it"),
    "IN07 OA 13": _entry("Multimodal stories and information writing", "Choose purpose, genre and audience|Plan ideas with a visual organizer|Draft a complete message|Integrate an image or layout meaningfully|Revise for clarity and effect", "original prompts for a fictional experience, cultural profile or environmental action, with storyboard and source-attribution boxes", "decorate before developing meaning, copy a model or use personal images and data unnecessarily"),
    "IN07 OA 14": _entry("Short functional and creative texts in English", "Recognize conventions of each genre|Adapt a model without copying|Develop a coherent short text|Use connectors and reference words|Edit for a real reader", "models of an email, brochure, rhyme, description and short story on one fictional topic, with differences in audience and layout marked", "use the same register and structure for every genre or replace all voice with a rigid template"),
    "IN07 OA 15": _entry("Writing to inform, express opinions and narrate", "State a clear purpose|Select relevant information or reasons|Order events and ideas|Connect sentences coherently|Revise content before accuracy", "three fictional situations requiring an information note, an opinion paragraph and a brief narrative, with a shared planning grid", "list disconnected sentences, repeat an opinion without reasons or correct grammar before the message is complete"),
    "IN07 OA 16": _entry("Language functions in written English", "Express quantity and comparison|Describe ongoing and habitual actions|Narrate past events|Express plans, obligation and possibility|Combine functions in a purposeful text", "fictional profiles, timetables, before-now-next image sequences and a language bank grouped by communicative function", "select a tense by isolated time words, fill blanks without meaning or avoid writing until every form is certain"),

    # Educación Física y Salud
    "EF07 OA 01": _entry("Habilidades motrices específicas en actividades deportivas", "Ajustar locomoción, manipulación y estabilidad|Combinar habilidades bajo presión gradual|Elegir variantes para deportes individuales|Aplicar combinaciones en colaboración y oposición|Evaluar control y seguridad", "estaciones sin eliminación con balones blandos, implementos graduados, zonas amplias y variantes equivalentes para atletismo, gimnasia, danza y juegos deportivos", "priorizar velocidad o resultado, comparar cuerpos o exigir una única ejecución técnica"),
    "EF07 OA 02": _entry("Estrategias y tácticas para resolver problemas de juego", "Leer espacio, reglas y compañeros|Crear líneas de pase o apoyo|Ajustar defensa y recuperación|Tomar decisiones con oposición regulada|Revisar una táctica desde evidencia", "juegos reducidos de tres contra tres, tableros magnéticos y pausas de observación con roles rotativos y reglas de contacto explícitas", "confundir táctica con jugada memorizada, excluir a quien se equivoca o atribuir el resultado a una sola persona"),
    "EF07 OA 03": _entry("Condición física y metas personales seguras", "Reconocer componentes de condición física|Regular intensidad y recuperación|Aplicar fuerza y movilidad con técnica|Registrar progreso respecto de sí mismo|Ajustar una meta alcanzable", "circuito de resistencia, fuerza, velocidad y flexibilidad con escala de esfuerzo percibido, pausas y alternativas sin datos corporales públicos", "usar dolor o agotamiento como logro, comparar marcas entre estudiantes o prescribir metas sin considerar señales y condiciones individuales"),
    "EF07 OA 04": _entry("Actividad física en distintos entornos", "Leer riesgos y oportunidades del entorno|Preparar equipo, normas y mínimo impacto|Practicar con una variante accesible|Responder a cambios de superficie o clima|Evaluar seguridad y cuidado ambiental", "planos y casos ficticios de gimnasio, patio, plaza, sendero y borde costero antes de cualquier salida autorizada, con lista de seguridad y cuidado", "suponer que todo espacio es apto, improvisar ante alertas o presentar aventura como exposición innecesaria al riesgo"),
    "EF07 OA 05": _entry("Participación autónoma en actividad física comunitaria", "Explorar opciones de interés|Reconocer barreras y apoyos|Elegir una participación realista|Planificar frecuencia y seguridad|Evaluar disfrute, continuidad y ajustes", "cartelera ficticia de actividades escolares y comunitarias gratuitas o de bajo recurso, con horarios, accesibilidad, reglas y alternativas domésticas seguras", "responsabilizar al estudiante por barreras de tiempo, dinero o traslado, o convertir una preferencia en obligación uniforme"),

    # Artes Visuales
    "AR07 OA 01": _entry("Creación visual desde percepciones, ideas y contexto", "Observar manifestaciones y registrar preguntas|Relacionar percepción, emoción e idea sin fórmula|Experimentar una traducción visual|Crear una propuesta propia|Explicar decisiones y revisar", "referentes atribuidos de arte, diseño y entorno de Chile, Latinoamérica y otros contextos, junto con bitácora de detalles, preguntas y asociaciones", "copiar la apariencia del referente, atribuir una cultura completa a una imagen o exigir autobiografía para crear"),
    "AR07 OA 02": _entry("Experimentación visual con materiales sustentables", "Definir intención y criterios de sustentabilidad|Explorar dibujo, pintura y volumen|Transformar materiales limpios y seguros|Resolver uniones, soporte y acabado|Crear y revisar sin perder autoría", "muestrario de cartón, papel, fibras, envases limpios, pigmentos escolares y sistemas de unión reversibles con ficha de origen y descarte", "llamar sustentable a cualquier material reciclado, acumular materiales sin intención o usar residuos inseguros"),
    "AR07 OA 03": _entry("Expresión visual con medios digitales contemporáneos", "Analizar encuadre, secuencia y audiencia|Explorar fotografía o imagen digital|Construir una narración visual|Editar respetando autoría y privacidad|Publicar o presentar en circuito protegido", "dispositivo sin cuentas o simulación en papel, banco de imágenes propias o autorizadas, storyboard y pauta de consentimiento, crédito y privacidad", "usar efectos como sustituto de una idea, publicar datos o rostros sin permiso o tomar imágenes de internet sin revisar derechos"),
    "AR07 OA 04": _entry("Interpretación de manifestaciones visuales patrimoniales y contemporáneas", "Describir antes de interpretar|Examinar material, medio y lenguaje visual|Situar autoría, propósito y contexto|Comparar interpretaciones con evidencia|Reconocer límites y preguntas abiertas", "dossier atribuido de obra patrimonial, diseño, artesanía y producción contemporánea con ficha de autoría, pueblo o comunidad, fecha, lugar y medio", "adivinar intenciones, convertir gusto en argumento o tratar patrimonio vivo como objeto anónimo disponible"),
    "AR07 OA 05": _entry("Propósito expresivo y lenguaje visual", "Reconocer propósito declarado por quien crea|Relacionar color, forma, composición y material|Comparar decisiones entre trabajos|Ofrecer retroalimentación según criterios|Revisar conservando la voz propia", "trabajos ficticios y producciones en proceso acompañados de declaración breve de intención y tarjetas de color, forma, textura, composición y material", "evaluar por parecido o talento, imponer la solución del observador o afirmar que un elemento visual tiene siempre el mismo efecto"),
    "AR07 OA 06": _entry("Espacios y formas de difusión de las artes visuales", "Caracterizar museo, galería, espacio público y plataforma digital|Relacionar espacio, montaje y audiencia|Examinar mediación, acceso y cuidado|Diseñar una difusión pertinente para un trabajo", "planos, recorridos y registros autorizados de museo, galería, centro cultural, espacio público y exposición digital sin datos de visitantes", "creer que difundir es solo decorar una sala, que todos los públicos acceden del mismo modo o que publicar en línea no requiere cuidado"),
}


PRIOR = {
    "CN": "formular preguntas, modelar sistemas y explicar fenómenos con evidencia trabajados en 6° básico",
    "HI": "interpretar mapas, cronologías y fuentes desde múltiples perspectivas trabajadas en 6° básico",
    "IN": "understand and produce short oral and written messages with purposeful support",
    "EF": "combinar habilidades motrices, regular esfuerzo y participar con seguridad en 6° básico",
    "AR": "crear, interpretar y revisar producciones visuales con decisiones propias en 6° básico",
}

VOCABULARY = {
    "CN": "pregunta, variable, observación, medición, evidencia, patrón, sistema, modelo, conclusión, limitación",
    "HI": "fuente, procedencia, temporalidad, territorio, actor, causa, consecuencia, continuidad, cambio, perspectiva",
    "IN": "purpose, audience, gist, detail, clue, chunk, interaction, function, evidence, revision",
    "EF": "habilidad motriz, estrategia, táctica, intensidad, regulación, seguridad, cooperación, evidencia, autocuidado",
    "AR": "intención, referente, lenguaje visual, materialidad, procedimiento, contexto, autoría, montaje, criterio, revisión",
}

FINISHERS = {
    "CN": ("Contrastar la explicación con los datos", "Comunicar resultados y límites", "Aplicar lo aprendido a una decisión segura"),
    "HI": ("Contrastar perspectivas y límites de las fuentes", "Argumentar con evidencia contextualizada", "Comunicar una explicación histórica o geográfica"),
    "IN": ("Communicate meaning independently", "Check evidence and revise", "Transfer meaning to a new audience or format"),
    "EF": ("Resolver una situación nueva con seguridad", "Regular el desempeño desde evidencia propia", "Transferir la decisión a otro juego o entorno"),
    "AR": ("Crear una respuesta visual propia", "Interpretar decisiones con evidencia visual", "Revisar sin perder autoría"),
}


def _dose_count(text: str, slug: str, readings: list) -> int:
    lowered = text.lower()
    count = 4
    if len(text) > 260 or lowered.count(";") >= 2:
        count += 1
    if any(verb in lowered for verb in ("investigar", "crear", "producir", "diseñar", "evaluar", "analizar", "argumentar", "interpretar")):
        count += 1
    if readings or ("leng" in slug and any(verb in lowered for verb in ("leer", "escribir", "obra", "texto"))):
        count += 1
    return min(count, 7)


RECORDS = {}
for record in SNAPSHOT["records"]:
    if record["course_order"] != 7 or record["subject_slug"] not in TARGET_SLUGS:
        continue
    for objective in record["objectives"]:
        if objective["code"].startswith("de "):
            continue
        RECORDS[objective["code"]] = {
            "slug": record["subject_slug"],
            "description": objective["description"],
            "url": objective["url"],
            "count": _dose_count(objective["description"], record["subject_slug"], objective.get("readings", [])),
        }

missing_profiles = sorted(set(RECORDS) - set(CONTENT))
extra_profiles = sorted(set(CONTENT) - set(RECORDS))
if missing_profiles or extra_profiles:
    raise RuntimeError(f"Perfiles de 7° desalineados: faltan={missing_profiles}; sobran={extra_profiles}")


def _profile(code: str) -> dict:
    prefix = code[:2]
    content = CONTENT[code]
    needed = RECORDS[code]["count"]
    focuses = list(content["facets"])
    for closer in FINISHERS[prefix]:
        if len(focuses) >= needed:
            break
        focuses.append(f"{closer}: {content['topic'].lower()}")
    if len(focuses) < needed:
        raise ValueError(f"{code}: faltan focos para {needed} clases")
    return {
        "topic": content["topic"],
        "prior": PRIOR[prefix],
        "vocabulary": VOCABULARY[prefix],
        "anchor": content["anchor"],
        "misconception": content["misconception"],
        "focuses": focuses[:needed],
    }


def _retarget_links(lesson: dict, prefix: str) -> None:
    replacements = {
        "CN": ("CN03", "CN07"),
        "HI": ("HI03", "HI07"),
        "IN": ("EN03", "IN07"),
        "EF": ("EF03", "EF07"),
        "AR": ("AR03", "AR07"),
    }
    old, new = replacements[prefix]
    for link in lesson.get("transversal", []):
        link["code"] = link["code"].replace(old, new)


def _natural_voice(lesson: dict, profile: dict, index: int, prefix: str) -> None:
    focus = profile["focuses"][index]
    action = focus[0].lower() + focus[1:]
    anchor = profile["anchor"]
    misconception = profile["misconception"]
    if prefix == "CN":
        openings = (
            f"Presenta {anchor}. Antes de explicar, cada estudiante separa en su cuaderno qué observa, qué infiere y qué pregunta queda abierta.",
            f"Plantea dos explicaciones posibles para un caso construido con {anchor}. El curso decide qué dato necesitaría para distinguirlas.",
            f"Muestra una representación incompleta de {anchor}. En parejas identifican qué ayuda a pensar y qué parte del fenómeno todavía no aparece.",
            f"Recupera {anchor} con una condición modificada. Cada estudiante predice el efecto y anota qué debería mantenerse constante para comprobarlo.",
            f"Comparte un resultado inesperado obtenido con {anchor}. El curso propone primero revisiones del procedimiento y después posibles explicaciones.",
            f"Abre con una decisión cotidiana o pública relacionada con {anchor}. Distinguen qué información científica sirve y qué afirmaciones aún requieren evidencia.",
        )
        models = (
            f"Modela cómo {action}: nombra la pregunta, hace visible la evidencia y construye una explicación prudente que no afirma más de lo observado.",
            f"Compara dos modelos o registros. Explica qué relación representa cada uno, dónde coinciden y qué limitación debe declararse.",
            f"Examina la idea frecuente «{misconception}». Localiza por qué parece razonable y usa evidencia para reconstruirla sin ridiculizar el error.",
            f"Hace una demostración o análisis seguro en voz alta: controla condiciones, registra el resultado y separa dato, patrón y conclusión.",
            f"Parte de una conclusión apresurada y la mejora agregando evidencia, una comparación válida y un límite explícito.",
            f"Construye una explicación breve para una audiencia no especialista y revisa cada palabra que podría convertir una posibilidad en certeza.",
        )
        lesson["purpose"] = f"Acompañar al curso a {action} mediante observación, modelos y evidencia examinada con cuidado."
        lesson["goal"] = f"Hoy voy a {action}; distinguiré evidencia, explicación y límites."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Equipos trabajan con {anchor} y una pregunta común. Distribuyen roles, registran datos o rasgos por separado, comparan resultados y mejoran una explicación después de recibir retroalimentación sobre un criterio."
        lesson["independent"] = f"Cada estudiante analiza un caso nuevo para {action}. Debe usar una tabla, diagrama o modelo pertinente, citar la evidencia decisiva y declarar una limitación."
        lesson["ticket"] = "Escribe una conclusión en dos oraciones: una con la evidencia que la sostiene y otra con el límite que impide exagerarla."
    elif prefix == "HI":
        openings = (
            f"Dispón {anchor} con autoría, fecha y lugar visibles. Cada estudiante elige una pieza, describe qué muestra y formula una pregunta que la fuente por sí sola no resuelve.",
            f"Presenta dos fuentes de {anchor} que no miran el asunto del mismo modo. El curso registra acuerdos, tensiones y datos de contexto antes de opinar.",
            f"Construye en el pizarrón una línea de tiempo o mapa incompleto a partir de {anchor}. El curso decide dónde ubicar cada evidencia y justifica la escala.",
            f"Comparte una afirmación histórica plausible sobre {anchor}. Los estudiantes buscan qué evidencia la apoya, qué la matiza y qué faltaría consultar.",
            f"Cambia la escala temporal, territorial o social de {anchor}. Antes de analizar, el curso anticipa qué actores o relaciones podrían volverse visibles.",
            f"Abre con una decisión ciudadana ficticia vinculada con {anchor}. Distinguen semejanzas útiles y diferencias que impiden trasladar el pasado de manera directa.",
        )
        models = (
            f"Modela cómo {action}: contextualiza la fuente, distingue descripción e interpretación y formula una conclusión proporcional a la evidencia.",
            f"Cruza un mapa, una cronología y una fuente breve. Explica qué aporta cada representación y evita convertir coincidencia en causalidad automática.",
            f"Examina la afirmación «{misconception}». Muestra el anacronismo, generalización o jerarquía que contiene y la reemplaza por una explicación contextualizada.",
            f"Compara dos perspectivas sin buscar una voz neutral inexistente. Identifica posición, propósito, coincidencias, silencios y límites.",
            f"Construye una relación de causa y consecuencia que incluye actores, condiciones y resultados no previstos, evitando una explicación monocausal.",
            f"Redacta un argumento breve, incorpora una evidencia precisa y agrega una frase que reconozca lo que todavía no puede concluirse.",
        )
        lesson["purpose"] = f"Guiar al curso para {action} mediante fuentes contextualizadas, relaciones temporales y perspectivas contrastadas."
        lesson["goal"] = f"Hoy voy a {action}; sostendré mi explicación con fuentes y reconoceré sus límites."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"En parejas, analizan dos piezas de {anchor}. Completan una matriz de contexto, evidencia, perspectiva y límite; después contrastan una conclusión y la corrigen si generaliza más de lo permitido."
        lesson["independent"] = f"Cada estudiante responde un problema nuevo que exige {action}. Integra al menos una fuente o representación espacial o temporal y explica por qué resulta pertinente."
        lesson["ticket"] = "Formula una conclusión, cita la evidencia más fuerte y escribe una pregunta que exigiría otra fuente o escala."
    elif prefix == "IN":
        openings = (
            f"Present {anchor} once without translating it in full. Students first respond with a choice, gesture, note or short chunk and then point to the clue they used.",
            f"Show the title, format or first image from {anchor}. Students make a tentative prediction and choose what they will listen or read for.",
            f"Offer two possible meanings for {anchor}. Students decide which one fits better and identify the word, sound, image or text feature that supports it.",
            f"Begin with a short information gap built from {anchor}. Students need one another's message to complete a practical task.",
            f"Change the speaker, audience or purpose in {anchor}. Students predict which language and delivery choices should change.",
        )
        models = (
            f"Think aloud in clear, accessible English and show how to {action}. Point to the exact clue, combine it with context and check the meaning instead of translating every word.",
            f"Compare two comprehensible responses. Explain why both may communicate, then revise the one that does not yet fit the purpose or audience.",
            f"Model a first attempt that shows this problem: {misconception}. Pause, ask for clarification or reread, and repair the message without hiding the mistake.",
            f"Build a response from useful chunks rather than a full script. Make one meaningful choice, test it with a partner and revise for clarity.",
            f"Use {anchor} to model planning, communicating and checking. Highlight meaning, not speed, accent imitation or immediate accuracy.",
        )
        lesson["purpose"] = f"Help students {action} through meaningful, accessible English and evidence from the message."
        lesson["goal"] = f"Today I will {action}; I will show the clue or language choice that helped me communicate."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"Pairs work with a second version of {anchor}. Each student contributes information, asks for clarification and improves one part of the message after focused feedback."
        lesson["independent"] = f"Each student completes a new task to {action}. They may use a word bank or planning card, but must select language, communicate meaning and check the result independently."
        lesson["ticket"] = "Give one short response for today's purpose and underline, point to or name the clue or language choice that supports it."
    elif prefix == "EF":
        openings = (
            f"Presenta {anchor} a velocidad de observación. El grupo identifica meta, espacio, señal de detención y una condición que vuelve segura la participación.",
            f"Propón dos soluciones motrices posibles con {anchor}. Antes de probarlas, cada estudiante anticipa cuál serviría mejor y según qué señal observable.",
            f"Organiza una exploración breve de {anchor} sin puntaje ni eliminación. Al detenerse, el curso nombra qué decisiones dieron control y cuáles necesitan ajuste.",
            f"Cambia una regla, distancia o implemento de {anchor}. Cada estudiante elige una variante accesible y predice cómo tendrá que adaptar su movimiento.",
            f"Presenta un caso ficticio de seguridad o participación relacionado con {anchor}. El curso propone una respuesta que cuide aprendizaje, integridad e inclusión.",
        )
        models = (
            f"Ejecuta lentamente cómo {action}. Nombra mirada, apoyos, trayectoria, fuerza y regulación; muestra una alternativa equivalente sin presentar un cuerpo ideal.",
            f"Compara dos decisiones motrices y hace visible el criterio: control, oportunidad, cooperación o seguridad. El resultado del juego no decide por sí solo cuál fue mejor.",
            f"Modela un intento que cae en «{misconception}». Detiene la acción, modifica una variable y vuelve a probar sin exponer ni etiquetar a nadie.",
            f"Piensa en voz alta antes, durante y después de la ejecución: anticipa, observa una señal corporal o espacial y ajusta el siguiente intento.",
            f"Muestra cómo dar retroalimentación sobre una conducta observable y cómo la persona decide qué ajuste incorporar.",
        )
        lesson["purpose"] = f"Crear una experiencia segura e inclusiva para {action}, con decisiones motrices observables y ajustables."
        lesson["goal"] = f"Hoy voy a {action}; elegiré una variante segura y explicaré el ajuste que realicé."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"En estaciones, practican con {anchor}, roles rotativos y variantes equivalentes. Reciben retroalimentación sobre un criterio y realizan un segundo intento sin comparaciones corporales."
        lesson["independent"] = f"Cada estudiante resuelve una variante nueva para {action}. Elige nivel, distancia, ritmo, implemento o rol, actúa con seguridad y ajusta desde evidencia propia."
        lesson["ticket"] = "Demuestra, dibuja o explica la decisión que tomaste y la señal corporal, espacial o reglamentaria que te ayudó a ajustarla."
    else:
        openings = (
            f"Presenta {anchor} sin convertirlo en modelo para copiar. Cada estudiante registra dos detalles, una pregunta y una posibilidad expresiva propia.",
            f"Dispón dos referentes de {anchor} con autoría y contexto. El curso describe primero y después compara cómo una decisión visual cambia el efecto.",
            f"Abre una estación breve de pruebas con {anchor}. Cada estudiante modifica una sola variable y conserva tanto el intento útil como el que no resultó.",
            f"Comparte una obra ficticia en proceso construida con {anchor}. El curso formula comentarios desde criterios acordados, nunca desde talento, gusto o parecido.",
            f"Cambia la audiencia, escala o espacio de presentación de {anchor}. Antes de crear, cada estudiante anticipa qué decisión visual tendría que revisar.",
        )
        models = (
            f"Realiza una prueba parcial para {action}. Explica cómo color, forma, textura, material, composición o encuadre cambia el efecto y deja visible una duda de proceso.",
            f"Compara dos caminos visuales posibles. Relaciona cada uno con la intención y muestra que una decisión fundamentada no elimina la diversidad de respuestas.",
            f"Examina la idea «{misconception}». Modifica una decisión concreta y explica cómo la revisión protege autoría, contexto o seguridad.",
            f"Construye una respuesta sin terminarla por el curso: demuestra solo el procedimiento necesario y devuelve las decisiones expresivas a cada estudiante.",
            f"Modela una conversación de apreciación: describe, interpreta con evidencia visual, pregunta y reconoce que otra lectura puede ser plausible.",
        )
        lesson["purpose"] = f"Abrir un proceso de creación o apreciación para {action}, cuidando intención, contexto y autoría."
        lesson["goal"] = f"Hoy voy a {action}; tomaré una decisión visual propia y explicaré su efecto."
        lesson["opening"] = openings[index % len(openings)]
        lesson["model"] = models[index % len(models)]
        lesson["guided"] = f"En estaciones o parejas, exploran una variable de {anchor}. Describen efectos, reciben retroalimentación sobre un criterio y cada autor decide qué incorporar."
        lesson["independent"] = f"Cada estudiante crea o interpreta una respuesta nueva para {action}. Documenta una elección, una revisión y la evidencia visual que sostiene su explicación."
        lesson["ticket"] = "Muestra una decisión visual de hoy y explica qué detalle, prueba o criterio te llevó a conservarla o cambiarla."

    visible_goal = lesson["goal"].removeprefix("Hoy ").removeprefix("Today ").rstrip(".")
    for link in lesson.get("transversal", []):
        application = link.get("application", "")
        if "meta «" in application:
            link["application"] = application.split("meta «", 1)[0] + f"meta «{visible_goal}»."
        elif "durante «" in application:
            link["application"] = application.split("durante «", 1)[0] + f"durante «{visible_goal}» mediante una acción observable y revisable."


def build_sequence(code: str) -> dict | None:
    if code not in RECORDS:
        return None
    prefix = code[:2]
    profile = _profile(code)
    lessons = []
    for index in range(len(profile["focuses"])):
        if prefix in {"CN", "HI"}:
            lesson = inquiry_lesson(code, index, profile, "science" if prefix == "CN" else "history")
        else:
            maker_code = code.replace("IN07", "EN07", 1) if prefix == "IN" else code
            lesson = applied_lesson(maker_code, index, profile)
        _retarget_links(lesson, prefix)
        _natural_voice(lesson, profile, index, prefix)
        lessons.append(lesson)
    record = RECORDS[code]
    return {
        "topic": profile["topic"],
        "pedagogical_explanation": (
            f"{profile['topic']} parte de {profile['prior']} y avanza mediante decisiones propias de la disciplina. "
            f"La secuencia cambia fuentes, representaciones y evidencias, y enfrenta la confusión «{profile['misconception']}»."
        ),
        "prerequisites": profile["prior"],
        "vocabulary": profile["vocabulary"],
        "official_alignment": {
            "units": [f"Eje oficial · progresión interna en {len(lessons)} clases"],
            "unit_origin": "Organización pedagógica interna derivada del eje y del OA; no se presenta como una unidad oficial del programa.",
            "indicators": [f"{focus}." for focus in profile["focuses"][:3]],
            "indicator_origin": "Criterios internos derivados del verbo, contenido y alcance del OA oficial.",
            "source": record["url"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    prepared = dict(item)
    if item["subject_slug"] == "ingles":
        prepared["subject_slug"] = "ingles-propuesta"
    result = base_integration(prepared)
    result["generated_for"] = "7-basico-next-five"
    return result


SEQUENCES = {code: True for code in RECORDS}
