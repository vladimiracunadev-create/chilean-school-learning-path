"""Cuaderno del estudiante, 8.º básico Inglés (oficial): IN08 OA 13, historias e información con recursos multimodales.

Los textos en inglés son originales y breves, con glosario en español dentro del enunciado. Las imágenes, los gráficos y los
afiches se describen con palabras dentro del enunciado, para poder resolverlos sin material externo. Los datos numéricos
son de ejemplo y están rotulados como tales. Los datos de países son generales y conocidos.
"""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA = "IN08 OA 13"


def E(rows):
    return [r if isinstance(r, dict) else ex(*r) for r in rows]


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": E(rec), "understand": E(und), "apply": E(app), "reason": E(rea), "challenge": E(cha)},
        context=E(context), selfcheck=E(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


# ============================================================ clase 1: experiencias personales y recursos multimodales
M1 = "Título: «My First Day Skating». Foto: una niña con casco en una pista de skate. Leyenda: «Me with my new helmet.» Texto: «Last Saturday I went to the skatepark with my cousin. I was nervous, but I tried again and again. Finally I stood on the board for ten seconds!» Globo de diálogo: «I did it!»"
G_M1 = "(skatepark = pista de skate; helmet = casco; tried again = lo intenté otra vez; stood = me mantuve de pie; board = tabla)"
H1 = "Título: «Hiking in the Hills». Foto: dos jóvenes con mochilas sentados en una roca, con la cara roja y una botella de agua. Texto: «Yesterday we went hiking. We walked for three hours and we were very tired. We ate fruit and drank water on a rock. The view was beautiful.»"
G_H1 = "(hiking = caminata; walked = caminamos; tired = cansados; drank = bebimos; rock = roca; view = vista)"

lesson(
    OA, 1,
    "Los textos, las fotos y los afiches descritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a contar una experiencia personal en inglés usando palabras junto con recursos como fotos, leyendas y globos de diálogo. Sirve para que otras personas entiendan y sientan mejor lo que viví.",
    ["Conozco el pasado simple de verbos como went, was y ate.", "Sé escribir oraciones de secuencia con first, then y finally."],
    [
        "Un texto multimodal combina varios modos: palabras, imágenes, colores, letras y diseño. Para contar una experiencia personal, el propósito es compartir lo que pasó y cómo te sentiste. El recurso (resource) correcto refuerza el mensaje: una foto de tu cara cansada apoya «I was very tired». Si la imagen dice algo distinto del texto, el mensaje se confunde.",
        "Los recursos más usados son: la foto o el dibujo (photo, drawing), la leyenda (caption, frase breve junto a la imagen), el globo de diálogo (speech bubble), el título (heading) y las viñetas o números. Una leyenda puede ser una frase sin verbo: «Me with my new helmet». El texto narra en pasado: went, was, saw, ate, took, tried. Usa palabras de sentimiento como nervous, tired, proud o happy.",
        "Para escribir tu texto, sigue este orden: primero elige tu propósito y tu audiencia; segundo, anota qué pasó en orden (First, Then, Finally); tercero, decide qué foto o dibujo apoya cada parte; cuarto, escribe una leyenda breve para cada imagen. Al final, revisa que imágenes y palabras cuenten la misma historia. Si una imagen no ayuda, cámbiala o quítala.",
    ],
    [("multimodal text", "texto con palabras e imágenes"), ("resource", "recurso"), ("caption", "leyenda"), ("speech bubble", "globo de diálogo"), ("heading", "título o encabezado"), ("went / was / ate / took", "fui / estuve / comí / tomé"), ("nervous / proud", "nervioso / orgulloso")],
    [
        ("Elegir la leyenda que calza con la foto", "Foto: dos niños sostienen un pez grande junto a un río. ¿Qué leyenda sirve: «Our first big fish!» o «The bus is late.»?",
         ["Mira lo que muestra la foto: un pez y dos niños.", "La leyenda debe hablar de eso.", "Our first big fish! calza con la imagen."], "Our first big fish!"),
        ("Revisar que imagen y texto cuenten lo mismo", "Texto: «I was very tired after the match.» Fotos posibles: 1) un joven bostezando sentado en una banca; 2) un mapa de Chile. ¿Cuál refuerza el mensaje? (match = partido; yawning = bostezando)",
         ["El mensaje es el cansancio.", "El joven bostezando muestra cansancio.", "El mapa no se relaciona con el texto."], "La foto 1, del joven bostezando."),
    ],
    [
        ("Escribir la experiencia en presente: «Yesterday I go to the beach».", "Yesterday indica un hecho pasado.", "Usa el pasado: Yesterday I went to the beach."),
        ("Poner una foto que no tiene relación con el texto.", "La imagen no refuerza el mensaje.", "Elige una imagen que muestre lo que cuenta el texto."),
    ],
    [
        ("Una leyenda (caption) es: a) una frase breve junto a la imagen b) un párrafo de diez líneas", "a", "Explica o acompaña la imagen con pocas palabras."),
        ("Completa: «Last summer we ___ to the lake.» Opciones: went, go.", "went", "Last summer indica pasado, y el pasado de go es went."),
        ("Un globo de diálogo (speech bubble) muestra: a) lo que dice un personaje b) el título", "a", "Es la forma de mostrar palabras habladas."),
    ],
    [
        (f"Lee: {M1} {G_M1} ¿Cuándo ocurrió la experiencia? a) Last Saturday b) Next Saturday", "a", "El texto dice Last Saturday, que es el sábado pasado."),
        (f"Lee: {M1} {G_M1} ¿Qué sentimiento aparece al comienzo? a) Nervous b) Bored", "a", "La narradora dice I was nervous."),
        (f"Lee: {M1} {G_M1} ¿Qué recurso muestra la alegría final de la niña? a) The speech bubble: I did it! b) The caption: Me with my new helmet", "a", "El globo de diálogo expresa su logro; la leyenda solo describe el casco."),
    ],
    [
        (f"Lee: {H1} {G_H1} Completa: «We ___ for three hours.» Opciones: walked, walk.", "walked", "El texto cuenta una caminata de ayer, así que va en pasado."),
        (f"Lee: {H1} {G_H1} ¿Qué detalle de la foto apoya la oración «We were very tired»? a) Red faces and a water bottle b) A big tree", "a", "La cara roja y la botella de agua muestran esfuerzo y cansancio."),
        (f"Lee: {H1} {G_H1} Elige una leyenda para la foto. a) Resting after three hours b) Lunch at school", "a", "La leyenda debe coincidir con el descanso después de caminar."),
    ],
    [
        (f"Lee: {H1} {G_H1} Un compañero quiere agregar una foto de una piscina. ¿Qué respondes? a) No, porque el texto habla de una caminata y la foto no refuerza el mensaje b) Sí, cualquier foto sirve", "a", "Cada imagen debe apoyar lo que cuenta el texto."),
        ("Ordena las partes de una experiencia: x) Finally, I stood on the board. y) First, I put on my helmet. z) Then I tried again and again. Escribe las tres letras en orden.", "y, z, x", "First va primero, Then en el medio y Finally al final."),
    ],
    [
        ("Texto: «On Friday I went to the museum with my class. I saw a big whale skeleton. It was amazing!» (whale skeleton = esqueleto de ballena; amazing = increíble) ¿Qué foto y qué leyenda refuerzan mejor el mensaje? a) Foto de un esqueleto de ballena, leyenda: «The whale skeleton was amazing» b) Foto de un perro, leyenda: «My dog is funny»", "a", "La foto y la leyenda repiten la experiencia del texto."),
        ("Un compañero escribió «I was go to the park yesterday». ¿Cuál es la corrección? a) I went to the park yesterday b) I goed to the park yesterday", "a", "Go es un verbo irregular y su pasado es went."),
    ],
    [("Tu curso arma un álbum digital con el título «Our Class Trip». Para la foto de un grupo frente a un bus, hay que elegir una leyenda corta en inglés. Opciones: «We were ready to travel!» o «Today is Monday and it is cold.» (travel = viajar) ¿Cuál elige una persona que quiere reforzar el mensaje de la foto? a) We were ready to travel! b) Today is Monday and it is cold.", "a", "Habla del bus, del grupo y del viaje, igual que la foto.")],
    [
        ("¿Qué tiempo verbal usas para contar algo que pasó ayer?", "Pasado simple", "Contar una experiencia pasada usa went, was, saw."),
        ("¿Cuál es el pasado de «eat»?", "Ate", "Es un verbo irregular."),
        ("Una imagen que no tiene relación con el texto, ¿refuerza el mensaje? Responde sí o no.", "No", "Debe mostrar lo que cuenta el texto."),
    ],
    task("Cuenta una experiencia breve usando este mini plan: Lugar: la feria de tu barrio. Cuándo: el sábado pasado. Foto: personas junto a un puesto de frutas. Sentimiento: happy. En tu hoja escribe un título, tres oraciones en pasado (con First, Then, Finally) y una leyenda para una foto. Dibuja la foto.", "Título: A Saturday at the Fair. First, I went to the fair with my aunt. Then we bought fruit. Finally we ate a juicy peach. Leyenda: Fresh fruit at the fair. I was happy.", ["usa pasado simple en las oraciones", "emplea First, Then, Finally", "leyenda y dibujo apoyan el texto"], ["hoja con título, oraciones, leyenda y dibujo"], ["escribir los verbos en presente", "dibujar algo que no está en el texto"], "Pide que explique por qué eligió esa foto y qué cambiaría si el sentimiento fuera nervous."),
    "Copia la tabla de vocabulario y escribe junto a cada palabra un dibujo pequeño.",
    "Escribe dos leyendas en inglés para dos fotos de tu familia o de objetos de tu casa, sin nombres personales.",
)

# ============================================================ clase 2: contenidos interdisciplinarios y datos
TAB2 = "Recycling week in class 8B (datos de ejemplo): Monday 4 kg, Tuesday 6 kg, Wednesday 5 kg, Thursday 9 kg of plastic."
GRO2 = "Plant growth in Science class (datos de ejemplo): day 1, 2 cm; day 5, 5 cm; day 10, 11 cm."
TAB2B = "Recycling week in class 8A (datos de ejemplo): Monday 3 kg, Tuesday 7 kg, Wednesday 8 kg, Thursday 4 kg."

lesson(
    OA, 2,
    "Los datos y las tablas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir información sobre contenidos de otras asignaturas, como Ciencias y Matemática, usando datos de una tabla o gráfico y una leyenda en inglés. Sirve para explicar datos con claridad.",
    ["Sé escribir una leyenda breve.", "Sé leer tablas con números."],
    [
        "Al escribir sobre contenidos de otras asignaturas (interdisciplinary content), tu texto necesita datos exactos. Un buen texto de información usa: un título, una tabla o gráfico con unidades (kg, cm, %), una leyenda y dos o tres oraciones que explican qué muestran los datos. Los datos de este cuaderno son de ejemplo, para practicar. En un trabajo real, copia solo datos que midió tu curso o que vienen de una fuente confiable.",
        "Para describir datos usa estas estructuras: «The chart shows…» (el gráfico muestra), «The highest / lowest number is…» (el número más alto / más bajo), «It increased from… to…» (aumentó de… a…), «It decreased» (disminuyó) y «In total, there are…» (en total hay…). Escribe la unidad después del número: 9 kg, 11 cm. Compara con «more than» (más que) y «less than» (menos que).",
        "Antes de escribir, revisa que cada afirmación coincida con la tabla. Si dices que Thursday fue el día más alto, comprueba que 9 kg es el mayor valor. Después, elige un recurso que ayude: un gráfico de barras para comparar días, un gráfico de línea para ver cambios en el tiempo, o un dibujo con etiquetas (labels) para partes de una planta.",
    ],
    [("chart", "gráfico"), ("table", "tabla"), ("increase / decrease", "aumentar / disminuir"), ("highest / lowest", "más alto / más bajo"), ("in total", "en total"), ("label", "etiqueta"), ("more than / less than", "más que / menos que")],
    [
        ("Describir un aumento con datos", f"Datos de ejemplo: day 1, 3 cm; day 8, 10 cm. Escribe una oración sobre el cambio entre el día 1 y el día 8. (plant = planta; growth = crecimiento)",
         ["El día 1 mide 3 cm y el día 8 mide 10 cm.", "Usa It increased from… to….", "Escribe las unidades."], "The plant increased from 3 cm to 10 cm."),
        ("Comprobar una afirmación contra la tabla", "Datos de ejemplo: Monday 2 kg, Tuesday 8 kg, Wednesday 6 kg of paper. Un compañero escribe: «Tuesday has the highest number». ¿Es correcta?",
         ["Mira todos los valores: 2, 8 y 6 kg.", "El mayor es 8 kg, el del martes.", "La afirmación es correcta."], "Sí, es correcta: 8 kg es el valor más alto."),
    ],
    [
        ("Escribir «9» sin unidad: «We collected 9 of plastic».", "Falta la unidad que explica de qué es el número.", "Escribe 9 kg of plastic."),
        ("Decir «The lowest day is Thursday» sin comparar con la tabla.", "No se revisó que el dato sea el menor.", "Compara todos los valores antes de escribir highest o lowest."),
    ],
    [
        ("«Highest» significa: a) el más alto b) el más bajo", "a", "Highest indica el mayor valor."),
        ("«In total» se usa para: a) dar la suma b) dar el título", "a", "In total indica el total."),
        ("Para un cambio en el tiempo, como la altura de una planta, sirve: a) un gráfico de línea b) una tabla de nombres", "a", "La línea muestra cómo cambia un dato en el tiempo."),
    ],
    [
        (f"Lee: {TAB2} ¿Qué día se recolectó menos plástico? a) Monday b) Thursday", "a", "El menor valor es 4 kg, el del lunes."),
        arith(f"Lee: {TAB2} ¿Cuántos kilos de plástico se recolectaron en total en los cuatro días? Escribe el número.", "4+6+5+9", "Se suman los cuatro valores de la tabla."),
        arith(f"Lee: {TAB2} ¿Cuántos kilos más se recolectaron el jueves que el lunes? Escribe el número.", "9-4", "Se resta el valor del lunes al del jueves."),
    ],
    [
        (f"Lee: {TAB2B} ¿Cuál oración es correcta? a) The highest number is 8 kg on Wednesday b) The highest number is 9 kg on Wednesday", "a", "El valor de miércoles es 8 kg y es el mayor de esa clase."),
        (f"Lee: {GRO2} Elige la leyenda más adecuada para un gráfico de línea. a) The plant grew 9 cm from day 1 to day 10 b) The plant is green", "a", "La leyenda con datos explica qué muestra el gráfico; 11 menos 2 son 9 cm."),
        arith(f"Lee: {GRO2} ¿Cuántos centímetros creció la planta entre el día 5 y el día 10? Escribe el número.", "11-5", "Se resta la altura del día 5 a la del día 10."),
    ],
    [
        (f"Lee: {TAB2} {TAB2B} Un compañero escribe: «Class 8A collected more plastic than class 8B in total». Comprueba los totales. ¿Tiene razón? a) No, class 8B collected 24 kg and class 8A collected 22 kg b) Sí, class 8A collected 24 kg", "a", "La clase 8B suma 4+6+5+9=24 kg y la 8A suma 3+7+8+4=22 kg."),
        (f"Lee: {TAB2} Una compañera dice que «the amount decreased from Wednesday to Thursday». Mira la tabla. ¿Es correcto? a) No, it increased from 5 kg to 9 kg b) Sí, disminuyó", "a", "De 5 kg a 9 kg es un aumento."),
    ],
    [
        arith(f"Lee: {TAB2} Debes escribir un aviso para el patio: «On Monday and Tuesday together we collected ___ kg of plastic». ¿Qué número escribes? Escribe el número.", "4+6", "Se suman los valores del lunes y del martes."),
        ("Quieres ilustrar las partes de una planta en Ciencias: raíz, tallo y hoja. ¿Qué recurso multimodal sirve mejor? a) Un dibujo con etiquetas (labels) b) Un gráfico de línea", "a", "Un dibujo con etiquetas nombra cada parte."),
    ],
    [(f"En el diario mural, un compañero dibuja un gráfico de barras con estos datos: {TAB2} Escribe la leyenda: «The bars show that plastic collection increased from Wednesday to Thursday.» ¿Coincide la leyenda con los datos? a) Sí, subió de 5 kg a 9 kg b) No, bajó de 9 kg a 5 kg", "a", "El miércoles hubo 5 kg y el jueves 9 kg, así que aumentó.")],
    [
        ("¿Qué escribes después de un número en un texto de ciencia?", "La unidad", "La unidad dice qué se mide, como kg o cm."),
        ("¿Qué expresión sirve para decir que algo subió: increased o decreased?", "Increased", "Increased significa aumentó."),
        ("¿Qué estructura usas para introducir lo que muestra un gráfico? a) The chart shows… b) I went to…", "a", "The chart shows presenta los datos."),
    ],
    task("Lee estos datos de ejemplo de una clase de Matemática: «Students who walk to school: Monday 12, Tuesday 15, Wednesday 11, Thursday 14.» (students = estudiantes; walk = caminan) En tu hoja dibuja un gráfico de barras sencillo, escribe un título, una leyenda y tres oraciones con the highest, the lowest e in total.", "Título: Walking to School. The highest number is 15 on Tuesday. The lowest number is 11 on Wednesday. In total, 52 students walked in four days.", ["incluye título y leyenda", "usa highest, lowest e in total con datos correctos", "el gráfico coincide con la tabla"], ["gráfico y tres oraciones en la hoja"], ["calcular mal el total", "poner una barra con altura distinta del dato"], "Pide que cambie el gráfico a una tabla y explique qué información se ve mejor en cada una."),
    "Copia los datos de la tabla y subraya el valor más alto y el más bajo con colores distintos.",
    "Con datos de ejemplo de tu cuaderno de Ciencias, escribe una oración con The chart shows….",
)

# ============================================================ clase 3: problemas globales (problema, causa, solución)
POS3 = "Título: «Save Water!» Imagen: una llave goteando sobre un balde. Texto: «Problem: Many taps drip all day. Cause: People forget to close them. Solution: Close the tap when you brush your teeth.» Eslogan: «Every drop counts.»"
G_POS3 = "(save = ahorrar; taps = llaves; drip = gotean; forget = olvidan; close = cerrar; brush your teeth = lavarse los dientes; drop = gota; counts = cuenta)"
POS3B = "Título: «Less Plastic, More Life». Imagen: una tortuga marina y una bolsa de plástico flotando. Texto: «Problem: Plastic bags reach the sea. Cause: Many people throw away bags after one use. Solution: Use a cloth bag.» Eslogan: «Say no to plastic bags.»"
G_POS3B = "(reach = llegan a; sea = mar; throw away = botan; use = uso; cloth bag = bolsa de tela)"

lesson(
    OA, 3,
    "Los afiches y los datos escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir sobre un problema global, como el agua o el plástico, con la estructura problema, causa y solución, y con un eslogan, una imagen y verbos de acción. Sirve para convencer y animar a otras personas.",
    ["Sé escribir oraciones con because y so.", "Conozco verbos como close, use y save."],
    [
        "Un problema global (global problem) afecta a muchos países: poca agua, plástico en el mar, contaminación del aire. Un texto de información sobre un problema suele tener tres partes: el problema (Problem), la causa (Cause) y la solución (Solution). Se unen con because (porque) y so (así que): «Many taps drip because people forget to close them. So we need to check the taps».",
        "Para convencer, un afiche (poster) combina un título corto, una imagen que refuerza el mensaje y un eslogan (slogan): una frase breve fácil de recordar, como «Every drop counts». Las soluciones usan el imperativo (imperative), la forma del verbo sin sujeto: Close the tap. Use a cloth bag. Don't waste water. Con let's (hagamos) invitas a todos: Let's recycle!",
        "Revisa que tu afiche sea claro y honesto. Usa datos solo si los conoces; si son de ejemplo, escribe «example». Evita palabras que asusten sin dar solución. Cada afiche necesita al menos una acción que cualquier persona pueda hacer: cerrar una llave, llevar una bolsa de tela, apagar luces. Una imagen sencilla, dos colores y letras grandes mejoran la lectura.",
    ],
    [("problem / cause / solution", "problema / causa / solución"), ("poster", "afiche"), ("slogan", "eslogan"), ("imperative", "verbo en imperativo: Close the tap"), ("let's", "hagamos"), ("waste", "desperdiciar"), ("because / so", "porque / así que")],
    [
        ("Clasificar una oración del afiche", f"Afiche: {POS3} {G_POS3} La oración «People forget to close them» ¿es problema, causa o solución?",
         ["Dice por qué las llaves gotean.", "Explicar el porqué es una causa.", "En el afiche está marcada como Cause."], "Es la causa."),
        ("Elegir un eslogan", "Tema: apagar las luces al salir de una sala. ¿Qué eslogan es más breve y fácil de recordar: «Switch off, save energy» o «You must remember that it is very important to switch off all the lights when you leave»? (switch off = apagar; save energy = ahorrar energía)",
         ["Un eslogan debe ser corto.", "La segunda opción es larga y difícil de recordar.", "La primera cumple lo que pide un eslogan."], "Switch off, save energy."),
    ],
    [
        ("Escribir una solución sin acción: «Water is important».", "Es un hecho, no una solución que una persona pueda hacer.", "Escribe una acción: Close the tap when you brush your teeth."),
        ("Usar un eslogan de tres líneas.", "Un eslogan largo no se recuerda.", "Reduce la idea a cuatro o seis palabras."),
    ],
    [
        ("Una solución se escribe con un verbo de acción, por ejemplo: a) Close the tap b) The tap is blue", "a", "El imperativo da una acción posible."),
        ("«Slogan» significa: a) eslogan b) solución", "a", "Es una frase breve que se recuerda."),
        ("«Because» une un problema con su: a) causa b) eslogan", "a", "Because significa porque y explica una causa."),
    ],
    [
        (f"Lee: {POS3} {G_POS3} ¿Qué imagen acompaña al afiche? a) A dripping tap over a bucket b) A closed tap beside a bucket", "a", "La imagen es una llave goteando sobre un balde."),
        (f"Lee: {POS3} {G_POS3} ¿Cuál es la solución? a) Close the tap when you brush your teeth b) People forget to close them", "a", "La segunda opción es la causa."),
        (f"Lee: {POS3B} {G_POS3B} ¿Cuál es el eslogan? a) Say no to plastic bags b) Less Plastic, More Life", "a", "El eslogan está rotulado como tal; la otra opción es el título."),
    ],
    [
        (f"Lee: {POS3B} {G_POS3B} Une la causa con la solución. ¿Qué solución responde a «Many people throw away bags after one use»? a) Use a cloth bag b) Draw a turtle", "a", "Una bolsa de tela se puede usar muchas veces."),
        ("Completa con la palabra correcta: «Many sea animals are in danger ___ they eat plastic.» (sea animals = animales marinos; danger = peligro) Opciones: because, so.", "because", "La parte final explica la causa de que mueran."),
        ("Completa: «The river is dirty, ___ let's clean it.» Opciones: so, because.", "so", "La segunda parte es la consecuencia o acción."),
    ],
    [
        (f"Lee: {POS3} {G_POS3} Un compañero cambia el eslogan por «Waste water!» (derrochar agua). ¿Por qué no sirve? a) Pide lo contrario del mensaje b) Es demasiado corto", "a", "El afiche quiere ahorrar agua y el eslogan pide desperdiciarla."),
        ("Una llave que gotea pierde, en un dato de ejemplo, 2 litros por hora. Según este dato, ¿cuántos litros se pierden en 6 horas? (litros = litres) a) 12 b) 8", "a", "2 litros por 6 horas son 12 litros."),
    ],
    [
        ("Eslogan A: «Plant trees today». Eslogan B: «Trees are tall and have leaves, and some are green, and some are brown». (plant = plantar) ¿Cuál es mejor para un afiche y por qué? a) A, porque es breve y pide una acción b) B, porque tiene más datos", "a", "Un eslogan breve con verbo de acción se recuerda mejor."),
        ("Quieres un afiche sobre la basura en la playa. ¿Qué combinación es la mejor? a) Título: Clean Beach; imagen: botellas en la arena; solución: Take your rubbish home b) Título: My birthday; imagen: un pastel; solución: none", "a", "Título, imagen y solución se relacionan con el tema."),
    ],
    [("Tu colegio prepara una campaña contra el desperdicio de pan en el casino. Un compañero propone esta secuencia: Problem: Students leave bread on the tray. Cause: They take too much bread. Solution: Take only what you eat. (leave = dejan; tray = bandeja; take = toman) ¿Qué parte del afiche es «Take only what you eat»? a) La solución b) La causa", "a", "Es una acción con imperativo que resuelve el problema.")],
    [
        ("¿Qué tres partes tiene un texto de información sobre un problema global?", "Problema, causa y solución", "Organizan el afiche."),
        ("¿Qué forma verbal se usa para dar órdenes o consejos, como Close the tap?", "Imperativo", "Se usa el verbo sin sujeto."),
        ("Un eslogan, ¿debe ser largo o breve?", "Breve", "Así se recuerda y se lee rápido."),
    ],
    task("Escribe en tu hoja un afiche corto sobre el problema de la luz que se deja encendida en una sala vacía. Incluye: título, Problem, Cause y Solution con un verbo de acción, y un eslogan de máximo seis palabras. Dibuja la imagen: un interruptor y una ampolleta. (interruptor = switch; ampolleta = light bulb)", "Título: Light Off! Problem: Lights stay on in empty rooms. Cause: We forget to switch them off. Solution: Switch off the light when you leave. Eslogan: Last out, lights out.", ["tiene problema, causa y solución", "la solución usa un imperativo", "el eslogan es breve"], ["afiche con texto y dibujo en la hoja"], ["escribir una solución que no es una acción", "poner un eslogan demasiado largo"], "Pide que cambie la solución por una acción para otro lugar, como el casino, y que explique qué cambió."),
    "Copia el vocabulario y escribe junto a cada palabra un ejemplo de afiche donde puedes usarla.",
    "Escribe tres consejos en inglés para ahorrar agua en casa usando verbos en imperativo.",
)

# ============================================================ clase 4: cultura de otros países (brecha de información)
CJ4 = "Tarjeta de Japón. Japan is an island country in Asia. The capital is Tokyo. People often bow to say hello. Many people take off their shoes at home. Rice is a very common food."
CK4 = "Tarjeta de Kenia. Kenya is a country in Africa. The capital is Nairobi. The official languages are English and Swahili. Many people visit its national parks to see wild animals."
G_CJK4 = "(island = isla; bow = hacer una reverencia; take off = sacarse; shoes = zapatos; official languages = idiomas oficiales; national parks = parques nacionales; wild animals = animales salvajes)"
CA4 = "Tarjeta de Australia. English is the main language. The capital is Canberra. Kangaroos are animals that live in the wild there."
CM4 = "Tarjeta de México. Spanish is the main language. The capital is Mexico City. Tortillas are a common food."
G_CAM4 = "(main language = idioma principal; capital = capital; kangaroos = canguros; live in the wild = viven en estado salvaje; tortillas = tortillas)"

lesson(
    OA, 4,
    "Las tarjetas de países escritas en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir información sobre la cultura de otros países y a comparar dos países con datos de dos tarjetas. Sirve para un afiche o un informe que respete lo que cada país tiene.",
    ["Sé usar is y are para datos.", "Conozco palabras como capital, language y food."],
    [
        "Para escribir sobre la cultura de otro país (culture of other countries), usa datos simples y comprobables: ubicación, capital, idioma, comida y costumbres frecuentes. Evita generalizar con frases como «All people in X are…». Mejor escribe «Many people… / Often…», porque dentro de un país hay mucha diversidad. Trata cada cultura con respeto y sin burlas.",
        "Para comparar usa Both… and… (los dos…), In X people…, but in Y… (en X la gente…, pero en Y…), also (también) y like (como). Ejemplo: «Both Japan and Kenya have a capital city. Japan is in Asia, but Kenya is in Africa». Compara siempre el mismo tipo de dato (capital con capital, idioma con idioma) y usa un solo dato por oración, con una palabra de comparación.",
        "En una brecha de información (information gap) tú tienes la tarjeta de un país y otra persona tiene la del otro. Cada uno lee su tarjeta en voz alta y el otro anota. Si falta un dato, pregunta con What is the capital? o Which language do they speak? No inventes lo que no está en las tarjetas. Al final, pegan las dos tarjetas en un solo afiche con un título, una tabla y dos imágenes.",
    ],
    [("culture", "cultura"), ("capital", "capital"), ("official language", "idioma oficial"), ("custom", "costumbre"), ("both… and…", "tanto… como…"), ("but", "pero"), ("also", "también")],
    [
        ("Comparar con both", f"Tarjetas: {CJ4} {CK4} {G_CJK4} ¿Qué tienen en común Japón y Kenia según las tarjetas?",
         ["Busca un dato que aparezca en las dos.", "Ambas tienen capital.", "Ambos son países; Tokyo y Nairobi son capitales."], "Los dos tienen una capital: Tokyo en Japón y Nairobi en Kenia."),
        ("Escribir una oración de contraste", f"Tarjetas: {CJ4} {CK4} {G_CJK4} Escribe una oración con but que contraste el mismo tipo de dato en cada país.",
         ["Elige el mismo tipo de dato en las dos tarjetas: dónde está cada país.", "Japón está en Asia y Kenia está en África.", "Une los dos datos con but y revisa que cada uno esté en su tarjeta."], "Japan is a country in Asia, but Kenya is a country in Africa."),
    ],
    [
        ("Escribir «All people in Japan bow to say hello».", "Es una generalización: no todas las personas actúan igual.", "Escribe Many people in Japan often bow to say hello."),
        ("Mezclar los datos de las dos tarjetas en una misma oración sin decir a qué país corresponden.", "El lector no sabe qué dato es de cada país.", "Usa In X… but in Y… o nombra cada país."),
    ],
    [
        ("«Both… and…» se usa para decir: a) algo que tienen los dos b) algo que no tiene ninguno", "a", "Both señala lo común."),
        ("«Official language» es: a) idioma oficial b) comida típica", "a", "Es el idioma reconocido por el país."),
        ("La capital de Kenia según la tarjeta es: a) Nairobi b) Tokyo", "a", "Tokyo es la capital de Japón."),
    ],
    [
        (f"Lee: {CA4} {CM4} {G_CAM4} ¿Cuál es la capital de Australia? a) Canberra b) Mexico City", "a", "La tarjeta de Australia dice Canberra."),
        (f"Lee: {CA4} {CM4} {G_CAM4} ¿Qué idioma es el principal en México? a) Spanish b) English", "a", "La tarjeta de México dice que el idioma principal es el español."),
        (f"Lee: {CA4} {CM4} {G_CAM4} ¿Qué dato aparece solo en la tarjeta de Australia? a) Kangaroos live in the wild b) Tortillas are common", "a", "Los canguros se mencionan solo en la tarjeta de Australia."),
    ],
    [
        (f"Lee: {CA4} {CM4} {G_CAM4} Completa: «___ Australia and Mexico have a capital city.» Opciones: Both, Only.", "Both", "Las dos tarjetas dan una capital."),
        (f"Lee: {CA4} {CM4} {G_CAM4} Elige la oración correcta. a) In Mexico the main language is Spanish, but in Australia it is English b) In Mexico the main language is English, but in Australia it is Spanish", "a", "Cada idioma coincide con la tarjeta."),
        (f"Lee: {CJ4} {G_CJK4} Elige la oración que evita generalizar. a) Many people in Japan often bow to say hello b) All people in Japan bow to say hello", "a", "Many y often permiten diferencias entre personas."),
    ],
    [
        (f"Lee: {CJ4} {CK4} {G_CJK4} Una compañera escribió: «In Kenya people take off their shoes at home». ¿Qué problema tiene? a) Ese dato está en la tarjeta de Japón, no en la de Kenia b) Está bien, porque todos se sacan los zapatos", "a", "Mezcló los datos de las dos tarjetas."),
        (f"Tu compañero A tiene la tarjeta de Australia y tú la de México. Tu tarjeta dice: {CM4} {G_CAM4} Él pregunta: «What is the capital of Mexico?». ¿Qué respondes? a) Mexico City b) Canberra", "a", "Tu tarjeta de México dice que la capital es Mexico City."),
    ],
    [
        ("Para un afiche que compara dos países, ¿cómo debe ser la tabla? a) Una columna para cada país con los mismos tipos de dato, como capital e idioma b) Una columna con datos de un solo país", "a", "Para comparar hay que poner el mismo tipo de dato de ambos países."),
        (f"Lee: {CJ4} {CK4} {G_CJK4} Una compañera dice que Tokyo es la capital de Kenia. ¿Cuál es la corrección? a) Tokyo is the capital of Japan and Nairobi is the capital of Kenya b) Tokyo is the capital of both countries", "a", "Las tarjetas indican una capital para cada país."),
    ],
    [("Tu curso prepara una feria de culturas. Un compañero hace un letrero sobre Australia: «Kangaroos are animals that live in the wild there. They are the only animals in the whole country.» ¿Qué parte del letrero no está respaldada por la tarjeta? (whole country = país entero) a) They are the only animals in the whole country b) Kangaroos live in the wild there", "a", "La tarjeta no dice que los canguros sean los únicos animales.")],
    [
        ("¿Qué palabra usas para señalar algo que tienen los dos países?", "Both", "Both significa los dos."),
        ("¿Qué debes hacer si falta un dato en tu tarjeta?", "Preguntar o decir que no lo sabes", "No se inventa información sobre una cultura."),
        ("¿Es mejor escribir «All people» o «Many people» al hablar de las costumbres de un país?", "Many people", "Evita generalizar sobre todas las personas."),
    ],
    task("Lee dos tarjetas distintas de ejemplo. Tarjeta de Perú: «Peru is a country in South America. The capital is Lima. Spanish is an official language.» Tarjeta de Nueva Zelanda: «New Zealand is an island country. The capital is Wellington. English is an official language.» (island = isla; official language = idioma oficial) En tu hoja arma un afiche con un título, una tabla con capital e idioma, y dos oraciones: una con Both… and… y otra con but.", "Título: Two Countries. Both Peru and New Zealand have an official language. In Peru the capital is Lima, but in New Zealand the capital is Wellington.", ["usa solo datos de las tarjetas", "escribe una oración con Both… and… y otra con but", "ordena título, tabla y oraciones"], ["afiche de comparación en la hoja"], ["agregar datos que no están en las tarjetas", "mezclar los datos de los países"], "Pide que revise con otra persona si las oraciones coinciden con las tarjetas y que anote una diferencia más."),
    "Copia el vocabulario y escribe una oración con both y otra con but.",
    "Escribe dos preguntas en inglés que harías para completar la tarjeta de un país, como What is the capital?",
)

# ============================================================ clase 5: textos leídos (reseña multimodal)
LH5 = "The Lighthouse Cat. Paragraph 1: Mina lives with her uncle in a lighthouse on a cold coast. Every night a grey cat sits at the window. Paragraph 2: One stormy night, the cat jumps on the lamp switch and the light turns on. Paragraph 3: A small boat sees the light and returns safely to the port. Paragraph 4: Mina names the cat Star."
G_LH5 = "(lighthouse = faro; coast = costa; lamp switch = interruptor de la lámpara; turns on = se enciende; safely = sin peligro; port = puerto; names = nombra)"
RV5 = "Reseña de ejemplo. Título: «The Lighthouse Cat». Calificación: 4 estrellas de 5. Imagen: un gato gris junto a una ventana, de noche. Leyenda: «Star waits at the window». Opinión: «I like this story because the cat helps a boat.»"
G_RV5 = "(review = reseña; rating = calificación; stars = estrellas; opinion = opinión)"

lesson(
    OA, 5,
    "El cuento y las reseñas escritos en cada ejercicio, lápiz y una hoja.",
    "Aprenderé a escribir una reseña de un texto que leí, con título, calificación, una imagen con leyenda y una opinión justificada. Sirve para recomendar una lectura a otras personas de forma clara y creativa.",
    ["Sé escribir una leyenda y una opinión con because.", "Sé resumir inicio, desarrollo y final."],
    [
        "Una reseña (review) cuenta de qué trata un texto que leíste y da tu opinión. Es un texto multimodal: lleva el título del texto, una calificación (rating) con estrellas, una imagen o dibujo con leyenda, un resumen corto y una opinión con razón. Las reseñas ayudan a otras personas a decidir si quieren leerlo.",
        "El resumen cuenta solo lo esencial, en presente: «A cat helps a boat find the port». No reveles todo el final si quieres que otros lo lean. La opinión se escribe con expresiones como «I like… because…», «I think… is great because…» o «I do not like… because…». Siempre incluye la razón, y que la razón venga del texto. La calificación debe ser coherente: si dices que te encantó, no pongas una estrella.",
        "Para elegir la imagen, piensa en el momento más importante: el gato junto a la ventana, el barco volviendo al puerto. La leyenda la describe en una frase breve. Revisa que el título, el resumen, la imagen y la opinión hablen del mismo texto. Una reseña bien hecha cabe en media hoja y se entiende sin haber leído el cuento.",
    ],
    [("review", "reseña"), ("rating", "calificación"), ("star", "estrella"), ("summary", "resumen"), ("opinion", "opinión"), ("recommend", "recomendar"), ("I like… because…", "me gusta… porque…")],
    [
        ("Armar un resumen breve", f"Texto: «{LH5}» {G_LH5} Escribe un resumen de una oración sin contar el final completo.",
         ["Identifica quién y qué: un gato ayuda a un barco.", "Usa presente.", "Resume sin repetir los párrafos."], "A cat in a lighthouse helps a boat find the port."),
        ("Justificar una opinión", f"Texto: «{LH5}» {G_LH5} ¿Qué opinión con razón puedes escribir? Elige la razón del texto.",
         ["Una opinión necesita un porque.", "La razón debe venir del texto.", "I like this story because the cat helps a boat."], "I like this story because the cat helps a boat."),
    ],
    [
        ("Escribir «I like it» sin razón.", "Una opinión sin razón no convence.", "Agrega because y una razón del texto."),
        ("Contar todo el final en la reseña.", "Quita las ganas de leer el texto.", "Resume el inicio y el problema sin revelar el cierre."),
    ],
    [
        ("Una «review» es: a) una reseña con opinión b) un horario", "a", "La reseña combina resumen y opinión."),
        ("En una escala de 5 estrellas, «Rating: 5 stars» indica: a) la calificación más alta b) la calificación más baja", "a", "Cinco estrellas de cinco es la calificación máxima de la escala."),
        ("Una opinión debe llevar: a) una razón con because b) solo un nombre propio", "a", "La razón la justifica."),
    ],
    [
        (f"Lee: «{LH5}» {G_LH5} ¿Dónde vive Mina? a) In a lighthouse b) In a port", "a", "El párrafo 1 dice lives with her uncle in a lighthouse."),
        (f"Lee: «{LH5}» {G_LH5} ¿Qué hace el gato en la noche de tormenta? a) Turns on the light by jumping on the switch b) Sleeps by the window", "a", "El párrafo 2 cuenta que salta sobre el interruptor y la luz se enciende."),
        (f"Lee: {RV5} {G_RV5} ¿Qué calificación da la reseña? a) 4 stars b) 2 stars", "a", "Dice 4 estrellas de 5."),
    ],
    [
        (f"Lee: {RV5} {G_RV5} ¿Qué parte es la leyenda? a) Star waits at the window b) I like this story because the cat helps a boat", "a", "La leyenda acompaña la imagen; la otra frase es la opinión."),
        (f"Lee: {RV5} {G_RV5} ¿Cuál es la razón de la opinión? a) The cat helps a boat b) The story is short", "a", "Después de because aparece la razón."),
        (f"Lee: «{LH5}» {G_LH5} ¿Qué imagen elegirías para la reseña? a) A cat at a window at night b) A busy beach in summer", "a", "Es una escena de un momento importante del cuento."),
    ],
    [
        (f"Lee: «{LH5}» {G_LH5} Un compañero escribió: «I give 5 stars because the story has a lot of cars». ¿Qué problema tiene la reseña? a) La razón no viene del texto b) La calificación es muy alta", "a", "En el cuento no hay autos, así que la razón es falsa."),
        ("Una reseña dice: «Rating: 1 star. I love this story because it is exciting and I want to read it again.» ¿Qué incoherencia tiene? a) La calificación es muy baja para una opinión tan positiva b) Falta el título", "a", "Dice que le encanta, pero da la nota más baja."),
    ],
    [
        (f"Lee: «{LH5}» {G_LH5} ¿Qué oración resume mejor el cuento sin revelar el final? a) A cat helps a boat on a stormy night b) The boat returns to the port and Mina names the cat Star c) The cat is grey", "a", "Cuenta quién y qué sin explicar el desenlace completo."),
        (f"Lee: «{LH5}» {G_LH5} ¿Cuál es el tema posible del cuento? a) Animals can help people b) Lighthouses are very old", "a", "El gato salva a un barco, lo que muestra la ayuda de un animal."),
    ],
    [("Tu curso prepara un mural con reseñas de lecturas. Una compañera presenta: Título: «Wind Kite». Imagen: un volantín rojo sobre un cerro. Leyenda: «The kite flies high». Opinión: «I recommend it because it is short and funny.» (kite = volantín; hill = cerro; recommend = recomendar; short = corto) ¿Cuántos de estos elementos tiene: título, imagen, leyenda, opinión con razón? Escribe el número.", "4", "Tiene título, imagen, leyenda y opinión con razón.")],
    [
        ("¿Qué palabra une tu opinión con su razón?", "Because", "Because significa porque."),
        ("¿En qué tiempo se resume una historia en una reseña: presente o pasado?", "Presente", "Se usa el presente para resumir un texto."),
        ("¿Qué debe hacer la imagen de una reseña: reforzar el texto o no tener relación?", "Reforzar el texto", "La imagen debe mostrar un momento del texto leído."),
    ],
    task("Lee este texto: «Title: The Red Bike. Paragraph 1: Gabo has an old red bike and wants to enter a race. Paragraph 2: His bike is slow, but he practises every morning. Paragraph 3: In the race, he finishes fourth. He is proud and smiles.» (enter = inscribirse en; race = carrera; practises = practica; finishes = termina; fourth = cuarto) En tu hoja arma una reseña con: título, calificación en estrellas, un dibujo con leyenda, resumen en una oración y opinión con because.", "Título: The Red Bike. Rating: 4 stars. Imagen: un niño en bicicleta roja. Leyenda: Gabo practises every morning. Resumen: A boy practises hard for a race. Opinión: I like it because Gabo does not give up.", ["incluye título, estrellas, dibujo y leyenda", "el resumen no cuenta todo el final", "la opinión tiene because y una razón del texto"], ["reseña completa en media hoja"], ["opinión sin razón", "razón que no está en el texto"], "Pide que lea su reseña a una persona de su casa y le pregunte si le dieron ganas de leer el texto."),
    "Copia las partes de una reseña en una lista: título, calificación, imagen y leyenda, resumen y opinión.",
    "Escribe una mini reseña de un libro o una película que te guste, con título, estrellas y una opinión con because.",
)
