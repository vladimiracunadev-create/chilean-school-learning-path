"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR06 (producir creaciones audiovisuales o escritas, incorporando frases y oraciones en lengua indígena, con recursos
TIC disponibles, para contar situaciones personales, familiares o comunitarias) y OA LS01 (disfrutar y comprender
historias y experiencias relacionadas con un evento sociocultural o espiritual de otros pueblos y culturas, reflexionando
y expresando opiniones sobre las distintas cosmovisiones, con lenguajes artísticos propios del pueblo indígena que
corresponda).

Criterio de autoría: los relatos, comunidades, guiones y personas son inventados para practicar y están rotulados como
tales; no describen ningún pueblo real. Los pueblos y culturas de los relatos (Valle Ejemplo, Isla Ejemplo) son ficticios
para no atribuir ritos ni creencias a pueblos reales. Las únicas expresiones en lengua indígena son mari mari y chaltumay
(mapuzugun) e iorana y maururu (rapa nui). No se inventa lengua ni rito.
"""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_lc6_c import L, M, T, W

LR6 = "LC06 OA LR06"
LS1 = "LC06 OA LS01"

# ============================================================ LR06 clase 1 · situar la creación
P1 = "Propuesta 1 (inventada para practicar): un audio de un minuto en el que una estudiante cuenta cómo se saluda en su casa cuando llega una visita. Usará «mari mari», saludo en mapuzugun que le entregó y autorizó el educador tradicional. Grabará con la grabadora del celular de su familia."
P2 = "Propuesta 2 (inventada): un video de tres escenas con compañeros del curso presentando su escuela. Todavía no tiene el permiso de las familias para mostrar sus caras. Dice incluir una frase en rapa nui que alguien vio en una página de internet."
P3 = "Propuesta 3 (inventada): un cartel dibujado en papel, sin celular ni computador, sobre una feria de lana de la comunidad cercana. Incluirá «mari mari» que autorizó el educador tradicional y los nombres de dos artesanas que dieron su permiso por escrito."

L(
    LR6, 1,
    materials="Lápiz y hoja. Las tres propuestas están escritas aquí y son inventadas para practicar. No necesitas ningún dispositivo.",
    use="Aprenderé a situar una creación audiovisual o escrita: elegir el formato según los recursos disponibles, decidir quién aparece, de dónde vienen las frases en lengua indígena y qué permisos hacen falta. Sirve para contar una situación personal, familiar o comunitaria sin dañar a nadie.",
    prior=["Sé que cada expresión en lengua indígena necesita una fuente y un permiso.", "Sé escribir un texto breve que respeta límites."],
    explain=[
        "Una creación audiovisual combina imagen y sonido, como un video o un audio. Una creación escrita puede ser un cartel, una historieta o una carta. Las TIC son los recursos tecnológicos de la información y la comunicación: el celular, el computador, la grabadora. Se usan los que haya disponibles; si no hay ninguno, un cartel dibujado en papel también es una creación válida.",
        "Para situar la creación me hago cuatro preguntas. ¿Qué situación cuento: personal, familiar o comunitaria? ¿Con qué recurso la hago? ¿Quién aparece o habla, y me dio permiso? ¿De dónde vienen las frases en lengua indígena? Esas frases las entrega una fuente, como el educador o la educadora tradicional. Una frase sacada de internet sin saber de quién es no sirve.",
        "Cuidar a las personas es parte de la creación. La voz, la cara y el nombre de una persona se muestran solo con su permiso y, si es menor de edad, con el permiso de su familia. Tampoco publico datos como direcciones. Y si algo no está claro, detengo el trabajo y pregunto, en vez de seguir y arreglar después.",
    ],
    vocab=[("TIC", "recursos tecnológicos para informar y comunicar, como el celular"), ("audiovisual", "que combina imagen y sonido"), ("permiso", "autorización de una persona para mostrar su voz, cara o nombre"), ("formato", "forma que toma una creación, como audio, video o cartel"), ("situación comunitaria", "algo que ocurre en la comunidad o el barrio")],
    worked=[
        W("Revisar una propuesta completa", P1 + " ¿Qué situación cuenta y de dónde viene la frase en lengua?", ["Es una situación familiar: cómo se saluda en su casa.", "La frase «mari mari» la entregó y autorizó el educador tradicional.", "Hay fuente y permiso."], "cuenta una situación familiar y la frase viene del educador tradicional, que la autorizó"),
        W("Detectar lo que falta", P2 + " ¿Qué dos cosas faltan para poder hacerlo?", ["Reviso los permisos: falta el de las familias.", "Reviso la frase: viene de una página de internet sin fuente.", "Sin esas dos cosas el trabajo se detiene."], "el permiso de las familias y una fuente confiable para la frase en rapa nui"),
    ],
    mistakes=[
        M("Poner en el video la frase en lengua que apareció en una página sin saber de quién era.", "Puede estar mal escrita o ser de otro pueblo.", "Pido la frase al educador o educadora tradicional y la uso solo con su permiso."),
        M("Mostrar la cara de compañeros sin preguntarles a ellos ni a sus familias.", "La imagen de una persona es suya.", "Pido permiso o hago el trabajo con dibujos."),
    ],
    R=[
        ex(P1 + " ¿Qué formato tiene la propuesta 1: un audio o un cartel?", "un audio", "Es un audio de un minuto."),
        ex(P3 + " ¿Qué recurso usa la propuesta 3: papel o computador?", "papel", "Es un cartel dibujado en papel, sin aparatos."),
        ex("Las TIC, ¿son recursos tecnológicos para informar y comunicar o solo juegos?", "recursos tecnológicos para informar y comunicar", "Así se definieron en la clase."),
    ],
    C=[
        ex(P2 + " ¿Qué permiso falta en la propuesta 2?", "el de las familias", "Todavía no tiene el permiso para mostrar sus caras."),
        ex(P3 + " ¿Quiénes dieron permiso por escrito en la propuesta 3?", "dos artesanas", "El texto lo dice."),
        ex("Verdadero o falso: se puede mostrar la cara de una niña si el curso quiere, aunque su familia no lo sepa.", "Falso", "Se necesita el permiso de su familia."),
    ],
    A=[
        ex("Ordena los pasos para preparar una creación. A) pedir los permisos. B) elegir el formato según los recursos. C) decidir qué situación cuento. D) pedir las frases en lengua a la fuente. Escribe las letras en orden.", "C, B, D, A", "Primero se decide qué contar y con qué, y luego se piden frases y permisos."),
        ex(P1 + " " + P2 + " " + P3 + " ¿Cuál de las tres propuestas no depende de ningún aparato?", "la propuesta 3", "Es un cartel en papel."),
        arith("Un curso de 30 estudiantes quiere hacer un video. 18 familias dieron su permiso. ¿De cuántas familias falta el permiso?", "30-18", "Se restan las que dieron permiso del total."),
    ],
    Z=[
        ex(P2 + " Un compañero propone seguir con el video y conseguir los permisos después. ¿Es correcto? Sí o No.", "No", "Los permisos van antes de grabar o mostrar."),
        ex(P3 + " ¿Qué propuesta cuenta una situación comunitaria: la 1 o la 3?", "la 3", "La propuesta 3 cuenta una feria de la comunidad; la 1 cuenta algo de una casa."),
    ],
    D=[
        ex(P1 + " La estudiante quiere agregar una segunda frase en mapuzugun que escuchó a un vecino. El educador solo autorizó «mari mari». ¿Qué debe hacer: agregarla igual o consultar al educador antes?", "consultar al educador antes", "La autorización cubre solo la expresión que él revisó."),
        ex("Tu familia no tiene celular ni computador. ¿Puedes igual hacer una creación para este trabajo: Sí o No?", "Sí", "Un cartel, una historieta o una carta dibujados también valen."),
    ],
    context=[ex("Quieres hacer un audio sobre cómo se prepara la comida de los domingos en tu casa. Una tía aparecerá hablando. ¿Qué haces antes de grabar: le pides permiso a tu tía o lo grabas y se lo cuentas después?", "le pides permiso a tu tía", "La voz de una persona se graba con su permiso.")],
    selfcheck=[
        ex("¿Una frase en lengua indígena puede venir de «una página que vi»? Sí o No.", "No", "Debe venir de una fuente identificada."),
        ex("¿Qué se pide antes de mostrar la imagen de una persona: permiso o una buena música?", "permiso", "La imagen es de la persona."),
        ex("Si no hay celular, ¿se puede crear en papel? Sí o No.", "Sí", "Se usan los recursos disponibles."),
    ],
    task=T(
        "Lee esta propuesta inventada: «Un estudiante quiere hacer un audio de dos minutos sobre cómo se despiden en su casa cuando alguien se va de visita. Tiene el celular de su casa. Quiere decir «maururu» al final, pero todavía no sabe quién se lo puede confirmar. Un familiar aparecerá hablando.» En tu cuaderno responde cuatro preguntas: qué situación cuenta, con qué recurso, quién habla y qué permiso necesita, y de dónde puede venir «maururu». Escribe también una lista de dos cosas que debe hacer antes de grabar.",
        "Situación: familiar, la despedida de una visita. Recurso: la grabadora del celular. Quién habla: el estudiante y un familiar; necesita el permiso del familiar. «Maururu» debe confirmarla un educador o educadora tradicional o una persona de la comunidad rapa nui. Antes de grabar: pedir el permiso del familiar y consultar la expresión.",
        ["responde las cuatro preguntas", "pide el permiso del familiar", "nombra una fuente válida para la expresión", "no inventa lengua"],
        ["cuatro respuestas escritas", "lista de dos pasos"],
        ["grabar sin permiso", "usar la expresión sin consultar"],
        "Si propone grabar primero, pídele que lea de nuevo la lista de pasos y ubique en qué lugar va el permiso.",
    ),
    reinforce="Vuelve a leer las tres propuestas y escribe al lado de cada una qué permiso o fuente tiene.",
    extend="Escribe una propuesta inventada de creación para contar una situación comunitaria de tu barrio, con las cuatro preguntas respondidas.",
)

# ============================================================ LR06 clase 2 · leer un guion modelo
GM = "Guion modelo (inventado para practicar): audio de 1 minuto con 4 escenas. Escena 1 (10 segundos): una estudiante dice «Mari mari, soy una estudiante del 6.º A». El educador tradicional autorizó el saludo. Escena 2 (20 segundos): cuenta que en su casa, cuando llega una visita, se le ofrece una taza de té. Escena 3 (20 segundos): suena el timbre de una puerta y se oyen pasos. Escena 4 (10 segundos): dice «Chaltumay por escucharme». El educador también autorizó esa expresión."

L(
    LR6, 2,
    materials="Lápiz y hoja. El guion modelo está escrito aquí y es inventado para practicar.",
    use="Aprenderé a leer un guion con sus escenas, tiempos, textos y sonidos, y a reconocer qué frases están en lengua indígena y cuáles límites respeta. Sirve para planificar mi propia creación antes de grabar.",
    prior=["Sé elegir un formato según los recursos y pedir permisos.", "Sé que las expresiones en lengua las entrega una fuente."],
    explain=[
        "Un guion es un plan escrito de una creación audiovisual. Se divide en escenas, que son partes cortas con una idea cada una. En cada escena anoto la duración, lo que se dice, los sonidos y, si es un video, la imagen. Con el guion puedo ver el total del tiempo y no me pierdo cuando grabo.",
        "Al leer el guion modelo busco primero las frases en lengua. Aparecen «mari mari» en la escena 1 y «chaltumay» en la escena 4, y el guion avisa que el educador las autorizó. Luego busco lo que protege a las personas: la estudiante no dice su nombre completo ni su dirección. Un buen guion deja claro qué se muestra y qué se guarda.",
        "También miro la coherencia. El saludo va al comienzo, el relato en el medio y el agradecimiento al final, como en una carta. Si cambio el orden, la creación se entiende peor. Cuando algo del guion no se entiende, lo anoto como pregunta y no lo completo con datos inventados.",
    ],
    vocab=[("guion", "plan escrito de una creación, dividido en escenas"), ("escena", "parte corta de una creación con una idea"), ("duración", "tiempo que dura algo"), ("sonido de fondo", "sonido que acompaña lo que se dice"), ("coherencia", "orden claro entre las partes")],
    worked=[
        W("Encontrar las frases en lengua", GM + " ¿En qué escenas hay frases en lengua indígena?", ["Busco expresiones que no estén en castellano.", "«Mari mari» está en la escena 1.", "«Chaltumay» está en la escena 4."], "en las escenas 1 y 4"),
        W("Calcular el tiempo total", GM + " ¿Cuántos segundos suman las cuatro escenas?", ["Anoto las duraciones: 10, 20, 20 y 10.", "Sumo 10 más 20 más 20 más 10.", "El total es 60 segundos, es decir un minuto."], "60 segundos"),
    ],
    mistakes=[
        M("Agregar al guion el nombre completo y la dirección de la estudiante.", "Son datos personales que no hace falta mostrar.", "Dejo solo lo necesario, como «una estudiante del 6.º A»."),
        M("Cambiar el orden de las escenas y poner el agradecimiento primero.", "El texto pierde coherencia: se agradece antes de saludar.", "Mantengo saludo, relato y agradecimiento en ese orden."),
    ],
    R=[
        ex(GM + " ¿Cuántas escenas tiene el guion modelo?", "4", "El guion lo dice y las enumera."),
        ex(GM + " ¿Qué saludo en lengua se dice en la escena 1?", "mari mari", "Está entre comillas."),
        ex(GM + " ¿Qué ofrecen en la casa cuando llega una visita según la escena 2?", "una taza de té", "La escena 2 lo cuenta."),
    ],
    C=[
        ex(GM + " ¿Quién autorizó las expresiones en lengua?", "el educador tradicional", "El guion lo señala."),
        ex(GM + " ¿Qué sonido hay en la escena 3?", "el timbre de una puerta y pasos", "La escena 3 lo describe."),
        ex(GM + " Verdadero o falso: la estudiante da su dirección en el audio.", "Falso", "No aparece ninguna dirección."),
    ],
    A=[
        arith(GM + " Las escenas 2 y 3 duran 20 segundos cada una. ¿Cuántos segundos duran juntas?", "20+20", "Se suman las dos duraciones."),
        arith(GM + " Un compañero propone que cada escena dure 15 segundos. ¿Cuántos segundos tendría el audio con las 4 escenas?", "15*4", "Cuatro escenas de 15 segundos cada una."),
        ex(GM + " Ordena las partes de una creación: A) agradecimiento. B) relato. C) saludo. Escribe las letras en orden.", "C, B, A", "Primero se saluda, luego se cuenta y al final se agradece."),
    ],
    Z=[
        ex(GM + " Un compañero quiere agregar «y mi dirección es la calle del Sol 120» en la escena 1. ¿Es buena idea? Sí o No.", "No", "Una dirección es un dato personal que no se publica."),
        ex(GM + " ¿La escena 3 incluye una frase en lengua indígena? Sí o No.", "No", "Solo hay sonidos: timbre y pasos."),
    ],
    D=[
        ex(GM + " Un estudiante cambia la escena 4 por «Maururu por escucharme». ¿Respeta lo que autorizó el educador? Sí o No.", "No", "El educador autorizó «chaltumay», no «maururu»."),
        ex(GM + " Elige la mejor mejora del guion. A) agregar una frase nueva en lengua que alguien dijo en la calle. B) pedir al educador que revise el guion completo. Escribe la letra.", "B", "Así se confirma que respeta lo autorizado."),
    ],
    context=[ex("Preparas un audio sobre la visita de un abuelo a tu casa. En el guion quieres incluir su apellido y su dirección. ¿Los dejas o los sacas y escribes «un abuelo de mi familia»?", "los sacas y escribes «un abuelo de mi familia»", "Los datos personales no se publican.")],
    selfcheck=[
        ex("Una escena, ¿es una parte corta con una idea o el título del trabajo?", "una parte corta con una idea", "Así se definió en la clase."),
        ex("¿Dónde va el saludo en el guion modelo: al comienzo o al final?", "al comienzo", "Está en la escena 1."),
        ex("¿Debo completar con datos inventados lo que el guion no dice? Sí o No.", "No", "Se anota la duda para preguntar."),
    ],
    task=T(
        "Lee este guion inventado: «Cartel digital o dibujado, 3 partes. Parte 1: título «Mi barrio», con el saludo «iorana» que autorizó una educadora tradicional. Parte 2: un dibujo de la plaza y un texto que cuenta que los sábados hay una feria. Parte 3: la frase «maururu», que la educadora también autorizó, y el nombre del curso.» En tu cuaderno escribe: las partes con frases en lengua, el orden saludo-relato-agradecimiento si se cumple o no, y dos datos personales que NO deberían aparecer en el cartel.",
        "Frases en lengua: parte 1 (iorana) y parte 3 (maururu). El orden se cumple: saludo en la parte 1, relato en la 2 y agradecimiento en la 3. Datos que no deben aparecer: dirección de una casa y nombre completo de una persona.",
        ["identifica las partes con frases en lengua", "verifica el orden", "nombra dos datos personales que no deben aparecer", "no agrega frases en lengua"],
        ["respuestas escritas en el cuaderno"],
        ["confundir un nombre propio con una expresión en lengua", "olvidar los datos personales"],
        "Pide que subraye en el guion cada frase en lengua y diga quién la autorizó.",
    ),
    reinforce="Copia el guion modelo en una tabla de cuatro filas con escena, segundos y qué se dice.",
    extend="Escribe un guion propio de tres escenas de 15 segundos, sin ninguna frase en lengua, para contar cómo llegas a la escuela.",
)

# ============================================================ LR06 clase 3 · coherencia y representación respetuosa
IMG = "Lista de imágenes (inventada para practicar) para un video sobre «La feria de mi barrio», donde una artesana mapuche, que dio su permiso, vende lana: 1) el puesto de lana, tomado de lejos y sin mostrar a personas. 2) un disfraz que el curso inventa para parecer «indígena». 3) la artesana mostrando su lana, con su permiso por escrito. 4) un dibujo hecho por el curso de la feria. 5) una foto de una ceremonia sacada de internet. 6) un mapa dibujado del barrio con la ubicación de la feria."

L(
    LR6, 3,
    materials="Lápiz y hoja. La lista de imágenes está escrita aquí y es inventada para practicar.",
    use="Aprenderé a relacionar las imágenes, los sonidos y las frases de una creación con el mensaje que quiero contar, y a evitar estereotipos y usos sin permiso. Sirve para contar situaciones de mi comunidad con respeto.",
    prior=["Sé leer un guion y reconocer sus escenas.", "Sé que la imagen y la voz de una persona se usan con su permiso."],
    explain=[
        "Cada imagen y cada sonido de una creación ayudan a decir algo. Para que el mensaje sea claro, elijo solo lo que se relaciona con lo que quiero contar. Si cuento una feria de lana, las imágenes de la lana, del puesto y de la feria tienen sentido. Una imagen que no tiene relación, aunque sea llamativa, confunde.",
        "Un estereotipo es una imagen simplificada y repetida de un grupo de personas, como mostrar a un pueblo indígena solo con disfraces o solo en el pasado. Los pueblos originarios son pueblos actuales, con personas distintas entre sí. Por eso no uso disfraces para «parecer» de un pueblo, ni imágenes de ceremonias que no me autorizaron a mostrar.",
        "Para mostrar bien a las personas, uso imágenes con permiso, dibujos hechos por mí o fotos de lugares sin personas. Y las frases en lengua indígena van donde corresponden: un saludo al comienzo, un agradecimiento al final. Cuando dudo si una imagen es respetuosa, consulto al educador o a la educadora tradicional o a la comunidad.",
    ],
    vocab=[("estereotipo", "imagen simplificada y repetida de un grupo de personas"), ("mensaje", "idea que quiero comunicar"), ("relación", "vínculo entre dos cosas"), ("representar", "mostrar algo con imágenes, palabras o sonidos"), ("respetuoso", "que cuida a las personas y sus creencias")],
    worked=[
        W("Elegir imágenes que se relacionan", IMG + " ¿La imagen 1 se relaciona con el mensaje de la feria de lana?", ["El mensaje es la feria de lana del barrio.", "La imagen 1 muestra el puesto de lana sin personas.", "Se relaciona y no usa la imagen de nadie."], "sí, muestra el puesto de lana sin mostrar personas"),
        W("Detectar un estereotipo", IMG + " ¿Por qué la imagen 2 no sirve?", ["La imagen 2 es un disfraz inventado para «parecer» indígena.", "Un disfraz muestra una idea simplificada, no a personas reales.", "Eso es un estereotipo."], "porque es un estereotipo: un disfraz no representa a las personas reales"),
    ],
    mistakes=[
        M("Usar una foto de una ceremonia sacada de internet porque «se ve linda».", "No sé quién la tomó ni si las personas autorizaron mostrarla.", "Uso dibujos propios o fotos con permiso."),
        M("Mostrar a los pueblos originarios solo en el pasado.", "Son pueblos actuales, con personas de hoy.", "Cuento situaciones actuales, como una feria de hoy."),
    ],
    R=[
        ex(IMG + " ¿Qué muestra la imagen 4: un dibujo del curso o una foto de internet?", "un dibujo del curso", "La lista lo dice."),
        ex(IMG + " ¿Quién dio su permiso por escrito en la imagen 3?", "la artesana", "Así lo indica la imagen 3."),
        ex("Un estereotipo, ¿es una imagen simplificada y repetida de un grupo de personas o una foto muy nítida?", "una imagen simplificada y repetida de un grupo de personas", "Esa es la definición de la clase."),
    ],
    C=[
        ex(IMG + " ¿Qué imagen es un estereotipo según la clase: la 2 o la 4?", "la 2", "El disfraz inventado simplifica a un pueblo."),
        ex(IMG + " Verdadero o falso: la imagen 5 sirve porque la foto de la ceremonia se ve linda.", "Falso", "No se sabe si fue autorizada y no se relaciona con la feria."),
        ex(IMG + " ¿Cuál imagen ayuda a ubicar la feria: el mapa de la imagen 6 o el disfraz de la imagen 2?", "el mapa de la imagen 6", "Muestra dónde está la feria."),
    ],
    A=[
        ex(IMG + " ¿Cuáles son los números de las dos imágenes que no se deben usar, una por ser un estereotipo y otra por no tener permiso ni relación con la feria?", "la 2 y la 5", "La 2 es un disfraz estereotipado y la 5 es una foto de ceremonia sin permiso."),
        arith(IMG + " La lista tiene 6 imágenes y 2 de ellas no se pueden usar. ¿Cuántas imágenes se pueden usar?", "6-2", "Se restan las dos que no se usan del total."),
        ex("Une cada frase en lengua con su lugar en el video. 1) «iorana». 2) «maururu». Lugares: A) al final. B) al comienzo. Escribe los dos pares.", "1-B, 2-A", "El saludo va al comienzo y el agradecimiento al final."),
    ],
    Z=[
        ex(IMG + " Un compañero dice que la imagen 2 es linda y que por eso conviene. ¿La belleza del disfraz resuelve el problema del estereotipo? Sí o No.", "No", "El problema es que muestra una idea simplificada del pueblo."),
        ex("Para mostrar cómo vive hoy una familia, ¿es mejor un dibujo propio de su casa con su permiso o un disfraz? Escribe cuál.", "un dibujo propio de su casa con su permiso", "Cuenta una situación actual y real."),
    ],
    D=[
        ex(IMG + " Pedro cree que sí se puede usar la imagen 5 si le pone una nota que diga «foto de internet». ¿Resuelve el problema esa nota? Sí o No.", "No", "La nota no da el permiso de las personas que aparecen."),
        ex("Una niña quiere mostrar una danza en su video para representar a un pueblo, pero no sabe si la comunidad autoriza mostrarla. ¿Qué debe hacer: mostrarla igual o consultar a un educador o educadora tradicional?", "consultar a un educador o educadora tradicional", "Una práctica cultural no se muestra sin autorización de quienes la cuidan."),
    ],
    context=[ex("Preparas un cartel sobre la fiesta de tu barrio, y alguien propone usar plumas de colores para «parecer indígena». ¿Las usas o cuentas la fiesta como realmente es?", "cuentas la fiesta como realmente es", "Evita el estereotipo y respeta lo real.")],
    selfcheck=[
        ex("¿Un disfraz muestra a las personas reales o una idea simplificada?", "una idea simplificada", "Eso es un estereotipo."),
        ex("¿Una imagen debe relacionarse con el mensaje de la creación? Sí o No.", "Sí", "Si no se relaciona, confunde."),
        ex("¿Los pueblos originarios son pueblos del pasado o de hoy también?", "de hoy también", "Son pueblos actuales."),
    ],
    task=T(
        "Lee esta lista inventada de imágenes para un audiovisual sobre «El taller de cestería de mi comunidad» (una artesana dio su permiso): 1) el cesto terminado sobre una mesa. 2) un dibujo del taller hecho por el curso. 3) una persona desconocida con un disfraz «de indígena». 4) la artesana, con su permiso por escrito, mostrando sus manos. En tu cuaderno marca con una cruz las imágenes que no se deben usar, explica en una oración por qué y propone una imagen nueva que sí sirva.",
        "No se debe usar la imagen 3 porque es un disfraz que simplifica a un pueblo y no se relaciona con el taller real. Imagen nueva: un dibujo del curso de los cestos en estantes.",
        ["marca la imagen 3", "explica la razón con la idea de estereotipo", "propone una imagen respetuosa y relacionada", "no usa personas sin permiso"],
        ["cruz en la imagen que no sirve", "explicación y propuesta escritas"],
        ["no ver el estereotipo", "proponer fotos de internet"],
        "Si no identifica el estereotipo, pídele que describa qué muestra realmente el disfraz y a quién.",
    ),
    reinforce="Vuelve a leer la lista de imágenes de la clase y escribe una S o una N según se pueda usar o no.",
    extend="Haz un dibujo de una feria de tu barrio en el que no aparezca ninguna persona identificable y escribe una frase de presentación.",
)

# ============================================================ LR06 clase 4 · créditos y atribución
CRE = "Créditos modelo (inventados para practicar): Creación: audio «Mi barrio hoy». Autor: un estudiante del 6.º A. Fuente de las expresiones en lengua: «mari mari» y «chaltumay», entregadas y autorizadas por el educador tradicional de la Escuela Ejemplo. Permiso de voz: una vecina que aparece contando la feria, con permiso escrito. Recursos TIC: la grabadora del celular de su familia. Aviso: lo que se cuenta es de este barrio y no de todas las comunidades."

L(
    LR6, 4,
    materials="Lápiz y hoja. Los créditos modelo están escritos aquí y son inventados para practicar.",
    use="Aprenderé a escribir los créditos de una creación, atribuyendo quién la hizo, quién entregó las frases en lengua indígena, quién dio permiso y con qué recursos. Sirve para reconocer a quienes aportaron y no apropiarme de lo que no es mío.",
    prior=["Sé planificar una creación con guion, imágenes respetuosas y permisos.", "Sé atribuir una información a su fuente."],
    explain=[
        "Los créditos son un texto breve, al final o al comienzo de una creación, que dice quién la hizo y quién colaboró. Un buen crédito nombra al autor, la fuente de las expresiones en lengua indígena, las personas que dieron permiso para mostrar su voz o su imagen y los recursos usados. Así reconozco el trabajo de otras personas y no me apropio de él.",
        "Apropiarse es presentar como propio algo que pertenece a otra persona o comunidad. Si una vecina contó lo que sabe de la feria, no digo «yo lo investigué»: digo que ella lo contó y que dio permiso. Si el educador tradicional entregó «mari mari», lo escribo en los créditos. También aclaro el límite: mi creación cuenta mi barrio, no a todas las comunidades.",
        "Escribir créditos ayuda a revisar mi propio trabajo. Si no puedo completar una línea, por ejemplo la del permiso de voz, significa que me falta algo y debo detenerme. Antes de mostrar la creación, le pido a la fuente que lea los créditos para confirmar que están bien.",
    ],
    vocab=[("créditos", "texto que dice quién hizo y quién colaboró en una creación"), ("colaborar", "ayudar con un aporte propio"), ("apropiarse", "presentar como propio algo que es de otra persona o comunidad"), ("autor", "persona que hace una creación"), ("recurso", "cosa que se usa para hacer algo")],
    worked=[
        W("Completar una línea de los créditos", CRE + " ¿Quién entregó las expresiones en lengua?", ["Busco la línea «Fuente de las expresiones en lengua».", "Dice que fueron entregadas y autorizadas por el educador tradicional de la Escuela Ejemplo.", "Esa es la fuente."], "el educador tradicional de la Escuela Ejemplo"),
        W("Detectar una apropiación", "Un estudiante escribe en su audio: «Yo investigué cómo funciona la feria». Pero en realidad se lo contó una vecina que dio permiso. ¿Qué debe cambiar?", ["Revisa de dónde vino la información: de la vecina.", "Decir «yo investigué» oculta a quien la contó.", "Debe poner a la vecina en los créditos."], "debe atribuir la información a la vecina en los créditos"),
    ],
    mistakes=[
        M("No poner en los créditos a la persona que entregó una frase en lengua.", "Parece que la frase la inventé yo.", "Nombro a la fuente y escribo que autorizó el uso."),
        M("Escribir créditos sin aclarar que mi creación cuenta solo mi barrio.", "Parece que hablo de todas las comunidades.", "Agrego un aviso de límite."),
    ],
    R=[
        ex(CRE + " ¿Cómo se llama la creación de los créditos modelo?", "Mi barrio hoy", "Aparece en la primera línea."),
        ex(CRE + " ¿Qué recurso TIC se usó?", "la grabadora del celular de su familia", "La línea «Recursos TIC» lo dice."),
        ex("Los créditos, ¿dicen quién hizo y quién colaboró en una creación o solo el título?", "quién hizo y quién colaboró en una creación", "Esa es su función."),
    ],
    C=[
        ex(CRE + " ¿Quién dio permiso de voz?", "una vecina", "La línea «Permiso de voz» lo dice."),
        ex(CRE + " ¿Qué aviso hacen los créditos modelo sobre el alcance de lo que se cuenta?", "que lo que se cuenta es de este barrio y no de todas las comunidades", "La última línea lo dice."),
        ex("Apropiarse, ¿es presentar como propio algo que es de otra persona o agradecer a quien ayudó?", "presentar como propio algo que es de otra persona", "Esa es la definición."),
    ],
    A=[
        ex("Ordena las líneas de los créditos. A) fuente de las expresiones en lengua. B) título de la creación. C) aviso de límite. D) autor. Escribe las letras en orden.", "B, D, A, C", "Se parte por el título y el autor, se nombran las fuentes y se cierra con el límite."),
        arith(CRE + " Los créditos tienen 6 líneas: creación, autor, fuente, permiso, recursos y aviso. Un estudiante escribió solo 4 líneas. ¿Cuántas líneas le faltan?", "6-4", "Se restan las escritas de las seis que debe tener."),
        ex(CRE + " Elige la mejor línea de créditos para una creación nueva. A) «Frases en lengua: de un video que vi». B) «Frases en lengua: entregadas y autorizadas por la educadora tradicional de mi escuela». Escribe la letra.", "B", "Nombra una fuente identificada y su autorización."),
    ],
    Z=[
        ex(CRE + " Un estudiante dice que no hace falta poner en los créditos a la vecina porque ella no lo pidió. ¿Es correcto? Sí o No.", "No", "Se reconoce a quien aportó, aunque no lo pida."),
        ex(CRE + " ¿Qué indica que una línea de los créditos no se puede completar: que falta una fuente o permiso, o que la creación quedó muy bonita?", "que falta una fuente o permiso", "Si no puedo completar una línea, me detengo."),
    ],
    D=[
        ex("Dos estudiantes entregan sus créditos. Rosa escribe «Fuente: mi imaginación» para «chaltumay». Nico escribe «Fuente: educador tradicional que autorizó». ¿Quién atribuyó bien la expresión en lengua?", "Nico", "La expresión no sale de la imaginación: la entregó una fuente."),
        ex("Quieres agradecer a la vecina por la entrevista, pero ella pidió que no se publique su nombre. ¿Escribes «una vecina del barrio» o su nombre completo?", "una vecina del barrio", "Respetas lo que ella pidió."),
    ],
    context=[ex("Terminaste un video corto sobre la feria con ayuda de tu curso y de una persona que contó su historia. ¿Pones los créditos al final o los dejas fuera para que el video sea más corto?", "pones los créditos al final", "Reconoces a quienes aportaron.")],
    selfcheck=[
        ex("¿Los créditos nombran a la fuente de las frases en lengua? Sí o No.", "Sí", "Es una de sus líneas."),
        ex("¿Qué palabra describe presentar como propio algo ajeno: «colaborar» o «apropiarse»?", "apropiarse", "Es la definición vista."),
        ex("Si no puedo completar el permiso de voz, ¿sigo igual o me detengo?", "me detengo", "Falta algo necesario."),
    ],
    task=T(
        "Escribe en tu cuaderno los créditos de esta creación inventada: un cartel llamado «Nuestra plaza» hecho por un estudiante del 6.º B, que usa el saludo «iorana» entregado y autorizado por una educadora tradicional de su escuela, con el dibujo de una vecina que dio permiso para que se muestren sus manos, hecho con lápices y papel, y que cuenta solo la plaza de su barrio. Usa seis líneas: creación, autor, fuente de las expresiones, permiso, recursos y aviso.",
        "Creación: cartel «Nuestra plaza». Autor: un estudiante del 6.º B. Fuente de las expresiones en lengua: «iorana», entregada y autorizada por una educadora tradicional de su escuela. Permiso: una vecina que permitió mostrar sus manos. Recursos: lápices y papel. Aviso: el cartel cuenta solo la plaza de este barrio.",
        ["tiene las seis líneas", "nombra la fuente de la expresión en lengua", "indica el permiso", "incluye el aviso de límite"],
        ["seis líneas escritas"],
        ["olvidar la fuente", "no incluir el aviso"],
        "Si falta una línea, pídele que revise la lista de seis y diga cuál no aparece.",
    ),
    reinforce="Copia los créditos modelo y pon al lado de cada línea el nombre de la persona o recurso que menciona.",
    extend="Escribe los créditos de una creación tuya imaginaria sobre un recuerdo de familia, incluyendo el aviso de límite.",
)

# ============================================================ LR06 clase 5 · contrastar dos creaciones sin jerarquizar
CRA = "Creación A (inventada para practicar): un audio de 2 minutos, hecho con el celular de una familia, que cuenta una comida de domingo y empieza con «mari mari» autorizado por el educador tradicional. Pide permiso de voz a dos familiares. Llega a quienes tengan un reproductor de audio."
CRB = "Creación B (inventada): un cartel dibujado en papel, hecho sin aparatos, que cuenta la feria del barrio y empieza con «iorana» autorizado por una educadora tradicional. Muestra solo dibujos, sin personas. Llega a quienes pasen por el pasillo de la escuela."

L(
    LR6, 5,
    materials="Lápiz y hoja. Las dos creaciones están descritas aquí y son inventadas para practicar.",
    use="Aprenderé a comparar dos creaciones con los mismos criterios (recursos, permisos, a quién llegan y cómo usan la lengua) sin decir que una es superior por el pueblo, la lengua o el recurso que usa. Sirve para valorar distintas formas de contar lo propio.",
    prior=["Sé armar guiones, créditos y permisos.", "Sé comparar sin jerarquizar pueblos ni lenguas."],
    explain=[
        "Dos creaciones pueden contar cosas distintas con recursos distintos. Para compararlas uso criterios que sirvan a las dos: qué recursos necesita, qué permisos pide, a quién llega y qué expresión en lengua indígena usa y quién la autorizó. Respondo cada criterio para cada creación y luego escribo semejanzas y diferencias.",
        "Una creación no es mejor porque use más tecnología. Un audio puede llegar a más lugares, pero necesita un aparato; un cartel en papel llega a quienes pasan por un pasillo y no necesita nada. Tampoco una lengua ni un pueblo vale más que otro: no comparo diciendo «la mapuche es mejor» ni «la rapa nui es más linda». Solo observo qué se parece y qué cambia.",
        "Sí puedo decir cuál creación se ajusta mejor a una situación concreta, si lo justifico con un criterio observable. Por ejemplo: si el curso no tiene aparatos, el cartel se ajusta mejor. Cierro la comparación con una frase que nombre una semejanza y una diferencia, sin palabras como «mejor», «más verdadero» o «más puro».",
    ],
    vocab=[("criterio", "aspecto que se usa para comparar"), ("alcance", "a quiénes llega una creación"), ("ajustarse", "responder bien a una situación concreta"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian")],
    worked=[
        W("Comparar con un criterio", CRA + " " + CRB + " Compara los recursos que necesita cada una.", ["La creación A necesita un celular y un reproductor de audio.", "La creación B necesita solo papel y lápices.", "Los recursos que necesitan son distintos."], "A necesita celular y reproductor; B solo papel y lápices"),
        W("Reconocer una jerarquización", "Alguien dice: «La creación A es mejor porque es más moderna». ¿Compara o jerarquiza?", ["La frase dice que A es mejor por usar tecnología.", "«Moderna» no es un criterio que sirva para valorar el contenido.", "Pone una creación sobre otra."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «el audio es mejor porque usa tecnología».", "Más tecnología no significa mejor creación.", "Comparo con criterios: recursos, permisos y alcance."),
        M("Decir que la creación con «mari mari» vale más que la que usa «iorana».", "Ninguna lengua vale más que otra.", "Comparo cómo usa cada una su expresión y quién la autorizó."),
    ],
    R=[
        ex(CRA + " ¿Qué expresión en lengua usa la creación A?", "mari mari", "La descripción lo dice."),
        ex(CRB + " ¿Qué expresión en lengua usa la creación B?", "iorana", "La descripción lo dice."),
        ex(CRB + " ¿Qué recursos usa la creación B: papel y lápices o un celular?", "papel y lápices", "Está hecha sin aparatos."),
    ],
    C=[
        ex(CRA + " ¿A quiénes llega la creación A?", "a quienes tengan un reproductor de audio", "La descripción lo indica."),
        ex(CRB + " ¿A quiénes llega la creación B?", "a quienes pasen por el pasillo de la escuela", "La descripción lo indica."),
        ex("Verdadero o falso: una creación es mejor solo porque usa más tecnología.", "Falso", "El valor depende de lo que cuenta, del respeto y del permiso, no del aparato."),
    ],
    A=[
        ex(CRA + " " + CRB + " Completa con A o B: pide permiso de voz a dos familiares la creación ___; muestra solo dibujos, sin personas, la creación ___. Escribe las dos letras en orden.", "A, B", "La A pide permiso de voz y la B no muestra personas."),
        arith(CRA + " La creación A dura 2 minutos. ¿Cuántos segundos son?", "2*60", "Un minuto tiene 60 segundos."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «La A usa un aparato y la B no». 2) «La B es más pura». 3) «Las dos empiezan con una expresión autorizada». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 pone una creación sobre otra."),
    ],
    Z=[
        ex(CRA + " " + CRB + " El curso no tiene celulares ni computadores. ¿Qué creación se ajusta mejor a esa situación: la A o la B?", "la B", "Se hace sin aparatos."),
        ex(CRA + " " + CRB + " Una niña dice: «La B es mejor persona que la A». ¿Tiene sentido hablar así? Sí o No.", "No", "Las creaciones no son personas y no se valoran como si lo fueran."),
    ],
    D=[
        ex(CRA + " " + CRB + " Elige la mejor frase de cierre. A) «Las dos creaciones cuentan una situación de su comunidad y empiezan con una expresión autorizada; el audio necesita aparatos y el cartel no». B) «El audio es más importante porque llega más lejos». Escribe la letra.", "A", "Resume semejanza y diferencia con criterios observables."),
        ex("Descubres que no puedes comprobar si el saludo del cartel B está bien escrito. ¿Qué haces: lo dejas o lo consultas con la educadora tradicional?", "lo consultas con la educadora tradicional", "Solo quien conoce la lengua puede confirmar la escritura."),
    ],
    context=[ex("En tu escuela, un curso hizo un audio y otro un cartel sobre el mismo evento del barrio. Te piden decir cuál es mejor. ¿Explicas qué se parece y qué cambia, o dices que uno es mejor sin razones?", "explicas qué se parece y qué cambia", "Así comparas sin jerarquizar.")],
    selfcheck=[
        ex("¿Qué se compara en esta clase: dos creaciones o dos pueblos?", "dos creaciones", "Se comparan las creaciones A y B."),
        ex("¿«Más puro» compara o jerarquiza?", "jerarquiza", "Pone una cosa sobre otra."),
        ex("¿Usamos los mismos criterios para las dos creaciones? Sí o No.", "Sí", "Así la comparación es justa."),
    ],
    task=T(
        "Lee estas dos creaciones inventadas. Creación 1: una historieta en papel de 6 recuadros sobre el día de la cosecha en una huerta comunitaria; empieza con «mari mari» autorizado por el educador tradicional; no muestra personas reales. Creación 2: un video de 90 segundos con el celular de la escuela, sobre el recreo; empieza con «iorana» autorizado por una educadora tradicional; las familias dieron permiso para mostrar a sus hijos. En tu cuaderno haz una tabla con estas filas: recursos, permisos, a quién llega y expresión en lengua. Luego escribe una frase de cierre con una semejanza y una diferencia, sin jerarquizar.",
        "Recursos: papel / celular de la escuela. Permisos: no muestra personas reales / permisos de las familias. Alcance: quienes lean la historieta / quienes vean el video. Expresión: mari mari / iorana. Cierre: «Las dos creaciones empiezan con una expresión autorizada; la historieta no muestra personas y el video tiene el permiso de las familias.»",
        ["completa las cuatro filas para ambas creaciones", "usa los mismos criterios", "escribe una semejanza y una diferencia", "no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que una es mejor por usar tecnología", "no completar una fila"],
        "Si aparece una jerarquización, pídele que cambie esa palabra por un criterio observable de la tabla.",
    ),
    reinforce="Copia las dos creaciones del ejemplo y subraya en cada una la expresión en lengua y quién la autorizó.",
    extend="Escribe una comparación breve entre una carta y un audio para dar las gracias, sin jerarquizar.",
)


# ============================================================ LS01 clase 1 · situar un relato
R1 = "Relato 1 (inventado para practicar; Valle Ejemplo es un lugar y un pueblo ficticios y no describe a ningún pueblo real): Al terminar la cosecha, las familias de Valle Ejemplo se reúnen en la plaza. Una abuela cuenta cómo el valle recibió su primer río. Las niñas y los niños llevan semillas en un canasto y las ponen sobre una mesa larga. Las personas dicen que la tierra es como una persona mayor a la que se agradece. Después comparten una comida y cada familia teje una cinta de color que se cuelga en un árbol de la plaza."
FR = "Ficha del relato (inventada): Pueblo o cultura: Valle Ejemplo (ficticio). Quien cuenta: una profesora de la escuela, que lo escribió para practicar. Evento: la fiesta de fin de cosecha. Permiso para contarlo: sí, es un relato inventado. Lenguajes artísticos que aparecen: el relato oral, las cintas tejidas y la mesa de semillas."

L(
    LS1, 1,
    materials="Lápiz y hoja. El relato y la ficha están escritos aquí y son inventados para practicar. Puede leerlos en voz alta una persona adulta.",
    use="Aprenderé a situar una historia sobre un evento sociocultural o espiritual de otro pueblo: de qué pueblo es, quién la cuenta, qué evento describe y con qué permiso. Sirve para disfrutar y comprender historias de otras culturas sin mezclarlas ni inventar detalles.",
    prior=["Sé que cada pueblo tiene su propia historia y su propia forma de entender el mundo.", "Sé que una información necesita una fuente y un permiso."],
    explain=[
        "Un evento sociocultural es un encuentro importante para una comunidad, como una fiesta, una cosecha o una conmemoración. Cuando además tiene un sentido espiritual, se vincula con las creencias de ese pueblo. Disfrutar una historia es dejar que me conmueva o me interese; comprenderla es entender qué cuenta, quién la cuenta y para quién.",
        "Antes de interpretar una historia la ubico con una ficha: ¿de qué pueblo o cultura es?, ¿quién la cuenta?, ¿qué evento relata? y ¿tengo permiso para contarla? Si una historia es de un pueblo real y no sé quién la cuenta ni si autoriza difundirla, me detengo y consulto al educador o a la educadora tradicional. Aquí usamos un relato inventado para practicar.",
        "La cosmovisión es la forma en que un pueblo entiende el mundo y su lugar en él. Cada pueblo tiene la suya, y no hay una mejor que otra. En el relato de Valle Ejemplo aparece la idea de la tierra como una persona mayor a la que se agradece. Esa idea pertenece a ese relato ficticio y no puedo atribuirla a otros pueblos ni decir que todos los pueblos piensan igual.",
    ],
    vocab=[("evento sociocultural", "encuentro importante para una comunidad, como una fiesta"), ("cosmovisión", "forma en que un pueblo entiende el mundo"), ("espiritual", "relacionado con las creencias de un pueblo"), ("ficticio", "inventado, que no existe de verdad"), ("lenguaje artístico", "forma de expresión como el relato, la música o el tejido")],
    worked=[
        W("Ubicar el evento", R1 + " " + FR + " ¿Qué evento relata el relato 1?", ["Leo la línea «Evento» de la ficha.", "Dice la fiesta de fin de cosecha.", "El relato la confirma: las familias se reúnen al terminar la cosecha."], "la fiesta de fin de cosecha de Valle Ejemplo"),
        W("Reconocer lenguajes artísticos", R1 + " " + FR + " ¿Qué lenguajes artísticos aparecen?", ["La ficha enumera tres.", "Son el relato oral, las cintas tejidas y la mesa de semillas.", "Los cuento: tres."], "el relato oral, las cintas tejidas y la mesa de semillas"),
    ],
    mistakes=[
        M("Decir que lo que pasa en Valle Ejemplo pasa en todos los pueblos.", "Es un relato de un solo pueblo, además ficticio.", "Digo «en el relato de Valle Ejemplo» y no generalizo."),
        M("Contar una historia de un pueblo real como si fuera mía.", "No es mía: pertenece a quien la cuida.", "Nombro a quien la cuenta y pido permiso."),
    ],
    R=[
        ex(R1 + " ¿Dónde se reúnen las familias al terminar la cosecha?", "en la plaza", "El relato lo dice al comienzo."),
        ex(FR + " ¿Quién escribió el relato según la ficha?", "una profesora de la escuela", "La ficha lo dice en «Quien cuenta»."),
        ex("Un evento sociocultural, ¿es un encuentro importante para una comunidad o un objeto de la sala?", "un encuentro importante para una comunidad", "Así se definió en la clase."),
    ],
    C=[
        ex(R1 + " ¿Qué ponen sobre una mesa larga las niñas y los niños?", "semillas", "El relato dice que llevan semillas en un canasto."),
        ex(R1 + " ¿Qué idea tiene la gente de Valle Ejemplo sobre la tierra?", "que es como una persona mayor a la que se agradece", "El relato la cuenta."),
        ex(FR + " Verdadero o falso: la ficha indica que Valle Ejemplo es un pueblo real de Chile.", "Falso", "La ficha dice que es ficticio."),
    ],
    A=[
        arith(R1 + " Si hay 14 familias en la plaza, llegan 3 familias más y cada una teje una cinta, ¿cuántas cintas se cuelgan en el árbol?", "14+3", "Se suman las familias, porque cada una teje una cinta."),
        ex(FR + " Ordena para situar una historia. A) averiguo si hay permiso. B) anoto de qué pueblo o cultura es. C) anoto quién la cuenta. Escribe las letras en orden.", "B, C, A", "Primero el pueblo, luego la voz y después el permiso."),
        ex(R1 + " Une cada elemento con su lenguaje artístico. 1) la abuela que cuenta. 2) la cinta de color. Opciones: A) tejido. B) relato oral. Escribe los dos pares.", "1-B, 2-A", "La abuela usa el relato oral y la cinta es un tejido."),
    ],
    Z=[
        ex(R1 + " Un estudiante dice: «Todos los pueblos creen que la tierra es una persona mayor». ¿Está bien? Sí o No.", "No", "Esa idea es del relato de Valle Ejemplo, no de todos los pueblos."),
        ex(FR + " Si el relato fuera de un pueblo real y no tuvieras permiso, ¿qué harías: contarlo igual o consultar al educador o a la educadora tradicional?", "consultar al educador o a la educadora tradicional", "Una historia se cuenta con permiso."),
    ],
    D=[
        ex(R1 + " Elige la mejor frase para presentar el relato. A) «En el relato inventado de Valle Ejemplo, las familias agradecen a la tierra en una fiesta». B) «Así celebran todos los pueblos la cosecha». Escribe la letra.", "A", "Dice de dónde viene y no generaliza."),
        ex("Una persona mayor de tu comunidad te cuenta una historia de su pueblo y te pide que no la repitas fuera de tu casa. ¿La cuentas en clase o respetas su petición?", "respetas su petición", "Una historia se cuenta solo con el permiso de quien la entrega."),
    ],
    context=[ex("Una compañera trae a clase una historia de un pueblo que aprendió en una visita. No recuerda quién se la contó. ¿La presentan igual al curso o primero averiguan quién la contó y si autorizó difundirla?", "primero averiguan quién la contó y si autorizó difundirla", "Sin fuente y sin permiso no se difunde.")],
    selfcheck=[
        ex("¿Qué es una cosmovisión: la forma en que un pueblo entiende el mundo o un tipo de fiesta?", "la forma en que un pueblo entiende el mundo", "Esa es su definición."),
        ex("¿Valle Ejemplo es un pueblo real o ficticio?", "ficticio", "La ficha lo dice."),
        ex("¿Debo inventar detalles de una historia que no me contaron? Sí o No.", "No", "Se consulta a quien la cuenta."),
    ],
    task=T(
        "Lee este relato inventado: «En Isla Ejemplo (lugar ficticio), cuando comienzan las lluvias, las personas bajan a la playa y cantan en grupo. Dicen que el viento lleva mensajes entre las islas. Los niños sueltan hojas secas al viento. Al final, una persona mayor cuenta un cuento breve sobre el primer viaje entre dos islas.» En tu cuaderno completa una ficha con estas líneas: pueblo o cultura (ficticio), quien cuenta (una profesora que lo escribió), evento, permiso y lenguajes artísticos. Agrega una oración que diga qué idea del mundo aparece en el relato, sin decir que otros pueblos piensan igual.",
        "Pueblo: Isla Ejemplo (ficticio). Quien cuenta: una profesora. Evento: la llegada de las lluvias. Permiso: sí, es inventado. Lenguajes artísticos: canto, cuento oral. Idea: en este relato el viento lleva mensajes entre las islas.",
        ["completa las cinco líneas", "nombra al menos dos lenguajes artísticos", "dice una idea del mundo del relato", "no generaliza a otros pueblos"],
        ["ficha completa", "una oración sobre la idea"],
        ["generalizar a todos los pueblos", "inventar detalles"],
        "Si generaliza, pídele que agregue «en el relato de Isla Ejemplo» al comienzo de su oración.",
    ),
    reinforce="Relee el relato de Valle Ejemplo y subraya con un color el evento y con otro los lenguajes artísticos.",
    extend="Inventa una ficha para un relato ficticio breve de tu invención, con las cinco líneas, y márcala como inventada.",
)

# ============================================================ LS01 clase 2 · leer con límites y disfrutar
R2 = "Relato 2 (inventado para practicar): En Aldea Muestra, un pueblo ficticio, el invierno comienza con una reunión en la casa común. Las personas se reúnen alrededor de una lámpara que cuidan los mayores. Una niña canta una melodía sin palabras. Nadie explica el significado de la melodía a quienes no son de la aldea, porque el pueblo pide guardarlo."

L(
    LS1, 2,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado para practicar. Puede leerlo una persona adulta.",
    use="Aprenderé a leer una historia sobre un evento de otro pueblo, a decir qué me gustó y a respetar los límites que el propio relato declara, como lo que el pueblo prefiere guardar. Sirve para disfrutar y comprender sin invadir lo que no me corresponde saber.",
    prior=["Sé situar un relato: pueblo, quien cuenta, evento y permiso.", "Sé que la cosmovisión es la forma en que un pueblo entiende el mundo."],
    explain=[
        "Al leer o escuchar una historia ajena hago tres cosas. Primero identifico qué cuenta: personas, lugar y acciones. Segundo, expreso lo que sentí o lo que me gustó, sin que eso signifique que la entiendo del todo. Tercero, busco los límites: lo que el relato no cuenta o pide guardar.",
        "En el relato 2, el pueblo pide guardar el significado de la melodía. Ese es un límite declarado: lo que se guarda no se explica a quien no es del pueblo. Yo respeto el límite y no invento un significado. Puedo decir qué observo («una niña canta una melodía sin palabras») y qué me hizo sentir, pero no por qué la cantan ni qué quiere decir.",
        "Disfrutar y comprender no es lo mismo que saber todo. Hay conocimientos que una comunidad comparte y otros que protege. Lo que no sé lo anoto como pregunta para el educador o la educadora tradicional, o simplemente lo dejo sin respuesta. Y cuando comento el relato, separo tres cosas: lo que dice el texto, lo que yo siento y lo que me queda por preguntar.",
    ],
    vocab=[("límite", "aviso de lo que no se cuenta o se guarda"), ("melodía", "sucesión de sonidos musicales"), ("casa común", "lugar donde la aldea se reúne"), ("significado", "lo que quiere decir algo"), ("guardar", "mantener algo reservado")],
    worked=[
        W("Decir qué cuenta el relato", R2 + " ¿Qué ocurre cuando comienza el invierno en Aldea Muestra?", ["Busco el comienzo del relato.", "Las personas se reúnen en la casa común.", "Los mayores cuidan una lámpara y una niña canta."], "las personas se reúnen en la casa común, cuidan una lámpara y una niña canta una melodía sin palabras"),
        W("Respetar el límite", R2 + " Un compañero pregunta qué significa la melodía. ¿Qué debe responderse?", ["El relato dice que el pueblo guarda su significado.", "No se explica a quienes no son de la aldea.", "Entonces se responde que no se puede explicar."], "que el pueblo guarda el significado y no se explica"),
    ],
    mistakes=[
        M("Escribir «la melodía significa que llegó el frío» porque suena lógico.", "El relato dice que el significado se guarda; yo no lo sé.", "Escribo lo que observo y anoto que el significado no se cuenta."),
        M("Creer que si no entiendo todo, la historia no vale.", "Se puede disfrutar y comprender una parte sin saberlo todo.", "Digo qué me gustó y qué me quedó por preguntar."),
    ],
    R=[
        ex(R2 + " ¿Dónde se reúnen las personas cuando comienza el invierno?", "en la casa común", "El relato lo dice."),
        ex(R2 + " ¿Alrededor de qué se reúnen las personas?", "de una lámpara", "El relato lo dice."),
        ex(R2 + " ¿Quién canta la melodía?", "una niña", "El relato lo dice."),
    ],
    C=[
        ex(R2 + " ¿Quiénes cuidan la lámpara?", "los mayores", "El relato lo dice."),
        ex(R2 + " ¿Qué pide guardar el pueblo?", "el significado de la melodía", "Es el límite del relato."),
        ex(R2 + " Verdadero o falso: el relato explica el significado de la melodía.", "Falso", "Dice que no se explica."),
    ],
    A=[
        ex(R2 + " Clasifica cada frase como T (dice el texto), S (siento yo) o P (me queda por preguntar). 1) Una niña canta una melodía sin palabras. 2) Me dio calma imaginar la lámpara encendida. 3) No sé por qué cantan esa melodía. Escribe las tres letras.", "1 T, 2 S, 3 P", "La primera frase está en el texto, la segunda es una emoción y la tercera es una duda."),
        arith("Una reunión de la aldea tiene 5 personas mayores y 9 niñas y niños. ¿Cuántas personas hay, sin contar a otras?", "5+9", "Se suman los dos grupos."),
        ex(R2 + " Ordena lo que haces al leer. A) anoto lo que me queda por preguntar. B) anoto lo que cuenta el texto. C) anoto lo que sentí. Escribe las letras en orden.", "B, C, A", "Primero el texto, luego lo que sentí y al final las dudas."),
    ],
    Z=[
        ex(R2 + " Un estudiante dice que la melodía es una oración para pedir calor. ¿Puede afirmarlo? Sí o No.", "No", "El significado está guardado; afirmarlo sería inventar."),
        ex(R2 + " ¿Qué conviene más ante la duda sobre un detalle del relato: adivinar o anotarla para preguntarla a quien cuenta?", "anotarla para preguntarla a quien cuenta", "Adivinar puede cambiar el sentido."),
    ],
    D=[
        ex(R2 + " Elige la mejor opinión. A) «Me gustó que los mayores cuiden la lámpara; no sé el significado de la melodía y el relato dice que no se cuenta». B) «Seguro la melodía significa algo triste». Escribe la letra.", "A", "La A dice lo que sintió y respeta el límite."),
        ex("Alguien te cuenta un relato de su comunidad y te pide que no expliques una parte a otras personas. ¿Qué hacer al contarlo después: dejar esa parte fuera o inventar una explicación?", "dejar esa parte fuera", "Se respeta lo que la comunidad guarda."),
    ],
    context=[ex("En una visita, una persona de la comunidad muestra un objeto y te dice que su historia no se cuenta fuera de ahí. Al escribir tu informe, ¿cuentas la historia que imaginas o dices que existe un objeto cuya historia se guarda?", "dices que existe un objeto cuya historia se guarda", "Respetas el límite sin inventar.")],
    selfcheck=[
        ex("¿Qué hago con lo que el pueblo guarda: lo explico o lo respeto?", "lo respeto", "Es un límite declarado."),
        ex("Si no entiendo todo un relato, ¿puedo igual decir qué me gustó? Sí o No.", "Sí", "Se puede disfrutar y comprender una parte."),
        ex("¿Una duda se anota o se inventa su respuesta?", "se anota", "Se pregunta a quien cuenta."),
    ],
    task=T(
        "Lee este relato inventado: «En Bosque Muestra, un pueblo ficticio, cuando nace una niña o un niño, las personas plantan un árbol pequeño. Una persona mayor lo riega con un cuenco de barro. Las personas cantan una canción corta. El pueblo no cuenta a visitantes lo que significa el cuenco.» En tu cuaderno escribe tres frases: una que diga qué cuenta el relato, una que diga qué te gustó y una que diga qué te queda por preguntar, sin explicar el significado del cuenco.",
        "Cuenta: cuando nace alguien, las personas plantan un árbol y cantan una canción corta. Me gustó: que cada niña o niño tenga un árbol. Por preguntar: ¿cómo se cuida el árbol? No explico el cuenco porque el pueblo no lo cuenta.",
        ["dice qué cuenta el relato", "dice qué le gustó", "anota una pregunta", "no explica el significado del cuenco"],
        ["tres frases escritas"],
        ["inventar el significado del cuenco", "mezclar lo que siente con lo que cuenta el texto"],
        "Si inventó el significado, pídele que lea la última oración del relato y diga qué límite declara.",
    ),
    reinforce="Relee el relato 2 y subraya con una línea lo que dice el texto y con una onda lo que el pueblo guarda.",
    extend="Escribe un relato ficticio de tres oraciones en el que algo se guarde, y explica cómo lo respetaría un lector.",
)

# ============================================================ LS01 clase 3 · relacionar el evento con la cosmovisión y con mi experiencia
R3 = "Relato 3 (inventado para practicar): En Costa Ejemplo, un pueblo ficticio, el día en que las barcas vuelven por primera vez después del temporal, toda la gente va al muelle. Cada familia lleva un trozo de pan y lo comparte con quienes no tienen barca. Un hombre toca un tambor sencillo mientras las barcas llegan. Las personas dicen que el mar presta lo que da y que por eso hay que devolver con cuidado."

L(
    LS1, 3,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado para practicar.",
    use="Aprenderé a relacionar el evento de un relato con la cosmovisión del pueblo que lo cuenta y con mi propia experiencia, y a reconocer los lenguajes artísticos que usa. Sirve para comprender qué valora una cultura sin pensar que es igual a la mía.",
    prior=["Sé situar un relato y respetar sus límites.", "Sé que la cosmovisión es la forma en que un pueblo entiende el mundo."],
    explain=[
        "Un evento se comprende mejor cuando lo relaciono con lo que el pueblo piensa del mundo, es decir, con su cosmovisión. En el relato de Costa Ejemplo la gente dice que el mar presta lo que da y que hay que devolver con cuidado. De esa idea se entiende por qué comparten el pan con quienes no tienen barca: devolver también es compartir.",
        "Los lenguajes artísticos ayudan a expresar esa cosmovisión. Aquí aparecen el tambor que acompaña la llegada de las barcas, el relato oral que repite la idea del mar y el gesto de compartir el pan como una especie de rito cotidiano. Cada pueblo tiene sus propios lenguajes artísticos, y los aprende de sus mayores y educadores.",
        "También relaciono el relato con mi experiencia. En mi casa o en mi curso hay momentos de compartir, de agradecer o de esperar a alguien. Puedo decir qué se parece y qué cambia, sin pensar que la otra cultura es igual que la mía ni mejor ni peor. Una buena comparación nombra el relato, lo que se parece y lo que cambia.",
    ],
    vocab=[("valor", "algo que una cultura considera importante"), ("compartir", "dar parte de lo que se tiene a otras personas"), ("devolver", "dar de vuelta lo recibido"), ("tambor", "instrumento de percusión que se golpea"), ("rito cotidiano", "gesto que se repite en la vida diaria con un sentido")],
    worked=[
        W("Relacionar con la cosmovisión", R3 + " ¿Qué idea del mar explica por qué comparten el pan?", ["Busco lo que la gente dice del mar.", "Dicen que el mar presta lo que da y que hay que devolver con cuidado.", "Por eso comparten con quienes no tienen barca."], "la idea de que el mar presta lo que da y hay que devolver con cuidado"),
        W("Relacionar con mi experiencia", R3 + " Escribe una semejanza con compartir en un curso.", ["En el relato se comparte pan con quienes no tienen.", "En un curso se puede compartir una colación con alguien que no trajo.", "Las dos son formas de cuidar a otras personas."], "ambos casos comparten algo con quien no lo tiene"),
    ],
    mistakes=[
        M("Escribir «en Costa Ejemplo comparten pan porque no tienen otra cosa».", "El relato explica otra razón: devolver con cuidado.", "Uso la razón que da el relato."),
        M("Decir «esa cultura es igual a la mía».", "Hay semejanzas y diferencias; no son iguales.", "Digo qué se parece y qué cambia."),
    ],
    R=[
        ex(R3 + " ¿Adónde va toda la gente el día en que vuelven las barcas?", "al muelle", "El relato lo dice."),
        ex(R3 + " ¿Qué lleva cada familia?", "un trozo de pan", "El relato lo dice."),
        ex(R3 + " ¿Qué instrumento toca un hombre?", "un tambor sencillo", "El relato lo dice."),
    ],
    C=[
        ex(R3 + " ¿Con quiénes comparten el pan las familias?", "con quienes no tienen barca", "El relato lo dice."),
        ex(R3 + " ¿Qué dicen las personas del mar?", "que presta lo que da", "Es la idea central de su cosmovisión."),
        ex(R3 + " Verdadero o falso: para esta gente, devolver con cuidado es parte de su forma de entender el mar.", "Verdadero", "El relato lo dice con esas palabras."),
    ],
    A=[
        ex(R3 + " Une cada elemento con lo que expresa. 1) el pan compartido. 2) el tambor. 3) la frase sobre el mar. Opciones: A) la llegada de las barcas con música. B) devolver con cuidado. C) una idea del mundo. Escribe los tres pares.", "1-B, 2-A, 3-C", "El pan expresa devolver con cuidado, el tambor acompaña la llegada y la frase expresa una idea del mundo."),
        arith(R3 + " Si llegan 18 familias con un trozo de pan cada una y se suman 7 familias más con un trozo cada una, ¿cuántos trozos de pan hay para compartir?", "18+7", "Se suman las familias, porque cada una lleva un trozo."),
        ex("Clasifica cada frase como S (semejanza con mi experiencia) o D (diferencia) respecto de compartir una colación en clase. 1) En ambos casos se comparte con quien no tiene. 2) En el muelle la razón es devolver lo que presta el mar; en clase la razón es ayudar a un compañero. Escribe las dos letras.", "1 S, 2 D", "La primera señala lo que se parece y la segunda lo que cambia."),
    ],
    Z=[
        ex(R3 + " Un estudiante dice: «En Costa Ejemplo comparten el pan porque son muy pobres». ¿Lo dice el relato? Sí o No.", "No", "El relato da una razón distinta: devolver con cuidado."),
        ex(R3 + " ¿Cuál es el valor que más se ve en el relato: el compartir o la velocidad de las barcas?", "el compartir", "Las familias comparten el pan y la idea de devolver."),
    ],
    D=[
        ex(R3 + " Elige la mejor frase de comparación. A) «En el relato de Costa Ejemplo se comparte para devolver al mar; en mi curso se comparte para ayudar a un compañero; en ambos casos se cuida a otras personas». B) «Esa gente comparte porque no sabe hacer otra cosa». Escribe la letra.", "A", "Dice semejanza y diferencia sin juzgar."),
        ex("Una compañera dice: «El valor de compartir es de todos los pueblos del mundo, entonces el relato de Costa Ejemplo es igual al de todos». ¿Es correcto? Sí o No.", "No", "Aunque haya valores parecidos, cada relato tiene su propia forma."),
    ],
    context=[ex("Imagina que en una casa se guarda siempre un plato de comida para quien llegue tarde. ¿Esto se parece al pan compartido de Costa Ejemplo o es exactamente lo mismo?", "se parece, pero no es exactamente lo mismo", "Hay semejanza en el cuidado y diferencia en la razón y el modo.")],
    selfcheck=[
        ex("En Lengua y Cultura de los Pueblos Originarios: ¿qué es una cosmovisión?", "la forma en que un pueblo entiende el mundo", "Así se definió en la clase."),
        ex("Al comparar con mi experiencia, ¿digo que son iguales o qué se parece y qué cambia?", "qué se parece y qué cambia", "Comparar es observar semejanzas y diferencias."),
        ex("¿El tambor del relato es un lenguaje artístico? Sí o No.", "Sí", "La música es un lenguaje artístico."),
    ],
    task=T(
        "Lee este relato inventado: «En Montaña Ejemplo, un pueblo ficticio, al comienzo del invierno las personas suben al mirador y dejan allí piedras pequeñas en fila. Dicen que cada piedra recuerda a quien cuida el camino. Un joven toca una flauta simple mientras las personas descienden en silencio.» En tu cuaderno escribe tres cosas: la idea del mundo que aparece, una semejanza con algo que ocurra en tu casa o curso, y una diferencia. No digas que los dos son iguales.",
        "Idea del mundo: en este relato se recuerda y se agradece a quienes cuidan el camino. Semejanza: en mi curso también agradecemos a quien nos ayuda. Diferencia: allí se hace con piedras en fila y flauta; en mi curso se hace con una tarjeta.",
        ["nombra la idea del mundo", "escribe una semejanza", "escribe una diferencia", "no dice que sean iguales"],
        ["tres frases escritas"],
        ["decir que son iguales", "inventar el significado de las piedras"],
        "Si dice que son iguales, pídele que complete «pero cambia que…».",
    ),
    reinforce="Relee el relato 3 y subraya la frase que expresa la idea del mar.",
    extend="Escribe cómo celebras o agradeces algo en tu casa y compáralo con el relato de Costa Ejemplo sin decir cuál es mejor.",
)

# ============================================================ LS01 clase 4 · opinión atribuida
OP = "Opinión modelo (inventada para practicar): «Según el relato 1 de Valle Ejemplo, las personas agradecen a la tierra al terminar la cosecha. Yo pienso que es una forma bonita de cuidar lo que se recibe, porque el relato dice que se comparte una comida y se cuelgan cintas. Eso me hace pensar en cómo agradecemos en mi curso. Mi opinión es solo mía y no habla por ese pueblo.»"

L(
    LS1, 4,
    materials="Lápiz y hoja. La opinión modelo está escrita aquí y es inventada para practicar.",
    use="Aprenderé a expresar una opinión sobre una historia de otra cultura que se apoya en lo que dice el relato, la separa de lo que pienso yo y reconoce un límite. Sirve para dar opiniones respetuosas y fundamentadas.",
    prior=["Sé relacionar un evento con su cosmovisión.", "Sé que «según» atribuye lo dicho a su fuente y «yo pienso» marca lo mío."],
    explain=[
        "Una opinión respetuosa tiene cuatro partes. Primero cita lo que dice el relato con «según». Segundo, dice lo que yo pienso con «yo pienso». Tercero, da una razón que se apoya en el relato, con «porque». Cuarto, declara el límite: mi opinión es mía y no habla por el pueblo del relato.",
        "Una opinión no es un juicio sobre las personas. Puedo decir «me gustó que compartan una comida», pero no «esa gente es rara» ni «mi cultura es mejor». Si mi opinión necesita datos que el relato no entrega, digo que me gustaría preguntar más y no los invento. Una razón sólida usa lo que realmente aparece en el texto.",
        "También separo lo que el relato dice de lo que yo le agrego. Si escribo «el relato dice que las personas son felices», debo ver si el texto lo afirma. Si no lo dice, es mi interpretación y debo marcarla como tal. Cuando la opinión toca creencias o ceremonias reales, la comparto con el educador o la educadora tradicional antes de hacerla pública.",
    ],
    vocab=[("opinión", "lo que alguien piensa sobre algo"), ("razón", "motivo que apoya una opinión"), ("fundamentar", "apoyar una opinión en datos"), ("juicio", "afirmación que valora a alguien, a menudo sin pruebas"), ("interpretación", "lo que yo concluyo aunque el texto no lo dice")],
    worked=[
        W("Reconocer las partes", OP + " ¿Cuál es la razón que apoya la opinión?", ["Busco la palabra «porque».", "Dice que el relato cuenta que se comparte una comida y se cuelgan cintas.", "Esa es la razón."], "que el relato dice que se comparte una comida y se cuelgan cintas"),
        W("Separar relato y opinión", OP + " ¿«Yo pienso que es una forma bonita de cuidar lo que se recibe» es lo que dice el relato o lo que piensa quien opina?", ["Veo que empieza con «yo pienso».", "Esa marca indica que es opinión de quien escribe.", "No es una frase del relato."], "es lo que piensa quien opina"),
    ],
    mistakes=[
        M("Escribir «esa gente es rara porque agradece a la tierra».", "Es un juicio sobre personas, sin razón y sin respeto.", "Digo qué me llamó la atención y qué razón del relato apoya mi opinión."),
        M("Afirmar «el relato dice que todos son felices» sin que el texto lo diga.", "Es una interpretación mía.", "La marco con «yo pienso» o la saco."),
    ],
    R=[
        ex(OP + " ¿Qué palabra introduce lo que dice el relato en la opinión modelo?", "según", "La opinión empieza con «Según el relato 1»."),
        ex(OP + " ¿Qué palabra introduce lo que piensa quien opina?", "yo pienso", "Aparece en la segunda oración."),
        ex("Una razón, ¿es el motivo que apoya una opinión o un título para el texto?", "el motivo que apoya una opinión", "Así se definió en la clase."),
    ],
    C=[
        ex(OP + " ¿Qué declara la última oración de la opinión modelo?", "que su opinión es solo suya y no habla por ese pueblo", "Es el límite de la opinión."),
        ex(OP + " ¿Con qué situación de su vida relaciona el relato quien opina?", "cómo agradecen en su curso", "La opinión lo dice."),
        ex("Verdadero o falso: «esa gente es rara» es una opinión fundamentada en el relato.", "Falso", "Es un juicio sin razón apoyada en el texto."),
    ],
    A=[
        ex("Ordena las partes de una opinión respetuosa. A) razón con «porque». B) límite. C) lo que dice el relato con «según». D) lo que pienso con «yo pienso». Escribe las letras en orden.", "C, D, A, B", "Se cita el relato, se opina, se justifica y se cierra con el límite."),
        ex("Valle Ejemplo (relato inventado): las familias se reúnen en la plaza al terminar la cosecha, una abuela cuenta cómo llegó el primer río y cada familia teje una cinta. Elige la mejor razón para la opinión «me gustó que todas las familias participen». A) «porque cada familia teje una cinta». B) «porque la gente de allí es muy simpática». Escribe la letra.", "A", "La razón se apoya en un dato del relato; la B es un juicio."),
        arith("Una opinión debe tener 4 partes. Un compañero escribió 3 oraciones, cada una con una parte distinta. ¿Cuántas partes le faltan?", "4-3", "Se restan las escritas de las cuatro pedidas."),
    ],
    Z=[
        ex(OP + " Un niño propone agregar «y por eso ese pueblo es mejor que otros». ¿Respeta la opinión modelo? Sí o No.", "No", "Jerarquiza pueblos y no se apoya en el relato."),
        ex(R1 + " " + OP + " ¿La opinión modelo usa un dato que no está en el relato 1? Sí o No.", "No", "Menciona la comida compartida y las cintas, que están en el relato."),
    ],
    D=[
        ex("Dos opiniones sobre el relato de Costa Ejemplo, donde se comparte pan al volver las barcas. Mario: «Yo pienso que es valioso compartir, porque el relato dice que se da pan a quienes no tienen barca». Lía: «Esa gente comparte porque es muy pobre». ¿Quién fundamentó mejor su opinión?", "Mario", "Se apoya en un dato del relato."),
        ex("Quieres publicar tu opinión sobre una ceremonia real que viste en una visita. ¿La publicas de inmediato o antes la muestras al educador o la educadora tradicional?", "antes la muestras al educador o la educadora tradicional", "Una opinión sobre prácticas reales se revisa con quien las conoce."),
    ],
    context=[ex("Tu curso vio la presentación de una comunidad sobre su fiesta. Te piden una opinión escrita. ¿Escribes qué te gustó y por qué, citando algo que viste, o solo «estuvo fome»?", "escribes qué te gustó y por qué, citando algo que viste", "Una opinión respetuosa tiene razones.")],
    selfcheck=[
        ex("¿Qué palabra marca una razón: «porque» o «según»?", "porque", "«Porque» introduce la razón."),
        ex("Una opinión, ¿habla por todo un pueblo o solo por quien la escribe?", "solo por quien la escribe", "Esa es la idea del límite."),
        ex("¿Puedo inventar datos que el relato no dice? Sí o No.", "No", "Debo apoyarme en el texto."),
    ],
    task=T(
        "Lee este relato inventado: «En Cumbre Ejemplo, un pueblo ficticio, cuando termina el invierno las personas salen a la ladera con cuerdas de colores y las atan a un palo largo. Dicen que así saludan a la primavera. Un grupo de niños baila en círculo mientras suena una flauta.» En tu cuaderno escribe una opinión de cuatro oraciones con estas partes: lo que dice el relato (con «según»), lo que piensas (con «yo pienso»), una razón (con «porque») apoyada en el relato y el límite de tu opinión. No juzgues a las personas.",
        "Según el relato de Cumbre Ejemplo, las personas saludan a la primavera atando cuerdas de colores a un palo largo. Yo pienso que es una forma alegre de recibir una estación nueva, porque el relato dice que los niños bailan en círculo con una flauta. Esto me recuerda cómo recibimos el verano en mi curso. Mi opinión es solo mía y no habla por ese pueblo.",
        ["usa «según» para citar el relato", "usa «yo pienso» para lo propio", "da una razón apoyada en el relato", "declara el límite y no juzga"],
        ["opinión de cuatro oraciones"],
        ["juzgar a las personas", "no dar una razón"],
        "Si no hay razón, pídele que busque en el relato la frase que apoye su opinión y la copie después de «porque».",
    ),
    reinforce="Copia la opinión modelo y subraya con distintos colores el «según», el «yo pienso», el «porque» y el límite.",
    extend="Escribe otra opinión sobre el relato de Costa Ejemplo con las cuatro partes.",
)

# ============================================================ LS01 clase 5 · contrastar dos cosmovisiones sin jerarquizar
VAL = "Resumen del relato de Valle Ejemplo (inventado): la tierra es como una persona mayor a la que se agradece al terminar la cosecha; se comparte una comida y cada familia teje una cinta."
COS = "Resumen del relato de Costa Ejemplo (inventado): el mar presta lo que da y hay que devolver con cuidado; las familias comparten pan con quienes no tienen barca y suena un tambor."

L(
    LS1, 5,
    materials="Lápiz y hoja. Los dos resúmenes están escritos aquí y son inventados para practicar.",
    use="Aprenderé a comparar dos cosmovisiones distintas usando los mismos criterios y a decir qué se parece y qué cambia sin afirmar que una sea más verdadera, más importante o más avanzada. Sirve para valorar la diversidad de maneras de entender el mundo.",
    prior=["Sé relacionar un evento con su cosmovisión.", "Sé dar una opinión respetuosa y fundamentada."],
    explain=[
        "Comparar cosmovisiones es mirar dos formas de entender el mundo con los mismos criterios. Puedo usar: qué elemento de la naturaleza aparece, qué valor se expresa, qué lenguajes artísticos usa y qué se hace en el evento. Respondo cada criterio para cada relato y luego escribo semejanzas y diferencias.",
        "Jerarquizar es decir que una forma de entender el mundo vale más que otra. En un trabajo de Lengua y Cultura de los Pueblos Originarios no se jerarquiza: una cosmovisión no es «más verdadera» ni «más avanzada» que otra. Sí puedo decir que son distintas y explicar en qué, con datos del relato.",
        "Una comparación respetuosa también evita dos errores. Uno es mezclar los relatos como si fueran un solo pueblo. El otro es suponer que lo que dice un relato vale para todo un pueblo real. Por eso nombro cada relato por su nombre y cierro con una frase que diga una semejanza, una diferencia y mi propia opinión, marcada como mía.",
    ],
    vocab=[("comparar", "mirar dos cosas con los mismos criterios"), ("jerarquizar", "decir que algo vale más que otra cosa"), ("semejanza", "algo en que dos cosas se parecen"), ("diferencia", "algo en que dos cosas cambian"), ("criterio", "aspecto que se usa para comparar")],
    worked=[
        W("Comparar con un criterio", VAL + " " + COS + " Compara el elemento de la naturaleza que aparece en cada relato.", ["En Valle Ejemplo aparece la tierra.", "En Costa Ejemplo aparece el mar.", "Son elementos distintos."], "en uno aparece la tierra y en el otro el mar"),
        W("Reconocer una jerarquización", "Una persona dice: «La cosmovisión de Costa Ejemplo es más avanzada que la de Valle Ejemplo». ¿Compara o jerarquiza?", ["La frase dice que una es más avanzada.", "Poner una cosmovisión sobre otra es jerarquizar.", "No usa un criterio observable."], "jerarquiza"),
    ],
    mistakes=[
        M("Escribir «la cosmovisión del mar es más verdadera que la de la tierra».", "Ninguna cosmovisión vale más que otra.", "Digo en qué se parecen y en qué cambian."),
        M("Mezclar los dos relatos y escribir «ese pueblo agradece a la tierra y al mar».", "Son dos relatos de dos pueblos ficticios distintos.", "Nombro cada relato con su nombre."),
    ],
    R=[
        ex(VAL + " ¿Qué elemento de la naturaleza aparece en el relato de Valle Ejemplo?", "la tierra", "El resumen lo dice."),
        ex(COS + " ¿Qué elemento de la naturaleza aparece en el relato de Costa Ejemplo?", "el mar", "El resumen lo dice."),
        ex("Jerarquizar, ¿es decir que algo vale más que otra cosa o comparar con los mismos criterios?", "decir que algo vale más que otra cosa", "Esa es la definición de la clase."),
    ],
    C=[
        ex(VAL + " " + COS + " ¿Qué se comparte en el relato de Costa Ejemplo?", "pan con quienes no tienen barca", "El resumen lo dice."),
        ex(VAL + " " + COS + " ¿Qué teje cada familia en el relato de Valle Ejemplo?", "una cinta", "El resumen lo dice."),
        ex("Verdadero o falso: es correcto decir que una cosmovisión es más verdadera que otra.", "Falso", "No se jerarquizan cosmovisiones."),
    ],
    A=[
        ex(VAL + " " + COS + " Completa con V o C: se agradece a la tierra en el relato ___; se devuelve con cuidado lo que presta el mar en el relato ___. Escribe las dos letras en orden.", "V, C", "El primero es Valle Ejemplo y el segundo Costa Ejemplo."),
        arith(VAL + " " + COS + " En una clase, 12 estudiantes eligieron comparar el criterio «elemento de la naturaleza» y 9 el criterio «valor». ¿Cuántos estudiantes compararon en total?", "12+9", "Se suman los dos grupos."),
        ex("Clasifica cada frase como C (compara) o J (jerarquiza). 1) «En un relato se agradece a la tierra y en el otro se devuelve al mar». 2) «La cosmovisión del mar es más importante». 3) «Los dos relatos expresan cuidado hacia lo que se recibe». Escribe las tres letras.", "1 C, 2 J, 3 C", "Solo la frase 2 pone una cosmovisión sobre otra."),
    ],
    Z=[
        ex(VAL + " " + COS + " Una compañera dice que ambos relatos expresan cuidado hacia lo que se recibe. ¿Está nombrando una semejanza o una diferencia?", "una semejanza", "Dice qué comparten los dos relatos."),
        ex(VAL + " " + COS + " Otro dice: «Valle Ejemplo y Costa Ejemplo son el mismo pueblo». ¿Es correcto? Sí o No.", "No", "Son dos relatos de dos pueblos ficticios distintos."),
    ],
    D=[
        ex(VAL + " " + COS + " Elige la mejor frase de cierre. A) «Los dos relatos expresan cuidado hacia lo que se recibe; uno agradece a la tierra y el otro devuelve al mar; yo pienso que ambos muestran formas respetuosas de vivir». B) «El relato de Valle Ejemplo es mejor». Escribe la letra.", "A", "Dice semejanza, diferencia y marca la opinión propia."),
        ex("Quieres comparar el relato de Valle Ejemplo con la fiesta real de una comunidad que visitaste, pero no tienes permiso para contar esa fiesta. ¿Qué haces: la comparas igual o comparas con otra situación que sí puedas contar?", "comparas con otra situación que sí puedas contar", "Sin permiso no se cuenta una fiesta real."),
    ],
    context=[ex("Dos compañeros discuten cuál cosmovisión es mejor, la de Valle Ejemplo o la de Costa Ejemplo. ¿Qué les dirías: que ninguna es mejor y que pueden explicar en qué se parecen y en qué cambian, o que voten?", "que ninguna es mejor y que pueden explicar en qué se parecen y en qué cambian", "Comparar no es votar entre pueblos.")],
    selfcheck=[
        ex("¿Una cosmovisión es más verdadera que otra? Sí o No.", "No", "No se jerarquizan cosmovisiones."),
        ex("¿Qué se hace con cada criterio: se responde solo para un relato o para los dos?", "para los dos", "Así la comparación es justa."),
        ex("¿Qué palabra jerarquiza: «distinto» o «más avanzado»?", "más avanzado", "Pone una cosa sobre otra."),
    ],
    task=T(
        "Usa estos dos resúmenes inventados. Relato A: «En Montaña Ejemplo, al comenzar el invierno, las personas dejan piedras en fila para recordar a quien cuida el camino; suena una flauta». Relato B: «En Bahía Ejemplo, al comenzar la primavera, las personas liberan hojas al viento porque creen que lleva mensajes; se canta en grupo». En tu cuaderno haz una tabla con estas filas: elemento de la naturaleza, valor que expresa, lenguaje artístico y qué se hace. Luego escribe una frase de cierre con una semejanza, una diferencia y tu opinión marcada con «yo pienso», sin jerarquizar.",
        "Elemento: piedras y camino / viento. Valor: recordar a quien cuida / comunicar mensajes. Lenguaje artístico: flauta / canto en grupo. Qué se hace: dejar piedras en fila / liberar hojas al viento. Cierre: «Los dos relatos marcan el comienzo de una estación con un gesto sencillo; uno recuerda a quien cuida el camino y el otro manda mensajes al viento. Yo pienso que ambos muestran cuidado por la comunidad.»",
        ["completa las cuatro filas para ambos relatos", "usa los mismos criterios", "escribe semejanza, diferencia y opinión marcada", "no jerarquiza"],
        ["tabla de comparación", "frase de cierre"],
        ["decir que una cosmovisión es mejor", "dejar una fila sin completar"],
        "Si jerarquiza, pídele que reemplace la palabra por un dato de la tabla.",
    ),
    reinforce="Copia los resúmenes de Valle Ejemplo y Costa Ejemplo y subraya con distinto color el elemento de la naturaleza de cada uno.",
    extend="Compara con la misma tabla uno de los relatos de la clase con un recuerdo familiar tuyo, sin jerarquizar.",
)

# ============================================================ LS01 clase 6 · comunicar con un lenguaje artístico, con validación
PL = "Plan de presentación (inventado para practicar): un grupo quiere comunicar el relato de Costa Ejemplo con un lenguaje artístico. Opciones: 1) un dibujo propio de las barcas llegando al muelle. 2) un tambor hecho con una caja de cartón, golpeado con las manos, para acompañar la lectura. 3) copiar un símbolo que vieron en una fiesta real y pintarlo en un cartel. 4) una pequeña obra de teatro con títeres de papel. El educador tradicional de la escuela aún no ha leído el plan."

L(
    LS1, 6,
    materials="Lápiz y hoja. El plan de presentación está escrito aquí y es inventado para practicar. Para la tarea abierta basta papel y lápices; una caja de cartón es opcional.",
    use="Aprenderé a elegir un lenguaje artístico para comunicar una historia de otro pueblo sin copiar símbolos que no me corresponden, a pedir validación al educador o a la educadora tradicional y a presentar con respeto. Sirve para expresar lo que comprendí sin apropiarme de lo ajeno.",
    prior=["Sé reconocer lenguajes artísticos en un relato.", "Sé dar una opinión respetuosa y fundamentada."],
    explain=[
        "Los lenguajes artísticos, como el dibujo, la música, el teatro y el tejido, sirven para comunicar lo que comprendí de una historia. Puedo usar lenguajes artísticos generales, que cualquiera puede practicar, como un dibujo propio o una lectura con un ritmo de palmas. Cada pueblo tiene además sus propios lenguajes artísticos, que enseñan sus mayores y educadores.",
        "Apropiarse es tomar un símbolo, un canto, un diseño o una danza de un pueblo y usarlo como propio sin permiso. No debo copiar símbolos ni diseños de fiestas reales, ni disfrazarme de un pueblo. En cambio, puedo hacer una obra propia inspirada en un relato, diciendo claramente que es mi interpretación y nombrando el relato que me inspiró.",
        "Validar es mostrar mi trabajo antes de presentarlo a una persona que conoce la cultura, como el educador o la educadora tradicional, y preguntarle si respeta lo que enseñó. Al presentar digo: qué relato me inspiró, que mi obra es mi interpretación y qué límites respeté. Si la persona pide cambiar algo, lo cambio.",
    ],
    vocab=[("validar", "mostrar un trabajo a quien conoce el tema para confirmar que lo respeta"), ("apropiación", "usar como propio algo que es de otro pueblo sin permiso"), ("interpretación propia", "obra hecha por mí a partir de un relato"), ("inspirar", "dar la idea para crear algo"), ("símbolo", "dibujo o signo con un significado")],
    worked=[
        W("Elegir lenguajes sin apropiación", PL + " ¿Cuáles opciones son interpretaciones propias que no copian símbolos ajenos?", ["La opción 1 es un dibujo propio.", "Las opciones 2 y 4 son obras propias: un tambor de cartón y un teatro de títeres.", "La opción 3 copia un símbolo de una fiesta real y no sirve."], "las opciones 1, 2 y 4"),
        W("Anunciar la presentación", "Un grupo presenta su dibujo del puerto. ¿Qué debe decir al comienzo?", ["Debe nombrar el relato que lo inspiró.", "Debe aclarar que el dibujo es su interpretación.", "Debe decir qué límite respetó, como no copiar símbolos de fiestas reales."], "el relato que lo inspiró, que es su interpretación y el límite que respetó"),
    ],
    mistakes=[
        M("Pintar un símbolo visto en una fiesta real y decir que es del grupo.", "Es apropiarse de algo que pertenece a otro pueblo.", "Hago un dibujo propio o consulto si se puede usar."),
        M("Presentar sin mostrar antes el trabajo al educador tradicional.", "No sé si respeta lo que él o ella enseñó.", "Pido validación antes de presentar."),
    ],
    R=[
        ex(PL + " ¿Qué opción es un dibujo propio de las barcas llegando al muelle?", "la opción 1", "La opción 1 lo dice."),
        ex(PL + " ¿Con qué se hace el tambor de la opción 2?", "con una caja de cartón", "La opción 2 lo dice."),
        ex("Validar, ¿es mostrar un trabajo a quien conoce el tema para confirmar que lo respeta o presentar sin avisar?", "mostrar un trabajo a quien conoce el tema para confirmar que lo respeta", "Así se definió en la clase."),
    ],
    C=[
        ex(PL + " ¿Qué opción copia un símbolo de una fiesta real?", "la opción 3", "La opción 3 lo dice."),
        ex(PL + " ¿Ha leído el plan el educador tradicional de la escuela?", "no", "El plan avisa que aún no lo ha leído."),
        ex("Verdadero o falso: copiar un símbolo de una fiesta real y decir que es de uno es apropiación.", "Verdadero", "Es usar como propio algo ajeno sin permiso."),
    ],
    A=[
        ex(PL + " Ordena los pasos para presentar. A) presentar y decir qué relato inspiró la obra. B) mostrar el trabajo al educador tradicional. C) cambiar lo que él o ella pida. D) hacer una obra propia. Escribe las letras en orden.", "D, B, C, A", "Se crea, se valida, se corrige y recién se presenta."),
        arith(PL + " El grupo hará 4 títeres de papel para la opción 4. Cada títere necesita 2 hojas. ¿Cuántas hojas necesitan?", "4*2", "Cuatro títeres por dos hojas cada uno."),
        ex(PL + " ¿Cuál de las opciones 1, 2 o 3 copia un símbolo de una fiesta real y por eso no sirve? Escribe el número.", "3", "La 1 y la 2 son obras propias; la 3 copia un símbolo real."),
    ],
    Z=[
        ex(PL + " Un compañero dice que la opción 3 es válida porque el símbolo se ve bonito. ¿Es una razón suficiente? Sí o No.", "No", "Lo que importa es el permiso y el respeto, no la belleza."),
        ex(PL + " Si el educador tradicional pide cambiar un detalle del dibujo, ¿qué se hace: se cambia o se presenta igual?", "se cambia", "Validar significa respetar lo que pide quien conoce."),
    ],
    D=[
        ex("Dos introducciones para una presentación. A) «Esta obra la hicimos nosotros, inspirados en el relato inventado de Costa Ejemplo; es nuestra interpretación». B) «Esta es la verdadera forma de celebrar de ese pueblo». ¿Cuál es respetuosa? Escribe la letra.", "A", "Reconoce la inspiración y no afirma hablar por un pueblo."),
        ex("Tu grupo quiere usar una canción real que oyeron en una ceremonia para acompañar su obra. ¿La usan sin consultar o primero consultan si se puede y si el pueblo lo autoriza?", "primero consultan si se puede y si el pueblo lo autoriza", "Un canto de una ceremonia no se usa sin permiso."),
    ],
    context=[ex("Tu curso hará una muestra sobre un relato de otra cultura. Alguien trae un disfraz «tradicional» comprado en una tienda. ¿Lo usan o hacen dibujos propios de lo que comprendieron?", "hacen dibujos propios de lo que comprendieron", "Un disfraz tipo estereotipo no respeta a las personas de ese pueblo.")],
    selfcheck=[
        ex("¿Se puede copiar un símbolo de una fiesta real? Sí o No.", "No", "Es apropiarse de algo ajeno."),
        ex("¿Antes de presentar se valida o se improvisa?", "se valida", "Se muestra el trabajo a quien conoce el tema."),
        ex("¿Qué se dice al presentar: que la obra es una interpretación propia o que es la forma verdadera del pueblo?", "que es una interpretación propia", "Nadie habla por todo un pueblo."),
    ],
    task=T(
        "Lee este plan inventado: «El curso quiere comunicar el relato de Cumbre Ejemplo (cuerdas de colores atadas a un palo largo para saludar a la primavera). Opciones: A) un dibujo propio de la ladera con las cuerdas. B) un cartel con un símbolo que vieron en una fiesta real. C) una lectura con palmas suaves. El educador tradicional no ha visto el plan.» En tu cuaderno haz tres cosas: marca la opción que no sirve y di por qué; elige una de las otras y descríbela en dos oraciones (qué haría el grupo); y escribe tres oraciones que dirías al presentar (relato que inspiró, interpretación propia, límite).",
        "No sirve la opción B porque copia un símbolo de una fiesta real. Elijo la opción A: el grupo dibujaría la ladera con cuerdas de colores. Al presentar: «Nos inspiró el relato de Cumbre Ejemplo. Este dibujo es nuestra interpretación. No copiamos símbolos de fiestas reales.»",
        ["marca la opción B con su razón", "describe una opción propia", "escribe tres oraciones de presentación", "menciona la validación"],
        ["marca y razón escritas", "descripción de dos oraciones", "tres oraciones de presentación"],
        ["elegir la opción B", "olvidar decir que es una interpretación propia"],
        "Si elige la B, pídele que relea la parte sobre apropiación y vuelva a decidir.",
    ),
    reinforce="Relee las cuatro opciones del plan y escribe al lado de cada una una S (sirve) o una N (no sirve).",
    extend="Diseña un plan de presentación para otro relato de la clase, con tres opciones propias y una justificación.",
)
