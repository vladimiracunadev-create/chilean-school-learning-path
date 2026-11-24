"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 3 (parte 4): OAD-12, elaborar y comunicar explicaciones sobre los conflictos internos en Chile en la segunda mitad del siglo XX, con multicausalidad, multidimensionalidad y apertura a distintas perspectivas. Todas las fuentes son textos de ejemplo inventados y se leen en papel."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y cuaderno. Todas las fuentes de esta clase son extractos inventados «de ejemplo», escritos en cada ejercicio: no son citas de personas reales y no necesitas internet, mapas ni libros. "
             "Este tema es sensible: muchas personas vivieron esos años y hay familias afectadas. Nadie te pide contar su experiencia ni la de su familia; trabaja con los casos del cuaderno y, si algo te incomoda, puedes pausar o pedir apoyo. "
             "Se trabaja con respeto, con hechos comprobados y sin justificar la violación de los derechos humanos.")
build = make_build(MATERIALS)

O = "EPJA-HGCS-NM1-OAD-12"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Tres textos inventados sobre el plebiscito de 1988. "
      "Texto A: «En 1988 se votó en un plebiscito; ganó la opción “No” y se convocó a elecciones para 1989.» "
      "Texto B: «Fue lo mejor que le pasó al país.» "
      "Texto C: «El plebiscito de 1988 se realizó porque la Constitución de 1980 lo contemplaba. El resultado cambió el rumbo porque una amplia coalición de partidos hizo campaña por el “No”, organizaciones sociales y de derechos humanos movilizaron a la ciudadanía y el proceso fue seguido con atención desde otros países.»")
build(
    O, 1, F1,
    use="Hoy distingo un relato, una opinión y una explicación, y reconozco qué necesita una explicación sobre un conflicto interno de Chile.",
    prior=["Distingo hecho de opinión.", "Conozco el orden de los hechos entre 1973 y 1990.", "Sé que un hecho tiene varias causas."],
    explain=[
        "Explicar es mucho más que contar. Un relato cuenta qué pasó y en qué orden. Una opinión dice qué piensa alguien sobre lo ocurrido. Una explicación responde por qué pasó: indica causas, las ordena y las apoya con evidencia. Tú explicas todos los días: cuando cuentas por qué llegaste tarde, das causas.",
        "En historia, una buena explicación sobre un conflicto interno reúne varias causas de distintas dimensiones (políticas, económicas, sociales, internacionales), incluye perspectivas diversas y se apoya en fuentes. Por ejemplo, el plebiscito de 1988 se explica por una Constitución que lo preveía, por una oposición unida, por la movilización social y por la atención internacional.",
        "Explicar también tiene un compromiso ético: decir de dónde sale cada dato, no inventar y no justificar violaciones a los derechos humanos. Con honestidad y responsabilidad, una explicación sirve para entender, no para ganar una discusión.",
    ],
    vocab=[("relato", "texto que cuenta qué ocurrió y en qué orden"), ("opinión", "juicio sobre lo ocurrido"), ("explicación", "texto que dice por qué ocurrió algo, con causas y evidencia"), ("evidencia", "dato de una fuente que apoya una afirmación"), ("responsabilidad", "hacerse cargo de lo que se dice y se hace")],
    worked=[
        ("Clasificar un texto", "{F} Clasifica el texto A.", ["El texto A cuenta qué ocurrió y en qué orden: se votó, ganó el «No», se convocó a elecciones.", "No dice por qué ocurrió."], "Es un relato"),
        ("Reconocer causas", "{F} ¿Cuántas causas nombra el texto C?", ["Primera: la Constitución de 1980 lo contemplaba; segunda: la coalición de partidos; tercera: la movilización social.", "Cuarta: la atención desde otros países."], "Cuatro causas"),
    ],
    mistakes=[("Creer que una explicación es lo mismo que contar lo que pasó.", "Contar el orden de los hechos no dice por qué ocurrieron.", "Agrega siempre las causas y la evidencia que las apoya."),
              ("Confundir una opinión con una explicación.", "«Fue lo mejor» juzga, pero no dice por qué ocurrió el plebiscito ni su resultado.", "Pregunta: ¿este texto dice por qué pasó o solo qué piensa su autor?")],
    T=[
        ("abc", "En HGCS: ¿qué es una explicación?", "Un texto que dice por qué ocurrió algo con causas y evidencia", "Un texto que solo cuenta el orden de los hechos", "Un texto con adjetivos", "Se distingue porque responde al por qué con evidencia."),
        ("abc", "{F} ¿Cuál texto es una opinión?", "El texto B", "El texto A", "El texto C", "El texto B juzga lo ocurrido y no entrega datos ni causas."),
        ("ab", "{F} ¿Qué texto es una explicación?", "El texto C", "El texto A", "El texto C incluye causas ordenadas y evidencia sobre el hecho."),
        ("abc", "{F} ¿Qué año fue el plebiscito?", "1988", "1973", "1990", "El texto A y el C lo indican con claridad."),
        ("abc", "{F} ¿Qué opción ganó según el texto A?", "El «No»", "El «Sí»", "Ninguna", "El texto lo dice de forma explícita."),
        ("ab", "{F} ¿Por qué se realizó el plebiscito según el texto C?", "Porque la Constitución de 1980 lo contemplaba", "Porque se declaró una fiesta nacional", "El texto C da esa causa en su primera frase."),
        ("=", "{F} ¿Cuántos años pasaron entre la Constitución de 1980 y el plebiscito de 1988?", "1988-1980", "Se restan los dos años para saber cuánto tiempo pasó entre ambos.", " años"),
        ("abc", "{F} ¿Qué dimensión muestra «una amplia coalición de partidos»?", "La política", "La medioambiental", "La económica", "Los partidos y las campañas pertenecen al ámbito político."),
        ("abc", "{F} Una persona dice: «El texto B explica el plebiscito». ¿Qué falla?", "Solo da una opinión y no dice causas ni evidencia", "El texto B es largo", "No usa fechas", "Una explicación necesita causas y evidencia, no solo un juicio."),
        ("abc", "{F} ¿Qué le falta al texto A para ser una explicación?", "Las causas de por qué ganó el «No»", "Más adjetivos", "Un título más largo", "Cuenta qué pasó pero no responde por qué."),
        ("ab", "¿Por qué una explicación incluye de dónde sale cada dato?", "Para que otras personas puedan comprobarlo", "Para hacerla más larga", "Citar la fuente es parte de la honestidad al explicar."),
        ("abc", "{F} ¿Qué idea del texto C muestra una perspectiva social?", "Que organizaciones sociales movilizaron a la ciudadanía", "Que la Constitución era de 1980", "Que hubo un resultado", "Alude a actores sociales y a su participación."),
        ("abc", "{F} ¿Cuál es una buena mejora para el texto B?", "Agregar al menos dos causas con su fuente", "Poner más signos de exclamación", "Quitar el año", "Así pasaría de opinión a explicación."),
    ],
    ctx=("abc", "En un taller de un centro de adultos, alguien pide explicar a un vecino joven por qué hubo un plebiscito en 1988. ¿Qué respuesta es una explicación y no solo un relato o una opinión?", "Porque la Constitución lo contemplaba, la oposición se unió y la ciudadanía se movilizó", "Porque fue lo mejor del mundo", "Porque votó mucha gente", "Da causas de distinto tipo que responden al por qué."),
    sc=[("En HGCS: ¿qué diferencia hay entre relato y explicación?", "El relato cuenta qué pasó y la explicación dice por qué", "La explicación agrega causas y evidencia."),
        ("En HGCS: ¿Qué incluye una buena explicación?", "Varias causas, evidencia y perspectivas", "Con eso se entiende mejor un conflicto."),
        ("¿Por qué citar la fuente?", "Para ser honestos y permitir comprobar los datos", "Citar da transparencia a la explicación.")],
    op=("Ficha de ejemplo: «Texto 1: En 1989 se eligió presidente y en 1990 asumió un gobierno elegido. Texto 2: Fue un cambio maravilloso. Texto 3: El regreso a gobiernos elegidos fue posible porque el plebiscito de 1988 abrió el camino a elecciones libres.» "
        "Clasifica cada texto como relato, opinión o explicación, justifica con una frase y reescribe el texto 1 para que explique al menos una causa.",
        "Texto 1: relato. Texto 2: opinión. Texto 3: explicación. Reescritura: En 1989 se eligió presidente y en 1990 asumió un gobierno elegido porque el plebiscito de 1988 abrió el camino a elecciones libres.",
        ["clasifica correctamente", "justifica con una frase", "agrega una causa en la reescritura"],
        ["una lista de tres clasificaciones y una frase reescrita"], ["llamar explicación a una opinión", "agregar una causa inventada"],
        "Pregunta: «¿Este texto dice por qué pasó o solo qué pasó?»."),
    reinforce="Escribe una frase de relato y otra de explicación sobre algo que haya cambiado en tu barrio, sin datos personales.",
    extend="Explica con un ejemplo por qué una opinión puede ser parte de una fuente pero no es una explicación.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (de ejemplo). Mapa de una explicación, con un ejemplo escrito para este cuaderno. "
      "Pregunta: «¿Por qué el plebiscito de 1988 llevó a elecciones y a un cambio de gobierno?» "
      "Tesis (idea central): el plebiscito llevó a un cambio porque se combinaron reglas que obligaban a realizar la votación, la unidad de la oposición y la movilización social. "
      "Argumento 1: la oposición se unió en una coalición (causa política). "
      "Argumento 2: organizaciones sociales movilizaron a la ciudadanía a inscribirse y a votar (causa social). "
      "Argumento 3: la Constitución de 1980 contemplaba el plebiscito (causa institucional). "
      "Conclusión: el resultado se explica por varias causas, y los historiadores siguen debatiendo cuánto pesó cada una.")
build(
    O, 2, F2,
    use="Hoy aprendo las partes de una explicación: pregunta, tesis, argumentos, evidencia, perspectivas y conclusión.",
    prior=["Distingo relato, opinión y explicación.", "Reconozco causas de distinto tipo.", "Sé qué es una fuente."],
    explain=[
        "Una explicación bien armada tiene partes. La pregunta dice qué queremos entender. La tesis es la idea central que respondemos. Los argumentos son las razones que sostienen la tesis, y cada uno se apoya en evidencia, es decir, en un dato de una fuente. La conclusión cierra con lo más importante y reconoce lo que aún se discute.",
        "Además conviene indicar la dimensión de cada causa (política, social, económica, internacional) y mostrar al menos dos perspectivas. Por ejemplo, la oposición y las organizaciones sociales vieron el plebiscito de forma distinta a la de quienes defendían al gobierno de entonces.",
        "También se usan conectores, como «porque», «por eso», «sin embargo» y «en conclusión», que ayudan a ordenar las ideas. Explicar con apertura a distintas perspectivas significa mostrar qué piensa cada actor sin cambiar los hechos comprobados.",
    ],
    vocab=[("tesis", "idea central que responde a la pregunta"), ("argumento", "razón que sostiene la tesis"), ("evidencia", "dato de una fuente que apoya un argumento"), ("conclusión", "cierre que resume lo más importante"), ("conector", "palabra que une ideas y muestra su relación")],
    worked=[
        ("Reconocer la tesis", "{F} ¿Cuál es la tesis del ejemplo?", ["La tesis es la idea central que responde a la pregunta.", "Dice que el cambio se explica por las reglas que obligaban a votar, la unidad de la oposición y la movilización social."], "Que el plebiscito llevó a un cambio por la combinación de reglas que obligaban a votar, unidad opositora y movilización social"),
        ("Tipo de argumento", "{F} ¿De qué tipo es el argumento 2?", ["Habla de organizaciones sociales que movilizaron a la ciudadanía.", "Se refiere a la sociedad: es una causa social."], "Una causa social"),
    ],
    mistakes=[("Escribir una tesis que solo repite la pregunta.", "Una tesis debe responder, no repetir.", "Contesta la pregunta con una idea central en una frase."),
              ("Dar argumentos sin evidencia.", "Sin un dato de una fuente, el argumento queda como opinión.", "Agrega un dato y la fuente que lo respalda.")],
    T=[
        ("abc", "{F} ¿Cuál es la pregunta de la ficha?", "Por qué el plebiscito de 1988 llevó a elecciones y a un cambio de gobierno", "Quién escribió la Constitución", "Cuántos votaron", "Es la pregunta escrita al comienzo de la ficha."),
        ("ab", "En HGCS: ¿qué es una tesis?", "La idea central que responde a la pregunta", "Un listado de fechas", "La tesis resume la respuesta que se defiende."),
        ("abc", "{F} ¿Cuántos argumentos tiene el ejemplo?", "Tres", "Uno", "Cinco", "La ficha enumera tres argumentos en su ejemplo."),
        ("abc", "{F} ¿Qué dimensión tiene el argumento 1?", "La política", "La medioambiental", "La económica", "La coalición de partidos es una causa política."),
        ("ab", "{F} ¿Qué argumento habla de la Constitución de 1980?", "El argumento 3", "El argumento 1", "Es el que menciona que contemplaba el plebiscito."),
        ("abc", "En HGCS: ¿qué es una evidencia?", "Un dato de una fuente que apoya un argumento", "Una opinión sin dato", "Un título", "La evidencia respalda el argumento con un dato."),
        ("=", "{F} Si hubo 3 argumentos y cada uno necesita 2 evidencias, ¿cuántas evidencias se necesitan en total?", "3*2", "Se multiplica el número de argumentos por las evidencias de cada uno.", " evidencias"),
        ("abc", "{F} ¿Para qué sirve la conclusión?", "Para cerrar con lo central y reconocer lo que aún se discute", "Para repetir toda la explicación", "Para cambiar de tema", "Resume y muestra los límites de lo que se sabe."),
        ("abc", "{F} Una persona escribe: «El plebiscito llevó a un cambio porque llevó a un cambio». ¿Qué falla?", "La tesis repite la pregunta y no explica", "Es muy corta", "No usa fechas", "Una tesis debe explicar por qué, no repetir."),
        ("abc", "{F} ¿Qué conector sirve para unir una causa con su efecto?", "«Por eso»", "«Sin embargo»", "«En cambio»", "«Por eso» muestra una relación de causa y efecto."),
        ("ab", "{F} ¿Qué conector sirve para mostrar oposición entre dos perspectivas?", "«Sin embargo»", "«Por eso»", "Se usa para contrastar dos ideas."),
        ("abc", "{F} Falta evidencia en el argumento 1. ¿Cuál serviría?", "Una nota de ejemplo de una coalición que informó sobre su campaña", "Un reglamento de fábrica de 1920", "Una carta de ejemplo sobre el voto de las mujeres", "Es un dato del tema, que respalda el argumento."),
        ("abc", "{F} ¿Qué perspectiva falta para tener apertura?", "La de quienes defendían al gobierno de entonces", "Otra opinión idéntica a la de la oposición", "Ninguna", "Mostrar más perspectivas aporta apertura a la explicación."),
    ],
    ctx=("abc", "Una dirigente vecinal prepara una charla sobre el plebiscito de 1988 para un centro cultural. Tiene tres ideas sueltas. ¿Qué parte de la explicación debe escribir primero?", "La pregunta y la tesis", "Los adjetivos finales", "El saludo", "La pregunta y la tesis ordenan todo lo demás."),
    sc=[("En HGCS: ¿Qué es un argumento?", "Una razón que sostiene la tesis", "Cada argumento se apoya en evidencia de una fuente."),
        ("¿Qué es la conclusión?", "El cierre que resume y reconoce lo que se discute", "Cierra la explicación y no introduce datos nuevos."),
        ("En HGCS: ¿Para qué sirven los conectores?", "Para unir ideas y mostrar su relación", "Hacen la explicación más clara y ordenada para quien lee.")],
    op=("Pregunta de ejemplo: «¿Por qué asumió un gobierno elegido en 1990?». Datos de ejemplo: a) el plebiscito de 1988 abrió el camino a elecciones; b) en 1989 se eligió presidente; c) la ciudadanía participó en la votación. "
        "Escribe una tesis de una frase, dos argumentos con su evidencia (letra del dato) y una conclusión que reconozca lo que aún se discute.",
        "Tesis: asumió un gobierno elegido en 1990 porque el plebiscito abrió el camino a elecciones y la ciudadanía participó. Argumento 1: el plebiscito abrió el camino (a). Argumento 2: se eligió presidente en 1989 con participación ciudadana (b, c). Conclusión: hubo varias causas; los historiadores debaten cuánto pesó cada una.",
        ["tesis que responde la pregunta", "argumentos con evidencia", "conclusión con límites"],
        ["una tesis, dos argumentos y una conclusión"], ["tesis que repite la pregunta", "argumentos sin evidencia"],
        "Pregunta: «¿Qué dato apoya este argumento?»."),
    reinforce="Escribe una pregunta sobre un cambio de tu barrio y una tesis de una frase que la responda.",
    extend="Explica con un ejemplo por qué una conclusión debe reconocer lo que aún se discute.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo). Pregunta: «¿Por qué se pasó de la dictadura a un gobierno elegido entre 1988 y 1990?» Fuentes inventadas. "
      "A) Texto de la Constitución de 1980 (resumen de ejemplo): contemplaba un plebiscito en 1988 sobre la continuidad del régimen. "
      "B) Relato de un dirigente vecinal (de ejemplo): «Desde 1983 hubo protestas nacionales; nos juntábamos en las poblaciones para pedir cambios.» "
      "C) Declaración de organizaciones de derechos humanos (de ejemplo): «Exigimos elecciones libres, verdad y respeto a los derechos.» "
      "D) Informe de una historiadora (de ejemplo): «La transición fue resultado de reglas institucionales, de la unidad opositora y de la presión social; sus resultados fueron graduales y no todos los sectores quedaron conformes.»")
build(
    O, 3, F3,
    use="Hoy aprendo, paso a paso, a construir una explicación con pregunta, tesis, argumentos y evidencia sobre la transición a la democracia.",
    prior=["Conozco las partes de una explicación.", "Distingo causas por dimensión.", "Cito fuentes."],
    explain=[
        "Para construir una explicación sigue estos pasos. Paso 1: escribe la pregunta. Paso 2: reúne las fuentes y subraya los datos. Paso 3: lista las causas y clasifícalas por dimensión. Paso 4: escribe la tesis, una idea central. Paso 5: redacta un argumento por causa, con su evidencia y la fuente. Paso 6: incluye una perspectiva distinta. Paso 7: concluye y reconoce los límites.",
        "En la transición se combinaron reglas institucionales (el plebiscito previsto), movilización social (protestas desde 1983), exigencias de derechos humanos y unidad opositora. La historiadora también aclara que los resultados fueron graduales y que no todos los sectores quedaron conformes. Una explicación completa menciona esa diversidad de miradas.",
        "Recuerda: no se inventan datos, se citan las fuentes y se evita justificar violaciones a los derechos humanos. Si un dato no está en las fuentes, se dice que no se sabe.",
    ],
    vocab=[("institucional", "relativo a las reglas y organismos del Estado"), ("movilización", "participación activa de personas y organizaciones para pedir un cambio"), ("gradual", "que ocurre por etapas"), ("sector", "grupo dentro de la sociedad"), ("límite de la evidencia", "lo que las fuentes no permiten saber")],
    worked=[
        ("Clasificar causas", "{F} Clasifica la causa de la fuente A.", ["La fuente A habla de una regla de la Constitución.", "Es una causa institucional y política."], "Causa institucional y política"),
        ("Escribir un argumento", "{F} Redacta un argumento con evidencia a partir de la fuente B.", ["Idea: hubo movilización social.", "Evidencia: desde 1983 hubo protestas nacionales (fuente B)."], "Hubo movilización social: desde 1983 hubo protestas nacionales (fuente B)"),
    ],
    mistakes=[("Escribir la conclusión sin haber definido antes la tesis.", "Sin una idea central, la explicación se dispersa.", "Define la tesis antes de redactar los argumentos."),
              ("Dar por seguro lo que las fuentes no dicen, como los porcentajes del plebiscito.", "Ninguna de las fuentes entrega cifras.", "Escribe «con las fuentes disponibles no se sabe».")],
    T=[
        ("abc", "{F} ¿Qué pregunta guía la explicación?", "Por qué se pasó de la dictadura a un gobierno elegido entre 1988 y 1990", "Quién ganó una elección", "Cuándo cerró una fábrica", "Es la pregunta de la ficha."),
        ("abc", "{F} ¿Qué dice la fuente A?", "Que la Constitución contemplaba un plebiscito en 1988", "Que hubo protestas desde 1983", "Que los sectores quedaron conformes", "Resume el contenido de la Constitución."),
        ("ab", "En HGCS: ¿qué significa «gradual»?", "Que ocurre por etapas", "Que ocurre de golpe", "Lo gradual avanza de a poco."),
        ("abc", "{F} ¿Desde qué año hubo protestas nacionales según B?", "1983", "1988", "1990", "El dirigente lo menciona de forma explícita en su relato."),
        ("ab", "{F} ¿Qué piden las organizaciones de C?", "Elecciones libres, verdad y respeto a los derechos", "Menos escuelas", "Las organizaciones lo dicen en su declaración."),
        ("abc", "{F} ¿Qué dimensión tiene la causa de B?", "La social", "La económica", "La medioambiental", "Habla de personas organizadas en las poblaciones."),
        ("=", "{F} ¿Cuántos años pasaron entre las protestas desde 1983 y el plebiscito de 1988?", "1988-1983", "Se restan los años para saber el tiempo entre ambos hechos.", " años"),
        ("abc", "{F} ¿Cuál es una buena tesis?", "La transición se explica por reglas institucionales, movilización social y unidad opositora", "La transición fue buena", "Hubo un plebiscito", "Responde con una idea central que reúne varias causas."),
        ("abc", "{F} ¿Cuál es un buen argumento con evidencia a partir de la fuente C?", "Hubo presión por los derechos: las organizaciones exigieron elecciones libres, verdad y respeto (fuente C)", "Hubo presión porque sí", "Todo el mundo estaba de acuerdo", "Une una idea, un dato y su fuente."),
        ("abc", "{F} ¿Qué aclara la historiadora que muestra una perspectiva distinta?", "Que no todos los sectores quedaron conformes", "Que todos aplaudieron", "Que nadie participó", "Muestra que hubo diversidad de miradas."),
        ("ab", "{F} Alguien pregunta cuántos votos ganó el «No». ¿Qué se debe responder?", "Que con estas fuentes no se sabe", "Que fueron muchísimos", "Las fuentes no entregan cifras, y no se inventan."),
        ("abc", "{F} ¿Qué paso del método falta si solo hay causas pero no tesis?", "El paso 4", "El paso 1", "El paso 7", "La tesis es el paso 4."),
        ("abc", "{F} ¿Qué conclusión es correcta y honesta?", "La transición se explica por varias causas y los resultados fueron graduales; con estas fuentes no se pueden medir los efectos", "La transición fue perfecta", "Todo fue una sola causa", "Reúne las causas y también los límites de la evidencia."),
    ],
    ctx=("abc", "Una organización comunitaria prepara un panel sobre la transición. Una persona propone agregar una cifra que «le suena». ¿Qué debería hacer el equipo según el método?", "No incluirla si no está en las fuentes y decir qué falta", "Ponerla en negrita", "Cambiarla por otra", "Una explicación honesta no usa datos sin fuente."),
    sc=[("¿Cuál es el primer paso para construir una explicación?", "Escribir la pregunta", "La pregunta ordena todo el trabajo posterior."),
        ("¿Qué incluye un argumento?", "Una idea, una evidencia y la fuente", "Así otras personas pueden comprobar el dato."),
        ("¿Qué hago con datos que no están en las fuentes?", "Digo que no se saben", "Así evito inventar datos que no existen.")],
    op=("Pregunta de ejemplo: «¿Por qué se crearon comisiones oficiales para investigar violaciones a los derechos humanos después de 1990?». Fuentes de ejemplo: a) declaración de una agrupación de familiares: ‘Pedimos saber la verdad’. "
        "b) discurso de un gobierno elegido de ejemplo: ‘Es necesario conocer lo ocurrido’. c) informe de una historiadora: ‘Hubo presión social y voluntad política’. "
        "Escribe pregunta, tesis, dos argumentos con fuente y una conclusión con un límite.",
        "Pregunta: ¿por qué se crearon comisiones oficiales? Tesis: se crearon por la demanda de las familias y la voluntad política del gobierno. Argumento 1: las familias pidieron verdad (a). Argumento 2: el gobierno quiso conocer lo ocurrido (b). Conclusión: la presión social y política (c) explican su creación; con estas fuentes no se conocen los detalles de su funcionamiento.",
        ["usa la pregunta y la tesis", "cita fuentes en los argumentos", "reconoce un límite"],
        ["una pregunta, una tesis, dos argumentos y una conclusión"], ["no citar", "inventar datos"],
        "Pregunta: «¿Qué fuente apoya cada argumento?»."),
    reinforce="Elige una fuente de esta clase y escribe un argumento con su evidencia y la letra de la fuente.",
    extend="Explica por qué un límite de la evidencia no debilita la explicación sino que la hace honesta.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo). Pregunta: «¿Por qué se crearon comisiones de verdad después de 1990?» Datos generales: tras el regreso a gobiernos elegidos, la Comisión Nacional de Verdad y Reconciliación entregó en 1991 un informe llamado Informe Rettig; "
      "años después una comisión sobre prisión política y tortura entregó en 2004 el Informe Valech. Fuentes inventadas. "
      "A) Declaración de familiares (de ejemplo): «Necesitamos saber qué pasó con nuestros seres queridos y que se reconozca el daño.» "
      "B) Discurso de una autoridad (de ejemplo): «Un país necesita conocer su pasado para construir una convivencia sana.» "
      "C) Columna de un analista (de ejemplo): «Investigar es importante, pero también hay que cuidar la estabilidad política.» "
      "D) Nota de una historiadora (de ejemplo): «Las comisiones respondieron a demandas sociales, a decisiones políticas y a la necesidad de reconocer lo ocurrido; sus informes aportaron antecedentes, aunque el debate sobre justicia siguió.»")
build(
    O, 4, F4,
    use="Hoy practico con apoyo la construcción de una explicación sobre la verdad y los derechos humanos, ordenando causas, perspectivas y evidencia.",
    prior=["Conozco los pasos para explicar.", "Sé qué es una tesis y un argumento.", "Distingo explicar de justificar."],
    explain=[
        "Después de 1990, los gobiernos elegidos crearon comisiones para investigar las violaciones a los derechos humanos de la dictadura. La Comisión de Verdad y Reconciliación entregó el Informe Rettig en 1991, y otra comisión entregó el Informe Valech en 2004. Sus informes reconocieron casos y entregaron antecedentes.",
        "Para explicar por qué se crearon, conviene combinar causas: sociales (la demanda de las familias y organizaciones), políticas (la decisión de gobiernos elegidos) y éticas o culturales (la necesidad de reconocer el daño). También hay perspectivas distintas sobre cómo equilibrar la verdad, la justicia y la estabilidad política.",
        "En este caso practicamos con apoyo: revisamos cada fuente, anotamos la causa que señala, la dimensión y qué valora. Luego escribimos una tesis y dos argumentos que citen fuentes, sin justificar abusos y sin descartar a quien piensa distinto.",
    ],
    vocab=[("comisión", "grupo oficial creado para investigar un tema"), ("informe", "documento que reúne y presenta los resultados de una investigación"), ("reconocer el daño", "aceptar públicamente que algo ocurrió y afectó a personas"), ("estabilidad política", "situación en que las instituciones funcionan sin grandes quiebres"), ("antecedente", "dato previo que ayuda a entender un hecho")],
    worked=[
        ("Causa y dimensión", "{F} Clasifica la causa de la fuente A.", ["Es una demanda de familiares.", "Las demandas de grupos de la sociedad son causas sociales."], "Causa social"),
        ("Argumento con evidencia", "{F} Escribe un argumento a partir de la fuente B.", ["Idea: hubo decisión política.", "Evidencia: una autoridad dijo que un país necesita conocer su pasado (fuente B)."], "Hubo decisión política: una autoridad sostuvo que se debía conocer el pasado (fuente B)"),
    ],
    mistakes=[("Presentar la columna del analista como «la verdad».", "La fuente C es una perspectiva sobre cómo equilibrar valores.", "Anota que es una opinión de un analista y qué valora."),
              ("Decir que las comisiones solucionaron todo.", "La fuente D indica que el debate sobre justicia siguió.", "Menciona los límites y lo que quedó pendiente.")],
    T=[
        ("abc", "{F} ¿Cuál de los dos informes se entregó primero?", "El Informe Rettig, en 1991", "El Informe Valech, en 2004", "Los dos en el mismo año", "La ficha da 1991 para el Rettig y 2004 para el Valech."),
        ("abc", "{F} ¿De qué trató la comisión que entregó el informe de 2004?", "De prisión política y tortura", "De la reforma agraria", "Del voto de las mujeres", "La ficha dice que fue una comisión sobre prisión política y tortura."),
        ("ab", "En HGCS: ¿qué es una comisión?", "Un grupo oficial creado para investigar un tema", "Un partido político", "Una comisión reúne antecedentes y entrega un informe."),
        ("abc", "{F} ¿Qué pide la fuente A?", "Saber qué pasó y que se reconozca el daño", "Que se cierre el tema", "Que no se hable más", "Lo dicen de forma explícita los familiares."),
        ("ab", "{F} ¿Qué valora la fuente C?", "La estabilidad política junto con investigar", "La inflación", "La columna conecta investigar con la estabilidad."),
        ("abc", "{F} ¿Qué dice la fuente D sobre el debate?", "Que el debate sobre justicia siguió", "Que terminó de inmediato", "Que nadie opinó", "Lo afirma la historiadora en su nota."),
        ("=", "{F} ¿Cuántos años pasaron entre el regreso a gobiernos elegidos en 1990 y el Informe Valech de 2004?", "2004-1990", "Se restan los dos años.", " años"),
        ("abc", "{F} ¿Qué dimensión muestra la fuente B?", "La política", "La medioambiental", "La económica", "Una autoridad toma una decisión pública."),
        ("abc", "{F} ¿Cuál es una buena tesis?", "Las comisiones se crearon por la demanda social, la decisión política y la necesidad de reconocer el daño", "Las comisiones eran inútiles", "Las comisiones lo resolvieron todo", "Reúne causas de varias dimensiones en una idea central."),
        ("abc", "{F} Una persona dice: «El Informe Rettig puso fin a toda discusión». ¿Qué falla?", "La fuente D dice que el debate sobre justicia siguió", "Nada falla", "No existió el informe", "Contradice lo que dice la fuente D."),
        ("ab", "{F} ¿Qué perspectiva presenta la fuente C?", "Que se debe investigar cuidando la estabilidad", "Que no se debe investigar nunca", "Pide equilibrio, no negar la investigación."),
        ("abc", "{F} ¿Cuál sería un buen conector para unir A y C?", "«Sin embargo»", "«Por eso»", "«Ahora»", "Las dos miradas valoran cosas distintas."),
        ("abc", "{F} ¿Qué conclusión es respetuosa y rigurosa?", "Las comisiones respondieron a varias causas; hubo perspectivas distintas sobre cómo equilibrar verdad, justicia y estabilidad", "Las comisiones fueron una pérdida de tiempo", "Todos opinaron lo mismo", "Reconoce varias causas y la diversidad de miradas."),
    ],
    ctx=("abc", "Una agrupación de la comuna prepara un folleto de ejemplo sobre las comisiones de verdad para estudiantes de un centro de adultos. Debe usar lenguaje claro y respetuoso. ¿Qué enfoque conviene?", "Explicar las causas, citar fuentes y no justificar abusos ni descalificar a nadie", "Usar solo adjetivos fuertes", "Evitar mencionar el Informe Rettig", "El folleto combina claridad, rigor y respeto."),
    sc=[("¿Qué es un informe?", "Un documento que presenta los resultados de una investigación", "Un informe sirve como fuente para explicar."),
        ("¿Qué son los antecedentes?", "Datos previos que ayudan a entender un hecho", "Aportan contexto a las explicaciones históricas."),
        ("¿Qué hago con una opinión?", "La atribuyo a quien la dice y anoto qué valora", "Así no la presento como si fuera un hecho.")],
    op=("Pregunta de ejemplo: «¿Por qué muchas organizaciones siguieron pidiendo justicia después de los informes de las comisiones?». Fuentes de ejemplo: a) declaración de una organización: ‘Conocer la verdad es un primer paso, pero falta justicia’. "
        "b) nota de una historiadora: ‘Los informes aportaron antecedentes, pero el debate sobre sanciones continuó’. c) columna de un analista: ‘Hay quienes prefieren cerrar el tema’. "
        "Escribe una tesis, dos argumentos con fuente y una conclusión que reconozca una perspectiva distinta.",
        "Tesis: siguieron pidiendo justicia porque conocer la verdad no cerraba la demanda de sanciones. Argumento 1: la organización dice que falta justicia (a). Argumento 2: la historiadora dice que el debate sobre sanciones continuó (b). Conclusión: existen quienes prefieren cerrar el tema (c); las perspectivas son distintas, pero los hechos comprobados no se discuten.",
        ["tesis que responde", "argumentos con fuente", "reconoce una perspectiva distinta sin justificar abusos"],
        ["una tesis, dos argumentos y una conclusión"], ["no citar", "descalificar a un grupo"],
        "Pregunta: «¿Qué perspectiva distinta incluí?»."),
    reinforce="Elige una fuente de la ficha y escribe una frase que empiece con «Según…».",
    extend="Explica por qué reconocer perspectivas distintas no es lo mismo que negar hechos comprobados.",
)

# ======================================================= clase 5
F5 = ("Ficha 5 (de ejemplo). Preparar una explicación para una audiencia. Pregunta: «¿Por qué se quebró la democracia en 1973?» Causas señaladas por distintas fuentes de ejemplo: "
      "1) polarización política, con dos bandos que no lograban dialogar (política); "
      "2) conflicto entre el gobierno y el Congreso (política); "
      "3) inflación y escasez de productos (económica); "
      "4) movilización y tensión en las calles, fábricas y campos (social); "
      "5) el contexto internacional de la Guerra Fría (internacional). "
      "Hecho comprobado: el 11 de septiembre de 1973 las Fuerzas Armadas derrocaron al gobierno y comenzó la dictadura, durante la cual se cometieron graves violaciones a los derechos humanos establecidas por informes oficiales y sentencias. "
      "Audiencia de ejemplo: una charla de dos minutos en un centro comunitario para personas de distintas edades y miradas.")
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido: preparo y comunico una explicación para una audiencia real, con claridad, respeto y evidencia.",
    prior=["Sé armar una explicación con tesis y argumentos.", "Distingo relato, opinión y explicación.", "Cito fuentes y reconozco límites."],
    explain=[
        "Comunicar una explicación es adaptar lo que sabes a quien te escucha. Para una charla de dos minutos eliges la idea central, dos o tres causas, un dato de evidencia y una conclusión. Usas frases cortas, palabras claras y conectores. No hace falta decirlo todo: hace falta que se entienda y que sea verdadero.",
        "En el caso del quiebre de la democracia hay varias causas de distintas dimensiones: política, económica, social e internacional. Distintas personas ponen el acento en unas u otras. Una explicación responsable las presenta como causas debatidas, no como una verdad cerrada, y aclara el hecho comprobado y que las violaciones a los derechos humanos no tienen justificación.",
        "Al comunicar, cuida el tono: no humilles, no exageres y no atribuyas ideas a quien no las dijo. Si alguien en la audiencia vivió esos años, su dolor o su experiencia merecen respeto; escuchar es también comunicar.",
    ],
    vocab=[("audiencia", "personas a quienes se dirige una explicación"), ("idea central", "lo más importante que se quiere comunicar"), ("tono", "manera de decir algo, que muestra respeto o falta de él"), ("guion", "texto breve que ordena lo que se va a decir"), ("causa debatida", "causa cuyo peso se discute entre quienes estudian el tema")],
    worked=[
        ("Elegir causas para dos minutos", "{F} ¿Cuántas causas conviene presentar en una charla de dos minutos?", ["Con dos minutos, tres causas alcanzan sin apurar.", "Cada una necesita una frase de explicación y un dato."], "Dos o tres causas, con un dato cada una"),
        ("Cuidar el tono", "{F} ¿Cómo se dice con respeto que la causa 3 fue una crisis económica?", ["Se nombra la causa sin culpar a nadie del público.", "Se atribuye a las fuentes: «según varias fuentes, hubo inflación y escasez»."], "Según varias fuentes, hubo inflación y escasez de productos"),
    ],
    mistakes=[("Intentar decir todas las causas en dos minutos.", "La audiencia se pierde y no recuerda nada.", "Elige tres causas principales y menciona que hay otras."),
              ("Usar un tono de burla o enojo hacia quien piensa distinto.", "Rompe el diálogo y no ayuda a comprender.", "Explica la causa y deja que la evidencia hable.")],
    T=[
        ("abc", "{F} ¿Cuántas causas lista la ficha?", "Cinco", "Tres", "Siete", "La ficha las enumera del 1 al 5."),
        ("abc", "{F} ¿Qué causa es económica?", "Inflación y escasez de productos", "Polarización política", "Contexto de Guerra Fría", "La causa habla de precios y de producción."),
        ("ab", "En HGCS: ¿qué es una audiencia?", "Las personas a quienes se dirige una explicación", "Un tipo de gobierno", "La audiencia es quien escucha o lee."),
        ("abc", "{F} ¿Qué hecho comprobado señala la ficha?", "El derrocamiento del gobierno el 11 de septiembre de 1973", "Que todos estaban de acuerdo", "Que no hubo crisis", "Es el hecho de partida de la explicación."),
        ("abc", "{F} ¿Qué dimensión tiene «contexto de la Guerra Fría»?", "La internacional", "La medioambiental", "La económica local", "Habla de la relación entre grandes bloques."),
        ("ab", "{F} ¿Cuánto debería durar la charla del ejemplo?", "Dos minutos", "Veinte minutos", "La ficha indica la duración de la charla."),
        ("=", "{F} Si eliges 3 de las 5 causas para la charla, ¿cuántas causas no incluyes?", "5-3", "Se resta las incluidas del total de causas.", " causas"),
        ("abc", "{F} ¿Cuál es una buena frase de inicio?", "Hoy les explico por qué se quebró la democracia en 1973, con tres causas que señalan las fuentes", "Todos saben por qué", "Fue culpa de ellos", "Anuncia la idea central y las causas."),
        ("abc", "{F} Una persona propone decir «los que pensaban distinto fueron culpables de todo». ¿Qué falla?", "Atribuye culpas sin evidencia y rompe el respeto", "Es muy corta", "Es muy larga", "Una explicación responsable no culpa sin evidencia."),
        ("abc", "{F} ¿Qué se debe aclarar sobre los derechos humanos en la charla?", "Que las violaciones están establecidas y no tienen justificación", "Que fueron necesarias", "Que no se pueden mencionar", "Está respaldado por informes oficiales y sentencias."),
        ("ab", "{F} ¿Cómo se presenta mejor la causa 5?", "Como una causa debatida que varias fuentes mencionan", "Como la única causa", "Mostrarla como debatida evita cerrar la discusión."),
        ("abc", "{F} ¿Qué recurso ayuda a que la audiencia recuerde la explicación?", "Un guion de tres ideas con ejemplos breves", "Un texto de diez páginas", "Muchos números sin explicar", "La brevedad y los ejemplos facilitan la memoria."),
        ("abc", "{F} Si alguien del público se emociona al hablar del tema, ¿qué conviene?", "Escuchar con respeto y dar espacio, sin presionar a nadie a contar", "Pedir que cuente todo", "Ignorar la emoción", "El respeto es parte de comunicar."),
    ],
    ctx=("abc", "En un centro comunitario piden explicar en dos minutos «qué pasó en 1973». Tienes la ficha. ¿Qué plan de charla es más adecuado?", "Hecho comprobado, tres causas con sus fuentes, aclaración sobre derechos humanos y una pregunta abierta", "Una lista de diez fechas sin explicar", "Una opinión personal sin datos", "El plan es breve, ordenado y respetuoso con la audiencia."),
    sc=[("¿Qué es una causa debatida?", "Una causa cuyo peso se discute entre quienes estudian el tema", "Se presenta como debatida, no como verdad cerrada."),
        ("¿Cuántas causas conviene en dos minutos?", "Dos o tres", "Con pocas causas la audiencia entiende mejor."),
        ("¿Qué cuido al comunicar?", "El tono, los datos y el respeto", "Son parte de comunicar con responsabilidad.")],
    op=("Prepara una charla de dos minutos (unas 150 palabras) con la ficha de esta clase para responder «¿Por qué se quebró la democracia en 1973?». Debe incluir: el hecho comprobado, tres causas con su dimensión, una aclaración sobre los derechos humanos, un cierre con una pregunta abierta. "
        "Después marca qué parte cuidaste para el tono.",
        "Hecho: el 11 de septiembre de 1973 se derrocó al gobierno. Causas: polarización política (política), inflación y escasez (económica), movilización y tensión social (social). Aclaración: las violaciones a los derechos humanos de la dictadura están establecidas y no tienen justificación. Pregunta: ¿qué otras causas pesaron? Tono: usé «según las fuentes» y no culpé a nadie.",
        ["incluye hecho, tres causas y aclaración", "usa conectores y un tono respetuoso", "cierra con una pregunta abierta"],
        ["un guion de unas 150 palabras y una nota sobre el tono"], ["culpar sin evidencia", "justificar violaciones a los derechos humanos"],
        "Pregunta: «¿Se entiende en dos minutos y respeta a la audiencia?»."),
    reinforce="Elige una causa de la ficha y escribe una frase clara para explicársela a una persona que no conoce el tema.",
    extend="Explica por qué cambiar el tono y el largo no debe cambiar los hechos comprobados.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Borrador inventado de un estudiante sobre la pregunta «¿Por qué hubo una dictadura y luego una transición en Chile?»: "
      "«En 1973 hubo un golpe. Después vino una dictadura y todos sufrieron igual. En 1988 hubo un plebiscito y todo se arregló. Esto pasó solo por culpa de los políticos.» "
      "Rúbrica de ejemplo: 1) responde la pregunta con una tesis; 2) incluye al menos tres causas o factores; 3) usa evidencia y cita las fuentes; 4) incluye al menos dos perspectivas; 5) no inventa ni exagera y no justifica violaciones a los derechos humanos; 6) reconoce límites y deja una pregunta abierta.")
build(
    O, 6, F6,
    use="Hoy reviso una explicación con una rúbrica, la mejoro con honestidad y decido cómo seguir aprendiendo.",
    prior=["Sé construir una explicación.", "Uso conectores y fuentes.", "Reconozco límites de la evidencia."],
    explain=[
        "Revisar una explicación es compararla con una rúbrica, una lista de criterios que describe qué significa hacerlo bien. La rúbrica de esta clase pide una tesis, varias causas, evidencia citada, perspectivas distintas, ausencia de exageraciones y reconocimiento de límites. Revisar no es castigar: es encontrar qué mejorar.",
        "El borrador de ejemplo tiene problemas típicos. Dice «todos sufrieron igual», una exageración que no distingue experiencias distintas; dice «todo se arregló», una frase absoluta que ignora que el debate continuó; y dice «solo por culpa de los políticos», una sola causa que simplifica un proceso con muchas causas. Corregirlo exige precisión.",
        "Comunicar con responsabilidad es corregir tus propios errores cuando los encuentras y decir cuáles fueron. La honestidad también está en reconocer qué no sabes y qué otras fuentes buscarías.",
    ],
    vocab=[("rúbrica", "lista de criterios para evaluar un trabajo"), ("exageración", "decir más de lo que muestran los datos"), ("frase absoluta", "frase que usa «todos», «nunca» o «todo» sin matices"), ("corregir", "cambiar algo para que sea más exacto"), ("responsabilidad", "hacerse cargo de lo que se dice y de sus efectos")],
    worked=[
        ("Evaluar con la rúbrica", "{F} ¿Cumple el borrador el criterio 2 (al menos tres causas)?", ["El borrador dice que fue «solo por culpa de los políticos».", "Menciona una sola causa."], "No cumple: hay una sola causa"),
        ("Corregir una frase absoluta", "{F} Reescribe «todo se arregló».", ["La frase es absoluta e ignora que el debate sobre justicia continuó.", "Se puede decir que el plebiscito abrió el camino a elecciones, pero quedaron temas pendientes."], "El plebiscito abrió el camino a elecciones libres, aunque quedaron temas pendientes"),
    ],
    mistakes=[("Corregir el borrador cambiando solo las palabras sin cambiar las ideas.", "Las exageraciones y la causa única siguen estando.", "Revisa criterio por criterio con la rúbrica."),
              ("Creer que una explicación mejora si se hace más larga.", "Más palabras no equivalen a más evidencia ni más perspectivas.", "Agrega datos y fuentes, no relleno.")],
    T=[
        ("abc", "{F} ¿Cuántos criterios tiene la rúbrica?", "Seis", "Tres", "Diez", "La ficha enumera seis criterios en su rúbrica."),
        ("abc", "{F} ¿Qué dice el borrador del plebiscito?", "Que todo se arregló", "Que no hubo plebiscito", "Que fue un golpe", "Es la frase que aparece escrita en el borrador."),
        ("ab", "En HGCS: ¿qué es una rúbrica?", "Una lista de criterios para evaluar un trabajo", "Un tipo de gobierno", "La rúbrica describe qué es hacerlo bien."),
        ("abc", "{F} ¿Qué criterio incumple «todos sufrieron igual»?", "El de no exagerar", "El de incluir una tesis", "El de usar fechas", "Esa frase no distingue las experiencias distintas."),
        ("ab", "{F} ¿Qué es una frase absoluta?", "Una frase con «todos», «nunca» o «todo» sin matices", "Una frase con fecha", "Las frases absolutas suelen ser inexactas."),
        ("abc", "{F} ¿Qué criterio exige que el borrador diga de dónde sale cada dato?", "El criterio 3, sobre evidencia y fuentes", "El criterio 1, sobre la tesis", "El criterio 4, sobre las perspectivas", "El criterio 3 pide evidencia y citar las fuentes."),
        ("=", "{F} Si el borrador cumple 1 de los 6 criterios, ¿cuántos le faltan?", "6-1", "Se resta los cumplidos del total de criterios.", " criterios"),
        ("abc", "{F} ¿Cuál es una mejor versión de «todos sufrieron igual»?", "Hubo graves violaciones a los derechos humanos y las experiencias de las personas fueron distintas", "Las experiencias personales no sirven para explicar", "Todas las experiencias fueron exactamente iguales", "Es precisa y respeta las experiencias."),
        ("abc", "{F} ¿Cuál es una mejor versión de «solo por culpa de los políticos»?", "Hubo varias causas políticas, económicas, sociales e internacionales", "No hubo causas", "Los políticos no existen", "Reconoce la multicausalidad del proceso histórico."),
        ("abc", "{F} ¿Qué falta para cumplir el criterio 3?", "Citar al menos una fuente de ejemplo con datos", "Más signos de exclamación", "Un título", "La evidencia se apoya en fuentes."),
        ("ab", "{F} ¿Cómo se cumple el criterio 6?", "Reconociendo que con estas fuentes no se sabe cuánto pesó cada causa y dejando una pregunta", "Diciendo que todo se sabe", "Los límites y las preguntas abiertas son parte de una explicación honesta."),
        ("abc", "{F} ¿Qué decisión de mejora es mejor para el borrador?", "Reescribirlo con tesis, tres causas, evidencia y dos perspectivas", "Borrarlo", "Agregar adjetivos", "Responde a la rúbrica con acciones concretas."),
        ("abc", "{F} Tras mejorar el borrador, ¿qué paso de comunicación conviene?", "Leerlo en voz alta a otra persona y preguntar qué entendió", "Esconderlo", "Cambiar las fechas", "La audiencia ayuda a ver si se entiende."),
    ],
    ctx=("abc", "En un taller de la biblioteca, una participante lee su explicación y otra le pregunta de dónde sacó un dato. Ella responde que no recuerda y decide indicar en la explicación que no puede comprobarlo. ¿Qué valor muestra?", "Honestidad y responsabilidad al comunicar", "Falta de interés", "Desorden", "Reconocer un límite es una forma de honestidad."),
    sc=[("¿Qué es una frase absoluta?", "Una frase con «todo» o «nunca» sin matices", "Una frase absoluta suele exagerar lo que dicen los datos."),
        ("En HGCS: ¿Para qué sirve una rúbrica?", "Para evaluar con criterios claros", "Evita decidir solo por una impresión personal."),
        ("¿Qué hago al encontrar un error en mi trabajo?", "Lo corrijo y lo reconozco", "Corregir y reconocerlo es una muestra de responsabilidad.")],
    op=("Elige uno de los temas del módulo (quiebre de la democracia, dictadura, transición o derechos humanos). Escribe una explicación final de 10 líneas con tesis, tres causas con su dimensión, dos perspectivas, evidencia con fuentes de ejemplo y una pregunta abierta. "
        "Evalúala con la rúbrica de seis criterios, marca cuáles cumple y decide un paso siguiente.",
        "Tema: derechos humanos. Tesis: se crearon comisiones por demanda social, decisión política y necesidad de reconocimiento. Perspectivas: familiares piden verdad y justicia; un analista pide cuidar la estabilidad. Evidencia: fuentes A y C de la clase 4. Pregunta: ¿cómo se recuerda el pasado hoy? Evaluación: cumple 1, 2, 3, 4, 5; falta mejorar el 6 explicando mejor el límite; paso siguiente: leer a otra persona.",
        ["cumple al menos cinco criterios o explica cuáles faltan", "cita fuentes del cuaderno", "decide un paso siguiente concreto"],
        ["una explicación de diez líneas, una autoevaluación y un paso siguiente"], ["no citar fuentes", "justificar violaciones a los derechos humanos"],
        "Pregunta: «¿Qué criterio cumplo y cuál me falta?»."),
    reinforce="Vuelve a tu explicación de la clase 3 y reescribe una frase absoluta con más precisión.",
    extend="Explica a otra persona, con tus palabras, qué cambia cuando se evalúa un trabajo con una rúbrica y no solo con una impresión.",
)
