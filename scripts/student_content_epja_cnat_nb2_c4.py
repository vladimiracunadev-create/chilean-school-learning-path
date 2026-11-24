"""Ciencias Naturales EPJA Básica N2, módulo 3 (parte 4): OAD-12, investigar el impacto de la actividad humana en los ecosistemas y las acciones de prevención y mitigación. Todo en papel; los casos y los datos son de ejemplo, inventados y rotulados; no se hacen salidas a terreno."""
from __future__ import annotations

from hc_common import make_build


MATERIALS = ("Papel, lápiz y goma. Todos los casos, tablas y datos están escritos en cada ejercicio y son de ejemplo, inventados para este cuaderno; "
             "los lugares nombrados son ficticios. La investigación se hace leyendo y analizando esos datos, sin salidas a terreno. Si algo te cuesta leer, pide apoyo a quien te acompañe.")
build = make_build(MATERIALS)

O = "EPJA-CNAT-NB2-OAD-12"
PRIOR = ["Conozco ecosistemas de mi entorno y sé cómo fluyen la energía y la materia en ellos.", "Sé leer tablas y sumar y restar."]

# ============================================================ clase 1
F = ("Ficha 1 (escenas de ejemplo). A) Una carretera cruza un bosque y lo divide en dos partes. B) Una fábrica de ejemplo descarga agua sucia a un río. "
     "C) Una comunidad planta árboles en un cerro sin vegetación. D) Un grupo de pescadores saca cada año más peces de los que nacen. E) Un grupo de visitantes deja basura en una playa.")
build(
    O, 1, F,
    use="Hoy parto de lo que ya observo en mi entorno para reconocer cómo la actividad humana cambia los ecosistemas.",
    prior=PRIOR,
    explain=[
        "Las personas vivimos dentro de los ecosistemas y los cambiamos con lo que hacemos: construimos caminos y ciudades, cultivamos, pescamos, producimos energía y generamos residuos. Muchos de estos cambios se ven en el barrio, en el campo o en la costa.",
        "Un impacto es el cambio que una actividad produce en un ecosistema. Puede ser negativo, como contaminar un río, o positivo, como plantar árboles en un cerro sin vegetación. Reconocer el impacto es el primer paso para decidir qué cuidar.",
        "Para describir un impacto conviene responder tres preguntas: qué actividad humana ocurre, qué cambio produce en el ecosistema y a qué seres vivos o elementos afecta. Así se empieza una investigación.",
    ],
    vocab=[("actividad humana", "lo que hacemos las personas que cambia el entorno"), ("impacto", "cambio que produce una actividad en un ecosistema"), ("residuo", "lo que se desecha después de usar algo"), ("vegetación", "plantas de un lugar")],
    worked=[
        ("Describir un impacto", F, ["Tomo la escena B.", "Actividad: descargar agua sucia. Cambio: el agua del río se contamina. Afecta a: seres vivos del río."], "B es un impacto negativo: el agua sucia contamina el río y afecta a los seres vivos"),
        ("Un impacto positivo", "La escena C muestra una comunidad que planta árboles en un cerro sin vegetación.", ["La actividad es plantar árboles.", "El cambio es más plantas, sombra y refugio para animales."], "C es un impacto positivo: aumenta la vegetación"),
    ],
    mistakes=[("Pensar que toda actividad humana daña el ecosistema.", "Algunas actividades lo cuidan o lo recuperan, como plantar árboles.", "Pregunta qué cambio produce antes de juzgar."),
              ("Culpar a una persona sin describir la actividad.", "En una investigación se describe lo que ocurre, no se acusa.", "Anota la actividad, el cambio y a quién afecta.")],
    T=[
        ("abc", "{F} ¿Qué actividad humana ocurre en la escena E?", "Dejar basura en una playa", "Plantar árboles", "Pescar", "La escena E describe visitantes que dejan basura."),
        ("ab", "{F} ¿Cuál escena es un impacto positivo?", "La C", "La B", "Plantar árboles aumenta la vegetación del cerro."),
        ("abc", "{F} ¿Cuántas de las cinco escenas muestran un impacto negativo?", "4", "1", "5", "La carretera, el agua sucia, la pesca excesiva y la basura son negativos; solo plantar árboles es positivo."),
        ("abc", "¿Qué es un impacto en un ecosistema?", "Un cambio que produce una actividad", "Un golpe", "Un animal nuevo", "El impacto es el cambio que genera una actividad."),
        ("ab", "{F} ¿Qué cambio produce la escena A?", "Divide el bosque en dos partes", "Hace crecer el bosque", "La carretera separa el hábitat en dos."),
        ("abc", "{F} ¿Qué cambio produce la escena D si sigue así?", "Disminuyen los peces porque se sacan más de los que nacen", "Aumentan los peces", "Los peces se vuelven plantas", "Si se saca más de lo que nace, el número baja."),
        ("abc", "{F} ¿A qué afecta la escena B?", "A los seres vivos del río", "Solo al cielo", "A nadie", "La contaminación del agua afecta a lo que vive en ella."),
        ("=", "Una playa de ejemplo recibe 30 bolsas de basura un fin de semana y se retiran 18. ¿Cuántas quedan?", "30-18", "Se resta lo retirado del total.", " bolsas"),
        ("ab", "Una persona dice «las actividades humanas siempre destruyen». ¿Qué respuesta es mejor?", "Hay impactos negativos y positivos según la actividad", "Tiene razón", "Plantar árboles es un ejemplo de impacto positivo."),
        ("abc", "{F} ¿Qué tres preguntas sirven para describir un impacto en cualquiera de las escenas?", "Qué actividad, qué cambio y a qué afecta", "Quién es culpable, cuánto cuesta y dónde queda", "Cómo se llama, qué color tiene y cuánto pesa", "Esas tres preguntas organizan la descripción."),
        ("abc", "{F} ¿Cuál descripción de la escena E es más precisa?", "Visitantes dejan basura en la playa y esto afecta a las aves y a otros seres vivos", "La playa es fea", "Las personas son malas", "Describe actividad y cambio sin acusar."),
        ("abc", "Una persona observa que desde que se construyó un camino ya no ve ciertas aves. ¿Cuál es una investigación razonable?", "Preguntar qué cambió en el hábitat y buscar datos de cuántas aves había antes", "Culpar al vecino", "Decir que no importa", "Una investigación busca información que apoye la pregunta."),
        ("ab", "¿Por qué reconocer un impacto sirve?", "Para decidir qué cuidar y qué acciones tomar", "Para dar un castigo", "Entenderlo ayuda a buscar acciones adecuadas."),
    ],
    ctx=("abc", "En una junta de vecinos de ejemplo, alguien comenta que el arroyo cercano lleva espuma y mal olor. ¿Qué es lo más adecuado como primer paso?", "Describir lo observado y buscar qué actividad podría estar influyendo", "Culpar de inmediato a una empresa", "Ignorarlo", "Primero se observa y se recogen datos."),
    sc=[("En Ciencias: ¿qué es un impacto ambiental?", "El cambio que una actividad produce en un ecosistema", "Puede ser negativo o positivo, según el cambio que produzca."),
        ("¿Qué preguntas ayudan a describir un impacto?", "Qué actividad, qué cambio y a quién afecta", "Así se ordena la observación antes de investigar."),
        ("¿Toda actividad humana es dañina?", "No, hay impactos positivos, como plantar árboles", "Depende del cambio que produce cada actividad en el ecosistema.")],
    op=("Elige una de estas tres situaciones de ejemplo: (a) un camino nuevo en un bosque, (b) una plantación de árboles en un cerro, (c) basura en una quebrada. Escribe tres líneas: la actividad, el cambio en el ecosistema y a qué seres vivos o elementos afecta.",
        "(c) Actividad: botar basura en la quebrada. Cambio: se contamina el agua. Afecta a: plantas, insectos y aves que dependen de ella.",
        ["nombra la actividad", "describe el cambio", "indica a quién afecta"],
        ["tres líneas escritas"],
        ["acusar a una persona", "no describir el cambio"],
        "Pregunta: «¿Qué cambió y cómo lo sabes?»."),
    reinforce="Observa un lugar cercano y anota una actividad humana y el cambio que produce.",
    extend="Explica por qué un mismo lugar puede tener impactos positivos y negativos a la vez.",
)

# ============================================================ clase 2
F = ("Ficha 2 (casos de ejemplo). 1) Se talan muchos árboles de un bosque para construir casas. 2) Un río recibe aguas con restos de aceite. "
     "3) Se pescan más peces de los que se reponen. 4) Se libera en un lago un pez traído de otro país que se come a los peces del lugar. "
     "5) La quema de combustibles libera gases que aumentan el efecto invernadero.")
build(
    O, 2, F,
    use="Hoy reconozco el vocabulario de los impactos y clasifico casos en tipos.",
    prior=PRIOR + ["Sé describir un impacto con actividad, cambio y a quién afecta."],
    explain=[
        "Los impactos más comunes se pueden agrupar en tipos. La contaminación es la presencia de sustancias que dañan el aire, el agua o el suelo. La pérdida de hábitat ocurre cuando se elimina o divide el lugar donde viven los seres vivos, por ejemplo al talar un bosque.",
        "La sobreexplotación es sacar de la naturaleza más de lo que se repone, como pescar más de lo que nace. Una especie introducida es una que llega de otro lugar y puede competir con las especies locales o comerse a algunas.",
        "El cambio climático es un aumento de la temperatura del planeta, relacionado con el aumento de gases de efecto invernadero que se liberan, entre otras causas, al quemar combustibles. Reconocer el tipo ayuda a elegir la acción adecuada.",
    ],
    vocab=[("contaminación", "presencia de sustancias que dañan el aire, el agua o el suelo"), ("hábitat", "lugar donde vive un ser vivo"), ("sobreexplotación", "sacar más de lo que la naturaleza repone"), ("especie introducida", "especie que llegó de otro lugar y puede dañar a las locales")],
    worked=[
        ("Clasificar un caso", F, ["Miro el caso 2: el río recibe aceite.", "Hay sustancias que dañan el agua."], "El caso 2 es contaminación"),
        ("Otro caso", "Una empresa corta árboles de un bosque donde anidan aves.", ["Se elimina el lugar donde viven las aves.", "Eso es perder su hábitat."], "Es pérdida de hábitat"),
    ],
    mistakes=[("Llamar contaminación a todo daño ambiental.", "La contaminación es solo uno de los tipos: también hay pérdida de hábitat y sobreexplotación.", "Pregunta qué se produce: sustancias, pérdida de lugar o exceso de uso."),
              ("Creer que una especie introducida siempre es dañina.", "Solo algunas se vuelven un problema; hay que evaluarlo en cada caso.", "Mira qué efecto tiene en las especies locales.")],
    T=[
        ("abc", "{F} ¿A qué tipo de impacto corresponde el caso 3?", "Sobreexplotación", "Contaminación", "Pérdida de hábitat", "Se pesca más de lo que se repone."),
        ("ab", "{F} ¿A qué tipo corresponde el caso 1?", "Pérdida de hábitat", "Especie introducida", "Talar el bosque elimina el lugar donde viven los seres vivos."),
        ("abc", "{F} ¿Qué tipo es el caso 4?", "Especie introducida", "Contaminación", "Sobreexplotación", "El pez llegó de otro país y daña a los peces locales."),
        ("abc", "¿Qué es un hábitat?", "El lugar donde vive un ser vivo", "Un tipo de energía", "Una sustancia", "El hábitat es el hogar natural de una especie."),
        ("ab", "{F} Según el caso 5, ¿qué aumenta el efecto invernadero?", "Los gases liberados al quemar combustibles", "El oxígeno que liberan las plantas", "La ficha dice que la quema de combustibles libera gases que aumentan el efecto invernadero."),
        ("=", "{F} Los casos de la ficha son 5. Si los casos 2 y 5 son de contaminación o de gases, ¿cuántos son de otro tipo?", "5-2", "Se resta del total los casos de contaminación y gases.", " casos"),
        ("abc", "Un lago recibe aguas con detergente de ejemplo. ¿Qué tipo de impacto es?", "Contaminación", "Sobreexplotación", "Pérdida de hábitat", "Es una sustancia que daña el agua."),
        ("abc", "Un cerro es convertido en loteo y desaparecen sus arbustos nativos. ¿Qué tipo es?", "Pérdida de hábitat", "Contaminación", "Especie introducida", "Se elimina el lugar donde vivían las plantas y animales."),
        ("ab", "{F} Una persona dice que el caso 4 es sobreexplotación. ¿Qué corrección es correcta?", "Es especie introducida, porque llegó de otro lugar", "Tiene razón", "El pez introducido no se pesca de más; es un animal que llegó de otro lugar."),
        ("abc", "{F} ¿Cuál caso puede tener impacto en el aire en todo el planeta?", "El 5", "El 1", "El 2", "Los gases de efecto invernadero se distribuyen por la atmósfera."),
        ("abc", "{F} Se quiere reducir el caso 3. ¿Qué acción apunta al problema?", "Limitar la cantidad de peces que se pueden sacar", "Sacar más peces", "Echar basura", "Hay que dejar que la población se reponga."),
        ("abc", "Una persona dice que «todo impacto es contaminación». ¿Qué respuesta es más precisa?", "Hay otros tipos: pérdida de hábitat, sobreexplotación y especies introducidas", "Tiene razón", "No hay impactos", "Cada tipo de impacto tiene causas y soluciones distintas."),
        ("ab", "¿Por qué sirve clasificar un impacto?", "Para elegir una acción adecuada al tipo de problema", "Para poner nombres difíciles", "La acción depende de la causa."),
    ],
    ctx=("abc", "En una caleta de ejemplo, los pescadores notan que cada año capturan menos peces de tamaño grande, pese a salir más veces. ¿Qué tipo de impacto podría ser?", "Sobreexplotación", "Contaminación del aire", "Una especie introducida", "Se saca más de lo que se repone."),
    sc=[("En Ciencias: ¿qué es la sobreexplotación?", "Sacar más de lo que la naturaleza repone", "Ocurre con peces, árboles y otros recursos."),
        ("En Ciencias: ¿qué es una especie introducida en un lago o un bosque?", "Una especie que llegó de otro lugar", "Puede competir con las especies locales por el alimento y el espacio."),
        ("¿Qué es la pérdida de hábitat?", "Eliminar o dividir el lugar donde vive un ser vivo", "Por ejemplo, al talar un bosque se pierde el hábitat de sus aves.")],
    op=("Clasifica estos cuatro casos de ejemplo en un tipo de impacto y explica en una línea por qué: (a) derrame de aceite en un río, (b) quema de leña en exceso, (c) tala de un bosque de aves, (d) pesca de más en una bahía.",
        "(a) Contaminación: una sustancia daña el agua. (c) Pérdida de hábitat: las aves se quedan sin lugar.",
        ["clasifica los cuatro casos", "da una razón por caso", "usa el vocabulario de la clase"],
        ["una tabla de cuatro filas"],
        ["llamar contaminación a todo", "no dar razón"],
        "Pregunta: «¿Qué se afecta: el agua, el lugar o la cantidad?»."),
    reinforce="Clasifica tres cosas que veas en la calle como posibles impactos.",
    extend="Explica por qué la sobreexplotación puede terminar con un recurso del que depende una comunidad.",
)

# ============================================================ clase 3
F = ("Ficha 3 (datos de ejemplo, río ficticio). Pregunta de investigación: ¿cambia la cantidad de insectos acuáticos sensibles a la contaminación cerca de una descarga? "
     "Conteo de insectos sensibles en muestras iguales: P1, antes de la descarga: 24. P2, junto a la descarga: 3. P3, 2 km después de la descarga: 11.")
build(
    O, 3, F,
    use="Hoy sigo los pasos de una investigación sencilla con datos de ejemplo para estudiar un impacto.",
    prior=PRIOR + ["Conozco tipos de impacto de la actividad humana."],
    explain=[
        "Investigar un impacto sigue pasos. Paso 1: formula una pregunta que se pueda responder con datos. Paso 2: decide qué datos necesitas y dónde obtenerlos. Paso 3: ordénalos en una tabla. Paso 4: analiza qué muestran y escribe una conclusión que se apoye en ellos.",
        "Algunos seres vivos sirven de indicadores: su presencia o ausencia muestra cómo está el ambiente. Por ejemplo, ciertos insectos acuáticos sensibles son abundantes en agua limpia y disminuyen cuando el agua está contaminada. Contar cuántos hay en lugares distintos entrega evidencia.",
        "Los datos pueden mostrar una relación, pero no siempre prueban la causa. Una conclusión cuidadosa dice: «los datos son coherentes con que la descarga afecta al río», e indica qué más se debería medir para confirmarlo. También hay que escoger fuentes confiables.",
    ],
    vocab=[("pregunta de investigación", "pregunta que se responde con datos"), ("indicador", "ser vivo cuya presencia muestra el estado del ambiente"), ("evidencia", "datos que apoyan una conclusión"), ("fuente confiable", "información de una institución o estudio que explica de dónde vienen sus datos")],
    worked=[
        ("Leer los datos", F, ["P1 tiene 24 insectos sensibles.", "P2 junto a la descarga tiene 3.", "P3 tiene 11."], "Los insectos sensibles bajan mucho junto a la descarga y se recuperan en parte después"),
        ("Conclusión cuidadosa", F, ["Los datos son coherentes con que la descarga daña el agua.", "Pero no prueban la causa si no se mide también el agua."], "Es coherente con un efecto de la descarga, aunque faltan más mediciones para asegurarlo"),
    ],
    mistakes=[("Concluir con total seguridad la causa a partir de un solo conjunto de datos.", "Los datos muestran una relación, pero otras causas podrían influir.", "Usa «es coherente con» y propone medir más."),
              ("Usar datos sin decir de dónde vienen.", "Sin fuente no se puede comprobar si son confiables.", "Anota quién midió, dónde y cuándo.")],
    T=[
        ("abc", "{F} ¿Cuántos insectos sensibles se contaron junto a la descarga (P2)?", "3", "24", "11", "La ficha indica 3 en P2."),
        ("ab", "{F} ¿En qué punto hubo más insectos sensibles?", "En P1, antes de la descarga", "En P2", "P1 tiene 24, el mayor valor."),
        ("=", "{F} ¿Cuántos insectos menos hubo en P2 que en P1?", "24-3", "Se resta el dato de P2 al de P1.", " insectos"),
        ("abc", "{F} ¿Qué pasó entre P2 y P3?", "Los insectos aumentaron de 3 a 11", "Los insectos desaparecieron", "No cambió nada", "De P2 a P3 el número sube."),
        ("=", "{F} ¿Cuántos insectos sensibles se contaron en total en los tres puntos?", "24+3+11", "Se suman los tres conteos.", " insectos"),
        ("ab", "En Ciencias: ¿qué es un indicador del ambiente?", "Un ser vivo cuya presencia muestra el estado del ambiente", "Un cartel", "Su abundancia o ausencia entrega información."),
        ("abc", "{F} ¿Cuál es una buena pregunta de investigación?", "¿Cambia el número de insectos sensibles cerca de la descarga?", "¿Por qué la gente es mala?", "¿Cuál es el río más lindo?", "Se responde con datos medibles, como un conteo de insectos."),
        ("abc", "{F} ¿Qué conclusión se apoya mejor en los datos?", "Hay menos insectos sensibles junto a la descarga, lo que es coherente con un daño del agua", "La descarga mató todos los seres vivos", "No hay relación", "Se limita a lo que los datos muestran."),
        ("ab", "Una persona dice que los datos prueban la causa sin duda. ¿Qué respuesta es mejor?", "Son coherentes con la causa, pero conviene medir más cosas del agua", "Tiene razón", "Una sola medición no prueba una causa."),
        ("=", "{F} Si en P3 se contaran 5 insectos más, ¿cuántos serían?", "11+5", "Se suman los insectos nuevos al conteo de P3.", " insectos"),
        ("abc", "{F} ¿Qué dato más ayudaría a la investigación?", "Medir también la limpieza del agua y repetir el conteo otro día", "Contar piedras", "Nada más", "Más mediciones fortalecen la conclusión y reducen las dudas."),
        ("abc", "Se pregunta qué fuente es más confiable para obtener datos: un informe de una institución que explica cómo midió, un comentario sin autor o un rumor. ¿Cuál se elige?", "El informe que explica cómo midió", "El comentario sin autor", "El rumor", "Una fuente confiable muestra su método."),
        ("ab", "¿Por qué ordenar los datos en una tabla?", "Para compararlos y ver patrones", "Para que se vean bonitos", "La tabla facilita la comparación de los datos entre los puntos."),
    ],
    ctx=("abc", "En un taller comunitario se ve un cartel que dice «la contaminación mató todos los peces del río» sin ningún dato. ¿Qué haces primero como investigador?", "Buscar datos que lo apoyen, por ejemplo conteos o informes con su fuente", "Compartirlo de inmediato", "Ignorar el río", "Una afirmación sin datos no se puede comprobar, así que necesita evidencia."),
    sc=[("En Ciencias: ¿qué es la evidencia?", "Los datos que apoyan una conclusión", "Sin evidencia, una afirmación no se puede comprobar."),
        ("En Ciencias: ¿qué es un indicador del ambiente?", "Un ser vivo que muestra el estado del ambiente", "Por ejemplo, ciertos insectos acuáticos sensibles a la contaminación."),
        ("¿Por qué conviene decir «es coherente con» y no «está probado»?", "Porque los datos pueden tener otras causas", "Es una conclusión honesta porque no afirma más de lo que muestran los datos.")],
    op=("Con estos datos de ejemplo de una quebrada: Punto A, 18 plantas nativas; Punto B (cerca de un basural), 4; Punto C (más lejos), 12. Escribe una pregunta de investigación, una tabla con los datos y una conclusión cuidadosa de dos líneas.",
        "Pregunta: ¿hay menos plantas nativas cerca del basural? Tabla A 18, B 4, C 12. Conclusión: hay menos plantas en B, lo que es coherente con un efecto del basural; faltan más datos.",
        ["la pregunta se responde con datos", "la tabla está ordenada", "la conclusión usa los datos y es cuidadosa"],
        ["una pregunta, una tabla y una conclusión"],
        ["afirmar la causa sin duda", "no usar los números"],
        "Pregunta: «¿Qué dato apoya tu conclusión?»."),
    reinforce="Escribe una pregunta de investigación sobre un lugar cercano que se pueda responder con datos.",
    extend="Explica qué otro dato aumentaría la confianza en la conclusión sobre el río.",
)

# ============================================================ clase 4
F = ("Ficha 4 (medidas de ejemplo). 1) Poner tarros de basura con tapa en una playa. 2) Limpiar la basura de una quebrada. 3) Establecer una veda de pesca durante la época de reproducción. "
     "4) Plantar árboles en un cerro que se quemó. 5) Colocar filtros en una descarga de agua antes de que llegue al río. "
     "Prevención: evitar que el daño ocurra. Mitigación: reducir un daño que ya ocurrió.")
build(
    O, 4, F,
    use="Hoy practico con apoyo cómo distinguir acciones de prevención y de mitigación.",
    prior=PRIOR + ["Sé describir un impacto y su tipo."],
    explain=[
        "Frente a un deterioro del ecosistema hay dos grandes tipos de acción. La prevención son acciones que buscan evitar que el daño ocurra. La mitigación son acciones que buscan reducir un daño que ya ocurrió o disminuir sus efectos.",
        "Por ejemplo, instalar un filtro antes de que el agua llegue al río es prevención; limpiar el río después de un derrame es mitigación. Poner una veda de pesca durante la época de reproducción previene la sobreexplotación; plantar árboles en un cerro quemado ayuda a recuperar lo dañado.",
        "Las dos son importantes y se complementan. En una comunidad, las acciones pueden ser personales, como no botar basura, y colectivas, como organizar una limpieza o pedir que se cumpla la norma vigente a la autoridad correspondiente.",
    ],
    vocab=[("prevención", "evitar que ocurra un daño"), ("mitigación", "reducir un daño que ya ocurrió"), ("veda", "período en que se prohíbe sacar un recurso para que se reponga"), ("norma vigente", "regla actual que se debe cumplir")],
    worked=[
        ("Clasificar una acción", F, ["La acción 1 evita que la basura llegue a la playa.", "Antes de que ocurra el daño."], "La acción 1 es prevención"),
        ("Otra acción", F, ["La acción 4 se hace después del incendio.", "Reduce el daño que ya ocurrió."], "La acción 4 es mitigación"),
    ],
    mistakes=[("Pensar que limpiar siempre es prevención.", "Limpiar actúa cuando el daño ya ocurrió: es mitigación.", "Pregunta si la acción es antes o después del daño."),
              ("Creer que basta con una sola acción.", "La prevención y la mitigación se complementan.", "Propón al menos una de cada tipo.")],
    T=[
        ("abc", "{F} ¿La acción 1 es?", "Prevención", "Mitigación", "Ninguna", "Los tarros evitan que la basura llegue a la playa."),
        ("ab", "{F} ¿La acción 2 es?", "Mitigación", "Prevención", "Limpiar actúa después de que hay basura."),
        ("abc", "{F} ¿La acción 3, una veda de pesca, es?", "Prevención de la sobreexplotación", "Mitigación de un derrame", "Contaminación", "Permite que los peces se reproduzcan y no se agoten."),
        ("abc", "{F} ¿La acción 4 es?", "Mitigación", "Prevención", "Sobreexplotación", "Se hace después de un incendio."),
        ("ab", "{F} ¿La acción 5 es?", "Prevención", "Mitigación", "Los filtros evitan que la contaminación llegue al río."),
        ("=", "{F} Si 3 de las 5 acciones de la ficha son de prevención, ¿cuántas son de mitigación?", "5-3", "Se resta del total las acciones de prevención.", " acciones"),
        ("abc", "Una persona recoge latas de una quebrada. ¿Qué tipo de acción es?", "Mitigación", "Prevención", "Sobreexplotación", "El daño ya ocurrió y se reduce limpiando."),
        ("abc", "Un grupo coloca carteles que piden no botar basura en un parque. ¿Qué tipo de acción es?", "Prevención", "Mitigación", "Contaminación", "La prevención busca evitar que el daño ocurra."),
        ("ab", "{F} Una persona dice que la veda es mitigación porque «se hace después». ¿Qué corrección es correcta?", "Es prevención: se hace antes de que el recurso se agote", "Tiene razón", "La veda evita que se agote el recurso."),
        ("abc", "{F} Se quiere cuidar un río. ¿Cuál combinación es más completa?", "Filtros en la descarga y limpieza del río cuando ocurre un derrame", "Solo limpiar una vez", "No hacer nada", "Combina una acción de prevención con una de mitigación."),
        ("=", "En una limpieza de ejemplo participan 14 vecinos y cada uno junta 3 bolsas. ¿Cuántas bolsas se juntan?", "14*3", "Se multiplica el número de vecinos por las bolsas de cada uno.", " bolsas"),
        ("abc", "¿Qué ocurre si solo se hace mitigación y no prevención?", "El daño puede repetirse y hay que limpiar siempre", "Se evita todo daño", "El ecosistema mejora solo", "Sin prevención el daño vuelve a ocurrir y hay que limpiar siempre."),
        ("ab", "Para pedir que se cumpla una norma ambiental, ¿qué es adecuado?", "Acudir a la autoridad o institución correspondiente con datos", "Quejarse sin datos en una red social", "Una solicitud con datos suele ser más efectiva."),
    ],
    ctx=("abc", "En una población se acumulan escombros en una quebrada. Una vecina propone limpiarla este sábado y otra propone poner un letrero y avisar a la municipalidad para que se controle. ¿Cómo se clasifican?", "Limpiar es mitigación y el letrero con aviso es prevención", "Las dos son prevención", "Las dos son mitigación", "Una repara lo ocurrido y la otra evita que vuelva a pasar."),
    sc=[("En Ciencias: ¿qué es la prevención?", "Acciones para evitar que ocurra un daño", "La prevención se hace antes de que ocurra el daño."),
        ("¿Qué es la mitigación?", "Acciones para reducir un daño que ya ocurrió", "Por ejemplo, limpiar una quebrada o reforestar un cerro quemado."),
        ("¿Por qué conviene combinar ambas?", "Porque se complementan: evitan y reducen el daño", "Una sola de ellas no resuelve todo el problema.")],
    op=("Para este caso de ejemplo, un humedal con basura y con aguas de desagüe que llegan sin tratar, propone dos acciones de prevención y dos de mitigación. Explica en una línea por qué cada una pertenece a su tipo.",
        "Prevención: tarros de basura con tapa; avisar a la autoridad para tratar el desagüe. Mitigación: limpiar la orilla; plantar juncos nativos.",
        ["propone dos de cada tipo", "explica el tipo de cada acción", "las acciones son realistas y seguras"],
        ["cuatro frases escritas"],
        ["confundir prevención con mitigación", "proponer algo peligroso o ilegal"],
        "Pregunta: «¿Esto evita el daño o repara uno que ya ocurrió?»."),
    reinforce="Piensa en una acción de prevención y una de mitigación para un problema de tu barrio.",
    extend="Explica por qué la prevención suele ser mejor que la mitigación a largo plazo.",
)

# ============================================================ clase 5
F = ("Ficha 5 (caso ficticio: Laguna Los Cisnes). Los vecinos observan: A) basura en la orilla, B) poca vegetación en la ribera, C) un desagüe que llega a la laguna sin tratar, "
     "D) menos aves que antes. La junta de vecinos evalúa tres acciones de ejemplo según si previenen o reducen daño, si participa la comunidad y si se pueden hacer pronto: "
     "X) jornada de limpieza, Y) plantar plantas nativas, Z) solicitar a la autoridad revisar y tratar el desagüe.")
build(
    O, 5, F,
    use="Hoy aplico lo aprendido a un caso de comunidad: investigo, priorizo y propongo acciones.",
    prior=PRIOR + ["Distingo prevención y mitigación y sé usar datos."],
    explain=[
        "Para aplicar la investigación a una situación real de una comunidad, sigue este camino: describe lo observado, identifica el tipo de impacto, busca datos que lo apoyen, propone acciones de prevención y mitigación y decide cuáles hacer primero.",
        "Para decidir, conviene usar criterios claros. Por ejemplo: si la acción evita el daño o lo reduce, si puede participar la comunidad y si se puede hacer pronto. Las acciones que dependen de una institución, como revisar un desagüe, se piden por escrito y con datos, según la norma vigente.",
        "Cuidar el ambiente también incluye cuidarse: las jornadas de limpieza deben hacerse con guantes y con apoyo de personas o instituciones informadas, y sin tocar sustancias desconocidas. Ante dudas de seguridad, se consulta a la institución que corresponda.",
    ],
    vocab=[("criterio", "regla para comparar y decidir"), ("priorizar", "decidir qué se hace primero"), ("ribera", "borde de un río o laguna"), ("comunidad", "grupo de personas que comparten un lugar")],
    worked=[
        ("Identificar tipos", F, ["A es basura: contaminación.", "B es poca vegetación: pérdida de hábitat en la ribera.", "C es contaminación del agua."], "A y C son contaminación; B es pérdida de hábitat"),
        ("Aplicar criterios", F, ["La acción Y (plantar nativas) la puede hacer la comunidad y recupera la ribera.", "Es una mitigación."], "Y es una mitigación que la comunidad puede hacer"),
    ],
    mistakes=[("Elegir las acciones sin explicar por qué.", "Sin criterios no se puede comparar ni justificar la decisión.", "Usa al menos dos criterios y escríbelos."),
              ("Proponer acciones que ponen en riesgo a las personas, como tocar sustancias desconocidas.", "El cuidado del ambiente no debe dañar a quienes participan.", "Incluye medidas de seguridad y consulta a la institución.")],
    T=[
        ("abc", "{F} ¿Qué observación indica contaminación del agua?", "La C, el desagüe sin tratar", "La B", "La D", "El desagüe sin tratar contamina el agua."),
        ("ab", "{F} ¿Qué tipo de acción es X, la jornada de limpieza?", "Mitigación", "Prevención", "Limpia un daño que ya ocurrió."),
        ("abc", "{F} ¿Qué acción previene que siga llegando agua sin tratar?", "Z", "X", "Y", "Revisar y tratar el desagüe evita que el daño siga."),
        ("=", "{F} Los vecinos miden 3 criterios por acción. Si evalúan 3 acciones, ¿cuántas evaluaciones hacen en total?", "3*3", "Se multiplica el número de acciones por los criterios.", " evaluaciones"),
        ("abc", "{F} ¿Qué acción permite la participación de la comunidad y recupera la ribera?", "Y", "Z", "Ninguna", "Plantar nativas puede hacerlo la comunidad."),
        ("ab", "{F} ¿Cuál observación sugiere pérdida de hábitat?", "B, poca vegetación en la ribera", "A, basura en la orilla", "Sin vegetación no hay refugio ni alimento."),
        ("abc", "{F} ¿Cuál es la mejor secuencia?", "Observar, buscar datos, proponer acciones y decidir con criterios", "Proponer, culpar y olvidar", "Decidir y después observar", "Sigue un camino ordenado, desde observar hasta decidir con criterios."),
        ("=", "Una jornada de ejemplo reúne 20 personas y cada una limpia 5 metros de orilla. ¿Cuántos metros se limpian?", "20*5", "Se multiplican personas por metros por persona.", " metros"),
        ("abc", "¿Qué medida de seguridad es razonable en una jornada de limpieza?", "Usar guantes y no tocar sustancias desconocidas", "Tocar todo con las manos", "Mezclar líquidos", "Cuidar la propia seguridad es parte del cuidado ambiental."),
        ("ab", "Una comunidad quiere pedir revisar un desagüe. ¿Qué conviene hacer?", "Presentar una solicitud con datos a la institución correspondiente", "Tapar el desagüe sin avisar", "Los datos ayudan a que la solicitud sea atendida."),
        ("abc", "{F} Las aves bajaron. ¿Qué explicación es más razonable?", "Pudieron influir la basura, el desagüe y la falta de vegetación", "Las aves no existen", "Fue por el color de la laguna", "Varios factores afectan al hábitat de las aves al mismo tiempo."),
        ("abc", "{F} Un vecino dice que solo la limpieza basta. ¿Qué respuesta es mejor?", "Hay que sumar prevención, como tratar el desagüe", "Tiene razón", "No hay que hacer nada", "Sin prevención, como tratar el desagüe, el daño volverá a ocurrir."),
        ("ab", "¿Por qué usar criterios para decidir?", "Para comparar acciones y justificar la decisión", "Para tardar más", "Los criterios hacen la decisión comprensible para todos."),
    ],
    ctx=("abc", "La junta de vecinos debe elegir qué hacer primero: limpiar, plantar o solicitar revisar el desagüe. Hay poco tiempo y pocos recursos. ¿Qué enfoque es más razonable?", "Comparar las acciones con criterios y combinar al menos una de prevención y una de mitigación", "Elegir lo más fácil sin pensar", "No hacer nada", "Priorizar con criterios ayuda a decidir."),
    sc=[("¿Qué es priorizar?", "Decidir qué se hace primero", "Se usan criterios claros para comparar las acciones."),
        ("¿Qué acciones combinar en un caso como la laguna?", "Prevención y mitigación", "Así se evita y se repara el daño."),
        ("¿Qué cuidado de seguridad conviene en una limpieza?", "Usar guantes y no tocar sustancias desconocidas", "Cuidar la ribera incluye cuidar a las personas.")],
    op=("Con el caso de la Laguna Los Cisnes, escribe un plan en cuatro líneas: qué observas, qué tipos de impacto hay, qué dos acciones propones (una de prevención y otra de mitigación) y qué criterio usaste para elegirlas.",
        "Observo basura y un desagüe. Hay contaminación y falta de vegetación. Prevención: pedir tratar el desagüe. Mitigación: plantar nativas. Criterio: pueden hacerse con la comunidad.",
        ["identifica los tipos de impacto", "propone una acción de cada tipo", "explica el criterio"],
        ["un plan de cuatro líneas"],
        ["proponer acciones sin criterio", "proponer algo inseguro"],
        "Pregunta: «¿Por qué esta acción antes que otra?»."),
    reinforce="Elige un problema de tu barrio y escribe una acción de prevención y una de mitigación.",
    extend="Explica qué información pedirías a una institución para decidir mejor las acciones sobre la laguna.",
)

# ============================================================ clase 6
F = ("Ficha 6 (informe de ejemplo, datos inventados). Cuenca ficticia El Roble. Superficie cubierta de bosque (hectáreas): año 1, 500; año 5, 420; año 10, 350. "
     "Observación: en el mismo período aumentaron las casas y los caminos. Acción realizada desde el año 6: plantación de árboles nativos en 40 hectáreas.")
build(
    O, 6, F,
    use="Hoy reviso lo logrado: evalúo conclusiones sobre un impacto, comunico un informe y decido qué mejorar.",
    prior=PRIOR + ["Sé investigar un impacto y proponer acciones."],
    explain=[
        "Revisar una investigación incluye evaluar si las conclusiones se apoyan en los datos y comunicar los resultados con honestidad. Una conclusión sólida usa números, dice qué pasó y qué no se puede asegurar. Una exagerada afirma más de lo que muestran los datos.",
        "Un informe breve tiene cuatro partes: la pregunta, los datos (por ejemplo en una tabla), la conclusión y una propuesta de acción con su limitación. Si se detecta un error, como una medición mal hecha, se corrige y se dice con claridad.",
        "En el ejemplo, el bosque pasó de 500 a 350 hectáreas en diez años. Puedes calcular el cambio, compararlo con la acción de plantación y proponer qué hacer a continuación, sin asegurar más de lo que dicen los datos.",
    ],
    vocab=[("informe", "texto breve que comunica una investigación"), ("conclusión sólida", "la que se apoya en los datos"), ("conclusión exagerada", "la que afirma más de lo que muestran los datos"), ("limitación", "aquello que los datos no permiten asegurar")],
    worked=[
        ("Calcular el cambio", F, ["Año 1: 500. Año 10: 350.", "Se resta 500 menos 350."], "El bosque disminuyó 150 hectáreas"),
        ("Evaluar una conclusión", "Una persona afirma: «El bosque desapareció por completo».", ["Los datos muestran 350 hectáreas en el año 10.", "La afirmación dice más que los datos."], "Es una conclusión exagerada: el bosque disminuyó, pero no desapareció"),
    ],
    mistakes=[("Atribuir toda la disminución a una sola causa sin evidencia.", "Los datos muestran un cambio, pero pueden influir varias causas.", "Di «es coherente con» y propone medir más."),
              ("Esconder un error de medición para que el informe se vea mejor.", "La honestidad es parte de una investigación científica.", "Corrige y comunica el error con claridad.")],
    T=[
        ("abc", "{F} ¿Cuántas hectáreas de bosque había en el año 5?", "420", "500", "350", "La ficha indica 420 en el año 5."),
        ("ab", "{F} ¿El bosque aumentó o disminuyó entre el año 1 y el 10?", "Disminuyó", "Aumentó", "Pasó de 500 a 350 hectáreas."),
        ("=", "{F} ¿Cuántas hectáreas se perdieron entre el año 1 y el año 5?", "500-420", "Se resta la superficie del año 5 a la del año 1.", " hectáreas"),
        ("=", "{F} ¿Cuántas hectáreas se perdieron entre el año 5 y el año 10?", "420-350", "Se resta la superficie del año 10 a la del año 5.", " hectáreas"),
        ("abc", "{F} ¿Cuál conclusión se apoya mejor en los datos?", "El bosque disminuyó 150 hectáreas en diez años", "El bosque desapareció", "El bosque aumentó", "Es lo que muestran los números."),
        ("ab", "{F} ¿Qué conclusión es exagerada?", "Las casas y los caminos son la única causa, seguro", "El bosque disminuyó mientras aumentaron las casas y los caminos", "Los datos muestran coincidencia, no prueban una sola causa."),
        ("=", "{F} Si las 40 hectáreas plantadas se suman a las 350 del año 10, ¿cuántas serían?", "350+40", "Se suman las hectáreas nuevas a la superficie del año 10.", " hectáreas"),
        ("abc", "{F} ¿Qué parte de la pérdida compensarían las 40 hectáreas plantadas, comparando con 150 perdidas?", "Menos de la mitad", "Toda", "Más del doble", "40 es menos de la mitad de 150."),
        ("abc", "{F} ¿Qué limitación tiene el informe?", "Solo tiene tres mediciones y no mide otras causas", "Tiene demasiados datos", "No tiene números", "Se debe aclarar lo que no se puede asegurar."),
        ("ab", "Un grupo descubre que contó mal el año 5. ¿Qué es lo correcto?", "Corregir el dato y decirlo con claridad", "Esconderlo", "Corregir y comunicar fortalece la confianza."),
        ("abc", "¿Cuál es la mejor propuesta de acción según los datos?", "Seguir plantando nativas y pedir proteger el bosque restante, midiendo cada año", "No hacer nada", "Talar más", "Combina mitigación, prevención y seguimiento de los datos cada año."),
        ("abc", "{F} Un informe sólido para la comunidad debe incluir:", "Pregunta, datos, conclusión y propuesta con su limitación", "Solo una opinión", "Solo dibujos", "Esas partes hacen que el informe sea comprensible y verificable."),
        ("ab", "¿Por qué comunicar con honestidad es importante?", "Porque otros usarán el informe para decidir", "Porque así parece más seguro", "Las decisiones de la comunidad dependen de datos fiables."),
    ],
    ctx=("abc", "En una reunión vecinal de ejemplo se presenta un informe donde «el bosque perdió 150 hectáreas desde el año 1 al año 10». Una persona pregunta cómo se sabe. ¿Qué respondes?", "Se comparan las superficies del año 1 y del año 10 de la tabla y se resta", "Porque alguien lo dijo", "Porque se ve feo", "La conclusión se apoya en los datos de la tabla."),
    sc=[("¿Qué distingue una conclusión sólida de una exagerada?", "La sólida se apoya en los datos y la exagerada afirma de más", "Hay que usar lo que muestran los números."),
        ("En Ciencias: ¿qué es una limitación?", "Lo que los datos no permiten asegurar", "Por ejemplo, la causa única de un cambio."),
        ("¿Qué hago si descubro un error en mis datos?", "Lo corrijo y lo comunico", "La honestidad es parte de la investigación.")],
    op=("Con el informe de la cuenca El Roble, escribe un informe de cinco líneas para la comunidad: la pregunta, los datos clave con el cálculo del cambio, una conclusión, una propuesta de acción (prevención y mitigación) y una limitación.",
        "Pregunta: ¿cambió el bosque? Datos: de 500 a 350 hectáreas, 150 menos. Conclusión: disminuyó. Acción: seguir plantando y pedir proteger el bosque. Limitación: no se midieron otras causas.",
        ["calcula bien el cambio", "propone acciones de prevención y mitigación", "indica una limitación"],
        ["un informe de cinco líneas"],
        ["exagerar la conclusión", "olvidar la limitación"],
        "Pregunta: «¿Qué dato apoya tu conclusión y qué no puedes asegurar?»."),
    reinforce="Escribe una conclusión sólida y otra exagerada sobre los mismos datos.",
    extend="Explica por qué un informe con tres mediciones puede orientar acciones, pero no cerrar la discusión.",
)
