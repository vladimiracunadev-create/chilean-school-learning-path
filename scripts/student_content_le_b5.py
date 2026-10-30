"""Cuaderno del estudiante, 1.º básico Lenguaje y Comunicación: OA 18 (comprensión de textos orales).

Los guiones que lee un adulto son textos originales y breves; cada ejercicio trae el guion que necesita.
"""
from __future__ import annotations

from student_lessons import ex, register

OA18 = "LE01 OA 18"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=open_task, reinforce=reinforce, extend=extend,
    )


AVISO = (
    "Aviso para el adulto que lee en voz alta: «Niños y niñas, el viernes iremos al parque. Salimos a las nueve. "
    "Traigan una botella con agua y un sombrero. Volvemos a las doce.»"
)

lesson(
    OA18, 1,
    "Un adulto que lea en voz alta los guiones de los ejercicios (o léelos tú). Cuaderno y lápiz.",
    "Aprenderé a escuchar con un propósito: saber qué necesito averiguar antes de oír. Sirve para recordar los datos importantes de lo que me dicen.",
    ["Sé escuchar en silencio.", "Sé contar hasta 12."],
    [
        "Escuchar es más que oír. Cuando escuchas con un propósito, piensas antes qué necesitas saber. Si un adulto va a dar un aviso, quizá necesites saber qué, cuándo y qué debes llevar. Con ese propósito, tu atención busca esos datos.",
        "Para escuchar bien, mira a quien habla, guarda silencio y piensa en las palabras importantes: horas, lugares, cosas que llevar. Puedes repetir los datos en tu mente o anotarlos con un dibujo o una palabra.",
        "Si algo no lo entendiste, levanta la mano y pide que lo repitan. Es mejor preguntar que quedarse con una duda. Al final, repasa los datos que escuchaste para comprobar que los recuerdas.",
    ],
    [("escuchar", "poner atención para entender"), ("propósito", "para qué escucho"), ("dato", "información importante"), ("aviso", "mensaje que informa algo"), ("repetir", "decir otra vez")],
    [
        ("Hora del aviso", f"{AVISO} ¿A qué hora salen?", ["Busco la hora de salida.", "Dice: salimos a las nueve."], "A las nueve"),
        ("Qué traer", f"{AVISO} ¿Qué deben traer?", ["Busco «traigan».", "Una botella con agua y un sombrero."], "Una botella con agua y un sombrero"),
    ],
    [
        ("Escuchar sin saber qué buscar.", "Se oye sin pensar.", "Piensa antes qué necesitas saber."),
        ("No pedir que repitan.", "Da vergüenza preguntar.", "Levanta la mano y pide repetir."),
    ],
    [
        E(f"{AVISO} ¿Adónde irán el viernes?", "Al parque", "El aviso lo dice."),
        E(f"{AVISO} ¿A qué hora vuelven?", "A las doce", "El aviso lo dice."),
        E("¿Qué se hace para escuchar bien? A) Mirar a quien habla B) Dibujar en la mesa", "A) Mirar a quien habla", "Así se mantiene la atención."),
    ],
    [
        E(f"{AVISO} ¿Cuántas cosas deben traer?", "2", "Una botella con agua y un sombrero."),
        E(f"{AVISO} ¿Cuántas horas (salida y regreso) se nombran?", "2", "Las nueve y las doce."),
        E("¿Qué es escuchar con un propósito?", "Pensar antes qué necesito averiguar", "Sirve para encontrar los datos importantes."),
    ],
    [
        E(f"{AVISO} Sabiendo que salen a las nueve y vuelven a las doce, ¿cuántas horas dura la salida?", "3 horas", "De las nueve a las doce pasan tres horas."),
        E("Otro aviso: «El lunes habrá reunión a las cuatro en la sala. Traigan una carpeta azul.» ¿Cuándo es la reunión?", "El lunes a las cuatro", "El aviso lo dice."),
        E("Otro aviso: «El lunes habrá reunión a las cuatro en la sala. Traigan una carpeta azul.» ¿Qué deben traer?", "Una carpeta azul", "El aviso lo dice."),
    ],
    [
        E(f"{AVISO} Ana anotó «sombrero» y «agua». Olvidó la hora. ¿Qué dato le falta?", "Las nueve", "Esa es la hora de salida."),
        E("Pablo dice que no necesita escuchar porque ya sabe. ¿Está bien? Responde sí o no.", "No", "Los datos pueden ser nuevos."),
    ],
    [
        E("Aviso: «La obra de teatro es el miércoles a las cinco en el patio. Entrada gratis.» ¿Cuánto cuesta entrar?", "Nada; es gratis", "El aviso dice que la entrada es gratis."),
        E("Aviso: «La feria abre el sábado a las diez y cierra a las cuatro.» ¿Cuántas horas dura la feria?", "6", "De diez a cuatro de la tarde hay seis horas."),
    ],
    [E("Tu profesora anuncia: «Mañana hay prueba de lectura a las nueve. Traigan un lápiz.» ¿Qué debes recordar? A) A las nueve y traer lápiz B) Que hay recreo", "A) A las nueve y traer lápiz", "Son los datos del aviso.")],
    [
        E("¿Para qué sirve escuchar con propósito?", "Para encontrar los datos que necesito", "La atención se dirige a lo importante."),
        E("¿Qué haces si no entendiste un dato?", "Pido que lo repitan", "Así aclaro mi duda."),
        E("¿Qué miro cuando alguien habla?", "A quien habla", "Ayuda a atender."),
    ],
    task(
        "Pide a un adulto que lea el aviso de esta clase (la salida al parque). Antes de que lea, escribe tus tres preguntas: ¿qué? ¿cuándo? ¿qué llevar? Después de escuchar, responde las tres.",
        "¿Qué? Salida al parque. ¿Cuándo? El viernes a las nueve. ¿Qué llevar? Una botella con agua y un sombrero.",
        ["escribe las tres preguntas antes", "responde las tres con datos del aviso", "los datos son correctos"],
        ["preguntas y respuestas escritas", "respuesta oral"],
        ["responder con datos que no están", "olvidar una pregunta"],
        "Pide que te lean el aviso otra vez para comprobar tus respuestas.",
    ),
    "Cuenta a alguien lo que escuchaste en el aviso.",
    "Escucha un aviso en tu casa o barrio y anota la hora y el lugar.",
)

DESCRIPCION = (
    "Guion: «Fuimos a una playa pequeña. La arena era tibia y amarilla. Había olas suaves que hacían espuma blanca. "
    "Un perro corría tras las gaviotas. Olía a mar y a sal.»"
)

lesson(
    OA18, 2,
    "Un adulto que lea en voz alta los guiones de los ejercicios. Cuaderno, lápiz y colores para dibujar.",
    "Aprenderé a imaginar lo que escucho y a relacionarlo con mis experiencias. Sirve para entender mejor y recordar lo que oigo.",
    ["Sé escuchar en silencio.", "Sé nombrar colores."],
    [
        "Cuando alguien describe algo, puedes hacer una película en tu mente: eso es visualizar. Si escuchas «arena tibia y amarilla», imaginas el color y la temperatura. Cada palabra que describe te da una imagen.",
        "También puedes conectar lo que oyes con tu vida. Si hablan de una playa, quizá recuerdes la vez que fuiste a una. Pensar en tus experiencias ayuda a entender mejor y a recordar lo escuchado.",
        "Para visualizar bien, cierra los ojos y presta atención a los colores, los sonidos, los olores y los movimientos. Después puedes dibujar lo que imaginaste o contarlo con tus palabras.",
    ],
    [("visualizar", "imaginar con la mente lo que escucho"), ("describir", "decir cómo es algo"), ("conectar", "relacionar con mi vida"), ("experiencia", "algo que viví"), ("detalle", "dato pequeño que da imagen")],
    [
        ("Visualizar", f"{DESCRIPCION} ¿De qué color es la arena?", ["Busco el color.", "Dice amarilla."], "Amarilla"),
        ("Conectar", "Si escuchas sobre una playa y recuerdas tu visita al mar, ¿qué estás haciendo?", ["Relaciono lo que oigo con algo mío.", "Eso es conectar."], "Conectando con mi experiencia"),
    ],
    [
        ("Escuchar sin imaginar nada.", "Se espera que alguien explique.", "Haz una película en tu mente."),
        ("Inventar detalles que no se dijeron.", "Se imagina de más.", "Imagina lo que se describe."),
    ],
    [
        E(f"{DESCRIPCION} ¿Cómo era la arena?", "Tibia y amarilla", "El guion lo dice."),
        E(f"{DESCRIPCION} ¿Qué hacía el perro?", "Corría tras las gaviotas", "El guion lo dice."),
        E(f"{DESCRIPCION} ¿A qué olía?", "A mar y a sal", "El guion lo dice."),
    ],
    [
        E(f"{DESCRIPCION} ¿De qué color era la espuma de las olas?", "Blanca", "El guion lo describe."),
        E(f"{DESCRIPCION} ¿Las olas eran suaves o fuertes?", "Suaves", "El guion lo dice."),
        E("Al escuchar la descripción de la playa, ¿qué es visualizar?", "Imaginar con la mente lo que escucho", "Es hacer una película mental."),
    ],
    [
        E(f"{DESCRIPCION} Completa: «Yo recuerdo que en el mar yo...» con una experiencia tuya (o inventada).", "Por ejemplo: Yo recuerdo que en el mar jugué con la arena", "Debe relacionar con una experiencia."),
        E("Guion: «El gato era gris con una mancha blanca en la pata y dormía en el sofá rojo.» ¿De qué color era el sofá?", "Rojo", "El guion lo dice."),
        E("Guion: «El gato era gris con una mancha blanca en la pata y dormía en el sofá rojo.» ¿Dónde estaba la mancha blanca?", "En la pata", "El guion lo dice."),
    ],
    [
        E(f"{DESCRIPCION} Pedro dice que había una tormenta. ¿Es correcto? Responde sí o no.", "No", "Había olas suaves y se pasaba bien."),
        E("Guion: «El gato era gris con una mancha blanca en la pata y dormía en el sofá rojo.» ¿Qué dibujo corresponde? A) gato gris con pata blanca en sofá rojo B) gato negro en sofá azul", "A", "Coincide con el guion."),
    ],
    [
        E("Guion: «En el patio hay un árbol alto. Sus hojas son verdes por fuera y claras por dentro. Un pájaro canta en la rama más alta.» ¿Dónde canta el pájaro?", "En la rama más alta", "El guion lo dice."),
        E("Con el guion del árbol, ¿cuántos elementos distintos se nombran (árbol, hojas, pájaro, rama)?", "4", "Se cuentan cuatro cosas."),
    ],
    [E("Una abuela cuenta cómo era su pueblo: «Tenía una plaza con una fuente de piedra y bancas verdes». Tomás recuerda su plaza. ¿Qué hace? A) Conecta con su experiencia B) No escucha", "A) Conecta con su experiencia", "Relaciona lo que oye con su vida.")],
    [
        E("¿Qué se hace para visualizar?", "Cerrar los ojos e imaginar", "Se forma una imagen mental."),
        E("Al oír sobre la playa y recordar mi paseo, ¿qué es conectar?", "Relacionar lo que oigo con mi vida", "Ayuda a entender."),
        E("¿Qué detalles ayudan a imaginar?", "Colores, sonidos y olores", "Todos ellos dan imágenes a la mente."),
    ],
    task(
        "Pide a un adulto que lea el guion «Fuimos a una playa pequeña...». Escucha con los ojos cerrados. Luego dibuja la playa con al menos cuatro detalles (arena, olas, perro, gaviotas) y di en una oración qué experiencia tuya te recordó.",
        "Dibujé la arena amarilla, las olas con espuma, el perro y las gaviotas. Me recordó la vez que jugué en la orilla del mar.",
        ["dibujo con al menos cuatro detalles del guion", "los colores coinciden con el texto", "dice una experiencia propia"],
        ["dibujo", "oración oral o escrita"],
        ["dibujar cosas que no se dijeron", "no relacionar con una experiencia"],
        "Compara tu dibujo con el guion y comprueba que cada detalle esté en el texto.",
    ),
    "Cuenta qué viste en tu mente al escuchar la descripción de la playa.",
    "Describe en voz alta tu cuarto para que otro lo dibuje.",
)

INSTR = (
    "Guion: «Toma una hoja. Dibuja un círculo grande en el centro. Dentro del círculo, dibuja dos puntos para los ojos. "
    "Debajo de los ojos, dibuja una línea curva hacia arriba. Arriba del círculo, dibuja tres líneas cortas.»"
)

lesson(
    OA18, 3,
    "Una hoja de papel, lápiz y un adulto que lea en voz alta el guion de las instrucciones.",
    "Aprenderé a seguir instrucciones que escucho, paso a paso. Sirve para hacer actividades, juegos y tareas sin equivocarme.",
    ["Sé dibujar un círculo.", "Sé qué significan arriba, abajo y en el centro."],
    [
        "Seguir instrucciones orales es escuchar cada paso y hacerlo en el orden en que se dice. Palabras como «primero», «luego», «debajo» y «arriba» indican qué hacer y dónde. Escucha todos los pasos con atención.",
        "Si no recuerdas un paso, pide que lo repitan. Puedes ir haciendo cada paso mientras lo oyes. Después, comprueba que lo que hiciste coincide con lo que dijeron: ¿están todos los pasos?, ¿en el lugar correcto?",
        "El orden importa. No es lo mismo dibujar los ojos antes del círculo que dentro del círculo. Una instrucción mal entendida cambia el resultado. Por eso conviene escuchar con calma.",
    ],
    [("instrucción", "dicho que indica qué hacer"), ("paso", "cada acción que me piden"), ("orden", "qué va primero y qué va después"), ("arriba", "en la parte de más alto"), ("debajo", "más abajo de algo")],
    [
        ("Primer paso", f"{INSTR} ¿Qué haces primero?", ["Busco el primer paso.", "Tomar una hoja."], "Tomar una hoja"),
        ("Ubicación", f"{INSTR} ¿Dónde dibujas los ojos?", ["Busco «ojos».", "Dentro del círculo."], "Dentro del círculo"),
    ],
    [
        ("Hacer los pasos desordenados.", "Se olvida lo que se dijo.", "Sigue el orden de las instrucciones."),
        ("No pedir que repitan.", "Da vergüenza.", "Levanta la mano y pide repetir."),
    ],
    [
        E(f"{INSTR} ¿Cuántos puntos dibujas para los ojos?", "2", "El guion dice dos puntos."),
        E(f"{INSTR} ¿Cómo es la línea que va debajo de los ojos?", "Curva hacia arriba", "El guion lo dice."),
        E(f"{INSTR} ¿Cuántas líneas cortas van arriba del círculo?", "3", "El guion dice tres."),
    ],
    [
        E(f"{INSTR} ¿Qué dibujo queda al final? A) Una cara sonriente con pelos B) Un árbol", "A) Una cara sonriente con pelos", "Círculo, ojos, sonrisa y tres líneas."),
        E(f"{INSTR} ¿Dónde va el círculo en la hoja?", "En el centro", "El guion lo dice."),
        E("¿Qué palabra indica que algo va más abajo?", "Debajo", "Señala una posición más baja."),
    ],
    [
        E("Guion: «Dibuja un cuadrado. Dentro, dibuja un triángulo. Debajo del cuadrado, dibuja dos líneas rectas.» ¿Qué va dentro del cuadrado?", "Un triángulo", "El guion lo indica."),
        E("Guion: «Dibuja un cuadrado. Dentro, dibuja un triángulo. Debajo del cuadrado, dibuja dos líneas rectas.» ¿Cuántas líneas van debajo?", "2", "El guion lo dice."),
        E("Guion: «Pinta el techo de rojo y la puerta de azul.» ¿De qué color es la puerta?", "Azul", "El guion lo dice."),
    ],
    [
        E(f"{INSTR} Ana dibujó los ojos fuera del círculo. ¿Siguió bien las instrucciones? Responde sí o no.", "No", "Debían ir dentro del círculo."),
        E(f"{INSTR} Beto dibujó tres líneas debajo del círculo. ¿Siguió bien las instrucciones? Responde sí o no.", "No", "Debían ir arriba del círculo."),
    ],
    [
        E("Guion: «Toma tres lápices. Pon el rojo a la izquierda y el azul a la derecha. El verde va en el medio.» ¿Qué color queda en el medio?", "Verde", "El guion lo dice."),
        E("Con el guion de los lápices, ¿qué orden queda de izquierda a derecha?", "Rojo, verde, azul", "Rojo a la izquierda, verde en el medio y azul a la derecha."),
    ],
    [E("Tu mamá dice: «Primero, lava las manos. Luego, pon la mesa. Al final, llama a tu hermano.» ¿Qué haces al final?", "Llamo a mi hermano", "Es el último paso.")],
    [
        E("¿Qué debes hacer con las instrucciones orales?", "Seguirlas en orden", "El orden cambia el resultado."),
        E("¿Qué significa «debajo»?", "Más abajo de algo", "Indica una posición."),
        E("¿Qué haces si no recuerdas un paso?", "Pido que lo repitan", "Así evito equivocarme."),
    ],
    task(
        "Pide a un adulto que lea en voz alta estas instrucciones y síguelas con papel y lápiz: «Dibuja un cuadrado grande. Dentro del cuadrado, dibuja una estrella. Arriba del cuadrado, dibuja un sol pequeño. Debajo del cuadrado, dibuja dos líneas onduladas.» Luego comprueba tu dibujo con una pauta: ¿hay cuadrado, estrella dentro, sol arriba, dos líneas abajo?",
        "Dibujé un cuadrado, una estrella adentro, un sol pequeño arriba y dos líneas onduladas abajo. Cumplí los cuatro pasos.",
        ["dibuja los cuatro elementos", "cada uno está en el lugar indicado", "comprueba con la pauta"],
        ["dibujo", "pauta marcada"],
        ["cambiar el lugar de un elemento", "olvidar un paso"],
        "Pide que te lean las instrucciones de nuevo y marca cada paso cumplido.",
    ),
    "Da a alguien tres instrucciones de dibujo y mira si las sigue bien.",
    "Inventa cuatro instrucciones para dibujar una casa y pide que las sigan.",
)

ANECDOTA = (
    "Guion: «Mi abuelo me contó que cuando era niño vivía en el sur. Cada mañana caminaba una hora para llegar a la escuela. "
    "En invierno llevaba botas de goma porque había mucho barro.»"
)

lesson(
    OA18, 4,
    "Un adulto que lea en voz alta los guiones de los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a hacer preguntas para obtener más información y aclarar dudas. Sirve para aprender más de lo que me cuentan.",
    ["Sé escuchar una anécdota.", "Sé qué es una pregunta."],
    [
        "Cuando escuchas algo y quieres saber más, haces preguntas. Las palabras para preguntar son: ¿qué?, ¿quién?, ¿cuándo?, ¿dónde?, ¿por qué? y ¿cómo? Cada una busca un dato distinto.",
        "Una buena pregunta se relaciona con lo que escuchaste y ayuda a saber algo nuevo. Si alguien cuenta que caminaba a la escuela, puedes preguntar «¿Qué veía en el camino?». Evita preguntas con respuesta de una sola palabra cuando quieres saber más.",
        "También puedes preguntar para aclarar una duda: «¿Puede repetir lo de las botas?». Preguntar no es molestar: es una forma de aprender mejor y de mostrar interés.",
    ],
    [("pregunta", "lo que digo para saber algo"), ("duda", "algo que no entendí"), ("¿por qué?", "pregunta para saber la razón"), ("¿cómo?", "pregunta para saber la manera"), ("aclarar", "hacer más claro")],
    [
        ("Hacer una pregunta", f"{ANECDOTA} ¿Qué pregunta te sirve para saber más del camino?", ["Pienso qué quiero saber.", "¿Qué veía en el camino?"], "¿Qué veía en el camino?"),
        ("Aclarar", f"{ANECDOTA} No oíste por qué usaba botas. ¿Qué preguntas?", ["Quiero la razón.", "¿Por qué usaba botas de goma?"], "¿Por qué usaba botas de goma?"),
    ],
    [
        ("Preguntar algo sin relación.", "No se escuchó bien.", "Pregunta sobre lo que oíste."),
        ("No preguntar por vergüenza.", "Se teme molestar.", "Pregunta con respeto: aprendes más."),
    ],
    [
        E(f"{ANECDOTA} ¿Dónde vivía el abuelo de niño?", "En el sur", "El guion lo dice."),
        E(f"{ANECDOTA} ¿Cuánto caminaba cada mañana?", "Una hora", "El guion lo dice."),
        E(f"{ANECDOTA} ¿Por qué llevaba botas de goma?", "Porque había mucho barro", "El guion lo explica."),
    ],
    [
        E("¿Qué palabra usas para preguntar por la razón?", "¿Por qué?", "Busca la causa."),
        E("¿Qué palabra usas para preguntar por el lugar?", "¿Dónde?", "Busca el sitio."),
        E("¿Qué palabra usas para preguntar por una persona?", "¿Quién?", "Busca quién hace algo."),
    ],
    [
        E(f"{ANECDOTA} Escribe una pregunta con «¿cuándo?» sobre lo que cuenta el abuelo.", "Por ejemplo: ¿Cuándo vivía en el sur?", "Debe usar cuándo."),
        E(f"{ANECDOTA} Escribe una pregunta con «¿cómo?» sobre el camino.", "Por ejemplo: ¿Cómo era el camino?", "Debe usar cómo."),
        E(f"{ANECDOTA} Escribe una pregunta con «¿qué?» sobre la escuela.", "Por ejemplo: ¿Qué hacía en la escuela?", "Debe usar qué."),
    ],
    [
        E(f"{ANECDOTA} Pedro preguntó «¿Cuántos autos tiene tu papá?». ¿Se relaciona con lo contado? Responde sí o no.", "No", "El relato no habla de autos."),
        E("¿Cuál da más información? A) ¿Te gustó? B) ¿Qué fue lo que más te gustó?", "B", "Pide un dato más completo."),
    ],
    [
        E("Guion: «Mi tía viajó en barco a una isla. Vio delfines.» Escribe una pregunta que ayude a saber más.", "Por ejemplo: ¿Cómo eran los delfines?", "Debe relacionarse con lo contado."),
        E("Ordena para formar una pregunta: «por qué / la tortuga / lenta / es / ¿?».", "¿Por qué la tortuga es lenta?", "Se arma la pregunta."),
    ],
    [E("Tu vecino cuenta que de niño ayudaba a su papá en la panadería y que se levantaba muy temprano. ¿Qué pregunta le haces para saber a qué hora se levantaba? A) ¿A qué hora te levantabas? B) ¿Te gusta el pan?", "A) ¿A qué hora te levantabas?", "Pregunta por el dato que quieres saber.")],
    [
        E("¿Para qué sirve preguntar?", "Para saber más y aclarar dudas", "Se aprende mejor."),
        E("¿Qué pregunta busca el lugar?", "¿Dónde?", "Pregunta por el sitio."),
        E("¿Con qué palabra preguntas la razón?", "¿Por qué?", "Pide la causa."),
    ],
    task(
        "Pide a un adulto que lea el guion del abuelo que vivía en el sur. Escribe tres preguntas para saber más, usando «¿qué?», «¿cómo?» y «¿por qué?». Pauta de oralidad: pregunto con voz clara, levanto la mano y espero la respuesta.",
        "¿Qué veía en el camino? ¿Cómo era la escuela? ¿Por qué había barro?",
        ["tres preguntas con las palabras pedidas", "se relacionan con el guion", "usa signos de pregunta"],
        ["tres preguntas escritas", "preguntas dichas en voz alta"],
        ["preguntas sin relación", "no usar las palabras pedidas"],
        "Lee tus preguntas a un adulto y comprueba que se pueda responder con lo contado.",
    ),
    "Haz una pregunta a alguien de tu casa sobre algo que contó.",
    "Escribe cinco preguntas para hacer a un abuelo sobre su infancia.",
)

PREG = (
    "Guion: «En mi barrio hay una plaza con muchos árboles. Después de la lluvia salen caracoles a pasear. "
    "Los niños los miran con cuidado y no los tocan para no hacerles daño.»"
)

lesson(
    OA18, 5,
    "Un adulto que lea en voz alta los guiones de los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a responder preguntas abiertas usando lo que escuché y mis propias ideas. Sirve para explicar lo que pienso con oraciones completas.",
    ["Sé escuchar una historia.", "Sé responder preguntas con una oración."],
    [
        "Una pregunta abierta no se responde con una sola palabra. Por ejemplo: «¿Por qué crees que los niños no tocan los caracoles?». La respuesta lleva una razón o una explicación y se dice con una oración completa.",
        "Para responder bien, piensa en lo que escuchaste y en lo que tú sabes. Luego usa «porque» para dar la razón: «Creo que no los tocan porque se les puede hacer daño». Si no estás seguro, puedes decir «Creo que...».",
        "Una buena respuesta abierta es clara, tiene sentido y se relaciona con la pregunta. No hay una única respuesta correcta, pero sí respuestas bien pensadas y respuestas que no se apoyan en nada.",
    ],
    [("pregunta abierta", "pregunta que no se responde con una sola palabra"), ("razón", "explicación de lo que pienso"), ("oración completa", "frase que dice algo completo"), ("explicar", "decir por qué o cómo"), ("porque", "palabra para dar la razón")],
    [
        ("Respuesta con razón", f"{PREG} ¿Por qué los niños no tocan los caracoles?", ["Busco la razón.", "Para no hacerles daño."], "Porque no quieren hacerles daño"),
        ("Respuesta abierta", f"{PREG} ¿Cómo cuidarías tú a los caracoles?", ["Pienso en lo escuchado y en mis ideas.", "Los miraría sin tocarlos."], "Los miraría sin tocarlos para no hacerles daño"),
    ],
    [
        ("Responder con una sola palabra.", "Se cree que basta.", "Responde con una oración completa."),
        ("Dar una respuesta sin relación.", "No se escuchó bien.", "Relaciona tu respuesta con lo que oíste."),
    ],
    [
        E(f"{PREG} ¿Cuándo salen los caracoles a pasear?", "Después de la lluvia", "El guion lo dice."),
        E(f"{PREG} ¿Qué hacen los niños con los caracoles?", "Los miran con cuidado", "El guion lo dice."),
        E(f"{PREG} ¿Dónde está la plaza?", "En el barrio", "El guion lo dice."),
    ],
    [
        E("¿Una pregunta abierta se responde con una palabra? Responde sí o no.", "No", "Necesita una explicación."),
        E(f"{PREG} ¿Cuál es una respuesta con razón? A) Porque no hacen ruido B) Para no hacerles daño", "B) Para no hacerles daño", "Es la razón que dice el guion."),
        E("¿Qué palabra ayuda a dar una razón?", "Porque", "Introduce la explicación."),
    ],
    [
        E(f"{PREG} Responde con una oración: «¿Por qué crees que salen después de la lluvia?»", "Por ejemplo: Creo que salen porque hay agua y humedad", "Debe dar una razón posible."),
        E(f"{PREG} Responde: «¿Qué harías tú si ves un caracol?»", "Por ejemplo: Lo miraría con cuidado", "Debe ser una oración con una acción."),
        E(f"{PREG} Completa: «Creo que es importante cuidar a los caracoles porque...»", "Por ejemplo: son seres vivos", "Debe dar una razón."),
    ],
    [
        E(f"{PREG} Luis responde «sí» a «¿Por qué los niños no los tocan?». ¿Está bien? Responde sí o no.", "No", "La pregunta pide una razón."),
        E("Ana responde: «Porque me gusta». A la pregunta «¿Por qué cuidar a los caracoles?». ¿Se relaciona con el guion?", "No", "No habla de los caracoles ni de su cuidado."),
    ],
    [
        E("Guion: «Rosa plantó una semilla y la regó todos los días. A las tres semanas salió un brote verde.» Pregunta: ¿Por qué salió el brote? Elige la mejor respuesta. A) Porque la regó todos los días B) Porque sí", "A", "Da una razón apoyada en el guion."),
        E("Con el guion de Rosa, ¿qué crees que haría Rosa con el brote? Escribe una respuesta con «Creo que...».", "Por ejemplo: Creo que seguirá regándolo", "Debe empezar con «Creo que» y tener sentido."),
    ],
    [E("En la sala la profesora cuenta cómo cuidar el agua: «Cerrar la llave mientras nos cepillamos los dientes ahorra agua.» Pregunta: ¿Por qué es bueno cerrar la llave? Elige la respuesta mejor pensada. A) Porque ahorramos agua B) Porque la llave se cansa", "A) Porque ahorramos agua", "Se apoya en lo dicho.")],
    [
        E("¿Qué lleva una respuesta abierta?", "Una razón o explicación", "No es una sola palabra."),
        E("¿Cómo respondes una pregunta abierta?", "Con una oración completa", "Se explica la idea."),
        E("Al responder una pregunta abierta, ¿qué palabra uso para dar la razón?", "Porque", "Une la respuesta con su razón."),
    ],
    task(
        "Pide a un adulto que lea esto: «En el patio hay un charco después de la lluvia. Un niño lo salta y se moja los pies. Otro lo rodea y llega seco.» Responde en voz alta con oraciones completas y razón: ¿Por qué crees que el segundo niño llegó seco? ¿Qué harías tú? Pauta de oralidad: respondo con «Creo que... porque...», hablo claro y miro a quien pregunta.",
        "Creo que el segundo niño llegó seco porque rodeó el charco. Yo lo rodearía porque no quiero mojarme los pies.",
        ["responde las dos preguntas", "usa «porque» en las dos", "oraciones completas relacionadas con el guion"],
        ["respuestas orales", "respuestas escritas"],
        ["responder con una sola palabra", "no dar razón"],
        "Pide al adulto que te diga qué razón te pareció mejor pensada.",
    ),
    "Responde en voz alta por qué es bueno cuidar el agua.",
    "Escribe dos preguntas abiertas sobre un cuento que conozcas y respóndelas.",
)

AGUA = (
    "Guion: «Para cuidar el agua podemos cerrar la llave mientras nos cepillamos los dientes. También podemos usar un balde para regar las plantas. "
    "Así el agua dura más y alcanza para todos.»"
)

lesson(
    OA18, 6,
    "Un adulto que lea en voz alta los guiones de los ejercicios. Cuaderno y lápiz.",
    "Aprenderé a dar mi opinión sobre lo que escucho y a apoyarla con razones. Sirve para participar en una conversación con respeto.",
    ["Sé escuchar un texto breve.", "Sé usar «porque»."],
    [
        "Una opinión es lo que tú piensas sobre algo que escuchaste. Para darla, usa frases como «Me parece que...» o «Creo que...». Una opinión mejora cuando agregas una razón con «porque» que se apoya en lo que oíste.",
        "Hay que distinguir lo que el texto dice, que es un dato, de lo que tú piensas, que es una opinión. «Podemos cerrar la llave» es un dato del guion. «Me parece fácil» es tu opinión.",
        "Cuando otras personas opinan distinto, se escucha con respeto. Puedes decir «Yo pienso distinto porque...» sin burlarte. Todos podemos aprender de lo que piensan los demás.",
    ],
    [("opinión", "lo que pienso sobre algo"), ("dato", "lo que el texto dice"), ("razón", "explicación de mi opinión"), ("respetar", "tratar bien a los demás"), ("de acuerdo", "pensar igual que otro")],
    [
        ("Dato u opinión", f"{AGUA} ¿«Se puede usar un balde para regar» es dato u opinión?", ["Está en el guion.", "Es un dato."], "Es un dato"),
        ("Opinar", f"{AGUA} Completa: «Me parece buena idea porque...»", ["Busco una razón del guion.", "El agua dura más y alcanza para todos."], "Me parece buena idea porque el agua dura más y alcanza para todos"),
    ],
    [
        ("Decir una opinión sin razón.", "Se piensa que basta.", "Agrega «porque» y una razón."),
        ("Burlarse de otra opinión.", "No se respeta al otro.", "Escucha y responde con respeto."),
    ],
    [
        E(f"{AGUA} ¿Qué se puede hacer mientras nos cepillamos los dientes?", "Cerrar la llave", "El guion lo dice."),
        E(f"{AGUA} ¿Para qué sirve un balde, según el guion?", "Para regar las plantas", "El guion lo dice."),
        E("«Me parece una buena idea» ¿es dato u opinión?", "Opinión", "Es lo que piensa quien habla."),
    ],
    [
        E(f"{AGUA} ¿Qué logra cuidar el agua, según el guion?", "Que dure más y alcance para todos", "El guion lo dice."),
        E("¿Qué palabra uso para dar la razón de mi opinión?", "Porque", "Anuncia la explicación."),
        E("¿Cuál es una opinión con razón? A) Me gustó. B) Me gustó porque aprendí a cuidar el agua.", "B", "Da una razón."),
    ],
    [
        E(f"{AGUA} Escribe tu opinión sobre cerrar la llave con «Me parece que... porque...».", "Por ejemplo: Me parece que está bien porque ahorramos agua", "Debe tener opinión y razón."),
        E(f"{AGUA} Completa: «Creo que usar un balde es ... porque...»", "Por ejemplo: útil porque no se gasta tanta agua", "Debe tener opinión y razón."),
        E("Escribe una frase para decir que piensas distinto de un compañero, con respeto.", "Por ejemplo: Yo pienso distinto porque...", "Debe usar «pienso distinto porque»."),
    ],
    [
        E(f"{AGUA} Pedro dice: «Cuidar el agua es aburrido». ¿Es dato u opinión?", "Opinión", "Lo piensa Pedro."),
        E(f"{AGUA} Mía dice: «Me parece importante porque alcanza para todos». ¿Cuál es su razón?", "Que alcanza para todos", "Está después de «porque»."),
    ],
    [
        E("Dos amigos opinan sobre el guion del agua. Luis: «Es buena idea porque ahorra agua». Rosa: «Es buena idea». ¿Quién apoyó mejor su opinión?", "Luis", "Dio una razón."),
        E("Beto opina distinto: «Creo que es difícil porque a veces me olvido». ¿Está bien pensar distinto? Responde sí o no.", "Sí", "Cada uno puede opinar, con respeto."),
    ],
    [E("Tu curso escucha que hay que cuidar el agua. Un compañero dice «Tonterías, no sirve». ¿Qué respuesta es respetuosa? A) «Yo pienso distinto porque ahorrar ayuda a todos» B) «Eres tonto»", "A) «Yo pienso distinto porque ahorrar ayuda a todos»", "Es respetuosa y da una razón.")],
    [
        E("Después de escuchar un texto, ¿qué es una opinión?", "Lo que yo pienso sobre algo", "Puede variar entre personas."),
        E("¿Cómo respondo si pienso distinto?", "Con respeto y una razón", "Así se conversa bien."),
        E("¿Qué palabra une mi opinión con su razón?", "Porque", "Anuncia la razón de mi opinión."),
    ],
    task(
        "Pide a un adulto que lea esto: «Hoy en la hora del cuento escuchamos que las abejas ayudan a las flores a dar frutos. Sin abejas habría menos fruta.» Da tu opinión en voz alta con «Me parece que... porque...» y escucha cómo opina otra persona. Pauta de oralidad: hablo claro, espero mi turno, respeto lo que dicen.",
        "Me parece que hay que cuidar las abejas porque ayudan a que haya frutas.",
        ["opina con «Me parece que... porque...»", "la razón se apoya en el guion", "escucha con respeto a otra persona"],
        ["opinión oral", "opinión escrita"],
        ["opinión sin razón", "burlarse de otro"],
        "Pregunta a otra persona qué pensó y comenta con respeto lo que dijo.",
    ),
    "Di tu opinión sobre cuidar el agua con una razón.",
    "Pregunta a dos familiares su opinión sobre cuidar el agua y compara las razones.",
)
