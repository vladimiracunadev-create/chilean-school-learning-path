"""Gastronomía TP 3.º medio (tronco): OAE-04 (ordenar, organizar y disponer productos intermedios, insumos, equipos y utensilios según sus características organolépticas, el proceso y la normativa de higiene e inocuidad; monitoreo de calidad, armado y presentación de productos y disposición de comedores). Todo en papel, solo conceptos, registros y cálculos con datos «de ejemplo»."""
from __future__ import annotations

from tp_gast_common import build

O4 = "TP-GAST-3-OAE-04"
LIM = " Este cuaderno trabaja en papel, con datos de ejemplo: la práctica en cocina requiere instructor/docente de la especialidad y norma vigente (autoridad sanitaria); no te habilita para trabajar."

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (productos intermedios de una cocina de ejemplo, inventada). Productos intermedios: caldo base, aliño, verduras troceadas y salsa base; la producción los usa para armar platos. "
     "Vida útil de ejemplo en refrigeración (valores inventados que no reemplazan la norma vigente): caldo base 3 días; aliño 2 días; verduras troceadas 1 día; salsa base 3 días. "
     "Características organolépticas: lo que se percibe con los sentidos, es decir, aspecto, color, olor, sabor y textura. La autoridad sanitaria fiscaliza la higiene y la inocuidad.")
build(
    O4, 1, F,
    use="Aprenderé a situar el trabajo con productos intermedios: qué son, qué son las características organolépticas, por qué tienen una vida útil y quién fiscaliza la inocuidad.",
    prior=["Conozco el flujo de materias primas y el rótulo.", "Sé dividir cantidades.", "Distingo limpiar y desinfectar."],
    explain=[
        "En Gastronomía, un producto intermedio es una preparación que se elabora antes y se usa después para armar otros platos, como un caldo base o una salsa base. No es la materia prima que llega de afuera ni el plato terminado que se sirve. Ordenar los productos intermedios significa guardarlos identificados, en el lugar correcto y listos para usarse a tiempo.",
        "Las características organolépticas son las que se perciben con los sentidos: aspecto, color, olor, sabor y textura. Sirven para evaluar la calidad, pero no bastan para saber si un producto es seguro: un producto puede verse y oler normal y no ser inocuo. La inocuidad es que el alimento no hace daño a quien lo consume. Por eso se respeta también la vida útil, el plazo durante el cual se puede usar.",
        "Los productos intermedios se rotulan, se guardan tapados y se usan antes de que venza su plazo. La autoridad sanitaria fiscaliza la higiene y la inocuidad según la norma vigente. Los plazos de esta ficha son de ejemplo." + LIM,
    ],
    vocab=[("producto intermedio", "preparación que se elabora antes y se usa para armar otros platos"), ("características organolépticas", "aspecto, color, olor, sabor y textura, percibidos con los sentidos"), ("inocuidad", "que el alimento no hace daño a quien lo consume"), ("vida útil", "plazo durante el cual un producto se puede usar"), ("perecible", "que se echa a perder con facilidad")],
    worked=[
        ("Clasificar un producto", "En una cocina de ejemplo se prepara una masa base para usar en varios platos. ¿Es materia prima, producto intermedio o plato terminado?", ["Se elabora antes y se usa para armar otros platos.", "No llega de afuera ni se sirve tal cual."], "Producto intermedio"),
        ("Distinguir una característica", "Un cocinero dice que una salsa de ejemplo tiene un olor agradable. ¿Qué tipo de característica describe?", ["El olor se percibe con un sentido.", "Es una característica organoléptica."], "Una característica organoléptica"),
    ],
    mistakes=[("Pensar que un producto es seguro si se ve y huele bien.", "Algunos microbios no cambian el aspecto ni el olor, por eso la vida útil también debe respetarse.", "Usa el producto solo dentro de su plazo, además de revisar sus características."),
              ("Dejar un producto intermedio sin tapar y sin rótulo.", "Se contamina con mayor facilidad y nadie sabe qué es ni hasta cuándo se puede usar.", "Guárdalo tapado y rotulado con su fecha de elaboración y plazo.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es un producto intermedio?", "Una preparación que se elabora antes y se usa para armar otros platos", "El plato terminado que se sirve a un cliente", "La materia prima recién recibida", "El intermedio queda entre la materia prima y el plato final."),
        ("abc", "{F} ¿Cuál de estos es un producto intermedio según la ficha?", "La salsa base", "La papa recién llegada del proveedor", "El plato servido en la mesa", "La salsa base se elabora antes y se usa para armar platos."),
        ("abc", "{F} ¿Qué son las características organolépticas?", "Lo que se percibe con los sentidos: aspecto, color, olor, sabor y textura", "Los plazos de uso de un producto", "Los datos del proveedor", "La ficha las define como lo que se percibe con los sentidos."),
        ("=", "{F} Si el caldo base debe elaborarse cada vez que vence su vida útil, ¿cuántas veces se elabora en 12 días?", "12//3", "Se dividen los días del período por los días de vida útil.", " veces"),
        ("abc", "{F} El aliño lleva 3 días en el refrigerador y se ve y huele normal. ¿Qué corresponde?", "No usarlo, descartarlo según el procedimiento de la cocina y registrarlo", "Usarlo, porque se ve y huele normal", "Mezclarlo con aliño nuevo para disimular", "Superó su vida útil de 2 días; aspecto y olor no garantizan que sea seguro."),
        ("abc", "En Gastronomía: ¿qué significa que un alimento sea inocuo?", "Que no hace daño a quien lo consume", "Que tiene un sabor agradable", "Que tiene un color uniforme", "La inocuidad se refiere a la seguridad del alimento, no a su sabor ni su aspecto."),
        ("abc", "{F} Una cocinera encuentra un recipiente con salsa base sin tapa ni rótulo. ¿Qué corresponde?", "No usarlo y consultar a la jefatura, porque no se sabe cuándo se elaboró", "Usarlo si no tiene mal olor", "Taparlo y seguir usándolo", "Sin rótulo no se puede verificar la vida útil, y sin tapa pudo contaminarse."),
        ("=", "{F} Una cocina elabora verduras troceadas cada día de su vida útil durante 6 días de trabajo. ¿Cuántas veces las elabora?", "6//1", "Se dividen los días de trabajo por los días de vida útil.", " veces"),
        ("abc", "Un compañero dice: «Si el producto huele normal después de su plazo, igual es seguro». ¿Qué respuesta es correcta?", "Un producto puede oler normal y no ser seguro; se respeta el plazo", "Tiene razón, porque el olor basta", "Solo importa el sabor", "Los microbios pueden estar presentes sin cambiar el aspecto o el olor."),
        ("=", "Un lote de 12 litros de salsa base se usa a razón de 4 litros por día. ¿Para cuántos días alcanza el lote?", "12//4", "Se divide el volumen del lote por el consumo diario.", " días"),
        ("abc", "{F} Una cocinera dice que no hace falta rotular el caldo base porque «ella se acuerda de cuándo lo hizo». ¿Qué observación corresponde?", "El rótulo informa a todo el equipo; la memoria de una persona no es un registro", "Tiene razón, si trabaja sola", "El rótulo solo sirve para el proveedor", "Otras personas deben saber qué es y cuándo vence, aunque ella lo recuerde."),
        ("=", "{F} En una semana de 6 días de trabajo, cada producto se elabora justo cuando vence su vida útil. ¿Cuántas elaboraciones hay en total de caldo base, aliño y verduras troceadas?", "6//3+6//2+6//1", "Se suman las elaboraciones de cada producto: días de trabajo dividido por su vida útil.", " elaboraciones"),
        ("abc", "{F} ¿Quién fiscaliza la higiene y la inocuidad de los productos de la cocina?", "La autoridad sanitaria", "Cada cocinero según su criterio", "El proveedor de materias primas", "La ficha asigna esa fiscalización a la autoridad sanitaria."),
    ],
    ctx=("abc", "{F} Un martes, la jefa encuentra un recipiente de caldo base con un rótulo que indica que fue elaborado hace 5 días. ¿Qué corresponde?", "No usarlo y descartarlo según el procedimiento de la cocina, porque superó su vida útil", "Usarlo en los platos de hoy, porque se ve bien", "Usarlo solo en el menú del personal", "Con 5 días ya superó el plazo de 3 días, sin importar su apariencia."),
    sc=[
        ("En Gastronomía: ¿qué son las características organolépticas?", "Aspecto, color, olor, sabor y textura", "Se perciben con los sentidos y sirven para evaluar calidad."),
        ("¿Basta con que un producto huela bien para ser inocuo?", "No, también se respeta el plazo", "El olor normal no garantiza la seguridad."),
        ("¿Qué lleva un producto intermedio guardado?", "Tapa y rótulo con fecha y plazo", "Así se protege y se sabe hasta cuándo se puede usar."),
    ],
    op=("Una cocina de ejemplo elabora tres productos intermedios: una masa base con vida útil de ejemplo de 4 días, una crema base de 2 días y un fondo de 3 días. "
        "Escribe: (a) qué es un producto intermedio con tus palabras, (b) cuántas veces se elabora cada producto en 12 días si se hace justo al vencer, (c) las cinco características organolépticas y una regla de por qué no bastan para saber si es seguro.",
        "(a) Preparación que se hace antes para armar otros platos. (b) Masa base: 12 ÷ 4 = 3 veces. Crema base: 12 ÷ 2 = 6 veces. Fondo: 12 ÷ 3 = 4 veces. (c) Aspecto, color, olor, sabor y textura; no bastan porque un producto puede verse y oler normal y no ser inocuo, por eso se respeta también el plazo.",
        ["define producto intermedio", "calcula 3, 6 y 4 elaboraciones", "nombra las cinco características y explica por qué no bastan"],
        ["hoja con definición, cálculos y respuesta"],
        ["decir que el olor garantiza la seguridad", "dividir al revés", "olvidar una característica"],
        "Pregunta: «¿qué pasa si usas la crema el tercer día?». Debe responder que superó su plazo."),
    reinforce="Haz una lista de tres productos intermedios inventados con su vida útil de ejemplo y calcula cuántas veces se elaboran en 12 días.",
    extend="Explica por qué la vida útil y las características organolépticas se usan juntas para decidir si un producto puede usarse.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (rótulo y refrigerador de ejemplo, inventados). Rótulo de la «Salsa base de ejemplo»: fecha de elaboración, día 5; usar antes del día 8; elaborada por las iniciales A. P.; contiene leche y huevo (alérgenos). "
     "Un alérgeno es una sustancia de un alimento que puede causar una reacción en algunas personas. "
     "Reglas del refrigerador de la cocina (de ejemplo): estante superior, productos listos para comer y tapados; estante medio, productos cocidos; estante inferior, productos crudos. Todo producto lleva rótulo y se usa primero lo que vence antes.")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario y los documentos para ordenar productos intermedios: rótulo, alérgenos, orden del refrigerador, reglas FEFO y roles.",
    prior=["Conozco productos intermedios y vida útil.", "Conozco el rótulo y FEFO.", "Sé restar y sumar."],
    explain=[
        "El rótulo de un producto intermedio lleva el nombre, la fecha de elaboración, el plazo máximo de uso, quién lo elaboró y los alérgenos que contiene. Un alérgeno es una sustancia que en algunas personas causa una reacción; entre los más comunes en alimentos están la leche, el huevo, el gluten de algunos cereales, el maní, los frutos secos, el pescado y los mariscos. Rotular los alérgenos permite informar con seguridad.",
        "El refrigerador se ordena por riesgo: los productos listos para comer, arriba y tapados; los cocidos, al medio; y los crudos, abajo, para que sus líquidos no goteen sobre otros alimentos. Se usa primero lo que vence antes (FEFO). Mantener el frío sin interrupción protege la inocuidad. Se evita abrir la puerta por mucho tiempo.",
        "Cada persona cumple un rol: la cocinera rotula lo que elabora, el ayudante ordena según las reglas y la jefa de cocina revisa. Ante una reacción alérgica de una persona, no se improvisan remedios: se avisa de inmediato a un adulto responsable y a los servicios de emergencia." + LIM,
    ],
    vocab=[("alérgeno", "sustancia de un alimento que puede causar reacción en algunas personas"), ("rótulo de alérgenos", "indicación de los alérgenos que contiene un producto"), ("contaminación cruzada", "paso de microbios o alérgenos de un alimento a otro"), ("listo para comer", "alimento que se consume sin más preparación"), ("FEFO", "primero que vence, primero en salir")],
    worked=[
        ("Leer un plazo", "Un rótulo de ejemplo indica elaborado el día 10 y usar antes del día 14. ¿Cuántos días de plazo tiene?", ["Se resta la fecha de elaboración al plazo.", "14 − 10 = 4."], "4 días"),
        ("Ubicar un producto", "Según las reglas de un refrigerador de ejemplo (listos arriba, cocidos al medio, crudos abajo), ¿dónde va una bandeja de pescado crudo?", ["Los crudos van abajo.", "Así sus líquidos no caen sobre otros alimentos."], "En el estante inferior"),
    ],
    mistakes=[("Poner carne cruda en el estante superior sobre alimentos listos para comer.", "Sus líquidos pueden gotear y contaminar alimentos que no se cocinarán de nuevo.", "Guarda los crudos abajo y tapados, separados de los listos para comer."),
              ("Omitir los alérgenos en el rótulo porque «todos saben qué lleva».", "Una persona alérgica puede consumir el producto sin saberlo.", "Anota los alérgenos que contiene cada preparación.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es un alérgeno?", "Una sustancia de un alimento que puede causar una reacción en algunas personas", "Un microorganismo que echa a perder los alimentos", "Un aditivo que se agrega para conservar", "El alérgeno es una sustancia que algunas personas no toleran; no se trata de un microbio."),
        ("abc", "{F} ¿Hasta qué día puede usarse la salsa base según el rótulo?", "Hasta antes del día 8", "Hasta el día 5", "Hasta el día 12", "El rótulo indica usar antes del día 8."),
        ("=", "{F} ¿Cuántos días de plazo tiene la salsa base desde su elaboración?", "8-5", "Al día límite se le resta el día de elaboración.", " días"),
        ("abc", "{F} ¿Qué alérgenos declara el rótulo de la salsa base?", "Leche y huevo", "Maní y pescado", "Gluten y soya", "El rótulo de la ficha declara solo leche y huevo."),
        ("abc", "{F} ¿En qué estante se guardan los productos crudos?", "En el inferior", "En el superior", "En el medio", "La regla del refrigerador ubica los crudos abajo."),
        ("abc", "{F} ¿Por qué los productos crudos van en el estante inferior?", "Para que sus líquidos no goteen sobre alimentos listos para comer", "Para que se enfríen más rápido que los demás", "Para que ocupen menos espacio", "La razón es evitar la contaminación cruzada por goteo."),
        ("=", "{F} Una nueva salsa base se elabora el día 12, con el mismo plazo del rótulo. ¿Hasta qué día se puede usar?", "12+(8-5)", "Al día de elaboración se le suma el plazo en días.", ""),
        ("abc", "{F} Un cliente pregunta si la salsa base lleva huevo. ¿Qué corresponde responder?", "Informar según el rótulo o la ficha de ingredientes, y consultar a la jefatura si hay dudas", "Decir que no, para evitar problemas", "Decir que no lo recuerdas", "La respuesta se basa en información verificada, nunca en suposiciones."),
        ("abc", "{F} Un cocinero deja una bandeja de pollo crudo tapada en el estante superior. ¿Qué observación corresponde?", "Debe ir en el estante inferior, junto a los otros productos crudos", "Está bien, porque está tapada", "Debe ir en el estante medio", "Los crudos van abajo aunque estén tapados, para evitar que sus líquidos caigan sobre otros alimentos."),
        ("=", "{F} Hay 6 bandejas en el estante superior, 4 en el medio y 5 en el inferior. Cada bandeja contiene 8 porciones. ¿Cuántas porciones hay en total?", "(6+4+5)*8", "Se suman las bandejas de los tres estantes y se multiplican por las porciones.", " porciones"),
        ("abc", "Un compañero dice que no hace falta rotular porque «todos saben qué es cada cosa». ¿Qué respuesta es correcta?", "El rótulo evita confusiones y permite controlar plazos y alérgenos, aunque todos recuerden", "Tiene razón, si el equipo es pequeño", "El rótulo solo se usa para productos crudos", "La memoria de las personas no reemplaza un registro verificable por todo el equipo."),
        ("abc", "Una persona del comedor presenta dificultad para respirar después de comer y se sospecha una reacción alérgica. ¿Qué corresponde?", "Avisar de inmediato a un adulto responsable y a los servicios de emergencia", "Darle un remedio casero", "Esperar a ver si mejora", "La atención es de personal de emergencia; no se improvisan remedios."),
        ("abc", "{F} Hay dos bandejas de ensalada lista, una con plazo hasta el día 9 y otra hasta el día 11. ¿Cuál se usa primero?", "La del plazo hasta el día 9", "La del plazo hasta el día 11", "Da lo mismo cuál se use", "FEFO indica usar primero lo que vence antes."),
    ],
    ctx=("abc", "{F} Una ayudante nueva guarda bandejas sin pensar: pone una de carne cruda arriba y una de ensalada lista abajo, «para que quepa mejor». ¿Qué debe hacer la jefa?", "Explicar la regla del orden por riesgo y pedir que reordene las bandejas", "Dejarlo así, porque lo importante es que quepan", "Pedirle que no vuelva a usar el refrigerador", "La corrección debe educar y restablecer la regla que evita la contaminación cruzada."),
    sc=[
        ("En Gastronomía: ¿qué datos lleva el rótulo de un producto intermedio?", "Nombre, fecha, plazo, quién lo elaboró y alérgenos", "Permite identificar y controlar el producto."),
        ("¿Dónde se guardan los crudos?", "En el estante inferior, tapados", "Así no gotean sobre otros alimentos."),
        ("¿Qué se hace ante una reacción alérgica?", "Avisar a un adulto responsable y a emergencias", "No se improvisan remedios: interviene personal capacitado."),
    ],
    op=("Refrigerador de ejemplo con tres estantes (arriba: listos para comer; medio: cocidos; abajo: crudos). Productos: pescado crudo, postre listo para comer, arroz cocido y huevos crudos. "
        "Escribe en qué estante va cada producto, el rótulo de una «crema base de ejemplo» elaborada el día 3 con plazo hasta el día 6 que contiene leche (nombre, fecha, plazo, alérgeno), y una frase que le dirías a un compañero que se olvidó de rotular.",
        "Pescado crudo: abajo. Postre: arriba. Arroz cocido: medio. Huevos crudos: abajo. Rótulo: «Crema base de ejemplo; elaborada el día 3; usar antes del día 6; contiene leche». Frase: «Recuerda rotular: sin rótulo no sabemos cuándo vence ni qué alérgenos tiene».",
        ["ubica los cuatro productos por riesgo", "completa el rótulo con nombre, fecha, plazo y alérgeno", "da una frase respetuosa sobre rotular"],
        ["hoja con ubicaciones, rótulo y frase"],
        ["poner el pescado en el estante superior", "olvidar los alérgenos en el rótulo", "criticar a la persona en público"],
        "Pregunta: «¿qué pasaría si los huevos crudos estuvieran sobre el postre?». Debe mencionar contaminación cruzada."),
    reinforce="Dibuja un refrigerador de tres estantes y ubica seis productos inventados según las reglas de riesgo.",
    extend="Explica por qué el orden del refrigerador y el rótulo funcionan juntos para proteger a los clientes con alergias.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (inspección del refrigerador, día 10, de ejemplo). Estante superior: ensalada lista con rótulo (usar antes del día 11); bandeja de pollo crudo sin tapa. Estante medio: arroz cocido con rótulo (elaborado el día 8, usar antes del día 11); caldo base sin rótulo. "
     "Estante inferior: carne cruda tapada y rotulada (usar antes del día 12); huevos. Reglas (de ejemplo): listos para comer arriba y tapados; cocidos al medio; crudos abajo y tapados; todo con rótulo; se usa primero lo que vence antes.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un refrigerador en papel: detectar hallazgos, decidir acciones correctivas y definir el orden de uso de los productos.",
    prior=["Conozco el rótulo y el orden por riesgo.", "Conozco FEFO.", "Sé comparar días."],
    explain=[
        "Un caso de ordenamiento se analiza comparando lo observado con las reglas. Primero se lista lo que hay en cada estante, luego se revisa si cada producto cumple tres cosas: está en el estante correcto, está tapado y tiene rótulo con plazo. Cada incumplimiento es un hallazgo.",
        "Después se decide una acción por hallazgo: reubicar un producto, taparlo, rotularlo si se conoce con certeza su origen o descartarlo si no se puede verificar. También se define el orden de uso con FEFO. Los hallazgos con riesgo de contaminación cruzada se corrigen primero.",
        "Un producto sin rótulo ni plazo conocido no se usa, porque no se puede asegurar su inocuidad. Todo se anota en el registro de la inspección con el día y el responsable." + LIM,
    ],
    vocab=[("inspección", "revisión de un lugar o producto comparando con reglas"), ("hallazgo", "situación observada que no cumple una regla"), ("acción correctiva", "medida para eliminar la causa de un hallazgo"), ("reubicar", "cambiar un producto al lugar correcto")],
    worked=[
        ("Detectar un hallazgo", "En un refrigerador de ejemplo hay carne cruda en el estante superior. ¿Es un hallazgo?", ["La regla ubica los crudos abajo.", "La carne está en un lugar incorrecto."], "Sí: debe reubicarse al estante inferior"),
        ("Aplicar FEFO", "Dos productos tienen plazos hasta el día 9 y hasta el día 12. ¿Cuál se usa primero?", ["FEFO usa primero lo que vence antes.", "El día 9 es anterior al 12."], "El del día 9"),
    ],
    mistakes=[("Corregir solo el producto más a la vista y no revisar el resto.", "Otros hallazgos más riesgosos pueden quedar sin corregir.", "Revisa todos los estantes con la misma lista de reglas."),
              ("Poner un rótulo nuevo a un producto desconocido con la fecha de hoy.", "Se inventa un plazo que no corresponde y se oculta el origen real.", "Si no se conoce su origen, no se usa y se descarta según el procedimiento.")],
    T=[
        ("abc", "{F} ¿Cuál es el hallazgo que implica mayor riesgo de contaminación cruzada?", "Pollo crudo sin tapa en el estante superior, sobre alimentos listos para comer", "Arroz cocido con rótulo en el estante medio", "Carne cruda tapada y rotulada en el estante inferior", "El pollo crudo destapado arriba puede gotear sobre alimentos que no se cocinarán."),
        ("abc", "{F} ¿Qué hallazgo tiene el caldo base?", "No tiene rótulo", "Está en el estante superior", "Está vencido hace 3 días", "La ficha dice que el caldo base no tiene rótulo."),
        ("abc", "{F} ¿Qué corresponde hacer con el caldo base?", "No usarlo, porque se desconoce su plazo, y descartarlo según el procedimiento", "Ponerle un rótulo con la fecha de hoy", "Usarlo primero", "Sin saber cuándo se elaboró no se puede asegurar su inocuidad."),
        ("abc", "{F} ¿Qué corresponde hacer con el pollo crudo?", "Taparlo y reubicarlo en el estante inferior", "Taparlo y dejarlo arriba", "Dejarlo destapado en el estante medio", "Los crudos van abajo y tapados."),
        ("=", "{F} El arroz cocido fue elaborado el día 8 y puede usarse antes del día 11. ¿Cuántos días de plazo tiene?", "11-8", "Al día límite se le resta el día de elaboración.", " días"),
        ("abc", "{F} Hoy es día 10. ¿Qué productos con rótulo vencen antes, la ensalada o la carne cruda?", "La ensalada, que vence antes del día 11", "La carne cruda, que vence antes del día 12", "Vencen el mismo día", "La ensalada tiene plazo hasta el día 11 y la carne hasta el 12."),
        ("abc", "{F} Según FEFO, ¿cuál de los tres productos rotulados (ensalada, arroz cocido y carne cruda) se usa después de los otros dos?", "La carne cruda, que vence antes del día 12", "La ensalada, que vence antes del día 11", "El arroz cocido, que vence antes del día 11", "La carne tiene el plazo más largo, por lo que se usa después de los que vencen antes."),
        ("=", "En una semana de ejemplo se hizo 1 inspección por día durante 6 días y en cada una se detectaron 3 hallazgos. Si cada hallazgo se corrige en 15 minutos de ejemplo, ¿cuántos minutos de corrección hubo en la semana?", "6*3*15", "Se multiplican los días, los hallazgos de cada día y los minutos por hallazgo.", " minutos"),
        ("=", "En una inspección de ejemplo se revisaron 20 productos y 15 cumplieron todas las reglas. ¿Qué porcentaje cumplió?", "15*100//20", "Se multiplican los productos que cumplen por 100 y se dividen por el total revisado.", " %"),
        ("abc", "{F} Un ayudante propone solo reordenar los estantes sin rotular el caldo base. ¿Qué observación corresponde?", "Reordenar no resuelve el producto sin rótulo, que además debe descartarse", "Está bien, porque lo importante es el orden", "Es suficiente, si lo recuerda quien lo hizo", "El producto sin rótulo es un hallazgo independiente del orden."),
        ("abc", "{F} ¿Cuál es el orden más lógico para corregir los hallazgos?", "Primero el pollo crudo destapado y el caldo sin rótulo, que implican riesgo; luego el orden de uso", "Primero el orden de uso por FEFO y después los riesgos", "Primero lo que sea más fácil de corregir", "Los hallazgos con riesgo de contaminación e inocuidad se corrigen primero."),
        ("=", "{F} La bandeja de carne cruda del estante inferior tiene 24 porciones y se usan 6 porciones por servicio. ¿Para cuántos servicios alcanza?", "24//6", "Se divide el total de porciones por las que se usan en cada servicio.", " servicios"),
        ("abc", "{F} Si el pollo crudo hubiera goteado sobre la ensalada lista, ¿qué corresponde hacer con la ensalada?", "Descartarla y registrar lo ocurrido, porque pudo contaminarse", "Servirla igual, porque se puede cocinar de nuevo", "Lavarla con agua y usarla", "Un alimento listo para comer que pudo contaminarse con crudos no debe usarse."),
    ],
    ctx=("abc", "{F} Un supervisor llega antes de un servicio y ve los hallazgos de la ficha. La jefa dice: «No hay tiempo, lo arreglamos mañana». ¿Qué respuesta es adecuada?", "Corregir ahora lo que implica riesgo, como el pollo destapado y el caldo sin rótulo, y planificar el resto", "Esperar hasta mañana, porque hoy hay servicio", "Corregir solo el orden estético", "Los riesgos de inocuidad no se postergan; el resto se planifica."),
    sc=[
        ("En Gastronomía: ¿qué es un hallazgo?", "Una situación observada que no cumple una regla", "Es lo que se detecta al comparar con las reglas."),
        ("¿Qué se hace con un producto sin rótulo ni origen conocido?", "No se usa y se descarta según el procedimiento", "No se puede asegurar su inocuidad."),
        ("¿Qué hallazgos se corrigen primero?", "Los que implican riesgo de contaminación", "Pueden afectar la salud de las personas."),
    ],
    op=("Refrigerador de ejemplo, día 6. Estante superior: postre listo para comer, tapado y rotulado (usar antes del día 8). Estante medio: pescado crudo sin tapa; salsa cocida con rótulo (usar antes del día 7). Estante inferior: un recipiente tapado sin rótulo. "
        "Escribe: los hallazgos que encuentras, la acción correctiva para cada uno y el orden de uso de los productos con rótulo según FEFO.",
        "Hallazgos: pescado crudo destapado en el estante medio (debe ir abajo y tapado); recipiente sin rótulo (se descarta según el procedimiento porque no se conoce su plazo). Acciones: reubicar y tapar el pescado; descartar el recipiente y registrar. Orden de uso: primero la salsa cocida (vence antes del día 7), luego el postre (antes del día 8).",
        ["detecta los dos hallazgos", "propone una acción correctiva para cada uno", "ordena el uso con FEFO"],
        ["hoja con hallazgos, acciones y orden de uso"],
        ["dejar el pescado crudo en el estante medio", "rotular el recipiente con una fecha inventada", "usar primero el postre"],
        "Pregunta: «¿por qué no puedes ponerle un rótulo nuevo al recipiente?». Debe responder que se inventaría un plazo."),
    reinforce="Inventa un refrigerador con ocho productos y tres hallazgos, y escribe la acción correctiva de cada uno.",
    extend="Explica por qué se corrigen primero los hallazgos de riesgo aunque el servicio esté por comenzar.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (servicio de almuerzo de ejemplo, inventado). Comedor con 9 mesas de 6 puestos cada una. Cada puesto lleva 1 plato, 1 vaso, 1 tenedor, 1 cuchillo y 1 servilleta. "
     "Tipo de servicio: autoservicio (cada persona retira su bandeja en una línea de servicio). Estándares de presentación (de ejemplo): porción estandarizada de 150 g; borde del plato limpio; lo frío se sirve frío y lo caliente se sirve caliente; área de servicio limpia y ordenada. "
     "Protocolo (reglas de atención): saludar, entregar la bandeja y desear buen provecho.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar criterios para disponer un comedor y presentar los productos: puestos, implementos, tipo de servicio, porciones y reglas de higiene y estética.",
    prior=["Conozco productos intermedios y su ordenamiento.", "Sé multiplicar y dividir.", "Conozco la porción y el rendimiento."],
    explain=[
        "Disponer un comedor es ordenar las mesas, los puestos y los implementos (platos, vasos, cubiertos, servilletas) antes del servicio, según las características del evento. El tipo de servicio define cómo se atiende: en el servicio a la mesa el personal lleva los platos a cada mesa; en el autoservicio cada persona retira su bandeja en una línea; en el buffet los alimentos están en fuentes sobre una mesa común y cada persona se sirve.",
        "Presentar un producto es entregarlo según el estándar: porción estandarizada (la misma cantidad para todos), borde del plato limpio, lo frío servido frío y lo caliente servido caliente. Los principios estéticos básicos son el orden, la uniformidad y la limpieza: todos los puestos con los mismos implementos en la misma posición.",
        "Por higiene, los implementos deben estar limpios y completos, y se toman por el mango o por la parte que no toca los alimentos, con las manos limpias. El protocolo es el conjunto de reglas de atención, como saludar y desear buen provecho." + LIM,
    ],
    vocab=[("puesto", "lugar de una persona en la mesa, con sus implementos"), ("implementos", "platos, vasos, cubiertos y servilletas"), ("autoservicio", "servicio en que cada persona retira su bandeja en una línea"), ("buffet", "servicio con fuentes en una mesa común, donde cada persona se sirve"), ("porción estandarizada", "cantidad igual para todos, fijada en la ficha"), ("protocolo", "reglas de atención al cliente")],
    worked=[
        ("Contar puestos", "Un comedor de ejemplo tiene 5 mesas de 8 puestos. ¿Cuántos puestos hay?", ["Se multiplican las mesas por los puestos de cada una.", "5 × 8 = 40."], "40 puestos"),
        ("Identificar un servicio", "En un salón de ejemplo, el personal lleva los platos a cada mesa. ¿Qué tipo de servicio es?", ["El personal atiende en la mesa.", "Eso es servicio a la mesa."], "Servicio a la mesa"),
    ],
    mistakes=[("Servir porciones «a ojo», unas más grandes que otras.", "Los clientes reciben cantidades distintas y el costo del servicio cambia de un día a otro.", "Usa la porción estandarizada de la ficha."),
              ("Tomar los cubiertos por la parte que va a la boca.", "Se contaminan con las manos, aunque estén limpios los cubiertos.", "Tómalos por el mango o por la parte que no toca los alimentos.")],
    T=[
        ("abc", "{F} ¿Cuál es el tipo de servicio de este comedor?", "Autoservicio", "Servicio a la mesa", "Buffet", "La ficha indica que cada persona retira su bandeja en una línea de servicio."),
        ("=", "{F} ¿Cuántos puestos tiene el comedor?", "9*6", "Se multiplican las mesas por los puestos de cada mesa.", " puestos"),
        ("=", "{F} ¿Cuántos cubiertos (tenedores y cuchillos) se necesitan para todos los puestos?", "9*6*2", "Se calculan los puestos y se multiplican por dos cubiertos de cada puesto.", " cubiertos"),
        ("=", "{F} Si se agregan 6 puestos de reserva, ¿cuántas servilletas se necesitan en total?", "9*6+6", "Se suman los puestos del comedor y los de reserva; hay una servilleta por puesto.", " servilletas"),
        ("abc", "{F} ¿Cuántos gramos tiene la porción estandarizada de la ficha?", "150 g", "100 g", "200 g", "La ficha fija la porción estandarizada en 150 g."),
        ("=", "{F} De 9 kg de un producto (9.000 g), ¿cuántas porciones estandarizadas salen?", "9000//150", "Se divide el peso total por el peso de cada porción.", " porciones"),
        ("abc", "{F} Un ayudante entrega un plato con el borde manchado. ¿Qué corresponde?", "Cambiarlo o dejarlo con el borde limpio antes de entregarlo", "Entregarlo igual, porque lo importante es el contenido", "Limpiarlo con la manga", "El estándar exige el borde limpio, tanto por presentación como por higiene."),
        ("abc", "{F} Un producto frío se deja demasiado rato sobre la línea sin cuidar el frío. ¿Qué estándar se incumple?", "Lo frío se sirve frío", "La porción estandarizada", "El borde del plato limpio", "El estándar de presentación exige servir frío lo frío."),
        ("abc", "En Gastronomía: ¿cuál de estas disposiciones de mesa sigue los principios de orden y uniformidad?", "Todos los puestos con los mismos implementos en la misma posición", "Cada puesto con implementos distintos", "Implementos apilados en el centro de la mesa", "La uniformidad significa que todos los puestos se ven iguales y ordenados."),
        ("abc", "¿Cómo se toman los cubiertos al disponer una mesa?", "Por el mango o por la parte que no toca los alimentos, con las manos limpias", "Por la parte que toca la comida, con las manos limpias", "De cualquier forma, si se usa delantal", "Así se evita contaminar la parte que entrará en contacto con los alimentos."),
        ("abc", "{F} Un compañero sirve porciones «a ojo», unas más grandes que otras. ¿Qué consecuencia tiene?", "Los clientes reciben cantidades distintas y el costo del servicio varía", "Ninguna, porque todos quedan satisfechos", "Mejora la calidad, porque se adapta a cada persona", "La porción estandarizada asegura igualdad y costo controlado."),
        ("=", "{F} Se sirve una porción de 150 g a cada uno de los 54 puestos y se dispone de 10 kg (10.000 g). ¿Cuántos gramos sobran?", "10000-54*150", "Del total disponible se resta lo servido a todos los puestos.", " g"),
        ("abc", "{F} ¿Cuál es el orden correcto del protocolo de atención?", "Saludar, entregar la bandeja y desear buen provecho", "Entregar la bandeja, desear buen provecho y saludar", "Desear buen provecho, saludar y entregar la bandeja", "El protocolo comienza con el saludo y termina con el buen provecho."),
    ],
    ctx=("abc", "{F} Faltando poco para el almuerzo se confirma la llegada de 2 mesas adicionales de 6 puestos. ¿Qué corresponde hacer?", "Disponer 12 puestos más con los mismos implementos, verificando que estén limpios y completos", "Poner solo los vasos, porque lo demás se improvisa", "Pedir que las personas traigan sus propios implementos", "Se mantiene el estándar de uniformidad y de limpieza aunque el tiempo sea breve."),
    sc=[
        ("En Gastronomía: ¿qué es una porción estandarizada?", "Una cantidad igual para todos, fijada en la ficha", "Asegura igualdad en el servicio y control del costo."),
        ("¿Cómo se toman los cubiertos al disponer la mesa?", "Por el mango o la parte que no toca la comida", "Así no se contamina la parte que va a la boca."),
        ("¿Qué tipo de servicio es el autoservicio?", "Cada persona retira su bandeja en una línea", "Se distingue del servicio a la mesa y del buffet."),
    ],
    op=("Servicio de ejemplo a la mesa para 5 mesas de 4 puestos. Cada puesto lleva plato, vaso, tenedor, cuchillo, cuchara y servilleta. Se sirve una porción estandarizada de 120 g de un producto y se dispone de 6 kg (6.000 g). "
        "Calcula los puestos, los cubiertos (tenedores, cuchillos y cucharas) y los vasos necesarios, cuántas porciones salen del producto y escribe tres reglas de presentación y una de higiene para disponer la mesa.",
        "Puestos: 5 × 4 = 20. Cubiertos: 20 × 3 = 60. Vasos: 20. Porciones: 6.000 ÷ 120 = 50, que alcanzan para los 20 puestos. Reglas: porción estandarizada, borde del plato limpio, lo frío servido frío. Higiene: tomar los cubiertos por el mango y con manos limpias.",
        ["calcula 20 puestos, 60 cubiertos y 20 vasos", "calcula 50 porciones", "nombra tres reglas de presentación y una de higiene"],
        ["hoja con cálculos y cuatro reglas"],
        ["contar solo dos cubiertos por puesto", "olvidar convertir kilos a gramos", "no mencionar higiene"],
        "Pregunta: «¿cuántos cubiertos lleva cada puesto?». Si responde 2, vuelve a leer el enunciado."),
    reinforce="Dibuja el esquema de un comedor de ejemplo con 4 mesas y anota los implementos de un puesto y el total de puestos.",
    extend="Explica por qué la porción estandarizada es importante tanto para el cliente como para el costo del servicio.",
)

# ============================================================ OAE-04, clase 5
F = ("Ficha 5 (control de calidad de ejemplo, inventado). Pauta sensorial para una salsa base: aspecto, color, olor, sabor y textura, cada uno con puntaje de 1 (muy deficiente) a 5 (muy bueno). "
     "Criterio de aceptación (de ejemplo): suma de al menos 20 puntos de 25 y ningún atributo con 1 o 2. "
     "Lote A: aspecto 4, color 5, olor 4, sabor 4, textura 4. Lote B: aspecto 5, color 5, olor 5, sabor 5, textura 2. "
     "Análisis sensorial: se evalúa con los sentidos. Análisis físico-químico básico: se mide con instrumentos, por ejemplo la temperatura o la acidez. Análisis microbiológico: lo realiza un laboratorio.")
build(
    O4, 5, F,
    use="Aprenderé a comparar alternativas con una pauta de calidad, verificar si un lote es aceptable y reconocer qué análisis hace cada persona o laboratorio.",
    prior=["Conozco las características organolépticas.", "Sé sumar puntajes.", "Conozco hallazgos y acciones correctivas."],
    explain=[
        "El aseguramiento de la calidad es el conjunto de controles que busca que los productos cumplan siempre los estándares. Un control comienza en la recepción de materias primas, sigue durante la elaboración y termina en el producto terminado. Para decidir si un lote es aceptable se usa una pauta con criterios fijos, aplicada igual a todas las alternativas que se comparan.",
        "Hay tres tipos de análisis. El sensorial se hace con los sentidos y sirve para evaluar aspecto, color, olor, sabor y textura. El físico-químico mide con instrumentos, por ejemplo la temperatura o la acidez. El microbiológico detecta microorganismos y lo hace un laboratorio. Cada análisis responde una pregunta distinta, y ninguno reemplaza a los otros.",
        "El criterio de aceptación combina dos condiciones: una suma mínima y que ningún atributo sea muy bajo. Un lote con una suma alta pero un atributo muy deficiente no se acepta. Un lote no aceptable se separa, se registra el hallazgo y la jefatura decide su destino." + LIM,
    ],
    vocab=[("aseguramiento de la calidad", "controles para que los productos cumplan siempre los estándares"), ("pauta sensorial", "lista de atributos con puntaje para evaluar con los sentidos"), ("criterio de aceptación", "condiciones que debe cumplir un lote para aceptarse"), ("lote", "grupo de producto elaborado junto"), ("análisis físico-químico", "medición con instrumentos, como temperatura o acidez"), ("análisis microbiológico", "detección de microorganismos, hecha por un laboratorio")],
    worked=[
        ("Sumar una pauta", "En una pauta de ejemplo de cinco atributos, un lote obtiene 3, 4, 4, 5 y 4. ¿Cuántos puntos suma?", ["Se suman los puntajes de los cinco atributos.", "3 + 4 + 4 + 5 + 4 = 20."], "20 puntos"),
        ("Aplicar el criterio", "Un lote de ejemplo suma 23 puntos, pero un atributo tiene puntaje 1. Con el criterio de «al menos 20 puntos y ningún atributo con 1 o 2», ¿se acepta?", ["La suma cumple.", "Pero hay un atributo con 1."], "No se acepta"),
    ],
    mistakes=[("Aceptar un lote solo porque su suma es alta.", "Un atributo muy deficiente puede significar un defecto importante.", "Verifica las dos condiciones del criterio: suma mínima y ningún atributo muy bajo."),
              ("Evaluar a un proveedor con una pauta y a otro con otra.", "La comparación no es justa ni confiable.", "Aplica la misma pauta a todas las alternativas que comparas.")],
    T=[
        ("abc", "En Gastronomía: ¿qué es el análisis sensorial?", "La evaluación de un producto con los sentidos", "La medición de la acidez con un instrumento", "El conteo de microorganismos en un laboratorio", "Lo sensorial se hace con vista, olfato, gusto y tacto; lo demás es físico-químico o microbiológico."),
        ("=", "{F} ¿Cuántos puntos suma el lote A?", "4+5+4+4+4", "Se suman los cinco puntajes del lote.", " puntos"),
        ("=", "{F} ¿Cuántos puntos suma el lote B?", "5+5+5+5+2", "Se suman los cinco puntajes del lote.", " puntos"),
        ("abc", "{F} ¿Es aceptable el lote A?", "Sí: suma 21 y ningún atributo tiene 1 o 2", "No: no llega a 25 puntos", "No: tiene atributos con 4", "Cumple las dos condiciones: la suma mínima y ningún atributo muy bajo."),
        ("abc", "{F} ¿Es aceptable el lote B?", "No, porque la textura tiene 2 puntos", "Sí, porque suma más que el lote A", "Sí, porque tiene cuatro atributos con 5", "Aunque suma 22, tiene un atributo con 2, que el criterio no permite."),
        ("abc", "{F} ¿Qué lote tiene mayor puntaje total?", "El lote B, con 22 puntos", "El lote A, con 21 puntos", "Ambos tienen el mismo total", "B suma 22 y A suma 21; el total más alto no implica que sea aceptable."),
        ("abc", "{F} ¿Qué análisis realiza un laboratorio?", "El microbiológico", "El sensorial", "El de color y olor", "La ficha indica que el análisis microbiológico lo realiza un laboratorio."),
        ("abc", "{F} ¿Cuál es un ejemplo de análisis físico-químico básico?", "Medir con un instrumento la temperatura de un producto", "Evaluar el sabor con el paladar", "Contar microorganismos en un laboratorio", "La medición con instrumentos corresponde a un análisis físico-químico."),
        ("=", "{F} Si el lote B mejorara su textura de 2 a 4 y los otros puntajes no cambiaran, ¿cuántos puntos sumaría?", "5+5+5+5+4", "Se suman los cinco puntajes con la textura corregida.", " puntos"),
        ("abc", "{F} Un cocinero dice que el lote B debe aceptarse porque suma más que el A. ¿Qué respuesta es correcta?", "No: el criterio exige también que ningún atributo tenga 1 o 2", "Sí, porque el total es lo único que importa", "Solo si un cliente lo pide", "El criterio tiene dos condiciones y B incumple una."),
        ("abc", "{F} ¿Qué corresponde hacer con el lote B?", "Separarlo, registrar el hallazgo de la textura y avisar a la jefatura para decidir su destino", "Servirlo igual, porque suma 22", "Mezclarlo con el lote A para mejorar el promedio", "Un lote no aceptable se separa y se registra; mezclar ocultaría el problema."),
        ("abc", "Para elegir entre dos proveedores de un mismo producto, ¿qué se necesita?", "Aplicar la misma pauta a las muestras de ambos, con los mismos criterios", "Evaluar a uno con una pauta y al otro con otra", "Elegir el más barato sin evaluar", "La comparación solo es válida si ambos se evalúan igual."),
        ("=", "En un mes de ejemplo se evaluaron 25 lotes y 20 resultaron aceptables. ¿Qué porcentaje no fue aceptable?", "(25-20)*100//25", "Se calcula cuántos lotes no fueron aceptables y se expresa como porcentaje del total.", " %"),
    ],
    ctx=("abc", "{F} Se evalúan con la misma pauta una muestra del proveedor X (aspecto 3, color 4, olor 4, sabor 3, textura 4) y otra del proveedor Y (aspecto 5, color 5, olor 5, sabor 4, textura 1). ¿Cuál se acepta?", "Ninguna: X suma 18 y Y tiene un atributo con 1", "Ambas, porque tienen buenos puntajes en general", "Solo Y, porque suma 20", "X no llega a 20 puntos e Y incumple la condición de ningún atributo con 1 o 2."),
    sc=[
        ("En Gastronomía: ¿qué dos condiciones tiene el criterio de aceptación de la ficha?", "Suma mínima y ningún atributo con 1 o 2", "Ambas deben cumplirse para aceptar el lote."),
        ("¿Quién hace el análisis microbiológico?", "Un laboratorio", "Requiere equipos y personal especializados que solo tiene un laboratorio."),
        ("¿Qué se hace con un lote no aceptable?", "Se separa, se registra y decide la jefatura", "Así no se mezcla con lotes buenos."),
    ],
    op=("Con la misma pauta y criterio de la ficha de esta clase (suma de al menos 20 y ningún atributo con 1 o 2), se evalúan dos lotes de aliño. Lote C: aspecto 3, color 4, olor 4, sabor 4, textura 4. Lote D: aspecto 4, color 4, olor 3, sabor 5, textura 5. "
        "Calcula el puntaje de cada lote, di cuál es aceptable y por qué, y escribe qué harías con el lote que no se acepta y qué análisis mide la temperatura con un instrumento.",
        "Lote C: 3 + 4 + 4 + 4 + 4 = 19, no llega a 20, por lo que no se acepta. Lote D: 4 + 4 + 3 + 5 + 5 = 21 y ningún atributo con 1 o 2, por lo que se acepta. El lote C se separa, se registra y la jefatura decide su destino. La temperatura se mide con un análisis físico-químico.",
        ["calcula 19 y 21 puntos", "aplica las dos condiciones del criterio", "indica separar, registrar y el análisis físico-químico"],
        ["hoja con puntajes, decisión y acciones"],
        ["aceptar C por tener atributos en 4", "olvidar la segunda condición", "mezclar los lotes"],
        "Pregunta: «¿cuánto suma el lote C?». Si no llega a 19, repasa la suma."),
    reinforce="Inventa una pauta de cuatro atributos con puntajes del 1 al 5 y evalúa dos lotes inventados con un criterio escrito por ti.",
    extend="Explica por qué ningún análisis por sí solo basta para asegurar que un producto sea de calidad e inocuo.",
)
