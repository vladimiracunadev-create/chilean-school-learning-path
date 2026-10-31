"""Student material for 7.º básico Música, OA 01 (reconocer sentimientos, sensaciones e ideas al escuchar músicas de Chile y el mundo y manifestarlos por medios verbales, visuales, sonoros y corporales).

Todas las audiciones de los ejercicios son descripciones inventadas para esta clase; las audiciones reales las selecciona y pone el docente.
Este módulo define el ayudante L (y task) que usan los demás módulos mu7_*.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA1 = "MU07 OA 01"


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, tk, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[dict(title=t, problem=p, steps=s, answer=a) for t, p, s, a in worked],
        mistakes=[dict(wrong=w, why=y, fix=f) for w, y, f in mistakes],
        tiers=dict(recovery=R, understand=C, apply=A, reason=Z, challenge=D),
        context=ctx, selfcheck=sc, open_task=task(*tk), reinforce=reinforce, extend=extend,
    )


# ---------------------------------------------------------------- OA 01 · clase 1 (lo que se oye, lo que siento, lo que imagino)
L(
    OA1, 1,
    "Lápiz y papel. Los fragmentos musicales están descritos con palabras en los ejercicios; si una persona de tu casa puede poner una canción o tararearla, también sirve, pero no es necesario. Escucha a volumen bajo.",
    "Aprenderé a separar tres cosas cuando escucho música: lo que se oye, lo que siento y lo que imagino. Sirve para hablar de la música con claridad y sin discutir por gustos.",
    ["Sé que la música tiene pulso, melodía y volumen.", "Sé decir si un sonido es fuerte o suave, rápido o lento.", "Sé escribir oraciones cortas."],
    [
        "Al escuchar música pasan tres cosas distintas. Lo primero es lo que se oye: un hecho que cualquier persona puede comprobar, como «la melodía baja», «el tambor va rápido» o «suena una flauta sola». Lo segundo es lo que siento: una sensación o emoción, como calma, miedo, alegría o ganas de moverme. Lo tercero es lo que imagino: una idea, un recuerdo o una escena, como «un barco que se aleja».",
        "Conviene escuchar primero y nombrar después. Primero anoto lo que se oye, porque eso es lo que todos podemos comprobar. Después escribo lo que siento y lo que imagino. Dos personas pueden sentir cosas distintas con la misma música y ninguna se equivoca, porque las sensaciones son personales. Lo que sí se puede revisar es si el hecho audible está bien descrito.",
        "Una buena descripción une las tres cosas con la palabra «porque»: «Siento calma porque la melodía baja despacio y suena suave». La frase nombra la sensación y da la evidencia audible que la sostiene. Así, quien te escuche puede volver a la música y comprobar tu idea. Decir solo «me gusta» o «es linda» no basta, porque no dice qué se oye.",
    ],
    [("hecho audible", "algo que se oye y que cualquiera puede comprobar"), ("sensación", "lo que siento al escuchar, como calma, alegría o miedo"), ("idea o imagen", "lo que imagino o recuerdo al escuchar"), ("evidencia", "el dato audible que sostiene lo que digo"), ("porque", "palabra que une mi sensación con la evidencia")],
    [
        ("Clasificar una frase", "Clasifica la frase «El violonchelo toca notas largas y graves» como hecho audible, sensación o idea.", ["Se puede comprobar escuchando: instrumento, notas largas y graves.", "No habla de emociones ni de escenas."], "Es un hecho audible"),
        ("Armar la descripción completa", "Fragmento: una flauta toca aguda y rápida, con volumen suave. Sensación: «me siento ligero». ¿Cómo queda la frase completa con evidencia?", ["Elijo la sensación: ligero.", "Elijo la evidencia audible: aguda, rápida y suave.", "Los uno con «porque»."], "Me siento ligero porque la flauta toca aguda, rápida y suave"),
    ],
    [
        ("Pensar que, si siento algo distinto a mi compañera, uno de los dos se equivoca.", "Las sensaciones son personales y pueden diferir con la misma música.", "Compara qué escucharon en cada caso, no qué sintieron."),
        ("Poner «es alegre» como si fuera un hecho audible.", "Alegre es una sensación; lo que se oye es, por ejemplo, el tempo rápido.", "Cambia «es alegre» por «siento alegría porque va rápido y fuerte»."),
    ],
    [
        ex("La frase «Siento miedo» ¿es un hecho audible, una sensación o una idea?", "Una sensación", "Habla de lo que siente la persona, no de lo que suena."),
        ex("La frase «Me hace pensar en un barco que se aleja del puerto» ¿es hecho audible, sensación o idea?", "Una idea", "Es una imagen que la persona imagina al escuchar."),
        ex("La frase «Los tambores suenan más fuerte que la guitarra» ¿es hecho audible, sensación o idea?", "Un hecho audible", "Cualquiera puede comprobarlo escuchando."),
    ],
    [
        ex("Tomás siente tristeza con una música y Ana siente calma con la misma. ¿Alguna de las dos sensaciones es un error? Responde sí o no.", "No", "Las sensaciones son personales, y ninguna se puede declarar equivocada."),
        ex("En la frase «Siento calma porque la melodía baja despacio y suena suave», ¿cuál es la evidencia audible?", "La melodía baja despacio y suena suave", "Es lo que se puede comprobar al escuchar; la calma es la sensación."),
        ex("Dos personas describen una música. A: «Es hermosa». B: «Un piano toca la misma melodía tres veces, cada vez más fuerte». ¿Quién da un hecho audible?", "B", "B nombra instrumento, repetición y volumen; A solo opina."),
    ],
    [
        ex("Cuenta los hechos audibles, sin contar el instrumento, en esta descripción: «Un violín toca notas largas; la melodía baja; el volumen es muy suave».", "3", "Son notas largas, melodía que baja y volumen muy suave; el violín nombra el instrumento y no se cuenta."),
        ex("Lee las cinco frases: 1) El tambor va rápido. 2) Me da miedo. 3) Parece una tormenta. 4) La voz canta una nota aguda y larga. 5) Me siento tranquilo. ¿Cuáles números son hechos audibles?", "1 y 4", "Solo 1 y 4 se pueden comprobar escuchando; 2 y 5 son sensaciones y 3 es una imagen."),
        ex("Fragmento: un violonchelo toca lento, grave y suave. ¿Qué descripción completa es mejor: A) Es una pena. B) Siento pena porque el violonchelo toca lento, grave y suave?", "B", "La opción B nombra la sensación y da la evidencia audible; A solo opina."),
    ],
    [
        ex("Juan escribió: «La música es triste porque a todos les da pena». ¿Qué le falta a su frase: un hecho audible o una sensación?", "Un hecho audible", "Ya tiene la sensación, pero no dice qué se oye que la provoque."),
        ex("Martina escribió: «Se oye alegría». ¿Por qué hay que corregir la frase?", "Porque la alegría es una sensación y no algo que se oye", "Lo que se oye es, por ejemplo, el tempo rápido; la alegría se siente."),
    ],
    [
        ex("Escuchas dos fragmentos: el 1 tiene tambor rápido y fuerte, y el 2 tiene flauta lenta y suave. Una persona dice «me dan ganas de saltar». ¿Con cuál fragmento es más probable que lo diga?", "Con el fragmento 1", "Tempo rápido y volumen fuerte suelen dar energía y ganas de moverse."),
        ex("Lee: 1) El bombo marca un pulso lento. 2) Me siento concentrada. 3) Veo una caravana que camina por el desierto. ¿Qué número es una idea y qué número es un hecho audible?", "Idea: 3; hecho audible: 1", "La frase 3 es una imagen; la 1 se puede comprobar; la 2 es una sensación."),
    ],
    [ex("En un bus escuchas una canción con guitarras rápidas y fuertes. Una persona dice «se oye feliz». ¿Cuál es la evidencia audible: A) todos van sonriendo o B) las guitarras tocan rápido y fuerte?", "B", "Lo que se oye es el tempo y el volumen; la sonrisa de los pasajeros no es sonido.")],
    [ex("¿Qué palabra une la sensación con la evidencia en una descripción completa?", "Porque", "Conecta lo que siento con lo que se oye."), ex("Una persona dice «me acuerdo de una fiesta». ¿Es hecho audible, sensación o idea?", "Una idea", "Es un recuerdo que la música despierta."), ex("¿Qué conviene hacer primero: escuchar o nombrar?", "Escuchar", "Se anota lo que se oye antes de poner nombres o sensaciones.")],
    (
        "Lee estos dos fragmentos inventados. Fragmento 1: un piano toca notas largas y graves, muy suave, y la melodía baja despacio. Fragmento 2: un tambor y una flauta tocan rápido y fuerte, con notas cortas, y la melodía sube. Elige uno y completa una tabla con tres columnas: «Se oye» (dos hechos audibles), «Siento» (una sensación tuya) e «Imagino» (una escena). Termina con la frase: «Siento … porque …».",
        "Fragmento 1. Se oye: notas graves y largas; melodía que baja despacio. Siento: calma. Imagino: una noche sin viento. Frase: «Siento calma porque el piano toca grave, muy suave y la melodía baja despacio».",
        ["separa hechos audibles, sensación e idea", "da al menos dos hechos audibles", "une sensación y evidencia con «porque»"],
        ["tabla de tres columnas", "frase final con evidencia"],
        ["poner una sensación en la columna «Se oye»", "usar solo «me gusta»"],
        "Reconoce la tabla y pide, para la sensación elegida, señalar en la columna «Se oye» qué dato la sostiene.",
    ),
    "Escribe tres frases sobre una música que conozcas: un hecho audible, una sensación y una imagen.",
    "Describe el mismo fragmento desde dos sensaciones distintas, cada una con su propia evidencia audible.",
)

# ---------------------------------------------------------------- OA 01 · clase 2 (rasgos audibles que se pueden reconocer)
L(
    OA1, 2,
    "Lápiz y papel. Los fragmentos están descritos en los ejercicios con tempo, volumen, instrumentos y registro. Si quieres, practica cada rasgo con tu voz: lento y rápido, suave y fuerte, grave y agudo.",
    "Aprenderé a reconocer cinco rasgos audibles: tempo, dinámica, timbre, registro y duración de las notas. Sirve para decir con precisión qué se oye antes de decir qué se siente.",
    ["Sé que el pulso es el latido parejo de la música.", "Sé distinguir sonidos fuertes y suaves.", "Sé distinguir un sonido grave de uno agudo."],
    [
        "Para describir lo que se oye usamos cinco rasgos. El tempo es la velocidad del pulso: lento, moderado o rápido, y se mide en pulsos por minuto. La dinámica es lo fuerte o suave que suena. El timbre es el color propio de cada instrumento o voz, el que nos permite distinguir una flauta de un violín aunque toquen la misma nota.",
        "El registro es qué tan grave o agudo suena el sonido: el violonchelo y el bombo suelen sonar graves; la flauta traversa y el silbato suenan agudos. La duración de las notas puede ser larga, como una nota sostenida, o corta, como un golpe seco. Cada rasgo responde una pregunta distinta, y por eso no se deben confundir: un sonido puede ser suave y rápido a la vez.",
        "Al describir un fragmento conviene nombrar los cinco rasgos en orden y con palabras precisas. Por ejemplo: «Tempo lento, dinámica suave, timbre de violonchelo, registro grave y notas largas». Si dos fragmentos se comparan, se dice en qué rasgos se parecen y en cuáles se diferencian. Esa precisión es lo que permite relacionar después cada rasgo con el efecto que produce.",
    ],
    [("tempo", "velocidad del pulso, en pulsos por minuto"), ("dinámica", "qué tan fuerte o suave suena la música"), ("timbre", "color propio de cada instrumento o voz"), ("registro", "qué tan grave o agudo es un sonido"), ("duración de las notas", "si las notas son largas o cortas")],
    [
        ("Comparar dos fragmentos", "Fragmento A: 60 pulsos por minuto, suave, guitarra, registro agudo, notas largas. Fragmento B: 120 pulsos por minuto, suave, guitarra, registro agudo, notas cortas. ¿En cuántos de los cinco rasgos se diferencian?", ["Tempo: 60 y 120, distinto.", "Dinámica, timbre y registro: iguales.", "Duración: largas y cortas, distinto."], "En 2 rasgos (tempo y duración)"),
        ("Identificar el rasgo", "«La misma melodía la toca primero una flauta y luego un clarinete.» ¿Qué rasgo cambia?", ["Las notas son las mismas.", "Cambia el instrumento, es decir, su color propio."], "El timbre"),
    ],
    [
        ("Decir que un sonido suave es un sonido lento.", "Suave habla de dinámica; lento habla de tempo, y son rasgos independientes.", "Pregunta por separado: ¿qué tan fuerte y qué tan rápido?"),
        ("Confundir timbre con registro.", "El timbre es el color del instrumento; el registro es qué tan grave o agudo suena.", "Si cambia el instrumento con las mismas notas, cambia el timbre."),
    ],
    [
        ex("La frase «Suena una guitarra» nombra un rasgo. ¿Cuál es: timbre o tempo?", "Timbre", "Nombra qué instrumento suena."),
        ex("La frase «Las notas son muy cortas y separadas» nombra un rasgo. ¿Cuál es: duración o registro?", "Duración", "Habla de cuánto dura cada nota."),
        ex("La frase «La voz canta en la parte grave» nombra un rasgo. ¿Cuál es: registro o dinámica?", "Registro", "Grave o agudo es registro."),
    ],
    [
        ex("Un bombo y una flauta tocan juntos. Según lo que sabes, ¿cuál suena en registro más grave?", "El bombo", "El bombo es un instrumento de sonido grave y la flauta suena aguda."),
        ex("Descripción: «Un bombo suena fuerte, un tambor suena fuerte y un violín suena suave». ¿Cuántos timbres distintos se nombran?", "3", "Son bombo, tambor y violín: tres instrumentos distintos."),
        ex("Si el pulso pasa de 60 a 120 pulsos por minuto, ¿qué rasgo cambió: el tempo o la dinámica?", "El tempo", "Los pulsos por minuto miden la velocidad."),
    ],
    [
        ex("Descripción: «tambor fuerte y rápido; flauta aguda y suave; violonchelo grave y lento». ¿Qué instrumento es a la vez grave y lento?", "El violonchelo", "Es el único al que se le atribuyen los dos rasgos."),
        arith("Un fragmento va a 120 pulsos por minuto. ¿Cuántos pulsos tiene en 30 segundos?", "120//2", "30 segundos son medio minuto, así que se toma la mitad de los pulsos de un minuto.", " pulsos"),
        arith("Un fragmento tiene 25 pulsos y va a 50 pulsos por minuto. ¿Cuántos segundos dura?", "25*60//50", "Se pasan los pulsos a minutos y luego a segundos: 25 ÷ 50 de minuto.", " segundos"),
    ],
    [
        ex("Pedro dice «es lento porque es suave». ¿Qué dos rasgos confundió?", "Dinámica y tempo", "Suave es dinámica y lento es tempo."),
        arith("Un fragmento tiene 25 pulsos. A 50 pulsos por minuto dura 30 segundos y a 100 dura 15. ¿Cuántos segundos más dura el lento?", "25*60//50-25*60//100", "Se resta la duración del rápido a la del lento.", " segundos más"),
    ],
    [
        ex("Un fragmento tiene tempo moderado, dinámica fuerte y flauta. Quieres cambiar su efecto de «tranquilo» a «enérgico» sin cambiar de instrumento. ¿Qué rasgo es más lógico cambiar: el tempo o el timbre?", "El tempo", "Cambiar el timbre significaría cambiar de instrumento, que no se puede."),
        ex("Dos fragmentos suenan igual de rápido y de fuerte, pero en uno toca una trompeta y en el otro un clarinete. ¿En qué rasgo se diferencian?", "En el timbre", "Cambia el instrumento, no el tempo ni la dinámica."),
    ],
    [ex("Escuchas una descripción de una mañana de feria: «un tambor suena rápido y fuerte; una flauta aguda toca notas cortas». ¿Cuántos de los cinco rasgos de la clase aparecen nombrados (tempo, dinámica, timbre, registro, duración)?", "5", "Tempo (rápido), dinámica (fuerte), timbre (tambor y flauta), registro (aguda) y duración (notas cortas).")],
    [ex("¿Qué rasgo mide la velocidad del pulso?", "El tempo", "Se mide en pulsos por minuto."), ex("¿Qué rasgo nos permite distinguir una flauta de un violín que tocan la misma nota?", "El timbre", "El color del instrumento."), ex("El sonido de un bombo, ¿es de registro grave o agudo?", "Grave", "Lo grave es lo bajo de altura.")],
    (
        "Describe con los cinco rasgos este fragmento inventado: «Un violonchelo toca lentamente, a 60 pulsos por minuto; sus notas son largas, suena muy suave y en la parte grave». Luego cambia dos rasgos para que se parezca a una fiesta en una plaza (por ejemplo, cambiando el instrumento y el tempo) y escribe el nuevo fragmento con sus cinco rasgos.",
        "Original: tempo lento (60), dinámica muy suave, timbre de violonchelo, registro grave, notas largas. Nueva versión: tempo rápido (120), dinámica fuerte, timbre de guitarra y tambor, registro medio-agudo, notas cortas. Se parece a una fiesta porque va rápido, fuerte y con notas cortas.",
        ["nombra bien los cinco rasgos", "cambia dos o más rasgos con intención", "explica el efecto con evidencia"],
        ["lista de cinco rasgos", "nuevo fragmento escrito"],
        ["confundir dinámica con tempo", "describir sin dar el número de pulsos"],
        "Reconoce el análisis y pide señalar cuáles rasgos cambiaron en la nueva versión y cuáles no.",
    ),
    "Di en voz baja la palabra «música» lento y suave, y luego rápido y fuerte, y nombra qué rasgos cambiaste.",
    "Describe con los cinco rasgos tres sonidos de tu casa o de tu calle, sin nombrar el objeto.",
)

# ---------------------------------------------------------------- OA 01 · clase 3 (rasgos que producen efectos; tradición oral, escrita y popular)
L(
    OA1, 3,
    "Lápiz y papel. Todos los fragmentos están descritos en los ejercicios. No necesitas audio. Si quieres, tararea o golpea la mesa suavemente para probar cada combinación de rasgos.",
    "Aprenderé a relacionar los rasgos audibles con el efecto que producen, y a reconocer si una música viene de la tradición oral, escrita o popular. Sirve para explicar por qué una música, de Chile o de otro lugar, nos hace sentir algo.",
    ["Sé reconocer tempo, dinámica, timbre, registro y duración.", "Sé que una canción puede aprenderse escuchando o leyendo.", "Sé separar lo que se oye de lo que siento."],
    [
        "Cada combinación de rasgos suele producir un efecto parecido en mucha gente, aunque no en todas las personas. Un tempo lento, una dinámica suave y un registro grave suelen dar calma o solemnidad. Un tempo rápido, una dinámica fuerte y notas cortas suelen dar energía o ganas de moverse. Un registro agudo con volumen suave suele dar delicadeza o ligereza. Un cambio de suave a fuerte de golpe suele dar sorpresa.",
        "Estas relaciones son tendencias, no reglas exactas. Por eso la descripción debe decir «suele» y apoyarse en lo que se oye. La música también viene de distintas tradiciones. La tradición oral se aprende escuchando y repitiendo, sin partitura: canciones de cuna, juegos cantados y cantos de trabajo. La tradición escrita se conserva en partitura: por ejemplo, la música de concierto de compositores como Beethoven. La música popular se difunde por radio, discos e internet: cumbia, rock, pop.",
        "Una misma pieza puede pertenecer a más de una tradición. La cueca, la danza nacional de Chile, se aprende oyendo y bailando, y también existe escrita y grabada. Lo importante es reconocer cómo se transmite la música y explicar el efecto con evidencia: «Esta música da energía porque va rápida, fuerte y con notas cortas». Así relacionamos el lenguaje musical con lo que sentimos, sin depender del gusto.",
    ],
    [("efecto", "lo que un rasgo musical suele provocar en quien escucha"), ("tradición oral", "música que se aprende escuchando y repitiendo, sin partitura"), ("tradición escrita", "música que se conserva y se aprende leyendo partitura"), ("música popular", "música difundida masivamente por radio, discos e internet"), ("solemnidad", "sensación de seriedad y respeto")],
    [
        ("Relacionar rasgo y efecto", "Un fragmento va a 55 pulsos por minuto, muy suave y grave. ¿Qué efecto suele producir: calma o energía?", ["Tempo lento, volumen suave y registro grave.", "Esa combinación suele dar calma."], "Calma"),
        ("Reconocer la tradición", "Una abuela le enseña a su nieta una canción de cuna cantándola varias noches, sin papel. ¿De qué tradición es la forma de aprenderla?", ["No hay partitura.", "Se aprende escuchando y repitiendo."], "Tradición oral"),
    ],
    [
        ("Creer que un rasgo siempre produce el mismo efecto en todas las personas.", "Los efectos son tendencias, y cada persona puede sentir algo distinto.", "Escribe «suele» y da la evidencia audible."),
        ("Creer que la música popular no puede ser tradición oral ni escrita.", "Una misma obra puede transmitirse de varias maneras al mismo tiempo.", "Pregunta cómo se transmite, no solo dónde suena."),
    ],
    [
        ex("Un tempo rápido y una dinámica fuerte con notas cortas, ¿suelen dar energía o calma?", "Energía", "Esa combinación activa y da ganas de moverse."),
        ex("Una música que se aprende leyendo una partitura, ¿es de tradición oral o escrita?", "Escrita", "La partitura es el medio de transmisión de la tradición escrita."),
        ex("Un juego cantado que los niños aprenden en el patio escuchando a los mayores, ¿es de tradición oral o escrita?", "Oral", "Se aprende escuchando y repitiendo, sin partitura."),
    ],
    [
        ex("Un volumen suave con registro agudo, ¿suele dar delicadeza o solemnidad?", "Delicadeza", "Lo agudo y suave se oye liviano y fino."),
        ex("Un cambio de volumen de muy suave a muy fuerte en un solo golpe, ¿suele producir sorpresa o calma?", "Sorpresa", "El cambio brusco rompe lo esperado."),
        ex("Una canción nueva se difunde por la radio y en internet y mucha gente la conoce. ¿Es música popular, escrita u oral?", "Popular", "Se difunde masivamente por medios como la radio e internet."),
    ],
    [
        ex("Fragmento: 50 pulsos por minuto, dinámica suave, violonchelo, notas largas. ¿Qué efecto es más probable: solemnidad o ganas de bailar?", "Solemnidad", "Lento, suave y grave suele dar seriedad; para bailar se necesita un pulso más vivo."),
        ex("La cueca se aprende oyendo y bailando en las fiestas, y también hay cuecas escritas en partitura. ¿Cuántas tradiciones de la clase (oral, escrita, popular) aparecen en esa descripción?", "2", "Aparecen la oral (se aprende oyendo) y la escrita (hay cuecas en partitura)."),
        arith("Un fragmento va a 120 pulsos por minuto. ¿Cuántos pulsos hay en 45 segundos?", "120*45//60", "45 segundos son 45/60 de minuto; se multiplica y se divide.", " pulsos"),
    ],
    [
        ex("Laura dice: «Todo el mundo siente alegría con el tempo rápido». ¿Cómo corregirías su frase para que sea más precisa: «suele dar energía» o «siempre da alegría»?", "«Suele dar energía»", "Los efectos son tendencias y dependen de la persona y del resto de los rasgos."),
        ex("Dos fragmentos comparten tempo lento y volumen suave, pero uno es en registro grave y otro en registro agudo. Con la regla de la clase, ¿cuál suena más delicado?", "El de registro agudo", "Lo agudo y suave suele dar delicadeza; lo grave se siente más pesado."),
    ],
    [
        ex("Una niña canta a su hermano una canción que aprendió de su abuelo sin partitura, y un cantante la graba y la difunde en internet. ¿Qué dos tradiciones aparecen: oral y popular o escrita y popular?", "Oral y popular", "Se aprendió de boca en boca (oral) y luego se difunde masivamente (popular)."),
        ex("Un compositor escribe una pieza para orquesta en partitura. Al mismo tiempo, un grupo de vecinos la aprende de memoria, escuchando y repitiendo entre ellos, sin leer la partitura. ¿Qué dos formas de transmisión hay: escrita y oral o escrita y popular?", "Escrita y oral", "La partitura es escrita y el aprendizaje de memoria, escuchando y repitiendo, es oral."),
    ],
    [ex("En una feria de barrio suena una música de tempo moderado, volumen fuerte y tambores que marcan notas cortas. Una vecina dice que da ganas de bailar. ¿Qué dos rasgos apoyan mejor su opinión: dinámica fuerte y notas cortas o registro grave y notas largas?", "Dinámica fuerte y notas cortas", "Esos rasgos dan energía y ganas de moverse.")],
    [ex("¿Qué palabra conviene usar para decir que un efecto no es una regla exacta?", "Suele", "Indica una tendencia."), ex("¿Qué tradición se transmite con partitura?", "La escrita", "La partitura es su medio."), ex("¿Qué efecto suele producir un tempo lento, suave y grave?", "Calma o solemnidad", "Esa combinación se oye serena.")],
    (
        "Lee estos tres fragmentos inventados. Fragmento A: canción de cuna cantada sin partitura, muy suave y lenta, voz sola. Fragmento B: pieza de concierto leída en partitura, rápida y fuerte, orquesta. Fragmento C: canción que suena por la radio, moderada, con guitarra eléctrica y voz. Elige dos fragmentos y escribe: la tradición, dos rasgos audibles y el efecto que suele producir, con la frase «Suele dar … porque …».",
        "A: tradición oral; rasgos: voz sola, muy suave y lenta; suele dar calma porque canta despacio y suave. B: tradición escrita; rasgos: rápida y fuerte, con orquesta; suele dar energía porque va rápida y fuerte.",
        ["identifica la tradición de cada fragmento", "nombra dos rasgos audibles por fragmento", "relaciona rasgos y efecto con «suele»"],
        ["tabla de dos fragmentos", "frases con evidencia"],
        ["afirmar que un efecto es siempre igual", "no distinguir entre sensación y evidencia"],
        "Reconoce la tabla y pide revisar que cada efecto se apoye en rasgos que sí aparecen en la descripción.",
    ),
    "Escribe una canción de cuna o un juego cantado que conozcas y di si lo aprendiste de forma oral o escrita.",
    "Describe un caso de una música que pertenece a dos tradiciones a la vez y explica cómo se transmite.",
)

# ---------------------------------------------------------------- OA 01 · clase 4 (manifestar lo que sentimos por medios verbales, visuales, sonoros y corporales)
CONV = "línea que sube = melodía que sube; línea que baja = melodía que baja; trazo grueso = sonido fuerte; trazo fino = sonido suave; línea larga = nota larga; puntos = notas cortas"

L(
    OA1, 4,
    f"Lápiz y papel. Convención de dibujo de la clase: {CONV}. Para el medio sonoro y el corporal, usa tu voz y tus manos a volumen bajo y con movimientos tranquilos, de pie o sentado, sin saltos ni giros.",
    "Aprenderé a mostrar lo que siento al escuchar de cuatro maneras: con palabras, con un dibujo, con sonidos y con movimientos. Sirve para compartir mi experiencia de una música de forma clara y respetuosa.",
    ["Sé separar lo que se oye de lo que siento.", "Sé relacionar rasgos y efectos.", "Sé que hay música oral, escrita y popular."],
    [
        "Lo que sentimos al escuchar se puede manifestar de cuatro maneras. El medio verbal usa palabras: una frase con la sensación y su evidencia. El medio visual usa dibujos o líneas: una línea que sube representa una melodía que sube, un trazo grueso un sonido fuerte, un trazo fino uno suave, y los puntos, notas cortas. El medio sonoro responde con sonidos de tu voz o de objetos, por ejemplo golpes suaves o un «la» largo. El medio corporal responde con movimiento.",
        "En el medio corporal, un movimiento grande y amplio acompaña un sonido fuerte y uno pequeño y lento acompaña un sonido suave. Los movimientos rápidos siguen un tempo rápido y los lentos, uno lento. Conviene moverse con tranquilidad y en un espacio libre, sin riesgo. Nadie está obligado a mostrar su movimiento ante otras personas: puede hacerlo en privado o elegir otro medio.",
        "Cada medio muestra la misma música de forma distinta, y ninguno es mejor que otro. Lo importante es que la respuesta tenga evidencia: quien mira tu dibujo, oye tus sonidos o ve tu movimiento debe poder reconocer qué rasgos de la música usaste. Una buena manifestación se puede comprobar volviendo a escuchar. Así se une lo que se oye con lo que siento y lo que imagino.",
    ],
    [("medio verbal", "mostrar con palabras lo que siento y su evidencia"), ("medio visual", "mostrar con un dibujo o línea los rasgos de la música"), ("medio sonoro", "mostrar con sonidos de la voz u objetos"), ("medio corporal", "mostrar con movimiento tranquilo y seguro"), ("manifestar", "expresar hacia afuera lo que siento o pienso")],
    [
        ("Leer un dibujo", "Un dibujo muestra una línea gruesa que sube y luego se vuelve fina y baja. ¿Qué melodía representa?", ["Línea gruesa que sube: melodía fuerte que sube.", "Luego trazo fino que baja: sonido suave que baja."], "Una melodía fuerte que sube y luego baja suave"),
        ("Elegir el medio", "Un estudiante quiere mostrar que la música era lenta y tranquila, sin hablar. ¿Cómo puede moverse?", ["Lento y tranquilo se relaciona con movimientos pequeños y lentos.", "Los movimientos rápidos no calzan con un tempo lento."], "Con movimientos pequeños y lentos"),
    ],
    [
        ("Dibujar solo lo que imagino y olvidar los rasgos de la música.", "El dibujo debe permitir reconocer rasgos como dirección, volumen y duración.", "Usa la convención de líneas y puntos de la clase."),
        ("Pensar que quien no se mueve frente a otros no puede participar.", "Puedes elegir otro medio o hacerlo en privado.", "Elige el medio con que te sientas cómodo."),
    ],
    [
        ex("Una línea que baja en un dibujo, ¿representa una melodía que sube o que baja?", "Que baja", "Con la convención de la clase, línea que baja = melodía que baja."),
        ex("En el dibujo, ¿un trazo fino representa un sonido fuerte o suave?", "Suave", "Trazo fino = suave."),
        ex("¿Qué medio usa palabras: el verbal, el visual, el sonoro o el corporal?", "El verbal", "Es el que muestra lo que siento con palabras."),
    ],
    [
        ex("Dibujo: ● ● ● ● (puntos seguidos). ¿Qué duración de notas representa: cortas o largas?", "Cortas", "Los puntos representan notas cortas."),
        ex("Quieres mostrar con el cuerpo un sonido fuerte y rápido. ¿Qué movimiento calza mejor: grande y rápido o pequeño y lento?", "Grande y rápido", "El tamaño sigue la fuerza y la rapidez sigue el tempo."),
        ex("Una persona responde a una música golpeando suavemente la mesa. ¿Qué medio usa: sonoro o visual?", "Sonoro", "Responde con sonidos."),
    ],
    [
        ex("Un dibujo tiene primero una línea gruesa y larga que baja y luego tres puntos finos. ¿Qué melodía muestra: una nota fuerte, larga y descendente seguida de tres notas suaves y cortas, o tres notas fuertes y cortas seguidas de una larga suave?", "Una nota fuerte, larga y descendente seguida de tres notas suaves y cortas", "Primero línea gruesa, larga y que baja; después puntos finos."),
        ex("Una música sube de a poco y cada vez más fuerte. ¿Cómo la dibujarías: línea que sube y se engrosa o línea que baja y se afina?", "Línea que sube y se engrosa", "Sube la melodía y aumenta el volumen."),
        ex("Cuenta cuántos de los cuatro medios (verbal, visual, sonoro, corporal) usa esta persona: «Escribí una frase, hice un dibujo con líneas y marqué el pulso golpeando la mesa con un lápiz».", "3", "Usa el verbal, el visual y el sonoro; los golpes con el lápiz son sonido."),
    ],
    [
        ex("Una compañera no quiere mostrar sus movimientos frente al curso. ¿Qué respuesta es más respetuosa: obligarla o ofrecerle otro medio?", "Ofrecerle otro medio", "Nadie debe ser obligado a exponerse y puede participar con otra forma."),
        ex("Dos estudiantes dibujan la misma música: uno con una línea que sube y otro con una línea que baja. Si la melodía sube, ¿quién tiene el dibujo correcto?", "El de la línea que sube", "El dibujo debe seguir lo que se oye: la melodía sube."),
    ],
    [
        ex("Un dibujo muestra: línea fina y larga que sube; después un punto grueso. Un estudiante dice que la música empieza con un sonido suave y largo que sube y que termina con un golpe fuerte y corto. ¿Es correcta su lectura? Responde sí o no.", "Sí", "La línea fina y larga que sube es un sonido suave y largo que sube; el punto grueso es una nota corta y fuerte."),
        ex("Quieres que un movimiento muestre una melodía que empieza fuerte y termina suave. ¿Qué movimiento calza: empezar con un gesto amplio y terminar con uno pequeño o al revés?", "Empezar con un gesto amplio y terminar con uno pequeño", "El tamaño del gesto sigue el volumen."),
    ],
    [ex("Un fragmento tiene este esquema: primero notas largas y suaves que suben; luego notas cortas y fuertes que bajan. ¿Qué dibujo es correcto: A) línea fina que sube y luego puntos gruesos que bajan o B) línea gruesa que baja y luego puntos finos que suben?", "A", "Fina = suave, larga = nota larga, sube; luego gruesos = fuertes, puntos = cortas, bajan.")],
    [ex("¿Qué debe tener toda manifestación de lo que siento para poder comprobarse?", "Evidencia de la música", "Debe poder verse, oírse o leerse qué rasgos usó."), ex("¿Qué medio usa movimientos tranquilos y seguros?", "El corporal", "Es el que responde con el cuerpo."), ex("¿Puede una persona elegir qué medio usar para participar?", "Sí", "Ninguno es mejor que otro y nadie está obligado a exponerse.")],
    (
        "Usa este fragmento inventado: «Una flauta toca notas largas y suaves que suben despacio; luego un tambor entra con golpes cortos y fuertes; al final todo baja y se calma». Responde con dos medios distintos a tu elección (verbal, visual, sonoro o corporal): por ejemplo, escribe una frase con «porque» y dibuja la línea con la convención de la clase, o muévete tranquilo y escribe qué rasgos mostraste.",
        "Medio verbal: «Siento expectativa y luego calma porque la flauta sube despacio y suave, el tambor entra fuerte con notas cortas y al final todo baja». Medio visual: línea fina y larga que sube; después puntos gruesos; al final línea que baja y se afina.",
        ["usa dos medios distintos", "muestra al menos tres rasgos de la música", "se puede comprobar volviendo al fragmento"],
        ["frase escrita", "dibujo con líneas y puntos", "descripción del movimiento"],
        ["no mostrar los rasgos de la música", "forzar un medio que incomoda"],
        "Reconoce los dos medios y pide señalar en el dibujo o en la frase dónde se ve cada rasgo del fragmento.",
    ),
    "Dibuja una línea con trazos gruesos y finos que represente una melodía que sube fuerte y baja suave.",
    "Elige un fragmento de tu casa y manifiéstalo con los cuatro medios, explicando qué rasgos mostró cada uno.",
)
