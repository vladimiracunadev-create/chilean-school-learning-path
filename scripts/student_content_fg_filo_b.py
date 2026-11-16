"""Filosofía 3.º medio FG: OA 04 (preguntas epistemológicas sobre conocimiento, ciencia y verdad). Casos de ejemplo inventados."""
from __future__ import annotations

from fg_filo_common import build

O4 = "FG-FILO-3M-OAC-04"

# ============================================================ OA 04, clase 1
F = ("Ficha 1 (caso de ejemplo): Camila dice «Sé que mañana lloverá, porque a mi abuelo le duele la rodilla antes de llover». "
     "Tomás dice «Creo que lloverá, porque un servicio meteorológico anunció un 90 % de probabilidad de lluvia». "
     "Ana dice «No lo sé: no tengo razones ni para afirmarlo ni para negarlo». Al día siguiente llovió.")
build(
    O4, 1, F,
    use="Aprenderé a convertir una situación cotidiana en preguntas sobre el conocimiento: cómo sé algo, qué razones bastan y cuándo puedo equivocarme.",
    prior=["Sé distinguir un hecho de una opinión.", "Sé que una afirmación puede ser verdadera o falsa.", "Sé que los argumentos tienen razones."],
    explain=[
        "La filosofía tiene ramas. La ontología pregunta qué existe y cómo es la realidad; la ética pregunta qué debemos hacer; la epistemología pregunta por el conocimiento: cómo lo obtenemos, qué lo justifica y cuándo podemos equivocarnos. Una pregunta epistemológica suele empezar con «¿cómo sé que…?» o «¿qué razones tengo para…?».",
        "Creer es aceptar que algo es verdadero. Saber pide más: que lo creído sea verdadero y que tengamos buenas razones para creerlo, a lo cual se llama justificación. Acertar por casualidad no es saber. Si Camila afirma que lloverá solo por una sensación y llueve, acertó, pero su razón es débil: pudo ser azar. Una razón es mejor cuando otras personas pueden revisarla.",
        "Problematizar es pasar de una situación a una pregunta que no se responde con un simple sí o no. Primero se separa lo que se afirma de las razones que se dan; luego se detecta lo que se da por supuesto, y al final se formula la pregunta. Una actitud posible es suspender el juicio: no afirmar ni negar mientras no haya razones suficientes.",
    ],
    vocab=[("epistemología", "rama de la filosofía que estudia el conocimiento, sus fuentes y su justificación"), ("creencia", "aceptar que algo es verdadero"), ("justificación", "razones que respaldan una creencia"), ("suspender el juicio", "no afirmar ni negar algo mientras faltan razones suficientes"), ("problematizar", "transformar una situación en una pregunta que exige razones y no se responde con un simple sí o no")],
    worked=[
        ("Distinguir creer y saber", "Un compañero de ejemplo asegura que su equipo ganará el sábado «porque lo presiente». Gana. ¿Sabía que ganaría?", ["Creía que ganaría y resultó verdadero.", "Su única razón era un presentimiento, que otros no pueden revisar.", "Acertar por azar no es saber."], "Acertó, pero no sabía: faltaba justificación"),
        ("Formular una pregunta epistemológica", "Una amiga de ejemplo comparte un mensaje que dice que cierto té cura el resfrío. ¿Qué pregunta epistemológica surge?", ["Se separa la afirmación («el té cura») de las razones que se dan (ninguna).", "Se pregunta cómo se podría saber si es cierto."], "¿Qué razones o pruebas respaldan que el té cura?"),
    ],
    mistakes=[("Creer que si una afirmación resultó verdadera, quien la dijo sabía.", "Se olvida que la verdad puede acertarse por azar.", "Pregunta qué razones tenía antes de saber el resultado."),
              ("Creer que sin certeza total no se puede decir nada.", "Se confunde equivocarse a veces con no tener razones.", "Distingue razones fuertes de razones débiles y di cuánta confianza tienes.")],
    T=[
        ('abc', '¿Qué estudia la epistemología?', 'El conocimiento: cómo se obtiene y cuándo está justificado', 'La existencia: qué cosas hay y cómo es la realidad en sí misma', 'La conducta: qué acciones debemos hacer y cuáles evitar', 'La ontología estudia lo que existe y la ética lo que debemos hacer; la epistemología se ocupa del conocimiento.'),
        ('abc', '{F} ¿Qué razón da Camila para afirmar que lloverá?', 'Una sensación física de su abuelo, que otros no pueden comprobar', 'Un dato de un servicio meteorológico que otras personas pueden consultar y revisar', 'La observación de nubes durante varias semanas seguidas', 'Camila solo menciona la rodilla de su abuelo; el servicio meteorológico lo cita Tomás.'),
        ('abc', '{F} ¿Cuál razón puede ser revisada por otras personas?', 'La probabilidad anunciada por el servicio meteorológico', 'La sensación en la rodilla del abuelo de Camila, que él describe con mucha seguridad', 'La seguridad con que Camila repite su afirmación', 'Un dato publicado puede consultarse y compararse; una sensación personal o la seguridad al hablar no pueden comprobarse desde afuera.'),
        ('abc', '{F} ¿Qué actitud muestra Ana?', 'Suspender el juicio, porque no afirma ni niega sin razones', 'Negar que llueva, porque no tiene ninguna razón a favor', 'Creer lo que diga la mayoría de las personas del grupo', 'Ana no afirma ni niega: eso es suspender el juicio, distinto de negar.'),
        ('abc', '{F} Llovió. Un compañero dice «Camila tenía razón y sabía que llovería». ¿Qué error comete?', 'Supone que acertar equivale a saber, sin mirar si había buenas razones', 'Supone que la lluvia es imposible de predecir con algún método, por lo que toda predicción sería inútil', 'Supone que Tomás y Camila usaron las mismas razones', 'Acertar puede ser azar; para saber hacen falta razones que respalden lo creído.'),
        ('Además de creer, ¿qué dos condiciones se piden para decir que alguien sabe algo?', 'Que sea verdadero y que esté justificado', 'Saber exige creer algo que sea verdadero y que tenga buenas razones; falta cualquiera de las dos y solo hay creencia.'),
        ('abc', '¿Cuál de estas es una pregunta epistemológica?', '¿Cómo puedo saber que una noticia es confiable?', '¿Qué es mejor, mentir o decir una verdad dolorosa?', '¿Existe el tiempo fuera de nuestra mente?', 'Pregunta por el conocimiento y sus razones; las otras son de ética y de ontología.'),
        ('abc', '{F} Si el servicio hubiera anunciado 90 % de lluvia y no hubiese llovido, ¿qué se puede decir de Tomás?', 'Tuvo una buena justificación, pero su creencia resultó falsa', 'No tuvo ninguna razón válida, porque la predicción falló y eso invalida cualquier justificación', 'Sabía que llovería, porque confiaba en una fuente', 'La justificación no garantiza la verdad: se puede tener buenas razones y equivocarse, y entonces no hay saber.'),
        ('abc', '{F} ¿Qué se da por supuesto en la frase de Camila?', 'Que la sensación del abuelo es un indicio fiable de lluvia', 'Que el servicio meteorológico se equivoca con frecuencia', 'Que Ana tiene una opinión parecida a la suya', 'Camila supone, sin mostrarlo, que lo que siente su abuelo anticipa la lluvia.'),
        ('abc', '{F} ¿Qué pregunta convierte este caso en un problema epistemológico?', '¿Qué razones hacen más confiable una predicción que una sensación?', '¿Quién de los tres tiene mejor carácter?', '¿Es bueno o malo que llueva en esa estación?', 'Pregunta por las razones y la confianza; las demás hablan de personas o de valoraciones.'),
        ('abc', 'Una persona dice: «Si no puedo estar 100 % seguro, entonces no sé nada y no puedo opinar». ¿Qué conviene responder?', 'Que se puede tener razones fuertes sin certeza total y seguir revisándolas', 'Que la duda no sirve y lo correcto es aceptar siempre lo que diga la mayoría del grupo', 'Que tiene razón, porque cualquier error posible borra todas las razones', 'Confundir razones fuertes con certeza total lleva a un error: se puede estar bien justificado y aun así revisar la creencia.'),
        ('{F} Escribe una pregunta epistemológica que Ana podría hacer a Camila.', '¿Cómo sabes que el dolor de rodilla de tu abuelo anuncia lluvia?', 'Pide las razones o pruebas detrás de la afirmación, que es lo propio de la epistemología.'),
        ('abc', '{F} Dos días seguidos Camila acierta, y el tercero se equivoca. ¿Qué indica esto sobre su método?', 'Que su razón es insuficiente para saber, aunque haya acertado algunas veces', 'Que su método es perfecto, porque acertó más de una vez y eso prueba que sus razones son buenas', 'Que su abuelo siente cosas distintas cada día', 'Acertar a veces no basta: un método fiable debería acertar con regularidad y dejar razones que otros revisen.'),
    ],
    ctx=('abc', 'Una amiga de ejemplo reenvía un mensaje que dice que «cierta marca de jugo mejora la memoria». No cita ninguna fuente. ¿Cuál es la mejor primera pregunta?', '¿Qué razones o estudios respaldan esa afirmación?', '¿Quién la reenvió primero y cuántas personas la leyeron?', '¿Por qué esa marca habría querido publicar eso?', 'Lo primero es ver si la afirmación está justificada; el origen y el motivo de la marca pueden revisarse después.'),
    sc=[
        ('En Filosofía: ¿qué es suspender el juicio?', 'No afirmar ni negar algo mientras faltan razones suficientes', 'Es una actitud intermedia: ni creer ni negar hasta tener razones.'),
        ('abc', '¿Cuál ejemplo corresponde a una creencia justificada?', 'Creer que el agua hierve a cierta temperatura porque lo midieron varias personas', 'Creer que un número saldrá sorteado porque anoche se soñó con él', 'Creer que una noticia es verdadera porque se la mandaron muchas veces', 'La justificación viene de una medición que otros pueden repetir; el sueño y la repetición no son razones.'),
        ('¿Para qué sirve problematizar una situación?', 'Para convertirla en una pregunta que exige razones', 'Se pasa de un caso a una pregunta que no se responde con un sí o un no.'),
    ],
    op=("Usa la {F} Escribe cuatro líneas: (1) qué afirma cada persona; (2) qué razón da cada una; (3) una pregunta epistemológica que surge; (4) una conclusión prudente que no diga quién es mejor persona.",
        "(1) Camila afirma que lloverá; Tomás lo cree; Ana no sabe. (2) Camila, una sensación; Tomás, un dato publicado; Ana, ninguna. (3) ¿Qué razones hacen confiable una predicción? (4) Tomás tiene razones más fáciles de revisar, pero un dato puede fallar.",
        ["separa afirmación y razón", "formula una pregunta sobre el conocimiento", "concluye sin juzgar a las personas"], ["cuatro líneas numeradas"], ["confundir acertar con saber", "juzgar el carácter de las personas"],
        "Pide que indique qué dato nuevo cambiaría su conclusión."),
    reinforce="Escribe una afirmación que hayas oído esta semana y sepárala en afirmación y razones.",
    extend="Anota una creencia tuya y qué razones la sostienen; luego, qué te haría dudar de ella.",
)

# ============================================================ OA 04, clase 2
F = ("Ficha 2 (cuatro afirmaciones de ejemplo): (1) «El agua del vaso está a 20 grados»: tres personas midieron con un termómetro y obtuvieron lo mismo. "
     "(2) «Esa película es la mejor de la década»: lo dice un espectador. (3) «Cinco más siete es doce»: se deduce de lo que significa sumar. "
     "(4) «La plaza cerrará el lunes»: lo dice una vecina, sin mostrar documento alguno.")
build(
    O4, 2, F,
    use="Aprenderé a definir conocimiento, verdad, justificación, evidencia, ciencia y refutación, y a distinguir de dónde viene cada afirmación.",
    prior=["Sé que creer no es lo mismo que saber.", "Sé que una razón puede revisarse.", "Sé distinguir hecho de opinión."],
    explain=[
        "Una definición clásica dice que conocer es tener una creencia verdadera y justificada. La verdad significa que lo que se afirma coincide con cómo son las cosas. La justificación son las razones o la evidencia, es decir, los datos o pruebas que respaldan la afirmación. Esta definición se discute, pero sirve para empezar: si falta la verdad, la justificación o la creencia, no hay conocimiento.",
        "Las afirmaciones tienen fuentes. La experiencia usa los sentidos o instrumentos (medir con un termómetro). La razón deduce a partir de ideas (la suma de números). El testimonio depende de lo que dice otra persona. Una opinión expresa un gusto, como «la mejor película», y no se prueba como un dato. Cada fuente tiene fortalezas y límites.",
        "La ciencia es un conocimiento que se apoya en observaciones y pruebas que otras personas pueden repetir. Una afirmación científica es refutable: se puede imaginar un dato que la contradiga. Si ningún dato posible podría contradecirla, no se puede comprobar. Que una afirmación sea refutable no la hace falsa; la hace comprobable.",
    ],
    vocab=[("conocimiento", "creencia verdadera y justificada, según una definición clásica"), ("verdad", "coincidencia entre lo que se afirma y cómo son las cosas"), ("evidencia", "datos o pruebas que respaldan una afirmación"), ("refutable", "que se puede imaginar un dato que la contradiga"), ("testimonio", "información que depende de lo que dice otra persona")],
    worked=[
        ("Identificar la fuente", "«En mi pieza hay 3 metros entre la cama y la puerta», dice Marta de ejemplo tras medirlo con una huincha. ¿De qué fuente viene?", ["Usó un instrumento para medir.", "Eso es observación y medición, es decir, experiencia."], "Experiencia"),
        ("Revisar si es refutable", "Un compañero de ejemplo dice: «Esta pulsera trae suerte, aunque a veces no se note». ¿Es refutable?", ["Si no se nota, nada la contradice.", "Ningún dato podría mostrar que está equivocado."], "No es refutable: no se puede comprobar"),
    ],
    mistakes=[("Pensar que una opinión sincera es conocimiento.", "La sinceridad no es justificación ni verdad.", "Pregunta qué evidencia la respalda y quién podría comprobarla."),
              ("Creer que una afirmación refutable ya está refutada.", "Se confunde poder comprobar con ser falsa.", "Refutable significa que podría fallar ante un dato; puede seguir resistiendo.")],
    T=[
        ('abc', '¿Qué es la verdad, según la definición de esta clase?', 'La coincidencia entre lo que se afirma y cómo son las cosas', 'La creencia que comparte la mayoría de las personas de un grupo', 'La afirmación que alguien sostiene con mucha seguridad', 'La verdad no depende de cuántos crean algo ni de qué tan segura sea una persona.'),
        ('abc', '{F} ¿De qué fuente viene la afirmación 1?', 'De la experiencia, mediante una medición', 'De la razón, mediante una deducción hecha sin ningún instrumento', 'Del testimonio de una persona', 'Hay un termómetro y tres personas que midieron: se apoya en observación e instrumentos.'),
        ('abc', '{F} ¿De qué fuente viene la afirmación 3?', 'De la razón, porque se deduce del significado de sumar', 'De la experiencia, porque alguien contó objetos', 'Del testimonio de quien la dijo en voz alta', 'Se obtiene pensando en lo que significa sumar, sin necesitar medir nada.'),
        ('abc', '{F} ¿Por qué la afirmación 2 no es un dato como la 1?', 'Porque expresa un gusto y no hay forma de medirla o comprobarla', 'Porque habla de una película y no de objetos medibles', 'Porque la dijo una sola persona y por eso no puede tener ningún valor', 'Una opinión de gusto no se prueba con evidencia; que sea de una persona no la hace falsa.'),
        ('abc', '{F} La afirmación 4 depende de lo que dice una vecina. ¿Qué fuente es?', 'Testimonio', 'Experiencia', 'Razón', 'Se acepta por lo que dice otra persona y no se muestra documento alguno.'),
        ('abc', '¿Qué es la evidencia?', 'Datos o pruebas que respaldan una afirmación', 'La seguridad con que una persona sostiene lo que cree', 'La opinión que más se repite en las redes sociales', 'La evidencia es lo que respalda una afirmación y puede revisarse; la seguridad o la repetición no la reemplazan.'),
        ('abc', '{F} ¿Qué haría más confiable la afirmación 4?', 'Que se mostrara un documento oficial que anuncie el cierre', 'Que la vecina repitiera la frase con más seguridad', 'Que otra vecina dijera lo mismo sin ninguna fuente', 'Un documento verificable es evidencia; repetir con seguridad o sumar rumores no agrega justificación.'),
        ('abc', 'Alguien afirma: «Todos los gatos de mi calle están en casa a las 8, y ningún dato podría mostrarme lo contrario». ¿Qué falla en esta afirmación?', 'Si nada puede contradecirla, no se puede comprobar', 'Es una opinión de gusto, y por eso no se puede comprobar', 'Es un testimonio y por eso carece de valor', 'Una afirmación comprobable debe poder fallar ante un dato; esta se blinda a sí misma.'),
        ('abc', '¿Qué significa que una afirmación sea refutable?', 'Que se puede imaginar un dato que la contradiga', 'Que ya fue refutada con datos y debe descartarse', 'Que nadie puede pensar en un caso que la ponga a prueba', 'Refutable es poder fallar ante un dato posible; no equivale a estar equivocada.'),
        ('abc', '{F} ¿Cuál afirmación se justifica con una medición hecha con un instrumento que otras personas pueden repetir?', 'La 1, porque hay mediciones repetidas por tres personas', 'La 2, porque el espectador está seguro de lo que dice y lo repite con firmeza', 'La 4, porque una vecina suele estar bien informada', 'Solo la 1 se apoya en mediciones repetibles; la 3 se deduce sin medir y las otras dependen de gusto o de palabra no comprobada.'),
        ('abc', 'Un estudiante afirma: «Creo con total sinceridad que mi equipo ganó el torneo de ejemplo». El equipo perdió. ¿Había conocimiento?', 'No, porque lo creído era falso aunque la creencia fuera sincera', 'Sí, porque creerlo con sinceridad y honestidad es suficiente para saberlo', 'Sí, porque tenía razones aunque el resultado fuera otro', 'Sin verdad no hay conocimiento: la sinceridad no convierte en verdadero lo que no lo es.'),
        ('Una persona dice: «Lo que repito mucho se vuelve cierto». ¿Cuál de las tres condiciones del conocimiento confunde?', 'La verdad con la repetición', 'Repetir no cambia cómo son las cosas: la verdad depende de la coincidencia con los hechos, no de cuántas veces se diga.'),
        ('abc', '{F} ¿Qué límite tiene confiar en la afirmación 1 sin revisar nada más?', 'El termómetro podría estar mal calibrado y las tres mediciones repetir el mismo error', 'Que tres personas son muy pocas para medir una temperatura', 'Que un termómetro es un instrumento y los instrumentos no dan evidencia', 'Un instrumento defectuoso falla igual en cada medición; revisar el instrumento es parte de la justificación.'),
    ],
    ctx=('abc', 'Una compañera de ejemplo dice: «Las plantas de mi casa crecen más cuando les hablo». Ha medido cada semana el alto de dos plantas iguales, una a la que habla y otra no. ¿Qué dato haría más sólida su afirmación?', 'Que otras personas repitan la medición con el mismo cuidado', 'Que ella insista más en que lo ha comprobado', 'Que sus amigas y familiares digan que les parece creíble y lo compartan', 'La repetición por otras personas es lo que permite comprobar; la insistencia y la simpatía no cuentan como evidencia.'),
    sc=[
        ('En Filosofía: ¿qué significa que una afirmación sea refutable?', 'Que se puede imaginar un dato que la contradiga', 'Es la condición para poder comprobarla con datos.'),
        ('abc', '¿Cuál es un ejemplo de testimonio?', 'Una persona cuenta que vio cerrar una tienda', 'Un termómetro marca 20 grados', 'Se deduce que 3 + 4 es 7', 'El testimonio es lo que dice otra persona; el termómetro es experiencia y la suma es razón.'),
        ('¿Qué dos condiciones, además de creer, forman el conocimiento en la definición clásica?', 'Que sea verdadero y esté justificado', 'La definición clásica pide verdad y justificación además de la creencia.'),
    ],
    op=("Usa la {F} Ordena las cuatro afirmaciones de la más a la menos justificada, y para cada una escribe la fuente y una razón breve. Termina con una forma de comprobar la afirmación 4.",
        "1 (experiencia, tres mediciones), 3 (razón, deducción), 4 (testimonio, sin documento), 2 (opinión de gusto, no comprobable). Comprobar la 4: pedir el documento oficial del cierre.",
        ["nombra la fuente de cada una", "justifica el orden con evidencia", "propone una comprobación posible"], ["lista ordenada de cuatro filas", "una comprobación"], ["tratar la opinión como dato", "no indicar cómo comprobar"],
        "Pregunta qué cambiaría si la afirmación 3 se probara con un ejemplo y no con una deducción."),
    reinforce="Redacta una afirmación de cada tipo: experiencia, razón, testimonio y opinión.",
    extend="Busca una afirmación de tu entorno que no sea refutable y explica por qué.",
)

# ============================================================ OA 04, clase 3
F = ("Ficha 3 (tres posturas de ejemplo, resumidas): "
     "Postura R: «Algunas verdades las alcanzo pensando, no mirando: que un cuadrado tiene cuatro lados iguales lo sé sin medir ningún cuadrado. Los sentidos a veces engañan: un lápiz parece quebrado dentro del agua.» "
     "Postura E: «Todo lo que sé lo aprendí viendo, oyendo y tocando. Nadie conoce el sabor de una fruta sin probarla.» "
     "Postura S: «Como los sentidos y la razón pueden fallar, no debo afirmar nada con total certeza; reviso cada creencia.»")
build(
    O4, 3, F,
    use="Aprenderé a reconstruir con fidelidad tres perspectivas sobre el origen del conocimiento (racional, empírica y escéptica) y a señalar sus límites.",
    prior=["Sé que el conocimiento se apoya en razones.", "Sé que hay fuentes como la experiencia y la razón.", "Sé que una perspectiva se evalúa con evidencia."],
    explain=[
        "Reconstruir una perspectiva es exponerla con fidelidad: se dice cuál es su tesis, qué razones da, qué ejemplo usa y qué límite tiene, sin deformarla para que sea más fácil criticarla. Deformarla es cometer la falacia del hombre de paja, que consiste en atacar una versión exagerada de lo que otro dijo.",
        "El racionalismo sostiene que la razón es la fuente principal del conocimiento seguro: ciertas verdades, como las de la geometría, se alcanzan pensando. El empirismo sostiene que el conocimiento nace de la experiencia, es decir, de lo que percibimos por los sentidos. El escepticismo propone dudar o suspender el juicio cuando las razones no bastan, y examinar cada creencia.",
        "Cada perspectiva tiene un límite que las otras señalan. Al racionalismo se le pregunta cómo la razón sola conoce hechos del mundo; al empirismo, cómo explica verdades que no dependen de lo que se mide y por qué confiar en sentidos que a veces fallan; al escepticismo, si puede vivir sin aceptar nada. Hablamos de posturas generales: no hace falta atribuirlas a una persona concreta.",
    ],
    vocab=[("racionalismo", "postura que sostiene que la razón es la fuente principal del conocimiento seguro"), ("empirismo", "postura que sostiene que el conocimiento nace de la experiencia"), ("escepticismo", "postura que propone dudar o suspender el juicio cuando las razones no bastan"), ("reconstruir una perspectiva", "exponerla con fidelidad: tesis, razones, ejemplo y límite"), ("hombre de paja", "falacia que consiste en atacar una versión exagerada de lo que otro dijo")],
    worked=[
        ("Identificar la postura", "Un estudiante de ejemplo dice: «Que dos más dos es cuatro lo sé pensando; no necesito contar manzanas». ¿Qué postura expresa?", ["Apela a la razón y no a la experiencia.", "Eso corresponde al racionalismo."], "Racionalismo"),
        ("Reconstruir con fidelidad", "Una compañera de ejemplo resume la postura E como «los empiristas creen que nunca hay que pensar». ¿Es fiel?", ["La postura E dice que el conocimiento nace de la experiencia.", "No dice que no haya que pensar; el resumen la exagera."], "No es fiel: es un hombre de paja"),
    ],
    mistakes=[("Resumir una postura con la versión más débil para refutarla fácil.", "Se comete la falacia del hombre de paja.", "Reconstruye la tesis y las razones tal como las daría quien la sostiene."),
              ("Creer que el escepticismo niega que exista algo verdadero.", "Se confunde dudar con negar.", "El escepticismo propone examinar las razones y suspender el juicio cuando no bastan.")],
    T=[
        ('abc', '{F} ¿Qué postura sostiene que el conocimiento nace de la experiencia?', 'La postura E, empirista', 'La postura R, racionalista', 'La postura S, escéptica', 'La postura E afirma que todo lo que sabe lo aprendió viendo, oyendo y tocando.'),
        ('abc', '{F} ¿Qué ejemplo usa la postura R para apoyar su tesis?', 'Que un cuadrado tiene cuatro lados iguales, sabido sin medir', 'Que una fruta solo se conoce probándola uno mismo con los propios sentidos', 'Que dudar de todo evita equivocarse', 'El ejemplo del cuadrado muestra una verdad alcanzada pensando; la fruta es de la postura E.'),
        ('abc', '{F} ¿Qué razón da la postura S para dudar?', 'Que los sentidos y la razón pueden fallar', 'Que los sentidos siempre muestran la realidad completa', 'Que nada de lo que se piensa puede ser verdadero', 'Para S, como ambas fuentes pueden fallar, conviene revisar cada creencia; no niega toda verdad.'),
        ('abc', '¿Qué es reconstruir una perspectiva?', 'Exponer su tesis, razones, ejemplo y límite de forma fiel', 'Resumirla para mostrar rápido por qué está equivocada', 'Reemplazarla por otra que parezca más convincente', 'Reconstruir es entender y exponer sin deformar; refutar viene después.'),
        ('abc', '{F} Un compañero resume la postura R así: «Los racionalistas creen que no hay que mirar el mundo». ¿Qué error comete?', 'Exagera R, que solo dice que algunas verdades se alcanzan pensando', 'Resume bien, porque R rechaza los sentidos por completo', 'Cambia la postura R por la postura E sin darse cuenta', 'R dice que algunas verdades se alcanzan pensando y que los sentidos a veces engañan: no que no deba mirarse el mundo.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la postura E?', 'Cómo explica verdades que se deducen sin medir, como las del cuadrado', 'Cómo es posible que un racionalista dude de los sentidos y aun así use la razón', 'Por qué las frutas tienen sabores distintos', 'La objeción a E es cómo da cuenta de verdades que no dependen de lo percibido.'),
        ('abc', '{F} ¿Qué límite se le puede plantear a la postura R?', 'Cómo puede la razón sola conocer hechos particulares, como cuánto llovió', 'Cómo alguien puede aprender cualquier cosa sin usar ningún sentido del cuerpo', 'Por qué dudar de todo evita los errores', 'Un límite de R es explicar hechos del mundo que parecen requerir observación.'),
        ('abc', '{F} ¿Qué punto en común tienen las posturas R y S?', 'Desconfían de los sentidos cuando estos pueden engañar', 'Aceptan la experiencia como única fuente fiable', 'Sostienen que la duda es innecesaria', 'Ambas señalan que los sentidos pueden fallar; R confía en la razón y S pide examinar todo.'),
        ('abc', '{F} Una persona dice: «Según S, no existe nada». ¿Es fiel a la postura S?', 'No: S propone suspender el juicio, no negar que algo exista', 'Sí: dudar de todo equivale a negar todo lo que podría ser conocido', 'Sí: S sostiene que solo existen las ideas', 'Dudar no es negar: S no afirma ni niega mientras faltan razones.'),
        ('abc', 'Una estudiante prueba una receta de ejemplo cuatro veces antes de afirmar que sale mejor con menos azúcar. ¿Qué postura refleja su método?', 'Empirista, porque se apoya en la experiencia repetida', 'Racionalista, porque se basa en razonar sin probar', 'Escéptica, porque se niega a afirmar algo', 'Su fuente es probar y observar, que es la experiencia.'),
        ('abc', '{F} ¿Qué dato haría más difícil sostener la postura E sin revisarla?', 'Que haya verdades como las del cuadrado que se aceptan sin medir', 'Que una persona nueva pruebe una fruta que no conocía y le guste mucho', 'Que los sentidos funcionen bien en general', 'Hay verdades que parecen no depender de lo percibido: eso presiona a E a explicarlas.'),
        ('{F} Escribe una pregunta que la postura S podría hacer a la postura R.', '¿Cómo sabes que tu razonamiento no se equivoca?', 'S pide revisar la fiabilidad de cada fuente, también de la razón.'),
        ('abc', '{F} ¿Qué respuesta daría R a la pregunta «¿cómo explicas lo que aprendes viendo y tocando?»', 'Que la experiencia da datos, pero la razón los ordena y asegura algunas verdades', 'Que la experiencia es la única fuente de conocimiento y que razonar no agrega nada a lo percibido', 'Que no existe ninguna forma de comprobar lo que se percibe', 'R puede aceptar que se aprende con los sentidos y sostener que la razón alcanza ciertas verdades seguras.'),
    ],
    ctx=('abc', 'Dos amigos de ejemplo discuten si hay vida en otros planetas. Uno dice: «Mientras no haya evidencia no afirmo ni niego». ¿Qué actitud muestra?', 'Escepticismo, porque suspende el juicio sin razones suficientes', 'Empirismo, porque rechaza la existencia de lo que no ve', 'Racionalismo, porque deduce la respuesta sin necesidad de observar nada', 'Suspender el juicio es la actitud escéptica; negar sería otra posición.'),
    sc=[
        ('En Filosofía: ¿qué sostiene el empirismo?', 'Que el conocimiento nace de la experiencia', 'Pone la experiencia, es decir lo que percibimos, como origen del conocimiento.'),
        ('abc', '¿Qué es el hombre de paja?', 'Atacar una versión exagerada de lo que otro dijo', 'Aceptar una tesis solo porque la dice la mayoría', 'Dudar de todo sin dar razones', 'Consiste en deformar la postura del otro para refutarla con facilidad.'),
        ('¿Qué tres partes de una postura conviene exponer al reconstruirla, además de la tesis?', 'Las razones, un ejemplo y un límite', 'Para exponerla bien se muestran las razones, se da un ejemplo y se señala su límite.'),
    ],
    op=("Usa la {F} Reconstruye en cinco líneas la postura que elijas: tesis, una razón, un ejemplo, un límite y una pregunta que le harías. No digas cuál te parece mejor.",
        "Postura E: tesis, el conocimiento nace de la experiencia. Razón: nadie conoce un sabor sin probarlo. Ejemplo: la fruta. Límite: verdades como las del cuadrado. Pregunta: ¿cómo se explica que sepamos eso sin medir?",
        ["expone la tesis sin deformarla", "incluye razón, ejemplo y límite", "formula una pregunta"], ["cinco líneas"], ["caricaturizar la postura", "opinar antes de reconstruir"],
        "Pide que cambie la pregunta por una objeción de otra postura."),
    reinforce="Escribe con tus palabras la tesis de cada postura en una línea.",
    extend="Piensa una situación diaria en que uses la razón y otra en que uses la experiencia.",
)

# ============================================================ OA 04, clase 4
F = ("Ficha 4 (argumento de ejemplo): Una publicación sin firma dice: «Un nuevo aceite hace crecer el pelo en una semana. Lo afirma una persona famosa, nadie ha publicado datos de lo contrario, y miles lo compartieron. Por lo tanto, el aceite funciona». "
     "Respuesta A: «No hay medición alguna; que sea famoso y compartido no prueba el efecto». "
     "Respuesta B: «Debería probar el aceite una semana y medir el largo del pelo antes y después, comparando con alguien que no lo use».")
build(
    O4, 4, F,
    use="Aprenderé a formular una tesis sobre cuándo confiar en una afirmación y a evaluar si sus razones son verdaderas, relevantes y suficientes.",
    prior=["Sé que creer no es saber.", "Sé distinguir experiencia, razón y testimonio.", "Sé que la evidencia debe poder revisarse."],
    explain=[
        "Un argumento es un conjunto de razones, llamadas premisas, que apoyan una conclusión. La tesis es la conclusión que se defiende. Evaluar un argumento significa revisar tres cosas: si las premisas son verdaderas o probables, si son relevantes para la conclusión y si son suficientes para sostenerla.",
        "Un argumento es débil cuando sus razones no tienen relación con la conclusión. Que algo sea famoso, o que muchas personas lo compartan, es una razón irrelevante para saber si funciona. Tampoco basta decir «nadie ha demostrado lo contrario»: la ausencia de pruebas en contra no es una prueba a favor. Es la falacia de apelar a la ignorancia, que da por cierto algo solo porque no se ha probado su falsedad. Tampoco basta un solo caso, como el de una persona que dice que le funcionó: de un caso no se puede generalizar a todos.",
        "Para apoyar una tesis con evidencia sirve diseñar una comprobación: medir antes y después, y comparar con un grupo que no recibe el producto. Esa comparación permite que otras personas repitan la prueba. Siempre conviene decir hasta dónde llega la conclusión: «los datos sugieren…» en vez de «está probado».",
    ],
    vocab=[("premisa", "razón que se ofrece para apoyar una conclusión"), ("tesis", "conclusión que se defiende en un argumento"), ("relevante", "que tiene relación con lo que se quiere probar"), ("suficiente", "que alcanza para sostener la conclusión"), ("apelar a la ignorancia", "dar por cierto algo porque no se ha probado que sea falso")],
    worked=[
        ("Evaluar relevancia", "Argumento de ejemplo: «Esta app es buena porque muchas personas la descargaron». ¿Es relevante la razón?", ["La cantidad de descargas no dice si la app funciona bien.", "Es una razón poco relevante para la conclusión."], "No es relevante para decir que funciona"),
        ("Proponer una comprobación", "Una amiga de ejemplo dice que una app mejora la concentración. ¿Cómo comprobarlo?", ["Medir tiempo de estudio antes y después.", "Comparar con alguien que no la use."], "Medir antes y después y comparar con quien no la usa"),
    ],
    mistakes=[("Aceptar un argumento porque tiene muchas razones.", "La cantidad no reemplaza la calidad ni la relevancia.", "Revisa una por una si son verdaderas, relevantes y suficientes."),
              ("Pensar que lo que no se ha desmentido es verdadero.", "Se apela a la ignorancia.", "Pide pruebas a favor, no solo ausencia de pruebas en contra.")],
    T=[
        ('abc', '¿Qué es una premisa?', 'Una razón que se ofrece para apoyar una conclusión', 'La conclusión que se busca defender en un argumento', 'Una opinión que no necesita ninguna razón', 'Las premisas son las razones; la conclusión es lo que ellas apoyan.'),
        ('abc', '{F} ¿Cuál es la tesis del argumento de la publicación?', 'Que el aceite funciona', 'Que una persona famosa es confiable', 'Que miles compartieron la publicación', 'La conclusión que se defiende es que el aceite funciona; lo demás son razones.'),
        ('abc', '{F} ¿Qué razón de la publicación es irrelevante para saber si el aceite funciona?', 'Que miles de personas lo compartieron', 'Que el pelo crezca en una semana según la publicación', 'Que no hay datos publicados', 'Compartir no dice nada sobre el efecto en el pelo.'),
        ('abc', '{F} La razón «nadie ha publicado datos de lo contrario» comete…', 'El error de apelar a la ignorancia', 'El error de atacar a la persona que habla', 'El error de generalizar un solo caso a todos', 'Se da por cierto algo porque no se ha probado que sea falso.'),
        ('abc', '{F} ¿Qué crítica hace la respuesta A?', 'Que la fama y los compartidos no prueban el efecto y falta una medición', 'Que la persona famosa miente porque quiere vender', 'Que el aceite no puede funcionar bajo ninguna condición posible y nunca lo hará', 'Señala razones irrelevantes y falta de datos, sin atacar a nadie ni afirmar lo contrario.'),
        ('abc', '{F} ¿Qué propone la respuesta B para comprobar la tesis?', 'Medir antes y después y comparar con alguien que no use el aceite', 'Preguntar a quienes lo compartieron si les gustó y si lo recomendarían a otras personas', 'Esperar a que alguien publique datos en contra', 'Una comparación medida permite que otros repitan la prueba.'),
        ('abc', '{F} ¿Qué conclusión sería adecuada con los datos de la publicación?', 'No hay evidencia suficiente para afirmar que funciona', 'Es seguro que el aceite no funciona y que la publicación miente', 'Funciona, porque muchas personas lo comparten', 'Con razones irrelevantes y ningún dato solo se puede decir que falta evidencia, no que sea falso.'),
        ('abc', 'Un estudiante dice: «Mi tesis es que el sueño ayuda a rendir mejor; mi única razón es que lo siento así». ¿Qué falla?', 'La razón es subjetiva y no alcanza para sostener la tesis', 'La tesis es falsa, porque dormir no sirve para rendir', 'Falta una opinión de alguien famoso que la respalde', 'Una sensación personal no puede revisarse desde fuera: es insuficiente.'),
        ('abc', 'Para evaluar un argumento, ¿qué tres cosas se revisan?', 'Si las premisas son verdaderas, relevantes y suficientes', 'Si es corto, claro y tiene muchos ejemplos', 'Si lo dijo alguien con experiencia, popular y seguro', 'Esas tres condiciones miden la calidad de las razones; el resto es forma o prestigio.'),
        ('abc', '{F} ¿Por qué es útil comparar con alguien que no use el aceite?', 'Porque permite ver si el cambio se debe al aceite y no a otra causa', 'Porque así se demuestra que el aceite no funciona y nunca funcionó para nadie', 'Porque los resultados de una persona valen más que los de dos', 'Sin comparación, el crecimiento podría deberse a otras causas.'),
        ('abc', 'Una compañera dice: «Probé el aceite una semana y me creció el pelo, así que funciona para todos». ¿Qué error hay?', 'Generaliza un solo caso a todas las personas', 'Usa un instrumento de medición equivocado', 'Atribuye la tesis a una persona famosa', 'Un solo caso no basta para una conclusión general.'),
        ('{F} Escribe una frase que exprese la conclusión con prudencia sobre el aceite.', 'Los datos disponibles sugieren que no hay evidencia suficiente de que funcione.', 'Usa «sugieren» y reconoce el límite de la evidencia en vez de afirmar algo seguro.'),
        ('abc', '{F} ¿Qué dato podría refutar la tesis si se hiciera la prueba de la respuesta B?', 'Que el pelo de quien usa el aceite y el de quien no lo usa crezca igual', 'Que la persona famosa deje de promocionar el aceite', 'Que más personas compartan la publicación y la comenten en sus redes sociales', 'Si no hay diferencia entre quienes lo usan y quienes no, el efecto no está respaldado.'),
    ],
    ctx=('abc', 'Un compañero de ejemplo argumenta: «Confío en este canal de noticias porque nunca se ha demostrado que mienta». ¿Qué conviene responder?', 'Que no haber probado que miente no demuestra que diga la verdad', 'Que seguramente miente, porque todos los canales lo hacen', 'Que la confianza es una cuestión de gusto personal', 'No tener pruebas en contra no es evidencia a favor; ni se asume mentira ni se reduce a gusto.'),
    sc=[
        ('En Filosofía: ¿qué es una tesis?', 'La conclusión que se defiende en un argumento', 'Es lo que se quiere probar con las razones.'),
        ('abc', '¿Qué significa que una razón sea suficiente?', 'Que alcanza para sostener la conclusión', 'Que muchas personas la repiten', 'Que tiene relación con el tema', 'Suficiente es que basta para apoyar la conclusión; tener relación es solo ser relevante.'),
        ('¿Por qué conviene decir «los datos sugieren» en vez de «está probado»?', 'Porque la evidencia puede ser incompleta y reconocer su límite es más honesto', 'Muestra hasta dónde llega la evidencia y deja abierta su revisión.'),
    ],
    op=("Usa la {F} Escribe un comentario de cinco líneas: tesis de la publicación; dos razones y si son relevantes; una falla; una prueba para comprobarla; una conclusión prudente. No ataques a la persona famosa.",
        "Tesis: el aceite funciona. Razones: la fama y los compartidos (irrelevantes). Falla: apela a la ignorancia. Prueba: medir antes y después, con comparación. Conclusión: falta evidencia para afirmarlo.",
        ["identifica tesis y razones", "evalúa relevancia", "propone una prueba", "concluye con prudencia"], ["cinco líneas"], ["atacar a la persona", "decir que es falso sin pruebas"],
        "Pregunta qué otros datos harían cambiar su conclusión."),
    reinforce="Elige un aviso o publicación de ejemplo y escribe su tesis y sus razones.",
    extend="Diseña una comprobación sencilla para una afirmación de tu vida diaria.",
)
