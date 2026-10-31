"""Cuaderno del estudiante, 6.º básico Historia, Geografía y Ciencias Sociales: OA 22 (participar en la elección de la directiva de curso)."""
from __future__ import annotations

from student_content_hi6_lib import arith, lesson

OA22 = "HI06 OA 22"

# ================================================================ OA 22 · clase 1
lesson(
    OA22, 1,
    "Aprenderé a ubicar las etapas, los lugares y los tiempos de una elección de directiva de curso, desde el anuncio hasta la proclamación. Sirve para participar en una elección ordenada y justa.",
    ["Sé que en una democracia las autoridades se eligen por voto.", "Sé que participar es una forma de cuidar lo que es de todos."],
    [
        "La directiva de curso es el grupo de estudiantes que representa y organiza al curso: por ejemplo, presidente o presidenta, secretario o secretaria y tesorero o tesorera. Se elige por votación. Elegir bien es importante porque quienes ganan toman decisiones que afectan a todos.",
        "Una elección tiene etapas ordenadas. Primero, el anuncio y la formación de una comisión electoral, que cuida que todo sea justo. Segundo, la inscripción de candidatos, que son las personas que quieren ser elegidas, con sus propuestas. Tercero, la campaña, donde cada candidato muestra sus propuestas con afiches o discursos. Cuarto, la votación secreta: cada estudiante recibe una papeleta, marca una sola opción y la deposita en una urna, que es una caja cerrada. Quinto, el escrutinio, que es el conteo de votos, hecho en público. Sexto, la proclamación de quienes ganaron.",
        "También importan el lugar y el tiempo. La votación se hace en la sala o en un lugar acordado, a una hora fijada. La campaña tiene un plazo y termina antes del día de votar. Cada etapa tiene un responsable. Participar significa informarse sobre las propuestas, votar con libertad y respetar el resultado.",
    ],
    [("directiva de curso", "grupo de estudiantes elegido para representar y organizar al curso"), ("candidato", "persona que se presenta para ser elegida"), ("papeleta", "papel donde se marca el voto"), ("urna", "caja cerrada donde se depositan los votos"), ("escrutinio", "conteo de los votos, hecho en público")],
    [
        ("Ordenar etapas", "Ordena tres etapas de una elección: votación, anuncio, escrutinio.", ["El anuncio abre el proceso.", "Luego se vota.", "Al final se cuentan los votos."], "Anuncio, votación, escrutinio"),
        ("Calcular un plazo", "La campaña empieza el lunes 10 y termina el jueves 13. La votación es el viernes 14. ¿Cuántos días dura la campaña, contando ambos?", ["Cuento 10, 11, 12 y 13.", "Son 4 días.", "El viernes ya se vota."], "4 días"),
    ],
    [
        ("Pensar que se puede votar más de una vez.", "Cada estudiante tiene un solo voto.", "Marca una sola opción."),
        ("Creer que la elección empieza el día de votar.", "Antes hay anuncio, candidaturas y campaña.", "Conoce todas las etapas."),
    ],
    [
        ("La urna, ¿es una caja cerrada donde se depositan los votos o una lista de candidatos?", "Una caja cerrada donde se depositan los votos", "Así se definió en el vocabulario."),
        ("El escrutinio, ¿es el conteo de votos o la campaña?", "El conteo de votos", "Así se definió en el vocabulario."),
        ("Un candidato, ¿es una persona que quiere ser elegida o una persona que cuenta los votos?", "Una persona que quiere ser elegida", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué la votación es secreta?", "Para que cada persona vote con libertad", "Nadie sabe por quién votó cada uno."),
        ("¿Para qué sirve una comisión electoral?", "Para cuidar que la elección sea justa", "Supervisa las etapas."),
        ("¿Por qué el escrutinio se hace en público?", "Para que todos vean que el conteo es honesto", "Así se genera confianza."),
    ],
    [
        ("Etapas desordenadas: A) campaña, B) votación, C) inscripción de candidatos. ¿Cuál es el orden correcto?", "C, A, B", "Primero se inscriben, luego hacen campaña y después se vota."),
        arith("Un curso tiene 32 estudiantes y 2 faltan el día de votar. Si todos los presentes entregan 1 papeleta, ¿cuántas papeletas debe haber en la urna?", "32-2", "Se restan los ausentes y cada presente entrega una papeleta.", " papeletas"),
        ("El escrutinio comienza a las 10:30 y dura 30 minutos. ¿A qué hora termina?", "A las 11:00", "10:30 más 30 minutos es 11:00."),
    ],
    [
        ("Luis dice: «Puedo votar dos veces por mi amigo». ¿Qué error comete?", "Cada estudiante tiene un solo voto", "Votar dos veces sería injusto."),
        ("Una compañera dice: «No me informo, voto por quien tenga el afiche más grande». ¿Qué criterio falta?", "Evaluar las propuestas", "El tamaño del afiche no muestra si la propuesta es buena."),
    ],
    [
        ("Ordena de la primera a la última etapa: A) escrutinio, B) campaña, C) proclamación, D) inscripción de candidatos.", "D, B, A, C", "Primero se inscriben, luego campaña, escrutinio y proclamación."),
        ("Una elección empieza el lunes 3 con el anuncio, la campaña dura hasta el jueves 6 y se vota el viernes 7. ¿Cuántos días hay entre el anuncio y la votación, contando ambos?", "5", "Del 3 al 7 hay cinco días.", "7-3+1"),
    ],
    [("En la sala 6.º C, la votación es el viernes a las 9:00. La campaña termina el jueves. Una estudiante pregunta si puede repartir afiches el viernes durante la votación. ¿Debe hacerse la campaña antes o durante la votación?", "Antes de la votación", "La campaña termina el día anterior para que cada uno vote con calma.")],
    [("En Historia: ¿qué es la directiva de curso?", "El grupo de estudiantes elegido para representar y organizar al curso", "Es la definición de la clase."), ("¿Qué es una urna?", "Una caja cerrada donde se depositan los votos", "Es la definición de la clase."), ("¿Qué etapa viene después de la votación?", "El escrutinio", "Se cuentan los votos.")],
    (
        "Planifica una elección de directiva para tu curso, con este calendario base: lunes, anuncio y comisión electoral; martes, inscripción de candidatos; miércoles y jueves, campaña; viernes, votación y escrutinio. Escribe: quién integraría la comisión (tres cargos), dónde se vota, a qué hora y qué materiales se necesitan (papeletas, urna, lápices). Agrega una regla que cuide que sea justa.",
        "Comisión: presidente, secretario y vocal. Lugar: la sala, a las 10:00. Materiales: papeletas, urna y lápices. Regla: cada persona vota una sola vez.",
        ["incluye todas las etapas del calendario", "indica lugar, hora y materiales", "agrega una regla de justicia"],
        ["plan escrito en seis líneas"],
        ["olvidar el escrutinio", "no definir el lugar"],
        "Lee tu plan a una persona de tu casa y pídele que diga qué etapa se podría mejorar.",
    ),
    "Pregunta a una persona de tu casa cómo era la elección de directiva cuando ella estudiaba y anótalo.",
    "Escribe una regla que ayudaría a que todos voten con libertad.",
)

# ================================================================ OA 22 · clase 2
lesson(
    OA22, 2,
    "Aprenderé a leer las propuestas de los candidatos como fuentes y a preguntar quién las hizo, si son claras y si se pueden cumplir. Sirve para votar con información y no por simpatía o por promesas imposibles.",
    ["Sé las etapas de una elección.", "Sé que una fuente tiene una procedencia."],
    [
        "En una campaña, las propuestas aparecen en afiches, discursos y programas escritos. Son fuentes, y hay que preguntar su procedencia: quién las hizo, cuándo y para qué. Un candidato las hace para convencer, por eso hay que revisarlas con atención y no solo creer.",
        "Para evaluar una propuesta usamos criterios. ¿Es clara, o sea dice qué se hará y cómo? ¿Es viable, o sea se puede cumplir con el tiempo, los materiales y las reglas de la escuela? ¿Beneficia a todo el curso o solo a unos pocos? ¿La persona que la propone tiene un historial de cumplir lo que promete? Una promesa como «no habrá más pruebas» no es viable, porque la directiva no decide eso.",
        "También separamos lo que dice la propuesta, lo que interpretamos y lo que no sabemos. Si un afiche dice «Soy el mejor», eso es una opinión, no una evidencia. Si dice «Organizaré un campeonato de ajedrez los jueves en el recreo», eso es una propuesta concreta que podemos revisar. Informarse antes de votar es parte de ser un buen ciudadano.",
    ],
    [("propuesta", "idea de lo que un candidato hará si es elegido"), ("viable", "que se puede cumplir con el tiempo y los medios disponibles"), ("promesa", "compromiso de hacer algo"), ("historial", "lo que una persona ha hecho antes"), ("criterio", "regla igual para evaluar todas las propuestas")],
    [
        ("Evaluar una propuesta", "Un candidato propone: «Organizaré un campeonato de ajedrez cada jueves en el recreo». ¿Es clara y concreta o es una frase vacía?", ["Dice qué hará y cuándo.", "Se puede revisar.", "Es clara y concreta."], "Clara y concreta"),
        ("Distinguir lo viable", "Otro candidato promete: «No habrá más tareas». ¿Es viable para una directiva de curso?", ["La directiva no decide las tareas.", "No puede cumplirla.", "No es viable."], "No es viable"),
    ],
    [
        ("Votar por quien tiene el afiche más bonito.", "La belleza del afiche no dice si la propuesta es buena.", "Evalúa la propuesta con criterios."),
        ("Creer toda promesa sin revisar si se puede cumplir.", "Algunas promesas no dependen de la directiva.", "Pregunta si es viable."),
    ],
    [
        ("Una propuesta, ¿es lo que un candidato hará si es elegido o su apellido?", "Lo que un candidato hará si es elegido", "Así se definió en el vocabulario."),
        ("«Soy el mejor», ¿es una propuesta concreta o una opinión?", "Una opinión", "No dice qué hará."),
        ("Una promesa viable, ¿se puede cumplir o es imposible?", "Se puede cumplir", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué conviene preguntar quién hizo el afiche de un candidato?", "Porque lo hizo para convencer", "Su propósito es obtener votos."),
        ("¿Por qué conviene mirar el historial de quien propone?", "Para ver si cumplió lo que prometió antes", "Cumplir antes sugiere que cumplirá después."),
        ("¿Por qué una propuesta que beneficia a todo el curso es mejor que una que beneficia a pocos?", "Porque la directiva representa a todos", "Debe pensar en el bien común del curso."),
    ],
    [
        ("Candidata Carla propone una biblioteca de aula con 20 libros donados y turnos de préstamo. ¿Es clara y viable?", "Sí", "Dice cuántos libros y cómo se prestan."),
        ("Candidato Diego propone: «Todos tendrán mejores notas». ¿Quién decide las notas: la directiva o los profesores?", "Los profesores", "La directiva no pone las notas."),
        ("Candidata Eva propone un recreo de 2 horas. Un recreo normal dura 15 minutos y es decisión de la dirección. ¿Es viable para la directiva?", "No", "El horario lo define la dirección."),
    ],
    [
        ("Teo dice: «Voto por Diego porque promete cosas bonitas». ¿Qué error comete?", "No revisa si las promesas se pueden cumplir", "Una promesa debe ser viable."),
        ("Una candidata no explica cómo hará su propuesta, solo dice «Será genial». ¿Qué le falta a su propuesta?", "Claridad sobre qué hará y cómo", "Sin detalles no se puede evaluar."),
    ],
    [
        ("Ordena los pasos para evaluar: A) decidir por quién votar, B) leer quién hizo la propuesta, C) revisar si es clara y viable.", "B, C, A", "Primero la procedencia, luego la evaluación y al final la decisión."),
        ("Tabla de criterios de ejemplo: la propuesta de Carla cumple 3 de 4 criterios y la de Diego 1 de 4. ¿Cuántos criterios más cumple Carla?", "2", "3 menos 1 es 2.", "3-1"),
    ],
    [("Un candidato muestra un cuaderno con registro de lo que hizo el año pasado: entregó a tiempo 9 de 10 informes del curso. ¿Qué criterio apoya con ese dato: el historial de cumplir o la belleza del afiche?", "El historial de cumplir", "Muestra que ha cumplido responsabilidades antes.")],
    [("¿Qué es una propuesta viable?", "Una que se puede cumplir con el tiempo y los medios disponibles", "Es la definición de la clase."), ("¿Qué criterios sirven para evaluar propuestas?", "Si son claras, viables y benefician a todos", "Así se enseñó en la clase."), ("¿Un afiche bonito prueba que la propuesta es buena?", "No", "La belleza no mide la calidad de la propuesta.")],
    (
        "Evalúa estas tres propuestas inventadas con los criterios claro, viable y beneficia a todos: Ana: «Armaré un calendario de cumpleaños del curso y un mural». Beto: «Prometo que todos tendrán un 7 en todas las pruebas». Carla: «Organizaré turnos de limpieza para que la sala esté ordenada». Escribe una tabla con sí o no por criterio y por qué votarías por una de ellas.",
        "Ana: clara sí, viable sí, beneficia a todos sí. Beto: clara no, viable no, beneficia a todos no. Carla: clara sí, viable sí, beneficia sí. Votaría por Carla porque cumple todos y mejora la sala.",
        ["usa los tres criterios", "justifica el voto", "distingue una promesa no viable"],
        ["tabla de tres filas y una frase"],
        ["no usar los criterios", "votar por simpatía"],
        "Muestra tu tabla a una persona de tu casa y pídele que diga si coincide con tu elección.",
    ),
    "Escribe una propuesta que haría mejorar tu curso y revisa si es viable.",
    "Escribe una pregunta que le harías a un candidato para comprobar su propuesta.",
)

# ================================================================ OA 22 · clase 3
lesson(
    OA22, 3,
    "Aprenderé a relacionar lo que ocurre cuando se elige a personas responsables y cuando no se participa o se vota sin informarse. Sirve para entender por qué mi voto y mi participación importan.",
    ["Sé evaluar propuestas con criterios.", "Sé que una causa explica por qué ocurre algo."],
    [
        "Elegir personas responsables tiene consecuencias. Una persona responsable cumple lo que promete, llega a las reuniones, escucha al curso y rinde cuentas, es decir, cuenta lo que hizo. Si el curso elige personas así, la directiva organiza actividades, resuelve problemas y representa bien al curso. Si elige sin pensar, puede ocurrir que la directiva no cumpla, que las reuniones no se hagan o que el curso se divida.",
        "Los actores son los candidatos, los votantes, la comisión electoral y el profesor jefe que acompaña. Cada uno tiene responsabilidades: los candidatos, presentar propuestas viables; los votantes, informarse y votar; la comisión, cuidar que todo sea justo. Cuando alguien no vota, se llama abstención. Si muchos se abstienen, deciden pocos y la directiva puede representar mal a los demás.",
        "También hay votos blancos, si la papeleta no tiene marca, y votos nulos, si tiene más de una marca o está dañada. Un voto blanco o nulo no suma a ningún candidato. Después de la elección, quienes ganaron deben cumplir sus propuestas y el curso debe colaborar. Respetar el resultado es parte de la democracia.",
    ],
    [("responsable", "que cumple lo que promete y se hace cargo de sus actos"), ("abstención", "no votar en una elección"), ("voto blanco", "papeleta sin ninguna marca"), ("voto nulo", "papeleta con más de una marca o dañada"), ("rendir cuentas", "contar lo que se hizo y asumir las responsabilidades")],
    [
        ("Armar una cadena", "Un curso elige a una presidenta responsable. Ella cumple lo prometido y organiza una actividad. Nombra causa y consecuencia.", ["Causa: se eligió a una persona responsable.", "Consecuencia: se cumplió lo prometido.", "El curso se beneficia."], "Causa: elección de una persona responsable; consecuencia: se cumplen las propuestas"),
        ("Contar votos", "En una urna hay 20 votos: 12 para A, 6 para B, 1 blanco y 1 nulo. ¿Cuántos votos recibieron en total los candidatos?", ["Sumo los de A y B.", "12 más 6.", "Son 18 votos."], "18 votos"),
    ],
    [
        ("Pensar que no votar no afecta a nadie.", "Si muchos no votan, deciden pocos.", "Participa e infórmate."),
        ("Creer que el voto blanco o nulo suma a un candidato.", "No suma a ninguno.", "Marca una sola opción con claridad."),
    ],
    [
        ("Un voto sin marca, ¿es blanco o nulo?", "Blanco", "Así se definió en el vocabulario."),
        ("Un voto con dos marcas, ¿es blanco o nulo?", "Nulo", "Tiene más de una marca."),
        ("No votar, ¿se llama abstención o escrutinio?", "Abstención", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué conviene elegir personas responsables?", "Porque cumplen lo prometido y representan bien al curso", "Esa es la consecuencia positiva."),
        ("¿Por qué la abstención de muchos puede perjudicar al curso?", "Porque deciden pocos y la directiva puede representar mal a los demás", "Menos personas participan en la decisión."),
        ("¿Por qué se debe respetar el resultado de la elección?", "Porque es una regla acordada por todos", "Así se mantiene la convivencia."),
    ],
    [
        arith("En una elección de ejemplo votaron 25 estudiantes y 3 votos fueron nulos. ¿Cuántos votos no fueron nulos?", "25-3", "Se restan los nulos al total.", " votos"),
        ("Un curso tiene 30 estudiantes y votan 24. ¿Cuántos se abstienen?", "6", "30 menos 24 es 6.", "30-24"),
        ("Una presidenta prometió reunirse cada mes y se reunió 4 veces en 4 meses. ¿Cumplió su promesa: sí o no?", "Sí", "Una reunión por mes en 4 meses son 4."),
    ],
    [
        ("Eva dice: «No voy a votar porque mi voto no cambia nada». ¿Qué error comete?", "Cada voto suma y las decisiones las toman quienes participan", "Un voto puede ser decisivo."),
        ("Una presidenta electa no cumple ninguna propuesta. ¿Quiénes pueden exigirle que rinda cuentas: el curso que la eligió o un curso de otra escuela?", "El curso que la eligió", "Los votantes pueden pedir explicaciones a quien eligieron."),
    ],
    [
        ("Ordena la cadena: A) la directiva organiza actividades, B) el curso elige a personas responsables, C) los compañeros participan y el curso mejora.", "B, A, C", "Primero la elección, luego las actividades y después la mejora."),
        ("En una votación de ejemplo, A tiene 11 votos, B tiene 11 votos y otros 8 votos son de otros candidatos. ¿Hay empate entre A y B: sí o no?", "Sí", "Ambos tienen 11 votos."),
    ],
    [("Un curso de 28 estudiantes elige presidente. Gana Bruno con 13 votos, Carla tiene 12 y hay 3 votos nulos. ¿Cuántos votos más tuvo Bruno que Carla?", "1", "13 menos 12 es 1.")],
    [("¿Qué es la abstención?", "No votar en una elección", "Es la definición de la clase."), ("¿Qué es un voto nulo?", "Una papeleta con más de una marca o dañada", "Es la definición de la clase."), ("¿Qué debe hacer una persona responsable con lo que promete?", "Cumplirlo", "Se hace cargo de sus compromisos.")],
    (
        "Elige una de estas situaciones y escribe causa, actores, consecuencia y qué harías tú como votante. Situación a) un curso elige a un presidente que prometió reuniones y las cumple; situación b) 15 de 30 estudiantes no votan y gana un candidato por 8 votos; situación c) un candidato que no cumplió lo prometido el año pasado vuelve a presentarse.",
        "Situación b: causa: abstención de la mitad; actores: votantes y candidato; consecuencia: deciden pocos; yo votaría e invitaría a participar.",
        ["nombra causa y actores", "explica la consecuencia", "propone qué haría como votante"],
        ["cuatro frases escritas"],
        ["no vincular la causa con la consecuencia", "olvidar a algún actor"],
        "Lee tu respuesta a una persona de tu casa y pídele que diga si ella votaría igual.",
    ),
    "Escribe una razón por la que cada voto cuenta.",
    "Escribe una pregunta que le harías a un candidato sobre cómo rendirá cuentas.",
)

# ================================================================ OA 22 · clase 4
lesson(
    OA22, 4,
    "Aprenderé a comparar candidaturas con los mismos criterios, a contar los votos con un escrutinio y a respetar el resultado, reconociendo perspectivas distintas. Sirve para decidir mi voto y participar con madurez.",
    ["Sé evaluar propuestas con criterios.", "Sé qué consecuencias tiene votar con información."],
    [
        "Para comparar candidaturas usamos los mismos criterios para todos: propuesta clara, viable, beneficia a todo el curso e historial responsable. Una tabla ayuda a ver con orden. Por ejemplo, la candidata A cumple los cuatro criterios, el candidato B cumple dos y la candidata C cumple uno. Eso no obliga a votar por A, pero da evidencia para decidir.",
        "Cada votante tiene una perspectiva, es decir, una mirada según su situación. A una persona le interesa el deporte, a otra el arte, a otra los problemas de convivencia. Por eso puede preferir una propuesta distinta. Entender las perspectivas ayuda a respetar que otras personas voten distinto.",
        "Después se hace el escrutinio: se cuentan los votos en público, uno por uno. Gana quien tiene más votos. Si hay empate, se hace una segunda votación solo entre quienes empataron. Quien gana asume la responsabilidad de representar a todo el curso, incluso a quienes no votaron por él. Y quienes no ganaron pueden colaborar en la directiva. Aceptar el resultado es una actitud cívica.",
    ],
    [("criterio", "regla igual para comparar candidaturas"), ("perspectiva", "mirada de una persona según su situación"), ("escrutinio", "conteo público de los votos"), ("empate", "cuando dos o más candidatos reciben la misma cantidad de votos"), ("proclamación", "anuncio de quién ganó la elección")],
    [
        ("Comparar con criterios", "Candidata A cumple 4 criterios; candidato B cumple 2. ¿Cuántos criterios más cumple A?", ["Resto los criterios.", "4 menos 2.", "Son 2."], "2 criterios más"),
        ("Hacer un escrutinio", "Votos: Ana 9, Beto 7, Carla 6. ¿Quién gana?", ["Comparo los votos.", "9 es el mayor.", "Gana Ana."], "Ana"),
    ],
    [
        ("Votar por la persona más simpática sin comparar propuestas.", "La simpatía no dice si cumplirá.", "Usa los mismos criterios para todos."),
        ("No aceptar el resultado cuando el candidato preferido pierde.", "Respetar el resultado es parte de la democracia.", "Colabora con la directiva elegida."),
    ],
    [
        ("Si dos candidatos reciben la misma cantidad de votos, ¿hay empate o escrutinio?", "Empate", "Así se definió en el vocabulario."),
        ("¿Quién gana una elección: quien tiene más votos o quien tiene más amigos?", "Quien tiene más votos", "Es la regla de la votación."),
        ("La proclamación, ¿es el anuncio de quién ganó o la campaña?", "El anuncio de quién ganó", "Así se definió en el vocabulario."),
    ],
    [
        ("¿Por qué conviene usar los mismos criterios para comparar a todos los candidatos?", "Para que la comparación sea justa", "Se mide lo mismo en todos."),
        ("¿Por qué las personas votan distinto aunque vean las mismas propuestas?", "Porque tienen perspectivas e intereses distintos", "Cada uno valora lo que le importa."),
        ("¿Por qué quien gana debe representar también a quienes no votaron por él?", "Porque la directiva representa a todo el curso", "Su responsabilidad es con todos."),
    ],
    [
        arith("Escrutinio de ejemplo: Dani 11 votos, Eli 8 votos, Fer 5 votos y 2 votos nulos. ¿Cuántos estudiantes votaron en total?", "11+8+5+2", "Se suman todos los votos de la urna.", " estudiantes"),
        arith("Con el mismo escrutinio (Dani 11, Eli 8, Fer 5), ¿cuántos votos más tuvo Dani que Fer?", "11-5", "Se resta el menor al mayor.", " votos"),
        ("Escrutinio de ejemplo: Gus 9 votos y Hana 9 votos. ¿Qué se hace según la regla de la clase: segunda votación entre ambos o gana el mayor de edad?", "Segunda votación entre ambos", "Un empate se resuelve votando de nuevo."),
    ],
    [
        ("Marta dice: «Voté por otro, así que no voy a ayudar a la directiva». ¿Qué error comete?", "Respetar el resultado y colaborar es parte de la democracia", "La directiva representa a todos."),
        ("Una estudiante prefiere la propuesta de deportes y otro la de arte. ¿Son perspectivas iguales o distintas?", "Distintas", "Cada uno valora algo diferente."),
    ],
    [
        ("Ordena por votos, de mayor a menor: Ivo 7, Jaz 12, Kai 9.", "Jaz, Kai, Ivo", "12 es mayor que 9 y este que 7."),
        ("Tabla de ejemplo con criterios: A cumple 4, B cumple 3, C cumple 1. Un votante prefiere los criterios de «historial responsable»; A y B lo cumplen y C no. ¿Cuál descarta primero: C o A?", "C", "No cumple el criterio que más valora."),
    ],
    [("Un curso de 30 estudiantes elige presidente. Lupe obtiene 14 votos, Mati 13 y hay 3 blancos. ¿Quién gana y por cuántos votos?", "Lupe, por 1 voto", "14 menos 13 es 1.")],
    [("¿Cómo se resuelve un empate?", "Con una segunda votación entre quienes empataron", "Es la regla de la clase."), ("¿Qué es la proclamación?", "El anuncio de quién ganó", "Es la definición de la clase."), ("¿Respetar el resultado es parte de la democracia?", "Sí", "Aceptar una decisión acordada es una actitud cívica.")],
    (
        "Tienes estas tres candidaturas inventadas. Ana: propuesta clara, viable, beneficia a todos, historial responsable. Beto: propuesta clara, no viable, beneficia a pocos, historial responsable. Carla: propuesta clara, viable, beneficia a todos, sin historial conocido. Haz una tabla de criterios con sí o no, cuenta los criterios que cumple cada una, elige una y escribe en dos frases por qué. Luego escribe cómo colaborarías con la directiva si ganara otra persona.",
        "Ana cumple 4, Beto 2, Carla 3. Elijo a Ana porque cumple los cuatro. Si ganara otra persona, colaboraría proponiendo ideas.",
        ["cuenta bien los criterios", "justifica la elección con evidencia", "propone cómo colaborar con quien gane"],
        ["tabla de tres filas y tres frases"],
        ["contar mal", "elegir sin justificar"],
        "Muestra tu tabla a una persona de tu casa y pídele que cuente contigo los criterios de cada candidata.",
    ),
    "Anota dos cosas que harías para ayudar a una directiva de curso.",
    "Escribe una frase que puedas decir cuando pierde tu candidato preferido.",
)
