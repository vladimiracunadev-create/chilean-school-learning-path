"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (Estados tempranos, poder y organización social)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 03"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (tres asentamientos de ejemplo, hechos para este cuaderno). "
     "Asentamiento X: 150 personas, todas cultivan; no hay templos ni muros; las decisiones las toma un consejo de ancianos conversando. "
     "Asentamiento Y: 5.000 personas; tiene calles, mercado, taller de cerámica y un templo; no hay registros escritos ni un gobierno central. "
     "Asentamiento Z: un territorio con 4 ciudades y 60 aldeas, gobernado por un rey, con funcionarios que cobran tributo, un ejército, leyes escritas y escribas. "
     "Definiciones: aldea es un poblado pequeño donde casi todos cultivan; ciudad es un poblado grande con oficios, mercado y edificios públicos; Estado es una organización con gobierno central, funcionarios, leyes y fuerza para hacerlas cumplir en un territorio.")
build(
    OA, 1, F,
    use="Aprenderé a distinguir una aldea, una ciudad y un Estado por sus rasgos. Sirve para no confundir tamaño con forma de organización.",
    prior=["Sé que la agricultura permitió excedentes y especialización.", "Sé qué es una aldea.", "Sé leer una descripción y sacar datos."],
    explain=[
        "Con el excedente de alimentos, algunos poblados crecieron. Una aldea es un poblado pequeño donde casi todas las personas cultivan y las decisiones se toman en conjunto. Una ciudad es un poblado grande con oficios diversos, mercado y edificios públicos, como templos. Pero tener muchas personas no basta para ser un Estado.",
        "Un Estado es una forma de organización política que tiene un gobierno central, funcionarios que cumplen tareas, leyes y fuerza para hacerlas cumplir sobre un territorio. Los primeros Estados aparecieron hace unos 5.000 años en lugares como Mesopotamia y Egipto. Solían usar la escritura para llevar cuentas y registrar leyes.",
        "Los primeros Estados no fueron todos iguales: unos eran un rey con varias ciudades, otros una ciudad con su territorio. Para decidir si un poblado es aldea, ciudad o Estado se observan sus rasgos: población, oficios, edificios, gobierno, registros y tributo. El tamaño ayuda, pero no es el único criterio.",
    ],
    vocab=[("ciudad", "poblado grande con oficios, mercado y edificios públicos"), ("Estado", "organización con gobierno central, funcionarios, leyes y fuerza para hacerlas cumplir"), ("funcionario", "persona que cumple una tarea al servicio del gobierno"), ("tributo", "pago obligatorio que se entrega a una autoridad"), ("escriba", "persona que sabía escribir y llevaba registros")],
    worked=[
        ("Clasificar un asentamiento", "Un poblado de 300 personas, todas campesinas, sin templo y que decide en asamblea. ¿Es aldea, ciudad o Estado?", ["Tiene pocas personas y todas cultivan.", "No tiene gobierno central ni funcionarios."], "Aldea"),
        ("Contar poblados", "{F} ¿Cuántos poblados hay en el territorio Z?", ["Sumo las ciudades y las aldeas: 4 + 60.", "El resultado incluye todos los poblados del territorio."], "64 poblados"),
    ],
    mistakes=[("Decir que cualquier ciudad grande es un Estado.", "Se usa solo el tamaño como criterio.", "Revisa si tiene gobierno central, funcionarios, leyes y fuerza para hacerlas cumplir."),
              ("Creer que todos los primeros Estados fueron iguales.", "Se usa un solo modelo para todos.", "Compara rasgos concretos: algunos tenían un rey sobre varias ciudades y otros una ciudad con su territorio.")],
    T=[
        ("{F} ¿Cuántas personas hay en el asentamiento X?", "150", "La ficha lo indica."),
        ("{F} ¿Quién toma las decisiones en el asentamiento X?", "Un consejo de ancianos", "La ficha lo indica."),
        ("{F} ¿Qué asentamiento tiene templo y mercado pero no registros escritos?", "El asentamiento Y", "La ficha lo describe así."),
        ("=", "{F} ¿Cuántas personas más hay en Y que en X?", "5000-150", "Se resta la población menor a la mayor.", " personas"),
        ("{F} Clasifica los asentamientos X, Y y Z como aldea, ciudad o Estado.", "X aldea, Y ciudad, Z Estado", "Cada uno cumple los rasgos de la definición correspondiente."),
        ("=", "{F} Si cada una de las 60 aldeas de Z entrega 10 sacos de tributo, ¿cuántos sacos recibe el rey?", "60*10", "Se multiplica el número de aldeas por el tributo de cada una.", " sacos"),
        ("{F} ¿Qué rasgo de Z, que no tiene Y, lo hace un Estado?", "Un gobierno central con rey, funcionarios, leyes escritas y fuerza para hacerlas cumplir", "Y es grande, pero no tiene esos rasgos."),
        ("{F} Un poblado tiene mercado, templo y 4.000 personas, pero ninguna autoridad que cobre tributo ni haga cumplir leyes. ¿Es un Estado? Explica.", "No: es una ciudad, porque le faltan gobierno central, funcionarios y leyes con fuerza", "El tamaño no basta; cuentan los rasgos políticos."),
        ("{F} En Z, ¿cuántos poblados hay que no son ciudades?", "60", "Las aldeas son 60 y las ciudades 4."),
        ("{F} Mateo dice: «Toda ciudad grande es un Estado». Corrígelo con la ficha.", "El asentamiento Y es grande y tiene templo y mercado, pero no tiene gobierno central ni registros: es ciudad, no Estado", "El tamaño no define al Estado."),
        ("{F} ¿Por qué un Estado necesita escribir registros?", "Para anotar los tributos, las leyes y las órdenes, que no se pueden recordar de memoria", "Z tiene escribas que llevan cuentas."),
        ("{F} Un territorio tiene un rey con funcionarios, leyes escritas y ejército, pero solo 3 aldeas. ¿Es un Estado? Explica.", "Sí, porque cumple los rasgos políticos aunque sea pequeño", "El tamaño no es el criterio principal."),
        ("{F} ¿Qué evidencia arqueológica podría indicar que un poblado era parte de un Estado y no solo una ciudad? Da un ejemplo.", "Tablillas con registros de tributo, o edificios de administración, o sellos de funcionarios", "Muestran gobierno central y control de recursos."),
    ],
    ctx=("Una profesora muestra un mapa con un rey, cuatro ciudades y sesenta aldeas, y pregunta si el territorio es una ciudad grande o un Estado. ¿Qué respondes y por qué? {F}", "Es un Estado, porque tiene gobierno central, funcionarios, tributo, ejército y leyes escritas", "Cumple los rasgos de la definición de Estado."),
    sc=[("¿Qué es un Estado?", "Una organización con gobierno central, funcionarios, leyes y fuerza para hacerlas cumplir", "Es la definición de la clase."),
        ("¿El tamaño de un poblado basta para decir que es un Estado?", "No", "Se necesitan rasgos políticos."),
        ("{F} ¿Cuántas ciudades tiene el asentamiento Z?", "4", "La ficha lo indica.")],
    op=("Haz un cuadro de tres columnas (aldea, ciudad y Estado) con tres rasgos en cada una, usando las definiciones de la ficha. Después escribe en dos líneas por qué Y no es un Estado. {F}",
        "Aldea: pocos habitantes, todos cultivan, decisiones en conjunto. Ciudad: oficios, mercado, templo. Estado: gobierno central, funcionarios, leyes.",
        ["tres rasgos por columna", "los rasgos son distintos entre columnas", "explica por qué Y no cumple"], ["cuadro escrito"], ["repetir rasgos entre columnas", "usar solo el tamaño"],
        "Pide que explique qué faltaría en Y para ser Estado."),
    reinforce="Di en voz alta los cuatro rasgos que tiene un Estado y una aldea no.",
    extend="Escribe una pregunta sobre cómo podría crecer una ciudad hasta convertirse en el centro de un Estado.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (Estado de ejemplo, inspirado en Estados reales de Mesopotamia y Egipto; las cifras son de ejemplo). "
     "Hay 30 aldeas. Cada aldea paga cada año un tributo de 20 sacos de cebada y 2 corderos. "
     "Los escribas anotan en tablillas de arcilla lo que entrega cada aldea. Los funcionarios guardan el tributo en graneros del templo y del palacio. "
     "Con el tributo se alimenta a 200 trabajadores que construyen un canal de riego y un muro de la ciudad.")
build(
    OA, 2, F,
    use="Aprenderé a relacionar la administración, el tributo y las obras públicas de los primeros Estados. Sirve para entender cómo se financiaba y organizaba el poder.",
    prior=["Sé qué es un Estado.", "Sé multiplicar y dividir.", "Sé que los escribas llevaban registros."],
    explain=[
        "La administración es la organización de tareas por parte de funcionarios: cobrar, anotar, guardar y repartir. Los primeros Estados necesitaban escribas para llevar cuentas en tablillas de arcilla, como en Mesopotamia, o en papiro, como en Egipto. Sin registros, no se podía saber quién había pagado.",
        "El tributo es un pago obligatorio de granos, animales u otros productos. El Estado lo guardaba en graneros y lo usaba para alimentar a funcionarios, ejército y trabajadores. Con esos recursos se hacían obras públicas: canales de riego, templos, murallas y caminos, que ninguna aldea podía construir por sí sola.",
        "Las obras beneficiaban a muchas personas, por ejemplo con más agua para los campos, pero también eran una carga: el tributo había que entregarlo aunque la cosecha fuera mala. Se forma un circuito: el tributo financia obras, las obras ayudan a producir más, y el Estado puede cobrar más. Esa explicación sirve, pero no dice qué pensaban los habitantes del tributo.",
    ],
    vocab=[("administración", "organización de tareas como cobrar, anotar y guardar"), ("tributo", "pago obligatorio que se entrega a una autoridad"), ("obra pública", "construcción para muchos, como un canal, un templo o una muralla"), ("tablilla", "pieza de arcilla donde se escribía"), ("granero", "lugar para guardar granos")],
    worked=[
        ("Calcular un tributo", "{F} ¿Cuántos sacos de cebada recibe el Estado de las 30 aldeas en un año?", ["Cada aldea entrega 20 sacos.", "Multiplico: 30 × 20 = 600."], "600 sacos"),
        ("Distribuir recursos", "Un Estado de ejemplo reúne 900 sacos para 300 trabajadores. ¿Cuántos sacos corresponden a cada trabajador?", ["Reparto en partes iguales.", "Divido: 900 ÷ 300 = 3."], "3 sacos por trabajador"),
    ],
    mistakes=[("Creer que el tributo era un regalo voluntario.", "Se confunde con una donación.", "Era un pago obligatorio fijado por la autoridad."),
              ("Decir que las obras públicas beneficiaban a todos por igual.", "Se ignora quién pagaba y quién se beneficiaba más.", "Pregunta quién entregaba el tributo, quién trabajaba y quién usaba la obra.")],
    T=[
        ("{F} ¿Dónde anotan los escribas lo que entrega cada aldea?", "En tablillas de arcilla", "La ficha lo indica."),
        ("{F} ¿Qué entrega cada aldea cada año?", "20 sacos de cebada y 2 corderos", "La ficha lo indica."),
        ("{F} ¿Dónde guardan los funcionarios el tributo?", "En graneros del templo y del palacio", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos corderos recibe el Estado de las 30 aldeas?", "30*2", "Se multiplica el número de aldeas por los corderos de cada una.", " corderos"),
        ("=", "{F} Si los sacos de cebada recibidos se reparten en partes iguales entre los 200 trabajadores, ¿cuántos sacos corresponden a cada uno?", "600//200", "Se divide el total por los trabajadores.", " sacos"),
        ("{F} ¿Para qué sirve el registro en tablillas?", "Para saber qué entregó cada aldea y poder exigirlo", "Sin registro no se sabe quién cumplió."),
        ("{F} Clasifica como administración (A) u obra pública (O): 1) anotar entregas; 2) construir el canal de riego; 3) guardar el tributo en graneros; 4) levantar el muro.", "1 A, 2 O, 3 A, 4 O", "Anotar y guardar organizan recursos; el canal y el muro son construcciones."),
        ("=", "{F} Cinco aldeas no pagan sus 20 sacos por una sequía. ¿Cuántos sacos menos recibe el Estado?", "5*20", "Se multiplican las aldeas que no pagan por su tributo.", " sacos"),
        ("{F} ¿Por qué un canal de riego puede beneficiar a las aldeas?", "Porque lleva agua a los campos y puede aumentar las cosechas", "Más agua permite producir más."),
        ("{F} Ana dice: «El tributo era un regalo voluntario de las aldeas». Corrígela con la ficha.", "Era un pago obligatorio y fijo: cada aldea debía entregar 20 sacos y 2 corderos", "La ficha habla de un pago anual fijo."),
        ("{F} Explica cómo se relacionan el tributo y las obras públicas.", "El tributo alimenta a los trabajadores que construyen las obras, y las obras (como el riego) ayudan a producir más tributo", "Forman un circuito entre recursos y construcciones."),
        ("{F} ¿Qué carga tenía el tributo para una aldea con mala cosecha?", "Debía entregar su parte igual, aunque le quedara menos para alimentarse", "La obligación no dependía del resultado de la cosecha."),
        ("{F} Las tablillas muestran lo que entregó cada aldea. ¿Qué no permiten saber sobre las aldeas?", "Qué pensaban las personas del tributo o si lo consideraban justo", "Son registros administrativos, no opiniones."),
    ],
    ctx=("En un colegio el centro de estudiantes cobra una cuota obligatoria y con ella paga un mural para todos. ¿Qué dos ideas de la clase se parecen y qué diferencia hay con un Estado antiguo? {F}", "Se parece al tributo y a la obra pública; difiere en que un Estado antiguo tenía fuerza para hacer cumplir el pago", "Cuota obligatoria + obra para todos recuerda al circuito tributo-obras."),
    sc=[("¿Qué es un tributo?", "Un pago obligatorio entregado a una autoridad", "No es voluntario."),
        ("¿Qué es una obra pública? Da un ejemplo de la clase.", "Una construcción para muchos, como un canal de riego, un templo o una muralla", "Beneficia a toda la comunidad."),
        ("=", "{F} ¿Cuántos sacos recibiría el Estado de 10 aldeas?", "10*20", "Se multiplican las aldeas por el tributo de cada una.", " sacos")],
    op=("Dibuja un esquema con flechas que muestre el circuito tributo, graneros, trabajadores, obras y mayor cosecha. Escribe una frase sobre quién se beneficia y quién carga con el costo. {F}",
        "Aldeas entregan tributo, los graneros guardan, el Estado alimenta a trabajadores, se construye el canal y las cosechas mejoran.",
        ["el esquema tiene todas las etapas", "las flechas muestran el orden", "la frase señala un beneficio y una carga"], ["esquema dibujado", "frase escrita"], ["olvidar de dónde sale el tributo", "mostrar solo beneficios"],
        "Pide que explique qué pasaría con el circuito si dos años seguidos hubiera sequía."),
    reinforce="Explica con tus palabras qué es el tributo y para qué se usaba.",
    extend="Escribe una pregunta sobre cómo se decidía qué obra construir primero.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (fuentes de ejemplo, inspiradas en los Estados de Mesopotamia y Egipto; los textos están inventados para este cuaderno). "
     "Fuente A: inscripción de un rey: «Los dioses me eligieron para dar justicia y agua a mi pueblo». "
     "Fuente B: tablilla de un templo: «El sacerdote recibe cebada y la ofrece al dios; el palacio guarda una parte». "
     "Fuente C: relieve donde el rey mide 12 cm de alto y las demás figuras, 4 cm; un dios le entrega un símbolo de autoridad. "
     "Fuente D: informe de un escriba: «Este año el río subió bien y el pueblo celebra al rey».")
build(
    OA, 3, F,
    use="Aprenderé a examinar cómo los gobernantes de los primeros Estados justificaban su poder con ideas religiosas. Sirve para entender por qué la gente aceptaba la autoridad.",
    prior=["Sé qué es un Estado y qué es el tributo.", "Sé que una fuente tiene un autor con un propósito.", "Sé leer imágenes como fuentes."],
    explain=[
        "La legitimación es el conjunto de razones que hacen que las personas acepten el poder de una autoridad. En los primeros Estados, muchas veces la religión daba esas razones. En Mesopotamia los reyes decían ser elegidos por los dioses; en Egipto el faraón era considerado un ser divino que mantenía el orden del mundo.",
        "Los gobernantes mostraban ese vínculo con inscripciones, relieves y templos. En una imagen, el rey puede aparecer más grande que los demás: no porque midiera más, sino para mostrar su importancia. Estas fuentes fueron hechas por el poder, así que muestran lo que el rey quería que se creyera, no necesariamente lo que pensaba la gente.",
        "Hoy separamos religión y política, pero en esa época estaban unidas: los templos recibían ofrendas, guardaban cebada y participaban en la economía, y el rey cumplía tareas religiosas. Por eso hay que evitar aplicar categorías actuales. Para entender la legitimación hay que mirar varias fuentes y preguntarse quién habla, a quién y para qué.",
    ],
    vocab=[("legitimación", "razones que hacen aceptar el poder de una autoridad"), ("faraón", "gobernante del Egipto antiguo"), ("sacerdote", "persona encargada de las ceremonias de un templo"), ("relieve", "imagen tallada en una superficie"), ("ofrenda", "cosa que se entrega a un dios")],
    worked=[
        ("Identificar un recurso de legitimación", "{F} ¿Qué razón da la fuente A para justificar el poder del rey?", ["Leo la frase de la inscripción.", "El rey dice que los dioses lo eligieron."], "Que los dioses lo eligieron"),
        ("Calcular proporciones en una imagen", "En un relieve de ejemplo, el rey mide 15 cm y los demás 5 cm. ¿Cuántas veces es más alto el rey?", ["Divido las alturas: 15 ÷ 5 = 3.", "El rey se dibuja con el triple de altura."], "3 veces más alto"),
    ],
    mistakes=[("Pensar que el rey medía más que los demás porque aparece más grande en el relieve.", "Se toma la imagen como una fotografía.", "El tamaño muestra importancia, no estatura real."),
              ("Creer que en esa época religión y política eran cosas separadas, como hoy.", "Se aplican categorías actuales.", "En esos Estados el poder y lo sagrado estaban unidos.")],
    T=[
        ("{F} ¿Quién eligió al rey según la fuente A?", "Los dioses", "La inscripción lo dice."),
        ("{F} ¿Qué recibe el sacerdote según la fuente B?", "Cebada", "La tablilla lo indica."),
        ("{F} ¿Qué entrega un dios al rey en la fuente C?", "Un símbolo de autoridad", "El relieve lo muestra."),
        ("=", "{F} ¿Cuántas veces mayor es la altura del rey que la de las demás figuras en la fuente C?", "12//4", "Se divide la altura del rey por la de las demás figuras.", " veces"),
        ("{F} ¿Cuál de las cuatro fuentes es una imagen y no un texto?", "La fuente C", "El relieve es una imagen tallada; las otras tres son textos."),
        ("{F} ¿Qué quiere lograr el rey con la fuente A?", "Que se acepte su poder", "Se presenta como elegido por los dioses."),
        ("=", "{F} Si el rey mide 12 cm y las demás figuras 4 cm, ¿cuántos centímetros más alto es el rey?", "12-4", "Se resta la altura de las demás figuras.", " cm"),
        ("{F} ¿En qué dos fuentes aparece el rey recibiendo su poder de los dioses?", "En la A y en la C", "En A lo eligen los dioses y en C un dios le entrega un símbolo de autoridad."),
        ("{F} ¿Por qué el rey aparece tan grande en la fuente C?", "Para mostrar su importancia, no su estatura real", "El tamaño es un recurso para señalar jerarquía."),
        ("{F} Pedro dice: «En esa época la religión y la política estaban separadas, como hoy». Corrígelo con la fuente B.", "El templo recibe cebada, la ofrece al dios y el palacio guarda una parte: lo religioso y lo económico estaban unidos", "La tablilla muestra templo y palacio relacionados."),
        ("{F} ¿Qué problema tiene usar solo la fuente A para saber qué pensaba el pueblo?", "Es la voz del rey y no muestra lo que pensaban las personas", "La fuente fue hecha por el poder."),
        ("{F} La fuente D dice que el pueblo celebra al rey cuando el río sube bien. ¿Qué idea sugiere sobre su poder?", "Que se relacionaba al rey con la fertilidad y las buenas cosechas", "La celebración une el río y el rey."),
        ("{F} ¿Qué otra fuente ayudaría a conocer la perspectiva del pueblo y no solo la del rey?", "Restos de casas, ofrendas de las familias o tablillas con quejas o pedidos de aldeanos", "Servirían fuentes creadas por personas comunes."),
    ],
    ctx=("Un museo exhibe un relieve donde el rey aparece el triple de alto que sus sirvientes. Un visitante dice: «Seguro era un gigante». ¿Qué le explicas? {F}", "Que el tamaño muestra importancia y no estatura real", "Los relieves usan el tamaño para señalar jerarquía."),
    sc=[("¿Qué es la legitimación del poder?", "Razones que hacen aceptar el poder de una autoridad", "Puede apoyarse en la religión."),
        ("¿Qué preguntas conviene hacer a una inscripción de un rey?", "Quién habla, a quién y con qué propósito", "Así se evita creerla sin examinarla."),
        ("{F} ¿Qué recibe el sacerdote en la tablilla del templo?", "Cebada", "La fuente B lo dice.")],
    op=("Escribe un cuadro con las fuentes A, B, C y D: quién la produjo, qué idea muestra y qué no permite saber. Después escribe una frase que explique cómo la religión ayudaba al poder del rey. {F}",
        "Fuente A: el rey; muestra que lo eligieron los dioses; no dice qué pensaba el pueblo.",
        ["completa las cuatro fuentes", "señala un límite en cada una", "la frase une religión y poder sin juicios de valor"], ["cuadro escrito", "frase escrita"], ["tomar las fuentes como verdad completa", "usar ideas actuales de separación entre religión y política"],
        "Pide que explique qué fuente le parece más fuerte y por qué."),
    reinforce="Explica con tus palabras qué es legitimar el poder.",
    extend="Escribe una pregunta sobre qué pensaba una campesina del tributo y de las ofrendas.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (esquema de ejemplo de la población de un Estado antiguo, con cifras inventadas para este cuaderno). "
     "Total: 1.000 personas. Rey y su familia: 10 personas. Sacerdotes y funcionarios: 90. Artesanos y comerciantes: 200. Campesinos: 650. Personas esclavizadas (sin libertad, capturadas o por deudas): 50. "
     "Tareas: los campesinos cultivan y pagan el tributo; los artesanos fabrican cerámica, telas y herramientas; los funcionarios recaudan y anotan; los sacerdotes realizan ceremonias; las personas esclavizadas trabajan para otros sin libertad ni pago.")
build(
    OA, 4, F,
    use="Aprenderé a analizar las jerarquías sociales y los tipos de trabajo en un Estado temprano. Sirve para entender quién producía, quién mandaba y quién no era libre.",
    prior=["Sé qué es un Estado.", "Sé qué es la especialización.", "Sé sumar y restar con números hasta mil."],
    explain=[
        "En los primeros Estados, la sociedad se organizó en jerarquías: grupos con distinto poder y prestigio. En la cima estaban el rey y su familia; luego, sacerdotes y funcionarios; después, artesanos y comerciantes; y la mayoría eran campesinos. Había además personas esclavizadas, que no tenían libertad.",
        "Cada grupo tenía formas de trabajo distintas. Los campesinos producían el alimento y entregaban tributo. Los artesanos fabricaban objetos. Los funcionarios recaudaban y anotaban. Los sacerdotes realizaban ceremonias. Las personas esclavizadas trabajaban para otros sin libertad ni pago. El Estado dependía sobre todo del trabajo de los campesinos.",
        "Un esquema por grupos simplifica la realidad. Dentro de cada grupo había diferencias, y las personas podían cambiar de situación por deudas, guerras o matrimonios. Además, las fuentes dicen poco sobre mujeres y niños. Algunas mujeres de la élite fueron sacerdotisas, pero la mayoría trabajaba en tareas como hilar, moler y cuidar a los hijos. Por eso hay que usar el esquema con cuidado.",
    ],
    vocab=[("jerarquía", "orden de grupos de mayor a menor poder o prestigio"), ("élite", "grupo pequeño con más poder y riqueza"), ("campesino", "persona que cultiva la tierra"), ("persona esclavizada", "persona sin libertad que trabaja para otro sin pago"), ("artesano", "persona que fabrica objetos con sus manos")],
    worked=[
        ("Leer una cifra", "{F} ¿Cuántas personas son campesinas?", ["Busco la categoría en la ficha.", "Hay 650 campesinos."], "650 personas"),
        ("Comparar grupos", "{F} ¿Cuántas personas más son artesanos y comerciantes que sacerdotes y funcionarios?", ["Artesanos y comerciantes: 200.", "Resto 200 − 90 = 110."], "110 personas"),
    ],
    mistakes=[("Creer que todas las personas de un grupo vivían igual.", "Se toma el esquema como descripción de cada vida.", "Dentro de cada grupo había diferencias de riqueza y de situación."),
              ("Decir que toda la sociedad trabajaba lo mismo que hoy.", "Se aplica la idea moderna de trabajo.", "Describe cada tarea según su grupo y su libertad.")],
    T=[
        ("{F} ¿Cuál es el grupo más numeroso?", "Los campesinos", "Son 650 de 1.000 personas."),
        ("{F} ¿Cuál es el grupo menos numeroso?", "El rey y su familia", "Son 10 personas."),
        ("{F} ¿Qué grupo recauda el tributo y anota?", "Los funcionarios", "La ficha asigna esa tarea a los funcionarios."),
        ("=", "{F} ¿Cuántas personas no son campesinas?", "1000-650", "Se resta la cantidad de campesinos al total.", " personas"),
        ("=", "{F} Si el rey y su familia y los sacerdotes y funcionarios forman la élite, ¿cuántas personas son de la élite?", "10+90", "Se suman ambos grupos.", " personas"),
        ("{F} ¿Qué significa que una persona está esclavizada según la ficha?", "Que no tiene libertad y trabaja para otros sin pago", "La ficha lo define así."),
        ("=", "{F} Si cada familia campesina pagara 2 sacos y fueran 100 familias, ¿cuántos sacos de tributo serían?", "100*2", "Se multiplican familias y sacos.", " sacos"),
        ("{F} Relaciona cada grupo con su tarea: campesinos, artesanos, sacerdotes. Tareas: ceremonias, cultivar, fabricar telas y cerámica.", "Campesinos: cultivar; artesanos: fabricar telas y cerámica; sacerdotes: ceremonias", "Cada grupo tiene su tarea en la ficha."),
        ("=", "{F} ¿Cuántas personas hay entre artesanos, comerciantes y personas esclavizadas?", "200+50", "Se suman ambos grupos.", " personas"),
        ("{F} ¿Por qué el Estado depende sobre todo del trabajo de los campesinos?", "Porque producen el alimento y entregan el tributo", "Son la mayoría y sostienen a los demás grupos."),
        ("{F} Lucía dice: «Los 650 campesinos vivían todos igual». ¿Por qué no se puede afirmar?", "Porque el esquema agrupa y simplifica; dentro del grupo podía haber diferencias", "Un esquema no describe cada vida."),
        ("{F} La ficha no dice cuántas mujeres hay en cada grupo. ¿Se puede conocer con ella cómo vivían las mujeres? Explica.", "No: se necesitan otras fuentes que hablen de ellas", "La ficha agrupa por oficio sin separar por sexo."),
        ("{F} Ordena los grupos de mayor a menor número de personas: sacerdotes y funcionarios, campesinos, artesanos y comerciantes, rey y su familia.", "Campesinos, artesanos y comerciantes, sacerdotes y funcionarios, rey y su familia", "Las cifras son 650, 200, 90 y 10."),
    ],
    ctx=("Una compañera dibuja el esquema de la ficha como una pirámide con el rey arriba y los campesinos abajo. ¿Qué muestra la forma de la pirámide? {F}", "Que hay pocos con más poder arriba y muchos con menos poder abajo", "La base más ancha representa a los campesinos."),
    sc=[("¿Qué es una jerarquía?", "Un orden de grupos de mayor a menor poder o prestigio", "Define quién está más arriba."),
        ("¿Qué grupo trabajaba sin libertad ni pago?", "Las personas esclavizadas", "Así lo define la ficha."),
        ("=", "{F} ¿Cuántas personas son sacerdotes y funcionarios, más personas esclavizadas?", "90+50", "Se suman ambos grupos.", " personas")],
    op=("Dibuja una pirámide con los cinco grupos de la ficha, escribe cuántas personas hay en cada uno y una tarea. Después escribe dos líneas sobre una limitación del esquema. {F}",
        "Pirámide con rey (10), sacerdotes y funcionarios (90), artesanos y comerciantes (200), campesinos (650) y esclavizados (50) con una tarea cada uno.",
        ["los cinco grupos con sus cifras", "una tarea por grupo", "una limitación explicada"], ["pirámide dibujada", "dos líneas escritas"], ["ordenar mal los grupos", "no señalar que el esquema simplifica"],
        "Pide que explique por qué a veces una persona podía cambiar de grupo."),
    reinforce="Nombra los cinco grupos sociales de la ficha y una tarea de cada uno.",
    extend="Escribe una pregunta sobre cómo se podía llegar a ser esclavizado y qué evidencia lo mostraría.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (caso de ejemplo y datos generales, hechos para este cuaderno). "
     "Un valle tiene 20 canales de riego: el palacio controla 12 y las aldeas, 8. "
     "Cinco factores que ayudan a que un Estado se consolide: 1) riego organizado; 2) ejército que protege rutas y cobra tributo; 3) templo que justifica el poder; 4) escritura para registros y leyes; 5) comercio de metales y sal controlado por el palacio. "
     "Estados reales fueron distintos entre sí: en Mesopotamia hubo ciudades-Estado, en Egipto un faraón gobernó un reino a lo largo del Nilo, y en el valle del Indo, según los hallazgos hasta hoy, hay pocas huellas de palacios o de reyes.")
build(
    OA, 5, F,
    use="Aprenderé a explicar el origen del poder en los primeros Estados con varias causas. Sirve para no reducirlo a una sola razón.",
    prior=["Sé qué es un Estado y cómo se justificaba el poder.", "Sé qué es una explicación multicausal.", "Sé comparar casos."],
    explain=[
        "Los Estados tempranos se consolidaron por varias causas a la vez. El riego organizado daba más cosechas y exigía coordinar el trabajo. El ejército protegía rutas y hacía cumplir el tributo. El templo ofrecía razones religiosas. La escritura permitía llevar registros y leyes. El comercio de metales o sal aportaba riqueza.",
        "Ninguna causa explica todo por sí sola, y su peso cambió según el lugar. Además, los primeros Estados no fueron iguales: en Mesopotamia hubo ciudades-Estado independientes, en Egipto un faraón gobernó un reino a lo largo del Nilo, y en el valle del Indo hay pocas huellas de palacios o de reyes. Esto muestra que no hubo un único camino hacia el poder.",
        "Para construir una explicación sólida se nombran varias causas, se usan fuentes de distintos tipos y se reconocen los límites de la evidencia. Por ejemplo, no sabemos cuánto pesó cada causa en cada lugar, ni qué pensaban las personas comunes. Una explicación honesta dice qué sabemos, qué suponemos y qué falta.",
    ],
    vocab=[("consolidarse", "hacerse firme y estable un poder o una organización"), ("ciudad-Estado", "ciudad con su territorio que se gobierna de manera independiente"), ("reino", "territorio gobernado por un rey o faraón"), ("multicausal", "que se explica por varias causas"), ("factor", "elemento que influye en un resultado")],
    worked=[
        ("Identificar una causa", "{F} ¿Qué factor de la ficha ayuda a llevar registros y leyes?", ["Reviso la lista de cinco factores.", "El factor 4 es la escritura."], "La escritura"),
        ("Calcular una diferencia", "{F} ¿Cuántos canales más controla el palacio que las aldeas?", ["El palacio controla 12 y las aldeas 8.", "Resto: 12 − 8 = 4."], "4 canales más"),
    ],
    mistakes=[("Explicar el poder de un Estado solo por su ejército.", "Se elige una sola causa.", "Combina varias causas y di cuál pudo pesar más en cada caso."),
              ("Creer que el valle del Indo fue igual a Egipto.", "Se supone un único modelo de Estado.", "Compara los rasgos y reconoce que la evidencia muestra diferencias.")],
    T=[
        ("{F} ¿Cuántos canales de riego hay en el valle?", "20", "La ficha lo indica."),
        ("{F} ¿Cuántos factores de consolidación nombra la ficha?", "5", "Son cinco, numerados del 1 al 5."),
        ("{F} ¿Qué factor de la ficha está ligado a la religión?", "El templo que justifica el poder", "Es el factor 3."),
        ("=", "{F} En total, ¿cuántos canales hay sumando los del palacio y los de las aldeas?", "12+8", "Se suman ambos números.", " canales"),
        ("{F} ¿En cuál de los lugares de la ficha gobernó un faraón?", "En Egipto", "La ficha lo dice."),
        ("{F} ¿Qué lugar de la ficha tiene pocas huellas de palacios o de reyes?", "El valle del Indo", "La ficha lo indica."),
        ("{F} Clasifica cada factor como económico (E), político-militar (P) o religioso (R): 1) riego organizado; 2) ejército; 3) templo; 4) comercio controlado por el palacio.", "1 E, 2 P, 3 R, 4 E", "El riego y el comercio producen riqueza; el ejército usa fuerza; el templo da razones sagradas."),
        ("=", "{F} Si el palacio controla 12 de los 20 canales, ¿cuántos canales controlan las aldeas?", "20-12", "Se resta lo que controla el palacio al total.", " canales"),
        ("{F} ¿Cómo se refuerzan el riego organizado y el tributo?", "El riego da más cosecha, con lo que se puede cobrar más tributo, que financia nuevas obras", "Cada factor facilita al otro."),
        ("{F} Pedro dice: «El ejército explica todo el poder de los primeros Estados». Da dos factores de la ficha que muestren que no.", "Por ejemplo: el riego organizado y el templo que justifica el poder", "La ficha nombra varios factores."),
        ("{F} ¿Por qué no se puede decir que todos los primeros Estados fueron iguales?", "Porque en Mesopotamia hubo ciudades-Estado, en Egipto un reino con faraón y en el Indo hay pocas huellas de reyes", "La ficha muestra diferencias entre los casos."),
        ("{F} ¿Qué no se puede saber con la ficha sobre los factores que ayudaron a consolidar un Estado?", "Cuánto pesó cada factor en cada lugar", "La ficha los nombra, pero no mide su peso."),
        ("{F} Un compañero dice que el comercio no importaba para el poder. ¿Qué dato de la ficha le muestra un error?", "El palacio controlaba el comercio de metales y sal, lo que le daba riqueza", "El factor 5 es el comercio controlado por el palacio."),
    ],
    ctx=("Un museo presenta la sala «El poder en un valle» con un canal, un ejército, un templo y tablillas. ¿Qué idea clave debe transmitir el rótulo para no reducir todo a una causa? {F}", "Que el poder se consolidó por varias causas combinadas", "La sala muestra factores distintos que se refuerzan."),
    sc=[("¿Qué es una ciudad-Estado?", "Una ciudad con su territorio que se gobierna de manera independiente", "Es el caso de Mesopotamia."),
        ("¿Por qué una explicación sobre el poder no debe tener una sola causa?", "Porque varios factores actuaron juntos y su peso cambió según el lugar", "Las evidencias muestran más de un factor."),
        ("{F} ¿Cuántos canales de riego controlan las aldeas?", "8", "La ficha lo indica.")],
    op=("Escribe una explicación de 6 líneas sobre cómo se consolidó el poder en el valle de la ficha: usa tres factores, di cómo se refuerzan entre sí y escribe una línea sobre algo que no podemos saber. {F}",
        "Riego organizado, ejército y templo se refuerzan; no sabemos cuánto pesó cada uno.",
        ["usa tres factores de la ficha", "explica cómo se refuerzan", "reconoce un límite"], ["explicación escrita"], ["usar una sola causa", "no mencionar ningún límite"],
        "Pide que compare su explicación con el caso del valle del Indo."),
    reinforce="Nombra los cinco factores de la ficha en voz alta.",
    extend="Escribe una pregunta sobre cómo pudo mantenerse el orden en un lugar sin huellas claras de reyes.",
)
