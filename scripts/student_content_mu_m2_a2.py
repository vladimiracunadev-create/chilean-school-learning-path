"""Student material for 2.º medio Música, OA 02 (contrastar músicas con características similares según lenguaje musical, procedimientos compositivos, contextos y propósito expresivo).

Las piezas de los ejercicios son descripciones inventadas («de ejemplo»); no se usan obras ni letras con derechos.
"""
from __future__ import annotations

from student_content_mu_m2_a import L
from student_lessons import arith, ex

OA2 = "MU2M OA 02"

# ---------------------------------------------------------------- OA 02 · clase 1 (comparar elementos del lenguaje)
L(
    OA2, 1,
    "Lápiz y papel. Las piezas A y B de cada ejercicio están descritas con sus datos; son de ejemplo.",
    "Aprenderé a contrastar dos músicas parecidas comparando, elemento por elemento, pulso, tempo, melodía, armonía, textura, timbre y forma. Sirve para encontrar qué las hace distintas aunque se parezcan.",
    ["Describo rasgos audibles.", "Sé qué son pulso, tempo, timbre, textura y forma.", "Sé que una melodía puede subir, bajar o repetirse."],
    [
        "Contrastar es poner dos músicas frente a frente y ver en qué se parecen y en qué se diferencian. Es más interesante contrastar músicas que ya se parecen, por ejemplo dos canciones de cuna o dos piezas para bailar, porque obliga a mirar con cuidado. El método es comparar el mismo elemento en ambas: el tempo con el tempo, el timbre con el timbre. Comparar un elemento de una pieza con otro distinto de la otra no sirve.",
        "El tempo se puede medir en pulsos por minuto: 60 pulsos por minuto es un pulso por segundo. La melodía se compara por su dirección (sube, baja, se repite) y por su ámbito, que es la distancia entre su nota más grave y su nota más aguda. La armonía son los acordes que acompañan, es decir, varias notas que suenan juntas. La forma es el orden de las partes.",
        "Una buena tabla de contraste tiene una columna por pieza y una fila por elemento. En cada fila se anota lo que tienen en común o lo que cambia. Al final se resume: «ambas comparten… pero se diferencian sobre todo en…». Así el contraste queda ordenado y se apoya en lo que se oye, no en una impresión general.",
    ],
    [("contrastar", "comparar dos cosas para ver semejanzas y diferencias"), ("ámbito", "distancia entre la nota más grave y la más aguda de una melodía"), ("armonía", "acordes que acompañan la melodía"), ("acorde", "varias notas que suenan a la vez"), ("pulsos por minuto", "medida del tempo: cuántos pulsos hay en un minuto")],
    [
        ("Comparar un mismo elemento", "Pieza A de ejemplo: 60 pulsos por minuto, voz sola. Pieza B de ejemplo: 120 pulsos por minuto, voz sola. Contrasta el tempo y la textura.", ["Tempo: A va a un pulso por segundo y B al doble.", "Textura: las dos tienen voz sola; es una semejanza."], "Tempo distinto: B es el doble de rápida que A. Textura igual: voz sola"),
        ("Comparar la forma", "Pieza A de ejemplo: estrofa, estribillo, estrofa, estribillo. Pieza B de ejemplo: estrofa, estrofa, estribillo. ¿En qué se diferencian en su forma?", ["A alterna estrofa y estribillo dos veces.", "B repite dos estrofas seguidas y termina con un solo estribillo."], "A alterna dos veces; B junta dos estrofas y cierra con un solo estribillo"),
    ],
    [
        ("Comparar elementos distintos, por ejemplo el tempo de una pieza con el timbre de la otra.", "Así no se sabe si hay semejanza o diferencia; hay que comparar el mismo elemento.", "Usa una fila de la tabla por cada elemento y completa las dos columnas."),
        ("Quedarse solo con las diferencias.", "Las semejanzas también explican por qué las músicas pertenecen a una misma familia.", "Anota lo que comparten y lo que cambia."),
    ],
    [
        ex("¿Qué significa contrastar dos músicas? A) Compararlas para ver semejanzas y diferencias. B) Elegir la que más te gusta.", "A", "Contrastar es comparar con criterio."),
        ex("¿Qué se compara en la fila «tempo» de una tabla de contraste? A) La rapidez del pulso de las dos piezas. B) El instrumento de una pieza y la forma de la otra.", "A", "En una fila se compara el mismo elemento."),
        ex("¿Cuántos pulsos por segundo tiene una pieza de 60 pulsos por minuto? A) Uno. B) Dos.", "A", "60 pulsos en 60 segundos es uno por segundo."),
    ],
    [
        ex("Pieza C de ejemplo: la melodía va de la nota más grave a una muy aguda. Pieza D de ejemplo: la melodía usa solo notas cercanas entre sí. ¿Qué elemento se contrasta? A) El ámbito. B) La forma.", "A", "El ámbito es la distancia entre la nota más grave y la más aguda."),
        ex("¿Qué es un acorde? A) Varias notas que suenan a la vez. B) Una melodía que se repite.", "A", "La armonía se construye con acordes."),
        ex("¿Por qué conviene contrastar músicas que ya se parecen? A) Porque obliga a mirar con más cuidado los detalles. B) Porque así se necesitan menos detalles.", "A", "Lo parecido exige precisión."),
    ],
    [
        arith("Una pieza de ejemplo tiene 144 pulsos y va a 72 pulsos por minuto. ¿Cuántos minutos dura?", "144//72", "Se divide el total de pulsos por los pulsos de cada minuto.", " minutos"),
        ex("Pieza E de ejemplo: guitarra y voz. Pieza F de ejemplo: guitarra, voz y bombo. ¿Cuál es la diferencia de timbre? A) F suma un bombo. B) E suma un violín.", "A", "El único timbre añadido es el bombo en F."),
        ex("Pieza G de ejemplo: forma ABA. Pieza H de ejemplo: forma ABAB. ¿Cuántas partes más tiene H? A) Una. B) Dos.", "A", "ABAB tiene cuatro partes y ABA tres: hay una más."),
    ],
    [
        ex("Una tabla dice: «Pieza J: tempo rápido. Pieza K: timbre suave». ¿Por qué no es un buen contraste? A) Porque compara elementos distintos. B) Porque las dos piezas son parecidas.", "A", "Debe comparar tempo con tempo y timbre con timbre."),
        ex("Dos piezas de ejemplo tienen ambas voz sola, pero una va a 60 y otra a 120 pulsos por minuto. ¿Qué afirmación es correcta? A) Se parecen en la textura y difieren en el tempo. B) Se diferencian en todo.", "A", "Se compara elemento por elemento."),
    ],
    [
        arith("Una pieza va a 90 pulsos por minuto y otra a 120. ¿Cuántos pulsos más por minuto tiene la segunda?", "120-90", "Se resta el tempo menor del mayor.", " pulsos"),
        ex("Pieza L de ejemplo: 4 estrofas de 8 pulsos. Pieza M de ejemplo: 3 estrofas de 12 pulsos. ¿Cuál tiene más pulsos en sus estrofas y por cuánto? A) M, por 4. B) L, por 4.", "A", "L tiene 4 × 8 = 32 pulsos y M tiene 3 × 12 = 36: M tiene 4 más."),
    ],
    [ex("Tu curso compara dos canciones de cuna de ejemplo: una con tempo de 50 pulsos por minuto y otra de 80. ¿Qué es más útil preguntar para contrastarlas? A) ¿Qué efecto produce cada tempo en la función de calmar? B) ¿Cuál tiene el nombre más largo?", "A", "Une el rasgo con el propósito.")],
    [
        ex("¿Qué se pide en cada fila de una tabla de contraste? A) Un elemento del lenguaje musical. B) Una opinión.", "A", "Cada fila corresponde a un elemento."),
        ex("¿Verdadero o falso? Es útil anotar también las semejanzas entre las piezas.", "Verdadero", "Las semejanzas muestran la familia común."),
        ex("¿Cuál es la unidad para medir el tempo en esta clase? A) Pulsos por minuto. B) Notas por voz.", "A", "Mide cuántos pulsos caben en un minuto."),
    ],
    (
        "Pieza A de ejemplo: voz y guitarra, 70 pulsos por minuto, forma estrofa-estrofa-estribillo. Pieza B de ejemplo: voz, guitarra y bombo, 100 pulsos por minuto, forma estrofa-estribillo-estrofa-estribillo. Arma una tabla de contraste con cuatro filas (tempo, timbre, textura y forma) y una frase final que empiece «ambas comparten… pero se diferencian en…».",
        "Tempo: A 70 y B 100. Timbre: B suma bombo. Textura: ambas voz con acompañamiento. Forma: A cierra con un solo estribillo y B alterna dos veces. Ambas comparten voz con guitarra, pero se diferencian en tempo, bombo y forma.",
        ["compara el mismo elemento en cada fila", "anota al menos una semejanza", "cierra con la frase pedida"],
        ["tabla de cuatro filas", "frase final"],
        ["comparar elementos distintos", "mencionar solo diferencias"],
        "Reconoce la tabla y pide revisar una fila que mezcle elementos.",
    ),
    "Elige dos canciones parecidas que conozcas y completa tres filas de tabla de contraste.",
    "Agrega la fila «armonía» a una tabla de contraste y explica qué cambiarías en el acompañamiento.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (procedimientos compositivos y contexto)
L(
    OA2, 2,
    "Lápiz y papel. Las piezas están descritas con palabras y son de ejemplo.",
    "Aprenderé a reconocer procedimientos compositivos (repetición, variación, contraste, imitación, ostinato y secuencia) y a relacionarlos con el contexto. Sirve para contrastar cómo dos músicas parecidas fueron construidas.",
    ["Contrasto elementos del lenguaje musical.", "Sé qué es la forma de una pieza.", "Sé qué es una melodía y un motivo."],
    [
        "Los procedimientos compositivos son las técnicas que usa quien compone para construir una música. La repetición vuelve a presentar algo igual. La variación lo repite con cambios. El contraste presenta algo distinto. La imitación hace que una voz repita lo que acaba de decir otra, como en un canon. El ostinato es un motivo breve que se repite sin cesar. La secuencia repite un motivo más agudo o más grave que antes.",
        "Dos músicas pueden parecerse en lo que dicen y diferenciarse en cómo se construyen. Una canción puede repetir tal cual el estribillo, mientras otra lo repite con variaciones cada vez. Los contextos también influyen: una música hecha para cantar de memoria tiende a repetir mucho, porque la repetición ayuda a recordar; una pieza escrita para un concierto puede variar más porque la partitura guarda los cambios.",
        "Para contrastar, primero se identifica el procedimiento con evidencia audible: «el motivo vuelve a aparecer en la segunda voz». Después se compara cuál usa cada pieza y cuánto. Por último se relaciona con el contexto y el propósito: «repite mucho porque se canta en grupo». Así el contraste muestra no solo qué hay, sino por qué la música está construida de ese modo.",
    ],
    [("repetición", "volver a presentar algo igual"), ("variación", "repetir algo con cambios"), ("imitación", "una voz repite lo que dijo otra"), ("ostinato", "motivo breve que se repite sin parar"), ("secuencia", "repetición de un motivo en otra altura"), ("canon", "forma en que varias voces cantan la misma melodía entrando una después de otra"), ("compás", "grupo de pulsos que se repite con regularidad")],
    [
        ("Identificar el procedimiento", "Pieza de ejemplo: un bajo toca cuatro notas que se repiten durante toda la pieza, mientras la voz canta distintas melodías encima. ¿Qué procedimiento sostiene el bajo?", ["Son cuatro notas que vuelven una y otra vez.", "Eso es un motivo breve que se repite sin parar."], "Un ostinato"),
        ("Relacionar procedimiento y contexto", "Una canción de ejemplo, aprendida de memoria en grupo, repite el estribillo cuatro veces sin cambios. ¿Qué relación hay con el contexto?", ["Se canta de memoria en grupo.", "La repetición exacta ayuda a recordar y a que todos canten juntos."], "La repetición favorece que el grupo la recuerde y la cante junta"),
    ],
    [
        ("Llamar «variación» a cualquier repetición.", "La repetición es igual; la variación trae cambios.", "Pregunta si lo que vuelve es idéntico o cambió algo."),
        ("Pensar que más repetición siempre es peor.", "La repetición cumple un papel según el propósito, por ejemplo ayudar a recordar.", "Relaciona cuánto se repite con el contexto y el propósito."),
    ],
    [
        ex("Un motivo breve que se repite sin cesar bajo una melodía es: A) un ostinato. B) una secuencia.", "A", "El ostinato es la repetición continua."),
        ex("Una voz repite lo que acaba de cantar otra voz. ¿Qué procedimiento es? A) La imitación. B) El contraste.", "A", "Imitar es repetir lo dicho por otra voz."),
        ex("Un estribillo vuelve con algunas notas cambiadas. ¿Qué procedimiento es? A) La repetición exacta. B) La variación.", "B", "Hay cambios al repetir."),
    ],
    [
        ex("¿En qué se diferencian repetición y variación? A) La variación repite con cambios. B) La repetición cambia todo.", "A", "La repetición mantiene lo igual."),
        ex("¿Qué es una secuencia? A) Repetir un motivo en otra altura, más agudo o más grave. B) Repetir un motivo en la misma altura pero con otro ritmo.", "A", "Es la repetición cambiando de altura."),
        ex("¿Por qué una música de tradición oral tiende a repetir bastante? A) Porque la repetición ayuda a recordarla. B) Porque quienes la cantan no saben variar.", "A", "En la tradición oral no hay partitura que recuerde la música; la repetición ayuda a memorizarla."),
    ],
    [
        ex("Pieza A de ejemplo: una melodía de tres notas vuelve más aguda dos veces seguidas. Pieza B de ejemplo: la misma melodía vuelve igual cada vez. ¿Cuál usa secuencia? A) La pieza A. B) La pieza B.", "A", "La secuencia cambia de altura."),
        ex("Dos voces cantan la misma melodía, la segunda entra dos compases después. ¿Qué procedimiento es? A) Imitación (como un canon). B) Contraste.", "A", "Una voz imita a la otra con retraso."),
        ex("Una pieza presenta una parte tranquila y luego otra rápida con otro ritmo. ¿Qué procedimiento usa? A) Contraste. B) Ostinato.", "A", "Presenta algo distinto."),
    ],
    [
        ex("Pieza C de ejemplo es un canto de trabajo con una respuesta fija del grupo que se repite exacta cada vez. Pieza D de ejemplo es una obra de concierto en la que la respuesta del grupo cambia algo cada vez. ¿Qué relación con el contexto es razonable? A) C repite exacto para que todos respondan igual al trabajar, y D varía para sostener el interés de quien escucha. B) C varía cada vez para entretener y D repite exacto para que todos respondan igual.", "A", "El uso explica cuánto se repite o varía."),
        ex("Una estudiante dice: «La pieza E es mala porque repite mucho». ¿Qué falta en su juicio? A) Relacionar la repetición con el propósito de la pieza. B) Contar los instrumentos.", "A", "La repetición puede cumplir un papel."),
    ],
    [
        arith("Un ostinato de ejemplo dura 2 compases y se repite sin cambios en una pieza de 24 compases. ¿Cuántas veces suena completo?", "24//2", "Se divide el total de compases por la duración del ostinato.", " veces"),
        ex("Una pieza de ejemplo tiene 4 estrofas con la misma melodía pero con acompañamiento distinto en cada una. ¿Cómo se puede describir? A) Repetición de la melodía con variación del acompañamiento. B) Contraste total entre estrofas.", "A", "Se mantiene la melodía y cambia el acompañamiento."),
    ],
    [ex("En un taller se compara una ronda infantil de ejemplo con una pieza de concierto de ejemplo. ¿Qué pregunta ayuda a contrastar su construcción? A) ¿Qué procedimientos usan y cuánto repiten o varían cada uno? B) ¿Cuál dura más en la agenda?", "A", "Apunta a los procedimientos y al contraste.")],
    [
        ex("¿Qué procedimiento mantiene una base repetida mientras la melodía cambia? A) Ostinato. B) Imitación.", "A", "La base repetida es el ostinato."),
        ex("¿Verdadero o falso? Una variación es una repetición idéntica.", "Falso", "La variación trae cambios."),
        ex("¿Qué relación puede haber entre repetición y contexto? A) Se repite para ayudar a recordar. B) Se repite para ocultar la forma.", "A", "En música de grupo ayuda a la memoria."),
    ],
    (
        "Pieza A de ejemplo: canción de cuna con la misma melodía en tres estrofas, sin cambios, y un motivo de dos notas que se repite en el acompañamiento. Pieza B de ejemplo: canción de concierto con una melodía que aparece tres veces, cada vez con adornos distintos, y una segunda voz que imita. Escribe: a) dos procedimientos de A, b) dos de B, c) una frase que los relacione con el contexto.",
        "a) Repetición exacta y ostinato. b) Variación e imitación. c) A repite exacto porque se canta para calmar y se aprende fácil; B varía y usa imitación porque se escribió para ser escuchada con atención.",
        ["identifica procedimientos con evidencia", "separa lo exacto de lo variado", "relaciona con el contexto"],
        ["a), b) y c)", "mención de repetición o variación"],
        ["llamar variación a toda repetición", "juzgar solo por la cantidad de repetición"],
        "Reconoce los procedimientos y pide dar una razón de contexto para cada uno.",
    ),
    "Busca una canción con estribillo y anota si el estribillo se repite exacto o con variación.",
    "Inventa un ostinato de cuatro golpes con palmas y combínalo con una melodía hablada.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (propósito expresivo)
L(
    OA2, 3,
    "Lápiz y papel. Las piezas son de ejemplo y se describen en cada ejercicio.",
    "Aprenderé a relacionar los recursos musicales con el propósito expresivo: qué quiere comunicar o provocar una música. Sirve para explicar por qué dos músicas parecidas producen efectos distintos.",
    ["Reconozco procedimientos compositivos.", "Conozco tempo, dinámica y timbre.", "Sé que una música tiene un propósito."],
    [
        "El propósito expresivo es lo que una música busca comunicar o provocar: calma, alegría, tensión, nostalgia, fuerza, homenaje. Los recursos que usa tienen que ver con ese propósito. Un tempo lento y una dinámica suave suelen asociarse con calma. Un pulso marcado y un tempo rápido, con energía. Una melodía en el registro agudo suele sentirse más ligera; en el registro grave, más pesada.",
        "Estas asociaciones son tendencias, no reglas. Una pieza en modo menor, que a menudo se asocia con tristeza, puede sonar enérgica si el tempo es rápido y el ritmo es marcado. Un tempo lento puede expresar solemnidad en lugar de calma. Por eso hay que escuchar el conjunto de recursos y el contexto, y no decidir por un solo rasgo. Dos músicas con los mismos instrumentos pueden expresar cosas muy distintas.",
        "Para contrastar el propósito expresivo se hace una cadena de tres pasos: qué recurso se oye, qué efecto produce y para qué propósito sirve. Por ejemplo: «el silencio breve antes del estribillo genera expectativa, y eso prepara la entrada fuerte de todo el grupo». Si la cadena no se sostiene con lo que se oye, hay que revisar la interpretación.",
    ],
    [("propósito expresivo", "lo que una música busca comunicar o provocar"), ("registro", "zona de sonidos graves, medios o agudos"), ("modo menor", "forma de organizar las notas que a menudo se asocia con ambientes serios o melancólicos"), ("tendencia", "relación frecuente que no siempre se cumple"), ("expectativa", "espera de lo que vendrá"), ("clímax", "momento de mayor intensidad de una pieza")],
    [
        ("Cadena recurso-efecto-propósito", "Una pieza de ejemplo hace un silencio breve antes de cada estribillo. ¿Qué efecto produce y para qué sirve?", ["Recurso: un silencio breve.", "Efecto: genera expectativa.", "Propósito: preparar la entrada fuerte del estribillo."], "Genera expectativa y prepara la entrada fuerte del estribillo"),
        ("Una tendencia no es una regla", "Una pieza de ejemplo está en modo menor, va rápida y con pulso marcado. Alguien dice que suena triste. ¿Es forzoso?", ["El modo menor suele asociarse con ambientes serios.", "El tempo rápido y el pulso marcado pueden darle energía."], "No: el conjunto de recursos puede expresar energía y no tristeza"),
    ],
    [
        ("Decidir el propósito expresivo mirando un solo rasgo.", "Un rasgo aislado puede engañar; importan el conjunto y el contexto.", "Escucha tempo, dinámica, timbre y contexto antes de concluir."),
        ("Creer que lento siempre significa triste.", "Un tempo lento puede expresar calma, solemnidad o ternura.", "Pregunta qué efecto produce junto con otros recursos."),
    ],
    [
        ex("¿Qué es el propósito expresivo? A) Lo que una música busca comunicar o provocar. B) El nombre del instrumento principal.", "A", "Es el fin expresivo."),
        ex("¿Qué recurso suele asociarse con calma? A) Tempo lento y dinámica suave. B) Pulso muy marcado y volumen fuerte.", "A", "Es una tendencia habitual."),
        ex("Una melodía en el registro grave suele sentirse A) más pesada. B) más ligera.", "A", "El registro grave pesa más. Es una tendencia, no una regla."),
    ],
    [
        ex("¿Por qué las asociaciones entre recursos y emociones son tendencias y no reglas? A) Porque el efecto depende del conjunto de recursos y del contexto. B) Porque la música lenta nunca expresa nada.", "A", "El efecto surge de varias decisiones juntas."),
        ex("¿Qué tres pasos tiene la cadena de contraste expresivo? A) Recurso, efecto y propósito. B) Autor, año y país.", "A", "Es el método de la clase."),
        ex("Un silencio breve antes de una entrada fuerte suele producir A) expectativa. B) confusión del pulso.", "A", "La pausa prepara la entrada."),
    ],
    [
        ex("Pieza A de ejemplo: tempo lento, dinámica suave, registro agudo, voz sola. Pieza B de ejemplo: tempo lento, dinámica fuerte, registro grave, coro y tambor. Ambas son lentas. ¿Qué diferencia expresiva es razonable? A) A suena delicada y B suena solemne o imponente. B) Las dos expresan exactamente lo mismo.", "A", "La dinámica, el registro y el timbre cambian el efecto."),
        ex("Una pieza de ejemplo cambia de dinámica suave a fuerte en el estribillo. ¿Qué efecto produce? A) Intensifica la emoción del estribillo. B) Oculta la melodía.", "A", "El aumento de dinámica realza el estribillo."),
        ex("Una música de homenaje usa tempo lento, voz coral y silencio final. ¿Qué propósito expresivo es coherente? A) Solemnidad y recuerdo. B) Energía festiva.", "A", "Los recursos apoyan un homenaje."),
    ],
    [
        ex("Una estudiante afirma: «Esta pieza es triste porque está en modo menor». ¿Qué falta para fundamentarlo? A) Relacionar el modo con el tempo, la dinámica, el timbre y el contexto. B) Cambiar el título.", "A", "El modo menor es una tendencia."),
        ex("Dos piezas de ejemplo tienen el mismo tempo y los mismos instrumentos, pero una se usa para dormir y otra para una marcha. ¿Qué elemento explica la diferencia de propósito? A) El contexto de uso y los demás recursos como la dinámica. B) Solo el tempo, que decide por sí solo el propósito.", "A", "El propósito depende del uso y del conjunto de recursos."),
    ],
    [
        ex("Cadena incompleta: «recurso: la melodía sube cada vez más agudo; efecto: ___; propósito: crecer hacia el clímax». ¿Qué efecto completa mejor? A) Aumenta la tensión. B) Se vuelve monótona.", "A", "La subida gradual de altura suele aumentar la tensión."),
        arith("Una pieza de ejemplo dura 5 minutos: 2 minutos suaves, 1 de tensión creciente y el resto fuerte. ¿Cuántos minutos son fuertes?", "5-2-1", "Se restan los minutos suaves y de tensión al total.", " minutos"),
    ],
    [ex("Tu curso elige la música para cerrar una actividad solidaria. ¿Qué pregunta aplica lo aprendido? A) ¿Qué propósito expresivo buscamos y qué recursos lo logran? B) ¿Cuál tiene más repeticiones?", "A", "Une propósito y recursos.")],
    [
        ex("¿Verdadero o falso? Un solo rasgo basta para decidir el propósito expresivo.", "Falso", "Hay que escuchar el conjunto."),
        ex("Un pulso marcado y un tempo rápido suelen asociarse con A) energía. B) calma profunda.", "A", "Es una tendencia habitual."),
        ex("¿Qué recurso aumenta la expectativa antes de una entrada? A) Un silencio breve. B) Una repetición exacta de diez veces.", "A", "El silencio prepara la entrada."),
    ],
    (
        "Pieza A de ejemplo: coro de voces graves, tempo lento, dinámica creciente, silencio antes del último acorde. Pieza B de ejemplo: voz y flauta agudas, tempo lento, dinámica suave todo el tiempo. Ambas se usan en ceremonias de recuerdo. Escribe dos cadenas «recurso, efecto, propósito», una para cada pieza, y una frase que diga en qué difieren expresivamente.",
        "A: dinámica creciente, genera intensidad, para expresar fuerza solemne. B: dinámica suave y registro agudo, genera delicadeza, para expresar ternura. Ambas son lentas, pero A es más imponente y B más íntima.",
        ["usa las tres partes de la cadena", "apoya cada efecto en un recurso audible", "señala una diferencia expresiva"],
        ["dos cadenas", "frase final"],
        ["decidir por un solo rasgo", "afirmar el efecto sin recurso"],
        "Reconoce las cadenas y pide revisar una en la que el efecto no se sigue del recurso.",
    ),
    "Elige una canción y anota un recurso, el efecto que produce y su propósito.",
    "Busca dos piezas con el mismo tempo y explica qué otro recurso cambia su efecto.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (redactar un contraste completo)
L(
    OA2, 4,
    "Lápiz y papel. Las piezas A y B de cada ejercicio vienen descritas; son de ejemplo.",
    "Aprenderé a redactar un contraste musical completo que une lenguaje, procedimientos, contexto y propósito expresivo. Sirve para presentar una comparación clara, ordenada y fundamentada.",
    ["Comparo elementos del lenguaje.", "Reconozco procedimientos compositivos.", "Relaciono recursos y propósito expresivo."],
    [
        "Un contraste completo tiene cuatro partes. Primero, la presentación: qué piezas se comparan y por qué se parecen. Segundo, las semejanzas: dos o tres rasgos comunes. Tercero, las diferencias: elemento por elemento, con el procedimiento compositivo y el contexto que las explican. Cuarto, la conclusión: cómo esas diferencias llevan a propósitos expresivos distintos o a una misma intención por caminos diferentes.",
        "Los conectores ayudan a ordenar: «ambas», «también», «en cambio», «mientras que», «a diferencia de», «por eso», «esto se debe a». Cada diferencia debe nombrar el elemento y las dos piezas, por ejemplo: «mientras que A mantiene un ostinato, B varía su acompañamiento». Una frase como «son muy distintas» sin dato no contrasta nada.",
        "Antes de entregar conviene revisar tres cosas: que se compare el mismo elemento en ambas piezas, que cada afirmación se pueda comprobar escuchando y que la conclusión relacione con el propósito y no repita las diferencias. Una buena conclusión responde: ¿qué logra cada pieza con sus decisiones?",
    ],
    [("conector", "palabra o expresión que une ideas"), ("semejanza", "rasgo que dos piezas comparten"), ("diferencia", "rasgo que cambia entre dos piezas"), ("conclusión", "cierre que resume y relaciona las ideas"), ("evidencia", "dato audible que apoya una afirmación")],
    [
        ("Completar con un conector", "Completa: «A mantiene un ostinato, ____ B varía su acompañamiento.» ¿Qué conector expresa contraste?", ["Se oponen dos rasgos.", "El conector que une opuestos es «mientras que»."], "Mientras que"),
        ("Ordenar las partes del contraste", "Un texto tiene: conclusión, semejanzas, presentación y diferencias. ¿En qué orden va?", ["Se parte por presentar las piezas.", "Luego semejanzas, diferencias y conclusión."], "Presentación, semejanzas, diferencias, conclusión"),
    ],
    [
        ("Escribir «son muy distintas» sin dato.", "No dice en qué ni cómo, y no se puede comprobar.", "Nombra el elemento, el rasgo de cada pieza y la evidencia."),
        ("Repetir en la conclusión las diferencias palabra por palabra.", "La conclusión debe relacionar las diferencias con el propósito, no copiarlas.", "Responde qué logra cada pieza con sus decisiones."),
    ],
    [
        ex("¿Cuál es la primera parte de un contraste completo? A) La presentación de las piezas. B) La conclusión.", "A", "Se parte presentando lo que se compara."),
        ex("¿Qué conector expresa oposición? A) «Mientras que». B) «Además».", "A", "Opone dos rasgos distintos."),
        ex("¿Qué debe comparar cada diferencia? A) El mismo elemento en ambas piezas. B) Un elemento en una y otro en la otra.", "A", "Es la base del contraste."),
    ],
    [
        ex("¿Qué función cumple la conclusión? A) Relacionar las diferencias con el propósito expresivo. B) Repetir la presentación.", "A", "Cierra con el sentido de la comparación."),
        ex("Un texto dice: «A usa ostinato; B también». ¿Qué falta? A) Contrastar algo, por ejemplo cómo lo usan. B) Que sea más largo y tenga más adjetivos.", "A", "Dice solo una semejanza vaga."),
        ex("¿Por qué conviene que cada afirmación pueda comprobarse escuchando? A) Para que el contraste se apoye en evidencia. B) Para que sea más corto.", "A", "La evidencia da fuerza al contraste."),
    ],
    [
        ex("Elige la frase que contrasta bien. A) «A va a 60 pulsos por minuto y B a 100, por eso A resulta más tranquila.» B) «A es lenta y B también es otra cosa.»", "A", "Da el dato y lo relaciona con el efecto."),
        ex("Completa: «Ambas piezas usan voz con guitarra; ____, A tiene tempo lento y B tempo rápido.» A) en cambio B) por eso", "A", "Introduce la diferencia."),
        ex("Una comparación de ejemplo dice: «A y B tienen formas parecidas, pero en B el estribillo cambia de dinámica». ¿Qué parte del contraste es la que sigue a «pero»? A) Una diferencia. B) La conclusión.", "A", "Es una diferencia concreta."),
    ],
    [
        ex("Estudiante 1: «A y B son muy distintas.» Estudiante 2: «A repite exacto el estribillo y B lo varía con adornos, por eso A se aprende más rápido.» ¿Quién contrasta con fundamento? A) El 1. B) El 2.", "B", "El 2 nombra el rasgo y lo conecta con el efecto."),
        ex("Un contraste dice: «A es de tradición oral y B de tradición escrita, por eso A tiene variantes y B se toca igual en cada lugar». ¿Qué parte es la conclusión del razonamiento? A) «Por eso A tiene variantes y B se toca igual.» B) «A es de tradición oral.»", "A", "Relaciona la tradición con el efecto."),
    ],
    [
        ex("¿Qué orden de cuatro frases forma un contraste completo? A) Presentación, semejanza, diferencia y conclusión. B) Conclusión, diferencia, semejanza y presentación.", "A", "El orden lógico parte por presentar."),
        arith("Un contraste de ejemplo debe tener 1 presentación, 2 semejanzas, 3 diferencias y 1 conclusión. ¿Cuántas ideas tiene en total?", "1+2+3+1", "Se suman las ideas de cada parte.", " ideas"),
    ],
    [ex("En una feria de música escolar se compara dos canciones de homenaje. ¿Qué texto es el más útil para las visitas? A) Uno que presenta las piezas, nombra semejanzas y diferencias con evidencia y cierra con el propósito. B) Uno que solo dice cuál le gusta más.", "A", "Cumple las cuatro partes.")],
    [
        ex("¿Verdadero o falso? Una buena conclusión relaciona las diferencias con el propósito.", "Verdadero", "Da sentido a la comparación."),
        ex("¿Qué palabra conecta una semejanza? A) «Ambas». B) «A diferencia de».", "A", "Introduce lo común."),
        ex("¿Qué se revisa antes de entregar? A) Que se compare el mismo elemento. B) Que sea muy largo.", "A", "Es parte de la revisión de la clase."),
    ],
    (
        "Pieza A de ejemplo: canción de cuna con voz sola, 55 pulsos por minuto, melodía repetida tres veces sin cambios. Pieza B de ejemplo: canción de cuna con voz y guitarra, 70 pulsos por minuto, melodía repetida tres veces con cambios en el acompañamiento. Escribe un contraste de cuatro frases: presentación, una semejanza, una diferencia con evidencia y una conclusión sobre el propósito de calmar.",
        "Comparo dos canciones de cuna de ejemplo. Ambas repiten tres veces la melodía. Mientras que A va a 55 pulsos y solo con voz, B va a 70 y suma guitarra con cambios. Las dos buscan calmar, pero A lo logra por sencillez y B por un acompañamiento que se renueva.",
        ["incluye las cuatro partes", "compara el mismo elemento", "usa conectores y evidencia"],
        ["texto de cuatro frases", "al menos un conector"],
        ["no mencionar evidencia", "repetir la presentación al final"],
        "Reconoce el texto y pide agregar un conector que oponga las diferencias.",
    ),
    "Redacta un contraste de cuatro frases entre dos canciones que te gusten.",
    "Intercambia tu contraste con una compañera o compañero y revisen juntos que cada afirmación pueda comprobarse.",
)
