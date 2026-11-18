"""Metalurgia Extractiva TP 3.º y 4.º medio: OAE-03 (minerales solubles), OAE-04 (fundición, tostación y refinación) y OAE-05 (muestreo). Todo en papel, con datos de ejemplo; sin procedimientos operativos."""
from __future__ import annotations

from tp_mete_common import AVISO, EMER, build

O3 = "TP-METE-3y4-OAE-03"
O4 = "TP-METE-3y4-OAE-04"
O5 = "TP-METE-3y4-OAE-05"

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Planta Lixiviación Demo» de la empresa ficticia «Minera Demo» trata un mineral soluble apilado en una pila de 10.000 toneladas con ley de 1 %. Una solución circula por la pila con un caudal de 120 metros cúbicos por hora (m³/h) y se recoge en una poza. "
     "Peligros anotados: la solución es corrosiva y puede salpicar, la poza está abierta y sin cerco, hay derrames sobre un suelo resbaladizo, y en las zonas cerradas pueden acumularse vapores. Datos de ejemplo.")
build(
    O3, 1, F,
    use="Aprenderé qué es un mineral soluble y qué son la disolución, la purificación y la recuperación, qué peligros tiene una planta de este tipo y por qué los insumos y las soluciones solo los maneja personal autorizado.",
    prior=["Sé qué son la ley, el concentrado y el relave.", "Sé calcular el metal contenido con una ley.", "Sé la jerarquía de controles."],
    explain=[
        "Un mineral soluble es aquel cuyo metal puede pasar a un líquido adecuado, llamado solución. El tratamiento tiene tres principios. La disolución es el paso del metal desde el mineral hacia la solución. La purificación separa y concentra el metal disuelto de otras sustancias que también están en la solución. La recuperación obtiene el metal en forma sólida a partir de la solución purificada. Entre una etapa y otra la solución circula por tuberías y pozas; por eso se mide su caudal, que es el volumen que pasa por unidad de tiempo, por ejemplo en metros cúbicos por hora (m³/h). 1 metro cúbico equivale a 1.000 litros.",
        "Para el cálculo se usa el metal contenido: toneladas por ley dividido por 100. En una pila de ejemplo de 3.000 toneladas con ley de 2 %, hay 60 toneladas de metal. Con un caudal de ejemplo de 50 m³/h durante 10 horas circulan 500 metros cúbicos. Estos valores son de ejemplo; los reales los fijan el proyecto y la norma vigente.",
        f"Las soluciones y los insumos de estos procesos son sustancias peligrosas: pueden quemar la piel y los ojos, y sus vapores o derrames dañan a las personas y al ambiente. Se manejan con su hoja de datos de seguridad (HDS), rótulos, zonas controladas y personal autorizado; este cuaderno no enseña a prepararlas ni a usarlas. Las medidas siguen la jerarquía de controles, y el ambiente se protege con una base impermeable bajo la pila, control de derrames y un plan de contingencia. La autoridad minera y la sanitaria fiscalizan según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("mineral soluble", "mineral cuyo metal puede pasar a un líquido adecuado"), ("solución", "líquido que lleva sustancias disueltas"), ("disolución", "paso del metal desde el mineral hacia la solución"), ("purificación", "separación y concentración del metal disuelto respecto de otras sustancias de la solución"), ("recuperación", "obtención del metal sólido a partir de la solución purificada"), ("caudal", "volumen que pasa por unidad de tiempo, por ejemplo en m³/h"), ("poza", "depósito abierto donde se recoge una solución"), ("plan de contingencia", "documento que dice quién avisa, a quién y cómo se actúa ante un derrame o una emergencia")],
    worked=[
        ("Metal contenido", "Una pila de ejemplo tiene 3.000 toneladas con ley de 2 %. ¿Cuántas toneladas de metal contiene?", ["Se multiplican las toneladas por la ley: 3.000 por 2.", "Se divide por 100: 6.000 dividido por 100 es 60."], "60 toneladas de metal"),
        ("Volumen de solución", "Una solución de ejemplo circula a 50 m³/h durante 10 horas. ¿Cuántos metros cúbicos circulan?", ["Se multiplica el caudal por las horas.", "50 por 10 es 500."], "500 metros cúbicos"),
    ],
    mistakes=[("Creer que una solución transparente no es peligrosa.", "El aspecto no informa el peligro: una solución clara puede ser corrosiva.", "El peligro se conoce con la HDS y el rótulo, y el manejo es de personal autorizado."),
              ("Creer que leer sobre los procesos habilita para preparar o manipular soluciones.", "Manipular soluciones y insumos exige instructor autorizado, HDS y norma vigente.", "Aprende aquí el concepto y deja el manejo a personal autorizado.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es un mineral soluble?", "Uno cuyo metal puede pasar a un líquido adecuado", "Uno que se derrite con facilidad", "Uno que flota en el agua", "Un mineral soluble se trata por disolución; derretirse es otro proceso."),
        ("abc", "En el tratamiento de minerales solubles: ¿qué es la disolución?", "El paso del metal desde el mineral hacia la solución", "La reducción del tamaño de las rocas", "La obtención del metal sólido desde la solución", "La disolución traslada el metal a la solución; el metal sólido se obtiene en la recuperación."),
        ("abc", "En el tratamiento de minerales solubles: ¿qué es la purificación?", "Separar y concentrar el metal disuelto de otras sustancias de la solución", "Agregar agua para diluir la solución", "Moler el mineral hasta hacerlo polvo", "La purificación limpia y concentra el metal disuelto; no es diluir ni moler."),
        ("=", "{F} ¿Cuántas toneladas de metal contiene la pila?", "10000*1//100", "Se multiplican las toneladas por la ley y se divide por 100.", " toneladas de metal"),
        ("=", "{F} ¿Cuántos metros cúbicos de solución circulan por la pila en un día completo de 24 horas?", "120*24", "Se multiplica el caudal por las horas del día.", " metros cúbicos"),
        ("=", "{F} ¿Cuántos litros de solución pasan por la pila en una hora?", "120*1000", "Se multiplica el caudal en metros cúbicos por 1.000 litros.", " litros"),
        ("abc", "{F} ¿Cuál es el riesgo asociado a que la solución sea corrosiva y pueda salpicar?", "Que el contacto dañe la piel o los ojos de una persona", "Que el mineral aumente su ley", "Que la pila crezca de tamaño", "El riesgo es un daño a las personas; la ley o el tamaño de la pila no dependen de las salpicaduras."),
        ("abc", "{F} Cercar la poza con barandas para impedir el acceso es un control de tipo:", "Ingeniería, porque pone una barrera física entre las personas y el peligro", "De EPP, porque protege el cuerpo de cada persona", "Administrativo, porque informa a las personas", "Una baranda es una barrera física; informar o proteger a cada persona son otros niveles."),
        ("abc", "{F} Una estudiante dice: «leí la ficha, así que puedo preparar la solución que se hace circular por la pila». ¿Qué respuesta es correcta?", "Es falso: manejar y preparar soluciones exige instructor autorizado, HDS y norma vigente", "Es cierto, si diluye bien la solución", "Es cierto, si usa lentes y guantes", "El EPP y la dilución no reemplazan la formación ni la autorización."),
        ("abc", "{F} Durante una visita de ejemplo, ves que una tubería derrama solución sobre el piso. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a cerrar la tubería con tus manos", "Pasar por encima del derrame para llegar antes", "Acercarse a un derrame sin formación puede causar una lesión; se avisa a quienes pueden actuar."),
        ("=", "{F} Si por una falla el caudal bajara a 90 m³/h, ¿cuántos metros cúbicos circularían en un día de 24 horas?", "90*24", "Se multiplica el nuevo caudal por las horas del día.", " metros cúbicos"),
        ("abc", "{F} El jefe dice que la poza no necesita cerco «porque nunca ha pasado nada». ¿Cuál es la mejor respuesta?", "Que ausencia de accidentes no elimina el peligro, y que la poza se controla con barreras según la norma vigente", "Que tiene razón, porque la poza no se usa de noche", "Que tiene razón, si todos conocen la poza", "El peligro existe aunque no haya ocurrido un accidente; las barreras previenen."),
        ("=", "{F} ¿Cuántas horas tardan en circular 14.400 metros cúbicos con el caudal de la ficha?", "14400//120", "Se divide el volumen entre el caudal.", " horas"),
    ],
    ctx=("abc", "Un vecino te ofrece un bidón con un líquido de minería para «probar a sacar cobre de unas piedras en tu patio». ¿Qué respondes?", "Que no, porque manejar esas sustancias exige instructor autorizado y norma vigente, y que se lo contarás a un adulto responsable", "Que sí, si lo haces lejos de la casa", "Que sí, si usas guantes de cocina", "Esas sustancias son peligrosas; el lugar o los guantes no reemplazan la formación y la autorización."),
    sc=[
        ("En Metalurgia Extractiva: ¿qué es la recuperación en el tratamiento de minerales solubles?", "La obtención del metal sólido a partir de la solución purificada", "La recuperación entrega el metal en forma sólida."),
        ("En una planta de minerales solubles: ¿qué es el caudal?", "El volumen de solución que pasa por unidad de tiempo", "El caudal relaciona volumen y tiempo, como m³ por hora."),
        ("En el manejo de sustancias: ¿quién prepara y maneja las soluciones de un proceso?", "Personal autorizado, con HDS y norma vigente", "Estas sustancias son peligrosas y exigen formación."),
    ],
    op=("Ficha de ejemplo: la «Planta Lixiviación Cordón Demo» tiene una pila de 6.000 toneladas con ley de 2 %. La solución circula a 80 m³/h y se recoge en una poza sin cerco. Escribe (a) cuántas toneladas de metal contiene la pila, (b) cuántos metros cúbicos circulan en 24 horas, (c) cuántos litros pasan en una hora, (d) un peligro de la poza y su riesgo, (e) un control de ingeniería y uno administrativo, (f) qué haces si ves un derrame.",
        "(a) 6.000 × 2 ÷ 100 = 120 toneladas. (b) 80 × 24 = 1.920 metros cúbicos. (c) 80 × 1.000 = 80.000 litros. (d) Peligro: la poza abierta; riesgo: que una persona caiga o se exponga a la solución. (e) Ingeniería: cercar la poza con barandas; administrativo: una señal y una capacitación. (f) No acercarme a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien el metal", "calcula bien los metros cúbicos", "calcula bien los litros", "distingue peligro y riesgo", "propone los dos controles", "indica no acercarse y avisar"],
        ["hoja con las seis respuestas"],
        ["olvidar dividir por 100", "no pasar metros cúbicos a litros", "responder que se acerca a cerrar la tubería"],
        "Pregunta: «¿qué barrera física impediría que alguien cayera a la poza?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe con tus palabras la disolución, la purificación y la recuperación, y calcula el volumen que circula en 6 horas a un caudal inventado de 40 m³/h.",
    extend="Explica con un ejemplo por qué una solución clara puede ser peligrosa.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Planta Lixiviación Demo». Documentos: la HDS de la solución de proceso, el registro de caudal y ley de solución, el plan de contingencia ante derrames (quién avisa, a quién y cómo se evacua), "
     "el permiso de trabajo (autorización escrita antes de una tarea de riesgo, con condiciones y responsables) y el informe del laboratorio. Registro de ejemplo: lunes, 2.400 m³ de solución con 3 g/L de metal; martes, 2.400 m³ con 2 g/L; "
     "miércoles, 2.000 m³ con 3 g/L (el caudal bajó por una detención). Equivalencia: 1 g/L es lo mismo que 1 kg/m³. Roles: operador de planta, supervisor, laboratorista, prevencionista de riesgos y encargado ambiental.")
build(
    O3, 2, F,
    use="Aprenderé los documentos de una planta de minerales solubles (HDS, registro de caudal y ley, plan de contingencia, permiso de trabajo e informe de laboratorio), los roles y cómo se calcula el metal que lleva una solución.",
    prior=["Sé qué son disolución, purificación y recuperación.", "Sé calcular volúmenes con un caudal.", "Sé leer un registro escrito."],
    explain=[
        "Los documentos ordenan el trabajo y respaldan las decisiones. La HDS informa los peligros de una sustancia. El registro de caudal y ley anota cuánta solución pasó y cuánto metal llevaba. El informe del laboratorio entrega la ley medida de una muestra. El plan de contingencia indica quién avisa, a quién y cómo se actúa ante un derrame. El permiso de trabajo es una autorización escrita, previa a una tarea de riesgo, que fija condiciones y responsables; cada firma certifica que quien firma comprobó lo que declara.",
        "La ley de una solución se mide en gramos por litro (g/L): 1 g/L equivale a 1 kg/m³, porque 1 m³ son 1.000 litros y 1 kg son 1.000 gramos. Por eso el metal que lleva una solución, en kilos, es el volumen en metros cúbicos multiplicado por la ley en g/L. En un registro de ejemplo, 500 m³ con 4 g/L llevan 2.000 kilos de metal. Si un día la ley se aleja de las demás, se informa y se busca la causa; el dato no se cambia.",
        f"Roles: el operador vigila su área, el supervisor decide, el laboratorista mide la ley, el prevencionista asesora en riesgos y el encargado ambiental vigila derrames y descargas. Un registro no se llena de antemano ni se firma por otra persona. {EMER} {AVISO}",
    ],
    vocab=[("hoja de datos de seguridad (HDS)", "documento que informa los peligros de una sustancia y las medidas generales de prevención"), ("registro de caudal y ley", "anotación de cuánta solución pasó y cuánto metal llevaba"), ("plan de contingencia", "documento que dice quién avisa, a quién y cómo se actúa ante un derrame"), ("permiso de trabajo", "autorización escrita previa a una tarea de riesgo, con condiciones y responsables"), ("gramos por litro (g/L)", "unidad de ley de una solución; 1 g/L equivale a 1 kg/m³"), ("encargado ambiental", "persona que vigila derrames, descargas y el cumplimiento del plan ambiental")],
    worked=[
        ("Metal en la solución", "Un registro de ejemplo anota 500 m³ de solución con 4 g/L. ¿Cuántos kilos de metal llevan?", ["1 g/L equivale a 1 kg/m³, así que 4 g/L son 4 kg/m³.", "500 por 4 es 2.000."], "2.000 kilos de metal"),
        ("Elegir el documento", "Antes de una tarea de riesgo, una supervisora de ejemplo quiere dejar por escrito las condiciones y quién responde. ¿Qué documento usa?", ["Es una autorización escrita previa a la tarea.", "Ese documento es el permiso de trabajo."], "El permiso de trabajo"),
    ],
    mistakes=[("Firmar un permiso de trabajo por otra persona porque está ocupada.", "Cada firma certifica que esa persona comprobó las condiciones; firmar por otra es un registro falso.", "Cada responsable comprueba y firma por sí mismo."),
              ("Cambiar un dato del registro porque se aleja de los demás.", "El dato distinto puede mostrar un problema real.", "Se anota el dato real, se informa al supervisor y se busca la causa.")],
    T=[
        ("abc", "En una planta de minerales solubles: ¿qué es un plan de contingencia ante derrames?", "El documento que dice quién avisa, a quién y cómo se actúa ante un derrame", "El registro del metal que lleva la solución cada día", "El informe del laboratorio con la ley de una muestra", "El plan de contingencia organiza la respuesta; los otros dos son registros de datos."),
        ("abc", "En el trabajo de una planta: ¿qué es un permiso de trabajo?", "Una autorización escrita previa a una tarea de riesgo, con condiciones y responsables", "Una pauta que se llena al final del turno", "El certificado de pureza de un producto", "El permiso se emite antes de la tarea; no es una pauta de cierre ni un certificado."),
        ("abc", "En una solución de planta: ¿qué significa que 1 g/L equivale a 1 kg/m³?", "Que la misma ley puede expresarse en ambas unidades, porque 1 m³ son 1.000 L y 1 kg son 1.000 g", "Que un litro de cualquier solución pesa un kilo", "Que las dos unidades no se pueden comparar", "Los factores de 1.000 se compensan y la equivalencia queda exacta."),
        ("=", "{F} ¿Cuántos kilos de metal llevó la solución del lunes?", "2400*3", "Se multiplica el volumen en metros cúbicos por la ley en g/L.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal llevó la solución del martes?", "2400*2", "Se multiplica el volumen en metros cúbicos por la ley en g/L.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal llevó la solución del miércoles?", "2000*3", "Se multiplica el volumen en metros cúbicos por la ley en g/L.", " kg"),
        ("abc", "{F} ¿Qué día la solución llevó menos metal?", "El martes, con 4.800 kg", "El miércoles, porque tuvo menos volumen", "El lunes, porque fue el primer día", "El martes llevó 4.800 kg, menos que los 7.200 y 6.000 de los otros días."),
        ("abc", "{F} ¿Qué corresponde frente a la baja de ley del martes?", "Anotar el dato real, informar al supervisor y pedir que se revise la causa", "Cambiar el 2 g/L por 3 g/L para que coincida con el lunes", "Ignorarla, porque el volumen fue el mismo", "Corregir el dato oculta un posible problema; se informa y se revisa."),
        ("abc", "{F} ¿Quién mide la ley de las muestras de solución?", "El laboratorista", "El encargado ambiental", "El operador de la poza", "La ley se mide en el laboratorio; el encargado ambiental vigila derrames y descargas."),
        ("=", "{F} ¿Cuántos kilos de metal llevó la solución durante los tres días?", "2400*3+2400*2+2000*3", "Se suman los kilos de cada día.", " kg"),
        ("abc", "{F} Un operador propone firmar el permiso de trabajo de un compañero «porque está ocupado». ¿Cuál es la mejor respuesta?", "No se firma por otra persona: cada firma certifica que quien firma comprobó las condiciones", "Se puede, si el compañero lo autoriza de palabra", "Se puede, si se firma con otro color", "Una firma que certifica una comprobación no puede darla otra persona."),
        ("=", "{F} Si el miércoles hubiera circulado el mismo volumen del lunes y de martes (2.400 m³) con la misma ley de 3 g/L, ¿cuántos kilos más habría llevado?", "(2400-2000)*3", "Se multiplica el volumen que faltó por la ley.", " kg"),
        ("abc", "{F} Durante un derrame de ejemplo, ¿qué corresponde a una persona sin formación?", "No acercarse a la zona de riesgo y avisar; el plan de contingencia indica quién actúa", "Consultar la HDS y limpiar el derrame por su cuenta", "Completar un permiso de trabajo y empezar a limpiar", "La respuesta al derrame la hace personal autorizado; quien no tiene formación se aleja y avisa."),
    ],
    ctx=("abc", "Un compañero de práctica te pide que cambies en el registro el volumen del miércoles de 2.000 a 2.400 m³ «para que no se note la detención». ¿Qué respondes?", "Que no, porque no se altera un registro, y que lo consultarás con un adulto responsable", "Que sí, porque la diferencia es pequeña", "Que sí, si avisas después", "Alterar un registro oculta lo que ocurrió y quita la base para decidir."),
    sc=[
        ("En una planta de minerales solubles: ¿qué es un permiso de trabajo?", "Una autorización escrita previa a una tarea de riesgo", "El permiso fija condiciones y responsables antes de la tarea."),
        ("En una solución de planta: ¿cómo se calculan los kilos de metal?", "Multiplicando los metros cúbicos por la ley en g/L", "Un g/L equivale a un kg por metro cúbico."),
        ("En el control de registros de planta: ¿qué se hace si un dato se aleja de los demás?", "Se anota el dato real, se informa y se busca la causa", "El dato distinto puede mostrar un problema."),
    ],
    op=("Ficha de ejemplo: «Planta Lixiviación Cordón Demo». Registro: lunes, 1.500 m³ de solución con 5 g/L; martes, 1.500 m³ con 3 g/L. Escribe (a) los kilos de metal de cada día, (b) cuál fue mayor y por cuántos kilos, (c) qué documento consultarías para conocer los peligros de la solución, (d) qué haces si el informe del laboratorio del martes trae una ley distinta de la del registro, (e) quién debe responder a un derrame.",
        "(a) Lunes: 1.500 × 5 = 7.500 kg; martes: 1.500 × 3 = 4.500 kg. (b) El lunes, por 3.000 kg. (c) La HDS de la solución. (d) Informar al supervisor y al laboratorio para revisar la diferencia, sin cambiar ningún dato por cuenta propia. (e) Personal autorizado, según el plan de contingencia.",
        ["calcula bien los kilos de cada día", "calcula bien la diferencia", "nombra la HDS", "informa la diferencia sin alterar el registro", "nombra a personal autorizado"],
        ["hoja con las cinco respuestas"],
        ["olvidar multiplicar por la ley", "cambiar el dato del registro", "decir que responde cualquier estudiante"],
        "Pregunta: «¿qué dos números multiplicas para tener el metal de cada día?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa el registro de dos días con volumen y ley de una solución y calcula los kilos de metal de cada día.",
    extend="Explica con un ejemplo por qué el plan de contingencia y el permiso de trabajo cumplen funciones distintas.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (balance de ejemplo, inventado). Una pila de la «Planta Lixiviación Demo» contiene 2.000 toneladas de mineral con ley de 1 % (20 toneladas de metal; 1 tonelada son 1.000 kilos). "
     "Durante el ciclo se recogieron 8.000 m³ de solución rica (solución con metal disuelto) con una ley promedio de 2 g/L. En la purificación y la recuperación se obtiene como metal sólido el 90 % del metal disuelto. Datos de ejemplo.")
build(
    O3, 3, F,
    use="Aprenderé a analizar el balance de metal de una pila: calcular el metal disuelto, la extracción y el metal recuperado, y a distinguir lo que hace cada etapa.",
    prior=["Sé qué son disolución, purificación y recuperación.", "Sé calcular kilos de metal con volumen y ley de solución.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "El balance de metal de un ciclo sigue el metal de una etapa a otra. Primero se calcula el metal del mineral: toneladas por ley dividido por 100, pasado a kilos. Después, el metal disuelto en la solución rica: metros cúbicos por ley en g/L. La extracción es el porcentaje del metal del mineral que pasó a la solución: kilos disueltos divididos por kilos del mineral y multiplicado por 100. Finalmente se aplica la eficiencia de la purificación y la recuperación para obtener los kilos de metal sólido.",
        "Un ejemplo: una pila de 500 toneladas con ley de 2 % tiene 10.000 kilos de metal. Si se recogen 1.000 m³ con 5 g/L, hay 5.000 kilos disueltos y la extracción es 50 %. La solución rica es la que lleva metal disuelto; la que sale de la purificación con poco metal y vuelve a la pila se llama refino. Cada etapa tiene su propio porcentaje, y no deben confundirse: la extracción depende de cuánto metal se disuelve, y la eficiencia de purificación depende de cuánto de lo disuelto se recupera.",
        f"Estos números son de ejemplo; los reales los miden y registran personas autorizadas. Si una cuenta da un resultado imposible, como más metal recuperado que disuelto, se revisan los datos y se informa. {EMER} {AVISO}",
    ],
    vocab=[("solución rica", "solución que lleva metal disuelto"), ("refino", "solución con poco metal que sale de la purificación y vuelve a la pila"), ("extracción", "porcentaje del metal del mineral que pasó a la solución"), ("eficiencia de purificación y recuperación", "porcentaje del metal disuelto que se obtiene como metal sólido"), ("metal disuelto", "metal que lleva la solución, igual a metros cúbicos por ley en g/L")],
    worked=[
        ("Extracción", "Una pila de ejemplo tiene 10.000 kilos de metal y la solución rica lleva 5.000 kilos. ¿Cuál es la extracción?", ["Se divide el metal disuelto por el del mineral: 5.000 entre 10.000.", "Multiplicado por 100 da 50 por ciento."], "50 %"),
        ("Metal recuperado", "De 5.000 kilos de metal disuelto se recupera el 80 %. ¿Cuántos kilos son?", ["80 por ciento es 80 de cada 100.", "5.000 por 80 dividido por 100 es 4.000."], "4.000 kilos"),
    ],
    mistakes=[("Confundir la extracción con la eficiencia de la purificación.", "La extracción compara el metal disuelto con el del mineral; la eficiencia compara el metal sólido con el disuelto.", "Cada porcentaje se calcula con su propia base."),
              ("Aceptar más metal recuperado que disuelto.", "Sería obtener más metal del que había en la solución.", "Se revisan los datos y se informa el error.")],
    T=[
        ("abc", "En el tratamiento de minerales solubles: ¿qué es la solución rica?", "La solución que lleva metal disuelto", "La solución sin metal que vuelve a la pila", "El mineral con una ley alta", "La solución rica lleva el metal; la que vuelve con poco metal es el refino."),
        ("abc", "En el tratamiento de minerales solubles: ¿qué es la extracción?", "El porcentaje del metal del mineral que pasó a la solución", "El porcentaje del metal disuelto que se obtiene como metal sólido", "El porcentaje de agua que se evapora de la poza", "La extracción mide la disolución; el metal sólido es la etapa de recuperación."),
        ("abc", "En el tratamiento de minerales solubles: ¿qué significa recuperar el metal de la solución?", "Obtenerlo en forma sólida a partir de la solución purificada", "Devolver la solución rica a la pila", "Medir la ley de la solución en el laboratorio", "Recuperar es obtener el metal sólido; devolver o medir son otras acciones."),
        ("=", "{F} ¿Cuántos kilos de metal contiene la pila?", "2000*1*1000//100", "Se multiplican las toneladas por la ley, se divide por 100 y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal lleva disueltos la solución rica?", "8000*2", "Se multiplican los metros cúbicos por la ley en g/L.", " kg"),
        ("=", "{F} ¿Cuál es la extracción de la pila, en porcentaje?", "8000*2*100//(2000*1*1000//100)", "Se divide el metal disuelto por el metal de la pila y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kilos de metal sólido se obtienen?", "8000*2*90//100", "Se aplica el 90 % al metal disuelto.", " kg"),
        ("abc", "{F} Un compañero dice que la extracción es 90 % porque «es lo que dice la purificación». ¿Qué corresponde?", "Corregirlo: la extracción compara el metal disuelto con el metal de la pila; el 90 % es otra etapa", "Aceptarlo, porque el 90 % es el único porcentaje de la ficha", "Corregirlo: la extracción es el metal sólido dividido por el metal de la pila", "La extracción tiene su propia base: el metal del mineral. El 90 % se aplica al metal disuelto."),
        ("=", "{F} ¿Cuántos kilos de metal de la pila quedan sin disolver?", "2000*1*1000//100-8000*2", "Se resta el metal disuelto al metal de la pila.", " kg"),
        ("=", "{F} ¿Qué porcentaje del metal de la pila se obtiene como metal sólido?", "8000*2*90//100*100//(2000*1*1000//100)", "Se divide el metal sólido por el metal de la pila y se multiplica por 100.", " %"),
        ("abc", "{F} En semanas sucesivas la ley de la solución rica baja de 3 a 2 y a 1 g/L. ¿Qué indica?", "Que queda menos metal por disolver y el ciclo se acerca a su fin", "Que la purificación está recuperando más metal", "Que la solución se hizo más corrosiva", "La baja de ley en la solución rica muestra que cada vez se disuelve menos."),
        ("=", "{F} Si la purificación y la recuperación lograran 95 %, ¿cuántos kilos de metal sólido se obtendrían?", "8000*2*95//100", "Se aplica el nuevo porcentaje al metal disuelto.", " kg"),
        ("abc", "{F} El jefe dice que mejorar la eficiencia de la purificación aumentará la extracción de la pila. ¿Cuál es la mejor objeción?", "Son etapas distintas: la extracción depende de cuánto metal se disuelve, y la eficiencia de cuánto de lo disuelto se recupera", "Ninguna, porque las dos son el mismo porcentaje", "Que la eficiencia solo cambia con el caudal", "Mejorar la recuperación no disuelve más metal del mineral."),
    ],
    ctx=("abc", "Un compañero te propone armar una pila pequeña en el patio con piedras y líquidos de limpieza «para ver si sale cobre». ¿Qué respondes?", "Que no, porque mezclar sustancias es peligroso y exige personal autorizado, y que lo consultarás con un adulto responsable", "Que sí, si es una pila muy pequeña", "Que sí, si se hace lejos de la casa", "Mezclar sustancias sin formación puede causar lesiones y contaminación; el tamaño no cambia el peligro."),
    sc=[
        ("En el tratamiento de minerales solubles: ¿cómo se calcula el metal disuelto?", "Multiplicando los metros cúbicos de solución por la ley en g/L", "El metal disuelto se obtiene con volumen y ley."),
        ("En el tratamiento de minerales solubles: ¿qué es el refino?", "La solución con poco metal que sale de la purificación y vuelve a la pila", "El refino es la solución que ya cedió su metal."),
        ("En un balance de pila: ¿qué se hace si resulta más metal recuperado que disuelto?", "Se revisan los datos y se informa el error", "Es un resultado imposible que muestra un error."),
    ],
    op=("Ficha de ejemplo: una pila de la «Planta Lixiviación Cordón Demo» tiene 4.000 toneladas con ley de 1 %. Se recogen 10.000 m³ de solución rica con 3 g/L, y la purificación y la recuperación obtienen el 80 % del metal disuelto. Escribe (a) los kilos de metal de la pila, (b) los kilos disueltos, (c) la extracción, (d) los kilos de metal sólido, (e) el porcentaje del metal de la pila que se obtiene como metal sólido.",
        "(a) 4.000 × 1 ÷ 100 = 40 toneladas = 40.000 kg. (b) 10.000 × 3 = 30.000 kg. (c) 30.000 ÷ 40.000 × 100 = 75 %. (d) 30.000 × 80 ÷ 100 = 24.000 kg. (e) 24.000 ÷ 40.000 × 100 = 60 %.",
        ["calcula bien el metal de la pila", "calcula bien el metal disuelto", "calcula bien la extracción", "calcula bien el metal sólido", "calcula bien el porcentaje global"],
        ["hoja con las cinco respuestas"],
        ["olvidar pasar las toneladas a kilos", "confundir la base de cada porcentaje", "no calcular el porcentaje global"],
        "Pregunta: «¿con qué cantidad comparas cada resultado?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa una pila y una solución rica y calcula el metal de la pila, el metal disuelto y la extracción.",
    extend="Explica con un ejemplo por qué la extracción y la eficiencia de purificación se calculan con bases distintas.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). «Planta Lixiviación Demo»: un ciclo con 5.000 toneladas de mineral con ley de 2 % (100.000 kilos de metal). Eficiencias de ejemplo: disolución (extracción), 75 %; purificación y recuperación juntas, 80 %. "
     "Consumo registrado de un insumo ficticio «I-1»: 12 kilos por tonelada de mineral; costo de ejemplo del insumo: $500 por kilo. Valor de ejemplo del metal: $5.000 por kilo. Otros costos de operación de ejemplo: $10.000.000 por ciclo.")
build(
    O3, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: encadenar eficiencias, calcular el costo de un insumo por kilo de metal recuperado y el margen de un ciclo, y ver qué pasa si cambia una eficiencia.",
    prior=["Sé calcular extracción y metal recuperado.", "Sé multiplicar y dividir números enteros.", "Sé leer un consumo registrado."],
    explain=[
        "Las eficiencias de las etapas se encadenan: cada etapa trabaja con lo que le dejó la anterior. Si el mineral tiene 100.000 kilos de metal y la extracción es 75 %, se disuelven 75.000 kilos; si después la purificación y la recuperación logran 80 %, se obtienen 60.000 kilos. Un insumo tiene un consumo específico, que aquí es una cifra registrada de kilos de insumo por tonelada de mineral; no es una cantidad que una persona decida agregar, porque eso lo fija el procedimiento aprobado y lo aplica personal autorizado.",
        "El costo de un insumo se calcula multiplicando sus kilos por su precio. El costo por kilo de metal recuperado se obtiene dividiendo ese costo entre los kilos de metal recuperados, y sirve para comparar ciclos. El margen de ejemplo de un ciclo es el valor del metal recuperado menos todos los costos. En un ciclo de ejemplo con 8.000 kilos de metal, un insumo de $4.000.000 y un valor de $2.000 por kilo, el costo del insumo por kilo es $500 y el valor del metal es $16.000.000.",
        f"Estas cifras son de ejemplo; las reales las registran personas autorizadas y cambian con el mineral y el proyecto. Nunca se reduce un insumo por cuenta propia «para ahorrar»: eso afecta la extracción y la seguridad del proceso. {EMER} {AVISO}",
    ],
    vocab=[("eficiencia de una etapa", "porcentaje del metal que recibe la etapa y que pasa a su producto"), ("consumo específico de un insumo", "kilos de insumo registrados por cada tonelada de mineral tratada"), ("costo por kilo de metal recuperado", "costo de un insumo dividido entre los kilos de metal recuperados"), ("margen de ejemplo", "valor del metal recuperado menos los costos del ciclo"), ("etapas encadenadas", "etapas en que cada una trabaja con lo que dejó la anterior")],
    worked=[
        ("Eficiencias encadenadas", "Un mineral de ejemplo tiene 20.000 kilos de metal; la extracción es 50 % y la purificación y recuperación 90 %. ¿Cuántos kilos de metal sólido se obtienen?", ["50 por ciento de 20.000 son 10.000 kilos disueltos.", "90 por ciento de 10.000 son 9.000 kilos."], "9.000 kilos"),
        ("Costo por kilo", "Un insumo de ejemplo cuesta $4.000.000 en un ciclo que recupera 8.000 kilos de metal. ¿Cuánto es el costo del insumo por kilo recuperado?", ["Se divide el costo entre los kilos recuperados.", "4.000.000 dividido por 8.000 es 500."], "$500 por kilo"),
    ],
    mistakes=[("Sumar las eficiencias de las etapas en vez de encadenarlas.", "Cada etapa trabaja con lo que le dejó la anterior, así que se aplica una después de otra.", "Se calcula el resultado de la primera etapa y se aplica la siguiente a ese resultado."),
              ("Creer que el consumo registrado de un insumo es lo que una persona debe agregar.", "La cantidad la fija el procedimiento aprobado y la aplica personal autorizado.", "El registro sirve para controlar y comparar, no para decidir un uso por cuenta propia.")],
    T=[
        ("abc", "En el tratamiento de minerales solubles: ¿qué es la eficiencia de una etapa?", "El porcentaje del metal que recibe la etapa y que pasa a su producto", "Las horas que trabaja la etapa en un día", "El costo de operar la etapa por tonelada", "La eficiencia compara lo que sale con lo que entra a la etapa."),
        ("abc", "En el control de insumos de una planta: ¿qué es el consumo específico de un insumo?", "Los kilos de insumo registrados por cada tonelada de mineral tratada", "La cantidad que cada operador debe agregar según su criterio", "Los kilos de metal recuperados por tonelada", "El consumo específico es una cifra registrada; la cantidad a usar la fija el procedimiento."),
        ("abc", "En el cálculo de un ciclo: ¿por qué se encadenan las eficiencias de las etapas?", "Porque cada etapa trabaja con lo que le dejó la anterior", "Porque la última etapa decide todo", "Porque se suman los porcentajes de cada una", "La salida de una etapa es la entrada de la siguiente."),
        ("=", "{F} ¿Cuántos kilos de metal contiene el mineral del ciclo?", "5000*2*1000//100", "Se multiplican las toneladas por la ley, se divide por 100 y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal se disuelven?", "100000*75//100", "Se aplica la extracción al metal del mineral.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal sólido se obtienen?", "100000*75//100*80//100", "Se aplica la eficiencia de purificación y recuperación al metal disuelto.", " kg"),
        ("=", "{F} ¿Cuántos kilos del insumo «I-1» se registran en el ciclo?", "5000*12", "Se multiplican las toneladas por el consumo específico.", " kg"),
        ("=", "{F} ¿Cuál es el costo del insumo en el ciclo, en pesos?", "5000*12*500", "Se multiplican los kilos del insumo por su precio.", " pesos"),
        ("=", "{F} ¿Cuál es el costo del insumo por kilo de metal recuperado, en pesos?", "5000*12*500//60000", "Se divide el costo del insumo entre los kilos de metal recuperados.", " pesos"),
        ("abc", "{F} Si la extracción bajara y las demás cifras se mantuvieran, ¿qué le pasaría al costo del insumo por kilo recuperado?", "Subiría, porque se gastaría lo mismo en el insumo para recuperar menos metal", "Bajaría, porque se recuperaría menos metal", "No cambiaría, porque el insumo cuesta lo mismo", "El mismo costo se reparte entre menos kilos recuperados."),
        ("=", "{F} ¿Cuál es el margen de ejemplo del ciclo, en pesos?", "60000*5000-5000*12*500-10000000", "Se resta al valor del metal recuperado el costo del insumo y los otros costos.", " pesos"),
        ("abc", "{F} El jefe propone bajar el insumo a la mitad «para ahorrar» sin cambiar nada más. ¿Cuál es la mejor respuesta?", "El consumo lo fija el procedimiento aprobado para ese mineral; recortarlo por cuenta propia puede bajar la extracción y la seguridad", "Es buena idea, porque gastar menos siempre mejora el margen", "Es buena idea, si se avisa después", "Un recorte sin criterio puede dañar la extracción y los controles del proceso."),
        ("=", "{F} Si la extracción fuera 60 % y todo lo demás igual, ¿cuál sería el costo del insumo por kilo de metal recuperado, en pesos?", "5000*12*500//(100000*60//100*80//100)", "Se calculan los kilos recuperados con la nueva extracción y se divide el costo entre ellos.", " pesos"),
    ],
    ctx=("abc", "Una compañera propone usar estos cálculos para decidir cuánto insumo agregar a una pila real, «porque salen exactos». ¿Qué respondes?", "Que los números son de ejemplo y que la cantidad real la fija un procedimiento aprobado aplicado por personal autorizado; lo consultarás con un adulto responsable", "Que sí, si se usa un poco menos", "Que sí, si se anota en el registro", "Un cálculo en papel no reemplaza el procedimiento aprobado ni a personal autorizado."),
    sc=[
        ("En el cálculo de un ciclo de planta: ¿cómo se obtiene el metal sólido a partir de dos eficiencias?", "Se aplica la primera al metal inicial y la segunda al resultado", "Cada etapa trabaja con lo que le dejó la anterior."),
        ("En el control de insumos de planta: ¿cómo se calcula el costo de un insumo?", "Multiplicando sus kilos por su precio por kilo", "El costo es cantidad por precio."),
        ("En un ciclo de planta: ¿qué es el margen de ejemplo?", "El valor del metal recuperado menos los costos del ciclo", "El margen resume lo que queda tras pagar los costos."),
    ],
    op=("Ficha de ejemplo: un ciclo de la «Planta Lixiviación Cordón Demo» tiene 3.000 toneladas con ley de 2 %. Extracción de ejemplo: 80 %; purificación y recuperación: 75 %. Consumo registrado del insumo ficticio «I-2»: 8 kilos por tonelada de mineral, a $300 por kilo. Escribe (a) los kilos de metal del mineral, (b) los kilos de metal sólido, (c) el costo del insumo, (d) el costo del insumo por kilo de metal recuperado, (e) por qué el consumo registrado no es una instrucción de cuánto agregar.",
        "(a) 3.000 × 2 ÷ 100 = 60 toneladas = 60.000 kg. (b) 60.000 × 80 ÷ 100 = 48.000 kg disueltos; 48.000 × 75 ÷ 100 = 36.000 kg de metal sólido. (c) 3.000 × 8 = 24.000 kg de insumo; 24.000 × 300 = 7.200.000 pesos. (d) 7.200.000 ÷ 36.000 = 200 pesos por kilo. (e) Porque es una cifra registrada de lo ocurrido: la cantidad a usar la fija el procedimiento aprobado y la aplica personal autorizado.",
        ["calcula bien el metal del mineral", "encadena las dos eficiencias", "calcula bien el costo del insumo", "calcula bien el costo por kilo", "explica que el consumo registrado no es instrucción"],
        ["hoja con las cinco respuestas"],
        ["sumar las eficiencias", "olvidar los kilos del insumo", "decir que el registro indica cuánto agregar"],
        "Pregunta: «¿sobre qué cantidad aplicas la segunda eficiencia?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Encadena dos eficiencias inventadas sobre un mineral de 40.000 kilos de metal y calcula los kilos de metal sólido.",
    extend="Explica con un ejemplo por qué un recorte de insumo puede subir el costo por kilo recuperado en vez de bajarlo.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (comparación de ejemplo, inventada). La «Planta Lixiviación Demo» compara dos duraciones de ciclo para una pila de 1.000 toneladas con ley de 2 % (20.000 kilos de metal), con purificación y recuperación de 90 % (datos de ejemplo). "
     "Alternativa 1, ciclo de 60 días con extracción de 70 %; alternativa 2, ciclo de 80 días con extracción de 80 %. Valor de ejemplo del metal: $5.000 por kilo; costo de operación de ejemplo: $900.000 por día de ciclo. "
     "El programa de producción exige una extracción mínima de 65 %. Balance de una prueba del ciclo largo: se disolvieron 16.000 kilos de metal, se recuperaron 14.400 kilos y las pérdidas registradas en la purificación fueron 1.500 kilos; se acepta una diferencia de hasta 2 % del metal disuelto (criterio de ejemplo).")
build(
    O3, 5, F,
    use="Aprenderé a comparar dos duraciones de ciclo con un criterio mínimo, a calcular el margen y el margen por día, y a verificar el balance de metal antes de recomendar.",
    prior=["Sé calcular extracción, metal recuperado y margen.", "Sé comparar un dato con un criterio.", "Sé multiplicar y restar números enteros."],
    explain=[
        "Un ciclo más largo suele recuperar más metal, pero también cuesta más días de operación. Por eso no basta mirar los kilos recuperados: se compara el margen del ciclo, que es el valor del metal recuperado menos el costo de operar todos sus días, y el margen por día, que es el margen dividido por la duración. Antes de comparar se revisa el criterio mínimo del programa de producción, porque una alternativa que no lo cumple no puede elegirse.",
        "Verificar la calidad de los datos también importa. En un balance de metal, lo disuelto debe ser igual a lo recuperado más las pérdidas registradas; la diferencia se compara con el máximo aceptado. Si la diferencia supera el máximo, se busca la causa y se informa; no se corrige un número para que cuadre. Ejemplo: se disolvieron 5.000 kilos, se recuperaron 4.000 y se registraron 900 de pérdidas; la diferencia es 100 kilos, que es el 2 % de 5.000.",
        f"La recomendación cita el criterio que decide, las cifras y lo que se acepta ceder. Las cifras son de ejemplo y la decisión sobre un ciclo real la toma personal autorizado. {EMER} {AVISO}",
    ],
    vocab=[("margen por día", "margen del ciclo dividido por su duración en días"), ("criterio mínimo", "valor que una alternativa debe alcanzar para poder elegirse"), ("pérdidas registradas", "metal que se anota como perdido en una etapa"), ("diferencia aceptable", "máximo de diferencia permitido en un balance"), ("recomendación", "propuesta escrita con la alternativa elegida y sus razones")],
    worked=[
        ("Margen por día", "Un ciclo de ejemplo de 50 días deja un margen de $10.000.000. ¿Cuál es el margen por día?", ["Se divide el margen entre los días.", "10.000.000 dividido por 50 es 200.000."], "$200.000 por día"),
        ("Verificar el balance", "Se disolvieron 5.000 kilos, se recuperaron 4.000 y se registraron 900 de pérdidas. Se acepta hasta 3 %. ¿Es aceptable?", ["La diferencia es 5.000 menos 4.900, es decir 100 kilos.", "El 3 % de 5.000 es 150, y 100 es menor."], "Sí, es aceptable"),
    ],
    mistakes=[("Elegir el ciclo que recupera más kilos sin mirar los días que cuesta.", "Más días de operación suben el costo y pueden dejar un margen menor.", "Se compara el margen y el margen por día."),
              ("Ajustar las pérdidas registradas para que el balance cuadre.", "Un balance forzado oculta pérdidas reales.", "Se anota la diferencia real, se busca la causa y se informa.")],
    T=[
        ("abc", "En la comparación de ciclos: ¿qué es el margen de ejemplo de un ciclo?", "El valor del metal recuperado menos el costo de operar el ciclo", "Los kilos de metal recuperados en el ciclo", "La duración del ciclo en días", "El margen resume lo que queda después de pagar los costos del ciclo."),
        ("abc", "En la comparación de ciclos: ¿por qué conviene mirar el margen por día y no solo los kilos recuperados?", "Porque un ciclo más largo recupera más kilos, pero también cuesta más días de operación", "Porque los kilos recuperados no importan", "Porque el ciclo corto siempre gana", "Los kilos y los días se miran juntos para comparar ciclos de distinta duración."),
        ("abc", "En un balance de planta: ¿qué significa verificar el balance de metal?", "Comprobar que lo disuelto sea igual a lo recuperado más las pérdidas, dentro de lo aceptado", "Repetir la medición hasta que dé lo esperado", "Sumar el caudal de cada día de la semana", "Verificar es comparar entradas y salidas con el máximo aceptado."),
        ("=", "{F} ¿Cuántos kilos de metal se disuelven en la alternativa 1?", "20000*70//100", "Se aplica la extracción al metal de la pila.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal sólido se obtienen en la alternativa 1?", "20000*70//100*90//100", "Se aplica la eficiencia de purificación y recuperación al metal disuelto.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal sólido se obtienen en la alternativa 2?", "20000*80//100*90//100", "Se aplica la extracción y luego la eficiencia de purificación y recuperación.", " kg"),
        ("=", "{F} ¿Cuál es el costo de operación de la alternativa 1, en pesos?", "60*900000", "Se multiplican los días del ciclo por el costo diario.", " pesos"),
        ("=", "{F} ¿Cuál es el margen de la alternativa 1, en pesos?", "12600*5000-60*900000", "Se resta el costo de operación al valor del metal recuperado.", " pesos"),
        ("=", "{F} ¿Cuál es el margen de la alternativa 2, en pesos?", "14400*5000-80*900000", "Se resta el costo de operación al valor del metal recuperado.", " pesos"),
        ("abc", "{F} Según el margen y el criterio mínimo de extracción, ¿qué alternativa conviene?", "La alternativa 1, porque cumple el 65 % y tiene mayor margen", "La alternativa 2, porque recupera más kilos de metal", "Ninguna, porque las dos tienen margen igual", "Ambas cumplen el 65 %, y la alternativa 1 deja mayor margen que la 2."),
        ("=", "{F} ¿Cuál es el margen por día de la alternativa 1, en pesos?", "(12600*5000-60*900000)//60", "Se divide el margen del ciclo entre sus días.", " pesos"),
        ("abc", "{F} Un compañero propone mantener 80 días porque «más kilos siempre es mejor». ¿Cuál es la mejor objeción?", "Más kilos cuestan más días de operación, y el margen de 80 días no supera al de 60", "Ninguna, porque los kilos son lo único que importa", "Que el ciclo largo incumple la extracción mínima", "Se comparan los kilos y los días: el ciclo largo recupera más, pero no mejora el margen."),
        ("abc", "{F} Con el balance de la prueba del ciclo largo, ¿cuál es la conclusión correcta?", "Es aceptable: la diferencia es 100 kilos y el 2 % de 16.000 es 320 kilos", "No es aceptable, porque existe una diferencia", "No es aceptable, porque 100 supera 2", "16.000 menos 14.400 menos 1.500 es 100; ese valor está bajo el máximo de 320."),
    ],
    ctx=("abc", "Un compañero propone omitir el balance de la prueba «porque el ciclo largo siempre da buenos resultados». ¿Qué respondes?", "Que el balance se hace siempre y se registra, y que lo consultarás con un adulto responsable", "Que sí, porque ya dio bien otras veces", "Que sí, si no hay tiempo", "Verificar el balance es lo que detecta los errores de cada ciclo."),
    sc=[
        ("En la comparación de ciclos de planta: ¿qué se revisa antes de comparar el margen?", "El criterio mínimo del programa de producción", "Una alternativa que no lo cumple no puede elegirse."),
        ("En la comparación de ciclos: ¿cómo se calcula el margen por día?", "Dividiendo el margen del ciclo entre sus días", "El margen por día permite comparar ciclos de distinta duración."),
        ("En un balance de metal con diferencia mayor a la aceptada: ¿qué se hace?", "Se busca la causa y se informa, sin corregir el número", "Un balance forzado oculta pérdidas reales."),
    ],
    op=("Ficha de ejemplo: una pila de la «Planta Lixiviación Cordón Demo» tiene 1.000 toneladas con ley de 3 % (30.000 kilos de metal), con purificación y recuperación de 80 %. Alternativa X: ciclo de 40 días con extracción de 60 %; alternativa Y: ciclo de 50 días con extracción de 75 %. Valor de ejemplo: $4.000 por kilo; costo de operación: $1.000.000 por día. Criterio mínimo de extracción: 55 %. Escribe (a) los kilos de metal sólido de X y de Y, (b) si ambas cumplen el criterio, (c) el margen de cada una, (d) cuál conviene y por qué.",
        "(a) X: 30.000 × 60 ÷ 100 = 18.000; × 80 ÷ 100 = 14.400 kg. Y: 30.000 × 75 ÷ 100 = 22.500; × 80 ÷ 100 = 18.000 kg. (b) Sí: 60 % y 75 % superan el 55 %. (c) X: 14.400 × 4.000 − 40 × 1.000.000 = 57.600.000 − 40.000.000 = 17.600.000 pesos. Y: 18.000 × 4.000 − 50 × 1.000.000 = 72.000.000 − 50.000.000 = 22.000.000 pesos. (d) Conviene Y: cumple el criterio y tiene mayor margen, aceptando un ciclo 10 días más largo.",
        ["calcula bien los kilos de metal sólido", "revisa el criterio mínimo", "calcula bien los márgenes", "recomienda con criterio y costo aceptado"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el costo diario", "no encadenar las eficiencias", "recomendar sin citar el criterio"],
        "Pregunta: «¿qué cuesta más en la alternativa que dura más días?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Compara dos ciclos inventados de distinta duración con un criterio mínimo, calcula el margen de cada uno y escribe una recomendación de dos líneas.",
    extend="Explica con un ejemplo por qué un ciclo más largo puede dejar menos margen aunque recupere más metal.",
)

# ============================================================ OAE-04, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Fundición Demo» de la empresa ficticia «Minera Demo» recibe 100 toneladas de concentrado al día, con ley de 30 %. Al fundirlo obtiene metal y escoria, y los gases y el polvo pasan por un sistema de captación. "
     "En el proceso se recupera el 90 % del metal que entra, que luego se enfría y forma lingotes de 500 kilos cada uno (datos de ejemplo). Peligros anotados: altas temperaturas en el área de hornos, contacto de metal fundido con humedad, gases y polvo, ruido, y un camino interno por donde circulan vehículos y grúas.")
build(
    O4, 1, F,
    use="Aprenderé qué son la fundición, la tostación y la refinación, qué es un lingote, qué peligros tiene una fundición y por qué esta tarea exige personal autorizado, zonas controladas y norma vigente.",
    prior=["Sé qué son el concentrado, la ley y la recuperación.", "Sé calcular el metal contenido con una ley.", "Sé la jerarquía de controles."],
    explain=[
        "La fundición es la etapa en que el material se calienta hasta fundirse, de modo que el metal se separe de la escoria, que es el material no metálico. Antes puede haber una tostación, que es un calentamiento del mineral para cambiar su composición química y dejarlo apto para la etapa siguiente; el sólido que resulta se llama calcina. Después puede haber una refinación, que purifica el metal para cumplir la calidad que exige el cliente. El producto final suele ser un lingote, un bloque de metal con forma y masa definidas que se obtiene al solidificar el metal.",
        "Los cálculos son de planilla. El metal contenido en un concentrado es toneladas por ley dividido por 100. Si se recupera cierto porcentaje, el metal de lingotes es ese porcentaje del contenido. Con un concentrado de ejemplo de 40 toneladas y ley de 25 %, hay 10 toneladas de metal, es decir 10.000 kilos, que en lingotes de 250 kilos son 40 lingotes si se aprovecha todo.",
        f"Una fundición tiene peligros de gravedad: altas temperaturas, metal fundido, gases, polvo y ruido. Además, el agua, la humedad o materiales extraños pueden provocar reacciones violentas con material fundido. Por eso las áreas son restringidas, se usa EPP especial, hay permisos de trabajo y solo personal autorizado interviene los equipos; este cuaderno no enseña esas tareas. Los gases y polvos se captan para proteger a las personas y al ambiente, según la norma vigente de las autoridades minera y sanitaria. {EMER} {AVISO}",
    ],
    vocab=[("fundición", "etapa en que el material se calienta hasta fundirse para separar el metal de la escoria"), ("escoria", "material no metálico que se separa del metal en la fundición"), ("tostación", "calentamiento del mineral para cambiar su composición química"), ("calcina", "producto sólido de la tostación"), ("refinación", "purificación del metal para cumplir la calidad exigida"), ("lingote", "bloque de metal con forma y masa definidas, obtenido al solidificar el metal"), ("sistema de captación", "conjunto de equipos que recoge gases y polvo para controlar su salida al ambiente")],
    worked=[
        ("Metal en lingotes", "Un concentrado de ejemplo de 40 toneladas tiene ley de 25 %. ¿Cuántos kilos de metal contiene y cuántos lingotes de 250 kilos serían?", ["40 por 25 dividido por 100 es 10 toneladas, o sea 10.000 kilos.", "10.000 dividido por 250 es 40 lingotes."], "10.000 kilos; 40 lingotes"),
        ("Clasificar una etapa", "En una planta de ejemplo se calienta un mineral solo para cambiar su composición química antes de otra etapa. ¿Cómo se llama?", ["No se busca separar metal y escoria, sino cambiar la composición.", "Esa etapa es la tostación."], "Tostación"),
    ],
    mistakes=[("Creer que el agua sirve para enfriar o apagar cualquier superficie caliente en una fundición.", "El agua y la humedad pueden reaccionar de forma violenta con material fundido.", "Las zonas con material fundido se controlan por personal autorizado, con medidas que fija el procedimiento."),
              ("Creer que leer sobre fundición habilita para trabajar cerca de un horno.", "Las áreas de fundición son restringidas y exigen instructor autorizado, EPP especial y norma vigente.", "Aprende aquí el concepto y deja el trabajo a personal autorizado.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es la fundición?", "La etapa en que el material se calienta hasta fundirse para separar el metal de la escoria", "La etapa en que se reduce el tamaño de las rocas", "La etapa en que se mide la ley de un mineral", "La fundición separa metal y escoria por calor; achicar y medir son otras tareas."),
        ("abc", "En una fundición: ¿qué es la escoria?", "El material no metálico que se separa del metal", "El metal puro en bloques", "El gas que sale por el sistema de captación", "La escoria es la parte no metálica; el metal en bloques es el lingote."),
        ("abc", "En una fundición: ¿qué es un lingote?", "Un bloque de metal con forma y masa definidas, obtenido al solidificar el metal", "El sistema que capta gases y polvo", "La hoja de datos de seguridad de una sustancia", "El lingote es el producto sólido; el sistema de captación y la HDS son otra cosa."),
        ("=", "{F} ¿Cuántas toneladas de metal contiene el concentrado que recibe la fundición cada día?", "100*30//100", "Se multiplican las toneladas por la ley y se divide por 100.", " toneladas de metal"),
        ("=", "{F} ¿Cuántas toneladas de metal se recuperan cada día?", "100*30//100*90//100", "Se aplica el 90 % de recuperación al metal contenido.", " toneladas de metal"),
        ("=", "{F} ¿Cuántos lingotes de 500 kilos salen cada día?", "27*1000//500", "Se pasan las toneladas a kilos y se dividen entre la masa de un lingote.", " lingotes"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al contacto de metal fundido con humedad?", "Una reacción violenta con proyección de material", "Que baje la ley del concentrado", "Que aumente la cantidad de escoria", "El riesgo es un daño a las personas; la ley o la escoria no son un daño directo."),
        ("abc", "{F} Que los gases y el polvo pasen por un sistema de captación es un control de tipo:", "De ingeniería, porque un equipo reduce la emisión al ambiente y la exposición", "De EPP, porque protege el cuerpo de cada persona", "Administrativo, porque solo informa de la emisión", "Un equipo que recoge gases y polvo actúa sobre el peligro; no es un equipo personal ni una señal."),
        ("abc", "{F} Una estudiante dice: «ya sé qué es fundir, así que puedo ayudar en el área de hornos». ¿Qué respuesta es correcta?", "Es falso: el área es restringida y exige instructor autorizado, EPP especial y norma vigente", "Es cierto, si usa ropa gruesa", "Es cierto, si va acompañada de un compañero", "La ropa o la compañía no reemplazan la formación ni la autorización."),
        ("=", "{F} ¿Cuántas toneladas del metal que entra no se recuperan en lingotes cada día?", "100*30//100-100*30//100*90//100", "Se resta el metal recuperado al metal que entra.", " toneladas de metal"),
        ("abc", "{F} Durante una visita de ejemplo, ves una salpicadura de metal fundido y una persona queda en el suelo. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte a sacar a la persona de inmediato", "Echar agua sobre el metal para enfriarlo", "Acercarse sin formación o echar agua puede agravar el accidente; se avisa a quienes pueden actuar."),
        ("abc", "{F} El jefe dice que un casco y un delantal bastan para entrar al área de hornos. ¿Cuál es la mejor objeción?", "El EPP es la última barrera: el área es restringida y se entra con autorización, EPP especial y norma vigente", "Ninguna, porque el casco elimina el peligro", "Que el casco solo se usa en el camino interno", "El EPP no quita el peligro; el acceso lo controlan la autorización y las barreras."),
        ("=", "{F} Si la recuperación bajara a 80 %, ¿cuántos lingotes de 500 kilos saldrían cada día?", "100*30//100*80//100*1000//500", "Se aplica la nueva recuperación al metal contenido y se divide entre la masa de un lingote.", " lingotes"),
    ],
    ctx=("abc", "Un conocido tiene un hornito casero para fundir metales y te pide ayuda «porque ya estudiaste fundición». ¿Qué respondes?", "Que no, porque trabajar con calor y metal fundido exige instructor autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si trabajas con guantes gruesos", "Que sí, si es un horno pequeño", "Haber estudiado el concepto no habilita para fundir metales; el tamaño o los guantes no cambian el riesgo."),
    sc=[
        ("En Metalurgia Extractiva: ¿qué es la tostación?", "El calentamiento del mineral para cambiar su composición química", "La tostación cambia la composición del mineral antes de otra etapa."),
        ("En una fundición: ¿qué es la refinación?", "La purificación del metal para cumplir la calidad exigida", "La refinación mejora la pureza del metal."),
        ("En una fundición: ¿qué hace una persona que ve un accidente en el área de hornos?", "No se acerca a la zona de riesgo, avisa a un adulto responsable y a emergencias", "Acercarse sin formación puede causar otro accidente."),
    ],
    op=("Ficha de ejemplo: la «Fundición Cordón Demo» recibe 80 toneladas de concentrado con ley de 25 %, recupera el 90 % del metal y forma lingotes de 600 kilos. Hay un área de hornos con metal fundido y humedad en el piso. Escribe (a) cuántas toneladas de metal contiene el concentrado, (b) cuántas se recuperan, (c) cuántos lingotes salen, (d) un peligro del área y su riesgo, (e) un control de ingeniería y uno administrativo, (f) qué hace una persona que ve una salpicadura y a alguien herido.",
        "(a) 80 × 25 ÷ 100 = 20 toneladas. (b) 20 × 90 ÷ 100 = 18 toneladas. (c) 18.000 ÷ 600 = 30 lingotes. (d) Peligro: metal fundido con humedad en el piso; riesgo: reacción violenta con proyección de material que lesione a personas. (e) Ingeniería: un sistema que mantenga seco y controlado el piso del área; administrativo: acceso restringido con permiso de trabajo y señales. (f) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien el metal contenido", "calcula bien el metal recuperado", "calcula bien los lingotes", "distingue peligro y riesgo", "propone los dos controles", "indica no acercarse y avisar"],
        ["hoja con las seis respuestas"],
        ["olvidar pasar toneladas a kilos", "proponer solo EPP", "responder que se acerca o echa agua"],
        "Pregunta: «¿qué barrera o regla impide que alguien entre sin autorización?». Si no responde, pídele que relea el tercer párrafo."),
    reinforce="Escribe en orden la tostación, la fundición y la refinación con una frase para cada una, y calcula los lingotes de un caso inventado.",
    extend="Explica con un ejemplo por qué el EPP no basta para trabajar en un área con metal fundido.",
)

# ============================================================ OAE-04, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Fundición Demo». Documentos: el registro de producción por lote (número de lote, cantidad de lingotes y masa de cada uno), el certificado de calidad del lote (pureza medida por el laboratorio), "
     "el rotulado de trazabilidad (código de lote en cada lingote), el permiso de trabajo en caliente (autorización escrita previa a tareas con calor, con condiciones y responsables) y el informe de emisiones (registro de los gases y polvos que salen de la planta). "
     "Registro de la semana (ejemplo): lote 21, 20 lingotes de 500 kilos, pureza 99 %; lote 22, 18 lingotes de 500 kilos, pureza 98 %; lote 23, 22 lingotes de 500 kilos, pureza 99 %. Pureza mínima exigida por el cliente (ejemplo): 99 %. "
     "Roles: operador de fundición, supervisor, laboratorista, prevencionista de riesgos, encargado ambiental y encargado de despacho.")
build(
    O4, 2, F,
    use="Aprenderé los documentos de una fundición (registro de producción, certificado de calidad, rotulado de trazabilidad, permiso de trabajo en caliente e informe de emisiones), los roles y cómo se calculan las masas de los lotes.",
    prior=["Sé qué son fundición, escoria y lingote.", "Sé leer un registro escrito.", "Sé multiplicar y sumar números enteros."],
    explain=[
        "Una fundición documenta cada lote. El registro de producción anota el número de lote, cuántos lingotes salieron y cuánto pesa cada uno. El certificado de calidad indica la pureza medida por el laboratorio; la pureza es el porcentaje de metal puro que tiene el lingote. El rotulado de trazabilidad pone en cada lingote un código de lote, para poder seguir su origen y su recorrido. El informe de emisiones registra los gases y polvos que salen de la planta, porque las autoridades fiscalizan su control según la norma vigente.",
        "El permiso de trabajo en caliente es una autorización escrita, previa a una tarea que usa calor, que fija condiciones y responsables; cada firma certifica una comprobación hecha por quien firma. La masa de un lote es la cantidad de lingotes por la masa de cada uno: 12 lingotes de 400 kilos pesan 4.800 kilos. Un lote que no alcanza la pureza mínima exigida no se despacha como si cumpliera: se retiene, se informa y se decide con la jefatura; el certificado no se cambia.",
        f"Roles: el operador de fundición trabaja con autorización, el supervisor decide, el laboratorista mide la pureza, el prevencionista asesora, el encargado ambiental vigila las emisiones y el encargado de despacho entrega los lotes que cumplen. {EMER} {AVISO}",
    ],
    vocab=[("registro de producción por lote", "anotación del número de lote, la cantidad de lingotes y la masa de cada uno"), ("certificado de calidad", "documento con la pureza medida por el laboratorio"), ("pureza", "porcentaje de metal puro que tiene un lingote"), ("trazabilidad", "posibilidad de seguir el origen y el recorrido de un lote mediante códigos y registros"), ("permiso de trabajo en caliente", "autorización escrita previa a una tarea con calor, con condiciones y responsables"), ("informe de emisiones", "registro de los gases y polvos que salen de la planta")],
    worked=[
        ("Masa de un lote", "Un lote de ejemplo tiene 12 lingotes de 400 kilos cada uno. ¿Cuántos kilos pesa?", ["Se multiplica la cantidad de lingotes por la masa de cada uno.", "12 por 400 es 4.800."], "4.800 kilos"),
        ("Cumple o no cumple", "Un cliente de ejemplo exige pureza mínima de 97 % y un certificado informa 96 %. ¿Cumple?", ["96 es menor que 97.", "No cumple: se retiene el lote y se informa."], "No cumple"),
    ],
    mistakes=[("Rotular los lingotes de un lote con el código de otro para despacharlos juntos.", "Se pierde la trazabilidad: ya no se sabe de qué lote vienen ni qué pureza tienen.", "Cada lingote lleva el código de su propio lote."),
              ("Cambiar la pureza de un certificado para poder despachar el lote.", "Es un registro falso y puede enviar al cliente un producto que no cumple.", "Se retiene el lote, se informa y la jefatura decide.")],
    T=[
        ("abc", "En una fundición: ¿qué es el certificado de calidad de un lote?", "El documento con la pureza medida por el laboratorio", "El registro de las horas que trabajó el horno", "El plano del área de hornos", "El certificado informa la calidad medida; las horas y el plano son otros documentos."),
        ("abc", "En una fundición: ¿qué es la trazabilidad?", "Poder seguir el origen y el recorrido de un lote mediante códigos y registros", "Poder mover los lingotes más rápido", "Pesar cada lingote dos veces", "La trazabilidad se apoya en códigos y registros; no se trata de rapidez ni de pesar."),
        ("abc", "En una fundición: ¿qué es un permiso de trabajo en caliente?", "Una autorización escrita previa a una tarea con calor, con condiciones y responsables", "Una pauta que se llena al final del turno", "El certificado de pureza de un lote", "El permiso se emite antes de la tarea; no es una pauta de cierre ni un certificado."),
        ("=", "{F} ¿Cuántos kilos pesa el lote 21?", "20*500", "Se multiplica la cantidad de lingotes por la masa de cada uno.", " kg"),
        ("=", "{F} ¿Cuántos kilos pesan juntos los tres lotes de la semana?", "(20+18+22)*500", "Se suman los lingotes y se multiplican por la masa de cada uno.", " kg"),
        ("abc", "{F} ¿Qué lote no cumple la pureza mínima del cliente?", "El lote 22, con 98 %", "El lote 21, porque tiene menos lingotes que el 23", "El lote 23, porque tiene más lingotes", "Solo el lote 22 queda bajo el 99 % exigido."),
        ("abc", "{F} ¿Qué corresponde hacer con el lote 22?", "Retenerlo, informar al supervisor y esperar la decisión de la jefatura, sin cambiar el certificado", "Despacharlo, porque 98 % es casi 99 %", "Cambiar el 98 por 99 para poder despacharlo", "Un lote que no cumple se retiene e informa; alterar el certificado sería un registro falso."),
        ("=", "{F} ¿Cuántos kilos pesa el lote 22?", "18*500", "Se multiplica la cantidad de lingotes por la masa de cada uno.", " kg"),
        ("abc", "{F} ¿Quién mide la pureza de un lote?", "El laboratorista", "El encargado de despacho", "El prevencionista de riesgos", "La pureza se mide en el laboratorio; despacho entrega y el prevencionista asesora."),
        ("=", "{F} ¿Cuántos kilos hay en los lotes que cumplen la pureza?", "(20+22)*500", "Se suman los lingotes de los lotes que cumplen y se multiplican por la masa de cada uno.", " kg"),
        ("abc", "{F} Un compañero propone rotular los lingotes del lote 22 con el código del lote 21 para despacharlos juntos. ¿Cuál es la mejor respuesta?", "No se hace: se pierde la trazabilidad y se despacharía un lote que no cumple", "Se puede, si el cliente no revisa los códigos", "Se puede, si se informa después del despacho", "El código identifica de qué lote viene cada lingote; cambiarlo oculta el origen."),
        ("=", "{F} El pesaje de despacho de los tres lotes informa 29.500 kilos. ¿Cuántos kilos de diferencia hay con el registro de producción?", "(20+18+22)*500-29500", "Se resta el pesaje de despacho a la masa registrada.", " kg"),
        ("abc", "{F} Se acepta una diferencia de hasta 2 % de la masa registrada (criterio de ejemplo). ¿Qué conclusión es correcta?", "Es aceptable: 500 kg es menor que el 2 % de 30.000 kg, que son 600 kg; igual se registra y se busca la causa", "No es aceptable: falta un lingote entero y la diferencia debe ser cero", "Es aceptable y no hace falta registrar nada", "El máximo aceptado es 600 kg; la diferencia es 500 kg y se anota para explicarla."),
    ],
    ctx=("abc", "Un compañero de práctica te pide que firmes un certificado de calidad en blanco «para adelantar el despacho». ¿Qué respondes?", "Que no, porque firmar sin comprobar es un registro falso, y que lo consultarás con un adulto responsable", "Que sí, si el lote parece bueno", "Que sí, si lo completa él después", "Una firma certifica una comprobación; firmar en blanco engaña a quien recibe el lote."),
    sc=[
        ("En una fundición: ¿cómo se calcula la masa de un lote?", "Multiplicando la cantidad de lingotes por la masa de cada uno", "La masa del lote es cantidad por masa unitaria."),
        ("En una fundición: ¿qué es la pureza de un lingote?", "El porcentaje de metal puro que tiene", "La pureza mide cuánto del lingote es metal puro."),
        ("En una fundición: ¿qué se hace con un lote que no alcanza la pureza mínima?", "Se retiene, se informa y decide la jefatura", "Un lote que no cumple no se despacha como si cumpliera."),
    ],
    op=("Ficha de ejemplo: «Fundición Cordón Demo». Lote 8: 16 lingotes de 400 kilos, pureza 99 %. Lote 9: 14 lingotes de 400 kilos, pureza 97 %. Pureza mínima exigida por el cliente (ejemplo): 98 %. Escribe (a) los kilos de cada lote, (b) qué lote cumple, (c) qué haces con el que no cumple, (d) qué documento autoriza una tarea con calor y cuándo se emite.",
        "(a) Lote 8: 16 × 400 = 6.400 kg; lote 9: 14 × 400 = 5.600 kg. (b) El lote 8, con 99 %; el lote 9, con 97 %, queda bajo el 98 %. (c) Retenerlo, informar al supervisor y esperar la decisión de la jefatura, sin cambiar el certificado. (d) El permiso de trabajo en caliente, que se emite antes de la tarea con condiciones y responsables.",
        ["calcula bien los kilos de cada lote", "identifica el lote que cumple", "retiene e informa sin alterar el certificado", "nombra el permiso de trabajo en caliente y que es previo"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar mal los lingotes por los kilos", "decir que se despacha porque 97 es casi 98", "decir que el permiso se llena al terminar"],
        "Pregunta: «¿qué pureza exige el cliente y cuál tiene cada lote?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un registro de producción de dos lotes con lingotes, masas y purezas, y calcula los kilos de cada uno.",
    extend="Explica con un ejemplo por qué la trazabilidad sirve ante un reclamo de un cliente.",
)

# ============================================================ OAE-04, clase 3
F = ("Ficha 3 (balance de ejemplo, inventado). «Fundición Demo», un lote de ejemplo. Tostación: entran 100 toneladas de concentrado y salen 80 toneladas de calcina; la diferencia sale como gases que van al sistema de captación. "
     "Fundición: la calcina tiene 30 % de metal; se obtienen lingotes con 21.600 kilos de metal, 2.000 kilos de metal quedan en la escoria y 300 kilos en el polvo captado. Se acepta una diferencia de hasta 1 % del metal que entra a la fundición (criterio de ejemplo).")
build(
    O4, 3, F,
    use="Aprenderé a analizar el balance de una tostación y una fundición en papel: calcular la masa que sale como gases, el metal que entra y sale, la recuperación y si la diferencia es aceptable.",
    prior=["Sé qué son tostación, fundición, escoria y lingote.", "Sé calcular el metal contenido con una ley.", "Sé calcular un porcentaje con números enteros."],
    explain=[
        "El balance de masa de una tostación compara lo que entra con lo que sale. Al calentar el concentrado, una parte sale como gases que se captan, así que la calcina pesa menos que el concentrado de partida: la diferencia de toneladas es la masa que salió como gases. En una tostación de ejemplo, 50 toneladas de concentrado dan 42 de calcina, y 8 toneladas salieron como gases.",
        "El balance de metal de la fundición sigue el metal. Entra el metal de la calcina (toneladas por ley, pasadas a kilos) y sale en tres lugares: los lingotes, la escoria y el polvo captado. Si la suma de salidas registradas es menor que lo que entró, hay una diferencia; se compara con el máximo aceptado. La recuperación de la fundición es el metal de los lingotes dividido por el metal que entró y multiplicado por 100. Un ejemplo: entran 10.000 kilos, los lingotes tienen 9.000, la escoria 800 y el polvo 100; la diferencia es 100 kilos y la recuperación es 90 %.",
        f"Si la diferencia supera lo aceptado, se busca la causa y se informa; no se cambia ninguna cifra para que cuadre. El polvo y los gases se captan porque dañan a las personas y al ambiente y se fiscalizan según la norma vigente. {EMER} {AVISO}",
    ],
    vocab=[("balance de masa", "comparación entre lo que entra y lo que sale de una etapa"), ("calcina", "producto sólido de la tostación"), ("metal en la escoria", "metal que no se recuperó en el lingote y quedó en el material no metálico"), ("polvo captado", "polvo recogido por el sistema de captación"), ("recuperación de la fundición", "metal de los lingotes dividido por el metal que entra, en porcentaje"), ("diferencia sin explicar", "parte del metal que entra y no aparece en ninguna salida registrada")],
    worked=[
        ("Masa que sale como gases", "Una tostación de ejemplo recibe 50 toneladas de concentrado y entrega 42 toneladas de calcina. ¿Cuántas toneladas salieron como gases?", ["Se resta la calcina al concentrado.", "50 menos 42 son 8."], "8 toneladas"),
        ("Recuperación de la fundición", "Entran 10.000 kilos de metal y los lingotes tienen 9.000. ¿Cuál es la recuperación?", ["Se divide 9.000 entre 10.000.", "Multiplicado por 100 da 90 por ciento."], "90 %"),
    ],
    mistakes=[("Creer que la calcina pesa lo mismo que el concentrado de partida.", "Una parte sale como gases, y por eso la masa sólida disminuye.", "La diferencia de masa entre el concentrado y la calcina es lo que salió como gases."),
              ("Ajustar el metal de la escoria para que el balance cuadre.", "Un balance forzado oculta pérdidas reales.", "Se anota la diferencia real, se busca la causa y se informa.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es la tostación?", "Un calentamiento del mineral para cambiar su composición química antes de otra etapa", "Una separación de partículas según su tamaño", "Una disolución del metal en una solución", "La tostación cambia la composición con calor; separar por tamaño o disolver son otros procesos."),
        ("abc", "En una fundición: ¿qué es la refinación?", "La purificación del metal para cumplir la calidad exigida", "La reducción del tamaño de los trozos de roca", "La captación de gases y polvo", "La refinación sube la pureza del metal; reducir tamaño o captar gases es otra tarea."),
        ("abc", "En una tostación: ¿qué es la calcina?", "El producto sólido que resulta de la tostación", "El metal puro listo para venderse", "El gas que se capta", "La calcina es el sólido de la tostación; el metal puro es el producto de otras etapas."),
        ("=", "{F} ¿Cuántas toneladas salen como gases en la tostación?", "100-80", "Se resta la calcina al concentrado.", " toneladas"),
        ("=", "{F} ¿Cuántos kilos de metal contiene la calcina?", "80*30*1000//100", "Se multiplican las toneladas por la ley, se divide por 100 y se pasa a kilos.", " kg"),
        ("=", "{F} ¿Cuál es la recuperación de la fundición, en porcentaje?", "21600*100//24000", "Se divide el metal de los lingotes por el metal que entra y se multiplica por 100.", " %"),
        ("=", "{F} ¿Cuántos kilos de metal suman las salidas registradas (lingotes, escoria y polvo)?", "21600+2000+300", "Se suman los kilos de metal de las tres salidas.", " kg"),
        ("=", "{F} ¿Cuántos kilos de metal entraron y no aparecen en ninguna salida registrada?", "24000-(21600+2000+300)", "Se resta la suma de las salidas al metal que entró.", " kg"),
        ("abc", "{F} ¿Es aceptable esa diferencia?", "Sí, porque 100 kg es menor que el 1 % de 24.000 kg, que son 240 kg", "No, porque existe una diferencia y debería ser cero", "No, porque 100 supera 1", "El máximo es 240 kg; comparar kilos con un porcentaje sería un error."),
        ("abc", "{F} Los 2.000 kilos de metal que quedan en la escoria representan:", "Metal que no se recuperó en los lingotes", "Metal que se recuperó y está en el lingote", "Ganga que se separó bien", "Si el metal está en la escoria, no llegó al lingote."),
        ("abc", "{F} ¿Por qué importa captar el polvo y los gases?", "Porque dañan a las personas y al ambiente y su control se fiscaliza según la norma vigente", "Porque aumentan la ley del concentrado", "Porque reducen el tamaño de la calcina", "El control de emisiones protege a las personas y al ambiente."),
        ("=", "{F} Si la escoria hubiera contenido solo 1.500 kilos de metal, con los lingotes y el polvo iguales, ¿cuántos kilos quedarían sin explicar?", "24000-(21600+1500+300)", "Se resta la suma de las salidas al metal que entró.", " kg"),
        ("abc", "{F} Con 600 kilos sin explicar y un máximo aceptado de 240 kilos, ¿qué corresponde?", "Buscar la causa, informar al supervisor y no cambiar ninguna cifra", "Aumentar el metal de la escoria en 600 kilos para que cuadre", "Aceptarlo, porque son pocos kilos frente a 24.000", "Una diferencia mayor que el máximo se investiga y se informa; forzar el balance la oculta."),
    ],
    ctx=("abc", "Un compañero propone anotar un metal de escoria distinto para que el balance «cuadre antes de la revisión». ¿Qué respondes?", "Que no, porque un balance forzado oculta el problema, y que lo consultarás con un adulto responsable", "Que sí, si son pocos kilos", "Que sí, si lo corriges después", "Alterar un dato quita la base para detectar y corregir pérdidas reales."),
    sc=[
        ("En una tostación: ¿cómo se calcula la masa que salió como gases?", "Restando la masa de calcina a la masa de concentrado", "La masa que falta salió como gases."),
        ("En una fundición: ¿cómo se calcula la recuperación?", "Dividiendo el metal de los lingotes entre el metal que entró y multiplicando por 100", "La recuperación compara el metal de los lingotes con el que entró."),
        ("En un balance de planta: ¿qué se hace si la diferencia supera lo aceptado?", "Se busca la causa y se informa, sin cambiar cifras", "Un balance forzado oculta pérdidas reales."),
    ],
    op=("Ficha de ejemplo: «Fundición Cordón Demo». Tostación: entran 60 toneladas de concentrado y salen 45 toneladas de calcina. La calcina tiene 40 % de metal. En la fundición se obtienen lingotes con 15.300 kilos de metal, la escoria tiene 2.000 kilos de metal y el polvo captado 400 kilos. Se acepta una diferencia de hasta 1 % del metal que entra. Escribe (a) las toneladas que salieron como gases, (b) los kilos de metal de la calcina, (c) la recuperación de la fundición, (d) los kilos sin explicar, (e) si es aceptable y qué haces.",
        "(a) 60 − 45 = 15 toneladas. (b) 45 × 40 ÷ 100 = 18 toneladas = 18.000 kg. (c) 15.300 ÷ 18.000 × 100 = 85 %. (d) 18.000 − (15.300 + 2.000 + 400) = 300 kg. (e) El 1 % de 18.000 es 180 kg; 300 supera 180, así que no es aceptable: se busca la causa y se informa, sin cambiar cifras.",
        ["calcula bien los gases", "calcula bien el metal de la calcina", "calcula bien la recuperación", "calcula bien los kilos sin explicar", "concluye que no es aceptable e informa"],
        ["hoja con las cinco respuestas"],
        ["olvidar pasar toneladas a kilos", "comparar kilos con un porcentaje", "ajustar la escoria para que cuadre"],
        "Pregunta: «¿qué suma de salidas comparas con el metal que entró?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa una tostación y una fundición con sus entradas y salidas y calcula la recuperación y la diferencia sin explicar.",
    extend="Explica con un ejemplo por qué la calcina pesa menos que el concentrado del que viene.",
)

# ============================================================ OAE-04, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). La «Fundición Demo» tiene un lote de 20 toneladas de metal con pureza de 98 %, y el cliente exige 99 %. Opción A: refinar el lote (costo de ejemplo de $80.000 por tonelada) y venderlo a $5.000.000 por tonelada, con una pureza certificada de 99 % después de la refinación. "
     "Opción B: vender el lote sin refinar con un descuento de ejemplo de $2.000.000 por tonelada, solo si el cliente acepta la pureza menor. Cada lingote de ejemplo pesa 500 kilos; 1 tonelada son 1.000 kilos.")
build(
    O4, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: comparar la opción de refinar con la de vender sin refinar, calcular el valor neto de cada una y justificar la recomendación con la calidad exigida.",
    prior=["Sé qué son la refinación, la pureza y el lingote.", "Sé multiplicar y restar números enteros.", "Sé comparar un dato con un criterio."],
    explain=[
        "La refinación purifica el metal para que cumpla la calidad que exige el cliente. Cuando un lote no alcanza la pureza pedida hay dos caminos: refinarlo, lo que tiene un costo por tonelada, o venderlo sin refinar, solo si el cliente acepta la pureza menor, con un descuento en el precio. Para decidir se compara el valor neto de cada opción, que es lo que se recibe por el lote menos lo que cuesta dejarlo en esa condición.",
        "Las impurezas del lote se calculan con la pureza: si un lote de 10.000 kilos tiene pureza de 96 %, las impurezas son el 4 % restante, es decir 400 kilos. Con un costo de refinación de ejemplo de $60.000 por tonelada y un precio de $3.000.000 por tonelada, un lote de 10 toneladas deja un valor neto de 30.000.000 − 600.000 = $29.400.000. Antes de comparar valores, se revisa si la opción cumple lo exigido o si necesita la aceptación del cliente.",
        f"Las cifras son de ejemplo; los costos y precios reales los fijan contratos y personas autorizadas. La refinación misma es un trabajo con calor y metal fundido que realiza solo personal autorizado; este cuaderno no enseña esos pasos. {EMER} {AVISO}",
    ],
    vocab=[("valor neto de una opción", "lo que se recibe por el lote menos lo que cuesta dejarlo en esa condición"), ("costo de refinación", "costo de purificar cada tonelada del lote, un dato de ejemplo"), ("descuento", "rebaja del precio por no cumplir la calidad exigida"), ("pureza certificada", "pureza medida y certificada por el laboratorio"), ("aceptación del cliente", "acuerdo del cliente para recibir un lote con menor pureza")],
    worked=[
        ("Impurezas de un lote", "Un lote de ejemplo de 10.000 kilos tiene pureza de 96 %. ¿Cuántos kilos de impurezas tiene?", ["Las impurezas son 4 por ciento del lote.", "10.000 por 4 dividido por 100 es 400."], "400 kilos"),
        ("Valor neto de refinar", "Un lote de ejemplo de 10 toneladas se refina a $60.000 por tonelada y se vende a $3.000.000 por tonelada. ¿Cuál es el valor neto?", ["Ingreso: 10 por 3.000.000 es 30.000.000.", "Costo de refinar: 10 por 60.000 es 600.000; la resta da 29.400.000."], "$29.400.000"),
    ],
    mistakes=[("Elegir la opción más barata sin revisar si el cliente acepta la pureza menor.", "Sin aceptación del cliente, vender sin refinar no es posible.", "Primero se revisa lo exigido y después se compara el valor neto."),
              ("Creer que estos costos de ejemplo valen para una fundición real.", "Los costos reales dependen del contrato, del lote y de la planta.", "Los números del cuaderno sirven para practicar el cálculo.")],
    T=[
        ("abc", "En una fundición: ¿para qué se refina un lote de metal?", "Para que cumpla la pureza que exige el cliente", "Para reducir el tamaño de sus lingotes", "Para disolverlo en una solución", "La refinación purifica el metal; no cambia su tamaño ni lo disuelve."),
        ("abc", "En una fundición: ¿qué es el costo de refinación de ejemplo?", "Lo que cuesta purificar cada tonelada del lote, un dato de ejemplo", "El precio al que se vende el lote refinado", "La rebaja que se hace al vender sin refinar", "El costo de refinación es un gasto por tonelada; el precio y el descuento son otros datos."),
        ("abc", "En una decisión de planta: ¿qué es el valor neto de una opción?", "Lo que se recibe por el lote menos lo que cuesta dejarlo en esa condición", "El peso total del lote en kilos", "La pureza que certifica el laboratorio", "El valor neto resta los costos a lo que se recibe."),
        ("=", "{F} ¿Cuántos kilos de impurezas tiene el lote antes de refinar?", "20*1000*2//100", "Se pasan las toneladas a kilos y se calcula el 2 % de impurezas.", " kg"),
        ("=", "{F} ¿Cuántos lingotes de 500 kilos forman el lote?", "20*1000//500", "Se pasan las toneladas a kilos y se dividen entre la masa de un lingote.", " lingotes"),
        ("=", "{F} ¿Cuánto cuesta refinar el lote, en pesos?", "20*80000", "Se multiplican las toneladas por el costo por tonelada.", " pesos"),
        ("=", "{F} ¿Cuál es el ingreso por vender el lote refinado, en pesos?", "20*5000000", "Se multiplican las toneladas por el precio por tonelada.", " pesos"),
        ("=", "{F} ¿Cuál es el valor neto de la opción A, en pesos?", "20*5000000-20*80000", "Se resta el costo de refinar al ingreso.", " pesos"),
        ("=", "{F} ¿Cuál es el valor de la opción B, en pesos?", "20*(5000000-2000000)", "Se multiplican las toneladas por el precio con descuento.", " pesos"),
        ("abc", "{F} ¿Qué opción tiene mayor valor neto?", "La opción A, porque el descuento de la B resta más que el costo de refinar", "La opción B, porque no tiene costo de refinación", "Ninguna, porque las dos dejan lo mismo", "El descuento de la opción B reduce más el valor que el costo de refinar en la A."),
        ("abc", "{F} ¿Qué condición debe cumplirse para considerar la opción B?", "Que el cliente acepte recibir un lote con menor pureza que la exigida", "Que el lote tenga más lingotes que antes", "Que el laboratorio certifique 100 % de pureza", "Sin aceptación del cliente, un lote que no cumple lo exigido no puede venderse como si cumpliera."),
        ("=", "{F} ¿Cuántos pesos más deja la opción A que la opción B?", "20*5000000-20*80000-20*(5000000-2000000)", "Se restan los valores netos de las dos opciones.", " pesos"),
        ("abc", "{F} El jefe pide una recomendación. ¿Cuál es la mejor?", "Elegir A, porque cumple los 99 % exigidos y tiene mayor valor neto, aceptando el costo de refinación", "Elegir B, porque no tiene costo de refinación", "Elegir A, porque tiene un descuento menor que B", "La recomendación cita la calidad exigida, el valor neto y el costo aceptado; A no tiene descuento, B sí."),
    ],
    ctx=("abc", "Un conocido te pide que, con estos costos de ejemplo, le digas si le conviene refinar un lote real de su pequeño negocio. ¿Qué respondes?", "Que los números del cuaderno son de ejemplo y que la decisión la toman personas autorizadas con datos reales; lo consultarás con un adulto responsable", "Que sí, porque el cálculo es exacto", "Que sí, si el lote es pequeño", "Los valores de ejemplo no describen un contrato ni un lote reales."),
    sc=[
        ("En una fundición: ¿cuándo se compara el valor neto de dos opciones?", "Después de revisar si cumplen lo exigido o necesitan la aceptación del cliente", "Lo exigido va antes que el valor."),
        ("En un lote de metal: ¿cómo se calculan los kilos de impurezas?", "Multiplicando los kilos del lote por el porcentaje de impureza y dividiendo por 100", "Las impurezas son el porcentaje que falta para 100 % de pureza."),
        ("En una decisión de planta: ¿qué debe citar una recomendación?", "La calidad exigida, las cifras y lo que se acepta ceder", "Así la decisión puede revisarse después con las mismas cifras."),
    ],
    op=("Ficha de ejemplo: la «Fundición Cordón Demo» tiene un lote de 10 toneladas de metal con pureza de 97 %; el cliente exige 99 %. Opción A: refinar a $90.000 por tonelada y vender a $4.000.000 por tonelada. Opción B: vender sin refinar con un descuento de $1.500.000 por tonelada, si el cliente acepta. Escribe (a) los kilos de impurezas del lote, (b) el costo de refinar, (c) el valor neto de A, (d) el valor de B, (e) qué opción conviene y qué falta confirmar para considerar B.",
        "(a) 10.000 × 3 ÷ 100 = 300 kg. (b) 10 × 90.000 = 900.000 pesos. (c) 10 × 4.000.000 − 900.000 = 39.100.000 pesos. (d) 10 × (4.000.000 − 1.500.000) = 25.000.000 pesos. (e) Conviene A: cumple el 99 % y deja más valor; para considerar B falta que el cliente acepte la pureza menor.",
        ["calcula bien las impurezas", "calcula bien el costo de refinar", "calcula bien el valor neto de A", "calcula bien el valor de B", "recomienda y menciona la aceptación del cliente"],
        ["hoja con las cinco respuestas"],
        ["olvidar pasar toneladas a kilos", "no restar el costo de refinar", "elegir B sin considerar la aceptación del cliente"],
        "Pregunta: «¿qué se descuenta del ingreso en cada opción?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Compara dos opciones inventadas, una con refinación y otra con descuento, y calcula el valor neto de cada una.",
    extend="Explica con un ejemplo por qué la opción de menor costo no siempre es la que conviene.",
)

# ============================================================ OAE-05, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). La «Planta Demo» de la empresa ficticia «Minera Demo» tiene tres puntos de muestreo: P1 (alimentación a molienda), P2 (concentrado) y P3 (relave). En cada punto se toma una muestra puntual cada 3 horas, "
     "en turnos de 12 horas, con 2 turnos por día (datos de ejemplo). Cada muestra puntual pesa 2 kilos y con las de un turno se forma una muestra compuesta. "
     "Peligros anotados: P1 queda junto a una cinta con partes en movimiento, P2 sobre una canaleta con pulpa resbaladiza y P3 junto al borde de una poza sin baranda.")
build(
    O5, 1, F,
    use="Aprenderé qué es el muestreo, qué es una muestra representativa, la diferencia entre muestra puntual y compuesta, qué peligros tienen los puntos de muestreo y por qué solo personal autorizado toma las muestras.",
    prior=["Sé qué son un concentrado y un relave.", "Sé multiplicar y dividir números enteros.", "Sé la jerarquía de controles."],
    explain=[
        "El muestreo es obtener una porción pequeña de un material para analizarla y conocer sus características, sin analizar todo el material. Una muestra representativa tiene las mismas características del material completo del que se tomó: si no lo es, el análisis engaña a quien decide. Una muestra puntual se toma en un instante; una muestra compuesta se forma uniendo varias puntuales de un período. El protocolo de muestreo es el documento aprobado que fija en qué punto, con qué frecuencia y con qué rotulado se toma cada muestra.",
        "El número de muestras se calcula con la duración del período y la frecuencia: en un turno de ejemplo de 10 horas con una muestra cada 2 horas se toman 5 muestras, y si cada una pesa 3 kilos, la compuesta reúne 15 kilos. Cada muestra se rotula para saber de dónde, cuándo y quién la tomó, y se entrega al laboratorio con un registro.",
        f"Un punto de muestreo es un lugar de trabajo con peligros: partes en movimiento, superficies resbaladizas, bordes de pozas, pulpa y soluciones. Por eso la toma de muestras la hacen solo personas autorizadas, con protocolo, EPP y permiso, y los puntos se protegen con resguardos, barandas y señales según la norma vigente. Este cuaderno no enseña cómo tomar muestras. {EMER} {AVISO}",
    ],
    vocab=[("muestreo", "obtención de una porción pequeña de un material para analizarla"), ("muestra representativa", "muestra con las mismas características del material completo del que se tomó"), ("muestra puntual", "muestra tomada en un instante"), ("muestra compuesta", "muestra formada por la unión de varias puntuales de un período"), ("protocolo de muestreo", "documento aprobado que fija punto, frecuencia y rotulado de cada muestra"), ("punto de muestreo", "lugar definido donde se toman las muestras")],
    worked=[
        ("Número de muestras", "Un turno de ejemplo dura 10 horas y se toma una muestra cada 2 horas en un punto. ¿Cuántas muestras puntuales se toman?", ["Se divide la duración entre la frecuencia.", "10 dividido por 2 es 5."], "5 muestras"),
        ("Masa de la compuesta", "Esas 5 muestras de ejemplo pesan 3 kilos cada una. ¿Cuántos kilos reúne la muestra compuesta?", ["Se multiplica la cantidad de muestras por la masa de cada una.", "5 por 3 es 15."], "15 kilos"),
    ],
    mistakes=[("Creer que cualquier porción de material sirve como muestra.", "Una porción tomada sin criterio puede no tener las características del material completo.", "La muestra se toma según el protocolo, para que sea representativa."),
              ("Creer que leer sobre muestreo habilita para tomar muestras en una planta.", "Los puntos de muestreo tienen peligros y exigen personal autorizado, EPP, permiso y norma vigente.", "Aprende aquí el concepto y deja la toma de muestras a personal autorizado.")],
    T=[
        ("abc", "En Metalurgia Extractiva: ¿qué es una muestra representativa?", "La que tiene las mismas características del material completo del que se tomó", "La más grande que se pueda llevar al laboratorio", "La que se toma más cerca de la sala de control", "Representativa significa que refleja al material completo; el tamaño o el lugar cómodo no lo garantizan."),
        ("abc", "En una planta: ¿qué es una muestra compuesta?", "La formada por la unión de varias muestras puntuales de un período", "Una única muestra tomada en un instante", "La que se mezcla con agua antes de analizarla", "La compuesta reúne puntuales; la tomada en un instante es la puntual."),
        ("abc", "En el control de una planta: ¿para qué sirve el muestreo?", "Para conocer con un análisis las características de un producto y controlar el proceso", "Para aumentar la producción del turno", "Para registrar las horas de trabajo del personal", "El muestreo entrega información para controlar el proceso; no aumenta producción ni registra horas."),
        ("=", "{F} ¿Cuántas muestras puntuales se toman por turno en un punto?", "12//3", "Se divide la duración del turno entre la frecuencia.", " muestras"),
        ("=", "{F} ¿Cuántas muestras puntuales se toman por día en un punto?", "12//3*2", "Se multiplican las muestras de un turno por los turnos del día.", " muestras"),
        ("=", "{F} ¿Cuántas muestras puntuales se toman por día en los tres puntos?", "12//3*2*3", "Se multiplican las muestras por punto y por día por los tres puntos.", " muestras"),
        ("=", "{F} ¿Cuántos kilos reúne la muestra compuesta de un turno en un punto?", "12//3*2", "Se multiplican las muestras de un turno por los kilos de cada una.", " kg"),
        ("abc", "{F} ¿Cuál es el riesgo asociado al punto P1?", "Que una persona sea atrapada o golpeada por las partes en movimiento de la cinta", "Que la muestra salga con más ley", "Que la muestra pese más de 2 kilos", "El riesgo es un daño a la persona; la ley o la masa de la muestra no son un daño."),
        ("abc", "{F} Un estudiante dice: «ya sé qué es muestrear, así que puedo tomar muestras en P3 sin permiso». ¿Qué respuesta es correcta?", "Es falso: tomar muestras exige personal autorizado, protocolo, EPP y permiso", "Es cierto, si lleva casco", "Es cierto, si va acompañado de un compañero", "El casco o la compañía no reemplazan la autorización ni el permiso."),
        ("abc", "{F} ¿Qué medida de la jerarquía actúa mejor sobre el borde sin baranda de la poza en P3?", "Instalar una baranda, por personal autorizado", "Pedir que las muestras se tomen con cuidado", "Entregar un casco al personal", "Una barrera física elimina la exposición; pedir cuidado o usar casco son niveles inferiores."),
        ("=", "{F} Si el turno se alargara a 15 horas con la misma frecuencia, ¿cuántas muestras puntuales se tomarían por punto?", "15//3", "Se divide la nueva duración entre la frecuencia.", " muestras"),
        ("abc", "{F} Un compañero propone tomar las 4 muestras del turno juntas al inicio «para ahorrar tiempo». ¿Cuál es la mejor objeción?", "Así la muestra no representa lo que ocurre durante todo el turno; deben tomarse repartidas según el protocolo", "Ninguna, porque 4 muestras iguales dan lo mismo", "Que las muestras al inicio siempre pesan menos", "La muestra compuesta debe reflejar todo el período, no un solo momento."),
        ("abc", "{F} Durante una visita de ejemplo, ves que una persona cae junto a la poza de P3. ¿Qué corresponde según las reglas generales?", "No acercarte a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarte al borde para ayudar", "Esperar a que se levante sola", "Acercarse al borde sin formación puede causar otra caída; se avisa a quienes pueden actuar."),
    ],
    ctx=("abc", "Un conocido que tiene una pequeña faena te ofrece pagarte por tomar unas muestras de su pila «porque ya sabes qué es una muestra representativa». ¿Qué respondes?", "Que no, porque tomar muestras en una faena exige personal autorizado y norma vigente, y que lo consultarás con un adulto responsable", "Que sí, si usas guantes", "Que sí, si es una sola muestra", "Haber estudiado el concepto no habilita para trabajar en una faena."),
    sc=[
        ("En Metalurgia Extractiva: ¿qué es el protocolo de muestreo?", "El documento aprobado que fija punto, frecuencia y rotulado de cada muestra", "El protocolo asegura que las muestras se tomen de forma comparable."),
        ("En una planta: ¿qué es una muestra puntual?", "Una muestra tomada en un instante", "La puntual se toma en un momento; la compuesta reúne varias."),
        ("En un punto de muestreo: ¿quién toma las muestras?", "Personal autorizado, con protocolo, EPP y permiso", "El punto tiene peligros y exige formación."),
    ],
    op=("Ficha de ejemplo: la «Planta Cordón Demo» tiene dos puntos de muestreo. En cada uno se toma una muestra puntual cada 3 horas en turnos de 9 horas, con 3 turnos por día, y cada muestra pesa 4 kilos. Uno de los puntos queda junto a una cinta sin resguardo. Escribe (a) cuántas muestras puntuales se toman por turno en un punto, (b) cuántas por día en los dos puntos, (c) cuántos kilos reúne la compuesta de un turno en un punto, (d) un peligro del punto junto a la cinta y su riesgo, (e) qué debe hacer una persona que ve a alguien atrapado en la cinta.",
        "(a) 9 ÷ 3 = 3 muestras. (b) 3 × 3 turnos × 2 puntos = 18 muestras. (c) 3 × 4 = 12 kg. (d) Peligro: la cinta sin resguardo; riesgo: que una persona sea atrapada por las partes en movimiento. (e) No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias.",
        ["calcula bien las muestras por turno", "calcula bien las muestras por día", "calcula bien los kilos", "distingue peligro y riesgo", "indica no acercarse y avisar"],
        ["hoja con las cinco respuestas"],
        ["olvidar multiplicar por los turnos", "olvidar multiplicar por los kilos", "responder que se acerca a soltar a la persona"],
        "Pregunta: «¿cuántas veces cabe la frecuencia en la duración del turno?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa un turno, una frecuencia de muestreo y un peso por muestra, y calcula cuántas muestras se toman y cuántos kilos tiene la compuesta.",
    extend="Explica con un ejemplo por qué una muestra tomada una sola vez al día puede no ser representativa.",
)

# ============================================================ OAE-05, clase 2
F = ("Ficha 2 (documentos de ejemplo, inventados). «Planta Demo». Documentos: el protocolo de muestreo (documento aprobado que fija en qué punto, con qué frecuencia y con qué rotulado se toma cada muestra; lo aplica personal autorizado), "
     "el rótulo de la muestra (código único, punto, fecha, hora, turno y responsable), la cadena de custodia (registro con la firma de cada persona que entrega y recibe la muestra, desde el punto hasta el laboratorio) y el informe del laboratorio. "
     "Cuatro rótulos de ejemplo, todos del 12 de marzo (fecha de ejemplo), turno 1: A, código M-01, punto P2, hora 08:00, responsable Luis Demo. B, código M-02, punto P2, sin hora, responsable Ana Demo. "
     "C, código M-03, punto P1, hora 11:00, sin responsable. D, código M-02, punto P3, hora 11:00, responsable Luis Demo. "
     "Cadena de custodia de M-01: entrega Luis Demo a las 08:30; recibe Camila Demo (laboratorio) a las 09:00, sin firma de recepción. Criterio de ejemplo: la muestra llega al laboratorio como máximo 60 minutos después de tomarse. "
     "Roles: muestrero autorizado, supervisor, laboratorista y prevencionista de riesgos.")
build(
    O5, 2, F,
    use="Aprenderé los documentos del muestreo (protocolo, rótulo, cadena de custodia e informe), los roles y cómo detectar un rótulo incompleto, un código repetido o una cadena de custodia con un vacío.",
    prior=["Sé qué es una muestra representativa.", "Sé leer un registro escrito.", "Sé calcular minutos entre dos horas."],
    explain=[
        "Una muestra sin identificación no sirve. El rótulo es la etiqueta de la muestra y debe tener un código único (que no se repite en ninguna otra muestra), el punto, la fecha, la hora, el turno y el responsable. La cadena de custodia es el registro que sigue a la muestra desde que se toma hasta que llega al laboratorio: cada persona que la entrega y la recibe anota la hora y firma. Con ella se sabe quién tuvo la muestra en cada momento, y si falta una firma, hay un vacío que debe informarse.",
        "El protocolo de muestreo es el documento aprobado que fija cómo se identifica y se entrega cada muestra; lo aplica personal autorizado. Un criterio de tiempo, como llegar al laboratorio en un máximo de minutos, se verifica restando la hora de toma a la de recepción: una muestra tomada a las 10:00 y recibida a las 10:40 tardó 40 minutos. Un rótulo o una cadena incompletos no se completan de memoria: se informa y se anota la observación.",
        f"Roles: el muestrero autorizado toma la muestra y la rotula, el supervisor decide qué hacer ante una irregularidad, el laboratorista recibe, analiza y firma la recepción, y el prevencionista asesora sobre riesgos del punto. Nadie firma por otra persona ni cambia un dato después. {EMER} {AVISO}",
    ],
    vocab=[("rótulo de la muestra", "etiqueta con el código único, el punto, la fecha, la hora, el turno y el responsable"), ("código único", "código que no se repite en ninguna otra muestra"), ("cadena de custodia", "registro con la hora y la firma de cada persona que entrega y recibe la muestra"), ("muestrero autorizado", "persona autorizada para tomar y rotular muestras"), ("trazabilidad de la muestra", "posibilidad de saber de dónde viene y quién la tuvo en cada momento")],
    worked=[
        ("Minutos hasta el laboratorio", "Una muestra de ejemplo se tomó a las 10:00 y el laboratorio la recibió a las 10:40. ¿Cuántos minutos pasaron?", ["De las 10:00 a las 10:40 pasan 40 minutos.", "Si el máximo es 60 minutos, cumple."], "40 minutos"),
        ("Detectar un rótulo incompleto", "Un rótulo de ejemplo trae código, punto, fecha y hora, pero no dice quién tomó la muestra. ¿Qué falta?", ["La lista exige también el responsable.", "Falta el responsable."], "El responsable"),
    ],
    mistakes=[("Completar de memoria la hora que falta en un rótulo.", "Un dato recordado sin respaldo puede ser falso y rompe la trazabilidad.", "Se informa al supervisor y se anota la observación sin inventar el dato."),
              ("Repetir un código porque «las muestras son parecidas».", "Dos muestras con el mismo código no se pueden distinguir en el laboratorio.", "Cada muestra lleva un código único.")],
    T=[
        ("abc", "En el muestreo de una planta: ¿qué es el protocolo de muestreo?", "El documento aprobado que fija en qué punto, con qué frecuencia y con qué rotulado se toma cada muestra", "El informe con la ley de cada muestra", "El permiso del dueño del terreno", "El protocolo define cómo se toman las muestras; el informe entrega resultados."),
        ("abc", "En el muestreo de una planta: ¿qué es la cadena de custodia?", "El registro con la hora y la firma de cada persona que entrega y recibe la muestra", "La cadena de la cinta transportadora", "El peso de la muestra al llegar al laboratorio", "La cadena de custodia sigue a la muestra por manos y horas."),
        ("abc", "En el muestreo de una planta: ¿qué debe tener el rótulo de una muestra?", "Código único, punto, fecha, hora, turno y responsable", "Solo el peso en kilos", "Solo el nombre del laboratorista", "El rótulo identifica de dónde, cuándo y quién; el peso o un nombre no bastan."),
        ("abc", "{F} ¿Cuál de los rótulos A, B y C está completo?", "El A, que tiene código, punto, fecha, hora, turno y responsable", "El B, que tiene todos los datos menos uno", "El C, que tiene hora y punto", "Entre A, B y C, solo el rótulo A trae los seis datos que debe tener."),
        ("abc", "{F} ¿Qué dato falta en el rótulo B?", "La hora", "El código", "El responsable", "El rótulo B trae código y responsable, pero no hora."),
        ("abc", "{F} ¿Qué dato falta en el rótulo C?", "El responsable", "La hora", "El punto", "El rótulo C trae hora y punto, pero no dice quién tomó la muestra."),
        ("abc", "{F} ¿Cuál es el problema del rótulo D?", "Su código M-02 se repite con el del rótulo B, y los códigos deben ser únicos", "Su hora es igual a la del rótulo C", "Su responsable es el mismo que el del rótulo A", "Un código repetido impide distinguir las muestras B y D."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la entrega de M-01 y su recepción en el laboratorio?", "9*60-(8*60+30)", "Se restan las horas pasadas a minutos.", " minutos"),
        ("abc", "{F} En la cadena de custodia de M-01 falta la firma de recepción. ¿Qué corresponde?", "Informar al supervisor para que el laboratorio verifique y registre la recepción real, sin firmar por otra persona", "Pedir a Luis Demo que firme también la recepción", "Dejarlo así, porque la hora de recepción está anotada", "Una firma ausente es un vacío en el registro; firmar por otra persona sería falsificarlo."),
        ("=", "{F} Si M-03 se tomó a las 11:00 y llegó al laboratorio a las 12:10, ¿cuántos minutos pasaron?", "(12*60+10)-(11*60)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} Con el criterio de máximo 60 minutos, ¿qué conclusión es correcta sobre M-03?", "No cumple, porque tardó 70 minutos; se informa para que el laboratorio decida", "Cumple, porque tardó poco más de una hora", "Cumple, porque la muestra tiene hora anotada", "70 minutos superan el máximo de 60; la decisión sobre el análisis la toma el laboratorio."),
        ("abc", "{F} Un compañero propone completar de memoria la hora del rótulo B. ¿Cuál es la mejor respuesta?", "No se hace: se informa al supervisor y se anota la observación sin inventar el dato", "Se puede, si recuerda más o menos la hora", "Se puede, si la hora se parece a la de otra muestra", "Un dato recordado sin respaldo puede ser falso y rompe la trazabilidad."),
        ("abc", "{F} ¿Quién aplica el protocolo en el punto de muestreo?", "El muestrero autorizado", "Cualquier estudiante en práctica", "El encargado de despacho", "El protocolo se aplica por personal autorizado."),
    ],
    ctx=("abc", "Un compañero de práctica propone copiar el rótulo de una muestra buena en otra «porque se parecen». ¿Qué respondes?", "Que no, porque cada muestra necesita su propio código, y que lo consultarás con un adulto responsable", "Que sí, porque ahorra tiempo", "Que sí, si cambia solo la hora", "Copiar un rótulo repite un código y rompe la trazabilidad."),
    sc=[
        ("En el muestreo: ¿qué es un código único?", "Un código que no se repite en ninguna otra muestra", "El código único permite distinguir cada muestra."),
        ("En el muestreo de una planta: ¿qué se hace si falta una firma en la cadena de custodia?", "Se informa y se verifica el hecho real, sin firmar por otra persona", "Un vacío se informa para poder resolverlo."),
        ("En el muestreo: ¿cómo se calculan los minutos entre dos horas?", "Pasando las horas a minutos y restando", "La resta entre horas en minutos entrega el tiempo transcurrido."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo», 3 de abril (fecha de ejemplo). Rótulo X: código M-10, punto P3, sin hora, responsable Eva Demo. Rótulo Y: código M-10, punto P2, hora 14:00, responsable Eva Demo. Criterio de ejemplo: máximo 60 minutos hasta el laboratorio. La muestra del rótulo Y se entregó a las 14:20 y el laboratorio la recibió a las 15:05. Escribe (a) qué falta en el rótulo X, (b) cuál es el problema de los códigos, (c) cuántos minutos pasaron entre la toma y la recepción de la muestra Y y si cumple, (d) qué haces si descubres estos problemas.",
        "(a) Falta la hora. (b) Los dos rótulos tienen el código M-10, que debe ser único. (c) De las 14:00 a las 15:05 pasaron 65 minutos; no cumple el máximo de 60. (d) Informar al supervisor y anotar las observaciones, sin completar datos de memoria ni cambiar códigos por cuenta propia.",
        ["identifica la hora que falta", "identifica el código repetido", "calcula bien los minutos y concluye que no cumple", "informa sin inventar datos"],
        ["hoja con las cuatro respuestas"],
        ["calcular los minutos desde la entrega y no desde la toma", "completar la hora de memoria", "cambiar el código por cuenta propia"],
        "Pregunta: «¿desde cuándo se cuenta el tiempo que tardó la muestra?». Si no responde, pídele que relea el segundo párrafo."),
    reinforce="Inventa dos rótulos, uno completo y otro con un dato faltante, y explica qué se hace con el incompleto.",
    extend="Explica con un ejemplo por qué una muestra con la cadena de custodia incompleta puede perder su valor como evidencia.",
)

# ============================================================ OAE-05, clase 3
F = ("Ficha 3 (planilla de ejemplo, inventada). Muestras puntuales de un producto intermedio de la «Planta Demo» en un día; cada una representa las toneladas indicadas. M-21: 400 toneladas, ley 2 %. M-22: 300 toneladas, ley 3 %. "
     "M-23: 100 toneladas, ley 5 %. M-24: 200 toneladas, ley 4 %. Análisis duplicados (la misma muestra analizada de nuevo): M-22, ley 5 %; M-24, ley 5 %. "
     "Criterio de repetibilidad de ejemplo: la diferencia entre el análisis original y el duplicado debe ser como máximo 1 punto de ley (una diferencia de exactamente 1 punto cumple).")
build(
    O5, 3, F,
    use="Aprenderé a analizar en papel una planilla de muestreo: calcular la ley ponderada de las muestras de un día, comprobar la repetibilidad de los duplicados y decidir qué informar.",
    prior=["Sé qué son muestra puntual y compuesta.", "Sé calcular unidades de metal.", "Sé comparar un dato con un criterio."],
    explain=[
        "Cada muestra puntual representa un tramo de producción, con sus toneladas. Para conocer la ley de todo el día se pondera: se multiplica cada ley por las toneladas que representa, se suman esas unidades de metal y se divide entre las toneladas totales. El promedio simple de las leyes engaña cuando los tramos tienen toneladas distintas. Con 100 toneladas de ley 2 % y 300 toneladas de ley 6 %, hay 200 + 1.800 = 2.000 unidades en 400 toneladas y la ley ponderada es 5 %; el promedio simple habría dado 4 %.",
        "Un duplicado es un nuevo análisis de la misma muestra que se hace para comprobar que el resultado se repite. La repetibilidad es esa coincidencia: se compara la diferencia entre el análisis original y el duplicado con un máximo aceptado. Si la diferencia es mayor, no se promedian los dos números ni se descarta uno por cuenta propia: se informa al laboratorio y al supervisor, que deciden si se repite el análisis o se revisa la muestra.",
        f"El informe del día debe incluir la ley ponderada y también las observaciones, como un duplicado fuera del criterio. Los datos reales los generan personas autorizadas; los de este cuaderno son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("ley ponderada", "ley de un conjunto de muestras calculada con las toneladas que representa cada una"), ("análisis duplicado", "nuevo análisis de la misma muestra para comprobar que el resultado se repite"), ("repetibilidad", "coincidencia entre dos análisis de la misma muestra dentro de un límite"), ("tramo de producción", "cantidad de toneladas que representa una muestra"), ("observación", "nota que deja constancia de una irregularidad en el informe")],
    worked=[
        ("Ley ponderada", "Dos muestras de ejemplo: 100 toneladas con ley de 2 % y 300 toneladas con ley de 6 %. ¿Cuál es la ley ponderada?", ["Unidades: 100 por 2 más 300 por 6, es decir 2.000.", "2.000 dividido por 400 toneladas es 5."], "5 %"),
        ("Repetibilidad", "El máximo de diferencia aceptado es 1 punto. Una muestra de ejemplo dio 3 % y su duplicado 4 %. ¿Cumple?", ["La diferencia es 4 menos 3, es decir 1 punto.", "Una diferencia igual al máximo cumple."], "Sí, cumple"),
    ],
    mistakes=[("Calcular la ley del día con el promedio simple de las leyes.", "Un tramo de pocas toneladas pesaría lo mismo que uno de muchas.", "Se pondera por las toneladas que representa cada muestra."),
              ("Descartar un duplicado que «estropea el promedio».", "Descartar un dato inconveniente oculta un posible problema en la muestra o el análisis.", "Se informa al laboratorio y al supervisor, y ellos deciden cómo revisar.")],
    T=[
        ("abc", "En el control de calidad de una planta: ¿qué es un análisis duplicado?", "Un nuevo análisis de la misma muestra para comprobar que el resultado se repite", "Una segunda muestra tomada en otro punto", "Una copia del informe del laboratorio", "El duplicado repite el análisis de la misma muestra, no la toma de otra."),
        ("abc", "En el control de calidad de una planta: ¿qué es la repetibilidad?", "La coincidencia entre dos análisis de la misma muestra dentro de un límite", "El tamaño de la muestra reunida", "La cantidad de veces que el muestrero visita el punto", "La repetibilidad mide cuánto se parecen dos análisis de una misma muestra."),
        ("abc", "En una planilla de muestreo: ¿por qué el promedio simple de las leyes puede engañar?", "Porque cada muestra representa distintas toneladas y debe pesar según ellas", "Porque el promedio siempre da un número mayor", "Porque no se puede calcular con números enteros", "Los tramos grandes deben influir más que los pequeños."),
        ("=", "{F} ¿Cuántas unidades de metal representa la muestra M-21?", "400*2", "Se multiplican las toneladas por la ley en porcentaje.", " unidades"),
        ("=", "{F} ¿Cuántas unidades de metal suman las cuatro muestras del día?", "400*2+300*3+100*5+200*4", "Se suman las unidades de cada muestra.", " unidades"),
        ("=", "{F} ¿Cuál es la ley ponderada del día, en porcentaje?", "(400*2+300*3+100*5+200*4)//(400+300+100+200)", "Se divide el total de unidades entre las toneladas totales.", " %"),
        ("abc", "{F} Un compañero calcula (2 + 3 + 5 + 4) ÷ 4 = 3,5 % como ley del día. ¿Qué corresponde?", "Corregirlo: hay que ponderar por las toneladas que representa cada muestra", "Aceptarlo, porque promediar es lo correcto", "Corregirlo: la ley del día es 5 %, la mayor de las muestras", "Con promedio simple los 100 toneladas de ley 5 % pesan igual que los 400 de ley 2 %."),
        ("=", "{F} ¿Cuántos puntos de ley hay entre el análisis original de M-24 y su duplicado?", "5-4", "Se resta la ley original a la del duplicado.", " punto"),
        ("abc", "{F} ¿Cumple la repetibilidad la muestra M-24?", "Sí, porque la diferencia de 1 punto no supera el máximo de 1", "No, porque hay una diferencia", "No, porque 1 es igual al máximo y debería ser menor", "El criterio permite una diferencia de hasta 1 punto, e incluye exactamente 1."),
        ("=", "{F} ¿Cuántos puntos de ley hay entre el análisis original de M-22 y su duplicado?", "5-3", "Se resta la ley original a la del duplicado.", " puntos"),
        ("abc", "{F} Con la diferencia de M-22, ¿qué corresponde?", "Informar al laboratorio y al supervisor para que decidan si se repite el análisis o se revisa la muestra", "Promediar los dos análisis y usar el resultado", "Descartar el duplicado y seguir con el original", "Una diferencia fuera del criterio se informa; promediar o descartar sin autorización oculta el problema."),
        ("=", "{F} Si el laboratorio confirmara que la ley correcta de M-22 es 4 % en vez de 3 %, ¿cuántas unidades de metal más sumarían las muestras del día?", "(4-3)*300", "Se multiplica la diferencia de ley por las toneladas de M-22.", " unidades"),
        ("abc", "{F} ¿Qué debe incluir el informe del día?", "La ley ponderada del día y la observación de que el duplicado de M-22 no cumplió el criterio", "Solo la ley ponderada del día", "La ley de 3,5 % calculada con el promedio simple", "Un informe completo deja constancia del resultado y de las irregularidades."),
    ],
    ctx=("abc", "Una compañera propone descartar el duplicado de M-22 «porque estropea el promedio del día». ¿Qué respondes?", "Que no, porque descartar un dato inconveniente oculta un posible problema, y que lo consultarás con un adulto responsable", "Que sí, porque una sola muestra no importa", "Que sí, si lo anota en un papel aparte", "Un dato fuera del criterio se informa para revisar la muestra o el análisis."),
    sc=[
        ("En el muestreo de una planta: ¿cómo se calcula la ley ponderada del día?", "Sumando las unidades de metal de las muestras y dividiendo entre las toneladas totales", "Cada muestra pesa según las toneladas que representa."),
        ("En el control de calidad de una planta: ¿qué es la repetibilidad?", "La coincidencia entre dos análisis de la misma muestra dentro de un límite", "La repetibilidad muestra si el análisis es confiable."),
        ("En un informe de muestreo: ¿qué se hace con un duplicado fuera del criterio?", "Se informa y se deja una observación, sin descartar el dato", "Descartar un dato oculta un posible problema."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Muestras de un día: M-31, 600 toneladas, ley 1 %; M-32, 300 toneladas, ley 2 %; M-33, 100 toneladas, ley 8 %. Duplicado de M-33: ley 10 %. Criterio de ejemplo: diferencia máxima de 1 punto de ley entre original y duplicado. Escribe (a) las unidades de metal de cada muestra, (b) la ley ponderada del día, (c) por qué el promedio simple no sirve aquí, (d) si M-33 cumple la repetibilidad, (e) qué haces con el resultado de M-33.",
        "(a) M-31: 600; M-32: 600; M-33: 800 unidades. (b) 2.000 ÷ 1.000 = 2 %. (c) Porque M-33 representa pocas toneladas pero tiene una ley muy alta: el promedio simple le daría el mismo peso que a los 600 toneladas de M-31. (d) No cumple: 10 − 8 = 2 puntos, mayor que 1. (e) Informar al laboratorio y al supervisor y dejar una observación en el informe, sin descartar ni promediar el dato por cuenta propia.",
        ["calcula bien las unidades", "calcula bien la ley ponderada", "explica la limitación del promedio simple", "concluye que no cumple la repetibilidad", "informa sin descartar el dato"],
        ["hoja con las cinco respuestas"],
        ["usar el promedio simple", "decir que 2 puntos cumplen", "descartar el duplicado"],
        "Pregunta: «¿cuánto pesa cada muestra en el resultado del día?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa tres muestras con toneladas y leyes y calcula la ley ponderada y el promedio simple, comparándolos.",
    extend="Explica con un ejemplo por qué una muestra de pocas toneladas con ley muy alta puede alterar un promedio simple.",
)

# ============================================================ OAE-05, clase 4
F = ("Ficha 4 (cálculo de ejemplo, inventado). Se muestrea el concentrado de la «Planta Demo», que sale en lotes de 40 toneladas. Protocolo de ejemplo: se toma un incremento (una porción) cada 5 toneladas; cada incremento pesa 3 kilos. "
     "La muestra reunida debe tener una masa mínima, en kilos, igual a 2 veces el tamaño máximo de partícula en milímetros (regla de ejemplo; las reales las fija el protocolo y el laboratorio). El tamaño máximo de partícula de este lote es 8 mm. "
     "Luego la muestra reunida se reduce dividiendo su masa a la mitad, varias veces seguidas, hasta una masa de laboratorio de 3 kilos.")
build(
    O5, 4, F,
    use="Aprenderé a aplicar un criterio técnico con datos de ejemplo: calcular incrementos y masa de una muestra reunida, compararla con una masa mínima según el tamaño de partícula y calcular cuántas reducciones a la mitad se necesitan.",
    prior=["Sé qué son muestra representativa y protocolo de muestreo.", "Sé multiplicar y dividir números enteros.", "Sé comparar un dato con un criterio."],
    explain=[
        "Un incremento es una porción de material que, junto con otras, forma la muestra reunida de un lote. El número de incrementos se calcula dividiendo las toneladas del lote entre cada cuántas toneladas se toma uno; la masa reunida es el número de incrementos por la masa de cada uno. Cuanto más gruesas son las partículas, más masa se necesita para que la muestra sea representativa, porque con pocas partículas grandes el azar pesa mucho. Por eso el protocolo fija una masa mínima según el tamaño máximo de partícula.",
        "Si la muestra reunida es demasiado grande para el laboratorio, se reduce por etapas: en cada etapa su masa se divide a la mitad. Con 20 kilos, tras una reducción quedan 10 y tras dos reducciones quedan 5. Un ejemplo: en un lote de 30 toneladas con un incremento cada 10 toneladas y 4 kilos por incremento hay 3 incrementos y 12 kilos reunidos; si el mínimo es 10 kilos, cumple con 2 kilos de holgura.",
        f"Si la masa reunida no alcanza el mínimo, la muestra no se usa como si fuera representativa: se informa y las personas autorizadas ajustan el protocolo. Estos valores son de ejemplo; los reales los fijan el protocolo y el laboratorio. {EMER} {AVISO}",
    ],
    vocab=[("incremento", "porción de material que, junto con otras, forma la muestra reunida de un lote"), ("muestra reunida", "conjunto de los incrementos de un lote"), ("masa mínima", "masa más baja que debe tener la muestra para ser representativa"), ("tamaño máximo de partícula", "tamaño de las partículas más gruesas del lote"), ("reducción a la mitad", "etapa en que la masa de la muestra se divide por dos"), ("masa de laboratorio", "masa final de la muestra que se envía a analizar")],
    worked=[
        ("Incrementos y masa", "Un lote de ejemplo de 30 toneladas se muestrea con un incremento cada 10 toneladas, de 4 kilos cada uno. ¿Cuántos incrementos hay y cuántos kilos se reúnen?", ["30 dividido por 10 son 3 incrementos.", "3 por 4 son 12 kilos."], "3 incrementos; 12 kilos"),
        ("Reducciones a la mitad", "Una muestra de ejemplo de 20 kilos se reduce dividiendo su masa a la mitad. ¿Cuántos kilos quedan tras 2 reducciones?", ["La primera reducción deja 10 kilos.", "La segunda deja 5 kilos."], "5 kilos"),
    ],
    mistakes=[("Creer que una muestra más pequeña siempre es mejor porque es más fácil de analizar.", "Una muestra por debajo de la masa mínima puede no representar al lote.", "Se reúne la masa mínima y después se reduce por etapas, según el protocolo."),
              ("Cambiar el protocolo por cuenta propia para tomar menos incrementos.", "El número de incrementos lo fija el protocolo aprobado y no depende del apuro.", "Si hay un problema se informa, y personas autorizadas ajustan el protocolo.")],
    T=[
        ("abc", "En el muestreo de un lote: ¿qué es un incremento?", "Una porción de material que, junto con otras, forma la muestra reunida", "El lote completo que se despacha", "El rótulo que identifica la muestra", "El incremento es una porción; el lote completo y el rótulo son otras cosas."),
        ("abc", "En el muestreo de un lote: ¿por qué las partículas más gruesas exigen una masa mínima mayor?", "Porque con pocas partículas grandes la muestra puede no representar al lote", "Porque las partículas gruesas pesan menos", "Porque las partículas gruesas se pesan peor", "Con pocas partículas grandes, el azar influye mucho en el resultado."),
        ("abc", "En el muestreo de un lote: ¿qué significa reducir la muestra a la mitad varias veces?", "Dividir su masa por dos en cada etapa hasta llegar a la masa de laboratorio", "Duplicar su masa en cada etapa", "Mezclarla con agua hasta que se diluya", "Reducir por etapas disminuye la masa sin perder la representatividad prevista por el protocolo."),
        ("=", "{F} ¿Cuántos incrementos se toman en un lote de 40 toneladas?", "40//5", "Se dividen las toneladas del lote entre cada cuántas se toma un incremento.", " incrementos"),
        ("=", "{F} ¿Cuántos kilos reúne la muestra del lote?", "40//5*3", "Se multiplican los incrementos por los kilos de cada uno.", " kg"),
        ("=", "{F} ¿Cuál es la masa mínima que exige la regla de ejemplo para el lote de 8 mm?", "2*8", "Se multiplica 2 por el tamaño máximo de partícula en milímetros.", " kg"),
        ("abc", "{F} ¿Cumple la muestra reunida la masa mínima?", "Sí, porque 24 kg supera los 16 kg con 8 kg de holgura", "No, porque 24 kg es menos que 40 toneladas", "No, porque cada incremento pesa solo 3 kg", "Se compara la masa reunida con la mínima, no con las toneladas del lote."),
        ("abc", "{F} ¿Cuántas reducciones a la mitad se necesitan para pasar de 24 kg a la masa de laboratorio de 3 kg?", "3 reducciones", "8 reducciones, una por cada incremento del lote", "2 reducciones", "Cada reducción divide por dos: 24, 12, 6 y 3 requieren tres divisiones."),
        ("=", "{F} Otro lote de 40 toneladas tiene tamaño máximo de partícula de 15 mm. ¿Cuál es su masa mínima según la regla de ejemplo?", "2*15", "Se multiplica 2 por el tamaño máximo en milímetros.", " kg"),
        ("=", "{F} Con incrementos de 3 kilos, ¿cuántos incrementos hacen falta para reunir la masa mínima de ese lote de 15 mm?", "30//3", "Se divide la masa mínima entre los kilos de cada incremento.", " incrementos"),
        ("abc", "{F} Con los 8 incrementos (24 kg) en el lote de 15 mm, ¿qué conclusión es correcta?", "No alcanza el mínimo de 30 kg: faltan 6 kg y se informa para ajustar el protocolo", "Alcanza, porque 24 kg es mayor que 15 mm", "Alcanza, porque son 8 incrementos y la regla pide 8", "Se compara masa con masa: 24 kg es menor que 30 kg."),
        ("=", "{F} Si el lote fuera de 60 toneladas con un incremento cada 5 toneladas, ¿cuántos kilos se reunirían?", "60//5*3", "Se calculan los incrementos y se multiplican por los kilos de cada uno.", " kg"),
        ("abc", "{F} Un compañero propone tomar solo 4 incrementos en vez de 8 y «multiplicar el resultado por 2». ¿Cuál es la mejor objeción?", "La muestra debe ser representativa por sí misma, y menos incrementos pueden sesgarla; el número lo fija el protocolo", "Ninguna, porque multiplicar el resultado compensa la diferencia", "Que 4 incrementos pesan más que 8", "Un cálculo posterior no corrige una muestra que ya no representa al lote."),
    ],
    ctx=("abc", "Un conocido te pide que diseñes con estas reglas de ejemplo el protocolo de muestreo de su faena real. ¿Qué respondes?", "Que las reglas del cuaderno son de ejemplo y que el protocolo real lo fijan personas autorizadas y el laboratorio; lo consultarás con un adulto responsable", "Que sí, si usas el doble del tamaño de partícula", "Que sí, si el lote es pequeño", "Un protocolo real depende del material, del laboratorio y de la norma vigente."),
    sc=[
        ("En el muestreo de un lote: ¿cómo se calcula el número de incrementos?", "Dividiendo las toneladas del lote entre cada cuántas se toma uno", "El número de incrementos depende del tamaño del lote y de la frecuencia."),
        ("En el muestreo de un lote: ¿qué se hace si la masa reunida no alcanza el mínimo?", "Se informa y se ajusta el protocolo por personas autorizadas", "Una muestra bajo el mínimo puede no representar al lote."),
        ("En una reducción de muestra: ¿cómo se calcula la masa tras varias reducciones a la mitad?", "Dividiendo por dos en cada etapa", "Cada etapa deja la mitad de la masa anterior."),
    ],
    op=("Ficha de ejemplo: «Planta Cordón Demo». Lote de 60 toneladas; un incremento cada 15 toneladas; cada incremento pesa 7 kilos. Regla de ejemplo: masa mínima igual a 2 veces el tamaño máximo de partícula en milímetros; el tamaño máximo del lote es 6 mm. Después la muestra se reduce a la mitad hasta 7 kilos. Escribe (a) cuántos incrementos se toman, (b) cuántos kilos se reúnen, (c) cuál es la masa mínima y si se cumple con cuántos kilos de holgura, (d) cuántas reducciones a la mitad se necesitan, (e) qué haces si el lote tuviera partículas de 15 mm.",
        "(a) 60 ÷ 15 = 4 incrementos. (b) 4 × 7 = 28 kg. (c) 2 × 6 = 12 kg; se cumple, con 16 kg de holgura. (d) 28 pasa a 14 y luego a 7: 2 reducciones. (e) La masa mínima sería 2 × 15 = 30 kg, mayor que los 28 kg reunidos; se informa para que personas autorizadas ajusten el protocolo, sin usar la muestra como si fuera representativa.",
        ["calcula bien los incrementos", "calcula bien la masa reunida", "calcula la mínima y la holgura", "calcula bien las reducciones", "concluye que no alcanzaría e informa"],
        ["hoja con las cinco respuestas"],
        ["comparar la masa con las toneladas del lote", "contar mal las reducciones", "ajustar el protocolo por cuenta propia"],
        "Pregunta: «¿qué dos masas comparas para saber si alcanza?». Si no responde, pídele que relea el primer párrafo."),
    reinforce="Inventa un lote, una frecuencia de incrementos y un tamaño de partícula, y calcula la masa reunida y la masa mínima de ejemplo.",
    extend="Explica con un ejemplo por qué una muestra por debajo de la masa mínima puede dar un resultado engañoso.",
)
