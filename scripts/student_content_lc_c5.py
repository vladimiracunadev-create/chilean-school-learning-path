"""Cuaderno del estudiante, 1.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LS03 (palabras, toponimia y antroponimia culturalmente significativas) y OA LS04 (relatos e información
cultural). No se inventa ninguna palabra, nombre ni relato de un pueblo. Los textos y mapas de práctica son
originales, en castellano, creados para este cuaderno y declarados como tales. Hechos generales usados:
«mari mari» (saludo en mapuzugun), «Rapa Nui» (nombre con que se conoce a la isla y a su pueblo), «mapuche»
(pueblo). Todo lo demás lo enseña el educador/a tradicional o la comunidad.
"""
from __future__ import annotations

from student_content_lc_c1 import task, w
from student_lessons import arith, ex, register

S3, S4 = "LC01 OA LS03", "LC01 OA LS04"
NOTE = "Texto de práctica creado para este cuaderno (no pertenece a ningún pueblo)."
MAP = "Mapa de práctica (inventado): el Río Claro pasa al lado de la Escuela. El Cerro Alto está al norte de la Escuela. La Plaza está al sur."

# ------------------------------------------------------------------ LS03
register(
    S3, 1,
    materials="Hoja y lápiz. Las palabras y situaciones de práctica están escritas aquí.",
    use="Aprenderé que una palabra se entiende mejor si sé qué significa y cuándo se usa. Sirve para respetar las palabras importantes de la vida de un pueblo.",
    prior=["Sé saludar.", "Sé que hay palabras para momentos especiales."],
    explain=[
        "Hay palabras que son importantes en la vida diaria de un pueblo: saludos, agradecimientos, nombres de alimentos, de objetos o de lugares. Una palabra importante tiene un significado y una ocasión de uso. No se usa en cualquier momento.",
        "«Mari mari» es un saludo en mapuzugun. Se dice al encontrarse con alguien. Es un ejemplo de palabra que sé con seguridad: sé qué significa y cuándo se dice. Con otras palabras no adivino: pregunto.",
        "Cuando el educador o la educadora tradicional me enseñe una palabra, anoto tres cosas: qué dice, qué significa y cuándo se usa. También anoto quién me la enseñó. Así la cuido y puedo explicar de dónde viene.",
    ],
    vocab=[("palabra significativa", "palabra importante para la vida de un pueblo"), ("ocasión de uso", "momento en que se dice"), ("saludo", "palabra para encontrarse con alguien"), ("fuente", "persona que me la enseñó"), ("situación", "momento y lugar de una conversación")],
    worked=[
        w("Significado y uso", "«Mari mari» es un saludo en mapuzugun. ¿Qué significa y cuándo se dice?", ["Es un saludo.", "Se dice al encontrarse con alguien."], "es un saludo; se dice al encontrarse"),
        w("Registrar con fuente", "Una persona de la comunidad me enseñó una palabra. ¿Qué tres datos anoto (qué dice, qué significa, cuándo se usa) y qué más?", ["Anoto los tres datos.", "También quién me la enseñó."], "quién me la enseñó"),
    ],
    mistakes=[
        {"wrong": "Usar una palabra importante solo para jugar.", "why": "Tiene una ocasión de uso para su pueblo.", "fix": "Pregunto cuándo se dice."},
        {"wrong": "Anotar la palabra sin decir quién me la enseñó.", "why": "Pierdo la fuente.", "fix": "Anoto el nombre de la fuente."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» es un saludo en mapuzugun. ¿Se dice al encontrarse o al dormir?", "al encontrarse", "Los saludos se dicen al encontrarse."),
            ex("Una palabra importante tiene significado y ocasión de uso. ¿Verdadero o falso?", "Verdadero", "Las dos cosas hay que conocer."),
            ex("¿Quién me puede enseñar palabras de una lengua indígena: el educador tradicional o mi imaginación?", "el educador tradicional", "Conoce su lengua."),
        ],
        "understand": [
            ex("¿Qué es la ocasión de uso de una palabra?", "el momento en que se dice", "Dice cuándo corresponde usarla."),
            ex("Si no sé una palabra, ¿la invento o pregunto?", "pregunto", "Inventar puede ser falso."),
            ex("¿Por qué anoto quién me enseñó una palabra?", "para cuidar la fuente", "Así sé de dónde viene."),
        ],
        "apply": [
            ex("Ordena los datos de una palabra: A) cuándo se usa B) quién me la enseñó C) qué significa. ¿Cuántos datos son en total?", "3", "Son tres datos."),
            ex("Situaciones: A) llegar a una casa B) irse a dormir. ¿En cuál usarías un saludo?", "A", "El saludo se dice al encontrarse."),
            ex("Una tarjeta dice: palabra, significado, fuente. ¿Qué dato falta si quiero saber cuándo se usa?", "la ocasión de uso", "No está en la tarjeta."),
        ],
        "reason": [
            ex("Un niño usa un saludo de un pueblo como chiste. ¿Es respetuoso?", "No", "Desconoce su ocasión de uso."),
            ex("¿Por qué las palabras importantes no se usan en cualquier momento?", "porque tienen una ocasión de uso", "Cada una se dice en su momento."),
        ],
        "challenge": [
            ex("Tengo 5 palabras de práctica y de 2 conozco la fuente. ¿De cuántas no conozco la fuente?", "3", "Cinco menos dos son tres."),
            ex("Una compañera anota «mari mari» con significado «saludo» y sin ocasión de uso. ¿Qué le falta?", "cuándo se dice", "Falta la ocasión de uso."),
        ],
    },
    context=[ex("Llega una visita a tu escuela y alguien dice «mari mari». Tu compañero responde con una palabra inventada. ¿Qué le dices?", "que escuche y pregunte", "No se inventa una palabra.")],
    selfcheck=[ex("¿Qué dos cosas sé de «mari mari»?", "es un saludo y se dice al encontrarse", "Significado y uso."), ex("¿Qué hago con una palabra que no conozco?", "pregunto", "No invento, pregunto a quien sabe."), ex("¿A quién anoto como fuente?", "a quien me la enseñó", "Cuido de dónde viene.")],
    open_task=task(
        "Haz una tarjeta de palabra con tres filas: «Qué dice», «Qué significa», «Cuándo se usa». Completa la tarjeta con «mari mari» (es un saludo en mapuzugun). Agrega una cuarta fila «Quién me la enseñó» y pregúntale al educador/a tradicional o a la comunidad si hay otra palabra de su pueblo que puedan compartirte.",
        "Qué dice: mari mari. Significa: saludo. Cuándo: al encontrarse. Quién me la enseñó: mi profesora. Pregunta: ¿qué otra palabra nos pueden compartir?",
        ["completa significado y uso", "anota la fuente", "pregunta al educador/a tradicional o a la comunidad"],
        ["tarjeta", "pregunta"],
        ["inventar significados", "olvidar la fuente"],
        "Verifica las cuatro filas; si inventó una palabra, pídele sustituirla por una pregunta.",
    ),
    reinforce="Haz una tarjeta de palabra para «gracias» en castellano con los tres datos.",
    extend="Pregunta en casa qué palabras se dicen solo en ocasiones especiales.",
)

register(
    S3, 2,
    materials="Hoja y lápiz. El mapa de práctica está escrito aquí.",
    use="Aprenderé que el nombre de un lugar se entiende mejor si lo relaciono con el territorio. Sirve para conocer y cuidar los lugares de mi país.",
    prior=["Sé decir norte y sur.", "Sé que los lugares tienen nombre."],
    explain=[
        "La toponimia es el estudio de los nombres de los lugares. Los nombres de ríos, cerros, valles e islas cuentan algo del territorio y de las personas que viven ahí. Muchos lugares de Chile tienen nombres que vienen de lenguas de pueblos originarios.",
        "Un ejemplo es Rapa Nui: es el nombre con que se conoce a la isla y también a su pueblo. Para entender un nombre, miro el lugar, pregunto quién lo nombró y cuál es su historia. No adivino el significado.",
        "Hoy practico con un mapa inventado en castellano para aprender a relacionar un nombre con un lugar. Con nombres reales de un territorio, pregunto al educador o a la educadora tradicional o a la comunidad.",
    ],
    vocab=[("toponimia", "nombres de los lugares"), ("territorio", "lugar donde vive y se desarrolla un pueblo"), ("río", "agua que corre"), ("cerro", "elevación del terreno"), ("Rapa Nui", "nombre de la isla y del pueblo rapanui")],
    worked=[
        w("Nombre y lugar", f"{MAP} ¿Qué pasa al lado de la Escuela?", ["Leo el mapa.", "Dice: el Río Claro pasa al lado de la Escuela."], "el Río Claro"),
        w("Dirección", f"{MAP} ¿Qué está al norte de la Escuela?", ["Busco norte.", "Dice: el Cerro Alto."], "el Cerro Alto"),
    ],
    mistakes=[
        {"wrong": "Inventar qué significa el nombre de un lugar.", "why": "Puedo equivocarme.", "fix": "Pregunto quién lo nombró."},
        {"wrong": "Cambiar el nombre de un lugar por otro que me gusta más.", "why": "El nombre tiene historia.", "fix": "Uso el nombre que usan las personas del lugar."},
    ],
    tiers={
        "recovery": [
            ex(f"{MAP} ¿Cómo se llama el río?", "Río Claro", "Lo dice el mapa."),
            ex(f"{MAP} ¿Cómo se llama el cerro?", "Cerro Alto", "Lo dice el mapa."),
            ex("Rapa Nui es el nombre de una isla. ¿Verdadero o falso?", "Verdadero", "Es la isla en el océano Pacífico."),
        ],
        "understand": [
            ex("¿Qué es la toponimia?", "los nombres de los lugares", "Estudia cómo se llaman los lugares."),
            ex("Verdadero o falso: puedo adivinar qué significa un nombre de lugar.", "Falso", "Hay que preguntar a quien sabe."),
            ex("¿Rapa Nui es solo el nombre de la isla?", "No, también del pueblo", "Nombra a la isla y a su pueblo."),
        ],
        "apply": [
            ex(f"{MAP} ¿Qué está al sur de la Escuela?", "la Plaza", "El mapa lo dice."),
            ex(f"{MAP} ¿Cuántos lugares nombra el mapa además de la Escuela?", "3", "Río Claro, Cerro Alto y Plaza."),
            ex(f"{MAP} ¿Qué lugar está más cerca del Río Claro: la Escuela o el Cerro Alto?", "la Escuela", "El río pasa al lado de la Escuela."),
        ],
        "reason": [
            ex("Un niño dice que el Cerro Alto debería llamarse otro nombre solo porque le gusta. ¿Qué le dices?", "que el nombre tiene historia", "No se cambia por gusto."),
            ex("¿A quién pregunto por la historia de un nombre real de un lugar?", "al educador tradicional o a la comunidad", "Ellos la conocen."),
        ],
        "challenge": [
            ex(f"{MAP} Si caminas de la Plaza a la Escuela y luego al Cerro Alto, ¿hacia qué direcciones caminas?", "norte y norte", "La Plaza está al sur y el cerro al norte de la Escuela."),
            ex(f"{MAP} ¿Cuántos nombres de lugar contienen la palabra «Río» o «Cerro»?", "2", "Río Claro y Cerro Alto."),
        ],
    },
    context=[ex("Tu familia pasea por un valle con un nombre que no entienden. ¿Qué hacen: inventar el significado o preguntar a alguien del lugar?", "preguntar a alguien del lugar", "Quien vive allí conoce la historia.")],
    selfcheck=[ex("¿De qué trata la toponimia: de lugares o de animales?", "de lugares", "Estudia los nombres de los lugares."), ex("¿Adivino qué significa el nombre de un lugar?", "No", "Pregunto a quien lo conoce."), ex("¿Quién conoce la historia del nombre de un lugar?", "las personas del territorio", "Viven y cuentan allí.")],
    open_task=task(
        "Dibuja el mapa de práctica: la Escuela en el centro, el Río Claro al lado, el Cerro Alto al norte y la Plaza al sur. Escribe el nombre de cada lugar. Después escribe una pregunta para el educador/a tradicional o la comunidad sobre el nombre de un lugar real de tu zona.",
        "Dibujé la Escuela, el río, el cerro arriba y la plaza abajo. Pregunta: ¿qué historia tiene el nombre de nuestro cerro?",
        ["ubica bien los lugares", "no inventa significados", "pregunta al educador/a tradicional o a la comunidad"],
        ["mapa dibujado", "pregunta"],
        ["confundir norte y sur", "inventar significados"],
        "Revisa el norte y el sur; si inventó un significado, cámbialo por pregunta.",
    ),
    reinforce="Nombra cuatro lugares de tu barrio y dónde están.",
    extend="Pregunta en casa por qué se llama así un lugar que conocen.",
)

register(
    S3, 3,
    materials="Hoja y lápiz. Los casos están escritos aquí.",
    use="Aprenderé que los nombres de las personas pueden llevar historia. Sirve para respetar los nombres propios y su origen.",
    prior=["Sé decir mi nombre.", "Sé que cada persona tiene una familia."],
    explain=[
        "La antroponimia es el estudio de los nombres de las personas. En muchas culturas, un nombre guarda historia: puede recordar a un familiar, un lugar o un momento importante. Por eso un nombre merece respeto.",
        "Los nombres de personas de pueblos originarios pueden tener una historia que su familia y su comunidad conocen. No adivino qué significa el nombre de otra persona. Si quiero saberlo, se lo pregunto con amabilidad, y la persona decide si lo cuenta.",
        "Tampoco comparto datos privados de nadie. Hoy practico con nombres de práctica: Rosa, Pedro y Elena. Con nombres reales, pregunto con respeto y acepto la respuesta.",
    ],
    vocab=[("antroponimia", "nombres de las personas"), ("nombre propio", "nombre de una persona"), ("historia", "lo que pasó y se recuerda"), ("respeto", "tratar con cuidado"), ("privado", "que cada persona decide si lo cuenta")],
    worked=[
        w("Pronunciar bien el nombre", "Una compañera se llama Elena. ¿Cómo la llamo?", ["Escucho cómo dice su nombre.", "Lo repito igual."], "Elena, como ella lo dice"),
        w("Preguntar con respeto", "Quiero saber por qué alguien se llama así. ¿Qué pregunto?", ["Pregunto con amabilidad.", "Acepto si no quiere contarlo."], "¿Te gustaría contarme la historia de tu nombre?"),
    ],
    mistakes=[
        {"wrong": "Burlarme del nombre de alguien.", "why": "Su nombre tiene valor.", "fix": "Lo digo con respeto."},
        {"wrong": "Insistir cuando alguien no quiere contar su historia.", "why": "Es privada.", "fix": "Acepto y agradezco."},
    ],
    tiers={
        "recovery": [
            ex("El nombre de una persona, ¿merece respeto?", "Sí", "Es parte de su identidad."),
            ex("Rosa, Pedro y Elena son nombres de personas. ¿Cuántos nombres son?", "3", "Cuento uno por cada nombre."),
            ex("Si alguien no quiere contar la historia de su nombre, ¿insisto?", "No", "Se acepta su respuesta."),
        ],
        "understand": [
            ex("¿Qué es la antroponimia?", "los nombres de las personas", "Estudia cómo se llaman las personas."),
            ex("Verdadero o falso: puedo adivinar la historia del nombre de alguien.", "Falso", "Debe contarla la persona o su familia."),
            ex("¿Quién decide si cuenta la historia de su nombre?", "la persona", "Es su historia."),
        ],
        "apply": [
            ex("Elige la forma amable de preguntar: A) «¿Te gustaría contarme por qué te llamas así?» B) «Tu nombre es raro».", "A", "A pregunta con respeto."),
            ex("Una persona dice cómo se pronuncia su nombre. ¿Lo repito igual?", "Sí", "Así lo respeto."),
            ex("Tres compañeros: Rosa, Pedro, Elena. ¿Cuántas letras tiene el nombre más corto (Rosa, Pedro, Elena)?", "4", "Rosa tiene cuatro letras."),
        ],
        "reason": [
            ex("Un niño se ríe del nombre de otro. ¿Qué le dices?", "que lo respete", "El nombre tiene valor."),
            ex("¿Por qué no cuento la historia del nombre de otra persona sin permiso?", "porque es privada", "Ella decide si la comparte."),
        ],
        "challenge": [
            ex("Nombres: Rosa, Pedro, Elena, Ana. ¿Cuántos tienen más de 4 letras?", "2", "Pedro y Elena."),
            ex("Una compañera cuenta que su nombre recuerda a su abuela. ¿Qué parte de la historia nos dio: a quién recuerda o dónde nació?", "a quién recuerda", "Mencionó a su abuela."),
        ],
    },
    context=[ex("Llega una niña nueva con un nombre que no conoces. ¿Qué haces: pedirle que te enseñe cómo se dice o cambiarlo por otro?", "pedirle que me enseñe cómo se dice", "Respeto su nombre.")],
    selfcheck=[ex("¿Qué es un nombre propio?", "el nombre de una persona", "Identifica a alguien."), ex("¿Quién decide contar la historia de su nombre?", "la persona", "La historia es suya."), ex("¿Me burlo de un nombre?", "No", "Todo nombre se respeta.")],
    open_task=task(
        "Escribe en tu cuaderno tres cosas sobre un nombre de práctica: A) Rosa B) Pedro C) Elena. Escribe cuántas letras tiene, cuántas sílabas y una frase amable para preguntar por su historia. Después pregunta al educador/a tradicional o a una persona de la comunidad cómo se cuidan los nombres en su pueblo.",
        "Rosa: 4 letras, 2 sílabas. Frase: ¿Te gustaría contarme la historia de tu nombre? Pregunta: ¿cómo cuidan los nombres en su pueblo?",
        ["cuenta bien letras y sílabas", "pregunta con amabilidad", "pregunta al educador/a tradicional o a la comunidad"],
        ["escritura", "pregunta"],
        ["burlarse", "adivinar historias"],
        "Revisa el conteo (Rosa 4 letras y 2 sílabas; Pedro 5 y 2; Elena 5 y 3).",
    ),
    reinforce="Cuenta las letras de tu nombre y de dos personas de tu familia.",
    extend="Pregunta con amabilidad en casa de dónde viene un nombre de tu familia y escucha la respuesta.",
)

register(
    S3, 4,
    materials="Hoja y lápiz. Los diálogos de práctica están escritos aquí.",
    use="Aprenderé a usar una expresión breve solo cuando sé que es correcta y en el momento que corresponde. Sirve para comunicarme con respeto.",
    prior=["Sé saludar.", "Sé que «mari mari» es un saludo en mapuzugun."],
    explain=[
        "Una interacción breve es una conversación corta: un saludo, un gracias, una despedida. Cuando el educador o la educadora tradicional me enseña una expresión, puedo usarla en el momento correcto y con quien corresponde.",
        "La expresión que sé con seguridad es «mari mari», que se dice al saludar. No la uso para burlarme ni para cualquier otra cosa. Si no estoy seguro de una expresión, no la uso: la pregunto.",
        "Un diálogo cuidado tiene tres pasos: escucho a la otra persona, respondo con lo que sé y agradezco. Si me da un consejo o una corrección, lo acepto. Así aprendo con respeto.",
    ],
    vocab=[("diálogo", "conversación entre dos personas"), ("expresión", "frase corta que se dice"), ("corrección", "ayuda para decir mejor"), ("agradecer", "decir gracias"), ("momento correcto", "situación en que se usa")],
    worked=[
        w("Saludo en su momento", "Una visita llega a tu sala. ¿Cuándo corresponde decir «mari mari»?", ["Es un saludo.", "Se dice al llegar la visita."], "al llegar la visita"),
        w("Aceptar una corrección", "El educador te corrige cómo decir el saludo. ¿Qué haces?", ["Escucho.", "Repito despacio.", "Agradezco."], "escucho, repito y agradezco"),
    ],
    mistakes=[
        {"wrong": "Decir «mari mari» como broma.", "why": "Es un saludo y no un chiste.", "fix": "Lo digo solo al saludar."},
        {"wrong": "Enojarme con la corrección.", "why": "Me ayuda a aprender.", "fix": "Agradezco y repito."},
    ],
    tiers={
        "recovery": [
            ex("«Mari mari» se dice al saludar. ¿Verdadero o falso?", "Verdadero", "Es un saludo."),
            ex("Si me corrigen, ¿me enojo o agradezco?", "agradezco", "La corrección ayuda."),
            ex("¿Cuántos pasos tiene un diálogo cuidado: 2 o 3?", "3", "Escucho, respondo y agradezco."),
        ],
        "understand": [
            ex("¿Cuándo uso una expresión de otra lengua: cuando estoy seguro o cuando no sé?", "cuando estoy seguro", "Si dudo, pregunto."),
            ex("¿Es respetuoso usar «mari mari» como broma?", "No", "Se usa para saludar."),
            ex("Verdadero o falso: una corrección es una ayuda.", "Verdadero", "Me permite aprender."),
        ],
        "apply": [
            ex("Ordena: A) agradezco B) escucho C) respondo. Escribe 3 letras.", "B, C, A", "Primero escucho, luego respondo y agradezco."),
            ex("Situaciones: A) llega una visita B) dibujo solo en mi puesto. ¿En cuál digo «mari mari»?", "A", "Es un saludo."),
            ex("Diálogo: «Mari mari». «Mari mari. ¿Cómo estás?». ¿Cuántas veces se dice el saludo?", "2", "Una vez cada persona."),
        ],
        "reason": [
            ex("Un niño usa «mari mari» para hacer reír a todos. ¿Qué le dices?", "que es un saludo y no un chiste", "Es una expresión para saludar con respeto."),
            ex("¿Por qué no uso expresiones que no estoy seguro de conocer?", "porque puedo equivocarme", "Mejor pregunto antes."),
        ],
        "challenge": [
            ex("En un diálogo de 4 turnos, el saludo está en el 1.º y el 2.º turno. ¿En cuántos turnos no hay saludo?", "2", "Cuatro menos dos son dos."),
            ex("El educador te corrige 1 vez y tú repites 3 veces despacio. ¿Cuántas veces dijiste la expresión (repetiste) en total?", "3", "Repetiste tres veces."),
        ],
    },
    context=[ex("Una persona mayor de la comunidad te saluda con «mari mari» en una visita a la escuela. ¿Qué haces: escuchar y responder un saludo o quedarte en silencio sin decir nada?", "escuchar y responder un saludo", "Respondo con respeto.")],
    selfcheck=[ex("¿Cuándo se dice «mari mari»?", "al saludar", "Es un saludo."), ex("¿Qué hago ante una corrección?", "agradezco", "Me ayuda a aprender."), ex("¿Qué hago si no estoy seguro de una expresión?", "pregunto", "No uso lo que no sé.")],
    open_task=task(
        "Escribe un diálogo de práctica de tres turnos: Turno 1: saludo; Turno 2: respuesta; Turno 3: gracias. Usa «mari mari» solo en el saludo. Represéntalo con alguien de casa. Pregunta al educador/a tradicional si hay otra expresión corta que puedan enseñarte y cuándo se usa.",
        "1: Mari mari. 2: Mari mari, ¿cómo estás? 3: Bien, gracias. Pregunta: ¿qué otra expresión podemos aprender y cuándo se usa?",
        ["usa «mari mari» en su momento", "agradece", "pregunta al educador/a tradicional o a la comunidad"],
        ["diálogo escrito", "representación"],
        ["usar la expresión como broma", "inventar frases"],
        "Verifica que el saludo esté al inicio; si inventó frases en otra lengua, pídele dejarlas fuera.",
    ),
    reinforce="Practica un diálogo de saludo en castellano de tres turnos.",
    extend="Cuenta a alguien de casa en qué momento se usa «mari mari».",
)

# ------------------------------------------------------------------ LS04
register(
    S4, 1,
    materials="Un adulto que lea el relato; hoja y lápiz. El relato de práctica está escrito aquí.",
    use="Aprenderé a escuchar un relato completo y a decir quiénes participan, dónde pasa y qué ocurre. Sirve para entender los relatos que cuentan los pueblos.",
    prior=["Sé escuchar un texto completo.", "Sé qué es un personaje."],
    explain=[
        "Un relato es una historia que se cuenta. Tiene personajes, un lugar y un acontecimiento, o sea, algo que pasa. Para entenderlo, lo escucho completo y después busco esas tres cosas.",
        "Muchos pueblos originarios cuentan relatos que guardan información sobre su cultura: cómo viven, qué cuidan y cómo se relacionan con la naturaleza. Esos relatos pertenecen a las comunidades. Los escucho con respeto y pregunto de qué pueblo son.",
        "Hoy practico con un relato de práctica creado para este cuaderno. Cuando el educador o la educadora tradicional comparta un relato real, buscaré también los personajes, el lugar y lo que ocurre, sin cambiar la historia.",
    ],
    vocab=[("relato", "historia que se cuenta"), ("personaje", "quien participa en la historia"), ("lugar", "dónde ocurre"), ("acontecimiento", "algo que pasa"), ("comunidad", "grupo que comparte su historia")],
    worked=[
        w("Personajes", f"{NOTE} Relato: «Rosa vivía cerca de un río. Una mañana el río se quedó sin agua. Rosa y su abuelo caminaron al cerro y movieron una piedra grande. El agua volvió a correr». ¿Quiénes son los personajes?", ["Busco a quienes actúan.", "Están Rosa y su abuelo."], "Rosa y su abuelo"),
        w("Lugar y acontecimiento", "En el mismo relato, ¿dónde pasa y qué pasa?", ["Pasa cerca de un río y en el cerro.", "Ocurre que el río se queda sin agua y vuelve a correr."], "río y cerro; el río se queda sin agua y vuelve a correr"),
    ],
    mistakes=[
        {"wrong": "Cambiar el final del relato porque no me gustó.", "why": "El relato tiene su historia.", "fix": "Cuento el final tal como es."},
        {"wrong": "Mezclar personajes de dos relatos.", "why": "Confundo la historia.", "fix": "Pienso en un relato a la vez."},
    ],
    tiers={
        "recovery": [
            ex("Un relato es una historia que se cuenta. ¿Verdadero o falso?", "Verdadero", "Eso es un relato."),
            ex(f"{NOTE} «Rosa vivía cerca de un río». ¿Cómo se llama la niña?", "Rosa", "El relato lo dice."),
            ex(f"{NOTE} «El río se quedó sin agua». ¿Qué le pasó al río?", "se quedó sin agua", "Lo dice el relato."),
        ],
        "understand": [
            ex("En Lengua y Cultura: ¿Qué es un personaje?", "quien participa en la historia", "Actúa en el relato."),
            ex("¿Qué es un acontecimiento?", "algo que pasa", "Es lo que ocurre."),
            ex("¿A quién pertenecen los relatos reales de un pueblo?", "a la comunidad", "Ella los cuida."),
        ],
        "apply": [
            ex(f"{NOTE} «Rosa y su abuelo caminaron al cerro y movieron una piedra grande». ¿Cuántos personajes actúan?", "2", "Rosa y su abuelo."),
            ex(f"{NOTE} Mismo relato. ¿Qué movieron?", "una piedra grande", "El relato lo dice."),
            ex(f"{NOTE} Mismo relato. ¿Qué pasó al final con el agua?", "volvió a correr", "El agua volvió a correr."),
        ],
        "reason": [
            ex("Pedro cuenta que Rosa encontró un tesoro. ¿Está en el relato?", "No", "El relato no habla de un tesoro."),
            ex("¿Por qué no cambio el final de un relato real de un pueblo?", "porque pertenece a la comunidad", "No me corresponde cambiarlo."),
        ],
        "challenge": [
            ex(f"{NOTE} Ordena: A) el agua vuelve B) el río se queda sin agua C) mueven la piedra. Escribe 3 letras.", "B, C, A", "Primero falta agua, luego mueven la piedra y vuelve."),
            ex(f"{NOTE} Mismo relato. ¿Cuántos lugares se nombran (río, cerro)?", "2", "Río y cerro."),
        ],
    },
    context=[ex("Tu abuelo te cuenta una historia de un pescador, su hijo y un lago. ¿Cuántos personajes hay si no cuentas el lago?", "2", "El pescador y su hijo.")],
    selfcheck=[ex("¿Qué tres cosas busco en un relato?", "personajes, lugar y acontecimiento", "Son las tres partes."), ex("¿Cambio el final?", "No", "Cuento tal como es."), ex("¿A quién pertenece un relato real?", "a su comunidad", "Ella lo cuida.")],
    open_task=task(
        "Pide a un adulto que lea el relato de práctica: «Rosa vivía cerca de un río. Una mañana el río se quedó sin agua. Rosa y su abuelo caminaron al cerro y movieron una piedra grande. El agua volvió a correr». Dibuja a los personajes, el lugar y lo que pasó. Pregunta al educador/a tradicional o a la comunidad si hay un relato real que puedan compartir y de qué pueblo es.",
        "Dibujé a Rosa y su abuelo, el cerro y el río. Pregunta: ¿qué relato de su pueblo nos pueden compartir?",
        ["identifica personajes, lugar y acontecimiento", "no cambia el relato", "pregunta al educador/a tradicional o a la comunidad"],
        ["dibujo", "pregunta"],
        ["cambiar el final", "mezclar relatos"],
        "Comprueba que aparezcan Rosa, su abuelo, el cerro y el río; si cambió el final, vuelve a escuchar.",
    ),
    reinforce="Cuenta a alguien un cuento corto con personajes, lugar y lo que pasa.",
    extend="Pide a alguien de casa que te cuente una historia y busca sus personajes.",
)

register(
    S4, 2,
    materials="Un adulto que lea el texto; hoja y lápiz. El texto de práctica está escrito aquí.",
    use="Aprenderé a encontrar un dato explícito, o sea, que el texto dice con claridad. Sirve para contar lo que dice un texto sin inventar.",
    prior=["Sé escuchar un texto completo.", "Sé contar hasta 10."],
    explain=[
        "Un dato explícito es una información que el texto dice con claridad. Por ejemplo, si el texto dice «trabajaron dos horas», el dato explícito es dos horas. No tengo que adivinarlo ni inventarlo.",
        "Para encontrar un dato, me hago una pregunta: ¿quién?, ¿qué?, ¿cuánto? o ¿dónde? Luego busco en el texto la parte que responde. Si no está, digo «el texto no lo dice».",
        "Los relatos y textos de los pueblos contienen información cultural: cómo hacen sus trabajos, qué cuidan o cómo comparten. Si el texto no explica algo, no lo invento: lo pregunto al educador o a la educadora tradicional.",
    ],
    vocab=[("dato explícito", "información que el texto dice claramente"), ("información cultural", "datos sobre cómo vive un grupo"), ("buscar", "mirar el texto para encontrar algo"), ("inventar", "decir algo que no está"), ("pregunta", "lo que quiero saber")],
    worked=[
        w("Buscar cuánto", f"{NOTE} Texto: «Tomás y su tía hicieron pan en un horno de barro. Usaron harina, agua y sal. Trabajaron dos horas y repartieron seis panes entre tres vecinos». ¿Cuántas horas trabajaron?", ["Busco «horas».", "Dice dos horas."], "2 horas"),
        w("Buscar qué", "En el mismo texto, ¿qué ingredientes usaron?", ["Busco «usaron».", "Dice harina, agua y sal."], "harina, agua y sal"),
    ],
    mistakes=[
        {"wrong": "Responder con algo que no dice el texto.", "why": "Es inventar.", "fix": "Busco la parte del texto que lo dice."},
        {"wrong": "Mezclar números del texto.", "why": "No leo con atención.", "fix": "Subrayo cada número."},
    ],
    tiers={
        "recovery": [
            ex(f"{NOTE} «Tomás y su tía hicieron pan». ¿Quién hizo pan con Tomás?", "su tía", "Lo dice el texto."),
            ex(f"{NOTE} «Hicieron pan en un horno de barro». ¿En qué hicieron pan?", "en un horno de barro", "Lo dice el texto."),
            ex("Un dato explícito es lo que el texto dice con claridad. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ],
        "understand": [
            ex("¿Qué digo si el texto no responde mi pregunta?", "el texto no lo dice", "No debo inventar."),
            ex("¿Para qué sirve la pregunta ¿cuánto?: para buscar una cantidad o un color?", "una cantidad", "Cuánto pide un número."),
            ex("¿A quién pregunto lo que el texto no explica?", "al educador tradicional", "Conoce los saberes."),
        ],
        "apply": [
            ex(f"{NOTE} «Usaron harina, agua y sal». ¿Cuántos ingredientes usaron?", "3", "Harina, agua y sal."),
            ex(f"{NOTE} «Repartieron seis panes entre tres vecinos». ¿Cuántos panes dieron a cada vecino?", "2", "Seis panes entre tres vecinos dan dos cada uno."),
            ex(f"{NOTE} «Trabajaron dos horas». Si trabajan una hora más, ¿cuántas horas serían en total?", "3", "Dos horas más una hora son tres horas."),
        ],
        "reason": [
            ex("Lola dice que usaron huevos. ¿Está en el texto?", "No", "El texto no lo menciona."),
            ex("¿Por qué subrayo los números del texto?", "para no mezclarlos", "Me ayuda a responder bien."),
        ],
        "challenge": [
            ex(f"{NOTE} «Repartieron seis panes entre tres vecinos». Si llegan 6 vecinos con 6 panes, ¿cuántos panes recibe cada uno?", "1", "Seis panes entre seis vecinos es uno cada uno."),
            arith(f"{NOTE} Si cada pan lleva 2 tazas de harina, ¿cuántas tazas se usan para los 6 panes?", "2*6", "Se repite 2 tazas seis veces."),
        ],
    },
    context=[ex("Tu abuela te cuenta que preparó dos ollas de sopa para cuatro vecinos. ¿Cuántos datos con número te dijo?", "2", "Dos ollas y cuatro vecinos.")],
    selfcheck=[ex("En Lengua y Cultura de los Pueblos Originarios, ¿qué es un dato explícito?", "lo que el texto dice con claridad", "Está escrito en el texto."), ex("¿Qué digo si el dato no está en el texto?", "el texto no lo dice", "No invento, lo reconozco."), ex("¿A quién pregunto lo que no explica el texto?", "al educador tradicional o a la comunidad", "Ellos saben más.")],
    open_task=task(
        "Pide a un adulto que lea el texto de práctica: «Tomás y su tía hicieron pan en un horno de barro. Usaron harina, agua y sal. Trabajaron dos horas y repartieron seis panes entre tres vecinos». Responde por escrito: ¿cuántas horas trabajaron? ¿qué ingredientes usaron? ¿cuántos vecinos hay? Escribe además una pregunta para el educador/a tradicional sobre cómo se hacen alimentos en su pueblo.",
        "Dos horas. Harina, agua y sal. Tres vecinos. Pregunta: ¿qué alimentos se preparan en su pueblo?",
        ["responde con datos del texto", "no inventa", "pregunta al educador/a tradicional o a la comunidad"],
        ["respuestas escritas", "pregunta"],
        ["inventar datos", "mezclar números"],
        "Verifica las tres respuestas (2 horas; harina, agua y sal; 3 vecinos).",
    ),
    reinforce="Escucha un cuento corto y di un dato que el texto dice claramente.",
    extend="Pregunta en casa cómo se prepara un alimento y anota un dato que te digan.",
)

register(
    S4, 3,
    materials="Un adulto que lea el texto; hoja y lápiz. El texto de práctica está escrito aquí.",
    use="Aprenderé a conectar el relato con algo que viví sin reemplazar lo que dice el relato. Sirve para entender mejor y respetar la historia.",
    prior=["Sé contar algo que me pasó.", "Sé encontrar datos explícitos."],
    explain=[
        "Relacionar un relato con mi experiencia es pensar: ¿cuándo me pasó algo parecido? Eso me ayuda a entender. Pero mi experiencia no reemplaza al relato: el relato dice lo suyo y yo cuento lo mío.",
        "Para no mezclar, uso dos frases. «El relato dice…» para lo que está en el texto. «A mí me pasó…» para lo mío. Así se nota qué es de quién. También cuido que mi experiencia no sea privada de otra persona.",
        "Con relatos de pueblos originarios, conecto con respeto. No digo que su historia es igual a la mía ni que sé todo de su cultura. Digo «me recuerda…» y pregunto lo que no sé.",
    ],
    vocab=[("experiencia", "algo que viví"), ("conectar", "unir dos cosas"), ("reemplazar", "poner una cosa en el lugar de otra"), ("parecido", "casi igual"), ("privado", "que cada persona decide si cuenta")],
    worked=[
        w("Dos frases", f"{NOTE} Relato: «La abuela Elena tejió una manta para el invierno». Me recuerda que mi abuela me tejió un gorro. ¿Qué frase uso para el relato y cuál para mí?", ["Para el relato: «El relato dice…».", "Para mí: «A mí me pasó…»."], "«El relato dice…» y «A mí me pasó…»"),
        w("No reemplazar", "Si digo «el relato dice que mi abuela tejió un gorro», ¿qué hice mal?", ["Puse mi experiencia en el relato.", "El relato habla de una manta."], "mezclé mi experiencia con el relato"),
    ],
    mistakes=[
        {"wrong": "Decir que el relato cuenta mi experiencia.", "why": "Mezclo mi historia con la del relato.", "fix": "Uso las dos frases."},
        {"wrong": "Contar un secreto de otra persona.", "why": "Es privado.", "fix": "Cuento solo lo mío."},
    ],
    tiers={
        "recovery": [
            ex("Mi experiencia es algo que yo viví. ¿Verdadero o falso?", "Verdadero", "Es algo que viví yo."),
            ex(f"{NOTE} «La abuela Elena tejió una manta». ¿Qué tejió?", "una manta", "Lo dice el relato."),
            ex("¿Con qué frase empiezo lo que dice el relato: «El relato dice…» o «A mí me pasó…»?", "«El relato dice…»", "Es para lo que está en el texto."),
        ],
        "understand": [
            ex("¿Mi experiencia reemplaza al relato?", "No", "Son cosas distintas."),
            ex("¿Qué hago con un secreto de otra persona?", "no lo cuento", "Es privado de esa persona."),
            ex("¿Por qué uso dos frases distintas?", "para separar el texto de mi experiencia", "Se nota qué es de quién."),
        ],
        "apply": [
            ex(f"{NOTE} «La abuela Elena tejió una manta». Elige lo que dice el relato: A) tejió una manta B) tejió un gorro.", "A", "El relato dice manta."),
            ex("Elige lo que es mi experiencia: A) La abuela Elena tejió una manta B) mi abuela me tejió un gorro.", "B", "Habla de mi vida."),
            ex("Ordena: A) vuelvo al relato B) digo qué dice el relato C) cuento lo mío. Escribe 3 letras.", "B, C, A", "Relato, mi experiencia y vuelvo."),
        ],
        "reason": [
            ex("Marta cuenta una historia familiar de su vecino sin permiso. ¿Está bien?", "No", "Es privada del vecino."),
            ex("¿Por qué no digo que sé todo de la cultura de un pueblo por un relato?", "porque un relato es una parte", "No cubre toda la cultura."),
        ],
        "challenge": [
            ex(f"{NOTE} Relato: «Elena tejió una manta en el invierno». Un niño dice «Elena tejió una manta en el verano». ¿Qué dato cambió?", "la estación", "Cambió invierno por verano."),
            ex("Una niña usa «El relato dice…» dos veces y «A mí me pasó…» una vez. ¿Cuántas frases usó en total?", "3", "Dos más una son tres."),
        ],
    },
    context=[ex("Después de un relato sobre tejidos, tu compañero cuenta cómo su tía tejió una bufanda. ¿Qué frase debe usar para ese dato: «A mí me pasó» o «El relato dice»?", "«A mí me pasó»", "Es su experiencia, no del relato.")],
    selfcheck=[ex("¿Qué frase uso para el texto?", "«El relato dice…»", "Es para lo que está escrito."), ex("¿Qué frase uso para lo mío?", "«A mí me pasó…»", "Es mi experiencia."), ex("¿Cuento secretos ajenos?", "No", "Son privados de otras personas.")],
    open_task=task(
        "Pide a un adulto que lea: «La abuela Elena tejió una manta para el invierno». Escribe dos frases: «El relato dice…» y «A mí me pasó…». Dibuja la manta del relato y, aparte, algo tuyo parecido. Pregunta al educador/a tradicional o a la comunidad cómo se conectan los relatos del pueblo con la vida de hoy.",
        "El relato dice que la abuela tejió una manta. A mí me pasó que mi abuela me tejió un gorro. Pregunta: ¿cómo se usa hoy ese saber?",
        ["separa relato y experiencia", "usa las dos frases", "pregunta al educador/a tradicional o a la comunidad"],
        ["frases escritas", "dibujos"],
        ["mezclar", "contar datos privados de otros"],
        "Revisa que las dos frases estén separadas; si mezcló, ayúdale a dividirlas.",
    ),
    reinforce="Elige un cuento y di una frase «El relato dice…» y otra «A mí me pasó…».",
    extend="Explica a alguien de casa por qué no se mezcla el relato con la experiencia propia.",
)

register(
    S4, 4,
    materials="Un adulto que lea el texto; hoja y lápiz. El texto de práctica está escrito aquí.",
    use="Aprenderé a explicar lo que aprendí de un relato y a reconocer lo que debo preguntar. Sirve para comunicar con honestidad y respeto.",
    prior=["Sé buscar datos explícitos.", "Sé separar relato y experiencia."],
    explain=[
        "Después de escuchar un relato, puedo contar qué aprendí. Digo lo que el relato dice y reconozco lo que no sé. Reconocer límites es una forma de ser honesto.",
        "Un buen cierre tiene tres partes: lo que aprendí, de dónde viene el relato y qué quiero preguntar. Por ejemplo: «Aprendí que juntar leña seca ayuda en el invierno. Es un relato de práctica. Quiero preguntar qué hacen en mi comunidad en el invierno».",
        "Los límites existen porque un solo relato no cuenta toda una cultura. Mi tarea es aprender un poco, agradecer y preguntar al educador o a la educadora tradicional o a la comunidad.",
    ],
    vocab=[("aprendizaje", "lo que aprendí"), ("límite", "lo que todavía no sé"), ("honesto", "que dice la verdad"), ("cierre", "final de lo que cuento"), ("agradecer", "decir gracias")],
    worked=[
        w("Tres partes", f"{NOTE} Relato: «Marta y su papá juntaron leña seca para el invierno». ¿Qué aprendí?", ["Leo el relato.", "Marta y su papá juntaron leña seca.", "Sirve para el invierno."], "que juntaron leña seca para el invierno"),
        w("Reconocer un límite", "No sé cómo se junta la leña en mi comunidad. ¿Qué digo?", ["Digo «no sé».", "Pregunto al educador tradicional."], "«No sé; lo voy a preguntar»"),
    ],
    mistakes=[
        {"wrong": "Decir «ya sé todo de esa cultura».", "why": "Un relato es solo una parte.", "fix": "Digo lo que aprendí y lo que me falta."},
        {"wrong": "No agradecer.", "why": "Olvido a quien compartió.", "fix": "Termino con un gracias."},
    ],
    tiers={
        "recovery": [
            ex("Un buen cierre tiene aprendizaje, procedencia y pregunta. ¿Cuántas partes son?", "3", "Son tres partes."),
            ex("¿Es honesto decir «no sé» cuando no sé?", "Sí", "Reconozco mis límites."),
            ex(f"{NOTE} «Marta y su papá juntaron leña seca». ¿Qué juntaron?", "leña seca", "Lo dice el relato."),
        ],
        "understand": [
            ex("¿Un relato cuenta toda la cultura de un pueblo?", "No", "Es una parte."),
            ex("¿Qué es un límite al aprender?", "lo que todavía no sé", "Reconozco que me falta."),
            ex("¿A quién agradezco al terminar?", "a quien compartió el relato", "Reconozco su aporte."),
        ],
        "apply": [
            ex(f"{NOTE} «Marta y su papá juntaron leña seca para el invierno». Elige lo que aprendí: A) la leña sirve para el invierno B) el invierno es cálido.", "A", "A resume el relato."),
            ex("Ordena: A) pregunta B) aprendizaje C) procedencia. ¿Qué letra va primero en el cierre?", "B", "Se empieza con el aprendizaje."),
            ex("Una frase dice: «Aprendí que juntaron leña. Es un relato de práctica. ¿Cómo la usan hoy?». ¿Cuántas partes tiene?", "3", "Tiene aprendizaje, procedencia y pregunta."),
        ],
        "reason": [
            ex("Alguien dice «con este relato ya conozco al pueblo completo». ¿Qué le dices?", "que un relato es solo una parte", "Falta mucho por aprender."),
            ex("¿Por qué agradecer es importante?", "porque reconoce a quien enseñó", "Valora su aporte."),
        ],
        "challenge": [
            ex("Dos frases: A) «Ya sé todo» B) «Aprendí esto y quiero preguntar aquello». ¿Cuál reconoce límites?", "B", "B pide más información."),
            ex("Una respuesta tiene solo el aprendizaje y un gracias. ¿Cuántas de las 3 partes del cierre tiene (aprendizaje, procedencia, pregunta)?", "1", "El gracias es un buen agregado, pero solo el aprendizaje es una de las 3 partes."),
        ],
    },
    context=[ex("Una persona mayor de la comunidad comparte un relato en tu escuela. Ahora haces tu cierre. ¿Con qué parte empiezas: aprendizaje, procedencia o pregunta?", "el aprendizaje", "El cierre empieza con lo que aprendí.")],
    selfcheck=[ex("¿Qué tres partes tiene un buen cierre?", "aprendizaje, procedencia y pregunta", "Son las tres."), ex("Si me falta un dato sobre el relato, ¿qué digo?", "no sé y lo voy a preguntar", "Soy honesto y pregunto."), ex("¿Un relato cuenta toda la cultura?", "No", "Es una parte.")],
    open_task=task(
        "Pide a un adulto que lea: «Marta y su papá juntaron leña seca para el invierno». Escribe tu cierre en tres partes: lo que aprendí, de dónde viene el relato (relato de práctica) y una pregunta. Además escribe una cosa que no sabes. Presenta tu pregunta al educador/a tradicional o a la comunidad.",
        "Aprendí que juntaron leña seca para el invierno. Es un relato de práctica. Pregunta: ¿qué hacen en su pueblo en el invierno? No sé cómo lo hacen en mi comunidad.",
        ["incluye aprendizaje, procedencia y pregunta", "reconoce un límite", "pregunta al educador/a tradicional o a la comunidad"],
        ["escrito o dicho en voz alta"],
        ["decir que lo sabe todo", "no agradecer"],
        "Revisa las tres partes y el límite; si falta el gracias, agrégalo.",
    ),
    reinforce="Cuenta lo que aprendiste hoy y una pregunta que te quedó.",
    extend="Enseña a alguien de casa las tres partes del cierre.",
)
