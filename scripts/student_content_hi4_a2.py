"""Material del estudiante de 4.º básico, Historia, Geografía y Ciencias Sociales: OA 01 clase 5 (mayas) y OA 02 (civilización azteca)."""
from __future__ import annotations

from student_lessons import arith, ex, register
from student_content_hi4_a import task

OA1 = "HI04 OA 01"
OA2 = "HI04 OA 02"

# ---------------------------------------------------------------- OA 01 clase 5
M5 = ("Ficha maya 5: Entre los años 800 y 900 d.C., muchas ciudades mayas del sur, como Tikal, dejaron de estar habitadas y sus templos quedaron abandonados. "
      "Los historiadores proponen varias causas posibles: sequías, guerras entre ciudades y uso excesivo de la tierra. No están seguros de cuál fue la principal. "
      "Algunas ciudades del norte, en Yucatán, siguieron habitadas. Hoy viven millones de personas mayas en México, Guatemala y otros países; muchas hablan lenguas mayas y mantienen costumbres de sus antepasados.")
register(
    OA1, 5,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a sacar una conclusión sobre los mayas y a sostenerla con evidencia. Sirve para opinar en historia sin inventar.",
    prior=["Sé qué es una fuente y una perspectiva.", "Sé cómo vivían los mayas y dónde."],
    explain=[
        "Argumentar es defender una idea con razones. Un buen argumento tiene tres partes: una afirmación, la evidencia que la apoya y un límite, es decir, lo que todavía no sabemos. Sin evidencia, una afirmación es solo una opinión.",
        "Una pregunta frecuente es si los mayas desaparecieron. La evidencia dice que, entre los años 800 y 900 d.C., muchas ciudades del sur quedaron abandonadas. Pero otras ciudades del norte siguieron habitadas y hoy viven millones de personas mayas. Entonces, las ciudades del sur se despoblaron, pero el pueblo maya continúa.",
        "También hay un límite. Los historiadores proponen causas posibles del abandono, como sequías, guerras y uso excesivo de la tierra, pero no saben cuál fue la principal. Por eso decimos «posibles causas» y no «la causa». Un buen argumento reconoce lo que no se sabe.",
    ],
    vocab=[("argumento", "idea defendida con razones y evidencia"), ("evidencia", "dato o fuente que apoya una idea"), ("conclusión", "idea final a la que se llega después de analizar"), ("abandonar", "dejar un lugar sin habitantes"), ("causa", "razón por la que ocurre algo")],
    worked=[
        {"title": "Armar un argumento", "problem": f"{M5} Afirmación: «El pueblo maya no desapareció». ¿Qué evidencia la apoya?", "steps": ["Busco un dato sobre el presente en la ficha.", "Dice que hoy viven millones de personas mayas que hablan lenguas mayas."], "answer": "Hoy viven millones de personas mayas que mantienen su lengua y costumbres"},
        {"title": "Reconocer un límite", "problem": f"{M5} ¿Sabemos con seguridad cuál fue la causa principal del abandono de las ciudades del sur?", "steps": ["Busco lo que dice la ficha sobre las causas.", "Propone tres causas posibles pero dice que no hay seguridad."], "answer": "No, solo hay causas posibles"},
    ],
    mistakes=[
        {"wrong": "Decir «los mayas desaparecieron» solo porque algunas ciudades quedaron vacías.", "why": "Se confunde el abandono de ciudades con la desaparición de un pueblo.", "fix": "Recuerda que hay ciudades del norte habitadas y millones de personas mayas hoy."},
        {"wrong": "Afirmar que la sequía fue la causa segura del abandono.", "why": "Se toma una posibilidad como certeza.", "fix": "Usa «posible causa» cuando los historiadores no están seguros."},
    ],
    tiers={
        "recovery": [
            ex(f"{M5} ¿Qué pasó entre 800 y 900 d.C. con muchas ciudades mayas del sur?", "dejaron de estar habitadas", "La ficha dice que quedaron abandonadas."),
            ex(f"{M5} ¿Quedaron abandonadas todas las ciudades mayas del norte?", "No", "La ficha dice que algunas del norte siguieron habitadas."),
            ex(f"{M5} ¿Viven mayas hoy?", "Sí, millones de personas", "La ficha dice que hoy viven millones de personas mayas."),
        ],
        "understand": [
            ex(f"{M5} ¿Cuántas causas posibles nombra la ficha para el abandono?", "tres: sequías, guerras y uso excesivo de la tierra", "Son las tres que la ficha enumera."),
            ex(f"{M5} ¿Los historiadores están seguros de cuál fue la causa principal?", "No", "La ficha dice que no están seguros."),
            ex("¿Qué es la evidencia en un argumento?", "un dato o fuente que apoya la idea", "Sin evidencia la afirmación es solo una opinión."),
        ],
        "apply": [
            ex(f"{M5} Elige la mejor conclusión. A) Los mayas desaparecieron por completo. B) Muchas ciudades del sur se abandonaron, pero el pueblo maya continúa.", "B", "B se apoya en los datos de la ficha."),
            ex(f"{M5} Afirmación: «Algunas ciudades mayas siguieron habitadas». ¿Qué dato sirve de evidencia?", "Algunas ciudades del norte, en Yucatán, siguieron habitadas", "Ese dato respalda directamente la afirmación."),
            ex(f"{M5} Completa con «posible» o «segura»: la sequía es una causa ___ del abandono.", "posible", "Los historiadores no están seguros de cuál fue la causa."),
        ],
        "reason": [
            ex(f"{M5} Sofía dice: «La causa fue la sequía». ¿Está bien dicho? Explica.", "No, es solo una causa posible y la ficha no permite afirmarlo", "La ficha dice que no están seguros de la principal."),
            ex(f"{M5} Rodrigo concluye: «Los mayas desaparecieron porque Tikal quedó vacía». Da un dato de la ficha que lo contradiga.", "Hoy viven millones de personas mayas", "Un dato del presente contradice la desaparición total."),
        ],
        "challenge": [
            ex(f"{M5} Marca cada parte del argumento: afirmación, evidencia o límite. a) «Hoy viven millones de personas mayas». b) «El pueblo maya continúa». c) «No se sabe cuál fue la causa principal del abandono».", "a: evidencia; b: afirmación; c: límite", "a respalda la idea, b la plantea y c dice lo que no se sabe."),
            ex(f"{M5} Dos estudiantes discuten. Luz: «Sabemos que las guerras causaron el abandono». Ema: «Las guerras son una causa posible». ¿Quién argumenta mejor y por qué?", "Ema, porque no afirma más de lo que se sabe", "La ficha solo habla de causas posibles."),
        ],
    },
    context=[ex("Una guía de turismo dice: «Los mayas son un misterio, ya no queda ninguno». ¿Qué dato de la ficha permite corregirla?", "Hoy viven millones de personas mayas", "Ese dato muestra que el pueblo maya continúa.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes de un buen argumento?", "afirmación, evidencia y límite", "Así se arma una idea bien sostenida."),
        ex(f"{M5} ¿Los mayas desaparecieron por completo?", "No, el pueblo maya continúa hoy", "Muchas ciudades se abandonaron, pero hay millones de mayas hoy."),
        ex("¿Por qué conviene decir «posible causa» y no «la causa»?", "porque los historiadores no están seguros", "Un buen argumento reconoce lo que no se sabe."),
    ],
    open_task=task(
        f"Escribe un argumento de tres frases para responder: «¿Los mayas desaparecieron?». Usa este molde: 1) «Pienso que…» (afirmación); 2) «Lo muestra que…» (evidencia de la ficha); 3) «Todavía no se sabe…» (límite). {M5}",
        "Pienso que el pueblo maya no desapareció. Lo muestra que hoy viven millones de personas mayas que hablan lenguas mayas. Todavía no se sabe cuál fue la causa principal del abandono de las ciudades del sur.",
        ["afirmación clara", "evidencia tomada de la ficha", "un límite honesto"], ["tres frases escritas"], ["afirmar que desaparecieron", "dar una causa como segura"],
        "Pide que lea su argumento en voz alta y señale cuál es la evidencia y cuál el límite."),
    reinforce="Explica a alguien de tu casa, con una afirmación y una evidencia, por qué los mayas no desaparecieron.",
    extend="Escribe una pregunta sobre los mayas que la ficha no responde y cómo podrías averiguarla.",
)

# ================================================================ OA 02 · AZTECAS
# ---------------------------------------------------------------- clase 1
A1 = ("Ficha azteca 1: Los aztecas, también llamados mexicas, vivieron en el valle de México, en el centro de México actual. "
      "Hacia el año 1325 fundaron su capital, Tenochtitlán, en una isla del lago de Texcoco. La ciudad se unía a la orilla por calzadas, que son caminos elevados sobre el agua. "
      "Tenochtitlán se alió con Texcoco y Tlacopan y juntas dominaron a muchos pueblos vecinos, que debían pagar tributo, es decir, entregar productos. "
      "Así se formó un imperio, gobernado por un emperador que vivía en Tenochtitlán. En su mayor extensión, el imperio llegaba desde la costa del golfo de México hasta la costa del océano Pacífico. En el año 1521 los españoles tomaron la ciudad y el imperio terminó.")
register(
    OA2, 1,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio. Un mapa de México ayuda, pero no es necesario.",
    use="Aprenderé dónde y cuándo vivieron los aztecas y cómo se organizó su imperio. Sirve para ubicar su historia y entender por qué Tenochtitlán fue tan importante.",
    prior=["Sé qué es una civilización.", "Sé que los mayas vivieron en Mesoamérica."],
    explain=[
        "Los aztecas, o mexicas, vivieron en el valle de México, en el centro de México actual. Hacia el año 1325 fundaron su capital, Tenochtitlán, en una isla del lago de Texcoco. Para llegar a la orilla se usaban calzadas, caminos elevados que cruzaban el agua.",
        "Con el tiempo, Tenochtitlán se alió con otras dos ciudades, Texcoco y Tlacopan. Juntas dominaron a muchos pueblos vecinos. Esos pueblos debían pagar tributo, que significa entregar productos como maíz, telas o cacao. Así se formó un imperio, es decir, un territorio grande con muchos pueblos bajo un mismo poder. En su mayor extensión, llegaba desde la costa del golfo de México hasta la costa del océano Pacífico.",
        "El imperio azteca tenía un emperador, la máxima autoridad, que vivía en Tenochtitlán. A diferencia de las ciudades-estado mayas, el poder se concentraba en una capital. El imperio terminó en 1521, cuando los españoles tomaron la ciudad. Pasaron cerca de 196 años entre la fundación y la caída.",
    ],
    vocab=[("imperio", "territorio grande con muchos pueblos gobernados por un mismo poder"), ("tributo", "productos que los pueblos dominados entregaban al imperio"), ("calzada", "camino elevado que cruzaba el lago"), ("capital", "ciudad principal donde está el gobierno"), ("emperador", "gobernante máximo de un imperio")],
    worked=[
        {"title": "Ubicar la capital", "problem": f"{A1} ¿Dónde fundaron los aztecas su capital?", "steps": ["Busco el nombre de la capital: Tenochtitlán.", "Leo que estaba en una isla del lago de Texcoco."], "answer": "En una isla del lago de Texcoco, en el valle de México"},
        {"title": "Calcular un tiempo", "problem": f"{A1} ¿Cuántos años pasaron entre la fundación (hacia 1325) y la toma de la ciudad (1521)?", "steps": ["Tomo los dos años: 1325 y 1521.", "Resto: 1521 − 1325 = 196."], "answer": "Cerca de 196 años"},
    ],
    mistakes=[
        {"wrong": "Decir que los aztecas fundaron Tenochtitlán en la selva.", "why": "Se confunde con las ciudades mayas.", "fix": "Recuerda: estaba en una isla de un lago, en el valle de México."},
        {"wrong": "Decir que el imperio azteca existió en la misma época que el período clásico maya.", "why": "Se mezclan fechas.", "fix": "Los aztecas fundaron su capital hacia 1325, mucho después del año 900."},
    ],
    tiers={
        "recovery": [
            ex(f"{A1} ¿Cómo se llamaba la capital de los aztecas?", "Tenochtitlán", "La ficha la nombra."),
            ex(f"{A1} ¿En qué lago estaba la isla de Tenochtitlán?", "en el lago de Texcoco", "La ficha dice que estaba en una isla de ese lago."),
            ex(f"{A1} ¿Cómo se llama lo que los pueblos dominados entregaban al imperio?", "tributo", "La ficha define el tributo así."),
        ],
        "understand": [
            ex(f"{A1} ¿Qué ciudades se aliaron con Tenochtitlán?", "Texcoco y Tlacopan", "La ficha nombra esas dos ciudades."),
            ex(f"{A1} ¿Para qué servían las calzadas de Tenochtitlán?", "para unir la isla con la orilla", "Eran caminos elevados sobre el agua."),
            ex(f"{A1} ¿Quién gobernaba el imperio azteca?", "un emperador que vivía en Tenochtitlán", "La ficha lo indica."),
        ],
        "apply": [
            arith(f"{A1} La ciudad fue fundada hacia 1325 y tomada en 1521. ¿Cuántos años pasaron?", "1521-1325", "Se resta el año final menos el inicial.", " años"),
            ex(f"{A1} Un pueblo vecino entrega maíz y telas al emperador cada año. ¿Cómo se llama ese pago?", "tributo", "Entregar productos al imperio es pagar tributo."),
            ex(f"{A1} ¿Entre qué dos costas se extendía el imperio azteca en su mayor extensión?", "entre la costa del golfo de México y la costa del océano Pacífico", "La ficha da esas dos costas como límites de su mayor extensión."),
        ],
        "reason": [
            ex(f"{A1} Ana dice: «Los aztecas y los mayas del período clásico eran vecinos en la misma época». Corrígela con dos años: el fin del período clásico maya fue hacia 900 d.C. ¿Qué año de la ficha de los aztecas lo contradice?", "1325, la fundación de Tenochtitlán, ocurrió mucho después", "Entre 900 y 1325 hay más de 400 años."),
            ex(f"{A1} Tomás dice: «Los pueblos vecinos entregaban tributo porque querían». ¿Qué dice la ficha sobre ese tributo?", "Que lo debían pagar por haber sido dominados", "La ficha dice que debían pagar tributo."),
        ],
        "challenge": [
            ex(f"{A1} Clasifica cada dato en «dónde», «cuándo» o «cómo se gobernaban»: a) hacia 1325 fundaron Tenochtitlán; b) un emperador en la capital; c) valle de México.", "a: cuándo; b: cómo se gobernaban; c: dónde", "Cada dato responde a una pregunta distinta."),
            ex(f"{A1} Un compañero dice que los aztecas eran ciudades-estado independientes como los mayas. ¿Qué dato de la ficha muestra la diferencia?", "Tenían un imperio con un emperador en Tenochtitlán", "El poder estaba concentrado en una capital."),
        ],
    },
    context=[ex("En un museo hay una maqueta: una isla con muchos edificios, unida a la orilla por tres caminos sobre el agua. ¿Qué ciudad azteca representa y qué nombre tienen esos caminos?", "Tenochtitlán; calzadas", "La capital estaba en una isla y se unía por calzadas.")],
    selfcheck=[
        ex("¿Dónde vivieron los aztecas?", "en el valle de México", "Allí se ubicó su capital."),
        ex("¿Qué es un imperio?", "un territorio grande con muchos pueblos gobernados por un mismo poder", "Así estaba organizado el mundo azteca."),
        ex("¿En qué año tomaron los españoles Tenochtitlán?", "1521", "Esa fecha figura en la ficha."),
    ],
    open_task=task(
        f"Haz un mapa simple de la ciudad: dibuja un lago (una mancha azul), una isla en el centro con la palabra «Tenochtitlán» y tres calzadas que la unan con la orilla. Escribe a la orilla «Texcoco» y «Tlacopan» como ciudades aliadas. Debajo, haz una línea de tiempo con dos puntos: «hacia 1325» y «1521». {A1}",
        "Lago con una isla y tres calzadas, dos ciudades aliadas y una línea con 1325 y 1521.",
        ["isla en el lago", "calzadas hacia la orilla", "dos años en orden"], ["mapa simple", "línea de tiempo"], ["poner la ciudad en tierra firme", "invertir las fechas"],
        "Pregunta cómo entraba la gente a la isla. La respuesta esperada son las calzadas."),
    reinforce="Cuenta en voz alta dónde estaba Tenochtitlán, quién la gobernaba y cuándo terminó el imperio.",
    extend="Escribe dos diferencias entre un imperio como el azteca y las ciudades-estado mayas.",
)

# ---------------------------------------------------------------- clase 2
A2 = ("Fuentes sobre los aztecas: (1) El Templo Mayor, cuyas ruinas fueron descubiertas en el centro de la actual Ciudad de México; dentro había ofrendas. "
      "(2) Un códice pintado hacia 1541 por escribas indígenas, por encargo de una autoridad española, con dibujos de tributos y de la crianza de los niños; llevaba comentarios en español. "
      "(3) La Piedra del Sol, un gran disco de piedra tallado con signos del calendario azteca. "
      "(4) Un relato escrito por un soldado español que participó en la conquista, donde describe la ciudad con asombro.")
register(
    OA2, 2,
    materials="Lápiz y papel. Las fuentes están escritas en cada ejercicio.",
    use="Aprenderé a preguntar quién hizo cada fuente sobre los aztecas, cuándo y para qué. Sirve para saber qué información es más confiable y qué no podemos saber.",
    prior=["Sé que la procedencia es quién hizo la fuente, cuándo y para qué.", "Sé dónde estaba Tenochtitlán."],
    explain=[
        "Conocemos a los aztecas por medio de fuentes muy distintas. Algunas son restos materiales, como las ruinas del Templo Mayor o la Piedra del Sol. Otras son documentos escritos o pintados, como un códice. Para cada fuente preguntamos: ¿quién la hizo, cuándo y para qué?",
        "El códice de la ficha fue pintado hacia 1541 por escribas indígenas, pero por encargo de una autoridad española y con comentarios en español. Eso significa que mezcla una mano indígena con un encargo español. Sirve para conocer tributos y crianza de niños, pero debemos recordar quién lo pidió y para qué.",
        "El relato del soldado español es una fuente escrita por alguien que participó en la conquista. Cuenta lo que vio con asombro, pero lo escribió desde su propia mirada y sus propios intereses. Las ruinas y la Piedra del Sol, en cambio, las hicieron los propios aztecas. Para entenderlos mejor, comparamos varias fuentes.",
    ],
    vocab=[("ruinas", "restos de un edificio muy antiguo"), ("códice", "libro pintado a mano por escribas"), ("conquista", "toma de un territorio por la fuerza"), ("procedencia", "quién hizo la fuente, cuándo y para qué"), ("ofrenda", "objeto o alimento entregado a los dioses")],
    worked=[
        {"title": "Preguntar por la procedencia", "problem": f"{A2} ¿Quién pidió el códice de la fuente 2?", "steps": ["Leo la fuente 2.", "Dice que fue pintado por escribas indígenas por encargo de una autoridad española."], "answer": "Una autoridad española"},
        {"title": "Contrastar", "problem": f"{A2} ¿Qué fuente la hicieron los propios aztecas?", "steps": ["Busco fuentes hechas en el mundo azteca.", "La Piedra del Sol fue tallada por los aztecas."], "answer": "La Piedra del Sol (fuente 3)"},
    ],
    mistakes=[
        {"wrong": "Creer que un solo relato dice toda la verdad sobre los aztecas.", "why": "Se olvida que cada autor tiene su mirada.", "fix": "Compara varias fuentes y pregunta por la procedencia."},
        {"wrong": "Creer que el códice es solo indígena porque lo pintaron escribas indígenas.", "why": "No se lee quién lo encargó.", "fix": "Lee la procedencia completa: pintado por indígenas por encargo español."},
    ],
    tiers={
        "recovery": [
            ex(f"{A2} ¿Qué fuente son ruinas encontradas en la actual Ciudad de México?", "el Templo Mayor", "La fuente 1 es el Templo Mayor."),
            ex(f"{A2} ¿En qué idioma estaban los comentarios del códice?", "en español", "La ficha dice que llevaba comentarios en español."),
            ex(f"{A2} ¿Quién escribió el relato de la fuente 4?", "un soldado español", "La ficha lo dice."),
        ],
        "understand": [
            ex(f"{A2} ¿Qué fuente tiene signos del calendario azteca?", "la Piedra del Sol", "La fuente 3 es un disco con signos del calendario."),
            ex(f"{A2} ¿Qué fuente muestra dibujos de tributos y de la crianza de los niños?", "el códice", "Son los contenidos de la fuente 2."),
            ex(f"{A2} ¿Qué sentimiento muestra el soldado al describir la ciudad?", "asombro", "La ficha dice que la describe con asombro."),
        ],
        "apply": [
            ex(f"{A2} Quieres saber cómo se criaba a los niños aztecas. ¿Qué fuente usas?", "el códice (fuente 2)", "El códice tiene dibujos de la crianza de los niños."),
            ex(f"{A2} Quieres saber qué objetos se dejaban como ofrendas. ¿Qué fuente usas?", "el Templo Mayor (fuente 1)", "Dentro del Templo Mayor se hallaron ofrendas."),
            ex(f"{A2} Une cada fuente con su procedencia: A) Piedra del Sol; B) relato del soldado. 1) tallada por aztecas; 2) escrito por un español de la conquista.", "A con 1; B con 2", "Cada fuente tiene un autor distinto."),
        ],
        "reason": [
            ex(f"{A2} Pedro dice: «El códice es una fuente totalmente indígena». ¿Por qué no es del todo cierto?", "Porque fue encargado por una autoridad española y llevaba comentarios en español", "La procedencia incluye quién lo pidió."),
            ex(f"{A2} Clara dice: «El soldado nos cuenta lo que pensaban los aztecas». ¿Qué problema tiene?", "El soldado cuenta lo que vio él, no lo que pensaban los aztecas", "Describe desde su propia mirada."),
        ],
        "challenge": [
            ex(f"{A2} Para comparar la mirada de los aztecas con la de un extranjero, ¿qué fuente enfrentarías con la fuente 4: la fuente 3 o la fuente 2?", "la fuente 3", "La Piedra del Sol la tallaron los aztecas; el códice tuvo encargo español."),
            ex(f"{A2} Elige la pregunta que estas fuentes no pueden responder. A) ¿Qué ciudad describió el soldado? B) ¿Qué nombre tenía el vecino de un campesino azteca?", "B", "Ninguna fuente de la ficha entrega nombres de vecinos."),
        ],
    },
    context=[ex("Un cartel dice: «Códice pintado hacia 1541 por encargo de una autoridad española». ¿Qué parte del cartel dice quién lo encargó?", "por encargo de una autoridad española", "Esa frase da la procedencia del encargo.")],
    selfcheck=[
        ex("¿Qué es el Templo Mayor para un historiador?", "una fuente: ruinas con ofrendas de la Ciudad de México", "Sus ruinas muestran cómo eran los edificios y ritos."),
        ex("¿Por qué debemos preguntar quién encargó un códice?", "porque quien lo encarga puede influir en lo que se muestra", "El encargo es parte de la procedencia."),
        ex("¿Qué fuente de la ficha escribió un soldado español?", "el relato de la fuente 4", "Es el texto de un testigo de la conquista."),
    ],
    open_task=task(
        f"Haz una tabla con las columnas «fuente», «quién la hizo» y «qué nos dice». Completa dos filas: el códice (fuente 2) y el relato del soldado (fuente 4). Escribe también una cosa que cada una no nos dice. {A2}",
        "Códice: escribas indígenas por encargo español; muestra tributos y niños; no dice qué pensaban los escribas. Relato: soldado español; describe la ciudad con asombro; no dice cómo vivía un campesino.",
        ["dos filas completas", "quién la hizo bien indicado", "un límite por fuente"], ["tabla completa"], ["mezclar quién hizo cada fuente", "decir que una fuente lo explica todo"],
        "Pregunta cuál de las dos fuentes sirve más para saber de los niños y por qué."),
    reinforce="Nombra cuatro fuentes sobre los aztecas y di quién hizo cada una.",
    extend="Escribe qué diría un historiador de dentro de mil años si encontrara una foto de tu escuela.",
)

# ---------------------------------------------------------------- clase 3
A3 = ("Ficha azteca 3: Los aztecas cultivaban maíz, frijol, zapallo, chile y tomate. Como su ciudad estaba en un lago, hicieron chinampas: terrenos pequeños y fértiles rodeados de agua, donde sembraban varias veces al año. "
      "Un acueducto llevaba agua potable a la ciudad. Los campesinos pagaban tributo a los nobles y al emperador. "
      "En la cima de la sociedad estaban el emperador y los nobles; luego los sacerdotes y guerreros; los comerciantes, llamados pochteca, y los artesanos; y los campesinos. También había esclavos. "
      "Los hijos de nobles iban a una escuela llamada calmécac y los demás jóvenes, al telpochcalli. Los hombres cultivaban, hacían la guerra y comerciaban. Las mujeres tejían, cocinaban y criaban; algunas eran parteras o sacerdotisas.")
register(
    OA2, 3,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé cómo cultivaban los aztecas, qué avances tecnológicos usaron y cómo se organizaba su sociedad. Sirve para describir su vida cotidiana con datos.",
    prior=["Sé dónde estaba Tenochtitlán.", "Sé qué es el tributo."],
    explain=[
        "Los aztecas vivían en una isla en medio de un lago, y por eso hicieron chinampas. Una chinampa es un terreno pequeño y fértil rodeado de agua, donde se sembraba maíz, frijol, zapallo, chile y tomate varias veces al año. Fue un gran avance para producir alimentos con poco terreno.",
        "Otros avances fueron las calzadas y un acueducto, un canal elevado que llevaba agua potable a la ciudad. La sociedad estaba ordenada en grupos: el emperador y los nobles; sacerdotes y guerreros; comerciantes (pochteca) y artesanos; y campesinos. También había esclavos. Los campesinos pagaban tributo a los nobles y al emperador.",
        "Los jóvenes aprendían en escuelas: los hijos de los nobles iban al calmécac y los demás jóvenes, al telpochcalli. Los hombres cultivaban, hacían la guerra y comerciaban. Las mujeres tejían, cocinaban y criaban a los hijos, y algunas eran parteras o sacerdotisas. La sociedad azteca no era igual para todas las personas.",
    ],
    vocab=[("chinampa", "terreno pequeño y fértil rodeado de agua, para sembrar"), ("acueducto", "canal elevado que lleva agua"), ("pochteca", "comerciantes aztecas"), ("calmécac", "escuela de los hijos de nobles"), ("partera", "mujer que ayuda en los partos")],
    worked=[
        {"title": "Explicar un avance", "problem": f"{A3} ¿Qué es una chinampa y por qué sirvió?", "steps": ["Busco la definición: terreno pequeño y fértil rodeado de agua.", "Sirvió para sembrar varias veces al año en una ciudad sobre un lago."], "answer": "Un terreno fértil rodeado de agua que permitía producir alimentos varias veces al año"},
        {"title": "Ubicar un grupo", "problem": f"{A3} ¿En qué grupo estaban los pochteca?", "steps": ["Busco la palabra pochteca.", "La ficha dice que eran comerciantes, junto a los artesanos."], "answer": "Entre los comerciantes y artesanos"},
    ],
    mistakes=[
        {"wrong": "Decir que las chinampas eran terrenos secos lejos del agua.", "why": "Se entiende mal «rodeados de agua».", "fix": "Son terrenos pequeños y fértiles rodeados de agua."},
        {"wrong": "Decir que todos los jóvenes aztecas iban a la misma escuela.", "why": "Se olvida la diferencia entre grupos.", "fix": "Los hijos de nobles iban al calmécac; los demás, al telpochcalli."},
    ],
    tiers={
        "recovery": [
            ex(f"{A3} ¿Qué eran las chinampas?", "terrenos pequeños y fértiles rodeados de agua", "La ficha las define así."),
            ex(f"{A3} ¿Qué llevaba agua potable a la ciudad?", "un acueducto", "La ficha lo indica."),
            ex(f"{A3} ¿Cómo se llamaban los comerciantes aztecas?", "pochteca", "La ficha da ese nombre."),
        ],
        "understand": [
            ex(f"{A3} ¿Para qué sirvieron las chinampas en una ciudad sobre un lago?", "para sembrar alimentos varias veces al año", "Resolvían el poco terreno disponible."),
            ex(f"{A3} ¿Qué escuela era para los hijos de los nobles?", "el calmécac", "La ficha lo indica."),
            ex(f"{A3} ¿Qué pagaban los campesinos a los nobles y al emperador?", "tributo", "La ficha dice que pagaban tributo."),
        ],
        "apply": [
            ex(f"{A3} Un joven que no es hijo de noble va a estudiar. ¿A qué escuela iría?", "al telpochcalli", "Los demás jóvenes iban allí."),
            ex(f"{A3} Un menú tiene tomate, maíz y chile. ¿Son cultivos aztecas de la ficha?", "Sí", "Los tres se nombran en la ficha."),
            ex(f"{A3} Une cada persona con su grupo: A) un sacerdote; B) un comerciante pochteca; C) un campesino. 1) comerciantes y artesanos; 2) sacerdotes y guerreros; 3) campesinos.", "A con 2; B con 1; C con 3", "Cada persona se ubica según los grupos de la ficha."),
        ],
        "reason": [
            ex(f"{A3} Luis dice: «Las mujeres aztecas solo cocinaban». ¿Qué datos de la ficha lo contradicen?", "Tejían, criaban a los hijos y algunas eran parteras o sacerdotisas", "La ficha da varios roles."),
            ex(f"{A3} Ana dice: «Los aztecas no podían producir muchos alimentos porque su ciudad estaba en un lago». ¿Qué avance tecnológico responde a su duda?", "Las chinampas", "Permitían sembrar varias veces al año."),
        ],
        "challenge": [
            ex(f"{A3} Clasifica cada dato en «cultivo», «tecnología» o «sociedad»: a) chinampas; b) emperador, nobles y campesinos; c) acueducto.", "a: cultivo; b: sociedad; c: tecnología", "Las chinampas sirven al cultivo, el acueducto es tecnología y los grupos son sociedad."),
            ex(f"{A3} ¿Qué dimensión NO aparece en la ficha: la religión o la educación?", "la religión", "La ficha trata de escuelas, no de religión."),
        ],
    },
    context=[ex("Un museo muestra un dibujo de una familia en una canoa junto a un terreno cuadrado rodeado de agua, con maíz sembrado. ¿Qué es ese terreno?", "una chinampa", "Es un terreno fértil rodeado de agua donde se sembraba.")],
    selfcheck=[
        ex("¿Qué cultivos nombra la ficha para los aztecas?", "maíz, frijol, zapallo, chile y tomate", "Son los cultivos de la ficha."),
        ex("¿Qué avance tecnológico llevaba agua potable a Tenochtitlán?", "el acueducto", "Era un canal elevado."),
        ex("¿Cómo se llamaba la escuela de los hijos de nobles?", "calmécac", "La ficha la nombra así."),
    ],
    open_task=task(
        f"Dibuja una chinampa: un cuadrado de tierra rodeado de agua, con tres plantas distintas (maíz, frijol y tomate) y una canoa. Escribe tres rótulos: «chinampa», «agua» y «cultivo». Luego escribe una frase que diga por qué las chinampas eran útiles. {A3}",
        "Cuadrado de tierra con maíz, frijol y tomate, rodeado de agua y una canoa. Rótulos y una frase: sirvieron para sembrar varias veces al año.",
        ["chinampa rodeada de agua", "tres plantas de la ficha", "una razón de su utilidad"], ["dibujo con rótulos", "frase"], ["dibujar la chinampa sin agua", "poner plantas que la ficha no nombra"],
        "Pregunta cómo llegaba el campesino a su chinampa. Una respuesta posible es en canoa; no está en la ficha, así que acepta lo razonable."),
    reinforce="Explica en voz alta qué es una chinampa y quiénes pagaban tributo.",
    extend="Compara con la milpa maya: escribe una semejanza y una diferencia con las chinampas.",
)

# ---------------------------------------------------------------- clase 4
A4 = ("Ficha azteca 4: Los aztecas creían en muchos dioses. Huitzilopochtli estaba asociado a la guerra y al Sol; Tláloc, a la lluvia. En la cima del Templo Mayor había dos santuarios, uno para cada dios. "
      "Creían que los dioses necesitaban ofrendas para que el mundo siguiera funcionando; por eso hacían sacrificios, incluidos sacrificios humanos, sobre todo de prisioneros de guerra. "
      "Los aztecas también guerreaban para dominar a otros pueblos y cobrar tributo. "
      "Hoy la Ciudad de México está construida sobre lo que fue Tenochtitlán. Gran parte del lago fue secado con los siglos, y las calzadas se transformaron en calles. "
      "Dos miradas: el códice indígena muestra los tributos como parte del orden del imperio; un soldado español cuenta los ritos con espanto.")
register(
    OA2, 4,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé sobre la religión de los aztecas, su relación con la guerra y qué cambió y qué continúa en el lugar donde estaba Tenochtitlán.",
    prior=["Sé qué es el tributo.", "Sé que una perspectiva es un punto de vista."],
    explain=[
        "Los aztecas adoraban a muchos dioses. Huitzilopochtli se asociaba con la guerra y el Sol, y Tláloc con la lluvia. En la cima del Templo Mayor había un santuario para cada uno. Creían que los dioses necesitaban ofrendas para que el mundo siguiera funcionando.",
        "Por eso hacían ceremonias con ofrendas y sacrificios, incluidos sacrificios humanos, sobre todo de prisioneros de guerra. Es un tema muy delicado que debemos explicar con respeto. La guerra tenía también un fin económico: dominar a otros pueblos y cobrar tributo. Religión y guerra estaban relacionadas.",
        "Las fuentes miran estos hechos desde perspectivas distintas. El códice indígena muestra los tributos como parte del orden del imperio. Un soldado español describe los ritos con espanto. Además, hay cambios y continuidades: hoy la Ciudad de México está sobre Tenochtitlán, pero gran parte del lago fue secado y las calzadas son calles.",
    ],
    vocab=[("sacrificio", "ofrenda ritual en que se entrega una vida"), ("santuario", "lugar sagrado donde se honra a un dios"), ("cambio", "algo que ya no es igual que antes"), ("continuidad", "algo que sigue igual a través del tiempo"), ("perspectiva", "punto de vista desde el que alguien cuenta algo")],
    worked=[
        {"title": "Identificar un cambio", "problem": f"{A4} ¿Qué cambió del lago de Tenochtitlán con los siglos?", "steps": ["Busco lo que dice la ficha sobre el lago.", "Gran parte fue secado y las calzadas son calles."], "answer": "Gran parte del lago fue secado y las calzadas se transformaron en calles"},
        {"title": "Identificar una continuidad", "problem": f"{A4} ¿Qué continúa en el mismo lugar de Tenochtitlán?", "steps": ["Pienso en lo que hay hoy donde estaba la ciudad.", "La ficha dice que la Ciudad de México está sobre Tenochtitlán."], "answer": "Hay una gran ciudad en el mismo lugar"},
    ],
    mistakes=[
        {"wrong": "Decir que Tenochtitlán desapareció del todo.", "why": "Se confunde la caída del imperio con el fin del lugar.", "fix": "Recuerda que la Ciudad de México está sobre Tenochtitlán."},
        {"wrong": "Decir que los aztecas solo hacían guerra y sacrificios.", "why": "Se exagera un solo aspecto.", "fix": "Piensa también en cultivos, comercio, escuelas y ciudad."},
    ],
    tiers={
        "recovery": [
            ex(f"{A4} ¿Con qué se asociaba el dios Tláloc?", "con la lluvia", "La ficha lo indica."),
            ex(f"{A4} ¿Con qué se asociaba Huitzilopochtli?", "con la guerra y el Sol", "La ficha da esas dos asociaciones."),
            ex(f"{A4} ¿Cuántos santuarios había en la cima del Templo Mayor?", "dos", "Había uno para cada dios."),
        ],
        "understand": [
            ex(f"{A4} ¿Por qué hacían ofrendas los aztecas?", "porque creían que los dioses las necesitaban para que el mundo siguiera funcionando", "La ficha lo explica."),
            ex(f"{A4} ¿Para qué guerreaban los aztecas, además de los sacrificios?", "para dominar a otros pueblos y cobrar tributo", "La guerra tenía un fin económico."),
            ex(f"{A4} ¿Qué hay hoy sobre Tenochtitlán?", "la Ciudad de México", "La ficha lo dice."),
        ],
        "apply": [
            ex(f"{A4} Clasifica como «cambio» o «continuidad»: hoy hay una gran ciudad donde estaba la capital azteca.", "continuidad", "Un lugar de ciudad sigue siendo ciudad."),
            ex(f"{A4} Clasifica como «cambio» o «continuidad»: las calzadas sobre el lago hoy son calles.", "cambio", "La forma de los caminos y el lago cambiaron."),
            ex(f"{A4} Clasifica como «cambio» o «continuidad»: el lago cubría gran parte del valle y hoy está en su mayoría seco.", "cambio", "El lago fue secado con los siglos."),
        ],
        "reason": [
            ex(f"{A4} Sofía dice: «Los aztecas guerreaban solo por religión». ¿Qué dato de la ficha completa su idea?", "También guerreaban para dominar a otros pueblos y cobrar tributo", "La guerra tenía un fin económico."),
            ex(f"{A4} Pedro dice que el códice y el soldado español cuentan lo mismo con el mismo tono. ¿Es cierto?", "No, el códice muestra el orden del imperio y el soldado cuenta con espanto", "Tienen perspectivas distintas."),
        ],
        "challenge": [
            ex(f"{A4} Si quisieras saber qué pensaban los aztecas de sus ritos, ¿qué fuente necesitarías más: una hecha por aztecas o la del soldado?", "una hecha por aztecas", "Es la que muestra su propia perspectiva."),
            ex(f"{A4} Clara dice: «Hoy no queda nada de Tenochtitlán». ¿Qué dato de la ficha la contradice?", "La Ciudad de México está construida sobre lo que fue Tenochtitlán", "El lugar sigue habitado."),
        ],
    },
    context=[ex("Un guía dice: «Caminas por una calle de la Ciudad de México que antes era una calzada sobre el lago». ¿Qué cambió y qué continúa?", "cambió el entorno, porque el lago casi no existe; continúa el camino en el mismo lugar", "El lugar es el mismo, pero hoy es una calle.")],
    selfcheck=[
        ex("¿Qué dios se asociaba con la lluvia?", "Tláloc", "La ficha lo indica."),
        ex("¿Qué es una continuidad?", "algo que sigue igual a través del tiempo", "Es lo contrario de un cambio."),
        ex("¿Por qué las fuentes pueden contar distinto los ritos aztecas?", "porque tienen perspectivas distintas", "Cada autor los mira desde su punto de vista."),
    ],
    open_task=task(
        f"Haz una tabla de dos columnas: «Tenochtitlán antes de 1521» y «Ciudad de México hoy». Escribe en cada una tres datos de la ficha. Al final subraya una continuidad y encierra un cambio. {A4}",
        "Antes: isla en el lago, calzadas, Templo Mayor. Hoy: ciudad sobre Tenochtitlán, lago casi seco, calzadas convertidas en calles. Continuidad: hay una gran ciudad en el mismo lugar.",
        ["tres datos por columna", "una continuidad", "un cambio"], ["tabla de dos columnas"], ["inventar datos que la ficha no entrega", "confundir cambio con continuidad"],
        "Pregunta cómo supo que algo era un cambio. Debe comparar antes y hoy."),
    reinforce="Explica con tus palabras un cambio y una continuidad entre Tenochtitlán y la Ciudad de México.",
    extend="Piensa en un lugar de tu ciudad que haya cambiado y uno que siga igual, y descríbelos.",
)

# ---------------------------------------------------------------- clase 5
A5 = ("Ficha azteca 5: Para decidir si Tenochtitlán era una ciudad grande y organizada, un historiador reúne estos datos. (1) Estaba sobre una isla unida por calzadas y atravesada por canales. "
      "(2) Un acueducto llevaba agua potable. (3) Tenía un gran templo en el centro y un mercado muy concurrido. (4) Había chinampas que producían alimentos. "
      "(5) Los españoles que llegaron en 1519 se asombraron al verla. (6) Se sabe poco sobre el número exacto de habitantes, porque las fuentes no coinciden en las cifras.")
register(
    OA2, 5,
    materials="Lápiz y papel. La ficha está escrita en cada ejercicio.",
    use="Aprenderé a defender una conclusión sobre Tenochtitlán con evidencia y a reconocer lo que no sabemos.",
    prior=["Sé que un argumento tiene afirmación, evidencia y límite.", "Sé cómo era la ciudad y la sociedad azteca."],
    explain=[
        "Para argumentar sobre el pasado, partimos de una pregunta y de datos. La pregunta de hoy es: ¿Tenochtitlán era una ciudad grande y organizada? Cada dato de la ficha es una pista que apoya o no apoya esa idea.",
        "Hay varias pistas que apoyan la idea de una ciudad organizada: calzadas y canales, un acueducto, un gran templo, un mercado concurrido y chinampas que producían alimentos. Además, los españoles de 1519 se asombraron al verla. Todas son evidencias de planificación y de actividad económica.",
        "Pero un buen argumento también reconoce un límite. La ficha dice que no se sabe el número exacto de habitantes, porque las fuentes no coinciden. Entonces podemos decir que era una ciudad organizada, pero no afirmar una cifra exacta. La conclusión debe ser tan grande como la evidencia, ni más ni menos.",
    ],
    vocab=[("planificación", "organización previa de cómo hacer algo"), ("evidencia", "dato o fuente que apoya una idea"), ("límite", "lo que no sabemos o no podemos afirmar"), ("conclusión", "idea final después de analizar"), ("mercado", "lugar donde se compra y se vende")],
    worked=[
        {"title": "Elegir evidencia", "problem": f"{A5} Afirmación: «Tenochtitlán tenía buena organización del agua». ¿Qué dato la apoya?", "steps": ["Busco un dato sobre el agua.", "Los datos 1 y 2: canales y acueducto."], "answer": "Los canales y el acueducto que llevaba agua potable"},
        {"title": "Reconocer un límite", "problem": f"{A5} ¿Podemos decir cuántos habitantes tenía exactamente?", "steps": ["Busco lo que dice el dato 6.", "Dice que las fuentes no coinciden en las cifras."], "answer": "No, no se sabe la cifra exacta"},
    ],
    mistakes=[
        {"wrong": "Dar una cifra exacta de habitantes como si fuera segura.", "why": "Se toma un número leído sin revisar su fuente.", "fix": "Di que las fuentes no coinciden en la cifra."},
        {"wrong": "Concluir que era la mejor ciudad del mundo sin comparar.", "why": "La ficha no compara con otras ciudades.", "fix": "Concluye solo lo que los datos permiten."},
    ],
    tiers={
        "recovery": [
            ex(f"{A5} ¿Qué llevaba agua potable a la ciudad?", "un acueducto", "Es el dato 2 de la ficha."),
            ex(f"{A5} ¿En qué año llegaron los españoles que se asombraron?", "1519", "El dato 5 lo indica."),
            ex(f"{A5} ¿Qué producían las chinampas?", "alimentos", "El dato 4 dice que producían alimentos."),
        ],
        "understand": [
            ex(f"{A5} ¿Qué dato nos muestra que no hay una cifra segura de habitantes?", "el dato 6", "Dice que las fuentes no coinciden."),
            ex(f"{A5} ¿Qué se pregunta el historiador al comienzo?", "si Tenochtitlán era una ciudad grande y organizada", "Esa es la pregunta de la ficha."),
            ex(f"{A5} El asombro de los españoles, ¿es un testimonio de lo que ellos vieron o una cifra de habitantes?", "un testimonio de lo que ellos vieron", "Muestra su impresión, no una medida."),
        ],
        "apply": [
            ex(f"{A5} Afirmación: «La ciudad tenía actividad económica». ¿Qué dos datos la apoyan?", "el mercado concurrido y las chinampas", "Muestran comercio y producción de alimentos."),
            ex(f"{A5} Afirmación: «La ciudad tenía una planificación de caminos». ¿Qué dato la apoya?", "las calzadas y canales", "Son el dato 1 de la ficha."),
            ex(f"{A5} Elige la mejor conclusión. A) Tenochtitlán tenía exactamente 300.000 habitantes. B) Tenochtitlán era una ciudad organizada, pero no se sabe su número exacto de habitantes.", "B", "B respeta el límite de la evidencia."),
        ],
        "reason": [
            ex(f"{A5} Ema dice: «El asombro de los españoles prueba que Tenochtitlán era la ciudad más grande del mundo». ¿Qué falla tiene?", "El asombro muestra su impresión, pero no prueba una comparación con todas las ciudades", "La evidencia no alcanza para esa afirmación."),
            ex(f"{A5} Luz dice: «La ficha no tiene datos sobre la actividad de las personas». ¿Qué datos la contradicen?", "el mercado concurrido y las chinampas", "Ambos muestran actividad cotidiana."),
        ],
        "challenge": [
            ex(f"{A5} Marca cada parte: afirmación, evidencia o límite. a) «Tenochtitlán era una ciudad organizada». b) «Tenía un acueducto y canales». c) «No se sabe el número exacto de habitantes».", "a: afirmación; b: evidencia; c: límite", "Cada frase cumple una función distinta."),
            ex(f"{A5} Dos estudiantes: Rosa dice «Sabemos que había exactamente 200.000 personas»; Tomás dice «Era grande, pero el número exacto no se conoce». ¿Quién argumenta mejor?", "Tomás", "Respeta lo que las fuentes permiten afirmar."),
        ],
    },
    context=[ex("Un vecino dice que los aztecas «no sabían construir bien». ¿Qué dos datos de la ficha podrías usar para responder?", "las calzadas y el acueducto", "Muestran obras planificadas.")],
    selfcheck=[
        ex("¿Cuáles son las tres partes de un buen argumento?", "afirmación, evidencia y límite", "Así se arma una idea bien sostenida."),
        ex(f"{A5} ¿Qué datos muestran que Tenochtitlán estaba organizada?", "calzadas, canales, acueducto, templo, mercado y chinampas", "Son los datos de planificación de la ficha."),
        ex(f"{A5} ¿Qué no podemos afirmar con seguridad?", "el número exacto de habitantes", "Las fuentes no coinciden."),
    ],
    open_task=task(
        f"Responde por escrito: «¿Tenochtitlán era una ciudad grande y organizada?». Escribe cuatro frases: tu afirmación, dos evidencias de la ficha y un límite. {A5}",
        "Pienso que Tenochtitlán era una ciudad organizada. Tenía calzadas y canales. Tenía un acueducto que llevaba agua potable. No se sabe cuántos habitantes tenía exactamente.",
        ["afirmación clara", "dos evidencias de la ficha", "un límite"], ["cuatro frases"], ["dar una cifra exacta", "olvidar el límite"],
        "Pide que subraye la afirmación, encierre las evidencias y marque el límite con una cruz."),
    reinforce="Explica en voz alta una afirmación sobre Tenochtitlán con una evidencia.",
    extend="Escribe una pregunta sobre los aztecas que no se puede responder con esta ficha.",
)
