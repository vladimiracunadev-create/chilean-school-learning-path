"""Filosofía política (electivo HC, 3.º y 4.º medio): OAC-01 (preguntas e hipótesis sobre un problema político, clases 1 a 4) y OAC-02 (relaciones de poder y bien común, clases 1 a 5). Casos ficticios y textos de ejemplo escritos para este cuaderno."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada caso y cada texto está escrito en el enunciado. "
             "Los lugares, las personas y los textos son ficticios o «de ejemplo»: sirven para practicar el razonamiento filosófico y no son citas de ningún autor. "
             "Las posturas se presentan con sus razones y sin tomar partido por un sector político: tu tarea es entenderlas, compararlas y evaluarlas con argumentos. "
             "Si un caso te incomoda, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O1 = "FI-FIPO-3y4-OAC-01"
O2 = "FI-FIPO-3y4-OAC-02"

# ============================================================ OAC-01, clase 1
F = ("Ficha 1 (caso ficticio). El municipio de «Villa Lomaverde» (no existe) anunció que cerrará de noche la plaza central por reclamos de ruido. "
     "Vecina A: «La plaza es de todos; cerrarla es quitarnos un espacio común.» "
     "Vecino B: «Si no se regula, unos pocos perjudican el descanso de muchos.» "
     "Funcionaria C: «Las normas del municipio permiten cerrar espacios públicos en ciertos horarios.»")
build(
    O1, 1, F,
    use="Aprenderé a pasar de una situación política a una pregunta filosófica bien formulada y a una hipótesis que se pueda examinar con razones.",
    prior=["Distingo un hecho de una opinión.", "Sé que una tesis es una idea que se defiende con razones.", "Conozco la diferencia entre una norma y su justificación."],
    explain=[
        "Un problema político es una situación en la que hay que decidir cómo se ejerce el poder o cómo se convive, y las personas no coinciden sobre lo que es justo. Alrededor de un mismo problema caben tres tipos de pregunta. La pregunta fáctica se responde averiguando datos («¿cuántos reclamos hubo?»). La pregunta jurídica se responde leyendo una norma («¿qué permite la ordenanza?»). La pregunta filosófica, en cambio, pide aclarar conceptos y evaluar razones («¿es justo restringir un espacio común para proteger el descanso?»). Cuando pregunta qué se debe hacer o qué es justo, se llama pregunta normativa.",
        "Una buena pregunta filosófica es abierta, precisa y tiene conceptos que se pueden definir, como justicia, espacio común o libertad. Una hipótesis es una respuesta tentativa a esa pregunta, formulada con una razón, que se somete a examen: se apoya con argumentos y se pone a prueba con objeciones. Que algo sea legal no responde por sí solo si es justo, y que algo nos moleste no lo vuelve injusto.",
        "Leer un texto filosófico para problematizar significa buscar qué pregunta intenta responder, qué conceptos usa y qué otra respuesta sería posible. Trabajarás con varias perspectivas: una perspectiva es el punto de vista desde el cual se mira un problema, con sus razones, y no se reduce a una opinión sin fundamento.",
    ],
    vocab=[("problema político", "situación en que hay que decidir cómo se ejerce el poder o se convive, sin acuerdo sobre lo justo"), ("pregunta fáctica", "pregunta que se responde averiguando datos"), ("pregunta jurídica", "pregunta que se responde leyendo una norma"), ("pregunta filosófica", "pregunta que exige aclarar conceptos y evaluar razones"), ("pregunta normativa", "pregunta filosófica sobre qué se debe hacer o qué es justo"), ("hipótesis", "respuesta tentativa con una razón, abierta a examen"), ("perspectiva", "punto de vista con razones desde el cual se mira un problema")],
    worked=[
        ("Clasificar una pregunta", "Sobre la plaza de la ficha se pregunta: «¿Cuántas personas firmaron la carta de reclamo?». ¿Qué tipo de pregunta es?",
         ["Pregunto si se responde con un dato o con una norma: basta contar las firmas.", "No hay que aclarar conceptos ni evaluar razones sobre lo justo."],
         "Es una pregunta fáctica"),
        ("Mejorar una pregunta vaga", "Un estudiante propone: «¿Está bien cerrar la plaza?». Mejórala como pregunta filosófica.",
         ["Detecto lo vago: «bien» no dice según qué criterio, y no aparecen conceptos que se puedan definir.", "Incorporo conceptos y un criterio: espacio común, descanso y justicia."],
         "«¿Es justo restringir de noche el uso de un espacio común para proteger el descanso de quienes viven cerca?»"),
    ],
    mistakes=[("Creer que toda pregunta sobre política es filosófica, incluso las que piden un dato.", "Se confunde hablar de un tema político con examinar razones y conceptos.", "Pregúntate si la respuesta se encuentra en un dato o en una norma; si exige evaluar razones, es filosófica."),
              ("Formular una pregunta que solo pide estar a favor o en contra, sin conceptos ni criterio.", "Una pregunta vaga invita a opinar sin razones y no se puede examinar.", "Nombra los conceptos en juego (justicia, libertad, bien común) y el criterio que usarás para responder.")],
    T=[
        ("abc", "¿Qué tipo de pregunta es «¿Cuántos reclamos por ruido recibió el municipio durante un mes?»?", "Fáctica, porque se responde averiguando datos", "Jurídica, porque se responde leyendo una norma", "Filosófica, porque trata de un problema político", "Se responde contando reclamos, así que basta un dato y no hace falta evaluar razones."),
        ("abc", "¿Qué tipo de pregunta es «¿Qué dice la ordenanza municipal sobre los horarios de las plazas?»?", "Jurídica, porque se responde leyendo la norma", "Fáctica, porque se responde midiendo el ruido", "Filosófica, porque exige definir la justicia", "Pregunta por el contenido de una norma, que se resuelve leyéndola."),
        ("abc", "¿Qué tipo de pregunta es «¿Es justo limitar un espacio común para proteger el descanso de una parte de los vecinos?»?", "Filosófica, porque exige aclarar conceptos y evaluar razones", "Fáctica, porque se responde con una encuesta", "Jurídica, porque la responde un abogado", "Ninguna encuesta ni ley decide por sí sola qué es justo; hay que evaluar razones."),
        ("abc", "Según la explicación, ¿qué vuelve «política» a una situación?", "Que hay que decidir cómo se ejerce el poder o se convive y no hay acuerdo sobre lo justo", "Que participa un político o una autoridad", "Que el tema aparece en los medios de comunicación", "Lo político es la decisión sobre poder y convivencia con desacuerdo sobre lo justo, no quién habla ni dónde aparece."),
        ("abc", "{F} ¿Qué valor defiende principalmente el Vecino B?", "El descanso de la mayoría de los vecinos", "El uso libre de la plaza a toda hora", "La obediencia a la norma por sí misma", "Su razón es que unos pocos perjudican el descanso de muchos."),
        ("ab", "¿Cuál es la mejor pregunta filosófica sobre el caso?", "¿Qué razones justifican restringir un espacio común y cuándo dejan de ser suficientes?", "¿Está bien o mal la plaza?", "La primera tiene conceptos precisos y pide evaluar razones, mientras la segunda es vaga."),
        ("abc", "El centro de estudiantes de un liceo ficticio propone que el patio se use solo en los recreos. ¿Cuál es una pregunta filosófica sobre esa propuesta?", "¿Es justo limitar el uso de un espacio compartido para ordenar la convivencia?", "¿Cuántos metros cuadrados tiene el patio?", "¿Qué artículo del reglamento menciona el patio?", "Solo la primera exige evaluar razones sobre lo justo; las otras se resuelven con un dato o una norma."),
        ("abc", "¿Cuál de estas frases es una hipótesis filosófica sobre el caso?", "Restringir un espacio común es justo solo si la medida es temporal y existe una alternativa para quienes lo usan", "¿Quién decidió cerrar la plaza?", "Hubo muchos reclamos durante el mes", "Una hipótesis es una respuesta tentativa con una razón; las otras opciones son una pregunta y un dato."),
        ("abc", "Alguien escribe: «La plaza debería cerrarse porque a mí me molesta el ruido». ¿Por qué no basta como hipótesis filosófica?", "Expresa una molestia personal y no una razón que otros puedan evaluar", "Porque habla de una plaza y no del país entero", "Porque no menciona ninguna ley", "Una hipótesis necesita una razón examinable; una molestia personal no muestra por qué sería justo restringir."),
        ("abc", "{F} La Funcionaria C responde solo qué permiten las normas. ¿Por qué eso no cierra la pregunta filosófica de si el cierre es justo?", "Porque que algo esté permitido no responde si es justo", "Porque las normas municipales nunca valen", "Porque la funcionaria no vive en el barrio", "La norma responde la pregunta jurídica, pero la justicia de la medida sigue abierta a evaluación."),
        ("abc", "¿Qué hace examinable a una hipótesis?", "Que se puede apoyar con argumentos y rebatir con objeciones", "Que la mayoría de las personas la acepte", "Que la haya dicho alguien con un cargo importante", "Examinar es poner a prueba con razones, no contar adhesiones ni autoridades."),
        ("abc", "Un grupo investiga si un cierre es justo. ¿Qué conviene hacer primero?", "Separar qué es dato, qué es norma y qué es valoración", "Votar y aceptar lo que decida la mayoría", "Buscar la opinión de la persona más conocida", "Distinguir los tipos de afirmación evita tratar una valoración como si fuera un dato."),
        ("abc", "Si la plaza fuera el único espacio verde del barrio, ¿qué cambia en la pregunta filosófica?", "Pesa más el valor del uso común, porque no habría alternativa", "La pregunta deja de ser política", "Desaparece el conflicto entre descanso y uso común", "Al faltar alternativas, restringir el uso afecta más el valor de lo común y la hipótesis debe revisarse."),
    ],
    ctx=("abc", "Una biblioteca ficticia de barrio decide cobrar entrada para financiar su mantención. Tres jóvenes discuten. ¿Cuál formula una pregunta filosófica y no solo un dato?", "¿Es justo cobrar por el acceso a un bien que sirve a toda la comunidad?", "¿Cuánto costará la entrada el próximo mes?", "¿Qué dice el contrato del arriendo del local?", "Solo la primera exige evaluar razones sobre justicia y acceso común; las demás piden un dato o un documento."),
    sc=[
        ("En Filosofía política: ¿qué es una pregunta normativa?", "La que pregunta qué se debe hacer o qué es justo", "Pide evaluar razones sobre lo que debería ocurrir, no solo describir lo que ocurre."),
        ("¿Qué es una hipótesis en esta clase?", "Una respuesta tentativa con una razón, abierta a examen", "Se formula para ser apoyada o rebatida con argumentos."),
        ("¿Por qué «es legal» no responde la pregunta de si algo es justo?", "Porque la norma responde lo jurídico y la justicia exige evaluar razones", "Una medida puede estar permitida y aun así discutirse como injusta."),
    ],
    op=("Elige una de estas dos situaciones ficticias. Situación 1: un liceo cierra con llave la sala de estudio después de las 18:00 para ahorrar energía. Situación 2: una junta de vecinos decide que solo los socios pueden usar la cancha del sector. "
        "Escribe una pregunta fáctica, una jurídica y una filosófica sobre la situación elegida, y luego una hipótesis que incluya una razón.",
        "Situación 1. Fáctica: ¿cuántos estudiantes usan la sala después de las 18:00? Jurídica: ¿qué dice el reglamento sobre el uso de salas? Filosófica: ¿es justo restringir un espacio de estudio para ahorrar energía? Hipótesis: es justo solo si existe otro lugar de estudio igual de accesible.",
        ["escribe tres preguntas de tipos distintos y bien clasificadas", "la pregunta filosófica contiene conceptos que se pueden definir", "la hipótesis es una respuesta tentativa e incluye una razón", "no mezcla un dato con una valoración"],
        ["tres preguntas y una hipótesis escritas sobre la situación elegida"],
        ["formular una pregunta filosófica que se responde con un dato", "escribir como hipótesis una simple preferencia personal", "usar «bien» o «mal» sin criterio"],
        "Pregunta: «¿tu pregunta filosófica se podría responder solo con un dato o una ley?». Si es así, pídele que agregue un concepto y un criterio."),
    reinforce="Elige un problema de tu entorno (un horario, una regla, un espacio compartido) y escribe una pregunta fáctica y una filosófica sobre él.",
    extend="Busca en una conversación o noticia una frase que mezcle un dato con una valoración y sepáralas por escrito en dos columnas.",
)

# ============================================================ OAC-01, clase 2
F = ("Ficha 2 (de ejemplo). En un taller ficticio se proponen tres definiciones de «autoridad». "
     "D1: «Autoridad es cualquier persona que logra que otros hagan lo que ella quiere.» "
     "D2: «Autoridad es el poder que un grupo reconoce como legítimo en un ámbito determinado.» "
     "D3: «Autoridad es solo la persona que figura con un cargo en el organigrama.»")
build(
    O1, 2, F,
    use="Aprenderé a definir conceptos políticos con rasgos claros y a probar una definición con ejemplos y contraejemplos.",
    prior=["Sé formular una pregunta filosófica.", "Distingo una norma de su justificación.", "Sé qué es un ejemplo."],
    explain=[
        "Definir un concepto es indicar qué rasgos debe tener algo para que podamos decidir si un caso entra o no. Poder es la capacidad de lograr que otros actúen de cierta manera, con o sin su acuerdo. Autoridad es el poder que un grupo reconoce como legítimo en un ámbito, como el de un capitán de equipo en el juego. Legitimidad es la justificación aceptada de por qué alguien puede mandar.",
        "Una definición se prueba con ejemplos y contraejemplos. Un ejemplo es un caso que cumple los rasgos. Un contraejemplo es un caso que muestra que la definición deja entrar algo que no debería (demasiado amplia) o deja fuera algo que sí debería (demasiado estrecha). Si un asaltante lograra que le entreguen dinero, una definición que lo llame «autoridad» sería demasiado amplia.",
        "Definir antes de discutir evita que dos personas crean estar en desacuerdo cuando solo usan una palabra de distinta manera. En esta clase se usa la definición de autoridad como poder reconocido como legítimo en un ámbito, que será el criterio para evaluar las propuestas.",
    ],
    vocab=[("poder", "capacidad de lograr que otros actúen de cierta manera, con o sin su acuerdo"), ("autoridad", "poder que un grupo reconoce como legítimo en un ámbito"), ("legitimidad", "justificación aceptada de por qué alguien puede mandar"), ("contraejemplo", "caso que muestra que una definición incluye o excluye algo que no corresponde"), ("definición amplia", "deja entrar casos que no deberían entrar"), ("definición estrecha", "deja fuera casos que sí deberían entrar")],
    worked=[
        ("Buscar un contraejemplo", "¿Qué contraejemplo muestra que D1 de la ficha es demasiado amplia?",
         ["Busco un caso que cumpla D1 pero no sea autoridad: alguien que obliga a otros por la fuerza.", "Ese caso logra lo que quiere, pero nadie lo reconoce como legítimo."],
         "Quien logra que otros obedezcan por la fuerza cumple D1 sin tener autoridad; por eso D1 es amplia"),
        ("Aplicar los rasgos", "Una presidenta de club elegida por votación decide cómo se reparten las canchas. ¿Tiene autoridad según la definición de la clase?",
         ["Rasgo 1: tiene poder, porque sus decisiones se cumplen.", "Rasgo 2: el grupo la reconoce como legítima y su ámbito es el reparto de canchas."],
         "Sí, tiene autoridad en el ámbito del club"),
    ],
    mistakes=[("Confundir poder con autoridad y decir que quien consigue obediencia siempre tiene autoridad.", "Se olvida el rasgo del reconocimiento legítimo.", "Pregunta si el grupo reconoce el derecho de esa persona a decidir en ese ámbito."),
              ("Dar solo ejemplos que confirman la definición y no buscar contraejemplos.", "Una definición parece buena cuando solo se miran los casos fáciles.", "Busca un caso extraño que la rompa antes de aceptarla.")],
    T=[
        ("abc", "Según la explicación, ¿qué es el poder?", "La capacidad de lograr que otros actúen de cierta manera, con o sin su acuerdo", "El derecho reconocido a mandar en un ámbito", "El cargo que aparece en un organigrama", "El poder no exige reconocimiento; ese rasgo es el que se agrega para hablar de autoridad."),
        ("abc", "¿Qué rasgo agrega la autoridad al poder?", "El reconocimiento legítimo del grupo en un ámbito", "El uso de la fuerza", "El tener un cargo con nombre propio", "La autoridad es el poder que el grupo reconoce como legítimo en un ámbito."),
        ("En Filosofía política: ¿cómo se llama la justificación aceptada de por qué alguien puede mandar?", "Legitimidad", "Es el término que nombra esa justificación que los demás aceptan."),
        ("abc", "{F} ¿Cuál de las tres definiciones coincide con la de esta clase?", "D2", "D1", "D3", "D2 incluye poder, reconocimiento legítimo y ámbito, que son los rasgos de la clase."),
        ("abc", "Alguien propone esta definición: «Autoridad es toda persona que tiene más dinero que el resto del grupo». ¿Por qué es demasiado amplia?", "Incluiría a personas con dinero a quienes nadie reconoce el derecho a decidir en ningún ámbito", "Porque deja fuera a quien tiene un cargo", "Porque no menciona la palabra legitimidad", "Entran casos que no cumplen el rasgo central: el reconocimiento legítimo del grupo en un ámbito."),
        ("ab", "¿Qué es un contraejemplo?", "Un caso que muestra que una definición incluye o excluye algo que no corresponde", "Un caso que confirma la definición", "El contraejemplo sirve para poner a prueba una definición mostrando dónde falla."),
        ("abc", "En un club ficticio nadie reconoce a Tomás como encargado, pero él logra que le cedan la cancha porque amenaza con no jugar más. Según la clase, ¿qué tiene Tomás?", "Poder sin autoridad, porque nadie lo reconoce como legítimo", "Autoridad, porque logra lo que quiere", "Ni poder ni autoridad, porque no tiene cargo", "Logra su efecto, así que tiene poder, pero falta el reconocimiento legítimo."),
        ("abc", "Una vecina sin cargo es reconocida por todos como quien puede decidir cómo se reparte el uso de la sede en un barrio ficticio. Según la clase, ¿qué podemos decir?", "Tiene autoridad en el ámbito de la sede, aunque no tenga cargo", "No tiene autoridad, porque no tiene cargo", "Solo tiene poder, porque nadie la eligió", "Hay poder reconocido como legítimo en un ámbito, y eso define la autoridad según la clase."),
        ("abc", "{F} ¿Qué contraejemplo muestra que D3 es demasiado estrecha según la definición de la clase?", "Una persona sin cargo a quien el grupo reconoce el derecho a decidir en un ámbito", "Un asaltante que logra que le entreguen dinero", "Una persona con cargo a quien el grupo sigue reconociendo", "D3 dejaría fuera a quien tiene poder reconocido como legítimo sin figurar en el organigrama."),
        ("abc", "Alguien propone: «Autoridad es toda persona mayor de edad». ¿Cuál es el problema?", "Es demasiado amplia, porque incluye a mayores que nadie reconoce como legítimos en ningún ámbito", "Es demasiado estrecha, porque deja fuera a los adultos", "Es correcta, porque los adultos siempre tienen poder", "Entrarían personas sin poder reconocido, así que la definición incluye casos que no corresponden."),
        ("abc", "¿Por qué conviene definir antes de discutir?", "Porque dos personas pueden creer que discrepan cuando solo usan la palabra de distinta manera", "Porque así se evita todo desacuerdo político", "Porque las definiciones siempre son verdaderas", "Aclarar el significado permite saber si el desacuerdo es de fondo o de lenguaje."),
        ("abc", "¿Cuál es la mejor definición de legitimidad según la clase?", "Una justificación aceptada de por qué alguien puede mandar", "La capacidad de castigar a quien desobedece", "El número de personas que obedecen una orden", "La legitimidad se refiere a la justificación aceptada, no a la fuerza ni a la cantidad."),
        ("abc", "Un delegado conserva su cargo, pero sus compañeros dejaron de reconocer su derecho a decidir sobre el uso de la sala. ¿Qué conserva y qué perdió según la clase?", "Conserva el cargo formal y perdió el reconocimiento legítimo, es decir, la autoridad", "Conserva la autoridad y perdió el cargo", "Perdió el poder y la legitimidad, pero conserva el cargo", "El cargo sigue en el papel, pero sin reconocimiento del grupo falta el rasgo central de la autoridad."),
    ],
    ctx=("abc", "En una cooperativa ficticia, el gerente fija las reglas de turnos. Una socia dice: «Obedezco porque me pagan, no porque lo vea justo». Según la clase, ¿qué le falta al gerente respecto de ella?", "Legitimidad reconocida por la socia", "Poder, porque sus órdenes se cumplen", "Un cargo en el organigrama", "Las órdenes se cumplen y hay cargo, pero la socia no reconoce el derecho a mandar, y eso es legitimidad."),
    sc=[
        ("En Filosofía política: ¿qué es la autoridad?", "El poder que un grupo reconoce como legítimo en un ámbito", "Combina poder, reconocimiento legítimo y ámbito."),
        ("¿Qué muestra un contraejemplo?", "Que una definición incluye o excluye algo que no corresponde", "Sirve para detectar definiciones demasiado amplias o estrechas."),
        ("¿Puede haber poder sin autoridad? Responde sí o no con una razón.", "Sí: quien logra que otros actúen por la fuerza tiene poder sin reconocimiento legítimo", "La autoridad exige reconocimiento legítimo; el poder, no."),
    ],
    op=("Elige uno de estos conceptos: «líder», «norma justa» o «espacio público». Escribe una definición de dos o tres rasgos, un ejemplo que la cumpla y un contraejemplo que muestre si tu definición es amplia o estrecha. "
        "Luego corrígela una vez para mejorarla.",
        "Concepto: líder. Definición: persona a la que un grupo sigue en una tarea común porque reconoce su orientación. Ejemplo: la capitana que organiza el equipo. Contraejemplo: alguien a quien siguen solo por miedo (la definición lo excluye, y eso es lo esperado). Corrección: agregar «voluntariamente».",
        ["la definición tiene al menos dos rasgos claros", "incluye un ejemplo y un contraejemplo bien elegidos", "indica si la definición es amplia o estrecha", "mejora la definición después del contraejemplo"],
        ["definición, ejemplo, contraejemplo y versión corregida"],
        ["definir con un sinónimo", "dar solo ejemplos fáciles", "no corregir la definición tras el contraejemplo"],
        "Pregunta: «¿qué caso extraño podría romper tu definición?». Pídele que lo busque y la corrija."),
    reinforce="Escribe tu propia definición de «poder» y busca un contraejemplo de la vida escolar que la ponga a prueba.",
    extend="Compara tu definición de autoridad con la de una persona cercana y escribe en qué rasgos coinciden y en cuáles difieren.",
)

# ============================================================ OAC-01, clase 3
F = ("Ficha 3 (textos de ejemplo escritos para este cuaderno; no son citas de ningún autor). "
     "Texto A: «Sin reglas comunes ni alguien que las haga cumplir, cada persona desconfía de las demás y vive con temor. Por eso conviene que todos cedan parte de su libertad a una autoridad que garantice la seguridad.» "
     "Texto B: «Las personas cooperan cuando se reconocen como iguales. Una autoridad es legítima solo si nace del acuerdo libre de quienes la integran y estos pueden corregirla.»")
build(
    O1, 3, F,
    use="Aprenderé a reconstruir la perspectiva de un texto: su tesis, sus razones y su idea del ser humano, antes de criticarla.",
    prior=["Sé formular una pregunta filosófica.", "Sé definir un concepto con rasgos.", "Distingo una tesis de una razón."],
    explain=[
        "Reconstruir una perspectiva es explicar con tus palabras qué sostiene un texto y por qué, sin agregar ni quitar nada. Se busca la tesis (lo que se defiende), las razones (por qué se defiende) y el supuesto sobre el ser humano (cómo se lo imagina: temeroso, cooperativo, egoísta, solidario). Sin ese supuesto, muchas conclusiones políticas parecen caídas del cielo.",
        "Un texto como el A recuerda a la tradición contractualista, que explica la autoridad como un acuerdo para vivir en común. Un texto como el B recuerda a una versión de esa tradición que pone el acento en la igualdad y el control de quienes obedecen. Son textos de ejemplo, así que no sabemos qué autor real los suscribiría: lo que importa aquí es el razonamiento.",
        "El principio de caridad indica reconstruir la versión más fuerte de una postura antes de criticarla. Atacar a la persona que habla o deformar su tesis no es criticar: critica la tesis, no a quien la sostiene. Reconstruir bien no significa estar de acuerdo.",
    ],
    vocab=[("tesis", "idea central que se defiende"), ("razón", "motivo que apoya una tesis"), ("supuesto", "idea previa, a veces no dicha, sobre la que se apoya un razonamiento"), ("principio de caridad", "reconstruir la versión más fuerte de una postura antes de criticarla"), ("reconstruir", "explicar con palabras propias tesis y razones sin deformarlas"), ("contractualismo", "idea de que la autoridad se explica por un acuerdo para vivir en común")],
    worked=[
        ("Reconstruir el Texto A", "Reconstruye la perspectiva del Texto A de la ficha en tres partes.",
         ["Tesis: conviene ceder parte de la libertad a una autoridad que dé seguridad.", "Razón: sin reglas y sin quien las haga cumplir, las personas desconfían y viven con temor."],
         "Tesis: ceder libertad por seguridad. Razón: sin reglas hay desconfianza y temor. Supuesto: sin una autoridad, las personas tienden a desconfiar"),
        ("Distinguir crítica de ataque", "Alguien responde al Texto B: «Quien escribió eso es ingenuo». ¿Es una crítica a la tesis?",
         ["Busco si la respuesta menciona la tesis o las razones del texto.", "Habla de la persona («ingenuo») y no discute que la autoridad legítima nazca del acuerdo libre."],
         "No: ataca a la persona y no la tesis"),
    ],
    mistakes=[("Atacar a la persona o al autor en vez de discutir su tesis.", "Se evita examinar las razones y se pasa al terreno personal.", "Reformula la tesis con caridad y discute sus razones."),
              ("Reconstruir un texto con las propias ideas y atribuirle lo que no dice.", "Se mezcla lo que dice el texto con lo que uno piensa.", "Separa «el texto sostiene…» de «yo pienso…» y vuelve al texto para comprobar cada afirmación.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis del Texto B?", "Una autoridad es legítima solo si nace del acuerdo libre de quienes la integran y estos pueden corregirla", "Conviene ceder parte de la libertad a una autoridad que garantice la seguridad", "Las personas viven con temor cuando no hay reglas comunes", "Es la idea central que defiende el Texto B; las otras opciones pertenecen al Texto A."),
        ("abc", "{F} ¿Qué supuesto sobre el ser humano se apoya el Texto B?", "Las personas pueden cooperar cuando se reconocen como iguales", "Las personas solo obedecen si sienten temor", "Las personas no necesitan ponerse de acuerdo", "El Texto B parte de que quienes se reconocen como iguales cooperan."),
        ("abc", "{F} Quienes obedecen quieren poder cambiar las decisiones de la autoridad. ¿Qué texto lo permite como condición de legitimidad?", "El Texto B, porque exige que quienes la integran puedan corregirla", "El Texto A, porque garantiza seguridad a todos", "Ninguno, porque ambos defienden obedecer sin condiciones", "Solo el Texto B menciona la posibilidad de corregir la autoridad."),
        ("abc", "Según la explicación, ¿qué es un supuesto sobre el ser humano?", "Una idea previa sobre cómo son las personas, sobre la que se apoya la conclusión", "Un dato de una encuesta", "La opinión de quien lee el texto", "El supuesto es la imagen de las personas que sostiene, a veces sin decirlo, un razonamiento político."),
        ("abc", "{F} Un estudiante dice que el Texto A sostiene que las personas son malas por naturaleza. ¿Por qué es una reconstrucción exagerada?", "El texto solo habla de desconfianza y temor cuando faltan reglas y quien las haga cumplir, no de maldad natural", "Porque el texto dice que las personas son buenas", "Porque el texto no menciona a las personas", "Debe mantenerse lo que el texto dice; añadir «maldad natural» deforma la tesis."),
        ("ab", "{F} ¿Qué diferencia principal hay entre los textos A y B sobre qué da legitimidad?", "A destaca la seguridad que garantiza la autoridad y B el acuerdo libre y la corrección posible", "A y B dicen lo mismo con otras palabras", "A pone el acento en la seguridad; B en el acuerdo libre y el control de quienes obedecen."),
        ("abc", "Un estudiante resume el Texto A diciendo: «El texto dice que la gente es mala y que hay que obedecer a cualquiera». ¿Qué defecto tiene la reconstrucción?", "Deforma la tesis: el texto habla de desconfianza y de una autoridad que garantice la seguridad, no de obedecer a cualquiera", "Es correcta, porque resume la idea", "Es incompleta, porque no cita ninguna ley", "Atribuye al texto cosas que no dice, y la reconstrucción debe ser fiel."),
        ("abc", "Una estudiante responde al Texto B: «Esa idea no vale porque quien la escribió nunca ha gobernado». ¿Qué error comete?", "Ataca a la persona y no la tesis", "Reconstruye con caridad la tesis", "Presenta una objeción a las razones", "No discute si la autoridad legítima nace del acuerdo; se refiere a quien escribe."),
        ("abc", "{F} Aplica el principio de caridad al Texto A. ¿Cuál es la reconstrucción más fuerte?", "Quien vive sin reglas ni quien las haga cumplir tiene razones para temer, y por eso sería razonable ceder parte de la libertad a cambio de seguridad", "El Texto A quiere que nadie sea libre", "El Texto A solo busca que unos manden sobre otros", "La versión caritativa recoge la razón del texto; las otras opciones la deforman."),
        ("{F} Compara los supuestos de A y de B. ¿Qué imagen de las personas parece haber detrás de cada texto?", "A: sin autoridad tienden a desconfiar; B: son capaces de cooperar si se reconocen como iguales", "Se ve en la razón de cada texto: temor sin reglas en A y cooperación entre iguales en B."),
        ("abc", "{F} Si el Texto B tuviera razón, ¿qué debería poder hacer una autoridad legítima respecto de sus integrantes?", "Aceptar que estos la corrijan", "Impedir cualquier cambio", "Decidir sin escuchar a nadie", "El texto condiciona la legitimidad a que quienes la integran puedan corregirla."),
        ("abc", "Reconstruir una perspectiva y estar de acuerdo con ella son cosas…", "Distintas: se puede reconstruir con fidelidad una postura que se rechaza", "La misma, porque no se puede explicar lo que no se comparte", "Opuestas, porque quien reconstruye debe criticarla", "Reconstruir es comprender con fidelidad; evaluar viene después."),
        ("abc", "{F} Quien lee A y B concluye: «Ambos hablan de la misma pregunta: por qué es legítima una autoridad». ¿Es correcto?", "Sí: A y B responden de manera distinta por qué conviene o es legítima una autoridad", "No: A trata de seguridad y B de un tema sin relación", "No: ninguno habla de autoridad", "Ambos ofrecen una justificación de la autoridad, con razones distintas."),
    ],
    ctx=("abc", "En un taller de filosofía, un grupo debe reconstruir una postura sobre las reglas de una biblioteca barrial ficticia: «Las reglas deben decidirlas todos los usuarios, porque quienes las cumplen deben poder discutirlas». ¿Cuál es la tesis?", "Las reglas deben ser decididas por todos los usuarios", "Las bibliotecas no necesitan reglas", "Los bibliotecarios no saben de reglas", "La tesis es la idea que se defiende; la razón es que quienes cumplen las reglas deben poder discutirlas."),
    sc=[
        ("En Filosofía política: ¿qué es el principio de caridad?", "Reconstruir la versión más fuerte de una postura antes de criticarla", "Evita atacar una versión deformada de la tesis."),
        ("¿Qué tres partes tiene una reconstrucción?", "Tesis, razones y supuesto sobre el ser humano", "Son los tres elementos que se buscaron en los textos de la ficha."),
        ("¿Por qué «es un ingenuo» no es una crítica a la tesis?", "Porque habla de la persona y no de las razones", "Una crítica examina las razones, no a quien las sostiene."),
    ],
    op=("Lee este texto de ejemplo (no es cita de ningún autor): «Una sociedad es más justa cuando quienes toman decisiones deben explicar sus razones a los demás, porque nadie puede ser obligado por motivos que no conoce». "
        "Reconstruye su perspectiva en tres partes: tesis, razón y supuesto sobre el ser humano. Luego escribe una objeción respetuosa dirigida a la tesis y no a la persona.",
        "Tesis: los que deciden deben explicar sus razones. Razón: nadie puede ser obligado por motivos que no conoce. Supuesto: las personas merecen comprender las razones de lo que se les exige. Objeción: explicar todo puede retrasar decisiones urgentes.",
        ["la tesis y la razón se distinguen sin mezclarse", "el supuesto sobre las personas está formulado", "la reconstrucción no agrega ideas que el texto no tiene", "la objeción se dirige a la tesis y no a la persona"],
        ["reconstrucción en tres partes y una objeción"],
        ["resumir sin separar tesis y razón", "atribuir al texto ideas propias", "criticar al autor en vez de la tesis"],
        "Pregunta: «¿dónde dice el texto eso que atribuyes?». Pídele que lo señale."),
    reinforce="Reconstruye en tres líneas una postura con la que no estés de acuerdo, tal como la defendería alguien que sí lo está.",
    extend="Escribe una versión alternativa del Texto A cambiando el supuesto sobre el ser humano, y anota qué conclusión política cambiaría.",
)

# ============================================================ OAC-01, clase 4
F = ("Ficha 4 (de ejemplo). Hipótesis H: «Una autoridad no es legítima solo porque logra obediencia». "
     "Argumento de apoyo: P1: Si lograr obediencia bastara para ser legítima, entonces una autoridad que gobierna por el miedo sería legítima. "
     "P2: Una autoridad que gobierna por el miedo no es legítima. C: Lograr obediencia no basta para ser legítima.")
build(
    O1, 4, F,
    use="Aprenderé a formular una hipótesis como argumento con premisas y conclusión y a evaluarla con un método propio de la filosofía.",
    prior=["Sé reconstruir una tesis y una razón.", "Sé buscar un contraejemplo.", "Distingo atacar una tesis de atacar a una persona."],
    explain=[
        "Un argumento es un conjunto de afirmaciones donde unas, las premisas, buscan apoyar otra, la conclusión. La hipótesis que se defiende suele ser la conclusión. Evaluar un argumento exige preguntar dos cosas: si las premisas son aceptables y si realmente apoyan la conclusión. Se puede formular una hipótesis con la estructura «si… entonces…», que ayuda a ver qué se está afirmando.",
        "La filosofía política dispone de métodos para examinar hipótesis. El análisis conceptual aclara qué significan los términos. El experimento mental imagina una situación posible para probar una idea. El contraste de casos compara situaciones parecidas con resultados distintos para ver qué factor importa. La reconstrucción argumentativa ordena premisas y conclusión para evaluarlas.",
        "Una buena evaluación considera además una objeción posible: una razón que cuestiona una premisa o la conclusión. Responder la objeción fortalece o corrige la hipótesis. Quien formula una hipótesis debe estar dispuesto a revisarla si encuentra una objeción fuerte.",
    ],
    vocab=[("argumento", "conjunto de premisas que buscan apoyar una conclusión"), ("premisa", "afirmación que apoya la conclusión"), ("conclusión", "afirmación que el argumento busca establecer"), ("análisis conceptual", "método que aclara qué significan los términos"), ("experimento mental", "situación imaginada para probar una idea"), ("objeción", "razón que cuestiona una premisa o la conclusión")],
    worked=[
        ("Identificar premisas y conclusión", "En el argumento de la ficha, ¿cuál es la conclusión y cuál la segunda premisa?",
         ["La conclusión es lo que se quiere establecer y aparece al final: lograr obediencia no basta.", "La segunda premisa dice que quien gobierna por el miedo no es legítimo."],
         "Conclusión: lograr obediencia no basta para ser legítima. P2: gobernar por el miedo no es legítimo"),
        ("Elegir un método", "Un grupo imagina un pueblo gobernado por el miedo donde todos obedecen y pregunta si esa autoridad es legítima. ¿Qué método usa?",
         ["Veo que el grupo imagina una situación posible para probar una idea.", "No compara casos reales ni aclara una palabra."],
         "Un experimento mental"),
    ],
    mistakes=[("Creer que un argumento es fuerte solo porque suena convincente.", "Se evalúa el efecto retórico y no las premisas.", "Pregunta siempre si las premisas son aceptables y si apoyan de verdad la conclusión."),
              ("Dar por válida una hipótesis sin buscar ninguna objeción.", "Se confunde estar convencido con haber examinado.", "Formula la mejor objeción posible y respóndela o corrige la hipótesis.")],
    T=[
        ("abc", "Según la explicación, ¿qué es una premisa?", "Una afirmación que apoya la conclusión", "La afirmación final que se quiere establecer", "Una opinión que no necesita razones", "Las premisas son los apoyos del argumento; la conclusión es lo que ellas respaldan."),
        ("abc", "Lee este argumento ficticio: «Todo reglamento debe poder corregirse. El reglamento del club no puede corregirse. Por lo tanto, el reglamento del club debe cambiar.» ¿Cuál es la conclusión?", "El reglamento del club debe cambiar", "Todo reglamento debe poder corregirse", "El reglamento del club no puede corregirse", "La conclusión es la afirmación final que las dos premisas buscan apoyar."),
        ("abc", "¿Qué método consiste en aclarar qué significan los términos de una hipótesis?", "Análisis conceptual", "Experimento mental", "Contraste de casos", "Aclarar el significado de los términos es lo propio del análisis conceptual."),
        ("abc", "{F} ¿Cuál es la premisa P1?", "Si lograr obediencia bastara para ser legítima, una autoridad que gobierna por el miedo sería legítima", "Una autoridad que gobierna por el miedo no es legítima", "Lograr obediencia no basta para ser legítima", "P1 es la primera afirmación de apoyo, una condición del tipo «si… entonces…»."),
        ("abc", "Un grupo compara dos clubes ficticios: uno decide por votación y otro por orden del presidente, y ve cuál tiene menos conflictos. ¿Qué método usa?", "Contraste de casos", "Experimento mental", "Análisis conceptual", "Compara casos parecidos con resultados distintos para ver qué factor importa."),
        ("abc", "Un grupo se pregunta: «¿Qué entendemos por obediencia: cumplir por miedo o cumplir por convicción?». ¿Qué método usa?", "Análisis conceptual", "Contraste de casos", "Experimento mental", "Busca precisar el significado de un término clave."),
        ("abc", "{F} ¿Qué objeción cuestionaría la premisa P2?", "Hay quienes sostienen que una autoridad temida puede ser legítima si protege a su gente", "El argumento no cita ninguna ley vigente", "Las dos premisas aparecen en orden inverso", "Una objeción pertinente ataca la premisa, en este caso la idea de que gobernar por el miedo nunca sea legítimo."),
        ("abc", "{F} Si alguien dice «H es falsa porque quien la propone es muy joven», ¿qué error comete?", "No discute las premisas ni la conclusión, sino a la persona", "Responde con una objeción a la premisa P1", "Propone un experimento mental", "Una evaluación debe examinar premisas y apoyo, no la edad de quien habla."),
        ("abc", "¿Cuál de estas frases formula mejor una hipótesis sobre las reglas de una comunidad ficticia?", "Una comunidad es más estable cuando sus reglas pueden ser discutidas por quienes las cumplen, porque así las sienten propias", "Las reglas de una comunidad son importantes para todos", "Las reglas de esta comunidad no me parecen bien", "Solo la primera tiene una afirmación concreta y una razón que se puede examinar."),
        ("abc", "{F} Un estudiante dice que el argumento no apoya la conclusión porque la conclusión no se sigue de P1 y P2. ¿Qué está evaluando?", "El apoyo de las premisas a la conclusión", "La aceptabilidad de P2", "La verdad de la conclusión en el mundo real", "Evalúa si, aun siendo aceptables, las premisas realmente apoyan la conclusión."),
        ("abc", "Para responder una objeción fuerte a su hipótesis, una estudiante debe…", "Revisar la hipótesis o explicar por qué la objeción no la afecta", "Ignorarla, porque la hipótesis ya es suya", "Repetir la hipótesis con más fuerza", "Responder una objeción es parte de evaluar; la hipótesis puede ajustarse."),
        ("abc", "En un experimento mental alguien imagina un pueblo donde nadie puede salir ni opinar y pregunta si la autoridad es legítima. ¿Qué ventaja tiene el método?", "Permite probar una idea en una situación que no se puede observar en la realidad", "Reemplaza cualquier dato", "Demuestra por sí solo que la idea es verdadera", "Su fuerza es aislar un factor imaginando una situación; no reemplaza la evaluación posterior."),
        ("abc", "{F} Se agrega la premisa P3: «Algunas autoridades temidas son obedecidas por todos». ¿Ayuda a apoyar la conclusión?", "No directamente: dice que hay obediencia pero no que sea legítima", "Sí, porque muestra que lograr obediencia es suficiente", "Sí, porque reemplaza a P2", "Que se obedezca no dice nada sobre la legitimidad; hace falta una premisa sobre ella."),
    ],
    ctx=("abc", "Un consejo de curso ficticio quiere decidir cómo escoger el tema de la jornada anual. Un grupo propone: «Lo mejor es que decidan todos, porque nadie debería cumplir un acuerdo en el que no pudo opinar». ¿Cuál es la premisa y cuál la conclusión?", "Premisa: nadie debería cumplir un acuerdo en el que no pudo opinar; conclusión: que decidan todos", "Premisa: que decidan todos; conclusión: nadie debería cumplir un acuerdo", "No hay premisa, solo una opinión", "La razón es la premisa, y lo que se defiende (que decidan todos) es la conclusión."),
    sc=[
        ("En Filosofía política: ¿qué es un experimento mental?", "Una situación imaginada para probar una idea", "Se usa cuando no se puede observar el caso en la realidad."),
        ("¿Qué dos cosas se preguntan al evaluar un argumento?", "Si las premisas son aceptables y si apoyan la conclusión", "Son los dos requisitos de un buen argumento."),
        ("¿Para qué sirve formular una objeción a la propia hipótesis?", "Para ponerla a prueba y corregirla si hace falta", "Quien examina una hipótesis debe considerar razones en contra."),
    ],
    op=("Elige una hipótesis: (1) «Una norma es justa solo si quienes la cumplen pudieron discutirla». (2) «Una regla de convivencia es buena si todos entienden su razón». "
        "Escríbela como argumento con dos premisas y una conclusión, indica qué método usarías para examinarla y escribe una objeción.",
        "Hipótesis 1. P1: Quien cumple una norma no discutida está obligado sin haber podido opinar. P2: Estar obligado sin poder opinar es injusto. C: Una norma es justa solo si pudo ser discutida. Método: contraste de casos entre grupos que discuten y grupos que no. Objeción: en emergencias no hay tiempo de discutir.",
        ["separa dos premisas y una conclusión", "las premisas apoyan la conclusión", "nombra un método propio de la filosofía", "formula una objeción pertinente"],
        ["argumento con premisas, método y objeción"],
        ["escribir premisas que repiten la conclusión", "confundir método con tema", "formular una objeción que ataca a la persona"],
        "Pregunta: «si aceptara tus dos premisas, ¿tendría que aceptar tu conclusión?». Pídele que lo compruebe."),
    reinforce="Toma una frase que hayas oído en una discusión y reescríbela como dos premisas y una conclusión.",
    extend="Escribe una segunda objeción a tu hipótesis, más fuerte que la primera, y una respuesta posible.",
)

# ============================================================ OAC-02, clase 1
F = ("Ficha 5 (casos ficticios). Escena 1: el directorio de una cooperativa de agua de «Valle Seco» (no existe) decide cobrar una cuota extra sin consultar a las socias y socios. "
     "Escena 2: en un trabajo grupal de un curso, una compañera elige siempre el tema y las demás no objetan para evitar conflictos. "
     "Escena 3: una junta de vecinos ficticia exige que cada decisión se anuncie en un panel con los motivos y se vote en asamblea.")
build(
    O2, 1, F,
    use="Aprenderé a reconocer relaciones de poder en instituciones y en la vida cotidiana y a plantear preguntas para evaluarlas desde el bien común.",
    prior=["Sé qué es el poder y la autoridad.", "Sé formular una pregunta filosófica.", "Distingo un hecho de una valoración."],
    explain=[
        "Una relación de poder existe cuando una persona o grupo puede influir en lo que otras personas hacen o pueden hacer. El poder aparece en las instituciones (reglas, cargos y procedimientos, como una cooperativa o un reglamento) y también en la vida cotidiana (un grupo de trabajo, una conversación, una costumbre). Detectarlo no significa que sea injusto: muchas relaciones de poder son necesarias y se pueden justificar.",
        "Para evaluarlas desde el bien común, es decir, desde lo que permite que todas las personas de la comunidad vivan bien, se pueden hacer preguntas guía. ¿Quién decide y con qué derecho? ¿Quién resulta afectado y puede opinar? ¿Se explican las razones? ¿Puede corregirse la decisión? ¿A quién beneficia?",
        "Estas preguntas ayudan a problematizar cada situación y a evitar dos errores: pensar que todo poder es malo o que todo poder es natural y no se puede discutir. Filosofar sobre el poder es examinar sus razones, no dejarlo pasar como si fuera invisible.",
    ],
    vocab=[("relación de poder", "situación en que alguien puede influir en lo que otros hacen o pueden hacer"), ("institución", "conjunto de reglas, cargos y procedimientos que organizan una actividad"), ("vida cotidiana", "situaciones habituales de la convivencia en grupos"), ("bien común", "condiciones que permiten que todas las personas de la comunidad vivan bien"), ("rendir cuentas", "explicar a los demás las razones y resultados de lo que se decide"), ("afectado", "persona a quien la decisión le cambia opciones o condiciones")],
    worked=[
        ("Detectar el poder", "En la Escena 2 de la ficha, ¿quién ejerce poder y cómo?",
         ["La compañera decide el tema siempre.", "Las demás no objetan por evitar conflictos: eso mantiene el poder aunque nadie lo imponga con fuerza."],
         "La compañera que elige el tema ejerce poder cotidiano sobre el grupo, que lo acepta para evitar conflictos"),
        ("Formular preguntas guía", "Para evaluar la Escena 1 desde el bien común, ¿qué preguntas conviene hacer?",
         ["Identifico quién decide: el directorio.", "Identifico quiénes son afectados y si pudieron opinar: las socias y socios, que no fueron consultados."],
         "¿Con qué derecho cobra el directorio? ¿Por qué no consultó a las socias y socios afectados? ¿Cómo se explica la cuota?"),
    ],
    mistakes=[("Pensar que toda relación de poder es injusta.", "Se confunde detectar el poder con condenarlo.", "Evalúa con preguntas: quién decide, con qué derecho, a quién afecta y si puede corregirse."),
              ("Decir que en la vida cotidiana no hay poder, porque solo existe en el Estado.", "Se olvida que las decisiones de grupos pequeños también limitan lo que otros hacen.", "Revisa en grupos pequeños quién decide y si los demás pueden opinar.")],
    T=[
        ("abc", "Según la explicación, ¿qué es una relación de poder?", "Una situación en que alguien puede influir en lo que otros hacen o pueden hacer", "Cualquier desacuerdo entre dos grupos", "El cargo que figura en un organigrama", "Lo central es la capacidad de influir en lo que otros pueden hacer."),
        ("abc", "{F} ¿Cuál de las escenas muestra a una institución ejerciendo poder sin consultar a quienes resultan afectados?", "La Escena 1, donde un directorio fija una cuota", "La Escena 2, donde una compañera elige el tema", "La Escena 3, donde se anuncian los motivos y se vota en asamblea", "Un directorio de cooperativa es una institución con cargos y procedimientos."),
        ("abc", "{F} ¿Cuál de las escenas muestra poder en la vida cotidiana?", "La Escena 2, el trabajo grupal", "La Escena 1, la cooperativa", "La Escena 3, la asamblea", "Un trabajo grupal es una situación habitual de convivencia, no una institución formal."),
        ("abc", "¿Qué significa «rendir cuentas»?", "Explicar a los demás las razones y los resultados de lo que se decide", "Cobrar una cuota", "Votar en secreto", "Rendir cuentas es dar razones y resultados a quienes se ven afectados."),
        ("abc", "{F} ¿Qué escena muestra un ejemplo de procedimiento que facilita rendir cuentas?", "La Escena 3, con panel de motivos y votación en asamblea", "La Escena 1, sin consulta", "La Escena 2, sin objeciones", "El panel con motivos y la asamblea permiten explicar y discutir las decisiones."),
        ("ab", "¿Detectar una relación de poder significa que es injusta?", "No: hay relaciones de poder necesarias y justificables que se evalúan con razones", "Sí: todo poder es injusto por definición", "Detectar es solo el primer paso; la evaluación exige razones sobre su justificación."),
        ("abc", "{F} Una socia dice: «Como el directorio tiene cargo, sus decisiones no necesitan revisión». ¿Qué pregunta guía muestra el límite de ese argumento?", "¿Puede corregirse la decisión si resulta injusta para quienes la sufren?", "¿Cuántos cargos tiene el directorio?", "¿Cuánto dinero se recaudaría con la cuota?", "Tener un cargo no responde por sí solo si la decisión puede ser revisada por los afectados."),
        ("abc", "En un centro de estudiantes ficticio, el presidente decide solo el calendario de actividades y no explica por qué. ¿Qué pregunta guía no se está cumpliendo?", "¿Se explican las razones de la decisión?", "¿Cuántas actividades incluye el calendario?", "¿Cuántos estudiantes hay en el liceo?", "Falta el rendimiento de cuentas: nadie conoce las razones."),
        ("abc", "Un equipo ficticio de trabajo reparte tareas según quién habla más fuerte. ¿Qué tipo de relación de poder aparece?", "Una cotidiana, informal, que influye en lo que los demás pueden hacer", "Una institucional, con reglamento", "Ninguna, porque nadie tiene un cargo", "No hay cargo, pero el equipo concentra decisiones en quien habla más fuerte."),
        ("{F} Según la Escena 2, ¿por qué el silencio de las demás ayuda a mantener el poder de la compañera?", "Porque al no objetar, la decisión no se discute y el poder se sostiene", "Si nadie reclama, su decisión no se pone a prueba y sigue funcionando."),
        ("abc", "Alguien dice: «El poder siempre es malo». ¿Cuál es la mejor respuesta filosófica?", "Pedir razones: algunas relaciones de poder pueden justificarse y otras no, según quién decide, a quién afecta y si se rinden cuentas", "Aceptar la frase, porque es evidente", "Responder que el poder siempre es bueno", "La evaluación exige criterios, no etiquetas generales."),
        ("abc", "¿Cuál de las siguientes preguntas ayuda a evaluar una decisión desde el bien común?", "¿Beneficia a todas las personas de la comunidad o solo a una parte?", "¿Qué opción es más barata de ejecutar?", "¿Quién propuso primero la idea?", "El bien común pregunta por los beneficios y afectaciones para toda la comunidad."),
        ("abc", "{F} Si en la Escena 1 el directorio explicara públicamente las razones y permitiera votar la cuota, ¿qué cambiaría?", "Mejorarían la participación y la rendición de cuentas, aunque el poder del directorio seguiría existiendo", "Desaparecería todo poder", "La cuota dejaría de existir", "El poder no desaparece, pero se justifica y puede corregirse."),
    ],
    ctx=("abc", "Un club deportivo ficticio decide cerrar el gimnasio a los estudiantes por la tarde sin consultarles. ¿Qué pregunta guía revela mejor el problema?", "¿Pudieron opinar quienes resultan afectados por la decisión?", "¿Cuántas horas a la semana está abierto el gimnasio?", "¿Quién administra el club?", "La pregunta por la participación de los afectados se centra en el poder y la decisión."),
    sc=[
        ("En Filosofía política: ¿qué es el bien común?", "Las condiciones que permiten que todas las personas de la comunidad vivan bien", "No es la suma de intereses personales ni el interés de una mayoría."),
        ("¿Dónde aparece el poder además de en el Estado?", "En instituciones y en la vida cotidiana, como los grupos de trabajo", "El poder está en toda situación en que alguien influye en lo que otros pueden hacer."),
        ("Nombra dos preguntas guía para evaluar una relación de poder.", "¿Quién decide y con qué derecho? ¿Se explican las razones? (u otras de la explicación)", "Son preguntas de la clase para evaluar el poder desde el bien común."),
    ],
    op=("Elige una situación ficticia: (1) un equipo de curso en que un compañero decide siempre el reparto de tareas; (2) una junta de vecinos que cambia sin avisar el horario de uso de la sede. "
        "Describe quién ejerce poder y sobre quién, escribe tres preguntas guía para evaluar la situación desde el bien común y formula una hipótesis sobre si es justificable.",
        "Situación 2. Ejerce poder la directiva sobre quienes usan la sede. Preguntas: ¿Con qué derecho cambia el horario? ¿Pudieron opinar los afectados? ¿Se explicaron las razones? Hipótesis: el cambio es justificable solo si se avisó con anticipación y se explicaron los motivos.",
        ["identifica quién ejerce poder y sobre quién", "escribe tres preguntas guía pertinentes", "formula una hipótesis con una razón", "no condena ni justifica por defecto"],
        ["descripción, tres preguntas y una hipótesis"],
        ["decir que toda relación de poder es injusta", "describir la situación sin preguntar por los afectados", "dar una opinión sin razón"],
        "Pregunta: «¿qué preguntas guía permitirían a otras personas evaluar tu situación?». Pídele que las escriba."),
    reinforce="Observa una decisión de tu entorno (horario, regla, reparto) y anota quién decide, quién se ve afectado y si se explican las razones.",
    extend="Compara por escrito una decisión institucional y una cotidiana: ¿en cuál es más fácil pedir razones y por qué?",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 6 (casos ficticios). Caso 1: una comunidad de «Cerro Alto» (no existe) debe decidir si construye una sede para todas las agrupaciones o una cancha para el club más numeroso. "
     "Caso 2: un colegio ficticio decide adelantar el inicio de clases para que un grupo de estudiantes tenga más horas de taller, aunque a otros les complica el transporte. "
     "Caso 3: un sindicato ficticio logra una mejora para sus socios que no cambia las condiciones del resto de las personas trabajadoras.")
build(
    O2, 2, F,
    use="Aprenderé a distinguir bien común, interés particular e interés de una mayoría, y poder para dominar de poder para actuar juntos.",
    prior=["Sé qué es una relación de poder.", "Sé definir con rasgos y buscar contraejemplos.", "Sé qué es la legitimidad."],
    explain=[
        "El bien común son las condiciones de la vida en común que permiten que todas las personas de una comunidad vivan bien y puedan desarrollarse. No es la suma de los deseos de cada persona ni lo que quiere la mayoría. El interés particular es lo que conviene a una persona o a un grupo determinado, y puede ser legítimo, pero no equivale al bien común.",
        "Se distinguen dos modos de entender el poder. Una postura asociada con el sociólogo Max Weber lo entiende como la probabilidad de imponer la propia voluntad aun contra la resistencia de otros. Otra postura, asociada con la filósofa Hannah Arendt, lo entiende como la capacidad de actuar en conjunto, que nace cuando las personas se reúnen y deciden algo común. La primera destaca el mando; la segunda, la acción conjunta.",
        "Dominación es el poder ejercido sin justificación aceptable para quienes lo sufren. Rendición de cuentas y participación son criterios para saber si el poder busca el bien común: quienes deciden explican sus razones, y los afectados pueden opinar y corregir. Un mismo acto puede ser interés particular en un caso y bien común en otro: depende de a quién beneficia y a quién deja fuera.",
    ],
    vocab=[("bien común", "condiciones de la vida en común que permiten a todas las personas vivir bien"), ("interés particular", "lo que conviene a una persona o grupo determinado"), ("poder como imposición", "probabilidad de imponer la propia voluntad aun contra la resistencia"), ("poder como acción conjunta", "capacidad de actuar en común cuando las personas se reúnen"), ("dominación", "poder ejercido sin justificación aceptable para quienes lo sufren"), ("participación", "posibilidad de opinar y decidir quienes se ven afectados")],
    worked=[
        ("Bien común o interés particular", "En el Caso 3 de la ficha, un sindicato mejora las condiciones solo para sus socios. ¿Es bien común o interés particular?",
         ["Pregunto a quién beneficia: a los socios del sindicato.", "Pregunto si cambia las condiciones de todas las personas: no."],
         "Es un interés particular, que puede ser legítimo pero no equivale al bien común"),
        ("Distinguir dos modos de entender el poder", "Un vecino dice: «La junta tiene poder porque logra que todos hagan lo que decide». Otra vecina dice: «Tiene poder porque todos se reunieron y decidieron juntos». ¿Qué postura expresa cada uno?",
         ["Él destaca imponer una decisión a otros: poder como mando.", "Ella destaca el actuar en conjunto: poder como acción común."],
         "El vecino expresa el poder como imposición y la vecina el poder como acción conjunta"),
    ],
    mistakes=[("Creer que bien común es lo que quiere la mayoría.", "Se confunde un número de votos con las condiciones que permiten vivir bien a todas las personas.", "Pregunta si la decisión protege las condiciones de vida de todas y todos, incluidas las minorías."),
              ("Pensar que un interés particular es siempre injusto.", "Se mezcla lo particular con lo ilegítimo.", "Evalúa si el interés particular respeta a los demás y no daña el bien común.")],
    T=[
        ("abc", "Según la explicación, ¿qué es el bien común?", "Las condiciones de la vida en común que permiten a todas las personas vivir bien", "Lo que desea la mayoría en una votación", "La suma de los gustos de cada persona", "Es la condición compartida que alcanza a todas las personas, no una cantidad de votos."),
        ("abc", "¿Qué es un interés particular?", "Lo que conviene a una persona o a un grupo determinado", "Lo que beneficia a toda la comunidad", "Una norma obligatoria", "Es una conveniencia de alguien en concreto, que puede ser legítima o no."),
        ("abc", "La postura asociada con Max Weber entiende el poder como…", "La probabilidad de imponer la propia voluntad aun contra la resistencia", "La capacidad de actuar en conjunto", "El cargo que se ocupa", "Así lo define la explicación para esa postura."),
        ("abc", "La postura asociada con Hannah Arendt entiende el poder como…", "La capacidad de actuar en conjunto cuando las personas se reúnen", "La capacidad de imponer una voluntad", "La fuerza física", "Destaca la acción común de las personas reunidas."),
        ("abc", "{F} En el Caso 1, ¿qué opción se acerca más al bien común si la comunidad busca servir a todas las agrupaciones?", "La sede para todas las agrupaciones", "La cancha solo para el club más numeroso", "Ninguna de las dos", "La sede sirve a todas las agrupaciones, no solo a una."),
        ("abc", "{F} En el Caso 2, ¿cuál es el interés particular y cuál el costo para otros?", "El interés del grupo de taller, con costo para quienes dependen del transporte", "El interés de todo el colegio, sin costo para nadie", "No hay interés particular, porque nadie se beneficia", "El taller beneficia a un grupo y el transporte complica a otros."),
        ("ab", "¿Es lo mismo bien común que lo que quiere la mayoría?", "No: el bien común considera las condiciones de todas las personas, incluidas las minorías", "Sí: el bien común es lo que decide la mayoría", "Una mayoría puede decidir algo que perjudique a una minoría, y eso no sería bien común."),
        ("abc", "{F} ¿Cómo podría el Caso 3 acercarse al bien común sin renunciar a la mejora de los socios?", "Buscando que la mejora se extienda a otras personas trabajadoras", "Eliminando la mejora", "Ocultándola al resto", "Ampliar el beneficio a más personas lo acerca a las condiciones de todos."),
        ("abc", "Un entrenador ficticio dice: «Aquí se hace lo que yo digo, quiera o no el equipo». ¿Qué postura expresa?", "Poder como imposición", "Poder como acción conjunta", "Ninguna, porque habla de obediencia", "Destaca el mando y la obediencia."),
        ("abc", "Una asamblea de estudiantes ficticia decide en conjunto organizar una campaña de reciclaje. ¿Qué postura describe mejor su poder?", "Poder como acción conjunta", "Poder como imposición", "Poder sin ningún sentido", "Las personas se reúnen y actúan en común."),
        ("abc", "¿Qué es la dominación según la explicación?", "Poder ejercido sin justificación aceptable para quienes lo sufren", "Cualquier poder", "Un poder que nace del acuerdo", "Se caracteriza porque los afectados no ven justificado ese poder."),
        ("abc", "Un directorio decide algo que conviene a sus propios miembros y deja a las demás personas sin opinión. ¿Qué criterios de la clase incumple?", "Participación y rendición de cuentas", "Ninguno, porque quien tiene el cargo puede decidir", "Solo la corrección, porque ya está tomada", "Los afectados no opinan ni reciben razones."),
        ("abc", "{F} Una estudiante afirma: «El Caso 2 es bien común porque los estudiantes del taller son felices». ¿Cuál es la mejor respuesta?", "La felicidad de un grupo no basta: hay que ver el efecto sobre quienes dependen del transporte", "Es correcta, porque la felicidad es lo central", "No, porque la felicidad no importa", "Debe considerar a todas las personas de la comunidad escolar."),
    ],
    ctx=("abc", "El municipio ficticio de «Costa Blanca» debe elegir entre arreglar una calle que usa todo el barrio o asfaltar el acceso de un club privado. ¿Cuál opción es más cercana al bien común?", "Arreglar la calle que usa todo el barrio", "Asfaltar el acceso del club privado", "Ninguna, porque cualquier gasto es particular", "La calle beneficia a toda la comunidad, y el acceso del club a un grupo concreto."),
    sc=[
        ("En Filosofía política: ¿qué es el interés particular?", "Lo que conviene a una persona o grupo determinado", "No es lo mismo que el bien común."),
        ("¿En qué se diferencian el poder como imposición y el poder como acción conjunta?", "El primero destaca imponer la voluntad y el segundo actuar en común", "Expresan dos modos de entender el poder."),
        ("¿Por qué el bien común no es lo que quiere la mayoría?", "Porque debe considerar las condiciones de todas las personas, incluidas las minorías", "Una mayoría puede perjudicar a una minoría."),
    ],
    op=("Elige uno de estos casos ficticios: (1) una comunidad debe decidir si usa un terreno vacío para una plaza abierta a todos o para un estacionamiento de un negocio; (2) un liceo debe decidir si reparte presupuesto solo entre los talleres más grandes o entre todos. "
        "Explica quién se beneficia y quién queda fuera, indica si hay bien común o interés particular y formula dos preguntas para decidir mejor.",
        "Caso 1. Se benefician quienes usan la plaza; con el estacionamiento, el negocio. La plaza abierta a todos se acerca al bien común; el estacionamiento es interés particular. Preguntas: ¿Quién queda sin acceso? ¿Se consultó a los vecinos?",
        ["identifica beneficiarios y personas que quedan fuera", "distingue bien común de interés particular", "no confunde bien común con voto de la mayoría", "formula dos preguntas útiles para decidir"],
        ["análisis breve de un caso con dos preguntas"],
        ["decir que bien común es lo que quiere la mayoría", "no nombrar a quienes quedan fuera", "dar una opinión sin criterio"],
        "Pregunta: «¿a quién deja fuera tu propuesta?». Pídele que lo considere antes de concluir."),
    reinforce="Escribe un ejemplo de tu comunidad donde un interés particular legítimo no sea contrario al bien común y otro donde sí lo sea.",
    extend="Explica con un ejemplo cómo una misma decisión puede mirarse como imposición o como acción conjunta, según quiénes participaron.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 7 (resúmenes de ejemplo escritos para este cuaderno). Tres perspectivas sobre el poder. "
     "Perspectiva 1 (asociada con Max Weber): el poder es la probabilidad de imponer la propia voluntad dentro de una relación, aun contra la resistencia. "
     "Perspectiva 2 (asociada con Hannah Arendt): el poder surge cuando las personas actúan de común acuerdo y desaparece cuando se dispersan. "
     "Perspectiva 3 (asociada con Michel Foucault): el poder no está solo en las instituciones, sino repartido en relaciones, normas y saberes que orientan lo que las personas hacen y consideran normal.")
build(
    O2, 3, F,
    use="Aprenderé a reconstruir tres perspectivas sobre el poder y a usarlas como lentes para evaluar casos de instituciones y de vida cotidiana.",
    prior=["Sé distinguir poder y autoridad.", "Sé qué es el bien común.", "Sé reconstruir tesis, razón y supuesto."],
    explain=[
        "Una perspectiva es una forma de mirar un fenómeno que destaca ciertos aspectos y deja otros en segundo plano. Las tres perspectivas de la ficha son resúmenes simplificados, no los libros completos de esos autores. Conviene usarlos como lentes: cada una hace visibles preguntas distintas.",
        "La perspectiva 1 pregunta quién impone su voluntad a quién y con qué recursos. La perspectiva 2 pregunta si las personas actúan juntas y cómo se sostiene esa acción. La perspectiva 3 pregunta qué normas y saberes hacen que ciertas conductas parezcan normales o inevitables, incluso en la vida cotidiana, donde nadie da órdenes explícitas.",
        "Elegir una perspectiva no es lo mismo que opinar sin razones: cada lente se justifica por lo que logra mostrar en un caso y por lo que deja sin explicar. Evaluar desde el bien común es preguntar qué ve cada lente respecto de las condiciones de vida de todas las personas.",
    ],
    vocab=[("perspectiva", "forma de mirar un fenómeno que destaca ciertos aspectos"), ("lente", "perspectiva usada para observar un caso"), ("imponer", "hacer que se cumpla la propia voluntad aun con resistencia"), ("acción conjunta", "actuar de común acuerdo entre varias personas"), ("norma social", "regla no escrita que orienta lo que se considera normal"), ("saber", "conjunto de ideas aceptadas como verdaderas en un grupo")],
    worked=[
        ("Aplicar una lente", "Caso ficticio: en un curso, todos dejan de reírse de ciertas bromas porque «así se hace aquí», sin que nadie lo ordene. ¿Qué perspectiva de la ficha lo ilumina mejor?",
         ["Veo que nadie ordena nada, pero hay una norma no escrita sobre lo normal.", "La perspectiva 3 se ocupa de normas y saberes que orientan lo que se considera normal."],
         "La perspectiva 3"),
        ("Qué deja sin explicar una lente", "Un compañero usa solo la perspectiva 1 para explicar cómo un curso organizó una campaña de reciclaje por acuerdo común. ¿Qué podría dejar sin ver?",
         ["La perspectiva 1 mira quién impone su voluntad.", "En el caso, lo central es que varias personas actuaron de común acuerdo, algo que ilumina mejor la perspectiva 2."],
         "Deja en segundo plano la acción conjunta, que muestra mejor la perspectiva 2"),
    ],
    mistakes=[("Atribuir a un autor ideas que están en un resumen simplificado como si fueran todo lo que pensó.", "Se confunde el resumen con la obra.", "Habla de «una perspectiva asociada con…» y señala que es un resumen de ejemplo."),
              ("Elegir una perspectiva porque «me cae bien» sin decir qué logra explicar.", "Se confunde perspectiva con opinión sin razones.", "Justifica la elección diciendo qué muestra y qué deja sin explicar la lente.")],
    T=[
        ("abc", "{F} ¿Qué pregunta hace visible la perspectiva 1?", "¿Quién impone su voluntad a quién y con qué recursos?", "¿Qué normas hacen parecer normales ciertas conductas?", "¿Cómo se sostiene la acción de personas reunidas?", "Su definición pone el acento en imponer la voluntad contra la resistencia."),
        ("abc", "{F} ¿Qué pregunta hace visible la perspectiva 2?", "¿Las personas actúan de común acuerdo y cómo se sostiene esa acción?", "¿Quién impone su voluntad?", "¿Qué saberes se consideran verdaderos?", "La perspectiva 2 destaca el actuar de común acuerdo."),
        ("abc", "{F} ¿Qué pregunta hace visible la perspectiva 3?", "¿Qué normas y saberes orientan lo que las personas consideran normal?", "¿Qué cargo ocupa cada persona?", "¿Quién ganó la votación?", "La perspectiva 3 destaca normas y saberes repartidos en relaciones."),
        ("abc", "Según la explicación, ¿qué es una lente en esta clase?", "Una perspectiva usada para observar un caso", "Una conclusión que no necesita razones", "Una opinión personal", "Se usa para ver aspectos distintos del mismo caso."),
        ("abc", "{F} En un taller de teatro ficticio, el director logra que todos cumplan su plan aunque algunos dudan. ¿Qué lente lo ilumina mejor?", "Perspectiva 1", "Perspectiva 2", "Perspectiva 3", "Destaca imponer la voluntad contra las dudas."),
        ("abc", "{F} Una cooperativa ficticia se dispersa y su campaña se debilita porque ya nadie participa. ¿Qué lente describe mejor lo ocurrido?", "Perspectiva 2, porque el poder desaparece cuando las personas se dispersan", "Perspectiva 1, porque nadie impuso nada", "Perspectiva 3, porque hubo una norma", "La perspectiva 2 sostiene que el poder desaparece cuando se dispersa la acción común."),
        ("abc", "{F} En un liceo ficticio, casi nadie levanta la mano para opinar porque se considera que «quien opina mucho busca destacar», aunque nadie lo dijo. ¿Qué lente ilumina mejor esa costumbre?", "Perspectiva 3", "Perspectiva 1", "Perspectiva 2", "Muestra cómo una norma no escrita orienta lo que se considera normal."),
        ("abc", "Una estudiante dice: «Usaré la perspectiva 1 porque me gusta más». ¿Qué falta en su justificación?", "Explicar qué logra mostrar la lente en el caso y qué deja sin explicar", "Elegir la lente más antigua", "Comprobar que la lente la haya propuesto un autor muy famoso", "Elegir una lente exige razones sobre su utilidad."),
        ("abc", "{F} ¿Qué puede ver la perspectiva 3 que la perspectiva 1 deja en segundo plano?", "Normas no escritas que orientan lo normal, sin que nadie dé una orden", "Quién da las órdenes", "El número de votos", "La perspectiva 3 se ocupa de relaciones, normas y saberes repartidos."),
        ("{F} Un grupo ficticio decide en conjunto un reglamento. ¿Qué dos lentes pueden complementarse para entender el caso y qué ve cada una?", "Perspectiva 2: la acción conjunta; perspectiva 3: las normas que ese reglamento instala como normales", "La acción conjunta crea el reglamento, y el reglamento orienta luego lo considerado normal."),
        ("abc", "Un periodista ficticio dice: «Según la perspectiva 1, el poder es siempre malo». ¿Es correcto?", "No: la perspectiva 1 describe cómo se impone una voluntad, sin decir que siempre sea malo", "Sí: el poder es solo mando", "Sí: toda imposición es injusta", "Es una descripción del poder, no una valoración automática."),
        ("abc", "Para evaluar un caso desde el bien común, ¿qué conviene hacer con las tres lentes?", "Preguntar qué ve cada una sobre las condiciones de vida de todas las personas", "Elegir la lente que más se parezca a mi opinión", "Usar siempre solo la primera", "El bien común guía la evaluación con cualquiera de las lentes."),
        ("abc", "{F} Si un reglamento escolar ficticio se aplica con castigos aunque muchos no lo comparten, ¿qué lente destaca esa característica?", "Perspectiva 1, por la imposición contra la resistencia", "Perspectiva 2, por la acción conjunta", "Ninguna", "Hay imposición de una voluntad aun cuando existe resistencia."),
    ],
    ctx=("abc", "Una radio comunitaria ficticia decide su programación en asamblea, pero con el tiempo todos los programas empiezan a parecerse porque nadie quiere salirse de lo habitual. ¿Qué lente ayuda a ver esto último?", "Perspectiva 3, por las normas que orientan lo considerado normal", "Perspectiva 1, por quién impone su voluntad", "Perspectiva 2, porque se acabó el acuerdo", "La repetición de lo normal sin órdenes explícitas la ilumina la perspectiva 3."),
    sc=[
        ("En Filosofía política: ¿qué es una perspectiva?", "Una forma de mirar un fenómeno que destaca ciertos aspectos", "No es una opinión sin razones: se justifica por lo que muestra."),
        ("¿Qué destaca la perspectiva asociada con Arendt en la ficha?", "La acción de personas que actúan de común acuerdo", "Es el centro de su definición del poder."),
        ("¿Por qué conviene decir «una perspectiva asociada con…»?", "Porque son resúmenes simplificados y no la obra completa", "Evita atribuir a un autor más de lo que sabemos."),
    ],
    op=("Elige un caso ficticio: (1) un grupo de curso decide en asamblea cambiar el horario de estudio, pero algunos se sienten presionados; (2) un club repite una costumbre que nadie recuerda por qué existe. "
        "Aplica dos de las tres perspectivas de la ficha: indica qué ve cada una, qué deja sin explicar y cuál usarías para evaluar el caso desde el bien común, con una razón.",
        "Caso 1. Perspectiva 2 ve la decisión en conjunto; perspectiva 1 ve la presión sobre algunos. La 2 deja sin ver la presión; la 1 deja sin ver el acuerdo. Usaría ambas porque el bien común exige que la acción conjunta no se vuelva imposición.",
        ["aplica correctamente dos perspectivas", "indica lo que cada una deja sin ver", "justifica la elección con una razón", "habla de perspectivas «asociadas con», no de obras completas"],
        ["aplicación de dos lentes con razones"],
        ["usar una lente sin explicar qué muestra", "tratar el resumen como la obra completa", "elegir por gusto"],
        "Pregunta: «¿qué ve tu lente que la otra no ve?». Pídele que lo escriba."),
    reinforce="Describe una costumbre de tu grupo que nadie ordenó y explica qué perspectiva la ilumina mejor.",
    extend="Elige una cuarta mirada posible sobre el poder (por ejemplo, el poder como protección de quienes dependen de otros) y explica qué preguntas haría visibles.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 8 (caso ficticio). El consejo de administración de un edificio de departamentos de «Parque Sur» (no existe) resolvió cerrar la sala común y destinarla a bodegas pagadas. "
     "Presidente del consejo: «Lo decidimos rápido para evitar discusiones y porque la mayoría de los miembros del consejo así lo quiso.» "
     "Residente A: «No se avisó y nadie explicó los motivos.» Residente B: «La sala servía a quienes no tienen otro lugar para juntarse.»")
build(
    O2, 4, F,
    use="Aprenderé a evaluar críticamente una relación de poder con cuatro criterios del bien común y a formular un argumento con ellos.",
    prior=["Sé la diferencia entre bien común e interés particular.", "Sé formular premisas y conclusión.", "Sé aplicar una perspectiva a un caso."],
    explain=[
        "Evaluar críticamente no es solo criticar: es juzgar con criterios y razones. Cuatro criterios ayudan a evaluar una relación de poder desde el bien común. Participación: ¿pudieron opinar quienes resultan afectados? Justificación pública: ¿se explicaron las razones de la decisión? Corrección: ¿existe forma de revisar o cambiar la decisión? Alcance: ¿a quién beneficia y a quién perjudica?",
        "Un argumento evaluativo tiene la forma «la decisión X es justificable/no justificable porque cumple/no cumple el criterio Y». Sus premisas incluyen un criterio (una regla general) y un hecho del caso. El criterio se defiende con razones y el hecho se comprueba con datos del enunciado. Rapidez y mayoría de votos no bastan por sí solos como justificación.",
        "Evaluar con criterios evita dos fallas: decidir por simpatía hacia las personas, y rechazar una decisión solo porque no nos favorece. Además, un mismo hecho puede evaluarse con más de un criterio y dar resultados distintos, lo que invita a ponderar.",
    ],
    vocab=[("criterio", "regla general que sirve para juzgar un caso"), ("participación", "posibilidad de opinar de quienes resultan afectados"), ("justificación pública", "explicar razones a quienes se ven afectados"), ("corrección", "posibilidad de revisar o cambiar una decisión"), ("alcance", "a quién beneficia y a quién perjudica una decisión"), ("ponderar", "comparar el peso de varios criterios")],
    worked=[
        ("Aplicar un criterio", "Con el criterio de justificación pública, evalúa la decisión del consejo en la ficha.",
         ["Pregunto si se explicaron las razones: el Residente A dice que no se avisó ni se explicó.", "El presidente solo alude a rapidez y mayoría del consejo, no a razones dirigidas a los afectados."],
         "No cumple el criterio de justificación pública"),
        ("Formular un argumento evaluativo", "Escribe un argumento con el criterio de alcance sobre la decisión del consejo.",
         ["Criterio: una decisión se justifica mejor si considera a quienes dependen del bien afectado.", "Hecho: la sala servía a quienes no tienen otro lugar para juntarse."],
         "Si una decisión debe considerar a quienes dependen del bien afectado y la sala servía a quienes no tienen otro lugar, entonces la decisión no cumplió con el alcance"),
    ],
    mistakes=[("Juzgar una decisión solo porque se tomó con rapidez o por mayoría, sin examinar criterios.", "Se confunde un procedimiento eficaz con una decisión justificada.", "Aplica los cuatro criterios y no te quedes con un solo rasgo."),
              ("Rechazar una decisión solo porque no me favorece.", "Se mezcla interés personal con evaluación.", "Evalúa la decisión con criterios que aceptarías aunque te favoreciera o no.")],
    T=[
        ("abc", "Según la explicación, ¿qué pregunta corresponde al criterio de participación?", "¿Pudieron opinar quienes resultan afectados?", "¿Cuánto cuesta la decisión?", "¿Cuántas personas votaron?", "La participación se refiere a la posibilidad de opinar de los afectados."),
        ("abc", "¿Qué pregunta corresponde al criterio de corrección?", "¿Existe forma de revisar o cambiar la decisión?", "¿Quién habló primero?", "¿Se tomó rápido?", "La corrección es la posibilidad de revisar o cambiar la decisión."),
        ("abc", "¿Qué pregunta corresponde al criterio de alcance?", "¿A quién beneficia y a quién perjudica la decisión?", "¿Se explicaron las razones?", "¿Se pudo opinar?", "El alcance se refiere a beneficiarios y perjudicados."),
        ("abc", "{F} El presidente dice que decidieron rápido «para evitar discusiones». ¿Qué criterio descuida esa razón?", "Participación, porque evita que los afectados opinen", "Alcance, porque la sala es pequeña", "Corrección, porque la decisión ya no existe", "Evitar la discusión impide que quienes resultan afectados opinen antes de decidir."),
        ("abc", "{F} Con las bodegas pagadas, ¿quiénes podrían quedar fuera según el criterio de alcance?", "Quienes no pueden pagar una bodega y usaban la sala para juntarse", "Todos los residentes por igual", "Solo los miembros del consejo", "El alcance pregunta a quién beneficia y a quién perjudica la decisión."),
        ("abc", "{F} ¿Por qué lo que dice el presidente («rápido» y «mayoría del consejo») no basta como justificación?", "Porque no responde a quienes resultan afectados ni explica por qué la medida es justa", "Porque ser presidente impide justificar", "Porque la rapidez es siempre mala", "No ofrece razones a los afectados ni considera el alcance."),
        ("abc", "{F} Si el consejo aceptara revisar la decisión en una asamblea, ¿qué criterio se cumpliría mejor?", "Corrección", "Alcance", "Rapidez", "Abre la posibilidad de revisar o cambiar la decisión."),
        ("abc", "Un centro de estudiantes ficticio cobra una cuota sin explicarla, pero la cuota es baja. ¿Qué criterio sigue incumpliendo?", "Justificación pública", "Corrección", "Alcance", "Que la cuota sea baja no reemplaza explicar las razones."),
        ("abc", "{F} ¿Cuál de estos argumentos evaluativos es correcto sobre la decisión del consejo?", "Una decisión debe permitir opinar a quienes resultan afectados; los residentes no pudieron opinar; luego la decisión no cumple la participación", "Una decisión es justa si es rápida; fue rápida; luego es justa", "Todo poder es injusto; el consejo tiene poder; luego es injusto", "Combina un criterio con un hecho del caso y obtiene una conclusión coherente."),
        ("abc", "Una estudiante dice: «Esa decisión es mala porque a mí no me favorece». ¿Qué falla tiene?", "Mezcla interés personal con evaluación y no usa un criterio", "Usa el criterio de alcance", "Respeta la participación", "Evaluar exige criterios que se aplicarían aunque la decisión la favoreciera."),
        ("abc", "Un caso cumple participación pero no corrección. ¿Qué indica esto?", "Que hay que ponderar criterios para valorar el caso completo", "Que el caso es justo sin más", "Que el caso es injusto sin más", "Un mismo caso puede cumplir unos criterios y no otros; se pondera."),
        ("abc", "{F} Se agrega un dato: la sala se usaba solo una vez al mes. ¿Cómo afecta el argumento del Residente B?", "Lo debilita, porque disminuye el beneficio perdido, aunque no elimina la falta de participación", "Lo elimina por completo", "No tiene relación", "Reduce el alcance negativo, pero no resuelve la falta de explicación ni de consulta."),
        ("abc", "{F} ¿Qué haría más justificable la decisión del consejo?", "Consultar a los residentes, explicar las razones y permitir revisarla", "Anunciarla más fuerte", "Cobrar menos por las bodegas sin explicar", "Responde a participación, justificación y corrección a la vez."),
    ],
    ctx=("abc", "Una escuela ficticia cambia el horario de los talleres a media mañana sin aviso, pues la dirección considera que así mejora la gestión. Algunos estudiantes dicen que ya no pueden ir. ¿Cuál es un argumento evaluativo adecuado?", "Los afectados deben poder opinar; no se consultó a quienes asisten a los talleres; luego la decisión no cumple la participación", "El horario es mejor si es nuevo; luego es justo", "Los estudiantes deben aceptarlo porque la dirección manda", "Aplica un criterio y un hecho del caso, y de ahí concluye de manera coherente."),
    sc=[
        ("En Filosofía política: ¿qué es un criterio?", "Una regla general que sirve para juzgar un caso", "Permite evaluar con razones y no por simpatía."),
        ("Nombra los cuatro criterios de la clase.", "Participación, justificación pública, corrección y alcance", "Son los cuatro criterios de la explicación."),
        ("¿Por qué la rapidez de una decisión no basta para justificarla?", "Porque no responde si se oyó a los afectados ni si hay razones públicas", "La rapidez es un rasgo del procedimiento, no una justificación."),
    ],
    op=("Elige un caso ficticio: (1) un club retira sin consulta el acceso gratuito de las y los socios a una cancha; (2) un curso cambia por votación la fecha de una jornada, pero tres personas no fueron avisadas. "
        "Evalúa el caso con al menos tres de los cuatro criterios y escribe un argumento de tres líneas (criterio, hecho, conclusión).",
        "Caso 2. Participación: tres personas no fueron avisadas, así que no cumple. Justificación pública: sí se discutió. Corrección: se puede repetir la votación. Argumento: todos los afectados deben poder opinar; tres no fueron avisadas; luego la decisión no cumple la participación.",
        ["usa al menos tres criterios correctamente", "el argumento tiene criterio, hecho y conclusión", "los hechos provienen del caso", "no evalúa por simpatía ni por interés personal"],
        ["evaluación con tres criterios y argumento de tres líneas"],
        ["usar solo un criterio", "inventar hechos que el caso no da", "evaluar por simpatía"],
        "Pregunta: «¿qué dato del caso apoya cada criterio que usaste?». Pídele que lo señale."),
    reinforce="Evalúa con los cuatro criterios una decisión reciente de tu curso o de tu barrio (descríbela en dos líneas).",
    extend="Compara dos decisiones con los mismos criterios y escribe cuál ponderarías primero y por qué.",
)

# ============================================================ OAC-02, clase 5
F = ("Ficha 9 (objeciones de ejemplo). Postura evaluada: «Las decisiones de una comunidad deben orientarse al bien común y evaluarse con participación, razones públicas y posibilidad de corrección». "
     "Objeción 1: «El bien común es una excusa para imponer lo que quiere la mayoría.» "
     "Objeción 2: «Siempre habrá jerarquías, así que criticar el poder no sirve de nada.» "
     "Objeción 3: «En la vida cotidiana no hay política, solo relaciones personales.»")
build(
    O2, 5, F,
    use="Aprenderé a responder objeciones a una postura sobre el poder y el bien común sin atacar a las personas y mejorando mi argumento.",
    prior=["Sé evaluar una decisión con cuatro criterios.", "Sé distinguir bien común de interés de la mayoría.", "Sé qué es una objeción."],
    explain=[
        "Responder una objeción es parte de defender una tesis. Primero se entiende la objeción en su versión más fuerte. Luego se elige cómo responder: conceder lo que tiene de cierto, distinguir conceptos que la objeción confunde, mostrar que su premisa es falsa o dudosa, o ajustar la tesis para que la resista. Una respuesta honesta puede incluir reconocer un límite.",
        "En la ficha, la objeción 1 mezcla bien común con voluntad de la mayoría; se responde distinguiendo: el bien común considera las condiciones de todas las personas, incluidas las minorías. La objeción 2 supone que si toda sociedad tiene jerarquías, evaluar el poder es inútil; se responde con una distinción: que exista jerarquía no implica que toda jerarquía esté justificada. La objeción 3 supone que lo cotidiano es solo personal; se responde mostrando que también en lo cotidiano hay decisiones que limitan lo que otros pueden hacer.",
        "Una buena respuesta no repite la tesis ni ataca a quien objeta. Reconoce el peso de la objeción, ofrece una razón y precisa qué cambia o qué se mantiene de la postura original.",
    ],
    vocab=[("objeción", "razón que cuestiona una tesis o una premisa"), ("conceder", "reconocer lo cierto de una objeción"), ("distinguir", "separar dos conceptos que la objeción confunde"), ("ajustar la tesis", "reformularla para que resista la objeción"), ("respuesta honesta", "respuesta que reconoce los límites de la propia postura"), ("versión más fuerte", "la formulación más sólida posible de una objeción")],
    worked=[
        ("Responder distinguiendo", "Responde la objeción 1 de la ficha.",
         ["Reconozco lo cierto: una mayoría podría invocar el bien común para imponer algo.", "Distingo: el bien común considera las condiciones de todas las personas, incluidas las minorías, y no equivale a lo que la mayoría desea."],
         "El bien común no equivale a la voluntad de la mayoría, porque considera las condiciones de todas las personas, incluidas las minorías"),
        ("Responder concediendo y ajustando", "Responde la objeción 2 sin negar que haya jerarquías.",
         ["Concedo: toda sociedad tiene jerarquías.", "Ajusto: lo que se evalúa es si cada jerarquía está justificada y se puede corregir, no si existe."],
         "Existen jerarquías, pero conviene evaluar si cada una está justificada y puede corregirse"),
    ],
    mistakes=[("Responder a una objeción atacando a quien la formula.", "Se evita discutir la razón y se pasa a la persona.", "Responde a la razón de la objeción y no a quien la dice."),
              ("Repetir la tesis como si fuera una respuesta.", "Una repetición no aporta una razón nueva.", "Concede, distingue o muestra qué premisa es dudosa.")],
    T=[
        ("abc", "{F} ¿Qué confunde la objeción 1?", "Bien común con voluntad de la mayoría", "Poder con autoridad", "Instituciones con grupos pequeños", "Trata como si fueran lo mismo bien común e interés de una mayoría."),
        ("abc", "{F} ¿Qué supone la objeción 2?", "Que si hay jerarquías, evaluar el poder es inútil", "Que no hay jerarquías", "Que toda jerarquía es injusta", "Su premisa implícita es que la existencia de jerarquías anula la crítica."),
        ("abc", "{F} ¿Qué supone la objeción 3?", "Que lo cotidiano es solo personal y no político", "Que el Estado es el único que decide", "Que no existen grupos pequeños", "Separa la política de la vida cotidiana."),
        ("abc", "Según la explicación, ¿qué significa «conceder» ante una objeción?", "Reconocer lo cierto de la objeción", "Aceptar toda la objeción y abandonar la tesis", "Ignorar la objeción", "Conceder es admitir lo que tiene de cierto, sin renunciar a la tesis."),
        ("abc", "Un estudiante responde a la objeción 1: «La mayoría siempre tiene razón». ¿Qué error comete?", "Acepta la confusión de la objeción y no distingue bien común de voluntad de la mayoría", "Distingue conceptos", "Concede y ajusta", "En vez de responder la distinción, la refuerza."),
        ("abc", "{F} ¿Cuál es la premisa dudosa de la objeción 2?", "Que, si algo siempre existe, no tiene sentido evaluarlo", "Que las sociedades tienen jerarquías", "Que el poder se puede criticar", "Del hecho de que algo exista no se sigue que esté justificado ni que no se pueda mejorar."),
        ("abc", "{F} ¿Cuál es una buena respuesta a la objeción 3?", "En grupos pequeños también se decide quién habla o qué se hace, y eso limita lo que otros pueden hacer", "La política solo ocurre en el Estado", "Las relaciones personales no tienen reglas ni decisiones", "Muestra que existen relaciones de poder en lo cotidiano."),
        ("abc", "Una estudiante responde a la objeción 2: «Usted dice eso porque nunca ha tenido un cargo». ¿Qué error comete?", "Ataca a la persona y no discute la razón", "Concede una parte", "Distingue conceptos", "No examina la premisa de la objeción."),
        ("abc", "Un grupo debe responder una objeción fuerte a su tesis. ¿Qué paso conviene primero?", "Formular la objeción en su versión más fuerte", "Ridiculizar la objeción", "Cambiar de tema", "Entender la objeción en su versión más sólida permite responderla bien."),
        ("abc", "{F} Se agrega la objeción 4: «Si todos opinan, nunca se decide nada». ¿Qué criterio de la clase anterior ayuda a responderla?", "Participación con procedimientos claros, para que opinar no impida decidir", "Rapidez absoluta", "Eliminar la participación", "Se puede mantener la participación con reglas y plazos."),
        ("abc", "Un estudiante responde la objeción 3: «Es cierto que muchas relaciones cotidianas son personales; pero cuando alguien decide por el grupo también se ejerce poder». ¿Qué estrategias usa?", "Conceder y distinguir", "Atacar a la persona", "Repetir la tesis sin cambios", "Reconoce un riesgo real y precisa el concepto."),
        ("abc", "Después de una objeción muy fuerte, una estudiante reformula su tesis para incluir una excepción. ¿Qué hizo?", "Ajustó la tesis", "Abandonó toda defensa", "Atacó a quien objeta", "Reformular para resistir la objeción es una respuesta legítima."),
        ("abc", "{F} Una estudiante dice: «La objeción 3 se responde diciendo que lo cotidiano es muy importante». ¿Por qué es insuficiente?", "No muestra que en lo cotidiano también hay decisiones que limitan a otros", "Porque la política solo ocurre en el Estado", "Porque falta citar una ley que regule lo cotidiano", "Debe mostrar por qué lo cotidiano es político, no solo decir que importa."),
    ],
    ctx=("abc", "En una asamblea ficticia de vecinos alguien objeta: «Si criticamos a la directiva, la comunidad se divide». ¿Cuál es la mejor respuesta filosófica?", "Criticar sus decisiones con razones puede fortalecer la comunidad si se buscan mejoras y no solo culpables", "No hay que criticar nunca", "Quien critica es un enemigo", "Distingue entre criticar decisiones con razones y dividir, y no ataca a la persona."),
    sc=[
        ("En Filosofía política: ¿qué es una objeción?", "Una razón que cuestiona una tesis o una premisa", "Se responde con razones, no atacando a la persona."),
        ("Nombra dos formas de responder una objeción.", "Conceder lo cierto y distinguir conceptos (o ajustar la tesis)", "Son dos de las estrategias que enseña la explicación de la clase."),
        ("¿Por qué conviene formular una objeción en su versión más fuerte?", "Porque así la respuesta es más sólida y honesta", "Responder una versión débil no pone a prueba la tesis."),
    ],
    op=("Elige una objeción: (1) «Evaluar el poder desde el bien común es imposible, porque cada persona entiende algo distinto por bien común»; (2) «Si todos deben opinar, las decisiones serán demasiado lentas». "
        "Escribe la objeción en su versión más fuerte, una respuesta que use al menos una de estas estrategias (conceder, distinguir, ajustar la tesis) y una frase que diga qué mantienes y qué cambias de tu postura.",
        "Objeción 2. Versión fuerte: en comunidades grandes, consultar a todos puede impedir actuar a tiempo. Respuesta: concedo que algunas decisiones requieren rapidez; distingo entre decisiones urgentes y decisiones de largo plazo. Mantengo la participación; ajusto: en urgencias se justifica decidir y rendir cuentas después.",
        ["formula la objeción en su versión más fuerte", "usa al menos una estrategia de respuesta", "no ataca a quien objeta", "indica qué mantiene y qué cambia de su postura"],
        ["objeción, respuesta y balance de la postura"],
        ["responder repitiendo la tesis", "atacar a quien objeta", "no precisar qué cambia en la postura"],
        "Pregunta: «¿qué parte de la objeción reconoces como cierta?». Pídele que lo escriba antes de responder."),
    reinforce="Anota una objeción que alguien te haya hecho en una conversación y escribe cómo la responderías concediendo algo y distinguiendo algo.",
    extend="Escribe la mejor objeción que podrías hacer a tu propia respuesta y una réplica breve.",
)
