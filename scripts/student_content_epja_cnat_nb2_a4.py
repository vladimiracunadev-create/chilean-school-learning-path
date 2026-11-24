"""Ciencias Naturales EPJA Básica N2, módulo 1, desempeño OAD-04: analizar datos sobre enfermedades del sistema reproductor humano, tendencias, prevención y autocuidado. Todo en papel; datos de ejemplo rotulados; sin consejo clínico."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = "Papel, lápiz y goma. Todo se resuelve con los textos y datos de ejemplo escritos en la ficha. Este cuaderno es ciencia general con lenguaje respetuoso, no un consejo médico: las dudas personales se conversan con una persona profesional del centro de salud, con privacidad."
build = make_build(MATERIALS)

O4 = "EPJA-CNAT-NB2-OAD-04"
PRIOR = ["Conozco los niveles de organización y varios sistemas del cuerpo.", "Sé leer tablas y distinguir una fuente confiable de una cadena anónima."]


def K(n, F, use, explain, vocab, worked, mistakes, T, ctx, sc, op, rf, ex_):
    if len(op) == 5:  # (enunciado, ejemplo, criterios, evidencia, retroalimentación): los errores son los frecuentes de la clase
        op = (*op[:4], [m[0] for m in mistakes], op[4])
    build(O4, n, F, use=use, prior=PRIOR, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes, T=T, ctx=ctx, sc=sc, op=op, reinforce=rf, extend=ex_)


# ====================================================== OAD-04 clase 1
F = ("Ficha 1 (frases de ejemplo de un folleto de salud). Frase 1: «El sistema reproductor produce células sexuales y, en una mujer, permite gestar un embarazo». "
     "Frase 2: «La salud sexual y reproductiva incluye información confiable, respeto y consulta a profesionales». Frase 3: «Toda relación sexual necesita consentimiento: un acuerdo libre de las personas involucradas». "
     "Frase 4: «Las infecciones de transmisión sexual se pasan al compartir un vaso».")
K(1, F,
  "Hoy aprenderé a partir de la vida diaria qué es la salud sexual y reproductiva, qué hace el sistema reproductor y cómo separar hechos de mitos con información confiable.",
  ["El sistema reproductor es el conjunto de órganos que permite la reproducción, es decir, producir nuevos seres. En las personas, produce células sexuales llamadas gametos: los óvulos en las mujeres y los espermatozoides en los hombres. Además produce hormonas, que son mensajeros químicos del cuerpo.",
   "La salud sexual y reproductiva es parte de la salud general. Incluye información confiable, respeto por uno mismo y por las demás personas, consentimiento y consulta a profesionales. El consentimiento es un acuerdo libre entre las personas involucradas. Ninguna persona debe ser presionada.",
   "Sobre este tema circulan muchos mitos, ideas falsas que se repiten. Para separar hechos de mitos se usan fuentes confiables, como el centro de salud o la matrona. En este cuaderno se estudia ciencia general; las dudas personales se conversan en privado con un profesional."],
  [("reproducción", "proceso por el que los seres vivos producen nuevos seres"), ("gametos", "células sexuales: óvulo y espermatozoide"), ("hormona", "mensajero químico que el cuerpo produce y que regula funciones"), ("consentimiento", "acuerdo libre de las personas involucradas")],
  [("Distinguir hecho de mito", "Un mensaje dice «las infecciones de transmisión sexual se pasan al compartir un vaso». ¿Es un hecho o un mito?",
    ["Hay que buscar una fuente confiable de salud.", "Esas infecciones no se transmiten así: es un mito."], "Es un mito"),
   ("Reconocer un gameto", "¿Cómo se llama la célula sexual femenina?", ["Los gametos son las células sexuales.", "La femenina se llama óvulo."], "Óvulo")],
  [("Creer todo lo que circula en cadenas sobre sexualidad.", "Se confunde popularidad con verdad.", "Revisa la fuente: centro de salud, matrona o institución con fecha."),
   ("Pensar que el consentimiento se da una sola vez para siempre.", "Se olvida que debe ser libre y se puede retirar.", "El consentimiento es libre y puede cambiar; sin acuerdo, no corresponde.")],
  [("abc", "¿Qué es la reproducción?", "el proceso por el que los seres vivos producen nuevos seres", "un tipo de alimento", "una enfermedad", "Reproducirse es generar nuevos individuos de la misma especie."),
   ("abc", "¿Cómo se llama la célula sexual masculina?", "espermatozoide", "óvulo", "neurona", "El espermatozoide es el gameto masculino."),
   ("abc", "{F} ¿Qué dice la frase 2 sobre la salud sexual y reproductiva?", "incluye información confiable, respeto y consulta a profesionales", "es solo cosa de adultos mayores", "no tiene relación con la salud", "La frase 2 la describe como parte de la salud con esos elementos."),
   ("abc", "{F} ¿Qué es el consentimiento según la frase 3?", "un acuerdo libre de las personas involucradas", "una orden de una persona", "un silencio", "La frase 3 lo define como acuerdo libre."),
   ("abc", "{F} ¿Cuál de las frases es un mito?", "la frase 4", "la frase 1", "la frase 2", "Las infecciones de transmisión sexual no se pasan por compartir un vaso."),
   ("abc", "¿Qué produce además de gametos el sistema reproductor?", "hormonas", "nutrientes", "oxígeno", "Los órganos reproductores producen hormonas que regulan funciones del cuerpo."),
   ("abc", "¿Dónde se puede obtener información confiable sobre salud sexual?", "en un centro de salud, con matrona o equipo de salud", "en cadenas anónimas", "en comentarios sin nombre", "Los profesionales de salud entregan información respaldada."),
   ("abc", "Una persona dice «no hace falta preguntar si la otra persona está de acuerdo». ¿Qué corresponde responder?", "Toda relación necesita consentimiento libre", "Tiene razón", "Basta con el silencio", "Sin acuerdo libre, no hay consentimiento y no corresponde seguir."),
   ("abc", "Se lee en una cadena «los vasos compartidos transmiten infecciones de transmisión sexual». ¿Qué conviene hacer?", "contrastarlo con una fuente confiable de salud", "reenviarlo", "creerlo sin revisar", "Una afirmación de salud se comprueba con una fuente confiable."),
   ("abc", "Alguien afirma «las hormonas son alimentos». ¿Cuál es el error?", "Las hormonas son mensajeros químicos, no alimentos", "Están bien definidas", "Son órganos", "Las hormonas regulan funciones del cuerpo y las produce el propio organismo."),
   ("abc", "{F} Si un folleto dice «gestar un embarazo», ¿a qué función del sistema reproductor se refiere?", "a la reproducción", "a la digestión", "a la respiración", "Gestar es parte del proceso de reproducción."),
   ("abc", "Dos amistades discuten un mito. ¿Qué paso es correcto?", "buscar una fuente confiable y revisar qué dice", "gana quien habla más fuerte", "creerle a quien tiene más seguidores", "La evidencia de una fuente confiable resuelve la duda."),
   ("abc", "¿Cuál de estas es una buena práctica de privacidad al conversar sobre salud sexual?", "conversar con un profesional en un espacio privado", "contarlo en voz alta en un lugar público", "publicarlo en una red social", "La privacidad protege a la persona y facilita preguntar con confianza.")],
  ("abc", "En una charla comunitaria, un folleto de ejemplo dice «consulta en el centro de salud ante dudas sobre salud sexual». ¿Qué tipo de recomendación es?", "una orientación general que respeta la privacidad", "un diagnóstico personal", "un tratamiento", "Orienta a buscar a un profesional sin indicar nada personal."),
  [("En Ciencias: ¿qué son los gametos?", "Las células sexuales: óvulo y espermatozoide", "Participan en la reproducción junto con las hormonas del cuerpo."),
   ("En salud sexual: ¿qué significa consentimiento?", "Un acuerdo libre de las personas involucradas", "Sin ese acuerdo no corresponde seguir."),
   ("En información de salud: ¿qué es un mito?", "Una idea falsa que se repite", "Se separa del hecho con una fuente confiable.")],
  ("Con las cuatro frases de la ficha, escribe para cada una si es un hecho o un mito, y para la frase que sea un mito escribe cómo la reemplazarías por una frase correcta. Indica dónde buscarías información confiable.",
   "Frase 1: hecho. Frase 2: hecho. Frase 3: hecho. Frase 4: mito; correcta: «las infecciones de transmisión sexual no se pasan por compartir un vaso». Buscaría en un centro de salud.",
   ["clasifica las cuatro frases", "corrige el mito", "nombra una fuente confiable"],
   ["Identifica la frase 4 como mito.", "La corrección es correcta.", "Menciona una fuente confiable."],
   "Si marca todas como hechos, pregunta qué dice una fuente de salud sobre compartir un vaso. Si no nombra fuente, recuerda el centro de salud."),
  "Escribe una definición de consentimiento con tus palabras.",
  "Escribe tres criterios para separar un hecho de un mito en temas de salud.")

# ====================================================== OAD-04 clase 2
F = ("Ficha 2 (cuadro de estructuras de ejemplo). Sistema reproductor femenino: ovarios (gónadas que producen óvulos y hormonas), trompas de Falopio (conducen el óvulo; ahí puede ocurrir la fecundación), útero (donde se desarrolla un embarazo) y vagina (canal de salida). "
     "Sistema reproductor masculino: testículos (gónadas que producen espermatozoides y hormonas), conductos deferentes (llevan los espermatozoides), próstata y vesículas seminales (aportan líquido), uretra (conducto de salida) y pene.")
K(2, F,
  "Hoy reconoceré las estructuras de los sistemas reproductores femenino y masculino y la función de cada una, incluidas las gónadas.",
  ["Las gónadas son los órganos que producen los gametos y las hormonas. En el sistema femenino son los ovarios, que producen óvulos. En el masculino son los testículos, que producen espermatozoides. Las demás estructuras conducen, protegen o ayudan en la reproducción.",
   "En el sistema femenino, las trompas de Falopio conducen el óvulo hasta el útero, y es en ellas donde puede ocurrir la fecundación, la unión de un óvulo con un espermatozoide. El útero es el órgano donde se desarrolla un embarazo. La vagina es un canal que comunica el útero con el exterior.",
   "En el sistema masculino, los espermatozoides salen de los testículos por los conductos deferentes. La próstata y las vesículas seminales aportan líquido que forma el semen junto con los espermatozoides. La uretra es el conducto de salida. Cada estructura tiene una función y todas se cuidan con higiene y controles de salud."],
  [("gónada", "órgano que produce gametos y hormonas"), ("fecundación", "unión de un óvulo con un espermatozoide"), ("útero", "órgano donde se desarrolla un embarazo"), ("testículo", "gónada masculina que produce espermatozoides")],
  [("Ubicar una gónada", "¿Cuál es la gónada femenina?", ["Las gónadas producen gametos y hormonas.", "Producen óvulos: son los ovarios."], "Los ovarios"),
   ("Identificar una función", "¿Qué hace el útero?", ["La ficha dice que ahí se desarrolla un embarazo.", "Su función es alojar el desarrollo."], "Es donde se desarrolla un embarazo")],
  [("Confundir ovarios con útero.", "Se mezclan el órgano que produce óvulos con el órgano de desarrollo.", "Ovarios producen óvulos; el útero aloja el embarazo."),
   ("Decir que la fecundación ocurre en el útero.", "Se olvida que puede ocurrir en las trompas.", "En las trompas de Falopio puede darse la unión del óvulo con el espermatozoide.")],
  [("abc", "{F} ¿Qué estructura produce los óvulos?", "los ovarios", "el útero", "la próstata", "Los ovarios son la gónada femenina y producen óvulos."),
   ("abc", "{F} ¿Qué estructura produce los espermatozoides?", "los testículos", "los ovarios", "la uretra", "Los testículos son la gónada masculina."),
   ("abc", "{F} ¿Dónde puede ocurrir la fecundación?", "en las trompas de Falopio", "en el estómago", "en los pulmones", "La ficha indica que la fecundación puede ocurrir en las trompas."),
   ("abc", "{F} ¿Qué es la fecundación?", "la unión de un óvulo con un espermatozoide", "la producción de leche", "la salida de la orina", "Es el encuentro de dos gametos."),
   ("abc", "{F} ¿Dónde se desarrolla un embarazo?", "en el útero", "en la próstata", "en la uretra", "El útero aloja el desarrollo del embarazo."),
   ("abc", "{F} ¿Qué estructuras aportan líquido para formar el semen?", "la próstata y las vesículas seminales", "los ovarios", "las trompas", "La ficha dice que aportan líquido junto con los espermatozoides."),
   ("abc", "¿Qué tienen en común ovarios y testículos?", "son gónadas que producen gametos y hormonas", "son parte del sistema digestivo", "son vasos sanguíneos", "Ambos órganos producen gametos y también hormonas."),
   ("abc", "Alguien dice «los ovarios son parte del sistema masculino». ¿Cuál es el error?", "Los ovarios son parte del sistema femenino", "No hay error", "Son parte del respiratorio", "Los ovarios producen óvulos y forman parte del sistema femenino."),
   ("abc", "Alguien afirma «la fecundación ocurre en la vagina». Según la ficha, ¿qué corresponde responder?", "La ficha indica que puede ocurrir en las trompas de Falopio", "Tiene razón", "Ocurre en el esófago", "Las trompas son el lugar de la fecundación."),
   ("abc", "¿Por qué se dice que los sistemas reproductores se cuidan con higiene y controles de salud?", "Porque son parte de la salud general y los profesionales pueden orientar", "Porque solo se cuidan cuando hay dolor", "Porque son órganos que no necesitan atención", "Cuidarlos es parte del autocuidado y de la prevención."),
   ("abc", "¿Cuál es el orden en que salen los espermatozoides hasta la uretra?", "testículos, conductos deferentes, uretra", "uretra, testículos, conductos deferentes", "conductos deferentes, uretra, testículos", "La ficha los presenta saliendo del testículo por los conductos hasta la uretra."),
   ("abc", "Se unen en una tabla las funciones: ovarios, útero, trompas. ¿Cuál función corresponde a las trompas?", "conducen el óvulo", "producen espermatozoides", "producen semen", "Las trompas conducen el óvulo y allí puede ocurrir la fecundación."),
   ("abc", "¿Cuál de estos es un órgano de ayuda para el semen?", "la próstata", "el útero", "el ovario", "La próstata aporta líquido que forma parte del semen.")],
  ("abc", "En un folleto de ejemplo del centro de salud se explica «los ovarios producen óvulos y hormonas». ¿Qué nivel de organización son los ovarios?", "órgano", "célula", "organismo", "Los ovarios están formados por varios tejidos y cumplen una función: son órganos."),
  [("En Ciencias: ¿qué es una gónada?", "Un órgano que produce gametos y hormonas", "Son los ovarios y los testículos."),
   ("En Ciencias: ¿qué es la fecundación humana?", "La unión de un óvulo con un espermatozoide", "Puede ocurrir en las trompas de Falopio."),
   ("¿Para qué sirve el útero?", "Para el desarrollo de un embarazo", "Es el órgano donde se aloja.")],
  ("Con los dos cuadros de la ficha, dibuja un esquema simple de cada sistema (femenino y masculino) con los rótulos que ya conoces, y escribe al lado de cada rótulo su función en una frase corta.",
   "Femenino: ovarios (producen óvulos), trompas (conducen el óvulo), útero (aloja el embarazo), vagina (canal). Masculino: testículos (producen espermatozoides), conductos deferentes (llevan espermatozoides), próstata (aporta líquido), uretra (salida).",
   ["rotula las estructuras de los dos sistemas", "escribe una función por cada una", "ubica las gónadas"],
   ["Los rótulos son correctos.", "Las funciones coinciden con la ficha.", "Se identifican ovarios y testículos como gónadas."],
   "Si confunde ovarios y útero, pregunta qué produce cada uno. Si omite una gónada, pregunta cuál produce los gametos."),
  "Escribe qué estructuras producen gametos y cuáles solo conducen o ayudan.",
  "Explica con tus palabras por qué ovarios y testículos se llaman gónadas.")

# ====================================================== OAD-04 clase 3
F = ("Ficha 3 (cuadro de ejemplo). Infecciones de transmisión sexual (ITS): infecciones que se pasan principalmente por contacto sexual, sobre todo cuando no se usa protección; algunas también pasan por la sangre o de la madre al bebé. Pueden ser causadas por bacterias (como la sífilis, la gonorrea y la clamidia) o por virus (como el VIH, el virus del papiloma humano y el herpes). "
     "Algunas no dan síntomas. Prevención general: usar preservativo de forma correcta en cada relación, vacunarse contra el virus del papiloma humano según el calendario de salud, consultar y hacerse exámenes en un centro de salud y conversar con respeto. "
     "No se transmiten por abrazos, saludos ni por compartir vasos. Autocuidado: controles de salud periódicos según indique un profesional.")
K(3, F,
  "Hoy investigaré enfermedades del sistema reproductor, en especial las infecciones de transmisión sexual: cómo se pasan, cómo se previenen y dónde pedir orientación.",
  ["Las infecciones de transmisión sexual, o ITS, se pasan principalmente por contacto sexual, sobre todo cuando no se usa protección; algunas también pasan por la sangre o de la madre al bebé. Las causan bacterias, como en la sífilis, la gonorrea y la clamidia, o virus, como el VIH, el virus del papiloma humano y el herpes. Algunas no dan síntomas, y por eso los exámenes son importantes.",
   "Hay mitos que conviene corregir. Las ITS no se transmiten por abrazos, saludos, compartir vasos o usar el mismo baño. Una persona con una ITS merece respeto y atención: el estigma impide consultar a tiempo. El diagnóstico y el tratamiento los define un profesional de salud.",
   "La prevención general incluye usar preservativo de forma correcta en cada relación (reduce el riesgo, pero no lo elimina por completo), vacunarse contra el virus del papiloma humano según el calendario de salud, hacerse exámenes y conversar con respeto. También hay otras enfermedades del sistema reproductor, que se detectan con controles de salud según indique un profesional."],
  [("ITS", "infección de transmisión sexual"), ("preservativo", "funda que reduce el riesgo de transmisión de muchas ITS si se usa bien"), ("estigma", "rechazo injusto hacia una persona por tener una enfermedad"), ("vacuna", "preparado que ayuda al cuerpo a defenderse de ciertas infecciones")],
  [("Distinguir hecho de mito", "Alguien dice «las ITS se pasan por un abrazo». ¿Es hecho o mito?", ["La ficha dice que no se transmiten por abrazos.", "Es un mito."], "Es un mito"),
   ("Reconocer una medida", "¿Qué medida de la ficha se asocia al virus del papiloma humano?", ["Hay una vacuna según el calendario de salud.", "La vacuna ayuda a prevenir esa infección."], "La vacunación")],
  [("Pensar que sin síntomas no hay infección.", "Algunas ITS no dan síntomas.", "Los exámenes de un centro de salud detectan lo que no se siente."),
   ("Rechazar o burlarse de una persona con una ITS.", "El estigma impide que se consulte a tiempo.", "Trata con respeto: son enfermedades, no un castigo.")],
  [("abc", "{F} ¿Cómo se pasan principalmente las ITS?", "por contacto sexual, sobre todo sin protección", "por compartir un vaso", "por un saludo", "La ficha indica el contacto sexual sin protección."),
   ("abc", "{F} ¿Cuál de estos agentes causa una ITS según la ficha?", "bacterias o virus", "solo el frío", "solo el polvo", "La ficha indica que las causan bacterias o virus."),
   ("abc", "{F} ¿Cuál de estas medidas de prevención aparece en la ficha?", "usar preservativo de forma correcta en cada relación", "compartir los vasos", "evitar los exámenes", "Es una medida de prevención de la ficha."),
   ("abc", "{F} ¿Se transmiten las ITS por compartir un vaso?", "no", "sí", "solo si hay síntomas", "La ficha dice que no se transmiten por compartir vasos."),
   ("abc", "{F} ¿Por qué son importantes los exámenes?", "porque algunas ITS no dan síntomas", "porque todas duelen", "porque así se evitan los controles de salud", "Sin síntomas no se pueden detectar a simple vista."),
   ("abc", "¿Cuál es el efecto del estigma hacia una persona con una ITS?", "puede impedir que consulte a tiempo", "ayuda a prevenir", "cura la infección", "El rechazo hace que la persona evite pedir ayuda."),
   ("abc", "¿Quién define el diagnóstico y el tratamiento de una ITS?", "un profesional de salud", "un mensaje de una cadena", "una conversación al azar", "El profesional puede evaluar cada caso."),
   ("abc", "Alguien dice «si no tengo síntomas, no necesito consultar nunca». ¿Qué corresponde responder?", "Algunas ITS no dan síntomas, por eso los controles son útiles", "Tiene razón", "Los controles no sirven", "Un examen puede detectar infecciones que no se notan."),
   ("abc", "Un cuadro de ejemplo clasifica: sífilis, clamidia, gonorrea. ¿Qué tienen en común?", "las causan bacterias", "las causan virus", "no se pasan", "La ficha las nombra como causadas por bacterias."),
   ("abc", "Un cuadro de ejemplo clasifica: VIH, herpes, virus del papiloma humano. ¿Qué tienen en común?", "las causan virus", "las causan bacterias", "no son ITS", "La ficha las nombra como causadas por virus."),
   ("abc", "Se dice «las ITS son un castigo». ¿Cuál es el error?", "Son enfermedades; el rechazo no ayuda a prevenirlas", "No hay error", "Son siempre culpa de quien las tiene", "La ciencia las describe como infecciones, no como castigos."),
   ("abc", "Una persona quiere saber más sobre prevención. ¿Qué conviene hacer?", "consultar en un centro de salud, de forma privada", "pedirlo en una cadena anónima", "preguntar a quien no sabe", "Un profesional entrega información confiable y cuida la privacidad."),
   ("abc", "¿Cuál es una medida general de autocuidado del sistema reproductor?", "asistir a controles de salud periódicos según indique un profesional", "evitar siempre consultar", "creer cualquier cadena", "Los controles ayudan a detectar a tiempo y a recibir orientación.")],
  ("abc", "En un afiche de un centro de salud de ejemplo se lee «la información es prevención; consulta». ¿Qué propone?", "informarse y consultar de forma confiable", "diagnosticarse con una cadena", "ignorar el tema", "Es una invitación general a prevenir con información confiable."),
  [("En Ciencias: ¿qué es una ITS?", "Una infección que se pasa principalmente por contacto sexual sin protección", "Pueden causarlas bacterias o virus, según la infección."),
   ("¿Qué es el estigma?", "Rechazo injusto hacia una persona por tener una enfermedad", "Impide que la persona consulte a tiempo."),
   ("¿Se transmiten las ITS por abrazos?", "No", "La ficha lo descarta de manera explícita.")],
  ("Con la ficha 3, arma un cuadro con tres filas: una ITS causada por bacterias, una causada por virus y una medida de prevención. Escribe una frase respetuosa que invite a consultar en un centro de salud.",
   "Sífilis: bacterias. VIH: virus. Prevención: preservativo bien usado y vacuna contra el virus del papiloma humano según el calendario. Frase: «Consultar a tiempo es cuidarse».",
   ["completa las tres filas con datos de la ficha", "incluye una frase respetuosa", "no da indicaciones de tratamiento"],
   ["Cada ITS está en el grupo correcto.", "La frase es respetuosa.", "No receta ni diagnostica."],
   "Si indica un tratamiento, recuerda que lo define un profesional. Si usa lenguaje de rechazo, reemplázalo por una frase respetuosa."),
  "Escribe dos mitos sobre las ITS y su corrección.",
  "Explica por qué el respeto es parte de la prevención.")

# ====================================================== OAD-04 clase 4
F = ("Ficha 4 (datos de ejemplo, inventados). Casos informados de una infección ficticia «X» en un centro de salud de ejemplo. Año 1: 40. Año 2: 32. Año 3: 36. Año 4: 44. Año 5: 48. "
     "Gráfico de barras en texto (cada ■ vale 4 casos): Año 1 ■■■■■■■■■■ (40). Año 2 ■■■■■■■■ (32). Año 3 ■■■■■■■■■ (36). Año 4 ■■■■■■■■■■■ (44). Año 5 ■■■■■■■■■■■■ (48).")
K(4, F,
  "Hoy analizaré datos de ejemplo sobre una enfermedad del sistema reproductor: leer tablas y gráficos, describir tendencias y calcular diferencias y promedios.",
  ["Analizar datos es leer una tabla o un gráfico, comparar valores y describir lo que se ve. Una tendencia es la dirección general de los datos en el tiempo: puede aumentar, disminuir o mantenerse. La ficha tiene datos inventados, rotulados como de ejemplo, para practicar.",
   "Para describir una tendencia se comparan valores en orden. En la ficha, del año 1 al año 2 los casos bajan; después suben cada año. Una diferencia se calcula restando. Un promedio se calcula sumando todos los datos y dividiendo por la cantidad de datos.",
   "Al interpretar hay que ser prudente. Una tendencia en datos de ejemplo no dice nada sobre la vida real. Y aun con datos reales, un aumento de casos puede deberse a más exámenes realizados, no solo a más infecciones. Se evita afirmar causas sin evidencia."],
  [("tendencia", "dirección general de los datos en el tiempo"), ("diferencia", "resultado de restar dos valores"), ("promedio", "suma de los datos dividida por cuántos son"), ("gráfico de barras", "gráfico donde cada barra representa un valor")],
  [("Describir una tendencia", "Los casos por año fueron 20, 25, 30 y 35 (datos de ejemplo). ¿Cuál es la tendencia?", ["Cada año hay más casos que el anterior.", "La tendencia es aumentar."], "Aumenta"),
   ("Calcular una diferencia", "Con esos datos de ejemplo, ¿cuántos casos más hubo en el último año que en el primero?", ["Se compara 35 con 20.", "Se resta: 35 − 20 = 15."], "15 casos")],
  [("Decir que hay tendencia con solo dos datos.", "Dos datos no muestran una dirección sostenida.", "Observa varios datos seguidos antes de hablar de tendencia."),
   ("Afirmar la causa de un aumento sin evidencia.", "No se sabe si hubo más infecciones o más exámenes.", "Describe lo observado y evita afirmar causas sin datos.")],
  [("abc", "{F} ¿Cuántos casos se informaron en el año 3?", "36", "32", "44", "La tabla indica 36 para el año 3."),
   ("abc", "{F} ¿Qué pasó entre el año 1 y el año 2?", "los casos bajaron", "los casos subieron", "no hubo cambios", "Pasaron de 40 casos a 32 casos."),
   ("abc", "{F} ¿Cuál es la tendencia entre el año 2 y el año 5?", "aumenta", "disminuye", "se mantiene", "Los valores van 32, 36, 44 y 48: cada año es mayor."),
   ("=", "{F} ¿Cuántos casos más hubo en el año 5 que en el año 1?", "48-40", "Se resta el valor del año 1 al del año 5.", " casos"),
   ("=", "{F} ¿Cuántos casos hubo en total entre los cinco años?", "40+32+36+44+48", "Se suman los casos de los cinco años.", " casos"),
   ("=", "{F} ¿Cuál es el promedio de casos por año?", "(40+32+36+44+48)//5", "Se suma y se divide por los 5 años.", " casos"),
   ("abc", "{F} En el gráfico de barras en texto, ¿cuántas ■ tiene el año 4?", "11", "10", "12", "Cada ■ vale 4 y 44 dividido por 4 son 11."),
   ("abc", "¿Cuál es la mejor descripción de los datos de la ficha?", "bajaron del año 1 al 2 y luego subieron cada año", "subieron siempre", "bajaron siempre", "Los datos muestran un descenso inicial y después un aumento sostenido."),
   ("=", "{F} ¿Cuántos casos más hubo en el año 4 que en el año 3?", "44-36", "Se restan los casos del año 3 a los del año 4.", " casos"),
   ("abc", "Alguien dice «el aumento prueba que ahora hay más infecciones». ¿Qué falta para afirmarlo?", "Saber si cambió el número de exámenes realizados", "Nada, está probado", "Más colores en el gráfico", "Un aumento de casos informados puede deberse a más exámenes."),
   ("abc", "Una persona dice «estos datos de ejemplo muestran la situación real del país». ¿Cuál es el error?", "Son datos inventados para practicar", "Son datos reales", "Son datos del año actual", "Los datos de ejemplo no describen la realidad."),
   ("abc", "Se quiere comparar una barra de 11 ■ con otra de 8 ■ (cada ■ vale 4). ¿Cuántos casos más tiene la primera?", "12", "3", "4", "La diferencia son 3 barras y 3 × 4 son 12 casos."),
   ("abc", "Se dice «hubo tendencia porque dos años subieron». ¿Cuál es el error?", "Se necesitan varios datos seguidos para hablar de tendencia", "No hay error", "Dos datos siempre alcanzan", "Con pocos datos puede ser una variación al azar.")],
  ("abc", "En una reunión comunitaria de ejemplo se muestra un gráfico de casos de una infección y una persona dice «la tendencia aumenta». ¿Qué debe revisar antes de aceptarlo?", "si los datos son seguidos y de una fuente confiable", "si el gráfico tiene colores", "si es largo", "Para afirmar una tendencia se necesitan varios datos seguidos y una fuente confiable."),
  [("En Ciencias: ¿qué es una tendencia?", "La dirección general de los datos en el tiempo", "Puede aumentar, disminuir o mantenerse a lo largo del tiempo."),
   ("¿Cómo se calcula una diferencia?", "Restando un valor a otro", "Se obtiene cuánto más o cuánto menos."),
   ("En análisis de datos: ¿cómo se calcula un promedio?", "Se suman los datos y se divide por cuántos son", "Resume varios datos en un solo valor para comparar.")],
  ("Con estos datos de ejemplo: Año 1: 50 casos, Año 2: 45, Año 3: 40, Año 4: 38, escribe en tres líneas: la tendencia, cuántos casos menos hubo en el año 4 respecto del año 1, y una frase prudente sobre qué no puedes afirmar.",
   "La tendencia es disminuir. Hubo 12 casos menos en el año 4 que en el año 1. No puedo afirmar la causa de la disminución ni que ocurra en la vida real: son datos de ejemplo.",
   ["describe la tendencia", "calcula la diferencia", "incluye una frase prudente"],
   ["La tendencia está bien descrita.", "La diferencia es correcta.", "No afirma causas sin evidencia."],
   "Si afirma una causa, pregunta qué dato la sostiene. Si calcula mal, pídele que escriba la resta."),
  "Calcula el promedio de estos datos de ejemplo: 10, 20 y 30.",
  "Inventa una tabla de cuatro años con una tendencia que aumenta y descríbela.")

# ====================================================== OAD-04 clase 5
F = ("Ficha 5 (informe comunitario de ejemplo; datos inventados). Un centro de salud de ejemplo registró cuántas personas pidieron una consulta preventiva por trimestre. "
     "Trimestre 1: 25. Trimestre 2: 27. Entre el trimestre 2 y el 3 se realizó una campaña informativa. Trimestre 3: 38. Trimestre 4: 45. "
     "Total de personas atendidas en el año: 135.")
K(5, F,
  "Hoy aplicaré el análisis de datos a una situación comunitaria: leer un informe de una campaña informativa, comparar antes y después y sacar conclusiones prudentes.",
  ["Una campaña informativa busca que más personas conozcan una medida de prevención. Para ver si hubo cambio, se comparan los datos antes y después de la campaña. En la ficha, los trimestres 1 y 2 son antes, y los trimestres 3 y 4, después.",
   "Una forma de comparar es calcular el promedio de cada periodo. Otra es calcular la diferencia entre el último y el primer valor. Con esas cifras se puede decir si las consultas aumentaron. Pero el informe no prueba que la campaña fue la causa: pudo haber otros motivos.",
   "Una conclusión prudente dice qué se observó, con cifras, y reconoce lo que no se sabe. Por ejemplo: «después de la campaña las consultas fueron mayores, pero con estos datos no se puede asegurar que fue por la campaña». Los datos son de ejemplo y la privacidad de las personas se protege siempre."],
  [("campaña informativa", "actividad para dar a conocer una medida de prevención"), ("antes y después", "comparación de datos de dos periodos"), ("conclusión prudente", "afirmación que se limita a lo que muestran los datos"), ("privacidad", "protección de los datos personales")],
  [("Comparar antes y después", "Antes de una campaña de ejemplo hubo 20 y 30 consultas. Después hubo 40 y 50. ¿Aumentaron?", ["Antes: 20 y 30; después: 40 y 50.", "Todos los valores después son mayores."], "Sí, aumentaron"),
   ("Calcular un promedio", "¿Cuál es el promedio de consultas de 40 y 50?", ["Se suman: 40 + 50 = 90.", "Se divide por 2: 45."], "45 consultas")],
  [("Afirmar que la campaña fue la causa del aumento.", "No se descartaron otros motivos.", "Usa una frase prudente: «después de la campaña, aumentaron»."),
   ("Comparar periodos de distinta duración como si fueran iguales.", "Los números no son comparables.", "Usa periodos de igual duración, como trimestres.")],
  [("=", "{F} ¿Cuántas consultas hubo en total antes de la campaña (trimestres 1 y 2)?", "25+27", "Se suman las consultas de los dos trimestres.", " consultas"),
   ("=", "{F} ¿Cuántas consultas hubo en total después de la campaña (trimestres 3 y 4)?", "38+45", "Se suman las consultas de los dos trimestres.", " consultas"),
   ("=", "{F} ¿Cuántas consultas más hubo después que antes de la campaña?", "(38+45)-(25+27)", "Se restan los totales: después menos antes.", " consultas"),
   ("abc", "{F} ¿Qué trimestre tuvo más consultas?", "el trimestre 4", "el trimestre 1", "el trimestre 2", "El trimestre 4 tuvo 45, el valor más alto."),
   ("abc", "{F} ¿Cuál es la tendencia general de los cuatro trimestres?", "aumenta", "disminuye", "se mantiene", "Los valores 25, 27, 38 y 45 crecen en orden."),
   ("=", "{F} ¿Cuántas consultas más hubo en el trimestre 4 que en el trimestre 1?", "45-25", "Se resta el valor del trimestre 1 al del 4.", " consultas"),
   ("abc", "{F} ¿Cuál es la conclusión prudente?", "Después de la campaña hubo más consultas, pero los datos no prueban que la campaña fue la única causa", "La campaña fue la única causa", "No hubo cambio", "Se describe lo observado sin afirmar una causa sin evidencia."),
   ("abc", "Alguien dice «las consultas aumentaron, así que la campaña es la causa segura». ¿Qué corresponde responder?", "Pudo haber otros motivos; los datos solo muestran que aumentaron", "Tiene razón", "No aumentaron", "Se observó un aumento, pero no se descartaron otras causas."),
   ("abc", "En un informe comunitario, ¿cuál es una práctica correcta con los datos de las personas?", "mostrar solo cifras y no nombres", "publicar nombres y motivos", "pedir el motivo de cada consulta en voz alta", "Se resguarda la privacidad mostrando solo totales."),
   ("abc", "Se compara un periodo de 3 meses con otro de 6 meses. ¿Qué problema hay?", "Los periodos no son de igual duración", "Son iguales", "Los meses no sirven", "Para comparar hay que usar periodos de igual duración."),
   ("abc", "Una persona calcula el promedio de consultas antes de la campaña sumando 25 y 27 y dividiendo por 3. ¿Cuál es el error?", "Debe dividir por 2, que es la cantidad de datos", "No debe sumar", "Debe restar", "El promedio divide la suma por cuántos datos hay."),
   ("abc", "Se dice «estos datos muestran cuántas personas reales se atendieron en el país». ¿Cuál es el error?", "Los datos son inventados y no demuestran nada real", "Tiene razón", "Los datos son del año pasado", "Los datos de ejemplo sirven solo para practicar el análisis."),
   ("abc", "¿Qué debe incluir una conclusión prudente?", "lo observado con cifras y lo que no se puede afirmar", "solo lo que gusta", "una causa segura", "Reconocer límites es parte de la honestidad científica.")],
  ("abc", "En una reunión comunitaria se presenta un informe como el de la ficha. ¿Qué pregunta ayuda a evaluarlo mejor?", "¿Se compararon periodos de igual duración y se evitó afirmar una causa sin evidencia?", "¿Tiene muchas ■?", "¿Está en colores?", "Esas preguntas permiten evaluar si el análisis es justo."),
  [("En Ciencias: ¿qué es una conclusión prudente?", "Una afirmación que se limita a lo que muestran los datos", "Reconoce lo que no se sabe."),
   ("¿Qué es una campaña informativa?", "Una actividad para dar a conocer una medida de prevención", "Se evalúa comparando antes y después."),
   ("¿Por qué se protege la privacidad?", "Porque los datos de las personas son personales", "Se muestran solo cifras, sin nombres.")],
  ("Con estos datos de ejemplo: antes de una campaña, 30 y 34 consultas; después, 41 y 45. Escribe: el promedio antes, el promedio después, la diferencia entre ambos promedios y una frase prudente.",
   "Promedio antes: 32. Promedio después: 43. Diferencia: 11 consultas. Frase: después de la campaña hubo más consultas, pero no se puede asegurar que fue la única causa.",
   ["calcula los dos promedios", "calcula la diferencia", "incluye una frase prudente"],
   ["Los promedios son correctos.", "La diferencia es correcta.", "La frase reconoce límites."],
   "Si afirma una causa, pregunta qué dato la sostiene. Si divide mal, pregunta cuántos datos hay."),
  "Calcula el promedio de estos datos de ejemplo: 12, 16 y 20 consultas.",
  "Escribe una frase prudente para un aumento de casos que podría deberse a más exámenes.")

# ====================================================== OAD-04 clase 6
F = ("Ficha 6 (autoevaluación de ejemplo). Frases escritas por una persona: 1) «Los ovarios producen espermatozoides». 2) «Las ITS se transmiten por abrazos». 3) «Una tendencia necesita varios datos seguidos». "
     "4) «El consentimiento se da en silencio». 5) «Un aumento de casos prueba la causa». Datos de ejemplo: Año 1: 60, Año 2: 66, Año 3: 72.")
K(6, F,
  "Hoy revisaré lo logrado: corregir frases sobre el sistema reproductor, las ITS y el análisis de datos, y decidir qué quiero seguir repasando.",
  ["Repasamos tres ideas. Primero, la estructura y función: los ovarios producen óvulos y los testículos espermatozoides, y ambos se llaman gónadas. Segundo, la prevención de las ITS: información, preservativo usado correctamente, vacunación según el calendario, exámenes y consulta con respeto.",
   "Tercero, el análisis de datos: se leen tablas y gráficos, se describe la tendencia, se calculan diferencias y promedios, y se evita afirmar causas sin evidencia. Los mitos se corrigen con fuentes confiables. Los datos de ejemplo sirven para practicar, no para describir la realidad.",
   "Revisar es leer lo que escribí como si fuera de otra persona, corregir y anotar qué me falta. Las dudas personales de salud se conversan con un profesional del centro de salud, con privacidad y respeto."],
  [("autoevaluación", "revisión de mi propio aprendizaje"), ("evidencia", "dato que respalda una afirmación"), ("fuente confiable", "origen de información con autoría, fecha y respaldo"), ("gónada", "órgano que produce gametos y hormonas")],
  [("Corregir una frase", "La frase «los ovarios producen espermatozoides» es incorrecta. ¿Cómo se corrige?", ["Los ovarios son la gónada femenina.", "Producen óvulos."], "Los ovarios producen óvulos"),
   ("Calcular una diferencia", "En los datos de ejemplo, de 60 a 72 casos, ¿cuántos casos más hubo?", ["Se resta: 72 − 60.", "La diferencia es 12."], "12 casos")],
  [("Dejar un error sin corregir por vergüenza.", "Se piensa que equivocarse es malo.", "Un error revisado es un aprendizaje."),
   ("Concluir una causa a partir de una tendencia.", "Una tendencia describe, no explica.", "Una conclusión prudente se limita a lo observado.")],
  [("abc", "{F} La frase 1 dice «Los ovarios producen espermatozoides». ¿Cómo se corrige?", "Los ovarios producen óvulos", "Los ovarios producen semen", "Los ovarios son parte del estómago", "Los espermatozoides los producen los testículos; los ovarios producen óvulos."),
   ("abc", "{F} La frase 2 dice «Las ITS se transmiten por abrazos». ¿Cuál es la corrección?", "Las ITS no se transmiten por abrazos", "Se transmiten por saludos", "Se transmiten por compartir vasos", "Las ITS se pasan principalmente por contacto sexual sin protección."),
   ("abc", "{F} La frase 3 dice «Una tendencia necesita varios datos seguidos». Esa frase es", "correcta", "incorrecta", "irrelevante", "Con pocos datos no se puede hablar de una tendencia."),
   ("abc", "{F} La frase 4 dice «El consentimiento se da en silencio». ¿Cuál es la corrección?", "El consentimiento es un acuerdo libre de las personas involucradas", "El silencio es consentimiento", "No se necesita acuerdo", "Sin acuerdo libre no hay consentimiento."),
   ("abc", "{F} La frase 5 dice «Un aumento de casos prueba la causa». ¿Cuál es la corrección?", "Un aumento describe lo observado, pero no prueba una causa", "Siempre prueba la causa", "Nunca hay aumentos", "Se necesita evidencia adicional para afirmar una causa."),
   ("=", "{F} ¿Cuántos casos más hubo en el año 3 que en el año 1?", "72-60", "Se resta el valor del año 1 al del año 3.", " casos"),
   ("=", "{F} ¿Cuál es el promedio de casos de los tres años?", "(60+66+72)//3", "Se suman los tres datos y se divide por 3.", " casos"),
   ("abc", "{F} ¿Cuál es la tendencia de los datos de ejemplo?", "aumenta", "disminuye", "se mantiene", "Los valores 60, 66 y 72 crecen cada año."),
   ("abc", "¿Qué estructura es la gónada masculina?", "los testículos", "los ovarios", "la vagina", "Los testículos producen espermatozoides y hormonas."),
   ("abc", "¿Qué se puede hacer ante una duda personal de salud sexual?", "conversar con un profesional del centro de salud", "preguntar en una cadena anónima", "ignorarla siempre", "Un profesional entrega orientación confiable y cuida la privacidad."),
   ("abc", "Una persona dice «equivocarme es motivo de vergüenza, mejor esconder mis errores». ¿Cuál es una mejor idea?", "Revisar mis errores ayuda a aprender", "Esconder los errores", "No revisar", "Corregir errores con evidencia es parte de aprender."),
   ("abc", "¿Cuál es un ejemplo de conclusión prudente con los datos de la ficha?", "«En los datos de ejemplo, los casos aumentaron cada año; no se puede afirmar la causa»", "«La causa es el clima»", "«Todos los años serán iguales»", "Describe lo observado y reconoce lo que no se sabe."),
   ("abc", "¿Qué debe incluir una buena autoevaluación?", "lo que logré y lo que me falta repasar", "solo lo que me gusta", "nada", "Reconocer lo logrado y lo que falta orienta el repaso.")],
  ("abc", "En una jornada del centro de salud, una persona repasa con un folleto: «información, respeto, consentimiento, prevención». ¿Qué le sirve para recordarlo?", "relacionar cada palabra con un ejemplo de la vida diaria", "memorizar sin comprender", "ignorar el folleto", "Relacionar con ejemplos facilita comprender y recordar."),
  [("En Ciencias: ¿qué es una autoevaluación?", "Una revisión de mi propio aprendizaje", "Sirve para decidir qué conviene repasar."),
   ("En una investigación: ¿qué es una evidencia?", "Un dato que respalda una afirmación", "Una conclusión se apoya en evidencia."),
   ("¿Qué son las gónadas?", "Los órganos que producen gametos y hormonas", "Son los ovarios y los testículos.")],
  ("Escribe un mini informe de cuatro líneas: 1) qué hace una gónada, 2) una medida de prevención de ITS, 3) la tendencia de los datos de ejemplo de la ficha 6 y 4) qué te falta repasar.",
   "Las gónadas producen gametos y hormonas. Una medida es usar preservativo de forma correcta y consultar en un centro de salud. En los datos de ejemplo, los casos aumentan cada año. Me falta repasar cómo se calcula un promedio.",
   ["explica qué hace una gónada", "nombra una medida de prevención de ITS", "describe la tendencia", "indica qué repasar"],
   ["La definición de gónada es correcta.", "La medida es de prevención.", "La tendencia es la correcta."],
   "Si la medida es un tratamiento, recuerda que eso lo define un profesional. Si falta la autoevaluación, pregunta qué le costó."),
  "Escribe dos preguntas que quieras conversar con un profesional del centro de salud sobre salud sexual y reproductiva.",
  "Explica con tus palabras por qué una tendencia no prueba una causa.")
