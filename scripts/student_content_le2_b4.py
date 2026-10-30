"""Cuaderno del estudiante, 2.º básico Lenguaje y Comunicación: OA 16 (planificar la escritura a partir de ideas)."""
from __future__ import annotations

from student_lessons import ex, register

OA16 = "LE02 OA 16"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


IMG = ("«Imagen: Una niña con botas amarillas salta en un charco. Llueve. Detrás hay una casa con una luz encendida en la ventana, "
       "un gato mira desde la puerta y un paraguas rojo está en el suelo.»")

reg(
    OA16, 1,
    "Este cuaderno, lápiz y la descripción de una imagen escrita en los ejercicios. Si quieres, usa también una foto o un dibujo de tu casa.",
    "Aprenderé a mirar una imagen más de una vez para sacar muchas ideas de ella. Sirve para tener qué escribir antes de empezar un texto.",
    ["Sé describir lo que veo en una imagen.", "Sé que planificar es pensar antes de escribir."],
    ["Planificar la escritura es pensar y juntar ideas antes de escribir el texto final. Una forma de generar ideas es observar una imagen. La primera mirada es rápida: ves lo más grande, como una niña, un charco y la lluvia.",
     "Con la segunda mirada, buscas detalles pequeños: el color de las botas, el gato en la puerta, la luz de la casa, el paraguas en el suelo. Con la tercera mirada, te preguntas qué pasó antes y qué pasará después, y qué estarán sintiendo los personajes.",
     "Cada cosa que notas es una idea posible. En esta etapa no escribes el texto final: solo anotas ideas, con palabras sueltas o dibujos. Después elegirás las mejores. Mientras más veces mires, más ideas encontrarás."],
    [("planificar", "pensar y organizar ideas antes de escribir"), ("observar", "mirar con atención"), ("detalle", "dato pequeño que se ve en una imagen"), ("idea", "pensamiento que puede servir para escribir"), ("borrador de ideas", "lista de ideas sueltas antes de escribir")],
    [("Primera mirada", IMG + " ¿Qué es lo más grande que se ve?", ["Miro la imagen completa.", "Veo una niña saltando en un charco.", "Anoto: niña, charco, lluvia."], "Una niña saltando en un charco"),
     ("Segunda mirada", "Con la misma imagen, ¿qué detalles pequeños encuentras?", ["Miro más despacio.", "Botas amarillas, gato en la puerta, luz en la ventana, paraguas rojo."], "Botas amarillas, gato, luz y paraguas")],
    [("Mirar la imagen una sola vez.", "Se pierden muchas ideas.", "Mira dos o tres veces, buscando detalles distintos."), ("Empezar a escribir el texto final de inmediato.", "Aún no tienes ideas.", "Primero anota ideas sueltas.")],
    ([E(IMG + " ¿De qué color son las botas?", "Amarillas", "La imagen dice botas amarillas."),
      E(IMG + " ¿Qué hace el gato?", "Mira desde la puerta", "Está en la puerta mirando."),
      E(IMG + " ¿De qué color es el paraguas?", "Rojo", "La imagen dice paraguas rojo.")],
     [E("¿Qué es planificar la escritura?", "Pensar y juntar ideas antes de escribir", "Es lo que se hace antes del texto final."),
      E("¿La primera mirada a una imagen busca detalles pequeños o lo más grande?", "Lo más grande", "Los detalles vienen en la segunda mirada."),
      E("¿Qué se hace en la tercera mirada: preguntar qué pasó antes o contar los pelos del gato?", "Preguntar qué pasó antes", "Se piensa en la historia detrás de la imagen.")],
     [E(IMG + " Escribe una pregunta sobre lo que pasó antes de la escena.", "¿Por qué la niña salió a saltar bajo la lluvia?", "Una pregunta sobre antes ayuda a imaginar."),
      E(IMG + " Anota tres palabras de la primera mirada.", "niña, charco, lluvia", "Son lo más grande de la imagen."),
      E(IMG + " ¿Qué podrías sentir la niña según la imagen? Escribe una emoción.", "Alegría", "Saltar en el charco sugiere diversión.")],
     [E("Beto miró la imagen una vez y dijo: «No hay nada más». Ana la miró tres veces y encontró el gato y el paraguas. ¿Quién tendrá más ideas para escribir?", "Ana", "Mirar varias veces revela más detalles."),
      E("Ema escribió un cuento completo sin anotar ideas. ¿Qué se saltó?", "La planificación", "Falta pensar antes de escribir.")],
     [E(IMG + " Escribe cinco ideas distintas que salgan de ella.", "Botas amarillas, charco, gato que mira, luz en la ventana, paraguas en el suelo", "Cada elemento es una idea posible."),
      E(IMG + " Imagina qué pasa después de la escena y escribe una idea.", "La niña entra a la casa y toma una sopa", "Una idea de después amplía la historia.")]),
    [E("Tu profesora muestra la imagen y pide ideas para un texto. " + IMG + " Escribe tres ideas, una de cada mirada.", "Niña en el charco; botas amarillas; la niña tiene frío después", "Cada idea viene de una mirada distinta.")],
    [E("¿Se puede mirar una imagen más de una vez?", "Sí", "Cada mirada muestra algo nuevo."),
     E("¿Planificar es escribir el texto final?", "No", "Es pensar antes de escribir."),
     E("¿Un detalle puede ser una idea?", "Sí", "Los detalles suman ideas.")],
    ("Observa un dibujo, una foto o este paisaje: «Un bote pequeño flota en un lago. Hay un pato nadando, una montaña al fondo y una persona que pesca sentada.» Haz tres miradas y anota: 1) lo más grande, 2) cuatro detalles, 3) una pregunta sobre antes o después.", "1) Bote en un lago. 2) Pato, montaña, persona que pesca, bote pequeño. 3) ¿Qué pescará la persona?", ["anota la primera mirada", "encuentra cuatro detalles", "hace una pregunta"], ["tres anotaciones de ideas"], ["mirar una vez", "escribir el texto final"], "Compara con otra persona: ¿qué detalles vio que tú no?"),
    "Mira una foto de tu casa dos veces y anota qué viste distinto.",
    "Mira una imagen por tres minutos y escribe diez ideas distintas.")

CONV = ("«Ana: Quiero escribir un cuento sobre la niña del charco para niños de primero. Pedro: Quizás el gato quiere salir a jugar con ella. "
        "Luisa: Mi abuela hace sopa cuando llueve. Mateo: Podría haber un dinosaurio en el charco.»")
EXP = ("«Sofía: Quiero escribir sobre un día de lluvia. Rodrigo: Una vez resbalé en un charco y me reí mucho. Profesora: ¿Qué hiciste después? "
       "Rodrigo: Mi mamá me dio ropa seca y tomamos chocolate caliente.»")
reg(
    OA16, 2,
    "Este cuaderno, lápiz y la conversación escrita en los ejercicios. Si puedes, conversa con alguien de tu casa sobre una historia.",
    "Aprenderé a conversar con otros para encontrar ideas nuevas sin perder mi propósito. Sirve para que mi texto sea más rico y siga teniendo sentido.",
    ["Sé mirar una imagen y sacar ideas.", "Sé escuchar a otras personas."],
    ["Conversar con otros es otra forma de generar ideas. Cada persona piensa algo distinto y puede ayudarte a ver cosas que no habías notado. Por eso es útil preguntar: ¿qué se te ocurre? ¿qué pasaría si...?",
     "Pero no todas las ideas sirven para tu texto. Primero debes tener claro tu propósito: qué quieres lograr y para quién escribes. Cuando escuches una idea, pregúntate: ¿esta idea ayuda a mi propósito? Si ayuda, la anotas. Si no, la dejas aunque sea buena.",
     "Algunas ideas se pueden adaptar. Por ejemplo, si quieres un cuento realista para niños de primero, «un dinosaurio en el charco» no encaja, pero «el gato quiere salir a jugar» sí. Escucha con respeto y toma solo lo que sirve.",
     "También puedes conversar sobre experiencias personales, es decir, cosas que te pasaron. Si cuentas «una vez resbalé en un charco» y alguien te pregunta «¿qué sentiste?», aparecen ideas nuevas: el susto, la risa, la ropa mojada. Tus compañeros o tu profesora pueden ayudarte con preguntas. Las experiencias son una buena fuente de ideas porque las conoces bien."],
    [("propósito", "lo que quiero lograr con mi texto"), ("audiencia", "personas que leerán o escucharán mi texto"), ("aportar", "agregar una idea útil"), ("adaptar", "cambiar una idea para que sirva"), ("respeto", "escuchar y valorar lo que dicen otros"), ("experiencia personal", "algo que me pasó y puedo contar")],
    [("Idea que sirve", "Propósito: cuento sobre la niña del charco. Pedro dice: «El gato quiere salir a jugar con ella». ¿Sirve?", ["Mi propósito es un cuento sobre la niña.", "El gato aparece en la imagen.", "La idea suma al cuento."], "Sí, sirve porque suma al cuento de la niña"),
     ("Idea que no encaja", "Mateo dice: «Podría haber un dinosaurio». Si el propósito es un cuento realista, ¿sirve?", ["Los dinosaurios ya no existen.", "No encaja con lo realista.", "No la uso."], "No, porque no es realista")],
    [("Anotar todas las ideas sin pensar si sirven.", "El texto pierde su propósito.", "Pregunta siempre: ¿ayuda a lo que quiero lograr?"), ("Rechazar una idea sin escucharla.", "Quizás se puede adaptar.", "Escucha y piensa cómo usarla.")],
    ([E("Conversación: " + CONV + " ¿Para quién escribe Ana?", "Para niños de primero", "Ana lo dice al inicio."),
      E("Conversación: " + CONV + " ¿Qué idea propuso Pedro?", "Que el gato quiere salir a jugar con ella", "Pedro habla del gato."),
      E("Conversación: " + CONV + " ¿Qué idea propuso Mateo?", "Que haya un dinosaurio en el charco", "Mateo habla del dinosaurio.")],
     [E("¿Para qué conversamos antes de escribir?", "Para encontrar ideas nuevas", "Otros aportan ideas."),
      E("En Lenguaje: ¿Qué es el propósito de un texto?", "Lo que quiero lograr con él", "Guía qué ideas elegir."),
      E("¿Todas las ideas que dicen otros sirven siempre?", "No, solo las que ayudan al propósito", "Hay que elegir.")],
     [E("Conversación: " + CONV + " Ana quiere un cuento realista. ¿Sirve la idea del gato?", "Sí", "Un gato mirando desde la puerta es posible."),
      E("Conversación: " + CONV + " Ana quiere un cuento realista. ¿Sirve la idea del dinosaurio?", "No", "No es realista."),
      E("Conversación: " + EXP + " Sofía escribirá sobre un día de lluvia. Anota dos ideas de la experiencia de Rodrigo que le sirven.", "Resbaló en un charco y se rio; su mamá le dio ropa seca y chocolate caliente", "La experiencia de un compañero da ideas para escribir.")],
     [E("Ana dice: «No quiero escuchar a Mateo porque su idea es tonta». ¿Es una buena forma de conversar? Explica.", "No, hay que escuchar con respeto aunque no la use", "Se escucha y luego se decide."),
      E("Conversación: " + EXP + " La profesora le preguntó a Rodrigo: «¿Qué hiciste después?». ¿Para qué sirve esa pregunta?", "Para sacar más ideas de su experiencia", "Una pregunta ayuda a recordar y ampliar lo que pasó.")],
     [E("Propón una idea para el cuento de la niña del charco que sea realista y que agregue algo nuevo.", "La niña salta en el charco porque la lluvia es su favorita", "Es realista y aporta una razón."),
      E("Adapta la idea del dinosaurio para que sirva en un cuento realista.", "La niña imagina que el charco tiene un dinosaurio", "Se mantiene la fantasía en la imaginación.")]),
    [E("Quieres escribir un cuento corto de aventura en el patio para niños de primero. Un amigo dice: «Cuenta cómo funciona un motor». ¿Esa idea sirve? Explica.", "No, porque no es una aventura para niños de primero", "No ayuda al propósito.")],
    [E("¿Conversar puede dar ideas nuevas?", "Sí", "Otras personas aportan ideas distintas."),
     E("¿Hay que anotar todas las ideas, sirvan o no?", "No", "Se eligen las que ayudan al propósito."),
     E("¿Se debe escuchar con respeto?", "Sí", "Valorar a otros ayuda a conversar.")],
    ("Con el propósito «escribir un cuento sobre la niña del charco para niños de primero», lee estas cuatro ideas: A) La niña invita al gato a saltar. B) La niña descubre un tesoro bajo el charco. C) Explicar cómo se forma la lluvia. D) La niña vuelve a casa y toma sopa. Marca las que sirven y escribe por qué rechazas alguna. Después escribe una pregunta que le harías a un compañero para que te cuente una experiencia suya de un día de lluvia.", "Sirven A, B y D. No sirve C porque explica ciencia y no cuenta un cuento. Pregunta: ¿Qué te pasó una vez cuando llovió mucho?", ["marca las ideas que sirven", "rechaza al menos una", "da una razón", "escribe una pregunta sobre una experiencia"], ["selección con razones"], ["aceptar todo", "rechazar sin razón"], "Conversa con otra persona y compara tus elecciones."),
    "Pregunta a alguien en tu casa qué cuento le gustaría y anota una idea.",
    "Elige una idea que rechazaste y piensa cómo adaptarla.")

BANCO = ("«Ideas: 1) La niña se pone las botas y sale. 2) Salta en el charco. 3) El gato la mira desde la puerta. 4) El viento se lleva su paraguas. 5) Vuelve a casa y toma sopa.»")
reg(
    OA16, 3,
    "Este cuaderno, lápiz y el banco de ideas escrito en los ejercicios. Puedes escribir cada idea en un papelito y moverla.",
    "Aprenderé a elegir ideas y ordenarlas en inicio, desarrollo y cierre. Sirve para armar un plan antes de escribir.",
    ["Sé reunir ideas de una imagen y de una conversación.", "Sé que una narración tiene inicio, desarrollo y desenlace."],
    ["Cuando ya tienes muchas ideas, debes elegir. No todas entran en un texto corto. Escoge las que ayudan a tu propósito y que se conectan entre sí. Las demás las guardas para otra ocasión.",
     "Después las ordenas. En un cuento, el inicio presenta al personaje y lo que quiere. El desarrollo cuenta el problema y las acciones. El cierre resuelve el problema. Cada idea elegida va en una de esas tres partes.",
     "Un organizador es una tabla o esquema con tres espacios: inicio, desarrollo y cierre. Escribes en cada espacio las ideas que van ahí. Así ves de un vistazo si tu historia tiene sentido y si falta algo."],
    [("seleccionar", "elegir las ideas que sirven"), ("organizador", "esquema para ordenar ideas"), ("inicio", "parte donde se presenta al personaje"), ("desarrollo", "parte donde pasan los hechos"), ("cierre", "parte donde se resuelve y termina")],
    [("Elegir el inicio", BANCO + " ¿Qué idea va en el inicio?", ["El inicio presenta al personaje.", "La idea 1 muestra a la niña saliendo.", "Va primero."], "La idea 1"),
     ("Ordenar", BANCO + " ¿Qué ideas van en el desarrollo?", ["El desarrollo cuenta lo que pasa.", "Las ideas 2, 3 y 4 son hechos.", "Las pongo en medio."], "Las ideas 2, 3 y 4")],
    [("Poner todas las ideas sin ordenar.", "El texto queda desordenado.", "Usa un organizador de inicio, desarrollo y cierre."), ("Dejar fuera una parte, como el cierre.", "El texto queda sin final.", "Revisa que haya inicio, desarrollo y cierre.")],
    ([E("Ideas: " + BANCO + " ¿Qué idea va primero?", "La niña se pone las botas y sale", "Presenta al personaje y comienza la historia."),
      E("Ideas: " + BANCO + " ¿Qué idea va al final?", "Vuelve a casa y toma sopa", "Cierra el cuento."),
      E("Ideas: " + BANCO + " ¿Cuántas ideas hay en total?", "5", "Están numeradas del 1 al 5.")],
     [E("¿Qué es un organizador?", "Un esquema para ordenar ideas", "Ayuda a planificar."),
      E("¿En qué parte se presenta al personaje: inicio o cierre?", "Inicio", "Allí se dice quién es."),
      E("¿En qué parte se resuelve el problema: desarrollo o cierre?", "Cierre", "El final resuelve.")],
     [E("Ideas: " + BANCO + " Ordena las ideas 2 y 4 dentro del desarrollo. ¿Cuál va primero si la niña salta y luego se vuela el paraguas?", "La 2", "Primero salta, después se vuela el paraguas."),
      E("Ideas: " + BANCO + " Elige las tres ideas del desarrollo.", "2, 3 y 4", "Son hechos que pasan en el medio."),
      E("Escribe cuál idea de la lista sería la de inicio: «La niña mira la lluvia por la ventana», «El gato salta», «La niña toma sopa».", "La niña mira la lluvia por la ventana", "Presenta la situación inicial.")],
     [E("Ema pone «vuelve a casa y toma sopa» en el inicio. ¿Por qué no va ahí?", "Porque es una idea de cierre", "Ocurre al terminar la historia."),
      E("Hay seis ideas y el texto es corto. ¿Conviene usar todas? Explica.", "No, conviene elegir las que ayudan", "Seleccionar evita que el texto se llene de cosas.")],
     [E("Arma un organizador con las ideas: «La niña se pone las botas y sale», «Salta en el charco», «Vuelve a casa y toma sopa». Escribe inicio, desarrollo y cierre.", "Inicio: se pone las botas y sale. Desarrollo: salta en el charco. Cierre: vuelve a casa y toma sopa", "Cada idea va en su parte."),
      E("Agrega una idea al desarrollo para que haya un problema: puede ser que algo se pierde o se rompe.", "El viento se lleva su paraguas", "Es un problema que se resuelve después.")]),
    [E("Tu equipo tiene estas ideas para un cuento sobre un perro que se pierde: «El perro sigue un olor», «Una niña lo encuentra», «El perro vuelve a casa», «Al inicio el perro juega en el patio». Ordénalas.", "El perro juega en el patio, sigue un olor, una niña lo encuentra, vuelve a casa", "Es el orden de los hechos.")],
    [E("¿Hay que elegir las ideas que sirven?", "Sí", "No entran todas."),
     E("¿Un organizador tiene inicio, desarrollo y cierre?", "Sí", "Son sus tres partes."),
     E("¿El cierre va primero?", "No", "Va al final.")],
    ("Elige cuatro ideas de esta lista para un cuento sobre un conejo que busca zanahorias y organízalas: «El conejo sale de su madriguera», «Ve una huerta cerrada», «Un niño abre la reja», «Hay un cartel de museo», «El conejo come y vuelve contento», «El conejo cuenta monedas». Haz un organizador con inicio, desarrollo y cierre.", "Inicio: sale de su madriguera. Desarrollo: ve una huerta cerrada; un niño abre la reja. Cierre: come y vuelve contento.", ["elige cuatro ideas", "las ordena en tres partes", "descarta las que no sirven"], ["organizador con tres partes"], ["usar ideas sin relación", "olvidar el cierre"], "Cuenta el cuento en voz alta con tu organizador."),
    "Ordena tres ideas de tu día con inicio, desarrollo y cierre.",
    "Escribe tres ideas más que podrían ir en el desarrollo del cuento del conejo.")

reg(
    OA16, 4,
    "Este cuaderno, lápiz y los planes escritos en los ejercicios. Sin materiales especiales.",
    "Aprenderé a comprobar que mi plan responde a mi propósito y a mi audiencia. Sirve para saber si estoy listo para escribir.",
    ["Sé elegir ideas y ordenarlas.", "Sé qué es el propósito de un texto."],
    ["Un plan listo para usar tiene cuatro cosas. Primero, el propósito: qué quiero lograr. Segundo, la audiencia: para quién escribo. Tercero, las ideas ordenadas en inicio, desarrollo y cierre. Cuarto, el vocabulario que usaré, simple para niños y más técnico para personas expertas.",
     "Antes de empezar a escribir, comprueba el plan con preguntas. ¿Cada idea ayuda al propósito? ¿Se entiende para la audiencia? ¿Hay inicio, desarrollo y cierre? ¿Falta alguna parte? Si algo no cuadra, cambia el plan antes de escribir; es más fácil que cambiar el texto terminado.",
     "Un plan no es el texto: son notas. Pueden ser palabras sueltas o frases cortas. Cuando el plan está listo, usas cada idea para escribir uno o dos párrafos. Si en medio de la escritura se te ocurre algo mejor, puedes ajustar el plan."],
    [("plan", "esquema de lo que voy a escribir"), ("audiencia", "personas para quienes escribo"), ("propósito", "lo que quiero lograr al escribir"), ("coherente", "que todas las partes encajan"), ("ajustar", "cambiar un poco para mejorar")],
    [("Revisar el plan", "Plan: Propósito: contar un cuento a niños de primero. Inicio: el niño sale al patio. Desarrollo: ve un bote. Cierre: ninguno. ¿Qué falta?", ["Reviso las tres partes.", "No hay cierre.", "Falta resolver."], "Falta el cierre"),
     ("Plan y audiencia", "Un plan para niños de primero usa la palabra «odisea». ¿Es adecuada?", ["Pienso en la edad.", "«Odisea» es difícil.", "Conviene una palabra simple."], "No, es difícil para esa edad")],
    [("Empezar a escribir con un plan incompleto.", "Quedan partes sin cubrir.", "Revisa propósito, audiencia y las tres partes."), ("Usar palabras difíciles para una audiencia pequeña.", "No lo entenderán.", "Elige un vocabulario que ellos conozcan.")],
    ([E("Plan: Propósito: cuento para niños de primero. Inicio: Leo sale a la playa. Desarrollo: construye un castillo y la marea lo destruye. Cierre: hace otro más lejos. ¿Tiene las tres partes?", "Sí", "Hay inicio, desarrollo y cierre."),
      E("Plan: Propósito: cuento para niños de primero. Inicio: Leo sale a la playa. Desarrollo: construye un castillo y la marea lo destruye. Cierre: hace otro más lejos. ¿Cuál es el problema?", "La marea destruye el castillo", "Impide lo que quería."),
      E("Plan: Propósito: cuento para niños de primero. Inicio: Leo sale a la playa. Desarrollo: construye un castillo y la marea lo destruye. Cierre: hace otro más lejos. ¿Para quién es?", "Para niños de primero", "La audiencia aparece en el propósito.")],
     [E("¿Qué cuatro cosas tiene un plan listo?", "Propósito, audiencia, ideas ordenadas y vocabulario", "Esas cuatro partes lo completan."),
      E("¿Por qué conviene comprobar el plan antes de escribir?", "Porque es más fácil cambiar el plan que el texto", "Se ahorra trabajo."),
      E("¿Un plan es el texto terminado?", "No", "Son notas para escribir.")],
     [E("Plan: Propósito: cuento para niños de primero. Inicio: Mía vive en un pueblo con viento. Desarrollo: no puede volar su volantín. Cierre: ninguno. ¿Qué parte falta?", "El cierre", "No dice cómo termina."),
      E("Plan para niños de primero: usará la palabra «odisea». Elige la palabra más simple: odisea, viaje o travesía.", "viaje", "Es la más conocida por niños pequeños."),
      E("Plan: Propósito: informar sobre las abejas. Inicio: Leo sale a la playa. ¿Esta idea ayuda al propósito?", "No", "Habla de otra cosa.")],
     [E("Tomás dice: «Mi plan está listo» pero no sabe para quién escribe. ¿Qué le falta?", "La audiencia", "Sin audiencia no sabe qué vocabulario usar."),
      E("Ema ve que una idea no ayuda al propósito. ¿Qué es mejor: dejarla igual o quitarla?", "Quitarla", "Mantener el plan coherente.")],
     [E("Completa este plan con las cuatro cosas: tema, la niña del charco. Debe incluir propósito, audiencia, tres ideas ordenadas y una palabra simple.", "Propósito: cuento; audiencia: niños de primero; inicio: sale con botas; desarrollo: salta y se vuela el paraguas; cierre: toma sopa; palabra: charco", "Tiene las cuatro cosas."),
      E("Escribe tres preguntas para comprobar un plan.", "¿Cada idea ayuda al propósito? ¿Es adecuado para la audiencia? ¿Hay inicio, desarrollo y cierre?", "Cualquier tres preguntas similares sirven.")]),
    [E("Tu curso hará un cartel informativo para niños de pre-kínder sobre las abejas. Tu plan dice: «Usaré palabras muy técnicas». ¿Está bien? Explica.", "No, porque los niños pequeños no las entienden", "El vocabulario debe adaptarse a la audiencia.")],
    [E("¿El plan incluye el propósito?", "Sí", "Es la primera parte."),
     E("¿Puedo ajustar el plan mientras escribo?", "Sí", "Si encuentro algo mejor."),
     E("¿El plan incluye la audiencia?", "Sí", "Dice para quién escribo.")],
    ("Haz un plan completo para un texto que elijas: a) un recado a tu familia, b) un cuento corto sobre un zorro, c) un artículo sobre la lluvia. Escribe propósito, audiencia, ideas en inicio, desarrollo y cierre, y dos palabras que usarás. Luego revísalo con las tres preguntas de comprobación.", "Cuento corto. Propósito: entretener. Audiencia: mi hermano de 6 años. Inicio: un zorro tiene hambre. Desarrollo: busca comida y un perro lo asusta. Cierre: encuentra frutas. Palabras: hambre, frutas.", ["tiene propósito y audiencia", "ideas en tres partes", "se revisó con las preguntas"], ["plan completo con revisión"], ["olvidar la audiencia", "plan sin cierre"], "Cuenta tu plan a otra persona y pregunta si entendió qué vas a escribir."),
    "Cuenta oralmente un plan de tres partes para un cuento.",
    "Cambia la audiencia de tu plan y escribe qué ajustes harías.")
