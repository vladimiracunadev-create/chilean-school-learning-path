"""Curated second-grade mathematics sequences derived from the official OA."""
from __future__ import annotations


def _s(title: str, goal: str, model: str, guided: str, ticket: str) -> dict[str, str]:
    return {"title": title, "goal": goal, "model": model, "guided": guided, "ticket": ticket}


MATH_SKILLS = (
    ("de Habilidad MA02 OAH a", "ensayar una estrategia y cambiarla cuando la evidencia lo exige"),
    ("de Habilidad MA02 OAH b", "comprobar un enunciado con material concreto o gráfico"),
    ("de Habilidad MA02 OAH c", "describir una situación real con lenguaje matemático"),
    ("de Habilidad MA02 OAH d", "comunicar una relación, patrón o regla mediante expresiones matemáticas"),
    ("de Habilidad MA02 OAH e", "explicar el procedimiento propio y escuchar otro camino"),
    ("de Habilidad MA02 OAH f", "seleccionar un modelo de suma, resta u orden de cantidades"),
    ("de Habilidad MA02 OAH g", "traducir una representación pictórica a lenguaje matemático"),
    ("de Habilidad MA02 OAH h", "elegir una representación concreta, pictórica o simbólica pertinente"),
    ("de Habilidad MA02 OAH i", "crear un relato coherente con una expresión matemática simple"),
)
MATH_ATTITUDES = (
    ("de Actitud MA02 OAA A", "trabajo ordenado y metódico"),
    ("de Actitud MA02 OAA B", "búsqueda flexible y creativa de soluciones"),
    ("de Actitud MA02 OAA C", "curiosidad por encontrar regularidades matemáticas"),
    ("de Actitud MA02 OAA D", "confianza progresiva en las propias capacidades"),
    ("de Actitud MA02 OAA E", "esfuerzo y perseverancia ante un desafío"),
    ("de Actitud MA02 OAA F", "expresión y escucha respetuosa de ideas"),
)


def transversal_links(oa_number: int, lesson_index: int, lesson_goal: str) -> list[dict[str, str]]:
    skill_code, skill = MATH_SKILLS[(oa_number * 2 + lesson_index) % len(MATH_SKILLS)]
    attitude_code, attitude = MATH_ATTITUDES[(oa_number + lesson_index * 3) % len(MATH_ATTITUDES)]
    return [
        {"code": skill_code, "type": "Habilidad", "application": f"Se observa al {skill}. La evidencia se recoge mientras el estudiante trabaja la meta «{lesson_goal}»."},
        {"code": attitude_code, "type": "Actitud", "application": f"Se promueve {attitude}: se reconoce la representación, explicación y revisión, no la rapidez."},
    ]


def _oa(topic, axis, prior, vocabulary, materials, support, extension, criteria, misconception, stages):
    return {
        "topic": topic, "axis": axis, "prior": prior, "vocabulary": vocabulary,
        "materials": materials, "support": support, "extension": extension,
        "criteria": criteria, "misconception": misconception, "stages": stages,
    }


SEQUENCES = {
    "MA02 OA 01": _oa(
        "Conteo hasta 1.000 por agrupaciones regulares y desde distintos puntos de inicio", "Números y operaciones",
        "Contar hacia adelante y atrás hasta 100 y reconocer agrupaciones de diez.",
        "secuencia, patrón, intervalo, centena, adelante, atrás y punto de inicio",
        "Tarjetas numéricas, tabla de 1.000, recta numérica abierta, sobres con fichas y bandas de conteo.",
        "Marca el punto de inicio y colorea saltos iguales; trabaja primero en una centena antes de cruzar a la siguiente.",
        "Compara dos maneras de llegar al mismo número y determina cuál usa menos saltos.",
        ["mantiene el intervalo solicitado", "continúa desde cualquier número menor que 1.000", "comprueba la regularidad hacia adelante y atrás"],
        "reiniciar el conteo en un múltiplo conocido en vez de continuar desde el número dado",
        [
            _s("Saltos de 2 desde un número impar", "contaré de 2 en 2 sin cambiar la paridad", "Parte en 137 y registra 139, 141, 143 y 145; cada salto agrega dos aunque no comience en un número par.", "Completan bandas con inicios pares e impares y explican qué se conserva.", "Continúa 253, 255, __, __, __ y comprueba las diferencias."),
            _s("Agrupar y contar de 5 en 5", "usaré grupos de cinco para avanzar y retroceder", "Forma paquetes de cinco tapas y parte en 320: 325, 330, 335; luego retira un paquete para volver a 330.", "Representan secuencias con paquetes y conectan cada movimiento con la escritura numérica.", "Desde 468 cuenta cuatro saltos de 5 hacia adelante y dos hacia atrás."),
            _s("Decenas que cruzan una centena", "contaré de 10 en 10 atravesando una centena", "En una recta abierta muestra 186, 196, 206 y 216; cambia centena, pero las unidades permanecen en seis.", "Resuelven recorridos que cruzan 200, 500 y 900 y detectan una secuencia con un salto incorrecto.", "Completa 774, 784, 794, __, __ y explica qué cifra cambia."),
            _s("Centenas hacia adelante y atrás", "contaré de 100 en 100 desde un número cualquiera", "Desde 246 registra 346, 446 y 546; al retroceder vuelve a 446 sin alterar decenas ni unidades.", "Usan tarjetas de centenas para construir recorridos reversibles menores que 1.000.", "Desde 825 retrocede de 100 en 100 tres veces y verifica invirtiendo el recorrido."),
        ],
    ),
    "MA02 OA 02": _oa(
        "Lectura y representación concreta, pictórica y simbólica de números del 0 al 100", "Números y operaciones",
        "Representar números hasta 20 y coordinar cantidad, dibujo y numeral.",
        "cantidad, numeral, decena, unidad, concreto, pictórico, simbólico y equivalencia",
        "Cubos encajables, palitos agrupados de diez, marcos de diez, tarjetas 0 a 100 y hojas cuadriculadas.",
        "Construye cada número con decenas visibles antes de leerlo; ofrece tarjetas para seleccionar si escribir es una barrera.",
        "Representa un número de dos maneras no canónicas y demuestra que la cantidad se conserva.",
        ["coordina cantidad y numeral", "traduce entre objetos, dibujo y símbolo", "comprueba agrupando en decenas y unidades"],
        "leer las cifras por separado o invertirlas sin comprobar la cantidad representada",
        [
            _s("Colecciones organizadas hasta 50", "leeré una cantidad agrupándola antes de elegir el numeral", "Organiza 34 palitos en tres atados de diez y cuatro sueltos; contrasta con 43 construyendo ambas cantidades.", "Construyen números dictados y cambian la disposición sin cambiar la cantidad.", "Representa 47 con grupos de diez y unidades y selecciona su numeral."),
            _s("Del material al dibujo", "dibujaré decenas y unidades sin perder información", "Traduce 62 cubos a seis barras y dos puntos; cada marca tiene una clave explícita.", "Transforman construcciones en dibujos esquemáticos y una pareja reconstruye el número desde el registro.", "Dibuja 58 con una clave y escribe el número que representa."),
            _s("Del símbolo a dos representaciones", "representaré un numeral en forma concreta y pictórica", "Lee 71 como setenta y uno, construye siete decenas y una unidad y dibuja una segunda representación.", "Rotan por tarjetas 26, 50, 83 y 99, justificando cada correspondencia.", "Muestra dos representaciones de 65 y explica por qué ambas valen lo mismo."),
            _s("Cero y números con cero final", "distinguiré ausencia de unidades de ausencia de cantidad", "Contrasta 0, 7 y 70: siete decenas sin unidades no es una bandeja vacía.", "Clasifican tarjetas y representaciones de 0, 10, 40, 70 y 100.", "Representa 80 y explica qué indica cada cifra, sin usar la frase “ocho y cero” como justificación."),
        ],
    ),
    "MA02 OA 03": _oa(
        "Comparación y orden de números hasta 100 con representaciones y monedas nacionales", "Números y operaciones",
        "Comparar números hasta 20 mediante correspondencia y recta numérica.",
        "mayor, menor, igual, ordenar, decena, unidad, valor y moneda",
        "Cubos base diez, recta numérica, tarjetas de precios y monedas chilenas didácticas o imágenes de igual tamaño.",
        "Compara primero decenas y luego unidades; usa dinero didáctico sin asumir experiencias de compra ni pedir dinero real.",
        "Encuentra todos los números que cumplen dos condiciones de orden y explica los límites.",
        ["compara valores y no tamaño visual", "ordena en la dirección solicitada", "justifica con decenas, unidades o una representación monetaria"],
        "decidir por la cifra de unidades o por el tamaño físico de una moneda",
        [
            _s("Más decenas decide", "compararé dos números observando primero sus decenas", "Construye 46 y 63; seis decenas superan cuatro, por lo que no hace falta comparar unidades.", "Comparan pares con material y escriben una frase de justificación.", "Compara 58 y 72 y explica qué evidencia basta."),
            _s("Mismas decenas, distintas unidades", "compararé números cuando sus decenas coinciden", "En 54 y 59, las cinco decenas empatan; nueve unidades hacen mayor a 59.", "Ordenan familias dentro de una misma decena y verifican en la recta.", "Ordena 84, 81, 87 y 80 de menor a mayor."),
            _s("Valor con monedas chilenas", "representaré y compararé cantidades usando monedas didácticas", "Compara $70 formado con monedas de $10 y $85 con una combinación autorizada; cuenta valor, no piezas.", "Construyen precios hasta $100 de dos maneras y comparan totales.", "Una bolsa representa $60 con seis monedas y otra $50 con diez monedas: ¿cuál vale más y por qué?"),
            _s("Orden con condiciones", "ubicaré números entre límites y comprobaré el orden", "Coloca 38, 52, 47 y 41 entre 30 y 60 en una recta y revisa cada intervalo.", "Resuelven listas ascendentes, descendentes y con un término faltante.", "Escribe tres números mayores que 46 y menores que 60 en orden descendente."),
        ],
    ),
    "MA02 OA 04": _oa(
        "Estimación de cantidades hasta 100 mediante referentes", "Números y operaciones",
        "Estimar hasta 20 usando referentes de cinco y diez y comprobar después.",
        "estimar, aproximadamente, referente, rango, decena, más cerca y comprobar",
        "Bolsas transparentes, colecciones de fichas, marcos de diez, tarjetas de rango y recipientes equivalentes.",
        "Muestra referentes de 10, 25 o 50 junto a la colección y acepta primero un rango razonado.",
        "Diseña una disposición que haga difícil estimar y explica qué referente reduce el engaño visual.",
        ["elige un referente pertinente", "propone una estimación razonable antes de contar", "compara estimación y total sin borrar el intento"],
        "adivinar una cifra exacta por el espacio ocupado o contar antes de registrar una estimación",
        [
            _s("Diez como unidad visual", "estimaré una colección reconociendo grupos cercanos a diez", "Observa una bandeja con 32 fichas organizadas como tres grupos de diez y dos sueltas; registra cerca de 30 antes de contar.", "Estiman colecciones ordenadas entre 20 y 60 y nombran cuántos grupos de diez perciben.", "Estima una colección que parece tener cuatro decenas y comprueba agrupando."),
            _s("Referentes de 25 y 50", "seleccionaré un referente que se acerque a la cantidad", "Compara un frasco con una tarjeta de 50 puntos: parece algo menor, por lo que un rango 40–50 es defendible.", "Eligen entre referentes de 10, 25, 50 y 100 y justifican antes del conteo.", "Para una colección cercana a 70, elige un referente y explica un rango razonable."),
            _s("Disposición y densidad", "evitaré confundir espacio ocupado con cantidad", "Muestra las mismas 48 tapas juntas y dispersas; la cantidad no cambia aunque el área ocupada sí.", "Comparan pares de imágenes, estiman y luego emparejan o agrupan para comprobar.", "Dos colecciones ocupan distinto espacio: explica qué harías antes de afirmar cuál tiene más."),
            _s("Evaluar una estimación", "mediré qué tan útil fue mi estimación", "Si se estimó 60 y había 57, la diferencia es 3; contrasta con estimar 30 para la misma colección.", "Ordenan estimaciones por cercanía al total y discuten qué referente ayudó.", "Estimaste 75 y contaste 68: calcula o representa la diferencia y evalúa tu estrategia."),
        ],
    ),
    "MA02 OA 05": _oa(
        "Composición y descomposición aditiva de números hasta 100", "Números y operaciones",
        "Componer y descomponer números hasta 20 conservando el total.",
        "componer, descomponer, sumando, decena, unidad, parte, todo y equivalencia",
        "Material base diez, fichas de dos colores, diagramas parte-parte-todo y tarjetas de expresiones.",
        "Mantén visible el todo y usa colores para las partes; pasa al símbolo después de construir y dibujar.",
        "Encuentra descomposiciones no canónicas y explica por qué siguen representando el mismo total.",
        ["conserva el total", "registra una descomposición aditiva coherente", "conecta forma concreta, pictórica y simbólica"],
        "creer que sólo la descomposición en decenas y unidades es válida",
        [
            _s("Decenas y unidades como partes", "descompondré un número en decenas y unidades", "Construye 47 como 40 + 7 y muestra cuatro barras y siete unidades.", "Descomponen números elegidos al azar y verifican reuniendo las partes.", "Representa 63 como decenas y unidades en tres formas."),
            _s("Dos sumandos diferentes", "formaré el mismo número con pares de sumandos distintos", "Para 35 compara 30+5, 20+15 y 18+17 con material; todas conservan 35.", "Buscan tres pares para un total y explican cómo trasladaron unidades entre partes.", "Escribe y representa dos descomposiciones distintas de 52."),
            _s("De un dibujo a la expresión", "traduciré una representación pictórica a una suma", "Un dibujo muestra dos barras de diez, nueve puntos y otro grupo de seis: registra 29+6=35.", "Interpretan diagramas sin etiquetas y discuten más de una expresión posible.", "Escribe una expresión para un dibujo que representa 48 y comprueba el total."),
            _s("Completar una parte desconocida", "hallaré la parte que falta con una representación", "Si el todo es 70 y una parte es 26, construye 26 y completa hasta 70 para obtener 44.", "Resuelven diagramas con parte faltante usando base diez o recta abierta.", "Completa: 38 + __ = 60 y muestra cómo verificaste."),
        ],
    ),
    "MA02 OA 06": _oa(
        "Estrategias de cálculo mental para adiciones y sustracciones hasta 20", "Números y operaciones",
        "Componer diez, reconocer dobles y relacionar suma con resta en casos pequeños.",
        "cálculo mental, completar diez, doble, mitad, compensar, reversibilidad y estrategia",
        "Marcos de diez, tarjetas de puntos, cubos de dos colores, recta vacía y tarjetas de cálculos.",
        "Permite ver la representación antes de pedir recuperación mental; trabaja una estrategia por vez y compara su utilidad.",
        "Clasifica cálculos según la estrategia más eficiente y defiende casos donde dos estrategias funcionan.",
        ["elige una estrategia compatible con los números", "explica la transformación realizada", "comprueba con representación u operación inversa"],
        "aplicar una estrategia memorizada sin reconocer por qué sirve para ese cálculo",
        [
            _s("Completar diez", "transformaré una suma formando primero diez", "Para 8+7, separa 2 de 7: 8+2=10 y quedan 5; entonces 15.", "Resuelven sumas con 8 o 9 y registran el traslado que completa diez.", "Calcula 9+6, dibuja el paso por diez y comprueba."),
            _s("Dobles y casi dobles", "usaré un doble conocido para calcular una suma cercana", "Para 7+8 parte de 7+7=14 y agrega uno; contrasta con duplicar 8 y quitar uno.", "Relacionan tarjetas de dobles con sumas uno más o uno menos.", "Resuelve 6+7 usando un doble y explica qué ajustaste."),
            _s("Uno más, uno menos", "compensaré una suma sin cambiar el total", "En 9+5, mueve una unidad: 10+4 conserva 14 porque una parte sube y la otra baja.", "Modelan compensaciones con dos torres y registran pares equivalentes.", "Transforma 8+6 en una suma más fácil y justifica que el total no cambia."),
            _s("Dos más, dos menos", "compensaré por dos cuando facilite el cálculo", "Convierte 8+4 en 10+2 trasladando dos; comprueba con doce fichas.", "Deciden si mover uno o dos en distintos cálculos y explican la elección.", "Calcula 7+5 usando dos más y dos menos; muestra el traslado."),
            _s("Reversibilidad para restar", "usaré una suma conocida para resolver una resta", "Para 15−7 pregunta 7+¿cuánto?=15; construye siete y completa ocho.", "Emparejan sumas y restas de la misma familia y ocultan un término distinto.", "Resuelve 18−9 mediante una suma y verifica ambas operaciones."),
        ],
    ),
    "MA02 OA 07": _oa(
        "Valor posicional de unidades y decenas en números hasta 100", "Números y operaciones",
        "Agrupar objetos en decenas y representar números de dos cifras.",
        "valor posicional, decena, unidad, cifra, canje, posición y cantidad",
        "Palitos y elásticos, bloques base diez, tabla DU, tarjetas de cifras y dinero didáctico.",
        "Realiza físicamente cada canje de diez unidades por una decena y usa una tabla con columnas visibles.",
        "Representa el mismo número con canjes no canónicos y explica el valor de una cifra según su posición.",
        ["agrupa y canjea diez unidades", "interpreta el valor de cada cifra", "conecta material, dibujo y notación posicional"],
        "nombrar la cifra sin considerar que su posición determina su valor",
        [
            _s("Diez unidades forman una decena", "realizaré un canje sin cambiar la cantidad", "Cuenta diez palitos, átalos y registra 10 U = 1 D; vuelve a soltarlos para comprobar.", "Canjean colecciones y registran cuántas decenas y unidades quedan.", "Agrupa 36 objetos y completa: __ decenas y __ unidades."),
            _s("Leer una tabla DU", "ubicaré decenas y unidades en su posición", "Coloca 4 en D y 7 en U para 47; invierte las cifras y construye 74 para contrastar.", "Representan números dictados en tabla y detectan tarjetas mal ubicadas.", "Escribe el número con 6 decenas y 2 unidades y dibuja una comprobación."),
            _s("Valor de una cifra", "explicaré cuánto vale una cifra según su posición", "En 55, el primer 5 vale 50 y el segundo 5 vale 5; representa ambos valores.", "Analizan números repetidos como 22, 66 y 99 y justifican cada posición.", "En 73, ¿cuánto vale el 7? Explica con material o dibujo."),
            _s("Representaciones no canónicas", "mostraré un número con más de una combinación equivalente", "Construye 42 como 4D 2U y después como 3D 12U tras deshacer una decena.", "Realizan canjes inversos y verifican el total con conteo por decenas.", "Representa 58 de dos formas y demuestra que ambas conservan el valor."),
        ],
    ),
    "MA02 OA 08": _oa(
        "Efecto de sumar y restar cero", "Números y operaciones",
        "Interpretar suma como agregar y resta como quitar con colecciones pequeñas.",
        "cero, agregar, quitar, cantidad inicial, cantidad final, identidad y comprobar",
        "Bandejas, fichas, tarjetas de historias, marcos de diez y recta numérica.",
        "Representa cero con una acción visible —no agregar o no retirar— antes de escribir la expresión.",
        "Explica por qué sumar o restar cero mantiene cualquier número y distingue 0−n de n−0.",
        ["representa la acción del cero", "mantiene la cantidad al sumar o restar cero", "distingue el orden en una sustracción"],
        "confundir no hacer un cambio con dejar la respuesta en cero",
        [
            _s("Agregar ninguna unidad", "demostraré qué ocurre al sumar cero", "Hay 14 fichas y se agregan 0: la bandeja sigue con 14; registra 14+0=14.", "Representan historias de suma cero y contrastan con agregar una unidad.", "Dibuja y explica 27+0 sin usar sólo la regla."),
            _s("Quitar ninguna unidad", "demostraré qué ocurre al restar cero", "De 19 cubos se retiran 0; ningún cubo se mueve y quedan 19: 19−0=19.", "Modelan restas de cero y corrigen una respuesta ficticia que obtuvo 0.", "Representa 35−0 y explica la cantidad final."),
            _s("Cero al inicio no es lo mismo", "distinguiré n−0 de 0−n en el ámbito estudiado", "Contrasta 8−0, que deja ocho, con una historia que parte en cero y no permite quitar ocho objetos existentes.", "Clasifican historias posibles, imposibles y distintas según la posición del cero.", "Explica por qué 12−0 y 0−12 no representan la misma acción."),
            _s("Generalizar con evidencia", "formularé una regla sobre sumar y restar cero", "Compara 6+0, 40+0, 83−0 y 100−0 y enuncia una regularidad apoyada en representaciones.", "Prueban la regla con números elegidos por otra pareja y buscan un contraejemplo válido.", "Completa y justifica: __ + 0 = 68 y 91 − __ = 91."),
        ],
    ),
    "MA02 OA 09": _oa(
        "Adición y sustracción hasta 100 mediante problemas, representaciones y algoritmo sin reserva", "Números y operaciones",
        "Resolver adiciones y sustracciones hasta 20 con acciones de agregar, quitar, juntar y comparar.",
        "adición, sustracción, algoritmo, decena, unidad, problema, representación y estimación",
        "Material base diez, tabla DU, recta abierta, tarjetas de problemas y cuaderno cuadriculado.",
        "Identifica la acción del problema antes de escoger operación; alinea unidades y decenas sólo después de representarlas.",
        "Resuelve un mismo problema por dos estrategias y determina cuál hace más visible la comprobación.",
        ["selecciona la operación por el sentido de la situación", "representa y registra sin mezclar posiciones", "estima o usa la operación inversa para comprobar"],
        "elegir operación por una palabra aislada o ejecutar el algoritmo sin comprender la situación",
        [
            _s("Juntar y separar hasta 100", "modelaré acciones de suma y resta con decenas y unidades", "Junta 32 y 25 como 3D+2D y 2U+5U para obtener 57; separa luego 25 y recupera 32.", "Representan pares de historias y explican qué acción indica cada operación.", "Resuelve: había 43 tarjetas y se agregan 24; representa y registra."),
            _s("Recta abierta para avanzar y retroceder", "usaré saltos de decenas y unidades", "Para 46+31 avanza 30 hasta 76 y uno hasta 77; dibuja y rotula cada salto.", "Resuelven sumas y restas con saltos elegidos y comparan descomposiciones.", "Calcula 78−24 con una recta abierta y comprueba los saltos."),
            _s("Algoritmo sin reserva", "registraré unidades y decenas en columnas con significado", "Representa 53+26; alinea 3 con 6 y 5 decenas con 2 decenas antes de sumar 79.", "Traducen material a tabla DU y luego al algoritmo, verbalizando cada columna.", "Resuelve 64−32 con algoritmo y dibuja qué representa cada cifra."),
            _s("Problemas de cambio y comparación", "decidiré si debo sumar o restar según la relación", "Compara 68 y 45 para hallar cuántos más: representa la diferencia 23, no el total 113.", "Clasifican problemas de juntar, quitar, completar y comparar y resuelven uno de cada tipo.", "Sofía tiene 57 láminas y Tomás 31. ¿Cuántas más tiene Sofía? Justifica la operación."),
            _s("Crear, resolver y comprobar", "crearé un problema coherente con una expresión", "Para 72−40 inventa una situación de quitar cuarenta, resuelve 32 y verifica 32+40=72.", "Intercambian expresiones, escriben problemas, revisan coherencia de datos y resuelven.", "Crea un problema para 35+42, resuélvelo y explica una comprobación."),
        ],
    ),
    "MA02 OA 10": _oa(
        "Relación entre adición y sustracción mediante familias de operaciones", "Números y operaciones",
        "Componer y descomponer un todo y usar la reversibilidad en cálculos hasta 20.",
        "familia de operaciones, parte, todo, suma, resta, inversa y comprobar",
        "Triángulos de familia, fichas, diagramas parte-parte-todo y tarjetas con operaciones incompletas.",
        "Mantén tres números visibles en un diagrama y cubre sólo una posición por vez.",
        "Determina cuándo tres números no forman una familia y corrige el miembro que rompe la relación.",
        ["identifica partes y todo", "construye las operaciones relacionadas", "usa una operación para comprobar la inversa"],
        "usar tres números cualquiera o restar una parte de otra en vez de partir del todo",
        [
            _s("Dos partes y un todo", "identificaré los tres números de una familia", "Construye 8 y 5 como partes de 13; ubica 13 en el vértice del todo.", "Forman familias con material y rotulan partes y todo antes de escribir.", "Dibuja el diagrama para 7, 9 y 16 y explica cada posición."),
            _s("Dos sumas relacionadas", "escribiré las adiciones que intercambian las partes", "Desde 6, 4 y 10 registra 6+4=10 y 4+6=10; cambia el orden, no el todo.", "Completan pares de sumas y verifican con el mismo conjunto de fichas.", "Escribe las dos sumas de la familia 12, 25 y 37."),
            _s("Dos restas relacionadas", "partiré del todo para escribir las sustracciones", "Con 15 como todo: 15−7=8 y 15−8=7; ambas recuperan la otra parte.", "Ocultan una parte del diagrama y la hallan con la resta correspondiente.", "Completa la familia de 24, 31 y 55 con sus dos restas."),
            _s("Usar la familia para comprobar", "comprobaré un cálculo con su operación inversa", "Si 63−21=42, verifica 42+21=63; un resultado que no recupera el todo debe revisarse.", "Detectan errores en familias y explican qué operación permite corregirlos.", "Comprueba 48+30=78 mediante una resta y representa la relación."),
        ],
    ),
    "MA02 OA 11": _oa(
        "Multiplicación como grupos iguales y construcción de las tablas del 2, 5 y 10", "Números y operaciones",
        "Contar por agrupaciones y representar adiciones de sumandos iguales.",
        "grupo igual, factor, producto, multiplicación, suma repetida, doble y distributividad",
        "Tapas, vasos, arreglos de puntos, tarjetas de grupos, recta numérica y cuadrícula.",
        "Construye grupos físicamente y nombra cantidad de grupos y elementos por grupo antes del símbolo ×.",
        "Descompone un producto en dos productos conocidos y explica la propiedad distributiva sin exigir su nombre formal.",
        ["construye grupos iguales", "conecta suma repetida y multiplicación", "resuelve y comprueba problemas de 2, 5 o 10"],
        "contar todos los objetos sin reconocer la estructura o invertir factores sin interpretar el contexto",
        [
            _s("Grupos iguales y grupos desiguales", "reconoceré cuándo una colección puede describirse con multiplicación", "Compara cuatro platos con dos fichas cada uno y platos con 2, 3, 2 y 1; sólo el primer caso tiene grupos iguales.", "Construyen ejemplos y no ejemplos y explican qué debe mantenerse.", "Dibuja 3 grupos de 2 y escribe la suma repetida."),
            _s("La tabla del 2 como dobles", "construiré productos por 2 usando dobles", "Cinco parejas son 2+2+2+2+2=10 y 5×2=10; señala las cinco parejas.", "Relacionan dobles con saltos de dos y completan productos faltantes.", "Representa 7×2 y explica cómo un doble ayuda."),
            _s("La tabla del 5", "usaré grupos de cinco y patrones de conteo", "Cuatro manos ficticias con cinco dedos representan 4×5=20; conecta con 5, 10, 15, 20.", "Construyen trenes de cinco, registran productos y observan las unidades 0 o 5.", "Resuelve 6×5 con grupos y una secuencia de múltiplos."),
            _s("La tabla del 10", "multiplicaré por diez mediante decenas completas", "Ocho paquetes de diez son ocho decenas: 8×10=80.", "Emparejan representaciones base diez con productos y explican el cero final desde la cantidad.", "Representa 9×10 y contrasta con 9+10."),
            _s("Distribuir y resolver problemas", "descompondré un producto para usar hechos conocidos", "Para 7×5 separa 5×5 y 2×5: 25+10=35; las partes conservan siete grupos.", "Resuelven problemas de filas, paquetes y turnos con tablas 2, 5 y 10, mostrando la descomposición.", "Hay 8 bolsas con 5 semillas cada una. Resuelve de dos maneras y comprueba el total."),
        ],
    ),
    "MA02 OA 12": _oa(
        "Creación, representación y continuación de patrones numéricos", "Patrones y álgebra",
        "Continuar patrones repetitivos y numéricos sencillos reconociendo una regla.",
        "patrón, regla, término, secuencia, aumentar, disminuir, diferencia y elemento faltante",
        "Tarjetas numéricas, bandas de secuencias, cubos, tabla numérica y cuadrícula.",
        "Marca la transformación entre términos y trabaja con patrones que cambian una sola característica antes de combinarlos.",
        "Crea dos patrones que compartan términos iniciales pero sigan reglas distintas y explica cuándo se separan.",
        ["identifica y expresa la regla", "continúa y completa términos coherentes", "crea una representación que permite verificar"],
        "inferir una regla desde un solo salto o continuar por apariencia sin comprobar todas las diferencias",
        [
            _s("Patrones que aumentan", "describiré una regla aditiva y continuaré la secuencia", "En 12, 17, 22, 27 suma cinco cada vez; verifica todas las diferencias.", "Continúan patrones de +2, +5 y +10 desde distintos inicios.", "Completa 31, 41, __, __ y escribe la regla."),
            _s("Patrones que disminuyen", "continuaré una regla de resta sin cruzar su límite", "En 84, 79, 74, 69 resta cinco y comprueba retrocediendo en la tabla.", "Construyen secuencias descendentes y corrigen saltos que cambiaron la regla.", "Continúa 96, 86, 76, __, __ y explica."),
            _s("Encontrar términos faltantes", "usaré términos vecinos para recuperar un número ausente", "En 24, __, 34 con regla +5, avanza desde 24 y retrocede desde 34 para hallar 29.", "Completan huecos al inicio, medio y final y justifican con dos direcciones.", "Completa __, 42, 47, __ en un patrón de +5."),
            _s("Representar una regla", "mostraré el mismo patrón con objetos, dibujo y números", "Construye torres de 2, 4, 6 y 8 cubos y registra +2 entre alturas.", "Traducen secuencias numéricas a torres o saltos y comparan qué representación hace visible la regla.", "Representa 5, 10, 15, 20 de otra forma y señala la regla."),
            _s("Crear y probar un patrón", "crearé una secuencia con regla inequívoca y la someteré a prueba", "Elige inicio 7 y regla +6: produce 7, 13, 19, 25 y entrega sólo tres términos a otra pareja.", "Crean patrones, intercambian desafíos y revisan si la regla propuesta explica todos los términos.", "Crea cinco términos, oculta uno y escribe una comprobación de la regla."),
        ],
    ),
    "MA02 OA 13": _oa(
        "Igualdad y desigualdad hasta 20 con símbolos =, > y <", "Patrones y álgebra",
        "Comparar cantidades y reconocer distintas descomposiciones de un mismo total.",
        "igualdad, desigualdad, equivalente, mayor que, menor que, expresión y símbolo",
        "Balanza de platillos, fichas, tarjetas de expresiones y símbolos móviles.",
        "Lee cada relación completa en ambos sentidos y verifica con cantidades antes de introducir el símbolo.",
        "Completa desigualdades con más de una solución y determina todos los valores posibles.",
        ["interpreta igualdad como mismo valor", "orienta > y < según los valores", "comprueba ambos lados con una representación"],
        "leer el signo igual como una orden de calcular o orientar > y < por memoria visual",
        [
            _s("Dos expresiones, el mismo valor", "demostraré una igualdad construyendo ambos lados", "Coloca 7+3 en un plato y 6+4 en el otro; ambos valen 10, por eso 7+3=6+4.", "Construyen igualdades con fichas y corrigen casos desequilibrados.", "Decide si 8+5=9+4 y muestra evidencia."),
            _s("El signo igual no siempre termina", "leeré igualdades con una expresión a cada lado", "Contrasta 12=7+5 y 7+5=12; el orden de lectura cambia, el valor no.", "Completan casillas en ambos lados y verbalizan “tiene el mismo valor que”.", "Completa __+6=14 y comprueba ambos lados."),
            _s("Mayor que y menor que", "compararé valores antes de elegir > o <", "Construye 16 y 11, abre el símbolo hacia 16 y lee 16 es mayor que 11; luego lee 11<16.", "Comparan números y expresiones, orientan el símbolo y leen la relación completa.", "Completa 9+4 __ 15 y explica la elección."),
            _s("Valores que hacen verdadera una relación", "buscaré números que satisfacen una igualdad o desigualdad", "Para __+5<12 prueba 0 a 6 y explica por qué 7 ya produce igualdad.", "Encuentran conjuntos de soluciones con material y registran límites.", "Escribe tres valores que hacen verdadero __+8>14 y verifica cada uno."),
        ],
    ),
    "MA02 OA 14": _oa(
        "Posición relativa con derecha e izquierda desde distintos referentes", "Geometría",
        "Describir posiciones con vocabulario espacial desde un referente explícito.",
        "derecha, izquierda, delante, detrás, entre, referente, perspectiva y recorrido",
        "Figuras, cuadrícula de piso, flechas, planos simples y tarjetas de instrucciones.",
        "Marca una mano o lado de referencia y cambia de perspectiva físicamente antes de pedir descripciones simbólicas.",
        "Escribe instrucciones que funcionen para una persona ubicada en otra orientación y prueba su claridad.",
        ["declara el referente", "usa derecha e izquierda coherentemente", "representa o sigue un recorrido verificable"],
        "describir desde la propia perspectiva cuando la consigna exige la perspectiva de otra persona",
        [
            _s("Mi derecha y mi izquierda", "ubicaré objetos respecto de mi propio cuerpo", "Con una cinta en la muñeca derecha, coloca un cono a la derecha y una pelota a la izquierda.", "Siguen y formulan instrucciones corporales sin copiar el movimiento del docente como espejo.", "Dibuja un objeto a tu derecha y otro a tu izquierda y rotula."),
            _s("Posición respecto de un objeto", "describiré dónde está algo usando un referente externo", "Ubica el lápiz a la izquierda del libro y relee desde el libro como referente.", "Construyen escenas y producen dos descripciones equivalentes desde referentes distintos.", "En un dibujo, describe la posición del círculo respecto del cuadrado."),
            _s("Cambiar de perspectiva", "explicaré cómo cambia derecha e izquierda al girar", "Dos personajes se miran: la derecha de uno queda frente a la izquierda del otro; compruébalo con figuras orientadas.", "Rotan figuras en cuadrícula y anticipan antes de comprobar qué lado cambia.", "Un personaje gira media vuelta: marca su nueva derecha y explica."),
            _s("Dar y seguir un recorrido", "usaré instrucciones espaciales para llegar a una meta", "Desde una flecha inicial avanza dos, gira a la derecha y avanza uno; dibuja cada cambio de orientación.", "En parejas diseñan recorridos, los ejecutan y corrigen instrucciones ambiguas.", "Escribe un recorrido de tres pasos desde A hasta B usando derecha o izquierda."),
        ],
    ),
    "MA02 OA 15": _oa(
        "Descripción, comparación y construcción de figuras 2D", "Geometría",
        "Reconocer figuras 2D por atributos y no sólo por apariencia global.",
        "figura 2D, lado, vértice, recto, curvo, triángulo, cuadrado, rectángulo y círculo",
        "Palitos, lana, geoplano opcional, recortes de figuras variadas y papel cuadriculado.",
        "Incluye figuras rotadas y de distintos tamaños; permite recorrer bordes de forma visual o táctil.",
        "Construye figuras que cumplan restricciones y explica cuáles condiciones pueden coexistir.",
        ["describe atributos observables", "clasifica sin depender de orientación o tamaño", "construye una figura que cumple condiciones"],
        "reconocer una figura sólo cuando coincide con el prototipo habitual",
        [
            _s("Lados y vértices", "describiré figuras por cantidad de lados y vértices", "Recorre un triángulo rotado: tres segmentos se encuentran en tres vértices aunque no apunte hacia arriba.", "Clasifican figuras por atributos y separan ejemplos de no ejemplos.", "Dibuja una figura de cuatro lados y marca sus vértices."),
            _s("Cuadrados y rectángulos", "compararé cuadrados y rectángulos usando sus lados", "Superpone un cuadrado y un rectángulo: ambos tienen cuatro lados, pero en el cuadrado los cuatro son iguales.", "Construyen ambos con palitos y registran semejanzas y diferencias.", "Explica por qué un cuadrado no deja de serlo al girarlo."),
            _s("Círculos y bordes curvos", "distinguiré bordes curvos de lados rectos", "Compara un círculo con una figura de muchos lados: el círculo tiene borde curvo continuo y no vértices.", "Trazan, recortan y clasifican figuras atendiendo al tipo de borde.", "Selecciona el círculo entre figuras parecidas y justifica por su borde."),
            _s("Construir con restricciones", "crearé una figura 2D que cumpla criterios", "Construye una figura cerrada con cuatro lados, dos largos y dos cortos; comprueba cada condición.", "Resuelven tarjetas de construcción y revisan trabajos con una lista de atributos.", "Construye o dibuja una figura con tres lados que no esté apoyada en una base horizontal."),
        ],
    ),
    "MA02 OA 16": _oa(
        "Descripción, comparación y construcción de figuras 3D", "Geometría",
        "Reconocer cuerpos por superficies, caras y comportamiento al rodar o apilar.",
        "figura 3D, cara, superficie curva, arista, vértice, cubo, paralelepípedo, esfera y cono",
        "Cajas, cubos, pelotas, conos de papel, plasticina, palitos y redes simples.",
        "Permite manipulación y exploración táctil; compara un atributo por vez y separa nombre cotidiano de nombre geométrico.",
        "Diseña una construcción estable con dos tipos de cuerpos y explica cómo sus superficies influyen.",
        ["describe superficies y partes", "compara cuerpos mediante atributos", "construye o selecciona un cuerpo que cumple criterios"],
        "clasificar por el objeto cotidiano que se parece al cuerpo en vez de observar sus atributos",
        [
            _s("Rodar, deslizar y apilar", "investigaré cómo las superficies influyen en el movimiento", "Prueba cubo, esfera y cono en una rampa: la superficie curva permite rodar, pero no todos ruedan igual.", "Realizan pruebas controladas y registran qué cuerpos ruedan, se deslizan o se apilan.", "Predice y comprueba qué hará un paralelepípedo en una rampa."),
            _s("Caras y superficies", "describiré cuerpos mediante caras planas y superficies curvas", "Cuenta seis caras cuadradas en un cubo y contrasta con la superficie curva continua de una esfera.", "Exploran cuerpos, calcan caras posibles y completan una tabla de atributos.", "Describe un cono sin decir su nombre para que otra persona lo identifique."),
            _s("Cubo y paralelepípedo", "compararé dos cuerpos de seis caras", "Observa que ambos tienen seis caras; en el cubo todas son cuadrados iguales, en una caja rectangular no.", "Construyen esqueletos o modelos y buscan semejanzas y diferencias.", "Explica una diferencia comprobable entre un cubo y un paralelepípedo."),
            _s("Construir un cuerpo", "construiré una figura 3D desde criterios", "Une seis cuadrados iguales como red y pliega un cubo; verifica que no falte ni se superponga una cara.", "Construyen con plasticina, palitos o redes y contrastan el resultado con una tarjeta de atributos.", "Elige materiales para construir un cono o cubo y justifica la elección."),
        ],
    ),
    "MA02 OA 17": _oa(
        "Lectura de días, semanas, meses y fechas en el calendario", "Medición",
        "Ordenar días y meses y ubicar fechas significativas en un calendario.",
        "día, semana, mes, fecha, calendario, anterior, posterior, fila y columna",
        "Calendarios mensuales y anuales, tarjetas de fechas ficticias, marcadores y línea temporal.",
        "Fija año y mes antes de leer un número; usa calendarios grandes y eventos ficticios o públicos para proteger privacidad.",
        "Calcula fechas a una o más semanas y explica cuándo cambia el mes o el año.",
        ["localiza una fecha completa", "relaciona días dentro de semanas y meses", "calcula desplazamientos en el calendario"],
        "leer sólo el número del día sin considerar mes, año o posición semanal",
        [
            _s("Partes de un calendario", "identificaré mes, semana, día y fecha", "En abril de un año dado señala encabezado, columnas de días y casilla 18; una fecha necesita día y mes.", "Exploran calendarios distintos y responden preguntas de localización.", "Ubica el segundo martes del mes y escribe su fecha completa."),
            _s("Una semana después", "avanzaré y retrocederé siete días", "Desde miércoles 6 baja una fila para llegar al miércoles 13; explica por qué conserva el día semanal.", "Resuelven desplazamientos de una y dos semanas y comprueban contando siete.", "Si una actividad es el lunes 10, ¿qué fecha será una semana después?"),
            _s("Cruzar el fin de mes", "calcularé fechas cuando cambia el mes", "Desde 29 de mayo avanza cuatro días: 30, 31, 1 y 2 de junio; no continúa con 32.", "Usan calendarios consecutivos para resolver intervalos cortos que cruzan mes o año.", "Tres días después del 30 de noviembre, ¿qué fecha es? Muestra el recorrido."),
            _s("Planificar con fechas", "usaré un calendario para ordenar eventos", "Ubica tres actividades ficticias, decide cuál ocurre primero y calcula cuántos días separan dos de ellas.", "Crean una agenda segura del curso con eventos públicos y justifican el orden.", "Ordena 12 de agosto, 29 de julio y 3 de agosto y explica tu criterio."),
        ],
    ),
    "MA02 OA 18": _oa(
        "Lectura de horas y medias horas en relojes digitales", "Medición",
        "Relacionar momentos del día con secuencias temporales y duración aproximada.",
        "hora, media hora, reloj digital, dos puntos, antes, después y duración",
        "Relojes digitales de cartón, tarjetas de horarios, líneas de tiempo y agendas ficticias.",
        "Separa visualmente horas y minutos y relaciona :00 con hora exacta y :30 con media hora.",
        "Determina horarios posibles bajo dos restricciones y explica más de una solución.",
        ["lee correctamente :00 y :30", "ubica horarios en orden temporal", "resuelve problemas de media hora con una línea de tiempo"],
        "leer 8:30 como ocho treinta unidades sin relacionarlo con media hora",
        [
            _s("Horas exactas en formato digital", "leeré y escribiré horas terminadas en :00", "Muestra 09:00: a la izquierda está la hora nueve y :00 indica que comienza esa hora.", "Emparejan relojes digitales con tarjetas de actividades ficticias.", "Escribe en formato digital las cuatro en punto y explica el :00."),
            _s("Media hora", "interpretaré :30 como media hora después", "Desde 10:00 avanza treinta minutos hasta 10:30; aún no son las once.", "Ordenan pares :00/:30 y construyen una línea con saltos de media hora.", "¿Qué hora marca 7:30 y cuál viene media hora después?"),
            _s("Ordenar horarios", "compararé horas y medias horas del mismo día", "Ordena 08:30, 09:00 y 09:30 mirando primero la hora y luego los minutos.", "Organizan agendas ficticias y detectan dos actividades superpuestas.", "Ordena 12:30, 11:30, 12:00 y explica el primer criterio usado."),
            _s("Problemas de media hora", "resolveré cambios de horario de treinta minutos", "Una actividad empieza 15:30 y termina media hora después: avanza a 16:00 en la línea temporal.", "Resuelven inicios y finales con uno o dos saltos de media hora.", "Un taller termina a las 18:30 y duró media hora. ¿A qué hora comenzó? Representa."),
        ],
    ),
    "MA02 OA 19": _oa(
        "Medición de longitudes con unidades no estandarizadas, centímetros y metros", "Medición",
        "Comparar longitudes y medir con una unidad repetida sin espacios ni superposiciones.",
        "longitud, unidad, centímetro, metro, regla, cinta, extremo, estimar y medir",
        "Clips iguales, tiras de papel, reglas, cintas métricas, objetos del aula y tablas de registro.",
        "Alinea el cero con el extremo y permite exploración táctil; elige objetos compatibles con la unidad usada.",
        "Analiza el error producido por comenzar en otra marca o por usar unidades de distinto tamaño.",
        ["elige una unidad adecuada", "itera la unidad sin huecos ni traslapes", "registra número y unidad y contrasta con una estimación"],
        "anotar sólo un número o comenzar a medir desde el borde físico de una regla dañada en vez del cero",
        [
            _s("Repetir una unidad informal", "mediré una longitud con unidades iguales", "Cubre un libro con clips idénticos desde un extremo, sin huecos: mide 9 clips, no sólo 9.", "Miden objetos con tiras o clips y comparan por qué la unidad debe mantenerse.", "Mide una tarjeta con una unidad informal y registra cantidad y unidad."),
            _s("Leer centímetros en una regla", "alinearé el cero y leeré la marca final", "Coloca un lápiz desde 0 hasta 14 cm; contrasta con comenzar en 1 y leer 15 sin calcular la diferencia.", "Miden trazos y objetos, revisando inicio, dirección y unidad.", "Dibuja un segmento de 8 cm y explica dónde comenzó tu medición."),
            _s("Elegir centímetros o metros", "seleccionaré una unidad estandarizada adecuada", "Para un cuaderno usa cm; para el largo de la sala, metros evitan cientos de repeticiones pequeñas.", "Clasifican objetos según unidad conveniente y luego comprueban una selección.", "¿Medirías una puerta en cm o m? Justifica y estima antes de medir."),
            _s("Estimar, medir y comparar", "usaré una estimación para evaluar mi medida", "Estima una mesa en 1 m y mide 1 m 20 cm; explica por qué 12 m sería poco razonable.", "Registran estimación, medida real y diferencia en estaciones.", "Estima y mide un objeto; comunica el resultado con unidad y una comparación."),
        ],
    ),
    "MA02 OA 20": _oa(
        "Recolección y registro de datos en juegos con monedas y dados", "Datos y probabilidades",
        "Formular preguntas estadísticas, registrar una respuesta por caso y leer pictogramas simples.",
        "dato, resultado, ensayo, aleatorio, conteo, frecuencia, tabla y pictograma",
        "Monedas didácticas, dados, bloques, tablas de conteo, pictogramas y bandejas para lanzar.",
        "Usa material grande o digital accesible y pocos ensayos al inicio; distingue predicción de resultado observado.",
        "Compara dos series de ensayos y explica por qué no tienen que producir exactamente las mismas frecuencias.",
        ["registra cada ensayo una sola vez", "organiza frecuencias coherentes con los resultados", "responde una pregunta citando datos"],
        "cambiar o completar resultados para que coincidan con lo que se esperaba",
        [
            _s("Resultados posibles", "identificaré qué puede ocurrir antes de jugar", "Una moneda didáctica tiene cara y sello: registra ambos como posibles sin afirmar cuál saldrá.", "Enumeran resultados de monedas y dados y separan posible de observado.", "Escribe los resultados posibles de un dado y marca uno imposible."),
            _s("Un registro por lanzamiento", "registraré cada ensayo sin omitir ni duplicar", "Lanza una moneda diez veces y mueve una ficha de pendiente a registrado tras cada marca.", "Realizan series breves con roles rotativos de lanzar, observar y registrar.", "Registra ocho resultados dados y comprueba que las frecuencias suman ocho."),
            _s("De marcas a bloques y pictograma", "representaré las frecuencias de un juego", "Convierte 6 caras y 4 sellos en dos torres y luego en un pictograma con una imagen por resultado.", "Traducen tablas de conteo a representaciones y verifican cada categoría.", "Construye un pictograma para 3 unos, 5 doses y 2 treses."),
            _s("Responder sin predecir de más", "sacaré conclusiones válidas de los datos observados", "Si salió cara 7 veces y sello 3, afirma qué ocurrió en esos diez ensayos, no qué saldrá siempre.", "Distinguen conclusiones sustentadas de generalizaciones y citan frecuencias.", "Escribe una conclusión verdadera sobre una tabla de lanzamientos y una afirmación que los datos no permiten."),
        ],
    ),
    "MA02 OA 21": _oa(
        "Registro de resultados aleatorios en tablas y gráficos de barra simple", "Datos y probabilidades",
        "Recolectar datos de juegos y organizar frecuencias en tablas y pictogramas.",
        "tabla, categoría, frecuencia, eje, escala, barra, título y resultado aleatorio",
        "Dados, monedas didácticas, papel cuadriculado, reglas, bloques y plantillas de gráfico.",
        "Mantén categorías y escala visibles; permite construir barras con bloques antes de dibujarlas.",
        "Compara gráficos correctos e engañosos y explica cómo la escala o desalineación altera la lectura.",
        ["traslada frecuencias sin modificarlas", "construye barras desde una línea base común", "incluye título, categorías y escala legibles"],
        "dibujar barras por impresión visual sin conservar la frecuencia ni la línea base",
        [
            _s("Tabla de resultados", "organizaré resultados aleatorios por categoría", "Registra doce lanzamientos de dado en filas 1 a 6 y comprueba que la suma de frecuencias sea doce.", "Transforman listas desordenadas en tablas y localizan omisiones.", "Completa una tabla desde diez resultados y verifica el total."),
            _s("Barras concretas", "construiré un gráfico con bloques desde una tabla", "Para frecuencias 2, 5 y 3, levanta torres desde la misma base y deja igual separación.", "Construyen gráficos concretos y los comparan con la tabla fuente.", "Representa 4, 1 y 6 con barras de bloques y rotula categorías."),
            _s("Gráfico de barra en cuadrícula", "dibujaré barras simples con escala de uno", "Marca eje, categorías y escala; una frecuencia 7 ocupa exactamente siete cuadros desde cero.", "Pasan gráficos concretos a papel y hacen revisión cruzada fila por fila.", "Dibuja un gráfico para una tabla dada e incluye título y escala."),
            _s("Leer y criticar un gráfico", "interpretaré frecuencias y detectaré representaciones engañosas", "Compara dos barras que parten en alturas distintas: aunque ambas dicen 5, la base desplazada engaña.", "Responden máximo, mínimo, total y diferencia y corrigen un gráfico defectuoso.", "Explica dos errores de un gráfico y redibuja una barra correctamente."),
        ],
    ),
    "MA02 OA 22": _oa(
        "Construcción e interpretación de pictogramas con escala y gráficos de barra simple", "Datos y probabilidades",
        "Leer pictogramas de una imagen por dato y construir gráficos de barra con escala uno.",
        "pictograma, símbolo, clave, escala, barra, frecuencia, diferencia y total",
        "Tablas de datos, símbolos recortables, cuadrículas, reglas y gráficos correctos e incorrectos.",
        "Destaca la clave y permite marcar cada símbolo; inicia con escala 2 antes de incorporar otras escalas simples.",
        "Representa los mismos datos con pictograma y barras y evalúa qué preguntas se leen mejor en cada formato.",
        ["aplica la clave a cada símbolo", "construye una representación fiel a la tabla", "interpreta comparaciones, totales y diferencias"],
        "contar símbolos sin multiplicar por la escala o tratar medio símbolo sin una convención explícita",
        [
            _s("Leer una clave de dos", "convertiré símbolos en frecuencias usando la escala", "Si cada estrella vale 2 votos, cuatro estrellas representan 8; señala 2+2+2+2 antes de multiplicar.", "Leen pictogramas con clave 2 y completan una tabla de frecuencias.", "Tres bicicletas representan dos viajes cada una: ¿cuántos viajes son? Explica."),
            _s("Comparar con escala", "calcularé diferencias entre categorías representadas", "Cinco símbolos frente a tres con clave 2 difieren en dos símbolos, es decir cuatro datos.", "Resuelven máximo, mínimo, diferencia y total sin olvidar la clave.", "Con clave 5, una fila tiene 6 símbolos y otra 4: ¿cuál es la diferencia?"),
            _s("Construir un pictograma", "transformaré una tabla en símbolos respetando la clave", "Para 4, 8 y 6 con clave 2 dibuja 2, 4 y 3 símbolos; comprueba multiplicando.", "Eligen una clave compatible, construyen y revisan cada fila contra la tabla.", "Construye dos filas para frecuencias 10 y 6 con clave 2."),
            _s("Pasar a gráfico de barras", "representaré los mismos datos en barras", "Convierte frecuencias 6, 10 y 4 a barras desde cero; la altura muestra frecuencia, no cantidad de símbolos previos.", "Construyen gráficos desde pictogramas y comparan títulos, categorías y escala.", "Dibuja las barras que corresponden a un pictograma con clave 2."),
            _s("Interpretar y elegir representación", "compararé pictograma y gráfico para comunicar una conclusión", "Con los mismos datos, usa el pictograma para ver unidades agrupadas y las barras para comparar alturas desde una base común.", "Responden preguntas, justifican qué formato facilita cada lectura y corrigen una conclusión falsa.", "Elige una representación para mostrar qué categoría tiene mayor frecuencia y defiende tu elección con datos."),
        ],
    ),
}


for _code, _data in SEQUENCES.items():
    _number = int(_code.rsplit(" ", 1)[-1])
    _data["source"] = f"https://www.curriculumnacional.cl/curriculum/1o-6o-basico/matematica/2-basico/ma02-oa-{_number:02d}"


def build_math_sequence(code: str) -> dict | None:
    data = SEQUENCES.get(code)
    if not data:
        return None
    oa_number = int(code.rsplit(" ", 1)[-1])
    lessons = []
    for index, step in enumerate(data["stages"]):
        lessons.append({
            "title": step["title"],
            "purpose": f"Construir comprensión de {data['topic'].lower()} mediante «{step['title'].lower()}», conectando representación, estrategia y comprobación.",
            "goal": f"Hoy {step['goal']}.",
            "opening": f"Presenta sin resolver el desafío de cierre: {step['ticket']} Cada estudiante registra una primera representación y una estimación; conserva dos caminos distintos para retomarlos.",
            "model": step["model"],
            "guided": step["guided"] + " El docente pregunta qué representa cada objeto, trazo o número y hace corregir la idea, no sólo el resultado.",
            "independent": step["ticket"] + " Luego resuelve un caso equivalente con datos nuevos y sin copiar la demostración.",
            "ticket": step["ticket"],
            "materials": data["materials"],
            "support": data["support"],
            "extension": data["extension"],
            "evidence": step["ticket"] + " acompañada de una representación y una comprobación atribuibles al estudiante.",
            "criteria": data["criteria"],
            "next_step": "Avanza cuando la representación, el resultado y la explicación coinciden; si no, identifica si el nudo está en el concepto, la traducción o la comprobación y reenseña con otro ejemplo.",
            "short_version": "Conserva el ejemplo específico, una práctica guiada, el desempeño individual y el ticket; reduce la cantidad de casos, no la representación ni la explicación.",
            "home_task": "Busca o inventa una situación cotidiana pequeña que use la idea matemática de la clase, represéntala con objetos seguros o dibujo y registra una comprobación. No requiere internet, impresión ni compras.",
            "complementary": [
                "Recuperación: reduce el rango numérico o la cantidad de condiciones, conserva la misma relación y vuelve luego al caso original.",
                f"Análisis de error: corrige un caso ficticio basado en esta confusión frecuente: {data['misconception']}.",
                "Profundización: cambia un dato o una condición, predice el efecto y comprueba antes de aceptar el resultado.",
            ],
            "difficulty_actions": [
                {"signal": "Inicia un cálculo sin representar la situación", "action": "Pide identificar datos, relación y pregunta; exige una representación breve antes de operar.", "check": "La operación elegida coincide con la relación representada."},
                {"signal": data["misconception"].capitalize(), "action": data["support"], "check": "Resuelve un caso nuevo sin repetir la confusión y explica la diferencia."},
                {"signal": "Entrega un resultado sin comprobar", "action": "Solicita estimación, operación inversa, segunda representación o sustitución según el OA.", "check": "La comprobación permite confirmar o corregir el resultado de manera independiente."},
            ],
            "specialist_coordination": "El docente conduce el razonamiento matemático y registra la estrategia; educación diferencial acuerda acceso a representaciones, manipulación, campo visual o respuesta oral sin entregar el procedimiento ni reducir el OA.",
            "transversal": transversal_links(oa_number, index, step["goal"]),
        })
    return {
        "topic": data["topic"],
        "pedagogical_explanation": f"{data['topic']} exige coordinar significado, representación y comprobación. La secuencia evita {data['misconception']} y progresa desde experiencias visibles hacia decisiones simbólicas justificadas.",
        "prerequisites": data["prior"],
        "vocabulary": data["vocabulary"],
        "official_alignment": {
            "units": [f"Eje {data['axis']} · organización interna en {len(data['stages'])} clases"],
            "unit_origin": "Organización interna derivada del eje y del OA; no se presenta como unidad oficial del programa de estudio.",
            "indicators": [step["goal"].capitalize() + "." for step in data["stages"][:3]],
            "indicator_origin": "Criterios de progresión internos derivados del verbo, contenido y rango del OA oficial",
            "source": data["source"],
        },
        "lessons": lessons,
    }


def build_transversal_integration(item: dict) -> dict:
    """Materialize second-grade math skills/attitudes as integrated experiences."""
    clean_oa = item["oa_text"].split("Unidad de Currículum", 1)[0].strip().rstrip(".")
    lessons = []
    for index, (phase, focus) in enumerate(item["phases"], 1):
        lessons.append({
            "title": f"Integrar {item['oa_code']}: evidencia {index}",
            "purpose": f"Integrar «{clean_oa}» dentro de una clase de contenido matemático, sin enseñarlo como bloque aislado.",
            "goal": f"Hoy mostraré {clean_oa.lower()} mientras resuelvo, represento y compruebo un problema.",
            "opening": f"Presenta dos respuestas ficticias a un problema de 2° básico: una hace visible «{focus}» y otra no. El curso identifica evidencia observable, no rasgos personales.",
            "model": f"Piensa en voz alta durante un problema breve y señala el momento exacto en que se manifiesta «{clean_oa}». Contrasta una acción aparente con una evidencia auténtica.",
            "guided": "Resuelven un caso de números, geometría, medición o datos; se detienen una vez para nombrar la estrategia, representación o actitud y recibir retroalimentación específica.",
            "independent": "Cada estudiante resuelve un caso corto de contenido, marca dónde aplicó la habilidad o actitud y conserva su representación para revisión.",
            "ticket": f"Muestra una evidencia matemática individual de «{focus}» y explica qué decisión permitió producirla.",
            "materials": "Problema breve de contenido, material concreto pertinente, hoja de registro y tarjeta con la habilidad o actitud en lenguaje accesible.",
            "support": "Ofrece una representación y una frase inicial para explicar; mantiene la decisión matemática y evita evaluar rapidez, obediencia o personalidad.",
            "extension": "Compara dos estrategias o cambia una condición del problema y explica cómo la habilidad o actitud mejora la nueva solución.",
            "evidence": "Resolución de contenido con una marca y explicación del momento en que se aplicó la habilidad o actitud.",
            "criteria": ["resuelve contenido matemático pertinente", "hace observable la habilidad o actitud", "explica una decisión o revisión"],
            "next_step": "Integra nuevamente el OA transversal en otra secuencia si la evidencia depende del apoyo; diversifica el contexto cuando aparece con autonomía.",
            "short_version": "Conserva problema de contenido, decisión observable, evidencia individual y ticket; elimina repetición, no la integración.",
            "home_task": "Explica con un ejemplo pequeño cómo la habilidad o actitud ayudó a resolver o revisar; puede hacerse oralmente o con dibujo y no requiere materiales comprados.",
            "complementary": ["Clasificar evidencias y no evidencias del OA transversal.", "Corregir una solución que oculta su estrategia.", "Transferir la habilidad o actitud a otro eje matemático."],
            "difficulty_actions": [
                {"signal": "Nombra la habilidad, pero no la usa", "action": "Pide señalar una acción concreta dentro de la resolución.", "check": "La producción contiene una evidencia localizable."},
                {"signal": "La actitud se confunde con conducta general", "action": "Vincula la retroalimentación a una decisión matemática, revisión o escucha de estrategia.", "check": "Describe qué hizo y cómo afectó la solución."},
                {"signal": "La integración desplaza el contenido", "action": "Recupera la pregunta matemática y usa el OA transversal como medio para resolverla.", "check": "El ticket demuestra contenido y transversalidad."},
            ],
            "specialist_coordination": "El docente mantiene el OA matemático como foco; los apoyos observan la misma habilidad o actitud en vías de respuesta accesibles, sin convertirla en diagnóstico ni calificación conductual.",
        })
    return {"generated_for": "2-basico", "lessons": lessons}
