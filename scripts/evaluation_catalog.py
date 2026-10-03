"""Catálogo pedagógico visible de evaluaciones y muestras breves originales.

Los datos de este módulo alimentan HTML y Markdown. No contienen ítems oficiales ni
tablas de conversión inventadas: las muestras calculan únicamente puntos del
proyecto y siempre conservan el regreso a OA y clases existentes.
"""

from __future__ import annotations


INSTRUMENTS = {
    "paes": {
        "name": "Prueba de Acceso a la Educación Superior",
        "short_name": "PAES",
        "category": "Acceso a la educación superior",
        "population": "Egresados de enseñanza media y estudiantes de 4° medio en la aplicación regular.",
        "purpose": "Observar competencias necesarias para postular al sistema de acceso centralizado; no reemplaza el currículo escolar.",
        "status": "Modelado con correspondencias, tareas y muestras breves originales; cobertura completa pendiente",
        "framework_id": "paes-2027",
        "source_url": "https://portaldemre.demre.cl/paes/factores-seleccion/pruebas-acceso-paes",
        "documents": [
            ("Pruebas PAES obligatorias, electivas y M2", "https://portaldemre.demre.cl/paes/factores-seleccion/pruebas-acceso-paes"),
            ("Temarios PAES de Invierno · Admisión 2027", "https://demre.cl/la-prueba/pruebas-y-temarios/presentacion-pruebas-temarios-paes-invierno"),
            ("Preguntas frecuentes PAES de Invierno 2026", "https://portaldemre.demre.cl/mesa-de-ayuda/preguntas-frecuentes-paes-invierno"),
        ],
    },
    "simce": {
        "name": "Sistema de Medición de la Calidad de la Educación",
        "short_name": "SIMCE",
        "category": "Evaluación nacional del sistema escolar",
        "population": "Niveles y áreas definidos por el plan vigente; en 2026, 4° y 6° básico y II medio en Lectura y Matemática.",
        "purpose": "Conocer resultados educativos de establecimientos respecto del Currículum Nacional y sus contextos.",
        "status": "Modelado con correspondencias, tareas y muestras breves originales; cobertura completa pendiente",
        "framework_id": "simce-2026",
        "source_url": "https://www.agenciaeducacion.cl/evaluar/simce/",
        "documents": [
            ("SIMCE · información y calendario 2026", "https://www.agenciaeducacion.cl/evaluar/simce/"),
            ("Plan de evaluaciones nacionales e internacionales", "https://www.agenciaeducacion.cl/evaluar/simce/#plan-de-evaluaciones-2021-2026"),
            ("Ejemplos de preguntas publicados por la Agencia", "https://www.agenciaeducacion.cl/evaluar/simce/#ejemplos-de-preguntas-simce"),
        ],
    },
    "dia": {
        "name": "Diagnóstico Integral de Aprendizajes",
        "short_name": "DIA",
        "category": "Herramienta nacional voluntaria de uso interno",
        "population": "Establecimientos de enseñanza básica y media; áreas académica y socioemocional según instrumentos disponibles.",
        "purpose": "Apoyar decisiones internas en diagnóstico, monitoreo intermedio y cierre; sus resultados no son calificaciones.",
        "status": "Explicado y conectado como referencia; sin copiar instrumentos oficiales",
        "framework_id": None,
        "source_url": "https://diagnosticointegral.agenciaeducacion.cl/",
        "documents": [
            ("Plataforma e información vigente DIA", "https://diagnosticointegral.agenciaeducacion.cl/"),
            ("Explicación institucional del DIA", "https://www.agenciaeducacion.cl/evaluar/diagnostico-integral-de-aprendizajes/"),
        ],
    },
    "pisa": {
        "name": "Programme for International Student Assessment",
        "short_name": "PISA",
        "category": "Estudio internacional",
        "population": "Estudiantes de 15 años de países y economías participantes.",
        "purpose": "Observar cómo se aplican conocimientos y habilidades ante problemas y contextos nuevos.",
        "status": "Modelado con correspondencias, tareas y muestras breves originales; cobertura completa pendiente",
        "framework_id": "pisa-2025",
        "source_url": "https://www.oecd.org/en/publications/pisa-2025-assessment-and-analytical-framework_86c36975-en.html",
        "documents": [
            ("Marco de evaluación y análisis PISA 2025", "https://www.oecd.org/en/publications/pisa-2025-assessment-and-analytical-framework_86c36975-en.html"),
            ("PISA en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/pisa/"),
        ],
    },
    "timss": {
        "name": "Trends in International Mathematics and Science Study",
        "short_name": "TIMSS",
        "category": "Estudio internacional",
        "population": "Estudiantes de 4° y 8° grado en Matemática y Ciencias.",
        "purpose": "Comparar desempeños en dominios de contenido y procesos de conocer, aplicar y razonar.",
        "status": "Modelado con correspondencias, tareas y muestras breves originales; cobertura completa pendiente",
        "framework_id": "timss-2027",
        "source_url": "https://timss2027.org/frameworks/",
        "documents": [
            ("Marcos TIMSS 2027", "https://timss2027.org/frameworks/"),
            ("TIMSS en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/timss/"),
        ],
    },
    "pirls": {
        "name": "Progress in International Reading Literacy Study",
        "short_name": "PIRLS",
        "category": "Estudio internacional de lectura",
        "population": "Estudiantes alrededor de 4° básico.",
        "purpose": "Observar comprensión de textos literarios e informativos y factores de contexto.",
        "status": "Modelado con correspondencias, tareas y muestras breves originales; cobertura completa pendiente",
        "framework_id": "pirls-2026",
        "source_url": "https://www.iea.nl/publications/assessment-framework/pirls-2026-assessment-frameworks",
        "documents": [
            ("Marcos PIRLS 2026", "https://www.iea.nl/publications/assessment-framework/pirls-2026-assessment-frameworks"),
            ("PIRLS en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/pirls/"),
        ],
    },
    "erce": {
        "name": "Estudio Regional Comparativo y Explicativo",
        "short_name": "ERCE",
        "category": "Estudio regional latinoamericano",
        "population": "Estudiantes de 3° y 6° básico; Lectura, Escritura y Matemática, además de Ciencias en 6°.",
        "purpose": "Comparar logros y factores asociados en América Latina y el Caribe.",
        "status": "Explicado, conectado a OA de referencia y acompañado por muestras breves; cobertura y mapeo aún parciales",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/erce/",
        "documents": [("ERCE en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/erce/")],
    },
    "icils": {
        "name": "International Computer and Information Literacy Study",
        "short_name": "ICILS",
        "category": "Estudio internacional de alfabetización digital",
        "population": "Muestra representativa de estudiantes de 8° básico.",
        "purpose": "Observar búsqueda, evaluación, transformación, creación y comunicación de información con computadores.",
        "status": "Explicado, conectado a OA de referencia y acompañado por una muestra breve; cobertura y mapeo aún parciales",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/icils/",
        "documents": [("ICILS en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/icils/")],
    },
    "iccs": {
        "name": "International Civic and Citizenship Education Study",
        "short_name": "ICCS",
        "category": "Estudio internacional de educación cívica",
        "population": "Estudiantes de 8° básico.",
        "purpose": "Observar preparación para la ciudadanía, conocimientos, razonamiento, actitudes y participación.",
        "status": "Explicado, conectado a OA de referencia y acompañado por una muestra breve; cobertura y mapeo aún parciales",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/iccs/",
        "documents": [("ICCS en Chile · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/iccs/")],
    },
    "eces": {
        "name": "Early Childhood Education Study",
        "short_name": "ECES",
        "category": "Estudio internacional de educación parvularia",
        "population": "Primera infancia y educación parvularia, fuera del tramo 1° básico–4° medio de este repositorio.",
        "purpose": "Estudiar contextos y experiencias de educación inicial; no se fuerza una equivalencia con OA escolares.",
        "status": "Identificado en el panorama oficial; fuera del alcance curricular actual",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/",
        "documents": [("Panorama de estudios internacionales de Chile", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/")],
    },
    "impulso-lector": {
        "name": "Evaluación Impulso Lector",
        "short_name": "Impulso Lector",
        "category": "Evaluación nacional censal de lectura inicial",
        "population": "Estudiantes de 2° básico; aplicación anunciada para noviembre y diciembre de 2026.",
        "purpose": "Observar tempranamente precursores de la lectura, comprensión y fluidez para orientar apoyos del sistema y los establecimientos.",
        "status": "Explicado y conectado con tres componentes y ejemplos originales; primera aplicación pendiente al corte documental",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/agencia-informa-el-calendario-de-evaluaciones-nacionales-2026/",
        "documents": [
            ("Calendario oficial 2026 e incorporación de Impulso Lector", "https://www.agenciaeducacion.cl/agencia-informa-el-calendario-de-evaluaciones-nacionales-2026/"),
            ("Presentación institucional de Impulso Lector", "https://www.agenciaeducacion.cl/agencia-de-la-calidad-de-la-educacion-presento-impulso-lector-la-primera-evaluacion-censal-de-habilidades-lectoras-en-2-basico/"),
            ("Cuadernillos prototipo publicados por la Agencia", "https://www.agenciaeducacion.cl/agencia-presenta-los-cuadernillos-de-la-prueba-impulso-lector-para-estudiantes-de-2-basico/"),
        ],
    },
    "estudios-nacionales": {
        "name": "Estudios Nacionales de aprendizaje",
        "short_name": "Estudios nacionales",
        "category": "Evaluaciones nacionales muestrales",
        "population": "Muestras representativas definidas para áreas y niveles específicos, entre ellos lectura inicial, escritura, formación ciudadana, inglés y educación técnico-profesional.",
        "purpose": "Monitorear aprendizajes y aportar evidencia para políticas, formación docente y reflexión del sistema en áreas que no siempre tienen una medición censal periódica.",
        "status": "Familia explicada con cinco rutas de referencia; ciclos y áreas deben verificarse en el plan vigente",
        "framework_id": None,
        "source_url": "https://www.agenciaeducacion.cl/orientar/estudios/estudios-nacionales/",
        "documents": [
            ("Estudios Nacionales · Agencia de Calidad", "https://www.agenciaeducacion.cl/orientar/estudios/estudios-nacionales/"),
            ("Propuesta de Plan de Evaluaciones y estudios muestrales", "https://archivos.agenciaeducacion.cl/Propuesta_de_Plan_de_Evaluaciones_del_Consejo_ACE_FINAL.pdf"),
        ],
    },
    "interna": {
        "name": "Evaluación formativa interna del proyecto",
        "short_name": "Interna",
        "category": "Evaluación de aula",
        "population": "Estudiantes de 1° básico a 4° medio en clases y tareas del proyecto.",
        "purpose": "Observar, retroalimentar, intervenir y reevaluar sin convertir automáticamente la evidencia en nota.",
        "status": "Modelada con ciclo de evidencia y muestras breves originales; cobertura completa pendiente",
        "framework_id": "internal-formative-v1",
        "source_url": "https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/EVALUACION_FORMATIVA.md",
        "documents": [],
    },
}


# Perfiles de lectura docente. La síntesis se apoya en las fuentes institucionales
# enlazadas en cada instrumento; la conexión a OA se declara siempre como propuesta
# pedagógica del proyecto y nunca como equivalencia oficial.
INSTRUMENT_PROFILES = {
    "paes": {
        "definition": "Conjunto de pruebas del Sistema de Acceso a la educación superior chilena. Combina conocimientos curriculares con la capacidad de usarlos para resolver tareas; sus resultados participan, junto con otros factores, en la postulación centralizada.",
        "why_exists": "Fue creada para reemplazar gradualmente el modelo PSU/PDT por instrumentos orientados al saber y al saber hacer, con dos oportunidades anuales y una escala que permite mantener puntajes vigentes entre procesos consecutivos.",
        "responsible": "Comité Técnico de Acceso, Ministerio de Educación y DEMRE de la Universidad de Chile",
        "first_cycle": "Primera aplicación regular: noviembre de 2022, Admisión 2023",
        "cadence": "Aplicación regular y aplicación de invierno; reglas, temarios y fechas cambian por proceso de admisión",
        "history": [
            ("1967–2002", "PAA", "La Prueba de Aptitud Académica y pruebas específicas organizaron la selección universitaria durante 35 años."),
            ("2003–2020", "PSU", "La Prueba de Selección Universitaria trasladó el foco hacia contenidos curriculares de enseñanza media; sus brechas y diseño fueron objeto de revisión."),
            ("2021–julio 2022", "PDT", "Las Pruebas de Transición incorporaron progresivamente preguntas de competencias y cerraron la etapa PSU."),
            ("Noviembre 2022", "Primera PAES", "Comenzó la aplicación regular con tareas basadas en saber y saber hacer y una escala de 100 a 1.000 puntos."),
            ("Hoy", "Sistema vigente", "Existen pruebas obligatorias, electivas y M2; cada proceso publica sus propios temarios, formas y tablas."),
        ],
        "predecessors": [
            ("Bachillerato", "Antecedente previo a 1967; no es una forma antigua de PAES."),
            ("PAA", "Medía aptitudes y conocimientos específicos en otro sistema de admisión."),
            ("PSU", "Priorizó contenidos curriculares y fue sustituida mediante una transición."),
            ("PDT", "Puente técnico y operativo entre PSU y PAES, no una versión paralela vigente."),
        ],
        "design": [
            "Competencia Lectora y Competencia Matemática 1 son pruebas obligatorias para la postulación centralizada.",
            "Ciencias e Historia y Ciencias Sociales son electivas; M2 se exige en carreras que declaran una demanda matemática adicional.",
            "Los temarios delimitan conocimientos y habilidades por proceso; una preparación responsable parte de la trayectoria escolar, no de trucos aislados.",
            "Los OA anteriores al rango declarado por un temario pueden funcionar como prerrequisitos pedagógicos, pero no deben presentarse por eso como contenido evaluado directamente en la PAES.",
            "La transformación desde respuestas correctas a puntaje depende de tablas oficiales de cada aplicación y forma.",
        ],
        "reporting": [
            "Entrega puntajes por prueba para el proceso de admisión y permite usar el mejor puntaje vigente conforme a las reglas oficiales.",
            "No entrega por sí sola un diagnóstico detallado de cada subhabilidad ni explica la causa pedagógica de un error.",
        ],
        "classroom_use": [
            "Usar el temario vigente para reconocer demandas y regresar a los OA que construyen esas habilidades durante la escolaridad.",
            "Practicar transferencia con textos, problemas y fuentes nuevos, conservando explicación y justificación.",
            "Registrar patrones en varias tareas antes de decidir una intervención; no convertir una muestra breve en predictor de admisión.",
        ],
        "boundaries": [
            "Este repositorio no reproduce preguntas protegidas ni declara que sus tareas sean formas oficiales.",
            "Los 0–4 puntos de los ejemplos no se convierten a la escala PAES de 100–1.000.",
            "Una relación entre PAES, OA y clase es una correspondencia pedagógica inferida, salvo que una fuente oficial diga expresamente lo contrario.",
        ],
    },
    "simce": {
        "definition": "Medición estandarizada nacional que forma parte del sistema de evaluación chileno y observa aprendizajes respecto del Currículum Nacional en niveles y áreas fijados por el plan vigente. Se complementa con información de contexto.",
        "why_exists": "Busca entregar evidencia comparable sobre resultados educativos para orientar decisiones del sistema, establecimientos y comunidades. No fue creado como examen de promoción individual ni como reemplazo de la evaluación de aula.",
        "responsible": "Agencia de Calidad de la Educación",
        "first_cycle": "SIMCE se inició oficialmente en 1988",
        "cadence": "Plan nacional por niveles y áreas; el calendario debe comprobarse cada año",
        "history": [
            ("1968–1971", "Prueba nacional de 8° básico", "Primer antecedente de medición anual de logros a escala nacional."),
            ("1982", "PER", "El Programa de Evaluación del Rendimiento Escolar apoyó desarrollo curricular y decisiones de recursos."),
            ("1985", "SECE", "El Sistema de Evaluación de la Calidad de la Educación analizó la información recogida por PER."),
            ("1988", "Inicio de SIMCE", "Se instaló una evaluación externa destinada a informar a distintos actores del sistema."),
            ("2012 en adelante", "Nueva institucionalidad", "SIMCE quedó integrado al Sistema de Aseguramiento de la Calidad y a la Agencia de Calidad."),
        ],
        "predecessors": [
            ("Prueba nacional 1968–1971", "Antecedente histórico limitado a 8° básico."),
            ("PER", "Programa de 1982 que recogió evidencia de rendimiento escolar."),
            ("SECE", "Sistema de 1985 que antecedió directamente a SIMCE."),
        ],
        "design": [
            "Evalúa áreas y niveles definidos por el Plan de Evaluaciones Nacionales e Internacionales.",
            "Las pruebas se construyen con referencia curricular y los cuestionarios recogen factores de contexto.",
            "Los resultados se informan con metodologías y categorías oficiales; no se reconstruyen desde un ensayo breve propio.",
            "La aplicación es censal en los niveles evaluados, con excepciones y modalidades definidas institucionalmente.",
        ],
        "reporting": [
            "Permite observar resultados agregados y tendencias para apoyar reflexión pedagógica y gestión institucional.",
            "No permite etiquetar a un estudiante ni atribuir causalidad a una sola práctica, curso o docente.",
        ],
        "classroom_use": [
            "Leer ejemplos y orientaciones oficiales para comprender la demanda, no para entrenar formatos de manera mecánica.",
            "Relacionar el área evaluada con OA del nivel y revisar evidencia cotidiana de las clases enlazadas.",
            "Combinar resultados agregados con trabajos, tickets y observaciones antes de priorizar una intervención.",
        ],
        "boundaries": [
            "El calendario 2026 documentado aquí no se proyecta automáticamente a años siguientes.",
            "Las muestras breves del proyecto no producen niveles de desempeño SIMCE.",
            "La asociación a dos OA es una puerta de entrada docente, no una cobertura del marco completo.",
        ],
    },
    "dia": {
        "definition": "Herramienta evaluativa voluntaria, flexible y de uso interno que la Agencia pone a disposición de los establecimientos para observar aprendizaje académico, aprendizaje socioemocional y convivencia en distintos momentos del año.",
        "why_exists": "Permite que equipos docentes y directivos cuenten con información oportuna para ajustar la planificación, monitorear avances y evaluar las acciones realizadas, sin convertir la medición en rendición externa de cuentas.",
        "responsible": "Agencia de Calidad de la Educación",
        "first_cycle": "Desarrollado en el contexto de recuperación educativa; formalizado mediante resoluciones y manuales desde 2021",
        "cadence": "Tres periodos: Diagnóstico, Monitoreo Intermedio y Evaluación de Cierre",
        "history": [
            ("2017–2020", "Evaluación Progresiva", "La Agencia ofreció diagnóstico, monitoreo y trayectoria para lectura en 2° básico y luego matemática en 7° básico como evaluación interna voluntaria."),
            ("2021", "Regulación y despliegue", "La Agencia publicó disposiciones de uso y amplió instrumentos académicos y socioemocionales."),
            ("2022", "Manual institucional", "Se consolidó el carácter voluntario, interno y formativo del proceso."),
            ("Hoy", "Ciclo durante el año", "La oferta se actualiza por periodo, nivel y área; incluye lectura, escritura, matemática y otras áreas según disponibilidad."),
        ],
        "predecessors": [
            ("Evaluación diagnóstica de aula", "Práctica pedagógica previa y más amplia; DIA la apoya, no la sustituye."),
            ("Instrumentos de la Agencia", "DIA reutiliza experiencia institucional, pero sus resultados tienen un propósito interno distinto de SIMCE."),
        ],
        "design": [
            "Combina instrumentos académicos y actividades o cuestionarios socioemocionales según nivel.",
            "El periodo diagnóstico observa aprendizajes previos; el monitoreo intermedio analiza avance; el cierre compara progreso y orienta continuidad.",
            "En lectura distingue procesos como localizar, interpretar y relacionar, y reflexionar; la oferta exacta debe verificarse en la plataforma.",
            "Los resultados pertenecen al trabajo interno del establecimiento y requieren conversación profesional para decidir acciones.",
        ],
        "reporting": [
            "Entrega información para ajustar planificación y analizar avance dentro del establecimiento.",
            "No es calificación, ranking, SIMCE alternativo ni diagnóstico clínico o psicológico.",
        ],
        "classroom_use": [
            "Antes: acordar propósito, condiciones y decisiones que sí podrán tomarse con la evidencia.",
            "Después: contrastar con clases, producciones y observaciones; seleccionar una intervención concreta.",
            "En el siguiente periodo: usar una situación distinta para comprobar cambio y transferencia.",
        ],
        "boundaries": [
            "La disponibilidad de pruebas y niveles cambia; se consulta siempre la plataforma oficial.",
            "Una respuesta aislada es una observación, no un diagnóstico pedagógico definitivo.",
            "Los ejemplos del proyecto ilustran el ciclo, pero no reemplazan los instrumentos DIA.",
        ],
    },
    "pisa": {
        "definition": "Estudio internacional de la OCDE, basado en una muestra de estudiantes de 15 años, que analiza cómo aplican conocimientos y habilidades de lectura, matemática y ciencias a problemas relevantes para la vida social.",
        "why_exists": "Fue diseñado para producir indicadores comparables sobre la preparación de quienes se acercan al final de la educación obligatoria, más allá del dominio de un currículo nacional específico.",
        "responsible": "OCDE; en Chile coordina la Agencia de Calidad de la Educación",
        "first_cycle": "Programa lanzado en 1997 y aplicado por primera vez en 2000",
        "cadence": "Históricamente trienal; la Agencia informa ciclos de cuatro años desde 2025",
        "history": [
            ("1997", "Creación del programa", "La OCDE inició el desarrollo de indicadores comparables centrados en lo que estudiantes pueden hacer con lo aprendido."),
            ("2000", "Primera aplicación", "Lectura fue el dominio principal del primer ciclo."),
            ("2012 en adelante", "Dominios innovadores", "Se incorporaron áreas emergentes además de lectura, matemática y ciencias."),
            ("2022", "Ciclo postergado", "La pandemia alteró la cadencia prevista y el ciclo 2021 pasó a denominarse PISA 2022."),
            ("2025", "Ciencia y mundo digital", "Ciencias fue dominio principal y aprendizaje en el mundo digital integró el diseño del ciclo."),
        ],
        "predecessors": [
            ("Encuestas internacionales previas", "Aportaron tradición comparativa, pero PISA inauguró un programa propio centrado en población de 15 años."),
            ("No tiene una 'PISA chilena' anterior", "No debe confundirse su historia con la secuencia PAA–PSU–PDT–PAES."),
        ],
        "design": [
            "Selecciona una muestra representativa de estudiantes de 15 años matriculados desde 7° grado, no un curso chileno único.",
            "Rota un dominio principal entre lectura, matemática y ciencias e incorpora cuestionarios de contexto y dominios innovadores.",
            "Plantea situaciones y problemas que exigen examinar, interpretar, razonar y comunicar.",
            "Sus escalas y comparaciones se estiman para sistemas y poblaciones mediante diseño muestral y procedimientos técnicos.",
        ],
        "reporting": [
            "Informa desempeño y contexto de sistemas educativos, distribuciones y tendencias comparables bajo condiciones técnicas.",
            "No entrega una nota curricular individual ni prescribe un currículo escolar.",
        ],
        "classroom_use": [
            "Diseñar tareas de transferencia con fuentes, datos y contextos nuevos sin copiar unidades protegidas.",
            "Enseñar explícitamente a seleccionar información, modelar, justificar y evaluar límites.",
            "Usar el resultado sólo como evidencia de la tarea local y regresar a OA concretos si aparece una dificultad.",
        ],
        "boundaries": [
            "Una tarea 'inspirada en PISA' no forma parte de PISA ni permite comparar países.",
            "El rango de 15 años no equivale automáticamente a II medio.",
            "La correspondencia curricular del proyecto es inferida y se declara como tal.",
        ],
    },
    "timss": {
        "definition": "Estudio internacional de la IEA que mide tendencias en Matemática y Ciencias en los grados que representan cuatro y ocho años de escolaridad, con marcos construidos junto con los países participantes.",
        "why_exists": "Permite seguir resultados y contextos de enseñanza en dos momentos de la trayectoria escolar y comparar cambios entre ciclos con referencia a lo que se enseña en los sistemas participantes.",
        "responsible": "IEA y TIMSS & PIRLS International Study Center; en Chile coordina la Agencia de Calidad",
        "first_cycle": "1995",
        "cadence": "Cada cuatro años",
        "history": [
            ("1960–1980", "Estudios IEA previos", "Evaluaciones internacionales de matemática y ciencias establecieron antecedentes metodológicos."),
            ("1995", "Primer TIMSS", "Comenzó la serie periódica conjunta en matemática y ciencias."),
            ("1995–hoy", "Tendencias de 4° y 8°", "Los ciclos cuatrienales permiten observar cohortes de manera cuasi longitudinal."),
            ("Etapa digital", "eTIMSS", "El estudio ha transitado a entornos digitales y tareas interactivas según ciclo."),
        ],
        "predecessors": [
            ("FIMS/SIMS", "Estudios internacionales de matemática anteriores a la serie TIMSS."),
            ("FISS/SISS", "Estudios internacionales de ciencias que antecedieron la integración periódica."),
        ],
        "design": [
            "Evalúa contenidos de Matemática y Ciencias y procesos cognitivos de conocer, aplicar y razonar.",
            "La población corresponde a grados internacionales definidos por años de escolaridad; la referencia chilena requiere comprobar la aplicación nacional.",
            "Incluye cuestionarios para estudiantes, docentes, directivos y hogares o contextos según el ciclo.",
            "Su diseño cuatrienal relaciona el grado 4 de un ciclo con el grado 8 del ciclo siguiente sin seguir necesariamente a los mismos estudiantes.",
        ],
        "reporting": [
            "Entrega tendencias y comparaciones de sistemas, dominios de contenido, procesos cognitivos y factores de contexto.",
            "No valida automáticamente una secuencia local ni produce diagnóstico individual a partir de una tarea breve.",
        ],
        "classroom_use": [
            "Comparar demandas de contenido y proceso con los OA chilenos sin declarar equivalencia de grados.",
            "Alternar tareas de conocer, aplicar y razonar sobre un mismo contenido.",
            "Si el estudiante conoce un procedimiento pero no lo aplica, regresar a clases de representación y modelación antes de repetir el ensayo.",
        ],
        "boundaries": [
            "Las referencias a 4° y 8° básico en este portal son aproximaciones pedagógicas explícitas.",
            "Los puntos del proyecto no corresponden a benchmarks internacionales TIMSS.",
            "No se copian preguntas ni se simula el diseño muestral internacional.",
        ],
    },
    "pirls": {
        "definition": "Estudio internacional de la IEA sobre comprensión lectora en el grado que representa cuatro años de escolaridad, etapa asociada al tránsito desde aprender a leer hacia leer para aprender.",
        "why_exists": "Permite observar tendencias de lectura, propósitos de lectura, procesos de comprensión y condiciones del hogar y la escuela que se relacionan con el aprendizaje.",
        "responsible": "IEA y TIMSS & PIRLS International Study Center; en Chile coordina la Agencia de Calidad",
        "first_cycle": "2001",
        "cadence": "Cada cinco años",
        "history": [
            ("1991", "IEA Reading Literacy Study", "Estudio internacional que sirvió de base conceptual y metodológica para PIRLS."),
            ("2001", "Primer PIRLS", "Comenzó la medición quinquenal de tendencias en lectura de cuarto grado."),
            ("2016", "ePIRLS", "Se incorporó una extensión para lectura informativa en línea."),
            ("2021–2026", "Transición digital", "Los ciclos avanzan hacia una evaluación digital integrada con materiales interactivos."),
        ],
        "predecessors": [
            ("IEA Reading Literacy Study 1991", "Fundamento directo del diseño de tendencias de lectura."),
            ("No es un curso de comprensión", "Es un estudio muestral; el currículo y las clases siguen siendo la base de enseñanza."),
        ],
        "design": [
            "Organiza la lectura por dos propósitos: experiencia literaria y adquirir y usar información.",
            "Observa recuperar información explícita, inferir, interpretar e integrar, y evaluar contenido y elementos textuales.",
            "Incluye cuestionarios de hogar, estudiante, docente y escuela para describir contextos de aprendizaje.",
            "La población objetivo es el grado que representa cuatro años desde el inicio de primaria, no una edad fija universal.",
        ],
        "reporting": [
            "Entrega tendencias y comparaciones de comprensión lectora y contexto en sistemas participantes.",
            "No reemplaza la evaluación de fluidez, escritura, conversación literaria ni seguimiento individual del aula.",
        ],
        "classroom_use": [
            "Planificar lectura de textos literarios e informativos con preguntas que recorran los cuatro procesos.",
            "Distinguir localizar de inferir y de evaluar para retroalimentar la acción, no la identidad del lector.",
            "Reevaluar con otro texto y propósito para comprobar transferencia.",
        ],
        "boundaries": [
            "Los OA enlazados son apoyos chilenos existentes, no una tabla oficial PIRLS–currículo.",
            "Una miniunidad del portal no reproduce la extensión ni las escalas PIRLS.",
            "No se concluye dominio lector general desde un texto único.",
        ],
    },
    "erce": {
        "definition": "Estudio regional del LLECE de UNESCO que compara aprendizajes y factores asociados en América Latina y el Caribe con marcos consensuados a partir de currículos de los países participantes.",
        "why_exists": "Responde a la necesidad regional de evidencia comparable y pertinente para comprender logros, brechas y contextos en Lectura, Escritura, Matemática y Ciencias.",
        "responsible": "OREALC/UNESCO Santiago y LLECE; en Chile coordina la Agencia de Calidad",
        "first_cycle": "PERCE 1997; la denominación ERCE se usa para el cuarto estudio de 2019 y siguientes",
        "cadence": "Ciclos regionales: PERCE 1997, SERCE 2006, TERCE 2013, ERCE 2019 y ERCE 2025",
        "history": [
            ("1994", "Creación del LLECE", "La red regional nació para fortalecer evaluación y capacidades técnicas en América Latina y el Caribe."),
            ("1997", "PERCE", "Primer estudio regional comparativo y explicativo."),
            ("2006", "SERCE", "Segundo estudio, con ampliación de áreas y análisis regional."),
            ("2013", "TERCE", "Tercer estudio y base de comparabilidad para ciclos posteriores."),
            ("2019 / 2025", "ERCE", "Cuarto y quinto estudios; Chile no aplicó el ciclo 2019 y retomó la aplicación en 2025."),
        ],
        "predecessors": [
            ("PERCE", "Primera medición regional de la serie, no comparable en todos sus resultados con ciclos posteriores."),
            ("SERCE", "Segunda aplicación regional de 2006."),
            ("TERCE", "Tercera aplicación de 2013 y antecedente directo de ERCE."),
        ],
        "design": [
            "Evalúa 3° y 6° básico en Lectura, Escritura y Matemática; Ciencias se incorpora en 6° según el ciclo.",
            "Combina dominios de contenido, procesos cognitivos y cuestionarios de contexto.",
            "Su marco curricular regional se acuerda analizando currículos participantes; no replica uno solo.",
            "En Chile, la aplicación y participación exactas deben leerse en la ficha del ciclo vigente.",
        ],
        "reporting": [
            "Entrega resultados regionales y nacionales sobre logro y factores asociados.",
            "No permite adjudicar causalidad simple a un factor ni reemplaza la evaluación de aula.",
        ],
        "classroom_use": [
            "Usar sus dominios para ampliar tareas de lectura, escritura, matemática y ciencias en contextos latinoamericanos pertinentes.",
            "Conectar procesos con OA existentes y observar producción escrita, no sólo reconocimiento de alternativas.",
            "Contrastar evidencia de varias tareas antes de intervenir y reevaluar con otra situación.",
        ],
        "boundaries": [
            "Chile no aplicó ERCE 2019; el portal no atribuye a Chile resultados que no existen para ese ciclo.",
            "Los ejemplos son originales y no son ítems liberados de UNESCO.",
            "Dos OA por variante orientan el recorrido, pero no agotan el marco ERCE.",
        ],
    },
    "icils": {
        "definition": "Estudio internacional de la IEA que observa alfabetización computacional e informacional en estudiantes de 8° grado y, cuando el país participa en el módulo, pensamiento computacional.",
        "why_exists": "Fue creado ante la necesidad de saber si los jóvenes pueden investigar, crear, participar y comunicar con computadores de manera crítica, más allá de asumir que por usar tecnología ya poseen alfabetización digital.",
        "responsible": "IEA; en Chile coordina la Agencia de Calidad de la Educación",
        "first_cycle": "2013",
        "cadence": "Ciclos 2013, 2018 y 2023; la Agencia lo describe como quinquenal",
        "history": [
            ("2013", "Primer ICILS", "Midió alfabetización computacional e informacional en una evaluación íntegramente digital."),
            ("2018", "Segundo ciclo", "Consolidó tendencias e incorporó pensamiento computacional como opción."),
            ("2023", "Tercer ciclo", "Evaluó CIL y, en países participantes, pensamiento computacional en un entorno digital actualizado."),
        ],
        "predecessors": [
            ("SITES y estudios TIC de IEA", "Aportaron información sobre tecnología en educación, pero ICILS mide directamente desempeño estudiantil digital."),
            ("No equivale a una asignatura de computación", "Integra información, comunicación, creación y juicio crítico en tareas digitales."),
        ],
        "design": [
            "Evalúa en computador la capacidad de buscar, juzgar, transformar, crear y comunicar información.",
            "El pensamiento computacional es un constructo diferenciado y su participación puede ser opcional según el ciclo.",
            "Incluye cuestionarios de contexto sobre acceso, uso, enseñanza y aprendizaje con tecnologías.",
            "La muestra representa estudiantes del grado objetivo; no califica individualmente a todo el sistema escolar.",
        ],
        "reporting": [
            "Entrega comparaciones y niveles de alfabetización digital y contexto para políticas educativas.",
            "No prueba que una persona sea segura, ética o competente en toda plataforma digital.",
        ],
        "classroom_use": [
            "Enseñar verificación de fuente, fecha, autoría y evidencia antes de producir o compartir información.",
            "Proponer tareas digitales con propósito, audiencia, transformación de información y reflexión ética.",
            "Separar dificultades de lectura, búsqueda, evaluación de fuentes y operación técnica antes de intervenir.",
        ],
        "boundaries": [
            "Los OA de Tecnología enlazados son una referencia parcial y no una equivalencia oficial ICILS.",
            "La muestra textual no reproduce la interacción digital completa del estudio.",
            "Alfabetización digital no se infiere por frecuencia de uso de dispositivos.",
        ],
    },
    "iccs": {
        "definition": "Estudio internacional de la IEA que investiga cómo estudiantes de 8° grado están preparados para asumir roles ciudadanos, considerando conocimiento, razonamiento, actitudes, percepciones y participación.",
        "why_exists": "Permite comprender educación cívica y ciudadanía en contextos sociales cambiantes sin reducirlas a memorización institucional ni a una sola opinión política.",
        "responsible": "IEA; en Chile coordina la Agencia de Calidad de la Educación",
        "first_cycle": "ICCS 2009; antecedente directo CIVED 1999",
        "cadence": "Ciclos ICCS 2009, 2016, 2022 y preparación de ICCS 2027",
        "history": [
            ("1971", "Primer estudio cívico de IEA", "Antecedente internacional sobre educación cívica."),
            ("1999", "CIVED", "Estudió conocimiento y actitudes cívicas de jóvenes y permitió enlaces posteriores."),
            ("2009", "Primer ICCS", "Amplió conocimientos, disposiciones y contextos con módulos regionales."),
            ("2016 y 2022", "Nuevos ciclos", "Actualizaron problemas ciudadanos, actitudes y participación ante cambios sociales."),
            ("2027", "Próximo ciclo", "Chile prepara estudio experimental y definitivo según el calendario oficial."),
        ],
        "predecessors": [
            ("IEA Civic Education Study 1971", "Primer antecedente internacional de la línea."),
            ("CIVED 1999", "Predecesor directo; ICCS 2009 conservó vínculos para estudiar tendencias."),
        ],
        "design": [
            "Combina prueba de conocimiento y razonamiento cívico con cuestionarios sobre actitudes, percepciones y participación.",
            "Recoge contexto de estudiantes, docentes y establecimientos y puede incluir módulos regionales.",
            "Distingue comprender instituciones y procesos, justificar posiciones y disposición a participar.",
            "Las actitudes se interpretan a nivel de estudio y no se convierten en calificación moral individual.",
        ],
        "reporting": [
            "Informa preparación cívica, actitudes y contextos de estudiantes y sistemas participantes.",
            "No etiqueta a una persona como buena o mala ciudadana ni prescribe una opinión política correcta.",
        ],
        "classroom_use": [
            "Trabajar casos públicos con fuentes diversas, derechos, instituciones y decisiones justificadas.",
            "Separar hechos, interpretación y posición; pedir evidencia y reconocer límites.",
            "Crear espacios seguros donde disentir razonadamente no reduzca la evaluación del estudiante.",
        ],
        "boundaries": [
            "El portal evalúa argumentación y uso de fuentes, no adhesión ideológica.",
            "Las clases de Historia son referencias pedagógicas parciales.",
            "Un caso local no produce puntaje ni nivel ICCS.",
        ],
    },
    "eces": {
        "definition": "Estudio comparativo de políticas y provisión de educación en primera infancia. Describe cómo los países organizan acceso, proveedores, participación, calidad y expectativas; no es una prueba aplicada a estudiantes escolares.",
        "why_exists": "Busca comprender fortalezas y debilidades de los sistemas de educación parvularia y su papel en la preparación de niños y niñas para aprendizajes y demandas sociales posteriores.",
        "responsible": "IEA, NFER y CREC; en Chile respondió la Agencia de Calidad de la Educación",
        "first_cycle": "Datos comparativos recogidos entre 2014 y 2015",
        "cadence": "Estudio comparativo específico; no posee un calendario escolar periódico equivalente a TIMSS o PIRLS",
        "history": [
            ("2014–2015", "Recolección internacional", "Ocho países completaron cuestionarios sobre políticas y provisión de educación inicial."),
            ("Publicación", "Resultados comparativos", "Los informes describieron regulación, acceso, personal, calidad y expectativas entre sistemas."),
            ("En este repositorio", "Fuera de cobertura curricular", "Se documenta para completar el panorama chileno, pero no se fuerza a OA de 1° básico–4° medio."),
        ],
        "predecessors": [
            ("No es una serie de pruebas escolares", "No tiene versiones por curso ni antecesores equivalentes a PAA/PSU o PER/SECE."),
            ("Estudios de política de primera infancia", "Pertenece a una tradición comparativa de sistemas y provisión, no de puntaje estudiantil."),
        ],
        "design": [
            "Recoge información mediante cuestionarios y revisión de políticas nacionales.",
            "Analiza políticas, modelos de provisión, participación y matrícula, promoción de calidad y expectativas de resultados.",
            "La unidad de análisis principal es el sistema de educación inicial, no el desempeño de un estudiante.",
            "No corresponde producir una muestra escolar ECES ni calcular puntajes de aprendizaje.",
        ],
        "reporting": [
            "Entrega una comparación descriptiva y crítica de la organización de educación parvularia.",
            "No entrega resultados individuales, niveles de logro escolar ni rutas de preparación para una prueba.",
        ],
        "classroom_use": [
            "Usarlo como referencia de política y transición educativa, no como instrumento de aula.",
            "Si el proyecto incorpora educación parvularia en el futuro, comenzar por Bases Curriculares y evaluación auténtica, no por simular ECES.",
        ],
        "boundaries": [
            "El repositorio comienza en 1° básico; por eso ECES se explica pero no se enlaza artificialmente a OA escolares.",
            "No se crea ensayo, escala ni preparación ECES.",
            "Su presencia completa el panorama de estudios en Chile y muestra por qué 'instrumento' no siempre significa prueba.",
        ],
    },
    "impulso-lector": {
        "definition": "Evaluación nacional censal anunciada para 2° básico en 2026. Se aplica en dos jornadas y observa tres componentes de la lectura inicial: precursores, comprensión y fluidez; oficialmente no forma parte de SIMCE.",
        "why_exists": "Busca entregar información temprana sobre habilidades fundamentales de lectura para apoyar decisiones antes de que las dificultades se acumulen en la trayectoria escolar.",
        "responsible": "Agencia de Calidad de la Educación, en el marco del Plan de Evaluaciones 2024–2026",
        "first_cycle": "Primera aplicación censal programada entre el 16 de noviembre y el 4 de diciembre de 2026",
        "cadence": "Primera aplicación al corte documental; no se asume una periodicidad futura no publicada",
        "history": [
            ("2017–2020", "Evaluación Progresiva", "La Agencia ofreció instrumentos internos voluntarios de comprensión lectora en 2° básico durante tres momentos del año."),
            ("2021 en adelante", "DIA y reactivación lectora", "El diagnóstico, monitoreo y cierre se integraron en una herramienta interna más amplia y se incorporaron apoyos para reactivación de la lectura."),
            ("2024–2025", "Diseño y pilotaje", "La Agencia informa validación experta y pilotaje de prototipos antes de la aplicación censal."),
            ("2026", "Primera aplicación Impulso Lector", "Se anuncia una evaluación externa censal separada de SIMCE para 2° básico."),
        ],
        "predecessors": [
            ("Evaluación Progresiva de Lectura", "Herramienta interna voluntaria desde 2017; comparte interés por lectura inicial, pero tenía otro propósito y modo de aplicación."),
            ("DIA Reactivación de la Lectura", "Herramienta interna que apoya decisiones pedagógicas; no debe confundirse con la nueva medición censal."),
            ("Estudio Nacional de Lectura 2° básico", "Medición muestral del sistema; Impulso Lector se anuncia como censal."),
        ],
        "design": [
            "Día 1 considera precursores de la lectura; día 2 considera comprensión y una actividad individual de fluidez.",
            "La fluidez se observa mediante lectura en voz alta y una rúbrica de velocidad, precisión y expresión, según la presentación institucional.",
            "La comprensión utiliza cuadernillos cuyo formato prototipo fue publicado por la Agencia.",
            "Al corte del repositorio la primera aplicación todavía no ha ocurrido; no existen resultados nacionales que este proyecto pueda resumir.",
        ],
        "reporting": [
            "Está diseñada para entregar evidencia temprana a establecimientos y al sistema sobre componentes de lectura inicial.",
            "Los detalles finales de reportes, escalas y uso deben leerse en la documentación oficial posterior a la aplicación.",
        ],
        "classroom_use": [
            "Enseñar conciencia fonológica, decodificación, fluidez y comprensión dentro de experiencias lectoras significativas, no como entrenamiento del cuadernillo.",
            "Separar precisión, ritmo, expresión y comprensión al observar una lectura; una dimensión no sustituye a las demás.",
            "Usar las clases de 1° y 2° básico enlazadas para intervenir y reevaluar con textos nuevos, sin esperar la medición censal.",
        ],
        "boundaries": [
            "Impulso Lector no es SIMCE, aunque ambos sean coordinados por la Agencia.",
            "Los prototipos oficiales muestran formato; los ejemplos del proyecto son originales y no se presentan como cuadernillos oficiales.",
            "No se anticipan puntajes, niveles ni resultados de una aplicación que aún no se ha realizado al corte documental.",
        ],
    },
    "estudios-nacionales": {
        "definition": "Familia de estudios muestrales de la Agencia aplicada a áreas y niveles seleccionados. A diferencia de SIMCE censal o DIA interno, busca producir una fotografía representativa del sistema sobre aprendizajes específicos.",
        "why_exists": "Permite monitorear áreas relevantes que requieren evidencia nacional profunda sin aplicar necesariamente una prueba a cada estudiante del país, y orientar políticas, investigación, formación docente y mejora educativa.",
        "responsible": "Agencia de Calidad de la Educación",
        "first_cycle": "La página institucional reúne estudios de distintos años; cada área conserva su propio ciclo e informe",
        "cadence": "Muestral y definida por el Plan de Evaluaciones; no existe una periodicidad única para toda la familia",
        "history": [
            ("Antes de 2012", "Evaluaciones nacionales por área", "Chile desarrolló mediciones específicas de lectura, escritura, inglés y educación física en distintos periodos."),
            ("2016–2020", "Plan con estudios muestrales", "Se organizaron aplicaciones en escritura, formación ciudadana, inglés y otras áreas complementarias."),
            ("2021–2025", "Priorización de áreas críticas", "La propuesta de plan mantuvo lectura inicial, escritura y competencias técnico-profesionales entre los estudios muestrales."),
            ("Archivo vigente", "Resultados por estudio", "La Agencia conserva informes y fichas; el año y la población deben leerse en cada publicación."),
        ],
        "predecessors": [
            ("Mediciones nacionales específicas", "Cada área tiene antecedentes propios; no hay una única prueba anterior llamada 'Estudio Nacional'."),
            ("SIMCE por áreas", "Algunas áreas fueron medidas por SIMCE en otros periodos, pero una medición muestral tiene alcance y reporte diferentes."),
            ("Evaluación Progresiva", "Herramienta interna para monitoreo; complementaba, pero no era el estudio nacional muestral."),
        ],
        "design": [
            "Selecciona una muestra representativa de establecimientos y estudiantes para el área y nivel definidos.",
            "Puede combinar pruebas de desempeño con cuestionarios de contexto y rúbricas según el constructo.",
            "La familia incluye estudios de Lectura 2° básico, Escritura 6° básico, Formación Ciudadana 8° básico, Inglés en enseñanza media y competencias de educación media técnico-profesional, según los planes e informes disponibles.",
            "Cada estudio posee marco, año y metodología propios; no corresponde sumar sus resultados en un puntaje común.",
        ],
        "reporting": [
            "Entrega estimaciones nacionales y análisis por área para orientar discusión y decisiones de política.",
            "No entrega necesariamente resultados individuales ni permite diagnosticar a estudiantes que no integraron la muestra.",
        ],
        "classroom_use": [
            "Leer los informes para reconocer desafíos sistémicos y revisar si la evidencia local muestra una necesidad semejante.",
            "Usar las rutas del portal para enseñar el contenido concreto y recoger evidencia propia de aula.",
            "No convertir un promedio nacional en expectativa rígida para un estudiante o curso particular.",
        ],
        "boundaries": [
            "Los niveles y áreas cambian por plan; esta página no los presenta como calendario anual permanente.",
            "Las cinco rutas del proyecto son entradas pedagógicas y no reconstruyen el marco completo de cada estudio.",
            "Las muestras breves no producen resultados muestrales nacionales ni escalas oficiales.",
        ],
    },
    "interna": {
        "definition": "Sistema de evaluación formativa propio del proyecto: recoge evidencias breves de clases y tareas para describir qué ocurrió, formular hipótesis prudentes, intervenir con contenido existente y reevaluar en una situación diferente.",
        "why_exists": "Los estudios externos no explican por sí solos qué necesita aprender un estudiante mañana. Esta capa cierra el ciclo entre OA, clase, evidencia, retroalimentación, intervención y transferencia.",
        "responsible": "Docente y establecimiento; el repositorio aporta estructuras y ejemplos, no decisiones automáticas",
        "first_cycle": "Integrada desde el diseño original de clases; formalizada como ciclo de evidencia en la capa de competencias v1",
        "cadence": "Continua: antes, durante y después de la enseñanza",
        "history": [
            ("Base del repositorio", "Evaluación formativa por clase", "Las fichas ya contenían evidencias, criterios, apoyos, profundizaciones y tickets de salida."),
            ("Capa de competencias v1", "Ciclo explícito", "Se separaron observación, patrón, hipótesis, intervención, reevaluación y decisión."),
            ("Estado actual", "Demostración determinista", "Existe un banco inicial y rutas a clases; no hay plataforma con datos reales ni diagnóstico automatizado."),
        ],
        "predecessors": [
            ("Evaluación formativa existente", "No se reemplaza: se conecta longitudinalmente y se hace visible."),
            ("Tickets, rúbricas y evidencias", "Son fuentes de evidencia, no instrumentos descartados ni una escala única."),
        ],
        "design": [
            "Define el criterio antes de recoger evidencia y conserva el OA como referencia curricular.",
            "Distingue observación de hipótesis y exige recurrencia antes de recomendar intervención.",
            "Prioriza clases y apoyos existentes en lugar de generar contenido duplicado.",
            "Reevalúa con una situación nueva para comprobar transferencia y revisar la hipótesis.",
        ],
        "reporting": [
            "Produce descripciones pedagógicas comprensibles y decisiones revisables.",
            "No produce diagnósticos clínicos, porcentajes ficticios, etiquetas personales ni validez psicométrica.",
        ],
        "classroom_use": [
            "Aplicar una tarea breve con criterio observable y registrar la evidencia literal.",
            "Si el patrón se repite, elegir una clase enlazada, practicar y ofrecer retroalimentación descriptiva.",
            "Reevaluar con un caso distinto, comparar evidencia y decidir consolidar, transferir o revisar prerrequisitos.",
        ],
        "boundaries": [
            "El algoritmo no sustituye juicio docente ni contexto del estudiante.",
            "Los 0–4 puntos describen un ejemplo y no representan porcentaje de dominio longitudinal.",
            "Sin evidencia acumulada no se formula diagnóstico pedagógico.",
        ],
    },
}

for _instrument_key, _profile in INSTRUMENT_PROFILES.items():
    INSTRUMENTS[_instrument_key].update(_profile)

INSTRUMENTS["paes"]["documents"].append(("Historia oficial: cómo surgió la PAES", "https://portaldemre.demre.cl/paes/como-surgio-la-paes"))
INSTRUMENTS["simce"]["documents"].append(("Informe técnico SIMCE 2012 e historia de sus antecedentes", "https://archivos.agenciaeducacion.cl/documentos-web/Informe_Tecnico_Simce_2012.pdf"))
INSTRUMENTS["dia"]["documents"].append(("Manual de uso del Diagnóstico Integral de Aprendizajes", "https://diagnosticointegral.agenciaeducacion.cl/documentos/Manual_uso.pdf"))
INSTRUMENTS["dia"]["documents"].append(("Antecedente: Evaluación Progresiva de comprensión lectora", "https://archivos.agenciaeducacion.cl/Resignificamos_evaluacion_para_mejorar_aprendizajes.pdf"))
INSTRUMENTS["pisa"]["documents"].append(("Descripción y preguntas frecuentes PISA · OCDE", "https://www.oecd.org/en/about/programmes/pisa/pisa-frequently-asked-questions-faqs.html"))
INSTRUMENTS["timss"]["documents"].append(("Descripción oficial TIMSS · IEA", "https://www.iea.nl/studies/iea/timss"))
INSTRUMENTS["pirls"]["documents"].append(("Descripción oficial PIRLS · IEA", "https://www.iea.nl/studies/iea/pirls"))
INSTRUMENTS["erce"]["documents"].append(("Historia de tres décadas del LLECE · UNESCO", "https://www.unesco.org/en/articles/three-decades-regional-educational-assessment-unesco-publication-traces-history-llece-laboratory"))
INSTRUMENTS["icils"]["documents"].append(("ICILS 2023 · IEA", "https://www.iea.nl/node/2779"))
INSTRUMENTS["iccs"]["documents"].append(("ICCS 2022 · IEA", "https://www.iea.nl/studies/iea/iccs/2022"))
INSTRUMENTS["eces"]["documents"] = [("ECES · Agencia de Calidad", "https://www.agenciaeducacion.cl/evaluar/estudios-internacionales/eces/")]


SAMPLE_FORMS = {
    "reading-primary": {
        "title": "Leer un aviso y explicar una conclusión",
        "stimulus": "La biblioteca escolar abrirá los miércoles hasta las 17:00. El aviso agrega: ‘Trae tu credencial y devuelve los libros en el buzón si llegas después del cierre’. Martina quiere cambiar un libro el jueves a las 17:15.",
        "questions": [
            {"prompt": "¿Qué día existe horario extendido?", "options": ["Lunes", "Miércoles", "Jueves", "Viernes"], "answer": 1},
            {"prompt": "¿Qué puede hacer Martina a las 17:15 del jueves?", "options": ["Cambiar el libro con la bibliotecaria", "Dejar el libro en el buzón", "Entrar sin credencial", "Esperar dentro de la biblioteca"], "answer": 1},
        ],
        "open_prompt": "Explica qué información del aviso permite responder la segunda pregunta.",
        "open_rubric": ["0: no usa información del aviso", "1: menciona el buzón o el cierre sin conectar ambos", "2: relaciona el horario del jueves con la instrucción de devolución en el buzón"],
    },
    "reading-secondary": {
        "title": "Evaluar una propuesta y su evidencia",
        "stimulus": "El centro de estudiantes propone ampliar la biblioteca. Afirma que la medida mejorará el estudio autónomo y cita una encuesta respondida por 38 de los 760 estudiantes del liceo; 31 de esas respuestas apoyan la propuesta.",
        "questions": [
            {"prompt": "¿Cuál es la afirmación principal?", "options": ["La encuesta fue obligatoria", "La biblioteca debe ampliar su horario", "Solo 38 estudiantes usan libros", "El liceo tiene 31 estudiantes"], "answer": 1},
            {"prompt": "¿Cuál es la limitación más importante de la evidencia?", "options": ["La encuesta tiene una muestra pequeña y posiblemente autoseleccionada", "La encuesta usa números", "La propuesta menciona una biblioteca", "La mayoría de quienes respondieron está de acuerdo"], "answer": 0},
        ],
        "open_prompt": "Indica una evidencia adicional que permitiría evaluar mejor la propuesta y justifica por qué.",
        "open_rubric": ["0: opinión sin evidencia adicional", "1: propone un dato pertinente sin justificar su utilidad", "2: propone un dato pertinente y explica cómo mejora la representatividad o contrasta la afirmación"],
    },
    "english-secondary": {
        "title": "Understand a school announcement and respond for a purpose",
        "stimulus": "School notice: ‘The science club meeting will take place in Room 12 on Thursday at 3:30 p.m. Bring your observation notebook. Students who need an accessible route should enter through the library corridor.’",
        "questions": [
            {"prompt": "What should every participant bring?", "options": ["A library card", "An observation notebook", "A lab coat", "A printed map"], "answer": 1},
            {"prompt": "Why does the notice mention the library corridor?", "options": ["To change the meeting time", "To provide an accessible route", "To borrow a science book", "To cancel the club"], "answer": 1},
        ],
        "open_prompt": "Write a short message to a classmate explaining when and where the meeting is and what they need to bring.",
        "open_rubric": ["0: the message does not communicate the required information", "1: the message communicates some correct details but omits time, place or material", "2: the message clearly communicates time, place and required material in understandable English"],
    },
    "math-primary": {
        "title": "Resolver una compra y comprobar",
        "stimulus": "Una caja contiene 6 paquetes con 8 lápices cada uno. El curso necesita 45 lápices.",
        "questions": [
            {"prompt": "¿Cuántos lápices hay en la caja?", "options": ["14", "42", "48", "54"], "answer": 2},
            {"prompt": "¿Cuántos lápices sobran después de entregar 45?", "options": ["2", "3", "5", "13"], "answer": 1},
        ],
        "open_prompt": "Explica una forma distinta de comprobar que el resultado es correcto.",
        "open_rubric": ["0: no presenta comprobación", "1: repite el cálculo sin explicar", "2: usa operación inversa, descomposición o representación y conecta la comprobación con 48 y 45"],
    },
    "math-secondary": {
        "title": "Modelar el costo de un recorrido",
        "stimulus": "Una cooperativa cobra $1.200 de bajada de bandera y $350 por kilómetro recorrido. Un segundo servicio no cobra base y cobra $500 por kilómetro.",
        "questions": [
            {"prompt": "¿Qué expresión representa el primer servicio para x kilómetros?", "options": ["1.200x + 350", "1.200 + 350x", "500 + 350x", "1.550x"], "answer": 1},
            {"prompt": "¿Cuánto cuesta el primer servicio en 4 km?", "options": ["$1.550", "$2.000", "$2.600", "$3.200"], "answer": 2},
        ],
        "open_prompt": "Compara ambos servicios para 10 km y justifica cuál conviene, mostrando tus cálculos.",
        "open_rubric": ["0: elige sin cálculo pertinente", "1: calcula al menos un costo correctamente", "2: calcula ambos costos, compara y justifica la decisión"],
    },
    "science": {
        "title": "Interpretar una investigación con plantas",
        "stimulus": "Dos grupos de diez plantas iguales recibieron la misma luz y el mismo suelo. El grupo A recibió 50 ml de agua diarios; el B, 100 ml. Tras 14 días, la altura media fue 12 cm en A y 15 cm en B.",
        "questions": [
            {"prompt": "¿Cuál fue la variable modificada?", "options": ["Tipo de planta", "Cantidad de agua", "Duración", "Tipo de suelo"], "answer": 1},
            {"prompt": "¿Qué conclusión está apoyada directamente?", "options": ["Toda planta crece mejor con más agua", "En estas condiciones, B tuvo mayor altura media", "El suelo causó la diferencia", "100 ml es siempre la cantidad óptima"], "answer": 1},
        ],
        "open_prompt": "Propón una modificación que permita investigar si el efecto se mantiene con otra cantidad de agua.",
        "open_rubric": ["0: no propone comparación", "1: propone otra cantidad sin controlar variables", "2: agrega un grupo comparable y mantiene constantes las demás condiciones"],
    },
    "civic": {
        "title": "Contrastar fuentes sobre una decisión pública",
        "stimulus": "La municipalidad propone transformar un estacionamiento en plaza. Un informe municipal estima 600 usuarios semanales. Una agrupación de comerciantes advierte pérdida de acceso, pero no presenta conteos. Vecinos solicitan conservar espacios para personas con movilidad reducida.",
        "questions": [
            {"prompt": "¿Qué fuente entrega un dato cuantitativo verificable?", "options": ["Informe municipal", "Advertencia sin conteos", "Solicitud vecinal", "Ninguna"], "answer": 0},
            {"prompt": "¿Qué información falta para comparar impactos?", "options": ["El color futuro de la plaza", "Conteos actuales de uso y accesibilidad", "El nombre de la calle", "La edad del alcalde"], "answer": 1},
        ],
        "open_prompt": "Formula una recomendación provisional que considere al menos dos fuentes y declare una limitación.",
        "open_rubric": ["0: opinión sin fuentes", "1: usa una fuente o no declara limitación", "2: integra dos fuentes y explicita qué evidencia falta antes de decidir"],
    },
    "digital": {
        "title": "Verificar información antes de compartir",
        "stimulus": "Un mensaje viral afirma que mañana se suspenden las clases y muestra una imagen con el logotipo del municipio. No incluye enlace ni fecha. Una búsqueda encuentra la web municipal sin ese anuncio y una cuenta social no verificada que repite el mensaje.",
        "questions": [
            {"prompt": "¿Cuál es la primera acción más responsable?", "options": ["Reenviar por precaución", "Confirmar en canales oficiales con fecha y URL", "Confiar en el logotipo", "Preguntar cuántos me gusta tiene"], "answer": 1},
            {"prompt": "¿Qué señal reduce la confiabilidad del mensaje?", "options": ["Menciona al municipio", "No tiene enlace ni fecha", "Usa una imagen", "Habla de clases"], "answer": 1},
        ],
        "open_prompt": "Describe un protocolo breve de verificación antes de compartir el mensaje.",
        "open_rubric": ["0: comparte o descarta sin comprobar", "1: consulta una fuente oficial", "2: verifica fuente, fecha y coincidencia entre al menos dos canales confiables"],
    },
    "writing": {
        "title": "Escribir una recomendación con evidencia",
        "stimulus": "Datos de una campaña escolar: 120 botellas desechables usadas el lunes y 75 el viernes después de instalar bebederos. La medición corresponde a una sola semana.",
        "questions": [
            {"prompt": "¿Qué afirmación es compatible con los datos?", "options": ["Los bebederos siempre reducen el consumo", "El viernes se observaron 45 botellas menos que el lunes", "Toda la escuela cambió sus hábitos", "La campaña fue validada por un estudio anual"], "answer": 1},
            {"prompt": "¿Qué límite debe declararse?", "options": ["Los datos son de una sola semana", "Las botellas son objetos", "El viernes ocurre después del lunes", "Hay dos cantidades"], "answer": 0},
        ],
        "open_prompt": "Escribe una recomendación de dos o tres oraciones que use el dato y declare su límite.",
        "open_rubric": ["0: no usa los datos", "1: usa la diferencia o formula recomendación, pero omite el límite", "2: formula recomendación coherente, usa la diferencia de 45 y reconoce que solo se observó una semana"],
    },
    "reading-foundations": {
        "title": "Reconocer sonidos y relacionarlos con palabras",
        "stimulus": "Actividad oral original: el docente dice lentamente ‘mesa’, ‘mano’, ‘sapo’ y ‘mapa’. Después muestra las palabras escritas con letra grande, sin exigir velocidad.",
        "questions": [
            {"prompt": "¿Qué dos palabras comienzan con el mismo sonido?", "options": ["mesa y mano", "mesa y sapo", "mano y sapo", "sapo y mapa"], "answer": 0},
            {"prompt": "¿Cuál palabra termina con el mismo sonido que ‘copa’?", "options": ["mesa", "mano", "sapo", "mapa"], "answer": 3},
        ],
        "open_prompt": "Elige una palabra nueva que comience con /m/, dilo en voz alta y explica cómo comprobaste el sonido inicial.",
        "open_rubric": ["0: no aporta una palabra o cambia el sonido", "1: aporta una palabra pertinente sin explicar cómo la reconoció", "2: aporta una palabra con /m/ inicial y describe una comprobación oral o articulatoria"],
    },
    "fluency": {
        "title": "Leer en voz alta con precisión, fraseo y sentido",
        "stimulus": "Texto original para lectura oral: ‘Al amanecer, Tomás abrió la ventana. La lluvia había terminado y, sobre el patio, brillaban pequeñas gotas. Tomó su cuaderno, dibujó tres hojas mojadas y escribió una pregunta: ¿por qué algunas gotas caen antes que otras?’",
        "questions": [
            {"prompt": "¿Qué ocurrió antes de que Tomás abriera la ventana?", "options": ["Comenzó la lluvia", "Terminó la lluvia", "Cerró el cuaderno", "Cayeron todas las gotas"], "answer": 1},
            {"prompt": "¿Qué hizo Tomás después de mirar el patio?", "options": ["Dibujó y escribió una pregunta", "Volvió a dormir", "Cerró la ventana", "Secó todas las hojas"], "answer": 0},
        ],
        "open_prompt": "Lee el texto en voz alta. El docente registra por separado precisión, respeto de pausas y expresión que ayude a comprender; luego comenta una fortaleza y un próximo paso.",
        "open_rubric": ["0: todavía no existe una muestra oral suficiente o la lectura requiere apoyo palabra por palabra", "1: la lectura comunica parte del sentido, pero pierde precisión, pausas o continuidad de manera frecuente", "2: la lectura es mayormente precisa, agrupa frases y usa pausas o expresión que sostienen el sentido; no se exige una velocidad única"],
    },
    "formative": {
        "title": "Observar, intervenir y reevaluar",
        "stimulus": "En dos tareas distintas, una estudiante identifica datos explícitos pero invierte causa y consecuencia. Tras una actividad con conectores causales, responde una nueva situación.",
        "questions": [
            {"prompt": "¿Qué se puede afirmar después del primer error?", "options": ["Existe diagnóstico definitivo", "Existe una observación que requiere más evidencia", "La habilidad está dominada", "Debe asignarse un porcentaje"], "answer": 1},
            {"prompt": "¿Qué hace válida la reevaluación pedagógica?", "options": ["Repetir la misma respuesta", "Usar una situación diferente para comprobar transferencia", "Subir la nota automáticamente", "Ocultar los criterios"], "answer": 1},
        ],
        "open_prompt": "Describe qué evidencia permitiría confirmar o rechazar la hipótesis de inversión causal.",
        "open_rubric": ["0: etiqueta a la estudiante", "1: propone otra respuesta sin criterio", "2: propone varias situaciones nuevas, criterio observable y decisión según consistencia"],
    },
}


def _variant(identifier, instrument, name, level, domain, form, oa_codes, journey=None):
    return {
        "id": identifier,
        "instrument": instrument,
        "name": name,
        "level": level,
        "domain": domain,
        "form": form,
        "oa_codes": oa_codes,
        "journey": journey or [],
    }


VARIANTS = [
    _variant("paes-competencia-lectora", "paes", "Competencia Lectora", "Trayectoria escolar hasta el egreso", "Lectura", "reading-secondary", ["LE04 OA 04", "LE06 OA 06", "LE08 OA 09", "LE1M OA 09", "LE2M OA 09"], [("Fundamentos", ["LE04 OA 04"]), ("Consolidación", ["LE06 OA 06"]), ("Razonamiento", ["LE08 OA 09", "LE1M OA 09"]), ("Transferencia", ["LE2M OA 09"])]),
    _variant("paes-m1", "paes", "Competencia Matemática 1 (M1)", "Trayectoria escolar hasta el egreso", "Matemática", "math-secondary", ["MA04 OA 07", "MA06 OA 08", "MA08 OA 08", "MA2M OA 06", "MA2M OA 12"], [("Fundamentos", ["MA04 OA 07"]), ("Consolidación", ["MA06 OA 08"]), ("Modelación", ["MA08 OA 08"]), ("Transferencia", ["MA2M OA 06", "MA2M OA 12"])]),
    _variant("paes-m2", "paes", "Competencia Matemática 2 (M2)", "Trayectoria escolar hasta el egreso", "Matemática avanzada", "math-secondary", ["MA06 OA 08", "MA08 OA 08", "MA1M OA 03", "MA2M OA 12", "FG-MATE-3M-OAC-02", "FG-MATE-3M-OAC-03"], [("Fundamentos", ["MA06 OA 08"]), ("Lenguaje algebraico", ["MA08 OA 08", "MA1M OA 03"]), ("Razonamiento con datos", ["MA2M OA 12"]), ("Profundización", ["FG-MATE-3M-OAC-02", "FG-MATE-3M-OAC-03"])]),
    _variant("paes-ciencias", "paes", "Ciencias", "Trayectoria escolar hasta el egreso", "Ciencias", "science", ["CN04 OA 11", "CN06 OA 08", "CN08 OA 07", "CN08 OA 11", "CN1M OA 05", "CN2M OA 06"], [("Observar y medir", ["CN04 OA 11"]), ("Explicar", ["CN06 OA 08"]), ("Usar evidencia", ["CN08 OA 07", "CN08 OA 11"]), ("Transferir", ["CN1M OA 05", "CN2M OA 06"])]),
    _variant("paes-historia", "paes", "Historia y Ciencias Sociales", "Trayectoria escolar hasta el egreso", "Fuentes y pensamiento crítico", "civic", ["HI04 OA 18", "HI06 OA 25", "HI08 OA 18", "HI1M OA 25", "HI2M OA 15", "FG-LELI-4M-OAC-03"], [("Opinar con evidencia", ["HI04 OA 18"]), ("Evaluar alternativas", ["HI06 OA 25"]), ("Contextualizar", ["HI08 OA 18", "HI1M OA 25"]), ("Contrastar interpretaciones", ["HI2M OA 15", "FG-LELI-4M-OAC-03"])]),
    _variant("simce-4-lectura", "simce", "4° básico · Lectura", "4° básico", "Lectura", "reading-primary", ["LE04 OA 04", "LE04 OA 06"]),
    _variant("simce-4-matematica", "simce", "4° básico · Matemática", "4° básico", "Matemática", "math-primary", ["MA04 OA 07", "MA04 OA 27"]),
    _variant("simce-6-lectura", "simce", "6° básico · Lectura", "6° básico", "Lectura", "reading-primary", ["LE06 OA 06", "LE06 OA 07"]),
    _variant("simce-6-matematica", "simce", "6° básico · Matemática", "6° básico", "Matemática", "math-primary", ["MA06 OA 08", "MA06 OA 24"]),
    _variant("simce-2m-lectura", "simce", "II medio · Lectura", "2° medio", "Lectura", "reading-secondary", ["LE2M OA 09", "LE2M OA 10"]),
    _variant("simce-2m-matematica", "simce", "II medio · Matemática", "2° medio", "Matemática", "math-secondary", ["MA2M OA 06", "MA2M OA 12"]),
    _variant("pisa-lectura", "pisa", "Lectura", "15 años", "Lectura en contexto", "reading-secondary", ["LE2M OA 09", "LE2M OA 10"]),
    _variant("pisa-matematica", "pisa", "Matemática", "15 años", "Modelación contextual", "math-secondary", ["MA2M OA 06", "MA2M OA 12"]),
    _variant("pisa-ciencias", "pisa", "Ciencias", "15 años", "Evidencia científica", "science", ["CN08 OA 07", "CN08 OA 11"]),
    _variant("pisa-mundo-digital", "pisa", "Aprendizaje en el mundo digital", "15 años", "Aprendizaje y verificación digital", "digital", ["TE08 OA 02", "TE08 OA 04"]),
    _variant("timss-4-matematica", "timss", "4° grado · Matemática", "Referencia aproximada: 4° básico", "Conocer, aplicar y razonar", "math-primary", ["MA04 OA 07", "MA04 OA 27"]),
    _variant("timss-4-ciencias", "timss", "4° grado · Ciencias", "Referencia aproximada: 4° básico", "Ciencias", "science", ["CN04 OA 01", "CN04 OA 11"]),
    _variant("timss-8-matematica", "timss", "8° grado · Matemática", "Referencia aproximada: 8° básico", "Conocer, aplicar y razonar", "math-secondary", ["MA08 OA 08", "MA08 OA 16"]),
    _variant("timss-8-ciencias", "timss", "8° grado · Ciencias", "Referencia aproximada: 8° básico", "Ciencias", "science", ["CN08 OA 07", "CN08 OA 11"]),
    _variant("pirls-literario", "pirls", "Experiencia literaria", "Alrededor de 4° básico", "Comprensión literaria", "reading-primary", ["LE04 OA 04", "LE04 OA 05"]),
    _variant("pirls-informativo", "pirls", "Adquirir y usar información", "Alrededor de 4° básico", "Comprensión informativa", "reading-primary", ["LE04 OA 06", "LE04 OA 09"]),
    _variant("dia-diagnostico", "dia", "Periodo de Diagnóstico", "1° básico a IV medio según oferta", "Punto de partida", "formative", ["LE04 OA 04", "MA04 OA 07"]),
    _variant("dia-monitoreo", "dia", "Monitoreo Intermedio", "1° básico a IV medio según oferta", "Progreso durante el año", "formative", ["LE06 OA 07", "MA06 OA 08"]),
    _variant("dia-cierre", "dia", "Evaluación de Cierre", "1° básico a IV medio según oferta", "Progreso al cierre", "formative", ["LE2M OA 09", "MA2M OA 12"]),
    _variant("erce-3-lectura", "erce", "3° básico · Lectura", "3° básico", "Lectura", "reading-primary", ["LE03 OA 04", "LE03 OA 06"]),
    _variant("erce-3-escritura", "erce", "3° básico · Escritura", "3° básico", "Escritura", "writing", ["LE03 OA 14", "LE03 OA 18"]),
    _variant("erce-3-matematica", "erce", "3° básico · Matemática", "3° básico", "Matemática", "math-primary", ["MA03 OA 10", "MA03 OA 23"]),
    _variant("erce-6-lectura", "erce", "6° básico · Lectura", "6° básico", "Lectura", "reading-primary", ["LE06 OA 06", "LE06 OA 07"]),
    _variant("erce-6-escritura", "erce", "6° básico · Escritura", "6° básico", "Escritura", "writing", ["LE06 OA 15", "LE06 OA 18"]),
    _variant("erce-6-matematica", "erce", "6° básico · Matemática", "6° básico", "Matemática", "math-primary", ["MA06 OA 08", "MA06 OA 24"]),
    _variant("erce-6-ciencias", "erce", "6° básico · Ciencias", "6° básico", "Ciencias", "science", ["CN06 OA 01", "CN06 OA 08"]),
    _variant("icils-alfabetizacion", "icils", "Alfabetización computacional e informacional", "8° básico", "Información digital", "digital", ["TE08 OA 02", "TE08 OA 04"]),
    _variant("icils-pensamiento-computacional", "icils", "Pensamiento computacional · referencia", "8° básico", "Resolución digital", "digital", ["TE08 OA 01", "TE08 OA 03"]),
    _variant("iccs-ciudadania", "iccs", "Educación cívica y ciudadanía", "8° básico", "Ciudadanía", "civic", ["HI08 OA 18", "HI08 OA 22"]),
    _variant("impulso-precursores", "impulso-lector", "Precursores de la lectura", "2° básico", "Conciencia fonológica y decodificación", "reading-foundations", ["LE01 OA 03", "LE01 OA 04"]),
    _variant("impulso-comprension", "impulso-lector", "Comprensión de lectura", "2° básico", "Comprensión inicial", "reading-primary", ["LE02 OA 03", "LE02 OA 05"]),
    _variant("impulso-fluidez", "impulso-lector", "Fluidez lectora", "2° básico", "Precisión, fraseo y expresión", "fluency", ["LE01 OA 05", "LE02 OA 02"]),
    _variant("nacional-lectura-2", "estudios-nacionales", "Estudio Nacional de Lectura", "2° básico", "Lectura inicial", "reading-primary", ["LE02 OA 03", "LE02 OA 05"]),
    _variant("nacional-escritura-6", "estudios-nacionales", "Estudio Nacional de Escritura", "6° básico", "Producción escrita", "writing", ["LE06 OA 15", "LE06 OA 18"]),
    _variant("nacional-ciudadania-8", "estudios-nacionales", "Estudio Nacional de Formación Ciudadana", "8° básico", "Ciudadanía", "civic", ["HI08 OA 18", "HI08 OA 22"]),
    _variant("nacional-ingles-media", "estudios-nacionales", "Estudio Nacional de Inglés", "Enseñanza media según ciclo", "Comprensión y comunicación en inglés", "english-secondary", ["FG-INGL-3M-OAC-01", "FG-INGL-3M-OAC-02"]),
    _variant("nacional-competencias-tp", "estudios-nacionales", "Competencias generales técnico-profesionales · referencia", "Enseñanza media técnico-profesional", "Comunicación, datos y decisión", "writing", ["FG-LELI-4M-OAC-05", "FG-MATE-4M-OAC-02"]),
    _variant("interna-diagnostico", "interna", "Diagnóstico inicial", "1° básico a 4° medio", "Observación inicial", "formative", ["LE04 OA 04", "MA04 OA 07"]),
    _variant("interna-intervencion", "interna", "Seguimiento de intervención", "1° básico a 4° medio", "Práctica y retroalimentación", "formative", ["LE06 OA 07", "MA06 OA 08"]),
    _variant("interna-transferencia", "interna", "Reevaluación y transferencia", "1° básico a 4° medio", "Situación nueva", "formative", ["LE2M OA 09", "MA2M OA 12"]),
]


FORM_GUIDANCE = {
    "reading-foundations": {
        "focus": "Reconocer y manipular sonidos del habla, relacionarlos con palabras y explicar una comprobación sin confundir rapidez con aprendizaje.",
        "observe": "Separar conciencia fonológica, conocimiento de letras, decodificación y comprensión; registrar el tipo de apoyo necesario.",
        "intervene": "Volver a actividades orales y visuales breves de la clase enlazada, modelar el sonido objetivo y retirar gradualmente el apoyo.",
        "reassess": "Usar palabras nuevas con la misma relación sonora y pedir una explicación oral o señalamiento accesible.",
    },
    "fluency": {
        "focus": "Leer un texto breve en voz alta con precisión, continuidad, pausas y expresión al servicio de la comprensión.",
        "observe": "Registrar por separado precisión, fraseo, pausas, expresión y comprensión; evitar fijar una velocidad universal como único criterio.",
        "intervene": "Modelar una frase, realizar lectura eco o repetida con propósito y volver al significado del texto, sin exposición pública obligatoria.",
        "reassess": "Usar un texto nuevo de dificultad semejante y comparar precisión, fraseo y comprensión con la primera lectura.",
    },
    "reading-primary": {
        "focus": "Localizar información, relacionar partes del texto, inferir con evidencia y explicar dónde aparece la pista.",
        "observe": "Distinguir si el error proviene de no localizar un dato, confundir una relación o responder sin evidencia textual.",
        "intervene": "Modelar una lectura con subrayado de pregunta, evidencia y conclusión; después retirar el apoyo.",
        "reassess": "Usar otro texto y otra situación, manteniendo el mismo proceso de comprensión.",
    },
    "reading-secondary": {
        "focus": "Identificar afirmación, evaluar evidencia, reconocer límites de una fuente y justificar una conclusión.",
        "observe": "Separar lectura literal, inferencia no sustentada y evaluación de la calidad de la evidencia.",
        "intervene": "Comparar afirmación, dato, procedencia y representatividad en dos textos o fuentes existentes.",
        "reassess": "Presentar una fuente nueva con otra limitación y pedir una conclusión proporcional a la evidencia.",
    },
    "english-secondary": {
        "focus": "Comprender información explícita y propósito en un texto breve en inglés y producir un mensaje funcional comprensible.",
        "observe": "Separar comprensión del contenido, vocabulario, organización del mensaje e inteligibilidad; no penalizar acento ni una forma emergente que conserva el sentido.",
        "intervene": "Volver a la clase enlazada, modelar cómo localizar detalles y usar un marco breve de mensaje antes de escribir de manera independiente.",
        "reassess": "Usar otro aviso auténtico u original y pedir un mensaje para una audiencia y propósito diferentes.",
    },
    "math-primary": {
        "focus": "Comprender la situación, elegir operaciones, representar cantidades, calcular y comprobar.",
        "observe": "Registrar por separado comprensión del problema, estrategia, cálculo e interpretación del resultado.",
        "intervene": "Volver a una clase enlazada y representar con dibujo, tabla u operación antes de automatizar el procedimiento.",
        "reassess": "Cambiar números y contexto, pero conservar la relación matemática que debe reconocerse.",
    },
    "math-secondary": {
        "focus": "Traducir una situación a una representación, modelar, calcular, comparar y justificar la decisión.",
        "observe": "Distinguir un error de modelación de un error algebraico o de interpretación de unidades.",
        "intervene": "Contrastar tabla, gráfico, expresión y lenguaje natural en la clase vinculada.",
        "reassess": "Proponer un problema nuevo que exija elegir el modelo y explicar por qué se ajusta.",
    },
    "science": {
        "focus": "Identificar variables, interpretar datos, construir una conclusión acotada y proponer una investigación controlada.",
        "observe": "Distinguir dato, patrón, explicación y generalización que excede la evidencia.",
        "intervene": "Revisar una clase de indagación enlazada y comparar diseños que cambian una o varias variables.",
        "reassess": "Usar otro fenómeno con tabla de datos y pedir conclusión, límite y siguiente prueba.",
    },
    "civic": {
        "focus": "Contrastar fuentes, reconocer derechos e intereses, evaluar evidencia y justificar una decisión pública provisional.",
        "observe": "Separar conocimiento cívico, uso de fuente y posición personal; no calificar adhesión ideológica.",
        "intervene": "Trabajar un caso de la clase vinculada con matriz de fuente, afirmación, evidencia y limitación.",
        "reassess": "Cambiar el conflicto público y pedir integrar dos fuentes y declarar qué dato falta.",
    },
    "digital": {
        "focus": "Buscar, verificar procedencia y fecha, contrastar fuentes, transformar información y comunicar responsablemente.",
        "observe": "Distinguir dificultad técnica, comprensión del mensaje y evaluación de confiabilidad.",
        "intervene": "Aplicar un protocolo explícito de autoría, fecha, evidencia, propósito y corroboración en la clase vinculada.",
        "reassess": "Usar otro contenido digital con señales distintas de confiabilidad y pedir documentar la verificación.",
    },
    "writing": {
        "focus": "Planificar, organizar, desarrollar ideas, usar evidencia, revisar coherencia y comunicar para una audiencia.",
        "observe": "Analizar el texto por criterios separados; no convertir ortografía en medida total de escritura.",
        "intervene": "Usar la clase enlazada para comparar borrador y revisión con un criterio visible cada vez.",
        "reassess": "Solicitar otro género o contexto que conserve la necesidad de explicar, justificar o sintetizar.",
    },
    "formative": {
        "focus": "Distinguir observación, patrón, hipótesis, intervención, práctica, reevaluación y decisión.",
        "observe": "Exigir más de una evidencia antes de formular una hipótesis y conservar literalmente lo que el estudiante hizo.",
        "intervene": "Seleccionar una de las clases enlazadas según el prerrequisito implicado y registrar el criterio de éxito.",
        "reassess": "Aplicar una situación distinta, comparar evidencia antes/después y confirmar o rechazar la hipótesis.",
    },
}

for _variant_record in VARIANTS:
    _variant_record.update(FORM_GUIDANCE[_variant_record["form"]])
