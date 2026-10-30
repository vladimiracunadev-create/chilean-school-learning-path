"""Student material for 2.º básico Matemática, OA 06 (cálculo mental hasta 20) y OA 07 (valor posicional hasta 100)."""
from __future__ import annotations

from student_content_ma02_a import bars
from student_content_ma02_c import KEY
from student_lessons import arith, ex, register

OA6 = "MA02 OA 06"
OA7 = "MA02 OA 07"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def frame(filled: int) -> str:
    """Marco de diez en texto: ● ficha puesta, ○ casilla vacía."""
    return "[" + "●" * filled + "○" * (10 - filled) + "]"


# ------------------------------------------------------------------ OA 06
register(
    OA6, 1,
    materials="Marcos de diez dibujados en este cuaderno (● es una ficha y ○ es una casilla vacía), diez fichas o botones y lápiz. Todas las sumas están escritas en los ejercicios.",
    use="Aprenderé a sumar pasando primero por 10. Sirve para calcular rápido en la cabeza, por ejemplo cuántos lápices hay en total.",
    prior=["Sé qué número falta para llegar a 10.", "Sé sumar hasta 10."],
    explain=[
        "Completar diez es una estrategia para sumar sin contar de uno en uno. Primero llenas un marco de diez. Después sumas lo que sobró. Así trabajas con 10, que es un número muy fácil.",
        f"Mira 8 + 5. El 8 es un marco casi lleno: {frame(8)}. Le faltan 2. Tomas 2 del 5 y los pasas al 8. Ahora el marco tiene 10 y del 5 quedan 3. Entonces 8 + 5 es lo mismo que 10 + 3 = 13.",
        "Para usarla, pregúntate dos cosas. ¿Cuánto le falta al primer número para llegar a 10? Eso lo sacas del segundo número. ¿Cuánto queda? Eso lo sumas a 10. El total no cambia: solo cambias la forma de sumar.",
    ],
    vocab=[("cálculo mental", "calcular en la cabeza, sin contar uno por uno"), ("completar diez", "agregar lo que falta a un número para llegar a 10"), ("estrategia", "un camino que elijo para calcular más fácil"), ("marco de diez", "dibujo de 10 casillas para ordenar fichas"), ("total", "resultado de juntar todas las partes")],
    worked=[
        {"title": "Completar diez con el 8", "problem": f"Calcula 8 + 7. Marco del 8: {frame(8)}.", "steps": ["Al 8 le faltan 2 para llegar a 10.", "Tomo 2 del 7 y quedan 5.", "Ahora sumo 10 + 5 = 15.", "Compruebo contando de 8 en adelante: 9, 10, 11, 12, 13, 14, 15."], "answer": "8 + 7 = 15"},
        {"title": "Completar diez con el 9", "problem": f"Calcula 9 + 6. Marco del 9: {frame(9)}.", "steps": ["Al 9 le falta 1 para llegar a 10.", "Tomo 1 del 6 y quedan 5.", "Sumo 10 + 5 = 15.", "Compruebo: 9 + 6 y 10 + 5 usan las mismas fichas, solo cambié una de lugar."], "answer": "9 + 6 = 15"},
    ],
    mistakes=[
        {"wrong": "Calcular 8 + 6 como 8 + 2 = 10 y luego 10 + 6 = 16.", "why": "Se saca 2 del 6 para llenar el marco, pero después se vuelve a sumar el 6 entero.", "fix": "Después de sacar 2 del 6 quedan 4. Entonces 8 + 6 = 10 + 4 = 14."},
        {"wrong": "Decir que a 7 le faltan 2 para llegar a 10.", "why": "Se cuenta mal lo que falta.", "fix": "Cuenta desde 7 hasta 10: 8, 9, 10. Son 3 números. A 7 le faltan 3."},
    ],
    tiers={
        "recovery": [
            arith(f"Un marco tiene 8 fichas: {frame(8)}. ¿Cuántas fichas faltan para llenarlo?", "10-8", "El marco completo tiene 10 fichas y hay 8."),
            arith("Para calcular 8 + 5 pasas 2 fichas del 5 al 8. Así el 8 llega a 10 y del 5 quedan 3. ¿Cuánto es 10 + 3?", "10+3", "Después de completar diez se suma lo que quedó."),
            ex("Calcula 9 + 3 completando diez. Escribe los dos pasos: 9 + 1 = __ y luego __ + 2 = __.", "9 + 1 = 10 y 10 + 2 = 12", "Del 3 se saca 1 para llenar el 9 y quedan 2."),
        ],
        "understand": [
            ex("¿Cuántas fichas le faltan al número 7 para llegar a 10?", "3", "Desde 7 hasta 10 hay 8, 9 y 10: son 3."),
            ex("En 8 + 6, ¿cuánto hay que sacar del 6 para llenar el marco del 8?", "2", "Al 8 le faltan 2 para ser 10."),
            ex("Ordena los pasos para calcular 8 + 5. A) Sumo 10 + 3. B) Separo 2 del 5 y quedan 3. C) Sumo 8 + 2 = 10. Escribe las letras en orden.", "B, C, A", "Primero se separa, luego se completa diez y al final se suma lo que queda."),
        ],
        "apply": [
            arith("Calcula 8 + 7 completando diez. Escribe el resultado.", "8+2+5", "Se completa 10 con 2 y quedan 5 para sumar."),
            arith("Calcula 9 + 6 completando diez. Escribe el resultado.", "9+1+5", "Se completa 10 con 1 y quedan 5 para sumar."),
            arith("Calcula 7 + 5 completando diez. Al 7 le faltan 3, que se sacan del 5.", "7+3+2", "Se completa 10 con 3 y quedan 2 para sumar."),
        ],
        "reason": [
            ex("Ana calculó 8 + 6 así: 8 + 2 = 10 y 10 + 6 = 16. ¿Qué error cometió y cuál es el resultado correcto?", "Sumó el 6 completo; debía sumar 4. El resultado es 14", "Del 6 ya usó 2, entonces quedan 4 y 10 + 4 = 14."),
            ex("¿Sirve completar diez para calcular 4 + 3? Responde sí o no y di por qué.", "No; la suma es 7 y no llega a 10", "Completar diez se usa cuando la suma pasa de 10; aquí no pasa."),
        ],
        "challenge": [
            ex("Escribe las cuatro sumas 9 + 2, 9 + 3, 9 + 4 y 9 + 5 con sus resultados.", "9 + 2 = 11, 9 + 3 = 12, 9 + 4 = 13, 9 + 5 = 14", "Cada vez se toma 1 del segundo número para llegar a 10 y se suma lo que queda."),
            ex("Si 8 + __ = 15, ¿qué número falta? Piensa: 8 + 2 = 10 y 10 + 5 = 15.", "7", "Se usaron 2 para llegar a 10 y 5 para llegar a 15; 2 + 5 = 7."),
        ],
    },
    context=[arith("Lucía tiene 9 lápices en su estuche. Su hermano le regala 5 más. ¿Cuántos lápices tiene ahora?", "9+5", "Se junta lo que tenía con lo que le regalaron.")],
    selfcheck=[arith("Calcula 8 + 9 completando diez.", "8+9", "Se llena 10 con 2 del 9 y quedan 7."), ex("¿Cuánto le falta a 9 para llegar a 10?", "1", "De 9 a 10 hay un paso."), ex("En 7 + 6, ¿cuánto del 6 se pasa al 7 para formar 10?", "3", "Al 7 le faltan 3 para llegar a 10.")],
    open_task=task(
        "Calcula estas tres sumas completando diez y dibuja un marco de diez para cada una: 9 + 4, 8 + 6 y 7 + 8. Escribe qué pasas de un número al otro y el resultado.",
        "9 + 4: al 9 le falta 1, saco 1 del 4 y quedan 3; 10 + 3 = 13. 8 + 6: al 8 le faltan 2, saco 2 del 6 y quedan 4; 10 + 4 = 14. 7 + 8: al 7 le faltan 3, saco 3 del 8 y quedan 5; 10 + 5 = 15.",
        ["completa diez en cada suma", "dice cuánto pasa y cuánto queda", "obtiene 13, 14 y 15", "dibuja los marcos"],
        ["tres resultados", "marcos dibujados", "pasos escritos"],
        ["sumar el segundo número completo después de completar diez", "equivocarse en lo que le falta a 10"],
        "Pide que cuente en voz alta cuánto le falta al primer número y cuánto queda del segundo; valora la explicación más que la rapidez.",
    ),
    reinforce="Con diez fichas, llena un marco con 8 y pasa fichas desde un montón de 5. Di cuánto quedó en el montón y cuánto da el total.",
    extend="Calcula 9 + 9 y 8 + 9 completando diez y explica cuál es más fácil y por qué.",
)

register(
    OA6, 2,
    materials="Dibujos de puntos dobles hechos en este cuaderno (por ejemplo ●●●  ●●●) y lápiz. Las sumas están escritas en los ejercicios.",
    use="Aprenderé a usar los dobles y las mitades para calcular. Sirve para sumar rápido cuando dos números son iguales o casi iguales.",
    prior=["Sé sumar un número consigo mismo hasta 10 + 10.", "Sé que dos mitades iguales forman un entero."],
    explain=[
        "Un doble es sumar un número consigo mismo. El doble de 6 es 6 + 6 = 12. Es bueno aprender los dobles de memoria, porque ayudan a calcular otras sumas.",
        "Si los números son casi iguales, usa el doble más cercano. En 7 + 8, el 8 es uno más que 7. Calculas 7 + 7 = 14 y agregas 1. Entonces 7 + 8 = 15. También puedes partir del doble de 8, que es 16, y quitar 1: también da 15.",
        "La mitad es lo contrario del doble. La mitad de 14 es 7, porque 7 + 7 = 14. Para hallar la mitad de un número, busca qué número repetido dos veces lo forma. Solo los números pares tienen mitad exacta: 7 no se puede partir en dos partes iguales.",
        "Los dobles y las mitades también sirven para restar. Como 8 + 8 = 16, entonces 16 − 8 = 8. Si sabes el doble, sabes qué pasa al quitar una de las dos partes iguales.",
    ],
    vocab=[("doble", "un número sumado consigo mismo"), ("mitad", "una de las dos partes iguales de un número"), ("casi doble", "suma de dos números seguidos, como 7 + 8"), ("números seguidos", "números que se diferencian en 1, como 7 y 8"), ("dividir en partes iguales", "repartir de modo que cada parte tenga lo mismo")],
    worked=[
        {"title": "Un casi doble", "problem": "Calcula 7 + 8 usando un doble.", "steps": ["Veo que 7 y 8 son números seguidos.", "El doble de 7 es 7 + 7 = 14.", "El 8 es uno más que 7, entonces agrego 1: 14 + 1 = 15.", "Compruebo con el doble de 8: 8 + 8 = 16 y quito 1, también da 15."], "answer": "7 + 8 = 15"},
        {"title": "La mitad de un número", "problem": "¿Cuál es la mitad de 16?", "steps": ["Busco un número que sumado consigo mismo dé 16.", "Pruebo con 7: 7 + 7 = 14, es poco.", "Pruebo con 8: 8 + 8 = 16.", "La mitad de 16 es 8."], "answer": "8"},
    ],
    mistakes=[
        {"wrong": "Decir que 7 + 8 = 14 porque el doble de 7 es 14.", "why": "Se usa el doble pero se olvida que el segundo número es uno más grande.", "fix": "7 + 8 es 7 + 7 y uno más: 14 + 1 = 15."},
        {"wrong": "Decir que la mitad de 12 es 24.", "why": "Se duplica en vez de partir en dos partes iguales.", "fix": "La mitad es lo contrario del doble. Como 6 + 6 = 12, la mitad de 12 es 6."},
    ],
    tiers={
        "recovery": [
            arith("Calcula el doble de 5: 5 + 5.", "5+5", "El doble repite el mismo número dos veces."),
            arith("Calcula el doble de 8: 8 + 8.", "8+8", "El doble de 8 es 16."),
            ex("¿Cuál es la mitad de 12? Piensa en qué número repetido forma 12.", "6", "6 + 6 = 12, entonces la mitad es 6."),
        ],
        "understand": [
            ex("¿Cuál es el doble de 7?", "14", "7 + 7 = 14."),
            ex("7 + 8 está cerca del doble de 7. ¿Cuánto hay que agregar a 7 + 7 para llegar a 7 + 8?", "1", "El 8 es uno más que el 7."),
            ex("¿Verdadero o falso? La mitad de 18 es 8.", "Falso; es 9", "9 + 9 = 18, así que la mitad de 18 es 9."),
        ],
        "apply": [
            arith("Calcula 6 + 7 usando el doble de 6.", "6+6+1", "Se suma el doble de 6 y 1 más."),
            arith("Calcula 9 + 8 usando el doble de 9 y quitando 1.", "9+9-1", "El 8 es uno menos que el 9, entonces se quita 1."),
            arith("Calcula 10 + 9 usando el doble de 10 y quitando 1.", "10+10-1", "El 9 es uno menos que el 10."),
        ],
        "reason": [
            ex("Tomás calculó 8 + 9 = 18 porque el doble de 9 es 18. ¿Qué olvidó y cuál es el resultado correcto?", "Olvidó que 8 es uno menos que 9; el resultado es 17", "18 − 1 = 17, porque 8 es uno menos que 9."),
            ex("El doble de un número es 14. ¿Cuánto es ese número sumado con el número que viene después?", "15", "El número es 7 y 7 + 8 = 15."),
        ],
        "challenge": [
            ex("Escribe una suma de dos números seguidos que dé 17.", "8 + 9 (o 9 + 8)", "8 + 8 = 16 y uno más es 17."),
            arith("Suma el doble de 4 con la mitad de 10. ¿Cuánto da?", "4+4+5", "El doble de 4 es 8 y la mitad de 10 es 5."),
        ],
    },
    context=[arith("En un curso hay 7 niñas y 8 niños. ¿Cuántos estudiantes hay? Usa el doble de 7 y agrega 1.", "7+7+1", "7 y 8 son números seguidos, entonces se usa el doble de 7 y uno más.")],
    selfcheck=[arith("Calcula el doble de 9.", "9+9", "9 + 9 = 18."), ex("¿Cuál es la mitad de 14?", "7", "7 + 7 = 14."), arith("Calcula 8 + 7 usando el doble de 7.", "7+7+1", "8 es uno más que 7.")],
    open_task=task(
        "Calcula 6 + 7, 8 + 9 y 5 + 6 con un doble cercano. Para cada suma escribe el doble que usaste y si agregaste o quitaste 1. Luego busca la mitad de 12, de 16 y de 20.",
        "6 + 7: el doble de 6 es 12 y agrego 1, da 13. 8 + 9: el doble de 8 es 16 y agrego 1, da 17. 5 + 6: el doble de 5 es 10 y agrego 1, da 11. La mitad de 12 es 6, la de 16 es 8 y la de 20 es 10.",
        ["usa un doble en cada suma", "dice si agrega o quita 1", "obtiene 13, 17 y 11", "halla las tres mitades: 6, 8 y 10"],
        ["tres sumas resueltas", "tres mitades", "explicación del doble usado"],
        ["olvidar agregar el 1", "duplicar en lugar de partir en dos al buscar la mitad"],
        "Pide que muestre con dibujo de puntos el doble y el punto extra; reconoce cuando explica por qué sirve el doble cercano.",
    ),
    reinforce="Dibuja filas de puntos iguales para los dobles de 1 a 10 y escribe cada resultado debajo.",
    extend="Calcula 9 + 10 de dos formas: con el doble de 9 y con el doble de 10. Explica por qué dan lo mismo.",
)

register(
    OA6, 3,
    materials="Dos filas de fichas dibujadas con ● en este cuaderno y lápiz. Las sumas están escritas en los ejercicios.",
    use="Aprenderé la estrategia «uno más, uno menos»: sumo 1 a un número y se lo quito al otro. Sirve para cambiar una suma difícil por otra más fácil.",
    prior=["Sé completar diez.", "Sé que una suma puede tener las partes en otro orden."],
    explain=[
        "En una suma puedes pasar una unidad de un número al otro y el total no cambia. Un número sube 1 y el otro baja 1. Es como pasar una ficha de un montón a otro: en total siguen las mismas fichas.",
        "Mira 9 + 5. Si subes el 9 a 10, debes bajar el 5 a 4. Entonces 9 + 5 = 10 + 4 = 14. Los dos lados valen lo mismo. Calcular 10 + 4 es mucho más fácil.",
        "También sirve para hacer un doble. En 6 + 8, subes el 6 a 7 y bajas el 8 a 7. Queda 7 + 7 = 14. Siempre que uno suba y el otro baje la misma cantidad, el total se mantiene.",
    ],
    vocab=[("uno más", "sumar 1 a un número"), ("uno menos", "quitar 1 a un número"), ("compensar", "hacer un cambio y otro contrario para que el total quede igual"), ("total", "lo que da la suma"), ("mantener", "dejar igual, no cambiar")],
    worked=[
        {"title": "Subir el 9 hasta 10", "problem": "Calcula 9 + 6 con «uno más, uno menos».", "steps": ["Subo el 9 a 10: es uno más.", "Bajo el 6 a 5: es uno menos.", "Calculo 10 + 5 = 15.", "El total no cambió, entonces 9 + 6 = 15."], "answer": "9 + 6 = 15"},
        {"title": "Formar un doble", "problem": "Calcula 6 + 8 haciendo un doble.", "steps": ["Subo el 6 a 7: uno más.", "Bajo el 8 a 7: uno menos.", "Ahora tengo 7 + 7 = 14.", "Entonces 6 + 8 = 14."], "answer": "6 + 8 = 14"},
    ],
    mistakes=[
        {"wrong": "Cambiar 9 + 4 por 10 + 4 y decir que da 14.", "why": "Se sube un número pero no se baja el otro, y el total cambia.", "fix": "Si el 9 sube a 10, el 4 baja a 3. Entonces 9 + 4 = 10 + 3 = 13."},
        {"wrong": "Subir los dos números: cambiar 8 + 6 por 9 + 7.", "why": "Los dos suben y el total aumenta en 2.", "fix": "Uno sube y el otro baja: 8 + 6 = 9 + 5."},
    ],
    tiers={
        "recovery": [
            ex("En 9 + 5, el 9 sube a 10. ¿A qué número baja el 5 para que el total no cambie?", "4", "Si uno sube 1, el otro baja 1."),
            arith("Cambia 9 + 6 por 10 + 5. Calcula 10 + 5.", "10+5", "Es una suma fácil que da lo mismo que 9 + 6."),
            ex("En 8 + 7 el 8 sube a 9. ¿Qué suma queda?", "9 + 6", "El 7 baja a 6 para mantener el total."),
        ],
        "understand": [
            ex("¿Cuál suma da lo mismo que 8 + 6: 9 + 5 o 9 + 6?", "9 + 5", "Si el 8 sube 1, el 6 debe bajar 1."),
            ex("En 7 + 7, un número sube 1 y el otro baja 1. ¿Qué suma queda?", "8 + 6", "7 sube a 8 y 7 baja a 6."),
            ex("¿Verdadero o falso? 9 + 5 y 10 + 5 dan el mismo total.", "Falso; dan 14 y 15", "En 10 + 5 solo subió un número, y el total subió."),
        ],
        "apply": [
            arith("Calcula 9 + 7 cambiándola por 10 + 6.", "10+6", "El 9 sube 1 y el 7 baja 1."),
            arith("Calcula 9 + 8 cambiándola por 10 + 7.", "10+7", "El 9 sube 1 y el 8 baja 1."),
            arith("Convierte 6 + 8 en un doble (7 + 7) y calcula el total.", "7+7", "El 6 sube 1 y el 8 baja 1, y el total se mantiene."),
        ],
        "reason": [
            ex("Rosa escribió 9 + 4 = 10 + 4. ¿Qué error cometió y cuál es el resultado correcto?", "Subió el 9 y no bajó el 4; el resultado es 13", "Debía ser 10 + 3 = 13."),
            ex("Si 12 + 5 se cambia por 13 + __ para que el total no cambie, ¿qué número va?", "4", "El 12 subió 1, entonces el 5 baja a 4."),
        ],
        "challenge": [
            ex("Escribe dos sumas distintas que den lo mismo que 7 + 9, usando «uno más, uno menos» una o dos veces.", "8 + 8 y 6 + 10 (también 5 + 11)", "7 + 9 = 16 y cada cambio de uno más y uno menos conserva 16."),
            arith("Empiezas con 9 + 9. Subes un número 1 y bajas el otro 1, y lo haces dos veces seguidas (la primera vez llegas a 10 + 8). ¿Cuánto es el total al final?", "11+7", "9 + 9 pasa a 10 + 8 y luego a 11 + 7; el total siempre es 18."),
        ],
    },
    context=[arith("Pedro tiene 9 canicas rojas y 6 azules. Cambia el cálculo por 10 + 5. ¿Cuántas canicas tiene en total?", "10+5", "Pasar una canica de un grupo al otro no cambia el total.")],
    selfcheck=[arith("Calcula 9 + 9 cambiándola por 10 + 8.", "10+8", "El 9 sube 1 y el otro 9 baja 1."), ex("¿Qué suma da lo mismo que 7 + 8: 8 + 7 o 8 + 8?", "8 + 7", "Cambia el orden pero el total es el mismo; en 8 + 8 solo un número cambió."), ex("En 6 + 8 haces un doble. ¿Cuál es?", "7 + 7", "6 sube a 7 y 8 baja a 7.")],
    open_task=task(
        "Resuelve 9 + 7, 9 + 5 y 6 + 10 con «uno más, uno menos». Para cada una escribe la suma nueva que formaste y su resultado. Después explica con una frase por qué el total no cambia.",
        "9 + 7 = 10 + 6 = 16. 9 + 5 = 10 + 4 = 14. 6 + 10 = 7 + 9 = 16 (otra forma correcta: 5 + 11 = 16). El total no cambia porque lo que sube un número lo baja el otro.",
        ["sube un número y baja el otro en cada suma", "obtiene 16, 14 y 16", "explica por qué el total no cambia"],
        ["sumas nuevas escritas", "resultados", "explicación en una frase"],
        ["subir solo un número", "subir los dos números"],
        "Pide que muestre la ficha que pasa de un grupo al otro con un dibujo; reconoce la explicación del total constante.",
    ),
    reinforce="Con 15 fichas, forma dos montones de 9 y 6. Pasa una ficha de un montón al otro y comprueba que el total sigue siendo 15.",
    extend="Escribe cuatro sumas distintas que den 14 pasando una unidad cada vez.",
)

register(
    OA6, 4,
    materials="Fichas dibujadas con ● en este cuaderno y lápiz. Las sumas están escritas en los ejercicios.",
    use="Aprenderé la estrategia «dos más, dos menos»: sumo 2 a un número y le quito 2 al otro. Sirve para llegar a 10 aunque falten dos.",
    prior=["Sé la estrategia «uno más, uno menos».", "Sé cuánto le falta a un número para llegar a 10."],
    explain=[
        "«Dos más, dos menos» es como «uno más, uno menos», pero pasas 2 unidades de un número al otro. Un número sube 2 y el otro baja 2. El total queda igual.",
        "Se usa cuando a un número le faltan 2 para llegar a 10. En 8 + 4, al 8 le faltan 2. Subes el 8 a 10 y bajas el 4 a 2. Entonces 8 + 4 = 10 + 2 = 12. Puedes comprobarlo con doce fichas: 8 y 4, o 10 y 2.",
        "Cuando falta 1 usas «uno más, uno menos». Cuando faltan 2 usas «dos más, dos menos». Mira bien cuánto falta antes de elegir la estrategia.",
    ],
    vocab=[("dos más", "sumar 2 a un número"), ("dos menos", "quitar 2 a un número"), ("pasar unidades", "mover fichas de un número al otro"), ("elegir una estrategia", "decidir qué camino sirve mejor para esa suma"), ("comprobar", "revisar que el resultado sea correcto")],
    worked=[
        {"title": "Pasar 2 para llegar a 10", "problem": "Calcula 8 + 5 con «dos más, dos menos».", "steps": ["Al 8 le faltan 2 para 10: lo subo 2.", "Bajo el 5 en 2: queda 3.", "Calculo 10 + 3 = 13.", "Compruebo con 13 fichas: 8 y 5, o 10 y 3."], "answer": "8 + 5 = 13"},
        {"title": "Formar un doble con dos de diferencia", "problem": "Calcula 6 + 10 pasando 2 de un número al otro.", "steps": ["Bajo el 10 en 2: queda 8.", "Subo el 6 en 2: queda 8.", "Obtengo el doble 8 + 8 = 16.", "Entonces 6 + 10 = 16."], "answer": "6 + 10 = 16"},
    ],
    mistakes=[
        {"wrong": "Cambiar 8 + 4 por 10 + 4 y decir que da 14.", "why": "Se sube el 8 en 2 y no se baja el otro número.", "fix": "Si el 8 sube 2, el 4 baja 2: 8 + 4 = 10 + 2 = 12."},
        {"wrong": "Bajar 1 al otro número cuando el primero sube 2.", "why": "La cantidad que sube y la que baja deben ser iguales.", "fix": "Si uno sube 2, el otro baja 2."},
    ],
    tiers={
        "recovery": [
            ex("En 8 + 4, el 8 sube 2 y llega a 10. ¿A qué número baja el 4?", "2", "Si uno sube 2, el otro baja 2."),
            arith("Cambia 8 + 6 por 10 + 4. Calcula 10 + 4.", "10+4", "El 8 sube 2 y el 6 baja 2."),
            ex("¿Cuánto le falta a 8 para llegar a 10?", "2", "De 8 a 10 hay 9 y 10: son 2."),
        ],
        "understand": [
            ex("¿Cuál suma da lo mismo que 8 + 7: 10 + 5 o 10 + 7?", "10 + 5", "El 8 sube 2, entonces el 7 baja 2."),
            ex("Para 9 + 4, ¿qué estrategia sirve más: uno más, uno menos, o dos más, dos menos?", "Uno más, uno menos", "Al 9 solo le falta 1 para llegar a 10."),
            ex("Para 8 + 9, ¿cuánto sube el 8 para llegar a 10?", "2", "Al 8 le faltan 2 y el 9 baja 2."),
        ],
        "apply": [
            arith("Calcula 8 + 5 cambiándola por 10 + 3.", "10+3", "El 8 sube 2 y el 5 baja 2."),
            arith("Calcula 8 + 8 cambiándola por 10 + 6.", "10+6", "El 8 sube 2 y el otro 8 baja 2."),
            arith("Calcula 6 + 10 convirtiéndola en el doble 8 + 8.", "8+8", "El 6 sube 2 y el 10 baja 2."),
        ],
        "reason": [
            ex("Sofía cambió 8 + 4 por 10 + 4. ¿Por qué el total cambió y cuánto debía ser?", "Subió el 8 sin bajar el 4; debía ser 10 + 2 = 12", "El total subió en 2: 14 y no 12."),
            ex("Camilo dice que 8 + 6 y 10 + 4 dan lo mismo. ¿Tiene razón?", "Sí; ambas dan 14", "El 8 subió 2 y el 6 bajó 2."),
        ],
        "challenge": [
            ex("Parte de 7 + 9. Primero sube el 7 en 2 y baja el 9 en 2. Después baja el 7 en 2 y sube el 9 en 2. Escribe las dos sumas nuevas.", "9 + 7 y 5 + 11", "7 + 9 = 16, 9 + 7 = 16 y 5 + 11 = 16."),
            arith("Empiezas con 8 + 4 y pasas 2 unidades de un número al otro, una vez. ¿Cuál es el total de la nueva suma?", "8+4", "Pasar unidades no cambia el total, que siempre es 12."),
        ],
    },
    context=[arith("En la caja hay 8 lápices azules y 5 rojos. Se pasan 2 rojos a los azules para tener 10 + 3. ¿Cuántos lápices hay en total?", "10+3", "Pasar lápices de un grupo al otro no cambia el total.")],
    selfcheck=[arith("Calcula 8 + 7 cambiándola por 10 + 5.", "10+5", "El 8 sube 2 y el 7 baja 2."), ex("¿Cuánto debe bajar el 6 si el 8 sube 2?", "2", "Lo que sube un número lo baja el otro."), arith("Calcula 8 + 9 con dos más, dos menos.", "10+7", "El 8 sube 2 y el 9 baja 2.")],
    open_task=task(
        "Resuelve 8 + 6, 8 + 7 y 8 + 9 con «dos más, dos menos». Para cada una escribe la suma nueva y el resultado. Luego dibuja 14 fichas como 8 y 6, y como 10 y 4.",
        "8 + 6 = 10 + 4 = 14. 8 + 7 = 10 + 5 = 15. 8 + 9 = 10 + 7 = 17. Dibujo: ●●●●●●●● ●●●●●● y ●●●●●●●●●● ●●●●; las 14 fichas están en los dos dibujos.",
        ["pasa 2 de un número al otro", "obtiene 14, 15 y 17", "dibuja los dos arreglos de 14"],
        ["sumas nuevas", "resultados", "dibujo"],
        ["subir sin bajar", "pasar distinta cantidad de un lado y del otro"],
        "Pide que cuente las fichas de ambos dibujos para comprobar que son 14; reconoce la comparación.",
    ),
    reinforce="Con 12 fichas, forma 8 y 4. Pasa 2 fichas de un grupo al otro y comprueba que sigues teniendo 12.",
    extend="Explica cuándo conviene «uno más, uno menos» y cuándo «dos más, dos menos», con un ejemplo de cada una.",
)

register(
    OA6, 5,
    materials="Hojas de papel con casillas dibujadas, lápiz y botones o fichas. Todas las restas están escritas en los ejercicios.",
    use="Aprenderé a restar pensando en una suma que falta. Sirve para calcular rápido cuánto falta o cuánto queda sin quitar de uno en uno.",
    prior=["Sé sumar hasta 20.", "Sé que sumar y restar son operaciones que se relacionan."],
    explain=[
        "La resta y la suma se deshacen entre sí. Eso se llama reversibilidad. Si sabes sumar, puedes restar: en vez de quitar, preguntas qué número falta para llegar al total.",
        "Mira 15 − 7. Piensa: 7 más, ¿cuánto, para llegar a 15? Parte de 7 y completa: 7 + 3 = 10 y 10 + 5 = 15. Agregaste 3 y 5, que son 8. Entonces 15 − 7 = 8.",
        "Para comprobar, haces el camino inverso: 7 + 8 = 15. Si la suma vuelve al número grande, la resta está bien. Esto sirve para revisar cualquier resta.",
    ],
    vocab=[("reversibilidad", "la suma y la resta se deshacen entre sí"), ("resta", "quitar o hallar cuánto falta"), ("completar", "agregar hasta llegar a un número"), ("diferencia", "resultado de una resta"), ("comprobar", "revisar con la operación contraria")],
    worked=[
        {"title": "Restar completando", "problem": "Calcula 15 − 7 pensando en una suma.", "steps": ["Pregunto: 7 + ¿cuánto? = 15.", "Desde 7 agrego 3 y llego a 10.", "Desde 10 agrego 5 y llego a 15.", "Agregué 3 + 5 = 8. Compruebo: 7 + 8 = 15."], "answer": "15 − 7 = 8"},
        {"title": "Restar 9 de un número", "problem": "Calcula 17 − 9 pensando en una suma.", "steps": ["Pregunto: 9 + ¿cuánto? = 17.", "Desde 9 agrego 1 y llego a 10.", "Desde 10 agrego 7 y llego a 17.", "Agregué 1 + 7 = 8. Compruebo: 9 + 8 = 17."], "answer": "17 − 9 = 8"},
    ],
    mistakes=[
        {"wrong": "Calcular 13 − 5 como 13 + 5 = 18.", "why": "Se confunde la operación: en vez de hallar lo que falta, se suma.", "fix": "Pregunta 5 + ¿cuánto? = 13. Falta 8, entonces 13 − 5 = 8."},
        {"wrong": "Responder 12 − 4 = 9 sin revisar.", "why": "No se comprueba con la suma contraria.", "fix": "Comprueba: 4 + 9 = 13, no 12. La respuesta correcta es 8, porque 4 + 8 = 12."},
    ],
    tiers={
        "recovery": [
            arith("Calcula 4 + 4. Luego responde cuánto es 8 − 4 sabiendo que se deshace la suma.", "8-4", "Si 4 + 4 = 8, al quitar 4 de 8 vuelve el otro 4."),
            ex("Para calcular 10 − 3 pregunta: 3 + ¿cuánto? = 10. ¿Cuánto es?", "7", "3 + 7 = 10."),
            ex("Para calcular 12 − 5 pregunta: 5 + ¿cuánto? = 12. ¿Cuánto es?", "7", "5 + 7 = 12."),
        ],
        "understand": [
            ex("Si 6 + 8 = 14, ¿cuánto es 14 − 6?", "8", "La resta deshace la suma."),
            ex("¿Qué suma sirve para calcular 16 − 9: 9 + __ = 16 o 16 + 9 = __?", "9 + __ = 16", "La resta pregunta cuánto falta para llegar al número grande."),
            ex("¿Qué suma comprueba que 13 − 8 = 5?", "5 + 8 = 13", "La suma contraria debe volver al número grande."),
        ],
        "apply": [
            arith("Calcula 13 − 8 pensando 8 + ¿cuánto? = 13.", "13-8", "Desde 8 se agregan 2 para 10 y 3 más para 13: son 5."),
            arith("Calcula 17 − 9 pensando 9 + ¿cuánto? = 17.", "17-9", "Desde 9 se agrega 1 para 10 y 7 más para 17: son 8."),
            arith("Calcula 16 − 7 pensando 7 + ¿cuánto? = 16.", "16-7", "Desde 7 se agregan 3 para 10 y 6 más para 16: son 9."),
        ],
        "reason": [
            ex("Marta dice que 12 − 5 = 6. ¿Cómo puedes comprobar si está bien y cuál es el resultado correcto?", "Compruebo 5 + 6 = 11, que no es 12; el resultado es 7", "5 + 7 = 12, entonces 12 − 5 = 7."),
            ex("¿Por qué 9 + 6 = 15 ayuda a saber que 15 − 6 = 9?", "Porque la resta deshace la suma y vuelve a una de las partes", "Quitar 6 de 15 deja la otra parte, que es 9."),
        ],
        "challenge": [
            ex("Escribe una resta con diferencia 8 y número grande 17, y su comprobación con suma.", "17 − 9 = 8; 9 + 8 = 17", "9 + 8 = 17, entonces 17 − 9 = 8."),
            arith("Si 5 + 14 = 19, ¿cuánto es 19 − 14?", "19-14", "Restar una parte del total deja la otra parte."),
        ],
    },
    context=[arith("Hay 15 vasos sobre la mesa. 7 son rojos y el resto son azules. ¿Cuántos son azules?", "15-7", "Se busca cuánto falta de 7 para llegar a 15.")],
    selfcheck=[arith("Calcula 14 − 6 pensando 6 + ¿cuánto? = 14.", "14-6", "6 + 8 = 14."), ex("¿Qué suma comprueba que 18 − 9 = 9?", "9 + 9 = 18", "La suma contraria vuelve a 18."), arith("Calcula 11 − 8.", "11-8", "8 + 3 = 11.")],
    open_task=task(
        "Calcula 15 − 8, 13 − 5 y 18 − 9 pensando en una suma. Para cada una escribe la pregunta «__ + ¿cuánto? = __», el resultado y la suma que comprueba.",
        "15 − 8: 8 + ¿cuánto? = 15, falta 7; comprobación 8 + 7 = 15. 13 − 5: 5 + ¿cuánto? = 13, falta 8; comprobación 5 + 8 = 13. 18 − 9: 9 + ¿cuánto? = 18, falta 9; comprobación 9 + 9 = 18.",
        ["escribe la suma que falta en cada resta", "obtiene 7, 8 y 9", "escribe la comprobación con suma"],
        ["tres preguntas escritas", "resultados", "comprobaciones"],
        ["sumar en vez de restar", "no comprobar con la suma contraria"],
        "Pide que explique en voz alta por qué la suma comprueba la resta; valora la conexión entre ambas operaciones.",
    ),
    reinforce="Con 14 fichas, quita 6 y cuenta cuántas quedan. Luego junta de nuevo y comprueba que 6 + las que quedaron vuelve a 14.",
    extend="Escribe tres restas con número grande 16 y comprueba cada una con una suma.",
)

# ------------------------------------------------------------------ OA 07
register(
    OA7, 1,
    materials=f"Paquetes y palitos dibujados en este cuaderno, diez palitos de helado o lápices. {KEY}",
    use="Aprenderé que 10 unidades sueltas se pueden cambiar por una decena. Sirve para contar cantidades grandes y escribirlas con orden.",
    prior=["Sé contar hasta 100.", "Sé qué es agrupar objetos de 10 en 10."],
    explain=[
        "Diez unidades forman una decena. Una decena es un paquete de 10. Si tienes 10 palitos sueltos, los puedes atar y quedan convertidos en 1 paquete. Esto se llama canje.",
        f"El canje no cambia la cantidad. Solo cambia la forma de mirarla. Mira 14 palitos sueltos: {'● ' * 14}. Cambias 10 sueltos por un paquete y queda {bars(14)}. Es decir, 1 decena y 4 unidades. Siguen siendo 14 palitos.",
        "Si juntas 10 unidades o más, puedes hacer un canje. Si tienes menos de 10, no alcanzan para una decena. Así 26 palitos son 2 decenas y 6 unidades: 2 paquetes de 10 y 6 sueltos.",
    ],
    vocab=[("unidad", "un objeto suelto"), ("decena", "paquete de 10 unidades"), ("canje", "cambiar 10 unidades por 1 decena, o 1 decena por 10 unidades"), ("paquete", "grupo de 10 atados juntos"), ("cantidad", "cuántos objetos hay")],
    worked=[
        {"title": "Canjear 10 sueltos", "problem": "Tienes 13 palitos sueltos. ¿Cuántas decenas y unidades tienes después del canje?", "steps": ["Cuento 10 palitos sueltos y los ato en un paquete.", "Queda 1 paquete y 3 sueltos.", "Es 1 decena y 3 unidades.", "Compruebo: 10 + 3 = 13."], "answer": "1 decena y 3 unidades"},
        {"title": "Hacer todos los paquetes", "problem": "Tienes 26 palitos sueltos. Haz todos los paquetes de 10 que puedas.", "steps": ["Con 26 hago un paquete (10) y otro (20).", "Para un tercero faltarían 4; no alcanzan.", "Quedan 2 paquetes y 6 sueltos.", "Compruebo: 20 + 6 = 26."], "answer": "2 decenas y 6 unidades"},
    ],
    mistakes=[
        {"wrong": "Decir que 10 unidades son 10 decenas.", "why": "Se confunde cuántos objetos hay con cuántos paquetes se forman.", "fix": "Diez unidades forman 1 decena. Diez decenas serían 100 unidades."},
        {"wrong": "Pensar que al hacer el canje hay menos palitos.", "why": "Se cree que atar cambia la cantidad.", "fix": "Atar no quita nada: 13 sueltos o 1 paquete y 3 sueltos son 13 palitos."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuántas unidades forman 1 decena?", "10", "Una decena es un paquete de 10 unidades."),
            ex("Tienes 10 palitos sueltos y los atas en un paquete. ¿Cuántos paquetes de 10 tienes?", "1 paquete (1 decena)", "Diez sueltos forman un paquete."),
            ex(f"Cuenta el dibujo: {bars(24)}. ¿Cuántas decenas y cuántas unidades hay?", "2 decenas y 4 unidades", "Hay 2 barras de 10 y 4 cubos sueltos."),
        ],
        "understand": [
            ex("Tienes 14 palitos sueltos. Atas 10. ¿Cuántas decenas y unidades tienes?", "1 decena y 4 unidades", "Diez quedan atados y 4 siguen sueltos."),
            ex("¿Cuántas unidades hay en 3 decenas?", "30", "Cada decena tiene 10 unidades: 10 + 10 + 10 = 30."),
            ex("¿Qué número es 2 decenas y 7 unidades?", "27", "Dos paquetes de 10 son 20 y 7 sueltos son 27."),
        ],
        "apply": [
            ex("Tienes 26 palitos sueltos. Si haces todos los paquetes de 10 que puedes, ¿cuántos paquetes y cuántos sueltos quedan?", "2 paquetes y 6 sueltos", "En 26 caben 2 grupos de 10 y sobran 6."),
            ex("Escribe 58 en decenas y unidades.", "5 decenas y 8 unidades", "En 58, el 5 está en las decenas y el 8 en las unidades."),
            arith("Tienes 4 paquetes de 10 y 15 palitos sueltos. ¿Cuántos palitos hay en total?", "10+10+10+10+15", "Cuatro paquetes son 40 y se suman 15 sueltos."),
        ],
        "reason": [
            ex("Mati dice: «Con 10 unidades sueltas tengo 1 decena y además sigo teniendo 10 unidades». ¿Tiene razón?", "No; las 10 unidades se cambiaron por la decena", "El canje no cambia la cantidad, solo la forma de agruparla."),
            ex("Hay 3 paquetes de 10 y 11 palitos sueltos. Sofía dice que se puede hacer un canje. ¿Cuántas decenas y unidades quedan después?", "4 decenas y 1 unidad", "Con 10 sueltos se hace otra decena y queda 1 suelto."),
        ],
        "challenge": [
            ex("¿Cuántos paquetes de 10 se forman con 90 palitos sueltos?", "9", "Cada paquete usa 10 palitos: de 10 en 10 se llega a 90 con 9 paquetes."),
            ex("Tienes 7 paquetes de 10 y 3 sueltos. Ganas 10 sueltos más y los atas. ¿Cuántas decenas y unidades tienes?", "8 decenas y 3 unidades", "Los 10 sueltos forman una decena más: 7 + 1 = 8."),
        ],
    },
    context=[ex("En un kiosco hay 36 caramelos sueltos. Los guardan en bolsas de 10. ¿Cuántas bolsas llenas y cuántos caramelos sueltos quedan?", "3 bolsas y 6 caramelos", "En 36 caben 3 grupos de 10 y sobran 6.")],
    selfcheck=[ex("¿Cuántas decenas se forman con 10 unidades?", "1", "Diez unidades hacen una decena."), ex("¿Qué número es 3 decenas y 5 unidades?", "35", "30 y 5 son 35."), ex("Tienes 17 palitos sueltos. ¿Cuántas decenas y unidades son?", "1 decena y 7 unidades", "Diez se atan y quedan 7 sueltos.")],
    open_task=task(
        "Tienes 43, 20 y 18 palitos sueltos. Para cada cantidad ata todos los paquetes de 10 posibles, dibújalos con ▮ y ●, y escribe cuántas decenas y unidades quedan.",
        "43: " + bars(43) + " son 4 decenas y 3 unidades. 20: " + bars(20) + " son 2 decenas y 0 unidades. 18: " + bars(18) + " son 1 decena y 8 unidades.",
        ["dibuja paquetes de 10 y sueltos", "escribe 4D 3U, 2D 0U y 1D 8U", "explica que el canje no cambia la cantidad"],
        ["tres dibujos", "tres escrituras en decenas y unidades"],
        ["contar un paquete como una unidad", "dejar 10 o más sueltos sin canjear"],
        "Pide que cuente en voz alta de 10 en 10 los paquetes y luego de 1 en 1 los sueltos; confirma el total.",
    ),
    reinforce="Con 25 palitos de helado, haz paquetes de 10 con cinta de papel. Cuenta cuántos paquetes y cuántos sueltos quedan.",
    extend="Escribe tres números de dos cifras que tengan 5 unidades y cuéntalos en paquetes y sueltos.",
)

register(
    OA7, 2,
    materials=f"Tablas D-U dibujadas en este cuaderno (D es decenas y U es unidades) y lápiz. {KEY}",
    use="Aprenderé a leer y escribir números en una tabla de decenas y unidades. Sirve para saber qué cifra vale más y no confundir 47 con 74.",
    prior=["Sé que 10 unidades forman 1 decena.", "Sé escribir números de dos cifras."],
    explain=[
        "Una tabla DU tiene dos columnas. La de la izquierda es D, de decenas. La de la derecha es U, de unidades. Cada cifra se escribe en su columna. La posición dice cuánto vale cada cifra.",
        "Para el número 47, escribes 4 en D y 7 en U. Se lee: 4 decenas y 7 unidades. Si cambias de lugar las cifras, escribes 7 en D y 4 en U. Eso es 74. No es el mismo número, porque 7 decenas es más que 4 decenas.",
        "Para armar un número desde la tabla, pones las decenas primero y las unidades después. Para pasar un número a la tabla, la cifra de la izquierda va en D y la de la derecha en U. Si hay 0 unidades, se escribe 0 en U.",
    ],
    vocab=[("tabla DU", "cuadro con una columna de decenas y otra de unidades"), ("columna", "fila vertical de la tabla"), ("posición", "el lugar donde está una cifra"), ("cifra", "cada número que forma un número, como 4 y 7 en 47"), ("decena", "grupo de 10")],
    worked=[
        {"title": "De número a tabla", "problem": "Escribe 47 en una tabla DU.", "steps": ["La cifra de la izquierda es 4: va en D.", "La cifra de la derecha es 7: va en U.", "La tabla queda así: D = 4 y U = 7.", "Se lee: 4 decenas y 7 unidades."], "answer": "D = 4, U = 7"},
        {"title": "Contrastar 47 y 74", "problem": "Una tabla dice D = 7 y U = 4. ¿Qué número es y en qué se diferencia de 47?", "steps": ["D = 7 son 7 decenas, es decir 70.", "U = 4 son 4 unidades.", "El número es 74.", "47 tiene 4 decenas; 74 tiene 7 decenas, por eso 74 es mayor."], "answer": "74; es mayor que 47"},
    ],
    mistakes=[
        {"wrong": "Escribir 5 decenas y 3 unidades como 35.", "why": "Se pone la cifra de las unidades en la columna de las decenas.", "fix": "Las decenas se escriben a la izquierda: 5 decenas y 3 unidades es 53."},
        {"wrong": "Escribir 4 decenas y 0 unidades como 4.", "why": "Se omite el 0 de las unidades.", "fix": "El 0 mantiene la posición: 4 decenas y 0 unidades es 40."},
    ],
    tiers={
        "recovery": [
            ex("En una tabla DU, ¿la columna de la izquierda es D o U?", "D", "Las decenas siempre van a la izquierda."),
            ex("Una tabla dice D = 6 y U = 2. ¿Qué número es?", "62", "6 decenas y 2 unidades se escriben 62."),
            ex("Escribe 35 en una tabla DU: ¿qué cifra va en D y cuál en U?", "D = 3 y U = 5", "La cifra de la izquierda va en D."),
        ],
        "understand": [
            ex("Una tabla dice D = 8 y U = 1. ¿Cuántas decenas y cuántas unidades tiene el número?", "8 decenas y 1 unidad", "Se lee cada columna por separado."),
            ex("¿Qué número es mayor, el que tiene D = 5 y U = 9, o el que tiene D = 6 y U = 0?", "El de D = 6 y U = 0, que es 60", "60 > 59 porque 6 decenas es más que 5 decenas."),
            ex("¿Qué número escribes con 9 decenas y 0 unidades?", "90", "El 0 mantiene el 9 en las decenas."),
        ],
        "apply": [
            ex("Escribe en una tabla DU el número 72.", "D = 7 y U = 2", "El 7 está a la izquierda y el 2 a la derecha."),
            ex("Una tabla dice D = 2 y U = 8. Escribe el número y cómo se lee en palabras.", "28; veintiocho", "2 decenas y 8 unidades forman 28."),
            ex("Con las cifras 3 y 6 puedes escribir dos números. Escríbelos de menor a mayor.", "36 y 63", "Con 3 decenas es 36 y con 6 decenas es 63."),
        ],
        "reason": [
            ex("Dani escribió 4 decenas y 7 unidades como 74. ¿Qué error cometió y cuál es el número correcto?", "Puso las unidades en la columna de las decenas; el número es 47", "4 decenas y 7 unidades es 40 + 7 = 47."),
            ex("¿Por qué 47 y 74 son números distintos si tienen las mismas cifras?", "Porque la posición cambia cuánto vale cada cifra", "En 47, el 4 vale 40; en 74, el 4 vale 4."),
        ],
        "challenge": [
            ex("Un número de dos cifras tiene el doble de decenas que unidades y sus unidades son 3. ¿Cuál es?", "63", "El doble de 3 es 6, entonces hay 6 decenas y 3 unidades."),
            ex("Con las cifras 2, 5 y 8 formas números de dos cifras sin repetir ninguna cifra. ¿Cuáles son el menor y el mayor?", "25 y 85", "El menor empieza con 2 decenas y 5 unidades; el mayor, con 8 decenas y 5 unidades."),
        ],
    },
    context=[ex("Un bus tiene el número 38. Escribe cuántas decenas y cuántas unidades tiene el número del bus.", "3 decenas y 8 unidades", "En 38, el 3 está en las decenas y el 8 en las unidades.")],
    selfcheck=[ex("En la tabla DU, ¿dónde va la cifra 6 del número 61?", "En D", "Es la cifra de la izquierda."), ex("Una tabla dice D = 4 y U = 0. ¿Qué número es?", "40", "4 decenas y ninguna unidad es 40."), ex("¿Qué número es mayor, 52 o 25?", "52", "5 decenas es más que 2 decenas.")],
    open_task=task(
        "Escribe en una tabla DU los números 83, 38 y 60. Para cada uno dibuja las barras y cubos con ▮ y ●, y explica en una frase por qué 83 y 38 son distintos.",
        "83: D = 8, U = 3. " + bars(83) + ". 38: D = 3, U = 8. " + bars(38) + ". 60: D = 6, U = 0. " + bars(60) + ". 83 y 38 son distintos porque en 83 el 8 vale 80 y en 38 el 8 vale solo 8.",
        ["coloca bien las cifras en D y U", "dibuja las barras y cubos", "explica con la posición de la cifra"],
        ["tres tablas", "tres dibujos", "frase de explicación"],
        ["invertir las columnas", "olvidar el 0 de las unidades"],
        "Pide que lea cada tabla en voz alta diciendo «decenas» y «unidades»; reconoce el uso de la posición.",
    ),
    reinforce="En una tarjeta escribe D y U. Arma con dos cifras dos números distintos y léelos en decenas y unidades.",
    extend="Con las cifras 4 y 9 forma los dos números posibles y explica cuál es mayor y por qué.",
)

register(
    OA7, 3,
    materials=f"Barras y cubos dibujados en este cuaderno y lápiz. {KEY}",
    use="Aprenderé cuánto vale cada cifra según su lugar. Sirve para entender por qué el 5 de 52 vale mucho más que el 5 de 25.",
    prior=["Sé escribir números en una tabla DU.", "Sé descomponer un número en decenas y unidades."],
    explain=[
        "Una misma cifra puede valer distinto según su posición. Esto se llama valor posicional. En la columna de las decenas, cada cifra cuenta de 10 en 10. En la de las unidades, vale lo que marca.",
        f"Mira 55. El primer 5 está en D y vale 50. El segundo 5 está en U y vale 5. Se ve en el dibujo: {bars(55)}. Son 5 barras de 10 y 5 cubos de 1. Entonces 55 = 50 + 5.",
        "Para saber el valor de una cifra, primero fíjate en su posición. En 73, el 7 vale 70 y el 3 vale 3. En 37, el 3 vale 30 y el 7 vale 7. Los mismos números valen distinto porque cambiaron de lugar.",
    ],
    vocab=[("valor posicional", "lo que vale una cifra según el lugar donde está"), ("valor", "cuánto vale una cifra en un número"), ("descomponer", "separar un número en sus partes, como 50 + 5"), ("cifra", "cada número que forma un número"), ("posición", "el lugar de una cifra")],
    worked=[
        {"title": "Dos cifras iguales", "problem": "En el número 55, ¿cuánto vale cada 5?", "steps": ["El primer 5 está en D: son 5 decenas, es decir 50.", "El segundo 5 está en U: son 5 unidades, es decir 5.", f"Lo veo en el dibujo: {bars(55)}.", "Compruebo: 50 + 5 = 55."], "answer": "Un 5 vale 50 y el otro vale 5"},
        {"title": "Mismas cifras, distinto lugar", "problem": "¿Cuánto vale el 3 en 37 y en 73?", "steps": ["En 37, el 3 está en D: vale 30.", "En 73, el 3 está en U: vale 3.", "El valor de la cifra depende del lugar.", "30 es mucho más que 3."], "answer": "En 37 vale 30 y en 73 vale 3"},
    ],
    mistakes=[
        {"wrong": "Decir que el 6 de 62 vale 6.", "why": "Se lee la cifra sin mirar su posición.", "fix": "El 6 está en las decenas, entonces vale 60."},
        {"wrong": "Pensar que los dos 4 de 44 valen lo mismo.", "why": "Se olvida que la posición cambia el valor.", "fix": "El primer 4 vale 40 y el segundo vale 4."},
    ],
    tiers={
        "recovery": [
            ex("En el número 62, ¿cuánto vale el 6?", "60", "Está en las decenas: 6 decenas son 60."),
            ex("En el número 26, ¿cuánto vale el 6?", "6", "Está en las unidades."),
            ex("En el número 40, ¿cuánto vale el 4?", "40", "Está en las decenas: 4 decenas son 40."),
        ],
        "understand": [
            ex("En 55, ¿vale lo mismo el primer 5 y el segundo 5?", "No; el primero vale 50 y el segundo 5", "La posición cambia el valor."),
            ex("En 38, ¿cuánto vale cada cifra?", "El 3 vale 30 y el 8 vale 8", "El 3 está en D y el 8 en U."),
            ex("¿Cuál es la cifra de las decenas de 94?", "9", "La decena es la cifra de la izquierda."),
        ],
        "apply": [
            ex("Descompón 73 en el valor de cada cifra.", "70 + 3", "7 decenas valen 70 y 3 unidades valen 3."),
            ex("En 88, ¿cuánto vale cada 8?", "El primero vale 80 y el segundo vale 8", "Uno está en D y otro en U."),
            arith("Suma 60 + 4. ¿Qué número formas?", "60+4", "Las partes 60 y 4 juntas forman 64."),
        ],
        "reason": [
            ex("Pía dice que el 7 de 17 y el 7 de 71 valen lo mismo. ¿Tiene razón?", "No; en 17 vale 7 y en 71 vale 70", "En 17 está en U y en 71 está en D."),
            ex("¿Por qué el 2 de 29 vale más que el 9?", "Porque el 2 está en las decenas y vale 20, y el 9 vale 9", "20 es mayor que 9."),
        ],
        "challenge": [
            ex("En un número de dos cifras, una cifra vale 90 y la otra vale 5. ¿Qué número es?", "95", "90 + 5 = 95."),
            ex("Un número de dos cifras tiene un 3 que vale 30. Su otra cifra es 3 más que 3. ¿Qué número es?", "36", "El 3 está en D y la otra cifra es 6 en U; 30 + 6 = 36."),
        ],
    },
    context=[ex("Una caja tiene el número 66. Si una cifra vale 60, ¿cuánto vale la otra y por qué?", "6; está en las unidades", "El segundo 6 está en U y vale solo 6.")],
    selfcheck=[ex("¿Cuánto vale el 4 en 49?", "40", "Está en las decenas."), ex("¿Cuánto vale el 9 en 49?", "9", "Está en las unidades."), ex("¿Cuánto vale el primer 5 de 55?", "50", "Está en D.")],
    open_task=task(
        "Mira los números 27, 72 y 77. Para cada número escribe cuánto vale cada cifra y dibuja las barras y cubos con ▮ y ●. Explica por qué el 7 de 27 y el 7 de 72 son distintos.",
        "27: 2 vale 20 y 7 vale 7 (" + bars(27) + "). 72: 7 vale 70 y 2 vale 2 (" + bars(72) + "). 77: un 7 vale 70 y el otro 7 (" + bars(77) + "). El 7 de 27 vale 7 y el 7 de 72 vale 70 porque cambia su posición.",
        ["escribe el valor de cada cifra", "dibuja barras y cubos correctos", "explica con la posición"],
        ["valores escritos", "tres dibujos", "frase de explicación"],
        ["decir que la cifra siempre vale lo mismo", "olvidar el valor de la decena"],
        "Pide que señale en el dibujo qué barras representan cada cifra; reconoce el uso del valor posicional.",
    ),
    reinforce="Escribe en tarjetas 20, 7, 50 y 3. Júntalas de a dos para formar números de dos cifras como 53 y 27 y di el valor de cada cifra.",
    extend="Escribe cinco números de dos cifras que tengan 4 decenas y explica el valor de cada cifra.",
)

register(
    OA7, 4,
    materials=f"Barras y cubos dibujados en este cuaderno y lápiz. {KEY}",
    use="Aprenderé que un mismo número se puede armar de varias maneras deshaciendo una decena. Sirve para restar y sumar con números grandes más adelante.",
    prior=["Sé hacer un canje de 10 unidades por 1 decena.", "Sé que 1 decena se puede deshacer en 10 unidades."],
    explain=[
        "Un número se puede mostrar de más de una forma. Por ejemplo, 42 es 4 decenas y 2 unidades. Pero también es 3 decenas y 12 unidades. Para obtenerlo, deshaces una decena y la cambias por 10 unidades.",
        f"Mira el dibujo de 42: {bars(42)}. Quitas una barra de 10 y la cambias por 10 cubos. Quedan 3 barras y 12 cubos sueltos: ▮ ▮ ▮ | {'● ' * 12}. Parece distinto, pero siguen siendo 42, porque 30 + 12 = 42.",
        "La forma con 4 decenas y 2 unidades es la forma normal. Las otras formas sirven mucho cuando necesitas más unidades sueltas. Siempre comprueba sumando: el valor de las decenas más las unidades debe dar el mismo número.",
    ],
    vocab=[("deshacer una decena", "cambiar 1 decena por 10 unidades"), ("forma normal", "la que usa la mayor cantidad posible de decenas"), ("otra forma", "una manera distinta de armar el mismo número"), ("canje", "cambiar unidades por decenas o decenas por unidades"), ("comprobar", "revisar que el total sea el mismo")],
    worked=[
        {"title": "Deshacer una decena", "problem": "Muestra 42 como 3 decenas y algunas unidades.", "steps": ["42 es 4 decenas y 2 unidades.", "Deshago una decena: queda 3 decenas.", "Esa decena se cambia por 10 unidades: 2 + 10 = 12.", "Compruebo: 30 + 12 = 42."], "answer": "3 decenas y 12 unidades"},
        {"title": "Otra forma de 53", "problem": "Muestra 53 como 4 decenas y algunas unidades.", "steps": ["53 es 5 decenas y 3 unidades.", "Deshago una decena: quedan 4 decenas.", "Las unidades suben a 3 + 10 = 13.", "Compruebo: 40 + 13 = 53."], "answer": "4 decenas y 13 unidades"},
    ],
    mistakes=[
        {"wrong": "Decir que 3 decenas y 12 unidades son 312.", "why": "Se escriben juntas las cifras sin pensar en el valor de cada una.", "fix": "Calcula 30 + 12 = 42: 3 decenas son 30."},
        {"wrong": "Al deshacer una decena, agregar solo 1 unidad.", "why": "Se olvida que una decena tiene 10 unidades.", "fix": "Una decena se cambia por 10 unidades."},
    ],
    tiers={
        "recovery": [
            arith("Una decena se deshace en 10 unidades. ¿Cuántas unidades hay en 2 decenas deshechas?", "10+10", "Cada decena son 10 unidades."),
            ex(f"El dibujo {bars(32)} muestra 3 decenas y 2 unidades. Si deshaces una decena, ¿cuántas decenas quedan?", "2", "De 3 decenas se quita 1."),
            arith("Tienes 2 decenas y 15 unidades. ¿Qué número es?", "10+10+15", "Dos decenas son 20 y 20 + 15 = 35."),
        ],
        "understand": [
            ex("¿Es verdad que 42 es 3 decenas y 12 unidades?", "Sí", "30 + 12 = 42."),
            ex("Si deshaces una decena, ¿cuántas unidades ganas?", "10", "Una decena equivale a 10 unidades."),
            ex("¿Cuál es la forma normal de 4 decenas y 12 unidades?", "5 decenas y 2 unidades", "Con 10 de las 12 unidades se arma otra decena."),
        ],
        "apply": [
            ex("Escribe 53 como 4 decenas y unidades.", "4 decenas y 13 unidades", "Se deshace una decena y las unidades suben a 13."),
            ex("Escribe 35 como 2 decenas y unidades.", "2 decenas y 15 unidades", "Se deshace una decena: 5 + 10 = 15."),
            ex("Escribe 20 como 1 decena y unidades.", "1 decena y 10 unidades", "Se deshace una decena: 0 + 10 = 10."),
        ],
        "reason": [
            ex("Gaby dice que 5 decenas y 3 unidades es distinto a 4 decenas y 13 unidades. ¿Tiene razón?", "No; los dos son 53", "50 + 3 = 53 y 40 + 13 = 53."),
            ex("Beto dice que 3 decenas y 12 unidades son 312. ¿Qué error comete y cuál es el número?", "No suma el valor de cada parte; el número es 42", "30 + 12 = 42."),
        ],
        "challenge": [
            ex("Escribe 61 de dos formas distintas usando decenas y unidades.", "6 decenas y 1 unidad; 5 decenas y 11 unidades (también 4 decenas y 21 unidades)", "Cada vez que se deshace una decena, se suman 10 unidades."),
            ex("Un número es 2 decenas y 25 unidades. ¿Cuál es su forma normal y qué número es?", "4 decenas y 5 unidades; 45", "20 + 25 = 45 y 25 unidades armadas son 2 decenas y 5 unidades."),
        ],
    },
    context=[ex("Un cajón tiene 4 paquetes de 10 lápices y 2 lápices sueltos. Si abres un paquete, ¿cuántos paquetes y cuántos sueltos quedan?", "3 paquetes y 12 lápices sueltos", "Al abrir un paquete se ganan 10 sueltos: 2 + 10 = 12.")],
    selfcheck=[ex("Escribe 25 como 1 decena y unidades.", "1 decena y 15 unidades", "Se deshace una decena: 5 + 10 = 15."), arith("¿Cuánto es 4 decenas y 13 unidades?", "10+10+10+10+13", "40 + 13 = 53."), ex("¿Cuántas unidades se ganan al deshacer una decena?", "10", "Una decena equivale a 10 unidades.")],
    open_task=task(
        "Muestra de dos formas distintas los números 36, 50 y 74. Dibuja con ▮ y ● la forma normal y una forma con una decena deshecha. Escribe las dos formas en decenas y unidades.",
        "36: " + bars(36) + " son 3D 6U y también 2D 16U. 50: 5D 0U y también 4D 10U. 74: 7D 4U y también 6D 14U.",
        ["muestra dos formas por número", "deshace una decena y suma 10 unidades", "comprueba que el total es el mismo"],
        ["dibujos", "formas escritas en decenas y unidades"],
        ["no sumar las 10 unidades al deshacer", "creer que el número cambió"],
        "Pide que cuente el total en las dos formas y compruebe que dan lo mismo.",
    ),
    reinforce="Con 3 paquetes de 10 palitos y 5 sueltos, abre un paquete y cuenta cuántos palitos hay en total antes y después.",
    extend="Escribe 70 de tres formas distintas y comprueba que las tres valen lo mismo.",
)
