"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 06 (mitosis, meiosis y alteraciones de la división celular), OA 07 (herencia mendeliana) y OA 08 (manipulación genética)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


OA6 = "CN2M OA 06"
OA7 = "CN2M OA 07"
OA8 = "CN2M OA 08"


# ---------------------------------------------------------------- OA 06

L(OA6, 1,
  materials="Este cuaderno y lápiz. Todos los datos están escritos en los ejercicios; no necesitas materiales especiales.",
  use="Aprenderé a distinguir mitosis y meiosis y a escribir preguntas que se pueden contestar con datos sobre cómo se transmite el material genético. Sirve para no mezclar los dos procesos de división celular.",
  prior=["Sé que el material genético está en el núcleo, organizado en cromosomas.", "Sé que una pregunta investigable indica qué se mide."],
  explain=[
      "Las células nuevas nacen de células que ya existen, por división celular. En la mitosis una célula madre forma dos células hijas con el mismo número de cromosomas y la misma información genética. Sirve para crecer, reparar tejidos y, en algunos organismos, reproducirse sin pareja. Las células del cuerpo humano que no son gametos tienen 46 cromosomas.",
      "En la meiosis una célula madre forma cuatro células hijas con la mitad de los cromosomas. Ocurre en los órganos reproductores y produce gametos: óvulos y espermatozoides en los animales. Un gameto humano tiene 23 cromosomas; al unirse dos gametos en la fecundación se recupera el número completo, 46. Así el material genético pasa de una generación a la siguiente sin duplicarse en cada una.",
      "Para investigar estos procesos hace falta una pregunta que indique qué se cuenta o se mide. «¿Cuántos cromosomas tienen las células hijas comparadas con la célula madre?» se contesta contando en imágenes del microscopio. «¿Cuál división es más linda?» no se puede investigar, porque «linda» no se mide.",
  ],
  vocab=[("mitosis", "división que forma dos células hijas iguales a la madre"), ("meiosis", "división que forma cuatro células con la mitad de cromosomas"), ("cromosoma", "estructura que contiene el ADN de la célula"), ("gameto", "célula sexual, como el óvulo o el espermatozoide"), ("célula hija", "célula que resulta de una división")],
  worked=[
      ("Comparar los dos procesos", "Una célula de ejemplo tiene 12 cromosomas y se divide. Indica cuántas células hijas y cuántos cromosomas tiene cada una si ocurre mitosis y si ocurre meiosis.", ["Mitosis: se forman 2 células y cada una conserva los 12 cromosomas.", "Meiosis: se forman 4 células y cada una recibe la mitad.", "La mitad de 12 es 6."], "Mitosis: 2 células con 12 cromosomas; meiosis: 4 células con 6 cromosomas"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Es hermosa la mitosis?» para que se pueda investigar.", ["Quito la opinión «hermosa».", "Indico qué se cuenta: los cromosomas de la célula madre y de las hijas.", "Indico la comparación: célula madre frente a células hijas."], "«¿Tienen las células hijas de la punta de una raíz el mismo número de cromosomas que la célula madre?»"),
  ],
  mistakes=[
      ("Decir que la meiosis forma dos células hijas.", "La meiosis forma cuatro células; la que forma dos es la mitosis.", "Recuerda: mitosis = 2 iguales; meiosis = 4 con la mitad."),
      ("Creer que los gametos tienen el mismo número de cromosomas que las demás células del cuerpo.", "Los gametos tienen la mitad, para que el cigoto recupere el número completo.", "Pregunta: ¿esta célula es un gameto? Entonces tiene la mitad."),
  ],
  rec=[
      ("¿Cuántas células hijas produce una mitosis?", "Dos", "La mitosis forma dos células hijas iguales."),
      ("Verdadero o falso: los gametos se forman por meiosis.", "Verdadero", "La meiosis produce las células sexuales."),
      ("¿Cuántos cromosomas tiene una célula del cuerpo humano que no es un gameto?", "46", "Es el número completo; los gametos tienen 23."),
  ],
  und=[
      ("Una herida en la piel se cierra con células nuevas. ¿Qué proceso las produce? A) Mitosis; B) Meiosis.", "A", "La reparación de tejidos usa divisiones que producen células iguales."),
      ("¿Por qué los gametos tienen la mitad de los cromosomas? A) Para que la fecundación recupere el número completo; B) Porque se les cae un cromosoma con la edad.", "A", "Dos gametos con la mitad suman el número normal en el cigoto."),
      ("Una división forma cuatro células con la mitad de cromosomas. ¿Es mitosis o meiosis?", "Meiosis", "Cuatro células con la mitad es el resultado de la meiosis."),
  ],
  app=[
      arith("Una célula de ejemplo con 20 cromosomas se divide por meiosis. ¿Cuántos cromosomas tiene cada célula hija?", "20//2", "Cada hija recibe la mitad de los cromosomas."),
      arith("Una célula de ejemplo con 8 cromosomas se divide por mitosis. ¿Cuántos cromosomas hay en total sumando las dos células hijas?", "8*2", "Cada una de las dos hijas conserva los 8 cromosomas."),
      ("¿Qué pregunta permite contrastar los dos procesos con datos? A) ¿Cuántas células hijas se forman en una mitosis y en una meiosis de una misma célula madre?; B) ¿Cuál de los dos procesos es más importante para las personas?", "A", "Indica qué se cuenta y qué se compara; la otra pide una opinión."),
  ],
  rea=[
      ("Un compañero dice: «Los espermatozoides tienen 46 cromosomas, igual que la piel». ¿Qué le responderías? A) Tienen 23, porque se forman por meiosis; B) Tiene razón, porque la mitosis los produce.", "A", "Los gametos se forman por meiosis y tienen la mitad de los cromosomas."),
      ("Un equipo observa que una célula madre de 14 cromosomas dio cuatro células de 7 cromosomas. ¿Qué proceso ocurrió?", "Meiosis", "Cuatro células con la mitad indican meiosis."),
  ],
  cha=[
      arith("Si los dos gametos que se unen tuvieran 46 cromosomas cada uno, ¿cuántos cromosomas tendría el cigoto?", "46+46", "Por eso los gametos deben reducirse a la mitad por meiosis."),
      ("Un estudiante propone la hipótesis «la mitosis conserva el número de cromosomas». ¿Qué dato la pone a prueba? A) Contar los cromosomas de la célula madre y de las hijas; B) Medir la altura del organismo.", "A", "La hipótesis habla de número de cromosomas, que es lo que hay que contar."),
  ],
  context=[arith("En un tejido de ejemplo se dividen por mitosis 3 células madre. ¿Cuántas células hijas se forman en total?", "3*2", "Cada mitosis forma dos células hijas.")],
  selfcheck=[("¿Cuántas células hijas forma la meiosis?", "Cuatro", "Cada una tiene la mitad de los cromosomas."), ("¿Para qué sirve la mitosis en el cuerpo?", "Para crecer y reparar tejidos", "Produce células iguales a la madre."), ("¿Qué hace investigable una pregunta sobre división celular?", "Que indica qué se cuenta o se mide", "Así se puede contestar con datos.")],
  open_task=task("Completa una tabla con dos columnas, mitosis y meiosis, y estas filas: cuántas células hijas se forman; cuántos cromosomas tiene cada hija si la madre tiene 16; en qué se usa. Después escribe una pregunta investigable que compare los dos procesos y diga qué se cuenta.", "Mitosis: 2 células, 16 cromosomas cada una, crecer y reparar. Meiosis: 4 células, 8 cromosomas cada una, formar gametos. Pregunta: «¿Cuántos cromosomas tienen las células hijas de una mitosis frente a las de una meiosis de una misma célula madre?»", ["la tabla tiene las tres filas completas", "calcula bien los cromosomas de cada hija", "la pregunta indica qué se cuenta"], ["tabla y una pregunta"], ["poner 2 células en la meiosis", "escribir una pregunta de opinión"], "Pregunta qué imagen del microscopio necesitarías para contestar tu pregunta."),
  reinforce="Escribe una frase que diga para qué sirve cada proceso, mitosis y meiosis.",
  extend="Explica por qué, si no existiera la meiosis, el número de cromosomas se duplicaría en cada generación.")

L(OA6, 2,
  materials="Este cuaderno y lápiz. Los datos de las tablas son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé a leer datos del conteo de células en división y a comparar tejidos. Sirve para saber qué parte de un tejido se está dividiendo.",
  prior=["Sé que la mitosis forma dos células iguales y la meiosis cuatro con la mitad de cromosomas.", "Sé calcular una suma, una resta y una división entera."],
  explain=[
      "Una célula pasa casi todo su tiempo en la interfase, cuando crece y copia su ADN. La mitosis es la parte corta en que el núcleo se divide. Por eso, al mirar un tejido en crecimiento en el microscopio, la mayoría de las células está en interfase y solo unas pocas están en mitosis. Contar cuántas hay de cada tipo da una idea de cuánto se divide ese tejido.",
      "La mitosis se reconoce por etapas: en la profase los cromosomas se hacen visibles; en la metafase se alinean en el centro; en la anafase las copias de cada cromosoma se separan hacia lados opuestos; en la telofase se forman dos núcleos. Después el citoplasma se divide y quedan dos células. Un conteo de ejemplo puede anotarse en una tabla con una fila por etapa.",
      "Para comparar tejidos hay que usar la misma cantidad de células observadas. Si en un tejido se cuentan 4 células en mitosis entre 50 y en otro 9 entre 50, el segundo se divide más en esa muestra. El resultado vale para la muestra: otra muestra podría dar valores distintos.",
  ],
  vocab=[("interfase", "etapa en que la célula crece y copia su ADN"), ("profase", "primera etapa de la mitosis; los cromosomas se hacen visibles"), ("metafase", "etapa en que los cromosomas se alinean en el centro"), ("anafase", "etapa en que las copias de los cromosomas se separan"), ("telofase", "etapa en que se forman dos núcleos")],
  worked=[
      ("Contar células en división", "En una muestra de ejemplo de raíz se observaron 60 células: 54 en interfase y el resto en mitosis. ¿Cuántas estaban en mitosis y qué fracción es?", ["Células en mitosis: 60 − 54 = 6.", "La fracción es 6 de 60.", "6 de 60 equivale a 1 de cada 10."], "6 células en mitosis, 1 de cada 10"),
      ("Ordenar etapas", "Ordena estas etapas de la mitosis: anafase, profase, telofase, metafase.", ["Primero los cromosomas se hacen visibles: profase.", "Luego se alinean en el centro: metafase.", "Después se separan las copias: anafase, y al final se forman dos núcleos: telofase."], "Profase, metafase, anafase, telofase"),
  ],
  mistakes=[
      ("Pensar que una célula en interfase está sin actividad.", "En la interfase la célula crece y copia su ADN; es una etapa muy activa.", "Recuerda: la interfase prepara la división."),
      ("Comparar dos tejidos contando muestras de distinto tamaño sin ajustar.", "Los números no son comparables si no se observó la misma cantidad de células.", "Compara con la misma cantidad observada o con fracciones."),
  ],
  rec=[
      ("¿En qué etapa se copia el ADN antes de la mitosis?", "En la interfase", "La interfase incluye la copia del ADN."),
      ("¿Cuál es la primera etapa de la mitosis?", "Profase", "En ella los cromosomas se hacen visibles."),
      ("Verdadero o falso: en un tejido en crecimiento la mayoría de las células está en mitosis al mismo tiempo.", "Falso", "La mayoría está en interfase, que es la etapa más larga."),
  ],
  und=[
      ("En la metafase los cromosomas están A) alineados en el centro de la célula; B) ya separados en dos núcleos.", "A", "La alineación central es lo que caracteriza la metafase."),
      ("¿Por qué se observa un número pequeño de células en mitosis? A) Porque la mitosis dura poco comparada con la interfase; B) Porque casi ninguna célula se divide jamás.", "A", "Es una etapa corta en el ciclo de la célula."),
      ("¿Qué etapa viene justo después de la anafase?", "Telofase", "En la telofase se forman los dos núcleos."),
  ],
  app=[
      arith("En una muestra de ejemplo de 80 células, 72 están en interfase. ¿Cuántas están en mitosis?", "80-72", "Se restan las células en interfase del total."),
      arith("Tabla de ejemplo de células en mitosis: profase 5, metafase 2, anafase 1, telofase 2. ¿Cuántas células en mitosis hay en total?", "5+2+1+2", "Se suman las células de las cuatro etapas."),
      ("Un tejido tiene 3 células en mitosis entre 50 observadas y otro tiene 7 entre 50 (datos de ejemplo). ¿Qué tejido se dividía más en esa muestra? A) El segundo; B) El primero.", "A", "Con igual cantidad observada, más células en mitosis indica más división."),
  ],
  rea=[
      ("Una persona contó 20 células en mitosis entre 200 en el tejido X y 15 entre 100 en el tejido Y. Dice que X se divide más porque 20 es mayor que 15. ¿Qué falla tiene? A) Observó cantidades distintas y no puede comparar los números sin ajustar; B) Debió contar solo la anafase.", "A", "Con 100 células, 15 es más proporción que 20 entre 200."),
      ("¿Por qué una muestra no basta para afirmar cuánto se divide un órgano completo? A) Porque otra muestra podría dar valores distintos; B) Porque el microscopio cambia las células.", "A", "Una muestra es una parte del tejido y tiene variación."),
  ],
  cha=[
      arith("En el tejido Y de ejemplo hubo 15 células en mitosis entre 100. Si se hubieran observado 200 células con la misma proporción, ¿cuántas estarían en mitosis?", "15*2", "Al duplicar las células observadas se duplica lo esperado."),
      ("En una imagen, una célula tiene sus cromosomas separados en dos grupos que se alejan. ¿En qué etapa está?", "Anafase", "Las copias se separan hacia lados opuestos en la anafase."),
  ],
  context=[arith("Un laboratorio escolar de ejemplo observó 90 células de una raíz y contó 9 en mitosis. ¿Cuántas de cada 10 células estaban en mitosis?", "9*10//90", "Se calcula la proporción por cada 10 células.")],
  selfcheck=[("¿Qué ocurre en la interfase?", "La célula crece y copia su ADN", "Es la etapa previa a la mitosis."), ("Nombra las cuatro etapas de la mitosis en orden.", "Profase, metafase, anafase, telofase", "Es el orden en que ocurren."), ("¿Por qué hay que observar igual cantidad de células para comparar tejidos?", "Para que los números sean comparables", "Cantidades distintas distorsionan la comparación.")],
  open_task=task("Datos de ejemplo de dos tejidos, con 100 células observadas en cada uno. Raíz: 12 en mitosis. Hoja adulta: 3 en mitosis. Calcula cuántas células están en interfase en cada tejido, indica cuál se divide más en la muestra y escribe una oración que declare un límite del conteo.", "Raíz: 100 − 12 = 88 en interfase. Hoja: 100 − 3 = 97. La raíz se divide más en esta muestra. Es solo una muestra de 100 células, otra muestra podría dar un valor distinto.", ["calcula bien los dos valores", "compara con igual cantidad observada", "declara un límite"], ["dos cálculos y dos oraciones"], ["comparar sin considerar la cantidad observada", "decir que la hoja nunca se divide"], "Pregunta qué harías para tener más confianza en el resultado."),
  reinforce="Dibuja las cuatro etapas de la mitosis con círculos y palitos y rotúlalas.",
  extend="Explica por qué la cantidad de células en mitosis puede cambiar de un tejido a otro.")

L(OA6, 3,
  materials="Este cuaderno y lápices de dos colores. Dibujarás cromosomas como palitos de colores; no necesitas más materiales.",
  use="Aprenderé a construir un modelo de cromosomas para seguir la mitosis y la meiosis y a decir qué muestra bien el modelo y qué no. Sirve para entender por qué la meiosis reduce los cromosomas a la mitad.",
  prior=["Sé las etapas de la mitosis.", "Sé que los gametos tienen la mitad de los cromosomas."],
  explain=[
      "Un modelo representa un proceso con objetos o dibujos simples, por ejemplo palitos de colores. Para la célula de ejemplo usamos 4 cromosomas: 2 pares de homólogos. Un par homólogo son dos cromosomas parecidos, uno heredado de cada progenitor. Se dibujan con dos colores: el color indica de qué progenitor viene. Antes de dividirse, cada cromosoma se copia y queda formado por dos cromátidas hermanas unidas.",
      "En la mitosis las cromátidas hermanas se separan: cada célula hija recibe 4 cromosomas, uno de cada tipo y color. En la meiosis hay dos divisiones. En la primera se separan los cromosomas homólogos: cada célula recibe 2 cromosomas. En la segunda se separan las cromátidas: resultan 4 células con 2 cromosomas simples cada una. Además, durante la meiosis los homólogos pueden intercambiar trozos, lo que mezcla la información.",
      "Todo modelo tiene límites. Este muestra el número de cromosomas y su reparto, pero no su tamaño real, ni el ADN, ni el tiempo que dura cada etapa. Un buen modelo se contrasta con los datos: si el modelo predice cuatro células hijas con 2 cromosomas y las observaciones muestran eso, el modelo es útil.",
  ],
  vocab=[("cromosomas homólogos", "par de cromosomas parecidos, uno de cada progenitor"), ("cromátida", "cada una de las dos copias unidas de un cromosoma duplicado"), ("meiosis I", "primera división de la meiosis; separa homólogos"), ("meiosis II", "segunda división de la meiosis; separa cromátidas"), ("modelo", "representación simple de un proceso")],
  worked=[
      ("Seguir la mitosis en el modelo", "Una célula modelo tiene 6 cromosomas, que se duplican. ¿Cuántos cromosomas tiene cada célula hija tras la mitosis?", ["Cada cromosoma duplicado tiene dos cromátidas hermanas.", "En la mitosis las cromátidas se separan, una para cada célula.", "Cada hija recibe una cromátida de cada cromosoma: 6."], "Cada célula hija tiene 6 cromosomas"),
      ("Seguir la meiosis en el modelo", "La misma célula modelo de 6 cromosomas hace meiosis. ¿Cuántos cromosomas tiene cada una de las 4 células finales?", ["En meiosis I se separan los homólogos: cada célula recibe la mitad, 3 cromosomas.", "En meiosis II se separan las cromátidas, sin reducir más el número.", "Las 4 células finales quedan con 3 cromosomas."], "Cuatro células con 3 cromosomas cada una"),
  ],
  mistakes=[
      ("Decir que en la meiosis I se separan las cromátidas hermanas.", "En la meiosis I se separan los cromosomas homólogos; las cromátidas se separan en la meiosis II.", "Asocia: meiosis I separa pares; meiosis II separa copias."),
      ("Creer que el modelo es una réplica exacta de la célula.", "Un modelo simplifica y no muestra el tamaño real ni el ADN.", "Declara siempre qué muestra y qué no muestra el modelo."),
  ],
  rec=[
      ("¿Cómo se llama cada una de las dos copias unidas de un cromosoma duplicado?", "Cromátida", "Las dos cromátidas hermanas forman el cromosoma duplicado."),
      ("¿Cuántas divisiones seguidas tiene la meiosis?", "Dos", "Son la meiosis I y la meiosis II."),
      ("Verdadero o falso: en la mitosis se separan los cromosomas homólogos.", "Falso", "En la mitosis se separan las cromátidas hermanas."),
  ],
  und=[
      ("¿Qué se separa en la meiosis I? A) Los cromosomas homólogos; B) Las cromátidas hermanas.", "A", "La primera división reduce el número a la mitad al separar homólogos."),
      ("¿Qué muestra mal un modelo de palitos de colores? A) El tamaño real de los cromosomas; B) El número de cromosomas.", "A", "El modelo simplifica el tamaño, pero sí representa el número."),
      ("Un par de cromosomas homólogos viene de A) un cromosoma de cada progenitor; B) un solo progenitor.", "A", "Un homólogo viene de cada progenitor."),
  ],
  app=[
      arith("Una célula modelo tiene 10 cromosomas y hace meiosis. ¿Cuántos cromosomas tiene cada célula final?", "10//2", "La meiosis deja la mitad en cada célula final."),
      arith("Una célula modelo con 4 cromosomas hace meiosis. ¿Cuántos cromosomas hay en total sumando las cuatro células finales?", "4*2", "Hay 4 células finales con 2 cromosomas cada una."),
      ("En el modelo, una célula hija tiene 4 cromosomas y la madre tenía 4. ¿Qué proceso representa? A) Mitosis; B) Meiosis.", "A", "Conservar el número de cromosomas es característico de la mitosis."),
  ],
  rea=[
      ("Un modelo predice cuatro células con la mitad de cromosomas. Las observaciones muestran dos células con el número completo. ¿Qué proceso ocurrió realmente? A) Mitosis; B) Meiosis.", "A", "Dos células con el número completo coinciden con la mitosis y no con el modelo de meiosis."),
      ("Para explicar la mezcla de información en la meiosis, ¿qué agregarías al modelo? A) Intercambio de trozos entre homólogos de distinto color; B) Pintar todos los cromosomas del mismo color.", "A", "El intercambio entre homólogos mezcla la información de los dos progenitores."),
  ],
  cha=[
      arith("Una célula modelo tiene 14 cromosomas y se divide por meiosis. ¿Cuántos cromosomas hay en total sumando sus cuatro células finales?", "4*7", "Cada una de las cuatro células finales tiene 7 cromosomas."),
      ("Si fallara la meiosis I y los homólogos no se separaran bien, ¿qué esperarías? A) Células con un número de cromosomas alterado; B) Células perfectamente normales.", "A", "Sin separación adecuada el reparto queda desigual."),
  ],
  context=[arith("Una especie de ejemplo tiene 18 cromosomas en las células de su cuerpo. ¿Cuántos cromosomas tiene cada uno de sus gametos?", "18//2", "El gameto tiene la mitad de los cromosomas.")],
  selfcheck=[("¿Qué se separa en la meiosis II?", "Las cromátidas hermanas", "Es la segunda división."), ("¿Cuántas células finales forma la meiosis?", "Cuatro", "Dos divisiones seguidas dan cuatro células."), ("Nombra un límite de un modelo de palitos.", "No muestra el tamaño real ni el ADN", "Un modelo simplifica el proceso.")],
  open_task=task("Con una célula modelo de 4 cromosomas (2 rojos y 2 azules, un rojo y un azul de cada tipo), dibuja cómo quedan las células hijas en una mitosis y las cuatro células de una meiosis. Rotula cuántos cromosomas tiene cada una y escribe una oración sobre un límite de tu dibujo.", "Mitosis: 2 células con 4 cromosomas cada una (2 rojos y 2 azules). Meiosis: 4 células con 2 cromosomas cada una. Límite: el dibujo no muestra el tamaño real ni el ADN.", ["la mitosis conserva 4 cromosomas", "la meiosis deja 2 cromosomas por célula", "declara un límite"], ["dibujo rotulado y una oración"], ["dejar 4 cromosomas en la meiosis", "olvidar el límite del modelo"], "Pregunta qué cambiaría en el dibujo si la célula tuviera 6 cromosomas."),
  reinforce="Explica con un dibujo la diferencia entre separar homólogos y separar cromátidas.",
  extend="Explica por qué la mezcla de información en la meiosis hace que los hermanos no sean idénticos.")

L(OA6, 4,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo y están escritas en los ejercicios.",
  use="Aprenderé a relacionar el tiempo con el número de células cuando se dividen por mitosis y a identificar qué variables se cambian, se miden y se controlan. Sirve para entender por qué un tejido crece y por qué la división debe tener freno.",
  prior=["Sé que la mitosis forma dos células hijas iguales.", "Sé identificar variable independiente, dependiente y controlada."],
  explain=[
      "Si cada célula se divide por mitosis y sus hijas también se dividen, el número de células se duplica en cada ronda: 1, 2, 4, 8, 16. No aumenta de a una cantidad fija sino que se multiplica por 2 cada vez. Después de varias rondas, el número de células crece muy rápido. Una tabla de ejemplo con el tiempo y el número de células permite ver este patrón.",
      "En un cultivo de células, la variable independiente puede ser el tiempo transcurrido y la dependiente, el número de células. Si se quiere comparar dos condiciones, por ejemplo dos cantidades de alimento, se mantienen iguales el tipo de célula y la temperatura. Solo así se puede atribuir la diferencia al alimento. Dos tejidos pueden dividirse a distinta velocidad: la piel se renueva con frecuencia, mientras que las neuronas maduras casi no se dividen.",
      "En un organismo sano la división tiene frenos: las células reciben señales para dividirse y para detenerse, y faltan recursos para crecer sin límite. Por eso una curva que se duplica siempre no describe a un tejido sano. Cuando los frenos fallan, las células pueden dividirse sin control, tema que verás en la próxima clase.",
  ],
  vocab=[("duplicarse", "pasar a ser el doble en cada ronda"), ("cultivo", "conjunto de células que crecen en un medio con alimento"), ("tasa de división", "rapidez con que se dividen las células de un tejido"), ("renovación", "reemplazo de células viejas por células nuevas"), ("freno de la división", "señal que detiene la división de una célula")],
  worked=[
      ("Predecir con una tabla", "Tabla de ejemplo de un cultivo que parte con 1 célula: 0 h, 1 célula; 3 h, 2 células; 6 h, 4 células; 9 h, 8 células. Predice cuántas habrá a las 15 h.", ["Cada 3 horas el número se duplica.", "De 9 h a 15 h pasan 6 horas, es decir 2 duplicaciones más.", "8 × 2 × 2 = 32."], "A las 15 h habría 32 células"),
      ("Identificar variables", "Se estudia si la cantidad de alimento cambia el número de células de un cultivo después de 6 horas. Indica las variables.", ["Lo que se cambia a propósito es la cantidad de alimento.", "Lo que se mide es el número de células a las 6 horas.", "Se mantienen iguales el tipo de célula y la temperatura."], "Independiente: alimento; dependiente: número de células; controladas: tipo de célula y temperatura"),
  ],
  mistakes=[
      ("Decir que el número aumenta siempre en la misma cantidad (1, 3, 5, 7).", "En la división celular el número se duplica, no suma una cantidad fija.", "Pregunta: ¿se multiplica por 2 o se suma lo mismo?"),
      ("Pensar que todos los tejidos se dividen igual de rápido.", "Cada tejido tiene su propia tasa: la piel se renueva mucho y las neuronas maduras casi no se dividen.", "Compara siempre tejidos con datos del tejido."),
  ],
  rec=[
      arith("Una célula se divide por mitosis y sus descendientes también se dividen. ¿Cuántas células hay tras 3 rondas?", "2*2*2", "El número se duplica en cada ronda."),
      ("En la secuencia 1, 2, 4, 8, ¿qué número sigue?", "16", "Cada término es el doble del anterior."),
      ("Verdadero o falso: si el tiempo entre divisiones es más corto, en el mismo lapso habrá más células.", "Verdadero", "Más rondas en el mismo tiempo dan más duplicaciones."),
  ],
  und=[
      ("En un cultivo de ejemplo, el número de células crece así: 1, 2, 4, 8. ¿Cómo cambia? A) Se duplica en cada ronda; B) Aumenta siempre en 2 unidades.", "A", "Pasa de 1 a 2, de 2 a 4 y de 4 a 8: se multiplica por 2."),
      ("En una tabla de tiempo y número de células, ¿qué variable es la dependiente?", "El número de células", "Es la que se mide y depende del tiempo."),
      ("¿Por qué se mantiene igual la temperatura al comparar dos cultivos? A) Para que solo cambie la variable estudiada; B) Para que el cultivo crezca más.", "A", "Una variable controlada evita mezclar causas."),
  ],
  app=[
      arith("Un cultivo de ejemplo parte con 1 célula que se divide cada 2 horas. ¿Cuántas células hay después de 8 horas?", "2*2*2*2", "En 8 horas hay 4 rondas y el número se duplica en cada una."),
      arith("Un cultivo parte con 5 células y se duplica 3 veces. ¿Cuántas células hay al final?", "5*2*2*2", "Se multiplica por 2 en cada una de las tres rondas."),
      ("Un tejido de ejemplo repara una herida en 5 días y otro en 12 días. ¿Cuál probablemente tiene la tasa de división más alta? A) El que repara en 5 días; B) El que repara en 12 días.", "A", "Repara más rápido porque produce células nuevas con más rapidez."),
  ],
  rea=[
      ("Un estudiante dice que un cultivo con una duplicación cada 3 horas tendrá 3 células a las 6 horas, partiendo de 1. ¿Qué le responderías? A) Habrá 4, porque se duplica en cada ronda; B) Está bien, porque 6 dividido en 2 es 3.", "A", "Hay dos rondas y 1 pasa a 2 y luego a 4."),
      ("Para probar si la temperatura cambia la rapidez de división, ¿qué debe mantenerse igual? A) El tipo de célula y el alimento; B) El tipo de célula distinto en cada temperatura.", "A", "Si cambian otras variables no se sabe qué produjo la diferencia."),
  ],
  cha=[
      arith("Dos cultivos de ejemplo se duplican 2 veces. El cultivo A parte con 3 células y el B con 6. ¿Cuántas células más tiene B al final?", "6*4-3*4", "A queda con 12 y B con 24; la diferencia es 12."),
      ("¿Por qué una curva que se duplica siempre no describe a un tejido sano? A) Porque hay señales que frenan la división y los recursos son limitados; B) Porque las células sanas pierden cromosomas.", "A", "En el organismo la división tiene frenos y límites."),
  ],
  context=[arith("En un laboratorio de ejemplo, una célula y todas sus descendientes se dividen 5 veces seguidas. ¿Cuántas células resultan?", "2*2*2*2*2", "Cada ronda duplica el número de células.")],
  selfcheck=[("¿Qué pasa con el número de células en cada ronda de mitosis?", "Se duplica", "Cada célula forma dos hijas."), ("¿Qué variable se mide al estudiar el crecimiento de un cultivo?", "El número de células", "Es la variable dependiente."), ("¿Por qué un tejido sano no crece sin límite?", "Porque tiene señales que frenan la división", "Hay frenos y recursos limitados.")],
  open_task=task("Datos de ejemplo de dos cultivos que parten con 1 célula. Cultivo A: se duplica cada 2 horas. Cultivo B: se duplica cada 4 horas. Calcula cuántas células tiene cada uno a las 8 horas, indica quién tiene más y escribe una oración que diga qué variables habría que mantener iguales para compararlos.", "A: 4 rondas, 16 células. B: 2 rondas, 4 células. A tiene más. Habría que mantener iguales el tipo de célula, el alimento y la temperatura.", ["calcula bien los dos números", "compara correctamente", "nombra variables controladas"], ["dos cálculos y dos oraciones"], ["sumar en lugar de duplicar", "no mencionar variables controladas"], "Pregunta qué pasaría a las 12 horas en cada cultivo."),
  reinforce="Construye una tabla de tiempo y número de células con 5 rondas de duplicación.",
  extend="Explica por qué la duplicación sin freno sería un problema para un órgano.")

L(OA6, 5,
  materials="Este cuaderno y lápiz. Todos los casos son ficticios y están escritos en los ejercicios.",
  use="Aprenderé a explicar cómo una falla en el control de la división produce un tumor o cáncer y cómo un error en la meiosis produce una trisomía. Sirve para distinguir causas y consecuencias sin mitos.",
  prior=["Sé que la mitosis forma células iguales y la meiosis gametos con la mitad de cromosomas.", "Sé que los tejidos tienen frenos de la división."],
  explain=[
      "El ciclo celular está controlado por genes. Una mutación es un cambio en el ADN. Si una mutación daña genes que frenan o que ordenan la división, la célula puede dividirse sin control y formar un tumor, que es una masa de células. Un tumor benigno crece en un lugar y no invade otros tejidos. Un tumor maligno invade tejidos vecinos y puede enviar células a otras partes del cuerpo; eso es el cáncer. El cáncer no se contagia de una persona a otra.",
      "Las mutaciones pueden aparecer por errores al copiar el ADN o por agentes como la radiación ultravioleta sin protección o el humo del tabaco; algunas se heredan. Una mutación en una célula del cuerpo se transmite a sus células hijas por mitosis, pero no a los hijos de la persona. Solo una mutación en un gameto puede pasar a la siguiente generación.",
      "Una trisomía es la presencia de tres copias de un cromosoma en lugar de dos. Ocurre cuando, en la meiosis, un par de cromosomas no se separa bien y un gameto queda con uno de más. Si ese gameto se une con uno normal, el cigoto tiene un cromosoma extra. En la trisomía 21 hay 47 cromosomas, en lugar de 46. Las anomalías cromosómicas son una variación biológica, y cada persona necesita apoyo de profesionales de salud según su caso.",
  ],
  vocab=[("mutación", "cambio en el ADN"), ("tumor", "masa de células que se dividieron en exceso"), ("cáncer", "enfermedad en que células con división sin control invaden otros tejidos"), ("trisomía", "presencia de tres copias de un cromosoma en lugar de dos"), ("no disyunción", "falla en que un par de cromosomas no se separa en la meiosis")],
  worked=[
      ("De la mutación al tumor", "Una célula de ejemplo sufre una mutación que anula un gen que frena la división. Explica qué podría ocurrir.", ["Sin ese freno, la célula se divide cuando no corresponde.", "Sus hijas heredan la mutación por mitosis y también se dividen sin control.", "Con el tiempo se forma una masa de células: un tumor."], "La célula y sus descendientes se dividen sin control y pueden formar un tumor"),
      ("Contar cromosomas en una trisomía", "Un gameto de ejemplo de una especie con 10 cromosomas en el cuerpo tiene 6 cromosomas en lugar de 5 y se une a un gameto normal. ¿Cuántos cromosomas tiene el cigoto?", ["El gameto normal aporta 5.", "El gameto con un cromosoma de más aporta 6.", "5 + 6 = 11, es decir uno más que lo normal."], "El cigoto tiene 11 cromosomas"),
  ],
  mistakes=[
      ("Creer que el cáncer se contagia por estar cerca de una persona.", "Surge de mutaciones en las propias células de la persona y no pasa por contacto.", "No hay contagio; ante dudas se consulta a un profesional de salud."),
      ("Decir que una mutación en la piel se hereda a los hijos.", "Solo se heredan las mutaciones presentes en los gametos.", "Pregunta: ¿la mutación está en un gameto o en una célula del cuerpo?"),
  ],
  rec=[
      ("¿Cómo se llama una masa de células que se dividieron en exceso?", "Tumor", "Es el resultado de una división descontrolada."),
      ("Verdadero o falso: el cáncer se contagia por estar cerca de una persona.", "Falso", "Surge de mutaciones en las propias células."),
      ("¿Cuántos cromosomas tiene una persona con trisomía 21?", "47", "Tiene tres copias del cromosoma 21, uno más que lo habitual."),
  ],
  und=[
      ("¿Qué tipo de tumor invade tejidos vecinos? A) El maligno; B) El benigno.", "A", "La invasión es característica de un tumor maligno."),
      ("¿Qué falla en el cáncer? A) Se pierde el control de la división celular; B) Las células dejan de dividirse.", "A", "Las células se dividen sin los frenos normales."),
      ("¿Qué origina una trisomía? A) Un par de cromosomas que no se separa bien en la meiosis; B) Un exceso de mitosis en la piel.", "A", "La falla en la meiosis deja un gameto con un cromosoma de más."),
  ],
  app=[
      arith("Un gameto de ejemplo con 24 cromosomas se une a un gameto normal de 23. ¿Cuántos cromosomas tiene el cigoto?", "24+23", "Se suman los cromosomas de ambos gametos."),
      arith("Una célula con una mutación se divide 4 veces seguidas por mitosis y todas las hijas conservan la mutación. ¿Cuántas células con la mutación hay?", "2*2*2*2", "Cada ronda duplica las células y todas la conservan."),
      ("Una mutación aparece en una célula de la piel de una persona de ejemplo. ¿Se hereda a sus hijos? A) No, porque no está en un gameto; B) Sí, siempre.", "A", "Solo las mutaciones de los gametos pasan a la descendencia."),
  ],
  rea=[
      ("Un compañero dice: «Mi vecina tiene cáncer; si me acerco, me contagio». ¿Qué le responderías? A) El cáncer no se contagia por cercanía, nace de mutaciones propias; B) Tiene razón, pasa por el aire.", "A", "No se trasmite por contacto ni por el aire."),
      ("Un tumor de ejemplo se mantiene en un solo lugar, rodeado de una cubierta, sin invadir tejidos. ¿Cómo se clasifica por esa característica? A) Benigno; B) Maligno.", "A", "No invade otros tejidos, rasgo del tumor benigno; igual debe evaluarlo un profesional."),
  ],
  cha=[
      ("¿Por qué una mutación que daña un gen que frena la división favorece un tumor? A) Porque la célula se divide sin el freno normal; B) Porque la célula deja de copiar su ADN.", "A", "Sin freno, las divisiones continúan sin control."),
      ("¿Por qué una mutación en un gameto importa para la herencia y una en la piel no? A) El gameto participa en la fecundación y la célula de la piel no; B) Porque las mutaciones de la piel se corrigen siempre.", "A", "Solo el gameto aporta ADN al hijo."),
  ],
  context=[arith("Una persona de ejemplo con trisomía 21 tiene 47 cromosomas. ¿Cuántos cromosomas más que el número habitual de 46 tiene?", "47-46", "Se resta el número habitual al observado.")],
  selfcheck=[("¿Qué es un tumor?", "Una masa de células que se dividieron en exceso", "Puede ser benigno o maligno."), ("¿Qué diferencia a un tumor maligno de uno benigno?", "El maligno invade otros tejidos", "El benigno no los invade."), ("¿Cómo se origina una trisomía?", "Por un par de cromosomas que no se separa en la meiosis", "Un gameto queda con un cromosoma extra.")],
  open_task=task("Elige uno de estos dos casos ficticios y explícalo en tres o cuatro oraciones. Caso 1: una célula de ejemplo muta en un gen que frena la división y forma un tumor. Caso 2: un gameto de ejemplo recibe un cromosoma de más. Indica la causa, la consecuencia y escribe una oración que diga a quién se debe consultar ante dudas de salud.", "Caso 2: en la meiosis un par de cromosomas no se separó y el gameto quedó con uno de más. Al unirse con un gameto normal el cigoto tiene un cromosoma extra: es una trisomía. Ante dudas de salud se consulta a un profesional de salud.", ["explica la causa con el proceso correcto", "indica la consecuencia", "incluye la consulta a un profesional"], ["explicación de tres oraciones"], ["decir que el cáncer se contagia", "confundir mutación del cuerpo con mutación de un gameto"], "Pregunta qué diferencia habría si la mutación del caso 1 estuviera en un gameto."),
  reinforce="Escribe tres diferencias entre un tumor benigno y uno maligno.",
  extend="Explica por qué una mutación en una célula de la piel no afecta a los hijos de la persona.")

L(OA6, 6,
  materials="Este cuaderno y lápiz. Los casos son ficticios; no reemplazan una consulta de salud.",
  use="Aprenderé a evaluar afirmaciones sobre cáncer y trisomías, a distinguir lo que un dato permite concluir de lo que no, y a nombrar conductas de cuidado. Sirve para decidir con criterio y avisar a un adulto cuando hay dudas de salud.",
  prior=["Sé qué es un tumor, el cáncer y una trisomía.", "Sé que un dato de una muestra tiene límites."],
  explain=[
      "Una afirmación científica se evalúa con evidencia. Un estudio puede mostrar que dos cosas aparecen juntas, pero eso no siempre prueba que una cause la otra. Para sostener una causa se necesitan varios estudios, grupos comparables y un mecanismo que lo explique. Los datos de ejemplo de esta clase sirven para practicar el razonamiento, no para conocer riesgos reales.",
      "Hay medidas de cuidado que reducen el riesgo de dañar el ADN o detectar a tiempo un problema: protegerse de la radiación ultravioleta con sombra, sombrero y filtro solar, evitar el humo del tabaco y asistir a los controles de salud que indica un profesional. Ningún modelo, dibujo o artículo de internet permite diagnosticar a una persona. Si alguien siente un cambio en su cuerpo o tiene dudas, debe hablar con una persona adulta de confianza y consultar a un profesional de salud.",
      "Los modelos de mitosis, meiosis y cáncer tienen límites: simplifican procesos muy complejos y no muestran todas las causas. Además, hay avisos engañosos que prometen curas rápidas con productos sin evidencia. Una fuente confiable cita datos, explica cómo se obtuvieron y reconoce sus límites.",
  ],
  vocab=[("evidencia", "datos que apoyan o rechazan una afirmación"), ("correlación", "dos cosas que aparecen juntas sin que una cause necesariamente la otra"), ("fuente confiable", "fuente que explica cómo obtuvo sus datos y reconoce sus límites"), ("prevención", "acciones para reducir un riesgo"), ("profesional de salud", "persona formada para evaluar y tratar problemas de salud")],
  worked=[
      ("Evaluar una afirmación", "Datos de ejemplo: de 100 personas que usaron sombrero y filtro solar, 10 tuvieron lesiones en la piel; de 100 que no los usaron, 30. Un aviso dice: «El sombrero cura el cáncer». ¿Qué permite concluir el dato?", ["Entre quienes se protegieron hubo menos lesiones: 10 contra 30.", "El dato compara prevención de lesiones; no habla de curar.", "Eso respalda la protección, pero no la frase «cura»."], "Respalda que protegerse se asocia a menos lesiones; no prueba una cura"),
      ("Reconocer un límite", "Un estudio de ejemplo tuvo solo 20 personas. ¿Qué límite tiene?", ["Con pocas personas el resultado puede cambiar mucho en otra muestra.", "No se puede generalizar a toda la población."], "El tamaño pequeño impide generalizar"),
  ],
  mistakes=[
      ("Creer que dos cosas que aparecen juntas siempre se causan entre sí.", "Puede haber otra causa o ser casualidad; se necesita más evidencia.", "Pregunta: ¿hay otro factor o un mecanismo que lo explique?"),
      ("Confiar en un aviso que promete una cura rápida sin datos.", "Una fuente confiable muestra cómo obtuvo sus datos.", "Busca fuentes que citen datos y consulta a un profesional."),
  ],
  rec=[
      ("¿A quién se consulta ante una duda de salud?", "A un profesional de salud", "Solo un profesional puede evaluar a una persona."),
      ("Verdadero o falso: un dibujo de un modelo permite diagnosticar a una persona.", "Falso", "Los modelos simplifican y no reemplazan el examen de un profesional."),
      ("Nombra una conducta que protege la piel de la radiación ultravioleta.", "Usar filtro solar, sombrero o buscar sombra", "Reduce el daño al ADN de las células de la piel."),
  ],
  und=[
      ("Dos cosas aparecen juntas en un estudio. ¿Qué se puede decir sin más datos? A) Están asociadas, pero no se prueba que una cause la otra; B) Una causa a la otra con seguridad.", "A", "Una asociación no basta para probar causa."),
      ("¿Qué rasgo tiene una fuente confiable? A) Explica cómo obtuvo sus datos y reconoce sus límites; B) Promete resultados rápidos y seguros.", "A", "La transparencia sobre los datos y límites da confianza."),
      ("¿Qué acción es prevención? A) Usar sombrero y filtro solar; B) Esperar a que aparezca un síntoma sin hacer nada.", "A", "La prevención reduce el riesgo antes del daño."),
  ],
  app=[
      arith("En un grupo de ejemplo de 100 personas sin protección solar hubo 28 con lesiones en la piel, y en otro de 100 con protección hubo 12. ¿Cuántas lesiones más hubo en el grupo sin protección?", "28-12", "Se resta el grupo con protección del grupo sin protección."),
      arith("Un estudio de ejemplo observó 4 grupos de 25 personas. ¿Cuántas personas participaron en total?", "4*25", "Se multiplica el número de grupos por las personas de cada grupo."),
      ("Un aviso dice que un jugo «elimina tumores» y no muestra datos. ¿Qué haces? A) Desconfiar y consultar a un profesional de salud; B) Reemplazar el tratamiento indicado por el jugo.", "A", "Sin datos no hay evidencia, y el tratamiento lo define un profesional."),
  ],
  rea=[
      ("Una amiga dice que una persona de su familia enfermó porque «le dieron mala suerte». ¿Qué respuesta usa mejor la evidencia? A) Hay varios factores posibles y solo un profesional puede evaluar el caso; B) Seguro fue un solo hecho.", "A", "La enfermedad suele tener varias causas y el caso lo evalúa un profesional."),
      ("Un estudio de ejemplo con 15 personas concluye que un hábito «previene el cáncer en todo el mundo». ¿Qué falla tiene? A) La muestra es pequeña para generalizar; B) El estudio debió preguntar solo a personas que ya tenían el hábito.", "A", "Una muestra pequeña no permite concluir sobre toda la población."),
  ],
  cha=[
      arith("En un grupo A de ejemplo hubo 6 casos entre 50 personas. Con esa misma proporción, ¿cuántos casos esperarías en un grupo de 100 personas?", "6*2", "100 es el doble de 50, así que se duplican los casos esperados."),
      ("¿Qué mensaje final es más responsable en un afiche de prevención? A) Protégete, infórmate y consulta a un profesional de salud ante dudas; B) Con este producto no necesitas ir al médico.", "A", "Un mensaje responsable promueve prevención y consulta profesional."),
  ],
  context=[arith("En un estudio de ejemplo, 3 de cada 10 personas sin protección solar tuvieron lesiones. De 200 personas de ejemplo sin protección, ¿cuántas tendrían lesiones con esa proporción?", "200//10*3", "Se calcula cuántos grupos de 10 hay y se multiplica por 3.")],
  selfcheck=[("¿Qué significa que dos cosas estén asociadas?", "Que aparecen juntas sin probar que una cause la otra", "Se necesita más evidencia para hablar de causa."), ("Nombra un límite de un estudio con pocas personas.", "No permite generalizar", "Otra muestra podría dar otro resultado."), ("¿Qué hace una persona ante un cambio en su cuerpo o una duda de salud?", "Habla con un adulto de confianza y consulta a un profesional de salud", "Solo un profesional puede evaluar.")],
  open_task=task("Lee este aviso de ejemplo: «Descubre el polvo milagroso: elimina el cáncer en una semana, sin médicos». Escribe una evaluación de tres oraciones: qué evidencia faltaría, qué límite tendría el aviso y qué mensaje de cuidado dirías a una persona de tu edad.", "Faltan datos que muestren cómo se probó el polvo. El aviso exagera con «una semana» y no reconoce límites. Mensaje: ante dudas de salud, hablar con un adulto de confianza y consultar a un profesional de salud.", ["pide evidencia", "reconoce una exageración", "incluye consulta a adulto y profesional"], ["tres oraciones"], ["aceptar la promesa sin datos", "no mencionar al profesional de salud"], "Pregunta qué datos pedirías para creerle a un producto."),
  reinforce="Escribe dos diferencias entre «asociado» y «causa».",
  extend="Explica por qué un modelo de la mitosis no sirve para diagnosticar a una persona.")

# ---------------------------------------------------------------- OA 07

L(OA7, 1,
  materials="Este cuaderno y lápiz. Todos los casos están escritos en los ejercicios.",
  use="Aprenderé el lenguaje básico de la herencia de Mendel (gen, alelo, dominante, recesivo, genotipo y fenotipo) y a plantear preguntas que se puedan contestar con cruces. Sirve para predecir rasgos de plantas y animales.",
  prior=["Sé que los gametos tienen la mitad de los cromosomas.", "Sé que el material genético pasa de padres a hijos."],
  explain=[
      "En el siglo XIX, Gregor Mendel estudió la herencia cruzando plantas de guisante. Observó rasgos que se podían clasificar con claridad, como flor violeta o flor blanca, o semilla lisa o rugosa. Un gen es una porción de ADN que influye en un rasgo. Cada individuo tiene dos alelos de cada gen, uno que viene de cada progenitor. Los alelos son las versiones de un gen.",
      "Cuando los dos alelos son distintos, a veces uno de ellos domina: es el alelo dominante y se escribe con mayúscula, por ejemplo P para flor violeta. El otro es el alelo recesivo y se escribe con minúscula, p para flor blanca. El genotipo son los alelos que tiene un individuo (PP, Pp o pp). El fenotipo es el rasgo que se observa. Un individuo es homocigoto si tiene dos alelos iguales y heterocigoto si tiene dos distintos.",
      "Una pregunta investigable sobre herencia indica qué cruce se hace y qué se cuenta. «¿Qué proporción de las plantas hijas tiene flor blanca si se cruzan dos plantas Pp?» se contesta contando plantas. «¿Qué planta es más bonita?» no se puede investigar. Los principios de Mendel valen también para animales: todos los organismos de reproducción sexual heredan un alelo de cada progenitor.",
  ],
  vocab=[("gen", "porción de ADN que influye en un rasgo"), ("alelo", "cada versión de un gen"), ("genotipo", "los alelos que tiene un individuo"), ("fenotipo", "el rasgo que se observa"), ("homocigoto", "individuo con dos alelos iguales")],
  worked=[
      ("Genotipo y fenotipo", "En el guisante, G es el alelo dominante de semilla amarilla y g el recesivo de semilla verde. Una planta es Gg. Indica su fenotipo y si es homocigota o heterocigota.", ["Tiene un alelo G y uno g: son distintos, por eso es heterocigota.", "El alelo dominante G se expresa.", "El fenotipo es semilla amarilla."], "Fenotipo: semilla amarilla; heterocigota"),
      ("Mejorar una pregunta", "Mejora la pregunta «¿Es mejor la flor violeta?» para que se pueda investigar.", ["Quito la palabra de opinión «mejor».", "Indico el cruce: dos plantas Pp.", "Indico qué se cuenta: cuántas plantas hijas tienen flor blanca."], "«¿Cuántas plantas hijas tienen flor blanca al cruzar dos plantas Pp?»"),
  ],
  mistakes=[
      ("Decir que el alelo recesivo desaparece cuando hay un dominante.", "El recesivo sigue presente en el genotipo, pero no se expresa si hay un dominante.", "Distingue entre lo que se tiene (genotipo) y lo que se ve (fenotipo)."),
      ("Confundir genotipo con fenotipo.", "El genotipo son los alelos y el fenotipo es el rasgo observable.", "Pregunta: ¿hablo de letras o de lo que se ve?"),
  ],
  rec=[
      ("En la notación de Mendel, ¿qué letra representa un alelo recesivo: P o p?", "p", "El alelo recesivo se escribe con minúscula."),
      ("Una planta tiene genotipo Pp. ¿Es homocigota o heterocigota?", "Heterocigota", "Tiene dos alelos distintos."),
      ("Verdadero o falso: un alelo dominante se expresa aunque el otro alelo sea distinto.", "Verdadero", "Eso es lo que significa dominante."),
  ],
  und=[
      ("Una planta es pp. ¿Qué fenotipo tiene? A) Flor blanca; B) Flor violeta.", "A", "Con dos alelos recesivos se expresa el rasgo recesivo."),
      ("¿Cuántos alelos de un mismo gen tiene un guisante?", "Dos", "Hereda uno de cada progenitor."),
      ("¿Qué es el fenotipo? A) El rasgo que se observa; B) Los alelos que tiene el individuo.", "A", "El genotipo son los alelos; el fenotipo es lo observable."),
  ],
  app=[
      ("Una planta es LL, con L alelo dominante de semilla lisa. ¿Qué fenotipo tiene? A) Semilla lisa; B) Semilla rugosa.", "A", "El alelo dominante se expresa."),
      ("Una planta de genotipo Ll, donde l es el recesivo de semilla rugosa, tiene A) semilla lisa; B) semilla rugosa.", "A", "El alelo dominante L se expresa."),
      arith("Un estudio observa 3 genes distintos en un guisante. ¿Cuántos alelos en total tiene la planta?", "3*2", "Tiene dos alelos de cada gen."),
  ],
  rea=[
      ("Una planta tiene flor violeta. ¿Se puede saber con certeza su genotipo? A) No, puede ser PP o Pp; B) Sí, es PP.", "A", "Dos genotipos distintos dan el mismo fenotipo."),
      ("Un compañero dice: «El alelo recesivo se pierde en la planta Pp». ¿Qué le responderías? A) Sigue presente y se puede pasar a los hijos; B) Tiene razón, desaparece.", "A", "El alelo recesivo no desaparece, solo no se expresa."),
  ],
  cha=[
      ("Una planta de semilla amarilla puede tener dos genotipos, con Y dominante e y recesivo. ¿Cuáles son?", "YY o Yy", "Ambos expresan el alelo dominante."),
      ("¿Cuál es una pregunta investigable? A) ¿Qué proporción de plantas de semilla rugosa resulta de cruzar dos plantas Ll?; B) ¿Qué semilla es más rica?", "A", "Indica el cruce y qué se cuenta."),
  ],
  context=[arith("En un conteo de ejemplo de 40 plantas hijas, 10 tienen flor blanca y el resto flor violeta. ¿Cuántas tienen flor violeta?", "40-10", "Se resta las blancas del total.")],
  selfcheck=[("¿Qué es un alelo?", "Cada versión de un gen", "Cada individuo tiene dos alelos de cada gen."), ("¿Cómo se escribe un alelo recesivo?", "Con letra minúscula", "El dominante va con mayúscula."), ("¿Qué diferencia hay entre genotipo y fenotipo?", "El genotipo son los alelos y el fenotipo es el rasgo observable", "Uno son letras y el otro es lo que se ve.")],
  open_task=task("Estos son tres guisantes de ejemplo: Pp, pp y PP (P violeta dominante, p blanca recesiva). Escribe para cada uno su fenotipo y si es homocigoto o heterocigoto. Luego escribe una pregunta investigable sobre un cruce que indique qué se cuenta.", "Pp: violeta, heterocigoto. pp: blanca, homocigoto. PP: violeta, homocigoto. Pregunta: «¿Cuántas plantas hijas tienen flor blanca al cruzar dos plantas Pp?»", ["clasifica bien los tres genotipos", "no confunde genotipo con fenotipo", "la pregunta indica cruce y qué se cuenta"], ["tres filas y una pregunta"], ["decir que Pp tiene flor blanca", "escribir una pregunta de opinión"], "Pregunta qué cruce haría que ninguna planta hija fuera blanca."),
  reinforce="Escribe con tus palabras la diferencia entre homocigoto y heterocigoto.",
  extend="Explica por qué dos plantas de flor violeta pueden tener genotipos distintos.")

L(OA7, 2,
  materials="Este cuaderno y lápiz. Los conteos son de ejemplo y están escritos en los ejercicios.",
  use="Aprenderé a leer los datos de un cruce de Mendel, a calcular proporciones y a decidir si se acercan a 3:1. Sirve para sostener una explicación de la herencia con datos.",
  prior=["Sé qué son alelo, genotipo y fenotipo.", "Sé calcular sumas y divisiones enteras."],
  explain=[
      "Mendel partió de líneas puras, plantas homocigotas que siempre dan el mismo rasgo. Al cruzar una planta de flor violeta PP con una de flor blanca pp, todas las plantas hijas, llamadas generación F1, salieron con flor violeta, y eran Pp. Al cruzar entre sí las plantas de F1, en la siguiente generación, F2, reapareció la flor blanca en una parte de las plantas.",
      "En F2 contó las plantas de cada fenotipo y calculó su razón: aproximadamente 3 plantas con rasgo dominante por cada 1 con rasgo recesivo, es decir una razón 3:1. Eso significa que 3 de cada 4 plantas muestran el rasgo dominante. Si hay 80 plantas, se esperan 60 y 20. Para obtener la razón se divide el número de plantas dominantes por el de recesivas.",
      "Los conteos reales casi nunca dan exactamente 3:1, porque la unión de los gametos ocurre al azar. Con pocas plantas, la diferencia con lo esperado puede ser grande; con muchas plantas, el resultado se acerca más a 3:1. Por eso una buena explicación usa muchos datos y dice qué tan cerca están de lo esperado.",
  ],
  vocab=[("generación F1", "primeros descendientes de un cruce entre líneas puras"), ("generación F2", "descendientes del cruce entre plantas de F1"), ("línea pura", "grupo de individuos homocigotos que dan siempre el mismo rasgo"), ("razón", "comparación entre dos cantidades, como 3:1"), ("valor esperado", "cantidad que se predice con el modelo")],
  worked=[
      ("Calcular una razón", "Conteo de ejemplo en F2: 90 plantas de flor violeta y 30 de flor blanca. Calcula la razón y di si se acerca a 3:1.", ["Razón: 90 ÷ 30 = 3.", "Eso es 3 violeta por cada 1 blanca, es decir, 3:1.", "El conteo coincide con lo esperado."], "La razón es 3:1; coincide con lo esperado"),
      ("Comparar con lo esperado", "En otro conteo de ejemplo hay 61 plantas violeta y 19 blancas. ¿Qué se espera y qué tan cerca está?", ["Total: 61 + 19 = 80. Se esperan 3/4 violeta y 1/4 blanca.", "Esperado: 60 violeta y 20 blancas.", "Hay 1 más y 1 menos: está muy cerca."], "Se esperan 60 y 20; el conteo está muy cerca"),
  ],
  mistakes=[
      ("Esperar que un conteo real dé exactamente 3:1.", "La unión de gametos ocurre al azar, por lo que hay pequeñas diferencias.", "Compara con lo esperado y juzga si la diferencia es pequeña."),
      ("Creer que 3:1 significa 3 plantas en total.", "Significa 3 por cada 1, es decir 3 de cada 4.", "Piensa en grupos de 4 plantas."),
  ],
  rec=[
      ("¿Cómo se llama la primera generación de hijos de dos líneas puras?", "F1", "Son los primeros descendientes del cruce."),
      ("En F1 de un cruce PP × pp, ¿qué fenotipo tienen todas las plantas?", "Violeta", "Todas son Pp y el alelo dominante se expresa."),
      ("Verdadero o falso: una razón 3:1 significa que 3 de cada 4 plantas muestran el rasgo dominante.", "Verdadero", "3 más 1 son 4 plantas por cada grupo."),
  ],
  und=[
      ("¿Qué razón se espera en F2 de un cruce de un solo gen entre plantas Pp? A) 3:1; B) 1:1.", "A", "Tres de cada cuatro plantas muestran el rasgo dominante."),
      ("¿Por qué los conteos reales no son exactamente 3:1? A) Porque la unión de gametos ocurre al azar; B) Porque la ley de Mendel no sirve.", "A", "El azar produce pequeñas diferencias."),
      ("¿Qué son las líneas puras de Mendel?", "Plantas homocigotas que siempre dan el mismo rasgo", "Sirven como punto de partida confiable."),
  ],
  app=[
      arith("En F2 de ejemplo hubo 48 plantas de semilla amarilla y 16 de semilla verde. ¿Cuántas plantas hay en total?", "48+16", "Se suman las plantas de los dos fenotipos."),
      arith("De 160 plantas de F2 de ejemplo, se espera que 3/4 tengan semilla lisa. ¿Cuántas se esperan?", "160//4*3", "Se divide por 4 y se multiplica por 3."),
      ("Un conteo de ejemplo da 55 plantas violeta y 5 blancas. ¿Se acerca a 3:1? A) No, para 60 plantas se esperarían 45 y 15; B) Sí, porque hay más violetas que blancas.", "A", "Hay demasiadas violetas respecto de lo esperado."),
  ],
  rea=[
      ("Un grupo cuenta solo 20 plantas de F2 y obtiene 12 violeta y 8 blancas. Dice que la ley de Mendel es falsa. ¿Qué respuesta es mejor? A) Con pocas plantas el azar pesa mucho; conviene contar más; B) Tiene razón, la ley falla.", "A", "Una muestra pequeña puede alejarse de lo esperado."),
      ("¿Qué cambia si se cuentan muchas más plantas? A) Los resultados tienden a acercarse a 3:1; B) Los resultados se alejan de 3:1.", "A", "Con más datos el azar pesa menos."),
  ],
  cha=[
      arith("En 240 plantas de F2 de ejemplo se espera una razón 3:1. ¿Cuántas se esperan con el rasgo recesivo?", "240//4", "Una de cada cuatro tiene el rasgo recesivo."),
      ("Un conteo de ejemplo en F2 dio 100 plantas del rasgo dominante y 100 del recesivo. ¿Se acerca a 3:1? A) No, con 200 plantas se esperarían 150 y 50; B) Sí, porque los dos números son iguales.", "A", "Una razón 1:1 está lejos de la esperada 3:1."),
  ],
  context=[arith("Cuatro equipos de ejemplo contaron cada uno 50 plantas de F2, 200 en total. Si la razón es 3:1, ¿cuántas plantas con rasgo recesivo se esperan en total?", "200//4", "Una de cada cuatro tiene el rasgo recesivo.")],
  selfcheck=[("¿Qué plantas forman la generación F1?", "Las hijas del cruce de líneas puras", "Son el primer grupo de descendientes."), ("¿Qué razón se espera en F2 para un gen con dominancia?", "3:1", "Tres con el rasgo dominante por cada uno con el recesivo."), ("¿Por qué conviene contar muchas plantas?", "Porque con más datos el azar pesa menos", "Los resultados se acercan a lo esperado.")],
  open_task=task("Datos de ejemplo de F2 de un cruce Pp × Pp: 117 plantas violeta y 33 blancas. Calcula el total, cuántas violeta y blancas se esperarían con 3:1 y compara. Escribe una conclusión de dos oraciones; la segunda debe decir un límite.", "Total: 150. Esperado: 112 y 38 aproximadamente. El conteo es cercano a 3:1. Es un solo conteo, otro grupo podría obtener valores algo distintos por azar.", ["calcula el total correctamente", "compara con lo esperado", "declara un límite"], ["cálculos y dos oraciones"], ["exigir exactamente 3:1", "no declarar ningún límite"], "Pregunta cuántas plantas más contarías y por qué."),
  reinforce="Escribe una razón 3:1 con tus palabras y con un ejemplo de 12 plantas.",
  extend="Explica por qué Mendel necesitó contar muchas plantas para apoyar su explicación.")

L(OA7, 3,
  materials="Este cuaderno y lápiz. Dibujarás cuadros de cuatro casillas.",
  use="Aprenderé a construir un cuadro de Punnett para predecir los genotipos y fenotipos de un cruce. Sirve para saber qué proporciones esperar sin cruzar plantas.",
  prior=["Sé qué son genotipo, fenotipo, homocigoto y heterocigoto.", "Sé que la razón 3:1 se espera en F2."],
  explain=[
      "Un cuadro de Punnett es un modelo que combina los gametos de dos progenitores. Cada progenitor forma gametos con un solo alelo de cada gen. Un individuo Yy forma dos tipos de gametos, Y y y, en igual cantidad. Un individuo YY solo forma gametos Y. Para un gen, el cuadro tiene 4 casillas: los gametos de un progenitor van arriba y los del otro a un costado.",
      "Cada casilla muestra un genotipo posible de la descendencia. En un cruce Yy × Yy las casillas son YY, Yy, Yy y yy: el genotipo se reparte 1 YY : 2 Yy : 1 yy. Si Y es dominante, tres de las cuatro casillas tienen semilla amarilla y una tiene semilla verde: razón de fenotipos 3:1. En un cruce Yy × yy las casillas son Yy, Yy, yy y yy: la mitad amarilla y la mitad verde, razón 1:1.",
      "El cuadro predice probabilidades, no resultados exactos. Con cuatro hijos puede salir cualquier combinación; con muchos hijos se acerca más a lo predicho. También sirve para animales: si en una especie de ejemplo el pelaje oscuro N domina al claro n, se usa igual el cuadro. Un límite del modelo es que supone que los gametos se unen al azar y que el rasgo depende de un solo gen.",
  ],
  vocab=[("cuadro de Punnett", "tabla que combina los gametos de dos progenitores"), ("gameto", "célula sexual con un alelo de cada gen"), ("probabilidad", "posibilidad de que ocurra un resultado, como 1 de 4"), ("razón genotípica", "proporción de los distintos genotipos"), ("razón fenotípica", "proporción de los distintos fenotipos")],
  worked=[
      ("Cruce de dos heterocigotos", "En un animal de ejemplo, N es pelaje oscuro dominante y n pelaje claro. Se cruzan dos individuos Nn. Construye el cuadro y da las razones.", ["Cada progenitor forma gametos N y n.", "Casillas: NN, Nn, Nn y nn.", "Genotipos: 1 NN : 2 Nn : 1 nn. Fenotipos: 3 oscuros : 1 claro."], "Genotipos 1:2:1; fenotipos 3 oscuros : 1 claro"),
      ("Cruce con un homocigoto recesivo", "Se cruza una planta Rr (R semilla redonda dominante) con una rr (rugosa). Construye el cuadro.", ["Gametos de Rr: R y r. Gametos de rr: solo r.", "Casillas: Rr, Rr, rr y rr.", "Mitad redonda y mitad rugosa."], "Fenotipos 1 redonda : 1 rugosa"),
  ],
  mistakes=[
      ("Poner dos alelos en un gameto.", "Un gameto lleva un solo alelo de cada gen.", "Separa los dos alelos del progenitor: uno por gameto."),
      ("Decir que Pp × Pp da 2 violeta y 2 blancas.", "Las casillas son PP, Pp, Pp y pp: tres violetas y una blanca.", "Cuenta qué casillas tienen un alelo dominante."),
  ],
  rec=[
      ("¿Qué gametos forma un individuo Yy?", "Y y y", "Cada gameto lleva uno de los dos alelos."),
      ("¿Qué genotipo tienen todos los hijos de un cruce YY × yy?", "Yy", "Todos reciben un Y y un y."),
      ("Verdadero o falso: el cuadro de Punnett de un gen tiene 4 casillas.", "Verdadero", "Hay 2 tipos de gameto por cada progenitor, 2 por 2."),
  ],
  und=[
      ("En un cruce Pp × pp, ¿cuántas de las 4 casillas son pp? A) 2; B) 1.", "A", "Las casillas son Pp, Pp, pp y pp."),
      ("¿Qué tipos de gameto forma un individuo YY? A) Solo Y; B) Y y y.", "A", "Con dos alelos iguales todos los gametos son iguales."),
      ("¿Qué entrega un cuadro de Punnett? A) Probabilidades de la descendencia; B) El resultado exacto de cada cruce.", "A", "Predice proporciones, no resultados exactos."),
  ],
  app=[
      ("En un cruce Yy × Yy se obtienen las casillas YY, Yy, Yy y yy. ¿Cuántas casillas tienen semilla verde (yy)?", "1", "Solo una casilla tiene los dos alelos recesivos."),
      arith("De 80 descendientes esperados de un cruce Yy × Yy, un cuarto es yy. ¿Cuántos son yy?", "80//4", "Una casilla de cuatro corresponde a un cuarto."),
      arith("Dos animales Nn tienen 48 crías en total. Si se esperan 3 oscuras por cada 4, ¿cuántas crías oscuras se esperan?", "48//4*3", "Se divide por 4 y se multiplica por 3."),
  ],
  rea=[
      ("Un estudiante dice que un cruce Pp × Pp da 2 plantas violeta y 2 blancas. ¿Qué error tiene? A) Las casillas PP, Pp y Pp son violeta; solo una es blanca; B) Su cuadro está correcto.", "A", "Tres de las cuatro casillas tienen un alelo dominante."),
      ("Un cruce entre dos plantas da mitad dominante y mitad recesiva. ¿Cuál es el cruce más probable? A) Aa × aa; B) AA × aa.", "A", "AA × aa da solo Aa; Aa × aa da mitad y mitad."),
  ],
  cha=[
      ("Una planta de semilla amarilla (Y dominante) se cruza con una verde yy y salen mitad amarillas y mitad verdes. ¿Qué genotipo tiene la planta amarilla?", "Yy", "Si fuera YY todos los hijos serían amarillos."),
      ("En el cuadro de Pp × Pp, ¿cuántas casillas son heterocigotas?", "2", "Las casillas Pp y Pp son heterocigotas."),
  ],
  context=[arith("De 120 semillas de ejemplo de un cruce Yy × yy, la mitad es verde. ¿Cuántas semillas verdes se esperan?", "120//2", "Dos de las cuatro casillas son yy: la mitad.")],
  selfcheck=[("¿Cuántos alelos de un gen lleva un gameto?", "Uno", "El gameto lleva un solo alelo de cada gen."), ("¿Qué razón fenotípica da Aa × Aa?", "3:1", "Tres casillas con el dominante y una con el recesivo."), ("Nombra un límite del cuadro de Punnett.", "Solo predice probabilidades y supone un solo gen", "No da resultados exactos.")],
  open_task=task("Se cruzan dos plantas de ejemplo Tt, con T tallo alto dominante y t tallo bajo. Dibuja el cuadro de Punnett, escribe las razones de genotipos y de fenotipos y calcula cuántas plantas altas se esperan entre 80 hijas. Escribe un límite del modelo.", "Casillas: TT, Tt, Tt, tt. Genotipos 1:2:1; fenotipos 3 altas : 1 baja. De 80, se esperan 60 altas. Límite: el cuadro predice probabilidades y supone un solo gen.", ["el cuadro está bien construido", "las razones son correctas", "declara un límite"], ["cuadro, razones, un cálculo y una oración"], ["poner tt como alta", "olvidar el límite"], "Pregunta qué cruce de estas plantas no daría ninguna planta baja."),
  reinforce="Construye el cuadro de Aa × Aa y rotula los fenotipos.",
  extend="Explica por qué un cuadro de Punnett no dice qué hijos concretos tendrá una pareja de plantas.")

L(OA7, 4,
  materials="Este cuaderno y lápiz. Puedes dibujar cuadros de 16 casillas.",
  use="Aprenderé a relacionar los genotipos de los progenitores con las proporciones de los hijos, a usar el cruce de prueba y a calcular probabilidades de dos genes. Sirve para explicar herencia con varios rasgos.",
  prior=["Sé construir un cuadro de Punnett de un gen.", "Sé que una razón 3:1 se espera en Aa × Aa."],
  explain=[
      "Mendel propuso tres principios. El primero: los individuos de la primera generación de líneas puras son uniformes. El segundo, de segregación: los dos alelos de un gen se separan al formar los gametos. El tercero, de distribución independiente: los alelos de genes distintos se reparten sin influirse. Esto vale cuando los genes están en cromosomas distintos.",
      "Al estudiar dos genes a la vez, un individuo AaBb forma cuatro tipos de gameto: AB, Ab, aB y ab. En el cruce AaBb × AaBb el cuadro tiene 16 casillas y los fenotipos salen en la razón 9:3:3:1: 9 con ambos rasgos dominantes, 3 con uno dominante y otro recesivo, otros 3 al revés y 1 con ambos recesivos. También se pueden multiplicar probabilidades: si la probabilidad de un rasgo es 1 de 4 y la del otro es 1 de 2, la de ambos es 1 de 8.",
      "Para saber si un individuo de fenotipo dominante es homocigoto o heterocigoto se usa el cruce de prueba: se cruza con un homocigoto recesivo. Si todos los hijos muestran el rasgo dominante, el individuo era homocigoto. Si la mitad muestra el rasgo recesivo, era heterocigoto. Con pocos hijos la conclusión es débil, porque el azar puede engañar.",
  ],
  vocab=[("segregación", "separación de los dos alelos de un gen al formar gametos"), ("distribución independiente", "reparto de los alelos de genes distintos sin influirse"), ("dihíbrido", "cruce que estudia dos genes a la vez"), ("cruce de prueba", "cruce con un homocigoto recesivo para saber un genotipo"), ("independiente", "que un suceso no cambia la probabilidad del otro")],
  worked=[
      ("Multiplicar probabilidades", "En un cruce Aa × Aa la probabilidad de aa es 1 de 4. En otro gen, Bb × bb, la de bb es 1 de 2. ¿Cuál es la probabilidad de aabb si los genes son independientes?", ["Se multiplican las probabilidades de cada gen.", "El denominador es 4 × 2 = 8.", "La probabilidad es 1 de 8."], "1 de 8"),
      ("Cruce de prueba", "Una planta de flor violeta se cruza con una de flor blanca pp y da 10 hijas: 5 violeta y 5 blancas. ¿Qué genotipo tenía?", ["Las hijas blancas son pp: recibieron un p de la planta violeta.", "Entonces la planta violeta tenía un alelo p y es Pp.", "Mitad y mitad es lo esperado para Pp × pp."], "La planta violeta era heterocigota, Pp"),
  ],
  mistakes=[
      ("Suponer que un individuo AaBb forma solo dos tipos de gameto.", "Forma cuatro: AB, Ab, aB y ab, porque los genes se reparten de forma independiente.", "Combina cada alelo de un gen con cada alelo del otro."),
      ("Concluir el genotipo con un cruce de prueba de solo dos hijos.", "Con pocos hijos el azar puede engañar.", "Usa varios hijos antes de concluir."),
  ],
  rec=[
      arith("¿Cuántas casillas tiene el cuadro de Punnett de AaBb × AaBb?", "4*4", "Cada progenitor forma 4 tipos de gameto."),
      ("¿Qué razón de fenotipos se espera en un cruce dihíbrido AaBb × AaBb?", "9:3:3:1", "Es la razón de los cuatro fenotipos posibles."),
      ("Verdadero o falso: el cruce de prueba se hace con un homocigoto recesivo.", "Verdadero", "Así los alelos del otro individuo se hacen visibles."),
  ],
  und=[
      ("¿Qué afirma el principio de distribución independiente? A) Los alelos de genes distintos se reparten sin influirse; B) Los alelos de un gen se quedan siempre juntos.", "A", "Cada gen se reparte por separado cuando están en cromosomas distintos."),
      ("¿Por qué se multiplican probabilidades de dos genes? A) Porque los eventos son independientes; B) Porque hay que sumar todos los casos.", "A", "Si un evento no cambia al otro, se multiplican."),
      ("En un cruce de prueba todos los hijos muestran el rasgo dominante. ¿Qué genotipo tenía el progenitor evaluado? A) Homocigoto dominante; B) Heterocigoto.", "A", "Un heterocigoto daría hijos con el rasgo recesivo."),
  ],
  app=[
      arith("En AaBb × AaBb se esperan 9/16 con ambos rasgos dominantes. De 160 hijos de ejemplo, ¿cuántos se esperan con ambos dominantes?", "160//16*9", "Se divide por 16 y se multiplica por 9."),
      arith("Un gen da 1 de 4 con rasgo recesivo y otro gen da 1 de 4. ¿1 de cuántos tendrá ambos rasgos recesivos?", "4*4", "Se multiplican los denominadores."),
      ("Un cruce de prueba de ejemplo dio 14 hijas violeta y ninguna blanca. ¿Qué genotipo es más probable en la planta evaluada? A) PP; B) Pp.", "A", "Con ningún hijo recesivo y varios hijos, lo más probable es homocigoto dominante."),
  ],
  rea=[
      ("Un compañero ve un cruce de prueba con 6 hijos violeta y 6 blancos y concluye que la planta era PP. ¿Qué falla tiene? A) Los hijos blancos muestran que el progenitor tenía un alelo p; B) Los hijos blancos no dicen nada.", "A", "Para tener hijos pp, el progenitor debía llevar p."),
      ("En un conteo dihíbrido de 16 plantas salieron 10, 3, 2 y 1. ¿Qué conclusión es adecuada? A) Con pocas plantas hay desviaciones; conviene contar más; B) La razón 9:3:3:1 es falsa.", "A", "Con pocas plantas el azar produce desvíos."),
  ],
  cha=[
      arith("En la razón 9:3:3:1 hay 9 con ambos dominantes, 3 con uno, 3 con el otro y 1 con ambos recesivos. ¿Cuántas casillas de las 16 tienen al menos un rasgo dominante?", "9+3+3", "Se suman todas menos la casilla con ambos recesivos."),
      ("¿Cuándo se cumple la distribución independiente? A) Cuando los genes están en cromosomas distintos; B) Siempre, sin excepciones.", "A", "Genes muy cercanos en un mismo cromosoma tienden a heredarse juntos."),
  ],
  context=[arith("Un criador de ejemplo cruza 64 pares de animales AaBb × AaBb y quiere estimar cuántos hijos tendrán ambos rasgos recesivos (1 de 16). Si cada par tiene una cría, ¿cuántas crías con ambos rasgos recesivos se esperan?", "64//16", "Se espera 1 de cada 16 crías.")],
  selfcheck=[("¿Cuántos tipos de gameto forma AaBb?", "Cuatro", "AB, Ab, aB y ab."), ("¿Para qué sirve el cruce de prueba?", "Para saber si un individuo dominante es homocigoto o heterocigoto", "Se cruza con un homocigoto recesivo."), ("¿Qué razón se espera en un dihíbrido?", "9:3:3:1", "Es la proporción de los cuatro fenotipos.")],
  open_task=task("Se cruzan dos plantas AaBb de ejemplo, con A semilla amarilla y B semilla lisa dominantes, a verde y b rugosa recesivas. Escribe los cuatro tipos de gameto, cuántas casillas tiene el cuadro, la razón de fenotipos y cuántas plantas con ambos rasgos recesivos se esperan entre 96 hijas.", "Gametos: AB, Ab, aB y ab. 16 casillas. Fenotipos 9:3:3:1. De 96, 1 de cada 16: 6 plantas con semilla verde y rugosa.", ["escribe los cuatro gametos", "da la razón 9:3:3:1", "calcula 96 ÷ 16"], ["gametos, razón y un cálculo"], ["escribir solo dos gametos", "confundir 9:3:3:1 con 3:1"], "Pregunta qué cambia si los dos genes están muy cerca en el mismo cromosoma."),
  reinforce="Escribe los cuatro gametos de un individuo CcDd.",
  extend="Explica con un ejemplo por qué un cruce de prueba con pocos hijos no es concluyente.")

# ---------------------------------------------------------------- OA 08

L(OA8, 1,
  materials="Este cuaderno y lápiz. Los casos y datos están escritos en los ejercicios.",
  use="Aprenderé qué es la manipulación genética, qué aplicaciones tiene en alimentos, detergentes, vestuario y fármacos, y a distinguir una pregunta que se contesta con datos de una que depende de valores. Sirve para informarse sin caer en mitos.",
  prior=["Sé que el ADN contiene los genes que influyen en los rasgos.", "Sé que una pregunta investigable indica qué se mide."],
  explain=[
      "La manipulación genética es un conjunto de técnicas de laboratorio para cambiar o agregar ADN en un organismo. Un organismo modificado genéticamente recibió un gen de otro organismo o un cambio en su propio ADN. Esto permite que produzca una sustancia nueva o que tenga un rasgo nuevo, por ejemplo resistencia a una plaga.",
      "Hay aplicaciones en varios ámbitos. En fármacos, bacterias modificadas producen insulina humana para tratar la diabetes. En detergentes, se usan enzimas producidas por microorganismos que ayudan a sacar manchas. En vestuario, existen cultivos de algodón modificados para resistir insectos. En alimentos, hay plantas de cultivo con rasgos nuevos, como resistencia a una plaga. Cada producto debe evaluarse por separado.",
      "Las preguntas sobre estas técnicas son de dos tipos. Una pregunta empírica se contesta con datos, como «¿cuántos kilos por parcela rinde un cultivo modificado frente a uno convencional?». Una pregunta ética depende de valores y se discute entre personas, como «¿debe etiquetarse siempre un alimento modificado?». Ambas son importantes, pero se tratan distinto: la primera con mediciones y la segunda con argumentos y criterios. Al medir, la variable independiente es la que se cambia a propósito, por ejemplo con enzima o sin enzima en un detergente.",
  ],
  vocab=[("manipulación genética", "técnicas para cambiar o agregar ADN en un organismo"), ("organismo modificado genéticamente", "ser vivo al que se le cambió o agregó ADN"), ("transgénico", "organismo con un gen de otra especie"), ("pregunta empírica", "pregunta que se contesta con datos"), ("pregunta ética", "pregunta que depende de valores y se discute")],
  worked=[
      ("Clasificar una aplicación", "Una bacteria modificada produce una enzima que se agrega a un detergente para sacar manchas. ¿En qué ámbito está la aplicación?", ["La enzima se usa en un producto de limpieza.", "No se come ni se usa como medicina.", "El ámbito son los detergentes."], "Detergentes"),
      ("Distinguir tipos de pregunta", "Clasifica: «¿Cuántas plantas de una parcela sobreviven a una plaga con y sin el gen de resistencia?». ¿Es empírica o ética?", ["Indica qué se cuenta: plantas que sobreviven.", "Se compara con y sin el gen.", "Se puede contestar con datos: es empírica."], "Es una pregunta empírica"),
  ],
  mistakes=[
      ("Decir que todo producto modificado genéticamente es peligroso, o que ninguno lo es.", "Cada producto tiene rasgos, usos y riesgos distintos y se evalúa con evidencia.", "Pregunta: ¿qué gen se agregó, para qué y qué datos hay?"),
      ("Mezclar preguntas empíricas y éticas.", "Los datos no deciden por sí solos qué es correcto; también influyen los valores.", "Separa lo que se mide de lo que se discute."),
  ],
  rec=[
      ("¿Qué material se cambia o se agrega en la manipulación genética?", "El ADN", "Es el material genético del organismo."),
      ("Verdadero o falso: bacterias modificadas pueden producir insulina humana.", "Verdadero", "Es una aplicación en fármacos."),
      ("¿Cómo se llama el organismo al que se le cambió o agregó ADN?", "Organismo modificado genéticamente", "Es el término para organismos con ADN cambiado en laboratorio."),
  ],
  und=[
      ("Bacterias que producen una hormona para tratar la diabetes pertenecen al ámbito A) de los fármacos; B) de los detergentes.", "A", "La insulina es un fármaco."),
      ("Una enzima producida por microorganismos para ayudar a sacar manchas se usa en A) detergentes; B) fármacos.", "A", "Se agrega a productos de limpieza."),
      ("¿Cuál es una pregunta ética? A) ¿Debe informarse siempre en la etiqueta que un alimento es modificado?; B) ¿Cuántos kilos rinde una parcela?", "A", "Depende de valores como el derecho a informarse."),
  ],
  app=[
      ("Un algodón modificado para resistir insectos se usa en A) vestuario; B) detergentes.", "A", "El algodón es una fibra textil."),
      arith("Una parcela de ejemplo con cultivo modificado rindió 420 kg y una convencional 380 kg. ¿Cuántos kg más rindió la modificada?", "420-380", "Se resta el rendimiento convencional del modificado."),
      ("¿Cuál es una pregunta investigable sobre un cultivo con gen de resistencia a una plaga? A) ¿Cuántas plantas de 100 resisten la plaga con y sin el gen?; B) ¿Es bueno cambiar la naturaleza?", "A", "La que cuenta plantas con y sin el gen indica qué se cuenta y qué se compara."),
  ],
  rea=[
      ("Un compañero dice: «Todo lo modificado genéticamente es peligroso». ¿Qué respuesta usa mejor la evidencia? A) Hay que evaluar cada producto con datos; B) Tiene razón, siempre lo es.", "A", "Cada producto tiene un gen y un uso distintos."),
      ("¿Por qué la pregunta «¿es ético modificar un cultivo?» no se contesta solo con una medición? A) Porque también depende de valores; B) Porque los cultivos no tienen genes.", "A", "Las preguntas éticas se discuten con argumentos."),
  ],
  cha=[
      ("Para investigar si un detergente con una enzima quita más manchas, ¿cuál es la variable independiente? A) La presencia de la enzima; B) El color de la ropa.", "A", "Es lo que se cambia a propósito."),
      ("La pregunta «¿Cuántos kilos más rinde el maíz modificado que el convencional con el mismo riego?» es A) empírica; B) ética.", "A", "Se contesta con mediciones."),
  ],
  context=[arith("En una parcela de ejemplo había 60 plantas y una plaga dañó 15. ¿Cuántas plantas quedaron sin daño?", "60-15", "Se restan las dañadas del total.")],
  selfcheck=[("¿Qué es una manipulación genética?", "Cambiar o agregar ADN en un organismo con técnicas de laboratorio", "Permite nuevos rasgos o sustancias."), ("Nombra dos ámbitos donde se aplica.", "Fármacos y detergentes", "También alimentos y vestuario."), ("¿En qué se diferencian una pregunta empírica y una ética?", "La empírica se contesta con datos y la ética depende de valores", "Se tratan con métodos distintos.")],
  open_task=task("Lee estos tres casos de ejemplo: (1) bacterias que producen insulina; (2) un cultivo con resistencia a una plaga; (3) una enzima para detergentes. Para cada uno escribe el ámbito de la aplicación, una pregunta empírica y una pregunta ética.", "Caso 2: ámbito, alimentos. Pregunta empírica: «¿Cuántas plantas resisten la plaga con y sin el gen?». Pregunta ética: «¿Debe informarse en la etiqueta si el alimento viene de un cultivo modificado?»", ["clasifica bien el ámbito", "la pregunta empírica indica qué se mide", "la pregunta ética depende de valores"], ["tres filas con tres respuestas"], ["escribir como empírica una pregunta de opinión", "mezclar ámbitos"], "Pregunta qué dato necesitarías para contestar tu pregunta empírica."),
  reinforce="Escribe una pregunta empírica y una ética sobre el mismo producto.",
  extend="Explica por qué una pregunta ética no se contesta solo con datos.")

L(OA8, 2,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo y están escritas en los ejercicios.",
  use="Aprenderé a leer una tabla que compara un cultivo modificado con uno convencional, a calcular promedios y diferencias y a reconocer los límites de los datos. Sirve para evaluar afirmaciones con evidencia.",
  prior=["Sé qué es un organismo modificado genéticamente.", "Sé calcular un promedio y distinguir variables."],
  explain=[
      "Para evaluar un producto de la manipulación genética se compara con uno convencional bajo las mismas condiciones. Se miden variables como los kilos cosechados por parcela o las veces que se aplicó un producto contra plagas. Se mantienen iguales el tamaño de la parcela, el riego y el suelo. Cada parcela es una repetición, y con el promedio se resume el resultado.",
      "En una tabla de ejemplo, cada fila es una parcela y cada columna una variable. Se calcula el promedio de cada grupo y se resta para ver la diferencia. Una diferencia pequeña entre promedios, con datos muy variados, no permite concluir mucho. Una diferencia grande y constante en todas las parcelas da más confianza.",
      "Los datos tienen límites. Una temporada en un solo lugar no representa todos los climas ni todos los suelos. Además, conviene preguntar quién hizo el estudio y quién lo financió, y si otros equipos obtuvieron resultados parecidos. Una buena comunicación presenta los datos, el método y los límites sin exagerar.",
  ],
  vocab=[("repetición", "cada parcela o intento usado para medir lo mismo"), ("promedio", "suma de los datos dividida por la cantidad de datos"), ("grupo de comparación", "grupo que se mantiene sin el cambio para comparar"), ("fuente", "origen de un dato o de un estudio"), ("límite", "aspecto que impide generalizar un resultado")],
  worked=[
      ("Comparar promedios", "Tabla de ejemplo de rendimiento en kg por parcela. Modificado: 30, 34, 32. Convencional: 24, 26, 25. Calcula los promedios y la diferencia.", ["Modificado: 30 + 34 + 32 = 96; 96 ÷ 3 = 32.", "Convencional: 24 + 26 + 25 = 75; 75 ÷ 3 = 25.", "Diferencia: 32 − 25 = 7."], "Promedios 32 y 25; la diferencia es de 7 kg"),
      ("Reconocer un límite", "El estudio de ejemplo se hizo en un solo terreno durante una temporada. ¿Qué límite tiene?", ["Un terreno no representa todos los suelos.", "Una temporada no representa todos los climas."], "No permite generalizar a otros lugares ni temporadas"),
  ],
  mistakes=[
      ("Comparar sin mantener iguales el riego y el suelo.", "Si cambian otras variables, no se sabe qué produjo la diferencia.", "Controla las condiciones y cambia una sola variable."),
      ("Concluir con una sola parcela.", "Una parcela puede salir distinta por azar.", "Usa varias repeticiones y el promedio."),
  ],
  rec=[
      ("¿Qué se calcula para resumir varias parcelas en un solo valor?", "El promedio", "Resume las repeticiones."),
      ("Verdadero o falso: para comparar dos cultivos conviene mantener igual el riego.", "Verdadero", "Así la diferencia no se debe al riego."),
      ("En la tabla de ejemplo, ¿qué representa cada fila?", "Una parcela", "Cada fila es una repetición."),
  ],
  und=[
      ("Una diferencia grande y constante en todas las parcelas A) da más confianza que una diferencia pequeña y variable; B) no sirve para nada.", "A", "La constancia indica un efecto más claro."),
      ("¿Por qué conviene saber quién financió un estudio? A) Porque puede influir en lo que se destaca; B) Porque cambia los kilos cosechados.", "A", "Conocer la fuente ayuda a evaluar posibles intereses."),
      ("¿Qué es un grupo de comparación?", "El grupo que no recibe el cambio y sirve de referencia", "Permite ver el efecto del cambio."),
  ],
  app=[
      arith("Modificado: 52, 48, 50 y 54 kg. ¿Cuál es el promedio? (Datos de ejemplo.)", "(52+48+50+54)//4", "Se suman los cuatro datos y se divide por cuatro."),
      arith("El grupo modificado promedió 51 kg por parcela. El convencional rindió 40, 44, 42 y 46 kg. ¿Cuántos kg más promedió el modificado? (Datos de ejemplo.)", "51-(40+44+42+46)//4", "El promedio convencional es 43; se resta de 51."),
      ("La tabla de ejemplo muestra que el cultivo modificado necesitó 1 aplicación contra plagas y el convencional 4. ¿Qué variable se midió? A) Las veces que se aplicó el producto contra plagas; B) El tamaño de la parcela.", "A", "La variable medida es el número de aplicaciones."),
  ],
  rea=[
      ("Un aviso dice que un producto «aumenta la cosecha en todo el planeta» con datos de una parcela. ¿Qué falla tiene? A) Una parcela no permite generalizar a todo el planeta; B) El aviso debió medir en litros y no en kilos.", "A", "Es una muestra mínima y de un solo lugar."),
      ("Dos estudios dan resultados distintos sobre el mismo cultivo. ¿Qué conviene hacer? A) Revisar el método, las condiciones y la fuente de cada estudio; B) Quedarse con el que dice lo que uno quiere.", "A", "Comparar métodos y fuentes ayuda a explicar la diferencia."),
  ],
  cha=[
      arith("Una tabla de ejemplo tiene 6 parcelas con cultivo modificado, cada una de 5 kg más que su par convencional. ¿Cuántos kg más cosechó en total el grupo modificado?", "6*5", "Se suman las diferencias de las seis parcelas."),
      ("Un estudio de ejemplo concluye que un cultivo «no tiene ningún riesgo» midiendo solo el rendimiento. ¿Qué falla tiene? A) No midió otras variables, como el efecto en el ambiente; B) Midió demasiadas parcelas.", "A", "Una variable no basta para descartar riesgos."),
  ],
  context=[arith("En un ensayo de ejemplo, 4 parcelas modificadas dieron 61, 59, 63 y 65 kg. ¿Cuánto cosecharon en total?", "61+59+63+65", "Se suman los cuatro rendimientos.")],
  selfcheck=[("¿Por qué se usan varias parcelas?", "Para que el promedio no dependa del azar de una sola", "Cada parcela es una repetición."), ("Nombra una variable que se debe controlar al comparar cultivos.", "El riego", "También el suelo y el tamaño de la parcela."), ("¿Qué límite tiene un estudio de una temporada?", "No representa otras temporadas ni climas", "No se puede generalizar.")],
  open_task=task("Datos de ejemplo en kg por parcela. Modificado: 45, 47, 46, 50. Convencional: 38, 40, 39, 43. Calcula los dos promedios y la diferencia. Escribe una conclusión de dos oraciones; la segunda debe declarar un límite. Escribe también una pregunta para hacer a quien hizo el estudio.", "Promedios: 47 y 40; diferencia, 7 kg. El cultivo modificado rindió más en estas parcelas. Es un ensayo pequeño de una temporada. Pregunta: «¿Quién financió el estudio y se repitió en otros terrenos?»", ["calcula bien los promedios", "declara un límite", "plantea una pregunta sobre la fuente"], ["dos promedios, dos oraciones y una pregunta"], ["generalizar a todos los cultivos", "no preguntar por la fuente"], "Pregunta qué otras variables medirías además del rendimiento."),
  reinforce="Calcula el promedio de 20, 22 y 24 kg y explica qué representa.",
  extend="Explica por qué importa conocer la fuente y el método de un estudio.")

L(OA8, 3,
  materials="Este cuaderno y lápiz. Dibujarás un esquema de pasos con flechas.",
  use="Aprenderé el modelo de la tecnología del ADN recombinante, que muestra cómo se lleva un gen a una bacteria para que fabrique una sustancia. Sirve para ordenar los pasos y reconocer qué simplifica el modelo.",
  prior=["Sé qué son un gen y un organismo modificado genéticamente.", "Sé qué es un modelo y que tiene límites."],
  explain=[
      "El ADN recombinante es ADN formado al unir fragmentos de dos orígenes distintos. Para obtenerlo se usan enzimas de restricción, que cortan el ADN en lugares específicos. Se corta el ADN que tiene el gen de interés y se corta un plásmido, un pequeño ADN circular de las bacterias. Si se usa la misma enzima en ambos, los extremos cortados encajan.",
      "El modelo tiene cinco pasos. Primero se aísla el gen de interés. Segundo, se cortan el gen y el plásmido con la misma enzima. Tercero, se pegan el gen y el plásmido y se forma el ADN recombinante. Cuarto, se introduce ese plásmido en bacterias. Quinto, se cultivan las bacterias, que se multiplican y fabrican la sustancia codificada por el gen.",
      "Este modelo simplifica el proceso. No muestra que solo algunas bacterias reciben el plásmido, por lo que hay que seleccionarlas, ni que el gen debe quedar en un lugar donde la bacteria pueda leerlo. Un modelo sirve para predecir qué esperar: si el gen es de insulina, se espera que el cultivo produzca insulina; si no ocurre, se revisan los pasos.",
  ],
  vocab=[("ADN recombinante", "ADN formado al unir fragmentos de orígenes distintos"), ("enzima de restricción", "enzima que corta el ADN en lugares específicos"), ("plásmido", "pequeño ADN circular de las bacterias"), ("gen de interés", "gen que se quiere llevar a otro organismo"), ("cultivo", "conjunto de bacterias que crecen en un medio con alimento")],
  worked=[
      ("Ordenar los pasos", "¿Qué paso va después de pegar el gen en el plásmido?", ["Antes se aisló el gen, se cortaron el gen y el plásmido y se pegaron.", "Falta llevar el ADN recombinante al organismo.", "Se introduce en bacterias."], "Introducir el plásmido recombinante en bacterias"),
      ("Usar el modelo para predecir", "Se llevó el gen de una enzima de detergente a un cultivo de bacterias. ¿Qué se espera del cultivo?", ["Las bacterias reciben el gen en el plásmido.", "Se multiplican y leen el gen.", "Fabrican la enzima."], "Se espera que el cultivo produzca la enzima"),
  ],
  mistakes=[
      ("Creer que todas las bacterias reciben el plásmido.", "Solo algunas lo reciben; hay que seleccionarlas.", "Piensa que el modelo omite ese paso."),
      ("Usar enzimas distintas para cortar el gen y el plásmido.", "Con la misma enzima los extremos cortados encajan.", "Corta ambos con la misma enzima de restricción."),
  ],
  rec=[
      ("¿Cómo se llama el pequeño ADN circular de las bacterias que lleva el gen?", "Plásmido", "Sirve como vehículo para el gen."),
      ("¿Qué corta el ADN en lugares específicos?", "Una enzima de restricción", "Corta en sitios determinados."),
      ("Verdadero o falso: el ADN recombinante combina ADN de dos orígenes distintos.", "Verdadero", "Une fragmentos de procedencias diferentes."),
  ],
  und=[
      ("¿Qué paso va primero en el modelo? A) Aislar el gen de interés; B) Cultivar las bacterias.", "A", "Antes de todo se necesita el gen."),
      ("¿Qué función tiene el plásmido? A) Llevar el gen a la bacteria; B) Dar energía a la bacteria.", "A", "Funciona como vehículo para el gen."),
      ("¿Por qué se corta con la misma enzima? A) Para que los extremos encajen; B) Para que el ADN se destruya.", "A", "Extremos compatibles permiten pegar los fragmentos."),
  ],
  app=[
      ("Solo algunas bacterias reciben el plásmido. ¿Qué conviene hacer? A) Seleccionar las que lo recibieron; B) Usar todas sin revisar.", "A", "Solo las que lo recibieron fabricarán la sustancia."),
      arith("De 200 bacterias de ejemplo, 8 recibieron el plásmido. ¿Cuántas no lo recibieron?", "200-8", "Se restan las que lo recibieron del total."),
      ("Se lleva el gen de la insulina humana a bacterias. ¿Qué sustancia se espera que produzca el cultivo? A) Insulina; B) Enzima de detergente.", "A", "El cultivo fabrica lo que codifica el gen."),
  ],
  rea=[
      ("Se insertó el gen, pero el cultivo no produce la sustancia. ¿Qué pudo fallar? A) El gen quedó en una posición donde la bacteria no puede leerlo; B) El gen de interés era demasiado pequeño para funcionar.", "A", "Si el gen no queda bien ubicado, no se lee."),
      ("¿Qué limitación del modelo hay que declarar? A) No muestra que solo algunas bacterias reciben el plásmido; B) Muestra todo con exactitud.", "A", "Un modelo simplifica y omite pasos."),
  ],
  cha=[
      ("Ordena estos pasos: 1) Introducir el plásmido en bacterias; 2) Aislar el gen; 3) Cultivar las bacterias; 4) Insertar el gen en el plásmido. Escribe los números en orden.", "2, 4, 1, 3", "Primero el gen, luego el plásmido, después las bacterias y al final el cultivo."),
      ("Un equipo corta el gen con una enzima y el plásmido con otra que no encaja. ¿Qué esperarías? A) Que el gen no se pegue bien; B) Que se pegue perfectamente.", "A", "Los extremos no son compatibles."),
  ],
  context=[arith("En un laboratorio de ejemplo se preparan 5 tubos de cultivo y cada uno recibe 40 bacterias con plásmido. ¿Cuántas bacterias con plásmido hay en total?", "5*40", "Se multiplica la cantidad de tubos por las bacterias de cada uno.")],
  selfcheck=[("¿Qué es un plásmido?", "Un pequeño ADN circular de las bacterias", "Lleva el gen."), ("¿Qué hacen las enzimas de restricción?", "Cortan el ADN en lugares específicos", "Permiten abrir el plásmido y cortar el gen."), ("Nombra un límite del modelo.", "No muestra que solo algunas bacterias reciben el plásmido", "El modelo simplifica el proceso.")],
  open_task=task("Dibuja un esquema de cinco pasos con flechas para producir en bacterias una sustancia de ejemplo (la insulina). Rotula cada paso y escribe un límite del modelo y una predicción sobre qué se espera del cultivo.", "1 Aislar el gen de la insulina; 2 cortar gen y plásmido con la misma enzima; 3 pegarlos; 4 introducir el plásmido en bacterias; 5 cultivar. Predicción: el cultivo produce insulina. Límite: no muestra que solo algunas bacterias reciben el plásmido.", ["los cinco pasos están en orden", "incluye una predicción", "declara un límite"], ["esquema rotulado y dos oraciones"], ["cultivar antes de insertar el gen", "no declarar el límite"], "Pregunta qué paso revisarías si el cultivo no produce la sustancia."),
  reinforce="Escribe los cinco pasos del modelo con tus palabras.",
  extend="Explica por qué la misma enzima debe cortar el gen y el plásmido.")

L(OA8, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé a relacionar el tiempo de cultivo, el número de bacterias y la cantidad de producto, y a organizar beneficios, riesgos y grupos interesados en una tabla. Sirve para ordenar la información antes de evaluar un producto.",
  prior=["Sé que las bacterias se multiplican por división.", "Sé identificar variables independiente, dependiente y controladas."],
  explain=[
      "En un cultivo de bacterias modificadas, la cantidad de producto depende del número de bacterias y de cuánto produce cada una. Si cada bacteria se divide una vez por hora, el número se duplica en cada hora. Con 5 bacterias y 3 horas el número se multiplica por 2 tres veces. Si cada bacteria produce una cantidad fija, el producto total crece con el número de bacterias.",
      "Esta relación tiene un límite: el alimento y el espacio son finitos. Cuando se agotan, el cultivo deja de crecer y la curva se aplana. Por eso, al diseñar una investigación, se cambia una variable, por ejemplo el tiempo o la temperatura, y se miden las bacterias o el producto. Se mantienen iguales el tipo de bacteria y el alimento.",
      "Además de las variables del cultivo, hay variables sociales: quiénes se benefician, quiénes asumen riesgos y quiénes pagan. Una tabla de beneficios y riesgos por grupo interesado ayuda a ordenar la información antes de discutir. Un riesgo potencial no es un riesgo comprobado: se estudia con evidencia antes de concluir.",
  ],
  vocab=[("variable independiente", "la que se cambia a propósito"), ("variable dependiente", "la que se mide"), ("grupo interesado", "personas a quienes afecta una decisión"), ("beneficio", "efecto positivo esperado"), ("riesgo potencial", "posible daño que debe estudiarse")],
  worked=[
      ("Cultivo que se duplica", "Un cultivo de ejemplo parte con 4 bacterias que se duplican cada hora. ¿Cuántas hay a las 2 horas? Si cada una produce 3 unidades de producto, ¿cuántas unidades en total?", ["Hora 1: 4 × 2 = 8. Hora 2: 8 × 2 = 16.", "Producto: 16 × 3 = 48 unidades."], "16 bacterias y 48 unidades"),
      ("Tabla de grupos interesados", "Para un cultivo de ejemplo con resistencia a plagas, nombra un beneficio para agricultores y una pregunta de riesgo para estudiar.", ["Beneficio posible: menos aplicaciones contra plagas.", "Pregunta de riesgo: si el gen puede pasar a plantas silvestres cercanas.", "El riesgo se estudia con datos antes de concluir."], "Beneficio: menos aplicaciones; riesgo por estudiar: paso del gen a plantas silvestres"),
  ],
  mistakes=[
      ("Pensar que el cultivo crece sin límite.", "El alimento y el espacio se agotan y el crecimiento se detiene.", "Revisa qué recurso limita el crecimiento."),
      ("Tratar un riesgo potencial como si ya estuviera comprobado.", "Un riesgo potencial es algo que debe estudiarse con evidencia.", "Escribe «por estudiar» hasta tener datos."),
  ],
  rec=[
      arith("Si cada bacteria produce 3 unidades, ¿cuántas unidades producen 50 bacterias?", "50*3", "El total es el producto por bacteria multiplicado por el número de bacterias."),
      ("Verdadero o falso: un cultivo en un frasco con alimento limitado puede dejar de crecer.", "Verdadero", "Al agotarse el alimento, el crecimiento se detiene."),
      ("En un estudio del tiempo de cultivo sobre el número de bacterias, ¿cuál es la variable dependiente?", "El número de bacterias", "Es la que se mide."),
  ],
  und=[
      ("Si se mantienen iguales el alimento y el tipo de bacteria y solo cambia el tiempo, ¿cuál es la variable independiente? A) El tiempo; B) El tipo de bacteria.", "A", "Es lo que se cambia a propósito."),
      ("La curva de un cultivo sube y luego se aplana. ¿Qué lo explica mejor? A) Se agota un recurso limitante; B) Las bacterias dejan de necesitar alimento.", "A", "Sin alimento o espacio, el crecimiento se detiene."),
      ("¿Qué es un grupo interesado? A) Personas a quienes afecta una decisión; B) Un grupo de bacterias.", "A", "Son quienes se benefician o asumen riesgos."),
  ],
  app=[
      arith("Un cultivo de ejemplo parte con 10 bacterias que se duplican cada hora. ¿Cuántas hay después de 3 horas?", "10*2*2*2", "Se multiplica por 2 en cada hora."),
      arith("Cada una de las 80 bacterias de ejemplo produce 2 unidades de producto. ¿Cuántas unidades produce el cultivo?", "80*2", "Se multiplica el número de bacterias por lo que produce cada una."),
      ("Para probar si la temperatura cambia la producción, ¿qué se mantiene igual? A) El tipo de bacteria y el alimento; B) La temperatura.", "A", "Si se cambian otras variables, no se sabe qué produjo la diferencia."),
  ],
  rea=[
      ("Un gráfico de ejemplo muestra que la producción sube durante 6 horas y luego se mantiene igual. Un estudiante dice que las bacterias dejaron de tener genes. ¿Qué respuesta es mejor? A) Es más probable que un recurso se agotara; B) Tiene razón.", "A", "El aplanamiento suele deberse a límites de alimento o espacio."),
      ("Un aviso presenta solo beneficios de un producto y ningún riesgo posible. ¿Qué falla tiene? A) Muestra solo una parte de la información; B) Es demasiado largo.", "A", "Una evaluación incluye beneficios y riesgos por estudiar."),
  ],
  cha=[
      arith("El cultivo A parte con 6 bacterias y el B con 3. Ambos se duplican 4 veces. ¿Cuántas bacterias más tiene A que B al final?", "6*16-3*16", "A queda con 96 y B con 48."),
      ("Un cultivo de ejemplo produce más cuando la temperatura sube de 25 a 35 grados, pero se detiene a 50. ¿Qué conclusión es prudente? A) Hay un rango de temperatura favorable y no conviene extrapolar fuera de él; B) Más temperatura siempre produce más.", "A", "Los datos muestran un máximo y luego una caída."),
  ],
  context=[arith("Un tubo de cultivo de ejemplo produce 25 dosis. ¿Cuántas dosis producen 6 tubos iguales?", "6*25", "Se multiplica la cantidad de tubos por las dosis de cada uno.")],
  selfcheck=[("¿De qué depende el producto total de un cultivo?", "Del número de bacterias y de cuánto produce cada una", "Más bacterias y más producción por bacteria dan más producto."), ("¿Por qué un cultivo deja de crecer?", "Porque se agota el alimento o el espacio", "Los recursos son limitados."), ("¿Qué diferencia hay entre riesgo potencial y riesgo comprobado?", "El potencial debe estudiarse con evidencia", "Aún no se confirma con datos.")],
  open_task=task("Un cultivo de ejemplo de bacterias modificadas parte con 5 bacterias que se duplican cada hora y cada una produce 4 unidades por hora. Calcula cuántas bacterias hay a la hora 3 y cuántas unidades se producen en esa hora. Luego arma una tabla con dos grupos interesados (por ejemplo, personas que usan el producto y la empresa), un beneficio y un riesgo por estudiar de cada uno.", "Hora 3: 5 × 2 × 2 × 2 = 40 bacterias; unidades: 40 × 4 = 160. Personas que usan el producto: beneficio, más acceso; riesgo por estudiar, efectos del producto. Empresa: beneficio, ingresos; riesgo por estudiar, dependencia del producto.", ["calcula bien las bacterias y unidades", "la tabla tiene dos grupos con beneficio y riesgo", "usa «por estudiar» para los riesgos"], ["dos cálculos y una tabla"], ["suponer que el cultivo crece sin límite", "presentar riesgos como comprobados"], "Pregunta qué dato cambiaría tu lista de riesgos."),
  reinforce="Calcula las bacterias de un cultivo que parte con 2 y se duplica 4 veces.",
  extend="Explica por qué un riesgo potencial no es lo mismo que un daño comprobado.")

L(OA8, 5,
  materials="Este cuaderno y lápiz. Los casos son de ejemplo; en las preguntas éticas no hay una única respuesta correcta, pero sí argumentos mejor o peor fundamentados.",
  use="Aprenderé cómo una bacteria fabrica una proteína humana y a evaluar implicancias éticas y sociales de una aplicación, considerando evidencia y valores. Sirve para participar en una discusión informada.",
  prior=["Sé el modelo del ADN recombinante.", "Sé distinguir una pregunta empírica de una ética."],
  explain=[
      "Una bacteria con un gen humano puede fabricar la proteína correspondiente porque el código genético es casi igual en todos los seres vivos. El flujo de información es ADN, luego ARN mensajero y luego proteína: se copia el gen en un ARN y este se lee para armar la proteína. La insulina es una proteína que regula la glicemia; una enzima de detergente es otra proteína que ayuda a descomponer manchas.",
      "Evaluar las implicancias éticas y sociales requiere separar evidencia y valores. La evidencia dice qué ocurre: cuánto rinde un cultivo, si una sustancia es segura. Los valores orientan qué es deseable: acceso justo, información al consumidor, protección del ambiente, precaución. Personas distintas pueden dar distinto peso a los mismos valores y llegar a posiciones diferentes con los mismos datos.",
      "Para discutir con criterio se usan preguntas como estas: ¿qué beneficio hay y para quién?, ¿qué riesgo se estudió y con qué datos?, ¿quién tiene acceso y a qué costo?, ¿se informa a las personas?, ¿qué pasa si hay error? Un buen argumento cita evidencia, nombra el valor en que se apoya y reconoce una objeción.",
  ],
  vocab=[("ARN mensajero", "copia del gen que se lee para armar la proteína"), ("proteína", "molécula que cumple una función, como una hormona o una enzima"), ("implicancia ética", "efecto que obliga a discutir qué es correcto"), ("equidad", "reparto justo, por ejemplo del acceso a un producto"), ("principio de precaución", "tomar cuidado cuando un riesgo aún no está bien estudiado")],
  worked=[
      ("Evidencia y valor", "En un argumento se dice: «El maíz de ejemplo tiene menos daño por plaga; por eso debe etiquetarse para que las personas elijan». Separa la evidencia y el valor.", ["La evidencia es que tiene menos daño por plaga.", "El valor es el derecho de las personas a informarse y elegir.", "Ambos se unen en la conclusión de etiquetar."], "Evidencia: menos daño por plaga; valor: derecho a informarse"),
      ("Seguir el flujo del gen", "Una bacteria lleva el gen de una enzima. ¿Qué ocurre para que fabrique la proteína?", ["El gen se copia en un ARN mensajero.", "El ARN se lee para armar la proteína.", "La proteína cumple su función."], "ADN, ARN mensajero y proteína"),
  ],
  mistakes=[
      ("Creer que los datos deciden solos qué es correcto.", "Los datos dicen qué ocurre; qué es deseable depende también de valores.", "Nombra qué dato usas y en qué valor te apoyas."),
      ("Descalificar a quien piensa distinto sin revisar su argumento.", "Una discusión informada evalúa la evidencia y el valor del otro.", "Reconoce al menos un punto fuerte del otro argumento."),
  ],
  rec=[
      ("En el flujo de información, ¿qué molécula va entre el ADN y la proteína?", "El ARN mensajero", "El ADN se copia en ARN y este se lee."),
      ("¿Qué proteína producen bacterias modificadas para tratar la diabetes?", "Insulina", "Regula la glicemia."),
      ("Verdadero o falso: el código genético es casi igual en todos los seres vivos.", "Verdadero", "Por eso una bacteria puede leer un gen humano."),
  ],
  und=[
      ("¿Qué cumple la enzima de un detergente? A) Ayuda a descomponer manchas; B) Aporta el perfume al detergente.", "A", "Es una proteína con función química."),
      ("«Se midió el rendimiento de 12 parcelas» es A) evidencia; B) un valor.", "A", "Describe qué ocurrió."),
      ("«Todas las personas tienen derecho a elegir con información» es A) un valor; B) un dato medido.", "A", "Expresa lo que se considera deseable."),
  ],
  app=[
      ("«Un estudio de ejemplo midió 20 parcelas y los resultados fueron parecidos entre ellas.» ¿Qué tipo de afirmación es? A) Evidencia; B) Valor.", "A", "Describe lo observado."),
      arith("En una encuesta de ejemplo a 100 personas, 55 prefieren que los alimentos modificados se etiqueten. ¿Cuántas no lo prefieren?", "100-55", "Se restan las que lo prefieren del total."),
      ("Un argumento dice: «Debe haber acceso para todas las personas que necesitan un fármaco». ¿En qué valor se apoya? A) Equidad; B) Rendimiento.", "A", "Habla de acceso justo."),
  ],
  rea=[
      ("Dos personas ven los mismos datos de un cultivo y deciden distinto. ¿Por qué puede ocurrir? A) Dan distinto peso a valores como la precaución y la producción; B) Los datos de una de ellas son siempre falsos.", "A", "Los valores influyen en cómo se pesan los datos."),
      ("Alguien dice: «Todo producto de la manipulación genética es malo» y otra persona dice lo contrario. ¿Qué respuesta usa mejor la evidencia? A) Evaluar cada producto por separado, con datos y valores explícitos; B) Elegir la frase que suena más segura.", "A", "Las generalizaciones no representan casos distintos."),
  ],
  cha=[
      ("¿Qué evidencia ayudaría a evaluar un riesgo para el ambiente de un cultivo modificado? A) Estudios sobre si el gen pasa a plantas silvestres cercanas; B) La opinión de una persona famosa.", "A", "Evalúa el riesgo con datos y no con autoridad."),
      ("Un posible riesgo social por considerar es A) que solo quienes pueden pagar tengan acceso a un producto; B) que las bacterias necesiten alimento para crecer.", "A", "El acceso desigual es una preocupación de equidad."),
  ],
  context=[arith("En una consulta de ejemplo votan 80 personas: 35 a favor de etiquetar, 25 en contra y el resto está indecisa. ¿Cuántas personas están indecisas?", "80-35-25", "Se restan los dos grupos del total.")],
  selfcheck=[("¿Qué ruta sigue la información para fabricar una proteína?", "ADN, ARN mensajero y proteína", "El gen se copia y se lee."), ("¿Qué diferencia hay entre evidencia y valor?", "La evidencia dice qué ocurre y el valor qué es deseable", "Ambos intervienen en la discusión."), ("Nombra un valor que puede orientar una discusión.", "Equidad", "También precaución o información al consumidor.")],
  open_task=task("Elige uno de estos casos de ejemplo: bacterias que producen insulina, un cultivo resistente a una plaga o una enzima para detergentes. Escribe cuatro oraciones: un beneficio con su evidencia, un riesgo por estudiar, un valor que oriente la discusión y una objeción que reconozcas. No hay una sola posición correcta; se evalúa la calidad del argumento.", "Cultivo resistente a plagas: usa menos aplicaciones contra plagas en las parcelas medidas (evidencia). Riesgo por estudiar: que el gen pase a plantas silvestres. Valor: precaución. Objeción: otras personas valorarían más el rendimiento.", ["incluye una evidencia concreta", "nombra un valor", "reconoce una objeción"], ["cuatro oraciones"], ["afirmar un riesgo como comprobado sin datos", "descalificar otras posiciones"], "Pregunta qué dato podría cambiar tu posición."),
  reinforce="Escribe una evidencia y un valor sobre el mismo producto.",
  extend="Explica por qué dos personas pueden llegar a conclusiones distintas con los mismos datos.")
