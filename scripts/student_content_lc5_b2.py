"""Cuaderno del estudiante, 5.º básico, Lengua y Cultura de los Pueblos Originarios Ancestrales.

OA LF03 (textos escritos sobre la realidad familiar, local y territorial) y OA LF04 (escritura, aglutinación y
reduplicación).

Criterio de autoría: todos los textos, cartas, fichas y personas son INVENTADOS y están en castellano; no pertenecen a
ningún pueblo. No se afirma ninguna palabra, gramática ni forma de escritura de una lengua indígena concreta. Para
practicar la aglutinación (pegar piezas con significado) y la reduplicación (repetir una raíz) se usa una «lengua de
práctica» inventada, Tolu, cuyas reglas se escriben completas en cada ejercicio y que se rotula como inventada. La única
información real de lengua es el nombre mapuche en dos escrituras en uso (mapuzugun, mapudungun) y la descomposición
muy difundida de «mapuche» (mapu, tierra + che, gente) y «mapuzugun» (mapu, tierra + zugun, habla), señalada para
revisión del educador/a tradicional. Las formas reales de aglutinar y reduplicar en la lengua de cada comunidad las
enseña el educador/a tradicional.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

LF3, LF4 = "LC05 OA LF03", "LC05 OA LF04"

CONSULT = " Recuerda: lo tradicional lo enseñan el educador o la educadora tradicional y tu comunidad. Consúltales antes de dar tu trabajo por terminado."
FEEDBACK_ADD = " Si surge una duda cultural o de lengua, no corregir desde la sala: invitar a consultar al educador/a tradicional o a la comunidad. No evaluar la identidad ni la fluidez de nadie."


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement + CONSULT, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback + FEEDBACK_ADD}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": C, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


MAT = "Lápiz y hojas. Los textos, las fichas y las reglas están escritos en este cuaderno y son inventados para practicar; no son de ningún pueblo."

# ------------------------------------------------------------------ textos de práctica (LF03)
CARTA = ("Carta de práctica (inventada): «Querida Ema: Hoy fui con mi curso a la vertiente del pueblo. Llevamos pan y agua en un termo. "
         "Una vecina nos explicó que la vertiente se limpia entre todos cada primavera. Después caminamos hasta el cerro y vimos un cóndor. "
         "Escríbeme pronto. Un abrazo, Camila.»")
CALETA = ("Texto de práctica «Mi caleta» (inventado): «Mi caleta se llama Roca Alta. Tiene una playa de arena gris y doce botes pintados de colores. "
          "En la mañana los pescadores salen al mar y en la tarde las personas ayudan a descargar. En el centro hay una sede donde nos reunimos cada mes.»")
HUERTA = ("Texto de práctica «La huerta de doña Elena» (inventado): «Doña Elena vive junto al camino. En su huerta siembra papas, habas y zapallos. "
          "Los domingos reparte verduras a los vecinos. Dice que cuando la tierra descansa, después da más. Su ayudante, Mateo, riega con un balde.»")
FICHA_T = ("Ficha de texto (inventada). Tipo: carta. Autora: Camila. Destinataria: Ema. Tema: una salida del curso a la vertiente. "
           "Lengua original: una lengua indígena de práctica; la versión en castellano es de apoyo y el texto original lo lee el educador tradicional. "
           "Permiso: Camila autorizó usar la carta en la escuela. Límite: no se publica el nombre del pueblo.")

# ============================================================ OA LF03 · textos culturales, familiares y territoriales
L(
    LF3, 1,
    materials=MAT,
    use="Aprenderé a situar un texto escrito sobre la familia, el lugar o el territorio: de qué tipo es, quién lo escribió, para quién y con qué permiso. Sirve para leer textos de la cultura con respeto y sin confundir su procedencia.",
    prior=["Sé situar un relato con una ficha de seis datos.", "Sé que lo reservado por una comunidad no se publica."],
    explain=[
        "Un texto escrito puede hablar de la familia, del lugar donde vivimos o del territorio de una comunidad. Hay textos de distintos tipos: una carta cuenta algo a otra persona, una descripción dice cómo es un lugar y un relato cuenta lo que le pasó a alguien. Saber el tipo de texto ayuda a leerlo bien.",
        "Antes de leer, situamos el texto con una ficha: tipo, autor o autora, destinatario, tema, lengua original, permiso y límite. Algunos textos están escritos originalmente en una lengua indígena; en este cuaderno usamos una versión en castellano de apoyo, y el texto original lo lee el educador o la educadora tradicional. La versión de apoyo no reemplaza al original.",
        "Un texto cuenta la mirada de quien lo escribió, no la de todos los pueblos. Por eso no generalizamos: lo que dice la carta de Camila vale para Camila y su pueblo de práctica. Si falta la autoría o el permiso, no usamos el texto. Y si una parte está reservada, la respetamos aunque no sepamos por qué.",
    ],
    vocab=[("carta", "texto que una persona escribe a otra para contarle algo"), ("descripción", "texto que dice cómo es un lugar, una persona o una cosa"), ("autor o autora", "persona que escribió el texto"), ("destinatario", "persona a quien va dirigido un texto"), ("versión de apoyo", "traducción que ayuda a entender, pero no reemplaza al original")],
    worked=[
        W("Leer la ficha de un texto", FICHA_T + " ¿Quién escribió la carta y para quién?", ["Busco «Autora» y «Destinataria».", "Autora: Camila. Destinataria: Ema."], "Camila escribió la carta para Ema."),
        W("Detectar un dato que falta", "Ficha: «Tipo: descripción. Tema: una caleta. Permiso: sí». ¿Qué dato falta para usarla bien?", ["Reviso autor, destinatario y límite.", "No aparece quién la escribió."], "Falta la autoría."),
    ],
    mistakes=[
        M("Usar un texto sin saber quién lo escribió.", "Se pierde su procedencia y no se puede atribuir.", "Busco el dato de autoría o pregunto a la persona responsable."),
        M("Pensar que la versión en castellano es el texto original.", "La versión de apoyo no reemplaza el original en lengua indígena.", "Aclaro que es una versión de apoyo y pido al educador que lea el original."),
    ],
    R=[
        ex(FICHA_T + " ¿Qué tipo de texto es?", "Una carta", "El primer dato de la ficha lo dice."),
        ex(FICHA_T + " ¿Quién es la destinataria?", "Ema", "La ficha la nombra."),
        ex("Un texto que dice cómo es un lugar es: A) una descripción B) una carta", "A", "Describir es decir cómo es algo."),
    ],
    C=[
        ex("Verdadero o falso: la versión en castellano de apoyo reemplaza al texto original en lengua indígena.", "Falso", "Solo ayuda a entender."),
        ex("¿Para qué sirve el dato «Límite» de la ficha? A) para saber qué no se publica B) para saber cuántas páginas tiene", "A", "El límite protege lo que debe reservarse."),
        ex("Verdadero o falso: una carta de una persona cuenta lo que piensan todos los pueblos.", "Falso", "Cuenta la mirada de quien escribe."),
    ],
    A=[
        ex(FICHA_T + " ¿Se puede publicar el nombre del pueblo de Camila? Responde Sí o No.", "No", "El límite lo prohíbe."),
        ex("Une cada tipo con su función. 1) carta 2) descripción 3) relato. a) cuenta lo que le pasó a alguien b) escribe a otra persona c) dice cómo es un lugar", "1-b, 2-c, 3-a", "Cada tipo de texto tiene una función distinta."),
        ex("Ficha: «Tipo: carta. Tema: una salida a la vertiente. Destinataria: Ema. Permiso: sí». ¿Qué dato falta: la autoría o el tema?", "La autoría", "El tema aparece, pero no quién escribió."),
    ],
    Z=[
        ex("Una compañera dice: «Como la carta de Camila habla de limpiar una vertiente, todas las comunidades lo hacen cada primavera». ¿Qué error comete?", "Generaliza lo que dice un texto", "La carta habla de una vecina y un pueblo de práctica."),
        ex("Solo tienes la versión en castellano de apoyo de un texto. ¿Qué dices al presentarlo? A) que es una versión de apoyo y que el original lo lee el educador tradicional B) que el original está en castellano", "A", "Se declara la procedencia."),
    ],
    D=[
        ex("Tres textos: la carta de Camila (permiso sí), un texto sin autoría y otro con permiso «no». ¿Con cuál puedes trabajar?", "Con la carta de Camila", "Solo ella tiene autoría y permiso."),
        ex("Si no sabes leer el original en lengua indígena, ¿qué haces? A) pido al educador o a una persona de la comunidad que lo lea B) invento lo que dice", "A", "Solo ellos pueden leerlo con seguridad."),
    ],
    context=[ex("En tu escuela una vecina deja una carta escrita por su hijo para leerla en clases. No indica si se puede leer en voz alta. ¿Qué haces primero? A) preguntarle si hay permiso y qué límites tiene B) leerla igual", "A", "Primero el permiso y los límites.")],
    selfcheck=[
        ex("Nombra tres datos de la ficha de un texto.", "Tres entre: tipo, autor, destinatario, tema, lengua original, permiso, límite", "Son datos de la ficha."),
        ex("Verdadero o falso: un texto puede estar escrito originalmente en una lengua indígena.", "Verdadero", "En ese caso se usa una versión de apoyo."),
        ex("¿Qué haces si falta el permiso? A) me detengo y pregunto B) lo uso igual", "A", "Sin permiso no se usa."),
    ],
    task=T("Lee la ficha y la carta de práctica: «" + FICHA_T + "» «" + CARTA.split("«", 1)[1].rstrip("»") + "» Haz una ficha propia con: tipo, autora, destinataria, tema, permiso y límite, y agrega una línea «Esto no lo sé:» con un dato que la ficha no trae. Escribe también una pregunta para el educador tradicional sobre cómo se escribe una carta en la lengua de tu comunidad.",
           "Tipo: carta. Autora: Camila. Destinataria: Ema. Tema: salida a la vertiente. Permiso: sí. Límite: no publicar el nombre del pueblo. Esto no lo sé: en qué mes ocurrió la salida. Pregunta: ¿cómo se escribe un saludo al comenzar una carta en nuestra lengua?",
           ["completa seis datos", "declara lo que no sabe", "formula una pregunta respetuosa"], ["ficha completa", "línea de lo que no sabe", "pregunta escrita"], ["agregar datos inventados", "generalizar a todos los pueblos"],
           "Pedir que muestre en qué línea de la ficha o de la carta está cada dato; valorar que deje en blanco lo no declarado."),
    reinforce="Copia la ficha de la carta y subraya la autoría y el límite con colores distintos.",
    extend="Escribe una ficha para un texto inventado tuyo que describa un lugar de tu comunidad, con los siete datos.",
)

L(
    LF3, 2,
    materials=MAT,
    use="Aprenderé a leer un texto sobre la vida familiar y local comprendiéndolo y declarando lo que dice, lo que no dice y lo que queda reservado. Sirve para no atribuirle al texto cosas que no contó.",
    prior=["Sé situar un texto con una ficha.", "Sé distinguir lo que dice una fuente de lo que yo imagino."],
    explain=[
        "Leer con comprensión es entender quién hace qué, dónde y cuándo. En una carta o en una descripción buscamos los hechos y los marcamos con lápiz: lugar, personas, acciones y objetos. Luego los resumimos con palabras propias, sin copiar frases enteras. Si no entendemos una palabra, la anotamos y la preguntamos.",
        "Leer con límites declarados es decir en voz alta tres cosas: lo que el texto dice, lo que no dice y lo que está reservado. En la carta de Camila, por ejemplo, no se dice cómo se llama la vecina ni de qué pueblo es. Eso no lo completamos con la imaginación. Si alguien lo pregunta, respondemos: «El texto no lo dice».",
        "Las palabras de un texto de la cultura pueden tener un sentido especial para la comunidad. Si una palabra no la conocemos, no inventamos su significado: la subrayamos y la consultamos al educador tradicional o a una persona de la comunidad. Eso también es leer con respeto.",
    ],
    vocab=[("comprensión", "entender lo que dice un texto"), ("resumir", "decir con pocas palabras y con las propias lo más importante"), ("hecho", "algo que ocurre en el texto"), ("límite del texto", "lo que el texto no dice"), ("subrayar", "marcar una palabra o frase para volver a ella")],
    worked=[
        W("Marcar los hechos", CARTA + " ¿Dónde fue Camila y con quién?", ["Busco el lugar: la vertiente del pueblo.", "Busco con quién: con su curso."], "Fue a la vertiente con su curso."),
        W("Lo que el texto no dice", CARTA + " ¿Dice cómo se llama la vecina?", ["Reviso la carta.", "Solo dice «una vecina»."], "No, el texto no lo dice."),
    ],
    mistakes=[
        M("Responder con lo que imagino y no con lo que dice el texto.", "Atribuyo al texto algo que no contó.", "Vuelvo al texto y marco la frase que lo apoya."),
        M("Copiar frases enteras al resumir.", "No compruebo que entendí.", "Resumo con mis palabras y cito la frase solo si es necesario."),
    ],
    R=[
        ex(CARTA + " ¿Qué llevaron en el termo?", "Pan y agua", "La carta dice que llevaron pan y agua en un termo."),
        ex(CARTA + " ¿Qué animal vieron cerca del cerro?", "Un cóndor", "La carta lo menciona."),
        ex(CARTA + " ¿Con qué palabras se despide Camila: «Un abrazo» o «Hasta nunca»?", "Un abrazo", "Es la despedida de la carta."),
    ],
    C=[
        ex(CARTA + " ¿Cada cuánto tiempo se limpia la vertiente según la vecina?", "Cada primavera", "La carta lo dice así."),
        ex(CARTA + " Verdadero o falso: la carta dice que la vecina se llama doña Rosa.", "Falso", "Solo dice «una vecina»."),
        ex("Si no entiendes una palabra de un texto de la cultura, ¿qué haces? A) la subrayo y pregunto al educador B) invento un significado", "A", "No se inventa el significado."),
    ],
    A=[
        ex(CARTA + " Ordena lo que hizo el curso: a) vio un cóndor b) fue a la vertiente c) caminó hasta el cerro. Escribe las letras.", "b, c, a", "La carta cuenta primero la vertiente, luego el cerro y allí el cóndor."),
        ex(CARTA + " ¿Cuál afirmación está en la carta? A) la vertiente se limpia entre todos B) la vertiente se seca cada verano", "A", "La B no aparece."),
        ex(CARTA + " ¿Qué resumen es fiel a la carta? A) Camila cuenta a Ema que fue con su curso a la vertiente y al cerro B) Camila cuenta a Ema que fue sola a un río", "A", "La B cambia con quién fue y adónde."),
    ],
    Z=[
        ex("Tomás dice: «En la carta se ve que el pueblo de Camila hace una fiesta en primavera». ¿Está en el texto? Responde Sí o No.", "No", "La carta habla de limpiar la vertiente, no de una fiesta."),
        ex("Una niña pregunta cómo se llama el pueblo de Camila y la ficha dice que ese dato no se publica. ¿Qué respuesta respeta el límite? A) «Ese dato no se publica» B) «Seguro es Villa Sur»", "A", "La B inventa un dato."),
    ],
    D=[
        ex("Dos resúmenes de la carta. R1: «Camila fue a la vertiente con su curso y vio un cóndor». R2: «Camila fue a la vertiente con su familia y vio un cóndor». ¿Cuál es fiel al texto?", "R1", "La R2 cambia a quién acompañaba."),
        ex(CARTA + " ¿A qué lugar caminó el curso después de la vertiente?", "Al cerro", "La carta dice que caminaron hasta el cerro."),
    ],
    context=[ex("Un vecino te muestra un texto escrito por una persona de su comunidad y te pide que lo expliques en clases, pero hay una palabra que no entiendes. ¿Qué haces? A) pregunto qué significa o consulto al educador B) digo lo que me parece", "A", "El significado lo da quien conoce el texto.")],
    selfcheck=[
        ex("Escribe qué tres cosas se declaran al leer con límites.", "Lo que el texto dice, lo que no dice y lo reservado", "Son los tres límites de la lectura."),
        ex(CARTA + " ¿A quién escribe Camila?", "A Ema", "Lo dice el saludo."),
        ex("Verdadero o falso: puedo completar con mi imaginación lo que el texto no cuenta.", "Falso", "Hay que decir que el texto no lo dice."),
    ],
    task=T("Lee la carta de Camila: «" + CARTA.split("«", 1)[1].rstrip("»") + "» Haz una tabla de tres columnas: «El texto dice» (cuatro datos), «El texto no dice» (dos datos) y «Palabras que consultaría» (una palabra o expresión que no entiendas del todo). Escribe luego un resumen de dos frases con tus propias palabras.",
           "El texto dice: fue a la vertiente con su curso; llevaron pan y agua; la vecina dijo que la vertiente se limpia cada primavera; vieron un cóndor. No dice: cómo se llama la vecina; en qué mes ocurrió. Consultaría: «primavera» en la lengua de mi comunidad. Resumen: Camila fue con su curso a la vertiente y al cerro. Una vecina explicó que la vertiente se limpia entre todos.",
           ["registra datos fieles al texto", "identifica lo que no dice", "resume con palabras propias"], ["tabla de tres columnas", "resumen de dos frases"], ["agregar datos que no están", "copiar la carta entera"],
           "Pedir que señale la frase de la carta de cada dato; valorar que reconozca lo que el texto no dice."),
    reinforce="Subraya en la carta los lugares con un color y las personas con otro.",
    extend="Escribe tres preguntas que la carta no responde y que podrías hacerle a una persona de la comunidad.",
)

L(
    LF3, 3,
    materials=MAT,
    use="Aprenderé a reconocer y analizar elementos significativos de la cultura en textos sobre la vida local: lugares, oficios, alimentos y formas de ayudarse. Sirve para valorar lo que los textos muestran sin inventar significados.",
    prior=["Sé leer un texto con límites declarados.", "Sé que un texto cuenta la mirada de quien lo escribe."],
    explain=[
        "Un elemento significativo de la cultura es algo que aparece en el texto y que tiene un valor especial para la comunidad: un lugar donde se reúnen, un oficio que se realiza, un alimento que se cultiva o una forma de ayudarse. Para encontrarlos hacemos una pregunta al texto: ¿qué lugares, trabajos, alimentos y acciones comunitarias aparecen?",
        "Podemos ordenarlos en una tabla con cuatro columnas: lugares, oficios, alimentos y cooperación. En «Mi caleta» el lugar es la sede, el oficio es la pesca y la cooperación es ayudar a descargar. En «La huerta de doña Elena», los alimentos son las papas, las habas y los zapallos, y la cooperación es repartir verduras a los vecinos.",
        "Analizar es explicar qué muestra cada elemento, sin pasar de lo que dice el texto. Valorar es reconocer su importancia con respeto. Por ejemplo, repartir verduras muestra que se comparte. Pero no podemos decir por qué lo hacen ni qué creencia hay detrás: eso lo explica la comunidad. Si queremos saber más, preguntamos.",
    ],
    vocab=[("elemento significativo", "algo del texto que tiene valor especial para la comunidad"), ("oficio", "trabajo que una persona sabe hacer"), ("cooperación", "ayudarse entre varias personas"), ("analizar", "explicar qué muestra cada parte de un texto"), ("valorar", "reconocer la importancia de algo con respeto")],
    worked=[
        W("Clasificar elementos", CALETA + " Clasifica: la sede, los pescadores, ayudar a descargar.", ["La sede es un lugar.", "Los pescadores tienen un oficio.", "Ayudar a descargar es cooperación."], "Sede: lugar. Pescadores: oficio. Ayudar a descargar: cooperación."),
        W("Analizar sin inventar", HUERTA + " ¿Qué muestra que doña Elena reparta verduras?", ["El texto dice que las reparte a los vecinos.", "Eso muestra que se comparte."], "Que se comparte; el texto no dice por qué lo hace."),
    ],
    mistakes=[
        M("Explicar la creencia que hay detrás de una práctica que el texto no explica.", "Invento un significado.", "Describo lo que el texto muestra y pregunto el resto a la comunidad."),
        M("Clasificar sin volver al texto.", "Puedo equivocar la categoría.", "Busco la frase que lo justifica."),
    ],
    R=[
        ex(CALETA + " ¿Dónde se reúnen en la caleta?", "En la sede", "El texto dice que hay una sede donde se reúnen."),
        ex(HUERTA + " ¿Qué siembra doña Elena además de papas y habas?", "Zapallos", "El texto lo menciona."),
        ex(CALETA + " ¿En qué momento del día salen los pescadores?", "En la mañana", "El texto lo dice."),
    ],
    C=[
        ex("Un oficio es: A) un trabajo que una persona sabe hacer B) un lugar de reunión", "A", "Oficio es trabajo."),
        ex("Verdadero o falso: puedo explicar la creencia detrás de una práctica aunque el texto no la cuente.", "Falso", "Eso lo explica la comunidad."),
        ex(HUERTA + " ¿Qué elemento de cooperación aparece: repartir verduras a los vecinos o vivir junto al camino?", "Repartir verduras a los vecinos", "Repartir es compartir con otros; vivir junto al camino es un lugar."),
    ],
    A=[
        ex(CALETA + " Clasifica «los pescadores salen al mar» como: A) lugar B) oficio C) alimento", "B", "Salir a pescar es un trabajo."),
        ex("Une cada elemento con su categoría. 1) la sede 2) los zapallos 3) ayudar a descargar. a) alimento b) lugar c) cooperación", "1-b, 2-a, 3-c", "Cada elemento corresponde a una columna de la tabla."),
        ex(HUERTA + " Escribe qué muestra que «cuando la tierra descansa, después da más», con la palabra «según doña Elena».", "Según doña Elena, la tierra necesita descansar para dar más", "Se atribuye la idea y no se agrega nada."),
    ],
    Z=[
        ex("Pedro dice: «En Roca Alta se junta cada mes porque es una tradición muy antigua». ¿Qué agrega que el texto no dice?", "Que es una tradición muy antigua", "El texto solo dice que se reúnen cada mes."),
        ex("Ana dice: «Doña Elena reparte verduras, por lo tanto todas las comunidades lo hacen». ¿Qué error comete?", "Generaliza a todas las comunidades", "El texto habla de una persona."),
    ],
    D=[
        ex("¿Qué actividad hace Mateo según el texto de doña Elena: regar con un balde o repartir verduras?", "Regar con un balde", "El texto dice que Mateo riega con un balde."),
        ex("Elige la frase que analiza sin inventar: A) «Repartir verduras muestra que se comparte con los vecinos» B) «Repartir verduras es un rito religioso»", "A", "La B inventa un significado."),
    ],
    context=[ex("En una exposición, una niña dice: «En mi comunidad se come papa porque es sagrada». No tiene a quién preguntar. ¿Qué es mejor? A) decir solo lo que sabe y consultar a alguien de la comunidad B) afirmar que es sagrada", "A", "Lo sagrado lo define la comunidad.")],
    selfcheck=[
        ex("Nombra las cuatro columnas de la tabla de elementos significativos.", "Lugares, oficios, alimentos y cooperación", "Son las cuatro categorías de la clase."),
        ex(CALETA + " ¿Cuál es el oficio que aparece?", "La pesca", "Los pescadores salen al mar."),
        ex("Verdadero o falso: valorar es reconocer la importancia de algo con respeto.", "Verdadero", "Esa es su definición."),
    ],
    task=T("Lee «La huerta de doña Elena»: «" + HUERTA.split("«", 1)[1].rstrip("»") + "» Haz una tabla con cuatro columnas: lugares, oficios, alimentos y cooperación, con al menos un dato en cada una. Escribe después dos frases: una con «El texto muestra que…» y otra con «Me gustaría preguntar a la comunidad…».",
           "Lugares: junto al camino, la huerta. Oficios: sembrar, regar. Alimentos: papas, habas, zapallos. Cooperación: repartir verduras a los vecinos. El texto muestra que doña Elena comparte lo que cosecha. Me gustaría preguntar a la comunidad por qué se deja descansar la tierra.",
           ["completa las cuatro columnas con datos del texto", "analiza sin inventar", "formula una pregunta respetuosa"], ["tabla de cuatro columnas", "dos frases"], ["inventar creencias", "poner datos que no están"],
           "Pedir que indique la frase del texto de cada dato; valorar que no explique creencias."),
    reinforce="Haz la misma tabla de cuatro columnas con el texto «Mi caleta».",
    extend="Escribe dos elementos significativos de tu comunidad que quisieras que un texto contara, y a quién consultarías.",
)

L(
    LF3, 4,
    materials=MAT,
    use="Aprenderé a construir una respuesta atribuida sobre un texto de la cultura: decir lo que el texto muestra, con una frase que lo apoye y la fuente. Sirve para analizar con respeto y sin adivinar.",
    prior=["Sé reconocer elementos significativos en un texto.", "Sé usar «según» para atribuir una idea."],
    explain=[
        "Una respuesta atribuida sobre un texto tiene cuatro partes. Primero la fuente: «Según la carta de Camila…». Luego la idea: lo que el texto muestra. Después la evidencia: una frase breve del texto que la apoya. Por último, si queremos, nuestra opinión, separada con «Yo pienso…». Así quien lee sabe qué viene del texto y qué viene de nosotros.",
        "Para elegir la evidencia, buscamos la frase que prueba lo que decimos. Si afirmamos que en la caleta se coopera, la evidencia es «las personas ayudan a descargar». Una evidencia no es una opinión: se puede encontrar en el texto con el dedo. Si no hay evidencia, no hacemos la afirmación.",
        "Una respuesta bien atribuida también dice lo que no sabemos: «El texto no explica por qué…». Y no usa palabras como «todos», «siempre» o «los pueblos», porque un texto cuenta lo de una persona o comunidad. Con estas reglas nuestras respuestas son más claras y más respetuosas.",
    ],
    vocab=[("evidencia", "frase del texto que prueba lo que afirmo"), ("atribuir", "decir de quién viene una idea"), ("afirmación", "lo que digo que es verdad"), ("opinión", "lo que yo pienso, separado de lo que dice el texto"), ("generalizar", "decir que algo vale para todos")],
    worked=[
        W("Armar la respuesta", CALETA + " Pregunta: ¿cómo cooperan las personas de la caleta?", ["Fuente: el texto «Mi caleta».", "Idea: se ayudan.", "Evidencia: «ayudan a descargar»."], "Según el texto «Mi caleta», las personas cooperan: «ayudan a descargar»."),
        W("Encontrar el error", "Respuesta: «Según el texto, todas las caletas se reúnen cada mes». ¿Qué error tiene?", ["Dice «todas las caletas».", "El texto solo habla de Roca Alta."], "Generaliza a todas las caletas."),
    ],
    mistakes=[
        M("Afirmar algo sin evidencia del texto.", "No se puede comprobar.", "Busco una frase que lo apoye o no lo afirmo."),
        M("Usar «todos» o «siempre».", "El texto cuenta un caso.", "Escribo el nombre del lugar o de la persona."),
    ],
    R=[
        ex("Completa: «Según la carta de ___, la vertiente se limpia entre todos».", "Camila", "Camila es la autora de la carta."),
        ex("La evidencia de una respuesta es: A) una frase del texto que la apoya B) mi opinión", "A", "La evidencia se encuentra en el texto."),
        ex(HUERTA + " ¿Qué evidencia muestra que doña Elena comparte: «reparte verduras a los vecinos» o «vive junto al camino»?", "Reparte verduras a los vecinos", "Esa frase prueba que comparte."),
    ],
    C=[
        ex("¿Cuál empieza con una fuente? A) «Según el texto “Mi caleta”, hay una sede» B) «Hay una sede»", "A", "La A nombra el texto."),
        ex("Verdadero o falso: puedo usar «todos» para hablar de un caso que cuenta un texto.", "Falso", "El texto cuenta solo ese caso."),
        ex("¿Cómo separo mi opinión de lo que dice el texto? A) con «Yo pienso…» B) sin avisar", "A", "Así se distingue."),
    ],
    A=[
        ex("Ordena para formar una respuesta: a) «ayudan a descargar» b) Según el texto «Mi caleta» c) las personas cooperan. Escribe las letras.", "b, c, a", "Fuente, idea y evidencia."),
        ex(HUERTA + " Elige la evidencia que apoya «Mateo ayuda en la huerta»: A) «Mateo riega con un balde» B) «doña Elena siembra papas»", "A", "La A muestra a Mateo ayudando."),
        ex(CARTA + " Completa: «Según la carta, la vecina explicó que la vertiente se limpia ___».", "entre todos cada primavera", "Lo dice la carta."),
    ],
    Z=[
        ex("Rosa escribe: «Según el texto, doña Elena es la mejor agricultora». ¿Qué problema tiene?", "No hay evidencia y jerarquiza", "El texto no compara a doña Elena con nadie."),
        ex("Luis escribe: «El texto no explica por qué la tierra descansa». ¿Es una respuesta válida? Responde Sí o No.", "Sí", "Declara un límite del texto."),
    ],
    D=[
        ex("Dos respuestas a «¿qué muestra “Mi caleta”?». R1: «Según el texto, las personas ayudan a descargar y se reúnen en la sede». R2: «Según el texto, todas las caletas hacen asambleas». ¿Cuál tiene evidencia?", "R1", "La R2 generaliza sin evidencia."),
        ex("Si la ficha reserva un dato del texto, ¿lo usas como evidencia? A) no, lo respeto B) sí, es una evidencia más", "A", "El límite de la ficha se respeta."),
    ],
    context=[ex("En una prueba te piden explicar cómo se ayudan los vecinos según un texto. ¿Qué haces? A) escribo la fuente, la idea y una frase del texto B) escribo lo que sé de mi barrio", "A", "Se responde con el texto y no con otra cosa.")],
    selfcheck=[
        ex("Nombra las cuatro partes de la respuesta atribuida.", "Fuente, idea, evidencia y opinión", "Son las partes de la clase."),
        ex("Verdadero o falso: una evidencia puede ser una opinión mía.", "Falso", "La evidencia sale del texto."),
        ex("Verdadero o falso: puedo decir «el texto no explica…» cuando algo falta.", "Verdadero", "Es una forma de declarar el límite."),
    ],
    task=T("Responde por escrito: «¿Qué muestra el texto “La huerta de doña Elena” sobre cómo se cuida la tierra y a los vecinos?». Usa el texto: «" + HUERTA.split("«", 2)[2].rstrip("»") + "». Tu respuesta debe tener fuente, idea, una frase del texto como evidencia, una frase con «El texto no explica…» y otra con «Yo pienso…».",
           "Según el texto sobre doña Elena, ella cuida la tierra dejándola descansar: «cuando la tierra descansa, después da más». También cuida a los vecinos porque «reparte verduras a los vecinos». El texto no explica por qué los domingos. Yo pienso que es una forma de compartir.",
           ["incluye fuente, idea y evidencia", "declara un límite del texto", "separa la opinión"], ["respuesta de cuatro frases"], ["usar «todos»", "afirmar sin evidencia"],
           "Pedir que muestre con el dedo la evidencia en el texto; valorar el uso de «el texto no explica»."),
    reinforce="Escribe una evidencia del texto «Mi caleta» que apoye cada una de estas ideas: cooperan, se reúnen, trabajan en el mar.",
    extend="Escribe una respuesta atribuida sobre la carta de Camila siguiendo las cuatro partes.",
)

L(
    LF3, 5,
    materials=MAT,
    use="Aprenderé a comparar dos textos de la cultura sin decir que uno es mejor. Sirve para ver cómo cada texto muestra una manera distinta de vivir el territorio.",
    prior=["Sé responder de forma atribuida con evidencia.", "Sé que contrastar es distinto de jerarquizar."],
    explain=[
        "Contrastar dos textos es mirar en qué se parecen y en qué se diferencian. Usamos criterios neutros: el lugar, el oficio, los alimentos o productos, la cooperación y quién escribe. «Mi caleta» y «La huerta de doña Elena» hablan de lugares y oficios distintos, pero ambos muestran personas que comparten con otros.",
        "No jerarquizamos: no decimos que la caleta es más importante que la huerta ni que un texto es mejor que otro. Cada uno muestra un territorio y un trabajo. Tampoco decimos que representan a todos los pueblos: son dos textos de práctica. Para contrastar con respeto usamos frases como «en este texto…, en cambio en el otro…».",
        "Una tabla de comparación ayuda: dos columnas, una por texto, y filas con los criterios. Al final escribimos una semejanza y una diferencia, cada una con evidencia. Si un criterio no aparece en uno de los textos, anotamos «no se menciona». No se llena con lo que suponemos.",
    ],
    vocab=[("contrastar", "decir en qué se parecen y en qué se diferencian dos cosas"), ("semejanza", "algo en lo que dos cosas se parecen"), ("diferencia", "algo en lo que dos cosas no se parecen"), ("criterio", "regla para comparar"), ("no se menciona", "el texto no dice nada sobre eso")],
    worked=[
        W("Comparar con un criterio", CALETA + " " + HUERTA + " Criterio: el oficio.", ["Mi caleta: pesca.", "La huerta: cultivar y regar."], "En un texto el oficio es la pesca y en el otro el cultivo."),
        W("Encontrar una semejanza", "Criterio: cooperación. En la caleta ayudan a descargar; doña Elena reparte verduras.", ["En la caleta se ayuda a descargar.", "Doña Elena reparte verduras a los vecinos."], "Ambos textos muestran personas que ayudan o comparten con otras."),
    ],
    mistakes=[
        M("Decir que un texto es mejor que otro.", "Cada texto muestra un lugar y un trabajo.", "Comparo con criterios neutros."),
        M("Llenar la tabla con datos que no están en los textos.", "Inventa información.", "Escribo «no se menciona»."),
    ],
    R=[
        ex(CALETA + " ¿Qué oficio muestra «Mi caleta»: la pesca o el cultivo?", "La pesca", "Los pescadores salen al mar."),
        ex(HUERTA + " ¿Qué lugar describe: una huerta o una caleta?", "Una huerta", "Es el texto de doña Elena."),
        ex("Contrastar es: A) decir en qué se parecen y en qué se diferencian B) elegir el mejor", "A", "Contrastar no jerarquiza."),
    ],
    C=[
        ex("Verdadero o falso: «es mejor» es una forma de jerarquizar.", "Verdadero", "Pone un texto sobre otro."),
        ex("Si un criterio no aparece en un texto, ¿qué escribo? A) no se menciona B) lo que supongo", "A", "No se inventa."),
        ex("Verdadero o falso: dos textos distintos pueden tener una semejanza.", "Verdadero", "Por ejemplo, ambos muestran que se comparte."),
    ],
    A=[
        ex(CALETA + " " + HUERTA + " Criterio «lugar». ¿Cuál de los dos textos describe un lugar con playa?", "Mi caleta", "«La huerta de doña Elena» habla de un lugar junto al camino."),
        ex("Une cada criterio con el dato de «La huerta de doña Elena». 1) alimento 2) cooperación. a) repartir verduras b) papas", "1-b, 2-a", "Cada criterio tiene su dato."),
        ex(CALETA + " ¿Cuál de estos datos aparece solo en «Mi caleta»: la sede o el balde?", "La sede", "La sede se menciona solo en «Mi caleta»."),
    ],
    Z=[
        ex("Marta escribe: «La caleta es más importante porque es más grande». ¿Qué error comete?", "Jerarquiza con un criterio que el texto no usa", "Los textos no comparan importancia."),
        ex("Pedro dice: «Ambos textos muestran cómo viven todos los pueblos». ¿Qué falla? A) generaliza dos textos de práctica B) está bien", "A", "Dos textos no representan a todos."),
    ],
    D=[
        ex("Elige la comparación respetuosa: A) «En “Mi caleta” el oficio es la pesca; en “La huerta”, el cultivo» B) «La caleta es mejor trabajo»", "A", "La A describe y no juzga."),
        ex("Criterio «cooperación». ¿Cuál es una semejanza entre «Mi caleta» y «La huerta de doña Elena»? A) ambos muestran personas que ayudan o comparten con otras B) en ambos se pesca en el mar", "A", "En la caleta ayudan a descargar y doña Elena reparte verduras; solo el primero habla de pesca."),
    ],
    context=[ex("Dos grupos presentan textos de comunidades distintas y discuten cuál «cuenta mejor la cultura». ¿Qué propones? A) comparar qué muestra cada texto y de quién viene B) votar", "A", "Se contrasta sin jerarquizar.")],
    selfcheck=[
        ex("Nombra dos criterios neutros para comparar textos.", "Dos entre: lugar, oficio, alimentos, cooperación, quién escribe", "Son criterios de la clase."),
        ex("Verdadero o falso: puedo llenar con mi imaginación un criterio que el texto no menciona.", "Falso", "Se anota «no se menciona»."),
        ex("Verdadero o falso: la comparación termina con una semejanza y una diferencia con evidencia.", "Verdadero", "Es la estructura de la clase."),
    ],
    task=T("Compara «Mi caleta» y «La huerta de doña Elena». Textos: «" + CALETA.split("«", 2)[2].rstrip("»") + "» y «" + HUERTA.split("«", 2)[2].rstrip("»") + "». Haz una tabla de dos columnas con las filas: lugar, oficio, alimento o producto, cooperación. Escribe «no se menciona» donde corresponda. Cierra con una semejanza y una diferencia con evidencia, y una frase que explique por qué no se debe decir cuál es mejor.",
           "Lugar: caleta con playa y sede / huerta junto al camino. Oficio: pesca / cultivar. Alimento: no se menciona / papas, habas y zapallos. Cooperación: ayudan a descargar / reparte verduras. Semejanza: ambos muestran personas que ayudan. Diferencia: uno trabaja en el mar y el otro en la tierra. No se dice cuál es mejor porque cada texto muestra un territorio distinto.",
           ["usa criterios neutros", "marca lo que no se menciona", "no jerarquiza"], ["tabla de comparación", "semejanza y diferencia", "frase de cierre"], ["decir cuál es mejor", "completar datos inventados"],
           "Pedir que señale la evidencia de cada celda; valorar que use «no se menciona»."),
    reinforce="Completa una tabla con tres criterios para la carta de Camila y «Mi caleta».",
    extend="Explica por qué dos textos de distintas comunidades no se pueden usar para hablar de «todos los pueblos».",
)

# ============================================================ OA LF04 · escritura, aglutinación y reduplicación
TOLU = ("Reglas de la lengua de práctica Tolu (inventada; no es de ningún pueblo): pak = casa; nem = río; lun = pájaro; tor = camino. "
        "Piezas que se pegan a la raíz: ka- = mi (va al comienzo); -tu = pequeño (va después de la raíz); -ra = muchos (va después de la raíz); "
        "-vi = en (siempre va al final). Si se repite la raíz, significa «muy grande». Orden: ka- + raíz + -tu o -ra + -vi.")

L(
    LF4, 1,
    materials=MAT,
    use="Aprenderé a situar la escritura de una lengua indígena: quién define cómo se escribe, que a veces hay más de una escritura y que las palabras se escriben como las enseña la fuente. Sirve para escribir con respeto y sin inventar letras ni palabras.",
    prior=["Sé que cada pueblo tiene su lengua y que la enseña el educador tradicional.", "Sé usar fichas de palabras."],
    explain=[
        "Escribir una lengua indígena no es copiar cómo suena según el castellano. Cada lengua tiene sus sonidos y las comunidades y sus educadores han acordado formas de escribirlos. A veces existe más de una escritura. Por ejemplo, el nombre de la lengua mapuche se escribe «mapuzugun» y también «mapudungun»: ambas se usan.",
        "Por eso, antes de escribir una palabra en lengua indígena, situamos la fuente: de qué lengua es, quién la enseñó y con qué escritura. Si una palabra aparece en una ficha de palabras, la copiamos tal como está. Si no aparece, no la inventamos: se la pedimos al educador tradicional o a una persona de la comunidad.",
        "Para practicar cómo se arman las palabras sin inventar nada de un pueblo real, en estas clases usamos una lengua de práctica inventada llamada Tolu, con reglas que están escritas en cada ejercicio. Tolu no es de ningún pueblo y no sirve para escribir en la lengua de una comunidad: solo sirve para entender cómo funcionan las palabras pegadas y repetidas.",
    ],
    vocab=[("escritura", "forma acordada de escribir los sonidos de una lengua"), ("fuente", "persona o ficha que enseña cómo se escribe una palabra"), ("lengua de práctica", "lengua inventada para ejercitar, que no es de ningún pueblo"), ("raíz", "parte principal de una palabra"), ("pieza", "parte con significado que se pega a la raíz")],
    worked=[
        W("Una lengua con dos escrituras", "El nombre de la lengua mapuche se escribe «mapuzugun» y también «mapudungun». ¿Una de las dos está mal?", ["Ambas se usan.", "Dependen de la escritura que use cada comunidad o fuente."], "No, las dos se usan; se escribe como lo indica la fuente."),
        W("Copiar de una ficha", "Ficha de palabras: «ko» es agua. Quieres escribir la palabra agua en mapuzugun. ¿Qué haces?", ["Busco la palabra en la ficha.", "La copio tal como está."], "Escribo «ko» como aparece en la ficha."),
    ],
    mistakes=[
        M("Escribir una palabra indígena según cómo la oigo en castellano.", "Los sonidos de la lengua se escriben de otra forma.", "Copio la palabra de una fuente o se la pido al educador."),
        M("Pensar que Tolu sirve para escribir en lengua indígena.", "Tolu es inventada solo para practicar.", "Uso Tolu para entender y la lengua real con el educador."),
    ],
    R=[
        ex("¿Cómo se escribe el nombre de la lengua mapuche en una de sus dos escrituras: «mapuzugun» o «zumapugun»?", "Mapuzugun", "Es una de las escrituras en uso."),
        ex("La lengua de práctica Tolu es: A) inventada, no es de ningún pueblo B) la lengua de un pueblo real", "A", "Se creó solo para ejercitar."),
        ex("Si una palabra está en la ficha, ¿la copio tal cual o la cambio?", "La copio tal cual", "La ficha es la fuente."),
    ],
    C=[
        ex("Verdadero o falso: «mapuzugun» y «mapudungun» son dos escrituras que se usan.", "Verdadero", "Ambas se usan."),
        ex("¿Quién enseña cómo se escribe una palabra en la lengua de mi comunidad? A) el educador tradicional B) mi imaginación", "A", "Es la fuente adecuada."),
        ex("Verdadero o falso: puedo escribir una palabra indígena como suena en castellano.", "Falso", "Los sonidos se escriben según la escritura acordada."),
    ],
    A=[
        ex(TOLU + " ¿Qué significa «pak» en Tolu?", "Casa", "Lo dice la regla."),
        ex(TOLU + " ¿Qué pieza va siempre al final de la palabra: «-vi» o «ka-»?", "-vi", "La regla dice que -vi siempre va al final."),
        ex("Une cada cosa con su fuente. 1) «ko» es agua 2) «pak» es casa en Tolu. a) ficha de palabras b) reglas de Tolu inventadas", "1-a, 2-b", "Cada dato viene de una fuente distinta."),
    ],
    Z=[
        ex("Camila usa la regla de Tolu para escribir «casa» en la lengua de su comunidad. ¿Qué error comete?", "Usa una lengua inventada para escribir una lengua real", "Tolu no pertenece a ningún pueblo."),
        ex("Dos compañeros escriben «mapuzugun» y «mapudungun». Uno dice que el otro se equivocó. ¿Qué respondes? A) las dos se usan B) solo una es correcta", "A", "Hay más de una escritura en uso."),
    ],
    D=[
        ex("No encuentras una palabra en ninguna ficha. ¿Qué haces? A) la pido al educador tradicional B) la invento con letras parecidas", "A", "No se inventan palabras de una lengua real."),
        ex("Si una persona de la comunidad te escribe una palabra y la ficha de tu cuaderno la escribe distinto, ¿qué haces? A) pregunto cuál escritura usa su comunidad B) cambio la de la persona", "A", "Puede haber más de una escritura."),
    ],
    context=[ex("Quieres escribir un cartel con una palabra de la lengua de tu comunidad. ¿Qué haces primero? A) pedirle al educador tradicional cómo se escribe B) buscar una palabra parecida y copiarla", "A", "La fuente adecuada es quien la enseña.")],
    selfcheck=[
        ex("Explica con tus palabras por qué Tolu no sirve para escribir en lengua indígena.", "Porque es inventada y no es de ningún pueblo", "Solo sirve para practicar."),
        ex("Verdadero o falso: una lengua puede tener más de una escritura en uso.", "Verdadero", "El ejemplo es mapuzugun y mapudungun."),
        ex(TOLU + " ¿Qué significa «nem»?", "Río", "Lo dice la regla."),
    ],
    task=T("Escribe una ficha de fuente con tres filas: «Palabra o regla», «De qué fuente viene» y «Qué debo preguntar». Usa tres ejemplos: «ko» (ficha de palabras), «pak» (reglas de Tolu inventadas) y una palabra de la lengua de tu comunidad que quieras aprender (escribe solo que quieres aprender cómo se dice «río»). Termina con una frase que explique por qué no se debe inventar la escritura de una palabra indígena.",
           "ko: ficha de palabras; preguntar si es la escritura de mi comunidad. pak: reglas de Tolu inventadas; no usar en lengua real. «río» en mi lengua: educador tradicional; preguntar cómo se dice y cómo se escribe. No se debe inventar la escritura porque cada lengua tiene sus propios sonidos y formas acordadas.",
           ["distingue la fuente de cada dato", "no inventa palabras", "justifica el respeto a la escritura"], ["ficha de tres filas", "frase final"], ["inventar una palabra indígena", "usar Tolu como lengua real"],
           "Pedir que explique la fuente de cada fila; valorar que no complete lo que no sabe."),
    reinforce="Copia las reglas de Tolu en tu hoja y subraya con un color las piezas que se pegan a la raíz.",
    extend="Escribe una pregunta para el educador tradicional sobre cómo se escriben los sonidos de la lengua de tu comunidad.",
)

L(
    LF4, 2,
    materials=MAT,
    use="Aprenderé a leer palabras formadas por aglutinación: separar la raíz y las piezas y decir qué significa cada una. Sirve para entender cómo se arman palabras largas pegando partes con significado.",
    prior=["Sé que una raíz es la parte principal de una palabra.", "Sé que Tolu es una lengua inventada de práctica."],
    explain=[
        "Aglutinar significa pegar. En algunas lenguas, una palabra se forma pegando una raíz con varias piezas, y cada pieza tiene un significado propio que casi no cambia. En castellano también pegamos piezas: «sacapuntas» es «saca» + «puntas», y «paraguas» es «para» + «aguas». Cada parte tiene su sentido y la palabra completa lo junta.",
        "Para leer una palabra aglutinada, la separamos con guiones: raíz y piezas. Luego decimos qué significa cada una y, por último, la palabra completa. Con las reglas de Tolu: ka-pak-tu se separa en ka (mi), pak (casa) y tu (pequeño), y significa «mi casita». El orden de las piezas importa: no se pueden cambiar de lugar.",
        "Lo que hacemos aquí es practicar la idea con una lengua inventada. En las lenguas reales, las piezas y el orden dependen de cada lengua y las enseña el educador tradicional. Una lengua que pega piezas no es más simple ni más difícil que otra: es una forma distinta de armar palabras.",
    ],
    vocab=[("aglutinación", "forma de armar palabras pegando una raíz con piezas que tienen significado"), ("raíz", "parte principal de la palabra"), ("pieza", "parte con significado que se pega a la raíz"), ("segmentar", "separar una palabra en sus partes"), ("palabra compuesta", "palabra formada por dos palabras unidas, como «paraguas»")],
    worked=[
        W("Segmentar una palabra", TOLU + " Separa y traduce: ka-pak-tu.", ["ka = mi; pak = casa; tu = pequeño.", "Se juntan en ese orden."], "Mi casita."),
        W("Armar una palabra", TOLU + " Escribe «en el camino» en Tolu.", ["Camino es tor.", "«En» es -vi y va al final."], "tor-vi"),
    ],
    mistakes=[
        M("Cambiar el orden de las piezas.", "En Tolu cada pieza tiene su lugar fijo.", "Reviso la regla del orden."),
        M("Pensar que una palabra larga es una oración.", "Es una sola palabra con varias piezas.", "Separo las piezas y las traduzco."),
    ],
    R=[
        ex(TOLU + " ¿Qué significa «lun»?", "Pájaro", "Lo dice la regla."),
        ex(TOLU + " ¿Qué significa la pieza «-ra»?", "Muchos", "Lo dice la regla."),
        ex("En castellano, «sacapuntas» se forma con «saca» y: A) puntas B) sacos", "A", "La palabra une dos partes."),
    ],
    C=[
        ex("Aglutinar significa: A) pegar piezas con significado B) borrar piezas", "A", "Aglutinar es pegar."),
        ex(TOLU + " ¿Qué significa «ka-nem»?", "Mi río", "ka = mi y nem = río."),
        ex("Verdadero o falso: en «paraguas», las dos partes conservan su sentido.", "Verdadero", "Para + aguas."),
    ],
    A=[
        ex(TOLU + " Separa y traduce: pak-ra.", "pak + ra: casas", "pak es casa y -ra es muchos."),
        ex(TOLU + " Escribe «mi río pequeño» en Tolu.", "ka-nem-tu", "Se pega ka-, la raíz y -tu en ese orden."),
        ex(TOLU + " Escribe «en el río» en Tolu.", "nem-vi", "-vi va al final."),
    ],
    Z=[
        ex(TOLU + " Marta escribió «tu-ka-pak» para «mi casita». ¿Qué error tiene?", "Cambió el orden de las piezas", "ka- va al comienzo y -tu después de la raíz."),
        ex(TOLU + " Tomás dice que «lun-tu» significa «un pájaro grande». ¿Es correcto? Responde Sí o No.", "No", "La pieza -tu significa pequeño, así que es un pájaro pequeño."),
    ],
    D=[
        ex(TOLU + " Traduce: ka-lun-ra-vi.", "En mis pájaros", "ka = mi; lun = pájaro; ra = muchos; vi = en."),
        ex(TOLU + " Escribe «en mis casas» en Tolu respetando el orden.", "ka-pak-ra-vi", "ka- primero, luego la raíz, -ra y al final -vi."),
    ],
    context=[ex("Un amigo te muestra una palabra larga en una lengua real y te dice que es una oración. ¿Qué propones? A) pedir al educador tradicional que muestre sus partes B) adivinar qué parte significa qué", "A", "Solo quien conoce la lengua puede separar sus piezas.")],
    selfcheck=[
        ex("Nombra la regla de Tolu sobre el orden de las piezas.", "ka- al comienzo, la raíz, -tu o -ra y -vi al final", "Es el orden fijo de las piezas."),
        ex(TOLU + " ¿Qué significa «ka-lun»?", "Mi pájaro", "ka = mi y lun = pájaro."),
        ex("Verdadero o falso: una lengua que pega piezas es más simple que otra.", "Falso", "Es una forma distinta de armar palabras."),
    ],
    task=T("Con las reglas de Tolu: «" + TOLU + "» Segmenta y traduce estas cuatro palabras: ka-tor, nem-ra, ka-pak-tu-vi y lun-vi. Luego arma en Tolu estas dos: «mis ríos» y «en mi camino». Escribe después una frase que explique qué es aglutinar con un ejemplo en castellano.",
           "ka-tor: mi camino. nem-ra: ríos. ka-pak-tu-vi: en mi casita. lun-vi: en el pájaro. «mis ríos»: ka-nem-ra. «en mi camino»: ka-tor-vi. Aglutinar es pegar piezas con significado, como en «paraguas»: para + aguas.",
           ["segmenta cada palabra", "respeta el orden de las piezas", "explica aglutinar con ejemplo"], ["cuatro segmentaciones", "dos palabras armadas", "definición con ejemplo"], ["cambiar el orden de las piezas", "usar Tolu como lengua real"],
           "Pedir que señale cada pieza y su significado en las reglas; valorar la definición propia."),
    reinforce="Segmenta en tu hoja «lavaplatos» y «cortaúñas» en las dos palabras que las forman.",
    extend="Arma tres palabras nuevas de Tolu con piezas distintas y tradúcelas.",
)

L(
    LF4, 3,
    materials=MAT,
    use="Aprenderé a reconocer cómo la forma de armar palabras se relaciona con la cultura, usando el ejemplo muy conocido de «mapuche» y «mapuzugun». Sirve para ver que las palabras guardan una mirada del mundo sin inventar significados.",
    prior=["Sé segmentar una palabra aglutinada.", "Sé que Tolu es inventada y que las lenguas reales las enseña el educador."],
    explain=[
        "Las palabras no solo sirven para nombrar: también guardan una manera de mirar el mundo. Un ejemplo muy conocido es la palabra «mapuche». Se suele explicar como «mapu», que es tierra, y «che», que es gente: «gente de la tierra». Y «mapuzugun» se suele explicar como «mapu» (tierra) y «zugun» (habla): «habla de la tierra».",
        "Esta forma de armar palabras muestra una relación entre las personas, la tierra y la lengua. Pero tenemos que ser cuidadosos: así lo explican muchas fuentes, y lo correcto es confirmarlo con el educador tradicional o una persona de la comunidad. Una explicación de palabras no reemplaza a quien habla la lengua, y no debemos sacar conclusiones sobre otros pueblos.",
        "Con Tolu también podemos ver la idea: «ka-pak-tu» (mi casita) junta quién tiene (ka), qué es (pak) y cómo es (tu). Una palabra puede decir en una sola unidad lo que en castellano decimos con varias palabras. Esa diferencia en la forma no hace mejor ni peor a una lengua; cada una es una manera de decir el mundo.",
    ],
    vocab=[("mapu", "tierra, en mapuzugun"), ("che", "gente, en mapuzugun"), ("zugun", "habla, en mapuzugun"), ("relación", "vínculo entre dos cosas"), ("confirmar", "comprobar con la fuente adecuada")],
    worked=[
        W("Separar una palabra conocida", "Separa la palabra «mapuche» y di qué significa cada parte.", ["Se separa en mapu y che.", "Mapu es tierra y che es gente."], "Mapu (tierra) + che (gente): gente de la tierra, según se explica comúnmente."),
        W("Cuidar la conclusión", "Un compañero dice: «Como mapuche se arma así, todos los pueblos arman sus nombres con la tierra». ¿Qué error comete?", ["Está generalizando un solo caso.", "No sabe cómo arman sus nombres otros pueblos."], "Generaliza; cada lengua forma sus palabras a su manera."),
    ],
    mistakes=[
        M("Afirmar que una explicación de palabras es definitiva sin consultar.", "Una explicación general no reemplaza a quien habla la lengua.", "La confirmo con el educador tradicional."),
        M("Generalizar la forma de una lengua a todas.", "Cada lengua tiene sus propias formas.", "Hablo solo de esa lengua."),
    ],
    R=[
        ex("Se suele explicar que «mapu» significa: A) tierra B) agua", "A", "Mapu es tierra."),
        ex("Se suele explicar que «che» significa: A) gente B) casa", "A", "Che es gente."),
        ex(TOLU + " En «ka-pak-tu», ¿qué significa «tu»?", "Pequeño", "Lo dice la regla de Tolu."),
    ],
    C=[
        ex("Verdadero o falso: «mapuche» se suele explicar como «mapu» + «che».", "Verdadero", "Esa es la explicación común."),
        ex("¿Qué hago con una explicación de palabras que encuentro en un libro? A) la confirmo con el educador tradicional B) la repito como si fuera segura", "A", "Debe validarla quien conoce la lengua."),
        ex("Verdadero o falso: una lengua que junta mucho en una palabra es mejor que una que usa varias palabras.", "Falso", "Son maneras distintas, no mejores ni peores."),
    ],
    A=[
        ex("Se suele explicar «mapuzugun» como «mapu» + «zugun». Si «zugun» es habla, ¿qué significa la palabra completa?", "Habla de la tierra", "Mapu es tierra y zugun es habla."),
        ex(TOLU + " Escribe en Tolu «mi casita» y separa sus piezas.", "ka-pak-tu: ka + pak + tu", "Mi, casa y pequeño."),
        ex("Une cada palabra con su explicación común. 1) mapuche 2) mapuzugun. a) gente de la tierra b) habla de la tierra", "1-a, 2-b", "Se usan mapu + che y mapu + zugun."),
    ],
    Z=[
        ex("Rafael dice: «Como en mapuche aparece “tierra”, todos los pueblos de Chile se llaman por la tierra». ¿Qué error comete?", "Generaliza un caso a todos los pueblos", "Cada pueblo tiene sus propios nombres."),
        ex("Una niña explica «mapuche» y agrega una historia de cómo los antepasados eligieron el nombre. El libro no lo cuenta. ¿Qué error comete?", "Inventa una historia que la fuente no dice", "Debe limitarse a lo explicado y consultar."),
    ],
    D=[
        ex("¿Qué frase cuida mejor la información? A) «Se suele explicar que mapuche viene de mapu y che; lo confirmaré con el educador tradicional» B) «Mapuche significa exactamente eso y no se discute»", "A", "La A reconoce que hay que confirmar."),
        ex(TOLU + " Escribe en Tolu «mi pájaro pequeño» y explica qué dice cada pieza.", "ka-lun-tu: mi + pájaro + pequeño", "Se respeta el orden de las piezas."),
    ],
    context=[ex("En clases, un compañero dice que sabe lo que significa cada parte de una palabra de otro pueblo porque «suena parecido». ¿Qué le propones? A) preguntar al educador tradicional de ese pueblo B) usar la que le parezca", "A", "El significado lo da quien conoce la lengua.")],
    selfcheck=[
        ex("Explica con tus palabras qué muestra la palabra «mapuche».", "Que une tierra y gente", "Según la explicación común."),
        ex("Verdadero o falso: una explicación de un libro basta para afirmar el significado de una palabra.", "Falso", "Hay que confirmar con la comunidad."),
        ex(TOLU + " ¿Qué significa «ka-nem»?", "Mi río", "ka = mi y nem = río."),
    ],
    task=T("Haz una ficha de dos palabras: «mapuche» (mapu + che) y «ka-pak-tu» (de Tolu, inventada). Para cada una escribe: sus partes, qué significa cada parte, de qué fuente viene y qué debes confirmar con el educador tradicional. Escribe después una frase que explique por qué la forma de las palabras puede mostrar una relación con el mundo, sin generalizar a otros pueblos.",
           "mapuche: mapu (tierra) + che (gente); fuente: explicación común; confirmar con el educador tradicional. ka-pak-tu: ka (mi) + pak (casa) + tu (pequeño); fuente: reglas de Tolu inventada; no se confirma porque no es real. Las palabras pueden mostrar una relación con el mundo, pero solo hablo de esta lengua.",
           ["separa las partes", "indica la fuente", "evita generalizar"], ["ficha de dos palabras", "frase final"], ["inventar significados", "generalizar a otros pueblos"],
           "Pedir que diga qué parte viene de una fuente y qué parte es de práctica; valorar que anote qué confirmará."),
    reinforce="Escribe en una tarjeta las dos explicaciones comunes y la frase «lo confirmaré con el educador tradicional».",
    extend="Pregunta al educador tradicional cómo se explica una palabra de la lengua de tu comunidad y anota su respuesta.",
)

L(
    LF4, 4,
    materials=MAT,
    use="Aprenderé a escribir oraciones y textos breves aplicando la aglutinación y la reduplicación, usando Tolu para practicar. Sirve para entender cómo se construye un texto con palabras pegadas y repetidas.",
    prior=["Sé segmentar y armar palabras con piezas.", "Sé que Tolu es una lengua inventada de práctica."],
    explain=[
        "La reduplicación es repetir una palabra o una parte de ella para cambiar su significado. En castellano lo hacemos a veces: decimos «grande grande» para decir «muy grande», o «chico chico» para decir «muy chico». En Tolu, repetir la raíz significa «muy grande»: nem-nem es «río muy grande» y pak-pak es «casa muy grande».",
        "Para escribir un texto breve en Tolu usamos etiquetas, que son frases cortas que nombran lo que vemos en un dibujo. Cada etiqueta puede tener aglutinación (ka-pak-tu) y reduplicación (tor-tor). Después escribimos al lado la traducción en castellano. Las etiquetas muestran que entendemos las reglas, pero no son un texto real de ningún pueblo.",
        "Al escribir en una lengua real, usamos solo las palabras y formas que enseña el educador tradicional. Podemos aplicar la misma idea: pedir una raíz, las piezas que se le pegan y el modo de repetir, y escribir lo aprendido con su ayuda. Siempre indicamos quién nos enseñó cada palabra.",
    ],
    vocab=[("reduplicación", "repetir una palabra o parte de ella para cambiar su significado"), ("etiqueta", "frase corta que nombra lo que se ve en un dibujo"), ("raíz repetida", "palabra que se dice dos veces para cambiar su significado"), ("traducción", "lo que dice un texto en otra lengua"), ("texto breve", "texto de pocas frases")],
    worked=[
        W("Reduplicar", TOLU + " Escribe «camino muy grande».", ["Camino es tor.", "Se repite la raíz."], "tor-tor"),
        W("Aglutinar y reduplicar", TOLU + " Escribe «en el río muy grande».", ["Río muy grande: nem-nem.", "«En» es -vi y va al final."], "nem-nem-vi"),
    ],
    mistakes=[
        M("Repetir la pieza en vez de la raíz.", "En Tolu se repite la raíz completa.", "Repito la raíz y pego después las piezas."),
        M("Poner -vi en el medio de la palabra.", "-vi siempre va al final.", "Reviso el orden."),
    ],
    R=[
        ex(TOLU + " ¿Cómo se escribe «casa muy grande» en Tolu?", "pak-pak", "Se repite la raíz."),
        ex(TOLU + " ¿Qué significa «nem-nem»?", "Río muy grande", "Raíz repetida significa muy grande."),
        ex("En castellano, «grande grande» quiere decir: A) muy grande B) pequeño", "A", "La repetición aumenta el sentido."),
    ],
    C=[
        ex("La reduplicación es: A) repetir una palabra o parte de ella B) cortar una palabra", "A", "Repetir cambia el significado."),
        ex(TOLU + " Verdadero o falso: «tor-tor» significa «muchos caminos».", "Falso", "Significa camino muy grande."),
        ex("Una etiqueta es: A) una frase corta que nombra lo que se ve B) un cuento largo", "A", "Las etiquetas nombran."),
    ],
    A=[
        ex(TOLU + " Escribe «mi casita» en Tolu.", "ka-pak-tu", "ka + pak + tu."),
        ex(TOLU + " Escribe «pájaros» en Tolu.", "lun-ra", "La raíz y -ra."),
        ex(TOLU + " Escribe «en el camino muy grande» en Tolu.", "tor-tor-vi", "Raíz repetida y -vi al final."),
    ],
    Z=[
        ex(TOLU + " Ana escribió «pak-ra-ra» para «muchísimas casas». ¿Qué error tiene?", "Repitió una pieza; la regla repite la raíz", "La reduplicación en Tolu repite la raíz."),
        ex(TOLU + " Luis escribe «nem-vi-tu» para «en el río pequeño». ¿Está bien? Responde Sí o No.", "No", "-vi debe ir al final: nem-tu-vi."),
    ],
    D=[
        ex(TOLU + " Escribe dos etiquetas en Tolu para un dibujo con un río muy grande y un pájaro pequeño, y tradúcelas.", "nem-nem y lun-tu: río muy grande y pájaro pequeño", "Se aplican la reduplicación y la pieza -tu."),
        ex(TOLU + " ¿Qué palabra diría «en mi casita»?", "ka-pak-tu-vi", "ka-, la raíz, -tu y al final -vi."),
    ],
    context=[ex("Quieres escribir un cartel en la lengua de tu comunidad con una palabra repetida. ¿Qué haces primero? A) pregunto al educador tradicional si se repite así y cómo se escribe B) repito la palabra porque se ve bien", "A", "Solo la fuente dice cómo se repite en esa lengua.")],
    selfcheck=[
        ex("Explica con tus palabras qué es la reduplicación.", "Repetir una palabra o parte de ella para cambiar su significado", "Es la definición de la clase."),
        ex(TOLU + " ¿Cómo se escribe «en mi río» en Tolu?", "ka-nem-vi", "ka + nem + vi."),
        ex("Verdadero o falso: puedo usar Tolu como si fuera un texto real de un pueblo.", "Falso", "Tolu es una lengua inventada."),
    ],
    task=T("Con las reglas de Tolu: «" + TOLU + "» escribe cuatro etiquetas para un dibujo que muestre un camino muy grande, mis pájaros, una casita mía y un río. Debes usar al menos una vez la reduplicación y dos veces la aglutinación. Escribe la traducción al lado. Termina con una pregunta que le harías al educador tradicional sobre cómo repetir o pegar palabras en la lengua de tu comunidad.",
           "tor-tor: camino muy grande. ka-lun-ra: mis pájaros. ka-pak-tu: mi casita. nem: río. Pregunta: ¿hay palabras que se repitan en nuestra lengua y qué significan?",
           ["usa reduplicación y aglutinación", "respeta las reglas", "traduce cada etiqueta"], ["cuatro etiquetas con traducción", "pregunta escrita"], ["mezclar el orden de las piezas", "usar Tolu como lengua real"],
           "Pedir que explique cada pieza con la regla; valorar la pregunta final."),
    reinforce="Escribe en Tolu tres palabras con reduplicación y tradúcelas.",
    extend="Haz un dibujo de un lugar y rotúlalo con cinco etiquetas en Tolu usando las reglas.",
)

L(
    LF4, 5,
    materials=MAT,
    use="Aprenderé a contrastar la aglutinación y la reduplicación entre sí y con el castellano, sin decir que una forma es mejor. Sirve para entender que cada lengua arma sus palabras de manera propia.",
    prior=["Sé armar palabras con piezas y con raíz repetida en Tolu.", "Sé que no se jerarquizan las lenguas."],
    explain=[
        "La aglutinación pega piezas distintas a una raíz: ka-pak-tu. La reduplicación repite la raíz: pak-pak. Las dos son formas de armar palabras, y una lengua puede usar una, otra o ambas. En castellano también hay las dos: «paraguas» pega partes y «grande grande» repite. Pero cada lengua tiene sus propias reglas.",
        "Contrastar es decir en qué se parecen y en qué se diferencian, con criterios neutros: qué cambia (el significado), cómo se arma (pegando o repitiendo) y cuántas piezas usa. No decimos que una forma sea más moderna, más avanzada o más fácil: eso es jerarquizar. Una lengua con palabras largas no es más difícil, ni una con palabras cortas es más simple.",
        "Cuando escribimos sobre lenguas indígenas reales, atribuimos la información a nuestra fuente y no generalizamos a todas las lenguas. Si queremos comparar la lengua de nuestra comunidad con el castellano, pedimos ejemplos al educador tradicional. Así la comparación se apoya en palabras reales y no en suposiciones.",
    ],
    vocab=[("contrastar", "decir en qué se parecen y en qué se diferencian dos cosas"), ("jerarquizar", "decir que algo es mejor o más avanzado que otra cosa"), ("criterio", "regla para comparar"), ("aglutinación", "armar una palabra pegando piezas"), ("reduplicación", "armar o cambiar una palabra repitiéndola")],
    worked=[
        W("Comparar con criterios", TOLU + " Compara ka-pak-tu y pak-pak con el criterio «cómo se arma».", ["ka-pak-tu pega piezas.", "pak-pak repite la raíz."], "Uno aglutina y el otro reduplica."),
        W("Evitar jerarquizar", "Una niña dice: «Las lenguas que pegan piezas son más avanzadas». ¿Qué corrige?", ["«Más avanzadas» jerarquiza.", "Puede decir cómo arman sus palabras."], "«Algunas lenguas arman palabras pegando piezas; otras lo hacen de otra forma»."),
    ],
    mistakes=[
        M("Decir que una forma de armar palabras es más avanzada.", "Jerarquiza lenguas.", "Describo cómo se arma cada una."),
        M("Comparar sin ejemplos.", "No se puede comprobar.", "Uso palabras concretas."),
    ],
    R=[
        ex(TOLU + " ¿Cuál palabra pega piezas: «ka-pak-tu» o «pak-pak»?", "ka-pak-tu", "Tiene varias piezas pegadas."),
        ex(TOLU + " ¿Cuál palabra repite la raíz: «tor-tor» o «ka-tor»?", "tor-tor", "Esa palabra repite la raíz tor."),
        ex("Contrastar significa: A) ver semejanzas y diferencias B) elegir la mejor", "A", "Contrastar no jerarquiza."),
    ],
    C=[
        ex("Verdadero o falso: «paraguas» pega partes y «grande grande» repite.", "Verdadero", "Son ejemplos del castellano."),
        ex("Verdadero o falso: una lengua con palabras largas es más difícil.", "Falso", "Es una forma distinta de armar palabras."),
        ex("¿Cuál es un criterio neutro? A) cómo se arma la palabra B) cuál es más bonita", "A", "Se puede comprobar en la palabra."),
    ],
    A=[
        ex(TOLU + " Compara «ka-nem» y «nem-nem». ¿Qué cambia en cada una? A) ka-nem agrega quién tiene y nem-nem cambia el tamaño B) ka-nem cambia el tamaño y nem-nem agrega quién tiene", "A", "Una pieza cambia quién tiene y la repetición cambia el tamaño."),
        ex(TOLU + " Une cada palabra con su forma. 1) tor-tor 2) ka-tor-vi. a) aglutinación b) reduplicación", "1-b, 2-a", "Una repite la raíz y la otra pega piezas."),
        ex("¿Cuál es una semejanza entre aglutinar y reduplicar? A) las dos arman o cambian palabras B) las dos pegan piezas distintas a la raíz", "A", "La B solo describe la aglutinación."),
    ],
    Z=[
        ex("Pablo dice: «La reduplicación es una forma infantil de hablar». ¿Qué error comete?", "Jerarquiza y descalifica", "Muchas lenguas la usan de manera regular."),
        ex("Una compañera dice: «Todas las lenguas indígenas pegan piezas como Tolu». ¿Qué falla? A) generaliza B) tiene razón", "A", "Cada lengua tiene sus propias formas."),
    ],
    D=[
        ex("Elige la frase que contrasta sin jerarquizar: A) «En Tolu se pegan piezas y se repite la raíz para armar palabras» B) «Tolu es más simple que el castellano»", "A", "La A describe."),
        ex("Si quieres comparar la lengua de tu comunidad con el castellano, ¿qué haces? A) pido ejemplos al educador tradicional B) supongo cómo es", "A", "Se necesita una fuente real."),
    ],
    context=[ex("Un compañero dice que cierta lengua indígena es «más difícil» porque tiene palabras largas. ¿Qué le propones? A) mirar cómo se arman esas palabras con ayuda del educador tradicional B) estar de acuerdo", "A", "Comprender la forma evita los juicios.")],
    selfcheck=[
        ex("Nombra una diferencia entre aglutinación y reduplicación.", "Una pega piezas distintas y la otra repite", "Son dos formas de armar palabras."),
        ex("Verdadero o falso: puedo decir que una lengua es más avanzada porque arma palabras más largas.", "Falso", "Eso es jerarquizar lenguas."),
        ex(TOLU + " ¿Cómo se escribe «pájaro muy grande» en Tolu?", "lun-lun", "Se repite la raíz."),
    ],
    task=T("Compara aglutinación y reduplicación con este cuadro: «" + TOLU + "». Escribe en una tabla de tres filas (cómo se arma, qué cambia, ejemplo en Tolu y ejemplo en castellano). Después escribe una semejanza, una diferencia y una frase que explique por qué no se dice cuál es más avanzada. Termina con una pregunta que harías al educador tradicional.",
           "Aglutinación: se pegan piezas; cambia quién, cuántos o dónde; ka-pak-tu / paraguas. Reduplicación: se repite la raíz; cambia el tamaño; pak-pak / grande grande. Semejanza: ambas arman palabras. Diferencia: una pega y la otra repite. No se dice cuál es más avanzada porque cada lengua arma sus palabras a su manera. Pregunta: ¿cómo se hace esto en nuestra lengua?",
           ["usa criterios neutros", "da ejemplos de Tolu y de castellano", "no jerarquiza"], ["tabla comparativa", "semejanza y diferencia", "pregunta al educador"], ["decir que una forma es más avanzada", "ejemplos inventados de lenguas reales"],
           "Pedir que justifique cada fila con la regla; valorar que no juzgue."),
    reinforce="Haz una lista de cinco palabras del castellano que pegan partes y cinco que se repiten.",
    extend="Escribe un párrafo corto sobre por qué no hay lenguas «más simples» que otras.",
)
