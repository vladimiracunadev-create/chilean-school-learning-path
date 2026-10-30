"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF05 (creación digital: valorar y comunicar el sentido de las expresiones de la lengua indígena en contextos
familiares y comunitarios) y OA LF06 (uso de recursos tecnológicos para contar y registrar experiencias
cotidianas y significativas en lengua indígena).

Criterio de autoría: todos los mensajes, guiones, fichas, nombres y experiencias de práctica son inventados, están
en castellano y se declaran como tales. Las únicas expresiones en lengua indígena son las ya atestiguadas (mari
mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana, maururu en rapa nui), con su ficha y
copiadas con su grafía exacta. No se escribe pronunciación, no se inventan frases en lengua indígena y no se afirma
cuándo, a quién ni en qué ocasiones se dice cada expresión: lo enseñan el educador/a tradicional y la comunidad.
En ambas unidades no se publica nada en internet, no se graba la voz ni la imagen de nadie sin permiso y todo
queda en el aula o en casa, con una persona adulta. Se enseñan criterios (propósito, permiso, acceso, privacidad,
almacenamiento) y no se nombra ninguna marca, aplicación ni programa. Las tareas se pueden hacer en papel.
"""
from __future__ import annotations

from student_content_lc4_b import FICHA_PAL, L, M, T, W
from student_lessons import arith, ex

LF5, LF6 = "LC04 OA LF05", "LC04 OA LF06"

# =================================================================== OA LF05 · creación digital
L(
    LF5, 1,
    materials="Lápiz y hoja. Las fichas y los mensajes están escritos aquí y son inventados. Si usas un aparato, solo con una persona adulta. " + FICHA_PAL,
    use="Aprenderé a definir un mensaje, para quién es y qué debo resguardar antes de crear algo digital. Sirve para comunicar el valor de una expresión de la lengua con respeto.",
    prior=["Sé usar las palabras de la ficha con su grafía.", "Sé que una creación tiene autoría y permiso."],
    explain=[
        "Una creación digital es un trabajo hecho con un aparato: puede ser un audio, una tarjeta con imagen o un texto escrito en pantalla. Antes de hacerla defino tres cosas. El mensaje es la idea única que quiero comunicar, por ejemplo «chaltumay es gracias». La audiencia es la persona o el grupo que lo va a ver o escuchar. El resguardo es lo que no pongo en mi creación para cuidar a otros.",
        "Las expresiones de una lengua se usan en la vida familiar y comunitaria: al saludar, al agradecer, al nombrar la casa o el agua. Valorarlas es reconocer que cada una dice algo de cómo un pueblo se relaciona con su mundo. Para qué ocasión sirve cada expresión, la enseñan el educador tradicional y la comunidad; yo comunico lo que me enseñaron.",
        "En el resguardo incluyo la voz y la cara de otras personas, datos personales como nombres completos o direcciones, y saberes que la comunidad no autorizó a compartir. Mi creación se queda en el aula o en casa: no se publica en internet.",
    ],
    vocab=[("mensaje", "la idea que quiero comunicar"), ("audiencia", "personas que van a ver o escuchar mi creación"), ("resguardo", "lo que dejo fuera para cuidar a otros"), ("creación digital", "trabajo hecho con un aparato, como un audio o una tarjeta"), ("expresión", "palabra o frase de una lengua")],
    worked=[
        W("Definir el mensaje", "Quiero hacer una tarjeta digital para agradecer a una visita. Palabra de la ficha: chaltumay (gracias en mapuzugun). ¿Cuál es el mensaje?", ["El mensaje es una sola idea.", "La idea es agradecer."], "«chaltumay es gracias»"),
        W("Qué debo resguardar", "Un compañero quiere poner en su audio la voz de su vecino sin avisar y su dirección. ¿Qué debe resguardar?", ["La voz de otra persona necesita permiso.", "La dirección es un dato personal."], "La voz del vecino y la dirección"),
    ],
    mistakes=[
        M("Poner varias ideas en una sola creación.", "El mensaje se pierde.", "Elijo una sola idea."),
        M("Incluir datos personales «porque es mi casa».", "Otras personas podrían usarlos.", "Los dejo fuera como parte del resguardo."),
    ],
    R=[
        ex("El mensaje es: A) la idea que quiero comunicar B) el aparato que uso.", "A", "El mensaje es la idea."),
        ex("La audiencia es: A) quien va a ver o escuchar mi creación B) quien la fabricó.", "A", "Audiencia significa quién la recibe."),
        ex("Según la ficha, «chaltumay» significa: A) gracias B) sol.", "A", "La ficha dice gracias en mapuzugun."),
    ],
    C=[
        ex("Verdadero o falso: puedo publicar en internet mi creación sin preguntar.", "Falso", "Mi creación se queda en el aula o en casa."),
        ex("El resguardo incluye: A) lo que dejo fuera para cuidar a otros B) lo que pongo más grande.", "A", "Resguardo es cuidado."),
        ex("Voz de un familiar en mi audio: ¿necesito permiso o no hace falta?", "necesito permiso", "Su voz es suya."),
    ],
    A=[
        ex("Quiero hacer una tarjeta para agradecer a una visita. ¿Quién es la audiencia: la visita o el dibujo de la tarjeta?", "la visita", "La audiencia es la persona que va a ver o escuchar la creación."),
        ex("Mensaje: «iorana es un saludo en rapa nui». Audiencia: mi curso. ¿Qué lengua se menciona?", "rapa nui", "La ficha dice que iorana es rapa nui."),
        arith("Un curso hace 4 tarjetas con 2 datos de resguardo cada una. ¿Cuántos datos de resguardo hay?", "4 * 2", "Multiplico tarjetas por datos."),
    ],
    Z=[
        ex("Dos mensajes: 1) «chaltumay es gracias» 2) «chaltumay es gracias, el antü es sol, la ruka es casa y hoy llueve». ¿Cuál tiene un mensaje más claro?", "1", "Una sola idea se entiende mejor."),
        ex("Rita quiere poner la foto de su compañero en una tarjeta. ¿Qué debe hacer primero: A) pedir permiso B) cambiar el color?", "A", "La imagen de otra persona necesita permiso."),
    ],
    D=[
        arith("Un grupo tiene 12 ideas posibles y elige 1 mensaje. ¿Cuántas ideas deja fuera?", "12 - 1", "Elegir uno deja las demás fuera."),
        ex("Una persona dice que cada expresión sirve para cualquier momento. ¿Qué debe hacer: A) consultar al educador tradicional cuándo se usa B) afirmarlo sin saber?", "A", "El uso lo enseña quien conoce la lengua."),
    ],
    context=[ex("Quieres hacer una tarjeta para decir gracias a una visita. ¿Qué eliges como mensaje: «chaltumay es gracias» o «todas las palabras que sé»?", "«chaltumay es gracias»", "Una sola idea clara.")],
    selfcheck=[
        ex("¿Cómo se llama la idea que quiero comunicar?", "mensaje", "Es el mensaje."),
        ex("¿Qué tres cosas defino antes de crear?", "mensaje, audiencia y resguardo", "Son los tres pasos de la clase."),
        ex("¿Dónde queda mi creación?", "en el aula o en casa", "No se publica en internet."),
    ],
    task=T(
        "Planifica en papel una tarjeta digital para agradecer a una visita inventada. Escribe: tu mensaje (una sola idea con una palabra de la ficha), tu audiencia y tres cosas que dejarás fuera como resguardo. Si usas un aparato, hazlo con una persona adulta y no publiques nada.",
        "Mensaje: chaltumay es gracias en mapuzugun. Audiencia: mi curso. Resguardo: no pongo fotos de mis compañeros, no pongo direcciones, no pongo voces ajenas.",
        ["escribe un mensaje claro", "nombra la audiencia", "enumera tres cosas de resguardo"],
        ["plan escrito en el cuaderno"],
        ["incluir datos personales", "poner muchas ideas"],
        "Valora que el mensaje sea único y el resguardo claro; si incluyó datos personales, pídele que los quite.",
    ),
    reinforce="Di en voz alta tu mensaje, tu audiencia y una cosa que dejarías fuera.",
    extend="Explica a una persona de tu casa por qué no se publica una creación sin pensarlo.",
)

L(
    LF5, 2,
    materials="Lápiz y hoja. Las fichas de recursos están escritas aquí y son inventadas. " + FICHA_PAL,
    use="Aprenderé a elegir recursos para mi creación (imágenes, sonidos, textos) solo cuando tengo permiso. Sirve para respetar la autoría de otras personas.",
    prior=["Sé definir mensaje, audiencia y resguardo.", "Sé que toda creación tiene autoría."],
    explain=[
        "Un recurso es algo que uso para armar mi creación: una imagen, un sonido o un texto. Antes de usarlo me pregunto tres cosas: ¿quién lo hizo?, ¿tengo permiso? y ¿pertenece a una comunidad? Si alguna respuesta es «no sé», no lo uso.",
        "Los recursos más seguros son los míos: un dibujo hecho por mí, un texto que escribí o mi propia voz con permiso de una persona adulta. También puedo usar los recursos que el educador tradicional o la escuela me entregan con permiso. Siempre anoto la autoría: quién lo hizo.",
        "No uso grabaciones, cantos, símbolos ni imágenes de una comunidad sin su permiso, aunque estén a mi alcance. Que algo esté en internet no significa que sea libre. Si dudo, pregunto al educador tradicional.",
    ],
    vocab=[("recurso", "imagen, sonido o texto que uso en mi creación"), ("permiso", "aviso claro de que sí puedo usar algo"), ("autoría", "quién hizo un recurso"), ("libre", "que cualquiera puede usar sin pedir permiso"), ("comunidad", "grupo que comparte territorio y cultura")],
    worked=[
        W("Elegir un recurso seguro", "Fichas inventadas. A) Un dibujo hecho por mí. B) Un canto de una comunidad que encontré sin saber de dónde venía. ¿Cuál puedo usar?", ["A lo hice yo.", "B no tiene permiso ni procedencia."], "A"),
        W("Anotar la autoría", "Camila usa un dibujo de su compañera Nora con permiso de Nora. ¿Qué debe anotar?", ["Anota quién lo hizo.", "Escribe que el dibujo es de Nora."], "Que el dibujo es de Nora"),
    ],
    mistakes=[
        M("Pensar que si algo está en internet es libre.", "Tiene autor y puede tener comunidad.", "Pregunto antes de usarlo."),
        M("No anotar quién hizo el recurso.", "La autoría se pierde.", "Anoto la autoría en mi plan."),
    ],
    R=[
        ex("Un recurso es: A) algo que uso en mi creación B) una persona.", "A", "Imagen, sonido o texto son recursos."),
        ex("Un dibujo que hice yo, ¿es un recurso seguro: sí o no?", "sí", "Lo hice yo."),
        ex("Si no sé quién hizo un sonido, ¿lo uso o no lo uso?", "no lo uso", "No hay permiso ni procedencia."),
    ],
    C=[
        ex("Verdadero o falso: todo lo que está en internet es libre para usar.", "Falso", "Puede tener autoría y permisos."),
        ex("¿Qué anoto de un recurso que uso: la autoría o el peso del archivo?", "la autoría", "La autoría dice quién lo hizo."),
        ex("Una grabación de una comunidad sin permiso: ¿la uso o pregunto?", "pregunto", "Primero pregunto si hay permiso."),
    ],
    A=[
        ex("Recursos de una lista. 1) Mi dibujo. 2) Una foto de una compañera sin su permiso. 3) Un texto que escribí. ¿Cuáles puedo usar? Escribe los números.", "1 y 3", "Los míos están permitidos; la foto no tiene permiso."),
        arith("Tienes 6 recursos y 2 no tienen permiso. ¿Cuántos puedes usar?", "6 - 2", "Resto los sin permiso del total."),
        ex("Ordena los pasos para un recurso ajeno: A) lo uso B) pregunto si hay permiso. Escribe las letras en el orden correcto.", "B, A", "Primero pregunto y solo después lo uso."),
    ],
    Z=[
        ex("Eva usa un dibujo suyo. Gaspar usa un símbolo que encontró sin saber de dónde viene. ¿Quién respetó la autoría?", "Eva", "Eva usó algo propio."),
        ex("Una persona dice que puede usar una canción porque «está a mano». ¿Qué le falta: A) permiso B) un aparato nuevo?", "A", "Estar a mano no es permiso."),
    ],
    D=[
        arith("Un curso junta 18 recursos y 5 necesitan permiso. ¿Cuántos no necesitan permiso por ahora?", "18 - 5", "Resto los que necesitan permiso del total."),
        ex("El educador tradicional te entrega una grabación suya y dice que puedes usarla solo en el aula. ¿La publicas en internet: sí o no?", "no", "El permiso es solo para el aula."),
    ],
    context=[ex("Para una tarjeta del curso necesitas una imagen. ¿Qué eliges: «dibujo uno yo» o «copio una imagen de un sitio sin saber su autor»?", "«dibujo uno yo»", "Es un recurso propio y con permiso.")],
    selfcheck=[
        ex("¿Qué tres preguntas hago sobre un recurso?", "quién lo hizo, si tengo permiso y si pertenece a una comunidad", "Son las preguntas de la clase."),
        ex("¿Qué recurso es el más seguro?", "uno propio", "Lo hice yo."),
        ex("Si dudo, ¿a quién pregunto?", "al educador tradicional", "Él o ella conoce la comunidad."),
    ],
    task=T(
        "Haz una lista de tres recursos para tu tarjeta digital: uno dibujado por ti, uno escrito por ti (por ejemplo, una frase corta de agradecimiento en castellano) y una palabra de la ficha. Para cada uno anota la autoría y si tienes permiso. Si usas un aparato, hazlo con un adulto y no publiques.",
        "1) Dibujo del sol: autoría, yo; permiso, sí. 2) Frase «Gracias por venir»: autoría, yo; permiso, sí. 3) Palabra ko: autoría, ficha; permiso, sí.",
        ["lista de tres recursos", "anota autoría y permiso de cada uno", "usa solo recursos propios o con permiso"],
        ["lista escrita en el cuaderno"],
        ["usar recursos sin permiso", "no anotar la autoría"],
        "Valora que anotó autoría y permiso; si usó un recurso sin permiso, pídele que lo reemplace por uno propio.",
    ),
    reinforce="Di en voz alta qué tres preguntas haces sobre cada recurso.",
    extend="Explica a una persona de tu casa por qué algo que está en internet puede tener autoría.",
)

L(
    LF5, 3,
    materials="Lápiz y hoja. El guion está escrito aquí y es inventado. Si usas un aparato, solo con una persona adulta. " + FICHA_PAL,
    use="Aprenderé a crear un registro breve con un guion de tres partes. Sirve para planear una tarjeta o un audio corto antes de hacerlo.",
    prior=["Sé elegir recursos con permiso.", "Sé definir mensaje y audiencia."],
    explain=[
        "Un registro breve es una creación corta que guarda un mensaje: un audio de pocos segundos, una tarjeta con un dibujo o un texto. Antes de hacerlo escribo un guion, que es el plan paso a paso. Mi guion tiene tres partes: inicio, mensaje y cierre.",
        "En el inicio saludo o presento. En el mensaje digo mi única idea con la palabra de la ficha. En el cierre agradezco o me despido. Por ejemplo: inicio: «Hola, hoy aprendí una palabra»; mensaje: «ko es agua en mapuzugun»; cierre: «Chaltumay por escuchar».",
        "Mido el tiempo para que sea breve: un audio de más de 30 segundos puede cansar. Si hay una voz, es la mía o la de alguien con permiso. No grabo en lugares donde otros no saben. La forma de decir las palabras en lengua indígena la practico con el educador tradicional antes de grabar.",
    ],
    vocab=[("guion", "plan paso a paso de lo que voy a hacer"), ("inicio", "primera parte: saludo o presentación"), ("cierre", "última parte: agradecimiento o despedida"), ("segundo", "unidad de tiempo; 60 segundos son 1 minuto"), ("registro", "creación que guarda un mensaje")],
    worked=[
        W("Leer un guion", "Guion inventado. Inicio: «Hola, hoy aprendí una palabra». Mensaje: «ko es agua en mapuzugun». Cierre: «Chaltumay por escuchar». ¿Cuál es el mensaje?", ["Busco la segunda parte.", "Dice «ko es agua en mapuzugun»."], "«ko es agua en mapuzugun»"),
        W("Medir el tiempo", "Cada parte dura 10 segundos. El guion tiene 3 partes. ¿Cuánto dura el audio?", ["Multiplico 3 partes por 10 segundos.", "3 × 10 = 30."], "30 segundos"),
    ],
    mistakes=[
        M("Hacer un guion sin cierre.", "El registro termina de golpe.", "Agrego un agradecimiento o una despedida."),
        M("Grabar sin avisar a otras personas.", "Pueden no querer salir.", "Aviso y pido permiso."),
    ],
    R=[
        ex("Un guion es: A) un plan paso a paso B) un tipo de dibujo.", "A", "El guion planea cada parte."),
        ex("Mi guion tiene tres partes: inicio, mensaje y...", "cierre", "La tercera parte es el cierre."),
        ex("En el cierre, ¿agradezco o empiezo otra idea?", "agradezco", "El cierre termina con agradecimiento o despedida."),
    ],
    C=[
        ex("Guion: «Inicio: Hola. Mensaje: antü es sol. Cierre: Chaltumay». ¿Qué significa antü en el mensaje?", "sol", "La ficha dice sol."),
        ex("Verdadero o falso: puedo grabar a otras personas sin avisar.", "Falso", "Necesito su permiso."),
        arith("Un audio tiene 3 partes de 10 segundos. ¿Cuántos segundos dura?", "3 * 10", "Multiplico partes por segundos."),
    ],
    A=[
        ex("Ordena el guion: A) cierro con un agradecimiento B) saludo en el inicio C) digo el mensaje. Escribe las letras.", "B, C, A", "Inicio, mensaje y cierre."),
        arith("Cada parte dura 15 segundos y hay 2 partes. ¿Cuánto dura en total?", "15 * 2", "Multiplico segundos por partes."),
        ex("Guion con mensaje: «kuyen es luna en mapuzugun». ¿Qué lengua se menciona?", "mapuzugun", "El mensaje la nombra."),
    ],
    Z=[
        ex("Guion 1: tiene inicio, mensaje y cierre. Guion 2: solo tiene mensaje. ¿Cuál tiene la estructura completa? Escribe 1 o 2.", "1", "Tiene las tres partes."),
        ex("Un amigo graba a una vecina sin avisar. ¿Qué error cometió: A) no pidió permiso B) hizo un guion corto?", "A", "La voz de una persona necesita permiso."),
    ],
    D=[
        arith("Un audio dura 45 segundos y quieres que dure 30. ¿Cuántos segundos debes quitar?", "45 - 30", "Resto el tiempo que sobra."),
        ex("Quieres decir una frase en lengua indígena en tu audio y no sabes cómo se pronuncia. ¿Qué haces: A) lo practico con el educador tradicional B) la invento?", "A", "No puedo inventar su sonido."),
    ],
    context=[ex("Tienes un mensaje y 30 segundos para decirlo. ¿Escribes un guion con tres partes o improvisas sin plan?", "un guion con tres partes", "El guion ayuda a ordenar y cumplir el tiempo.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes del guion?", "inicio, mensaje y cierre", "Son las partes de la clase."),
        ex("¿Cuántos segundos hay en 1 minuto?", "60", "Un minuto tiene 60 segundos."),
        ex("¿Qué hago antes de grabar una expresión en lengua indígena?", "la practico con el educador tradicional", "Así la digo bien y con respeto."),
    ],
    task=T(
        "Escribe un guion de tres partes para un audio o tarjeta de 30 segundos. Usa una palabra de la ficha en el mensaje. Calcula cuánto dura cada parte para que sumen 30 segundos. Si grabas, hazlo con una persona adulta, solo tu voz y sin publicar.",
        "Inicio (10 s): «Hola, hoy aprendí una palabra». Mensaje (10 s): «ko es agua en mapuzugun». Cierre (10 s): «Chaltumay por escuchar».",
        ["guion con inicio, mensaje y cierre", "una palabra de la ficha", "suma 30 segundos"],
        ["guion escrito en el cuaderno"],
        ["omitir el cierre", "pasarse del tiempo"],
        "Valora que el guion tenga tres partes y suma 30 segundos; si se pasó de tiempo, pídele que acorte.",
    ),
    reinforce="Lee en voz alta tu guion y cuenta los segundos con un reloj.",
    extend="Pide a una persona de tu casa que escuche tu guion y diga qué parte entendió mejor.",
)

L(
    LF5, 4,
    materials="Lápiz y hoja. La lista de revisión está escrita aquí. " + FICHA_PAL,
    use="Aprenderé a revisar mi creación: lengua, autoría y acceso. Sirve para que sea correcta, respetuosa y que todas las personas puedan entenderla.",
    prior=["Sé hacer un guion de tres partes.", "Sé anotar autoría y permiso."],
    explain=[
        "Revisar mi creación tiene tres partes. La lengua: las palabras de la ficha están copiadas con su grafía exacta y, si hay una expresión en lengua indígena, el educador tradicional la confirmó. La autoría: anoté quién hizo cada recurso y tengo permiso. El acceso: otras personas pueden entenderla sin dificultad.",
        "Para el acceso me pregunto: ¿se ve y se lee con letras grandes?, ¿tiene una versión escrita si es un audio?, ¿se puede ver sin internet? Un recurso accesible incluye a más personas, por ejemplo a quien no oye bien o no tiene un aparato.",
        "Si la revisión muestra un problema, lo corrijo antes de mostrar mi creación. No muestro nada sin la revisión del educador tradicional cuando hay palabras de la lengua indígena.",
    ],
    vocab=[("revisar", "leer o mirar de nuevo para corregir"), ("acceso", "posibilidad de que todas las personas lo entiendan"), ("grafía", "manera de escribir una palabra"), ("versión escrita", "texto que dice lo mismo que un audio"), ("corregir", "cambiar para que quede bien")],
    worked=[
        W("Revisar la lengua", "En una tarjeta dice «El antu brilla». La ficha dice antü. ¿Qué corrige?", ["Compara con la ficha.", "Faltan los dos puntos de la ü."], "Escribir «antü»"),
        W("Revisar el acceso", "Un audio no tiene versión escrita y una compañera no oye bien. ¿Qué agrega?", ["La compañera necesita leer.", "Agrega una versión escrita."], "Una versión escrita del audio"),
    ],
    mistakes=[
        M("Mostrar la creación sin revisar la grafía.", "Pueden quedar letras cambiadas.", "Comparo con la ficha."),
        M("Pensar que todos pueden oír y ver igual.", "Hay personas con otras necesidades.", "Agrego una versión escrita o letras grandes."),
    ],
    R=[
        ex("La revisión tiene tres partes: lengua, autoría y...", "acceso", "La tercera parte es el acceso."),
        ex("La ficha dice «ruka». ¿Cuál coincide con la ficha: ruka o ruca?", "ruka", "La ficha escribe ruka con k; en este cuaderno copiamos la ficha."),
        ex("Un audio con versión escrita es más accesible: ¿verdadero o falso?", "verdadero", "Más personas lo pueden entender."),
    ],
    C=[
        ex("Verdadero o falso: basta con que yo entienda mi creación.", "Falso", "Debe entenderla también la audiencia."),
        ex("Ficha: antü es sol. ¿Qué parte de la revisión confirma que la palabra esté bien escrita?", "la lengua", "Revisa la grafía."),
        ex("Revisión de la autoría: ¿anoto quién hizo cada recurso o solo mi nombre?", "quién hizo cada recurso", "Cada recurso tiene su autoría."),
    ],
    A=[
        ex("Tu tarjeta tiene letras grandes y una versión escrita del audio. ¿Qué parte de la revisión estás comprobando: lengua, autoría o acceso?", "acceso", "Letras grandes y versión escrita ayudan a que más personas la entiendan."),
        arith("Revisaste 5 puntos y 3 estaban bien. ¿Cuántos debes corregir?", "5 - 3", "Resto los bien de los revisados."),
        ex("¿Qué agregas para que una persona sin aparato pueda conocer tu mensaje: una versión escrita o más colores?", "una versión escrita", "El texto se lee sin aparato."),
    ],
    Z=[
        ex("Una tarjeta tiene letras muy pequeñas. ¿Qué parte de la revisión falla: A) acceso B) autoría?", "A", "Letras pequeñas dificultan leer."),
        ex("Eva revisó solo la lengua. Gaspar revisó lengua, autoría y acceso. ¿Quién hizo una revisión completa?", "Gaspar", "Revisó las tres partes."),
    ],
    D=[
        arith("En un curso hay 8 creaciones y 6 pasaron la revisión. ¿Cuántas deben corregirse?", "8 - 6", "Resto las aprobadas del total."),
        ex("Quieres incluir una frase en lengua indígena. ¿Quién debe confirmarla: A) el educador tradicional B) un compañero sin saber?", "A", "Él o ella conoce la lengua."),
    ],
    context=[ex("Tu audio dura 30 segundos y una compañera no oye bien. ¿Qué haces: «agrego una versión escrita» o «lo dejo así»?", "«agrego una versión escrita»", "Incluye a más personas.")],
    selfcheck=[
        ex("¿Con qué comparo la grafía de las palabras?", "con la ficha", "La ficha trae la grafía exacta."),
        ex("¿Qué significa acceso en esta clase?", "que todas las personas puedan entenderla", "Acceso es alcance para todos."),
        ex("¿Quién confirma una expresión en lengua indígena?", "el educador tradicional", "Él o ella conoce la lengua."),
    ],
    task=T(
        "Revisa tu guion o tu tarjeta con esta lista: ¿las palabras de la ficha están bien copiadas?, ¿anoté la autoría de cada recurso?, ¿se entiende con letras grandes y con una versión escrita? Escribe sí o no a cada pregunta y, si hay un no, cómo lo corregirás.",
        "1) Sí. 2) No: anotaré la autoría del dibujo. 3) No: agregaré letras más grandes.",
        ["responde las tres preguntas", "explica una corrección", "usa la ficha para la lengua"],
        ["lista de revisión en el cuaderno"],
        ["revisar sin comparar con la ficha", "no corregir los no"],
        "Valora que revisó las tres partes y que corrigió; si no comparó, pídele que lo haga con la ficha.",
    ),
    reinforce="Elige una creación tuya y revisa solo la lengua con la ficha.",
    extend="Pide a una persona de tu casa que mire tu creación y diga si la entiende sin ayuda.",
)

L(
    LF5, 5,
    materials="Lápiz y hoja. Las situaciones están escritas aquí y son inventadas. " + FICHA_PAL,
    use="Aprenderé a adaptar mi creación a una condición diferente, como otra audiencia o no tener un aparato. Sirve para comunicar mi mensaje en cualquier situación.",
    prior=["Sé hacer y revisar un registro breve.", "Sé que cada recurso tiene autoría."],
    explain=[
        "Transferir es llevar lo que aprendí a una situación nueva. Mi mensaje es el mismo, pero cambia una condición: la audiencia, el medio o los recursos. Por ejemplo, un audio para el curso puede convertirse en un cartel para un niño de primero básico, o en una exposición oral sin aparato.",
        "Para adaptar sigo tres pasos. Primero mantengo el mensaje. Luego cambio la forma para que la nueva audiencia la entienda: frases más cortas, dibujos más grandes o lectura en voz alta. Finalmente reviso de nuevo la lengua, la autoría y el acceso.",
        "Si no hay aparato ni electricidad, puedo comunicar mi mensaje con papel o con la voz. La tecnología es una ayuda, no un requisito. Y la parte de lengua indígena la sigo consultando con el educador tradicional.",
    ],
    vocab=[("transferir", "llevar lo que aprendí a una situación nueva"), ("adaptar", "cambiar la forma sin cambiar el mensaje"), ("condición", "circunstancia: otra audiencia, sin aparato"), ("medio", "forma de comunicar: audio, papel, voz"), ("exposición oral", "presentación hablada ante un grupo")],
    worked=[
        W("Cambiar de audiencia", "Mi mensaje es «ko es agua en mapuzugun» y ahora es para niños de primero. ¿Qué cambio?", ["Mantengo el mensaje.", "Uso una frase más corta y un dibujo grande."], "La forma: frase corta y dibujo grande"),
        W("Sin aparato", "Quiero comunicar el mismo mensaje en una sala sin electricidad. ¿Qué medio uso?", ["Puedo usar papel.", "O mi voz."], "Un cartel en papel o una exposición oral"),
    ],
    mistakes=[
        M("Cambiar el mensaje cuando cambio la audiencia.", "Se pierde la idea original.", "Mantengo el mensaje y adapto la forma."),
        M("Creer que sin aparato no se puede comunicar.", "Hay otros medios.", "Uso papel o voz."),
    ],
    R=[
        ex("Transferir es: A) llevar lo aprendido a una situación nueva B) borrar el trabajo.", "A", "Transferir es adaptar."),
        ex("Al adaptar, ¿cambio el mensaje o la forma?", "la forma", "El mensaje se mantiene."),
        ex("Sin aparato, ¿puedo comunicar con papel?", "Sí", "El papel es un medio."),
    ],
    C=[
        ex("Verdadero o falso: para comunicar un mensaje siempre necesito un aparato.", "Falso", "Papel o voz también sirven."),
        ex("Audiencia nueva: niños de primero. ¿Qué es mejor: frases más cortas o frases muy largas?", "frases más cortas", "Son más fáciles de entender."),
        ex("Mensaje: «antü es sol». Si la audiencia cambia, ¿el mensaje cambia: sí o no?", "no", "El mensaje se mantiene."),
    ],
    A=[
        ex("Ordena para adaptar: A) reviso de nuevo B) mantengo el mensaje C) cambio la forma. Escribe las letras.", "B, C, A", "Mantengo, cambio y reviso."),
        arith("Para niños de primero haces 3 carteles con 2 frases cada uno. ¿Cuántas frases son en total?", "3 * 2", "Multiplico carteles por frases."),
        ex("Condición: no hay electricidad. ¿Qué medio eliges: un cartel en papel o un video en pantalla?", "un cartel en papel", "El papel no necesita electricidad."),
    ],
    Z=[
        ex("Dos adaptaciones para un niño de primero. Eva: dibujo grande y una frase. Gaspar: cuatro párrafos. ¿Quién adaptó mejor?", "Eva", "Adaptó forma y extensión."),
        ex("Una persona adapta el mensaje y cambia la palabra de la ficha por una inventada. ¿Qué error comete: A) cambió la lengua B) cambió el color?", "A", "No debe inventar palabras."),
    ],
    D=[
        arith("De 10 estudiantes, 6 adaptaron su mensaje a otra audiencia. ¿Cuántos faltan?", "10 - 6", "Resto los que adaptaron."),
        ex("Una persona quiere compartir en internet su adaptación. ¿Qué debe hacer primero: A) pedir permiso al educador y a un adulto B) subirla?", "A", "No se publica sin permiso."),
    ],
    context=[ex("Te invitan a mostrar tu mensaje a niños pequeños sin aparato. ¿Haces «un cartel grande con dibujo» o «un audio largo»?", "«un cartel grande con dibujo»", "Es accesible para esa condición.")],
    selfcheck=[
        ex("¿Qué se mantiene al adaptar?", "el mensaje", "La idea sigue igual."),
        ex("¿Qué puedo usar si no hay aparato?", "papel o mi voz", "Son otros medios."),
        ex("¿Qué reviso después de adaptar?", "lengua, autoría y acceso", "Repito la revisión."),
    ],
    task=T(
        "Elige una de estas dos condiciones nuevas: (a) la audiencia son niños de primero, o (b) no hay aparato ni electricidad. Adapta tu mensaje de la clase 3 a esa condición. Escribe qué cambiaste en la forma y qué mantuviste. Revisa de nuevo lengua, autoría y acceso.",
        "Condición (b). Mensaje: ko es agua en mapuzugun. Cambié: un cartel en papel con dibujo. Mantuve: el mensaje y la grafía de la ficha.",
        ["mantiene el mensaje", "adapta la forma a la condición", "revisa de nuevo lengua, autoría y acceso"],
        ["adaptación escrita en el cuaderno"],
        ["cambiar el mensaje", "no revisar"],
        "Valora que adaptó la forma; si cambió el mensaje, pídele que vuelva a la idea original.",
    ),
    reinforce="Di en voz alta cómo cambiarías tu mensaje para un niño pequeño.",
    extend="Prueba tu adaptación con una persona de tu casa y anota qué entendió.",
)

# =================================================================== OA LF06 · registro tecnológico situado
L(
    LF6, 1,
    materials="Lápiz y hoja. Las fichas están escritas aquí y son inventadas. Los aparatos solo se usan con una persona adulta. " + FICHA_PAL,
    use="Aprenderé a definir para qué registro una experiencia, quién es la fuente y si hay autorización. Sirve para contar experiencias con respeto, sin exponer a nadie.",
    prior=["Sé que una creación tiene autoría y permiso.", "Sé que mi creación no se publica."],
    explain=[
        "Registrar una experiencia es guardar lo que pasó con un audio, un dibujo o un texto. Las experiencias de la vida familiar y comunitaria son importantes porque guardan la memoria de un grupo. Antes de registrar defino tres cosas: el propósito, la fuente y la autorización.",
        "El propósito es para qué registro, por ejemplo «guardar cómo cuidamos la huerta del curso». La fuente es la persona o el grupo que cuenta o vive la experiencia. La autorización es el permiso claro de esa persona, y de un adulto si es menor. Sin autorización, no registro.",
        "No tengo que contar nada de mi familia ni de mi vida privada. Puedo registrar una experiencia del curso o una inventada. Si se trata de la comunidad, pido al educador tradicional que me diga qué se puede registrar y qué no.",
    ],
    vocab=[("registrar", "guardar lo que pasó con un audio, texto o dibujo"), ("propósito", "para qué hago algo"), ("fuente", "persona o grupo que cuenta la experiencia"), ("autorización", "permiso claro para usar algo"), ("memoria", "lo que un grupo recuerda y guarda")],
    worked=[
        W("Definir el propósito", "Un curso quiere registrar cómo cuida la huerta del colegio. ¿Cuál es el propósito?", ["El propósito es para qué se registra.", "Es guardar cómo se cuida la huerta."], "Guardar cómo se cuida la huerta"),
        W("Ver si hay autorización", "Ficha inventada. Fuente: don Luis, jardinero de la escuela. Autorización: «Sí, para el aula». ¿Se puede registrar su relato?", ["Busco la autorización.", "Dice «Sí, para el aula»."], "Sí, solo para el aula"),
    ],
    mistakes=[
        M("Registrar sin preguntar a la persona.", "No hay autorización.", "Pido permiso antes."),
        M("Contar cosas privadas de mi familia.", "No es necesario y puede exponer a otros.", "Registro una experiencia del curso o inventada."),
    ],
    R=[
        ex("El propósito es: A) para qué registro B) con qué lápiz registro.", "A", "Propósito es el motivo."),
        ex("La autorización es: A) el permiso claro B) el nombre del archivo.", "A", "Autorización es permiso."),
        ex("La fuente es: A) quien cuenta o vive la experiencia B) el aparato.", "A", "La fuente es la persona o el grupo."),
    ],
    C=[
        ex("Verdadero o falso: puedo registrar a alguien sin avisarle si es para mí.", "Falso", "Siempre pido autorización."),
        ex("Ficha: «Fuente: don Luis. Autorización: no». ¿Registro su relato: sí o no?", "no", "Sin autorización no se registra."),
        ex("¿Estoy obligado a contar algo de mi familia?", "No", "Puedo usar una experiencia del curso o inventada."),
    ],
    A=[
        ex("Ficha: Propósito, guardar cómo se riega la huerta. Fuente, la profesora. Autorización, (sin dato). ¿Qué dato falta completar: el propósito, la fuente o la autorización?", "la autorización", "Sin ese dato no se puede registrar."),
        arith("En un curso hay 5 fichas y 3 tienen autorización. ¿Cuántas fichas no la tienen?", "5 - 3", "Resto las autorizadas del total."),
        ex("Propósito: «guardar cómo se riega la huerta». ¿Qué experiencia debe registrar: cómo se riega la huerta o un partido?", "cómo se riega la huerta", "Debe coincidir con el propósito."),
    ],
    Z=[
        ex("Eva pidió permiso a su profesora para registrar la clase de huerta. Gaspar registró sin avisar. ¿Quién cumplió con la autorización?", "Eva", "Eva pidió permiso."),
        ex("Una persona quiere registrar un saber de la comunidad. ¿A quién consulta primero: A) al educador tradicional B) a nadie?", "A", "Él o ella dice qué se puede registrar."),
    ],
    D=[
        arith("Una escuela tiene 12 experiencias posibles y registra 3. ¿Cuántas quedan sin registrar?", "12 - 3", "Resto las registradas."),
        ex("La autorización es «solo para el aula». ¿Puedes subir el audio a internet: sí o no?", "no", "La autorización limita el uso al aula."),
    ],
    context=[ex("Quieres registrar cómo el curso riega la huerta. ¿Qué haces primero: «defino el propósito y pido autorización» o «empiezo a grabar»?", "«defino el propósito y pido autorización»", "Son los pasos previos.")],
    selfcheck=[
        ex("¿Qué tres cosas defino antes de registrar?", "propósito, fuente y autorización", "Son los pasos de la clase."),
        ex("¿Qué experiencia puedo registrar si no quiero contar de mi familia?", "una del curso o una inventada", "Hay otras opciones seguras."),
        ex("¿A quién consulto si es un saber de la comunidad?", "al educador tradicional", "Él o ella orienta."),
    ],
    task=T(
        "Completa esta ficha con una experiencia inventada o del curso: propósito (para qué registras), fuente (quién la cuenta), autorización (sí o no, y hasta dónde) y una pregunta para el educador tradicional sobre qué se puede registrar de la comunidad. No uses datos de tu familia.",
        "Propósito: guardar cómo el curso cuida la huerta. Fuente: mi profesora. Autorización: sí, para el aula. Pregunta: ¿qué se puede registrar de la comunidad?",
        ["define propósito, fuente y autorización", "no usa datos privados", "formula una pregunta para quien enseña"],
        ["ficha escrita en el cuaderno"],
        ["registrar sin autorización", "incluir datos de la familia"],
        "Valora que definió los tres datos; si incluyó datos privados, pídele que use una experiencia del curso.",
    ),
    reinforce="Di en voz alta propósito, fuente y autorización de una experiencia de tu curso.",
    extend="Explica a una persona de tu casa por qué se pide permiso antes de registrar a alguien.",
)

L(
    LF6, 2,
    materials="Lápiz y hoja. La tabla de medios está escrita aquí. Los aparatos solo se usan con una persona adulta.",
    use="Aprenderé a elegir un medio para registrar (audio, dibujo, texto o foto) según el acceso y la seguridad. Sirve para registrar sin riesgos y para que todos puedan participar.",
    prior=["Sé definir propósito, fuente y autorización.", "Sé que mi registro no se publica."],
    explain=[
        "Un medio es la forma que uso para registrar. Puede ser un audio, un dibujo, un texto o una foto. Cada medio tiene ventajas. El audio guarda la voz, pero necesita un aparato con batería. El dibujo y el texto se hacen en papel y no necesitan electricidad. La foto muestra imágenes, pero puede mostrar caras.",
        "Para elegir un medio me hago tres preguntas. ¿Está disponible para mí y para mi grupo? Es el acceso. ¿Protege la privacidad de las personas? Es la seguridad. ¿Sirve para el propósito? Es la utilidad. Si un medio muestra la cara de alguien y no tengo permiso, elijo otro.",
        "No es necesario usar tecnología para registrar. Un dibujo o un texto en papel también son registros válidos. Lo importante es que el medio cuide a las personas.",
    ],
    vocab=[("medio", "forma de registrar: audio, dibujo, texto o foto"), ("acceso", "posibilidad real de usarlo"), ("seguridad", "que no exponga ni dañe a nadie"), ("privacidad", "cuidado de lo personal de cada uno"), ("batería", "energía que necesita un aparato para funcionar")],
    worked=[
        W("Elegir sin aparato", "No hay aparato disponible en la sala. Quiero registrar cómo se riega la huerta. ¿Qué medio elijo?", ["Necesito un medio sin aparato.", "Puedo dibujar o escribir."], "Un dibujo o un texto en papel"),
        W("Cuidar la privacidad", "Una foto mostraría la cara de un niño que no tiene permiso. ¿Qué medio elijo?", ["La foto muestra caras.", "Elijo un dibujo o un audio con permiso."], "Un dibujo"),
    ],
    mistakes=[
        M("Elegir el medio solo porque es nuevo.", "Puede no estar disponible ni ser seguro.", "Reviso acceso, seguridad y utilidad."),
        M("Usar una foto con caras sin permiso.", "Expone a las personas.", "Elijo un medio que proteja la privacidad."),
    ],
    R=[
        ex("Un medio es: A) forma de registrar B) una persona.", "A", "Audio, dibujo, texto o foto son medios."),
        ex("¿Qué medio no necesita electricidad: dibujo o audio?", "dibujo", "El dibujo se hace en papel."),
        ex("¿Qué medio puede mostrar caras: la foto o el texto?", "la foto", "Una foto puede mostrar rostros."),
    ],
    C=[
        ex("Verdadero o falso: un dibujo en papel es un registro válido.", "Verdadero", "Cualquier medio válido sirve."),
        ex("El acceso es: A) si lo puedo usar B) si es bonito.", "A", "Acceso es poder usarlo."),
        ex("Si no hay batería, ¿elijo un audio o un texto en papel?", "un texto en papel", "El audio necesita batería."),
    ],
    A=[
        ex("Tabla: audio (necesita aparato, guarda la voz), dibujo (papel, sin voz), texto (papel, sin voz), foto (aparato, muestra caras). No hay aparato. ¿Qué dos medios quedan?", "dibujo y texto", "Los de papel no necesitan aparato."),
        arith("Un aparato graba 10 minutos y cada audio dura 2 minutos. ¿Cuántos audios caben?", "10 // 2", "Divido el tiempo total por la duración de cada audio."),
        ex("Una de estas preguntas es la de seguridad: A) ¿está disponible para mi grupo? B) ¿protege la privacidad de las personas? ¿Cuál?", "B", "Proteger la privacidad es el criterio de seguridad; estar disponible es el acceso."),
    ],
    Z=[
        ex("Eva elige un dibujo porque no hay permiso para mostrar caras. Gaspar elige una foto con caras. ¿Quién cuidó la privacidad?", "Eva", "El dibujo evita mostrar caras."),
        ex("Un grupo no tiene aparatos. Un compañero dice «no podemos registrar nada». ¿Qué le contestas: A) podemos dibujar y escribir B) tiene razón?", "A", "El papel también sirve."),
    ],
    D=[
        arith("Un grupo tiene 15 minutos de grabación y usa 9. ¿Cuántos minutos quedan?", "15 - 9", "Resto los usados del total."),
        ex("Quieres un medio que guarde la voz de una persona que te dio permiso. ¿Elijes un audio o un dibujo?", "un audio", "El audio guarda la voz."),
    ],
    context=[ex("Quieres registrar la clase de huerta pero no puedes usar fotos de las caras. ¿Eliges «un dibujo» o «una foto de los niños»?", "«un dibujo»", "Protege la privacidad.")],
    selfcheck=[
        ex("¿Qué tres preguntas hago para elegir un medio?", "acceso, seguridad y utilidad", "Son los criterios."),
        ex("¿Qué medios no necesitan aparato?", "dibujo y texto", "Se hacen en papel."),
        ex("¿Qué cuido al elegir un medio?", "la privacidad", "No expongo a las personas."),
    ],
    task=T(
        "Elige un medio para registrar una experiencia inventada del curso (por ejemplo, regar la huerta). Escribe cuál elegiste, por qué (acceso, seguridad y utilidad) y qué medios descartaste. Si no tienes aparato, usa papel.",
        "Elijo un dibujo porque no necesita aparato, no muestra caras y sirve para mostrar el riego. Descarto la foto porque muestra caras.",
        ["elige un medio", "justifica con acceso, seguridad y utilidad", "nombra un medio que descartó"],
        ["decisión escrita en el cuaderno"],
        ["elegir sin justificar", "usar fotos con caras sin permiso"],
        "Valora que justificó con los tres criterios; si no, pídele que los revise.",
    ),
    reinforce="Di en voz alta qué medio elegirías si no hay aparato y por qué.",
    extend="Pregunta a una persona de tu casa qué medio prefiere para guardar un recuerdo.",
)

L(
    LF6, 3,
    materials="Lápiz y hoja. Las listas están escritas aquí y son inventadas.",
    use="Aprenderé a registrar una experiencia sin mostrar datos personales ni saberes que la comunidad no autorizó a compartir. Sirve para cuidar a las personas y a su cultura.",
    prior=["Sé elegir un medio accesible y seguro.", "Sé pedir autorización."],
    explain=[
        "Los datos personales son informaciones que identifican a una persona: nombre completo, dirección, teléfono, cara, voz o fecha de nacimiento. Al registrar una experiencia no los incluyo. Puedo usar nombres inventados o solo un nombre de pila si hay permiso.",
        "Un saber restringido es un conocimiento que una comunidad decidió no compartir con todos. No lo registro aunque lo conozca. Si no sé si un saber es restringido, lo trato como si lo fuera y pregunto al educador tradicional.",
        "Antes de registrar reviso mi contenido con una lista: sin datos personales, sin voces ni caras sin permiso y sin saberes restringidos. Si un dato falla, lo quito. Nadie puede obligarme a registrar algo que no quiero, y puedo cambiar la experiencia por una inventada.",
    ],
    vocab=[("datos personales", "informaciones que identifican a una persona"), ("saber restringido", "conocimiento que una comunidad decidió no compartir"), ("privado", "que pertenece solo a una persona o familia"), ("identificar", "reconocer quién es alguien"), ("quitar", "sacar algo de mi registro")],
    worked=[
        W("Clasificar un dato", "Dato: «Mi dirección es calle Uno 123». ¿Se puede incluir en un registro: sí o no?", ["Una dirección identifica una casa.", "Es un dato personal."], "No"),
        W("Quitar lo que falla", "Un guion dice: «Mi vecina Andrea Pérez nos enseñó a regar». ¿Qué debe cambiar?", ["El nombre completo es un dato personal.", "Lo cambia por «una vecina» o un nombre inventado."], "Quitar el nombre completo"),
    ],
    mistakes=[
        M("Poner el nombre completo y la dirección «para que quede más real».", "Expone a las personas.", "Uso nombres inventados o «una vecina»."),
        M("Registrar un saber que no sé si se puede compartir.", "Puede ser restringido.", "Lo trato como restringido y pregunto."),
    ],
    R=[
        ex("¿Una dirección es un dato personal: sí o no?", "sí", "Identifica una casa."),
        ex("Un saber restringido es: A) uno que la comunidad decidió no compartir B) uno que todos conocen.", "A", "Restringido es no compartido."),
        ex("¿Una cara en una foto puede ser un dato personal: sí o no?", "sí", "Identifica a una persona."),
    ],
    C=[
        ex("Verdadero o falso: puedo usar nombres inventados para proteger a las personas.", "Verdadero", "Los nombres inventados protegen."),
        ex("Si no sé si un saber es restringido, ¿lo trato como restringido o lo registro?", "lo trato como restringido", "Es más seguro y respetuoso."),
        ex("¿A quién pregunto qué se puede compartir de la comunidad: al educador tradicional o a nadie?", "al educador tradicional", "Él o ella orienta."),
    ],
    A=[
        ex("Lista: 1) nombre completo 2) un nombre inventado 3) dirección 4) «una vecina». ¿Cuáles puedo incluir? Escribe los números.", "2 y 4", "No identifican a nadie."),
        arith("Un registro tiene 8 datos y 3 son personales. ¿Cuántos puedes dejar?", "8 - 3", "Quito los personales."),
        ex("Revisaste tu registro y encontraste una dirección. ¿Qué haces: A) la quito y vuelvo a revisar B) lo registro igual?", "A", "Un dato personal que falla se quita antes de registrar."),
    ],
    Z=[
        ex("Dos guiones. Eva: «Una vecina nos enseñó a regar». Gaspar: «Rosa Pérez, de calle Uno 123, nos enseñó». ¿Cuál protege los datos?", "el de Eva", "No identifica a nadie."),
        ex("Una persona conoce un saber de su comunidad y quiere registrarlo para su cuaderno. ¿Qué hace primero: A) consultar al educador tradicional B) registrarlo?", "A", "Puede ser restringido."),
    ],
    D=[
        arith("De 15 registros del curso, 9 no tenían datos personales. ¿Cuántos sí los tenían?", "15 - 9", "Resto los seguros del total."),
        ex("Un amigo te pide registrar algo privado de tu familia. ¿Qué haces: A) puedo decir que no y usar una experiencia inventada B) lo grabo igual?", "A", "Nadie está obligado a contar cosas privadas."),
    ],
    context=[ex("Registras cómo se riega la huerta. ¿Escribes «una vecina nos enseñó» o «Andrea Pérez, de calle Uno 123, nos enseñó»?", "«una vecina nos enseñó»", "No expone datos personales.")],
    selfcheck=[
        ex("¿Qué son los datos personales?", "informaciones que identifican a una persona", "Nombre, dirección, cara o voz."),
        ex("¿Qué hago con un saber que no sé si es restringido?", "lo trato como restringido", "Es la forma de cuidar."),
        ex("¿Estoy obligado a contar cosas privadas?", "No", "Puedo usar una experiencia inventada."),
    ],
    task=T(
        "Escribe un registro de tres frases sobre una experiencia inventada del curso (por ejemplo, regar la huerta). No incluyas nombres completos, direcciones ni saberes restringidos. Revísalo con la lista: sin datos personales, sin voces ni caras sin permiso, sin saberes restringidos.",
        "El curso riega la huerta. Una vecina nos enseñó a regar temprano. Aprendimos que el ko es importante.",
        ["tres frases", "sin datos personales", "revisado con la lista"],
        ["registro escrito y revisado en el cuaderno"],
        ["incluir nombre completo o dirección", "registrar un saber restringido"],
        "Valora que protegió los datos; si incluyó alguno, pídele que lo cambie.",
    ),
    reinforce="Mira tu registro y subraya cualquier dato personal que encuentres.",
    extend="Explica a una persona de tu casa qué son los datos personales.",
)

L(
    LF6, 4,
    materials="Lápiz y hoja. La lista de revisión está escrita aquí. " + FICHA_PAL,
    use="Aprenderé a revisar mi registro (lengua, contexto, autoría y almacenamiento) y a guardarlo de forma ordenada y segura. Sirve para cuidar lo que registré.",
    prior=["Sé registrar sin exponer datos.", "Sé anotar la autoría."],
    explain=[
        "Revisar un registro tiene cuatro partes. La lengua: las palabras de la ficha están copiadas con su grafía exacta y, si hay lengua indígena, el educador tradicional la confirmó. El contexto: explica cuándo y dónde pasó la experiencia. La autoría: dice quién lo hizo. El almacenamiento: dónde y cómo se guarda.",
        "Almacenar es guardar un registro en un lugar seguro. Pongo un nombre claro al archivo o al papel: tema y fecha, por ejemplo «huerta-curso-mayo». No uso nombres completos ni datos personales en el título. Dejo el registro en un lugar que el adulto autorizó y aviso a las personas que participaron si lo voy a conservar.",
        "Quien me dio permiso puede pedirme que borre mi registro. Si lo pide, lo borro. Un registro bien cuidado respeta a las personas que participaron.",
    ],
    vocab=[("almacenar", "guardar en un lugar seguro"), ("archivo", "documento guardado con un nombre"), ("contexto", "cuándo y dónde pasó la experiencia"), ("autoría", "quién hizo el registro"), ("borrar", "eliminar un registro cuando la persona lo pide")],
    worked=[
        W("Nombre de un archivo", "Opciones: A) huerta-curso-mayo B) Andrea-Pérez-calle-Uno-123. ¿Cuál es un buen nombre?", ["B tiene datos personales.", "A dice tema y fecha."], "A"),
        W("Pedir que se borre", "Una persona que dio permiso pide que borres un audio. ¿Qué haces?", ["Respeto su decisión.", "Borro el audio."], "Lo borro"),
    ],
    mistakes=[
        M("Nombrar el archivo con el nombre completo de alguien.", "Es un dato personal.", "Uso tema y fecha."),
        M("Guardar en cualquier lugar.", "Otros podrían verlo sin permiso.", "Guardo donde el adulto autorizó."),
    ],
    R=[
        ex("Almacenar es: A) guardar en un lugar seguro B) tirar a la basura.", "A", "Almacenar es guardar."),
        ex("Un buen nombre de archivo incluye tema y...", "fecha", "Tema y fecha ordenan el registro."),
        ex("Si una persona pide borrar su registro, ¿lo borro o lo guardo igual?", "lo borro", "Respeto su decisión."),
    ],
    C=[
        ex("Verdadero o falso: el nombre completo de un niño puede ir en el título del archivo.", "Falso", "Es un dato personal."),
        ex("El contexto de un registro dice: A) cuándo y dónde pasó B) cuántos colores usé.", "A", "Contexto es situación."),
        ex("Un registro dice «Ayer, en el patio, el curso regó la huerta». ¿Qué parte de la revisión cubre «ayer, en el patio»: el contexto o el almacenamiento?", "el contexto", "El contexto dice cuándo y dónde pasó la experiencia."),
    ],
    A=[
        ex("A tu registro le falta decir quién lo hizo. ¿Qué parte de la revisión debes completar: lengua, contexto, autoría o almacenamiento?", "autoría", "La autoría dice quién hizo el registro."),
        arith("Tienes 6 registros y guardaste 4. ¿Cuántos faltan por guardar?", "6 - 4", "Resto los guardados del total."),
        ex("Archivo: «huerta-curso-mayo». ¿Qué dos datos da el nombre: tema y fecha o nombre y dirección?", "tema y fecha", "Esos datos están en el título."),
    ],
    Z=[
        ex("Eva guardó su registro en un lugar que autorizó el adulto. Gaspar lo dejó en cualquier parte. ¿Quién almacenó mejor?", "Eva", "Eva guardó en un lugar autorizado."),
        ex("Una persona agrega al registro una palabra en lengua indígena que no está en la ficha. ¿Qué falta: A) la confirmación del educador tradicional B) más color?", "A", "Debe confirmar la palabra."),
    ],
    D=[
        arith("En un curso hay 20 registros y 14 están bien revisados. ¿Cuántos faltan por revisar?", "20 - 14", "Resto los revisados del total."),
        ex("Una persona quiere guardar su registro en un lugar que otras personas ven. ¿Qué hace primero: A) pregunta al adulto y a los participantes B) lo guarda?", "A", "El almacenamiento necesita autorización."),
    ],
    context=[ex("Terminaste tu registro de la huerta. ¿Qué haces: «lo reviso y lo guardo donde el adulto me indicó» o «lo dejo donde sea»?", "«lo reviso y lo guardo donde el adulto me indicó»", "Así queda seguro y ordenado.")],
    selfcheck=[
        ex("¿Cuáles son las cuatro partes de la revisión?", "lengua, contexto, autoría y almacenamiento", "Son las partes de la clase."),
        ex("¿Qué incluye un buen nombre de archivo?", "tema y fecha", "Y no datos personales."),
        ex("¿Qué hago si alguien pide borrar su registro?", "lo borro", "Respeto su decisión."),
    ],
    task=T(
        "Revisa tu registro de la clase 3 con las cuatro partes. Escribe sí o no a cada una: lengua, contexto, autoría y almacenamiento. Inventa un nombre de archivo con tema y fecha y escribe dónde lo guardarías con la autorización de un adulto. Escribe una pregunta para el educador tradicional sobre cómo cuida su comunidad los registros.",
        "Lengua: sí. Contexto: sí. Autoría: sí. Almacenamiento: sí. Nombre: huerta-curso-mayo. Lugar: carpeta del curso, con permiso. Pregunta: ¿cómo cuidan los registros?",
        ["responde las cuatro partes", "inventa un nombre sin datos personales", "formula una pregunta para quien enseña"],
        ["revisión escrita en el cuaderno"],
        ["incluir datos personales en el nombre", "no indicar dónde guarda"],
        "Valora que revisó las cuatro partes; si el nombre incluye datos personales, pídele que lo cambie.",
    ),
    reinforce="Di en voz alta las cuatro partes de la revisión.",
    extend="Explica a una persona de tu casa cómo ordenarías tus archivos con tema y fecha.",
)
