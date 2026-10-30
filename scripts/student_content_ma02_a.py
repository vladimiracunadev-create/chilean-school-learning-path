"""Student material for 2.º básico Matemática, OA 01 and OA 02 (lote 1)."""
from __future__ import annotations

from student_lessons import arith, ex, fmt, register


def seq(start: int, step: int, count: int) -> list[int]:
    return [start + step * index for index in range(count)]


def fill(start: int, step: int, count: int, blanks: tuple[int, ...], why: str) -> dict:
    values = seq(start, step, count)
    shown = ", ".join("__" if index in blanks else fmt(value) for index, value in enumerate(values))
    answer = ", ".join(fmt(values[index]) for index in blanks)
    return ex(f"Completa la secuencia: {shown}.", answer, why)


def words(number: int) -> str:
    units = ["cero", "uno", "dos", "tres", "cuatro", "cinco", "seis", "siete", "ocho", "nueve", "diez", "once", "doce", "trece", "catorce", "quince",
             "dieciséis", "diecisiete", "dieciocho", "diecinueve", "veinte", "veintiuno", "veintidós", "veintitrés", "veinticuatro", "veinticinco",
             "veintiséis", "veintisiete", "veintiocho", "veintinueve"]
    tens = {3: "treinta", 4: "cuarenta", 5: "cincuenta", 6: "sesenta", 7: "setenta", 8: "ochenta", 9: "noventa"}
    if number < 30:
        return units[number]
    if number == 100:
        return "cien"
    ten, unit = divmod(number, 10)
    return tens[ten] if unit == 0 else f"{tens[ten]} y {units[unit]}"


def bars(number: int) -> str:
    ten, unit = divmod(number, 10)
    return ("▮ " * ten).strip() + (" | " if ten and unit else "") + ("● " * unit).strip() if number else "(nada)"


OA1 = "MA02 OA 01"
OA2 = "MA02 OA 02"

register(
    OA1, 1,
    materials="Cinta de papel con los números del 120 al 160 escritos en cada casilla; seis fichas; lápiz de color. Todos los números se entregan en este cuaderno.",
    use="Aprenderé a contar de 2 en 2 aunque parta de un número impar. Sirve para contar pares de zapatos, guantes o ruedas sin ir uno por uno.",
    prior=["Sé contar hacia adelante y hacia atrás hasta 100.", "Sé que sumar 2 es avanzar dos lugares en la recta numérica."],
    explain=[
        "Contar de 2 en 2 significa que cada número nuevo es dos más que el anterior. Si cuentas 2, 4, 6, 8 estás avanzando de a dos, y todos esos números son pares. Pero no es obligatorio partir en un par: puedes partir donde quieras.",
        "Si partes en 137, el siguiente es 139, después 141, 143 y 145. Mira las unidades: 7, 9, 1, 3, 5. Siempre son impares, porque a un impar le sumas 2 y sigue siendo impar. Lo que se conserva es el tamaño del salto, y también si el número es par o impar.",
        "Para no equivocarte, usa una recta numérica abierta: dibuja una flecha por cada salto y escribe arriba «+2». Al terminar, revisa que entre dos números vecinos siempre haya 2 de diferencia. Si en algún lugar hay 3 o 1, hay un error.",
    ],
    vocab=[("secuencia", "lista de números que sigue una regla"), ("salto", "lo que avanzo o retrocedo en cada paso"), ("punto de inicio", "el primer número desde el que empiezo a contar"), ("par", "número que termina en 0, 2, 4, 6 u 8"), ("impar", "número que termina en 1, 3, 5, 7 o 9")],
    worked=[
        {"title": "Partir en un impar", "problem": "Cuenta de 2 en 2 desde 137 y escribe cuatro números.", "steps": ["Escribo el punto de inicio: 137.", "Sumo 2: 137 + 2 = 139.", "Sumo 2 otra vez: 139 + 2 = 141. Luego 141 + 2 = 143 y 143 + 2 = 145.", "Compruebo: entre cada par de vecinos hay 2."], "answer": "137, 139, 141, 143, 145"},
        {"title": "Contar hacia atrás", "problem": "Cuenta hacia atrás de 2 en 2 desde 91 y escribe cuatro números más.", "steps": ["Retroceder 2 es restar 2.", "91 − 2 = 89.", "89 − 2 = 87, 87 − 2 = 85 y 85 − 2 = 83.", "Compruebo que todos terminan en número impar, igual que 91."], "answer": "91, 89, 87, 85, 83"},
    ],
    mistakes=[
        {"wrong": "Partir en 137 y escribir 138, 140, 142.", "why": "Creer que al contar de 2 en 2 hay que pasar a los pares.", "fix": "Suma 2 al número que tienes: 137 + 2 = 139. El primer salto siempre se calcula desde el punto de inicio."},
        {"wrong": "Escribir 141, 143, 144, 146.", "why": "Se cambió el salto en el medio de la secuencia.", "fix": "Calcula la diferencia entre cada par de vecinos; todas deben ser 2."},
    ],
    tiers={
        "recovery": [fill(137, 2, 5, (1, 3), "Cada número es 2 más que el anterior: 137+2=139 y 141+2=143."), fill(53, 2, 5, (2, 4), "Se suma 2 cada vez: 53, 55, 57, 59, 61."), fill(204, 2, 5, (1, 2), "Se parte en 204 y se suman 2: 206, 208.")],
        "understand": [
            ex("Mateo contó 61, 63, 65, 67. ¿Cuál es el salto que usó?", "Contó de 2 en 2", "63 − 61 = 2 y 65 − 63 = 2: la diferencia siempre es 2."),
            ex("¿El número 149 puede aparecer si cuentas de 2 en 2 desde 137? Explica.", "Sí", "137, 139, 141, 143, 145, 147, 149: los impares aparecen todos cuando parto de un impar."),
            ex("¿Aparecerá 150 si cuentas de 2 en 2 desde 137? Explica.", "No", "Todos los números de esta secuencia son impares y 150 es par."),
        ],
        "apply": [
            arith("En una caja hay zapatos. Contamos de 2 en 2 y llegamos a 12 pies, partiendo en 0. ¿Cuántos pares de zapatos hay? (Cuenta 2, 4, 6, 8, 10, 12.)", "12//2", "Seis saltos de 2 llegan a 12, por eso hay 6 pares."),
            fill(325, 2, 6, (1, 3, 5), "Se suma 2 a partir de 325: 327, 331, 335."),
            ex("Cuenta hacia atrás de 2 en 2 desde 99: escribe los cinco números siguientes.", "97, 95, 93, 91, 89", "Cada vez se resta 2 al número anterior."),
        ],
        "reason": [
            ex("Ana dice: «Si parto en 137 y cuento de 2 en 2, el cuarto número que digo es 144». ¿Tiene razón?", "No; es 143", "Si 137 es el primero, el segundo es 139, el tercero 141 y el cuarto 143. 144 es par y no puede aparecer."),
            ex("En la secuencia 211, 213, 215, 217 hay un error si se escribe 211, 213, 216, 217. ¿Cuál es el error y cómo se corrige?", "216 debe ser 215", "Entre 213 y 216 hay 3 de diferencia; el salto debe ser 2, entonces el número es 215."),
        ],
        "challenge": [
            ex("Parto en 398 y cuento de 2 en 2. ¿Cuál es el primer número mayor que 400 que digo?", "402", "La secuencia es 398, 400, 402: el 400 aparece porque 398 es par, y el siguiente es 402."),
            ex("Dos amigos cuentan de 2 en 2: uno parte en 51 y otro en 52. ¿Dirán alguna vez el mismo número? Explica.", "No", "El primero dice sólo impares y el segundo sólo pares; nunca coinciden."),
        ],
    },
    context=[ex("Una profesora tiene que repartir guantes. Cada niño recibe 1 par (2 guantes). Hay 9 niños. Cuenta de 2 en 2 y escribe cuántos guantes entrega en total.", "18 guantes", "Los números son 2, 4, 6, 8, 10, 12, 14, 16, 18: son nueve saltos de 2.")],
    selfcheck=[
        ex("Completa: 71, 73, __, 77.", "75", "73 + 2 = 75."),
        ex("¿Cuál de estas secuencias salta de 2 en 2: 20, 22, 24, 26 o 20, 25, 30, 35?", "20, 22, 24, 26", "La primera aumenta 2 en cada paso."),
        ex("Si parto en 49 y cuento de 2 en 2, ¿el siguiente número es 51 o 50?", "51", "49 + 2 = 51."),
    ],
    open_task={
        "statement": "Parte en 85 y cuenta de 2 en 2 hasta tener seis números. Dibuja los saltos en una recta numérica y escribe una frase que diga qué notas en las unidades.",
        "example": "85, 87, 89, 91, 93, 95. En la recta hay cinco flechas con +2. Observo que las unidades son 5, 7, 9, 1, 3, 5: siempre impares.",
        "criteria": ["escribe seis números", "mantiene el salto de 2", "dibuja los saltos", "describe lo que se repite en las unidades"],
        "evidence": ["secuencia escrita en el cuaderno", "recta numérica dibujada", "frase de explicación propia"],
        "errors": ["cambiar el salto a mitad de la secuencia", "pasar a números pares sin sumar 2"],
        "feedback": "Reconoce que la secuencia es correcta y pide que revise la diferencia entre vecinos; si hay un error, que sea el propio estudiante quien encuentre dónde cambió el salto.",
    },
    reinforce="Cuenta de 2 en 2 desde 21 con ayuda de tapas: pon dos tapas en cada salto y escribe el número que alcanzas.",
    extend="Busca una secuencia de 2 en 2 que empiece en un impar y pase por 100 sin tocarlo. ¿Es posible? Explica con ejemplos.",
)
