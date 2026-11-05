"""Cuaderno del estudiante, 2.º medio Historia, Geografía y Ciencias Sociales: OA 21 (sociedad chilena desde la recuperación democrática) y OA 22 (derechos humanos e institucionalidad de protección)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 21"

# ================================================================ OA 21, clase 1
F = ("Ficha 1 (un hecho y datos de ejemplo). "
     "Hecho: en marzo de 1990 asumió un presidente elegido por voto popular y comenzaron los gobiernos democráticos posteriores a la dictadura. "
     "Ámbitos para estudiar la sociedad: estructura social (cómo se distribuyen las personas según ingreso, ocupación y educación); acceso a bienes (qué cosas pueden comprar o usar los hogares); infraestructura (caminos, puentes, agua, electricidad); "
     "medios y tecnologías de comunicación; sistema educacional; mercado del trabajo; derechos de grupos históricamente discriminados. "
     "Actores: familias, Estado, empresas, escuelas y universidades, sindicatos y organizaciones de la sociedad civil. "
     "Datos de ejemplo, inventados para practicar: de cada 100 hogares de una comuna ficticia, 8 tenían teléfono celular en 1995 y 90 en 2015.")
build(
    OA, 1, F,
    use="Aprenderé a situar la sociedad chilena posterior a 1990 en sus ámbitos y actores, y a plantear una pregunta de investigación que no se reduzca a un solo dato.",
    prior=["Sé que en 1990 terminó la dictadura y volvió el gobierno elegido por voto.", "Sé calcular diferencias entre dos cifras.", "Sé que una fuente es una huella del pasado."],
    explain=[
        "Estudiar la sociedad chilena después de la recuperación de la democracia obliga a mirar varios ámbitos a la vez. La estructura social describe cómo se distribuyen las personas según ingreso, ocupación y educación. El acceso a bienes indica qué pueden comprar o usar los hogares, y la infraestructura incluye caminos, agua y electricidad.",
        "Otros ámbitos son los medios y tecnologías de comunicación, el sistema educacional, el mercado del trabajo y los derechos de grupos históricamente discriminados, es decir, personas que por mucho tiempo recibieron un trato desigual. Un indicador es un dato que mide un aspecto de la realidad, como el porcentaje de hogares con celular.",
        "Un solo indicador muestra solo una parte. Por eso se pregunta quiénes actúan (familias, Estado, empresas, escuelas, sindicatos, organizaciones) y a quiénes alcanzaron los cambios. Los datos de esta clase son de ejemplo: sirven para practicar, no para afirmar cifras reales del país.",
    ],
    vocab=[("estructura social", "forma en que se distribuyen las personas según ingreso, ocupación y educación"), ("indicador", "dato que mide un aspecto de la realidad, como un porcentaje de hogares"), ("infraestructura", "obras como caminos, puentes, agua y electricidad que sostienen la vida cotidiana"), ("mercado del trabajo", "conjunto de empleos disponibles y de personas que buscan trabajo"), ("grupos históricamente discriminados", "personas que durante mucho tiempo recibieron un trato desigual")],
    worked=[
        ("Elegir el ámbito", "Un liceo de ejemplo abre un taller para aprender oficios con la ayuda del Estado. ¿Qué ámbitos de la ficha toca?",
         ["Un taller en un liceo pertenece al sistema educacional.", "Aprender oficios se relaciona además con el mercado del trabajo."], "Sistema educacional y mercado del trabajo"),
        ("Leer un indicador", "En un barrio de ejemplo, 20 de cada 100 familias tenían computador en 2000 y 70 en 2020. ¿Cuántas familias más de cada 100 lo tenían?",
         ["Tomo los dos porcentajes.", "Resto: 70 − 20 = 50."], "50 familias más de cada 100"),
    ],
    mistakes=[("Describir la sociedad chilena con un solo dato, como los hogares con celular.", "Se confunde un indicador con el conjunto de la sociedad.", "Nombra al menos dos ámbitos y un dato para cada uno."),
              ("Tomar los datos de ejemplo como cifras reales del país.", "No se lee el rótulo «de ejemplo».", "Antes de citar una cifra, revisa si es real, de quién es y de qué año.")],
    T=[
        ("{F} ¿En qué mes y año comenzaron los gobiernos democráticos posteriores a la dictadura?", "Marzo de 1990", "La ficha lo indica como el comienzo de esos gobiernos."),
        ("{F} ¿Qué ámbito de la ficha estudia caminos, puentes, agua y electricidad?", "Infraestructura", "La ficha pone esas obras en infraestructura."),
        ("{F} Según la ficha, ¿qué es la estructura social?", "Cómo se distribuyen las personas según ingreso, ocupación y educación", "Esa es la definición de la ficha."),
        ("=", "{F} En la comuna ficticia, ¿cuántos hogares más de cada 100 tenían celular en 2015 que en 1995?", "90-8", "Se resta el dato de 1995 al de 2015.", " hogares"),
        ("{F} ¿Cuál de estos datos es solo un ejemplo y no un hecho histórico de la ficha? A) 8 de cada 100 hogares con celular en 1995 B) Marzo de 1990 como inicio de los gobiernos democráticos", "A) 8 de cada 100 hogares con celular en 1995", "La ficha rotula como de ejemplo los datos de la comuna ficticia."),
        ("{F} Un sindicato negocia un reajuste de sueldos. ¿Qué ámbito toca principalmente? A) Mercado del trabajo B) Infraestructura", "A) Mercado del trabajo", "Los sueldos y el empleo pertenecen al mercado del trabajo."),
        ("{F} Un hogar compra su primera lavadora a crédito. ¿Qué ámbito ilustra? A) Acceso a bienes B) Infraestructura", "A) Acceso a bienes", "Comprar objetos para el hogar es acceso a bienes."),
        ("{F} Una mujer reclama igual sueldo por igual trabajo. ¿Qué ámbitos toca a la vez? A) Mercado del trabajo y derechos de grupos históricamente discriminados B) Infraestructura y medios de comunicación", "A) Mercado del trabajo y derechos de grupos históricamente discriminados", "Habla de un sueldo y de un trato desigual hacia las mujeres."),
        ("=", "{F} En una muestra ficticia de 50 hogares, 35 tienen internet. Si la proporción fuera igual en 100 hogares, ¿cuántos tendrían?", "35*2", "La muestra es la mitad de 100, así que se duplica el dato.", " hogares"),
        ("{F} ¿Por qué un solo dato, como los hogares con celular, no basta para describir la sociedad chilena desde 1990?", "Porque la sociedad tiene varios ámbitos, como educación, trabajo e infraestructura, y un dato muestra solo uno", "Cada ámbito exige sus propios indicadores y actores."),
        ("{F} Alguien dice: «En 2015 casi todos los hogares de la comuna tenían celular, así que ya no había desigualdades». ¿Qué corrección corresponde? A) Tener celular es un solo indicador y no mide desigualdades de ingreso, trabajo o derechos B) Tiene razón, porque 90 es un número alto", "A) Tener celular es un solo indicador y no mide desigualdades de ingreso, trabajo o derechos", "Un indicador no resume todos los ámbitos de la ficha."),
        ("{F} Escribe una pregunta de investigación sobre la sociedad chilena desde 1990 que combine dos ámbitos de la ficha.", "Respuesta modelo: ¿Cómo cambió el acceso a la educación superior y qué efecto tuvo en el mercado del trabajo desde 1990?", "Combina el sistema educacional con el mercado del trabajo y pide explicar un cambio."),
        ("¿Cuál es la mejor pregunta para este tema? A) ¿Cómo cambió el acceso a bienes y a la educación de las familias chilenas desde 1990, y para quiénes? B) ¿Era mejor la vida antes de 1990?", "A) ¿Cómo cambió el acceso a bienes y a la educación de las familias chilenas desde 1990, y para quiénes?", "La pregunta A tiene tiempo, ámbitos y actores y se responde con datos; la B es una opinión sin criterio."),
    ],
    ctx=("Un reportaje titula: «Desde 1990 Chile cambió por completo». ¿Qué le falta para ser una afirmación histórica sólida? A) Precisar qué ámbito cambió, entre qué años y con qué evidencia B) Cambiar «cambió» por «mejoró»", "A) Precisar qué ámbito cambió, entre qué años y con qué evidencia", "Una afirmación histórica exige ámbito, tiempo y evidencia."),
    sc=[("¿Qué es un indicador?", "Un dato que mide un aspecto de la realidad", "Así se define en el vocabulario de la clase."),
        ("En Historia: ¿qué ámbito estudia los empleos disponibles y a las personas que buscan trabajo?", "El mercado del trabajo", "Así se define el mercado del trabajo en el vocabulario de la clase."),
        ("=", "En un pueblo de ejemplo había 12 de cada 100 hogares con internet en 2005 y 64 en 2019. ¿Cuántos más de cada 100 hay?", "64-12", "Se resta el dato antiguo al reciente.", " hogares")],
    op=("Elige dos ámbitos de la ficha (por ejemplo, sistema educacional y mercado del trabajo) y escribe, para cada uno, un indicador que lo mediría y un actor que influye en él. Luego redacta una pregunta de investigación que los relacione y que incluya los años 1990 y 2020. {F}",
        "Ámbito 1: sistema educacional; indicador: jóvenes de cada 100 que ingresan a estudios superiores; actor: universidades y Estado. Ámbito 2: mercado del trabajo; indicador: personas con contrato; actor: empresas y sindicatos. Pregunta: ¿cómo cambió entre 1990 y 2020 la relación entre estudiar más y conseguir empleos formales?",
        ["elige dos ámbitos distintos", "cada indicador mide realmente su ámbito", "la pregunta incluye los dos ámbitos y las fechas"], ["dos ámbitos con indicador y actor", "una pregunta de investigación"], ["usar el mismo indicador para los dos ámbitos", "plantear una pregunta de opinión"],
        "Pide que explique por qué el indicador elegido no alcanza para describir todo el ámbito."),
    reinforce="Explica a una persona de tu casa qué es un indicador y da un ejemplo de un ámbito de la sociedad que podría medirse con él.",
    extend="Elige un servicio de tu barrio, como una plaza o un paradero, y di a qué ámbito de la ficha pertenece y qué indicador lo mediría.",
)

# ================================================================ OA 21, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos reales). "
     "Fuente A, informe de una oficina estadística ficticia, 2018: «En la región Alfa, el 62 % de los jóvenes de 18 a 24 años cursa estudios superiores.» "
     "Fuente B, aviso de una empresa de telefonía ficticia, 2005: «Conecte a toda su familia: el futuro ya llegó a su barrio.» "
     "Fuente C, testimonio de una trabajadora ficticia, 2019: «Tengo contrato, pero mi sueldo no alcanza para el arriendo y la locomoción.»")
build(
    OA, 2, F,
    use="Aprenderé a preguntar a una fuente quién la hizo, cuándo y para qué, y a decidir qué puede probar y qué no sobre la sociedad chilena reciente.",
    prior=["Sé qué es un indicador y qué ámbitos tiene la sociedad.", "Sé distinguir una cifra de un testimonio.", "Sé que una fuente puede tener un propósito."],
    explain=[
        "La procedencia de una fuente es su origen: quién la produjo, cuándo y con qué propósito. Un informe estadístico busca medir; un aviso comercial busca vender; un testimonio cuenta la experiencia de una persona. Cada tipo sirve para algo distinto y no todos prueban lo mismo.",
        "Una cifra permite comparar muchos casos, pero no cuenta cómo se vive cada uno. Un testimonio muestra una experiencia concreta, pero no se puede generalizar a toda la población. Un aviso muestra cómo una empresa quería presentar sus productos, no cuántos hogares los tenían.",
        "Antes de usar una fuente se hacen tres preguntas: ¿quién habla?, ¿cuándo?, ¿para qué? Después se escribe lo que la fuente permite afirmar y lo que no. Una fuente oficial no es falsa por ser oficial, pero tampoco es neutral por serlo: conviene contrastarla con otra fuente independiente.",
    ],
    vocab=[("procedencia", "origen de una fuente: autor, fecha y propósito"), ("propósito", "razón por la que alguien produjo una fuente"), ("testimonio", "relato de una persona sobre lo que vivió"), ("generalizar", "extender lo que vale para unos pocos casos a toda una población"), ("fuente independiente", "fuente de otro autor, que no depende de lo que se quiere probar")],
    worked=[
        ("Preguntar por el propósito", "Un afiche de 2010 dice: «Compre en cuotas el televisor de sus sueños». ¿Para qué se hizo?",
         ["Es un afiche de una tienda.", "Busca que la gente compre, no medir cuántos televisores hay."], "Para vender televisores; no sirve para medir cuántos hogares los tenían"),
        ("Acotar una conclusión", "Un testimonio de 2017 dice que un taller de oficios ayudó a su autor a encontrar trabajo. ¿Se puede concluir que el taller funciona para todos?",
         ["El testimonio cuenta una sola experiencia.", "Generalizar exigiría datos de muchos participantes."], "No; solo muestra una experiencia"),
    ],
    mistakes=[("Usar un aviso comercial como prueba de cuántos hogares tenían un servicio.", "Se olvida que su propósito es vender.", "Pregunta para qué se hizo y busca un dato que mida."),
              ("Decir que una fuente oficial es falsa porque es oficial.", "Se reemplaza el análisis por una sospecha automática.", "Revisa su propósito y contrástala con otra fuente independiente.")],
    T=[
        ("{F} ¿Quién produjo la Fuente B y con qué propósito principal?", "Una empresa de telefonía, para vender sus servicios", "Es un aviso comercial."),
        ("{F} ¿En qué año se produjo la Fuente A?", "2018", "La ficha indica su fecha."),
        ("{F} ¿Qué problema cuenta la trabajadora de la Fuente C?", "Que aunque tiene contrato su sueldo no alcanza para el arriendo y la locomoción", "Eso dice el testimonio."),
        ("{F} ¿Por qué el aviso de la Fuente B no prueba por sí solo cuántos hogares tenían telefonía? A) Porque busca vender y no mide cuántos hogares la tenían B) Porque es de 2005", "A) Porque busca vender y no mide cuántos hogares la tenían", "El año no invalida una fuente; su propósito limita lo que prueba."),
        ("{F} ¿Qué puede mostrar la Fuente C que la Fuente A no muestra? A) La experiencia de una persona con el trabajo y el costo de vivir B) El porcentaje de toda la región", "A) La experiencia de una persona con el trabajo y el costo de vivir", "El testimonio cuenta una vivencia; la cifra mide muchos casos."),
        ("=", "{F} Si el 62 % de una muestra de 200 jóvenes cursa estudios superiores, ¿cuántos jóvenes son?", "62*200/100", "Se calcula el 62 % de 200.", " jóvenes"),
        ("{F} Quieres afirmar que «aumentó la participación de jóvenes en estudios superiores en la región Alfa». ¿Qué fuente sirve más como evidencia principal? A) La Fuente A B) La Fuente B", "A) La Fuente A", "Es un informe que mide el porcentaje de jóvenes en estudios superiores."),
        ("{F} Una compañera escribe: «La Fuente C prueba que a todos los trabajadores les falta dinero». ¿Qué error comete? A) Generaliza desde el testimonio de una sola persona B) Usa una fuente de 2019", "A) Generaliza desde el testimonio de una sola persona", "Un testimonio no autoriza afirmaciones sobre todos."),
        ("{F} ¿Qué tipo de fuente es la Fuente A: informe estadístico, aviso comercial o testimonio?", "Un informe estadístico", "Mide el porcentaje de jóvenes en estudios superiores en una región."),
        ("{F} ¿Cómo usarías la Fuente A y la Fuente B juntas sin tratarlas como el mismo tipo de evidencia?", "La A como dato de estudios superiores en 2018 y la B como muestra de cómo una empresa promocionaba sus servicios en 2005, no como prueba de cobertura", "Cada fuente tiene un propósito distinto y prueba cosas distintas."),
        ("{F} ¿Qué pregunta de procedencia haces a la Fuente C antes de usarla? A) ¿Quién habla, en qué año y en qué situación laboral? B) ¿Es una fuente oficial? Si lo es, no hace falta preguntar más", "A) ¿Quién habla, en qué año y en qué situación laboral?", "La procedencia pregunta por autor, fecha y situación, no por el largo."),
        ("{F} Redacta una conclusión de una oración con las Fuentes A y C que no exagere.", "Respuesta modelo: En la región Alfa había muchos jóvenes en estudios superiores en 2018 y, según un testimonio de 2019, tener contrato no aseguraba que el sueldo alcanzara; falta evidencia para generalizar.", "Usa cada fuente para lo que puede probar y reconoce un límite."),
        ("{F} Un estudiante concluye: «Entre 2005 y 2019 la vida mejoró para todos». ¿Qué evidencia faltaría? A) Datos que midan ingresos y empleo de distintos grupos en ambos años B) Más testimonios de personas conformes con su situación", "A) Datos que midan ingresos y empleo de distintos grupos en ambos años", "Para afirmar mejora general hacen falta mediciones comparables de varios grupos."),
    ],
    ctx=("Un diario de 2012 publica una entrevista a un gerente que dice que su empresa «ha creado empleo para toda la comuna». ¿Qué haces antes de usar la entrevista como evidencia? A) Buscar otra fuente independiente que mida los empleos de la comuna B) Citarla tal cual porque es una entrevista", "A) Buscar otra fuente independiente que mida los empleos de la comuna", "El gerente tiene interés en mostrar logros; conviene contrastar."),
    sc=[("¿Qué es la procedencia de una fuente?", "Su origen: autor, fecha y propósito", "Así se define en la clase."),
        ("¿Por qué un testimonio no se puede generalizar?", "Porque cuenta la experiencia de una persona y no mide a toda la población", "Una vivencia no representa a todos."),
        ("¿Qué tipo de fuente busca medir muchos casos: un informe estadístico o un aviso comercial?", "Un informe estadístico", "El informe estadístico mide; el aviso busca vender.")],
    op=("Lee estas tres fuentes de ejemplo. Fuente 1, informe ficticio de 2016: «En la ciudad Beta, 4 de cada 10 familias arrendaban su vivienda». Fuente 2, aviso ficticio de 2016: «Compre su casa con crédito hipotecario sin trabas». Fuente 3, carta ficticia de una vecina, 2016: «Llevo cinco años buscando una casa que pueda pagar». Para cada una escribe quién habla, para qué y qué puede probar. Después redacta una conclusión de dos oraciones que use las tres sin exagerar.",
        "Fuente 1: oficina de estadística; mide; prueba que 4 de cada 10 familias arrendaban en Beta. Fuente 2: empresa de crédito; vende; no prueba cuántas familias compraron. Fuente 3: una vecina; cuenta su experiencia; no se puede generalizar. Conclusión: en 2016 muchas familias de Beta arrendaban y una vecina contó que comprar era difícil; faltan datos de precios para afirmar más.",
        ["identifica autor y propósito de cada fuente", "indica lo que cada fuente puede y no puede probar", "la conclusión reconoce un límite"], ["tabla de tres fuentes", "conclusión de dos oraciones"], ["tratar el aviso como medición", "generalizar desde la carta"],
        "Pide que diga qué otra fuente conseguiría para comprobar el precio de las viviendas."),
    reinforce="Elige un aviso que veas en tu casa o en la calle y di quién lo hizo, para qué y qué no podría probar.",
    extend="Escribe una pregunta que le harías a una persona mayor de tu familia para recoger un testimonio sobre cómo cambió su barrio, y una razón para no generalizar su respuesta.",
)

# ================================================================ OA 21, clase 3
F = ("Ficha 3 (datos de ejemplo de dos comunas ficticias con igual número de hogares). "
     "Comuna A, ciudad grande: 80 de cada 100 hogares tienen internet fijo; los adultos tienen en promedio 12 años de estudio. "
     "Comuna B, zona rural: 30 de cada 100 hogares tienen internet fijo; los adultos tienen en promedio 8 años de estudio. "
     "Testimonio de una familia de la comuna A: «Mis hijos hacen las tareas en línea». "
     "Testimonio de una familia de la comuna B: «La señal llega solo desde la plaza». "
     "Declaración de una funcionaria municipal de la comuna B: «Necesitamos inversión para conectar a los hogares».")
build(
    OA, 3, F,
    use="Aprenderé a comparar la situación de distintos lugares y grupos, a leer brechas y a distinguir qué dice un promedio nacional y qué dice cada comuna.",
    prior=["Sé interpretar un porcentaje.", "Sé que una fuente tiene procedencia.", "Sé que hay escalas: hogar, comuna, país."],
    explain=[
        "La escala es el tamaño del territorio o del grupo que se mira: un hogar, una comuna, una región o todo el país. Un promedio nacional resume muchos casos en un solo número, pero puede ocultar diferencias grandes entre comunas. Por eso se comparan lugares con el mismo indicador y el mismo año.",
        "La brecha es la diferencia entre dos grupos o lugares en un indicador. Si una comuna tiene 80 % de hogares con internet y otra 30 %, la brecha es de 50 puntos porcentuales, que es la diferencia entre dos porcentajes. Medir la brecha ayuda a ver quién queda atrás.",
        "También se comparan perspectivas: una familia, una funcionaria o un informe miran el mismo problema desde posiciones distintas. Una perspectiva no es una mentira; es un punto de vista que se apoya en lo que esa persona vive o conoce. La evidencia se contrasta para ver cuánto se puede generalizar.",
    ],
    vocab=[("escala", "tamaño del territorio o grupo que se analiza: hogar, comuna, región o país"), ("brecha", "diferencia entre dos grupos o lugares en un indicador"), ("punto porcentual", "unidad con que se mide la diferencia entre dos porcentajes"), ("promedio", "valor que resume varios datos al repartirlos por igual"), ("perspectiva", "punto de vista de una persona o grupo según lo que vive o conoce")],
    worked=[
        ("Calcular una brecha", "En dos comunas ficticias, 90 % y 45 % de los hogares tienen agua potable. ¿Cuál es la brecha?",
         ["Resto el porcentaje menor al mayor.", "90 − 45 = 45."], "45 puntos porcentuales"),
        ("Leer un promedio", "Dos comunas con igual número de hogares tienen 60 % y 20 % de hogares con computador. ¿El promedio de 40 % describe a cada una?",
         ["El promedio resulta de (60 + 20) ÷ 2 = 40.", "Ninguna comuna tiene 40 %: una está muy arriba y otra muy abajo."], "No; el promedio oculta la diferencia"),
    ],
    mistakes=[("Comparar una comuna en 1995 con otra en 2020.", "No se usa el mismo año ni el mismo indicador.", "Compara siempre mismo indicador y mismo año."),
              ("Creer que el promedio nacional describe a todas las comunas.", "Se olvida que un promedio ocultaba diferencias.", "Mira los datos por comuna antes de concluir.")],
    T=[
        ("{F} ¿Qué porcentaje de hogares de la comuna B tiene internet fijo?", "30 %", "La ficha lo indica."),
        ("{F} ¿Cuántos años promedio de estudio tienen los adultos de la comuna A?", "12 años", "La ficha lo indica."),
        ("{F} Según la explicación, ¿qué es una brecha?", "La diferencia entre dos grupos o lugares en un indicador", "Esa es la definición de la clase."),
        ("=", "{F} ¿Cuántos puntos porcentuales más de hogares con internet fijo tiene la comuna A que la B?", "80-30", "Se resta el porcentaje menor al mayor.", " puntos porcentuales"),
        ("=", "{F} Con igual número de hogares en ambas comunas, ¿cuál es el porcentaje promedio de hogares con internet fijo?", "(80+30)/2", "Se suman los dos porcentajes y se divide por dos.", " %"),
        ("{F} La familia de la comuna B dice que la señal llega solo desde la plaza. ¿A qué escala corresponde su testimonio? A) Escala del hogar y la comuna B) Escala nacional", "A) Escala del hogar y la comuna", "Habla de una familia y de su lugar de residencia."),
        ("=", "{F} ¿Cuántos años de estudio tendría un adulto que represente el promedio de las dos comunas?", "(12+8)/2", "Se suman los dos promedios y se divide por dos.", " años"),
        ("{F} Quieres comparar justamente ambas comunas. ¿Qué debes cuidar? A) Usar el mismo indicador y el mismo año para las dos B) Usar datos de 1995 para una y de 2020 para la otra", "A) Usar el mismo indicador y el mismo año para las dos", "Sin el mismo indicador y año la comparación no es válida."),
        ("{F} La funcionaria de B pide inversión y la familia de A no la menciona. ¿Qué explica esa diferencia de perspectiva? A) Viven situaciones distintas de acceso a internet B) Una de las dos miente", "A) Viven situaciones distintas de acceso a internet", "Las perspectivas dependen de la experiencia de cada una."),
        ("{F} ¿Por qué un promedio de las dos comunas puede ocultar la situación de la comuna rural?", "Porque mezcla un 80 % y un 30 % en un número que no describe bien a ninguna de las dos", "Un promedio esconde las diferencias entre los lugares."),
        ("{F} Un reportaje afirma que «55 de cada 100 hogares tienen internet fijo» sumando las dos comunas. ¿Qué pregunta de escala corresponde? A) ¿Cómo varía el dato entre cada comuna? B) ¿Qué canal lo emitió?", "A) ¿Cómo varía el dato entre cada comuna?", "La pregunta de escala busca las diferencias dentro del promedio."),
        ("{F} Redacta una oración que compare las comunas A y B con dos escalas: la de la comuna y la del hogar.", "Respuesta modelo: En la comuna A 80 de cada 100 hogares tienen internet fijo y una familia dice que sus hijos hacen tareas en línea, mientras en la comuna B son 30 de cada 100 y una familia cuenta que la señal llega solo desde la plaza.", "Une un dato de comuna con un testimonio de hogar."),
        ("{F} ¿Cuál propuesta se apoya en la escala comunal de los datos? A) Dirigir la inversión a las comunas donde el porcentaje de hogares conectados es más bajo B) Repartir una misma inversión a todo el país sin mirar los datos", "A) Dirigir la inversión a las comunas donde el porcentaje de hogares conectados es más bajo", "Usa el dato de cada comuna para decidir."),
    ],
    ctx=("Un informe dice: «El 55 % de los hogares tiene internet fijo». Una profesora de una zona rural responde que en su escuela casi nadie lo tiene. ¿Cómo se explican ambas afirmaciones? A) El informe habla de un promedio y la profesora de su lugar, que puede estar por debajo B) La profesora se equivoca", "A) El informe habla de un promedio y la profesora de su lugar, que puede estar por debajo", "Un promedio general puede coexistir con lugares muy distintos."),
    sc=[("¿Qué es una brecha?", "La diferencia entre dos grupos o lugares en un indicador", "Así se define en la clase."),
        ("¿Qué debes mantener igual al comparar dos comunas?", "El indicador y el año", "Sin eso la comparación no es justa."),
        ("=", "Una comuna ficticia tiene 70 % de hogares con agua potable y otra 25 %. ¿Cuál es la brecha en puntos porcentuales?", "70-25", "Se resta el porcentaje menor al mayor.", " puntos porcentuales")],
    op=("Con los datos de la ficha escribe un párrafo de cuatro oraciones que compare las comunas A y B. Debe incluir: la brecha en hogares con internet fijo, la diferencia en años de estudio, una perspectiva de una familia y una advertencia sobre el uso del promedio. {F}",
        "En la comuna A, 80 % de los hogares tiene internet fijo y en la B, 30 %; la brecha es de 50 puntos. Los adultos de A estudiaron en promedio 4 años más que los de B (12 y 8). Una familia de B dice que la señal llega solo desde la plaza. Un promedio de ambas comunas escondería esa diferencia.",
        ["calcula bien la brecha y la diferencia", "incluye una perspectiva", "advierte sobre el promedio"], ["párrafo de cuatro oraciones"], ["restar mal los datos", "concluir solo con el promedio"],
        "Pide que explique por qué la comuna B necesita una medida distinta de la comuna A."),
    reinforce="Explica a una persona de tu casa por qué un promedio de dos lugares muy distintos no describe a ninguno.",
    extend="Anota un servicio (por ejemplo, transporte o salud) que en tu comuna sea más fácil o más difícil de usar que en otra y di cómo medirías la diferencia.",
)

# ================================================================ OA 21, clase 4
F = ("Ficha 4 (indicadores de ejemplo de un país ficticio; no son cifras reales de Chile). "
     "De cada 100 jóvenes, ingresaban a la educación superior 15 en 1990 y 55 en 2015. De cada 100 hogares, tenían refrigerador 60 en 1990 y 95 en 2015. "
     "Causas que se proponen: crecimiento económico, mayor oferta de créditos para comprar y estudiar, y políticas públicas de ampliación de la educación. "
     "Continuidades: la calidad de los colegios sigue siendo desigual, los barrios están separados por nivel de ingreso y el trabajo informal sigue existiendo. "
     "Advertencia: que dos hechos ocurran a la vez no prueba que uno cause al otro.")
build(
    OA, 4, F,
    use="Aprenderé a distinguir cambios y continuidades en la sociedad chilena posterior a 1990, a proponer varias causas y a no confundir coincidencia con causa.",
    prior=["Sé comparar un indicador entre dos años.", "Sé que un hecho puede tener varias causas.", "Sé leer una brecha."],
    explain=[
        "Un cambio es algo que ya no es igual que antes; una continuidad es algo que se mantiene a pesar del tiempo. En una misma época hay ambos: crece el acceso a ciertos bienes y servicios, y a la vez persisten desigualdades. Mirar solo cambios o solo continuidades da una imagen incompleta.",
        "Los cambios casi nunca tienen una sola causa. El aumento de jóvenes en la educación superior puede explicarse por el crecimiento económico, por más créditos para estudiar y por políticas públicas que ampliaron las oportunidades. Esto se llama multicausalidad: varias causas combinadas.",
        "Cuidado con la correlación, que es cuando dos datos suben o bajan juntos. Que ocurra no prueba que uno cause al otro: pueden depender de una tercera causa. Para sostener una causa hace falta evidencia que muestre cómo actuó, no solo que ocurrió al mismo tiempo.",
    ],
    vocab=[("cambio", "aspecto de la sociedad que ya no es igual que antes"), ("continuidad", "aspecto que se mantiene a pesar del paso del tiempo"), ("multicausalidad", "explicación de un hecho por varias causas combinadas"), ("correlación", "relación entre dos datos que suben o bajan juntos, sin que eso pruebe causa"), ("segregación", "separación de personas en barrios o espacios según su ingreso u origen")],
    worked=[
        ("Clasificar un hecho", "En una ciudad ficticia, el 30 % de los trabajadores tenía un empleo informal en 1990 y sigue habiendo informalidad en 2015. ¿Es un cambio o una continuidad?",
         ["Se compara 1990 con 2015.", "La informalidad existe en ambos años, aunque su porcentaje pueda variar."], "Una continuidad: la informalidad se mantiene"),
        ("Separar correlación y causa", "Cuando suben las ventas de bufandas, suben las de estufas. ¿Una causa la otra?",
         ["Ambas suben en invierno.", "La causa común es el frío, no que una produzca la otra."], "No; hay una causa común"),
    ],
    mistakes=[("Explicar el aumento de ingresos a la educación superior solo por el crecimiento económico.", "Se ignora la multicausalidad.", "Propón al menos dos causas y busca evidencia para cada una."),
              ("Decir que, como suben los dos datos, uno causa el otro.", "Se confunde correlación con causa.", "Busca una causa común o evidencia del mecanismo.")],
    T=[
        ("{F} ¿Cuántos jóvenes de cada 100 ingresaban a la educación superior en 1990?", "15", "La ficha lo indica."),
        ("{F} ¿Cómo se llama lo que se mantiene a pesar del paso del tiempo?", "Continuidad", "Esa es la definición de continuidad."),
        ("{F} ¿Qué continuidad de la ficha se relaciona con el nivel de ingreso de las familias?", "Los barrios están separados por nivel de ingreso", "La ficha lo indica como una continuidad."),
        ("=", "{F} ¿Cuántos jóvenes más de cada 100 ingresaban a la educación superior en 2015 que en 1990?", "55-15", "Se resta el dato de 1990 al de 2015.", " jóvenes"),
        ("=", "{F} De 2.000 jóvenes de ejemplo en 2015, ¿cuántos ingresarían a la educación superior con la proporción de la ficha?", "55*20", "2.000 jóvenes son 20 grupos de 100.", " jóvenes"),
        ("{F} Una familia de ejemplo compra su primera casa gracias a un crédito. ¿Qué causa de la ficha se ve ahí? A) La mayor oferta de créditos B) El menor ingreso nacional", "A) La mayor oferta de créditos", "Comprar con crédito muestra la oferta de créditos."),
        ("{F} Alguien afirma: «Aumentó la educación superior, así que desapareció la desigualdad». ¿Qué falta? A) Mirar las continuidades, como la calidad desigual de los colegios y la separación de barrios B) Nada, el argumento es completo", "A) Mirar las continuidades, como la calidad desigual de los colegios y la separación de barrios", "Un cambio no borra las continuidades de la ficha."),
        ("{F} Los hogares con refrigerador pasaron de 60 a 95 de cada 100. ¿Qué causa de la ficha lo explica en parte? A) El crecimiento económico B) La segregación de barrios", "A) El crecimiento económico", "Más ingresos y crédito permiten comprar electrodomésticos."),
        ("{F} Una investigadora ve que suben las ventas de celulares y también las de helados. ¿Qué error debe evitar? A) Concluir que una cosa causa la otra solo porque ocurren juntas B) Medir ambos datos", "A) Concluir que una cosa causa la otra solo porque ocurren juntas", "La advertencia de la ficha distingue coincidencia de causa."),
        ("{F} ¿Por qué decir que «el crecimiento económico causó todo el aumento de la educación superior» es un error?", "Porque hubo otras causas, como los créditos y las políticas públicas, y una explicación multicausal es más completa", "La ficha propone tres causas combinadas."),
        ("{F} ¿Qué descripción muestra mejor un proceso con cambios y continuidades? A) Aumentó el ingreso a la educación superior y a la vez los colegios siguen con calidad desigual B) Aumentó el ingreso a la educación superior", "A) Aumentó el ingreso a la educación superior y a la vez los colegios siguen con calidad desigual", "Incluye un cambio y una continuidad."),
        ("{F} Escribe una oración que una un cambio, una continuidad y una causa usando la ficha.", "Respuesta modelo: Entre 1990 y 2015 aumentaron los jóvenes en la educación superior, en parte por más créditos, pero la calidad de los colegios siguió siendo desigual.", "Combina un dato de cambio, una causa y una continuidad."),
        ("{F} ¿Cuál es la conclusión más proporcional a la evidencia? A) Entre 1990 y 2015 aumentó el acceso a bienes y a la educación superior, pero persistieron desigualdades, y varias causas lo explican B) El crecimiento económico resolvió todos los problemas sociales", "A) Entre 1990 y 2015 aumentó el acceso a bienes y a la educación superior, pero persistieron desigualdades, y varias causas lo explican", "Incluye cambio, continuidad y multicausalidad sin exagerar."),
    ],
    ctx=("Un afiche escolar dice: «Desde 1990 todo mejoró y nada se mantuvo igual». ¿Qué corrección aplicas con la ficha? A) Hubo cambios importantes, pero también continuidades como la segregación de barrios B) El afiche está completo", "A) Hubo cambios importantes, pero también continuidades como la segregación de barrios", "La ficha muestra que cambios y continuidades conviven."),
    sc=[("¿Qué es la multicausalidad?", "Explicar un hecho por varias causas combinadas", "Así se define en la clase."),
        ("¿Qué es una continuidad?", "Algo que se mantiene a pesar del paso del tiempo", "Es lo opuesto a un cambio."),
        ("=", "En un barrio ficticio, 40 de cada 100 familias tenían trabajo informal en 1990 y 30 en 2015. ¿Cuántas menos hay?", "40-30", "Se resta el dato reciente al antiguo.", " familias")],
    op=("Elige un ámbito (educación, acceso a bienes o trabajo) y construye una tabla con tres columnas: un cambio entre 1990 y 2015, una continuidad y dos causas posibles. Usa los datos de la ficha. Luego escribe una frase que advierta por qué no puedes asegurar que una sola causa lo explique todo. {F}",
        "Ámbito: educación. Cambio: de 15 a 55 jóvenes de cada 100 en la educación superior. Continuidad: calidad desigual de los colegios. Causas: créditos para estudiar y políticas públicas. Advertencia: varias causas actuaron a la vez y coincidir en el tiempo no prueba una causa única.",
        ["usa datos de la ficha", "separa cambio, continuidad y causas", "advierte sobre las causas únicas"], ["tabla de tres columnas", "frase de advertencia"], ["poner una causa como continuidad", "afirmar una causa única sin evidencia"],
        "Pide que explique qué evidencia nueva necesitaría para sostener una de las causas."),
    reinforce="Cuenta a una persona de tu casa un cambio y una continuidad que veas en tu barrio y di una causa posible del cambio.",
    extend="Busca en tu entorno dos cosas que suben juntas, como el uso de abrigo y el consumo de sopa, y explica por qué una no causa la otra.",
)

# ================================================================ OA 21, clase 5
F = ("Ficha 5 (hechos y fuentes de ejemplo). "
     "Hecho: la ley que estableció la Jornada Escolar Completa en los colegios que reciben recursos del Estado se aprobó en 1997. "
     "Hecho: desde 2016 se aplica la gratuidad en la educación superior para estudiantes que cumplen requisitos de ingreso del hogar. "
     "Fuente 1, informe de una oficina estadística ficticia: «Entre 2000 y 2020, la matrícula en educación superior de la región Gamma pasó de 20.000 a 60.000 estudiantes.» "
     "Fuente 2, testimonio de una profesora ficticia, 2010: «Las clases se alargaron, pero faltan salas y materiales.» "
     "Estructura de un párrafo documentado: tesis (lo que se defiende), evidencia (datos o fuentes) y límite (lo que la evidencia no permite afirmar).")
build(
    OA, 5, F,
    use="Aprenderé a escribir una interpretación breve de un cambio social con una tesis, evidencia de dos fuentes y un límite explícito.",
    prior=["Sé distinguir cambio y continuidad.", "Sé evaluar la procedencia de una fuente.", "Sé que una conclusión debe ser proporcional a la evidencia."],
    explain=[
        "Una interpretación documentada es una explicación del pasado reciente que se apoya en fuentes. Tiene tres partes: la tesis, que es la afirmación que se defiende; la evidencia, que son los datos o textos que la sostienen; y el límite, que dice qué no se puede afirmar con esa evidencia.",
        "Una buena tesis es específica: nombra un ámbito, un período y un cambio o una continuidad. Por ejemplo: «Entre 2000 y 2020 aumentó la matrícula en educación superior en la región Gamma». La evidencia puede ser una cifra y un testimonio; juntos muestran cantidad y experiencia.",
        "El límite protege de exagerar. Se escribe con expresiones como «sin embargo», «aunque» o «no permite afirmar». Si los datos son de una sola región o de pocos años, el límite lo dice. Una interpretación honesta no oculta lo que la evidencia no muestra.",
    ],
    vocab=[("interpretación", "explicación del pasado apoyada en fuentes"), ("tesis", "afirmación principal que se defiende"), ("evidencia", "dato o texto que sostiene una afirmación"), ("límite", "aquello que la evidencia no permite afirmar"), ("matrícula", "número de estudiantes inscritos en un nivel educativo")],
    worked=[
        ("Armar un párrafo", "Datos de ejemplo: en el pueblo Delta los niños que terminan la básica pasaron de 70 a 90 de cada 100 entre 1990 y 2010. Escribe tesis, evidencia y límite.",
         ["Tesis: aumentó la educación básica completa en Delta.", "Evidencia: de 70 a 90 de cada 100; límite: son datos de un solo pueblo."], "Tesis, cifra de 70 a 90 y límite de un solo pueblo"),
        ("Medir un aumento", "Una matrícula de ejemplo pasó de 5.000 a 15.000 estudiantes. ¿Cuántas veces mayor es?",
         ["Divido el valor final por el inicial.", "15.000 ÷ 5.000 = 3."], "3 veces"),
    ],
    mistakes=[("Escribir una tesis sin período ni ámbito, como «la educación mejoró».", "No se puede comprobar con evidencia concreta.", "Nombra ámbito, período y cambio."),
              ("Omitir el límite de la conclusión.", "Se cree que más seguridad vuelve más convincente la tesis.", "Escribe qué no se puede afirmar con tus fuentes.")],
    T=[
        ("{F} ¿En qué año se aprobó la ley de la Jornada Escolar Completa?", "1997", "La ficha lo indica."),
        ("{F} ¿Cuáles son las tres partes de un párrafo documentado?", "Tesis, evidencia y límite", "La ficha enumera esas tres partes."),
        ("=", "{F} ¿Cuántos estudiantes más había en la matrícula de la región Gamma en 2020 que en 2000?", "60000-20000", "Se resta la matrícula inicial a la final.", " estudiantes"),
        ("{F} ¿Cuál es una tesis? A) Entre 2000 y 2020 aumentó el acceso a la educación superior en la región Gamma, aunque persisten problemas de recursos en las escuelas B) La educación superior es muy importante para Chile", "A) Entre 2000 y 2020 aumentó el acceso a la educación superior en la región Gamma, aunque persisten problemas de recursos en las escuelas", "Una tesis es una afirmación con ámbito, período y cambio; una cifra suelta no lo es."),
        ("{F} ¿Qué fuente apoya mejor que aumentó la matrícula? A) El informe de la oficina estadística B) El testimonio de la profesora", "A) El informe de la oficina estadística", "Entrega cifras de la matrícula en dos años."),
        ("=", "{F} ¿Cuántas veces mayor fue la matrícula de 2020 que la de 2000 en la región Gamma?", "60000/20000", "Se divide el valor final por el inicial.", " veces"),
        ("{F} El testimonio de la profesora, ¿qué límite aporta? A) Muestra que ampliar el tiempo de clases no resolvió la falta de salas y materiales B) Prueba que la ley no se aplicó", "A) Muestra que ampliar el tiempo de clases no resolvió la falta de salas y materiales", "Cuenta una limitación; no prueba que la ley no se aplicara."),
        ("{F} Completa el límite: «Estos datos son de una sola región, por lo tanto no permiten...»", "Generalizar a todo el país", "El límite dice que la evidencia no alcanza para afirmar algo sobre todo el país."),
        ("{F} ¿Qué expresión introduce mejor un límite? A) Sin embargo B) Por lo tanto", "A) Sin embargo", "Marca una restricción a lo que se acaba de afirmar."),
        ("{F} ¿Por qué el informe y el testimonio dicen cosas distintas y aun así se pueden usar juntos?", "Porque el informe muestra cantidad y el testimonio muestra la experiencia, y juntos dan una imagen más completa", "Cada fuente aporta un tipo de evidencia distinto."),
        ("{F} Una tesis dice: «La Jornada Escolar Completa mejoró el aprendizaje de todo el país». ¿Qué problema tiene con la evidencia de la ficha? A) Ninguna fuente de la ficha mide aprendizajes de todo el país B) Es demasiado corta", "A) Ninguna fuente de la ficha mide aprendizajes de todo el país", "La tesis afirma más de lo que la evidencia permite."),
        ("{F} Redacta un párrafo de tres oraciones (tesis, evidencia y límite) sobre educación en Chile usando solo la ficha.", "Respuesta modelo: La educación superior se amplió en la región Gamma entre 2000 y 2020. La matrícula pasó de 20.000 a 60.000 estudiantes. Sin embargo, el dato es de una sola región y un testimonio de 2010 cuenta que faltan salas y materiales.", "Incluye una tesis específica, una cifra y un límite."),
        ("{F} ¿Qué párrafo está mejor documentado? A) La matrícula pasó de 20.000 a 60.000 estudiantes en Gamma entre 2000 y 2020; sin embargo, no sabemos si pasó lo mismo en otras regiones B) La educación mejoró mucho y todos están contentos", "A) La matrícula pasó de 20.000 a 60.000 estudiantes en Gamma entre 2000 y 2020; sin embargo, no sabemos si pasó lo mismo en otras regiones", "Tiene cifra, período y límite; el otro es una opinión."),
    ],
    ctx=("Una estudiante escribe: «Desde que hay gratuidad, todos los jóvenes chilenos estudian». ¿Qué cambio mejora más su interpretación? A) Precisar a quiénes alcanza la gratuidad según la ficha y declarar qué datos faltan B) Quitar la palabra gratuidad", "A) Precisar a quiénes alcanza la gratuidad según la ficha y declarar qué datos faltan", "La gratuidad se aplica a estudiantes que cumplen requisitos; la tesis exagera."),
    sc=[("¿Qué es la tesis de una interpretación?", "La afirmación principal que se defiende", "Así se define en la clase."),
        ("¿Para qué sirve el límite?", "Para decir qué no se puede afirmar con la evidencia", "Protege de exagerar."),
        ("=", "Una matrícula de ejemplo pasó de 8.000 a 32.000 estudiantes. ¿Cuántas veces mayor es?", "32000/8000", "Se divide el valor final por el inicial.", " veces")],
    op=("Escribe un párrafo de cuatro oraciones sobre el cambio en la educación superior de la región Gamma entre 2000 y 2020, con este orden: tesis, cifra de la Fuente 1, una experiencia de la Fuente 2 y un límite que mencione al menos una cosa que no sabes. {F}",
        "La educación superior se amplió en la región Gamma entre 2000 y 2020. La matrícula pasó de 20.000 a 60.000 estudiantes. Una profesora contó en 2010 que las clases se alargaron pero faltan salas y materiales. Sin embargo, no sabemos si los egresados consiguieron trabajo.",
        ["la tesis es específica", "usa las dos fuentes", "el límite nombra algo que no se sabe"], ["párrafo de cuatro oraciones"], ["escribir una tesis sin período", "no incluir límite"],
        "Pide que diga qué tercera fuente buscaría para reforzar la interpretación."),
    reinforce="Escribe en una frase una tesis sobre un cambio de tu barrio, con ámbito y período.",
    extend="Pide a una persona mayor de tu casa que te cuente un cambio de su barrio y anota una tesis, una evidencia y un límite a partir de su relato.",
)

# ================================================================ OA 21, clase 6
F = ("Ficha 6 (hechos y un caso de ejemplo). "
     "Hechos: en 1993 se aprobó en Chile la ley indígena; en 2010, la ley sobre igualdad de oportunidades e inclusión social de personas con discapacidad; en 2012, la ley que establece medidas contra la discriminación. "
     "Un argumento tiene una tesis, una razón y una evidencia. Un contraargumento responde a ese argumento. Un límite es lo que la evidencia no permite afirmar. "
     "Caso de ejemplo para debatir: «El Estado debe asegurar la accesibilidad en los edificios públicos». "
     "Datos de ejemplo: una municipalidad ficticia tiene 40 edificios públicos y 28 cuentan con rampa de acceso.")
build(
    OA, 6, F,
    use="Aprenderé a debatir sobre las demandas de derechos de grupos históricamente discriminados con argumentos, contraargumentos y límites, respetando a las personas.",
    prior=["Sé construir una tesis con evidencia y un límite.", "Sé que una ley no garantiza por sí sola su cumplimiento.", "Sé distinguir hechos y opiniones."],
    explain=[
        "Desde la recuperación democrática, grupos históricamente discriminados, como pueblos indígenas, personas con discapacidad y mujeres, han demandado derechos. Algunas respuestas fueron leyes, como las tres de la ficha. Una ley aprobada es un paso, pero no asegura por sí sola que el derecho se cumpla en la vida diaria.",
        "Debatir no es ganar discutiendo: es dar razones. Un argumento tiene tesis, razón y evidencia. El contraargumento responde con otra razón o con un límite, por ejemplo el costo o el plazo. Un buen debate reconoce lo que la otra postura aporta y no ataca a las personas.",
        "Un error frecuente es atacar a quien habla en vez de responder su razón, como decir «quienes piden eso solo buscan ventajas». Otro es generalizar con pocos datos. Una postura sólida usa datos, reconoce sus límites y propone una forma concreta de avanzar.",
    ],
    vocab=[("argumento", "afirmación apoyada en una razón y en evidencia"), ("contraargumento", "respuesta que se opone a un argumento con otra razón o con un límite"), ("accesibilidad", "condición que permite a todas las personas usar un lugar o servicio"), ("discriminación", "trato desigual e injusto hacia una persona o un grupo"), ("cumplimiento", "grado en que una norma se aplica en la práctica")],
    worked=[
        ("Reconocer la razón", "«Hay que poner ascensores en los consultorios porque algunas personas no pueden subir escaleras». ¿Cuál es la razón?",
         ["La tesis es poner ascensores.", "Lo que viene después de «porque» es la razón."], "Porque algunas personas no pueden subir escaleras"),
        ("Calcular una proporción", "Una municipalidad ficticia tiene 20 plazas y 15 tienen caminos accesibles. ¿Qué porcentaje cumple?",
         ["Divido 15 entre 20 y multiplico por 100.", "15 × 100 ÷ 20 = 75."], "75 %"),
    ],
    mistakes=[("Responder a un argumento atacando a quien lo dice.", "Se cambia el tema desde las razones hacia la persona.", "Responde la razón con otra razón o con un dato."),
              ("Creer que una ley aprobada resuelve el problema.", "Se confunde norma con cumplimiento.", "Pregunta cuánto se cumple y con qué datos se mide.")],
    T=[
        ("{F} ¿En qué año se aprobó la ley indígena mencionada en la ficha?", "1993", "La ficha lo indica."),
        ("{F} ¿Qué ley de la ficha es de 2012?", "La que establece medidas contra la discriminación", "Así lo dice la ficha."),
        ("{F} ¿Qué es un contraargumento?", "Una respuesta que se opone a un argumento con otra razón o con un límite", "Esa es la definición de la clase."),
        ("{F} ¿Qué grupo de la ficha tiene la ley más antigua de las tres? A) Los pueblos indígenas, con la ley de 1993 B) Las personas con discapacidad, con la ley de 2010", "A) Los pueblos indígenas, con la ley de 1993", "La ley indígena es de 1993; las otras son de 2010 y 2012."),
        ("{F} En «Hay que ampliar las rampas porque sin ellas algunas personas no pueden entrar a servicios públicos», ¿cuál es la razón? A) Porque sin ellas algunas personas no pueden entrar a servicios públicos B) Hay que ampliar las rampas", "A) Porque sin ellas algunas personas no pueden entrar a servicios públicos", "La razón va después de «porque»; lo otro es la tesis."),
        ("{F} Un compañero responde: «Las rampas cuestan, pero el gasto se reparte en varios años y evita excluir». ¿Qué hace? A) Responde con un contraargumento que reconoce el costo B) Cambia de tema", "A) Responde con un contraargumento que reconoce el costo", "Reconoce el costo y lo responde con otra razón."),
        ("=", "{F} En la municipalidad ficticia, ¿cuántos edificios públicos no tienen rampa de acceso?", "40-28", "Se resta el número con rampa al total.", " edificios"),
        ("{F} Alguien dice: «Quienes piden más derechos solo quieren ventajas». ¿Qué error de argumentación comete? A) Ataca las intenciones de las personas sin responder su razón B) Reconoce el costo de la propuesta", "A) Ataca las intenciones de las personas sin responder su razón", "No discute el argumento, sino a quienes lo plantean."),
        ("{F} ¿Qué ley de la ficha respalda un argumento sobre acceso a edificios públicos? A) La de 2010 sobre igualdad de oportunidades e inclusión social de personas con discapacidad B) La ley indígena de 1993", "A) La de 2010 sobre igualdad de oportunidades e inclusión social de personas con discapacidad", "Esa ley trata de la inclusión de personas con discapacidad."),
        ("{F} ¿Por qué una ley aprobada no garantiza que el derecho se cumpla en la vida diaria?", "Porque hace falta aplicarla, financiarla y revisar con datos si se cumple", "En la ficha, 12 de 40 edificios aún no cumplen aunque haya ley."),
        ("{F} Un debatiente dice: «Con los datos de una municipalidad no puedo afirmar lo mismo de todo el país». ¿Qué límite reconoce? A) Límite de generalización B) Límite de costo", "A) Límite de generalización", "Reconoce que los datos de un lugar no se extienden automáticamente al país."),
        ("{F} Redacta un argumento a favor, un contraargumento y un límite sobre «El Estado debe asegurar la accesibilidad en los edificios públicos».", "Respuesta modelo: A favor, sin accesibilidad algunas personas no pueden usar servicios públicos. Contra, la obra tiene costo y requiere plazos. Límite, los datos de una municipalidad no permiten hablar del país.", "Incluye argumento, contraargumento y límite."),
        ("{F} ¿Qué cierre respeta mejor la evidencia? A) Hay avances legales desde 1993, pero faltan datos para saber si se cumplen en todos los edificios B) Las leyes ya resolvieron la discriminación", "A) Hay avances legales desde 1993, pero faltan datos para saber si se cumplen en todos los edificios", "Reconoce avances y declara lo que no se sabe."),
    ],
    ctx=("En un debate de curso, un grupo defiende que se asigne más presupuesto a la accesibilidad en edificios públicos y otro pide esperar. ¿Cuál es una intervención respetuosa y documentada? A) «Entiendo el costo, pero en la municipalidad de ejemplo 12 de 40 edificios no tienen rampa; propongo hacerlo por etapas» B) «Ustedes no entienden nada»", "A) «Entiendo el costo, pero en la municipalidad de ejemplo 12 de 40 edificios no tienen rampa; propongo hacerlo por etapas»", "Reconoce la razón contraria, usa un dato y propone avanzar."),
    sc=[("¿Qué partes tiene un argumento?", "Una tesis, una razón y una evidencia", "Así se define en la ficha."),
        ("¿Cuál es un error de argumentación común?", "Atacar a la persona en vez de responder su razón", "Se explicó como error frecuente."),
        ("=", "Una ciudad ficticia tiene 50 paraderos y 35 tienen techo accesible. ¿Cuántos no lo tienen?", "50-35", "Se resta los que sí lo tienen al total.", " paraderos")],
    op=("Prepara una intervención de debate de cinco oraciones sobre la afirmación «El Estado debe asegurar la accesibilidad en los edificios públicos». Incluye tu tesis, una razón con un dato de la ficha, un contraargumento y cómo lo responderías, y un límite de tu evidencia. Usa un tono respetuoso. {F}",
        "Tesis: el Estado debe asegurar la accesibilidad. Razón: en la municipalidad ficticia 12 de 40 edificios no tienen rampa. Contraargumento: tiene costo. Respuesta: puede hacerse por etapas, empezando por los más usados. Límite: son datos de una sola municipalidad.",
        ["incluye tesis, razón, contraargumento y límite", "usa un dato de la ficha", "el tono es respetuoso"], ["texto de cinco oraciones"], ["atacar a las personas", "no incluir límite"],
        "Pide que diga qué argumento de la otra postura le parece más fuerte y por qué."),
    reinforce="Explica a alguien de tu casa la diferencia entre un argumento y un contraargumento con un ejemplo cotidiano.",
    extend="Elige una norma de tu colegio y escribe un argumento a favor y un contraargumento respetuoso.",
)

OA = "HI2M OA 22"

# ================================================================ OA 22, clase 1
F = ("Ficha 1 (hechos y definiciones). "
     "Los derechos humanos son los derechos que tiene toda persona por el hecho de ser persona. La Declaración Universal de Derechos Humanos fue adoptada por la Asamblea General de la ONU el 10 de diciembre de 1948. "
     "Características: universalidad (corresponden a todas las personas, sin distinción); indivisibilidad (no se pueden separar ni ordenar de mayor a menor importancia); "
     "interdependencia (el ejercicio de un derecho depende de que se respeten otros); imprescriptibilidad (no se pierden por el paso del tiempo). "
     "Actores: las personas, que son titulares de derechos; el Estado, que es garante, es decir, el que debe respetarlos y protegerlos; y organismos nacionales e internacionales que vigilan su cumplimiento.")
build(
    OA, 1, F,
    use="Aprenderé qué son los derechos humanos, cuáles son sus cuatro características y quiénes participan en su protección.",
    prior=["Sé que la ONU se creó después de la Segunda Guerra Mundial.", "Sé que en 1948 se adoptó la Declaración Universal de Derechos Humanos.", "Sé qué es una ley."],
    explain=[
        "Los derechos humanos son los que corresponden a toda persona por ser persona, sin importar su origen, sexo, religión u otra condición. No los entrega un gobierno: el Estado los reconoce y debe respetarlos y protegerlos. Por eso se dice que el Estado es el garante y las personas son las titulares de derechos.",
        "Tienen cuatro características. La universalidad dice que son para todas las personas. La indivisibilidad dice que no se pueden separar ni ordenar por importancia: los derechos civiles, políticos, económicos, sociales y culturales forman un conjunto. La interdependencia dice que el ejercicio de uno depende de otros, por ejemplo estudiar requiere salud y alimentación.",
        "La imprescriptibilidad dice que los derechos no se pierden por el paso del tiempo. Que un derecho sea universal no asegura que se cumpla igual en todos los lugares: el cumplimiento depende de instituciones, leyes y políticas. Por eso existe una institucionalidad nacional e internacional que se estudia en esta unidad.",
    ],
    vocab=[("universalidad", "característica por la que los derechos corresponden a todas las personas sin distinción"), ("indivisibilidad", "característica por la que los derechos no se separan ni se ordenan por importancia"), ("interdependencia", "característica por la que el ejercicio de un derecho depende de que se respeten otros"), ("imprescriptibilidad", "característica por la que los derechos no se pierden por el paso del tiempo"), ("garante", "quien debe respetar y proteger los derechos, en especial el Estado")],
    worked=[
        ("Identificar la característica", "«Un derecho tan básico como la salud no puede ser menos importante que otro». ¿Qué característica refleja?",
         ["Dice que no hay derechos más o menos importantes.", "Eso es no ordenarlos de mayor a menor importancia."], "Indivisibilidad"),
        ("Identificar titular y garante", "Una niña no puede ir al colegio porque no hay vacantes. ¿Quién es titular y quién garante del derecho a la educación?",
         ["La persona que tiene el derecho es la titular.", "El que debe asegurarlo es el Estado."], "Titular: la niña; garante: el Estado"),
    ],
    mistakes=[("Pensar que los derechos humanos los concede cada gobierno.", "Se confunde reconocer con otorgar.", "Recuerda que corresponden a toda persona por ser persona; el Estado los garantiza."),
              ("Confundir indivisibilidad con interdependencia.", "Ambas hablan de relación entre derechos.", "La indivisibilidad es que no se separan ni jerarquizan; la interdependencia, que unos dependen de otros.")],
    T=[
        ("{F} ¿Qué día y año se adoptó la Declaración Universal de Derechos Humanos?", "10 de diciembre de 1948", "La ficha lo indica."),
        ("{F} ¿Qué característica dice que los derechos corresponden a todas las personas sin distinción?", "La universalidad", "Esa es su definición en la ficha."),
        ("{F} ¿Quién es el garante de los derechos humanos?", "El Estado", "La ficha lo presenta como quien debe respetarlos y protegerlos."),
        ("{F} Alguien dice: «Mi derecho a estudiar depende de que también tenga salud y alimentación». ¿Qué característica ilustra? A) Interdependencia B) Imprescriptibilidad", "A) Interdependencia", "Un derecho depende de que se respeten otros."),
        ("{F} Alguien dice: «El derecho a votar es más importante que el derecho a la vivienda, así que solo defenderé el primero». ¿Qué característica contradice? A) Indivisibilidad B) Universalidad", "A) Indivisibilidad", "Los derechos no se ordenan por importancia."),
        ("{F} Alguien dice: «Pasó mucho tiempo, así que esa persona ya perdió sus derechos humanos». ¿Qué característica lo contradice? A) Imprescriptibilidad B) Interdependencia", "A) Imprescriptibilidad", "Los derechos no se pierden por el paso del tiempo."),
        ("{F} Un país niega derechos a las personas de otro pueblo por su origen. ¿Qué característica no respeta? A) Universalidad B) Indivisibilidad", "A) Universalidad", "Los derechos son para todas las personas sin distinción."),
        ("{F} ¿Qué ejemplo muestra mejor la interdependencia? A) Sin alimentación adecuada, un niño no puede aprovechar su derecho a la educación B) Todas las personas tienen derecho a la educación", "A) Sin alimentación adecuada, un niño no puede aprovechar su derecho a la educación", "Muestra un derecho que depende de que se respete otro; la B habla de universalidad."),
        ("{F} Una vecina denuncia que no recibe atención de salud. ¿Quién es la titular y quién el garante? A) Titular: la vecina; garante: el Estado B) Titular: el Estado; garante: la vecina", "A) Titular: la vecina; garante: el Estado", "La persona tiene el derecho y el Estado debe asegurarlo."),
        ("{F} ¿Por qué decir que los derechos son universales no significa que se cumplan igual en todos los países?", "Porque universal significa que corresponden a todas las personas, pero su cumplimiento depende de instituciones, leyes y políticas", "La ficha distingue tener un derecho de que se cumpla."),
        ("{F} ¿Cuál es la diferencia entre indivisibilidad e interdependencia? A) La primera dice que no se separan ni se ordenan por importancia; la segunda, que el ejercicio de unos depende de otros B) Son lo mismo con otro nombre", "A) La primera dice que no se separan ni se ordenan por importancia; la segunda, que el ejercicio de unos depende de otros", "Son características distintas con definiciones distintas."),
        ("{F} Escribe un ejemplo propio que muestre interdependencia entre dos derechos.", "Respuesta modelo: Para ejercer el derecho a la educación una niña necesita también el derecho a la salud, porque si está enferma no puede asistir al colegio.", "Muestra que un derecho necesita de otro."),
        ("¿Cuál es la mejor pregunta de investigación para este tema? A) ¿Cómo se organiza la protección de los derechos humanos desde 1948 y qué grupos requieren protección especial? B) ¿Los derechos humanos son buenos?", "A) ¿Cómo se organiza la protección de los derechos humanos desde 1948 y qué grupos requieren protección especial?", "La pregunta A tiene tiempo y se responde con hechos; la B es una opinión."),
    ],
    ctx=("En un afiche escolar se lee: «Los derechos humanos son un regalo del gobierno de turno». ¿Qué corrección corresponde? A) Corresponden a toda persona por ser persona y el Estado debe garantizarlos B) Cambiar «gobierno de turno» por «gobierno actual»", "A) Corresponden a toda persona por ser persona y el Estado debe garantizarlos", "El Estado reconoce y garantiza; no concede."),
    sc=[("¿Qué significa imprescriptibilidad?", "Que los derechos no se pierden por el paso del tiempo", "Es la definición de la ficha."),
        ("¿Qué es ser titular de derechos?", "Ser la persona a quien le corresponden los derechos", "El titular es la persona; el garante es el Estado."),
        ("En Historia: ¿qué característica dice que el ejercicio de un derecho depende de que se respeten otros?", "La interdependencia", "Así se define en el vocabulario de la clase.")],
    op=("Elige dos derechos (por ejemplo, educación y salud). Escribe una frase que muestre que son interdependientes, otra que muestre que son indivisibles y una tercera que diga quién es el titular y quién el garante en un caso ficticio que inventes. {F}",
        "Interdependencia: una niña enferma no puede asistir a clases. Indivisibilidad: no se puede decir que la salud importa más que la educación. Caso: Ana, titular, no tiene vacante en un colegio; el Estado es el garante.",
        ["las dos características están bien explicadas", "distingue titular y garante", "el caso es ficticio y claro"], ["tres frases escritas"], ["definir indivisibilidad como interdependencia", "poner al Estado como titular"],
        "Pide que diga qué institución podría ayudar si el derecho no se cumple."),
    reinforce="Explica a una persona de tu casa qué significa que los derechos humanos sean universales e imprescriptibles.",
    extend="Busca en tu comunidad una norma o lugar (una biblioteca, una escuela) que ayude a que se cumpla un derecho y di cuál.",
)

# ================================================================ OA 22, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo; no son documentos reales). "
     "Fuente A, resumen redactado para este cuaderno de la idea central de la Declaración Universal de 1948: todas las personas nacen libres e iguales en dignidad y derechos. "
     "Fuente B, informe de una organización ficticia, 2019: «En la comuna Épsilon, de 40 edificios públicos visitados, 12 no tenían acceso para sillas de ruedas.» "
     "Fuente C, nota de prensa de un ministerio ficticio, 2019: «El Estado cumplió todas las metas de inclusión.»")
build(
    OA, 2, F,
    use="Aprenderé a distinguir qué dice una fuente sobre cómo deben ser los derechos y qué dice sobre cómo se cumplen en la práctica, y a evaluar su procedencia.",
    prior=["Sé qué son los derechos humanos y sus cuatro características.", "Sé que una fuente tiene autor, fecha y propósito.", "Sé que un informe puede medir y un aviso puede persuadir."],
    explain=[
        "Hay fuentes que dicen cómo deben ser los derechos y fuentes que cuentan cómo se cumplen. Un texto como la Declaración Universal es normativo: declara lo que debe ser. Un informe de observación mide lo que ocurre en la práctica. Confundir ambas cosas lleva a creer que un derecho declarado ya se cumple.",
        "Una nota de prensa de una institución puede ser útil, pero esa institución quiere mostrar sus logros. Que una fuente sea oficial no la hace falsa, pero tampoco prueba por sí sola lo que afirma. Se contrasta con otra fuente independiente que haya observado o medido.",
        "Todo informe también tiene límites: si visitó 40 edificios de una comuna, no dice nada de todo el país. Al interrogar una fuente se pregunta quién la hizo, cuándo, cómo reunió sus datos y para qué. Con eso se decide qué conclusión permite y cuál no.",
    ],
    vocab=[("fuente normativa", "documento que declara cómo deben ser las cosas, como una declaración de derechos"), ("fuente de observación", "documento que registra lo que se midió o se vio en la práctica"), ("fuente oficial", "documento producido por una institución del Estado"), ("muestra", "parte de los casos que se estudia para describir el conjunto"), ("contrastar", "comparar una fuente con otra independiente para comprobar lo que dice")],
    worked=[
        ("Normativa u observación", "Un decreto ficticio dice: «Todos los colegios deberán tener baños accesibles». ¿Qué tipo de fuente es?",
         ["Dice cómo deben ser los colegios.", "No mide cuántos cumplen."], "Fuente normativa"),
        ("Leer una muestra", "Una organización visitó 25 plazas de ejemplo y 5 no tenían rampa. ¿Qué fracción no tenía rampa?",
         ["Comparo los casos sin rampa con el total visitado.", "5 de 25 es 1 de 5."], "1 de cada 5 plazas visitadas"),
    ],
    mistakes=[("Usar una declaración de derechos como prueba de que se cumplen.", "Se confunde lo que debe ser con lo que ocurre.", "Busca una fuente de observación que mida el cumplimiento."),
              ("Desconfiar de una fuente solo porque es oficial.", "Se reemplaza el análisis por una sospecha.", "Revisa su propósito y contrástala.")],
    T=[
        ("{F} ¿Qué idea central resume la Fuente A?", "Que todas las personas nacen libres e iguales en dignidad y derechos", "Es el contenido de la Fuente A."),
        ("{F} Según la Fuente B, ¿cuántos edificios no tenían acceso para sillas de ruedas?", "12", "El informe lo indica."),
        ("{F} ¿Quién emite la Fuente C?", "Un ministerio, es decir, una institución del Estado", "Es una nota de prensa de un ministerio."),
        ("=", "{F} Según la Fuente B, ¿cuántos de los 40 edificios visitados sí tenían acceso para sillas de ruedas?", "40-12", "Se resta los edificios sin acceso al total visitado.", " edificios"),
        ("{F} La Fuente A es un documento que... A) declara cómo deben ser los derechos B) mide cuántos derechos se cumplen", "A) declara cómo deben ser los derechos", "Es una declaración, es decir, una fuente normativa."),
        ("{F} ¿Por qué conviene contrastar la Fuente C con otra? A) El ministerio puede querer mostrar sus logros y no entrega datos B) Porque es de un ministerio y por eso es falsa", "A) El ministerio puede querer mostrar sus logros y no entrega datos", "Una fuente oficial no es falsa por serlo, pero tiene un propósito y no presenta datos."),
        ("{F} Quieres saber si en la comuna Épsilon se cumple el acceso a edificios públicos. ¿Qué fuente usas primero? A) La Fuente B B) La Fuente A", "A) La Fuente B", "Es la que mide el acceso en edificios de una comuna."),
        ("{F} Un compañero cita la Fuente A para probar que todos los derechos se cumplen. ¿Qué error comete? A) Confunde lo que el documento declara con lo que ocurre en la práctica B) Usó el año equivocado", "A) Confunde lo que el documento declara con lo que ocurre en la práctica", "Una declaración no prueba cumplimiento."),
        ("=", "{F} ¿Qué porcentaje de los edificios visitados no tenía acceso para sillas de ruedas?", "12*100/40", "Se divide 12 entre 40 y se multiplica por 100.", " %"),
        ("{F} ¿Qué pregunta de procedencia es útil para la Fuente B? A) ¿Cómo eligió la organización los edificios que visitó? B) ¿Cuántas sillas de ruedas hay en el país?", "A) ¿Cómo eligió la organización los edificios que visitó?", "Pregunta por cómo reunió sus datos; la B pide un dato que la fuente no entrega."),
        ("{F} La Fuente B visitó 40 edificios. ¿Qué límite tiene su conclusión? A) Solo describe 40 edificios de una comuna, no todo el país B) Es de 2019", "A) Solo describe 40 edificios de una comuna, no todo el país", "Una muestra de una comuna no permite hablar de todo el país."),
        ("{F} Escribe una conclusión que use las Fuentes B y C sin exagerar.", "Respuesta modelo: Un informe de 2019 encontró 12 de 40 edificios sin acceso en la comuna Épsilon, y un ministerio afirmó que cumplió todas sus metas; hacen falta datos para comparar ambas afirmaciones.", "Reconoce las dos fuentes y señala que se deben contrastar."),
        ("{F} ¿Qué haría más confiable la conclusión sobre el acceso en edificios públicos? A) Buscar otra fuente independiente que también observe los edificios B) Repetir la nota del ministerio", "A) Buscar otra fuente independiente que también observe los edificios", "La independencia permite contrastar."),
    ],
    ctx=("Una alcaldía ficticia publica: «Nuestra comuna respeta todos los derechos». ¿Qué evidencia pedirías para evaluar esa frase? A) Un informe que mida el cumplimiento de derechos concretos, como el acceso a servicios B) Otra frase de la misma alcaldía", "A) Un informe que mida el cumplimiento de derechos concretos, como el acceso a servicios", "Una afirmación general necesita datos de cumplimiento."),
    sc=[("¿Qué es una fuente normativa?", "Un documento que declara cómo deben ser las cosas", "Así se define en la clase."),
        ("¿Por qué una muestra tiene límites?", "Porque solo describe los casos estudiados y no todo el conjunto", "No permite hablar de todo el país."),
        ("=", "Una organización ficticia visitó 60 escuelas y 18 no tenían rampa. ¿Cuántas tenían rampa?", "60-18", "Se resta las escuelas sin rampa al total.", " escuelas")],
    op=("Lee estas fuentes de ejemplo. Fuente 1, ley ficticia: «Todos los servicios públicos deben ser accesibles». Fuente 2, informe ficticio de una organización, 2020: «De 30 oficinas visitadas, 9 no eran accesibles». Fuente 3, nota ficticia de una oficina pública, 2020: «Todas nuestras oficinas son accesibles». Para cada una anota si es normativa, de observación u oficial con interés, y qué puede o no probar. Después escribe una conclusión de dos oraciones.",
        "Fuente 1: normativa; dice cómo debe ser, no si se cumple. Fuente 2: de observación; prueba que 9 de 30 oficinas visitadas no eran accesibles. Fuente 3: oficial; hay que contrastarla. Conclusión: la ley exige accesibilidad y un informe encontró 9 de 30 oficinas sin ella en 2020; la nota de la oficina debe contrastarse con otra fuente.",
        ["clasifica bien cada fuente", "indica lo que puede y no puede probar", "la conclusión usa las tres sin exagerar"], ["tabla de tres fuentes", "conclusión de dos oraciones"], ["usar la ley como prueba de cumplimiento", "decir que la nota es falsa sin contrastarla"],
        "Pide que diga qué otra fuente buscaría para comprobar si se cumple el acceso."),
    reinforce="Explica con tus palabras la diferencia entre una fuente que dice cómo deben ser los derechos y otra que mide cómo se cumplen.",
    extend="Anota un cartel o norma de tu colegio que diga cómo debe ser algo y cómo comprobarías si realmente se cumple.",
)

# ================================================================ OA 22, clase 3
F = ("Ficha 3 (instituciones de protección de los derechos humanos; funciones generales). "
     "Escala nacional: los tribunales de justicia; el recurso de protección, que se presenta ante una Corte de Apelaciones cuando un acto o una omisión priva, perturba o amenaza ciertos derechos que la Constitución garantiza; "
     "el Instituto Nacional de Derechos Humanos, organismo autónomo que promueve y protege los derechos humanos; la Defensoría de la Niñez, que defiende y promueve los derechos de niños, niñas y adolescentes. "
     "Escala internacional: la ONU, creada en 1945; la Comisión Interamericana de Derechos Humanos, que recibe denuncias y hace recomendaciones a los Estados de las Américas; "
     "la Corte Interamericana de Derechos Humanos, con sede en San José de Costa Rica, que juzga si un Estado violó la Convención Americana, siempre que ese Estado haya aceptado su competencia; "
     "la Corte Penal Internacional, con sede en La Haya, que juzga a personas acusadas de genocidio, crímenes de lesa humanidad y crímenes de guerra. "
     "Regla general: se recurre primero a las instancias nacionales y, si no responden, a las internacionales.")
build(
    OA, 3, F,
    use="Aprenderé a comparar las instituciones nacionales e internacionales que protegen los derechos humanos, sus funciones y sus límites.",
    prior=["Sé qué son los derechos humanos y quiénes participan en su protección.", "Sé que la ONU se creó después de la Segunda Guerra.", "Sé distinguir escalas: país y mundo."],
    explain=[
        "La protección de los derechos humanos funciona en dos escalas. En Chile, los tribunales de justicia resuelven casos y el recurso de protección permite pedir a una Corte de Apelaciones que ampare un derecho amenazado. Además existen organismos como el Instituto Nacional de Derechos Humanos y la Defensoría de la Niñez.",
        "A escala internacional hay instituciones que actúan cuando las instancias nacionales no responden. La Comisión Interamericana recibe denuncias y hace recomendaciones; la Corte Interamericana juzga a Estados que aceptaron su competencia; la Corte Penal Internacional juzga a personas acusadas de crímenes muy graves. Cada una tiene una función distinta.",
        "Comparar escalas ayuda a ver ventajas y límites. Las instituciones nacionales están más cerca de las personas. Las internacionales dependen de la aceptación de los Estados. También conviene comparar perspectivas: la víctima busca reparación, el Estado defiende sus procedimientos y un organismo observa. Ante una situación de riesgo para una persona menor de edad, lo primero es avisar a una persona adulta de confianza.",
    ],
    vocab=[("recurso de protección", "acción que se presenta ante una Corte de Apelaciones para amparar derechos garantizados por la Constitución"), ("competencia", "facultad de un tribunal para resolver ciertos casos"), ("denuncia", "aviso formal de que se violó un derecho"), ("recomendación", "propuesta que se hace a un Estado, sin ser una sentencia"), ("crimen de lesa humanidad", "crimen muy grave cometido de forma sistemática contra población civil")],
    worked=[
        ("Elegir la institución", "Un Estado fue acusado de violar la Convención Americana y se busca una sentencia. ¿Qué órgano la dicta?",
         ["Se necesita un tribunal.", "El tribunal interamericano es la Corte Interamericana."], "La Corte Interamericana de Derechos Humanos"),
        ("Distinguir escalas", "El recurso de protección ¿es de escala nacional o internacional?",
         ["Se presenta ante una Corte de Apelaciones de Chile.", "Las Cortes de Apelaciones son nacionales."], "Nacional"),
    ],
    mistakes=[("Creer que la Comisión Interamericana dicta sentencias.", "Se confunde una comisión con un tribunal.", "La Comisión recibe denuncias y recomienda; la Corte juzga."),
              ("Creer que la Corte Penal Internacional juzga a Estados.", "Se confunde con la Corte Interamericana.", "La Corte Penal Internacional juzga a personas.")],
    T=[
        ("{F} ¿Qué institución de la ficha defiende y promueve los derechos de la niñez?", "La Defensoría de la Niñez", "La ficha lo indica."),
        ("{F} ¿Dónde tiene sede la Corte Interamericana de Derechos Humanos?", "En San José de Costa Rica", "La ficha lo indica."),
        ("{F} ¿A quiénes juzga la Corte Penal Internacional?", "A personas acusadas de genocidio, crímenes de lesa humanidad y crímenes de guerra", "La ficha lo indica."),
        ("{F} Una persona quiere pedir a una Corte de Apelaciones que ampare un derecho amenazado. ¿Qué herramienta usa? A) Recurso de protección B) Comisión Interamericana", "A) Recurso de protección", "El recurso de protección se presenta ante una Corte de Apelaciones."),
        ("{F} ¿Qué órgano juzga si un Estado violó la Convención Americana? A) La Corte Interamericana B) El Instituto Nacional de Derechos Humanos", "A) La Corte Interamericana", "Es el tribunal interamericano; el Instituto no juzga."),
        ("{F} ¿Cuál institución es de escala internacional? A) La Comisión Interamericana B) El recurso de protección", "A) La Comisión Interamericana", "La Comisión actúa en las Américas; el recurso es nacional."),
        ("{F} ¿Cuál es la diferencia correcta entre la Comisión y la Corte Interamericanas? A) La Comisión recibe denuncias y recomienda; la Corte juzga B) La Corte recibe denuncias y la Comisión juzga", "A) La Comisión recibe denuncias y recomienda; la Corte juzga", "La ficha asigna a cada una una función distinta."),
        ("{F} Una institución internacional solo puede juzgar a los Estados que aceptaron su competencia. ¿Qué límite muestra? A) Depende de la aceptación de los Estados B) Solo juzga a personas", "A) Depende de la aceptación de los Estados", "La ficha dice que la Corte Interamericana juzga siempre que el Estado haya aceptado su competencia."),
        ("{F} Un tribunal nacional resuelve un caso en una ciudad y la Corte Penal Internacional uno de genocidio. ¿Qué diferencia de escala y de acusados hay?", "El tribunal nacional actúa dentro del país; la Corte Penal Internacional juzga a personas acusadas de crímenes muy graves y tiene sede en La Haya", "Compara la escala y a quiénes juzga cada una."),
        ("{F} La víctima busca reparación, el Estado defiende sus procedimientos y un organismo observa. ¿Por qué conviene considerar las tres perspectivas? A) Para comprender cada punto de vista y contrastar evidencias B) Para decidir que el Estado siempre tiene razón", "A) Para comprender cada punto de vista y contrastar evidencias", "Comparar perspectivas permite contrastar lo que dice cada actor."),
        ("{F} Una persona denuncia que se violó un derecho suyo y ningún tribunal chileno respondió. ¿Ante qué institución internacional de la ficha puede presentar una denuncia? A) La Comisión Interamericana de Derechos Humanos B) La Corte Penal Internacional", "A) La Comisión Interamericana de Derechos Humanos", "La Comisión recibe denuncias; la Corte Penal Internacional juzga a personas por crímenes muy graves."),
        ("{F} ¿Qué orden de recursos es más lógico? A) Primero las instancias nacionales y, si no responden, las internacionales B) Primero la Corte Penal Internacional", "A) Primero las instancias nacionales y, si no responden, las internacionales", "Es la regla general de la ficha."),
        ("{F} Un adolescente ficticio cuenta que en su casa lo maltratan. ¿Cuál es el primer paso correcto? A) Avisar a una persona adulta de confianza B) Esperar a que pase", "A) Avisar a una persona adulta de confianza", "Ante riesgo, un adolescente debe avisar a un adulto de confianza y no guardar el secreto."),
    ],
    ctx=("Una comuna ficticia no responde a un reclamo por un derecho. ¿Qué camino sigue la regla general de la ficha? A) Usar las instancias nacionales y, si no responden, acudir a las internacionales B) Ir directamente a la Corte Penal Internacional", "A) Usar las instancias nacionales y, si no responden, acudir a las internacionales", "La Corte Penal Internacional juzga crímenes muy graves, no cualquier reclamo."),
    sc=[("¿Qué hace la Comisión Interamericana?", "Recibe denuncias y hace recomendaciones a los Estados", "Esa es su función en la ficha."),
        ("¿Qué es el recurso de protección?", "Una acción ante una Corte de Apelaciones para amparar derechos garantizados por la Constitución", "Así se describe en la ficha."),
        ("¿La Corte Penal Internacional juzga a Estados o a personas?", "A personas", "Juzga a personas acusadas de crímenes muy graves.")],
    op=("Construye una tabla con dos columnas, «Nacional» e «Internacional». En cada una escribe las instituciones de la ficha que correspondan y, al lado, una frase con su función. Luego escribe un caso ficticio de tres líneas, sin datos personales, en que se use primero una institución nacional y después una internacional. {F}",
        "Nacional: tribunales, recurso de protección, Instituto Nacional de Derechos Humanos, Defensoría de la Niñez. Internacional: ONU, Comisión Interamericana, Corte Interamericana, Corte Penal Internacional. Caso: un reclamo no se resuelve en un tribunal chileno y se presenta una denuncia ante la Comisión Interamericana.",
        ["ubica bien las instituciones", "describe una función correcta para cada una", "el caso respeta la regla de recurrir primero a lo nacional"], ["tabla de dos columnas", "caso de tres líneas"], ["poner la Corte Penal Internacional como institución nacional", "juntar las funciones de comisión y corte"],
        "Pide que explique por qué las instituciones internacionales no reemplazan a las nacionales."),
    reinforce="Explica con tus palabras la diferencia entre una institución que recomienda y una que juzga.",
    extend="Averigua en tu casa quién podría ayudarte si alguien no respetara un derecho tuyo y a qué institución se acudiría después.",
)

# ================================================================ OA 22, clase 4
F = ("Ficha 4 (causas, cambios y continuidades; hechos). "
     "Causas: la Segunda Guerra Mundial y los crímenes contra población civil llevaron a crear la ONU en 1945 y a adoptar la Declaración Universal en 1948. "
     "Ampliaciones posteriores: Convención sobre la eliminación de todas las formas de discriminación contra la mujer, 1979; Convención sobre los Derechos del Niño, 1989; "
     "Convención sobre los Derechos de las Personas con Discapacidad, 2006; Declaración de las Naciones Unidas sobre los derechos de los pueblos indígenas, 2007. "
     "Cambio: los derechos pasaron de depender solo de las leyes de cada país a tener también normas internacionales. "
     "Continuidad: aún hay discriminación y casos en que los derechos no se cumplen.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar por qué surgió el sistema de derechos humanos, qué cambió con las nuevas convenciones y qué problemas continúan.",
    prior=["Sé qué son los derechos humanos y quién los garantiza.", "Sé distinguir cambio y continuidad.", "Sé que un hecho tiene varias causas."],
    explain=[
        "Después de la Segunda Guerra Mundial, la gravedad de los crímenes contra población civil impulsó a los países a acordar normas comunes. Así nacieron la ONU, en 1945, y la Declaración Universal de Derechos Humanos, en 1948. La guerra fue una causa importante, pero no la única: también influyó la experiencia de muchas personas que exigían protección.",
        "Con los años se vio que una declaración general no bastaba para proteger a quienes sufrían más discriminación. Por eso se adoptaron convenciones sobre las mujeres, la niñez, las personas con discapacidad y los pueblos indígenas. Una convención es un tratado que obliga a los Estados que lo aceptan.",
        "El cambio principal fue que los derechos pasaron de depender solo de las leyes de cada país a tener también normas internacionales. La continuidad es que todavía hay discriminación y derechos que no se cumplen. Una norma nueva no prueba que la situación haya mejorado: se necesitan datos de antes y después.",
    ],
    vocab=[("convención", "tratado que obliga a los Estados que lo aceptan"), ("ampliación de derechos", "reconocimiento de protecciones para grupos que antes tenían menos"), ("causa", "hecho que ayuda a explicar otro"), ("continuidad", "aspecto que se mantiene pese al paso del tiempo"), ("tratado", "acuerdo escrito entre Estados")],
    worked=[
        ("Calcular un intervalo", "Una convención de ejemplo se adoptó en 1966 y otra en 1992. ¿Cuántos años separan ambas?",
         ["Resto los años.", "1992 − 1966 = 26."], "26 años"),
        ("Clasificar", "Que un colegio de ejemplo siga sin matricular a un grupo pese a existir una convención, ¿es cambio o continuidad?",
         ["Se mantiene una exclusión.", "La norma cambió, pero la práctica no."], "Continuidad"),
    ],
    mistakes=[("Pensar que la Declaración de 1948 resolvió la discriminación.", "Se confunde adopción de normas con cumplimiento.", "Distingue la norma y los datos sobre su cumplimiento."),
              ("Explicar el sistema de derechos humanos solo por la guerra.", "Se ignora la multicausalidad.", "Menciona también la experiencia de las personas que exigían protección y la necesidad de normas comunes.")],
    T=[
        ("{F} ¿Qué hecho de los años cuarenta impulsó la creación de la ONU y de la Declaración Universal?", "La Segunda Guerra Mundial y los crímenes contra población civil", "La ficha lo presenta como la causa principal."),
        ("{F} ¿En qué año se adoptó la Convención sobre los Derechos del Niño?", "1989", "La ficha lo indica."),
        ("{F} ¿En qué año se adoptó la convención sobre la eliminación de la discriminación contra la mujer?", "1979", "La ficha lo indica."),
        ("{F} ¿Cuál de las convenciones de la ficha se adoptó primero? A) La de la discriminación contra la mujer B) La de los derechos del niño", "A) La de la discriminación contra la mujer", "La de la mujer es de 1979 y la del niño, de 1989."),
        ("{F} Antes de 1948 muchas protecciones dependían solo de las leyes de cada país y después aparece una declaración internacional. ¿Qué es eso? A) Un cambio B) Una continuidad", "A) Un cambio", "Pasar a tener normas internacionales es el cambio principal de la ficha."),
        ("{F} Hoy siguen existiendo casos de discriminación pese a las convenciones. ¿Qué es eso? A) Una continuidad B) Un cambio", "A) Una continuidad", "La discriminación persiste pese a las normas."),
        ("{F} ¿Qué orden cronológico es correcto? A) ONU (1945), Declaración Universal (1948), Convención sobre los Derechos del Niño (1989) B) Convención sobre los Derechos del Niño (1989), ONU (1945), Declaración Universal (1948)", "A) ONU (1945), Declaración Universal (1948), Convención sobre los Derechos del Niño (1989)", "La ficha fecha los hitos en ese orden."),
        ("{F} ¿Por qué se crearon convenciones específicas para ciertos grupos? A) Porque una declaración general no bastaba para proteger a quienes sufrían más discriminación B) Porque la Declaración solo rige en los países que ganaron la guerra", "A) Porque una declaración general no bastaba para proteger a quienes sufrían más discriminación", "Las convenciones responden a esa necesidad."),
        ("{F} ¿Qué convención de la ficha se adoptó después de 2000? A) La de las personas con discapacidad B) La del niño", "A) La de las personas con discapacidad", "Es de 2006; la del niño es de 1989."),
        ("{F} ¿Por qué una declaración de derechos no basta para afirmar que la situación de un grupo mejoró?", "Porque una norma no prueba el cumplimiento y se necesitan datos de antes y después", "La ficha distingue norma y práctica."),
        ("{F} Quieres sostener que las convenciones mejoraron la situación de un grupo. ¿Qué evidencia necesitas? A) Datos de antes y después sobre su situación B) La fecha de adopción de la convención", "A) Datos de antes y después sobre su situación", "La fecha solo prueba la norma, no el efecto."),
        ("{F} Escribe una oración que una un cambio, una continuidad y una causa del sistema de derechos humanos.", "Respuesta modelo: Tras la Segunda Guerra surgió la Declaración Universal y luego convenciones para varios grupos, aunque la discriminación continúa en muchos lugares.", "Une una causa, un cambio y una continuidad."),
        ("{F} ¿Cuál es la conclusión más proporcional? A) Desde 1948 se ampliaron las normas de protección, pero persisten problemas de cumplimiento B) Desde 1948 ya no hay discriminación", "A) Desde 1948 se ampliaron las normas de protección, pero persisten problemas de cumplimiento", "Incluye cambio y continuidad sin exagerar."),
    ],
    ctx=("Un compañero dice: «Como existe la Convención sobre los Derechos del Niño, ningún niño sufre vulneraciones». ¿Qué respondes? A) Que la convención es una norma, y el cumplimiento se mide con datos y puede fallar B) Que tiene razón, porque los tratados se cumplen solos en todos los casos", "A) Que la convención es una norma, y el cumplimiento se mide con datos y puede fallar", "Distingue norma y práctica."),
    sc=[("¿Qué es una convención?", "Un tratado que obliga a los Estados que lo aceptan", "Así se define en la clase."),
        ("¿Qué es una continuidad?", "Algo que se mantiene pese al paso del tiempo", "Es lo contrario de un cambio."),
        ("En Historia: ¿qué es un tratado?", "Un acuerdo escrito entre Estados", "Así se define en el vocabulario de la clase.")],
    op=("Dibuja una línea de tiempo con 1945, 1948, 1979, 1989, 2006 y 2007, y escribe junto a cada año el hecho de la ficha. Debajo escribe tres frases: una causa del sistema de derechos humanos, un cambio y una continuidad. {F}",
        "1945 creación de la ONU; 1948 Declaración Universal; 1979 convención sobre la mujer; 1989 convención sobre el niño; 2006 convención sobre personas con discapacidad; 2007 declaración sobre pueblos indígenas. Causa: la Segunda Guerra. Cambio: normas internacionales. Continuidad: la discriminación persiste.",
        ["ubica bien los seis hitos", "distingue causa, cambio y continuidad", "no afirma que ya no hay discriminación"], ["línea de tiempo", "tres frases"], ["poner un hito en el año equivocado", "decir que el cambio eliminó el problema"],
        "Pide que explique qué datos necesitaría para saber si una convención mejoró la situación de un grupo."),
    reinforce="Explica a una persona de tu casa por qué se adoptaron convenciones para ciertos grupos además de la Declaración Universal.",
    extend="Escribe una pregunta que le harías a una persona mayor sobre cómo cambió el trato hacia la niñez desde que ella era joven.",
)

# ================================================================ OA 22, clase 5
F = ("Ficha 5 (grupos de especial protección; casos ficticios). "
     "Grupos de especial protección son personas que, por su situación, tienen mayor riesgo de discriminación o de vulneración de sus derechos: niñas, niños y adolescentes; mujeres; personas con discapacidad; pueblos indígenas; personas migrantes; personas mayores. "
     "Instrumentos: Convención sobre los Derechos del Niño (1989); convención sobre la discriminación contra la mujer (1979); Convención sobre los Derechos de las Personas con Discapacidad (2006); Declaración de la ONU sobre los derechos de los pueblos indígenas (2007). "
     "En Chile, la ley de 2010 trata la igualdad de oportunidades de las personas con discapacidad. "
     "Las medidas de protección especial buscan igualar condiciones, no dar privilegios. "
     "Caso ficticio: Ana usa silla de ruedas y la sala de su colegio está en un segundo piso sin ascensor. "
     "Dato de ejemplo: el 15 % de los 120 estudiantes de un colegio ficticio necesita apoyos para aprender.")
build(
    OA, 5, F,
    use="Aprenderé a explicar por qué algunos grupos requieren protección especial y a escribir una interpretación con tesis, evidencia y límite sobre un caso ficticio.",
    prior=["Sé qué son las convenciones y para qué sirven.", "Sé escribir una tesis con evidencia.", "Sé que la igualdad no siempre es trato idéntico."],
    explain=[
        "Los grupos de especial protección son personas que, por su situación, tienen más riesgo de ser discriminadas o de ver vulnerados sus derechos. Entre ellos están niñas, niños y adolescentes, mujeres, personas con discapacidad, pueblos indígenas, personas migrantes y personas mayores. No tienen más derechos que otras personas: necesitan medidas adicionales para ejercer los mismos.",
        "Dar el mismo trato idéntico a todos puede mantener desigualdades. Si la sala de Ana está en un segundo piso sin ascensor, tratarla igual que a los demás la deja sin acceso. Un ascensor o una sala en el primer piso igualan condiciones. Eso se llama igualdad real: asegurar que cada persona pueda ejercer su derecho.",
        "Para interpretar un caso se escribe una tesis, se busca evidencia y se declara un límite. Para pueblos indígenas, las formas tradicionales de cada pueblo las explican su comunidad o un educador o educadora tradicional. Si una persona menor de edad sufre maltrato, debe avisar a una persona adulta de confianza y no guardar el secreto.",
    ],
    vocab=[("grupo de especial protección", "personas con mayor riesgo de discriminación o vulneración de derechos que requieren medidas adicionales"), ("igualdad real", "asegurar que cada persona pueda ejercer sus derechos en la práctica, no solo en la ley"), ("vulneración", "daño o falta de respeto a un derecho"), ("medida de protección", "acción para que un derecho pueda ejercerse en condiciones iguales"), ("inclusión", "acceso de todas las personas a los espacios y servicios en condiciones iguales")],
    worked=[
        ("Reconocer una medida", "Un colegio de ejemplo instala una rampa para un estudiante con muletas. ¿Es un privilegio o una medida que iguala condiciones?",
         ["La rampa permite el mismo acceso a la sala.", "No da una ventaja sobre los demás."], "Una medida que iguala condiciones"),
        ("Calcular un porcentaje", "En un colegio ficticio de 200 estudiantes, el 10 % necesita apoyos. ¿Cuántos son?",
         ["Calculo 10 % de 200.", "200 × 10 ÷ 100 = 20."], "20 estudiantes"),
    ],
    mistakes=[("Creer que la protección especial es un privilegio.", "Se confunde igualar condiciones con dar ventajas.", "Pregunta si la medida permite ejercer el mismo derecho que los demás."),
              ("Tratar a todas las personas de forma idéntica y creer que eso es siempre justo.", "No se considera que las condiciones de partida son distintas.", "Evalúa si el trato idéntico mantiene una desigualdad.")],
    T=[
        ("{F} ¿Qué convención de la ficha protege a niñas, niños y adolescentes?", "La Convención sobre los Derechos del Niño", "La ficha la nombra entre los instrumentos."),
        ("{F} ¿En qué año se adoptó la Declaración de la ONU sobre los derechos de los pueblos indígenas?", "2007", "La ficha lo indica."),
        ("{F} ¿Qué trata la ley chilena de 2010 mencionada en la ficha?", "La igualdad de oportunidades de las personas con discapacidad", "La ficha lo indica."),
        ("{F} ¿Por qué se llaman grupos de especial protección? A) Porque tienen mayor riesgo de discriminación o vulneración y requieren medidas adicionales B) Porque tienen más derechos que otras personas", "A) Porque tienen mayor riesgo de discriminación o vulneración y requieren medidas adicionales", "La protección especial no crea más derechos, sino condiciones para ejercerlos."),
        ("{F} Ana usa silla de ruedas y su sala está en un segundo piso sin ascensor. ¿Qué derecho se ve afectado? A) La educación en igualdad de condiciones B) El derecho a votar", "A) La educación en igualdad de condiciones", "No puede acceder a su sala como los demás."),
        ("{F} Instalar un ascensor para Ana es... A) una medida para igualar condiciones de acceso B) un privilegio injusto", "A) una medida para igualar condiciones de acceso", "Le permite ejercer el mismo derecho que sus compañeros."),
        ("=", "{F} ¿Cuántos estudiantes necesitan apoyos en el colegio ficticio de 120 estudiantes?", "120*15/100", "Se calcula el 15 % de 120.", " estudiantes"),
        ("{F} Una niña ficticia cuenta que un adulto la maltrata en su casa. ¿Qué respuesta de apoyo es adecuada? A) Aconsejarle avisar a una persona adulta de confianza, sin guardar el secreto B) Pedirle que no lo cuente", "A) Aconsejarle avisar a una persona adulta de confianza, sin guardar el secreto", "Ante riesgo, se avisa a un adulto de confianza; el secreto la mantiene en peligro."),
        ("{F} Una comunidad indígena ficticia pide que su educación respete su cultura. ¿Qué principio se relaciona? A) Reconocer la diversidad cultural como parte de la igualdad B) Enseñar a todos exactamente igual, sin considerar su cultura, porque la igualdad es trato idéntico", "A) Reconocer la diversidad cultural como parte de la igualdad", "La protección de los pueblos indígenas incluye su cultura; sus formas tradicionales las explican su comunidad o su educador tradicional."),
        ("{F} ¿Por qué dar el mismo trato idéntico a todas las personas puede mantener desigualdades?", "Porque no considera que algunas personas parten de condiciones distintas y necesitan medidas para ejercer el mismo derecho", "Con la sala de Ana, el trato idéntico la deja sin acceso."),
        ("{F} ¿Qué evidencia respalda mejor que un colegio protege a sus estudiantes con discapacidad? A) Registro de rampas, apoyos y asistencia de esos estudiantes B) Un cartel con la palabra inclusión", "A) Registro de rampas, apoyos y asistencia de esos estudiantes", "Los datos de la práctica prueban más que una palabra."),
        ("{F} Escribe una tesis, una evidencia y un límite sobre el caso de Ana.", "Respuesta modelo: Tesis: el colegio no asegura la igualdad real de Ana. Evidencia: su sala está en un segundo piso sin ascensor. Límite: el caso es ficticio y no permite generalizar a todos los colegios.", "Incluye las tres partes y limita la conclusión."),
        ("{F} ¿Cuál afirmación es más proporcional? A) El colegio de Ana, con una sala sin ascensor, no asegura su acceso en igualdad de condiciones B) Ningún colegio de Chile respeta los derechos de las personas con discapacidad", "A) El colegio de Ana, con una sala sin ascensor, no asegura su acceso en igualdad de condiciones", "Se apoya en el caso y no generaliza a todo el país."),
    ],
    ctx=("Un colegio de ejemplo pone un cartel que dice «Aquí somos inclusivos», pero no tiene rampas ni apoyos. ¿Cómo evaluarías su cumplimiento? A) Con datos de accesos, apoyos y asistencia, no con el cartel B) Con lo que dice el cartel, porque es una declaración pública", "A) Con datos de accesos, apoyos y asistencia, no con el cartel", "El cumplimiento se mide en la práctica."),
    sc=[("¿Qué es un grupo de especial protección?", "Personas con mayor riesgo de discriminación o vulneración que requieren medidas adicionales", "Así se define en la clase."),
        ("¿Una medida de protección especial es un privilegio?", "No, busca igualar condiciones para ejercer los mismos derechos", "Así se explica en la clase."),
        ("=", "En un colegio ficticio de 80 estudiantes, el 25 % necesita apoyos. ¿Cuántos son?", "80*25/100", "Se calcula el 25 % de 80.", " estudiantes")],
    op=("Elige uno de estos casos ficticios: (a) un adulto mayor que no puede usar una aplicación para pedir su hora de salud, (b) una persona migrante que no entiende los formularios de un trámite, (c) Ana y su sala sin ascensor. Escribe una tesis, una evidencia del caso, una medida que igualaría condiciones y un límite. No uses datos personales reales. {F}",
        "Caso (a): tesis, el servicio no asegura el acceso a una persona mayor; evidencia, solo ofrece horas por una aplicación; medida, atención telefónica o presencial; límite, el caso es ficticio y no permite generalizar a todos los servicios.",
        ["la tesis se apoya en el caso", "la medida iguala condiciones y no da un privilegio", "el límite reconoce que el caso es ficticio"], ["cuatro frases escritas"], ["proponer una medida que cambia el derecho en vez de igualar condiciones", "generalizar a todo el país"],
        "Pide que explique quién es el titular, quién el garante y qué institución de la clase anterior podría intervenir."),
    reinforce="Explica a una persona de tu casa por qué una rampa o un intérprete no son privilegios.",
    extend="Observa tu colegio o barrio y anota un lugar donde una medida de acceso ayudaría a que todas las personas ejerzan un mismo derecho.",
)

# ================================================================ OA 22, clase 6
F = ("Ficha 6 (hechos y caso ficticio para debatir). "
     "Los derechos no se ordenan por importancia (indivisibilidad), pero en casos concretos dos derechos pueden entrar en tensión. "
     "Una restricción a un derecho solo es legítima si está en la ley, busca un fin legítimo y es proporcional, es decir, limita el derecho solo lo necesario. "
     "Hay derechos que no admiten restricción, como el derecho a no ser sometido a tortura. "
     "Los crímenes de lesa humanidad no prescriben: pasado el tiempo siguen pudiendo investigarse. "
     "Caso ficticio: un sindicato convoca una marcha por una avenida de 10 cuadras que lleva a un hospital. Los vecinos piden poder circular y el sindicato pide ejercer su derecho a reunirse.")
build(
    OA, 6, F,
    use="Aprenderé a debatir con argumentos las tensiones entre derechos, sus límites legítimos y por qué algunas protecciones no admiten restricción.",
    prior=["Sé qué es la indivisibilidad e imprescriptibilidad.", "Sé construir un argumento con razón y evidencia.", "Sé reconocer un límite en una conclusión."],
    explain=[
        "Los derechos humanos no se ordenan por importancia, pero a veces dos derechos parecen chocar en un caso concreto. Por ejemplo, el derecho a reunirse en una marcha y el derecho a circular. Debatir estas situaciones exige buscar cómo respetar ambos lo más posible, sin eliminar ninguno.",
        "Una restricción es legítima solo si está en la ley, busca un fin legítimo y es proporcional. Proporcional significa limitar el derecho lo necesario y no más. Hay derechos que no admiten restricción, como no ser sometido a tortura. Y los crímenes de lesa humanidad no prescriben porque, por su gravedad, el derecho internacional decidió que no se extinguen con el tiempo.",
        "Un debate respetuoso presenta tesis, razones y evidencia, reconoce el mejor argumento contrario y declara los límites de los datos. Evita atacar a las personas o generalizar. Los casos de esta clase son ficticios; si una situación real pone en riesgo a una persona, lo primero es avisar a una persona adulta de confianza.",
    ],
    vocab=[("proporcionalidad", "limitar un derecho solo lo necesario para proteger otro"), ("restricción legítima", "limitación de un derecho que está en la ley y busca un fin legítimo"), ("tensión entre derechos", "situación en que dos derechos parecen chocar en un caso concreto"), ("lesa humanidad", "crimen muy grave cometido de forma sistemática contra población civil"), ("derecho absoluto", "derecho que no admite restricción, como no ser sometido a tortura")],
    worked=[
        ("Evaluar proporcionalidad", "Una ciudad ficticia prohíbe todas las marchas para siempre porque una vez hubo ruido. ¿Es proporcional?",
         ["La prohibición limita el derecho a reunirse por completo.", "El ruido se podría enfrentar con medidas menores, como horarios o rutas."], "No; limita más de lo necesario"),
        ("Aplicar el cálculo", "En una avenida de 8 cuadras se reservan 3 para una actividad y el resto queda libre. ¿Cuántas cuadras quedan libres?",
         ["Resto las reservadas del total.", "8 − 3 = 5."], "5 cuadras"),
    ],
    mistakes=[("Pensar que un derecho solo puede ejercerse si no molesta a nadie.", "Se confunde restricción con anulación.", "Busca cómo ejercerlo limitando solo lo necesario."),
              ("Creer que el tiempo puede borrar la responsabilidad en un crimen de lesa humanidad.", "Se confunde con delitos que sí prescriben.", "Recuerda que los crímenes de lesa humanidad no prescriben.")],
    T=[
        ("{F} ¿Qué dos derechos entran en tensión en el caso de la marcha?", "El derecho a reunirse y el derecho a circular", "Son los que piden el sindicato y los vecinos."),
        ("{F} ¿Cuál de estos derechos no admite restricción, según la ficha? A) No ser sometido a tortura B) Reunirse en una marcha", "A) No ser sometido a tortura", "La ficha lo nombra como derecho que no admite restricción."),
        ("{F} ¿Qué significa que una restricción sea proporcional?", "Que limita el derecho solo lo necesario", "Esa es la definición de la ficha."),
        ("{F} Cerrar toda la ciudad para siempre porque una marcha causa molestias es... A) desproporcionado B) proporcional", "A) desproporcionado", "Limita mucho más de lo necesario."),
        ("{F} ¿Cuál es una condición para que una restricción sea legítima? A) Que esté en la ley y busque un fin legítimo B) Que la pida la mayoría de los vecinos", "A) Que esté en la ley y busque un fin legítimo", "Son dos de las condiciones de la ficha."),
        ("=", "{F} Si de las 10 cuadras de la avenida la marcha ocupa 4 y el resto queda libre, ¿qué porcentaje queda libre para circular?", "(10-4)*100/10", "Se calculan las cuadras libres y se llevan a porcentaje.", " %"),
        ("{F} Un argumento que busca respetar ambos derechos es... A) desviar el tránsito por vías alternativas y mantener libre el acceso al hospital B) prohibir las marchas", "A) desviar el tránsito por vías alternativas y mantener libre el acceso al hospital", "Limita lo necesario y protege ambos derechos."),
        ("{F} Un debatiente dice: «Quienes marchan no piensan en nadie». ¿Qué error comete? A) Generaliza y ataca a las personas en vez de responder sus razones B) Usa una fuente de otro año", "A) Generaliza y ataca a las personas en vez de responder sus razones", "No discute el argumento."),
        ("{F} ¿Qué dato pedirías para evaluar el caso? A) Cuántas ambulancias necesitaron pasar y qué rutas alternas existían B) Cuántos sindicatos hay en el país", "A) Cuántas ambulancias necesitaron pasar y qué rutas alternas existían", "Es el dato relevante para decidir la proporcionalidad."),
        ("{F} ¿Por qué la indivisibilidad no impide que haya tensiones entre derechos en casos concretos?", "Porque dice que no se ordenan por importancia en abstracto, pero en un caso concreto hay que buscar cómo conciliarlos", "La indivisibilidad no dice que nunca choquen, sino que ninguno vale menos."),
        ("{F} ¿Por qué los crímenes de lesa humanidad no prescriben? A) Por su gravedad, el derecho internacional decidió que no se extinguen con el tiempo B) Porque ocurrieron hace tanto tiempo que ya no se pueden investigar", "A) Por su gravedad, el derecho internacional decidió que no se extinguen con el tiempo", "La ficha indica que siguen pudiendo investigarse."),
        ("{F} Redacta una postura sobre el caso con un argumento, un contraargumento y un límite.", "Respuesta modelo: Argumento: la marcha es un derecho. Contraargumento: bloquear el acceso al hospital pone en riesgo a las personas. Límite: no conocemos las rutas alternas, así que solo puedo recomendar medidas que limiten lo necesario.", "Incluye argumento, contraargumento y límite."),
        ("{F} ¿Qué cierre respeta mejor la evidencia? A) Habría que conciliar la marcha y el acceso al hospital con la menor restricción necesaria, según los datos de rutas y emergencias B) Un derecho siempre debe vencer al otro", "A) Habría que conciliar la marcha y el acceso al hospital con la menor restricción necesaria, según los datos de rutas y emergencias", "Aplica la proporcionalidad y pide datos."),
    ],
    ctx=("En un debate de curso se discute si una autoridad puede cerrar una calle durante una marcha. ¿Qué intervención es más documentada? A) «Se puede cerrar parte de la calle si hay rutas alternas y acceso a emergencias, porque es lo necesario para proteger ambos derechos» B) «Hay que cerrarla porque yo lo digo»", "A) «Se puede cerrar parte de la calle si hay rutas alternas y acceso a emergencias, porque es lo necesario para proteger ambos derechos»", "Da una razón, aplica proporcionalidad y menciona evidencia."),
    sc=[("¿Qué es la proporcionalidad?", "Limitar un derecho solo lo necesario para proteger otro", "Así se define en la clase."),
        ("¿Qué derecho no admite restricción según la ficha?", "No ser sometido a tortura", "La ficha lo nombra como derecho absoluto."),
        ("=", "Una avenida ficticia tiene 12 cuadras y se reservan 5 para una actividad. ¿Cuántas quedan libres?", "12-5", "Se restan las reservadas al total.", " cuadras")],
    op=("Escribe una intervención de debate de cinco oraciones sobre el caso de la marcha. Incluye tu tesis, una razón, una medida proporcional, el mejor argumento de la postura contraria y un límite de tus datos. Usa un tono respetuoso. {F}",
        "Tesis: se puede conciliar la marcha y la circulación. Razón: ambos derechos son importantes. Medida: reservar parte de la avenida y mantener libre el acceso al hospital. Mejor argumento contrario: la marcha puede dificultar emergencias. Límite: no conocemos las rutas alternas.",
        ["incluye tesis, razón, medida, argumento contrario y límite", "la medida es proporcional", "el tono es respetuoso"], ["texto de cinco oraciones"], ["proponer anular un derecho", "no incluir límite"],
        "Pide que diga qué dato nuevo cambiaría su postura."),
    reinforce="Explica a una persona de tu casa qué significa limitar un derecho solo lo necesario.",
    extend="Piensa en una norma de convivencia de tu colegio que limita una libertad y di si es proporcional y por qué.",
)
