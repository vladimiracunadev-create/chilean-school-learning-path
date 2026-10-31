"""Material del estudiante de 7.º básico, Historia, Geografía y Ciencias Sociales: OA 06 (democracia ateniense, participación y exclusiones)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI07 OA 06"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 1 (resumen hecho para este cuaderno). Atenas fue una ciudad-Estado de Grecia que en el siglo V a. C. tenía un gobierno llamado democracia. "
     "Asamblea (Ekklesía): reunión de ciudadanos que votaban leyes y decisiones sobre la guerra y la paz; se reunía unas 40 veces al año. "
     "Consejo de los 500 (Boulé): preparaba los temas de la Asamblea; tenía 50 miembros por cada una de las 10 tribus (grupos en que se dividían los ciudadanos), elegidos por sorteo cada año. "
     "Tribunales populares (Heliea): los jurados eran ciudadanos elegidos por sorteo. "
     "Estrategos: 10 generales elegidos por votación cada año. "
     "Actores: Clístenes, que hizo reformas hacia 508 a. C.; Pericles, líder muy influyente entre 461 y 429 a. C.")
build(
    OA, 1, F,
    use="Aprenderé a ubicar las instituciones y los actores de la democracia ateniense. Sirve para entender quién decidía qué en Atenas.",
    prior=["Sé qué es una ciudad-Estado.", "Sé comparar años a. C.", "Sé que Grecia estaba formada por muchas ciudades-Estado."],
    explain=[
        "Democracia significa «gobierno del pueblo». En Atenas, en el siglo V a. C., los ciudadanos participaban directamente en las decisiones. La institución principal era la Asamblea, donde los ciudadanos votaban las leyes y las decisiones de guerra y paz; se reunía unas 40 veces al año.",
        "El Consejo de los 500 preparaba los temas que se discutían en la Asamblea; sus miembros se elegían por sorteo cada año. Los tribunales populares tenían jurados ciudadanos, también elegidos por sorteo. Los estrategos, diez generales, se elegían por votación, porque se necesitaba experiencia.",
        "Esta organización se fue construyendo en el tiempo. Clístenes hizo reformas hacia 508 a. C. y Pericles fue un líder muy influyente entre 461 y 429 a. C. Atenas era una democracia para los ciudadanos, un grupo limitado; en las próximas clases veremos quiénes participaban y quiénes quedaban fuera.",
    ],
    vocab=[("democracia", "gobierno donde el pueblo participa en las decisiones"), ("Asamblea", "reunión de ciudadanos que votaba leyes y decisiones importantes"), ("sorteo", "elección por azar entre quienes pueden participar"), ("estratego", "general elegido por votación en Atenas"), ("tribu", "uno de los diez grupos en que se dividían los ciudadanos")],
    worked=[
        ("Calcular miembros del Consejo", "{F} Si cada tribu aporta 50 miembros, ¿cuántos miembros tiene el Consejo con 10 tribus?", ["Multiplico los miembros por las tribus.", "50 × 10 = 500."], "500 miembros"),
        ("Distinguir sorteo y votación", "{F} ¿Cómo se elegían los estrategos?", ["La ficha dice que se elegían por votación.", "Los jurados, en cambio, por sorteo."], "Por votación"),
    ],
    mistakes=[("Pensar que el Consejo de los 500 decidía todo por sí solo.", "Se confunde preparar los temas con decidirlos.", "El Consejo preparaba los temas; la Asamblea los votaba."),
              ("Decir que todos los cargos de Atenas se elegían por sorteo.", "No se distinguen los cargos que exigían experiencia.", "Los estrategos se elegían por votación.")],
    T=[
        ("{F} ¿Qué institución votaba las leyes?", "La Asamblea", "La ficha lo indica."),
        ("{F} ¿Cuántos estrategos había?", "10", "La ficha lo indica."),
        ("{F} ¿Cómo se elegían los jurados de los tribunales populares?", "Por sorteo", "La ficha lo indica."),
        ("=", "{F} ¿Cuántas reuniones tendría la Asamblea en 5 años a razón de 40 por año?", "5*40", "Se multiplican los años por las reuniones anuales.", " reuniones"),
        ("{F} ¿Quién hizo reformas hacia 508 a. C.?", "Clístenes", "La ficha lo indica."),
        ("{F} ¿Qué institución preparaba los temas de la Asamblea?", "El Consejo de los 500", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años duró el periodo de influencia de Pericles, de 461 a 429 a. C.?", "461-429", "Se restan los años a. C.", " años"),
        ("{F} Relaciona la tarea con la institución: votar leyes, preparar los temas, juzgar, dirigir el ejército.", "Votar leyes: Asamblea; preparar los temas: Consejo; juzgar: tribunales populares; dirigir el ejército: estrategos", "Cada institución tiene su tarea en la ficha."),
        ("=", "{F} Con 10 estrategos elegidos por año, ¿cuántos estrategos se eligen en 6 años?", "6*10", "Se multiplican los años por los estrategos de cada año.", " estrategos"),
        ("{F} ¿Por qué se elegía a los miembros del Consejo por sorteo?", "Para que cualquier ciudadano pudiera participar y para evitar que el poder se concentrara", "El sorteo daba igual oportunidad a los ciudadanos."),
        ("{F} Ana dice: «El Consejo de los 500 decidía todo». Corrígela con la ficha.", "El Consejo solo preparaba los temas; la Asamblea los votaba", "La ficha distingue las tareas."),
        ("{F} ¿Por qué los estrategos se elegían por votación y no por sorteo?", "Porque se necesitaba experiencia para dirigir el ejército", "Un sorteo no asegura capacidad militar."),
        ("{F} Pedro afirma: «Pericles inventó la democracia en 429 a. C.». Usa las fechas de la ficha para corregirlo.", "Las reformas de Clístenes son de hacia 508 a. C., antes que Pericles, y 429 a. C. es cuando terminó su influencia", "La democracia se construyó en el tiempo."),
    ],
    ctx=("Un curso quiere organizar su centro de estudiantes imitando a Atenas: una asamblea donde votan todos y un grupo pequeño que prepara los temas. ¿Qué dos instituciones de la ficha imitan? {F}", "La Asamblea y el Consejo de los 500", "Una vota y la otra prepara los temas."),
    sc=[("¿Qué significa democracia?", "Gobierno donde el pueblo participa en las decisiones", "Viene de «pueblo» y «gobierno»."),
        ("¿Cómo se elegían los estrategos?", "Por votación", "Se necesitaba experiencia."),
        ("=", "{F} ¿Cuántos miembros tendría un consejo con 30 miembros por tribu y 10 tribus?", "30*10", "Se multiplican los miembros por las tribus.", " miembros")],
    op=("Dibuja un esquema de la democracia ateniense con las cuatro instituciones de la ficha, una flecha que muestre que el Consejo prepara los temas para la Asamblea y una frase sobre cómo se elegían los miembros de cada una. {F}",
        "Asamblea (todos los ciudadanos), Consejo (500 por sorteo), tribunales (jurados por sorteo) y estrategos (10 por votación).",
        ["incluye las cuatro instituciones", "muestra la flecha Consejo-Asamblea", "explica la forma de elección"], ["esquema dibujado"], ["decir que el Consejo decide", "confundir sorteo y votación"],
        "Pide que explique por qué Atenas usaba el sorteo en algunos cargos."),
    reinforce="Di en voz alta las cuatro instituciones y una tarea de cada una.",
    extend="Escribe una pregunta sobre cómo se hacía cumplir lo que votaba la Asamblea.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 2 (resumen hecho para este cuaderno; las cifras de votación y de pago son de ejemplo). "
     "Un ciudadano ateniense era un hombre adulto, hijo de padres atenienses. Podía hablar y votar en la Asamblea, ser jurado y ocupar cargos, muchos de ellos por sorteo. También debía hacer servicio militar. "
     "Pericles propuso pagar unas pocas monedas por día a los jurados, para que ciudadanos pobres pudieran participar sin perder su jornada de trabajo. "
     "Ostracismo: una vez al año se podía votar para desterrar por diez años a un ciudadano considerado peligroso; se escribía su nombre en un trozo de cerámica llamado ostrakon. "
     "Votación de ejemplo en la Asamblea: 4.200 votos a favor y 1.800 en contra. Pago de ejemplo: 2 monedas por día de juicio.")
build(
    OA, 2, F,
    use="Aprenderé a explicar cómo participaban los ciudadanos en Atenas. Sirve para entender qué significa democracia directa.",
    prior=["Sé qué instituciones tenía la democracia ateniense.", "Sé hacer sumas y restas de números hasta mil.", "Sé qué es una votación."],
    explain=[
        "En Atenas, un ciudadano era un hombre adulto, hijo de padres atenienses. Los ciudadanos participaban de manera directa: hablaban y votaban ellos mismos en la Asamblea, sin elegir representantes. A esto se le llama democracia directa.",
        "Participar exigía tiempo. Por eso Pericles propuso pagar a los jurados unas pocas monedas por día: así los ciudadanos pobres podían participar sin perder su jornada de trabajo. Muchos cargos se ocupaban por sorteo, y todos los ciudadanos debían hacer servicio militar.",
        "Otro mecanismo era el ostracismo: una vez al año se podía votar para desterrar por diez años a un ciudadano considerado peligroso para la ciudad, escribiendo su nombre en un trozo de cerámica. La participación tenía límites prácticos: quienes vivían lejos de la ciudad, o tenían mucho trabajo, no podían asistir tanto como quienes vivían cerca.",
    ],
    vocab=[("ciudadano", "persona con derecho a participar en las decisiones políticas"), ("democracia directa", "sistema en que los ciudadanos deciden ellos mismos, sin representantes"), ("ostracismo", "votación para desterrar por diez años a un ciudadano"), ("jurado", "ciudadano que juzga en un tribunal"), ("destierro", "obligación de vivir fuera de la ciudad")],
    worked=[
        ("Sumar votos", "{F} ¿Cuántos votos hubo en total?", ["Sumo los votos a favor y en contra.", "4.200 + 1.800 = 6.000."], "6.000 votos"),
        ("Calcular un pago", "{F} ¿Cuántas monedas gana un jurado que juzga 10 días?", ["Gana 2 monedas por día.", "10 × 2 = 20."], "20 monedas"),
    ],
    mistakes=[("Creer que todos los habitantes de Atenas votaban en la Asamblea.", "Se confunde habitante con ciudadano.", "Solo los ciudadanos, hombres adultos hijos de atenienses, votaban."),
              ("Pensar que la democracia directa significa que no había reglas.", "Se ignoran instituciones como el sorteo y los tribunales.", "Había instituciones y procedimientos para decidir.")],
    T=[
        ("{F} ¿Quién era ciudadano en Atenas?", "Un hombre adulto, hijo de padres atenienses", "La ficha lo define así."),
        ("{F} ¿Cómo se llama la votación para desterrar a un ciudadano, escribiendo su nombre en un trozo de cerámica?", "Ostracismo; el trozo de cerámica se llama ostrakon", "La ficha lo indica."),
        ("{F} ¿Por cuántos años se desterraba a un ciudadano por ostracismo?", "10 años", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos votos hubo en total en la votación de ejemplo?", "4200+1800", "Se suman los votos a favor y en contra.", " votos"),
        ("=", "{F} ¿Por cuántos votos ganó la propuesta?", "4200-1800", "Se resta la cifra menor a la mayor.", " votos"),
        ("{F} ¿Ganó la propuesta o la rechazaron? Explica.", "Ganó, porque tuvo más votos a favor", "4.200 es mayor que 1.800."),
        ("=", "{F} ¿Cuántas monedas gana un jurado que juzga 25 días?", "25*2", "Se multiplican los días por el pago diario.", " monedas"),
        ("{F} ¿Qué es la democracia directa?", "Un sistema en que los ciudadanos deciden ellos mismos, sin representantes", "En la Asamblea hablaban y votaban todos."),
        ("{F} ¿Por qué Pericles propuso pagar a los jurados?", "Para que los ciudadanos pobres pudieran participar sin perder su jornada de trabajo", "El pago compensaba el tiempo perdido."),
        ("{F} Carlos dice: «Todos los habitantes de Atenas votaban en la Asamblea». Corrígelo.", "Solo votaban los ciudadanos, que eran hombres adultos hijos de padres atenienses", "La ficha define quién era ciudadano."),
        ("{F} Un campesino vive a 40 km de la ciudad y debe cuidar sus campos. ¿Qué dificultad tiene para participar?", "Asistir a la Asamblea le toma tiempo y viaje, y puede perder trabajo", "La participación directa exige presencia."),
        ("{F} ¿Qué evidencia arqueológica conservada permite estudiar el ostracismo?", "Los ostraka, trozos de cerámica con nombres escritos", "Son los objetos usados para votar."),
        ("{F} Un compañero dice: «El ostracismo era un castigo por un delito». Corrígelo.", "Era una votación para desterrar por diez años a alguien considerado peligroso, no un castigo por un delito", "La ficha lo describe como una medida política."),
    ],
    ctx=("En un curso, todos los estudiantes votan alzando la mano si hacen una salida o no. ¿Con qué idea de la clase se parece y qué diferencia hay con Atenas? {F}", "Se parece a la democracia directa; en Atenas votaban solo los ciudadanos", "Votan ellos mismos, sin representantes."),
    sc=[("¿Qué es un ciudadano en Atenas?", "Un hombre adulto, hijo de padres atenienses", "Es la definición de la clase."),
        ("¿Qué es el ostracismo?", "Una votación para desterrar por diez años a un ciudadano", "Se escribía el nombre en un trozo de cerámica."),
        ("=", "{F} ¿Cuántos votos en total si hubo 3.000 a favor y 900 en contra?", "3000+900", "Se suman las dos cifras.", " votos")],
    op=("Escribe un guion de 6 líneas de una votación en la Asamblea de ejemplo: quién propone, quién habla, cómo se vota y quién gana, usando cifras. Agrega una línea que diga quién no puede participar. {F}",
        "Un ciudadano propone; otros hablan; se vota a mano alzada con 4.200 a favor y 1.800 en contra; gana la propuesta; no participan mujeres ni extranjeros.",
        ["incluye propuesta, discusión y votación", "usa cifras coherentes", "señala a quiénes excluye"], ["guion escrito"], ["olvidar que solo votan los ciudadanos", "cifras que no suman"],
        "Pide que explique qué cambiaría si votaran también las mujeres."),
    reinforce="Explica con tus palabras qué es democracia directa.",
    extend="Escribe una pregunta sobre cómo se decidía quién podía hablar en la Asamblea.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 3 (proporciones de ejemplo, no exactas; los especialistas discuten la población de Atenas). "
     "De cada 100 habitantes de Atenas: 10 eran ciudadanos varones adultos con derecho a votar; 45 eran mujeres y menores de familias ciudadanas; 15 eran metecos (extranjeros que vivían en Atenas) y sus familias; 30 eran personas esclavizadas. "
     "Las mujeres de familias ciudadanas no votaban ni ocupaban cargos; cuidaban la casa y participaban en ceremonias religiosas. "
     "Los metecos pagaban un impuesto especial y no podían votar. "
     "Las personas esclavizadas eran propiedad de otras y trabajaban en casas, talleres y minas.")
build(
    OA, 3, F,
    use="Aprenderé a reconocer quiénes quedaban excluidos de la democracia ateniense. Sirve para evaluar la participación sin idealizarla.",
    prior=["Sé qué era un ciudadano ateniense.", "Sé qué es la democracia directa.", "Sé usar proporciones simples."],
    explain=[
        "La democracia ateniense era limitada. Solo participaban los ciudadanos varones adultos. Quedaban excluidos: las mujeres, que no votaban ni ocupaban cargos; los metecos, extranjeros que vivían en Atenas y pagaban un impuesto especial; y las personas esclavizadas, que eran propiedad de otros y no tenían derechos políticos.",
        "Aunque no existen cifras exactas, los especialistas estiman que solo una pequeña parte de los habitantes era ciudadana con derecho a voto. En nuestro ejemplo, de cada 100 habitantes, 10 podían votar y 90 no. Es decir, la participación era amplia entre los ciudadanos, pero estrecha para el conjunto de la población.",
        "Las fuentes que conservamos las escribieron sobre todo hombres ciudadanos, por lo que sabemos menos sobre las mujeres, los metecos y las personas esclavizadas. Al estudiar Atenas conviene reconocer su aporte, la participación directa, sin ocultar que excluía a la mayoría de sus habitantes.",
    ],
    vocab=[("meteco", "extranjero que vivía en Atenas sin ser ciudadano"), ("exclusión", "dejar a alguien fuera de un derecho o de un grupo"), ("esclavizado", "persona que no es libre y es propiedad de otra"), ("derecho político", "posibilidad de votar y ocupar cargos"), ("estimación", "cálculo aproximado")],
    worked=[
        ("Calcular un grupo", "{F} De cada 100 habitantes, ¿cuántos pertenecían a familias ciudadanas (ciudadanos varones más mujeres y menores)?", ["Ciudadanos varones: 10. Mujeres y menores de familias ciudadanas: 45.", "Sumo: 10 + 45 = 55."], "55 habitantes"),
        ("Identificar un grupo excluido", "{F} ¿Por qué un meteco no podía votar?", ["Era un extranjero que vivía en Atenas.", "No era hijo de padres atenienses, así que no era ciudadano."], "Porque no era ciudadano"),
    ],
    mistakes=[("Decir que en Atenas «todos» participaban en las decisiones.", "Se olvida que los ciudadanos eran un grupo pequeño.", "Di «los ciudadanos» y nombra a quienes quedaban fuera."),
              ("Creer que solo importa la parte que votaba.", "Se mira la democracia sin la perspectiva de los excluidos.", "Nombra y considera a mujeres, metecos y personas esclavizadas.")],
    T=[
        ("{F} ¿Cuántos de cada 100 habitantes eran ciudadanos varones adultos?", "10", "La ficha lo indica."),
        ("{F} ¿Qué eran los metecos?", "Extranjeros que vivían en Atenas", "La ficha lo indica."),
        ("{F} ¿Qué pagaban los metecos?", "Un impuesto especial", "La ficha lo indica."),
        ("=", "{F} De cada 100 habitantes, ¿cuántos no podían votar?", "100-10", "Se resta la cantidad de ciudadanos al total.", " habitantes"),
        ("=", "{F} ¿Cuántos habitantes de cada 100 eran metecos o personas esclavizadas?", "15+30", "Se suman ambos grupos.", " habitantes"),
        ("{F} ¿Cuántas personas sin voto hay por cada ciudadano con voto? (Divide los que no votaban por los que votaban).", "9", "Son 90 sin voto por cada 10 con voto."),
        ("{F} Clasifica como ciudadano con voto (C) o sin voto (S): 1) una mujer ateniense; 2) un hombre adulto hijo de padres atenienses; 3) un meteco; 4) una persona esclavizada.", "1 S, 2 C, 3 S, 4 S", "Solo el hombre adulto hijo de atenienses era ciudadano."),
        ("{F} ¿Qué hacían las mujeres de familias ciudadanas según la ficha?", "Cuidaban la casa y participaban en ceremonias religiosas", "La ficha lo indica."),
        ("{F} Lucía dice: «En Atenas todos los habitantes eran ciudadanos». Corrígela con una cifra de la ficha.", "No: solo 10 de cada 100 eran ciudadanos varones adultos con voto", "La ficha da esa proporción."),
        ("{F} ¿Se puede decir que Atenas era democrática? Responde con matices.", "Sí para los ciudadanos, que decidían directamente, pero excluía a la mayoría de los habitantes", "La democracia era amplia entre ciudadanos y estrecha en el conjunto."),
        ("{F} ¿Por qué sabemos poco sobre la vida de las personas esclavizadas y de las mujeres?", "Porque las fuentes las escribieron sobre todo hombres ciudadanos", "Las fuentes reflejan su propia perspectiva."),
        ("{F} Un compañero dice: «Como los esclavizados no votaban, no importaban en la economía». Corrígelo.", "Trabajaban en casas, talleres y minas, así que eran importantes para la economía", "La ficha muestra su trabajo."),
        ("{F} Pedro dice: «Si hubo exclusiones, no se debe estudiar la democracia ateniense». ¿Qué responderías?", "Se estudia para entender sus aportes y también sus límites, sin idealizarla", "Un buen análisis considera ambos."),
    ],
    ctx=("Un afiche escolar dice: «En Atenas todos decidían». Usa la ficha para corregirlo con un dato. {F}", "Solo 10 de cada 100 habitantes eran ciudadanos varones adultos con derecho a voto", "El afiche omite a las mujeres, los metecos y las personas esclavizadas."),
    sc=[("¿Qué es un meteco?", "Un extranjero que vivía en Atenas sin ser ciudadano", "No podía votar."),
        ("¿Podían votar las mujeres atenienses?", "No", "Los ciudadanos eran solo varones."),
        ("=", "{F} Si hubiera 200 habitantes en la misma proporción, ¿cuántos serían ciudadanos con voto?", "200//100*10", "Se mantiene la proporción de 10 por cada 100.", " ciudadanos")],
    op=("Haz un gráfico de barras simple con los cuatro grupos de la ficha (por cada 100 habitantes). Escribe debajo una frase sobre quiénes participaban y otra sobre quiénes quedaban excluidos y por qué. {F}",
        "Barras de 10 (ciudadanos), 45 (mujeres y menores), 15 (metecos) y 30 (esclavizados); los excluidos no eran ciudadanos.",
        ["las barras respetan las cifras", "explica quién participaba", "explica quién estaba excluido y por qué"], ["gráfico dibujado", "frases escritas"], ["cambiar las cifras", "no mencionar exclusiones"],
        "Pide que explique qué sabemos y qué no sabemos de los grupos excluidos."),
    reinforce="Nombra los tres grupos excluidos de la ciudadanía ateniense.",
    extend="Escribe una pregunta sobre cómo vivía una persona esclavizada en Atenas y qué fuentes ayudarían.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 4 (resumen hecho para este cuaderno). "
     "Formas de gobierno: monarquía, gobierna un rey; oligarquía, gobiernan unos pocos ricos o poderosos; tiranía, una persona toma el poder, a veces con apoyo popular (Pisístrato gobernó Atenas en el siglo VI a. C.); democracia, los ciudadanos deciden. "
     "Esparta, otra ciudad-Estado griega: tenía dos reyes (cargo que se heredaba en dos familias), un Consejo de ancianos (Gerusía) de 28 ancianos de más de 60 años, 5 éforos (magistrados con mucho poder) y una asamblea. "
     "Los helotas, siervos que trabajaban la tierra, no eran ciudadanos.")
build(
    OA, 4, F,
    use="Aprenderé a comparar la democracia ateniense con otras formas de gobierno. Sirve para entender qué la hacía distinta.",
    prior=["Sé quiénes eran los ciudadanos de Atenas.", "Sé qué instituciones tenía Atenas.", "Sé comparar con un criterio."],
    explain=[
        "Las ciudades griegas tuvieron distintas formas de gobierno. En una monarquía gobierna un rey; en una oligarquía, unos pocos ricos o poderosos; en una tiranía, una persona toma el poder, a veces con apoyo popular, como Pisístrato en Atenas en el siglo VI a. C.; en una democracia deciden los ciudadanos.",
        "Esparta es un buen ejemplo para comparar. Tenía dos reyes, cargo que se heredaba en dos familias, un Consejo de 28 ancianos (la Gerusía), cinco éforos con mucho poder y una asamblea. Los helotas, que trabajaban la tierra, no eran ciudadanos. En Atenas, en cambio, los ciudadanos votaban directamente y muchos cargos se elegían por sorteo.",
        "Para comparar se eligen criterios: quién decide, cómo se eligen los cargos y quiénes participan. En ambas ciudades había exclusiones, pero el modo de decidir era distinto. Atenas no fue «mejor» ni «peor» en todo: fueron formas de organizar el poder, con ventajas y problemas, que hay que ubicar en su época.",
    ],
    vocab=[("monarquía", "gobierno de un rey"), ("oligarquía", "gobierno de unos pocos ricos o poderosos"), ("tiranía", "gobierno de una persona que toma el poder"), ("éforo", "magistrado espartano con mucho poder"), ("helota", "siervo espartano que trabajaba la tierra, sin ciudadanía")],
    worked=[
        ("Sumar miembros", "{F} ¿Cuántas personas había en la Gerusía si se cuentan los 28 ancianos y los 2 reyes?", ["Sumo los ancianos y los reyes.", "28 + 2 = 30."], "30 personas"),
        ("Clasificar un gobierno", "Un grupo de cinco familias ricas decide todo. ¿Qué forma de gobierno es?", ["Gobiernan unos pocos ricos.", "Eso es una oligarquía."], "Oligarquía"),
    ],
    mistakes=[("Pensar que toda ciudad griega era una democracia.", "Se generaliza a partir de Atenas.", "Esparta y otras ciudades tenían reyes, consejos de ancianos o gobiernos de pocos."),
              ("Creer que Esparta era una democracia solo porque tenía una asamblea.", "Se ignora quién tenía el poder real.", "Esparta tenía además dos reyes, éforos y un consejo de ancianos con mucho poder.")],
    T=[
        ("{F} ¿Cuántos reyes tenía Esparta?", "2", "La ficha lo indica."),
        ("{F} ¿Cuántos éforos había en Esparta?", "5", "La ficha lo indica."),
        ("{F} ¿Quién gobierna en una monarquía?", "Un rey", "Es su definición."),
        ("=", "{F} ¿Cuántas personas había en la Gerusía, contando los 28 ancianos y los 2 reyes?", "28+2", "Se suman ancianos y reyes.", " personas"),
        ("=", "{F} ¿Cuántos miembros más tenía el Consejo de Atenas, de 500 miembros, que la Gerusía de 30 personas?", "500-30", "Se resta la cifra menor a la mayor.", " miembros"),
        ("{F} Clasifica: 1) gobierna un rey; 2) unos pocos ricos deciden todo; 3) la Asamblea de ciudadanos vota las leyes.", "1 monarquía, 2 oligarquía, 3 democracia", "Cada descripción coincide con una forma de gobierno."),
        ("{F} ¿Qué forma de gobierno tenía Atenas?", "Democracia", "Los ciudadanos decidían directamente."),
        ("{F} ¿Quiénes eran los helotas?", "Siervos espartanos que trabajaban la tierra y no eran ciudadanos", "La ficha lo dice."),
        ("{F} ¿Qué diferencia hay entre la forma de elegir cargos en Atenas y la de los reyes espartanos?", "En Atenas muchos cargos se elegían por sorteo o votación; los reyes espartanos eran hereditarios", "Es una diferencia en la forma de acceder al poder."),
        ("{F} Pedro dice: «Esparta era una democracia porque tenía asamblea». Corrígelo.", "Esparta tenía además dos reyes, éforos y un consejo de ancianos con mucho poder", "La asamblea no era el único centro de decisión."),
        ("{F} ¿Por qué se dice que la tiranía de Pisístrato fue distinta de la oligarquía?", "Porque una sola persona tomó el poder, a diferencia de un grupo pequeño de ricos", "Se distingue por cuántos gobiernan."),
        ("{F} Una ciudad tiene tres familias ricas que eligen todos los cargos. ¿Qué forma de gobierno es?", "Oligarquía", "Gobiernan unos pocos ricos."),
        ("{F} Elige la frase correcta: A) Atenas y Esparta eran ciudades-Estado griegas con gobiernos distintos; B) Todas las ciudades griegas eran democracias.", "A) Atenas y Esparta eran ciudades-Estado griegas con gobiernos distintos", "La ficha muestra gobiernos diferentes."),
    ],
    ctx=("Una profesora propone que el curso decida una salida con una votación de todos, y otra propone que decidan solo tres estudiantes. ¿Cuál se parece a la democracia y cuál a la oligarquía? {F}", "La votación de todos se parece a la democracia; la de tres estudiantes, a la oligarquía", "Quién decide marca la diferencia."),
    sc=[("¿Qué es una oligarquía?", "Un gobierno de unos pocos ricos o poderosos", "Es el gobierno de unos pocos."),
        ("¿Qué es una tiranía?", "Un gobierno de una persona que toma el poder", "Puede contar con apoyo popular."),
        ("=", "{F} ¿Cuántas personas hay entre 2 reyes y 5 éforos?", "2+5", "Se suman ambos grupos.", " personas")],
    op=("Haz un cuadro comparativo entre Atenas y Esparta con tres criterios: quién decide, cómo se eligen los cargos y quiénes quedan excluidos. Escribe una frase final sobre qué tiene de particular la democracia ateniense. {F}",
        "Atenas: los ciudadanos deciden; cargos por sorteo y votación; excluye mujeres, metecos y esclavizados. Esparta: reyes, ancianos y éforos; los helotas no eran ciudadanos.",
        ["completa los tres criterios para ambas", "usa datos de la ficha", "la frase final es una comparación, no un juicio de valor"], ["cuadro escrito"], ["decir que una ciudad es mejor", "olvidar excluidos de Esparta"],
        "Pide que explique qué criterio le parece más importante para comparar."),
    reinforce="Define con tus palabras monarquía, oligarquía y democracia.",
    extend="Escribe una pregunta sobre qué ventajas y problemas tenía el gobierno de Esparta.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 5 (resumen hecho para este cuaderno). "
     "Chile hoy: pueden votar las personas desde los 18 años, sin diferencia entre hombres y mujeres; se eligen representantes (presidente o presidenta, parlamentarios, alcaldes y concejales) y la ciudadanía no vota cada ley. "
     "En Chile las mujeres votaron en elecciones municipales desde 1935 y, por una ley de 1949, en todas las elecciones. "
     "La esclavitud está prohibida en Chile desde 1823. "
     "Atenas, siglo V a. C.: votaban los ciudadanos varones adultos, directamente, en la Asamblea; muchos cargos se ocupaban por sorteo; había mujeres, metecos y personas esclavizadas sin derechos políticos.")
build(
    OA, 5, F,
    use="Aprenderé a evaluar semejanzas y diferencias entre la democracia ateniense y la democracia de hoy. Sirve para valorar el pasado sin copiarlo ni juzgarlo con ideas actuales.",
    prior=["Sé qué era la democracia directa en Atenas.", "Sé quiénes estaban excluidos.", "Sé qué es un criterio de comparación."],
    explain=[
        "Atenas y Chile hoy comparten ideas: que los ciudadanos participen en las decisiones, que se decida por votación y que la mayoría tenga un peso. Por eso se dice que la democracia ateniense es un antecedente de las democracias actuales. Pero no son iguales.",
        "Una diferencia clave es cómo se participa. En Atenas la democracia era directa: los ciudadanos votaban ellos mismos. En Chile hoy es representativa: se eligen representantes. Otra diferencia es quién participa: hoy votan las personas desde los 18 años, mujeres y hombres, y la esclavitud está prohibida; en Atenas, votaban solo los ciudadanos varones adultos.",
        "Para evaluar una comparación se eligen criterios (quién participa, cómo se decide, cómo se elige a las autoridades) y se evitan dos errores: llamar «democracia» a Atenas como si fuera igual a la actual, y celebrar su participación sin ver las exclusiones. También se evita juzgar la época solo con ideas de hoy: se explica su contexto y luego se evalúa.",
    ],
    vocab=[("democracia representativa", "sistema en que los ciudadanos eligen representantes para decidir"), ("antecedente", "hecho anterior que ayuda a entender uno posterior"), ("sufragio", "derecho a votar"), ("criterio", "aspecto con el que se compara"), ("anacronismo", "juzgar el pasado con ideas de hoy")],
    worked=[
        ("Calcular años", "{F} ¿Cuántos años pasaron entre el primer voto municipal de las mujeres chilenas y la ley que les permitió votar en todas las elecciones?", ["Fechas: 1935 y 1949.", "Resto: 1949 − 1935 = 14."], "14 años"),
        ("Clasificar una diferencia", "{F} ¿En qué se diferencia la forma de votar de Atenas y la de Chile?", ["Atenas: los ciudadanos votaban ellos mismos.", "Chile: se eligen representantes."], "Atenas era directa y Chile es representativa"),
    ],
    mistakes=[("Decir que Atenas era igual a una democracia actual.", "Se compara solo el nombre, sin los criterios.", "Compara quién participa y cómo se decide."),
              ("Celebrar la participación de Atenas sin mirar a quién excluía.", "Se mira solo una parte.", "Incluye a mujeres, metecos y personas esclavizadas en el análisis.")],
    T=[
        ("{F} ¿Desde qué edad pueden votar las personas en Chile hoy?", "18 años", "La ficha lo indica."),
        ("{F} ¿Cómo se llama el sistema en que se eligen representantes?", "Democracia representativa", "Es la definición de la clase."),
        ("{F} ¿Qué prohíbe la ley chilena desde 1823?", "La esclavitud", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la prohibición de la esclavitud en Chile y la ley que permitió votar a las mujeres en todas las elecciones?", "1949-1823", "Se restan los años.", " años"),
        ("{F} Clasifica como semejanza (S) o diferencia (D): 1) en ambas se decide por votación; 2) en Atenas votaban solo varones; 3) hoy se eligen representantes; 4) en ambas la mayoría tiene peso.", "1 S, 2 D, 3 D, 4 S", "Las semejanzas son ideas compartidas; las diferencias, formas distintas."),
        ("{F} ¿Qué significa que Atenas era una democracia directa y Chile una representativa?", "En Atenas los ciudadanos votaban ellos mismos; en Chile eligen representantes", "Es la diferencia en cómo se participa."),
        ("{F} Aplicando el criterio «quiénes pueden votar», ¿qué democracia incluye a más personas: Atenas del siglo V a. C. o Chile hoy?", "Chile hoy", "Allí votan mujeres y hombres desde los 18 años."),
        ("=", "{F} Una mujer chilena votó en elecciones municipales en 1935. ¿Cuántos años antes que la ley de 1949 fue eso?", "1949-1935", "Se restan los años.", " años"),
        ("{F} Ana dice: «Atenas era igual a la democracia de hoy». Corrígela con dos diferencias de la ficha.", "En Atenas la democracia era directa y excluía a mujeres, metecos y personas esclavizadas; hoy es representativa y vota toda persona desde los 18 años", "La ficha da ambas diferencias."),
        ("{F} Un compañero dice: «La democracia ateniense era perfecta porque todos participaban». ¿Qué error comete?", "Olvida que excluía a mujeres, metecos y personas esclavizadas", "La ficha muestra esas exclusiones."),
        ("{F} ¿Por qué estudiar Atenas sirve aunque su democracia haya sido distinta de la actual?", "Porque muestra el origen de ideas como participación y ciudadanía, y permite evaluar el presente", "Ayuda a comprender y comparar."),
        ("{F} Pedro dice: «Los atenienses eran injustos porque no dejaban votar a las mujeres». ¿Qué error de método hay?", "Juzga con ideas de hoy sin explicar el contexto; primero se explica la época y luego se evalúa", "Eso se llama anacronismo."),
        ("{F} Propón un criterio más para comparar Atenas con Chile hoy.", "Cómo se eligen las autoridades, o quién puede ser juez, o cómo se toman las decisiones sobre la guerra", "Hay criterios adicionales al voto."),
    ],
    ctx=("Un diario escolar titula «Atenas inventó la democracia que tenemos hoy». Con la ficha, ¿cómo corriges el título para hacerlo más preciso? {F}", "Atenas fue un antecedente de la democracia actual, pero su democracia era directa y excluía a muchos", "Hay semejanzas y diferencias importantes."),
    sc=[("¿Qué es una democracia representativa?", "Un sistema en que los ciudadanos eligen representantes para decidir", "Es la de Chile hoy."),
        ("¿Qué es un anacronismo?", "Juzgar el pasado con ideas de hoy", "Se evita explicando primero el contexto."),
        ("=", "{F} ¿Cuántos años pasaron entre 1823 y 1935?", "1935-1823", "Se restan los años.", " años")],
    op=("Escribe una comparación de 8 líneas entre Atenas y Chile hoy: dos semejanzas, dos diferencias y una evaluación final con un criterio. Cuida no usar ideas de hoy para juzgar sin explicar el contexto. {F}",
        "Semejanzas: votación y peso de la mayoría; diferencias: democracia directa y exclusiones; evaluación según quiénes pueden votar.",
        ["dos semejanzas y dos diferencias", "usa un criterio de evaluación", "explica el contexto antes de juzgar"], ["comparación escrita"], ["decir que son iguales", "juzgar con anacronismo"],
        "Pide que explique qué aprendió de las exclusiones de Atenas sobre derechos hoy."),
    reinforce="Menciona una semejanza y una diferencia entre Atenas y Chile hoy.",
    extend="Escribe una pregunta sobre cómo se amplió el derecho a voto en Chile durante el siglo XX.",
)
