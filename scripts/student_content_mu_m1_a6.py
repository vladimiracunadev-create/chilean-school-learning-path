"""Student material for 1.º medio Música, OA 06 (analizar fortalezas y áreas de crecimiento personal en la audición, interpretación, creación y reflexión, y su influencia en el trabajo musical propio y colectivo, proponiendo alternativas de desarrollo).

Todas las bitácoras, personas y datos de los ejercicios son inventados («de ejemplo»); se evalúa siempre lo que suena y el proceso, nunca a la persona.
"""
from __future__ import annotations

from student_content_mu_m1_a import L
from student_lessons import arith, ex

OA6 = "MU1M OA 06"

CAMI = ("Bitácora de ejemplo de Camila. Audición: identificó 4 de 5 rasgos pedidos en un fragmento. Interpretación: mantuvo el pulso estable, pero tuvo 6 errores de afinación en una frase. "
        "Creación: inventó un motivo y lo varió dos veces, pero no terminó en la nota de reposo. Reflexión: justificó con «porque» 2 de sus 4 respuestas")

# ---------------------------------------------------------------- OA 06 · clase 1 (fortalezas y áreas de crecimiento con evidencia)
L(
    OA6, 1,
    f"Lápiz y papel. Bitácora de ejemplo, que se repite en los ejercicios: {CAMI}.",
    "Aprenderé a reconocer mis fortalezas y mis áreas de crecimiento en cuatro dimensiones del trabajo musical (audición, interpretación, creación y reflexión) apoyándome en evidencia. Sirve para saber qué mantener y qué mejorar sin juzgarme como persona.",
    ["Sé registrar lo que escucho y lo que toco.", "Sé comparar versiones con datos.", "Sé usar «porque» para justificar."],
    [
        "El trabajo musical tiene cuatro dimensiones. La audición es escuchar con atención y reconocer rasgos. La interpretación es cantar o tocar con precisión y fluidez. La creación es improvisar, componer o arreglar. La reflexión es explicar lo que se hizo y decidir cómo mejorar. En cada una, una fortaleza es algo que ya hago bien, con evidencia que lo muestra, y un área de crecimiento es algo que todavía puedo mejorar, también con evidencia.",
        "Una frase como «soy malo para cantar» no sirve, porque juzga a la persona y no dice qué mejorar. En cambio, «mantuve el pulso estable, pero tuve 6 errores de afinación en una frase» sí sirve: muestra una fortaleza (el pulso) y un área de crecimiento (la afinación), cada una con un dato. Los datos pueden ser conteos, tempos, porcentajes o comentarios de otras personas basados en lo que se oyó.",
        "Todas las personas tienen fortalezas y áreas de crecimiento, y no son fijas: cambian con la práctica. Para analizarlas, conviene mirar las cuatro dimensiones y no solo una. Se compara con la propia versión anterior y no con otra persona, porque cada quien parte de un lugar distinto. Si pensar en lo que cuesta genera mucha angustia, es bueno contárselo a una persona adulta de confianza.",
    ],
    [("fortaleza", "algo que hago bien y puedo mostrar con evidencia"), ("área de crecimiento", "algo que puedo mejorar, con evidencia de dónde estoy"), ("dimensión", "parte del trabajo musical: audición, interpretación, creación o reflexión"), ("evidencia", "dato que se oye o se registra y que sostiene lo que digo"), ("bitácora", "libreta donde se anotan datos de cada ensayo")],
    [
        ("Separar fortaleza y área de crecimiento", f"{CAMI}. En interpretación, ¿cuál es la fortaleza y cuál el área de crecimiento de Camila?", ["Pulso estable: lo hace bien.", "6 errores de afinación: puede mejorar."], "Fortaleza: pulso estable. Área de crecimiento: afinación"),
        ("Calcular una proporción", f"{CAMI}. ¿Cuántos rasgos de los 5 pedidos no identificó en audición?", ["Identificó 4 de 5.", "5 − 4 = 1."], "1 rasgo"),
    ],
    [
        ("Decir «soy malo en música».", "Juzga a la persona y no dice qué mejorar.", "Escribe qué hiciste bien, qué puedes mejorar y el dato que lo muestra."),
        ("Compararse con otra persona para saber si se avanza.", "Cada quien parte de un lugar distinto.", "Compara con tu propia versión anterior."),
    ],
    [
        ex("Una fortaleza ¿es algo que hago bien con evidencia o algo que me gusta más que a otras personas?", "Algo que hago bien con evidencia", "Se apoya en un dato que lo muestra."),
        ex(f"{CAMI}. ¿Cuántos errores de afinación tuvo Camila en la frase?", "6", "Así lo indica la bitácora."),
        ex(f"{CAMI}. ¿En cuál de las cuatro dimensiones Camila varió dos veces su motivo?", "En la creación", "Inventar y variar un motivo es crear."),
    ],
    [
        ex("¿Qué frase sirve para analizar el trabajo musical? A) «Mantuve el pulso estable, pero tuve 6 errores de afinación.» B) «Soy malo para cantar.»", "A", "Muestra una fortaleza y un área de crecimiento con datos."),
        ex(f"{CAMI}. ¿Qué área de crecimiento muestra la creación de Camila? A) No terminó en la nota de reposo. B) Inventó un motivo.", "A", "Inventar el motivo es una fortaleza; no cerrar bien es el aspecto por mejorar."),
        ex("Una estudiante compara su práctica de esta semana con la de la semana pasada y no con la de una compañera. ¿Por qué es mejor? A) Porque cada persona parte de un lugar distinto. B) Porque la compañera practica más.", "A", "Comparar con la propia versión anterior muestra el avance personal."),
    ],
    [
        arith(f"{CAMI}. De sus 4 respuestas de reflexión, ¿cuántas justificó sin «porque»?", "4-2", "Se restan las respuestas justificadas del total.", " respuestas"),
        ex(f"{CAMI}. Camila compara dos proporciones: en audición identificó 4 de 5 rasgos y en reflexión justificó 2 de 4 respuestas. ¿En cuál dimensión tiene la menor proporción de logro?", "En reflexión", "Justificó la mitad (2 de 4), mientras que en audición logró 4 de 5, que es más de la mitad."),
        ex("Un comentario sobre un ensayo dice: «Tu tempo subió de 70 a 80 y tuviste menos errores». ¿Es una evidencia observable? Responde sí o no.", "Sí", "Contiene datos de tempo y errores que se pueden comprobar."),
    ],
    [
        ex(f"{CAMI}. Camila dice: «Soy mala para crear». ¿Qué afirmación con datos la reemplaza mejor? A) «Inventé un motivo y lo varié dos veces; me falta terminar en la nota de reposo.» B) «Soy buena en audición.»", "A", "Con datos, muestra una fortaleza y qué mejorar en la dimensión creación."),
        arith("En tres ensayos, Camila tuvo 6, 5 y 3 errores de afinación en la misma frase. ¿Cuántos errores bajó del primero al tercero?", "6-3", "Se restan los errores del último ensayo a los del primero.", " errores"),
    ],
    [
        arith("Un estudiante registra en una semana: 3 ensayos de 20 minutos, 2 sesiones de audición de 15 minutos y 1 sesión de creación de 25 minutos. ¿Cuántos minutos de trabajo musical suma?", "3*20+2*15+25", "Se multiplican las sesiones por sus minutos y se suman.", " minutos"),
        ex("Un compañero te dice que eres «el mejor del curso». ¿Qué conviene preguntarle para obtener información útil? A) En qué dimensión y con qué evidencia. B) Si él es peor que tú.", "A", "Pedir dimensión y evidencia convierte el elogio en información para mejorar."),
    ],
    [ex("Tu profesora te devuelve una nota en la que dice «necesitas mejorar». ¿Qué le preguntas para entender qué mejorar? A) En qué dimensión y con qué dato lo vio. B) Si hay otra nota más alta.", "A", "Con el dato sabes en qué trabajar.")],
    [ex("¿Cuáles son las cuatro dimensiones del trabajo musical?", "Audición, interpretación, creación y reflexión", "Son las áreas de análisis."), ex("¿Con quién conviene compararse para ver el avance?", "Con mi propia versión anterior", "Cada persona parte de un lugar distinto."), ex("¿Qué es un área de crecimiento?", "Algo que puedo mejorar, con evidencia", "No es un defecto fijo.")],
    (
        "Escribe tu propia bitácora de ejemplo para una semana imaginaria (con datos que inventes) con una entrada por dimensión: audición, interpretación, creación y reflexión. En cada una anota un dato. Luego marca una fortaleza y un área de crecimiento en dos dimensiones distintas, y escribe una frase que no juzgue a la persona.",
        "Audición: reconocí 3 de 4 rasgos. Interpretación: toqué una frase sin detenerme 2 de 3 veces. Creación: inventé un motivo de 4 notas. Reflexión: justifiqué 1 respuesta. Fortaleza: audición (3 de 4). Área de crecimiento: reflexión (justificar más veces). Frase: «Reconocí 3 de 4 rasgos; me falta justificar más con «porque»».",
        ["incluye las cuatro dimensiones", "cada entrada tiene un dato", "la frase final describe y no juzga a la persona"],
        ["bitácora con cuatro entradas", "fortaleza, área de crecimiento y frase"],
        ["frases del tipo «soy malo»", "entradas sin datos"],
        "Reconoce la bitácora y pide elegir un dato que cambiarías en una semana y explicar por qué.",
    ),
    "Anota una fortaleza y un área de crecimiento de tu última práctica musical, con un dato en cada una.",
    "Escribe qué evidencia usarías para saber si mejoras en audición durante un mes.",
)

# ---------------------------------------------------------------- OA 06 · clase 2 (influencia en el trabajo colectivo)
GRUPO = ("Grupo de ejemplo de cuatro estudiantes que prepara una pieza. Dani: su fortaleza es mantener el pulso; su área de crecimiento es leer partituras. "
         "Eli: su fortaleza es afinar; su área de crecimiento es entrar a tiempo. Fran: su fortaleza es proponer ideas para arreglar; su área de crecimiento es terminar lo que propone. "
         "Gabi: su fortaleza es explicar y anotar lo que ocurre en el ensayo; su área de crecimiento es tocar con volumen suave cuando acompaña")
L(
    OA6, 2,
    f"Lápiz y papel. Grupo de ejemplo, que se repite en los ejercicios: {GRUPO}.",
    "Aprenderé a analizar cómo mis fortalezas y mis áreas de crecimiento influyen en el trabajo del grupo, y a repartir roles para que el grupo aproveche lo que cada quien hace bien y apoye lo que cada quien debe mejorar. Sirve para trabajar mejor en colectivo.",
    ["Sé reconocer fortalezas y áreas de crecimiento con evidencia.", "Sé ensayar por etapas.", "Sé que cada voz o instrumento cumple un rol."],
    [
        "En un grupo musical, cada persona aporta con sus fortalezas y también necesita apoyo en sus áreas de crecimiento. Una fortaleza individual puede beneficiar a todo el grupo: quien mantiene el pulso ayuda a que todos entren juntos, y quien afina bien puede guiar a quienes tienen dudas. Un área de crecimiento también afecta al grupo: si alguien entra tarde, todos pierden el pulso. Por eso es útil conversarlo con respeto.",
        "Para analizar la influencia se hacen tres preguntas: ¿qué aporta mi fortaleza al grupo?, ¿cómo afecta mi área de crecimiento al resultado?, ¿qué apoyo puedo pedir y qué apoyo puedo dar? Un reparto de roles aprovecha las fortalezas: quien tiene buen pulso marca el tiempo; quien afina bien ayuda a ensayar las voces; quien propone ideas lidera el arreglo; quien anota lleva la bitácora. Y se acuerdan apoyos: una pareja que ensaya junta la parte difícil.",
        "Cuidado con dos errores: dejar siempre a la misma persona con la parte difícil, y tomar solo los roles que ya se dominan. El grupo también debe darle a cada integrante oportunidades de practicar su área de crecimiento. Las conversaciones se refieren a lo que sonó y no a cómo es cada quien. Si hay conflictos que no se resuelven hablando, se pide ayuda a la persona que dirige o a una persona adulta de confianza.",
    ],
    [("rol", "tarea que una persona cumple en el grupo"), ("aporte", "lo que una persona agrega al trabajo del grupo"), ("apoyo", "ayuda que se da o se pide para mejorar"), ("colectivo", "relativo al grupo"), ("acuerdo", "decisión tomada entre todas las personas del grupo")],
    [
        ("Asignar un rol según la fortaleza", f"{GRUPO}. ¿Quién conviene que marque el pulso con palmas suaves durante el ensayo?", ["Dani tiene como fortaleza mantener el pulso.", "El rol aprovecha esa fortaleza."], "Dani"),
        ("Pensar un apoyo", f"{GRUPO}. Eli tiene como área de crecimiento entrar a tiempo. ¿Quién puede apoyarla y cómo?", ["Dani mantiene el pulso.", "Puede darle una señal de entrada con la cabeza."], "Dani, con una señal de entrada"),
    ],
    [
        ("Dejar siempre la parte difícil a la misma persona.", "No permite que otras personas practiquen su área de crecimiento.", "Rota las partes y ofrece apoyo."),
        ("Hablar de cómo es cada quien en vez de lo que sonó.", "Genera conflicto y no dice qué mejorar.", "Habla de evidencia: tempo, entradas, afinación."),
    ],
    [
        ex(f"{GRUPO}. ¿Quién tiene como fortaleza afinar?", "Eli", "Así lo dice la descripción del grupo."),
        ex(f"{GRUPO}. ¿Quién tiene como área de crecimiento terminar lo que propone?", "Fran", "Así lo dice la descripción del grupo."),
        ex(f"{GRUPO}. ¿Qué rol conviene dar a Gabi, que explica y anota bien?", "Llevar la bitácora del ensayo", "Aprovecha su fortaleza de explicar y anotar."),
    ],
    [
        ex(f"{GRUPO}. ¿Cómo afecta al grupo que Eli entre tarde? A) Todos pierden el pulso y se desordena la entrada conjunta. B) El grupo suena más fuerte.", "A", "Una entrada tarde descoordina a las demás voces."),
        ex(f"{GRUPO}. ¿Qué rol aprovecha la fortaleza de Fran? A) Liderar las propuestas del arreglo. B) Marcar el pulso.", "A", "Fran propone ideas para arreglar."),
        ex("Un grupo reparte siempre la parte más difícil a la misma persona. ¿Qué pasa? A) Esa persona no puede practicar otras partes y las demás no practican la difícil. B) El grupo mejora porque hay un especialista.", "A", "Rotar permite que todas practiquen su área de crecimiento."),
    ],
    [
        ex(f"{GRUPO}. Gabi tiene como área de crecimiento tocar suave cuando acompaña. ¿Qué apoyo del grupo ayuda? A) Que le pidan bajar el volumen cuando entra la melodía y practiquen juntas esa parte. B) Que la dejen sin acompañar.", "A", "La práctica guiada ayuda a mejorar el área de crecimiento."),
        arith(f"{GRUPO}. Los 4 integrantes ensayan 3 veces por semana, 25 minutos cada vez, durante 4 semanas. ¿Cuántos minutos ensaya el grupo en total en esas semanas? Cuenta los minutos de grupo, no los de cada persona por separado.", "3*25*4", "Se multiplican las veces por semana, los minutos y las semanas.", " minutos"),
        ex(f"{GRUPO}. El grupo decide que quien marca el pulso rote cada semana entre las 4 personas. ¿Cuántas semanas necesitan para que todas lo hayan hecho una vez?", "4", "Cada semana lo hace una persona distinta."),
    ],
    [
        ex(f"{GRUPO}. Fran propone cinco cambios para el arreglo, pero termina solo dos. ¿Cómo puede el grupo apoyarla? A) Acordar entre todas un cambio por ensayo y registrarlo en la bitácora. B) Hacerle todas las tareas.", "A", "Un acuerdo concreto ayuda a completar lo que se propone."),
        arith(f"{GRUPO}. Fran propone 5 cambios y termina 2. ¿Qué parte de los cambios queda sin terminar, en cantidad?", "5-2", "Se restan los cambios terminados a los propuestos.", " cambios"),
    ],
    [
        ex("En un grupo, dos integrantes discuten porque uno dice que el otro «no sirve para tocar». ¿Qué respuesta ayuda más? A) Hablar de lo que sonó: «en el compás 5 la entrada llegó tarde» y proponer un apoyo. B) Seguir discutiendo hasta que uno cambie de grupo.", "A", "Los hechos y los apoyos concretos resuelven mejor que los juicios."),
        arith("Un grupo de 6 personas tiene 4 roles: pulso, afinación, propuestas y bitácora. Si cada rol lo cumplen personas distintas y quedan sin rol fijo las restantes, ¿cuántas personas quedan sin rol fijo?", "6-4", "Se restan las personas con rol a las del grupo.", " personas"),
    ],
    [ex("Si un conflicto del grupo no se resuelve conversando con respeto, ¿qué corresponde? A) Pedir ayuda a la persona que dirige o a una persona adulta de confianza. B) Dejar de hablar con la otra persona.", "A", "Pedir ayuda es una forma responsable de resolver el conflicto.")],
    [ex("¿Qué es un rol en un grupo?", "Una tarea que una persona cumple", "Ordena el trabajo colectivo."), ex("¿De qué debe hablar el grupo: de lo que sonó o de cómo es cada quien?", "De lo que sonó", "Se evalúa la música."), ex("¿Qué se acuerda entre todas las personas?", "Los roles y los apoyos", "Hace posible trabajar mejor juntas.")],
    (
        "Usa el grupo de ejemplo (Dani, Eli, Fran y Gabi). Arma un plan de ensayo de 20 minutos con estos roles: quien marca el pulso, quien guía la afinación, quien propone cambios y quien anota. Escribe: a) quién cumple cada rol y por qué, b) un apoyo para una de las áreas de crecimiento, c) cómo rotarán los roles.",
        "a) Pulso: Dani, porque mantiene el pulso. Afinación: Eli, porque afina bien. Propuestas: Fran, porque propone ideas. Anotar: Gabi, porque explica y anota. b) Dani da una señal de entrada a Eli. c) Cada ensayo rotan un puesto.",
        ["cada rol se justifica con una fortaleza de la descripción", "incluye un apoyo concreto", "propone una forma de rotar"],
        ["roles asignados con razón", "apoyo y rotación"],
        ["roles sin justificar", "dejar siempre la parte difícil a la misma persona"],
        "Reconoce el plan y pide explicar qué pasaría si falta una persona en el ensayo.",
    ),
    "Anota qué fortaleza tuya ayudaría a un grupo y qué apoyo pedirías para una de tus áreas de crecimiento.",
    "Escribe un acuerdo de tres líneas para que un grupo rote la parte más difícil de una pieza.",
)

# ---------------------------------------------------------------- OA 06 · clase 3 (plan de mejora)
META = ("Situación de ejemplo: Hugo tiene 6 errores de afinación en una frase de 8 compases y quiere bajar a 2 en 4 semanas. Dispone de 15 minutos al día, 5 días a la semana, y de su voz")
L(
    OA6, 3,
    f"Lápiz y papel; tarareo con volumen bajo si quieres practicar. Situación de ejemplo, que se repite en los ejercicios: {META}.",
    "Aprenderé a ensayar una decisión de mejora: escribir una meta específica, medible y con plazo, elegir acciones concretas y definir cómo sabré si avanzo. Sirve para que mis áreas de crecimiento se conviertan en pasos reales.",
    ["Sé reconocer áreas de crecimiento con evidencia.", "Sé comparar versiones con datos.", "Sé calcular minutos y tiempos."],
    [
        "Un plan de mejora convierte un área de crecimiento en acciones. Tiene cinco partes. Primero, la meta: debe ser específica (qué voy a mejorar), medible (con un número) y con plazo (para cuándo). «Cantar mejor» no es una meta; «bajar de 6 a 2 errores de afinación en 4 semanas» sí lo es. Segundo, las acciones: cosas que puedo hacer, como practicar la frase despacio y cantarla con una guía. Tercero, el tiempo disponible. Cuarto, la evidencia: qué voy a medir y cuándo. Quinto, el apoyo.",
        "Un buen plan es realista. Se calcula el tiempo disponible: 15 minutos al día durante 5 días son 75 minutos a la semana, y en 4 semanas son 300 minutos. También se divide la meta en pasos: si hay que bajar 4 errores en 4 semanas, se baja 1 error por semana. Cada semana se mide el avance con el mismo método, por ejemplo cantar la frase tres veces y contar los errores de cada vez.",
        "Si el avance no es el esperado, no hay que culparse: se revisa el plan y se cambia una acción o el plazo. Equivocarse al planificar también enseña. Un plan se escribe de forma sencilla, se pone a la vista y se comparte con alguien que pueda apoyar. Si la presión por mejorar produce mucha angustia o desánimo, se conversa con una persona adulta de confianza.",
    ],
    [("meta", "objetivo específico, medible y con plazo"), ("específica", "que dice con claridad qué se va a mejorar"), ("medible", "que tiene un número para comprobar el avance"), ("plazo", "fecha o tiempo en que se espera lograrla"), ("acción", "paso concreto que se hace para avanzar")],
    [
        ("Calcular el tiempo", f"{META}. ¿Cuántos minutos puede practicar Hugo en las 4 semanas?", ["15 minutos al día durante 5 días son 75 minutos por semana.", "75 × 4 = 300."], "300 minutos"),
        ("Dividir la meta en pasos", f"{META}. Si baja la misma cantidad de errores cada semana, ¿cuántos errores baja por semana?", ["Debe bajar de 6 a 2: son 4 errores.", "En 4 semanas, 1 por semana."], "1 error por semana"),
    ],
    [
        ("Escribir una meta como «cantar mejor».", "No es específica ni medible, y no tiene plazo.", "Agrega qué mejorar, un número y un plazo."),
        ("Esperar un avance parejo sin revisar el plan.", "Si no se mide, no se sabe si el plan funciona.", "Mide cada semana con el mismo método."),
    ],
    [
        ex(f"{META}. ¿Cuántas semanas dura el plazo?", "4", "Así lo indica la situación."),
        ex(f"{META}. ¿Cuántos errores quiere tener Hugo al final?", "2", "Su meta es bajar a 2."),
        ex("¿Qué número hace medible una meta de mejora: la cantidad de errores, o una impresión como «sonó mejor»?", "La cantidad de errores", "Un dato numérico permite comprobar el avance."),
    ],
    [
        ex("¿Cuál es una meta específica, medible y con plazo? A) Bajar de 6 a 2 errores de afinación en 4 semanas. B) Cantar mejor este año.", "A", "Tiene qué mejorar, un número y un plazo."),
        ex(f"{META}. ¿Qué acción es concreta para Hugo? A) Cantar la frase despacio tres veces cada día y contar los errores. B) Esforzarse más.", "A", "Es una acción que se puede realizar y medir."),
        ex(f"{META}. Si después de 2 semanas Hugo sigue con 6 errores, ¿qué conviene hacer? A) Revisar el plan y cambiar una acción. B) Abandonar la meta.", "A", "Un avance menor al esperado es información para ajustar."),
    ],
    [
        arith(f"{META}. ¿Cuántos minutos practica Hugo en una semana?", "15*5", "Se multiplican los minutos diarios por los días.", " minutos"),
        arith(f"{META}. Si Hugo cumple 4 de las 5 sesiones de una semana, ¿cuántos minutos practicó esa semana?", "15*4", "Se multiplican los minutos de cada sesión por las sesiones cumplidas.", " minutos"),
        ex(f"{META}. Hugo mide cantando la frase tres veces: tuvo 6, 5 y 7 errores. ¿Cuál es la menor cantidad de errores de las tres?", "5", "Es el valor más bajo de la lista."),
    ],
    [
        arith(f"{META}. Hugo quiere dedicar 25 minutos más a la semana a escuchar ejemplos. Con ese aumento, ¿cuántos minutos suma por semana entre práctica y audición?", "15*5+25", "Se suman los minutos de práctica diaria y los de audición.", " minutos"),
        ex(f"{META}. Una amiga le sugiere que su meta sea «ser el mejor cantante del curso». ¿Por qué no es buena para un plan? A) Porque depende de otras personas y no se puede medir en su propio avance. B) Porque es muy corta.", "A", "La meta debe depender del propio trabajo y tener un dato propio."),
    ],
    [
        arith("Una estudiante planifica bajar de 9 a 3 errores en 6 semanas, bajando la misma cantidad cada semana. ¿Cuántos errores baja por semana?", "(9-3)//6", "Se divide la diferencia entre las semanas.", " error por semana"),
        ex("Una estudiante tiene 10 minutos al día, 3 días a la semana, durante 4 semanas. Quiere practicar al menos 90 minutos en total. ¿Alcanza el tiempo? Responde sí o no.", "Sí", "Dispone de 10 × 3 × 4 = 120 minutos, que son más que 90."),
    ],
    [ex(f"{META}. El jueves Hugo no puede practicar porque tiene una actividad familiar. ¿Qué es una buena decisión? A) Recuperar 15 minutos el sábado y anotarlo. B) Dejar la meta.", "A", "Un ajuste razonable mantiene el plan.")],
    [ex("¿Cuáles son las tres características de una buena meta?", "Específica, medible y con plazo", "Permiten saber si se logró."), ex("¿Qué haces si el plan no da resultado?", "Reviso el plan y cambio una acción", "Se usa la evidencia para ajustar."), ex("Si una meta baja 4 errores en 4 semanas, ¿cuántos baja por semana?", "1", "4 dividido en 4.")],
    (
        "Elige un área de crecimiento (por ejemplo, entrar a tiempo, afinar, mantener el pulso o improvisar) y escribe un plan de mejora con datos que inventes: a) meta específica, medible y con plazo, b) tiempo disponible por semana y total, c) dos acciones concretas, d) cómo medirás el avance cada semana, e) quién puede apoyarte.",
        "a) Entrar a tiempo en 4 de 4 ensayos en 3 semanas (hoy entro a tiempo 1 de 4). b) 15 minutos por día, 4 días: 60 minutos por semana; 180 en 3 semanas. c) Contar mentalmente 4 pulsos antes de entrar; practicar la entrada con palmas. d) Cada semana anotaré en cuántos de 4 ensayos entré a tiempo. e) Mi compañera Eli me da la señal.",
        ["la meta es específica, medible y con plazo", "los cálculos de tiempo son correctos", "incluye acciones, medición y apoyo"],
        ["plan con cinco partes", "cálculos de tiempo"],
        ["meta sin número", "no explicar cómo se mide"],
        "Reconoce el plan y pide cambiar un dato (por ejemplo, el plazo) y recalcular el tiempo total.",
    ),
    "Escribe una meta de mejora musical para una semana con un número y una fecha.",
    "Divide una meta de 6 semanas en 3 pasos de 2 semanas y define qué medirás en cada paso.",
)

# ---------------------------------------------------------------- OA 06 · clase 4 (proponer alternativas de desarrollo)
RESTR = ("Situación de ejemplo: Ines quiere mejorar su pulso, pero en su casa no tiene instrumentos ni un lugar donde hacer ruido, y solo dispone de 12 minutos al día. "
         "Alternativas: 1) marcar el pulso con palmas suaves a 80 pulsos por minuto mientras oye una canción con auriculares a volumen bajo; 2) comprar un instrumento caro; 3) ensayar con volumen muy alto; 4) tararear y caminar al pulso en un lugar seguro")
L(
    OA6, 4,
    f"Lápiz y papel. Situación de ejemplo, que se repite en los ejercicios: {RESTR}.",
    "Aprenderé a proponer alternativas para desarrollar un área de crecimiento y a elegir la más adecuada según tres criterios: si sirve al objetivo, si es posible con mis recursos y si es segura y respetuosa. Sirve para no quedarme sin opciones cuando mi primer plan no se puede cumplir.",
    ["Sé escribir una meta específica, medible y con plazo.", "Sé calcular el tiempo disponible.", "Sé reconocer áreas de crecimiento con evidencia."],
    [
        "A veces el primer plan no se puede cumplir: falta un instrumento, un lugar o tiempo. Entonces se piensan alternativas, que son otras maneras de lograr el mismo objetivo. Para elegir entre ellas se usan tres criterios. Primero, que sirva al objetivo: debe trabajar de verdad la dimensión que se quiere mejorar. Segundo, que sea posible con los recursos, el tiempo y el espacio que se tienen. Tercero, que sea segura y respetuosa: sin dañar los oídos, la voz ni a otras personas.",
        "Una alternativa puede descartarse por no cumplir un criterio. Comprar un instrumento caro quizás sirva al objetivo, pero no es posible si no hay dinero. Ensayar con volumen muy alto puede servir, pero no es seguro ni respetuoso. Marcar el pulso con palmas suaves mientras se oye una canción sirve para el pulso, es posible sin instrumentos y es seguro y respetuoso, de modo que cumple los tres criterios.",
        "Conviene tener un plan A y un plan B. Si el plan A no funciona, el B ya está pensado. También se puede combinar: practicar con palmas en días de poco tiempo y con instrumento cuando hay más. Las alternativas se evalúan con datos: si después de dos semanas el avance medido no cambia, se prueba otra. Si algo no sale, no es un fracaso, es una prueba que da información para elegir mejor.",
    ],
    [("alternativa", "otra manera de lograr el mismo objetivo"), ("criterio", "regla para comparar y elegir"), ("plan B", "alternativa preparada por si el plan A no funciona"), ("recursos", "tiempo, espacio, dinero y materiales con que se cuenta"), ("descartar", "dejar de lado una opción por no cumplir un criterio")],
    [
        ("Descartar con un criterio", f"{RESTR}. ¿Por qué se descarta la alternativa 3?", ["Ensayar con volumen muy alto no es seguro.", "También molesta a otras personas."], "Porque no es segura ni respetuosa"),
        ("Elegir las alternativas que cumplen los tres criterios", f"{RESTR}. ¿Cuáles alternativas sirven al objetivo, son posibles y son seguras?", ["Las alternativas 2 y 3 se descartan.", "La 1 y la 4 cumplen los tres criterios."], "Las alternativas 1 y 4"),
    ],
    [
        ("Elegir una alternativa sin revisar si es posible.", "Una opción imposible no se puede cumplir.", "Verifica tiempo, espacio y dinero."),
        ("Pensar que cambiar de plan es fracasar.", "Cambiar el plan con datos es parte de mejorar.", "Prepara un plan B antes de empezar."),
    ],
    [
        ex(f"{RESTR}. ¿Cuántos minutos al día tiene Ines para practicar?", "12", "Así lo dice la situación."),
        ex(f"{RESTR}. ¿Qué área quiere mejorar Ines?", "El pulso", "Así lo dice la situación."),
        ex(f"{RESTR}. ¿Por qué la alternativa 2 no es posible para Ines?", "Porque no tiene recursos para comprar un instrumento caro", "No cumple el criterio de recursos."),
    ],
    [
        ex(f"{RESTR}. ¿Qué criterio incumple la alternativa 3? A) Ser segura y respetuosa. B) Servir al objetivo.", "A", "Un volumen muy alto daña el oído y molesta."),
        ex("¿Qué es un plan B? A) Una alternativa preparada por si el plan A no funciona. B) El mismo plan A escrito otra vez.", "A", "Permite seguir avanzando sin empezar de cero."),
        ex(f"{RESTR}. Ines duda entre la alternativa 1 y la 4. ¿Qué dato conviene para decidir? A) Medir durante una semana con cuál mantiene mejor el pulso. B) Elegir la que le parece más divertida sin medir.", "A", "Un dato de avance permite elegir con evidencia."),
    ],
    [
        arith(f"{RESTR}. Si Ines practica con la alternativa 1 durante 12 minutos al día, 6 días a la semana, ¿cuántos minutos practica en una semana?", "12*6", "Se multiplican los minutos diarios por los días.", " minutos"),
        arith(f"{RESTR}. A 80 pulsos por minuto, ¿cuántas palmas da Ines en los 12 minutos de práctica de un día?", "80*12", "Se multiplican los pulsos por minuto por los minutos.", " palmas"),
        ex(f"{RESTR}. Ines propone combinar la alternativa 1 (días de semana) con la 4 (fines de semana). ¿Cumplen las dos los tres criterios? Responde sí o no.", "Sí", "Las dos sirven al pulso, son posibles y seguras."),
    ],
    [
        ex(f"{RESTR}. Después de 2 semanas con la alternativa 1, el pulso de Ines no mejora: marca 80 pulsos por minuto pero se atrasa en la segunda mitad. ¿Qué cambio de alternativa es razonable? A) Probar la 4: caminar y tararear al pulso para sentirlo en el cuerpo. B) Abandonar la meta.", "A", "Es otra alternativa válida que trabaja el pulso con el cuerpo."),
        arith("Una estudiante tiene 4 alternativas y descarta 1 por insegura y 1 por imposible. ¿Cuántas alternativas válidas le quedan?", "4-1-1", "Se restan las alternativas descartadas.", " alternativas"),
    ],
    [
        ex("Una estudiante quiere mejorar su improvisación, pero no tiene instrumento. Alternativas: A) improvisar con la voz sobre una base de palmas, B) esperar a tener un instrumento caro, C) improvisar a gritos. ¿Cuál cumple los tres criterios?", "A", "Sirve a la improvisación, es posible sin instrumento y es segura."),
        arith("Un plan A prevé 5 sesiones por semana de 15 minutos y un plan B prevé 3 sesiones de 20 minutos. ¿Cuántos minutos más a la semana suma el plan A?", "5*15-3*20", "Se calculan los minutos semanales de cada plan y se restan.", " minutos"),
    ],
    [ex(f"{RESTR}. Tu amiga Ines comenta que se siente muy desanimada porque no avanza. ¿Qué es lo más adecuado? A) Escucharla y sugerirle que lo converse con una persona adulta de confianza si el desánimo continúa. B) Decirle que no se esfuerce.", "A", "Escuchar y sugerir apoyo adulto es una forma de cuidar.")],
    [ex("¿Cuáles son los tres criterios para elegir una alternativa?", "Sirve al objetivo, es posible y es segura y respetuosa", "Permiten comparar con orden."), ex("¿Qué es un plan B?", "Una alternativa preparada de antemano", "Se usa si el plan A no funciona."), ex("¿Con qué se evalúa una alternativa?", "Con datos de avance", "Un dato permite saber si funciona.")],
    (
        "Elige un área de crecimiento y una restricción (sin instrumento, poco tiempo o sin lugar para hacer ruido). Escribe cuatro alternativas, evalúa cada una con los tres criterios (sí o no) y elige tu plan A y tu plan B. Después escribe qué dato medirías para saber si cambias de plan.",
        "Área: afinación; restricción: poco tiempo (10 minutos). Alternativas: 1) tararear una frase y compararla con una grabación (sirve, posible, seguro); 2) tomar clases caras (no posible); 3) cantar fuerte toda la tarde (no seguro); 4) cantar la frase tres veces y contar errores (sirve, posible, seguro). Plan A: 4; plan B: 1. Dato: errores por semana.",
        ["propone cuatro alternativas distintas", "evalúa con los tres criterios", "indica plan A, plan B y dato de medición"],
        ["tabla de cuatro alternativas con criterios", "plan A, plan B y dato"],
        ["alternativas imposibles o inseguras", "no medir"],
        "Reconoce la elección y pide explicar qué dato haría pasar del plan A al plan B.",
    ),
    "Escribe dos formas distintas de practicar tu pulso en casa sin instrumentos y evalúalas con los tres criterios.",
    "Prepara un plan A y un plan B para mejorar tu audición y define cuándo cambiarías de uno a otro.",
)

# ---------------------------------------------------------------- OA 06 · clase 5 (registrar y contrastar el avance)
AV = ("Registro de ejemplo de Joaquín, semana 1 y semana 4, en la misma frase de 8 compases cantada tres veces. Semana 1: errores de afinación 6, 7 y 5; entró a tiempo 1 de 3 veces; 70 pulsos por minuto. "
      "Semana 4: errores de afinación 4, 3 y 2; entró a tiempo 3 de 3 veces; 80 pulsos por minuto")
L(
    OA6, 5,
    f"Lápiz y papel. Registro de ejemplo, que se repite en los ejercicios: {AV}.",
    "Aprenderé a registrar mi avance con los mismos indicadores en dos momentos y a contrastar el antes y el después para concluir qué mejoró, qué no y qué decido hacer. Sirve para sostener con datos mi análisis de fortalezas y áreas de crecimiento.",
    ["Sé escribir una meta medible.", "Sé proponer alternativas.", "Sé calcular diferencias y promedios simples."],
    [
        "Para saber si un plan de mejora funciona hay que registrar el avance con los mismos indicadores en dos o más momentos. Un indicador es un dato que se mide siempre igual, como los errores de afinación en una frase, las veces que se entra a tiempo o el tempo con que se canta sin errores. Si el método cambia entre una medición y otra, la comparación no sirve. Se registran la fecha, la frase, el método y los resultados.",
        "Para contrastar, se calcula la diferencia entre el antes y el después. En el registro de ejemplo, el promedio de errores de la semana 1 es (6 + 7 + 5) ÷ 3 = 6, y el de la semana 4 es (4 + 3 + 2) ÷ 3 = 3. La diferencia es 3 errores menos. También se miran los otros indicadores: pasó de entrar a tiempo 1 de 3 veces a 3 de 3 (2 veces más), y el tempo subió 10 pulsos por minuto. Con esos datos se concluye qué mejoró y qué aún falta.",
        "Una conclusión honesta dice qué mejoró, en cuánto y con qué evidencia, y reconoce los límites: tres cantos en una semana son pocos datos, y los errores pudieron variar por cansancio. Luego se decide qué mantener, qué cambiar y cuál será la siguiente meta. El registro habla de la música que se hizo y no de cuánto vale la persona. Compartirlo con quien dirige o con una persona adulta de confianza ayuda a seguir.",
    ],
    [("indicador", "dato que se mide siempre de la misma forma para seguir un avance"), ("promedio", "suma de varios valores dividida por la cantidad de valores"), ("diferencia", "resultado de restar el valor inicial del final"), ("límite", "aspecto que no permite concluir con total seguridad"), ("conclusión", "afirmación que se apoya en los datos")],
    [
        ("Calcular promedios", f"{AV}. ¿Cuál es el promedio de errores de la semana 4?", ["Los errores son 4, 3 y 2.", "(4 + 3 + 2) ÷ 3 = 3."], "3 errores"),
        ("Concluir con datos", f"{AV}. ¿Qué mejoró entre la semana 1 y la semana 4 en la entrada a tiempo?", ["Semana 1: 1 de 3.", "Semana 4: 3 de 3.", "Mejoró en 2 entradas."], "Entró a tiempo 2 veces más"),
    ],
    [
        ("Cambiar el método de medición entre una semana y otra.", "No se puede comparar si los indicadores cambian.", "Mide siempre la misma frase, el mismo número de veces y con el mismo método."),
        ("Sacar una conclusión definitiva con muy pocos datos.", "Tres intentos pueden variar por cansancio o suerte.", "Indica los límites y sigue midiendo."),
    ],
    [
        ex(f"{AV}. ¿A cuántos pulsos por minuto cantó Joaquín en la semana 4?", "80", "Así lo indica el registro."),
        ex(f"{AV}. ¿Cuántas veces entró a tiempo en la semana 1?", "1", "Así lo indica el registro."),
        ex("En Música: ¿Qué es un indicador?", "Un dato que se mide siempre de la misma forma", "Permite seguir un avance."),
    ],
    [
        ex(f"{AV}. ¿En qué semana tuvo menos errores de afinación? A) En la semana 4. B) En la semana 1.", "A", "En la semana 4 tuvo 4, 3 y 2, valores menores que 6, 7 y 5."),
        ex("¿Por qué conviene medir siempre la misma frase? A) Para que la comparación sea justa. B) Para cantar más rápido.", "A", "Si cambia la frase, cambia la dificultad y la comparación falla."),
        ex(f"{AV}. Joaquín dice: «Mejoré mucho, soy un genio». ¿Qué le falta a esa afirmación? A) Los datos que sostienen la mejora. B) Más adjetivos.", "A", "Una conclusión se apoya en datos del registro."),
    ],
    [
        arith(f"{AV}. ¿Cuál es el promedio de errores de la semana 1? Suma 6, 7 y 5 y divide entre 3.", "(6+7+5)//3", "La suma es 18 y se divide entre 3.", " errores"),
        arith(f"{AV}. ¿Cuántos pulsos por minuto subió el tempo entre la semana 1 y la 4?", "80-70", "Se restan los pulsos de la semana 1 a los de la 4.", " pulsos por minuto"),
        ex(f"{AV}. Un compañero concluye: «Mejoró en todo, para siempre». ¿Qué límite tiene su conclusión? A) Son pocos datos de dos semanas. B) Nunca se pueden usar datos.", "A", "La evidencia disponible no asegura el futuro."),
    ],
    [
        arith(f"{AV}. ¿Cuántos errores menos hubo en promedio en la semana 4 que en la semana 1?", "6-3", "Se restan los promedios de la semana 4 a los de la semana 1.", " errores"),
        ex(f"{AV}. La meta de Joaquín era tener 2 errores de promedio. ¿La alcanzó en la semana 4? Responde sí o no.", "No", "Su promedio fue 3, que es mayor que 2."),
    ],
    [
        arith("En otro registro, una estudiante tiene errores de 8, 6 y 4 en la semana 1, y 5, 3 y 1 en la semana 3. ¿Cuánto bajó el promedio de errores?", "(8+6+4)//3-(5+3+1)//3", "Los promedios son 6 y 3; se restan.", " errores"),
        ex(f"{AV}. Joaquín decide seguir con su plan, pero ahora medirá en 5 intentos y no en 3, para tener más datos. ¿Qué límite reduce? A) El de pocos datos. B) El del tempo.", "A", "Medir más veces reduce la influencia de un resultado fortuito."),
    ],
    [ex(f"{AV}. Después de ver su registro, Joaquín decide su siguiente meta. ¿Cuál es razonable? A) Bajar a 2 errores de promedio y mantener la entrada a tiempo en 3 de 3, a 80 pulsos por minuto. B) Cantar mejor.", "A", "La meta es específica, medible y parte de los datos.")],
    [ex("¿Qué se calcula para contrastar el antes y el después?", "La diferencia", "Se restan los valores."), ex("¿Qué debe cambiar entre una medición y la otra: el método o el momento?", "El momento", "El método debe mantenerse igual."), ex("¿Qué se hace después de la conclusión?", "Se decide qué mantener, cambiar y la siguiente meta", "El registro sirve para decidir.")],
    (
        "Crea tu propio registro con datos que inventes: semana 1 y semana 3, la misma frase cantada o tocada tres veces, con tres indicadores (errores, veces que entras a tiempo y tempo). Calcula el promedio de errores de cada semana, la diferencia y escribe una conclusión con un límite y la siguiente meta.",
        "Semana 1: errores 5, 6 y 4 (promedio 5); entré a tiempo 1 de 3; 70 pulsos por minuto. Semana 3: errores 3, 2 y 1 (promedio 2); entré a tiempo 2 de 3; 76. Diferencia: 3 errores menos. Conclusión: mejoré la afinación y la entrada; el límite es que son solo tres intentos. Siguiente meta: promedio 1 y 3 de 3 entradas en 3 semanas.",
        ["usa los mismos indicadores en ambas semanas", "calcula bien promedios y diferencia", "la conclusión incluye un límite y una nueva meta"],
        ["dos registros con tres indicadores", "promedios, diferencia y conclusión"],
        ["cambiar el método entre semanas", "conclusión sin límites"],
        "Reconoce el registro y pide indicar qué dato añadirías para tener una conclusión más sólida.",
    ),
    "Anota dos datos de tu práctica de hoy que podrías medir de la misma forma la próxima semana.",
    "Escribe una conclusión de tres líneas sobre tu avance en una habilidad, con un dato y un límite.",
)
