"""Música 3.º y 4.º medio FG: OAC-05 (juicios estéticos musicales fundamentados). Obras y argumentos de ejemplo, inventados; sin audio real."""
from __future__ import annotations

from fg_musi_common import build

O5 = "FG-MUSI-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (obra de ejemplo «Faro», inventada). Una voz y un piano tocan una melodía de ocho compases que se repite tres veces; en cada repetición después de la primera, el piano agrega una nota nueva en el acompañamiento. "
     "El tempo es 66 pulsos por minuto y el volumen sube poco a poco hasta la tercera repetición, que termina con una nota larga de la voz. Propósito declarado: transmitir esperanza. "
     "Tres frases de estudiantes: (1) «No me gusta el piano.» (2) «Las repeticiones con un cambio pequeño cada vez dan sensación de avance.» (3) «La música actual es mejor.»")
build(
    O5, 1, F,
    use="Aprenderé a distinguir un gusto personal de un juicio estético fundamentado, y a usar criterios estéticos (coherencia, expresividad, dominio técnico, originalidad y claridad de la forma) para valorar una obra.",
    prior=["Analizo propósito, evidencia y efecto.", "Separo rasgo audible, contexto y opinión.", "Conozco criterios del lenguaje musical."],
    explain=[
        "Un gusto personal dice si algo te agrada o no («no me gusta el piano»). Un juicio estético valora una obra con razones: afirma algo sobre su valor y lo apoya en criterios. Los criterios estéticos más usados son: coherencia (los recursos sirven al propósito), expresividad (la obra comunica con claridad lo que busca), dominio técnico (la ejecución y la producción están controladas), originalidad (aporta algo propio o una combinación interesante) y claridad de la forma (las partes se ordenan de manera comprensible).",
        "Un juicio fundamentado tiene la estructura: afirmación + criterio + evidencia audible. Por ejemplo: «La obra es coherente porque las repeticiones con un cambio pequeño, junto con el volumen que sube, sostienen la sensación de avance que busca». Un gusto puede coexistir con un juicio, pero no lo reemplaza: puedes valorar una obra que no te gusta si reconoces sus méritos con criterios.",
        "Los juicios no son verdades absolutas, pero tampoco todos valen lo mismo: un juicio con criterio y evidencia se puede discutir y comprobar; un gusto sin razones, no.",
    ],
    vocab=[("juicio estético", "valoración de una obra apoyada en criterios y evidencia"), ("gusto personal", "preferencia propia, sin necesidad de razones"), ("coherencia", "relación lógica entre los recursos y el propósito"), ("originalidad", "aporte propio o combinación interesante de recursos"), ("expresividad", "claridad con que la obra comunica lo que busca")],
    worked=[
        ("Distinguir gusto de juicio", "¿Es un juicio estético fundamentado la frase (2) de la ficha?", ["Afirma algo sobre la obra: que las repeticiones dan sensación de avance.", "Se apoya en una evidencia audible: el cambio pequeño en cada repetición.", "Tiene un criterio implícito: coherencia con el propósito."], "Sí, porque tiene afirmación y evidencia audible"),
        ("Contar las notas agregadas", "El piano agrega una nota nueva en cada repetición después de la primera. ¿Cuántas notas nuevas agregó al terminar?", ["Hay 3 repeticiones.", "Se agrega una nota en la 2.ª y otra en la 3.ª: 3 − 1 = 2."], "2 notas nuevas"),
    ],
    mistakes=[("Creer que «no me gusta» es un juicio sobre la calidad.", "Es una preferencia: no dice nada comprobable sobre la obra.", "Agrega un criterio y una evidencia, aunque la obra no te guste."),
              ("Pensar que cualquier juicio vale lo mismo.", "Un juicio con criterios y evidencia se puede discutir y comprobar; un gusto sin razones no.", "Pide siempre el criterio y la evidencia.")],
    T=[
        ('abc', '{F} ¿Cuál de las tres frases es un gusto personal?', 'La (1): «No me gusta el piano», porque solo dice si agrada', 'La (2): sobre repeticiones', 'Ninguna: todas son juicios', 'La (1) solo dice si agrada o no; la (2) cita evidencia.'),
        ('abc', '{F} ¿Qué criterio estético usa la frase (2)?', 'Coherencia entre recursos y propósito', 'Originalidad de la obra', 'Dominio técnico del piano', 'Relaciona repeticiones y avance con lo que busca.'),
        ('abc', '{F} La frase (3) dice «La música actual es mejor». ¿Qué le falta?', 'Un criterio y una evidencia audible que la sostengan', 'Un título más largo', 'Nombrar la obra en cada oración', 'Compara épocas de la música sin criterios ni evidencia.'),
        ('abc', '¿Qué tiene un juicio estético fundamentado?', 'Afirmación, criterio y evidencia audible', 'Solo una opinión sincera', 'Solo el nombre del autor', 'Esa estructura permite comprobar el juicio con la escucha.'),
        ('abc', '{F} ¿Cuántas repeticiones de la melodía hay?', '3', '2', '8', 'Se repite tres veces; los ocho son compases por repetición.'),
        ('=', '{F} ¿Cuántos compases suenan en total, sumando las tres repeticiones?', '8*3', 'Cada repetición tiene 8 compases y son 3 repeticiones.', ' compases'),
        ('abc', '{F} ¿Qué rasgo audible puede sostener el criterio de claridad de la forma?', 'Tres repeticiones de ocho compases, con una nota nueva del piano en la segunda y en la tercera', 'Que a la crítica le guste el piano', 'Que el tempo sea 66 de manera casual', 'Muestra un orden de partes comprensible.'),
        ('abc', 'Una estudiante escribe: «No me gusta, pero reconozco que el volumen que sube poco a poco ayuda a sostener la esperanza buscada». ¿Qué muestra?', 'Que se puede separar el gusto del juicio', 'Que su opinión no tiene valor', 'Que no entendió la obra', 'Reconoce un mérito aunque la obra no le agrade.'),
        ('abc', '{F} El propósito declarado es la esperanza. ¿Qué decisión de la obra apoya ese propósito?', 'El crecimiento gradual del volumen hasta una nota larga final', 'Un tempo de 200 pulsos por minuto', 'La ausencia total de cambios', 'El crecimiento gradual del volumen sugiere ascenso y esperanza.'),
        ('abc', '¿Qué significa el criterio de originalidad?', 'Que aporta algo propio o una combinación interesante', 'Que nadie más haya usado un piano', 'Que dura más que otras obras', 'No exige inventar algo nunca visto, sino un aporte propio.'),
        ('abc', 'Dos estudiantes discrepan sobre la misma obra y ambos citan criterios y evidencia. ¿Qué se concluye?', 'Es posible discrepar con juicios igualmente fundamentados', 'Uno de los dos no sabe nada de música', 'No se puede juzgar la obra', 'Los criterios permiten debatir sin descalificar.'),
        ('abc', '{F} ¿Qué conviene hacer si no te agrada el piano pero quieres juzgar la obra?', 'Valorar los criterios y reconocer el gusto como aparte', 'Evitar el juicio y solo decir que no te gusta', 'Pedirle a otra persona que lo haga', 'Se pueden separar el gusto y el juicio.'),
        ('abc', '{F} ¿Qué expresa la frase «Faro es la mejor obra del mundo»?', 'Una exageración sin criterio ni evidencia', 'Un juicio fundamentado', 'Un dato técnico de la grabación', 'Un superlativo sin razones no es un juicio fundamentado.'),
    ],
    ctx=('abc', 'En un taller, un estudiante dice que la obra «Faro» es mala porque «no es su estilo». ¿Cómo se puede transformar su comentario en un juicio?', 'Indicar qué criterio no se cumple y qué evidencia lo muestra', 'Agregar que a su grupo tampoco le gusta', 'Repetir la frase con más fuerza', 'Un juicio necesita criterio y evidencia, no solo preferencia.'),
    sc=[
        ('¿Qué es un juicio estético?', 'Una valoración con criterios y evidencia', 'No basta con decir si agrada.'),
        ('¿Cuántos compases suenan en 4 repeticiones de 8 compases?', '32', 'Se multiplican 4 repeticiones por 8 compases.'),
        ('abc', 'La coherencia, como criterio, mide', 'si los recursos sirven al propósito', 'si la obra es famosa', 'si la obra es larga', 'Revisa la relación entre decisiones y propósito.'),
    ],
    op=("Con la {F} escribe un juicio estético fundamentado de «Faro» con la estructura afirmación + criterio + evidencia audible, y aparte una línea de gusto personal rotulada.",
        "Faro es coherente con su propósito de esperanza porque el volumen crece poco a poco hasta una nota larga final, y cada repetición suma una nota nueva. Gusto personal: prefiero la voz sola, pero reconozco el mérito de la obra.",
        ["afirmación", "criterio", "evidencia audible"], ["juicio y línea de gusto"], ["mezclar gusto y juicio", "no citar evidencia"],
        "Reconoce el juicio y pide separar el gusto en otra línea."),
    reinforce="Escribe un juicio de una canción que no te guste, usando un criterio y una evidencia.",
    extend="Elige dos criterios y explica por qué dos personas podrían valorar distinto la misma obra.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (dos obras de ejemplo con el mismo propósito declarado: transmitir energía para una carrera escolar). Obra M: percusión con pulso marcado a 150 pulsos por minuto, voces que repiten una frase corta y un crescendo al final. "
     "Obra N: un solo violonchelo con notas largas y muy suaves a 50 pulsos por minuto, sin cambios de volumen. Ambas están bien ejecutadas: pulso estable y afinación correcta.")
build(
    O5, 2, F,
    use="Aprenderé a valorar una obra considerando si sus recursos de producción y elementos del lenguaje musical sirven a su propósito expresivo, y a separar la calidad técnica de la coherencia con el propósito.",
    prior=["Distingo gusto de juicio estético.", "Conozco los criterios: coherencia, expresividad, dominio técnico, originalidad y forma.", "Explico recursos por su efecto."],
    explain=[
        "Al valorar una obra conviene preguntar primero para qué fue hecha. El propósito expresivo permite medir la coherencia: si los recursos y los elementos del lenguaje musical (tempo, timbre, dinámica, forma) ayudan a lograr lo que la obra busca. Una obra puede estar muy bien ejecutada y ser poco coherente con su propósito, o al revés. Por eso son criterios distintos y se juzgan por separado.",
        "En la ficha, ambas obras están bien ejecutadas: tienen pulso estable y afinación correcta, es decir, buen dominio técnico. Pero el propósito es transmitir energía para una carrera. La obra M usa un pulso marcado, tempo rápido y crescendo, lo que apoya la energía. La obra N usa notas largas y suaves a 50 pulsos por minuto, lo que sugiere calma; es coherente con otros propósitos, no con este.",
        "Esto no significa que N sea una mala obra, sino que su coherencia con ese propósito es baja. Un juicio completo reconoce los méritos que sí tiene y explica qué criterio no se cumple.",
    ],
    vocab=[("coherencia con el propósito", "grado en que los recursos ayudan a lograr lo que la obra busca"), ("dominio técnico", "control de la ejecución y de la producción"), ("ejecución", "manera de tocar o cantar la obra"), ("mérito", "cualidad valiosa que se puede reconocer")],
    worked=[
        ("Valorar la coherencia", "Para una carrera escolar se usa la obra M. ¿Es coherente? Justifica con dos rasgos.", ["Propósito: energía.", "Pulso marcado a 150 y crescendo final.", "Ambos impulsan el movimiento."], "Sí, por el pulso marcado a 150 y el crescendo final"),
        ("Separar criterios", "La obra N está bien ejecutada pero no es coherente con el propósito de la carrera. ¿Cómo se informa?", ["Dominio técnico: alto.", "Coherencia con este propósito: baja.", "Se juzga cada criterio por separado."], "Buen dominio técnico, baja coherencia con este propósito"),
    ],
    mistakes=[("Concluir que una obra es mala porque no cumple un propósito ajeno.", "Puede ser coherente con su propio fin.", "Valora la obra según el propósito que declara o muestra."),
              ("Mezclar calidad de ejecución y coherencia en un solo puntaje.", "Un criterio puede ser alto y el otro bajo.", "Valora cada criterio con su evidencia.")],
    T=[
        ('abc', '{F} ¿Qué obra es más coherente con el propósito de energía para una carrera?', 'La obra M, por su pulso marcado y su tempo rápido', 'La obra N, porque está muy bien tocada', 'Las dos por igual, porque están bien ejecutadas', 'M tiene pulso marcado, tempo rápido y crescendo.'),
        ('abc', '{F} ¿Qué rasgo de N va en contra de la energía?', 'Notas largas y muy suaves a 50 pulsos por minuto', 'Su afinación correcta', 'Su ejecución con pulso estable', 'Esos rasgos sugieren calma, no movimiento.'),
        ('abc', '{F} ¿Qué se puede decir del dominio técnico de ambas?', 'Es bueno en las dos, porque ambas tienen pulso estable y afinación', 'Es bueno solo en M, porque es la más movida', 'Es malo en las dos, porque suenan muy distintas', 'La ficha indica que ambas están bien ejecutadas.'),
        ('=', '{F} ¿Cuántos pulsos más por minuto tiene M que N?', '150-50', 'Se resta el tempo de N del de M.', ' pulsos por minuto'),
        ('abc', 'Una estudiante dice que N es mala obra. ¿Qué respuesta de juicio fundamentado corresponde?', 'N es poco coherente con ese propósito, aunque tenga buen dominio técnico', 'N no puede juzgarse porque es violonchelo', 'N es la mejor porque es suave', 'Se separan la coherencia y la calidad técnica.'),
        ('abc', '{F} Si el propósito cambiara a «acompañar una siesta», ¿qué obra sería más coherente?', 'La obra N, que es suave y lenta, y sirve para descansar', 'La obra M, que tiene un pulso marcado', 'Ninguna de las dos, porque ambas son enérgicas', 'N es suave y lenta, adecuada para el descanso.'),
        ('abc', 'El dominio técnico se refiere a', 'el control de la ejecución y la producción', 'qué tan famosa es la obra', 'cuántos instrumentos usa', 'Incluye pulso estable, afinación y producción limpia.'),
        ('abc', '{F} ¿Qué evidencia de M apoya el criterio de expresividad?', 'Voces que repiten una frase corta con pulso marcado', 'Una sola nota larga', 'Silencio durante la mitad de la obra', 'La repetición con pulso comunica la energía con claridad.'),
        ('abc', '{F} Un estudiante propone agregar un crescendo a N. ¿Qué efecto tendría?', 'Acercaría un poco la obra a la energía, sin cambiar el tempo', 'Haría que dejara de ser violonchelo', 'Reduciría la afinación', 'Un crescendo suma intensidad, aunque el tempo lento seguiría limitando.'),
        ('abc', 'Un juicio completo sobre una obra', 'reconoce méritos y explica qué criterio no se cumple', 'solo enumera defectos', 'solo menciona méritos', 'Un juicio equilibrado considera ambos lados.'),
        ('abc', '{F} ¿Qué dato de la ficha sirve para comprobar que M es rápida?', 'Los 150 pulsos por minuto, un dato que se mide', 'Sus voces, que repiten una frase corta', 'Su final con crescendo, que sube el volumen', 'El tempo se mide en pulsos por minuto.'),
        ('abc', 'Dos obras pueden estar bien ejecutadas y tener distinta coherencia. Esto muestra que', 'dominio técnico y coherencia son criterios distintos', 'la coherencia no existe', 'todas las obras son iguales', 'Cada criterio mide un aspecto diferente de la obra.'),
        ('abc', '{F} ¿Cuántas veces más rápido es M que N?', '3 veces', '2 veces', '5 veces', '150 dividido en 50 es 3.'),
    ],
    ctx=('abc', 'Un grupo debe elegir música para animar el último minuto de una carrera de relevos. Tienen M y N. Alguien propone N «porque está muy bien tocada». ¿Qué argumento corresponde?', 'La buena ejecución no basta: M es más coherente con el propósito', 'N, porque la ejecución es lo único que importa', 'Ninguna, porque la música no sirve para carreras', 'Hay que mirar coherencia además de técnica.'),
    sc=[
        ('¿Qué mide la coherencia con el propósito?', 'Si los recursos ayudan a lograr lo que la obra busca', 'Relaciona los recursos de la obra con su fin.'),
        ('¿Cuántos pulsos suenan en 2 minutos a 150 pulsos por minuto?', '300', 'Se multiplican 150 pulsos por 2 minutos.'),
        ('abc', 'Una obra con buena ejecución puede', 'tener baja coherencia con un propósito', 'no tener ningún mérito', 'ser incomprensible', 'Son criterios independientes y pueden dar resultados distintos.'),
    ],
    op=("Con la {F} escribe un juicio de la obra N con tres partes: un mérito con evidencia, un criterio que no cumple para el propósito de la carrera con evidencia, y una situación donde N sí sería coherente.",
        "Mérito: buen dominio técnico, con pulso estable y afinación correcta. Límite: tempo de 50 y volumen constante no transmiten energía. Sería coherente para acompañar un momento de descanso.",
        ["mérito con evidencia", "criterio no cumplido", "otra situación"], ["juicio de tres partes"], ["olvidar el mérito", "no citar evidencia"],
        "Reconoce el juicio y pide citar el dato exacto de la ficha."),
    reinforce="Elige una canción y explica para qué propósito sería coherente y para cuál no.",
    extend="Propone un cambio a la obra N que la acerque al propósito de energía sin perder su carácter.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (tres piezas de ejemplo con su contexto). Pieza X: una canción de cuna cantada por una persona sin acompañamiento, con una melodía simple que se repite; se usa para dormir a un bebé. "
     "Pieza Y: una música de baile para una fiesta, con tambor y guitarra, a 120 pulsos por minuto; se toca en reuniones. "
     "Pieza Z: una obra de concierto para una sala silenciosa, con muchas capas y cambios de tempo, pensada para escucharla sentado y en silencio.")
build(
    O5, 3, F,
    use="Aprenderé a incluir aspectos contextuales (función, lugar, público, medios disponibles y época) al juzgar una obra, y a evitar prejuicios como valorar solo lo conocido o lo complejo.",
    prior=["Valoro con criterios y propósito.", "Sé que cada música tiene una función.", "Separo gusto y juicio."],
    explain=[
        "Los aspectos contextuales son las circunstancias en que una obra nace y se usa: su función (para qué sirve), el lugar y el público al que va dirigida, los medios disponibles y la época. Conocerlos evita juzgar una obra con una vara que no le corresponde. Una canción de cuna no necesita muchas capas ni un tempo vivo, porque su función es calmar; una música de baile necesita un pulso claro porque su función es mover el cuerpo.",
        "Hay prejuicios frecuentes al valorar: creer que lo complejo es siempre mejor que lo simple, que lo antiguo es mejor que lo reciente o al revés, que lo tradicional es mejor que lo popular, o que lo comercial no tiene valor. Un juicio fundamentado revisa si la obra cumple bien su función y su propósito, con criterios claros, sin rechazar una música por su origen.",
        "El contexto ayuda a entender, pero no reemplaza el análisis: también se mira la evidencia audible. Cuando falta información de contexto, se dice con claridad y se evita suponer.",
    ],
    vocab=[("contexto", "circunstancias en que una obra se crea y se usa"), ("función", "para qué se usa una música"), ("público", "personas a las que se dirige la obra"), ("prejuicio", "juicio previo sin examinar la evidencia"), ("época", "período en que se crea una obra")],
    worked=[
        ("Juzgar según la función", "¿Por qué la melodía simple y repetida de la pieza X es un acierto y no un defecto?", ["Su función es calmar a un bebé.", "La repetición simple y la voz sola favorecen la calma.", "Más capas o cambios de tempo podrían inquietar."], "Porque su función pide calma y repetición simple"),
        ("Detectar un prejuicio", "Una estudiante dice: «La pieza Y es menos valiosa porque es solo para bailar». ¿Qué prejuicio muestra?", ["Considera que la función de bailar tiene menos valor.", "No examina si la pieza cumple bien su función."], "Prejuicio contra lo popular o funcional"),
    ],
    mistakes=[("Pensar que lo complejo es siempre mejor.", "La complejidad no mide el logro del propósito.", "Valora si la obra cumple bien su función con sus recursos."),
              ("Usar el contexto como excusa para no analizar.", "Con solo decir «es de tradición» no se justifica un juicio.", "Combina el contexto con evidencia audible.")],
    T=[
        ('abc', '{F} ¿Cuál es la función de la pieza X?', 'Dormir a un bebé, que pide calma y repetición', 'Animar un baile con un pulso claro', 'Escuchar en una sala, en silencio y con atención', 'La función aparece indicada de forma explícita en la ficha.'),
        ('abc', '{F} ¿Qué rasgo de Y se relaciona con su función de baile?', 'El pulso claro a 120 pulsos por minuto', 'La voz sola sin acompañamiento', 'Las capas y cambios de tempo', 'Un pulso claro permite seguir la música con el cuerpo.'),
        ('abc', '{F} ¿Por qué no sería un buen juicio decir que X es peor que Z porque tiene menos capas?', 'Porque la cantidad de capas no mide el logro de su función', 'Porque X tiene más capas que Z', 'Porque las dos piezas tienen igual número de capas', 'Cada pieza tiene una función distinta.'),
        ('abc', '¿Qué es un prejuicio al valorar música?', 'Un juicio previo que no examina la evidencia', 'Un juicio basado en tres rasgos audibles', 'Una opinión razonada', 'Se decide antes de escuchar o analizar.'),
        ('abc', '{F} ¿Qué dato de contexto de Z se relaciona con sus cambios de tempo y muchas capas?', 'Está pensada para escucharse con atención en silencio', 'Es música de baile para reuniones y fiestas', 'Se usa para dormir a un bebé con una voz sola', 'El público que escucha en silencio permite detalles finos.'),
        ('abc', 'Alguien dice: «Esa música es de moda, así que no vale». ¿Qué prejuicio muestra?', 'Rechazar algo por ser actual o popular', 'Valorar algo por ser muy complejo', 'Usar criterios musicales', 'No examina la obra; descarta por su origen.'),
        ('abc', '{F} ¿Qué medios de producción usa Y?', 'Tambor y guitarra', 'Solo voz', 'Orquesta completa', 'La ficha nombra esos dos medios de producción.'),
        ('abc', '{F} Si Y se tocara en una sala silenciosa para escucharse sentado, ¿qué cambiaría en su valoración?', 'Se evaluaría si sirve a ese nuevo contexto, que no es el de baile', 'Se valoraría igual porque el contexto no importa', 'Perdería todo valor para siempre', 'Cambiar el contexto cambia lo que se espera de la obra.'),
        ('abc', '¿Cuál es una forma correcta de usar el contexto?', 'Unirlo a evidencia audible en el juicio', 'Reemplazar el análisis con él', 'Ignorarlo siempre', 'El contexto ayuda a entender, no reemplaza el análisis.'),
        ('=', '{F} A 120 pulsos por minuto, ¿cuántos pulsos suenan en 2 minutos de baile?', '120*2', 'Se multiplican los pulsos por minuto por los minutos.', ' pulsos'),
        ('abc', '{F} ¿Qué pieza tiene una melodía simple que se repite?', 'La pieza X, que es una canción de cuna cantada sin acompañamiento', 'La pieza Y, que es música para bailar', 'La pieza Z, que es una obra de concierto', 'Se describe en la ficha como canción de cuna.'),
        ('abc', 'Si no conoces el contexto de una obra, ¿qué corresponde hacer?', 'Decir que se desconoce y evitar suponerlo', 'Inventar un contexto verosímil', 'Descartar la obra', 'No se debe suponer lo que no se sabe.'),
        ('abc', '{F} Un estudiante dice que Z es la mejor porque es la más compleja. ¿Qué error comete?', 'Confunde complejidad con logro del propósito', 'Olvida que Z tiene una melodía simple', 'No cuenta los pulsos', 'La complejidad no mide por sí sola el valor.'),
    ],
    ctx=('abc', 'En un acto escolar quieren incluir la pieza Z como música de fondo mientras la gente conversa y come. ¿Qué observación de contexto es la más razonable?', 'Z fue pensada para escucharla en silencio, así que quizás no funcione allí', 'Z siempre funciona igual en cualquier lugar', 'Z debe quitarse de todo programa', 'El lugar y el público influyen en cómo funciona la obra.'),
    sc=[
        ('¿Qué incluye el contexto de una obra?', 'Función, lugar, público, medios y época', 'Son circunstancias que rodean a la obra.'),
        ('¿Cuántos pulsos suenan en 3 minutos a 120 pulsos por minuto?', '360', 'Se multiplica 120 por 3 minutos.'),
        ('abc', 'Juzgar sin examinar la obra por su origen es', 'un prejuicio, porque se decide sin analizar', 'un criterio estético', 'una evidencia', 'Rechaza por origen, no por análisis.'),
    ],
    op=("Con la {F} escribe un juicio breve de la pieza que elijas que incluya su función, un aspecto contextual, una evidencia audible y una frase que evite un prejuicio.",
        "La pieza X cumple bien su función de calmar: la voz sola y la melodía simple repetida favorecen la calma. Su contexto es una canción de cuna. No es menos valiosa que Z por tener menos capas.",
        ["función", "contexto", "evidencia"], ["juicio breve"], ["comparar con una vara ajena", "no citar evidencia"],
        "Reconoce el juicio y pide mostrar qué rasgo cumple la función."),
    reinforce="Elige una música de tu casa y anota su función, su público y un rasgo que la sirve.",
    extend="Elige dos músicas con funciones distintas y explica cómo cambiarían los criterios para juzgarlas.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (obra de ejemplo «Puente» y un argumento modelo). «Puente»: un grupo con guitarra, bajo, batería y voz; 100 pulsos por minuto; estrofas con texto que cuenta un viaje, un estribillo que se repite cuatro veces y, en la última, una parte en la que se suman dos voces. "
     "Argumento modelo: Afirmación: «Puente logra transmitir el entusiasmo de partir». Criterio: coherencia. Evidencia: el estribillo se repite cuatro veces y en la última se suman dos voces. Contexto: está pensada para tocarse en vivo ante un público que puede cantar. "
     "Contraargumento posible: «Las repeticiones pueden cansar». Respuesta: «Cada vez que se repite, suma una voz más, así que no suena igual».")
build(
    O5, 4, F,
    use="Aprenderé a construir un argumento estético completo (afirmación, criterio, evidencia, contexto y respuesta a un contraargumento) para defender un juicio sobre una obra.",
    prior=["Distingo gusto de juicio.", "Considero el propósito y el contexto.", "Cito evidencia audible."],
    explain=[
        "Argumentar un juicio estético es defender con razones una valoración. Un argumento completo tiene cinco partes: la afirmación (lo que sostienes), el criterio (desde qué aspecto valoras: coherencia, expresividad, dominio técnico, originalidad o forma), la evidencia audible (lo que se oye y se puede comprobar), el contexto (función, público, lugar) y, si es posible, una respuesta a un contraargumento, es decir, una objeción razonable que otra persona podría hacer.",
        "Considerar un contraargumento fortalece el juicio: muestra que miraste la obra desde más de un ángulo. Por ejemplo, alguien podría objetar que las repeticiones cansan; la respuesta puede indicar que cada repetición suma una voz y por eso no suena igual. Si la objeción tiene razón, un buen argumento la reconoce y ajusta la afirmación: «Puente es coherente, aunque sus repeticiones podrían resultar largas para un oyente que escucha en silencio».",
        "Escribe en frases claras y evita palabras absolutas como «siempre» o «nadie». Una afirmación demasiado fuerte es difícil de defender.",
    ],
    vocab=[("afirmación", "lo que se sostiene sobre la obra"), ("contraargumento", "objeción razonable al juicio propio"), ("evidencia audible", "dato que se comprueba escuchando"), ("matizar", "ajustar una afirmación para hacerla más precisa"), ("objeción", "razón en contra de una afirmación")],
    worked=[
        ("Reconocer las partes", "En el argumento modelo, ¿cuál es la evidencia audible?", ["Buscamos lo que se oye y se comprueba.", "El estribillo se repite cuatro veces.", "En la última repetición se suman dos voces."], "El estribillo repetido cuatro veces y la suma de dos voces en la última"),
        ("Contar las repeticiones", "El estribillo se repite 4 veces y dura 8 compases cada vez. ¿Cuántos compases de estribillo hay en total?", ["4 repeticiones × 8 compases.", "4 × 8 = 32."], "32 compases"),
    ],
    mistakes=[("Defender el juicio sin considerar objeciones.", "El argumento parece frágil ante cualquier crítica.", "Escribe una objeción posible y respóndela."),
              ("Usar palabras absolutas como «nadie» o «siempre».", "Basta un caso en contra para derrumbar la afirmación.", "Matiza con «en general», «probablemente» o «en este contexto».")],
    T=[
        ('abc', '{F} ¿Cuál es la afirmación del argumento modelo?', 'Puente logra transmitir el entusiasmo de partir', 'El estribillo se repite cuatro veces', 'Está pensada para tocarse en vivo', 'La afirmación es lo que se sostiene; lo demás son evidencia y contexto.'),
        ('abc', '{F} ¿Qué criterio usa el argumento modelo?', 'Coherencia con el propósito', 'Originalidad', 'Dominio técnico', 'El argumento se refiere a coherencia con el propósito.'),
        ('abc', '{F} ¿Qué dato de contexto aparece en el argumento modelo?', 'Está pensada para tocarse en vivo ante un público que puede cantar', 'Se graba a volumen bajo', 'Tiene 100 pulsos por minuto', 'La función y el público son parte del contexto.'),
        ('abc', '{F} ¿Qué es la objeción «Las repeticiones pueden cansar»?', 'Un contraargumento, es decir, una razón en contra', 'Una evidencia audible', 'El criterio estético', 'Es una razón en contra de la valoración.'),
        ('=', '{F} El estribillo se repite 4 veces y dura 6 compases cada vez. ¿Cuántos compases de estribillo hay?', '4*6', 'Se multiplican las repeticiones por los compases de cada una.', ' compases'),
        ('abc', 'Un estudiante escribe: «Nadie podría criticar esta obra». ¿Qué error comete?', 'Usa una afirmación absoluta difícil de defender', 'Usa demasiados criterios', 'Cita evidencia audible', 'Una sola objeción razonable la derrumba.'),
        ('abc', '{F} ¿Cómo se responde con evidencia a «las repeticiones cansan»?', 'Mostrando que cada repetición suma una voz y no suena igual', 'Diciendo que a mucha gente le gusta', 'Aceptando que la obra es mala', 'Se responde con un rasgo audible que cambia en cada repetición.'),
        ('abc', '{F} Una compañera argumenta que Puente es poco original. ¿Qué evidencia necesita para sostenerlo?', 'Comparar rasgos con otra obra y mostrar que son muy similares', 'Decir que le recuerda otra canción', 'Afirmar que otros también piensan así', 'La originalidad se discute con rasgos comparables.'),
        ('abc', '¿Para qué sirve incluir un contraargumento?', 'Para mostrar que se miró la obra desde más de un ángulo', 'Para evitar tener que citar evidencia', 'Para que el juicio sea más largo', 'Fortalece el juicio y lo hace más justo.'),
        ('abc', '{F} ¿Qué es matizar la afirmación?', 'Ajustarla para hacerla más precisa, por ejemplo según el contexto', 'Cambiarla por su opuesto', 'Agregar una opinión sin razones', 'Se agrega una condición o un límite.'),
        ('abc', '{F} Si Puente se escuchara en silencio en una sala, ¿qué matiz es razonable agregar?', 'Que las repeticiones podrían resultar largas en ese contexto', 'Que dejaría de tener estribillo', 'Que no se podría juzgar', 'El contexto cambia cómo se perciben las repeticiones.'),
        ('abc', 'Un argumento tiene afirmación, evidencia y contexto, pero no criterio. ¿Qué falta?', 'Decir desde qué aspecto se valora, como coherencia o forma', 'Un título para la obra', 'Una mayor cantidad de opiniones', 'El criterio explica qué se está valorando.'),
        ('abc', '{F} ¿Cuántas repeticiones del estribillo suenan antes de que se sumen las dos voces?', '3', '4', '2', 'El estribillo se repite 4 veces y las voces se suman en la última, así que antes suenan 3.'),
    ],
    ctx=('abc', 'Un estudiante afirma que una obra es original, pero solo dice «se nota». ¿Qué le conviene agregar para argumentar mejor?', 'Un criterio y una evidencia audible que lo muestren', 'Un comentario sobre la fama del grupo', 'Otra opinión igual de fuerte', 'La afirmación necesita criterio y evidencia.'),
    sc=[
        ('¿Qué partes tiene un argumento estético completo?', 'Afirmación, criterio, evidencia, contexto y respuesta a una objeción', 'Cada parte del argumento aporta razones distintas.'),
        ('¿Cuántos compases son 5 repeticiones de 4 compases?', '20', 'Se multiplican 5 por 4 compases.'),
        ('abc', 'Un contraargumento es', 'una objeción razonable que otra persona podría hacer a tu juicio', 'una evidencia que confirma todo', 'una forma de criticar a la obra', 'Pone a prueba el juicio y lo vuelve más justo.'),
    ],
    op=("Con la {F} escribe un argumento estético de «Puente» sobre un criterio distinto a coherencia (por ejemplo expresividad o forma) con afirmación, evidencia, contexto y una objeción respondida.",
        "Puente tiene una forma clara porque alterna estrofas que cuentan el viaje con un estribillo repetido cuatro veces, y en la última se suman dos voces. Contexto: para tocarse en vivo. Objeción: puede ser predecible. Respuesta: la suma de voces lo renueva al final.",
        ["afirmación y criterio", "evidencia y contexto", "objeción respondida"], ["argumento breve"], ["no incluir objeción", "afirmación absoluta"],
        "Reconoce el argumento y pide matizar la afirmación según el contexto."),
    reinforce="Escribe una afirmación sobre una canción y dos evidencias que la apoyen.",
    extend="Intercambia tu argumento con una compañera, que escribirá una objeción; respóndela por escrito.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (cuatro argumentos de ejemplo sobre una pieza «Ola», inventada, que tiene voz y percusión y un final que se apaga de a poco). "
     "Argumento 1: «Es buena porque es la más escuchada del curso.» Argumento 2: «Mi profesor dice que es excelente, así que lo es.» Argumento 3: «Todo lo que usa percusión es movido, así que Ola es movida.» "
     "Argumento 4: «El final que se apaga de a poco sostiene la sensación de despedida que busca; la percusión suave lo acompaña.»")
build(
    O5, 5, F,
    use="Aprenderé a revisar y ajustar un juicio estético: detectar razonamientos débiles (apelar a la popularidad o a la autoridad, generalizar, confundir gusto con verdad) y reformularlos con criterio y evidencia.",
    prior=["Construyo un argumento con afirmación, criterio, evidencia y contexto.", "Incluyo una objeción.", "Evito palabras absolutas."],
    explain=[
        "Revisar un juicio es buscar razonamientos débiles. Los más comunes son: apelar a la popularidad («es buena porque todos la escuchan»), apelar a la autoridad («lo dijo alguien importante, así que es cierto»), generalizar sin evidencia («todo lo que tiene percusión es movido»), y confundir gusto con verdad («me gusta, entonces es buena»). Ninguno es una razón estética suficiente: la popularidad y la autoridad pueden orientar, pero no reemplazan la evidencia audible.",
        "Para ajustar un argumento débil se hace una pregunta: ¿qué se oye que respalde la afirmación? Con esa respuesta se reformula: se cambia la razón débil por un criterio y una evidencia. La popularidad se puede usar como dato de contexto, por ejemplo para entender el público, pero no como fundamento de calidad. La opinión de una persona experta es útil si se comprueba con lo que se oye.",
        "Al ajustar, también se revisan los datos (tempo, número de partes) y el lenguaje (sin absolutos). Un juicio mejora cuando cada frase puede comprobarse escuchando.",
    ],
    vocab=[("apelar a la popularidad", "defender algo solo porque mucha gente lo prefiere"), ("apelar a la autoridad", "defender algo solo porque lo dijo una persona importante"), ("generalizar", "extender una regla a todos los casos sin comprobarlos"), ("razonamiento débil", "argumento que no se apoya en evidencia suficiente"), ("reformular", "volver a escribir una idea con mejores razones")],
    worked=[
        ("Detectar el error", "¿Qué razonamiento débil tiene el argumento 1 de la ficha?", ["Dice que es buena porque la escuchan mucho.", "Eso es popularidad, no una evidencia musical."], "Apelar a la popularidad"),
        ("Contar los argumentos débiles", "En la ficha, los argumentos 1, 2 y 3 tienen razonamientos débiles y el 4 no. ¿Cuántos argumentos son sólidos?", ["Hay 4 argumentos.", "3 son débiles: 4 − 3 = 1."], "1 argumento sólido"),
    ],
    mistakes=[("Creer que la opinión de una persona experta no se puede cuestionar.", "Se puede comprobar con lo que se oye.", "Úsala como pista y verifica con evidencia."),
              ("Defender un juicio con «a todos les gusta».", "La popularidad no mide calidad.", "Reemplázala por un criterio y una evidencia audible.")],
    T=[
        ('abc', '{F} ¿Qué razonamiento débil tiene el argumento 2?', 'Apela a la autoridad: se apoya en lo que dijo otra persona', 'Apela a la popularidad', 'Generaliza sin evidencia', 'Se apoya en lo que dijo otra persona, no en lo que se oye.'),
        ('abc', '{F} ¿Qué razonamiento débil tiene el argumento 3?', 'Generaliza sin evidencia, pues extiende una regla a todos', 'Apela a la autoridad, porque cita a otra persona', 'Confunde gusto con verdad, porque habla de preferencia', 'Extiende una regla a todos los casos.'),
        ('abc', '{F} ¿Cuál es el argumento más sólido?', 'El 4, porque cita un rasgo audible y su efecto en el propósito', 'El 1, porque es el más escuchado', 'El 2, porque lo dice un profesor', 'El 4 enlaza evidencia, efecto y propósito.'),
        ('abc', '{F} ¿Qué evidencia audible cita el argumento 4?', 'Un final que se apaga de a poco y percusión suave', 'Que es la más escuchada', 'Que lo dijo un profesor', 'Es lo que se oye y se puede comprobar.'),
        ('abc', 'Una estudiante dice: «Me gusta, entonces es buena». ¿Qué error comete?', 'Confunde gusto con verdad', 'Apela a la autoridad', 'Generaliza una regla', 'Presenta su preferencia como prueba de calidad.'),
        ('abc', '{F} ¿Cómo se puede reformular el argumento 1 para que sea más sólido?', 'Citar un rasgo de Ola y su efecto, y dejar la popularidad como contexto', 'Repetir que todos la escuchan, pero con más datos', 'Decir que nadie la critica y que gusta a todo el curso', 'La popularidad no es fundamento; el rasgo sí.'),
        ('abc', '{F} El argumento 3 puede corregirse así:', '«Ola usa percusión suave, así que su movimiento es leve»', '«Ola es movida porque todos dicen que sí»', '«Toda música sin percusión es mala»', 'Se basa en un rasgo de la obra, no en una regla general.'),
        ('abc', '¿Cuándo es útil la opinión de una persona experta?', 'Como una pista que se comprueba con lo que se oye en la obra', 'Como prueba definitiva, sin escuchar', 'Nunca, porque quien sabe puede equivocarse', 'Una pista se verifica con evidencia.'),
        ('abc', '{F} ¿Cuántos argumentos de la ficha se apoyan en la autoridad o en la popularidad?', '2', '1', '3', 'El argumento 1 apela a la popularidad y el 2 a la autoridad.'),
        ('abc', 'Para ajustar un argumento débil, la mejor pregunta es', '¿qué se oye que respalde mi afirmación?', '¿cuánta gente opina igual?', '¿quién lo dijo antes?', 'Lleva el juicio a la evidencia audible.'),
        ('abc', '{F} Un compañero dice que el final que se apaga demuestra que Ola es «perfecta». ¿Qué conviene matizar?', 'Evitar absolutos y hablar de coherencia con el propósito de despedida', 'Agregar que nadie podría criticarla', 'Afirmar que es la mejor de todas', 'Un matiz evita afirmaciones imposibles de defender.'),
        ('abc', 'La popularidad de una obra puede usarse como', 'dato de contexto, no como fundamento de calidad', 'criterio de dominio técnico', 'prueba de que es original', 'Informa sobre el público, no sobre la calidad.'),
        ('=', '{F} Ola se escucha 3 veces seguidas y cada vez dura 4 minutos. ¿Cuántos minutos son?', '3*4', 'Se multiplican las veces por los minutos de cada una.', ' minutos'),
    ],
    ctx=('abc', 'Para defender una canción, un estudiante escribe: «Es excelente porque ganó un concurso». ¿Qué ajuste mejora el juicio?', 'Agregar un criterio y una evidencia audible, y dejar el premio como contexto', 'Agregar más premios que respalden que es excelente', 'Quitar el premio y no decir nada más sobre la canción', 'El premio es contexto; el juicio necesita rasgos.'),
    sc=[
        ('¿Qué es apelar a la popularidad?', 'Defender algo solo porque mucha gente lo prefiere', 'No muestra rasgos de la obra.'),
        ('¿Cuántos minutos son 3 audiciones de 5 minutos?', '15', 'Se multiplican 3 por 5 minutos.'),
        ('abc', 'Para reformular un argumento débil hay que', 'reemplazar la razón débil por criterio y evidencia', 'agregar más frases de gusto', 'repetirlo con más fuerza', 'Así el juicio se puede comprobar.'),
    ],
    op=("Con la {F} elige uno de los argumentos débiles (1, 2 o 3), nombra su razonamiento débil y reescríbelo con criterio, evidencia audible y una frase de contexto, sin absolutos.",
        "Argumento 2 (autoridad). Reescritura: «Ola es expresiva porque el final se apaga de a poco y la percusión suave lo acompaña, lo que sugiere despedida. Contexto: un profesor la recomendó, pero eso solo me motivó a escucharla con atención».",
        ["nombra el error", "criterio y evidencia", "sin absolutos"], ["argumento reescrito"], ["repetir la misma razón débil", "usar absolutos"],
        "Reconoce la reescritura y pide comprobar que cada frase pueda verificarse escuchando."),
    reinforce="Busca un argumento débil en una conversación sobre música y reescríbelo con evidencia.",
    extend="Prepara un breve debate de dos minutos entre dos juicios distintos sobre una misma obra, con criterios y evidencia.",
)
