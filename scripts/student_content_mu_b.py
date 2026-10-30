"""Student material for 1.º básico Música, OA 03 (escucha abundante de músicas de diversos contextos) y OA 04 (canto al unísono y percusión)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_content_mu_a import LEY, SIL, TA, TT, P, sounds
from student_lessons import ex, register

OA3, OA4 = "MU01 OA 03", "MU01 OA 04"

# ---------------------------------------------------------------- OA 03
register(
    OA3, 1,
    materials="Lápiz y una hoja. Las músicas de esta clase están descritas por escrito; un adulto puede leer la descripción o hacer sonar objetos de la casa. No hace falta internet ni parlante.",
    use="Aprenderé a prepararme para escuchar con atención: qué mirar, qué oír y cuándo escuchar de nuevo. Sirve para disfrutar y comprender más cualquier música.",
    prior=["Sé quedarme en silencio unos segundos.", "Sé decir si un sonido es fuerte o suave, rápido o lento.", "Sé que contraste es una parte distinta de la anterior."],
    explain=[
        "Escuchar con atención es distinto de oír de fondo. Oímos de fondo cuando hay música mientras hacemos otra cosa. Escuchamos con atención cuando dejamos lo que hacemos, quedamos en silencio y ponemos la mente en los sonidos. Así notamos detalles que antes no veíamos.",
        "Antes de escuchar, piensa qué vas a observar. Puedes buscar qué instrumentos o voces suenan, si va rápido o lento, si es fuerte o suave, y si hay partes que se repiten. No sabes la respuesta antes: solo decides dónde poner tu oído. Después de escuchar, cuenta qué notaste.",
        "Conviene escuchar dos veces. La primera vez, para sentir y quedarte con una impresión general. La segunda, para buscar la pista que respalda tu idea. Si algo no lo entiendes o no lo sabes, puedes decir «no lo sé todavía». Eso también es una respuesta honesta.",
    ],
    vocab=[("escuchar con atención", "poner todo mi oído en un sonido"), ("oír de fondo", "oír música mientras hago otra cosa"), ("observar", "buscar algo con atención"), ("instrumento", "objeto hecho para hacer música"), ("impresión", "lo primero que siento o noto")],
    worked=[
        {"title": "Elegir qué observar", "problem": "Vas a escuchar una música desconocida. Eliges observar tres cosas. ¿Cuáles puedes elegir?", "steps": ["Pienso en lo que se puede oír: instrumentos, rapidez y fuerza.", "Elijo tres: si hay voz o instrumentos, si va rápido o lento y si es fuerte o suave.", "Los anoto antes de escuchar."], "answer": "Voz o instrumentos; rápido o lento; fuerte o suave"},
        {"title": "Escuchar dos veces", "problem": "Tu mamá toca golpes de cuchara en un tarro, lentos y suaves, y a la mitad aparece un cascabel. ¿Para qué escuchas dos veces?", "steps": ["La primera vez noto que es lento y suave, y que cambia a la mitad.", "La segunda vez busco cuándo aparece el cascabel.", "Así puedo explicar mi idea con una pista exacta."], "answer": "Para quedarme con una impresión y luego buscar la pista"},
    ],
    mistakes=[
        {"wrong": "Decir qué es la música antes de escucharla.", "why": "Se cree que ya se sabe la respuesta.", "fix": "Primero decide qué observar y después escucha para comprobarlo."},
        {"wrong": "Escuchar con la música de fondo mientras juego.", "why": "No se pone atención en los sonidos.", "fix": "Deja lo que haces y quédate en silencio, aunque sea un minuto."},
    ],
    tiers={
        "recovery": [
            ex("Si pones música mientras juegas y no la miras, ¿escuchas con atención o de fondo?", "De fondo", "La atención está puesta en el juego."),
            ex("Antes de escuchar con atención, ¿qué debes hacer con lo que tienes en las manos?", "Dejarlo", "La atención necesita calma y silencio."),
            ex("¿Cuántas veces conviene escuchar una música para comprenderla mejor?", "Dos", "La primera para sentir y la segunda para buscar pistas."),
        ],
        "understand": [
            ex("¿Para qué decides qué observar antes de escuchar?", "Para saber dónde poner el oído", "Así escuchas con un propósito."),
            ex("Escuchas una música y no sabes qué instrumento es. ¿Qué respuesta honesta puedes dar?", "No lo sé todavía", "Es mejor decirlo que inventar."),
            ex("¿Qué haces en la segunda escucha?", "Buscar la pista que respalda mi idea", "La segunda escucha confirma lo que noté."),
        ],
        "apply": [
            ex("Un adulto toca una pandereta rápida y fuerte. Escribe qué observarías sobre su rapidez y su fuerza.", "Rápida y fuerte", "Esas son dos pistas que se pueden oír."),
            ex("Escoge tres cosas para observar en una música con voz. Usa estas opciones: instrumentos, voz, rapidez, fuerza, silencio, repetición.", "Cualquier tres de las seis opciones, por ejemplo voz, rapidez y repetición", "Todas se pueden observar al escuchar."),
            ex("Un adulto tararea una melodía lenta y suave y luego la repite igual. ¿Qué se repitió?", "La melodía", "Volvió a sonar igual."),
        ],
        "reason": [
            ex("Ema escuchó solo una vez y dijo que la música era toda igual. Tras escuchar otra vez, notó que cambió a la mitad. ¿Qué mostró esta segunda escucha?", "Que se pueden descubrir más detalles al escuchar de nuevo", "Un cambio a la mitad se nota con más atención."),
            ex("¿Por qué no es buena idea decir «es aburrida» antes de escuchar?", "Porque aún no se ha escuchado", "Hay que escuchar antes de decidir."),
        ],
        "challenge": [
            ex("Armas una lista de cuatro cosas para observar en una música. Anótala usando las palabras del cuaderno.", "Por ejemplo: instrumentos, rapidez, fuerza y partes que se repiten", "Son cosas que se pueden oír y anotar."),
            ex("Si la música sigue igual de principio a fin, ¿qué respondes cuando te preguntan si hubo contraste?", "No, no hubo contraste", "Contraste es una parte distinta y aquí no la hubo."),
        ],
    },
    context=[ex("En el auto suena música mientras tu familia conversa. Tú quieres escucharla con atención. ¿Qué le pides a las personas y qué haces?", "Pido un momento de silencio y pongo todo mi oído en la música", "Escuchar con atención necesita silencio y concentración.")],
    selfcheck=[ex("¿Cómo se llama oír música sin ponerle atención?", "Oír de fondo", "No hay atención puesta en el sonido."), ex("¿Qué se hace antes de escuchar?", "Decidir qué observar", "Eso guía el oído."), ex("¿Qué dices si no sabes qué instrumento suena?", "No lo sé todavía", "Es una respuesta honesta.")],
    open_task=task(
        "Un adulto toca dos veces esta música con una cuchara y un tarro: golpes lentos y suaves, luego golpes rápidos y fuertes. Antes de escuchar, escribe qué vas a observar (elige tres de: rapidez, fuerza, repetición, silencio). Después escucha dos veces y anota qué notaste en cada escucha.",
        "Voy a observar rapidez, fuerza y repetición. En la primera escucha noté que cambia de lento a rápido. En la segunda noté que los golpes rápidos también eran más fuertes.",
        ["elige qué observar antes de escuchar", "escucha dos veces", "anota algo distinto en cada escucha"],
        ["lista escrita antes de escuchar", "dos anotaciones", "conversación"],
        ["decidir la respuesta antes de escuchar", "repetir exactamente lo mismo en ambas escuchas"],
        "Reconoce que su lista guió el oído y pregunta qué descubrió en la segunda escucha; si repitió la misma idea, pide una pista más exacta.",
    ),
    reinforce="Escucha un sonido de tu casa (el agua, la puerta) durante un minuto en silencio y cuenta qué notaste.",
    extend="Escucha dos músicas distintas de tu casa y cuenta qué observaste primero en cada una.",
)

register(
    OA3, 2,
    materials=f"Lápiz y tus palmas. Patrón para tocar: {P(TT, TA, TT, TA)} ({LEY}). Las músicas de tradición oral están descritas por escrito; un adulto puede cantar una ronda o dar el ejemplo con palmas.",
    use="Aprenderé a reconocer la tradición oral: músicas que se aprenden de persona a persona. Sirve para valorar rondas, canciones y bailes que pasan de abuelos a niños.",
    prior=["Sé qué es una ronda.", "Sé repetir un sonido o un verso que oigo."],
    explain=[
        "La tradición oral es música que se aprende escuchando y repitiendo, sin partitura. Los abuelos, los padres y los niños la cantan y la pasan a otras personas. Así viven las rondas, los juegos cantados, los bailes y los versos rítmicos que se dicen con las manos o los pies.",
        "En la tradición oral casi siempre participan muchas personas a la vez. Todos cantan, aplauden o bailan. Hay repeticiones: la misma frase vuelve varias veces, lo que ayuda a recordarla. Y siempre hay un contexto: se canta para jugar, para dormir, para celebrar o para bailar.",
        "Muchos pueblos originarios de Chile y del mundo tienen músicas de tradición oral con tambores, flautas, sonajas y cantos que enseñan las personas mayores de la comunidad. Para conocer cada música de manera correcta hay que escuchar a quienes la guardan. Aquí solo aprendemos a reconocer las características generales.",
    ],
    vocab=[("tradición oral", "música que se aprende de persona a persona, sin partitura"), ("ronda", "canción para jugar en círculo"), ("participar", "cantar, tocar o bailar junto a otros"), ("repetición", "frase o parte que vuelve a sonar"), ("contexto", "dónde, cuándo y para qué se hace la música")],
    worked=[
        {"title": "Reconocer una música de tradición oral", "problem": "Un grupo de niños juega en ronda, canta una frase corta cuatro veces y aplaude el pulso. Nadie lee ningún papel. ¿Por qué parece tradición oral?", "steps": ["Se aprende escuchando y repitiendo, sin papel.", "Participan todos: cantan y aplauden.", "La frase vuelve a sonar cuatro veces."], "answer": "Porque se aprende de oído, participan todos y hay repetición"},
        {"title": "Decir el contexto", "problem": "Una abuela canta bajito una canción para dormir a su nieto. ¿Cuál es el contexto?", "steps": ["Pregunto dónde y para qué suena la música.", "Se canta en la casa, de noche.", "Sirve para tranquilizar y hacer dormir."], "answer": "Se canta en casa para dormir a un niño"},
    ],
    mistakes=[
        {"wrong": "Pensar que una canción de tradición oral es «menos importante» porque no está escrita.", "why": "Se cree que solo lo escrito vale.", "fix": "La tradición oral se cuida por las personas que la cantan; es otra manera de guardar música."},
        {"wrong": "Decir que todas las músicas de los pueblos originarios suenan igual.", "why": "Se resume una tradición en una sola pieza.", "fix": "Cada pueblo tiene sus propias músicas; para conocer una, escucha a quienes la guardan."},
    ],
    tiers={
        "recovery": [
            ex("La música de tradición oral, ¿se aprende leyendo una partitura o escuchando y repitiendo?", "Escuchando y repitiendo", "Pasa de persona a persona."),
            ex("Una ronda se juega, ¿en fila o en círculo?", "En círculo", "La ronda es una rueda."),
            ex("En una ronda, ¿participa una persona o todo el grupo?", "Todo el grupo", "En la tradición oral participan muchos."),
        ],
        "understand": [
            ex("¿Por qué las repeticiones ayudan a recordar una canción de tradición oral?", "Porque la frase vuelve y se aprende de memoria", "Repetir ayuda a recordar sin papel."),
            ex("¿Quién suele enseñar la música de un pueblo originario?", "Las personas mayores de la comunidad", "Ellos guardan y transmiten el saber."),
            ex("¿Qué es el contexto de una música?", "Dónde, cuándo y para qué suena", "Ayuda a entender su función."),
        ],
        "apply": [
            ex(f"Toca con las palmas el patrón {P(TT, TA, TT, TA)}. ¿Cuántos sonidos suenan?", str(sounds(TT, TA, TT, TA)), "ti-ti da 2, TA da 1, ti-ti da 2 y TA da 1: 2 + 1 + 2 + 1 = 6."),
            ex("Una rueda de niños canta y gira para celebrar un cumpleaños. Escribe el contexto en una frase.", "Se canta en círculo para celebrar un cumpleaños", "Dice dónde, cómo y para qué."),
            ex("Una frase de cuatro sílabas se repite tres veces en una ronda. ¿Cuántas sílabas se cantan en total?", "12", "4 sílabas × 3 veces = 12."),
        ],
        "reason": [
            ex("Ana dice «esta ronda no vale porque nadie la escribió». ¿Qué le responderías?", "Que se guarda en la memoria de las personas y por eso también vale", "La tradición oral se mantiene al cantarla."),
            ex("Dos niños escuchan una música tradicional de un pueblo originario. Uno dice «todas las músicas de pueblos originarios suenan así». ¿Qué falta?", "Cada pueblo tiene muchas músicas distintas", "Una pieza no representa una tradición completa."),
        ],
        "challenge": [
            ex("Inventa una frase corta de 4 pulsos que se pueda repetir como en una ronda. Escríbela con los símbolos de la clase.", f"Por ejemplo: {P(TA, TA, TT, TA)}", "Una frase corta y repetible se aprende de oído."),
            ex("Cuenta tres cosas que ayudan a que una canción se pase de abuelos a nietos sin partitura.", "Que sea corta, que se repita y que se cante en grupo", "Esas características facilitan la memoria."),
        ],
    },
    context=[ex("En una fiesta del barrio todos hacen un círculo, cantan un estribillo que se repite y aplauden el pulso. Nadie lee letras. ¿Qué tipo de música es y cómo lo sabes?", "Tradición oral; se aprende de oído, participan todos y hay repetición", "Reúne las tres características de la clase.")],
    selfcheck=[ex("¿Cómo se aprende la tradición oral?", "Escuchando y repitiendo", "No necesita partitura."), ex("Nombra una forma de participar en una ronda.", "Cantar, aplaudir o bailar", "Todos pueden participar así."), ex("¿Qué debemos hacer para conocer bien la música de un pueblo originario?", "Escuchar a las personas que la guardan", "Ellos conocen su tradición.")],
    open_task=task(
        f"Aprende de oído una ronda de palmas. Un adulto lee este patrón en secreto: {P(TT, TA, TT, TA)}. Que lo toque con las palmas sin mostrarte el papel y tú lo repites tres veces. Luego enséñaselo tú a otra persona. Cuenta quién participó, cuántas veces se repitió y para qué podría servir.",
        "Mi hermano me enseñó la ronda y yo la repetí tres veces. Se la enseñé a mi abuela. Participamos tres personas y se puede usar para jugar en ronda.",
        ["aprende el patrón escuchando, sin mirar el papel", "lo repite varias veces", "cuenta quién participó y para qué podría servir"],
        ["interpretación", "frase escrita", "explicación oral"],
        ["leer en vez de escuchar", "tocar sin repetir"],
        "Reconoce que aprendió de oído y pregunta cómo supo que lo hacía igual; si cambió el patrón, vuelve a escucharlo despacio.",
    ),
    reinforce="Aprende de memoria una ronda corta de tu familia o de tu curso y cántala dos veces.",
    extend="Pregunta a un adulto de tu familia qué canción o juego cantado aprendió de pequeño y cuéntalo.",
)

register(
    OA3, 3,
    materials="Lápiz y una hoja. Las piezas están descritas por escrito; un adulto puede leerlas o tocar notas sueltas en un instrumento si lo tiene.",
    use="Aprenderé a reconocer la tradición escrita: música que un compositor guardó en partitura. Sirve para entender cómo una misma pieza puede tocarse de nuevo en otro lugar.",
    prior=["Sé nombrar algunos instrumentos como piano, violín y flauta.", "Sé decir si una parte se repite."],
    explain=[
        "La tradición escrita, también llamada docta, es música que un compositor escribió en una partitura. La partitura es como una receta: dice qué notas tocar, cuánto duran y qué tan fuerte. Así, personas distintas pueden tocar la misma pieza en lugares y años diferentes.",
        "Algunas piezas son muy breves y están pensadas para niños y jóvenes. Un ejemplo es el «Álbum para la juventud» del compositor Robert Schumann, que reúne piezas cortas para piano. Otra colección de piezas cortas se llama «Juguetería», de P. Bisquert. En estas piezas se pueden escuchar los instrumentos y las secciones.",
        "Al escuchar tradición escrita, observa qué instrumentos o voces suenan, si hay partes que regresan y cómo cambian la fuerza y la rapidez. Describe lo que oyes, por ejemplo: «un piano toca notas suaves y lentas, y la primera parte regresa al final».",
    ],
    vocab=[("tradición escrita", "música guardada en una partitura"), ("compositor", "persona que crea y escribe música"), ("partitura", "papel con las notas y el modo de tocarlas"), ("pieza", "una obra musical completa y corta"), ("intérprete", "persona que toca o canta la música")],
    worked=[
        {"title": "Describir una pieza", "problem": "Un adulto describe: un piano toca notas suaves y lentas durante ocho pulsos; luego notas rápidas y fuertes; al final regresa la primera parte. ¿Qué instrumento suena y cuál es su forma?", "steps": ["El instrumento mencionado es un piano.", "Primera parte: suave y lenta (A). Segunda: rápida y fuerte (B).", "Al final vuelve la primera parte (A)."], "answer": "Piano; forma A – B – A"},
        {"title": "Entender para qué sirve la partitura", "problem": "Una pianista toca hoy una pieza que se escribió hace muchos años. ¿Cómo supo qué tocar?", "steps": ["La partitura guarda las notas y su duración.", "La intérprete lee la partitura.", "Así puede tocar la pieza como el compositor la escribió."], "answer": "Leyendo la partitura"},
    ],
    mistakes=[
        {"wrong": "Pensar que la música docta es solo música antigua.", "why": "Se une «escrita» con «de hace mucho».", "fix": "La tradición escrita también se compone hoy; lo importante es que se guarda en partitura."},
        {"wrong": "Decir que la tradición escrita es mejor que la oral.", "why": "Se juzga un estilo como superior.", "fix": "Son maneras distintas de guardar y compartir música."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama la persona que crea y escribe una pieza?", "Compositor", "Compone la música y la anota."),
            ex("¿Qué papel guarda las notas de una pieza?", "La partitura", "Es el papel donde se escribe la música."),
            ex("La tradición escrita, ¿se guarda en la memoria de las personas o en partituras?", "En partituras", "Es lo que la distingue de la oral."),
        ],
        "understand": [
            ex("¿Para qué sirve una partitura?", "Para que otras personas puedan tocar la pieza igual", "Guarda las notas y su duración."),
            ex("¿Quién toca la música que está en una partitura?", "El intérprete", "El intérprete lee y toca o canta."),
            ex("¿La música escrita siempre es muy antigua?", "No", "También se compone hoy."),
        ],
        "apply": [
            ex("Un piano toca suave y lento, luego rápido y fuerte, luego suave y lento otra vez. Escribe la forma con letras.", "A – B – A", "La primera parte regresa."),
            ex("Una pieza para violín y piano tiene dos instrumentos. ¿Cuántos instrumentos suenan?", "2", "Son violín y piano."),
            ex("Un coro canta una pieza breve de ocho pulsos y la repite una vez. ¿Cuántos pulsos canta en total?", "16", "8 pulsos × 2 veces = 16."),
        ],
        "reason": [
            ex("Un niño dice «la música docta es aburrida porque es antigua». ¿Qué dos errores tiene?", "Juzga sin escuchar y cree que toda la música docta es antigua", "Escribir música también se hace hoy y todos los estilos se pueden escuchar con atención."),
            ex("¿Por qué dos intérpretes distintos pueden tocar la misma pieza?", "Porque ambos leen la misma partitura", "La partitura conserva la pieza."),
        ],
        "challenge": [
            ex("Una pieza para piano de ocho pulsos tiene las partes: suave–suave–fuerte–suave. Escribe cuál es la parte que contrasta.", "La tercera, que es fuerte", "Las otras tres son suaves."),
            ex("Escribe una frase corta que describa una pieza de piano que oyes: lenta, suave y grave.", "Un piano toca notas lentas, suaves y graves", "Describe instrumento y cualidades."),
        ],
    },
    context=[ex("Un grupo de niños va a un concierto escolar. Un violín y un piano tocan una pieza breve de un compositor. ¿Qué observarías? Nombra dos cosas que se pueden oír.", "Cualquier dos: instrumentos, rapidez, fuerza, partes que regresan", "Son pistas audibles de una pieza escrita.")],
    selfcheck=[ex("¿Quién escribe una pieza en una partitura?", "El compositor", "Crea y anota la música."), ex("¿Cómo se llama el papel con las notas?", "Partitura", "Guarda la música escrita."), ex("Nombra un instrumento de una pieza docta.", "Piano, violín o flauta", "Son instrumentos comunes.")],
    open_task=task(
        "Lee esta pieza inventada para piano: «Primero, ocho notas lentas y suaves. Después, cuatro notas rápidas y fuertes. Al final, otra vez las ocho notas lentas y suaves». Dibuja la forma con letras, anota qué instrumento suena y escribe qué parte contrasta.",
        "La forma es A – B – A. Suena el piano. Contrasta la parte B, que es rápida y fuerte.",
        ["identifica la forma A – B – A", "nombra el instrumento", "señala la parte que contrasta"],
        ["forma escrita", "frase", "explicación oral"],
        ["decir que la tercera parte es nueva", "no nombrar el instrumento"],
        "Reconoce la forma correcta y pide la pista que muestra el contraste; si cree que todas las partes son iguales, vuelve a leer en voz alta.",
    ),
    reinforce="Cuenta dos instrumentos que conoces y di si podrían tocar una pieza escrita.",
    extend="Compara en una frase una canción de tradición oral y una pieza escrita para piano.",
)

register(
    OA3, 4,
    materials=f"Lápiz y tus palmas. Patrón de pulso para esta clase: {P(TA, TA, TT, SIL)} ({LEY}). Los ejemplos de música popular están descritos por escrito.",
    use="Aprenderé a escuchar música popular e identificar su pulso, timbres y función. Sirve para entender por qué la música suena en fiestas, juegos y programas.",
    prior=["Sé qué es el pulso.", "Sé nombrar instrumentos como guitarra, batería y piano."],
    explain=[
        "La música popular es la que muchas personas escuchan y disfrutan en la vida diaria: en la radio, en fiestas, en conciertos y en canciones para niños. Incluye estilos como el jazz, el rock y la fusión, que mezcla estilos. También hay música infantil popular, hecha para que niños canten y bailen.",
        "Casi siempre se oye un pulso claro. Una batería o un bombo marca el latido y una guitarra eléctrica o un bajo suena encima. Algunos estilos usan instrumentos como el saxofón, el piano o la voz. En el jazz, a veces los músicos inventan melodías en el momento: eso se llama improvisar.",
        "Para escuchar música popular, pregúntate qué instrumentos suenan, si el pulso es claro y para qué sirve. Una canción para bailar tiene un pulso muy marcado. Una canción para escuchar tranquilo puede ser lenta y suave. Describe lo que oyes sin decir que un estilo es mejor que otro.",
    ],
    vocab=[("música popular", "música que muchas personas oyen en la vida diaria"), ("jazz", "estilo que a veces improvisa"), ("rock", "estilo con batería, bajo y guitarra eléctrica"), ("fusión", "mezcla de estilos"), ("función", "para qué sirve una música")],
    worked=[
        {"title": "Identificar pulso y función", "problem": "Una banda toca con una batería muy marcada, un bajo y una guitarra eléctrica. La gente salta en una fiesta. ¿Cuál es la función?", "steps": ["El pulso es muy claro.", "La gente salta y baila.", "Sirve para bailar y celebrar."], "answer": "Bailar y celebrar"},
        {"title": "Reconocer improvisación", "problem": "En un jazz un saxofonista toca una melodía que inventa en el momento. ¿Cómo se llama eso?", "steps": ["Los músicos inventan al tocar.", "No leen una melodía escrita.", "Se llama improvisar."], "answer": "Improvisar"},
    ],
    mistakes=[
        {"wrong": "Pensar que la música popular no tiene valor.", "why": "Se juzga un estilo como inferior.", "fix": "Cada estilo tiene su función y su cuidado; descríbelo antes de opinar."},
        {"wrong": "Creer que todo lo popular es rock.", "why": "Se reduce un conjunto de estilos a uno solo.", "fix": "La música popular incluye jazz, rock, fusión y muchos estilos más."},
    ],
    tiers={
        "recovery": [
            ex("Una banda con batería, bajo y guitarra eléctrica, ¿toca música popular o música docta?", "Música popular", "Son instrumentos típicos de estilos populares como el rock."),
            ex("¿Qué instrumento suele marcar el pulso en una banda?", "La batería", "Marca el latido con golpes parejos."),
            ex("Un saxofonista inventa una melodía en el momento. ¿Qué hace?", "Improvisa", "Inventar al tocar es improvisar."),
        ],
        "understand": [
            ex("¿Cuál es la función de una música con pulso muy marcado en una fiesta?", "Bailar", "El pulso claro invita a moverse."),
            ex("¿Qué es la fusión?", "Mezcla de estilos", "Une dos o más estilos en una música."),
            ex("¿La música popular incluye solo rock?", "No", "También incluye jazz, fusión y más."),
        ],
        "apply": [
            ex(f"Toca con las palmas el patrón {P(TA, TA, TT, SIL)}. ¿Cuántos sonidos tiene?", str(sounds(TA, TA, TT, SIL)), "1 + 1 + 2 + 0 = 4."),
            ex("Una canción para niños es lenta, suave y se canta antes de dormir. ¿Cuál es su función?", "Hacer dormir o tranquilizar", "Lento y suave calma."),
            ex("Una banda tiene batería, bajo, guitarra y voz. ¿Cuántos instrumentos y voces tiene?", "4", "Batería, bajo, guitarra y voz suman cuatro."),
        ],
        "reason": [
            ex("Paz dice: «el jazz es mejor que el rock». ¿Qué falta para decirlo con respeto?", "Describir lo que se oye en cada uno y no juzgar", "Cada estilo tiene sus características y su función."),
            ex("Si una música tiene pulso muy claro y fuerte, ¿es más fácil bailarla o dormirse con ella?", "Bailarla", "Un pulso marcado invita a moverse."),
        ],
        "challenge": [
            ex("Escribe una frase que describa una música popular con tres datos: instrumentos, pulso y función.", "Por ejemplo: batería, bajo y guitarra marcan un pulso claro para bailar", "La frase debe incluir los tres datos."),
            ex("Una música mezcla un ritmo tradicional con una guitarra eléctrica. ¿Cómo se llama esta mezcla?", "Fusión", "Mezclar estilos es fusión."),
        ],
    },
    context=[ex("En el recreo, un grupo de niños baila una canción infantil con un pulso muy marcado y palmas. ¿Qué observan sobre el pulso y la función?", "El pulso es claro y la función es bailar", "Lo marcado invita al baile.")],
    selfcheck=[ex("Nombra dos estilos de música popular.", "Jazz y rock (u otros como fusión)", "Son estilos nombrados en la clase."), ex("¿Qué instrumento marca el pulso en una banda?", "La batería", "Marca el latido."), ex("¿Qué significa improvisar?", "Inventar música en el momento", "No se lee una melodía escrita.")],
    open_task=task(
        f"Escucha o pide que un adulto cante una canción infantil que conozcan. Marca el pulso con los pies mientras suena la canción. Después toca con las palmas el patrón {P(TA, TA, TT, SIL)} varias veces. Anota: qué instrumento o voz hay, si el pulso es claro y para qué sirve la canción (bailar, dormir, jugar).",
        "Escuché una canción infantil con voz y palmas. El pulso era claro. Servía para jugar.",
        ["marca el pulso con los pies", "toca el patrón sin perderse", "anota instrumento, pulso y función"],
        ["interpretación", "tres datos escritos", "explicación"],
        ["perder el pulso al tocar el patrón", "juzgar la música sin describirla"],
        "Reconoce el pulso estable y pregunta cómo supo la función; si dice «me gusta», pide una pista audible.",
    ),
    reinforce="Escucha una canción que te guste y marca el pulso con los pies durante 8 pulsos.",
    extend="Compara en dos frases la función de una canción de cuna y una canción para bailar.",
)

register(
    OA3, 5,
    materials="Lápiz y una hoja. Las seis músicas de la bitácora están descritas por escrito. Se necesitan colores si quieres decorar tu bitácora.",
    use="Aprenderé a llevar una bitácora de las músicas que escucho y a comparar. Sirve para recordar lo escuchado y reconocer qué no sé todavía.",
    prior=["Sé escribir algunas palabras.", "Sé describir un sonido con sus cualidades."],
    explain=[
        "Una bitácora es un cuaderno donde anotamos lo que escuchamos. Para cada música escribimos tres cosas: de qué tipo es (tradición oral, tradición escrita o popular), qué se oye (instrumentos, voz, rapidez, fuerza) y para qué sirve. También podemos dibujar o pintar.",
        "Durante el año conviene escuchar muchas músicas distintas. La meta del año es escuchar al menos 20 músicas variadas y breves. Si comparas dos, puedes decir en qué se parecen y en qué se diferencian. Por ejemplo, las dos pueden ser lentas, pero una tiene voces y la otra, un piano.",
        "En la bitácora también anotamos lo que no sabemos. Puedes escribir «no sé de dónde viene» o «no sé cómo se llama el instrumento». Eso es honesto y ayuda a aprender más. Nunca escribas datos privados, como nombres de personas o direcciones.",
    ],
    vocab=[("bitácora", "cuaderno donde se anota lo que se escucha"), ("comparar", "decir en qué se parecen y se diferencian dos cosas"), ("repertorio", "conjunto de músicas que conozco"), ("tipo de música", "oral, escrita o popular"), ("no sé todavía", "frase honesta cuando falta información")],
    worked=[
        {"title": "Anotar una entrada", "problem": "Escuchas una ronda en la que todos cantan y aplauden. ¿Cómo la anotas en tu bitácora?", "steps": ["Tipo: tradición oral.", "Qué se oye: voces y palmas, pulso claro.", "Para qué sirve: jugar en ronda."], "answer": "Tradición oral; voces y palmas; sirve para jugar"},
        {"title": "Comparar dos músicas", "problem": "La música 1 es una pieza de piano lenta y suave. La música 2 es una canción de banda rápida y fuerte. ¿En qué se diferencian?", "steps": ["La 1 tiene piano; la 2 tiene banda.", "La 1 es lenta y suave; la 2, rápida y fuerte.", "Ambas se pueden escuchar con atención."], "answer": "Se diferencian en instrumentos, rapidez y fuerza"},
    ],
    mistakes=[
        {"wrong": "Escribir solo «me gustó» en la bitácora.", "why": "Una opinión no cuenta lo que se oyó.", "fix": "Anota tipo, qué se oyó y para qué sirve."},
        {"wrong": "Inventar el nombre de una música que no se conoce.", "why": "Se quiere tener todas las respuestas.", "fix": "Escribe «no lo sé todavía» y pregunta a alguien."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué es una bitácora?", "Un cuaderno donde se anota lo que se escucha", "Guarda las experiencias de escucha."),
            ex("¿Cuántas músicas conviene escuchar al menos durante el año?", "20", "Es la meta del año."),
            ex("Una ronda en que todos cantan, ¿es de tradición oral o escrita?", "Oral", "Se aprende de persona a persona."),
        ],
        "understand": [
            ex("Nombra las tres cosas que se anotan de cada música.", "Tipo, qué se oye y para qué sirve", "Son las partes de la entrada."),
            ex("¿Por qué anotamos lo que no sabemos?", "Porque es honesto y ayuda a aprender", "Se puede preguntar después."),
            ex("¿Por qué no se escriben datos privados en la bitácora?", "Porque deben protegerse las personas", "Nombres y direcciones son privados."),
        ],
        "apply": [
            ex("Completa la entrada: un pianista lee una partitura y toca música lenta y suave. ¿De qué tipo es?", "Tradición escrita", "El piano lee la partitura."),
            ex("Música A: voz y palmas, ronda. Música B: banda con batería y guitarra. ¿Cuál es popular?", "La B", "La batería y la guitarra son típicas de música popular."),
            ex("Dos músicas son lentas. Una tiene piano y la otra tiene tambor. Escribe una semejanza y una diferencia.", "Semejanza: las dos son lentas; diferencia: una tiene piano y la otra tambor", "Se compara lo que se parece y lo que no."),
        ],
        "reason": [
            ex("Si escribes «no sé cómo se llama el instrumento», ¿estás haciendo algo mal?", "No", "Decir lo que no se sabe es honesto."),
            ex("Un compañero anota solo «me gustó». ¿Qué le agregarías?", "Qué se oyó y para qué sirve", "Una opinión necesita datos."),
        ],
        "challenge": [
            ex("Compara en una frase una canción de cuna (lenta, suave, para dormir) con una canción de banda (rápida, fuerte, para bailar).", "La cuna es lenta, suave y calma; la banda es rápida, fuerte y hace bailar", "La comparación usa cualidades y función."),
            ex("Escribe una bitácora de 3 líneas para una música inventada de tu elección, con tipo, lo que se oye y su función.", "Cualquier entrada con las tres partes, por ejemplo: popular; batería y voz; para bailar", "Debe tener los tres datos."),
        ],
    },
    context=[ex("Tu bitácora tiene tres músicas: una ronda, una pieza de piano y una canción de banda. ¿Qué tipo escribes para cada una, en ese orden?", "Tradición oral, tradición escrita, popular", "Cada una corresponde a un tipo distinto.")],
    selfcheck=[ex("¿Qué se escribe cuando no se sabe una información?", "No lo sé todavía", "Es una respuesta honesta."), ex("¿Cuántas músicas, al menos, es la meta del año?", "20", "Es la meta del año."), ex("¿Qué es comparar?", "Decir en qué se parecen y se diferencian", "Se buscan semejanzas y diferencias.")],
    open_task=task(
        "Completa esta bitácora con tres músicas descritas. Música 1: un grupo de niños canta en círculo y aplaude. Música 2: una pianista lee una partitura y toca notas suaves y lentas. Música 3: una banda con batería, bajo y guitarra eléctrica toca para bailar. Para cada una escribe el tipo, lo que se oye y su función. Al final escribe una cosa que no sabes todavía.",
        "1: Tradición oral; voces y palmas; jugar en ronda. 2: Tradición escrita; piano suave y lento, leído de partitura; escuchar con calma. 3: Popular; batería, bajo y guitarra; bailar. No sé cómo se llama el estilo de la tercera.",
        ["anota el tipo correcto de cada música", "describe lo que se oye con pistas", "dice una cosa que no sabe"],
        ["bitácora escrita", "conversación"],
        ["escribir solo me gustó", "inventar datos que no se conocen"],
        "Reconoce las entradas completas y valora la frase de lo que no sabe; si falta la función, pide que explique para qué serviría.",
    ),
    reinforce="Anota en una sola línea una música que escuchaste hoy con su tipo y su función.",
    extend="Compara dos entradas de tu bitácora usando la palabra «en cambio».",
)

# ---------------------------------------------------------------- OA 04
register(
    OA4, 1,
    materials="Lápiz, un vaso con agua y un espacio donde puedas sentarte o pararte derecho. El texto para cantar está en el cuaderno: «Canto bajito, canto parejo, mi voz es un hilo que sube y se va».",
    use="Aprenderé a cantar con una voz cuidada, por eco, sin forzar la garganta. Sirve para cantar con otros sin cansarme y sin gritar.",
    prior=["Sé repetir una frase que oigo.", "Sé respirar por la nariz y soltar el aire por la boca."],
    explain=[
        "Cantar bien es cantar con una voz cuidada. No se canta fuerte gritando. Se canta con el cuerpo derecho, los hombros sueltos y el aire que viene desde la panza. Si te duele la garganta, deja de cantar, descansa y toma agua.",
        "Cantar por eco significa repetir lo que escuchas. Una persona canta una frase corta y tú la repites igual: las mismas palabras, el mismo ritmo y el mismo tono. Si todos los niños cantan el mismo tono a la vez, se dice que cantan al unísono.",
        "Para afinar con otros, escucha más de lo que cantas. Si no oyes a las otras voces, estás cantando demasiado fuerte. Una buena voz de grupo suena junta, como una sola. Después de cantar, haz silencio un momento para escuchar cómo terminó.",
    ],
    vocab=[("unísono", "cantar o tocar el mismo sonido a la vez"), ("eco", "repetir lo que acabo de oír"), ("afinar", "cantar el mismo tono que los demás"), ("respirar", "tomar y soltar aire con calma"), ("voz cuidada", "voz que no grita ni se fuerza")],
    worked=[
        {"title": "Cantar por eco", "problem": "Un adulto canta «Canto bajito». ¿Cómo lo repites?", "steps": ["Escucho la frase completa.", "Repito las mismas palabras, el mismo ritmo y el mismo tono.", "Canto sin gritar."], "answer": "Repito «Canto bajito» igual, con voz suave"},
        {"title": "Saber si grito", "problem": "Cantas y no oyes a tus compañeros. ¿Qué te indica?", "steps": ["Si no oigo a los demás, mi voz tapa las otras.", "Eso significa que estoy cantando muy fuerte.", "Debo bajar mi voz hasta oír al grupo."], "answer": "Que estoy cantando muy fuerte y debo bajar la voz"},
    ],
    mistakes=[
        {"wrong": "Gritar para cantar fuerte.", "why": "Se cree que más fuerte es mejor.", "fix": "Canta con aire y voz cuidada; la fuerza viene del aire, no de la garganta."},
        {"wrong": "Cantar sin escuchar a los demás.", "why": "Se pone la atención solo en la propia voz.", "fix": "Escucha al grupo y trata de sonar igual que ellos."},
    ],
    tiers={
        "recovery": [
            ex("Si cantas por eco, ¿repites lo que oyes o inventas otra frase?", "Repito lo que oigo", "El eco es una repetición."),
            ex("Antes de cantar, ¿cómo pones tu cuerpo: encorvado o derecho?", "Derecho", "Una postura recta ayuda al aire."),
            ex("Si te duele la garganta, ¿sigues cantando fuerte o descansas?", "Descanso", "Se debe cuidar la voz."),
        ],
        "understand": [
            ex("¿Qué significa cantar al unísono?", "Cantar el mismo sonido a la vez", "Todos suenan igual."),
            ex("¿Por qué no se debe gritar al cantar?", "Porque se daña la garganta", "La voz se cuida."),
            ex("¿Qué haces con el aire para cantar con fuerza sin gritar?", "Respiro profundo desde la panza", "El aire sostiene la voz."),
        ],
        "apply": [
            ex("Un adulto canta «mi voz es un hilo». Escribe lo que repites si cantas por eco.", "Mi voz es un hilo", "El eco repite las mismas palabras."),
            ex("La frase «canto bajito, canto parejo» tiene 10 sílabas (can-to ba-ji-to, can-to pa-re-jo). Si la cantas dos veces seguidas, ¿cuántas sílabas cantas?", "20", "10 sílabas × 2 veces = 20."),
            ex("Cantas con 3 compañeros. ¿Cuántas voces cantan al unísono, contándote a ti?", "4", "Tres compañeros más tú suman cuatro."),
        ],
        "reason": [
            ex("Ana dice: «Si canto más fuerte me oyen mejor». ¿Qué problema tiene?", "Puede gritar y no escuchar a los demás", "Cantar al unísono necesita que todos se oigan."),
            ex("Si todos cantan en tonos distintos, ¿están al unísono?", "No", "Al unísono es el mismo tono."),
        ],
        "challenge": [
            ex("Una profesora canta una frase de cuatro palabras y tú la repites. Luego ella canta otra de cinco. ¿Cuántas palabras cantaste en total, en el eco?", "9", "4 + 5 = 9 palabras."),
            ex("Explica con tus palabras por qué escuchar a los demás ayuda a afinar.", "Porque puedo copiar su tono y cantar igual que ellos", "Escuchar permite igualar el sonido."),
        ],
    },
    context=[ex("En el acto de la escuela quieres cantar fuerte, pero tu voz se siente rasposa. ¿Qué haces?", "Tomo agua, descanso y después canto bajito", "Se cuida la voz para no dañarla.")],
    selfcheck=[ex("¿Qué es cantar por eco?", "Repetir lo que oigo", "Escucho y repito igual."), ex("¿Se grita para cantar fuerte?", "No", "Se canta con aire, no con grito."), ex("¿Qué significa unísono?", "El mismo sonido a la vez", "Todos suenan igual.")],
    open_task=task(
        "Canta por eco con alguien de tu casa la frase «Canto bajito, canto parejo, mi voz es un hilo que sube y se va». Que esa persona cante una parte y tú la repites con voz cuidada. Después cantan juntos al mismo tiempo. Anota si lograron sonar como una sola voz y cómo cuidaste tu garganta.",
        "Mi mamá cantó «Canto bajito» y yo la repetí. Después cantamos juntas y sonamos parejas. Tomé agua y no grité.",
        ["repite la frase por eco", "canta sin gritar", "canta junto a otra persona y comenta cómo sonaron"],
        ["interpretación", "frase escrita", "explicación"],
        ["cantar gritando", "no escuchar a la otra voz"],
        "Reconoce el cuidado de la voz y pregunta cómo supo que sonaban juntos; si grita, que repita más bajito.",
    ),
    reinforce="Respira tres veces profundo y canta una frase corta con voz suave.",
    extend="Canta una frase una vez fuerte pero cuidada y otra suave, y cuenta qué cambió.",
)

register(
    OA4, 2,
    materials=f"Lápiz, tus palmas y una persona que haga de director. Señales: mano arriba = prepararse; mano baja = empezar; puño cerrado = terminar. Patrón: {P(TA, TT, TA, SIL)} ({LEY}).",
    use="Aprenderé a entrar y terminar juntos con una señal y a mantener un pulso común. Sirve para tocar y cantar en grupo sin perderme.",
    prior=["Sé qué es el pulso.", "Sé mirar a una persona que da una señal."],
    explain=[
        "Para tocar o cantar juntos, el grupo necesita un pulso común. Es como si todos camináramos al mismo paso. Para empezar juntos, una persona hace de director y da una señal: la mano arriba significa «prepárense», la mano baja significa «empiecen». Para terminar, el director cierra el puño.",
        "Antes de empezar se cuentan algunos pulsos en voz baja: «uno, dos, tres, cuatro». Así todos saben la rapidez. Durante la música, mira al director y escucha a los demás. Si alguien se adelanta o se atrasa, no hay que parar: baja un poco tu volumen y vuelve al pulso.",
        "Al final, espera la señal y detente todos a la vez. Quédate quieto un instante en silencio para que el final se note. Si cada uno termina en un momento distinto, el grupo no suena junto.",
    ],
    vocab=[("pulso común", "el mismo latido para todo el grupo"), ("director", "persona que da las señales"), ("señal", "gesto que dice cuándo empezar o terminar"), ("entrar", "empezar a tocar o cantar"), ("detenerse", "dejar de sonar juntos")],
    worked=[
        {"title": "Empezar con la señal", "problem": "El director levanta la mano, cuenta 1, 2, 3, 4 y baja la mano. ¿Cuándo empiezas?", "steps": ["La mano arriba significa prepararme.", "Escucho los cuatro pulsos de preparación.", "Empiezo cuando baja la mano."], "answer": "Cuando baja la mano"},
        {"title": "Volver al pulso", "problem": "Te das cuenta de que vas más rápido que el grupo. ¿Qué haces?", "steps": ["Dejo de acelerar.", "Escucho el pulso de los demás.", "Vuelvo al pulso sin parar."], "answer": "Me bajo el volumen y vuelvo al pulso del grupo"},
    ],
    mistakes=[
        {"wrong": "Empezar cuando el director todavía tiene la mano arriba.", "why": "Se confunde prepararse con empezar.", "fix": "Espera la mano que baja."},
        {"wrong": "Terminar más tarde que los demás.", "why": "No se mira la señal de final.", "fix": "Mira el puño cerrado y detente a la vez."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué significa la mano arriba?", "Prepararse", "Es la señal acordada."),
            ex("¿Qué significa la mano baja?", "Empezar", "Es la señal acordada."),
            ex("¿Qué significa el puño cerrado?", "Terminar", "Es la señal acordada."),
        ],
        "understand": [
            ex("¿Para qué se cuentan pulsos en voz baja antes de empezar?", "Para que todos sepan la rapidez", "Así el grupo comparte el pulso."),
            ex("¿Qué es el pulso común?", "El mismo latido para todo el grupo", "Todos marcan igual."),
            ex("¿Por qué hay que terminar juntos?", "Para que el final suene claro", "Si terminan distinto, no suenan juntos."),
        ],
        "apply": [
            ex("El director cuenta 1, 2, 3, 4 antes de empezar. ¿Cuántos pulsos de preparación hay?", "4", "Son los cuatro números."),
            ex(f"Toca el patrón {P(TA, TT, TA, SIL)} tres veces seguidas. ¿Cuántos pulsos tocas en total?", "12", "4 pulsos × 3 repeticiones = 12."),
            ex("Estás en un grupo de 5 niños y todos entran a la vez con una señal. ¿Cuántos niños entran?", "5", "Todos entran en la misma señal."),
        ],
        "reason": [
            ex("Un niño empieza cuando el director solo levantó la mano. ¿Qué error cometió?", "Empezó antes de la señal de empezar", "La mano arriba solo prepara."),
            ex("Si el grupo acelera sin querer, ¿qué haces?", "Escucho y vuelvo al pulso sin gritar", "Escuchar ayuda a corregir juntos."),
        ],
        "challenge": [
            ex("Inventa una señal nueva para pedir «más suave». Descríbela en una frase.", "Por ejemplo: bajar la mano con la palma hacia abajo", "Una señal clara ayuda al grupo."),
            ex("En el grupo todos empiezan con la señal, pero uno termina tarde. ¿Qué habría que mirar?", "El puño cerrado del director", "La señal de final dice cuándo parar."),
        ],
    },
    context=[ex("En un acto, tu grupo debe cantar tres veces el estribillo y terminar a la vez. ¿Qué señal usan y qué hacen?", "Una señal clara de empezar y de terminar, y escuchan el pulso", "Con señales y escucha el grupo suena junto.")],
    selfcheck=[ex("¿Qué se hace antes de empezar?", "Contar pulsos en voz baja", "Así todos sienten el pulso."), ex("¿Quién da las señales?", "El director", "Dirige al grupo."), ex("¿Se termina cuando uno quiere?", "No, con la señal", "Se termina todos a la vez.")],
    open_task=task(
        f"Con dos personas de tu casa o tres peluches como grupo, hagan de director e intérpretes. Usen las señales de la clase para tocar el patrón {P(TA, TT, TA, SIL)} cuatro veces con palmas. Anota si empezaron juntos, si mantuvieron el pulso y si terminaron a la vez.",
        "El director levantó la mano y contó 1, 2, 3, 4. Tocamos el patrón cuatro veces. Empezamos juntos, nos adelantamos un poco en la tercera vuelta y terminamos a la vez.",
        ["usa las señales de empezar y terminar", "toca el patrón cuatro veces", "anota lo observado sobre pulso y final"],
        ["interpretación", "registro escrito"],
        ["empezar antes de la señal", "no registrar lo observado"],
        "Reconoce la coordinación y pregunta qué hicieron cuando se adelantaron; si no pararon juntos, repite el final con la señal más clara.",
    ),
    reinforce="Marca 16 pulsos con palmas contando en voz baja de 1 a 4 cuatro veces.",
    extend="Cambia la rapidez del pulso con una señal nueva y cuenta qué pasó con el grupo.",
)

register(
    OA4, 3,
    materials=f"Un tarro o caja de cartón, una cuchara de madera, una botella plástica con arroz tapada y tus palmas. Patrón para mantener: {P(TA, TT, TA, SIL)} ({LEY}).",
    use="Aprenderé a acompañar una canción con un patrón de percusión sin acelerar. Sirve para dar un latido firme a quien canta.",
    prior=["Sé tocar un golpe suave y uno fuerte.", "Sé mantener un pulso con los pies."],
    explain=[
        "Los instrumentos de percusión suenan al golpearlos, sacudirlos o rasparlos. Hay convencionales, como el pandero, las claves, el triángulo y el tambor. Y hay no convencionales, que son objetos cotidianos: un tarro, una caja de cartón, una cuchara de madera o una botella con arroz.",
        f"Acompañar es tocar un patrón que se repite mientras alguien canta. El patrón {P(TA, TT, TA, SIL)} se toca una y otra vez sobre el pulso. Lo difícil es no acelerar. Cuando nos emocionamos, tocamos más rápido. Para evitarlo, marca el pulso con el pie y compara tu patrón con él.",
        "Cuida los objetos y tus oídos. Golpea con suavidad, usa una cuchara de madera y no objetos duros o pesados. No toques tan fuerte que tapes la voz que canta. Un buen acompañante es el que se oye, pero deja oír a quien canta.",
    ],
    vocab=[("percusión", "instrumentos que suenan al golpear, sacudir o raspar"), ("convencional", "hecho para hacer música, como el pandero"), ("no convencional", "objeto cotidiano que uso para sonar"), ("acompañar", "tocar mientras otro canta"), ("acelerar", "ir cada vez más rápido sin querer")],
    worked=[
        {"title": "Elegir un instrumento", "problem": "No tienes pandero en casa. ¿Qué puedes usar para tocar el patrón?", "steps": ["Busco un objeto seguro que suene.", "Un tarro con una cuchara de madera sirve.", "Pruebo que suene claro y no muy fuerte."], "answer": "Un tarro con una cuchara de madera"},
        {"title": "No acelerar", "problem": "Tu patrón se va haciendo cada vez más rápido. ¿Qué haces?", "steps": ["Marco el pulso con el pie.", "Hago que cada TA coincida con un paso.", "Si me adelanto, bajo la velocidad."], "answer": "Marco el pulso con el pie y toco sobre él"},
    ],
    mistakes=[
        {"wrong": "Tocar tan fuerte que no se oye la voz.", "why": "Se piensa que acompañar es sonar más.", "fix": "Toca más suave que la voz."},
        {"wrong": "Acelerar al emocionarse.", "why": "No se compara con el pulso.", "fix": "Marca el pulso con el pie y mantén tu patrón sobre él."},
    ],
    tiers={
        "recovery": [
            ex("Un pandero, ¿es un instrumento convencional o no convencional?", "Convencional", "Se hizo para hacer música."),
            ex("Un tarro con una cuchara, ¿es convencional o no convencional?", "No convencional", "Es un objeto cotidiano."),
            ex("Acompañar, ¿es tocar mientras otro canta o dejar de tocar?", "Tocar mientras otro canta", "Es dar apoyo al canto."),
        ],
        "understand": [
            ex("¿Por qué conviene marcar el pulso con el pie?", "Para no acelerar", "Sirve de guía constante."),
            ex("¿Por qué no se debe tocar más fuerte que la voz?", "Porque taparía a quien canta", "El acompañamiento apoya la voz."),
            ex("¿Cómo se toca un objeto para cuidarlo?", "Con suavidad", "Así no se rompe."),
        ],
        "apply": [
            ex(f"Cuenta los sonidos del patrón {P(TA, TT, TA, SIL)}.", str(sounds(TA, TT, TA, SIL)), "1 + 2 + 1 + 0 = 4 sonidos."),
            ex("Una botella con arroz suena cuando la sacudes. ¿La tocas golpeando o sacudiendo?", "Sacudiendo", "Así produce el sonido."),
            ex("Tocas el patrón de 4 pulsos 5 veces. ¿Cuántos pulsos tocas?", "20", "4 pulsos × 5 = 20."),
        ],
        "reason": [
            ex("Ema tocó el patrón y se fue acelerando. ¿Qué pudo hacer?", "Marcar el pulso con el pie", "Eso la ayuda a mantener la rapidez."),
            ex("¿Por qué un objeto cotidiano puede ser un instrumento?", "Porque suena y se puede tocar con un patrón", "Lo importante es el sonido que produce."),
        ],
        "challenge": [
            ex("Quieres dos sonidos distintos en tu patrón: uno agudo y uno grave. Nombra dos objetos que puedan lograrlo.", "Por ejemplo: una cuchara que golpea la tapa de una olla (agudo) y una caja de cartón (grave)", "Cada objeto tiene su altura."),
            ex("Explica con tus palabras cómo comprobarías que no aceleraste.", "Comparándolo con el pulso del pie", "El pulso del pie es una referencia constante."),
        ],
    },
    context=[ex("Tu papá canta y tú lo acompañas con una cuchara y un tarro. Él dice que no lo oye. ¿Qué haces?", "Toco más suave", "El acompañamiento no debe tapar la voz.")],
    selfcheck=[ex("Nombra un instrumento de percusión convencional.", "Pandero, claves, triángulo o tambor", "Son instrumentos hechos para hacer música."), ex("¿Qué es acelerar sin querer?", "Ir cada vez más rápido", "Cambia el pulso del grupo."), ex("¿Cómo evitas acelerar?", "Marcando el pulso con el pie", "Es una referencia.")],
    open_task=task(
        f"Elige un tarro, una caja o una botella con arroz. Toca el patrón {P(TA, TT, TA, SIL)} ocho veces seguidas mientras alguien canta «Canto bajito, canto parejo». Marca el pulso con el pie. Anota si aceleraste y qué hiciste para evitarlo.",
        "Usé un tarro y una cuchara. Toqué ocho veces el patrón. Al principio me adelanté, pero marqué el pulso con el pie y volví al ritmo.",
        ["mantiene el patrón completo con el silencio", "no acelera o corrige", "anota qué hizo para evitar acelerar"],
        ["interpretación", "registro escrito"],
        ["acelerar", "tapar la voz"],
        "Reconoce el pulso estable y pregunta cómo lo comprobó; si aceleró, que repita con el pie marcando.",
    ),
    reinforce="Toca el patrón cuatro veces con las palmas y luego con una cuchara en una caja.",
    extend="Cambia el patrón a TA – TA – ti-ti – SIL y compara con el original.",
)

register(
    OA4, 4,
    materials=f"Un tarro o caja, una cuchara, tu voz y una persona que dirija. Patrón: {P(TA, TA, TT, SIL)} ({LEY}). Texto para cantar: «Canto bajito, canto parejo, mi voz es un hilo que sube y se va».",
    use="Aprenderé a cantar y tocar a la vez equilibrando voz, instrumento y escucha. Sirve para tocar en grupo sin que una parte tape a las otras.",
    prior=["Sé cantar por eco.", "Sé mantener un patrón sin acelerar."],
    explain=[
        "En una interpretación conjunta unos cantan y otros tocan. Cada parte tiene su papel. La voz lleva el texto y la melodía. La percusión da el latido y el patrón. Todos escuchan a todos para sonar bien juntos.",
        "El equilibrio es que ninguna parte tape a las demás. Si el instrumento suena muy fuerte, la voz no se oye. Si la voz grita, el instrumento se pierde. Por eso se prueba el volumen de cada parte hasta que se pueda oír todo.",
        "Antes de empezar, el grupo se pone de acuerdo: quién canta, quién toca, quién da la señal y cuántas veces se repite. Después ensayan y comentan qué se oyó bien y qué mejorar. Terminar juntos con la señal es parte del trabajo.",
    ],
    vocab=[("interpretación conjunta", "cantar y tocar juntos"), ("equilibrio", "que ninguna parte tape a otra"), ("papel", "lo que hace cada persona"), ("ensayar", "repetir para mejorar"), ("volumen", "qué tan fuerte suena algo")],
    worked=[
        {"title": "Repartir papeles", "problem": "Son cuatro niños. ¿Cómo repartes los papeles para cantar y tocar?", "steps": ["Dos cantan.", "Uno toca el patrón.", "Uno da las señales."], "answer": "2 voces, 1 percusión y 1 director"},
        {"title": "Equilibrar", "problem": "La percusión suena tan fuerte que no se oye la voz. ¿Qué cambias?", "steps": ["Bajo el volumen de la percusión.", "Pido que canten con voz cuidada.", "Pruebo otra vez hasta oír las dos."], "answer": "Toco más suave la percusión"},
    ],
    mistakes=[
        {"wrong": "Tocar sin escuchar a quien canta.", "why": "Se atiende solo al propio patrón.", "fix": "Escucha la voz mientras tocas."},
        {"wrong": "Cada uno termina cuando quiere.", "why": "No se pone atención en la señal.", "fix": "Mira al director y termina juntos."},
    ],
    tiers={
        "recovery": [
            ex("En una interpretación conjunta, ¿quién lleva el texto: la voz o la percusión?", "La voz", "Canta las palabras."),
            ex("¿Quién da el latido: la voz o la percusión?", "La percusión", "Marca el patrón."),
            ex("¿Qué significa equilibrio?", "Que ninguna parte tape a otra", "Se oyen todas."),
        ],
        "understand": [
            ex("¿Por qué se ensaya antes de presentar?", "Para mejorar", "Repetir ayuda a corregir."),
            ex("¿Por qué es importante escuchar a todos?", "Para sonar juntos", "Escuchar permite coordinarse."),
            ex("¿Quién da la señal de terminar?", "El director", "Dirige al grupo."),
        ],
        "apply": [
            ex(f"Cuenta los sonidos del patrón {P(TA, TA, TT, SIL)}.", str(sounds(TA, TA, TT, SIL)), "1 + 1 + 2 + 0 = 4."),
            ex("Cantan seis niños y dos tocan percusión. ¿Cuántos participan en total?", "8", "6 + 2 = 8."),
            ex("La frase cantada se repite 3 veces y la percusión toca 4 pulsos por cada repetición. ¿Cuántos pulsos toca?", "12", "4 pulsos × 3 repeticiones = 12."),
        ],
        "reason": [
            ex("La percusión suena muy fuerte y la voz no se oye. ¿Quién debe cambiar: la percusión o la voz?", "La percusión, tocando más suave", "El acompañamiento debe apoyar la voz."),
            ex("¿Es mejor que todos toquen lo más fuerte que puedan?", "No", "Se pierde el equilibrio."),
        ],
        "challenge": [
            ex("Diseña un plan de interpretación para tres niños con tres papeles. Escríbelo.", "Uno canta, uno toca percusión y uno da las señales", "Cada niño tiene un papel distinto."),
            ex("Después de ensayar, ¿qué dos cosas comentas con el grupo?", "Qué se oyó bien y qué se puede mejorar", "Ese es el objetivo del ensayo."),
        ],
    },
    context=[ex("En tu casa cantan «Canto bajito» en familia. Tu hermana toca el tarro y tu papá canta. ¿Qué hacen para que se oiga todo?", "Probar el volumen del tarro y de la voz", "Ajustar volumen logra el equilibrio.")],
    selfcheck=[ex("¿Qué es equilibrio?", "Que ninguna parte tape a otra", "Todos se oyen."), ex("¿Qué se hace en un ensayo?", "Repetir para mejorar", "Ensayar sirve para corregir."), ex("¿Quién da la señal de empezar?", "El director", "Él dirige al grupo.")],
    open_task=task(
        f"Con una o dos personas, canten «Canto bajito, canto parejo, mi voz es un hilo que sube y se va» mientras uno toca el patrón {P(TA, TA, TT, SIL)} con un tarro. Repártanse papeles: voz, percusión y director. Ensayen dos veces y escribe una cosa que se oyó bien y una que mejoraron.",
        "Mi hermano cantó, yo toqué el tarro y mi mamá dio la señal. Se oía bien la voz. La segunda vez toqué más suave y se oyó mejor.",
        ["reparte papeles y usa las señales", "mantiene voz y percusión a la vez", "anota una cosa buena y una mejora"],
        ["interpretación", "registro escrito"],
        ["tapar la voz", "no ensayar"],
        "Reconoce el equilibrio logrado y pregunta qué cambió entre ensayos; si no mejoró, que cambie el volumen de la percusión.",
    ),
    reinforce="Canta una frase y toca un patrón con palmas a la vez, despacio.",
    extend="Agrega un segundo patrón con una botella con arroz y comprueba si se mantiene el equilibrio.",
)
