"""Cuaderno del estudiante, 4.º básico Lenguaje y Comunicación: OA 08 (uso responsable de la biblioteca).

Los catálogos, signaturas y reglas de préstamo son inventados para el ejercicio; cada ejercicio trae todos los datos que necesita.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA8 = "LE04 OA 08"
E = ex
A = arith


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


CAT = ("Catálogo de la biblioteca «Los Aromos»: «El volcán dormido», C-21; «Cómo viven las ballenas», I-30; "
       "«Adivinanzas del campo», P-5; «Mapas de América», M-1; «Aves de Chile», I-14.")
SECC = "En esa biblioteca la letra C es Cuentos, I es Informativos, P es Poesía y M es Mapas."
MATERIALES = "Este cuaderno, lápiz y los catálogos y reglas escritos en los ejercicios. Sin materiales especiales."

# ================================================================ OA 08 · biblioteca
reg(
    OA8, 1, MATERIALES,
    "Aprenderé a decir para qué voy a la biblioteca antes de entrar. Sirve para buscar lo que necesito y no perder el tiempo.",
    ["Sé que una biblioteca tiene libros.", "Sé cuidar un libro."],
    ["La biblioteca es un lugar con libros, revistas, mapas y otros materiales que se leen allí o se llevan prestados. Se puede ir muchas veces durante el año. Cada visita tiene un propósito, que es lo que quieres lograr al ir.",
     "Hay cinco propósitos principales. Encontrar información: buscar un dato que quieres saber. Elegir libros: escoger algo para leer por gusto. Estudiar: repasar lo que aprendiste para una prueba. Trabajar: hacer una tarea o un proyecto, solo o con compañeros. Investigar: responder una pregunta usando varias fuentes.",
     "Pensar el propósito antes de ir te ayuda a decidir qué materiales mirar, cuánto tiempo necesitas y en qué parte sentarte. Quien llega sin propósito suele pasear sin encontrar nada. Un propósito claro cabe en una oración corta."],
    [("biblioteca", "lugar con libros y otros materiales para leer, prestar y estudiar"), ("propósito", "lo que quiero lograr al hacer algo"), ("investigar", "responder una pregunta usando varias fuentes"), ("préstamo", "llevar un libro a casa por unos días y devolverlo")],
    [("Reconocer el propósito", "Ana va a la biblioteca a mirar la portada de cinco cuentos para llevarse uno a casa. ¿Cuál es su propósito?", ["Ana no busca un dato ni estudia.", "Quiere escoger algo para leer.", "Eso es elegir libros."], "Elegir libros"),
     ("Escribir el propósito", "Luis quiere saber cuántos años vive una tortuga. Escribe su propósito en una oración.", ["Quiere un dato puntual.", "Uso «para» y digo qué busca.", "Escribo la oración."], "Voy a la biblioteca para encontrar información sobre cuántos años vive una tortuga.")],
    [("Ir «a ver qué hay» sin saber para qué.", "Sin propósito no se sabe qué materiales sirven.", "Antes de ir, escribe una oración: «Voy para…»."), ("Pensar que la biblioteca sirve solo para sacar cuentos.", "También sirve para estudiar, trabajar e investigar.", "Revisa los cinco propósitos antes de decidir.")],
    ([E("Julia va a leer en silencio sus tablas de multiplicar antes de la prueba. ¿Cuál es su propósito: estudiar o elegir libros?", "Estudiar", "Repasa lo aprendido para una prueba."),
      E("Pedro busca en una enciclopedia cuántos huesos tiene el cuerpo humano. ¿Su propósito es elegir libros o encontrar información?", "Encontrar información", "Busca un dato puntual."),
      E("¿Qué es un propósito: lo que quiero lograr o el nombre de un libro?", "Lo que quiero lograr", "El propósito responde a «¿para qué voy?».")],
     [E("Tomás dice: «Voy a ver qué hay». Rosa dice: «Voy a buscar dos libros de planetas para mi trabajo de ciencias». ¿Quién tiene un propósito claro?", "Rosa", "Dice qué quiere lograr y qué materiales busca."),
      E("¿Cuántos propósitos principales para visitar la biblioteca se explican en esta clase?", "5", "Son encontrar información, elegir libros, estudiar, trabajar e investigar."),
      E("Dos compañeros se sientan en una mesa grande a hacer juntos un afiche para la sala. ¿Es estudiar o trabajar?", "Trabajar", "Hacen un proyecto en equipo, no repasan para una prueba.")],
     [E("Une cada visita con su propósito. 1) Lee dos libros de volcanes para responder «¿Cómo se forma un volcán?». 2) Mira las portadas de cinco cuentos para llevarse uno. Propósitos: investigar, elegir libros.", "1 investigar, 2 elegir libros", "El primero busca responder una pregunta con varias fuentes; el segundo escoge una lectura."),
      E("Mateo necesita saber en qué año nació un escritor. Completa su oración con dos palabras: «Voy a la biblioteca para ____ ____ sobre el año en que nació».", "encontrar información", "Es un dato puntual, así que el propósito es encontrar información."),
      E("Hoy quieres saber cuántas patas tiene una araña. ¿Qué propósito escoges: estudiar, encontrar información o elegir libros?", "Encontrar información", "Buscas un solo dato.")],
     [E("Sofía pasó 30 minutos mirando estantes, sin sacar nada, y dijo: «Entré a ver qué había». ¿Qué le faltó antes de entrar?", "Un propósito claro", "Sin saber para qué iba, no supo qué buscar."),
      E("Pablo entró para estudiar su prueba, pero se puso a escoger cuentos para llevar. ¿Cumplió su propósito de estudiar? Responde sí o no.", "No", "Hizo otra cosa: eligió libros.")],
     [E("Visita A: Luis saca dos libros de astronomía y anota datos para responder «¿Por qué hay estaciones?». Visita B: Rosa repasa sus apuntes de lenguaje en silencio. ¿Qué propósito tiene cada visita?", "A investigar, B estudiar", "A responde una pregunta con libros; B repasa para aprender."),
      E("Nico llegó para estudiar y, al terminar, escogió un cuento para llevar. ¿Cuántos propósitos tuvo en esa visita?", "2", "Estudiar y elegir libros.")]),
    [E("Tu curso irá 40 minutos a la biblioteca. Tu profesora pidió buscar datos para responder «¿Qué comen los cóndores?». ¿Qué propósito tienes: investigar, estudiar o elegir libros?", "Investigar", "Respondes una pregunta con información de los libros.")],
    [E("¿Se puede ir a la biblioteca a estudiar?", "Sí", "Estudiar es uno de los propósitos."),
     E("¿Conviene pensar el propósito antes de entrar?", "Sí", "Así decides qué buscar."),
     E("¿«Encontrar información» es lo mismo que «elegir libros»?", "No", "Uno busca datos; el otro, lecturas por gusto.")],
    ("Elige una de estas situaciones: a) necesitas leer algo entretenido para el fin de semana, b) debes repasar para la prueba de ciencias del viernes, c) quieres saber cómo duermen los murciélagos. Escribe para cada una el propósito de tu visita con una oración que empiece con «Voy a la biblioteca para…».", "a) Voy a la biblioteca para elegir un libro entretenido para el fin de semana.", ["escribe una oración por situación", "usa «para» y dice qué quiere lograr", "nombra el propósito correcto (elegir libros, estudiar, encontrar información)", "no es demasiado larga"], ["tres oraciones escritas"], ["escribir solo «voy a ver qué hay»", "confundir estudiar con investigar"], "Lee tus oraciones a otra persona y pregúntale si entendió para qué irías."),
    "Escribe dos propósitos distintos que podrías tener la próxima vez que vayas a una biblioteca.",
    "Elige un propósito de los cinco y escribe qué materiales usarías y cuánto tiempo necesitarías.")

reg(
    OA8, 2, MATERIALES,
    "Aprenderé a ubicarme en la biblioteca con el catálogo y la signatura. Sirve para encontrar un libro sin recorrer todos los estantes.",
    ["Sé para qué voy a la biblioteca.", "Sé ordenar números de menor a mayor."],
    ["Una biblioteca guarda sus materiales por secciones: cuentos, poesía, libros informativos, mapas, revistas. Cada libro está en un estante, que es una repisa. Los libros de cada estante están en orden, para que se puedan encontrar.",
     "El catálogo es la lista de todos los materiales de la biblioteca. Puede ser un fichero o un computador. Para cada material dice el título, el autor y la signatura. La signatura es un código que va en el lomo del libro. En los ejemplos de esta clase, la letra dice la sección y el número dice el orden dentro de ella.",
     "Para buscar un libro: primero lo buscas en el catálogo por título, autor o tema. Luego anotas su signatura. Después vas a la sección y recorres el estante hasta el código. Los números se ordenan por su valor: 9, 20, 100, y no por la primera cifra."],
    [("catálogo", "lista de todos los materiales de la biblioteca, con su signatura"), ("signatura", "código del lomo que indica dónde está el libro"), ("estante", "repisa donde se guardan los libros en orden"), ("sección", "parte de la biblioteca con un tipo de materiales")],
    [("Buscar en el catálogo", CAT + " " + SECC + " Quieres un libro sobre aves de Chile. ¿Cuál es su signatura y en qué sección está?", ["Busco «aves» en el catálogo: «Aves de Chile».", "Su signatura es I-14.", "La letra I es la sección Informativos."], "I-14, sección Informativos"),
     ("Ordenar signaturas", "En un estante están los libros I-12, I-3 y I-25. ¿En qué orden se ordenan?", ["Todos tienen la letra I.", "Comparo los números por su valor: 3, 12, 25.", "Los pongo de menor a mayor."], "I-3, I-12, I-25")],
    [("Ordenar I-9, I-20 e I-100 como I-100, I-20, I-9 por mirar solo la primera cifra.", "Los números se ordenan por su valor, no por la primera cifra.", "Compara cuánto vale cada número: 9, 20, 100."), ("Buscar un libro de informativos en el estante de cuentos.", "La letra de la signatura indica la sección.", "Mira primero la letra y ve a esa sección.")],
    ([E("¿Qué es el catálogo: la lista de los materiales de la biblioteca o una mesa de lectura?", "La lista de los materiales", "Dice qué hay y dónde está cada material."),
      E(SECC + " Un libro tiene la signatura C-7. ¿En qué sección está?", "Cuentos", "La letra C significa Cuentos."),
      E("¿Qué es un estante: una repisa donde se guardan los libros o un carné de socio?", "Una repisa donde se guardan los libros", "Es el lugar físico donde está cada libro.")],
     [E(CAT + " " + SECC + " Buscas un atlas de mapas. ¿En qué sección buscarías?", "Mapas", "«Mapas de América» tiene la signatura M-1."),
      E("Un estante tiene los libros I-3, I-9, I-12 e I-25 en orden. ¿Cuál va justo después de I-9?", "I-12", "El orden va de menor a mayor número."),
      E(CAT + " Quieres el libro de poesía del catálogo. ¿Qué signatura anotas?", "P-5", "«Adivinanzas del campo» tiene signatura P-5, de la sección Poesía.")],
     [E(CAT + " Quieres un libro sobre ballenas. ¿Cuál es su signatura?", "I-30", "«Cómo viven las ballenas» está en el catálogo con esa signatura."),
      E("Un estante de la sección I tiene I-4, I-11, I-18 e I-27. Buscas I-18. ¿Entre qué dos libros está?", "Entre I-11 e I-27", "I-11 es menor y I-27 es mayor que 18."),
      E("Ordena de menor a mayor: C-30, C-4, C-12.", "C-4, C-12, C-30", "Se ordenan por el valor del número.")],
     [E("Un compañero ordenó I-9, I-100 e I-20 así: I-100, I-20, I-9. ¿Cuál es el orden correcto?", "I-9, I-20, I-100", "Se ordena por el valor del número, no por la primera cifra."),
      E(CAT + " " + SECC + " Buscas «Aves de Chile» (I-14) pero recorres el estante C-1 a C-40. ¿Por qué no lo encontrarás?", "Porque la letra I es otra sección y estás mirando Cuentos", "La letra de la signatura indica la sección.")],
     [E("Pasos para buscar un libro, desordenados: A) ir al estante con esa signatura, B) anotar la signatura, C) buscar «tortugas» en el catálogo. ¿En qué orden se hacen?", "C, B, A", "Primero se busca en el catálogo, luego se anota la signatura y al final se va al estante."),
      E("En el catálogo hay «Tortugas del mar», I-33; «Tortugas para pintar», A-6, de Arte; y «Cuento de la tortuga Tula», C-17. Quieres datos sobre cómo viven las tortugas marinas. ¿Cuál signatura anotas?", "I-33", "Es el único libro informativo sobre tortugas marinas.")]),
    [E(CAT + " " + SECC + " Tu profesora pide un libro de poemas. ¿Qué signatura anotas?", "P-5", "La sección Poesía tiene la letra P y el único título es «Adivinanzas del campo».")],
    [E("¿La signatura va en el lomo del libro?", "Sí", "Así se sabe dónde guardarlo."),
     E("¿Los números de las signaturas se ordenan por su valor?", "Sí", "9 va antes que 20 y 20 antes que 100."),
     E("¿Se puede buscar un libro en el catálogo por su título?", "Sí", "También por autor o tema.")],
    ("Usa este catálogo: «El zorro y la luna», C-8; «Volcanes de Chile», I-22; «Poemas de lluvia», P-3; «Mapas del mundo», M-4. Quieres saber cómo se forma un volcán. Escribe: el título que buscas, su signatura, la sección y qué harías después de anotarla. " + SECC, "Busco «Volcanes de Chile», signatura I-22, sección Informativos. Luego voy al estante y recorro los números hasta I-22.", ["elige el título correcto", "escribe la signatura exacta", "nombra la sección", "dice que irá al estante y seguirá el orden numérico"], ["cuatro datos escritos"], ["buscar en la sección equivocada", "ordenar los números por la primera cifra"], "Pide a otra persona que siga tus pasos y diga si llega al mismo libro."),
    "Con el catálogo de esta clase, escribe la signatura de dos libros y di en qué sección están.",
    "Inventa un catálogo con cuatro libros de tu curso y ordénalos por signatura.")

reg(
    OA8, 3, MATERIALES,
    "Aprenderé a elegir un libro según mi propósito y a anotarlo en el registro de préstamo. Sirve para llevar el material adecuado y devolverlo a tiempo.",
    ["Sé buscar un libro con la signatura.", "Sé sumar días en un calendario."],
    ["Elegir bien un libro es decidir con razones. Primero mira si el tema sirve para tu propósito. Luego mira el índice y el año de publicación si necesitas datos recientes. Después lee una página al azar: si no entiendes más de cinco palabras, quizás es muy difícil para ti ahora.",
     "El préstamo es llevar el material a casa por unos días. Para eso se hace un registro, que es una nota escrita de lo que se lleva. El registro del préstamo dice el título, la signatura, tu curso, la fecha de retiro y la fecha de devolución. Así la biblioteca sabe dónde está cada libro.",
     "La fecha de devolución depende del plazo. Si el plazo es de siete días y retiras el libro el día 4, debes devolverlo el 11. Anotar la fecha en tu agenda evita olvidos. Un libro devuelto a tiempo puede ser usado por otra persona."],
    [("registro de préstamo", "nota donde se escribe qué libro se lleva, quién y hasta cuándo"), ("plazo", "cantidad de días que puedes tener el libro"), ("fecha de devolución", "día en que debes entregar el libro"), ("índice", "lista de las partes de un libro con su página")],
    [("Elegir con razones", "Propósito: saber cómo viven las abejas. Libro A: «Las abejas y su colmena», con índice y página «Cómo viven». Libro B: «Cuento de la abeja Lila». ¿Cuál eliges?", ["Mi propósito es encontrar datos.", "El libro A informa y tiene índice.", "El libro B es un cuento."], "Libro A"),
     ("Calcular la devolución", "Retiras un libro el día 12 con plazo de 7 días. ¿Qué día lo devuelves?", ["Parto del día de retiro: 12.", "Sumo el plazo: 12 + 7.", "Da 19."], "El día 19")],
    [("Llevar un libro porque tiene linda portada, sin ver si sirve para el propósito.", "La portada no dice si el contenido te sirve.", "Mira el tema, el índice y una página."), ("No anotar la fecha de devolución.", "Se olvida y el libro se atrasa.", "Escríbela en el registro y en tu agenda.")],
    ([E("¿Qué es el plazo de un préstamo: los días que puedes tener el libro o el nombre del autor?", "Los días que puedes tener el libro", "El plazo es el tiempo del préstamo."),
      E("¿Qué se anota en el registro de préstamo: el título, la signatura y la fecha de devolución, o solo el color del libro?", "El título, la signatura y la fecha de devolución", "Permiten saber qué libro es y cuándo vuelve."),
      E("Quieres cuentos entretenidos para leer en casa. ¿Qué propósito tienes: elegir libros o investigar?", "Elegir libros", "Escoges lecturas por gusto.")],
     [A("Retiras un libro el día 9 con un plazo de 7 días. ¿Qué día es la devolución?", "9+7", "Se suma el plazo al día de retiro."),
      E("En una página al azar de un libro hay ocho palabras que no entiendes. ¿Es un buen libro para leer solo ahora? Responde sí o no.", "No", "Hay más de cinco palabras desconocidas, así que es muy difícil por ahora."),
      E("¿Para qué sirve mirar el índice de un libro antes de pedirlo prestado?", "Para ver si trae el tema que necesito", "El índice lista las partes del libro y sus páginas.")],
     [A("Retiras un libro el día 10 con un plazo de 7 días. ¿Qué día lo devuelves?", "10+7", "Se suma el plazo al día de retiro."),
      E("Necesitas datos recientes sobre robots. Libro A: año 2003. Libro B: año 2022. ¿Cuál eliges?", "Libro B", "Es más reciente."),
      E("Completa el registro: título «Aves de Chile», signatura I-14, retiro el día 6, plazo de 7 días. ¿Cuál es la fecha de devolución?", "El día 13", "6 + 7 = 13.")],
     [E("Lucas elige un libro por su portada brillante, pero es una novela y él necesita datos sobre el mar. ¿Qué error cometió?", "Eligió sin pensar en su propósito", "La portada no muestra si el contenido sirve."),
      E("Ana retiró un libro el día 5 con plazo de 7 días y lo devolvió el día 14. ¿Llegó a tiempo? Responde sí o no.", "No", "Debía devolverlo el día 12.")],
     [E("Propósito: preparar una disertación sobre los volcanes. Libro A: «Volcanes de Chile», con índice y fotos, 2021. Libro B: «Mis aventuras en el campo», un diario de viaje. Libro C: «Volcanes para colorear», con dibujos. ¿Cuál eliges y por qué?", "Libro A, porque trae información sobre el tema", "El B no trata del tema y el C solo tiene dibujos."),
      E("Retiras dos libros el día 3, uno con plazo de 7 días y otro con plazo de 14 días. ¿Qué día devuelves cada uno? Responde en orden.", "El día 10 y el día 17", "3 + 7 = 10 y 3 + 14 = 17.")]),
    [E("Quieres llevarte a casa un cuento para el fin de semana. Un libro tiene muchas palabras que no entiendes y otro es entretenido y lo entiendes bien. ¿Cuál eliges?", "El que entiendo bien", "Debe ser un libro que puedas leer con gusto.")],
    [E("¿El registro de préstamo lleva la fecha de devolución?", "Sí", "Dice cuándo debe volver el libro."),
     E("¿Un libro muy antiguo sirve siempre para datos recientes?", "No", "Puede no tener los datos nuevos."),
     E("¿Hay que mirar el propósito antes de elegir?", "Sí", "El libro debe servir para lo que necesito.")],
    ("Propósito: saber cómo viven los pingüinos. Opciones: Libro A, «Pingüinos del sur», informativo, 2020, con índice. Libro B, «El pingüino Pepe», cuento. Libro C, «Mapas de Asia». Elige uno, escribe por qué lo eliges y completa este registro de préstamo: título, signatura (A: I-18, B: C-9, C: M-2), fecha de retiro (día 5) y fecha de devolución (plazo de 7 días).", "Elijo el A porque es informativo y tiene índice. Registro: «Pingüinos del sur», I-18, retiro día 5, devolución día 12.", ["elige el libro que sirve para el propósito", "da una razón sobre el contenido", "copia el título y la signatura correctos", "calcula bien la fecha de devolución"], ["registro escrito completo"], ["elegir por portada", "calcular mal la fecha"], "Muestra tu registro a otra persona y pídele que revise la fecha."),
    "Escribe un registro de préstamo para un libro con retiro el día 8 y plazo de 7 días.",
    "Compara dos libros posibles para un mismo propósito y explica por qué elegirías uno.")

reg(
    OA8, 4, MATERIALES,
    "Aprenderé a cuidar y devolver los materiales de la biblioteca. Sirve para que los libros duren y otras personas puedan usarlos.",
    ["Sé pedir un libro prestado.", "Sé que debo devolverlo."],
    ["Los libros de la biblioteca son de todos. Por eso se cuida el material en favor del uso común, que significa que todos puedan usarlo. Si un libro se rompe, se pierde o no se devuelve, otras personas se quedan sin él.",
     "Para cuidar un libro: lávate las manos y no comas encima. No rayes ni dobles las páginas; usa un marcapáginas. Ábrelo con cuidado, sin forzar el lomo. Llévalo en la mochila, protegido de la lluvia. Si algo se daña, avisa a la persona encargada de la biblioteca; no lo arregles tú con cinta.",
     "Para devolver: hazlo en el plazo y entrégalo en el mesón o en el lugar indicado, sin dejarlo en una mesa ni guardarlo tú en el estante. Así la persona encargada lo anota como devuelto y lo vuelve a ordenar. Si no puedes devolverlo a tiempo, avisa y pide más plazo."],
    [("uso común", "que todas las personas puedan usar el material"), ("devolución", "entregar de vuelta lo que se prestó"), ("marcapáginas", "tira de papel o cartulina que señala dónde quedaste"), ("daño", "rotura o mancha que estropea un libro")],
    [("Decidir cómo cuidar", "Tienes un libro prestado y vas a leer mientras tomas once. ¿Qué haces?", ["La comida puede manchar el libro.", "Dejo el libro lejos y primero me lavo las manos.", "Leo sin comer encima."], "Leo con las manos limpias y sin comer sobre el libro"),
     ("Resolver un daño", "Una página de tu libro prestado se desprendió. ¿Qué haces?", ["No debo pegarla con cinta.", "La persona encargada sabe cómo repararla.", "Le aviso al devolverlo, o antes."], "Aviso a la persona encargada")],
    [("Dejar el libro devuelto en cualquier mesa.", "La persona encargada no sabe que fue devuelto y otros no lo encuentran.", "Entrégalo en el mesón."), ("Pegar con cinta una página rota.", "La cinta daña el papel con el tiempo.", "Avisa para que lo reparen bien.")],
    ([E("Para marcar dónde quedaste en un libro de la biblioteca, ¿usas un marcapáginas o doblas la página?", "Un marcapáginas", "Doblar la página la daña."),
      E("¿Los libros de la biblioteca son de una persona o de todos?", "De todos", "Se cuidan para el uso común."),
      E("Si un libro se moja, ¿avisas a la persona encargada o lo escondes?", "Avisas a la persona encargada", "Así saben cómo repararlo.")],
     [E("Nina lleva su libro prestado suelto en la mochila, bajo una botella de agua. ¿Qué riesgo corre el libro?", "Que se moje", "El agua estropea las páginas."),
      E("Un libro vence hoy y no alcanzaste a terminarlo. ¿Qué haces: avisar y pedir más plazo, o no devolverlo?", "Avisar y pedir más plazo", "Así otros saben cuándo estará disponible."),
      E("¿Qué significa «uso común»?", "Que todas las personas puedan usar el material", "El libro prestado debe volver para que otros lo lean.")],
     [E("Terminaste de leer en la biblioteca. ¿Dónde dejas el libro: en el mesón de devolución o en una mesa cualquiera?", "En el mesón de devolución", "Allí lo registran y lo ordenan."),
      E("Tu hermano menor dibujó en una página de tu libro prestado. ¿Qué haces primero?", "Avisar a la persona encargada", "No debes intentar borrarlo tú; ella decide cómo arreglarlo."),
      E("Tienes las manos con migas de galleta y vas a abrir un libro prestado. ¿Qué haces primero: limpiarte las manos o abrirlo igual?", "Limpiarme las manos", "Las migas y la grasa manchan el libro.")],
     [E("Tomás dice: «Si devuelvo tarde, no pasa nada». ¿Qué le pasa a otro niño que esperaba ese libro?", "Se queda sin poder usarlo", "El libro no está disponible mientras él lo tiene."),
      E("Un curso devuelve 12 libros con un día de atraso cada uno. ¿Cuántos días de atraso hay en total?", "12", "Son 12 libros con 1 día cada uno: 12 días.")],
     [E("Dos casos. Caso 1: Rosa subraya con lápiz un libro de la biblioteca porque «es solo una línea». Caso 2: Ema copia la frase en su cuaderno. ¿Cuál cuida el uso común?", "Caso 2", "Subrayar daña el libro de todos; copiar no."),
      E("Un libro vence el día 14. Un compañero lo devuelve el día 14 y otro el día 17. ¿Cuántos días de atraso tiene el segundo?", "3", "17 − 14 = 3 días.")]),
    [E("En el recreo llueve y llevas un libro prestado hacia la sala. ¿Lo cubres con la mochila o lo dejas al aire libre?", "Lo cubro con la mochila", "Así no se moja.")],
    [E("¿Se puede subrayar un libro de la biblioteca?", "No", "El libro es de todos."),
     E("¿Hay que devolver el libro en el plazo?", "Sí", "Así otros lo pueden usar."),
     E("¿Conviene avisar si un libro se dañó?", "Sí", "La persona encargada puede repararlo.")],
    ("Lee este caso: Mía retiró «Las ballenas» el día 3 con plazo de 7 días. El día 9 se le cayó jugo sobre una página y la dejó secando sin avisar. Devolvió el libro el día 14 y lo dejó sobre una mesa. Escribe tres cosas que hizo mal y qué debió hacer en cada una.", "1) No avisó del jugo: debió avisar. 2) Devolvió tarde (el día 10 era el límite): debió devolver o avisar. 3) Lo dejó en una mesa: debió entregarlo en el mesón.", ["nombra tres errores distintos", "explica qué haría en cada uno", "usa las fechas del caso", "nombra el cuidado del uso común"], ["tres errores con su corrección"], ["decir solo «portarse bien»", "no usar las fechas"], "Lee tu lista a otra persona y comprueba que cada error tenga su corrección."),
    "Escribe tres reglas para cuidar un libro prestado.",
    "Dibuja o escribe un cartel de cuatro líneas para pedir cuidado de los libros.")

reg(
    OA8, 5, MATERIALES,
    "Aprenderé a usar lo que sé en una situación distinta: una biblioteca de aula con pocas reglas escritas y un libro que no está disponible. Sirve para saber actuar aunque el lugar cambie.",
    ["Sé buscar con catálogo y signatura.", "Sé cuidar y devolver."],
    ["No todas las bibliotecas son iguales. En la biblioteca de aula, que es un estante con pocos libros en tu sala, puede que no haya catálogo ni signaturas. A veces los libros se ordenan por color de etiqueta, por tema o por tamaño. Lo primero es preguntar o mirar cómo se ordenan.",
     "Aunque cambie el lugar, el método es el mismo: tener un propósito, saber dónde buscar, anotar lo que llevas, cuidarlo y devolverlo. En una biblioteca de aula, el registro puede ser una hoja pegada en la pared con tu nombre, el título y la fecha.",
     "A veces el libro que quieres está prestado. Entonces puedes anotarte en una lista de espera, pedir otro libro del mismo tema o volver otro día. No se pide a un compañero que te lo pase si el libro está a su nombre, porque el registro quedaría mal."],
    [("biblioteca de aula", "estante con libros en la sala de clases, para uso del curso"), ("lista de espera", "lista de personas que esperan un libro prestado"), ("etiqueta", "papel pegado que indica tema o sección"), ("criterio de orden", "regla que se usa para ordenar los libros")],
    [("Entender el orden", "En tu sala, los libros tienen etiqueta azul (animales), roja (cuentos) y verde (poesía). Quieres leer un poema. ¿Qué etiqueta buscas?", ["Poesía es el tipo de texto.", "La etiqueta verde es de poesía.", "Voy a esos libros."], "La etiqueta verde"),
     ("Qué hacer sin el libro", "Quieres «Las ballenas», pero está prestado a otro compañero hasta el día 12. ¿Qué puedes hacer?", ["No debo pedírselo a quien lo tiene.", "Puedo anotarme en la lista de espera.", "O pedir otro libro del tema."], "Anotarme en la lista de espera o pedir otro libro de ballenas")],
    [("Sacar un libro de la sala sin anotarlo, porque «es un curso pequeño».", "Sin registro, nadie sabe dónde está.", "Anota título, nombre y fecha en la hoja."), ("Pedirle a un compañero el libro que está a su nombre.", "El registro dice que lo tiene él y se pierde el control.", "Anótate en la lista de espera.")],
    ([E("¿Qué es una biblioteca de aula: un estante con libros en tu sala o un edificio aparte?", "Un estante con libros en tu sala", "Está en la sala para uso del curso."),
      E("En la sala, los libros azules son de animales. Quieres información sobre delfines. ¿Qué color miras?", "Azul", "Los animales están en la etiqueta azul."),
      E("¿Qué es una lista de espera?", "Una lista de quienes esperan un libro prestado", "Se usa cuando el libro no está disponible.")],
     [E("En una biblioteca de aula no hay catálogo. ¿Qué haces primero para saber cómo encontrar un libro?", "Preguntar o mirar cómo están ordenados", "Cada biblioteca tiene su propio criterio de orden."),
      E("La hoja de registro del aula tiene tres columnas: nombre, título y fecha. ¿Cuántos datos anotas por cada libro que llevas?", "3", "Son nombre, título y fecha."),
      E("Quieres un libro que ya tiene otro compañero a su nombre. ¿Qué haces: anotarte en la lista de espera o llevártelo?", "Anotarme en la lista de espera", "Así se respeta el registro y el uso común.")],
     [E("Etiquetas del aula: roja, cuentos; azul, animales; verde, poesía; amarilla, mapas. Buscas un atlas. ¿Qué color eliges?", "Amarillo", "El atlas es de mapas."),
      E("Quieres llevar «La luna y el mar» (etiqueta roja) hasta el lunes. ¿Qué escribes en la hoja? Escribe los tres datos que faltan: tu nombre, el título y la fecha.", "Mi nombre, «La luna y el mar» y la fecha de hoy", "Son los datos de registro de esa hoja."),
      E("El libro que quieres vuelve el día 15. Hoy es el día 11. ¿Cuántos días faltan?", "4", "15 − 11 = 4.")],
     [E("Marta dice: «En mi sala no hay catálogo, así que no puedo ser ordenada con los libros». ¿Qué respuesta es correcta?", "Puede seguir el criterio de orden de la sala y anotar sus préstamos", "El método de cuidado y registro no cambia."),
      E("Si el libro que necesitas no está, ¿es mejor irte sin nada o pedir otro del mismo tema? Elige y explica.", "Pedir otro del mismo tema, porque así cumplo mi propósito", "El propósito se puede lograr con otro libro.")],
     [E("Caso: Quieres datos de pingüinos. Etiquetas: azul, animales; roja, cuentos. El libro azul de pingüinos está prestado hasta el día 12 y hoy es el día 9. Hay un cuento rojo llamado «El pingüino Lalo». ¿Qué conviene hacer para investigar?", "Anotarme en la lista de espera o buscar otro libro azul", "El cuento no entrega datos reales."),
      E("Si en la sala todos los libros se guardan por altura, ¿puedes encontrar un cuento por su signatura?", "No", "Ese criterio no usa signaturas.")]),
    [E("Hoy llegas al fondo de la sala a buscar un libro y ves una hoja de registro pegada con 5 nombres y libros. Quieres llevarte «El puma Tito» y nadie lo tiene anotado. ¿Qué haces antes de salir con él?", "Anotar mi nombre, el título y la fecha", "El registro debe mostrar quién lo tiene.")],
    [E("¿El método de cuidar y registrar sirve también en la sala?", "Sí", "Es el mismo en cualquier biblioteca."),
     E("¿Hay que mirar cómo están ordenados los libros?", "Sí", "Cada biblioteca puede tener otro orden."),
     E("¿Puedo anotarme en una lista de espera?", "Sí", "Sirve cuando el libro no está disponible.")],
    ("Imagina esta biblioteca de aula: etiqueta azul, animales; roja, cuentos; verde, poesía. Quieres leer algo sobre las orcas para tu trabajo de ciencias. El libro azul «Orcas del sur» está prestado hasta el día 12, y hoy es el día 8. Escribe tu plan: qué propósito tienes, qué harás con el libro prestado y cómo vas a registrar lo que te lleves.", "Mi propósito es encontrar información sobre orcas. Me anotaré en la lista de espera del libro azul y mientras reviso otro libro azul; si me lo llevo, anotaré mi nombre, título y fecha.", ["nombra el propósito", "propone una solución para el libro prestado", "dice qué registrará", "es coherente con las reglas de la sala"], ["plan escrito en pocas líneas"], ["decir «le pido el libro a mi compañero»", "olvidar el registro"], "Pide a otra persona que diga si tu plan respeta el uso común."),
    "Escribe un criterio distinto para ordenar una biblioteca de aula y una ventaja.",
    "Diseña una hoja de registro para una sala con cinco columnas y escribe un ejemplo.")

reg(
    OA8, 6, MATERIALES,
    "Aprenderé a resumir lo que encontré en la biblioteca y a decidir qué haré en mi próxima visita. Sirve para mejorar cada vez que voy.",
    ["Sé el propósito de mi visita.", "Sé buscar, registrar, cuidar y devolver."],
    ["Al terminar una visita conviene preguntarse qué logré. Un hallazgo es lo que encontraste o aprendiste. Puede ser un dato, un libro o una forma de buscar que te funcionó. Anótalo con tus palabras, junto con el título y la signatura, para poder volver.",
     "También revisa lo que salió mal: si no encontraste el libro, si perdiste tiempo o si te atrasaste con el plazo. Cada problema tiene un próximo paso: usar el catálogo antes de recorrer estantes, anotar la fecha en la agenda, escoger un libro más fácil.",
     "Una buena síntesis dice: mi propósito, qué encontré, cómo lo registré, cómo cuidé el material y qué haré la próxima vez. Cabe en cinco oraciones. Sirve para planear la siguiente visita y para contarle a otros qué hay en la biblioteca."],
    [("hallazgo", "lo que encontraste o aprendiste en una búsqueda"), ("síntesis", "resumen breve de lo más importante"), ("próximo paso", "lo que harás después para mejorar"), ("evaluar", "revisar qué salió bien y qué se puede mejorar")],
    [("Escribir un hallazgo", "Buscaste «¿Cuántos años viven las tortugas?» en «Tortugas del mar», I-33, y leíste que algunas pueden vivir más de 50 años. Escribe el hallazgo con tus palabras y la fuente.", ["Digo la idea sin copiar.", "Agrego título y signatura.", "Escribo una oración."], "Algunas tortugas viven más de 50 años (fuente: «Tortugas del mar», I-33)."),
     ("Decidir el próximo paso", "Perdiste 20 minutos recorriendo estantes sin hallar tu libro. ¿Qué haces la próxima vez?", ["El problema fue buscar a ciegas.", "Existe una herramienta para eso: el catálogo.", "Primero busco en el catálogo y anoto la signatura."], "Buscar primero en el catálogo y anotar la signatura")],
    [("Anotar solo «encontré cosas».", "No dice cuál fue el hallazgo ni de dónde viene.", "Escribe el dato, el título y la signatura."), ("Pensar que una visita en la que algo salió mal fue inútil.", "Los problemas sirven para planear mejoras.", "Escribe un próximo paso para cada problema.")],
    ([E("¿Un hallazgo es lo que encontraste o lo que perdiste?", "Lo que encontraste", "Es el dato o material que descubriste."),
      E("¿Qué sirve para anotar de dónde sacaste un dato: título y signatura o solo el día de la semana?", "Título y signatura", "Permiten volver al libro."),
      E("¿Qué es un próximo paso: algo que harás para mejorar o un libro de cuentos?", "Algo que harás para mejorar", "Responde a «¿qué haré la próxima vez?».")],
     [E("En una síntesis de visita, la oración «La próxima vez llegaré con más tiempo para leer» es parte de qué: ¿el hallazgo o el próximo paso?", "El próximo paso", "Dice qué haré después para mejorar."),
      E("Pedro escribió: «Fui a la biblioteca y fue bueno». ¿Qué le falta a su síntesis?", "Decir su propósito, qué encontró y cuál es su próximo paso", "Es muy general; no aporta datos."),
      E("No terminaste de leer tu libro en el plazo. ¿Cuál es un buen próximo paso: pedir más plazo o no volver?", "Pedir más plazo", "Soluciona el problema sin perjudicar a otros.")],
     [E("Hallazgo: en «Aves de Chile» (I-14) leíste que el cóndor es un ave grande que vuela alto. Escribe cuál es la fuente completa que anotarías.", "«Aves de Chile», I-14", "Son título y signatura."),
      E("Problema: entregaste el libro dos días tarde. ¿Cuál es un próximo paso útil: anotar la fecha de devolución en la agenda o devolverlo siempre al final?", "Anotar la fecha de devolución en la agenda", "Ayuda a recordar el plazo."),
      E("Visita 1: encontraste el libro en 5 minutos. Visita 2: tardaste 20. ¿Cuántos minutos más tardaste en la segunda?", "15", "20 − 5 = 15.")],
     [E("Lucía dice: «Si no encontré el libro, mi visita no sirvió». Elena dice: «Sirvió: aprendí que debo usar el catálogo». ¿Quién evalúa mejor su visita?", "Elena", "Convierte el problema en un próximo paso."),
      E("¿Por qué conviene anotar los hallazgos con tus palabras y no copiar?", "Porque así compruebo que entendí", "Copiar no muestra comprensión.")],
     [E("Síntesis A: «Fui a investigar sobre ballenas. Usé el catálogo y anoté I-30. Aprendí que son mamíferos. Devolví el libro a tiempo. Próxima vez buscaré otro libro del tema.» Síntesis B: «Fui y vi cosas». ¿Cuál síntesis cumple mejor?", "A", "Tiene propósito, hallazgo, registro, cuidado y próximo paso."),
      E("De las cinco partes de una síntesis (propósito, hallazgo, registro, cuidado y próximo paso), ¿cuántas tiene la síntesis B «Fui y vi cosas»?", "0", "No dice ni el propósito, ni el hallazgo, ni el registro, ni el cuidado, ni el próximo paso.")]),
    [E("Tu profesora te pide contar a tu curso en una oración qué lograste hoy en la biblioteca. Hallaste en «Cómo viven las ballenas» (I-30) que las ballenas respiran aire. ¿Cuál oración sirve: «Descubrí que las ballenas respiran aire en I-30» o «Fue fome»?", "Descubrí que las ballenas respiran aire en I-30", "Dice el hallazgo y la fuente.")],
    [E("¿Un problema en la visita puede dar un próximo paso?", "Sí", "Sirve para mejorar la próxima visita."),
     E("¿Anotar la signatura ayuda a volver al libro?", "Sí", "Dice dónde está."),
     E("¿La síntesis puede ser muy larga?", "No", "Debe ser breve, de unas cinco oraciones.")],
    ("Escribe tu síntesis de una visita a la biblioteca con cinco oraciones: tu propósito, un hallazgo (usa este: «Los delfines usan sonidos para comunicarse», en «Delfines», I-40), cómo lo registraste, cómo cuidaste el libro y tu próximo paso.", "Fui a investigar sobre delfines. Hallé que los delfines usan sonidos para comunicarse en «Delfines», I-40. Lo anoté con título y signatura. Cuidé el libro con las manos limpias. La próxima vez usaré el catálogo antes de recorrer estantes.", ["tiene las cinco partes", "usa el dato dado con sus palabras", "anota título y signatura", "propone un próximo paso realista"], ["cinco oraciones escritas"], ["copiar la frase del texto", "olvidar el próximo paso"], "Pide a otra persona que cuente cuántas partes tiene tu síntesis."),
    "Escribe tres próximos pasos para mejorar tus visitas a la biblioteca.",
    "Escribe una síntesis de visita a una biblioteca de aula que tenga un problema y un próximo paso.")
