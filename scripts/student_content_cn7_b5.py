"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 15 (cambios físicos y químicos de la materia)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA15 = "CN07 OA 15"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ================================================================ OA 15, clase 1
register(
    OA15, 1,
    materials="Papel y lápiz. Para la tarea abierta: una manzana, un hielo en un plato, una hoja de papel, un reloj o celular y una regla. No pruebes los materiales ni uses calor.",
    use="Aprenderé a observar un cambio de la materia con cuidado, registrando antes, durante y después, sin concluir de inmediato. Sirve para tener evidencia antes de clasificar el cambio.",
    prior=["Sé distinguir observación de interpretación.", "Sé medir tiempo, masa y largo con unidades."],
    explain=[
        "Un cambio de la materia es una alteración en las propiedades de un material, como su forma, su color, su estado o su temperatura. Algunos cambios son rápidos, como romper un papel, y otros son lentos, como el color de una manzana cortada. Para estudiarlos conviene observar con calma y registrar los datos antes de decidir qué tipo de cambio es.",
        "Una buena observación se hace en tres momentos: antes del cambio, durante el cambio y después del cambio. En cada uno se anota qué se ve, qué se mide (masa en gramos, largo en centímetros, tiempo en minutos, temperatura en grados Celsius) y la hora. No se prueba ni se huele de cerca ningún material desconocido. Lo observado es el dato; lo que pensamos que pasó es una interpretación.",
        "Concluir de inmediato es un error frecuente: un solo dato, como un cambio de color, no basta para clasificar un cambio. Primero se acumulan observaciones; después, en las clases siguientes, se las compara con criterios para decidir si el cambio es físico o químico.",
    ],
    vocab=[("cambio de la materia", "alteración de las propiedades de un material"), ("propiedad", "característica que se observa o se mide, como color, forma o masa"), ("registro", "anotación ordenada de lo observado y medido"), ("interpretación", "explicación que agregamos a lo observado"), ("evidencia", "dato observado o medido que apoya una idea")],
    worked=[
        {"title": "Separar observación de interpretación", "problem": "Frases: A) «El trozo de manzana pasó de blanco a café claro en 30 minutos». B) «Cambió porque el aire le hizo algo». ¿Cuál es la observación?", "steps": ["A dice qué se ve y cuánto tardó.", "B explica una causa que no se midió."], "answer": "A es observación; B es interpretación"},
        {"title": "Calcular el tiempo del cambio", "problem": "Una manzana cortada se ve blanca a las 10:00, café claro a las 10:30 y café a las 11:15. ¿Cuántos minutos pasaron entre la primera y la última observación?", "steps": ["De 10:00 a 11:00 hay 60 minutos.", "Se suman 15 minutos: 60 + 15 = 75."], "answer": "75 minutos"},
    ],
    mistakes=[
        {"wrong": "Escribir «se oxidó» en la columna de observaciones de una manzana cortada.", "why": "Es una explicación, no un dato.", "fix": "Anota «pasó de blanco a café claro» y deja la explicación para después."},
        {"wrong": "Clasificar el cambio después de mirarlo un minuto.", "why": "Se concluye con una sola observación.", "fix": "Registra antes, durante y después, y compara con criterios."},
    ],
    tiers={
        "recovery": [
            ex("«El papel se rompió en cuatro pedazos». ¿Es una observación o una interpretación?", "Observación", "Dice lo que se ve."),
            ex("«El hielo se derrite porque el aire le pasa calor». ¿Es una observación o una interpretación?", "Interpretación", "Explica una causa que no se midió."),
            ex("¿En cuántos momentos se registra un cambio: antes, durante y después? Escribe el número.", "3", "Son los tres momentos de un buen registro."),
        ],
        "understand": [
            ex("¿Por qué conviene registrar la hora de cada observación?", "Para saber cuánto tarda el cambio", "El tiempo es un dato medible del cambio."),
            ex("Una compañera mira un trozo de pan por un minuto y dice «ya sé qué tipo de cambio es». ¿Qué error comete?", "Concluye con muy pocas observaciones", "Hay que acumular observaciones antes de clasificar."),
            ex("¿Cuál es una observación bien escrita: (a) «el hielo está raro» o (b) «el hielo pasó de 60 g a 0 g de sólido en 20 minutos»?", "(b)", "Tiene cifras y unidades."),
        ],
        "apply": [
            arith("Un hielo en un plato se registra a las 15:00 con 80 g de sólido y a las 15:40 con 20 g de sólido. ¿Cuántos gramos de hielo se derritieron en ese tiempo?", "80-20", "Se resta la masa final a la masa inicial.", " g"),
            ex("Una hoja de papel de 5 g se arruga hasta formar una bolita y se vuelve a pesar, sin que se pierda nada de papel. ¿Cuántos gramos marca la balanza?", "5 g", "Arrugar cambia la forma, no la cantidad de papel."),
            arith("Una banana pelada se registra a las 12:00 con 3 manchas cafés y a las 13:00 con 9 manchas cafés. ¿Cuántas manchas nuevas aparecieron en esa hora?", "9-3", "Se resta el dato inicial al dato final.", " manchas"),
        ],
        "reason": [
            ex("Ema anotó: «el pan se tuesta porque se quema». ¿Qué parte es interpretación y qué observación podría anotar en su lugar?", "«Porque se quema»; «el pan pasó de blanco a dorado»", "La observación describe el color, la interpretación pone la causa."),
            ex("Un grupo registró solo el estado final de un hielo: «agua». ¿Qué momentos le faltan al registro?", "Antes y durante", "Un registro completo tiene los tres momentos."),
        ],
        "challenge": [
            ex("Pedro midió un trozo de manzana al comienzo (blanco, 100 g) y a la hora (café, 98 g). Dice «se perdió masa porque el color cambió». ¿Qué dato falta para afirmar que el color causó la pérdida?", "Un trozo de control sin cambio de color con su masa", "Podría haberse perdido agua por evaporación; se necesita comparar."),
            ex("Una persona dice «algo cambió porque se ve distinto». ¿Qué datos medibles pedirías, además del aspecto?", "Masa, tiempo y temperatura, entre otros", "Las mediciones dan evidencia más firme que el aspecto."),
        ],
    },
    context=[ex("Una persona de tu casa deja una banana pelada sobre un plato. A la hora se ve con manchas cafés. ¿Cómo escribirías esto como observación?", "La banana pasó de amarilla a tener manchas cafés en una hora", "Una observación describe lo que se ve y cuándo.")],
    selfcheck=[
        ex("¿Qué tres momentos tiene un buen registro?", "Antes, durante y después", "Así se ve cómo evoluciona el cambio."),
        ex("¿Se puede clasificar un cambio con un solo dato? Responde sí o no.", "No", "Hay que acumular evidencia."),
        ex("En Ciencias: ¿Qué es una interpretación?", "Una explicación que agregamos a lo observado", "No es un dato medido."),
    ],
    open_task=task(
        "Observa tres cambios: un trozo de manzana cortada, un hielo en un plato y una hoja de papel que arrugas y desarrugas. Haz una tabla con tres columnas (antes, durante, después) y tres filas (una por material). Anota color, forma, masa si tienes balanza de cocina, y la hora. Marca con O las observaciones y con I las interpretaciones, y no escribas todavía si cada cambio es físico o químico.",
        "Manzana: antes, blanca, 10:00; durante, café claro, 10:30; después, café, 11:15. Hielo: antes, sólido; después, agua. Papel: antes, plano; después, arrugado.",
        ["tres materiales observados", "tres momentos por material", "marcas O e I", "sin clasificar todavía"],
        ["tabla de tres columnas y tres filas", "marcas O e I"],
        ["clasificar de inmediato", "anotar solo el estado final"],
        "Pregunta qué dato te falta para clasificar el cambio del papel.",
    ),
    reinforce="Elige un cambio de tu casa (leche que se agria, una fruta que madura) y escribe una observación antes, otra durante y otra después.",
    extend="Averigua con una persona de tu casa cómo reconoce que un alimento se echó a perder y qué cambios observa.",
)

# ================================================================ OA 15, clase 2
register(
    OA15, 2,
    materials="Papel y lápiz. Los registros están escritos en el cuaderno. No hace falta que repitas ninguna de las pruebas.",
    use="Aprenderé a reconocer los indicadores de un cambio químico y a ver que no todos son pruebas definitivas. Sirve para decidir qué más investigar.",
    prior=["Sé registrar un cambio antes, durante y después.", "Sé que hay cambios de estado como la fusión y la ebullición."],
    explain=[
        "En un cambio químico se forman sustancias nuevas, con propiedades distintas de las originales. Hay indicadores que sugieren que esto ocurrió: aparecen burbujas de un gas nuevo, cambia el color de forma permanente, se forma un sólido dentro de un líquido (como cuando la leche se corta), cambia la temperatura sin una fuente de calor externa, hay luz, o aparece un olor nuevo.",
        "Pero ningún indicador es una prueba definitiva por sí solo. Un cambio de estado también puede dar burbujas: cuando el agua hierve, las burbujas son de vapor de agua, la misma sustancia. Una tinta que se diluye cambia de color sin que se forme una sustancia nueva. Un hielo derritiéndose puede enfriar el vaso. Por eso se necesitan varios indicadores o pruebas adicionales, como comparar propiedades antes y después.",
        "Un buen razonamiento dice: «Vi X; X es un indicador de cambio químico; pero también puede pasar en cambios físicos; necesito otro dato». Los datos de esta clase son registros de ejemplo.",
    ],
    vocab=[("cambio químico", "cambio en el que se forman sustancias nuevas"), ("indicador", "señal que sugiere que ocurrió un cambio químico"), ("gas", "estado de la materia sin forma ni volumen propios"), ("sólido formado", "sólido que aparece dentro de un líquido tras un cambio"), ("prueba adicional", "otro dato que ayuda a decidir")],
    worked=[
        {"title": "Burbujas, pero de qué", "problem": "Se calienta agua pura en una olla con un adulto y aparecen burbujas desde el fondo a 100 °C. ¿Es indicador de cambio químico?", "steps": ["Las burbujas son vapor de agua, la misma sustancia.", "Es un cambio de estado (ebullición)."], "answer": "No; es ebullición, un cambio físico"},
        {"title": "Un conjunto de indicadores", "problem": "Registro de ejemplo: al mezclar bicarbonato con vinagre en un vaso aparecen burbujas, el sólido desaparece y la masa del vaso baja de 250 g a 248 g. ¿Qué indicadores hay?", "steps": ["Hay burbujas de un gas que antes no estaba.", "La masa baja porque el gas se escapa al aire."], "answer": "Formación de un gas nuevo (burbujas y pérdida de masa)"},
    ],
    mistakes=[
        {"wrong": "Decir que todo cambio de color es químico.", "why": "Se usa un solo indicador como prueba.", "fix": "Una tinta que se diluye cambia de color sin que se forme una sustancia nueva."},
        {"wrong": "Creer que toda burbuja es un gas nuevo.", "why": "Se confunden burbujas de vapor con un gas formado.", "fix": "En la ebullición las burbujas son del mismo líquido hecho vapor."},
    ],
    tiers={
        "recovery": [
            ex("Aparecen burbujas de un gas que antes no estaba en la mezcla. ¿Es un indicador de cambio químico? Responde sí o no.", "Sí", "Indica que se formó una sustancia nueva."),
            ex("Se forma un sólido dentro de un líquido que estaba claro. ¿Es un indicador de cambio químico? Responde sí o no.", "Sí", "Es un indicador de formación de una sustancia nueva."),
            ex("Una tinta que se diluye en agua cambia de color. ¿Se formó una sustancia nueva? Responde sí o no.", "No", "La tinta sigue siendo la misma, solo está diluida."),
        ],
        "understand": [
            ex("¿Por qué las burbujas del agua que hierve no son un indicador de cambio químico?", "Porque son vapor de agua, la misma sustancia", "Es un cambio de estado."),
            ex("¿Qué es un indicador de cambio químico: una señal que sugiere o una prueba definitiva?", "Una señal que sugiere", "Por sí solo, un indicador no es prueba."),
            ex("La leche se corta al agregarle jugo de limón y se forman grumos sólidos. ¿Qué indicador se observó?", "Formación de un sólido", "Aparece un sólido dentro de un líquido."),
        ],
        "apply": [
            arith("En un vaso abierto, la masa de otra mezcla de ejemplo era 310 g antes y 307 g después de que salieran burbujas. ¿Cuántos gramos de gas se escaparon?", "310-307", "El gas formado se escapó y la masa del vaso bajó.", " g"),
            ex("Se registra: hierve agua y sale vapor, sin cambio de olor ni de color. ¿Cuántos indicadores de cambio químico hay? Escribe el número.", "0", "Las burbujas de vapor no son un gas nuevo."),
            ex("Registro de ejemplo: un clavo en agua se cubre con una capa café-rojiza al cabo de varios días. ¿Qué indicador es?", "Cambio de color y formación de un sólido nuevo", "La capa café-rojiza es una sustancia nueva, el óxido."),
        ],
        "reason": [
            ex("Rosa dice: «Cambió de color, entonces es químico». Su registro es una gota de colorante de cocina que tiñó un vaso de agua. ¿Qué otro dato necesita?", "Si se formó una sustancia nueva; el colorante solo se diluyó", "El color por sí solo no basta."),
            ex("Registro: se mezclan dos polvos blancos en agua y el vaso se siente más frío, sin que aparezcan burbujas ni sólidos. Un compañero dice «es seguro que es químico». ¿Qué responderías?", "Falta evidencia; un solo indicador no basta", "Un cambio de temperatura puede darse también en cambios físicos."),
        ],
        "challenge": [
            ex("Registro 1: burbujas y olor nuevo. Registro 2: solo un cambio de color. ¿Cuál tiene más evidencia de cambio químico?", "El registro 1", "Tiene dos indicadores en lugar de uno."),
            ex("Un registro dice: «una bebida en polvo cambió de color al agregarle más agua». ¿Qué prueba adicional pedirías para decidir si hay una sustancia nueva?", "Evaporar el agua y ver si se recupera el mismo polvo", "Si se recupera la misma sustancia, fue un cambio físico."),
        ],
    },
    context=[ex("Una persona de tu casa deja una manzana cortada sobre la mesa y a la hora se pone café. ¿Qué indicador de cambio químico es y por qué no basta por sí solo?", "Cambio de color; no basta porque también hay cambios físicos que cambian el color", "Hay que sumar otras evidencias.")],
    selfcheck=[
        ex("Nombra dos indicadores de cambio químico.", "Por ejemplo, burbujas de un gas nuevo y formación de un sólido", "Cualquier par entre los indicadores de la clase."),
        ex("¿Un solo indicador es una prueba definitiva?", "No", "Se necesitan varios datos."),
        ex("¿Qué burbujas no indican cambio químico?", "Las del agua hirviendo", "Son vapor de agua."),
    ],
    open_task=task(
        "Lee estos tres registros de ejemplo. Registro A: un hielo se derrite en un plato y aparecen gotas en el borde. Registro B: se calienta agua pura con ayuda de un adulto y salen burbujas de vapor. Registro C: se deja un clavo húmedo varios días y aparece una capa café-rojiza que se desprende como polvo. Para cada registro escribe: los indicadores que ves, si alcanzan para afirmar un cambio químico, y qué prueba adicional pedirías.",
        "A: gotas, no son indicador; falta evidencia de una sustancia nueva. B: burbujas de vapor, no son indicador; prueba adicional: enfriar el vapor para recuperar agua. C: cambio de color y sólido nuevo, es indicador de cambio químico; prueba adicional: comprobar que el polvo no es el clavo.",
        ["tres registros analizados", "indicadores identificados", "prueba adicional razonable"],
        ["tabla con tres filas", "frase por registro"],
        ["tomar un solo indicador como prueba", "no pedir prueba adicional"],
        "Pregunta qué observarías para estar más seguro en el registro C.",
    ),
    reinforce="Escribe un ejemplo en que un cambio de color no es un cambio químico.",
    extend="Averigua con una persona de tu casa qué cambia en un huevo cuando se cocina y cuáles de los indicadores de la clase se observan.",
)

# ================================================================ OA 15, clase 3
register(
    OA15, 3,
    materials="Papel y lápiz. Los casos están escritos en el cuaderno. Para la tarea abierta: hielo, una cucharada de sal y un vaso con agua, para observar sin probar.",
    use="Aprenderé a comparar cambios reversibles con cambios en los que se forman sustancias nuevas. Sirve para clasificar un cambio como físico o químico con un criterio claro.",
    prior=["Conozco los indicadores de cambio químico.", "Sé que los cambios de estado conservan la sustancia."],
    explain=[
        "En un cambio físico no se forman sustancias nuevas: la sustancia sigue siendo la misma, aunque cambie su forma, su tamaño o su estado. Romper un papel, derretir hielo, disolver sal en agua o doblar un alambre son cambios físicos. Muchos de ellos se pueden revertir con métodos físicos: el agua líquida vuelve a ser hielo al enfriarse; la sal se recupera evaporando el agua.",
        "En un cambio químico se forman sustancias nuevas con propiedades distintas. Cocinar un huevo, oxidar un clavo, tostar pan o dejar que la leche se agrie son cambios químicos. Suelen ser difíciles o imposibles de revertir con métodos físicos: no se puede volver a obtener un huevo crudo.",
        "Atención: la reversibilidad es una pista y no la regla definitiva. Un papel rasgado no vuelve a unirse y, sin embargo, sigue siendo papel: es un cambio físico. El criterio principal es si se forman sustancias nuevas. Para decidir, pregúntate: ¿la sustancia original se puede recuperar con métodos físicos? ¿Las propiedades del producto son distintas?",
    ],
    vocab=[("cambio físico", "cambio en el que no se forman sustancias nuevas"), ("reversible", "que se puede volver al estado inicial"), ("irreversible", "que no se puede volver al estado inicial con métodos simples"), ("sustancia nueva", "sustancia con propiedades distintas de las originales"), ("oxidación", "cambio en que un metal como el hierro forma óxido")],
    worked=[
        {"title": "Clasificar con el criterio principal", "problem": "Se disuelve sal en agua y luego se evapora el agua: reaparece la sal. ¿El cambio fue físico o químico?", "steps": ["La sal se recuperó con un método físico.", "No se formó una sustancia nueva."], "answer": "Físico"},
        {"title": "Reversible no siempre es físico", "problem": "Un papel se rasga en cuatro pedazos y no se puede volver a unir. ¿Es un cambio químico?", "steps": ["Los pedazos siguen siendo papel.", "Aunque no se pueda revertir, no se formó una sustancia nueva."], "answer": "No; es físico, porque no hay sustancias nuevas"},
    ],
    mistakes=[
        {"wrong": "Decir que todo cambio irreversible es químico.", "why": "Se usa la reversibilidad como regla.", "fix": "El criterio principal es si se forman sustancias nuevas; un papel rasgado es físico."},
        {"wrong": "Decir que disolver sal es químico porque la sal desaparece.", "why": "Se confunde invisible con transformada.", "fix": "Si evaporas el agua, reaparece la sal: sigue siendo sal."},
    ],
    tiers={
        "recovery": [
            ex("Derretir hielo, ¿es un cambio físico o químico?", "Físico", "El agua sigue siendo agua."),
            ex("Cocinar un huevo, ¿es un cambio físico o químico?", "Químico", "Se forman sustancias nuevas con otras propiedades."),
            ex("Doblar un alambre de cobre, ¿es un cambio físico o químico?", "Físico", "Cambia su forma, pero sigue siendo cobre."),
        ],
        "understand": [
            ex("¿Cuál es el criterio principal para decir que un cambio es químico: que sea irreversible o que se formen sustancias nuevas?", "Que se formen sustancias nuevas", "La reversibilidad es solo una pista."),
            ex("¿Por qué un papel rasgado es un cambio físico, aunque no se pueda volver a unir?", "Porque sigue siendo papel y no se formó una sustancia nueva", "No hay sustancia nueva."),
            ex("Un trozo de cobre se funde y, al enfriarse, vuelve a ser cobre sólido. ¿Es un cambio físico o químico?", "Físico", "Es la misma sustancia que cambió de estado."),
        ],
        "apply": [
            ex("Clasifica en el orden dado: oxidar un clavo, romper una galleta, tostar pan. Escribe Q para químico y F para físico.", "Q, F, Q", "Oxidar y tostar forman sustancias nuevas; romper solo cambia la forma."),
            arith("Se disuelven 20 g de sal en 180 g de agua. Al evaporar toda el agua se recuperan 20 g de sal. ¿Cuántos gramos tenía la disolución antes de evaporar?", "20+180", "La disolución tiene la masa de la sal más la del agua.", " g"),
            ex("Un hielo de 120 g se derrite por completo y no se pierde nada. ¿Cuántos gramos pesa el agua líquida?", "120 g", "Un cambio físico conserva la masa."),
        ],
        "reason": [
            ex("Luis dice que, como la leche agria no vuelve a ser leche fresca, es un cambio físico. ¿Qué criterio olvidó y cuál es la clasificación correcta?", "Si se forman sustancias nuevas; es un cambio químico", "La leche agria tiene sustancias nuevas con otro olor y otra textura."),
            ex("Una compañera dice que, como el hielo se puede volver agua y de nuevo hielo, es un cambio químico reversible. ¿Qué dato lo contradice?", "El agua sigue siendo la misma sustancia", "No se formó una sustancia nueva."),
        ],
        "challenge": [
            ex("Un cambio produce un gas nuevo y, con otro procedimiento, se puede volver al material inicial. Una persona dice «si es reversible, es físico». ¿Qué respuesta corresponde?", "No; si se formó un gas nuevo hubo un cambio químico, aunque se pueda revertir", "La reversibilidad no define el tipo de cambio."),
            ex("Se mezclan arena y sal secas. ¿Es un cambio químico? Justifica con el criterio principal.", "No; no se forman sustancias nuevas y se pueden separar", "Ambas sustancias conservan sus propiedades."),
        ],
    },
    context=[ex("Una persona deja un clavo húmedo al aire libre y aparece óxido. Otra persona derrite hielo en la mano. ¿Cuál de los dos cambios forma una sustancia nueva?", "El del clavo", "El óxido es una sustancia nueva y el agua sigue siendo agua.")],
    selfcheck=[
        ex("¿Qué se forma en un cambio químico y no en uno físico?", "Sustancias nuevas", "Es el criterio principal."),
        ex("¿Reversible significa siempre físico?", "No", "Es una pista, no la regla."),
        ex("¿Disolver sal en agua es físico o químico?", "Físico", "La sal se puede recuperar."),
    ],
    open_task=task(
        "Observa sin probar: pon un hielo en un vaso con agua a temperatura ambiente y mira cómo cambia. Luego disuelve una cucharada de sal en medio vaso de agua y deja el vaso al sol varios días hasta que el agua se evapore. Haz una tabla con dos filas (hielo, sal en agua) y columnas: qué observo, ¿se forman sustancias nuevas?, ¿es reversible?, clasificación y una limitación de tu evidencia.",
        "Hielo: se derrite, sigue siendo agua, reversible, físico. Sal en agua: la sal desaparece y reaparece al evaporarse el agua, reversible, físico. Limitación: no medí la masa y no puedo asegurar que se recuperó toda la sal.",
        ["dos cambios observados", "criterio de sustancias nuevas", "limitación de la evidencia"],
        ["tabla con dos filas", "frase de limitación"],
        ["probar el agua con sal", "clasificar solo por reversibilidad"],
        "Pregunta qué cambio de la cocina clasificarías como químico y qué indicadores tendría.",
    ),
    reinforce="Clasifica cinco cambios de tu casa en físicos o químicos y explica uno con el criterio de sustancias nuevas.",
    extend="Averigua con una persona de tu casa qué cambia en una vela encendida y en una vela derretida, y pregunta cuál es físico y cuál químico, sin encender nada tú.",
)

# ================================================================ OA 15, clase 4
register(
    OA15, 4,
    materials="Papel y lápiz. Para la tarea abierta: una manzana, jugo de limón, agua, tres platos y un reloj. No pruebes las muestras.",
    use="Aprenderé a diseñar una prueba justa con un control para estudiar un cambio de la materia. Sirve para que los resultados sean confiables.",
    prior=["Sé registrar un cambio antes, durante y después.", "Sé cuáles son los indicadores de cambio químico."],
    explain=[
        "Una prueba justa cambia una sola cosa a la vez. La variable independiente es la que decides cambiar; la variable dependiente es la que mides para ver el efecto; las variables controladas son las que se mantienen iguales. El grupo de control es la muestra a la que no se le aplica el cambio, y sirve para comparar.",
        "Por ejemplo, para saber si el jugo de limón retrasa que una manzana cortada se ponga café, se usan tres trozos del mismo tamaño y de la misma manzana. El trozo A queda al aire (control), el B se cubre con jugo de limón y el C se cubre con agua. La variable independiente es el tratamiento, la dependiente es el color medido en una escala (0 blanco, 1 café claro, 2 café, 3 café oscuro) cada 15 minutos, y se controlan el tamaño, el lugar y la hora.",
        "Se escribe una hipótesis, es decir, una respuesta que se puede comprobar: «Si cubro un trozo con jugo de limón, entonces tardará más en ponerse café que el control». Si los datos no apoyan la hipótesis, se acepta el resultado y se corrige la idea; no se cambian los datos.",
    ],
    vocab=[("variable independiente", "lo que cambias a propósito"), ("variable dependiente", "lo que mides para ver el efecto"), ("variable controlada", "lo que se mantiene igual"), ("grupo de control", "muestra sin el cambio, usada para comparar"), ("hipótesis", "respuesta que se puede comprobar con datos")],
    worked=[
        {"title": "Identificar variables", "problem": "En la prueba de la manzana con jugo de limón, ¿cuál es la variable independiente?", "steps": ["Es lo que se decide cambiar entre trozos.", "Se cambia el tratamiento: aire, limón o agua."], "answer": "El tratamiento aplicado al trozo"},
        {"title": "Leer una tabla", "problem": "Colores a los 30 min (escala 0 a 3): A (control) 2, B (limón) 1, C (agua) 2. ¿Qué trozo tuvo menos cambio?", "steps": ["El valor menor es 1.", "Corresponde al trozo B."], "answer": "El trozo B con jugo de limón"},
    ],
    mistakes=[
        {"wrong": "Cambiar el tamaño del trozo y el tratamiento a la vez.", "why": "No se sabe qué causó la diferencia.", "fix": "Cambia una sola variable y deja iguales las demás."},
        {"wrong": "No usar un trozo de control.", "why": "No hay con qué comparar.", "fix": "Deja siempre una muestra sin el tratamiento."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama la muestra a la que no se le aplica el cambio y sirve para comparar?", "Grupo de control", "Es la referencia de la prueba."),
            ex("¿Cuántas variables independientes tiene una prueba justa?", "Una", "Solo se cambia una cosa a la vez."),
            ex("En la prueba de la manzana, ¿qué se mide cada 15 minutos?", "El color en la escala", "Es la variable dependiente."),
        ],
        "understand": [
            ex("¿Por qué los tres trozos de manzana deben ser del mismo tamaño?", "Para que el tamaño no sea otra causa de la diferencia", "Es una variable controlada."),
            ex("Hipótesis: «Si cubro un trozo con jugo de limón, entonces tardará más en ponerse café». ¿Se puede comprobar con datos? Responde sí o no.", "Sí", "Se puede medir el color en el tiempo."),
            ex("Los datos no apoyan una hipótesis. ¿Qué se corrige: la hipótesis o los datos?", "La hipótesis", "Los datos son la evidencia."),
        ],
        "apply": [
            ex("Tabla de ejemplo con la escala de 0 a 3 a los 45 minutos: A 3, B 1, C 3. Si el grupo de control es A, ¿qué trozo muestra un efecto distinto al control?", "El trozo B", "Es el único con un valor diferente al control."),
            arith("A los 60 minutos el trozo de control marca 3 en la escala de color y el trozo con limón marca 1. ¿Cuántos puntos de diferencia hay?", "3-1", "Se resta el valor menor al mayor.", " puntos"),
            arith("Una prueba mide el color cada 15 minutos durante 2 horas. ¿Cuántas mediciones se hacen, contando la de las 0 horas?", "120//15+1", "Se divide el tiempo total por el intervalo y se suma la medición inicial.", " mediciones"),
        ],
        "reason": [
            ex("Un grupo prueba tres tratamientos con trozos de manzana de distintas manzanas. ¿Qué variable no controló?", "El origen de la manzana", "Las manzanas pueden cambiar a distinto ritmo."),
            ex("Un compañero dice que el trozo con limón cambió menos «porque le tengo fe». ¿Qué le faltó?", "Datos medidos comparados con el control", "La conclusión debe basarse en evidencia."),
        ],
        "challenge": [
            ex("Diseña con palabras una prueba para saber si el frío retrasa que un trozo de banana se ponga café: nombra la variable independiente, la dependiente y una controlada.", "Independiente: la temperatura del lugar; dependiente: el color; controlada: el tamaño del trozo", "Cualquier variable controlada válida sirve."),
            ex("Una prueba tiene tres trozos, pero se dejaron en lugares distintos de la casa. ¿Qué variable se descontroló y cómo se corrige?", "El lugar o la temperatura; dejar todos en el mismo lugar", "Debe haber una sola variable independiente."),
        ],
    },
    context=[ex("Una persona quiere saber si guardar un pan en una bolsa cerrada evita que le salga moho. Propone comparar el pan en la bolsa con otro pan abierto de la misma marca y del mismo día. ¿Cuál de los dos es el grupo de control?", "El pan abierto", "Es el que no recibe el tratamiento.")],
    selfcheck=[
        ex("¿Qué se mantiene igual en una prueba justa?", "Las variables controladas", "Para que solo cambie la independiente."),
        ex("¿Para qué sirve el grupo de control?", "Para comparar", "Muestra qué pasa sin el tratamiento."),
        ex("¿Qué es una hipótesis?", "Una respuesta que se puede comprobar con datos", "Se acepta o se corrige según la evidencia."),
    ],
    open_task=task(
        "Diseña y, si puedes, ejecuta con ayuda de una persona adulta esta prueba: pide a una persona adulta que corte tres trozos iguales de manzana y ponlos en tres platos. Plato A: sin nada (control). Plato B: cubierto con jugo de limón. Plato C: cubierto con agua. Registra el color con la escala de 0 a 3 cada 15 minutos durante una hora, en una tabla. Escribe tu hipótesis, nombra la variable independiente, la dependiente y dos controladas, y concluye con una limitación.",
        "Hipótesis: el limón retrasa el cambio de color. Independiente: el tratamiento. Dependiente: el color. Controladas: tamaño y lugar. Datos de ejemplo a los 60 minutos: A 3, B 1, C 3. Conclusión: apoya la hipótesis. Limitación: un solo ensayo.",
        ["hipótesis comprobable", "variables nombradas", "tabla de datos y conclusión con limitación"],
        ["tabla de cinco filas de tiempo", "frase de conclusión"],
        ["no incluir un control", "cambiar el tamaño de los trozos"],
        "Pregunta qué harías para repetir la prueba y confirmar el resultado.",
    ),
    reinforce="Escribe una hipótesis y las variables para una prueba con otra fruta que cambia de color.",
    extend="Averigua con una persona de tu casa qué usa para evitar que una fruta cortada se oscurezca y compáralo con tu prueba.",
)

# ================================================================ OA 15, clase 5
register(
    OA15, 5,
    materials="Papel y lápiz. Todos los casos están escritos en el cuaderno.",
    use="Aprenderé a argumentar si un cambio es físico o químico usando evidencias y a decir qué límites tiene mi conclusión. Sirve para comunicar un resultado con honestidad.",
    prior=["Conozco los indicadores de cambio químico.", "Sé que el criterio principal es si se forman sustancias nuevas."],
    explain=[
        "Un argumento científico sobre un cambio tiene cuatro partes. La afirmación dice si el cambio es físico o químico. La evidencia reúne los datos y observaciones, como indicadores, masas y si se puede recuperar la sustancia. El razonamiento explica por qué esa evidencia lleva a la afirmación, usando el criterio de las sustancias nuevas. La limitación dice qué no se pudo comprobar.",
        "Por ejemplo: «El pan tostado sufrió un cambio químico (afirmación). Cambió de color de forma permanente, se formó un olor nuevo y no se puede recuperar el pan blanco (evidencia). Estos indicadores muestran que se formaron sustancias nuevas (razonamiento). No analizamos las sustancias con instrumentos, así que no sabemos cuáles son (limitación)».",
        "Antes de concluir, revisa: ¿hay varios indicadores o solo uno? ¿se hizo una prueba con control? ¿hay una explicación física alternativa? Una buena conclusión puede ser «probablemente químico», si la evidencia es fuerte pero incompleta.",
    ],
    vocab=[("afirmación", "respuesta que se quiere demostrar"), ("razonamiento", "explicación que une la evidencia con la afirmación"), ("limitación", "aspecto que no se pudo comprobar"), ("explicación alternativa", "otra posible causa del mismo resultado"), ("evidencia empírica", "datos obtenidos por observación o medición")],
    worked=[
        {"title": "Armar un argumento", "problem": "Caso de ejemplo: un huevo cocido cambia de textura y de color y no vuelve a ser crudo al enfriarse. ¿Qué afirmación y qué evidencias das?", "steps": ["Afirmación: es un cambio químico.", "Evidencias: cambio permanente de textura y color, no se recupera el huevo crudo."], "answer": "Cambio químico, apoyado en dos evidencias"},
        {"title": "Detectar una limitación", "problem": "Un grupo concluye que cierto cambio es químico por solo un cambio de color. ¿Cuál es la limitación?", "steps": ["Un solo indicador puede darse también en un cambio físico.", "Falta otra evidencia."], "answer": "Hay un único indicador y no se descartó una explicación física"},
    ],
    mistakes=[
        {"wrong": "Escribir una conclusión sin ninguna limitación.", "why": "Se presenta la evidencia como completa.", "fix": "Dile al lector qué no pudiste comprobar."},
        {"wrong": "Usar «porque sí» como razonamiento.", "why": "No se une la evidencia con el criterio.", "fix": "Explica que la evidencia muestra sustancias nuevas o no."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué parte de un argumento son los datos y observaciones?", "La evidencia", "Es lo que se observó o midió."),
            ex("¿Qué parte de un argumento dice qué no se pudo comprobar?", "La limitación", "Es la honestidad sobre los límites."),
            ex("El pan tostado cambió de color y de olor y no vuelve a ser pan blanco. ¿Es físico o químico?", "Químico", "Hay varios indicadores de sustancias nuevas."),
        ],
        "understand": [
            ex("¿Por qué es mejor usar varios indicadores que uno solo?", "Porque un indicador puede darse en un cambio físico", "Varias evidencias dan más seguridad."),
            ex("¿Qué es una explicación alternativa?", "Otra posible causa del mismo resultado", "Hay que revisar si también explica los datos."),
            ex("Una conclusión dice «probablemente químico». ¿Qué indica sobre la evidencia?", "Que es fuerte pero incompleta", "Se reconoce un grado de incertidumbre."),
        ],
        "apply": [
            ex("Caso 1: se disuelve azúcar en agua, desaparece y al evaporar el agua reaparece el azúcar. Escribe la afirmación y una evidencia.", "Cambio físico; el azúcar reaparece al evaporar el agua", "Se recuperó la misma sustancia."),
            ex("Caso 2: un clavo húmedo forma una capa café-rojiza que no se puede volver a hacer clavo con un método simple. Escribe la afirmación y una evidencia.", "Cambio químico; apareció una sustancia nueva de otro color", "El óxido es una sustancia nueva."),
            ex("Caso 3: un trozo de mantequilla se derrite en una sartén tibia y, al enfriarse, vuelve a ser sólido. Escribe la afirmación y una evidencia.", "Cambio físico; vuelve a ser sólido sin cambiar de sustancia", "Se recuperó la misma sustancia al enfriar."),
        ],
        "reason": [
            ex("Una compañera afirma «es químico» y su única evidencia es que algo cambió de color. ¿Qué parte del argumento es débil?", "La evidencia, porque hay un solo indicador", "Un cambio de color puede ser físico."),
            ex("Otro grupo concluye «es físico» sin haber comprobado si se podía recuperar la sustancia original. ¿Qué limitación debería declarar?", "No se comprobó si se recupera la sustancia original", "Falta una prueba clave."),
        ],
        "challenge": [
            ex("Caso: se mezclan dos líquidos transparentes y aparece un sólido blanco en el fondo. Un grupo dice «cambio químico seguro». ¿Qué prueba adicional pedirías para estar más seguro?", "Comprobar que el sólido no estaba disuelto antes y que tiene propiedades distintas", "Una sustancia nueva tiene propiedades distintas de las originales."),
            ex("Escribe una limitación para un argumento sobre un huevo cocido en el que no se midió la masa antes y después.", "No sabemos si la masa se conservó", "Es un dato que faltó."),
        ],
    },
    context=[ex("Una persona de tu casa dice: «El charco desapareció porque el agua se transformó en otra sustancia». Con el criterio de las sustancias nuevas, ¿qué evidencia la contradice?", "El agua pasó a vapor de agua, que sigue siendo agua y puede condensarse", "Un cambio de estado no forma una sustancia nueva.")],
    selfcheck=[
        ex("¿Cuáles son las cuatro partes de un argumento científico?", "Afirmación, evidencia, razonamiento y limitación", "Son las partes de la clase."),
        ex("¿Qué debe tener una buena conclusión además de la afirmación?", "Evidencia y limitación", "Así se puede revisar."),
        ex("¿Puede una conclusión decir «probablemente químico»?", "Sí", "Cuando la evidencia es fuerte pero incompleta."),
    ],
    open_task=task(
        "Elige uno de estos tres casos de ejemplo y escribe un argumento de cuatro partes. Caso A: una galleta se rompe en pedazos. Caso B: una manzana cortada se pone café en una hora. Caso C: una taza de leche se agria después de varios días fuera del refrigerador. Usa la afirmación, la evidencia (con al menos dos datos), el razonamiento con el criterio de sustancias nuevas y una limitación. Después escribe qué prueba adicional harías para mejorar tu conclusión. No pruebes ni huelas de cerca ningún alimento echado a perder.",
        "Caso C: afirmación, cambio químico. Evidencia: cambia el olor (que se percibe sin acercarse), cambia la textura y no vuelve a ser leche fresca. Razonamiento: esos cambios indican sustancias nuevas. Limitación: no se analizó la leche con instrumentos. Prueba adicional: comparar con un envase guardado en el refrigerador.",
        ["caso elegido y clasificado", "al menos dos evidencias", "razonamiento y limitación", "prueba adicional"],
        ["argumento de cuatro partes", "frase de prueba adicional"],
        ["omitir la limitación", "clasificar solo por un indicador"],
        "Pregunta qué explicación alternativa descartaste.",
    ),
    reinforce="Elige otro caso de la tarea y escribe su argumento en una frase por parte.",
    extend="Averigua con una persona de tu casa cómo reconoce un alimento echado a perder y escribe esos indicadores como evidencia.",
)
