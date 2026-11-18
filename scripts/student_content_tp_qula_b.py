"""Química Industrial, mención Laboratorio Químico (4.º medio TP): OAM-03 (preparar muestras para ensayos) y OAM-04 (medir, registrar y verificar estados y cambios). Todo en papel, con datos de ejemplo; los cálculos de concentración y dilución son solo de planilla y no enseñan a preparar nada."""
from __future__ import annotations

from tp_qula_common import AVISO, EMER, build, em

O3 = "TP-QULA-4-OAM-03"
O4 = "TP-QULA-4-OAM-04"

# ============================================================ OAM-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Orden de trabajo OT-52 del «Laboratorio Demo Valle Claro»: preparar 6 muestras de un material de ejemplo para un ensayo de humedad de ejemplo, según el método aprobado por la empresa. Tiempo estimado de preparación: 15 minutos por muestra. "
     "Etapas generales del método (solo nombradas, sin instrucciones): homogeneizar, pesar y secar. Peligros anotados: polvo, superficie caliente de un equipo y vidrio roto. Matriz de ejemplo: puntaje de riesgo = probabilidad × gravedad. Polvo: probabilidad 4 y gravedad 2. Superficie caliente: probabilidad 3 y gravedad 4. Vidrio roto: probabilidad 2 y gravedad 3.")
build(
    O3, 1, F,
    use="Aprenderé por qué se preparan las muestras antes de un ensayo, qué es un método de ensayo y una orden de trabajo, y por qué solo personal formado prepara muestras: este cuaderno no enseña a prepararlas.",
    prior=["Sé qué es una muestra representativa.", "Sé qué es una orden de trabajo.", "Sé calcular el puntaje de riesgo."],
    explain=[
        "En el laboratorio químico, preparar una muestra es dejarla en la condición que exige el método de ensayo, sin alterar lo que se quiere medir. Un método de ensayo es el documento aprobado por la empresa que dice qué ensayo se hace y con qué condiciones; la orden de trabajo indica qué muestras se trabajan, cuándo y quién. La preparación puede incluir etapas generales como homogeneizar, que es dejar la muestra uniforme, pesar y secar. Aquí solo se nombran; no se enseñan.",
        "Una mala preparación cambia el resultado del ensayo aunque el instrumento sea perfecto: por eso se sigue el método sin improvisar y se registra todo. La hoja de datos de seguridad del fabricante informa los peligros del material y se lee antes de trabajar. El puntaje de riesgo de la matriz de ejemplo se calcula como probabilidad por gravedad.",
        f"Preparar muestras exige formación, autorización y elementos de protección. En este cuaderno solo se trabaja con documentos y cálculos en papel. {EMER} {AVISO}",
    ],
    vocab=[("preparar una muestra", "dejarla en la condición que exige el método de ensayo"), ("método de ensayo", "documento aprobado que fija qué ensayo se hace y con qué condiciones"), ("orden de trabajo", "documento que indica qué se trabaja, cuándo y quién lo hace"), ("homogeneizar", "dejar la muestra uniforme"), ("puntaje de riesgo", "probabilidad multiplicada por gravedad, según la matriz")],
    worked=[
        ("Tiempo total", "Una orden de ejemplo pide preparar 8 muestras y cada una toma 10 minutos. ¿Cuántos minutos toma en total?", ["Se multiplica el número de muestras por el tiempo de cada una.", "8 por 10 son 80."], "80 minutos"),
        ("Puntaje de riesgo", "Un peligro de ejemplo, un cable suelto, tiene probabilidad 2 y gravedad 5. ¿Qué puntaje tiene?", ["Se multiplica la probabilidad por la gravedad.", "2 por 5 son 10."], "10 puntos"),
    ],
    mistakes=[("Creer que leer el método de ensayo ya permite preparar las muestras.", "Preparar muestras exige formación, autorización y elementos de protección.", "Usa el método para entender el trabajo y pide autorización para hacerlo."),
              ("Saltarse una etapa de la preparación «porque se ve igual».", "Una etapa omitida puede cambiar el resultado del ensayo.", "El método no se modifica por cuenta propia: se consulta al jefe de laboratorio.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué significa preparar una muestra?", "Dejarla en la condición que exige el método de ensayo", "Botar la parte que sobra sin registrar", "Cambiarle el rótulo para el análisis", "La preparación adapta la muestra al método sin alterar lo que se mide."),
        ("abc", "En el laboratorio químico: ¿qué es un método de ensayo?", "Un documento aprobado que fija qué ensayo se hace y con qué condiciones", "El nombre del analista", "El precio del ensayo", "El método es el documento que guía el trabajo."),
        ("abc", "En el laboratorio químico: ¿qué es homogeneizar una muestra?", "Dejarla uniforme", "Dividirla en dos partes distintas", "Cambiar su rótulo", "Una muestra homogénea es igual en todas sus partes."),
        ("=", "{F} ¿Cuántos minutos toma preparar las 6 muestras de la orden?", "6*15", "Se multiplica el número de muestras por el tiempo de cada una.", " minutos"),
        ("=", "{F} ¿Cuántas órdenes completas como la OT-52 caben en una jornada de 480 minutos?", "480//90", "Se divide la jornada entre los 90 minutos que toma una orden y se cuentan solo las completas.", " órdenes"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la superficie caliente?", "3*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} Según la matriz, ¿qué peligro tiene el mayor puntaje?", "La superficie caliente, con 12 puntos", "El polvo, con 8 puntos", "El vidrio roto, con 6 puntos", "Se compara probabilidad por gravedad de cada peligro."),
        ("abc", "{F} ¿Por qué se lee la hoja de datos de seguridad antes de trabajar con el material?", "Porque informa los peligros y las precauciones generales del fabricante", "Porque indica cuánto cuesta el material", "Porque reemplaza al método de ensayo", "La hoja se lee para conocer los peligros; no es un método."),
        ("abc", "{F} Una analista propone saltarse la etapa de secar «para terminar antes». ¿Qué corresponde?", "No hacerlo: el método no se modifica por cuenta propia; se consulta al jefe de laboratorio", "Hacerlo si la muestra se ve seca", "Hacerlo si el resultado se necesita hoy", "Una etapa omitida puede cambiar el resultado."),
        ("abc", "{F} ¿Por qué una mala preparación cambia el resultado aunque la balanza sea exacta?", "Porque la muestra deja de reflejar lo que se quería medir", "Porque la balanza deja de funcionar", "Porque el método cambia solo", "El instrumento mide la muestra tal como llega."),
        ("abc", "Una estudiante de práctica de ejemplo propone preparar ella sola las 6 muestras «porque ya leyó el método». ¿Qué corresponde?", "No hacerlo: solo personal formado y autorizado prepara muestras", "Hacerlo con guantes", "Hacerlo si el jefe no está", "Leer el método no autoriza a preparar muestras."),
        ("=", "{F} Si se agregan 2 muestras más a la orden, ¿cuántos minutos tomaría prepararlas todas?", "(6+2)*15", "Se suman las muestras y se multiplica por el tiempo de cada una.", " minutos"),
        em("Lees la orden de trabajo de ejemplo en la oficina cuando alguien avisa que el equipo de secado de la sala echa humo y que se siente un olor a quemado.", 0),
    ],
    ctx=("abc", "Una jefatura de ejemplo te dice: «Prepara tú las 6 muestras mientras salgo, el método es fácil». No hay autorización. ¿Qué respondes?", "Que no, porque preparar muestras exige formación, autorización y norma vigente, y que consultarás a un adulto responsable", "Que sí, si sigues el método", "Que sí, si usas delantal", "Un método escrito no sustituye la formación ni la autorización."),
    sc=[
        ("En el laboratorio químico: ¿qué es una orden de trabajo?", "Un documento que indica qué se trabaja, cuándo y quién lo hace", "Organiza las tareas del laboratorio y quién las hace."),
        ("En el laboratorio químico: ¿se modifica el método de ensayo por cuenta propia?", "No, se consulta al jefe de laboratorio", "Un cambio no autorizado puede alterar el resultado."),
        ("¿Quién prepara las muestras de un ensayo?", "Personal formado y autorizado", "Leer un método no habilita para prepararlas."),
    ],
    op=("Orden ficticia del «Laboratorio Demo Costa Norte»: preparar 4 muestras, 20 minutos cada una, peligros: polvo (probabilidad 4, gravedad 3) y superficie caliente (probabilidad 2, gravedad 4). Escribe (a) cuántos minutos toma preparar las 4 muestras, (b) los puntajes de riesgo y cuál se atiende primero, (c) por qué no se salta una etapa del método, (d) por qué leer esta orden no te habilita para preparar muestras.",
        "(a) 4 por 20 son 80 minutos. (b) Polvo: 12 puntos; superficie caliente: 8 puntos; se atiende primero el polvo. (c) Porque puede cambiar el resultado del ensayo. (d) Porque preparar muestras exige formación, autorización y norma vigente.",
        ["calcula el tiempo", "calcula y prioriza los puntajes", "justifica seguir el método", "aclara que leer no habilita"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "no priorizar por puntaje", "creer que el método autoriza"],
        "Pregunta: «¿qué puede pasar si se omite una etapa?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa una orden de trabajo con cinco muestras y calcula el tiempo total y un puntaje de riesgo.",
    extend="Explica con un ejemplo por qué un método de ensayo no se modifica sin autorización.",
)

# ============================================================ OAM-03, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Hoja de preparación de la muestra H-07 del «Laboratorio Demo Valle Claro». Masa del envase vacío (tara): 12 g. Masa del envase con la muestra (masa bruta): 52 g. "
     "Para un ensayo de ejemplo se usa una alícuota de 10 mL de una solución de 200 g/L, y el volumen final del ensayo es de 100 mL. Blanco: un ensayo sin muestra que se hace con las mismas condiciones, para detectar contaminación. Réplicas pedidas por el método: 3. Responsable: analista. "
     "Los cálculos de esta clase son solo de planilla: cómo se prepara lo define el método y lo hace personal formado.")
build(
    O3, 2, F,
    use="Aprenderé los conceptos y documentos de la preparación de muestras: tara, masa bruta y neta, alícuota, factor de dilución, blanco y réplicas, y a hacer los cálculos de planilla con números enteros.",
    prior=["Sé qué es un método de ensayo.", "Sé restar y dividir números enteros.", "Sé qué es una unidad de masa y de volumen."],
    explain=[
        "En el laboratorio químico, la tara es la masa del envase vacío y la masa bruta es la masa del envase con la muestra; la masa neta es la masa de la muestra sola y se calcula restando: masa neta igual a masa bruta menos tara. Una alícuota es una porción medida de una muestra o de una solución. El factor de dilución compara el volumen final con el de la alícuota: factor igual a volumen final dividido por volumen de la alícuota.",
        "Un blanco es un ensayo sin muestra, con las mismas condiciones, que sirve para detectar contaminación en los materiales o en el método. Las réplicas son repeticiones del ensayo para comprobar que el resultado se repite. La hoja de preparación registra tara, masa bruta, alícuota, blanco y réplicas, con fecha, responsable y firma. Los valores son números de ejemplo.",
        f"Estos cálculos no indican cómo preparar: eso lo fija el método y lo hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("tara", "masa del envase vacío"), ("masa bruta", "masa del envase con la muestra"), ("masa neta", "masa de la muestra sola: masa bruta menos tara"), ("alícuota", "porción medida de una muestra o solución"), ("factor de dilución", "volumen final dividido por el volumen de la alícuota"), ("blanco", "ensayo sin muestra para detectar contaminación"), ("réplica", "repetición del ensayo para comprobar el resultado")],
    worked=[
        ("Masa neta", "Un envase de ejemplo con tara de 15 g y masa bruta de 65 g. ¿Cuál es la masa neta?", ["Se resta la tara a la masa bruta.", "65 menos 15 son 50."], "50 g"),
        ("Factor de dilución", "Una alícuota de ejemplo de 5 mL se lleva a un volumen final de 50 mL. ¿Cuál es el factor de dilución?", ["Se divide el volumen final entre el de la alícuota.", "50 entre 5 son 10."], "10"),
    ],
    mistakes=[("Anotar la masa bruta como si fuera la masa de la muestra.", "La masa bruta incluye el envase; la de la muestra es la neta.", "Resta siempre la tara para obtener la masa neta."),
              ("Omitir el blanco porque «no tiene muestra».", "El blanco detecta contaminación y sin él el resultado puede estar falseado.", "Registra el blanco que pide el método.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es la tara?", "La masa del envase vacío", "La masa de la muestra sola", "La masa del envase con la muestra", "La tara es el envase sin contenido."),
        ("abc", "En el laboratorio químico: ¿qué es una alícuota?", "Una porción medida de una muestra o de una solución", "Un envase vacío", "El resultado de un ensayo", "La alícuota es una porción con medida conocida."),
        ("abc", "En el laboratorio químico: ¿para qué sirve un blanco?", "Para detectar contaminación en los materiales o en el método", "Para aumentar la masa de la muestra", "Para reemplazar las réplicas", "El blanco ayuda a descubrir contaminación."),
        ("=", "{F} ¿Cuál es la masa neta de la muestra H-07?", "52-12", "Se resta la tara a la masa bruta.", " g"),
        ("=", "{F} ¿Cuál es el factor de dilución del ensayo?", "100//10", "Se divide el volumen final entre el volumen de la alícuota.", ""),
        ("abc", "{F} ¿Qué es la masa de 52 g de la hoja?", "La masa bruta", "La masa neta", "La tara", "Es la masa del envase con la muestra."),
        ("=", "{F} Si el método pide 3 réplicas de la masa neta, ¿cuántos gramos de muestra se necesitan en total?", "(52-12)*3", "Se calcula la masa neta y se multiplica por las réplicas.", " g"),
        ("abc", "{F} Un analista anota 52 g como «masa de la muestra». ¿Qué corresponde?", "Corregir: la masa de la muestra es la neta, de 40 g", "Dejarlo porque es lo que marca la balanza", "Dejarlo si el envase es liviano", "La balanza marcó la masa bruta; la neta se calcula."),
        ("abc", "{F} ¿Por qué el método incluye un blanco?", "Porque permite detectar contaminación que falsearía el resultado", "Porque reemplaza la muestra cuando falta", "Porque reduce el número de réplicas", "Sin blanco no se sabe si el resultado viene de la muestra."),
        ("=", "{F} Si el método pide 3 réplicas y cada una usa una alícuota de 10 mL de la solución de 200 g/L de la ficha, ¿cuántos mL de solución suman las tres alícuotas?", "3*10", "Se multiplica el número de réplicas por la alícuota de cada una.", " mL"),
        ("abc", "{F} Una persona propone preparar la hoja de la muestra H-08 copiando los valores de la H-07 «porque son parecidos». ¿Qué corresponde?", "Rechazarlo: cada muestra se registra con sus propios valores medidos", "Aceptarlo si la fecha es la misma", "Aceptarlo si la masa neta es cercana", "Un registro copiado no refleja lo realmente medido."),
        ("=", "{F} Otra hoja de ejemplo tiene tara de 13 g y masa bruta de 53 g. ¿Cuál es la masa neta?", "53-13", "Se resta la tara a la masa bruta.", " g"),
        em("Revisas una hoja de preparación de ejemplo en la oficina cuando alguien avisa que en la sala se cayó un frasco y que hay un olor fuerte y vapores.", 1),
    ],
    ctx=("abc", "Una técnica de ejemplo te dice: «Anota la masa neta de 40 g aunque no la pesamos, es lo que siempre da». ¿Qué respondes?", "Que no: se anota solo lo realmente medido, y la masa neta se calcula con la tara y la masa bruta reales", "Que sí, si siempre da lo mismo", "Que sí, si se anota con lápiz", "Un registro con datos supuestos deja de ser confiable."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula la masa neta?", "Masa bruta menos tara", "Así se obtiene la masa de la muestra sola."),
        ("En el laboratorio químico: ¿qué es una réplica?", "Una repetición del ensayo para comprobar el resultado", "Si el resultado se repite, es más confiable."),
        ("En el laboratorio químico: ¿cómo se calcula el factor de dilución?", "Volumen final dividido por el volumen de la alícuota", "Indica cuántas veces más diluida queda la solución."),
    ],
    op=("Hoja ficticia del «Laboratorio Demo Costa Norte»: tara 14 g, masa bruta 54 g; alícuota de 5 mL llevada a un volumen final de 100 mL; se piden 2 réplicas y un blanco. Escribe (a) la masa neta, (b) el factor de dilución, (c) para qué sirve el blanco, (d) por qué no se copian valores de otra hoja.",
        "(a) 54 menos 14 son 40 g. (b) 100 entre 5 son 20. (c) Para detectar contaminación en los materiales o en el método. (d) Porque cada hoja debe registrar lo realmente medido en esa muestra.",
        ["calcula la masa neta", "calcula el factor", "explica el blanco", "justifica no copiar valores"],
        ["hoja con las cuatro respuestas"],
        ["usar la masa bruta", "dividir al revés", "copiar valores"],
        "Pregunta: «¿qué mide la balanza y qué se calcula después?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una hoja de preparación con tara, masa bruta, alícuota y volumen final, y calcula la masa neta y el factor de dilución.",
    extend="Explica con un ejemplo por qué el blanco ayuda a confiar en un resultado.",
)

# ============================================================ OAM-03, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Hoja de preparación de 5 muestras del «Laboratorio Demo Valle Claro». Requisito de ejemplo: masa neta de 40 g con tolerancia de ±2 g (se aceptan de 38 a 42 g). "
     "M1: tara 12 g, masa bruta 52 g. M2: tara 12 g, masa bruta 50 g. M3: tara 13 g, masa bruta 53 g. M4: tara 12 g, masa bruta anotada 62 g (el analista dice que midió 52 g y se equivocó al escribir). M5: tara 13 g, masa bruta 52 g.")
build(
    O3, 3, F,
    use="Aprenderé a analizar una hoja de preparación: calcular masas netas, comprobar la tolerancia, detectar errores de anotación y corregir un registro sin ocultar el error.",
    prior=["Sé calcular la masa neta.", "Sé qué es una tolerancia.", "Sé corregir un registro con traza."],
    explain=[
        "En el laboratorio químico, revisar una hoja de preparación es calcular la masa neta de cada muestra y compararla con el requisito. Una muestra cumple si su masa neta está dentro de la tolerancia, entre el mínimo y el máximo aceptables. Una muestra que no cumple se informa y no se usa hasta resolver la causa.",
        "Si un dato parece un error de anotación, por ejemplo una masa bruta que da una neta muy distinta de las demás, no se corrige por suposición: se compara con el instrumento o con el respaldo y se corrige tachando con una línea, anotando el valor correcto, la fecha y la firma. Si no se puede comprobar, se registra como dato dudoso y se informa al jefe de laboratorio.",
        f"El análisis es de papel; la preparación real la hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("requisito", "valor que la muestra debe tener para poder usarse"), ("tolerancia", "desviación máxima permitida"), ("dato dudoso", "dato que no se puede comprobar y que se informa"), ("corrección con traza", "valor tachado con una línea, valor correcto, fecha y firma"), ("muestra que no cumple", "muestra con valor fuera de tolerancia")],
    worked=[
        ("Comprobar la tolerancia", "Con un requisito de ejemplo de 50 g ±3 g, una muestra tiene masa neta de 54 g. ¿Cumple?", ["El rango aceptable va de 47 a 53 g.", "54 g está fuera de ese rango."], "No cumple"),
        ("Dato dudoso", "Una masa bruta anotada de 92 g da una neta de 80 g, y las demás dan 40 g. ¿Qué se hace?", ["La neta de 80 g es muy distinta de las otras.", "Se compara con el respaldo y, si no se puede comprobar, se informa como dato dudoso."], "Se informa como dato dudoso"),
    ],
    mistakes=[("Corregir un dato sospechoso borrándolo y escribiendo el que «debería ser».", "Se pierde el valor original y no se puede revisar.", "Tacha con una línea, anota el correcto con fecha y firma, y deja respaldo."),
              ("Usar una muestra fuera de tolerancia porque «es muy poca la diferencia».", "La tolerancia es el límite aceptable; fuera de ella no cumple.", "Informa y espera instrucciones.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué significa que una muestra cumpla la tolerancia?", "Que su masa neta está entre el mínimo y el máximo aceptables", "Que su masa bruta es mayor que la tara", "Que tiene rótulo de colores", "Cumplir es estar dentro del rango aceptable."),
        ("abc", "En el laboratorio químico: ¿qué es un dato dudoso?", "Un dato que no se puede comprobar y que se informa", "Un dato que siempre es correcto", "Un dato que no importa", "El dato dudoso se informa sin usarse como válido."),
        ("abc", "En el laboratorio químico: ¿cómo se corrige un dato de la hoja?", "Tachando con una línea, anotando el correcto con fecha y firma", "Borrando y escribiendo encima", "Dejando el dato y avisando de palabra", "La corrección debe dejar visible el valor original."),
        ("=", "{F} ¿Cuál es la masa neta de M1?", "52-12", "Se resta la tara a la masa bruta.", " g"),
        ("=", "{F} ¿Cuál es la masa neta de M2?", "50-12", "Se resta la tara a la masa bruta.", " g"),
        ("=", "{F} ¿Cuál es la masa neta de M4 con el dato tal como se anotó?", "62-12", "Se resta la tara a la masa bruta anotada.", " g"),
        ("=", "{F} ¿Cuál sería la masa neta de M4 si la masa bruta fuera 52 g, como dice el analista?", "52-12", "Se resta la tara a la masa bruta que dice haber medido.", " g"),
        ("abc", "{F} ¿Cuál es la muestra que, con el dato anotado, queda fuera de tolerancia?", "M4", "M2", "M5", "M4 da 50 g, fuera del rango de 38 a 42 g."),
        ("abc", "{F} ¿Cumple la muestra M2 el requisito?", "Sí, porque 38 g está dentro de 38 a 42 g", "No, porque 38 g es menor que 40 g", "No, porque tiene tara de 12 g", "El límite inferior de 38 g aún cumple."),
        ("=", "{F} ¿Cuántas muestras de las 5 cumplen el requisito, suponiendo el dato de M4 tal como se anotó?", "4", "Cumplen M1, M2, M3 y M5; no cumple M4.", " muestras"),
        ("abc", "{F} ¿Cómo debe corregirse la masa bruta de M4 si se confirma con el respaldo que era 52 g?", "Tachando el 62 con una línea y anotando 52, con fecha y firma", "Borrando el 62 y escribiendo 52", "Dejando el 62 y anotando la neta correcta aparte", "La corrección debe dejar visible el valor original."),
        ("abc", "{F} El analista no puede comprobar si midió 52 g o 62 g. ¿Qué corresponde?", "Registrar el dato como dudoso, informar al jefe de laboratorio y no usar la muestra", "Anotar 52 g porque es lo más probable", "Anotar el promedio de 52 y 62", "Sin comprobación no se elige un valor por suposición."),
        em("Revisas la hoja de ejemplo en la oficina cuando alguien avisa que en el laboratorio se rompió un frasco de vidrio y que hay un olor fuerte.", 2),
    ],
    ctx=("abc", "Una analista de ejemplo dice: «M4 da 50 g, pero la uso igual, el ensayo no se nota». ¿Qué respondes?", "Que no corresponde: M4 está fuera de tolerancia y debe informarse al jefe de laboratorio", "Que sí, si el resto cumple", "Que sí, si hace dos réplicas", "Una muestra fuera de tolerancia no se usa sin autorización."),
    sc=[
        ("En el laboratorio químico: ¿qué rango acepta un requisito de 40 g con tolerancia de ±2 g?", "De 38 a 42 g", "Se resta y se suma la tolerancia al valor del requisito."),
        ("En el laboratorio químico: ¿qué se hace con una muestra fuera de tolerancia?", "Se informa y no se usa sin autorización", "No cumple el requisito del método."),
        ("¿Se corrige un dato por suposición?", "No, se comprueba y se corrige con traza", "La suposición no es un respaldo."),
    ],
    op=("Hoja ficticia del «Laboratorio Demo Costa Norte»: requisito de 30 g con tolerancia de ±1 g. N1: tara 10 g y bruta 40 g. N2: tara 10 g y bruta 42 g. N3: tara 11 g y bruta 41 g. Escribe (a) la masa neta de cada una, (b) qué rango acepta el requisito, (c) cuáles cumplen, (d) qué harías con la que no cumple.",
        "(a) N1: 30 g; N2: 32 g; N3: 30 g. (b) De 29 a 31 g. (c) Cumplen N1 y N3. (d) Informar al jefe de laboratorio y no usarla sin autorización.",
        ["calcula las masas netas", "calcula el rango", "identifica las que cumplen", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["no restar la tara", "no aplicar la tolerancia", "usar la muestra fuera de rango"],
        "Pregunta: «¿cuál es el máximo aceptable?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una hoja con cuatro muestras, un requisito y una tolerancia, y decide cuáles cumplen.",
    extend="Explica con un ejemplo por qué no se corrige un dato dudoso por suposición.",
)

# ============================================================ OAM-03, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada) del «Laboratorio Demo Valle Claro». Solución madre A: 200 g/L; se usa una alícuota de 10 mL y el volumen final es de 100 mL. Solución madre B: 150 g/L; alícuota de 20 mL y volumen final de 100 mL. "
     "Fórmula de planilla de ejemplo: concentración final = concentración madre × volumen de la alícuota ÷ volumen final. Muestra sólida de ejemplo: 30 g de un componente en 200 g de muestra. "
     "Una solución de ejemplo de 20 g/L ocupa un volumen de 5 L. Los cálculos son solo de planilla: cómo se prepara lo define el método y lo hace personal formado.")
build(
    O3, 4, F,
    use="Aprenderé a hacer cálculos de planilla de concentración y dilución con números enteros: concentración final, porcentaje en masa y masa de componente en un volumen, sin que esto signifique saber preparar soluciones.",
    prior=["Sé qué es una alícuota y un factor de dilución.", "Sé multiplicar y dividir números enteros.", "Sé calcular porcentajes."],
    explain=[
        "En el laboratorio químico, la concentración de una solución dice cuánto de un componente hay en un volumen; en este cuaderno se expresa en gramos por litro (g/L). Para saber qué concentración queda al diluir, la planilla usa: concentración final igual a concentración madre por volumen de la alícuota, dividido por el volumen final. El porcentaje en masa de un componente es su masa dividida entre la masa total de la muestra, por 100.",
        "La masa de componente en un volumen de solución se calcula multiplicando la concentración por el volumen: 20 g/L en 5 L son 100 g. Los valores son de ejemplo y están elegidos para que las divisiones sean exactas. En una orden real, las cantidades las fija el método aprobado y la preparación la hace personal formado.",
        f"Este cuaderno no enseña a preparar soluciones ni a diluir sustancias: solo muestra cómo se calcula en una planilla. {EMER} {AVISO}",
    ],
    vocab=[("concentración", "cantidad de componente por unidad de volumen, aquí en g/L"), ("solución madre", "solución de partida de la que se toma una alícuota"), ("concentración final", "concentración después de la dilución"), ("porcentaje en masa", "masa del componente dividida entre la masa total, por 100"), ("masa de componente", "concentración multiplicada por el volumen")],
    worked=[
        ("Concentración final", "Una solución madre de ejemplo de 100 g/L, una alícuota de 20 mL y un volumen final de 200 mL. ¿Qué concentración final resulta?", ["Se multiplica 100 por 20, que da 2.000.", "2.000 entre 200 son 10."], "10 g/L"),
        ("Porcentaje en masa", "Una muestra de ejemplo de 400 g contiene 40 g de un componente. ¿Qué porcentaje en masa es?", ["Se divide 40 entre 400 y se multiplica por 100.", "40 por 100 son 4.000, y 4.000 entre 400 son 10."], "10 %"),
    ],
    mistakes=[("Dividir la concentración madre entre la alícuota en vez de multiplicarla.", "La alícuota aporta componente; la dilución se calcula con ese producto dividido entre el volumen final.", "Aplica la fórmula: concentración × alícuota ÷ volumen final."),
              ("Confundir g/L con %.", "Son formas distintas de expresar la cantidad de componente y no se intercambian sin calcular.", "Usa cada unidad con su fórmula.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué indica la concentración de una solución?", "Cuánto componente hay por unidad de volumen", "Cuánto pesa el envase vacío", "Cuántas réplicas se pidieron", "La concentración relaciona componente y volumen."),
        ("abc", "En el laboratorio químico: ¿qué es una solución madre?", "La solución de partida de la que se toma una alícuota", "Una muestra sin componente", "El resultado del ensayo", "La madre es el punto de partida de la dilución."),
        ("abc", "En el laboratorio químico: ¿cómo se calcula el porcentaje en masa de un componente?", "Masa del componente entre masa total, por 100", "Masa total entre masa del componente, por 100", "Volumen entre concentración", "Se compara la parte con el total."),
        ("=", "{F} ¿Qué concentración final tiene la dilución de la solución madre A?", "200*10//100", "Se multiplica la concentración madre por la alícuota y se divide entre el volumen final.", " g/L"),
        ("=", "{F} ¿Qué concentración final tiene la dilución de la solución madre B?", "150*20//100", "Se multiplica la concentración madre por la alícuota y se divide entre el volumen final.", " g/L"),
        ("=", "{F} ¿Qué porcentaje en masa tiene el componente de la muestra sólida?", "30*100//200", "Se divide la masa del componente entre la masa de la muestra y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos gramos de componente hay en los 5 L de solución de 20 g/L?", "20*5", "Se multiplica la concentración por el volumen.", " g"),
        ("abc", "{F} ¿Qué dilución deja la concentración final más alta?", "La de la solución B, con 30 g/L, frente a 20 g/L de la A", "La de la solución A, con 20 g/L, frente a 30 g/L de la B", "Quedan iguales", "Se comparan 30 g/L de la B y 20 g/L de la A."),
        ("=", "{F} ¿Cuál es el factor de dilución de la solución A?", "100//10", "Se divide el volumen final entre el de la alícuota.", ""),
        ("abc", "{F} Un compañero dice: «30 g/L y 30 % son lo mismo». ¿Es correcto?", "No: son formas distintas de expresar la cantidad de componente", "Sí, porque ambos tienen el número 30", "Sí, si el volumen es de un litro", "Cada unidad se calcula con su propia relación."),
        ("=", "{F} ¿Cuántos gramos de componente habría en 3 L de la solución diluida A (de 20 g/L)?", "20*3", "Se multiplica la concentración por el volumen.", " g"),
        ("abc", "Una estudiante de ejemplo, al ver estos cálculos, quiere «probar» a hacer la dilución con lo que hay en el laboratorio. ¿Qué corresponde?", "No hacerlo: preparar soluciones exige método, formación y autorización", "Hacerlo si lleva guantes", "Hacerlo con cantidades pequeñas", "Los cálculos de planilla no habilitan para preparar."),
        em("Haces cálculos de concentración en la oficina cuando alguien avisa que en el laboratorio se volcó un frasco y que sale humo de la mesa.", 3),
    ],
    ctx=("abc", "Un técnico de ejemplo te pide calcular la concentración final y luego «arreglarla» agregando lo que falte, sin método ni jefe. ¿Qué respondes?", "Que solo calculas en la planilla y que preparar o ajustar soluciones lo hace personal formado según el método", "Que sí, si el cálculo da bien", "Que sí, si lo anotas después", "El cálculo no autoriza a manipular sustancias."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula la concentración final de una dilución en planilla?", "Concentración madre por alícuota, dividido por el volumen final", "Es la fórmula de la ficha."),
        ("En el laboratorio químico: ¿cómo se calcula la masa de componente de un volumen de solución?", "Concentración por volumen", "La masa de componente resulta de multiplicar concentración por volumen."),
        ("¿Habilita este cálculo para preparar soluciones?", "No, solo es un cálculo de planilla", "La preparación exige método y personal formado."),
    ],
    op=("Planilla ficticia del «Laboratorio Demo Costa Norte»: solución madre de 300 g/L, alícuota de 10 mL y volumen final de 100 mL; una muestra sólida de 500 g contiene 50 g de un componente; una solución de 30 g/L ocupa 4 L. Escribe (a) la concentración final de la dilución, (b) el porcentaje en masa de la muestra, (c) los gramos de componente en los 4 L, (d) por qué este cálculo no te habilita para preparar una solución.",
        "(a) 300 por 10 entre 100 son 30 g/L. (b) 50 por 100 entre 500 son 10 %. (c) 30 por 4 son 120 g. (d) Porque preparar soluciones exige método aprobado, formación y autorización.",
        ["calcula la concentración final", "calcula el porcentaje", "calcula la masa de componente", "aclara que el cálculo no habilita"],
        ["hoja con las cuatro respuestas"],
        ["dividir sin multiplicar por la alícuota", "confundir g/L con %", "creer que el cálculo autoriza"],
        "Pregunta: «¿qué se multiplica y qué se divide?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa una solución madre con alícuota y volumen final de números enteros y calcula la concentración final.",
    extend="Explica con un ejemplo por qué los resultados de una dilución en papel no reemplazan el método aprobado.",
)

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (registro de ejemplo, inventado). Ensayo E-12 del «Laboratorio Demo Valle Claro». Estado inicial de la muestra: masa 50 g; temperatura 20 °C; aspecto: polvo blanco; pH 7. "
     "Estado final: masa 45 g; temperatura 20 °C; aspecto: polvo blanco, más compacto; pH 7. Condiciones del laboratorio durante el ensayo: temperatura ambiente 20 °C (rango permitido de 18 a 22 °C) y humedad 50 % (rango permitido de 40 a 60 %). "
     "Instrumentos: balanza verificada ese día con un patrón de 100 g (marcó 100 g) y termómetro con certificado vigente.")
build(
    O4, 1, F,
    use="Aprenderé a leer un registro de estado inicial y cambios de una muestra: qué se mide, qué se observa, qué son los cambios físicos y químicos en términos generales y por qué se controlan las condiciones.",
    prior=["Sé qué es una variable, un límite y un registro.", "Sé calcular un porcentaje.", "Sé qué es un patrón de verificación."],
    explain=[
        "En el laboratorio químico, el estado inicial de una muestra es cómo está antes del ensayo, y el estado final es cómo está después. Se registran medidas, como masa, temperatura y pH, y observaciones, como el aspecto. Un cambio físico altera la forma, el tamaño o el estado de la sustancia, pero no la convierte en otra; un cambio químico forma sustancias nuevas. Quien registra describe lo observado con datos; la interpretación de qué tipo de cambio ocurrió la hace el analista o el especialista.",
        "Las condiciones del laboratorio, como temperatura ambiente y humedad, se controlan y se registran, porque pueden alterar las medidas. Una variable controlada es la que se mantiene dentro de un rango para que no sesgue las observaciones. Antes de medir se comprueba que los instrumentos estén verificados; por ejemplo, una balanza se verifica con una masa patrón.",
        f"Esta clase trabaja con un registro de ejemplo en papel; los ensayos reales los hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("estado inicial", "cómo está la muestra antes del ensayo"), ("estado final", "cómo está la muestra después del ensayo"), ("cambio físico", "cambio de forma, tamaño o estado sin formar otra sustancia"), ("cambio químico", "cambio en que se forman sustancias nuevas"), ("variable controlada", "condición que se mantiene dentro de un rango para no sesgar la medida"), ("verificación con patrón", "comprobación de un instrumento con una referencia conocida")],
    worked=[
        ("Cambio de masa", "Una muestra de ejemplo pasa de 80 g a 72 g. ¿Cuánto cambió su masa y qué porcentaje es?", ["Cambió 80 menos 72, es decir, 8 g.", "8 por 100 entre 80 son 10."], "Bajó 8 g, es decir, 10 %"),
        ("Condición controlada", "Un rango de temperatura ambiente de ejemplo va de 18 a 22 °C y se registra 19 °C. ¿Está controlada?", ["19 está entre 18 y 22.", "La condición está dentro del rango."], "Sí, está controlada"),
    ],
    mistakes=[("Registrar solo la medida final y omitir el estado inicial.", "Sin el estado inicial no se puede calcular el cambio.", "Registra siempre inicial y final con sus unidades."),
              ("Decidir por cuenta propia que un cambio fue «químico» sin que lo confirme el analista.", "La interpretación la hace el analista o el especialista.", "Describe lo que ves con datos y deja la interpretación a quien corresponde.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es el estado inicial de una muestra?", "Cómo está antes del ensayo", "Cómo está al terminar el análisis", "El nombre del cliente", "El estado inicial se registra antes del ensayo."),
        ("abc", "En el laboratorio químico: ¿qué es un cambio químico?", "Un cambio en que se forman sustancias nuevas", "Un cambio de tamaño sin formar otra sustancia", "Un cambio de rótulo", "En un cambio químico aparecen sustancias distintas."),
        ("abc", "En el laboratorio químico: ¿qué es una variable controlada?", "Una condición que se mantiene dentro de un rango para no sesgar la medida", "Una medida que cambia sin parar", "El resultado final del ensayo", "Controlar es mantener la condición dentro de límites."),
        ("=", "{F} ¿Cuántos gramos cambió la masa de la muestra entre el estado inicial y el final?", "50-45", "Se resta la masa final a la inicial.", " g"),
        ("=", "{F} ¿Qué porcentaje de la masa inicial se perdió?", "(50-45)*100//50", "Se divide el cambio entre la masa inicial y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Estaba la temperatura ambiente dentro del rango permitido?", "Sí, porque 20 °C está entre 18 y 22 °C", "No, porque 20 °C es mayor que 18 °C", "No, porque 20 °C es menor que 22 °C", "Estar dentro del rango exige estar entre el mínimo y el máximo."),
        ("abc", "{F} ¿Estaba la humedad dentro del rango permitido?", "Sí, porque 50 % está entre 40 y 60 %", "No, porque 50 % es menor que 60 %", "No, porque 50 % es mayor que 40 %", "El 50 % queda entre ambos límites."),
        ("abc", "{F} ¿Por qué se verificó la balanza con un patrón de 100 g?", "Para comprobar que mide bien antes de usarla", "Para aumentar la masa de la muestra", "Para reemplazar el certificado", "El patrón permite detectar un error del instrumento."),
        ("abc", "{F} El aspecto cambió de «polvo blanco» a «polvo blanco, más compacto». ¿Qué debe hacer quien registra?", "Anotar la observación y dejar la interpretación al analista", "Anotar que hubo un cambio químico", "Omitir el cambio porque el color es igual", "Quien registra describe; el analista interpreta."),
        ("abc", "{F} Un compañero anota solo la masa final de 45 g. ¿Qué problema tiene?", "Falta el estado inicial, y sin él no se calcula el cambio", "Ninguno, porque basta la masa final", "Falta la firma del cliente", "El cambio se calcula comparando inicial y final."),
        ("=", "{F} Si otra muestra del mismo ensayo parte con 60 g y termina con 54 g, ¿cuántos gramos cambió?", "60-54", "Se resta la masa final a la inicial.", " g"),
        ("abc", "{F} ¿Qué corresponde si la temperatura ambiente registrada fuera 25 °C, fuera del rango?", "Anotarlo, informar al jefe de laboratorio y no tomar las medidas como válidas hasta resolverlo", "Seguir midiendo sin anotar nada", "Cambiar el rango permitido", "Una condición fuera de rango puede sesgar las medidas."),
        em("Lees el registro de un ensayo de ejemplo en la oficina cuando alguien avisa que el equipo del laboratorio echa humo y que se siente un olor químico fuerte.", 4),
    ],
    ctx=("abc", "Una analista de ejemplo te dice: «Anota que la temperatura ambiente fue 20 °C, aunque no la medimos». ¿Qué respondes?", "Que no: solo se registra lo realmente medido", "Que sí, porque suele ser 20 °C", "Que sí, si lo escribe con lápiz", "Un registro con datos supuestos no es confiable."),
    sc=[
        ("En el laboratorio químico: ¿qué es un cambio físico?", "Un cambio de forma, tamaño o estado sin formar otra sustancia", "La sustancia sigue siendo la misma."),
        ("En el laboratorio químico: ¿cómo se calcula el cambio de masa?", "Masa inicial menos masa final", "Se comparan los dos estados registrados."),
        ("¿Quién interpreta si un cambio fue físico o químico?", "El analista o el especialista", "Quien registra solo describe lo observado y no interpreta."),
    ],
    op=("Registro ficticio del «Laboratorio Demo Costa Norte»: estado inicial: masa 70 g, temperatura 21 °C, pH 7; estado final: masa 63 g, temperatura 21 °C, pH 7; condiciones: temperatura ambiente 20 °C (rango de 18 a 22 °C) y humedad 70 % (rango de 40 a 60 %). Escribe (a) cuántos gramos y qué porcentaje cambió la masa, (b) si las condiciones estaban controladas, (c) qué debes hacer con la humedad, (d) quién interpreta el tipo de cambio.",
        "(a) Cambió 7 g, que son 10 %. (b) La temperatura sí; la humedad no, porque 70 % supera el máximo de 60 %. (c) Anotarlo e informar al jefe de laboratorio. (d) El analista o el especialista.",
        ["calcula el cambio", "evalúa las condiciones", "indica qué hacer con lo fuera de rango", "nombra quién interpreta"],
        ["hoja con las cuatro respuestas"],
        ["no calcular el porcentaje", "no comparar con el rango", "interpretar sin ser analista"],
        "Pregunta: «¿entre qué valores debería estar la humedad?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa un registro de estado inicial y final de una muestra con cuatro datos y calcula el cambio de masa.",
    extend="Explica con un ejemplo por qué una condición fuera de rango puede sesgar una medida.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (registro de ejemplo, inventado). Control de condiciones del «Laboratorio Demo Valle Claro»: temperatura ambiente 20 °C (rango de 18 a 22 °C); humedad 50 % (rango de 40 a 60 %). Balanza verificada con un patrón de 100 g: marcó 100 g. "
     "Tres réplicas de la masa de una muestra: 40 g, 41 g y 42 g. Blanco: lectura de 2 unidades de ejemplo. Buenas prácticas de registro de ejemplo: legible, con fecha y firma, con unidad, sin borrones y hecho en el momento. Una variable de ejemplo que sesgó: un ventilador cercano a la balanza movía el aire.")
build(
    O4, 2, F,
    use="Aprenderé los conceptos de la medición en laboratorio: variable controlada, sesgo, error sistemático y aleatorio, blanco, réplicas y buenas prácticas de registro, usando datos de ejemplo.",
    prior=["Sé qué es una réplica y un blanco.", "Sé calcular un promedio.", "Sé qué es un registro con traza."],
    explain=[
        "En el laboratorio químico, un sesgo es una desviación que hace que las medidas se alejen del valor verdadero de manera sistemática. El error sistemático se repite siempre en el mismo sentido, por ejemplo una balanza que marca 3 g de más; el error aleatorio cambia de una medida a otra sin patrón fijo. Un blanco permite detectar un error sistemático por contaminación, y las réplicas permiten ver la variación aleatoria.",
        "Para controlar variables que podrían sesgar, se registran las condiciones (temperatura, humedad, corrientes de aire) y se verifican los instrumentos con patrones. El rango de las réplicas es la diferencia entre la mayor y la menor; el promedio de las réplicas resume el resultado. Las buenas prácticas de registro piden que cada anotación sea legible, con unidad, fecha y firma, sin borrones y hecha en el momento.",
        f"Se trabaja con datos de ejemplo en papel; los ensayos y las mediciones reales los hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("sesgo", "desviación sistemática de las medidas respecto del valor verdadero"), ("error sistemático", "error que se repite siempre en el mismo sentido"), ("error aleatorio", "error que cambia de una medida a otra sin patrón fijo"), ("blanco", "ensayo sin muestra para detectar contaminación"), ("rango de las réplicas", "diferencia entre la réplica mayor y la menor"), ("buena práctica de registro", "anotar de forma legible, con unidad, fecha y firma, sin borrones y en el momento")],
    worked=[
        ("Promedio de réplicas", "Tres réplicas de ejemplo dan 30, 33 y 36 g. ¿Cuál es el promedio?", ["Se suman: 30 más 33 más 36 son 99.", "99 entre 3 son 33."], "33 g"),
        ("Error sistemático", "Una balanza de ejemplo marca siempre 2 g más que un patrón. ¿Qué tipo de error es?", ["El error se repite en el mismo sentido.", "Eso es un error sistemático."], "Error sistemático"),
    ],
    mistakes=[("Creer que si las réplicas son parecidas el resultado es correcto.", "Las réplicas parecidas muestran poca variación aleatoria, pero puede haber un error sistemático.", "Verifica también los instrumentos con patrones y el blanco."),
              ("Anotar las mediciones al final del día de memoria.", "El registro debe hacerse en el momento para no olvidar ni cambiar datos.", "Anota cada medida al hacerla, con fecha y firma.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es un error sistemático?", "Un error que se repite siempre en el mismo sentido", "Un error que cambia sin patrón en cada medida", "Un error de la persona que lee el informe", "El sistemático se repite siempre igual."),
        ("abc", "En el laboratorio químico: ¿qué es el error aleatorio?", "Un error que cambia de una medida a otra sin patrón fijo", "Un error que siempre suma lo mismo", "Un error que solo se da en las balanzas", "El error aleatorio varía sin un patrón fijo entre medidas."),
        ("abc", "En el laboratorio químico: ¿para qué se anotan las condiciones del laboratorio?", "Porque pueden sesgar las medidas", "Para decorar el registro", "Para reemplazar la firma", "Las condiciones pueden alterar los resultados."),
        ("=", "{F} ¿Cuál es el promedio de las tres réplicas de la masa?", "(40+41+42)//3", "Se suman las tres réplicas y se divide entre 3.", " g"),
        ("=", "{F} ¿Cuál es el rango de las tres réplicas?", "42-40", "Se resta la réplica menor a la mayor.", " g"),
        ("abc", "{F} ¿Qué indica que la balanza marcó 100 g con el patrón de 100 g?", "Que no se detecta error en esa verificación", "Que la balanza está descalibrada", "Que la muestra pesa 100 g", "Si marca el valor del patrón, la verificación no muestra error."),
        ("abc", "{F} ¿Qué efecto podría tener el ventilador cercano a la balanza?", "Mover el aire y alterar las lecturas, lo que sesga las medidas", "Aumentar la masa de la muestra", "Mejorar la exactitud de la balanza", "Las corrientes de aire pueden perturbar la balanza."),
        ("abc", "{F} ¿Qué corresponde hacer con el ventilador?", "Registrarlo e informar para que se resuelva antes de medir", "Medir igual y no anotar nada", "Anotar que no había ventilador", "Una variable no controlada se informa y se resuelve."),
        ("abc", "{F} Una analista anota las tres réplicas al final del día, de memoria. ¿Qué corresponde?", "Corregir la práctica: anotar cada medida en el momento", "Dejarlo si recuerda bien los valores", "Dejarlo si firma al final", "El registro debe hacerse en el momento."),
        ("=", "{F} Si el blanco marca 2 unidades y una lectura de la muestra marca 52 unidades, ¿cuántas unidades vale la lectura corregida por el blanco?", "52-2", "Se resta la lectura del blanco a la lectura de la muestra.", " unidades"),
        ("abc", "{F} Las tres réplicas valen 40, 41 y 42 g. ¿Qué tipo de variación muestran?", "Una variación pequeña entre réplicas, típica del error aleatorio", "Un error sistemático, porque todas son distintas", "Ninguna variación", "Las diferencias pequeñas y sin patrón fijo son aleatorias."),
        ("=", "{F} ¿Cuántas réplicas tienen una masa mayor o igual a 41 g?", "2", "Son las de 41 g y 42 g.", " réplicas"),
        em("Lees un registro de condiciones del laboratorio cuando alguien avisa que se rompió un equipo de la sala y que sale humo con olor extraño.", 5),
    ],
    ctx=("abc", "Una compañera de ejemplo dice: «Mis réplicas dan 40, 41 y 42, así que el resultado es correcto». ¿Qué respondes?", "Que las réplicas parecidas indican poca variación, pero falta verificar que no haya un error sistemático", "Que sí, porque son muy parecidas", "Que sí, si el promedio es 41", "Una pequeña variación no descarta un error sistemático."),
    sc=[
        ("En el laboratorio químico: ¿qué es el sesgo?", "Una desviación sistemática de las medidas respecto del valor verdadero", "El sesgo aleja las medidas del verdadero valor."),
        ("En el laboratorio químico: ¿cómo se corrige una lectura con el blanco?", "Se resta la lectura del blanco a la de la muestra", "Así se elimina la contaminación detectada."),
        ("¿Cuándo debe anotarse una medición?", "En el momento en que se hace", "Anotar después aumenta el riesgo de error."),
    ],
    op=("Registro ficticio del «Laboratorio Demo Costa Norte»: tres réplicas de masa de una muestra: 60 g, 63 g y 66 g; blanco de 3 unidades; lectura de la muestra de 63 unidades; la balanza se verificó con un patrón de 100 g y marcó 104 g; tolerancia de ±2 g. Escribe (a) el promedio de las réplicas, (b) la lectura corregida por el blanco, (c) si la balanza cumple la tolerancia y qué harías, (d) por qué se anotan las condiciones.",
        "(a) 189 entre 3 son 63 g. (b) 63 menos 3 son 60 unidades. (c) No cumple: el error es de 4 g, mayor que 2 g; se informa y no se usa hasta que se revise. (d) Porque pueden sesgar las medidas.",
        ["calcula el promedio", "corrige con el blanco", "evalúa la balanza", "explica el control de condiciones"],
        ["hoja con las cuatro respuestas"],
        ["no restar el blanco", "aceptar la balanza fuera de tolerancia", "no anotar condiciones"],
        "Pregunta: «¿cuánto se aleja la balanza del patrón?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa tres réplicas con un blanco y calcula el promedio y la lectura corregida.",
    extend="Explica con un ejemplo por qué un error sistemático es más difícil de detectar que uno aleatorio.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Registro de tres réplicas de la masa de una muestra en el «Laboratorio Demo Valle Claro»: réplica 1: 40 g con temperatura ambiente de 20 °C; réplica 2: 41 g con 21 °C; réplica 3: 47 g con 26 °C. "
     "Rango permitido de temperatura ambiente: de 18 a 22 °C. Regla de ejemplo: se aceptan réplicas que se diferencian entre sí en 2 g o menos. La réplica 3 se anotó sin firma.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un caso con réplicas: calcular diferencias, comprobar condiciones, detectar un dato atípico y decidir qué informar sin repetir ni corregir por cuenta propia.",
    prior=["Sé qué es una réplica, un rango y un dato atípico.", "Sé comparar un valor con un rango.", "Sé qué es un registro con traza."],
    explain=[
        "En el laboratorio químico, al analizar réplicas se calcula la diferencia entre la mayor y la menor y se compara con la regla de aceptación. Si una réplica se aleja mucho de las demás, es un dato atípico; antes de descartarla, se revisan sus condiciones: si fue medida fuera del rango de temperatura o sin verificación, hay una causa posible. Un dato atípico no se descarta ni se promedia sin decisión del responsable.",
        "El registro debe ser completo: valor, unidad, fecha, firma y condiciones. Una réplica sin firma es una no conformidad. Lo que corresponde es informar al jefe de laboratorio con los datos, y que él decida si se repite el ensayo, quién lo repite y bajo qué condiciones. Quien registra no repite ni corrige por cuenta propia.",
        f"El caso se resuelve en papel. {EMER} {AVISO}",
    ],
    vocab=[("regla de aceptación", "criterio que fija cuánto pueden diferir las réplicas para aceptarse"), ("dato atípico", "valor muy distinto de los demás"), ("condición fuera de rango", "condición ambiental que se salió del rango permitido"), ("no conformidad", "incumplimiento de un requisito del registro o del método"), ("repetir el ensayo", "volver a hacerlo por decisión del responsable")],
    worked=[
        ("Aplicar la regla", "Tres réplicas de ejemplo dan 50, 51 y 52 g y la regla acepta diferencias de hasta 3 g. ¿Se aceptan?", ["La mayor menos la menor es 52 menos 50, es decir, 2 g.", "2 g es menor que 3 g, así que se aceptan."], "Sí, se aceptan"),
        ("Revisar condiciones", "Una réplica de ejemplo fue medida a 28 °C y el rango permitido llega a 22 °C. ¿Qué se informa?", ["28 °C está fuera del rango permitido.", "Se informa que la réplica se midió fuera de condiciones."], "Que se midió fuera de condiciones"),
    ],
    mistakes=[("Descartar la réplica atípica y promediar solo las otras dos sin avisar.", "Esa decisión no es de quien registra y puede ocultar un problema.", "Informa los datos y deja la decisión al responsable."),
              ("Repetir la medida por cuenta propia hasta que dé «bien».", "Repetir hasta que cuadre sesga los resultados.", "Informa y espera la decisión del jefe de laboratorio.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es una regla de aceptación de réplicas?", "El criterio que fija cuánto pueden diferir para aceptarse", "El orden en que se miden", "El nombre de la balanza", "La regla marca el máximo de diferencia aceptable."),
        ("abc", "En el laboratorio químico: ¿qué se hace antes de descartar un dato atípico?", "Se revisan sus condiciones y se informa al responsable", "Se borra del registro", "Se reemplaza por el promedio", "El descarte no se hace sin revisar causas ni decisión del responsable."),
        ("abc", "En el laboratorio químico: ¿quién decide si se repite un ensayo?", "El jefe de laboratorio o el responsable", "Quien registra el dato", "El cliente", "La decisión de repetir el ensayo es del responsable."),
        ("=", "{F} ¿Cuál es la diferencia entre la mayor y la menor de las tres réplicas?", "47-40", "Se resta la réplica menor a la mayor.", " g"),
        ("abc", "{F} ¿Cumplen las tres réplicas la regla de aceptación de 2 g?", "No, porque la diferencia de 7 g supera los 2 g", "Sí, porque son tres réplicas", "Sí, porque 47 es mayor que 40", "La diferencia entre la mayor y la menor debe ser de 2 g o menos."),
        ("abc", "{F} ¿Qué réplica es la atípica?", "La réplica 3, con 47 g", "La réplica 1, con 40 g", "La réplica 2, con 41 g", "El 47 g se aleja de las otras dos."),
        ("abc", "{F} ¿Qué condición de la réplica 3 está fuera de rango?", "La temperatura ambiente de 26 °C", "La masa de 47 g", "El nombre del analista", "El máximo permitido de temperatura es 22 °C."),
        ("=", "{F} ¿Cuál es la diferencia entre las réplicas 1 y 2?", "41-40", "Se resta la menor a la mayor de las dos.", " g"),
        ("=", "{F} ¿Cuántos °C sobre el máximo permitido estuvo la temperatura de la réplica 3?", "26-22", "Se resta el máximo permitido a la temperatura registrada.", " °C"),
        ("abc", "{F} ¿Qué falla de registro tiene la réplica 3, además de la temperatura?", "No tiene firma", "No tiene masa", "No tiene fecha del ensayo", "La ficha dice que se anotó sin firma."),
        ("abc", "{F} Un analista propone promediar solo las réplicas 1 y 2 y no avisar de la 3. ¿Qué corresponde?", "Rechazarlo: debe informar los datos y dejar la decisión al jefe de laboratorio", "Aceptarlo, porque las dos primeras son parecidas", "Aceptarlo si las firma otra persona", "Ocultar una réplica sesga el resultado."),
        ("abc", "{F} Otra persona dice que repetirá la medida «hasta que dé 41 g». ¿Qué corresponde?", "Rechazarlo: repetir hasta que cuadre sesga el resultado", "Aceptarlo si lo hace rápido", "Aceptarlo si anota solo la última", "Se informa y se espera la decisión del responsable."),
        em("Analizas las réplicas de ejemplo en la oficina cuando alguien avisa que se rompió un envase en el laboratorio y que sale vapor con olor fuerte.", 0),
    ],
    ctx=("abc", "Una supervisora de ejemplo te dice: «Borra la réplica 3 del registro, no la usemos». ¿Qué respondes?", "Que no se borra: se informa como dato atípico con sus condiciones y se espera la decisión del jefe de laboratorio", "Que sí, si la firma", "Que sí, si el promedio mejora", "Un dato no se borra: el registro debe conservar todo lo medido."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula la diferencia entre réplicas?", "La mayor menos la menor", "La diferencia mide la dispersión de las réplicas."),
        ("En el laboratorio químico: ¿se borra un dato atípico?", "No, se informa y decide el responsable", "El registro conserva todo lo medido."),
        ("¿Qué condiciones se revisan ante un dato atípico?", "Temperatura, humedad y verificación de instrumentos", "Pueden explicar por qué el dato se aleja."),
    ],
    op=("Caso ficticio del «Laboratorio Demo Costa Norte»: tres réplicas: 30 g a 20 °C, 31 g a 21 °C y 36 g a 25 °C; rango permitido de 18 a 22 °C; regla de aceptación de 2 g. Escribe (a) la diferencia entre la mayor y la menor, (b) si se cumple la regla, (c) cuál es la réplica atípica y qué condición pudo influir, (d) qué debes hacer con ese dato.",
        "(a) 36 menos 30 son 6 g. (b) No, porque 6 g supera los 2 g. (c) La tercera, medida a 25 °C, fuera del rango. (d) Informarla al jefe de laboratorio sin borrarla ni repetirla por cuenta propia.",
        ["calcula la diferencia", "aplica la regla", "identifica el dato atípico y la causa posible", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["promediar sin avisar", "borrar el dato", "repetir hasta que cuadre"],
        "Pregunta: «¿qué temperatura estuvo fuera del rango?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa tres réplicas con condiciones y decide si se cumple la regla y qué informarías.",
    extend="Explica con un ejemplo por qué repetir una medición hasta que dé el valor esperado es una mala práctica.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada) del «Laboratorio Demo Valle Claro». Lecturas de una muestra: 52, 54 y 50 unidades de ejemplo. Blanco: 2 unidades. Valor de referencia de una muestra de control: 100 unidades; el laboratorio midió 96. "
     "Criterio de aceptación de ejemplo de la muestra de control: recuperación entre 95 % y 105 %. Fórmula de ejemplo: recuperación (%) = valor medido × 100 ÷ valor de referencia. Error absoluto = |valor medido − valor de referencia|. Masa inicial de una muestra: 200 g; masa final: 180 g.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo: corregir lecturas con el blanco, calcular error absoluto, recuperación y variación de masa, y compararlos con un criterio de aceptación.",
    prior=["Sé qué es un blanco y una réplica.", "Sé calcular porcentajes.", "Sé qué es un criterio de aceptación."],
    explain=[
        "En el laboratorio químico, la lectura corregida es la lectura de la muestra menos la lectura del blanco. Una muestra de control es una muestra con valor de referencia conocido que se mide para comprobar que el método funciona. El error absoluto es la diferencia, sin signo, entre el valor medido y el de referencia. La recuperación, en porcentaje, es el valor medido por 100 dividido por el valor de referencia.",
        "Un criterio de aceptación fija entre qué valores debe estar la recuperación para considerar que el método funciona bien; si queda fuera, se informa y no se aceptan los resultados de esa serie. La variación de masa entre el estado inicial y final se calcula como cambio entre valor inicial, por 100. Todos los cálculos de este cuaderno usan números enteros.",
        f"Los cálculos son de planilla; las mediciones reales las hace personal formado. {EMER} {AVISO}",
    ],
    vocab=[("lectura corregida", "lectura de la muestra menos la lectura del blanco"), ("muestra de control", "muestra de valor de referencia conocido que se mide para comprobar el método"), ("error absoluto", "diferencia sin signo entre el valor medido y el de referencia"), ("recuperación", "valor medido por 100 dividido por el valor de referencia"), ("criterio de aceptación", "rango en que debe estar un resultado para aceptarse")],
    worked=[
        ("Recuperación", "Una muestra de control de ejemplo tiene referencia de 50 y se mide 48. ¿Cuál es la recuperación?", ["Se multiplica 48 por 100, que da 4.800.", "4.800 entre 50 son 96."], "96 %"),
        ("Error absoluto", "Una medida de ejemplo es 47 y la referencia es 50. ¿Cuál es el error absoluto?", ["Se resta el valor menor al mayor, sin signo.", "50 menos 47 son 3."], "3"),
    ],
    mistakes=[("Restar el blanco solo a una de las lecturas.", "El blanco corrige todas las lecturas de la misma serie.", "Resta el blanco a cada lectura de la serie."),
              ("Aceptar los resultados de una serie cuyo control quedó fuera de criterio.", "Si el control falla, no se sabe si el método funcionó bien.", "Informa y no aceptes los resultados hasta resolverlo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es una muestra de control?", "Una muestra de valor de referencia conocido que se mide para comprobar el método", "Una muestra que no se mide", "Una muestra sin rótulo", "El control permite verificar que el método funciona."),
        ("abc", "En el laboratorio químico: ¿qué es el error absoluto?", "La diferencia sin signo entre el valor medido y el de referencia", "El porcentaje de la masa perdida", "La lectura del blanco", "Se calcula sin importar el signo."),
        ("abc", "En el laboratorio químico: ¿qué es un criterio de aceptación?", "El rango en que debe estar un resultado para aceptarse", "El nombre del método", "La fecha del informe", "El criterio fija los límites de lo aceptable."),
        ("=", "{F} ¿Cuál es la primera lectura corregida por el blanco (52 unidades)?", "52-2", "Se resta la lectura del blanco.", " unidades"),
        ("=", "{F} ¿Cuál es el promedio de las tres lecturas corregidas?", "((52-2)+(54-2)+(50-2))//3", "Se corrige cada lectura con el blanco, se suman y se divide entre 3.", " unidades"),
        ("=", "{F} ¿Cuál es el error absoluto de la muestra de control?", "100-96", "Se resta el valor medido al de referencia.", " unidades"),
        ("=", "{F} ¿Cuál es la recuperación de la muestra de control?", "96*100//100", "Se multiplica por 100 el valor medido y se divide entre la referencia.", " %"),
        ("abc", "{F} ¿Cumple la muestra de control el criterio de aceptación de 95 % a 105 %?", "Sí, porque 96 % está entre 95 % y 105 %", "No, porque 96 % es menor que 100 %", "No, porque 96 % es mayor que 95 %", "El criterio acepta valores entre ambos límites."),
        ("=", "{F} ¿Cuántos gramos cambió la masa de la muestra entre el estado inicial y el final?", "200-180", "Se resta la masa final a la inicial.", " g"),
        ("=", "{F} ¿Qué porcentaje de la masa inicial cambió?", "(200-180)*100//200", "Se divide el cambio entre la masa inicial y se multiplica por 100.", " %"),
        ("abc", "{F} Si la muestra de control hubiera dado 90 unidades, ¿qué corresponde?", "Informar que quedó fuera del criterio y no aceptar los resultados hasta resolverlo", "Aceptar los resultados porque 90 es cercano a 100", "Restar 10 a todas las lecturas por cuenta propia", "Con el control fuera de criterio, la serie no es confiable."),
        ("=", "{F} Si la lectura de la muestra fuera 60 y el blanco 2, ¿cuántas unidades vale la lectura corregida?", "60-2", "Se resta el blanco a la lectura.", " unidades"),
        em("Haces cálculos de control en la oficina del laboratorio cuando alguien avisa que se cayó un frasco y que hay un olor muy fuerte y gases en la sala.", 1),
    ],
    ctx=("abc", "Una analista de ejemplo dice: «El control dio 90 sobre 100, pero igual informemos los resultados». ¿Qué respondes?", "Que no: el control quedó fuera del criterio y debe informarse al jefe de laboratorio", "Que sí, si los resultados parecen razonables", "Que sí, si se indica en el informe", "Un control fuera de criterio impide confiar en la serie."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula la recuperación?", "Valor medido por 100 entre el valor de referencia", "Compara lo medido con lo esperado."),
        ("En el laboratorio químico: ¿qué es la lectura corregida?", "La lectura de la muestra menos la del blanco", "Se descuenta así la contaminación detectada por el blanco."),
        ("¿Qué se hace si el control queda fuera del criterio?", "Se informa y no se aceptan los resultados", "Si falla el control, la serie no es confiable."),
    ],
    op=("Planilla ficticia del «Laboratorio Demo Costa Norte»: lecturas de la muestra: 31, 33 y 35 unidades; blanco: 1 unidad; muestra de control con referencia de 200 y medida de 196; criterio de aceptación de 95 % a 105 %. Escribe (a) las lecturas corregidas, (b) su promedio, (c) la recuperación del control, (d) si el control cumple el criterio y qué harías si no lo cumpliera.",
        "(a) 30, 32 y 34 unidades. (b) 96 entre 3 son 32. (c) 196 por 100 entre 200 son 98 %. (d) Sí cumple porque 98 % está dentro del criterio; si no cumpliera, se informaría y no se aceptarían los resultados.",
        ["corrige con el blanco", "calcula el promedio", "calcula la recuperación", "aplica el criterio de aceptación"],
        ["hoja con las cuatro respuestas"],
        ["no restar el blanco a todas las lecturas", "dividir al revés", "aceptar un control fuera de criterio"],
        "Pregunta: «¿qué se resta a cada lectura?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa tres lecturas con blanco y una muestra de control, y calcula la recuperación.",
    extend="Explica con un ejemplo por qué se mide una muestra de control junto con las muestras reales.",
)

# ============================================================ OAM-04, clase 5
F = ("Ficha 5 (caso de ejemplo, inventado). Dos registros de la misma medición de masa en el «Laboratorio Demo Valle Claro». Registro R1: «Masa 40 g; temperatura 20 °C; fecha; firma; hecho en el momento; sin borrones». "
     "Registro R2: «Masa 400 g» con un valor tachado y sobrescrito sin firma, sin hora y sin temperatura. Balanza X: resolución 1 g, verificada hoy con el patrón. Balanza Y: resolución 10 g, verificada hoy con el patrón. Tolerancia de la medición: ±2 g. "
     "Regla de ejemplo: la resolución debe ser menor que la tolerancia. Lista de control de registros, 5 puntos: valor con unidad; fecha y hora; firma; condiciones; sin borrones. Se revisaron 12 registros: 9 cumplen los 5 puntos y 3 no.")
build(
    O4, 5, F,
    use="Aprenderé a comparar instrumentos y registros de una misma medición con una regla de resolución y una lista de control, y a verificar la calidad de la información antes de usarla.",
    prior=["Sé qué es la resolución y la tolerancia.", "Sé calcular porcentajes.", "Sé qué es un registro con traza."],
    explain=[
        "En el laboratorio químico, al comparar dos instrumentos se aplica una condición obligatoria: la resolución debe ser menor que la tolerancia de la medición, porque si no, el instrumento no distingue lo que se quiere controlar. Entre los que cumplen, se mira la verificación vigente y el costo. Un instrumento sin verificación vigente no se usa.",
        "Al comparar dos registros de la misma medición se revisa cuál cumple las buenas prácticas: valor con unidad, fecha y hora, firma, condiciones y sin borrones. El registro que no las cumple se informa y no se usa como respaldo del resultado. El porcentaje de registros conformes es los registros que cumplen todos los puntos entre los revisados, por 100.",
        f"Se trabaja con documentos de ejemplo; medir y registrar en el laboratorio real corresponde a personal formado. {EMER} {AVISO}",
    ],
    vocab=[("condición obligatoria", "requisito que una opción debe cumplir para poder elegirse"), ("resolución", "cambio más pequeño que el instrumento puede mostrar"), ("registro conforme", "registro que cumple todos los puntos de la lista de control"), ("buena práctica de registro", "anotar de forma legible, con unidad, fecha, firma y sin borrones")],
    worked=[
        ("Elegir un instrumento", "Una tolerancia de ejemplo es ±5 g. El instrumento P tiene resolución de 10 g y el Q, de 1 g. ¿Cuál cumple la regla?", ["La resolución debe ser menor que la tolerancia.", "10 no es menor que 5, pero 1 sí."], "El instrumento Q"),
        ("Porcentaje de conformidad", "De 20 registros de ejemplo, 15 cumplen los 5 puntos. ¿Qué porcentaje es?", ["Se divide 15 entre 20 y se multiplica por 100.", "15 por 100 son 1.500, y 1.500 entre 20 son 75."], "75 %"),
    ],
    mistakes=[("Elegir el instrumento más barato aunque su resolución no cumpla la regla.", "No distingue lo que se quiere controlar.", "Aplica primero la regla y luego compara el costo."),
              ("Usar un registro con borrones como respaldo.", "Un registro con borrones no deja traza ni responsable.", "Informa y pide una corrección con traza.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué regla relaciona la resolución con la tolerancia?", "La resolución debe ser menor que la tolerancia", "La resolución debe ser mayor que la tolerancia", "La resolución debe ser igual al error", "Así el instrumento distingue lo que se quiere controlar."),
        ("abc", "En el laboratorio químico: ¿qué es un registro conforme?", "Uno que cumple todos los puntos de la lista de control", "Uno con mucha información", "Uno firmado por el cliente", "Conforme significa que cumple todo lo exigido."),
        ("abc", "En el laboratorio químico: ¿por qué no se usa un instrumento sin verificación vigente?", "Porque no hay respaldo de que mida bien", "Porque pesa más", "Porque tiene otra unidad", "La verificación vigente respalda que la medida es confiable."),
        ("abc", "{F} ¿Cuál es la tolerancia de la medición?", "±2 g", "±10 g", "±1 g", "La ficha fija una tolerancia de ±2 g para la medición."),
        ("abc", "{F} ¿Cumple la balanza X la regla de resolución?", "Sí, porque 1 g es menor que 2 g", "No, porque la resolución debería ser igual a la tolerancia", "No, porque no está verificada", "La resolución de 1 g es menor que la tolerancia de 2 g."),
        ("abc", "{F} ¿Por qué la balanza Y no sirve para esta medición?", "Su resolución de 10 g es mayor que la tolerancia de 2 g", "Su resolución es de 1 g", "No está verificada", "No distinguiría diferencias de 2 g."),
        ("abc", "{F} ¿Qué registro cumple las buenas prácticas?", "El R1", "El R2", "Ambos", "R1 tiene valor, unidad, temperatura, fecha, firma y no tiene borrones."),
        ("abc", "{F} ¿Qué problemas tiene el registro R2?", "Valor sobrescrito sin firma y faltan hora y temperatura", "Solo falta la unidad", "Ninguno, porque dice 400 g", "La ficha lista varias fallas de R2."),
        ("=", "{F} ¿Qué porcentaje de los 12 registros revisados cumple los 5 puntos?", "9*100//12", "Se divide los conformes entre los revisados y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos de los 12 registros no cumplen?", "12-9", "Se resta los conformes al total.", " registros"),
        ("abc", "{F} ¿Qué corresponde hacer con R2?", "Informarlo y pedir una corrección con traza, sin usarlo como respaldo", "Usarlo porque el valor es parecido", "Borrar el valor sobrescrito", "Un registro con borrones no respalda un resultado."),
        ("=", "{F} Si se corrigen con traza los 3 registros no conformes, ¿cuántos de los 12 cumplirían los 5 puntos?", "9+3", "Se suman los conformes y los corregidos.", " registros"),
        em("Comparas registros de ejemplo cuando alguien avisa que se rompió un envase en el laboratorio y que hay un olor fuerte y gases en el aire.", 2),
    ],
    ctx=("abc", "Un jefe de ejemplo te pide usar la balanza Y «porque está libre», para medir con tolerancia de ±2 g. ¿Qué respondes?", "Que no corresponde: su resolución de 10 g no cumple la regla, y se debe usar la X", "Que sí, si se anota la masa con cuidado", "Que sí, porque Y está verificada", "La resolución debe ser menor que la tolerancia."),
    sc=[
        ("En el laboratorio químico: ¿qué debe cumplir la resolución respecto de la tolerancia?", "Ser menor", "Si no lo es, el instrumento no distingue lo controlado."),
        ("En el laboratorio químico: ¿qué se hace con un registro con borrones?", "Se informa y se corrige con traza", "No sirve como respaldo del resultado."),
        ("¿Cómo se calcula el porcentaje de registros conformes?", "Conformes entre revisados, por 100", "Es una proporción expresada en porcentaje."),
    ],
    op=("Caso ficticio del «Laboratorio Demo Costa Norte»: tolerancia de ±5 g. Balanza M: resolución 10 g. Balanza N: resolución 1 g. Registro S: valor con unidad, fecha, hora, firma y condiciones, sin borrones. Registro T: sin firma y con una cifra sobrescrita. De 10 registros revisados, 8 son conformes. Escribe (a) qué balanza cumple la regla y por qué, (b) qué registro sirve de respaldo, (c) el porcentaje de registros conformes, (d) qué harías con T.",
        "(a) La N, porque su resolución de 1 g es menor que la tolerancia de 5 g. (b) El S. (c) 8 por 100 entre 10 son 80 %. (d) Informarlo y pedir una corrección con traza.",
        ["aplica la regla de resolución", "elige el registro correcto", "calcula la conformidad", "propone la acción sobre T"],
        ["hoja con las cuatro respuestas"],
        ["elegir la balanza M", "usar T como respaldo", "borrar la cifra sobrescrita"],
        "Pregunta: «¿qué resolución es menor que 5 g?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Compara dos registros inventados de la misma medición con la lista de cinco puntos y decide cuál sirve.",
    extend="Explica con un ejemplo por qué la resolución del instrumento debe ser menor que la tolerancia.",
)

# ============================================================ OAM-05, clase 1
O5 = "TP-QULA-4-OAM-05"
F = ("Ficha 1 (caso de ejemplo, inventado). Plan de mantención de equipos del «Laboratorio Demo Valle Claro» (calibración cada cierto número de días y días desde la última): balanza B-5: cada 180 días, última hace 150; pHmetro: cada 90 días, última hace 60; estufa de secado: cada 365 días, última hace 200; centrífuga: cada 365 días, última hace 380. "
     "Peligros anotados: equipo energizado, superficie caliente y vidrio roto. Matriz de ejemplo: puntaje = probabilidad × gravedad. Equipo energizado: probabilidad 2 y gravedad 5. Superficie caliente: probabilidad 3 y gravedad 4. Vidrio roto: probabilidad 3 y gravedad 2. "
     "Roles de ejemplo: el usuario opera y registra; el técnico de mantención autorizado mantiene y ajusta; el jefe de laboratorio aprueba; el fabricante entrega el manual.")
build(
    O5, 1, F,
    use="Aprenderé qué es mantener y ajustar equipos de laboratorio, qué documentos y roles intervienen y por qué solo el técnico autorizado interviene un equipo: este cuaderno no enseña a mantener ni a ajustar nada.",
    prior=["Sé qué es una calibración y un patrón.", "Sé restar números enteros.", "Sé calcular el puntaje de riesgo."],
    explain=[
        "En el laboratorio químico, mantener un equipo es conservarlo en buen estado de funcionamiento, y ajustar es devolverlo a sus especificaciones técnicas cuando se desvía. Ambas tareas las hace un técnico autorizado, según el manual del fabricante, que es el documento que explica el equipo, y la norma vigente. El usuario del equipo lo opera según el método, anota lo que observa en la bitácora y avisa si algo no funciona; no abre ni repara el equipo.",
        "El plan de mantención indica cada cuánto se calibra o revisa un equipo; los días restantes se calculan restando los transcurridos al intervalo. Un equipo con plazo vencido queda fuera de servicio hasta que se renueve su calibración. El bloqueo y etiquetado es una medida de seguridad que impide que un equipo se encienda mientras alguien lo interviene, y solo la aplican personas autorizadas.",
        f"Este cuaderno solo lee planes y calcula plazos: no enseña a intervenir equipos. {EMER} {AVISO}",
    ],
    vocab=[("mantener un equipo", "conservarlo en buen estado de funcionamiento"), ("ajustar un equipo", "devolverlo a sus especificaciones cuando se desvía"), ("manual del fabricante", "documento que explica el equipo y sus condiciones"), ("plan de mantención", "documento que indica cada cuánto se revisa o calibra un equipo"), ("fuera de servicio", "estado de un equipo que no se debe usar hasta resolver su problema"), ("bloqueo y etiquetado", "medida que impide que un equipo se encienda mientras se interviene")],
    worked=[
        ("Días restantes", "Un equipo de ejemplo se calibra cada 120 días y la última calibración fue hace 90 días. ¿Cuántos días quedan?", ["Se resta lo transcurrido al intervalo.", "120 menos 90 son 30."], "30 días"),
        ("Plazo vencido", "Otro equipo de ejemplo se calibra cada 100 días y la última fue hace 112. ¿Está vencido?", ["112 es mayor que 100.", "Está vencido hace 12 días y queda fuera de servicio."], "Sí, vencido hace 12 días"),
    ],
    mistakes=[("Abrir un equipo para «revisar rápido» porque se ve que funciona mal.", "Intervenir un equipo es tarea del técnico autorizado y puede ser peligroso.", "Anota lo observado en la bitácora y avisa al responsable."),
              ("Usar un equipo con la calibración vencida «porque anda bien».", "Sin calibración vigente no hay respaldo de que mida bien.", "No lo uses y avisa que está fuera de servicio.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué significa mantener un equipo?", "Conservarlo en buen estado de funcionamiento", "Usarlo todos los días", "Cambiarle el rótulo", "Mantener es cuidar que siga funcionando bien."),
        ("abc", "En el laboratorio químico: ¿qué es un plan de mantención?", "Un documento que indica cada cuánto se revisa o calibra un equipo", "Una lista de precios de los equipos", "El manual de uso del cliente", "El plan fija la frecuencia de las revisiones."),
        ("abc", "En el laboratorio químico: ¿quién ajusta un equipo?", "El técnico de mantención autorizado", "El usuario que lo opera", "El cliente", "Ajustar es una tarea del técnico autorizado."),
        ("=", "{F} ¿Cuántos días le quedan a la balanza B-5 para su próxima calibración?", "180-150", "Se resta lo transcurrido al intervalo.", " días"),
        ("=", "{F} ¿Cuántos días le quedan a la estufa de secado?", "365-200", "Se resta lo transcurrido al intervalo.", " días"),
        ("abc", "{F} ¿Qué equipo del plan está vencido?", "La centrífuga", "El pHmetro", "La balanza B-5", "Su intervalo es de 365 días y han pasado 380."),
        ("=", "{F} ¿Hace cuántos días venció la calibración de la centrífuga?", "380-365", "Se resta el intervalo a los días transcurridos.", " días"),
        ("=", "{F} ¿Qué puntaje de riesgo tiene la superficie caliente?", "3*4", "Se multiplica la probabilidad por la gravedad.", " puntos"),
        ("abc", "{F} ¿Qué peligro tiene el mayor puntaje de riesgo?", "La superficie caliente, con 12 puntos", "El equipo energizado, con 10 puntos", "El vidrio roto, con 6 puntos", "Se compara probabilidad por gravedad de cada peligro."),
        ("abc", "{F} ¿Qué corresponde con la centrífuga vencida?", "Dejarla fuera de servicio y avisar para renovar la calibración", "Usarla porque funciona bien", "Calibrarla el usuario con un patrón improvisado", "Con calibración vencida no hay respaldo de la medida."),
        ("abc", "{F} Un usuario ve que la estufa parece calentar de más y propone abrirla para revisarla. ¿Qué corresponde?", "No abrirla: anotar lo observado y avisar al técnico autorizado", "Abrirla si está apagada", "Abrirla con guantes", "Intervenir equipos es tarea del técnico autorizado."),
        ("abc", "{F} ¿Quién entrega el manual del equipo según los roles?", "El fabricante", "El usuario", "El jefe de laboratorio", "La ficha asigna el manual al fabricante."),
        em("Lees el plan de mantención de ejemplo en la oficina cuando alguien avisa que la estufa de secado echa humo y que huele a quemado.", 0),
    ],
    ctx=("abc", "Un técnico de ejemplo te dice: «Ayúdame a abrir la centrífuga para ajustarla, tú solo sostén la tapa». No tienes formación ni autorización. ¿Qué respondes?", "Que no, porque intervenir un equipo exige formación y autorización, y que avisarás a un adulto responsable", "Que sí, si solo sostienes la tapa", "Que sí, si el equipo está apagado", "Participar en una intervención sin formación es riesgoso."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calculan los días restantes de una calibración?", "Intervalo menos días transcurridos", "La resta indica cuántos días faltan para el vencimiento."),
        ("En el laboratorio químico: ¿qué se hace con un equipo con calibración vencida?", "Se deja fuera de servicio y se avisa", "No hay respaldo de que mida bien."),
        ("¿Quién ajusta un equipo del laboratorio?", "El técnico autorizado", "El usuario solo opera y registra."),
    ],
    op=("Plan ficticio del «Laboratorio Demo Costa Norte»: balanza: cada 120 días, última hace 100; pHmetro: cada 60 días, última hace 75; estufa: cada 365 días, última hace 100. Peligro: superficie caliente (probabilidad 3, gravedad 3). Escribe (a) los días restantes de la balanza y de la estufa, (b) cuál equipo está vencido y hace cuántos días, (c) el puntaje del peligro, (d) qué debe hacer un usuario si un equipo funciona mal.",
        "(a) Balanza: 20 días; estufa: 265 días. (b) El pHmetro, vencido hace 15 días. (c) 3 por 3 son 9 puntos. (d) No intervenirlo, anotar lo observado en la bitácora y avisar al técnico autorizado.",
        ["calcula los días restantes", "identifica el equipo vencido", "calcula el puntaje", "indica la conducta correcta"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "usar el equipo vencido", "intervenir el equipo"],
        "Pregunta: «¿quién puede ajustar un equipo?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa un plan de mantención con tres equipos, sus intervalos y días transcurridos, y calcula cuáles vencen primero.",
    extend="Explica con un ejemplo por qué el usuario de un equipo no debe ajustarlo.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (documento de ejemplo, inventado). Hoja de vida de la balanza B-5 del «Laboratorio Demo Valle Claro». Especificaciones de ejemplo: rango de 0 a 600 g; resolución 1 g; tolerancia ±2 g; temperatura de trabajo de 18 a 25 °C. Intervalo de calibración: 180 días. "
     "Mantención preventiva (revisión programada): cada 90 días; la última se hizo hace 60 días por un técnico autorizado. Mantención correctiva (reparación por una falla): 2 en el año, la última hace 200 días. "
     "Costos de ejemplo: preventiva, $40.000 por visita, 4 visitas al año; correctiva, $150.000 por visita. Etiqueta «fuera de servicio»: indica que el equipo no debe usarse.")
build(
    O5, 2, F,
    use="Aprenderé los conceptos y documentos del mantenimiento de equipos: hoja de vida, bitácora, mantención preventiva y correctiva, calibración y verificación, especificaciones y etiqueta de fuera de servicio.",
    prior=["Sé qué es un plan de mantención.", "Sé calcular costos y diferencias.", "Sé qué es una calibración."],
    explain=[
        "En el laboratorio químico, la hoja de vida de un equipo reúne sus especificaciones técnicas, su calibración y sus mantenciones. Las especificaciones indican su rango, su resolución, su tolerancia y las condiciones en que debe trabajar. La bitácora es el registro diario de uso, verificaciones y novedades. La mantención preventiva es una revisión programada para evitar fallas; la correctiva es una reparación después de una falla, y suele costar más.",
        "La verificación es una comprobación rápida con un patrón, que puede hacer el usuario según el método; la calibración es una comparación más completa con patrones certificados, que hace un técnico autorizado y deja un certificado. Cuando un equipo no cumple, se le pone la etiqueta de fuera de servicio y no se usa hasta que lo revise un técnico.",
        f"Este cuaderno trabaja con documentos de ejemplo en papel; intervenir equipos corresponde a personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("hoja de vida", "documento que reúne especificaciones, calibraciones y mantenciones de un equipo"), ("bitácora", "registro diario de uso, verificaciones y novedades del equipo"), ("mantención preventiva", "revisión programada para evitar fallas"), ("mantención correctiva", "reparación hecha después de una falla"), ("verificación", "comprobación rápida con un patrón"), ("etiqueta de fuera de servicio", "señal que indica que el equipo no debe usarse")],
    worked=[
        ("Costo anual", "Una mantención preventiva de ejemplo cuesta $30.000 y se hacen 3 al año. ¿Cuál es el costo anual?", ["Se multiplica el costo por las visitas.", "30.000 por 3 son 90.000."], "$90.000"),
        ("Clasificar una mantención", "Un técnico de ejemplo repara un equipo después de que dejó de funcionar. ¿Qué tipo de mantención es?", ["La reparación ocurre después de una falla.", "Eso es una mantención correctiva."], "Correctiva"),
    ],
    mistakes=[("Pensar que verificar y calibrar son lo mismo.", "La verificación es una comprobación rápida; la calibración es más completa y la hace un técnico autorizado con certificado.", "Registra cada una con su nombre y con quién la hizo."),
              ("Quitar la etiqueta de «fuera de servicio» para usar el equipo «solo hoy».", "La etiqueta indica que el equipo no es seguro o confiable.", "Solo el técnico autorizado la retira después de revisar el equipo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es la hoja de vida de un equipo?", "El documento que reúne sus especificaciones, calibraciones y mantenciones", "El manual de usuario del cliente", "El rótulo de las muestras", "La hoja de vida resume la historia del equipo."),
        ("abc", "En el laboratorio químico: ¿qué es una mantención correctiva?", "Una reparación hecha después de una falla", "Una revisión programada para evitar fallas", "Una verificación con patrón", "Correctiva significa que corrige una falla ya ocurrida."),
        ("abc", "En el laboratorio químico: ¿qué indica la etiqueta de «fuera de servicio»?", "Que el equipo no debe usarse", "Que el equipo está recién calibrado", "Que el equipo es nuevo", "La etiqueta evita que alguien use un equipo no confiable."),
        ("=", "{F} ¿Cuántos días faltan para la próxima mantención preventiva de la balanza?", "90-60", "Se resta lo transcurrido al intervalo.", " días"),
        ("=", "{F} ¿Cuál es el costo anual de las mantenciones preventivas?", "40000*4", "Se multiplica el costo de cada visita por las visitas del año.", " pesos"),
        ("=", "{F} ¿Cuál es el costo de las 2 mantenciones correctivas del año?", "150000*2", "Se multiplica el costo de cada visita por las visitas.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuestan las correctivas del año que las preventivas?", "150000*2-40000*4", "Se resta el costo de las preventivas al de las correctivas.", " pesos"),
        ("abc", "{F} ¿Podría la balanza B-5 medir 700 g?", "No, porque 700 g está fuera de su rango de 0 a 600 g", "Sí, porque su resolución es 1 g", "Sí, si se calibra antes", "Fuera del rango el instrumento no mide bien."),
        ("abc", "{F} ¿Qué tipo de comprobación hace el usuario con un patrón antes de usar la balanza?", "Una verificación", "Una calibración", "Una mantención correctiva", "La verificación es rápida y la puede hacer el usuario según el método."),
        ("abc", "{F} ¿Quién realiza la mantención preventiva de la balanza?", "Un técnico autorizado", "El usuario que la usa", "El cliente", "La hoja de vida indica que la hace un técnico autorizado."),
        ("abc", "{F} Una persona quita la etiqueta de «fuera de servicio» para usar la balanza «solo hoy». ¿Qué corresponde?", "Corregirla: solo un técnico autorizado la retira tras revisar el equipo", "Aceptarlo si el equipo parece funcionar", "Aceptarlo si lo anota", "La etiqueta protege contra el uso de un equipo no confiable."),
        ("abc", "{F} ¿Por qué conviene la mantención preventiva?", "Porque evita fallas y suele costar menos que las reparaciones", "Porque reemplaza la calibración", "Porque elimina la bitácora", "La prevención reduce fallas y costos."),
        em("Lees la hoja de vida de un equipo de ejemplo cuando alguien avisa que un equipo de la sala echa chispas y que huele a quemado.", 1),
    ],
    ctx=("abc", "Una compañera de ejemplo dice: «No anotes en la bitácora que la balanza marcó raro, ya la apagué y listo». ¿Qué respondes?", "Que debe anotarse la novedad y avisarse al técnico, para que se revise el equipo", "Que no hace falta si está apagada", "Que se anota solo si se repite", "La bitácora conserva las novedades para el técnico."),
    sc=[
        ("En el laboratorio químico: ¿qué es la bitácora de un equipo?", "El registro diario de uso, verificaciones y novedades", "Sirve para seguir lo ocurrido con el equipo."),
        ("En el laboratorio químico: ¿qué diferencia hay entre verificar y calibrar?", "Verificar es una comprobación rápida; calibrar es más completa y la hace un técnico", "La calibración es más completa y deja un certificado."),
        ("¿Quién retira la etiqueta de fuera de servicio?", "El técnico autorizado tras revisar el equipo", "Evita que se use un equipo no confiable."),
    ],
    op=("Hoja de vida ficticia de un pHmetro del «Laboratorio Demo Costa Norte»: mantención preventiva cada 60 días, última hace 45; costo de $25.000 por visita preventiva, 6 visitas al año; una reparación correctiva de $120.000 en el año. Escribe (a) cuántos días faltan para la próxima preventiva, (b) el costo anual de las preventivas, (c) cuánto más cuesta la correctiva que una preventiva, (d) qué se anota en la bitácora si el pHmetro marca raro.",
        "(a) 60 menos 45 son 15 días. (b) 25.000 por 6 son 150.000 pesos. (c) 120.000 menos 25.000 son 95.000 pesos. (d) La novedad, con fecha y firma, y se avisa al técnico.",
        ["calcula los días", "calcula el costo anual", "compara costos", "indica el registro en bitácora"],
        ["hoja con las cuatro respuestas"],
        ["restar al revés", "no multiplicar por las visitas", "no anotar la novedad"],
        "Pregunta: «¿qué se registra y quién lo revisa?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa la hoja de vida de un equipo con intervalo, costos y mantenciones, y calcula el costo anual.",
    extend="Explica con un ejemplo por qué una mantención preventiva puede ahorrar dinero.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado). Bitácora de verificación diaria de la balanza B-5 del «Laboratorio Demo Valle Claro» con un patrón de 100 g (de ejemplo). Tolerancia de ±2 g. "
     "Lunes: marcó 100 g. Martes: 101 g. Miércoles: 100 g. Jueves: 103 g. Viernes: 100 g, sin registro de ninguna intervención del técnico entre el jueves y el viernes. "
     "Reglas de ejemplo: si la verificación queda fuera de tolerancia, se pone la etiqueta de fuera de servicio, se anota en la bitácora y se avisa al técnico autorizado.")
build(
    O5, 3, F,
    use="Aprenderé a analizar una bitácora de verificación: calcular errores, decidir cuándo un equipo queda fuera de servicio y qué se registra e informa, sin intervenir el equipo.",
    prior=["Sé qué es una verificación con patrón.", "Sé calcular el error de un instrumento.", "Sé qué es una tolerancia."],
    explain=[
        "En el laboratorio químico, la bitácora de verificación anota cada día cuánto marcó el equipo frente al patrón. El error del día es la diferencia entre la lectura y el valor del patrón. Si el error supera la tolerancia, el equipo queda fuera de servicio, se pone la etiqueta, se anota en la bitácora y se avisa al técnico autorizado; el usuario no lo ajusta.",
        "Una verificación que vuelve a dar bien sin que nadie haya intervenido el equipo no basta para volver a usarlo: una desviación puede reaparecer. Se necesita el registro de la revisión del técnico autorizado, con fecha y firma. Un dato bueno después de uno malo, sin explicación, es una razón para desconfiar y no para seguir usando el equipo.",
        f"Es un análisis en papel; no enseña a ajustar equipos. {EMER} {AVISO}",
    ],
    vocab=[("verificación diaria", "comprobación diaria del equipo con un patrón"), ("error del día", "lectura menos valor del patrón"), ("fuera de tolerancia", "con error mayor que la tolerancia"), ("revisión del técnico", "intervención registrada que permite volver a usar el equipo"), ("desviación", "alejamiento de la lectura respecto del patrón")],
    worked=[
        ("Error del día", "Un equipo de ejemplo con patrón de 50 g marca 52 g y la tolerancia es ±3 g. ¿Cuál es el error y cumple?", ["El error es 52 menos 50, es decir, 2 g.", "2 g es menor que 3 g: cumple."], "Error de 2 g; cumple"),
        ("Fuera de tolerancia", "Con patrón de 50 g y tolerancia de ±3 g, el equipo marca 55 g. ¿Qué corresponde?", ["El error de 5 g supera los 3 g.", "Queda fuera de servicio y se avisa al técnico."], "Fuera de servicio y aviso al técnico"),
    ],
    mistakes=[("Volver a usar el equipo apenas una verificación posterior da bien.", "Sin revisión del técnico, la desviación puede reaparecer.", "Espera el registro de la revisión del técnico autorizado."),
              ("Ajustar el equipo por cuenta propia hasta que marque el patrón.", "Ajustar es tarea del técnico autorizado.", "Pon la etiqueta de fuera de servicio y avisa.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es el error del día en una verificación?", "La diferencia entre la lectura y el valor del patrón", "El costo de la verificación", "La fecha de la calibración", "El error mide cuánto se aleja el equipo del patrón."),
        ("abc", "En el laboratorio químico: ¿qué significa estar fuera de tolerancia?", "Que el error es mayor que la tolerancia", "Que el equipo es nuevo", "Que el patrón pesa 100 g", "Fuera de tolerancia es un error mayor al aceptable."),
        ("abc", "En el laboratorio químico: ¿qué se hace con un equipo fuera de tolerancia?", "Se pone fuera de servicio, se anota y se avisa al técnico", "Se ajusta el equipo por cuenta propia", "Se sigue usando con cuidado", "Solo el técnico autorizado lo revisa."),
        ("=", "{F} ¿Cuál fue el error del jueves?", "103-100", "Se resta el valor del patrón a la lectura.", " g"),
        ("=", "{F} ¿Cuál fue el error del martes?", "101-100", "Se resta el valor del patrón a la lectura.", " g"),
        ("abc", "{F} ¿Qué día quedó la balanza fuera de tolerancia?", "El jueves", "El martes", "El miércoles", "El error de 3 g del jueves supera los 2 g."),
        ("abc", "{F} ¿Qué corresponde hacer el jueves?", "Poner la etiqueta de fuera de servicio, anotar en la bitácora y avisar al técnico", "Ajustar la balanza hasta que marque 100 g", "Seguir usándola con cuidado", "Las reglas de la ficha lo indican."),
        ("=", "{F} ¿Cuántas de las 5 verificaciones estuvieron dentro de tolerancia?", "4", "Estuvieron dentro lunes, martes, miércoles y viernes.", " verificaciones"),
        ("abc", "{F} El viernes la balanza marcó 100 g. ¿Se puede volver a usar?", "No, porque falta el registro de la revisión del técnico autorizado", "Sí, porque marcó el patrón", "Sí, si se anota la lectura", "Sin intervención registrada, la desviación puede reaparecer."),
        ("abc", "{F} Un usuario dice: «ya marcó 100 g, quitemos la etiqueta». ¿Qué corresponde?", "No quitarla: solo el técnico autorizado la retira tras revisar y registrar", "Quitarla porque ya marca bien", "Quitarla si la balanza está limpia", "La etiqueta se retira con la revisión del técnico."),
        ("=", "{F} ¿Cuál es el error máximo aceptable según la tolerancia?", "2", "La ficha fija una tolerancia de ±2 g.", " g"),
        ("abc", "{F} Otro usuario propone «corregir» la balanza girando algo en su interior hasta que marque 100 g. ¿Qué corresponde?", "Rechazarlo: ajustar la balanza es tarea del técnico autorizado", "Aceptarlo si lo hace con cuidado", "Aceptarlo si la balanza está apagada", "Intervenir un equipo sin autorización es peligroso y no vale como ajuste."),
        em("Lees la bitácora de ejemplo en la oficina cuando alguien avisa que se rompió el vidrio de una balanza y que hay un olor fuerte y humo.", 2),
    ],
    ctx=("abc", "Una supervisora de ejemplo dice: «Anota que el jueves marcó 100 g, así no tenemos que parar la balanza». ¿Qué respondes?", "Que no: se anota lo realmente medido y se avisa al técnico", "Que sí, si se corrige después", "Que sí, porque el viernes ya marcó bien", "Cambiar un dato oculta una falla y vuelve inseguro el equipo."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula el error de la verificación?", "Lectura menos valor del patrón", "Mide cuánto se aleja el equipo del patrón."),
        ("En el laboratorio químico: ¿quién ajusta un equipo fuera de tolerancia?", "El técnico autorizado", "El usuario solo registra y avisa."),
        ("¿Basta una verificación buena para volver a usar un equipo reparado?", "No, falta el registro de la revisión del técnico", "Sin revisión registrada, la desviación podría reaparecer."),
    ],
    op=("Bitácora ficticia del «Laboratorio Demo Costa Norte»: patrón de 50 g y tolerancia de ±1 g; lunes: 50 g; martes: 51 g; miércoles: 53 g; jueves: 50 g sin intervención registrada. Escribe (a) el error de cada día, (b) qué día queda fuera de tolerancia, (c) qué debe hacerse ese día, (d) por qué no se vuelve a usar el jueves aunque marque 50 g.",
        "(a) 0, 1, 3 y 0 g. (b) El miércoles. (c) Poner la etiqueta de fuera de servicio, anotar en la bitácora y avisar al técnico autorizado. (d) Porque falta la revisión registrada del técnico: la desviación podría reaparecer.",
        ["calcula los errores", "identifica el día fuera de tolerancia", "indica la conducta", "justifica no reutilizar"],
        ["hoja con las cuatro respuestas"],
        ["usar el equipo porque marcó bien", "ajustar por cuenta propia", "borrar el dato malo"],
        "Pregunta: «¿qué documento falta para volver a usarla?». Si no responde, pídele que relea el segundo párrafo de la explicación."),
    reinforce="Inventa cinco verificaciones con un patrón y una tolerancia, y decide qué día queda fuera de servicio.",
    extend="Explica con un ejemplo por qué un equipo que «solo a veces» falla es más peligroso que uno que falla siempre.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (planilla de ejemplo, inventada) del «Laboratorio Demo Valle Claro». Datos de planilla de ejemplo: balanza B-5: patrón de 200 g, lectura de 204 g, tolerancia de ejemplo de ±2 % del patrón. Balanza B-6: patrón de 50 g, lectura de 52 g, tolerancia de ±2 % del patrón. "
     "Fórmula de ejemplo: error relativo (%) = error absoluto × 100 ÷ valor del patrón. Horas programadas de uso de un equipo en el mes: 200; horas en que estuvo disponible: 160. "
     "Plan A: 1 mantención preventiva de $40.000 cada 3 meses (4 al año). Plan B: solo reparar cuando falle, con 2 reparaciones al año de $150.000 cada una.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar criterios con datos de ejemplo: error relativo, comparación con una tolerancia en porcentaje, disponibilidad del equipo y costo anual de dos planes de mantención.",
    prior=["Sé calcular el error de un instrumento.", "Sé calcular porcentajes.", "Sé qué es una mantención preventiva y una correctiva."],
    explain=[
        "En el laboratorio químico, el error absoluto es la diferencia entre la lectura y el patrón; el error relativo expresa ese error como porcentaje del patrón: error absoluto por 100 entre el valor del patrón. Sirve para comparar equipos con distinto tamaño de patrón. Si el error relativo es menor o igual que la tolerancia en porcentaje, el equipo cumple.",
        "La disponibilidad de un equipo es el porcentaje de las horas programadas en que estuvo listo para usarse: horas disponibles por 100 entre horas programadas. Para comparar dos planes de mantención se calcula el costo anual de cada uno, multiplicando el costo de cada visita por el número de visitas; luego se considera también el riesgo de fallas inesperadas, que no se ve solo en el precio.",
        f"Los cálculos son de planilla y orientan a quien decide; el técnico autorizado es quien interviene los equipos. {EMER} {AVISO}",
    ],
    vocab=[("error relativo", "error absoluto como porcentaje del valor del patrón"), ("disponibilidad", "porcentaje de las horas programadas en que el equipo estuvo listo"), ("horas programadas", "horas en que se planificó usar el equipo"), ("costo anual", "costo por visita multiplicado por las visitas del año"), ("falla inesperada", "falla que detiene el equipo sin aviso")],
    worked=[
        ("Error relativo", "Un instrumento de ejemplo con patrón de 100 g marca 104 g. ¿Cuál es el error relativo?", ["El error absoluto es 4 g.", "4 por 100 entre 100 son 4 %."], "4 %"),
        ("Disponibilidad", "Un equipo de ejemplo tuvo 150 horas disponibles de 200 programadas. ¿Qué disponibilidad tuvo?", ["Se divide 150 entre 200 y se multiplica por 100.", "150 por 100 son 15.000, y 15.000 entre 200 son 75."], "75 %"),
    ],
    mistakes=[("Comparar solo el error absoluto de dos balanzas con patrones distintos.", "Un error de 4 g es grande en un patrón de 50 g y pequeño en uno de 500 g.", "Usa el error relativo para comparar."),
              ("Elegir el plan más barato sin pensar en las fallas inesperadas.", "Una falla puede detener el laboratorio y costar más que la prevención.", "Compara también la disponibilidad y el riesgo.")],
    T=[
        ("abc", "En el laboratorio químico: ¿qué es el error relativo?", "El error absoluto expresado como porcentaje del valor del patrón", "La diferencia entre dos patrones", "El costo del instrumento", "Permite comparar errores en patrones de distinto tamaño."),
        ("abc", "En el laboratorio químico: ¿qué es la disponibilidad de un equipo?", "El porcentaje de las horas programadas en que estuvo listo", "El precio del equipo", "El número de usuarios", "Mide qué parte del tiempo planificado se pudo usar."),
        ("abc", "En el laboratorio químico: ¿por qué un plan solo correctivo puede ser más riesgoso?", "Porque las fallas llegan sin aviso y pueden detener el trabajo", "Porque la reparación es gratis", "Porque no requiere técnico", "La prevención reduce las fallas inesperadas y sus costos."),
        ("=", "{F} ¿Cuál es el error absoluto de la balanza B-5?", "204-200", "Se resta el patrón a la lectura.", " g"),
        ("=", "{F} ¿Cuál es el error relativo de la balanza B-5?", "(204-200)*100//200", "Se divide el error absoluto entre el patrón y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuál es el error relativo de la balanza B-6?", "(52-50)*100//50", "Se divide el error absoluto entre el patrón y se multiplica por 100.", " %"),
        ("abc", "{F} Con tolerancia de ±2 %, ¿qué balanza cumple?", "La B-5, porque su error relativo es 2 %", "La B-6, porque su error absoluto es solo 2 g", "Ambas, porque las dos marcan más que el patrón", "El 2 % de la B-5 está dentro de la tolerancia; el 4 % de la B-6 no."),
        ("abc", "{F} ¿Por qué se compara el error relativo y no solo el absoluto?", "Porque los patrones son de tamaños distintos", "Porque el absoluto siempre da cero", "Porque el relativo es siempre menor", "Un mismo error absoluto pesa distinto con patrones distintos."),
        ("=", "{F} ¿Qué disponibilidad tuvo el equipo en el mes?", "160*100//200", "Se divide las horas disponibles entre las programadas y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas horas programadas no estuvo disponible el equipo?", "200-160", "Se resta las horas disponibles a las programadas.", " horas"),
        ("=", "{F} ¿Cuál es el costo anual del plan A?", "40000*4", "Se multiplica el costo de cada visita por las visitas del año.", " pesos"),
        ("=", "{F} ¿Cuál es el costo anual del plan B?", "150000*2", "Se multiplica el costo de cada reparación por las reparaciones del año.", " pesos"),
        em("Haces cálculos de mantención de ejemplo en la oficina cuando alguien avisa que un equipo de la sala hace un ruido anormal y que sale humo.", 3),
    ],
    ctx=("abc", "Una jefatura de ejemplo dice: «Elijamos el plan B, el de solo reparar, porque siempre sale más barato». ¿Qué respondes?", "Que con estos datos el plan A cuesta 160.000 pesos al año frente a 300.000 del plan B, y además previene fallas", "Que tiene razón, porque así no se paga mantención preventiva", "Que da lo mismo, porque ambos cuestan igual", "Los cálculos muestran que el plan A es más barato y más seguro."),
    sc=[
        ("En el laboratorio químico: ¿cómo se calcula el error relativo?", "Error absoluto por 100 entre el patrón", "Se expresa como porcentaje del patrón."),
        ("En el laboratorio químico: ¿cómo se calcula la disponibilidad?", "Horas disponibles por 100 entre programadas", "Es un porcentaje del tiempo planificado."),
        ("¿Cómo se calcula el costo anual de un plan?", "Costo por visita por número de visitas", "Se multiplica el costo unitario por la frecuencia."),
    ],
    op=("Planilla ficticia del «Laboratorio Demo Costa Norte»: balanza M: patrón de 100 g, lectura de 102 g; balanza N: patrón de 25 g, lectura de 26 g; tolerancia de ±2 %. Un equipo: 120 horas disponibles de 150 programadas. Plan 1: 3 preventivas de $30.000 al año. Plan 2: 1 reparación de $200.000 al año. Escribe (a) el error relativo de M y de N, (b) cuál cumple la tolerancia, (c) la disponibilidad del equipo, (d) el costo anual de cada plan.",
        "(a) M: 2 por 100 entre 100 son 2 %; N: 1 por 100 entre 25 son 4 %. (b) Solo M cumple. (c) 120 por 100 entre 150 son 80 %. (d) Plan 1: 90.000 pesos; plan 2: 200.000 pesos.",
        ["calcula los errores relativos", "aplica la tolerancia", "calcula la disponibilidad", "calcula los costos anuales"],
        ["hoja con las cuatro respuestas"],
        ["comparar solo errores absolutos", "dividir al revés", "olvidar multiplicar por las visitas"],
        "Pregunta: «¿respecto de qué valor se divide el error?». Si no responde, pídele que relea el primer párrafo de la explicación."),
    reinforce="Inventa dos balanzas con patrón y lectura, calcula el error relativo y decide si cumplen una tolerancia en porcentaje.",
    extend="Explica con un ejemplo por qué un plan barato puede salir caro si el equipo se detiene.",
)
