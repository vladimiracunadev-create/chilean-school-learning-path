"""Student material for 2.º medio Música, OA 03 (cantar y tocar repertorio diverso desde una selección personal: estilo, fluidez, proponer y dirigir, voces y funciones en un grupo).

Las piezas de los ejercicios son descripciones inventadas («de ejemplo»); no hay letras ni partituras con derechos.
La práctica cantada o tocada con instrumentos y el repertorio real los pone el docente; el cuaderno solo prepara la reflexión escrita.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA3 = "MU2M OA 03"

# ---------------------------------------------------------------- OA 03 · clase 1 (criterios para elegir repertorio)
L(
    OA3, 1,
    "Lápiz y papel. Las piezas son descripciones de ejemplo escritas en cada ejercicio. La práctica con voz o instrumento la dirige tu docente.",
    "Aprenderé a elegir repertorio para cantar o tocar con criterios claros y a justificar mi selección personal. Sirve para armar un repertorio diverso que mi grupo pueda interpretar bien.",
    ["Valoro una música con rasgos audibles y propósito.", "Sé que hay tradición oral, escrita y popular.", "Distingo voz principal, acompañamiento y pulso."],
    [
        "Elegir repertorio es una decisión musical. Un repertorio es el conjunto de piezas que un grupo o una persona puede interpretar. Para elegir bien se usan criterios: el interés personal (qué me motiva), el propósito o la ocasión (para quién y dónde se tocará), la dificultad (ritmos, extensión de la melodía, cantidad de voces), los recursos disponibles (qué voces e instrumentos hay) y la duración.",
        "Un repertorio diverso mezcla músicas distintas: de tradición oral, escrita y popular, de Chile y de otras partes del mundo, y de estilos o épocas diferentes. La diversidad no significa elegir cualquier cosa: cada pieza debe tener una razón. También se revisa el permiso: para ensayar en clase se puede usar cualquier pieza, pero para difundir una versión conviene respetar a quienes la crearon y pedir autorización cuando corresponde.",
        "Un buen método es escuchar la pieza completa, probar un fragmento corto, comprobar si el grupo lo logra con el tiempo disponible y recién entonces decidir. Si una pieza es demasiado difícil, se puede simplificar (menos voces, tempo más lento) sin perder su carácter, o dejarla para más adelante.",
    ],
    [("repertorio", "conjunto de piezas que una persona o un grupo puede interpretar"), ("criterio de selección", "razón que se usa para elegir una pieza"), ("dificultad", "esfuerzo que exige interpretar una pieza"), ("repertorio diverso", "conjunto con tradiciones, estilos u orígenes distintos"), ("recursos", "voces, instrumentos y tiempo con que cuenta el grupo")],
    [
        ("Elegir entre dos piezas", "Un grupo de cinco personas tiene una guitarra y dos voces cantantes, y debe tocar 8 minutos en un acto. Pieza X de ejemplo: dura 3 minutos, usa dos voces y guitarra. Pieza Y de ejemplo: dura 9 minutos y pide ocho voces. ¿Cuál conviene?", ["Los recursos son una guitarra y dos voces.", "X cabe en los recursos y en el tiempo.", "Y pide más voces y dura más de lo que hay."], "La pieza X, porque se ajusta a los recursos y a la duración"),
        ("Revisar si un repertorio es diverso", "Lista de ejemplo: una canción de cuna de tradición oral, una pieza para piano de tradición escrita y una canción popular actual. ¿Es diverso?", ["Cada pieza viene de una tradición distinta.", "Se pueden justificar por propósitos distintos."], "Sí, porque reúne tradición oral, escrita y popular"),
    ],
    [
        ("Elegir solo por la dificultad más alta, para «lucirse».", "Una pieza muy difícil puede salir mal y no sirve al propósito del acto.", "Equilibra el interés con la dificultad real y el tiempo disponible."),
        ("Pensar que «repertorio diverso» es juntar piezas al azar.", "Cada pieza necesita una razón de ser elegida.", "Anota para cada una el criterio que la justifica."),
    ],
    [
        ex("¿Qué es un repertorio? A) El conjunto de piezas que se pueden interpretar. B) El instrumento principal de un grupo.", "A", "Se define como conjunto de piezas."),
        ex("¿Cuál es un criterio de selección? A) La dificultad frente a los recursos del grupo. B) Que la pieza sea la más antigua del repertorio.", "A", "La dificultad y los recursos influyen en la decisión."),
        ex("Un grupo tiene tres voces y ninguna percusión. ¿Qué pieza de ejemplo se ajusta mejor? A) Una que se canta a tres voces sin instrumentos. B) Una que exige cuatro percusionistas.", "A", "Se ajusta a los recursos disponibles."),
    ],
    [
        ex("¿Por qué conviene probar un fragmento antes de decidir? A) Para comprobar si el grupo lo logra en el tiempo disponible. B) Para no escuchar la pieza completa.", "A", "El fragmento muestra la dificultad real."),
        ex("Una pieza de ejemplo es muy difícil para el grupo. ¿Qué opción mantiene su carácter? A) Simplificarla, por ejemplo con menos voces y tempo más lento. B) Cambiarle el estilo completo.", "A", "Simplificar no cambia lo esencial."),
        ex("¿Qué hace diverso a un repertorio? A) Reúne tradiciones, estilos u orígenes distintos con razones. B) Tiene muchas piezas de igual estilo.", "A", "La diversidad exige variedad justificada."),
    ],
    [
        ex("Una persona propone una pieza porque «es la que más suena en la radio». ¿Qué criterio falta para justificarla? A) Si se ajusta al propósito, a los recursos y a la dificultad. B) Si tiene un título largo.", "A", "La popularidad sola no es un criterio completo."),
        ex("Se necesita una pieza para un recreo cultural de 5 minutos con voz y percusión corporal. ¿Cuál es adecuada? A) Una de 4 minutos para voz y palmas. B) Una de 15 minutos para orquesta.", "A", "Cabe en el tiempo y en los recursos."),
        arith("Un programa de ejemplo lleva tres piezas de 6, 4 y 3 minutos. ¿Cuántos minutos dura en total, sin pausas?", "6+4+3", "Se suman las duraciones.", " minutos"),
    ],
    [
        ex("Dos estudiantes defienden una pieza. Mía: «Me encanta.» Noa: «Me gusta, tiene dos voces como nuestro grupo y dura 4 minutos, que es lo que el acto permite.» ¿Quién justifica mejor la selección? A) Mía. B) Noa.", "B", "Noa une gusto personal con recursos y tiempo."),
        ex("Un grupo elige solo piezas populares actuales y dice que su repertorio es diverso. ¿Qué observación es correcta? A) Falta variedad de tradiciones u orígenes. B) Está bien, porque todas son canciones.", "A", "Una sola tradición no es diversidad."),
    ],
    [
        ex("¿Qué se hace con una pieza que nadie del grupo puede lograr en el tiempo del ensayo? A) Se simplifica o se deja para más adelante. B) Se exige que alguien la logre igual.", "A", "Se ajusta la decisión a la realidad."),
        ex("Para un acto de homenaje, ¿qué criterio pesa más en la elección? A) El propósito de homenajear. B) La cantidad de notas.", "A", "El propósito guía la selección."),
    ],
    [ex("Tu curso debe preparar tres piezas para una muestra de música. ¿Qué lista de ejemplo es la mejor elección? A) Una canción de tradición oral, una pieza escrita y una popular, todas ajustadas a las voces del curso. B) Tres piezas muy parecidas escogidas por sorteo.", "A", "Combina diversidad con recursos.")],
    [
        ex("¿Verdadero o falso? Un criterio de selección es una razón para elegir una pieza.", "Verdadero", "Es la razón que sustenta la decisión."),
        ex("¿Qué se revisa antes de difundir una versión? A) Respetar a quienes crearon la pieza y pedir autorización cuando corresponde. B) Cambiar el nombre de la pieza.", "A", "Se cuida la autoría."),
        ex("¿Qué dato NO sirve como criterio de dificultad? A) La cantidad de voces. B) El color del instrumento.", "B", "El color no cambia lo que se debe tocar."),
    ],
    (
        "Escribe un repertorio de ejemplo de tres piezas para un acto de tu curso (describe cada una en una línea, sin copiar letras). Para cada pieza anota: tradición, propósito en el acto, dificultad (baja, media o alta) y la razón de elegirla.",
        "1) Canción de cuna de tradición oral: da inicio tranquilo, dificultad baja, porque toda la clase puede cantarla. 2) Pieza escrita para flauta dulce: muestra lectura, dificultad media, porque hay seis flautas. 3) Canción popular a dos voces: cierra el acto con energía, dificultad media, porque el curso la conoce.",
        ["tres piezas con tradiciones distintas", "cada pieza con propósito, dificultad y razón", "al menos un criterio ligado a los recursos del curso"],
        ["lista de tres piezas con cuatro datos cada una"],
        ["justificar solo con «me gusta»", "elegir piezas imposibles para los recursos"],
        "Reconoce la lista y pide reemplazar un «me gusta» por un criterio de recursos o propósito.",
    ),
    "Anota dos piezas que te gustaría tocar o cantar y, para cada una, un criterio que las justifique.",
    "Propón a tu grupo un cambio que haga más fácil una pieza difícil sin perder su carácter y explica qué cambiaste.",
)

# ---------------------------------------------------------------- OA 03 · clase 2 (voces y funciones en un grupo)
L(
    OA3, 2,
    "Lápiz y papel. Las piezas y sus voces están descritas en los ejercicios (son de ejemplo). Tu docente organiza la práctica del grupo.",
    "Aprenderé a identificar las voces de una pieza y la función de cada una dentro de un grupo. Sirve para saber qué papel me toca y cómo encajar con las demás personas al cantar o tocar.",
    ["Elijo repertorio con criterios.", "Distingo melodía, acompañamiento y pulso.", "Describo la textura de una música."],
    [
        "En una pieza para varias personas, cada voz o instrumento cumple una función. La melodía principal es la línea que más se recuerda. El acompañamiento armónico sostiene los acordes, por ejemplo con guitarra o piano. El bajo da la base grave. La percusión marca el pulso y el ritmo. Una segunda voz o contramelodía canta o toca otra línea que acompaña a la principal sin taparla.",
        "Una misma persona puede cambiar de función a lo largo de la pieza: en la estrofa lleva la melodía y en el estribillo acompaña. Por eso conviene mirar la pieza por secciones. Identificar las funciones ayuda a decidir el volumen: quien lleva la melodía se debe escuchar, y quien acompaña ajusta su dinámica para no taparla.",
        "Para encajar en el grupo se escucha al resto mientras se toca: se mantiene el pulso común, se entra a tiempo y se cuida el balance, que es la proporción entre los volúmenes de las voces. Cuando todas las voces cantan o tocan lo mismo a la vez se llama unísono. Cuando suenan líneas distintas al mismo tiempo, hay una textura de varias capas.",
    ],
    [("melodía principal", "línea que lleva el tema de la pieza"), ("acompañamiento", "voces o instrumentos que sostienen la melodía"), ("bajo", "línea grave que da la base"), ("contramelodía", "otra línea que acompaña a la principal"), ("balance", "proporción entre los volúmenes de las voces"), ("unísono", "todas las voces hacen lo mismo a la vez"), ("compás", "grupo de pulsos que se repite con regularidad")],
    [
        ("Asignar funciones", "Un grupo de ejemplo: una voz canta el tema, otra voz canta una línea más grave que lo acompaña, una guitarra toca acordes y un bombo marca el pulso. ¿Qué función cumple cada una?", ["La voz del tema lleva la melodía principal.", "La otra voz hace la contramelodía.", "La guitarra acompaña con acordes y el bombo marca el pulso."], "Melodía principal, contramelodía, acompañamiento y pulso"),
        ("Cuidar el balance", "En la estrofa de una pieza de ejemplo la voz principal canta bajito y la guitarra suena fuerte. ¿Qué debe ajustar la guitarra?", ["La melodía debe oírse.", "La guitarra acompaña, no tapa."], "Bajar su dinámica para que se oiga la melodía"),
    ],
    [
        ("Pensar que quien acompaña no es importante.", "El acompañamiento sostiene la pieza; sin él la melodía queda sin base.", "Valora cada función por lo que aporta al conjunto."),
        ("Tocar siempre lo más fuerte posible para «lucirse».", "El balance depende de la función en cada sección.", "Escucha al grupo y ajusta tu volumen según la función."),
    ],
    [
        ex("¿Qué función cumple el bajo? A) Da la base grave. B) Lleva la melodía aguda.", "A", "El bajo es la línea grave que sostiene."),
        ex("¿Cómo se llama cuando todas las voces hacen lo mismo a la vez? A) Unísono. B) Contramelodía.", "A", "Unísono significa la misma línea para todos."),
        ex("Una persona toca acordes con guitarra. ¿Qué función cumple? A) Acompañamiento. B) Melodía principal.", "A", "Los acordes sostienen la melodía."),
    ],
    [
        ex("En el estribillo de una pieza de ejemplo, la voz principal calla y todo el grupo canta el tema. ¿Qué textura se oye? A) Unísono. B) Una voz sola.", "A", "Todas las voces cantan lo mismo."),
        ex("¿Qué es el balance en un grupo? A) La proporción entre los volúmenes de las voces. B) La cantidad de ensayos.", "A", "Se refiere al volumen relativo."),
        ex("Una contramelodía suena más fuerte que la melodía principal. ¿Qué problema hay? A) No hay balance y la melodía se tapa. B) Hay demasiada percusión.", "A", "La contramelodía debe acompañar sin tapar."),
    ],
    [
        ex("Tu función es marcar el pulso con un tambor en una pieza de ejemplo. ¿Qué haces cuando la voz canta bajito? A) Bajas tu volumen para no taparla. B) Subes el volumen para mantener el protagonismo.", "A", "La percusión sigue el balance."),
        ex("En una pieza de ejemplo hay cuatro personas: una canta el tema, otra toca acordes, otra marca el pulso y otra toca el bajo. ¿Cuántas funciones distintas hay? A) Cuatro. B) Dos.", "A", "Cada persona tiene una función diferente."),
        arith("En un compás de 4 pulsos, un bombo suena en los pulsos 1 y 3. ¿Cuántas veces suena en 5 compases seguidos?", "2*5", "Suena dos veces por compás durante cinco compases.", " veces"),
    ],
    [
        ex("Un grupo dice: «La guitarra no importa, solo la voz.» Otro responde: «Sin acordes, la voz se queda sin base.» ¿Quién describe mejor las funciones? A) El primero. B) El segundo.", "B", "El acompañamiento aporta la base."),
        ex("Una persona canta la melodía en la estrofa y acompaña en el estribillo. ¿Qué dice esto de las funciones? A) Pueden cambiar de sección en sección. B) Son fijas en toda la pieza.", "A", "Las funciones se asignan por sección."),
    ],
    [
        ex("Para que un grupo de seis voces cuide el balance, ¿qué decisión es más útil? A) Acordar quién lleva la melodía en cada sección. B) Que cada voz suba su volumen.", "A", "Definir funciones ordena el volumen."),
        ex("Dos voces cantan líneas distintas a la vez. ¿Qué textura hay? A) De varias capas. B) De unísono.", "A", "Hay más de una línea simultánea."),
    ],
    [ex("Un trío de ejemplo ensaya y el bajo tapa a la melodía. ¿Qué propuesta soluciona el problema? A) Que quien toca el bajo baje su volumen y escuche la melodía. B) Que la melodía grite más.", "A", "El balance se corrige escuchando.")],
    [
        ex("¿Verdadero o falso? Una misma persona puede cumplir funciones distintas en secciones distintas.", "Verdadero", "Las funciones cambian por sección."),
        ex("¿Qué es una contramelodía? A) Otra línea que acompaña a la principal. B) Un cambio de dinámica entre dos secciones.", "A", "Es una línea melódica secundaria."),
        ex("Para encajar en un grupo, ¿qué se hace mientras se toca? A) Escuchar al resto y mantener el pulso común. B) Mirar solo la propia parte para no equivocarse.", "A", "Se toca atento al conjunto."),
    ],
    (
        "Pieza de ejemplo: tema cantado por una voz, acordes de guitarra, pulso en un cajón y una segunda voz grave que repite una frase corta. Escribe: a) la función de cada una de las cuatro personas, b) qué sección cambia las funciones si en el estribillo todas cantan el tema, c) una indicación de balance para la guitarra.",
        "a) Voz: melodía; guitarra: acordes; cajón: pulso; voz grave: contramelodía. b) En el estribillo todos pasan a la melodía en unísono. c) La guitarra baja su volumen cuando la voz canta suave.",
        ["nombra cuatro funciones distintas", "explica un cambio de función por sección", "da una indicación concreta de balance"],
        ["respuestas a), b) y c) escritas"],
        ["decir que todas las voces hacen lo mismo siempre", "no mencionar el volumen"],
        "Reconoce las funciones y pide precisar cuándo cada persona debe oírse más.",
    ),
    "Escucha una canción y anota qué instrumento o voz lleva la melodía, cuál acompaña y cuál marca el pulso.",
    "Explica a una persona de tu casa qué función tendrías tú en un grupo y cómo cuidarías el balance.",
)

# ---------------------------------------------------------------- OA 03 · clase 3 (estilo y fluidez)
L(
    OA3, 3,
    "Lápiz y papel. Los tempos y las frases están escritos en los ejercicios. La práctica instrumental o vocal real la guía tu docente.",
    "Aprenderé a cuidar el estilo y la fluidez al cantar o tocar, y a ensayar con un método. Sirve para que una pieza suene continua, con pulso estable y con el carácter que le corresponde.",
    ["Escribo y leo pulsos por minuto.", "Reconozco el tempo y la dinámica.", "Identifico mi función en un grupo."],
    [
        "La fluidez es interpretar sin detenerse y con pulso estable, aunque la pieza tenga pasajes difíciles. No es tocar rápido: es mantener un avance parejo. El estilo es el conjunto de rasgos que dan carácter a una pieza: el tempo, la dinámica, la articulación (si las notas se unen en ligado o se separan en staccato), los adornos y el timbre.",
        "Para mejorar la fluidez se ensaya con un método: primero, a tempo lento; luego, por fragmentos cortos y repitiendo con atención; después, se une cada fragmento y se sube el tempo de a poco. El tempo se mide en pulsos por minuto. Si el tempo es de 60 pulsos por minuto, cada pulso dura un segundo; si es de 120, cada pulso dura medio segundo.",
        "Para calcular cuánto dura una frase se multiplica la cantidad de pulsos por 60 y se divide por los pulsos por minuto. Una frase de 16 pulsos a 120 pulsos por minuto dura 16 × 60 ÷ 120 = 8 segundos. Para cuidar el estilo se escucha un modelo, se anota qué rasgos se oyen y se decide qué se imitará y qué se adaptará a la voz o al instrumento propio.",
    ],
    [("fluidez", "interpretar con avance parejo y pulso estable"), ("estilo", "conjunto de rasgos que dan carácter a una pieza"), ("articulación", "modo de unir o separar las notas"), ("ligado", "notas unidas sin corte entre ellas"), ("staccato", "notas cortas y separadas"), ("pulsos por minuto", "medida del tempo")],
    [
        ("Calcular la duración", "Una frase de ejemplo tiene 8 pulsos y se toca a 60 pulsos por minuto. ¿Cuánto dura?", ["A 60 pulsos por minuto, cada pulso dura 1 segundo.", "8 pulsos × 1 segundo = 8 segundos."], "8 segundos"),
        ("Ordenar un método de ensayo", "Pasos desordenados: subir el tempo, repetir un fragmento corto, tocar a tempo lento. ¿Cuál es un orden lógico?", ["Se parte por lo más fácil de controlar.", "Luego se trabaja un fragmento.", "Al final se sube el tempo."], "Tempo lento, fragmento corto y subir el tempo"),
    ],
    [
        ("Creer que fluidez es tocar rápido.", "Se puede tocar rápido y con tropiezos; la fluidez es avance parejo.", "Cuida el pulso estable y sube el tempo solo cuando salga."),
        ("Imitar un modelo nota por nota sin pensar en la voz propia.", "La imitación ciega ignora los recursos de quien interpreta.", "Escucha, anota los rasgos del estilo y decide qué adaptarás."),
    ],
    [
        ex("¿Qué es la fluidez? A) Interpretar con avance parejo y pulso estable. B) Tocar siempre lo más fuerte posible.", "A", "La fluidez trata de continuidad."),
        ex("¿Cómo se llama el modo de unir o separar las notas? A) Articulación. B) Armonía.", "A", "Es la articulación."),
        ex("A 60 pulsos por minuto, ¿cuánto dura cada pulso? A) Un segundo. B) Medio segundo.", "A", "60 pulsos en 60 segundos dan un pulso por segundo."),
    ],
    [
        ex("¿Qué se hace primero al ensayar un pasaje difícil? A) Tocarlo a tempo lento. B) Tocarlo lo más rápido posible.", "A", "Se parte lento para controlar."),
        ex("Notas cortas y separadas se llaman: A) staccato. B) ligado.", "A", "Staccato indica notas separadas."),
        ex("¿Qué rasgo NO forma parte del estilo? A) El tempo. B) La fecha del ensayo.", "B", "La fecha del ensayo no da carácter musical."),
    ],
    [
        arith("Una frase de ejemplo tiene 24 pulsos y se toca a 60 pulsos por minuto. ¿Cuántos segundos dura?", "24*60//60", "A 60 pulsos por minuto cada pulso dura un segundo.", " segundos"),
        arith("Otra frase de ejemplo tiene 32 pulsos y se toca a 120 pulsos por minuto. ¿Cuántos segundos dura?", "32*60//120", "Se multiplica por 60 y se divide por los pulsos por minuto.", " segundos"),
        ex("Una pieza de ejemplo pide un carácter suave y unido. ¿Qué articulación conviene? A) Ligado. B) Staccato.", "A", "Lo suave y unido pide notas ligadas."),
    ],
    [
        ex("Una intérprete toca rápido pero se detiene en cada pasaje difícil. ¿Qué le falta? A) Fluidez. B) Más volumen.", "A", "Se detiene, no avanza parejo."),
        ex("Un grupo logra un fragmento a tempo lento. ¿Qué paso corresponde? A) Subir el tempo de a poco. B) Dejar de ensayar ese fragmento.", "A", "El método sube el tempo gradualmente."),
    ],
    [
        ex("Un estudiante imita el estilo de un modelo, pero su voz es más grave y no llega a la nota más aguda. ¿Qué decisión es más adecuada? A) Cantar la pieza un poco más grave, adaptada a su voz, y mantener los otros rasgos del estilo. B) Forzar la voz hasta lograrla.", "A", "Se adapta sin perder el carácter y se cuida la voz."),
        ex("Una frase de 40 pulsos dura 20 segundos. ¿A cuántos pulsos por minuto se toca? A) 120. B) 60.", "A", "40 pulsos en 20 segundos son 2 por segundo, o sea 120 por minuto."),
    ],
    [ex("Tienes 10 minutos para ensayar una pieza de ejemplo. ¿Qué plan es más útil? A) 3 minutos a tempo lento, 5 minutos por fragmentos y 2 minutos uniendo. B) 10 minutos tocando siempre desde el principio sin detenerte.", "A", "Combina lento, fragmentos y unión.")],
    [
        ex("¿Verdadero o falso? El estilo incluye tempo, dinámica y articulación.", "Verdadero", "Son rasgos que dan carácter."),
        ex("A 120 pulsos por minuto, ¿cuánto dura cada pulso? A) Medio segundo. B) Un segundo.", "A", "120 pulsos en 60 segundos son 2 por segundo."),
        ex("¿Qué se anota al escuchar un modelo de estilo? A) Los rasgos que se oyen. B) La opinión de otra persona sobre el compositor.", "A", "Se describe lo audible."),
    ],
    (
        "Pieza de ejemplo: una frase de 20 pulsos, carácter suave y unido, tempo final de 120 pulsos por minuto. Escribe: a) un plan de ensayo de tres pasos, b) la articulación que usarás y por qué, c) cuánto dura la frase al tempo final (muestra el cálculo).",
        "a) Tempo lento, fragmentos de 4 pulsos, unir y subir el tempo. b) Ligado, porque el carácter es suave y unido. c) 20 × 60 ÷ 120 = 10 segundos.",
        ["plan de tres pasos ordenado", "articulación coherente con el carácter", "cálculo correcto con la fórmula de la clase"],
        ["respuestas a), b) y c) escritas con el cálculo"],
        ["subir el tempo antes de lograr el fragmento", "olvidar multiplicar por 60"],
        "Reconoce el plan y pide revisar el cálculo de la duración paso a paso.",
    ),
    "Elige una frase de una canción y escribe cuánto duraría a 60 y a 120 pulsos por minuto si tuviera 12 pulsos.",
    "Describe con palabras los rasgos de estilo de una pieza (tempo, dinámica, articulación) y decide qué conservarías.",
)

# ---------------------------------------------------------------- OA 03 · clase 4 (proponer y dirigir)
L(
    OA3, 4,
    "Lápiz y papel. Los casos de ensayo están escritos en los ejercicios. La dirección con el grupo real y los instrumentos la organiza tu docente.",
    "Aprenderé a proponer ideas y a dirigir un ensayo con claridad y respeto. Sirve para coordinar a un grupo, dar entradas y cortes, y mejorar una pieza usando lo que se oye.",
    ["Elijo repertorio con criterios.", "Identifico voces y funciones.", "Ensayo con método y cuido la fluidez."],
    [
        "Dirigir un grupo es coordinarlo para que interprete junto. Quien dirige da la entrada con una cuenta previa que marca el tempo, por ejemplo cuatro pulsos antes de empezar. Indica con gestos claros el tempo, las entradas de cada voz, los cambios de dinámica y el corte final. Sus indicaciones deben ser breves, concretas y apoyadas en lo que se oye: «la voz grave entra un pulso tarde» ayuda más que «suena mal».",
        "Proponer es sugerir una idea musical al grupo: cambiar el orden de las estrofas, repetir el estribillo, quitar un instrumento en una sección. Una buena propuesta indica qué cambiar, para qué y qué efecto se espera. El grupo la prueba y decide si la adopta. Dirigir no es mandar: se escuchan las ideas de las demás personas y se rotan los roles para que todas participen, sin obligar a nadie a exponerse más de lo que quiera.",
        "Un ensayo eficaz tiene fases: calentamiento de voz y cuerpo, trabajo de fragmentos difíciles, unión de la pieza y breve evaluación final. Los comentarios al grupo se refieren a la evidencia audible y a la tarea, no a las personas: «la entrada del estribillo se adelanta» y no «tú siempre fallas».",
    ],
    [("dirigir", "coordinar a un grupo para que interprete junto"), ("entrada", "momento en que una voz o instrumento comienza"), ("cuenta previa", "pulsos que se marcan antes de empezar para fijar el tempo"), ("corte", "señal para terminar juntos"), ("propuesta", "idea musical que se sugiere al grupo"), ("evidencia audible", "lo que se puede comprobar escuchando")],
    [
        ("Dar una indicación útil", "En un ensayo de ejemplo, la segunda voz entra un pulso antes de lo debido. Quien dirige dice: «Suena mal.» ¿Cómo puede mejorar esa indicación?", ["Debe decir qué se oye, dónde y cómo corregirlo.", "Se señala la entrada y se repite desde antes."], "«La segunda voz entra un pulso antes; repitamos con una cuenta de cuatro y entra en el pulso uno»"),
        ("Planificar el ensayo", "Un ensayo de ejemplo dura 30 minutos: 5 de calentamiento, 15 de fragmentos y el resto para unir la pieza y evaluar. ¿Cuántos minutos quedan para unir y evaluar?", ["Se suman los minutos ya asignados: 5 + 15 = 20.", "Se restan del total: 30 − 20 = 10."], "10 minutos"),
    ],
    [
        ("Dar órdenes sin escuchar las ideas del grupo.", "Dirigir es coordinar, no imponer; las ideas del grupo mejoran la pieza.", "Escucha propuestas y pruébalas antes de decidir."),
        ("Comentar a las personas («eres desafinado») en lugar de lo audible.", "El comentario sobre la persona no dice qué corregir y puede herir.", "Describe lo que se oye y propone un ajuste de la tarea."),
    ],
    [
        ex("¿Para qué sirve la cuenta previa? A) Para fijar el tempo antes de empezar. B) Para terminar la pieza.", "A", "Marca el tempo de entrada."),
        ex("¿Qué indica el corte? A) El final común. B) El comienzo de la pieza.", "A", "El corte hace terminar juntos."),
        ex("¿Qué debe tener una propuesta musical? A) Qué cambiar, para qué y qué efecto se espera. B) Solo el nombre de quien la hace.", "A", "Así el grupo puede probarla."),
    ],
    [
        ex("¿Qué comentario se apoya en evidencia audible? A) «La guitarra se adelanta en el estribillo.» B) «Eres muy lento.»", "A", "Describe lo que se oye y dónde."),
        ex("¿Qué fase ocurre primero en un ensayo eficaz? A) El calentamiento. B) La evaluación final.", "A", "Se parte calentando."),
        ex("¿Qué hace quien dirige cuando el grupo propone una idea? A) La prueba con el grupo y decide con el resultado. B) La rechaza porque dirige él o ella.", "A", "Se prueba antes de decidir."),
    ],
    [
        ex("Una cuenta previa de 4 pulsos a 60 pulsos por minuto, ¿cuánto dura? A) Cuatro segundos. B) Dos segundos.", "A", "Cada pulso dura un segundo a ese tempo."),
        ex("En una pieza de ejemplo, dos personas entran juntas en el estribillo, pero una entra un pulso tarde. ¿Qué indicación de quien dirige es mejor? A) «Marquemos la entrada del estribillo con un gesto y cuenten dos pulsos antes.» B) «Entren cuando puedan.»", "A", "Propone un ajuste concreto."),
        ex("Un grupo de seis personas ensaya y siempre dirige la misma. ¿Qué mejora conviene? A) Rotar el rol para que todas participen. B) Que dirija siempre quien mejor lo hace.", "A", "La rotación da oportunidades."),
    ],
    [
        ex("Una estudiante propone repetir el estribillo al final para cerrar con más energía. ¿Qué falta para que la propuesta se pueda evaluar? A) Probarla con el grupo y comparar cómo suena. B) Anotar la edad de la estudiante.", "A", "La idea y su efecto están; falta probarla con el grupo."),
        ex("Un ensayo se hizo de 18:00 a 18:40 con 8 minutos de calentamiento, 20 de fragmentos y el resto para unir. ¿Cuántos minutos hubo para unir? A) 12. B) 8.", "A", "El ensayo duró 40 minutos; 40 − 8 − 20 = 12."),
    ],
    [
        ex("En el ensayo, alguien dice: «Preferiría no dirigir hoy, pero puedo marcar el pulso.» ¿Qué respuesta del grupo es adecuada? A) Aceptar y asignarle ese rol equivalente. B) Insistir en que dirija delante de todos.", "A", "Se respeta la participación sin exposición forzada."),
        ex("Un grupo termina cada vez en un momento distinto. ¿Qué indicación de dirección ayuda mejor? A) Acordar una señal de corte y practicarla. B) Pedir que todos terminen cuando se sientan listos.", "A", "El corte común ordena el final."),
    ],
    [ex("Eres quien dirige un trío de ejemplo y la voz tapa a la guitarra en la estrofa. ¿Qué dices? A) «En la estrofa la voz puede bajar un poco para que se oiga la guitarra; probemos.» B) «No saben cantar.»", "A", "Indica qué cambiar, dónde y propone probar.")],
    [
        ex("¿Verdadero o falso? Dirigir es lo mismo que mandar sin escuchar.", "Falso", "Es coordinar escuchando ideas."),
        ex("¿Qué se hace con los comentarios al grupo? A) Se refieren a lo audible y a la tarea. B) Se dirigen a las personas.", "A", "Así ayudan a mejorar."),
        ex("¿Qué señal usa quien dirige para pedir un sonido más suave? A) Un gesto de dinámica. B) Una cuenta previa.", "A", "Los gestos indican dinámica."),
    ],
    (
        "Escribe el guion de 5 líneas de un ensayo de ejemplo de 36 minutos para una pieza a dos voces con guitarra: fases con minutos que sumen 36, una cuenta previa, una propuesta musical con su efecto esperado y un comentario sobre lo audible.",
        "1) Calentamiento 6 min. 2) Fragmentos 18 min. 3) Unir y evaluar 12 min. 4) Cuenta previa de 4 pulsos para cada entrada. 5) Propuesta: repetir el estribillo al final para cerrar con más energía; comentario: la segunda voz entra un pulso tarde.",
        ["fases con minutos que suman 36", "una cuenta previa y una propuesta con efecto", "un comentario sobre evidencia audible, no sobre personas"],
        ["guion de cinco líneas"],
        ["tiempos que no suman 36", "comentarios sobre personas"],
        "Reconoce el guion y pide revisar que los minutos sumen el total y que el comentario sea sobre lo audible.",
    ),
    "Practica con una persona de tu casa una cuenta previa de 4 pulsos a pulso parejo y anota cuál fue más difícil de mantener.",
    "Escribe dos propuestas musicales para una canción que conozcas y qué efecto esperas de cada una.",
)
