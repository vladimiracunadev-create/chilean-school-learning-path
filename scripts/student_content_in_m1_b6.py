"""Cuaderno del estudiante, 1.º medio Inglés (oficial): IN1M OA 16, funciones comunicativas en textos escritos.

Clase 1: cantidades, enumerar; lugares, ocupaciones y personas. Clase 2: expresarse con claridad, objetos en detalle,
opiniones propias y ajenas. Clase 3: frecuencia, grado y tiempo; hábitos pasados (used to). Clase 4: acciones que continúan
en el presente y duración (present perfect, for/since). Clase 5: información esencial o adicional (who, which),
unir ideas y voz pasiva. Todos los textos son originales.
"""
from __future__ import annotations

from student_content_in_m1_b import MAT, lesson, mc, task
from student_lessons import arith, ex

OA = "IN1M OA 16"

# ============================================================ clase 1: cantidades, lugares, ocupaciones y personas
lesson(
    OA, 1, MAT,
    "Aprenderé a escribir cantidades y a enumerar, y a describir lugares, ocupaciones y personas con adjetivos precisos. Sirve para dar datos exactos y descripciones claras por escrito.",
    ["Sé contar hasta cien en inglés.", "Conozco adjetivos como big, happy y quiet."],
    [
        "Para expresar cantidades, escribe los números en palabras: 250 es two hundred and fifty, 2,000 es two thousand, 4,000 es four thousand y 1,000,000 es one million. En inglés los miles se separan con coma (1,000) y no con punto. Con un número exacto, thousand no lleva -s (four thousand students); thousands of se usa para una cantidad grande sin número exacto. Para enumerar, usa first, second y third, o both (los dos) y all (todos).",
        "Enough significa suficiente y va antes de un sustantivo (enough money) o después de un adjetivo (tall enough). No enough indica que falta. No money significa que no hay nada de dinero; no time, que no hay nada de tiempo. Estas formas sirven para explicar si algo alcanza o no alcanza.",
        "Para describir lugares y personas, usa adjetivos precisos: busy (con mucha actividad), crowded (con muchas personas y poco espacio), colorful (colorido), cheerful (alegre). Distingue interested (interesado, se dice de una persona) de interesting (interesante, se dice de una cosa o una persona que llama la atención). Las ocupaciones (jobs) se nombran con he is a teacher, she is a pianist o she is a waitress. Para decir que alguien lo hace bien, usa good at + sustantivo o + verbo con -ing (she is good at drawing). Responsible y irresponsible, respectful y disrespectful forman opuestos con ir- y dis-.",
    ],
    [("two thousand / one million", "dos mil / un millón"), ("enough", "suficiente"), ("no money / no time", "nada de dinero / nada de tiempo"), ("crowded", "con mucha gente y poco espacio"), ("interested / interesting", "interesado / interesante"), ("pianist / waitress / teacher", "pianista / camarera / profesor"), ("good at…", "bueno para…"), ("responsible / irresponsible", "responsable / irresponsable")],
    [
        ("Escribir números en palabras", "Escribe en inglés con palabras: 4,000 y 1,000,000.",
         ["4,000 tiene el dígito 4 y mil: four thousand.", "1,000,000 es un millón: one million.", "Thousand no lleva -s con un número exacto."], "four thousand y one million"),
        ("Interested o interesting", "Completa: «The film is very ___. I am ___ in films.»",
         ["La película es una cosa que llama la atención: interesting.", "Yo soy una persona que siente interés: interested.", "La oración queda: The film is very interesting. I am interested in films."], "interesting; interested"),
    ],
    [
        ("Escribir «four thousands students».", "Con un número exacto, thousand no lleva -s.", "Escribe four thousand students."),
        ("Decir «I am interesting in music».", "Se confunde la persona (interested) con la cosa (interesting).", "Una persona está interested in algo."),
    ],
    [
        mc("El número 2,000 se escribe en palabras", "two thousand", ["two thousands", "twenty thousand"], "Con número exacto, thousand no lleva -s."),
        mc("El número 1,000,000 se escribe", "one million", ["one thousand", "ten thousand"], "Un millón es one million."),
        mc("«Enough money» significa", "suficiente dinero", ["dinero de más", "ningún dinero"], "Enough es suficiente."),
    ],
    [
        mc("Hay 30 estudiantes y 30 sillas. Completa: «We have ___ chairs for everybody.»", "enough", ["no", "too"], "Hay una silla para cada estudiante."),
        mc("Hay 20 estudiantes y 5 sillas. Completa: «There are not ___ chairs.»", "enough", ["much", "no"], "Faltan sillas, así que no alcanzan."),
        mc("Mateo tiene 0 pesos. Completa: «Mateo can't buy a snack because he has ___ money.»", "no", ["enough", "many"], "No tiene nada de dinero."),
    ],
    [
        mc("El mercado está lleno de gente y casi no hay espacio para caminar. Elige el adjetivo más preciso:", "crowded", ["quiet", "cheerful"], "Crowded describe mucha gente y poco espacio."),
        mc("Completa: «I am ___ in astronomy, and the book is very ___.»", "interested ... interesting", ["interesting ... interested", "interested ... interested"], "La persona está interested y el libro es interesting."),
        mc("Una persona que toca el piano como profesión es", "a pianist", ["a waitress", "a teacher"], "Pianist es pianista."),
    ],
    [
        mc("Camila siempre devuelve los libros a tiempo y cuida sus cosas. ¿Qué adjetivo la describe?", "responsible", ["irresponsible", "disrespectful"], "Cuidar y devolver a tiempo muestra responsabilidad."),
        mc("¿Cuál frase está bien escrita?", "Four thousand students", ["Four thousands students", "Four thousand of students"], "Thousand no lleva -s y no se usa of con un número exacto."),
    ],
    [
        mc("¿Cuál oración usa bien good at?", "She is good at drawing", ["She is good in drawing", "She is good at draw"], "Good at va seguido de sustantivo o verbo con -ing."),
        ex("Un estadio tiene 4,000 asientos y 2,500 están ocupados. Escribe en palabras en inglés cuántos asientos quedan libres.", "One thousand five hundred", "4,000 menos 2,500 son 1,500 asientos."),
    ],
    [mc("Escribes la reseña de una cafetería para el blog del curso. Datos: hay 40 mesas, todas ocupadas, y hay personas esperando afuera. ¿Qué oración la describe mejor?", "The café is very crowded", ["The café is quiet", "The café is empty"], "Mesas ocupadas y gente esperando indican mucha gente.")],
    [
        mc("¿Cómo se escribe «suficiente» en inglés?", "Enough", ["Never"], "Enough se escribe con g-h al final."),
        mc("¿Cuál de estos adjetivos describe un lugar con muchas personas?", "Crowded", ["Silent"], "Crowded es lleno de gente."),
        ("Escribe en inglés con palabras el número 250.", "Two hundred and fifty", "250 es 200 más 50."),
    ],
    task("Datos de ejemplo del Mercado del Puerto: 250 puestos; 4,000 visitantes el sábado; una camarera y una pianista trabajan en el café; las frutas son de muchos colores; no hay más espacio para sentarse. Escribe cuatro oraciones en inglés: (1) una con un número en palabras, (2) una con un adjetivo para el lugar, (3) una con una ocupación, (4) una con enough o no. (puesto = stall; visitantes = visitors; sentarse = sit)",
         "(1) There are two hundred and fifty stalls. (2) The market is crowded and colorful. (3) A pianist plays at the café. (4) There is no space to sit.",
         ["escribe el número en palabras", "usa un adjetivo preciso para el lugar", "nombra una ocupación", "usa enough o no correctamente"],
         ["cuatro oraciones numeradas en la hoja"],
         ["escribir 250 con cifras", "usar interesting en vez de interested"],
         "Pide que subraye cada función (cantidad, adjetivo, ocupación y suficiencia) en sus oraciones."),
    "Copia los ocho términos y escribe una oración con cada uno.",
    "Escribe en inglés cuatro oraciones sobre tu barrio con un número en palabras, un adjetivo y una ocupación.",
)

# ============================================================ clase 2: claridad, objetos en detalle y opiniones
lesson(
    OA, 2, MAT,
    "Aprenderé a usar sinónimos y palabras compuestas, a ordenar los adjetivos para describir un objeto y a expresar mi opinión o la de otros. Sirve para escribir con precisión y citar fuentes.",
    ["Sé usar adjetivos como old, big y red.", "Conozco I think y because."],
    [
        "Para expresarte con claridad, usa palabras de uso común, sinónimos y palabras compuestas (compound words). Una palabra compuesta junta dos palabras: part-time job (trabajo de media jornada), notebook, classroom, sunglasses y chopstick (palillo para comer). Las colocaciones (collocations) son combinaciones habituales: apply for a job (postular a un trabajo), take a photo, do homework. Si no sabes cuál usar, busca la combinación habitual.",
        "Para describir un objeto en detalle, los adjetivos van antes del sustantivo en este orden: opinión, tamaño, edad, color, material. Por eso se dice a beautiful big old brown wooden table y no a wooden old big table. Un ejemplo: it's an old wooden musical instrument. No se usa coma entre adjetivos de distinta categoría.",
        "Para dar una opinión propia, usa In my opinion, … o I think… Para citar la opinión o el dato de otra persona o fuente, usa according to: According to my teacher, the exam is on Monday. No se dice according to me; se dice in my opinion. Citar una fuente muestra que el dato no es solo tuyo.",
    ],
    [("compound word", "palabra compuesta"), ("part-time job", "trabajo de media jornada"), ("apply for a job", "postular a un trabajo"), ("chopstick", "palillo para comer"), ("In my opinion", "en mi opinión"), ("according to", "según (una fuente)"), ("adjective order", "orden de los adjetivos: opinión, tamaño, edad, color, material")],
    [
        ("Ordenar los adjetivos", "Ordena para describir un objeto: wooden / old / a / musical instrument.",
         ["Los adjetivos son old (edad) y wooden (material).", "Primero va la edad y luego el material.", "La frase es: an old wooden musical instrument (con an por la vocal)."], "An old wooden musical instrument"),
        ("Citar una fuente", "Completa: «___ the website, the museum opens at 10:00.»",
         ["El dato viene de un sitio web, no de mi opinión.", "Para citar una fuente se usa according to.", "La oración es: According to the website, the museum opens at 10:00."], "According to"),
    ],
    [
        ("Decir «according to me».", "Se usa según solo para otras personas o fuentes.", "Para ti, usa in my opinion."),
        ("Escribir «a wooden old big table».", "Se ordenan mal los adjetivos.", "Tamaño, edad y material: a big old wooden table."),
    ],
    [
        mc("Un part-time job es", "un trabajo de pocas horas", ["un trabajo que dura toda la noche", "un trabajo sin pago"], "Part-time es de media jornada."),
        mc("According to se usa para", "citar la opinión o el dato de otra persona o fuente", ["decir mi propia opinión", "contar un chiste"], "Indica de dónde viene el dato."),
        mc("Un chopstick es", "un palillo para comer", ["un palo para caminar", "una olla"], "Es una palabra compuesta de chop y stick."),
    ],
    [
        mc("Completa: «She has a ___ job at the café, only on weekends.»", "part-time", ["full-time", "free-time"], "Trabaja solo los fines de semana."),
        mc("¿Cuál frase tiene el orden de adjetivos correcto?", "a small red ball", ["a red small ball", "a ball small red"], "El tamaño va antes del color."),
        mc("Completa: «___ my teacher, the exam is on Monday.»", "According to", ["In my opinion", "I think"], "El dato viene de la profesora."),
    ],
    [
        mc("Elige la descripción correcta de una mesa.", "a big old wooden table", ["a wooden old big table", "an old big wooden table"], "El orden es tamaño, edad y material."),
        mc("Completa: «She wants to ___ for a job at the library.»", "apply", ["ask", "need"], "Apply for a job es una colocación habitual."),
        mc("¿Cuál palabra es el sinónimo más cercano de enormous? (enormous = enorme)", "huge", ["tiny", "quiet"], "Huge y enormous significan muy grande."),
    ],
    [
        mc("Una estudiante escribe «According to me, the film is boring». ¿Qué corrección haces?", "In my opinion, the film is boring", ["According to the film, I am boring", "Nothing, it is correct"], "Para opiniones propias se usa in my opinion."),
        mc("¿Cuál oración da el dato de otra fuente?", "According to the museum website, it opens at 9:00", ["In my opinion, the museum is great", "I think museums are quiet"], "Cita una fuente."),
    ],
    [
        mc("Datos: el reloj es nuevo, pequeño, plateado y de metal. ¿Cuál es la descripción correcta?", "a small new silver metal watch", ["a metal silver new small watch", "a new small metal silver watch"], "Tamaño, edad, color y material."),
        mc("¿Cuál frase pone la opinión en el lugar correcto?", "a beautiful old wooden box", ["an old beautiful wooden box", "a wooden beautiful old box"], "La opinión va antes que la edad y el material."),
    ],
    [mc("Preparas un aviso para la venta del curso con un artículo: la lámpara es grande, nueva, blanca y de plástico. ¿Qué frase escribes?", "a big new white plastic lamp", ["a plastic white new big lamp", "a white big new plastic lamp"], "El orden es tamaño, edad, color y material.")],
    [
        mc("¿Qué va primero en el orden de los adjetivos?", "La opinión", ["El material"], "Opinión, tamaño, edad, color, material."),
        mc("¿Qué es una palabra compuesta?", "Una palabra formada por dos palabras", ["Una palabra con tres significados"], "Notebook y classroom son compuestas."),
        ("Escribe en inglés la expresión «postular a un trabajo» (tres palabras).", "Apply for a job", "Apply for es la colocación habitual."),
    ],
    task("Escribe en tu hoja tres oraciones en inglés: (1) describe este objeto con cuatro adjetivos en orden: es una caja (box) hermosa, grande, antigua y de madera; (2) da una opinión tuya con In my opinion sobre ese objeto; (3) cita un dato con According to: «el museo dice que la caja tiene mucho tiempo» (the museum says the box is very old).",
         "(1) It is a beautiful big old wooden box. (2) In my opinion, it is the best object in the room. (3) According to the museum, the box is very old.",
         ["los adjetivos están en el orden correcto", "usa In my opinion para la opinión propia", "usa According to para la fuente"],
         ["tres oraciones numeradas en la hoja"],
         ["escribir according to me", "poner madera antes de tamaño"],
         "Pide que cambie el objeto por otro y vuelva a ordenar los adjetivos."),
    "Copia las cuatro categorías de adjetivos en orden y escribe un ejemplo de cada una.",
    "Describe en inglés un objeto de tu casa con cuatro adjetivos en orden y una opinión con In my opinion.",
)

# ============================================================ clase 3: frecuencia, grado, tiempo y hábitos pasados
lesson(
    OA, 3, MAT,
    "Aprenderé a decir con qué frecuencia, en qué grado y cuándo ocurre una acción, y a contar hábitos del pasado con used to. Sirve para escribir sobre rutinas y cambios.",
    ["Sé usar el presente simple y el pasado simple.", "Conozco always, never y yesterday."],
    [
        "La frecuencia (frequency) dice cuántas veces ocurre una acción. Los adverbios always, usually, often, sometimes y never van antes del verbo principal, pero después de to be: I usually go by bus; She is always late. También se puede decir una frecuencia exacta: once a month (una vez al mes), twice a week (dos veces a la semana) y every day. El grado (degree) dice cuánto: very, quite (bastante), a bit (un poco), really: She is quite shy.",
        "Para el tiempo, ago se usa con el pasado simple y significa hace: I studied French five years ago. Since indica el punto donde empezó algo y se usa con el presente perfecto: he has worked here since 2010 (lo verás en la próxima clase). Last year, last week y yesterday también ubican la acción.",
        "Para hablar de hábitos del pasado que ya no ocurren, usa used to + verbo: I used to work at the coffee shop, but now I work at a school. Negativo: I didn't use to like fish. Pregunta: Did you use to walk to school? Con used to no se indica cuántas veces ni hasta cuándo; solo que antes era costumbre y ya no.",
    ],
    [("always / usually / often / sometimes / never", "siempre / normalmente / a menudo / a veces / nunca"), ("once a month / twice a week", "una vez al mes / dos veces por semana"), ("quite", "bastante"), ("ago", "hace"), ("used to", "solía; antes (hábito pasado)"), ("didn't use to", "antes no solía"), ("habit", "hábito")],
    [
        ("Ubicar el adverbio de frecuencia", "Ubica always en «She is late».",
         ["El verbo es to be: is.", "Con to be, el adverbio va después del verbo.", "La oración queda: She is always late."], "She is always late"),
        ("Contar un hábito pasado", "Escribe con used to: «Antes caminaba al colegio, pero ahora tomo la micro.» (walk = caminar; take the bus = tomar la micro)",
         ["Es un hábito del pasado que ya no ocurre.", "Uso used to + walk.", "Y marco el cambio con but now."], "I used to walk to school, but now I take the bus"),
    ],
    [
        ("Escribir «She always is late».", "Con to be, el adverbio de frecuencia va después del verbo.", "Escribe She is always late."),
        ("Escribir «I didn't used to like fish».", "Después de didn't, used se escribe use.", "Escribe I didn't use to like fish."),
    ],
    [
        mc("Once a month significa", "una vez al mes", ["cada mes dos veces", "todos los días"], "Once es una vez."),
        mc("Used to se usa para", "hábitos del pasado que ya no ocurren", ["acciones de mañana", "órdenes"], "Cuenta lo que se hacía antes."),
        mc("Quite shy significa", "bastante tímida", ["nada tímida", "tímida para siempre"], "Quite es bastante."),
    ],
    [
        mc("¿Cuál oración ubica bien el adverbio?", "She is always late", ["She always is late", "Always she is late"], "Después de to be."),
        mc("Completa: «I studied French five years ___.»", "ago", ["since", "for"], "Ago se usa con el pasado simple."),
        mc("Completa: «She is ___ shy, but not extremely shy.»", "quite", ["never", "twice"], "Quite expresa un grado medio."),
    ],
    [
        mc("Completa: «When I was little, I ___ play with toy cars. Now I play video games.»", "used to", ["use to", "am used to"], "Describe un hábito pasado."),
        mc("¿Cuál oración negativa es correcta?", "He didn't use to like fish", ["He didn't used to like fish", "He not used to like fish"], "Después de didn't va la forma use."),
        mc("Completa: «We visited the museum two weeks ___.»", "ago", ["since", "always"], "Two weeks ago es hace dos semanas."),
    ],
    [
        mc("«I used to work at the coffee shop, but now I work at a school.» ¿Dónde trabaja hoy la persona?", "En un colegio", ["En la cafetería", "En ninguna parte"], "Used to indica que ya no trabaja en la cafetería."),
        mc("¿Cuál oración muestra un hábito pasado que terminó?", "I used to swim on Saturdays, but now I play tennis", ["I swim on Saturdays", "I will swim on Saturdays"], "Marca el cambio con used to y but now."),
    ],
    [
        arith("Mía hace yoga dos veces por semana y nada una vez por semana. ¿Cuántas sesiones hace en 3 semanas?", "(2+1)*3", "Se suman las sesiones de una semana y se multiplican por 3.", " sesiones"),
        arith("Un técnico visita la escuela twice a week. ¿Cuántas visitas hace en 4 semanas?", "2*4", "Dos visitas por 4 semanas.", " visitas"),
    ],
    [mc("Escribes un mensaje a un amigo por correspondencia. ¿Cuál frase cuenta bien un cambio?", "I used to live in a small town, but now I live in a city", ["I used to live in a small town and I live there now", "I use to live in a city"], "Contrasta el hábito pasado con el presente.")],
    [
        mc("¿Qué adverbio de frecuencia significa «nunca»?", "Never", ["Often"], "Never es nunca."),
        mc("Used to + ¿qué forma del verbo?", "La forma base, como walk", ["La forma con -ing"], "Used to walk, used to play."),
        ("Escribe en inglés «una vez al mes» (cuatro palabras).", "Once a month", "Once significa una vez."),
    ],
    task("Escribe tres oraciones en inglés: (1) una rutina con usually y once a week, (2) un hábito de cuando eras pequeño con used to y un contraste con but now, (3) una acción de hace unos años con ago. Datos de ejemplo: go to the library; play in the park; learn to swim. (rutina = routine; park = parque; learn = aprender)",
         "(1) I usually go to the library once a week. (2) I used to play in the park, but now I study. (3) I learned to swim four years ago.",
         ["usa un adverbio de frecuencia en el lugar correcto", "usa used to con un contraste", "usa ago con el pasado simple"],
         ["tres oraciones numeradas en la hoja"],
         ["escribir didn't used to", "usar ago con el presente perfecto"],
         "Pide que subraye en cada oración la palabra que indica frecuencia, hábito y tiempo."),
    "Copia las cinco palabras de frecuencia en orden de más a menos y escribe una oración con cada una.",
    "Escribe en inglés tres cosas que hacías de pequeño y que ya no haces, con used to.",
)

# ============================================================ clase 4: acciones que continúan y duración (con brecha de información)
CQ = "«Card A (questions): (1) How long has Nico played the guitar? (2) How long have you and Ana been friends? (3) How long has the shop been open?»"
CR = "«Card B (answers): (1) Nico started in March and still plays. (2) We became friends two years ago and we still are. (3) The shop opened last Monday and it is still open.»"
GC = "(guitar = guitarra; friends = amigos; shop = tienda; started = empezó; opened = abrió; still = todavía)"

lesson(
    OA, 4, MAT,
    "Aprenderé a escribir acciones que empezaron en el pasado y continúan hoy, con el presente perfecto, y a preguntar y responder cuánto tiempo con for y since. Sirve para contar cuánto tiempo llevo haciendo algo.",
    ["Sé usar el pasado simple y los participios have, been y lived.", "Conozco las preguntas con how y how many."],
    [
        "El presente perfecto (present perfect) se forma con have o has + participio pasado. Se usa para una acción que empezó en el pasado y continúa hoy: I have saved money to buy a bike. She has lived here for two years. Participios útiles: be-been, live-lived, save-saved, work-worked, have-had, see-seen, write-written, do-done, make-made. Con he, she e it se usa has; con I, you, we y they, have.",
        "Para decir cuánto tiempo, hay dos palabras. For va con una duración (for two years, for three months, for a week). Since va con el momento en que empezó (since March, since Monday, since 2010). Las dos se usan con el presente perfecto, no con el pasado simple. La pregunta es How long have you…? o How long has she…? Respuesta: We have been friends for two years.",
        "Cuidado con el pasado simple: I lived in Temuco for three years significa que ya no vivo ahí. I have lived in Temuco for three years significa que todavía vivo ahí. En una actividad con tarjetas, una persona tiene las preguntas (Card A) y otra las respuestas (Card B): une cada pregunta con su dato y escribe la respuesta completa.",
    ],
    [("present perfect", "presente perfecto: have/has + participio"), ("for", "durante: una duración"), ("since", "desde: un punto de inicio"), ("How long…?", "¿cuánto tiempo…?"), ("still", "todavía"), ("participle", "participio pasado"), ("card", "tarjeta")],
    [
        ("Elegir for o since", "Completa: «She has worked here ___ five years» y «She has worked here ___ Monday».",
         ["Five years es una duración: se usa for.", "Monday es el momento en que empezó: se usa since.", "Las dos oraciones son: ...for five years y ...since Monday."], "for; since"),
        ("Escribir con el presente perfecto", "Escribe: «Yo / ahorrar dinero / tres meses» (save money / three months).",
         ["Sujeto I: uso have.", "El participio de save es saved.", "Tres meses es una duración: for three months."], "I have saved money for three months"),
    ],
    [
        ("Escribir «She has lived here since five years».", "Since no se usa con una duración.", "Usa for con duraciones: for five years."),
        ("Escribir «I have wrote a letter».", "El participio de write es written.", "Memoriza los participios irregulares."),
    ],
    [
        mc("El presente perfecto se forma con", "have o has y un participio pasado", ["was o were y el infinitivo", "will y el infinitivo"], "Have/has + participio."),
        mc("For se usa con", "una duración, como two years", ["un momento de inicio, como Monday", "un lugar"], "For dice cuánto tiempo."),
        mc("Since se usa con", "un punto de inicio, como Monday", ["una duración, como two years", "una persona"], "Since dice desde cuándo."),
    ],
    [
        mc("Completa: «She ___ lived here for two years.»", "has", ["have", "is"], "She va con has."),
        mc("Completa: «I ___ saved money to buy a bike.»", "have", ["has", "had to"], "I va con have."),
        mc("Completa: «They ___ not seen the film.»", "have", ["has", "are"], "They va con have."),
    ],
    [
        mc(f"Tarjetas: {CQ} {CR} {GC} ¿Qué oración escribes como respuesta a la pregunta (1)?", "Nico has played the guitar since March", ["Nico played the guitar since March", "Nico has played the guitar for March"], "March es un punto de inicio y la acción continúa."),
        mc(f"Tarjetas: {CQ} {CR} Completa con la respuesta (2): «We have been friends ___ two years.»", "for", ["since", "ago"], "Two years es una duración."),
        mc(f"Tarjetas: {CQ} {CR} Completa con la respuesta (3): «The shop has been open ___ last Monday.»", "since", ["for", "ago"], "Last Monday es el inicio."),
    ],
    [
        mc("¿Cuál oración está mal escrita?", "She has lived here since five years", ["She has lived here for five years", "She has lived here since 2015"], "Since se usa con un inicio, no con una duración."),
        mc("¿Cuál es el participio correcto de write?", "written", ["wrote", "writed"], "El participio de write es written."),
    ],
    [
        mc("¿Qué respuesta calza con «How long have you been friends?»", "For two years", ["Since two years", "Two years ago"], "For se usa con una duración."),
        mc("¿Qué oración significa que la persona todavía vive en Temuco?", "I have lived in Temuco for three years", ["I lived in Temuco for three years", "I used to live in Temuco"], "El presente perfecto conecta con hoy."),
    ],
    [mc(f"En un club de ajedrez, tu compañero tiene la tarjeta con «The club started in April and it has twenty members.» ¿Qué oración escribes para decir desde cuándo funciona?", "The chess club has existed since April", ["The chess club has existed for April", "The chess club existed since April"], "Since indica el inicio y el club todavía funciona.")],
    [
        mc("¿Cuál es la pregunta para saber cuánto tiempo?", "How long have you lived here?", ["How many are you?"], "How long pide una duración."),
        mc("Con he, she o it se usa", "has", ["have"], "Has va con la tercera persona."),
        ("Escribe en inglés la palabra que significa «desde» con el presente perfecto.", "Since", "Since se usa con un punto de inicio."),
    ],
    task("Con otra persona, usen estas tarjetas: Card A: «How long has Nico played the guitar?» Card B: «Nico started in March and still plays.» En tu hoja escribe: (1) la respuesta con since, (2) una oración sobre ti: llevas dos años estudiando inglés (for), (3) una pregunta con How long para tu compañero.",
         "(1) Nico has played the guitar since March. (2) I have studied English for two years. (3) How long have you studied English?",
         ["usa has y have en el lugar correcto", "usa for con una duración y since con un inicio", "la pregunta empieza con How long"],
         ["tres líneas escritas en la hoja"],
         ["usar el pasado simple en vez del presente perfecto", "escribir since two years"],
         "Pide que explique por qué eligió for o since en cada oración."),
    "Copia los nueve participios de la lección y escribe una oración con cada uno.",
    "Escribe en inglés cuánto tiempo llevas haciendo tres actividades, con for o since.",
)

# ============================================================ clase 5: información adicional, unir ideas y voz pasiva
lesson(
    OA, 5, MAT,
    "Aprenderé a agregar información esencial o adicional con who y which, a unir ideas con although, so that, both… and y and lastly, y a escribir acciones donde el agente no importa con la voz pasiva. Sirve para escribir oraciones más completas.",
    ["Sé usar conectores como and, but, because y so.", "Conozco el pasado simple y los participios."],
    [
        "Las cláusulas relativas (relative clauses) agregan información. Who se usa para personas y which para cosas. La información esencial identifica de quién o de qué hablas y no lleva comas: Simon is the boy who lives next door. La información adicional agrega un dato y va entre comas: The science book, which I borrowed from the library, is very interesting. Si quitas la información adicional, la oración sigue teniendo sentido.",
        "Para unir ideas: although introduce un contraste (although it's cheap, I'm not sure); so that indica propósito (come early so that we can talk); both… and une dos elementos (both Luis and Tomás are my neighbors); and lastly o and finally cierra una lista de acciones. Elige el conector según la relación entre las ideas.",
        "La voz pasiva (passive voice) se usa cuando no se conoce o no importa quién hace la acción. Se forma con be + participio pasado: The money was found on the floor; Rooms are cleaned daily; Plastic is produced from oil. En presente se usa am, is o are, y en pasado was o were. El foco está en lo que ocurre, no en quién lo hace.",
    ],
    [("who / which", "quien / el cual (personas / cosas)"), ("relative clause", "cláusula relativa"), ("although", "aunque"), ("so that", "para que"), ("both… and…", "tanto… como…"), ("passive voice", "voz pasiva: be + participio"), ("agent", "quien hace la acción")],
    [
        ("Unir con who", "Une las dos oraciones con who: «I have a neighbor. He plays the drums.» (neighbor = vecino; drums = batería)",
         ["La segunda oración habla de una persona: he.", "Reemplazo he por who.", "Queda: I have a neighbor who plays the drums."], "I have a neighbor who plays the drums"),
        ("Pasar a voz pasiva", "Reescribe sin decir quién: «Someone cleans the rooms every day.»",
         ["El agente (someone) no importa.", "Pongo rooms como sujeto con are y el participio cleaned.", "Queda: The rooms are cleaned every day."], "The rooms are cleaned every day"),
    ],
    [
        ("Escribir «Simon is the boy which lives next door».", "Which no se usa para personas.", "Usa who para personas."),
        ("Escribir «Rooms is cleaned daily».", "Rooms es plural y pide are.", "Escribe Rooms are cleaned daily."),
    ],
    [
        mc("Who se usa para", "personas", ["cosas", "lugares únicamente"], "Who es para personas."),
        mc("Which se usa para", "cosas", ["personas", "el verbo"], "Which es para cosas."),
        mc("La voz pasiva se forma con", "be y un participio pasado", ["will y el infinitivo", "do y un adjetivo"], "Por ejemplo, was found."),
    ],
    [
        mc("Completa: «Simon is the boy ___ lives next door.»", "who", ["which", "where"], "Es una persona."),
        mc("Completa: «The science book, ___ I borrowed from the library, is very interesting.»", "which", ["who", "what"], "Es una cosa y el dato es adicional."),
        mc("Completa: «Rooms ___ cleaned daily.»", "are", ["is", "was"], "Rooms es plural y la acción es habitual."),
    ],
    [
        mc("Completa: «Come early ___ we can talk.»", "so that", ["although", "both"], "Indica el propósito."),
        mc("Completa: «___ Luis and Tomás are my neighbors.»", "Both", ["Although", "Which"], "Both une dos personas."),
        mc("Completa: «Plastic ___ produced from oil.»", "is", ["are", "were"], "Plastic es singular y es un hecho general."),
    ],
    [
        mc("¿En qué oración se usan correctamente las comas?", "The science book, which I borrowed from the library, is very interesting", ["The science book which, I borrowed from the library is very interesting", "The science book which I borrowed from the library, is very interesting"], "El dato adicional va entre comas."),
        mc("¿Cuál oración está en voz pasiva?", "The money was found on the floor", ["Someone found the money", "I will find the money"], "Was found es be + participio."),
    ],
    [
        mc("Une las ideas: «It's cheap. I'm not sure.»", "Although it's cheap, I'm not sure", ["Although it's cheap, but I'm not sure", "Because it's cheap, I'm not sure"], "Although expresa contraste y no se usa con but."),
        mc("Reescribe sin agente: «Someone cleans the rooms daily».", "The rooms are cleaned daily", ["The rooms cleans daily", "The rooms is cleaned daily"], "Rooms es plural y lleva are."),
    ],
    [mc("En un aviso del hotel del curso de turismo se lee: «Rooms are cleaned daily. Towels are changed every two days.» (towels = toallas; changed = cambiadas) ¿Qué información da y por qué no importa quién lo hace?", "Cuándo se limpia y se cambia; interesa el servicio, no la persona", ["Quién limpia; interesa el nombre de la persona", "Que las habitaciones no se limpian"], "La voz pasiva se usa cuando el agente no importa.")],
    [
        mc("¿En qué oración va entre comas la información adicional?", "The book, which I borrowed, is old", ["The boy who lives next door is my friend"], "Which I borrowed es un dato extra."),
        mc("¿Qué conector expresa propósito?", "So that", ["Although"], "So that dice para qué."),
        ("Escribe en inglés la palabra que significa «tanto… como…» para unir dos elementos: ___ … and.", "Both", "Both … and une dos elementos."),
    ],
    task("Escribe cuatro oraciones en inglés: (1) une con who: «I know a girl. She speaks three languages.»; (2) une con although: «It was raining. We went out.»; (3) reescribe en pasiva: «Someone cleans the classroom every day.»; (4) escribe una oración con both… and… sobre dos compañeros. (languages = idiomas; classroom = sala de clases)",
         "(1) I know a girl who speaks three languages. (2) Although it was raining, we went out. (3) The classroom is cleaned every day. (4) Both Ana and Luis are in my class.",
         ["usa who para personas", "usa although sin but", "forma la pasiva con be y participio", "usa both… and… correctamente"],
         ["cuatro oraciones numeradas en la hoja"],
         ["usar which para personas", "escribir although con but"],
         "Pide que subraye en cada oración la palabra clave (who, although, is cleaned, both... and)."),
    "Copia los siete términos y escribe una oración con cada uno.",
    "Escribe en inglés una oración con who, otra con which, otra con although y otra en voz pasiva sobre tu colegio.",
)
