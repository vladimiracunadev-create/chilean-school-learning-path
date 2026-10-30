"""Student material for 2.º básico Matemática, OA 14 (posición, derecha e izquierda, perspectiva y recorridos)."""
from __future__ import annotations

from student_content_ma02_f import task
from student_lessons import ex, register

OA14 = "MA02 OA 14"

GRID = "Cuadrícula con columnas A, B, C y D (de izquierda a derecha) y filas 1, 2, 3 y 4 (de abajo hacia arriba)."
DIRS = ["arriba", "derecha", "abajo", "izquierda"]  # sentido de las agujas del reloj
STEP = {"arriba": (0, 1), "derecha": (1, 0), "abajo": (0, -1), "izquierda": (-1, 0)}
FACE = {"arriba": "hacia arriba", "derecha": "hacia la derecha del dibujo", "abajo": "hacia abajo", "izquierda": "hacia la izquierda del dibujo"}


def walk(cell: str, facing: str, commands: list) -> tuple[str, str]:
    """Simula un recorrido. commands: ('av', n), ('gd',) giro a la derecha, ('gi',) giro a la izquierda."""
    col, row = "ABCD".index(cell[0]), int(cell[1]) - 1
    for command in commands:
        if command[0] == "av":
            dx, dy = STEP[facing]
            col, row = col + dx * command[1], row + dy * command[1]
            assert 0 <= col <= 3 and 0 <= row <= 3, "el recorrido se sale de la cuadrícula"
        elif command[0] == "gd":
            facing = DIRS[(DIRS.index(facing) + 1) % 4]
        else:
            facing = DIRS[(DIRS.index(facing) - 1) % 4]
    return "ABCD"[col] + str(row + 1), facing


def route(cell: str, facing: str, commands: list, why: str, text: str, with_facing: bool = False) -> dict:
    end, final = walk(cell, facing, commands)
    answer = f"{end}; mira {FACE[final]}" if with_facing else end
    return ex(f"{GRID} {text}", answer, why)


# ------------------------------------------------------------------ OA 14
register(
    OA14, 1,
    materials="Una cinta o un trozo de lana, un vaso, una pelota o un calcetín enrollado, y un adulto que te confirme cuál es tu derecha. Todo lo demás está en los ejercicios.",
    use="Aprenderé a distinguir mi derecha y mi izquierda y a ubicar objetos respecto de mi cuerpo. Sirve para seguir indicaciones y explicar dónde está algo.",
    prior=["Sé decir delante, detrás, arriba y abajo.", "Sé nombrar las partes del cuerpo."],
    explain=[
        "Tu cuerpo tiene un lado derecho y un lado izquierdo. Pídele a un adulto que te diga cuál es tu mano derecha. Ata una cinta en esa muñeca. Así recordarás que ese lado es tu derecha, y el otro lado es tu izquierda.",
        "Tu derecha es la mano, el brazo, la pierna, el pie y la oreja de ese lado. Tu izquierda es lo mismo del otro lado. Si pones un vaso cerca de tu mano con cinta, está a tu derecha. Si pones una pelota cerca de la otra mano, está a tu izquierda.",
        "Tu derecha y tu izquierda van contigo. Si das una vuelta o caminas hacia otro lado, tu mano con cinta sigue siendo la derecha. Lo que cambia es dónde queda el vaso o la pelota respecto de ti, pero no cuál es tu mano derecha.",
    ],
    vocab=[("derecha", "el lado de tu cuerpo donde está la mano con cinta"), ("izquierda", "el otro lado de tu cuerpo"), ("lado", "una de las dos partes del cuerpo, derecha o izquierda"), ("a mi derecha", "al lado de mi mano derecha"), ("a mi izquierda", "al lado de mi mano izquierda")],
    worked=[
        {"title": "Ubicar objetos en mi cuerpo", "problem": "Tienes una cinta en la muñeca derecha. Pones un vaso junto a esa mano y una pelota junto a la otra mano. ¿Qué está a tu derecha y qué está a tu izquierda?", "steps": ["La cinta marca mi derecha.", "El vaso está junto a la mano con cinta: está a mi derecha.", "La pelota está junto a la otra mano: está a mi izquierda.", "Lo digo en voz alta: el vaso está a mi derecha y la pelota a mi izquierda."], "answer": "Vaso a la derecha; pelota a la izquierda"},
        {"title": "La derecha viaja contigo", "problem": "Giras para mirar hacia la pared de atrás. ¿La mano con cinta sigue siendo tu derecha?", "steps": ["La cinta sigue en la misma muñeca.", "Mi cuerpo giró, pero mi muñeca no cambió.", "Mi derecha es la del cuerpo, y no la de la sala.", "Sí, sigue siendo mi derecha."], "answer": "Sí, sigue siendo la derecha"},
    ],
    mistakes=[
        {"wrong": "Pensar que la derecha es un lugar fijo de la sala.", "why": "Se confunde la derecha del cuerpo con un lugar del espacio.", "fix": "Tu derecha es de tu cuerpo y va contigo cuando giras."},
        {"wrong": "Decir izquierda para el vaso junto a la mano con cinta.", "why": "Se mezclan los dos lados.", "fix": "La cinta marca la derecha: lo que está junto a ella está a tu derecha."},
    ],
    tiers={
        "recovery": [
            ex("Tienes una cinta en la muñeca derecha. Pones un vaso junto a esa mano y una pelota junto a la otra. ¿Qué objeto está a tu derecha?", "El vaso", "Está junto a la mano con cinta."),
            ex("Con la cinta en la muñeca derecha, ¿cuál lado es tu izquierda?", "El lado de la mano sin cinta", "El otro lado es el izquierdo."),
            ex("Levantas la mano izquierda. ¿Es la mano con cinta o sin cinta?", "Sin cinta", "La cinta está en la derecha."),
        ],
        "understand": [
            ex("Giras para mirar hacia otra pared. ¿Tu mano derecha sigue siendo la derecha?", "Sí; la derecha es de tu cuerpo", "El giro no cambia tu mano."),
            ex("Tocas tu oreja derecha con tu mano derecha. ¿Qué lado de la cabeza tocas?", "El lado derecho", "La oreja derecha está en el lado derecho."),
            ex("Mueves un vaso desde tu derecha hasta el otro lado de tu cuerpo. ¿A qué lado queda?", "A tu izquierda", "Cambió de lado."),
        ],
        "apply": [
            ex("Estás de pie. A tu derecha hay una silla y a tu izquierda una mesa. ¿Qué hay a tu izquierda?", "Una mesa", "La mesa está del lado izquierdo."),
            ex("Un lápiz está a tu izquierda. Lo pasas al otro lado de tu cuerpo. ¿A qué lado queda?", "A tu derecha", "Cambió de lado."),
            ex("Pones una pelota a tu derecha y un libro a tu izquierda. Levantas el objeto que está a tu derecha. ¿Cuál levantas?", "La pelota", "La pelota está del lado derecho."),
        ],
        "reason": [
            ex("Camila dice que su derecha cambia cuando camina hacia atrás. ¿Tiene razón?", "No; su derecha del cuerpo sigue siendo la misma", "La derecha va con el cuerpo."),
            ex("¿Por qué es útil marcar la mano con una cinta?", "Para recordar cuál es la derecha", "Así no se confunden los lados."),
        ],
        "challenge": [
            ex("Pones tres objetos en fila a tu derecha. Desde el más cercano a ti hasta el más lejano están el vaso, la pelota y el libro. ¿Cuál es el más lejano?", "El libro", "Es el último de la fila, el más alejado de ti."),
            ex("Tocas con tu mano izquierda tu rodilla derecha. ¿Cruzaste el cuerpo?", "Sí; la mano de un lado toca el otro lado", "Mano izquierda y rodilla derecha están en lados opuestos."),
        ],
    },
    context=[ex("En el patio, Luis tiene un banco a su derecha y un árbol a su izquierda. Si Luis quiere sentarse en el banco, ¿hacia qué lado debe girar?", "Hacia su derecha", "El banco está a su derecha.")],
    selfcheck=[ex("¿Con qué mano sostienes la cinta si marca tu derecha?", "Con la mano derecha", "La cinta está en esa muñeca."), ex("Un cuaderno está a tu izquierda. ¿Cerca de qué mano está?", "De la mano izquierda", "Izquierda significa el lado de esa mano."), ex("Si giras, ¿cambia cuál es tu mano derecha?", "No", "La derecha es de tu cuerpo.")],
    open_task=task(
        "Pídele a un adulto que te diga cuál es tu mano derecha y ata la cinta en esa muñeca. Pon un vaso a tu derecha, una pelota a tu izquierda y un libro delante de ti. Dibuja la escena vista desde arriba. Pon un círculo para ti, mirando hacia el borde de arriba de la hoja. Escribe tres frases: «El vaso está a mi ____», «La pelota está a mi ____» y «El libro está ____ de mí».",
        "Dibujo: un círculo (yo) con una cruz a la derecha (vaso), una cruz a la izquierda (pelota) y una cruz delante (libro). Frases: el vaso está a mi derecha, la pelota está a mi izquierda y el libro está delante de mí.",
        ["ata la cinta en la mano derecha", "ubica los tres objetos correctamente", "completa las tres frases con derecha, izquierda y delante"],
        ["dibujo visto desde arriba", "tres frases"],
        ["confundir la derecha con la izquierda", "pensar que la derecha cambia al girar"],
        "Pide que gire y diga de nuevo dónde está cada objeto respecto de su cuerpo; reconoce que usa «a mi derecha» y «a mi izquierda».",
    ),
    reinforce="Camina por tu casa diciendo en voz alta: «La puerta está a mi derecha», «La mesa está a mi izquierda», según donde estés.",
    extend="Juega «Simón dice» con un adulto usando solo las órdenes «toca tu oreja derecha» y «toca tu rodilla izquierda».",
)

register(
    OA14, 2,
    materials="Tres objetos pequeños (lápiz, libro, goma) y una mesa. Los demás objetos están escritos en los ejercicios.",
    use="Aprenderé a decir dónde está un objeto respecto de otro objeto, usando derecha, izquierda, delante, detrás y entre. Sirve para dar indicaciones claras sobre dónde buscar algo.",
    prior=["Sé cuál es mi derecha y mi izquierda.", "Sé que el lugar de un objeto se puede describir con una palabra de posición."],
    explain=[
        "Para decir dónde está un objeto, se usa otro objeto como punto de referencia. Si el lápiz está a la izquierda del libro, el libro es el referente. Miras la fila como si estuvieras de frente a ella, y lo que queda hacia tu izquierda es la izquierda.",
        "Mira esta fila de izquierda a derecha, como tú la ves: lápiz, libro, goma. El lápiz está a la izquierda del libro. La goma está a la derecha del libro. El libro está entre el lápiz y la goma. Si cambias el referente, cambia la frase: el libro está a la derecha del lápiz.",
        "También puedes decir delante y detrás. Lo que está más cerca de ti está delante, y lo que está más lejos está detrás. Una frase completa nombra los dos objetos, por ejemplo: «La goma está a la derecha del libro». Así otra persona puede encontrarla sin ver tu dibujo.",
    ],
    vocab=[("referente", "el objeto desde el cual se describe la posición"), ("delante", "más cerca de ti"), ("detrás", "más lejos de ti"), ("entre", "en el medio de otros dos"), ("fila", "objetos puestos uno al lado del otro")],
    worked=[
        {"title": "Describir una fila", "problem": "La fila, de izquierda a derecha como tú la ves, es lápiz, libro, goma. ¿Dónde está el lápiz respecto del libro?", "steps": ["El libro es el referente.", "El lápiz está antes del libro, hacia la izquierda.", "Digo: el lápiz está a la izquierda del libro.", "Lo contrario: el libro está a la derecha del lápiz."], "answer": "El lápiz está a la izquierda del libro"},
        {"title": "Entre dos objetos", "problem": "En la misma fila, ¿qué objeto está entre el lápiz y la goma?", "steps": ["El lápiz es el primero y la goma el último.", "En el medio de los dos está el libro.", "Digo: el libro está entre el lápiz y la goma.", "Reviso: lápiz, libro, goma."], "answer": "El libro"},
    ],
    mistakes=[
        {"wrong": "Decir que la goma está a la izquierda del libro.", "why": "Se mira la fila desde el lado equivocado.", "fix": "Lee la fila de izquierda a derecha: la goma viene después del libro, a su derecha."},
        {"wrong": "Describir la posición sin decir el referente («está a la izquierda»).", "why": "No se sabe a la izquierda de qué.", "fix": "Siempre nombra el objeto de referencia: «a la izquierda del libro»."},
    ],
    tiers={
        "recovery": [
            ex("La fila, de izquierda a derecha, es lápiz, libro, goma. ¿Qué hay a la izquierda del libro?", "El lápiz", "En la fila, el lápiz viene antes del libro."),
            ex("En la misma fila, ¿qué hay a la derecha del libro?", "La goma", "La goma viene después del libro."),
            ex("En la misma fila, ¿qué objeto está entre el lápiz y la goma?", "El libro", "Está en el medio."),
        ],
        "understand": [
            ex("La goma está a la derecha del libro. ¿El libro está a la derecha o a la izquierda de la goma?", "A la izquierda", "Si uno está a la derecha del otro, el otro está a la izquierda."),
            ex("Una taza está más cerca de ti que un libro. ¿Está delante o detrás del libro?", "Delante", "Delante es más cerca de ti."),
            ex("¿Qué palabra usas para decir que un objeto está en el medio de otros dos?", "Entre", "Esa palabra nombra el lugar del medio."),
        ],
        "apply": [
            ex("La fila, de izquierda a derecha, es taza, plato, vaso, cuchara, servilleta. ¿Qué hay a la derecha del vaso?", "La cuchara", "Viene justo después del vaso."),
            ex("En la misma fila, ¿qué objeto está a la izquierda del plato?", "La taza", "Viene justo antes del plato."),
            ex("En la misma fila, ¿qué objeto está entre el plato y la cuchara?", "El vaso", "Es el único entre los dos."),
        ],
        "reason": [
            ex("Lía dice que el vaso está a la izquierda del plato en la fila taza, plato, vaso, cuchara, servilleta. ¿Qué error comete?", "El vaso está a la derecha del plato", "En la fila, el vaso viene después del plato."),
            ex("Te paras al otro lado de la mesa y miras la fila lápiz, libro, goma. ¿El lápiz queda a tu derecha o a tu izquierda?", "A tu derecha", "Al verla desde el lado opuesto, se invierten izquierda y derecha."),
        ],
        "challenge": [
            ex("Hay cinco sillas A, B, C, D y E, de izquierda a derecha. Luz está en C. Ana está justo a la derecha de Luz y Tomás está justo a la izquierda de Luz. ¿En qué sillas están Ana y Tomás?", "Ana en D y Tomás en B", "La silla de la derecha de C es D y la de la izquierda es B."),
            ex("Ordena de izquierda a derecha: el gato está a la derecha del perro, el pez está a la izquierda del perro y el loro está a la derecha del gato.", "Pez, perro, gato, loro", "Cada animal queda en el lugar que indica su referente."),
        ],
    },
    context=[ex("En tu estante hay, de izquierda a derecha, un libro de cuentos, uno de ciencias y uno de dibujo. ¿Cuál está en el medio y cuál está más a la derecha?", "Ciencias está en el medio; dibujo está más a la derecha", "El orden es cuentos, ciencias, dibujo.")],
    selfcheck=[ex("En la fila lápiz, libro, goma, ¿qué está a la izquierda de la goma?", "El libro", "Viene justo antes de la goma."), ex("¿Qué es el referente en «el lápiz está a la izquierda del libro»?", "El libro", "Es el objeto desde el cual se describe."), ex("Si A está a la derecha de B, ¿dónde está B respecto de A?", "A la izquierda", "Son posiciones opuestas.")],
    open_task=task(
        "En una mesa pon un lápiz, un libro y una goma en fila, de izquierda a derecha, y una taza delante del libro (más cerca de ti). Dibuja la mesa vista desde arriba y escribe cuatro frases: dónde está el lápiz respecto del libro, la goma respecto del libro, la taza respecto del libro y qué objeto está entre dos.",
        "Dibujo: una fila lápiz, libro, goma y la taza más cerca de ti, frente al libro. Frases: el lápiz está a la izquierda del libro; la goma está a la derecha del libro; la taza está delante del libro; el libro está entre el lápiz y la goma.",
        ["ordena la fila de izquierda a derecha", "ubica la taza delante del libro", "usa un referente en cada frase", "usa la palabra entre"],
        ["dibujo visto desde arriba", "cuatro frases"],
        ["no nombrar el referente", "mirar la fila desde el lado equivocado"],
        "Pide que cambie el referente (por ejemplo, la goma) y diga de nuevo la posición del libro; reconoce que las frases son completas.",
    ),
    reinforce="Pon tres juguetes en fila y di dónde está cada uno respecto de los otros, usando izquierda, derecha y entre.",
    extend="Desordena tu fila, descríbela a un adulto sin mostrarla y pídele que la arme con solo tus palabras.",
)

register(
    OA14, 3,
    materials="Dos figuras pequeñas de papel con una flecha que indique hacia dónde miran, y lápiz. Todo está descrito en los ejercicios.",
    use="Aprenderé que la derecha y la izquierda dependen de hacia dónde mira cada persona. Sirve para entender indicaciones de otras personas, y para darlas bien.",
    prior=["Sé que mi derecha y mi izquierda son de mi cuerpo.", "Sé decir la posición de un objeto respecto de otro."],
    explain=[
        "Cada persona tiene su propia derecha y su propia izquierda. Dos personas pueden mirar hacia lugares distintos, así que su derecha no siempre apunta al mismo lugar. Para saber qué es derecha para alguien, imagina que estás en su lugar mirando hacia donde esa persona mira.",
        "Si dos personas están frente a frente, sus lados están al revés. Lo que está a la derecha de una queda a la izquierda de la otra. Por ejemplo, Ana y Beto se miran de frente. La pelota está a la derecha de Ana, entonces está a la izquierda de Beto.",
        "Si dos personas miran hacia el mismo lado, una detrás de la otra, tienen la misma derecha y la misma izquierda. Cuando alguien te da una indicación, pregúntate hacia dónde mira esa persona. Cuando tú se la das a otra, piensa desde dónde ella la verá.",
    ],
    vocab=[("perspectiva", "el punto desde el cual alguien mira"), ("frente a frente", "dos personas que se miran"), ("hacia el mismo lado", "dos personas que miran hacia donde mismo"), ("lados opuestos", "uno es derecha y el otro es izquierda"), ("indicación", "una instrucción que dice dónde ir o dónde está algo")],
    worked=[
        {"title": "Dos personas frente a frente", "problem": "Ana y Beto están frente a frente. Una pelota está a la derecha de Ana. ¿A qué lado de Beto está?", "steps": ["Ana y Beto miran hacia lados opuestos.", "Lo que está a la derecha de Ana está hacia el lado contrario para Beto.", "Imagino que estoy en el lugar de Beto: la pelota queda a mi izquierda.", "La pelota está a la izquierda de Beto."], "answer": "A la izquierda de Beto"},
        {"title": "Hacia el mismo lado", "problem": "Laura va delante de ti y las dos miran hacia el pizarrón. Su mochila queda en su lado derecho. ¿En qué lado de ti la ves?", "steps": ["Las dos miramos hacia el mismo lado.", "Entonces tenemos la misma derecha.", "Si la mochila está a su derecha, también está a mi derecha.", "La veo a mi derecha."], "answer": "A mi derecha"},
    ],
    mistakes=[
        {"wrong": "Decir que la derecha de dos personas frente a frente es del mismo lado.", "why": "Se piensa que la derecha es un lugar de la sala.", "fix": "Frente a frente, sus lados son opuestos: la derecha de una es la izquierda de la otra."},
        {"wrong": "Responder desde mi lugar sin pensar hacia dónde mira la otra persona.", "why": "Se usa la propia perspectiva en lugar de la ajena.", "fix": "Imagina que estás en su lugar mirando hacia donde mira."},
    ],
    tiers={
        "recovery": [
            ex("Tú y una amiga están frente a frente. Ella levanta su mano derecha. ¿La ves a tu derecha o a tu izquierda?", "A tu izquierda", "Frente a frente, los lados quedan opuestos."),
            ex("Dos niños miran hacia la misma pared, uno detrás del otro. ¿Tienen la misma derecha?", "Sí", "Miran hacia el mismo lado."),
            ex("Ana y Beto están frente a frente. Una pelota está a la derecha de Ana. ¿A qué lado de Beto queda?", "A la izquierda", "Son lados opuestos."),
        ],
        "understand": [
            ex("Estás detrás de Laura y los dos miran hacia el pizarrón. Su mochila queda en su lado derecho. ¿La ves a tu derecha o a tu izquierda?", "A tu derecha", "Ambos miran hacia el mismo lado."),
            ex("¿Por qué la derecha de dos personas frente a frente apunta a lados contrarios?", "Porque cada una mira hacia el lado opuesto", "Su cuerpo está de frente al otro."),
            ex("Una niña dice «mi derecha» y el niño de enfrente también dice «mi derecha», señalando. ¿Señalan el mismo lado de la sala?", "No", "Sus derechas están en lados opuestos."),
        ],
        "apply": [
            ex("Dos personas se miran. Una tiene un vaso en su lado izquierdo. ¿En qué lado de la otra persona está el vaso?", "En su lado derecho", "Frente a frente, izquierda y derecha se invierten."),
            ex("Una niña mira hacia el pizarrón y el reloj está a su derecha. Un niño parado junto al pizarrón la mira de frente. ¿El reloj queda a la derecha o a la izquierda del niño?", "A la izquierda del niño", "Ella y él miran hacia lados opuestos."),
            ex("Un libro está a tu derecha. Das media vuelta para mirar hacia atrás. ¿Dónde queda el libro respecto de ti?", "A tu izquierda", "El libro no se movió, pero tu cuerpo giró."),
        ],
        "reason": [
            ex("Camila dice: «Si estoy frente a Tomás, mi derecha y su derecha son del mismo lado». ¿Qué error comete?", "Frente a frente, sus lados son opuestos", "Cada uno mira hacia el otro."),
            ex("Dos amigas miran hacia el mismo lado. Una dice que la mochila está a su derecha. ¿La otra puede decir lo mismo?", "Sí", "Tienen la misma derecha."),
        ],
        "challenge": [
            ex("Tres personas A, B y C están en fila mirando al frente. A está a la izquierda de B y C a su derecha. Una persona D está frente a ellas y las mira. Desde D, ¿quién queda a su izquierda: A o C?", "C", "D mira hacia el lado contrario y sus lados se invierten."),
            ex("Luz y Ben están frente a frente. Luz ve la mano levantada de Ben a su izquierda. ¿Ben levantó su mano derecha o su mano izquierda?", "Su mano derecha", "Lo que Luz ve a su izquierda es la derecha de Ben."),
        ],
    },
    context=[ex("En el patio, Ana corre hacia el árbol y Beto la espera junto al árbol, mirándola de frente. El banco está a la derecha de Ana. ¿Dónde ve Beto el banco?", "A su izquierda", "Beto y Ana se miran de frente.")],
    selfcheck=[ex("Dos personas frente a frente. Lo que está a la derecha de una, ¿queda a la derecha o a la izquierda de la otra?", "A la izquierda", "Los lados se invierten."), ex("Dos personas miran hacia el mismo lado. ¿Comparten la misma derecha?", "Sí", "Miran hacia el mismo lugar."), ex("Para saber la derecha de otra persona, ¿qué debes imaginar?", "Que estás en su lugar mirando hacia donde ella mira", "Así ves lo que ella ve.")],
    open_task=task(
        "Dibuja dos figuras de papel que se miran de frente, con una flecha para mostrar hacia dónde mira cada una. Pon una pelota a la derecha de la primera. Luego haz que las dos miren hacia el mismo lado, una detrás de la otra, y pon la pelota a la derecha de la primera. En cada caso escribe a qué lado de la segunda figura queda la pelota.",
        "Frente a frente: la pelota está a la derecha de la primera figura y queda a la izquierda de la segunda. Mirando hacia el mismo lado: la pelota está a la derecha de la primera y también a la derecha de la segunda.",
        ["dibuja las figuras con sus flechas", "responde izquierda en el caso frente a frente", "responde derecha en el caso mismo lado", "explica por qué cambia"],
        ["dibujos con flechas", "dos respuestas", "explicación"],
        ["creer que la derecha es un lugar fijo", "no imaginar la perspectiva de la otra persona"],
        "Pide que gire las figuras de papel para comprobar lo que dice; reconoce que explica la diferencia entre los dos casos.",
    ),
    reinforce="Pídele a un adulto que se pare frente a ti, levante su mano derecha y diga hacia qué lado de tu cuerpo queda esa mano.",
    extend="Párate frente a otra persona. Explícale por qué tu mano derecha queda frente a su mano izquierda.",
)

register(
    OA14, 4,
    materials=f"Una hoja con una cuadrícula de 4 por 4 dibujada por ti, un botón o una ficha como figura y lápiz. {GRID}",
    use="Aprenderé a seguir un recorrido con las instrucciones avanza, gira a la derecha y gira a la izquierda, y a dar un recorrido a otra persona. Sirve para guiar a alguien por un camino.",
    prior=["Sé cuál es mi derecha y mi izquierda.", "Sé que lo que veo a mi derecha depende de hacia dónde miro."],
    explain=[
        "Un recorrido es un camino que se describe con instrucciones. «Avanza 2» significa mover 2 casillas hacia donde mira la figura. «Gira a la derecha» significa que la figura gira hacia su lado derecho, sin moverse de casilla. «Gira a la izquierda» es lo mismo hacia el otro lado.",
        "Cada giro cambia hacia dónde mira la figura. Una figura que mira hacia arriba y gira a la derecha queda mirando hacia la derecha del dibujo. Si vuelve a girar a la derecha, queda mirando hacia abajo. Por eso, para seguir un recorrido, conviene girar la figura de papel con las manos y no solo el lápiz.",
        "Para dar un recorrido, di primero dónde parte la figura y hacia dónde mira. Después da las instrucciones una por una. Prueba con tu figura para ver si llega a la casilla pedida. Si no llega, revisa cuál instrucción cambió el camino.",
    ],
    vocab=[("recorrido", "camino que sigue una figura"), ("avanzar", "moverse hacia donde mira la figura"), ("girar a la derecha", "cambiar la mirada hacia el lado derecho de la figura"), ("girar a la izquierda", "cambiar la mirada hacia el lado izquierdo de la figura"), ("casilla", "cada cuadrado de la cuadrícula")],
    worked=[
        {"title": "Seguir un recorrido", "problem": f"{GRID} La figura está en B1 mirando hacia arriba. Avanza 2, gira a la derecha y avanza 1. ¿En qué casilla queda?", "steps": ["Avanza 2 hacia arriba: B1 → B2 → B3.", "Gira a la derecha: ahora mira hacia la derecha del dibujo.", "Avanza 1: B3 → C3.", "Queda en C3."], "answer": "C3"},
        {"title": "El giro depende de hacia dónde mira", "problem": "Una figura mira hacia abajo y gira a la derecha. ¿Hacia dónde mira ahora?", "steps": ["Imagino que soy la figura mirando hacia abajo.", "Mi lado derecho está hacia la izquierda del dibujo.", "Al girar a la derecha, miro hacia la izquierda del dibujo.", "Por eso conviene girar la figura con las manos."], "answer": "Hacia la izquierda del dibujo"},
    ],
    mistakes=[
        {"wrong": "Pensar que «gira a la derecha» siempre significa ir hacia la columna D.", "why": "No se mira hacia dónde está mirando la figura.", "fix": "La derecha es de la figura: si mira hacia abajo, su derecha es hacia la izquierda del dibujo."},
        {"wrong": "Mover la figura al girar.", "why": "Se confunde girar con avanzar.", "fix": "Girar cambia hacia dónde mira, pero la figura queda en la misma casilla."},
    ],
    tiers={
        "recovery": [
            route("B1", "arriba", [("av", 2)], "Se avanza 2 casillas hacia arriba.", "Estás en B1 mirando hacia arriba. Avanzas 2 casillas. ¿En qué casilla quedas?"),
            ex("Estás en B3 mirando hacia arriba. Giras a la derecha. ¿Hacia dónde miras: hacia arriba, hacia la derecha del dibujo, hacia abajo o hacia la izquierda del dibujo?", "Hacia la derecha del dibujo", "Mirando hacia arriba, tu derecha apunta hacia el lado derecho."),
            route("A1", "derecha", [("av", 3)], "Se avanza 3 casillas hacia la derecha del dibujo.", "Estás en A1 mirando hacia la derecha del dibujo. Avanzas 3 casillas. ¿En qué casilla quedas?"),
        ],
        "understand": [
            ex("Una figura en B2 mira hacia arriba y gira a la izquierda. ¿Hacia dónde mira?", "Hacia la izquierda del dibujo", "Su lado izquierdo apunta hacia la izquierda."),
            ex("Una figura mira hacia arriba y gira a la derecha dos veces seguidas. ¿Hacia dónde mira?", "Hacia abajo", "Primero queda mirando hacia la derecha y luego hacia abajo."),
            ex("¿«Gira a la derecha» depende de hacia dónde mira la figura?", "Sí", "La derecha es de la figura, no del dibujo."),
        ],
        "apply": [
            route("B1", "arriba", [("av", 2), ("gd",), ("av", 1)], "Sube 2 hasta B3, gira hacia la derecha y avanza 1 hasta C3.", "Estás en B1 mirando hacia arriba. Avanzas 2, giras a la derecha y avanzas 1. ¿En qué casilla quedas?"),
            route("C1", "arriba", [("av", 3), ("gi",), ("av", 2)], "Sube hasta C4, gira hacia la izquierda y avanza 2 hasta A4.", "Estás en C1 mirando hacia arriba. Avanzas 3, giras a la izquierda y avanzas 2. ¿En qué casilla quedas?"),
            route("D3", "izquierda", [("av", 1), ("gi",), ("av", 2)], "Va hasta C3, gira a su izquierda (hacia abajo) y avanza 2 hasta C1.", "Estás en D3 mirando hacia la izquierda del dibujo. Avanzas 1, giras a la izquierda y avanzas 2. ¿En qué casilla quedas?"),
        ],
        "reason": [
            ex("Ana dice que «gira a la derecha» siempre lleva hacia la columna D. ¿Qué error comete?", "Depende de hacia dónde mira la figura; mirando hacia abajo, su derecha es hacia la columna A", "La derecha es de la figura."),
            ex("Desde B1 mirando hacia arriba hay dos recorridos: uno avanza 2, gira a la derecha y avanza 1; el otro gira a la derecha, avanza 1, gira a la izquierda y avanza 2. ¿Terminan en la misma casilla?", "Sí; en C3", "El primero llega a C3 y el segundo también."),
        ],
        "challenge": [
            ex("Escribe instrucciones para ir de A1 a C3 mirando hacia arriba al comienzo.", "Por ejemplo: avanza 2, gira a la derecha y avanza 2 (también: gira a la derecha, avanza 2, gira a la izquierda, avanza 2)", "Sube 2 hasta A3 y luego recorre 2 hacia la derecha hasta C3."),
            route("A1", "arriba", [("av", 3), ("gd",), ("av", 3), ("gd",), ("av", 3)], "Sube hasta A4, gira a la derecha y avanza hasta D4, gira a la derecha otra vez y baja hasta D1.", "Estás en A1 mirando hacia arriba. Avanzas 3, giras a la derecha, avanzas 3, giras a la derecha y avanzas 3. ¿En qué casilla quedas y hacia dónde miras?", with_facing=True),
        ],
    },
    context=[route("A2", "derecha", [("av", 2), ("gi",), ("av", 2)], "Avanza hasta C2, gira a la izquierda (hacia arriba) y avanza 2 hasta C4.", "Un robot de juguete está en A2 mirando hacia la derecha del dibujo. Avanza 2, gira a la izquierda y avanza 2. ¿En qué casilla queda?")],
    selfcheck=[route("B2", "arriba", [("av", 2)], "Se avanza hacia arriba.", "Estás en B2 mirando hacia arriba y avanzas 2. ¿En qué casilla quedas?"), ex("Una figura mira hacia la derecha del dibujo y gira a la derecha. ¿Hacia dónde mira?", "Hacia abajo", "Su lado derecho apunta hacia abajo."), ex("Cuando la figura gira, ¿cambia de casilla?", "No", "Solo cambia hacia dónde mira.")],
    open_task=task(
        f"{GRID} Una figura está en A1 mirando hacia arriba. Escribe instrucciones para que llegue a D2. Después sigue estas instrucciones desde B1 mirando hacia arriba: gira a la derecha, avanza 2, gira a la izquierda y avanza 1. Marca en tu cuadrícula cada casilla por la que pasa y escribe dónde termina.",
        "De A1 a D2: gira a la derecha, avanza 3 hasta D1, gira a la izquierda y avanza 1 hasta D2. Desde B1: gira a la derecha (mira hacia la derecha del dibujo), avanza 2 hasta D1, gira a la izquierda (mira hacia arriba), avanza 1 hasta D2. Termina en D2.",
        ["escribe instrucciones que llegan a D2", "sigue el segundo recorrido casilla por casilla", "termina en D2", "usa los giros según hacia dónde mira"],
        ["instrucciones escritas", "cuadrícula con el camino marcado", "casilla final"],
        ["girar sin pensar hacia dónde mira la figura", "mover la figura al girar"],
        "Pide que gire su ficha con las manos mientras lee las instrucciones; reconoce que comprueba su recorrido en la cuadrícula.",
    ),
    reinforce="Con una ficha en una cuadrícula de papel, sigue estas instrucciones: avanza 2, gira a la derecha, avanza 2. Marca el camino.",
    extend="Escribe un recorrido de cuatro instrucciones que parta y termine en la misma casilla y pide a un adulto que lo siga.",
)
