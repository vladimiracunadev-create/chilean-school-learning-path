"""Cuaderno del estudiante, 7.º básico Inglés (oficial), IN07 OA 10 (comprensión de textos no literarios: descripciones,
instrucciones, procedimientos, avisos publicitarios, correos, páginas web, biografías y gráficos). Todos los textos son
originales o datos generales muy conocidos; cada uno trae su glosa en español.
"""
from __future__ import annotations

from student_content_in7_a import lesson, task
from student_lessons import arith

OA10 = "IN07 OA 10"
MAT = "Los textos y datos escritos en cada ejercicio, lápiz y, si quieres, un destacador o un lápiz de color para subrayar las pistas."

TURTLE = "«Our class turtle, Pancho, is small and green. He eats lettuce and moves very slowly. He sleeps in a box under the window. He looks happy when the students talk quietly, but he looks unhappy when the room is noisy.» (turtle = tortuga, lettuce = lechuga, moves = se mueve, window = ventana, noisy = ruidoso)"
TENT = "«How to set up a small tent in the school yard. First, find a flat place without stones. Second, lay the tent on the ground. Next, put the poles through the tent. Then ask a friend to hold the poles while you fix the corners. Finally, check that the tent is tight.» (set up = armar, tent = carpa, flat = plano, stones = piedras, poles = varillas, hold = sostener, fix = fijar, corners = esquinas, tight = firme)"
LAB = "«NOTICE: Science Lab Rules. Before the class, wash your hands. While you work, wear goggles. After the experiment, clean your table. You must not run in the lab. Ask the teacher before you use any tool.» (notice = aviso, goggles = lentes de seguridad, experiment = experimento, tool = herramienta)"
PLANT = "«How to take care of a class plant. First, check the soil every morning. If it is dry, add a little water. Do not add too much water because the roots can rot. After a week, turn the pot a quarter so every side gets light.» (soil = tierra, dry = seca, roots = raíces, rot = pudrirse, pot = maceta, a quarter = un cuarto de vuelta)"
SHOES = "«Super Sneakers! Run faster with our new Wave shoes. They are light, comfortable and cheap. Buy two pairs and get one T-shirt free! Only until Sunday. Everyone loves them!» (sneakers = zapatillas, faster = más rápido, light = livianas, cheap = baratas, pairs = pares, free = gratis, everyone = todos)"
JUICE = "«Sunny Juice: 100% fruit, no sugar added. Each bottle has 300 ml. Price: $1,500.» (juice = jugo, fruit = fruta, sugar = azúcar, added = agregada, bottle = botella, price = precio)"
MAIL = "«Subject: Book Fair. Dear students, the Book Fair is on Friday from 10:00 to 14:00 in the gym. Entry is free. Please bring a bag. Mrs. Rojas» (book fair = feria del libro, entry = entrada, bring = traer, bag = bolsa)"
WEB = "«Book Fair. Date: Friday. Time: 10:00 to 15:00. Place: Gym. Free entry. Activities: author talk at 11:00.» (date = fecha, place = lugar, author talk = charla de un autor)"
POSTER = "«BOOK FAIR! FRIDAY! GYM! Meet an author! Free!» (meet = conoce, author = autor, free = gratis)"
BIO = "«Gabriela Mistral was a Chilean poet and teacher. She was born in 1889. She won the Nobel Prize in Literature in 1945.» (poet = poeta, teacher = profesora, was born = nació, won = ganó, prize = premio, literature = literatura)"
RECYCLE = "«RECYCLING GUIDE. Paper: blue bin. Plastic: yellow bin. Glass: green bin. Batteries: special box in the office. Note: Clean the containers first.» (guide = guía, bin = contenedor, batteries = pilas, office = oficina, note = nota, containers = envases)"
BUS = "«Bus 12 timetable. School days (Monday to Friday): 7:15, 7:45, 8:15. Weekend: 9:00, 10:00. Bus stop: Pine Street. Note: no service on holidays.» (timetable = horario, school days = días de clases, weekend = fin de semana, bus stop = paradero, service = servicio, holidays = feriados)"

# ------------------------------------------------------------------ clase 1
lesson(
    OA10, 1, MAT,
    "Aprenderé a leer descripciones e instrucciones y a reconocer palabras derivadas con el prefijo un- y los sufijos -ing y -ly. Sirve para entender cómo es algo, qué hacer y cómo se hace.",
    ["Sé reconocer el formato y el propósito de un texto.", "Conozco first, next, finally y adjetivos como small y quiet."],
    [
        "Una descripción (description) dice cómo es algo: su tamaño, su color, qué come, dónde duerme. Usa adjetivos como small y green y verbos como is, has y eats. Unas instrucciones (instructions) dicen qué hacer, en pasos, con verbos en forma de orden: find, lay, put, check. Los conectores first, second, next, then y finally marcan el orden.",
        "Muchas palabras nuevas se forman a partir de otras. El prefijo un- le da el sentido contrario: happy (feliz) se vuelve unhappy (infeliz), tidy (ordenado) se vuelve untidy (desordenado) y safe (seguro) se vuelve unsafe (inseguro). El sufijo -ly convierte un adjetivo en adverbio de modo: slow se vuelve slowly (despacio), quiet se vuelve quietly (en silencio) y careful se vuelve carefully (con cuidado). El sufijo -ing forma el gerundio: read se vuelve reading (leyendo o la lectura).",
        "Cuando encuentres una palabra larga desconocida, busca la base. Si ves untidy, elimina un- y lee tidy. Luego piensa qué cambia. Ese truco te ayuda a entender sin diccionario. En unas instrucciones, subraya los verbos de acción y numera los pasos para no perderte; en una descripción, subraya los adjetivos.",
    ],
    [("description", "descripción: dice cómo es algo"), ("instructions", "instrucciones: pasos para hacer algo"), ("un-", "prefijo que da el sentido contrario (unhappy)"), ("-ly", "sufijo que forma adverbios (slowly)"), ("-ing", "sufijo del gerundio (reading)"), ("step", "paso")],
    [
        ("Detalles de una descripción", TURTLE + " ¿Qué come Pancho y de qué color es?", ["Busco eats y green.", "Dice He eats lettuce.", "Dice small and green."], "Come lechuga y es verde"),
        ("Palabra derivada", "¿Qué significa unhappy?", ["Quito un-: queda happy.", "Un- da el sentido contrario.", "Unhappy es infeliz."], "Infeliz o triste"),
    ],
    [
        ("Pensar que un- siempre significa «uno».", "Se confunde con un número.", "Un- da el sentido contrario: happy, unhappy."),
        ("Leer los pasos sin respetar el orden.", "No se miran los conectores.", "Numera cada paso con first, next, then y finally."),
    ],
    [
        (TURTLE + " ¿De qué color es Pancho?", "Verde", "Dice small and green."),
        (TURTLE + " ¿Qué come Pancho?", "Lechuga", "Dice He eats lettuce."),
        (TENT + " ¿Qué se hace primero? a) encontrar un lugar plano sin piedras b) fijar las esquinas", "a) encontrar un lugar plano sin piedras", "Dice First, find a flat place without stones."),
    ],
    [
        (TURTLE + " «Slowly» viene de slow. ¿Qué indica? a) cómo se mueve b) cuánto come", "a) cómo se mueve", "Slowly es un adverbio de modo."),
        (TENT + " ¿Cuántos pasos están marcados con First, Second, Next, Then y Finally?", "5", "Son cinco conectores y cinco pasos."),
        (TURTLE + " ¿Cuándo se ve infeliz Pancho? a) cuando la sala es ruidosa b) cuando come lechuga", "a) cuando la sala es ruidosa", "Dice he looks unhappy when the room is noisy."),
    ],
    [
        ("«Tidy» significa ordenado. ¿Qué significa untidy?", "Desordenado", "Un- da el sentido contrario."),
        ("¿Qué indica -ly en quietly? a) que es un adverbio de modo (cómo) b) que es un número", "a) que es un adverbio de modo (cómo)", "Quietly significa en silencio."),
        ("¿Qué muestra -ing en «He is reading»? a) una acción que ocurre ahora b) una acción terminada", "a) una acción que ocurre ahora", "El gerundio muestra una acción en curso."),
    ],
    [
        ("¿Qué significa «He carries the box carefully»?", "Lleva la caja con cuidado", "Carefully viene de careful."),
        (TENT + " ¿Qué hace un amigo mientras tú fijas las esquinas?", "Sostiene las varillas", "Dice ask a friend to hold the poles."),
    ],
    [
        (TENT + " ¿Qué palabra marca el último paso? a) Finally b) Second", "a) Finally", "Finally significa finalmente."),
        ("Lugar A: plano, sin piedras y lejos de la calle. Lugar B: al borde de la calle. ¿Cuál lugar es unsafe para una carpa?", "El lugar B", "Unsafe significa inseguro y la calle es peligrosa."),
    ],
    [(TENT + " Revisas la lista de pasos y ves que alguien puso la carpa antes de buscar un lugar plano. ¿Qué paso se saltó? a) First, find a flat place b) Finally, check the tent", "a) First, find a flat place", "El primer paso es buscar el lugar.")],
    [
        ("¿Qué hace el prefijo un-?", "Da el sentido contrario", "Happy se vuelve unhappy."),
        ("¿Qué convierte un adjetivo en adverbio?", "El sufijo -ly", "Slow se vuelve slowly."),
        ("¿Qué palabras marcan el orden de los pasos?", "First, next, then y finally", "Son conectores de secuencia."),
    ],
    task("Lee esta descripción: «My cousin Lucas is tall and thin. He has dark hair. He plays the guitar very well, and he sings quietly. He gets unhappy when his guitar is out of tune.» (tall = alto, thin = delgado, dark hair = pelo oscuro, out of tune = desafinada). Escribe tres rasgos de Lucas, un adverbio terminado en -ly y una palabra con el prefijo un- y su significado.", "Rasgos: alto, delgado, pelo oscuro. Adverbio: quietly. Palabra: unhappy, que significa infeliz.", ["tres rasgos del texto", "un adverbio con -ly", "una palabra con un- y su significado"], ["hoja con cuatro respuestas", "nota de quien revisó"], ["inventar rasgos", "confundir un- con -ing"], "Reconoce los rasgos acertados y revisa cómo se forma cada palabra derivada."),
    "Haz una lista de seis palabras con un-, -ly o -ing que conozcas en español o inglés y explica su base.",
    "Escribe cuatro pasos en inglés para armar una carpa de juguete, usando first, next, then y finally.",
)

# ------------------------------------------------------------------ clase 2
lesson(
    OA10, 2, MAT,
    "Aprenderé a interpretar procedimientos y avisos con conectores como before, after, while, when, if y because. Sirve para seguir reglas e instrucciones en el orden correcto y entender por qué se dan.",
    ["Sé leer instrucciones con first, next y finally.", "Conozco must y don't."],
    [
        "Un procedimiento (procedure) explica cómo se hace algo con pasos ordenados, y un aviso (notice) da reglas o información para un lugar. Los conectores muestran la relación entre las acciones. Before significa antes de y after significa después de. While indica dos acciones a la vez. When y if introducen una condición: If it is dry, add a little water. Because explica una causa.",
        "En el aviso del laboratorio, la secuencia es: antes de la clase, lavarse las manos (before); mientras se trabaja, usar lentes (while); después del experimento, limpiar la mesa (after). Must not y do not expresan prohibiciones. Fíjate también en la causa: Do not add too much water because the roots can rot. La razón de la regla es lo que sigue a because: las raíces pueden pudrirse.",
        "Para seguir un procedimiento, marca los conectores, numera las acciones y relee antes de actuar. Distingue entre el orden (first, after a week) y la condición (if). Las relaciones de adición se marcan con and, also y too: you must wear goggles and gloves; the teacher also helps. Comprender estas relaciones evita errores y accidentes.",
    ],
    [("procedure", "procedimiento: pasos de cómo se hace algo"), ("notice", "aviso: texto con reglas o información"), ("before / after", "antes de / después de"), ("while", "mientras"), ("if", "si (condición)"), ("because", "porque")],
    [
        ("Secuencia en un aviso", LAB + " ¿Qué se hace antes de la clase?", ["Busco Before the class.", "Dice wash your hands.", "Es lavarse las manos."], "Lavarse las manos"),
        ("Condición", PLANT + " ¿Qué se hace si la tierra está seca?", ["Busco If it is dry.", "Dice add a little water.", "Agregar un poco de agua."], "Agregar un poco de agua"),
    ],
    [
        ("Confundir before con after.", "Marcan el orden en sentido contrario.", "Before es antes de y after es después de."),
        ("Ignorar la condición de if.", "Se hace la acción siempre, aunque no corresponda.", "Haz la acción solo si se cumple la condición."),
    ],
    [
        (LAB + " ¿Qué se hace antes de la clase?", "Lavarse las manos", "Dice Before the class, wash your hands."),
        (LAB + " ¿Qué se usa mientras se trabaja?", "Lentes de seguridad", "Dice While you work, wear goggles."),
        (LAB + " ¿Qué se hace después del experimento?", "Limpiar la mesa", "Dice After the experiment, clean your table."),
    ],
    [
        (LAB + " ¿Qué palabra indica que dos cosas ocurren a la vez? a) while b) after", "a) while", "While significa mientras."),
        (PLANT + " ¿Qué se hace si la tierra está seca?", "Agregar un poco de agua", "Dice If it is dry, add a little water."),
        (PLANT + " ¿Por qué no hay que agregar demasiada agua?", "Porque las raíces pueden pudrirse", "Dice because the roots can rot."),
    ],
    [
        (PLANT + " ¿Cada cuánto se gira la maceta?", "Después de una semana, un cuarto de vuelta", "Dice After a week, turn the pot a quarter."),
        (LAB + " Ordena. A) Limpiar la mesa. B) Lavarse las manos. C) Usar lentes.", "B, C, A", "Primero before, luego while y por último after."),
        (LAB + " «Ask the teacher before you use any tool». ¿Cuándo se pregunta al profesor? a) antes de usar una herramienta b) después de usarla", "a) antes de usar una herramienta", "Before significa antes de."),
    ],
    [
        (PLANT + " En «Do not add too much water because the roots can rot», ¿cuál es la razón de la advertencia? a) las raíces pueden pudrirse b) la tierra está seca", "a) las raíces pueden pudrirse", "Lo que sigue a because es la razón de la regla."),
        (LAB + " ¿«You must not run in the lab» es una obligación o una prohibición?", "Una prohibición", "Must not prohíbe correr."),
    ],
    [
        arith(PLANT + " Si revisas la tierra cada mañana de lunes a viernes durante 3 semanas, ¿cuántas veces la revisas?", "5*3", "Se multiplican los días por las semanas.", " veces"),
        (LAB + " ¿Cuántas oraciones dan una instrucción en el aviso, sin contar el título?", "5", "Hay cinco reglas, una por oración."),
    ],
    [(LAB + " Estás por empezar un experimento. ¿Qué debes tener puesto mientras trabajas?", "Lentes de seguridad", "Dice While you work, wear goggles.")],
    [
        ("En Inglés de 7.º (OA 10, clase 2): ¿Qué significa «before»?", "Antes de", "Marca lo que ocurre primero."),
        ("¿Qué introduce una condición?", "If", "If significa si en español."),
        ("¿Qué muestra «because»?", "Una causa", "Explica el porqué."),
    ],
    task("Lee este procedimiento: «How to wash a cup. First, put some soap on a sponge. Then wash the cup slowly. While the water runs, rinse the soap. If the cup is still greasy, wash it again. Finally, dry it with a clean cloth.» (soap = jabón, sponge = esponja, rinse = enjuagar, greasy = grasosa, cloth = paño). Numera los pasos en tu hoja y subraya los conectores. Escribe qué haces si la taza sigue grasosa.", "1. First, put soap on the sponge. 2. Then wash. 3. While the water runs, rinse. 4. If still greasy, wash again. 5. Finally, dry. Si sigue grasosa, la lavo otra vez.", ["numera los pasos en orden", "subraya los conectores", "responde la condición"], ["hoja con pasos numerados", "nota de quien revisó"], ["ignorar la condición con if", "cambiar el orden"], "Reconoce el orden acertado y repasa los conectores de condición y simultaneidad."),
    "Lee en voz alta el aviso del laboratorio y di qué conector usa cada regla.",
    "Escribe un aviso de cinco reglas para un patio de juegos, usando before, while y after.",
)

# ------------------------------------------------------------------ clase 3
lesson(
    OA10, 3, MAT,
    "Aprenderé a examinar el propósito de los avisos publicitarios y a distinguir hechos de opiniones y causas de efectos. Sirve para no dejarme convencer solo por un anuncio.",
    ["Sé que un anuncio busca convencer.", "Sé distinguir hechos de opiniones."],
    [
        "Un aviso publicitario (advertisement o ad) quiere convencer a las personas de comprar algo o de hacer algo. Usa recursos para atraer: signos de exclamación, adjetivos positivos (light, comfortable), superlativos (the best), ofertas (Buy two and get one free) y plazos (Only until Sunday). Estos recursos crean urgencia: si no compras pronto, pierdes la oferta.",
        "Para leer con sentido crítico, separa hechos de opiniones. Un hecho se puede comprobar: Each bottle has 300 ml; Price: $1,500. Una opinión no se puede comprobar: Everyone loves them! o the best in the world. Los anuncios mezclan ambas cosas. También busca la relación causa-efecto que se promete: Run faster with our new shoes sugiere que los zapatos causan que corras más rápido, aunque eso podría no ser cierto.",
        "Compara dos anuncios: el que da datos medibles, como mililitros y precio, ayuda más a decidir. El que solo usa palabras fuertes y exclamaciones aporta menos información. Antes de comprar, pregúntate: ¿qué dato concreto me dan?, ¿qué opinión hay?, ¿qué me promete? y ¿qué no dicen?",
    ],
    [("advertisement / ad", "aviso publicitario"), ("offer", "oferta"), ("free", "gratis"), ("persuade", "convencer"), ("fact / opinion", "hecho / opinión"), ("only until", "solo hasta")],
    [
        ("Propósito del anuncio", SHOES + " ¿Cuál es el propósito?", ["Hay oferta y exclamaciones.", "Pide comprar antes del domingo.", "Quiere convencer de comprar las zapatillas."], "Convencer de comprar las zapatillas"),
        ("Hecho u opinión", SHOES + " «Everyone loves them» ¿es un hecho o una opinión?", ["No se puede comprobar que todos las amen.", "Es lo que dice el anuncio.", "Es una opinión."], "Una opinión"),
    ],
    [
        ("Creer que todo lo que dice un anuncio es un hecho.", "Se mezclan hechos y opiniones.", "Pregunta qué se puede comprobar."),
        ("No ver el plazo de la oferta.", "Se decide sin pensar por la urgencia.", "Lee los plazos con calma."),
    ],
    [
        (SHOES + " ¿Cuál es el propósito? a) convencer de comprar b) enseñar a correr", "a) convencer de comprar", "Tiene oferta y plazo."),
        (SHOES + " ¿Hasta cuándo dura la oferta?", "Hasta el domingo", "Dice Only until Sunday."),
        (SHOES + " ¿Qué regalan si compras dos pares?", "Una polera", "Dice get one T-shirt free."),
    ],
    [
        (SHOES + " ¿«Everyone loves them!» es un hecho o una opinión? a) una opinión b) un hecho", "a) una opinión", "No se puede comprobar."),
        (SHOES + " ¿«Buy two pairs and get one T-shirt free» es un hecho o una opinión? a) un hecho b) una opinión", "a) un hecho", "Es una oferta concreta que se puede comprobar."),
        (JUICE + " ¿Cuántos mililitros tiene cada botella?", "300", "Dice 300 ml."),
    ],
    [
        (SHOES + " ¿Qué anuncio da más datos medibles: el de las zapatillas o el del jugo? " + JUICE, "El del jugo", "Da mililitros, precio y composición."),
        arith(JUICE + " Si compras 3 botellas de Sunny Juice, ¿cuántos pesos pagas?", "3*1500", "Se multiplica el precio por la cantidad.", " pesos"),
        (SHOES + " «Run faster with our new Wave shoes». ¿Qué efecto promete? a) correr más rápido b) dormir mejor", "a) correr más rápido", "Faster significa más rápido."),
    ],
    [
        ("Un anuncio dice «Best in the world». ¿Se puede comprobar? Responde sí o no.", "No", "Es una opinión exagerada."),
        ("«Only until Sunday» ¿para qué sirve en un anuncio? a) crea urgencia para comprar b) da una receta", "a) crea urgencia para comprar", "Un plazo apura a decidir."),
    ],
    [
        (SHOES + " ¿Cuántos signos de exclamación tiene el anuncio?", "3", "Aparecen en Super Sneakers!, free! y loves them!."),
        arith("Un local ofrece 2 jugos de $1.500 y el tercero gratis. ¿Cuánto pagas por 3 jugos?", "2*1500", "Pagas solo dos jugos, porque el tercero es gratis.", " pesos"),
    ],
    [(JUICE + " Quieres comprar jugo y comparar dos marcas. ¿Qué información de este anuncio es más útil? a) mililitros y precio b) el color de la botella", "a) mililitros y precio", "Son datos medibles que permiten comparar.")],
    [
        ("En Inglés de 7.º (OA 10, clase 3): ¿Qué quiere lograr un aviso publicitario?", "Convencer de comprar o hacer algo", "Ese es su propósito."),
        ("¿Una opinión se puede comprobar?", "No", "Es lo que alguien piensa."),
        ("¿Qué recurso crea urgencia?", "El plazo de la oferta", "Only until... apura a decidir."),
    ],
    task("Lee este anuncio: «Fantastic Backpacks! Strong, light and beautiful. Only $12,000 until Friday! Everyone needs one!» (backpacks = mochilas, strong = resistentes). Escribe el propósito, un hecho, una opinión y un recurso que crea urgencia.", "Propósito: convencer de comprar mochilas. Hecho: cuestan $12.000 hasta el viernes. Opinión: Everyone needs one. Recurso: Only until Friday.", ["indica el propósito", "separa un hecho y una opinión", "señala el recurso de urgencia"], ["hoja con cuatro respuestas", "nota de quien revisó"], ["tomar una opinión como hecho", "no ver el plazo"], "Reconoce lo que acertó y repasa qué se puede comprobar en el anuncio."),
    "Observa un anuncio de revista o televisión y di un hecho, una opinión y qué quiere lograr.",
    "Escribe un anuncio de cuatro frases en inglés para un cuaderno, con un hecho, una opinión y una oferta.",
)

# ------------------------------------------------------------------ clase 4
lesson(
    OA10, 4, MAT,
    "Aprenderé a comparar información de un mismo tema en distintos formatos: correo, página web, afiche, biografía y gráfico. Sirve para verificar datos y decidir qué fuente es más completa.",
    ["Sé reconocer el formato de un texto.", "Sé ubicar información explícita."],
    [
        "Un mismo tema puede aparecer en varios formatos. El correo de la profesora informa con frases completas. La página web entrega datos ordenados: fecha, hora, lugar. El afiche usa letras grandes y poco texto. Cada formato tiene fortalezas: el correo explica, la página web detalla y el afiche llama la atención. Comparar te permite completar la información y detectar diferencias.",
        "Para comparar, haz una tabla con los datos clave: fecha, hora, lugar, precio y actividades. En la feria del libro, el correo dice que termina a las 14:00 y la página web dice que termina a las 15:00. Cuando dos fuentes no coinciden, no elijas al azar: pregunta a la organizadora o busca la información más reciente. También conviene ver qué formato no da cierto dato, como el afiche, que no dice la hora.",
        "Otros formatos entregan datos distintos. Una biografía (biography) cuenta la vida de una persona con fechas y logros, en orden: nació en 1889, ganó un premio en 1945. Un gráfico muestra cantidades que puedes comparar. Combinar todas las fuentes te da una imagen más completa y confiable.",
    ],
    [("compare", "comparar"), ("source", "fuente: de dónde viene la información"), ("email", "correo electrónico"), ("web page", "página web"), ("poster", "afiche"), ("biography", "biografía")],
    [
        ("Comparar dos fuentes", MAIL + " " + WEB + " ¿A qué hora termina la feria según cada fuente?", ["Miro el correo: from 10:00 to 14:00.", "Miro la web: 10:00 to 15:00.", "Hay una diferencia de una hora."], "Según el correo, a las 14:00; según la web, a las 15:00"),
        ("Dato que falta", POSTER + " ¿Qué dato importante no da el afiche?", ["Leo el afiche: viernes, gimnasio, gratis.", "No hay hora.", "La hora no aparece."], "La hora"),
    ],
    [
        ("Creer la primera fuente sin comparar.", "Se pierden diferencias importantes.", "Compara en una tabla los datos clave."),
        ("Elegir al azar cuando dos fuentes no coinciden.", "Se arriesga a llegar a una hora equivocada.", "Pregunta a quien organiza."),
    ],
    [
        (MAIL + " ¿Dónde es la feria?", "En el gimnasio", "Dice in the gym."),
        (WEB + " ¿A qué hora es la charla del autor?", "A las 11:00", "Dice author talk at 11:00."),
        (POSTER + " ¿Cuánto cuesta la entrada?", "Es gratis", "El afiche dice Free! al final."),
    ],
    [
        (MAIL + " " + WEB + " ¿Qué dato difiere entre el correo y la página web? a) la hora de término b) el día", "a) la hora de término", "El correo dice 14:00 y la web 15:00."),
        (MAIL + " " + WEB + " ¿Qué formato da más detalles de actividades? a) la página web b) el afiche", "a) la página web", "Es la única que menciona la charla de un autor."),
        (MAIL + " ¿Qué pide la profesora que lleven los estudiantes?", "Una bolsa", "Dice Please bring a bag."),
    ],
    [
        arith(MAIL + " " + WEB + " ¿Cuántas horas más dura la feria según la web que según el correo?", "(15-10)-(14-10)", "Según la web dura 5 horas y según el correo 4.", " hora"),
        (POSTER + " ¿Qué formato de los tres no menciona la hora? a) el afiche b) la página web", "a) el afiche", "El afiche solo trae día, lugar y entrada."),
        (BIO + " ¿Qué premio ganó Gabriela Mistral?", "El Premio Nobel de Literatura", "Dice She won the Nobel Prize in Literature."),
    ],
    [
        ("Las dos horas de término de la feria no coinciden. ¿Qué haces? a) pregunto a la organizadora b) elijo al azar", "a) pregunto a la organizadora", "Así confirmo el dato correcto."),
        (BIO + " ¿Es un texto de hechos o de opiniones?", "De hechos", "Entrega fechas y logros comprobables."),
    ],
    [
        arith(BIO + " Restando años, ¿cuántos años pasaron entre su nacimiento (1889) y el premio (1945)?", "1945-1889", "Se resta el año de nacimiento al año del premio.", " años"),
        ("Gráfico de barras descrito: libros prestados en la biblioteca. Lunes 30, martes 45, miércoles 25. Pie del gráfico: «Tuesday had the most loans.» (loans = préstamos). ¿Coincide el pie con las barras? Responde sí o no.", "Sí", "El martes tiene la barra más alta, 45, y el pie dice que tuvo más préstamos."),
    ],
    [("Ves el afiche de la feria del libro y quieres saber la hora. ¿Dónde la buscas? a) en el correo o en la página web b) en el afiche", "a) en el correo o en la página web", "El afiche no trae la hora.")],
    [
        ("¿Para qué sirve comparar fuentes?", "Para completar y verificar la información", "Así detecto las diferencias entre fuentes."),
        ("En Inglés de 7.º (OA 10, clase 4): ¿Qué cuenta una biografía?", "La vida de una persona", "Lo hace con fechas y logros."),
        ("¿Qué haces si dos fuentes no coinciden?", "Pregunto a quien organiza", "Así evito equivocarme de hora."),
    ],
    task("Compara estas dos fuentes sobre una obra de teatro. Correo: «The play is on Saturday at 18:00 in the theater. Tickets cost $3,000.» Página web: «Play: Saturday, 19:00, Theater. Tickets: $3,000. Children under six: free.» (play = obra, theater = teatro, under six = menores de seis). Haz una tabla en tu hoja con día, hora, lugar y precio de cada fuente y escribe qué dato difiere y qué harías.", "Día: sábado en ambas. Hora: 18:00 vs 19:00. Lugar: teatro. Precio: $3.000. Difiere la hora; preguntaría a la organización.", ["tabla con los cuatro datos de cada fuente", "identifica la diferencia", "propone qué hacer"], ["hoja con tabla", "nota de quien revisó"], ["no ver la diferencia de hora", "elegir al azar"], "Reconoce lo que acertó y repasa cómo se organiza una tabla comparativa."),
    "Busca dos textos de un mismo tema, como un horario en un afiche y en una página, y compara un dato.",
    "Escribe un párrafo de cuatro frases en inglés que combine los datos del correo y de la página web de la feria del libro.",
)

# ------------------------------------------------------------------ clase 5
lesson(
    OA10, 5, MAT,
    "Aprenderé a usar las características de un texto (títulos, notas, tablas, horarios, listas) para resolver una tarea. Sirve para encontrar rápido lo que necesito en guías y horarios.",
    ["Sé ubicar información explícita.", "Sé leer una tabla o un horario."],
    [
        "Los textos no literarios tienen características que organizan la información (text features): el título dice el tema, los subtítulos separan partes, las listas muestran elementos uno por uno, las tablas organizan datos en filas y columnas, y las notas (Note) advierten algo importante. Una guía como RECYCLING GUIDE reúne materiales y contenedores; un horario (timetable) reúne horas y paradas.",
        "Para resolver una tarea, decide qué necesitas y busca la característica adecuada. Si quieres saber dónde va una botella plástica, mira la lista de materiales. Si quieres saber a qué hora pasa el próximo bus, mira la fila de la mañana o del fin de semana. Si hay una nota, léela: Note: Clean the containers first es una instrucción adicional que no debes olvidar.",
        "Lee con atención las condiciones. En el horario del bus 12, los días de clases y el fin de semana tienen horas distintas, y en feriados no hay servicio. Responde solo con lo que el texto dice. Practica con tareas concretas: clasificar objetos, planear un viaje o calcular una espera. Así usarás la lectura para actuar.",
    ],
    [("text feature", "característica del texto: título, lista, tabla, nota"), ("guide", "guía"), ("timetable", "horario"), ("note", "nota: aviso importante"), ("bin", "contenedor"), ("weekend", "fin de semana")],
    [
        ("Usar una lista", RECYCLE + " ¿En qué contenedor va el papel?", ["Busco Paper.", "Dice blue bin.", "Va en el azul."], "En el contenedor azul"),
        ("Usar un horario", BUS + " Es lunes y llegas al paradero a las 7:20. ¿A qué hora pasa el siguiente bus?", ["Miro las horas de días de clases: 7:15, 7:45, 8:15.", "7:15 ya pasó.", "El siguiente es a las 7:45."], "A las 7:45"),
    ],
    [
        ("Ignorar la nota del texto.", "Se omite una instrucción importante.", "Lee todas las notas antes de actuar."),
        ("Mezclar el horario de semana con el del fin de semana.", "Se mira la fila equivocada.", "Revisa a qué días corresponde cada fila."),
    ],
    [
        (RECYCLE + " ¿En qué contenedor va el plástico?", "En el amarillo", "Dice Plastic: yellow bin."),
        (RECYCLE + " ¿Dónde van las pilas?", "En una caja especial en la oficina", "Dice special box in the office."),
        (BUS + " ¿A qué horas pasa el bus en el fin de semana?", "A las 9:00 y a las 10:00", "Dice Weekend: 9:00, 10:00."),
    ],
    [
        (RECYCLE + " ¿Qué indica la nota? a) limpiar los envases primero b) comprar más contenedores", "a) limpiar los envases primero", "Dice Clean the containers first."),
        (BUS + " ¿Cuál es el paradero del bus 12?", "Pine Street", "Dice Bus stop: Pine Street."),
        (BUS + " ¿Hay servicio en feriados? Responde sí o no.", "No", "Dice no service on holidays."),
    ],
    [
        (RECYCLE + " Tienes un periódico, una botella plástica y un frasco de mermelada de vidrio. ¿Qué colores de contenedor usas, en ese orden?", "Azul, amarillo y verde", "Papel va en azul, plástico en amarillo y vidrio en verde."),
        (BUS + " Es lunes y llegas al paradero a las 7:20. ¿Cuál es el siguiente bus? a) 7:45 b) 7:15", "a) 7:45", "El de las 7:15 ya pasó."),
        arith(BUS + " ¿Cuántos minutos hay entre el primer y el último bus de un día de clases? Los horarios son 7:15 y 8:15.", "(8-7)*60", "Entre las 7:15 y las 8:15 hay una hora, es decir, 60 minutos.", " minutos"),
    ],
    [
        ("¿Para qué sirve una tabla en un texto? a) para encontrar datos rápido b) para decorar", "a) para encontrar datos rápido", "Organiza la información."),
        (BUS + " Es un feriado y quieres tomar el bus. ¿Qué dice el horario?", "No hay servicio", "Dice no service on holidays."),
    ],
    [
        (BUS + " Es domingo y llegas al paradero a las 9:30. ¿Cuál es el siguiente bus? a) 10:00 b) 9:00", "a) 10:00", "El de las 9:00 ya pasó."),
        (RECYCLE + " ¿Cuántos materiales distintos aparecen en la guía?", "4", "Papel, plástico, vidrio y pilas."),
    ],
    [(RECYCLE + " Quieres reciclar una pila usada. ¿Qué haces? a) la dejo en la caja especial de la oficina b) la pongo en el contenedor verde", "a) la dejo en la caja especial de la oficina", "La guía lo indica.")],
    [
        ("¿Para qué sirve una nota en un texto?", "Para advertir algo importante", "Hay que leerla."),
        ("¿Qué organiza una tabla?", "Datos en filas y columnas", "Facilita encontrar información."),
        ("¿Qué haces con un horario de varios días?", "Reviso la fila que corresponde a mi día", "Cada fila tiene horas distintas."),
    ],
    task("Usa esta guía: «School Library Guide. Opening hours: Monday to Friday, 8:00 to 17:00. Books: you can borrow three books for two weeks. Computers: 30 minutes per student. Note: silence in the reading room.» (borrow = pedir prestado, weeks = semanas, reading room = sala de lectura). Responde en tu hoja: ¿cuántos libros puedes llevar?, ¿por cuánto tiempo?, ¿cuánto puedes usar el computador? y ¿qué dice la nota?", "Tres libros; dos semanas; 30 minutos; silencio en la sala de lectura.", ["responde las cuatro preguntas", "usa la nota", "usa solo datos de la guía"], ["hoja con cuatro respuestas", "nota de quien revisó"], ["olvidar la nota", "confundir los 30 minutos con las dos semanas"], "Reconoce lo que acertó y repasa cómo se busca cada dato en una guía."),
    "Busca un horario de bus o un calendario y responde tres preguntas de tiempo con él.",
    "Crea una mini guía de tres líneas en inglés para tu sala, con una regla, un horario y una nota.",
)
