"""Dibujo Técnico TP 3.º y 4.º medio: OAE-05 (piezas mecánicas) y OAE-06 (planos de montaje y estructurales). Solo lectura de planos y conceptos; datos de ejemplo; sin software."""
from __future__ import annotations

from tp_dite_common import build

O5 = "TP-DITE-3y4-OAE-05"
O6 = "TP-DITE-3y4-OAE-06"

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (pedido de ejemplo, inventado). El taller «Mecánica Andes» pide el plano de fabricación de una escuadra de soporte, una pieza metálica plana en forma de L para fijar un estante. "
     "Medidas: lado largo 120 mm; lado corto 80 mm; ancho 30 mm; espesor 4 mm; 2 agujeros de 8 mm de diámetro. Material: acero (de ejemplo). Cantidad: 50 piezas. "
     "Costo de material de ejemplo: $350 por pieza. El pedido no indica la posición de los agujeros. El taller fabricará la pieza con sus máquinas; el dibujante entrega solo el plano.")
build(
    O5, 1, F,
    use="Aprenderé qué debe contener el plano de una pieza mecánica para que otra persona pueda fabricarla, y qué cuidados de seguridad y de propiedad intelectual se aplican.",
    prior=["Sé qué es una cota y una escala.", "Sé qué es un plano de fabricación en términos generales.", "Sé multiplicar cantidades y costos."],
    explain=[
        "Una pieza mecánica es un elemento de una máquina o herramienta, como un eje, una escuadra o una placa. El plano de fabricación debe contener todo lo necesario para que otra persona la haga sin tener que adivinar: la forma en vistas, todas las medidas con su unidad, el material, la cantidad, el acabado de las superficies y las tolerancias, que son las diferencias de medida aceptables. Si falta un dato, se pide al mandante; no se inventa.",
        "Dibujar en forma digital significa hacerlo en un computador, con ventajas como la precisión y las copias exactas, pero la responsabilidad por los datos sigue siendo de quien dibuja. El dibujante no opera las máquinas del taller: operarlas exige capacitación, autorización y elementos de protección. Esto es aprendizaje conceptual en papel y no te habilita para trabajar en un taller.",
        "El diseño de una pieza puede estar protegido por derechos de propiedad intelectual o industrial. No se copia ni se reproduce la pieza de otra empresa sin su autorización. Por último, quien dibuja muchas horas debe cuidar su postura, mantener la pantalla a la altura de los ojos y hacer pausas breves.",
    ],
    vocab=[("pieza mecánica", "elemento de una máquina o herramienta"), ("plano de fabricación", "plano con todo lo necesario para fabricar una pieza"), ("tolerancia", "diferencia de medida aceptable"), ("acabado", "estado de la superficie de la pieza"), ("mandante", "persona o empresa que encarga el trabajo"), ("propiedad industrial", "derecho sobre un diseño o invento")],
    worked=[
        ("Contar elementos", "Un pedido de ejemplo es de 30 placas con 4 agujeros cada una. ¿Cuántos agujeros hay en total?", ["Se multiplican las placas por los agujeros de cada una.", "30 × 4 = 120 agujeros."], "120 agujeros"),
        ("Detectar un dato faltante", "El pedido de ejemplo de una placa dice: «largo 100 mm, ancho 50 mm, 2 agujeros, cantidad 10». ¿Qué datos de fabricación faltan?", ["No se indica el espesor ni el material.", "Tampoco aparece la posición de los agujeros: son tres datos."], "Espesor, material y posición de los agujeros"),
    ],
    mistakes=[("Suponer que el material es «el que se usa siempre» porque el pedido no lo dice.", "El material cambia el costo, la resistencia y el proceso; el taller no puede adivinar.", "Pide el dato al mandante antes de cerrar el plano."),
              ("Pensar que el dibujante puede usar una máquina del taller para «probar» su dibujo.", "Operar maquinaria exige capacitación y autorización; el dibujante entrega el plano.", "Entrega el plano y deja la fabricación al personal autorizado.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué debe permitir un plano de fabricación?", "Que otra persona fabrique la pieza sin tener que adivinar datos", "Que la pieza quede más bonita", "Que el taller no necesite comunicarse nunca más", "Un buen plano contiene todos los datos; no se espera que el taller adivine."),
        ("abc", "¿Quién opera las máquinas de un taller?", "Personal capacitado y autorizado", "Cualquier persona que haya visto el plano", "El dibujante, para comprobar su dibujo", "La capacitación y la autorización son necesarias por el riesgo de la maquinaria."),
        ("abc", "En Dibujo Técnico: ¿qué es la tolerancia?", "La diferencia de medida que se acepta en la pieza", "El material de la pieza", "El color del plano", "La tolerancia fija entre qué valores la medida es aceptable."),
        ("=", "{F} ¿Cuántos agujeros se deben hacer en total en las 50 piezas?", "50*2", "Se multiplican las piezas por los agujeros de cada una.", " agujeros"),
        ("=", "{F} ¿Cuántos pesos cuesta el material de las 50 piezas?", "50*350", "Se multiplica la cantidad por el costo de cada pieza.", " pesos"),
        ("abc", "{F} ¿Qué dato necesario para fabricar no trae el pedido?", "La posición de los agujeros", "El material", "La cantidad", "El pedido indica material y cantidad, pero no dónde van los agujeros."),
        ("=", "{F} Se apilan 6 escuadras una sobre otra, apoyadas por su espesor. ¿Cuántos milímetros mide la pila?", "6*4", "Se multiplica el espesor de cada pieza por la cantidad.", " mm"),
        ("ab", "Un cliente trae una pieza con la marca de otra empresa y pide un plano para copiarla exactamente. ¿Qué corresponde?", "Consultar si el diseño está protegido y si hay autorización antes de copiarlo", "Copiarla, porque la pieza está a la vista", "Que una pieza se pueda ver no autoriza a copiarla si su diseño está protegido."),
        ("abc", "{F} El taller te ofrece «probar» el plano con una de sus máquinas. ¿Qué haces?", "Agradezco, pero la operación es del personal capacitado; yo entrego el plano", "Acepto, porque es solo una prueba", "Acepto si me pongo guantes", "Operar maquinaria exige capacitación y autorización, y no es parte del rol del dibujante."),
        ("abc", "{F} Calculas que un lado mide 120 mm, pero el pedido dice «12 cm de lado largo». ¿Qué conclusión sacas?", "Es la misma medida expresada en otra unidad", "Hay una contradicción grave", "El pedido tiene un error de 108 mm", "12 cm son 120 mm, por lo que ambas medidas coinciden."),
        ("abc", "{F} El mandante dice por teléfono «cámbiale el espesor a 5 mm». ¿Qué haces?", "Pido confirmar el cambio por escrito y registro una nueva revisión", "Cambio el espesor sin anotar nada", "Ignoro el cambio hasta que se fabrique", "Un cambio se confirma por escrito y se registra, porque afecta el costo y la fabricación."),
        ("=", "{F} Si el espesor cambiara a 5 mm, ¿cuántos mm mediría una pila de 6 escuadras?", "6*5", "Se multiplica el nuevo espesor por la cantidad.", " mm"),
        ("abc", "{F} El taller necesita agregar al plano el acabado. ¿Qué es el acabado?", "El estado de la superficie de la pieza", "El número de agujeros", "El nombre del taller", "El acabado describe cómo debe quedar la superficie."),
    ],
    ctx=("abc", "Un diseñador de otra empresa te muestra su plano de una pieza «para que veas cómo se hace». Más tarde, un cliente te pide algo similar. ¿Qué corresponde?", "Diseñar la pieza con los datos del cliente y sin copiar el plano ajeno", "Copiar el plano que viste, cambiando el rótulo", "Pedirle al cliente que copie la pieza él mismo", "Copiar un plano ajeno vulnera la propiedad intelectual aunque cambie el rótulo."),
    sc=[
        ("En Dibujo Técnico: ¿qué es un plano de fabricación?", "Un plano con todo lo necesario para fabricar una pieza", "Debe incluir forma, medidas, material y cantidad."),
        ("¿Qué haces si falta el material en el pedido?", "Se lo pido al mandante antes de cerrar el plano", "Un dato faltante no se inventa."),
        ("¿Quién opera las máquinas del taller?", "Personal capacitado y autorizado", "Operarlas exige capacitación, autorización y elementos de protección."),
    ],
    op=("Un taller de ejemplo pide 40 placas de aluminio de 90 mm por 60 mm, con 3 agujeros de 6 mm de diámetro, espesor de 3 mm. El pedido no indica el acabado ni la posición de los agujeros. Calcula el total de agujeros, el espesor de una pila de 8 placas y escribe qué dos datos pedirías y por qué no los inventarías.",
        "Agujeros: 40 × 3 = 120. Pila de 8 placas: 8 × 3 = 24 mm. Pediría el acabado y la posición de los agujeros, porque si los invento puede fabricarse una pieza que no sirva y el costo lo asumiría el taller.",
        ["calcula los agujeros y la pila", "identifica los dos datos faltantes", "justifica por qué no inventarlos"],
        ["hoja con cálculos y dos frases"],
        ["inventar el acabado", "multiplicar mal los agujeros", "no justificar la consulta"],
        "Pregunta: «¿qué pasa si el taller hace las placas con agujeros en otro lugar?». Si no responde, repasa por qué el plano debe ser completo."),
    reinforce="Elige un objeto metálico simple de tu casa, anota tres datos que un taller necesitaría para fabricarlo y uno que no podrías saber sin preguntar.",
    extend="Explica con un ejemplo inventado por qué copiar el plano de otra empresa puede causar un problema.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (pieza de ejemplo). Un buje es un cilindro hueco, como un tubo corto: diámetro exterior 40 mm, diámetro interior 20 mm y alto 30 mm. "
     "Vista frontal (mirando desde un lado): un rectángulo de 40 mm de ancho por 30 mm de alto con dos líneas discontinuas verticales que muestran el hueco interior. "
     "Vista superior (mirando desde arriba): dos círculos concéntricos, es decir, con el mismo centro. Acotado: diámetros con el símbolo Ø; alto en la vista frontal. Material: bronce (de ejemplo).")
build(
    O5, 2, F,
    use="Aprenderé a leer las vistas de una pieza, a acotar con orden y a reconocer los datos de un plano de fabricación.",
    prior=["Sé qué son líneas continuas y discontinuas.", "Sé qué es una cota.", "Sé qué es un diámetro."],
    explain=[
        "Una pieza se representa con vistas ortogonales: dibujos de la pieza vista de frente, desde arriba y desde un lado, cada uno perpendicular a la mirada. Las vistas se eligen para mostrar la forma con la menor cantidad de dibujos. Si algo no se ve desde una vista, se dibuja con línea discontinua, que representa un contorno oculto. La disposición de las vistas en la hoja la fija el método de proyección que indique la norma de dibujo vigente.",
        "El acotado debe ser completo y ordenado: cada medida aparece una sola vez, con su unidad, en la vista donde se lee mejor, sin cotas repetidas. Los diámetros se acotan con el símbolo Ø antes del número. El espesor de la pared de un tubo se obtiene restando el diámetro interior al exterior y dividiendo por dos.",
        "El plano de fabricación incluye un rótulo con el nombre de la pieza, el material, la escala, la revisión y la cantidad, y a veces una lista de piezas si el plano muestra un conjunto. Se verifica que las vistas sean coherentes: las medidas que aparecen en dos vistas deben coincidir.",
    ],
    vocab=[("vista ortogonal", "dibujo de la pieza visto de frente, desde arriba o de lado"), ("contorno oculto", "borde que no se ve desde esa vista"), ("concéntricos", "con el mismo centro"), ("Ø", "símbolo que indica diámetro"), ("lista de piezas", "tabla de piezas de un conjunto"), ("espesor de pared", "grosor del material de un tubo")],
    worked=[
        ("Calcular el espesor de pared", "Un tubo corto de ejemplo tiene diámetro exterior 50 mm y diámetro interior 30 mm. ¿Cuál es el espesor de la pared?", ["Se restan los diámetros: 50 − 30 = 20 mm.", "Se divide por dos, porque hay pared a ambos lados: 10 mm."], "10 mm"),
        ("Elegir la vista", "Para mostrar que una pieza de ejemplo tiene forma circular, ¿qué vista usas?", ["El círculo se ve cuando se mira de frente a la base.", "En un cilindro vertical, esa mirada es desde arriba: vista superior."], "La vista superior"),
    ],
    mistakes=[("Dibujar el hueco interior del buje con línea continua en la vista frontal.", "No se ve desde esa vista: debe ir con línea discontinua.", "Usa discontinua para todo lo oculto."),
              ("Acotar el mismo diámetro en la vista frontal y en la superior.", "Una medida repetida puede contradecirse si se corrige solo una vez.", "Acota cada medida una vez, donde se lea mejor.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es una vista ortogonal?", "Un dibujo de la pieza visto de frente, desde arriba o de lado", "Un dibujo en perspectiva con sombras", "Un esquema de la ruta de fabricación", "Las vistas ortogonales muestran la pieza desde direcciones perpendiculares."),
        ("abc", "¿Qué indica el símbolo Ø antes de un número?", "Que la cota es un diámetro", "Que la cota es un radio", "Que la cota está en pulgadas", "Ø se usa para indicar diámetros."),
        ("abc", "¿Cómo se dibuja un contorno que no se ve desde la vista?", "Con línea discontinua", "Con línea continua gruesa", "No se dibuja", "Lo oculto se representa con línea discontinua."),
        ("=", "{F} ¿Cuál es el espesor de pared del buje?", "(40-20)//2", "Se resta el diámetro interior al exterior y se divide por dos.", " mm"),
        ("abc", "{F} ¿Qué vista muestra los dos círculos concéntricos?", "La vista superior", "La vista frontal", "Ninguna de las dos", "Los círculos se ven al mirar desde arriba la base del cilindro."),
        ("abc", "{F} En la vista frontal, ¿qué muestran las dos líneas discontinuas verticales?", "El hueco interior, que no se ve desde esa vista", "Un eje de simetría", "El contorno exterior de la pieza", "Las discontinuas representan lo oculto: el hueco interior."),
        ("=", "{F} ¿Cuántos milímetros mide el alto del buje si se apilan 4 bujes?", "4*30", "El alto de la pila es el alto de cada buje por la cantidad.", " mm"),
        ("abc", "{F} ¿Qué medidas necesita la vista frontal para quedar acotada?", "El diámetro exterior (40) y el alto (30), más el diámetro interior (20)", "Solo el alto (30)", "Solo el diámetro interior (20)", "El acotado completo incluye diámetro exterior, interior y alto, cada uno una vez."),
        ("abc", "{F} Un dibujante acota el diámetro exterior en las dos vistas, como 40 en una y 42 en la otra. ¿Qué haces como revisor?", "Registro la contradicción y consulto cuál valor es el correcto", "Dejo ambas cotas", "Uso 41, que está en el medio", "Dos cotas distintas para la misma medida son un error que se consulta."),
        ("ab", "Para fabricar el buje, el material figura en el rótulo. ¿Cuál es el material de la ficha?", "Bronce, de ejemplo", "Acero, de ejemplo", "La ficha indica bronce como material de ejemplo."),
        ("=", "{F} ¿Cuántos mm mide la distancia entre la pared exterior y la interior a cada lado (espesor de pared) si el diámetro exterior fuera 60 mm y el interior 36 mm?", "(60-36)//2", "Se restan los diámetros y se divide por dos.", " mm"),
        ("abc", "{F} Se agrega una pared más gruesa con 8 mm de pared, manteniendo el diámetro exterior de 40 mm. ¿Cuál sería el diámetro interior?", "24 mm", "32 mm", "16 mm", "Con 8 mm de pared a cada lado, el interior es 40 − 16 = 24 mm."),
        ("abc", "{F} Una compañera dice: «con una sola vista, la frontal, basta, porque ya se ve el alto». ¿Qué le falta?", "No se ve que la base es circular; se necesita la vista superior o una indicación del símbolo Ø", "Nada, la frontal siempre basta", "Falta solo el rótulo", "Un rectángulo podría ser un prisma; la vista superior o el símbolo Ø aclara que es un cilindro."),
    ],
    ctx=("abc", "El taller te pregunta si el buje de 40 mm tiene el hueco pasante (de lado a lado). La vista frontal muestra las líneas discontinuas de arriba a abajo. ¿Qué respondes?", "Sí: las líneas discontinuas recorren todo el alto, así que el hueco es pasante", "No: las líneas discontinuas indican un borde exterior", "No se puede saber con vistas ortogonales", "Las discontinuas completas indican que el hueco atraviesa la pieza."),
    sc=[
        ("En Dibujo Técnico: ¿para qué sirve la vista superior?", "Para mostrar la pieza vista desde arriba", "Allí se ven, por ejemplo, círculos de una base."),
        ("¿Cómo se calcula el espesor de pared de un tubo?", "Diámetro exterior menos interior, dividido por dos", "Hay pared a ambos lados del hueco."),
        ("¿Cuántas veces se acota cada medida?", "Una sola vez, donde mejor se lea", "Repetirla puede producir contradicciones si se corrige solo una vez."),
    ],
    op=("Un casquillo de ejemplo es un cilindro hueco de 50 mm de diámetro exterior, 30 mm de diámetro interior y 25 mm de alto, de bronce. Describe por escrito qué se vería en la vista frontal y en la superior, cuántas cotas necesita, calcula el espesor de pared y escribe qué línea usarías para el hueco en la vista frontal.",
        "Vista frontal: un rectángulo de 50 mm por 25 mm con dos líneas discontinuas verticales para el hueco. Vista superior: dos círculos concéntricos. Cotas: Ø50, Ø30 y 25. Espesor de pared: (50 − 30) ÷ 2 = 10 mm. El hueco se dibuja con línea discontinua.",
        ["describe correctamente las dos vistas", "indica las tres cotas necesarias", "calcula el espesor de pared"],
        ["hoja con descripción de vistas y cálculo"],
        ["usar línea continua para el hueco", "repetir cotas", "no dividir por dos"],
        "Pregunta: «¿qué ves en la vista superior?». Si no responde, repasa las vistas de un cilindro."),
    reinforce="Elige un vaso o un tarro y describe sus vistas frontal y superior en dos frases.",
    extend="Explica con un ejemplo inventado por qué las líneas discontinuas ayudan a quien fabrica una pieza.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (placa de ejemplo). Placa rectangular de 120 mm de largo y 100 mm de ancho, con 4 agujeros de 10 mm de diámetro, uno en cada esquina, con el centro a 20 mm de cada borde. "
     "Cotas anotadas por el dibujante: largo 120; ancho 100; distancia entre centros horizontal 85; distancia entre centros vertical 60. "
     "En un rectángulo, la diagonal d cumple d × d = a × a + b × b, donde a y b son sus lados.")
build(
    O5, 3, F,
    use="Aprenderé a calcular y comprobar las cotas de una pieza con agujeros, y a detectar un error de acotado antes de fabricar.",
    prior=["Sé qué son los centros de un agujero.", "Sé sumar y restar cotas.", "Sé qué es un rectángulo."],
    explain=[
        "En una placa con agujeros se acota la posición de cada centro respecto de los bordes y las distancias entre centros. Las distancias entre centros no son independientes: se pueden calcular a partir de las otras cotas, y se comprueba que coincidan. Si una cota anotada no coincide con la calculada, hay un error de acotado y se corrige antes de fabricar.",
        "Para una placa con agujeros simétricos, la distancia entre centros en una dirección es la medida de la placa menos dos veces la distancia del centro al borde. Para la distancia diagonal entre dos centros opuestos se usa que el cuadrado de la diagonal es igual a la suma de los cuadrados de los lados. Por ejemplo, con lados 3 y 4, la diagonal es 5, porque 25 = 9 + 16.",
        "También se comprueba que los agujeros quepan: el borde del agujero no debe estar más cerca del borde de la placa que lo indicado en el proyecto. La distancia del borde del agujero al borde de la placa es la distancia del centro menos el radio, que es la mitad del diámetro. Todo cambio se registra con la revisión del plano.",
    ],
    vocab=[("acotado", "conjunto de cotas de un plano"), ("distancia entre centros", "separación entre los centros de dos agujeros"), ("diagonal", "línea que une dos esquinas opuestas"), ("radio", "mitad del diámetro"), ("simétrico", "igual a ambos lados de un eje")],
    worked=[
        ("Calcular distancia entre centros", "Una placa de ejemplo mide 150 mm de largo y sus agujeros tienen el centro a 25 mm de cada extremo. ¿Cuánto hay entre centros?", ["Se resta dos veces la distancia al borde.", "150 − 25 − 25 = 100 mm."], "100 mm"),
        ("Calcular una diagonal", "Los centros de dos agujeros opuestos están separados 60 mm en una dirección y 80 mm en la otra. ¿Cuál es la distancia diagonal entre ellos?", ["d × d = 60 × 60 + 80 × 80 = 3.600 + 6.400 = 10.000.", "Como 100 × 100 = 10.000, la diagonal es 100 mm."], "100 mm"),
    ],
    mistakes=[("Restar el radio del agujero a la distancia entre centros.", "La distancia entre centros se mide de centro a centro; el radio se usa para el borde.", "Usa el radio solo para calcular distancias de borde a borde."),
              ("Dejar dos cotas distintas para la misma distancia, sin consultar.", "Quien fabrique no sabrá cuál usar y puede hacer una pieza mal.", "Marca la contradicción y consulta antes de fabricar.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la distancia entre centros?", "La separación entre los centros de dos agujeros", "El diámetro de los agujeros", "El espesor de la placa", "Se mide de centro a centro."),
        ("abc", "¿Qué es el radio de un agujero?", "La mitad de su diámetro", "El doble de su diámetro", "Su profundidad", "El radio es la mitad del diámetro."),
        ("abc", "¿Qué haces si una cota anotada no coincide con la calculada?", "Registro el error y lo corrijo o consulto antes de fabricar", "Dejo la cota anotada porque estaba primero", "Ajusto el dibujo a ojo", "Un error de acotado se resuelve antes de fabricar."),
        ("=", "{F} ¿Cuál es la distancia horizontal entre centros que resulta de las otras cotas?", "120-20-20", "Al largo se le restan las dos distancias del centro al borde.", " mm"),
        ("=", "{F} ¿Cuál es la distancia vertical entre centros que resulta de las otras cotas?", "100-20-20", "Al ancho se le restan las dos distancias del centro al borde.", " mm"),
        ("abc", "{F} ¿Qué cota anotada es incorrecta?", "La distancia horizontal de 85 mm, que debería ser 80 mm", "La distancia vertical de 60 mm, que es correcta", "El largo de 120 mm", "La vertical sí cuadra con 100 − 40 = 60; la horizontal debería ser 80."),
        ("=", "{F} ¿Cuántos milímetros de diferencia hay entre la distancia horizontal anotada y la calculada?", "85-80", "Se resta el valor calculado al anotado.", " mm"),
        ("abc", "{F} Con las distancias corregidas de 80 mm y 60 mm entre centros, ¿cuánto mide la diagonal entre centros opuestos?", "100 mm, porque 100 × 100 es 10.000, igual a 6.400 más 3.600", "140 mm, porque 80 más 60 son 140", "70 mm, porque es el promedio de 80 y 60", "La diagonal cumple d × d = a × a + b × b; sumar o promediar los lados no da la diagonal."),
        ("abc", "{F} ¿A qué distancia queda el borde del agujero del borde de la placa?", "15 mm, porque 20 − 5 = 15", "20 mm", "25 mm", "Al centro a 20 mm se le resta el radio de 5 mm."),
        ("abc", "{F} Un proyecto exige que el borde del agujero esté al menos a 12 mm del borde de la placa. ¿Se cumple?", "Sí: 15 mm es mayor que 12 mm", "No: 15 mm es menor que 12 mm", "No se puede saber sin el espesor", "El borde del agujero está a 15 mm y la exigencia es de 12 mm."),
        ("abc", "{F} Un compañero propone anotar 85 porque «es lo que ya se había anotado». ¿Qué le respondes?", "Que una cota anotada que no cuadra con las demás debe corregirse, no mantenerse por costumbre", "Que tiene razón, porque lo anotado primero manda", "Que se anote 82,5", "Las cotas deben ser coherentes entre sí."),
        ("=", "{F} Si el centro de los agujeros estuviera a 25 mm de cada borde y el largo se mantuviera, ¿cuánta distancia horizontal habría entre centros?", "120-25-25", "Al largo se le restan las dos distancias nuevas.", " mm"),
        ("ab", "{F} Un dibujante cambia la posición de los agujeros de 20 a 25 mm sin avisar. ¿Qué corresponde?", "Registrar el cambio como nueva revisión y avisar a quien lo pidió", "No hacer nada, porque el plano es del dibujante", "Un cambio de posición afecta la fabricación y debe quedar en una nueva revisión comunicada."),
    ],
    ctx=("abc", "El taller ya empezó a fabricar usando la cota de 85 mm. Descubres tu error. ¿Qué haces?", "Aviso de inmediato al taller y al mandante, con la cota correcta y la nueva revisión", "No digo nada para no generar problemas", "Espero a que el taller descubra el error", "Un error con consecuencias se comunica de inmediato y por escrito."),
    sc=[
        ("En Dibujo Técnico: ¿cómo se calcula la distancia entre centros?", "Medida total menos dos veces la distancia del centro al borde", "Es una resta de las dos distancias al borde."),
        ("¿Cuánto es el radio de un agujero de 12 mm de diámetro?", "6 mm", "El radio es la mitad del diámetro."),
        ("¿Qué haces si descubres un error de acotado ya enviado?", "Aviso de inmediato con la corrección", "No se esconden errores que ya pueden afectar la fabricación."),
    ],
    op=("Una placa de ejemplo mide 200 mm de largo y 120 mm de ancho, con 4 agujeros de 12 mm de diámetro y centros a 30 mm de cada borde. El dibujante anotó distancias entre centros de 140 mm (horizontal) y 60 mm (vertical). Calcula las distancias correctas, indica qué cota está mal, calcula la distancia del borde del agujero al borde de la placa y escribe cómo avisarías.",
        "Horizontal: 200 − 60 = 140 mm (correcta). Vertical: 120 − 60 = 60 mm (correcta). En este caso las cotas están bien. Borde del agujero: 30 − 6 = 24 mm. Aviso: «Cotas verificadas, sin diferencias».",
        ["calcula ambas distancias", "calcula la distancia al borde", "concluye si hay o no error"],
        ["hoja con cálculos y una frase"],
        ["restar el diámetro en vez del radio", "decir que hay error sin calcular", "no escribir el aviso"],
        "Pregunta: «¿cómo demuestras que las cotas están bien?». Si no responde, pídele que repita ambos cálculos."),
    reinforce="Dibuja una tarjeta rectangular con cuatro agujeros en las esquinas y calcula la distancia entre centros.",
    extend="Explica con un ejemplo inventado por qué una cota calculada sirve para detectar errores.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (control de calidad de ejemplo). Un eje debe medir 40 mm de diámetro, con una tolerancia de ejemplo de más o menos 1 mm; es decir, se acepta entre 39 mm y 41 mm. "
     "Seis ejes medidos por el taller: 39; 40; 41; 42; 38; 40 mm. El agujero donde entra el eje mide 42 mm de diámetro. Los valores de tolerancia son de ejemplo y no representan los de un taller real.")
build(
    O5, 4, F,
    use="Aprenderé a leer una tolerancia, a decidir si una pieza se acepta o se rechaza, y a calcular la holgura entre un eje y su agujero.",
    prior=["Sé qué es un diámetro.", "Sé comparar números.", "Sé qué es una cota."],
    explain=[
        "Ninguna pieza se fabrica exactamente con la medida del plano. La tolerancia fija cuánto puede variar la medida y se escribe con el signo más o menos: 40 ± 1 mm significa que el valor nominal, que es la medida de referencia, es 40 mm, el límite inferior es 39 mm y el superior es 41 mm. Una pieza cuya medida está entre los dos límites, incluidos ellos, se acepta; fuera de ellos, se rechaza o se manda a revisión.",
        "La holgura, o juego, es la diferencia de diámetro entre un agujero y el eje que entra en él: holgura = diámetro del agujero − diámetro del eje. Si es positiva, el eje entra con juego; si es cero, entra justo; si es negativa, no entra sin forzarlo. Las tolerancias reales dependen de la función de la pieza y se definen según la norma vigente; aquí son valores de ejemplo.",
        "El control de calidad registra cada medición en una tabla con la medida, el límite inferior, el superior y el resultado. Aceptar una pieza fuera de tolerancia por apuro es un error de calidad; informar el rechazo con claridad es parte del trabajo.",
    ],
    vocab=[("valor nominal", "medida de referencia del plano"), ("tolerancia", "variación permitida de una medida"), ("límite superior", "mayor medida aceptada"), ("límite inferior", "menor medida aceptada"), ("holgura", "diferencia de diámetro entre agujero y eje"), ("rechazo", "decisión de no aceptar una pieza")],
    worked=[
        ("Calcular los límites", "Una pieza de ejemplo debe medir 60 mm con tolerancia de ± 2 mm. ¿Entre qué valores se acepta?", ["Límite inferior: 60 − 2 = 58 mm.", "Límite superior: 60 + 2 = 62 mm."], "Entre 58 mm y 62 mm"),
        ("Calcular la holgura", "Un agujero de ejemplo mide 25 mm y el eje que entra mide 23 mm. ¿Cuál es la holgura?", ["Holgura = agujero − eje.", "25 − 23 = 2 mm."], "2 mm"),
    ],
    mistakes=[("Aceptar una pieza de 42 mm «porque falta poco» con tolerancia hasta 41 mm.", "Fuera de los límites, la pieza no cumple, aunque sea por poco.", "Compara la medida con los dos límites y registra el rechazo."),
              ("Confundir tolerancia con medida nominal.", "La nominal es la medida de referencia; la tolerancia es cuánto puede variar.", "Escribe siempre ambas: 40 ± 1 mm.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es el valor nominal?", "La medida de referencia del plano", "La tolerancia de la pieza", "La medida real de cada pieza fabricada", "El nominal es la medida de referencia; la real puede variar dentro de la tolerancia."),
        ("abc", "¿Qué significa 40 ± 1 mm?", "Se aceptan medidas de 39 mm a 41 mm", "Se aceptan medidas de 40 mm a 41 mm", "La pieza debe medir exactamente 41 mm", "El ± aplica hacia arriba y hacia abajo del nominal."),
        ("abc", "¿Qué es la holgura entre eje y agujero?", "La diferencia de diámetros entre agujero y eje", "El largo del eje", "El espesor de la pieza", "La holgura se calcula restando el diámetro del eje al del agujero."),
        ("=", "{F} ¿Cuál es el límite superior del eje?", "40+1", "Se suma la tolerancia al valor nominal.", " mm"),
        ("=", "{F} ¿Cuál es el límite inferior del eje?", "40-1", "Se resta la tolerancia al valor nominal.", " mm"),
        ("abc", "{F} El eje de 41 mm, ¿se acepta?", "Sí: coincide con el límite superior", "No: supera el nominal", "No: no es de 40 mm", "El límite está incluido, por lo tanto se acepta."),
        ("abc", "{F} El eje de 42 mm, ¿se acepta?", "No: supera el límite superior de 41 mm", "Sí: solo supera por 1 mm", "Sí: cabe en el agujero de 42 mm", "Cumplir la tolerancia no depende del agujero, sino de los límites."),
        ("abc", "{F} ¿Cuántos de los seis ejes medidos están dentro de tolerancia?", "4 ejes: los de 39, 40, 41 y 40 mm", "5 ejes: todos menos el de 42 mm", "2 ejes: solo los de 40 mm", "Cumplen 39, 40, 41 y 40 mm; el de 42 supera el límite superior y el de 38 no llega al inferior."),
        ("=", "{F} ¿Cuál es la holgura del eje nominal de 40 mm con el agujero de 42 mm?", "42-40", "Se resta el diámetro del eje al del agujero.", " mm"),
        ("=", "{F} ¿Cuál es la holgura con el eje de 41 mm (el mayor aceptado)?", "42-41", "Se calcula la holgura mínima posible dentro de la tolerancia.", " mm"),
        ("=", "{F} ¿Cuál es la holgura con el eje de 39 mm (el menor aceptado)?", "42-39", "Se calcula la holgura máxima posible dentro de la tolerancia.", " mm"),
        ("abc", "{F} Un inspector dice: «el eje de 42 mm entra justo en el agujero, entonces sirve». ¿Qué respondes?", "No cumple el plano; el control se hace con la tolerancia y se registra el rechazo", "Tiene razón, entra", "Basta con que entre sin forzarlo", "Aceptar una pieza fuera de tolerancia es un error de calidad."),
        ("abc", "{F} El taller necesita fabricar más ejes y una pieza mide 38 mm. ¿Qué queda anotado en el registro?", "Medida 38, límite inferior 39, resultado: rechazo", "Medida 38, resultado: aceptado", "Solo la palabra «error»", "El registro muestra la medida, los límites y el resultado."),
    ],
    ctx=("abc", "Faltan pocas horas para entregar y quedan ejes de 42 mm. El jefe dice «entréguenlos igual, el cliente no se va a dar cuenta». ¿Qué corresponde?", "Informar que están fuera de tolerancia y proponer rehacerlos o acordar la desviación por escrito con el cliente", "Entregarlos sin avisar", "Cambiar la tolerancia en el plano para que calcen", "Una desviación se informa y se acuerda por escrito; no se oculta ni se cambia el plano para justificarla."),
    sc=[
        ("En Dibujo Técnico: ¿qué significa 50 ± 2 mm?", "Se aceptan medidas entre 48 mm y 52 mm", "El ± aplica hacia ambos lados."),
        ("¿Cómo se calcula la holgura?", "Diámetro del agujero menos diámetro del eje", "Si el resultado es positivo, el eje entra con juego."),
        ("¿Qué haces con una pieza fuera de tolerancia?", "Registro el rechazo e informo", "No se acepta ni se oculta."),
    ],
    op=("Una pieza de ejemplo debe medir 80 mm con tolerancia ± 2 mm. Se miden cinco piezas: 78, 79, 81, 83 y 80 mm. Calcula los límites, indica cuántas piezas se aceptan y cuántas se rechazan, y calcula la holgura de la pieza de 79 mm con un agujero de 82 mm. Escribe una línea del registro del rechazo.",
        "Límites: 78 y 82 mm. Aceptadas: 78, 79, 81, 80 (cuatro). Rechazada: 83 (una). Holgura: 82 − 79 = 3 mm. Registro: «Pieza de 83 mm, límite superior 82 mm, resultado rechazo».",
        ["calcula los límites", "clasifica las cinco piezas", "calcula la holgura y escribe el registro"],
        ["tabla de medidas con resultado y una línea de registro"],
        ["aceptar la pieza de 83", "calcular mal los límites", "omitir la unidad"],
        "Pregunta: «¿qué piezas rechazas y por qué?». Si no responde, repasa los límites."),
    reinforce="Imagina una pieza de 30 mm con tolerancia de ± 1 mm y escribe cuáles de estas medidas aceptarías: 28, 29, 30, 31, 32.",
    extend="Explica con un ejemplo inventado qué problema podría producir aceptar una pieza fuera de tolerancia.",
)

# ============================================================ OAE-05, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Pieza de tres tramos en línea: A mide 30 mm, B mide 50 mm y C mide 20 mm, total 100 mm. Cada tramo tiene una tolerancia de ± 1 mm. "
     "Alternativa 1: acotar en cadena (se anotan las tres cotas de tramo). Alternativa 2: acotar desde una referencia común (cada punto se mide desde el extremo izquierdo: 30, 80 y 100). "
     "Se necesitan 100 piezas. Material: Opción X, acero a $400 por pieza; Opción Y, aluminio a $520 por pieza. Todos los valores son de ejemplo.")
build(
    O5, 5, F,
    use="Aprenderé a comparar dos formas de acotar y dos materiales con criterios medibles, y a verificar un plano con una lista de control.",
    prior=["Sé qué es una tolerancia.", "Sé sumar tolerancias.", "Sé comparar costos."],
    explain=[
        "Una pieza puede acotarse de varias formas. En el acotado en cadena se anota cada tramo uno tras otro, y las tolerancias se acumulan: el total puede variar la suma de las tolerancias de los tramos. En el acotado desde una referencia común, cada punto se mide desde el mismo extremo, y la tolerancia de cada punto no depende de los demás. Se elige según qué medida es crítica para la función de la pieza.",
        "Para comparar alternativas se usan criterios medibles: acumulación de tolerancia, costo total y facilidad de lectura. El costo total es el costo por pieza por la cantidad. La decisión final la toma quien diseña la pieza; el dibujante entrega los cálculos y la recomendación justificada.",
        "La calidad del plano se verifica con una lista de control: rótulo completo, escala, todas las cotas con unidad, sin cotas repetidas, tolerancias donde corresponde, material y cantidad, y revisión. Un solo punto que falle impide entregarlo.",
    ],
    vocab=[("acotado en cadena", "cotas anotadas tramo tras tramo"), ("referencia común", "extremo desde donde se miden todas las cotas"), ("acumulación de tolerancias", "suma de las variaciones de varios tramos"), ("costo total", "costo por pieza por la cantidad"), ("lista de control", "lista de puntos que se revisan antes de entregar")],
    worked=[
        ("Acumular tolerancias", "Una pieza de ejemplo tiene dos tramos acotados en cadena, cada uno con ± 2 mm. ¿Cuánto puede variar la longitud total?", ["Las variaciones se suman: 2 + 2 = 4 mm.", "La longitud total puede variar ± 4 mm."], "± 4 mm"),
        ("Comparar costos", "Opción X: $200 por pieza; Opción Y: $260 por pieza; se necesitan 50 piezas. ¿Cuánto cuesta cada opción?", ["X: 50 × 200 = $10.000.", "Y: 50 × 260 = $13.000."], "X cuesta $10.000 e Y cuesta $13.000"),
    ],
    mistakes=[("Acotar en cadena una medida crítica de la pieza.", "Las tolerancias se acumulan y la medida crítica puede quedar fuera de lo aceptable.", "Acota la medida crítica directamente desde una referencia."),
              ("Elegir el material más barato sin considerar la función de la pieza.", "Un material inadecuado puede fallar y salir más caro después.", "Compara con criterios y consulta a quien diseña.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es acotar en cadena?", "Anotar las cotas de cada tramo uno tras otro", "Medir todo desde un mismo extremo", "Anotar solo la cota total", "El acotado en cadena anota tramo tras tramo."),
        ("abc", "¿Qué pasa con las tolerancias en una cadena de cotas?", "Se acumulan", "Se anulan entre sí", "Se vuelven cero", "La variación total puede ser la suma de las variaciones de los tramos."),
        ("abc", "¿Qué es una referencia común?", "Un extremo desde donde se miden todas las cotas", "El material de la pieza", "El número de piezas", "Todas las cotas parten del mismo punto."),
        ("=", "{F} Con acotado en cadena, ¿cuántos mm puede variar la longitud total? (suma de tolerancias de los tres tramos)", "1+1+1", "Se suman las tolerancias de A, B y C.", " mm"),
        ("abc", "{F} Con acotado desde la referencia común, ¿cuánto puede variar el punto de 100 mm si cada cota tiene ± 1 mm?", "± 1 mm", "± 3 mm", "± 0 mm", "Esa cota depende solo de su medición desde la referencia."),
        ("abc", "{F} Si la medida de 100 mm es crítica, ¿qué alternativa conviene?", "Acotar desde la referencia común", "Acotar en cadena", "Es indiferente", "En cadena la tolerancia se acumula; desde la referencia no."),
        ("=", "{F} ¿Cuánto cuesta el material de 100 piezas de la Opción X?", "100*400", "Se multiplica el costo por pieza por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta el material de 100 piezas de la Opción Y?", "100*520", "Se multiplica el costo por pieza por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta la Opción Y que la X?", "100*520-100*400", "Se resta el costo total de X al costo total de Y.", " pesos"),
        ("abc", "{F} ¿Quién decide el material final?", "Quien diseña la pieza, con los cálculos entregados", "El dibujante, según su preferencia", "Siempre el más barato", "El dibujante entrega cálculos; la decisión es de quien diseña."),
        ("abc", "{F} El plano lleva las tres cotas de tramo y además la total de 100 mm sin tolerancia. ¿Qué problema hay?", "Hay cotas redundantes que pueden contradecirse", "Ninguno, entre más cotas mejor", "El plano no tiene escala", "Si tres tramos y el total están acotados, una cota sobra y puede contradecir a las otras."),
        ("=", "{F} Si el tramo B tuviera ± 2 mm en lugar de ± 1 mm, ¿cuánto variaría la longitud total en cadena?", "1+2+1", "Se suman las tolerancias de los tres tramos.", " mm"),
        ("abc", "{F} En la lista de control, falta la cantidad de piezas. ¿Se entrega el plano?", "No: falta un punto de la lista", "Sí: la cantidad no importa", "Sí: se agrega después de entregarlo", "Un punto faltante de la lista impide entregar el plano."),
    ],
    ctx=("abc", "El mandante pide acero, pero tú crees que aluminio sería mejor. ¿Qué haces?", "Presento los cálculos de costo y mi observación, y que decidan quien diseña y el mandante", "Cambio el material en el plano sin avisar", "Callo mi observación aunque vea un problema", "El dibujante informa con fundamentos; no cambia lo que pidió el mandante por su cuenta."),
    sc=[
        ("En Dibujo Técnico: ¿qué ventaja tiene acotar desde una referencia común?", "La tolerancia de cada punto no se acumula con la de los demás", "Cada punto se mide desde el mismo extremo."),
        ("¿Cómo se calcula el costo total de un material?", "Costo por pieza por cantidad", "Se multiplican ambos valores para obtener el total."),
        ("¿Qué pasa si un punto de la lista de control no cumple?", "No se entrega el plano hasta corregirlo", "La lista exige todos los puntos."),
    ],
    op=("Una pieza de ejemplo tiene tres tramos de 40, 60 y 30 mm, cada uno con ± 1 mm. Compara el acotado en cadena y el acotado desde una referencia común para la medida total de 130 mm, calcula cuánto puede variar la total en la cadena, y compara el costo de 60 piezas a $300 (opción P) y $380 (opción Q). Recomienda una alternativa de cada tipo.",
        "En cadena: 1 + 1 + 1 = ± 3 mm. Desde la referencia: ± 1 mm. Costo P: 60 × 300 = $18.000. Costo Q: 60 × 380 = $22.800. Recomendación: acotar desde la referencia común si la total es crítica; el material lo decide quien diseña, según función y costo.",
        ["calcula la acumulación de tolerancias", "compara los costos", "recomienda con fundamento y respeta quién decide"],
        ["hoja con cálculos y una recomendación"],
        ["no sumar las tolerancias", "comparar costos sin multiplicar por la cantidad", "decidir el material por su cuenta"],
        "Pregunta: «¿qué ventaja tiene la referencia común?». Si no responde, repasa la acumulación de tolerancias."),
    reinforce="Mide tres tramos de una regla o cinta y explica qué pasaría con la medida total si cada medición varía 1 mm.",
    extend="Explica con un ejemplo inventado cuándo conviene acotar en cadena y cuándo desde una referencia común.",
)

# ============================================================ OAE-06, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). «Bodega Pampa»: estructura de acero con 4 pilares y 2 vigas principales. Plano de montaje de ejemplo: muestra cómo se ubican y se unen las piezas ya fabricadas, con una marca (identificador) para cada una. "
     "Catálogo de ejemplo de un fabricante: perfil P1, 10 kg por metro; perfil P2, 15 kg por metro. Pilares de perfil P2 de 4 m de largo; vigas de perfil P1 de 6 m de largo. "
     "Roles: la calculista decide las secciones y verifica la resistencia; el dibujante representa; el fabricante corta y arma las piezas; el montajista instala con autorización.")
build(
    O6, 1, F,
    use="Aprenderé qué es un plano de montaje y un plano estructural, quién decide qué en un proyecto de estructuras y por qué el dibujante no cambia secciones por su cuenta.",
    prior=["Sé multiplicar longitud por una cantidad por metro.", "Sé qué es un plano de fabricación.", "Sé qué es un catálogo."],
    explain=[
        "Un plano de montaje industrial muestra cómo se ubican y se unen piezas ya fabricadas para formar un conjunto: cada pieza lleva una marca para identificarla. Un plano estructural muestra los elementos que soportan cargas en una obra: pilares, vigas, losas y muros. Las estructuras pueden ser de madera, hormigón (mezcla de cemento, arena, gravilla y agua), albañilería (muros de ladrillos o bloques unidos con mortero) o acero. Se dibujan conforme a normas, manuales y catálogos de fabricantes, que entregan medidas y pesos estandarizados.",
        "El dibujante no calcula ni decide la resistencia: eso lo hace la calculista, que es la profesional responsable. Si el dibujante cree que una sección es insuficiente o que hay un error, lo informa por escrito; no cambia el perfil, ni la medida, ni el material por su cuenta. Un error en una estructura puede causar daños graves.",
        "Montar piezas pesadas o trabajar en altura exige personal autorizado, equipo de protección y procedimientos que no se enseñan en este cuaderno. Esto es aprendizaje conceptual en papel. Practicar esta tarea exige instructor autorizado, norma vigente y elementos de protección; este cuaderno no te habilita para trabajar. Los planos del proyecto son confidenciales y no se comparten sin permiso.",
    ],
    vocab=[("plano de montaje", "plano que muestra cómo se ubican y unen piezas ya fabricadas"), ("plano estructural", "plano de los elementos que soportan cargas"), ("marca", "identificador de cada pieza"), ("calculista", "profesional que decide las secciones y verifica la resistencia"), ("catálogo", "documento del fabricante con medidas y pesos estandarizados"), ("hormigón", "mezcla de cemento, arena, gravilla y agua"), ("albañilería", "muros de ladrillos o bloques unidos con mortero")],
    worked=[
        ("Calcular un peso", "Una viga de ejemplo mide 5 m y su perfil pesa 8 kg por metro según el catálogo. ¿Cuánto pesa?", ["Peso = largo × peso por metro.", "5 × 8 = 40 kg."], "40 kg"),
        ("Quién decide", "En un plano estructural de ejemplo, el dibujante cree que un pilar es muy delgado. ¿Qué hace?", ["La sección la decide la calculista.", "El dibujante informa por escrito su duda y espera la decisión."], "Informa por escrito a la calculista; no cambia el perfil"),
    ],
    mistakes=[("Cambiar un perfil por otro «más barato» del catálogo para ahorrar.", "La calculista eligió ese perfil por su resistencia; cambiarlo puede poner en riesgo la estructura.", "Propón el cambio por escrito y espera la decisión de la calculista."),
              ("Creer que si el plano está en el computador ya es correcto.", "El archivo no verifica la resistencia ni los datos.", "Revisa los datos con la lista de piezas y con el catálogo.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un plano de montaje?", "Un plano que muestra cómo se ubican y unen piezas ya fabricadas", "Un plano que muestra los precios de las piezas", "Un dibujo del terreno sin piezas", "El plano de montaje explica cómo se ensamblan las piezas."),
        ("abc", "¿Quién decide la sección de un pilar?", "La calculista", "El dibujante", "El montajista", "La sección se decide con cálculo de resistencia."),
        ("abc", "¿Para qué sirve el catálogo del fabricante?", "Para obtener medidas y pesos estandarizados de los perfiles", "Para decidir el color de la obra", "Para firmar el proyecto", "El catálogo entrega medidas y pesos estandarizados de los perfiles."),
        ("=", "{F} ¿Cuántos kilogramos pesa una viga principal (perfil P1, 6 m)?", "6*10", "Se multiplica el largo por el peso por metro.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesa un pilar (perfil P2, 4 m)?", "4*15", "Se multiplica el largo por el peso por metro.", " kg"),
        ("abc", "{F} ¿Quién arma las piezas en el taller?", "El fabricante", "La mandante", "El dibujante", "El fabricante corta y arma; el montajista instala."),
        ("=", "{F} ¿Cuántos kilogramos pesan los 4 pilares juntos?", "4*4*15", "Se multiplica la cantidad de pilares por su peso unitario.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesan las 2 vigas principales juntas?", "2*6*10", "Se multiplica la cantidad por el peso de cada viga.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesan en total los pilares y las vigas?", "4*4*15+2*6*10", "Se suman los pesos de pilares y vigas.", " kg"),
        ("abc", "{F} La mandante pide cambiar los pilares P2 por P1 para ahorrar. ¿Qué haces?", "Informo que el cambio de sección lo decide la calculista, y se lo consulto", "Lo cambio en el plano, porque la mandante manda", "Lo cambio si el catálogo lo permite", "Las secciones las decide la calculista."),
        ("abc", "{F} Un dibujante detecta que dos piezas tienen la misma marca. ¿Qué problema produce?", "Se pueden confundir al fabricar o montar", "Ninguno, porque son iguales", "Se pierde la escala", "La marca identifica cada pieza de forma única."),
        ("=", "{F} Si se agregara un pilar más de perfil P2 de 4 m, ¿cuántos kg sumaría al total?", "4*15", "Es el peso de un pilar.", " kg"),
        ("abc", "{F} Un compañero propone subirse a probar cómo se une una viga a un pilar «para dibujarlo mejor». ¿Qué corresponde?", "No: trabajar en altura exige personal autorizado y protección; el dibujante usa el plano", "Sí, si hay una escalera firme", "Sí, si lo hace rápido", "Trabajar en altura es un riesgo grave que corresponde a personal autorizado."),
    ],
    ctx=("abc", "El fabricante te envía un catálogo con perfiles del mismo nombre pero con pesos distintos a los de tu plano. ¿Qué haces?", "Consulto cuál catálogo y versión corresponde al proyecto antes de usar los pesos", "Uso el que me parece más actual", "Uso el promedio de los dos", "Hay que usar el catálogo indicado por el proyecto; no se promedian datos distintos."),
    sc=[
        ("En Dibujo Técnico: ¿qué es la marca de una pieza?", "Un identificador único de la pieza", "Permite saber de qué pieza se habla."),
        ("¿Quién decide las secciones de una estructura?", "La calculista", "El dibujante solo representa lo que decidió la calculista."),
        ("¿Cómo se calcula el peso de una viga con el catálogo?", "Largo por peso por metro", "Es una multiplicación sencilla de dos datos del catálogo."),
    ],
    op=("Un proyecto de ejemplo tiene 3 pilares de perfil P3 de 3 m, con 12 kg por metro, y 2 vigas de perfil P4 de 5 m, con 9 kg por metro. Calcula el peso de cada tipo de pieza, el peso total y escribe qué harías si el mandante pide cambiar P4 por un perfil más liviano.",
        "Pilares: 3 × 3 × 12 = 108 kg. Vigas: 2 × 5 × 9 = 90 kg. Total: 198 kg. Ante el cambio, informo que lo decide la calculista, se lo consulto y espero su respuesta.",
        ["calcula los pesos con el catálogo", "suma el peso total", "no cambia el perfil por su cuenta"],
        ["hoja con cálculos y una frase"],
        ["olvidar multiplicar por la cantidad de piezas", "cambiar el perfil", "no escribir el total con unidad"],
        "Pregunta: «¿quién decide el cambio de perfil?». Si no responde, repasa los roles."),
    reinforce="Elige un objeto de tu casa con dos o más partes y haz una lista de piezas con una marca para cada una.",
    extend="Explica con un ejemplo inventado por qué el dibujante no debe cambiar una sección por su cuenta.",
)

# ============================================================ OAE-06, clase 2
F = ("Ficha 2 (elementos de ejemplo). Hormigón armado: hormigón con barras de acero en su interior llamadas armadura. Viga de ejemplo: sección de 20 cm de ancho por 40 cm de alto, 3 m de largo, con 4 barras longitudinales de 12 mm de diámetro y estribos (aros de barra que rodean a las barras longitudinales) cada 20 cm. "
     "Madera: una escuadría es la sección transversal de una pieza de madera; escuadría de ejemplo: 50 mm por 100 mm. Albañilería: muro de bloques de 40 cm de largo por 20 cm de alto cada uno, de ejemplo. Acero: perfil de catálogo con peso por metro. "
     "Lista de piezas de ejemplo: marca V1, cantidad 2, perfil P1, largo 6 m; marca C1, cantidad 4, perfil P2, largo 4 m.")
build(
    O6, 2, F,
    use="Aprenderé los elementos y documentos de los proyectos estructurales en madera, hormigón, albañilería y acero, y cómo se lee una lista de piezas.",
    prior=["Sé qué es un plano estructural.", "Sé calcular superficies.", "Sé leer tablas."],
    explain=[
        "Los materiales estructurales se representan de forma distinta. En hormigón armado se dibujan la sección del hormigón y la armadura: barras longitudinales y estribos. En madera se anota la escuadría, que es la sección de la pieza, y su largo. En albañilería se muestran los muros, con el tipo de ladrillo o bloque y sus dimensiones. En acero se usan perfiles de catálogo, cada uno con su nombre, su peso por metro y sus medidas.",
        "Los documentos principales son el plano de elementos o de montaje, la lista de piezas con marca, cantidad, perfil y largo, el cuadro de armaduras con diámetro, cantidad y largo de cada barra, y las especificaciones, que describen materiales y calidades según la norma vigente. Los números de calidad y las exigencias los fija la norma; este cuaderno usa solo valores de ejemplo.",
        "Para leer una lista de piezas se multiplica cantidad por largo para obtener el largo total de cada marca. Con él, y el peso por metro del catálogo, se obtiene el peso. Esto es aprendizaje conceptual en papel; la construcción real exige personal y supervisión autorizados.",
    ],
    vocab=[("armadura", "barras de acero dentro del hormigón"), ("estribo", "aro de barra que rodea las barras longitudinales"), ("escuadría", "sección transversal de una pieza de madera"), ("lista de piezas", "tabla con marca, cantidad, perfil y largo"), ("especificaciones", "descripción escrita de materiales y calidades"), ("sección", "forma que se ve al cortar una pieza de forma transversal")],
    worked=[
        ("Largo total de una marca", "En una lista de ejemplo, la marca B2 tiene cantidad 3 y largo 2 m. ¿Cuántos metros suman?", ["Largo total = cantidad × largo.", "3 × 2 = 6 m."], "6 m"),
        ("Superficie de una sección", "Una viga de ejemplo tiene sección de 15 cm de ancho por 30 cm de alto. ¿Cuántos cm² tiene?", ["Superficie = ancho × alto.", "15 × 30 = 450 cm²."], "450 cm²"),
    ],
    mistakes=[("Confundir la escuadría de madera con el largo de la pieza.", "La escuadría es la sección transversal; el largo se anota aparte.", "Lee las dos medidas por separado."),
              ("Contar solo una vez una marca que tiene cantidad 4.", "La lista indica cuántas piezas iguales hay; hay que multiplicar.", "Multiplica la cantidad por el largo de cada pieza.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la armadura de una viga de hormigón armado?", "Las barras de acero dentro del hormigón", "El molde exterior de madera", "La pintura de la viga", "La armadura de acero refuerza el hormigón por dentro."),
        ("abc", "¿Qué es la escuadría de una pieza de madera?", "La sección transversal de la pieza", "El largo de la pieza", "El tipo de árbol", "La escuadría describe la sección transversal de la pieza."),
        ("abc", "¿Qué es un estribo?", "Un aro de barra que rodea a las barras longitudinales", "Una barra recta de la parte inferior", "Un pilar de acero", "Los estribos abrazan a las barras longitudinales."),
        ("=", "{F} ¿Cuántos centímetros cuadrados tiene la sección de la viga de hormigón?", "20*40", "La superficie de la sección es ancho por alto.", " cm²"),
        ("=", "{F} ¿Cuántos centímetros cuadrados tiene la escuadría de madera de ejemplo?", "5*10", "50 mm por 100 mm son 5 cm por 10 cm.", " cm²"),
        ("abc", "{F} ¿Qué dato de la lista de piezas indica cuántas piezas iguales hay?", "La cantidad", "El perfil", "La marca", "La cantidad dice cuántas piezas iguales hay."),
        ("=", "{F} ¿Cuántos metros de largo suman las piezas de la marca V1?", "2*6", "Se multiplica la cantidad por el largo.", " m"),
        ("=", "{F} ¿Cuántos metros de largo suman las piezas de la marca C1?", "4*4", "Se multiplica la cantidad por el largo.", " m"),
        ("=", "{F} ¿Cuántos kilogramos pesan las piezas de la marca V1 si el perfil P1 pesa 10 kg por metro?", "2*6*10", "Se multiplica el largo total por el peso por metro.", " kg"),
        ("abc", "{F} ¿Cuántas barras longitudinales tiene la viga de hormigón de la ficha?", "4", "2", "20", "La ficha indica 4 barras longitudinales; el 20 corresponde al ancho de la sección."),
        ("abc", "{F} Un compañero lee «bloques de 40 cm de largo por 20 cm de alto» y dice que cada bloque tiene 60 cm². ¿Qué error comete?", "Suma las medidas en vez de multiplicarlas: la superficie es 800 cm²", "Ninguno, porque 40 + 20 es 60", "Olvida convertir a metros", "La superficie se obtiene multiplicando largo por alto."),
        ("=", "{F} ¿Cuántos bloques de 40 cm de largo caben en un muro de 400 cm de largo, en una hilada?", "400//40", "Se divide el largo del muro por el largo de cada bloque.", " bloques"),
        ("abc", "{F} Los estribos están cada 20 cm en una viga de 3 m. ¿Qué cálculo da la cantidad de espacios entre estribos?", "300 ÷ 20 = 15", "3 × 20 = 60", "300 + 20 = 320", "Los espacios se cuentan dividiendo el largo por la separación."),
    ],
    ctx=("abc", "En la lista de piezas aparece la marca C1 con cantidad 4, pero en el plano de montaje se ven 5 pilares. ¿Qué haces?", "Registro la diferencia y la consulto con quien firmó el proyecto", "Uso la lista, porque tiene números", "Agrego un pilar a la lista", "Una diferencia entre lista y plano es una incoherencia que se consulta."),
    sc=[
        ("En Dibujo Técnico: ¿qué es una escuadría?", "La sección transversal de una pieza de madera", "Se anota en milímetros o centímetros."),
        ("¿Para qué sirven los estribos?", "Para rodear las barras longitudinales de la viga", "Son parte de la armadura del hormigón armado."),
        ("¿Cómo se obtiene el largo total de una marca?", "Cantidad por largo", "Se multiplica para sumar piezas iguales."),
    ],
    op=("Una lista de ejemplo dice: marca V2, cantidad 3, largo 5 m, perfil de 8 kg por metro; marca P3, cantidad 5, largo 3 m, perfil de 12 kg por metro. Calcula el largo total y el peso de cada marca, el peso total, y compara la cantidad de P3 con un plano que muestra 6 pilares.",
        "V2: largo total 15 m; peso 120 kg. P3: largo total 15 m; peso 180 kg. Total: 300 kg. La lista dice 5 pilares P3 y el plano muestra 6: hay una diferencia que debe consultarse con quien firmó.",
        ["calcula largo y peso por marca", "suma el total", "detecta y consulta la diferencia"],
        ["tabla con largos y pesos, y una frase"],
        ["no multiplicar por la cantidad", "corregir la lista sin consultar", "olvidar las unidades"],
        "Pregunta: «¿por qué no corriges tú la lista?». Si no responde, repasa quién decide."),
    reinforce="Haz una lista de piezas de una caja de herramientas imaginaria con marca, cantidad y largo.",
    extend="Explica con un ejemplo inventado qué problema produce una lista de piezas con una cantidad equivocada.",
)

# ============================================================ OAE-06, clase 3
F = ("Ficha 3 (conjunto de ejemplo: marco de acero). Plano de montaje: 2 pilares de marca C1 y 1 viga de marca V1 que une los pilares. "
     "Lista de piezas de ejemplo: C1, cantidad 2, perfil P2 (15 kg por metro), largo 3 m; V1, cantidad 1, perfil P1 (10 kg por metro), largo 5 m. "
     "Distancia entre ejes de los pilares anotada en el plano: 4,8 m. El plano también dice: «largo de la viga V1: 4,2 m».")
build(
    O6, 3, F,
    use="Aprenderé a analizar un plano de montaje con su lista de piezas y a detectar contradicciones entre ambos.",
    prior=["Sé calcular pesos con el catálogo.", "Sé qué es una lista de piezas.", "Sé comparar medidas en la misma unidad."],
    explain=[
        "Analizar un caso es cruzar los documentos entre sí. El plano de montaje y la lista de piezas deben coincidir en marca, cantidad, perfil y largo. La distancia entre ejes es la separación entre los centros de dos pilares; la viga que une los pilares debe ser al menos tan larga como esa distancia, más lo necesario para apoyarse. Por eso, si la viga es más corta que la distancia entre ejes, no puede unir los pilares.",
        "Los controles son tres: coincidencia (lista y plano dicen lo mismo), plausibilidad (las medidas permiten que el conjunto exista) y unidades (todas en la misma unidad). Si hay una contradicción, se registra con su lugar, el valor leído y el valor esperado, y se consulta a quien firmó el proyecto. No se elige la medida que parezca mejor.",
        "El peso de cada marca se calcula con el catálogo, como largo total por peso por metro. Un peso que no coincide con el que indica el proyecto es otra señal de que algún dato está equivocado. Todo se hace en papel; instalar piezas pesadas es trabajo de personal autorizado.",
    ],
    vocab=[("distancia entre ejes", "separación entre los centros de dos pilares"), ("coincidencia", "que dos documentos digan lo mismo"), ("plausibilidad", "que las medidas permitan que el conjunto exista"), ("incoherencia", "contradicción entre datos")],
    worked=[
        ("Verificar que una viga alcanza", "Dos pilares de ejemplo tienen sus ejes a 5 m. La viga de la lista mide 4 m. ¿Alcanza?", ["La viga debe cubrir al menos la distancia entre ejes: 5 m.", "4 m es menor que 5 m: no alcanza."], "No alcanza"),
        ("Cruzar lista y plano", "La lista de ejemplo dice 3 pilares y el plano muestra 3. ¿Coinciden?", ["Se compara la cantidad de la lista con la del plano.", "Ambas dicen 3."], "Sí, coinciden"),
    ],
    mistakes=[("Elegir como correcta la medida «que hace que todo calce».", "Se oculta el error y la pieza puede salir mal.", "Registra y consulta; no ajustes por tu cuenta."),
              ("Comparar 4,8 m con 480 sin convertir la unidad.", "Son la misma medida en unidades distintas, y puede parecer una diferencia que no existe.", "Convierte todo a la misma unidad antes de comparar.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la distancia entre ejes de dos pilares?", "La separación entre los centros de los pilares", "El largo de la viga", "El peso de los pilares", "Se mide de eje a eje."),
        ("abc", "¿Qué debe coincidir entre el plano de montaje y la lista de piezas?", "Marca, cantidad, perfil y largo", "Solo el color", "Solo el nombre del proyecto", "Ambos documentos describen las mismas piezas."),
        ("abc", "¿Qué haces si hay una contradicción?", "La registro y la consulto con quien firmó el proyecto", "Elijo el dato que calza mejor", "No hago nada", "No se elige a ojo; se consulta."),
        ("=", "{F} ¿Cuántos centímetros son 4,8 m?", "4.8*100", "Un metro son 100 centímetros.", " cm"),
        ("=", "{F} ¿Cuántos kilogramos pesa cada pilar C1?", "3*15", "Se multiplica el largo por el peso por metro.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesan los dos pilares C1?", "2*3*15", "Se multiplica por la cantidad.", " kg"),
        ("=", "{F} ¿Cuántos kilogramos pesa la viga V1 de la lista?", "5*10", "Largo de la lista por peso por metro.", " kg"),
        ("abc", "{F} El plano anota la viga V1 con 4,2 m y la lista con 5 m. ¿Qué pasa?", "Hay una contradicción entre plano y lista", "No pasa nada, son vistas distintas", "La lista siempre manda", "Dos documentos dan largos distintos para la misma pieza."),
        ("abc", "{F} Con 4,2 m, ¿la viga alcanza a unir los dos pilares?", "No: 4,2 m es menor que la distancia entre ejes de 4,8 m", "Sí: 4,2 es mayor que 4", "Sí: la viga siempre alcanza", "Con 4,2 m faltan 0,6 m para cubrir los 4,8 m entre ejes."),
        ("=", "{F} ¿Cuántos centímetros faltan para que la viga de 4,2 m cubra la distancia entre ejes?", "4.8*100-4.2*100", "Se resta el largo de la viga a la distancia entre ejes, ambos en centímetros.", " cm"),
        ("abc", "{F} Con la viga de 5 m de la lista, ¿alcanza a unir los pilares?", "Sí: 5 m es mayor que 4,8 m", "No: 5 m es menor que 4,8 m", "No se puede saber", "5 m cubre la distancia entre ejes de 4,8 m con un sobrante."),
        ("=", "{F} ¿Cuántos centímetros de sobrante tiene la viga de 5 m sobre la distancia entre ejes?", "500-480", "Se resta la distancia entre ejes al largo de la viga.", " cm"),
        ("abc", "{F} ¿Qué registro correcto harías de la contradicción?", "Viga V1: plano 4,2 m; lista 5 m; se consulta a quien firmó el proyecto", "Viga V1: error del dibujante", "Viga V1: cambiar a 4,8 m", "El registro indica lugar, valores y consulta, sin culpar ni cambiar."),
    ],
    ctx=("abc", "Tu jefe dice: «usa los 5 m de la lista, el plano debe estar mal». ¿Qué haces?", "Pido que se confirme el largo con quien firmó el proyecto y dejo registro", "Cambio el plano a 5 m sin dejar registro", "Dejo los dos valores", "La corrección debe confirmarla quien firmó, aunque el jefe pida rapidez."),
    sc=[
        ("En Dibujo Técnico: ¿qué es la distancia entre ejes?", "La separación entre los centros de dos pilares", "La viga debe cubrir al menos esa distancia."),
        ("¿Qué controles haces entre plano y lista?", "Coincidencia, plausibilidad y unidades", "Son los tres controles del análisis."),
        ("¿Cómo se calcula el peso de una marca?", "Cantidad por largo por peso por metro", "Se multiplica con datos del catálogo."),
    ],
    op=("En un plano de ejemplo, dos pilares tienen sus ejes a 6 m. La lista dice una viga V2 de 5,5 m (perfil de 9 kg por metro), pero el plano la anota con 6,3 m. Calcula si cada largo alcanza, el peso de la viga con el largo de la lista y escribe el registro de la contradicción.",
        "Con 5,5 m no alcanza (faltan 0,5 m). Con 6,3 m alcanza y sobra 0,3 m. Peso con 5,5 m: 5,5 × 9 = 49,5 kg. Registro: «Viga V2: lista 5,5 m, plano 6,3 m; distancia entre ejes 6 m. Se consulta a quien firmó el proyecto».",
        ["evalúa ambos largos", "calcula el peso", "escribe el registro con lugar y valores"],
        ["hoja con cálculos y registro"],
        ["elegir un largo sin consultar", "no convertir 5,5 m", "olvidar unidades"],
        "Pregunta: «¿cuál de los dos largos es el correcto?». La respuesta esperada es que no lo sabes y debes consultar."),
    reinforce="Mide la distancia entre dos patas de una mesa y explica qué largo mínimo debería tener una tabla que las una.",
    extend="Explica con un ejemplo inventado por qué una contradicción entre plano y lista debe resolverse antes de fabricar.",
)

# ============================================================ OAE-06, clase 4
F = ("Ficha 4 (cuadro de armaduras de ejemplo, hormigón armado). Viga de ejemplo de 400 cm de largo. Barras longitudinales: 6 barras de 12 mm de diámetro, de 395 cm de largo cada una. "
     "Estribos: cada 20 cm a lo largo de la viga, comenzando en un extremo y terminando en el otro (es decir, 1 estribo más que los espacios entre ellos). Largo de una barra comercial de ejemplo: 1.200 cm. "
     "Todos los valores son de ejemplo y no son reglas de armado.")
build(
    O6, 4, F,
    use="Aprenderé a leer un cuadro de armaduras, a calcular largos totales de barras y la cantidad de estribos, y a pedir material con cantidades enteras.",
    prior=["Sé multiplicar y dividir.", "Sé qué es la armadura.", "Sé redondear hacia arriba."],
    explain=[
        "El cuadro de armaduras lista cada barra del proyecto: diámetro, cantidad, largo y forma. El largo total de un grupo de barras es la cantidad por el largo de cada una. Con él se calcula cuántas barras comerciales hay que pedir: se divide el largo total por el largo comercial y se redondea hacia arriba, porque no se pueden pedir fracciones. Los cortes y sobrantes reales los define el proyecto y quien fabrica, y aquí se ignoran.",
        "Para los estribos, la cantidad se obtiene con la separación. Si hay estribos cada cierta distancia a lo largo de un largo L, desde un extremo hasta el otro, los espacios son L dividido por la separación, y los estribos son un estribo más que los espacios. Por ejemplo, 100 cm con estribos cada 25 cm: 4 espacios y 5 estribos.",
        "El dibujante no define el diámetro, la cantidad ni la separación: son datos del cálculo estructural de la calculista. Su trabajo es leer, representar y detectar contradicciones. Esto es aprendizaje conceptual en papel; armar y colocar armaduras es trabajo de personal autorizado.",
    ],
    vocab=[("cuadro de armaduras", "tabla con diámetro, cantidad y largo de las barras"), ("barra comercial", "barra de largo estándar que vende el fabricante"), ("separación", "distancia entre elementos repetidos"), ("largo total", "cantidad por largo de cada elemento")],
    worked=[
        ("Contar estribos", "Una viga de ejemplo de 200 cm tiene estribos cada 25 cm de extremo a extremo. ¿Cuántos estribos hay?", ["Espacios: 200 ÷ 25 = 8.", "Estribos: 8 + 1 = 9."], "9 estribos"),
        ("Pedir barras comerciales", "Se necesitan 2.500 cm de barras y cada barra comercial de ejemplo mide 1.200 cm. ¿Cuántas barras se piden?", ["2.500 ÷ 1.200 da 2 y sobran 100 cm.", "Se redondea hacia arriba: 3 barras."], "3 barras"),
    ],
    mistakes=[("Contar los estribos como los espacios, sin sumar uno.", "Entre dos extremos hay un estribo más que espacios.", "Cuenta espacios y suma uno."),
              ("Pedir 2 barras comerciales porque «2 × 1.200 es casi 2.500».", "Faltarían 100 cm de barra.", "Divide y redondea hacia arriba.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es un cuadro de armaduras?", "Una tabla con el diámetro, cantidad y largo de las barras", "Un dibujo del terreno", "Una lista de precios", "El cuadro describe las barras del proyecto."),
        ("abc", "¿Por qué se redondea hacia arriba al pedir barras?", "Porque no se pueden pedir fracciones y faltaría barra", "Porque conviene pedir de más", "Porque así lo decide el dibujante", "Si sobra una fracción, hace falta una barra más."),
        ("abc", "¿Quién define la cantidad y el diámetro de las barras?", "La calculista, en el cálculo estructural", "El dibujante", "El montajista", "El cálculo estructural define esos datos."),
        ("=", "{F} ¿Cuántos centímetros de barra suman las 6 barras longitudinales?", "6*395", "Se multiplica la cantidad por el largo de cada una.", " cm"),
        ("=", "{F} ¿Cuántos espacios hay entre estribos en la viga de 400 cm?", "400//20", "Se divide el largo por la separación.", " espacios"),
        ("=", "{F} ¿Cuántos estribos hay en total?", "400//20+1", "Hay un estribo más que espacios.", " estribos"),
        ("=", "{F} ¿Cuántas barras comerciales de 1.200 cm se piden para las barras longitudinales? (redondea hacia arriba)", "(2370+1199)//1200", "Se divide el largo total por el largo comercial y se redondea hacia arriba.", " barras"),
        ("abc", "{F} Un compañero cuenta 20 estribos porque «400 ÷ 20 son 20». ¿Cuál es su error?", "No suma el estribo del extremo: son 21", "Divide mal el largo", "Confunde los estribos con las barras", "Entre dos extremos hay un estribo más que espacios."),
        ("abc", "{F} El largo de las barras es 395 cm y el de la viga 400 cm. ¿Qué indica esa diferencia?", "Que las barras son 5 cm más cortas que la viga", "Que hay un error de 395 cm", "Que sobran 5 cm de barra", "400 − 395 es 5 cm, y deja espacio en los extremos."),
        ("=", "{F} ¿Cuántos centímetros más corta es cada barra que la viga?", "400-395", "Se resta el largo de la barra al de la viga.", " cm"),
        ("abc", "{F} El mandante pide más barras «para mayor seguridad». ¿Qué haces?", "Informo que cambiar la armadura lo decide la calculista", "Agrego barras en el cuadro", "Cambio el diámetro a 20 mm", "Un cambio de armadura es una decisión estructural."),
        ("=", "{F} Si la viga midiera 500 cm con estribos cada 20 cm, ¿cuántos estribos habría?", "500//20+1", "Espacios más uno.", " estribos"),
        ("abc", "{F} El cuadro de armaduras no anota el diámetro de los estribos. ¿Qué haces?", "Registro la omisión y la consulto con quien firmó el proyecto", "Pongo el mismo de las barras longitudinales", "Dejo el estribo sin dibujar", "No se inventa un dato estructural faltante."),
    ],
    ctx=("abc", "Calculas las barras comerciales y el resultado da 2,0 exacto. Un compañero dice que pidas 3 «por si acaso». ¿Qué corresponde?", "Pedir 2 si el cálculo lo indica, y consultar si el proyecto exige sobrante", "Pedir 3 siempre", "Pedir 1 para ahorrar", "Se pide lo que indica el cálculo y el criterio de proyecto, sin improvisar."),
    sc=[
        ("En Dibujo Técnico: ¿cuántos estribos hay en 200 cm con separación de 20 cm de extremo a extremo?", "11", "Son 10 espacios y un estribo más."),
        ("¿Cómo se calcula el largo total de un grupo de barras?", "Cantidad por largo de cada una", "Se multiplica para sumar piezas iguales."),
        ("¿Qué haces si falta un dato estructural?", "Lo consulto con quien firmó el proyecto", "No se inventa un dato estructural que falta."),
    ],
    op=("Una viga de ejemplo de 300 cm tiene 4 barras longitudinales de 295 cm y estribos cada 15 cm de extremo a extremo. La barra comercial mide 1.200 cm. Calcula el largo total de barras, cuántas barras comerciales se piden, cuántos estribos hay y escribe una observación si el cuadro no anotara el diámetro de los estribos.",
        "Largo total: 4 × 295 = 1.180 cm; 1.180 ÷ 1.200 da menos de 1, por lo tanto 1 barra. Espacios: 300 ÷ 15 = 20; estribos: 21. Observación: «Cuadro de armaduras, estribos: falta el diámetro; se consulta a quien firmó el proyecto».",
        ["calcula el largo total y las barras", "calcula los estribos con el + 1", "escribe la observación sin inventar el dato"],
        ["hoja con cálculos y una observación"],
        ["no sumar el estribo extra", "no redondear hacia arriba", "inventar el diámetro faltante"],
        "Pregunta: «¿por qué 21 estribos y no 20?». Si no responde, dibuja una línea con marcas."),
    reinforce="Dibuja una regla de 10 cm con marcas cada 2 cm y cuenta marcas y espacios.",
    extend="Explica con un ejemplo inventado por qué un cuadro de armaduras con un dato faltante no debe entregarse a fabricación.",
)

# ============================================================ OAE-06, clase 5
F = ("Ficha 5 (alternativas de ejemplo). Una viga debe cubrir 4 m. Alternativa 1: viga de acero de perfil P1 (10 kg por metro), 4 m de largo, precio de ejemplo $2.400 por metro. "
     "Alternativa 2: viga de madera, escuadría de ejemplo 50 mm por 200 mm, 4 m de largo, precio de ejemplo $1.600 por metro. La calculista indicó que ambas cumplen la resistencia de ejemplo. "
     "Lista de control del plano de montaje: (1) marcas únicas; (2) lista de piezas igual al plano; (3) catálogo y versión vigentes; (4) unidades iguales; (5) revisión escrita; (6) firma del profesional responsable.")
build(
    O6, 5, F,
    use="Aprenderé a comparar alternativas estructurales con criterios medibles y a verificar la calidad de un plano de montaje con una lista de control.",
    prior=["Sé calcular pesos y costos.", "Sé qué es una lista de control.", "Sé que la calculista decide la resistencia."],
    explain=[
        "Cuando existen varias soluciones que cumplen lo exigido por la calculista, se comparan con criterios medibles: costo, peso, disponibilidad y facilidad de transporte. El costo se calcula multiplicando precio por metro por largo. El peso se obtiene con el catálogo, y para la madera con el dato del proveedor. Los datos de ejemplo de esta ficha no son precios reales. El dibujante entrega la comparación; la decisión final la toma la calculista con la mandante.",
        "La verificación de calidad usa una lista de control: marcas únicas, lista de piezas igual al plano, catálogo vigente, unidades consistentes, revisión escrita y firma del responsable. Si un punto no cumple, no se entrega. Se guarda un registro de cada verificación con fecha y revisión, para saber qué se controló.",
        "Un error de estructura es grave, por lo que se aplica el principio de doble verificación: una segunda persona revisa lo que hizo la primera. Los planos son confidenciales. Esto es aprendizaje conceptual en papel y no te habilita para trabajar en una obra.",
    ],
    vocab=[("alternativa", "una opción posible entre varias"), ("criterio medible", "regla con números para comparar"), ("doble verificación", "revisión de un trabajo por una segunda persona"), ("disponibilidad", "que el material se pueda conseguir a tiempo")],
    worked=[
        ("Comparar costos", "Alternativa A: 3 m a $1.500 por metro. Alternativa B: 3 m a $1.900 por metro. ¿Cuánto cuesta cada una?", ["A: 3 × 1.500 = $4.500.", "B: 3 × 1.900 = $5.700."], "A $4.500 y B $5.700"),
        ("Aplicar la lista de control", "Un plano de ejemplo tiene todas las marcas únicas, pero la lista de piezas dice 3 vigas y el plano muestra 4. ¿Se entrega?", ["El punto 2 de la lista no se cumple.", "No se entrega hasta resolver la diferencia."], "No se entrega"),
    ],
    mistakes=[("Elegir siempre la alternativa más barata.", "Puede ser menos disponible, más pesada o menos adecuada para la obra.", "Compara varios criterios y deja la decisión a la calculista."),
              ("Marcar un punto de la lista de control sin revisarlo.", "Un error no revisado llegaría a fabricación.", "Revisa cada punto en los documentos.")],
    T=[
        ("abc", "En Dibujo Técnico: ¿qué es la doble verificación?", "La revisión de un trabajo por una segunda persona", "Revisar dos veces el mismo dato uno mismo", "Hacer el plano dos veces", "La segunda persona detecta errores que el autor no ve."),
        ("abc", "¿Qué es un criterio medible?", "Una regla con números para comparar opciones", "Una opinión personal", "El color del material", "Un criterio medible permite comparar con datos."),
        ("abc", "¿Quién decide entre alternativas que cumplen la resistencia?", "La calculista con la mandante, usando la comparación", "El dibujante, por su cuenta", "El montajista", "El dibujante entrega la comparación y no decide."),
        ("=", "{F} ¿Cuántos pesos cuesta la viga de acero (Alternativa 1)?", "4*2400", "Se multiplica el largo por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuántos pesos cuesta la viga de madera (Alternativa 2)?", "4*1600", "Se multiplica el largo por el precio por metro.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta la de acero que la de madera?", "4*2400-4*1600", "Se resta el costo de la madera al del acero.", " pesos"),
        ("=", "{F} ¿Cuántos kilogramos pesa la viga de acero?", "4*10", "Se multiplica el largo por el peso por metro.", " kg"),
        ("abc", "{F} ¿Qué criterio favorece a la madera en la ficha?", "Su menor costo", "Su mayor peso", "Su menor largo", "La madera cuesta $6.400 y el acero $9.600."),
        ("abc", "{F} Para que el acero fuera más conveniente por costo, ¿qué tendría que pasar?", "Que su precio por metro fuera menor que el de la madera", "Que fuera más largo", "Que pesara más", "El costo depende del precio por metro y del largo."),
        ("abc", "{F} La lista de control tiene todos los puntos en regla, menos la firma del profesional. ¿Qué corresponde?", "No entregarlo hasta tener la firma", "Entregarlo, porque cinco de seis alcanza", "Firmar el dibujante en su lugar", "Todos los puntos de la lista deben cumplirse."),
        ("abc", "{F} El plano dice «viga 4 m» y la lista «viga 400 mm». ¿Qué haces?", "Registro la contradicción de unidades y consulto", "Considero que es lo mismo", "Uso la medida del plano", "4 m son 4.000 mm, no 400 mm: hay un error."),
        ("=", "{F} ¿Cuántos milímetros son 4 m?", "4*1000", "Un metro son 1.000 milímetros.", " mm"),
        ("abc", "{F} Dos marcas distintas de la lista tienen el mismo nombre V1. ¿Qué punto de la lista falla?", "Marcas únicas", "Catálogo vigente", "Firma del profesional", "Dos piezas distintas con la misma marca se confunden."),
    ],
    ctx=("abc", "Tu compañera termina el plano y te dice que no necesita revisión porque «ya lo comprobó dos veces». ¿Qué respondes?", "Que una segunda persona debe revisarlo, porque un error de estructura es grave", "Que tiene razón, para ahorrar tiempo", "Que lo revise ella una tercera vez", "La doble verificación evita errores que el autor ya no ve."),
    sc=[
        ("En Dibujo Técnico: ¿qué es un criterio medible?", "Una regla con números para comparar", "Por ejemplo, el costo o el peso de cada alternativa."),
        ("¿Qué pasa si un punto de la lista de control no se cumple?", "No se entrega el plano hasta corregirlo", "La lista exige todos los puntos."),
        ("¿Por qué se hace una doble verificación?", "Porque un error estructural es grave", "Otra persona detecta errores que el autor no ve."),
    ],
    op=("Una viga de ejemplo de 5 m puede ser de acero (perfil de 12 kg por metro, $2.800 por metro) o de madera (escuadría de ejemplo, $1.900 por metro). La calculista dice que ambas cumplen. Calcula el costo y el peso del acero, el costo de la madera, la diferencia de costo, y escribe tres puntos de la lista de control que revisarías.",
        "Acero: costo 5 × 2.800 = $14.000; peso 5 × 12 = 60 kg. Madera: 5 × 1.900 = $9.500. Diferencia: $4.500. Lista: marcas únicas; lista de piezas igual al plano; unidades consistentes. La decisión la toma la calculista con la mandante.",
        ["calcula costos y peso", "compara y calcula la diferencia", "propone tres puntos de control y respeta quién decide"],
        ["hoja con cálculos y la lista"],
        ["no multiplicar por el largo", "decidir por su cuenta", "olvidar un punto de control"],
        "Pregunta: «¿quién decide entre las dos?». Si dice 'yo', repasa los roles."),
    reinforce="Compara dos materiales imaginarios para un estante con costo por metro y largo.",
    extend="Explica con un ejemplo inventado por qué una segunda revisión evita errores graves.",
)
