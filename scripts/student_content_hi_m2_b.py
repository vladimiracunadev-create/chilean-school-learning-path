"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 09 (bienestar, consumo, derechos y tecnología en la Guerra Fría)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 09"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Dossier de ejemplo, años 1950 y 1960, Europa occidental y Estados Unidos: tras la Segunda Guerra Mundial la producción y los empleos crecieron; los gobiernos ampliaron la salud pública, la educación y las pensiones; Estados Unidos y la Unión Soviética (URSS) competían sin enfrentarse directamente en una guerra entre ambos."
build(
    OA, 1, F1,
    use="Aprenderé a situar el crecimiento económico y el Estado de Bienestar de la sociedad occidental dentro de la Guerra Fría, y a reconocer quiénes eran los actores. Sirve para explicar los cambios sociales de la segunda mitad del siglo XX sin buscar una sola causa.",
    prior=["Sé qué fue la Segunda Guerra Mundial.", "Sé leer una fuente con autor y fecha.", "Sé que una explicación histórica suele tener varias causas."],
    explain=[
        "La Guerra Fría fue la rivalidad entre dos bloques después de la Segunda Guerra Mundial: el bloque occidental, liderado por Estados Unidos, y el bloque oriental, liderado por la Unión Soviética (URSS). Se llama «fría» porque las dos potencias no se enfrentaron en una guerra directa, aunque compitieron en economía, ideas, armas y tecnología.",
        "En las sociedades occidentales hubo un fuerte crecimiento económico: aumentó lo que se producía, se crearon empleos y subieron los ingresos de muchas familias. Con esos recursos, varios gobiernos construyeron un Estado de Bienestar, es decir, un Estado que garantiza derechos sociales como la salud, la educación y las pensiones, y que se financia con impuestos.",
        "Los actores fueron los gobiernos, los sindicatos (organizaciones de trabajadores), las empresas y las familias. Cada uno tenía intereses distintos. Además, no todos los grupos se beneficiaron igual: algunos quedaron marginados, es decir, con menos acceso a derechos y oportunidades. Por eso conviene preguntar siempre quién ganó, quién quedó fuera y en qué lugar.",
    ],
    vocab=[("Guerra Fría", "rivalidad entre el bloque occidental y el oriental, sin guerra directa entre las dos potencias"), ("crecimiento económico", "aumento de lo que un país produce en un período"), ("Estado de Bienestar", "Estado que garantiza derechos sociales con recursos públicos"), ("derecho social", "derecho a servicios básicos como salud, educación o pensión"), ("marginado", "grupo con menos acceso a derechos y oportunidades")],
    worked=[
        ("Reconocer el Estado de Bienestar", "Un gobierno de ejemplo paga hospitales públicos, escuelas gratuitas y pensiones con los impuestos de la población y de las empresas. ¿Qué modelo es y qué lo financia?",
         ["Veo que el Estado entrega salud, educación y pensiones.", "Esos servicios son derechos sociales garantizados por el Estado.", "El texto dice que se pagan con impuestos."], "Es un Estado de Bienestar financiado con impuestos"),
        ("Corregir una idea sobre la Guerra Fría", "Un compañero dice: «La Guerra Fría fue una guerra con batallas entre Estados Unidos y la URSS». ¿Cómo lo corriges?",
         ["La palabra «fría» indica que no hubo guerra directa entre ambas.", "La rivalidad se dio en economía, ideas, armas y tecnología."], "Fue una rivalidad entre bloques sin guerra directa entre las dos potencias"),
    ],
    mistakes=[
        ("Creer que la Guerra Fría fue una guerra directa entre Estados Unidos y la URSS.", "Se confunde la rivalidad con enfrentamiento armado entre las dos potencias.", "Recuerda que la competencia fue económica, ideológica, militar y tecnológica, sin guerra directa entre ellas."),
        ("Pensar que el crecimiento económico benefició a todos por igual.", "Se olvidan los grupos marginados y las diferencias entre países y regiones.", "Pregunta siempre quién se benefició y quién quedó fuera."),
    ],
    T=[
        ("En Historia: ¿qué fue la Guerra Fría?", "Una rivalidad entre el bloque occidental y el oriental después de la Segunda Guerra Mundial, sin guerra directa entre las dos potencias", "Se definió por la competencia entre Estados Unidos y la URSS."),
        ("En Historia: ¿qué es el crecimiento económico?", "El aumento de lo que un país produce en un período", "Es el aumento de la producción de bienes y servicios."),
        ("{F} ¿Qué tres servicios dice el dossier que los gobiernos ampliaron?", "Salud pública, educación y pensiones", "El dossier los menciona de forma explícita."),
        ("En Historia: ¿qué es el Estado de Bienestar?", "Un modelo en que el Estado garantiza derechos sociales como salud, educación y pensiones", "Es la definición central de la clase."),
        ("Clasifica cada hecho como crecimiento económico o Estado de Bienestar: a) más fábricas producen más bienes; b) pensiones públicas pagadas con impuestos.", "a) crecimiento económico; b) Estado de Bienestar", "El aumento de la producción es crecimiento; la pensión pública es un derecho social garantizado."),
        ("{F} ¿Qué dos potencias competían, según el dossier? A) Estados Unidos y la URSS, B) Reino Unido y Francia, C) Alemania y Japón.", "A", "El dossier nombra a Estados Unidos y a la URSS."),
        ("Un gobierno de ejemplo decide pagar, con impuestos, un dinero temporal a quien pierde su trabajo. ¿Qué rasgo del Estado de Bienestar muestra? A) protección ante el desempleo con financiamiento público, B) control de la prensa, C) rebaja de todos los impuestos.", "A", "Garantiza un derecho social frente a un riesgo, con recursos públicos."),
        ("Clasifica estos actores como gobierno, trabajadores o empresas: un Ministerio de Salud de ejemplo; un sindicato de ejemplo; una fábrica de ejemplo.", "Ministerio: gobierno; sindicato: trabajadores; fábrica: empresas", "Cada uno representa un tipo distinto de actor."),
        ("=", "Un país de ejemplo recaudó 200 unidades en impuestos y destinó el 30 % a salud, educación y pensiones. ¿Cuántas unidades fueron?", "200*30//100", "El 30 % de 200 es el gasto social de ejemplo."),
        ("Una compañera dice: «El Estado de Bienestar apareció solo porque los gobiernos eran generosos». ¿Qué explicación agrega una causa económica? A) el crecimiento económico dio más recursos para cobrar impuestos y financiar servicios, B) la rivalidad con la URSS fue la única causa, C) los gobernantes eran personalmente más generosos que antes.", "A", "El crecimiento económico explica de dónde salían los recursos."),
        ("Explica por qué la frase «todo el bienestar social vino solo de la competencia con la URSS» es una explicación de una sola causa.", "Porque ignora otras causas, como el crecimiento económico y las demandas de sindicatos y ciudadanos", "Una explicación multicausal suma varias causas."),
        ("{F} Un lector concluye: «En todos los países del mundo se creó un Estado de Bienestar». ¿Qué límite de la evidencia señalas?", "El dossier solo habla de Europa occidental y Estados Unidos, no de todo el mundo", "La conclusión generaliza más allá del lugar de la fuente."),
        ("Evalúa: «Si hubo crecimiento económico, todos los grupos mejoraron por igual». A) es correcta, B) es excesiva porque algunos grupos marginados se beneficiaron menos, C) es correcta porque el Estado lo aseguraba.", "B", "El crecimiento no garantiza el mismo acceso para todos los grupos."),
    ],
    ctx=("{F} Un museo de ejemplo prepara un cartel sobre este período. ¿Cuál es el más ajustado al dossier? A) «Tras la guerra creció la producción y varios gobiernos ampliaron salud, educación y pensiones», B) «Tras la guerra todo el mundo vivió igual de bien», C) «Los gobiernos dejaron de intervenir en salud y educación».", "A", "Es la única frase que respeta lo que dice el dossier."),
    sc=[("En Historia: ¿qué es un derecho social?", "El derecho a servicios básicos como salud, educación o pensión", "Es la base del Estado de Bienestar."),
        ("¿Qué significa que un grupo estuvo marginado en este período?", "Que tuvo menos acceso a derechos y oportunidades", "Marginado indica menor acceso."),
        ("¿La Guerra Fría fue una guerra directa entre Estados Unidos y la URSS? Responde sí o no y por qué.", "No, porque fue una rivalidad sin guerra directa entre ellas", "Por eso se llama fría.")],
    op=("Imagina que debes explicar a un compañero por qué creció el Estado de Bienestar en Occidente. Escribe cuatro líneas con: dos causas distintas (por ejemplo, crecimiento económico y presión de los sindicatos), un grupo que quedó marginado y una pregunta que no puedes responder solo con el dossier de la clase.",
        "El Estado de Bienestar creció porque había crecimiento económico para financiarlo y porque los sindicatos pedían derechos. Algunos grupos marginados se beneficiaron menos. Una pregunta pendiente: ¿cómo fue en otros continentes?",
        ["da dos causas distintas", "nombra un grupo marginado", "formula una pregunta pendiente"], ["texto breve de cuatro líneas"], ["explicar con una sola causa", "decir que todos se beneficiaron igual"], "Pide a una persona de tu casa que marque en tu texto las dos causas."),
    reinforce="Haz una tabla de tres columnas con actores (gobierno, sindicatos, empresas) y escribe qué quería cada uno.",
    extend="Escribe dos frases que expliquen por qué la rivalidad entre bloques pudo influir en la creación de servicios sociales.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (aviso publicitario de ejemplo, años 1950, Estados Unidos): «¡Su familia merece una lavadora nueva! Pague en cuotas mensuales.» Fuente B (encuesta de ejemplo en una ciudad de ejemplo): en 1950, 10 de cada 100 hogares tenían televisor; en 1965, 85 de cada 100. Fuente C (carta de ejemplo de una dueña de casa a un diario): «La lavadora me da tiempo, pero las cuotas me preocupan.» Fuente D (historiador actual, texto de ejemplo): «El crédito y la publicidad hicieron del consumo un rasgo central de la vida cotidiana.»"
build(
    OA, 2, F2,
    use="Aprenderé a interrogar fuentes sobre el consumo y los medios de comunicación de masas preguntando quién las produjo, para qué y qué no dicen. Sirve para no tomar un aviso o una carta como prueba de lo que vivió toda una sociedad.",
    prior=["Sé qué fue el crecimiento económico de posguerra.", "Distingo fuente primaria y secundaria.", "Sé que una fuente tiene autor, fecha e intención."],
    explain=[
        "Con el crecimiento económico, más familias occidentales pudieron comprar bienes como electrodomésticos, autos y televisores. A ese fenómeno se le llama consumo masivo. Ayudaron la producción en serie, que abarata los productos, los mayores ingresos y el crédito, que permite comprar ahora y pagar después en cuotas.",
        "Al mismo tiempo se expandieron los medios de comunicación de masas: la prensa, la radio y la televisión, que llegan a millones de personas con noticias, entretenimiento y publicidad. La publicidad busca vender productos. La propaganda, en cambio, busca convencer sobre ideas o posiciones políticas, y fue muy usada por ambos bloques en la Guerra Fría.",
        "Al leer fuentes sobre el consumo hay que contextualizarlas. Un aviso lo hace una empresa para vender y no mide cuánto se compró. Una encuesta cuenta hogares, pero no dice qué opinaban. Una carta muestra una voz individual y no representa a todos. Un libro actual interpreta con distancia. Una fuente primaria es la que nace en el tiempo estudiado (el aviso, la encuesta, la carta); una secundaria la escribe después alguien que interpreta (el historiador). Cada fuente tiene límites.",
    ],
    vocab=[("consumo masivo", "compra de bienes por una gran parte de la población"), ("crédito", "forma de comprar ahora y pagar después, por ejemplo en cuotas"), ("medios de comunicación de masas", "prensa, radio y televisión, que llegan a millones de personas"), ("publicidad", "mensaje que busca vender un producto"), ("propaganda", "mensaje que busca convencer sobre ideas o posiciones políticas"), ("fuente primaria y secundaria", "primaria: nace en el tiempo estudiado; secundaria: la escribe después quien interpreta")],
    worked=[
        ("Reconocer la intención", "Un aviso de ejemplo dice «Compre hoy su refrigerador y pague en seis cuotas». ¿Quién lo produce y qué intención tiene?",
         ["Los avisos los paga una empresa o una tienda.", "Su propósito es lograr que la gente compre.", "Por eso es publicidad, no un registro de cuántos compraron."], "Lo produce una empresa para vender; es publicidad"),
        ("Señalar un límite", "Una encuesta de ejemplo muestra que 40 de cada 100 hogares tenían radio. ¿Qué no puede decir sobre la vida cotidiana?",
         ["La encuesta cuenta hogares con radio.", "No dice qué escuchaban ni qué opinaban las personas."], "No dice qué escuchaban ni qué opinaban las personas"),
    ],
    mistakes=[
        ("Tomar un aviso publicitario como prueba de lo que compraba toda la gente.", "El aviso quiere vender; no mide compras reales.", "Contrástalo con datos como una encuesta."),
        ("Usar una sola carta para hablar de todas las familias.", "Una voz individual no representa a toda una sociedad.", "Úsala como ejemplo y busca más voces."),
    ],
    T=[
        ("En Historia: ¿qué es el crédito?", "Una forma de comprar ahora y pagar después, por ejemplo en cuotas", "Permite comprar sin pagar todo al contado."),
        ("En Historia: ¿qué son los medios de comunicación de masas?", "La prensa, la radio y la televisión, que llegan a millones de personas", "Se llaman de masas por su alcance."),
        ("{F} ¿Qué intención tiene la Fuente A?", "Que las personas compren lavadoras", "Es un aviso publicitario."),
        ("{F} ¿La Fuente D es primaria o secundaria?", "Secundaria", "La escribe un historiador actual que interpreta."),
        ("{F} ¿Qué dato entrega la Fuente B sobre la televisión?", "Que pasó de 10 de cada 100 hogares en 1950 a 85 de cada 100 en 1965", "La encuesta cuantifica hogares con televisor."),
        ("En Historia: ¿en qué se diferencian publicidad y propaganda?", "La publicidad busca vender productos y la propaganda busca convencer sobre ideas o posiciones políticas", "Cambia el propósito del mensaje."),
        ("=", "{F} ¿Cuántos hogares más de cada 100 tenían televisor en 1965 que en 1950, según la Fuente B?", "85-10", "Se resta el valor inicial al final."),
        ("{F} ¿Qué se puede saber con la Fuente C que no se sabe con la Fuente B? A) cómo vivió una persona el consumo, con una ventaja y una preocupación, B) cuántos hogares tenían televisor, C) qué interpreta hoy un historiador.", "A", "La carta da una voz individual; la encuesta, números."),
        ("{F} ¿Por qué la Fuente A no basta para saber cuántas familias compraron lavadora?", "Porque es un aviso para vender y no mide las compras", "Su fin es persuadir, no contar."),
        ("{F} Una compañera concluye con la Fuente C: «Todas las familias se endeudaban en cuotas». ¿Qué error comete?", "Generaliza desde una sola carta, que es una voz individual", "Una carta no representa a todos."),
        ("{F} ¿Qué conclusión es proporcional a la evidencia? A) en la ciudad de ejemplo la tenencia de televisor pasó de 10 a 85 hogares de cada 100 entre 1950 y 1965, B) en todo el mundo había televisor en 1965, C) la televisión hizo que todas las familias compraran lavadora.", "A", "Solo A se limita a lo que dice la encuesta."),
        ("{F} Para sostener que «la publicidad ofrecía pagar en cuotas y los historiadores la ven como motor del consumo», ¿qué fuentes combinas? A) la A y la D, B) la B y la C, C) la A y la B.", "A", "El aviso ofrece cuotas y el historiador interpreta."),
        ("{F} ¿Qué pregunta no responde ninguna fuente de la ficha? A) cuántos hogares tenían televisor en 1965, B) qué familias no pudieron comprar electrodomésticos ni televisor, C) qué ofrecía el aviso.", "B", "Las fuentes no identifican a las familias que quedaron fuera."),
    ],
    ctx=("{F} Un estudiante afirma: «Los avisos de la época prueban que todas las familias compraban a crédito». ¿Qué problema de contexto tiene esa conclusión?", "El aviso lo hace una empresa para vender y no prueba cuántas familias compraron", "Se confunde la intención publicitaria con evidencia de compras."),
    sc=[("En Historia: ¿qué es el consumo masivo?", "La compra de bienes por una gran parte de la población", "Lo hizo posible el aumento de ingresos y el crédito."),
        ("Nombra un límite de una encuesta como fuente.", "No dice qué opinaban las personas ni sus razones", "Solo cuenta hogares."),
        ("¿Quién produce un aviso publicitario y para qué?", "Una empresa, para vender un producto", "Procedencia e intención.")],
    op=("Con las Fuentes A, B y C de la ficha, escribe un párrafo de cuatro líneas que responda: «¿Cómo cambió el consumo en la ciudad de ejemplo?». Indica qué fuente aporta datos, cuál aporta una voz personal y un límite de cada una.",
        "La Fuente B muestra que los televisores pasaron de 10 a 85 hogares de cada 100. La Fuente C aporta una voz personal que valora el tiempo ganado y teme las cuotas. Límite de B: no dice opiniones; límite de C: es una sola persona.",
        ["usa al menos dos fuentes", "distingue datos y voz personal", "anota un límite por fuente"], ["párrafo de cuatro líneas"], ["generalizar desde una carta", "tomar el aviso como dato de compras"], "Pide a una persona de tu casa que lea tu párrafo y señale el límite que anotaste."),
    reinforce="Haz una tabla con las Fuentes A, B, C y D: autor, intención y límite.",
    extend="Escribe qué otra fuente (por ejemplo, un registro de ventas de una tienda) ayudaría a saber cuántas lavadoras se compraron.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo, Estados Unidos, décadas de 1950 y 1960. Situación: en varios estados las personas afroamericanas sufrían segregación racial, es decir, separación obligatoria en escuelas, buses y lugares públicos. Un movimiento por los derechos civiles organizó marchas pacíficas y boicots, con líderes como Martin Luther King Jr. En 1964 se aprobó una ley nacional que prohibió la discriminación. En esos años también pedían igualdad las mujeres y los jóvenes cuestionaban normas tradicionales. Voz de un gobernador de ejemplo: «Cada estado debe decidir sus propias leyes.» Voz de una activista de ejemplo: «Un derecho no puede depender del estado donde se vive.»"
build(
    OA, 3, F3,
    use="Aprenderé a comparar perspectivas y escalas en la ampliación de los derechos civiles de grupos marginados durante la Guerra Fría. Sirve para entender que un cambio de derechos tiene a quienes lo piden, a quienes lo frenan y a quienes lo deciden.",
    prior=["Sé qué es el Estado de Bienestar.", "Sé qué es una fuente con procedencia.", "Sé que la Guerra Fría fue una rivalidad entre bloques."],
    explain=[
        "Los derechos civiles son los derechos que protegen a las personas frente a la discriminación y garantizan igualdad ante la ley, por ejemplo votar, estudiar o usar lugares públicos. Durante la Guerra Fría, grupos marginados de la sociedad occidental, como la población afroamericana en Estados Unidos y las mujeres, ampliaron sus derechos mediante movimientos sociales y cambios de leyes.",
        "Hay que comparar perspectivas, es decir, los puntos de vista de cada actor. Los activistas pedían igualdad. Algunas autoridades locales defendían las normas existentes con el argumento de que cada estado decidía. El gobierno nacional podía intervenir con leyes. Ninguna perspectiva es neutral: cada una muestra intereses y valores.",
        "También hay que comparar escalas. En la escala local, el conflicto estaba en un bus o una escuela; en la escala nacional, se discutía una ley para todo el país; en la escala internacional, el bloque oriental criticaba la segregación, también como parte de su rivalidad con Estados Unidos, y Estados Unidos quería mostrar una democracia con derechos. Mirar varias escalas evita explicar el cambio con una sola causa.",
    ],
    vocab=[("derechos civiles", "derechos que protegen frente a la discriminación y aseguran igualdad ante la ley"), ("segregación racial", "separación obligatoria de personas por su origen en lugares públicos"), ("movimiento social", "grupo organizado que exige cambios"), ("boicot", "negarse en grupo a comprar o usar algo para presionar por un cambio"), ("perspectiva", "punto de vista de un actor según sus intereses y valores"), ("escala", "nivel de observación: local, nacional o internacional")],
    worked=[
        ("Comparar perspectivas", "Una activista pide un derecho igual en todos los estados y un gobernador de ejemplo dice que cada estado decide. ¿En qué se diferencian sus perspectivas?",
         ["La activista habla de un derecho que no depende del lugar.", "El gobernador defiende que cada estado fije sus leyes.", "Uno busca igualdad nacional; el otro, decisión local."], "Una busca igualdad nacional y el otro defiende la decisión de cada estado"),
        ("Distinguir escalas", "Un joven boicotea un bus local; el Congreso aprueba una ley; otro país critica la segregación. ¿A qué escala corresponde cada hecho?",
         ["El bus es un hecho de lugar: local.", "El Congreso decide para todo el país: nacional.", "Otro país opina desde fuera: internacional."], "Local, nacional e internacional, en ese orden"),
    ],
    mistakes=[
        ("Explicar la ampliación de derechos solo por una ley.", "La ley llegó después de años de organización y protesta.", "Incluye siempre a los movimientos sociales y al contexto."),
        ("Creer que los actores que frenaban el cambio no tenían argumentos.", "Tenían razones, aunque se discutan: por ejemplo, el poder de cada estado.", "Describe su argumento y luego evalúalo con evidencia."),
    ],
    T=[
        ("En Historia: ¿qué son los derechos civiles?", "Derechos que protegen frente a la discriminación y aseguran igualdad ante la ley", "Es la definición básica."),
        ("{F} ¿Qué es la segregación racial según el cuadro?", "La separación obligatoria en escuelas, buses y lugares públicos", "El cuadro la define de modo explícito."),
        ("En Historia: ¿qué es un movimiento social?", "Un grupo organizado que exige cambios", "Los movimientos actúan para transformar normas o leyes."),
        ("{F} ¿Qué dos formas de acción usó el movimiento por los derechos civiles, según el cuadro?", "Marchas pacíficas y boicots", "El cuadro las menciona."),
        ("{F} ¿Qué perspectiva defiende el gobernador de ejemplo? A) que cada estado decida sus leyes, B) que haya una ley igual para todo el país, C) que se terminen los derechos civiles en todo el país.", "A", "Su voz lo dice textualmente."),
        ("Clasifica por escala: a) un grupo de estudiantes de ejemplo ocupa pacíficamente una cafetería; b) el Congreso vota una ley; c) un gobierno extranjero critica la segregación.", "a) local; b) nacional; c) internacional", "Cada hecho ocurre en un nivel distinto."),
        ("=", "En una escuela de ejemplo había 240 estudiantes y 96 pertenecían a un grupo que antes no podía entrar. ¿Qué porcentaje del total eran?", "96*100//240", "Se divide la parte por el total y se multiplica por 100."),
        ("Una activista de ejemplo dice: «Un derecho no puede depender del estado donde se vive». ¿Qué escala de problema plantea? A) nacional, B) solo local, C) solo internacional.", "A", "Pide un derecho igual en todo el país."),
        ("Compara: ¿qué quería la activista y qué defendía el gobernador de ejemplo?", "La activista, igualdad de derechos en todo el país; el gobernador, que cada estado decidiera", "Son perspectivas opuestas sobre quién decide."),
        ("Explica por qué decir «la ley de 1964 explica sola el cambio» es una explicación de una sola causa.", "Porque deja fuera las marchas, los boicots y la presión de la opinión pública que antecedieron a la ley", "El cambio tuvo varias causas y actores."),
        ("{F} Una lectora dice: «El cuadro prueba que en todo el mundo se ampliaron los derechos civiles». ¿Qué corrección haces?", "El cuadro solo trata de Estados Unidos; para el mundo hacen falta otras fuentes", "La conclusión excede el lugar de la fuente."),
        ("Evalúa: «El bloque oriental criticaba la segregación solo por preocupación sincera por los derechos». A) es cierta sin dudas, B) es excesiva porque también competía con Estados Unidos y buscaba ventaja política, C) es falsa porque no la criticó nunca.", "B", "En la Guerra Fría las críticas también tenían intención política."),
        ("Elige la conclusión más proporcional. A) en las décadas de 1950 y 1960, en Estados Unidos, movimientos sociales y una ley nacional ampliaron derechos civiles de grupos marginados, B) la segregación terminó el mismo día en todo el mundo, C) los derechos civiles fueron concedidos sin que nadie los pidiera.", "A", "A se limita a lugar, tiempo y actores del cuadro."),
    ],
    ctx=("{F} Para una exposición, un grupo escribe «Los derechos se ampliaron porque el gobierno lo decidió». Usando el cuadro, ¿qué actores faltan en esa frase?", "Los movimientos sociales y los grupos marginados que organizaron marchas y boicots", "El cuadro muestra que el cambio vino de la presión organizada."),
    sc=[("En Historia: ¿qué es una perspectiva?", "El punto de vista de un actor según sus intereses y valores", "Ayuda a comparar voces."),
        ("Nombra las tres escalas que usamos para comparar.", "Local, nacional e internacional", "Es la clasificación de la clase."),
        ("¿Qué dos acciones usaban los movimientos por derechos civiles en el cuadro?", "Marchas pacíficas y boicots", "Son las acciones nombradas en el cuadro.")],
    op=("Imagina un debate escolar sobre una ley que prohíbe la discriminación en las escuelas de un país de ejemplo. Escribe seis líneas con: lo que diría un movimiento social, lo que diría una autoridad local que se opone, una razón a escala nacional y una a escala internacional.",
        "El movimiento diría que todos deben estudiar juntos. La autoridad local diría que cada estado decide. A escala nacional, una ley evita que los derechos cambien según el lugar. A escala internacional, el país proyecta una imagen democrática.",
        ["incluye dos perspectivas opuestas", "usa escala nacional e internacional", "argumenta con una razón por cada una"], ["texto de seis líneas"], ["describir solo una perspectiva", "mezclar escalas"], "Pide a una persona de tu casa que marque en tu texto la razón nacional y la internacional."),
    reinforce="Dibuja un cuadro de tres filas (local, nacional, internacional) y escribe un hecho del cuadro de la clase en cada una.",
    extend="Escribe una frase sobre otro grupo, además de los citados, que ampliara sus derechos en esa época y qué fuente necesitarías para comprobarlo.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Cuadro de ejemplo. 1957: la URSS lanza al espacio el satélite Sputnik. 1969: la misión estadounidense Apolo 11 llega a la Luna. En esas décadas, los dos bloques invirtieron en ciencia militar y espacial; se difundieron la televisión, los computadores de gran tamaño en universidades y empresas, y los programas de vacunación. Aun así, en muchos hogares de ejemplo no había televisor ni acceso a servicios de salud cercanos."
build(
    OA, 4, F4,
    use="Aprenderé a relacionar las causas del desarrollo tecnológico en la Guerra Fría con sus cambios y continuidades en la vida cotidiana. Sirve para explicar un proceso con varias causas y reconocer qué cambió y qué siguió igual.",
    prior=["Sé qué fue la Guerra Fría y qué es el crecimiento económico.", "Distingo cambio y continuidad.", "Sé que un hecho puede tener varias causas."],
    explain=[
        "La tecnología es la aplicación del conocimiento científico para crear herramientas y procesos. En la Guerra Fría hubo un gran desarrollo tecnológico. Una causa fue la competencia entre bloques: la carrera armamentista (competir por tener más y mejores armas) y la carrera espacial, con hitos como el Sputnik en 1957 y la llegada a la Luna en 1969.",
        "Pero no fue la única causa. El crecimiento económico dio recursos; las universidades y los centros de investigación formaron científicos; las empresas vieron mercado en nuevos productos. Además, parte de lo desarrollado para fines militares o espaciales tuvo usos civiles, como las comunicaciones por satélite. Por eso hablamos de multicausalidad: varias causas actúan juntas.",
        "También hay cambios y continuidades. Cambiaron las comunicaciones, el transporte y la salud para muchas personas. Se mantuvieron desigualdades: no todos los hogares ni países tuvieron el mismo acceso. Y apareció un riesgo nuevo, el miedo a una guerra con armas nucleares. Una buena explicación nombra causas, cambios, continuidades y límites.",
    ],
    vocab=[("tecnología", "aplicación del conocimiento científico para crear herramientas y procesos"), ("carrera armamentista", "competencia por tener más y mejores armas"), ("carrera espacial", "competencia entre potencias por logros en el espacio"), ("multicausalidad", "explicación en que varias causas actúan juntas"), ("uso civil", "uso para la vida cotidiana, no para la guerra")],
    worked=[
        ("Separar causas", "Para explicar el desarrollo de satélites en la Guerra Fría, un estudiante anota: competencia entre bloques, fondos del Estado, universidades. ¿Es una explicación de una o de varias causas?",
         ["Anota tres factores distintos.", "Los tres actúan juntos: rivalidad, dinero e investigación."], "De varias causas: es multicausal"),
        ("Cambio y continuidad", "En una ciudad de ejemplo llegaron las vacunas masivas, pero en una aldea de ejemplo no había médico cercano. ¿Qué cambió y qué continuó?",
         ["La llegada de vacunas en la ciudad es un cambio.", "La falta de acceso en la aldea es una continuidad de desigualdad."], "Cambio: vacunas masivas; continuidad: desigualdad de acceso"),
    ],
    mistakes=[
        ("Explicar la carrera espacial solo por la rivalidad entre bloques.", "Se ignoran la economía, las universidades y las empresas.", "Anota al menos tres causas de tipos distintos."),
        ("Pensar que la tecnología llegó a todos al mismo tiempo.", "El acceso dependía del lugar, de los ingresos y de las políticas.", "Pregunta quién accedió y quién no."),
    ],
    T=[
        ("En Historia: ¿qué es la tecnología?", "La aplicación del conocimiento científico para crear herramientas y procesos", "Es la definición de la clase."),
        ("En Historia: ¿qué fue la carrera espacial?", "Una competencia entre potencias por logros en el espacio", "Fue parte de la Guerra Fría."),
        ("{F} ¿Qué logro de la URSS menciona el cuadro?", "El lanzamiento del satélite Sputnik en 1957", "El cuadro lo indica."),
        ("{F} ¿Qué logro de Estados Unidos aparece y en qué año? A) la llegada a la Luna con Apolo 11 en 1969, B) el lanzamiento del Sputnik en 1957, C) la llegada a la Luna con Apolo 11 en 1957.", "A", "El cuadro lo asocia a 1969."),
        ("En Historia: ¿qué es un uso civil de una tecnología?", "Un uso para la vida cotidiana y no para la guerra", "Contrasta con el uso militar."),
        ("Clasifica como cambio o continuidad: a) se difunden los programas de vacunación; b) algunos hogares siguen sin acceso a salud cercana.", "a) cambio; b) continuidad", "La difusión es una novedad; la falta de acceso se mantiene."),
        ("Un estudiante dice que los satélites de comunicación nacieron solo de la competencia espacial. ¿Qué causa económica puedes sumar? A) los recursos que dio el crecimiento económico para investigar, B) que la competencia entre bloques fue la única causa, C) que la desigualdad de acceso a la televisión los creó.", "A", "Sin recursos no habría investigación ni lanzamientos."),
        ("Ordena de causa a consecuencia: a) los Estados invierten en ciencia; b) la rivalidad entre bloques crece; c) se difunden nuevos productos para el hogar.", "b, a, c", "La rivalidad impulsa la inversión y esta, nuevos productos."),
        ("{F} Elige la mejor explicación del desarrollo tecnológico. A) la competencia entre bloques, el crecimiento económico y la investigación en universidades actuaron juntos, B) solo hubo una causa: la carrera espacial, C) el desarrollo se debió únicamente a que las empresas vieron un mercado.", "A", "La explicación multicausal reúne varios factores."),
        ("Explica por qué es un límite afirmar que «la tecnología mejoró la vida de toda la población» usando el cuadro.", "Porque el cuadro dice que muchos hogares no tenían televisor ni salud cercana", "El cuadro muestra desigualdad de acceso."),
        ("=", "En una ciudad de ejemplo vivían 5.000 hogares y 3.500 tenían televisor. ¿Cuántos hogares no lo tenían?", "5000-3500", "Se resta los hogares con televisor del total."),
        ("Evalúa: «Como se llegó a la Luna en 1969, todo el mundo tenía acceso a la tecnología». A) es correcta, B) es excesiva porque un logro espacial no significa acceso general, C) es correcta porque el Estado lo aseguró.", "B", "Un hito no prueba el acceso de todos."),
        ("Redacta una frase con dos causas del desarrollo tecnológico en la Guerra Fría y un límite.", "Por ejemplo: la competencia entre bloques y los fondos del crecimiento económico impulsaron la tecnología, pero no todos los hogares tuvieron acceso", "Incluye dos causas y una limitación."),
    ],
    ctx=("{F} Un diario escolar titula «La Guerra Fría solo trajo miedo y armas». Usando el cuadro, ¿qué evidencia contradice el «solo»?", "Los usos civiles, como la difusión de la televisión y los programas de vacunación", "El cuadro muestra beneficios cotidianos además del riesgo."),
    sc=[("En Historia: ¿qué es la multicausalidad?", "Una explicación en que varias causas actúan juntas", "Evita atribuir todo a una causa."),
        ("En Historia: ¿qué es la carrera armamentista?", "La competencia por tener más y mejores armas", "Fue otra forma de rivalidad."),
        ("Nombra una continuidad señalada en el cuadro.", "La desigualdad de acceso a televisor y a servicios de salud", "Muchos hogares quedaron sin acceso.")],
    op=("Escribe un párrafo de cinco líneas sobre el siguiente problema: «¿Por qué se desarrolló tanta tecnología durante la Guerra Fría?». Incluye dos causas distintas, un cambio, una continuidad y un límite de las fuentes.",
        "La competencia entre bloques y los fondos del crecimiento económico explican parte del desarrollo. Cambió el acceso a comunicaciones y vacunas. Continuó la desigualdad en muchos hogares. Los datos del cuadro son de ejemplo y no cubren todo el mundo.",
        ["da dos causas distintas", "incluye cambio y continuidad", "anota un límite"], ["párrafo de cinco líneas"], ["usar una sola causa", "olvidar la desigualdad"], "Pide a una persona de tu casa que marque en tu texto el cambio y la continuidad."),
    reinforce="Haz una tabla con las columnas causa, cambio, continuidad y completa una fila con el cuadro de la clase.",
    extend="Escribe una frase que explique un uso civil de una tecnología creada para la guerra.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = "Datos de ejemplo de una ciudad de ejemplo, 1950 y 1970. Hogares con televisor: 10 de cada 100 en 1950 y 85 de cada 100 en 1970. Hogares con acceso a pensiones públicas: 20 de cada 100 en 1950 y 70 de cada 100 en 1970. Mujeres con trabajo remunerado: 25 de cada 100 en 1950 y 35 de cada 100 en 1970. Hogares sin agua potable: 30 de cada 100 en 1950 y 12 de cada 100 en 1970. Nota: los datos no incluyen a las zonas rurales de la región."
build(
    OA, 5, F5,
    use="Aprenderé a construir una interpretación documentada sobre cuánto cambió la vida cotidiana en Occidente durante la Guerra Fría. Sirve para escribir una tesis con evidencias, un límite y una pregunta pendiente.",
    prior=["Conozco el Estado de Bienestar, el consumo, los derechos civiles y la tecnología de la época.", "Sé contextualizar fuentes.", "Sé distinguir cambio y continuidad."],
    explain=[
        "Una interpretación documentada responde a una pregunta histórica con una tesis, es decir, una afirmación que se puede defender, y la sostiene con evidencias de las fuentes. No basta con contar hechos: hay que explicar qué significan. Una buena estructura es: tesis, dos o tres evidencias, un límite y una pregunta que quedó abierta.",
        "Para escribir sin exagerar, se usan palabras de grado como «mayormente», «en la ciudad de ejemplo» o «entre 1950 y 1970». También se incluye un contraargumento, que es una razón que podría debilitar la tesis, y se responde con otra evidencia. Así se muestra que la conclusión es proporcional a lo que se sabe.",
        "En este tema una tesis útil puede decir que la vida cotidiana cambió mucho en bienestar, consumo, derechos y tecnología, pero que hubo grupos y lugares que se beneficiaron menos. Cada dato que mide un cambio, como los hogares con televisor, es un indicador. Revisa siempre la procedencia de los datos, el lugar al que se refieren y qué grupos no aparecen en ellos.",
    ],
    vocab=[("tesis", "afirmación que se defiende con evidencias"), ("evidencia", "dato o cita de una fuente que apoya una afirmación"), ("contraargumento", "razón que podría debilitar la tesis"), ("conclusión proporcional", "conclusión que no afirma más de lo que prueba la evidencia"), ("pregunta abierta", "pregunta que las fuentes dadas no permiten responder")],
    worked=[
        ("Construir una tesis", "Con los datos de ejemplo sobre televisores y pensiones, escribe una tesis breve para la pregunta «¿cambió el consumo y el bienestar entre 1950 y 1970?».",
         ["Veo que ambos indicadores subieron mucho.", "Elijo una afirmación con lugar y fechas.", "Agrego una palabra de grado para no exagerar."], "En la ciudad de ejemplo, entre 1950 y 1970, el consumo y el acceso a pensiones aumentaron de manera marcada"),
        ("Responder a un contraargumento", "Un compañero objeta: «Los datos suben, pero ¿y las zonas rurales?». ¿Cómo respondes con la nota de la ficha?",
         ["La nota dice que los datos no incluyen zonas rurales.", "Entonces la tesis vale solo para la ciudad de ejemplo."], "Reconozco el límite: la tesis solo vale para la ciudad de ejemplo"),
    ],
    mistakes=[
        ("Copiar datos sin decir qué significan.", "Una lista de cifras no es una interpretación.", "Cada dato debe apoyar una afirmación."),
        ("Generalizar desde una ciudad a toda la sociedad occidental.", "Los datos son de un solo lugar y no incluyen zonas rurales.", "Acota el lugar y las fechas en la tesis."),
    ],
    T=[
        ("En Historia: ¿qué es una tesis?", "Una afirmación que se defiende con evidencias", "Es el centro de una interpretación."),
        ("En Historia: ¿qué es un contraargumento?", "Una razón que podría debilitar la tesis", "Se incluye para probar la solidez de la tesis."),
        ("{F} ¿Cuántos hogares de cada 100 tenían acceso a pensiones públicas en 1970?", "70", "El dato está en la ficha."),
        ("=", "{F} ¿Cuántos hogares más de cada 100 tenían acceso a pensiones públicas en 1970 que en 1950?", "70-20", "Se resta el valor de 1950 al de 1970."),
        ("{F} ¿Qué indicador pasó de 30 a 12 hogares de cada 100? A) hogares sin agua potable, B) mujeres con trabajo remunerado, C) hogares con televisor.", "A", "La ficha lo asocia al agua potable."),
        ("{F} ¿Qué advertencia hace la nota de la ficha?", "Que los datos no incluyen a las zonas rurales de la región", "Es un límite explícito."),
        ("{F} Elige la tesis más proporcional. A) en la ciudad de ejemplo, entre 1950 y 1970, aumentaron la televisión, las pensiones y el empleo de mujeres, B) en toda la sociedad occidental la vida cambió igual entre 1950 y 1970, C) la vida de todas las personas de la región, incluidas las rurales, mejoró.", "A", "Solo A respeta lugar, fechas y datos."),
        ("{F} Un compañero afirma: «Las mujeres trabajaban casi tanto como los hombres en 1970». ¿Qué responde la ficha? A) solo informa que 35 de cada 100 mujeres tenían trabajo remunerado, sin compararlas con los hombres, B) lo confirma porque el trabajo de las mujeres subió 10 puntos, C) lo contradice porque solo 35 de cada 100 trabajaban.", "A", "La ficha no entrega datos de los hombres."),
        ("{F} ¿Qué evidencia de la ficha apoya la afirmación «aumentó el consumo»?", "El aumento de hogares con televisor de 10 a 85 de cada 100", "Es el indicador de consumo que da la ficha."),
        ("{F} Una lectora dice que los datos prueban que la sociedad occidental entera mejoró. ¿Qué dos límites señalas?", "Son de una sola ciudad de ejemplo y no incluyen zonas rurales", "Hay límites de lugar y de grupos."),
        ("Ordena una interpretación documentada: a) evidencias; b) tesis; c) límite y pregunta abierta.", "b, a, c", "La estructura parte por la tesis, sigue con evidencias y cierra con el límite."),
        ("{F} Escribe un contraargumento a la tesis «el bienestar mejoró para todos entre 1950 y 1970».", "Aunque los indicadores subieron, aún 12 de cada 100 hogares no tenían agua potable y las zonas rurales no están medidas", "Usa datos de la ficha para debilitar la tesis."),
        ("{F} Redacta una pregunta abierta que las fuentes no responden.", "Por ejemplo: ¿cómo cambió la vida en las zonas rurales de la región?", "La ficha no incluye zonas rurales."),
    ],
    ctx=("{F} Un grupo escribe: «Entre 1950 y 1970 todo mejoró en todas partes». ¿Cómo la reescribes de forma proporcional, con lugar, fechas y un límite?", "Por ejemplo: en la ciudad de ejemplo, entre 1950 y 1970, subieron la televisión y las pensiones, pero los datos no incluyen zonas rurales", "Debe nombrar lugar, fechas, indicadores y límite."),
    sc=[("En Historia: ¿qué es una conclusión proporcional?", "Una conclusión que no afirma más de lo que prueba la evidencia", "Evita exagerar con los datos."),
        ("Nombra las partes de una interpretación documentada.", "Tesis, evidencias, límite y pregunta abierta", "Es la estructura de la clase."),
        ("¿Para qué sirve un contraargumento?", "Para mostrar una razón que podría debilitar la tesis y responderla", "Hace más sólida la interpretación.")],
    op=("Responde con un texto de seis líneas la pregunta «¿Cuánto cambió la vida cotidiana en una ciudad occidental de ejemplo entre 1950 y 1970?». Usa la ficha de la clase e incluye tesis, dos evidencias, un contraargumento con su respuesta, un límite y una pregunta abierta.",
        "En la ciudad de ejemplo, entre 1950 y 1970, la vida cotidiana cambió de manera marcada. Los hogares con televisor pasaron de 10 a 85 de cada 100 y las pensiones llegaron a 70. Se podría objetar que 12 de cada 100 hogares seguían sin agua potable; eso muestra que no todos mejoraron igual. Límite: no hay datos rurales. Pregunta: ¿cómo cambió el campo?",
        ["tesis clara con lugar y fechas", "dos evidencias de la ficha", "contraargumento, límite y pregunta abierta"], ["texto de seis líneas"], ["tesis demasiado general", "no citar datos"], "Pide a una persona de tu casa que marque en tu texto la tesis y una evidencia."),
    reinforce="Reescribe una afirmación exagerada (por ejemplo «todos tenían todo») en una versión con lugar y fechas.",
    extend="Escribe una segunda tesis sobre el mismo tema que enfatice las desigualdades en vez de los avances.",
    materials=MAT,
)
