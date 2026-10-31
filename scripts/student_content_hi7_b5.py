"""Cuaderno del estudiante, 7.º básico Historia, Geografía y Ciencias Sociales: OA 15 (culturas maya, azteca e inca)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA = "HI07 OA 15"

# ================================================================ clase 1
lesson(
    OA, 1,
    "Aprenderé a examinar el arte, la arquitectura y la escritura de mayas, aztecas e incas. Sirve para reconocer qué tipo de obra corresponde a cada civilización.",
    ["Sé ubicar a mayas, aztecas e incas en el mapa y en el tiempo.", "Sé que una obra de arte es una fuente histórica."],
    [
        "Los mayas escribían con glifos, signos que representaban palabras y sílabas. Los grabaron en piedra, en cerámica y en libros de papel de corteza llamados códices. Construyeron templos-pirámide, palacios y estelas, que son columnas de piedra con retratos de gobernantes y fechas. También pintaron murales.",
        "Los aztecas construyeron el Templo Mayor y grandes esculturas de piedra. Una de las más conocidas es la Piedra del Sol, un gran disco de piedra con signos del calendario. Los aztecas usaron escritura con imágenes (pictogramas) en códices y hacían mosaicos y objetos con plumas.",
        "Los incas no tuvieron escritura como la maya, pero usaron el quipu para registrar cantidades. Su arquitectura se reconoce por muros de piedras muy bien cortadas que encajan sin mortero, y por puertas y ventanas en forma de trapecio. Machu Picchu y Sacsayhuamán son ejemplos. Sus textiles tenían diseños geométricos de gran calidad. Comparar el arte de las tres civilizaciones ayuda a ver qué materiales, técnicas y mensajes eligió cada una.",
    ],
    [("glifo", "signo de la escritura maya"), ("estela", "columna de piedra con imágenes y textos"), ("códice", "libro pintado o escrito por pueblos mesoamericanos"), ("pictograma", "dibujo que representa una idea o un objeto"), ("trapecio", "figura de cuatro lados con dos paralelos y dos que se inclinan"), ("mortero", "mezcla que une piedras o ladrillos")],
    [
        ("Reconocer una obra", "Una ficha de ejemplo dice: «Muro de piedras cortadas que encajan sin mortero, con una puerta en forma de trapecio». ¿A qué civilización corresponde?", ["Muros que encajan sin mortero.", "Puertas trapezoidales.", "Es inca."], "Inca"),
        ("Distinguir la escritura", "Un códice de ejemplo muestra dibujos en secuencia que cuentan un viaje. ¿Qué tipo de escritura es?", ["Son imágenes.", "Es pictográfica."], "Pictográfica"),
    ],
    [
        ("Creer que todas las civilizaciones andinas y mesoamericanas escribían igual.", "Los mayas usaban glifos, los aztecas pictogramas y los incas el quipu.", "Nombra el sistema de cada una."),
        ("Pensar que sin escritura alfabética no había registro.", "Los incas registraron cantidades con quipus y los aztecas con códices pintados.", "Pregunta qué sistema usaban."),
    ],
    [
        ("En la unidad de culturas americanas, ¿qué es un glifo?", "Un signo de la escritura maya", "Es la definición del vocabulario."),
        ("¿Qué gran disco de piedra con signos del calendario es azteca?", "La Piedra del Sol", "La clase la menciona."),
        ("¿Qué sitio inca tiene muros de piedra que encajan sin mortero?", "Machu Picchu o Sacsayhuamán", "Son los ejemplos de la clase."),
    ],
    [
        ("¿Qué mostraban las estelas mayas?", "Retratos de gobernantes y fechas", "Eran columnas con imágenes y textos."),
        ("¿Qué usaban los incas para registrar cantidades?", "El quipu", "Es el sistema de cuerdas con nudos."),
        ("¿Qué forma tenían las puertas incas?", "Forma de trapecio", "Es un rasgo de su arquitectura."),
    ],
    [
        ("Una ficha de ejemplo dice: «Libro de papel de corteza con signos que representan sílabas y palabras». ¿Qué civilización es más probable?", "La maya", "Los glifos son escritura maya."),
        ("Una ficha de ejemplo dice: «Mosaico de plumas de colores usado en un adorno». ¿Qué civilización de la clase hacía objetos con plumas?", "La azteca", "La clase menciona objetos con plumas en los aztecas."),
        ("Observa dos muros: A) piedras irregulares unidas con barro; B) piedras muy bien cortadas que encajan sin mortero. ¿Cuál es más probable que sea una obra inca?", "B", "El corte exacto sin mortero es un rasgo inca."),
    ],
    [
        ("Luis dice: «Los incas no dejaron registros porque no tenían escritura». Da un argumento de la clase en contra.", "Usaron quipus para registrar cantidades", "Tenían un sistema de registro."),
        ("¿Por qué se dice que el arte es una fuente histórica?", "Porque muestra materiales, técnicas, creencias y formas de vida de quien lo hizo", "Una obra aporta información sobre su época."),
    ],
    [
        ("Relaciona cada sistema de registro con su civilización, en este orden: glifos, quipu, pictogramas.", "Maya, inca, azteca", "Los glifos son mayas, el quipu es inca y los pictogramas son aztecas."),
        ("Un estudiante dice: «El Templo Mayor y Machu Picchu son de la misma civilización». ¿Qué corrección haces?", "El Templo Mayor es azteca y Machu Picchu es inca", "Son civilizaciones y regiones distintas."),
    ],
    [("Un museo de ejemplo tiene tres piezas: una estela con signos y un retrato, un disco de piedra con signos del calendario y un muro de piedras que encajan sin mortero. ¿A qué civilización corresponde cada una, en ese orden?", "Maya, azteca, inca", "Cada pieza coincide con un rasgo descrito.")],
    [("En la unidad de culturas americanas, ¿qué es una estela?", "Una columna de piedra con imágenes y textos", "Es la definición del vocabulario."), ("En la unidad de culturas americanas, ¿qué es un pictograma?", "Un dibujo que representa una idea o un objeto", "Es la definición del vocabulario."), ("¿Qué usaban los incas en vez de escritura alfabética?", "Quipus", "Eran cuerdas con nudos para registrar cantidades.")],
    (
        "Elige una de estas obras y descríbela en seis líneas: A) una estela maya con un gobernante y fechas; B) la Piedra del Sol azteca; C) un muro inca de Machu Picchu. Indica el material, la técnica, qué mensaje transmite y qué te permite concluir sobre la civilización. Termina con un límite de lo que no podemos saber solo viéndola.",
        "C: muro de piedras cortadas que encajan sin mortero; muestra dominio de la técnica; no sabemos quiénes lo construyeron exactamente.",
        ["indica el material", "indica la técnica", "indica el mensaje o uso", "incluye un límite"],
        ["descripción de seis líneas con cuatro elementos"],
        ["mezclar civilizaciones", "no incluir límite"],
        "Muestra tu descripción a una persona de tu casa y pídele que adivine cuál obra elegiste.",
    ),
    "Dibuja un glifo inventado, un pictograma y un quipu simple y rotula cada uno.",
    "Averigua dónde se conserva hoy la Piedra del Sol y cuánto pesa aproximadamente.",
)

# ================================================================ clase 2
lesson(
    OA, 2,
    "Aprenderé a comparar los conocimientos matemáticos y astronómicos de mayas, aztecas e incas. Sirve para entender cómo medían el tiempo y qué observaban del cielo.",
    ["Sé contar en base 10.", "Sé que los calendarios organizan el tiempo."],
    [
        "Los mayas usaban un sistema de numeración en base 20. Escribían con puntos, barras y un signo para el cero, hecho con forma de concha. Un punto vale 1 y una barra vale 5. El segundo nivel, hacia arriba, vale 20 por cada unidad. Así, un punto en el segundo nivel y tres puntos abajo valen 20 + 3 = 23.",
        "Mayas y aztecas usaron dos calendarios que se combinaban: uno de 365 días, ligado a las estaciones, y otro de 260 días, ligado a rituales. Los dos coinciden de nuevo cada 52 años, ciclo que llamamos Rueda Calendárica. Los mayas observaron con cuidado el Sol, la Luna y Venus, y registraron eclipses y ciclos de Venus.",
        "Los incas usaron el quipu con un sistema decimal: la posición de los nudos indicaba unidades, decenas, centenas. También observaron el Sol y las estaciones, y celebraban fiestas ligadas a los solsticios. Su calendario se basaba en la Luna y el Sol. Cada civilización respondió a sus necesidades agrícolas y religiosas con las herramientas que tenía.",
    ],
    [("base 20", "sistema de numeración que agrupa de 20 en 20"), ("calendario", "sistema para organizar y medir el tiempo"), ("solsticio", "día del año en que el Sol alcanza su punto más alto o más bajo"), ("Venus", "planeta visible desde la Tierra, muy brillante al amanecer o al atardecer"), ("decimal", "sistema que agrupa de 10 en 10"), ("eclipse", "momento en que un astro tapa a otro")],
    [
        ("Leer un número maya", "Una barra y tres puntos en el primer nivel. ¿Qué número es?", ["La barra vale 5.", "Cada punto vale 1.", "5 + 3 = 8."], "8"),
        ("Leer un número maya de dos niveles", "Un punto en el segundo nivel y dos puntos en el primero. ¿Qué número es?", ["El segundo nivel vale 20 por unidad.", "20 + 2 = 22."], "22"),
    ],
    [
        ("Pensar que el cero lo inventaron los europeos.", "Los mayas usaron un signo para el cero desde antes de que los europeos llegaran a América.", "Reconoce el uso del cero en el sistema maya."),
        ("Mezclar los dos calendarios.", "Uno tiene 365 días y el otro 260.", "Pregunta siempre cuántos días tiene cada uno."),
    ],
    [
        ("¿En qué base contaban los mayas?", "En base 20", "Es la definición del vocabulario."),
        ("¿Cuántos días tiene el calendario mesoamericano ligado a las estaciones?", "365 días", "La explicación lo dice."),
        ("¿Qué usaban los incas para registrar números?", "El quipu", "Es el sistema de cuerdas y nudos."),
    ],
    [
        ("¿Cuánto vale una barra en la numeración maya?", "5", "Una barra vale 5 y un punto 1."),
        ("¿Cada cuántos años coinciden de nuevo los dos calendarios?", "Cada 52 años", "Es el ciclo de la Rueda Calendárica."),
        ("¿Qué astro observaban los mayas con especial cuidado además del Sol y la Luna?", "Venus", "La clase lo menciona."),
    ],
    [
        ("Una barra, una barra y dos puntos, todos en el primer nivel. ¿Qué número maya es?", "12", "Dos barras valen 10 y dos puntos valen 2, así que 10 + 2 = 12."),
        ("Dos puntos en el segundo nivel y una barra en el primero. ¿Qué número es?", "45", "Cada punto del segundo nivel vale 20, así que 40, más 5 de la barra."),
        arith("Un ciclo de 52 años de 365 días tiene cuántos días en total (sin contar años bisiestos)?", "52*365", "Se multiplica el número de años por los días de cada año."),
    ],
    [
        ("Luis dice: «El quipu era igual al sistema maya de puntos y barras». ¿Qué diferencia de la clase puedes dar?", "El quipu usaba cuerdas con nudos en sistema decimal y el maya puntos y barras en base 20", "Cambian el soporte y la base."),
        ("Marta dice: «Los pueblos americanos no hacían astronomía». Cita un hecho de la clase en contra.", "Los mayas registraron ciclos de Venus y eclipses", "La clase lo menciona."),
    ],
    [
        ("Tres números mayas: A = tres barras, B = un punto en el segundo nivel y un punto en el primero, C = cuatro puntos. Ordénalos de menor a mayor.", "C, A, B", "C vale 4, A vale 15 y B vale 21."),
        ("Un número maya tiene un punto en el segundo nivel, una barra y cuatro puntos en el primero. ¿Qué número es?", "29", "20 más 5 más 4 son 29."),
    ],
    [("Un agricultor de ejemplo sabe que el calendario de 260 días marca las fiestas y el de 365 las estaciones. ¿Cuál debe usar para saber cuándo sembrar?", "El de 365 días", "Está ligado a las estaciones.")],
    [("En la unidad de culturas americanas, ¿qué es un solsticio?", "El día del año en que el Sol alcanza su punto más alto o más bajo", "Es la definición del vocabulario."), ("¿Qué signo usaban los mayas para el cero?", "Una concha", "Es parte de su sistema."), ("¿Qué base usaban los incas con el quipu?", "Decimal", "Tenían un sistema de 10 en 10.")],
    (
        "Escribe una tabla con tres números mayas: 7, 15 y 24. Para cada uno dibuja con puntos y barras cómo se escribiría y explica cuántas barras y puntos usas. Después escribe cuatro líneas comparando el sistema maya con el sistema decimal que usamos hoy.",
        "7: una barra y dos puntos; 15: tres barras; 24: un punto en el segundo nivel y cuatro puntos en el primero.",
        ["escribe correctamente los tres números", "explica barras y puntos", "compara con nuestro sistema", "usa el segundo nivel en 24"],
        ["tabla de tres números y cuatro líneas de comparación"],
        ["usar la barra como 10", "olvidar el segundo nivel"],
        "Pide a una persona de tu casa que lea tus números como si fuera maya.",
    ),
    "Inventa tres números del 1 al 19 y escríbelos en notación maya.",
    "Averigua qué fue la Piedra del Sol y qué calendario representa.",
)

# ================================================================ clase 3
lesson(
    OA, 3,
    "Aprenderé a relacionar la religión, la política y la vida cotidiana de mayas, aztecas e incas. Sirve para entender que creencias, poder y rutina diaria estaban conectados.",
    ["Sé que las civilizaciones tenían gobernantes y dioses.", "Sé que una creencia puede explicar prácticas sociales."],
    [
        "En las tres civilizaciones el poder político se relacionaba con la religión. Los gobernantes mayas se mostraban como intermediarios con los dioses; entre ellos había dioses de la lluvia, como Chaac. Los aztecas veneraban a Huitzilopochtli, ligado al Sol y a la guerra, a Tláloc, dios de la lluvia, y a Quetzalcóatl, serpiente emplumada. Los incas veneraban al Sol (Inti), a Viracocha, creador, y a la Pachamama, la Madre Tierra; el Sapa Inca se consideraba hijo del Sol.",
        "La vida cotidiana también tenía rutinas propias. En Mesoamérica se comía maíz en forma de tortillas y tamales, con frijoles y chile. En los Andes la papa y el maíz eran básicos, y la papa se conservaba deshidratada como chuño. Había diferencias de género: las mujeres tejían, cocinaban y comerciaban en los mercados; algunas fueron gobernantes mayas; entre los incas existían las acllas, mujeres escogidas que tejían y servían en templos. Los varones hacían trabajo agrícola, militar y en obras públicas.",
        "Los ritos funerarios mostraban creencias sobre la vida y la muerte. Los mayas enterraban a los gobernantes en tumbas con ofrendas, como las de Palenque con máscaras de jade. Los incas conservaban las momias de sus gobernantes y las cuidaban con ofrendas. Entre los aztecas, la forma de morir determinaba el destino del difunto y se usaba la cremación. Estos datos vienen de la arqueología y de crónicas, así que requieren cautela.",
    ],
    [("Pachamama", "Madre Tierra en las creencias andinas"), ("Inti", "dios Sol de los incas"), ("ofrenda", "objeto o alimento que se entrega a un dios o a un difunto"), ("aclla", "mujer escogida inca que tejía y servía en templos"), ("rito funerario", "ceremonia relacionada con la muerte"), ("momia", "cuerpo conservado de un difunto")],
    [
        ("Relacionar creencia y poder", "El Sapa Inca se consideraba hijo del Sol. ¿Qué efecto político tenía esa creencia?", ["Si es hijo de un dios, su mando parece legítimo.", "Refuerza su autoridad."], "Reforzaba su autoridad ante el pueblo"),
        ("Reconocer un alimento", "Un plato de ejemplo se hace con papa deshidratada llamada chuño. ¿Es más probable que sea de los Andes o de Mesoamérica?", ["La papa es andina.", "Chuño es un alimento andino."], "De los Andes"),
    ],
    [
        ("Creer que las creencias de las tres civilizaciones eran iguales.", "Tenían dioses y prácticas distintas, aunque compartieran la veneración del Sol y de la lluvia.", "Nombra el dios y la civilización."),
        ("Interpretar un rito funerario con ideas de hoy.", "Cada rito responde a creencias propias sobre la muerte.", "Pregunta qué creía cada pueblo."),
    ],
    [
        ("¿Cómo se llamaba el dios Sol de los incas?", "Inti", "Está en el vocabulario."),
        ("¿Quién era Chaac para los mayas?", "El dios de la lluvia", "La clase lo menciona."),
        ("¿Qué conservaban los incas de sus gobernantes?", "Las momias", "Las cuidaban con ofrendas."),
    ],
    [
        ("¿Quién era Huitzilopochtli para los aztecas?", "Un dios ligado al Sol y a la guerra", "La explicación lo describe así."),
        ("¿Qué eran las acllas?", "Mujeres escogidas que tejían y servían en templos", "Es la definición del vocabulario."),
        ("¿Qué alimento básico de Mesoamérica se comía en tortillas y tamales?", "El maíz", "Es el alimento de la explicación."),
    ],
    [
        ("Una tumba de ejemplo de Palenque tiene una máscara de jade y ofrendas. ¿Qué civilización es más probable?", "La maya", "La clase menciona tumbas con máscaras de jade en Palenque."),
        ("Una crónica de ejemplo dice que las mujeres vendían tejidos en el mercado. ¿Qué dato de la clase la respalda?", "Las mujeres comerciaban en los mercados", "Es un rol femenino mencionado."),
        ("Un lugar de ejemplo cuida momias con ofrendas de comida. ¿Qué civilización es más probable?", "La inca", "Los incas conservaban momias de sus gobernantes."),
    ],
    [
        ("Pedro dice: «Todas las mujeres de estas civilizaciones tenían el mismo rol». Da un dato en contra.", "Algunas fueron gobernantes mayas y otras eran acllas incas", "Había roles distintos."),
        ("¿Por qué conviene usar cautela con las crónicas sobre ritos?", "Porque fueron escritas por españoles y pueden estar sesgadas", "Hay que contrastar con la arqueología."),
    ],
    [
        ("¿Cuál de estos dos datos muestra un rito funerario? A) comer tortillas de maíz B) cuidar momias con ofrendas.", "B", "Cuidar momias es una práctica ligada a la muerte; las tortillas son comida cotidiana."),
        ("Relaciona el dios con la civilización: Viracocha, Tláloc, Chaac. Responde en ese orden.", "Inca, azteca, maya", "Viracocha es inca, Tláloc azteca y Chaac maya."),
    ],
    [("Datos de ejemplo: 1) un gobernante se presenta como hijo del Sol; 2) una familia cocina tortillas de maíz. ¿Cuál dato une religión y política y cuál muestra la vida cotidiana?", "El 1 une religión y política; el 2 muestra la vida cotidiana", "Ser hijo del Sol da autoridad religiosa y política; cocinar es rutina diaria.")],
    [("En la unidad de culturas americanas, ¿qué es una ofrenda?", "Un objeto o alimento que se entrega a un dios o a un difunto", "Es la definición del vocabulario."), ("¿Quién era la Pachamama?", "La Madre Tierra en las creencias andinas", "Es la definición del vocabulario."), ("¿Cómo se conservaba la papa en los Andes?", "Deshidratada como chuño", "Se explica en el texto.")],
    (
        "Elige una de las tres civilizaciones y escribe un texto de seis líneas que relacione religión, poder y vida cotidiana. Incluye un dios, una autoridad, un alimento y un rito funerario. Escribe al final una duda sobre las fuentes.",
        "Inca: Inti, hijo del Sol, el Sapa Inca, la papa y el chuño, las momias cuidadas; duda: las crónicas son españolas.",
        ["incluye un dios", "incluye una autoridad", "incluye un alimento", "incluye un rito funerario y una duda"],
        ["texto de seis líneas con cinco elementos"],
        ["mezclar civilizaciones", "no incluir duda"],
        "Léele tu texto a una persona de tu casa y pídele que adivine la civilización.",
    ),
    "Anota un alimento mesoamericano y uno andino que hoy comes y qué uso le damos.",
    "Averigua qué hacían los aztecas en la fiesta del Sol y qué dicen las fuentes de ello.",
)

# ================================================================ clase 4
lesson(
    OA, 4,
    "Aprenderé a analizar la agricultura y las tecnologías de mayas, aztecas e incas. Sirve para comparar cómo resolvieron la alimentación y el trabajo en ambientes distintos.",
    ["Sé qué son terrazas, chinampas y milpas.", "Sé que cada ambiente exige técnicas diferentes."],
    [
        "Los mayas, aztecas e incas dependían de la agricultura. En Mesoamérica el cultivo básico era el maíz, con frijol y zapallo; los mayas usaron terrazas, campos elevados y depósitos de agua, y los aztecas, chinampas. En los Andes los incas cultivaban papa, maíz y quinua en andenes, escalones construidos en la ladera con muros de piedra y canales de riego. Los andenes evitaban la erosión y creaban microclimas.",
        "Una diferencia importante fue el transporte. En Mesoamérica no había animales de tiro y la carga se llevaba a pie; en los Andes se usaban llamas para llevar carga. Los incas almacenaban alimentos en collcas y deshidrataban papas como chuño. Los aztecas conservaban maíz en graneros. También usaban herramientas simples, como el palo cavador, para sembrar.",
        "Estas tecnologías eran sostenibles y adecuadas a su ambiente. Compararlas permite ver soluciones distintas a problemas similares: poca tierra plana, lluvias irregulares y necesidad de guardar alimentos. Los pueblos actuales de la región conservan muchos cultivos y algunas técnicas.",
    ],
    [("andén", "terraza de cultivo con muros de piedra de los Andes"), ("quinua", "cereal andino de alto valor alimentario"), ("erosión", "pérdida de suelo por agua o viento"), ("riego", "aporte de agua a los cultivos"), ("palo cavador", "palo con punta para hacer hoyos y sembrar"), ("microclima", "clima particular de un lugar pequeño")],
    [
        ("Elegir la técnica", "Una ladera empinada de los Andes necesita cultivarse sin que la lluvia arrastre el suelo. ¿Qué técnica inca sirve?", ["Hay que crear terrazas con muros.", "Se llaman andenes."], "Andenes"),
        ("Elegir el transporte", "Un grupo debe llevar cargas en los Andes por un camino empinado. ¿Qué animal usaban los incas?", ["Era un animal de carga andino.", "Es la llama."], "La llama"),
    ],
    [
        ("Creer que en América se usaban bueyes y carretas.", "No había animales de tiro grandes en Mesoamérica; en los Andes se usaban llamas para carga.", "Piensa en los animales que sí existían."),
        ("Pensar que las técnicas eran primitivas.", "Eran soluciones adaptadas, sostenibles y complejas.", "Describe el problema que resolvían."),
    ],
    [
        ("Nombra dos cultivos básicos de los Andes.", "Dos de estos: papa, maíz, quinua", "Son los cultivos andinos de la explicación."),
        ("¿Cómo se llamaban las terrazas de cultivo de los Andes?", "Andenes", "Está en el vocabulario."),
        ("¿Para qué servía el riego?", "Para dar agua a los cultivos", "Es la definición del vocabulario."),
    ],
    [
        ("¿Qué animal cargaba cosas en los Andes y no en Mesoamérica?", "La llama", "La clase lo indica."),
        ("¿Por qué los andenes evitaban la erosión?", "Porque sus muros retenían el suelo en la ladera", "Los escalones sujetaban el suelo."),
        ("¿Dónde guardaban los incas sus alimentos?", "En collcas", "Eran depósitos estatales."),
    ],
    [
        arith("Un andén de ejemplo mide 40 m de largo y 3 m de ancho. ¿Cuántos metros cuadrados tiene?", "40*3", "Largo por ancho.", " m²"),
        ("Un campo de ejemplo tiene tres niveles de andenes, cada uno con 150 plantas de papa. ¿Cuántas plantas hay en total?", "3*150", "Se multiplican los niveles por las plantas."),
        ("Un agricultor de ejemplo debe guardar papas por varios meses. ¿Qué técnica andina de la clase le conviene?", "Deshidratarlas como chuño", "La deshidratación permite conservarlas."),
    ],
    [
        ("Marta dice: «Los cultivos de maíz y papa eran iguales en toda América». ¿Qué corrección haces?", "El maíz era básico en Mesoamérica y la papa era básica en los Andes", "Cada región tenía cultivos propios."),
        ("Pedro dice: «Las chinampas y los andenes resolvían el mismo problema». Explica qué problema distinto resolvía cada una.", "Las chinampas creaban tierra de cultivo en el agua y los andenes evitaban la erosión en laderas", "Resuelven problemas distintos."),
    ],
    [
        ("¿Qué técnica sirve para cultivar dentro de un lago poco profundo? A) chinampa B) andén.", "A", "La chinampa es una isla artificial de cultivo en un lago; el andén es una terraza de ladera."),
        ("Una afirmación dice: «Los aztecas, mayas e incas compartieron una sola técnica agrícola». ¿Qué dos técnicas distintas de la clase la contradicen?", "Chinampas aztecas y andenes incas", "Son técnicas diferentes."),
    ],
    [("Un agricultor de ejemplo vive en una montaña con poca tierra plana y lluvias irregulares. Elige la solución: A) construir andenes con riego. B) cultivar en un lago.", "A", "Los andenes sirven en laderas.")],
    [("En la unidad de culturas americanas, ¿qué es un andén?", "Una terraza de cultivo con muros de piedra de los Andes", "Es la definición del vocabulario."), ("¿Qué animal servía de carga en los Andes?", "La llama", "La explicación lo dice."), ("¿Qué cereal andino de alto valor alimentario se menciona?", "La quinua", "Es parte de la explicación.")],
    (
        "Completa una tabla con tres filas (mayas, aztecas, incas) y tres columnas (cultivo base, técnica, transporte). Usa solo datos de la clase y escribe «no mencionado» donde no haya dato. Escribe después tres líneas explicando por qué las técnicas se adaptaron a cada ambiente.",
        "Mayas: maíz, terrazas, a pie. Aztecas: maíz, chinampas, a pie. Incas: papa, andenes, llamas.",
        ["completa nueve casillas", "usa datos de la clase", "marca lo no mencionado", "explica la adaptación"],
        ["tabla de nueve casillas y tres líneas de explicación"],
        ["poner llamas en Mesoamérica", "confundir chinampa con andén"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga cuál técnica le parece más ingeniosa.",
    ),
    "Dibuja un andén en corte lateral con su muro, el suelo y un canal de riego.",
    "Averigua qué variedades de papa existen hoy en Chile y de dónde provienen.",
)

# ================================================================ clase 5
lesson(
    OA, 5,
    "Aprenderé a comunicar similitudes entre mayas, aztecas e incas sin borrar sus diferencias, y a identificar lo que persiste hasta hoy. Sirve para cerrar la unidad con una explicación justa.",
    ["Sé comparar con criterios claros.", "Sé que muchas palabras y alimentos actuales vienen de América."],
    [
        "Las tres civilizaciones compartieron algunos rasgos: agricultura avanzada, calendarios, observación del cielo, arquitectura monumental y religiones ligadas a la naturaleza. Pero se diferenciaron en la escritura (glifos, pictogramas, quipus), en el cultivo base (maíz o papa), en el transporte y en la forma de gobierno. Comunicar bien significa nombrar ambas cosas: «las tres..., pero los mayas..., los aztecas... y los incas...».",
        "También hay elementos que persisten hasta hoy. Se hablan lenguas como el quechua, el náhuatl y las lenguas mayas, con millones de hablantes. Palabras como tomate, aguacate, chile y coyote vienen del náhuatl; papa, cancha, cóndor y puma, del quechua. Seguimos comiendo maíz, papa, tomate y cacao. Hay textiles, música y fiestas que combinan tradiciones antiguas y actuales, y pueblos maya, nahua y quechua viven hoy.",
        "Persistencia no significa que nada cambió. Las costumbres cambian y se mezclan con otras. Un buen texto distingue entre lo que viene del pasado, lo que se transformó y lo que se creó después. También evita hablar de estos pueblos como si solo existieran en el pasado.",
    ],
    [("persistencia", "permanencia de un rasgo del pasado en el presente"), ("similitud", "rasgo que dos cosas tienen en común"), ("diferencia", "rasgo que distingue una cosa de otra"), ("náhuatl", "lengua de los aztecas, que aún se habla"), ("quechua", "lengua de los incas, que aún se habla"), ("transformación", "cambio de un rasgo con el tiempo")],
    [
        ("Reconocer una palabra", "La palabra «cóndor» se usa en español y viene del quechua. ¿Qué tipo de persistencia es?", ["Es una palabra de una lengua antigua.", "Es persistencia lingüística."], "Lingüística"),
        ("Reconocer un alimento", "Los pueblos de Mesoamérica usaban tomate y cacao. ¿Cuál de los dos usamos hoy en el chocolate?", ["El chocolate se hace con cacao.", "Es el cacao."], "El cacao"),
    ],
    [
        ("Decir que estas civilizaciones desaparecieron.", "Sus descendientes y sus lenguas persisten hoy.", "Conecta pasado y presente."),
        ("Comparar sin matices.", "Hay similitudes y diferencias que deben mencionarse a la vez.", "Usa «pero» o «en cambio»."),
    ],
    [
        ("¿De qué lengua viene la palabra «aguacate»?", "Del náhuatl", "La explicación lo menciona entre las palabras náhuatl."),
        ("¿De qué lengua viene la palabra «papa»?", "Del quechua", "La explicación lo menciona."),
        ("¿Qué cultivos seguimos comiendo hoy según la clase?", "Maíz, papa, tomate y cacao", "Son los cultivos de la explicación."),
    ],
    [
        ("¿Qué significa «persistencia»?", "Que un rasgo del pasado permanece en el presente", "Es la definición del vocabulario."),
        ("Nombra dos similitudes de las tres civilizaciones.", "Dos de estas: agricultura, calendarios, observación del cielo, arquitectura, religiones ligadas a la naturaleza", "Son las similitudes de la clase."),
        ("Nombra una diferencia clara entre los incas y los mayas.", "Escribían con glifos los mayas y usaban quipus los incas, o cultivaban maíz y papa", "Son diferencias de la clase."),
    ],
    [
        ("Un texto de ejemplo dice: «Las tres usaron calendarios y observaron el cielo; pero los mayas escribían con glifos y los incas usaban quipus». ¿Qué similitud y qué diferencia contiene?", "Similitud: calendarios y observación del cielo; diferencia: sistema de registro", "El texto usa «pero» para marcar la diferencia."),
        ("Una comunidad quechua de hoy mantiene su lengua y celebra fiestas andinas con elementos nuevos. ¿Qué dos conceptos de la clase muestra?", "Persistencia y transformación", "Conserva y cambia."),
        ("Un texto dice: «Los mayas ya no existen». ¿Qué dato de la clase lo corrige?", "Pueblos maya viven hoy y hablan lenguas mayas", "La clase indica que hay pueblos maya actuales."),
    ],
    [
        ("Luis escribe: «Mayas, aztecas e incas eran idénticos». ¿Qué le falta a su comparación?", "Las diferencias, como la escritura, el cultivo base o la forma de gobierno", "Una comparación justa nombra semejanzas y diferencias."),
        ("¿Por qué hablar de «persistencia» no es lo mismo que decir «nada cambió»?", "Porque lo que persiste también se transforma y se mezcla con otras tradiciones", "Las costumbres cambian."),
    ],
    [
        ("Ordena las partes de un buen texto comparativo: A) diferencias, B) similitudes, C) persistencias actuales.", "B, A, C", "Primero lo común, luego lo distinto y al final lo que persiste."),
        ("Un estudiante escribe: «El tomate es del náhuatl, la papa del quechua y el aguacate del náhuatl». ¿Cuántas palabras de cada lengua cita?", "Dos del náhuatl y una del quechua", "Tomate y aguacate son náhuatl; papa es quechua."),
    ],
    [("Un cartel de ejemplo dice: «Maya, azteca e inca: tres civilizaciones que comparten maíz, calendarios y templos, y que hoy viven en sus descendientes». ¿Qué falta para respetar las diferencias?", "Mencionar qué diferencia a cada una", "El cartel solo nombra similitudes.")],
    [("En la unidad de culturas americanas, ¿qué es la persistencia?", "La permanencia de un rasgo del pasado en el presente", "Es la definición del vocabulario."), ("Nombra una lengua indígena de la clase que hablan millones de personas hoy.", "El quechua, el náhuatl o una lengua maya", "Se mencionó en la clase."), ("¿Cómo se evitan los estereotipos?", "Nombrando diferencias y reconociendo pueblos actuales", "Es la recomendación de la clase.")],
    (
        "Escribe un texto de ocho líneas titulado «Tres civilizaciones, muchas diferencias, un legado». Debe incluir: dos similitudes, tres diferencias (una por civilización), tres elementos que persisten hoy y una frase final que evite el estereotipo. Usa solo datos de la unidad.",
        "Similitudes: calendarios y agricultura. Diferencias: glifos mayas, pictogramas aztecas, quipus incas. Persisten: quechua, tomate y maíz. Estos pueblos viven hoy.",
        ["dos similitudes", "tres diferencias", "tres persistencias", "frase final sin estereotipo"],
        ["texto de ocho líneas con cuatro partes"],
        ["decir que desaparecieron", "olvidar las diferencias"],
        "Pide a una persona de tu casa que subraye las semejanzas y las diferencias de tu texto.",
    ),
    "Escribe cinco palabras de origen indígena americano que uses y su lengua de origen.",
    "Averigua qué fiestas de tu región conservan elementos indígenas.",
)
