"""Student material for 3.º básico Matemática, OA 01 (conteo flexible hasta 1.000) y OA 02 (representaciones)."""
from __future__ import annotations

from student_content_ma02_a import words as words2
from student_lessons import arith, ex, fmt, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def seq(start: int, step: int, count: int) -> list[int]:
    return [start + step * index for index in range(count)]


def fill(start: int, step: int, count: int, blanks: tuple[int, ...], why: str, lead: str = "Completa la secuencia") -> dict:
    values = seq(start, step, count)
    shown = ", ".join("__" if index in blanks else fmt(value) for index, value in enumerate(values))
    answer = ", ".join(fmt(values[index]) for index in blanks)
    return ex(f"{lead}: {shown}.", answer, why)


def words3(number: int) -> str:
    """Número del 0 al 1.000 escrito con palabras."""
    if number == 1000:
        return "mil"
    if number < 100:
        return words2(number)
    hundreds = {1: "ciento", 2: "doscientos", 3: "trescientos", 4: "cuatrocientos", 5: "quinientos", 6: "seiscientos", 7: "setecientos", 8: "ochocientos", 9: "novecientos"}
    c, rest = divmod(number, 100)
    if rest == 0:
        return "cien" if c == 1 else hundreds[c]
    return f"{hundreds[c]} {words2(rest)}"


def blk(c: int, d: int, u: int) -> str:
    """Bloques: ▣ centena, ▮ decena, ● unidad."""
    return " | ".join(part for part in (" ".join(["▣"] * c), " ".join(["▮"] * d), " ".join(["●"] * u)) if part) or "(nada)"


OA1 = "MA03 OA 01"
OA2 = "MA03 OA 02"

# ---------------------------------------------------------------- OA 01
register(
    OA1, 1,
    materials="Una recta numérica dibujada en el cuaderno y un lápiz. Todos los números que necesitas están escritos en cada ejercicio.",
    use="Aprenderé a contar de 5 en 5 empezando en cualquier número, no solo en 0 ni en 5. Sirve para contar cosas en grupos de cinco sin perder el lugar.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10 hasta 100.", "Sé leer números de tres cifras."],
    explain=[
        "Contar de 5 en 5 significa que cada número nuevo es 5 más que el anterior. Si empiezas en 235, dices 240, 245, 250. Pero puedes empezar en cualquier número menor que 1.000, por ejemplo en 237: 242, 247, 252, 257.",
        "Mira las cifras de las unidades. Si empiezas en un múltiplo de 5 (termina en 0 o en 5), las unidades son siempre 0 y 5. Si empiezas en 237, las unidades son 7, 2, 7, 2. Se repiten solo dos cifras, y eso te ayuda a revisar la cuenta.",
        "Para no equivocarte, suma de a poco: 237 + 5 = 242. Si pasas por una decena, ten cuidado: 247 + 5 = 252, las decenas cambian de 4 a 5. Después revisa que entre dos vecinos haya siempre 5 de diferencia.",
    ],
    vocab=[("secuencia", "lista de números que sigue una regla"), ("salto", "lo que avanzo en cada paso"), ("punto de partida", "el primer número desde el que cuento"), ("múltiplo de 5", "número que se dice al contar de 5 en 5 desde 0"), ("unidades", "la última cifra de un número")],
    worked=[
        {"title": "Partir en un número cualquiera", "problem": "Cuenta de 5 en 5 desde 237 y escribe cuatro números más.", "steps": ["Escribo el punto de partida: 237.", "Sumo 5: 237 + 5 = 242.", "Sumo 5 otra vez: 242 + 5 = 247. Luego 247 + 5 = 252 y 252 + 5 = 257.", "Compruebo: entre vecinos siempre hay 5."], "answer": "237, 242, 247, 252, 257"},
        {"title": "Contar hacia atrás", "problem": "Cuenta hacia atrás de 5 en 5 desde 413 y escribe tres números más.", "steps": ["Ir hacia atrás es restar 5.", "413 − 5 = 408.", "408 − 5 = 403 y 403 − 5 = 398.", "Observo que las unidades se repiten: 3, 8, 3, 8."], "answer": "413, 408, 403, 398"},
    ],
    mistakes=[
        {"wrong": "Partir en 237 y escribir 240, 245, 250.", "why": "Se salta al múltiplo de 5 más cercano en vez de sumar 5 al número dado.", "fix": "El primer número que dices es 237 + 5 = 242. El salto siempre se calcula desde el punto de partida."},
        {"wrong": "Escribir 242, 247, 253, 257.", "why": "En el medio se cambió el salto de 5 por 6.", "fix": "Calcula la diferencia entre cada par de vecinos; todas deben ser 5."},
    ],
    tiers={
        "recovery": [
            ex("Completa la secuencia de 5 en 5: 235, 240, __, 250, __.", "245, 255", "Cada número es 5 más que el anterior: 240 + 5 = 245 y 250 + 5 = 255."),
            fill(128, 5, 5, (2, 4), "Se suma 5 cada vez: 128, 133, 138, 143, 148.", "Escribe los números que faltan al contar de 5 en 5"),
            ex("Cuenta de 5 en 5 hacia adelante desde 462 y escribe los tres números siguientes.", "467, 472, 477", "462 + 5 = 467, 467 + 5 = 472 y 472 + 5 = 477."),
        ],
        "understand": [
            ex("Lucía contó 84, 89, 94, 99. ¿De cuánto en cuánto contó?", "De 5 en 5", "89 − 84 = 5 y 94 − 89 = 5: la diferencia siempre es 5."),
            ex("Si cuentas de 5 en 5 desde 237, ¿qué número viene después de 242: 245 o 247?", "247", "242 + 5 = 247. No se salta a 245 porque se parte en 237, no en un múltiplo de 5."),
            ex("Al contar de 5 en 5 desde 237, las unidades de los números se repiten. ¿Qué dos cifras se repiten?", "7 y 2", "237, 242, 247, 252: las unidades son 7, 2, 7, 2."),
        ],
        "apply": [
            ex("Una caja tiene 295 clips y se cuentan de 5 en 5 desde el 295. ¿Qué tres números se dicen después de 295?", "300, 305, 310", "295 + 5 = 300, luego 305 y 310. Al pasar por 300 cambia la cifra de las centenas."),
            arith("Sofía cuenta pasos de 5 en 5. Partió en el paso 340 y dio 4 saltos. ¿En qué número quedó?", "340+5+5+5+5", "Cada salto suma 5 y son 4 saltos."),
            fill(906, -5, 5, (1, 3), "Hacia atrás se resta 5: 906, 901, 896, 891, 886.", "Completa la cuenta hacia atrás de 5 en 5"),
        ],
        "reason": [
            ex("Mario dice: «Si parto en 237 y cuento de 5 en 5, diré el 250». ¿Tiene razón?", "No", "237, 242, 247, 252: salto de 5 en 5, nunca aparece el 250 porque las unidades son 7 y 2."),
            ex("Camila escribió esta secuencia de 5 en 5: 413, 418, 424, 428. ¿Cuál es el error y cómo se corrige?", "424 debe ser 423", "418 + 5 = 423, no 424. Después 423 + 5 = 428, así que el último número queda bien."),
        ],
        "challenge": [
            ex("Parto en 976 y cuento de 5 en 5 sin pasar de 1.000. ¿Cuál es el último número que digo?", "996", "976, 981, 986, 991, 996: el siguiente sería 1.001, que ya pasa de 1.000."),
            ex("Dos amigas cuentan de 5 en 5: una parte en 602 y la otra en 607. ¿Dirán alguna vez el mismo número? Explica.", "Sí, el 607", "La primera dice 602, 607, ... y la segunda parte justo en 607."),
        ],
    },
    context=[ex("Un guardia cuenta personas que entran a un estadio de 5 en 5. Va en 465 y cuenta tres saltos más. ¿Qué números dice?", "470, 475, 480", "465 + 5 = 470, 470 + 5 = 475 y 475 + 5 = 480.")],
    selfcheck=[
        ex("Completa: 71, 76, __, 86.", "81", "76 + 5 = 81."),
        ex("Cuenta de 5 en 5 desde 238. ¿Qué número sigue?", "243", "238 + 5 = 243."),
        ex("Mira 304, 309, 314, 319. ¿Qué dos cifras de unidades se repiten?", "4 y 9", "Las unidades son 4, 9, 4, 9: se repiten solo dos cifras."),
    ],
    open_task=task(
        "Parte en 372 y cuenta de 5 en 5 hasta tener seis números. Dibuja los saltos en una recta numérica y escribe una frase que diga qué notas en las unidades.",
        "372, 377, 382, 387, 392, 397. En la recta hay cinco flechas con +5. Observo que las unidades son 2, 7, 2, 7, 2, 7: se repiten dos cifras.",
        ["escribe seis números", "mantiene el salto de 5", "dibuja los saltos", "describe lo que observa en las unidades"],
        ["secuencia escrita en el cuaderno", "recta numérica dibujada", "frase de explicación propia"],
        ["empezar en un múltiplo de 5 en vez del número dado", "cambiar el salto a mitad de la secuencia"],
        "Reconoce que la secuencia es correcta y pide que revise la diferencia entre vecinos; si hay un error, que sea el propio estudiante quien encuentre dónde cambió el salto.",
    ),
    reinforce="Cuenta de 5 en 5 desde 20 con ayuda de tapas: pon cinco tapas en cada salto y escribe el número que alcanzas.",
    extend="Si cuentas de 5 en 5 desde 237, ¿llegarás a 1.000? Escribe cómo lo sabes mirando las unidades.",
)

register(
    OA1, 2,
    materials="Una recta numérica dibujada en el cuaderno y lápiz de color. Los números de trabajo están escritos en cada ejercicio.",
    use="Aprenderé a contar de 10 en 10 aunque pase de una centena a la siguiente. Sirve para saltar rápido, por ejemplo de 290 a 300.",
    prior=["Sé contar de 10 en 10 hasta 100.", "Sé que 10 decenas forman una centena."],
    explain=[
        "Contar de 10 en 10 es sumar 10 cada vez. Las unidades no cambian, porque 10 no tiene unidades. Si empiezas en 274, dices 284, 294, 304, 314: todas terminan en 4.",
        "Lo que sí cambia son las decenas. Cuando las decenas llegan a 9 y sumas 10, se completa una centena: 294 + 10 = 304. La cifra de las centenas sube en 1 y las decenas vuelven a 0. Eso pasa al cruzar de una centena a otra.",
        "Hacia atrás es parecido: restas 10 cada vez. De 512 vas a 502, y de 502 a 492. Aquí las centenas bajan de 5 a 4. Para revisar, pregúntate: ¿cambió solo la decena, o también la centena?",
    ],
    vocab=[("decena", "grupo de 10 unidades"), ("centena", "grupo de 10 decenas, o 100 unidades"), ("cruzar una centena", "pasar de un número como 298 a uno como 308"), ("hacia atrás", "contar restando en cada salto"), ("secuencia", "lista de números que sigue una regla")],
    worked=[
        {"title": "Cruzar la centena hacia adelante", "problem": "Cuenta de 10 en 10 desde 274 y escribe cuatro números más.", "steps": ["Sumo 10 a 274: 284.", "284 + 10 = 294.", "294 + 10 = 304: las decenas llegaron a 10 y formaron una centena más. Luego 304 + 10 = 314.", "Las unidades siempre fueron 4."], "answer": "274, 284, 294, 304, 314"},
        {"title": "Cruzar la centena hacia atrás", "problem": "Cuenta hacia atrás de 10 en 10 desde 512 y escribe cuatro números más.", "steps": ["Resto 10: 512 − 10 = 502.", "502 − 10 = 492: la centena bajó de 5 a 4.", "492 − 10 = 482 y 482 − 10 = 472.", "Las unidades siempre fueron 2."], "answer": "512, 502, 492, 482, 472"},
    ],
    mistakes=[
        {"wrong": "Escribir 274, 284, 294, 2104.", "why": "Se sigue sumando a la cifra de las decenas sin reagrupar.", "fix": "10 decenas son 1 centena: después de 294 viene 304."},
        {"wrong": "Contar 502, 492, 482 como 502, 592, 582.", "why": "Se confunde la cifra que baja al restar 10.", "fix": "Al restar 10 de 502 bajas una decena: queda 4 centenas y 9 decenas, o sea 492."},
    ],
    tiers={
        "recovery": [
            fill(270, 10, 5, (1, 3), "Cada número es 10 más: 270, 280, 290, 300, 310.", "Completa la secuencia de 10 en 10"),
            fill(386, 10, 5, (2, 3), "Se suma 10 cada vez: 386, 396, 406, 416, 426.", "Escribe los números que faltan al contar de 10 en 10"),
            ex("Cuenta de 10 en 10 hacia atrás desde 530 y escribe los tres números siguientes.", "520, 510, 500", "Cada vez se resta 10: 530 − 10 = 520, luego 510 y 500."),
        ],
        "understand": [
            ex("En la secuencia 388, 398, 408, 418 cambió la cifra de las centenas. ¿Entre qué dos números cambió?", "Entre 398 y 408", "398 + 10 = 408: las 9 decenas más 1 decena forman una centena."),
            ex("¿Qué número viene después de 790 si cuentas de 10 en 10 hacia adelante?", "800", "790 + 10 = 800, porque 10 decenas forman una centena."),
            ex("Al contar de 10 en 10, ¿qué cifra nunca cambia: la de las unidades o la de las decenas?", "La de las unidades", "Sumar 10 solo agrega una decena; las unidades quedan iguales."),
        ],
        "apply": [
            arith("Un contador de pasos marca 695 y sube de 10 en 10. Pasa por 4 saltos. ¿Qué número marca al final?", "695+10+10+10+10", "Se suma 10 cuatro veces."),
            fill(905, -10, 5, (2, 4), "Hacia atrás se resta 10 cada vez: 905, 895, 885, 875, 865.", "Completa la cuenta hacia atrás de 10 en 10"),
            ex("Escribe los cuatro números que siguen al contar de 10 en 10 desde 956.", "966, 976, 986, 996", "956 + 10 = 966, luego 976, 986 y 996."),
        ],
        "reason": [
            ex("Ana cuenta de 10 en 10 desde 862 y escribe 872, 882, 892, 8102. ¿Está bien? Escribe el número correcto.", "No, después de 892 va 902", "892 + 10 = 902; 10 decenas forman una centena y las decenas vuelven a 0."),
            ex("Dos niñas cuentan de 10 en 10: una parte en 245 y otra en 255. ¿Dirán alguna vez el mismo número?", "Sí, el 255", "245 + 10 = 255: la primera llega al número donde parte la segunda."),
        ],
        "challenge": [
            ex("Parto en 190 y cuento de 10 en 10 hasta llegar a 250. ¿Cuántos saltos doy?", "6 saltos", "200, 210, 220, 230, 240 y 250: son 6 números dichos, y cada uno es un salto."),
            ex("Cuenta hacia atrás de 10 en 10 desde 1.000. ¿Qué número dices en el quinto salto?", "950", "990, 980, 970, 960 y 950: el quinto número es 950."),
        ],
    },
    context=[ex("El contador de visitantes de un museo marca 297. Entran 10 personas cada vez. ¿Qué números marcará en las tres veces siguientes?", "307, 317, 327", "297 + 10 = 307, luego 317 y 327. Al pasar de 297 a 307 cambia la centena.")],
    selfcheck=[
        ex("Completa: 440, 450, __, 470.", "460", "450 + 10 = 460."),
        ex("¿Qué número viene después de 497 si cuentas de 10 en 10?", "507", "497 + 10 = 507: pasa de la centena 4 a la 5."),
        ex("Cuenta hacia atrás de 10 en 10 desde 305: ¿qué número sigue?", "295", "305 − 10 = 295."),
    ],
    open_task=task(
        "Parte en 684 y cuenta de 10 en 10 hacia adelante hasta pasar de 700. Escribe todos los números y marca con un círculo el lugar donde cambia la cifra de las centenas. Explica con una frase qué pasó con las decenas.",
        "684, 694, 704, 714. Marco 694 → 704, porque 9 decenas más 1 decena forman 10 decenas = 1 centena. Las decenas vuelven a 0.",
        ["escribe la secuencia completa", "marca el cambio de centena", "mantiene las unidades en 4", "explica el cambio en las decenas"],
        ["secuencia escrita en el cuaderno", "círculo en el cambio de centena", "frase de explicación propia"],
        ["escribir 7 en vez de 704", "cambiar la cifra de las unidades"],
        "Destaca que la secuencia es correcta y pide que explique en voz alta por qué 694 + 10 da 704; si hubo error, que cuente con tapas 10 decenas para formar una centena.",
    ),
    reinforce="Con dos tazas de 10 tapas cada una, cuenta de 10 en 10 desde 170 hasta 230 y anota los números.",
    extend="Cuenta de 10 en 10 desde 365. ¿Llegarás al 500? Explica mirando las unidades.",
)

register(
    OA1, 3,
    materials="Una recta numérica dibujada en el cuaderno, lápiz de color y hojas para anotar. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a contar de 100 en 100, hacia adelante y hacia atrás. Sirve para saltar de centena en centena sin contar de a uno.",
    prior=["Sé contar de 10 en 10 pasando de una centena a otra.", "Sé que 100 es una centena."],
    explain=[
        "Contar de 100 en 100 es sumar 100 cada vez, o sea una centena. Si empiezas en 237, dices 337, 437, 537. Solo cambia la cifra de las centenas; las decenas y las unidades se quedan igual: siempre 37.",
        "Hacia atrás restas 100. De 862 vas a 762, luego 662, 562. De nuevo cambia solo la primera cifra, que baja de 1 en 1. Eso hace fácil esta cuenta: miras la cifra de las centenas.",
        "Cuidado con el final. Desde 237 llegas hasta 937; después de 937 ya viene 1.037, que es mayor que 1.000. En este tema trabajamos hasta 1.000. Si empiezas en 0, 100, 200, ... llegas justo al 1.000.",
    ],
    vocab=[("centena", "100 unidades, es decir, 10 decenas"), ("hacia adelante", "contar sumando"), ("hacia atrás", "contar restando"), ("mil", "diez centenas, se escribe 1.000"), ("secuencia", "lista de números que sigue una regla")],
    worked=[
        {"title": "De 100 en 100 hacia adelante", "problem": "Cuenta de 100 en 100 desde 237 y escribe cuatro números más.", "steps": ["Sumo 100 a 237: 337.", "337 + 100 = 437.", "437 + 100 = 537 y 537 + 100 = 637.", "Solo cambia la cifra de las centenas; siempre queda 37."], "answer": "237, 337, 437, 537, 637"},
        {"title": "De 100 en 100 hacia atrás", "problem": "Cuenta hacia atrás de 100 en 100 desde 862 y escribe tres números más.", "steps": ["Resto 100: 862 − 100 = 762.", "762 − 100 = 662.", "662 − 100 = 562.", "Solo cambia la primera cifra; siempre queda 62."], "answer": "862, 762, 662, 562"},
    ],
    mistakes=[
        {"wrong": "Contar de 100 en 100 desde 237 y escribir 247, 257, 267.", "why": "Se sumó 10 en vez de 100, o sea una decena en vez de una centena.", "fix": "100 se suma a la cifra de las centenas: 237 + 100 = 337."},
        {"wrong": "Escribir 237, 337, 437, 537, 538.", "why": "Se cambió el salto al final de la secuencia.", "fix": "Revisa que todos los saltos sean de 100: solo debe cambiar la primera cifra."},
    ],
    tiers={
        "recovery": [
            fill(137, 100, 5, (1, 3), "Se suma 100 cada vez: 137, 237, 337, 437, 537.", "Completa la secuencia de 100 en 100"),
            fill(900, -100, 5, (1, 3), "Hacia atrás se resta 100: 900, 800, 700, 600, 500.", "Completa la cuenta hacia atrás de 100 en 100"),
            ex("Cuenta de 100 en 100 hacia adelante desde 312 y escribe los tres números siguientes.", "412, 512, 612", "312 + 100 = 412, 412 + 100 = 512 y 512 + 100 = 612."),
        ],
        "understand": [
            ex("Al sumar 100 a 458, ¿qué cifra cambia: la de las centenas, la de las decenas o la de las unidades?", "La de las centenas", "458 + 100 = 558: solo la primera cifra pasa de 4 a 5."),
            ex("Si cuentas de 100 en 100 hacia atrás desde 745, ¿cuál es el número que sigue: 735 o 645?", "645", "745 − 100 = 645; se resta una centena, no una decena."),
            ex("Mía contó 64, 164, 264, 364. ¿De cuánto en cuánto contó?", "De 100 en 100", "164 − 64 = 100 y 264 − 164 = 100."),
        ],
        "apply": [
            arith("Una bodega tiene 125 cajas. Llegan 100 cajas nuevas cada día durante 3 días. ¿Cuántas cajas hay al final?", "125+100+100+100", "Se suma 100 tres veces."),
            arith("Un estanque tiene 870 litros de agua y se sacan 100 litros cada hora durante 4 horas. ¿Cuántos litros quedan?", "870-100-100-100-100", "Se resta 100 cuatro veces."),
            fill(66, 100, 6, (2, 4, 5), "Se suma 100 cada vez: 66, 166, 266, 366, 466, 566.", "Escribe los números que faltan al contar de 100 en 100"),
        ],
        "reason": [
            ex("Tomás dice: «Si cuento de 100 en 100 desde 237, diré el 750». ¿Tiene razón?", "No", "La secuencia es 237, 337, ..., 737, 837. Todos terminan en 37, no en 50."),
            ex("Cuentas de 100 en 100 desde 360 hacia adelante. ¿Qué número es el primero con 9 en las centenas?", "960", "360, 460, 560, 660, 760, 860, 960."),
        ],
        "challenge": [
            ex("Parto en 48 y cuento de 100 en 100. ¿Cuál es el primer número mayor que 500 que digo?", "548", "48, 148, 248, 348, 448, 548."),
            ex("Cuenta hacia atrás de 100 en 100 desde 1.000. ¿Qué número dices en el sexto salto?", "400", "900, 800, 700, 600, 500 y 400: el sexto número es 400."),
        ],
    },
    context=[arith("Una biblioteca escolar tiene 215 libros y recibe 100 libros nuevos cada mes. ¿Cuántos libros tendrá después de 3 meses?", "215+100+100+100", "Se suma 100 tres veces.")],
    selfcheck=[
        ex("Completa: 150, 250, __, 450.", "350", "250 + 100 = 350."),
        ex("¿Qué número viene después de 799 si cuentas de 100 en 100?", "899", "799 + 100 = 899."),
        ex("Cuenta hacia atrás de 100 en 100 desde 640: ¿qué número sigue?", "540", "640 − 100 = 540."),
    ],
    open_task=task(
        "Escoge uno de estos puntos de partida: 128, 345 o 506. Cuenta de 100 en 100 hacia adelante hasta no poder pasar de 1.000. Escribe todos los números y una frase que diga qué cifra cambia y qué cifras se quedan iguales.",
        "Parto en 345: 345, 445, 545, 645, 745, 845, 945. Cambia la cifra de las centenas; las decenas y las unidades, 45, se quedan igual.",
        ["escribe todos los números hasta no pasar de 1.000", "mantiene el salto de 100", "dice qué cifra cambia", "dice qué cifras no cambian"],
        ["secuencia escrita en el cuaderno", "frase de explicación propia"],
        ["sumar 10 en vez de 100", "pasar de 1.000"],
        "Reconoce el patrón correcto y pregunta qué número seguiría si se pudiera pasar de 1.000; si hay error, pide que sume con tapas o con dinero de juguete de $100.",
    ),
    reinforce="Escribe los números de 100 en 100 desde 0 hasta 1.000 y lee la lista en voz alta.",
    extend="Cuenta de 100 en 100 desde 28. Escribe todos los números hasta 1.000 y explica por qué no llegas justo al 1.000.",
)

register(
    OA1, 4,
    materials="Una recta numérica dibujada en el cuaderno, 20 tapas o fichas y lápiz. Todos los números están escritos en cada ejercicio.",
    use="Aprenderé a contar de 3 en 3 y de 4 en 4 empezando en un múltiplo. Sirve para contar objetos que vienen en grupos de 3 o de 4.",
    prior=["Sé contar de 2 en 2, de 5 en 5 y de 10 en 10.", "Sé que sumar es avanzar en la recta numérica."],
    explain=[
        "Contar de 3 en 3 desde 0 da 0, 3, 6, 9, 12, 15, 18. Esos números se llaman múltiplos de 3. Contar de 4 en 4 desde 0 da 0, 4, 8, 12, 16, 20. Esos son los múltiplos de 4.",
        "En este tema empiezas en un múltiplo del número que cuentas. Por ejemplo, de 3 en 3 desde 21: 21, 24, 27, 30, 33. De 4 en 4 desde 36: 36, 40, 44, 48. Fíjate en cómo pasas por una decena: 27 + 3 = 30.",
        "Hacia atrás restas el salto: de 3 en 3 desde 45 dices 42, 39, 36. Para revisar, mira que la diferencia entre vecinos sea 3 (o 4). Si no estás seguro, apoya la cuenta con tapas: una tapa por cada número que dices.",
    ],
    vocab=[("múltiplo de 3", "número que dices al contar de 3 en 3 desde 0"), ("múltiplo de 4", "número que dices al contar de 4 en 4 desde 0"), ("patrón", "regla que se repite en una secuencia"), ("salto", "lo que sumo o resto en cada paso"), ("hacia atrás", "contar restando en cada salto")],
    worked=[
        {"title": "De 3 en 3 desde un múltiplo de 3", "problem": "Cuenta de 3 en 3 desde 21 y escribe cuatro números más.", "steps": ["21 es múltiplo de 3 (0, 3, 6, ..., 18, 21).", "21 + 3 = 24.", "24 + 3 = 27, 27 + 3 = 30 y 30 + 3 = 33.", "Compruebo: entre vecinos siempre hay 3."], "answer": "21, 24, 27, 30, 33"},
        {"title": "De 4 en 4 desde un múltiplo de 4", "problem": "Cuenta de 4 en 4 desde 36 y escribe cuatro números más.", "steps": ["36 es múltiplo de 4 (4, 8, 12, ..., 32, 36).", "36 + 4 = 40.", "40 + 4 = 44, 44 + 4 = 48 y 48 + 4 = 52.", "Compruebo: entre vecinos siempre hay 4."], "answer": "36, 40, 44, 48, 52"},
    ],
    mistakes=[
        {"wrong": "Contar de 4 en 4 desde 36 y escribir 40, 44, 49.", "why": "Se perdió el salto de 4 al pasar por la decena.", "fix": "Suma 4 al último número que dijiste: 44 + 4 = 48."},
        {"wrong": "Contar de 3 en 3 desde 21 y escribir 24, 27, 29.", "why": "Se sumó 2 en vez de 3 en el último salto.", "fix": "Revisa la diferencia de cada par de vecinos; debe ser siempre 3."},
    ],
    tiers={
        "recovery": [
            fill(12, 3, 5, (1, 3), "Se suma 3 cada vez: 12, 15, 18, 21, 24.", "Completa la secuencia de 3 en 3"),
            fill(24, 4, 5, (2, 4), "Se suma 4 cada vez: 24, 28, 32, 36, 40.", "Completa la secuencia de 4 en 4"),
            ex("Cuenta de 3 en 3 desde 27 y escribe los tres números siguientes.", "30, 33, 36", "27 + 3 = 30, 30 + 3 = 33 y 33 + 3 = 36."),
        ],
        "understand": [
            ex("¿Es 18 un múltiplo de 3? Cuenta de 3 en 3 desde 0 para comprobarlo.", "Sí", "0, 3, 6, 9, 12, 15, 18: el 18 aparece al contar de 3 en 3."),
            ex("¿Cuál de estos números se dice al contar de 4 en 4 desde 20: 22, 24 o 26?", "24", "20 + 4 = 24."),
            ex("Joaquín quiere contar de 4 en 4 comenzando en un múltiplo de 4. ¿Cuál puede elegir: 18, 20 o 22?", "20", "4, 8, 12, 16, 20: el 20 es múltiplo de 4; 18 y 22 no aparecen."),
        ],
        "apply": [
            arith("Cuenta de 4 en 4 desde 36. ¿Qué número dices en el tercer salto?", "36+4+4+4", "Tres saltos de 4: 40, 44 y 48."),
            fill(45, -3, 6, (1, 3), "Hacia atrás se resta 3: 45, 42, 39, 36, 33, 30.", "Completa la cuenta hacia atrás de 3 en 3"),
            ex("Cuenta hacia atrás de 4 en 4 desde 100 y escribe los tres números siguientes.", "96, 92, 88", "100 − 4 = 96, 96 − 4 = 92 y 92 − 4 = 88."),
        ],
        "reason": [
            ex("Rosa cuenta de 3 en 3 desde 21 y dice: 24, 27, 31. ¿Dónde se equivocó y cuál es el número correcto?", "En el 31; debe ser 30", "27 + 3 = 30, no 31."),
            ex("¿Aparece el 50 si cuentas de 4 en 4 desde 20?", "No", "20, 24, 28, 32, 36, 40, 44, 48, 52: pasa de 48 a 52."),
        ],
        "challenge": [
            ex("Cuento de 3 en 3 desde 90. ¿Cuál es el primer número mayor que 100 que digo?", "102", "90, 93, 96, 99, 102."),
            ex("Cuento de 4 en 4 desde 96. ¿Cuál es el primer número de tres cifras que digo?", "100", "96 + 4 = 100."),
        ],
    },
    context=[arith("Una profesora arma mesas con 4 sillas cada una y cuenta las sillas de 4 en 4: 4, 8, 12, ... ¿Cuántas sillas cuenta hasta la sexta mesa?", "4+4+4+4+4+4", "Seis saltos de 4 sillas cada uno.")],
    selfcheck=[
        ex("Completa: 12, 15, __, 21.", "18", "15 + 3 = 18."),
        ex("¿Qué número sigue en 28, 32, 36?", "40", "36 + 4 = 40."),
        ex("Cuenta hacia atrás de 3 en 3 desde 33: ¿qué número sigue?", "30", "33 − 3 = 30."),
    ],
    open_task=task(
        "Escoge: contar de 3 en 3 desde 60, o contar de 4 en 4 desde 60. Escribe seis números de la secuencia y explica cómo comprobaste que cada salto es el correcto.",
        "De 4 en 4 desde 60: 60, 64, 68, 72, 76, 80. Comprobé que entre vecinos hay siempre 4; por ejemplo, 72 − 68 = 4.",
        ["escribe seis números", "mantiene el salto elegido", "empieza en 60", "explica cómo comprobó"],
        ["secuencia escrita en el cuaderno", "frase de comprobación propia"],
        ["cambiar el salto a mitad de la secuencia", "no partir en 60"],
        "Reconoce el esfuerzo y pide que verifique restando vecinos; si hay error, que cuente con tapas los saltos de 3 o de 4.",
    ),
    reinforce="Con 24 tapas, ordénalas en grupos de 3 y cuenta de 3 en 3 hasta 24; luego en grupos de 4 y cuenta de 4 en 4.",
    extend="Cuenta de 3 en 3 desde 60 y de 4 en 4 desde 60. ¿Qué número, además del 60, aparece en las dos secuencias? Está entre 60 y 80.",
)
