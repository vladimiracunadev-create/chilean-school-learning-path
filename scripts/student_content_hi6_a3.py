"""Material del estudiante de 6.º básico, Historia, Geografía y Ciencias Sociales: OA 03 (organización de la república, siglo XIX)."""
from __future__ import annotations

from hi5_lib import build

OA3 = "HI06 OA 03"

# ---------------------------------------------------------------- clase 1
F = ("Ficha 10 (cronología de la organización de la república, hecha para este cuaderno). "
     "1818: Chile proclama su independencia y Bernardo O'Higgins gobierna como Director Supremo hasta 1823. "
     "1823 a 1830: varios ensayos de constituciones y cambios frecuentes de gobierno; es un período de desorden político. "
     "17 de abril de 1830: batalla de Lircay, que ganan las fuerzas conservadoras. "
     "1831-1841: presidente José Joaquín Prieto. 1833: se promulga la Constitución de 1833, que rige hasta 1925. "
     "1841-1851: presidente Manuel Bulnes. 1851-1861: presidente Manuel Montt. "
     "1871: reforma que impide la reelección inmediata del presidente. 1874: reforma electoral que amplía el voto a los hombres mayores de 21 años que sepan leer y escribir. "
     "1883-1884: leyes laicas (cementerios laicos, Registro Civil y matrimonio civil).")
build(
    OA3, 1, F,
    use="Aprenderé a ubicar en el tiempo los hitos de la organización de la república de Chile en el siglo XIX. Sirve para no confundir cuándo ocurrió cada uno.",
    prior=["Sé que Chile proclamó su independencia en 1818.", "Sé leer una línea de tiempo y restar años.", "Sé qué es una constitución: la ley principal de un país."],
    explain=[
        "Después de la independencia, Chile tuvo que organizarse como república: un país donde las autoridades son elegidas y gobiernan según leyes, no por herencia como un rey. Para eso había que acordar quién gobierna, cómo se hacen las leyes y qué derechos tiene cada persona. Todo eso se escribe en una constitución.",
        "La tarea no fue fácil. Entre 1823 y 1830 hubo varios ensayos de constituciones y cambios de gobierno. Los grupos políticos discrepaban sobre cuánto poder debía tener el presidente y qué papel tenía la Iglesia. El conflicto se resolvió por la fuerza en la batalla de Lircay, en 1830, que ganaron los conservadores.",
        "Después llegó un orden más estable. La Constitución de 1833 rigió casi un siglo, hasta 1925, y los presidentes Prieto, Bulnes y Montt gobernaron por diez años cada uno. En la segunda mitad del siglo XIX, los liberales hicieron reformas: limitaron la reelección del presidente, ampliaron el voto y separaron algunas funciones de la Iglesia y del Estado.",
    ],
    vocab=[("república", "forma de gobierno en que las autoridades son elegidas y gobiernan según leyes"), ("constitución", "ley principal de un país que organiza el gobierno y los derechos"), ("reelección", "volver a ser elegido para el mismo cargo"), ("reforma", "cambio que mejora o modifica una ley o una institución"), ("laico", "que no depende de ninguna religión")],
    worked=[
        ("Calcular una duración", "{F} ¿Cuántos años rigió la Constitución de 1833 según la ficha?", ["La ficha dice que se promulgó en 1833 y rigió hasta 1925.", "Resto: 1925 − 1833 = 92."], "92 años"),
        ("Ordenar hechos", "{F} ¿Qué ocurrió antes: la batalla de Lircay o la Constitución de 1833?", ["Lircay fue en 1830.", "La Constitución se promulgó en 1833."], "La batalla de Lircay"),
    ],
    mistakes=[("Creer que la república se organizó de inmediato después de 1818.", "Se mira solo la independencia y no el desorden posterior.", "Hubo varios ensayos constitucionales hasta la Constitución de 1833."),
              ("Mezclar la Constitución de 1833 con las reformas liberales.", "Se olvida el orden de los hechos.", "La Constitución es de 1833 y las reformas liberales son de 1871 a 1884.")],
    T=[
        ("{F} ¿En qué año se promulgó la Constitución que rigió hasta 1925?", "1833", "La ficha da ese año."),
        ("{F} ¿Qué presidente gobernó de 1841 a 1851?", "Manuel Bulnes", "La ficha lo indica."),
        ("{F} ¿Quién ganó la batalla de Lircay?", "las fuerzas conservadoras", "La ficha lo dice."),
        ("=", "{F} ¿Cuántos años pasaron entre la proclamación de la independencia y la batalla de Lircay?", "1830-1818", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué reforma de 1871 se refiere a la reelección del presidente?", "impide la reelección inmediata del presidente", "La ficha la describe así."),
        ("=", "{F} ¿Cuántos años gobernó Manuel Montt?", "1861-1851", "Se resta el año de inicio al año de término.", " años"),
        ("{F} Ordena de más antiguo a más reciente: leyes laicas, Constitución de 1833, batalla de Lircay, reforma electoral de 1874.", "batalla de Lircay, Constitución de 1833, reforma electoral de 1874, leyes laicas", "Los años son 1830, 1833, 1874 y 1883-1884."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1833 y la reforma electoral de 1874?", "1874-1833", "Se restan los años de ambas.", " años"),
        ("{F} Clasifica cada hecho como «de orden» (hasta 1833) o «de reforma liberal» (después de 1860): a) Lircay; b) matrimonio civil; c) reelección; d) Constitución de 1833.", "de orden: a y d; de reforma liberal: b y c", "Los hechos b y c son de 1871 a 1884."),
        ("{F} Un compañero dice: «En 1818 Chile ya tenía la Constitución de 1833». Corrígelo.", "No: la Constitución de 1833 se promulgó 15 años después de 1818, y hubo ensayos constitucionales antes", "Hay 15 años y varios intentos entre ambas fechas."),
        ("{F} Una alumna dice que los presidentes Prieto, Bulnes y Montt gobernaron cinco años cada uno. ¿Es correcto?", "No: la ficha indica que gobernaron diez años cada uno", "1831-1841, 1841-1851 y 1851-1861 son diez años."),
        ("{F} ¿Cuántos presidentes gobernaron entre 1831 y 1861 según la ficha?", "tres (Prieto, Bulnes y Montt)", "La ficha nombra tres presidentes en ese período."),
        ("=", "{F} ¿Cuántos años pasaron entre el inicio del gobierno de Prieto y el fin del gobierno de Montt?", "1861-1831", "Se resta el año de inicio al de término.", " años"),
    ],
    ctx=("En una plaza de tu ciudad hay una placa que dice «1833-1925». ¿Qué período representa esa placa en la historia de Chile?", "la vigencia de la Constitución de 1833", "La ficha dice que esa Constitución rigió hasta 1925."),
    sc=[("¿Qué es una república?", "una forma de gobierno donde las autoridades son elegidas y gobiernan según leyes", "La definición de la clase."),
        ("{F} ¿Qué reforma de la ficha tiene que ver con el voto?", "la reforma electoral de 1874", "Amplía el voto a hombres que sepan leer y escribir."),
        ("{F} ¿En qué años se publicaron las leyes laicas de la ficha?", "1883-1884", "La ficha indica ese período.")],
    op=("Dibuja una línea de tiempo desde 1818 hasta 1890. Marca al menos ocho hechos de la ficha con su año y escribe una frase corta. Usa un color para los hechos de orden político (1818-1861) y otro para las reformas liberales (1871-1884). {F}",
        "Puntos en 1818, 1830, 1833, 1841, 1851, 1871, 1874 y 1883-1884, con colores distintos para los dos períodos.",
        ["ocho hechos ordenados", "dos colores bien usados", "una frase por hecho"], ["línea de tiempo coloreada"], ["poner Lircay después de 1833", "pintar las leyes laicas como hecho de orden"],
        "Pide que explique en voz alta por qué decidió separar los hechos en dos colores."),
    reinforce="Di en voz alta la secuencia: 1818, 1830, 1833, 1871, 1874, 1883, y qué ocurrió en cada año.",
    extend="Escribe una pregunta que te gustaría responder sobre qué pasó en Chile entre 1823 y 1830.",
)

# ---------------------------------------------------------------- clase 2
F = ("Ficha 11 (fuentes inventadas para este cuaderno, basadas en contenidos conocidos). "
     "Fuente A, extracto adaptado de la Constitución de 1833: el presidente dura cinco años, puede ser reelegido una vez, y la religión del Estado es la católica. "
     "Fuente B, carta de un comerciante de Valparaíso, 1850 (texto inventado): «Después de tantos desórdenes, la autoridad firme de este gobierno ha permitido que el comercio funcione y que los caminos sean seguros». "
     "Fuente C, discurso de un diputado liberal, 1870 (texto inventado): «El presidente tiene demasiado poder; es necesario que no pueda ser reelegido de inmediato y que más ciudadanos puedan votar». "
     "Fuente D, libro de historia de 1980 sobre el siglo XIX: explica que el sistema de 1833 dio orden, pero limitó la participación política.")
build(
    OA3, 2, F,
    use="Aprenderé a leer fuentes sobre la organización de la república preguntando quién habla, cuándo y desde qué punto de vista. Sirve para evaluar la Constitución de 1833 con más de una opinión.",
    prior=["Sé la diferencia entre fuente primaria y secundaria.", "Sé qué es la Constitución de 1833.", "Sé que cada autor tiene un punto de vista."],
    explain=[
        "Las fuentes sobre la organización de la república incluyen leyes, cartas, discursos y libros de historia. La Constitución de 1833 es una fuente primaria importante porque muestra las reglas del gobierno. Pero una ley no cuenta cómo la vivieron las personas, para eso se necesitan otras fuentes.",
        "La carta del comerciante de 1850 muestra que para algunas personas el orden de este gobierno fue bueno, porque dio seguridad al comercio. El discurso del diputado liberal de 1870 muestra otra mirada: el poder del presidente era excesivo y el voto estaba limitado. Las dos son fuentes primarias, pero hablan desde lugares distintos.",
        "El libro de 1980 es una fuente secundaria. Resume ambas miradas y concluye que hubo orden, pero poca participación. Aun así, hay que preguntar qué fuentes usó y qué dejó fuera. Ninguna de estas fuentes cuenta lo que pensaban las mujeres, que no podían votar, ni los trabajadores sin propiedades.",
    ],
    vocab=[("fuente primaria", "documento creado en la época que se estudia"), ("fuente secundaria", "texto escrito después sobre hechos del pasado"), ("diputado", "persona elegida para representar a los ciudadanos en la Cámara de Diputados"), ("participación política", "posibilidad de elegir autoridades o decidir en asuntos públicos"), ("autoridad", "persona o institución con derecho a mandar")],
    worked=[
        ("Reconocer el punto de vista", "{F} ¿Qué opina sobre el poder del presidente el autor de la fuente C?", ["Es un diputado liberal.", "Dice que el presidente tiene demasiado poder."], "Que es excesivo y debe limitarse"),
        ("Clasificar una fuente", "{F} ¿La fuente D es primaria o secundaria?", ["Se escribió en 1980.", "Habla del siglo XIX, mucho tiempo antes."], "Secundaria"),
    ],
    mistakes=[("Creer que la opinión del comerciante representa a todos.", "Se generaliza desde una sola fuente.", "La carta muestra la opinión de una persona de Valparaíso."),
              ("Pensar que la Constitución cuenta la vida real de las personas.", "Se confunde la regla escrita con la experiencia.", "La ley dice cómo debe gobernarse; otras fuentes muestran cómo se vivió.")],
    T=[
        ("{F} ¿Cuántos años dura el presidente según la fuente A?", "cinco años", "La fuente A lo indica."),
        ("{F} ¿Cuál es la religión del Estado según la fuente A?", "la católica", "La fuente A lo dice."),
        ("{F} ¿Qué ciudad menciona la fuente B?", "Valparaíso", "El encabezado indica al comerciante de Valparaíso."),
        ("{F} ¿Qué dos cambios propone el diputado de la fuente C?", "que el presidente no sea reelegido de inmediato y que más ciudadanos puedan votar", "La fuente C los nombra."),
        ("=", "{F} ¿Cuántos años pasaron entre la fuente B y la fuente C?", "1870-1850", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Cuál de las cuatro fuentes es la única secundaria?", "la fuente D", "Se escribió en 1980."),
        ("{F} ¿Qué valora el comerciante de la fuente B del gobierno?", "la autoridad firme, que dio orden, comercio y caminos seguros", "Lo dice la carta."),
        ("{F} Compara B y C: ¿quién defiende el orden del sistema y quién pide más participación?", "B defiende el orden; C pide más participación", "Cada uno habla desde su situación."),
        ("{F} Una alumna dice: «La fuente B prueba que todos estaban contentos con el gobierno». ¿Qué error comete?", "generaliza: la carta es de un solo comerciante", "Una persona no representa a todos."),
        ("{F} Según la explicación de la clase, nombra un grupo que no podía votar y cuya opinión no aparece en ninguna de las cuatro fuentes.", "las mujeres (o los trabajadores sin propiedades)", "La explicación los nombra y las fuentes no los mencionan."),
        ("{F} Según la fuente D, ¿qué logró el sistema de 1833 y qué limitó?", "dio orden, pero limitó la participación política", "La fuente D lo resume."),
        ("{F} Para saber cómo se vivió el orden de 1850 en un puerto, ¿qué fuente es más útil: la A, la B o la D?", "la B", "Es testimonio directo de un comerciante de la época."),
        ("{F} Ordena de la más antigua a la más reciente las fuentes A, B, C y D, considerando que la A es de 1833.", "A, B, C, D", "Los años son 1833, 1850, 1870 y 1980."),
    ],
    ctx=("Un grupo quiere saber si en 1870 había personas que pedían ampliar el voto. ¿Qué fuente de la ficha les sirve y qué dato usarían?", "la fuente C, porque el diputado pide que más ciudadanos puedan votar", "C es de 1870 y contiene esa petición."),
    sc=[("¿Qué se pregunta primero a una fuente?", "quién la escribió y para qué", "El autor y el propósito ayudan a ver su punto de vista."),
        ("{F} ¿Qué punto de vista tiene la fuente C?", "el de un diputado liberal", "El encabezado lo dice."),
        ("¿Por qué conviene usar varias fuentes?", "porque cada una muestra una perspectiva distinta", "Una sola fuente es parcial.")],
    op=("Escribe una ficha de análisis para las fuentes B y C de la ficha. Para cada una anota: quién habla, año, qué defiende, qué no dice. Después escribe dos oraciones que expliquen por qué ambas fuentes son útiles aunque piensen distinto. {F}",
        "B: comerciante de Valparaíso, 1850, defiende el orden; no dice qué pensaban los trabajadores. C: diputado liberal, 1870, pide reformas; no dice qué pensaban las mujeres. Ambas muestran miradas distintas del mismo sistema.",
        ["dos fichas completas", "defensa de cada fuente correcta", "límite razonable en cada una", "dos oraciones finales"], ["fichas de B y C", "dos oraciones finales"], ["decir que B y C dicen lo mismo", "no anotar límites"],
        "Pide que explique por qué su límite para la fuente C es verdadero."),
    reinforce="Con tus palabras, resume en una oración lo que dice cada fuente de la ficha.",
    extend="Escribe qué fuente nueva buscarías para saber cómo vivía un trabajador del campo durante el gobierno de Montt.",
)

# ---------------------------------------------------------------- clase 3
F = ("Ficha 12 (actores, ideas y desafíos, hecha para este cuaderno). "
     "Desafíos de organizar la república: no había experiencia de gobierno propio, el Estado tenía pocos recursos y los grupos políticos discrepaban. "
     "Conservadores («pelucones»): querían un gobierno fuerte y ordenado, con presidente poderoso y la Iglesia católica con papel central. "
     "Liberales («pipiolos»): querían más libertades, un presidente con menos poder, más ciudadanos votando y, más adelante, separar funciones de la Iglesia y del Estado. "
     "Diego Portales fue un ministro conservador muy influyente en los primeros años de la Constitución de 1833. "
     "Entre los gobiernos liberales de la segunda mitad del siglo XIX estuvieron los de Federico Errázuriz Zañartu (1871-1876) y Domingo Santa María (1881-1886).")
build(
    OA3, 3, F,
    use="Aprenderé a explicar los desafíos de organizar la república y las ideas de conservadores y liberales. Sirve para entender por qué hubo conflictos y reformas.",
    prior=["Sé qué es una república y una constitución.", "Sé ubicar la Constitución de 1833 y las reformas en el tiempo.", "Sé distinguir causa y consecuencia."],
    explain=[
        "Organizar una república fue un desafío porque Chile no tenía experiencia de gobierno propio. El Estado tenía pocos recursos y los grupos políticos discrepaban en puntos importantes. Esos desacuerdos produjeron conflictos hasta que un grupo logró imponer un orden.",
        "Los conservadores, llamados pelucones, querían un gobierno fuerte y ordenado, con un presidente poderoso y la Iglesia católica con papel central. Los liberales, llamados pipiolos, querían más libertades, un presidente con menos poder y más ciudadanos votando. Estas diferencias son ideas políticas: modos de pensar cómo debe gobernarse un país.",
        "Con la Constitución de 1833 predominó la visión conservadora, con un presidente fuerte. En la segunda mitad del siglo XIX, los liberales ganaron influencia y lograron reformas durante los gobiernos de Errázuriz Zañartu y Santa María. Así, una causa del cambio fue el deseo de más libertades; una consecuencia fue que se limitó el poder presidencial y se separó a la Iglesia de ciertas funciones públicas.",
    ],
    vocab=[("conservador", "persona que defiende el orden, la autoridad fuerte y la tradición"), ("liberal", "persona que defiende más libertades y límites al poder"), ("idea política", "manera de pensar cómo debe gobernarse un país"), ("desafío", "dificultad que hay que resolver"), ("influyente", "que tiene mucha capacidad de afectar decisiones")],
    worked=[
        ("Clasificar una idea", "{F} ¿«Un presidente con menos poder» es idea conservadora o liberal?", ["Busco qué grupo defendía menos poder presidencial.", "La ficha lo asigna a los liberales."], "Liberal"),
        ("Explicar un cambio", "{F} ¿Qué consecuencia tuvo que los liberales ganaran influencia en la segunda mitad del siglo XIX?", ["Querían limitar el poder del presidente y ampliar el voto.", "Lograron reformas en gobiernos como el de Santa María."], "Lograron reformas durante gobiernos liberales"),
    ],
    mistakes=[("Pensar que conservadores y liberales eran partidos como los de hoy.", "Se compara sin considerar el contexto.", "Eran grupos con ideas políticas de su época, distintos de los partidos actuales."),
              ("Creer que los desafíos desaparecieron en 1833.", "Se piensa que una constitución resuelve todo.", "La Constitución dio orden, pero las diferencias continuaron.")],
    T=[
        ("{F} ¿Cómo se llamaba a los conservadores?", "pelucones", "La ficha lo indica."),
        ("{F} ¿Cómo se llamaba a los liberales?", "pipiolos", "La ficha lo indica."),
        ("{F} ¿Qué ministro conservador fue muy influyente en los primeros años de la Constitución de 1833?", "Diego Portales", "La ficha lo nombra."),
        ("{F} Clasifica como conservador (C) o liberal (L): a) presidente poderoso; b) más ciudadanos votando; c) Iglesia católica con papel central; d) más libertades.", "a: C; b: L; c: C; d: L", "La ficha asigna cada idea a un grupo."),
        ("{F} ¿Qué dos desafíos de organizar la república, además de los desacuerdos políticos, menciona la ficha?", "no había experiencia de gobierno propio y el Estado tenía pocos recursos", "Son los dos primeros desafíos."),
        ("=", "{F} ¿Cuántos años duró el gobierno de Santa María?", "1886-1881", "Se resta el año de inicio al año de término.", " años"),
        ("{F} ¿Qué idea defendían los liberales sobre el poder del presidente?", "que debía tener menos poder", "La ficha lo dice."),
        ("{F} Un conservador y un liberal discuten sobre quién debe votar. ¿Quién querría que votaran más ciudadanos?", "el liberal", "La ficha le atribuye esa idea a los liberales."),
        ("{F} ¿Qué relación hay entre el deseo de más libertades y las reformas de la segunda mitad del siglo XIX?", "el deseo de más libertades fue una causa de las reformas", "Fue una idea que impulsó los cambios."),
        ("{F} Un compañero dice: «Portales era liberal». Corrígelo.", "No: Portales fue un ministro conservador", "La ficha lo clasifica así."),
        ("{F} Una alumna dice: «Los liberales querían un presidente más poderoso». ¿Por qué se equivoca?", "porque querían un presidente con menos poder", "La ficha dice lo contrario."),
        ("=", "{F} ¿Cuántos años gobernó Errázuriz Zañartu?", "1876-1871", "Se resta el año de inicio al de término.", " años"),
        ("{F} ¿Por qué se dice que los conflictos continuaron después de 1833?", "porque los liberales tenían otras ideas y lograron reformas más tarde", "Las diferencias de ideas seguían."),
    ],
    ctx=("Imagina que un conservador y un liberal de 1860 debaten si el presidente debe tener más o menos poder. Según la ficha, ¿qué defendería cada uno?", "el conservador, un presidente poderoso; el liberal, un presidente con menos poder", "Los liberales querían limitar el poder del presidente."),
    sc=[("¿Qué es una idea política?", "una manera de pensar cómo debe gobernarse un país", "La definición de la clase."),
        ("{F} ¿Qué grupo defendía a la Iglesia católica con papel central?", "los conservadores", "La ficha lo dice."),
        ("¿Cuál fue una causa de las reformas liberales?", "el deseo de más libertades y menos poder presidencial", "Lo explica la clase.")],
    op=("Dibuja una tabla con dos columnas, «Conservadores (pelucones)» y «Liberales (pipiolos)». Escribe tres ideas de cada grupo, tomadas de la ficha. Debajo, explica en dos oraciones cuál fue la causa de los conflictos y una consecuencia. {F}",
        "Conservadores: gobierno fuerte, presidente poderoso, Iglesia con papel central. Liberales: más libertades, presidente con menos poder, más votantes. Causa: ideas distintas sobre cómo gobernar. Consecuencia: reformas liberales en la segunda mitad.",
        ["tres ideas por grupo", "ideas en la columna correcta", "causa y consecuencia explicadas"], ["tabla de dos columnas", "dos oraciones"], ["poner presidente poderoso en liberales", "no explicar causa ni consecuencia"],
        "Pide que cambie una idea de columna y explique por qué quedaría mal."),
    reinforce="Di tres ideas conservadoras y tres liberales de la ficha sin mirar el texto.",
    extend="Escribe una pregunta sobre qué opinaría una persona que no podía votar en el siglo XIX.",
)

# ---------------------------------------------------------------- clase 4
F = ("Ficha 13 (comparación de la Constitución de 1833 con las reformas liberales, hecha para este cuaderno). "
     "Presidente: en 1833, mandato de cinco años con una reelección inmediata posible; desde la reforma de 1871, no se permite la reelección inmediata. "
     "Voto: en 1833, solo podían votar hombres mayores de 25 años (21 si estaban casados) que supieran leer y escribir y tuvieran propiedades o cierta renta; desde la reforma de 1874, votan los hombres mayores de 21 que sepan leer y escribir, sin exigir propiedades. "
     "Religión: en 1833, la religión del Estado es la católica y no se permiten otros cultos públicos; en 1865 se acepta que otras religiones celebren sus cultos en recintos privados. "
     "Registro y matrimonio: hasta 1884, la Iglesia llevaba los registros de nacimientos y matrimonios; desde 1884, el Estado crea el Registro Civil y el matrimonio civil. "
     "En todos los casos citados, las mujeres no podían votar.")
build(
    OA3, 4, F,
    use="Aprenderé a comparar la Constitución de 1833 con las reformas liberales en el voto, el presidente y la religión. Sirve para explicar qué cambió y qué siguió igual.",
    prior=["Sé qué dice la Constitución de 1833.", "Sé qué reformas hicieron los liberales.", "Sé comparar usando un criterio."],
    explain=[
        "Comparar dos épocas es ver qué cambió y qué siguió igual. Para la organización de la república podemos comparar la Constitución de 1833 con las reformas liberales usando tres criterios: el poder del presidente, quién puede votar y el papel de la Iglesia.",
        "En 1833 el presidente podía ser reelegido de inmediato, y en 1871 se prohibió. En 1833 votaban solo hombres adultos que sabían leer y escribir y tenían propiedades; en 1874 se eliminó el requisito de propiedades. En 1833 solo se permitía la religión católica en público; en 1865 se aceptaron cultos privados de otras religiones, y en 1884 el Estado asumió los registros civiles.",
        "No todo cambió. Las mujeres seguían sin poder votar, y el Estado seguía organizado de manera centralizada, con un presidente importante. Esto muestra que una reforma puede ampliar derechos para algunas personas y dejar a otras fuera. Por eso al comparar conviene decir qué cambió, qué siguió igual y para quién.",
    ],
    vocab=[("centralizado", "con las decisiones principales tomadas en la capital"), ("requisito", "condición necesaria para hacer algo"), ("culto", "ceremonias de una religión"), ("registro civil", "oficina del Estado que anota nacimientos, matrimonios y muertes"), ("renta", "dinero que una persona recibe regularmente")],
    worked=[
        ("Comparar un criterio", "{F} ¿Qué cambió entre 1833 y 1874 en el voto?", ["En 1833 se exigían propiedades o renta; en 1874 no.", "Desde 1874 bastaba tener 21 años y saber leer y escribir."], "Se eliminó el requisito de propiedades"),
        ("Encontrar una continuidad", "{F} ¿Qué siguió igual en ambos momentos respecto del voto?", ["Comparo quién votaba en 1833 y en 1874.", "En ambos casos solo votaban hombres."], "Las mujeres no podían votar"),
    ],
    mistakes=[("Decir que en 1874 votaban todos los adultos.", "Se exagera la ampliación del voto.", "Votaban hombres de 21 años o más que supieran leer y escribir; las mujeres no."),
              ("Pensar que la reforma de 1871 terminó con el poder del presidente.", "Se confunde limitar con eliminar.", "Solo impidió la reelección inmediata; el presidente seguía siendo muy importante.")],
    T=[
        ("{F} ¿Desde qué año no se permite la reelección inmediata del presidente?", "1871", "La ficha lo indica."),
        ("{F} ¿Qué edad mínima se exigía a los votantes casados en 1833?", "21 años", "La ficha dice 25, o 21 si estaban casados."),
        ("{F} ¿Desde qué año existe el Registro Civil en Chile según la ficha?", "1884", "La ficha lo indica."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1833 y la reforma electoral de 1874?", "1874-1833", "Se resta el año menor al mayor.", " años"),
        ("{F} ¿Qué requisito se eliminó para votar con la reforma de 1874?", "tener propiedades o renta", "La ficha lo dice."),
        ("{F} ¿Qué cultos se aceptaron en 1865 y dónde?", "los de otras religiones, en recintos privados", "La ficha lo indica."),
        ("{F} Clasifica como cambio (C) o continuidad (K) entre 1833 y 1884: a) reelección inmediata; b) mujeres sin voto; c) Registro Civil del Estado; d) presidente importante.", "a: C; b: K; c: C; d: K", "Las mujeres y el presidente siguen igual en lo central."),
        ("{F} ¿Quién llevaba los registros de nacimientos y matrimonios hasta 1884?", "la Iglesia", "La ficha lo dice."),
        ("{F} Compara el voto de 1833 y el de 1874: ¿cuál amplió el voto para más hombres?", "el de 1874", "Eliminó el requisito de propiedades."),
        ("{F} Un alumno dice: «Después de 1874 votaban hombres y mujeres». Corrígelo con la ficha.", "No: las mujeres no podían votar", "La ficha lo señala."),
        ("{F} Una alumna dice: «La reforma de 1871 sacó al presidente del poder». ¿Qué error comete?", "solo impidió la reelección inmediata; el presidente seguía siendo importante", "Limitar no es eliminar."),
        ("{F} Un hombre de 22 años, soltero, que no sabe leer, ¿podía votar según la reforma de 1874?", "no, porque no sabía leer ni escribir", "Faltaba un requisito."),
        ("{F} ¿Qué dos cosas debes decir al comparar dos épocas?", "qué cambió y qué siguió igual", "Es la definición de comparación de la clase."),
    ],
    ctx=("En una exposición escolar, un compañero dice: «Con las reformas liberales, todos los chilenos adultos pudieron elegir a sus autoridades». Usa la ficha para explicar por qué no es cierto.", "las mujeres no podían votar y los hombres tenían que saber leer y escribir", "La reforma amplió el voto, pero no a todos."),
    sc=[("¿Qué se compara cuando se hace una comparación de épocas?", "qué cambió y qué siguió igual", "Es el objetivo de comparar."),
        ("{F} ¿Qué ley amplió el voto en 1874?", "la reforma electoral", "La ficha la nombra."),
        ("¿Por qué una reforma puede dejar a algunas personas fuera?", "porque amplía derechos solo para algunos grupos", "Por ejemplo, el voto no incluía a las mujeres.")],
    op=("Dibuja una tabla de tres filas (presidente, voto, religión o registros) y tres columnas: «1833», «reforma liberal» y «qué cambió o qué siguió igual». Completa con datos de la ficha. Debajo, escribe una oración que diga una continuidad importante. {F}",
        "Voto: 1833 con propiedades; 1874 sin propiedades; cambió el requisito y siguió sin voto femenino. Continuidad: las mujeres no votaban.",
        ["tres filas con datos de la ficha", "cambio o continuidad bien identificados", "una continuidad en la oración final"], ["tabla comparativa", "oración final"], ["decir que votaban todos", "no anotar ninguna continuidad"],
        "Pide que explique qué fila le mostró mejor un cambio."),
    reinforce="Cuenta a alguien de tu casa qué cambió con las reformas liberales y qué siguió igual.",
    extend="Escribe una pregunta sobre qué reforma pudo cambiar más la vida cotidiana de las familias.",
)

# ---------------------------------------------------------------- clase 5
F = ("Ficha 14 (impacto de las reformas liberales, hecha para este cuaderno). "
     "Reforma 1: en 1871 se prohíbe la reelección inmediata del presidente, lo que limita su permanencia en el poder. "
     "Reforma 2: en 1874 se amplía el voto, porque ya no se exige tener propiedades, solo saber leer y escribir. "
     "Reforma 3: en 1883 y 1884, con las leyes laicas, el Estado asume los cementerios, el Registro Civil y el matrimonio civil, y la Iglesia deja de tener esas funciones públicas. "
     "Efectos conocidos: más personas pudieron participar en elecciones; el poder del presidente quedó más limitado; las familias de distintas religiones tuvieron acceso a registros y matrimonios sin depender de la Iglesia católica.")
build(
    OA3, 5, F,
    use="Aprenderé a argumentar cuál reforma liberal tuvo mayor impacto, usando evidencia. Sirve para defender una idea con razones y para reconocer objeciones.",
    prior=["Sé qué reformas hicieron los liberales.", "Sé comparar épocas.", "Sé que un argumento tiene afirmación, evidencia y razón."],
    explain=[
        "El impacto de una reforma es lo que cambió gracias a ella. Para medirlo podemos preguntar a cuántas personas afectó, qué derechos amplió y qué cambios dejó a largo plazo. No hay una única respuesta correcta: se puede defender una reforma u otra si usamos buenos argumentos.",
        "Por ejemplo, la reforma electoral de 1874 amplió el voto a más hombres, y eso afectó a muchas personas. La reforma de 1871 limitó el poder del presidente, y eso afectó la organización del gobierno. Las leyes laicas de 1883 y 1884 cambiaron la vida cotidiana, porque el Estado asumió los registros y el matrimonio civil.",
        "Un argumento sólido incluye una objeción: una razón en contra. Por ejemplo, alguien puede decir que el voto de 1874 no cambió tanto, porque las mujeres seguían sin votar. Reconocer ese límite no debilita el argumento: lo hace más honesto y más preciso. Así se practica el pensamiento histórico.",
    ],
    vocab=[("impacto", "cambio que produce un hecho o una reforma"), ("argumentar", "defender una idea con razones y evidencia"), ("objeción", "razón en contra de una idea"), ("a largo plazo", "que dura o se nota muchos años después"), ("evidencia", "dato que apoya una afirmación")],
    worked=[
        ("Armar un argumento", "{F} Defiende que la reforma 2 tuvo impacto.", ["Afirmación: la reforma de 1874 tuvo impacto.", "Evidencia y razón: amplió el voto, así más personas pudieron participar."], "La reforma de 1874 tuvo impacto porque amplió el voto"),
        ("Reconocer una objeción", "{F} ¿Qué objeción se puede poner al argumento anterior?", ["Miro los límites del voto en la ficha.", "Las mujeres seguían sin votar."], "Las mujeres seguían sin poder votar"),
    ],
    mistakes=[("Defender una reforma sin dar datos.", "Se confunde opinión con argumento.", "Cada afirmación necesita un dato de la ficha y una razón."),
              ("Pensar que reconocer una objeción debilita el argumento.", "No se entiende para qué sirve.", "Reconocer límites hace el argumento más sólido.")],
    T=[
        ("{F} ¿Qué reforma limitó la permanencia del presidente en el poder?", "la reforma de 1871", "La ficha la describe así."),
        ("{F} ¿Qué cambió la reforma 3 respecto de quién llevaba los registros?", "el Estado asumió el Registro Civil, en lugar de la Iglesia", "La ficha lo dice."),
        ("{F} ¿Qué requisito se mantuvo en la reforma 2 para votar?", "saber leer y escribir", "La ficha lo indica."),
        ("{F} Completa: «La reforma 2 tuvo impacto porque ______». Usa un dato de la ficha.", "amplió el voto: ya no se exigía tener propiedades", "Es el dato de la reforma 2."),
        ("{F} ¿Cuál es un argumento con evidencia? A) Las leyes laicas fueron importantes porque sí. B) Las leyes laicas tuvieron impacto porque el Estado asumió los registros y el matrimonio civil.", "B", "B tiene afirmación y razón con dato."),
        ("{F} Un compañero defiende la reforma 1 diciendo que fue la más importante. ¿Qué dato de la ficha puede usar?", "que prohibió la reelección inmediata y limitó la permanencia del presidente", "Es el contenido de la reforma 1."),
        ("{F} ¿Qué objeción se puede poner a quien dice que la reforma 2 cambió todo en el voto?", "que las mujeres seguían sin votar", "Es el límite principal de esa reforma."),
        ("{F} ¿Qué reforma cambió la vida cotidiana de las familias de distintas religiones?", "las leyes laicas de 1883 y 1884", "Permitieron registros y matrimonio civil sin depender de la Iglesia católica."),
        ("{F} Ordena las tres reformas de la más antigua a la más reciente.", "reforma 1 (1871), reforma 2 (1874), reforma 3 (1883-1884)", "Siguen el orden de los años."),
        ("=", "{F} ¿Cuántos años pasaron entre la reforma 1 y el inicio de la reforma 3?", "1883-1871", "Se resta el año menor al mayor.", " años"),
        ("{F} Una alumna dice: «La reforma 3 solo afectó a la Iglesia». ¿Qué dato la contradice?", "que también cambió los registros y el matrimonio de las familias", "Afectó la vida cotidiana de muchas personas."),
        ("{F} Elige la mejor razón para decir que la reforma 1 tuvo impacto a largo plazo: A) cambió una regla de la constitución que seguiría valiendo para los gobiernos siguientes; B) fue la primera de la lista.", "A", "Una regla constitucional afecta a todos los gobiernos siguientes."),
        ("=", "{F} ¿Cuántos años pasaron entre la reforma electoral y el final de las leyes laicas, en 1884?", "1884-1874", "Se resta el año menor al mayor.", " años"),
    ],
    ctx=("Tu curso debate qué reforma liberal merece un afiche para el aniversario del colegio. Escribe una oración que recomiende una y dé una razón.", "Recomiendo la reforma de 1874, porque amplió el voto a más hombres", "Sirve cualquier reforma con razón basada en la ficha."),
    sc=[("¿Cuáles son las tres partes de un argumento?", "afirmación, evidencia y razón", "Así se organiza un argumento."),
        ("{F} ¿Qué reforma cambió el matrimonio civil?", "las leyes laicas de 1883 y 1884", "La ficha las describe."),
        ("¿Para qué sirve una objeción?", "para que el argumento sea más honesto y preciso", "Reconoce límites y razones contrarias.")],
    op=("Escribe un texto de cinco oraciones: 1) elige una reforma; 2) di qué cambió con un dato; 3) explica a quién afectó; 4) escribe una objeción; 5) responde a la objeción. {F}",
        "Elijo la reforma de 1874. Amplió el voto porque ya no se exigían propiedades. Afectó a más hombres. Una objeción es que las mujeres seguían sin votar. Aun así, fue un paso hacia más participación.",
        ["reforma elegida de la ficha", "dato correcto", "objeción y respuesta"], ["texto de cinco oraciones"], ["no usar dato de la ficha", "no incluir objeción"],
        "Pide que lea su argumento en voz alta y señale la evidencia."),
    reinforce="Di en voz alta un argumento completo sobre una reforma de la ficha.",
    extend="Escribe una segunda objeción posible y cómo la responderías.",
)
