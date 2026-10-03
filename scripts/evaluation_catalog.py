"""Catálogo pedagógico visible de evaluaciones y miniensayos originales.

Los datos de este módulo alimentan HTML y Markdown. No contienen ítems oficiales ni
tablas de conversión inventadas: los miniensayos calculan únicamente puntos del
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
        "status": "Modelado con correspondencias, tareas y miniensayos originales",
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
        "status": "Modelado con correspondencias, tareas y miniensayos originales",
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
        "status": "Modelado con correspondencias, tareas y miniensayos originales",
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
        "status": "Modelado con correspondencias, tareas y miniensayos originales",
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
        "status": "Modelado con correspondencias, tareas y miniensayos originales",
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
        "status": "Explicado, conectado a OA de referencia y cubierto con miniensayos originales; mapeo de competencias aún parcial",
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
        "status": "Explicado, conectado a OA de referencia y cubierto con miniensayo original; mapeo de competencias aún parcial",
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
        "status": "Explicado, conectado a OA de referencia y cubierto con miniensayo original; mapeo de competencias aún parcial",
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
    "interna": {
        "name": "Evaluación formativa interna del proyecto",
        "short_name": "Interna",
        "category": "Evaluación de aula",
        "population": "Estudiantes de 1° básico a 4° medio en clases y tareas del proyecto.",
        "purpose": "Observar, retroalimentar, intervenir y reevaluar sin convertir automáticamente la evidencia en nota.",
        "status": "Modelada con ciclo de evidencia y miniensayos originales",
        "framework_id": "internal-formative-v1",
        "source_url": "https://github.com/vladimiracunadev-create/chilean-school-learning-path/blob/main/docs/EVALUACION_FORMATIVA.md",
        "documents": [],
    },
}


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


def _variant(identifier, instrument, name, level, domain, form, oa_codes):
    return {
        "id": identifier,
        "instrument": instrument,
        "name": name,
        "level": level,
        "domain": domain,
        "form": form,
        "oa_codes": oa_codes,
    }


VARIANTS = [
    _variant("paes-competencia-lectora", "paes", "Competencia Lectora", "Egreso y 4° medio", "Lectura", "reading-secondary", ["LE1M OA 09", "LE2M OA 09"]),
    _variant("paes-m1", "paes", "Competencia Matemática 1 (M1)", "Egreso y 4° medio", "Matemática", "math-secondary", ["MA2M OA 06", "MA2M OA 12"]),
    _variant("paes-m2", "paes", "Competencia Matemática 2 (M2)", "Egreso y 4° medio", "Matemática avanzada", "math-secondary", ["FG-MATE-3M-OAC-02", "FG-MATE-3M-OAC-03"]),
    _variant("paes-ciencias", "paes", "Ciencias", "Egreso y 4° medio", "Ciencias", "science", ["CN08 OA 07", "CN08 OA 11"]),
    _variant("paes-historia", "paes", "Historia y Ciencias Sociales", "Egreso y 4° medio", "Fuentes y pensamiento crítico", "civic", ["HI08 OA 18", "FG-LELI-4M-OAC-03"]),
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
    _variant("interna-diagnostico", "interna", "Diagnóstico inicial", "1° básico a 4° medio", "Observación inicial", "formative", ["LE04 OA 04", "MA04 OA 07"]),
    _variant("interna-intervencion", "interna", "Seguimiento de intervención", "1° básico a 4° medio", "Práctica y retroalimentación", "formative", ["LE06 OA 07", "MA06 OA 08"]),
    _variant("interna-transferencia", "interna", "Reevaluación y transferencia", "1° básico a 4° medio", "Situación nueva", "formative", ["LE2M OA 09", "MA2M OA 12"]),
]


PROMPT_STATUS = [
    ("Auditoría previa", "Cumplido", "docs/COMPETENCY_GAP_REPORT.md", "La línea base histórica se conserva sin reescribirla."),
    ("Taxonomía transversal", "Entrega inicial", "docs/GUIA_DOCENTE_COMPETENCIAS.md", "86 habilidades en 7 dominios; falta mapear exhaustivamente los 2.823 OA."),
    ("Mapa longitudinal y grafo", "Entrega demostrativa", "docs/COMPETENCY_SYSTEM.md", "Cinco progresiones y enlaces verificables a OA; no es cobertura total."),
    ("Marcos de evaluación", "Ampliado", "docs/EVALUACIONES_COMPLEMENTARIAS.md", "PAES, SIMCE, DIA, PISA, TIMSS, PIRLS, ERCE, ICILS, ICCS, ECES e interna explicados por separado."),
    ("Ensayos de ejemplo", "Ampliado", "docs/ENSAYOS_EJEMPLO.md", f"{len(VARIANTS)} variantes con miniensayo original, clave, rúbrica y cálculo de puntos del proyecto."),
    ("Banco de tareas", "Entrega inicial", "docs/BANCO_TAREAS.md", "Seis tareas completas; falta ampliación disciplinar y pilotaje."),
    ("Distractores inteligentes", "Parcial", "docs/BANCO_TAREAS.md", "Disponibles cuando existe justificación; una respuesta nunca produce diagnóstico automático."),
    ("Evidencia y diagnóstico", "Prototipo determinista", "docs/EVIDENCE_CYCLE.md", "Distingue observación, patrón, hipótesis, intervención, reevaluación y decisión."),
    ("Remediación y reevaluación", "Conectado", "docs/COMPETENCY_SYSTEM.md", "Las referencias vuelven a clases existentes antes de crear contenido nuevo."),
    ("Adaptación", "Arquitectura preparada", "docs/COMPETENCY_SYSTEM.md", "Reglas descritas; no existe aún una plataforma adaptativa con estudiantes reales."),
    ("Psicometría", "Solo resguardos", "docs/COMPETENCY_SYSTEM.md", "No hay IRT, baremos, validez ni conversiones oficiales simuladas."),
    ("Tutor adaptativo", "Concepto revisado", "docs/COMPETENCY_GAP_REPORT.md", "No se copió la arquitectura externa ni se incorporó LLM al núcleo."),
    ("IA opcional", "Política definida", "docs/COMPETENCY_SYSTEM.md", "Sin IA en el cálculo de evidencia; cualquier uso futuro requiere trazabilidad y revisión."),
    ("Vistas estudiante y docente", "Demostración sintética", "docs/GUIA_DOCENTE_COMPETENCIAS.md", "Sin datos personales ni porcentajes ficticios."),
    ("Interdisciplinariedad", "Implementada en el esquema", "docs/BANCO_TAREAS.md", "Una tarea puede activar lectura, matemática, ciencias y datos sin duplicar competencias."),
]
