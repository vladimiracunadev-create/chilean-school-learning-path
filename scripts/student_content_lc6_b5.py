"""Cuaderno del estudiante, 6.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LR03 (comprender textos orales y escritos de otras culturas, interpretar elementos significativos, valorarlos como
fuentes de conocimiento e incorporar vocabulario pertinente en lengua indígena).

Criterio de autoría: comunidades, personas y textos son INVENTADOS y rotulados. Las únicas palabras en lengua indígena
son «mari mari» y «chaltumay» (mapuzugun) y «iorana» y «maururu» (rapa nui). El vocabulario de cada lengua lo entrega el
educador o la educadora tradicional y aparece como espacio por completar. Las deducciones por contexto se practican con
palabras en castellano. Importa los ayudantes de student_content_lc6_b.
"""
from __future__ import annotations

from student_content_lc6_b import ab, vf, L, M, T, W, MAT
from student_lessons import arith, ex

LR3 = "LC06 OA LR03"

L(
    LR3, 1, materials=MAT,
    use="Aprenderé a situar un texto oral o escrito de otra cultura y a reconocer en él elementos significativos y vocabulario pertinente. Sirve para comprenderlo y valorarlo como fuente de conocimiento.",
    prior=["Sé que un texto oral se dice en voz alta y uno escrito se guarda en letras.", "Sé que el vocabulario en lengua lo enseña el educador."],
    explain=[
        "Los textos de otras culturas pueden ser orales, como un relato contado por una persona mayor, o escritos, como un cartel o una carta. Ambos guardan conocimientos: cómo organizar el trabajo, cómo cuidar un lugar, cómo convivir. Por eso se valoran como fuentes de conocimiento, es decir, textos de los que podemos aprender.",
        "Para comprender un texto lo situamos con una ficha: comunidad, tipo de texto, fuente, permiso y límite. Después buscamos sus elementos significativos: personas, lugares, objetos, acciones que se repiten y expresiones especiales. Algunas de esas expresiones están en lengua indígena; las anotamos aparte en un glosario con su significado y quién las enseñó.",
        "Las únicas palabras en lengua indígena que conocemos en este cuaderno son «mari mari» (saludo en mapuzugun), «chaltumay» (gracias en mapuzugun), «iorana» (saludo en rapa nui) y «maururu» (gracias en rapa nui). Las demás las enseña el educador o la educadora, y mientras tanto dejamos un espacio para completar.",
    ],
    vocab=[("fuente de conocimiento", "texto o persona de quien se aprende algo"), ("elemento significativo", "parte del texto que lleva una idea importante"), ("glosario", "lista de palabras con su significado"), ("pertinente", "que corresponde a lo que se habla y fue validado"), ("tipo de texto", "forma del texto, como relato oral, cartel o carta")],
    worked=[
        W("Situar un texto", "Ficha inventada. Comunidad: Cumbre Nevada (no es un pueblo real). Tipo: texto oral. Fuente: doña Marcela. Permiso: sí. Límite: no se cuenta el cuento de los días largos. ¿Qué tipo de texto es y qué no se cuenta?", ["Tipo: oral.", "Fuente: doña Marcela con permiso.", "El cuento de los días largos no se cuenta."], "Es un texto oral de doña Marcela; no se cuenta el cuento de los días largos."),
        W("Reconocer elementos y vocabulario", "Texto inventado: «Cuando cae la primera nieve guardamos la leña. Mari mari a quien llega». ¿Qué elementos y qué palabra de glosario hay?", ["Elementos: la primera nieve y la leña guardada.", "Palabra de glosario: mari mari.", "Significado: saludo en mapuzugun."], "Elementos: nieve y leña. Glosario: mari mari = saludo."),
    ],
    mistakes=[
        M("Pensar que un cartel vale más que un relato oral.", "Ambos son fuentes de conocimiento.", "Valora ambos."),
        M("Poner una palabra en lengua sin glosario.", "No se sabe qué significa ni quién la enseñó.", "Anota palabra, significado y fuente."),
    ],
    R=[
        ex("Ficha: «Comunidad: Arenal Ancho. Tipo: cartel. Fuente: don Cristóbal.» ¿Qué tipo de texto es? A) escrito B) oral", "A", "Un cartel está escrito."),
        ex("¿Cuál es la fuente de esa ficha?", "Don Cristóbal", "La ficha lo nombra."),
        ex("¿Qué significa «iorana»?", "Saludo en rapa nui", "Es un saludo atestiguado."),
    ],
    C=[
        vf("un texto oral puede ser una fuente de conocimiento.", True, "Transmite saberes de la comunidad."),
        vf("un glosario tiene solo la palabra, sin significado.", False, "Incluye el significado y quién la enseñó."),
        ab("¿Qué es un elemento significativo?", "una parte del texto que lleva una idea importante", "una letra del texto", "Se destaca por su idea."),
    ],
    A=[
        ex("Texto inventado: «Los niños apilan la leña y los mayores cuentan un cuento». Clasifica en PERSONAS o ACCIÓN: a) los niños y los mayores b) apilan la leña.", "a personas, b acción", "La primera nombra quién; la segunda, qué hacen."),
        ex("Texto inventado: «Chaltumay por cuidar el pozo». ¿Qué agradece la persona? A) cuidar el pozo B) cargar leña", "A", "El texto lo dice."),
        ex("Una ficha no trae permiso. ¿Qué haces? A) pido el permiso antes de usarla B) la uso igual", "A", "Sin permiso no se usa."),
    ],
    Z=[
        ex("Rosario dice: «El cartel es una fuente de verdad y el relato oral no». ¿Qué error comete?", "Jerarquiza el texto escrito sobre el oral", "Ambos transmiten saberes."),
        ex("Un niño inventa el significado de «maururu» como «adiós». ¿Qué falla? A) significa gracias en rapa nui B) no tiene tilde", "A", "«Maururu» es gracias."),
    ],
    D=[
        arith("Un texto tiene 3 elementos de personas, 2 de lugares y 4 de acciones. ¿Cuántos elementos tiene en total?", "3+2+4", "Se suman los tres tipos.", " elementos"),
        ex("Un glosario tiene tres palabras: mari mari, chaltumay y [palabra del educador]. ¿Qué significa el espacio entre corchetes? A) falta que el educador la dicte B) es una palabra de fantasía", "A", "No se inventan palabras."),
    ],
    context=[ab("Tu curso recibe un cartel de una comunidad con una palabra en lengua que no conoces. ¿Qué haces?", "pregunto al educador qué significa", "adivino su significado", "El significado lo da quien enseña la lengua.")],
    selfcheck=[
        ex("Nombra dos tipos de elementos significativos.", "Dos entre: personas, lugares, objetos, acciones, expresiones", "Son tipos de la clase."),
        vf("un glosario ayuda a recordar el significado y la fuente de cada palabra.", True, "Esa es su función."),
        ex("¿Quién enseña las palabras de la lengua de tu comunidad? A) el educador o la educadora B) una aplicación", "A", "Ellos enseñan la lengua."),
    ],
    task=T("Lee este texto oral inventado de doña Marcela, de Cumbre Nevada: «Cuando cae la primera nieve, guardamos la leña bajo techo. Los niños la apilan y los mayores cuentan un cuento. Mari mari a quien llega a la casa. Chaltumay por ayudar». Haz una ficha con comunidad, tipo de texto, fuente y límite. Anota tres elementos significativos y un glosario con las dos palabras en lengua.",
           "Comunidad: Cumbre Nevada. Tipo: texto oral. Fuente: doña Marcela. Límite: no sé qué cuento cuentan. Elementos: la primera nieve, la leña, los niños y los mayores. Glosario: mari mari = saludo en mapuzugun; chaltumay = gracias en mapuzugun.",
           ["completa la ficha", "tres elementos", "glosario con significado"], ["ficha completa", "glosario"], ["inventar el cuento", "inventar palabras"],
           "Pedir que señale cada elemento; valorar que deje sin inventar el cuento."),
    reinforce="Subraya en el texto de doña Marcela las dos palabras en lengua y sus significados.",
    extend="Explica por qué un texto oral puede ser tan valioso como uno escrito.",
)

L(
    LR3, 2, materials=MAT,
    use="Aprenderé a leer o escuchar un texto con límites declarados, interpretando sus elementos sin inventar e incorporando el vocabulario pertinente. Sirve para comprender y para saber qué consultar.",
    prior=["Sé situar un texto con su ficha.", "Sé separar lo que dice el texto de lo que interpreto."],
    explain=[
        "Comprender un texto de otra cultura requiere tres pasos: leer o escuchar completo, marcar los elementos significativos y separar lo que el texto dice, lo que yo interpreto y lo que no se explica. Una interpretación válida se apoya en una frase del texto y se marca con «yo pienso que».",
        "Cuando el texto trae palabras en lengua indígena, las leemos dentro de su contexto: observamos qué ocurre antes y después, y si el texto da pistas de su función. Así, «Mari mari a quien llega» sugiere que es un saludo. Pero una pista no reemplaza al significado: para estar seguros preguntamos al educador o a la educadora.",
        "Los límites se declaran con frases como «el texto no explica por qué guardan la leña» o «no sé qué cuento cuentan los mayores». Con los límites, evitamos inventar y dejamos claro qué quedó por preguntar a la comunidad.",
    ],
    vocab=[("contexto", "lo que rodea a una palabra y ayuda a comprenderla"), ("pista", "elemento que ayuda a descubrir una idea"), ("interpretación", "idea propia apoyada en el texto"), ("límite declarado", "frase que dice lo que el texto no explica"), ("confirmar", "asegurarse de que algo es correcto")],
    worked=[
        W("Usar el contexto", "Texto inventado de don Cristóbal, de Arenal Ancho: «Cada familia anota su turno en el cuaderno común. Chaltumay por cuidar el pozo». ¿Qué pista da el contexto sobre «chaltumay»?", ["La frase habla de cuidar el pozo.", "La palabra aparece junto a una acción que se reconoce.", "Sugiere que agradece, pero se confirma con el educador."], "Sugiere que agradece; se confirma con el educador."),
        W("Separar tres cosas", "Texto: «Los niños apilan la leña. Los mayores cuentan un cuento que solo es de la casa». Separa lo que dice, lo que interpreto y lo que no se cuenta.", ["Dice: los niños apilan y los mayores cuentan.", "Interpreto: yo pienso que los niños aprenden con los mayores.", "No se cuenta: el cuento."], "Dice: apilan y cuentan. Interpreto: aprenden con los mayores. No se cuenta: el cuento."),
    ],
    mistakes=[
        M("Dar por cierto un significado que solo deduje.", "Una pista no es confirmación.", "Confirma con el educador."),
        M("Interpretar sin apoyarme en el texto.", "La interpretación queda inventada.", "Busca la frase que la respalda."),
    ],
    R=[
        ex("Texto inventado: «Cada familia anota su turno». ¿Qué anota cada familia? A) su turno B) su receta", "A", "El texto lo dice."),
        ex("¿Qué marca una idea tuya? A) «yo pienso que» B) «el texto afirma que»", "A", "Marca una interpretación."),
        ex("Si el texto no explica algo, ¿qué escribes? A) el texto no lo explica B) lo invento", "A", "Se declara el límite."),
    ],
    C=[
        vf("el contexto puede dar una pista del sentido de una palabra, pero se confirma con el educador.", True, "Una pista no reemplaza al significado."),
        vf("una interpretación válida puede contradecir el texto.", False, "Debe apoyarse en el texto."),
        ab("Para leer palabras en lengua dentro de un texto, ¿qué haces?", "las leo en su contexto y confirmo con el educador", "las cambio por otras", "Primero contexto, luego confirmación."),
    ],
    A=[
        ex("Texto: «Los mayores guardan la leña en la bodega». Clasifica en DICE EL TEXTO o INTERPRETO: a) los mayores guardan la leña b) los mayores son muy ordenados.", "a dice el texto, b interpreto", "La segunda es una suposición."),
        ex("Texto: «Mari mari a quien llega a la casa». ¿Qué pista da el contexto? A) sugiere un saludo B) sugiere una despedida", "A", "Se dirige a quien llega."),
        ex("El texto no dice por qué guardan la leña. ¿Qué escribes en los límites? A) el texto no explica por qué la guardan B) la guardan por frío", "A", "Se declara lo que no se sabe."),
    ],
    Z=[
        ex("Pablo asegura: «Chaltumay significa ‘hasta luego’ porque está al final del texto». ¿Qué error comete?", "Deduce el significado por la posición y no lo confirma", "«Chaltumay» agradece; la posición no lo define."),
        ex("Una niña interpreta: «Yo pienso que cuidar el pozo une a las familias», apoyándose en «cada familia anota su turno». ¿Es válida? A) sí, está marcada y se apoya en el texto B) no", "A", "Es interpretación apoyada."),
    ],
    D=[
        ex("Texto de Cumbre Nevada: «Cuando cae la primera nieve, guardamos la leña bajo techo». Dos interpretaciones. Una: «yo pienso que se prepara el invierno». Otra: «la comunidad cree que la nieve es sagrada». ¿Cuál se apoya en el texto?", "La primera", "La segunda inventa una creencia."),
        ex("Un texto trae una palabra en lengua que no está en tu glosario. ¿Qué haces? A) la anoto con espacio para el significado B) escribo uno inventado", "A", "No se inventan significados."),
    ],
    context=[ab("Lees en un cartel una palabra en lengua que no conoces. Una compañera dice que seguro significa lo mismo que en castellano. ¿Qué le dices?", "que lo confirmemos con el educador", "que tiene razón", "No se adivina el significado.")],
    selfcheck=[
        ex("Nombra los tres pasos para comprender un texto.", "Leer completo, marcar elementos y separar dice, interpreto y no se explica", "Son los pasos."),
        vf("el contexto da pistas, pero no confirma el significado.", True, "La confirmación es del educador."),
        ex("¿Qué escribes junto a una palabra de significado dudoso? A) pregunta pendiente B) un significado inventado", "A", "No se inventa."),
    ],
    task=T("Lee este texto escrito inventado de don Cristóbal, de Arenal Ancho: «Se comparte el agua del pozo por turnos. Cada familia anota su turno en el cuaderno común. Los niños ayudan a sacar el agua. Chaltumay por cuidar el pozo. Hay un lugar del pozo que solo cuida la comunidad.» Haz tres columnas: «El texto dice», «Yo interpreto» y «No se explica». Pon al menos dos datos en cada una. Anota qué pista da el contexto sobre «chaltumay» y confírmala con tu glosario.",
           "El texto dice: se comparte el agua por turnos; cada familia anota su turno. Yo interpreto: yo pienso que los turnos buscan que todos tengan agua. No se explica: el lugar que solo cuida la comunidad. Pista: «chaltumay» está junto a «cuidar el pozo»; confirmación del glosario: gracias en mapuzugun.",
           ["separa tres columnas", "usa la pista del contexto", "confirma con el glosario"], ["tabla", "nota sobre la pista"], ["inventar el lugar reservado", "dar por cierto sin confirmar"],
           "Pedir que indique la frase que apoya cada idea; valorar que confirme con el glosario."),
    reinforce="Subraya con un color lo que dice el texto y con otro lo que interpretas.",
    extend="Escribe dos interpretaciones distintas del texto de Arenal Ancho y señala en qué frase se apoya cada una.",
)

L(
    LR3, 3, materials=MAT,
    use="Aprenderé a relacionar el vocabulario con los saberes que transmite un texto y a deducir el sentido de palabras nuevas por el contexto. Sirve para comprender textos de otras culturas con cuidado.",
    prior=["Sé interpretar con apoyo del texto.", "Sé que una pista no reemplaza la confirmación."],
    explain=[
        "El vocabulario de un texto está relacionado con los saberes que transmite. Si un texto habla de turnos, pozo, cuaderno y agua, esas palabras forman un campo de significado: el cuidado compartido del agua. Reconocer esa relación nos ayuda a comprender el conocimiento del texto, no solo cada palabra.",
        "Para comprender una palabra nueva en castellano usamos el contexto: leemos antes y después, buscamos pistas y probamos un significado. Por ejemplo, en «el aljibe guarda el agua de la lluvia», sabemos por el contexto que un aljibe es un depósito de agua. Con las palabras en lengua indígena hacemos lo mismo solo como pista: confirmamos con el educador o la educadora.",
        "Cada saber pertenece a la comunidad que lo desarrolló. Por eso lo citamos con su fuente: «según don Cristóbal, de Arenal Ancho». Y usamos el vocabulario de manera pertinente: la palabra se usa en el momento adecuado, con el sentido enseñado, y sin cambiarla.",
    ],
    vocab=[("campo de significado", "conjunto de palabras relacionadas con una misma idea"), ("deducir", "sacar una idea a partir de pistas"), ("aljibe", "depósito donde se guarda agua"), ("saber", "conocimiento que una comunidad desarrolla y transmite"), ("citar", "decir de quién es un dato")],
    worked=[
        W("Armar un campo de significado", "Palabras del texto de Arenal Ancho: turno, pozo, cuaderno, agua, nieve. ¿Cuál no pertenece al campo del cuidado compartido del agua?", ["Turno, pozo, cuaderno y agua se relacionan con compartir agua.", "Nieve no aparece en ese texto.", "No pertenece «nieve»."], "No pertenece «nieve»."),
        W("Deducir por contexto", "Oración: «El aljibe guarda el agua de la lluvia para el verano». ¿Qué es un aljibe?", ["La oración dice que guarda agua de lluvia.", "El contexto indica un depósito.", "Es un depósito de agua."], "Un aljibe es un depósito donde se guarda agua."),
    ],
    mistakes=[
        M("Aprender solo palabras sueltas.", "No se comprende el saber.", "Relaciona las palabras con la idea del texto."),
        M("Dar por hecho el significado de una palabra en lengua por una pista.", "Puede estar equivocado.", "Confirma con el educador."),
    ],
    R=[
        ex("¿Qué palabra pertenece al campo del agua? A) pozo B) lápiz", "A", "El pozo guarda agua."),
        ex("¿Qué es un aljibe? A) un depósito de agua B) un animal", "A", "El aljibe guarda agua."),
        ex("¿Cómo se llama el conocimiento que una comunidad desarrolla y transmite? A) saber B) turno", "A", "Es el saber de la comunidad."),
    ],
    C=[
        vf("el contexto ayuda a deducir el sentido de una palabra nueva en castellano.", True, "Las pistas dan sentido."),
        vf("una palabra en lengua se puede cambiar por otra parecida.", False, "Se usa tal como la enseña el educador."),
        ab("¿Qué es un campo de significado?", "palabras relacionadas con una misma idea", "palabras de la misma letra", "Se relacionan por el sentido."),
    ],
    A=[
        ex("Oración: «El canal lleva el agua desde el río hasta la huerta». ¿Qué es un canal? A) un camino para el agua B) un tipo de pan", "A", "El contexto indica que lleva agua."),
        ex("Clasifica cada palabra en AGUA o ANIMALES: a) pozo b) oveja.", "a agua, b animales", "El pozo guarda agua y la oveja es un animal."),
        ex("Tienes el campo «turno, cuaderno, anotar, familias». ¿Qué saber transmite? A) organizar el uso compartido B) cocinar pan", "A", "Las palabras se relacionan con organizar turnos."),
    ],
    Z=[
        ex("Marta dice que una palabra en lengua «significa lo mismo que en castellano» sin consultar. ¿Qué error comete?", "Da por hecho un significado sin confirmar", "El significado lo da el educador."),
        ex("Andrés cita el saber de Arenal Ancho como «lo que hacen todos los pueblos». ¿Qué falla? A) generaliza un saber de una comunidad B) usa letra pequeña", "A", "Cada saber pertenece a una comunidad."),
    ],
    D=[
        ex("Dos listas: una con «turno, pozo, agua, cuaderno»; otra con «turno, nieve, lápiz, pozo». ¿Cuál forma un campo de significado del agua?", "La primera", "Todas se relacionan con el agua."),
        arith("Un glosario tiene 5 palabras en castellano nuevas y 2 en lengua. ¿Cuántas palabras tiene?", "5+2", "Se suman ambas listas.", " palabras"),
    ],
    context=[ab("Preparas un cartel con vocabulario de un texto de una comunidad. ¿Cómo presentas cada palabra?", "con su significado, su fuente y la comunidad", "solo la palabra en grande", "El vocabulario se atribuye.")],
    selfcheck=[
        ex("Escribe una palabra de un campo de significado del agua.", "Pozo, canal, aljibe, río o agua", "Se relacionan con el agua."),
        vf("el vocabulario pertinente se usa con el sentido enseñado.", True, "No se cambia."),
        ex("¿Qué haces con una palabra nueva en lengua? A) la anoto con espacio para el educador B) la invento", "A", "No se inventa."),
    ],
    task=T("Con este texto inventado de don Cristóbal, de Arenal Ancho: «El pozo se comparte por turnos. Cada familia anota su turno en el cuaderno. El aljibe guarda agua de lluvia para el verano. Chaltumay por cuidar el agua», haz: 1) un campo de significado de cuatro palabras, 2) la deducción por contexto de «aljibe», 3) un glosario con las palabras en lengua y 4) una cita del saber con su fuente.",
           "Campo: pozo, turno, cuaderno, agua. Aljibe: depósito donde se guarda agua de lluvia. Glosario: chaltumay = gracias en mapuzugun. Cita: según don Cristóbal, de Arenal Ancho, el pozo se comparte por turnos.",
           ["campo de significado", "deducción por contexto", "glosario", "cita"], ["cuatro respuestas"], ["generalizar", "inventar significados"],
           "Pedir que muestre la pista del contexto; valorar la cita."),
    reinforce="Elige una palabra nueva de un texto y deduce su sentido por contexto.",
    extend="Arma otro campo de significado con cinco palabras de un texto que leas en la escuela.",
)

L(
    LR3, 4, materials=MAT,
    use="Aprenderé a escribir una ficha de lectura que valore un texto de otra cultura como fuente de conocimiento, con idea principal, elementos, vocabulario y fuente. Sirve para comprender y atribuir.",
    prior=["Sé relacionar vocabulario con saberes.", "Sé citar la fuente."],
    explain=[
        "Una ficha de lectura resume un texto de forma ordenada. Tiene cinco partes: título y fuente, idea principal, elementos significativos, vocabulario pertinente (con significado y quién lo enseñó) y una valoración. La valoración explica por qué el texto es una fuente de conocimiento, con una razón tomada del texto.",
        "La idea principal es lo más importante del texto en una frase: por ejemplo, «las familias comparten el agua del pozo por turnos». Los elementos significativos son partes que sostienen esa idea. El vocabulario incluye las palabras en lengua con su significado validado. Y los límites se agregan al final.",
        "La valoración puede decir: «Valoro este texto porque enseña a repartir el agua de forma justa». No usa palabras como «el mejor». Si la ficha va a presentarse a otras personas, la revisa el educador o la comunidad, y se hace la devolución.",
    ],
    vocab=[("ficha de lectura", "resumen ordenado de un texto con sus partes principales"), ("idea principal", "lo más importante del texto en una frase"), ("valoración", "explicación de por qué un texto es valioso"), ("fuente", "persona o texto de quien viene el saber"), ("devolución", "mostrar la ficha a la fuente para que la revise")],
    worked=[
        W("Completar una ficha", "Texto inventado de doña Marcela, de Cumbre Nevada: «Cuando cae la primera nieve, guardamos la leña. Los niños la apilan. Mari mari a quien llega». Completa la ficha.", ["Título y fuente: guardar la leña, doña Marcela.", "Idea principal: se prepara la leña para el invierno entre todos.", "Elementos: nieve, leña, niños. Vocabulario: mari mari = saludo. Valoración: enseña a prepararse juntos."], "Ficha completa con título, idea principal, elementos, vocabulario y valoración."),
        W("Corregir una valoración", "Un niño escribe: «Es el mejor texto del mundo». ¿Qué corriges?", ["«El mejor» no tiene razón.", "La valoración debe explicar qué enseña.", "Debe agregar una razón del texto."], "Se cambia por una razón del texto, como «porque enseña a prepararse juntos»."),
    ],
    mistakes=[
        M("Copiar el texto entero en lugar de resumir.", "La ficha pierde su función.", "Resume en una frase la idea principal."),
        M("Valorar sin razón.", "No queda fundamentada.", "Agrega una razón del texto."),
    ],
    R=[
        ex("¿Cuántas partes tiene la ficha de lectura de esta clase? Escribe el número.", "5", "Son cinco partes en total."),
        ex("¿Qué es la idea principal? A) lo más importante del texto en una frase B) una letra del texto", "A", "Esa es la definición."),
        ex("¿Qué incluye el vocabulario de la ficha? A) significado y quién lo enseñó B) solo el color", "A", "Se atribuye la fuente."),
    ],
    C=[
        vf("la valoración de la ficha debe tener una razón tomada del texto.", True, "Así queda fundamentada."),
        vf("usar «el mejor texto» es una buena valoración.", False, "No tiene razón."),
        ab("¿Quién revisa la ficha antes de compartirla?", "el educador o la comunidad", "nadie", "Ellos validan lo que se dice."),
    ],
    A=[
        ex("Texto: «Se comparte el agua del pozo por turnos». Escribe la idea principal. A) el agua se comparte por turnos B) hay un cuaderno de colores", "A", "Resume el texto."),
        ex("Clasifica en IDEA PRINCIPAL o ELEMENTO: a) el pozo b) las familias comparten el agua por turnos.", "a elemento, b idea principal", "El pozo es una parte; la segunda es la idea completa."),
        ex("Valoración: «Valoro este texto porque enseña a repartir el agua de forma justa». ¿Cuál es la razón? A) enseña a repartir el agua de forma justa B) valoro", "A", "Es lo que explica el valor."),
    ],
    Z=[
        ex("Lucía copia todo el texto en su ficha. ¿Qué error comete?", "No resume la idea principal", "La ficha debe resumir."),
        ex("Una ficha no tiene vocabulario. ¿Qué le falta? A) las palabras en lengua con significado y fuente B) más dibujos", "A", "El vocabulario es parte de la ficha."),
    ],
    D=[
        ex("Dos fichas del mismo texto. Una tiene las cinco partes y la otra solo la idea principal. ¿Cuál es más completa?", "La primera", "Tiene todas las partes."),
        arith("Una ficha tiene 1 idea principal, 3 elementos, 2 palabras de vocabulario y 1 valoración. ¿Cuántos datos tiene?", "1+3+2+1", "Se suman los datos de cada parte.", " datos"),
    ],
    context=[ab("Tu curso hará una exposición de fichas de lectura con textos de comunidades. ¿Qué debe llevar cada una?", "las cinco partes y la fuente de cada texto", "solo un dibujo", "Así se atribuye y se valora.")],
    selfcheck=[
        ex("Nombra tres partes de la ficha de lectura.", "Tres entre: título y fuente, idea principal, elementos, vocabulario y valoración", "Son partes de la clase."),
        vf("la ficha se muestra a la fuente para que la revise.", True, "Es la devolución."),
        ex("¿Qué haces con el vocabulario que no te enseñaron? A) dejo un espacio para el educador B) lo invento", "A", "No se inventa."),
    ],
    task=T("Completa una ficha de lectura con este texto inventado de don Cristóbal, de Arenal Ancho: «Se comparte el agua del pozo por turnos. Cada familia anota su turno en el cuaderno común. Los niños ayudan a sacar el agua. Chaltumay por cuidar el pozo». La ficha tiene: título y fuente, idea principal, tres elementos, vocabulario (con significado y fuente) y una valoración que empiece con «Valoro este texto porque…». Agrega una frase de devolución.",
           "Título: El pozo compartido (don Cristóbal). Idea principal: las familias comparten el agua del pozo por turnos. Elementos: pozo, cuaderno, niños. Vocabulario: chaltumay = gracias en mapuzugun. Valoración: valoro este texto porque enseña a repartir el agua de forma justa. Devolución: le mostraré la ficha a don Cristóbal.",
           ["las cinco partes", "razón en la valoración", "devolución"], ["ficha completa"], ["copiar todo el texto", "valorar sin razón"],
           "Pedir que señale cada parte; valorar la razón."),
    reinforce="Subraya con cinco colores las cinco partes de tu ficha.",
    extend="Escribe una segunda valoración del mismo texto con otra razón.",
)

L(
    LR3, 5, materials=MAT,
    use="Aprenderé a contrastar un texto oral y un texto escrito de comunidades distintas sin decir cuál es mejor, valorando ambos como fuentes de conocimiento. Sirve para dialogar entre culturas.",
    prior=["Sé completar una ficha de lectura.", "Sé contrastar con los mismos criterios."],
    explain=[
        "Dos textos de comunidades distintas pueden hablar de saberes parecidos, pero cada uno lo cuenta a su manera. Uno puede ser oral, con pausas, tono y repetición; otro puede ser escrito, con letras fijas que se leen muchas veces. Contrastarlos es ponerlos lado a lado con los mismos criterios.",
        "Los criterios útiles son: qué saber transmite, quién lo cuenta, cómo se transmite y qué vocabulario aparece. Anotamos semejanzas y diferencias con «en cambio» y «a diferencia de». Evitamos decir que el texto escrito es más confiable o que el oral es más antiguo, porque esas son jerarquías sin fundamento.",
        "Valorar ambos como fuentes de conocimiento significa reconocer que cada uno nos enseña algo valioso. Una buena valoración compara y a la vez reconoce el aporte de cada texto: «Valoro el relato de Cumbre Nevada porque enseña a prepararse juntos y valoro el cartel de Arenal Ancho porque organiza el uso del agua».",
    ],
    vocab=[("contrastar", "poner dos cosas lado a lado para ver semejanzas y diferencias"), ("jerarquía", "orden de lo mejor a lo peor"), ("confiable", "que se puede creer porque tiene una fuente clara"), ("aporte", "lo que algo o alguien entrega a otros"), ("criterio", "punto igual para comparar")],
    worked=[
        W("Contrastar dos textos", "Texto A (oral, Cumbre Nevada): se guarda la leña entre niños y mayores. Texto B (escrito, Arenal Ancho): se comparte el agua por turnos anotados en un cuaderno. Contrasta con el criterio «cómo se transmite».", ["A se transmite hablando y escuchando.", "B se transmite escrito en un cartel y un cuaderno.", "Semejanza: ambos enseñan a organizarse. Diferencia: uno es oral y el otro, escrito."], "Ambos enseñan a organizarse en comunidad; A es oral y B, escrito. No se dice cuál es mejor."),
        W("Evitar la jerarquía", "Un niño dice: «El cartel es más confiable que el relato». ¿Qué corriges?", ["«Más confiable» es un orden.", "Ambos tienen fuente clara.", "Debe describir qué aporta cada uno."], "Debe describir el aporte de cada texto, sin ordenar."),
    ],
    mistakes=[
        M("Decir que un texto escrito siempre es más confiable.", "Un texto oral con fuente clara también lo es.", "Revisa la fuente y el permiso de cada texto."),
        M("Comparar con criterios distintos para cada texto.", "La comparación deja de ser justa.", "Usa los mismos criterios."),
    ],
    R=[
        ex("En el texto de Arenal Ancho, ¿cómo se anotan los turnos? A) en un cuaderno B) en una pizarra", "A", "El texto lo dice."),
        ex("En el texto de Cumbre Nevada, ¿qué se guarda? A) la leña B) el agua", "A", "El texto habla de la leña."),
        ex("¿Qué expresión marca una diferencia sin ordenar? A) «en cambio» B) «es mejor»", "A", "Describe sin jerarquizar."),
    ],
    C=[
        vf("contrastar dos textos es decir cuál es el mejor.", False, "Contrastar es ver semejanzas y diferencias."),
        vf("un texto oral y uno escrito pueden ser igualmente valiosos como fuentes.", True, "Ambos transmiten saberes."),
        ab("¿Qué debe haber en cada texto para usarlo como fuente?", "fuente clara y permiso", "letra bonita", "Sin fuente ni permiso no se usa."),
    ],
    A=[
        ex("Criterio «qué saber transmite». A: prepararse juntos para el invierno. B: repartir el agua por turnos. ¿Qué diferencia hay? A) cada texto enseña un saber distinto B) ambos enseñan lo mismo", "A", "Los saberes son distintos."),
        ex("Clasifica en SEMEJANZA o DIFERENCIA: a) en ambos textos hay una comunidad organizada b) uno es oral y el otro, escrito.", "a semejanza, b diferencia", "La primera es común; la segunda, distinta."),
        ex("Completa: «A diferencia del relato de Cumbre Nevada, el cartel de Arenal Ancho…» A) está escrito B) es oral", "A", "El cartel es un texto escrito."),
    ],
    Z=[
        ex("Gonzalo dice: «El relato oral no sirve porque no se puede archivar». ¿Qué error comete?", "Piensa que solo lo escrito sirve como fuente", "El oral transmite saberes."),
        ex("Una niña valora solo el texto escrito y no menciona el oral. ¿Qué falta? A) reconocer el aporte del texto oral B) más letra", "A", "Se valoran ambos."),
    ],
    D=[
        ex("Dos valoraciones: Una: «Valoro el relato porque enseña a prepararse juntos y el cartel porque organiza el agua». Otra: «Valoro solo el cartel porque es escrito». ¿Cuál valora ambos?", "La primera", "La segunda ignora el relato."),
        arith("Comparas 2 textos con 4 criterios cada uno. ¿Cuántas anotaciones haces en total?", "2*4", "Se multiplican los textos por los criterios.", " anotaciones"),
    ],
    context=[ab("Para un diario mural escolar, tienes un relato oral y un cartel de dos comunidades. ¿Cómo los presentas?", "con la fuente de cada uno y su aporte", "solo con el cartel", "Se valoran ambos con su fuente.")],
    selfcheck=[
        ex("Escribe una semejanza entre los textos de Cumbre Nevada y Arenal Ancho.", "En ambos las personas se organizan en comunidad", "Aparece en los dos textos."),
        vf("al contrastar usamos los mismos criterios con los dos textos.", True, "Así la comparación es justa."),
        ex("¿Qué haces si dudas del vocabulario en lengua de alguno? A) lo confirmo con el educador B) lo invento", "A", "Él enseña la lengua."),
    ],
    task=T("Contrasta estos dos textos inventados. A (oral, doña Marcela, Cumbre Nevada): «Cuando cae la primera nieve, guardamos la leña. Los niños la apilan. Mari mari a quien llega». B (escrito, don Cristóbal, Arenal Ancho): «El pozo se comparte por turnos. Cada familia anota su turno. Chaltumay por cuidar el agua». Haz una tabla con cuatro criterios: saber que transmite, quién lo cuenta, cómo se transmite y vocabulario. Escribe una semejanza, una diferencia y una valoración de ambos que empiece con «Valoro…» y no use «mejor».",
           "Saber: A prepararse juntos para el invierno; B repartir el agua por turnos. Quién: doña Marcela; don Cristóbal. Cómo: oral; escrito. Vocabulario: mari mari = saludo; chaltumay = gracias. Semejanza: ambos enseñan a organizarse. Diferencia: uno es oral y el otro, escrito. Valoro el relato porque enseña a prepararse juntos y el cartel porque organiza el uso del agua.",
           ["tabla de cuatro criterios", "semejanza y diferencia", "valora ambos sin ordenar"], ["tabla", "valoración"], ["decir cuál es mejor", "inventar vocabulario"],
           "Pedir que explique cada celda; valorar que reconozca el aporte de ambos."),
    reinforce="Cambia tres frases que ordenan de mejor a peor por frases que describen el aporte de cada texto.",
    extend="Explica por qué un texto oral y uno escrito pueden complementarse en una comunidad.",
)
