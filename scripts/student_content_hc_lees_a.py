"""Lectura y escritura especializadas (electivo 3.º y 4.º medio HC): OAC-01 (producir textos académicos, clases 1 a 5) y OAC-02 (producción colaborativa, clases 1 a 4)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno (o un procesador de texto, si lo tienes). Todos los textos, fichas, datos y fuentes de los ejercicios están escritos en el enunciado y son originales y de ejemplo: no necesitas internet ni libros. "
             "En la actividad abierta trabajas con los insumos que la propia actividad entrega. Si ocupas un computador o un celular, no compartas datos personales ni subas textos ajenos sin permiso.")
build = make_build(MATERIALS)

O1 = "LL-LEES-3y4-OAC-01"
O2 = "LL-LEES-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (situaciones de ejemplo). P: una estudiante debe contar a las familias del barrio, sin términos técnicos, qué hace una estación que mide la calidad del agua. "
     "Q: un equipo debe informar qué midió en un estudio propio, cómo lo midió, qué obtuvo y qué concluye. "
     "R: un estudiante debe sostener una postura propia sobre si conviene limitar el uso del celular en clases, apoyándose en fuentes. "
     "S: un curso debe valorar, con criterios, un estudio ajeno, indicando sus aciertos y sus límites.")
build(
    O1, 1, F,
    use="Aprenderé a elegir el género discursivo académico según el propósito y la audiencia: informe, ensayo, reseña crítica, resumen y artículo de divulgación. Sirve para decidir cómo escribir antes de empezar.",
    prior=["Sé que los textos se escriben para algo y para alguien.", "Conozco la estructura básica de un texto argumentativo.", "Sé distinguir un hecho de una opinión."],
    explain=[
        "Un género discursivo académico es un tipo de texto con un propósito, una audiencia y una forma de organizarse que una comunidad reconoce. El propósito es lo que quien escribe quiere lograr: informar, explicar, convencer o evaluar. La audiencia es quien leerá. Estas dos preguntas, para qué y para quién, deciden el género antes que el tema: el mismo tema se puede tratar en varios géneros.",
        "Cinco géneros frecuentes: el resumen condensa un texto ajeno sin agregar opinión; la reseña crítica describe y evalúa una obra o un estudio con criterios; el informe de investigación presenta un estudio propio con problema, método, resultados y conclusión; el ensayo defiende una tesis personal con argumentos y fuentes; el artículo de divulgación explica un tema especializado a un público general, con lenguaje claro y ejemplos.",
        "Cada género trae convenciones: apartados, tipo de lenguaje y grado de precisión. Un informe usa términos exactos y rotula sus partes; una divulgación explica los términos y usa ejemplos cotidianos. Elegir mal el género hace que el texto no cumpla su propósito, aunque esté bien escrito: una reseña que solo cuenta de qué trata una obra, sin evaluarla, se queda en un resumen.",
    ],
    vocab=[("género discursivo", "tipo de texto con propósito, audiencia y forma reconocidos"), ("propósito", "lo que quien escribe quiere lograr con el texto"), ("audiencia", "personas a quienes se dirige el texto"), ("convención", "modo de escribir que la comunidad acepta para ese género"), ("tesis", "postura que el texto defiende con argumentos")],
    worked=[
        ("Elegir el género de una situación", "Un grupo debe mostrar a su curso qué hizo y qué resultó de una encuesta propia sobre horarios de estudio (datos de ejemplo). ¿Qué género conviene?",
         ["Propósito: informar un estudio propio, con método y resultados.", "Audiencia: el curso, que necesita datos precisos.", "El género que presenta problema, método, resultados y conclusión es el informe de investigación."],
         "Informe de investigación"),
        ("Mismo tema, dos géneros", "El tema es la energía solar en los techos de un liceo (de ejemplo). Una versión es para el diario mural; otra, para el centro de estudios. ¿Cómo cambian?",
         ["Diario mural: audiencia general, así que se usa un artículo de divulgación con términos explicados y ejemplos.", "Centro de estudios: audiencia especialista, así que se usa un informe con términos exactos y partes rotuladas."],
         "Divulgación para el mural e informe para el centro de estudios"),
    ],
    mistakes=[("Elegir el género por el tema: «es sobre ciencias, entonces escribo un informe».", "El tema no decide el género; lo deciden el propósito y la audiencia.", "Pregúntate para qué escribes y para quién, y recién después escoge el género."),
              ("Entregar como reseña crítica un texto que solo cuenta de qué trata la obra.", "Falta la evaluación con criterios, que es el propósito de la reseña.", "Agrega al menos un criterio y un juicio fundamentado con evidencia de la obra.")],
    T=[
        ("abc", "{F} ¿Qué género conviene en la situación P?", "Artículo de divulgación", "Informe de investigación", "Ensayo", "P pide explicar a un público general sin términos técnicos, que es el propósito de la divulgación."),
        ("abc", "{F} ¿Qué género conviene en la situación Q?", "Informe de investigación", "Reseña crítica", "Artículo de divulgación", "Q cuenta un estudio propio con método, resultados y conclusión, que es lo que organiza un informe."),
        ("ab", "En Lengua: ¿qué es el propósito de un texto académico?", "Lo que quien escribe quiere lograr con su texto en la audiencia", "El tema del que trata el texto", "El propósito es el para qué se escribe; el tema es el de qué se escribe."),
        ("abc", "{F} ¿Qué género conviene en la situación R?", "Ensayo", "Resumen", "Informe de investigación", "R pide defender una postura propia con fuentes, que es la tesis argumentada de un ensayo."),
        ("abc", "{F} ¿Qué género conviene en la situación S?", "Reseña crítica", "Resumen", "Informe de investigación", "S pide valorar un estudio ajeno con criterios; el resumen no evalúa y el informe presenta un estudio propio."),
        ("ab", "Una compañera entrega como reseña crítica un texto que solo cuenta de qué trata el estudio, sin decir sus aciertos ni sus límites. ¿Qué le falta?", "Una evaluación fundamentada con criterios", "Un título más extenso", "La reseña existe para valorar; sin juicio y criterios queda en resumen."),
        ("abc", "Un equipo adaptará los resultados de un estudio sobre el agua de la comunidad para el consejo vecinal, que no es especialista. ¿Qué cambio es adecuado?", "Explicar los términos técnicos y usar ejemplos cotidianos", "Mantener todos los términos técnicos sin explicarlos", "Eliminar las cifras para que no se noten los datos", "Una audiencia general necesita lenguaje claro; quitar las cifras o dejar tecnicismos sin explicar le impide entender."),
        ("ab", "Dos estudiantes discuten: Luis dice que el género se elige por el tema; Marta, que se elige por propósito y audiencia. ¿Quién tiene razón según esta clase?", "Marta, porque un mismo tema puede escribirse en varios géneros", "Luis, porque cada tema tiene un único género posible", "El mismo tema admite informe, ensayo o divulgación según para qué y para quién se escribe."),
        ("abc", "Un texto tiene apartados rotulados «Problema», «Método», «Resultados» y «Conclusión», y usa términos exactos. ¿Qué convención de género muestra?", "La de un informe de investigación", "La de un ensayo", "La de una reseña crítica", "Esa organización rotulada de un estudio propio es la forma convencional del informe."),
        ("abc", "{F} Un texto sobre la situación R tiene este remate: «Por eso, limitar el celular en clases es conveniente, porque mejora la atención, según las fuentes citadas». ¿Qué rasgo del género muestra?", "Una tesis sostenida con argumentos y fuentes", "El resultado de un método propio", "La explicación de términos para un público general", "El remate afirma una postura y la apoya con razones y fuentes, rasgo propio del ensayo."),
        ("abc", "{F} Se pide un solo texto que cuente qué hizo el equipo de la situación Q y, además, defienda una postura con esos datos. ¿Qué decisión es más razonable?", "Escribir un informe y, en su conclusión, sostener con los datos una postura acotada", "Escribir un resumen para no tomar ninguna postura", "Escribir una divulgación sin método ni datos", "El informe ya contiene los datos y el método; en su conclusión puede defender, con cautela, una postura que esos datos permitan."),
        ("abc", "{F} Un grupo quiere reunir en un solo escrito la situación P y la S: explicar a las familias y, a la vez, valorar un estudio ajeno. ¿Qué es lo más razonable?", "Escribir dos textos de géneros distintos, cada uno con su propósito y su audiencia", "Escribir un único informe que mezcle todo", "Escribir un resumen para ambas audiencias", "Propósitos y audiencias distintos piden géneros distintos; mezclarlos confunde a quien lee."),
        ("{F} Cada situación se resuelve con un género distinto. Los géneros disponibles son resumen, reseña crítica, informe, ensayo y divulgación. ¿Cuál género queda sin usar?", "Resumen", "P usa divulgación, Q informe, R ensayo y S reseña crítica; solo sobra el resumen."),
    ],
    ctx=("abc", "El centro de estudiantes anotó cuántos kilos de papel reciclaron por mes (datos de ejemplo) y debe informar a todo el liceo con un texto breve y claro. ¿Qué género y qué lenguaje conviene?", "Un artículo de divulgación con lenguaje claro y las cifras explicadas", "Un informe de investigación con términos técnicos sin explicar", "Una reseña crítica de otro estudio sobre reciclaje", "La audiencia es todo el liceo, no especialistas; la divulgación explica las cifras con lenguaje accesible."),
    sc=[
        ("En Lengua: ¿qué dos preguntas deciden el género de un texto?", "Para qué escribo (propósito) y para quién escribo (audiencia)", "El género se elige según el propósito y la audiencia, no según el tema."),
        ("¿Qué distingue a una reseña crítica de un resumen?", "La reseña evalúa con criterios; el resumen solo condensa", "El resumen no agrega juicio; la reseña sí lo hace con fundamento."),
        ("¿Qué género defiende una tesis personal con argumentos y fuentes?", "El ensayo", "La tesis argumentada con fuentes es el rasgo central del ensayo."),
    ],
    op=("Elige uno de estos temas: A) el uso del celular en clases, B) los horarios de estudio de tu curso, C) el reciclaje en tu liceo. Escribe un cuadro con tres géneros distintos (por ejemplo, divulgación, informe y ensayo) para el mismo tema: en cada uno anota el propósito, la audiencia y dos rasgos de lenguaje.",
        "Tema B. Divulgación: propósito, explicar a las familias cómo estudia el curso; audiencia general; lenguaje claro y ejemplos cotidianos. Informe: propósito, presentar una encuesta propia; audiencia, el consejo de profesores; términos exactos y partes rotuladas. Ensayo: propósito, defender que conviene fijar un horario de estudio; audiencia, el curso; tesis con argumentos.",
        ["tres géneros distintos con propósito y audiencia diferentes", "dos rasgos de lenguaje por género", "los rasgos coinciden con el propósito y la audiencia"],
        ["cuadro de tres filas con propósito, audiencia y rasgos"],
        ["repetir el mismo propósito en los tres géneros", "describir solo el tema y no el para qué", "rasgos que no corresponden al género"],
        "Pregunta: «¿para quién es este texto y qué quieres que haga o entienda?». Si no puede responder, el propósito aún no está claro."),
    reinforce="Escribe tres situaciones breves de tu liceo y asigna a cada una el género más adecuado (resumen, reseña, informe, ensayo o divulgación), con una razón de una línea.",
    extend="Explica por qué un informe y un ensayo sobre el mismo tema pueden usar los mismos datos pero cumplir propósitos distintos.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo). Tema amplio: «el consumo de electricidad en un curso». "
     "Pregunta 1: «¿Qué es la electricidad?». "
     "Pregunta 2: «¿Cuánto bajó el consumo semanal de electricidad de un curso de 35 estudiantes durante las cuatro semanas de una campaña de apagar luces en recreos?». "
     "Pregunta 3: «¿Es bueno ahorrar?». "
     "Registro del curso: semana 1, 120 kWh; semana 4, 96 kWh (datos de ejemplo).")
build(
    O1, 2, F,
    use="Aprenderé a pasar de un tema amplio a una pregunta de investigación acotada y a formular una tesis. Sirve para que el texto tenga un problema claro que resolver.",
    prior=["Sé distinguir el propósito y la audiencia de un texto.", "Sé calcular un porcentaje simple.", "Sé que una opinión necesita razones."],
    explain=[
        "Un tema es un campo amplio, como «la electricidad en un curso». Un tema no basta para escribir: hace falta un problema o pregunta de investigación, que sea acotada y se pueda responder con evidencia. Para acotar se agregan límites de población (quiénes), de lugar, de tiempo y de aspecto (qué se mira). «¿Qué es la electricidad?» se responde con una definición; «¿Es bueno ahorrar?» es vaga y valorativa; ninguna guía una investigación.",
        "Una buena pregunta de investigación pide algo que no se resuelve con una definición ni con un sí o un no sin pruebas. Suele llevar un verbo de análisis como cuánto, cómo, por qué o en qué medida, y límites claros. Si no se puede saber qué evidencia la respondería, la pregunta aún está demasiado amplia.",
        "La tesis es la respuesta provisional y sostenible que el autor propone: una afirmación que se puede discutir y que se apoya con evidencia. Ejemplo: «La campaña redujo el consumo del curso, porque la baja se mantuvo las cuatro semanas». Una tesis no es un tema («este texto trata de electricidad») ni un hecho evidente («la electricidad es útil»): debe poder ser defendida o refutada con datos.",
    ],
    vocab=[("tema", "campo amplio del que se habla"), ("pregunta de investigación", "pregunta acotada que se responde con evidencia"), ("delimitar", "poner límites de población, lugar, tiempo y aspecto"), ("tesis", "afirmación discutible que el texto sostiene con evidencia"), ("evidencia", "dato o prueba que apoya una afirmación")],
    worked=[
        ("Acotar un tema", "Tema: «las redes sociales y los estudiantes». Delimita con población, tiempo y aspecto.",
         ["Población: estudiantes de un tercero medio.", "Tiempo: durante una semana de ejemplo.", "Aspecto: cuántas horas diarias usan redes sociales para fines de estudio."],
         "¿Cuántas horas diarias usó un tercero medio las redes sociales para estudiar durante una semana?"),
        ("De la pregunta a la tesis", "Pregunta: «¿Cómo influye el sueño en la atención de un curso durante una semana de ejemplo?». Formula una tesis posible.",
         ["Se toma una posición que los datos puedan apoyar o refutar.", "La tesis se escribe como afirmación con una razón."],
         "Tesis: dormir menos de siete horas se asocia con menor atención en el curso, según los registros de la semana."),
    ],
    mistakes=[("Usar como pregunta de investigación una de definición: «¿Qué es el reciclaje?».", "Se responde con un diccionario y no exige evidencia propia.", "Acótala con población, lugar y tiempo: «¿Cuántos kilos de papel recicló el liceo en un mes?»."),
              ("Escribir como tesis «Este texto trata del reciclaje».", "Eso anuncia el tema; no afirma nada que se pueda discutir.", "Escribe una afirmación defendible: «El reciclaje de papel creció porque se ubicaron contenedores en cada piso».")],
    T=[
        ("abc", "{F} ¿Cuál de las preguntas está más acotada?", "La pregunta 2", "La pregunta 1", "La pregunta 3", "La pregunta 2 fija población, tiempo y aspecto; las otras son una definición y una pregunta vaga."),
        ("ab", "En Lengua: ¿qué es una tesis?", "Una afirmación discutible que el texto sostiene con evidencia", "Un tema general anunciado al comienzo", "La tesis se puede defender o refutar; anunciar el tema no afirma nada."),
        ("abc", "{F} ¿Por qué la pregunta 1 no sirve para guiar una investigación?", "Se responde con una definición y no exige evidencia propia", "Porque tiene demasiadas palabras", "Porque menciona a un curso", "Una pregunta de definición se resuelve en un diccionario; no necesita datos ni análisis."),
        ("abc", "El tema «el deporte en el liceo» se acota agregando:", "Población y tiempo: «en los primeros medios durante un semestre»", "Más temas: «el deporte, la música y las fiestas»", "Una frase más larga sin límites", "Delimitar es poner límites; agregar más temas lo ensancha."),
        ("abc", "¿Cuál de estas es una tesis?", "«El consumo del curso bajó durante la campaña, porque entre la semana 1 y la 4 hubo 24 kWh menos»", "«Este informe trata de la campaña»", "«La electricidad es útil»", "Solo la primera afirma algo discutible y apoyado en evidencia; las otras anuncian el tema o dicen algo evidente."),
        ("ab", "{F} Con el registro dado, ¿qué verbo de análisis tiene la pregunta 2?", "«Cuánto bajó», porque pide medir un cambio", "«Durante», porque marca el tiempo de la campaña", "«Cuánto bajó» pide cantidad y comparación, lo que permite buscar datos."),
        ("=", "{F} ¿En qué porcentaje bajó el consumo semanal entre la semana 1 y la semana 4? Usa (120 − 96) dividido por 120 y multiplicado por 100.", "(120-96)/120*100", "La baja es 24 kWh sobre una base de 120 kWh, que equivale a la quinta parte.", " %"),
        ("abc", "{F} Con esos datos, ¿qué tesis queda mejor apoyada?", "La campaña se asocia con una baja del consumo semanal del curso", "La campaña cambió la vida de todo el liceo", "El consumo de todos los cursos del país bajó", "Los datos son de un solo curso; las otras tesis afirman más de lo que el registro permite."),
        ("abc", "Un estudiante propone como tesis: «El celular es bueno». ¿Qué problema tiene?", "Es vaga y no indica qué evidencia la apoyaría", "Es demasiado corta para ser tesis", "No usa la palabra investigación", "Una tesis útil indica qué se afirma y con qué evidencia podría sostenerse."),
        ("ab", "Una compañera cambia su pregunta «¿Qué es el estrés?» por «¿Cuántas horas de sueño reportó un primero medio en una semana de exámenes?». ¿Qué mejoró?", "La acotó con población, tiempo y aspecto medible", "La hizo más larga sin cambiar lo que pide", "La segunda se puede responder con datos; la primera se responde con una definición."),
        ("abc", "{F} Se agrega la pregunta 4: «¿Cuánto bajó el consumo semanal de electricidad en todos los colegios del país en diez años?». ¿Qué defecto tiene frente a la pregunta 2?", "Es demasiado amplia para un estudio escolar con datos propios", "Es demasiado corta", "No usa la palabra cuánto", "Abarca todo el país y diez años; un curso no tiene datos para responderla."),
        ("ab", "Un estudiante dice: «Si mi tesis es evidente para todos, es mejor, porque nadie la discutirá». ¿Es correcto?", "No: una tesis debe poder discutirse y sostenerse con evidencia", "Sí: una tesis evidente evita errores", "Si nadie puede discutirla, no hay nada que defender ni evidencia que aportar."),
        ("abc", "{F} Un compañero propone como tesis solo «El consumo bajó 20 %». ¿Qué le falta para ser una tesis sostenida?", "Una razón o interpretación que explique el dato, además del porcentaje", "Más decimales en el porcentaje", "Una pregunta en lugar de la afirmación", "El porcentaje es un dato; la tesis debe interpretarlo y relacionarlo con una razón."),
    ],
    ctx=("abc", "Un grupo quiere investigar «el sueño de los estudiantes». ¿Cuál es una pregunta acotada y respondible con datos del propio liceo?", "¿Cuántas horas durmieron en promedio los estudiantes de un segundo medio durante una semana de ejemplo?", "¿Qué es dormir?", "¿Es importante dormir?", "Solo la primera fija población, tiempo y aspecto medible; las otras no guían una recolección de datos."),
    sc=[
        ("En Lengua: ¿qué cuatro límites ayudan a acotar un tema?", "Población, lugar, tiempo y aspecto", "Esos límites reducen un tema amplio a un problema investigable."),
        ("¿Una pregunta de definición sirve como pregunta de investigación?", "No: se responde con un diccionario, sin evidencia propia", "Una pregunta de investigación debe exigir datos o análisis."),
        ("¿Qué debe poder hacerse con una tesis?", "Discutirse y sostenerse con evidencia", "Una tesis útil se puede defender o refutar con datos."),
    ],
    op=("Elige un tema: A) los recreos del liceo, B) el uso de bicicletas para llegar al colegio, C) los tiempos de traslado a clases. Escribe: (1) tres límites que lo acoten, (2) una pregunta de investigación y (3) una tesis provisional con una razón.",
        "Tema B. Límites: estudiantes de tercero medio, durante una semana de ejemplo, cantidad de días que llegan en bicicleta. Pregunta: ¿cuántos días de la semana llegaron en bicicleta los estudiantes de un tercero medio? Tesis: la mayoría usó la bicicleta al menos tres días porque el liceo tiene estacionamiento para ellas.",
        ["tres límites distintos de población, tiempo, lugar o aspecto", "pregunta acotada, respondible con datos", "tesis que afirma algo discutible con una razón"],
        ["tres líneas: límites, pregunta y tesis"],
        ["pregunta de definición", "tesis que solo anuncia el tema", "tesis sin razón"],
        "Pregunta: «¿qué dato te permitiría saber si tu tesis es falsa?». Si no hay ninguno, la tesis es demasiado vaga."),
    reinforce="Acota el tema «los celulares en el liceo» con población, tiempo y aspecto, y escribe una pregunta y una tesis.",
    extend="Explica por qué una tesis muy general («todos los jóvenes») puede ser más difícil de sostener que una acotada.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (fuentes de ejemplo). Fuente A (informe escolar): «En un curso de 30 estudiantes, 18 declararon dormir menos de siete horas en días de prueba y 9 dijeron dormir siete horas o más; 3 no respondieron». "
     "Fuente B (nota de divulgación): «Dormir poco se asocia con más errores de atención, aunque la relación depende de la edad y de otros hábitos». "
     "Dato C: en el mismo curso, 12 estudiantes tuvieron una nota bajo 5,0 en la prueba de ejemplo.")
build(
    O1, 3, F,
    use="Aprenderé a gestionar información de varias fuentes: parafrasear, citar, integrar y atribuir ideas ajenas sin copiarlas. Sirve para demostrar dominio de un tema con evidencia propia y bien atribuida.",
    prior=["Sé qué es una tesis y qué es evidencia.", "Sé comparar dos textos.", "Sé calcular restas y porcentajes simples."],
    explain=[
        "Gestionar información es reunir datos de distintas fuentes, decidir cuáles sirven para la tesis y usarlos con orden. En un texto académico las ideas de otros se usan de tres formas: la cita textual, entre comillas y con la fuente; la paráfrasis, que reescribe la idea con palabras propias sin cambiar su sentido, también con la fuente; y el resumen, que condensa varias ideas. En todos los casos hay que decir de dónde viene la idea.",
        "Integrar no es pegar. Un buen párrafo presenta una afirmación propia, agrega la evidencia de una o más fuentes, explica por qué esa evidencia la apoya y, si hay diferencias entre fuentes, las señala. Cuando dos fuentes dicen cosas distintas, se compara qué midió cada una y cuál tiene más respaldo. Una fuente de divulgación puede orientar, pero un informe con datos propios pesa más como evidencia.",
        "Copiar un texto ajeno sin comillas ni fuente es plagio, aun cuando se cambie una palabra. También lo es atribuir a una fuente algo que no dice. Para evitarlo se anota la fuente al tomar cada dato, se separa lo que dice la fuente de lo que opina quien escribe, y se verifica que la paráfrasis conserve el sentido y los datos.",
    ],
    vocab=[("cita textual", "palabras exactas de la fuente, entre comillas y con atribución"), ("paráfrasis", "idea ajena dicha con palabras propias, con la fuente"), ("integrar", "unir evidencia de varias fuentes dentro de un argumento propio"), ("atribuir", "indicar de quién o de dónde viene una idea"), ("plagio", "presentar como propias las palabras o ideas de otros")],
    worked=[
        ("Parafrasear sin cambiar el sentido", "Frase de una fuente de ejemplo: «El 60 % de los estudiantes encuestados prefiere estudiar por la tarde». Escribe una paráfrasis atribuida.",
         ["Se conserva el dato exacto: 60 %.", "Se cambian las palabras y se agrega la fuente: según la encuesta, seis de cada diez prefieren la tarde para estudiar."],
         "Según la encuesta de ejemplo, el 60 % de los estudiantes prefiere estudiar por la tarde."),
        ("Integrar dos fuentes", "Fuente 1: «Se registraron 20 horas de estudio semanales». Fuente 2: «Se registraron 14 horas de estudio semanales», pero en otra población. ¿Cómo se integran?",
         ["No se mezclan sin más: se indica que cada fuente midió una población distinta.", "Se compara con cautela y se explica la diferencia posible."],
         "Se presentan ambos datos, se atribuye cada uno y se aclara que las poblaciones son distintas."),
    ],
    mistakes=[("Copiar una oración de la fuente cambiando una palabra y sin atribución.", "Sigue siendo plagio: no hay comillas ni reescritura real ni fuente.", "Usa comillas y fuente si es cita, o reescribe la idea con tus palabras y cita la fuente si es paráfrasis."),
              ("Parafrasear cambiando el dato: «casi todos» en vez de «18 de 30».", "La paráfrasis debe conservar el sentido y la cifra.", "Mantén los datos exactos y cambia solo la redacción.")],
    T=[
        ("abc", "{F} Según la fuente A, ¿cuántos estudiantes declararon dormir menos de siete horas en días de prueba?", "18", "9", "3", "La fuente A dice 18; 9 duermen siete horas o más y 3 no respondieron."),
        ("ab", "En Lengua: ¿qué es una paráfrasis?", "Decir una idea ajena con palabras propias y atribuir la fuente", "Copiar la oración de la fuente entre comillas", "Copiar entre comillas es una cita textual; la paráfrasis reescribe la idea."),
        ("abc", "{F} ¿Cuál es una paráfrasis fiel de la fuente A?", "Según el informe escolar, 18 de 30 estudiantes dijeron dormir menos de siete horas en días de prueba", "Casi todos los estudiantes duermen poco en días de prueba", "El informe escolar demuestra que dormir poco baja las notas", "La primera conserva el dato y la fuente; las otras exageran o agregan una causa que la fuente no afirma."),
        ("=", "{F} En la fuente A, ¿qué porcentaje de los 30 estudiantes declaró dormir menos de siete horas en días de prueba? Divide 18 entre 30 y multiplica por 100.", "18/30*100", "18 de 30 equivale a 60 de cada 100 estudiantes.", " %"),
        ("ab", "{F} La fuente A dice «18 de 30». Alguien escribe «casi todos». ¿Qué problema hay?", "Cambia el dato exacto por una exageración", "Usa palabras propias, lo que está prohibido", "18 de 30 es el 60 %; «casi todos» distorsiona lo que dice la fuente."),
        ("abc", "{F} ¿Cuál es una cita textual correcta de la fuente B?", "Según la nota, «Dormir poco se asocia con más errores de atención»", "Según la nota, dormir poco causa siempre errores", "Dormir poco se asocia con más errores de atención, según yo", "La cita textual lleva comillas, palabras exactas y fuente; las otras no cumplen alguna de las tres cosas."),
        ("abc", "{F} Una estudiante escribe: «Está demostrado que dormir poco baja las notas». ¿Qué le falta a ese uso de las fuentes?", "Decir que los datos muestran asociación, no causa, y atribuirlos", "Más adjetivos para dar fuerza", "Mencionar solo la fuente B", "Las fuentes muestran relaciones, no demuestran causa, y toda afirmación debe estar atribuida."),
        ("abc", "{F} ¿Qué fuente pesa más como evidencia para un informe sobre un curso concreto?", "La fuente A, porque mide al curso con datos propios", "La fuente B, porque es de divulgación y está bien escrita", "Las dos pesan igual, porque ambas hablan del sueño", "A entrega datos del propio curso; B orienta en general, pero no mide a ese grupo."),
        ("ab", "Una estudiante pega en su ensayo un párrafo de una nota de divulgación y solo cambia dos palabras, sin indicar la fuente. ¿Qué es esto?", "Plagio: falta reescritura real y atribución", "Paráfrasis válida: cambió palabras", "Cambiar dos palabras no basta; hay que reescribir la idea y citar la fuente."),
        ("abc", "{F} ¿Qué enunciado integra bien las fuentes A y B?", "El informe escolar muestra que 18 de 30 duermen poco en días de prueba, y la nota de divulgación señala que dormir poco se asocia con más errores de atención", "Dormir poco causa errores de atención, como lo mostraron A y B", "Los estudiantes no duermen bien y por eso fallan", "El primero atribuye cada dato a su fuente y los une con una conexión que ambas permiten; los otros afirman causas o no atribuyen."),
        ("abc", "{F} El dato C dice que 12 estudiantes tuvieron nota bajo 5,0. Un compañero escribe: «Los 18 que duermen poco son los 12 con nota baja». ¿Qué problema tiene?", "Mezcla datos que no se pueden igualar: 12 no es 18 ni la fuente cruza ambos datos", "Está bien, porque ambos datos son del mismo curso", "Debe cambiar 12 por 18 para que calce", "No hay dato que cruce sueño y notas: 18 y 12 son conteos distintos y no se pueden dar por el mismo grupo."),
        ("abc", "{F} Un estudiante escribe: «Según el informe escolar, 18 de 30 duermen poco. Además, la nota de divulgación prueba que dormir poco baja las notas». ¿Qué error tiene la segunda parte?", "Dice «prueba» y «baja las notas», cuando la fuente solo habla de una asociación con errores de atención", "Cita demasiadas fuentes", "Usa palabras propias", "La nota de divulgación dice «se asocia con más errores de atención»; no prueba causa ni habla de notas."),
        ("{F} ¿Qué dos datos de la ficha habría que cruzar, por estudiante, para afirmar algo sobre sueño y notas del mismo curso?", "Las horas de sueño en días de prueba y la nota de la prueba de cada estudiante", "Solo cruzando, para cada estudiante, su sueño y su nota se puede sostener una relación; los conteos sueltos no bastan."),
    ],
    ctx=("abc", "Un equipo escribe sobre el uso de bicicletas al liceo. Tiene una encuesta propia (de ejemplo): 14 de 40 llegan en bicicleta. Una nota de divulgación dice que el uso de la bicicleta crece en ciudades con ciclovías. ¿Cómo integra ambas?", "Presenta su dato atribuido a la encuesta, cita la nota para el contexto y aclara que son poblaciones distintas", "Copia la nota completa como si fuera su análisis", "Usa solo la nota porque está mejor escrita", "Integrar es atribuir cada dato, usar la fuente general como contexto y no mezclar poblaciones distintas."),
    sc=[
        ("En Lengua: ¿qué hace falta siempre al usar una idea de otra persona?", "Decir de dónde viene: atribuir la fuente", "Citar o parafrasear sin atribuir es plagio."),
        ("¿Qué diferencia hay entre cita textual y paráfrasis?", "La cita textual conserva las palabras exactas entre comillas; la paráfrasis usa palabras propias", "Ambas llevan fuente, pero solo la cita lleva comillas y las palabras originales."),
        ("¿Qué debe conservar una paráfrasis?", "El sentido y los datos de la fuente", "Cambiar palabras no autoriza a cambiar el sentido ni las cifras."),
    ],
    op=("Lee estas dos fuentes de ejemplo. Fuente 1 (encuesta de un liceo): «De 50 estudiantes, 35 dijeron leer por gusto al menos una vez a la semana». Fuente 2 (nota de divulgación): «Leer con regularidad se asocia con mejor vocabulario». Escribe un párrafo de cuatro a seis líneas con una afirmación propia, la paráfrasis de ambas fuentes atribuidas, una frase de conexión y una cautela sobre lo que no se puede concluir.",
        "Los estudiantes de ese liceo parecen leer con frecuencia. Según la encuesta, 35 de 50 leen por gusto al menos una vez a la semana. La nota de divulgación señala que leer con regularidad se asocia con mejor vocabulario. Esto sugiere un vínculo posible, pero no prueba que la lectura cause el vocabulario ni que el liceo tenga mejor vocabulario.",
        ["afirmación propia clara", "parafrasea y atribuye las dos fuentes sin cambiar los datos", "incluye una cautela sobre asociación y causa"],
        ["párrafo de cuatro a seis líneas con atribución"],
        ["copiar las frases tal cual", "cambiar el dato 35 de 50", "afirmar causa sin cautela"],
        "Pregunta: «¿qué parte es de la fuente y cuál es tuya?». Si no se distingue, falta atribución."),
    reinforce="Parafrasea con atribución: «El 40 % de los alumnos encuestados llega al liceo caminando». Conserva el dato.",
    extend="Explica por qué dos fuentes con cifras distintas no son necesariamente contradictorias.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (tres versiones de ejemplo sobre un pozo). Versión X: «Lo del agua del pozo fue terrible: estaba súper contaminada y era obvio que nadie hacía nada». "
     "Versión Y: «En la muestra del pozo se detectó una concentración de nitratos superior al valor de referencia (dato de ejemplo), lo que sugiere un posible aporte de abonos cercanos; se requiere un muestreo adicional para confirmarlo». "
     "Versión Z: «Al revisar el agua del pozo, el equipo encontró más nitratos de lo recomendado. Los nitratos son sustancias que pueden venir de abonos; falta repetir las mediciones para estar seguros».")
build(
    O1, 4, F,
    use="Aprenderé a reconocer y usar las convenciones de un texto académico: registro formal, términos precisos, impersonalidad y cautela. Sirve para mostrar dominio de un tema y para contrastar versiones de un mismo contenido.",
    prior=["Conozco la diferencia entre lenguaje coloquial y formal.", "Sé qué es una tesis y qué es evidencia.", "Sé distinguir un texto de divulgación de uno académico."],
    explain=[
        "Un texto académico usa un registro formal: evita expresiones coloquiales («súper», «terrible»), exageraciones y juicios sin respaldo («era obvio que nadie hacía nada»). Usa términos precisos del campo, como «concentración de nitratos», que nombran con exactitud lo observado. También entrega datos concretos y los atribuye, en vez de impresiones generales.",
        "Otras convenciones son la impersonalidad y la cautela. La impersonalidad pone el foco en lo observado y no en quien escribe: «se detectó» en lugar de «yo vi». La cautela, o modalización, usa expresiones como «sugiere», «es posible» o «se requiere confirmar» para no afirmar más de lo que la evidencia permite. Un texto cauteloso no es débil: es riguroso.",
        "Cada género ajusta estas convenciones. La divulgación conserva la cautela y los datos, pero explica los términos y usa frases más cortas. Contrastar versiones ayuda a ver qué se gana y qué se pierde: la versión X es expresiva pero no es verificable; la Y es precisa pero exige conocer términos; la Z mantiene la precisión esencial y la hace comprensible para un público general.",
    ],
    vocab=[("registro formal", "modo de escribir sin coloquialismos ni exageraciones"), ("término técnico", "palabra precisa de un campo especializado"), ("impersonalidad", "foco en lo observado y no en quien escribe"), ("cautela", "expresión que no afirma más de lo que la evidencia permite"), ("modalizar", "marcar con grado de certeza lo que se afirma")],
    worked=[
        ("Reconocer rasgos académicos", "Frase: «Se registró un descenso de 12 mm en el nivel del pozo durante la semana (dato de ejemplo)». ¿Qué rasgos tiene?",
         ["«Se registró» es impersonal: no dice «yo medí».", "«12 mm» es un dato concreto y «nivel» es un término preciso."],
         "Impersonalidad, dato concreto y término preciso"),
        ("Reescribir con cautela", "Frase: «Está claro que el abono contamina el pozo». Reescríbela con cautela.",
         ["Se identifica la afirmación demasiado fuerte: «está claro» y «contamina» como causa segura.", "Se modaliza y se pide confirmación."],
         "«Los datos sugieren que el abono podría estar relacionado con la contaminación del pozo; falta confirmarlo»."),
    ],
    mistakes=[("Creer que formal significa llenar el texto de palabras difíciles.", "Un texto formal busca precisión, no complejidad inútil.", "Usa el término técnico cuando nombra algo con exactitud y explícalo si el público no lo conoce."),
              ("Eliminar toda cautela para que el texto «suene seguro».", "Afirmar más de lo que muestran los datos es un error de rigor.", "Usa «sugiere» o «es posible» cuando la evidencia es parcial.")],
    T=[
        ("abc", "{F} ¿Qué versión usa expresiones coloquiales como «súper»?", "La versión X", "La versión Y", "La versión Z", "«Súper» y «terrible» son coloquialismos y aparecen en X."),
        ("ab", "En Lengua: ¿qué es la impersonalidad en un texto académico?", "Poner el foco en lo observado y no en quien escribe", "Escribir sin mencionar ningún dato", "«Se detectó» es impersonal; evitar datos es otra cosa y no es una convención."),
        ("abc", "{F} ¿Qué rasgo muestra la expresión «se detectó» de la versión Y?", "Impersonalidad", "Coloquialismo", "Exageración", "«Se detectó» no nombra a la persona que observa y se centra en lo observado."),
        ("abc", "{F} ¿Qué expresión de la versión Y muestra cautela?", "«lo que sugiere un posible aporte»", "«se detectó»", "«en la muestra del pozo»", "«Sugiere» y «posible» limitan la afirmación a lo que la evidencia permite."),
        ("abc", "{F} ¿Qué versión es más adecuada para un informe dirigido a especialistas?", "La versión Y, por su precisión y su cautela", "La versión X, por su fuerza", "La versión Z, porque explica los términos", "Un informe para especialistas necesita términos exactos y cautela; X no es verificable."),
        ("ab", "{F} La versión X dice «era obvio que nadie hacía nada». ¿Qué problema tiene?", "Es un juicio sin respaldo, sin dato ni fuente", "Es demasiado cautelosa", "Ese juicio no se apoya en evidencia y no se puede verificar."),
        ("abc", "{F} ¿Qué versión es más adecuada para explicar el hallazgo a las familias del barrio?", "La versión Z, porque explica los términos y mantiene la cautela", "La versión X, porque es más emotiva", "La versión Y, porque es la más técnica", "Z conserva el rigor y lo hace comprensible; X pierde precisión y Y exige conocer términos."),
        ("ab", "Un estudiante afirma que reescribir en registro formal siempre implica cambiar los datos. ¿Es correcto?", "No: cambia la forma de decirlo, no los datos", "Sí: formal significa usar otros datos", "El registro es la manera de expresar la información; los datos deben mantenerse."),
        ("abc", "{F} Quien escribe Z sustituye «falta repetir las mediciones» por «ya está comprobado». ¿Qué ocurre?", "Pierde cautela y afirma más de lo que los datos permiten", "Mejora la precisión", "Pasa a ser un coloquialismo", "«Ya está comprobado» contradice que haya que repetir las mediciones."),
        ("ab", "Un compañero reescribe «el estudio muestra que el abono causa daños» como «los datos sugieren una posible relación entre el abono y los daños». ¿Qué ganó?", "Un grado de certeza ajustado a lo que la evidencia permite", "Más seguridad en la afirmación", "La segunda no afirma causa segura donde solo hay una asociación posible."),
        ("abc", "{F} Se debe pasar la versión X a un texto académico sin cambiar su contenido esencial. ¿Cuál es el mejor primer paso?", "Reemplazar los coloquialismos y reemplazar los juicios por datos con fuente", "Alargar las oraciones", "Agregar más exageraciones para que impacte", "Se parte quitando lo coloquial y los juicios sin respaldo, y reemplazándolos por datos atribuidos."),
        ("abc", "{F} Un equipo debe elegir cuál versión citar como modelo de registro académico. ¿Qué criterio es adecuado?", "Que tenga dato concreto, término preciso, impersonalidad y cautela", "Que tenga más adjetivos", "Que sea la más corta", "Esos cuatro rasgos definen el registro académico; adjetivos y brevedad no."),
        ("abc", "{F} Alguien reescribe la versión Y agregando «de forma concluyente se demuestra». ¿Qué ocurre con el texto?", "Pierde la cautela, porque la propia versión dice que falta un muestreo adicional", "Gana precisión técnica", "Se vuelve coloquial", "«Se demuestra» contradice la necesidad de confirmar, que sí aparece en el texto."),
    ],
    ctx=("abc", "Una estudiante escribe en su informe sobre bicicletas: «Obvio que todos andan en bici porque es lo mejor». Debe presentarlo en un informe académico. ¿Qué versión es mejor?", "«En la muestra, 14 de 40 estudiantes llegan en bicicleta, lo que sugiere un uso moderado»", "«Todos andan en bici, y punto»", "«Yo creo que la bici es genial»", "La primera da un dato, usa un término neutro y modaliza; las otras son coloquiales y sin respaldo."),
    sc=[
        ("En Lengua: ¿qué es la cautela en un texto académico?", "Ajustar lo que se afirma a lo que la evidencia permite", "La cautela evita decir más de lo que muestran los datos."),
        ("¿Para qué sirve un término técnico?", "Nombrar con precisión algo propio de un campo", "El término técnico reduce la ambigüedad."),
        ("¿Qué conserva una versión de divulgación respecto de la académica?", "Los datos y la cautela, con términos explicados", "Cambia la forma de explicar, no el rigor."),
    ],
    op=("Esta es una versión coloquial de ejemplo: «Las clases de refuerzo son geniales; todos mejoraron mucho, es obvio». Reescríbela en tres versiones: (1) académica para especialistas, (2) de divulgación para familias, (3) una breve nota sobre qué cambió. Debes inventar un dato de ejemplo (por ejemplo, 18 de 25 mejoraron) y señalar que es de ejemplo.",
        "(1) En el grupo de ejemplo, 18 de 25 estudiantes mejoraron su promedio tras las clases de refuerzo, lo que sugiere un efecto favorable; se requieren más datos. (2) En un curso de ejemplo, 18 de 25 estudiantes subieron su promedio después de las clases de refuerzo; falta confirmar si se repite. (3) Se eliminó el coloquialismo y la afirmación sin dato, y se agregó una cautela.",
        ["la versión académica es formal, con dato y cautela", "la versión de divulgación conserva el dato y explica en lenguaje claro", "la nota nombra al menos dos cambios"],
        ["tres textos breves"],
        ["mantener expresiones como «genial»", "cambiar el dato entre versiones", "afirmar sin cautela"],
        "Pregunta: «¿qué cambió en la forma y qué se mantuvo en el contenido?»."),
    reinforce="Reescribe con cautela y sin coloquialismos: «El nuevo horario es lo peor, todos están cansadísimos».",
    extend="Explica cuándo conviene usar un término técnico en un texto de divulgación y cuándo conviene explicarlo.",
)

# ============================================================ OAC-01, clase 5
F = ("Ficha 5 (encargo de ejemplo). El consejo de un liceo pide a un grupo de tercero medio un texto de 600 palabras para recomendar si conviene retrasar 30 minutos el inicio de las clases. "
     "Audiencia: apoderados y docentes, que no son especialistas. Plazo total: 10 días. "
     "Fuentes disponibles: A, una encuesta propia del curso; B, un informe de otro liceo; C, una nota de opinión sin datos. "
     "Plan en blanco: propósito, audiencia, género, tesis, esquema, reparto de fuentes y calendario.")
build(
    O1, 5, F,
    use="Aprenderé a planificar la respuesta a un encargo de escritura: propósito, audiencia, género, tesis, esquema y calendario. Sirve para producir un texto académico completo y organizado.",
    prior=["Sé elegir un género según el propósito y la audiencia.", "Sé formular una tesis.", "Sé distinguir fuentes con datos de fuentes de opinión."],
    explain=[
        "Planificar es decidir, antes de escribir, qué texto se producirá. Un plan mínimo responde: ¿para qué escribo (propósito)?, ¿para quién (audiencia)?, ¿en qué género?, ¿qué sostengo (tesis)?, ¿en qué partes se organiza el texto (esquema)? y ¿qué evidencia irá en cada parte? Con esas respuestas, la escritura deja de ser improvisación y se vuelve una secuencia de tareas.",
        "El esquema distribuye las ideas: una introducción que presenta el problema y la tesis; un desarrollo con argumentos, cada uno apoyado en evidencia de una fuente; y una conclusión que retoma la tesis y su alcance. Además, se decide qué fuente apoya cada parte y cuál se descarta por ser solo opinión sin datos. Un plan flexible se puede ajustar, pero no se omite.",
        "El calendario reparte el plazo en etapas: reunir y leer fuentes, esquematizar, escribir un borrador, revisar y entregar. Dejar tiempo para revisar evita entregar el primer borrador. Si el plazo es de 10 días y se reserva la mitad para escribir y el resto para el resto de las etapas, se puede repartir con cifras concretas y verificar que sumen el total.",
    ],
    vocab=[("planificación", "decisiones previas sobre propósito, audiencia, género, tesis y esquema"), ("esquema", "organización de las partes del texto y de sus ideas"), ("borrador", "primera versión completa que se revisará"), ("calendario", "reparto del plazo en etapas con fechas"), ("alcance", "hasta dónde llega lo que se afirma")],
    worked=[
        ("Definir propósito y audiencia", "Encargo: explicar a las familias por qué cambiar la hora de salida de un taller (de ejemplo). ¿Cuál es el propósito y cuál la audiencia?",
         ["Propósito: persuadir con razones para que se apruebe el cambio.", "Audiencia: familias, que no son especialistas, así que el lenguaje debe ser claro."],
         "Propósito persuasivo y audiencia general; género ensayo breve o carta argumentativa"),
        ("Repartir un calendario", "Un plazo de 8 días se divide en lectura de fuentes (2 días), esquema (1 día), borrador (3 días) y revisión. ¿Cuántos días quedan para la revisión?",
         ["Se suman los días usados: 2 + 1 + 3 = 6.", "Se resta del plazo: 8 − 6 = 2."],
         "2 días"),
    ],
    mistakes=[("Empezar a escribir sin plan y reunir las fuentes al final.", "Se pierde la guía: no se sabe qué evidencia pertenece a qué parte.", "Primero propósito, audiencia, tesis y esquema; luego se ubica la evidencia en cada parte."),
              ("Dejar la revisión para el último minuto.", "Sin tiempo no se pueden corregir contenido y organización.", "Reserva días de la planificación para revisar.")],
    T=[
        ("abc", "{F} ¿Cuál es la audiencia del encargo?", "Apoderados y docentes, que no son especialistas", "Solo especialistas en sueño", "El propio grupo que escribe", "La ficha indica que leerán apoderados y docentes sin formación especializada."),
        ("ab", "En Lengua: ¿qué es un esquema de escritura?", "La organización previa de las partes del texto y de sus ideas", "El borrador terminado del texto", "El esquema ordena el texto antes de escribirlo; el borrador es una versión completa posterior."),
        ("abc", "{F} ¿Qué género conviene al encargo, que pide recomendar una decisión con razones?", "Un ensayo breve o texto argumentativo con tesis y evidencia", "Un resumen de otro texto", "Una reseña crítica de un libro", "Recomendar con razones exige tesis y argumentos, rasgos del texto argumentativo."),
        ("=", "{F} El plazo total es de 10 días. Se reserva la mitad para el borrador, 2 días para leer fuentes y 1 día para el esquema. ¿Cuántos días quedan para revisar y entregar?", "10-10/2-2-1", "Se restan del plazo el borrador (5), las fuentes (2) y el esquema (1).", " días"),
        ("abc", "{F} ¿Qué fuente conviene descartar como evidencia principal?", "La C, porque es una opinión sin datos", "La A, porque es propia", "La B, porque es de otro liceo", "Una opinión sin datos no sustenta una afirmación; A y B aportan datos."),
        ("ab", "{F} Un estudiante propone esta tesis: «Retrasar 30 minutos la entrada podría favorecer la atención, según la encuesta propia y el informe de otro liceo». ¿Qué cuida?", "Su alcance, con cautela y apoyo en las fuentes A y B", "Afirma una certeza total sin necesitar fuentes", "Usa «podría» y atribuye a fuentes con datos, lo que mantiene la afirmación en su alcance."),
        ("abc", "{F} ¿Dónde conviene ubicar la tesis en el esquema?", "En la introducción, junto con la presentación del problema", "Solo en el último párrafo", "En un anexo al final", "La introducción presenta el problema y la tesis para guiar al lector desde el comienzo."),
        ("abc", "{F} El calendario es: lectura de fuentes 2 días, esquema 1 día, borrador 4 días. ¿Cuántos días quedan para revisar?", "3", "2", "4", "Se usan 2 + 1 + 4 = 7 días y 10 − 7 = 3 quedan para revisar."),
        ("ab", "Una compañera dice que, si ya tiene el esquema, no necesita elegir fuentes para cada parte. ¿Es correcto?", "No: cada argumento necesita la evidencia que lo apoye", "Sí: las fuentes se buscan al final", "Sin saber qué fuente apoya cada parte, el esquema queda sin sustento."),
        ("abc", "{F} Si el grupo escribe para las familias, ¿qué ajuste de lenguaje es adecuado?", "Explicar los términos y usar ejemplos del liceo", "Usar solo términos técnicos", "Evitar todo dato para que sea corto", "Las familias no son especialistas, así que se explican los términos y se incluyen datos claros."),
        ("abc", "{F} El grupo reparte las fuentes: A para el argumento sobre la atención del curso, B para comparar con otro liceo y C para el cierre, sin aclarar que C es solo opinión. ¿Qué falla tiene este reparto?", "Usa una opinión sin datos como apoyo del cierre sin señalar que es opinión", "Usa la fuente A", "Compara con otro liceo", "C no tiene datos; si se usa debe presentarse como opinión, no como evidencia."),
        ("=", "{F} El texto debe tener 600 palabras: la introducción y la conclusión llevan 90 palabras cada una, y el resto se reparte en tres argumentos de igual extensión. ¿Cuántas palabras lleva cada argumento?", "(600-90-90)/3", "Primero se quitan las 180 palabras de introducción y conclusión; las 420 restantes se dividen en tres.", " palabras"),
        ("abc", "{F} Al planificar, el grupo nota que la fuente B es de un liceo con otra jornada escolar. ¿Qué conviene hacer?", "Usarla como comparación y aclarar que el contexto es distinto", "Presentarla como si fuera del propio liceo", "Descartar todas las fuentes con datos", "Una fuente de contexto distinto sirve para comparar si se declara la diferencia."),
    ],
    ctx=("abc", "Un grupo debe escribir en 6 días un texto para el diario mural sobre el reciclaje. Asigna 1 día a fuentes, 1 a esquema, 2 al borrador y el resto a revisión. ¿Cuántos días de revisión tiene?", "2", "1", "3", "Se usan 1 + 1 + 2 = 4 días, de modo que 6 − 4 = 2 quedan para revisar."),
    sc=[
        ("En Lengua: ¿qué debe responder un plan de escritura antes de empezar?", "Para qué escribo, para quién, en qué género y qué sostengo", "Propósito, audiencia, género y tesis guían el resto de las decisiones."),
        ("¿Por qué se reserva tiempo para revisar?", "Para corregir contenido y organización antes de entregar", "La revisión mejora el texto y evita entregar el primer borrador."),
        ("=", "Si un plazo de 12 días reserva 3 para fuentes y 4 para el borrador, ¿cuántos quedan para esquema, revisión y entrega?", "12-3-4", "Se restan los días usados del total de 12."),
    ],
    op=("Elige un encargo: A) un texto para recomendar un lugar de reciclaje en el liceo, B) un texto para proponer un nuevo recreo activo, C) un texto para proponer un nuevo horario de biblioteca. Escribe un plan con propósito, audiencia, género, tesis provisional, un esquema de tres partes, una fuente (de ejemplo) por parte y un calendario de 8 días que sume exactamente 8.",
        "Encargo A. Propósito: persuadir. Audiencia: dirección y apoderados. Género: texto argumentativo. Tesis: un punto limpio en la entrada reduciría el papel desechado. Esquema: introducción, argumentos, conclusión. Fuentes: encuesta propia, informe de otro liceo, nota de opinión (solo como contexto). Calendario: 2 fuentes, 1 esquema, 3 borrador, 2 revisión = 8.",
        ["define propósito, audiencia y género coherentes", "esquema de tres partes con una fuente por parte", "calendario que suma 8 días"],
        ["hoja con plan completo de siete elementos"],
        ["calendario que no suma 8", "tesis sin razón", "usar la opinión sin datos como evidencia principal"],
        "Pregunta: «¿qué parte del plan depende de qué otra?»."),
    reinforce="Reparte 9 días en lectura, esquema, borrador y revisión, de modo que la revisión tenga al menos 2 días, y comprueba que sumen 9.",
    extend="Explica cómo cambiaría tu plan si la audiencia fuera un grupo de especialistas en lugar de apoderados.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 6 (comunidad de ejemplo «Taller de Agua»). Ana escribe un informe sobre el pozo del liceo. Beto lee su borrador y anota dudas como lector. "
     "Carla revisa el informe con una pauta de cinco criterios acordada por el taller. Darío escribe su propio texto y, a la vez, lee el de Ana. "
     "Reglas del taller: se comenta el texto y no a la persona, cada comentario indica el criterio y la parte del texto, y toda idea ajena se cita.")
build(
    O2, 1, F,
    use="Aprenderé qué roles cumplen autor, lector y revisor dentro de una comunidad de pares especialistas y qué reglas hacen posible trabajar juntos. Sirve para participar con responsabilidad en la producción de textos.",
    prior=["Sé escribir un borrador de un texto académico.", "Sé que un texto necesita revisión.", "He trabajado en equipo en tareas de curso."],
    explain=[
        "Una comunidad de pares especialistas es un grupo de personas que leen, escriben y aprenden sobre un mismo tema. En ella se circulan borradores, se comentan y se mejoran. Los pares no son «jefes» ni «alumnos»: son personas con un interés común que se ayudan mutuamente a mejorar los textos y a comprender mejor el tema.",
        "Hay tres roles que suelen alternarse: el autor, que escribe y responde por su texto; el lector, que lee para comprender y avisa dónde no entiende; y el revisor, que evalúa el texto con criterios acordados y propone mejoras fundamentadas. Una misma persona puede ser autor de su texto y lector o revisor del de otros. Cada rol tiene responsabilidades: el autor entrega un borrador legible y recibe comentarios sin ofenderse; el lector es honesto; el revisor sustenta sus observaciones.",
        "Para que la comunidad funcione se acuerdan normas: comentar el texto y no a la persona, indicar el criterio y el lugar exacto del comentario, respetar plazos, citar siempre las ideas ajenas y reconocer los aportes de cada integrante. Una comunidad que no tiene normas claras produce comentarios vagos, conflictos y retrasos.",
    ],
    vocab=[("pares especialistas", "personas que leen, escriben y aprenden juntas sobre un tema"), ("autor", "quien escribe un texto y responde por él"), ("lector", "quien lee para comprender y dice dónde no entiende"), ("revisor", "quien evalúa con criterios y propone mejoras"), ("criterio", "aspecto acordado con que se evalúa un texto")],
    worked=[
        ("Reconocer un rol", "Beto lee el borrador de Ana y anota: «En el párrafo 2 no entendí qué mide el aparato». ¿Qué rol cumple?",
         ["Lee para comprender y avisa dónde no entiende.", "No aplica una pauta de criterios ni propone una reescritura completa."],
         "Lector"),
        ("Aplicar una norma", "Un comentario dice: «Ana escribe mal». ¿Qué norma incumple y cómo se corrige?",
         ["Incumple comentar el texto y no a la persona, y no indica criterio ni lugar.", "Se corrige: «En el párrafo 3, la tesis no se distingue de los datos; conviene separarla (criterio: claridad)»."],
         "Se reescribe sobre el texto, con criterio y lugar"),
    ],
    mistakes=[("Pensar que el revisor es quien «corrige» y el autor solo obedece.", "El autor decide qué cambios acepta; el revisor propone con fundamento.", "El revisor propone y fundamenta; el autor evalúa y decide."),
              ("Comentar «me gustó» o «no me gustó» sin criterio.", "No sirve para mejorar el texto: no dice qué ni dónde.", "Indica criterio, lugar del texto y una sugerencia.")],
    T=[
        ("abc", "{F} ¿Qué rol cumple Beto en el taller?", "Lector", "Revisor con pauta", "Autor del informe", "Beto lee el borrador y anota dudas de comprensión, lo que corresponde al lector."),
        ("ab", "En Lengua: ¿qué es una comunidad de pares especialistas?", "Un grupo que lee, escribe y aprende junto sobre un tema", "Un grupo con un jefe que corrige a los demás", "Los pares comparten un interés y se ayudan; no hay jefes ni subordinados."),
        ("abc", "{F} ¿Quién revisa el informe con una pauta de cinco criterios acordada?", "Carla", "Beto", "Ana", "La ficha dice que Carla revisa con la pauta acordada por el taller."),
        ("abc", "{F} ¿Qué dos roles cumple Darío al mismo tiempo?", "Autor de su texto y lector del texto de Ana", "Revisor de Ana y lector de Carla", "Solo autor", "La ficha dice que Darío escribe su propio texto y lee el de Ana."),
        ("ab", "{F} Un comentario dice: «Ana escribe mal». ¿Qué norma del taller incumple?", "Comentar el texto y no a la persona", "Citar las ideas ajenas", "El comentario se dirige a Ana como persona y no indica criterio ni lugar."),
        ("abc", "{F} ¿Cuál es un comentario que cumple las normas del taller?", "«En el párrafo 2, la tesis no se distingue de los datos; conviene separarla (criterio: claridad)»", "«El párrafo 2 está mal»", "«Ana debería escribir mejor»", "El primero indica el lugar, el criterio y una sugerencia, y habla del texto."),
        ("abc", "¿Qué responsabilidad tiene el autor de un borrador?", "Entregar un borrador legible y recibir los comentarios con apertura", "Aceptar todos los cambios sin discutir", "Revisar solo el texto de otros", "El autor responde por su texto, pero decide qué cambios aceptar con fundamento."),
        ("ab", "¿Puede una misma persona ser autora de un texto y revisora de otro dentro de la comunidad?", "Sí, los roles se alternan según el texto", "No, cada persona tiene un rol fijo", "Los roles pertenecen al texto y no a la persona, y se alternan."),
        ("abc", "{F} Un integrante copia un párrafo de una fuente sin citarla. ¿Qué regla del taller incumple?", "Toda idea ajena se cita", "Se comenta el texto y no a la persona", "Se respetan los plazos", "La regla dice que toda idea ajena se cita."),
        ("abc", "{F} Beto escribe: «Me gustó mucho el informe». ¿Por qué no basta como comentario de lector?", "No indica qué parte ni qué se entendió o no", "Porque es demasiado largo", "Porque lo escribe un lector", "Un comentario útil dice dónde y por qué; «me gustó» no ayuda a mejorar."),
        ("abc", "{F} Dos integrantes del taller discuten porque uno comentó sobre la persona. ¿Qué medida ayuda más?", "Reescribir el comentario sobre el texto, con criterio y lugar", "Cambiar a todos los revisores", "Eliminar los comentarios del taller", "Recordar la norma de comentar el texto y no a la persona evita conflictos y mantiene la utilidad."),
        ("abc", "{F} Carla escribe su propia versión del párrafo 3 del informe y la pega en el borrador de Ana sin avisarle. ¿Qué falla de rol hay?", "El revisor propone y fundamenta; quien decide los cambios es la autora", "Carla actuó como lectora, que es lo que le correspondía", "Nada: el revisor decide qué cambios entran en el texto", "La revisora debe proponer con fundamento, y la autora evalúa y decide qué acepta."),
        ("ab", "Un revisor nunca indica con qué criterio evalúa. ¿Qué consecuencia tiene para el autor?", "No sabe qué mejorar ni por qué se le sugiere un cambio", "Todos sus textos mejoran más rápido", "Sin criterio, el comentario no se puede fundamentar ni aplicar con seguridad."),
    ],
    ctx=("abc", "En el taller del curso, Rosa terminó su borrador. Su lector le dijo: «En el párrafo 4 no entendí la cifra». Su revisora le pidió citar la fuente de esa cifra. ¿Qué debería hacer Rosa?", "Decidir qué cambios aceptar, aclarar la cifra y agregar la fuente", "Ignorar ambos comentarios", "Borrar la cifra sin revisar nada más", "El autor evalúa los comentarios y decide con fundamento; aquí ambos son pertinentes."),
    sc=[
        ("En Lengua: ¿cuáles son los tres roles de la comunidad de pares?", "Autor, lector y revisor", "Son los tres roles que se alternan al producir un texto."),
        ("¿Qué debe indicar un comentario útil?", "El criterio y el lugar exacto del texto", "Sin criterio ni lugar no se sabe qué mejorar."),
        ("¿Qué se comenta, según las normas?", "El texto y no a la persona", "El comentario se dirige al texto para mantener el respeto."),
    ],
    op=("Lee este fragmento de ejemplo: «Hace poco hicimos una encuesta. Salieron buenos resultados. La gente estuvo de acuerdo con el cambio». Actúa como lector y como revisor. Escribe: (1) dos comentarios como lector (qué no entiendes y dónde) y (2) dos comentarios como revisor, cada uno con criterio, lugar y sugerencia.",
        "Lector: «En la primera oración no entiendo de qué encuesta se habla»; «en la segunda no sé qué significa buenos resultados». Revisor: «Criterio precisión, frase 2: indicar cuántos respondieron y qué porcentaje apoyó»; «Criterio claridad, frase 3: especificar quién es la gente».",
        ["dos comentarios de lector sobre comprensión", "dos comentarios de revisor con criterio, lugar y sugerencia", "los comentarios hablan del texto y no de la persona"],
        ["cuatro comentarios escritos"],
        ["comentarios sin lugar", "juicios sobre la persona", "sugerencias que no se pueden aplicar"],
        "Pregunta: «¿podría la autora saber exactamente qué cambiar?»."),
    reinforce="Reescribe este comentario inútil como comentario útil de revisor: «Está confuso».",
    extend="Explica por qué rotar los roles de autor, lector y revisor mejora el aprendizaje de la comunidad.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 7 (párrafo de ejemplo y cuatro comentarios). Párrafo de Mateo: «La bicicleta es el mejor transporte. Muchos la usan. Por eso el liceo debería hacer ciclovías». "
     "Comentario 1: «Está mal». "
     "Comentario 2: «Frase 1, criterio evidencia: falta un dato que muestre que es el mejor; propongo citar la encuesta». "
     "Comentario 3: «Mateo no sabe argumentar». "
     "Comentario 4: «Frase 2, criterio precisión: reemplazar «muchos» por una cifra».")
build(
    O2, 2, F,
    use="Aprenderé a dar retroalimentación útil a un texto de un par: específica, fundamentada en criterios y con sugerencias aplicables. Sirve para que la revisión mejore el texto y cuide la relación.",
    prior=["Conozco los roles de autor, lector y revisor.", "Sé que se comenta el texto y no a la persona.", "Sé identificar una tesis y su evidencia."],
    explain=[
        "Retroalimentar es devolver al autor una lectura de su texto para que lo mejore. Un comentario útil tiene cuatro rasgos: es específico (dice dónde), se apoya en un criterio acordado (por ejemplo, claridad, evidencia o precisión), explica por qué importa y propone una mejora posible. Un comentario como «está mal» no cumple ninguno de esos rasgos y no ayuda a corregir.",
        "Conviene priorizar. Primero se comentan los problemas de contenido y organización (tesis, evidencia, estructura) y después los de forma (ortografía, puntuación, precisión del lenguaje, estilo). Corregir solo la superficie sin revisar el contenido deja intactos los problemas importantes. También conviene señalar lo que funciona bien, para que el autor lo conserve.",
        "Un buen comentario cuida el trato: se dirige al texto y usa fórmulas como «propongo» o «sugiero», sin descalificar. Comentar a la persona («no sabe argumentar») ofende y no dice qué mejorar. La retroalimentación es una forma de colaborar, no de calificar a nadie, y el autor siempre decide qué acepta.",
    ],
    vocab=[("retroalimentación", "comentario que devuelve al autor una lectura de su texto para mejorarlo"), ("criterio", "aspecto acordado con que se evalúa, como claridad o evidencia"), ("específico", "que dice con precisión dónde y qué"), ("sugerencia", "propuesta de mejora que el autor puede aplicar o no"), ("priorizar", "ordenar los comentarios de lo más importante a lo menos")],
    worked=[
        ("Reconocer un comentario útil", "Comentario: «Párrafo 2, criterio evidencia: la cifra no tiene fuente; sugiero citar la encuesta». ¿Qué rasgos tiene?",
         ["Lugar: párrafo 2.", "Criterio: evidencia.", "Sugerencia: citar la encuesta."],
         "Es específico, con criterio y con sugerencia"),
        ("Mejorar un comentario", "Comentario: «Está desordenado». Mejóralo con el lugar y un criterio.",
         ["Se identifica dónde está el desorden: la conclusión aparece en el segundo párrafo.", "Se indica el criterio y una mejora."],
         "«Criterio organización: la conclusión aparece en el párrafo 2; conviene moverla al final»."),
    ],
    mistakes=[("Corregir solo ortografía y dar el trabajo por revisado.", "Los problemas de contenido y organización siguen sin atenderse.", "Revisa primero tesis, evidencia y estructura; deja la ortografía para después."),
              ("Decir «mejora la redacción» sin más.", "No indica qué mejorar ni cómo.", "Señala la oración, el criterio y una opción de reescritura.")],
    T=[
        ("abc", "{F} ¿Cuál comentario es específico y fundamentado en un criterio?", "El comentario 2", "El comentario 1", "El comentario 3", "El comentario 2 indica la frase, el criterio y una sugerencia; los otros no."),
        ("ab", "En Lengua: ¿qué significa que un comentario sea específico?", "Que indica con precisión dónde y qué se comenta", "Que es muy largo", "Específico es lo contrario de vago: dice el lugar y el aspecto."),
        ("abc", "{F} ¿Qué comentario descalifica a la persona en lugar de comentar el texto?", "El comentario 3", "El comentario 2", "El comentario 4", "«Mateo no sabe argumentar» se refiere a la persona y no al texto."),
        ("abc", "{F} ¿Qué criterio usa el comentario 4?", "Precisión", "Evidencia", "Ortografía", "El comentario 4 pide una cifra en vez de «muchos», es decir, precisión."),
        ("ab", "{F} ¿Qué falta en el comentario 1, «Está mal»?", "El lugar, el criterio y una sugerencia", "Una pregunta final", "No dice qué parte ni por qué está mal, así que no se puede mejorar."),
        ("abc", "{F} ¿Cuál es una buena sugerencia para el párrafo de Mateo, según el criterio de evidencia?", "Citar un dato de la encuesta que muestre cuántos usan bicicleta", "Cambiar la palabra «bicicleta» por «vehículo»", "Agregar adjetivos al final", "Un dato con fuente apoya la afirmación; los cambios de palabra no resuelven la falta de evidencia."),
        ("abc", "Un revisor encuentra errores de ortografía, una tesis difusa y una conclusión que no responde a la pregunta. ¿Qué conviene comentar primero?", "La tesis y la conclusión, porque afectan el sentido del texto", "Los acentos, porque son más fáciles", "Ninguno, hasta que el autor pida ayuda", "Se prioriza el contenido y la organización antes de la forma."),
        ("ab", "Un compañero dice: «Si corrijo toda la ortografía, el texto queda revisado». ¿Es correcto?", "No: puede quedar el contenido y la organización sin atender", "Sí: la ortografía es lo único que importa", "Corregir solo la superficie deja los problemas de fondo."),
        ("abc", "{F} ¿Qué cambio vuelve más útil el comentario 3?", "«Criterio argumentación: las frases 2 y 3 no explican por qué la bicicleta es mejor»", "«Mateo debería intentarlo otra vez»", "«Habría que ser más claro»", "Se dirige al texto, indica lugar y criterio, y señala el problema."),
        ("abc", "{F} Un lector agrega: «Frase 3: la conexión entre ‘muchos la usan’ y ‘ciclovías’ no está explicada; propongo agregar una razón». ¿Qué rasgo tiene?", "Es específico, usa el criterio de argumentación y sugiere una mejora", "Es una descalificación de la persona", "Solo menciona ortografía", "Cumple los tres elementos: lugar, criterio y una sugerencia concreta."),
        ("abc", "Un revisor dice: «Esto es lo peor que he leído». ¿Qué conviene responderle como par?", "Pedirle que reformule indicando lugar, criterio y sugerencia", "Aceptar el comentario y reescribir todo", "Aceptarlo en silencio y dejar de participar", "La retroalimentación debe ayudar a mejorar; se le pide precisión y respeto."),
        ("abc", "{F} Un revisor propone al mismo tiempo cambiar la tesis, el orden de los argumentos y la ortografía de doce palabras. ¿Cómo conviene presentar los comentarios?", "Primero tesis y argumentos, y después la ortografía", "Empezar por la ortografía", "Mezclarlos sin orden", "Se priorizan los problemas de contenido y organización antes de los de forma."),
        ("{F} ¿Cuántos de los cuatro comentarios cumplen lugar, criterio y sugerencia a la vez?", "2", "Solo los comentarios 2 y 4 incluyen lugar, criterio y una mejora posible."),
    ],
    ctx=("abc", "Daniela recibió este comentario sobre su informe de ejemplo: «Falta rigor». ¿Cuál es la mejor respuesta como colaboradora?", "Pedir al revisor que indique en qué parte y qué criterio le falla", "Borrar el informe", "Responder que el revisor no entiende", "Un comentario vago se aclara pidiendo lugar y criterio, para poder mejorar."),
    sc=[
        ("En Lengua: ¿qué cuatro rasgos tiene un comentario útil?", "Específico, con criterio, explicado y con sugerencia", "Los cuatro rasgos permiten que el autor sepa qué cambiar."),
        ("¿Qué se comenta primero, el contenido o la forma?", "El contenido y la organización", "Los problemas de fondo afectan más el sentido del texto."),
        ("¿Cómo debe tratar un comentario a la persona autora?", "Hablando del texto, sin descalificarla", "El respeto hacia la persona mantiene viva la colaboración del taller."),
    ],
    op=("Lee este párrafo de ejemplo: «Las clases deberían empezar más tarde. Todos duermen poco. Por eso rinden mal». Redacta cuatro comentarios útiles: dos sobre contenido (tesis, evidencia o argumentación) y dos sobre forma (precisión del lenguaje, puntuación o estilo). Cada uno debe indicar lugar, criterio y sugerencia.",
        "1. Frase 2, criterio evidencia: «todos» no es verificable; sugiero citar una encuesta. 2. Frase 3, criterio argumentación: la relación entre dormir poco y rendir mal no está explicada; sugiero agregar una razón. 3. Frase 1, criterio precisión: indicar cuánto más tarde. 4. Frase 2, criterio precisión: reemplazar «todos» por una cifra.",
        ["dos comentarios de contenido y dos de forma", "cada comentario indica lugar, criterio y sugerencia", "todos hablan del texto"],
        ["cuatro comentarios escritos"],
        ["comentarios vagos", "solo comentarios de forma", "sugerencias inaplicables"],
        "Pregunta: «¿qué haría la autora al leer tu comentario?»."),
    reinforce="Convierte «No me convence» en un comentario con lugar, criterio y sugerencia, sobre el párrafo de la actividad.",
    extend="Explica por qué mencionar lo que funciona bien también es parte de la retroalimentación.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 8 (comentarios recibidos, de ejemplo). Borrador de Valeria: informe de 400 palabras sobre el uso de bicicletas en el liceo, con tesis, dos argumentos y conclusión. "
     "Comentario A (lector): «En el párrafo 2 no entiendo qué significa ‘uso moderado’». "
     "Comentario B (revisora): «Criterio evidencia: el argumento 2 no tiene fuente; sugiero citar la encuesta». "
     "Comentario C (revisor): «Eliminar el argumento 1 y reemplazarlo por mi opinión». "
     "Comentario D (lector): «La conclusión repite la introducción sin agregar la cifra principal».")
build(
    O2, 3, F,
    use="Aprenderé a recibir comentarios, decidir cuáles incorporar, justificar mis decisiones y registrar los cambios. Sirve para mejorar el texto sin perder mi propósito.",
    prior=["Sé qué es un comentario útil.", "Conozco los roles de autor, lector y revisor.", "Sé qué es la tesis de mi texto."],
    explain=[
        "Recibir retroalimentación exige separar tres cosas: lo que dice el comentario, lo que importa para el propósito del texto y lo que se decide hacer. El autor no está obligado a aceptar todo, pero tampoco debe rechazar sin pensar. Cada comentario se contrasta con el propósito y la audiencia: si mejora la claridad, la evidencia o la organización, probablemente conviene aceptarlo.",
        "Una buena forma de ordenar las decisiones es un registro de cambios, una lista con tres columnas: el comentario, la decisión (aceptar, aceptar parcialmente o no aceptar) y la razón. Si no se acepta, se explica por qué, con respeto. Así el equipo entiende qué cambió y la autoría de las ideas queda clara. El registro también sirve para detectar comentarios que se repiten.",
        "Algunos comentarios piden cambios que alteran la tesis o reemplazan la voz del autor («cambia esto por mi opinión»). Esos casos se conversan: el autor puede aceptar la preocupación de fondo sin adoptar la solución propuesta. La mejora de un texto colectivo se apoya en el diálogo y no en la imposición.",
    ],
    vocab=[("registro de cambios", "lista de comentarios con decisión y razón"), ("aceptar parcialmente", "tomar la idea del comentario sin adoptar la solución exacta"), ("propósito", "lo que el texto debe lograr"), ("justificar", "explicar la razón de una decisión"), ("voz del autor", "modo propio de decir las ideas del texto")],
    worked=[
        ("Decidir sobre un comentario", "Comentario: «Criterio evidencia: falta fuente en el argumento 2». El autor tiene la encuesta. ¿Qué decide?",
         ["El comentario mejora la evidencia, que es clave para el propósito.", "El autor tiene la fuente, así que puede incorporarla."],
         "Aceptar: citar la encuesta en el argumento 2"),
        ("Aceptar parcialmente", "Comentario: «Elimina el argumento 1 y usa mi opinión». El argumento 1 tiene datos. ¿Qué conviene?",
         ["El argumento 1 tiene datos, por lo que eliminarlo debilita el texto.", "La preocupación puede ser que el argumento esté poco claro."],
         "Aceptar parcialmente: pedir al revisor qué le preocupa y mejorar el argumento sin eliminarlo"),
    ],
    mistakes=[("Aceptar todos los comentarios sin evaluarlos.", "Algunos comentarios contradicen el propósito o la tesis.", "Contrasta cada uno con el propósito antes de decidir."),
              ("Rechazar un comentario porque «me dolió».", "Reaccionar a la persona impide ver si el contenido es útil.", "Lee el comentario como información sobre el texto y decide con razones.")],
    T=[
        ("abc", "{F} ¿Qué comentario pide una definición de un término?", "El comentario A", "El comentario B", "El comentario C", "El comentario A dice que no entiende «uso moderado», así que pide aclararlo."),
        ("ab", "En Lengua: ¿qué es un registro de cambios?", "Una lista de comentarios con la decisión tomada y la razón", "Una copia del borrador anterior sin cambios", "Registra qué se decidió y por qué."),
        ("abc", "{F} ¿Qué decisión conviene ante el comentario B, si Valeria tiene la encuesta?", "Aceptarlo y citar la encuesta en el argumento 2", "Rechazarlo porque cita su texto", "Eliminar todo el argumento 2", "El comentario mejora la evidencia y Valeria cuenta con la fuente."),
        ("abc", "{F} ¿Qué comentario reemplaza la voz de la autora con la opinión del revisor?", "El comentario C", "El comentario A", "El comentario D", "C pide eliminar un argumento y poner «mi opinión», lo que reemplaza la voz de la autora."),
        ("abc", "{F} ¿Qué conviene hacer con el comentario C?", "Conversar con el revisor y aceptar la preocupación de fondo sin adoptar su solución", "Cumplirlo al pie de la letra", "Ignorarlo sin responder", "El autor decide, pero conviene entender la preocupación del revisor."),
        ("ab", "{F} El comentario D dice que la conclusión no agrega la cifra principal. ¿Qué decisión es razonable?", "Aceptarlo y agregar la cifra principal a la conclusión", "Rechazarlo porque la conclusión debe repetir la introducción", "Una conclusión debe retomar la tesis y destacar lo principal, incluida la cifra clave."),
        ("abc", "{F} Valeria decide no aceptar el comentario C. ¿Cuál es una razón fundada para esa decisión?", "Reemplazaría un argumento por una opinión sin evidencia y cambiaría la voz de la autora", "Lo escribió un compañero y no una persona con más experiencia", "Ningún comentario de un revisor debe aceptarse", "Una razón fundada se apoya en el propósito del texto: C quitaría un argumento y pondría una opinión sin datos."),
        ("ab", "¿Qué debe incluir una decisión de no aceptar un comentario?", "Una razón respetuosa basada en el propósito del texto", "Un silencio para evitar discusión", "Sin razón, el revisor no sabe por qué no se aplicó su comentario."),
        ("abc", "{F} Dos revisores piden cambios opuestos: uno quiere la tesis al comienzo y otro al final. ¿Qué criterio ayuda a decidir?", "El propósito y la audiencia del texto", "Elegir la opinión del revisor más veterano", "Lanzar una moneda", "La decisión se apoya en lo que el texto debe lograr para su audiencia."),
        ("abc", "{F} ¿Cuál es una fila completa del registro de cambios para el comentario A?", "Comentario A | aceptar | «uso moderado» no se entiende y se aclarará con una cifra", "Comentario A | aceptar", "Comentario A | razón: lo dijo un lector", "Una fila completa trae el comentario, la decisión y la razón; las otras omiten alguna de las tres."),
        ("abc", "{F} Si Valeria incorpora el comentario A, ¿qué cambio hará en el texto?", "Definir qué significa «uso moderado» con una cifra", "Quitar la expresión sin explicar", "Cambiar la tesis", "A dice que no se entiende el término; se aclara con un dato."),
        ("abc", "{F} Valeria recibe además un comentario E que dice «Esto es un desastre». ¿Cómo lo registra?", "Pide al revisor que indique lugar y criterio, porque así no puede decidir", "Lo acepta y reescribe todo", "Lo borra sin responder", "Un comentario sin lugar ni criterio no permite decidir; se pide que se aclare."),
        ("abc", "Un autor acepta un cambio que contradice el propósito de su texto solo porque lo dijo un revisor veterano. ¿Qué error comete?", "Decide por la autoridad de quien comenta y no por el propósito del texto", "Respeta el registro de cambios", "Acepta parcialmente el comentario", "Los cambios se deciden por su aporte al propósito, no por quién los dice."),
    ],
    ctx=("abc", "Tomás recibe este comentario sobre su informe de ejemplo: «Cambia tu tesis por la mía, que es mejor». ¿Qué conviene hacer?", "Conversar sobre qué preocupa al revisor y decidir si ajusta su tesis con argumentos", "Aceptar sin pensar", "Rechazar enojado sin leer la propuesta", "La tesis es la voz del autor; se dialoga y se decide con fundamento."),
    sc=[
        ("En Lengua: ¿qué tres decisiones puede tomar un autor ante un comentario?", "Aceptar, aceptar parcialmente o no aceptar", "Cada decisión debe tener una razón."),
        ("¿Contra qué se contrasta un comentario antes de decidir?", "El propósito y la audiencia del texto", "Esos dos factores indican si el cambio mejora el texto."),
        ("=", "Un autor recibió 9 comentarios, aceptó 5 y rechazó 1. ¿Cuántos aceptó parcialmente?", "9-5-1", "Se restan los aceptados y rechazados del total para obtener los parciales."),
    ],
    op=("Imagina que recibes estos tres comentarios sobre un informe tuyo de ejemplo: (1) «En la segunda frase falta la fuente del dato», (2) «Cambia toda la tesis por mi idea», (3) «No se entiende el término ‘sobrecarga’». Completa un registro de cambios con tres columnas: comentario, decisión y razón.",
        "(1) Aceptar: citar la fuente mejora la evidencia. (2) Aceptar parcialmente: conversar con quien comentó para entender su preocupación, sin cambiar toda la tesis. (3) Aceptar: definir «sobrecarga» ayuda a la audiencia.",
        ["registro con tres columnas completas", "la decisión de cada comentario tiene una razón", "distingue aceptar, parcial y no aceptar"],
        ["tabla con tres filas"],
        ["no dar razones", "aceptar todo sin evaluar", "rechazar sin justificar"],
        "Pregunta: «¿esta decisión ayuda al propósito del texto?»."),
    reinforce="Escribe un registro de cambios con dos comentarios inventados y la decisión de cada uno con su razón.",
    extend="Explica cómo el registro de cambios ayuda cuando varias personas escriben un mismo texto.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 9 (plan de equipo, de ejemplo). Cuatro integrantes (Ema, Fito, Gabi y Hugo) escriben un informe de cinco secciones: introducción, método, resultados, discusión y conclusión. "
     "Reparto: Ema escribe introducción y conclusión; Fito, método; Gabi, resultados; Hugo, discusión. "
     "Acuerdos: una sola forma de citar, tiempo verbal pasado en método y resultados, y archivo «informe_v1», «informe_v2». "
     "Plazo: 12 días en total, con 3 días para reunir las secciones y revisarlas entre todos.")
build(
    O2, 4, F,
    use="Aprenderé a coordinar un texto escrito entre varias personas: repartir tareas, acordar convenciones comunes, unificar el texto y reconocer la autoría. Sirve para producir un solo informe coherente.",
    prior=["Conozco los roles de autor, lector y revisor.", "Sé dar y recibir comentarios.", "Sé que el texto necesita una estructura clara."],
    explain=[
        "Escribir entre varias personas exige coordinación. Primero se reparte el trabajo por secciones y se define quién es responsable de cada una, para que no haya partes duplicadas ni vacías. Después se acuerdan convenciones comunes: cómo citar, qué tiempo verbal usar, qué vocabulario técnico y qué formato. Sin esos acuerdos, el texto parece un collage de voces distintas.",
        "Los textos colectivos se versionan: cada archivo lleva un nombre con número de versión o fecha, y solo una versión es la oficial. Antes de integrar las partes, cada sección se revisa con la pauta acordada; luego una persona o el equipo unifica el texto, cuidando la coherencia: que la tesis de la introducción se retome en la conclusión y que los términos sean iguales en todo el texto.",
        "También se reconoce la autoría: quién escribió qué y quién revisó. Copiar la sección de otro integrante como propia o borrar su aporte es una falta de respeto. Las decisiones se registran, los plazos se cumplen y los desacuerdos se resuelven con diálogo y criterios, sin imponer. La responsabilidad del producto final es del equipo completo.",
    ],
    vocab=[("sección", "parte de un texto con una función propia"), ("convención común", "acuerdo de forma que sigue todo el equipo"), ("versión", "estado fechado o numerado de un archivo"), ("coherencia", "relación lógica entre las partes de un texto"), ("autoría", "reconocimiento de quién escribió o revisó cada parte")],
    worked=[
        ("Detectar un vacío en el reparto", "Un equipo reparte introducción, método y resultados, pero nadie asumió la conclusión. ¿Qué problema aparece?",
         ["Se compara el reparto con las secciones del informe.", "Falta una persona responsable de la conclusión."],
         "Hay una sección sin responsable; se debe asignar"),
        ("Unificar una convención", "Ema cita «según Pérez (2020)» y Fito pone el número entre corchetes. ¿Cómo se resuelve?",
         ["Se acuerda un solo estilo de cita para todo el equipo.", "Quien tenga el otro estilo lo adapta."],
         "Se elige un único estilo de cita y todos lo aplican"),
    ],
    mistakes=[("Juntar las secciones al último día sin leerlas juntas.", "Quedan repeticiones, contradicciones y voces distintas.", "Reserva días para integrar y revisar el texto completo."),
              ("Escribir sobre la versión de otro sin avisar.", "Se pierde el rastro de quién cambió qué.", "Usa versiones numeradas y registra los cambios.")],
    T=[
        ("abc", "{F} ¿Qué sección escribe Fito?", "Método", "Resultados", "Discusión", "El reparto dice que Fito escribe el método."),
        ("ab", "En Lengua: ¿qué es una convención común en un texto colectivo?", "Un acuerdo de forma que sigue todo el equipo", "Una opinión personal de quien coordina", "Es una regla compartida, como el estilo de cita."),
        ("abc", "{F} Ema escribe dos de las cinco secciones. ¿Qué riesgo trae eso para el plazo?", "Si Ema se atrasa, quedan dos secciones sin terminar y se acorta la revisión conjunta", "Ninguno, porque cada integrante trabaja en una sola sección", "Que Fito y Gabi deban cambiar el estilo de cita", "Una persona con más secciones concentra el riesgo: su atraso afecta varias partes y la integración."),
        ("abc", "{F} ¿Quién escribe la introducción y la conclusión?", "Ema", "Gabi", "Hugo", "El reparto asigna ambas secciones a Ema."),
        ("abc", "{F} ¿Qué acuerdo de forma tiene el equipo para citar?", "Una sola forma de citar para todos", "Cada integrante cita a su manera", "No se cita en el método", "La ficha dice que se acordó una única forma de citar."),
        ("ab", "{F} El equipo guarda «informe_v1» y «informe_v2». ¿Para qué sirve esto?", "Para saber cuál es la versión más reciente y no perder cambios", "Para ocultar quién escribió cada parte", "Los números de versión ordenan el trabajo y evitan pisar archivos."),
        ("abc", "{F} Si Hugo termina la discusión con 6 días de atraso, ¿qué consecuencia es más probable?", "Se acorta el tiempo de revisión conjunta de todo el equipo", "No pasa nada con el resto", "Se cancela el informe", "Los 3 días de revisión dependen de que todas las secciones estén listas."),
        ("abc", "Al juntar las partes, la introducción habla de «estudiantes» y la discusión de «alumnado». ¿Qué falla de coherencia aparece?", "Términos distintos para lo mismo", "Falta de datos", "Exceso de citas", "Unificar el vocabulario es parte de la coherencia."),
        ("ab", "Gabi copia el texto de la discusión de Hugo y lo presenta como suyo en otra tarea. ¿Qué ocurre?", "Falta de respeto a la autoría de Hugo", "Colaboración permitida", "Usar el aporte de un compañero sin reconocerlo es no respetar su autoría."),
        ("abc", "{F} El equipo detecta que el método está en presente y los resultados en pasado. ¿Qué acuerdo incumple?", "El uso del pasado en método y resultados", "La forma de citar", "El nombre de los archivos", "Los acuerdos pedían pasado en ambas secciones."),
        ("abc", "{F} Ema y Hugo discuten sobre la conclusión. ¿Cuál es la forma más adecuada de resolverlo?", "Revisar juntos el propósito y los criterios del texto y decidir con argumentos", "Que gane el que insiste más", "Eliminar la conclusión", "Las decisiones se resuelven con diálogo y criterios compartidos."),
        ("=", "{F} Hugo entrega su discusión el día 9 de los 12. La integración y revisión toman 3 días desde que están todas las secciones. ¿En qué día termina la revisión?", "9+3", "Se suman los 3 días de integración al día 9 de entrega de la última sección.", ""),
        ("abc", "Dos integrantes editan a la vez la misma sección y cada uno guarda su propia copia. ¿Qué problema aparece?", "Dos versiones distintas de la sección y riesgo de perder cambios", "Un texto más coherente", "Mayor claridad en la autoría", "Sin versionado coordinado, los cambios paralelos se pisan o se pierden."),
    ],
    ctx=("abc", "Un grupo de cuatro estudiantes tiene 10 días para entregar un informe sobre el consumo de agua en el liceo (de ejemplo). Quieren escribir en 5 días, reunir y revisar en 3 y entregar el día restante. ¿Cuántos días sobran para otras tareas?", "1", "2", "0", "Se usan 5 + 3 + 1 = 9 días de los 10 disponibles, de modo que sobra 1."),
    sc=[
        ("En Lengua: ¿para qué se reparte un texto colectivo por secciones con responsables?", "Para que no haya partes duplicadas ni vacías", "Cada sección tiene una persona a cargo."),
        ("¿Qué se debe hacer antes de unir las secciones?", "Revisarlas con la pauta acordada", "La revisión por sección evita errores acumulados."),
        ("¿Qué se debe reconocer en un texto colectivo?", "Quién escribió y quién revisó cada parte", "Esto respeta la autoría de cada integrante del equipo."),
    ],
    op=("Un equipo de tres personas (Ana, Beto y Cami) debe escribir un informe de cuatro secciones: introducción, desarrollo, discusión y conclusión, en 9 días. Escribe: (1) un reparto con responsable por sección, (2) dos convenciones comunes, (3) un calendario que sume 9 días con una etapa de integración y (4) una forma de nombrar las versiones.",
        "(1) Ana: introducción y conclusión; Beto: desarrollo; Cami: discusión. (2) Un solo estilo de cita y tiempo verbal pasado en el desarrollo. (3) Escribir 5 días, integrar y revisar 3 días, entregar 1 día = 9. (4) informe_v1, informe_v2, con la fecha al lado.",
        ["cada sección tiene un responsable", "dos convenciones comunes", "calendario que suma 9 días", "sistema de versiones"],
        ["plan escrito de cuatro puntos"],
        ["secciones sin responsable", "calendario que no suma 9", "no definir cómo nombrar versiones"],
        "Pregunta: «¿cómo sabrán cuál es la versión oficial?»."),
    reinforce="Escribe tres acuerdos de convención que un equipo debería tomar antes de empezar a escribir un informe entre cuatro personas.",
    extend="Explica por qué la coherencia final no se logra solo juntando las secciones.",
)
