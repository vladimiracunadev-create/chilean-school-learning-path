"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF03 (comprender textos orales y escritos de otras culturas, interpretar elementos significativos y valorarlos como
fuentes de conocimiento) y OA LF04 (escribir textos con expresiones propias del pueblo en distintas situaciones
comunicativas: ceremonias, rogativas, salidas a terreno).

Criterio de autoría: comunidades, personas, textos y situaciones son INVENTADOS, rotulados como tales, y no describen
ritos reales. Las únicas palabras en lengua indígena son «mari mari» y «chaltumay» (mapuzugun) y «iorana» y «maururu»
(rapa nui). No se inventa gramática, grafía ni pronunciación: las expresiones que se escriben en lengua las dicta el
educador o la educadora tradicional. Importa los ayudantes de student_content_lc6_b.
"""
from __future__ import annotations

from student_content_lc6_b import ab, vf, L, M, T, W, MAT
from student_lessons import arith, ex

LF3, LF4 = "LC06 OA LF03", "LC06 OA LF04"

# ============================================================ OA LF03 · Textos orales y escritos de otras culturas
L(
    LF3, 1, materials=MAT,
    use="Aprenderé a situar un texto oral o escrito de otra cultura y a reconocer en él elementos significativos. Sirve para valorarlo como fuente de conocimiento sin inventar su significado.",
    prior=["Sé que una fuente es la persona o el texto que entrega un dato.", "Sé separar lo que dice un texto de lo que interpreto."],
    explain=[
        "Un texto oral es el que se dice en voz alta y se transmite al escuchar, como un relato de una persona mayor. Un texto escrito se guarda en letras y se puede leer muchas veces. Muchas culturas guardan sus conocimientos de manera oral, y eso no los hace menos valiosos: la palabra dicha también es una fuente de conocimiento.",
        "Un elemento significativo es una parte del texto que lleva una idea importante: un lugar, un personaje, un objeto, una señal de la naturaleza o una frase que se repite. Para reconocerlos, nos preguntamos qué parte del texto se destaca y qué idea del texto sostiene. No decidimos nosotros su significado: lo que dice el texto lo afirmamos, y lo que no explica lo dejamos como pregunta.",
        "Antes de interpretar, situamos el texto con una ficha: comunidad, tipo de texto (oral o escrito), fuente, permiso y límite. Así sabemos quién lo cuenta y qué no podemos compartir. Cómo se valora el texto en la lengua indígena lo trabajamos con el educador o la educadora tradicional.",
    ],
    vocab=[("texto oral", "texto que se dice en voz alta y se transmite al escuchar"), ("texto escrito", "texto guardado en letras que se puede leer muchas veces"), ("elemento significativo", "parte del texto que lleva una idea importante"), ("fuente de conocimiento", "texto o persona de quien se aprende algo"), ("transmitir", "pasar un saber de una persona a otra")],
    worked=[
        W("Situar un texto oral", "Ficha inventada. Comunidad: Meseta Azul (no es un pueblo real). Tipo: texto oral. Fuente: doña Carmen, vecina. Permiso: autorizó usarlo en la escuela. Límite: no se cuenta cómo se guarda la semilla de la comunidad. ¿Qué tipo de texto es y qué no se cuenta?", ["Leo el tipo de texto: oral.", "La fuente es doña Carmen y dio permiso.", "El límite dice que no se cuenta cómo se guarda la semilla."], "Es un texto oral de doña Carmen; no se cuenta cómo se guarda la semilla."),
        W("Reconocer elementos significativos", "Texto inventado: «Cuando florece el arbusto amarillo, las familias abren la tierra. Mi abuela me lo enseñó». ¿Qué elementos se destacan?", ["Un elemento de la naturaleza: el arbusto amarillo.", "Una acción de las familias: abrir la tierra.", "Una persona que transmite el saber: la abuela."], "Elementos: el arbusto amarillo, abrir la tierra y la abuela que enseñó."),
    ],
    mistakes=[
        M("Pensar que un texto oral vale menos que uno escrito.", "Cada cultura guarda y transmite su saber a su manera.", "Valora ambas formas como fuentes de conocimiento."),
        M("Decidir yo qué significa un elemento del texto.", "Su significado lo explica la comunidad.", "Afirma solo lo que el texto dice y pregunta el resto."),
    ],
    R=[
        ex("Ficha: «Comunidad: Costa Clara. Tipo: texto oral. Fuente: don Efraín.» ¿Qué tipo de texto es? A) oral B) escrito", "A", "La ficha lo dice así."),
        ex("En la misma ficha, ¿quién es la fuente?", "Don Efraín", "La ficha lo nombra."),
        ex("¿Cómo se transmite un texto oral? A) al escuchar B) solo con letras", "A", "El texto oral se pasa hablando y escuchando."),
    ],
    C=[
        vf("un texto oral puede ser una fuente de conocimiento igual de valiosa que uno escrito.", True, "La palabra dicha también transmite saber."),
        ab("¿Qué es un elemento significativo?", "una parte del texto que lleva una idea importante", "cualquier palabra del texto", "Se destaca porque sostiene una idea."),
        vf("yo puedo decidir cuál es el significado de un elemento del texto aunque no lo explique.", False, "Su significado lo explica quien cuenta o la comunidad."),
    ],
    A=[
        ex("Texto inventado de don Efraín: «Cuando las gaviotas miran todas hacia el mar, los pescadores revisan las cuerdas. Me lo enseñó mi tío». Clasifica en NATURALEZA o PERSONA: a) las gaviotas b) el tío.", "a naturaleza, b persona", "Las gaviotas son parte de la naturaleza; el tío transmite el saber."),
        ex("En el mismo texto, ¿qué hacen los pescadores cuando las gaviotas miran al mar? A) revisan las cuerdas B) apagan las luces", "A", "El texto lo dice."),
        ex("Una ficha dice «Tipo: texto escrito. Fuente: no dice». ¿Qué falta para usarla? A) la fuente B) un dibujo", "A", "Sin fuente no se sabe de quién es el texto."),
    ],
    Z=[
        ex("Marcos dice: «Como el texto no está escrito, no sirve como fuente». ¿Qué error comete?", "Cree que solo lo escrito es fuente de conocimiento", "Los textos orales también transmiten saber."),
        ex("Lucía lee «florece el arbusto amarillo» y afirma «seguro el arbusto es sagrado». ¿Qué falla? A) el texto no dice eso B) el arbusto es verde", "A", "Se afirma algo que el texto no explica."),
    ],
    D=[
        ex("Dos textos: el de Meseta Azul es oral y el de una guía de la escuela es escrito. Un compañero dice que el oral es «más antiguo y por lo tanto mejor». ¿Qué error comete?", "Jerarquiza los textos", "Ser oral o escrito no hace a un texto mejor."),
        ex("En un texto aparece tres veces la frase «esperamos la flor». ¿Qué tipo de elemento significativo es? A) una frase que se repite B) un lugar", "A", "La repetición destaca la idea."),
    ],
    context=[ab("Tu curso recibe un audio con un relato de una persona de la comunidad. Falta la autorización para compartirlo. ¿Qué haces?", "no lo uso hasta pedir permiso", "lo subo igual porque es bonito", "Sin permiso no se comparte.", right_first=False)],
    selfcheck=[
        ex("Nombra dos tipos de elemento significativo.", "Dos entre: lugar, personaje, objeto, señal de la naturaleza, frase que se repite", "Son tipos que se destacan en un texto."),
        vf("conviene consultar al educador cuando no sé qué significa un elemento.", True, "Ellos pueden explicarlo."),
        ex("¿Cómo se llama el texto que se dice en voz alta? A) texto oral B) texto escrito", "A", "Es el que se transmite al escuchar."),
    ],
    task=T("Lee este texto oral inventado de doña Carmen, de Meseta Azul: «Cuando florece el arbusto amarillo del cerro, las familias abren la tierra. Mi abuela decía que el viento del sur trae la lluvia mansa. Por eso esperamos la flor antes de sembrar.» Haz una ficha con comunidad, tipo de texto, fuente y un límite. Luego anota tres elementos significativos y qué parte del texto los destaca.",
           "Comunidad: Meseta Azul. Tipo: texto oral. Fuente: doña Carmen. Límite: el texto no explica por qué se espera la flor. Elementos: el arbusto amarillo (lo dice al inicio), la abuela (transmite el saber) y la frase «esperamos la flor» (muestra la espera).",
           ["completa la ficha", "identifica tres elementos con su parte del texto", "no inventa significados"], ["ficha completa", "tres elementos"], ["inventar el significado", "decir que lo oral vale menos"],
           "Pedir que señale cada elemento en el texto; valorar que no invente significados."),
    reinforce="Subraya en el texto de doña Carmen los lugares, las personas y las señales de la naturaleza con tres colores.",
    extend="Explica con tus palabras por qué un texto oral puede ser una fuente de conocimiento.",
)

L(
    LF3, 2, materials=MAT,
    use="Aprenderé a leer o escuchar un texto de otra cultura con límites declarados, interpretando sus elementos sin inventar. Sirve para comprender el texto y decir qué valor tiene.",
    prior=["Sé situar un texto con su ficha.", "Sé que lo que no se cuenta se respeta."],
    explain=[
        "Para comprender un texto de otra cultura hacemos tres pasos. Primero leemos o escuchamos completo. Segundo, marcamos los elementos significativos: un lugar, una persona, una señal, una frase repetida. Tercero, separamos tres cosas: lo que el texto dice, lo que yo interpreto y lo que no se explica.",
        "La interpretación es una idea mía sobre el texto. Para que sea válida, debe apoyarse en una parte del texto y no contradecirla. Por ejemplo, si el texto dice que las familias esperan la flor antes de sembrar, puedo interpretar «yo pienso que observar la naturaleza es importante para esa comunidad». Pero no puedo afirmar qué creen sobre la flor si el texto no lo dice.",
        "Cuando el texto es oral, podemos pedir que lo repitan, anotar palabras clave y comprobar con la fuente si entendimos bien. Cuando es escrito, subrayamos y releemos. En ambos casos, los límites se declaran al final: «el texto no explica por qué la flor indica la siembra».",
    ],
    vocab=[("interpretación", "idea propia que se apoya en una parte del texto"), ("palabra clave", "palabra que sostiene la idea principal"), ("releer", "volver a leer para comprender mejor"), ("contradecir", "decir lo contrario de lo que dice el texto"), ("límite declarado", "frase que dice lo que el texto no explica")],
    worked=[
        W("Separar tres cosas", "Texto inventado de don Efraín, de Costa Clara: «Cuando las gaviotas miran todas hacia el mar, los pescadores revisan las cuerdas. Me lo enseñó mi tío. Hay otros avisos que solo cuenta la comunidad». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: los pescadores revisan las cuerdas cuando las gaviotas miran al mar.", "Interpreto: yo pienso que observan a las aves para prepararse.", "No se cuenta: los otros avisos."], "Dice: revisan las cuerdas cuando las gaviotas miran al mar. Interpreto: observan a las aves para prepararse. No se cuenta: los otros avisos."),
        W("Validar una interpretación", "Interpretación: «Yo pienso que en Costa Clara el saber pasa de familiares a jóvenes». ¿Se apoya en el texto?", ["Busco una parte del texto: «me lo enseñó mi tío».", "Esa parte muestra que un familiar enseñó.", "La interpretación se apoya en el texto."], "Sí: se apoya en «me lo enseñó mi tío»."),
    ],
    mistakes=[
        M("Interpretar sin apoyarme en ninguna parte del texto.", "La interpretación queda inventada.", "Busca la frase del texto que la respalda."),
        M("Afirmar lo que la comunidad cree sobre algo que el texto no explica.", "El texto no lo dice.", "Escribe «el texto no lo explica»."),
    ],
    R=[
        ex("Texto inventado de doña Carmen: «Cuando florece el arbusto amarillo, abrimos la tierra». ¿Qué hacen cuando florece el arbusto? A) abren la tierra B) cosechan", "A", "El texto lo dice así."),
        ex("¿Qué es una interpretación? A) una idea mía apoyada en el texto B) un dato copiado", "A", "Interpretar es dar una idea propia con respaldo."),
        ex("Si el texto no explica algo, ¿qué escribes? A) el texto no lo explica B) lo invento", "A", "Se declara el límite."),
    ],
    C=[
        vf("una interpretación válida debe apoyarse en una parte del texto.", True, "Si no, queda inventada."),
        vf("una interpretación puede contradecir lo que dice el texto.", False, "Contradecir el texto la hace inválida."),
        ab("En un texto oral, ¿qué puedes hacer para comprender mejor?", "pedir que lo repitan y anotar palabras clave", "adivinar las partes que no entendí", "Repetir y anotar ayuda a comprobar lo entendido."),
    ],
    A=[
        ex("Texto inventado de doña Carmen: «Mi abuela decía que el viento del sur trae la lluvia mansa». Clasifica en DICE EL TEXTO o INTERPRETO: a) la abuela decía que el viento del sur trae lluvia b) la abuela era una mujer sabia.", "a dice el texto, b interpreto", "La primera es literal; la segunda es una suposición."),
        ex("Texto de doña Carmen: «Esperamos la flor antes de sembrar. Mi abuela decía que el viento del sur trae la lluvia mansa». Interpretación: «Yo pienso que las familias de Meseta Azul respetan los tiempos de la naturaleza». ¿En qué frase del texto se apoya? A) «Esperamos la flor antes de sembrar» B) «Mi abuela decía que el viento del sur trae la lluvia mansa»", "A", "Esperar la flor muestra respeto por los tiempos."),
        ex("Don Efraín no explicó por qué las gaviotas miran al mar. ¿Qué escribes en el límite? A) el texto no explica por qué miran al mar B) miran por hambre", "A", "Declarar el límite evita inventar."),
    ],
    Z=[
        ex("Pablo afirma: «En Costa Clara creen que las gaviotas son mensajeras de los espíritus». El texto solo habla de que revisan las cuerdas. ¿Qué error comete?", "Atribuye una creencia que el texto no dice", "El texto no habla de espíritus."),
        ex("Una niña interpreta: «Yo pienso que el tío de don Efraín fue un buen maestro». ¿Es válida? A) sí, se apoya en «me lo enseñó mi tío» B) no, debe ser dato", "A", "Es una interpretación apoyada en el texto y marcada como suya."),
    ],
    D=[
        ex("Texto de Meseta Azul: «Esperamos la flor antes de sembrar». Dos interpretaciones. Una: «yo pienso que sembrar con calma es importante para la comunidad». Otra: «la comunidad cree que el arbusto da poderes». ¿Cuál se apoya en el texto?", "La primera", "La segunda inventa una creencia."),
        ex("Una persona escucha un relato y solo entendió la mitad. ¿Qué hace? A) pide que lo repitan B) completa con ideas propias", "A", "Pedir repetición evita inventar."),
    ],
    context=[ab("En un taller escolar, un invitado cuenta un texto oral. Una compañera dice en voz alta lo que cree que significa cada elemento. ¿Qué le sugieres?", "preguntar al invitado qué significa", "decirlo más fuerte", "Quien cuenta puede explicar su texto.")],
    selfcheck=[
        ex("Nombra los tres pasos para comprender un texto de otra cultura.", "Leer o escuchar completo, marcar elementos y separar dice, interpreto y no se explica", "Son los pasos de la clase."),
        vf("subrayar y releer ayuda a comprender un texto escrito.", True, "Son técnicas de lectura."),
        ex("¿Cómo marcas una idea tuya? A) con «yo pienso que» B) con «la comunidad dice que»", "A", "Así no se confunde con la fuente."),
    ],
    task=T("Lee este texto inventado de don Efraín, de Costa Clara: «Cuando las gaviotas miran todas hacia el mar, los pescadores revisan las cuerdas de sus botes. Lo aprendí de mi tío, que lo aprendió de su padre. Hay otros avisos que solo cuenta la comunidad.» Haz tres columnas: «El texto dice», «Yo interpreto» y «No se explica». Pon al menos dos datos en cada una y cierra con una frase de límites.",
           "El texto dice: revisan las cuerdas cuando las gaviotas miran al mar; el saber pasó del padre al tío y a don Efraín. Yo interpreto: yo pienso que el saber se transmite entre generaciones. No se explica: los otros avisos. Límite: el texto no dice por qué miran al mar.",
           ["separa tres columnas", "interpretación apoyada en el texto", "declara límites"], ["tabla de tres columnas", "frase de límites"], ["interpretar sin apoyo", "inventar los otros avisos"],
           "Pedir que indique la frase que respalda cada interpretación; valorar que deje sin completar lo no contado."),
    reinforce="Subraya con un color lo que dice el texto de Costa Clara y con otro lo que interpretas.",
    extend="Escribe dos interpretaciones distintas del texto de Meseta Azul y señala en qué frase se apoya cada una.",
)

L(
    LF3, 3, materials=MAT,
    use="Aprenderé a relacionar los elementos significativos de un texto con el conocimiento que transmite. Sirve para valorar el texto como fuente de saber de una comunidad.",
    prior=["Sé interpretar un texto con apoyo en sus frases.", "Sé declarar límites."],
    explain=[
        "Un texto de una cultura suele transmitir un conocimiento: cómo observar la naturaleza, cómo organizarse, cómo cuidar a otros o cómo recordar a quienes vivieron antes. Los elementos significativos del texto son pistas de ese conocimiento. Por ejemplo, un arbusto que florece puede ser una señal para empezar a sembrar.",
        "Para relacionar un elemento con un conocimiento hacemos tres preguntas: ¿qué elemento aparece?, ¿qué hace o qué indica en el texto?, ¿qué enseña sobre cómo vive esa comunidad? Respondemos solo con lo que dice el texto; si falta un dato, lo marcamos como pregunta para el educador o la educadora tradicional.",
        "Los conocimientos de una comunidad se llaman saberes. Pueden ser de la naturaleza, del trabajo, de la convivencia o de la historia. Cada saber pertenece a la comunidad que lo desarrolló, por eso lo citamos con su fuente y no lo presentamos como propio ni como verdad universal.",
    ],
    vocab=[("saber", "conocimiento que una comunidad ha desarrollado y transmite"), ("señal", "elemento que indica que algo va a ocurrir o que es momento de actuar"), ("convivencia", "manera de vivir juntos y cuidarse"), ("citar", "decir de quién es un dato o una idea"), ("pista", "elemento que ayuda a descubrir una idea")],
    worked=[
        W("Relacionar elemento y conocimiento", "Texto inventado de doña Carmen: «Cuando florece el arbusto amarillo, abrimos la tierra para sembrar». Relaciona el elemento con el saber.", ["Elemento: el arbusto amarillo.", "Qué hace en el texto: indica que es tiempo de sembrar.", "Qué enseña: la comunidad observa la naturaleza para organizar su trabajo."], "El arbusto es una señal para sembrar; el saber es observar la naturaleza para organizar el trabajo."),
        W("Citar un saber con su fuente", "Un niño escribe: «Es sabido que las flores avisan cuándo sembrar». ¿Qué corrige?", ["No nombra la fuente.", "Presenta el saber como universal.", "Debe decir: Según doña Carmen, de Meseta Azul…"], "Debe citar: «Según doña Carmen, de Meseta Azul, la flor del arbusto indica el tiempo de sembrar»."),
    ],
    mistakes=[
        M("Presentar el saber de una comunidad como verdad para todos.", "Cada comunidad desarrolla su propio saber.", "Escribe «según…, de…»."),
        M("Relacionar un elemento con algo que el texto no menciona.", "Se inventa el saber.", "Usa solo lo que dice el texto."),
    ],
    R=[
        ex("Texto inventado de don Efraín: «Cuando las gaviotas miran hacia el mar, revisamos las cuerdas». ¿Qué elemento de la naturaleza aparece? A) las gaviotas B) los cerros", "A", "El texto menciona a las gaviotas."),
        ex("En ese mismo texto, ¿qué hace el pescador cuando las gaviotas miran al mar? A) revisa las cuerdas B) duerme", "A", "El texto lo dice."),
        ex("¿Cómo se llaman los conocimientos que una comunidad desarrolla y transmite? A) saberes B) mapas", "A", "Esa es la palabra de la clase."),
    ],
    C=[
        vf("un elemento significativo puede ser una pista del conocimiento que transmite el texto.", True, "Los elementos destacados indican el saber."),
        vf("el saber de una comunidad es igual para todas las comunidades.", False, "Cada comunidad desarrolla el suyo."),
        ab("¿Qué conviene hacer si falta un dato para entender el saber?", "anotar una pregunta para el educador", "inventar el dato", "El dato faltante lo aporta quien sabe."),
    ],
    A=[
        ex("Texto: «Cuando sube la neblina del cerro, guardamos las ovejas en el corral». Elemento: la neblina. ¿Qué indica? A) que es momento de guardar las ovejas B) que es hora de comer", "A", "El texto relaciona la neblina con guardar las ovejas."),
        ex("Clasifica el saber como NATURALEZA o CONVIVENCIA: a) observar al arbusto para sembrar b) turnarse para cuidar el corral.", "a naturaleza, b convivencia", "El primero observa la naturaleza; el segundo organiza la vida en común."),
        ex("Completa la cita: «Según don Efraín, de Costa Clara, cuando las gaviotas miran al mar, los pescadores…»", "Revisan las cuerdas", "Repite lo que dice el texto."),
    ],
    Z=[
        ex("Rosa escribe: «Las gaviotas siempre avisan el mal tiempo en todo Chile». ¿Qué falla? A) generaliza un saber de una comunidad B) usa letra pequeña", "A", "El texto solo habla de Costa Clara."),
        ex("Un compañero relaciona la neblina con un espíritu porque «suena misterioso». ¿Qué error comete?", "Inventa un significado que el texto no dice", "El texto no habla de espíritus."),
    ],
    D=[
        ex("Dos textos: Meseta Azul (la flor indica sembrar) y Costa Clara (las gaviotas indican revisar cuerdas). ¿Qué tienen en común? A) ambas comunidades observan la naturaleza para decidir qué hacer B) ambas siembran", "A", "Los dos textos usan una señal natural para actuar."),
        ex("Tienes un texto de una tercera comunidad sin fuente. ¿Qué haces? A) pido la fuente antes de citarlo B) lo cito como saber de todos", "A", "Sin fuente no se cita."),
    ],
    context=[ab("Preparas una infografía escolar con saberes de varias comunidades. ¿Cómo presentas cada uno?", "con el nombre de la comunidad y la fuente", "con el título «Así lo hacen todos»", "Cada saber se cita con su fuente.")],
    selfcheck=[
        ex("Nombra una pregunta para relacionar un elemento con un conocimiento.", "¿Qué elemento aparece, qué indica y qué enseña?", "Son las tres preguntas de la clase."),
        vf("un saber de una comunidad puede ser sobre la naturaleza, el trabajo, la convivencia o la historia.", True, "Esos son tipos de saberes."),
        ex("¿Cómo citas un saber? A) según [persona], de [comunidad] B) es sabido que", "A", "Nombra a la fuente."),
    ],
    task=T("Lee este texto oral inventado de doña Ximena, de Cumbre Clara: «Cuando la neblina baja al valle, guardamos las ovejas en el corral. Si la neblina se queda hasta el mediodía, esperamos para salir. Así nos enseñó mi madre.» Haz una tabla con tres columnas: «Elemento», «Qué indica en el texto» y «Saber que transmite». Pon dos elementos. Escribe una cita con «Según…, de…».",
           "Elemento: neblina; indica guardar las ovejas; saber: observar el clima para cuidar los animales. Elemento: la madre; indica que el saber se enseñó; saber: la familia transmite el saber. Cita: Según doña Ximena, de Cumbre Clara, cuando la neblina baja al valle guardan las ovejas.",
           ["relaciona elemento con saber", "usa solo lo que dice el texto", "cita con fuente"], ["tabla", "cita"], ["generalizar el saber", "inventar significados"],
           "Pedir que muestre la frase que sostiene cada relación; valorar la cita con fuente."),
    reinforce="Elige un elemento del texto de Meseta Azul y escribe qué indica y qué saber transmite.",
    extend="Escribe una pregunta para el educador sobre un saber del texto de Costa Clara.",
)

L(
    LF3, 4, materials=MAT,
    use="Aprenderé a construir una valoración de un texto como fuente de conocimiento, con razones tomadas del texto y con la fuente atribuida. Sirve para opinar con respeto y fundamentar mis ideas.",
    prior=["Sé relacionar elementos con saberes.", "Sé citar una fuente."],
    explain=[
        "Valorar un texto como fuente de conocimiento significa explicar por qué nos enseña algo importante. Una valoración tiene tres partes: qué texto es y de quién, qué conocimiento transmite y por qué creo que es valioso. La razón se toma del texto: «porque ayuda a organizar el trabajo» o «porque cuida a los animales».",
        "Una valoración atribuida cita la fuente y la comunidad: «Según doña Carmen, de Meseta Azul…». Después agrega la razón propia: «Valoro este texto porque…». Si la valoración usa palabras fuertes como «el mejor» o «el más importante», pierde respeto, porque compara con otros textos sin fundamento.",
        "Expresar la valoración en la lengua indígena que corresponda es un trabajo con el educador o la educadora tradicional. Tú escribes tu idea en castellano, en frases cortas; él o ella te enseña cómo se dice y qué forma usa tu comunidad. Nunca se inventan frases en lengua.",
    ],
    vocab=[("valoración", "explicación de por qué un texto es valioso"), ("razón", "dato del texto que respalda una idea"), ("atribuir", "decir de quién viene un dato"), ("fundamentar", "apoyar una idea con razones"), ("frase corta", "oración sencilla que facilita traducir y revisar")],
    worked=[
        W("Escribir una valoración", "Texto inventado de doña Carmen: «Cuando florece el arbusto amarillo, abrimos la tierra». Escribe una valoración.", ["Texto y fuente: doña Carmen, de Meseta Azul.", "Conocimiento: observar la flor para decidir cuándo sembrar.", "Razón: ayuda a organizar el trabajo de la comunidad."], "Según doña Carmen, de Meseta Azul, la flor indica cuándo sembrar. Valoro este texto porque ayuda a organizar el trabajo de la comunidad."),
        W("Evitar un juicio sin fundamento", "Un niño escribe: «El texto de Meseta Azul es el mejor de todos». ¿Qué corriges?", ["«El mejor de todos» compara con textos que no leyó.", "No tiene razón del texto.", "Debe explicar qué enseña."], "Debe cambiarlo por una razón del texto, como «porque enseña a observar la naturaleza»."),
    ],
    mistakes=[
        M("Usar «el mejor» o «el más importante».", "Compara sin fundamento.", "Explica qué enseña el texto."),
        M("No decir de quién es el texto.", "Se pierde la fuente.", "Empieza con «Según…, de…»."),
    ],
    R=[
        ex("¿Cuántas partes tiene una valoración según la clase (texto y fuente, conocimiento, razón de valor)? Escribe el número.", "3", "Son texto y fuente, conocimiento y razón de valor."),
        ex("¿Qué frase empieza una valoración atribuida? A) «Según doña Carmen, de Meseta Azul…» B) «Todos saben que…»", "A", "Nombra la fuente."),
        ex("¿Quién te enseña cómo se dice tu valoración en lengua indígena? A) el educador o la educadora B) un traductor automático", "A", "Es quien enseña la lengua de tu comunidad."),
    ],
    C=[
        vf("una valoración debe incluir una razón tomada del texto.", True, "Sin razón no está fundamentada."),
        vf("decir «el mejor texto del mundo» es una valoración fundamentada.", False, "No tiene razón del texto."),
        ab("¿Cómo conviene escribir las frases que luego se dirán en lengua indígena?", "cortas y sencillas", "muy largas y con muchas ideas", "Las frases cortas se revisan y traducen mejor."),
    ],
    A=[
        ex("Texto: «Cuando las gaviotas miran al mar, revisamos las cuerdas». ¿Qué conocimiento transmite, para completar «Valoro este texto porque enseña a…»? A) observar a las aves para prepararse B) pescar siempre de noche", "A", "Es el conocimiento que transmite el texto; la otra opción no aparece en él."),
        ex("Clasifica en FUENTE o RAZÓN: a) según don Efraín, de Costa Clara b) porque ayuda a prevenir accidentes.", "a fuente, b razón", "La primera nombra de quién es el texto; la segunda explica el valor."),
        ex("Elige la valoración mejor fundamentada. A) «Valoro el texto porque enseña a guardar las ovejas con la neblina» B) «Valoro el texto porque es el más lindo»", "A", "Tiene razón tomada del texto."),
    ],
    Z=[
        ex("Camila quiere decir su valoración en lengua indígena y escribe palabras que cree que están bien. ¿Qué falla? A) no consultó al educador B) escribió muy ordenado", "A", "No se inventan palabras en lengua."),
        ex("Una valoración dice «Valoro el texto porque es antiguo». ¿Qué le falta? A) una razón del texto que explique qué enseña B) más adjetivos", "A", "Ser antiguo no explica el conocimiento."),
    ],
    D=[
        ex("Dos valoraciones del texto de Cumbre Clara (la neblina y las ovejas). Una: «Valoro el texto porque enseña a cuidar a los animales según el clima». Otra: «Valoro el texto porque es especial». ¿Cuál se apoya mejor en el texto?", "La primera", "Dice qué enseña el texto."),
        ex("Tu valoración queda muy larga para traducirla en lengua. ¿Qué haces? A) la divido en frases cortas B) la dejo igual", "A", "Las frases cortas facilitan la revisión con el educador."),
    ],
    context=[ab("Tu curso hará un mural con valoraciones de textos de comunidades. ¿Qué debe llevar cada valoración?", "texto, fuente, conocimiento y una razón del texto", "solo una opinión sin fuente", "Con esos elementos queda fundamentada y respetuosa.")],
    selfcheck=[
        ex("Escribe la fórmula de una valoración con tus palabras.", "Según [fuente], de [comunidad], el texto enseña [saber]; lo valoro porque [razón]", "Une fuente, saber y razón."),
        vf("la razón de una valoración se toma del texto.", True, "Así queda fundamentada."),
        ex("¿Qué haces con las frases que quieres decir en lengua? A) las reviso con el educador B) las invento", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Lee este texto inventado de doña Ximena, de Cumbre Clara: «Cuando la neblina baja al valle, guardamos las ovejas en el corral. Esperamos hasta que se vaya. Así nos enseñó mi madre.» Escribe una valoración de tres frases cortas: una con la fuente, otra con el conocimiento y otra que empiece con «Valoro este texto porque…». Después anota la pregunta que llevarías al educador para decir tu valoración en la lengua de tu comunidad.",
           "Según doña Ximena, de Cumbre Clara, cuando baja la neblina guardan las ovejas. El texto enseña a cuidar a los animales según el clima. Valoro este texto porque protege a las ovejas. Pregunta: «¿Cómo se dice mi valoración en nuestra lengua?»",
           ["tres frases cortas", "razón tomada del texto", "pregunta al educador"], ["valoración escrita", "pregunta"], ["decir «el mejor»", "inventar palabras en lengua"],
           "Pedir que señale la razón en el texto; valorar que no use juicios sin fundamento."),
    reinforce="Cambia tres frases con «el mejor» o «el más importante» por frases con una razón del texto.",
    extend="Escribe una segunda valoración del texto de Costa Clara con una razón distinta.",
)

L(
    LF3, 5, materials=MAT,
    use="Aprenderé a contrastar la versión oral y la versión escrita de un mismo texto sin decir cuál es mejor. Sirve para entender que cada forma guarda el conocimiento a su manera.",
    prior=["Sé valorar un texto como fuente.", "Sé comparar con los mismos criterios."],
    explain=[
        "Un mismo relato puede existir en versión oral y en versión escrita. La versión oral se dice en voz alta; quien cuenta puede hacer pausas, repetir, cambiar el tono y mirar a quienes escuchan. La versión escrita queda fija: se puede leer muchas veces, pero no tiene voz ni gestos. Cada una guarda y transmite el saber de una forma distinta.",
        "Contrastar significa comparar con los mismos criterios: cómo se transmite, quién participa, qué se puede repetir y qué cambia. Anotamos semejanzas y diferencias. No decimos que una versión es más verdadera, más antigua o más valiosa. Tampoco olvidamos que, en el paso de oral a escrito, se pueden perder gestos, tonos o partes reservadas.",
        "Si una versión escrita cambia algo respecto de la oral, quien la escribió debe explicar cómo la hizo y quién la autorizó. Las variantes de un mismo texto, por ejemplo dos formas de decir lo mismo, se reconocen sin jerarquizar. Para valorar ambas versiones en lengua indígena, pedimos ayuda al educador o la educadora tradicional.",
    ],
    vocab=[("versión", "forma en que existe un mismo relato"), ("variante", "otra forma de decir o escribir lo mismo"), ("fijo", "que no cambia cada vez que se lee"), ("gesto", "movimiento del cuerpo o la cara que acompaña la palabra"), ("contrastar", "comparar para ver semejanzas y diferencias")],
    worked=[
        W("Contrastar dos versiones", "Versión oral de doña Carmen: dice «esperamos la flor» tres veces, con pausas y mirando al cerro. Versión escrita de la escuela: «Las familias esperan la flor». Contrasta con el criterio «cómo se transmite».", ["Oral: pausas, repetición y gesto.", "Escrita: texto fijo que se lee las veces que se quiera.", "Semejanza: ambas transmiten que se espera la flor."], "Ambas transmiten la espera de la flor; la oral usa voz, pausas y gestos, y la escrita queda fija."),
        W("Evitar la jerarquía", "Un compañero dice: «La escrita es mejor porque no se olvida». ¿Qué corriges?", ["Dice «mejor», que es un orden.", "La oral también transmite durante generaciones.", "Debe describir qué guarda cada versión."], "Corrige la jerarquía: la escrita queda fija y la oral guarda tonos y gestos; ninguna es mejor."),
    ],
    mistakes=[
        M("Decir que la versión escrita es más verdadera que la oral.", "Ser escrita no la hace más verdadera.", "Describe qué guarda cada versión."),
        M("Escribir un texto oral sin pedir permiso.", "La fuente decide si se escribe y cómo.", "Pide autorización y muestra la versión."),
    ],
    R=[
        ex("¿Qué versión puede tener pausas, tono y gestos: la oral o la escrita?", "La oral", "Se dice con la voz y el cuerpo."),
        ex("¿Qué versión queda fija y se puede leer muchas veces? A) la escrita B) la oral", "A", "El texto escrito se guarda en letras."),
        ex("¿Qué se hace para comparar dos versiones? A) usar los mismos criterios B) elegir la que gusta", "A", "Con criterios iguales la comparación es justa."),
    ],
    C=[
        vf("la versión oral y la escrita de un relato pueden guardar el saber de maneras distintas.", True, "Cada una tiene sus características."),
        vf("la versión escrita es siempre más verdadera que la oral.", False, "Ser escrita no la hace más verdadera."),
        ab("¿Qué se debe hacer antes de escribir un texto oral de una comunidad?", "pedir permiso a la fuente", "cambiarlo para que quede mejor", "La fuente decide si se escribe."),
    ],
    A=[
        ex("Criterio «qué se puede repetir». Oral: se repite cada vez que alguien cuenta, aunque cambie el tono. Escrita: se repite igual cada vez. ¿Qué diferencia hay? A) la oral puede cambiar de tono; la escrita se repite igual B) no hay diferencia", "A", "La escrita queda fija."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas versiones transmiten un saber b) solo una tiene gestos.", "a semejanza, b diferencia", "La primera es común; la segunda, distinta."),
        ex("Dos variantes del mismo texto: «Esperamos la flor» y «Aguardamos la flor». ¿Qué relación tienen? A) dicen lo mismo con palabras distintas B) cuentan historias distintas", "A", "Son variantes, no relatos diferentes."),
    ],
    Z=[
        ex("Sebastián dice: «Si el texto no se escribe, se pierde». ¿Qué error comete? A) piensa que solo lo escrito se conserva B) piensa que lo oral es largo", "A", "Los textos orales se han transmitido durante generaciones."),
        ex("Una versión escrita no dice quién autorizó escribirla. ¿Qué falta?", "La autorización de la fuente", "Es parte de respetar el origen del texto."),
    ],
    D=[
        ex("Hay dos versiones del texto de Cumbre Clara: oral (con pausas y silencio al final) y escrita (con una frase de cierre). Una niña dice que la escrita «completa» a la oral. ¿Qué corriges?", "La escrita no completa a la oral, es otra versión", "Cada versión tiene su forma y no se corrige a la otra."),
        ex("Si en el paso de oral a escrito se pierden los gestos, ¿qué conviene anotar? A) una nota que diga que la versión oral tenía gestos B) nada", "A", "Declarar lo que se pierde evita engañar."),
    ],
    context=[ab("Para una exposición, un grupo debe elegir entre contar un relato en voz alta o leerlo escrito. ¿Qué criterio usa?", "la audiencia y lo que autorizó la fuente", "cuál se ve más bonito", "La decisión depende de la fuente y de quién escucha.")],
    selfcheck=[
        ex("Nombra una diferencia entre un texto oral y uno escrito.", "El oral tiene voz, pausas y gestos; el escrito queda fijo", "Resume la diferencia."),
        vf("al contrastar versiones, decimos cuál es la mejor.", False, "Contrastar es describir, no ordenar."),
        ex("¿Qué es una variante? A) otra forma de decir o escribir lo mismo B) un error", "A", "No es un error, es otra forma."),
    ],
    task=T("Lee dos versiones inventadas del mismo texto de doña Carmen, de Meseta Azul. Oral (cuenta con pausas, mira al cerro y repite la frase final): «Cuando florece el arbusto amarillo… abrimos la tierra… esperamos la flor, esperamos la flor». Escrita (de la escuela): «Cuando florece el arbusto amarillo, las familias abren la tierra». Haz una tabla con tres criterios: cómo se transmite, qué se puede repetir y qué se pierde o se gana. Escribe una semejanza y una diferencia sin usar «mejor» ni «peor».",
           "Oral: voz, pausas, repetición y gesto; se puede repetir cada vez con cambios; se gana el tono, se pierde la letra fija. Escrita: texto fijo; se repite igual; se gana permanencia, se pierden los gestos. Semejanza: ambas dicen cuándo se abre la tierra. Diferencia: la oral repite «esperamos la flor».",
           ["usa tres criterios iguales para ambas", "escribe semejanza y diferencia", "no jerarquiza"], ["tabla comparativa", "dos frases"], ["decir cuál es más verdadera", "olvidar lo que se pierde"],
           "Pedir que muestre cada dato en las dos versiones; valorar que describa sin ordenar."),
    reinforce="Subraya con verde las semejanzas y con azul las diferencias entre las dos versiones del texto.",
    extend="Explica por qué pedir permiso a la fuente es importante antes de escribir un texto oral.",
)

# ============================================================ OA LF04 · Escribir textos con expresiones propias
L(
    LF4, 1, materials=MAT,
    use="Aprenderé a reconocer en qué situaciones comunicativas (ceremonias, rogativas, salidas a terreno) se escriben textos y qué cuidado requieren las expresiones del pueblo. Sirve para escribir con respeto y sin inventar lengua.",
    prior=["Sé que lo reservado de una comunidad se respeta.", "Sé que el educador o la educadora enseña las expresiones en lengua."],
    explain=[
        "Escribimos para comunicar algo a otras personas. Una situación comunicativa es el momento en que se comunica: quién escribe, a quién, para qué y en qué lugar. En esta clase pensamos en tres: las ceremonias, que son reuniones con un sentido espiritual o cultural; las rogativas, que son momentos de pedir o agradecer; y las salidas a terreno, que son visitas para aprender en el lugar.",
        "Cada situación pide un texto distinto. Para invitar a una reunión se escribe una invitación. Para agradecer, una carta o tarjeta. Para una salida a terreno, una nota de campo con fecha, lugar y lo observado. Pero ojo: lo que se dice en una ceremonia o rogativa muchas veces es reservado y no se escribe sin permiso de la comunidad.",
        "Las expresiones en lengua indígena que aparecen en un texto, como un saludo, un agradecimiento o un nombre de lugar, las entrega el educador o la educadora tradicional. Algunas muy conocidas son «mari mari» (saludo en mapuzugun), «chaltumay» (gracias en mapuzugun), «iorana» (saludo en rapa nui) y «maururu» (gracias en rapa nui). Fuera de estas, no inventamos ninguna.",
    ],
    vocab=[("situación comunicativa", "momento en que se comunica: quién, a quién, para qué y dónde"), ("invitación", "texto que convoca a una reunión"), ("nota de campo", "texto breve con fecha, lugar y lo observado en una salida a terreno"), ("expresión", "palabra o frase que se usa para saludar, agradecer o nombrar"), ("reservado", "que la comunidad prefiere no escribir ni compartir")],
    worked=[
        W("Elegir el texto para la situación", "Situación: tu curso visitará un huerto comunitario y deben registrar lo que ven. ¿Qué texto escribes?", ["Es una salida a terreno.", "Se necesita registrar fecha, lugar y lo observado.", "El texto adecuado es la nota de campo."], "Una nota de campo con fecha, lugar y lo observado."),
        W("Reconocer lo que no se escribe", "Una niña quiere escribir en su cuaderno las palabras exactas que se dijeron en una reunión espiritual de la comunidad. El educador le dijo que son reservadas. ¿Qué hace?", ["Lo que la comunidad reserva no se escribe.", "Puede escribir que hubo una reunión, sin las palabras.", "Agradece al educador la orientación."], "No escribe las palabras reservadas; solo anota que hubo una reunión."),
    ],
    mistakes=[
        M("Escribir palabras en lengua indígena «porque suenan lindas».", "Pueden ser incorrectas o reservadas.", "Usa solo las que entregue el educador."),
        M("Escribir todo lo que se escuchó en una reunión de la comunidad.", "Algunas partes son reservadas.", "Pregunta qué se puede escribir."),
    ],
    R=[
        ex("¿Qué texto escribes para convocar a una reunión? A) una invitación B) una receta", "A", "La invitación convoca."),
        ex("¿Qué texto registra fecha, lugar y lo observado en una salida a terreno? A) una nota de campo B) un chiste", "A", "Esa es su función."),
        ex("¿Qué significa «chaltumay» en mapuzugun?", "Gracias", "Es un agradecimiento muy conocido."),
    ],
    C=[
        vf("«mari mari» es un saludo muy conocido en mapuzugun.", True, "Está atestiguado como saludo."),
        vf("todo lo que se dice en una ceremonia se puede escribir libremente.", False, "Muchas partes son reservadas y requieren permiso."),
        ab("¿Quién entrega las expresiones en lengua que irán en el texto?", "el educador o la educadora tradicional", "un compañero que las adivina", "Quien enseña la lengua las entrega."),
    ],
    A=[
        ex("Clasifica el texto: a) «Los invitamos a la reunión del sábado» b) «Gracias por recibirnos» c) «Hoy observamos tres huertos». Escribe INVITACIÓN, AGRADECIMIENTO o NOTA DE CAMPO para cada uno.", "a invitación, b agradecimiento, c nota de campo", "Cada texto cumple una función distinta."),
        ex("Para agradecer a una persona de la comunidad después de una salida, ¿qué expresión muy conocida puedes pedir al educador? A) chaltumay B) una palabra inventada", "A", "«Chaltumay» es un agradecimiento muy conocido en mapuzugun."),
        ex("Un texto de salida a terreno debe llevar siempre cuál de estos datos: A) fecha y lugar B) solo un dibujo", "A", "La nota de campo registra fecha y lugar."),
    ],
    Z=[
        ex("Leo escribe en una invitación palabras en lengua que no pidió al educador. ¿Qué error comete?", "Usa expresiones sin validar", "Podrían estar mal o ser reservadas."),
        ex("Una compañera dice: «Como es una rogativa, escribiré todo lo que se dijo». ¿Qué debe hacer primero? A) preguntar a la comunidad qué se puede escribir B) escribir más rápido", "A", "La comunidad decide qué es reservado."),
    ],
    D=[
        ex("En un huerto comunitario te dicen: «Pueden anotar lo que ven, pero no tomar fotos del lugar de respeto». ¿Qué anotas? A) lo que ves, excepto el lugar de respeto B) todo y también el lugar", "A", "Se respeta lo que la comunidad pidió."),
        ex("Quieres escribir un saludo en rapa nui para una tarjeta. ¿Cuál es la forma más segura? A) usar «iorana», conocido, y pedir otras al educador B) inventar una frase larga", "A", "Solo se usan expresiones conocidas o validadas."),
    ],
    context=[ab("Tu curso prepara una invitación para una persona de la comunidad que visitará la escuela. ¿Qué haces con el saludo en lengua?", "pido al educador que me indique uno apropiado", "uso un traductor sin revisar", "El saludo debe ser validado.")],
    selfcheck=[
        ex("Nombra dos situaciones comunicativas de esta clase.", "Dos entre: ceremonias, rogativas, salidas a terreno", "Son las tres de la clase."),
        vf("una nota de campo registra fecha, lugar y lo observado.", True, "Esos son sus datos."),
        ex("¿Qué haces si no sabes si una frase puede escribirse? A) pregunto al educador o a la comunidad B) la escribo igual", "A", "Ellos deciden qué es reservado."),
    ],
    task=T("Tu curso visitará un huerto comunitario inventado, «Huerto Esperanza». Escribe: 1) una invitación de tres líneas para la persona que cuida el huerto (con espacio para el saludo en lengua que te dará el educador), 2) la lista de tres cosas que anotarás en tu nota de campo y 3) una cosa que no escribirás porque sería reservada.",
           "Invitación: [saludo que dará el educador], queremos visitar el huerto el jueves a las 10:00. ¿Nos puede recibir? Gracias. Nota de campo: fecha, lugar y qué cultivos observé. No escribiré: palabras de una reunión que la comunidad pida reservar.",
           ["invitación con saludo pendiente de validar", "tres datos de la nota de campo", "una cosa reservada"], ["invitación", "lista", "frase de límites"], ["inventar el saludo", "escribir lo reservado"],
           "Pedir que muestre dónde deja el espacio para el educador; valorar el límite."),
    reinforce="Une cada situación (invitar, agradecer, salir a terreno) con el texto adecuado.",
    extend="Explica por qué algunas partes de una ceremonia o rogativa no se escriben sin permiso.",
)

L(
    LF4, 2, materials=MAT,
    use="Aprenderé a copiar con exactitud las expresiones en lengua que me dicta el educador o la educadora y a declarar los límites de lo que escribo. Sirve para que mi texto sea respetuoso y correcto.",
    prior=["Sé qué situaciones comunicativas piden un texto.", "Sé que no se inventan expresiones en lengua."],
    explain=[
        "Cuando una expresión en lengua indígena aparece en un texto, debe estar escrita tal como la entrega el educador o la educadora. Se copia con cuidado, letra por letra, y se anota quién la dictó y cuándo. Si dudas de una letra o un signo, preguntas y no cambias nada.",
        "Una misma lengua puede escribirse de más de una manera. Se llaman variantes de escritura, y la comunidad o el educador indican cuál usa su gente. No decimos que una forma es la correcta y otras son erróneas: seguimos la que enseña la comunidad. Para este cuaderno, las únicas expresiones que aparecen son «mari mari» y «chaltumay» (mapuzugun) e «iorana» y «maururu» (rapa nui).",
        "Los límites se escriben al final: qué parte del texto no entiendo, qué no se puede escribir y qué debo consultar. Un buen texto distingue las partes en castellano (que reviso yo) de las partes en lengua (que valida el educador). Escribir esa distinción ayuda a revisar con calma.",
    ],
    vocab=[("dictar", "decir en voz alta lo que otra persona escribirá"), ("variante de escritura", "otra forma de escribir una misma lengua"), ("copiar con exactitud", "escribir sin cambiar letras ni signos"), ("validar", "pedir a quien sabe que confirme que está correcto"), ("límite", "lo que no sé o no se puede escribir")],
    worked=[
        W("Copiar con exactitud", "El educador te dicta «chaltumay» y lo escribes «chaltumai». ¿Qué debes hacer?", ["Comparo con lo que dictó.", "La letra final no coincide.", "Corrijo y pido que lo revise."], "Corregir a «chaltumay» y pedir revisión."),
        W("Declarar la fuente de una expresión", "En una tarjeta escribiste «mari mari». Escribe una nota que atribuya la expresión.", ["Anoto quién la dictó: el educador o la educadora.", "Anoto cuándo: la fecha de hoy.", "Escribo: Expresión dictada por el educador tradicional."], "Nota: «Mari mari» fue dictada por el educador tradicional en la fecha de hoy."),
    ],
    mistakes=[
        M("Cambiar una letra porque «se ve más bonito».", "Se altera la expresión.", "Copia con exactitud."),
        M("Decir que solo una forma de escribir es correcta y las demás son errores.", "Pueden ser variantes de escritura.", "Usa la forma que indique tu comunidad."),
    ],
    R=[
        ex("¿Cómo se copia una expresión en lengua? A) con exactitud, sin cambiar letras B) cambiando lo que no entiendo", "A", "Se copia tal como la entrega el educador."),
        ex("¿Qué significa «iorana»?", "Saludo en rapa nui", "Es un saludo muy conocido."),
        ex("¿Qué se anota junto a una expresión en lengua? A) quién la dictó y cuándo B) el color del lápiz", "A", "Se atribuye la fuente."),
    ],
    C=[
        vf("una misma lengua puede escribirse de más de una manera.", True, "Son variantes de escritura."),
        vf("si dudas de una letra, la cambias a tu gusto.", False, "Se pregunta al educador."),
        ab("¿Quién decide qué variante de escritura usa tu comunidad?", "la comunidad y el educador o la educadora", "el primer resultado de una búsqueda", "Ellos conocen la forma que usa la comunidad."),
    ],
    A=[
        ex("El educador dicta «maururu». Escribes «maruru». ¿Hay error? Responde Sí o No.", "Sí", "Falta una letra respecto de lo dictado."),
        ex("Clasifica en CASTELLANO o LENGUA: a) «Gracias por recibirnos» b) «chaltumay».", "a castellano, b lengua", "La primera frase está en castellano; la segunda es una expresión en mapuzugun."),
        ex("Completa la nota de atribución: «Expresión dictada por… el ______ tradicional». Responde con la palabra.", "Educador o educadora", "Es quien enseña la expresión."),
    ],
    Z=[
        ex("Rodrigo dice: «Escribí ‘mari mari’ de otra manera y es mejor». ¿Qué error comete? A) cambió la expresión sin consultar B) la escribió con lápiz", "A", "No se cambia una expresión sin validar."),
        ex("Carla comparó dos formas de escribir una palabra y dijo que una era «la verdadera». ¿Qué falla? A) puede ser una variante, no hay una verdadera B) usó la regla", "A", "Pueden ser variantes de escritura."),
    ],
    D=[
        ex("Tu texto tiene: un saludo en castellano, «mari mari» y una frase de agradecimiento en castellano. ¿Qué parte debe validar el educador? A) «mari mari» B) el saludo en castellano", "A", "Es la expresión en lengua."),
        ex("Quieres agregar una frase larga en lengua que viste en un afiche en línea. ¿Qué haces? A) pregunto al educador si corresponde y cómo se escribe B) la copio", "A", "No se copia lo que no se sabe si es correcto."),
    ],
    context=[ab("Preparas un cartel de bienvenida con «mari mari». ¿Qué haces antes de imprimirlo?", "lo muestro al educador para que confirme cómo se escribe", "lo imprimo y luego lo corrijo", "La validación va antes de compartir.")],
    selfcheck=[
        ex("Nombra una expresión de esta clase y su significado.", "Una entre: mari mari, saludo en mapuzugun; chaltumay, gracias en mapuzugun; iorana, saludo en rapa nui; maururu, gracias en rapa nui", "Son las expresiones atestiguadas de este cuaderno."),
        vf("conviene separar lo que está en castellano de lo que está en lengua para que cada parte se revise.", True, "Ayuda a validar."),
        ex("¿Qué haces si el educador corrige tu escritura? A) agradezco y corrijo B) discuto", "A", "El educador enseña la lengua."),
    ],
    task=T("Escribe una tarjeta de cuatro líneas para agradecer a una persona de la comunidad que visitó tu curso. Deja un espacio marcado [expresión en lengua] donde irá la que te dicte el educador o la educadora. Anota debajo quién la dictará y qué parte de la tarjeta está en castellano. Agrega una frase de límites.",
           "Tarjeta: Querida visita: [expresión en lengua] Gracias por compartir con nosotros. Fue un gusto recibirla. Nos despedimos con cariño. Nota: la expresión la dictará el educador tradicional; el resto está en castellano. Límite: no sé cómo escribir la expresión.",
           ["deja espacio para la expresión", "atribuye la expresión", "declara límites"], ["tarjeta", "nota"], ["inventar la expresión", "mezclar sin separar"],
           "Pedir que muestre dónde irá la expresión y quién la dictará; valorar el límite."),
    reinforce="Copia con exactitud «mari mari», «chaltumay», «iorana» y «maururu» y compara con el cuaderno.",
    extend="Explica con un ejemplo qué es una variante de escritura y por qué no se dice cuál es la correcta.",
)

L(
    LF4, 3, materials=MAT,
    use="Aprenderé a relacionar la situación (ceremonia, rogativa, salida a terreno) con el tipo de texto, el registro y las partes que lleva. Sirve para escribir textos adecuados y respetuosos.",
    prior=["Sé qué situaciones comunicativas piden un texto.", "Sé distinguir registro formal y no formal."],
    explain=[
        "Un texto adecuado a la situación tiene partes ordenadas. Una invitación lleva saludo, motivo, fecha, hora y lugar, y despedida. Un agradecimiento lleva saludo, qué se agradece y despedida. Una nota de campo lleva fecha, lugar, lo observado y una pregunta pendiente. Conocer las partes ayuda a no olvidar nada.",
        "El registro también depende de la situación. Para invitar a una autoridad tradicional o a una persona mayor usamos registro formal: «usted», frases claras y respetuosas. Para una nota que solo leeremos nosotros, usamos registro no formal y frases breves. El saludo en lengua, cuando corresponde, abre el texto con respeto y se valida con el educador.",
        "En ceremonias y rogativas, lo que se escribe es lo que la comunidad autoriza. Por ejemplo: la fecha, el lugar y quiénes están invitados, pero no las palabras reservadas. En salidas a terreno, lo que observamos lo escribimos con datos exactos, sin interpretar de más. Si dudamos, anotamos una pregunta para el educador o la comunidad.",
    ],
    vocab=[("partes del texto", "pasos ordenados que forman un texto, como saludo, motivo y despedida"), ("motivo", "razón por la que se escribe"), ("autorizado", "que la comunidad permitió escribir o compartir"), ("observación", "dato que veo directamente"), ("pregunta pendiente", "duda anotada para consultar después")],
    worked=[
        W("Ordenar una invitación", "Ordena las partes: a) «Los esperamos en la sala común, a las 10:00» b) «Despedida: gracias por venir» c) «Saludo: Estimado vecino» d) «Motivo: queremos conocer el huerto».", ["Primero va el saludo: c.", "Después el motivo: d, y el lugar y la hora: a.", "Al final la despedida: b."], "Orden: c, d, a, b."),
        W("Elegir el registro", "Escribes a una persona mayor de la comunidad y a tu grupo de trabajo. ¿Qué registro usas en cada caso?", ["La persona mayor merece respeto: formal.", "Con el grupo hay confianza: no formal.", "Cada registro cambia el trato."], "Formal con la persona mayor y no formal con el grupo."),
    ],
    mistakes=[
        M("Escribir una nota de campo con opiniones mezcladas con datos.", "Se confunde lo observado con lo interpretado.", "Escribe datos y deja las ideas para otra línea marcada «yo pienso que»."),
        M("Usar «tú» en una invitación a una autoridad tradicional.", "No respeta el registro formal.", "Usa «usted»."),
    ],
    R=[
        ex("¿Qué parte va primero en una invitación? A) el saludo B) la despedida", "A", "Los textos empiezan saludando."),
        ex("¿Qué datos lleva una nota de campo? A) fecha, lugar y lo observado B) solo el título", "A", "Son sus partes."),
        ex("¿Qué registro usas para invitar a una persona mayor? A) formal B) no formal", "A", "Se muestra respeto."),
    ],
    C=[
        vf("la fecha, el lugar y los invitados de una ceremonia pueden escribirse si la comunidad lo autoriza.", True, "Son datos que la comunidad puede autorizar."),
        vf("las palabras reservadas de una rogativa deben escribirse completas en tu cuaderno.", False, "Lo reservado no se escribe."),
        ab("¿Qué es una pregunta pendiente?", "una duda anotada para consultar al educador", "una respuesta inventada", "Se guarda para consultar después."),
    ],
    A=[
        ex("Ordena las partes de un agradecimiento con letras: a) «Gracias por la visita» b) «Hasta pronto» c) «Querida vecina». Escribe el orden.", "c, a, b", "Saludo, agradecimiento y despedida."),
        ex("Clasifica en OBSERVACIÓN o INTERPRETACIÓN: a) «Vi cuatro surcos de lechuga» b) «Yo pienso que el huerto es muy cuidado».", "a observación, b interpretación", "La primera es un dato; la segunda es una idea."),
        ex("Nota de campo: «Fecha: 15 de mayo. Lugar: huerto. Observé 3 hileras de zapallos y 2 de papas». ¿Cuántas hileras observó en total?", "5", "Se suman 3 y 2."),
    ],
    Z=[
        ex("Julia escribe una invitación para la persona que cuida el huerto sin fecha ni hora. ¿Qué error comete? A) omite datos necesarios B) usa «usted»", "A", "Una invitación necesita fecha, hora y lugar."),
        ex("Víctor escribe en su nota de campo: «El huerto es sagrado». No le dijeron eso. ¿Qué error comete? A) interpreta sin base B) escribe fecha", "A", "No es observación ni fuente."),
    ],
    D=[
        ex("Dos invitaciones: Una lleva saludo, motivo, fecha, hora, lugar y despedida. Otra lleva solo «Vengan». ¿Cuál es más adecuada?", "La primera", "Tiene todas las partes."),
        arith("En una salida contaste 6 hileras de zapallos, 4 de papas y 3 de lechugas. ¿Cuántas hileras anotas en total?", "6+4+3", "Se suman las tres cantidades observadas.", " hileras"),
    ],
    context=[ab("Antes de una salida a terreno, el curso debe decidir qué anotar. ¿Qué eligen?", "datos observados con fecha y lugar", "sus opiniones sin marcarlas", "La nota de campo registra datos.")],
    selfcheck=[
        ex("Nombra tres partes de una invitación.", "Tres entre: saludo, motivo, fecha, hora, lugar, despedida", "Son sus partes."),
        vf("el registro formal se usa con personas mayores y autoridades.", True, "Muestra respeto hacia la persona."),
        ex("¿Qué haces si una duda cultural aparece al escribir? A) la anoto para el educador B) la invento", "A", "Se consulta a quien sabe."),
    ],
    task=T("Escribe una invitación de cinco líneas para que una persona mayor de la comunidad inventada «Huerto Esperanza» visite tu curso el viernes a las 11:00 en la sala común. Debe tener: saludo con espacio para la expresión en lengua que dicte el educador, motivo, fecha y hora, lugar y despedida. Usa registro formal. Subraya cada parte.",
           "[Expresión en lengua que dicte el educador]. Estimada vecina: queremos conocer su experiencia en el huerto. La esperamos el viernes a las 11:00 en la sala común. Le agradecemos de antemano. Un cordial saludo, 6.º básico.",
           ["incluye las seis partes", "usa registro formal", "deja espacio para la expresión en lengua"], ["invitación subrayada"], ["omitir datos", "usar «tú»"],
           "Pedir que señale cada parte; valorar el registro."),
    reinforce="Ordena las partes de una invitación y de un agradecimiento en dos listas.",
    extend="Escribe una nota de campo de cuatro líneas sobre tu patio o plaza, con fecha, lugar y tres observaciones.",
)

L(
    LF4, 4, materials=MAT,
    use="Aprenderé a escribir un texto completo con atribución: quién dictó las expresiones, de qué comunidad es el dato y qué límites se respetaron. Sirve para escribir con respeto y poder revisar.",
    prior=["Sé las partes de una invitación, un agradecimiento y una nota de campo.", "Sé que las expresiones en lengua se copian con exactitud."],
    explain=[
        "Una respuesta atribuida en un texto escrito se parece a una cita: dice quién aportó cada dato. En una nota de campo se escribe «según doña Luz…», y las expresiones en lengua se acompañan de «dictada por el educador». Así quien lee el texto sabe qué viene de la comunidad, qué viene del educador y qué viene de mí.",
        "Un buen texto escrito tiene una sección de límites: qué no entendí, qué no se pudo escribir y qué pienso consultar. También tiene una línea de devolución: a quién mostraré el texto para que lo revise. En una salida a terreno, la devolución puede ser leer la nota de campo a la persona que nos recibió.",
        "El texto final separa las partes por colores o por títulos: datos observados, citas de la fuente, expresiones en lengua y límites. Esta separación ayuda al educador a revisar y evita que mezclemos mis ideas con las de la comunidad.",
    ],
    vocab=[("atribución", "mención de quién aportó cada dato"), ("cita", "frase de la fuente copiada o resumida con su nombre"), ("sección de límites", "parte que dice lo que no entendí o no se pudo escribir"), ("devolución", "mostrar el texto a la fuente para que lo revise"), ("observado", "visto directamente por quien escribe")],
    worked=[
        W("Atribuir en una nota de campo", "Nota: «En Puerto Sereno vi una red tendida. Doña Luz contó que la reparan los miércoles. El educador dictó ‘maururu’ para agradecer». Separa lo observado, lo citado y la expresión.", ["Observado: una red tendida.", "Citado: doña Luz cuenta que la reparan los miércoles.", "Expresión: «maururu», dictada por el educador."], "Observado: la red; citado: doña Luz; expresión: «maururu» dictada por el educador."),
        W("Escribir límites y devolución", "Escribe una frase de límites y una de devolución para esa nota.", ["Límite: no sé por qué reparan los miércoles.", "Devolución: le leeré la nota a doña Luz.", "Las unimos en dos frases."], "Límites: no sé por qué reparan los miércoles. Devolución: le leeré la nota a doña Luz."),
    ],
    mistakes=[
        M("Mezclar lo que vi con lo que me contaron sin decirlo.", "No se sabe qué es dato y qué es relato.", "Separa «observado» de «citado»."),
        M("No decir quién dictó la expresión en lengua.", "Se pierde la atribución.", "Anota «dictada por el educador»."),
    ],
    R=[
        ex("¿Cómo atribuyes un dato a doña Luz? A) «Según doña Luz…» B) «Dicen que…»", "A", "Nombra la fuente."),
        ex("¿Qué dice la sección de límites? A) lo que no entendí o no se pudo escribir B) los mejores datos", "A", "Los límites muestran lo que falta."),
        ex("¿Qué es la devolución? A) mostrar el texto a la fuente para que lo revise B) venderlo", "A", "Es mostrar y agradecer."),
    ],
    C=[
        vf("en un texto, lo observado y lo citado deben separarse.", True, "Así se distingue lo que vi de lo que me contaron."),
        vf("la expresión en lengua puede aparecer sin decir quién la dictó.", False, "Siempre se atribuye."),
        ab("¿Cómo se ayuda al educador a revisar un texto?", "separando los datos, las citas, las expresiones en lengua y los límites", "juntando todo en un solo párrafo", "La separación facilita la revisión."),
    ],
    A=[
        ex("Clasifica en OBSERVADO o CITADO: a) «Vi tres botes en la orilla» b) «Doña Luz contó que salen al amanecer».", "a observado, b citado", "La primera la vio quien escribe; la segunda la contó la fuente."),
        ex("Escribe la atribución de «maururu»: «La expresión ‘maururu’ fue dictada por el ______». Responde con las palabras que faltan.", "Educador o educadora tradicional", "Es quien dicta las expresiones."),
        ex("Un texto dice «No sé cómo se llama el muelle». ¿En qué sección va? A) límites B) observado", "A", "Es algo que no sé."),
    ],
    Z=[
        ex("Marina leyó su nota de campo a la persona que la recibió, quien corrigió un dato. ¿Qué paso del proceso cumplió Marina? A) devolución B) ensayo", "A", "Mostró el texto a la fuente."),
        ex("Iván escribió: «La comunidad cree que la red es sagrada». Doña Luz solo dijo que la reparan los miércoles. ¿Qué error comete?", "Atribuye una creencia que la fuente no dijo", "No está en lo contado."),
    ],
    D=[
        ex("Dos notas de campo del mismo día. Una separa observado, citado y límites. La otra los mezcla en un párrafo. ¿Cuál se revisa mejor?", "La primera", "Está ordenada por tipo de dato."),
        arith("En tu nota de campo anotas 5 observaciones, 3 citas y 2 límites. ¿Cuántas líneas tiene la nota?", "5+3+2", "Se suman las líneas de cada tipo.", " líneas"),
    ],
    context=[ab("Tras una salida a terreno, tu grupo debe presentar sus notas a la comunidad. ¿Qué hacen primero?", "revisar que separen observado, citado y límites", "agregar detalles inventados", "Un texto ordenado y fiel se presenta con respeto.")],
    selfcheck=[
        ex("Nombra las cuatro secciones de un texto ordenado de esta clase.", "Datos observados, citas de la fuente, expresiones en lengua y límites", "Son las secciones que ayudan a revisar."),
        vf("en una devolución se agradece a la persona que ayudó.", True, "Es parte de cerrar el trabajo."),
        ex("¿Qué escribes si no sabes un dato? A) lo anoto como límite B) lo invento", "A", "Los límites evitan inventar."),
    ],
    task=T("Lee estas anotaciones inventadas de una salida a la caleta de Puerto Sereno: «Vi tres botes azules y una red tendida. Doña Luz contó que reparan las redes los miércoles. El educador dictó ‘maururu’ para agradecer. No supe cómo se llama el muelle.» Escribe una nota de campo con cuatro secciones: «Observado», «Citado», «Expresión en lengua» y «Límites». Cierra con una frase de devolución.",
           "Observado: tres botes azules y una red tendida. Citado: según doña Luz, reparan las redes los miércoles. Expresión en lengua: ‘maururu’, dictada por el educador. Límites: no supe cómo se llama el muelle. Devolución: le leeré la nota a doña Luz.",
           ["separa las cuatro secciones", "atribuye cada dato", "incluye devolución"], ["nota de campo ordenada"], ["mezclar tipos de dato", "no atribuir"],
           "Pedir que señale cada sección; valorar la atribución."),
    reinforce="Pinta con tres colores lo observado, lo citado y los límites en la nota de campo.",
    extend="Escribe cómo reordenarías una nota de campo desordenada para que el educador pueda revisarla.",
)

L(
    LF4, 5, materials=MAT,
    use="Aprenderé a contrastar dos versiones escritas de un mismo mensaje sin decir cuál es mejor y a revisar con una lista de verificación. Sirve para mejorar mis textos y respetar variantes.",
    prior=["Sé escribir un texto atribuido.", "Sé que existen variantes de escritura."],
    explain=[
        "Un mismo mensaje se puede escribir de más de una manera según a quién va dirigido. Una versión puede ser más formal y otra más cercana. Ambas pueden ser adecuadas si cumplen su propósito. Contrastar es poner las dos versiones lado a lado y ver qué cambia: el saludo, el trato, las palabras y el cierre.",
        "También existen variantes en la escritura de una expresión en lengua. Si dos personas de la comunidad la escriben distinto, no decimos que una se equivoca: anotamos las dos y preguntamos al educador cuál se usará en el texto y por qué. Así reconocemos que la lengua tiene diversidad.",
        "Para revisar, usamos una lista de verificación con cinco preguntas: ¿tiene todas las partes?, ¿usa el registro adecuado?, ¿atribuye las expresiones en lengua?, ¿respeta lo reservado?, ¿tiene límites y devolución? Si la respuesta a alguna es no, corregimos. Revisar es parte de escribir bien.",
    ],
    vocab=[("versión", "forma en que se escribe un mismo mensaje"), ("contrastar", "comparar dos cosas para ver semejanzas y diferencias"), ("lista de verificación", "serie de preguntas para revisar un texto"), ("propósito", "para qué se escribe un texto"), ("diversidad", "existencia de varias formas distintas")],
    worked=[
        W("Contrastar dos versiones", "Versión A: «Estimada vecina: le agradecemos su visita». Versión B: «Hola vecina: gracias por venir». Contrasta con el criterio «trato».", ["A usa «usted» y saludo respetuoso.", "B usa un saludo cercano.", "Ambas agradecen la visita."], "Semejanza: ambas agradecen. Diferencia: A es formal y B es cercana. No se dice cuál es mejor."),
        W("Usar la lista de verificación", "Texto: tiene saludo y despedida, pero no atribuye la expresión en lengua. ¿Qué corriges?", ["Reviso la pregunta de atribución.", "Falta decir quién dictó la expresión.", "Agrego la atribución."], "Se agrega «dictada por el educador»."),
    ],
    mistakes=[
        M("Decir que una versión es mejor sin pensar en su propósito.", "Cada versión sirve a una audiencia distinta.", "Compara según el propósito."),
        M("Elegir una variante de escritura sin consultar.", "Podría no ser la que usa la comunidad.", "Pregunta al educador."),
    ],
    R=[
        ex("Versión A: «Estimado vecino, lo invitamos». Versión B: «Hola vecino, ven». ¿Cuál usa «usted»? A) la A B) la B", "A", "«Lo invitamos» corresponde al trato formal."),
        ex("¿Cuántas preguntas tiene la lista de verificación de esta clase? Escribe el número.", "5", "Son cinco preguntas en total."),
        ex("¿Qué es contrastar? A) comparar para ver semejanzas y diferencias B) elegir una sola versión", "A", "Es comparar sin elegir un ganador."),
    ],
    C=[
        vf("dos versiones de un mismo mensaje pueden ser adecuadas si sirven a su propósito.", True, "Dependen de la audiencia."),
        vf("si dos personas escriben una expresión distinto, una de ellas se equivoca.", False, "Pueden ser variantes."),
        ab("¿Qué haces para elegir entre dos variantes de escritura?", "pregunto al educador cuál usa la comunidad", "elijo la que más me gusta", "La comunidad decide."),
    ],
    A=[
        ex("Lista de verificación: ¿el texto respeta lo reservado? Texto: «Les contaré qué se dijo en la rogativa». ¿Cumple? Responde Sí o No.", "No", "Dice que contará lo reservado."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) ambas versiones agradecen b) una usa «usted» y la otra «tú».", "a semejanza, b diferencia", "La primera es común; la segunda, distinta."),
        ex("Una versión dice «Estimada vecina» y otra «Querida vecina». ¿Qué criterio las separa? A) el trato B) la fecha", "A", "Una es más formal que la otra."),
    ],
    Z=[
        ex("Tomás dice: «Mi versión es más correcta porque es más corta». ¿Qué error comete? A) usa la longitud como criterio de corrección B) usó un título", "A", "La longitud no define si es adecuada."),
        ex("Elena revisó su texto y respondió «sí» a todas las preguntas, pero no preguntó al educador. ¿Qué falta? A) validación de las expresiones en lengua B) otra hoja", "A", "La lista no reemplaza la validación."),
    ],
    D=[
        ex("Dos tarjetas de agradecimiento. Una tiene saludo, motivo, atribución de la expresión en lengua y despedida. Otra tiene solo «gracias». ¿Cuál cumple más preguntas de la lista?", "La primera", "Tiene más partes de la lista."),
        arith("Un texto responde sí a 4 preguntas de 5 de la lista. ¿Cuántas preguntas le faltan por cumplir?", "5-4", "Se resta lo cumplido del total.", " pregunta"),
    ],
    context=[ab("Tu grupo escribió dos tarjetas para la misma persona de la comunidad: una formal y una cercana. ¿Cuál entregan?", "la que corresponda a la relación con esa persona y la validada por el educador", "la más larga", "La elección depende de la audiencia y la validación.")],
    selfcheck=[
        ex("Nombra dos preguntas de la lista de verificación.", "Dos entre: partes, registro, atribución, reservado, límites y devolución", "Son preguntas de la lista."),
        vf("contrastar versiones es decir cuál es mejor.", False, "Es describir semejanzas y diferencias."),
        ex("¿Qué haces cuando dos personas escriben distinto una expresión? A) consulto al educador B) elijo al azar", "A", "Él valida la variante."),
    ],
    task=T("Lee dos versiones inventadas de un agradecimiento. Versión A: «Estimada vecina: le agradecemos su visita al curso. Fue un gusto escucharla. Hasta pronto.» Versión B: «Hola vecina: gracias por venir. Estuvo muy bueno. Chao.» Haz una tabla con tres criterios: trato, partes y propósito. Escribe una semejanza y una diferencia. Luego revisa la versión A con la lista de verificación y anota qué le falta (por ejemplo, la expresión en lengua con atribución).",
           "Trato: A formal, B cercano. Partes: ambas tienen saludo y despedida. Propósito: agradecer. Semejanza: ambas agradecen. Diferencia: A es más formal. Revisión de A: falta la expresión en lengua dictada por el educador y una línea de devolución.",
           ["tabla con tres criterios", "semejanza y diferencia sin jerarquizar", "revisa con la lista"], ["tabla", "revisión"], ["decir cuál es mejor", "omitir la validación"],
           "Pedir que explique cada criterio; valorar que no ordene de mejor a peor."),
    reinforce="Revisa un texto tuyo con la lista de verificación y marca cuántas preguntas cumple.",
    extend="Escribe una lista de verificación de seis preguntas para revisar una nota de campo.",
)
