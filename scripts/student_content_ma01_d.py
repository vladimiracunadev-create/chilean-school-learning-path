"""Student material for 1.º básico Matemática, OA 12 (igualdad), OA 13 (posición) y OA 14 (figuras 2D y 3D)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA12, OA13, OA14 = "MA01 OA 12", "MA01 OA 13", "MA01 OA 14"

# ---------------------------------------------------------------- OA 12
register(
    OA12, 1,
    materials="Una balanza de dos platillos (dibujada en este cuaderno o con una regla sobre un lápiz) y fichas; las cantidades están escritas en cada ejercicio.",
    use="Aprenderé que una balanza se equilibra cuando hay la misma cantidad a cada lado. Sirve para entender qué es igual y qué es distinto.",
    prior=["Sé comparar cantidades.", "Sé contar hasta 20."],
    explain=[
        "Una balanza tiene dos platillos. Si en cada platillo hay la misma cantidad, los dos están a la misma altura: hay equilibrio. Si un platillo tiene más, ese lado baja y el otro sube: hay desequilibrio.",
        "Por ejemplo, con 5 fichas a la izquierda y 5 fichas a la derecha, la balanza queda plana. Con 5 a la izquierda y 3 a la derecha, baja la izquierda, porque tiene más. Lo que baja siempre es el lado que pesa más, es decir, el que tiene más fichas iguales.",
        "Para recuperar el equilibrio hay que igualar las cantidades: quitar al lado que tiene más, o agregar al que tiene menos. Después de cada cambio, vuelve a mirar la balanza.",
    ],
    vocab=[("balanza", "instrumento con dos platillos para comparar"), ("equilibrio", "los dos lados tienen la misma cantidad"), ("desequilibrio", "un lado tiene más que el otro"), ("platillo", "cada lado de la balanza"), ("igualar", "hacer que ambos lados tengan lo mismo")],
    worked=[
        {"title": "Equilibrio", "problem": "Izquierda: 5 fichas. Derecha: 5 fichas. ¿Qué pasa con la balanza?", "steps": ["Comparo: 5 y 5 son iguales.", "No sobra ninguna.", "La balanza queda en equilibrio."], "answer": "Equilibrio"},
        {"title": "Desequilibrio", "problem": "Izquierda: 7 fichas. Derecha: 4 fichas. ¿Qué lado baja?", "steps": ["Comparo: 7 es mayor que 4.", "El lado con más fichas pesa más.", "Baja la izquierda."], "answer": "Baja la izquierda (desequilibrio)"},
    ],
    mistakes=[
        {"wrong": "Decir que baja el lado con menos fichas.", "why": "Se confunde cuál pesa más.", "fix": "Baja el lado que tiene más fichas."},
        {"wrong": "Pensar que equilibrio es que haya fichas a los dos lados.", "why": "No se compara la cantidad.", "fix": "Equilibrio es que haya la misma cantidad."},
    ],
    tiers={
        "recovery": [ex("Izquierda: 3 fichas. Derecha: 3 fichas. ¿Hay equilibrio?", "Sí", "Hay la misma cantidad."), ex("Izquierda: 6 fichas. Derecha: 2 fichas. ¿Hay equilibrio?", "No", "Un lado tiene más."), ex("Izquierda: 4 fichas. Derecha: 9 fichas. ¿Qué lado baja?", "La derecha", "Tiene más fichas.")],
        "understand": [
            ex("¿Qué significa que una balanza esté en equilibrio?", "Que ambos lados tienen la misma cantidad", "Los platillos están a la misma altura."),
            ex("¿Cómo se llama cuando un lado tiene más que el otro?", "Desequilibrio", "La balanza se inclina."),
            ex("Si un lado baja, ¿tiene más o menos que el otro?", "Más", "El lado que baja pesa más."),
        ],
        "apply": [
            ex("Izquierda: 8 fichas. Derecha: 8 fichas. ¿Qué pasa con la balanza?", "Equilibrio", "Ocho y ocho son iguales."),
            ex("Izquierda: 10 fichas. Derecha: 7 fichas. ¿Qué lado baja y cuántas fichas más tiene?", "Baja la izquierda; 3 más", "10 − 7 = 3."),
            ex("Izquierda: 5 fichas. Derecha: 12 fichas. ¿Qué lado sube?", "La izquierda", "Tiene menos fichas."),
        ],
        "reason": [
            ex("Rosa dice que con 6 y 6 hay desequilibrio porque hay muchas fichas. ¿Qué error comete?", "Mira cuántas hay y no si son iguales; hay equilibrio", "6 y 6 son iguales."),
            ex("Un lado tiene 9 y el otro 9. Agrego 1 al primero. ¿Qué pasa?", "Se desequilibra: baja el primero", "Ahora hay 10 y 9."),
        ],
        "challenge": [
            ex("Izquierda: 6 fichas. Derecha: 10 fichas. ¿Cuántas fichas debo agregar a la izquierda para equilibrar?", "4", "6 + 4 = 10."),
            ex("Izquierda: 12 fichas. Derecha: 8 fichas. Quito fichas de la izquierda. ¿Cuántas debo quitar para equilibrar?", "4", "12 − 4 = 8."),
        ],
    },
    context=[ex("En la feria, una balanza tiene 5 manzanas de un lado y 8 del otro. ¿Qué lado baja y cuántas manzanas debo sacar para equilibrar?", "Baja el lado de 8; sacar 3", "8 − 3 = 5.")],
    selfcheck=[ex("Izquierda: 7, derecha: 7. ¿Qué hay?", "Equilibrio", "Los dos lados tienen cantidades iguales."), ex("Izquierda: 2, derecha: 5. ¿Qué lado baja?", "La derecha", "La derecha tiene más fichas."), ex("¿Cómo igualo un lado que tiene menos?", "Agregando", "Hay que sumarle lo que falta.")],
    open_task=task("Dibuja una balanza. Pon 6 fichas a la izquierda y 9 a la derecha. Escribe qué lado baja, cuántas fichas más tiene y cómo recuperarías el equilibrio de dos maneras.", "Baja la derecha; tiene 3 más. Para equilibrar puedo quitar 3 de la derecha (queda 6 y 6) o agregar 3 a la izquierda (queda 9 y 9).", ["dibuja la balanza", "dice qué lado baja y cuánto más", "propone dos maneras"], ["dibujo", "frase", "dos soluciones"], ["decir que baja el lado con menos", "dar sólo una solución"], "Pide comprobar con fichas cada solución."),
    reinforce="Con fichas y una regla sobre un lápiz, arma equilibrios con 4, 6 y 8 fichas.",
    extend="Busca todas las maneras de equilibrar 5 fichas a la izquierda con fichas de la derecha, sin tocar la izquierda.",
)

register(
    OA12, 2,
    materials="Balanzas dibujadas con cantidades en cada ejercicio; lápiz.",
    use="Aprenderé a escribir una igualdad con el signo igual (=) y a entender que dice «es lo mismo que». Sirve para registrar un equilibrio con números.",
    prior=["Sé qué es el equilibrio.", "Sé sumar hasta 20."],
    explain=[
        "El signo = se llama igual. Dice que lo que está a la izquierda tiene el mismo valor que lo que está a la derecha. 5 = 5 se lee «cinco es igual a cinco» y corresponde a una balanza en equilibrio.",
        "El signo igual no siempre significa «el resultado viene ahora». En 3 + 2 = 5, es verdad que 5 es el resultado, pero también podemos escribir 5 = 3 + 2. Las dos están bien, porque ambos lados valen lo mismo.",
        "Para saber si una igualdad es verdadera, calcula cada lado y compara. En 4 + 3 = 7, el lado izquierdo vale 7 y el derecho 7: es verdadera. En 4 + 3 = 8, el izquierdo vale 7 y el derecho 8: es falsa.",
    ],
    vocab=[("igual (=)", "dice que ambos lados valen lo mismo"), ("igualdad", "dos cosas que valen lo mismo, escritas con ="), ("verdadera", "se cumple"), ("falsa", "no se cumple"), ("lado", "lo que está a la izquierda o a la derecha del =")],
    worked=[
        {"title": "Registrar un equilibrio", "problem": "Una balanza tiene 4 fichas a un lado y 4 al otro. Escribe la igualdad.", "steps": ["Cada lado vale 4.", "Escribo 4 = 4."], "answer": "4 = 4"},
        {"title": "Verdadera o falsa", "problem": "¿Es verdadera 4 + 3 = 8?", "steps": ["Calculo el lado izquierdo: 4 + 3 = 7.", "El derecho es 8.", "7 y 8 no son iguales."], "answer": "Falsa"},
    ],
    mistakes=[
        {"wrong": "Creer que después del = siempre va el resultado.", "why": "Se piensa que = sólo anuncia la respuesta.", "fix": "= dice que ambos lados valen lo mismo."},
        {"wrong": "Escribir 4 + 3 = 8.", "why": "No se calcula el lado izquierdo.", "fix": "Calcula primero: 4 + 3 = 7."},
    ],
    tiers={
        "recovery": [ex("Escribe la igualdad de una balanza con 6 y 6 fichas.", "6 = 6", "Ambos lados valen 6."), ex("Escribe la igualdad de una balanza con 9 y 9 fichas.", "9 = 9", "Ambos lados valen 9."), ex("¿Cómo se lee 5 = 5?", "Cinco es igual a cinco", "El signo = dice igual.")],
        "understand": [
            ex("¿Qué significa el signo =?", "Que ambos lados valen lo mismo", "Es el equilibrio."),
            ex("¿Es verdadera 2 + 3 = 5?", "Sí", "Ambos lados valen 5."),
            ex("¿Es verdadera 6 = 4 + 3?", "No", "El lado derecho vale 7."),
        ],
        "apply": [
            ex("¿Es verdadera 5 + 4 = 9?", "Sí", "5 + 4 = 9."),
            ex("¿Es verdadera 7 + 2 = 10?", "No", "7 + 2 = 9."),
            ex("¿Es verdadera 8 = 5 + 3?", "Sí", "5 + 3 = 8."),
        ],
        "reason": [
            ex("Beto dice que 3 + 2 = 5 es verdadera pero 5 = 3 + 2 no. ¿Tiene razón?", "No; ambas son verdaderas", "Los dos lados valen 5 en ambos casos."),
            ex("Lola dice que 6 + 1 = 7 + 1 es verdadera. ¿Qué error comete?", "Es falsa: 7 y 8 no son iguales", "6 + 1 = 7 y 7 + 1 = 8."),
        ],
        "challenge": [
            ex("Escribe una igualdad verdadera que use el 10 de un lado y una suma del otro.", "10 = 6 + 4", "6 + 4 = 10."),
            ex("Completa para que sea verdadera: 8 + __ = 12.", "4", "12 − 8 = 4."),
        ],
    },
    context=[ex("Ana tiene 4 lápices y 3 crayones. Beto tiene 7 pinceles. Escribe una igualdad que diga que tienen la misma cantidad de útiles.", "4 + 3 = 7", "Ambos tienen siete.")],
    selfcheck=[ex("¿Es verdadera 3 + 3 = 6?", "Sí", "3 + 3 = 6."), ex("¿Es verdadera 10 = 8 + 1?", "No", "8 + 1 = 9."), ex("¿Qué se hace primero para saber si una igualdad es verdadera?", "Calcular cada lado", "Luego se comparan.")],
    open_task=task("Escribe tres igualdades verdaderas y una falsa usando el signo =. Marca cuál es la falsa y explica cómo lo sabes.", "6 = 6, 4 + 2 = 6, 3 + 3 = 6 son verdaderas. 4 + 2 = 7 es falsa porque 4 + 2 = 6 y 6 no es 7.", ["tres verdaderas", "una falsa marcada", "justifica con cálculo"], ["cuatro igualdades", "explicación"], ["confundir verdadera y falsa", "no calcular"], "Pide mostrar el cálculo de cada lado."),
    reinforce="Escribe la igualdad de cada equilibrio que armes con fichas.",
    extend="Busca cuántas igualdades verdaderas con una suma puedes escribir para el número 8.",
)

register(
    OA12, 3,
    materials="Expresiones escritas en cada ejercicio; fichas de dos colores; lápiz.",
    use="Aprenderé que dos sumas distintas pueden valer lo mismo. Sirve para ver que un número se puede formar de muchas maneras.",
    prior=["Sé escribir igualdades.", "Sé sumar hasta 20."],
    explain=[
        "Dos expresiones son equivalentes si valen lo mismo. 3 + 4 y 5 + 2 son equivalentes porque las dos valen 7. Se escribe 3 + 4 = 5 + 2.",
        "Puedes usar la balanza para comprobarlo: en un platillo pones 3 + 4 y en el otro 5 + 2. Si queda en equilibrio, son equivalentes. Si no, uno de los lados vale más.",
        "Para encontrar una expresión equivalente, calcula el valor y busca otra suma con el mismo resultado. Si 3 + 4 = 7, entonces 6 + 1 = 7 y 2 + 5 = 7 son equivalentes.",
    ],
    vocab=[("expresión", "una suma o resta escrita con números"), ("equivalente", "que vale lo mismo"), ("valor", "el resultado de calcular"), ("lado", "la expresión a la izquierda o a la derecha"), ("comprobar", "calcular los dos lados")],
    worked=[
        {"title": "Comprobar equivalencia", "problem": "¿Son equivalentes 3 + 4 y 5 + 2?", "steps": ["3 + 4 = 7.", "5 + 2 = 7.", "Los dos valen 7."], "answer": "Sí; 3 + 4 = 5 + 2"},
        {"title": "Encontrar una equivalente", "problem": "Encuentra una suma equivalente a 8 + 2.", "steps": ["8 + 2 = 10.", "Busco otra con resultado 10: 6 + 4.", "6 + 4 = 10."], "answer": "6 + 4"},
    ],
    mistakes=[
        {"wrong": "Decir que 3 + 4 y 5 + 3 son equivalentes.", "why": "No se calculan los dos valores.", "fix": "3 + 4 = 7 y 5 + 3 = 8; no son equivalentes."},
        {"wrong": "Pensar que equivalente significa los mismos números.", "why": "Se compara la forma.", "fix": "Equivalente significa mismo valor, aunque los números sean distintos."},
    ],
    tiers={
        "recovery": [ex("¿Cuánto vale 4 + 2?", "6", "4 + 2 = 6."), ex("¿Cuánto vale 5 + 1?", "6", "5 + 1 = 6."), ex("¿Son equivalentes 4 + 2 y 5 + 1?", "Sí", "Las dos valen 6.")],
        "understand": [
            ex("¿Qué quiere decir que dos expresiones sean equivalentes?", "Que valen lo mismo", "Dan el mismo resultado."),
            ex("¿Son equivalentes 6 + 3 y 7 + 2?", "Sí", "Las dos valen 9."),
            ex("¿Son equivalentes 5 + 5 y 6 + 3?", "No", "10 y 9 son distintos."),
        ],
        "apply": [
            ex("Escribe una suma equivalente a 9 + 1.", "8 + 2", "8 + 2 = 10."),
            ex("Escribe una suma equivalente a 7 + 5.", "6 + 6", "Las dos valen 12."),
            ex("Completa para que sea equivalente: 4 + 6 = 7 + __.", "3", "4 + 6 = 10 y 7 + 3 = 10."),
        ],
        "reason": [
            ex("Mateo dice que 8 + 3 y 3 + 8 son equivalentes. ¿Tiene razón?", "Sí", "Las dos valen 11."),
            ex("Pía dice que 5 + 4 = 4 + 6. ¿Tiene razón?", "No", "9 y 10 son distintos."),
        ],
        "challenge": [
            ex("Escribe tres sumas equivalentes a 12.", "6 + 6, 7 + 5 y 9 + 3", "Todas valen 12."),
            ex("Completa: 10 + 3 = 8 + __.", "5", "Las dos valen 13."),
        ],
    },
    context=[ex("Sofi tiene 4 manzanas rojas y 6 verdes. Su hermano tiene 7 manzanas amarillas y 3 verdes. ¿Tienen la misma cantidad de manzanas?", "Sí; 4 + 6 = 7 + 3", "Las dos valen 10.")],
    selfcheck=[ex("¿Son equivalentes 2 + 6 y 4 + 4?", "Sí", "Ambas valen 8."), ex("¿Es equivalente 5 + 5 a 3 + 6?", "No", "10 y 9."), ex("Escribe una suma equivalente a 3 + 3.", "4 + 2", "Ambas valen 6.")],
    open_task=task("Encuentra tres sumas equivalentes a 5 + 4 y comprueba cada una calculando los dos lados. Escribe la igualdad completa.", "5 + 4 = 6 + 3, 5 + 4 = 7 + 2, 5 + 4 = 8 + 1. Todas valen 9.", ["tres sumas distintas", "las tres valen 9", "comprueba los dos lados"], ["tres igualdades", "cálculo"], ["una suma que no vale 9", "repetir sumas"], "Pide verificar con la balanza."),
    reinforce="Usa fichas para comprobar que 3 + 4 y 5 + 2 se equilibran.",
    extend="Busca una suma de tres números equivalente a 3 + 4.",
)

register(
    OA12, 4,
    materials="Balanzas con cantidades escritas en cada ejercicio; lápiz.",
    use="Aprenderé a recuperar el equilibrio cuando la balanza está desequilibrada, agregando o quitando lo que falta. Sirve para resolver igualdades con un número que falta.",
    prior=["Sé qué es una igualdad.", "Sé qué es una expresión equivalente."],
    explain=[
        "Si una balanza está desequilibrada, un lado vale más. Para recuperar el equilibrio, hay que quitar al lado mayor o agregar al menor. Pero debes calcular cuánto.",
        "Si a la izquierda hay 7 y a la derecha 4, la diferencia es 7 − 4 = 3. Agregando 3 a la derecha o quitando 3 de la izquierda se equilibra. Cada solución es correcta.",
        "También puedes completar una igualdad con un número que falta: 5 + __ = 9. El número que falta es lo que hay que agregar al 5 para llegar a 9, es decir, 9 − 5 = 4. Después comprueba: 5 + 4 = 9.",
    ],
    vocab=[("recuperar", "volver a lograr"), ("diferencia", "lo que falta para igualar"), ("agregar", "poner más"), ("quitar", "sacar"), ("número que falta", "el valor que hace verdadera la igualdad")],
    worked=[
        {"title": "Equilibrar", "problem": "Izquierda: 7 fichas. Derecha: 4 fichas. ¿Cómo recupero el equilibrio?", "steps": ["Diferencia: 7 − 4 = 3.", "Opción 1: agrego 3 a la derecha: 7 y 7.", "Opción 2: quito 3 de la izquierda: 4 y 4."], "answer": "Agregar 3 a la derecha o quitar 3 de la izquierda"},
        {"title": "Número que falta", "problem": "Completa 5 + __ = 9.", "steps": ["Necesito llegar de 5 a 9.", "9 − 5 = 4.", "Compruebo: 5 + 4 = 9."], "answer": "4"},
    ],
    mistakes=[
        {"wrong": "Agregar 7 al lado menor.", "why": "No se calcula la diferencia.", "fix": "Calcula 7 − 4 = 3 y agrega sólo 3."},
        {"wrong": "Quitar del lado menor.", "why": "Se empeora el desequilibrio.", "fix": "Se quita al lado que tiene más."},
    ],
    tiers={
        "recovery": [ex("Izquierda: 5. Derecha: 3. ¿Cuánto falta para igualar?", "2", "5 − 3 = 2."), ex("Izquierda: 8. Derecha: 6. ¿Cuánto falta para igualar?", "2", "8 − 6 = 2."), ex("Izquierda: 10. Derecha: 4. ¿Cuánto falta para igualar?", "6", "10 − 4 = 6.")],
        "understand": [
            ex("Si un lado tiene más, ¿cómo lo equilibro sin agregar?", "Quitando", "Se saca lo que sobra."),
            ex("Si un lado tiene menos, ¿cómo lo equilibro sin quitar?", "Agregando", "Se pone lo que falta."),
            ex("Después de equilibrar, ¿qué debo comprobar?", "Que ambos lados valgan lo mismo", "Se calculan los dos lados."),
        ],
        "apply": [
            ex("Completa: 6 + __ = 11.", "5", "11 − 6 = 5."),
            ex("Completa: 8 + __ = 15.", "7", "15 − 8 = 7."),
            ex("Izquierda: 12. Derecha: 7. Escribe una manera de equilibrar.", "Agregar 5 a la derecha o quitar 5 de la izquierda", "12 − 7 = 5."),
        ],
        "reason": [
            ex("Raúl dice que para equilibrar 9 y 4 hay que agregar 9 a la derecha. ¿Qué error comete?", "Debe agregar 5", "9 − 4 = 5."),
            ex("¿Hay una sola manera de equilibrar una balanza desequilibrada?", "No; se puede agregar o quitar", "Las dos acciones funcionan."),
        ],
        "challenge": [
            ex("Un lado tiene 3 + 4 y el otro 2 + __. Completa para que se equilibre.", "5", "3 + 4 = 7 y 2 + 5 = 7."),
            ex("Quito 2 al lado de 9 y agrego 1 al lado de 5. ¿Quedó en equilibrio?", "No; 7 y 6", "Faltaba quitar 4 o agregar 4."),
        ],
    },
    context=[ex("En una tienda, un platillo tiene 9 bananas y el otro 6. El vendedor quiere equilibrar sacando bananas. ¿Cuántas debe sacar?", "3", "9 − 3 = 6.")],
    selfcheck=[ex("Completa: 4 + __ = 10.", "6", "10 − 4 = 6."), ex("Izquierda: 8. Derecha: 5. ¿Cuánto falta?", "3", "8 − 5 = 3."), ex("¿Se puede equilibrar quitando?", "Sí", "Se saca del lado mayor.")],
    open_task=task("Dibuja una balanza con 11 fichas a la izquierda y 5 a la derecha. Escribe la diferencia, y dos formas de recuperar el equilibrio con las operaciones que usas.", "Diferencia: 11 − 5 = 6. Forma 1: agrego 6 a la derecha, 5 + 6 = 11. Forma 2: quito 6 de la izquierda, 11 − 6 = 5.", ["calcula la diferencia", "dos formas", "escribe las operaciones"], ["dibujo", "operaciones"], ["agregar o quitar una cantidad incorrecta", "una sola forma"], "Pide comprobar con fichas."),
    reinforce="Equilibra con fichas balanzas con 7 y 10, 6 y 11, 9 y 4.",
    extend="Equilibra una balanza agregando una parte a un lado y quitando otra del otro.",
)

# ---------------------------------------------------------------- OA 13
register(
    OA13, 1,
    materials="Una hoja con un dibujo de dos manos y un niño de frente; lápiz de color. Todo está descrito en este cuaderno.",
    use="Aprenderé a distinguir mi derecha de mi izquierda en mi propio cuerpo. Sirve para seguir instrucciones y orientarme.",
    prior=["Sé nombrar partes del cuerpo.", "Sé qué significa lado."],
    explain=[
        "Tienes dos lados en el cuerpo: el derecho y el izquierdo. La mano derecha es la que usas para escribir si eres diestro; la izquierda es la otra. Tienes un pie derecho y uno izquierdo, un ojo derecho y uno izquierdo.",
        "Para no confundirte, escribe una D en una pulsera de lápiz en tu mano derecha o ata una cinta ahí. Mira tu mano: si es la de la cinta, es la derecha. Así asocias la palabra con tu lado.",
        "Al decir «a mi derecha» me refiero al lado derecho de mi cuerpo, no al de otra persona. Si alguien te mira de frente, su derecha queda frente a tu izquierda.",
    ],
    vocab=[("derecha", "el lado del cuerpo donde está la mano derecha"), ("izquierda", "el otro lado del cuerpo"), ("mi lado", "el lado de mi propio cuerpo"), ("de frente", "mirando a alguien cara a cara"), ("cinta", "señal para recordar la derecha")],
    worked=[
        {"title": "Identificar", "problem": "Levanta la mano con la cinta. ¿Es la derecha o la izquierda?", "steps": ["Puse la cinta en la mano derecha.", "Levanto esa mano.", "Es la derecha."], "answer": "La derecha"},
        {"title": "Oponerse al de enfrente", "problem": "Una niña de frente levanta su mano derecha. ¿Qué mano parece levantar desde donde tú la miras?", "steps": ["Ella me mira, así que su derecha queda frente a mi izquierda.", "Desde mi lado veo la mano a mi izquierda."], "answer": "Me parece que levanta la mano a mi izquierda"},
    ],
    mistakes=[
        {"wrong": "Confundir la derecha de otra persona con la mía.", "why": "Se mira de frente.", "fix": "La derecha es la de la persona de la que hablo."},
        {"wrong": "Usar «derecha» para el lado donde hay una puerta.", "why": "Se mezcla un lugar con el cuerpo.", "fix": "Derecha e izquierda se refieren a mi cuerpo."},
    ],
    tiers={
        "recovery": [ex("¿Con cuál mano escribes: derecha o izquierda? Responde para ti.", "Depende de cada persona; la mano que usas se llama así", "La mano con que escribes es una de las dos."), ex("Nombra una parte del cuerpo que tiene lado derecho e izquierdo.", "Por ejemplo, pie, mano, ojo u oreja", "Muchas partes vienen en pares."), ex("Si levantas la mano derecha, ¿levantas la que está del lado de la cinta?", "Sí, si pusiste la cinta en la derecha", "La cinta ayuda a recordar.")],
        "understand": [
            ex("¿Cuántas manos tienes: derecha e izquierda?", "Dos", "Una a cada lado."),
            ex("¿Qué lado es el contrario del izquierdo?", "El derecho", "Son los dos lados del cuerpo."),
            ex("Si me miras de frente, ¿mi derecha queda frente a tu derecha o a tu izquierda?", "A tu izquierda", "Estamos uno frente al otro."),
        ],
        "apply": [
            ex("Toca tu oreja derecha con tu mano izquierda. ¿Qué lados usaste?", "Mano izquierda y oreja derecha", "Cruzaste los lados."),
            ex("Levanta el pie izquierdo. ¿Qué lado levantaste?", "El izquierdo", "Es el pie del lado izquierdo."),
            ex("Cierra el ojo derecho. ¿Qué ojo sigue abierto?", "El izquierdo", "Son dos ojos."),
        ],
        "reason": [
            ex("Mateo dice que su derecha cambia cuando se da vuelta. ¿Tiene razón?", "No; la derecha siempre es la de su cuerpo", "Cambia hacia dónde mira, no su lado."),
            ex("¿Por qué una cinta en la mano derecha ayuda a recordar?", "Porque asocia la palabra con una señal en mi cuerpo", "Cada vez que la veo, recuerdo."),
        ],
        "challenge": [
            ex("Pon la mano derecha en la cabeza y la izquierda en el hombro derecho. ¿Qué hiciste?", "Cruzaste la mano izquierda hacia el lado derecho", "El hombro derecho está del lado derecho."),
            ex("Una niña me mira de frente y levanta su mano izquierda. ¿Hacia qué lado la veo yo?", "Hacia mi derecha", "Estamos uno frente al otro."),
        ],
    },
    context=[ex("En una clase de baile la profesora dice: «¡pie izquierdo adelante!». ¿Qué pie mueves?", "El izquierdo", "Es el del lado izquierdo de tu cuerpo.")],
    selfcheck=[ex("¿Cuál lado es el contrario de derecha?", "Izquierda", "Son los dos lados del cuerpo."), ex("Levanta la mano derecha. ¿Qué mano levantaste?", "La derecha", "Es la del lado derecho."), ex("¿Se parece mi derecha a la de otra persona?", "Sí, si miramos hacia el mismo lado", "Depende de hacia dónde mira.")],
    open_task=task("Haz un dibujo de ti mismo de frente. Pinta de rojo tu mano derecha y de azul tu mano izquierda. Escribe debajo cuál es cuál y explica cómo lo recuerdas.", "Pinté la mano derecha de rojo (la que uso para escribir) y la izquierda de azul. Lo recuerdo con una cinta en la derecha.", ["pinta las manos", "rotula cuál es cuál", "explica cómo lo recuerda"], ["dibujo", "rótulos", "explicación"], ["invertir derecha e izquierda en el dibujo", "no explicar"], "Pide que mire su propia mano para comprobar."),
    reinforce="Juega «Simón dice» con derecha e izquierda.",
    extend="Descubre cómo ayudaría a una persona que mira de frente a ubicar su derecha.",
)

register(
    OA13, 2,
    materials="Dibujos de objetos sobre una mesa descritos en cada ejercicio; lápiz.",
    use="Aprenderé a decir dónde está un objeto respecto de otro usando derecha, izquierda, arriba, abajo, delante, detrás, cerca y lejos. Sirve para dar y entender indicaciones.",
    prior=["Sé distinguir mi derecha e izquierda.", "Sé nombrar objetos de la sala."],
    explain=[
        "Para decir dónde está un objeto, lo comparas con otro: «el libro está a la derecha del lápiz». Necesitas tres cosas: el objeto que buscas, el objeto de referencia y la palabra de posición.",
        "Las palabras de posición más comunes son derecha, izquierda, arriba, abajo, delante, detrás, cerca, lejos, entre, al lado. Cada una dice una relación distinta. «Arriba» y «abajo» miran el alto; «delante» y «detrás» miran el fondo.",
        "Cuando uses derecha o izquierda, aclara desde dónde miras: desde el cuaderno o desde una persona. Si no lo dices, la otra persona puede entender lo contrario.",
    ],
    vocab=[("referencia", "el objeto con el que comparo"), ("a la derecha de", "en el lado derecho del objeto"), ("arriba", "más alto"), ("abajo", "más bajo"), ("entre", "en medio de dos objetos")],
    worked=[
        {"title": "Posición respecto de otro", "problem": "En una mesa hay: lápiz, libro y goma en fila, de izquierda a derecha. ¿Dónde está el libro respecto del lápiz?", "steps": ["El lápiz está primero a la izquierda.", "El libro viene después hacia la derecha.", "El libro está a la derecha del lápiz."], "answer": "A la derecha del lápiz"},
        {"title": "Entre", "problem": "¿Dónde está el libro respecto del lápiz y la goma?", "steps": ["Lápiz, libro, goma.", "El libro queda en el medio."], "answer": "Entre el lápiz y la goma"},
    ],
    mistakes=[
        {"wrong": "Decir «está allá» sin referencia.", "why": "No se compara con otro objeto.", "fix": "Nombra un objeto de referencia y una palabra de posición."},
        {"wrong": "Confundir la derecha de la mesa con la mía.", "why": "No se aclara desde dónde se mira.", "fix": "Di desde dónde miras."},
    ],
    tiers={
        "recovery": [ex("Fila de izquierda a derecha: gato, perro, pez. ¿Qué hay a la derecha del gato?", "El perro", "Viene después del gato."), ex("Misma fila. ¿Qué hay a la izquierda del pez?", "El perro", "Viene antes del pez."), ex("Misma fila. ¿Qué está entre el gato y el pez?", "El perro", "Queda en el medio.")],
        "understand": [
            ex("¿Qué necesitas para decir dónde está un objeto?", "Un objeto de referencia y una palabra de posición", "Se compara con otro."),
            ex("¿Qué significa «arriba»?", "Más alto", "Está en un nivel superior."),
            ex("¿Qué significa «entre»?", "En medio de dos objetos", "Tiene uno a cada lado."),
        ],
        "apply": [
            ex("Un libro está sobre una mesa. ¿Está arriba o abajo de la mesa?", "Arriba", "Se apoya encima."),
            ex("Un perro está debajo de la mesa. ¿Está arriba o abajo de ella?", "Abajo", "Está en un nivel inferior."),
            ex("Fila: manzana, plátano, uva, kiwi. ¿Qué está a la izquierda de la uva?", "El plátano", "Viene antes de la uva."),
        ],
        "reason": [
            ex("Ema dice que «el lápiz está a la derecha» sin decir de qué. ¿Qué falta?", "Un objeto de referencia", "Hay que decir a la derecha de qué."),
            ex("Dos niños miran una mesa desde lados opuestos. ¿Verán lo mismo a su derecha?", "No", "Cada uno tiene su derecha."),
        ],
        "challenge": [
            ex("Fila de izquierda a derecha: A, B, C, D. Describe la posición de C usando entre.", "Entre B y D", "B está a su izquierda y D a su derecha."),
            ex("Fila de izquierda a derecha: A, B, C, D. ¿Qué letra está dos lugares a la derecha de A?", "C", "Hay B y luego C."),
        ],
    },
    context=[ex("En un estante hay: arriba un libro, en el medio una caja y abajo una pelota. ¿Qué hay entre el libro y la pelota?", "La caja", "Está en el medio.")],
    selfcheck=[ex("En la fila rojo, azul, verde, ¿qué hay a la derecha del azul?", "Verde", "Viene después del azul."), ex("¿Está el techo arriba o abajo del piso?", "Arriba", "Está más alto."), ex("¿Qué debo decir además de «derecha»?", "A la derecha de qué", "Se necesita referencia.")],
    open_task=task("Dibuja tres objetos en fila sobre una mesa: un lápiz, un libro y una goma. Escribe dos frases que digan dónde está cada uno respecto de los otros usando derecha, izquierda y entre.", "El libro está entre el lápiz y la goma. La goma está a la derecha del libro.", ["dibuja tres objetos", "usa dos palabras de posición", "nombra la referencia"], ["dibujo", "dos frases"], ["no nombrar la referencia", "invertir derecha e izquierda"], "Pide leer las frases mientras señala los objetos."),
    reinforce="Describe la posición de tres objetos de tu escritorio.",
    extend="Describe la posición de un objeto sin nombrarlo y pide que otra persona lo adivine.",
)

register(
    OA13, 3,
    materials="Un recorrido de cuadrados dibujado en este cuaderno con una flecha de inicio y objetos descritos; lápiz.",
    use="Aprenderé a dar y seguir instrucciones precisas para moverse. Sirve para guiar a otra persona hacia un lugar.",
    prior=["Sé decir derecha e izquierda.", "Sé nombrar posiciones."],
    explain=[
        "Una instrucción precisa dice qué hacer, hacia dónde y cuánto. Por ejemplo: «avanza 3 pasos, gira a la derecha y avanza 2 pasos». Sin cantidad ni dirección, la persona puede equivocarse.",
        "Para dar buenas instrucciones, piensa desde el lugar de quien las sigue. Si la persona mira de espaldas a ti, tu derecha es su izquierda. Primero di hacia dónde mira y luego las instrucciones.",
        "Para seguir instrucciones, imagina que estás en el lugar y mira de frente. Hazlas una por una. Si algo no se entiende, pide aclararla. Luego comprueba si llegaste al lugar esperado.",
    ],
    vocab=[("instrucción", "una orden clara"), ("avanzar", "ir hacia adelante"), ("girar", "cambiar la dirección"), ("pasos", "cantidad de avances"), ("precisa", "clara y exacta")],
    worked=[
        {"title": "Seguir una instrucción", "problem": "Estás mirando hacia arriba en la hoja. «Avanza 3 cuadrados, gira a la derecha y avanza 2.» ¿Dónde terminas?", "steps": ["Avanzo 3 hacia arriba.", "Giro a la derecha: ahora miro hacia la derecha de la hoja.", "Avanzo 2 hacia la derecha."], "answer": "3 cuadrados arriba y 2 a la derecha"},
        {"title": "Dar una instrucción", "problem": "Guía a un compañero de un lápiz a una goma que está 4 cuadrados a su izquierda.", "steps": ["Pregunto hacia dónde mira.", "Digo: «gira a la izquierda».", "Digo: «avanza 4 cuadrados»."], "answer": "Gira a la izquierda y avanza 4 cuadrados"},
    ],
    mistakes=[
        {"wrong": "Decir «ve por allá».", "why": "No hay dirección ni cantidad.", "fix": "Usa una dirección y un número de pasos."},
        {"wrong": "Dar la derecha según uno mismo cuando el otro mira al revés.", "why": "No se piensa desde el otro.", "fix": "Piensa desde donde está parado quien sigue."},
    ],
    tiers={
        "recovery": [ex("«Avanza 2 cuadrados.» ¿Qué dice la instrucción?", "Cuánto avanzar", "Da una cantidad."), ex("«Gira a la derecha.» ¿Qué cambia?", "La dirección en que miro", "Cambia hacia dónde miro."), ex("¿Qué falta en «gira»?", "Hacia qué lado", "Debe decir derecha o izquierda.")],
        "understand": [
            ex("¿Qué debe tener una instrucción precisa?", "Dirección y cantidad", "Para no equivocarse."),
            ex("¿Desde dónde hay que pensar para dar la derecha a otra persona?", "Desde el lugar de ella", "Su derecha puede ser mi izquierda."),
            ex("Si no entiendo una instrucción, ¿qué hago?", "Pido que la aclaren", "Es mejor que adivinar."),
        ],
        "apply": [
            ex("Miras hacia arriba. «Avanza 2, gira a la derecha y avanza 3.» ¿Dónde terminas?", "2 cuadrados arriba y 3 a la derecha", "Cada instrucción se hace en orden."),
            ex("Miras hacia arriba. «Gira a la izquierda y avanza 4.» ¿Hacia dónde avanzas?", "Hacia la izquierda", "Giraste a la izquierda."),
            ex("Escribe una instrucción para ir 3 cuadrados hacia arriba y luego 1 a la derecha.", "Avanza 3, gira a la derecha y avanza 1", "Dirección y cantidad."),
        ],
        "reason": [
            ex("Luis dice «avanza» sin decir cuánto. ¿Qué problema hay?", "No se sabe cuánto avanzar", "Falta la cantidad."),
            ex("Una niña mira hacia mí. Para que gire a su derecha, ¿hacia mi lado debe girar?", "Hacia mi izquierda", "Estamos uno frente al otro."),
        ],
        "challenge": [
            ex("Miras hacia arriba. «Avanza 1, gira a la derecha, avanza 1, gira a la derecha, avanza 1.» ¿Hacia dónde miras al final?", "Hacia abajo", "Dos giros a la derecha dan media vuelta."),
            ex("Escribe una instrucción de tres pasos que te lleve del inicio a un cuadrado 2 arriba y 2 a la izquierda.", "Avanza 2, gira a la izquierda y avanza 2", "Dirección y cantidad."),
        ],
    },
    context=[ex("Una niña está en la puerta mirando hacia la sala. Debe llegar a su silla, que está 3 pasos adelante y luego 1 paso a su derecha. Escribe la instrucción.", "Avanza 3 pasos, gira a la derecha y avanza 1 paso", "Tiene dirección y cantidad.")],
    selfcheck=[ex("«Avanza 5» ¿tiene cantidad?", "Sí, 5", "El 5 dice cuánto avanzar."), ex("«Gira» solo, ¿es precisa?", "No", "Falta el lado."), ex("¿Qué se hace primero para dar una instrucción a alguien?", "Ver hacia dónde mira", "Para elegir derecha o izquierda.")],
    open_task=task("En un cuadriculado dibuja una flecha de inicio (mirando hacia arriba) y una estrella a 3 cuadrados arriba y 2 a la derecha. Escribe la instrucción para llegar a la estrella y pídele a alguien que la siga.", "Avanza 3 cuadrados, gira a la derecha y avanza 2 cuadrados. La persona llegó a la estrella.", ["marca inicio y estrella", "instrucción con dirección y cantidad", "comprueba que llega"], ["dibujo", "instrucción", "resultado"], ["falta de cantidad", "confundir derecha e izquierda"], "Pide seguir las instrucciones con el dedo."),
    reinforce="Guía a un compañero de ojos cerrados con instrucciones de avance y giro.",
    extend="Escribe las instrucciones de ida y de vuelta entre dos objetos.",
)

register(
    OA13, 4,
    materials="Un plano simple de una sala con cuadrados y objetos descritos; lápiz de color.",
    use="Aprenderé a ubicar objetos en un plano simple con filas y columnas. Sirve para encontrar un lugar en un mapa y describirlo.",
    prior=["Sé decir derecha e izquierda.", "Sé seguir instrucciones."],
    explain=[
        "Un plano simple muestra un lugar visto desde arriba, con cuadrados para ubicar objetos. Cada cuadrado tiene una fila (horizontal) y una columna (vertical). Para decir dónde está un objeto, nombra la fila y la columna.",
        "Por ejemplo, la mesa está en la fila 2, columna 3: la ubicas bajando 2 desde arriba y avanzando 3 desde la izquierda. Primero la fila y luego la columna, siempre en el mismo orden.",
        "Puedes describir una posición usando derecha e izquierda: «la silla está a la derecha de la mesa». Y puedes dibujar un plano de tu mesa o tu pieza para ubicar objetos.",
    ],
    vocab=[("plano", "dibujo de un lugar visto desde arriba"), ("fila", "línea horizontal de cuadrados"), ("columna", "línea vertical de cuadrados"), ("cuadrado", "casilla del plano"), ("ubicación", "lugar donde está algo")],
    worked=[
        {"title": "Leer un plano", "problem": "En un plano, la mesa está en la fila 2, columna 3. ¿Cómo la encuentras?", "steps": ["Parto en la esquina de arriba a la izquierda.", "Bajo 2 filas.", "Avanzo 3 columnas a la derecha."], "answer": "Fila 2, columna 3"},
        {"title": "Describir una posición", "problem": "La silla está en la fila 2, columna 4. ¿Dónde está respecto de la mesa (fila 2, columna 3)?", "steps": ["Están en la misma fila.", "La silla está una columna más a la derecha.", "Está a la derecha de la mesa."], "answer": "A la derecha de la mesa"},
    ],
    mistakes=[
        {"wrong": "Decir primero la columna y luego la fila sin aclararlo.", "why": "Se pierde el orden.", "fix": "Siempre fila primero y luego columna."},
        {"wrong": "Contar desde la esquina equivocada.", "why": "No se fija el inicio.", "fix": "Cuenta desde la esquina de arriba a la izquierda."},
    ],
    tiers={
        "recovery": [ex("¿Qué es una fila en un plano?", "Una línea horizontal de cuadrados", "Va de lado a lado."), ex("¿Qué es una columna en un plano?", "Una línea vertical de cuadrados", "Va de arriba a abajo."), ex("¿Desde dónde parto a contar?", "Desde la esquina de arriba a la izquierda", "Es el inicio acordado.")],
        "understand": [
            ex("Mesa: fila 2, columna 3. ¿Qué número va primero al describir la ubicación?", "La fila", "Es el orden acordado."),
            ex("¿Dos objetos pueden estar en la misma fila?", "Sí", "Con distintas columnas."),
            ex("Silla: fila 2, columna 4; mesa: fila 2, columna 3. ¿Cuál está más a la derecha?", "La silla", "Su columna es mayor."),
        ],
        "apply": [
            ex("Pelota: fila 1, columna 1. ¿Está en la esquina de arriba a la izquierda?", "Sí", "Es el inicio del plano."),
            ex("Cama: fila 3, columna 2. ¿Cuántas filas bajas y cuántas columnas avanzas desde la esquina?", "Bajas 3 filas y avanzas 2 columnas", "Fila primero y columna después."),
            ex("Lámpara: fila 1, columna 4. Libro: fila 1, columna 2. ¿Cuál está a la derecha?", "La lámpara", "Su columna es 4."),
        ],
        "reason": [
            ex("Pía dice que fila 2, columna 3 y fila 3, columna 2 son el mismo lugar. ¿Tiene razón?", "No", "Cambian la fila y la columna."),
            ex("Para describir que una silla está justo debajo de la mesa (fila 2, columna 3), ¿en qué fila y columna está?", "Fila 3, columna 3", "Una fila más abajo, misma columna."),
        ],
        "challenge": [
            ex("Un objeto está en la fila 2, columna 2. Otro está 2 columnas a la derecha. ¿Dónde está el otro?", "Fila 2, columna 4", "2 + 2 = 4."),
            ex("¿En cuántos cuadrados distintos puede estar un objeto en un plano de 3 filas y 3 columnas?", "9", "3 × 3 = 9."),
        ],
    },
    context=[ex("En un plano de una sala, el escritorio de la profesora está en la fila 1, columna 3. Tu puesto está en la fila 3, columna 3. ¿Cuántas filas hay entre su escritorio y tu puesto?", "1", "Entre la fila 1 y la fila 3 está la fila 2.")],
    selfcheck=[ex("Objeto en fila 1, columna 2. ¿Cuántas filas bajas?", "1", "Es la primera fila."), ex("¿Qué indica la columna?", "Cuántos cuadrados avanzo a la derecha", "Se cuenta desde la izquierda."), ex("¿Se puede dibujar un plano de la mesa?", "Sí", "Es una vista desde arriba.")],
    open_task=task("Dibuja un plano de 3 filas por 3 columnas. Pon un libro en la fila 1, columna 1, un lápiz en la fila 2, columna 3 y una goma en la fila 3, columna 2. Escribe una frase que describa dónde está la goma respecto del lápiz.", "La goma está en la fila 3, columna 2: una fila más abajo y una columna a la izquierda del lápiz.", ["ubica los tres objetos", "usa filas y columnas", "describe una posición relativa"], ["plano", "frase"], ["invertir fila y columna", "ubicar mal un objeto"], "Pide señalar con el dedo cada ubicación."),
    reinforce="Juega a la batalla naval simple con un plano de 3 por 3.",
    extend="Dibuja un plano de tu pieza y escribe tres ubicaciones.",
)

# ---------------------------------------------------------------- OA 14
register(
    OA14, 1,
    materials="Objetos de la sala y figuras dibujadas en este cuaderno: cuadrado ■, círculo ●, triángulo ▲ y rectángulo ▬.",
    use="Aprenderé a reconocer figuras planas (círculo, cuadrado, triángulo, rectángulo) en los objetos que me rodean. Sirve para describir y comparar objetos.",
    prior=["Sé nombrar objetos de la sala.", "Sé comparar formas."],
    explain=[
        "Una figura plana es una forma sin grosor, como las que dibujas en una hoja. El círculo es redondo y no tiene lados. El cuadrado tiene 4 lados iguales. El rectángulo tiene 4 lados y dos son más largos. El triángulo tiene 3 lados.",
        "Muchos objetos tienen partes con estas figuras: la tapa de un tarro es un círculo, la cara de un dado es un cuadrado, una hoja de cuaderno es un rectángulo, un cartel de aviso puede ser un triángulo.",
        "Para reconocer una figura, cuenta los lados y fíjate si hay esquinas. El círculo no tiene esquinas. Si un objeto tiene bordes rectos y cuatro esquinas, puede ser un cuadrado o un rectángulo; mide los lados para saber cuál.",
    ],
    vocab=[("figura plana", "forma sin grosor"), ("lado", "borde recto de una figura"), ("esquina", "lugar donde se juntan dos lados"), ("círculo", "figura redonda sin lados"), ("triángulo", "figura con 3 lados")],
    worked=[
        {"title": "Contar lados", "problem": "Una figura tiene 3 lados y 3 esquinas. ¿Cuál es?", "steps": ["Cuento: 3 lados.", "Cuento: 3 esquinas.", "Es un triángulo."], "answer": "Triángulo"},
        {"title": "Figura en un objeto", "problem": "La tapa de un tarro es redonda. ¿Qué figura tiene?", "steps": ["No tiene lados ni esquinas.", "La tapa del tarro es redonda.", "Es un círculo."], "answer": "Círculo"},
    ],
    mistakes=[
        {"wrong": "Llamar cuadrado a cualquier figura con 4 lados.", "why": "No se miran los lados iguales.", "fix": "El cuadrado tiene 4 lados iguales; el rectángulo tiene dos largos y dos cortos."},
        {"wrong": "Decir que el círculo tiene un lado.", "why": "Se confunde borde y lado.", "fix": "El círculo no tiene lados rectos ni esquinas."},
    ],
    tiers={
        "recovery": [ex("¿Cuántos lados tiene un triángulo?", "3", "Por eso se llama así."), ex("¿Cuántos lados tiene un cuadrado?", "4", "Y los 4 son iguales."), ex("¿Qué figura no tiene esquinas?", "El círculo", "El círculo es redondo, sin lados rectos.")],
        "understand": [
            ex("¿En qué se parecen el cuadrado y el rectángulo?", "Los dos tienen 4 lados y 4 esquinas", "Se diferencian por el largo de los lados."),
            ex("¿En qué se diferencian?", "El cuadrado tiene los 4 lados iguales; el rectángulo no", "Es lo que los distingue."),
            ex("¿Qué figura tiene una moneda de frente?", "Círculo", "La tapa del tarro es redonda."),
        ],
        "apply": [
            ex("¿Qué figura es la cara de un dado?", "Cuadrado", "Tiene 4 lados iguales."),
            ex("¿Qué figura es una hoja de cuaderno?", "Rectángulo", "Dos lados más largos."),
            ex("¿Qué figura es una señal de «ceda el paso» (pico hacia abajo)?", "Triángulo", "Tiene 3 lados."),
        ],
        "reason": [
            ex("Pía dice que una ventana con 4 lados iguales es un rectángulo. ¿Hay otra manera de llamarla?", "Cuadrado", "El cuadrado es un caso especial con 4 lados iguales."),
            ex("¿Por qué un círculo no es un polígono con lados rectos?", "Porque su borde es curvo", "No tiene lados rectos."),
        ],
        "challenge": [
            ex("Una figura tiene 4 lados, 2 largos y 2 cortos. ¿Qué figura es?", "Rectángulo", "Los lados no son todos iguales."),
            ex("¿Cuántas esquinas hay entre un triángulo y un cuadrado juntos?", "7", "3 + 4 = 7."),
        ],
    },
    context=[ex("En la sala hay un reloj redondo, un pizarrón rectangular y una banderita triangular. Nombra la figura de cada uno.", "Círculo, rectángulo y triángulo", "Cada objeto tiene una figura distinta.")],
    selfcheck=[ex("¿Cuántos lados tiene un rectángulo?", "4", "Dos largos y dos cortos."), ex("¿Qué figura es una pelota vista de frente?", "Círculo", "La tapa del tarro es redonda."), ex("¿Qué figura tiene 3 esquinas?", "Triángulo", "Tiene 3 lados.")],
    open_task=task("Busca en tu casa tres objetos que tengan una figura plana (círculo, cuadrado, rectángulo o triángulo). Dibuja cada uno, escribe el nombre del objeto y de la figura y cuántos lados y esquinas tiene.", "Plato: círculo, 0 lados, 0 esquinas. Ventana: rectángulo, 4 lados, 4 esquinas. Cartel: triángulo, 3 lados, 3 esquinas.", ["tres objetos distintos", "nombra la figura", "cuenta lados y esquinas"], ["tres dibujos", "tabla"], ["contar mal los lados", "confundir cuadrado y rectángulo"], "Pide recorrer los bordes con el dedo para contar."),
    reinforce="Recorta un círculo, un cuadrado y un triángulo y pégalos en tu cuaderno.",
    extend="Busca un objeto con dos figuras diferentes, por ejemplo una casa con cuadrado y triángulo.",
)

register(
    OA14, 2,
    materials="Objetos de la sala y cuerpos dibujados en este cuaderno: caja (paralelepípedo), dado (cubo), pelota (esfera), tarro (cilindro).",
    use="Aprenderé a reconocer cuerpos que ruedan y cuerpos que se apilan. Sirve para elegir cómo guardar o transportar objetos.",
    prior=["Sé reconocer figuras planas.", "Sé qué es rodar."],
    explain=[
        "Los cuerpos geométricos son objetos que ocupan espacio, con alto, ancho y largo. Algunos tienen partes curvas y otros sólo partes planas. La pelota es una esfera: es toda curva, rueda hacia todos lados y no se apila.",
        "El tarro es un cilindro: tiene dos tapas planas y un lado curvo. Rueda de lado, pero se apila parado. La caja es un paralelepípedo y el dado es un cubo: tienen caras planas, no ruedan y se apilan fácilmente.",
        "Para clasificar, pregúntate: ¿rueda? ¿Se apila? Prueba con objetos reales empujando y apilando. Anota tus resultados en una tabla: así comparas todos con orden.",
    ],
    vocab=[("cuerpo geométrico", "objeto que ocupa espacio"), ("esfera", "cuerpo redondo como una pelota"), ("cilindro", "cuerpo con dos tapas planas y un lado curvo"), ("cubo", "cuerpo con 6 caras cuadradas"), ("apilar", "poner uno sobre otro")],
    worked=[
        {"title": "Clasificar por rodar", "problem": "¿Rueda una pelota? ¿Se apila?", "steps": ["Es toda curva: rueda hacia todos lados.", "No tiene caras planas: no se apila bien."], "answer": "Rueda; no se apila"},
        {"title": "Un cilindro", "problem": "¿Qué pasa con un tarro cilíndrico?", "steps": ["De lado, su parte curva rueda.", "Parado, sus tapas planas lo apilan."], "answer": "Rueda de lado y se apila parado"},
    ],
    mistakes=[
        {"wrong": "Decir que todo lo que se apila rueda.", "why": "Se mezclan las dos propiedades.", "fix": "Rodar necesita parte curva; apilar necesita cara plana."},
        {"wrong": "Decir que la caja rueda.", "why": "No se prueba.", "fix": "La caja tiene caras planas y no rueda."},
    ],
    tiers={
        "recovery": [ex("¿Rueda una pelota?", "Sí", "Es toda curva."), ex("¿Rueda un dado?", "No", "Tiene caras planas."), ex("¿Se apila un dado sobre otro?", "Sí", "Tiene caras planas.")],
        "understand": [
            ex("¿Qué necesita un cuerpo para rodar?", "Una parte curva", "Las caras planas no ruedan."),
            ex("¿Qué necesita un cuerpo para apilarse?", "Una cara plana", "Se apoya y sostiene."),
            ex("¿Cuál cuerpo rueda y se apila (según cómo se ponga)?", "El cilindro", "Rueda de lado y se apila parado."),
        ],
        "apply": [
            ex("Clasifica: pelota. ¿Rueda? ¿Se apila?", "Rueda; no se apila bien", "La pelota es toda curva."),
            ex("Clasifica: caja de zapatos. ¿Rueda? ¿Se apila?", "No rueda; se apila", "La caja tiene todas sus caras planas."),
            ex("Clasifica: tarro de conserva. ¿Rueda? ¿Se apila?", "Rueda de lado; se apila parado", "Es un cilindro: lado curvo y tapas planas."),
        ],
        "reason": [
            ex("Ana dice que un cubo rueda como una pelota. ¿Qué error comete?", "El cubo tiene caras planas y no rueda", "Sólo lo curvo rueda."),
            ex("¿Por qué se guardan latas apiladas en las tiendas?", "Porque sus tapas son planas", "Se apoyan unas sobre otras."),
        ],
        "challenge": [
            ex("¿Cuántas caras planas tiene un cubo?", "6", "Las seis caras del cubo son planas."),
            ex("¿Cuántas caras planas tiene un cilindro?", "2", "Las dos tapas."),
        ],
    },
    context=[ex("Para guardar pelotas, latas y cajas en una bodega, ¿qué conviene poner en el piso con una barrera para que no rueden?", "Pelotas y latas de lado", "Los cuerpos con partes curvas ruedan.")],
    selfcheck=[ex("¿Una caja rueda?", "No", "Tiene caras planas."), ex("¿Una esfera se apila?", "No", "No tiene cara plana."), ex("¿Qué cuerpo es un dado?", "Cubo", "Tiene 6 caras cuadradas.")],
    open_task=task("Con tres objetos de tu casa (una pelota o fruta redonda, una caja y un tarro), pruébalos: empuja cada uno y trata de apilarlo. Anota en una tabla si rueda y si se apila.", "Pelota: rueda, no se apila. Caja: no rueda, se apila. Tarro: rueda de lado, se apila parado.", ["prueba los tres", "anota en tabla", "relaciona con partes planas y curvas"], ["tabla", "conclusión"], ["no probar", "anotar sin ver"], "Pide mostrar el experimento."),
    reinforce="Haz una torre con cajas y observa qué cuerpos se caen.",
    extend="Busca un objeto que ruede y se apile y explica cómo lo logras.",
)

register(
    OA14, 3,
    materials="Cuerpos y huellas descritos en cada ejercicio: cubo, caja, cilindro, pirámide y cono; papel y témpera o lápiz.",
    use="Aprenderé que las caras de los cuerpos dejan figuras planas al apoyarlas. Sirve para relacionar cuerpos con figuras.",
    prior=["Sé reconocer figuras planas.", "Sé reconocer cuerpos que ruedan y se apilan."],
    explain=[
        "Si apoyas un cuerpo con tinta sobre una hoja, la cara plana deja una huella con forma de figura plana. El cubo deja un cuadrado. La caja deja un rectángulo. El cilindro deja un círculo. La pirámide deja un triángulo o un cuadrado, según la cara.",
        "Una cara es una parte plana de un cuerpo. Un cubo tiene 6 caras, todas cuadradas. Una caja tiene 6 caras rectangulares. Un cilindro tiene 2 caras circulares y una superficie curva que no deja huella plana.",
        "Para predecir la huella, mira la cara con que lo apoyas. Si es cuadrada, la huella es un cuadrado; si es redonda, un círculo. La esfera no tiene caras planas, así que sólo deja un punto.",
    ],
    vocab=[("cara", "parte plana de un cuerpo"), ("huella", "marca que deja una cara en la hoja"), ("pirámide", "cuerpo con un triángulo en cada lado y una base"), ("cono", "cuerpo con una base circular y un vértice"), ("superficie curva", "parte redondeada que no es plana")],
    worked=[
        {"title": "Predecir una huella", "problem": "Apoyas un dado con tinta. ¿Qué figura queda?", "steps": ["Las caras del dado son cuadradas.", "Al apoyar una, queda un cuadrado."], "answer": "Cuadrado"},
        {"title": "Cilindro", "problem": "Apoyas un tarro parado. ¿Qué figura queda?", "steps": ["La tapa es redonda.", "La huella es un círculo."], "answer": "Círculo"},
    ],
    mistakes=[
        {"wrong": "Decir que la esfera deja un círculo.", "why": "No tiene cara plana.", "fix": "Sólo deja un punto pequeño."},
        {"wrong": "Decir que el cono tiene cara cuadrada.", "why": "Se confunde con la pirámide.", "fix": "La base del cono es un círculo."},
    ],
    tiers={
        "recovery": [ex("¿Qué figura deja una cara de un cubo?", "Cuadrado", "Sus caras son cuadradas."), ex("¿Qué figura deja una tapa de un tarro?", "Círculo", "La tapa del tarro es redonda."), ex("¿Qué figura deja una cara de una caja de zapatos?", "Rectángulo", "Sus caras son rectángulos.")],
        "understand": [
            ex("¿Qué es una cara?", "Una parte plana de un cuerpo", "Se puede apoyar."),
            ex("¿Cuántas caras tiene un cubo?", "6", "Las seis caras del cubo son cuadradas."),
            ex("¿Una esfera deja una figura plana grande?", "No", "No tiene caras planas."),
        ],
        "apply": [
            ex("Apoyas la base de un cono. ¿Qué figura dejas?", "Círculo", "La base es redonda."),
            ex("Apoyas un lado triangular de una pirámide. ¿Qué figura dejas?", "Triángulo", "Esa cara es triangular."),
            ex("Apoyas una cara de una caja. ¿Qué figuras podrían quedar?", "Rectángulos", "Las caras de la caja son rectángulos."),
        ],
        "reason": [
            ex("Pablo dice que un cilindro deja un cuadrado. ¿Qué error comete?", "Deja un círculo", "Sus tapas son redondas."),
            ex("¿Por qué una pelota no deja una figura grande?", "Porque no tiene cara plana", "Sólo toca la hoja en un punto."),
        ],
        "challenge": [
            ex("¿Cuántas figuras distintas pueden dejar las caras de una pirámide de base cuadrada?", "2", "Un cuadrado y triángulos."),
            ex("¿Cuántas caras tiene una caja de zapatos?", "6", "La caja tiene seis caras rectangulares."),
        ],
    },
    context=[ex("Una profesora estampa con una caja de cartón, un tarro y un dado. ¿Qué figuras salen?", "Rectángulo, círculo y cuadrado", "Cada cuerpo deja la figura de su cara.")],
    selfcheck=[ex("¿Qué figura deja un dado?", "Cuadrado", "Sus caras son cuadradas."), ex("¿Qué figura deja un tarro de pie?", "Círculo", "La tapa es redonda."), ex("¿Qué cuerpo no deja figuras planas?", "La esfera", "No tiene caras planas.")],
    open_task=task("Con tinta o lápiz suave, apoya sobre una hoja un dado, una caja y un tarro. Marca la huella de cada uno, escribe el nombre del cuerpo y de la figura, y cuántos lados tiene la figura.", "Dado: cuadrado, 4 lados. Caja: rectángulo, 4 lados. Tarro: círculo, 0 lados.", ["tres huellas", "nombra el cuerpo y la figura", "cuenta los lados"], ["huellas", "tabla"], ["confundir figura con cuerpo", "contar mal lados"], "Pide predecir la figura antes de estampar."),
    reinforce="Estampa con otros objetos de tu casa y clasifica las huellas.",
    extend="Busca un cuerpo que deje dos figuras distintas según la cara con que lo apoyes.",
)

register(
    OA14, 4,
    materials="Cuerpos y figuras descritos en cada ejercicio; barras de plasticina o palitos; lápiz.",
    use="Aprenderé a clasificar figuras y cuerpos por sus características y a construir con ellos. Sirve para organizar formas y armar modelos.",
    prior=["Sé reconocer figuras planas y cuerpos.", "Sé relacionar caras con figuras."],
    explain=[
        "Clasificar es agrupar según una característica. Para las figuras puedes agrupar por número de lados: 0 (círculo), 3 (triángulo) o 4 (cuadrado y rectángulo). Para los cuerpos puedes agrupar por si ruedan o por la figura de sus caras.",
        "Construir con formas es juntar figuras y cuerpos para crear algo, como una casa con un cubo y una pirámide o un cohete con un cilindro y un cono. Describe tu construcción nombrando cada pieza y su figura.",
        "Para comprobar tu clasificación, usa un criterio claro y revisa que todo lo del grupo lo cumpla. Si algo no lo cumple, cámbialo de grupo.",
    ],
    vocab=[("clasificar", "agrupar según una característica"), ("criterio", "la regla para agrupar"), ("construir", "armar algo juntando piezas"), ("característica", "algo que describe una forma"), ("grupo", "conjunto de formas con algo en común")],
    worked=[
        {"title": "Clasificar figuras", "problem": "Clasifica por lados: círculo, triángulo, cuadrado, rectángulo.", "steps": ["Sin lados: círculo.", "3 lados: triángulo.", "4 lados: cuadrado y rectángulo."], "answer": "0 lados: círculo; 3 lados: triángulo; 4 lados: cuadrado y rectángulo"},
        {"title": "Construir", "problem": "Describe un cohete con cilindro y cono.", "steps": ["El cuerpo es un cilindro.", "La punta es un cono.", "Las ventanas son círculos."], "answer": "Un cilindro, un cono y círculos"},
    ],
    mistakes=[
        {"wrong": "Clasificar sin un criterio claro.", "why": "Se agrupa al azar.", "fix": "Elige una característica y revisa que todos la cumplan."},
        {"wrong": "Mezclar figuras y cuerpos en un mismo grupo.", "why": "No se distinguen.", "fix": "Las figuras son planas y los cuerpos ocupan espacio."},
    ],
    tiers={
        "recovery": [ex("Cuento los bordes rectos de un cuadrado. ¿Cuántos son?", "4", "Los cuatro iguales."), ex("¿Qué cuerpo tiene 6 caras cuadradas?", "Cubo", "Es un dado."), ex("¿Qué figura no tiene lados rectos?", "Círculo", "El círculo es redondo, sin lados rectos.")],
        "understand": [
            ex("¿Qué es un criterio para clasificar?", "La regla para agrupar", "Dice qué comparte el grupo."),
            ex("¿Pertenecen el cuadrado y el rectángulo al mismo grupo si el criterio es «4 lados»?", "Sí", "Los dos tienen 4 lados."),
            ex("¿Pertenecen la esfera y el cilindro al mismo grupo si el criterio es «rueda»?", "Sí", "Ambos tienen parte curva."),
        ],
        "apply": [
            ex("Clasifica por rueda/no rueda: pelota, caja, tarro, dado.", "Ruedan: pelota y tarro. No ruedan: caja y dado", "Los curvos ruedan."),
            ex("Clasifica por lados: triángulo, círculo, rectángulo, cuadrado.", "0: círculo; 3: triángulo; 4: rectángulo y cuadrado", "Se cuentan los lados."),
            ex("Dibuja una casa con un cuadrado y un triángulo.", "Cuadrado para el cuerpo y triángulo para el techo", "Cada figura cumple una función."),
        ],
        "reason": [
            ex("Ema puso un círculo en el grupo de «4 lados». ¿Qué error comete?", "El círculo no tiene lados", "No cumple el criterio."),
            ex("¿Pueden dos personas clasificar las mismas formas de distinta manera?", "Sí, si usan criterios distintos", "El criterio decide el grupo."),
        ],
        "challenge": [
            ex("Con un cilindro, un cono y un cubo, inventa una construcción y nómbrala.", "Por ejemplo, un cohete con cilindro, cono y cubo como base", "Hay que usar las tres piezas."),
            ex("¿Cuántas figuras planas distintas puedes ver en una casa hecha con un cuadrado, un triángulo y dos círculos?", "3", "Cuadrado, triángulo y círculo."),
        ],
    },
    context=[ex("Una tienda quiere guardar balones, cajas y latas. Para que nada ruede, ¿qué debe poner en estantes con tope?", "Balones y latas", "Son cuerpos con partes curvas.")],
    selfcheck=[ex("¿Qué criterio agrupa círculo aparte del cuadrado?", "El número de lados", "Cero y cuatro."), ex("¿Se puede construir con cubos y conos?", "Sí", "Sirven como piezas."), ex("¿Es una esfera una figura plana?", "No", "Es un cuerpo.")],
    open_task=task("Elige cinco formas: círculo, triángulo, cuadrado, pelota y caja. Clasifícalas en dos grupos con un criterio que tú elijas. Escribe el criterio y los dos grupos, y comprueba que todos cumplen.", "Criterio: «tiene bordes rectos». Sí: triángulo, cuadrado, caja. No: círculo, pelota. Comprobé uno por uno.", ["elige un criterio claro", "forma dos grupos", "comprueba cada una"], ["criterio", "dos grupos", "comprobación"], ["criterio ambiguo", "una forma en el grupo equivocado"], "Pide explicar por qué cada forma va en su grupo."),
    reinforce="Arma una torre con tres cuerpos y nombra cada uno.",
    extend="Inventa otro criterio para clasificar las mismas formas y compara los grupos.",
)
