"""Cuaderno del estudiante, 4.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR01 (comprensión de relatos orales con expresiones culturalmente significativas, en contexto de
revitalización lingüística) y OA LR02 (comunicación oral de ideas y comentarios con esas expresiones).

Criterio de autoría: los relatos, personajes, diálogos, intervenciones y devoluciones de práctica son inventados,
están en castellano y se declaran como tales; no pertenecen a ningún pueblo y no son relatos fundacionales ni
cosmogónicos reales (esos los cuenta el educador/a tradicional o la comunidad). Las únicas expresiones en lengua
indígena son las ya atestiguadas (mari mari, chaltumay, ko, antü, kuyen, ruka, mapu, ñuke en mapuzugun; iorana,
maururu en rapa nui), siempre con su ficha y con su grafía exacta. No se escribe pronunciación ni gramática. No se
mide la pertenencia ni la identidad de nadie por saber o no una lengua, y nadie está obligado a contar cosas de su
familia: siempre hay una opción ficticia o de pasar. Cuándo, a quién y en qué ocasiones se dice cada expresión lo
enseñan el educador/a tradicional y la comunidad; cada tarea abierta lo remite a ellos.
"""
from __future__ import annotations

from student_content_lc4_b import FICHA_PAL, L, M, T, W
from student_lessons import arith, ex

LR1, LR2 = "LC04 OA LR01", "LC04 OA LR02"

RELATO2 = "Relato de práctica (inventado; no es de ningún pueblo): «Nora despertó cuando el antü asomó. Fue al río a buscar ko. En el camino encontró a su ñuke y juntas llevaron el ko a la ruka. Allí regaron la huerta y Nora dijo: chaltumay.»"

# =================================================================== OA LR01 · relatos y expresiones en revitalización
L(
    LR1, 1,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé qué es la revitalización de una lengua y a reconocer, sin que nadie me evalúe, las palabras que ya he oído. Sirve para empezar a escuchar relatos con confianza.",
    prior=["Sé que mari mari, chaltumay, ko y antü son palabras de la ficha.", "Sé que nadie es evaluado por hablar o no una lengua."],
    explain=[
        "La memoria lingüística es el conjunto de palabras y expresiones que una persona ha oído alguna vez, en cualquier lengua: en la casa, en la escuela o en la calle. Todas las personas tienen una memoria lingüística distinta, y ninguna es mejor que otra. Recordar pocas palabras no es una falta.",
        "Algunas lenguas indígenas tienen hoy menos personas que las hablan. Por eso muchas comunidades trabajan para fortalecerlas y volver a usarlas. Eso se llama revitalización. Escuchar con respeto, aprender de quienes enseñan y no burlarse de nadie ayuda a la revitalización.",
        "Hoy no hay prueba ni nota. Hago una lista de palabras que he oído y las comparo con la ficha. Si no conozco ninguna, está bien: aprenderé. Qué palabras enseñar y cómo decirlas lo decide el educador tradicional con su comunidad.",
    ],
    vocab=[("memoria lingüística", "palabras y expresiones que alguien ha oído"), ("revitalización", "trabajo de una comunidad para fortalecer su lengua"), ("hablante", "persona que habla una lengua"), ("expresión", "palabra o frase de una lengua"), ("examen", "prueba para ver qué sabe alguien")],
    worked=[
        W("Reconocer una palabra de la ficha", "Una niña dice que ha oído «ko». La ficha dice ko es agua en mapuzugun. ¿Qué palabra de la ficha reconoció?", ["Busco ko en la ficha.", "Está: ko es agua."], "ko, agua"),
        W("Sin examen", "Un compañero conoce 1 palabra y otro conoce 5. El profesor dice que no hay nota. ¿Quién debe sentirse mal por saber menos?", ["No hay prueba.", "Nadie debe sentirse mal."], "Nadie"),
    ],
    mistakes=[
        M("Burlarse de alguien que conoce pocas palabras.", "Todos estamos aprendiendo y la burla aleja.", "Ofrezco ayuda con respeto."),
        M("Pensar que quien no habla una lengua no pertenece a su pueblo.", "La pertenencia no se mide por la lengua.", "No evalúo la identidad de nadie."),
    ],
    R=[
        ex("La revitalización es: A) el trabajo de una comunidad para fortalecer su lengua B) una fiesta.", "A", "Revitalizar es fortalecer."),
        ex("La memoria lingüística son: A) las palabras que he oído B) el número de mi sala.", "A", "Son palabras y expresiones que recuerdo."),
        ex("Si no conozco ninguna palabra, ¿está bien o está mal?", "está bien", "Aprender comienza desde cualquier punto."),
    ],
    C=[
        ex("Verdadero o falso: hoy hay una prueba para ver cuántas palabras sé.", "Falso", "No hay prueba ni nota."),
        ex("Según la ficha, «chaltumay» es: A) gracias B) casa.", "A", "La ficha dice gracias."),
        ex("¿Una persona que no habla una lengua indígena deja de pertenecer a su pueblo: sí o no?", "no", "La pertenencia no se mide por la lengua."),
    ],
    A=[
        arith("En el curso, 4 estudiantes recordaron 2 palabras cada uno. ¿Cuántas palabras recordaron entre todos?", "4 * 2", "Multiplico estudiantes por palabras."),
        ex("Lista de una niña: ko, antü, perro. ¿Cuáles de esas palabras están en la ficha?", "ko y antü", "Perro no está en la ficha."),
        ex("Según la ficha, ¿cuál de estas palabras significa casa en mapuzugun: ruka o mapu?", "ruka", "La ficha dice que «ruka» es casa y «mapu» es tierra."),
    ],
    Z=[
        ex("Eva: «Me da vergüenza porque sé una palabra». Lola: «No pasa nada, aprendamos juntas». ¿Quién ayuda más a la revitalización?", "Lola", "Ofrece apoyo sin burla."),
        ex("Un compañero dice que quien no habla una lengua indígena «no es de verdad» de ese pueblo. ¿Qué respondes: A) la pertenencia no se mide por la lengua B) tiene razón?", "A", "La identidad no se evalúa por hablar o no."),
    ],
    D=[
        arith("En la lista del curso hay 9 palabras y 4 están en la ficha. ¿Cuántas no están en la ficha?", "9 - 4", "Resto las de la ficha del total."),
        ex("Una persona quiere enseñar palabras a su curso sin consultar al educador tradicional. ¿Qué debe hacer: A) consultar qué palabras puede enseñar B) enseñar las que quiera?", "A", "Quien decide es el educador con su comunidad."),
    ],
    context=[ex("Un compañero se ríe porque otro conoce pocas palabras. ¿Qué dices: «Aprendamos juntos, nadie nos evalúa» o «Tienes razón en reírte»?", "«Aprendamos juntos, nadie nos evalúa»", "El respeto ayuda a revitalizar.")],
    selfcheck=[
        ex("¿Cómo se llama el trabajo de una comunidad para fortalecer su lengua?", "revitalización", "Eso es revitalizar."),
        ex("¿Hay nota por saber más o menos palabras?", "No", "No hay prueba."),
        ex("¿Qué hago con una palabra que no conozco?", "pregunto y aprendo", "Aprender comienza preguntando."),
    ],
    task=T(
        "Haz una lista con tres palabras que hayas oído alguna vez en cualquier lengua (puedes usar las de la ficha) y escribe dónde las oíste: en la sala, en un libro o en una conversación. No tienes que contar nada de tu familia. Si prefieres no escribir tu lista, escribe tres palabras de la ficha y su significado.",
        "Palabras: mari mari (saludo), ko (agua), antü (sol). Las vi en la ficha de la sala.",
        ["escribe tres palabras", "dice dónde las vio u oyó (sala, libro o ficha)", "no cuenta cosas privadas"],
        ["lista escrita en el cuaderno"],
        ["compararse con otros", "contar vivencias familiares"],
        "Valora que escribió palabras sin compararse; si contó cosas privadas, recuérdale que puede usar la ficha.",
    ),
    reinforce="Di en voz alta dos palabras de la ficha y su significado.",
    extend="Pregunta a una persona de tu casa si recuerda alguna palabra de otra lengua y escúchala con respeto.",
)

L(
    LR1, 2,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado; una persona puede leerlo en voz alta. " + FICHA_PAL,
    use="Aprenderé a escuchar un relato breve con expresiones en lengua indígena y a entender su significado por el contexto y la ficha. Sirve para comprender sin necesidad de traducir palabra por palabra.",
    prior=["Sé escuchar un relato la primera vez para disfrutarlo.", "Sé usar la ficha de palabras."],
    explain=[
        "Un relato fundacional cuenta cómo empezó algo; uno cosmogónico cuenta cómo se formó el mundo. Los relatos reales de ese tipo pertenecen a los pueblos y los cuenta el educador tradicional o la comunidad. Hoy practico con un relato inventado de la vida diaria, que no es de ningún pueblo.",
        "Al escuchar un relato con expresiones en lengua indígena uso el contexto, es decir, lo que dice la frase alrededor de la palabra. Por ejemplo, «fue al río a buscar ko»: como se busca en el río, puede ser agua. La ficha me confirma que ko es agua. No necesito traducir cada palabra: entiendo el sentido completo.",
        "Escucho primero para disfrutar. Luego, en una segunda escucha, marco las expresiones y las relaciono con la ficha. Nunca invento cómo suena una palabra ni qué significa; si no sé, pregunto.",
    ],
    vocab=[("relato fundacional", "relato que cuenta cómo empezó algo"), ("relato cosmogónico", "relato que cuenta cómo se formó el mundo"), ("contexto", "palabras alrededor que ayudan a entender"), ("sentido", "idea completa de lo que se dice"), ("segunda escucha", "volver a escuchar para revisar los detalles")],
    worked=[
        W("Entender por contexto", RELATO2 + " ¿Qué busca Nora en el río?", ["Leo la frase: «fue al río a buscar ko».", "La ficha dice que ko es agua."], "agua"),
        W("Confirmar con la ficha", RELATO2 + " ¿A quién encuentra Nora?", ["Busco la frase «encontró a su ñuke».", "La ficha dice que ñuke es madre."], "A su madre"),
    ],
    mistakes=[
        M("Traducir palabra por palabra y perder el sentido.", "El sentido está en toda la frase.", "Uso el contexto y la ficha."),
        M("Pensar que este relato es un relato fundacional real.", "Está inventado para practicar.", "Los relatos reales los cuenta el educador tradicional o la comunidad."),
    ],
    R=[
        ex("Un relato cosmogónico cuenta: A) cómo se formó el mundo B) una receta.", "A", "Cosmogónico habla del origen del mundo."),
        ex(RELATO2 + " ¿Cómo se llama la niña?", "Nora", "El relato la nombra."),
        ex("Según la ficha, «ruka» es: A) casa B) sol.", "A", "La ficha dice casa."),
    ],
    C=[
        ex(RELATO2 + " ¿Qué asomó cuando Nora despertó?", "el antü", "El texto dice que el antü asomó."),
        ex("Verdadero o falso: este relato es un relato fundacional de un pueblo.", "Falso", "Es inventado para practicar."),
        ex(RELATO2 + " ¿Adónde llevaron el ko Nora y su ñuke?", "a la ruka", "El texto dice que llevaron el ko a la ruka."),
    ],
    A=[
        ex("Ordena según el relato: A) regaron la huerta B) Nora despertó C) encontró a su ñuke D) fue al río. Escribe las letras.", "B, D, C, A", "Despertó, fue al río, encontró a su ñuke y regaron."),
        ex(RELATO2 + " ¿Qué dijo Nora al final?", "chaltumay", "Es la última palabra de Nora."),
        arith("Imagina que Nora fue al río 3 mañanas y su ñuke la acompañó 2 de esas mañanas. ¿En cuántas mañanas fue sola?", "3 - 2", "Resto las mañanas acompañada del total."),
    ],
    Z=[
        ex("Ana dice que «chaltumay» en el relato significa «adiós». Rita dice que significa «gracias». ¿Quién tiene razón según la ficha?", "Rita", "La ficha dice gracias."),
        ex("Un niño dice que sabe lo que significa «ko» porque se lo imaginó. ¿Qué es mejor: A) confirmar con la ficha B) quedarse con su idea?", "A", "La ficha confirma el significado."),
    ],
    D=[
        arith("El relato tiene 4 oraciones. Una niña recordó 3. ¿Cuántas le faltan por recordar?", "4 - 3", "Resto las recordadas del total."),
        ex("Una persona quiere contar este relato como si fuera de un pueblo. ¿Qué error comete: A) atribuye un relato inventado a un pueblo B) lo cuenta en voz alta?", "A", "No pertenece a ningún pueblo."),
    ],
    context=[ex("Escuchas «fue al río a buscar ko» y no recuerdas qué es ko. ¿Qué haces: «uso el contexto y reviso la ficha» o «adivino sin mirar»?", "«uso el contexto y reviso la ficha»", "Así confirmo el significado.")],
    selfcheck=[
        ex("¿Qué cuenta un relato cosmogónico?", "cómo se formó el mundo", "Habla del origen del mundo."),
        ex("¿Qué es el contexto?", "las palabras alrededor que ayudan a entender", "Aporta el sentido."),
        ex("¿Quién cuenta los relatos reales de un pueblo?", "el educador tradicional o la comunidad", "Ellos los cuidan."),
    ],
    task=T(
        "Lee o escucha el relato inventado de Nora: " + RELATO2 + " Escribe tres cosas: dónde pasó, a quién encontró Nora y qué significa «chaltumay» según la ficha. Subraya las palabras de la ficha que aparecen en el relato.",
        "Pasó en el río y la ruka. Nora encontró a su ñuke, su madre. Chaltumay significa gracias. Subrayé antü, ko, ñuke, ruka y chaltumay.",
        ["responde los tres datos", "usa la ficha", "subraya las palabras de la ficha"],
        ["respuestas y subrayado en el cuaderno"],
        ["traducir sin sentido", "creer que es un relato real"],
        "Valora que usó contexto y ficha; si dijo que es de un pueblo, pídele que recuerde que es inventado.",
    ),
    reinforce="Cuenta el relato de Nora con tus palabras, usando las palabras de la ficha.",
    extend="Pide a una persona de tu casa que escuche tu resumen y diga si entendió.",
)

L(
    LR1, 3,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado. " + FICHA_PAL,
    use="Aprenderé a ordenar los hechos de un relato y a explicar su idea central. Sirve para comprender qué pasó y qué mensaje deja.",
    prior=["Sé que la secuencia es el orden de los hechos.", "Sé entender expresiones por contexto y ficha."],
    explain=[
        "Para comprender un relato primero reconstruyo su secuencia: qué pasó primero, qué después y qué al final. Uso las palabras primero, luego, después y finalmente. Luego pregunto por su sentido: ¿qué idea deja el relato?",
        "La idea central es el mensaje principal. En el relato de Nora, la idea central puede ser: «compartir el trabajo ayuda a la familia». Esa idea sale de los hechos: Nora busca agua, encuentra a su madre y juntas riegan la huerta.",
        "Una idea central de un relato inventado la puedo decir yo con mis palabras. En un relato real de un pueblo, el significado profundo lo explica el educador tradicional o la comunidad; yo no lo interpreto por mi cuenta.",
    ],
    vocab=[("secuencia", "orden de los hechos"), ("idea central", "mensaje principal de un relato"), ("sentido", "lo que quiere decir el relato en conjunto"), ("hecho", "algo que pasa en el relato"), ("compartir", "hacer algo juntos o repartir")],
    worked=[
        W("Ordenar", RELATO2 + " Ordena: A) llevaron el ko a la ruka B) Nora despertó C) encontró a su ñuke. Primero, luego, después.", ["Primero despertó.", "Luego encontró a su ñuke.", "Después llevaron el ko."], "B, C, A"),
        W("Idea central", "Hechos del relato: Nora busca agua, encuentra a su madre, regaron la huerta juntas. ¿Cuál puede ser la idea central?", ["Los hechos muestran trabajo compartido.", "Todos tratan del agua y la familia."], "Compartir el trabajo ayuda a la familia"),
    ],
    mistakes=[
        M("Contar un detalle suelto y creer que es la idea central.", "La idea central une todos los hechos.", "Pregunto qué mensaje dejan todos los hechos."),
        M("Interpretar yo el significado de un relato real.", "Ese significado lo explica la comunidad.", "Pregunto al educador tradicional."),
    ],
    R=[
        ex("La idea central es: A) el mensaje principal B) el título.", "A", "La idea central es el mensaje."),
        ex(RELATO2 + " ¿Qué hizo Nora primero?", "despertó", "Es el primer hecho."),
        ex("¿Qué palabra usas para empezar a contar una secuencia: primero o finalmente?", "primero", "Primero abre la secuencia."),
    ],
    C=[
        ex(RELATO2 + " ¿Qué regaron Nora y su ñuke?", "la huerta", "El relato dice que regaron la huerta."),
        ex("Verdadero o falso: puedo decidir yo el significado de un relato real de un pueblo.", "Falso", "Lo explica la comunidad."),
        ex("Hechos: Nora busca agua y comparte el trabajo. ¿La idea central trata de compartir o de volar?", "compartir", "Los hechos hablan de trabajo compartido."),
    ],
    A=[
        ex("Ordena: A) regaron la huerta B) llevaron el ko C) Nora fue al río D) Nora dijo chaltumay. Escribe las letras.", "C, B, A, D", "Fue al río, llevaron el ko, regaron y agradeció."),
        arith("Imagina que Nora llevó 2 vasijas de ko el lunes y 3 el martes. ¿Cuántas vasijas llevó en total?", "2 + 3", "Sumo las vasijas de los dos días."),
        ex("¿Qué palabra del relato expresa agradecimiento?", "chaltumay", "La ficha dice gracias."),
    ],
    Z=[
        ex("Dos ideas centrales. Eva: «Compartir el trabajo ayuda a la familia». Gaspar: «Nora despertó con el antü». ¿Cuál une todos los hechos?", "la de Eva", "La de Gaspar es un detalle."),
        ex("Una niña dice que el relato real de su pueblo significa algo que ella supone. ¿Qué debe hacer: A) preguntar al educador tradicional B) dejarlo así?", "A", "El significado lo explica la comunidad."),
    ],
    D=[
        arith("Un relato tiene 6 hechos. En una reconstrucción se ordenaron 4. ¿Cuántos faltan por ordenar?", "6 - 4", "Resto los ordenados del total."),
        ex("En el relato, Nora agradece al final con «chaltumay». ¿Cómo ayuda eso a la idea central: A) muestra gratitud por compartir B) no tiene relación?", "A", "La gratitud refuerza el compartir."),
    ],
    context=[ex("Te piden explicar el sentido del relato de Nora en una frase. ¿Qué dices: «Compartir el trabajo ayuda a la familia» o «Nora despertó con el antü»?", "«Compartir el trabajo ayuda a la familia»", "Es la idea central.")],
    selfcheck=[
        ex("¿Qué es la idea central?", "el mensaje principal", "Resume el sentido del relato."),
        ex("¿Qué palabras uso para ordenar hechos?", "primero, luego, después y finalmente", "Marcan la secuencia."),
        ex("¿Quién explica el significado de un relato real?", "el educador tradicional o la comunidad", "Ellos lo cuidan."),
    ],
    task=T(
        "Con el relato de Nora (" + RELATO2 + ") escribe en tres frases la secuencia usando primero, luego y finalmente, y una frase con la idea central con tus palabras. Añade una pregunta que le harías al educador tradicional sobre cómo se cuentan los relatos de su pueblo.",
        "Primero Nora despertó. Luego fue al río y encontró a su ñuke. Finalmente regaron la huerta. Idea central: compartir el trabajo ayuda a la familia. Pregunta: ¿cómo se cuentan sus relatos?",
        ["tres frases ordenadas", "idea central con sus palabras", "pregunta para quien enseña"],
        ["secuencia, idea y pregunta en el cuaderno"],
        ["confundir un detalle con la idea central", "interpretar relatos reales"],
        "Valora que ordenó y dio una idea central; si dio un detalle suelto, pídele que una todos los hechos.",
    ),
    reinforce="Cuenta el relato en orden con primero, luego y finalmente.",
    extend="Pregunta a una persona de tu casa qué idea central le deja un cuento corto que te cuente.",
)

L(
    LR1, 4,
    materials="Lápiz y hoja. El relato está escrito aquí y es inventado. " + FICHA_PAL,
    use="Aprenderé a relacionar un relato con lo que conozco usando una opción ficticia, para no tener que contar cosas privadas. Sirve para opinar con fundamentos y cuidar nuestra privacidad.",
    prior=["Sé la idea central del relato de Nora.", "Sé que nadie tiene que contar vida privada."],
    explain=[
        "Relacionar un relato con lo que conozco ayuda a entenderlo. Puedo relacionarlo de tres maneras: con un conocimiento general, como «el agua es necesaria para las plantas»; con un personaje inventado; o con una experiencia propia, si quiero. La tercera opción es siempre voluntaria.",
        "Una opción ficticia es una situación inventada que uso como ejemplo. Por ejemplo: «Un niño inventado, Beto, cuida el agua de su escuela». Con ella puedo opinar sin hablar de mi familia. Mi opinión debe llevar un porque y un dato del relato.",
        "Cuando relaciono un relato de un pueblo con mi vida, no digo que mi experiencia es igual a la del pueblo. Mi mirada es solo mía. Y si el relato es de una comunidad, mi opinión no corrige su cosmovisión: la escucho y pregunto.",
    ],
    vocab=[("opción ficticia", "situación inventada que uso como ejemplo"), ("conocimiento general", "algo que se sabe en común, como que el agua sirve a las plantas"), ("voluntario", "que se hace solo si uno quiere"), ("cosmovisión", "manera en que un pueblo ve el mundo"), ("opinión", "lo que pienso con una razón")],
    worked=[
        W("Relacionar con un conocimiento general", RELATO2 + " Conocimiento general: las plantas necesitan agua. ¿Cómo se relaciona con el relato?", ["Nora lleva agua a la huerta.", "Las plantas necesitan agua."], "Nora riega la huerta porque las plantas necesitan agua"),
        W("Elegir una opción ficticia", "Pía no quiere hablar de su casa. ¿Qué opción puede usar para relacionar el relato?", ["Puede inventar un niño.", "Así no cuenta cosas privadas."], "Un personaje inventado, como Beto"),
    ],
    mistakes=[
        M("Obligar a alguien a contar cosas de su casa.", "Es privado.", "Ofrezco opciones ficticias."),
        M("Decir que mi experiencia es igual a la de un pueblo.", "Mi mirada no habla por un pueblo.", "Hablo solo por mí."),
    ],
    R=[
        ex("Una opción ficticia es: A) una situación inventada B) una verdad privada.", "A", "Ficticia significa inventada."),
        ex("Relacionar con mi experiencia propia es: A) voluntario B) obligatorio.", "A", "Cada uno decide."),
        ex("Un conocimiento general es: A) algo que se sabe en común B) un secreto.", "A", "Es un saber compartido."),
    ],
    C=[
        ex("Verdadero o falso: debo contar una vivencia familiar para opinar.", "Falso", "Puedo usar opciones ficticias."),
        ex("Opción ficticia: «Beto cuida el agua de su escuela». ¿Se relaciona con el relato de Nora: sí o no?", "sí", "Ambos cuidan el agua."),
        ex("Una opinión debe llevar: A) una razón con porque B) un silencio.", "A", "La razón la fundamenta."),
    ],
    A=[
        ex("Ordena: A) doy mi opinión B) elijo cómo relacionar (general, ficticia o propia) C) leo el relato. Escribe las letras.", "C, B, A", "Leo, elijo y opino."),
        arith("Un grupo escribe 3 opiniones con una opción ficticia cada una y 2 con un conocimiento general. ¿Cuántas opiniones son?", "3 + 2", "Sumo las dos clases de opiniones."),
        ex("Escribe «general» o «ficticia»: «Las plantas necesitan agua».", "general", "Es algo que se sabe en común."),
    ],
    Z=[
        ex("Eva: «Me gustó porque Nora comparte el trabajo con su madre». Gaspar: «Me gustó». ¿Quién opinó con fundamento?", "Eva", "Da una razón y un dato."),
        ex("Una niña dice que su opinión es igual a la de «todos los pueblos». ¿Qué error comete: A) habla por todos los pueblos B) usa una opción ficticia?", "A", "No puede hablar por todos."),
    ],
    D=[
        arith("De 25 estudiantes, 10 usaron opciones ficticias. ¿Cuántos usaron otras formas?", "25 - 10", "Resto los de opción ficticia."),
        ex("Una persona escribe una opinión sobre un relato real que escuchó de una comunidad y dice que «está mal contado». ¿Qué conviene: A) preguntar cómo se cuenta B) corregirlo ella?", "A", "La forma de contar la define la comunidad."),
    ],
    context=[ex("Te preguntan qué te recuerda el relato de Nora. ¿Respondes «un niño inventado, Beto, que cuida el agua» o «cuento cosas de mi casa»?", "«un niño inventado, Beto, que cuida el agua»", "Es una opción ficticia que protege tu privacidad.")],
    selfcheck=[
        ex("¿Qué es una opción ficticia?", "una situación inventada que uso como ejemplo", "No requiere hablar de uno mismo."),
        ex("¿Qué debe llevar una opinión?", "una razón", "La razón la fundamenta."),
        ex("¿Es obligatorio contar mi vida?", "No", "Es una decisión voluntaria."),
    ],
    task=T(
        "Relaciona el relato de Nora con lo que sabes, usando una opción ficticia o un conocimiento general. Escribe tu opinión con este modelo: «Me gustó / no me gustó… porque… En el relato dice…». No cuentes cosas de tu familia.",
        "Me gustó porque Nora comparte el trabajo con su ñuke. En el relato dice «juntas llevaron el ko a la ruka». Opción ficticia: Beto cuida el agua de su escuela.",
        ["usa una opción ficticia o un conocimiento general", "da una razón y un dato", "no cuenta cosas privadas"],
        ["opinión escrita en el cuaderno"],
        ["contar vida privada", "no dar razón"],
        "Valora que fundamentó con un dato; si contó cosas privadas, recuérdale que puede usar una opción ficticia.",
    ),
    reinforce="Di en voz alta una opinión sobre el relato con «porque».",
    extend="Pide a una persona de tu casa su opinión sobre el relato y anota su razón.",
)

L(
    LR1, 5,
    materials="Lápiz, hoja y colores. Las ideas de devolución están escritas aquí. " + FICHA_PAL,
    use="Aprenderé a crear una devolución, es decir, algo con lo que agradezco y aporto a quien me enseñó, sin invadir ni copiar. Sirve para ayudar a fortalecer una lengua con respeto.",
    prior=["Sé qué es la revitalización.", "Sé que la fuente de un saber merece reconocimiento."],
    explain=[
        "Una devolución es lo que doy a cambio de lo que aprendí. No es una nota ni un adorno: es un gesto útil. Por ejemplo, una tarjeta de gracias, un afiche con las palabras de la ficha con su significado y su fuente, o una lista de preguntas para seguir aprendiendo.",
        "Una buena devolución cumple cuatro criterios. Nombra la fuente: quién me enseñó. Copia las palabras con su grafía exacta. Es útil para otras personas del curso. Y no inventa palabras ni significados. Si va a compartirse, primero se muestra al educador tradicional.",
        "Aportar a la revitalización no significa hablar perfecto. Significa escuchar, aprender con respeto, cuidar las palabras y agradecer a quien enseña. Con «chaltumay» en mapuzugun o «maururu» en rapa nui puedo decir gracias, según me enseñen.",
    ],
    vocab=[("devolución", "gesto con que agradezco y aporto a quien me enseñó"), ("fuente", "quien me enseñó o de donde aprendí"), ("afiche", "papel con dibujo y texto para mostrar"), ("aportar", "dar algo útil a otros"), ("agradecer", "decir gracias con palabras o gestos")],
    worked=[
        W("Elegir una devolución respetuosa", "Opción A: un afiche con tres palabras de la ficha, su significado y la fuente. Opción B: un afiche con palabras inventadas que suenan bonitas. ¿Cuál es respetuosa?", ["A usa palabras de la ficha con fuente.", "B inventa palabras."], "A"),
        W("Revisar los criterios", "Un afiche tiene la fuente, la grafía copiada de la ficha y es útil para el curso, pero no dice si pidió permiso. ¿Qué le falta?", ["Revisa los cuatro criterios.", "Falta que se lo muestre al educador tradicional."], "Mostrarlo al educador tradicional antes de compartir"),
    ],
    mistakes=[
        M("Inventar palabras para que el afiche se vea más completo.", "No son validadas.", "Uso solo las de la ficha."),
        M("Compartir el afiche sin mostrarlo al educador tradicional.", "Puede tener errores o usos no autorizados.", "Se lo muestro primero."),
    ],
    R=[
        ex("Una devolución es: A) un gesto con que agradezco y aporto B) una prueba.", "A", "Devolver es agradecer y aportar."),
        ex("Un afiche con la fuente, ¿respeta la autoría: sí o no?", "sí", "Nombrar la fuente reconoce a quien enseñó."),
        ex("Según la ficha, «maururu» es: A) gracias en rapa nui B) agua.", "A", "La ficha dice gracias en rapa nui."),
    ],
    C=[
        ex("Verdadero o falso: puedo inventar palabras para el afiche.", "Falso", "Solo uso palabras validadas."),
        ex("¿Cuál es un criterio de una buena devolución: A) nombra la fuente B) usa palabras que suenan bonitas aunque sean inventadas?", "A", "Nombrar la fuente es uno de los cuatro criterios; inventar palabras los incumple."),
        ex("Antes de compartir un afiche con palabras de la lengua, ¿lo muestro al educador tradicional o lo publico?", "lo muestro al educador tradicional", "Puede revisar que esté correcto."),
    ],
    A=[
        arith("Un afiche tiene 3 palabras de la ficha. El curso hace 4 afiches. ¿Cuántas palabras hay en total?", "3 * 4", "Multiplico palabras por afiches."),
        ex("Ordena: A) comparto con el curso B) lo muestro al educador tradicional C) hago el afiche. Escribe las letras.", "C, B, A", "Hago, muestro y comparto."),
        ex("Afiche con «ko — agua — fuente: educador tradicional». ¿Qué criterio cumple al nombrar al educador?", "nombra la fuente", "Dice quién enseñó."),
    ],
    Z=[
        ex("Dos devoluciones. Eva: tarjeta de gracias con «chaltumay» copiado de la ficha. Gaspar: afiche con palabras que inventó. ¿Cuál aporta con respeto?", "la de Eva", "Gaspar usó palabras inventadas."),
        ex("Una persona quiere decir gracias a un educador de rapa nui. ¿Qué palabra de la ficha elige: A) maururu B) chaltumay?", "A", "«maururu» es gracias en rapa nui."),
    ],
    D=[
        arith("En un curso, 28 estudiantes hacen una tarjeta de gracias. 20 ya la entregaron. ¿Cuántas faltan por entregar?", "28 - 20", "Resto las entregadas del total."),
        ex("Una persona dice que su afiche ayuda a revitalizar una lengua porque tiene muchas palabras, aunque algunas las inventó. ¿Qué responde: A) no ayuda si hay palabras inventadas B) igual ayuda?", "A", "Las palabras inventadas confunden y no respetan la lengua."),
    ],
    context=[ex("El educador tradicional te enseñó tres palabras. ¿Qué haces para agradecer: «hago una tarjeta con tres palabras de la ficha y la fuente» o «no hago nada»?", "«hago una tarjeta con tres palabras de la ficha y la fuente»", "Es una devolución respetuosa.")],
    selfcheck=[
        ex("¿Qué es una devolución?", "un gesto con que agradezco y aporto", "Es un aporte a quien enseñó."),
        ex("¿Qué palabra de la ficha significa gracias en mapuzugun?", "chaltumay", "La ficha lo dice."),
        ex("¿A quién muestro mi trabajo antes de compartirlo?", "al educador tradicional", "Él o ella lo revisa."),
    ],
    task=T(
        "Crea una devolución en papel para quien te enseñó las palabras de la ficha: una tarjeta o un afiche con tres palabras de la ficha, su significado y la fuente («aprendí con…»). Revisa los cuatro criterios: fuente, grafía, utilidad y sin inventos. Escribe una pregunta para el educador tradicional sobre cómo puede ayudar el curso a fortalecer su lengua.",
        "Afiche: ko — agua; antü — sol; kuyen — luna. Fuente: aprendí con el educador tradicional. Pregunta: ¿cómo podemos ayudar a fortalecer su lengua?",
        ["tres palabras con significado y fuente", "grafía exacta", "pregunta para quien enseña"],
        ["tarjeta o afiche en papel"],
        ["inventar palabras", "compartir sin mostrar"],
        "Valora que cumplió los criterios; si inventó palabras, pídele que use la ficha.",
    ),
    reinforce="Revisa tu devolución con los cuatro criterios en voz alta.",
    extend="Muestra tu devolución a una persona de tu casa y pregúntale si entiende para qué sirve.",
)

# =================================================================== OA LR02 · comunicación oral con expresiones en revitalización
L(
    LR2, 1,
    materials="Lápiz y hoja. Las situaciones están escritas aquí y son inventadas. " + FICHA_PAL,
    use="Aprenderé a elegir una situación de comunicación y a decidir qué idea o sentimiento quiero expresar. Sirve para hablar con un propósito claro.",
    prior=["Sé qué es el interlocutor.", "Sé que las expresiones de la ficha están validadas."],
    explain=[
        "Una situación comunicativa es el momento en que hablo con alguien. Para elegirla pienso en cuatro cosas: quién escucha, dónde estoy, para qué hablo y qué quiero expresar. Lo que expreso puede ser una idea, como «el agua es importante», o un sentimiento, como alegría o gratitud.",
        "En este cuaderno practico con situaciones inventadas: saludar a una visita, agradecer a quien me enseñó y presentar una palabra de la ficha al curso. En cada una puedo usar una expresión de la ficha que corresponda al propósito: un saludo para saludar o gracias para agradecer.",
        "Elijo situaciones que no me expongan: no tengo que hablar de mi familia ni de mis emociones íntimas. Si dudo cuándo se usa una expresión, pregunto al educador tradicional. Elegir bien la situación hace que mis palabras sean adecuadas.",
    ],
    vocab=[("situación comunicativa", "momento en que hablo con alguien"), ("propósito", "para qué hablo"), ("idea", "pensamiento que quiero decir"), ("sentimiento", "lo que siento, como alegría o gratitud"), ("adecuado", "que corresponde a la situación")],
    worked=[
        W("Elegir expresión según el propósito", "Situación inventada: agradecer a quien me enseñó. Expresiones de la ficha: mari mari (saludo), chaltumay (gracias). ¿Cuál corresponde?", ["El propósito es agradecer.", "Gracias es chaltumay."], "chaltumay"),
        W("Idea o sentimiento", "Frase: «Me alegra que me enseñen». ¿Expresa una idea o un sentimiento?", ["Habla de alegría.", "La alegría es un sentimiento."], "Un sentimiento"),
    ],
    mistakes=[
        M("Usar una expresión que no corresponde al propósito.", "Puede confundir.", "Elijo la que calza con lo que quiero decir."),
        M("Hablar de cosas íntimas por obligación.", "Nadie está obligado.", "Uso situaciones inventadas o paso."),
    ],
    R=[
        ex("El propósito es: A) para qué hablo B) con qué lápiz hablo.", "A", "Propósito es el motivo."),
        ex("Para saludar elijo: A) mari mari B) chaltumay.", "A", "La ficha dice que mari mari es saludo."),
        ex("Para agradecer elijo: A) mari mari B) chaltumay.", "B", "La ficha dice que chaltumay es gracias."),
    ],
    C=[
        ex("Verdadero o falso: debo contar emociones íntimas en cualquier situación.", "Falso", "Puedo usar una situación inventada."),
        ex("«El agua es importante para las plantas» expresa: A) una idea B) un sentimiento.", "A", "Es un pensamiento."),
        ex("«Estoy agradecida» expresa: A) un sentimiento B) un lugar.", "A", "Gratitud es un sentimiento."),
    ],
    A=[
        ex("Situación inventada: agradecer a quien me enseñó. ¿Qué sentimiento quiero expresar: gratitud o enojo?", "gratitud", "Agradecer expresa gratitud."),
        arith("Un curso prepara 3 situaciones y cada una tiene 2 frases. ¿Cuántas frases hay?", "3 * 2", "Multiplico situaciones por frases."),
        ex("Situación: saludar a una visita. Expresiones: iorana (saludo en rapa nui), maururu (gracias en rapa nui). ¿Cuál sirve?", "iorana", "Iorana es un saludo."),
    ],
    Z=[
        ex("Eva usa «chaltumay» para saludar al llegar. ¿Qué error cometió: A) usó gracias para saludar B) saludó bien?", "A", "Chaltumay es gracias."),
        ex("Una persona dice que una expresión sirve para cualquier momento. ¿Qué debe hacer: A) preguntar al educador tradicional cuándo se usa B) decirlo igual?", "A", "El uso lo enseña quien conoce la lengua."),
    ],
    D=[
        arith("Hay 5 situaciones y el curso ya practicó 2. ¿Cuántas faltan?", "5 - 2", "Resto las practicadas."),
        ex("Quieres expresar alegría con una expresión de la ficha, pero ninguna dice alegría. ¿Qué haces: A) lo digo en castellano o pregunto B) invento una palabra?", "A", "No debo inventar."),
    ],
    context=[ex("Llega un visitante inventado a tu sala. ¿Qué situación eliges: «saludarlo» o «pedirle que cuente su vida»?", "«saludarlo»", "Es una situación adecuada y sin exposición.")],
    selfcheck=[
        ex("¿Qué cuatro cosas pienso para elegir una situación?", "quién escucha, dónde estoy, para qué hablo y qué quiero expresar", "Son los pasos de la clase."),
        ex("¿Qué expresa «estoy agradecida»?", "un sentimiento", "La gratitud se siente."),
        ex("¿Qué expresión de la ficha uso para agradecer en mapuzugun?", "chaltumay", "Significa gracias en mapuzugun."),
    ],
    task=T(
        "Elige una de estas situaciones inventadas: saludar a una visita, agradecer a quien te enseñó o presentar una palabra de la ficha al curso. Escribe quién escucha, para qué hablas, qué idea o sentimiento quieres expresar y qué expresión de la ficha usarás. Pregunta al educador tradicional cuándo se usa esa expresión.",
        "Situación: agradecer a quien me enseñó. Escucha: el educador. Propósito: agradecer. Sentimiento: gratitud. Expresión: chaltumay. Pregunta: ¿cuándo se dice chaltumay?",
        ["describe quién escucha y el propósito", "elige idea o sentimiento", "elige una expresión de la ficha adecuada"],
        ["situación escrita en el cuaderno"],
        ["usar una expresión que no corresponde", "hablar de cosas íntimas"],
        "Valora que la expresión calza con el propósito; si no, pídele que revise la ficha.",
    ),
    reinforce="Di en voz alta una situación, un propósito y una expresión.",
    extend="Pregunta a una persona de tu casa para qué usa palabras de agradecimiento.",
)

L(
    LR2, 2,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a aprender expresiones desde la fuente, es decir, de quien enseña, y a anotar su significado y su uso. Sirve para decir las expresiones de forma correcta y respetuosa.",
    prior=["Sé elegir una expresión según el propósito.", "Sé que las expresiones validadas no se inventan."],
    explain=[
        "Aprender desde la fuente significa aprender de la persona o la comunidad que conoce la lengua: el educador tradicional, un hablante que enseña o un material que ellos entregan. No aprendo expresiones de un video de origen desconocido ni las invento por parecerme.",
        "Sigo cinco pasos. Pido que me enseñen la expresión. La escucho con atención. La repito con ayuda. Pregunto qué significa y en qué ocasiones se usa. Y anoto la fuente: quién me la enseñó. En mi cuaderno solo escribo la grafía de la ficha y no escribo cómo suena, porque eso me lo muestra la voz de quien enseña.",
        "Si la persona que enseña usa una variante distinta a la de la ficha, aprendo la suya y la respeto. Una expresión aprendida desde la fuente es una expresión cuidada.",
    ],
    vocab=[("fuente", "persona o material de donde aprendo"), ("hablante", "persona que habla una lengua"), ("variante", "forma distinta de decir lo mismo"), ("ocasión", "momento en que se usa una expresión"), ("anotar", "escribir para recordar")],
    worked=[
        W("Elegir la fuente", "Opción A: el educador tradicional. Opción B: un video sin autor. ¿Qué fuente es mejor para aprender una expresión?", ["A es una persona que conoce la lengua.", "B no tiene autor conocido."], "A"),
        W("Anotar la fuente", "Marta aprendió «ko» con el educador tradicional. ¿Qué anota como fuente?", ["Anota quién le enseñó.", "Escribe: el educador tradicional."], "El educador tradicional"),
    ],
    mistakes=[
        M("Aprender una expresión de una fuente desconocida.", "Puede estar mal o ser de otra variante.", "Aprendo de quien conoce la lengua."),
        M("Escribir cómo suena una palabra sin haberla escuchado.", "Puedo inventar una pronunciación.", "Solo anoto la grafía y escucho de quien enseña."),
    ],
    R=[
        ex("Aprender desde la fuente es aprender de: A) quien conoce la lengua B) un rumor.", "A", "La fuente conoce la lengua."),
        ex("Según la ficha, «ko» es: A) agua B) luna.", "A", "La ficha dice agua."),
        ex("Si la persona que enseña usa otra variante, ¿aprendo la suya o la desprecio?", "aprendo la suya", "Respeto la variante de quien enseña."),
    ],
    C=[
        ex("Verdadero o falso: puedo aprender expresiones de un video sin autor conocido.", "Falso", "No sé si es correcto."),
        ex("Pido que me enseñen la expresión. ¿Es el primer paso o el último?", "el primer paso", "Primero pido que me enseñen."),
        ex("¿Qué pregunto además de cómo se dice: qué significa o qué hora es?", "qué significa", "Debo conocer el significado."),
    ],
    A=[
        ex("Ordena los pasos: A) repito con ayuda B) escucho con atención C) pido que me enseñen. Escribe las letras.", "C, B, A", "Pido, escucho y repito."),
        arith("Aprendes 2 expresiones por clase durante 4 clases. ¿Cuántas aprendiste?", "2 * 4", "Multiplico expresiones por clases."),
        ex("Marta anota: «ko — agua — me enseñó el educador tradicional». ¿Qué parte es la fuente?", "me enseñó el educador tradicional", "Dice quién enseñó."),
    ],
    Z=[
        ex("Eva aprendió una expresión con el educador y anotó la fuente. Gaspar la aprendió en un sitio sin autor. ¿Quién la aprendió desde la fuente?", "Eva", "Aprendió de quien conoce la lengua."),
        ex("Un niño dice que ya sabe cómo suena «antü» porque se lo imaginó. ¿Qué debe hacer: A) escucharlo de quien enseña B) quedarse con su idea?", "A", "No debe inventar la pronunciación."),
    ],
    D=[
        arith("De 12 expresiones de una lista, el curso aprendió 7 con el educador. ¿Cuántas faltan?", "12 - 7", "Resto las aprendidas."),
        ex("Una persona anota una expresión pero no su fuente. ¿Qué le falta: A) el nombre de quien la enseñó B) un dibujo?", "A", "La fuente reconoce a quien enseñó."),
    ],
    context=[ex("El educador tradicional te enseña una expresión. ¿Qué haces después de escucharla: «pregunto su significado y anoto la fuente» o «la olvido»?", "«pregunto su significado y anoto la fuente»", "Así aprendo con cuidado.")],
    selfcheck=[
        ex("¿Qué cinco pasos sigo? Nombra el primero.", "pedir que me enseñen", "Es el primer paso."),
        ex("¿Qué anoto además de la expresión?", "su significado y la fuente", "Para recordarla bien."),
        ex("¿Qué hago si la variante es distinta a la ficha?", "aprendo la de quien enseña", "Respeto su variante."),
    ],
    task=T(
        "Elige una palabra de la ficha y simula (con una persona adulta que haga de educador) el proceso: pide que te la enseñen, escúchala, repítela con ayuda, pregunta su significado y anota la fuente. Escribe los cinco pasos con tus palabras y la ficha con la palabra, su significado y la fuente.",
        "1) Pedí que me enseñaran «ko». 2) Escuché. 3) Repetí con ayuda. 4) Pregunté qué significa: agua. 5) Fuente: el educador tradicional.",
        ["sigue los cinco pasos", "anota significado y fuente", "no inventa cómo suena"],
        ["pasos y ficha escritos en el cuaderno"],
        ["no anotar la fuente", "inventar la pronunciación"],
        "Valora que siguió los pasos; si inventó la pronunciación, pídele que pregunte a quien enseña.",
    ),
    reinforce="Di en voz alta los cinco pasos para aprender una expresión.",
    extend="Pregunta a una persona de tu casa cómo aprende ella una palabra nueva.",
)

L(
    LR2, 3,
    materials="Lápiz y hoja. " + FICHA_PAL,
    use="Aprenderé a construir una intervención breve, de pocas oraciones, con saludo, idea, sentimiento y cierre. Sirve para exponer mis ideas de forma ordenada.",
    prior=["Sé elegir una situación comunicativa.", "Sé usar expresiones de la ficha."],
    explain=[
        "Una intervención es lo que digo cuando me toca hablar. Una intervención breve tiene cuatro partes: un saludo, una idea sobre un tema (por ejemplo, el agua o el sol), un sentimiento o comentario y un cierre con agradecimiento. Dura menos de un minuto.",
        "Escribo antes lo que voy a decir. Uso oraciones cortas, de hasta unas diez palabras. Pongo en mi texto una o dos expresiones de la ficha tal como están escritas. Luego ensayo en voz alta con una persona de confianza.",
        "En mi intervención no hablo por un pueblo ni invento expresiones. Digo lo que pienso o siento y, si quiero hablar de la cosmovisión de un pueblo, cito lo que me enseñó el educador tradicional con su fuente.",
    ],
    vocab=[("intervención", "lo que digo cuando me toca hablar"), ("saludo", "palabra para comenzar"), ("cierre", "final con agradecimiento o despedida"), ("ensayar", "practicar antes de presentar"), ("breve", "corta, de poco tiempo")],
    worked=[
        W("Leer una intervención", "Intervención inventada: «Mari mari. El ko es importante para las plantas. Me alegra aprender. Chaltumay». ¿Cuál es la idea?", ["Busco la frase del tema.", "Es «el ko es importante para las plantas»."], "El ko es importante para las plantas"),
        W("Partes de la intervención", "En esa intervención, ¿qué parte es «Chaltumay»?", ["Es lo último que se dice.", "Agradece."], "El cierre"),
    ],
    mistakes=[
        M("Hablar sin ordenar las partes.", "Se pierde el mensaje.", "Uso saludo, idea, sentimiento y cierre."),
        M("Usar una expresión que no está en la ficha.", "No está validada.", "Uso solo las de la ficha."),
    ],
    R=[
        ex("Una intervención breve tiene: A) cuatro partes B) cien partes.", "A", "Tiene cuatro partes."),
        ex("La parte final de una intervención es: A) el cierre B) el saludo.", "A", "El cierre termina."),
        ex("«Mari mari» al inicio es un: A) saludo B) cierre.", "A", "La ficha lo dice."),
    ],
    C=[
        ex("Intervención: «Mari mari. El antü da luz. Me alegra el día. Chaltumay». ¿Qué parte es «Me alegra el día»?", "el sentimiento", "Expresa una emoción."),
        ex("Verdadero o falso: una intervención breve debe durar más de diez minutos.", "Falso", "Es breve: menos de un minuto."),
        ex("¿Se ensaya antes de presentar o se improvisa todo?", "se ensaya", "Ensayar ayuda a decir bien."),
    ],
    A=[
        ex("Ordena una intervención: A) cierro con gracias B) saludo C) digo una idea D) digo un sentimiento. Escribe las letras.", "B, C, D, A", "Saludo, idea, sentimiento y cierre."),
        arith("Tu intervención tiene 4 oraciones de 8 palabras cada una. ¿Cuántas palabras dices?", "4 * 8", "Multiplico oraciones por palabras."),
        ex("Completa: «Mari mari. El ___ es importante para las plantas.» Elige la palabra de la ficha que significa agua.", "ko", "La ficha dice ko es agua."),
    ],
    Z=[
        ex("Dos intervenciones. Eva: «Mari mari. El ko ayuda a las plantas. Me alegra. Chaltumay». Gaspar: «El ko». ¿Cuál es una intervención completa?", "la de Eva", "Tiene las cuatro partes."),
        ex("Una niña dice «todos los pueblos creen lo mismo del agua». ¿Qué error cometió: A) habla por todos los pueblos B) usó un saludo?", "A", "No puede hablar por todos."),
    ],
    D=[
        arith("Tienes 60 segundos y tu intervención dura 45. ¿Cuántos segundos te sobran?", "60 - 45", "Resto lo usado del total."),
        ex("Quieres hablar de un saber de un pueblo. ¿Qué haces: A) cito lo que me enseñó el educador tradicional con su fuente B) lo invento?", "A", "Cito la fuente."),
    ],
    context=[ex("Te piden decir algo breve al curso sobre el agua. ¿Qué haces: «preparo saludo, idea, sentimiento y cierre» o «hablo sin pensar»?", "«preparo saludo, idea, sentimiento y cierre»", "Es una estructura clara.")],
    selfcheck=[
        ex("¿Cuáles son las cuatro partes de una intervención?", "saludo, idea, sentimiento y cierre", "Son las partes de la clase."),
        ex("¿Cuánto dura una intervención breve?", "menos de un minuto", "Es una intervención corta."),
        ex("¿Qué hago antes de presentar?", "ensayar", "Practico en voz alta."),
    ],
    task=T(
        "Escribe una intervención de cuatro oraciones sobre el agua o el sol: saludo, idea, sentimiento y cierre. Incluye una palabra de la ficha. Ensáyala en voz alta con una persona de confianza y cuenta cuántos segundos dura.",
        "Mari mari. El ko ayuda a crecer a las plantas. Me alegra aprender sobre el agua. Chaltumay.",
        ["cuatro oraciones", "una palabra de la ficha", "ensayada en voz alta"],
        ["intervención escrita en el cuaderno"],
        ["no incluir cierre", "inventar expresiones"],
        "Valora que tenga las cuatro partes; si inventó expresiones, pídele que use la ficha.",
    ),
    reinforce="Lee tu intervención en voz alta y mide el tiempo.",
    extend="Presenta tu intervención a una persona de tu casa y pídele que diga qué parte entendió mejor.",
)

L(
    LR2, 4,
    materials="Lápiz y hoja. El diálogo está escrito aquí y es inventado. " + FICHA_PAL,
    use="Aprenderé a interactuar escuchando al otro: esperar mi turno, responder a lo que dice y preguntar si no entiendo. Sirve para conversar con respeto.",
    prior=["Sé hacer una intervención breve.", "Sé que dialogar es hablar por turnos."],
    explain=[
        "Interactuar es conversar con otra persona, hablando y escuchando. Escuchar al otro incluye cuatro acciones: esperar mi turno, mirar a quien habla, responder a lo que dijo y preguntar si no entiendo. Repetir con mis palabras lo que dijo la otra persona se llama parafrasear y muestra que escuché.",
        "Si la otra persona usa una expresión que no conozco, puedo decir: «¿puede enseñarme qué significa?». Si ella usa una variante distinta a la mía, la respeto. Si hay silencios, no los lleno con burlas: dejo que cada uno piense.",
        "Cuando pido apoyo, lo hago con respeto: «¿puede repetir más despacio?». Pedir apoyo es parte de aprender una lengua. Y no necesito hablar perfecto: lo importante es comunicarme con respeto.",
    ],
    vocab=[("interactuar", "conversar hablando y escuchando"), ("parafrasear", "repetir con mis palabras lo que dijo otro"), ("turno", "momento en que me toca hablar"), ("apoyo", "ayuda de otra persona"), ("silencio", "momento en que nadie habla")],
    worked=[
        W("Responder a lo que dijo", "Diálogo inventado. Ana: «El ko es importante para mi huerta». Beto: «Qué bien. ¿Qué plantas riegas?». ¿Beto responde a lo que dijo Ana?", ["Beto menciona la huerta.", "Pregunta algo relacionado."], "Sí"),
        W("Parafrasear", "Ana dijo: «El ko es importante para mi huerta». ¿Qué frase parafrasea?", ["Repite la idea con otras palabras.", "Dice: tu huerta necesita agua."], "«Tu huerta necesita agua»"),
    ],
    mistakes=[
        M("Interrumpir para decir lo mío.", "No escucho.", "Espero mi turno."),
        M("Burlarse cuando alguien dice mal una palabra.", "Aleja a las personas.", "Ofrezco apoyo con respeto."),
    ],
    R=[
        ex("Escuchar incluye: A) esperar mi turno B) hablar siempre primero.", "A", "Esperar el turno es escuchar."),
        ex("Parafrasear es repetir: A) con mis palabras lo que dijo otro B) lo mismo palabra por palabra sin pensar.", "A", "Parafrasear usa mis palabras."),
        ex("Si no entiendo, ¿pregunto o me quedo callado?", "pregunto", "Pedir apoyo ayuda."),
    ],
    C=[
        ex("Verdadero o falso: puedo interrumpir cuando creo que mi idea es mejor.", "Falso", "Debo esperar mi turno."),
        ex("Ana dijo: «Riego mi huerta». ¿Qué frase parafrasea: «Tú cuidas tus plantas con agua» o «Hoy hace calor»?", "«Tú cuidas tus plantas con agua»", "Repite la idea con otras palabras."),
        ex("Una persona usa una expresión que no conozco. ¿Qué digo: «¿qué significa?» o nada?", "«¿qué significa?»", "Pedir significado ayuda a entender."),
    ],
    A=[
        ex("Ordena: A) respondo B) escucho C) espero mi turno. Escribe las letras.", "C, B, A", "Espero, escucho y respondo."),
        arith("En un diálogo cada persona habla 4 veces y son 2 personas. ¿Cuántos turnos hay?", "4 * 2", "Multiplico turnos por personas."),
        ex("Beto dijo: «Mari mari». ¿Qué responde Ana al saludar: «Mari mari» o «Chaltumay»?", "Mari mari", "Es un saludo; chaltumay es gracias."),
    ],
    Z=[
        ex("Eva espera su turno y responde a lo que Ana dijo. Gaspar interrumpe. ¿Quién interactúa escuchando al otro?", "Eva", "Espera y responde."),
        ex("Un compañero se equivoca con una palabra. ¿Qué haces: A) lo ayudo con respeto B) me río?", "A", "El apoyo respeta."),
    ],
    D=[
        arith("Un diálogo tiene 10 turnos. Ya se escribieron 6. ¿Cuántos faltan?", "10 - 6", "Resto los escritos."),
        ex("Una persona dice que no puede hablar con otra porque usa una variante distinta. ¿Qué puede hacer: A) preguntar con respeto y aprender B) no conversar?", "A", "Una variante es parte de la lengua."),
    ],
    context=[ex("En un diálogo, tu compañera dice algo que no entiendes. ¿Qué haces: «le pido que repita más despacio» o «cambio de tema»?", "«le pido que repita más despacio»", "Pedir apoyo es respetuoso.")],
    selfcheck=[
        ex("¿Qué cuatro acciones incluye escuchar?", "esperar mi turno, mirar, responder y preguntar", "Son las acciones de la clase."),
        ex("¿Qué es parafrasear?", "repetir con mis palabras lo que dijo otro", "Muestra que escuché."),
        ex("¿Qué hago si no entiendo?", "pregunto", "Pedir apoyo ayuda a entender."),
    ],
    task=T(
        "Escribe un diálogo de seis turnos entre dos personas inventadas que conversan sobre el agua. Incluye un saludo con una palabra de la ficha, una pregunta para entender mejor, una frase que parafrasee lo que dijo el otro y un agradecimiento. Léelo en voz alta con una persona de confianza.",
        "Ana: «Mari mari». Beto: «Mari mari». Ana: «El ko es importante para mi huerta». Beto: «O sea, tu huerta necesita agua. ¿Qué plantas riegas?». Ana: «Riego lechugas». Beto: «Chaltumay».",
        ["seis turnos", "una pregunta y una paráfrasis", "usa palabras de la ficha"],
        ["diálogo escrito y leído en voz alta"],
        ["no responder a lo que dijo el otro", "inventar expresiones"],
        "Valora que responde a lo que dijo el otro; si no, pídele que relea y conecte.",
    ),
    reinforce="Haz una pregunta a una persona de tu casa y parafrasea su respuesta.",
    extend="Pide a una persona que lea tu diálogo contigo y turnen los papeles.",
)
