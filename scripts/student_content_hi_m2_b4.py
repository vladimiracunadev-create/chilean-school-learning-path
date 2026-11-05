"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 14 (crisis, polarización y quiebre democrático en Chile) y OA 15 (interpretaciones historiográficas del golpe de 1973)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 14"

# ================================================================ OA 14, clase 1
F = ("Ficha 1 (hechos seguros y definiciones). "
     "Hechos: en 1964 es elegido presidente Eduardo Frei Montalva, de la Democracia Cristiana, que gobierna hasta 1970; en 1967 se aprueba una nueva ley de reforma agraria; en 1970 es elegido presidente Salvador Allende, de la Unidad Popular; el 11 de septiembre de 1973 las Fuerzas Armadas derrocan al gobierno. "
     "Actores: gobierno, partidos de oposición, sindicatos y gremios empresariales, campesinos y pobladores, Fuerzas Armadas y el gobierno de Estados Unidos. "
     "Conceptos: polarización es la separación de la sociedad en bloques opuestos que casi no dialogan; retórica de la violencia es hablar de los adversarios como enemigos a eliminar o vencer por la fuerza; reforma agraria es el reparto de grandes propiedades de tierra entre campesinos; estatización es el paso de una empresa privada al Estado; expropiación es la compra o toma de una propiedad privada por el Estado, por ley y con indemnización, para un fin público.")
build(
    OA, 1, F,
    use="Aprenderé a situar la crisis de comienzos de los años setenta en Chile en su tiempo y entre sus actores, y a distinguir hechos de interpretaciones.",
    prior=["Sé que Chile tuvo reformas y movilización social en los años sesenta.", "Sé calcular diferencias entre años.", "Sé que una fuente es una huella del pasado."],
    explain=[
        "A comienzos de los años setenta, Chile vivió una crisis política, económica y social que terminó con el golpe de Estado del 11 de septiembre de 1973. Para entenderla hay que situarla en el tiempo, desde las reformas de los años sesenta, y reconocer a sus actores: gobierno, oposición, sindicatos, gremios, campesinos, pobladores, Fuerzas Armadas y la influencia de Estados Unidos en plena Guerra Fría.",
        "En esos años se habló de polarización, es decir, bloques opuestos que casi no dialogaban, y de retórica de la violencia, que es hablar de los adversarios como enemigos. También se disputaron la reforma agraria, las estatizaciones y las expropiaciones, que son decisiones sobre quién es dueño de la tierra y de las empresas: la expropiación es la compra o toma de una propiedad privada por el Estado, por ley y con indemnización, para un fin público. Cada actor valoraba la institucionalidad democrática, o la desvalorizaba, de manera distinta.",
        "Un hecho se puede comprobar con fecha y fuente; una interpretación es una explicación que alguien da sobre ese hecho. Un error frecuente es mirar el pasado sabiendo el final y pensar que todos lo veían venir. Quien estudia historia debe explicar sin juzgar con los ojos de hoy a cada persona de entonces.",
    ],
    vocab=[("polarización", "separación de la sociedad en bloques opuestos que casi no dialogan"), ("retórica de la violencia", "forma de hablar que presenta a los adversarios como enemigos a vencer por la fuerza"), ("reforma agraria", "reparto de grandes propiedades de tierra entre campesinos"), ("estatización", "paso de una empresa privada a manos del Estado"), ("institucionalidad democrática", "reglas e instituciones que organizan el poder, como la Constitución y el Congreso"), ("expropiación", "compra o toma de una propiedad privada por el Estado, por ley y con indemnización, para un fin público")],
    worked=[
        ("Calcular un período", "Según la ficha, Frei fue elegido en 1964 y Allende en 1970. ¿Cuántos años separan ambas elecciones?", ["Tomo los dos años de la ficha.", "Resto: 1970 − 1964 = 6."], "6 años"),
        ("Distinguir hecho e interpretación", "«En 1967 se aprobó una ley de reforma agraria». ¿Es un hecho o una interpretación?", ["Tiene fecha y se puede comprobar en una ley.", "No agrega una explicación sobre sus causas ni sus efectos."], "Es un hecho"),
    ],
    mistakes=[("Decir que en 1970 ya era seguro que habría un golpe en 1973.", "Se mira el pasado sabiendo el final y se olvida que las personas de entonces no lo sabían.", "Explica qué opciones había en cada momento sin dar por inevitable el desenlace."),
              ("Explicar la crisis con un solo actor como único responsable.", "Se ignora que hubo varios actores con decisiones propias.", "Nombra a los actores y di qué hizo cada uno.")],
    T=[
        ("{F} ¿En qué año fue elegido presidente Salvador Allende?", "1970", "La ficha lo indica."),
        ("{F} ¿Qué ocurrió el 11 de septiembre de 1973 según la ficha?", "Las Fuerzas Armadas derrocaron al gobierno", "Es el hecho que cierra el período."),
        ("{F} ¿De qué coalición era Salvador Allende?", "De la Unidad Popular", "La ficha lo indica."),
        ("{F} Un compañero dice que la ley de reforma agraria de 1967 fue obra del gobierno de Allende. ¿Qué corrección haces? A) Se aprobó en 1967, durante el gobierno de Frei, antes de que Allende fuera elegido B) Tiene razón, porque Allende impulsó la reforma agraria", "A) Se aprobó en 1967, durante el gobierno de Frei, antes de que Allende fuera elegido", "Frei gobernó de 1964 a 1970 y Allende fue elegido en 1970."),
        ("{F} El Estado compra por ley un terreno privado, paga a su dueño y lo usa para un fin público. ¿Cómo se llama el proceso? A) Expropiación B) Privatización", "A) Expropiación", "Es la compra o toma de una propiedad privada por el Estado, por ley y con indemnización."),
        ("{F} ¿Cuál de estas situaciones describe polarización? A) Dos bloques cada vez más alejados que casi no dialogan B) Todos los partidos acuerdan una ley", "A) Dos bloques cada vez más alejados que casi no dialogan", "La definición de la ficha habla de bloques opuestos sin diálogo."),
        ("{F} Un dirigente dice sobre sus rivales: «Hay que aplastarlos». ¿Qué rasgo muestra? A) Retórica de la violencia B) Reforma agraria", "A) Retórica de la violencia", "Presenta a los adversarios como enemigos a vencer por la fuerza."),
        ("{F} Un grupo de familias campesinas recibe tierras de un gran predio. ¿Qué proceso ocurre? A) Reforma agraria B) Estatización", "A) Reforma agraria", "Es el reparto de grandes propiedades de tierra entre campesinos."),
        ("{F} Un banco privado pasa a ser propiedad del Estado. ¿Cómo se llama el proceso? A) Estatización B) Privatización", "A) Estatización", "La ficha define estatización como paso al Estado; privatizar es lo contrario."),
        ("{F} ¿Por qué no se puede explicar la crisis con un solo actor?", "Porque participaron varios actores con decisiones propias", "La ficha enumera gobierno, oposición, gremios, campesinos, Fuerzas Armadas y Estados Unidos."),
        ("{F} Un compañero afirma: «En 1970 todos sabían que habría golpe en 1973». ¿Qué problema tiene? A) Mira el pasado sabiendo el final B) Usa un año equivocado", "A) Mira el pasado sabiendo el final", "Las personas de 1970 no conocían el desenlace de 1973."),
        ("{F} ¿Cuál es una interpretación y no un hecho? A) La reforma agraria llevó inevitablemente al golpe B) En 1967 se aprobó una ley de reforma agraria", "A) La reforma agraria llevó inevitablemente al golpe", "Es una explicación discutible; la otra frase se comprueba con una ley."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Qué factores internos y externos se combinaron entre 1970 y 1973 y cómo los vivieron los distintos actores? B) ¿Quién tuvo toda la culpa?", "A) ¿Qué factores internos y externos se combinaron entre 1970 y 1973 y cómo los vivieron los distintos actores?", "Se puede responder con evidencias; la B parte de una conclusión."),
    ],
    ctx=("Un afiche escolar dice: «Chile cayó en crisis solo por las malas ideas de un grupo». ¿Qué problema tiene? A) Reduce un proceso con muchos actores a un solo culpable B) Es demasiado corto", "A) Reduce un proceso con muchos actores a un solo culpable", "La ficha muestra actores internos y externos con distintos intereses."),
    sc=[("En Historia, ¿qué es la polarización?", "La separación de la sociedad en bloques opuestos que casi no dialogan", "Así se define en la clase."),
        ("En Historia, ¿qué es la reforma agraria?", "El reparto de grandes propiedades de tierra entre campesinos", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una estatización?", "El paso de una empresa privada a manos del Estado", "Así se define en el vocabulario.")],
    op=("Dibuja una línea de tiempo de 1964 a 1973. Marca la elección de Frei (1964), la ley de reforma agraria (1967), la elección de Allende (1970) y el golpe (1973). Debajo escribe una frase con un hecho y otra con una interpretación sobre este período, y marca cuál es cuál. {F}",
        "Frase hecho: «En 1970 fue elegido Allende». Interpretación: «La polarización hizo imposible el diálogo». Marca cada una.",
        ["ubica los cuatro años en orden", "escribe un hecho comprobable", "escribe una interpretación y la marca como tal"], ["línea de tiempo", "dos frases marcadas"], ["usar una interpretación como si fuera un hecho", "dar por seguro el desenlace desde 1964"],
        "Pide que explique por qué el hecho se puede comprobar y la interpretación se debe argumentar."),
    reinforce="Explica a una persona de tu casa qué significa polarización y da un ejemplo cotidiano de bloques que no dialogan.",
    extend="Anota un cambio que haya vivido tu comunidad en el que hubo personas a favor y en contra, y di qué argumentos daba cada una.",
)

# ================================================================ OA 14, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente 1, discurso de ejemplo de un dirigente de gobierno, 1972, ante una concentración: «Avanzaremos junto al pueblo; quienes se oponen quieren frenar los cambios y defender sus privilegios.» "
     "Fuente 2, editorial de ejemplo de un diario de oposición, 1972: «El gobierno desconoce la ley cuando le conviene y la propiedad ya no está segura.» "
     "Fuente 3, carta de ejemplo de un campesino a su hermano, 1971: «Por fin la hacienda donde trabajo pasó a manos de los trabajadores, pero faltan semillas y nadie sabe cuándo llegarán.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes de la crisis de los años setenta preguntando quién las produjo, cuándo, para qué y qué no dicen.",
    prior=["Sé qué es una fuente y distingo hecho de opinión.", "Conozco los actores de la crisis de 1970-1973.", "Sé calcular mitades."],
    explain=[
        "Interrogar una fuente es hacerle preguntas antes de creerle. La procedencia es el conjunto de datos sobre quién la produjo, cuándo, dónde y con qué propósito. Un discurso político busca convencer; un editorial expresa la línea de un diario; una carta personal cuenta una experiencia concreta. Cada una sirve para algo distinto.",
        "En los años de crisis, la retórica de la violencia y las posiciones opuestas hacían que los textos fueran muy distintos. Por eso conviene separar lo que la fuente afirma como hecho de lo que es un juicio del autor, como «defienden sus privilegios». Un juicio revela la perspectiva del autor, pero no prueba por sí solo lo que dice.",
        "Ninguna fuente basta. Una carta cuenta lo que vio una persona en un lugar, no el país entero. Para sacar una conclusión proporcional a la evidencia hay que comparar fuentes de autores distintos y decir qué límites tiene cada una.",
    ],
    vocab=[("procedencia", "datos sobre quién produjo una fuente, cuándo, dónde y para qué"), ("editorial", "texto en que un diario expresa su posición sobre un tema"), ("juicio", "opinión del autor que no se puede comprobar por sí sola"), ("perspectiva", "punto de vista desde el que alguien mira un hecho"), ("conclusión proporcional", "conclusión que no afirma más de lo que la evidencia permite")],
    worked=[
        ("Reconocer la procedencia", "¿Quién produjo una carta que cuenta que «la hacienda pasó a manos de los trabajadores» y con qué propósito probable?", ["Una carta personal la escribe alguien que cuenta lo que vive.", "Su propósito es informar a un familiar, no convencer a un público."], "Un campesino; contar su experiencia a un familiar"),
        ("Separar hecho y juicio", "En «el gobierno desconoce la ley cuando le conviene», ¿qué parte es juicio?", ["Un hecho se puede comprobar con una ley o una fecha.", "«Cuando le conviene» atribuye una intención que no se comprueba sin más pruebas."], "«Cuando le conviene» es un juicio del autor"),
    ],
    mistakes=[("Creer que una fuente dice la verdad porque fue escrita en la época.", "Estar en la época no elimina la perspectiva ni el propósito del autor.", "Pregunta quién escribe, para quién y qué intención tiene."),
              ("Generalizar a todo el país lo que cuenta una carta.", "Una carta muestra un caso y un lugar.", "Dilo con prudencia: «en este caso» y busca más fuentes.")],
    T=[
        ("{F} ¿Qué tipo de fuente es la Fuente 3?", "Una carta personal", "Es un mensaje privado de un campesino a su hermano."),
        ("{F} ¿De qué año es el editorial de la Fuente 2?", "1972", "La ficha lo fecha en 1972."),
        ("{F} ¿Quién produjo la Fuente 1?", "Un dirigente de gobierno", "La ficha lo indica."),
        ("{F} En Historia, ¿qué significa «procedencia» de una fuente? A) Quién la produjo, cuándo, dónde y para qué B) Si me gusta o no lo que dice", "A) Quién la produjo, cuándo, dónde y para qué", "Es la definición de la clase."),
        ("{F} ¿Qué propósito probable tiene la Fuente 2? A) Convencer a sus lectores de que el gobierno no respeta la ley B) Informar con neutralidad sobre una ley sin tomar posición", "A) Convencer a sus lectores de que el gobierno no respeta la ley", "Un editorial opina y busca influir."),
        ("=", "En una concentración de ejemplo asisten 4.000 personas, y un diario opositor informa que fue la mitad. ¿Cuántas personas informa el diario?", "4000/2", "La mitad se calcula dividiendo por 2.", " personas"),
        ("{F} ¿Qué limita el uso de la Fuente 1 como prueba de que los opositores defendían privilegios? A) Es un discurso para una concentración y atribuye una intención sin presentar pruebas B) Está fechado en 1972", "A) Es un discurso para una concentración y atribuye una intención sin presentar pruebas", "Un discurso busca convencer y «defender sus privilegios» es un juicio; la fecha no es un límite."),
        ("{F} ¿Qué fuente muestra mejor la experiencia cotidiana de un campesino? A) La Fuente 3 B) La Fuente 1", "A) La Fuente 3", "Es una carta escrita por un campesino sobre su trabajo."),
        ("{F} En la Fuente 1, la frase «defender sus privilegios» es: A) Un juicio del autor B) Un hecho comprobado", "A) Un juicio del autor", "Atribuye una intención a los opositores sin pruebas en el texto."),
        ("{F} ¿Por qué las Fuentes 1 y 2 hablan distinto de un mismo año?", "Porque sus autores tienen posiciones e intereses distintos", "Cada uno escribe desde una perspectiva diferente."),
        ("{F} ¿Qué límite tiene la Fuente 3 como evidencia? A) Habla de una sola hacienda, no de todo el país B) Es falsa por ser una carta privada", "A) Habla de una sola hacienda, no de todo el país", "Una carta muestra un caso y no se puede generalizar sin otras fuentes."),
        ("{F} ¿Qué conclusión es proporcional a las tres fuentes? A) En 1971-1972 había visiones opuestas sobre la ley, la propiedad y las reformas B) La mayoría del país apoyaba al gobierno", "A) En 1971-1972 había visiones opuestas sobre la ley, la propiedad y las reformas", "La otra afirma más de lo que tres fuentes permiten."),
        ("{F} ¿Qué documento ayudaría mejor a comprobar lo que cuenta la Fuente 3? A) Un registro de la época sobre la entrega de semillas a esa hacienda B) Una opinión actual sin fecha ni autor", "A) Un registro de la época sobre la entrega de semillas a esa hacienda", "Un documento fechado y atribuido permite contrastar el dato."),
    ],
    ctx=("Una compañera cita solo el editorial de la Fuente 2 para afirmar: «Todo el país pensaba que la propiedad estaba en peligro». ¿Qué corrección haces? A) Un editorial expresa la posición de un diario, no la de todo el país B) Hay que cambiar el año del editorial", "A) Un editorial expresa la posición de un diario, no la de todo el país", "Generaliza desde una sola fuente con perspectiva propia."),
    sc=[("En Historia, ¿qué es un juicio en una fuente?", "Una opinión del autor que no se puede comprobar por sí sola", "Así se distingue de un hecho."),
        ("¿Cuál es una pregunta de procedencia? A) ¿Quién la produjo y para qué? B) ¿Estoy de acuerdo con su autor?", "A) ¿Quién la produjo y para qué?", "Son las preguntas que define la clase; estar de acuerdo no es una pregunta de procedencia."),
        ("=", "Un diario de ejemplo dice que a un acto asistieron 3.000 personas y otro dice que fue el doble. ¿Cuántas dice el segundo diario?", "3000*2", "El doble se calcula multiplicando por 2.", " personas")],
    op=("Elige dos de las tres fuentes de la ficha y completa una tabla con: autor, año, propósito probable, un hecho que afirma, un juicio que contiene y un límite. Termina con una conclusión de una frase que no afirme más de lo que ambas fuentes permiten. {F}",
        "Fuentes 1 y 3: autores distintos; propósito de convencer y de contar; hecho: la hacienda pasó a los trabajadores; juicio: «defender sus privilegios»; límite: un caso. Conclusión: en 1971-1972 había experiencias y discursos diferentes sobre las reformas.",
        ["completa los seis datos de cada fuente", "distingue hecho y juicio", "su conclusión es proporcional"], ["tabla", "conclusión de una frase"], ["tomar el juicio como hecho", "generalizar a todo el país"],
        "Pide que diga qué otra fuente buscaría para comprobar el hecho de la carta."),
    reinforce="Elige un mensaje que hayas recibido hoy y di quién lo produjo, para qué y qué parte es opinión.",
    extend="Compara cómo dos personas de tu casa cuentan un mismo evento reciente y anota en qué difieren.",
)

# ================================================================ OA 14, clase 3
F = ("Ficha 3 (perspectivas y escalas; textos y datos de ejemplo escritos para este cuaderno). "
     "Perspectivas: el gobierno de la Unidad Popular decía que había que acelerar las reformas para mejorar la vida de trabajadores y campesinos; la oposición decía que defendía la ley, la propiedad y las libertades; "
     "campesinos y pobladores pedían tierra y vivienda; empresarios y gremios temían las expropiaciones y organizaban paros. "
     "Escalas: local (un predio o una población), nacional (el Congreso, el gobierno y los partidos) e internacional (la Guerra Fría; documentos desclasificados del gobierno de Estados Unidos muestran que buscó impedir que Allende asumiera en 1970 y luego debilitar a su gobierno). "
     "Datos de ejemplo: en una comuna se encuestó a 200 personas y 120 dijeron apoyar la reforma agraria; un predio de 900 hectáreas se divide en 30 parcelas iguales.")
build(
    OA, 3, F,
    use="Aprenderé a comparar las perspectivas de distintos actores sobre la crisis y a distinguir las escalas local, nacional e internacional.",
    prior=["Sé interrogar fuentes por su procedencia.", "Conozco los actores de 1970-1973.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Comparar perspectivas es poner lado a lado lo que distintos actores pensaban de un mismo hecho y por qué. El gobierno, la oposición, los campesinos y los empresarios tenían intereses y temores diferentes sobre la reforma agraria, las estatizaciones y las expropiaciones. Ninguna perspectiva basta por sí sola; cada una debe sostenerse con evidencia.",
        "La escala es el nivel desde el que se mira un hecho. En la escala local se observa lo que pasó en un predio o una población; en la nacional, las decisiones del Congreso, los partidos y el gobierno; en la internacional, la Guerra Fría y la intervención extranjera. Un mismo suceso puede verse distinto en cada escala.",
        "Un error común es generalizar un dato de una escala a otra. Si en una comuna 120 de 200 personas apoyan una reforma, eso es un 60 % en esa comuna, no en todo Chile. Para hablar del país hay que usar datos de escala nacional.",
    ],
    vocab=[("perspectiva", "punto de vista de un actor según sus intereses y su experiencia"), ("escala", "nivel desde el que se observa un hecho: local, nacional o internacional"), ("intervención extranjera", "acción de un gobierno de otro país en asuntos internos de un Estado"), ("desclasificado", "documento secreto que se hizo público"), ("generalizar", "extender a un conjunto lo observado en una parte")],
    worked=[
        ("Reconocer una perspectiva", "Un texto dice: «Defendemos la ley y la propiedad». ¿Qué actor lo diría?", ["La ficha asocia ese discurso con la oposición.", "Los campesinos pedían tierra y el gobierno aceleraba reformas."], "La oposición"),
        ("Cuidar la escala de un dato", "En una comuna, 90 de 150 personas encuestadas apoyan una reforma. ¿Qué porcentaje es y a qué escala sirve?", ["90 dividido en 150 es 0,6, o sea 60 %.", "Es un dato de una sola comuna: escala local."], "60 %; sirve solo para esa comuna"),
    ],
    mistakes=[("Creer que una perspectiva es verdadera por ser la de un actor importante.", "Se confunde la posición de un actor con evidencia de lo ocurrido.", "Pide la evidencia que sostiene lo que dice cada actor."),
              ("Usar el dato de una comuna para hablar de todo el país.", "Se salta de una escala a otra sin datos.", "Di a qué escala sirve cada dato.")],
    T=[
        ("{F} ¿Qué pedían campesinos y pobladores?", "Tierra y vivienda", "La ficha lo indica."),
        ("{F} ¿Qué temían los empresarios y los gremios?", "Las expropiaciones", "La ficha describe ese temor."),
        ("{F} ¿Qué actor de la ficha decía defender la ley, la propiedad y las libertades?", "La oposición", "Así se presenta su perspectiva."),
        ("=", "{F} ¿Qué porcentaje de las 200 personas encuestadas en la comuna apoya la reforma agraria?", "120/200*100", "Se divide lo que apoya por el total y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántas hectáreas tiene cada parcela del predio?", "900/30", "Se reparte el total en partes iguales.", " hectáreas"),
        ("{F} Una discusión en el Congreso sobre una ley de expropiaciones, ¿en qué escala se ubica? A) Nacional B) Local", "A) Nacional", "El Congreso es una institución del país entero."),
        ("{F} Un grupo de familias de una población pide terrenos para viviendas. ¿Qué escala observa? A) Local B) Internacional", "A) Local", "Se trata de un lugar y un grupo concretos."),
        ("{F} La Guerra Fría y la actuación del gobierno de Estados Unidos corresponden a la escala: A) Internacional B) Nacional", "A) Internacional", "Involucra relaciones entre países."),
        ("{F} ¿Por qué un campesino y un dueño de fundo pueden valorar distinto la misma reforma agraria?", "Porque tienen intereses y experiencias distintas", "Una perspectiva depende de lo que cada actor gana o teme perder."),
        ("{F} Un compañero dice: «Como son perspectivas, todas valen igual como explicación». ¿Qué corrección haces? A) Cada perspectiva debe sostenerse con evidencia B) Es correcto, ninguna necesita pruebas", "A) Cada perspectiva debe sostenerse con evidencia", "Entender una postura no la hace verdadera sin pruebas."),
        ("{F} ¿Por qué no se puede afirmar con el dato de la comuna que el 60 % de Chile apoyaba la reforma? A) Es un dato de una comuna y no del país B) Porque una encuesta de 200 personas siempre es falsa", "A) Es un dato de una comuna y no del país", "Cambia de escala sin evidencia."),
        ("{F} ¿Qué afirmación reconoce bien las escalas? A) Un conflicto por un predio podía conectarse con un debate nacional y con la Guerra Fría B) Lo local nunca tiene relación con lo internacional", "A) Un conflicto por un predio podía conectarse con un debate nacional y con la Guerra Fría", "Las escalas se relacionan entre sí."),
        ("{F} ¿Cuál criterio sirve para comparar dos perspectivas? A) Qué quiere cada actor, qué teme y qué evidencia usa B) Cuál habla más fuerte", "A) Qué quiere cada actor, qué teme y qué evidencia usa", "Son criterios que se pueden analizar con fuentes."),
    ],
    ctx=("Para una exposición sobre un fundo de la zona central, una estudiante usa el discurso de un ministro, una carta de un campesino y un informe desclasificado extranjero. ¿Qué logra con esa mezcla? A) Mirar el caso desde tres escalas B) Repetir tres veces la misma perspectiva", "A) Mirar el caso desde tres escalas", "El discurso es nacional, la carta local y el informe internacional."),
    sc=[("En Historia, ¿qué es una escala en historia?", "El nivel desde el que se observa un hecho: local, nacional o internacional", "Así se define en la clase."),
        ("Nombra las tres escalas de la clase.", "Local, nacional e internacional", "Son las tres que presenta la ficha."),
        ("=", "En un predio de ejemplo de 600 hectáreas se hacen 20 parcelas iguales. ¿Cuántas hectáreas tiene cada una?", "600/20", "Se reparte el total en partes iguales.", " hectáreas")],
    op=("Completa una tabla con cuatro actores (gobierno, oposición, campesinos y pobladores, empresarios y gremios): qué querían, qué temían y a qué escala actuaban. Después escribe dos frases: una que compare dos perspectivas y otra que explique por qué el dato de la comuna no sirve para todo el país. {F}",
        "Gobierno: reformas, mejorar vida de trabajadores, nacional. Oposición: ley y propiedad, nacional. Campesinos: tierra, local. Empresarios: temor a expropiaciones, nacional. Frase: el gobierno aceleraba reformas y la oposición defendía la propiedad. El 60 % es solo de una comuna.",
        ["completa los cuatro actores", "distingue la escala de cada uno", "explica el límite del dato local"], ["tabla completa", "dos frases"], ["mezclar escalas", "tratar una perspectiva como hecho"],
        "Pide que diga qué evidencia buscaría para comprobar la perspectiva de la oposición."),
    reinforce="Explica con tus palabras por qué un dato de una comuna no sirve para describir a todo el país.",
    extend="Anota un tema de tu barrio y di quién tendría perspectivas distintas sobre él.",
)

# ================================================================ OA 14, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; datos de ejemplo cuando se indica). "
     "Procesos de largo plazo: desde los años sesenta crecían las demandas de tierra, vivienda y participación; las reformas de Frei y de Allende buscaron responder a ellas. "
     "Procesos del período 1970-1973: polarización creciente; retórica de la violencia en distintos sectores; conflictos por la reforma agraria, las estatizaciones y las expropiaciones; "
     "crisis económica, con alza sostenida de precios (inflación) y escasez de productos; paros y movilizaciones; intervención extranjera en el contexto de la Guerra Fría; y creciente papel político de las Fuerzas Armadas. "
     "Hechos: en octubre de 1972 hubo un paro de transportistas y comerciantes; en noviembre de 1972 el presidente incorporó a jefes de las Fuerzas Armadas al gabinete; el 29 de junio de 1973 un regimiento blindado se sublevó en Santiago sin éxito; en 1972 y en 1973 la inflación anual superó el 100 %. "
     "Continuidades entre 1964 y 1973: la Constitución de 1925 estuvo vigente y las demandas sociales de los años sesenta no habían desaparecido. "
     "Dato de ejemplo: una canasta de alimentos que costaba 100 pesos de ejemplo pasó a costar 160 pesos de ejemplo en un año.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar causas de largo plazo y de corto plazo de la crisis con sus cambios y continuidades, evitando explicar con una sola causa.",
    prior=["Sé que un hecho tiene varias causas.", "Sé comparar perspectivas y escalas.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Un quiebre democrático no se explica con una causa. Hay causas de largo plazo, como las demandas sociales de los años sesenta, y causas de corto plazo, como la polarización, la crisis económica y la movilización social de 1970 a 1973. A esto se sumó la intervención extranjera durante la Guerra Fría y el papel político de las Fuerzas Armadas: en noviembre de 1972 jefes militares ingresaron al gabinete, y en octubre de ese año un paro de transportistas y comerciantes afectó el abastecimiento.",
        "La inflación es el alza sostenida de los precios; cuando es muy alta se habla de hiperinflación, y en 1972 y 1973 la inflación anual superó el 100 %. Si una canasta pasa de 100 a 160 pesos de ejemplo, subió un 60 %. La escasez de productos y la inflación afectaban la vida cotidiana y aumentaban el descontento. Con la retórica de la violencia, cada sector veía al otro como una amenaza y valoraba menos la institucionalidad.",
        "Hubo cambios: de una democracia con alternancia a un gobierno de las Fuerzas Armadas sin elecciones. Hubo continuidades: la Constitución de 1925 estuvo vigente durante todo el período anterior al golpe y las demandas sociales seguían pendientes. Para explicar con prudencia se usan verbos como «contribuyó a», no «causó por sí sola».",
    ],
    vocab=[("causa de largo plazo", "proceso que se acumula durante años antes de una crisis"), ("causa de corto plazo", "hecho cercano en el tiempo que empuja una crisis"), ("inflación", "alza sostenida y general de los precios"), ("escasez", "falta de productos en el mercado"), ("continuidad", "algo que se mantiene a pesar de los cambios")],
    worked=[
        ("Calcular un alza", "Un producto de ejemplo cuesta 200 pesos de ejemplo y pasa a 250. ¿Qué porcentaje subió?", ["Resto: 250 − 200 = 50.", "Divido 50 en 200 y multiplico por 100: 25 %."], "25 %"),
        ("Clasificar una causa", "«Las demandas de tierra crecen desde los años sesenta». ¿Largo o corto plazo?", ["Se acumulan durante años.", "No es un hecho de un momento puntual."], "Causa de largo plazo"),
    ],
    mistakes=[("Decir que la crisis económica causó por sí sola el quiebre democrático.", "Se deja fuera la polarización, la intervención extranjera y las decisiones de los actores.", "Usa «contribuyó a» y suma otras causas."),
              ("Pensar que todo cambió en 1973.", "No se ven las continuidades, como las demandas sociales.", "Pregunta qué se mantuvo y qué cambió.")],
    T=[
        ("{F} ¿Qué Constitución estuvo vigente durante el período 1964-1973?", "La de 1925", "La ficha lo indica."),
        ("{F} En Historia, ¿qué es la inflación?", "El alza sostenida y general de los precios", "Así se define en la clase."),
        ("{F} ¿Qué problema de los productos afectaba la vida cotidiana según la ficha?", "La escasez", "La ficha la cuenta junto a la inflación."),
        ("=", "{F} ¿Qué porcentaje subió la canasta de ejemplo?", "(160-100)/100*100", "Se calcula el aumento sobre el precio inicial.", " %"),
        ("{F} ¿Qué hecho de noviembre de 1972 muestra el papel político de las Fuerzas Armadas? A) Jefes de las Fuerzas Armadas se incorporaron al gabinete B) Las Fuerzas Armadas redactaron una nueva Constitución", "A) Jefes de las Fuerzas Armadas se incorporaron al gabinete", "La ficha lo menciona; la Constitución de 1925 seguía vigente."),
        ("{F} La demanda de vivienda de los pobladores, ¿qué tipo de causa es? A) De largo plazo B) De corto plazo", "A) De largo plazo", "Se acumula desde los años sesenta."),
        ("{F} «Las demandas sociales de los años sesenta seguían pendientes en 1973». ¿Qué es? A) Una continuidad B) Un cambio", "A) Una continuidad", "Se mantiene a lo largo del período."),
        ("{F} Pasar de un gobierno elegido a un gobierno de las Fuerzas Armadas sin elecciones es: A) Un cambio B) Una continuidad", "A) Un cambio", "Modifica la forma de ejercer el poder."),
        ("{F} ¿Por qué decir «la crisis económica causó el golpe» es insuficiente? A) Porque hubo otras causas políticas, sociales e internacionales B) Porque la economía no importa", "A) Porque hubo otras causas políticas, sociales e internacionales", "La ficha muestra causas múltiples."),
        ("{F} ¿Qué frase es más prudente? A) La retórica de la violencia pudo contribuir a desvalorizar la institucionalidad B) La retórica de la violencia fue la única causa del quiebre", "A) La retórica de la violencia pudo contribuir a desvalorizar la institucionalidad", "Evita afirmar una causa única sin pruebas."),
        ("{F} Alguien dice: «Solo la intervención extranjera explica todo». ¿Qué corrección haces? A) Hubo también factores internos como la polarización y la crisis económica B) Es correcta porque era la Guerra Fría", "A) Hubo también factores internos como la polarización y la crisis económica", "La ficha incluye causas internas y externas."),
        ("{F} ¿Cuál es la mejor síntesis? A) Causas de largo plazo y de corto plazo, internas y externas, produjeron cambios en el régimen político y mantuvieron demandas sociales B) Todo ocurrió por una decisión en 1973", "A) Causas de largo plazo y de corto plazo, internas y externas, produjeron cambios en el régimen político y mantuvieron demandas sociales", "Reúne causas, cambios y continuidades."),
        ("{F} ¿Qué evidencia permitiría probar que la escasez afectaba la vida cotidiana? A) Relatos y registros de la época sobre filas y falta de productos B) Una frase de un discurso sin fecha", "A) Relatos y registros de la época sobre filas y falta de productos", "Se necesita evidencia fechada y atribuida."),
    ],
    ctx=("Un cartel de una feria escolar dice: «El golpe de 1973 solo se explica por el precio de los alimentos». ¿Qué problema tiene? A) Reduce el proceso a una causa y no considera la polarización ni la intervención extranjera B) Usa demasiadas palabras", "A) Reduce el proceso a una causa y no considera la polarización ni la intervención extranjera", "La ficha muestra varias causas."),
    sc=[("En Historia, ¿qué es una continuidad?", "Algo que se mantiene a pesar de los cambios", "Así se define en el vocabulario."),
        ("¿Qué verbo es más prudente: «causó» o «contribuyó a»?", "Contribuyó a", "Evita afirmar una causa única."),
        ("=", "Si una inflación anual de 100 % duplica los precios, ¿cuánto costaría al final del año un producto de ejemplo que cuesta 300 pesos de ejemplo?", "300+300*100/100", "Se suma al precio inicial el 100 % de aumento.", " pesos de ejemplo")],
    op=("Dibuja un esquema con «quiebre democrático de 1973» al centro. A la izquierda escribe dos causas de largo plazo, arriba dos de corto plazo y a la derecha un cambio y una continuidad. Debajo escribe una frase con «contribuyó a…». {F}",
        "Largo plazo: demandas de tierra y vivienda; reformas anteriores. Corto plazo: polarización; crisis económica. Cambio: gobierno de las Fuerzas Armadas sin elecciones. Continuidad: demandas sociales pendientes. Frase: la escasez contribuyó a aumentar el descontento.",
        ["distingue largo y corto plazo", "incluye un cambio y una continuidad", "evita causas únicas"], ["esquema", "frase con «contribuyó a…»"], ["poner una sola causa", "no dar continuidades"],
        "Pide que explique por qué una causa externa no excluye las internas."),
    reinforce="Explica a alguien de tu casa la diferencia entre una causa de largo plazo y una de corto plazo.",
    extend="Piensa en un conflicto reciente de tu entorno y anota una causa antigua y una causa cercana.",
)

# ================================================================ OA 14, clase 5
F = ("Ficha 5 (pregunta y evidencias de ejemplo). "
     "Pregunta: ¿qué factores contribuyeron a la crisis de 1970-1973 y cómo se relacionan entre sí? "
     "Evidencia 1, discurso de ejemplo, 1972: «Con los adversarios no hay diálogo posible; se vence o se pierde.» "
     "Evidencia 2, editorial de ejemplo, 1972: «Las instituciones ya no sirven si cada sector las usa solo cuando le conviene.» "
     "Evidencia 3, tabla de ejemplo: canasta de alimentos, año 1: 100 pesos de ejemplo; año 2: 160 pesos de ejemplo. "
     "Evidencia 4, informe desclasificado de ejemplo del gobierno de otro país: «Se buscó debilitar al gobierno de Chile apoyando a sus opositores.» "
     "Modelo de interpretación: tesis (qué afirmo), argumentos, evidencia que los sostiene y un límite (qué no puedo afirmar).")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada de la crisis de 1970-1973: una tesis con argumentos, evidencia y un límite.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir causas de largo y corto plazo.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Una interpretación documentada es una explicación propia que se apoya en fuentes. Tiene una tesis, que es lo que afirmo; argumentos, que son las razones; evidencia, que son los datos y textos que las sostienen; y un límite, que dice qué no puedo asegurar con lo que tengo.",
        "Para construirla se parte de una pregunta. Luego se eligen evidencias de distinto tipo: un discurso, un editorial, una tabla de precios y un informe desclasificado. Cada una aporta algo y tiene un límite. Un discurso muestra la retórica de la violencia, pero no prueba cuántos la compartían.",
        "Una buena tesis no culpa a un solo actor ni asegura más de lo que muestran las fuentes. Puede decir, por ejemplo, que la polarización, la crisis económica y la intervención extranjera contribuyeron a debilitar la institucionalidad democrática. Cada parte debe tener una evidencia que la sostenga.",
    ],
    vocab=[("tesis", "afirmación central que una persona defiende con argumentos"), ("argumento", "razón que sostiene una tesis"), ("evidencia", "dato o texto de una fuente que sostiene un argumento"), ("límite", "aquello que la evidencia disponible no permite afirmar"), ("interpretación documentada", "explicación propia apoyada en fuentes")],
    worked=[
        ("Elegir evidencia", "Quiero argumentar que la retórica de la violencia debilitó el diálogo. ¿Qué tipo de evidencia me sirve?", ["Necesito un texto de la época que use ese lenguaje.", "Un discurso donde se dice que no hay diálogo posible lo muestra."], "Un discurso con ese lenguaje"),
        ("Reconocer un límite", "Tengo una sola carta de un campesino. ¿Qué no puedo afirmar?", ["Una carta muestra un caso.", "No prueba lo que vivió todo el campo."], "Que toda la población campesina vivió lo mismo"),
    ],
    mistakes=[("Escribir una tesis sin evidencia que la sostenga.", "Se confunde una opinión con una interpretación documentada.", "A cada argumento asócialo una evidencia citada."),
              ("Olvidar el límite.", "Se cree que explicar bien es no dudar nunca.", "Escribe qué no puedes asegurar con tus fuentes.")],
    T=[
        ("{F} En Historia, ¿qué es una tesis?", "La afirmación central que una persona defiende con argumentos", "Así se define en la clase."),
        ("{F} ¿Qué evidencia de la ficha es una tabla?", "La Evidencia 3", "Es la tabla de la canasta de alimentos."),
        ("{F} ¿Cuál es la pregunta de la ficha?", "Qué factores contribuyeron a la crisis de 1970-1973 y cómo se relacionan entre sí", "Está escrita en la ficha."),
        ("=", "{F} ¿Qué porcentaje subió la canasta de alimentos entre el año 1 y el año 2?", "(160-100)/100*100", "Se divide el aumento por el precio inicial y se multiplica por 100.", " %"),
        ("=", "{F} Si en un año 3 la canasta subiera otra vez el mismo porcentaje que entre el año 1 y el año 2, ¿cuántos pesos de ejemplo costaría?", "160+160*60/100", "Se suma al precio del año 2 el 60 % de aumento.", " pesos de ejemplo"),
        ("{F} ¿Qué evidencia sostiene mejor un argumento sobre la retórica de la violencia? A) La Evidencia 1 B) La Evidencia 3", "A) La Evidencia 1", "El discurso usa un lenguaje de vencer al adversario."),
        ("{F} ¿Qué evidencia sostiene mejor un argumento sobre la intervención extranjera? A) La Evidencia 4 B) La Evidencia 2", "A) La Evidencia 4", "El informe desclasificado habla de apoyar opositores."),
        ("{F} ¿Qué evidencia sostiene mejor un argumento sobre el costo de la vida? A) La Evidencia 3 B) La Evidencia 1", "A) La Evidencia 3", "La tabla muestra el alza de precios."),
        ("{F} ¿Por qué el discurso de la Evidencia 1 no prueba por sí solo que todo el país pensaba así?", "Porque es un texto de una persona o sector, no de toda la sociedad", "Es una sola fuente con perspectiva propia."),
        ("{F} ¿Cuál es un buen límite para esta interpretación? A) Con estas cuatro evidencias no puedo afirmar cuál factor pesó más B) Con estas evidencias lo explico todo", "A) Con estas cuatro evidencias no puedo afirmar cuál factor pesó más", "Un límite reconoce lo que las fuentes no permiten."),
        ("{F} ¿Qué tesis es mejor? A) La polarización, la crisis económica y la intervención extranjera contribuyeron a debilitar la institucionalidad democrática B) El quiebre se debió solo a la intervención extranjera", "A) La polarización, la crisis económica y la intervención extranjera contribuyeron a debilitar la institucionalidad democrática", "Reúne varios factores y cada uno tiene evidencia en la ficha."),
        ("{F} Una estudiante escribe: «La tabla prueba que el golpe fue inevitable». ¿Qué corrección haces? A) La tabla solo muestra alza de precios; no prueba inevitabilidad B) Debe usar otro año", "A) La tabla solo muestra alza de precios; no prueba inevitabilidad", "Una evidencia no permite afirmar más de lo que muestra."),
        ("{F} ¿Qué orden tiene un párrafo bien armado? A) Tesis, argumento, evidencia, límite B) Evidencia, límite, tesis sin argumento", "A) Tesis, argumento, evidencia, límite", "Es la secuencia del modelo de la ficha."),
    ],
    ctx=("Un compañero te muestra su trabajo: tiene una tesis fuerte pero ninguna fuente. ¿Qué le recomiendas? A) Agregar evidencias de distinto tipo y señalar un límite B) Escribir con más fuerza", "A) Agregar evidencias de distinto tipo y señalar un límite", "Una interpretación documentada necesita evidencia."),
    sc=[("En Historia, ¿qué es un límite en una interpretación?", "Lo que la evidencia disponible no permite afirmar", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una interpretación documentada?", "Una explicación propia apoyada en fuentes", "Así se define en la clase."),
        ("=", "Un precio de ejemplo sube de 50 a 75 pesos de ejemplo. ¿Cuántos pesos de ejemplo subió?", "75-50", "Se resta el precio inicial al final.", " pesos de ejemplo")],
    op=("Escribe un párrafo de cinco a siete líneas que responda la pregunta de la ficha. Debe tener una tesis, dos argumentos con la evidencia que los sostiene (cítala como «Evidencia 1», etc.) y un límite. No culpes a un solo actor. {F}",
        "Tesis: la polarización y la crisis económica, junto con la intervención extranjera, contribuyeron a debilitar la institucionalidad. Argumento 1: la retórica de la violencia (Evidencia 1). Argumento 2: el alza de precios (Evidencia 3). Límite: no sé cuál factor pesó más.",
        ["tiene tesis, dos argumentos y límite", "cita evidencias distintas", "no culpa a un solo actor"], ["párrafo escrito"], ["tesis sin evidencia", "olvidar el límite"],
        "Pide que cambie un verbo fuerte por uno prudente, como «contribuyó a»."),
    reinforce="Explica en voz alta tu tesis con un argumento y su evidencia.",
    extend="Elige una decisión reciente de tu curso y escribe una tesis, un argumento, su evidencia y un límite.",
)

# ================================================================ OA 14, clase 6
F = ("Ficha 6 (debate; textos de ejemplo escritos para este cuaderno). "
     "Posición A, de ejemplo: «El principal problema fue que los sectores políticos dejaron de dialogar y desvalorizaron la institucionalidad.» "
     "Posición B, de ejemplo: «El principal problema fue la intervención extranjera y la presión económica sobre el país.» "
     "Posición C, de ejemplo: «El principal problema fue que las demandas sociales superaron lo que las instituciones podían responder.» "
     "Reglas del debate: escuchar sin interrumpir, apoyar cada afirmación con evidencia, reconocer los límites y no usar insultos. "
     "Principio: ninguna crisis política justifica violar los derechos humanos de las personas.")
build(
    OA, 6, F,
    use="Aprenderé a debatir sobre la crisis de 1970-1973 y sus consecuencias con respeto, evidencia y reconocimiento de los límites de cada posición.",
    prior=["Sé construir una interpretación con tesis, argumentos y evidencia.", "Sé que hubo varias causas y actores.", "Sé escuchar posturas distintas."],
    explain=[
        "Debatir en historia no es ganar una discusión, sino examinar distintas interpretaciones con evidencia. En este tema hay posiciones que ponen el acento en el diálogo entre los partidos, en la intervención extranjera o en las demandas sociales que las instituciones no lograron responder. Cada una tiene algo de verdad y un límite.",
        "Un debate de calidad exige reglas: escuchar sin interrumpir, apoyar cada afirmación con evidencia, reconocer lo que no se sabe y no usar insultos. También exige no confundir explicar con justificar. Se puede explicar por qué ocurrió una crisis sin aceptar que lo que vino después estuviera bien.",
        "Una consecuencia del quiebre fue la suspensión de la democracia representativa y, como verás en otra clase, graves violaciones a los derechos humanos. Ninguna crisis política las justifica. Si el tema te afecta emocionalmente, conversa con una persona adulta de confianza.",
    ],
    vocab=[("debate", "intercambio ordenado de argumentos con evidencia"), ("consecuencia", "efecto de un hecho en el tiempo"), ("límite de una posición", "aquello que la posición no logra explicar"), ("justificar", "presentar algo como correcto o aceptable"), ("explicar", "mostrar las causas y condiciones de un hecho sin aprobarlo")],
    worked=[
        ("Detectar un límite", "La posición «solo importó la intervención extranjera» no menciona las decisiones de los partidos chilenos. ¿Qué límite tiene?", ["Un límite es lo que no logra explicar.", "Deja fuera las causas internas."], "Ignora las causas internas"),
        ("Explicar sin justificar", "Una estudiante dice: «Entender por qué hubo polarización no significa aprobar lo que vino después». ¿Qué distingue?", ["Explicar muestra causas.", "Justificar presenta algo como aceptable."], "Distingue explicar de justificar"),
    ],
    mistakes=[("Defender una posición atacando a quienes piensan distinto.", "Se confunde ganar con argumentar.", "Responde a los argumentos con evidencia, no a las personas."),
              ("Pensar que explicar un hecho es aprobarlo.", "Se mezclan explicar y justificar.", "Di que explicas las causas y mantén el rechazo a las violaciones de derechos humanos.")],
    T=[
        ("{F} ¿Qué enfatiza la Posición A?", "El diálogo entre sectores políticos y el respeto a la institucionalidad", "Así se presenta en la ficha."),
        ("{F} ¿Qué enfatiza la Posición B?", "La intervención extranjera y la presión económica", "Así se presenta en la ficha."),
        ("{F} ¿Qué enfatiza la Posición C?", "Que las demandas sociales superaron lo que las instituciones podían responder", "Así se presenta en la ficha."),
        ("=", "En un debate de ejemplo hay 30 estudiantes y cada uno habla 2 minutos. ¿Cuántos minutos dura el debate?", "30*2", "Se multiplica el número de personas por el tiempo de cada una.", " minutos"),
        ("=", "En el mismo debate de ejemplo, 12 estudiantes eligen la Posición A, 9 la B y el resto la C. ¿Cuántos eligen la C?", "30-12-9", "Se resta del total lo que eligieron A y B.", " estudiantes"),
        ("{F} ¿Cuál es una regla del debate? A) Apoyar cada afirmación con evidencia B) Hablar más fuerte que los demás", "A) Apoyar cada afirmación con evidencia", "La ficha lo establece como regla."),
        ("{F} Una estudiante dice «Quien piense la Posición B es un tonto». ¿Qué regla rompe? A) No usar insultos B) Escuchar sin interrumpir", "A) No usar insultos", "Es una descalificación personal."),
        ("{F} ¿Qué diferencia hay entre explicar y justificar? A) Explicar muestra causas; justificar presenta algo como aceptable B) Son sinónimos", "A) Explicar muestra causas; justificar presenta algo como aceptable", "La clase los distingue."),
        ("{F} ¿Cuál es un límite de la Posición A? A) Deja poco espacio a la presión externa B) Ignora que los partidos políticos tomaron decisiones", "A) Deja poco espacio a la presión externa", "No considera el factor que enfatiza la B."),
        ("{F} ¿Cuál es un límite de la Posición B? A) Da poco peso a las decisiones de los actores chilenos B) Da demasiado peso a las decisiones de los partidos chilenos", "A) Da poco peso a las decisiones de los actores chilenos", "Todo lo explica por causas externas."),
        ("{F} ¿Qué principio sostiene la ficha sobre los derechos humanos?", "Ninguna crisis política justifica violarlos", "Está escrito en la ficha."),
        ("{F} Un compañero dice: «Si el país estaba en crisis, lo que vino después estuvo justificado». ¿Qué respondes? A) Explicar una crisis no justifica violar derechos humanos B) Tiene razón porque había crisis", "A) Explicar una crisis no justifica violar derechos humanos", "Aplica el principio de la ficha."),
        ("{F} ¿Qué cierre de un debate es mejor? A) Reconocer qué evidencia aportó cada posición y qué límites tiene B) Declarar ganador al que habló más tiempo", "A) Reconocer qué evidencia aportó cada posición y qué límites tiene", "El debate histórico examina interpretaciones, no gana por volumen."),
    ],
    ctx=("En un debate del curso, un compañero se siente atacado por su posición. ¿Qué haces? A) Volver a las reglas y responder a sus argumentos con evidencia B) Hablar más fuerte", "A) Volver a las reglas y responder a sus argumentos con evidencia", "Se debate sobre las ideas, no sobre las personas."),
    sc=[("En Historia, ¿qué significa justificar?", "Presentar algo como correcto o aceptable", "Así se define en el vocabulario."),
        ("¿Cuál de estas es una regla del debate de la ficha? A) Reconocer los límites de la propia posición B) Repetir la misma idea hasta convencer", "A) Reconocer los límites de la propia posición", "Es una de las cuatro reglas de la ficha."),
        ("=", "Un debate de ejemplo tiene 8 turnos de 3 minutos. ¿Cuántos minutos dura?", "8*3", "Se multiplica el número de turnos por el tiempo.", " minutos")],
    op=("Prepara un turno de un minuto sobre una de las tres posiciones de la ficha (A, B o C). Escribe tu tesis, un argumento con su evidencia, un límite de esa posición y una frase que diga que explicar no es justificar. {F}",
        "Posición A: tesis: el diálogo se rompió. Argumento: la retórica de la violencia (Evidencia de discurso). Límite: no considera la presión externa. Frase: explico las causas sin justificar la violación de derechos humanos.",
        ["tiene tesis, argumento y límite", "respeta las reglas del debate", "distingue explicar de justificar"], ["turno escrito"], ["atacar a las personas", "afirmar más de lo que la evidencia permite"],
        "Pide que diga qué argumento de otra posición le parece más fuerte."),
    reinforce="Explica a alguien de tu casa por qué en un debate de historia importa la evidencia.",
    extend="Anota una regla que te gustaría que se aplicara en las discusiones de tu curso.",
)

OA = "HI2M OA 15"
TEXTOS = ("Interpretación A (de ejemplo): pone el foco en las decisiones de partidos y dirigentes chilenos, del gobierno y de la oposición, que habrían dejado de buscar acuerdos y se encerraron en proyectos que se excluían entre sí; usa debates del Congreso y discursos. "
          "Interpretación B (de ejemplo): pone el foco en el contexto de la Guerra Fría y en la presión externa; usa documentos desclasificados y cables diplomáticos. "
          "Interpretación C (de ejemplo): pone el foco en la desigualdad y en la crisis económica que sobrecargaron las instituciones; usa series de datos y estudios sociales. "
          "Son textos de ejemplo escritos para este cuaderno; no reproducen a ningún autor real.")

# ================================================================ OA 15, clase 1
F = ("Ficha 1. Historiografía es el estudio de cómo los historiadores han escrito y explicado un hecho. Una interpretación historiográfica es la explicación que un historiador propone sobre un hecho, apoyada en fuentes. "
     "Hecho que todas las interpretaciones aceptan: el 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno de Salvador Allende, elegido en 1970. " + TEXTOS)
build(
    OA, 1, F,
    use="Aprenderé a situar el golpe de 1973 como un tema sobre el que existen distintas interpretaciones, a reconocer quiénes las producen y a separar hecho de interpretación.",
    prior=["Conozco los actores y las causas de la crisis de 1970-1973.", "Sé distinguir hecho y opinión.", "Sé interrogar fuentes por su procedencia."],
    explain=[
        "La historiografía es el conjunto de lo que los historiadores han escrito sobre un tema y la forma en que lo explican. Sobre el golpe de Estado de 1973 y el quiebre de la democracia hay hechos que nadie discute, como la fecha, y explicaciones distintas sobre sus causas. A esas explicaciones se les llama interpretaciones historiográficas.",
        "Una interpretación elige una pregunta, unas fuentes y unos factores a los que da más peso. Una puede destacar las decisiones de los partidos chilenos, otra el contexto de la Guerra Fría y otra la desigualdad y la crisis económica. Ninguna tiene que ser falsa para ser distinta: cada una ilumina una parte del proceso.",
        "Para estudiarlas hay que situarlas: quién escribe, cuándo, qué pregunta se hace y con qué fuentes. Un error común es pensar que una interpretación es un hecho o que las demás están equivocadas por pensar distinto. La tarea es compararlas con criterios, no elegir un bando sin evidencia.",
    ],
    vocab=[("historiografía", "estudio de cómo los historiadores escriben y explican un hecho"), ("interpretación historiográfica", "explicación que un historiador propone sobre un hecho, apoyada en fuentes"), ("hecho", "dato que se puede comprobar con fecha y fuente"), ("factor", "causa o condición que influye en un proceso"), ("énfasis", "mayor peso que se da a un factor")],
    worked=[
        ("Separar hecho e interpretación", "«El 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno». ¿Es hecho o interpretación?", ["Se puede comprobar con fecha y fuentes.", "Todas las interpretaciones lo aceptan."], "Es un hecho"),
        ("Identificar el énfasis", "Un texto explica el golpe sobre todo por la Guerra Fría y usa cables diplomáticos. ¿Cuál es su énfasis?", ["Lee el factor que más pesa en la explicación.", "Es el contexto internacional."], "El contexto internacional"),
    ],
    mistakes=[("Creer que si dos interpretaciones son distintas, una es falsa.", "Pueden destacar factores diferentes y complementarse.", "Compara qué factor enfatiza cada una y con qué evidencia."),
              ("Tratar una interpretación como si fuera un hecho.", "Se olvida que es una explicación que se argumenta.", "Pregunta si se puede comprobar o si se debe argumentar.")],
    T=[
        ("{F} En Historia, ¿qué es la historiografía?", "El estudio de cómo los historiadores han escrito y explicado un hecho", "Así se define en la ficha."),
        ("{F} ¿En qué año fue elegido Allende?", "1970", "La ficha lo indica."),
        ("{F} ¿Qué factor enfatiza la Interpretación C?", "La desigualdad y la crisis económica", "Así se presenta en la ficha."),
        ("{F} ¿Qué pregunta se hace la Interpretación A? A) ¿Por qué partidos y dirigentes dejaron de buscar acuerdos? B) ¿Qué presión externa hubo sobre el país?", "A) ¿Por qué partidos y dirigentes dejaron de buscar acuerdos?", "La A pone el foco en las decisiones de partidos y dirigentes chilenos; la presión externa es el foco de la B."),
        ("=", "En una biblioteca de ejemplo hay 24 libros sobre el tema: 9 destacan la Guerra Fría y 7 las decisiones de los partidos; el resto destaca la crisis económica. ¿Cuántos destacan la crisis económica?", "24-9-7", "Se resta del total lo que enfatizan los otros dos factores.", " libros"),
        ("{F} ¿Qué fuentes usa la Interpretación B? A) Documentos desclasificados y cables diplomáticos B) Series de datos y estudios sociales", "A) Documentos desclasificados y cables diplomáticos", "La ficha los asocia a la B; la otra opción es de la C."),
        ("{F} ¿Cuál de estas frases es un hecho? A) Las Fuerzas Armadas derrocaron al gobierno el 11 de septiembre de 1973 B) La crisis económica fue la causa decisiva del golpe", "A) Las Fuerzas Armadas derrocaron al gobierno el 11 de septiembre de 1973", "La otra es una interpretación que se argumenta."),
        ("{F} Un texto explica el golpe sobre todo por discursos y debates del Congreso. ¿Con cuál se parece más? A) La Interpretación A B) La Interpretación C", "A) La Interpretación A", "Usa debates y discursos de actores chilenos."),
        ("{F} Un texto explica el quiebre sobre todo con gráficos de precios y de pobreza. ¿Con cuál se parece más? A) La Interpretación C B) La Interpretación B", "A) La Interpretación C", "Usa series de datos y estudios sociales."),
        ("{F} ¿Por qué dos interpretaciones distintas pueden ser ambas útiles?", "Porque cada una destaca un factor diferente del mismo proceso", "Se complementan en lugar de excluirse."),
        ("{F} Un compañero dice: «Si la B tiene razón, la A está equivocada». ¿Qué corrección haces? A) Pueden enfatizar factores distintos y ambas tener evidencia B) Es correcto, solo puede haber una", "A) Pueden enfatizar factores distintos y ambas tener evidencia", "La ficha muestra énfasis diferentes, no hechos contradictorios."),
        ("{F} ¿Qué dato necesito para situar bien una interpretación? A) Quién la escribe, cuándo y con qué fuentes B) Cuántas páginas tiene", "A) Quién la escribe, cuándo y con qué fuentes", "La procedencia permite entender su énfasis."),
        ("¿Cuál es una buena pregunta de investigación? A) ¿Qué factores destaca cada interpretación sobre el quiebre de 1973 y con qué evidencias? B) ¿Cuál historiador tiene la verdad?", "A) ¿Qué factores destaca cada interpretación sobre el quiebre de 1973 y con qué evidencias?", "Se responde comparando; la B pide un veredicto sin criterio."),
    ],
    ctx=("En una feria escolar un panel dice: «La historia del golpe de 1973 ya está resuelta: hay una sola explicación». ¿Qué problema tiene? A) Ignora que existen interpretaciones distintas que se discuten con evidencia B) Usa una fecha incorrecta", "A) Ignora que existen interpretaciones distintas que se discuten con evidencia", "La ficha muestra tres énfasis diferentes."),
    sc=[("En Historia, ¿qué es un factor?", "Una causa o condición que influye en un proceso", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una interpretación historiográfica?", "La explicación que un historiador propone sobre un hecho, apoyada en fuentes", "Así se define en la clase."),
        ("=", "En un estante de ejemplo hay 18 libros y 5 son sobre este tema. ¿Cuántos no lo son?", "18-5", "Se resta lo que sí lo es del total.", " libros")],
    op=("Completa una tabla con las Interpretaciones A, B y C: factor que enfatizan, fuentes que usan y una pregunta que cada una se hace. Después escribe una frase con un hecho que las tres aceptan. {F}",
        "A: decisiones de los partidos; debates y discursos; ¿por qué dejaron de dialogar? B: Guerra Fría; documentos desclasificados; ¿qué presión externa hubo? C: desigualdad y crisis; datos y estudios sociales; ¿qué demandas sobrecargaron las instituciones? Hecho: el 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno.",
        ["completa factor, fuentes y pregunta de las tres", "escribe un hecho aceptado por todas", "no declara a una como verdadera sin evidencia"], ["tabla", "frase con el hecho"], ["confundir hecho e interpretación", "decir que una es falsa por ser distinta"],
        "Pide que explique por qué ninguna interpretación de la tabla cubre por sí sola todo el proceso."),
    reinforce="Explica con tus palabras la diferencia entre un hecho y una interpretación sobre el golpe de 1973.",
    extend="Piensa en un conflicto escolar reciente y escribe dos explicaciones posibles que destaquen factores distintos.",
)

# ================================================================ OA 15, clase 2
F = ("Ficha 2 (cuatro textos de ejemplo escritos para este cuaderno; no reproducen a ningún autor real). "
     "Texto 1, escrito en 1976 por un autor chileno que vivió los hechos y escribe desde el exilio: «La crisis se explica sobre todo porque los grupos poderosos y sus aliados externos se negaron a aceptar los cambios.» "
     "Texto 2, escrito en 2013 por una historiadora que usa archivos abiertos años después: «El quiebre fue resultado de una combinación de polarización interna, crisis económica y presión externa; ningún factor basta por sí solo.» "
     "Texto 3, escrito en 1990 por un periodista que se basa en entrevistas a protagonistas: «Cada sector sintió que el otro amenazaba su futuro y por eso dejó de negociar.» "
     "Texto 4, escrito en 1974 por un autor chileno que apoyó al gobierno militar: «El gobierno de Allende perdió el respaldo del Congreso y violó la ley; por eso las Fuerzas Armadas intervinieron.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar interpretaciones sobre el golpe de 1973 por su procedencia: quién escribe, cuándo, desde dónde, con qué fuentes y con qué propósito.",
    prior=["Sé qué es una interpretación historiográfica.", "Sé distinguir hecho y juicio.", "Sé calcular diferencias entre años."],
    explain=[
        "Un texto histórico también tiene procedencia: quién lo escribió, cuándo, desde qué lugar y con qué fuentes. Una persona que vivió los hechos puede aportar vivencias muy valiosas, pero su cercanía puede influir en lo que destaca, sea que haya apoyado o rechazado el golpe. Una historiadora que escribe décadas después puede usar archivos que antes no estaban abiertos, pero su visión también se forma en su época.",
        "Por eso no se pregunta «¿es verdadero o falso?», sino «¿en qué se apoya y desde dónde habla?». Se revisa qué fuentes usa, si distingue entre hechos y juicios y si reconoce los límites de lo que afirma. Un texto que dice «ningún factor basta por sí solo» muestra prudencia sobre las causas.",
        "La procedencia no descalifica un texto: explica su énfasis. Un testimonio vivido, un estudio con archivos y un trabajo periodístico con entrevistas son tipos de fuente distintos que se complementan. Para sacar una conclusión proporcional hay que contrastarlos. Y entender el argumento de un autor no es justificar lo que vino después, como las violaciones a los derechos humanos.",
    ],
    vocab=[("procedencia", "datos sobre quién escribe un texto, cuándo, dónde y con qué fuentes"), ("testimonio", "relato de una persona que vivió los hechos"), ("archivo", "conjunto de documentos conservados que sirven como fuente"), ("exilio", "vida fuera del país por razones políticas"), ("proporcional", "que no afirma más de lo que la evidencia permite")],
    worked=[
        ("Reconocer la procedencia", "El Texto 2 fue escrito en 2013 con archivos abiertos después. ¿Qué ventaja tiene?", ["Se pregunta qué pudo usar que antes no estaba disponible.", "Pudo consultar documentos que el autor de 1976 no tenía."], "Pudo usar archivos que antes no estaban abiertos"),
        ("Detectar un límite", "El Texto 3 usa entrevistas a protagonistas. ¿Qué límite tiene?", ["Los protagonistas hablan de lo que recuerdan y viven.", "Pueden destacar lo que los favorece."], "Depende de recuerdos que pueden ser parciales"),
    ],
    mistakes=[("Descartar un texto solo porque su autor vivió los hechos o porque escribe desde un lugar determinado.", "Se confunde procedencia con falsedad.", "Usa la procedencia para entender el énfasis y luego revisa las evidencias."),
              ("Creer que un texto más reciente siempre es mejor.", "Se supone que más tarde es más verdadero.", "Revisa las fuentes y la prudencia de cada texto.")],
    T=[
        ("{F} ¿En qué año se escribió el Texto 1?", "1976", "La ficha lo indica."),
        ("{F} ¿Qué fuentes usa el autor del Texto 3?", "Entrevistas a protagonistas", "Así se presenta en la ficha."),
        ("{F} ¿Qué dos textos escribieron, pocos años después del golpe, autores chilenos que habían vivido los hechos y tomaron posiciones opuestas? A) Los Textos 1 y 4 B) Los Textos 2 y 3", "A) Los Textos 1 y 4", "El 1 desde el exilio y el 4 desde el apoyo al gobierno militar; el 2 es de 2013 y el 3 de 1990."),
        ("=", "{F} ¿Cuántos años pasaron entre el golpe de Estado de 1973 y la escritura del Texto 2?", "2013-1973", "Se resta el año del golpe al del texto.", " años"),
        ("{F} ¿Qué texto pudo usar archivos que el autor del Texto 1 no podía consultar en 1976? A) El Texto 2 B) El Texto 3", "A) El Texto 2", "La historiadora usa archivos abiertos años después; el Texto 3 se basa en entrevistas."),
        ("{F} En Historia, ¿qué es la procedencia de un texto? A) Quién lo escribe, cuándo, dónde y con qué fuentes B) Cuántas páginas tiene", "A) Quién lo escribe, cuándo, dónde y con qué fuentes", "Es la definición de la clase."),
        ("{F} ¿Qué texto muestra más prudencia sobre las causas? A) El Texto 2 B) El Texto 1", "A) El Texto 2", "Dice que ningún factor basta por sí solo."),
        ("{F} El Texto 3 dice que cada sector sintió amenazado su futuro. ¿Qué tipo de afirmación es? A) Una interpretación sobre cómo vivieron los sectores el conflicto B) Un dato comprobable con un acta", "A) Una interpretación sobre cómo vivieron los sectores el conflicto", "Habla de percepciones, no de un hecho fechado."),
        ("{F} ¿Por qué el Texto 1 puede destacar más a ciertos grupos?", "Porque su autor vivió los hechos y escribe desde el exilio, lo que influye en su énfasis", "La procedencia explica el énfasis."),
        ("{F} Una estudiante dice: «El Texto 2 es mejor porque es más nuevo». ¿Qué corrección haces? A) Hay que revisar sus fuentes y su prudencia, no solo la fecha B) Tiene razón, lo nuevo siempre es mejor", "A) Hay que revisar sus fuentes y su prudencia, no solo la fecha", "La fecha no basta para evaluar un texto."),
        ("{F} ¿Qué límite comparten los Textos 1 y 4 en las citas de la ficha? A) Afirman una causa principal sin mostrar en la cita qué evidencia la sostiene B) Fueron escritos antes de 1973", "A) Afirman una causa principal sin mostrar en la cita qué evidencia la sostiene", "Una afirmación fuerte requiere evidencia visible."),
        ("{F} ¿Qué conclusión es proporcional a los cuatro textos? A) Distintos autores, épocas y fuentes dan explicaciones diferentes del mismo proceso B) Los cuatro prueban que una sola causa explica todo", "A) Distintos autores, épocas y fuentes dan explicaciones diferentes del mismo proceso", "La otra afirma más de lo que muestran."),
        ("{F} ¿Qué documento permitiría contrastar el Texto 3? A) Actas fechadas de reuniones entre los sectores B) Un resumen sin autor", "A) Actas fechadas de reuniones entre los sectores", "Sirve para comprobar las percepciones con registros."),
    ],
    ctx=("Una profesora te entrega un libro sin autor ni fecha y te pide usarlo como fuente. ¿Qué haces primero? A) Buscar su procedencia o reemplazarlo por una fuente atribuida B) Copiar sus conclusiones", "A) Buscar su procedencia o reemplazarlo por una fuente atribuida", "Sin procedencia no se puede evaluar la fuente."),
    sc=[("En Historia, ¿qué es un testimonio?", "El relato de una persona que vivió los hechos", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es un archivo?", "Un conjunto de documentos conservados que sirven como fuente", "Así se define en la clase."),
        ("Un autor escribe en 1980 desde el exilio y otro en 2015 con archivos abiertos. ¿Qué diferencia de procedencia importa? A) Distinta época, distinta posición y distintas fuentes disponibles B) Ninguna, porque ambos tratan el mismo tema", "A) Distinta época, distinta posición y distintas fuentes disponibles", "La procedencia explica el énfasis de cada texto.")],
    op=("Elige dos de los cuatro textos de la ficha. Para cada uno anota autor, año, tipo de fuente que usa, énfasis y un límite. Después escribe una frase proporcional que compare ambos sin decir cuál es verdadero. {F}",
        "Textos 1 y 2: 1976, vivido, énfasis en grupos poderosos y aliados externos; 2013, archivos, combina factores. Límite: el 1 no muestra evidencia en la cita; el 2 depende de los archivos disponibles. Frase: ambos explican el proceso con énfasis distintos según su época y sus fuentes.",
        ["anota los cinco datos de cada texto", "usa la procedencia para explicar el énfasis", "no declara verdadero a uno"], ["tabla", "frase proporcional"], ["descartar un texto por su autor", "creer que lo reciente es mejor"],
        "Pide que diga qué otra fuente consultaría para contrastar el énfasis de cada texto."),
    reinforce="Explica con tus palabras por qué la procedencia ayuda a entender un texto sin descalificarlo.",
    extend="Compara cómo dos personas distintas de tu entorno cuentan un mismo suceso reciente y anota qué destaca cada una.",
)

# ================================================================ OA 15, clase 3
F = ("Ficha 3 (comparación de las interpretaciones de ejemplo). " + TEXTOS + " "
     "Criterios de comparación: pregunta que se hace, factor que enfatiza, tipo de fuente, escala (local, nacional o internacional) y lo que omite. "
     "Datos de ejemplo: 3 de los 12 capítulos de un libro de ejemplo tratan el contexto internacional.")
build(
    OA, 3, F,
    use="Aprenderé a comparar críticamente varias interpretaciones del golpe de 1973 con criterios fijos, sin tomar partido por una sin evidencia.",
    prior=["Sé situar una interpretación y su procedencia.", "Conozco las escalas local, nacional e internacional.", "Sé calcular fracciones sencillas."],
    explain=[
        "Comparar críticamente es examinar cada interpretación con los mismos criterios para ver en qué coinciden y en qué difieren. Los criterios de esta clase son: la pregunta que se hace, el factor que enfatiza, el tipo de fuente que usa, la escala desde la que mira y lo que omite o deja en segundo plano.",
        "La Interpretación A mira sobre todo la escala nacional y las decisiones de los partidos. La B mira la escala internacional y la presión externa. La C mira la estructura social y económica. Cada una tiene fortalezas, porque explica bien un aspecto, y límites, porque deja otros en segundo plano.",
        "Comparar no es votar por la mejor. Es decir qué explica cada una y qué le falta, y luego ver si se pueden combinar. Un error común es juzgar una interpretación porque no responde a una pregunta que nunca se hizo.",
    ],
    vocab=[("criterio", "regla fija que se usa para comparar"), ("fortaleza", "aspecto que una interpretación explica bien"), ("omisión", "aspecto que una interpretación deja fuera o en segundo plano"), ("complementarse", "completarse una con otra"), ("críticamente", "examinando con criterios y evidencia, sin aceptar ni rechazar sin razones")],
    worked=[
        ("Aplicar un criterio", "¿Qué escala usa la Interpretación B?", ["Se mira el tipo de factor que enfatiza: la Guerra Fría y la presión externa.", "Eso corresponde a relaciones entre países."], "La escala internacional"),
        ("Identificar una omisión", "La Interpretación A casi no usa datos económicos. ¿Qué omite?", ["Su foco son las decisiones de los partidos.", "Deja en segundo plano la estructura económica."], "Los factores económicos"),
    ],
    mistakes=[("Juzgar una interpretación por lo que no pretende explicar.", "Se le exige una pregunta que no se hizo.", "Primero identifica su pregunta y luego evalúa si la responde."),
              ("Quedarse con la que coincide con la opinión propia.", "Se elige por simpatía y no por evidencia.", "Usa los mismos criterios en todas.")],
    T=[
        ("{F} ¿Qué factor enfatiza la Interpretación A?", "Las decisiones de los partidos y dirigentes chilenos", "Así se presenta en la ficha."),
        ("{F} ¿Qué tipo de fuentes usa la Interpretación C?", "Series de datos y estudios sociales", "Así se presenta en la ficha."),
        ("{F} ¿Cuál de estos es un criterio de comparación de la ficha? A) La escala desde la que mira la interpretación B) El prestigio de su autor", "A) La escala desde la que mira la interpretación", "La ficha enumera pregunta, factor, tipo de fuente, escala y lo que omite; el prestigio no es un criterio."),
        ("=", "{F} ¿Qué porcentaje del libro de ejemplo trata el contexto internacional?", "3/12*100", "Se divide 3 por 12 y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos capítulos del libro de ejemplo no tratan el contexto internacional?", "12-3", "Se resta del total los capítulos que sí lo tratan.", " capítulos"),
        ("{F} ¿En qué escala se ubica sobre todo la Interpretación A? A) Nacional B) Internacional", "A) Nacional", "Mira las decisiones de partidos y dirigentes chilenos."),
        ("{F} ¿Qué omite o deja en segundo plano la Interpretación B? A) Las decisiones de los actores chilenos B) La Guerra Fría", "A) Las decisiones de los actores chilenos", "Su foco está en lo externo."),
        ("{F} ¿Cuál es una fortaleza de la Interpretación C? A) Explica cómo la desigualdad y la economía presionaban a las instituciones B) Muestra todos los cables diplomáticos", "A) Explica cómo la desigualdad y la economía presionaban a las instituciones", "Es lo que su foco permite ver; los cables son de la B."),
        ("{F} ¿Por qué comparar con los mismos criterios evita tomar partido sin evidencia?", "Porque todas se examinan con las mismas preguntas y no por simpatía", "Un criterio común trata a todas igual."),
        ("{F} Un compañero dice: «La A está mal porque no habla de la Guerra Fría». ¿Qué corrección haces? A) Su pregunta es otra; lo adecuado es decir que lo deja en segundo plano B) Tiene razón, toda interpretación debe hablar de todo", "A) Su pregunta es otra; lo adecuado es decir que lo deja en segundo plano", "Se evalúa según su pregunta, no según lo que no se propuso."),
        ("{F} ¿Se pueden combinar las tres interpretaciones? A) Sí, porque destacan factores distintos que pueden complementarse B) No, porque se contradicen en todo", "A) Sí, porque destacan factores distintos que pueden complementarse", "No niegan el mismo hecho, sino que cambian el énfasis."),
        ("{F} ¿Qué conclusión es proporcional a la comparación? A) Cada interpretación explica bien un aspecto y deja otros en segundo plano B) La B es la única válida porque usa documentos desclasificados", "A) Cada interpretación explica bien un aspecto y deja otros en segundo plano", "La otra afirma más de lo que la comparación muestra."),
        ("{F} ¿Qué haría más sólida una comparación? A) Revisar para cada interpretación la evidencia concreta que cita B) Contar cuál tiene más páginas", "A) Revisar para cada interpretación la evidencia concreta que cita", "La evidencia permite evaluar los argumentos."),
    ],
    ctx=("En una charla escolar alguien afirma: «Solo las interpretaciones que culpan a un país extranjero son serias». ¿Qué problema tiene? A) Escoge por conveniencia y no compara con criterios B) Usa una fecha incorrecta", "A) Escoge por conveniencia y no compara con criterios", "Una comparación crítica examina todas con los mismos criterios."),
    sc=[("En Historia, ¿qué es un criterio de comparación?", "Una regla fija que se usa para comparar", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una omisión?", "Un aspecto que una interpretación deja fuera o en segundo plano", "Así se define en la clase."),
        ("=", "Un libro de ejemplo tiene 10 capítulos y 3 tratan la economía. ¿Cuántos no la tratan?", "10-3", "Se resta lo que sí la trata del total.", " capítulos")],
    op=("Arma una tabla con las Interpretaciones A, B y C y los cinco criterios de la ficha. Después escribe tres frases: una sobre una coincidencia, una sobre una diferencia y una sobre cómo podrían combinarse. {F}",
        "Coincidencia: las tres aceptan que el 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno. Diferencia: la A enfatiza decisiones de partidos y la B la presión externa. Combinación: la crisis pudo resultar de decisiones internas, desigualdad y presión externa a la vez.",
        ["completa los cinco criterios de las tres", "escribe coincidencia, diferencia y combinación", "no toma partido sin evidencia"], ["tabla", "tres frases"], ["juzgar por lo que no pretende explicar", "elegir por simpatía"],
        "Pide que diga qué evidencia pediría a cada interpretación para sostener su énfasis."),
    reinforce="Explica a alguien de tu casa qué significa comparar con criterios en lugar de elegir la que más te gusta.",
    extend="Elige dos reseñas de una película y compáralas con tres criterios que tú definas.",
)

# ================================================================ OA 15, clase 4
F = ("Ficha 4 (cambios y continuidades en la historiografía; datos de ejemplo). "
     "Primera etapa, de ejemplo: en los años inmediatos al golpe, muchos textos se escribían con pocos documentos disponibles, muchas veces desde el exilio y con fuerte carga política. "
     "Segunda etapa, de ejemplo: con los años se abrieron archivos, se recogieron más testimonios y surgieron estudios de la economía y de la sociedad, lo que permitió interpretaciones más complejas. "
     "Continuidades: casi todas las interpretaciones reconocen la polarización, la crisis económica y el contexto de Guerra Fría, aunque con distinto peso; todas aceptan la fecha del golpe, el 11 de septiembre de 1973. "
     "Dato de ejemplo: un catálogo registra 20 libros de la primera etapa y 60 de la segunda.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar los cambios y continuidades en cómo se ha interpretado el golpe de 1973, y a explicar por qué cambian las interpretaciones con el tiempo.",
    prior=["Sé comparar interpretaciones con criterios.", "Sé qué es una causa de largo y corto plazo.", "Sé calcular razones sencillas."],
    explain=[
        "Las interpretaciones sobre el golpe de 1973 no son siempre las mismas: cambian con el tiempo. Cambian porque se abren nuevos archivos, se recogen más testimonios, aparecen nuevas preguntas y cambia el contexto en que escriben las personas. Es un cambio normal en la historiografía, no una prueba de que antes todo estaba mal.",
        "También hay continuidades. Casi todas las interpretaciones reconocen la polarización, la crisis económica y el contexto de la Guerra Fría, aunque con distinto peso, y todas aceptan la fecha del golpe. Estas coincidencias muestran puntos firmes sobre los que se puede construir.",
        "Para relacionar causas, cambios y continuidades en la historiografía conviene preguntar: qué se sabe hoy que antes no se sabía, qué preguntas son nuevas y qué se mantiene. Se evita decir que lo nuevo reemplaza por completo a lo anterior, porque muchas ideas se conservan y otras se corrigen con evidencia.",
    ],
    vocab=[("cambio historiográfico", "modificación en cómo se interpreta un tema con el tiempo"), ("continuidad", "idea o dato que se mantiene a pesar de los cambios"), ("contexto de escritura", "situación del momento en que un autor escribe"), ("complejidad", "presencia de muchos factores relacionados"), ("evidencia nueva", "documentos o testimonios que antes no estaban disponibles")],
    worked=[
        ("Clasificar un cambio", "Se abren archivos que antes estaban cerrados. ¿Es cambio o continuidad en la historiografía?", ["Antes no se podían consultar y ahora sí.", "Modifica lo que se puede investigar."], "Es un cambio"),
        ("Calcular una proporción", "En un catálogo de ejemplo hay 25 libros de la primera etapa y 75 de la segunda. ¿Cuántas veces es mayor la segunda?", ["Divido 75 en 25.", "75 ÷ 25 = 3."], "3 veces"),
    ],
    mistakes=[("Pensar que las interpretaciones antiguas están equivocadas por ser antiguas.", "Se confunde cambio con corrección total.", "Pregunta qué evidencia tenían y qué preguntas se hacían."),
              ("Creer que todo cambió y nada se mantuvo.", "No se ven las continuidades.", "Busca qué reconocen todas las interpretaciones.")],
    T=[
        ("{F} ¿Qué fecha aceptan todas las interpretaciones?", "El 11 de septiembre de 1973", "La ficha lo indica."),
        ("{F} ¿Qué se abrió con los años que permitió estudios más complejos?", "Archivos", "La ficha lo menciona."),
        ("{F} ¿Qué reconocen casi todas las interpretaciones además de la polarización y la crisis económica?", "El contexto de la Guerra Fría", "Está en las continuidades de la ficha."),
        ("=", "{F} ¿Cuántos libros hay en total en el catálogo de ejemplo?", "20+60", "Se suman los libros de ambas etapas.", " libros"),
        ("=", "{F} ¿Cuántas veces mayor es el número de libros de la segunda etapa que el de la primera?", "60/20", "Se divide 60 por 20.", " veces"),
        ("{F} La aparición de más testimonios es: A) Un cambio B) Una continuidad", "A) Un cambio", "Modifica la evidencia disponible."),
        ("{F} Que todas las interpretaciones acepten la fecha del golpe es: A) Una continuidad B) Un cambio", "A) Una continuidad", "Es un punto que se mantiene."),
        ("{F} Una historiadora formula hoy una pregunta nueva sobre cómo vivían las familias en las poblaciones. ¿Qué tipo de cambio es? A) Un cambio en el foco del estudio B) Una continuidad con la primera etapa", "A) Un cambio en el foco del estudio", "Antes se preguntaba otra cosa; la fecha del golpe, en cambio, es una continuidad."),
        ("{F} ¿Por qué las interpretaciones de la segunda etapa pueden ser más complejas?", "Porque tienen más documentos, testimonios y estudios disponibles", "Más evidencia permite combinar más factores."),
        ("{F} Una compañera dice: «Los textos de la primera etapa no sirven para nada». ¿Qué corrección haces? A) Sirven como fuente para conocer cómo se interpretaba entonces y qué se sabía B) Tiene razón, lo antiguo no vale", "A) Sirven como fuente para conocer cómo se interpretaba entonces y qué se sabía", "Cada etapa muestra su contexto de escritura."),
        ("{F} ¿Qué afirmación es proporcional? A) Con más evidencia cambiaron los énfasis, pero se mantuvieron puntos comunes B) Después de abrirse los archivos todo lo anterior quedó descartado", "A) Con más evidencia cambiaron los énfasis, pero se mantuvieron puntos comunes", "Reúne cambios y continuidades."),
        ("{F} ¿Qué relación causal es prudente? A) La apertura de archivos contribuyó a que surgieran interpretaciones más complejas B) La apertura de archivos causó por sí sola todas las interpretaciones actuales", "A) La apertura de archivos contribuyó a que surgieran interpretaciones más complejas", "Evita una causa única."),
        ("{F} ¿Qué pregunta ayuda a estudiar el cambio historiográfico? A) ¿Qué evidencia nueva apareció y qué preguntas nuevas permitió? B) ¿Quién escribió más páginas?", "A) ¿Qué evidencia nueva apareció y qué preguntas nuevas permitió?", "Relaciona cambio y causas."),
    ],
    ctx=("Un diario escolar titula: «Los historiadores se equivocaban hasta que se abrieron los archivos». ¿Qué problema tiene? A) Ignora el contexto de cada época y las continuidades B) Es muy largo", "A) Ignora el contexto de cada época y las continuidades", "Cada etapa tenía otras fuentes y preguntas."),
    sc=[("En Historia, ¿qué es una continuidad?", "Una idea o dato que se mantiene a pesar de los cambios", "Así se define en el vocabulario."),
        ("¿Cuál es una razón por la que cambian las interpretaciones? A) Se abren archivos y se recogen más testimonios B) Los hechos del pasado cambian de fecha", "A) Se abren archivos y se recogen más testimonios", "La explicación la enumera junto a nuevas preguntas y un contexto distinto."),
        ("=", "En un catálogo de ejemplo hay 15 libros antiguos y 45 recientes. ¿Cuántos libros hay en total?", "15+45", "Se suman ambas cantidades.", " libros")],
    op=("Completa un cuadro con dos columnas, «primera etapa» y «segunda etapa». Escribe para cada una la evidencia disponible, un tipo de pregunta y un énfasis. Debajo escribe dos continuidades y una frase con «contribuyó a…» sobre la apertura de archivos. {F}",
        "Primera etapa: pocos documentos; fuerte carga política. Segunda: archivos y testimonios; estudios de economía y sociedad. Continuidades: polarización, crisis económica y fecha del golpe. Frase: la apertura de archivos contribuyó a interpretaciones más complejas.",
        ["completa ambas etapas", "incluye dos continuidades", "evita causas únicas"], ["cuadro", "frase con «contribuyó a…»"], ["decir que todo cambió", "descartar lo antiguo"],
        "Pide que explique por qué un texto antiguo igual es útil como fuente."),
    reinforce="Explica por qué una interpretación puede cambiar con el tiempo sin que la anterior sea absurda.",
    extend="Piensa en un tema escolar sobre el que hoy se sepa más que hace diez años y di qué cambió.",
)

# ================================================================ OA 15, clase 5
F = ("Ficha 5 (pregunta y material para una interpretación propia). " + TEXTOS + " "
     "Pregunta: ¿cómo se relacionan los factores internos y externos en el quiebre democrático de 1973? "
     "Evidencias de ejemplo: E1, un discurso de 1972 que habla de vencer a los adversarios; E2, un informe desclasificado de ejemplo sobre apoyo externo a opositores; E3, una tabla de ejemplo con alza de precios de 60 %; E4, un testimonio de ejemplo de una familia que hacía filas para comprar alimentos. "
     "Modelo: tesis, argumentos con evidencia, comparación con al menos una interpretación y un límite.")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación propia y documentada sobre el golpe de 1973, comparándola con las interpretaciones de la ficha y reconociendo sus límites.",
    prior=["Sé comparar interpretaciones con criterios.", "Sé escribir tesis, argumentos y límite.", "Sé distinguir causas de largo y corto plazo."],
    explain=[
        "Construir una interpretación propia es elegir una pregunta, reunir evidencias de distinto tipo y escribir una tesis que las relacione. Aquí la pregunta es cómo se relacionan los factores internos, como la polarización y la economía, con los externos, como la Guerra Fría y la presión extranjera.",
        "Una interpretación madura dialoga con otras. Puedes decir en qué coincides con la Interpretación A, qué agregas desde la B o qué te enseña la C. También debes mostrar tus evidencias y sus límites: un discurso muestra la retórica, una tabla muestra el alza de precios, un informe muestra apoyo externo y un testimonio muestra la vida cotidiana de una familia.",
        "Tu texto debe evitar causas únicas y verbos como «demuestra todo». Usa expresiones como «contribuyó a», «es coherente con» o «las evidencias disponibles sugieren». Termina con un límite: qué te faltaría para estar más seguro o segura. No defiendas una interpretación sin evidencia ni justifiques violaciones a los derechos humanos.",
    ],
    vocab=[("interpretación propia", "explicación que cada persona construye con evidencias y criterios"), ("dialogar con otras interpretaciones", "decir en qué se coincide, en qué se difiere y qué se agrega"), ("evidencia sugerente", "evidencia que apoya una idea sin probarla del todo"), ("tesis matizada", "tesis que reconoce varios factores y sus límites"), ("coherente con", "que concuerda con la evidencia sin demostrarlo por completo")],
    worked=[
        ("Relacionar evidencia y argumento", "Quiero argumentar que la vida cotidiana se vio afectada por la escasez. ¿Qué evidencia de la ficha me sirve?", ["Busco una evidencia sobre la vida diaria de personas comunes.", "El testimonio de la familia que hacía filas lo muestra."], "E4, el testimonio de la familia"),
        ("Dialogar con otra interpretación", "Mi tesis combina decisiones de partidos y presión externa. ¿Con cuáles interpretaciones dialoga?", ["Las decisiones de partidos son el énfasis de la A.", "La presión externa es el énfasis de la B."], "Con la A y con la B"),
    ],
    mistakes=[("Copiar una interpretación sin evidencia propia.", "Se repite lo que dice otro sin comprobarlo.", "Cita al menos dos evidencias y explica qué muestran."),
              ("Usar verbos como «demuestra» con una sola evidencia.", "Se afirma más de lo que la evidencia permite.", "Usa «sugiere» o «contribuyó a» y agrega un límite.")],
    T=[
        ("{F} ¿Cuál es la pregunta de la ficha?", "Cómo se relacionan los factores internos y externos en el quiebre democrático de 1973", "Está escrita en la ficha."),
        ("{F} ¿Qué evidencia es un testimonio?", "E4", "Es el relato de la familia que hacía filas."),
        ("{F} ¿Qué evidencia corresponde a la presión externa?", "E2", "Es el informe desclasificado sobre apoyo externo."),
        ("=", "{F} Si un producto de ejemplo costaba 100 pesos de ejemplo y subió lo que dice E3, ¿cuánto cuesta ahora?", "100+100*60/100", "Se suma el 60 % de aumento al precio inicial.", " pesos de ejemplo"),
        ("=", "En el curso de ejemplo, 36 estudiantes forman grupos de 4 para comparar interpretaciones. ¿Cuántos grupos hay?", "36/4", "Se reparte el total en grupos iguales.", " grupos"),
        ("{F} ¿Qué evidencia sostiene un argumento sobre la retórica de la violencia? A) E1 B) E3", "A) E1", "El discurso habla de vencer a los adversarios."),
        ("{F} ¿Qué evidencia sostiene un argumento sobre el alza de precios? A) E3 B) E2", "A) E3", "La tabla muestra el alza de 60 %."),
        ("{F} Mi tesis dice que el quiebre se explica por decisiones de partidos y por presión externa. ¿Con qué interpretaciones dialoga? A) La A y la B B) Solo la C", "A) La A y la B", "Combina los énfasis de ambas."),
        ("{F} ¿Por qué E4 no prueba por sí sola la causa del quiebre?", "Porque es el testimonio de una familia y muestra un caso", "Un caso no permite generalizar."),
        ("{F} ¿Qué verbo es más prudente para cerrar el párrafo? A) «Las evidencias sugieren que» B) «Está demostrado que»", "A) «Las evidencias sugieren que»", "No afirma más de lo que la evidencia muestra."),
        ("{F} ¿Cuál es un buen límite? A) Con estas cuatro evidencias no puedo medir cuánto pesó cada factor B) Con estas evidencias lo expliqué todo", "A) Con estas cuatro evidencias no puedo medir cuánto pesó cada factor", "Reconoce lo que las fuentes no permiten."),
        ("{F} Un compañero escribe: «Como la B usa documentos desclasificados, es la correcta». ¿Qué corrección haces? A) Los documentos son una evidencia valiosa, pero una interpretación se evalúa con varios criterios B) Tiene razón, solo importan los documentos", "A) Los documentos son una evidencia valiosa, pero una interpretación se evalúa con varios criterios", "Los criterios incluyen pregunta, escala y omisiones."),
        ("{F} ¿Qué tesis es mejor? A) Factores internos y externos se reforzaron entre sí y contribuyeron a debilitar la institucionalidad B) Todo se explica por un solo factor", "A) Factores internos y externos se reforzaron entre sí y contribuyeron a debilitar la institucionalidad", "Es matizada y relaciona factores."),
    ],
    ctx=("En un trabajo, una estudiante defiende la Interpretación B sin citar ninguna evidencia. ¿Qué le recomiendas? A) Agregar evidencias concretas y compararla con otra interpretación B) Escribir con más seguridad", "A) Agregar evidencias concretas y compararla con otra interpretación", "Una interpretación documentada necesita evidencias y diálogo."),
    sc=[("En Historia, ¿qué es una tesis matizada?", "Una tesis que reconoce varios factores y sus límites", "Así se define en el vocabulario."),
        ("En Historia, ¿qué significa dialogar con otras interpretaciones?", "Decir en qué se coincide, en qué se difiere y qué se agrega", "Así se define en la clase."),
        ("=", "Un grupo de ejemplo de 5 estudiantes revisa 3 evidencias cada uno. ¿Cuántas revisiones hacen en total?", "5*3", "Se multiplican los estudiantes por las evidencias.", " revisiones")],
    op=("Escribe un texto de seis a ocho líneas que responda la pregunta de la ficha. Debe tener una tesis matizada, dos argumentos con evidencias (E1 a E4), una comparación con una de las Interpretaciones A, B o C y un límite. No justifiques violaciones a los derechos humanos ni culpes a un solo actor. {F}",
        "Tesis: factores internos y externos se reforzaron entre sí. Argumento 1: la retórica de la violencia (E1). Argumento 2: la presión externa (E2) y el alza de precios (E3). Comparación: coincido con la A en las decisiones internas y con la B en la presión externa. Límite: no puedo medir cuánto pesó cada factor.",
        ["tesis matizada con dos argumentos y evidencias", "compara con una interpretación", "incluye un límite y evita causas únicas"], ["texto escrito"], ["copiar sin evidencia", "usar verbos que afirman demasiado"],
        "Pide que cambie un verbo fuerte por uno prudente y que diga qué evidencia le faltaría."),
    reinforce="Explica en voz alta tu tesis, una evidencia y tu límite.",
    extend="Escribe una tesis matizada de cuatro líneas sobre un tema de tu elección, con una evidencia y un límite.",
)
