"""Material del estudiante de 2.º medio, Historia, Geografía y Ciencias Sociales: OA 12 (pobreza, migración campo-ciudad y segregación urbana) y OA 13 (actores sociales y proyectos políticos de los años sesenta)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI2M OA 12"

# ================================================================ OA 12, clase 1
F = ("Ficha 1 (mediados del siglo XX son los años cercanos a 1950; los números son de ejemplo, no estadísticas oficiales). "
     "Pobreza: falta de ingresos y bienes para cubrir necesidades básicas como comida, vivienda y salud. "
     "Precariedad: condiciones inestables, sin seguridad de empleo, de vivienda ni de atención. "
     "Marginalidad: vivir al margen del acceso a servicios y a decisiones. "
     "Desnutrición: alimentación insuficiente para las necesidades del cuerpo. "
     "Migración campo-ciudad: traslado de familias desde zonas rurales a ciudades en busca de trabajo, escuela o salud. "
     "Población urbana: personas que viven en ciudades. "
     "Poder adquisitivo: cantidad de bienes y servicios que una familia puede comprar con sus ingresos. "
     "Crédito: préstamo de dinero o de mercadería que se devuelve más tarde; quien no tiene bienes ni contrato fijo lo consigue con dificultad. "
     "Datos de ejemplo: de cada 100 familias de un barrio, 35 vivían en piezas sin agua potable; el salario de una familia de ejemplo alcanzaba para 20 días de comida en un mes de 30 días.")
build(
    OA, 1, F,
    use="Aprenderé a situar la pobreza y la precariedad de mediados del siglo XX en Chile y a nombrar a los actores que migraron del campo a la ciudad.",
    prior=["Sé que una fuente es una huella del pasado.", "Sé ubicar procesos en una época y calcular diferencias simples.", "Sé que un proceso histórico tiene varios actores."],
    explain=[
        "A mediados del siglo XX, muchas familias chilenas vivían en la pobreza: sus ingresos no alcanzaban para comer, tener una vivienda digna o atenderse en salud. A eso se sumaba la precariedad, que es vivir sin seguridad de empleo, de techo o de atención. También había bajo poder adquisitivo (los ingresos compraban poco) y poco acceso al crédito, que es el préstamo que se devuelve más tarde y que era difícil de conseguir sin bienes ni contrato fijo. La marginalidad es vivir al margen del acceso a servicios y a las decisiones, y la desnutrición es comer menos de lo que el cuerpo necesita. Los historiadores miden esta situación con indicadores sociodemográficos, es decir, datos sobre salud, edad, educación y vivienda de la población.",
        "Muchas familias del campo se trasladaron a las ciudades buscando trabajo, escuela y hospital. Eso se llama migración campo-ciudad y hizo crecer la población urbana. Los actores son las familias migrantes, los dueños de fundos, los obreros, las autoridades y quienes ya vivían en las ciudades.",
        "No todos vivían igual: la pobreza era extensa, pero había grupos con más recursos. Por eso conviene preguntar quiénes vivían así, dónde y en qué fecha, y no generalizar con un solo dato. Los números de esta ficha son de ejemplo y sirven para practicar el análisis.",
    ],
    vocab=[("pobreza", "falta de ingresos y bienes para cubrir necesidades básicas"), ("precariedad", "condiciones inestables, sin seguridad de empleo, vivienda o atención"), ("desnutrición", "alimentación insuficiente para las necesidades del cuerpo"), ("migración campo-ciudad", "traslado de familias de zonas rurales a ciudades"), ("indicador sociodemográfico", "dato sobre salud, edad, educación o vivienda de una población"), ("poder adquisitivo", "cantidad de bienes y servicios que una familia compra con sus ingresos"), ("crédito", "préstamo de dinero o de mercadería que se devuelve más tarde"), ("marginalidad", "vivir al margen del acceso a servicios y a las decisiones")],
    worked=[
        ("Calcular un indicador", "En un barrio de ejemplo, 18 de cada 100 familias no tienen cocina propia. ¿Cuántas de cada 100 sí la tienen?", ["Parto del total, 100 familias.", "Resto las que no la tienen: 100 − 18 = 82."], "82 de cada 100 familias"),
        ("Nombrar el proceso", "Una familia vende su yunta de bueyes en el campo y se instala en una ciudad para que los hijos vayan a la escuela. ¿Qué proceso muestra?", ["Cambia de zona rural a ciudad.", "Lo hace buscando trabajo y escuela."], "Migración campo-ciudad"),
    ],
    mistakes=[("Decir que pobreza y migración son lo mismo.", "Se confunde una condición de vida con un traslado de personas.", "Define cada una y explica cómo se relacionan: la pobreza puede empujar a migrar."),
              ("Creer que todo Chile vivía igual en 1950.", "Se generaliza desde un barrio o un dato.", "Indica a quién describe el dato y qué grupos faltan.")],
    T=[
        ("{F} En Historia, ¿qué es la desnutrición?", "Alimentación insuficiente para las necesidades del cuerpo", "La ficha la define así."),
        ("{F} En Historia, ¿qué es la migración campo-ciudad?", "El traslado de familias de zonas rurales a ciudades en busca de trabajo, escuela o salud", "Así la define la ficha."),
        ("=", "{F} ¿Cuántas de cada 100 familias del barrio de ejemplo vivían con agua potable?", "100-35", "Se resta al total las familias sin agua potable.", " familias"),
        ("{F} Un jefe de hogar trabaja solo por días, sin contrato y sin certeza de tener trabajo la semana siguiente. ¿Qué rasgo describe mejor? A) Precariedad B) Desnutrición", "A) Precariedad", "Vivir sin seguridad de empleo es precariedad; la desnutrición es falta de alimentación."),
        ("{F} Una familia deja un fundo y se instala en una ciudad para trabajar en una fábrica. ¿Qué proceso protagoniza? A) Migración campo-ciudad B) Aumento de la población rural", "A) Migración campo-ciudad", "Pasa de una zona rural a una ciudad en busca de trabajo."),
        ("{F} Un libro dice que «la población urbana creció». ¿Qué significa? A) Más personas vivían en ciudades B) Se fundaron más ciudades en el país", "A) Más personas vivían en ciudades", "Población urbana es el número de personas que viven en ciudades, no la cantidad de ciudades."),
        ("{F} Una familia recibe un sueldo que, por los precios, solo le permite comprar pan y fideos. ¿Qué situación describe? A) Bajo poder adquisitivo B) Poco acceso al crédito", "A) Bajo poder adquisitivo", "El poder adquisitivo es lo que se puede comprar con los ingresos; el crédito se refiere a préstamos."),
        ("{F} Una familia pide un préstamo para comprar una cama, pero se lo niegan porque no tiene bienes ni contrato fijo. ¿Qué limitación muestra? A) Poco acceso al crédito B) Aumento de la población urbana", "A) Poco acceso al crédito", "El crédito es el préstamo que se devuelve más tarde; sin bienes ni contrato es difícil conseguirlo."),
        ("{F} Un sector de la ciudad no tiene agua, luz, escuela ni consultorio, y sus habitantes no participan en las decisiones de la comuna. ¿Qué situación describe mejor? A) Marginalidad B) Migración campo-ciudad", "A) Marginalidad", "Vivir al margen del acceso a servicios y a las decisiones es marginalidad."),
        ("{F} ¿Por qué la desnutrición se considera un indicador de pobreza y no solo un problema de salud?", "Porque muestra que los ingresos no alcanzaban para comer lo necesario", "El hambre prolongada revela falta de ingresos para alimentarse."),
        ("{F} Un compañero dice: «En 1950 todo Chile era igual de pobre». ¿Qué corrección corresponde? A) Los datos de un barrio de ejemplo no permiten hablar de todo el país B) Tiene razón porque la pobreza era extensa", "A) Los datos de un barrio de ejemplo no permiten hablar de todo el país", "Extensa no significa igual para todos; un solo barrio no representa a todo el país."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Cómo vivían las familias pobres y qué efectos tuvo su traslado a las ciudades a mediados del siglo XX? B) ¿Fue buena o mala la vida en las ciudades?", "A) ¿Cómo vivían las familias pobres y qué efectos tuvo su traslado a las ciudades a mediados del siglo XX?", "La pregunta A tiene época y lugar y se responde con fuentes; la B pide una opinión sin época ni criterio."),
        ("=", "{F} Otro barrio de ejemplo tenía 12 de cada 100 familias sin agua potable. ¿Cuántas familias más por cada 100 estaban sin agua en el barrio de la ficha?", "35-12", "Se resta el dato del segundo barrio al del primero.", " familias"),
    ],
    ctx=("Una exposición muestra una foto de una calle de tierra, un salario de ejemplo y una lista de enfermedades de niños. ¿Qué título resume mejor la muestra? A) Pobreza y precariedad urbana a mediados del siglo XX B) La modernización del campo", "A) Pobreza y precariedad urbana a mediados del siglo XX", "Los tres materiales hablan de condiciones de vida difíciles en la ciudad."),
    sc=[("En Historia, ¿qué es la precariedad?", "Vivir en condiciones inestables, sin seguridad de empleo, vivienda o atención", "Así se define en el vocabulario."),
        ("¿Qué buscaban las familias del campo al migrar a la ciudad? A) Trabajo, escuela y atención de salud B) Tierras más grandes para cultivar", "A) Trabajo, escuela y atención de salud", "La ficha define la migración campo-ciudad por esos tres motivos."),
        ("=", "Un barrio de ejemplo tiene 60 familias y 24 viven sin agua potable. ¿Cuántas tienen agua?", "60-24", "Se resta al total las familias sin agua.", " familias")],
    op=("Elige una familia de ejemplo que migra del campo a la ciudad (inventa su nombre de pila). Escribe en seis líneas: de dónde sale, por qué se va, a qué ciudad llega y dos dificultades que enfrenta, usando al menos cuatro palabras del vocabulario. No uses datos personales reales. {F}",
        "«Rosa y su familia dejan un fundo porque el salario no alcanza (pobreza). Llegan a una ciudad y viven en una pieza sin agua (precariedad). Buscan trabajo y escuela para sus hijos (migración campo-ciudad)…»",
        ["usa cuatro términos del vocabulario con sentido", "explica por qué migra", "menciona dos dificultades"], ["texto de seis líneas"], ["inventar cifras presentadas como reales", "usar un solo término del vocabulario"],
        "Pide que explique en qué se diferencian pobreza y precariedad."),
    reinforce="Explica a alguien de tu casa, con tus palabras, qué es la migración campo-ciudad y por qué pudo ocurrir.",
    extend="Pregunta a una persona mayor de tu casa si conoce a alguien que se mudó del campo a la ciudad y anota el motivo en una frase.",
)

# ================================================================ OA 12, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, informe de una asistente social, 1950: «De 30 hogares visitados en el cerro, 21 no tienen agua en la casa y comparten una sola llave.» "
     "Fuente B, carta de un propietario agrícola a un amigo, 1950: «Los jóvenes se van a la ciudad por ambición; en el fundo siempre hubo pan y techo para todos.» "
     "Fuente C, nota de un diario de la capital, 1951: «Cada semana llegan familias del sur; se levantan casas de lata y cartón en la orilla del río.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes por su procedencia: quién las escribió, cuándo, para qué y qué pueden y no pueden probar sobre la pobreza y la migración.",
    prior=["Sé qué es una fuente y distingo hecho de opinión.", "Conozco la pobreza y la migración campo-ciudad de la clase anterior.", "Sé contrastar dos textos."],
    explain=[
        "Interrogar una fuente es hacerle preguntas antes de creerle. La primera es su procedencia: quién la produjo, en qué fecha, en qué lugar y con qué propósito. Una asistente social que visita hogares escribe para informar; un propietario que escribe a un amigo defiende su posición.",
        "Toda fuente tiene una intención y un punto de vista. Eso se llama sesgo cuando la mirada del autor deforma lo que cuenta. Un sesgo no vuelve inútil la fuente: sirve para saber cómo pensaba su autor. Lo que no se puede hacer es tomar una sola fuente como prueba de todo.",
        "Para corroborar, es decir, confirmar un dato, se busca otra fuente independiente que diga algo parecido. Además hay que respetar el alcance: un informe sobre 30 hogares habla de esos hogares, no de todo el país. Cada fuente se usa para lo que realmente puede mostrar.",
    ],
    vocab=[("procedencia", "datos de una fuente: quién la hizo, cuándo, dónde y para qué"), ("sesgo", "mirada del autor que deforma lo que cuenta por su interés o postura"), ("corroborar", "confirmar un dato con otra fuente independiente"), ("fuente primaria", "documento producido en la época que se estudia"), ("alcance", "lo que una fuente puede probar y lo que no")],
    worked=[
        ("Preguntar por la procedencia", "Un cartel de 1952 de una empresa inmobiliaria dice que «la vida en la periferia es sana y tranquila». ¿Qué pregunta de procedencia haces primero?", ["Veo quién lo produjo: una empresa que vende terrenos.", "Pregunto qué gana al describir así la periferia."], "¿Qué interés tiene la empresa en ese mensaje?"),
        ("Medir el alcance", "Un informe de 2 ciudades de ejemplo dice que en ambas faltan escuelas. ¿Puede afirmarse que faltaban en todo el país?", ["El informe cubre solo 2 ciudades.", "Habría que corroborar con más fuentes."], "No, solo prueba lo que ocurría en esas ciudades"),
    ],
    mistakes=[("Creer que una fuente oficial o escrita es siempre verdadera.", "Se confunde estar escrita con ser neutral.", "Pregunta quién la escribe y para qué antes de usarla."),
              ("Descartar una fuente porque tiene sesgo.", "Se olvida que sirve para conocer cómo pensaba su autor.", "Úsala para eso y contrástala con otras.")],
    T=[
        ("{F} ¿Quién escribe la fuente A?", "Una asistente social", "El encabezado de la fuente lo dice."),
        ("{F} ¿Qué fuente habla de casas de lata y cartón?", "La fuente C, la nota del diario", "La nota de 1951 menciona esas casas."),
        ("=", "{F} ¿Cuántos de los 30 hogares visitados sí tienen agua en la casa?", "30-21", "Se resta al total los hogares sin agua.", " hogares"),
        ("{F} En Historia, ¿qué es la procedencia de una fuente? A) Quién la produjo, cuándo y para qué B) El lugar donde hoy se guarda", "A) Quién la produjo, cuándo y para qué", "Procedencia es el origen de la fuente, no su ubicación actual."),
        ("{F} ¿Por qué la fuente B puede estar sesgada? A) Su autor es dueño de un fundo y defiende su posición B) Porque es una carta", "A) Su autor es dueño de un fundo y defiende su posición", "Su interés como propietario influye en lo que cuenta."),
        ("{F} ¿Cuál de estas dos fuentes describe condiciones de vida observadas en un barrio? A) La fuente A B) La fuente B", "A) La fuente A", "La asistente social visitó hogares; el propietario da una opinión sobre los jóvenes."),
        ("{F} Para corroborar lo que dice la fuente C sobre las casas de lata, ¿qué otra fuente sirve? A) Una fotografía o un plano de la época de ese sector B) Una copia de la misma nota en otro diario", "A) Una fotografía o un plano de la época de ese sector", "Una fuente independiente confirma; una copia repite la misma información."),
        ("{F} Un volante de 1950 lo escribió alguien que vendía sitios en la periferia. ¿Qué pregunta de procedencia es la más útil? A) ¿Qué ganaba el autor al describir así la ciudad? B) ¿Estoy de acuerdo con lo que dice?", "A) ¿Qué ganaba el autor al describir así la ciudad?", "Revela la intención que puede sesgar el texto."),
        ("{F} En la fuente A, 21 de 30 hogares no tienen agua. ¿Qué fracción es? A) Siete de cada diez B) Tres de cada diez", "A) Siete de cada diez", "21 de 30 equivale a 7 de cada 10."),
        ("{F} ¿Por qué la carta B no basta para explicar por qué migraron los jóvenes? A) Habla desde el interés del dueño y no recoge la voz de los jóvenes B) Porque está escrita a mano", "A) Habla desde el interés del dueño y no recoge la voz de los jóvenes", "Falta la perspectiva de quienes migraron."),
        ("{F} Un compañero dice: «La fuente A prueba que todo Chile vivía sin agua». ¿Qué respondes? A) Es un informe sobre 30 hogares y no permite hablar de todo el país B) Es correcto porque la escribió una asistente social", "A) Es un informe sobre 30 hogares y no permite hablar de todo el país", "El alcance de la fuente se limita a los hogares visitados."),
        ("{F} ¿Cuál es el orden correcto para interrogar una fuente? A) Ver quién la produjo y para qué, leer su contenido y contrastarla con otra B) Leer solo lo que confirma lo que pienso y citarla", "A) Ver quién la produjo y para qué, leer su contenido y contrastarla con otra", "Procedencia, contenido y contraste son los pasos del análisis."),
        ("{F} ¿Qué oración usa las fuentes A y C sin exagerar? A) Una asistente social y un diario describen viviendas precarias en sectores de ciudades de esa época B) Las fuentes A y C prueban que todas las familias de Chile vivían en casas de lata", "A) Una asistente social y un diario describen viviendas precarias en sectores de ciudades de esa época", "La otra generaliza a todo el país más allá del alcance de las fuentes."),
    ],
    ctx=("Una profesora te entrega una fotografía sin fecha ni autor de una calle con casas de cartón. ¿Qué haces primero? A) Averiguar quién la tomó, cuándo y dónde antes de usarla como prueba B) Usarla como prueba porque es una imagen", "A) Averiguar quién la tomó, cuándo y dónde antes de usarla como prueba", "Sin procedencia no se sabe qué puede probar la imagen."),
    sc=[("En Historia, ¿qué significa corroborar?", "Confirmar un dato con otra fuente independiente", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es el sesgo de una fuente?", "La mirada del autor que deforma lo que cuenta por su interés o postura", "Así se define en la clase."),
        ("Una fuente de ejemplo dice que 8 de 20 hogares no tienen luz. ¿Puede afirmarse que a todo el país le faltaba luz? A) No, solo habla de esos 20 hogares B) Sí, porque es un dato", "A) No, solo habla de esos 20 hogares", "El alcance es el de los hogares observados.")],
    op=("Interroga la fuente C de la ficha con una tabla de tres filas: «quién la produjo y para qué», «qué cuenta» y «qué otra fuente usarías para corroborarla». Escribe una respuesta de una línea en cada fila y una conclusión de dos líneas sobre qué prueba y qué no prueba. {F}",
        "Quién: un diario capitalino, informa. Qué cuenta: llegan familias del sur y se levantan casas de lata. Corroborar: una fotografía o un plano de la época. Conclusión: prueba que había viviendas precarias en un sector; no prueba cuántas ni en todo el país.",
        ["responde las tres preguntas", "distingue lo que prueba de lo que no", "propone una fuente independiente"], ["tabla de tres filas", "conclusión de dos líneas"], ["proponer la misma nota como corroboración", "generalizar a todo el país"],
        "Pide que explique por qué la fuente B también sirve aunque tenga sesgo."),
    reinforce="Explica en voz alta qué tres preguntas haces a una fuente antes de usarla.",
    extend="Elige un aviso o una noticia que veas hoy y anota quién lo produce y qué quiere lograr.",
)

# ================================================================ OA 12, clase 3
F = ("Ficha 3 (tres perspectivas de ejemplo escritas para este cuaderno). "
     "Perspectiva del migrante, 1955: «En el fundo ganaba en especies y no tenía escuela para mis hijos; en la ciudad tendré un salario, aunque la pieza sea pequeña.» "
     "Perspectiva del propietario agrícola, 1955: «Se van los peones más jóvenes y la cosecha queda con pocos brazos.» "
     "Perspectiva de la autoridad local de una ciudad, 1955: «Llegan más familias de las que podemos atender con escuelas y viviendas.» "
     "Escalas: local (un barrio), regional (una provincia o zona), nacional (todo el país). "
     "Datos de ejemplo: un barrio pasa de 800 a 2.000 habitantes en diez años; otro barrio pasa de 500 a 1.100; una provincia de 60.000 habitantes pierde 5.000.")
build(
    OA, 3, F,
    use="Aprenderé a comparar cómo veían la migración un migrante, un propietario y una autoridad, y a distinguir la escala local, regional y nacional.",
    prior=["Sé interrogar una fuente por su procedencia.", "Sé que la pobreza y la migración tuvieron varios actores.", "Sé comparar dos datos con una resta."],
    explain=[
        "Un mismo proceso se ve distinto según quién lo mira. Esa mirada es la perspectiva. Para el migrante, irse a la ciudad era una oportunidad con costos; para el propietario, una pérdida de trabajadores; para la autoridad local, un desafío de servicios. Las tres pueden ser verdaderas a la vez, porque cada una describe una parte.",
        "También importa la escala, es decir, el tamaño del espacio que se mira. En la escala local se observa un barrio, en la regional una provincia o zona y en la nacional todo el país. Un hecho local, como un barrio que crece mucho, no siempre representa lo que ocurre en el resto.",
        "Comparar es buscar semejanzas y diferencias con un criterio. Aquí los criterios son quién habla, qué problema ve y a qué escala se refiere. Comparar no obliga a elegir una perspectiva ganadora: sirve para entender mejor el proceso completo.",
    ],
    vocab=[("perspectiva", "mirada de un actor según su posición e intereses"), ("escala", "tamaño del espacio que se estudia: local, regional o nacional"), ("local", "referido a un barrio o una comunidad"), ("regional", "referido a una provincia o zona del país"), ("criterio de comparación", "aspecto que se usa para comparar, como el actor o la escala")],
    worked=[
        ("Reconocer la escala", "Un informe de ejemplo describe cómo cambió un barrio de 300 familias. ¿Qué escala usa?", ["Mira un solo barrio o población.", "Es el espacio más pequeño de las tres escalas."], "Escala local"),
        ("Comparar perspectivas", "Un trabajador dice que migra para ganar un salario. Un dueño de fundo dice que migrar le deja sin peones. ¿En qué coinciden?", ["Ambos reconocen que migrar cambia el trabajo en el campo.", "Se diferencian en si lo ven como oportunidad o como pérdida."], "En que la migración cambia el trabajo rural"),
    ],
    mistakes=[("Elegir una perspectiva como la única verdadera.", "Se confunde comparar con juzgar quién tiene razón.", "Describe qué parte del proceso ve cada actor."),
              ("Generalizar desde un barrio a todo el país.", "Se cambia de escala sin datos que lo respalden.", "Indica la escala del dato y no la cambies sin evidencia.")],
    T=[
        ("{F} ¿Qué escala es un barrio?", "Local", "La ficha define lo local como un barrio."),
        ("{F} ¿Quién dice que se van los peones más jóvenes?", "El propietario agrícola", "Es la frase de su perspectiva."),
        ("=", "{F} ¿Cuántos habitantes más tiene el primer barrio al final de los diez años?", "2000-800", "Se resta la población inicial a la final.", " habitantes"),
        ("{F} Una autoridad dice que faltan escuelas para tantos niños recién llegados. ¿Qué perspectiva es? A) La autoridad local B) El propietario agrícola", "A) La autoridad local", "Habla de servicios que debe entregar la ciudad."),
        ("{F} Un informe mide cuántos habitantes perdió toda la provincia de ejemplo en diez años. ¿Qué escala usa? A) Regional B) Local", "A) Regional", "Mira una provincia entera, un espacio mayor que un barrio."),
        ("{F} ¿Por qué conviene comparar escalas? A) Porque un hecho local puede no representar lo que ocurre en el país B) Porque todas las escalas siempre dan el mismo resultado", "A) Porque un hecho local puede no representar lo que ocurre en el país", "Cada escala muestra algo distinto."),
        ("{F} Un trabajador dice «en la ciudad tendré salario» y un dueño dice «se van los mejores peones». ¿Qué tienen en común? A) Ambos reconocen que la migración cambia el trabajo del campo B) Ambos opinan que migrar fue un error", "A) Ambos reconocen que la migración cambia el trabajo del campo", "Coinciden en el hecho y difieren en cómo lo valoran."),
        ("=", "{F} ¿Cuántos habitantes quedan en la provincia de ejemplo después de perder población?", "60000-5000", "Se resta lo que perdió a lo que tenía.", " habitantes"),
        ("{F} Un informe suma cuántas personas dejaron el campo en todo el país durante diez años. ¿Qué escala usa? A) Nacional B) Regional", "A) Nacional", "Cuenta a todo el país, no a una provincia ni a un barrio."),
        ("{F} ¿Por qué dos perspectivas distintas pueden ser verdaderas a la vez?", "Porque cada una describe una parte del proceso desde su posición", "Cada actor ve aspectos distintos de la misma realidad."),
        ("{F} Un estudiante dice: «Si un barrio creció mucho, todo Chile creció igual». ¿Cuál es el error? A) Pasa de escala local a nacional sin datos B) Usa datos de ejemplo", "A) Pasa de escala local a nacional sin datos", "El barrio no representa por sí solo al país."),
        ("{F} ¿Qué perspectiva falta para evaluar el impacto de la migración en la ciudad? A) La de las familias que ya vivían en ella B) Ninguna, ya están todas", "A) La de las familias que ya vivían en ella", "La ficha no recoge a quienes recibieron a los migrantes."),
        ("=", "{F} El segundo barrio pasó de 500 a 1.100 habitantes. ¿Cuántos habitantes más sumó el primer barrio que el segundo?", "(2000-800)-(1100-500)", "Se calcula cuánto creció cada barrio y se restan los aumentos.", " habitantes"),
    ],
    ctx=("Un concejo municipal de ejemplo debe decidir cómo gastar en el barrio que pasó de 800 a 2.000 habitantes. ¿Qué escala y qué perspectiva debe considerar primero? A) Escala local y la perspectiva de los vecinos del barrio B) Escala nacional y solo la del propietario", "A) Escala local y la perspectiva de los vecinos del barrio", "La decisión es sobre un barrio y quienes viven allí."),
    sc=[("En Historia, ¿qué es la perspectiva?", "La mirada de un actor según su posición e intereses", "Así se define en el vocabulario."),
        ("¿Qué escala es una provincia?", "Regional", "La ficha ubica lo regional en provincias o zonas."),
        ("=", "Un barrio de ejemplo pasa de 700 a 1.500 habitantes. ¿Cuántos habitantes sumó?", "1500-700", "Se resta la población inicial a la final.", " habitantes")],
    op=("Escribe tres frases de dos líneas: una desde la perspectiva de un migrante, otra desde la de un propietario y otra desde la de una autoridad local sobre la llegada de familias del campo. Después escribe una línea que diga si cada una habla en la escala local, regional o nacional y una semejanza entre dos de ellas. {F}",
        "Migrante: «Me voy porque en la ciudad tendré salario» (escala local: su familia y su pieza). Propietario: «Me quedo sin peones» (escala local: su fundo). Autoridad: «Faltan escuelas» (escala local: su ciudad). Semejanza: dos reconocen que el trabajo y los servicios cambian.",
        ["tres perspectivas bien diferenciadas", "indica la escala de cada una", "señala una semejanza real"], ["tres frases", "línea de escalas y semejanza"], ["repetir la misma idea con distintas palabras", "no indicar la escala"],
        "Pide que explique por qué no hace falta elegir una sola perspectiva."),
    reinforce="Explica a alguien de tu casa qué es una perspectiva y da un ejemplo de este tema.",
    extend="Piensa en un cambio reciente de tu barrio y di cómo lo verían una persona joven y una persona mayor.",
)

# ================================================================ OA 12, clase 4
F = ("Ficha 4 (hechos generales y datos de ejemplo rotulados). "
     "Causas de salida del campo: salarios bajos o pagados en especies, tierra concentrada en pocos fundos, pocas escuelas y servicios de salud. "
     "Causas de atracción de la ciudad: industrias, comercio, escuelas y hospitales. "
     "Cambios: crece la población urbana; se levantan viviendas improvisadas en los bordes de las ciudades (en Chile se les llamó poblaciones callampa); faltan casas. "
     "Segregación urbana: separación de los grupos sociales en barrios distintos según sus ingresos. "
     "Continuidades: la pobreza y la desigualdad no desaparecen, cambian de lugar. "
     "Hecho: en 1957 un grupo de familias sin casa ocupó terrenos en Santiago y formó la población La Victoria. "
     "Dato de ejemplo: una ciudad tiene 3.000 viviendas y 4.500 familias (cada vivienda aloja a una sola familia).")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de la migración con sus cambios, la escasez de viviendas y la segregación urbana, y a señalar qué continuó igual.",
    prior=["Sé comparar perspectivas y escalas.", "Sé que un proceso tiene varias causas.", "Sé interrogar fuentes."],
    explain=[
        "La migración campo-ciudad tuvo causas de salida y de atracción. Salían del campo familias con salarios bajos, sin tierra propia y con pocas escuelas cerca. La ciudad atraía con industrias, comercio, escuelas y hospitales. Ambas fuerzas actuaron a la vez, y ninguna explica el proceso por sí sola.",
        "El cambio principal fue el crecimiento de la población urbana. Como no había casas suficientes, muchas familias levantaron viviendas improvisadas o ocuparon terrenos, como en La Victoria, en 1957. Además apareció la segregación urbana: los grupos con más ingresos y los con menos vivían en barrios separados, con distinto acceso a servicios.",
        "También hubo continuidades. La pobreza y la desigualdad no se acabaron al llegar a la ciudad: se trasladaron. Por eso un buen análisis separa lo que cambió, lo que siguió igual y las causas, y evita decir que todo ocurrió por una sola razón.",
    ],
    vocab=[("causa de salida", "razón que empuja a una familia a dejar su lugar de origen"), ("causa de atracción", "razón que atrae a una familia hacia un lugar de destino"), ("segregación urbana", "separación de grupos sociales en barrios distintos según sus ingresos"), ("población callampa", "conjunto de viviendas improvisadas en los bordes de una ciudad"), ("continuidad", "aspecto que sigue igual a pesar de un cambio")],
    worked=[
        ("Clasificar una causa", "Una familia migra porque en la ciudad hay un hospital cercano. ¿Es causa de salida o de atracción?", ["El hospital está en la ciudad de destino.", "Atrae a la familia hacia ese lugar."], "Causa de atracción"),
        ("Calcular un déficit", "En una ciudad de ejemplo hay 2.000 viviendas y 2.600 familias. ¿Cuántas familias quedan sin vivienda propia?", ["Cada vivienda aloja a una familia.", "Resto: 2.600 − 2.000 = 600."], "600 familias"),
    ],
    mistakes=[("Explicar la migración con una sola causa.", "Se ignora que hubo fuerzas de salida y de atracción a la vez.", "Nombra al menos una de cada tipo."),
              ("Pensar que al llegar a la ciudad la pobreza desaparecía.", "Se confunde cambiar de lugar con salir de la pobreza.", "Distingue qué cambió y qué siguió igual.")],
    T=[
        ("{F} En Historia, ¿qué es la segregación urbana?", "La separación de los grupos sociales en barrios distintos según sus ingresos", "La ficha la define así."),
        ("{F} ¿En qué año se formó la población La Victoria?", "1957", "La ficha lo indica."),
        ("{F} ¿Cuál es una causa de atracción de la ciudad? A) Las industrias y los hospitales B) Los salarios bajos del campo", "A) Las industrias y los hospitales", "La ficha enumera industrias, comercio, escuelas y hospitales; los salarios bajos son causa de salida."),
        ("=", "{F} ¿Cuántas familias de la ciudad de ejemplo quedan sin vivienda propia?", "4500-3000", "Se resta el número de viviendas al de familias.", " familias"),
        ("{F} Un peón deja el fundo porque su pago en especies no alcanza. ¿Qué tipo de causa es? A) De salida B) De atracción", "A) De salida", "El motivo está en el lugar de origen y lo empuja a irse."),
        ("{F} Familias sin casa ocupan un terreno y levantan viviendas improvisadas. ¿Qué problema muestra? A) Escasez de viviendas B) Aumento de la población rural", "A) Escasez de viviendas", "Ocupar terrenos responde a la falta de casas."),
        ("{F} En una ciudad de ejemplo, un barrio con calles pavimentadas y otro sin agua potable están separados por un canal. ¿Qué fenómeno ilustra? A) Segregación urbana B) Migración rural", "A) Segregación urbana", "Grupos con distintos recursos viven separados y con distinto acceso a servicios."),
        ("=", "{F} La ciudad de ejemplo agrega 500 viviendas nuevas. ¿Cuántas familias siguen sin vivienda propia?", "4500-(3000+500)", "Se suman las viviendas nuevas a las existentes y se resta de las familias.", " familias"),
        ("{F} Un historiador escribe: «Salían del campo familias, pero nada atraía a la ciudad». ¿Qué falta en su explicación? A) Las causas de atracción como industrias y escuelas B) Las causas de salida", "A) Las causas de atracción como industrias y escuelas", "Hubo fuerzas de salida y de atracción a la vez."),
        ("{F} ¿Qué continuidad muestra la ficha entre el campo y la ciudad?", "La pobreza y la desigualdad seguían, pero en otro lugar", "Cambiaron de lugar, no desaparecieron."),
        ("{F} Alguien afirma: «La toma de terrenos de 1957 prueba que la migración fue la única causa de la falta de viviendas». ¿Qué corriges? A) Un solo hecho no prueba una causa única; hay que considerar otras causas B) Nada, es correcto", "A) Un solo hecho no prueba una causa única; hay que considerar otras causas", "Una toma de terrenos muestra falta de casas, pero no basta para explicar todo con una sola causa."),
        ("{F} ¿Por qué la segregación urbana es a la vez un cambio y una continuidad?", "Porque es un cambio de lugar de la desigualdad que ya existía en el campo", "La desigualdad se traslada y toma forma de barrios separados."),
        ("{F} ¿Cuál es la mejor síntesis? A) Causas de salida y atracción produjeron crecimiento urbano, falta de casas y segregación, con continuidad de la pobreza B) La ciudad resolvió la pobreza del campo", "A) Causas de salida y atracción produjeron crecimiento urbano, falta de casas y segregación, con continuidad de la pobreza", "Reúne causas, cambios y continuidades."),
    ],
    ctx=("Un afiche escolar dice: «Las familias migraron a la ciudad y salieron de la pobreza». ¿Qué problema tiene? A) Ignora la continuidad de la pobreza y la segregación en la ciudad B) Es demasiado corto", "A) Ignora la continuidad de la pobreza y la segregación en la ciudad", "La ficha muestra que la pobreza cambió de lugar."),
    sc=[("En Historia, ¿qué es una causa de atracción?", "Una razón que atrae a una familia hacia un lugar de destino", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una continuidad?", "Un aspecto que sigue igual a pesar de un cambio", "Así se define en la clase."),
        ("=", "Una ciudad de ejemplo tiene 1.800 viviendas y 2.400 familias. ¿Cuántas familias no tienen vivienda propia?", "2400-1800", "Se resta el número de viviendas al de familias.", " familias")],
    op=("Dibuja un esquema con tres columnas: «causas», «cambios» y «continuidades». Escribe dos causas (una de salida y una de atracción), dos cambios y una continuidad de la migración campo-ciudad. Añade una frase que explique cómo se conectan una causa y un cambio. {F}",
        "Causas: salarios bajos en el campo; escuelas en la ciudad. Cambios: crece la población urbana; faltan viviendas. Continuidad: la pobreza. Frase: como llegaron más familias que casas, surgieron viviendas improvisadas.",
        ["distingue causa de salida y de atracción", "separa cambios y continuidades", "conecta una causa con un cambio"], ["esquema de tres columnas", "frase de conexión"], ["poner la pobreza solo como cambio", "no conectar causas y efectos"],
        "Pide que explique por qué la segregación urbana mezcla cambio y continuidad."),
    reinforce="Explica con tus palabras la diferencia entre una causa de salida y una causa de atracción.",
    extend="Observa tu barrio y anota un servicio que esté cerca y uno que esté lejos de tu casa.",
)

# ================================================================ OA 12, clase 5
F = ("Ficha 5 (datos de ejemplo para practicar; no son cifras de un censo real). "
     "Tabla de ejemplo, por cada 100 habitantes de un país imaginario: año 1930, 40 vivían en ciudades; año 1950, 52; año 1970, 68. "
     "Fuente de ejemplo 1 (diario, 1960): «Los cerros se llenan de casas de lata; faltan escuelas.» "
     "Fuente de ejemplo 2 (informe municipal, 1960): «Hay una escuela cada 1.000 niños en los barrios nuevos y una cada 400 en el centro.» "
     "Una interpretación histórica es una explicación del pasado que se sostiene con evidencias y reconoce sus límites. "
     "Estructura: tesis (lo que afirmo), evidencia (datos o fuentes), razonamiento (por qué la evidencia apoya la tesis) y límite (lo que no puedo afirmar).")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre la migración y la pobreza: una tesis con evidencia, razonamiento y un límite.",
    prior=["Sé interrogar fuentes y comparar perspectivas.", "Sé distinguir causas, cambios y continuidades.", "Sé leer una tabla sencilla."],
    explain=[
        "Una interpretación histórica no es una opinión: es una explicación que se sostiene con evidencias. Tiene cuatro partes. La tesis es lo que afirmo. La evidencia son los datos o fuentes que uso. El razonamiento explica por qué esa evidencia apoya la tesis. El límite dice qué no puedo afirmar con lo que tengo.",
        "Con los datos de ejemplo se puede afirmar que en este país imaginario la población urbana aumentó entre 1930 y 1970. Las fuentes de 1960 sugieren que los servicios no crecieron al mismo ritmo en todos los barrios. Esa es una tesis posible, pero hay que cuidar la forma: «sugiere» no es lo mismo que «prueba».",
        "El límite protege contra los errores. Con una tabla y dos fuentes no se puede afirmar qué ocurría en todo el mundo ni en todas las ciudades de ese país. Una buena interpretación dice hasta dónde llega y qué otra evidencia haría falta.",
    ],
    vocab=[("interpretación histórica", "explicación del pasado sostenida con evidencias"), ("tesis", "afirmación central que se quiere sostener"), ("evidencia", "dato o fuente que apoya una afirmación"), ("razonamiento", "explicación de por qué la evidencia apoya la tesis"), ("límite", "aquello que no se puede afirmar con la evidencia disponible")],
    worked=[
        ("Leer una tabla", "En un país imaginario, 35 de cada 100 personas vivían en ciudades en un año y 50 de cada 100 veinte años después. ¿Cuántas personas más por cada 100 vivían en ciudades?", ["Tomo los dos valores.", "Resto: 50 − 35 = 15."], "15 personas más por cada 100"),
        ("Separar tesis y límite", "«Los datos muestran que la población urbana creció, pero no dicen por qué.» ¿Qué parte es el límite?", ["La primera parte afirma algo con datos.", "La segunda dice lo que los datos no permiten afirmar."], "«pero no dicen por qué»"),
    ],
    mistakes=[("Escribir una tesis sin evidencia.", "Se confunde interpretar con opinar.", "Cada afirmación debe ir con un dato o una fuente."),
              ("Usar «prueba» cuando solo hay indicios.", "Se exagera lo que dicen dos fuentes.", "Usa «sugiere» o «indica» y escribe el límite.")],
    T=[
        ("{F} En Historia, ¿qué es la evidencia en una interpretación?", "Un dato o una fuente que apoya una afirmación", "Así se define en el vocabulario."),
        ("{F} ¿Cuántos de cada 100 habitantes vivían en ciudades en 1950 según la tabla de ejemplo?", "52", "El dato está en la tabla de la ficha."),
        ("{F} ¿Qué parte de la interpretación dice lo que no se puede afirmar?", "El límite", "El límite señala hasta dónde llega la evidencia."),
        ("=", "{F} ¿Cuántas personas más por cada 100 vivían en ciudades en 1970 que en 1930?", "68-40", "Se resta el dato de 1930 al de 1970.", " personas"),
        ("{F} ¿Qué frase es una tesis? A) La población urbana aumentó entre 1930 y 1970 B) En 1950 vivían 52 de cada 100 personas en ciudades", "A) La población urbana aumentó entre 1930 y 1970", "Una tesis es una afirmación central que se sostiene con evidencia; el dato de 1950 es evidencia, no la tesis."),
        ("{F} ¿Qué evidencia apoya que los servicios no llegaron igual a todos los barrios? A) El informe municipal de 1960 sobre escuelas B) La tabla de población urbana", "A) El informe municipal de 1960 sobre escuelas", "Compara las escuelas del centro y de los barrios nuevos."),
        ("=", "{F} Según el informe municipal, en el centro hay una escuela cada 400 niños. ¿Cuántas escuelas se necesitarían para 2.000 niños?", "2000/400", "Se divide el número de niños por los que atiende cada escuela.", " escuelas"),
        ("{F} Un estudiante escribe: «La tabla prueba que las ciudades eran peores que el campo». ¿Qué corriges? A) La tabla solo muestra cuánta gente vivía en ciudades, no si vivían peor B) Está bien porque la tabla muestra que las ciudades crecieron", "A) La tabla solo muestra cuánta gente vivía en ciudades, no si vivían peor", "Sus datos no dicen nada sobre calidad de vida."),
        ("{F} Elige la tesis mejor formulada. A) La población urbana creció entre 1930 y 1970 y el informe de 1960 sugiere que los servicios llegaron de forma desigual B) Las ciudades siempre fueron mejores", "A) La población urbana creció entre 1930 y 1970 y el informe de 1960 sugiere que los servicios llegaron de forma desigual", "Se apoya en dos evidencias y usa un verbo prudente."),
        ("{F} ¿Por qué es mejor decir «sugiere» que «prueba» al usar el informe municipal?", "Porque es un solo informe de una fecha y no permite generalizar", "Con una fuente solo hay un indicio."),
        ("{F} ¿Cuál es un límite adecuado para una tesis basada solo en la tabla de ejemplo y las dos fuentes? A) Son datos de ejemplo y pocas fuentes, por lo que no permiten hablar de todas las ciudades B) No tiene límites porque hay una tabla y dos fuentes", "A) Son datos de ejemplo y pocas fuentes, por lo que no permiten hablar de todas las ciudades", "Con pocos datos no se generaliza."),
        ("{F} ¿Qué evidencia adicional fortalecería la tesis sobre desigualdad de servicios? A) Datos de escuelas de otros años y de otras ciudades B) Una opinión sin fecha ni autor", "A) Datos de escuelas de otros años y de otras ciudades", "Más datos comparables reducen el riesgo de generalizar."),
        ("=", "{F} Si en un barrio nuevo hay una escuela cada 1.000 niños y en el centro una cada 400, ¿cuántos niños más atiende cada escuela del barrio nuevo?", "1000-400", "Se resta lo que atiende una escuela del centro a lo que atiende una del barrio nuevo.", " niños"),
    ],
    ctx=("Una compañera dice: «Mi tesis es que la migración fue buena». ¿Qué le falta para que sea una interpretación? A) Evidencia, razonamiento y un límite B) Más entusiasmo", "A) Evidencia, razonamiento y un límite", "Sin evidencia y límite es solo una opinión."),
    sc=[("En Historia, ¿qué es una tesis?", "La afirmación central que se quiere sostener", "Así se define en el vocabulario."),
        ("¿Qué hace el razonamiento?", "Explica por qué la evidencia apoya la tesis", "Así se define en el vocabulario."),
        ("=", "En un país imaginario, 30 de cada 100 personas vivían en ciudades y luego 45 de cada 100. ¿Cuánto aumentó?", "45-30", "Se resta el dato inicial al final.", " personas por cada 100")],
    op=("Escribe una interpretación de cuatro líneas sobre la migración y los servicios en el país imaginario, con tesis, evidencia (cita un dato de la tabla y una fuente de 1960), razonamiento y límite. Usa «sugiere» o «indica» y no «prueba». {F}",
        "Tesis: la población urbana creció y los servicios llegaron de forma desigual. Evidencia: pasó de 40 a 68 de cada 100 y el informe de 1960 muestra más niños por escuela en barrios nuevos. Razonamiento: llegaron más personas que escuelas. Límite: son datos de ejemplo y de una sola fecha.",
        ["incluye las cuatro partes", "cita un dato y una fuente", "evita «prueba»"], ["texto de cuatro líneas"], ["tesis sin evidencia", "olvidar el límite"],
        "Pide que explique qué otra evidencia buscaría para reforzar su tesis."),
    reinforce="Explica con tus palabras las cuatro partes de una interpretación documentada.",
    extend="Escribe una tesis de una línea sobre algún cambio de tu barrio y un dato que la apoyaría.",
)

# ================================================================ OA 12, clase 6
F = ("Ficha 6 (debate sobre consecuencias; fuentes y datos de ejemplo). "
     "Consecuencias positivas posibles de la migración: más acceso a escuela, hospital y trabajo asalariado; organización de los vecinos para exigir servicios. "
     "Consecuencias negativas posibles: hacinamiento (muchas personas en poco espacio), falta de agua y alcantarillado, segregación urbana. "
     "Posición A, de ejemplo: «La migración mejoró la vida de muchas familias porque llegaron a escuelas y hospitales.» "
     "Posición B, de ejemplo: «La migración trasladó la pobreza a los bordes de la ciudad y la volvió más visible.» "
     "Dato de ejemplo: una casa de dos piezas alberga a 9 personas. "
     "Estructura del argumento: tesis, razón, evidencia y contraargumento (la objeción más fuerte a mi tesis).")
build(
    OA, 6, F,
    use="Aprenderé a debatir las consecuencias de la migración campo-ciudad reconociendo ventajas, costos y los límites de lo que sé.",
    prior=["Sé construir una interpretación con tesis, evidencia y límite.", "Sé comparar perspectivas.", "Sé reconocer causas, cambios y continuidades."],
    explain=[
        "Debatir consecuencias es evaluar qué efectos tuvo un proceso y para quién. La migración dio a muchas familias acceso a escuelas, hospitales y trabajo con salario. A la vez produjo hacinamiento, falta de servicios y segregación. Ambos efectos ocurrieron, y un buen debate no oculta ninguno.",
        "Un argumento sólido tiene una tesis, una razón y evidencia. Además considera un contraargumento, que es la objeción más fuerte contra mi posición. Responder al contraargumento muestra que entiendo el tema y no solo defiendo una idea.",
        "También hay que decir los límites. Con un caso o una fuente no se puede afirmar que algo ocurrió en todas partes. Debatir no es ganar: es mostrar razones claras, respetar a quien piensa distinto y aceptar que la evidencia puede cambiar mi postura.",
    ],
    vocab=[("hacinamiento", "situación en que muchas personas viven en un espacio muy pequeño"), ("consecuencia", "efecto que sigue a un proceso"), ("contraargumento", "objeción más fuerte contra la propia tesis"), ("argumento", "razón con evidencia para sostener una tesis"), ("alcantarillado", "red que retira las aguas servidas de las viviendas")],
    worked=[
        ("Calcular hacinamiento", "Una pieza de ejemplo la ocupan 6 personas en 12 metros cuadrados. ¿Cuántos metros cuadrados corresponden a cada persona?", ["Divido el espacio entre las personas.", "12 ÷ 6 = 2."], "2 metros cuadrados por persona"),
        ("Identificar un contraargumento", "Tesis: «La migración mejoró la vida de las familias». ¿Cuál es su contraargumento más fuerte?", ["Busco una razón que la contradiga.", "Muchas familias quedaron en viviendas sin agua ni alcantarillado."], "Muchas familias quedaron en viviendas sin agua ni alcantarillado"),
    ],
    mistakes=[("Defender una posición sin considerar el contraargumento.", "Se piensa que reconocer una objeción debilita el argumento.", "Nómbrala y respóndela con evidencia."),
              ("Decir que la migración fue «buena» o «mala» sin precisar para quién.", "Se juzga todo el proceso con un solo criterio.", "Indica quién ganó, quién perdió y en qué aspecto.")],
    T=[
        ("{F} En Historia, ¿qué es el hacinamiento?", "Que muchas personas vivan en un espacio muy pequeño", "Así se define en el vocabulario."),
        ("{F} ¿Cuál es una consecuencia positiva posible de la migración? A) Más acceso a escuela, hospital y trabajo asalariado B) Hacinamiento y falta de alcantarillado", "A) Más acceso a escuela, hospital y trabajo asalariado", "La ficha ubica el hacinamiento y la falta de servicios entre las consecuencias negativas."),
        ("{F} ¿Qué posición dice que la pobreza se trasladó a los bordes de la ciudad?", "La posición B", "Esa es la afirmación de la posición B."),
        ("=", "{F} ¿Cuántas personas deberían salir de la casa de dos piezas para que quedaran 3 en cada pieza?", "9-2*3", "Se multiplican las 2 piezas por 3 personas y se resta de las 9 que viven allí.", " personas"),
        ("{F} Una familia llega a la ciudad y sus hijos entran a una escuela. ¿Qué tipo de consecuencia es? A) Positiva B) Negativa", "A) Positiva", "Obtener acceso a escuela es una consecuencia positiva de la ficha."),
        ("{F} Un sector sin alcantarillado y con casas muy juntas. ¿Qué consecuencia negativa muestra? A) Falta de servicios y hacinamiento B) Más acceso a escuelas", "A) Falta de servicios y hacinamiento", "La ficha asocia esas condiciones a consecuencias negativas."),
        ("{F} Alguien dice: «La posición A y la posición B se contradicen totalmente». ¿Cómo lo corriges? A) Ambas pueden ser verdaderas, pues describen efectos distintos para grupos distintos B) Tiene razón, solo una puede serlo", "A) Ambas pueden ser verdaderas, pues describen efectos distintos para grupos distintos", "Un proceso puede tener efectos positivos y negativos a la vez."),
        ("=", "{F} Una pieza de ejemplo de 15 metros cuadrados la ocupan 5 personas. ¿Cuántos metros cuadrados tiene cada una?", "15/5", "Se divide el espacio entre las personas.", " metros cuadrados"),
        ("{F} Para apoyar la posición B conviene usar como evidencia: A) Un informe con datos de viviendas sin agua en barrios de borde B) Un recuerdo vago de alguien", "A) Un informe con datos de viviendas sin agua en barrios de borde", "Un informe con datos sustenta mejor que un recuerdo sin fecha."),
        ("{F} Una estudiante defiende la posición A y responde con datos la objeción más fuerte de la posición B. ¿Qué logra? A) Un argumento que resiste mejor las críticas B) Un argumento que ya no necesita evidencia", "A) Un argumento que resiste mejor las críticas", "Responder la objeción más fuerte muestra que el argumento resiste; la evidencia sigue siendo necesaria."),
        ("{F} Un compañero escribe: «La migración fue totalmente mala». ¿Qué le falta? A) Reconocer las consecuencias positivas y el límite de sus datos B) Más adjetivos", "A) Reconocer las consecuencias positivas y el límite de sus datos", "La ficha muestra efectos positivos y negativos."),
        ("{F} Solo conoces los datos de un barrio de ejemplo. ¿Qué límite corresponde? A) No puedo afirmar que lo mismo ocurrió en todas las ciudades B) Los datos de un barrio sirven para describir a todo el país", "A) No puedo afirmar que lo mismo ocurrió en todas las ciudades", "Un caso no basta para generalizar."),
        ("{F} ¿Qué postura es la más prudente? A) La migración tuvo ventajas y costos, y su balance depende del grupo y del lugar B) La migración solo trajo ventajas", "A) La migración tuvo ventajas y costos, y su balance depende del grupo y del lugar", "Considera ambos tipos de efectos y reconoce variaciones."),
    ],
    ctx=("En una clase se debate si «la migración campo-ciudad fue positiva». Una estudiante empieza diciendo: «Para las familias que accedieron a escuela, sí; sin embargo, para quienes quedaron sin agua en los bordes, hubo costos». ¿Qué hace bien? A) Considera efectos distintos según el grupo B) Evita dar su opinión", "A) Considera efectos distintos según el grupo", "Distingue para quién fue positiva y para quién negativa."),
    sc=[("En Historia, ¿qué es un contraargumento?", "La objeción más fuerte contra la propia tesis", "Así se define en el vocabulario."),
        ("¿Por qué conviene decir los límites en un debate?", "Porque un caso o una fuente no permite generalizar", "Así se explica en la clase."),
        ("=", "Un cuarto de ejemplo de 20 metros cuadrados lo ocupan 4 personas. ¿Cuántos metros cuadrados tiene cada una?", "20/4", "Se divide el espacio entre las personas.", " metros cuadrados")],
    op=("Prepara un mini debate escrito: elige la posición A o la B de la ficha y escribe tesis, una razón, una evidencia (inventa un dato rotulado «de ejemplo») y el contraargumento más fuerte con tu respuesta. Termina con una línea que diga qué evidencia podría cambiar tu postura. {F}",
        "Tesis: la migración mejoró el acceso a servicios. Razón: llegaron a escuelas y hospitales. Evidencia (de ejemplo): 30 niños nuevos matriculados. Contraargumento: faltaban viviendas. Respuesta: aun así más niños accedieron a clases. Cambiaría de postura si el dato mostrara que no había cupos.",
        ["incluye tesis, razón, evidencia y contraargumento", "rotula como ejemplo los datos inventados", "dice qué evidencia cambiaría su postura"], ["texto de seis líneas"], ["ignorar el contraargumento", "presentar datos inventados como reales"],
        "Pide que explique por qué un buen debatiente puede cambiar de postura."),
    reinforce="Explica a alguien de tu casa una ventaja y un costo de la migración campo-ciudad, con razones.",
    extend="Escribe una pregunta de debate sobre vivienda en tu comuna que se pueda responder con datos.",
)

OA = "HI2M OA 13"

# ================================================================ OA 13, clase 1
F = ("Ficha 1 (los años sesenta son 1960 a 1969; hechos generales y datos de ejemplo rotulados). "
     "Actores sociales nuevos u organizados: jóvenes (estudiantes de escuelas y universidades), campesinado (trabajadores del campo que pedían tierra y mejores condiciones), pobladores (familias que vivían en poblaciones y exigían vivienda y servicios). "
     "Sistema político: partidos de derecha, de centro y de izquierda que competían por votos. "
     "Hechos: en 1964 fue elegido presidente Eduardo Frei Montalva, de la Democracia Cristiana, con el lema «revolución en libertad»; en 1970 fue elegido Salvador Allende, de la Unidad Popular, con el proyecto de la «vía chilena al socialismo». "
     "Cada período presidencial duraba seis años. "
     "Dato de ejemplo: un sindicato campesino pasó de 40 a 75 afiliados en un año.")
build(
    OA, 1, F,
    use="Aprenderé a situar la década de 1960 en Chile: quiénes se organizaron, qué pedían y cuáles fueron los dos grandes proyectos políticos que gobernaron al final de la década.",
    prior=["Conozco la pobreza y la migración campo-ciudad a mediados del siglo XX.", "Sé qué es un partido político y una elección.", "Sé calcular diferencias entre años."],
    explain=[
        "En la década de 1960 se organizaron y movilizaron grupos que antes tenían poca voz. Los jóvenes participaron en escuelas y universidades; el campesinado formó sindicatos para pedir tierra y mejores condiciones; los pobladores se organizaron para exigir vivienda y servicios. Se llaman actores sociales porque actúan colectivamente para lograr cambios.",
        "El sistema político, formado por partidos de derecha, centro e izquierda, tuvo que responder a esas demandas. En 1964 ganó Eduardo Frei Montalva, de la Democracia Cristiana, que propuso la «revolución en libertad», un conjunto de reformas. En 1970 ganó Salvador Allende, de la Unidad Popular, que propuso la «vía chilena al socialismo».",
        "Un proyecto político es un plan de país con metas y métodos. Los dos proyectos buscaban cambios profundos, pero eran distintos. Para estudiarlos conviene preguntar quién lo propone, a quién representa y qué pide, y recordar que cada gobierno duraba seis años.",
    ],
    vocab=[("actor social", "grupo que actúa colectivamente para lograr cambios"), ("campesinado", "trabajadores del campo que pedían tierra y mejores condiciones"), ("pobladores", "familias de poblaciones que exigían vivienda y servicios"), ("proyecto político", "plan de país con metas y métodos para lograrlas"), ("reforma", "cambio de leyes o instituciones sin cambiar todo el sistema")],
    worked=[
        ("Calcular un período", "Un presidente asume en 1958 y gobierna seis años. ¿En qué año termina su período?", ["Sumo la duración al año de inicio.", "1958 + 6 = 1964."], "1964"),
        ("Identificar un actor", "Un grupo de familias sin casa organiza una toma de terreno y negocia con el municipio. ¿Qué actor social es?", ["Son familias de poblaciones.", "Exigen vivienda y servicios."], "Pobladores"),
    ],
    mistakes=[("Decir que los pobladores y el campesinado eran el mismo actor.", "Se mezclan grupos con demandas distintas: vivienda en la ciudad y tierra en el campo.", "Define cada actor con su lugar y su demanda."),
              ("Confundir el lema de un proyecto con el de otro.", "Se memorizan frases sin relacionarlas con el partido que las usó.", "Une cada lema con su gobierno y su año.")],
    T=[
        ("{F} ¿Qué lema usó la Democracia Cristiana en 1964?", "«Revolución en libertad»", "La ficha lo indica."),
        ("{F} ¿Qué proyecto propuso Allende?", "La «vía chilena al socialismo»", "La ficha lo asocia a la Unidad Popular."),
        ("{F} ¿Quiénes eran los pobladores?", "Familias que vivían en poblaciones y exigían vivienda y servicios", "Así los define la ficha."),
        ("=", "{F} Allende fue elegido en 1970. Si hubiera completado su período presidencial, ¿en qué año habría terminado?", "1970+6", "Se suma al año de elección la duración de un período, seis años."),
        ("{F} Un sindicato de peones de un fundo pide tierra y mejores salarios. ¿Qué actor social es? A) El campesinado B) Los pobladores", "A) El campesinado", "Trabajan en el campo y piden tierra."),
        ("{F} Un grupo de estudiantes pide cambios en su escuela mediante asambleas. ¿Qué actor social representa? A) Los jóvenes B) El campesinado", "A) Los jóvenes", "Son estudiantes organizados."),
        ("{F} Un grupo de familias de una población organiza una marcha para pedir agua, luz y escuela. ¿Qué actor social es? A) Los pobladores B) El campesinado", "A) Los pobladores", "Viven en poblaciones de la ciudad y exigen vivienda y servicios."),
        ("=", "{F} El sindicato campesino de ejemplo, ¿cuántos afiliados ganó en un año?", "75-40", "Se resta el número inicial al final.", " afiliados"),
        ("{F} «Revolución en libertad» y «vía chilena al socialismo» son: A) Proyectos políticos de dos gobiernos distintos B) Dos nombres para el mismo gobierno", "A) Proyectos políticos de dos gobiernos distintos", "Corresponden a Frei Montalva y a Allende."),
        ("{F} ¿Por qué se llama «actor social» a un sindicato campesino?", "Porque actúa colectivamente para lograr cambios", "Un actor social actúa en conjunto, no como individuo."),
        ("{F} Un compañero dice: «En los sesenta nadie se organizaba y los partidos decidían todo». ¿Qué respondes? A) La ficha muestra jóvenes, campesinado y pobladores organizados B) Tiene razón porque los partidos competían por votos", "A) La ficha muestra jóvenes, campesinado y pobladores organizados", "Hubo actores sociales que presionaban al sistema político."),
        ("¿Cuál es la mejor pregunta para investigar este tema? A) ¿Qué demandas tuvieron los nuevos actores sociales en los años sesenta y cómo respondieron los proyectos políticos? B) ¿Quién fue el mejor presidente de Chile?", "A) ¿Qué demandas tuvieron los nuevos actores sociales en los años sesenta y cómo respondieron los proyectos políticos?", "La pregunta A se responde con hechos y fuentes; la B es una opinión sin criterio."),
        ("{F} ¿Por qué un proyecto político es más que un lema?", "Porque tiene metas y métodos para lograrlas, no solo una frase", "El vocabulario lo define como plan de país."),
    ],
    ctx=("Una línea de tiempo escolar dice: «1964: revolución en libertad; 1970: vía chilena al socialismo». ¿Qué más conviene agregar para situar bien el tema? A) Los actores sociales que se organizaban y sus demandas B) Solo más fechas de la misma década", "A) Los actores sociales que se organizaban y sus demandas", "Los proyectos respondían a demandas de actores concretos."),
    sc=[("En Historia, ¿qué es un actor social?", "Un grupo que actúa colectivamente para lograr cambios", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es un proyecto político?", "Un plan de país con metas y métodos para lograrlas", "Así se define en la clase."),
        ("=", "Un presidente asume en 1964 y gobierna seis años completos. ¿En qué año termina su período?", "1964+6", "Se suma la duración del período al año de inicio.")],
    op=("Haz un cuadro de tres filas, una por actor social (jóvenes, campesinado, pobladores). En cada fila escribe dónde actuaba y qué pedía. Debajo, escribe en dos líneas qué proyecto político llegó al gobierno en 1964 y cuál en 1970, con su lema. {F}",
        "Jóvenes: escuelas y universidades, participación y cambios en la educación. Campesinado: campo, tierra y mejores condiciones. Pobladores: poblaciones de la ciudad, vivienda y servicios. 1964: Democracia Cristiana, «revolución en libertad». 1970: Unidad Popular, «vía chilena al socialismo».",
        ["describe lugar y demanda de cada actor", "une cada lema con su gobierno", "usa los años correctos"], ["cuadro de tres filas", "dos líneas sobre los proyectos"], ["mezclar las demandas de campesinado y pobladores", "intercambiar los lemas"],
        "Pide que explique qué hace distintos a un actor social y a un partido político."),
    reinforce="Explica con tus palabras quiénes eran los pobladores, el campesinado y los jóvenes en los años sesenta.",
    extend="Pregunta a una persona mayor de tu casa qué cambios recuerda de esa época o qué ha oído; anota una frase sin datos personales.",
)

# ================================================================ OA 13, clase 2
F = ("Ficha 2 (tres fuentes de ejemplo escritas para este cuaderno; no son documentos históricos reales). "
     "Fuente A, programa de campaña de un partido de centro, 1964: «Haremos reformas profundas respetando la libertad de las personas y las instituciones.» "
     "Fuente B, carta de un dirigente campesino a un periódico, 1967: «Hace años trabajamos tierras ajenas; esperamos que la ley nos permita tener las nuestras y formar sindicato.» "
     "Fuente C, columna de un diario de oposición, 1968: «Las reformas se hacen con apuro y sin escuchar a quienes producen.» "
     "Fuente D, canción de ejemplo de un cantor popular, 1969: «Pobladores, a levantar la voz por la casa que nos falta.»")
build(
    OA, 2, F,
    use="Aprenderé a interrogar fuentes políticas de los años sesenta por su procedencia, su intención y su público, y a no tomar un lema o una columna como prueba de un hecho.",
    prior=["Sé qué es la procedencia de una fuente.", "Conozco a los actores sociales de los años sesenta.", "Sé distinguir hecho de opinión."],
    explain=[
        "Las fuentes políticas casi siempre quieren convencer. Un programa de campaña presenta lo que el partido promete; una carta de un dirigente expresa lo que piden sus representados; una columna de oposición critica al gobierno; una canción busca emocionar y reunir. Ninguna es neutral, pero todas muestran cómo pensaba quien las produjo.",
        "Para interrogarlas hay que preguntar quién habla, a quién le habla, cuándo y para qué. La intención es el propósito del autor y el público es a quien se dirige. Un programa promete, pero no prueba que lo prometido se haya cumplido; una crítica opina, pero puede apuntar a un problema real que otros datos deben confirmar.",
        "La propaganda es un mensaje diseñado para influir en la opinión. No es un insulto: sirve para conocer la intención del autor. Lo que no se debe hacer es tratar un lema como un dato, ni usar una sola fuente para hablar por todos los grupos.",
    ],
    vocab=[("programa de campaña", "documento donde un partido o candidato promete lo que hará si gana"), ("intención", "propósito del autor al producir una fuente"), ("público", "personas a quienes se dirige el mensaje de una fuente"), ("propaganda", "mensaje diseñado para influir en la opinión"), ("oposición", "grupos que critican o se enfrentan al gobierno")],
    worked=[
        ("Distinguir promesa y hecho", "Un afiche de 1965 dice «Construiremos escuelas en cada barrio». ¿Prueba que se construyeron?", ["Es una promesa de campaña o gobierno.", "Faltan datos o registros de las escuelas construidas."], "No, solo muestra lo que se prometía"),
        ("Preguntar por el público", "Un volante repartido en una feria rural pide organizar un sindicato. ¿A quién se dirige?", ["Se distribuye entre personas del campo.", "El mensaje habla de sindicato."], "Al campesinado"),
    ],
    mistakes=[("Usar un lema como si fuera un dato.", "Se confunde lo que un actor dice de sí mismo con lo que ocurrió.", "Contrasta el lema con registros o leyes."),
              ("Descartar una fuente de oposición por ser crítica.", "Se cree que una crítica nunca puede apuntar a algo real.", "Úsala para conocer la crítica y compárala con otros datos.")],
    T=[
        ("{F} ¿Qué fuente es una carta de un dirigente campesino?", "La fuente B", "La ficha la rotula así."),
        ("{F} ¿Qué fuente critica a las reformas por apuradas?", "La fuente C, la columna del diario de oposición", "Esa columna habla de reformas hechas con apuro."),
        ("{F} ¿En qué año es la fuente D?", "1969", "La ficha la ubica en 1969."),
        ("{F} En la fuente B, el dirigente espera que la ley les permita tener tierras y formar sindicato. ¿Qué demanda del campesinado expresa? A) Acceso a la tierra y organización sindical B) Vivienda en la ciudad", "A) Acceso a la tierra y organización sindical", "Pide tierras y sindicato; la vivienda en la ciudad es demanda de pobladores."),
        ("{F} En Historia, ¿qué es la intención de una fuente? A) El propósito del autor al producirla B) Su cantidad de páginas", "A) El propósito del autor al producirla", "La intención es lo que el autor quiere lograr."),
        ("{F} La fuente A, ¿qué tipo de documento es? A) Programa de campaña B) Informe de un censo", "A) Programa de campaña", "Un partido promete lo que hará si gana."),
        ("{F} ¿A quién se dirige la fuente D? A) A los pobladores B) A los dueños de fundos", "A) A los pobladores", "Los llama directamente y habla de la casa que falta."),
        ("{F} La fuente A promete reformas respetando la libertad. ¿Qué puede afirmarse con ella? A) Que el partido prometía reformas sin romper las instituciones B) Que todas las reformas se cumplieron", "A) Que el partido prometía reformas sin romper las instituciones", "Un programa muestra promesas, no resultados."),
        ("{F} ¿Cuál fuente fue escrita por un partido que quería convencer a los votantes de que lo eligieran? A) La fuente A, el programa de campaña B) La fuente B, la carta del dirigente", "A) La fuente A, el programa de campaña", "Un programa de campaña promete para ganar votos; la carta cuenta una esperanza del dirigente."),
        ("{F} ¿Por qué la fuente C sirve aunque sea crítica?", "Porque muestra cómo pensaba la oposición, aunque debe contrastarse con otros datos", "Una crítica expresa una perspectiva que se debe corroborar."),
        ("{F} Alguien dice: «La carta B prueba que todos los campesinos de Chile pensaban igual». ¿Qué respondes? A) Es la carta de un dirigente y no habla por todos B) Tiene razón porque lo dice un dirigente", "A) Es la carta de un dirigente y no habla por todos", "El alcance de la fuente es limitado."),
        ("{F} ¿Qué dos fuentes sirven mejor para comparar posiciones distintas sobre las reformas? A) La B y la C B) La B y la D", "A) La B y la C", "Una espera la ley y otra critica las reformas; la B y la D piden cambios y no se oponen."),
        ("{F} ¿Qué pregunta de procedencia sirve para la fuente D? A) ¿Quién la compuso, para qué público y con qué intención? B) ¿Me gusta la canción?", "A) ¿Quién la compuso, para qué público y con qué intención?", "Reúne autor, público e intención; el gusto personal no es una pregunta de procedencia."),
    ],
    ctx=("Un afiche de 1969 dice «¡Todo cambió para bien!». Tu profesor te pide usarlo como prueba. ¿Qué haces? A) Averiguar quién lo hizo y para qué, y contrastarlo con datos B) Usarlo tal cual porque es de la época", "A) Averiguar quién lo hizo y para qué, y contrastarlo con datos", "Un afiche es propaganda y no basta como prueba."),
    sc=[("En Historia, ¿qué es la propaganda?", "Un mensaje diseñado para influir en la opinión", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es el público de una fuente?", "Las personas a quienes se dirige su mensaje", "Así se define en el vocabulario."),
        ("Un afiche de campaña de 1964 promete casas para todos. ¿Prueba que se construyeron? A) No, solo muestra lo que se prometía B) Sí, porque es de la época", "A) No, solo muestra lo que se prometía", "Un afiche de campaña es una promesa; para saber si se cumplió se necesitan registros.")],
    op=("Elige dos fuentes de la ficha (A, B, C o D). Para cada una escribe: quién habla, a quién le habla, qué intención tiene y qué no podrías afirmar con ella. Termina con una línea que diga qué otra fuente usarías para contrastarlas. {F}",
        "Fuente B: un dirigente campesino; habla a un periódico; quiere apoyar una ley para tener tierra; no prueba lo que pensaban todos los campesinos. Fuente C: un diario de oposición; habla a lectores; critica las reformas; no prueba que las reformas fueran apuradas. Contraste: el texto de las leyes o datos de ejemplo.",
        ["responde las cuatro preguntas para cada fuente", "señala un límite real de cada una", "propone una fuente para contrastar"], ["dos fichas de análisis", "línea de contraste"], ["tomar el lema como dato", "no indicar los límites"],
        "Pide que explique por qué una canción también es una fuente histórica."),
    reinforce="Explica en voz alta por qué un programa de campaña muestra promesas y no resultados.",
    extend="Mira un aviso o cartel de hoy y anota su intención y su público en una línea.",
)

# ================================================================ OA 13, clase 3
F = ("Ficha 3 (comparación de dos proyectos; resumen general para este cuaderno). "
     "Democracia Cristiana, gobierno de Frei Montalva, desde 1964: lema «revolución en libertad»; proponía reformas profundas dentro de las instituciones democráticas y sin cambiar todo el sistema económico; entre ellas, una reforma agraria y la organización de campesinos y pobladores. "
     "Unidad Popular, gobierno de Allende, desde 1970: proyecto de la «vía chilena al socialismo»; proponía transformar la economía hacia el socialismo, ampliando el papel del Estado en las industrias y en la propiedad de la tierra, por una vía democrática y sin violencia. "
     "Apoyos de la Democracia Cristiana: sectores medios y parte del campesinado y de los pobladores. Apoyos de la Unidad Popular: partidos de izquierda como el Socialista y el Comunista, sindicatos de trabajadores y sectores de pobladores y campesinos. Cada proyecto también recibió la crítica de otros grupos. "
     "Escalas: nacional (las decisiones del gobierno), local (cómo se vivía en un fundo o una población). "
     "Dato de ejemplo: un fundo de ejemplo con 120 trabajadores.")
build(
    OA, 3, F,
    use="Aprenderé a comparar los proyectos de la Democracia Cristiana y de la Unidad Popular con criterios claros: método, rol del Estado y apoyos, sin tomar partido.",
    prior=["Conozco los lemas y años de ambos proyectos.", "Sé interrogar fuentes políticas.", "Sé comparar con un criterio."],
    explain=[
        "Comparar dos proyectos exige usar los mismos criterios. Aquí usamos tres: el objetivo (qué buscaba cambiar), el método (cómo pretendía hacerlo) y los apoyos (quiénes lo respaldaban). La Democracia Cristiana buscaba reformas profundas dentro de las instituciones y sin cambiar todo el sistema económico. La Unidad Popular buscaba transformar la economía hacia el socialismo.",
        "Ambos proyectos declaraban que Chile necesitaba cambios y que debían hacerse por vías democráticas, sin violencia. Se diferenciaban en el alcance: la reforma frente a la transformación hacia el socialismo, y en cuánto debía crecer el papel del Estado en la economía. Comparar no es decidir cuál era mejor, sino explicar con claridad las semejanzas y diferencias.",
        "También conviene cambiar de escala. En la escala nacional se miran las leyes y decisiones del gobierno; en la local, cómo cambió la vida en un fundo o en una población. Y no hay que olvidar que ambos proyectos tenían apoyos y críticas, y que cada actor los vio desde su posición.",
    ],
    vocab=[("objetivo", "meta que un proyecto busca lograr"), ("método", "forma que se propone para lograr una meta"), ("apoyos", "grupos que respaldan un proyecto"), ("socialismo", "sistema en que los principales medios de producción pasan a propiedad social o estatal, con el fin de reducir la desigualdad"), ("criterio", "aspecto común usado para comparar")],
    worked=[
        ("Aplicar un criterio", "Si el criterio es «método», ¿qué dice la ficha de la Unidad Popular?", ["Busco cómo pretendía lograr el cambio.", "La ficha dice: por una vía democrática y sin violencia."], "Por una vía democrática y sin violencia"),
        ("Dividir un fundo", "Un fundo de ejemplo con 90 trabajadores se organiza en grupos de 15 para una reunión. ¿Cuántos grupos hay?", ["Divido el total por el tamaño de cada grupo.", "90 ÷ 15 = 6."], "6 grupos"),
    ],
    mistakes=[("Comparar con criterios distintos para cada proyecto.", "Se describe uno por su método y el otro por sus apoyos.", "Elige tres criterios y aplícalos a ambos."),
              ("Decir que un proyecto era «bueno» y el otro «malo».", "Se confunde comparar con juzgar.", "Describe semejanzas y diferencias y deja el juicio para el debate.")],
    T=[
        ("{F} ¿Qué lema usó la Democracia Cristiana?", "«Revolución en libertad»", "La ficha lo indica."),
        ("{F} Según el criterio «método», ¿cómo pretendía actuar la Unidad Popular?", "Por una vía democrática y sin violencia", "La ficha lo dice."),
        ("{F} ¿Qué proyecto proponía transformar la economía hacia el socialismo?", "La Unidad Popular", "La ficha lo atribuye a ese proyecto."),
        ("{F} ¿Qué grupos apoyaban a la Democracia Cristiana según la ficha? A) Sectores medios y parte del campesinado y de los pobladores B) Los partidos de izquierda como el Socialista y el Comunista", "A) Sectores medios y parte del campesinado y de los pobladores", "El Partido Socialista y el Comunista aparecen entre los apoyos de la Unidad Popular."),
        ("{F} ¿En qué coincidían los dos proyectos? A) En que se necesitaban cambios por vías democráticas B) En ampliar la economía estatal en la misma medida", "A) En que se necesitaban cambios por vías democráticas", "La ficha señala el uso de vías democráticas en ambos; difieren en el alcance."),
        ("{F} ¿Qué criterio permite comparar a quiénes respaldaba cada proyecto? A) Los apoyos B) El método", "A) Los apoyos", "Los apoyos son los grupos que respaldaban."),
        ("{F} Un compañero compara un proyecto por su método y el otro por sus apoyos. ¿Qué error comete? A) Usa criterios distintos para cada uno B) Compara demasiado", "A) Usa criterios distintos para cada uno", "Para comparar hay que aplicar los mismos criterios."),
        ("=", "{F} El fundo de ejemplo tiene 120 trabajadores y se forman asambleas de 20 personas. ¿Cuántas asambleas hay?", "120/20", "Se divide el total entre el tamaño de cada asamblea.", " asambleas"),
        ("{F} ¿Qué escala usa el estudio de cómo se vivía un cambio en un fundo concreto? A) Local B) Nacional", "A) Local", "Mira un solo fundo."),
        ("{F} ¿Por qué comparar dos proyectos con criterios no es lo mismo que decidir cuál era mejor?", "Porque comparar describe semejanzas y diferencias y no emite un juicio", "El juicio exige otros criterios y evidencias."),
        ("{F} Alguien afirma: «Los dos proyectos eran idénticos porque ambos querían cambios». ¿Qué corriges? A) Coincidían en cambiar, pero diferían en el alcance de la transformación de la economía B) Nada, es correcto", "A) Coincidían en cambiar, pero diferían en el alcance de la transformación de la economía", "Que ambos quisieran cambios no los hace iguales."),
        ("{F} ¿Qué diferencia muestra la ficha en el papel del Estado?", "La Unidad Popular proponía ampliar más el papel del Estado en industrias y tierra", "La ficha lo dice al describir ese proyecto."),
        ("{F} ¿Qué evidencia ayudaría a comparar cómo se recibió cada proyecto en la escala local? A) Testimonios de personas de un fundo o una población de esos años B) Un mapa de Europa", "A) Testimonios de personas de un fundo o una población de esos años", "Muestra la vida cotidiana en la escala local."),
    ],
    ctx=("En una clase se pide comparar los dos proyectos. Una estudiante escribe: «El proyecto de Frei era mejor porque era más moderado». ¿Qué falta? A) Criterios y evidencias, porque «mejor» es un juicio sin comparación B) Una opinión más fuerte", "A) Criterios y evidencias, porque «mejor» es un juicio sin comparación", "La comparación necesita criterios comunes y datos."),
    sc=[("En Historia, ¿qué es un criterio de comparación?", "Un aspecto común usado para comparar", "Así se define en el vocabulario."),
        ("Nombra los tres criterios que usa esta clase.", "Objetivo, método y apoyos", "La explicación los enumera."),
        ("=", "Un sindicato de ejemplo reúne 60 personas en equipos de 12. ¿Cuántos equipos son?", "60/12", "Se divide el total entre el tamaño de cada equipo.", " equipos")],
    op=("Haz una tabla de comparación con tres filas (objetivo, método, apoyos) y dos columnas (Democracia Cristiana y Unidad Popular). Completa cada casilla en una línea. Debajo escribe una semejanza y una diferencia. Evita las palabras «mejor» y «peor». {F}",
        "Objetivo: reformas profundas / transformar la economía hacia el socialismo. Método: dentro de las instituciones y sin cambiar todo el sistema / por una vía democrática ampliando el Estado. Apoyos: sectores medios, campesinos y pobladores / partidos de izquierda, sindicatos, pobladores y campesinos. Semejanza: ambos pedían cambios por vías democráticas. Diferencia: el alcance de la transformación económica.",
        ["usa los mismos criterios para ambos", "incluye una semejanza y una diferencia", "no emite juicios"], ["tabla de seis casillas", "línea de semejanza y diferencia"], ["usar criterios distintos para cada proyecto", "decir cuál era mejor"],
        "Pide que explique por qué comparar no obliga a elegir un proyecto."),
    reinforce="Explica a alguien de tu casa las semejanzas y diferencias entre los dos proyectos sin decir cuál era mejor.",
    extend="Compara dos opciones de tu vida diaria con tres criterios y escribe el resultado en cuatro líneas.",
)

# ================================================================ OA 13, clase 4
F = ("Ficha 4 (causas, cambios y continuidades de las reformas de los años sesenta). "
     "Contexto: en 1959 triunfó la Revolución cubana y en 1961 Estados Unidos lanzó la Alianza para el Progreso, un programa para impulsar reformas en América Latina; en Chile, gran parte de la tierra estaba en pocos fundos y el campesinado pedía acceso a ella. "
     "Causas: demandas de campesinado, jóvenes y pobladores; desigualdad en la tierra y en la vivienda; temor de unos a una revolución y deseo de otros de realizarla; influencia de la Guerra Fría. "
     "Cambios: en 1967 se aprobó una ley de Reforma Agraria y una ley de sindicalización campesina; se organizaron más sindicatos y organizaciones de pobladores; creció la participación en la educación. "
     "Continuidades: persistía la desigualdad y muchas familias seguían sin vivienda adecuada. "
     "Dato de ejemplo: un fundo de ejemplo de 1.200 hectáreas se divide en parcelas de 40 hectáreas.")
build(
    OA, 4, F,
    use="Aprenderé a relacionar las causas de las reformas de los años sesenta con sus cambios y continuidades, y a distinguir una causa de un contexto.",
    prior=["Conozco los proyectos de la Democracia Cristiana y de la Unidad Popular.", "Sé distinguir causa de largo plazo y detonante.", "Sé que la Guerra Fría fue una confrontación entre dos bloques."],
    explain=[
        "Las reformas de los años sesenta tuvieron varias causas. Una fue la desigualdad: mucha tierra estaba en pocos fundos y muchas familias no tenían casa. Otra fue la presión de actores sociales organizados: campesinado, jóvenes y pobladores. Otra fue el contexto de la Guerra Fría, con la Revolución cubana de 1959 y la Alianza para el Progreso de 1961, que alentaron reformas en América Latina.",
        "Entre los cambios, en 1967 se aprobaron la ley de Reforma Agraria y la ley de sindicalización campesina. Con esas leyes el Estado intervino en la propiedad de la tierra y los campesinos pudieron organizarse en sindicatos. También creció la participación social en la educación y en las poblaciones.",
        "Las continuidades son lo que no cambió: la desigualdad persistía y muchas familias seguían sin vivienda adecuada. Por eso no se puede decir que una ley «resolvió» el problema. Una buena explicación nombra causas distintas, separa el contexto de las causas directas y reconoce lo que siguió igual.",
    ],
    vocab=[("reforma agraria", "cambio de leyes para redistribuir la propiedad de la tierra"), ("sindicalización campesina", "organización de los trabajadores del campo en sindicatos"), ("Alianza para el Progreso", "programa de 1961 de Estados Unidos para impulsar reformas en América Latina"), ("contexto", "situación general en que ocurre un hecho"), ("expropiar", "quitar la propiedad a su dueño por ley, con compensación, para un fin público")],
    worked=[
        ("Separar causa y contexto", "La Guerra Fría, ¿es causa directa de la reforma agraria chilena o parte del contexto?", ["Influyó en América Latina de forma general.", "No fue la demanda concreta del campesinado por tierra."], "Parte del contexto"),
        ("Dividir tierra", "Un fundo de ejemplo de 600 hectáreas se divide en parcelas de 30 hectáreas. ¿Cuántas parcelas resultan?", ["Divido el total entre el tamaño de cada parcela.", "600 ÷ 30 = 20."], "20 parcelas"),
    ],
    mistakes=[("Explicar la reforma agraria solo por la influencia de otros países.", "Se ignoran las demandas internas del campesinado y la desigualdad en la tierra.", "Nombra causas internas y externas."),
              ("Creer que la ley de 1967 acabó con la desigualdad.", "Se confunde aprobar una ley con resolver el problema.", "Separa lo que cambió de lo que siguió igual.")],
    T=[
        ("{F} ¿En qué año se aprobó la ley de Reforma Agraria?", "1967", "La ficha lo indica."),
        ("{F} ¿Qué programa lanzó Estados Unidos en 1961?", "La Alianza para el Progreso", "La ficha lo nombra."),
        ("{F} ¿Qué permitió la ley de sindicalización campesina?", "Que los trabajadores del campo se organizaran en sindicatos", "La ficha y el vocabulario lo definen."),
        ("=", "{F} ¿Cuántas parcelas de 40 hectáreas salen del fundo de ejemplo?", "1200/40", "Se divide el total entre el tamaño de cada parcela.", " parcelas"),
        ("{F} ¿Cuál es una causa interna de la reforma agraria? A) La concentración de la tierra en pocos fundos B) La Revolución cubana", "A) La concentración de la tierra en pocos fundos", "Es una condición dentro de Chile; la Revolución cubana es del contexto externo."),
        ("{F} ¿Cuál es un cambio que menciona la ficha? A) Se organizaron más sindicatos campesinos B) Desapareció la desigualdad", "A) Se organizaron más sindicatos campesinos", "La ficha afirma que la desigualdad persistía."),
        ("{F} Un fundo de ejemplo de 800 hectáreas se divide en parcelas de 25 hectáreas. ¿Cuántas parcelas completas salen y cuántas hectáreas sobran? A) 32 parcelas y 0 hectáreas B) 30 parcelas y 50 hectáreas", "A) 32 parcelas y 0 hectáreas", "800 ÷ 25 = 32 y la división es exacta."),
        ("{F} El temor a una revolución como la cubana, ¿a qué tipo de explicación pertenece? A) Contexto de Guerra Fría B) Demanda directa del campesinado", "A) Contexto de Guerra Fría", "Se relaciona con el enfrentamiento entre bloques."),
        ("{F} Una familia de pobladores sigue sin vivienda en 1969. ¿Qué es eso? A) Una continuidad B) Un cambio logrado", "A) Una continuidad", "La ficha señala que muchas familias seguían sin vivienda adecuada."),
        ("{F} ¿Por qué no basta decir que la reforma agraria fue solo consecuencia de la Alianza para el Progreso?", "Porque también existían demandas internas y desigualdad en la tierra", "Hubo causas internas del campesinado y de la estructura agraria."),
        ("{F} Un compañero afirma: «Con la ley de 1967 se acabó la pobreza en el campo». ¿Qué respondes? A) La ficha dice que la desigualdad persistía, así que no puede afirmarse B) Tiene razón porque hubo una ley", "A) La ficha dice que la desigualdad persistía, así que no puede afirmarse", "Una ley no prueba el fin del problema."),
        ("{F} ¿Qué mejora esta síntesis: «Las reformas fueron por la Guerra Fría»? A) Agregar demandas internas, cambios y continuidades B) Agregar otra fecha de la Guerra Fría", "A) Agregar demandas internas, cambios y continuidades", "Una buena explicación es multicausal."),
        ("=", "{F} Una organización de pobladores de ejemplo crece de 90 a 150 familias. ¿Cuántas familias se sumaron?", "150-90", "Se resta el número inicial al final.", " familias"),
    ],
    ctx=("Un titular escolar dice: «La reforma agraria solucionó el problema de la tierra». ¿Qué problema tiene? A) Ignora la continuidad de la desigualdad que señala la ficha B) Es muy corto", "A) Ignora la continuidad de la desigualdad que señala la ficha", "No distingue entre cambios logrados y problemas que siguieron."),
    sc=[("En Historia, ¿qué es la Alianza para el Progreso?", "Un programa de 1961 de Estados Unidos para impulsar reformas en América Latina", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es una continuidad?", "Lo que sigue igual a pesar de un cambio", "Es la definición de la clase."),
        ("=", "Un fundo de ejemplo de 900 hectáreas se divide en parcelas de 30. ¿Cuántas parcelas salen?", "900/30", "Se divide el total entre el tamaño de cada parcela.", " parcelas")],
    op=("Haz un esquema con «reformas de los años sesenta» al centro. A un lado escribe dos causas internas y una externa; al otro, dos cambios y una continuidad. Debajo escribe una frase que conecte una causa con un cambio sin decir «la única causa». {F}",
        "Causas internas: desigualdad en la tierra; demandas del campesinado. Externa: Guerra Fría. Cambios: ley de Reforma Agraria de 1967; ley de sindicalización campesina. Continuidad: desigualdad persistente. Frase: las demandas del campesinado y la concentración de la tierra contribuyeron a la reforma agraria.",
        ["separa causas internas y externas", "incluye cambios y una continuidad", "evita causas únicas"], ["esquema", "frase de conexión"], ["explicar todo por una causa", "olvidar una continuidad"],
        "Pide que explique la diferencia entre contexto y causa directa."),
    reinforce="Explica con tus palabras qué cambió y qué siguió igual con la reforma agraria.",
    extend="Piensa en un cambio de reglas en tu colegio y di qué causas lo motivaron y qué siguió igual.",
)

# ================================================================ OA 13, clase 5
F = ("Ficha 5 (datos y fuentes de ejemplo para practicar; no son cifras oficiales). "
     "Tabla de ejemplo de sindicatos campesinos legales: año 1965, 20 sindicatos; año 1967, 60; año 1969, 280. "
     "Fuente de ejemplo 1, relato de un campesino, 1969: «Antes dependíamos del patrón para todo; ahora tenemos sindicato y votamos nuestras decisiones.» "
     "Fuente de ejemplo 2, nota de un propietario, 1969: «Los sindicatos traen conflictos al fundo y bajan la producción.» "
     "Fuente de ejemplo 3, informe de un técnico, 1969: «En los predios reformados, la producción tardó en estabilizarse por falta de crédito y maquinaria.» "
     "Estructura de una interpretación: tesis, evidencia, razonamiento y límite. Un verbo prudente es «sugiere» o «indica»; «prueba» exige evidencia muy sólida.")
build(
    OA, 5, F,
    use="Aprenderé a construir una interpretación documentada sobre el impacto de las reformas de los años sesenta usando una tabla y fuentes con perspectivas distintas.",
    prior=["Sé armar una tesis con evidencia, razonamiento y límite.", "Sé comparar los proyectos de los años sesenta.", "Sé leer una tabla."],
    explain=[
        "Construir una interpretación sobre las reformas de los sesenta significa responder una pregunta con evidencias. Una pregunta posible es: ¿cómo cambió la organización del campesinado? La tabla muestra que los sindicatos campesinos legales aumentaron mucho, de 20 en 1965 a 280 en 1969. Esa es una evidencia cuantitativa, es decir, basada en números.",
        "Las fuentes aportan evidencia cualitativa, basada en testimonios y opiniones. El campesino valora tener sindicato; el propietario teme conflictos; el técnico advierte problemas de crédito y maquinaria. Cada fuente es una perspectiva y ninguna basta sola para evaluar todo el proceso.",
        "Una interpretación equilibrada une las dos clases de evidencia, nombra las perspectivas y dice sus límites. Por ejemplo: los sindicatos crecieron y los campesinos valoraron participar, pero los problemas de producción muestran que el cambio tuvo dificultades. Los datos de ejemplo no permiten afirmar cifras reales.",
    ],
    vocab=[("evidencia cuantitativa", "dato expresado en números, como una tabla"), ("evidencia cualitativa", "testimonio, opinión o descripción que no se mide en números"), ("sindicato", "organización de trabajadores para defender sus intereses"), ("predio", "terreno agrícola de un propietario"), ("estabilizarse", "volver a un nivel regular después de un cambio")],
    worked=[
        ("Leer una tabla", "En una tabla de ejemplo, un registro pasa de 15 a 50 organizaciones. ¿Cuántas más hay?", ["Tomo el valor final y el inicial.", "Resto: 50 − 15 = 35."], "35 organizaciones más"),
        ("Clasificar evidencias", "Una lista de cuántos sindicatos hay cada año, ¿es evidencia cuantitativa o cualitativa?", ["Se expresa en números.", "Puede compararse entre años."], "Cuantitativa"),
    ],
    mistakes=[("Usar solo una fuente para evaluar todo el proceso.", "Se cree que una perspectiva representa a todos los actores.", "Combina tabla y fuentes de distintos actores."),
              ("Escribir que los datos «prueban» el éxito o el fracaso.", "Se exagera lo que dicen unos pocos datos.", "Usa «sugiere» y escribe el límite.")],
    T=[
        ("{F} ¿Cuántos sindicatos legales de ejemplo había en 1967?", "60", "El dato está en la tabla de la ficha."),
        ("{F} En Historia, ¿qué es una evidencia cualitativa?", "Un testimonio, opinión o descripción que no se mide en números", "Así se define en el vocabulario."),
        ("{F} ¿Qué fuente menciona problemas de crédito y maquinaria?", "La fuente 3, el informe del técnico", "El técnico los nombra."),
        ("=", "{F} ¿Cuántos sindicatos más había en 1969 que en 1965?", "280-20", "Se resta el dato de 1965 al de 1969.", " sindicatos"),
        ("{F} La tabla de sindicatos, ¿qué tipo de evidencia es? A) Cuantitativa B) Cualitativa", "A) Cuantitativa", "Está expresada en números."),
        ("{F} ¿Qué perspectiva valora tener sindicato y votar decisiones? A) El campesino de la fuente 1 B) El propietario de la fuente 2", "A) El campesino de la fuente 1", "El campesino destaca esa participación."),
        ("{F} Un historiador quiere saber si crecieron las organizaciones. ¿Qué evidencia es la más adecuada? A) La tabla de sindicatos B) La nota del propietario", "A) La tabla de sindicatos", "La tabla mide el aumento; la nota expresa una opinión."),
        ("=", "{F} Entre 1967 y 1969, ¿cuántos sindicatos más se sumaron que entre 1965 y 1967?", "(280-60)-(60-20)", "Se calcula el aumento de cada tramo y se restan.", " sindicatos"),
        ("{F} Elige la tesis mejor formulada. A) Los sindicatos campesinos crecieron entre 1965 y 1969 y los testimonios sugieren valoración de la participación, aunque hubo problemas de producción B) La reforma fue un éxito total", "A) Los sindicatos campesinos crecieron entre 1965 y 1969 y los testimonios sugieren valoración de la participación, aunque hubo problemas de producción", "Usa datos, testimonios y verbos prudentes."),
        ("{F} ¿Por qué la fuente 3 matiza una interpretación solo positiva?", "Porque muestra dificultades de producción por falta de crédito y maquinaria", "Agrega una perspectiva sobre problemas del proceso."),
        ("{F} Un compañero escribe: «La tabla prueba que todos los campesinos de Chile apoyaron los sindicatos». ¿Qué corriges? A) La tabla cuenta sindicatos, no mide el apoyo de todos B) Nada, la tabla es oficial", "A) La tabla cuenta sindicatos, no mide el apoyo de todos", "El dato mide número de organizaciones, no apoyo."),
        ("{F} ¿Qué límite escribirías para una interpretación basada en esta ficha?", "Que los datos son de ejemplo y de pocas fuentes, por lo que no permiten generalizar a todo el país", "Con pocos datos no se generaliza."),
        ("{F} ¿Qué otra evidencia mejoraría la interpretación? A) Datos de producción y testimonios de más fundos de varios lugares B) Una opinión sin fecha ni autor", "A) Datos de producción y testimonios de más fundos de varios lugares", "Más evidencia diversa reduce el riesgo de generalizar."),
    ],
    ctx=("Una estudiante dice: «La reforma agraria fue un fracaso porque el técnico cuenta problemas». ¿Qué le falta para una interpretación documentada? A) Considerar también la tabla y los demás testimonios, y escribir un límite B) Eliminar la fuente del técnico", "A) Considerar también la tabla y los demás testimonios, y escribir un límite", "Una sola fuente no basta para evaluar el proceso."),
    sc=[("En Historia, ¿qué es una evidencia cuantitativa?", "Un dato expresado en números, como una tabla", "Así se define en el vocabulario."),
        ("¿Qué verbo conviene usar si solo tienes indicios? A) Sugiere B) Prueba", "A) Sugiere", "«Prueba» exige evidencia muy sólida."),
        ("=", "En otra tabla de ejemplo, un registro pasa de 25 a 90 organizaciones. ¿Cuántas más hay?", "90-25", "Se resta el valor inicial al final.", " organizaciones")],
    op=("Responde en cinco líneas: ¿cómo cambió la organización del campesinado en la década de 1960 según la ficha? Escribe tesis, dos evidencias (una de la tabla y una de las fuentes), razonamiento y límite. Usa «sugiere» o «indica». {F}",
        "Tesis: los sindicatos campesinos crecieron y fueron valorados por quienes participaban, aunque hubo dificultades. Evidencia: de 20 a 280 sindicatos de ejemplo y el relato del campesino. Razonamiento: más organizaciones y testimonios de participación indican mayor organización. Límite: datos de ejemplo y pocas fuentes.",
        ["incluye tesis, evidencia, razonamiento y límite", "usa evidencia cuantitativa y cualitativa", "usa verbos prudentes"], ["texto de cinco líneas"], ["omitir el límite", "usar «prueba» sin evidencia suficiente"],
        "Pide que explique por qué importa incluir la fuente del técnico."),
    reinforce="Explica la diferencia entre evidencia cuantitativa y cualitativa con un ejemplo de esta clase.",
    extend="Elige una noticia de hoy y anota un dato en números y un testimonio que la acompañen.",
)

# ================================================================ OA 13, clase 6
F = ("Ficha 6 (debate sobre proyectos excluyentes; posiciones y datos de ejemplo). "
     "En 1970 hubo tres candidatos principales a la presidencia: uno de derecha, uno de la Democracia Cristiana y uno de la Unidad Popular. Esa división se llamó «los tres tercios» porque ninguno tenía mayoría clara. "
     "Hecho: como ningún candidato superó la mitad de los votos, en octubre de 1970 el Congreso Pleno ratificó a Allende, que había obtenido la primera mayoría, después de un acuerdo con la Democracia Cristiana sobre garantías constitucionales. "
     "Proyecto excluyente: plan político que busca aplicarse con su propio programa y deja poco espacio a acuerdos con proyectos distintos. "
     "Posición A, de ejemplo: «Cada proyecto representaba a grandes sectores y buscaba cumplir su programa; con tres bloques era difícil llegar a acuerdos.» "
     "Posición B, de ejemplo: «A pesar de las diferencias, los proyectos usaron los mecanismos democráticos y se pudo seguir conversando.» "
     "Contraargumento: la objeción más fuerte contra la propia tesis. "
     "Dato de ejemplo: en una votación de ejemplo, tres candidatos obtienen 35, 34 y 31 de cada 100 votos.")
build(
    OA, 6, F,
    use="Aprenderé a debatir con evidencia si los proyectos de los años sesenta fueron excluyentes, reconociendo los límites de lo que se sabe y respetando otras posiciones.",
    prior=["Sé comparar los proyectos de la Democracia Cristiana y de la Unidad Popular.", "Sé construir un argumento con contraargumento.", "Sé leer porcentajes sencillos."],
    explain=[
        "Un proyecto excluyente es un plan político que quiere aplicar su programa completo y deja poco espacio a acuerdos con quienes piensan distinto. Los historiadores discuten si los proyectos de la Democracia Cristiana y de la Unidad Popular lo fueron. Unos dicen que cada uno buscó cumplir su propio programa sin pactar con los demás; otros destacan que ambos usaron mecanismos democráticos y siguieron conversando.",
        "En 1970 hubo tres bloques de tamaño parecido, los «tres tercios». Con votos tan repartidos, ningún proyecto tenía mayoría clara. Eso ayuda a entender por qué los acuerdos eran difíciles, pero no prueba que fueran imposibles. Una votación repartida es evidencia, no una sentencia. Además, en octubre de 1970 el Congreso ratificó a Allende tras un acuerdo con la Democracia Cristiana sobre garantías constitucionales, un hecho que usa la posición B.",
        "Para debatir bien se usan tesis, razón, evidencia y contraargumento. También se dicen los límites: con una fuente o un dato no se puede juzgar a todo un período. Y se respeta a quien piensa distinto. Un debate busca entender mejor, no declarar un ganador.",
    ],
    vocab=[("proyecto excluyente", "plan político que busca aplicarse con su programa y deja poco espacio a acuerdos con otros"), ("tres tercios", "división política de 1970 en tres bloques de tamaño parecido"), ("mayoría clara", "apoyo de más de la mitad de los votos"), ("acuerdo político", "pacto entre grupos distintos para tomar decisiones"), ("contraargumento", "objeción más fuerte contra la propia tesis")],
    worked=[
        ("Calcular una mayoría", "En una votación de ejemplo, una candidata obtiene 44 votos de cada 100. ¿Tiene mayoría clara?", ["La mayoría clara es más de 50 de cada 100.", "44 es menor que 50."], "No, no llega a 50 de cada 100"),
        ("Identificar un contraargumento", "Tesis: «Los proyectos eran excluyentes». ¿Cuál es su contraargumento más fuerte?", ["Busco una razón que la contradiga.", "Ambos proyectos usaron los mecanismos democráticos."], "Ambos proyectos usaron los mecanismos democráticos"),
    ],
    mistakes=[("Afirmar que los tres tercios prueban que la democracia fracasaría.", "Se salta de una evidencia a una conclusión que necesita más datos.", "Distingue qué muestra el dato y qué no."),
              ("Tratar al otro bando como el enemigo en un debate escolar.", "Se confunde debatir con ganar.", "Responde a las razones, no a las personas.")],
    T=[
        ("{F} En Historia, ¿qué son «los tres tercios»?", "La división política de 1970 en tres bloques de tamaño parecido", "La ficha lo explica."),
        ("{F} En Historia, ¿qué es un proyecto excluyente?", "Un plan político que busca aplicarse con su programa y deja poco espacio a acuerdos con otros", "Así lo define la ficha."),
        ("{F} ¿Qué hecho de octubre de 1970 apoya mejor la posición B? A) El Congreso ratificó a Allende tras un acuerdo con la Democracia Cristiana sobre garantías constitucionales B) Allende obtuvo más de la mitad de los votos", "A) El Congreso ratificó a Allende tras un acuerdo con la Democracia Cristiana sobre garantías constitucionales", "Muestra un acuerdo entre proyectos distintos; además ningún candidato superó la mitad de los votos."),
        ("=", "{F} En la votación de ejemplo, ¿cuántos votos de cada 100 separan al primero del tercero?", "35-31", "Se resta lo del tercero a lo del primero.", " votos"),
        ("{F} Con 35 de cada 100 votos, ¿el primer candidato tiene mayoría clara? A) No, necesitaría más de 50 de cada 100 B) Sí, porque quedó primero", "A) No, necesitaría más de 50 de cada 100", "Una mayoría clara supera la mitad."),
        ("{F} Un candidato dice: «Solo mi programa puede salvar al país y no negociaré con nadie». ¿Qué rasgo muestra? A) Exclusión de acuerdos B) Disposición a pactar", "A) Exclusión de acuerdos", "No acepta negociar con otros proyectos."),
        ("{F} ¿Qué debe hacer una buena tesis en un debate? A) Apoyarse en evidencia y considerar el contraargumento B) Evitar los datos para no equivocarse", "A) Apoyarse en evidencia y considerar el contraargumento", "Un argumento sólido enfrenta la objeción más fuerte."),
        ("=", "{F} Los tres candidatos de ejemplo obtienen 35, 34 y 31 votos de cada 100. ¿Cuánto suman?", "35+34+31", "Se suman los tres porcentajes.", " votos"),
        ("{F} ¿Qué evidencia apoya mejor la posición A? A) Que ningún bloque tenía mayoría clara y los acuerdos eran difíciles B) Que había tres candidatos", "A) Que ningún bloque tenía mayoría clara y los acuerdos eran difíciles", "Conecta la división con la dificultad de pactar."),
        ("{F} ¿Por qué los tres tercios no prueban que los acuerdos fueran imposibles?", "Porque una votación repartida es evidencia y no impide negociar", "Mide el apoyo, no la voluntad de acuerdo."),
        ("{F} Un estudiante dice: «Los proyectos fueron excluyentes, punto». ¿Qué le falta? A) Evidencia, un contraargumento y un límite B) Más énfasis", "A) Evidencia, un contraargumento y un límite", "Sin esos elementos es solo una opinión."),
        ("{F} ¿Qué postura es la más prudente? A) Hubo rasgos excluyentes y también uso de mecanismos democráticos, según qué evidencia se mire B) Los proyectos fueron solo excluyentes", "A) Hubo rasgos excluyentes y también uso de mecanismos democráticos, según qué evidencia se mire", "Reconoce evidencias en ambos sentidos."),
        ("{F} ¿Qué cambia en un debate respetuoso si alguien presenta una evidencia nueva?", "Se puede ajustar la postura según la evidencia", "Debatir busca comprender mejor, no ganar."),
    ],
    ctx=("En un debate de curso, un grupo dice: «La posición A tiene razón porque es la nuestra». ¿Qué falta? A) Evidencia y respuesta al contraargumento B) Un tono más fuerte", "A) Evidencia y respuesta al contraargumento", "Una posición se sostiene con razones y datos."),
    sc=[("En Historia, ¿qué es una mayoría clara?", "Más de la mitad de los votos", "Así se define en el vocabulario."),
        ("En Historia, ¿qué es un acuerdo político?", "Un pacto entre grupos distintos para tomar decisiones", "Así se define en el vocabulario."),
        ("=", "En una votación de ejemplo, un candidato obtiene 38 votos de cada 100 y otro 27. ¿Cuántos votos de diferencia hay?", "38-27", "Se restan los dos resultados.", " votos")],
    op=("Prepara un debate escrito: elige la posición A o la B de la ficha. Escribe tesis, una razón, una evidencia (el dato de ejemplo o un hecho de la ficha), el contraargumento más fuerte con tu respuesta y un límite. Termina con una línea que diga qué evidencia nueva te haría cambiar de postura. {F}",
        "Tesis: los proyectos mostraron rasgos excluyentes. Razón: cada uno buscó aplicar su programa. Evidencia: tres bloques de 35, 34 y 31 votos de cada 100. Contraargumento: usaron mecanismos democráticos. Respuesta: aun así hubo poca disposición a pactar. Límite: son datos de ejemplo. Cambiaría si hubiera acuerdos documentados.",
        ["incluye tesis, razón, evidencia, contraargumento y límite", "respeta la posición contraria", "dice qué evidencia cambiaría su postura"], ["texto de seis líneas"], ["ignorar el contraargumento", "descalificar a un bando"],
        "Pide que explique la diferencia entre debatir y discutir para ganar."),
    reinforce="Explica a alguien de tu casa qué es un proyecto excluyente y por qué no basta un dato para afirmarlo.",
    extend="Escribe dos razones a favor y una en contra de una decisión de tu curso, con respeto por todas las opiniones.",
)
