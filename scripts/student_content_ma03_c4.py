"""Student material for 3.º básico Matemática, OA 25 (pictogramas y gráficos de barra con escala) y OA 26 (diagramas de puntos)."""
from __future__ import annotations

from collections import Counter

from student_lessons import arith, ex, register

OA25, OA26 = "MA03 OA 25", "MA03 OA 26"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def lista(items) -> str:
    return ", ".join(str(i) for i in items)


def fila(pares, sym) -> str:
    """Una fila de símbolos por categoría: «Ana: ● ● ●»."""
    return "; ".join(f"{nombre}: {' '.join([sym] * n)}" for nombre, n in pares) + "."


# ---- datos de OA 25 (símbolos por categoría)
LIBROS = [("Ana", 4), ("Beto", 2), ("Carla", 6), ("Diego", 3)]       # ● = 5 libros
VASOS = [("lunes", 5), ("martes", 3), ("miércoles", 6), ("jueves", 4)]  # ▮ = 2 vasos
P_LIBROS = "Pictograma de libros leídos (cada ● vale 5 libros): " + fila(LIBROS, "●")
B_VASOS = "Gráfico de barras de vasos de agua (cada ▮ vale 2 vasos): " + fila(VASOS, "▮")
LIB = dict(LIBROS)
VAS = dict(VASOS)


# ================================================================ OA 25
register(
    OA25, 1,
    materials="Lápiz y papel. Los gráficos están escritos con símbolos en cada ejercicio. Siempre dice cuánto vale cada símbolo.",
    use="Aprenderé a leer la escala de un pictograma o de un gráfico de barras antes de contestar. Sirve para no equivocarme al contar símbolos.",
    prior=["Sé contar de 2 en 2 y de 5 en 5.", "Sé leer una tabla."],
    explain=[
        "Un pictograma usa símbolos para mostrar datos. En muchos pictogramas, un símbolo no vale 1, vale más. Eso lo dice la escala o equivalencia, por ejemplo «cada ● vale 5 libros». Primero lee la escala.",
        "Para saber el valor de una fila, cuenta los símbolos y multiplica por lo que vale cada uno. Si Ana tiene 4 símbolos y cada uno vale 5, entonces 4 × 5 = 20 libros. También puedes contar de 5 en 5: 5, 10, 15, 20.",
        "En un gráfico de barras pasa lo mismo: cada cuadradito o raya vale lo que dice la escala. Si cada ▮ vale 2 y una barra tiene 5 ▮, vale 10. Nunca respondas con la cantidad de símbolos sin pensar en la escala.",
    ],
    vocab=[("pictograma", "gráfico que usa símbolos para mostrar datos"), ("símbolo", "dibujo pequeño que representa una cantidad"), ("escala", "lo que vale cada símbolo o cada cuadradito"), ("equivalencia", "cuánto vale un símbolo, como 1 ● = 5 libros"), ("frecuencia", "cantidad que muestra una fila o una barra")],
    worked=[
        {"title": "Leer un pictograma", "problem": P_LIBROS + " ¿Cuántos libros leyó Carla?", "steps": ["Leo la escala: cada ● vale 5 libros.", "Carla tiene 6 símbolos.", "6 × 5 = 30."], "answer": "30 libros"},
        {"title": "Leer una barra con escala", "problem": B_VASOS + " ¿Cuántos vasos se tomaron el miércoles?", "steps": ["Leo la escala: cada ▮ vale 2 vasos.", "El miércoles tiene 6 ▮.", "6 × 2 = 12."], "answer": "12 vasos"},
    ],
    mistakes=[
        {"wrong": "Responder que Carla leyó 6 libros porque tiene 6 símbolos.", "why": "No se leyó la escala.", "fix": "Multiplica los símbolos por lo que vale cada uno: 6 × 5 = 30."},
        {"wrong": "Contar de 1 en 1 los cuadraditos de una barra con escala de 2.", "why": "Se ignora que cada cuadradito vale 2.", "fix": "Cuenta de 2 en 2."},
    ],
    tiers={
        "recovery": [
            ex(P_LIBROS + " ¿Cuánto vale cada ●?", "5 libros", "Lo dice la escala del pictograma."),
            ex(P_LIBROS + " ¿Cuántos ● tiene Diego?", str(LIB["Diego"]), "Se cuentan los símbolos de su fila."),
            ex("Cada ● vale 5. Una fila tiene 2 ●. ¿Cuánto vale la fila?", "10", "2 × 5 = 10.", calc="2*5"),
        ],
        "understand": [
            arith(P_LIBROS + " ¿Cuántos libros leyó Ana?", f"{LIB['Ana']}*5", "Se multiplican los símbolos por 5."),
            arith(P_LIBROS + " ¿Cuántos libros leyó Beto?", f"{LIB['Beto']}*5", "Se multiplican los símbolos por 5."),
            ex("¿Por qué hay que leer la escala antes de responder?", "Porque cada símbolo puede valer más de 1", "Sin escala se responde mal."),
        ],
        "apply": [
            arith(B_VASOS + " ¿Cuántos vasos se tomaron el lunes?", f"{VAS['lunes']}*2", "Se multiplican los ▮ por 2."),
            arith(B_VASOS + " ¿Cuántos vasos se tomaron el martes?", f"{VAS['martes']}*2", "Se multiplican los ▮ por 2."),
            arith(P_LIBROS + " ¿Cuántos libros leyeron Ana y Diego en total?", f"{LIB['Ana']}*5+{LIB['Diego']}*5", "Se suman los libros de los dos."),
        ],
        "reason": [
            ex(P_LIBROS + " Rosa dice que Carla leyó 6 libros. ¿Qué error cometió?", "No usó la escala; son 30 libros", "Cada ● vale 5 y 6 × 5 = 30.", calc="6*5"),
            ex(B_VASOS + " Pedro cuenta los ▮ del jueves de 1 en 1 y dice 4 vasos. ¿Es correcto?", "No; son 8 vasos", "Cada ▮ vale 2 y 4 × 2 = 8.", calc="4*2"),
        ],
        "challenge": [
            arith(P_LIBROS + " ¿Cuántos libros más leyó Carla que Beto?", f"{LIB['Carla']}*5-{LIB['Beto']}*5", "Se restan los libros de las dos filas."),
            arith(B_VASOS + " ¿Cuántos vasos se tomaron en los cuatro días?", "(" + "+".join(str(n) for _d, n in VASOS) + ")*2", "Se suman todos los ▮ y se multiplica por 2."),
        ],
    },
    context=[arith("En un pictograma de pegatinas cada ● vale 10 pegatinas. Sofía tiene 5 ●. ¿Cuántas pegatinas tiene?", "5*10", "Se multiplican los símbolos por 10.")],
    selfcheck=[
        ex("Cada ● vale 5. ¿Cuánto valen 3 ●?", "15", "3 × 5 = 15.", calc="3*5"),
        ex("Cada ▮ vale 2. ¿Cuánto valen 7 ▮?", "14", "7 × 2 = 14.", calc="7*2"),
        ex("¿Dónde se lee cuánto vale cada símbolo?", "En la escala", "La escala dice la equivalencia."),
    ],
    open_task=task(
        "Usa este pictograma de pegatinas (cada ● vale 10 pegatinas): Luz: ● ● ● ; Mateo: ● ● ● ● ● ; Nora: ● ●. Escribe cuántas pegatinas tiene cada niño y quién tiene más. Explica qué hiciste con la escala.",
        "Luz: 3 × 10 = 30. Mateo: 5 × 10 = 50. Nora: 2 × 10 = 20. Mateo tiene más. Primero leí que cada ● vale 10.",
        ["lee la escala primero", "multiplica los símbolos por 10", "escribe tres cantidades", "dice quién tiene más y explica"],
        ["tres cálculos", "respuesta", "explicación"],
        ["responder con la cantidad de símbolos", "olvidar la escala"],
        "Pide decir en voz alta lo que vale cada ●. Reconoce que multiplique antes de comparar.",
    ),
    reinforce="Dibuja un pictograma de 3 filas donde cada símbolo vale 5 y escribe cuánto vale cada fila.",
    extend="Cambia la escala del pictograma de libros de esta clase a ● = 10. ¿Qué fila no se puede dibujar exacta y por qué?",
)

register(
    OA25, 2,
    materials="Lápiz y papel. Las tablas y la escala de cada pictograma están escritas en los ejercicios.",
    use="Aprenderé a construir un pictograma con una equivalencia, a partir de una tabla de datos. Sirve para mostrar cantidades grandes con pocos dibujos.",
    prior=["Sé leer la escala de un pictograma.", "Sé dividir hasta la tabla del 10."],
    explain=[
        "Para construir un pictograma, primero decide la equivalencia: cuánto vale cada símbolo. Debe ser un número con el que puedas armar todas las cantidades, como 2, 5 o 10. Luego calcula cuántos símbolos necesita cada fila.",
        "Para eso divides la cantidad entre lo que vale un símbolo. Si Pía vendió 20 manzanas y cada ● vale 10, entonces 20 ÷ 10 = 2 símbolos. Si cada ● vale 5, serían 20 ÷ 5 = 4 símbolos.",
        "Al terminar, escribe el título del pictograma y la equivalencia. Revisa que al multiplicar los símbolos por la equivalencia vuelvas a las cantidades de la tabla.",
    ],
    vocab=[("equivalencia", "cuánto vale un símbolo"), ("tabla de datos", "tabla con categorías y cantidades"), ("título", "frase que dice de qué trata el gráfico"), ("calcular los símbolos", "dividir la cantidad entre el valor del símbolo"), ("comprobar", "multiplicar los símbolos por la escala y ver si da la cantidad")],
    worked=[
        {"title": "De la tabla al pictograma", "problem": "Tabla de ventas: manzanas 20, peras 10, uvas 30. Dibuja el pictograma con ● = 10.", "steps": ["Manzanas: 20 ÷ 10 = 2 símbolos.", "Peras: 10 ÷ 10 = 1 símbolo.", "Uvas: 30 ÷ 10 = 3 símbolos."], "answer": "Manzanas ● ●; peras ●; uvas ● ● ●"},
        {"title": "Elegir otra escala", "problem": "Tabla: gatos 15, perros 25. Dibuja con ● = 5.", "steps": ["Gatos: 15 ÷ 5 = 3.", "Perros: 25 ÷ 5 = 5."], "answer": "Gatos ● ● ●; perros ● ● ● ● ●"},
    ],
    mistakes=[
        {"wrong": "Dibujar un símbolo por cada unidad aunque la escala sea 10.", "why": "No se usa la equivalencia.", "fix": "Divide la cantidad entre el valor del símbolo."},
        {"wrong": "No escribir cuánto vale cada símbolo.", "why": "El lector no puede interpretar el gráfico.", "fix": "Escribe siempre la equivalencia junto al título."},
    ],
    tiers={
        "recovery": [
            arith("En un pictograma cada ● vale 10. ¿Cuántos ● se necesitan para 20?", "20//10", "Se divide 20 entre 10."),
            arith("En un pictograma cada ● vale 5. ¿Cuántos ● se necesitan para 15?", "15//5", "Se divide 15 entre 5."),
            ex("¿Qué dos cosas debe llevar un pictograma además de los símbolos?", "Título y escala", "Sin ellas no se entiende."),
        ],
        "understand": [
            arith("Cada ● vale 10. ¿Cuántos ● se necesitan para 30?", "30//10", "Se divide 30 entre 10."),
            arith("Cada ● vale 5. ¿Cuántos ● se necesitan para 25?", "25//5", "Se divide 25 entre 5."),
            ex("Una tabla tiene 12 y 8. ¿Sirve una escala de ● = 5 para dibujarlas exactas?", "No; 12 no se arma con símbolos de 5", "12 no es múltiplo de 5."),
        ],
        "apply": [
            ex("Tabla de juguetes: autos 40, muñecas 20, pelotas 10. Con ● = 10, ¿cuántos ● tiene la fila de autos?", "4", "40 ÷ 10 = 4.", calc="40//10"),
            ex("Tabla: patos 35, gansos 20. Con ● = 5, ¿cuántos ● tiene la fila de patos?", "7", "35 ÷ 5 = 7.", calc="35//5"),
            ex("Tabla de libros prestados: lunes 8, martes 4, miércoles 6. Con ● = 2, ¿cuántos ● tiene el lunes?", "4", "8 ÷ 2 = 4.", calc="8//2"),
        ],
        "reason": [
            ex("Luis dibuja 20 ● para 20 manzanas aunque la escala es ● = 10. ¿Qué error cometió?", "No usó la escala; debía dibujar 2 ●", "20 ÷ 10 = 2."),
            ex("Ana dibuja el pictograma pero no escribe lo que vale cada ●. ¿Qué problema trae?", "Nadie puede saber las cantidades", "La equivalencia es necesaria para leer."),
        ],
        "challenge": [
            ex("Tabla: rojo 40, azul 20, verde 10. Si usas ● = 10, ¿cuántos ● dibujas en total?", "7", "4 + 2 + 1 = 7.", calc="4+2+1"),
            ex("Tabla: rojo 40, azul 20, verde 10. Si usas ● = 5 en vez de 10, ¿cuántos ● dibujas en total?", "14", "8 + 4 + 2 = 14.", calc="8+4+2"),
        ],
    },
    context=[ex("La biblioteca prestó 40 libros el lunes y 30 el martes. Con ● = 10, ¿cuántos ● dibujas para cada día?", "Lunes 4 y martes 3", "40 ÷ 10 = 4 y 30 ÷ 10 = 3.")],
    selfcheck=[
        ex("Con ● = 10, ¿cuántos ● se necesitan para 50?", "5", "50 ÷ 10 = 5.", calc="50//10"),
        ex("Con ● = 5, ¿cuántos ● se necesitan para 10?", "2", "10 ÷ 5 = 2.", calc="10//5"),
        ex("¿Cómo compruebas un pictograma terminado?", "Multiplicando los símbolos por la escala", "Así debes volver a la cantidad de la tabla."),
    ],
    open_task=task(
        "Con esta tabla de goles de un campeonato escolar: Rojo 20, Azul 30, Verde 10, construye un pictograma con ● = 10. Escribe título, equivalencia y comprueba cada fila.",
        "Goles por equipo (● = 10 goles): Rojo ● ●; Azul ● ● ●; Verde ●. Comprobación: 2 × 10 = 20, 3 × 10 = 30, 1 × 10 = 10.",
        ["calcula 2, 3 y 1 símbolos", "dibuja las filas", "escribe título y equivalencia", "comprueba multiplicando"],
        ["pictograma dibujado", "comprobación escrita"],
        ["dibujar un símbolo por cada gol", "olvidar la equivalencia"],
        "Pide decir en voz alta cuánto vale cada ●. Reconoce que compruebe con una multiplicación.",
    ),
    reinforce="Haz un pictograma con ● = 2 para 8 manzanas, 6 peras y 4 plátanos.",
    extend="Haz el mismo pictograma con ● = 4 y explica qué cambia.",
)

register(
    OA25, 3,
    materials="Lápiz, regla y papel cuadriculado. La escala de las barras está escrita en cada ejercicio.",
    use="Aprenderé a completar un gráfico de barras con escala usando los datos de una tabla. Sirve para mostrar y comparar cantidades con barras.",
    prior=["Sé leer un gráfico de barras.", "Sé contar de 5 en 5 y de 10 en 10."],
    explain=[
        "En un gráfico de barras, el eje es la línea con los números. Las rayas del eje avanzan con una escala, por ejemplo 0, 5, 10, 15, 20, de 5 en 5. La barra llega hasta la raya que tiene el número del dato.",
        "Para dibujar una barra, mira el dato en la tabla y busca su número en el eje. Si el dato es 15, la barra llega a la raya del 15. Si la escala es de 5 en 5, esa raya es la tercera después del cero.",
        "Todas las barras empiezan en 0 y tienen el mismo ancho. Escribe el título y qué mide cada eje. Después revisa cada barra con la tabla.",
    ],
    vocab=[("eje", "línea con los números del gráfico"), ("raya del eje", "marca con un número en el eje"), ("barra", "rectángulo que llega hasta el valor del dato"), ("empezar en cero", "todas las barras parten desde el 0"), ("dato", "cantidad de la tabla")],
    worked=[
        {"title": "Hasta dónde llega una barra", "problem": "El eje tiene 0, 5, 10, 15, 20, 25 y 30. El dato de gatos es 15. ¿Hasta qué raya llega la barra?", "steps": ["Busco el 15 en el eje.", "La barra llega hasta la raya del 15."], "answer": "Hasta la raya del 15"},
        {"title": "Cuántas rayas sube", "problem": "Con escala de 5 en 5, ¿cuántas rayas después del 0 sube la barra de 25?", "steps": ["Cuento de 5 en 5: 5, 10, 15, 20, 25.", "Son 5 rayas."], "answer": "5 rayas"},
    ],
    mistakes=[
        {"wrong": "Hacer que una barra no parta de 0.", "why": "Parece más corta o más larga de lo que es.", "fix": "Todas las barras empiezan en el 0."},
        {"wrong": "Dibujar la barra de 25 hasta la quinta raya pensando que el eje va de 1 en 1.", "why": "No se lee la escala.", "fix": "Con escala de 5 en 5, la quinta raya vale 25 y no 5."},
    ],
    tiers={
        "recovery": [
            ex("El eje va de 5 en 5: 0, 5, 10, 15, 20. ¿Qué número viene después del 20?", "25", "Se suma 5 al 20."),
            ex("¿Desde qué número parten todas las barras?", "Desde el 0", "Así se comparan bien."),
            ex("El dato de perros es 10 y el eje va de 5 en 5. ¿Hasta qué raya llega la barra?", "Hasta la raya del 10", "Se busca el 10 en el eje."),
        ],
        "understand": [
            ex("Escala de 5 en 5. ¿Cuántas rayas después del 0 sube una barra de 25?", "5", "5, 10, 15, 20, 25.", calc="25//5"),
            ex("Escala de 10 en 10. ¿Hasta qué raya llega una barra de 30?", "La del 30", "Se busca el 30 en el eje."),
            ex("Escala de 2 en 2. ¿Cuántas rayas después del 0 sube una barra de 8?", "4", "2, 4, 6, 8.", calc="8//2"),
        ],
        "apply": [
            ex("Tabla: gatos 15, perros 25, peces 10. Escala de 5 en 5. ¿Cuántas rayas sube la barra de gatos?", "3", "15 ÷ 5 = 3.", calc="15//5"),
            ex("Tabla: gatos 15, perros 25, peces 10. Escala de 5 en 5. ¿Cuántas rayas sube la barra de peces?", "2", "10 ÷ 5 = 2.", calc="10//5"),
            ex("Tabla: gatos 15, perros 25, peces 10. ¿Qué barra es la más larga?", "La de perros", "25 es el dato mayor."),
        ],
        "reason": [
            ex("Beto dibuja la barra de 25 con 5 rayas pensando que el eje va de 1 en 1. Pero el eje va de 5 en 5. ¿Qué debería haber dibujado?", "Una barra que llegue a la quinta raya, que vale 25", "Con 5 rayas de 5, la barra vale 25."),
            ex("Una barra parte desde 5 y no desde 0. Ana dice que mide lo mismo que otra de igual altura que parte desde 0. ¿Tiene razón?", "No; la que parte desde 5 vale menos", "Las barras deben partir de 0 para compararse."),
        ],
        "challenge": [
            ex("Tabla: Sol 40, Luna 20, Estrella 30. Escala de 10 en 10. ¿Cuántas rayas sube cada barra, en orden Sol, Luna y Estrella?", "4, 2 y 3", "40 ÷ 10 = 4, 20 ÷ 10 = 2 y 30 ÷ 10 = 3."),
            arith("Tabla: gatos 15, perros 25, peces 10. ¿Cuántas mascotas hay en total?", "15+25+10", "Se suman todos los datos."),
        ],
    },
    context=[ex("Una biblioteca anota cuántos libros prestó cada día de la semana: lunes 20, martes 10, miércoles 30. Con escala de 10 en 10, ¿cuántas rayas sube la barra del miércoles?", "3", "30 ÷ 10 = 3.", calc="30//10")],
    selfcheck=[
        ex("Escala de 5 en 5. ¿Cuánto vale la tercera raya después del 0?", "15", "5, 10, 15."),
        ex("¿Dónde empiezan todas las barras?", "En el 0", "Es el inicio del eje."),
        ex("Escala de 10 en 10. ¿Cuántas rayas sube una barra de 50?", "5", "50 ÷ 10 = 5.", calc="50//10"),
    ],
    open_task=task(
        "Con esta tabla de libros prestados: lunes 10, martes 25, miércoles 15, jueves 30, dibuja en papel cuadriculado un gráfico de barras con el eje de 5 en 5. Escribe el título, el 0 en el eje y revisa cada barra con la tabla.",
        "Barras que llegan a 10, 25, 15 y 30. Todas parten desde el 0 y tienen el mismo ancho. Título: libros prestados por día.",
        ["dibuja el eje de 5 en 5", "las cuatro barras llegan a su valor", "todas parten de 0", "escribe el título"],
        ["gráfico dibujado", "revisión con la tabla"],
        ["no partir de 0", "leer el eje de 1 en 1"],
        "Pide señalar la raya de cada dato. Reconoce que las barras queden en el valor correcto.",
    ),
    reinforce="Dibuja un eje de 2 en 2 hasta 12 y marca las rayas del 4, el 8 y el 12.",
    extend="Dibuja el mismo gráfico con eje de 10 en 10. ¿Qué barras quedan entre dos rayas?",
)

register(
    OA25, 4,
    materials="Lápiz y papel. Los dos gráficos de cada ejercicio están escritos con símbolos y con la escala.",
    use="Aprenderé a comparar un pictograma con un gráfico de barras que muestran los mismos datos. Sirve para elegir la forma más clara de mostrar la información.",
    prior=["Sé leer pictogramas y barras con escala.", "Sé multiplicar por 2, 5 y 10."],
    explain=[
        "Los mismos datos se pueden mostrar con una tabla, un pictograma o un gráfico de barras. Aunque se vean distintos, cuentan lo mismo. Para comprobarlo, lee la escala de cada uno y calcula los valores.",
        "En un pictograma, cada fila tiene símbolos. En un gráfico de barras, cada barra tiene un largo. Lo importante es que las escalas pueden ser diferentes: en uno cada símbolo vale 5 y en otro cada cuadradito vale 1.",
        "Para decidir cuál es más claro, piensa en qué quieres ver. El pictograma es entretenido y sirve con cantidades redondas. Las barras sirven mejor cuando los números son muy distintos o no son redondos.",
    ],
    vocab=[("representación", "forma de mostrar datos, como una tabla o un gráfico"), ("mismos datos", "las mismas cantidades"), ("comparar", "ver qué se parece y qué cambia"), ("escala distinta", "cuando cada símbolo vale algo diferente"), ("clara", "fácil de leer")],
    worked=[
        {"title": "Mismos datos, dos gráficos", "problem": P_LIBROS + " Un gráfico de barras muestra a Ana con una barra que llega a la raya del 20. ¿Es el mismo dato?", "steps": ["Ana en el pictograma: 4 × 5 = 20.", "En las barras, la barra de Ana llega a 20."], "answer": "Sí, los dos muestran 20 libros"},
        {"title": "Elegir el gráfico más claro", "problem": "Quieres mostrar 7, 13 y 21 libros. ¿Sirve un pictograma con ● = 10?", "steps": ["Con ● = 10 no se arma exacto el 7, el 13 ni el 21.", "Un gráfico de barras sí puede mostrar esos valores."], "answer": "Conviene el gráfico de barras"},
    ],
    mistakes=[
        {"wrong": "Decir que dos gráficos muestran datos distintos porque se ven distintos.", "why": "No se comparan las escalas.", "fix": "Calcula los valores de cada gráfico y compáralos."},
        {"wrong": "Comparar el número de símbolos de un gráfico con el de otro con distinta escala.", "why": "Cada símbolo vale algo diferente.", "fix": "Pasa todo a la cantidad real antes de comparar."},
    ],
    tiers={
        "recovery": [
            ex("¿Dos gráficos con los mismos datos pueden verse distintos?", "Sí", "Pueden usar símbolos o escalas diferentes."),
            ex(P_LIBROS + " ¿Cuántos libros leyó Diego?", "15", "3 × 5 = 15.", calc="3*5"),
            ex("En un pictograma ● = 5. En otro ● = 10. ¿Un ● vale lo mismo en los dos?", "No", "Cada uno tiene su equivalencia."),
        ],
        "understand": [
            ex("Ana tiene 4 ● en un pictograma con ● = 5. Otro pictograma con ● = 10 muestra el mismo dato. ¿Cuántos ● tiene Ana ahí?", "2", "20 ÷ 10 = 2.", calc="20//10"),
            ex("En un gráfico de barras una barra llega a 15 y en un pictograma hay 4 ● con ● = 5. ¿Muestran el mismo dato?", "No", "4 × 5 = 20 y la barra muestra 15."),
            ex("¿Qué debes hacer antes de comparar dos gráficos con escalas distintas?", "Calcular las cantidades reales", "Los símbolos no valen lo mismo."),
        ],
        "apply": [
            ex("Tabla: Ana 20, Beto 10. En un pictograma con ● = 10, ¿cuántos ● tiene Ana?", "2", "20 ÷ 10 = 2.", calc="20//10"),
            ex("Tabla: Ana 20, Beto 10. En un pictograma con ● = 5, ¿cuántos ● tiene Beto?", "2", "10 ÷ 5 = 2.", calc="10//5"),
            ex("Quieres mostrar 12, 18 y 30. ¿Conviene un pictograma con ● = 10 o un gráfico de barras?", "El gráfico de barras", "Con ● = 10 no se arman 12 ni 18."),
        ],
        "reason": [
            ex("Rosa dice: «el gráfico A tiene 4 símbolos y el B tiene 2, así que A muestra más». En A, ● = 5, y en B, ● = 10. ¿Tiene razón?", "No; los dos muestran 20", "4 × 5 = 20 y 2 × 10 = 20.", calc="4*5"),
            ex("Luis dice que una tabla y un pictograma no pueden mostrar lo mismo. ¿Es cierto?", "No; pueden mostrar los mismos datos", "Es la misma información en otra forma."),
        ],
        "challenge": [
            ex("Un pictograma con ● = 5 tiene Ana 4, Beto 2 y Carla 6 símbolos. Otro con ● = 10 muestra los mismos datos. ¿Cuántos ● tiene Carla ahí?", "3", "6 × 5 = 30 y 30 ÷ 10 = 3.", calc="6*5//10"),
            ex("Un pictograma con ● = 5 tiene Ana 4, Beto 2 y Carla 6 símbolos. Un gráfico de barras tiene escala de 10 en 10. ¿Hasta qué raya llega la barra de Beto?", "Hasta el 10", "2 × 5 = 10."),
        ],
    },
    context=[ex("Un curso muestra sus ventas de calendarios con dos gráficos. En uno, ● = 5 y María tiene 3 ●. En el otro, ▮ = 5 y María tiene 3 ▮. ¿Muestran el mismo dato?", "Sí; 15 calendarios", "3 × 5 = 15 en los dos.", calc="3*5")],
    selfcheck=[
        ex("Con ● = 10, ¿cuántos ● representan 40?", "4", "40 ÷ 10 = 4.", calc="40//10"),
        ex("¿Se pueden mostrar los mismos datos con un pictograma y con barras?", "Sí", "Son dos formas de mostrar lo mismo."),
        ex("En un gráfico ● = 2 y en otro ● = 4. Un dato es 8. ¿Cuántos ● tiene en el segundo?", "2", "8 ÷ 4 = 2.", calc="8//4"),
    ],
    open_task=task(
        "Con esta tabla de bicicletas: Lía 10, Teo 20, Mía 15, muestra los datos de dos formas: (a) un pictograma con ● = 5 y (b) un gráfico de barras con eje de 5 en 5. Escribe cuántos ● y a qué raya llega cada barra, y explica cuál te parece más claro y por qué.",
        "Pictograma: Lía ● ●, Teo ● ● ● ●, Mía ● ● ●. Barras: llegan a 10, 20 y 15. Me parece más claro el de barras porque se comparan los largos. Los dos muestran los mismos datos.",
        ["dibuja ambos gráficos", "usa 2, 4 y 3 símbolos", "las barras llegan a 10, 20 y 15", "explica su elección"],
        ["dos gráficos", "explicación"],
        ["usar símbolos sin escala", "pensar que los gráficos muestran datos distintos"],
        "Pide explicar por qué los dos gráficos dicen lo mismo. Reconoce una elección con razón.",
    ),
    reinforce="Dibuja un pictograma y un gráfico de barras con tres datos inventados y explica qué se parece.",
    extend="Elige una tabla con números no redondos (como 9, 14 y 22) y decide qué gráfico es mejor.",
)

register(
    OA25, 5,
    materials="Lápiz y papel. Los gráficos están descritos con palabras y números en cada ejercicio.",
    use="Aprenderé a detectar gráficos que pueden engañar. Sirve para no creer en una imagen sin revisar la escala.",
    prior=["Sé leer la escala de un gráfico.", "Sé comparar números hasta 100."],
    explain=[
        "Algunos gráficos pueden hacerte pensar algo que no es cierto, aunque tengan datos verdaderos. Para no equivocarte, revisa tres cosas: si las barras parten de 0, si la escala avanza igual en todo el eje y si los símbolos son todos del mismo tamaño.",
        "Por ejemplo, si el eje parte desde 50 y no desde 0, dos barras de 52 y 56 parecen muy distintas, aunque la diferencia es sólo 4. Si la escala salta de 10 en 10 y luego de 30 en 30, la barra parece más baja de lo que es. Y si un símbolo es más grande que otro, parece que hay más.",
        "Un buen gráfico tiene título, escala clara, barras que parten de 0 y símbolos del mismo tamaño. Antes de sacar una conclusión, lee los números y no sólo mires el dibujo.",
    ],
    vocab=[("gráfico engañoso", "gráfico que hace pensar algo que los datos no dicen"), ("eje que no parte de 0", "eje que empieza en un número mayor que cero"), ("escala irregular", "escala que salta distinto en cada tramo"), ("símbolo de otro tamaño", "símbolo más grande o más chico que los demás"), ("revisar", "comprobar antes de concluir")],
    worked=[
        {"title": "Eje que no parte de cero", "problem": "Un gráfico tiene dos barras: A vale 52 y B vale 56. El eje parte en 50. B parece el triple de alta que A. ¿Es cierto?", "steps": ["Miro los números: 52 y 56.", "56 − 52 = 4.", "B no es el triple de A; es sólo un poco mayor."], "answer": "No; la diferencia es sólo 4"},
        {"title": "Símbolos de distinto tamaño", "problem": "En un pictograma, ● = 10 pero el símbolo de Pía es el doble de grande que el de Tomás. Ambos tienen 3 símbolos. ¿Quién tiene más?", "steps": ["Los dos tienen 3 símbolos y cada uno vale 10.", "3 × 10 = 30 para cada uno."], "answer": "Tienen lo mismo, 30 cada uno"},
    ],
    mistakes=[
        {"wrong": "Decir que una barra es el doble de otra sólo porque parece el doble de alta.", "why": "No se revisan los números ni si el eje parte de 0.", "fix": "Lee los valores y resta o divide para comparar."},
        {"wrong": "Ignorar que los símbolos tienen distinto tamaño.", "why": "Se cree que el símbolo más grande vale más.", "fix": "Todos los símbolos deben valer lo mismo y tener el mismo tamaño."},
    ],
    tiers={
        "recovery": [
            ex("¿Desde qué número deben partir las barras de un buen gráfico?", "Desde el 0", "Así las alturas se comparan bien."),
            ex("¿Deben los símbolos de un pictograma tener el mismo tamaño?", "Sí", "Si no, parece que hay más en una fila."),
            ex("Un gráfico no tiene escala. ¿Se puede leer bien?", "No", "Sin escala no se sabe lo que vale cada barra."),
        ],
        "understand": [
            ex("Dos barras valen 52 y 56, y el eje parte en 50. ¿Cuánto más vale la segunda?", "4", "56 − 52 = 4.", calc="56-52"),
            ex("¿Qué problema tiene un eje que salta 0, 10, 20, 50?", "No avanza igual; hace parecer algunas barras más bajas", "La escala debe avanzar igual en todo el eje."),
            ex("Dos filas tienen 3 símbolos de ● = 10, pero un símbolo es más grande. ¿Valen distinto?", "No; las dos valen 30", "Cada símbolo vale lo mismo."),
        ],
        "apply": [
            ex("Un gráfico con eje que parte en 50 muestra A = 52 y B = 56. Pedro dice que B es mucho más grande. ¿Qué debe revisar?", "El eje y los números; la diferencia es sólo 4", "Los números muestran poca diferencia."),
            ex("Un pictograma muestra a Ana con 2 símbolos y a Beto con 3, pero los de Ana son más grandes. Con ● = 10, ¿quién tiene más?", "Beto, con 30 contra 20", "3 × 10 = 30 y 2 × 10 = 20.", calc="3*10"),
            ex("Una escala va 0, 10, 20, 50. ¿Es una escala buena?", "No", "Los saltos no son iguales."),
        ],
        "reason": [
            ex("Un gráfico muestra que las ventas de enero son 60 y las de febrero son 65, con el eje desde 55. Una barra parece el doble de la otra. ¿Por qué engaña?", "El eje no parte de 0; la diferencia es sólo 5", "65 − 60 = 5."),
            ex("María dice que el gráfico es bueno porque la barra más grande es la mayor. ¿Qué más debe revisar?", "La escala y que parta de 0", "Una barra grande puede ser engañosa."),
        ],
        "challenge": [
            ex("Un gráfico dice: A = 100 y B = 104, con el eje desde 98. La barra de B parece 3 veces más alta. ¿Cuál es la diferencia real?", "4", "104 − 100 = 4.", calc="104-100"),
            ex("Para que un gráfico sea justo, ¿qué tres cosas debes revisar?", "Que parta de 0, que la escala avance igual y que los símbolos sean iguales", "Son las tres señales de un gráfico confiable."),
        ],
    },
    context=[ex("Un aviso muestra dos barras de ventas: 40 y 42, con el eje desde 38. La segunda parece mucho más alta. ¿Qué dirías?", "Que la diferencia real es sólo 2", "42 − 40 = 2.", calc="42-40")],
    selfcheck=[
        ex("¿Un eje que parte de 50 puede hacer que dos números parecidos se vean muy distintos?", "Sí", "Se ve más grande la diferencia que es en realidad."),
        ex("¿Qué debe decir un gráfico para poder leerse bien?", "Título y escala", "Sin ellos no se entiende."),
        ex("Si un símbolo es más grande que otro, ¿vale más?", "No, si la escala dice que valen lo mismo", "Todos valen lo mismo."),
    ],
    open_task=task(
        "Mira este caso: un gráfico de barras tiene el eje que parte en 70. Muestra Tienda A = 72 y Tienda B = 78. La barra de B parece 4 veces más alta. Escribe cuál es la diferencia real, explica por qué el gráfico engaña y cómo lo corregirías.",
        "78 − 72 = 6. Engaña porque el eje parte en 70 y no en 0. Lo corregiría haciendo que el eje parta desde 0 y que la escala avance igual.",
        ["calcula la diferencia 78 − 72", "dice que el eje no parte de 0", "propone corregirlo", "usa números para explicar"],
        ["resta escrita", "explicación", "propuesta"],
        ["creer que la barra más alta indica mucha diferencia", "no mirar el eje"],
        "Pide leer los números antes de mirar las barras. Reconoce que proponga partir de 0.",
    ),
    reinforce="Busca en una revista o diario un gráfico y revisa si parte de 0 y si tiene escala.",
    extend="Dibuja el mismo gráfico de la tarea con el eje bien hecho, desde 0, y compara cómo se ve.",
)


# ================================================================ OA 26
LIBROS_DP = [2, 3, 3, 4, 2, 5, 3, 4, 3, 2, 4, 3]   # libros leídos en un mes por 12 niños
LC = Counter(LIBROS_DP)
assert len(LIBROS_DP) == 12
GRUPO_A = [8, 9, 9, 10, 10, 10, 11, 9, 10, 8]     # largo de lápices en cm
GRUPO_B = [6, 7, 7, 8, 8, 9, 7, 8, 6, 7]
AC, BC = Counter(GRUPO_A), Counter(GRUPO_B)


def dp(counter, valores, unidad="") -> str:
    """Diagrama de puntos en texto: una fila por valor del eje, con tantos puntos como veces aparece."""
    return " | ".join(f"{v}{unidad}: " + (" ".join(["●"] * counter[v]) if counter[v] else "(sin puntos)") for v in valores)


DP_LIBROS = "Diagrama de puntos de libros leídos (cada ● es un niño): " + dp(LC, range(2, 6)) + "."

register(
    OA26, 1,
    materials="Lápiz, regla y papel. Todos los datos están escritos en los ejercicios.",
    use="Aprenderé a preparar la recta numérica de un diagrama de puntos: elegir desde dónde hasta dónde va y cuánto avanza. Sirve para ubicar bien cada dato.",
    prior=["Sé ordenar números hasta 100.", "Sé contar de 1 en 1 y de 2 en 2."],
    explain=[
        "Un diagrama de puntos muestra datos numéricos sobre una recta. Sobre cada número se pone un punto por cada vez que aparece ese dato. Primero hay que preparar la recta, que se llama eje.",
        "Para preparar el eje, busca el dato menor y el dato mayor. El eje debe ir desde el menor hasta el mayor, con todos los números del medio, aunque alguno no tenga puntos. Las marcas deben estar a la misma distancia, por ejemplo de 1 en 1.",
        "Por ejemplo, si los datos son 2, 3, 3, 4, 2, 5, el menor es 2 y el mayor es 5. El eje lleva 2, 3, 4 y 5. Escribe un título que diga qué miden los números, como «libros leídos».",
    ],
    vocab=[("diagrama de puntos", "gráfico con puntos sobre una recta numérica"), ("eje", "recta con los números del diagrama"), ("dato", "cada número que se registra"), ("menor y mayor", "el dato más chico y el más grande"), ("misma distancia", "las marcas del eje están igualmente separadas")],
    worked=[
        {"title": "Elegir el eje", "problem": f"Datos de libros leídos: {lista(LIBROS_DP)}. ¿Qué números lleva el eje?", "steps": [f"El menor es {min(LIBROS_DP)} y el mayor es {max(LIBROS_DP)}.", "El eje va de 2 a 5 con todos los números del medio."], "answer": "2, 3, 4 y 5"},
        {"title": "Un número sin puntos", "problem": "Datos: 1, 3, 3, 4. ¿Lleva el eje el número 2 aunque nadie lo tenga?", "steps": ["El eje va del menor 1 al mayor 4.", "El 2 está en el medio, así que se escribe aunque no tenga puntos."], "answer": "Sí, el 2 va en el eje sin puntos"},
    ],
    mistakes=[
        {"wrong": "Dejar fuera un número del medio porque nadie lo tiene.", "why": "La recta queda con saltos distintos.", "fix": "Escribe todos los números desde el menor hasta el mayor."},
        {"wrong": "Poner las marcas del eje a distinta distancia.", "why": "Se pierde la comparación entre los datos.", "fix": "Deja la misma distancia entre cada número."},
    ],
    tiers={
        "recovery": [
            ex(f"Datos: {lista(LIBROS_DP)}. ¿Cuál es el dato menor?", str(min(LIBROS_DP)), "Es el número más chico de la lista."),
            ex(f"Datos: {lista(LIBROS_DP)}. ¿Cuál es el dato mayor?", str(max(LIBROS_DP)), "Es el número más grande de la lista."),
            ex("¿Cómo se llama la recta con los números de un diagrama de puntos?", "Eje", "Sobre el eje se ponen los puntos."),
        ],
        "understand": [
            ex("Datos: 4, 6, 5, 4. ¿Qué números lleva el eje?", "4, 5 y 6", "Va del menor 4 al mayor 6."),
            ex("Datos: 5, 7, 7, 9. ¿Hay que escribir el 8 en el eje aunque nadie lo tenga?", "Sí", "Está entre el menor 5 y el mayor 9."),
            ex("¿Cómo deben estar separadas las marcas del eje?", "A la misma distancia", "Así se comparan bien los datos."),
        ],
        "apply": [
            ex("Datos: 7, 9, 8, 7, 10. ¿Qué números lleva el eje?", "7, 8, 9 y 10", "Va del menor 7 al mayor 10."),
            ex("Datos de edades: 8, 9, 8, 10, 9, 8. ¿Cuántos números lleva el eje?", "3", "Lleva el 8, el 9 y el 10."),
            ex("Datos: 20, 25, 30, 20. Si el eje avanza de 5 en 5, ¿qué números lleva?", "20, 25 y 30", "Va de 20 a 30 de 5 en 5."),
        ],
        "reason": [
            ex("Ana hizo el eje con 2, 3 y 5 para los datos 2, 3, 3, 5, 4. ¿Qué error cometió?", "Le faltó el 4", "El eje debe llevar todos los números del 2 al 5."),
            ex("Tomás puso el 2 y el 3 muy juntos y el 4 muy lejos. ¿Qué problema tiene?", "Las marcas no están a la misma distancia", "Así el diagrama engaña."),
        ],
        "challenge": [
            ex("Datos: 12, 15, 13, 18, 14. ¿Qué números lleva el eje si avanza de 1 en 1, y cuántos son?", "12 al 18; son 7 números", "Del 12 al 18 hay 12, 13, 14, 15, 16, 17 y 18.", calc="18-12+1"),
            ex("Datos: 10, 20, 30, 20. Si el eje avanza de 10 en 10, ¿cuántos números lleva?", "3", "10, 20 y 30."),
        ],
    },
    context=[ex("Un grupo anotó cuántas mascotas tiene cada niño (0, 1 o 2). Los datos son 0, 1, 1, 2, 0, 1. ¿Qué números lleva el eje?", "0, 1 y 2", "Va del menor 0 al mayor 2.")],
    selfcheck=[
        ex("Datos: 3, 5, 4. ¿Cuál es el menor?", "3", "Es el más chico."),
        ex("Datos: 3, 5, 4. ¿Qué números lleva el eje?", "3, 4 y 5", "Va del menor al mayor."),
        ex("¿Qué se escribe en el título de un diagrama de puntos?", "Qué miden los números", "Por ejemplo, libros leídos."),
    ],
    open_task=task(
        "Usa estos datos de goles de 10 partidos: 1, 2, 2, 3, 1, 0, 2, 3, 2, 1. Escribe el dato menor y el mayor y dibuja el eje con todos los números necesarios, con un título.",
        "El menor es 0 y el mayor es 3. Eje: 0, 1, 2 y 3, con las marcas a la misma distancia. Título: goles por partido.",
        ["encuentra el menor y el mayor", "dibuja el eje con todos los números", "marcas a igual distancia", "escribe el título"],
        ["menor y mayor escritos", "eje dibujado con título"],
        ["omitir un número del medio", "marcas a distinta distancia"],
        "Pide mostrar con el dedo cada número de 0 a 3. Reconoce que el eje esté completo.",
    ),
    reinforce="Anota las edades de cinco personas de tu casa y escribe qué números lleva el eje.",
    extend="Elige datos que vayan de 10 a 20 y decide si conviene un eje de 1 en 1 o de 2 en 2.",
)

register(
    OA26, 2,
    materials="Lápiz y papel. Los datos y los diagramas están escritos con puntos en los ejercicios.",
    use="Aprenderé a registrar cada dato con un punto, también los repetidos. Sirve para que cada dato quede dibujado una sola vez.",
    prior=["Sé preparar el eje de un diagrama de puntos.", "Sé contar hasta 20."],
    explain=[
        "En un diagrama de puntos, cada dato se registra con un punto sobre su número. Si un número aparece 3 veces, tiene 3 puntos, uno encima del otro o uno al lado del otro. Un dato repetido no se pone una sola vez.",
        f"Por ejemplo, en los datos {lista(LIBROS_DP)}, el número 3 aparece {LC[3]} veces. Entonces sobre el 3 hay {LC[3]} puntos. El 5 aparece {LC[5]} vez y tiene {LC[5]} punto.",
        "Cuando termines, cuenta todos los puntos. Deben ser tantos como datos hay. Si hay 12 datos, el diagrama debe tener 12 puntos. Si no coincide, se perdió o se repitió algún dato.",
    ],
    vocab=[("punto", "marca que representa un dato"), ("dato repetido", "número que aparece más de una vez"), ("apilar", "poner los puntos uno encima del otro"), ("contar los puntos", "comprobar que son tantos como datos"), ("registro", "anotar cada dato en el diagrama")],
    worked=[
        {"title": "Registrar datos repetidos", "problem": f"Datos de libros leídos por 12 niños: {lista(LIBROS_DP)}. ¿Cuántos puntos van sobre el 2?", "steps": ["Cuento las veces que aparece el 2 en la lista.", f"Aparece {LC[2]} veces."], "answer": f"{LC[2]} puntos"},
        {"title": "Comprobar el total", "problem": f"Un diagrama tiene {LC[2]}, {LC[3]}, {LC[4]} y {LC[5]} puntos en los números 2, 3, 4 y 5. ¿Coincide con los 12 datos?", "steps": ["Escribo la suma de los puntos de los cuatro números.", f"{LC[2]} + {LC[3]} + {LC[4]} + {LC[5]} = {sum(LC.values())}."], "answer": "Sí, son 12 puntos"},
    ],
    mistakes=[
        {"wrong": "Poner un solo punto sobre un número que se repite.", "why": "Se pierde la información de cuántas veces aparece.", "fix": "Pon un punto por cada vez que aparece el dato."},
        {"wrong": "Poner puntos de distinto tamaño o muy separados.", "why": "Es difícil contarlos.", "fix": "Haz los puntos iguales y ordenados."},
    ],
    tiers={
        "recovery": [
            ex(f"Datos: {lista(LIBROS_DP)}. ¿Cuántas veces aparece el 4?", str(LC[4]), "Se cuentan las veces que aparece."),
            ex(f"Datos: {lista(LIBROS_DP)}. ¿Cuántas veces aparece el 5?", str(LC[5]), "Se cuentan las veces que aparece."),
            ex("Un número aparece 3 veces. ¿Cuántos puntos lleva?", "3", "Un punto por cada vez."),
        ],
        "understand": [
            ex(f"Datos: {lista(LIBROS_DP)}. ¿Cuántos puntos van sobre el 3?", str(LC[3]), "El 3 aparece esas veces."),
            ex("¿Se pone un solo punto sobre un dato repetido?", "No; un punto por cada vez", "Cada dato se registra."),
            ex(f"Hay {len(LIBROS_DP)} datos. ¿Cuántos puntos debe tener el diagrama?", str(len(LIBROS_DP)), "Un punto por dato."),
        ],
        "apply": [
            ex("Datos: 7, 9, 8, 7, 10, 7. ¿Cuántos puntos van sobre el 7?", "3", "El 7 aparece tres veces."),
            ex("Datos: 7, 9, 8, 7, 10, 7. ¿Cuántos puntos tiene el diagrama en total?", "6", "Hay 6 datos."),
            ex("Datos: 1, 1, 2, 3, 3, 3, 3. ¿Cuántos puntos van sobre el 3?", "4", "El 3 aparece cuatro veces."),
        ],
        "reason": [
            ex("Ana puso un solo punto sobre el 3 aunque el 3 aparece 5 veces. ¿Qué error cometió?", "Registró el dato una sola vez; son 5 puntos", "Un punto por cada vez que aparece."),
            ex("Un diagrama de 12 datos tiene 11 puntos. ¿Qué debe hacer?", "Revisar la lista porque falta un punto", "Los puntos deben ser tantos como datos."),
        ],
        "challenge": [
            ex("Datos: 4, 5, 5, 6, 4, 5, 6, 5. ¿Cuántos puntos va a tener cada número, en orden 4, 5 y 6?", "2, 4 y 2", "El 4 aparece 2 veces, el 5 aparece 4 y el 6 aparece 2."),
            arith("Un diagrama tiene 4 puntos en el 1, 6 puntos en el 2 y 3 puntos en el 3. ¿Cuántos datos hay?", "4+6+3", "Se suman todos los puntos."),
        ],
    },
    context=[ex("Un curso anotó cuántos años tienen sus 6 alumnos: 8, 9, 8, 8, 9, 10. ¿Cuántos puntos van sobre el 8?", "3", "El 8 aparece tres veces.")],
    selfcheck=[
        ex("Un dato aparece 2 veces. ¿Cuántos puntos tiene?", "2", "Un punto por vez."),
        ex("Si hay 8 datos, ¿cuántos puntos hay en el diagrama?", "8", "Un punto por dato."),
        ex("¿Qué se hace al terminar de poner los puntos?", "Contarlos y compararlos con los datos", "Así se comprueba el registro."),
    ],
    open_task=task(
        f"Usa los datos de libros leídos por 12 niños: {lista(LIBROS_DP)}. Dibuja el eje de 2 a 5 y pon un punto por cada dato. Cuenta los puntos de cada número y comprueba que el total es 12.",
        f"Sobre el 2 hay {LC[2]} puntos, sobre el 3 hay {LC[3]}, sobre el 4 hay {LC[4]} y sobre el 5 hay {LC[5]}. Total: {LC[2]} + {LC[3]} + {LC[4]} + {LC[5]} = 12.",
        ["dibuja el eje de 2 a 5", "un punto por cada dato", "puntos ordenados y del mismo tamaño", "comprueba el total"],
        ["diagrama dibujado", "cuenta de los puntos", "suma de comprobación"],
        ["un solo punto para un dato repetido", "no comprobar el total"],
        "Pide tachar cada dato de la lista al dibujar su punto. Reconoce que el total coincida.",
    ),
    reinforce="Anota cuántos años tienen ocho personas conocidas y haz un diagrama de puntos.",
    extend="Haz un diagrama de puntos con 15 datos entre 1 y 6 y compruébalo contando los puntos.",
)

register(
    OA26, 3,
    materials="Lápiz y papel. Los diagramas de puntos están escritos en los ejercicios con símbolos ●.",
    use="Aprenderé a leer un diagrama de puntos: la frecuencia de cada valor, el dato que más se repite y los valores menor y mayor. Sirve para contar una historia con los datos.",
    prior=["Sé registrar datos con puntos.", "Sé sumar números hasta 100."],
    explain=[
        "En un diagrama de puntos, la frecuencia de un número es la cantidad de puntos que tiene encima. Para leerla, cuenta los puntos sobre ese número. El valor con más puntos es el que más se repite: es el valor más frecuente.",
        "El valor menor es el primer número del eje que tiene puntos, y el valor mayor es el último que tiene puntos. A los dos se les llama valores extremos. La distancia entre ellos es qué tan separados están los datos.",
        "También puedes sumar todos los puntos para saber cuántos datos hay, o sumar los puntos de algunos números, por ejemplo cuántos niños leyeron 4 libros o más.",
    ],
    vocab=[("frecuencia", "cantidad de puntos sobre un número"), ("valor más frecuente", "valor con más puntos"), ("valor menor", "primer número del eje con puntos"), ("valor mayor", "último número del eje con puntos"), ("valores extremos", "el menor y el mayor")],
    worked=[
        {"title": "Leer el valor más frecuente", "problem": DP_LIBROS + " ¿Cuál es el valor con más puntos?", "steps": [f"Cuento los puntos: 2 → {LC[2]}, 3 → {LC[3]}, 4 → {LC[4]}, 5 → {LC[5]}.", f"La mayor frecuencia es {LC[3]}, en el 3."], "answer": "El 3 (es el valor más frecuente)"},
        {"title": "Sumar frecuencias", "problem": DP_LIBROS + " ¿Cuántos niños leyeron 4 libros o más?", "steps": [f"Los que leyeron 4: {LC[4]}.", f"Los que leyeron 5: {LC[5]}.", f"{LC[4]} + {LC[5]} = {LC[4] + LC[5]}."], "answer": f"{LC[4] + LC[5]} niños"},
    ],
    mistakes=[
        {"wrong": "Decir que el valor más alto del eje es el que más se repite.", "why": "Se confunde el número con la cantidad de puntos.", "fix": "Cuenta los puntos de cada número y compara."},
        {"wrong": "Decir que el valor mayor es 5 si el 5 no tiene puntos.", "why": "Se mira el eje y no los puntos.", "fix": "El valor mayor es el último número que sí tiene puntos."},
    ],
    tiers={
        "recovery": [
            ex(DP_LIBROS + " ¿Cuántos puntos tiene el 4?", str(LC[4]), "Se cuentan los ● sobre el 4."),
            ex(DP_LIBROS + " ¿Cuántos puntos tiene el 5?", str(LC[5]), "Se cuentan los ● sobre el 5."),
            ex("¿Qué indican los puntos sobre un número?", "Cuántas veces aparece ese dato", "Un punto por cada vez."),
        ],
        "understand": [
            ex(DP_LIBROS + " ¿Cuál es el valor con más puntos?", "El 3", f"Tiene {LC[3]} puntos, la mayor frecuencia."),
            ex(DP_LIBROS + " ¿Cuál es el valor menor con puntos?", "El 2", "Es el primer número del eje con puntos."),
            ex(DP_LIBROS + " ¿Cuál es el valor mayor con puntos?", "El 5", "Es el último número del eje con puntos."),
        ],
        "apply": [
            arith(DP_LIBROS + " ¿Cuántos niños leyeron 4 libros o más?", f"{LC[4]}+{LC[5]}", "Se suman los puntos del 4 y del 5."),
            arith(DP_LIBROS + " ¿Cuántos niños leyeron 2 o 3 libros?", f"{LC[2]}+{LC[3]}", "Se suman los puntos del 2 y del 3."),
            arith(DP_LIBROS + " ¿Cuántos niños hay en total?", f"{LC[2]}+{LC[3]}+{LC[4]}+{LC[5]}", "Se suman todos los puntos."),
        ],
        "reason": [
            ex(DP_LIBROS + " Rosa dice que el 5 es el valor más frecuente porque es el número más alto. ¿Qué error comete?", "El valor más frecuente es el que tiene más puntos, no el más alto", f"El 3 tiene {LC[3]} puntos y el 5 sólo {LC[5]}."),
            ex(DP_LIBROS + " Luis dice que 6 libros es el valor mayor porque el eje podría seguir. ¿Es correcto?", "No; el valor mayor es el 5, que es el último con puntos", "Se mira dónde hay puntos."),
        ],
        "challenge": [
            arith(DP_LIBROS + " ¿Cuántos puntos más tiene el valor más frecuente que el valor mayor?", f"{LC[3]}-{LC[5]}", "Se resta la frecuencia menor a la mayor."),
            ex("Diagrama de puntos de edades: 7 → ●, 8 → ● ● ●, 9 → ● ●, 10 → ●. ¿Cuál es el valor más frecuente y cuántos datos hay en total?", "El valor más frecuente es 8; hay 7 datos", "El 8 tiene 3 puntos y 1 + 3 + 2 + 1 = 7.", calc="1+3+2+1"),
        ],
    },
    context=[ex("Un diagrama de puntos de las mascotas que tienen 6 niños muestra: 0 → ●, 1 → ● ● ●, 2 → ● ●. ¿Cuántos niños tienen 1 mascota?", "3", "Se cuentan los puntos sobre el 1.")],
    selfcheck=[
        ex("El valor más frecuente es el que tiene ¿cuántos puntos?", "Más puntos que los demás", "Es el que más se repite."),
        ex("En 3 → ● ● ●, 4 → ●, ¿cuál es el valor más frecuente?", "El 3", "Tiene más puntos."),
        ex("¿Qué son los valores extremos?", "El menor y el mayor", "Son el primero y el último con puntos."),
    ],
    open_task=task(
        "Usa este diagrama de puntos de libros leídos por 12 niños: " + dp(LC, range(2, 6)) + ". Escribe el valor más frecuente, el valor menor, el valor mayor y cuántos niños leyeron 3 libros o menos.",
        f"Valor más frecuente: 3 (con {LC[3]} puntos). Menor: 2. Mayor: 5. Leyeron 3 libros o menos: {LC[2]} + {LC[3]} = {LC[2] + LC[3]} niños.",
        ["cuenta los puntos de cada número", "identifica el valor más frecuente", "dice los valores menor y mayor", "suma los puntos pedidos"],
        ["cuatro respuestas escritas", "suma"],
        ["confundir el valor más frecuente con el número más alto", "contar mal los puntos"],
        "Pide señalar los puntos al contar. Reconoce las cuatro respuestas.",
    ),
    reinforce="Haz un diagrama de puntos con las edades de siete personas y di cuál es el valor más frecuente.",
    extend="Inventa un diagrama de puntos donde el valor más frecuente sea el valor menor.",
)

register(
    OA26, 4,
    materials="Lápiz y papel. Los dos diagramas de puntos están escritos con símbolos ● en cada ejercicio.",
    use="Aprenderé a comparar dos diagramas de puntos y decir en qué se parecen y se diferencian. Sirve para comparar dos grupos de datos.",
    prior=["Sé leer frecuencias y el valor más frecuente de un diagrama.", "Sé restar números hasta 100."],
    explain=[
        "Dos diagramas de puntos se pueden comparar. Fíjate en el valor menor y el mayor de cada uno, en el valor más frecuente y en qué lado del eje hay más puntos. Si dos diagramas tienen el mismo eje y uno tiene los puntos más a la derecha, sus datos son mayores.",
        "Para que la comparación sea justa, los dos grupos deben tener la misma cantidad de datos. Además, lee los números de cada eje, porque dos ejes pueden empezar en números distintos. Si los grupos no tienen los mismos datos, compara con cuidado y di cuántos datos tiene cada uno.",
        "Una buena conclusión usa números: «El valor más frecuente de A es 10 y el de B es 7, así que lo más común en A son lápices más largos». Evita decir cosas que el diagrama no muestra.",
    ],
    vocab=[("comparar", "decir en qué se parecen y en qué se diferencian"), ("valor más frecuente", "valor con más puntos"), ("más a la derecha", "con valores mayores en el eje"), ("distribución", "cómo se reparten los datos en el eje"), ("conclusión", "lo que se puede afirmar al ver los datos")],
    worked=[
        {"title": "Comparar los valores más frecuentes", "problem": "Largo de lápices en cm. Grupo A: " + dp(AC, range(8, 12)) + ". Grupo B: " + dp(BC, range(6, 10)) + ". ¿Qué grupo tiene el valor más frecuente mayor?", "steps": [f"Valor más frecuente de A: el {max(AC, key=AC.get)}, con {max(AC.values())} puntos.", f"Valor más frecuente de B: el {max(BC, key=BC.get)}, con {max(BC.values())} puntos."], "answer": f"El grupo A ({max(AC, key=AC.get)} contra {max(BC, key=BC.get)})"},
        {"title": "Comparar los extremos", "problem": "Con los mismos grupos, ¿cuál es el lápiz más corto de cada grupo?", "steps": [f"En A, el menor es {min(GRUPO_A)} cm.", f"En B, el menor es {min(GRUPO_B)} cm."], "answer": f"A: {min(GRUPO_A)} cm y B: {min(GRUPO_B)} cm"},
    ],
    mistakes=[
        {"wrong": "Decir que un grupo tiene más lápices largos sólo porque tiene más puntos.", "why": "Se compara la cantidad de puntos y no su posición.", "fix": "Mira dónde están los puntos en el eje: más a la derecha son valores mayores."},
        {"wrong": "Comparar sin mirar que los ejes son distintos.", "why": "Los números no son comparables sin revisar cada eje.", "fix": "Lee los números de cada eje antes de comparar."},
    ],
    tiers={
        "recovery": [
            ex(f"Lápices de A (cm): {lista(GRUPO_A)}. ¿Cuántos lápices hay?", str(len(GRUPO_A)), "Se cuentan todos los datos."),
            ex(f"Lápices de B (cm): {lista(GRUPO_B)}. ¿Cuántos lápices hay?", str(len(GRUPO_B)), "Se cuentan todos los datos."),
            ex(f"Lápices de A (cm): {lista(GRUPO_A)}. ¿Cuál es el largo menor?", str(min(GRUPO_A)), "Es el número más chico de la lista."),
        ],
        "understand": [
            ex("Grupo A: " + dp(AC, range(8, 12)) + ". ¿Cuál es el valor más frecuente de A?", str(max(AC, key=AC.get)), f"Tiene {max(AC.values())} puntos."),
            ex("Grupo B: " + dp(BC, range(6, 10)) + ". ¿Cuál es el valor más frecuente de B?", str(max(BC, key=BC.get)), f"Tiene {max(BC.values())} puntos."),
            ex("Un diagrama tiene los puntos más a la derecha del eje. ¿Sus datos son mayores o menores?", "Mayores", "A la derecha están los números mayores."),
        ],
        "apply": [
            ex(f"Largos de A (cm): {lista(GRUPO_A)}. ¿Cuál es el largo mayor de A?", str(max(GRUPO_A)), "Es el número más grande de la lista."),
            ex(f"Largos de B (cm): {lista(GRUPO_B)}. ¿Cuál es el largo mayor de B?", str(max(GRUPO_B)), "Es el número más grande de la lista."),
            arith(f"Valor más frecuente de A: {max(AC, key=AC.get)} cm. De B: {max(BC, key=BC.get)} cm. ¿Cuántos cm más largo es el de A?", f"{max(AC, key=AC.get)}-{max(BC, key=BC.get)}", "Se resta el valor menor al mayor."),
        ],
        "reason": [
            ex("Pedro dice que A tiene lápices más largos porque tiene más puntos. Los dos grupos tienen 10 datos. ¿Qué error comete?", "Los dos tienen 10 puntos; hay que mirar dónde están", "Los lápices más largos están más a la derecha."),
            ex("Ana dice: «lo más común en B es más largo porque su valor más frecuente es 7». El de A es 10. ¿Está bien?", "No; A tiene el valor más frecuente mayor", "10 es mayor que 7."),
        ],
        "challenge": [
            ex(f"A: {lista(GRUPO_A)}. B: {lista(GRUPO_B)}. ¿El lápiz más largo de B es más corto que el más corto de A?", "No; el más largo de B (9) es más largo que el más corto de A (8)", f"{max(GRUPO_B)} es mayor que {min(GRUPO_A)}."),
            arith(f"A: {lista(GRUPO_A)}. B: {lista(GRUPO_B)}. ¿Cuántos cm separan el lápiz más corto de A del más corto de B?", f"{min(GRUPO_A)}-{min(GRUPO_B)}", "Se resta el menor de B al menor de A."),
        ],
    },
    context=[ex("Dos cursos anotaron cuántos libros leyeron. En el curso A lo más común es haber leído 5 libros y en el curso B lo más común es haber leído 3. ¿En qué curso lo más común es leer más libros?", "En el curso A", "5 es mayor que 3.")],
    selfcheck=[
        ex("¿Para comparar dos diagramas qué conviene mirar primero?", "El eje, el menor, el mayor y el valor más frecuente", "Son los datos más fáciles de comparar."),
        ex("En A el valor más frecuente es 10 y en B es 7. ¿En cuál lo más común es mayor?", "En A", "10 es mayor que 7."),
        ex("¿Un diagrama con más puntos tiene siempre datos mayores?", "No", "Importa la posición, no la cantidad de puntos."),
    ],
    open_task=task(
        "Compara estos dos grupos de largos de lápices en cm. A: " + lista(GRUPO_A) + ". B: " + lista(GRUPO_B) + ". Escribe el valor más frecuente, el menor y el mayor de cada grupo y una conclusión usando números.",
        f"A: más frecuente {max(AC, key=AC.get)}, menor {min(GRUPO_A)}, mayor {max(GRUPO_A)}. B: más frecuente {max(BC, key=BC.get)}, menor {min(GRUPO_B)}, mayor {max(GRUPO_B)}. Lo más común en A son lápices más largos: su valor más frecuente es {max(AC, key=AC.get) - max(BC, key=BC.get)} cm mayor.",
        ["encuentra valor más frecuente, menor y mayor de cada grupo", "compara con números", "escribe una conclusión justificada", "no usa sólo la cantidad de puntos"],
        ["seis valores escritos", "conclusión"],
        ["confundir cantidad de puntos con tamaño", "concluir sin números"],
        "Pide justificar con un número del diagrama. Reconoce que mire la posición de los puntos.",
    ),
    reinforce="Compara las edades de dos grupos de cinco personas de tu familia usando un diagrama de puntos para cada grupo.",
    extend="Inventa un grupo C cuyo valor más frecuente sea mayor que el de A y el de B, y escribe sus datos.",
)
