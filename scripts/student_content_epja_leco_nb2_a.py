"""Lenguaje y Comunicación EPJA Nivel 2, módulo 1 (parte 1): OAD-01, caracterizar el cuento como género narrativo comparando y seleccionar el preferido. Todos los textos son inventados y se leen en papel."""
from __future__ import annotations

from epja_leco_nb2_common import build

O = "EPJA-LECO-NB2-OAD-01"

F1 = ("Texto 1 (inventado), cuento «La llave perdida»: Marta abrió la panadería a las seis, como todos los días. Buscó la llave del horno y no estaba. "
      "Revisó el delantal, el cajón y la bolsa del pan. Por fin la encontró dentro de un guante, sobre la mesa. Se rio, se puso el guante y encendió el horno. "
      "Texto 2 (inventado), aviso: La feria de la plaza abre desde las nueve. Hay puestos de verduras y de pan. Se pide llegar con bolsa propia. "
      "Texto 3 (inventado), poema: La lluvia llega despacio / y canta sobre el tejado; / yo la escucho desde adentro, / tranquilo, con el pan tostado. "
      "Texto 4 (inventado), escena de teatro: MARTA: ¿Viste la llave del horno? / LUIS: La dejaste en la mesa, dentro de un guante.")

F2 = ("Cuento (inventado), «El paraguas de don Hugo»: Una tarde de invierno, don Hugo esperaba el bus en la parada de la avenida. Llovía fuerte y su paraguas tenía un roto. "
      "Una joven que esperaba a su lado le ofreció compartir el suyo. Caminaron juntos hasta la esquina, conversando de la lluvia. "
      "Cuando llegó el bus, la joven le dijo: «Mañana le traigo su paraguas arreglado; trabajo en un taller de costura». Don Hugo sonrió y subió al bus.")

F3 = ("Cuento A (inventado), «El reloj de la feria»: Rita vendía relojes usados en la feria. Un domingo, un cliente le devolvió uno que se atrasaba. "
      "Rita lo abrió con paciencia, limpió el mecanismo y lo dejó andando. A la semana siguiente, el cliente volvió con otro reloj para arreglar. "
      "Cuento B (inventado), «El corte de luz»: Una noche se cortó la luz en el edificio. Los vecinos salieron a la escalera, asustados. "
      "Don Sergio trajo una linterna y la señora Elena, otra. Subieron juntos a revisar el tablero y vieron que solo había saltado un interruptor. "
      "Lo levantaron y la luz volvió. Esa noche se quedaron conversando en la escalera.")

F4 = ("Cuento C (inventado), «El ascensor detenido»: Martina subía en el ascensor del consultorio cuando este se detuvo entre dos pisos. Se asustó, pero recordó que había un botón de ayuda. "
      "Lo apretó y una voz le pidió que esperara tranquila. Cinco minutos después las puertas se abrieron. Martina respiró hondo y salió al pasillo. "
      "Cuento D (inventado), «La carta de la señora Rosa»: La señora Rosa escribió una carta para su hermano, que vivía lejos. Le contó cómo crecían los tomates de su huerta. "
      "Fue al correo, pero estaba cerrado por feriado. Volvió el martes y despachó la carta. Dos semanas después llegó la respuesta, con una foto de la huerta de su hermano.")

F5 = ("Cuento 1 (inventado), «Un día de lluvia en la terminal»: tiempo de lectura en voz alta, 2 minutos. Un paraguas gigante se abre solo con el viento y rueda por el andén; los pasajeros corren tras él entre risas hasta que un guardia lo atrapa. "
      "Cuento 2 (inventado), «La huerta del pasaje»: tiempo de lectura, 6 minutos. Los vecinos de un pasaje angosto convierten un sitio vacío en huerta. Al principio discuten, luego se turnan para regar y en primavera reparten lechugas entre todos. "
      "Cuento 3 (inventado), «El turno de noche»: tiempo de lectura, 3 minutos. Raúl termina su turno en la bodega y oye un golpe al fondo. Camina despacio con una linterna y descubre un gato atrapado entre las cajas; lo libera y el gato se va.")

F6 = ("Texto 1 (inventado), cuento «La bolsa de pan»: Cada viernes, Ema compraba pan para la reunión del grupo. Ese viernes la panadería estaba cerrada y Ema no tenía nada que llevar. "
      "Entonces recordó que tenía harina y levadura en casa. Amasó, esperó y horneó unos panes sencillos. Cuando los llevó, todos preguntaron quién los había hecho. "
      "Texto 2 (inventado), poema «Pan»: Pan tibio, pan de mañana, / olor que llena la casa, / ventana que se despierta / con el vapor de la masa.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy reconozco qué es un cuento entre otros textos que leo a diario y recuerdo cuentos que ya conozco.",
    prior=["Leo textos cortos: avisos, mensajes, historias.", "He escuchado cuentos contados por otras personas.", "Sé decir de qué trata un texto."],
    explain=[
        "Tú ya conoces muchos cuentos: los que se cuentan en una reunión, los que escuchaste de otras personas y los que viste escritos. Un cuento es una historia breve, inventada, en la que les pasan cosas a uno o más personajes.",
        "Los textos se agrupan en géneros literarios. La narrativa cuenta hechos que les ocurren a personajes, y el cuento es una de sus formas. La poesía usa versos para expresar lo que siente quien habla. El texto dramático se escribe para que personas lo representen: cada una dice sus palabras.",
        "Un aviso, una receta o una noticia no son literatura: informan. Para reconocer un cuento, pregúntate: ¿hay personajes?, ¿les pasan cosas en un orden?, ¿alguien las cuenta? Si las tres respuestas son sí, es narrativa.",
    ],
    vocab=[("género literario", "grupo de textos que se parecen: narrativa, poesía o texto dramático"), ("cuento", "historia breve y inventada, con personajes y hechos"), ("personaje", "quien actúa en una historia"), ("verso", "cada línea de un poema")],
    worked=[
        ("Reconocer un cuento", "Fragmento (inventado): «Doña Clara cerró el kiosco, contó las monedas y se fue a casa bajo la lluvia.»", ["Busco personajes: aparece doña Clara.", "Busco hechos en orden: cierra, cuenta, se va.", "Alguien lo cuenta: sí."], "Es narrativo: cuenta hechos de un personaje"),
        ("Distinguir un aviso", "Texto (inventado): «Se arrienda pieza; incluye agua y luz; consultar por la tarde».", ["No hay personajes que actúen.", "No cuenta hechos en orden: da información."], "No es un cuento; informa"),
    ],
    mistakes=[("Pensar que todo texto con la palabra «pan» es el mismo género.", "El género no depende del tema, sino de cómo está escrito el texto.", "Mira si hay personajes, hechos, versos o diálogos."),
              ("Creer que un texto corto siempre es un poema.", "El largo no define el género: un cuento puede ser muy breve.", "Un poema se reconoce por sus versos y por lo que expresa quien habla.")],
    T=[
        ("abc", "{F} ¿Cuál de los textos es un cuento?", "El Texto 1, porque cuenta hechos que le pasan a Marta", "El Texto 2, porque habla de pan", "El Texto 3, porque nombra el pan tostado", "Solo el Texto 1 cuenta hechos en orden que le ocurren a un personaje."),
        ("ab", "{F} ¿Quién es la persona que actúa en el Texto 1?", "Marta", "El horno", "Marta busca y encuentra la llave; el horno es un objeto."),
        ("{F} ¿A qué hora abrió Marta la panadería? Escribe solo el número.", "6", "El Texto 1 dice que abrió a las seis."),
        ("abc", "{F} ¿Qué texto informa sin contar una historia?", "El Texto 2, el aviso de la feria", "El Texto 1, el cuento", "El Texto 4, la escena", "El aviso da datos de la feria y no tiene personajes que actúen."),
        ("abc", "{F} ¿Qué hace que el Texto 3 sea un poema?", "Está escrito en versos y expresa lo que siente quien habla", "Cuenta hechos con personajes en orden", "Da instrucciones para llegar a la feria", "El poema usa versos y expresa una vivencia, no cuenta una historia."),
        ("ab", "{F} ¿Qué texto se escribió para que personas lo representen hablando?", "El Texto 4, porque cada intervención empieza con el nombre de quien habla", "El Texto 1, porque tiene un personaje", "El texto dramático marca quién habla; el cuento tiene un narrador."),
        ("abc", "Lee este fragmento (inventado): «Ayer Tomás perdió el bus. Corrió por la calle, pero el bus ya se iba. Entonces decidió caminar hasta el trabajo.» ¿Qué género es?", "Narrativo", "Poesía", "Texto dramático", "Cuenta hechos en orden que le pasan a un personaje."),
        ("abc", "Lee este fragmento (inventado): «PEDRO: ¿Vienes a la reunión? / ROSA: Sí, llego a las ocho.» ¿Qué género es?", "Texto dramático", "Poesía", "Aviso informativo", "Cada línea marca quién habla, como en una obra para representar."),
        ("Un texto dice: «Se vende pan amasado, ocho unidades por mil pesos (precio de ejemplo)». ¿Es un cuento? Responde sí o no.", "no", "Es un aviso de venta: informa y no cuenta hechos de personajes."),
        ("ab", "Lucía dice que el Texto 2 es un cuento porque nombra pan, igual que el Texto 1. ¿Tiene razón?", "No: un cuento se reconoce por sus personajes y hechos, no por las palabras que repite", "Sí: dos textos que nombran lo mismo son del mismo género", "El género depende de cómo se escribe el texto, no del tema."),
        ("abc", "{F} ¿Qué tienen en común los Textos 1 y 4?", "Ambos tratan de la llave del horno, pero uno es cuento y el otro es escena de teatro", "Ambos son poemas porque son cortos", "Ambos son avisos porque nombran un lugar", "Comparten el asunto, pero se escriben de distinto modo."),
        ("abc", "¿Cuál de estos textos podría ser el inicio de un cuento?", "«Una mañana de lluvia, Rosa perdió el sobre con sus papeles y volvió corriendo a buscarlo.»", "«Los documentos deben entregarse en la ventanilla 3 antes de las dos.»", "«Lleve cédula, certificado y boleta.»", "Solo el primero tiene personaje, tiempo y un hecho que puede continuar."),
        ("ab", "Un texto dice: «Verde, verde, el cerro / y el cielo, de lana». Otro dice: «El cerro estaba verde y Pedro subió con su perro hasta la cima.» ¿Cuál es narrativo?", "El segundo, porque cuenta lo que hace Pedro", "El primero, porque habla del cerro", "El segundo tiene un personaje que actúa; el primero está en versos."),
    ],
    ctx=("abc", "En el taller de lectura de tu centro reparten un reglamento de biblioteca, un poema y un cuento corto. Quieres reconocer el cuento. ¿Qué miras primero?", "Si cuenta hechos que le pasan a uno o más personajes", "Si es el texto más largo", "Si tiene números", "El cuento se reconoce por sus personajes y hechos, no por su largo."),
    sc=[("En Lenguaje: ¿qué es un género narrativo?", "El que cuenta hechos que les pasan a personajes", "La narrativa se reconoce por personajes y hechos en orden."),
        ("En Lenguaje: ¿qué diferencia a un poema de un cuento?", "El poema usa versos y expresa lo que siente quien habla; el cuento cuenta hechos", "El poema se organiza en versos y expresa una vivencia; el cuento organiza hechos en orden."),
        ("En Lenguaje: ¿cómo se reconoce un texto dramático?", "Hablan los personajes y se escribe para representarlo", "Cada intervención lleva el nombre de quien habla.")],
    op=("Lee los Textos 1 y 4: {F} Escribe en tu cuaderno dos diferencias entre el cuento y la escena de teatro. Después cuenta, oralmente o en tres oraciones escritas, un cuento muy breve que conozcas o inventes, sin datos personales.",
        "Diferencias: en el cuento hay alguien que narra lo que hace Marta; en la escena solo se ven las palabras de Marta y Luis. El cuento dice que ella se rio; la escena no.",
        ["escribe dos diferencias reales entre los textos", "usa datos de los textos", "su cuento tiene un personaje y hechos en orden"],
        ["dos diferencias escritas y un cuento de tres oraciones"],
        ["decir que se diferencian solo por el largo", "escribir un cuento sin personaje"],
        "Pregunta: «¿Quién cuenta y quién habla en cada texto?»."),
    reinforce="Piensa en un cuento que conozcas y di quién es el personaje y qué le pasa.",
    extend="Escribe tres textos que lees en la semana y di si son narrativa, poesía, texto dramático o informativos.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy aprendo las partes de un cuento y las palabras para hablar de él: narrador, personajes, ambiente, conflicto y desenlace.",
    prior=["Sé que un cuento cuenta hechos de personajes.", "Distingo un cuento de un aviso.", "Cuento lo que me pasó en una situación."],
    explain=[
        "Un cuento tiene elementos que se pueden señalar. Los personajes son quienes actúan. El narrador es la voz que cuenta la historia: puede ser alguien de afuera o un personaje. El ambiente es el lugar y el momento en que ocurre.",
        "Los hechos siguen un orden. En el inicio se presenta la situación. En el nudo aparece un conflicto, que es el problema que enfrentan los personajes. En el desenlace el conflicto se resuelve o queda decidido.",
        "Cuando lees, puedes preguntarte: ¿quiénes están?, ¿dónde y cuándo ocurre?, ¿cuál es el problema?, ¿cómo termina? Con esas cuatro preguntas ya entiendes el esqueleto de casi cualquier cuento.",
    ],
    vocab=[("narrador", "voz que cuenta la historia"), ("ambiente", "lugar y momento donde ocurre la historia"), ("conflicto", "problema que enfrentan los personajes"), ("desenlace", "parte final, donde el problema se resuelve")],
    worked=[
        ("Elementos del cuento", "Cuento breve (inventado): «Un lunes por la mañana, Olga llegó a la feria y vio que el viento había botado su toldo. Sus vecinos de puesto lo levantaron entre todos y Olga pudo vender hasta el mediodía».", ["Personajes: Olga y sus vecinos de puesto.", "Ambiente: la feria, un lunes por la mañana.", "Conflicto: el viento botó el toldo.", "Desenlace: lo levantan entre todos y ella vende."], "Cuatro elementos identificados"),
        ("Reconocer al narrador", "Fragmento: «Una joven que esperaba a su lado le ofreció compartir el suyo».", ["La voz habla de «una joven» y de «le ofreció»: usa tercera persona.", "No dice «yo»: el narrador está afuera de la historia."], "Narrador que cuenta desde afuera"),
    ],
    mistakes=[("Confundir el ambiente con los personajes.", "El ambiente es el lugar y el momento, no quienes actúan.", "Pregunta «¿dónde y cuándo?» para el ambiente y «¿quién?» para los personajes."),
              ("Pensar que el narrador es siempre el personaje principal.", "El narrador puede contar desde afuera sin ser parte de la historia.", "Fíjate si dice «yo» o habla de otros en tercera persona.")],
    T=[
        ("abc", "{F} ¿Quién cuenta la historia?", "Un narrador que habla de don Hugo desde afuera", "Don Hugo, que habla de sí mismo", "La joven del taller de costura", "El texto dice «don Hugo esperaba», sin usar «yo»."),
        ("ab", "{F} ¿Cuál es el ambiente de la historia?", "Una parada de bus, en una tarde lluviosa de invierno", "Un taller de costura, en verano", "El texto ubica la escena en la parada, en invierno."),
        ("{F} ¿Cuántos personajes actúan en el cuento? Escribe el número.", "2", "Actúan don Hugo y la joven; el bus solo llega."),
        ("abc", "{F} ¿Cuál es el conflicto del cuento?", "Llueve fuerte y el paraguas de don Hugo está roto", "Don Hugo pierde el bus", "La joven no quiere conversar", "El problema es la lluvia con un paraguas roto."),
        ("ab", "{F} ¿Cómo se resuelve el problema?", "La joven comparte su paraguas y ofrece arreglar el roto", "Deja de llover de pronto", "El texto no dice que deje de llover: la solución viene de la ayuda de la joven."),
        ("abc", "En Lenguaje: ¿qué es el desenlace de un cuento?", "La parte final, donde el problema se resuelve o queda decidido", "La parte inicial, donde se presenta a los personajes", "El título del cuento", "El desenlace es la parte final, donde el problema se resuelve o queda decidido."),
        ("abc", "Lee: «Temprano, Inés llegó al consultorio. La fila daba la vuelta a la cuadra y ella solo traía un abrigo liviano.» ¿Cuál es el ambiente?", "El consultorio, muy temprano en la mañana", "Una casa, por la noche", "El abrigo de Inés", "El ambiente es el lugar y el momento: consultorio y temprano."),
        ("abc", "Lee: «El jefe de turno anunció que cerraría la bodega antes de lo previsto. Julio y Camila debían terminar el inventario en una hora.» ¿Qué problema enfrentan?", "Tienen poco tiempo para terminar el inventario", "No tienen jefe de turno", "La bodega está en otra ciudad", "El conflicto es la falta de tiempo para una tarea."),
        ("abc", "¿En qué orden suceden las partes de un cuento?", "Inicio, nudo y desenlace", "Desenlace, inicio y nudo", "Nudo, desenlace e inicio", "Primero se presenta la situación, luego el problema y al final su resolución."),
        ("ab", "Pablo dice que en «El paraguas de don Hugo» el narrador es don Hugo, porque es el personaje principal. ¿Tiene razón?", "No: el narrador cuenta desde afuera y don Hugo es solo un personaje", "Sí: el personaje principal siempre narra", "El texto habla de don Hugo en tercera persona, sin «yo»."),
        ("abc", "{F} ¿Por qué la joven es importante para el desenlace?", "Porque su ayuda resuelve el problema de don Hugo", "Porque es quien narra el cuento", "Porque cambia el ambiente a un taller", "Sin su paraguas, el conflicto seguiría sin resolverse."),
        ("abc", "Un cuento comienza: «Un viernes en la feria, Rosa vio que su puesto no tenía luz.» ¿Cuál podría ser el conflicto?", "Rosa deberá vender sin luz antes de que anochezca", "Rosa compra verduras para el almuerzo", "La feria tiene muchos puestos", "Un conflicto es un problema que enfrentan los personajes; las otras opciones solo describen."),
        ("ab", "{F} Si el cuento terminara con «Don Hugo se mojó entero y nadie lo ayudó», ¿qué elemento cambiaría?", "El desenlace, porque el problema no se resolvería", "El ambiente, porque ya no sería una parada", "Cambia el final, no el lugar ni el momento."),
    ],
    ctx=("abc", "En una reunión de vecinos alguien cuenta: «Una vez el techo de la sede goteaba. Entre todos juntamos tablas y lo arreglamos un sábado.» ¿Cuál es el problema y cuál la solución?", "Problema: el techo goteaba. Solución: lo arreglaron entre todos", "Problema: el sábado. Solución: las tablas", "Problema: la reunión. Solución: ninguna", "El conflicto es la gotera y el desenlace es el arreglo en conjunto."),
    sc=[("En Lenguaje: ¿qué es un narrador?", "La voz que cuenta la historia", "Puede contar desde afuera o ser un personaje."),
        ("En Lenguaje: ¿qué es el ambiente de un cuento?", "El lugar y el momento donde ocurre", "El ambiente responde dónde y cuándo ocurre la historia."),
        ("¿Cuáles son las tres partes de un cuento?", "Inicio, nudo y desenlace", "Presentan la situación, el conflicto y su resolución.")],
    op=("Escribe en tu cuaderno un cuento de cuatro oraciones que ocurra en «una parada de bus, de noche». Después señala el personaje, el problema y cómo termina.",
        "Era de noche y Lidia esperaba el bus en la parada. El último bus no pasaba. Un vecino le avisó que había cambiado su horario. Los dos caminaron hasta otra parada y subieron juntos. Personaje: Lidia. Problema: el bus no pasaba. Final: lo toman en otra parada.",
        ["usa el ambiente dado", "tiene un problema claro", "señala personaje, problema y final"],
        ["cuatro oraciones y tres datos señalados"],
        ["no incluir un problema", "no cerrar la historia"],
        "Pregunta: «¿Qué problema tiene y cómo se resuelve?»."),
    reinforce="Elige un cuento que conozcas y di quién es el narrador, el ambiente y el conflicto.",
    extend="Reescribe el final de «El paraguas de don Hugo» con un desenlace distinto.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy comparo dos cuentos paso a paso con una ficha y elijo el que prefiero.",
    prior=["Reconozco personajes, ambiente, conflicto y desenlace.", "Sé decir qué me gusta de un texto.", "Puedo hacer una tabla simple."],
    explain=[
        "Comparar es mirar dos cosas a la vez para ver en qué se parecen y en qué se diferencian. Para no comparar al azar, usamos criterios: aspectos que miramos en los dos cuentos, por ejemplo los personajes, el ambiente, el problema y el final.",
        "Paso 1: lee cada cuento completo. Paso 2: elige los criterios. Paso 3: anota lo que dice cada cuento sobre cada criterio, en una tabla. Paso 4: mira qué se parece y qué cambia. Paso 5: decide cuál prefieres y explica por qué con un dato del texto.",
        "Elegir un cuento preferido no es un error ni un acierto: es una decisión tuya. Lo importante es que la apoyes en lo que el texto realmente cuenta.",
    ],
    vocab=[("comparar", "mirar dos cosas para ver en qué se parecen y en qué se diferencian"), ("criterio", "aspecto que se mira en todos los textos que se comparan"), ("preferir", "elegir algo porque te gusta más"), ("ficha", "hoja o tabla donde se anotan datos")],
    worked=[
        ("Llenar una ficha", "Cuento (inventado): «Una mañana, Elsa abrió su almacén y vio que el refrigerador no enfriaba. Llamó al técnico, que llegó al mediodía y lo reparó. Elsa alcanzó a guardar la leche a tiempo».", ["Personajes: Elsa y el técnico.", "Ambiente: el almacén, una mañana.", "Problema: el refrigerador no enfría.", "Final: lo reparan y ella guarda la leche."], "Ficha completa"),
        ("Ver qué cambia", "El cuento del almacén frente a este otro (inventado): «Una tarde, a Nelson se le cayó el celular a un charco. Lo dejó secar un día y volvió a encender». Criterio: «problema».", ["Almacén: el refrigerador no enfría.", "Otro cuento: un celular mojado.", "Son problemas distintos."], "Se diferencian en el problema"),
    ],
    mistakes=[("Escribir «el A es más lindo» sin mirar un criterio.", "Es una opinión sin dato del texto.", "Compara con criterios y agrega un dato de cada cuento."),
              ("Anotar en la ficha datos de un cuento en la columna del otro.", "La comparación queda equivocada.", "Relee cada cuento antes de llenar su columna.")],
    T=[
        ("abc", "{F} ¿Cuál es el problema del Cuento A?", "Un reloj usado se atrasaba", "Se cortó la luz", "Rita perdió su puesto de la feria", "El cliente devuelve un reloj que se atrasaba."),
        ("ab", "{F} ¿Cómo termina el Cuento A?", "Rita arregla el reloj y el cliente vuelve con otro", "El cliente se queda con el reloj atrasado", "Rita lo deja andando y el cliente regresa con otro para arreglar."),
        ("{F} ¿Cuántos vecinos con nombre propio actúan en el Cuento B? Escribe el número.", "2", "Los vecinos nombrados son don Sergio y la señora Elena."),
        ("abc", "En Lenguaje: al comparar textos, ¿qué es un criterio?", "Un aspecto que se mira en todos los textos, como personajes o final", "La opinión final de quien lee", "El título más largo", "Los criterios permiten comparar lo mismo en cada texto."),
        ("ab", "{F} ¿Qué criterio compara «el reloj se atrasaba» con «se cortó la luz»?", "El problema", "El ambiente", "Ambas frases son los conflictos de cada cuento."),
        ("abc", "{F} ¿En qué se parecen los dos cuentos?", "En que el problema queda resuelto al final", "En que ambos ocurren de noche", "En que ambos ocurren en una feria", "En los dos el conflicto se resuelve."),
        ("abc", "{F} Completa el criterio «ambiente» del Cuento B.", "Un edificio, de noche", "Una feria, un domingo", "Don Sergio y la señora Elena", "El cuento B ocurre en una escalera, durante la noche."),
        ("abc", "{F} Completa el criterio «personajes» del Cuento A.", "Rita y un cliente", "Don Sergio y la señora Elena", "Los vecinos del edificio", "Rita y el cliente son quienes actúan en A."),
        ("abc", "Para comparar dos cuentos tenemos cinco pasos. ¿Qué paso va entre «leer cada cuento» y «anotar lo que dice cada uno»?", "Elegir los criterios que se van a mirar", "Decidir cuál prefieres", "Escribir el final", "Se eligen los criterios antes de anotar los datos."),
        ("ab", "{F} Ana escribe: «El A es más lindo que el B.» Beto escribe: «En A el problema es un reloj que se atrasa; en B es un corte de luz.» ¿Quién comparó con un criterio?", "Beto, porque contrasta el problema de cada cuento", "Ana, porque dio su opinión", "Beto nombra un criterio y un dato de cada texto; Ana solo opina."),
        ("abc", "{F} ¿Qué cuento muestra a varias personas resolviendo juntas un problema?", "El B, porque los vecinos revisan el tablero juntos", "El A, porque Rita trabaja con vecinos", "Ninguno", "En B actúan varios vecinos; en A actúa Rita con su cliente."),
        ("abc", "{F} Una lectora prefiere el cuento con un ambiente cerrado y de noche. ¿Cuál elige?", "El B", "El A", "Ninguno, porque ambos ocurren de día", "El B ocurre en un edificio, de noche."),
        ("ab", "{F} Si cambiáramos el Cuento B para que la luz no vuelva, ¿qué criterio cambia?", "El final", "El ambiente", "Cambia cómo termina; el lugar sigue siendo el edificio."),
    ],
    ctx=("abc", "Tu grupo debe elegir entre los Cuentos A y B para leerlo en la reunión. Quieres decidir con un criterio. ¿Qué haces?", "Comparo ambos según personajes, ambiente, problema y final y elijo con un motivo", "Elijo el de título más corto", "Elijo el primero que leí", "Una elección razonada se apoya en datos de los textos."),
    sc=[("¿Cuántos pasos tiene el método para comparar que usamos hoy?", "Cinco", "Leer, elegir criterios, anotar, mirar semejanzas y diferencias, decidir."),
        ("En Lenguaje: ¿qué hago después de anotar lo de cada cuento?", "Miro qué se parece y qué cambia", "Es el paso 4 antes de decidir."),
        ("¿Con qué apoyo mi decisión de preferir un cuento?", "Con un dato del texto", "Un dato del texto muestra que la preferencia tiene un motivo real y no solo gusto.")],
    op=("Compara los Cuentos A y B: {F} Haz en tu cuaderno una tabla con cuatro filas (personajes, ambiente, problema y final) y dos columnas (A y B). Después escribe una oración que diga cuál prefieres y un motivo.",
        "Personajes: A, Rita y un cliente; B, don Sergio, la señora Elena y vecinos. Ambiente: A, la feria; B, un edificio de noche. Problema: A, un reloj atrasado; B, un corte de luz. Final: A, el cliente vuelve; B, vuelve la luz. Prefiero el B porque los vecinos resuelven juntos el problema.",
        ["tabla con los cuatro criterios", "datos correctos en cada columna", "una preferencia con motivo"],
        ["una tabla de 4 filas y 2 columnas y una oración"],
        ["mezclar los datos de A y B", "decir solo «me gustó»"],
        "Pregunta: «¿Qué dato del cuento apoya tu preferencia?»."),
    reinforce="Compara dos cuentos que recuerdes usando solo el criterio «final».",
    extend="Agrega un quinto criterio a la ficha, por ejemplo «cómo se siente el cuento» (alegre, tranquilo o tenso), y úsalo en A y B.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo: comparo otros dos cuentos y uso estrategias para comprender mejor lo que leo.",
    prior=["Sé comparar con criterios.", "Reconozco el conflicto y el final.", "Puedo resumir con mis palabras."],
    explain=[
        "Para comprender mejor un cuento puedes usar estrategias. Antes de leer, predice: mira el título y piensa de qué podría tratar. Mientras lees, hazte preguntas y vuelve a leer lo que no entendiste. Después de leer, resume con tus palabras lo más importante.",
        "A veces el texto no dice todo. Entonces haces una inferencia: deduces algo a partir de pistas. Si alguien mira el reloj varias veces mientras espera, puedes inferir que está apurado o impaciente.",
        "Un resumen cuenta solo lo principal, en pocas oraciones, y no copia el texto. Con estas estrategias y con una ficha de criterios comparas dos cuentos con más seguridad.",
    ],
    vocab=[("predecir", "pensar de qué podría tratar un texto antes de leerlo"), ("inferir", "deducir algo a partir de pistas del texto"), ("resumir", "contar lo principal con pocas palabras"), ("releer", "volver a leer una parte para entenderla mejor")],
    worked=[
        ("Resumir un cuento", "Cuento (inventado): «La señora Aurora llegó a la oficina de trámites y vio que su número era el 48, pero atendían el 20. Se sentó, sacó su cuaderno y esperó. A las once la llamaron».", ["Pregunto: ¿quién, qué problema, cómo termina?", "Aurora debe esperar su turno y la atienden a las once."], "Aurora espera su turno y finalmente la atienden"),
        ("Inferir", "Dato: «Aurora salió de la oficina con la carpeta en alto y una sonrisa».", ["Sonreír suele mostrar alivio o contento.", "Venía de esperar mucho y la atendieron."], "Quedó contenta de haber resuelto su trámite"),
    ],
    mistakes=[("Copiar casi todo el cuento como resumen.", "Un resumen debe ser breve y decir solo lo principal.", "Responde quién, qué pasa y cómo termina, en dos oraciones."),
              ("Inferir algo que el texto no insinúa.", "Una inferencia necesita pistas dentro del texto.", "Señala la frase que te hizo pensar eso.")],
    T=[
        ("abc", "{F} ¿Qué problema tiene Martina en el Cuento C?", "El ascensor se detiene entre dos pisos", "Se le perdió una carta", "El consultorio está cerrado", "El texto dice que el ascensor se detuvo entre dos pisos."),
        ("ab", "{F} ¿Por qué la señora Rosa volvió el martes al correo?", "Porque el primer día estaba cerrado por feriado", "Porque olvidó la carta", "El texto dice que el correo estaba cerrado por feriado."),
        ("{F} ¿Cuántos minutos pasaron hasta que se abrieron las puertas del ascensor? Escribe el número.", "5", "El Cuento C dice «cinco minutos después»."),
        ("abc", "{F} ¿Cuál es un buen resumen del Cuento D?", "La señora Rosa envía una carta a su hermano y recibe una respuesta con una foto", "La señora Rosa cultiva tomates en su huerta", "El hermano de la señora Rosa viaja a visitarla", "Un resumen dice lo principal: envío y respuesta."),
        ("ab", "En Lenguaje: antes de leer, miras el título «La carta de la señora Rosa» y piensas «tratará de una carta». ¿Qué estrategia usas?", "Predecir", "Resumir", "Pensar de qué tratará a partir del título es predecir."),
        ("abc", "{F} Martina «respiró hondo». ¿Qué se puede inferir?", "Que estaba nerviosa y se calmó", "Que estaba muy tranquila desde el principio", "Que se enojó con quien le habló", "La pista es el susto anterior."),
        ("abc", "{F} Compara los problemas. ¿Cuál afirmación es correcta?", "En C el problema es un ascensor detenido; en D es un correo cerrado", "En C el problema es un correo cerrado; en D un ascensor detenido", "Ambos tienen el mismo problema", "Cada cuento plantea un problema distinto."),
        ("abc", "{F} ¿En qué criterio se parecen C y D?", "En que ambos problemas se resuelven esperando", "En que ambos ocurren en un consultorio", "En que ambos tienen hermanos como personajes", "En C Martina espera cinco minutos; en D Rosa espera hasta el martes."),
        ("ab", "{F} ¿Qué ocurre primero en el Cuento D?", "La señora Rosa escribe la carta", "Llega la respuesta de su hermano", "La carta se escribe antes de ir al correo; la respuesta llega después."),
        ("ab", "Luz no entendió quién apretó el botón y vuelve a leer esa parte. ¿Qué estrategia usa?", "Releer", "Predecir", "Volver a leer una parte para entenderla es releer."),
        ("abc", "{F} Tomás prefiere el cuento con un momento de susto; Iris prefiere el que cuenta algo tranquilo, sin sustos. ¿Qué cuento elige cada uno?", "Tomás elige C e Iris elige D", "Tomás elige D e Iris elige C", "Ambos eligen C", "Solo en C la protagonista se asusta."),
        ("abc", "Un cuento se titula «El sobre sin nombre». ¿Qué predicción es propia de un cuento?", "Alguien encuentra un sobre y debe descubrir de quién es", "Se explica cómo se fabrica el papel", "Se enumeran las reglas de un correo", "Un cuento cuenta hechos con personajes; las otras opciones informan."),
        ("abc", "{F} Se dice: «Martina es valiente». ¿Qué dato del texto lo apoya?", "Que apretó el botón de ayuda y esperó tranquila", "Que el ascensor se detuvo entre dos pisos", "Que salió al pasillo", "Pedir ayuda y esperar con calma pese al susto muestra valentía; las otras opciones no lo muestran."),
    ],
    ctx=("abc", "En una sala de espera te dan un cuento titulado «La fila interminable». Antes de leerlo, ¿qué haces para comprender mejor?", "Pienso de qué podría tratar según el título", "Salto al final", "Leo solo la primera palabra", "Predecir con el título ayuda a prepararse para leer."),
    sc=[("En Lenguaje: ¿qué significa inferir al leer un cuento?", "Deducir algo a partir de pistas del texto", "La respuesta no está escrita, pero tiene pistas."),
        ("¿Qué incluye el resumen de un cuento?", "Lo principal, en pocas oraciones", "Un resumen deja los detalles y no copia el texto completo."),
        ("¿Qué estrategia uso antes de leer?", "Predecir con el título", "Predecir con el título prepara a quien lee para comprender el texto.")],
    op=("Relee el Cuento C: {F} Escribe en tu cuaderno una predicción hecha solo con el título, una pregunta que te harías mientras lees y un resumen de dos oraciones.",
        "Predicción: alguien queda encerrado en un ascensor. Pregunta: ¿cómo pedirá ayuda? Resumen: Martina queda atrapada en un ascensor. Aprieta el botón de ayuda y a los cinco minutos sale.",
        ["una predicción con el título", "una pregunta sobre el texto", "un resumen de dos oraciones sin copiar"],
        ["tres textos breves"],
        ["copiar el cuento", "una pregunta que no se relaciona con el texto"],
        "Pregunta: «¿Esto es lo principal o un detalle?»."),
    reinforce="Elige un cuento que conozcas y resúmelo en dos oraciones.",
    extend="Escribe una inferencia sobre la señora Rosa y la frase del texto que te dio la pista.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a una decisión real: elegir, entre tres cuentos, cuál leer en voz alta en una reunión de grupo.",
    prior=["Comparo cuentos con criterios.", "Resumo un cuento.", "Sé que preferir algo requiere un motivo."],
    explain=[
        "En la vida, a veces hay que elegir un cuento para compartirlo: en un taller, en una reunión de vecinos o en la biblioteca del barrio. Para elegir bien conviene decidir primero qué criterios importan.",
        "Algunos criterios útiles son el tema, el tono (alegre, tranquilo o tenso), el final y el tiempo disponible para leerlo. Al aplicar un criterio, descartas los cuentos que no lo cumplen y te quedas con los que sí.",
        "Una buena elección se explica con una frase: «Elijo este cuento porque…», seguida de un dato del texto. Así otras personas entienden tu decisión aunque prefieran otro cuento.",
    ],
    vocab=[("tono", "cómo se siente un cuento: alegre, tranquilo, tenso"), ("tema", "asunto de que trata el cuento"), ("descartar", "dejar de lado lo que no cumple el criterio"), ("seleccionar", "elegir uno entre varios")],
    worked=[
        ("Elegir con un criterio de tiempo", F5, ["Hay solo 3 minutos.", "El cuento 1 dura 2 y el 3 dura 3: caben.", "El cuento 2 dura 6: se descarta."], "Caben los cuentos 1 y 3"),
        ("Elegir con un criterio de final", F5, ["Quiero un final en que se comparta algo entre todos.", "El cuento 2 termina con vecinos que reparten lechugas."], "Elijo el cuento 2"),
    ],
    mistakes=[("Elegir sin decir un criterio.", "La decisión queda sin motivo.", "Di qué criterio usaste: tema, tono, final o tiempo."),
              ("Olvidar el tiempo disponible.", "Puede que el cuento no alcance a leerse.", "Revisa cuánto dura cada cuento antes de elegir.")],
    T=[
        ("abc", "{F} ¿Cuál cuento trata de vecinos que hacen una huerta?", "El cuento 2, «La huerta del pasaje»", "El cuento 1, «Un día de lluvia en la terminal»", "El cuento 3, «El turno de noche»", "El título y el resumen del cuento 2 hablan de la huerta."),
        ("ab", "{F} ¿Quién atrapa el paraguas en el cuento 1?", "Un guardia", "Raúl", "El resumen dice que lo atrapa un guardia; Raúl es del cuento 3."),
        ("{F} ¿Cuántos minutos dura el cuento 3? Escribe el número.", "3", "El resumen indica un tiempo de lectura de 3 minutos."),
        ("abc", "{F} Tu grupo quiere un cuento humorístico. ¿Cuál eliges?", "El cuento 1", "El cuento 2", "El cuento 3", "El paraguas que rueda por el andén y las risas dan un tono alegre."),
        ("ab", "{F} Quieres un cuento con un final en que alguien rescata a un ser atrapado. ¿Cuál eliges?", "El cuento 3, donde Raúl libera al gato atrapado", "El cuento 1, donde el viento se lleva el paraguas", "Raúl ayuda a un gato que estaba atrapado."),
        ("{F} Si leen los cuentos 1 y 3 seguidos, ¿cuántos minutos necesitan en total? Escribe el número.", "5", "Se suman 2 y 3 minutos."),
        ("=", "{F} Si leen los tres cuentos seguidos, ¿cuántos minutos necesitan en total?", "2+6+3", "Suma los tiempos de los tres: 2, 6 y 3 minutos.", "minutos"),
        ("abc", "{F} En la reunión hay solo 4 minutos y quieren un cuento sobre trabajo en comunidad. ¿Qué conviene decir?", "No alcanza: el único cuento de ese tema dura 6 minutos", "Alcanza: el cuento 2 dura 2 minutos", "Alcanza: el cuento 3 trata de vecinos", "El cuento 2 es el de comunidad y dura 6 minutos, más que 4."),
        ("abc", "{F} Hay 5 minutos y quieren leer dos cuentos. ¿Qué pareja cabe?", "Los cuentos 1 y 3", "Los cuentos 2 y 3", "Los cuentos 1 y 2", "Solo 2 y 3 minutos suman 5; las otras parejas pasan de 5."),
        ("ab", "Un lector dice: «Elijo el cuento 3 porque tiene un tono tenso al principio y un final tranquilo.» ¿Qué hizo bien?", "Dio un motivo apoyado en el tono y el final del cuento", "Dijo solo el número del cuento", "Un buen motivo nombra un criterio y un dato del texto."),
        ("abc", "{F} Un asistente dice que el cuento 1 es el más largo. ¿Qué se puede responder?", "El más largo es el cuento 2, con 6 minutos", "Tiene razón, porque trata de un paraguas gigante", "El más largo es el cuento 3", "Se compara el tiempo de lectura: 6 es mayor que 2 y 3."),
        ("abc", "{F} Una vecina prefiere un cuento con personajes que se turnan para trabajar. ¿Qué dato del texto apoya la elección del cuento 2?", "Que los vecinos se turnan para regar", "Que el guardia atrapa el paraguas", "Que Raúl usa una linterna", "En el cuento 2 los vecinos se turnan para regar la huerta."),
        ("ab", "{F} El grupo quiere el cuento más breve. ¿Cuál es?", "El cuento 1", "El cuento 3", "Con 2 minutos es más corto que los de 3 y 6."),
    ],
    ctx=("abc", "En la biblioteca del barrio te piden elegir un cuento para leer a un grupo de personas en 3 minutos. ¿Qué haces?", "Descarto los que duran más de 3 minutos y elijo entre los demás con otro criterio", "Elijo el que tiene el título más largo", "Leo el más largo aunque no alcance", "Primero se cumple el criterio de tiempo y luego se elige por tema o tono."),
    sc=[("En Lenguaje: ¿qué es el tono de un cuento?", "Cómo se siente: alegre, tranquilo o tenso", "El tono es parte de lo que se compara."),
        ("¿Qué criterios me ayudan a elegir un cuento?", "Tema, tono, final y tiempo", "Son datos de los que se puede hablar."),
        ("¿Cómo explico mi elección?", "Digo «elijo este cuento porque…» y doy un dato del texto", "Decir el motivo con un dato del texto permite que otros entiendan y comparen la decisión.")],
    op=("Con los tres cuentos: {F} Elige uno para leer en una reunión. Escribe en tu cuaderno el cuento elegido, el criterio que usaste y dos datos del texto que lo apoyan.",
        "Elijo el cuento 3 porque tiene suspenso y dura 3 minutos. Datos: Raúl oye un golpe y camina con una linterna; descubre un gato atrapado y lo libera.",
        ["elige un cuento", "dice el criterio", "apoya con dos datos del texto"],
        ["un párrafo de tres oraciones"],
        ["no decir el criterio", "datos que no están en el texto"],
        "Pregunta: «¿Qué dato del cuento apoya tu elección?»."),
    reinforce="Elige entre dos cuentos que conozcas y di cuál lees en voz alta, con un motivo.",
    extend="Agrega un cuarto cuento inventado a la lista y decide si lo elegirías, con un criterio.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso lo logrado: reconozco géneros, elementos del cuento, comparo y elijo, y decido qué quiero repasar.",
    prior=["Reconozco narrativa, poesía y texto dramático.", "Comparo con criterios.", "Uso estrategias de comprensión."],
    explain=[
        "Revisar lo aprendido es mirar qué ya haces bien y qué quieres repasar. En estas clases aprendiste a reconocer un cuento, a nombrar sus elementos, a compararlo con criterios y a elegir uno con un motivo.",
        "Cuando escuchas un cuento leído por otra persona, usas las mismas estrategias: predices con el título, te preguntas cosas, y al final resumes. No hace falta tomar notas largas: una palabra por personaje, lugar y problema ayuda a recordar.",
        "Para decidir tus próximos pasos, marca en tu cuaderno qué te resulta fácil, qué te cuesta y qué practicarás. Pedir apoyo para lo que cuesta es parte de aprender.",
    ],
    vocab=[("género narrativo", "textos que cuentan hechos que les pasan a personajes"), ("poesía", "textos escritos en versos que expresan lo que siente quien habla"), ("repasar", "volver a trabajar algo para dominarlo"), ("escuchar con atención", "seguir lo que se dice para entenderlo y recordarlo")],
    worked=[
        ("Comparar un cuento y un poema", "Texto A (inventado): «Don Ramón fue al banco y vio una fila larga. Esperó, conversó con una vecina y salió con su trámite hecho». Texto B (inventado): «Lluvia en la ventana, / el té que se enfría; / la tarde se queda / quieta, tibia, mía».", ["A: tiene personaje (don Ramón), hechos en orden y un problema.", "B: tiene versos y expresa una sensación, sin personaje que actúe."], "A es cuento; B es poema"),
        ("Tomar notas al escuchar", "Un lector dice en voz alta: «Doña Luisa llegó a la feria y su puesto estaba ocupado por otro vendedor».", ["Anoto: Luisa; feria; puesto ocupado.", "Esa nota es el problema."], "Nota: problema = su puesto está ocupado"),
    ],
    mistakes=[("Creer que el poema tiene los mismos elementos que el cuento.", "El poema expresa lo que siente quien habla; no siempre tiene personajes ni hechos.", "Pregunta si cuenta hechos o si expresa una vivencia."),
              ("Dejar de lado lo que cuesta.", "No se avanza si no se nombra lo difícil.", "Anota qué quieres repasar y cómo lo harás.")],
    T=[
        ("abc", "{F} ¿Cuál texto es un cuento?", "El Texto 1, «La bolsa de pan»", "El Texto 2, «Pan»", "Ninguno", "El Texto 1 tiene una protagonista, hechos en orden y un problema."),
        ("ab", "{F} ¿Quién es la protagonista del Texto 1?", "Ema", "La panadería", "Ema es quien actúa y resuelve el problema."),
        ("{F} ¿En qué día de la semana ocurre el cuento? Escribe el día.", "viernes", "El texto dice «ese viernes»: el cuento ocurre un viernes, día de la reunión."),
        ("abc", "{F} ¿Cuál es el conflicto del Texto 1?", "La panadería está cerrada y Ema no tiene pan para llevar", "A Ema no le gusta amasar", "El grupo no hizo reunión", "El problema es no tener qué llevar a la reunión."),
        ("ab", "{F} ¿Cómo resuelve Ema el problema?", "Hornea unos panes con harina y levadura que tenía en casa", "Compra pan en otra ciudad", "Usa lo que tenía en casa para amasar y hornear."),
        ("abc", "{F} ¿Qué hace que el Texto 2 sea un poema?", "Está en versos y expresa sensaciones sobre el pan", "Cuenta lo que hace Ema", "Da instrucciones para hornear", "Usa versos y describe sensaciones; no cuenta hechos."),
        ("abc", "Escuchas esta frase leída en voz alta: «Don Pedro llegó tarde al taller y encontró la puerta cerrada.» ¿Cuál es la mejor nota?", "Pedro; llega tarde; puerta cerrada", "Taller; puerta; tarde; Pedro; llegó; encontró", "Pedro es un hombre", "Una nota breve recoge personaje, hecho y problema."),
        ("abc", "Alguien lee: «Cuando amaneció, la plaza estaba vacía. Solo un perro dormía bajo el banco. Sara se sentó a esperar.» ¿Cuál es el ambiente?", "Una plaza al amanecer", "Una panadería al mediodía", "Un banco de la ciudad", "El lugar es la plaza y el momento es el amanecer."),
        ("abc", "¿Qué estrategia usas cuando, al terminar un cuento, cuentas lo principal con tus palabras?", "Resumir", "Predecir", "Releer", "Contar lo principal en pocas palabras es resumir."),
        ("ab", "Juan dice: «El Texto 2 es un cuento porque tiene pan, igual que el Texto 1.» ¿Cuál es la respuesta más precisa?", "No: el Texto 2 está en versos y no cuenta hechos de un personaje", "Sí: tiene el mismo tema", "El tema no define el género; los versos sí distinguen la poesía."),
        ("abc", "{F} Al comparar los dos textos con el criterio «qué cuentan», ¿cuál afirmación es correcta?", "El Texto 1 cuenta hechos y el Texto 2 expresa sensaciones", "Los dos cuentan hechos de personajes", "Los dos son avisos", "El cuento narra hechos; el poema expresa lo que se siente."),
        ("abc", "Dos lectores eligen. Nora: «Prefiero el cuento porque Ema resuelve su problema con ingenio.» Ariel: «Prefiero el cuento porque sí.» ¿Quién justifica mejor?", "Nora, porque da un motivo apoyado en el texto", "Ariel, porque es más corto", "Ninguno justifica", "Nora usa un dato del texto; Ariel no da razón."),
        ("ab", "{F} Después de leer, anotas: «Predije que habría un problema con el pan.» ¿En qué etapa predijiste?", "Antes de leer, con el título", "Después de resumir", "Una predicción se hace antes de leer."),
    ],
    ctx=("abc", "Una persona te cuenta un cuento en una reunión y quieres recordarlo después. ¿Qué haces mientras escuchas?", "Anoto personajes, lugar y problema con pocas palabras", "Copio cada palabra", "No anoto nada", "Las notas breves ayudan a recordar sin perder el hilo."),
    sc=[("¿Qué aprendí a nombrar en un cuento?", "Personajes, narrador, ambiente, conflicto y desenlace", "Son los elementos del cuento que se señalan al leer y al comparar."),
        ("¿Qué criterios usé para comparar?", "Personajes, ambiente, problema y final", "Son los criterios de la ficha que usamos para comparar los cuentos."),
        ("En Lenguaje: ¿qué hago para recordar un cuento que escucho?", "Anoto con pocas palabras personajes, lugar y problema", "Las notas breves guardan lo principal sin perder el hilo de lo que se dice.")],
    op=("Revisa tu avance: {F} Escribe en tu cuaderno tres cosas que ya haces bien con los cuentos, una que quieres repasar y cómo la practicarás esta semana. Después compara el Texto 1 y el Texto 2 en dos oraciones.",
        "Hago bien: reconozco el conflicto; resumo; elijo con criterio. Quiero repasar: inferir. Lo practicaré inferiendo una pista en cada cuento. Comparación: el Texto 1 cuenta lo que hace Ema; el Texto 2 expresa sensaciones sobre el pan.",
        ["tres logros", "una meta concreta", "una comparación de dos textos con datos"],
        ["un párrafo con logros, meta y comparación"],
        ["escribir metas muy generales", "comparar sin datos"],
        "Pregunta: «¿Qué harás concretamente para practicarlo?»."),
    reinforce="Cuenta a otra persona un cuento breve, con inicio, nudo y desenlace.",
    extend="Escribe un cuento de tres oraciones y su versión en poema de dos versos, y di qué cambia.",
)
