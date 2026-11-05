"""Cuaderno del estudiante, 2.º medio Orientación: OA 01 (alternativas y decisiones para proyectos de vida) y OA 02 (sexualidad, vínculos, respeto e integridad)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR2M OA 01", "OR2M OA 02"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. El caso de Catalina, una estudiante inventada, está escrito en la clase y en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a examinar un caso ficticio de proyecto de vida y a separar en él los ámbitos, los intereses, las capacidades, las condiciones y las decisiones. Sirve para analizar alternativas con datos antes de hablar de las tuyas.",
    ["Sé distinguir interés, capacidad y condición (1.º medio).", "Sé que un proyecto de vida puede cambiar con nueva información."],
    [
        "Un proyecto de vida tiene varios ámbitos, que son las áreas donde proyectas tu futuro: el laboral o de estudios, el familiar, el comunitario y el personal. Una misma persona puede tener alternativas en cada ámbito a la vez. Por ejemplo, puede pensar en una carrera técnica, en cuidar a un familiar y en participar en un club deportivo.",
        "Para examinar un caso se separan cinco elementos. Los intereses son lo que atrae. Las capacidades son lo que la persona puede hacer o aprender. Las condiciones son las circunstancias, como el dinero, el tiempo, el lugar o los apoyos. Las decisiones son las elecciones que ya tomó. Las experiencias son lo que vivió al decidir. Las dos últimas importan porque influyen en que una alternativa se haga realidad o se cierre.",
        "Un caso ficticio protegido se analiza en tercera persona: hablas de «ella» o «él» y no de ti. Así puedes opinar y equivocarte sin exponer tu vida. Al terminar, tu análisis debe poder apoyarse en datos del caso, no en lo que imaginas de la persona.",
    ],
    [("ámbito", "área de la vida donde se proyecta el futuro, como estudios, trabajo o familia"), ("decisión", "elección que una persona ya hizo entre varias alternativas"), ("experiencia", "lo que una persona vivió y aprendió al actuar"), ("caso ficticio", "historia inventada para analizar sin exponer a nadie real"), ("tercera persona", "forma de hablar de otra persona usando «ella» o «él»")],
    [
        W("Identificar el ámbito", "Catalina escribe: «Quiero estudiar técnico en laboratorio clínico». ¿A qué ámbito pertenece esta frase?", ["Habla de estudios y de un futuro oficio.", "No habla de su familia ni de su comunidad."], "Al ámbito laboral o de estudios"),
        W("Separar decisión y condición", "Catalina se inscribió en el taller de ciencias del liceo, que funciona los martes, y su casa queda a 15 minutos del liceo. ¿Cuál dato es una decisión y cuál una condición?", ["Inscribirse es algo que ella eligió.", "La distancia a su casa es una circunstancia."], "Decisión: inscribirse; condición: la distancia a su casa"),
    ],
    [
        M("Hablar del caso como si fuera tu propia vida.", "Se mezcla el análisis con experiencias personales que no hay que contar.", "Usa «ella» o «él» y apóyate solo en los datos escritos."),
        M("Inventar datos que el caso no dice.", "Se rellenan los vacíos con suposiciones sobre la persona.", "Si falta un dato, anótalo como pregunta pendiente y no como hecho."),
    ],
    R=[
        ex("Catalina dice: «Me gustaría ayudar a mi abuelo con sus controles de salud». ¿A qué ámbito pertenece? A) Familiar B) Laboral", "A", "Se trata de apoyar a una persona de su familia."),
        ex("«Catalina sabe organizar listas de asistencia para el taller». ¿Es un interés, una capacidad o una condición?", "Una capacidad", "Describe algo que sabe hacer."),
        ex("«Catalina se inscribió en el taller de ciencias». ¿Es una decisión o una condición?", "Una decisión", "Es una elección que ella hizo."),
    ],
    U=[
        ex("En el caso se lee: «Su liceo tiene laboratorio y un profesor que la apoya». ¿Cuál es el elemento que describe? A) Condiciones y apoyos B) Intereses", "A", "Habla de recursos y personas que la rodean, no de lo que le gusta."),
        ex("Catalina probó el taller de ciencias y descubrió que le gusta más analizar muestras que escribir informes. ¿Qué influyó en ese descubrimiento? A) Una experiencia B) Una condición económica", "A", "Lo supo al vivir la actividad."),
        ex("¿Por qué el caso se cuenta en tercera persona? A) Para analizar sin exponer la vida privada de nadie B) Para que las respuestas sean más cortas", "A", "El análisis protege la privacidad de quienes participan."),
    ],
    A=[
        ex("Clasifica con I (interés), C (capacidad) o D (condición): 1) Le atrae la biología marina. 2) Puede explicar un gráfico con claridad. 3) El único taller está lejos de su barrio. Escribe las letras en orden.", "I, C, D", "La 1 es lo que le atrae, la 2 lo que puede hacer y la 3 una circunstancia."),
        ex("Catalina tiene alternativas en tres ámbitos: estudiar un técnico, cuidar a su hermano menor por las tardes y ser delegada de curso. ¿Cuántos ámbitos distintos aparecen?", "3", "Estudios o trabajo, familia y participación en la comunidad escolar son tres ámbitos."),
        ex("Si el caso no dice cuánto cuesta el técnico, ¿qué conviene hacer? A) Anotarlo como un dato pendiente de averiguar B) Suponer que es gratis", "A", "Un vacío se marca como pregunta y no se rellena con una suposición."),
    ],
    Z=[
        ex("Dos estudiantes inventados tienen el mismo interés por la cocina. Uno vive cerca de un instituto con esa carrera y el otro a 3 horas de uno. ¿Qué elemento explica que sus alternativas sean distintas?", "Las condiciones, como el lugar donde viven", "El interés es igual; cambia la circunstancia."),
        ex("Un compañero dice: «Las decisiones que Catalina tomó antes no importan, solo cuentan sus notas». ¿Qué respondes? A) Importan, porque cada decisión y experiencia le abre o le cierra alternativas B) Tiene razón, solo cuentan las notas", "A", "Las decisiones previas generan información y oportunidades."),
    ],
    D=[
        arith("Catalina ahorra $3.000 por semana durante 9 semanas para pagar un curso corto de primeros auxilios. ¿Cuántos pesos reúne en total?", "3000*9", "Se multiplica lo ahorrado cada semana por las semanas.", " pesos"),
        ex("Si un caso entrega estos datos: A) interés por la biología, B) nota promedio, C) lo que opina un vecino sin conocerla, ¿cuál NO sirve para analizar sus alternativas? Escribe la letra y una razón corta.", "C, porque es una opinión sin datos de ella", "Los dos primeros son datos del caso; el tercero no se apoya en nada comprobable."),
    ],
    context=[ex("En Orientación te entregan este caso inventado: Bastián quiere ser mecánico, trabaja los sábados en el taller de un tío y su familia puede pagarle los pasajes. ¿Cuál de estos datos es una condición? A) Que su familia puede pagarle los pasajes B) Que quiere ser mecánico", "A", "Es un apoyo concreto; querer ser mecánico es un interés.")],
    selfcheck=[ex("En Orientación: ¿un proyecto de vida puede tener alternativas en varios ámbitos?", "Sí", "Estudios, familia y comunidad pueden proyectarse a la vez."), ex("¿Una experiencia vivida puede cambiar las alternativas de una persona?", "Sí", "Da información nueva para decidir."), ex("¿Un caso ficticio se analiza contando experiencias propias?", "No", "Se analiza en tercera persona para proteger la privacidad.")],
    task=T("Lee el caso inventado de Nicolás: le gusta el ciclismo; arregla bien frenos de bicicleta; vive en un pueblo con una sola línea de bus; su prima le ofreció aprender en su bicicletería los sábados; el año pasado dejó un taller de dibujo por falta de tiempo. Escribe cinco líneas: un interés, una capacidad, una condición, una decisión y una pregunta que falta responder sobre su caso. Cada línea apoyada en un dato del texto.", "Interés: ciclismo. Capacidad: arregla frenos. Condición: una sola línea de bus. Decisión: dejó el taller de dibujo. Pregunta pendiente: ¿cuánto le pagarían o qué aprendería en la bicicletería?", ["escribe las cinco líneas", "cada línea usa un dato del texto", "no inventa datos nuevos", "habla en tercera persona"], ["cuadro escrito", "explicación oral"], ["contar experiencias propias", "inventar datos que el caso no dice"], "Reconoce las líneas bien apoyadas y pregunta de dónde salió el dato de la menos clara."),
    reinforce="Elige un personaje de una serie y escribe en tercera persona dos intereses y una condición suyos.",
    extend="Explica por qué una decisión tomada hace un año puede cambiar las alternativas de hoy.",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. Las frases del caso de Javiera, una estudiante inventada, están escritas en los ejercicios.",
    "Aprenderé a distinguir hechos, derechos y límites cuando analizo alternativas de proyecto de vida. Sirve para no descartar opciones por rumores ni por estereotipos y para saber qué se puede mover.",
    ["Sé analizar un caso con intereses, capacidades y condiciones.", "Sé qué es un estereotipo (1.º medio)."],
    [
        "Un hecho se puede comprobar con un dato, un documento o una persona que lo confirme. Una opinión es lo que alguien cree. Un rumor es algo que se repite sin saber de dónde viene. Antes de descartar una alternativa, conviene preguntar: ¿cómo lo sé? La frase «ese instituto cerró» es un hecho solo si una fuente oficial lo confirma.",
        "Las personas tienen derecho a la educación y a elegir su camino sin discriminación por género, origen, apariencia, discapacidad o situación económica. Un derecho es lo que te corresponde y los demás deben respetar. Una frase como «eso no es para mujeres» no describe una capacidad: expresa un prejuicio, es decir, un juicio previo sin conocer a la persona.",
        "Los límites pueden ser reales o aparentes. Un límite real es una condición que hoy no puedes cambiar, como un puntaje mínimo que aún no tienes o una edad mínima. Un límite aparente parece fijo, pero tiene vías de solución, como ahorrar, pedir una beca o buscar otro lugar. Distinguirlos permite poner energía donde sí se puede avanzar.",
    ],
    [("rumor", "información que se repite sin saber su origen ni comprobarla"), ("prejuicio", "juicio previo sobre alguien, sin conocerlo"), ("discriminación", "trato injusto a una persona por una característica suya"), ("límite real", "condición que hoy no se puede cambiar"), ("límite aparente", "obstáculo que parece fijo, pero se puede mover con un plan")],
    [
        W("Hecho o rumor", "Javiera oyó en el recreo: «Dicen que esa carrera no tiene trabajo». Ella no sabe quién lo dijo. ¿Es un hecho comprobado?", ["No hay una fuente que lo confirme.", "Se repite sin saber su origen.", "Primero habría que buscar datos oficiales."], "No: es un rumor hasta que se compruebe"),
        W("Límite aparente", "Javiera piensa: «No puedo estudiar eso porque la sede está en otra ciudad». Hay residencias estudiantiles y becas de mantención para quienes cumplen requisitos. ¿Qué tipo de límite es?", ["La distancia no cambia, pero hay formas de resolver el alojamiento.", "Existen vías que ella aún no ha revisado."], "Un límite aparente"),
    ],
    [
        M("Aceptar un rumor porque lo dicen muchas personas.", "Se confunde repetición con comprobación.", "Pide la fuente y revisa información oficial."),
        M("Creer que todo obstáculo es un límite real.", "Se desanima antes de buscar vías de solución.", "Pregunta qué se podría hacer para moverlo antes de descartar."),
    ],
    R=[
        ex("«El instituto publicó en su sitio oficial que las matrículas abren en enero». ¿Es un hecho o un rumor? A) Un hecho apoyado en una fuente B) Un rumor", "A", "Tiene una fuente identificada que se puede revisar."),
        ex("«Mi primo oyó que esa carrera es solo para hombres». ¿Es un hecho o un prejuicio?", "Un prejuicio", "Generaliza sobre un grupo y no se apoya en un dato."),
        ex("Un curso exige tener 18 años cumplidos y Javiera tiene 16. ¿El límite es real o aparente?", "Real", "La edad mínima no se puede cambiar hoy."),
    ],
    U=[
        ex("¿Cuál frase expresa un derecho? A) «Toda persona puede elegir su carrera sin ser discriminada.» B) «Esa carrera es mejor que otras.»", "A", "La primera habla de lo que corresponde a todas las personas; la segunda es una opinión."),
        ex("Una profesora le dice a Javiera: «Con tus notas de ciencias puedes postular a varias carreras de salud». ¿En qué se apoya esa frase? A) En un dato de Javiera B) En su género", "A", "Usa sus notas, que son un hecho comprobable."),
        ex("La familia de Javiera no puede pagar hoy un curso de $120.000, pero ella podría ahorrar y buscar una beca. ¿Qué tipo de límite es la falta de dinero hoy? A) Aparente B) Real", "A", "Se puede mover con ahorro o ayudas."),
    ],
    A=[
        ex("Clasifica con H (hecho comprobable) o R (rumor): 1) «El taller de electricidad funciona los jueves, está en el horario del liceo.» 2) «Dicen que ahí nadie consigue trabajo.» 3) «La ficha de postulación pide certificado de notas.» Escribe las letras en orden.", "H, R, H", "La 1 y la 3 se comprueban con documentos; la 2 no tiene fuente."),
        ex("A un compañero le dicen: «Estudiar peluquería es de mujeres». ¿Qué derecho puede recordar? A) Elegir su oficio sin discriminación B) Que todos coincidan con su elección", "A", "La elección de estudios no puede limitarse por el género."),
        ex("Javiera quiere estudiar una carrera que pide un puntaje mínimo de ingreso que hoy no tiene. Puede estudiar y rendir la prueba otra vez. ¿Cómo se clasifica el límite? A) Real hoy, pero se puede mover con preparación B) Real y nunca cambia", "A", "El puntaje de hoy es un hecho, pero puede mejorar con estudio."),
    ],
    Z=[
        ex("¿Por qué conviene preguntar «¿cómo lo sé?» antes de descartar una alternativa?", "Porque separa lo comprobado de los rumores y evita decidir con información falsa", "Una buena decisión se apoya en hechos."),
        ex("Dos amigos oyen que una carrera «ya no sirve». Uno busca la información oficial; el otro la descarta de inmediato. ¿Quién decide mejor? A) El que busca información oficial B) El que la descarta para no perder tiempo", "A", "Comprueba antes de cerrar una alternativa."),
    ],
    D=[
        arith("Una estudiante inventada revisa 4 fuentes oficiales de 3 carreras cada una. ¿Cuántas fichas de carrera revisa en total?", "4*3", "Se multiplican las fuentes por las carreras que tiene cada una."),
        ex("Un curso de $90.000 puede pagarse en 6 cuotas iguales. ¿De cuánto es cada cuota? Responde y di si el costo es un límite real o aparente.", "$15.000; es un límite aparente porque se puede repartir en cuotas", "90.000 dividido en 6 da 15.000, y pagar en cuotas lo hace más alcanzable."),
    ],
    context=[ex("En el pasillo escuchas: «Matías no puede ser enfermero porque es hombre». ¿Cuál es la respuesta que respeta su derecho? A) «Cada persona puede elegir su carrera sin discriminación.» B) «Mejor que elija algo más común.»", "A", "Afirma el derecho a elegir y no refuerza el prejuicio.")],
    selfcheck=[ex("En Orientación: ¿un rumor es un hecho comprobado?", "No", "Se repite sin una fuente que lo confirme."), ex("¿Todas las personas tienen derecho a elegir su carrera sin discriminación?", "Sí", "Es un derecho que no depende del género ni del origen."), ex("¿Un límite aparente puede moverse con un plan?", "Sí", "Parece fijo, pero tiene vías de solución.")],
    task=T("Lee estas cuatro frases inventadas: (a) «La beca de transporte se solicita con un formulario del liceo»; (b) «Esa especialidad es para los más inteligentes»; (c) «No tengo computador en mi casa para postular»; (d) «Para ese curso de buceo hay que tener 18 años». Clasifica cada una como hecho, prejuicio, límite aparente o límite real y escribe una razón.", "(a) Hecho: se comprueba con el formulario. (b) Prejuicio: generaliza sin datos. (c) Límite aparente: el liceo o una biblioteca pueden prestar computador. (d) Límite real: la edad no se puede cambiar hoy.", ["clasifica las cuatro frases", "da una razón para cada una", "distingue límite real de aparente", "no cuenta datos personales"], ["tabla escrita", "texto oral"], ["llamar hecho a un prejuicio", "tratar un límite aparente como definitivo"], "Reconoce las clasificaciones bien razonadas y pregunta cómo comprobaría la frase más dudosa."),
    reinforce="Escribe un rumor sobre estudios que hayas escuchado en general y una forma de comprobarlo.",
    extend="Explica con un ejemplo inventado por qué un límite real hoy puede dejar de serlo en dos años.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. Las tres alternativas de Bastián, un estudiante inventado, están escritas en los ejercicios.",
    "Aprenderé a comparar alternativas de proyecto de vida con una tabla de criterios y a prever consecuencias de corto y largo plazo. Sirve para decidir con más información.",
    ["Sé separar hechos, derechos y límites.", "Sé qué son corto y largo plazo."],
    [
        "Comparar alternativas es ponerlas lado a lado con los mismos criterios. Una tabla útil usa cuatro: interés (me atrae), capacidad (puedo hacerlo o aprenderlo), condiciones (es viable hoy) y consecuencia a largo plazo (qué abre o qué cierra). Cada alternativa recibe un sí o un no por criterio, con un dato que lo justifique, y cada sí vale 1 punto.",
        "Los criterios no siempre pesan igual. A veces una persona decide que la viabilidad vale doble porque no puede arriesgarse con el dinero. Eso se llama ponderar: dar más valor a un criterio. Si ponderas, debes decirlo antes de sumar, para que otra persona entienda tu resultado.",
        "Las consecuencias son lo que ocurre después de elegir. A corto plazo pueden ser esfuerzo, costo o tiempo. A largo plazo, oportunidades nuevas o cerradas. Un empate de puntos no obliga a elegir al azar: indica qué información falta. Y elegir una alternativa hoy no impide revisarla si cambian los datos.",
    ],
    [("criterio", "aspecto que se usa para comparar alternativas"), ("ponderar", "dar más valor a un criterio que a otro al comparar"), ("viable", "que se puede realizar con las condiciones de hoy"), ("consecuencia", "lo que ocurre después de una decisión"), ("empate", "igualdad de puntos entre dos alternativas")],
    [
        W("Sumar puntos", "Bastián evalúa un técnico en mecánica: interés sí, capacidad sí, condiciones no, largo plazo sí. Cada sí vale 1 punto. ¿Cuántos puntos tiene?", ["Se cuentan los síes: interés, capacidad y largo plazo.", "Condiciones tiene un no."], "3 puntos"),
        W("Ponderar un criterio", "Bastián decide que «condiciones» vale doble. Alternativa X: interés no, capacidad sí, condiciones sí, largo plazo sí. ¿Cuántos puntos suma?", ["Interés no suma 0.", "Capacidad sí suma 1 y largo plazo sí suma 1.", "Condiciones sí vale 2."], "4 puntos"),
    ],
    [
        M("Dar por ganadora la alternativa que tiene un punto más sin mirar de dónde viene.", "Se confía en el número y no en los datos que lo justifican.", "Revisa qué criterio aportó el punto y si el dato es comprobable."),
        M("Elegir al azar cuando hay empate.", "No se piensa en conseguir información del criterio dudoso.", "Averigua el dato que falta y vuelve a comparar."),
    ],
    R=[
        ex("¿Cuál de estos es un criterio de la tabla de cuatro criterios? A) Capacidad B) El color favorito de un amigo", "A", "Describe si la persona puede hacer o aprender la actividad."),
        ex("Perder las tardes libres por estudiar un año, ¿es consecuencia de corto o de largo plazo?", "De corto plazo", "Ocurre mientras estudia."),
        ex("Una alternativa tiene tres síes y un no. Cada sí vale 1 punto. ¿Cuántos puntos suma?", "3", "Se cuentan solo los síes."),
    ],
    U=[
        ex("Si dos alternativas empatan en puntos, ¿qué conviene hacer? A) Averiguar el dato que falta del criterio más dudoso B) Elegir la que alguien dijo primero", "A", "Un empate indica que falta información."),
        ex("Bastián pondera «condiciones» porque no puede arriesgar el dinero de su familia. ¿Qué debe hacer antes de sumar? A) Decir que ese criterio vale doble B) Sumar y explicar después", "A", "Ponderar exige decirlo antes para que el resultado se entienda."),
        ex("Una alternativa es cómoda hoy y cierra caminos después. ¿Qué parte de la tabla lo muestra? A) La consecuencia a largo plazo B) El interés", "A", "Esa columna registra lo que se abre o se cierra con el tiempo."),
    ],
    A=[
        ex("Bastián evalúa: Electricidad: interés sí, capacidad sí, condiciones sí, largo plazo no. Mecánica: interés sí, capacidad no, condiciones sí, largo plazo sí. Cada sí vale 1. ¿Cuál tiene más puntos?", "Hay empate con 3 puntos cada una", "Cada una suma 3 síes, por lo que hace falta más información."),
        ex("Con «condiciones» valiendo doble, Electricidad de la pregunta anterior suma 4 y Mecánica también suma 4. Bastián averigua que Mecánica ofrece beca. ¿Qué criterio se actualiza? A) Condiciones B) Interés", "A", "La beca cambia la viabilidad económica, no el gusto."),
        ex("Un curso de inglés cuesta $20.000 al mes por 5 meses y da un certificado que abre prácticas laborales. ¿Qué es el certificado? A) Una consecuencia de largo plazo B) Un costo inmediato", "A", "Se usa más adelante; el pago mensual es lo inmediato."),
    ],
    Z=[
        ex("¿Por qué una alternativa con más puntos hoy no siempre es la mejor?", "Porque los puntos dependen de datos que pueden cambiar y de criterios que se pueden ponderar distinto", "La tabla ayuda a decidir, pero revisa si los datos y los pesos son razonables."),
        ex("Una estudiante pondera «interés» como lo más importante y otra «condiciones». ¿Es correcto que lleguen a resultados distintos con los mismos datos? A) Sí, si cada una explica cómo ponderó B) No, solo hay un resultado posible", "A", "Los pesos reflejan prioridades personales."),
    ],
    D=[
        arith("Bastián dedica 4 horas semanales a un taller durante 14 semanas. ¿Cuántas horas dedica en total?", "4*14", "Se multiplican las horas por semana por las semanas."),
        arith("Una carrera técnica cuesta $1.200.000 por año. Una beca cubre $450.000 de ese año. ¿Cuántos pesos debe pagar la familia?", "1200000-450000", "Al costo anual se le resta lo que cubre la beca.", " pesos"),
    ],
    context=[ex("En el Consejo de Curso, Elisa compara estudiar en un CFT de su comuna o en otra región con más especialidades pero con gastos de arriendo. ¿Cuál es un criterio de viabilidad? A) El costo de arrendar y viajar B) Que a un compañero le guste más", "A", "Es una condición concreta que afecta la decisión.")],
    selfcheck=[ex("En Orientación: ¿ponderar es darle más valor a un criterio?", "Sí", "Se declara antes de sumar."), ex("¿Un empate de puntos obliga a elegir al azar?", "No", "Indica que falta información para decidir."), ex("¿Una decisión puede revisarse si cambian los datos?", "Sí", "Los proyectos de vida son flexibles.")],
    task=T("Bastián tiene tres alternativas para después de 4.º medio: (1) técnico en refrigeración en un instituto de su ciudad, 2 años, costo medio; (2) trabajar en la ferretería de una tía, ingreso inmediato, sin título; (3) ingeniería en otra ciudad, 5 años, costo alto, sin beca confirmada. Datos de Bastián: le atraen la electricidad y la refrigeración; se le dan bien física y matemática; su familia puede pagar un gasto medio, pero no uno alto. Haz una tabla con los cuatro criterios, un sí o no por cada uno con una razón, suma los puntos, y escribe una consecuencia de corto y una de largo plazo de la alternativa que más puntos tenga.", "Tabla de ejemplo: (1) interés sí, capacidad sí, condiciones sí, largo plazo sí = 4. (2) interés no, capacidad sí, condiciones sí, largo plazo no = 2. (3) interés sí, capacidad sí, condiciones no, largo plazo sí = 3. Corto plazo de (1): dedicar tardes a estudiar. Largo plazo: un título técnico que abre empleos.", ["completa los cuatro criterios para cada alternativa", "da una razón por criterio", "suma bien los puntos", "separa corto y largo plazo"], ["tabla escrita", "explicación oral"], ["sumar mal", "no justificar los síes y noes"], "Reconoce el orden de la tabla y pregunta qué dato apoya el criterio más débil."),
    reinforce="Compara dos planes para tu fin de semana con los cuatro criterios y escribe cuál tiene más puntos.",
    extend="Explica cómo cambiaría tu tabla si ponderas más el interés que las condiciones.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El caso de Antonia, una estudiante inventada, y sus tres pasos posibles están escritos en los ejercicios.",
    "Aprenderé a elegir un paso concreto, pequeño y seguro para acercarme a una alternativa de proyecto de vida. Sirve para pasar de pensar a probar sin arriesgarme de más.",
    ["Sé comparar alternativas con criterios.", "Sé que decisiones y experiencias influyen en el futuro."],
    [
        "Una acción segura para avanzar tiene cuatro rasgos. Es concreta: dice qué hacer, cuándo y dónde. Es pequeña: se puede cumplir en pocos días. Es reversible: si no resulta, puedes cambiar sin perder mucho. Y es acompañada: avisas o consultas a una persona adulta de confianza. Visitar una feria de estudios con una persona de tu casa cumple los cuatro rasgos. Dejar los estudios sin un plan no cumple ninguno.",
        "Cada paso que das te entrega una experiencia y datos nuevos. Si pruebas algo y descubres que no te gusta, no fracasaste: obtuviste información. Por eso conviene dividir una meta grande en pasos pequeños y guardar una evidencia de cada uno, como una nota con fecha o un comprobante.",
        "Tu seguridad también cuenta. Las ofertas de trabajo o cursos que piden dinero por adelantado, que prometen ganancias rápidas o que te piden salir solo a un lugar desconocido deben revisarse con una persona adulta antes de responder. Si algo te presiona o te incomoda, no sigas y avisa.",
    ],
    [("acción segura", "paso concreto, pequeño, reversible y acompañado"), ("reversible", "que se puede cambiar o deshacer sin perder mucho"), ("meta progresiva", "objetivo grande dividido en pasos pequeños"), ("evidencia", "prueba de que se hizo un paso, como una nota con fecha"), ("oferta engañosa", "propuesta que promete mucho y pide dinero o datos sin dar garantías")],
    [
        W("Elegir la acción más segura", "Antonia quiere explorar la carrera de kinesiología. Opción A: asistir a una charla abierta del instituto junto a una persona de su casa. Opción B: faltar tres semanas al liceo para hacer una práctica sin permiso. ¿Cuál es más segura?", ["A es concreta, pequeña y acompañada.", "B no es reversible y nadie la supervisa.", "A le da información sin riesgos."], "La opción A"),
        W("Dividir una meta", "La meta de Antonia: conocer tres carreras de salud en dos meses. ¿Cómo la divide en pasos con evidencia?", ["Paso 1: buscar en sitios oficiales los requisitos de las tres carreras.", "Paso 2: anotar en una tabla lo que descubrió.", "Paso 3: conversar con una profesora o con la persona orientadora y guardar sus comentarios."], "Tres pasos pequeños, cada uno con una evidencia escrita"),
    ],
    [
        M("Creer que una meta grande se logra con un solo paso.", "No se divide en partes alcanzables.", "Divide la meta en pasos semanales, cada uno con evidencia."),
        M("Aceptar una oferta de curso que pide pagar por adelantado sin averiguar.", "Se confunde la rapidez con la oportunidad.", "Revisa con una persona adulta y busca información oficial antes de pagar."),
    ],
    R=[
        ex("Antonia anota: «Algún día voy a hacer algo con la salud». ¿Qué le falta a ese paso para ser concreto? A) Decir qué hará y cuándo B) Pensar en más metas a la vez", "A", "Una acción concreta tiene tarea y fecha."),
        ex("Si un paso se puede cambiar sin perder mucho, ¿es reversible o irreversible?", "Reversible", "Se puede deshacer o ajustar."),
        ex("Antonia quiere dejar evidencia de que visitó la charla. ¿Cuál sirve? A) Una nota con la fecha y tres cosas que aprendió B) Contar que fue", "A", "Una nota con datos se puede mostrar; contarlo no deja registro."),
    ],
    U=[
        ex("¿Cuál de estas acciones es pequeña y acompañada? A) Pedir a la profesora jefe una hora para conversar sobre carreras B) Mudarse sola a otra ciudad el próximo mes", "A", "Es corta y cuenta con una persona adulta del colegio."),
        ex("Un aviso dice: «Gana $500.000 a la semana desde tu casa; paga $30.000 hoy para empezar». ¿Qué rasgo es una señal de alerta? A) Pide dinero por adelantado y promete ganancias rápidas B) Se publica en internet", "A", "Esas dos señales son típicas de ofertas engañosas."),
        ex("Si un paso resulta ser distinto de lo que Antonia esperaba, ¿qué ha obtenido? A) Información para ajustar su plan B) Un fracaso definitivo", "A", "Cada experiencia aporta datos."),
    ],
    A=[
        ex("Ordena de primero a último estos pasos de Antonia: 1) escribir lo aprendido en una tabla, 2) buscar los requisitos en un sitio oficial, 3) comentar la tabla con la persona orientadora. Escribe los números en orden.", "2, 1, 3", "Primero busca información, luego la ordena y al final la conversa."),
        ex("Un compañero propone: «Anda sola a una oficina que te dio un desconocido por mensaje». ¿Qué falta para que sea una acción segura? A) Avisar y consultar a una persona adulta de confianza y verificar la oferta B) Llevar más dinero", "A", "La seguridad depende de que haya acompañamiento y verificación."),
        ex("Antonia planea visitar 3 sedes distintas en 6 semanas, una cada dos semanas. ¿Es un plan pequeño y repartido en el tiempo? A) Sí B) No", "A", "Son tres visitas, cada una con dos semanas de margen."),
    ],
    Z=[
        ex("¿Por qué es mejor que un primer paso sea reversible?", "Porque si no resulta se puede cambiar sin perder mucho tiempo ni dinero", "Permite probar sin comprometer todo el proyecto."),
        ex("Dos estudiantes quieren saber si les gusta la cocina. Una se inscribe en un taller de un mes del liceo; el otro firma un contrato por tres años. ¿Quién actúa con más cuidado? A) La que se inscribe en el taller de un mes B) El que firma por tres años", "A", "Su paso es breve y reversible."),
    ],
    D=[
        arith("Antonia lleva 5 notas de pasos hechos y planea hacer 3 más cada mes durante 4 meses. ¿Cuántas notas tendrá al final?", "5+3*4", "Se multiplican las notas por mes por los meses y se suman a las que ya tiene."),
        ex("Una oferta pide $25.000 por adelantado para «reservar un puesto de trabajo» y no da una dirección ni un nombre de empresa. Escribe una acción segura que puede hacer Antonia.", "Avisar a una persona adulta de confianza y no pagar hasta verificar la oferta", "Sin datos verificables, pagar es un riesgo; un adulto puede ayudar a comprobar."),
    ],
    context=[ex("Joaquín quiere probar si le interesa la gastronomía. ¿Cuál es una acción segura y concreta? A) Anotarse a un taller escolar de cocina de un mes y contárselo a una persona de su casa B) Abandonar el liceo para entrar a trabajar a una cocina sin permiso", "A", "Es breve, reversible y acompañada.")],
    selfcheck=[ex("En Orientación: ¿una acción segura debe ser concreta?", "Sí", "Dice qué, cuándo y dónde."), ex("¿Conviene pagar por adelantado ante una oferta que promete ganancias rápidas sin verificar?", "No", "Es una señal típica de oferta engañosa."), ex("¿Guardar evidencia de un paso ayuda a revisar el plan?", "Sí", "Muestra qué se hizo y qué se aprendió.")],
    task=T("Antonia quiere saber si le gusta trabajar con niños. Tiene estas opciones: (a) hacer una tarde de ayudante en el taller de lectura de la biblioteca del barrio, avisando a una persona de su casa; (b) aceptar un trabajo de cuidadora que le ofrece una persona que conoció por internet; (c) leer los requisitos de una carrera de educación de párvulos en el sitio oficial de un instituto. Elige las dos acciones más seguras, justifica con los cuatro rasgos de una acción segura y escribe qué evidencia dejaría.", "Elijo (a) y (c). (a) es concreta (una tarde), pequeña, reversible y acompañada. (c) es concreta y reversible. Evidencia: una nota con fecha de la tarde y una tabla con los requisitos. Descarto (b) por ser con un desconocido de internet.", ["elige dos acciones seguras", "justifica con los rasgos", "propone una evidencia", "descarta la opción riesgosa"], ["texto escrito", "explicación oral"], ["no explicar por qué una acción es riesgosa", "olvidar la evidencia"], "Reconoce los rasgos bien aplicados y pregunta qué haría si la opción elegida no resultara."),
    reinforce="Divide en tres pasos con evidencia una meta pequeña de tu semana, por ejemplo mejorar una nota.",
    extend="Explica por qué avisar a una persona adulta es parte de la autonomía y no una pérdida de ella.",
)

lesson(
    OA1, 5,
    "Una hoja y un lápiz. Los mensajes de ejemplo están escritos en los ejercicios; usa personas inventadas.",
    "Aprenderé a pedir orientación sobre mi futuro y a comunicar una decisión a otra persona con claridad y respeto. Sirve para conversar con tu familia, con tu profesora o con la persona orientadora sin discutir.",
    ["Sé elegir una acción segura.", "Conozco a las personas adultas de apoyo del colegio."],
    [
        "Pedir orientación es una forma de cuidar tu proyecto. Un buen mensaje tiene tres partes: saludo con tu propósito, una pregunta concreta y lo que ya averiguaste. Por ejemplo: «Hola, profesora. Estoy comparando dos técnicos. ¿Puede orientarme sobre sus requisitos? Ya revisé los costos». Así la otra persona sabe cómo ayudar.",
        "Cuando quieres comunicar una decisión, usa la estructura de tres pasos: cuenta lo que piensas hacer, explica la razón con un dato y pregunta qué opina la otra persona. Si hay desacuerdo, escucha primero y repite con tus palabras lo que entendiste. Un desacuerdo no es una pelea: es información sobre lo que la otra persona valora.",
        "A veces los adultos de tu casa y tú tienen ideas distintas sobre el futuro. Puedes proponer un acuerdo: una prueba corta, una visita o una revisión en tres meses. Si la conversación sube de tono, pide una pausa y vuelve después. Si sientes presión que te asusta, avisa a la persona orientadora o a otro adulto de confianza.",
    ],
    [("orientación", "ayuda para tomar decisiones sobre estudios y trabajo"), ("propósito", "para qué se escribe o se conversa"), ("desacuerdo", "diferencia de opinión entre personas"), ("acuerdo", "decisión que aceptan las dos partes"), ("pausa", "detener la conversación un momento para calmarse")],
    [
        W("Armar un mensaje", "Rodrigo quiere pedir a la persona orientadora información sobre becas. Ya revisó dos sitios oficiales. ¿Cómo lo escribe?", ["Saludo y propósito: «Hola, quiero informarme sobre becas».", "Pregunta concreta: «¿Qué requisitos suelen pedir?».", "Lo ya averiguado: «Ya revisé dos sitios oficiales»."], "Un mensaje con saludo, pregunta concreta y lo averiguado"),
        W("Proponer un acuerdo", "Camila y una persona de su casa no coinciden sobre su carrera. Ella propone ir juntos a una charla informativa y decidir después. ¿Qué tipo de propuesta es?", ["No obliga a nadie a cambiar de idea hoy.", "Entrega información a ambas partes.", "Se revisa después de la visita."], "Un acuerdo de prueba corta"),
    ],
    [
        M("Escribir un mensaje sin decir qué se necesita.", "Se cree que la otra persona adivinará la petición.", "Incluye una pregunta concreta."),
        M("Defender la decisión sin escuchar la opinión del otro.", "Se piensa que escuchar es perder.", "Repite con tus palabras lo que entendiste antes de responder."),
    ],
    R=[
        ex("¿Cuál mensaje tiene una pregunta concreta? A) «¿Qué requisitos pide el técnico en administración?» B) «Necesito ayuda con todo lo del futuro»", "A", "La primera pide una información precisa."),
        ex("En el mensaje «Hola, quiero comparar dos institutos», ¿qué parte es el propósito?", "Quiero comparar dos institutos", "Dice para qué se escribe."),
        ex("Si la conversación sube de tono, ¿qué conviene? A) Pedir una pausa y retomar después B) Subir la voz para que te escuchen", "A", "La pausa baja la tensión y permite conversar mejor."),
    ],
    U=[
        ex("Una persona de tu casa dice «prefiero que estudies otra cosa». ¿Qué sigue en la estructura de tres pasos? A) Escuchar, repetir lo que entendiste y proponer una forma de probar B) Responder «no me importa»", "A", "Repetir lo entendido muestra respeto y abre un acuerdo."),
        ex("¿Qué dato refuerza más tu decisión ante un adulto? A) «Revisé los requisitos y cumplo cinco de seis» B) «Todos mis amigos van ahí»", "A", "Es un dato comprobable de tu situación."),
        ex("Rodrigo siente que en su casa lo presionan de forma que lo asusta. ¿A quién recurre? A) A la persona orientadora o a otro adulto de confianza B) A nadie, para no causar problemas", "A", "Pedir ayuda es parte del cuidado."),
    ],
    A=[
        ex("Ordena las partes de un mensaje: 1) «¿Puede decirme qué documentos piden?», 2) «Hola, profesor. Quiero postular a una beca», 3) «Ya revisé el calendario de postulación». Escribe los números en orden.", "2, 1, 3", "Primero el saludo con propósito, luego la pregunta y al final lo averiguado."),
        ex("Una amiga dice: «Quiero estudiar diseño y mi tío dice que no sirve». Entre estas respuestas, ¿cuál escucha primero? A) «¿Qué datos tiene tu tío para decir eso?» B) «Tu tío está equivocado, no lo escuches»", "A", "Pregunta por los datos sin descalificar a nadie."),
        ex("Camila propone «una visita al instituto y revisar la decisión en tres meses». ¿Qué ventaja tiene? A) Todos obtienen información antes de decidir B) Evita hablar del tema para siempre", "A", "Permite decidir con datos y no con presiones."),
    ],
    Z=[
        ex("¿Por qué es útil repetir con tus palabras lo que dijo la otra persona antes de responder?", "Porque muestra que la escuchaste y evita malentendidos", "Aclara si entendiste bien y baja la tensión."),
        ex("Dos formas de comunicar una decisión: A) «Voy a estudiar eso, pase lo que pase» B) «Pienso estudiar eso porque cumplo los requisitos; ¿qué opinas?». ¿Cuál invita a conversar?", "B", "Da una razón y pregunta la opinión del otro."),
    ],
    D=[
        arith("En su Consejo de Curso, 32 estudiantes se reparten en grupos de 4 para practicar mensajes. ¿Cuántos grupos se forman?", "32//4", "Se divide el total entre los integrantes de cada grupo."),
        ex("Un estudiante quiere decirle a una persona adulta que visitará un instituto, con lo que piensa hacer, una razón y una pregunta. ¿Qué frase tiene las tres partes? A) «Quiero visitar el instituto porque me interesa la carrera; ¿qué día conviene ir?» B) «Quiero visitar el instituto.»", "A", "Incluye lo que hará, la razón y una pregunta."),
    ],
    context=[ex("Ignacio quiere contarle a una persona de su casa que prefiere un técnico y no la universidad. ¿Cuál es el mejor inicio? A) «Estuve comparando opciones y me gustaría contarte lo que descubrí.» B) «Ya decidí, no hay nada que hablar.»", "A", "Abre la conversación con respeto y sin cerrar el diálogo.")],
    selfcheck=[ex("En Orientación: ¿un buen mensaje de consulta incluye una pregunta concreta?", "Sí", "Permite que la otra persona sepa cómo ayudar."), ex("¿Un desacuerdo es siempre una pelea?", "No", "Puede ser información sobre lo que el otro valora."), ex("¿Puedes pedir ayuda a la persona orientadora si sientes presión?", "Sí", "Es una persona adulta de apoyo en el colegio.")],
    task=T("Escribe un mensaje de cinco líneas para la persona orientadora de un liceo inventado. Imagina que eres Valentina, quien duda entre dos carreras técnicas: contabilidad y programación. Incluye: saludo y propósito, una pregunta concreta, dos cosas que ya averiguó (por ejemplo, la duración y el costo de ejemplo) y una propuesta de día para conversar.", "Hola, profesora Mónica. Quiero orientarme entre contabilidad y programación. Ya vi que ambas duran dos años y que una tiene mensualidad más baja. ¿Podría explicarme qué se estudia en cada una? ¿Podemos conversar el jueves en el recreo largo?", ["incluye saludo y propósito", "hace una pregunta concreta", "menciona lo ya averiguado", "propone un momento para conversar"], ["mensaje escrito", "práctica oral en parejas"], ["no hacer ninguna pregunta", "mensaje demasiado largo"], "Reconoce las partes bien escritas y pregunta cuál sería la respuesta que más le sirve."),
    reinforce="Escribe un mensaje de tres líneas para pedir información sobre una charla de carreras.",
    extend="Explica por qué proponer una prueba corta puede ayudar a llegar a un acuerdo con una persona de tu casa.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. El caso de Daniela y Tomás, estudiantes inventados, está escrito en la clase y en los ejercicios. Nadie debe contar experiencias propias.",
    "Aprenderé a examinar un caso ficticio sobre vínculos afectivos con tres ideas: respeto, responsabilidad y cuidado. Sirve para reconocer cuándo una relación cuida a las personas y cuándo no.",
    ["Sé que todas las personas tienen derecho a ser respetadas (1.º medio).", "Sé a qué personas adultas puedo pedir ayuda."],
    [
        "Un vínculo afectivo es la relación de cariño entre dos personas, como una amistad, un pololeo o la relación con la familia. En los vínculos de pareja de adolescentes, tres valores orientan el análisis. El respeto es tratar a la otra persona como alguien con derechos. La responsabilidad es hacerse cargo de las consecuencias de lo que uno hace y dice. El cuidado es proteger la salud, la intimidad y las emociones propias y ajenas.",
        "La sexualidad es una parte de la vida de toda persona: incluye el cuerpo, los afectos, las ideas y los vínculos. Hablar de ella en el colegio no es exponer a nadie, sino aprender a decidir con información, a respetar límites y a pedir ayuda. Por eso el análisis se hace con casos inventados, sin preguntar a nadie por su vida privada.",
        "Para examinar un caso conviene preguntar tres cosas: qué hechos hay (qué dijo, qué hizo), qué derechos o valores están en juego (respeto, intimidad, integridad) y quién puede ayudar. La integridad física y emocional es el derecho a no ser dañado en el cuerpo ni en los sentimientos. Una relación sana se nota porque ambas personas pueden decir que no y seguir siendo respetadas.",
    ],
    [("vínculo afectivo", "relación de cariño entre dos personas"), ("respeto", "tratar a otra persona como alguien con derechos"), ("responsabilidad", "hacerse cargo de las consecuencias de lo que se hace"), ("intimidad", "lo privado de una persona, que ella decide si comparte"), ("integridad", "derecho a no ser dañado en el cuerpo ni en las emociones")],
    [
        W("Identificar un valor en juego", "En el caso, Tomás le pide a Daniela la contraseña de su celular «para confiar». Daniela se siente incómoda. ¿Qué derecho está en juego?", ["La contraseña da acceso a mensajes privados.", "Daniela no quiere compartirla.", "Lo privado le corresponde a ella decidirlo."], "Su intimidad"),
        W("Separar hecho y suposición", "Del caso: «Tomás se enojó y dejó de hablarle dos días» y «Seguro lo hace porque la quiere mucho». ¿Cuál es el hecho?", ["Dejar de hablar dos días ocurrió y se puede describir.", "«Porque la quiere mucho» es una interpretación."], "El hecho es que dejó de hablarle dos días"),
    ],
    [
        M("Pensar que celar o controlar es una forma de cuidar.", "Se confunde interés con control.", "Cuidar respeta la intimidad y la decisión de la otra persona."),
        M("Culpar a la persona que sufre la situación.", "Se piensa que ella debió actuar distinto.", "Analiza qué hizo la persona que cruzó el límite y qué ayuda hay disponible."),
    ],
    R=[
        ex("«Daniela decide no compartir su contraseña». ¿Qué derecho ejerce? A) Su intimidad B) Su derecho a estar sola siempre", "A", "Decide qué parte de su vida privada comparte."),
        ex("Tomás le dice: «Si no me das tu contraseña, me enojo». ¿Eso es un hecho o una suposición sobre sus intenciones?", "Un hecho", "Es una frase que dijo y que puede describirse."),
        ex("¿Qué valor consiste en hacerse cargo de las consecuencias de lo que uno dice y hace? A) Responsabilidad B) Intimidad", "A", "Ese es el significado de responsabilidad."),
    ],
    U=[
        ex("En una relación sana, ¿qué ocurre cuando una persona dice que no? A) La otra la respeta y la relación continúa B) La otra se enoja y la castiga con silencio", "A", "Decir que no no debe traer castigos."),
        ex("¿Cuál frase describe cuidado? A) «Si algo te incomoda, dímelo y lo conversamos.» B) «Dime dónde estás cada hora.»", "A", "Respeta a la persona y abre el diálogo."),
        ex("¿Por qué el caso se analiza sin pedir experiencias personales? A) Para proteger la privacidad de quienes participan B) Para que el tema no sea importante", "A", "Se puede aprender sin exponer la vida privada de nadie."),
    ],
    A=[
        ex("Clasifica con H (hecho) o S (suposición): 1) «Tomás leyó los mensajes de Daniela sin su permiso.» 2) «Lo hizo porque está muy enamorado.» 3) «Daniela le pidió que dejara de hacerlo.» Escribe las letras en orden.", "H, S, H", "La 1 y la 3 son acciones descritas; la 2 es una interpretación de sus razones."),
        ex("Daniela duda si pedir ayuda. ¿A quién podría recurrir según el caso? A) A la persona orientadora o a otro adulto de confianza B) A nadie, porque la privacidad prohíbe contar", "A", "Pedir ayuda protege su integridad; contar a un adulto no la expone."),
        ex("Daniela y Tomás llevan 3 meses de relación. Tomás le pidió la contraseña 2 veces por semana durante 4 semanas. ¿Cuántas veces la pidió en total?", "8", "Dos veces por semana durante cuatro semanas son 8 veces."),
    ],
    Z=[
        ex("¿Por qué pedir la contraseña «para confiar» puede ser una señal de alerta?", "Porque la confianza no se prueba invadiendo la intimidad ajena", "La confianza se construye respetando lo privado."),
        ex("Un compañero dice: «Si ella lo permite hoy, ya lo permitió siempre». ¿Qué respondes? A) El consentimiento puede retirarse en cualquier momento B) Tiene razón, no puede cambiar de opinión", "A", "Cada persona puede cambiar de opinión sobre su intimidad."),
    ],
    D=[
        arith("En una encuesta anónima de ejemplo, de 36 estudiantes de un curso inventado, 9 dijeron conocer una relación con control del celular. ¿Cuántos estudiantes no lo dijeron?", "36-9", "Al total se le resta quienes sí lo dijeron."),
        ex("Tomás se entera de que a Daniela le incomodó su petición. ¿Qué respuesta de Tomás respeta su límite? A) «Perdón por pedírtela; tu celular es privado.» B) «No es para tanto, otras parejas se las dan.»", "A", "Reconoce su error y respeta la intimidad de Daniela."),
    ],
    context=[ex("En un taller de convivencia leen este caso inventado: Lucas manda mensajes cada 10 minutos a su pareja y se enoja si ella no responde. ¿Cuál es el hecho? A) Manda mensajes cada 10 minutos y se enoja si no responde B) Quiere mucho a su pareja", "A", "Es lo que se observa; lo otro es una suposición.")],
    selfcheck=[ex("En Orientación: ¿la intimidad es lo privado que cada persona decide compartir?", "Sí", "Es un derecho personal."), ex("¿Controlar el celular de otra persona es una forma de cuidado?", "No", "Invade su intimidad."), ex("¿Es importante pedir ayuda a una persona adulta de confianza ante una relación que incomoda?", "Sí", "Ayuda a protegerse sin enfrentarse solo.")],
    task=T("Lee el caso inventado: Fernanda y Ricardo son pareja. Ricardo le pide que no hable con sus amigos hombres y le revisa las fotos del celular. Fernanda se siente nerviosa y no sabe qué hacer. Escribe: (1) dos hechos del caso, (2) un derecho que está en juego, (3) una acción segura para Fernanda y (4) a quién puede pedir ayuda.", "Hechos: le pide que no hable con sus amigos; le revisa las fotos. Derecho: intimidad y libertad de relacionarse. Acción segura: decir que no se siente cómoda y contarle a una persona adulta de confianza. Ayuda: la persona orientadora o una persona de su casa.", ["escribe dos hechos distintos", "nombra un derecho en juego", "propone una acción segura", "indica una persona de apoyo"], ["texto escrito", "tabla"], ["culpar a Fernanda", "pensar que el control es cuidado"], "Reconoce los hechos separados de las suposiciones y pregunta quién más podría apoyar."),
    reinforce="Anota tres frases que muestren respeto en un vínculo de amistad inventado.",
    extend="Explica por qué la responsabilidad en un vínculo afectivo se aplica a las dos personas.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. Las frases y casos de ejemplo están escritos en los ejercicios; son de personas inventadas.",
    "Aprenderé a distinguir hechos, derechos y límites sobre consentimiento y vínculos, usando fuentes confiables. Sirve para separar mitos de información y reconocer qué siempre se debe respetar.",
    ["Sé analizar un caso con respeto, responsabilidad y cuidado.", "Sé qué es la intimidad."],
    [
        "El consentimiento es aceptar algo de manera libre, clara y sin presión. Debe ser voluntario, es decir, sin amenazas ni chantaje; informado, es decir, la persona sabe a qué dice sí; y reversible, es decir, puede cambiar de opinión cuando quiera. El silencio, el miedo o el cansancio no son un sí. Y alguien que está bajo presión no está consintiendo.",
        "Un mito es una creencia popular que no es verdadera, como «si alguien acepta una vez, acepta siempre» o «las personas tienen que demostrar amor con pruebas». Un hecho se confirma en una fuente confiable: el centro de salud, la persona orientadora o materiales de organismos públicos de salud. Una fuente no confiable es un chisme, un video sin autor o una cadena de mensajes.",
        "Algunos límites son siempre válidos. Nadie puede obligarte a hacer algo con tu cuerpo ni con tu intimidad, ni puede difundir imágenes tuyas sin permiso. Además, la información sobre salud sexual, como los métodos para prevenir infecciones y embarazos, se consulta con profesionales de la salud. Pedir información no es una falta, es un acto de cuidado.",
    ],
    [("consentimiento", "aceptación libre, clara e informada, que se puede retirar"), ("voluntario", "sin amenazas, presión ni chantaje"), ("reversible", "que se puede cambiar de opinión cuando se quiera"), ("mito", "creencia popular que no es verdadera"), ("fuente confiable", "persona o institución con conocimiento verificable, como un centro de salud")],
    [
        W("Reconocer una presión", "Marcos le dice a Sofía: «Si de verdad me quieres, lo haces». Sofía no quiere. ¿Hay consentimiento?", ["Sofía no quiere.", "Marcos usa presión emocional.", "Un sí bajo presión no es libre."], "No hay consentimiento"),
        W("Fuente confiable", "Leo recibió en una cadena de mensajes un dato de salud sin autor. ¿Dónde puede verificarlo?", ["La cadena no tiene autor ni respaldo.", "Un centro de salud o la persona orientadora tienen información verificable."], "En un centro de salud o con la persona orientadora"),
    ],
    [
        M("Creer que un «sí» antes sirve para siempre.", "Se confunde un acuerdo pasado con permiso permanente.", "El consentimiento se renueva y se puede retirar."),
        M("Confiar en cualquier información que circula por redes.", "Se piensa que si muchos la comparten es verdad.", "Verifica en fuentes confiables."),
    ],
    R=[
        ex("¿Cuál es una característica del consentimiento? A) Que sea voluntario B) Que se dé por cansancio", "A", "Debe darse libremente y sin presión."),
        ex("«Si aceptó una vez, acepta siempre». ¿Es un hecho o un mito?", "Un mito", "El consentimiento puede cambiar en cualquier momento."),
        ex("¿Dónde se puede consultar información verificable sobre salud sexual? A) En un centro de salud B) En una cadena de mensajes sin autor", "A", "Tiene profesionales que respaldan la información."),
    ],
    U=[
        ex("Si una persona no dice nada por miedo, ¿hay consentimiento? A) No, el miedo o el silencio no son un sí B) Sí, porque no se negó", "A", "El consentimiento debe ser claro y libre."),
        ex("¿Cuál de estas frases presiona? A) «Si me quisieras, lo harías.» B) «Me importa lo que tú quieras.»", "A", "Pone a la otra persona en situación de culpa."),
        ex("Un mensaje dice «las mujeres siempre dicen no cuando quieren decir sí». ¿Qué corresponde? A) Verificar y reconocer que es un mito peligroso B) Compartirlo para que todos lo sepan", "A", "Ese mito se usa para justificar la presión y la violencia."),
    ],
    A=[
        ex("Clasifica con H (hecho) o M (mito): 1) «El consentimiento puede retirarse en cualquier momento.» 2) «Si alguien acepta una vez, ya no puede cambiar de opinión.» 3) «Nadie puede difundir imágenes de otra persona sin su permiso.» Escribe las letras en orden.", "H, M, H", "La 1 y la 3 son principios de respeto; la 2 es un mito."),
        ex("Sofía le dice a Marcos: «No quiero, gracias». Marcos responde: «Ok, gracias por decírmelo». ¿Qué hizo Marcos? A) Respetó el límite B) Cedió porque ella lo presionó", "A", "Aceptó su decisión sin insistir."),
        ex("Leo quiere saber cómo prevenir infecciones de transmisión sexual. ¿Cuál es una acción segura? A) Consultar a un profesional de un centro de salud con una persona adulta de confianza B) Preguntar a un grupo anónimo de internet", "A", "Los profesionales entregan información verificada."),
    ],
    Z=[
        ex("¿Por qué «un sí bajo presión» no vale como consentimiento?", "Porque no es libre ni voluntario", "El consentimiento requiere decidir sin miedo ni chantaje."),
        ex("Un joven dice: «Pedí permiso una vez, con eso basta». ¿Qué falta? A) Que la otra persona pueda cambiar de opinión y él lo respete B) Nada, con una vez alcanza", "A", "El consentimiento no es permanente."),
    ],
    D=[
        arith("Una encuesta anónima de ejemplo en un curso de 40 estudiantes dice que 14 creyeron un mito sobre consentimiento. ¿Cuántos no lo creyeron?", "40-14", "Al total se le restan quienes lo creyeron."),
        ex("Sofía quiere decir que no sin justificarse largamente. ¿Qué frase le sirve? A) «No quiero, gracias.» B) «No puedo porque tengo mucho que hacer, además mi tía dijo que tal vez, y quizás después.»", "A", "Es corta y clara, y no necesita explicación."),
    ],
    context=[ex("En un taller leen este caso inventado: Pía recibe un video de un grupo que dice «todas aceptan si se insiste». ¿Qué debe hacer? A) No creerlo, no reenviarlo y consultar a una persona adulta de confianza B) Reenviarlo a otro grupo para comentarlo", "A", "Es un mito que justifica la presión y no debe difundirse.")],
    selfcheck=[ex("En Orientación: ¿el consentimiento puede cambiarse en cualquier momento?", "Sí", "Puede retirarse en cualquier momento."), ex("¿El silencio por miedo equivale a un sí?", "No", "No es una aceptación libre."), ex("¿Una cadena de mensajes sin autor es una fuente confiable de salud?", "No", "No se puede verificar quién la escribió.")],
    task=T("Lee las cuatro frases inventadas: (a) «Aceptó ayer, así que hoy también»; (b) «Una persona puede decir no sin explicar»; (c) «Me mandaron una cadena que dice que no hay que ir al centro de salud»; (d) «Para consultar sobre salud sexual puedes acudir a un centro de salud o a la persona orientadora». Clasifica cada una como hecho, mito, fuente confiable o fuente no confiable, y escribe por qué.", "(a) Mito: el consentimiento no es permanente. (b) Hecho: nadie debe justificar su no. (c) No es fuente confiable: no tiene autor. (d) Fuente confiable: indica instituciones con profesionales.", ["clasifica las cuatro frases", "justifica cada una", "distingue mito de fuente", "no cuenta experiencias propias"], ["tabla escrita", "texto oral"], ["llamar hecho a un mito", "aceptar una cadena sin autor"], "Reconoce los mitos bien identificados y pregunta cómo verificaría la frase (c)."),
    reinforce="Escribe dos mitos sobre relaciones que hayas oído en general y la información correcta.",
    extend="Explica por qué el consentimiento debe ser voluntario, informado y reversible.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. Las dos opciones de Camilo, un estudiante inventado, están escritas en los ejercicios.",
    "Aprenderé a comparar dos opciones ante una presión en una relación y a prever sus consecuencias para la salud, la intimidad y las emociones. Sirve para decidir con cuidado y sin apuro.",
    ["Sé que el consentimiento es libre y reversible.", "Sé distinguir mitos de hechos."],
    [
        "Cuando alguien presiona, hay al menos dos caminos. Uno es ceder para evitar un conflicto. Otro es decir que no, proponer esperar o pedir ayuda. Para compararlos se analizan las consecuencias a corto plazo (cómo te sientes hoy, cómo reacciona la otra persona) y a largo plazo (riesgos para tu salud, tu intimidad y tu bienestar emocional).",
        "Ceder bajo presión puede traer consecuencias que no se pueden deshacer: una imagen enviada puede circular, una decisión apurada puede afectar la salud, y el malestar emocional puede durar. Decir que no puede traer incomodidad hoy, pero protege lo importante. Además, una relación que no tolera un no puede necesitar una revisión con ayuda de un adulto.",
        "La responsabilidad afectiva es cuidar tanto lo propio como lo ajeno. Incluye informarse, pedir consentimiento, respetar un no y no presionar. También incluye saber cuándo no te corresponde resolver solo: si hay amenazas, chantaje o miedo, la salida segura es avisar a un adulto de confianza.",
    ],
    [("presión", "insistencia para que alguien haga algo que no quiere"), ("ceder", "aceptar algo que no se quiere para evitar un conflicto"), ("consecuencia irreversible", "efecto que no se puede deshacer"), ("responsabilidad afectiva", "cuidar a las personas de un vínculo, incluyéndote a ti"), ("chantaje", "amenaza de hacer algo malo si no se cumple lo que se pide")],
    [
        W("Comparar dos opciones", "Camilo recibe presión para enviar una foto íntima. Opción A: enviarla para evitar que se enoje. Opción B: decir que no y avisar a una persona adulta de confianza. ¿Cuál protege mejor su intimidad?", ["A produce una imagen que puede circular sin control.", "B pone un límite y busca apoyo.", "B es la que protege a largo plazo."], "La opción B"),
        W("Corto y largo plazo", "Decir que no genera incomodidad hoy, pero evita que una imagen circule después. ¿Qué parte es corto plazo y cuál largo plazo?", ["La incomodidad ocurre ahora.", "Evitar que circule es un efecto posterior."], "Corto plazo: incomodidad; largo plazo: proteger su intimidad"),
    ],
    [
        M("Pensar que ceder una vez solucionará la presión.", "Se cree que el problema termina al complacer.", "La presión suele repetirse; poner un límite y pedir apoyo protege mejor."),
        M("Creer que decir que no daña la relación para siempre.", "Se ve solo la consecuencia inmediata.", "Una relación respetuosa tolera un no."),
    ],
    R=[
        ex("Enviar una imagen íntima y que otra persona la difunda, ¿es una consecuencia reversible o irreversible?", "Irreversible", "Una vez difundida no se puede controlar."),
        ex("La incomodidad al decir que no, ¿es corto o largo plazo? A) Corto plazo B) Largo plazo", "A", "Se siente en el momento."),
        ex("¿Qué es un chantaje? A) Amenazar con algo malo si no se hace lo que se pide B) Pedir ayuda a un adulto", "A", "Ese es el significado de chantaje."),
    ],
    U=[
        ex("Si alguien te amenaza con mostrar algo si no haces lo que pide, ¿qué conviene? A) Avisar a un adulto de confianza y no ceder B) Hacer lo que pide para que no lo muestre", "A", "Ceder no detiene el chantaje."),
        ex("¿Qué consecuencia de largo plazo tiene protegerse al decir que no? A) Cuidar la salud y la intimidad B) Perder amigos para siempre", "A", "El cuidado propio tiene efectos duraderos."),
        ex("¿Cuál es un riesgo de decidir apurado? A) Que la decisión no se pueda deshacer B) Que la relación mejore automáticamente", "A", "Algunas decisiones apuradas son irreversibles."),
    ],
    A=[
        ex("Camilo evalúa dos caminos con 1 punto por cada consecuencia protectora: Ceder: protege intimidad no, protege salud no, protege emociones no. Decir que no y pedir ayuda: intimidad sí, salud sí, emociones sí. ¿Cuántos puntos más tiene la segunda?", "3", "Ceder suma 0 y la segunda suma 3."),
        ex("Una compañera le dice a Camilo: «Si dices que no, te quedarás solo». ¿Qué pregunta le ayuda a decidir? A) «¿Esta persona me respeta cuando digo no?» B) «¿Cuántos amigos tengo hoy?»", "A", "Examina el respeto en el vínculo."),
        ex("Camilo recibe un mensaje de un desconocido que le ofrece dinero por fotos personales. ¿Qué paso corresponde? A) No responder, guardar captura y avisar a un adulto B) Preguntar cuánto paga", "A", "Es una situación de riesgo que debe conocer un adulto."),
    ],
    Z=[
        ex("¿Por qué comparar solo la consecuencia de hoy puede llevar a una mala decisión?", "Porque ignora riesgos que aparecen después y que no se pueden deshacer", "Los efectos a largo plazo pueden ser más graves."),
        ex("Dos estudiantes enfrentan una presión. Una cede por temor y el otro pide ayuda a la orientadora. ¿Quién previene mejor sus riesgos? A) El que pide ayuda B) La que cede", "A", "Recibe apoyo y evita consecuencias irreversibles."),
    ],
    D=[
        arith("En una actividad de ejemplo, 5 grupos de 6 estudiantes comparan opciones de un caso. ¿Cuántos estudiantes participan?", "5*6", "Se multiplican los grupos por los integrantes."),
        ex("Camilo quiere decir que no sin ofender y proponer esperar. ¿Qué frase lo logra? A) «No me siento listo, prefiero esperar.» B) «Eres un presionador y no te hablo más.»", "A", "Es clara y firme y no ataca a la otra persona."),
    ],
    context=[ex("En una película que analizan en clase, el personaje Iván le pide a su pareja una foto íntima y ella duda. ¿Cuál es la acción más segura para ella? A) Decir que no quiere y contarle a un adulto de confianza B) Enviarla y pedirle que la borre", "A", "Pedir que borre no asegura que no se difunda.")],
    selfcheck=[ex("En Orientación: ¿ceder bajo presión puede traer consecuencias irreversibles?", "Sí", "Una imagen enviada puede circular."), ex("¿Una relación respetuosa tolera un no?", "Sí", "El respeto incluye aceptar un límite."), ex("¿Hay que enfrentar solo un chantaje?", "No", "Se avisa a un adulto de confianza.")],
    task=T("Lee el caso inventado de Valeria: su pololo insiste en que le mande una foto íntima y le dice que, si no lo hace, le contará a todos que lo dejó. Haz una tabla con dos opciones (ceder; decir que no y pedir ayuda), escribe una consecuencia a corto plazo y una a largo plazo de cada una, y elige una justificando con un derecho.", "Ceder: corto plazo, él deja de insistir; largo plazo, la imagen puede circular y el chantaje seguir. Decir que no y pedir ayuda: corto plazo, incomodidad; largo plazo, protege su intimidad. Elijo la segunda por el derecho a la intimidad y a no ser amenazada.", ["compara dos opciones", "escribe corto y largo plazo", "elige con un derecho", "incluye a un adulto de confianza"], ["tabla escrita", "explicación oral"], ["olvidar el largo plazo", "no mencionar el apoyo adulto"], "Reconoce la tabla completa y pregunta por la consecuencia que más pesa."),
    reinforce="Anota dos riesgos de decidir apurado en cualquier tema y una forma de evitarlos.",
    extend="Explica por qué la responsabilidad afectiva incluye cuidarte a ti y a la otra persona.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. El caso de Isidora, una estudiante inventada, está escrito en los ejercicios. No escribas casos tuyos.",
    "Aprenderé a elegir una acción segura cuando una imagen íntima se comparte sin permiso o cuando alguien cruza un límite. Sirve para saber qué hacer, qué no hacer y a quién avisar.",
    ["Sé comparar opciones y consecuencias.", "Sé que la intimidad es un derecho."],
    [
        "Compartir una imagen íntima de otra persona sin su permiso daña su intimidad y su integridad emocional, y puede ser delito. La persona que sufre la difusión no es culpable. Si recibes una imagen así, no la reenvíes, no la comentes ni la guardes. Reenviarla multiplica el daño. No guardes la imagen en tu celular ni la saques en captura. No borres la conversación, porque muestra quién la envió, y avisa a una persona adulta de confianza, que te ayudará a decidir qué hacer.",
        "Quien fue afectada o afectado debe saber que puede pedir ayuda sin ser juzgado. No debe borrar el chat, porque el chat es la evidencia. Puede bloquear a quien presiona y avisar a la persona orientadora, a una persona de su casa o a otro adulto de confianza. El Fono Niños 147 también orienta. Si hay miedo o amenazas, la ayuda de un adulto es parte de la seguridad.",
        "Una acción segura combina cuatro pasos: parar (no seguir ni reenviar), proteger (no borrar el chat y bloquear), avisar (a un adulto) y cuidarse (hablar de cómo te sientes). No consiste en hacer justicia por mano propia ni en enfrentar al agresor, porque eso puede aumentar el riesgo.",
    ],
    [("difusión", "hacer que algo llegue a muchas personas"), ("evidencia", "prueba de lo ocurrido, como una captura de la conversación"), ("culpa", "responsabilidad por una falta, que recae en quien comete la acción"), ("bloquear", "impedir que alguien te escriba o te vea"), ("Fono Niños 147", "línea telefónica de orientación para niñas, niños y adolescentes")],
    [
        W("Elegir los pasos", "Isidora ve en un grupo una imagen íntima de una compañera. ¿Qué hace primero?", ["No la reenvía ni la comenta.", "No guarda la imagen ni la saca en captura, y no borra la conversación.", "Avisa a un adulto de confianza."], "No reenviar, no guardar la imagen, no borrar el chat y avisar a un adulto"),
        W("Apoyar a la persona afectada", "La compañera afectada se siente avergonzada. ¿Qué frase la apoya?", ["No es su culpa.", "Hay ayuda disponible.", "No tiene que enfrentar sola la situación."], "«No es tu culpa. Hay adultos que pueden ayudarte. Estoy contigo»"),
    ],
    [
        M("Reenviar la imagen «para avisar a alguien».", "Se piensa que mostrarla ayuda.", "Reenviar multiplica el daño; avisa al adulto sin compartirla."),
        M("Borrar el chat para que nadie lo vea.", "Se cree que sin chat el problema desaparece.", "El chat es evidencia: no lo borres y avisa a un adulto."),
    ],
    R=[
        ex("Si recibes una imagen íntima de otra persona, ¿qué haces con ella? A) La reenvío para que otros opinen B) No la reenvío ni la comento y aviso a un adulto", "B", "Reenviar multiplica el daño a la persona afectada."),
        ex("¿Qué debe conservar quien recibe presión por chat? A) La captura de la conversación B) Nada, para olvidarlo", "A", "Sirve de evidencia."),
        ex("¿Quién es responsable de la difusión de una imagen sin permiso? A) Quien la difunde B) La persona de la imagen", "A", "La responsabilidad es de quien comete la acción."),
    ],
    U=[
        ex("Isidora recibe en un grupo una imagen íntima de una compañera. ¿Qué paso es correcto? A) No reenviarla ni comentarla, no borrar el chat y avisar a un adulto B) Comentarla para saber quién la mandó", "A", "Comentarla aumenta la difusión."),
        ex("¿Por qué no se debe borrar el chat? A) Porque es evidencia B) Porque ocupa poco espacio", "A", "Permite mostrar qué ocurrió."),
        ex("¿Cuál frase apoya a la persona afectada? A) «No fue tu culpa; busquemos ayuda.» B) «¿Cómo se te ocurrió mandar eso?»", "A", "Reconoce que no es culpable y ofrece apoyo."),
    ],
    A=[
        ex("Clasifica cada acción con P (parar), R (proteger), A (avisar) o C (cuidarse): 1) No reenviar ni comentar la imagen. 2) No borrar el chat y bloquear a quien la envió. 3) Contarle a la persona orientadora. 4) Conversar con alguien de confianza sobre cómo te sientes. Escribe las letras en orden.", "P, R, A, C", "Cada acción corresponde a uno de los cuatro pasos de la acción segura."),
        ex("Un compañero propone «ir a buscar a quien la difundió para que pague». ¿Qué responde Isidora? A) «Mejor avisemos a un adulto; enfrentarlo puede ser peligroso.» B) «Vamos todos a pedirle cuentas.»", "A", "Enfrentar puede aumentar el riesgo."),
        ex("¿A cuál de estas personas puede avisar? A) La persona orientadora o una persona de su casa B) A un desconocido en una red social", "A", "Son personas adultas de confianza."),
    ],
    Z=[
        ex("¿Por qué la persona afectada por una difusión no es responsable?", "Porque la responsabilidad es de quien difundió sin permiso", "La difusión es una decisión de otra persona."),
        ex("Dos estudiantes reciben la misma imagen. Uno la reenvía y otra la reporta y avisa. ¿Quién protege a la persona afectada? A) Quien reporta y avisa B) Quien la reenvía", "A", "Reenviar multiplica el daño."),
    ],
    D=[
        arith("En un grupo de 48 integrantes, 12 reenviaron un mensaje dañino. ¿Cuántos integrantes no lo reenviaron?", "48-12", "Se restan los que reenviaron al total."),
        ex("Un testigo ve que difunden una imagen íntima de una compañera. ¿Qué acción es segura? A) Avisar a un adulto de confianza sin reenviar nada B) Preguntar en el grupo quién tiene la imagen", "A", "Protege a la persona afectada sin aumentar la difusión."),
    ],
    context=[ex("En un taller de ejemplo, Sebastián ve que un compañero amenaza a otro con difundir una foto. ¿Qué acción es segura? A) Guardar captura, no reenviar y avisar a la persona orientadora B) Reírse para que no se enoje", "A", "Se detiene el daño sin enfrentar al agresor.")],
    selfcheck=[ex("En Orientación: ¿reenviar una imagen íntima multiplica el daño?", "Sí", "Más personas la ven."), ex("¿Se debe borrar el chat que sirve de evidencia?", "No", "Se conserva y se avisa a un adulto."), ex("¿Es una acción segura avisar a un adulto de confianza?", "Sí", "Es la ayuda más útil.")],
    task=T("Lee el caso inventado: en un grupo del curso circula una imagen íntima de una compañera, y alguien propone reírse del tema. Escribe un plan de cuatro pasos para una persona testigo (parar, proteger, avisar, cuidarse) y una frase de apoyo para la compañera afectada.", "Parar: no reenviar ni comentar. Proteger: no borrar el chat y bloquear. Avisar: contarle a la persona orientadora. Cuidarse: conversar con alguien de confianza sobre cómo me siento. Frase: «No es tu culpa; estoy contigo y busquemos ayuda».", ["escribe los cuatro pasos", "incluye a un adulto", "no sugiere enfrentar al agresor", "escribe una frase de apoyo"], ["plan escrito", "juego de roles"], ["reenviar la imagen", "borrar el chat"], "Reconoce los pasos bien ordenados y pregunta qué haría si el adulto no responde."),
    reinforce="Escribe una frase de apoyo para alguien que está avergonzado por una situación en línea.",
    extend="Explica por qué enfrentar al agresor por mano propia puede ser peligroso.",
)

lesson(
    OA2, 5,
    "Una hoja y un lápiz. Las frases de ejemplo están escritas en los ejercicios; usa personas inventadas.",
    "Aprenderé a practicar frases para poner límites y a pedir ayuda sobre vínculos y sexualidad. Sirve para saber qué decir y a quién acudir cuando algo incomoda o genera dudas.",
    ["Sé elegir una acción segura.", "Conozco a la persona orientadora y otras personas de apoyo."],
    [
        "Poner un límite es decir qué aceptas y qué no. Se hace con frases cortas y firmes: «No quiero», «Para, por favor», «No me siento cómodo con eso». No necesitas pedir perdón ni dar largas explicaciones. Si no te escuchan, repite la frase y aléjate. Una buena frase combina lo que sientes, lo que pides y lo que harás si no se respeta.",
        "Pedir ayuda también se practica. Puedes decir: «Necesito contarte algo que me incomoda» y luego dar hechos: qué pasó, cuándo y dónde. No necesitas tener todas las pruebas. Si la primera persona no te escucha, sigue buscando a otra: la persona orientadora, la profesora jefe, una persona de tu casa, el centro de salud o el Fono Niños 147.",
        "En los chats, si alguien presiona, no respondas con enojo: guarda una captura, bloquea y avisa a un adulto. Cuando otra persona te diga «no», respétalo de inmediato: «ok, gracias por decírmelo». Para consultas de salud sexual puedes pedir una hora en un centro de salud, solo o acompañado, con información confiable. Practicar antes ayuda a decirlo cuando lo necesites.",
    ],
    [("límite", "lo que una persona acepta o no acepta"), ("frase en primera persona", "frase que empieza con «yo» y dice lo que uno siente o decide"), ("captura de pantalla", "imagen de lo que se ve en el celular, útil como evidencia"), ("red de apoyo", "personas e instituciones a las que se puede pedir ayuda"), ("consulta de salud", "conversación con un profesional para informarse y cuidarse")],
    [
        W("Armar una frase de límite", "Fabián quiere que un compañero deje de hacerle bromas sobre su cuerpo. Usa las tres partes de una frase de límite.", ["Siento: «me incomoda».", "Pido: «no hagas bromas de mi cuerpo».", "Haré: «si sigues, me voy y aviso a un adulto»."], "«Me incomoda. No hagas bromas de mi cuerpo. Si sigues, me voy y aviso a un adulto»"),
        W("Pedir ayuda con hechos", "Lorena quiere contar a su profesora que un compañero le escribe mensajes que la incomodan. ¿Qué hechos da?", ["Qué mensajes recibe.", "Desde cuándo.", "Qué hizo ella: guardó capturas y bloqueó."], "Qué, desde cuándo y qué hizo"),
    ],
    [
        M("Decir un límite pidiendo perdón o con largas excusas.", "Se teme que el otro se enoje.", "Usa frases cortas y firmes, sin justificarte."),
        M("Esperar a tener todas las pruebas para pedir ayuda.", "Se cree que sin pruebas no te creerán.", "Cuenta lo que pasó y guarda las capturas; el adulto ayuda a averiguar."),
    ],
    R=[
        ex("¿Cuál frase es un límite claro? A) «Para, por favor, no me gusta.» B) «Quizás, no sé, déjame ver.»", "A", "Dice lo que siente y lo que pide."),
        ex("Un chat te incomoda y quieres mostrárselo a un adulto. ¿Qué sirve como evidencia? A) Una captura de pantalla con fecha y hora B) Un recuerdo vago de lo que decía", "A", "Muestra lo que se escribió."),
        ex("Si la primera persona adulta no te escucha, ¿qué haces? A) Sigues buscando a otra persona de confianza B) Dejas de contar", "A", "Hay varias personas y servicios de apoyo."),
    ],
    U=[
        ex("¿Qué respondes cuando alguien te dice «no»? A) «Ok, gracias por decírmelo.» B) «Vamos, no seas así.»", "A", "Se respeta el límite."),
        ex("Alguien te presiona por chat. ¿Qué haces primero? A) Guardar una captura y luego bloquear B) Responder con insultos para que pare", "A", "La captura queda como evidencia y el bloqueo evita que siga."),
        ex("Una estudiante quiere informarse sobre salud sexual. ¿Qué es una opción segura? A) Pedir una hora en el centro de salud, con una persona adulta de confianza si lo prefiere B) Buscar en un foro sin autor", "A", "Un profesional de salud entrega información verificada."),
    ],
    A=[
        ex("Clasifica cada frase como L (límite claro) o E (excusa): 1) «No me gusta que me toques el pelo.» 2) «Es que mi mamá se enoja, por eso no.» 3) «Para, por favor.» Escribe las letras en orden.", "L, E, L", "La 1 y la 3 son directas; la 2 se apoya en otra persona."),
        ex("Rodrigo quiere pedir ayuda a su profesor jefe porque le hacen bromas de tipo sexual en el curso. ¿Cuál es el mejor inicio? A) «Necesito contarle algo que me incomoda.» B) «No es nada, olvídelo.»", "A", "Abre la conversación con claridad."),
        ex("Un desconocido en una red pide una foto íntima a una amiga. ¿Qué haces tú si ella te lo cuenta? A) Ayudarla a guardar la captura, bloquear y avisar a un adulto B) Reírte y decirle que conteste", "A", "Es el protocolo de protección en línea."),
    ],
    Z=[
        ex("¿Por qué no es necesario justificar un «no»?", "Porque cada persona tiene derecho a decidir sobre su cuerpo sin dar explicaciones", "El límite es un derecho y no depende de que otros lo aprueben."),
        ex("¿Por qué conviene guardar capturas de un chat que te incomoda? A) Porque permiten mostrar a un adulto qué pasó B) Para publicarlas y que todos sepan quién es", "A", "Son evidencia; publicarlas expone a más personas."),
    ],
    D=[
        arith("Una orientadora inventada atiende 6 estudiantes por jornada, en 4 jornadas a la semana. ¿Cuántos estudiantes atiende por semana?", "6*4", "Se multiplican estudiantes por jornadas."),
        arith("En una actividad, 38 estudiantes practican frases de límite en parejas. ¿Cuántas parejas se forman?", "38//2", "Se divide el total entre los 2 integrantes de cada pareja."),
    ],
    context=[ex("Lucía recibe en el recreo comentarios sexuales de un compañero. ¿Qué serie de pasos es la más segura? A) Decir «para, no me gusta», alejarse y avisar a un adulto B) Responderle con otra burla para que se detenga", "A", "Pone un límite sin violencia y busca ayuda.")],
    selfcheck=[ex("En Orientación: ¿un límite debe ser claro y breve?", "Sí", "Se entiende mejor."), ex("¿Hay que tener todas las pruebas antes de pedir ayuda?", "No", "Basta contar lo que pasó."), ex("¿Puedes bloquear y avisar a un adulto si alguien te presiona por chat?", "Sí", "Es una forma de cuidarte.")],
    task=T("Lee las tres situaciones inventadas: (a) un compañero te hace bromas sexuales en el pasillo; (b) un perfil desconocido te pide una foto; (c) una amiga te cuenta que su pololo le revisa el celular y se enoja si no responde rápido. Escribe una frase de límite para (a), tres pasos de protección para (b) y una frase para apoyar a tu amiga en (c).", "(a) «Me incomoda. Para, por favor.» (b) Guardar captura, bloquear, avisar a un adulto. (c) «Lo que cuentas es importante; hablemos con la orientadora.»", ["escribe una frase de límite", "escribe tres pasos para el chat", "ofrece apoyo a la amiga", "no usa casos propios"], ["frases escritas", "juego de roles"], ["frase larga con excusas", "olvidar al adulto"], "Reconoce las frases firmes y pregunta cuál paso es el primero en el chat."),
    reinforce="Escribe dos frases cortas de límite para usar con un compañero que te molesta.",
    extend="Explica por qué bloquear no es lo mismo que dejar de pedir ayuda.",
)

lesson(
    OA2, 6,
    "Una hoja y un lápiz. Los dos casos nuevos están escritos en los ejercicios; son de personas inventadas. No cuentes nada tuyo.",
    "Aprenderé a transferir lo aprendido a casos nuevos sin hablar de mi vida privada. Sirve para aplicar respeto, responsabilidad y cuidado en situaciones distintas.",
    ["Sé poner límites y pedir ayuda.", "Sé comparar opciones y consecuencias."],
    [
        "Transferir es usar lo que aprendiste en una situación que no habías visto. Para eso conviene tener una guía de cinco preguntas: ¿qué hechos hay?, ¿qué derecho o valor está en juego?, ¿qué opciones hay y qué consecuencias tiene cada una?, ¿cuál es la acción más segura? y ¿a quién se puede pedir ayuda?",
        "Los casos nuevos pueden cambiar de lugar, de personas o de medio: una conversación presencial, un chat de grupo o una red social. Aun así, los principios se mantienen: el consentimiento es libre y reversible, la intimidad se respeta, no se reenvían imágenes y se avisa a una persona adulta de confianza. Lo que cambia son los detalles, como dónde guardar evidencia.",
        "Aprender a transferir te protege porque no memorizas un caso, sino un método. Y mantiene tu privacidad: respondes sobre personajes, no sobre ti. Si alguien se siente mal durante la actividad, puede pasar o conversar con la persona orientadora en privado.",
    ],
    [("transferir", "aplicar lo aprendido a una situación nueva"), ("principio", "idea central que se mantiene en distintos casos"), ("guía de preguntas", "lista de preguntas que ordena el análisis"), ("medio", "canal donde ocurre algo, como un chat o un encuentro presencial"), ("privacidad", "derecho a mantener en reserva la vida personal")],
    [
        W("Aplicar la guía", "Caso nuevo: en un chat de curso, alguien pide a Paula que muestre una foto en ropa de baño «para ver si encaja». Paula no quiere. ¿Qué derecho está en juego y qué acción es segura?", ["El derecho es la intimidad y el consentimiento.", "La acción segura es decir que no, guardar captura, bloquear y avisar a un adulto."], "Intimidad; decir no, guardar captura y avisar"),
        W("Cambiar el medio", "El mismo principio se aplica si la presión ocurre en persona. ¿Qué cambia?", ["En persona no hay captura.", "Se puede anotar lo ocurrido con fecha y lugar apenas pase.", "Se avisa igual a un adulto de confianza."], "Cambia la evidencia, no el principio"),
    ],
    [
        M("Pensar que un principio vale solo para el caso que se estudió.", "No se reconoce la idea central en un contexto distinto.", "Pregunta qué derecho está en juego y aplica la guía."),
        M("Contar experiencias propias para demostrar que se aprendió.", "Se confunde aprender con exponerse.", "Responde sobre casos inventados y pide ayuda en privado si lo necesitas."),
    ],
    R=[
        ex("¿Cuál es la primera pregunta de la guía? A) ¿Qué hechos hay? B) ¿Quién tiene la culpa?", "A", "Primero se separan los hechos."),
        ex("En un chat de curso piden una foto íntima a Paula. ¿Qué derecho está en juego? A) La intimidad B) La libertad de pasear", "A", "Es su derecho a decidir qué muestra de su cuerpo."),
        ex("¿Qué se mantiene igual si el caso pasa de un chat a una conversación en persona?", "El principio de respetar el no y avisar a un adulto", "Los principios no cambian con el medio."),
    ],
    U=[
        ex("Un amigo de Tomás le pide que reenvíe una captura de un video privado de una compañera. ¿Qué aplica Tomás? A) No reenviarlo y avisar a un adulto B) Reenviarlo solo a un amigo", "A", "Reenviar multiplica el daño."),
        ex("¿Por qué las respuestas de esta actividad son sobre personajes? A) Para proteger la privacidad B) Porque los estudiantes no saben nada del tema", "A", "Se aprende sin exponer la vida personal."),
        ex("En el caso de Paula, ¿quién puede ayudar? A) La persona orientadora o una persona adulta de confianza B) El grupo que la presiona", "A", "Son personas de apoyo y no parte del problema."),
    ],
    A=[
        ex("Caso: Matías recibe un mensaje que dice «si no me mandas una foto, publico lo que sé de ti». ¿Cuál es la acción más segura? A) Enviar la foto para que no publique nada B) Guardar captura del mensaje, bloquear y avisar a un adulto de confianza", "B", "Ceder no detiene el chantaje; la ayuda adulta sí protege."),
        ex("Otro caso: una persona adulta desconocida le pide a una adolescente de 15 años que le cuente secretos y que no avise a nadie. ¿Qué corresponde? A) Dejar de responder, guardar captura y avisar a un adulto B) Guardar el secreto", "A", "Un pedido de secreto de un adulto desconocido es una señal de riesgo."),
        ex("Un caso nuevo muestra a dos estudiantes que se gustan y conversan sobre sus límites. ¿Qué rasgo de relación sana tiene? A) Ambos pueden decir que no y son respetados B) Uno decide por los dos", "A", "Hay respeto por los límites."),
    ],
    Z=[
        ex("¿Por qué conviene aprender un método y no memorizar un solo caso?", "Porque el método sirve en situaciones nuevas aunque cambien las personas o el medio", "Los casos varían, pero los principios y las preguntas se mantienen."),
        ex("¿Cuál respuesta transfiere mejor lo aprendido a un caso nuevo? A) Identificar hechos, derecho en juego, opciones y ayuda B) Repetir la respuesta de otro caso", "A", "Aplica el método al caso."),
    ],
    D=[
        arith("En un taller, 4 grupos analizan 3 casos cada uno. ¿Cuántos casos se analizan en total?", "4*3", "Se multiplican los grupos por los casos de cada uno."),
        ex("Un compañero de ejemplo sufre presión por un chat. ¿Qué frase lo cuida sin pedirle detalles personales? A) «Estoy contigo; hablemos con la orientadora.» B) «Cuéntame todo lo que te escribieron.»", "A", "Apoya sin exponerlo ni exigir detalles."),
    ],
    context=[ex("En una charla de salud, un profesional de un centro de salud explica que atiende a adolescentes con respeto a su privacidad. ¿Qué hace valioso ese espacio? A) Puede consultar con información confiable y respeto a su privacidad B) Debe contar todo a sus compañeros", "A", "La confidencialidad protege la intimidad.")],
    selfcheck=[ex("En Orientación: ¿los principios de respeto cambian según el medio?", "No", "El principio se mantiene aunque el medio cambie."), ex("¿Se puede responder sobre personajes inventados sin hablar de uno mismo?", "Sí", "Así se protege la privacidad."), ex("¿Es válido pedir ayuda en privado si la actividad incomoda?", "Sí", "Se puede pasar o hablar con la orientadora.")],
    task=T("Lee este caso nuevo inventado: Emilia recibe en un grupo del taller de teatro el mensaje «sube una foto en traje de baño o te sacamos del grupo». Usa la guía de cinco preguntas y responde: hechos, derecho en juego, dos opciones con consecuencias, acción más segura y a quién avisar.", "Hechos: le piden una foto bajo amenaza de sacarla. Derecho: intimidad y consentimiento. Opciones: enviarla (puede circular) o negarse y avisar (incomodidad, pero se protege). Acción más segura: no enviar, guardar captura, bloquear y avisar a la persona orientadora. Ayuda: orientadora, profesor del taller o una persona de su casa.", ["responde las cinco preguntas", "compara dos opciones", "elige una acción segura", "nombra a un adulto de apoyo"], ["texto escrito", "tabla"], ["contar un caso propio", "no mencionar al adulto"], "Reconoce las preguntas bien respondidas y pregunta qué cambiaría si el mensaje fuera en persona."),
    reinforce="Elige un personaje de una serie y aplica la guía de cinco preguntas a una situación de presión.",
    extend="Explica qué principio se mantiene al pasar de un chat a una situación presencial.",
)
