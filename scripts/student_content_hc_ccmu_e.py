"""Creación y composición musical 3.º y 4.º medio HC: OAC-05 (argumentar juicios estéticos a partir de análisis y apreciaciones personales). Obras y juicios inventados; sin posturas partidistas."""
from __future__ import annotations

from hc_ccmu_common import CLAVE, build

O5 = "AR-CCMU-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obra y enunciados de ejemplo, inventados). Obra «Ceniza» (de ejemplo): cuarteto de cuerdas; 60 pulsos por minuto; compás de 4 pulsos; una melodía descendente de 4 compases que se repite tres veces, cada vez más suave; termina con un silencio largo. "
     "Propósito expresivo declarado por quien la compuso: transmitir la sensación de apagarse. "
     "Enunciados: E1 «La melodía desciende y se repite tres veces, cada vez más suave.» E2 «Eso transmite una sensación de apagarse.» E3 «Me gusta.» "
     "E4 «La obra es valiosa porque su repetición cada vez más suave logra, con pocos medios, la sensación de apagarse que busca.» E5 «Es la mejor obra de todas.»")
build(
    O5, 1, F,
    use="Aprenderé a distinguir una descripción, una interpretación, un gusto personal y un juicio estético argumentado sobre una obra, para empezar a opinar con razones.",
    prior=["Sé describir con evidencia.", "Sé interpretar el efecto de una obra.", "Sé que una opinión necesita razones."],
    explain=[
        "Sobre una obra se pueden decir cuatro tipos de cosas. Una descripción anota rasgos comprobables («la melodía se repite tres veces»). Una interpretación propone el efecto que produce («transmite la sensación de apagarse»). Un gusto personal expresa preferencia sin dar razones («me gusta»). Un juicio estético argumentado valora la obra, dice cuánto valor tiene y explica por qué, apoyándose en rasgos y en el propósito de la obra.",
        "Un juicio estético tiene tres partes: una afirmación de valor («la obra es valiosa» o «tiene poco valor»), una razón (por qué) y una evidencia (el rasgo de la obra que apoya la razón). Puede ser positivo o negativo: «tiene poco valor porque no logra su propósito» también es un juicio argumentado si da razones. Lo que no es un juicio argumentado es un gusto sin razones o un elogio vacío como «es la mejor».",
        "La apreciación personal, lo que cada persona siente al escuchar, es válida como experiencia, pero no reemplaza al análisis. El juicio estético une ambas cosas: declara la apreciación y la apoya en el análisis de rasgos. Todos los ejemplos de este cuaderno son de obras inventadas, descritas por escrito.",
    ],
    vocab=[("juicio estético", "valoración razonada de una obra que dice cuánto valor tiene y por qué"), ("descripción", "anotación de rasgos comprobables"), ("interpretación", "propuesta del efecto que produce una obra"),
           ("gusto personal", "preferencia que no da razones"), ("evidencia", "rasgo de la obra que apoya una razón"), ("apreciación personal", "lo que una persona siente o piensa al escuchar")],
    worked=[
        ("Clasificar un enunciado", "Sobre una pieza ficticia se dice: «El tempo es lento y la melodía usa notas largas». ¿Es descripción, interpretación, gusto o juicio argumentado?",
         ["Se refiere al tempo y a las notas, rasgos que se pueden comprobar.", "No propone un efecto ni un valor: es una descripción."],
         "Descripción"),
        ("Completar un juicio", "Una frase dice «la pieza es valiosa». Se le agrega: «porque su melodía de notas largas logra la calma que busca». ¿Qué partes del juicio aparecen ahora?",
         ["Hay una afirmación de valor: «es valiosa».", "También hay una razón («logra la calma que busca») apoyada en un rasgo: la melodía de notas largas."],
         "Afirmación, razón y evidencia"),
    ],
    mistakes=[("Creer que un juicio estético es solo «me gusta» o «no me gusta».", "Se confunde gusto con valoración razonada.", "Agrega una razón y el rasgo de la obra que la apoya."),
              ("Pensar que un juicio negativo no necesita argumentos.", "Se cree que solo hay que justificar lo positivo.", "Un juicio negativo también debe dar razones y evidencia.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un juicio estético?', 'Una valoración razonada de una obra, que dice cuánto valor tiene y por qué', 'Un dato sobre cuánto dura la obra y cuántas personas la han escuchado', 'Una regla que todas las obras de una época deben cumplir para ser valiosas', 'El juicio estético une una valoración con razones apoyadas en la obra.'),
        ('abc', '{F} El enunciado E1 es:', 'Una descripción', 'Una interpretación', 'Un gusto personal', 'E1 anota rasgos comprobables: la melodía desciende y se repite tres veces.'),
        ('abc', '{F} El enunciado E2 es:', 'Una interpretación', 'Una descripción', 'Un gusto personal', 'E2 propone el efecto que produce la obra: la sensación de apagarse.'),
        ('abc', '{F} El enunciado E3, «me gusta», es:', 'Un gusto personal sin argumento', 'Un juicio argumentado, porque dice que a la persona le gusta la obra', 'Una descripción, porque anota un rasgo comprobable de la obra', 'No da razones ni rasgos, solo una preferencia.'),
        ('=', '{F} La melodía de 4 compases de 4 pulsos se repite 3 veces a 60 pulsos por minuto. ¿Cuántos segundos dura?', '3*4*4*60//60', 'Se calculan los pulsos totales y se pasan a segundos con los pulsos por minuto.', ' s'),
        ('abc', '{F} ¿Por qué E4 es un juicio argumentado?', 'Porque afirma un valor, da una razón y se apoya en rasgos y en el propósito de la obra', 'Porque usa muchas palabras y eso siempre hace más fuerte un juicio', 'Porque dice que la obra es famosa y que muchas personas la conocen', 'E4 tiene afirmación, razón y evidencia.'),
        ('abc', '{F} ¿Qué le falta a E5, «es la mejor obra de todas», para ser un juicio argumentado?', 'Una razón apoyada en rasgos de la obra y en su propósito', 'Más adjetivos, como «increíble» o «única», para que suene más fuerte', 'Una opinión de otra persona que piense lo mismo y la repita', 'Una afirmación de valor necesita razones y evidencia.'),
        ('abc', '{F} ¿Cuál reescritura convierte E3 en un juicio argumentado?', 'Me parece valiosa porque su melodía descendente, cada vez más suave, logra la sensación de apagarse que busca', 'Me gusta mucho y la escucho siempre que puedo en mi casa', 'Me gusta porque la compuso alguien conocido y todos hablan de ella', 'Solo la primera da una razón apoyada en rasgos de la obra y en su propósito.'),
        ('{F} Rotula E1 a E5 con D (descripción), I (interpretación), G (gusto sin argumento) y J (juicio argumentado). Trata E5 como gusto sin argumento.', 'E1 D; E2 I; E3 G; E4 J; E5 G', 'E1 describe, E2 interpreta, E3 y E5 no dan razones y E4 argumenta.'),
        ('abc', 'Dos estudiantes dicen «me gusta» y «no me gusta» sobre una obra. ¿Por qué ninguno es todavía un juicio argumentado?', 'Porque ninguno da razones apoyadas en rasgos de la obra', 'Porque los juicios nunca pueden ser personales', 'Porque solo las personas expertas pueden emitir un juicio estético', 'Expresan preferencias, pero un juicio necesita razones y evidencia.'),
        ('abc', '{F} ¿Puede un juicio argumentado ser negativo?', 'Sí: valora poco la obra y da razones apoyadas en rasgos, por ejemplo que no logra su propósito', 'No: un juicio argumentado siempre debe elogiar la obra para ser respetuoso', 'No: los juicios negativos no se pueden justificar con rasgos de la obra', 'Lo que hace argumentado a un juicio son las razones y la evidencia, no que sea positivo.'),
        ('abc', '{F} Alguien dice que E4 no es un juicio, sino una simple opinión. ¿Qué respuesta es adecuada?', 'Es una opinión razonada: se apoya en rasgos y en el propósito, que otras personas pueden examinar', 'Tiene razón: toda opinión es solo gusto, aunque tenga razones y evidencia', 'Es falsa, porque un juicio nunca puede apoyarse en el propósito de una obra', 'Una opinión con razones y evidencia es un juicio que se puede discutir.'),
        ('abc', 'A una persona le gusta una obra que no logra su propósito. ¿Qué es lo más preciso?', 'Puede reconocer su gusto personal y distinguirlo de su juicio sobre el logro del propósito, que necesita razones', 'Debe decir que la obra es excelente, porque si le gusta no necesita razones', 'Debe ocultar su gusto personal para que nadie piense que no es objetiva', 'Gusto y juicio estético se distinguen: el segundo se apoya en razones.'),
    ],
    ctx=('abc', 'Una amiga te dice «esa música es mala» y no explica más. ¿Qué pregunta ayuda a convertir su opinión en un juicio argumentado?', '¿Qué rasgo de la obra te lleva a decir eso y qué esperabas que lograra?', '¿Por qué no tienes mejor gusto para elegir qué música escuchar?', '¿Cuántas personas opinan igual que tú sobre esa música tan conocida?', 'La pregunta útil pide el rasgo y el propósito, que son la base de un juicio argumentado.'),
    sc=[
        ("En Composición musical: ¿qué es un gusto personal?", "Una preferencia que no da razones", "El gusto personal expresa lo que se prefiere sin razonar."),
        ('abc', 'Las tres partes de un juicio estético argumentado son:', 'Afirmación de valor, razón y evidencia', 'Título, autor y fecha de la obra que se está valorando', 'Tempo, compás y tonalidad con que está escrita la obra', 'Valor, razón y evidencia forman el argumento.'),
        ("En Creación y composición musical: ¿Qué diferencia hay entre describir e interpretar?", "Describir anota rasgos comprobables; interpretar propone el efecto que producen", "La interpretación va un paso más allá de lo que se oye."),
    ],
    op=("Con la {F}, escribe un juicio estético argumentado sobre «Ceniza» (positivo o negativo) con una afirmación de valor, una razón y una evidencia de la ficha. Después rotula cada parte.",
        "Afirmación: «Ceniza» tiene valor. Razón: logra la sensación de apagarse que busca. Evidencia: la melodía desciende y se repite tres veces cada vez más suave. Juicio completo: «Ceniza» tiene valor porque, con una melodía que desciende y se repite cada vez más suave, logra la sensación de apagarse que busca.",
        ["incluye afirmación, razón y evidencia", "la evidencia es un rasgo de la ficha", "se relaciona con el propósito de la obra"],
        ["hoja con el juicio y sus partes rotuladas"],
        ["decir solo «me gusta»", "inventar rasgos que la ficha no dice", "no relacionar con el propósito"],
        "Pregunta: «¿qué rasgo de la obra apoya tu razón?». Si no lo menciona, pídele que lo subraye en la ficha."),
    reinforce="Escribe cuatro frases sobre una canción tuya: una descripción, una interpretación, un gusto personal y un juicio argumentado.",
    extend="Explica con un ejemplo inventado por qué dos personas pueden tener juicios distintos sobre una obra y ambos ser argumentados.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (criterios y obra de ejemplo, inventados). Criterios estéticos de la pauta del curso: "
     "C1 coherencia (los medios sirven al propósito); C2 originalidad (aporta una idea propia); C3 unidad y variedad (se reconoce una idea y hay cambios); C4 expresividad (el efecto es claro); C5 dominio técnico (los recursos se usan con precisión). "
     "Cada criterio se puntúa de 0 a 2. Obra «Ceniza» (de ejemplo): cuarteto de cuerdas; una melodía descendente de 4 compases repetida 3 veces, cada vez más suave; termina con un silencio largo; propósito: transmitir la sensación de apagarse. "
     "Observaciones: O1, la dinámica baja en cada repetición; O2, la melodía es casi igual las tres veces; O3, las cuatro cuerdas tocan juntas, sin desajustes; O4, el silencio final dura 4 pulsos y el público lo percibe como un cierre. "
     "Puntajes de una persona evaluadora: C1, 2; C2, 1; C3, 1; C4, 2; C5, 2.")
build(
    O5, 2, F,
    use="Aprenderé a usar criterios estéticos, como la coherencia o la originalidad, y a combinar análisis y apreciación personal como fuentes de argumentos para juzgar una obra.",
    prior=["Sé distinguir descripción, interpretación y juicio.", "Sé analizar rasgos de una obra.", "Sé que un juicio necesita razones."],
    explain=[
        "Un criterio estético es un aspecto con el que se valora una obra. Algunos criterios son la coherencia (si los medios sirven al propósito), la originalidad (si aporta una idea propia), la unidad y variedad (si se reconoce una idea y hay cambios), la expresividad (si el efecto es claro) y el dominio técnico (si los recursos se usan con precisión). Un juicio estético se vuelve más sólido cuando nombra el criterio que usa.",
        "Las razones de un juicio provienen de tres fuentes: el análisis de la obra (rasgos comprobables), la apreciación personal (lo que quien escucha siente) y el contexto (época, procedencia, función). Un puntaje de una pauta resume un juicio, pero no lo reemplaza: se debe explicar por qué se dio cada puntaje con evidencia. La pauta también debe ser adecuada a la obra: no se penaliza un rasgo propio de un estilo, como la repetición en una música hecha para bailar.",
        "Cuando se valoran obras de épocas y procedencias distintas, se revisa que los criterios sean válidos para ambas y se declara qué criterio pesa más para el propósito de cada una. La apreciación personal se declara como tal («a mí me emociona») y se apoya en el análisis. Aquí los datos son de ejemplo y se trabaja por escrito.",
    ],
    vocab=[("criterio estético", "aspecto con el que se valora una obra"), ("coherencia", "relación adecuada entre los medios y el propósito"), ("originalidad", "aporte de una idea propia"),
           ("unidad y variedad", "equilibrio entre lo que se reconoce y lo que cambia"), ("pauta", "lista de criterios con puntajes"), ("contexto", "situación de origen y uso de una obra")],
    worked=[
        ("Relacionar observación y criterio", "Una observación sobre una pieza ficticia dice: «los tres instrumentos terminan juntos y a tiempo en cada frase». ¿A qué criterio se relaciona?",
         ["Terminar juntos y a tiempo es usar los recursos con precisión.", "Eso corresponde al dominio técnico."],
         "Dominio técnico"),
        ("Sumar una pauta", "Una pauta de ejemplo tiene 4 criterios puntuados de 0 a 3. Una obra obtiene 3, 2, 3 y 1. ¿Cuántos puntos suma y cuántos le faltan para el máximo?",
         ["Suma 3 + 2 + 3 + 1 = 9 puntos.", "El máximo es 4 × 3 = 12, así que faltan 12 − 9 = 3 puntos."],
         "9 puntos; faltan 3"),
    ],
    mistakes=[("Usar un solo criterio para valorar cualquier obra.", "Un criterio puede no ser adecuado para el estilo o el contexto de la obra.", "Elige criterios válidos para la obra y explica cuál pesa más."),
              ("Dar puntajes sin explicarlos.", "El puntaje resume un juicio que no se ve.", "Anota una razón y la evidencia de cada puntaje.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un criterio estético?', 'Un aspecto con el que se valora una obra, como la coherencia o la originalidad', 'La nota que recibe una obra después de evaluarla con una pauta', 'El nombre de la persona que compuso la obra y la fecha en que lo hizo', 'Un criterio es el aspecto desde el cual se hace la valoración.'),
        ('abc', '{F} El criterio C1, coherencia, pregunta:', 'Si los medios sirven al propósito', 'Si la obra es famosa y la conocen muchas personas del curso', 'Si dura mucho tiempo y tiene muchos compases y secciones', 'La ficha define la coherencia como la relación entre medios y propósito.'),
        ('abc', '{F} ¿Con qué criterio se relaciona la observación O3, que las cuerdas tocan juntas sin desajustes?', 'C5, dominio técnico', 'C2, originalidad', 'C3, unidad y variedad', 'Tocar juntos sin desajustes muestra precisión en el uso de los recursos.'),
        ('abc', '{F} La observación O2 dice que la melodía es casi igual las tres veces. ¿Qué indica sobre la unidad y variedad?', 'Mucha unidad y poca variedad', 'Mucha variedad y poca unidad', 'Ni unidad ni variedad', 'Si se repite casi igual, se reconoce la idea pero hay pocos cambios.'),
        ('=', '{F} ¿Cuántos puntos suman los cinco criterios puntuados por la persona evaluadora?', '2+1+1+2+2', 'Se suman los puntajes de los cinco criterios.', ' puntos'),
        ('abc', '{F} La observación O4 dice que el silencio final se percibe como un cierre. ¿Con qué criterio se relaciona?', 'C4, expresividad, porque el efecto es claro', 'C5, dominio técnico, porque suena fuerte', 'C2, originalidad, porque nadie usa silencios', 'Un efecto que el público percibe con claridad corresponde a expresividad.'),
        ('=', '{F} Con 5 criterios de 0 a 2 puntos, ¿cuántos puntos le faltan a la obra para el máximo?', '5*2-(2+1+1+2+2)', 'Se calcula el máximo posible y se resta el puntaje obtenido.', ' puntos'),
        ('abc', '{F} ¿Qué observación apoya mejor un juicio sobre coherencia (C1)?', 'O1: la dinámica baja en cada repetición, lo que sirve al propósito de apagarse', 'O3: las cuatro cuerdas tocan juntas y a tiempo, sin desajustes en la ejecución', 'O2: la melodía es casi igual las tres veces, con muy pocos cambios entre ellas', 'Bajar la dinámica en cada repetición sirve directamente al propósito de apagarse.'),
        ('abc', 'Un estudiante valora una obra de tradición oral solo con el criterio de dominio técnico, porque no hay virtuosismo. ¿Qué falla?', 'Un solo criterio no basta y debe ser adecuado a la obra y su contexto', 'Nada, porque el dominio técnico es el único criterio', 'Que no se puede valorar nada de tradición oral', 'La pauta debe ser válida para la obra y su contexto, no solo un criterio.'),
        ('abc', '{F} Alguien da 0 en originalidad a «Ceniza» porque «repetir es copiar». ¿Qué respuesta es adecuada?', 'La repetición es un procedimiento compositivo; la originalidad se juzga por la idea y su uso, no por repetir', 'Tiene razón: repetir siempre es copiar a otra obra, aunque sea dentro de la misma pieza', 'La originalidad no se puede juzgar nunca, porque depende solo del gusto de cada persona', 'La repetición dentro de una obra no es copiar a otra persona.'),
        ('abc', '{F} La pauta da 8 puntos de 10 a «Ceniza». ¿Basta ese puntaje como juicio estético?', 'No: se necesita explicar con razones y evidencia por qué se dio cada puntaje', 'Sí: un puntaje reemplaza al juicio y no necesita razones ni evidencia que lo apoyen', 'Sí, si el puntaje es mayor que 5, porque eso ya demuestra que la obra es valiosa', 'El puntaje resume el juicio, pero no explica sus razones.'),
        ('abc', 'Dos obras de épocas y procedencias distintas se valoran con la misma pauta. ¿Qué cuidado hay que tener?', 'Revisar que los criterios sean válidos para ambas y no penalizar rasgos propios de su estilo', 'Usar la pauta sin revisarla, porque los criterios sirven igual para cualquier obra', 'Dar más puntos a la obra más antigua, porque su época la hace más valiosa', 'Una pauta común debe respetar los rasgos de cada estilo y contexto.'),
        ('abc', 'Quieres combinar tu apreciación personal con el análisis. ¿Cómo lo haces?', 'Declaras la apreciación como tal y la apoyas con rasgos que analizaste', 'La escondes del texto, porque la apreciación personal no vale como razón', 'La usas como única razón y no necesitas mirar rasgos de la obra', 'La apreciación es válida como experiencia y se fortalece con el análisis.'),
    ],
    ctx=('=', 'Una pauta de ejemplo tiene 6 criterios puntuados de 0 a 2. Una obra obtiene 9 puntos. ¿Cuántos puntos le faltan para el máximo?', '6*2-9', 'Se calcula el máximo posible y se resta el puntaje obtenido.', ' puntos'),
    sc=[
        ("En Composición musical: ¿qué es la coherencia en una obra?", "La relación adecuada entre los medios y el propósito", "Una obra es coherente si lo que usa sirve a lo que busca."),
        ('abc', 'Un puntaje de una pauta se complementa con:', 'Razones y evidencia que expliquen cada puntaje', 'Otro puntaje igual que el primero, repetido por una persona distinta', 'Una opinión sin argumentos que diga si la obra le gustó a quien evalúa', 'El puntaje resume el juicio, pero necesita razones.'),
        ("¿Cuáles son las tres fuentes de razones de un juicio estético?", "El análisis, la apreciación personal y el contexto", "Las razones pueden venir de lo analizado, lo sentido y la situación de la obra."),
    ],
    op=("Con la {F}, elige dos criterios y escribe, para cada uno, una razón y una evidencia de «Ceniza». Después escribe un juicio final de dos frases que combine una apreciación personal con una razón del análisis.",
        "C1: coherencia, porque la dinámica baja en cada repetición y eso sirve al propósito de apagarse. C4: expresividad, porque el silencio final de 4 pulsos se percibe como cierre. Juicio: «A mí me conmueve el final. Considero valiosa la obra porque su melodía cada vez más suave logra la sensación de apagarse».",
        ["dos criterios con razón y evidencia", "evidencias de la ficha", "juicio que combina apreciación y análisis"],
        ["hoja con los criterios, las razones y el juicio final"],
        ["usar solo un criterio", "dar razones sin evidencia", "mezclar gusto con evidencia sin declararlo"],
        "Pregunta: «¿qué criterio usaste y qué rasgo lo apoya?». Si no responde, pídele que vuelva a las observaciones."),
    reinforce="Elige una canción que conozcas y escribe tres criterios para valorarla, con una razón de cada uno.",
    extend="Explica con un ejemplo inventado por qué no conviene usar la misma pauta, sin revisarla, para una pieza de baile y una pieza de meditación.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (obra y argumentos de ejemplo, inventados). Obra «Pasos de madera» (de ejemplo): percusión de 6 personas con objetos de madera; 120 pulsos por minuto; compás de 4 pulsos. Forma ABA: el patrón A «X . X X» se repite 8 veces; el patrón B «X X . X» se repite 8 veces; el patrón A vuelve 8 veces. "
     "Propósito: evocar un caminar que cambia de ritmo. Clave: X es un golpe y «.» un silencio; cada casilla es un pulso. "
     "Argumento 1: «Considero valiosa «Pasos de madera» porque logra evocar un caminar que cambia de ritmo. Se nota en que el patrón X . X X se repite ocho veces y luego cambia a X X . X, con un retorno final que da unidad y variedad. Alguien podría decir que repite demasiado; sin embargo, la repetición establece el caminar antes de cambiarlo.» "
     "Argumento 2: ««Pasos de madera» es buena porque a todo el curso le gustó.»")
build(
    O5, 3, F,
    use="Aprenderé a construir un argumento estético con afirmación, razón, evidencia, criterio y respuesta a una objeción, apoyado en el análisis y en una apreciación personal.",
    prior=["Sé distinguir un juicio de un gusto.", "Sé usar criterios estéticos.", "Sé analizar rasgos con evidencia."],
    explain=[
        "Un argumento estético sólido tiene varias partes. La afirmación dice cuánto valor tiene la obra. La razón explica por qué. La evidencia es el rasgo comprobable de la obra que apoya la razón. El criterio es el aspecto desde el que se valora (por ejemplo, unidad y variedad). Una objeción es una crítica posible al argumento, y responderla lo fortalece.",
        "Un buen argumento se apoya en lo que la obra hace, no en cuánta gente la prefiere. «A todo el curso le gustó» es un argumento de popularidad: dice cuántas personas opinan igual, pero no explica qué rasgo da valor a la obra. Tampoco son argumentos válidos «es antigua, por eso es mejor» o «la compuso alguien famoso»: ninguno se refiere a rasgos de la obra.",
        "Antes de escribir un argumento se decide la afirmación y se buscan en la obra dos evidencias que la apoyen. Después se escribe en orden: afirmación, razón con criterio, evidencia, objeción y respuesta. El argumento es breve y se puede revisar parte por parte. Esta clase usa obras inventadas descritas por escrito, sin audio real.",
    ],
    vocab=[("argumento", "conjunto de afirmación, razón y evidencia que defiende un juicio"), ("afirmación", "enunciado del valor que se atribuye a la obra"), ("razón", "explicación de por qué se afirma ese valor"),
           ("objeción", "crítica posible a un argumento"), ("popularidad", "cantidad de personas que prefieren una obra"), ("criterio", "aspecto desde el que se valora una obra")],
    worked=[
        ("Identificar las partes", "Un argumento ficticio dice: «La pieza vale porque su tempo lento y sus notas largas logran calma; esto se nota en que cada frase termina en una nota de cuatro pulsos». ¿Cuál es la razón y cuál la evidencia?",
         ["La razón es que el tempo lento y las notas largas logran calma.", "La evidencia es el rasgo comprobable: cada frase termina en una nota de cuatro pulsos."],
         "Razón: logran calma; evidencia: frases que terminan en notas de cuatro pulsos"),
        ("Contar golpes", "Un patrón ficticio «X X . .» se repite 6 veces. ¿Cuántos golpes suenan en total?",
         ["Cada repetición tiene 2 golpes.", "En 6 repeticiones suenan 6 × 2 = 12 golpes."],
         "12 golpes"),
    ],
    mistakes=[("Defender una obra diciendo que a mucha gente le gusta.", "La popularidad no explica qué hace la obra.", "Cita un rasgo de la obra y el criterio con que lo valoras."),
              ("No considerar ninguna objeción.", "El argumento queda débil frente a críticas razonables.", "Anticipa una objeción y respóndela con evidencia.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una objeción a un argumento?', 'Una crítica posible al argumento', 'La conclusión del argumento', 'El título de la obra', 'Una objeción cuestiona el argumento y responderla lo fortalece.'),
        ('abc', '{F} ¿Cuál es la afirmación del argumento 1?', 'Que «Pasos de madera» es una obra valiosa', 'Que la obra dura 48 segundos y tiene seis personas que la tocan', 'Que a todo el curso le gustó y por eso se vuelve valiosa', 'La primera oración afirma el valor de la obra.'),
        ('abc', '{F} ¿Cuál es la evidencia del argumento 1?', 'El patrón X . X X se repite ocho veces y luego cambia a X X . X, con un retorno final', 'Que la obra es valiosa, porque eso es lo que se afirma al comienzo', 'Que alguien podría decir que la obra repite demasiado cada patrón', 'La evidencia es el rasgo comprobable de la obra.'),
        ('abc', '{F} ¿Qué criterio estético usa el argumento 1?', 'Unidad y variedad', 'Popularidad', 'Dominio técnico', 'El texto lo nombra: el retorno da unidad y variedad.'),
        ('=', '{F} La obra tiene tres secciones de 8 repeticiones de un patrón de 4 pulsos, a 120 pulsos por minuto. ¿Cuántos segundos dura?', '3*8*4*60//120', 'Se calculan las repeticiones, los pulsos totales y luego los segundos.', ' s'),
        ('abc', '{F} ¿Cuál es la objeción que anticipa el argumento 1?', 'Que la obra repite demasiado', 'Que la obra es muy corta', 'Que la obra no usa madera', 'El argumento dice: «alguien podría decir que repite demasiado».'),
        ('abc', '{F} ¿Por qué el argumento 2 no es un argumento estético sólido?', 'Porque se apoya en la popularidad y no en rasgos de la obra', 'Porque es demasiado largo y por eso el argumento no se entiende', 'Porque usa criterios estéticos que no se pueden aplicar a una obra', 'El gusto del curso no explica qué hace valiosa a la obra.'),
        ('abc', '{F} ¿Cuál reescritura convierte el argumento 2 en un argumento con evidencia?', 'Es buena porque el cambio del patrón X . X X al X X . X hace sentir un caminar que cambia de ritmo', 'Es buena porque ganó muchos aplausos de las personas que la escucharon', 'Es buena porque está hecha de madera, un material que suena muy bien', 'La primera relaciona un rasgo con el propósito de la obra.'),
        ('=', '{F} ¿Cuántos golpes suenan en las 8 repeticiones del patrón X . X X?', '8*3', 'El patrón tiene 3 golpes y se repite 8 veces.', ' golpes'),
        ('abc', 'Un estudiante defiende una obra diciendo «es antigua, por eso es mejor». ¿Qué falla?', 'La antigüedad no es un rasgo que explique el valor estético; falta evidencia de la obra', 'Nada, porque lo antiguo siempre es mejor que lo más reciente', 'Que las obras antiguas no existen en la actualidad y no se pueden valorar', 'La época no demuestra calidad; se necesita citar rasgos.'),
        ('abc', '{F} ¿Por qué conviene responder a una objeción en el argumento?', 'Porque muestra que la crítica fue considerada y fortalece el argumento con evidencia', 'Porque alarga el texto y así se cumple el largo pedido sin esfuerzo', 'Porque elimina la afirmación y deja el argumento sin su parte principal', 'Responder objeciones hace al argumento más sólido.'),
        ('abc', '{F} Una compañera dice que el patrón B es el verdadero valor de la obra y que A no importa. ¿Qué argumento es más completo?', 'El valor está en la relación entre A y B y su retorno, porque el contraste solo se nota frente a lo que se repite', 'Solo B es valioso porque es distinto, y A no aporta nada a la obra', 'Ninguno de los dos patrones tiene valor si se repite ocho veces', 'La forma ABA depende de la relación entre secciones.'),
        ('abc', 'Antes de escribir un argumento, ¿qué conviene hacer primero?', 'Decidir la afirmación y buscar en la obra dos evidencias que la apoyen', 'Escribir cualquier razón y luego buscar datos que la apoyen, aunque no existan', 'Preguntar quién la compuso y valorarla según su fama', 'El argumento parte de una afirmación y de evidencia de la obra.'),
    ],
    ctx=('abc', 'En un taller del liceo, un grupo debe defender por escrito el valor de una pieza de ejemplo en tres líneas. ¿Qué orden de escritura es el más claro?', 'Afirmación, razón con criterio, evidencia y respuesta a una objeción', 'Evidencia, título, fecha y firma de quien escribe el argumento', 'Objeción, afirmación y título, sin incluir evidencia de la obra', 'El orden afirmación, razón, evidencia y objeción hace el argumento claro y revisable.'),
    sc=[
        ("En Composición musical: ¿qué es la evidencia en un argumento estético?", "Un rasgo comprobable de la obra que apoya la razón", "La evidencia hace comprobable el argumento."),
        ('abc', 'Decir «es buena porque a todos les gustó» es un argumento de:', 'Popularidad', 'Evidencia', 'Criterio', 'Apela a cuánta gente opina igual y no a rasgos de la obra.'),
        ("¿Por qué se anticipa una objeción?", "Para fortalecer el argumento respondiendo una crítica posible", "Responder objeciones muestra que el argumento ya fue puesto a prueba."),
    ],
    op=("Con la {F}, escribe un argumento estético de máximo cuatro frases sobre «Pasos de madera»: afirmación, razón con un criterio, una evidencia y la respuesta a una objeción. Elige tú la objeción.",
        "Considero valiosa la obra porque logra evocar un caminar que cambia de ritmo. El patrón A se repite ocho veces y luego cambia a B, y vuelve A, lo que da unidad y variedad. Alguien podría decir que cada patrón se repite demasiado; sin embargo, la repetición permite notar el cambio.",
        ["incluye afirmación, razón, criterio, evidencia y objeción", "la evidencia es de la ficha", "máximo cuatro frases"],
        ["hoja con el argumento de cuatro frases"],
        ["apoyarse en la popularidad", "no responder la objeción", "no nombrar el criterio"],
        "Pregunta: «¿qué objeción consideraste y cómo la respondes?». Si no tiene respuesta, pídele que la formule."),
    reinforce="Escribe un argumento de tres frases sobre una canción tuya, con afirmación, razón y evidencia.",
    extend="Explica con un ejemplo inventado por qué una objeción bien respondida puede fortalecer un juicio aunque no convenza a todos.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (dos juicios de ejemplo, inventados). Obra «Río quieto» (de ejemplo): pieza para flauta y guitarra; 120 pulsos por minuto; compás de 4 pulsos; la guitarra repite un patrón de 4 pulsos sin cambios durante 3 minutos; la flauta toca una melodía distinta en cada pasada. "
     "Valeria: «La obra es valiosa porque la repetición del patrón crea una base estable que deja lucir la melodía de la flauta; la unidad es su mayor logro.» "
     "Tomás: «La obra tiene poco valor porque la guitarra no cambia en tres minutos y falta variedad; se vuelve monótona.» "
     "Ambos coinciden en que la guitarra repite el patrón sin cambios durante 3 minutos.")
build(
    O5, 4, F,
    use="Aprenderé a contrastar juicios estéticos distintos sobre la misma obra, a distinguir si el desacuerdo es de hechos o de criterios y a dialogar con respeto usando evidencia.",
    prior=["Sé construir un argumento estético.", "Sé usar criterios.", "Sé dar retroalimentación respetuosa."],
    explain=[
        "Dos personas pueden valorar distinto la misma obra. Primero conviene ver si el desacuerdo es de hechos (una dice que la guitarra cambia y la otra que no) o de criterio (coinciden en los hechos, pero dan distinto peso a lo que importa, como la unidad o la variedad). Los desacuerdos de hechos se resuelven volviendo a la obra; los de criterio se resuelven conversando sobre cuál criterio pesa más para el propósito de la obra.",
        "Un diálogo respetuoso sigue reglas: se escucha el argumento completo, se cita la evidencia, se critica el argumento y no a la persona, y se reconoce lo que el otro punto de vista acierta. Atacar a la persona («tú no sabes de música») no responde al argumento. Cambiar de opinión después de un diálogo no es obligatorio: se puede matizar el juicio o mantenerlo si las razones siguen siendo sólidas.",
        "Dos juicios opuestos pueden ser ambos argumentados si cada uno se apoya en evidencia y en un criterio claro. Contrastar juicios ayuda a ver más aspectos de la obra y a afinar el propio. En este cuaderno los juicios son de ejemplo, sobre obras inventadas.",
    ],
    vocab=[("desacuerdo de hechos", "diferencia sobre lo que ocurre en la obra"), ("desacuerdo de criterio", "diferencia sobre qué aspecto importa más al valorar"), ("matizar", "ajustar un juicio sin cambiarlo del todo"),
           ("diálogo", "conversación en que se escuchan y se responden los argumentos"), ("peso de un criterio", "importancia que se da a un criterio en un juicio"), ("evidencia", "rasgo de la obra que apoya un argumento")],
    worked=[
        ("Tipo de desacuerdo", "Ana dice que una pieza ficticia tiene tres secciones y Beto dice que tiene cuatro. ¿Qué tipo de desacuerdo es y cómo se resuelve?",
         ["Discuten sobre un hecho que se puede comprobar: cuántas secciones hay.", "Se resuelve volviendo a la obra y contando las secciones."],
         "De hechos; se resuelve volviendo a la obra"),
        ("Calcular repeticiones", "Un patrón de 4 pulsos, a 60 pulsos por minuto, se repite sin cambios durante 2 minutos. ¿Cuántas veces suena?",
         ["A 60 pulsos por minuto, 4 pulsos duran 4 segundos.", "En 120 segundos caben 120 ÷ 4 = 30 repeticiones."],
         "30 veces"),
    ],
    mistakes=[("Discutir sin ver si el desacuerdo es de hechos o de criterio.", "Se pierde tiempo discutiendo algo que se resolvería mirando la obra.", "Primero comprueba los hechos; luego conversa sobre los criterios."),
              ("Responder a un argumento atacando a la persona.", "No se examina el argumento y se cierra el diálogo.", "Cita evidencia y responde a lo que dice el argumento.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es un desacuerdo de criterio?', 'Una diferencia sobre qué aspecto importa más, aunque haya acuerdo sobre los hechos', 'Una diferencia sobre cuántas secciones tiene una obra, que se resuelve contándolas', 'Una discusión sin razones, en la que cada persona repite su preferencia', 'En un desacuerdo de criterio se coincide en los hechos pero se valora distinto.'),
        ('abc', '{F} ¿En qué hecho coinciden Valeria y Tomás?', 'En que la guitarra repite el patrón sin cambios durante 3 minutos', 'En que la obra es valiosa y que la repetición es su mayor logro', 'En que la flauta tampoco cambia, así que toda la obra repite sin cambios', 'La ficha dice que ambos coinciden en ese hecho.'),
        ('abc', '{F} ¿Qué criterio pesa más en el juicio de Valeria?', 'La unidad', 'La variedad', 'La originalidad', 'Valeria dice que la unidad es el mayor logro.'),
        ('abc', '{F} ¿Qué criterio pesa más en el juicio de Tomás?', 'La variedad', 'La unidad', 'El dominio técnico', 'Tomás reprocha que falta variedad, es decir, cambios en la obra.'),
        ('=', '{F} El patrón de 4 pulsos dura 2 segundos a 120 pulsos por minuto y se repite durante 3 minutos. ¿Cuántas veces suena?', '3*60//2', 'Se pasan los minutos a segundos y se divide por la duración de cada repetición.', ' veces'),
        ('abc', '{F} ¿Qué dato de la ficha no considera el juicio de Tomás?', 'Que la flauta toca una melodía distinta en cada pasada', 'Que la guitarra repite el patrón sin cambios durante tres minutos', 'Que la obra dura tres minutos y se toca a 120 pulsos por minuto', 'Tomás no menciona los cambios de la flauta, que aportan variedad.'),
        ('abc', '{F} El desacuerdo entre Valeria y Tomás es:', 'De criterio, porque coinciden en los hechos y valoran distinto la unidad y la variedad', 'De hechos, porque dicen cosas contrarias sobre lo que hace la guitarra', 'No hay desacuerdo, porque los dos coinciden en que la obra es valiosa', 'Ambos aceptan los mismos hechos; difieren en qué criterio pesa más.'),
        ('abc', '{F} ¿Qué pregunta ayuda más a dialogar?', '¿Qué peso le das a la unidad y a la variedad en esta obra, dado su propósito?', '¿Por qué no entiendes la música como la entendemos quienes sí la estudiamos?', '¿Cuántas personas opinan como tú y cuántas como la persona que critica?', 'La pregunta útil lleva el diálogo a los criterios y al propósito.'),
        ('abc', '{F} ¿Qué evidencia podría reforzar el juicio de Tomás?', 'Señalar que, aparte de la flauta, no hay ningún otro cambio en 180 segundos', 'Decir que la obra es antigua y por eso ya no se debe valorar', 'Decir que a su curso no le gustó y que todos opinan igual', 'La evidencia refuerza el argumento con un dato de la obra.'),
        ('abc', '¿Pueden Valeria y Tomás tener ambos juicios argumentados?', 'Sí, si cada uno se apoya en evidencia y en un criterio claro, aunque lleguen a valoraciones opuestas', 'No: solo uno puede tener razones, porque las valoraciones opuestas se anulan', 'No: dos juicios opuestos nunca se pueden argumentar con evidencia de la obra', 'Un juicio es argumentado por sus razones y evidencia, no por coincidir con el otro.'),
        ('abc', '{F} Alguien responde a Tomás: «tú no sabes de música». ¿Qué falla?', 'Ataca a la persona y no responde al argumento', 'Responde bien, porque desacredita el argumento', 'Aporta evidencia de la obra', 'Un argumento se responde con evidencia, no con descalificaciones.'),
        ('abc', '{F} Tras oír a Valeria, Tomás reconoce que la flauta aporta variedad. ¿Está obligado a cambiar su juicio?', 'No necesariamente: puede matizarlo, por ejemplo diciendo que la variedad está solo en la flauta, o mantenerlo si sus razones siguen firmes', 'Sí, siempre debe cambiarlo, porque reconocer un hecho obliga a abandonar el juicio', 'No puede cambiar nada de su juicio, porque ya lo escribió y lo dijo en voz alta', 'Dialogar permite ajustar el juicio sin abandonarlo del todo.'),
        ('abc', 'En una discusión grupal sobre una obra, ¿qué regla ayuda más?', 'Escuchar sin interrumpir, citar evidencia y criticar el argumento y no a la persona', 'Hablar más fuerte para convencer y repetir el argumento hasta que el otro acepte', 'No decir nada para evitar conflictos, aunque se piense distinto del resto', 'Un diálogo respetuoso se apoya en escucha, evidencia y respeto.'),
    ],
    ctx=('abc', 'En clase hay dos juicios opuestos sobre una obra de ejemplo y el docente pide una actividad útil. ¿Cuál conviene?', 'Escribir cada juicio con su criterio y su evidencia y buscar en qué coinciden', 'Votar cuál juicio gana y descartar el otro sin revisar sus razones', 'Pedir que una persona se retracte para que el grupo vuelva a estar de acuerdo', 'Separar criterio y evidencia ayuda a ver dónde coinciden y dónde difieren.'),
    sc=[
        ("En Composición musical: ¿qué es un desacuerdo de hechos?", "Una diferencia sobre lo que ocurre en la obra, que se resuelve volviendo a ella", "Los hechos se comprueban en la obra."),
        ('abc', 'Si dos personas coinciden en los hechos y valoran distinto, el desacuerdo es de:', 'Criterio', 'Hechos', 'Notas', 'Hay acuerdo en los hechos y diferencia en lo que importa más.'),
        ("¿Es obligatorio cambiar de juicio tras un diálogo?", "No; se puede matizar o mantener si las razones siguen siendo sólidas", "El diálogo no obliga a cambiar, solo a considerar las razones."),
    ],
    op=("Con la {F}, escribe un breve diálogo de cuatro intervenciones entre Valeria y Tomás en el que cada uno cita evidencia, reconoce algo que el otro acierta y propone cómo ponerse de acuerdo sobre qué criterio pesa más.",
        "Valeria: «La base estable deja lucir la flauta». Tomás: «Es cierto, la flauta cambia, pero la guitarra no cambia en tres minutos». Valeria: «Reconozco que falta variedad en la guitarra». Tomás: «Podemos valorar la unidad de la base y la variedad de la flauta por separado».",
        ["cuatro intervenciones", "cada persona cita evidencia", "reconoce algo del otro", "no ataca a la persona"],
        ["hoja con el diálogo"],
        ["atacar a la persona", "no citar evidencia", "ceder sin razones"],
        "Pregunta: «¿qué reconoció cada persona del otro juicio?». Si nadie reconoce nada, pídele que reescriba una intervención."),
    reinforce="Escribe dos juicios opuestos sobre una canción conocida, cada uno con su criterio y su evidencia.",
    extend="Explica con un ejemplo inventado cómo un desacuerdo de criterio puede transformarse en un acuerdo de matiz.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (borrador de ejemplo, inventado). Obra «Aire de campo» (de ejemplo): voz y guitarra; cuatro estrofas con la misma melodía de cuatro notas; la dinámica no cambia; dura 3 minutos; propósito declarado: ser fácil de cantar en grupo. "
     "Borrador de juicio: «Esta obra es mala porque es muy antigua, tiene pocas visitas en internet y la compuso alguien que no estudió música.» "
     "Reescritura propuesta: «La obra logra su propósito de ser fácil de cantar en grupo porque repite una melodía de cuatro notas en las cuatro estrofas, aunque tiene poca variedad de dinámica.» "
     "El juicio final debe tener como máximo 40 palabras.")
build(
    O5, 5, F,
    use="Aprenderé a revisar y reescribir un juicio estético para quitar falacias, apoyarlo en evidencia y ajustarlo a un largo dado, dejando registro de los cambios.",
    prior=["Sé construir un argumento estético.", "Sé dialogar sobre juicios distintos.", "Sé distinguir evidencia de opinión."],
    explain=[
        "Un juicio estético se revisa como cualquier texto. Se buscan las falacias, es decir, razonamientos que parecen válidos pero no lo son. Las más comunes aquí son la antigüedad («es antigua, por eso es mala o buena»), la popularidad («tiene pocas visitas, por eso es mala»), el ataque a la persona («la compuso alguien que no estudió música») y el prejuicio contra un grupo. Ninguna se apoya en rasgos de la obra.",
        "Para reescribir se reemplaza cada falacia por un rasgo de la obra y su efecto, relacionado con el propósito. También se revisa que haya una afirmación de valor, una razón y una evidencia, y que el texto cumpla el largo pedido. Se guarda el borrador original y la reescritura, y se anota qué cambió y por qué, de modo que se vea el proceso de ajuste.",
        "Un buen juicio final es breve, claro y prudente: dice lo que se puede sostener con la obra y declara lo que es apreciación personal. Esta clase no pretende que todas las personas coincidan, sino que los juicios se puedan discutir con razones.",
    ],
    vocab=[("falacia", "razonamiento que parece válido pero no lo es"), ("reescribir", "volver a escribir un texto mejorándolo"), ("prejuicio", "juicio sobre una persona o grupo sin conocerlos"),
           ("registro de cambios", "anotación de qué se cambió y por qué"), ("prudente", "que no afirma más de lo que se puede sostener"), ("largo máximo", "cantidad de palabras que un texto no puede superar")],
    worked=[
        ("Detectar una falacia", "Un borrador ficticio dice: «La pieza es valiosa porque la compuso alguien muy famoso». ¿Qué falacia tiene?",
         ["Se apoya en quién la compuso y no en un rasgo de la pieza.", "Es un argumento de autoridad o fama, que no explica el valor de la obra."],
         "Apelación a la fama de la persona que compuso"),
        ("Contar palabras", "El texto «La pieza logra calma con notas largas» tiene 7 palabras y el máximo es 25. ¿Cuántas palabras más se pueden agregar?",
         ["Se resta lo escrito al máximo: 25 − 7.", "25 − 7 = 18 palabras."],
         "18 palabras"),
    ],
    mistakes=[("Corregir una falacia cambiándola por otra, como «tiene muchas visitas».", "La popularidad tampoco explica el valor de la obra.", "Reemplázala por un rasgo de la obra y su efecto."),
              ("No guardar el borrador al reescribir.", "No se puede mostrar el proceso ni volver atrás.", "Guarda ambas versiones y anota qué cambió.")],
    T=[
        ('abc', 'En Composición musical: ¿qué es una falacia en un juicio estético?', 'Un razonamiento que parece válido pero no se apoya en rasgos de la obra', 'Una razón basada en un rasgo de la obra y relacionada con su propósito', 'Una afirmación sin ninguna opinión que solo describe cuántas notas tiene la obra', 'Una falacia parece un argumento, pero no es válida.'),
        ('abc', '{F} «Es muy antigua» es una falacia de:', 'Antigüedad', 'Popularidad', 'Ataque a la persona', 'Se apoya en la edad de la obra y no en sus rasgos.'),
        ('abc', '{F} «Tiene pocas visitas en internet» es una falacia de:', 'Popularidad', 'Antigüedad', 'Ataque a la persona', 'Se apoya en cuánta gente la visita y no en sus rasgos.'),
        ('abc', '{F} «La compuso alguien que no estudió música» es una falacia de:', 'Ataque a la persona', 'Popularidad', 'Antigüedad', 'Se refiere a quien compuso y no a la obra.'),
        ('=', '{F} La obra dura 3 minutos y tiene 4 estrofas del mismo largo. ¿Cuántos segundos dura cada estrofa?', '3*60//4', 'Se pasan los minutos a segundos y se reparten entre las estrofas.', ' s'),
        ('abc', '{F} ¿Qué rasgo de la obra sirve de evidencia para su propósito de ser fácil de cantar en grupo?', 'La melodía de cuatro notas que se repite en las cuatro estrofas', 'Que la obra sea muy antigua y se haya compuesto hace mucho tiempo', 'Que la obra tenga pocas visitas en internet y poca gente la conozca', 'Una melodía breve y repetida facilita que un grupo la aprenda.'),
        ('abc', '{F} ¿Qué parte del borrador falta para que sea un juicio argumentado?', 'Una razón apoyada en un rasgo de la obra y relacionada con su propósito', 'Más falacias, como la antigüedad o la popularidad, que refuercen la opinión', 'El nombre de otra obra parecida que también le haya gustado a la persona', 'El borrador no tiene evidencia de la obra.'),
        ('=', '{F} La reescritura propuesta tiene 29 palabras y el máximo es 40. ¿Cuántas palabras más se pueden agregar?', '40-29', 'Se resta lo escrito al máximo permitido.', ' palabras'),
        ('abc', '{F} ¿Cuál de estas es la mejor corrección de «es mala porque es muy antigua»?', 'La obra no varía la dinámica en las cuatro estrofas, lo que da poca variedad', 'La obra es mala porque pocas personas la conocen y por eso no merece ser cantada', 'La obra es mala porque no me gusta cómo suena y eso es suficiente', 'La corrección cita un rasgo de la obra en lugar de su época.'),
        ('abc', '{F} Alguien corrige «tiene pocas visitas» por «tiene muchas visitas en otra página». ¿Qué falla?', 'Cambia una falacia de popularidad por otra y sigue sin citar rasgos de la obra', 'Nada, porque ya es un juicio argumentado, ya que usa un dato sobre visitas', 'Que las visitas en otra página no se pueden comparar con las de internet', 'La popularidad, alta o baja, no explica el valor de la obra.'),
        ('abc', '¿Por qué conviene guardar el borrador original cuando se reescribe?', 'Para mostrar el proceso de ajuste y poder comparar y volver atrás', 'Para entregar dos textos iguales y así ocupar más páginas del trabajo', 'Para evitar tener que leer el borrador cuando se haga la versión final', 'El registro de cambios muestra cómo mejoró el juicio.'),
        ('abc', '{F} La reescritura dice «aunque tiene poca variedad de dinámica». ¿Qué cumple al incluirlo?', 'Es prudente: reconoce un límite de la obra y no solo la elogia', 'Contradice su propia afirmación y deja el juicio sin fuerza ni razones', 'No tiene ninguna función, porque en un juicio no se deben mencionar límites', 'Reconocer límites hace el juicio más honesto y sólido.'),
        ('abc', 'Después de reescribir el juicio, ¿cómo se comprueba que mejoró?', 'Cada afirmación tiene un rasgo o una razón relacionada con el propósito, no tiene falacias y respeta el largo máximo', 'Tiene más adjetivos y por eso suena más seguro que el borrador original', 'Es más largo que el borrador, porque tiene más frases que antes', 'Se revisa evidencia, falacias y largo, no la cantidad de adjetivos.'),
    ],
    ctx=('=', 'Tienes 30 minutos para reescribir un juicio: 10 para leer la obra, 12 para escribir y el resto para revisar falacias y largo. ¿Cuántos minutos quedan para revisar?', '30-10-12', 'Se restan del total los minutos de lectura y de escritura.', ' minutos'),
    sc=[
        ("En Composición musical: ¿qué es un prejuicio en un juicio estético?", "Un juicio sobre una persona o grupo sin conocerlos, que no se apoya en la obra", "Los prejuicios no están basados en rasgos de la obra."),
        ('abc', 'Para corregir una falacia de antigüedad hay que:', 'Reemplazarla por un rasgo de la obra y su efecto', 'Repetirla más fuerte para que el juicio quede claro para todas las personas', 'Cambiar la fecha de la obra para que parezca más reciente', 'La falacia se corrige con evidencia de la obra.'),
        ("¿Qué se anota en un registro de cambios?", "Qué se cambió y por qué", "El registro muestra el proceso de ajuste."),
    ],
    op=("Con la {F}, reescribe el borrador en un juicio de máximo 40 palabras, sin falacias, con afirmación, razón y evidencia de la obra. Cuenta las palabras y anota qué cambiaste respecto del borrador.",
        "«La obra logra su propósito de ser fácil de cantar en grupo porque su melodía de cuatro notas se repite en las cuatro estrofas; tiene poca variedad de dinámica.» Son 29 palabras. Cambié las tres falacias del borrador por un rasgo de la obra y reconocí un límite.",
        ["sin falacias", "afirmación, razón y evidencia", "máximo 40 palabras con conteo", "registra qué cambió"],
        ["hoja con el borrador, la reescritura, el conteo y el registro de cambios"],
        ["cambiar una falacia por otra", "pasar del largo máximo", "no registrar los cambios"],
        "Pregunta: «¿qué rasgo de la obra reemplaza a cada falacia?». Si no lo encuentra, pídele que vuelva a la ficha."),
    reinforce="Escribe un juicio con una falacia sobre una canción conocida y luego reescríbelo con evidencia.",
    extend="Explica con un ejemplo inventado por qué reconocer un límite de una obra puede hacer más convincente un juicio positivo.",
)
