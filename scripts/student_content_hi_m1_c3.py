"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 23 (respuestas políticas ante problemas sociales: la cuestión social y otros conflictos actuales)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 23"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = ("Ficha de ejemplo, ciudad industrial ficticia hacia 1900: jornada de trabajo, 12 horas al día durante 6 días a la semana; "
      "salario de un obrero, 3 unidades de dinero de la época por día trabajado (dato de ejemplo); gasto mínimo de alimentación de una familia, 4 unidades por día, los 7 días de la semana; "
      "vivienda típica, una pieza de conventillo (casa de piezas pequeñas alrededor de un patio) de 12 metros cuadrados donde viven 6 personas; "
      "no existía seguro obligatorio por enfermedad ni por vejez.")
build(
    OA, 1, F1,
    use="Aprenderé a situar la «cuestión social» en el tiempo y el espacio y a reconocer el problema que motivó respuestas políticas distintas. Sirve para entender por qué surgieron corrientes como el liberalismo, el socialismo y el socialcristianismo.",
    prior=["Sé qué fue la industrialización y la migración del campo a la ciudad.", "Sé calcular multiplicaciones y restas sencillas.", "Sé que una fuente tiene fecha y lugar."],
    explain=[
        "La «cuestión social» es el nombre que se dio, a fines del siglo XIX y comienzos del XX, al conjunto de problemas que afectaban a los obreros y a los sectores populares de las ciudades industriales: salarios bajos, jornadas muy largas, viviendas pequeñas e insalubres, enfermedades, falta de seguros y escasa educación. Surgió con la industrialización, que es el paso a una producción hecha en fábricas con máquinas, y con la urbanización, que es el crecimiento de las ciudades por la llegada de población desde el campo.",
        "Los problemas eran sociales y no solo personales: afectaban a muchas familias a la vez y tenían causas comunes, como la falta de leyes laborales, el bajo valor del trabajo y la rápida llegada de población a ciudades que no estaban preparadas. Por eso se discutió si debían resolverlos las familias, las empresas, la caridad, el Estado o los propios trabajadores organizados.",
        "A esas preguntas respondieron distintas corrientes políticas, es decir, conjuntos de ideas sobre cómo debe organizarse la sociedad y qué papel debe tener el Estado. Cada una dio su propia respuesta al mismo problema. Para estudiarlas se comienza por situar el problema: cuándo ocurrió, dónde y a quiénes afectó, y qué datos permiten medirlo.",
    ],
    vocab=[("cuestión social", "conjunto de problemas de obreros y sectores populares de las ciudades industriales"), ("industrialización", "paso a una producción hecha en fábricas con máquinas"), ("urbanización", "crecimiento de las ciudades por la llegada de población desde el campo"), ("conventillo", "casa con muchas piezas pequeñas alrededor de un patio común"), ("corriente política", "conjunto de ideas sobre cómo organizar la sociedad y el papel del Estado")],
    worked=[
        ("Calcular horas de trabajo", "En otra ciudad ficticia, un obrero trabaja 10 horas al día durante 6 días a la semana. ¿Cuántas horas trabaja por semana?",
         ["Multiplico las horas diarias por los días.", "10 × 6 = 60."], "60 horas por semana"),
        ("Calcular espacio por persona", "Una pieza de ejemplo de 20 metros cuadrados es habitada por 5 personas. ¿Cuántos metros cuadrados corresponden a cada una?",
         ["Divido el espacio entre las personas.", "20 ÷ 5 = 4."], "4 metros cuadrados por persona"),
    ],
    mistakes=[
        ("Creer que los problemas de los obreros eran solo mala suerte personal.", "Afectaban a muchas familias a la vez y tenían causas comunes, como la falta de leyes laborales.", "Busca datos que muestren que el problema era general."),
        ("Pensar que la cuestión social ocurrió en una sola ciudad.", "Apareció en muchas ciudades industriales y mineras, con rasgos propios de cada lugar.", "Ubica siempre el lugar y la fecha del problema."),
    ],
    T=[
        ("En Historia: ¿qué fue la «cuestión social»?", "El conjunto de problemas de los obreros y sectores populares de las ciudades industriales", "Incluía salarios, jornadas y vivienda."),
        ("=", "{F} ¿Cuántas horas semanales trabajaba el obrero de la ficha?", "12*6", "Se multiplican las horas diarias por los días."),
        ("En Historia: ¿qué es un conventillo? A) una casa de muchas piezas pequeñas alrededor de un patio, B) una fábrica de textiles.", "A", "Era una vivienda popular de la ciudad."),
        ("{F} ¿Qué tipo de problemas muestra la ficha? A) laborales, de vivienda y de protección ante la enfermedad, B) solo problemas de transporte.", "A", "Habla de jornada, pieza y falta de seguros."),
        ("¿Qué proceso trajo población del campo a las ciudades industriales? A) la urbanización, B) la deflación.", "A", "Es el crecimiento de las ciudades por la llegada de población."),
        ("{F} Un empresario afirma: «Si no alcanza el dinero, es porque los obreros no saben ahorrar». ¿Qué dato de la ficha contradice la idea? A) el gasto de alimentación era mayor que el salario, B) la pieza tenía 12 metros cuadrados.", "A", "El salario diario era menor que el gasto de alimentación."),
        ("=", "{F} ¿Cuántos metros cuadrados corresponden a cada persona en la pieza?", "12//6", "Se divide el espacio entre las personas."),
        ("=", "{F} ¿Cuánto ganaba un obrero en una semana de 6 días de trabajo (en unidades de la época)?", "3*6", "Se multiplica el salario diario por los días."),
        ("=", "{F} ¿Cuánto gastaba la familia en alimentación en una semana de 7 días (en unidades)?", "4*7", "Se multiplica el gasto diario por 7."),
        ("=", "{F} ¿Cuánto faltaba cada semana entre lo que ganaba el obrero y lo que gastaba en alimentación la familia (en unidades)?", "4*7-3*6", "Se resta el salario semanal al gasto semanal."),
        ("{F} ¿Por qué se habla de un problema social y no solo personal? A) porque afectaba a muchas familias con causas comunes, B) porque ocurría en un solo conventillo.", "A", "Las causas eran compartidas."),
        ("=", "{F} Si el salario subiera a 5 unidades por día y se trabajaran los 6 días, ¿cuánto sobraría por semana después de pagar la alimentación (en unidades)?", "5*6-4*7", "Se resta el gasto al nuevo salario semanal."),
        ("=", "{F} Si la jornada se redujera de 72 a 45 horas semanales, ¿cuántas horas menos trabajaría el obrero?", "12*6-45", "Se resta la jornada nueva a la jornada original de 72 horas."),
    ],
    ctx=("Un museo de ejemplo presenta una vitrina: «Salario diario de una costurera, 2 unidades; pan diario de su familia, 3 unidades». ¿Qué problema de la cuestión social muestra? A) un ingreso insuficiente para cubrir la alimentación, B) un exceso de dinero para gastar.", "A", "El ingreso es menor que el gasto necesario."),
    sc=[("En Historia: ¿qué es una corriente política?", "Un conjunto de ideas sobre cómo organizar la sociedad y el papel del Estado", "Cada corriente responde de una manera distinta."),
        ("¿Qué es la urbanización?", "El crecimiento de las ciudades por la llegada de población desde el campo", "Fue una causa de la cuestión social."),
        ("Nombra dos problemas de la cuestión social.", "Por ejemplo: salarios bajos y viviendas insalubres", "Están entre los problemas de la ficha.")],
    op=("{F} Escribe un texto corto que diga: dos problemas de la cuestión social que muestra la ficha, una causa que los explique y un dato con cifras (por ejemplo, las horas de trabajo o el metraje de la pieza). Termina con una pregunta que te permita saber cómo respondieron distintas corrientes a ese problema.",
        "Problemas: jornadas de 72 horas por semana y viviendas de 2 metros cuadrados por persona. Causa: falta de leyes laborales y crecimiento rápido de la ciudad. Pregunta: ¿qué propuso cada corriente política para mejorar el salario y la vivienda?",
        ["nombra dos problemas", "propone una causa", "usa una cifra", "formula una pregunta"], ["un texto con una cifra y una pregunta"], ["describir solo problemas personales", "no usar ninguna cifra"], "Léele tu texto a una persona de tu casa y pídele que diga si la pregunta final se puede responder con fuentes."),
    reinforce="Haz un cuadro con tres problemas de la cuestión social y una causa para cada uno.",
    extend="Explica por qué la industrialización pudo traer progreso y también problemas sociales.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = ("Cuatro textos de ejemplo, escritos para este ejercicio como resúmenes de ideas de distintas corrientes (no son citas reales; en la vida real hay que verificar autor, fecha y lugar). "
      "Texto A: «El progreso nace de la libertad: cada persona debe poder trabajar y contratar sin que el Estado intervenga; con más producción y comercio, los salarios irán subiendo.» "
      "Texto B: «Los trabajadores deben organizarse en sindicatos y partidos para conseguir leyes que reduzcan la jornada y protejan el salario.» "
      "Texto C: «El trabajo no es una mercancía cualquiera: el salario debe permitir vivir con dignidad a la familia, y patrones y obreros deben colaborar con justicia.» "
      "Texto D: «No hace falta un gobierno que mande: los trabajadores pueden organizar la producción por acuerdo libre entre ellos.»")
build(
    OA, 2, F2,
    use="Aprenderé a reconocer cinco corrientes políticas frente a la cuestión social y a leer textos que las expresan sin convertirlas en caricaturas. Sirve para entender sus ideas con fuentes y no con etiquetas.",
    prior=["Sé qué fue la cuestión social.", "Sé que una fuente tiene autor, fecha y propósito.", "Sé distinguir una idea principal de un ejemplo."],
    explain=[
        "Frente a la cuestión social surgieron varias respuestas. El liberalismo defiende la libertad individual, la propiedad privada y el mercado libre, y sostiene que el Estado debe intervenir poco. El socialismo busca más igualdad: propone que los trabajadores se organicen y que se cambien las leyes o la propiedad de las fábricas para repartir mejor la riqueza. El comunismo es una corriente socialista que propone abolir la propiedad privada de los medios de producción para llegar a una sociedad sin clases.",
        "El anarquismo rechaza la existencia del Estado y de toda autoridad impuesta, y plantea que los trabajadores se organicen por acuerdo libre y voluntario. El socialcristianismo, inspirado en la doctrina social de la Iglesia católica, defiende la dignidad del trabajador, un salario justo y la colaboración entre patrones y obreros, y se aleja tanto del liberalismo extremo como del socialismo revolucionario. Estas son descripciones generales, y dentro de cada corriente hay matices.",
        "Para leer un texto que expresa una corriente, pregunto quién lo escribió, cuándo y para qué, qué problema reconoce, qué solución propone y qué papel le da al Estado. También separo lo que el texto afirma de lo que yo creo, porque entender una idea no significa compartirla. Contrastar textos permite ver qué tienen en común y en qué se diferencian.",
    ],
    vocab=[("liberalismo", "corriente que defiende la libertad individual, la propiedad privada y un Estado que interviene poco"), ("socialismo", "corriente que busca más igualdad mediante la organización de los trabajadores y cambios en las leyes o la propiedad"), ("anarquismo", "corriente que rechaza el Estado y propone organizarse por acuerdo libre"), ("socialcristianismo", "corriente que defiende la dignidad del trabajador y la colaboración entre patrones y obreros"), ("comunismo", "corriente socialista que propone abolir la propiedad privada de los medios de producción")],
    worked=[
        ("Reconocer una postura", "Un texto de ejemplo dice: «Los trabajadores deben ser dueños de las fábricas». ¿A qué problema responde y a qué corriente se acerca más?",
         ["Habla de quién es dueño de las fábricas: la propiedad.", "Pedir que los trabajadores sean dueños se acerca al socialismo y al comunismo."], "Se acerca al socialismo o al comunismo"),
        ("Separar descripción y opinión", "Una frase de ejemplo dice: «El liberalismo defiende un Estado que interviene poco». ¿Es una descripción o una opinión?",
         ["Describe lo que defiende la corriente.", "No dice si es bueno o malo."], "Es una descripción"),
    ],
    mistakes=[
        ("Reducir una corriente a una burla o una sola palabra.", "Cada corriente tiene ideas y matices; una burla no la explica.", "Explica con una idea central y un ejemplo."),
        ("Creer que todas las corrientes querían lo mismo.", "Coinciden en que hay un problema, pero difieren en las causas y en las soluciones.", "Compara qué solución propone cada una."),
    ],
    T=[
        ("En Historia: ¿qué defiende el liberalismo? A) la libertad individual y un Estado que interviene poco, B) la desaparición de toda propiedad.", "A", "Es su idea central."),
        ("En Historia: ¿qué rechaza el anarquismo?", "La existencia del Estado y de toda autoridad impuesta", "Propone organizarse por acuerdo libre."),
        ("{F} ¿Qué texto propone que el Estado no intervenga en los contratos? A) el texto A, B) el texto B.", "A", "Dice que el Estado no debe intervenir."),
        ("{F} ¿Qué texto propone sindicatos y partidos para lograr leyes? A) el texto B, B) el texto D.", "A", "Habla de organizarse para conseguir leyes."),
        ("{F} ¿Qué texto habla de un salario que permita vivir con dignidad? A) el texto C, B) el texto A.", "A", "Pide un salario digno y colaboración."),
        ("{F} ¿Qué texto dice que no hace falta un gobierno que mande? A) el texto D, B) el texto C.", "A", "Es la idea del anarquismo."),
        ("{F} ¿Qué idea tienen en común los textos B y C? A) ambos reconocen que los salarios y las condiciones de los trabajadores deben mejorar, B) ambos piden eliminar el Estado.", "A", "Los dos buscan mejores condiciones, por vías distintas."),
        ("{F} ¿En qué se diferencian los textos A y B respecto del Estado? A) el A le asigna poco papel y el B espera que haga leyes, B) los dos le asignan el mismo papel.", "A", "Proponen soluciones distintas."),
        ("{F} Un compañero dice: «El texto C es socialista porque habla de obreros». ¿Qué le falta considerar? Responde con una frase.", "Que el texto C defiende la colaboración entre patrones y obreros y un salario justo, que es socialcristianismo", "Hablar de obreros no basta para clasificar la corriente."),
        ("{F} Para saber qué pedía cada corriente sobre la jornada de trabajo, ¿qué texto leerías? A) el B, porque habla de reducirla por ley, B) el D, porque habla de acuerdo libre.", "A", "El texto B menciona la jornada."),
        ("{F} Los cuatro textos son de ejemplo. ¿Qué tres datos habría que verificar si fueran fuentes reales? Responde con una frase.", "Quién los escribió, cuándo y en qué lugar", "Es lo que se pregunta a toda fuente."),
        ("{F} Una persona resume el texto A como «los liberales no se preocupaban de nadie». ¿Qué problema tiene ese resumen? A) es una caricatura, porque el texto dice que más producción subiría los salarios, B) es correcto.", "A", "Atribuye una intención que el texto no dice."),
        ("{F} Elige la conclusión mejor sostenida. A) los textos muestran distintas soluciones a un mismo problema, B) los textos prueban cuál corriente tenía razón.", "A", "Los textos no alcanzan para decidir cuál era la mejor."),
    ],
    ctx=("Para una exposición de ejemplo, un grupo debe elegir una frase que represente al socialcristianismo. Opciones: A) «El salario debe permitir vivir con dignidad y patrones y obreros deben colaborar», B) «Hay que suprimir el Estado». ¿Cuál elige?", "A", "Expresa la dignidad del trabajador y la colaboración."),
    sc=[("En Historia: ¿qué propone el socialismo en general?", "Más igualdad mediante la organización de los trabajadores y cambios en las leyes o la propiedad", "Es su idea central."),
        ("¿Qué defiende el socialcristianismo?", "La dignidad del trabajador, un salario justo y la colaboración entre patrones y obreros", "Se inspira en la doctrina social de la Iglesia."),
        ("¿Por qué conviene leer textos y no solo etiquetas?", "Porque los textos muestran las ideas reales y evitan caricaturas", "Una etiqueta no explica la postura.")],
    op=("{F} Elige dos de los cuatro textos y escribe para cada uno: qué problema reconoce, qué solución propone y qué papel le da al Estado. Termina con una frase que diga en qué coinciden y en qué se diferencian.",
        "Texto A: reconoce salarios bajos; propone libertad de contratar; poco papel del Estado. Texto B: reconoce jornadas largas; propone sindicatos y leyes; el Estado hace leyes. Coinciden en que hay problemas; se diferencian en la solución.",
        ["describe dos textos", "indica el papel del Estado", "compara coincidencias y diferencias"], ["dos textos analizados y una comparación"], ["resumir con burlas", "no mencionar el papel del Estado"], "Pide a una persona de tu casa que diga si entendió la diferencia entre los dos textos."),
    reinforce="Escribe una frase para cada corriente, con tus palabras y sin burlas.",
    extend="Explica por qué dos corrientes pueden coincidir en el problema y discrepar en la solución.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = ("Línea de tiempo con hechos reales, resumida: 1891, el papa León XIII publica la encíclica Rerum Novarum sobre la situación de los trabajadores; "
      "1906, en Chile se aprueba una ley sobre habitaciones obreras; "
      "1907, matanza en la Escuela Santa María de Iquique, durante una huelga de trabajadores del salitre en el norte de Chile; "
      "1912, Luis Emilio Recabarren funda en Iquique el Partido Obrero Socialista; "
      "1924, se aprueban en Chile las llamadas leyes sociales, con normas sobre contrato de trabajo, seguro obrero y organización sindical.")
build(
    OA, 3, F3,
    use="Aprenderé a ver cómo la cuestión social fue produciendo cambios en Chile y qué rasgos se mantuvieron, según el lugar. Sirve para entender que las respuestas políticas se vieron en leyes, organizaciones y conflictos concretos.",
    prior=["Conozco la cuestión social y las corrientes políticas.", "Sé calcular años entre dos fechas.", "Sé que una línea de tiempo ordena hechos."],
    explain=[
        "Las respuestas políticas a la cuestión social se expresaron con el tiempo en documentos, leyes, organizaciones y conflictos. En 1891 la Iglesia católica publicó la encíclica Rerum Novarum, un documento que defendió los derechos de los trabajadores y dio base al socialcristianismo. En Chile, una ley de 1906 intentó enfrentar el problema de las viviendas obreras. Estos hechos muestran que el Estado y otros actores comenzaron a reconocer el problema.",
        "El territorio importa. En la zona del salitre, en el norte, los trabajadores vivían lejos de las ciudades y dependían de las empresas, y allí ocurrió en 1907 la matanza de la Escuela Santa María de Iquique durante una huelga, un hecho que mostró la dureza del conflicto social. En 1912, también en Iquique, se fundó el Partido Obrero Socialista, un ejemplo de la organización política de los trabajadores.",
        "Hubo cambios: en 1924 se aprobaron leyes sociales que regularon contratos, seguros y sindicatos. Pero también hubo continuidades: los problemas de vivienda, salarios y desigualdad no desaparecieron de un día para otro. Para evaluar una respuesta política conviene preguntar qué cambió, qué se mantuvo, dónde ocurrió y quiénes participaron.",
    ],
    vocab=[("encíclica", "carta solemne del papa dirigida a la Iglesia o al mundo"), ("huelga", "suspensión colectiva del trabajo para exigir mejoras"), ("salitre", "mineral que se explotaba en el norte de Chile y se exportaba"), ("sindicato", "organización de trabajadores para defender sus intereses"), ("leyes sociales", "normas que protegen derechos de los trabajadores")],
    worked=[
        ("Calcular años entre dos hechos", "Si una ley se aprobó en 1900 y otra en 1915, ¿cuántos años pasaron entre ambas?",
         ["Resto el año menor al mayor.", "1915 - 1900 = 15."], "15 años"),
        ("Separar cambio y continuidad", "Antes de una ley de ejemplo no existía contrato de trabajo escrito, y después sí. Pero siguieron los salarios bajos. ¿Qué cambió y qué continuó?",
         ["Cambió la existencia del contrato escrito.", "Continuaron los salarios bajos."], "Cambió el contrato escrito; continuaron los salarios bajos"),
    ],
    mistakes=[
        ("Pensar que una ley resolvió de inmediato todos los problemas.", "Los problemas de salarios, vivienda y desigualdad continuaron durante años.", "Busca cambios y continuidades después de la ley."),
        ("Creer que la cuestión social ocurrió igual en todo el país.", "El norte salitrero tuvo rasgos propios, con trabajadores lejos de las ciudades.", "Ubica el lugar antes de generalizar."),
    ],
    T=[
        ("En Historia: ¿qué es una huelga?", "Una suspensión colectiva del trabajo para exigir mejoras", "Fue una forma de presión de los trabajadores."),
        ("{F} ¿Qué año se aprobaron las leyes sociales en Chile?", "1924", "La línea de tiempo lo informa."),
        ("{F} ¿Dónde ocurrió la matanza de la Escuela Santa María? A) en Iquique, B) en Concepción.", "A", "La línea la ubica en Iquique."),
        ("=", "{F} ¿Cuántos años pasaron entre Rerum Novarum y la matanza de Iquique?", "1907-1891", "Se resta el año menor al mayor."),
        ("=", "{F} ¿Cuántos años pasaron entre la ley de habitaciones obreras y las leyes sociales?", "1924-1906", "Se resta el año menor al mayor."),
        ("=", "{F} ¿Cuántos años pasaron entre la fundación del Partido Obrero Socialista y las leyes sociales?", "1924-1912", "Se resta el año menor al mayor."),
        ("{F} ¿Qué hecho de la línea se asocia al socialcristianismo? A) Rerum Novarum, B) la ley de 1924.", "A", "Es un documento de la Iglesia que defiende a los trabajadores."),
        ("{F} ¿Qué hecho muestra una forma de organización política de los trabajadores? A) la fundación del Partido Obrero Socialista, B) la ley sobre habitaciones obreras.", "A", "Es una organización creada por trabajadores."),
        ("{F} Un compañero dice: «Con las leyes de 1924 terminó la cuestión social». Con lo que sabes, ¿qué respuesta es mejor? A) hubo cambios, pero problemas como la vivienda y la desigualdad continuaron, B) es correcto, porque se aprobaron leyes.", "A", "Una ley no resuelve todo de inmediato."),
        ("{F} ¿Por qué la zona del salitre fue un escenario especial del conflicto? Responde con una frase.", "Porque los trabajadores vivían lejos de las ciudades, dependían de las empresas y allí se realizó una gran huelga", "El territorio influyó en cómo se vivió el conflicto."),
        ("{F} ¿Qué dos actores distintos aparecen respondiendo a la cuestión social? A) la Iglesia y los trabajadores organizados, B) solo los empresarios.", "A", "Rerum Novarum y el partido de 1912 lo muestran."),
        ("Una ciudad de ejemplo tenía 10.000 habitantes en 1890 y 25.000 en 1920. ¿Cuántos habitantes más tenía en 1920 y qué problema social puede explicar? A) 15.000 más; falta de viviendas, B) 5.000 más; exceso de viviendas.", "A", "25.000 menos 10.000 son 15.000 más."),
        ("=", "{F} ¿Cuántos años abarca la línea de tiempo completa, desde el primer hecho hasta el último?", "1924-1891", "Se resta el primer año al último."),
    ],
    ctx=("Un grupo de ejemplo prepara un mural con tres hechos: la huelga de 1907, la ley de 1906 y las leyes de 1924. Deben ponerlos en orden cronológico. ¿Cuál va primero? A) la ley de 1906, B) las leyes de 1924.", "A", "1906 es el año más antiguo."),
    sc=[("En Historia: ¿qué fue la matanza de la Escuela Santa María de Iquique?", "La muerte de trabajadores del salitre y sus familias durante una huelga en 1907", "Muestra la dureza del conflicto social."),
        ("¿Qué regularon las leyes sociales de 1924?", "Contrato de trabajo, seguro obrero y organización sindical", "Están en la línea de tiempo."),
        ("¿Por qué conviene distinguir cambios y continuidades?", "Porque las leyes mejoraron algunas cosas, pero otros problemas siguieron", "Así se evita exagerar los resultados.")],
    op=("{F} Elige tres hechos de la línea y escribe qué respuesta a la cuestión social representa cada uno, en qué lugar ocurrió (si se indica) y cuántos años lo separan del siguiente hecho elegido. Termina con una frase sobre qué cambió y qué continuó.",
        "Rerum Novarum (1891): respuesta de la Iglesia; 15 años antes de 1906. Ley de 1906: respuesta del Estado a la vivienda; 18 años antes de 1924. Leyes sociales (1924): contrato, seguro y sindicatos. Cambió la protección legal; continuó la desigualdad.",
        ["elige tres hechos", "indica el tipo de respuesta", "calcula los años", "distingue cambio y continuidad"], ["tres hechos con cálculos y una frase final"], ["no calcular los años", "afirmar que todo se resolvió"], "Pide a una persona de tu casa que compruebe tus restas."),
    reinforce="Dibuja una línea de tiempo con las cinco fechas y una palabra para cada una.",
    extend="Explica por qué el conflicto del salitre muestra la importancia del territorio en la cuestión social.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = ("Caso de ejemplo, fábrica ficticia «Textil Aurora» en una ciudad industrial ficticia hacia 1905: los trabajadores piden bajar la jornada de 12 a 10 horas al día y subir en 20 % su salario de 5 unidades diarias. "
      "Voz del dueño (de ejemplo, de ideas liberales): «Cada uno acuerda libremente su contrato; si subo los salarios, mi fábrica quiebra.» "
      "Voz de un dirigente sindical (de ejemplo, socialista): «Solo unidos y con leyes lograremos mejores condiciones.» "
      "Voz de un sacerdote (de ejemplo, socialcristiano): «El patrón debe un salario justo y el obrero, un trabajo honrado.» "
      "Voz de un partidario de ideas comunistas (de ejemplo): «El problema es la propiedad privada de las fábricas; deben pasar a manos de los trabajadores.» "
      "Voz de un partidario de ideas anarquistas (de ejemplo): «No hay que esperar nada del gobierno; los trabajadores deben decidir por sí mismos.»")
build(
    OA, 4, F4,
    use="Aprenderé a contrastar actores, causas y perspectivas frente a un mismo conflicto laboral. Sirve para entender por qué una misma situación genera respuestas políticas distintas.",
    prior=["Conozco las cinco corrientes: liberalismo, socialismo, comunismo, anarquismo y socialcristianismo.", "Sé que cada actor tiene una perspectiva.", "Sé calcular un porcentaje sencillo."],
    explain=[
        "En un conflicto laboral actúan varios actores: los dueños de las fábricas, los trabajadores y sus organizaciones, las autoridades del Estado, la Iglesia y otras organizaciones. Cada uno tiene una perspectiva distinta, que depende de sus intereses y de su posición. El dueño se preocupa por sus costos y por la libertad de contratar; los trabajadores por su salario y su jornada; el Estado por el orden y por las leyes.",
        "Las causas de un conflicto son varias: jornadas largas, salarios bajos, falta de leyes laborales y desconfianza entre las partes. Esto es multicausalidad. También pueden coincidir en el tiempo dos hechos que no se causan entre sí; por ejemplo, un aumento de huelgas y una crisis económica pueden estar relacionados o no, y hay que buscar evidencia antes de afirmarlo.",
        "Cada corriente ofrece una solución distinta al mismo conflicto: el liberalismo confía en el acuerdo libre y el mercado; el socialismo, en la organización y las leyes; el comunismo, en cambiar la propiedad de las fábricas; el anarquismo, en la autogestión sin Estado; el socialcristianismo, en la justicia y la colaboración entre las partes. Para evaluar hay que preguntar qué cambia cada solución y a quién beneficia o perjudica.",
    ],
    vocab=[("actor", "persona o grupo que participa en un conflicto o en una decisión"), ("perspectiva", "punto de vista que depende de los intereses y de la posición de cada actor"), ("multicausalidad", "situación en que un hecho tiene varias causas a la vez"), ("autogestión", "organización de una actividad por las mismas personas que la realizan"), ("quiebra", "situación en que una empresa no puede pagar sus deudas y deja de funcionar")],
    worked=[
        ("Calcular una petición de salario", "En otra fábrica de ejemplo, los trabajadores piden subir 10 % un salario de 20 unidades diarias. ¿Cuánto pedirían ganar?",
         ["El 10 % de 20 es 2.", "El nuevo salario es 20 + 2 = 22."], "22 unidades diarias"),
        ("Asociar una voz con una corriente", "Una voz de ejemplo dice: «Debemos confiar en el acuerdo libre y en el mercado». ¿Qué corriente se acerca?",
         ["La confianza en el acuerdo libre y el mercado es propia del liberalismo.", "No pide eliminar el Estado ni la propiedad privada."], "Liberalismo"),
    ],
    mistakes=[
        ("Atribuirle el conflicto a un solo actor.", "Los conflictos laborales tienen varias causas y actores.", "Revisa las causas y las perspectivas de cada actor."),
        ("Confundir correlación con causa.", "Que dos hechos coincidan no prueba que uno cause el otro.", "Busca un mecanismo y evidencia."),
    ],
    T=[
        ("En Historia: ¿qué es una perspectiva?", "El punto de vista que depende de los intereses y de la posición de cada actor", "Explica por qué los actores piensan distinto."),
        ("{F} ¿Qué piden los trabajadores de Textil Aurora respecto de la jornada?", "Bajarla de 12 a 10 horas diarias", "Lo dice el caso."),
        ("{F} ¿Qué voz expresa ideas liberales? A) la del dueño, B) la del sacerdote.", "A", "Defiende la libertad de contrato."),
        ("=", "{F} ¿Cuántas unidades por día aumentaría el salario con el alza pedida?", "5*20//100", "Se calcula el 20 % de 5."),
        ("=", "{F} ¿Cuánto ganarían por día con el aumento (en unidades)?", "5+5*20//100", "Se suma el aumento al salario."),
        ("=", "{F} ¿Cuántas horas semanales (de 6 días) se trabajarían con la jornada de 10 horas?", "10*6", "Se multiplican las horas por los días."),
        ("{F} ¿Qué voz propone cambiar la propiedad de las fábricas? A) la del partidario comunista, B) la del dirigente sindical socialista.", "A", "Pide que pasen a los trabajadores."),
        ("{F} ¿Qué voz desconfía del gobierno y propone decidir sin Estado? A) la del partidario anarquista, B) la del sacerdote.", "A", "Propone la autogestión sin Estado."),
        ("{F} ¿Qué voz combina justicia y colaboración entre patrón y obrero? A) la del sacerdote, B) la del dueño.", "A", "Es la idea socialcristiana."),
        ("=", "{F} Si la jornada pasara de 12 a 10 horas diarias durante 6 días, ¿cuántas horas menos se trabajarían en la semana?", "(12-10)*6", "Se resta la jornada nueva a la antigua y se multiplica por los días."),
        ("{F} El dueño dice que si sube los salarios, quiebra. ¿Qué dato necesitaría un investigador para comprobarlo? A) los costos y ganancias de la fábrica, B) el número de afiliados al sindicato.", "A", "Con ellos se puede verificar la afirmación."),
        ("{F} Un comentarista dice: «El conflicto se debe solo a los dirigentes sindicales». Usando las voces, ¿qué contradice la idea? Responde con una frase.", "Que hay otras causas, como la jornada larga, los salarios bajos y la falta de leyes laborales", "El conflicto tiene varias causas."),
        ("{F} ¿Qué voz espera que el Estado apruebe leyes que mejoren las condiciones? A) la del dirigente sindical, B) la del partidario anarquista.", "A", "El dirigente habla de lograr mejoras con leyes."),
    ],
    ctx=("Dos hechos de ejemplo en una ciudad ficticia: aumentaron las huelgas y aumentó la venta de helados. Una persona dice que uno causa el otro. ¿Qué concepto del vocabulario describe mejor el error? A) correlación sin causa, B) quiebra.", "A", "Coinciden en el tiempo sin que uno cause al otro."),
    sc=[("En Historia: ¿qué es la multicausalidad?", "Que un hecho tiene varias causas a la vez", "Evita explicar un conflicto con una sola causa."),
        ("¿Qué solución propone el anarquismo?", "La autogestión sin Estado", "Los trabajadores deciden por sí mismos."),
        ("¿Qué solución propone el socialcristianismo?", "Justicia en el salario y colaboración entre patrón y obrero", "Busca equilibrar a las partes.")],
    op=("{F} Elige dos voces y escribe para cada una: qué actor es, qué solución propone y a quién puede beneficiar o perjudicar. Termina con una frase que diga qué información adicional necesitarías para evaluar mejor el conflicto.",
        "Dueño: actor empresario; propone acuerdo libre; beneficia al dueño y puede perjudicar a los trabajadores. Dirigente sindical: actor trabajador; propone organización y leyes; beneficia a los obreros y puede aumentar costos del dueño. Necesitaría saber las ganancias de la fábrica.",
        ["identifica dos actores", "explica la solución de cada uno", "indica a quién beneficia o perjudica", "pide información adicional"], ["dos voces y una pregunta final"], ["describir una voz con burla", "no mencionar quién se beneficia"], "Léele tus dos voces a una persona de tu casa y pídele que diga cuál le pareció mejor explicada."),
    reinforce="Haz un cuadro de dos columnas: actor y solución que propone, con tres filas.",
    extend="Explica por qué evaluar quién se beneficia con una propuesta ayuda a comprender sus apoyos y sus críticas.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 5
F5 = ("Dossier de ejemplo, «¿Cómo responder al alza de los arriendos en la ciudad ficticia de Puerto Nuevo?» "
      "Dato 1: en dos años el arriendo promedio subió de $250.000 a $350.000 al mes. "
      "Dato 2: el ingreso promedio de las familias de la ciudad es de $700.000 al mes. "
      "Dato 3: construir viviendas privadas nuevas demora en promedio 3 años. "
      "Respuesta A (inspirada en el liberalismo): facilitar los permisos para que más empresas construyan y la mayor oferta baje los precios. "
      "Respuesta B (inspirada en el socialismo): construir viviendas públicas de arriendo a bajo costo. "
      "Respuesta C (inspirada en el socialcristianismo): subsidios y acuerdos entre propietarios, autoridades y organizaciones vecinales para lograr arriendos justos.")
build(
    OA, 5, F5,
    use="Aprenderé a argumentar sobre una respuesta política a un problema social actual con datos, reconociendo la mejor versión de las posturas contrarias. Sirve para debatir con evidencia y sin caricaturas.",
    prior=["Conozco las corrientes políticas frente a la cuestión social.", "Sé construir un argumento con tesis, evidencia, objeción y límite.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Los problemas sociales no son solo del pasado. Hoy también hay situaciones conflictivas, como el alza de los arriendos, el acceso a la salud o el cuidado del agua, que provocan respuestas políticas distintas. Muchas de esas respuestas se inspiran, en parte, en ideas parecidas a las que surgieron frente a la cuestión social: confiar más en el mercado, en el Estado, en acuerdos entre sectores o en la organización de la sociedad.",
        "Al trasladar una corriente al presente hay que hacerlo con cuidado y matices. Una propuesta actual puede tener rasgos de varias corrientes, y las circunstancias cambiaron. Por eso no basta con etiquetar una propuesta como «liberal» o «socialista»: hay que describir qué medida concreta propone, qué efectos puede tener, cuánto demora y quiénes ganan o pierden.",
        "Un argumento sólido incluye una tesis, evidencia numérica del dossier, una objeción que presente lo mejor de la postura contraria y un límite que diga qué datos faltan. La conclusión debe ser proporcional: si los datos no permiten saber cuál respuesta es la más eficaz, se dice y se propone qué información sería necesaria.",
    ],
    vocab=[("subsidio", "ayuda en dinero del Estado para reducir un costo"), ("oferta de viviendas", "cantidad de viviendas disponibles para arrendar o comprar"), ("tesis", "afirmación que se defiende en un argumento"), ("objeción", "razón que va en contra de una tesis"), ("proporcional", "que corresponde al tamaño de la evidencia disponible")],
    worked=[
        ("Calcular una alza", "Un arriendo de ejemplo pasó de $200.000 a $260.000. ¿De cuánto fue el alza y qué porcentaje fue?",
         ["Alza: 260.000 - 200.000 = 60.000.", "Porcentaje: 60.000 ÷ 200.000 × 100 = 30."], "$60.000, es decir, 30 %"),
        ("Formular una objeción", "Una tesis de ejemplo dice: «Hay que construir viviendas públicas». ¿Cuál puede ser una objeción?",
         ["Una objeción va en contra de la tesis.", "Puede decir que construir demora o cuesta mucho al Estado."], "Que puede demorar o ser costoso para el Estado"),
    ],
    mistakes=[
        ("Etiquetar una propuesta con una corriente y creer que eso la explica.", "Una etiqueta no dice qué medida es ni qué efectos tiene.", "Describe la medida y sus efectos."),
        ("Presentar la postura contraria de manera burlesca.", "Pierde credibilidad y no responde a las razones reales.", "Presenta la mejor versión de la objeción."),
    ],
    T=[
        ("En Historia: ¿qué es un subsidio?", "Una ayuda en dinero del Estado para reducir un costo", "Puede ayudar a pagar un arriendo."),
        ("{F} ¿Cuánto subió el arriendo promedio?", "$100.000", "De 250.000 a 350.000."),
        ("{F} ¿Cuánto demora construir viviendas privadas nuevas, según el dato 3?", "3 años", "El dato lo informa."),
        ("=", "{F} ¿Qué porcentaje subió el arriendo promedio en esos dos años?", "(350000-250000)*100//250000", "Se divide el alza por el arriendo inicial y se multiplica por 100.", "%"),
        ("=", "{F} ¿Qué porcentaje del ingreso promedio es el arriendo de $350.000?", "350000*100//700000", "Se divide el arriendo por el ingreso y se multiplica por 100.", "%"),
        ("{F} ¿Qué respuesta se apoya en que más oferta baje los precios? A) la respuesta A, B) la respuesta B.", "A", "Propone facilitar permisos para construir."),
        ("{F} ¿Qué respuesta propone viviendas públicas de arriendo a bajo costo? A) la respuesta B, B) la respuesta C.", "A", "Es la propuesta inspirada en el socialismo."),
        ("=", "{F} Si el arriendo siguiera subiendo $50.000 cada año, ¿cuánto sería dentro de 2 años (en pesos)?", "350000+2*50000", "Se suma el alza de dos años al arriendo actual."),
        ("{F} Una objeción a la respuesta A es que construir demora 3 años. ¿Qué dato apoya esa objeción? A) el dato 3, B) el dato 2.", "A", "Dice cuánto demora construir."),
        ("{F} Una persona concluye: «La respuesta B es la mejor porque es del Estado». ¿Qué problema tiene la conclusión? A) no usa datos ni compara efectos, B) es muy larga.", "A", "Falta evidencia de los efectos."),
        ("{F} ¿Qué dato muestra que el alza de arriendos es un problema social y no solo individual? Responde con una frase.", "Que el arriendo pasó a ser la mitad del ingreso promedio de la ciudad, es decir, afecta a muchas familias", "350.000 es la mitad de 700.000."),
        ("{F} La respuesta C propone acuerdos entre sectores. ¿Cuál puede ser un límite de esta respuesta? A) no se sabe si los propietarios aceptarían, B) no tiene ninguna ventaja.", "A", "Depende de que las partes acepten."),
        ("{F} Elige la mejor conclusión. A) las tres respuestas tienen ventajas y límites, y falta información sobre sus costos, B) una respuesta es perfecta.", "A", "La evidencia no basta para decidir con certeza."),
    ],
    ctx=("En un barrio de ejemplo se discute cómo responder a la falta de cupos en una sala cuna. Propuestas: A) que el municipio la construya con recursos públicos, B) que empresas privadas ofrezcan el servicio con precios libres. ¿Qué dato necesitas para evaluar mejor ambas? A) el costo y las familias que podrían pagar, B) el año en que se fundó el barrio.", "A", "Permite comparar efectos y acceso."),
    sc=[("En Historia: ¿por qué no basta con etiquetar una propuesta como «liberal» o «socialista»?", "Porque una etiqueta no dice qué medida es ni qué efectos tiene", "Hay que describir la medida y sus efectos."),
        ("¿Qué función tiene una objeción?", "Presentar la mejor versión de la postura contraria", "Da honestidad al argumento."),
        ("¿Qué significa una conclusión proporcional?", "Que afirma solo lo que los datos permiten afirmar", "Así se evita exagerar los resultados.")],
    op=("{F} Escribe un argumento de cinco a siete líneas sobre qué respuesta (A, B, C o una combinación) te parece más razonable. Incluye tu tesis, dos datos del dossier, una objeción presentada con respeto y un límite de los datos.",
        "Tesis: una combinación de B y C es más razonable. Datos: el arriendo subió de $250.000 a $350.000 y construir privado demora 3 años. Objeción: las viviendas públicas son costosas; se responde con subsidios temporales. Límite: no conocemos el costo de cada medida.",
        ["declara una tesis", "usa dos datos", "presenta una objeción con respeto", "indica un límite"], ["un argumento de cinco a siete líneas"], ["caricaturizar una corriente", "no usar datos"], "Pide a una persona de tu casa que identifique tu objeción y diga si fue justa con la otra postura."),
    reinforce="Escribe una tesis sobre un problema de tu barrio y un dato que podrías buscar para apoyarla.",
    extend="Explica por qué una propuesta puede combinar ideas de más de una corriente.",
    materials=MAT,
)
