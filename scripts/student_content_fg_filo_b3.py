"""Filosofía 3.º medio FG: OA 06 (argumentación, validez y razonamiento filosófico). Textos y casos de ejemplo inventados."""
from __future__ import annotations

from fg_filo_common import build

O6 = "FG-FILO-3M-OAC-06"

# ============================================================ OA 06, clase 1
F = ("Ficha 1 (tres intervenciones de ejemplo en un consejo de curso): "
     "(a) «Propongo alargar el recreo, porque en el recreo conversamos y eso mejora el ánimo para estudiar». "
     "(b) «Hay que alargar el recreo, ¡ya, ya, ya!». "
     "(c) «No le hagan caso a esa propuesta: la hace alguien que siempre llega tarde».")
build(
    O6, 1, F,
    use="Aprenderé a distinguir un argumento de una opinión suelta o de un ataque, y a identificar su conclusión y sus premisas.",
    prior=["Sé que una razón puede revisarse.", "Sé que creer no es saber.", "Sé que en un diálogo se piden razones."],
    explain=[
        "Un argumento es un conjunto de afirmaciones en que algunas, llamadas premisas, se ofrecen como razones para aceptar otra, llamada conclusión. La conclusión es lo que se quiere que acepten; las premisas son las razones. En la intervención (a) la conclusión es «hay que alargar el recreo» y la premisa es «en el recreo conversamos y eso mejora el ánimo para estudiar».",
        "No toda frase es un argumento. Una opinión suelta, como la intervención (b), afirma algo sin dar razones. Un ataque personal, como la (c), habla de quien propone y no de lo que propone. Las palabras como «porque», «ya que», «por lo tanto» o «entonces» suelen señalar razones o conclusión, pero no siempre aparecen: hay que preguntarse qué se quiere probar y qué se ofrece para probarlo.",
        "Problematizar una situación de discusión es preguntarse qué se afirma, qué razones hay y si esas razones realmente apoyan la afirmación. Una razón puede ser verdadera y aun así no tener relación con la conclusión. Distinguir estas partes es el primer paso para evaluar un argumento.",
    ],
    vocab=[("argumento", "conjunto de afirmaciones en que unas, las premisas, se ofrecen como razones para aceptar otra, la conclusión"), ("premisa", "afirmación que se ofrece como razón"), ("conclusión", "afirmación que se quiere que la otra persona acepte"), ("opinión suelta", "afirmación que se da sin razones"), ("ataque personal", "crítica a quien propone en vez de a lo que propone")],
    worked=[
        ("Hallar la conclusión", "Texto de ejemplo: «El gimnasio debería abrir temprano, ya que muchas personas trabajan desde las 9». ¿Cuál es la conclusión?", ["La palabra «ya que» señala la razón.", "Lo que se quiere que acepten es lo que va antes."], "El gimnasio debería abrir temprano"),
        ("Distinguir argumento y opinión", "Dos frases de ejemplo: «Ese libro es horrible» y «Ese libro es confuso, porque cambia de narrador sin avisar». ¿Cuál es un argumento?", ["La primera no da razón.", "La segunda da una razón."], "La segunda"),
    ],
    mistakes=[("Creer que cualquier frase con «porque» es un buen argumento.", "La razón puede no tener relación con la conclusión.", "Revisa si la razón realmente apoya la conclusión."),
              ("Tomar el ataque a una persona como si fuera una razón.", "Quien propone no cambia el valor de lo propuesto.", "Pregunta qué razones hay sobre la propuesta en sí.")],
    T=[
        ('abc', '{F} ¿Cuál es la conclusión de la intervención (a)?', 'Hay que alargar el recreo', 'En el recreo conversamos', 'Eso mejora el ánimo para estudiar', 'Lo que se quiere que acepten es alargar el recreo; las otras frases son las razones.'),
        ('abc', '{F} ¿Cuál es la premisa de (a)?', 'En el recreo conversamos y eso mejora el ánimo para estudiar', 'Propongo alargar el recreo', 'Hay que decidir hoy en el consejo', 'La premisa es la razón que se da, y va después de «porque».'),
        ('abc', '{F} ¿Por qué (b) no es un argumento?', 'Porque afirma algo sin dar ninguna razón', 'Porque tiene muchos signos de exclamación', 'Porque se dice con mucha urgencia', 'Un argumento necesita premisas; (b) solo repite la afirmación con énfasis.'),
        ('abc', '{F} ¿Qué hace la intervención (c)?', 'Critica a quien propone y no a lo que propone', 'Ofrece una razón sobre la propuesta del recreo', 'Presenta datos sobre el ánimo para estudiar', 'Habla de la puntualidad de la persona, no de si conviene alargar el recreo.'),
        ('abc', '¿Para qué sirven las palabras «porque» y «por lo tanto» en un texto?', 'Suelen señalar una razón o una conclusión', 'Aseguran que lo dicho es verdadero', 'Solo sirven para unir frases largas', 'Ayudan a ubicar premisas y conclusión, pero no prueban nada por sí solas.'),
        ('abc', 'Texto: «Mañana habrá poco público, porque es feriado y la mayoría viaja». ¿Cuál es la conclusión?', 'Mañana habrá poco público', 'Es feriado', 'La mayoría viaja', 'Se afirma que habrá poco público y se dan dos razones.'),
        ('abc', 'Texto de ejemplo: «El parque debe tener más bancas. Lo digo yo». ¿Qué le falta?', 'Una razón que apoye la conclusión', 'Una conclusión más corta', 'Una pregunta al final', 'Hay una conclusión, pero la única razón es que la dice quien habla.'),
        ('abc', 'Texto de ejemplo: «Hay que llegar temprano, porque la puerta abre a las 8 y la fila es larga». ¿Cuántas premisas tiene?', 'Dos', 'Una', 'Tres', 'Las razones son «la puerta abre a las 8» y «la fila es larga»; la conclusión es llegar temprano.'),
        ('abc', '{F} Un compañero dice: «(c) es un buen argumento, porque dice quién hace la propuesta». ¿Qué error comete?', 'Confunde hablar de quien propone con dar una razón sobre la propuesta', 'Cree que un argumento no puede criticar nada', 'Piensa que toda crítica a una persona es falsa', 'Que alguien llegue tarde no dice nada sobre si conviene alargar el recreo.'),
        ('abc', 'Una razón verdadera pero sin relación con la conclusión, ¿qué problema tiene?', 'Es irrelevante: no apoya la conclusión aunque sea cierta', 'Es falsa, porque no se relaciona', 'Es una conclusión disfrazada de razón', 'Una razón puede ser cierta y no tener relación con lo que se quiere probar.'),
        ('{F} ¿Qué pregunta haría avanzar la discusión entre (a) y (c)?', '¿Mejora realmente el ánimo conversar en el recreo?', 'Esa pregunta lleva la discusión a la razón de (a), que es lo que se puede examinar con datos o experiencias.'),
        ('abc', 'Texto de ejemplo: «Si estudias cada día, aprendes mejor; por eso conviene estudiar cada día». ¿Cuál es la conclusión?', 'Conviene estudiar cada día', 'Si estudias cada día, aprendes mejor', 'Aprendes mejor', 'La conclusión viene tras «por eso»; la razón es la condición antes.'),
        ('abc', '{F} Si (b) agregara: «porque el recreo es corto y nos falta tiempo para conversar», ¿pasaría a ser un argumento?', 'Sí, porque tendría una razón para la conclusión', 'No, porque seguiría siendo una exigencia', 'No, porque las razones no pueden agregarse después', 'Con una razón que apoya la conclusión, hay un argumento, aunque pueda ser débil.'),
    ],
    ctx=('abc', 'En el chat del curso de ejemplo alguien escribe: «Propongo hacer la salida al museo, porque nadie del curso lo conoce y sirve para el trabajo de historia». ¿Qué parte es la conclusión?', 'Hacer la salida al museo', 'Nadie del curso lo conoce', 'Sirve para el trabajo de historia', 'Lo que se propone aceptar es hacer la salida; lo demás son razones.'),
    sc=[
        ('En Filosofía: ¿qué es una premisa?', 'Una afirmación que se ofrece como razón', 'Es la razón que apoya la conclusión.'),
        ('abc', '¿Cuál de estas frases es un argumento?', 'Hay que cuidar la plaza, porque es el lugar donde juegan los niños del barrio', 'Hay que cuidar la plaza, ¡ya mismo!', 'Hay que cuidar la plaza, aunque lo diga alguien que nunca va', 'La primera da una razón; las otras repiten la orden o atacan a la persona.'),
        ('¿Qué es un ataque personal?', 'Criticar a quien propone y no a lo que propone', 'Se dirige a la persona y deja sin responder la propuesta.'),
    ],
    op=("Usa la {F} Escribe una tabla con las tres intervenciones: para cada una indica si es argumento, opinión suelta o ataque personal y por qué. Luego reescribe (b) para que sea un argumento con una razón.",
        "(a) argumento: conclusión alargar el recreo, razón conversar mejora el ánimo. (b) opinión suelta: no da razones. (c) ataque personal: habla de quien propone. Reescrito: «Hay que alargar el recreo, porque quince minutos no alcanzan para almorzar y conversar».",
        ["clasifica cada intervención con razón", "reescribe con una premisa pertinente"], ["tabla de tres filas", "reescritura de (b)"], ["llamar argumento a un ataque", "reescribir sin dar razón"],
        "Pide que explique por qué su razón apoya realmente la conclusión."),
    reinforce="Escribe dos frases: una opinión suelta y un argumento sobre el mismo tema.",
    extend="Elige una discusión que hayas escuchado y anota su conclusión y sus premisas.",
)

# ============================================================ OA 06, clase 2
F = ("Ficha 2 (tres argumentos de ejemplo): "
     "Argumento 1: «Todos los gatos son mamíferos. Pelusa es un gato. Por lo tanto, Pelusa es un mamífero». "
     "Argumento 2: «Todos los peces vuelan. El salmón es un pez. Por lo tanto, el salmón vuela». "
     "Argumento 3: «Algunos estudiantes del curso estudian. Ana es estudiante del curso. Por lo tanto, Ana estudia».")
build(
    O6, 2, F,
    use="Aprenderé a definir inferencia, validez, solidez y consistencia, y a decidir si un argumento es válido imaginando un caso en que las premisas sean verdaderas y la conclusión falsa.",
    prior=["Sé distinguir premisa y conclusión.", "Sé que una razón puede ser verdadera y no relevante.", "Sé qué es una afirmación verdadera o falsa."],
    explain=[
        "Una inferencia es el paso de las premisas a la conclusión. Un argumento es válido cuando, si las premisas fueran verdaderas, la conclusión no podría ser falsa. La validez habla de la forma del razonamiento y no de si las premisas son ciertas. Por eso un argumento puede ser válido y tener una conclusión falsa: si una premisa es falsa, todo puede salir mal.",
        "Un argumento es sólido cuando es válido y además sus premisas son verdaderas. El argumento 1 es válido y sólido. El argumento 2 es válido, porque si todos los peces volaran, el salmón volaría, pero no es sólido, porque su primera premisa es falsa. El argumento 3 es inválido: que algunos estudiantes estudien no obliga a que Ana sea una de ellos.",
        "Para probar que un argumento es inválido se busca un contraejemplo: una situación imaginable en que las premisas sean verdaderas y la conclusión falsa. En el argumento 3, Ana podría ser una estudiante que no estudia. Un conjunto de afirmaciones es consistente cuando pueden ser todas verdaderas a la vez; si no, es inconsistente.",
    ],
    vocab=[("inferencia", "paso de las premisas a la conclusión"), ("validez", "cualidad de un argumento en que, si las premisas fueran verdaderas, la conclusión no podría ser falsa"), ("solidez", "cualidad de un argumento válido cuyas premisas son verdaderas"), ("contraejemplo", "situación imaginable con premisas verdaderas y conclusión falsa"), ("consistencia", "cualidad de un conjunto de afirmaciones que pueden ser todas verdaderas a la vez")],
    worked=[
        ("Válido pero no sólido", "Argumento de ejemplo: «Todos los autos son verdes. Mi vehículo es un auto. Mi vehículo es verde». ¿Es válido? ¿Es sólido?", ["Si las premisas fueran ciertas, la conclusión no podría fallar: es válido.", "La primera premisa es falsa, así que no es sólido."], "Válido, no sólido"),
        ("Buscar un contraejemplo", "Argumento de ejemplo: «Algunas frutas son dulces. La palta es una fruta. Por lo tanto, la palta es dulce». ¿Hay contraejemplo?", ["Las premisas pueden ser verdaderas.", "La palta podría estar entre las frutas no dulces."], "Hay contraejemplo: es inválido"),
    ],
    mistakes=[("Decir que un argumento es válido porque su conclusión es verdadera.", "La validez depende de la relación entre premisas y conclusión, no de la verdad de la conclusión.", "Imagina premisas verdaderas y pregunta si la conclusión podría fallar."),
              ("Decir que un argumento con una premisa falsa es inválido.", "Se confunde validez con solidez.", "Un argumento puede ser válido y no sólido.")],
    T=[
        ('abc', '¿Qué es un argumento válido?', 'Uno en que, si las premisas fueran verdaderas, la conclusión no podría ser falsa', 'Uno cuya conclusión es verdadera en el mundo real', 'Uno cuyas premisas son verdaderas', 'La validez solo mira la relación entre premisas y conclusión.'),
        ('abc', '{F} ¿El argumento 1 es sólido?', 'Sí, porque es válido y sus premisas son verdaderas', 'No, porque trata de animales', 'No, porque la conclusión es demasiado obvia', 'La solidez pide validez y premisas verdaderas; ambas se cumplen.'),
        ('abc', '{F} ¿Por qué el argumento 2 es válido aunque su conclusión sea falsa?', 'Porque, si todos los peces volaran, el salmón volaría', 'Porque las premisas son verdaderas y la conclusión también', 'Porque en la vida real los salmones nadan', 'Se evalúa la forma suponiendo verdaderas las premisas; la falsedad viene de una premisa.'),
        ('abc', '{F} ¿Por qué el argumento 2 no es sólido?', 'Porque su primera premisa es falsa', 'Porque su forma es inválida', 'Porque su conclusión es una opinión', 'No todos los peces vuelan; la forma es correcta pero falla una premisa.'),
        ('abc', '{F} ¿Por qué el argumento 3 es inválido?', 'Porque Ana podría ser una estudiante que no estudia, con premisas verdaderas', 'Porque la conclusión es falsa en todos los casos posibles', 'Porque «algunos» es una palabra que no permite razonar', 'Hay un contraejemplo: se pueden cumplir las premisas y fallar la conclusión.'),
        ('abc', '¿Qué es un contraejemplo?', 'Una situación imaginable con premisas verdaderas y conclusión falsa', 'Un ejemplo que demuestra que la conclusión es verdadera y que el argumento es válido', 'Una premisa que contradice la conclusión', 'Sirve para mostrar que un argumento es inválido.'),
        ('abc', 'Argumento de ejemplo: «Todos los perros ladran. Rex ladra. Por lo tanto, Rex es un perro». ¿Es válido?', 'No: Rex podría ser otro animal que ladre', 'Sí: si Rex ladra es perro', 'Sí: todos los perros ladran, Rex ladra y entonces es perro', 'Un contraejemplo es otro animal que ladre; las premisas no obligan a la conclusión.'),
        ('abc', 'Argumento de ejemplo: «Todas las cucharas del cajón son de metal. Esta es una cuchara del cajón. Por lo tanto, esta es de metal». ¿Es válido?', 'Sí: si las premisas son verdaderas, la conclusión debe serlo', 'No: porque habla de cucharas', 'No: no se sabe si las premisas son ciertas en la realidad', 'La validez no necesita saber si es cierto, solo si la conclusión se sigue.'),
        ('abc', 'Alguien dice: «Mi argumento es válido porque su conclusión es verdadera». ¿Qué error comete?', 'Confunde la verdad de la conclusión con la validez', 'Confunde premisa con conclusión', 'Cree que todo argumento válido es falso', 'La validez no depende de que la conclusión sea verdadera.'),
        ('abc', '¿Cuál conjunto es inconsistente?', '«Todas las tiendas cierran a las 8» y «La tienda Sol, del barrio, abre hasta las 10»', '«Mañana lloverá» y «Mañana hará frío»', '«Ana es mayor que Luis, que tiene 15 años» y «Luis es menor que Ana, que tiene 17 años»', 'No pueden ser verdaderas a la vez: si todas cierran a las 8, la tienda Sol no abre hasta las 10.'),
        ('abc', '{F} Si se cambiara la premisa 1 del argumento 3 por «Todos los estudiantes del curso estudian», ¿qué pasaría?', 'Pasaría a ser válido', 'Seguiría siendo inválido', 'Dejaría de tener conclusión', 'Si todos los estudiantes estudian y Ana es estudiante, Ana estudia necesariamente.'),
        ('Un argumento tiene premisas verdaderas y es válido. ¿Qué se sigue de su conclusión?', 'Que es verdadera', 'Si es válido y las premisas son verdaderas, el argumento es sólido y la conclusión no puede ser falsa.'),
        ('abc', '{F} Si el argumento 1 cambiara su primera premisa por «Algunos gatos son mamíferos», ¿seguiría siendo válido?', 'No: Pelusa podría ser uno de los gatos que no lo son', 'Sí: Pelusa sigue siendo un gato', 'Sí: la conclusión sigue siendo verdadera', 'Con «algunos» ya no se garantiza que Pelusa esté entre ellos.'),
    ],
    ctx=('abc', 'Un amigo de ejemplo argumenta: «Todos los que van al taller de teatro hablan fuerte. Sofía habla fuerte. Entonces Sofía va al taller de teatro». ¿Qué conviene responderle?', 'Que es inválido: Sofía podría hablar fuerte sin ir al taller', 'Que es válido, porque Sofía habla fuerte', 'Que es sólido, porque sus premisas son verdaderas', 'Las premisas no obligan a la conclusión; basta imaginar a Sofía hablando fuerte sin ir al taller.'),
    sc=[
        ('En Filosofía: ¿qué es la solidez de un argumento?', 'Que es válido y sus premisas son verdaderas', 'Pide forma correcta y premisas verdaderas.'),
        ('abc', '¿Qué conviene hacer para mostrar que un argumento es inválido?', 'Buscar un contraejemplo', 'Comprobar que su conclusión es falsa', 'Contar cuántas premisas tiene', 'Un contraejemplo muestra premisas verdaderas con conclusión falsa.'),
        ('En Filosofía: ¿Qué es una inferencia?', 'El paso de las premisas a la conclusión', 'Es el movimiento de razonar desde las razones hacia lo que se concluye.'),
    ],
    op=("Usa la {F} Para cada uno de los tres argumentos escribe: si es válido o inválido, si es sólido o no, y una razón de una línea (un contraejemplo si es inválido). Termina diciendo por qué conviene separar validez y solidez.",
        "1: válido y sólido. 2: válido, no sólido (premisa 1 falsa). 3: inválido (Ana podría ser una estudiante que no estudia). Se separan porque la forma y la verdad de las premisas fallan por motivos distintos.",
        ["distingue validez y solidez", "da un contraejemplo", "explica la diferencia"], ["tres clasificaciones", "una frase final"], ["decir que válido significa verdadero", "no dar contraejemplo"],
        "Pregunta qué cambiaría en el argumento 2 para que fuera sólido."),
    reinforce="Escribe un argumento válido con una premisa falsa.",
    extend="Busca en una conversación un razonamiento inválido y escribe su contraejemplo.",
)

# ============================================================ OA 06, clase 3
F = ("Ficha 3 (textos de ejemplo): "
     "Texto A: «Si llueve, la cancha se moja. La cancha está seca. Entonces no llovió». "
     "Texto B: «Si llueve, la cancha se moja. La cancha está mojada. Entonces llovió». "
     "Texto C: «Si hay clases, el patio se llena. Hay clases. Entonces el patio se llena». "
     "Texto D: «Los últimos 30 lunes la panadería abrió. Entonces, probablemente abrirá el próximo lunes».")
build(
    O6, 3, F,
    use="Aprenderé a reconstruir razonamientos en forma estándar y a reconocer cuatro formas de razonar: dos válidas, dos inválidas, y el razonamiento inductivo.",
    prior=["Sé qué son premisa, conclusión, validez y contraejemplo.", "Sé que un argumento válido no siempre es sólido.", "Sé buscar un contraejemplo."],
    explain=[
        "Reconstruir un argumento es escribirlo en forma estándar: las premisas en una lista numerada y la conclusión al final, quitando adornos. Un enunciado condicional tiene la forma «si P, entonces Q»; P se llama antecedente (lo que se supone) y Q consecuente (lo que se sigue). Con condicionales hay dos formas válidas y dos inválidas.",
        "Válidas: afirmar el antecedente (si P entonces Q; P; luego Q, como el texto C) y negar el consecuente (si P entonces Q; no Q; luego no P, como el texto A). Inválidas: afirmar el consecuente (si P entonces Q; Q; luego P, como el texto B) y negar el antecedente (si P entonces Q; no P; luego no Q). El texto B falla porque la cancha puede estar mojada por otra causa, como un riego.",
        "Un razonamiento deductivo busca que la conclusión se siga con necesidad de las premisas. Uno inductivo, como el texto D, parte de casos observados y concluye algo probable: puede ser más o menos fuerte, pero nunca garantiza la conclusión. Un razonamiento inductivo no se llama válido o inválido, sino fuerte o débil.",
    ],
    vocab=[("forma estándar", "premisas listadas y conclusión al final, sin adornos"), ("condicional", "enunciado de la forma «si P, entonces Q»"), ("antecedente", "la parte P del condicional, lo que se supone"), ("consecuente", "la parte Q del condicional, lo que se sigue"), ("razonamiento inductivo", "el que parte de casos observados y concluye algo probable")],
    worked=[
        ("Reconstruir en forma estándar", "Texto de ejemplo: «Si hace frío, uso chaleco. Hoy no uso chaleco. Entonces hoy no hace frío». ¿Cómo queda en forma estándar y qué forma es?", ["P1: Si hace frío, uso chaleco. P2: No uso chaleco. C: No hace frío.", "Niega el consecuente: es una forma válida."], "Negar el consecuente, válido"),
        ("Detectar forma inválida", "Texto de ejemplo: «Si estudio, apruebo. Aprobé. Entonces estudié». ¿Es válido?", ["Afirma el consecuente.", "Se puede aprobar sin estudiar, por ejemplo por mucha suerte."], "Inválido"),
    ],
    mistakes=[("Creer que si el consecuente se cumple, el antecedente también.", "Se afirma el consecuente: la cancha puede mojarse por otra causa.", "Busca otra causa posible: si existe, hay contraejemplo."),
              ("Llamar «válido» a un razonamiento inductivo fuerte.", "La validez es de los deductivos; los inductivos son fuertes o débiles.", "Di cuán fuerte es y por qué no garantiza la conclusión.")],
    T=[
        ('abc', '{F} ¿Qué forma tiene el texto C?', 'Afirmar el antecedente: es válido', 'Afirmar el consecuente: es inválido', 'Negar el antecedente: es inválido', 'Dice «si P entonces Q; P; luego Q», una forma válida.'),
        ('abc', '{F} ¿Qué forma tiene el texto A?', 'Negar el consecuente: es válido', 'Afirmar el consecuente: es inválido', 'Afirmar el antecedente: es válido', 'Dice «si P entonces Q; no Q; luego no P»: si lloviera, la cancha estaría mojada.'),
        ('abc', '{F} ¿Por qué el texto B es inválido?', 'Porque la cancha podría estar mojada por otra causa, como un riego', 'Porque la cancha no puede mojarse con lluvia', 'Porque no tiene una conclusión', 'El contraejemplo es una cancha mojada sin lluvia: las premisas verdaderas no obligan a la conclusión.'),
        ('abc', '{F} En «si llueve, la cancha se moja», ¿cuál es el antecedente?', 'Llueve', 'La cancha se moja', 'La cancha está seca', 'El antecedente es la parte que va después de «si».'),
        ('abc', '{F} En «si llueve, la cancha se moja», ¿cuál es el consecuente?', 'La cancha se moja', 'Llueve', 'No llovió', 'El consecuente es lo que se sigue, después de «entonces».'),
        ('abc', '{F} ¿Qué tipo de razonamiento es el texto D?', 'Inductivo, porque parte de casos observados y concluye algo probable', 'Deductivo, porque la conclusión es segura', 'Inválido, porque tiene una premisa', 'Se basa en 30 casos y concluye «probablemente».'),
        ('abc', '{F} ¿Qué dato debilitaría más el razonamiento del texto D?', 'Que la panadería anunció que cerrará el próximo lunes', 'Que la panadería abrió también muchos martes', 'Que la panadería es muy conocida', 'Un anuncio de cierre afecta directamente a la conclusión sobre el próximo lunes.'),
        ('abc', 'Forma estándar: P1: Si el cable está roto, la lámpara no enciende. P2: La lámpara enciende. C: El cable no está roto. ¿Qué forma es?', 'Negar el consecuente: válida', 'Afirmar el consecuente: inválida', 'Negar el antecedente: inválida', 'La lámpara enciende niega «no enciende», que es el consecuente, y se concluye la negación del antecedente.'),
        ('abc', 'Texto de ejemplo: «Si se corta la luz, el semáforo se apaga. No se cortó la luz. Entonces el semáforo no se apagó». ¿Qué forma es?', 'Negar el antecedente: inválida', 'Negar el consecuente: válida', 'Afirmar el antecedente: válida', 'Un semáforo puede apagarse por otra falla sin que se corte la luz.'),
        ('abc', 'Texto de ejemplo: «Si Ana trae la llave, entramos. Ana trajo la llave. Entonces entramos». ¿Qué forma es?', 'Afirmar el antecedente: válida', 'Afirmar el consecuente: inválida', 'Negar el consecuente: válida', 'Se afirma que se cumple lo que va tras «si», y se concluye lo que sigue.'),
        ('{F} Escribe en forma estándar el texto A (P1, P2 y C).', 'P1: Si llueve, la cancha se moja. P2: La cancha no está mojada. C: No llovió.', 'La forma estándar lista las premisas y deja la conclusión al final, sin adornos.'),
        ('abc', '¿Cuál es una diferencia entre un razonamiento deductivo y uno inductivo?', 'El deductivo busca que la conclusión sea necesaria; el inductivo, que sea probable', 'El deductivo parte de casos particulares y el inductivo de reglas generales', 'El deductivo da conclusiones probables y el inductivo necesarias', 'La diferencia está en el grado de apoyo que dan las premisas.'),
        ('abc', '{F} Si el texto D tuviera 3 lunes en vez de 30, ¿qué pasaría?', 'Sería más débil, porque se apoya en menos casos', 'Sería más fuerte, porque es más sencillo', 'Sería inválido, porque cambió el número', 'Con menos casos observados, la conclusión probable queda menos apoyada.'),
    ],
    ctx=('abc', 'Una amiga de ejemplo dice: «Si me enojo, hablo fuerte. Hablo fuerte. Entonces estoy enojada». ¿Qué forma comete?', 'Afirmar el consecuente: inválida', 'Afirmar el antecedente: válida', 'Negar el consecuente: válida', 'Puede hablar fuerte por otra razón, como estar en un lugar con mucho ruido.'),
    sc=[
        ('En Filosofía: ¿qué es el antecedente de «si P, entonces Q»?', 'P', 'Es la parte que se supone, tras «si».'),
        ('abc', '¿Cuál forma de razonamiento con condicionales es inválida?', 'Afirmar el consecuente', 'Afirmar el antecedente', 'Negar el consecuente', 'Las otras dos son válidas; la primera tiene contraejemplos.'),
        ('¿Cómo se llama el razonamiento que parte de casos observados y concluye algo probable?', 'Inductivo', 'Parte de casos particulares y concluye con probabilidad.'),
    ],
    op=("Usa la {F} Reconstruye en forma estándar los textos A y B, di qué forma tiene cada uno y por qué uno es válido y el otro no. Cierra con una frase sobre la fuerza del texto D.",
        "A: P1 Si llueve, la cancha se moja; P2 La cancha no está mojada; C No llovió: negar el consecuente, válido. B: P1 Si llueve, la cancha se moja; P2 La cancha está mojada; C Llovió: afirma el consecuente, inválido (riego). D: es inductivo, fuerte pero no garantiza.",
        ["escribe premisas y conclusión", "nombra las formas", "da un contraejemplo", "califica el inductivo"], ["dos reconstrucciones", "una frase final"], ["llamar válido al texto B", "decir que D es seguro"],
        "Pregunta qué cambio dejaría válido al texto B."),
    reinforce="Escribe un condicional de tu vida diaria y dos formas válidas con él.",
    extend="Busca una frase que afirme el consecuente y escribe un contraejemplo.",
)

# ============================================================ OA 06, clase 4
F = ("Ficha 4 (cuatro textos de ejemplo): "
     "Texto 1: «Si dejamos usar celular en clases, pronto nadie va a escuchar a nadie y nos quedaremos sin colegio». "
     "Texto 2: «O prohibimos todos los celulares, o aceptamos que las clases sean un caos». "
     "Texto 3: «Ese compañero dice que hay que reciclar, pero él llega en auto: no lo escuchemos». "
     "Texto 4: «Mi vecina compró una marca de zapatillas y se rompieron; esa marca es mala para todos».")
build(
    O6, 4, F,
    use="Aprenderé a evaluar razonamientos en textos de ejemplo, a reconocer algunas falacias, a detectar inconsistencias y a usar el contraejemplo y el caso imaginado como métodos filosóficos.",
    prior=["Sé qué es un argumento válido y uno sólido.", "Sé buscar un contraejemplo.", "Sé distinguir deductivo e inductivo."],
    explain=[
        "Una falacia es un razonamiento que parece bueno pero no lo es. Cuatro falacias frecuentes: la pendiente resbaladiza (afirmar que un paso llevará a un desastre sin razones para cada etapa); la falsa dicotomía (presentar solo dos opciones cuando hay más); el ataque a la persona (criticar a quien habla en vez de lo que dice); y la generalización apresurada (concluir sobre todos desde pocos casos).",
        "Cada texto de la ficha comete una: el 1, pendiente resbaladiza; el 2, falsa dicotomía; el 3, ataque a la persona; el 4, generalización apresurada. Reconocer una falacia no prueba que la conclusión sea falsa: solo muestra que las razones dadas no la apoyan. Tal vez exista otra razón buena para la misma conclusión.",
        "En la filosofía se usan métodos para razonar mejor. El contraejemplo muestra que una afirmación general falla con un caso. El caso imaginado, también llamado experimento mental, es una situación inventada para probar una idea: «si pudiéramos…, ¿qué diríamos?». Y la consistencia obliga a no sostener a la vez ideas que se contradicen.",
    ],
    vocab=[("falacia", "razonamiento que parece bueno pero no lo es"), ("pendiente resbaladiza", "falacia de afirmar que un primer paso llevará a un desastre sin razones para cada etapa"), ("falsa dicotomía", "falacia de presentar solo dos opciones cuando hay más"), ("generalización apresurada", "falacia de concluir sobre todos a partir de pocos casos"), ("caso imaginado", "situación inventada para probar una idea")],
    worked=[
        ("Reconocer una falacia", "Texto de ejemplo: «Mi primo probó una app de cocina y le falló; todas las apps de cocina son inútiles». ¿Qué falacia es?", ["Se concluye sobre todas a partir de un caso.", "Es una generalización apresurada."], "Generalización apresurada"),
        ("Usar un contraejemplo", "Afirmación de ejemplo: «Todos los deportes se juegan con pelota». ¿Qué contraejemplo la refuta?", ["Se busca un deporte sin pelota.", "La natación, por ejemplo."], "La natación"),
    ],
    mistakes=[("Decir que una conclusión es falsa porque el argumento tiene una falacia.", "Falta de buenas razones no es lo mismo que falsedad.", "Di que las razones no la apoyan y busca si hay otras."),
              ("Ver falacias en todo desacuerdo.", "Se acusa de falacia sin mostrar qué razón falla.", "Nombra la falacia solo si puedes mostrar qué pasa en el texto.")],
    T=[
        ('abc', '{F} ¿Qué falacia comete el texto 1?', 'Pendiente resbaladiza', 'Falsa dicotomía', 'Ataque a la persona', 'Afirma que un primer paso llevará a un desastre sin razones para cada etapa.'),
        ('abc', '{F} ¿Qué falacia comete el texto 2?', 'Falsa dicotomía', 'Generalización apresurada', 'Pendiente resbaladiza', 'Presenta solo dos opciones cuando hay más, como regular los usos del celular.'),
        ('abc', '{F} ¿Qué falacia comete el texto 3?', 'Ataque a la persona', 'Falsa dicotomía', 'Generalización apresurada', 'Se critica a quien propone reciclar en vez de a la propuesta.'),
        ('abc', '{F} ¿Qué falacia comete el texto 4?', 'Generalización apresurada', 'Ataque a la persona', 'Pendiente resbaladiza', 'Concluye sobre todas las zapatillas de la marca desde un solo caso.'),
        ('abc', '{F} ¿Qué opción deja fuera el texto 2?', 'Permitir los celulares solo para actividades acordadas', 'Prohibir el celular en todo el colegio durante todas las horas del día', 'Aceptar que las clases sean un caos', 'Hay opciones intermedias que el texto no considera.'),
        ('abc', '{F} Si el compañero del texto 3 llega en auto, ¿eso demuestra que reciclar es malo?', 'No: no dice nada sobre la propuesta de reciclar', 'Sí: demuestra que no cree lo que dice', 'Sí: demuestra que la propuesta de reciclar es falsa porque quien la hace no la cumple', 'Los hábitos de quien propone no prueban que la propuesta sea falsa.'),
        ('abc', '¿Qué es una falacia?', 'Un razonamiento que parece bueno pero no lo es', 'Una afirmación falsa', 'Una opinión que no gusta', 'Es un error del razonamiento, aunque la conclusión pudiera ser verdadera por otras razones.'),
        ('abc', 'Alguien dice: «El texto 3 comete una falacia; por lo tanto, reciclar es una mala idea». ¿Qué error hay?', 'Concluye que algo es falso solo porque una razón es mala', 'Confunde la falacia con un contraejemplo', 'Supone que reciclar es malo porque el compañero llega en auto', 'Mostrar una falacia no prueba lo contrario; la conclusión puede tener otras razones.'),
        ('abc', 'Afirmación de ejemplo: «Todos los fines de semana llueve». ¿Qué contraejemplo la refuta?', 'Un fin de semana soleado', 'Un lunes soleado', 'Un día de lluvia entre semana', 'Debe mostrar un fin de semana sin lluvia.'),
        ('abc', '¿Qué es un caso imaginado?', 'Una situación inventada para probar una idea', 'Una historia que se cuenta para entretener', 'Un dato recogido en una encuesta', 'Se usa en filosofía para ver qué diríamos si ocurriera algo; no es un dato.'),
        ('abc', '¿Cuál es un conjunto inconsistente?', '«Todo el curso aprobó la prueba» y «Rosa, del curso, reprobó la prueba»', '«Hoy es lunes» y «Mañana es martes»', '«Pedro es alto para su edad» y «Pedro juega básquetbol los sábados»', 'No pueden ser ambas verdaderas: si todo el curso aprobó, Rosa no reprobó.'),
        ('{F} Escribe una frase que corrija el texto 4 para que no sea una generalización apresurada.', 'La zapatilla de mi vecina se rompió; sería bueno revisar la experiencia de más personas con esa marca.', 'Se limita a un caso y reconoce que hacen falta más datos.'),
        ('abc', 'Caso imaginado: «Si una persona pudiera saber el futuro, ¿sería libre de cambiarlo?». ¿Para qué sirve?', 'Para probar qué entendemos por libertad', 'Para predecir cómo será el futuro', 'Para medir cuánta gente cree que puede saber el futuro', 'Es un experimento mental sobre un concepto, no un dato.'),
    ],
    ctx=('abc', 'En un debate de ejemplo alguien dice: «O estás de acuerdo con todo lo que propongo, o no te importa el curso». ¿Qué falacia comete?', 'Falsa dicotomía', 'Pendiente resbaladiza', 'Generalización apresurada', 'Reduce las opciones a dos; hay quien se interesa y discrepa.'),
    sc=[
        ('En Filosofía: ¿qué es una generalización apresurada?', 'Concluir sobre todos a partir de pocos casos', 'Se pasa de casos aislados a una regla general sin base.'),
        ('abc', '¿Qué hace un contraejemplo?', 'Muestra que una afirmación general falla con un caso', 'Prueba que una afirmación general es verdadera si se repite', 'Repite la afirmación con otras palabras', 'Un solo caso que falle basta para refutar una afirmación general.'),
        ('¿Qué es la falsa dicotomía?', 'Presentar solo dos opciones cuando hay más', 'Reduce las posibilidades a dos aunque existan intermedias.'),
    ],
    op=("Usa la {F} Para los textos 1 y 3 escribe: la falacia, qué razón falta o está fuera de lugar y una versión mejorada que sí argumente. Cierra con una pregunta que usarías como caso imaginado sobre el celular en clases.",
        "Texto 1: pendiente resbaladiza; faltan razones para cada paso; mejora: «Si se permite el celular sin reglas, podría distraer, por eso conviene fijar reglas». Texto 3: ataque a la persona; mejora: «Reciclar disminuye la basura, por eso conviene proponerlo». Caso imaginado: si nadie pudiera usar el celular, ¿qué se perdería en clases?",
        ["identifica la falacia", "explica qué falla", "reescribe con razones", "formula un caso imaginado"], ["dos análisis", "una pregunta"], ["decir que la conclusión es falsa por la falacia", "no corregir el texto"],
        "Pide que explique qué razón nueva incorporó en la versión mejorada."),
    reinforce="Inventa un ejemplo breve de cada falacia de la clase.",
    extend="Busca en una publicación o discurso de ejemplo un razonamiento y analiza si cae en alguna falacia.",
)
