"""Student material for 4.º básico Matemática, OA 25 (encuestas, muestras aleatorias, tablas y gráficos)."""
from __future__ import annotations

from collections import Counter

from student_lessons import arith, ex, register

OA25 = "MA04 OA 25"

# Población ficticia de 20 estudiantes numerados, con su mascota favorita.
MASCOTA = {1: "perro", 2: "gato", 3: "perro", 4: "pez", 5: "perro", 6: "gato", 7: "perro", 8: "ave", 9: "gato", 10: "perro",
           11: "pez", 12: "perro", 13: "gato", 14: "perro", 15: "ave", 16: "perro", 17: "gato", 18: "pez", 19: "perro", 20: "gato"}
LISTA = ", ".join(f"{n} {m}" for n, m in MASCOTA.items())
CURSO = f"Lista de un curso de 20 estudiantes con su mascota favorita (número y mascota): {LISTA}."


def cnt(nums):
    return Counter(MASCOTA[n] for n in nums)


S_A = [3, 8, 9, 12, 17]
S_B = [1, 4, 5, 10, 14, 16, 19, 6, 11, 15]
S_C = [2, 6, 9, 13, 17]
POB = cnt(MASCOTA)
assert POB == {"perro": 9, "gato": 6, "pez": 3, "ave": 2}
assert cnt(S_A) == {"perro": 2, "gato": 2, "ave": 1}
assert cnt(S_B) == {"perro": 6, "pez": 2, "gato": 1, "ave": 1}
assert cnt(S_C) == {"gato": 5}
SA = cnt(S_A)
SB = cnt(S_B)
DATOS10 = ["gato", "perro", "perro", "pez", "gato", "perro", "ave", "perro", "gato", "perro"]
D10 = Counter(DATOS10)
assert D10 == {"perro": 5, "gato": 3, "pez": 1, "ave": 1}


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


register(
    OA25, 1,
    materials="Lápiz y papel. Las preguntas y las categorías para practicar están escritas en cada ejercicio.",
    use="Aprenderé a escribir una buena pregunta de encuesta y sus categorías de respuesta. Sirve para recoger datos que se puedan contar sin confusión.",
    prior=["Sé qué es una tabla de conteo.", "Sé leer un gráfico de barras sencillo."],
    explain=[
        "Una encuesta es una forma de reunir datos haciendo la misma pregunta a varias personas. Una buena pregunta es clara y cada persona puede contestarla con una sola respuesta. Por ejemplo: «¿Cuál es tu mascota favorita?».",
        "Las categorías son las respuestas posibles que ofreces. Deben ser distintas entre sí, de modo que una respuesta no caiga en dos categorías, y deben alcanzar para todas las personas. Por eso se agrega una categoría «otra».",
        "Si una categoría incluye a otra, como «deportes con pelota» y «fútbol», se mezclan y no se puede contar bien. Antes de preguntar, revisa que la pregunta tenga una sola idea, que las categorías no se mezclen y que ninguna persona se quede sin opción.",
    ],
    vocab=[("encuesta", "preguntas que se hacen a varias personas para reunir datos"), ("categoría", "una de las respuestas posibles de una pregunta"), ("dato", "respuesta que se anota de una persona"), ("pregunta cerrada", "pregunta con respuestas posibles ya escritas")],
    worked=[
        {"title": "Revisar las categorías", "problem": "Pregunta: «¿Cuál es tu mascota favorita?». Categorías: perro, gato, pez y ave. Una niña quiere a su conejo. ¿Qué falta?", "steps": ["Su respuesta no cabe en ninguna categoría.", "Agrego una categoría para las demás: otra."], "answer": "Falta la categoría «otra»"},
        {"title": "Categorías que se mezclan", "problem": "Categorías para «deporte favorito»: fútbol, deportes con pelota y natación. ¿Qué problema tienen?", "steps": ["El fútbol es un deporte con pelota.", "Una persona que elige fútbol cabe en dos categorías."], "answer": "Se mezclan; hay que cambiar «deportes con pelota» por otra categoría separada, como básquetbol"},
    ],
    mistakes=[
        {"wrong": "Hacer una pregunta con dos ideas, como «¿Te gusta el fútbol y el cine?».", "why": "Una persona puede responder distinto a cada idea.", "fix": "Haz una sola idea por pregunta."},
        {"wrong": "Dar categorías que se pisan, como «fruta» y «manzana».", "why": "Una respuesta cabe en las dos.", "fix": "Elige categorías que no se incluyan entre sí."},
    ],
    tiers={
        "recovery": [
            ex("¿Una encuesta pregunta lo mismo a varias personas para reunir datos o dibujos?", "Datos", "Las respuestas se anotan como datos."),
            ex("En «¿Cuál es tu color favorito?», ¿«rojo» es una categoría o una pregunta?", "Una categoría", "Es una de las respuestas posibles."),
            ex("¿Qué categoría conviene agregar para que nadie se quede sin opción?", "Otra", "Recoge las respuestas que no están en la lista."),
        ],
        "understand": [
            ex("¿Cuál es una buena pregunta de encuesta: «¿Qué fruta prefieres: manzana, plátano, naranja u otra?» o «¿Qué opinas de todo?»?", "La de la fruta", "Es clara, tiene una sola idea y categorías definidas."),
            ex("Categorías: «fútbol», «deportes con pelota» y «natación». ¿Cuáles dos se mezclan?", "Fútbol y deportes con pelota", "El fútbol es un deporte con pelota."),
            ex("En «¿Qué mascota prefieres: perro o gato?», una niña prefiere los peces. ¿Qué problema hay?", "Falta una categoría para su respuesta", "Las categorías no cubren a todas las personas."),
        ],
        "apply": [
            ex("Una encuesta de color favorito ofrece las categorías rojo, azul y verde. Si se agrega «otro», ¿cuántas categorías tiene en total?", "4", "Tres colores más «otro» son cuatro categorías.", calc="3+1"),
            ex("En una encuesta de comida favorita las categorías son pizza, fideos y ensalada. Un niño prefiere el pollo. ¿Qué cambio resuelve el problema?", "Agregar la categoría «otra»", "Así hay lugar para su respuesta."),
            ex("La pregunta es «¿Te gusta el recreo y la clase de arte?». ¿Cómo la corriges para que tenga una sola idea?", "Preguntar «¿Qué prefieres: recreo o clase de arte?»", "Se deja una sola idea con categorías claras."),
        ],
        "reason": [
            ex("Rosa dice que «fruta» y «manzana» sirven como categorías para «comida favorita». ¿Tiene razón? Explica.", "No; una manzana es una fruta y la respuesta cabe en las dos", "Las categorías se mezclan."),
            ex("¿Por qué no sirve la pregunta «¿Qué piensas del colegio?» para contar respuestas en una tabla?", "Porque las respuestas pueden ser muy distintas y no hay categorías", "No se pueden agrupar respuestas libres con facilidad."),
        ],
        "challenge": [
            ex("Pregunta: «¿Cómo vienes al colegio?». Categorías: a pie, en bus, en auto. Un niño viene en bicicleta y una niña viene en bus y a pie. ¿Qué dos problemas hay?", "Falta una categoría para la bicicleta y a una persona le caben dos categorías", "Falta «otra» o «bicicleta», y hay que pedir una sola forma principal."),
            ex("Hay 24 estudiantes y las categorías de una encuesta son 4. Si cada estudiante responde una vez, ¿cuántas respuestas se anotan en total?", "24", "Cada estudiante da una respuesta."),
        ],
    },
    context=[ex("Un curso quiere saber qué jugar en el recreo. Pregunta: «¿Qué juego prefieres en el recreo?». Categorías: pelota, cuerda, conversar y otro. ¿Cuántas categorías ofrece?", "4", "Son cuatro respuestas posibles.")],
    selfcheck=[
        ex("¿Qué debe tener una buena pregunta de encuesta: una idea o dos ideas?", "Una idea", "Así cada persona da una sola respuesta."),
        ex("¿Se pueden usar «animal» y «perro» como categorías de una misma pregunta?", "No", "Perro es un animal y se mezclan."),
        ex("¿Para qué sirve la categoría «otra»?", "Para que nadie se quede sin opción", "Recoge las respuestas que no están en las categorías."),
    ],
    open_task=task(
        "Elige un tema: mascota favorita, juego del recreo o fruta favorita. Escribe una pregunta cerrada con una sola idea y cuatro categorías que no se mezclen; una de ellas debe ser «otra». Revisa tu trabajo con la lista de control: una idea, categorías separadas y nadie sin opción.",
        "Tema fruta: «¿Cuál es tu fruta favorita?». Categorías: manzana, plátano, naranja, otra.",
        ["elige un tema de la lista", "escribe una pregunta con una sola idea", "escribe cuatro categorías separadas", "incluye «otra»"],
        ["pregunta", "cuatro categorías"],
        ["categorías que se mezclan", "olvidar «otra»"],
        "Pide leer la pregunta a otra persona para ver si entiende. Reconoce la revisión con la lista.",
    ),
    reinforce="Pregunta a tres personas de tu casa su fruta favorita con categorías cerradas y anota sus respuestas.",
    extend="Elige una pregunta con categorías que se mezclan y corrígela. Explica qué cambiaste.",
)

register(
    OA25, 2,
    materials="Lápiz y papel. La lista del curso está escrita en cada ejercicio.",
    use="Aprenderé a distinguir la población, que es todo el grupo, de la muestra, que es una parte. Sirve para saber a cuántas personas hay que preguntar.",
    prior=["Sé hacer una pregunta con categorías.", "Sé contar y restar números hasta 100."],
    explain=[
        "La población es todo el grupo sobre el que quieres saber algo. Por ejemplo, los 25 estudiantes de un curso. La muestra es una parte de ese grupo a la que sí le haces la pregunta.",
        "La muestra siempre es más pequeña que la población, o igual si preguntas a todos. Preguntar a todos puede tardar mucho. Por eso muchas veces se pregunta a una muestra y se usa su resultado para tener una idea del grupo.",
        "Si el grupo tiene 25 estudiantes y preguntas a 5, la población es 25 y la muestra es 5. Quedan 25 − 5 = 20 sin preguntar. Las personas de la muestra deben salir de la población: no puedes preguntar a otro curso si quieres saber del tuyo.",
    ],
    vocab=[("población", "todo el grupo del que se quiere saber algo"), ("muestra", "parte de la población a la que sí se pregunta"), ("tamaño de la muestra", "cantidad de personas en la muestra"), ("representar", "parecerse al grupo completo")],
    worked=[
        {"title": "Identificar población y muestra", "problem": "En un curso de 30 estudiantes se pregunta su deporte favorito a 6 de ellos. ¿Cuál es la población y cuál la muestra?", "steps": ["La población es todo el curso: 30.", "La muestra son los que se preguntaron: 6."], "answer": "Población: 30 estudiantes; muestra: 6 estudiantes"},
        {"title": "Quiénes quedan fuera", "problem": "Con 30 estudiantes y una muestra de 6, ¿cuántos no fueron preguntados?", "steps": ["Resto la muestra a la población.", "30 − 6 = 24."], "answer": "24 estudiantes"},
    ],
    mistakes=[
        {"wrong": "Decir que la muestra es todo el curso.", "why": "Se confunde la muestra con la población.", "fix": "La muestra es solo la parte que se pregunta."},
        {"wrong": "Preguntar a otro curso para saber algo de mi curso.", "why": "La muestra no sale de la población que interesa.", "fix": "La muestra debe salir de los estudiantes de tu curso."},
    ],
    tiers={
        "recovery": [
            ex("En un curso de 24 estudiantes se pregunta a 4. ¿Cuántos estudiantes tiene la población?", "24", "La población es todo el grupo."),
            ex("En ese mismo curso, ¿cuántos estudiantes tiene la muestra?", "4", "La muestra son los que se preguntan."),
            ex("¿La muestra es todo el grupo o una parte del grupo?", "Una parte del grupo", "La muestra es una parte de la población."),
        ],
        "understand": [
            arith("En un curso de 28 estudiantes se pregunta a 7. ¿Cuántos no fueron preguntados?", "28-7", "Se resta la muestra a la población.", " estudiantes"),
            ex("Quieres saber el postre favorito de tu curso y preguntas a 5 estudiantes de otro curso. ¿Es una muestra de tu curso? Explica.", "No; no salen de tu curso", "La muestra debe salir de la población de interés."),
            ex("Si se pregunta a todos los estudiantes del curso, ¿qué tamaño tiene la muestra comparada con la población?", "Es igual", "Se pregunta a todo el grupo."),
        ],
        "apply": [
            ex("La población son los 40 estudiantes de dos cursos. Se pregunta a 10. ¿Qué tamaño tiene la muestra?", "10", "La muestra es la parte que se pregunta."),
            arith("En una escuela de 120 estudiantes se pregunta a 20. ¿Cuántos quedaron sin preguntar?", "120-20", "Se resta la muestra a la población.", " estudiantes"),
            ex("Quieres conocer el cuento favorito de los 18 estudiantes de tu curso. Preguntas a 6 de ellos. Escribe: población, muestra.", "Población: 18; muestra: 6", "18 es todo el grupo y 6 los preguntados."),
        ],
        "reason": [
            ex("Pablo dice que la muestra puede ser más grande que la población. ¿Tiene razón?", "No; la muestra es una parte de la población", "No se puede preguntar a más personas de las que hay en el grupo."),
            ex("Para saber el juego favorito del curso, Ema pregunta a sus 3 mejores amigos. ¿Qué problema puede tener esa muestra?", "Los amigos pueden parecerse entre sí y no representar a todo el curso", "La muestra puede ser poco variada."),
        ],
        "challenge": [
            ex("Un curso tiene 32 estudiantes. Si la muestra tiene 8, ¿cuántos estudiantes de la población no están en la muestra?", "24", "32 − 8 = 24.", calc="32-8"),
            ex("En una población de 20 estudiantes, ¿cuántos estudiantes puede tener como máximo una muestra?", "20", "Como máximo se pregunta a todos."),
        ],
    },
    context=[ex("Un colegio de 150 estudiantes quiere saber qué actividad prefieren y encuesta a 25. ¿Cuántos estudiantes no fueron encuestados?", "125", "150 − 25 = 125.", calc="150-25")],
    selfcheck=[
        ex("¿Cómo se llama todo el grupo sobre el que quieres saber algo?", "Población", "Es todo el grupo."),
        ex("¿Cómo se llama la parte del grupo a la que preguntas?", "Muestra", "Es la parte que se encuesta."),
        ex("Un curso de 26 estudiantes y una muestra de 6. ¿Cuántos no fueron preguntados?", "20", "26 − 6 = 20.", calc="26-6"),
    ],
    open_task=task(
        "Elige un grupo: los 30 estudiantes de tu curso, las 12 personas de una fiesta o los 20 vecinos de una cuadra. Escribe la población, inventa un tamaño razonable para una muestra menor que la población y calcula cuántas personas quedan sin preguntar.",
        "Curso de 30 estudiantes. Muestra de 6. Quedan 30 − 6 = 24 sin preguntar.",
        ["elige un grupo de la lista", "escribe la población", "propone una muestra menor que la población", "calcula quiénes quedan sin preguntar"],
        ["población y muestra", "resta"],
        ["muestra mayor que la población", "restar mal"],
        "Pide explicar la diferencia entre población y muestra con sus palabras. Reconoce la resta correcta.",
    ),
    reinforce="Escribe cuántas personas viven en tu cuadra o tu edificio, si sabes, y piensa a cuántas preguntarías para saber su color favorito.",
    extend="Explica por qué a veces conviene preguntar a una muestra y no a toda la población.",
)

register(
    OA25, 3,
    materials="Papelitos numerados (si tienes) o la lista escrita en cada ejercicio. La lista del curso trae las mascotas favoritas.",
    use="Aprenderé a elegir una muestra aleatoria, es decir, al azar. Sirve para que todas las personas tengan la misma oportunidad de ser elegidas.",
    prior=["Sé qué es población y muestra.", "Sé leer una lista con números."],
    explain=[
        "Una muestra aleatoria es la que se elige al azar. Cada persona de la población tiene la misma oportunidad de ser elegida. Así la muestra no favorece a ningún grupo.",
        "Para elegirla, puedes numerar a los estudiantes, escribir los números en papelitos, revolverlos en una bolsa y sacar algunos sin mirar. Los números que salen indican quiénes forman la muestra, y no se cambia ninguno.",
        "No es aleatorio preguntar solo a quienes están cerca, a tus amigos o a los que levantan la mano. Esa muestra puede quedar con personas parecidas y dar un resultado engañoso.",
    ],
    vocab=[("aleatorio", "elegido al azar, sin escoger a propósito"), ("azar", "lo que ocurre sin poder decidirlo"), ("papelito numerado", "papel con un número que representa a una persona"), ("sesgo", "inclinación que hace que la muestra no se parezca al grupo")],
    worked=[
        {"title": "Elegir al azar", "problem": CURSO + " Se sacan los papelitos 3, 8, 9, 12 y 17. ¿Qué mascotas favoritas hay en esa muestra?", "steps": ["Busco cada número en la lista: 3 perro, 8 ave, 9 gato, 12 perro y 17 gato.", f"Cuento: perro {SA['perro']}, gato {SA['gato']}, ave {SA['ave']}."], "answer": f"Perro {SA['perro']}, gato {SA['gato']}, ave {SA['ave']} y pez 0"},
        {"title": "Detectar una muestra que no es aleatoria", "problem": "Para elegir a 5 estudiantes, la profesora llama a los primeros 5 que levantan la mano. ¿Es una muestra aleatoria?", "steps": ["No todos tienen la misma oportunidad.", "Los que no levantan la mano casi no pueden salir."], "answer": "No es aleatoria"},
    ],
    mistakes=[
        {"wrong": "Elegir solo a los amigos y llamarlo muestra aleatoria.", "why": "Se escoge a propósito y no al azar.", "fix": "Saca papelitos numerados sin mirar."},
        {"wrong": "Sacar un papelito, mirarlo y dejar el que no gusta.", "why": "Se decide en vez de dejar actuar al azar.", "fix": "Acepta el número que sale."},
    ],
    tiers={
        "recovery": [
            ex("¿Una muestra aleatoria se elige al azar o a propósito?", "Al azar", "Aleatorio significa al azar."),
            ex("En una muestra aleatoria, ¿todas las personas tienen la misma oportunidad de salir?", "Sí", "Ese es el sentido de elegir al azar."),
            ex("¿Es aleatorio elegir a tus 5 amigos para preguntarles?", "No", "Se escoge a propósito."),
        ],
        "understand": [
            ex("¿Qué sirve para elegir al azar: sacar papelitos numerados sin mirar o llamar a quienes levantan la mano?", "Sacar papelitos numerados sin mirar", "Cada número tiene la misma oportunidad."),
            ex(CURSO + " Salen los papelitos 2, 4 y 6. ¿Qué mascotas favoritas tienen esos estudiantes, en orden?", "Gato, pez, gato", "2 gato, 4 pez y 6 gato."),
            ex("¿Por qué no es aleatorio elegir a los 5 estudiantes que se sientan adelante?", "Porque los de atrás casi no tienen oportunidad de salir", "No todos tienen la misma oportunidad."),
        ],
        "apply": [
            ex(CURSO + " Se sacan los papelitos 3, 8, 9, 12 y 17. ¿Cuántos de la muestra prefieren perro?", str(SA["perro"]), "Los números 3 y 12 son perro."),
            ex(CURSO + " La muestra son los números 1, 4, 5, 10, 14, 16, 19, 6, 11 y 15. ¿Cuántos prefieren perro?", str(SB["perro"]), "Son los números 1, 5, 10, 14, 16 y 19."),
            ex(CURSO + " Salen los papelitos 2, 6, 9, 13 y 17. ¿Cuántos de los 5 prefieren gato?", "5", "Los 5 números corresponden a gato."),
        ],
        "reason": [
            ex("Luis saca un papelito, ve que sale un compañero que le cae mal y lo cambia por otro. ¿Es aleatoria su muestra? Explica.", "No; eligió a propósito", "Al cambiarlo, deja de ser al azar."),
            ex("Dos muestras aleatorias de 5 del mismo curso pueden dar resultados distintos. ¿Por qué?", "Porque salen estudiantes distintos al azar", "Cada sorteo puede elegir personas diferentes."),
        ],
        "challenge": [
            ex(CURSO + " Se sacan los papelitos 3, 8, 9, 12 y 17. En esa muestra, ¿perro es la única mascota con más votos? Responde sí o no y explica.", "No; perro y gato empatan con 2 votos cada uno", "En la muestra hay 2 perros, 2 gatos y 1 ave: perro y gato empatan."),
            ex("Una muestra aleatoria de 5 estudiantes se hace con papelitos del 1 al 20. ¿Puede salir dos veces el mismo número si el papelito no se vuelve a la bolsa?", "No", "Cada papelito se saca una sola vez."),
        ],
    },
    context=[ex("En tu curso de 20 estudiantes, la lista de mascotas está numerada del 1 al 20. Se sortean los números 15, 2, 18, 7 y 11. ¿Cuántos estudiantes de la muestra prefieren pez?", "2", "Los números 18 y 11 son pez.")],
    selfcheck=[
        ex("¿Qué significa aleatorio?", "Elegido al azar", "No se escoge a propósito."),
        ex("¿Se puede elegir al azar numerando papelitos y sacándolos sin mirar?", "Sí", "Todos los números tienen la misma oportunidad."),
        ex(CURSO + " ¿Qué mascota tiene el estudiante número 13?", "Gato", "En la lista, 13 gato."),
    ],
    open_task=task(
        CURSO + " Escribe los números del 1 al 20 en papelitos (o en tarjetas), revuélvelos y saca 5. Si no tienes papel, usa este sorteo: 4, 9, 13, 16, 20. Anota la mascota favorita de cada número y cuenta cuántas veces sale cada una.",
        "Sorteo 4, 9, 13, 16, 20: pez, gato, gato, perro, gato. Gato 3, perro 1, pez 1.",
        ["usa papelitos numerados o el sorteo dado", "anota la mascota de cada número", "cuenta cada mascota", "no cambia ningún número que salió"],
        ["lista de mascotas por número", "conteo"],
        ["elegir a propósito", "contar mal"],
        "Pide explicar por qué el sorteo es al azar. Reconoce que acepte los números que salen.",
    ),
    reinforce="Escribe los números del 1 al 10 en papelitos y saca 3 sin mirar. Anota cuáles salieron.",
    extend="Explica por qué una muestra aleatoria puede ser distinta del grupo aunque se haya elegido bien.",
)

register(
    OA25, 4,
    materials="Lápiz y papel. Los datos están escritos en el enunciado; con papel cuadriculado puedes dibujar el gráfico.",
    use="Aprenderé a pasar una lista de respuestas a una tabla de conteo y a un gráfico de barras. Sirve para ver rápido cuál respuesta es más frecuente.",
    prior=["Sé contar con marcas de conteo.", "Sé leer un gráfico de barras sencillo."],
    explain=[
        "Los datos de una encuesta, al principio, son una lista desordenada. Para entenderlos, se ordenan en una tabla de conteo: se anota cada categoría y cuántas veces apareció. Ese número se llama frecuencia.",
        "Para contar sin equivocarte, recorre la lista una vez y marca cada respuesta. Después comprueba que la suma de todas las frecuencias sea igual al total de respuestas. Si no coincide, algo se contó mal o se olvidó.",
        "Con la tabla puedes dibujar un gráfico de barras. En el eje horizontal escribes las categorías y en el vertical una escala de números. La altura de cada barra es la frecuencia. Pon un título y nombre a los ejes.",
    ],
    vocab=[("frecuencia", "cantidad de veces que aparece una categoría"), ("tabla de conteo", "tabla que anota cada categoría y su frecuencia"), ("gráfico de barras", "gráfico donde la altura de cada barra es una frecuencia"), ("escala", "números del eje que dicen cuánto vale cada marca")],
    worked=[
        {"title": "De la lista a la tabla", "problem": "Respuestas de 10 estudiantes sobre su mascota favorita: " + ", ".join(DATOS10) + ". Haz la tabla de conteo.", "steps": ["Cuento cada mascota recorriendo la lista una vez.", f"Resulta: perro {D10['perro']}, gato {D10['gato']}, pez {D10['pez']}, ave {D10['ave']}."], "answer": f"Perro {D10['perro']}, gato {D10['gato']}, pez {D10['pez']}, ave {D10['ave']}, y suman 10"},
        {"title": "De la tabla al gráfico", "problem": f"Con esa tabla, ¿cómo es la barra de perro en un gráfico con escala de 1 en 1?", "steps": ["La altura de la barra es la frecuencia.", f"La barra de perro sube hasta {D10['perro']}."], "answer": f"Llega hasta {D10['perro']}, la más alta"},
    ],
    mistakes=[
        {"wrong": "Contar sin comprobar que la suma dé el total de respuestas.", "why": "Se pueden contar mal o saltar una respuesta.", "fix": "Suma las frecuencias y compara con el total."},
        {"wrong": "Dibujar barras sin escala ni título.", "why": "Nadie sabe qué muestran las barras.", "fix": "Agrega título, nombre de los ejes y escala."},
    ],
    tiers={
        "recovery": [
            ex("Una tabla de conteo anota cada categoría y su ¿qué?", "Frecuencia", "La frecuencia es cuántas veces aparece."),
            ex("Respuestas: " + ", ".join(DATOS10) + ". ¿Cuántas veces aparece «pez»?", str(D10["pez"]), "Hay un solo «pez»."),
            ex("En un gráfico de barras, ¿qué indica la altura de cada barra?", "La frecuencia", "Más alta significa más repeticiones."),
        ],
        "understand": [
            ex("Respuestas: " + ", ".join(DATOS10) + ". ¿Cuántas veces aparece «perro»?", str(D10["perro"]), "Se cuentan cinco «perro» en la lista."),
            ex("Una tabla suma 4 + 3 + 2 + 2 = 11, pero había 12 respuestas. ¿Qué indica?", "Que se contó mal o se olvidó una respuesta", "La suma debe ser igual al total."),
            ex("¿Qué dos cosas no deben faltar en un gráfico de barras además de las barras?", "Título y escala (o nombres de los ejes)", "Sin ellos no se entiende qué muestra."),
        ],
        "apply": [
            ex("Respuestas: rojo, azul, rojo, verde, azul, rojo, rojo, azul. Haz la tabla: ¿cuántos hay de rojo, azul y verde, en ese orden?", "4, 3, 1", "Rojo aparece 4 veces, azul 3 y verde 1."),
            arith("Una tabla tiene frecuencias 6, 4, 3 y 2. ¿Cuántas respuestas se anotaron en total?", "6+4+3+2", "Se suman todas las frecuencias.", " respuestas"),
            ex("En un gráfico con escala de 2 en 2, una barra llega a la marca 6. ¿Cuál es la frecuencia?", "6", "La altura de la barra es la frecuencia."),
        ],
        "reason": [
            ex("Beto dibuja las barras de perro (5), gato (3) y pez (1) del mismo alto. ¿Qué error comete?", "Las alturas no respetan las frecuencias", "La altura debe ser proporcional a cada frecuencia."),
            ex("Ema dice que si la suma de frecuencias es menor al total de respuestas, la tabla está bien. ¿Tiene razón?", "No; faltan respuestas por contar", "Debe sumar el total."),
        ],
        "challenge": [
            ex("Respuestas de 12 estudiantes: gato, perro, perro, gato, perro, ave, gato, perro, gato, gato, perro, ave. ¿Cuántos gatos hay?", "5", "Se cuentan cinco «gato» en la lista."),
            ex("Con las mismas 12 respuestas, ¿cuántos perros hay y cuántas aves?", "5 perros y 2 aves", "Perro aparece 5 veces y ave 2; con 5 gatos suman 12."),
        ],
    },
    context=[ex("En un curso se preguntó el deporte favorito de 9 estudiantes y se obtuvo: fútbol 4, natación 3 y básquetbol 2. ¿Suman las frecuencias el total de estudiantes?", "Sí, 4 + 3 + 2 = 9", "4 + 3 + 2 es igual a 9.", calc="4+3+2")],
    selfcheck=[
        ex("¿Cuántas veces se repite la mascota más frecuente de esta lista: " + ", ".join(DATOS10) + "?", "5", "«Perro» aparece 5 veces."),
        ex("¿Qué dice la altura de una barra?", "La frecuencia de esa categoría", "Es cuántas veces aparece."),
        ex("Una tabla tiene frecuencias 3, 3 y 4. ¿Cuántas respuestas hay?", "10", "3 + 3 + 4 = 10.", calc="3+3+4"),
    ],
    open_task=task(
        "Con esta lista de 12 respuestas de color favorito: azul, rojo, azul, verde, amarillo, azul, rojo, azul, verde, rojo, azul, amarillo. Haz una tabla de conteo y dibuja o describe un gráfico de barras con título, escala y nombres de ejes. Comprueba que la suma de frecuencias dé 12.",
        "Azul 5, rojo 3, verde 2, amarillo 2. Total 12.",
        ["cuenta cada categoría", "comprueba que la suma dé 12", "pone título y escala al gráfico", "la altura de las barras coincide con la tabla"],
        ["tabla de conteo", "gráfico con título y escala"],
        ["no comprobar el total", "olvidar título o escala"],
        "Pide mostrar la suma de frecuencias. Reconoce que el gráfico coincida con la tabla.",
    ),
    reinforce="Pregunta el color favorito a 8 personas de tu casa o familiares y haz una tabla de conteo.",
    extend="Explica por qué conviene comprobar que la suma de las frecuencias dé el total de la muestra.",
)

register(
    OA25, 5,
    materials="Lápiz y papel. Los datos de la población y de las muestras están escritos en los ejercicios.",
    use="Aprenderé a comparar el resultado de una muestra con el de toda la población y a decir qué se puede y qué no se puede concluir. Sirve para no sacar conclusiones apuradas.",
    prior=["Sé hacer tablas de conteo.", "Sé qué es una muestra aleatoria."],
    explain=[
        "Cuando preguntas a una muestra, su resultado se parece a veces al de la población, pero no siempre. Si comparas los dos, puedes ver qué tanto se parecen. Una muestra pequeña puede dar un resultado muy distinto.",
        "Por ejemplo, en un curso de 20 estudiantes, 9 prefieren perro. Una muestra de 5 estudiantes puede dar 2 que prefieren perro. No es igual, pero ayuda a ver que perro es una de las mascotas más nombradas. Para comparar bien, usa el mismo tipo de dato: cuenta cuántos de cada categoría hay.",
        "Una muestra grande suele parecerse más a la población, pero no hay seguridad. Por eso hay que decir «en esta muestra» y no «en todo el curso» cuando solo se preguntó a una parte. Una conclusión debe decir qué datos la sostienen y qué límites tiene.",
    ],
    vocab=[("comparar", "ver qué se parece y qué es distinto entre dos resultados"), ("conclusión", "frase que dice lo que muestran los datos"), ("límite", "lo que los datos no permiten asegurar"), ("estimar", "dar una idea aproximada de la población usando una muestra")],
    worked=[
        {"title": "Comparar una muestra con la población", "problem": CURSO + f" En toda la lista hay {POB['perro']} que prefieren perro. En la muestra 3, 8, 9, 12, 17 hay {SA['perro']}. ¿Cuál es la mascota con más votos en la población?", "steps": [f"En la población: perro {POB['perro']}, gato {POB['gato']}, pez {POB['pez']}, ave {POB['ave']}.", "El número más alto es el de perro."], "answer": "Perro, con 9 votos"},
        {"title": "Decir la conclusión con límites", "problem": f"En la muestra 3, 8, 9, 12, 17, perro y gato tienen {SA['perro']} cada uno. ¿Se puede afirmar que a todo el curso le gustan igual?", "steps": ["La muestra tiene solo 5 estudiantes.", "En toda la población, perro tiene 9 y gato 6, así que son distintos."], "answer": "No; la muestra no basta para afirmar eso del curso"},
    ],
    mistakes=[
        {"wrong": "Decir que lo que salió en la muestra es exactamente lo que pasa en todo el curso.", "why": "La muestra es solo una parte.", "fix": "Di «en esta muestra» y compara con la población si la tienes."},
        {"wrong": "Concluir con una muestra muy pequeña como si fuera segura.", "why": "Un grupo pequeño puede parecer distinto del total.", "fix": "Indica que hay incertidumbre y usa más datos si puedes."},
    ],
    tiers={
        "recovery": [
            ex(CURSO + " En toda la población, ¿cuántos prefieren perro?", str(POB["perro"]), "Se cuentan los números 1, 3, 5, 7, 10, 12, 14, 16 y 19."),
            ex(CURSO + " En toda la población, ¿cuántos prefieren pez?", str(POB["pez"]), "Son los números 4, 11 y 18."),
            ex(CURSO + " En toda la población, ¿cuántos prefieren gato?", str(POB["gato"]), "Son los números 2, 6, 9, 13, 17 y 20."),
        ],
        "understand": [
            ex(CURSO + " En toda la población, ¿qué mascota tiene menos votos?", "Ave", "Ave tiene 2 votos, la cantidad más baja."),
            ex(CURSO + f" En la muestra 3, 8, 9, 12, 17, ¿cuántos prefieren gato?", str(SA["gato"]), "Los números 9 y 17 son gato."),
            ex(f"En una muestra de 5, perro y gato empatan con {SA['perro']}. ¿Se puede decir que en todo el curso empatan?", "No", "Una muestra pequeña puede no representar al grupo."),
        ],
        "apply": [
            ex(CURSO + f" La muestra es 1, 4, 5, 10, 14, 16, 19, 6, 11, 15. ¿Qué mascota tiene más votos en esa muestra?", "Perro", f"Perro tiene {SB['perro']} votos en la muestra."),
            ex(CURSO + " La muestra es 1, 4, 5, 10, 14, 16, 19, 6, 11, 15. ¿La mascota más votada en esa muestra es la misma que en toda la población?", "Sí, perro", "Perro lidera tanto en la muestra como en la población."),
            ex(CURSO + f" En la muestra 1, 4, 5, 10, 14, 16, 19, 6, 11, 15, ¿cuántos prefieren pez?", str(SB["pez"]), "Los números 4 y 11 son pez."),
        ],
        "reason": [
            ex(CURSO + " En la muestra 2, 6, 9, 13, 17 los 5 prefieren gato. ¿Se puede concluir que todos los del curso prefieren gato? Explica con la población.", "No; en el curso solo 6 de 20 prefieren gato", "La muestra no se parece a la población."),
            ex("Pablo concluye algo de todo un colegio preguntando a 3 estudiantes. ¿Qué límite tiene su conclusión?", "Tres estudiantes son muy pocos para asegurar algo del colegio", "Una muestra muy pequeña puede no representar."),
        ],
        "challenge": [
            ex(f"La muestra de 5 dio empate entre perro y gato; la de 10 dio a perro como ganador claro. En la población, perro gana con {POB['perro']} de 20. ¿Cuál de las dos muestras coincide mejor con la población?", "La muestra de 10", "En la población y en la muestra de 10 gana perro con claridad."),
            ex("¿Una conclusión correcta de una muestra empieza con «En esta muestra…» o con «En todo el curso…»?", "«En esta muestra…»", "Solo se preguntó a una parte."),
        ],
    },
    context=[ex("Una profesora sortea 5 papelitos del curso de 20 y pregunta la mascota favorita: sale 3 perros, 1 gato y 1 ave. Ella escribe «Perro es la favorita del curso». ¿Qué debería agregar a su conclusión para ser prudente?", "Que se basa solo en una muestra de 5 estudiantes", "La muestra es una parte pequeña de la población.")],
    selfcheck=[
        ex("¿Puede una muestra dar un resultado distinto del de la población?", "Sí", "Es solo una parte del grupo."),
        ex("¿Qué frase es más prudente: «En esta muestra ganó el perro» o «Todo el curso prefiere perro»?", "«En esta muestra ganó el perro»", "Solo habla de lo que se preguntó."),
        ex(CURSO + " En la población, ¿perro tiene más o menos votos que gato?", "Más", f"Perro tiene {POB['perro']} y gato {POB['gato']}."),
    ],
    open_task=task(
        CURSO + " Compara estas dos muestras: la muestra pequeña 3, 8, 9, 12, 17 y la muestra grande 1, 4, 5, 10, 14, 16, 19, 6, 11, 15. Haz una tabla de conteo para cada una, compárala con la población y escribe una conclusión con sus límites (una frase que empiece con «En esta muestra…»).",
        "Muestra pequeña: perro 2, gato 2, ave 1. Muestra grande: perro 6, pez 2, gato 1, ave 1. En la población perro es la más votada. En esta muestra pequeña perro y gato empatan, así que no alcanza para saber cuál gana en todo el curso.",
        ["hace las dos tablas de conteo", "compara con la población", "escribe una conclusión con límites", "usa «en esta muestra»"],
        ["dos tablas", "comparación", "conclusión con límites"],
        ["concluir de más", "contar mal"],
        "Pide revisar si la conclusión dice la fuente de los datos. Reconoce el uso de los límites.",
    ),
    reinforce="Lee en voz alta una conclusión que escribiste hoy y revisa si dice de qué grupo habla.",
    extend="Explica por qué dos muestras aleatorias del mismo curso pueden dar resultados distintos.",
)
