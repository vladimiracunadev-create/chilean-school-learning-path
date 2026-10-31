"""Cuaderno del estudiante, 5.º básico Historia, Geografía y Ciencias Sociales: OA 18 (proyecto escolar con plan y presupuesto)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA18 = "HI05 OA 18"
E = ex


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def tiers(recovery, understand, apply, reason, challenge):
    return {"recovery": recovery, "understand": understand, "apply": apply, "reason": reason, "challenge": challenge}


register(
    OA18, 1,
    materials="Este cuaderno y un lápiz. Los datos de la escuela de ejemplo están escritos en los ejercicios.",
    use="Aprenderé a ubicar un problema de la comunidad escolar (agua, electricidad, medioambiente o voluntariado) y las partes de un proyecto. Sirve para empezar un proyecto sabiendo qué problema se quiere resolver.",
    prior=["Sé que cuidar el medioambiente y los espacios comunes es una actitud cívica.", "Sé que la participación es un derecho y una responsabilidad."],
    explain=[
        "Un proyecto escolar es un plan para resolver un problema de la comunidad de la escuela. Puede tratar sobre el gasto excesivo de agua o de electricidad, el cuidado del medioambiente o una campaña de voluntariado, como ayudar a un hogar de ancianos o limpiar un espacio. Lo primero es ubicar el problema: qué ocurre, dónde y desde cuándo.",
        "Un proyecto tiene partes. El problema describe lo que no funciona. El objetivo dice qué se quiere lograr. El plan lista las actividades, quién las hace y en qué plazo. El presupuesto calcula cuánto dinero y materiales se necesitan. La evaluación revisa si se logró lo propuesto.",
        "Ubicar el problema con datos evita proyectos inútiles. Por ejemplo, decir «gastamos mucha agua» es vago. Decir «la llave del baño de la planta baja gotea desde el lunes» indica dónde y desde cuándo, y permite proponer una solución concreta.",
    ],
    vocab=[("proyecto", "plan con objetivo, actividades, plazos y recursos para resolver un problema"), ("objetivo", "lo que se quiere lograr"), ("plazo", "tiempo en que se hará una actividad"), ("presupuesto", "cálculo del dinero que se necesita"), ("voluntariado", "trabajo que se hace por decisión propia para ayudar, sin recibir pago")],
    worked=[
        W("Ubicar un problema", "Frase vaga: «la escuela gasta mucha luz». Frase precisa: «en la sala 5.º A las 8 luces quedan encendidas en el recreo». ¿Cuál sirve para empezar un proyecto?",
          ["Busco dónde y cuándo.", "La segunda dice la sala y el momento.", "Permite proponer una solución concreta."], "La segunda"),
        W("Partes de un proyecto", "«Poner un recordatorio para apagar luces» y «instalar carteles el lunes». ¿Qué parte del proyecto son?",
          ["Son actividades con plazo.", "Pertenecen al plan.", "No son el objetivo ni el presupuesto."], "El plan (actividades y plazos)"),
    ],
    mistakes=[
        M("Plantear un problema sin decir dónde ni desde cuándo.", "No se puede resolver algo tan general.", "Describe lugar y momento."),
        M("Empezar con las actividades antes de definir el objetivo.", "Sin objetivo no se sabe si se logró algo.", "Primero el problema y el objetivo."),
    ],
    tiers=tiers(
        [E("Lo que se quiere lograr con un proyecto, ¿es el objetivo o el presupuesto?", "El objetivo", "El presupuesto calcula el dinero."),
         E("El cálculo del dinero que necesita un proyecto, ¿es el presupuesto o el plazo?", "El presupuesto", "Es el cálculo de gastos."),
         E("Trabajar por decisión propia para ayudar, sin pago, ¿es voluntariado o empleo?", "Voluntariado", "No recibe pago.")],
        [E("¿Qué partes tiene un proyecto escolar?", "Problema, objetivo, plan, presupuesto y evaluación", "Son las partes de la clase."),
         E("¿Por qué conviene decir dónde y desde cuándo ocurre un problema?", "Para poder proponer una solución concreta", "Un problema preciso se resuelve mejor."),
         E("¿Para qué sirve la evaluación de un proyecto?", "Para revisar si se logró el objetivo", "Se compara lo hecho con lo propuesto.")],
        [E("Clasifica cada tema como agua, electricidad o medioambiente: a) llave que gotea; b) luces encendidas sin nadie; c) basura en el patio.", "a agua; b electricidad; c medioambiente", "Cada caso se relaciona con un recurso."),
         E("Describe con precisión un problema: llave que gotea en el baño del primer piso desde el lunes. ¿Qué datos aporta: lugar y momento, o solo la cantidad de agua?", "Lugar y momento", "Dice dónde y desde cuándo."),
         arith("Una escuela de ejemplo tiene 3 baños con 2 llaves cada uno. ¿Cuántas llaves hay que revisar en total?", "3*2", "Se multiplican los baños por las llaves de cada uno.")],
        [E("Pía dice: «Nuestro problema es que todo está mal». ¿Qué falta para empezar un proyecto?", "Precisar qué, dónde y desde cuándo", "El problema debe ser concreto."),
         E("Un curso empieza a pintar carteles sin saber qué quiere lograr. ¿Qué parte olvidó: el objetivo o el presupuesto?", "El objetivo", "Sin objetivo no sabe qué lograr.")],
        [E("Ordena el comienzo de un proyecto: A) fijar el objetivo, B) describir el problema, C) planificar actividades.", "B, A, C", "Primero el problema, luego el objetivo y después las actividades."),
         arith("Un proyecto dura 4 semanas. Ya pasó 1 semana. ¿Cuántas semanas faltan?", "4-1", "Se resta la semana transcurrida del plazo total.", " semanas")],
    ),
    context=[E("En una escuela de ejemplo, el patio se llena de papeles a la hora de almuerzo y hay solo un basurero. ¿Qué tema de proyecto es: electricidad o medioambiente?", "Medioambiente", "Se trata de basura y cuidado del patio.")],
    selfcheck=[E("¿Qué es un proyecto escolar?", "Un plan para resolver un problema de la escuela", "Es la definición de la clase."), E("¿Qué es el presupuesto?", "El cálculo del dinero que se necesita", "Es la definición del vocabulario."), E("¿Qué es un voluntariado?", "Trabajar por decisión propia para ayudar sin pago", "Es la definición del vocabulario.")],
    open_task=task("Elige uno de estos problemas de ejemplo: a) el baño gotea; b) las luces quedan encendidas en el recreo; c) se pierde basura en el patio; d) un hogar de ancianos cercano necesita compañía (las visitas se harían con profesores). Escribe el problema con lugar y momento, el objetivo y dos actividades.", "Problema: la llave del baño del primer piso gotea desde el lunes. Objetivo: que deje de gotear. Actividades: avisar a la dirección, revisar cada semana.", ["precisa lugar y momento", "escribe un objetivo claro", "propone dos actividades"], ["ficha de tres partes"], ["describir el problema de forma vaga", "no escribir objetivo"], "Pide a una persona que diga si entiende cuál es el problema."),
    reinforce="Observa tu escuela o casa y anota un lugar donde se gasta agua o luz de más.",
    extend="Escribe cómo podría ayudar un voluntariado a una persona mayor de tu barrio.",
)

register(
    OA18, 2,
    materials="Este cuaderno y un lápiz. Las tablas y textos están escritos en los ejercicios.",
    use="Aprenderé a usar datos y fuentes (una tabla de consumo, una boleta, una encuesta) para entender el problema y a preguntar quién los produjo. Sirve para que el proyecto se apoye en información confiable.",
    prior=["Sé las partes de un proyecto.", "Sé que una fuente tiene procedencia."],
    explain=[
        "Para conocer un problema usamos datos. Una boleta de agua o de luz muestra cuánto se consumió en un mes. Una tabla de registro puede anotar cuántas luces quedan encendidas cada día. Una encuesta pregunta a los compañeros su opinión o sus hábitos. Cada fuente se hace de una manera y tiene límites.",
        "Hay que preguntar por la procedencia: quién midió, cuándo, cómo y para qué. Una encuesta con pocos respondientes no representa a toda la escuela. Un registro de un solo día no muestra lo que pasa durante el mes. Los datos con unidades claras, como litros o kWh, son más fáciles de comparar.",
        "También conviene cruzar fuentes. Si la boleta muestra más consumo y el registro de luces encendidas también, los datos se apoyan entre sí. Si no coinciden, hay que investigar más antes de decidir.",
    ],
    vocab=[("boleta", "documento que muestra cuánto se consumió y cuánto cuesta"), ("registro", "anotación ordenada de lo que se observa"), ("encuesta", "serie de preguntas a varias personas"), ("kWh", "unidad con que se mide la electricidad consumida"), ("muestra", "grupo pequeño que representa a uno mayor")],
    worked=[
        W("Leer una boleta", "Boleta de ejemplo: marzo, 20.000 litros de agua; abril, 26.000 litros. ¿Cuánto aumentó el consumo?",
          ["Comparo ambos meses.", "26.000 menos 20.000.", "Aumentó 6.000 litros."], "6.000 litros"),
        W("Límite de una encuesta", "Una encuesta se hizo a 5 de 150 estudiantes. ¿Representa a toda la escuela?",
          ["Pregunto cuántos respondieron.", "5 de 150 es muy poco.", "No representa a toda la escuela."], "No; es una muestra muy pequeña"),
    ],
    mistakes=[
        M("Tomar un dato de un solo día como si fuera de todo el mes.", "Un día no muestra el patrón completo.", "Pide datos de varios días."),
        M("Comparar datos sin mirar las unidades.", "Litros y kWh no se comparan.", "Revisa que usen la misma unidad."),
    ],
    tiers=tiers(
        [E("Un documento que muestra cuánto se consumió y cuánto cuesta, ¿es una boleta o una encuesta?", "Una boleta", "La encuesta pregunta opiniones."),
         E("Una serie de preguntas a varias personas, ¿es una encuesta o un registro?", "Una encuesta", "Sirve para conocer opiniones o hábitos."),
         E("Los litros, ¿miden el agua o la electricidad?", "El agua", "El kWh mide la electricidad.")],
        [E("¿Qué datos de procedencia conviene preguntar a una tabla de consumo?", "Quién midió, cuándo y cómo", "Así se juzga su confianza."),
         E("¿Por qué una encuesta con pocas personas no representa a toda la escuela?", "Porque la muestra es muy pequeña", "Pocas respuestas no muestran a todos."),
         E("¿Qué conviene hacer si dos fuentes no coinciden?", "Investigar más antes de decidir", "No se debe elegir sin más información.")],
        [arith("Boleta de ejemplo: abril 26.000 litros y mayo 22.000 litros. ¿Cuántos litros bajó el consumo?", "26000-22000", "Se resta el consumo de mayo al de abril.", " litros"),
         arith("Registro de ejemplo: lunes 3 luces encendidas, martes 5, miércoles 4. ¿Cuántas luces encendidas se anotaron en total?", "3+5+4", "Se suman los tres días."),
         E("Encuesta de ejemplo a 20 estudiantes: 14 apagan la luz al salir y el resto no. ¿Cuántos no la apagan?", "6", "20 menos 14 son 6.", "20-14")],
        [E("Sofía mide el consumo de agua solo un lunes y concluye: «Todo el mes gastamos igual». ¿Qué error tiene?", "Un día no muestra todo el mes", "Faltan más datos."),
         E("Una tabla da «Sala A: 120» y otra «Sala B: 120» pero una está en litros y la otra en kWh. ¿Se pueden comparar? Responde sí o no.", "No", "Las unidades son distintas.")],
        [E("Ordena los pasos para usar una fuente: A) decidir cómo usar el dato, B) revisar quién la hizo, C) leer el dato.", "B, C, A", "Primero la procedencia, luego el dato y luego su uso."),
         E("Consumo de luz de tres meses: enero 3.000, febrero 2.800, marzo 2.600 kWh. ¿Aumentó o bajó mes a mes?", "Bajó", "300, 280 y 260 son cada vez menos.")],
    ),
    context=[E("Una tabla de ejemplo dice que el gasto de agua subió de 20.000 a 26.000 litros. El conserje cuenta que una llave del baño gotea. ¿Las dos fuentes se apoyan entre sí? Responde sí o no.", "Sí", "La llave que gotea puede explicar el aumento.")],
    selfcheck=[E("¿Qué es una boleta?", "Un documento que muestra cuánto se consumió y cuesta", "Es la definición del vocabulario."), E("¿Por qué preguntar quién midió un dato?", "Para saber si es confiable", "Es la procedencia."), E("¿Un día de datos muestra todo el mes?", "No", "Faltan más días.")],
    open_task=task("Datos de ejemplo: consumo de agua del colegio: marzo 20.000 litros, abril 26.000 litros, mayo 28.000 litros. Encuesta a 30 estudiantes: 18 dicen que a veces dejan la llave abierta. Escribe cuánto aumentó el consumo entre marzo y mayo, qué dice la encuesta, una limitación de los datos y una pregunta para conseguir otra fuente.", "Aumentó 8.000 litros. 18 de 30 dejan la llave abierta. Límite: son datos de un colegio y solo tres meses. Pregunta: ¿cuántas llaves gotean?", ["calcula el aumento", "interpreta la encuesta", "señala una limitación y una pregunta"], ["cuatro frases"], ["olvidar la limitación", "mezclar unidades"], "Revisa tus cálculos con una persona de tu casa."),
    reinforce="Anota cuántas veces abres la llave de agua en una mañana en tu casa.",
    extend="Escribe una pregunta para una encuesta sobre el uso de la luz en tu curso.",
)

register(
    OA18, 3,
    materials="Este cuaderno y un lápiz. Los casos están escritos en los ejercicios.",
    use="Aprenderé a relacionar las causas de un problema escolar, los actores que pueden ayudar y las consecuencias de actuar o no. Sirve para planificar actividades con responsables y plazos.",
    prior=["Sé ubicar un problema y leer datos.", "Sé armar causas y consecuencias."],
    explain=[
        "Un problema tiene causas. El gasto excesivo de agua puede tener como causa una llave que gotea, personas que dejan la llave abierta o un tubo roto. El gasto excesivo de electricidad puede tener como causa luces encendidas sin necesidad. Descubrir la causa evita arreglar solo lo que se ve.",
        "Los actores son quienes pueden ayudar: estudiantes, profesores, auxiliares, la dirección y las familias. En un plan se anota qué actividad hará cada uno y para cuándo. Una actividad sin responsable y sin plazo no se cumple. Por ejemplo: «Revisar las llaves cada viernes; responsable: dos estudiantes del curso».",
        "Las consecuencias de actuar son ahorrar agua y electricidad, cuidar el medioambiente y gastar menos dinero. Las de no actuar son mayor gasto y desorden. Un plan que reparte tareas y plazos aumenta las posibilidades de lograr el objetivo.",
    ],
    vocab=[("causa", "razón por la que ocurre un problema"), ("responsable", "persona que se encarga de una actividad"), ("cronograma", "lista de actividades con sus fechas"), ("hábito", "costumbre que se repite"), ("ahorro", "gastar menos de lo habitual")],
    worked=[
        W("Buscar la causa", "El consumo de agua subió. Se descubre una llave que gotea. ¿Cuál es la causa y cuál la solución?",
          ["Causa: la llave que gotea.", "Solución: repararla.", "Después revisar si bajó el consumo."], "Causa: la llave que gotea; solución: repararla"),
        W("Responsable y plazo", "Actividad: «Revisar las llaves del patio». ¿Qué falta para que se cumpla?",
          ["Falta quién lo hará.", "Falta cuándo.", "Con responsable y plazo se puede cumplir."], "Un responsable y un plazo"),
    ],
    mistakes=[
        M("Resolver solo lo que se ve sin buscar la causa.", "El problema puede volver.", "Pregunta por qué ocurre."),
        M("Anotar actividades sin responsable ni plazo.", "Nadie sabe cuándo ni quién debe hacerlas.", "Agrega responsable y fecha."),
    ],
    tiers=tiers(
        [E("Una costumbre que se repite, ¿es un hábito o un cronograma?", "Un hábito", "El cronograma lista actividades con fechas."),
         E("La persona que se encarga de una actividad, ¿es el responsable o el elector?", "El responsable", "Es quien la hace."),
         E("Gastar menos de lo habitual, ¿es ahorro o gasto?", "Ahorro", "El gasto es lo contrario.")],
        [E("¿Por qué conviene buscar la causa de un problema?", "Para que no vuelva a ocurrir", "Se evita arreglar solo lo visible."),
         E("¿Qué debe tener cada actividad de un plan?", "Un responsable y un plazo", "Si no, nadie sabe quién ni cuándo."),
         E("¿Qué consecuencia tiene actuar para ahorrar agua?", "Se cuida el medioambiente y se gasta menos dinero", "Son beneficios del ahorro.")],
        [E("Causas posibles de un alto gasto de luz: a) luces encendidas sin nadie; b) ampolletas de bajo consumo. ¿Cuál es una causa real del alto gasto?", "a", "Las luces encendidas sin uso consumen electricidad."),
         E("Actividad: «Apagar luces al terminar el recreo». ¿Quién puede ser el responsable: un grupo de estudiantes o nadie?", "Un grupo de estudiantes", "Debe haber alguien a cargo."),
         arith("El plan dice revisar 4 llaves cada viernes durante 5 viernes. ¿Cuántas revisiones de llave se harán en total?", "4*5", "Se multiplican las llaves por los viernes.")],
        [E("Gabo dice: «No importa por qué se gasta agua, basta con pedir que gasten menos». ¿Qué error tiene?", "Hay que descubrir la causa para solucionarla", "Si hay una fuga, pedir ahorro no basta."),
         E("Un plan dice «Alguien limpiará el patio algún día». ¿Qué le falta?", "Un responsable y una fecha", "Sin esos datos no se cumple.")],
        [E("Ordena la cadena: A) baja el gasto de agua, B) se detecta una fuga y se repara, C) sube el gasto por una fuga.", "C, B, A", "Primero el problema, luego la reparación y después el efecto."),
         arith("Un cronograma tiene 6 actividades y ya se hicieron 4. ¿Cuántas faltan?", "6-4", "Se resta las hechas del total.")],
    ),
    context=[E("Una escuela de ejemplo quiere gastar menos luz. Los estudiantes anotan que las luces del pasillo quedan encendidas todo el día. ¿Cuál puede ser una actividad con responsable: «Un delegado de turno apaga las luces del pasillo a las 14:00» o «Que alguien las apague»?", "«Un delegado de turno apaga las luces del pasillo a las 14:00»", "Tiene responsable y hora.")],
    selfcheck=[E("En Historia: ¿Qué es una causa?", "La razón por la que ocurre un problema", "Es la definición del vocabulario."), E("¿Qué es un cronograma?", "Una lista de actividades con sus fechas", "Es la definición del vocabulario."), E("¿Qué necesita cada actividad?", "Un responsable y un plazo", "Para poder cumplirse.")],
    open_task=task("Caso de ejemplo: en la escuela se usa demasiada agua porque dos llaves gotean y algunos estudiantes dejan la llave abierta. Escribe la causa, tres actores que pueden ayudar, tres actividades con responsable y plazo (por ejemplo, «revisar llaves, delegados de curso, cada viernes») y una consecuencia esperada.", "Causas: llaves que gotean y hábitos. Actores: estudiantes, auxiliar, dirección. Actividades: reparar llaves (auxiliar, esta semana), campaña (curso, dos semanas), revisión (delegados, viernes). Consecuencia: bajar el consumo.", ["identifica las causas", "asigna responsable y plazo a cada actividad", "indica una consecuencia esperada"], ["cronograma de tres filas"], ["actividades sin responsable", "plazos imprecisos"], "Pide a una persona que diga qué actividad no queda clara."),
    reinforce="Escribe una actividad de ahorro de agua para tu casa con responsable y día.",
    extend="Escribe qué adulto de tu escuela podría ayudar a un proyecto y por qué.",
)

register(
    OA18, 4,
    materials="Este cuaderno y un lápiz. Las opciones de proyecto están escritas en los ejercicios.",
    use="Aprenderé a comparar dos alternativas de proyecto según su costo, su impacto y las perspectivas de quienes participan. Sirve para elegir la mejor solución para la comunidad escolar.",
    prior=["Sé armar un plan con responsables y plazos.", "Sé comparar con criterios."],
    explain=[
        "Un mismo problema puede resolverse de varias maneras. Para elegir, comparamos alternativas con los mismos criterios: cuánto cuestan, cuánto ayudan al problema, cuánto tardan y cuántas personas pueden participar. A veces la solución más barata no es la que más ayuda, y a veces la más cara no cabe en el presupuesto.",
        "También comparamos perspectivas. Los estudiantes pueden querer una campaña llamativa. Los profesores pueden preferir algo que no interrumpa las clases. El auxiliar puede saber dónde están las fugas. La dirección debe cuidar el dinero. Escuchar a todos mejora el plan.",
        "Se puede comparar con otras escuelas que hicieron proyectos parecidos: qué resultados tuvieron, qué problemas enfrentaron y qué no volverían a hacer. Aprender de otros ahorra errores, pero el plan debe adaptarse a la realidad de cada escuela.",
    ],
    vocab=[("alternativa", "una de las opciones posibles"), ("impacto", "cuánto ayuda una solución a resolver el problema"), ("costo", "dinero y esfuerzo que requiere algo"), ("viabilidad", "posibilidad real de llevar algo a cabo"), ("adaptar", "cambiar algo para que sirva en otra realidad")],
    worked=[
        W("Comparar alternativas", "Alternativa A: reparar dos llaves, cuesta $6.000 y baja el gasto mucho. Alternativa B: carteles, cuesta $4.000 y baja el gasto poco. ¿Cuál tiene más impacto?",
          ["Comparo el impacto.", "A baja mucho; B poco.", "A tiene más impacto aunque cueste más."], "La alternativa A"),
        W("Perspectivas", "Los profesores no quieren interrupciones. ¿Qué adaptación del plan respeta esa perspectiva?",
          ["Pienso en el horario.", "Hacer la campaña en el recreo.", "Así no interrumpe las clases."], "Hacer la campaña en el recreo"),
    ],
    mistakes=[
        M("Elegir siempre la alternativa más barata.", "Puede no resolver el problema.", "Compara costo e impacto."),
        M("Copiar un proyecto de otra escuela sin adaptarlo.", "Cada escuela tiene necesidades distintas.", "Adapta a tu realidad."),
    ],
    tiers=tiers(
        [E("Una de las opciones posibles, ¿es una alternativa o un cronograma?", "Una alternativa", "El cronograma es una lista de fechas."),
         E("Cuánto ayuda una solución a resolver un problema, ¿es el impacto o el costo?", "El impacto", "El costo es el dinero y esfuerzo."),
         E("Cambiar algo para que sirva en otra realidad, ¿es adaptar o copiar?", "Adaptar", "Copiar no cambia nada.")],
        [E("¿Por qué conviene comparar alternativas con los mismos criterios?", "Para elegir de manera justa y con información", "Se miden igual todas las opciones."),
         E("¿Por qué escuchar las perspectivas de profesores y auxiliares mejora el plan?", "Porque cada uno conoce aspectos distintos del problema", "Aportan información útil."),
         E("¿Qué se aprende de proyectos de otras escuelas?", "Qué resultados tuvieron y qué errores evitar", "Ahorra errores propios.")],
        [E("Alternativa A cuesta $8.000 y resuelve el problema por completo. Alternativa B cuesta $3.000 y lo resuelve a medias. Si hay $10.000, ¿cuál se puede elegir y resuelve más?", "A", "Cabe en el presupuesto y resuelve todo."),
         arith("Con la alternativa A de $8.000 y un presupuesto de $10.000, ¿cuánto dinero sobra?", "10000-8000", "Se resta el costo al presupuesto.", " pesos"),
         E("Otra escuela hizo carteles que nadie leyó. ¿Qué conviene adaptar en tu escuela: ponerlos en lugares muy vistos o repetirlos igual?", "Ponerlos en lugares muy vistos", "Se corrige el error de la otra escuela.")],
        [E("Hugo dice: «Lo más barato siempre es mejor». ¿Qué error tiene?", "Puede no resolver el problema", "Hay que comparar costo e impacto."),
         E("Un proyecto necesita 20 personas pero solo hay 8 voluntarios. ¿Tiene viabilidad tal como está? Responde sí o no.", "No", "Faltan personas para hacer todas las tareas.")],
        [E("Ordena de mayor a menor impacto: A) reparar la fuga, B) pedir que se ahorre sin reparar, C) no hacer nada.", "A, B, C", "Reparar resuelve la causa, pedir ahorro ayuda algo y no hacer nada no ayuda."),
         arith("Una alternativa cuesta $4.500 y otra $7.000. ¿Cuántos pesos más cuesta la segunda?", "7000-4500", "Se resta el menor costo al mayor.", " pesos")],
    ),
    context=[E("Dos cursos proponen cuidar el agua: uno propone repartir folletos ($5.000) y otro reparar una llave ($6.000). La escuela tiene $10.000 y quiere que baje de verdad el consumo. ¿Qué alternativa conviene más?", "Reparar la llave", "Resuelve la causa del gasto y cabe en el presupuesto.")],
    selfcheck=[E("¿Qué es el impacto de una solución?", "Cuánto ayuda a resolver el problema", "Es la definición del vocabulario."), E("En Historia: ¿Qué es una alternativa?", "Una de las opciones posibles", "Es la definición del vocabulario."), E("¿Qué se debe hacer con un proyecto de otra escuela?", "Adaptarlo a tu realidad", "No se copia igual.")],
    open_task=task("Compara estas dos alternativas para ahorrar luz de ejemplo: A) cambiar 8 ampolletas por modelos de bajo consumo, costo $24.000, reduce mucho el gasto; B) campaña de carteles y recordatorios, costo $6.000, reduce algo el gasto. Presupuesto disponible: $20.000. Compara con costo, impacto y viabilidad, escribe una decisión que cabe en el presupuesto y la perspectiva de un profesor o del director.", "A cuesta $4.000 más de lo disponible, no es viable por ahora. B cabe. Decisión: empezar con B y ahorrar para A. Perspectiva del director: cuidar el dinero.", ["usa los tres criterios", "decisión coherente con el presupuesto", "incluye una perspectiva"], ["tabla de criterios y una decisión"], ["elegir sin mirar el presupuesto", "ignorar el impacto"], "Pide a una persona que diga si cambiaría la decisión y por qué."),
    reinforce="Escribe dos formas de ahorrar agua en tu casa y cuál ayudaría más.",
    extend="Escribe una pregunta que le harías a un curso que hizo un proyecto parecido.",
)

register(
    OA18, 5,
    materials="Este cuaderno y un lápiz. Los precios están escritos en los ejercicios.",
    use="Aprenderé a armar y justificar un presupuesto con evidencia, calculando totales y comprobando que el dinero alcance. Sirve para que el proyecto se pueda hacer de verdad.",
    prior=["Sé comparar alternativas de proyecto.", "Sé calcular con números en el cuaderno."],
    explain=[
        "Un presupuesto es una lista de los materiales y servicios que necesita el proyecto, con su precio. Cada fila indica el ítem, la cantidad, el precio unitario y el total. El total del proyecto se obtiene sumando todos los totales. Si el total es mayor que el dinero disponible, hay que ajustar el plan.",
        "Para justificar un presupuesto usamos evidencia: cotizaciones o precios de ejemplo, la cantidad que realmente se necesita y el beneficio esperado. Por ejemplo: 4 carteles a $1.500 cada uno cuestan $6.000. Si reparar una llave cuesta $5.000 y evita el gasto de 600 litros por mes, el beneficio justifica el gasto.",
        "Un buen presupuesto deja un pequeño margen para imprevistos y no gasta más de lo disponible. También se debe llevar un registro de los gastos reales para compararlos con lo planeado.",
    ],
    vocab=[("ítem", "cada cosa que aparece en una lista de gastos"), ("precio unitario", "precio de una sola unidad"), ("total", "suma de todos los montos"), ("imprevisto", "gasto que no estaba planeado"), ("cotización", "precio que ofrece un proveedor antes de comprar")],
    worked=[
        W("Calcular un total", "Ítem: 4 carteles a $1.500 cada uno. ¿Cuánto cuestan en total?",
          ["Multiplico cantidad por precio unitario.", "4 × 1.500.", "Resulta $6.000."], "$6.000"),
        W("Comprobar el presupuesto", "Presupuesto: $20.000. Gastos planeados: $6.000 en carteles y $9.000 en una reparación. ¿Alcanza?",
          ["Sumo los gastos: 6.000 + 9.000 = 15.000.", "15.000 es menor que 20.000.", "Sobran 5.000."], "Sí, sobran $5.000"),
    ],
    mistakes=[
        M("Calcular el presupuesto sin sumar todos los ítems.", "Puede faltar dinero.", "Suma cada fila y revisa el total."),
        M("Gastar todo el dinero sin dejar margen.", "Pueden aparecer imprevistos.", "Deja un pequeño margen."),
    ],
    tiers=tiers(
        [E("Cada cosa que aparece en una lista de gastos, ¿es un ítem o un imprevisto?", "Un ítem", "El imprevisto no estaba planeado."),
         E("El precio de una sola unidad, ¿es el precio unitario o el total?", "El precio unitario", "El total suma todas."),
         E("Un gasto que no estaba planeado, ¿es un imprevisto o una cotización?", "Un imprevisto", "La cotización es un precio ofrecido.")],
        [E("¿Qué se hace para obtener el total de un ítem?", "Se multiplica la cantidad por el precio unitario", "Así se calcula cada fila."),
         E("¿Qué se hace si el total supera el dinero disponible?", "Ajustar el plan", "No se puede gastar más de lo que hay."),
         E("¿Para qué sirve comparar gastos reales con los planeados?", "Para ver si se cumplió el presupuesto", "Permite controlar el gasto.")],
        [arith("Presupuesto: 4 carteles a $1.500 cada uno. ¿Cuántos pesos cuestan?", "4*1500", "Se multiplica la cantidad por el precio unitario.", " pesos"),
         arith("Presupuesto: 3 carteles a $2.000 cada uno y una reparación de $5.000. ¿Cuál es el total?", "3*2000+5000", "Se suman los totales de cada ítem.", " pesos"),
         arith("El curso tiene $20.000 y planea gastar $14.500. ¿Cuánto dinero queda?", "20000-14500", "Se resta lo planeado al dinero disponible.", " pesos")],
        [E("Lola dice: «Mi presupuesto es $9.000 aunque mis ítems suman $11.000». ¿Qué error tiene?", "El total debe ser la suma de los ítems", "No se puede decir menos del costo real."),
         E("Un curso planea gastar exactamente todo su dinero sin margen. ¿Qué riesgo corre?", "No poder pagar un imprevisto", "Siempre puede surgir un gasto inesperado.")],
        [E("Ítems: 5 lápices a $200 cada uno y 2 cartulinas a $500 cada una. Presupuesto de $2.500. ¿Alcanza? Responde sí o no.", "Sí", "5×200 son 1.000, 2×500 son 1.000; el total 2.000 es menor que 2.500."),
         arith("Reparar una llave cuesta $5.000 y ahorra 600 litros de agua por mes. ¿Cuántos litros ahorra en 4 meses?", "600*4", "Se multiplica el ahorro mensual por los meses.", " litros")],
    ),
    context=[arith("Un curso quiere hacer un huerto con 4 bolsas de tierra a $2.500 cada una y 6 plantas a $1.000 cada una. ¿Cuánto cuesta en total?", "4*2500+6*1000", "Se suman los totales de tierra y plantas.", " pesos")],
    selfcheck=[E("¿Qué es un ítem?", "Cada cosa de una lista de gastos", "Es la definición del vocabulario."), E("¿Cómo se obtiene el total de un presupuesto?", "Sumando los totales de todos los ítems", "Así se calcula el costo completo."), E("¿Por qué dejar un margen?", "Por los imprevistos", "Pueden surgir gastos no planeados.")],
    open_task=task("Arma el presupuesto de un proyecto de ejemplo para ahorrar agua con estos precios: llave nueva $4.000, 2 horas de un gasfíter a $3.000 cada una, 5 carteles a $800 cada uno. Presupuesto disponible: $15.000. Escribe una tabla con ítem, cantidad, precio unitario y total; calcula el total del proyecto, cuánto sobra y una evidencia que justifique el gasto.", "Llave 1×4.000=4.000; gasfíter 2×3.000=6.000; carteles 5×800=4.000. Total 14.000. Sobra 1.000. Evidencia: la llave gotea y pierde agua.", ["tabla con cuatro columnas", "total y saldo correctos", "justifica con evidencia"], ["tabla y tres frases"], ["no multiplicar cantidad por precio", "pasarse del presupuesto"], "Pide a una persona que recalcule los totales y compara."),
    reinforce="Anota los precios de tres útiles escolares y calcula cuánto cuestan 5 de uno de ellos.",
    extend="Escribe cómo registrarías los gastos reales de un proyecto de curso.",
)

register(
    OA18, 6,
    materials="Este cuaderno y un lápiz. Los resultados están escritos en los ejercicios.",
    use="Aprenderé a evaluar si un proyecto cumplió su objetivo, su plan y su presupuesto, y a tomar decisiones para mejorarlo. Sirve para aprender de lo hecho y seguir mejorando.",
    prior=["Sé armar un presupuesto.", "Sé que un proyecto tiene objetivo, plan, presupuesto y evaluación."],
    explain=[
        "Evaluar un proyecto es comparar lo que se hizo con lo que se había propuesto. Se revisan tres cosas. Primero, el objetivo: si el problema mejoró. Segundo, el plan: si se hicieron las actividades en los plazos. Tercero, el presupuesto: si el gasto real fue igual o menor al planeado.",
        "Para evaluar usamos datos. Si la meta era bajar el consumo de agua de 26.000 a 20.000 litros y bajó a 21.000, el objetivo se logró casi por completo. Si el gasto real fue $14.000 y el presupuesto era $15.000, se cumplió. Una evaluación honesta reconoce lo que salió bien y lo que no.",
        "Una decisión ciudadana al final del proyecto puede ser continuar, ajustar o terminar. Se decide con evidencia y escuchando a quienes participaron. También se comparte lo aprendido con la comunidad escolar para que otros cursos puedan hacer proyectos parecidos.",
    ],
    vocab=[("evaluar", "comparar lo logrado con lo propuesto"), ("meta", "resultado específico que se quiere alcanzar"), ("indicador", "dato que muestra si se logró algo"), ("ajustar", "cambiar el plan para mejorar"), ("lección aprendida", "algo útil que se aprendió de la experiencia")],
    worked=[
        W("Evaluar el objetivo", "Meta: bajar de 26.000 a 20.000 litros. Resultado: 21.000 litros. ¿Cuántos litros faltaron para la meta?",
          ["Comparo 21.000 con 20.000.", "Faltaron 1.000 litros.", "Se logró casi por completo."], "1.000 litros"),
        W("Evaluar el presupuesto", "Presupuesto: $15.000. Gasto real: $14.000. ¿Se cumplió?",
          ["Comparo 14.000 con 15.000.", "Gastó $1.000 menos.", "Sí se cumplió."], "Sí, gastó $1.000 menos"),
    ],
    mistakes=[
        M("Decir que el proyecto salió perfecto sin comparar con la meta.", "Sin datos no se sabe.", "Compara resultados con la meta."),
        M("Culpar a una persona si algo salió mal.", "Se evalúa el proyecto para aprender.", "Busca qué ajustar en el plan."),
    ],
    tiers=tiers(
        [E("Comparar lo logrado con lo propuesto, ¿es evaluar o ajustar?", "Evaluar", "Ajustar es cambiar el plan."),
         E("Un resultado específico que se quiere alcanzar, ¿es una meta o un imprevisto?", "Una meta", "El imprevisto no estaba planeado."),
         E("Algo útil que se aprendió de la experiencia, ¿es una lección aprendida o un indicador?", "Una lección aprendida", "El indicador es un dato.")],
        [E("¿Qué tres cosas se revisan al evaluar un proyecto?", "El objetivo, el plan y el presupuesto", "Son las tres partes de la clase."),
         E("¿Por qué una evaluación debe ser honesta?", "Para aprender de lo que salió bien y lo que no", "Así se mejora."),
         E("¿Qué puede decidirse al final de un proyecto?", "Continuar, ajustar o terminar", "Depende de la evidencia.")],
        [arith("Meta: bajar de 26.000 a 20.000 litros. Resultado: 21.000 litros. ¿Cuántos litros se redujeron en total?", "26000-21000", "Se resta el resultado al consumo inicial.", " litros"),
         arith("Presupuesto: $15.000. Gasto real: $14.000. ¿Cuánto menos se gastó?", "15000-14000", "Se resta el gasto real al presupuesto.", " pesos"),
         E("Actividades planeadas: 6. Actividades realizadas a tiempo: 5. ¿Se cumplió todo el plan? Responde sí o no.", "No", "Una actividad no se hizo a tiempo.")],
        [E("Mía dice: «El proyecto salió perfecto» sin mostrar datos. ¿Qué falta?", "Comparar con la meta usando datos", "Sin datos no se puede afirmar."),
         E("Un curso gastó $18.000 teniendo un presupuesto de $15.000. ¿Cumplió el presupuesto? Responde sí o no.", "No", "Gastó $3.000 más.")],
        [E("Ordena los pasos para evaluar: A) decidir qué ajustar, B) reunir los resultados, C) compararlos con la meta.", "B, C, A", "Primero datos, luego comparación y luego decisión."),
         arith("Una escuela de 300 estudiantes logra que 240 apaguen la luz al salir. ¿Cuántos estudiantes aún no lo hacen?", "300-240", "Se resta los que lo hacen al total.")],
    ),
    context=[E("Un curso logró bajar el consumo de agua, pero tardó dos semanas más de lo planeado y gastó lo previsto. ¿Qué parte del proyecto debe ajustarse la próxima vez: el plazo o el presupuesto?", "El plazo", "Fue lo que no se cumplió.")],
    selfcheck=[E("¿Qué es evaluar un proyecto?", "Comparar lo logrado con lo propuesto", "Es la definición de la clase."), E("En Historia: ¿Qué es una meta?", "Un resultado específico que se quiere alcanzar", "Es la definición del vocabulario."), E("¿Qué puede hacerse con una lección aprendida?", "Compartirla para mejorar futuros proyectos", "Ayuda a otros cursos.")],
    open_task=task("Datos de un proyecto de ejemplo: meta, bajar el consumo de luz de 3.000 a 2.400 kWh; resultado, 2.500 kWh; presupuesto $20.000, gasto real $19.000; actividades planeadas 5, hechas 4. Escribe si se cumplió el objetivo, el plan y el presupuesto, con una cifra para cada uno, y una decisión (continuar, ajustar o terminar) con una razón.", "Objetivo: faltaron 100 kWh. Plan: 4 de 5. Presupuesto: sobró $1.000. Decisión: ajustar el plan para completar la actividad que faltó.", ["evalúa objetivo, plan y presupuesto con cifras", "toma una decisión", "justifica con datos"], ["tres frases con cifras y una decisión"], ["afirmar sin datos", "decidir sin razones"], "Pide a una persona que diga si tu decisión es coherente con los datos."),
    reinforce="Escribe una meta con número para un proyecto sobre ahorro de agua.",
    extend="Escribe cómo contarías los resultados de un proyecto al resto de la escuela.",
)
