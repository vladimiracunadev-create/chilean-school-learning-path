"""Cuaderno del estudiante, 2.º básico Orientación: OA 05 (buen trato, solidaridad y respeto) y OA 06 (conflictos entre pares)."""
from __future__ import annotations

from student_content_or2_a import lesson, T, W, M
from student_lessons import ex

OA5, OA6 = "OR02 OA 05", "OR02 OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y lápiz. Las escenas con frases de saludo y petición están escritas en los ejercicios.",
    "Aprenderé formas de buen trato: saludar, despedirse, pedir por favor y dar las gracias. Sirve para que todos nos sintamos bien en el curso y en casa.",
    ["Sé decir hola y chao.", "Sé que las palabras pueden alegrar o molestar."],
    [
        "El buen trato es tratar a los demás con respeto y cariño. Se nota en palabras y gestos simples. Saludar cuando llegas, despedirte cuando te vas, pedir las cosas por favor y decir gracias cuando te ayudan. Son palabras pequeñas con un efecto grande.",
        "Saludar es mirar a la persona y decir «hola» o «buenos días». Despedirte es decir «chao» o «hasta mañana». Al pedir algo, usa «por favor» y un tono amable, sin gritar ni exigir. Si te dicen que no, puedes responder «está bien».",
        "Cada familia y cultura saluda a su manera: con la mano, con una sonrisa o con un abrazo si ambos quieren. Lo importante es que el otro se sienta bien tratado. El buen trato también se usa con quienes nos cuesta: al compañero que no es tu amigo y a quienes trabajan en tu escuela.",
    ],
    [("buen trato", "tratar a otros con respeto y cariño"), ("saludar", "decir hola al encontrarse con alguien"), ("despedirse", "decir chao al irse"), ("por favor", "palabra para pedir con respeto"), ("gracias", "palabra para agradecer lo que alguien hizo")],
    [
        W("Pedir con buen trato", "Rosa quiere usar la tijera de Beto. ¿Qué dice mejor: «Dame la tijera» o «¿Me prestas la tijera, por favor?»?", ["La primera frase manda.", "La segunda pide con respeto.", "El «por favor» y la pregunta muestran buen trato."], "«¿Me prestas la tijera, por favor?»"),
        W("Agradecer", "Pablo recoge el lápiz que se cayó de Ema. ¿Qué puede decir Ema?", ["Pablo hizo algo amable.", "Se agradece lo que alguien hace.", "Ema puede decir «gracias»."], "«Gracias, Pablo»"),
    ],
    [
        M("Pensar que saludar solo es para los amigos.", "Saludamos más a quienes conocemos mejor.", "Saluda también a compañeros y adultos de la escuela."),
        M("Pedir las cosas gritando porque estoy apurado.", "El apuro hace olvidar el tono.", "Respira y di «por favor» con voz tranquila."),
    ],
    R=[
        ex("Al llegar al curso, ¿qué dices para saludar?", "Hola o buenos días", "Es la forma básica de saludo."),
        ex("Al recibir ayuda, ¿qué palabra dices?", "Gracias", "Agradece lo que hicieron por ti."),
        ex("Al irte de un lugar, ¿qué puedes decir?", "Chao o hasta mañana", "Es una despedida."),
    ],
    U=[
        ex("¿Para qué sirve decir «por favor» al pedir algo?", "Para pedir con respeto", "Muestra que la petición no es una orden."),
        ex("¿Se puede saludar de formas distintas?", "Sí", "Cada familia y cultura saluda a su manera."),
        ex("¿Se usa el buen trato solo con los amigos?", "No", "Se usa con todas las personas."),
    ],
    A=[
        ex("Dani quiere que Pía le pase un lápiz. Escribe una frase con buen trato.", "¿Me pasas el lápiz, por favor?", "Pide con respeto."),
        ex("Luis llega al curso y ve a su profesora. Escribe un saludo.", "Buenos días, profesora", "Es un saludo respetuoso."),
        ex("Elige la mejor forma de pedir: «¡Pásame eso!» o «¿Me puedes pasar eso, por favor?»", "«¿Me puedes pasar eso, por favor?»", "Es más amable."),
    ],
    Z=[
        ex("Un niño dice: «No digo gracias porque ya sabe que se lo agradezco». ¿Qué le falta considerar?", "Que decirlo hace sentir bien al otro", "Las palabras hacen visible el agradecimiento."),
        ex("Una niña saluda con la mano y otra con un abrazo. ¿Alguna saluda mal?", "No, ambas saludan bien", "Hay varias formas de saludar con respeto."),
    ],
    D=[
        ex("Si das 3 saludos por la mañana y 2 por la tarde, ¿cuántos saludos diste?", "5", "3 más 2 es 5."),
        ex("En una fila, un niño empuja y dice «permiso». ¿Hay buen trato aunque diga permiso?", "No del todo, empujar no es buen trato", "El gesto debe ser respetuoso también."),
    ],
    context=[ex("En la panadería, Camila dice: «Buenas tardes, ¿me da un pan, por favor?». Al recibirlo dice: «Gracias, chao». ¿Qué formas de buen trato usó?", "Saludó, pidió por favor, agradeció y se despidió", "Usó las cuatro formas que vimos.")],
    selfcheck=[ex("¿Decir «por favor» es buen trato?", "Sí", "Muestra respeto al pedir."), ex("¿Saludar con respeto puede hacerse de varias maneras?", "Sí", "Lo importante es el respeto."), ex("¿Se agradece lo que hacen por mí?", "Sí", "Reconoce al otro.")],
    task=T("Escribe o di una frase de buen trato para cada situación: (1) llegas al curso, (2) pides un borrador prestado, (3) te ayudaron a recoger tus cosas, (4) te vas a casa. Usa estas palabras: hola, por favor, gracias, chao.", "(1) «Hola, buenos días.» (2) «¿Me prestas tu borrador, por favor?» (3) «Gracias por ayudarme.» (4) «Chao, hasta mañana.»", ["cuatro frases", "usa las palabras de buen trato", "tono amable"], ["frases escritas o dichas"], ["pedir con tono de orden", "olvidar una situación"], "Reconoce cada frase y pregunta cómo se siente quien la escucha."),
    reinforce="Hoy saluda a tres personas y agradece una vez.",
    extend="Escribe un saludo que podrías usar con un adulto mayor.",
)

lesson(
    OA5, 2,
    "Una hoja y lápiz. Los diálogos y las filas están escritos en los ejercicios.",
    "Aprenderé a escuchar a los demás y a esperar mi turno. Sirve para que todos puedan hablar y jugar con tranquilidad.",
    ["Sé que hablar con respeto es buen trato.", "Sé qué es una fila."],
    [
        "Escuchar es poner atención a quien habla. Para hacerlo, dirige tu atención a la persona, calla tu voz y piensa en lo que dice. No interrumpas. Cuando termine, puedes responder. Escuchar muestra que la otra persona te importa.",
        "Respetar el turno es esperar a que llegue tu momento. Hay turnos para hablar, para jugar, para usar un material y para pasar en la fila. Si todos esperan, todos tienen su oportunidad. Si alguien se salta el turno, los demás pierden.",
        "A veces esperar cuesta. Puedes contar hasta 10, respirar o pensar qué vas a decir. Si no logras esperar, pide ayuda. Algunas personas necesitan apoyo especial para esperar, y eso se respeta. Los acuerdos de turno también cuidan a quienes hablan más bajito.",
    ],
    [("escuchar", "poner atención a quien habla"), ("interrumpir", "hablar cuando otro todavía está hablando"), ("turno", "momento que le toca a cada persona"), ("esperar", "aguantar un momento hasta que llegue mi turno"), ("fila", "personas una detrás de otra")],
    [
        W("Esperar el turno", "Hay tres niños en la fila del bebedero: Ema, Beto y Rosa, en ese orden. ¿Quién va primero?", ["La fila va en orden de llegada.", "Ema está primera.", "Ema bebe primero."], "Ema"),
        W("No interrumpir", "Luis está contando su fin de semana. Ana quiere decir algo. ¿Qué hace?", ["Luis todavía no termina.", "Ana espera.", "Cuando él termine, Ana habla."], "Esperar a que Luis termine y luego hablar"),
    ],
    [
        M("Hablar al mismo tiempo que otro porque tengo mucho que decir.", "Las ganas de hablar son más grandes que la espera.", "Espera, cuenta hasta 10 y habla cuando termine el otro."),
        M("Pensar que esperar significa que no me toca nunca.", "Cuesta ver que el turno llega.", "Todos tienen su turno; el mío también llega."),
    ],
    R=[
        ex("Cuando alguien habla, ¿qué haces: escuchar o interrumpir?", "Escuchar", "Escuchar es poner atención."),
        ex("En una fila, ¿quién va primero: quien llegó antes o quien llegó después?", "Quien llegó antes", "Así se respeta el turno."),
        ex("¿Todos tienen derecho a un turno?", "Sí", "El turno es para todos."),
    ],
    U=[
        ex("¿Qué es interrumpir?", "Hablar cuando otro todavía está hablando", "Corta lo que el otro quería decir."),
        ex("¿Qué puedes hacer si te cuesta esperar?", "Contar hasta 10 o respirar", "Ayuda a calmar las ganas de hablar."),
        ex("¿Por qué es importante respetar el turno?", "Para que todos tengan su oportunidad", "Si alguien se salta el turno, otros pierden."),
    ],
    A=[
        ex("En la fila hay 4 niños y tú eres el tercero. ¿Cuántos niños van antes?", "2", "Van el primero y el segundo."),
        ex("Pedro quiere hablar y Sofía todavía está contando algo. Escribe una frase para pedir su turno.", "¿Puedo hablar cuando termines?", "Pide el turno sin interrumpir."),
        ex("Elige cómo escuchar mejor: prestar atención a quien habla o conversar con otro compañero.", "Prestar atención a quien habla", "Poner atención muestra que la otra persona te importa."),
    ],
    Z=[
        ex("Un niño dice: «Yo hablo primero porque soy más alto». ¿Es un buen motivo?", "No", "El turno no depende de la altura sino del orden."),
        ex("Una niña habla muy bajito y nadie la oye. Los demás hablan fuerte. ¿Qué pueden hacer?", "Hacer silencio para escucharla", "Escuchar también cuida a quienes hablan bajito."),
    ],
    D=[
        ex("Si hay 6 niños esperando y pasan 2, ¿cuántos esperan?", "4", "6 menos 2 es 4."),
        ex("Si un niño se salta la fila y el que estaba primero se enoja, ¿qué podría decir el que se la saltó?", "Perdón, voy al final de la fila", "Repara y vuelve a su lugar."),
    ],
    context=[ex("En el juego de dados, cada niño tira una vez por turno. Leo tira dos veces seguidas. Ana le dice: «Te tocaba a Camila». ¿Qué debería hacer Leo?", "Pedir disculpas y esperar su próximo turno", "Respeta a Camila y al orden del juego.")],
    selfcheck=[ex("¿Escuchar es poner atención?", "Sí", "Es poner atención y callar mientras el otro habla."), ex("¿Interrumpir respeta el turno?", "No", "Corta al que habla."), ex("¿Todos tienen turno?", "Sí", "Es una regla de respeto.")],
    task=T("Mira este diálogo: «Ema: Ayer fui al parque. Beto: ¡Yo también fui! Luis: Yo vi un perro…». Escribe cómo corregirías el diálogo para que cada uno espere su turno. Escribe también una frase para pedir tu turno.", "Ema: Ayer fui al parque. Beto espera y después dice: Yo también fui. Frase: «¿Puedo hablar cuando termines?»", ["corrige el diálogo con turnos", "escribe una frase para pedir el turno", "nombra una forma de esperar"], ["diálogo corregido"], ["dejar las interrupciones", "no pedir el turno"], "Reconoce lo corregido y pregunta cómo se sentirá Ema al ser escuchada."),
    reinforce="Hoy escucha a alguien sin interrumpir hasta que termine.",
    extend="Practica con un adulto: cada uno habla un minuto y el otro solo escucha.",
)

lesson(
    OA5, 3,
    "Una hoja y lápiz. Las situaciones con útiles, juguetes y salas están escritas en los ejercicios.",
    "Aprenderé a cuidar lo mío, lo de otros y los espacios que usamos juntos. Sirve para que los materiales duren y todos nos sintamos respetados.",
    ["Sé que algunas cosas son mías y otras de otros.", "Sé ordenar mis cosas."],
    [
        "Las pertenencias son las cosas que son de alguien, como tu mochila o tus lápices. Las cosas de otros se respetan: no se toman sin pedir permiso, no se rompen ni se esconden. Si pides algo prestado, lo cuidas y lo devuelves cuando prometiste.",
        "También hay cosas de todos, como la sala, el patio, los libros de la biblioteca y los baños. Se llaman espacios y bienes compartidos. Para cuidarlos, los dejas ordenados, no los rayas y avisas si algo se rompió. Así los puede usar el curso siguiente.",
        "Si por accidente se te rompe algo ajeno, avisa y ofrece ayuda para arreglarlo o reponerlo con un adulto. Los accidentes pasan. Lo importante es decir la verdad. Si ves algo ajeno perdido, entrégalo a un adulto para que llegue a su dueño.",
    ],
    [("pertenencia", "cosa que es de alguien"), ("permiso", "decir que sí antes de usar algo ajeno"), ("préstamo", "dejar usar algo por un tiempo"), ("espacio compartido", "lugar que usamos entre todos"), ("reponer", "devolver algo igual a lo que se rompió")],
    [
        W("Pedir permiso", "Tomás quiere usar la regla de Ema. ¿Qué hace primero?", ["La regla es de Ema.", "Debe pedir permiso.", "Si Ema dice sí, la usa y la devuelve."], "Pedir permiso a Ema"),
        W("Un accidente", "A Luis se le cayó y se quebró el lápiz de Pía. ¿Qué hace?", ["Fue un accidente.", "Debe decir la verdad.", "Puede ofrecer reponerlo con un adulto."], "Avisar a Pía y ofrecer reponerlo"),
    ],
    [
        M("Tomar algo ajeno porque «solo lo voy a mirar».", "Pensamos que un momento no cuenta.", "Pide permiso incluso para mirar."),
        M("Esconder que algo se rompió por miedo a que me reten.", "El miedo hace callar.", "Decir la verdad ayuda a arreglarlo."),
    ],
    R=[
        ex("Antes de usar el cuaderno de otro niño, ¿qué haces?", "Pido permiso", "Es una cosa que es de él."),
        ex("Si pides algo prestado, ¿lo devuelves?", "Sí", "Es parte de respetar el préstamo."),
        ex("¿La sala es un espacio compartido?", "Sí", "Es usada por todo el curso."),
    ],
    U=[
        ex("¿Qué son las pertenencias?", "Las cosas que son de alguien", "Por ejemplo mochila, lápiz o libro."),
        ex("Si algo se rompió por accidente, ¿qué conviene hacer?", "Decir la verdad y ofrecer ayuda", "Así se repara el daño."),
        ex("Si encuentras un abrigo perdido, ¿qué haces?", "Lo entrego a un adulto", "Para que llegue a su dueño."),
    ],
    A=[
        ex("Rosa pidió prestado un libro por 3 días y ya pasaron 5. ¿Cuántos días de atraso lleva?", "2", "5 menos 3 es 2."),
        ex("Beto usó la tijera del curso. ¿Dónde debe dejarla?", "En su lugar, ordenada", "Así el siguiente la encuentra."),
        ex("Escribe una frase para pedir prestado un lápiz.", "¿Me prestas tu lápiz, por favor?", "Pide permiso con respeto."),
    ],
    Z=[
        ex("Un niño dijo: «No fui yo» aunque rompió una silla sin querer. ¿Qué pudo hacer mejor?", "Decir la verdad", "Los accidentes se arreglan mejor con la verdad."),
        ex("Dos niños ven un cuaderno en el piso. Uno lo guarda en su mochila y otro lo lleva a la profesora. ¿Quién cuida mejor el espacio compartido?", "El que lo lleva a la profesora", "Así el cuaderno vuelve a su dueño."),
    ],
    D=[
        ex("Si el curso tiene 10 lápices compartidos y se pierden 2, ¿cuántos quedan?", "8", "10 menos 2 es 8."),
        ex("Si cada día 3 niños ordenan la sala, ¿cuántos niños ordenan en 4 días?", "12", "3 más 3 más 3 más 3 es 12."),
    ],
    context=[ex("Al terminar arte, quedan lápices tirados, papeles en el piso y pintura en la mesa. Ema dice: «Lo dejamos como estaba». ¿Qué conviene hacer?", "Ordenar entre todos", "Es un espacio compartido y se cuida entre todos.")],
    selfcheck=[ex("¿Se pide permiso para usar algo ajeno?", "Sí", "Así se respeta al dueño."), ex("¿Los espacios compartidos se cuidan?", "Sí", "Los usamos todos."), ex("¿Se dice la verdad cuando algo se rompe?", "Sí", "Ayuda a arreglarlo.")],
    task=T("Escribe o dibuja tres acciones de cuidado: una para tus pertenencias, una para las de otro niño y una para un espacio compartido, como la sala. Usa estas ideas: guardar, pedir permiso, devolver, ordenar, avisar.", "Mis cosas: guardo mi estuche. De otro: pido permiso y devuelvo el lápiz. Compartido: dejo la sala ordenada.", ["tres acciones", "una por cada tipo", "usa verbos de cuidado"], ["lista escrita o dibujada"], ["olvidar pedir permiso", "no incluir espacios compartidos"], "Reconoce cada acción y sugiere decir la verdad si hay un accidente."),
    reinforce="Hoy devuelve algo prestado y ordena un espacio compartido.",
    extend="Escribe una regla de tres palabras para cuidar la sala.",
)

lesson(
    OA5, 4,
    "Una hoja y lápiz. Las escenas de ayuda están escritas en los ejercicios.",
    "Aprenderé a ser solidario ayudando sin hacer por los demás lo que pueden hacer solos. Sirve para apoyar a otros cuidando su esfuerzo.",
    ["Sé que ayudar es una forma de afecto.", "Sé que debo preguntar antes de ayudar."],
    [
        "La solidaridad es ayudar a otros cuando lo necesitan, porque nos importan. Se puede ayudar en el curso, en casa o en la comunidad. Por ejemplo, ofrecer tu lápiz, invitar a jugar a quien está solo, acompañar a un compañero nuevo o ayudar a cargar una bolsa pesada.",
        "Ayudar bien tiene una regla: no sustituir. Sustituir es hacer por el otro lo que él puede hacer solo. Antes de ayudar pregunta: «¿Qué necesitas?». Ayuda con la parte que no puede o con una pista. Así la persona sigue aprendiendo y se siente capaz.",
        "También puedes recibir solidaridad. Cuando alguien te ayuda, di gracias. Y si algo es peligroso, como un enchufe o un objeto filoso, no ayudes tú. Avisa a un adulto. Ser solidario es cuidar a los demás sin ponerte en peligro.",
    ],
    [("solidaridad", "ayudar a otros porque me importan"), ("sustituir", "hacer por otro lo que puede hacer solo"), ("colaborar", "trabajar juntos para lograr algo"), ("necesidad", "algo que alguien requiere"), ("peligroso", "que puede hacer daño")],
    [
        W("Ayudar sin sustituir", "Ana lee muy despacio y quiere leer sola un párrafo. Beto se ofrece a leerlo por ella. ¿Es mejor leerlo por ella o preguntarle qué necesita?", ["Leerlo por ella le quita la práctica.", "Preguntar le deja decidir.", "Es mejor preguntar."], "Preguntarle qué necesita"),
        W("Pedir ayuda a un adulto", "Tomás ve que un compañero intenta alcanzar un objeto filoso arriba de un estante. ¿Qué hace Tomás?", ["Es un objeto peligroso.", "No lo toma él.", "Avisa a un adulto."], "Avisar a un adulto"),
    ],
    [
        M("Hacer toda la tarea de otro para ayudarlo.", "Pensamos que ayudar es resolverlo.", "Ayuda con una parte o una pista, y deja que él termine."),
        M("Ayudar con algo peligroso por mi cuenta.", "Queremos resolver rápido.", "Avisa a un adulto cuando hay peligro."),
    ],
    R=[
        ex("Acompañar a un compañero nuevo en el recreo, ¿es solidaridad?", "Sí", "Ayuda a que se sienta incluido."),
        ex("Antes de ayudar, ¿qué conviene preguntar?", "¿Qué necesitas?", "Así sabes cómo ayudar."),
        ex("¿Una pista sustituye al otro?", "No", "Le ayuda sin hacerlo por él."),
    ],
    U=[
        ex("¿Qué es sustituir?", "Hacer por otro lo que puede hacer solo", "Quita el esfuerzo del otro."),
        ex("¿Qué es la solidaridad?", "Ayudar a otros porque me importan", "Nace del cuidado por los demás."),
        ex("¿Debes ayudar tú con algo peligroso?", "No", "Debe hacerlo un adulto."),
    ],
    A=[
        ex("Ema se cae y se lastima el brazo. Elige la mejor ayuda: avisar a un adulto o seguir jugando.", "Avisar a un adulto", "Un adulto puede cuidarla mejor."),
        ex("Luis tiene problemas para abrochar su mochila. Escribe una pregunta para ofrecer ayuda.", "¿Quieres que te ayude con la mochila?", "Pregunta antes de ayudar."),
        ex("Rosa cargaba una mochila muy pesada. Un compañero la ayudó con una parte. ¿Sustituyó o ayudó?", "Ayudó", "Hizo solo una parte y ella siguió."),
    ],
    Z=[
        ex("Un niño dice: «Yo hago todo, así termino más rápido». ¿Qué pierde su compañero?", "La oportunidad de aprender y colaborar", "Hacerlo todo quita el esfuerzo del otro."),
        ex("Una niña ayuda a un compañero con una pista y él la hace solo. ¿Cómo se siente él, probablemente?", "Capaz y orgulloso", "Ayuda sin quitarle su logro."),
    ],
    D=[
        ex("Tres niños ayudan a mover libros y cada uno lleva 4. ¿Cuántos libros mueven entre los tres?", "12", "4 más 4 más 4 es 12."),
        ex("Pía está sola en el recreo. Elige la acción solidaria: invitarla a jugar o pasar de largo.", "Invitarla a jugar", "Ofrecer compañía muestra que ella importa; si dice que no, se respeta."),
    ],
    context=[ex("En clase, Pablo no entiende cómo se arma una tabla. Su compañera Rosa le dice: «Si quieres, te muestro una fila y las otras las haces tú». ¿Cómo ayudó Rosa?", "Con una parte y dejó que él siguiera", "Ayudó sin sustituir.")],
    selfcheck=[ex("¿La solidaridad es ayudar a otros?", "Sí", "Porque me importan."), ex("¿Se debe sustituir al otro?", "No", "Quita su esfuerzo."), ex("¿Con peligro avisas a un adulto?", "Sí", "No resuelves solo.")],
    task=T("Elige una de estas situaciones y escribe qué harías para ser solidario sin sustituir: (1) un compañero nuevo no conoce el patio, (2) una amiga no puede abrir su colación, (3) un niño no encuentra su cuaderno. Escribe la pregunta que harías y una acción de ayuda.", "Situación 1: «¿Quieres que te muestre el patio?» Lo acompaño y le muestro los lugares.", ["pregunta antes de ayudar", "acción de ayuda que no sustituye", "pide ayuda a un adulto si hay peligro"], ["frases escritas o dichas"], ["hacerlo todo por el otro", "no preguntar"], "Reconoce la pregunta y sugiere ayudar con la parte más pequeña."),
    reinforce="Hoy ayuda a alguien con una parte pequeña y deja que termine solo.",
    extend="Escribe una situación en que debes avisar a un adulto en vez de ayudar tú.",
)

lesson(
    OA5, 5,
    "Una hoja y lápiz. Las reglas para clasificar y el formato del acuerdo están escritos en los ejercicios.",
    "Aprenderé a armar un acuerdo de convivencia con reglas claras y positivas. Sirve para que todos sepamos cómo tratarnos en el curso.",
    ["Sé saludar, esperar turnos y cuidar lo de otros.", "Sé que ayudar es solidaridad."],
    [
        "Un acuerdo de convivencia es un conjunto de reglas que hacemos entre todos para llevarnos bien. Cada regla dice qué hacemos, no solo qué no hacemos. Por ejemplo: «Escuchamos cuando alguien habla» es mejor que «No interrumpir».",
        "Un buen acuerdo es corto, claro y posible de cumplir. Tres o cuatro reglas son suficientes. Debe cuidar a todos y no dejar a nadie fuera. También debe decir qué hacemos cuando alguien no cumple: recordar con respeto y ayudar a reparar.",
        "Si alguien rompe una regla, no es para humillarlo. Es para ayudarle a volver al acuerdo. Y los acuerdos pueden cambiar cuando el curso lo decide. Todos participan y todos firman, con su nombre o un dibujo.",
    ],
    [("acuerdo", "regla que decidimos entre todos"), ("convivencia", "vivir juntos de forma respetuosa"), ("cumplir", "hacer lo que se acordó"), ("reparar", "arreglar el daño"), ("posible", "que se puede lograr")],
    [
        W("Regla positiva", "Convierte «No gritar» en una regla que diga qué hacemos.", ["Piensa en qué conducta queremos.", "En vez de gritar, hablamos con voz tranquila.", "Escribo lo que sí hacemos."], "Hablamos con voz tranquila"),
        W("Elegir reglas posibles", "¿Cuál regla es posible: «Siempre estaremos felices» o «Saludamos al llegar»?", ["Nadie puede estar siempre feliz.", "Saludar se puede lograr.", "La regla debe poder cumplirse."], "«Saludamos al llegar»"),
    ],
    [
        M("Hacer una lista larga de cosas prohibidas.", "Pensamos que más reglas es mejor.", "Escribe tres o cuatro reglas claras y positivas."),
        M("Creer que el acuerdo es solo del profesor.", "Se cree que lo manda un adulto.", "El acuerdo se arma entre todos y todos lo firman."),
    ],
    R=[
        ex("¿El acuerdo de convivencia se hace entre todos?", "Sí", "Todos participan en armarlo."),
        ex("¿Una regla positiva dice lo que sí hacemos?", "Sí", "Indica una conducta clara."),
        ex("¿Todos firman el acuerdo?", "Sí", "Es parte de comprometerse."),
    ],
    U=[
        ex("¿Cuántas reglas conviene tener en un buen acuerdo?", "Tres o cuatro", "Son pocas y fáciles de recordar."),
        ex("¿Para qué sirve un acuerdo de convivencia?", "Para llevarnos bien entre todos", "Dice cómo nos tratamos."),
        ex("Si alguien no cumple, ¿se le humilla?", "No", "Se le ayuda a volver al acuerdo."),
    ],
    A=[
        ex("Cambia «No correr en la sala» por una regla positiva.", "Caminamos en la sala", "Dice lo que sí hacemos."),
        ex("Elige la regla clara: «Ser buenos» o «Esperamos nuestro turno para hablar».", "«Esperamos nuestro turno para hablar»", "Es concreta y observable."),
        ex("Cambia «No botar basura al piso» por una regla positiva.", "Usamos el basurero", "Dice lo que sí hacemos."),
    ],
    Z=[
        ex("Un curso escribió 20 reglas. Nadie las recuerda. ¿Qué podrían hacer?", "Elegir las 3 o 4 más importantes", "Un acuerdo corto es más fácil de cumplir."),
        ex("Un niño dice: «Esa regla no me gusta, no la cumplo». ¿Qué pueden hacer?", "Conversar y ver si el curso quiere cambiarla", "Los acuerdos se pueden revisar entre todos."),
    ],
    D=[
        ex("Si un curso de 20 niños y niñas firma el acuerdo y 18 ya firmaron, ¿cuántos faltan?", "2", "20 menos 18 es 2."),
        ex("Si se acuerdan 4 reglas y se cumplen 3 hoy, ¿cuántas faltaron?", "1", "4 menos 3 es 1."),
    ],
    context=[ex("En el curso de Ema, el recreo estaba muy desordenado. Armaron tres reglas: «Esperamos turnos», «Ordenamos lo que usamos» y «Hablamos con respeto». ¿Son reglas positivas?", "Sí", "Dicen lo que sí hacemos.")],
    selfcheck=[ex("¿El acuerdo lo arma solo el adulto?", "No", "Lo armamos entre todos."), ex("¿Las reglas deben decir lo que sí hacemos?", "Sí", "Así son más claras."), ex("¿Se puede cambiar un acuerdo si el curso lo decide?", "Sí", "Los acuerdos se revisan.")],
    task=T("Escribe un acuerdo de convivencia de tres reglas para tu curso o tu casa. Usa las ideas de este módulo: buen trato, turnos, cuidado de lo de otros y ayuda. Escribe cada regla en positivo y firma con tu nombre o un dibujo.", "1. Saludamos al llegar. 2. Esperamos nuestro turno. 3. Ordenamos lo que usamos. Firma: un dibujo de una estrella.", ["tres reglas", "escritas en positivo", "posibles de cumplir", "incluye firma"], ["acuerdo escrito o dibujado"], ["usar reglas negativas", "reglas imposibles"], "Reconoce las reglas y sugiere revisar cada cierto tiempo si funcionan."),
    reinforce="Pega tu acuerdo en un lugar visible y léelo en voz alta.",
    extend="Agrega una cuarta regla sobre cómo reparamos cuando alguien no cumple.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y lápiz. Las escenas de conflicto están escritas en los ejercicios.",
    "Aprenderé a identificar qué ocurre en un conflicto: quiénes participan, qué pasó y qué sienten. Sirve para entender un problema antes de buscar cómo resolverlo.",
    ["Sé reconocer emociones.", "Sé que las personas piensan distinto."],
    [
        "Un conflicto es un desacuerdo entre dos o más personas porque quieren cosas distintas. Es normal que existan. Pasan por muchos motivos: querer el mismo juguete, no ponerse de acuerdo en las reglas de un juego o sentir que alguien fue injusto.",
        "Para entender un conflicto, responde cuatro preguntas. ¿Quiénes participan? ¿Qué pasó? ¿Qué quiere cada uno? ¿Cómo se sienten? Cuenta los hechos, es decir, lo que se vio, y no opiniones como «es un mentiroso». Los hechos ayudan a pensar con calma.",
        "No todos los problemas son conflictos entre iguales. Si alguien golpea, amenaza o se burla muchas veces de otra persona, no es solo un conflicto: es una situación que debe conocer un adulto. En esos casos no se arregla solo entre niños. Pide ayuda de inmediato.",
    ],
    [("conflicto", "desacuerdo entre personas que quieren cosas distintas"), ("hecho", "lo que realmente pasó y se pudo ver"), ("opinión", "lo que alguien piensa o cree"), ("participar", "ser parte de algo"), ("burla repetida", "reírse de alguien muchas veces para herirlo")],
    [
        W("Contar los hechos", "Ana y Beto discuten porque ambos quieren el balón. Ana dice: «Beto es un egoísta». ¿Qué parte es un hecho?", ["«Beto es un egoísta» es una opinión.", "«Ambos quieren el balón» se vio.", "Ese es el hecho."], "Ambos quieren el balón"),
        W("Reconocer cuándo avisar", "Luis le dice cada día un apodo ofensivo a Pía y ella llora. ¿Es un conflicto simple?", ["Se repite cada día.", "Le hace daño a Pía.", "Un adulto debe saberlo."], "No, un adulto debe saberlo"),
    ],
    [
        M("Contar un conflicto con opiniones como «siempre me molesta».", "Estamos enojados y exageramos.", "Cuenta los hechos: qué pasó y cuándo."),
        M("Pensar que solo se pelean los niños «malos».", "Se cree que el conflicto es un defecto.", "Los conflictos pasan entre todos."),
    ],
    R=[
        ex("¿Es normal tener conflictos?", "Sí", "Pasan entre personas que piensan distinto."),
        ex("Dos niños quieren el mismo columpio. ¿Es un conflicto?", "Sí", "Quieren lo mismo a la vez."),
        ex("¿Un hecho es lo que se vio?", "Sí", "Es lo que realmente pasó."),
    ],
    U=[
        ex("En Orientación: ¿Qué es un conflicto?", "Un desacuerdo entre personas que quieren cosas distintas", "Es una diferencia entre dos o más personas."),
        ex("¿Qué diferencia hay entre un hecho y una opinión?", "El hecho se vio; la opinión es lo que pienso", "Los hechos ayudan a entender."),
        ex("Si alguien golpea o amenaza muchas veces, ¿es un conflicto simple?", "No, debe saberlo un adulto", "Necesita ayuda de un adulto."),
    ],
    A=[
        ex("Pedro y Rosa discuten porque Pedro cambió las reglas del juego. Escribe quiénes participan.", "Pedro y Rosa", "Son las personas del desacuerdo."),
        ex("Elige el hecho: «Dani le quitó el lápiz a Sofía» o «Dani es un ladrón».", "«Dani le quitó el lápiz a Sofía»", "Es lo que se vio; la otra es una opinión."),
        ex("Ema quiere jugar a las escondidas y Luis a la pelota. ¿Qué quiere cada uno?", "Ema escondidas; Luis pelota", "Cada uno quiere una cosa."),
    ],
    Z=[
        ex("Un niño cuenta: «Ella siempre me hace trampa». ¿Es un hecho o una exageración?", "Una exageración", "«Siempre» no se puede comprobar."),
        ex("Dos niños se golpearon en un conflicto. ¿Pueden resolverlo solos sin avisar a nadie?", "No", "Hubo daño y debe saberlo un adulto."),
    ],
    D=[
        ex("En un recreo hubo 3 conflictos por el balón y 2 por la cuerda. ¿Cuántos conflictos hubo?", "5", "3 más 2 es 5."),
        ex("En un conflicto hay cuatro preguntas. Si respondiste 3, ¿cuántas faltan?", "1", "4 menos 3 es 1."),
    ],
    context=[ex("En el recreo, Camila y Luis discuten porque ambos quieren el mismo balón. Camila grita «¡tú siempre lo quitas!». Luis dice «¡tú no lo prestas!». ¿Cuál es el conflicto?", "Ambos quieren el mismo balón", "Es lo que los dos quieren a la vez.")],
    selfcheck=[ex("¿Un conflicto es normal?", "Sí", "Pasa entre todas las personas."), ex("¿Se cuentan hechos?", "Sí", "Los hechos ayudan."), ex("¿La violencia repetida se resuelve sola?", "No", "Debe saberlo un adulto.")],
    task=T("Lee esta escena: «Rosa y Beto quieren usar el mismo cuaderno de dibujo. Rosa lo tomó primero, Beto lo sacó de sus manos y Rosa gritó». Responde con tus palabras las cuatro preguntas: quiénes, qué pasó, qué quiere cada uno y cómo se sienten.", "Quiénes: Rosa y Beto. Pasó: ambos quieren el cuaderno. Quieren: usarlo. Sienten: rabia.", ["responde las cuatro preguntas", "usa hechos y no opiniones", "nombra emociones con cuidado"], ["respuestas escritas o dichas"], ["usar etiquetas", "olvidar una pregunta"], "Reconoce las respuestas y sugiere separar hechos de opiniones."),
    reinforce="Cuenta un conflicto que viste usando solo hechos.",
    extend="Escribe una situación que no es un conflicto sencillo y que un adulto debe conocer.",
)

lesson(
    OA6, 2,
    "Una hoja y lápiz. Los relatos con dos puntos de vista están escritos en los ejercicios.",
    "Aprenderé a escuchar a cada persona de un conflicto y a ponerme en su lugar. Sirve para entender lo que siente el otro sin dejar de decir lo que siento yo.",
    ["Sé reconocer qué ocurre en un conflicto.", "Sé que las emociones son normales."],
    [
        "La perspectiva es la forma en que cada persona ve lo que pasó. En un conflicto, cada uno tiene la suya, y ambas pueden ser ciertas. Por ejemplo, un niño siente que le quitaron el balón y el otro siente que lo había pedido primero. Ambos ven distinto.",
        "Escuchar la perspectiva del otro significa dejar que termine, mirarlo y repetir con tus palabras lo que dijo: «Entiendo que querías el balón desde antes». Ponerte en su lugar es imaginar cómo te sentirías tú. No significa que tengas que estar de acuerdo, pero ayuda a entender.",
        "Después, dices tu perspectiva con un mensaje en primera persona: «Yo me sentí mal cuando…». Evita las acusaciones como «tú siempre…». Si la otra persona no quiere escuchar, no lo obligues. Si hay gritos o golpes, busca ayuda de un adulto antes de seguir.",
    ],
    [("perspectiva", "la forma en que cada uno ve lo que pasó"), ("ponerse en el lugar del otro", "imaginar cómo se siente el otro"), ("repetir con mis palabras", "decir con mis palabras lo que escuché"), ("acusar", "echar la culpa a alguien"), ("mensaje en primera persona", "frase que parte con «yo me siento…»")],
    [
        W("Repetir con mis palabras", "Pía dice: «Quería el columpio porque llevaba esperando mucho». ¿Cómo lo repite Luis?", ["Debe decir lo que entendió.", "Usa sus propias palabras.", "No acusa ni discute."], "«Entiendo que llevabas rato esperando»"),
        W("Mensaje en primera persona", "Ema se enojó porque Tomás cambió su dibujo sin avisar. ¿Qué es mejor decir: «Tú siempre arruinas todo» o «Me sentí mal cuando cambiaste mi dibujo»?", ["La primera frase acusa.", "La segunda cuenta lo que siente Ema.", "Elige la segunda."], "«Me sentí mal cuando cambiaste mi dibujo»"),
    ],
    [
        M("Interrumpir al otro para decir mi versión.", "Queremos que nos entiendan primero.", "Deja que termine y luego habla tú."),
        M("Pensar que entender al otro es darle la razón.", "Se mezclan entender y acordar.", "Entender no es aceptar todo; es saber cómo lo vive."),
    ],
    R=[
        ex("¿Cada persona puede ver distinto lo que pasó?", "Sí", "Cada una tiene su perspectiva."),
        ex("Para escuchar al otro, ¿lo dejas terminar?", "Sí", "No se interrumpe."),
        ex("¿Acusar con «tú siempre…» ayuda a resolver?", "No", "Hace que el otro se defienda."),
    ],
    U=[
        ex("¿Qué es la perspectiva?", "La forma en que cada uno ve lo que pasó", "Cada persona ve el conflicto desde su lugar."),
        ex("¿Ponerse en el lugar del otro es estar siempre de acuerdo?", "No", "Es entender cómo se siente."),
        ex("¿Cómo empieza un mensaje en primera persona?", "Con «yo me siento…»", "Habla de lo que siento yo."),
    ],
    A=[
        ex("Dani dice: «Me enojé porque no me dejaron jugar». Escribe cómo lo repite Rosa con sus palabras.", "Entiendo que te enojaste porque no te dejaron jugar", "Repite lo que entendió."),
        ex("Cambia «Eres un egoísta» por un mensaje en primera persona.", "Yo me siento mal cuando no compartes", "Cuenta lo que siento sin acusar."),
        ex("Elige una frase para ponerse en el lugar de Beto, que perdió un juego: «¿Cómo te sientes?» o «No es para tanto».", "«¿Cómo te sientes?»", "Pregunta y no minimiza."),
    ],
    Z=[
        ex("Dos niños cuentan versiones distintas de lo mismo. ¿Uno miente necesariamente?", "No, cada uno puede ver distinto", "Las perspectivas pueden ser distintas."),
        ex("Una niña intenta explicar y el otro no quiere oírla. ¿Qué puede hacer?", "Esperar un momento o pedir ayuda a un adulto", "No se obliga a escuchar."),
    ],
    D=[
        ex("Si dos niños hablan 2 minutos cada uno, ¿cuántos minutos son?", "4", "2 más 2 es 4."),
        ex("Si uno de los niños grita y amenaza, ¿conviene seguir hablando solo con él?", "No, conviene avisar a un adulto", "La amenaza requiere ayuda."),
    ],
    context=[ex("Ema y Luis pelean porque Luis rompió la torre de Ema sin querer. Luis dice «fue un accidente». Ema dice «igual me dolió». ¿Pueden ser ciertas las dos cosas?", "Sí", "Fue un accidente y a Ema le dolió.")],
    selfcheck=[ex("¿Hay que dejar que el otro termine?", "Sí", "Así escuchas de verdad."), ex("¿Acusar ayuda a resolver?", "No", "Hace que el otro se defienda."), ex("¿Pedir ayuda a un adulto si hay gritos o golpes es buena idea?", "Sí", "Ayuda a mantener la seguridad.")],
    task=T("Lee esta escena: «Beto dice que Ana le quitó el balón sin permiso. Ana dice que Beto se lo había prestado». Escribe: (1) una frase para repetir lo que dice Beto con tus palabras, (2) una frase para repetir lo que dice Ana, (3) un mensaje en primera persona que diría cada uno.", "(1) Entiendo que sentiste que te quitaron el balón. (2) Entiendo que pensaste que podías tenerlo. (3) Beto: «Me sentí mal cuando lo tomaste sin preguntar.»", ["repite ambas perspectivas", "usa mensaje en primera persona", "no acusa"], ["frases escritas o dichas"], ["acusar a uno", "no repetir lo que dijo el otro"], "Reconoce las frases y pregunta cómo se siente cada persona."),
    reinforce="La próxima vez que alguien te cuente algo, repite con tus palabras lo que escuchaste.",
    extend="Escribe un mensaje en primera persona para una situación que te haya molestado.",
)

lesson(
    OA6, 3,
    "Una hoja y lápiz. Las situaciones con opciones de acuerdo están escritas en los ejercicios.",
    "Aprenderé a buscar acuerdos donde las dos personas ganan algo. Sirve para resolver un conflicto sin que alguien se sienta perdedor.",
    ["Sé escuchar las perspectivas de cada uno.", "Sé decir lo que siento sin acusar."],
    [
        "Un acuerdo es una solución que aceptan las personas del conflicto. Para encontrarlo, primero cada uno dice qué necesita. Luego piensan varias opciones, sin criticar ninguna. Por último, eligen la que sirve a ambos o en la que ambos ceden un poco.",
        "Hay formas simples de acuerdo. Turnarse: primero uno y luego el otro. Compartir: usar juntos. Cambiar: elegir otra actividad. Dividir: cada uno toma una parte. Un buen acuerdo es justo, posible de cumplir y lo aceptan todos. Si uno se siente obligado, no es un acuerdo.",
        "Antes de terminar, revisen: ¿cada uno entendió lo que acordó? ¿Se puede cumplir hoy? Si no llegan a un acuerdo, pueden pedir ayuda a un adulto, que escucha a ambos y ayuda a encontrar opciones. Pedir ayuda no es perder; es seguir cuidando la relación.",
    ],
    [("acuerdo", "solución que aceptan ambos"), ("opción", "una posible solución"), ("turnarse", "usar algo uno después del otro"), ("ceder", "dejar algo para que haya acuerdo"), ("justo", "que cuida a todos por igual")],
    [
        W("Pensar opciones", "Pía y Leo quieren el mismo columpio. Escribe tres opciones.", ["Turnarse: cada uno 10 empujones.", "Compartir: en el columpio doble, si hay.", "Cambiar: uno juega en el resbalín primero."], "Turnarse, compartir o cambiar de juego"),
        W("Elegir la mejor", "Ana y Beto discuten por un lápiz. Opciones: «Quedárselo el más fuerte» o «Usarlo por turnos de 5 minutos». ¿Cuál es justa?", ["La primera favorece al más fuerte.", "La segunda cuida a los dos.", "Elige los turnos."], "Usarlo por turnos de 5 minutos"),
    ],
    [
        M("Querer que el otro ceda todo.", "Pensamos que si cedemos perdemos.", "En un acuerdo cada uno cede un poco y gana algo."),
        M("Aceptar un acuerdo que no me gusta solo para terminar.", "Queremos acabar la discusión.", "Un buen acuerdo lo aceptan ambos; si no, se busca otra opción."),
    ],
    R=[
        ex("¿Un acuerdo lo deben aceptar ambos?", "Sí", "Si uno se siente obligado, no es acuerdo."),
        ex("Usar un juguete uno después del otro, ¿cómo se llama?", "Turnarse", "Cada uno usa en su momento."),
        ex("¿Se puede pedir ayuda a un adulto para llegar a un acuerdo?", "Sí", "Un adulto puede ayudar a encontrar opciones."),
    ],
    U=[
        ex("¿Cuáles son tres formas simples de acuerdo?", "Turnarse, compartir y cambiar", "Son opciones del texto."),
        ex("¿Qué debe ser un buen acuerdo?", "Justo, posible y aceptado por todos", "Así cuida a todos."),
        ex("¿Ceder un poco significa perder?", "No", "Permite que ambos ganen algo."),
    ],
    A=[
        ex("Dani y Rosa quieren la misma pelota. Escribe un acuerdo de turnos.", "Cada uno juega 5 minutos", "Reparte el tiempo igual."),
        ex("Tomás quiere jugar a las escondidas y Luisa a la pelota. Elige un acuerdo: jugar a una y luego a la otra o que se vaya uno.", "Jugar a una y luego a la otra", "Ambos juegan lo que quieren."),
        ex("Dos niños reparten stickers y cada uno recibe 6. ¿Cuántos stickers había en total?", "12", "6 más 6 es 12."),
    ],
    Z=[
        ex("Un niño dice: «El acuerdo es que yo gano». ¿Es un acuerdo justo?", "No", "No cuida al otro."),
        ex("Dos niñas aceptan turnos pero una se enoja y no cumple. ¿Qué pueden hacer?", "Revisar el acuerdo o pedir ayuda a un adulto", "Un acuerdo puede ajustarse."),
    ],
    D=[
        ex("Si cada niño usa el columpio 5 minutos y son 3 niños, ¿cuántos minutos pasan hasta que todos usaron?", "15", "5 más 5 más 5 es 15."),
        ex("Si hay 3 opciones y se descarta 1, ¿cuántas quedan?", "2", "3 menos 1 es 2."),
    ],
    context=[ex("Ema y Camila pelean porque ambas quieren dibujar con el único lápiz rojo. Ema propone: «Yo dibujo la mitad y luego tú». ¿Es un buen acuerdo?", "Sí", "Reparte el uso y ambas lo aceptan.")],
    selfcheck=[ex("¿Un acuerdo cuida a ambos?", "Sí", "Un acuerdo justo cuida a los dos."), ex("¿Se piensan varias opciones?", "Sí", "Ayuda a elegir mejor."), ex("¿Puedo pedir ayuda a un adulto?", "Sí", "Si no llegamos a un acuerdo.")],
    task=T("Lee esta escena: «Beto y Ana quieren el último trozo de plasticina de la caja. Beto lo tenía, Ana lo pidió primero». Escribe tres opciones de acuerdo y elige una explicando por qué es justa.", "Opciones: partirlo por la mitad, turnarse o buscar otro trozo. Elijo partirlo por la mitad porque ambos usan.", ["tres opciones", "elige una justa", "explica por qué"], ["opciones escritas"], ["elegir una opción que favorece a uno", "no explicar"], "Reconoce las opciones y pregunta cómo se sentiría cada uno."),
    reinforce="Cuando tengas un desacuerdo, piensa tres opciones antes de elegir.",
    extend="Escribe un acuerdo posible para un desacuerdo que viste en casa o en el curso.",
)

lesson(
    OA6, 4,
    "Una hoja y lápiz. Las disculpas y los casos están escritos en los ejercicios.",
    "Aprenderé a reparar el daño después de un conflicto y a reconciliarme cuando es seguro hacerlo. Sirve para volver a convivir con confianza.",
    ["Sé buscar acuerdos.", "Sé decir lo que siento."],
    [
        "Reparar es hacer algo para arreglar el daño que causaste. Una buena disculpa tiene cuatro partes. Digo qué hice. Digo que lo siento. Pregunto o propongo cómo arreglarlo. Y digo qué haré distinto. Por ejemplo: «Rompí tu dibujo. Lo siento. ¿Puedo ayudarte a hacer uno nuevo? La próxima vez preguntaré».",
        "Reconciliarse es volver a llevarse bien después del conflicto. Puede ser con un saludo, una sonrisa, jugar juntos de nuevo o un gesto que ambos quieran. Cada uno decide cuándo está listo. Si el otro necesita tiempo, se respeta. No se obliga a nadie a perdonar de inmediato.",
        "Reconciliarse no es volver a una situación que te hace daño. Si alguien te golpeó, te amenazó o se burla seguido, primero hay que avisar a un adulto. Estar seguro es lo primero. Un adulto ayudará a que la reparación sea justa y a que no se repita.",
    ],
    [("reparar", "arreglar el daño que causé"), ("disculpa", "palabras para reconocer que hice daño"), ("reconciliarse", "volver a llevarse bien"), ("perdonar", "decidir dejar atrás el enojo"), ("seguridad", "estar a salvo de daño")],
    [
        W("Armar una disculpa", "Tomás rompió sin querer la torre de Ema. Arma una disculpa con las cuatro partes.", ["Qué hice: rompí tu torre.", "Lo siento.", "Cómo arreglo: te ayudo a armarla otra vez. Qué haré distinto: miraré antes de pasar."], "«Rompí tu torre, lo siento, te ayudo a armarla y miraré antes de pasar»"),
        W("Reconciliarse con tiempo", "Después de discutir, Pía dice: «Todavía no quiero jugar contigo». ¿Qué hace Luis?", ["Pía necesita tiempo.", "Se respeta.", "Puede decir «cuando quieras me avisas»."], "Respetar y decir «cuando quieras me avisas»"),
    ],
    [
        M("Decir «perdón» sin más, para que me dejen en paz.", "Queremos acabar rápido.", "Di qué hiciste y cómo vas a arreglarlo."),
        M("Obligar al otro a perdonarme ahora mismo.", "Queremos sentirnos mejor.", "Cada uno perdona cuando está listo."),
    ],
    R=[
        ex("¿Reparar es arreglar el daño que causé?", "Sí", "Esa es la idea."),
        ex("¿Una disculpa dice qué hice?", "Sí", "Reconoce lo que pasó."),
        ex("¿Se puede obligar a perdonar?", "No", "Cada persona decide."),
    ],
    U=[
        ex("¿Cuáles son las cuatro partes de una buena disculpa?", "Qué hice, lo siento, cómo arreglarlo y qué haré distinto", "Así la disculpa repara de verdad."),
        ex("¿Qué es reconciliarse?", "Volver a llevarse bien", "Se recupera la buena relación."),
        ex("Si alguien te golpeó, ¿lo primero es reconciliarse o avisar a un adulto?", "Avisar a un adulto", "La seguridad va primero."),
    ],
    A=[
        ex("Rosa rayó el cuaderno de Beto. Escribe la primera parte de su disculpa.", "Rayé tu cuaderno", "Dice lo que hizo."),
        ex("Dani dijo algo hiriente. Elige cómo reparar: «Perdón y ya» o «Lo que dije te dolió, lo siento, no lo diré más».", "«Lo que dije te dolió, lo siento, no lo diré más»", "Reconoce, pide perdón y promete cambiar."),
        ex("Dos niños se reconcilian. Elige una forma: un saludo o fingir que no pasó nada.", "Un saludo", "Marca el reencuentro."),
    ],
    Z=[
        ex("Un niño que se burla cada día de otro dice «perdón» y sigue burlándose. ¿Es una reparación real?", "No", "Falta cambiar lo que hace y avisar a un adulto."),
        ex("Una niña acepta una disculpa pero dice «necesito un tiempo». ¿Hizo algo mal?", "No", "Puede perdonar a su ritmo."),
    ],
    D=[
        ex("Si una disculpa tiene 4 partes y dijiste 3, ¿cuántas faltan?", "1", "4 menos 3 es 1."),
        ex("Si alguien insiste en seguirte molestando después de disculparse, ¿qué haces?", "Aviso a un adulto de confianza", "Puede ser una situación que se repite."),
    ],
    context=[ex("Luis empujó a Ana en el recreo y ella se cayó. Luis le dice: «Te empujé, lo siento. ¿Estás bien? Ya no lo haré». Ana está llorando. ¿Qué debe hacer también Luis?", "Avisar a un adulto para que revise a Ana", "Hay un daño físico y un adulto debe ayudar.")],
    selfcheck=[ex("¿Una disculpa tiene varias partes?", "Sí", "Tiene cuatro partes distintas."), ex("¿Se puede esperar para perdonar?", "Sí", "Cada uno decide."), ex("¿La seguridad va primero?", "Sí", "Primero evitamos daño.")],
    task=T("Escribe una disculpa de cuatro partes para esta escena: «Pedro pisó sin querer el dibujo de Sofía y lo arrugó». Escribe también una frase de Sofía para decir si necesita tiempo o acepta. Si prefieres, usa otra escena que se parezca.", "Pedro: «Pisé tu dibujo. Lo siento. ¿Te ayudo a alisarlo o hacer otro? Miraré donde piso.» Sofía: «Gracias, necesito un rato».", ["incluye las cuatro partes", "frase del otro", "respeta los tiempos"], ["frases escritas o dichas"], ["disculpa sin explicar", "obligar a perdonar"], "Reconoce la disculpa y sugiere avisar a un adulto si hay daño o se repite."),
    reinforce="Si lastimas a alguien, usa las cuatro partes de la disculpa.",
    extend="Escribe cómo reparar un daño a una pertenencia y otro a los sentimientos.",
)
