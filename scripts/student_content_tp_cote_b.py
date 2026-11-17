"""Terminaciones de la Construcción TP 4.º medio: OAM-04 (protecciones hídricas, cubiertas y evacuación de aguas lluvia), OAM-05 (puertas y ventanas) y OAM-06 (pintura y papeles). Solo conceptos, lectura de documentos y planillas con datos de ejemplo."""
from __future__ import annotations

from tp_cote_common import AVISO, EMER, build

O4 = "TP-COTE-4-OAM-04"
O5 = "TP-COTE-4-OAM-05"
O6 = "TP-COTE-4-OAM-06"

# ============================================================ OAM-04, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Casa ficticia de un piso con techumbre a dos aguas, es decir, dos paños inclinados. Cada paño mide 10 m de largo por 4 m de ancho medido por la inclinación. "
     "Documentos: plano de techumbre (1 lámina), especificaciones técnicas (4 páginas), ficha técnica del fabricante de la cubierta (2 páginas, de ejemplo) y plan de prevención de riesgos (3 páginas). "
     "Riesgos anotados: caída desde altura, corte con bordes de planchas, golpe de calor, viento fuerte y contacto con líneas eléctricas cercanas.")
build(
    O4, 1, F,
    use="Aprenderé qué es una cubierta, para qué sirve la evacuación de aguas lluvia, qué documentos la respaldan y qué riesgos tiene el trabajo en techumbres, sin aprender a instalarla.",
    prior=["Sé leer un plano simple.", "Sé multiplicar y sumar números enteros.", "Sé qué es una lista de riesgos."],
    explain=[
        "En Terminaciones, la cubierta es el material que cubre la parte exterior del techo y evita que pase el agua. La protección hídrica es cualquier material o capa que impide que el agua llegue a zonas interiores. La evacuación de aguas lluvia es el recorrido que sigue el agua para salir de la casa: la canaleta la recoge en el borde del techo y la bajada la conduce hasta el suelo o el desagüe. La pendiente es la inclinación del techo, que ayuda a que el agua corra hacia la canaleta.",
        "Los documentos del trabajo son el plano de techumbre, las especificaciones técnicas, la ficha técnica del fabricante y el plan de prevención de riesgos. El principal riesgo es la caída desde altura; también hay cortes con bordes, golpe de calor, viento y contacto con líneas eléctricas. En la jerarquía de controles, lo más eficaz es evitar trabajar en altura cuando se puede, luego proteger de forma colectiva y por último usar protección personal. Trabajar en un techo exige personal capacitado y autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubierta", "material que cubre el techo por fuera y evita que pase el agua"), ("protección hídrica", "material o capa que impide que el agua llegue a zonas interiores"), ("evacuación de aguas lluvia", "recorrido que sigue el agua de lluvia para salir de la construcción"), ("canaleta", "canal en el borde del techo que recoge el agua"), ("bajada de aguas lluvia", "tubo que conduce el agua desde la canaleta hasta el suelo o el desagüe"), ("pendiente", "inclinación de una superficie"), ("techumbre", "conjunto del techo con su estructura y su cubierta"), ("plano de techumbre", "dibujo que muestra el techo visto desde arriba"), ("ficha técnica del fabricante", "documento con las indicaciones de quien fabrica el producto")],
    worked=[
        ("Elegir el documento", "Una instaladora de ejemplo necesita las indicaciones que da quien fabrica un producto de cubierta. ¿Qué documento consulta?", ["Las indicaciones de quien fabrica están en un documento propio.", "Ese documento es la ficha técnica del fabricante."], "La ficha técnica del fabricante"),
        ("Sumar superficies", "Un techo de ejemplo tiene dos paños de 20 m² cada uno. ¿Cuántos m² tiene en total?", ["Se suman las superficies de los dos paños.", "20 más 20 son 40."], "40 m²"),
    ],
    mistakes=[("Subir al techo «un momento» sin autorización para mirar las planchas.", "La caída desde altura puede causar lesiones graves.", "El trabajo en techos lo hace personal capacitado y autorizado, con las protecciones del plan."),
              ("Creer que leer el plano de techumbre habilita para instalar una cubierta.", "Instalar exige capacitación, autorización y norma vigente.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es la cubierta de una casa?", "El material que cubre el techo por fuera y evita que pase el agua", "El tubo que lleva el agua hasta el suelo", "El dibujo del techo visto desde arriba", "La cubierta es el material exterior del techo; el tubo es la bajada y el dibujo es el plano."),
        ("abc", "¿Qué elemento recoge el agua de lluvia en el borde del techo?", "La canaleta", "La bajada de aguas lluvia", "La ficha técnica", "La canaleta recoge el agua en el borde; la bajada la conduce hacia abajo."),
        ("abc", "Una persona trabaja en el borde de un techo. ¿Cuál es el riesgo principal?", "Caída desde altura", "Pérdida de la ficha técnica", "Aumento del precio de la canaleta", "En el borde de un techo, el principal riesgo es caer desde la altura."),
        ("=", "{F} ¿Cuántos m² de cubierta tienen los dos paños juntos?", "2*10*4", "Se multiplican dos paños por su largo y su ancho inclinado.", " m²"),
        ("abc", "{F} ¿Dónde están las indicaciones de quien fabrica la cubierta?", "En la ficha técnica del fabricante", "En el plano de techumbre", "En el plan de prevención de riesgos", "Las indicaciones del producto están en la ficha técnica; el plano muestra el dibujo del techo."),
        ("abc", "{F} ¿Qué riesgo de la ficha puede producirse por postes o cables cercanos al techo?", "Contacto con líneas eléctricas", "Golpe de calor", "Corte con bordes", "Los cables cercanos pueden provocar contacto con líneas eléctricas, un riesgo de electrocución."),
        ("=", "{F} ¿Cuántas páginas escritas suman las especificaciones, la ficha técnica y el plan de prevención?", "4+2+3", "Se suman las páginas de los tres documentos escritos.", " páginas"),
        ("abc", "{F} Un trabajador sin autorización quiere subir al techo «porque solo es mirar». ¿Qué corresponde?", "No hacerlo: el trabajo en el techo lo hace personal capacitado y autorizado", "Subir si lleva casco", "Subir si el dueño de la casa lo permite", "El casco o el permiso del dueño no reemplazan la capacitación y la autorización."),
        ("abc", "{F} Las especificaciones dicen una cosa sobre la pendiente y la ficha del fabricante dice otra. ¿Qué se hace?", "Anotar la diferencia e informarla al supervisor", "Seguir la ficha sin avisar", "Seguir las especificaciones sin comparar", "Cuando dos documentos se contradicen no se elige uno por cuenta propia: se informa."),
        ("ab", "{F} Una estudiante dice: «ya sé leer el plano de techumbre, así que puedo instalar la cubierta». ¿Qué respuesta es correcta?", "No: leer el plano no habilita; instalar exige personal capacitado y autorizado", "Sí: entender el plano la habilita para instalar", "Leer un plano es distinto de estar autorizada para trabajar en altura."),
        ("abc", "{F} Para reducir el riesgo de caída, ¿qué medida es más eficaz según la jerarquía de controles?", "Evitar trabajar en altura cuando se pueda hacer de otra forma", "Pedir a cada persona que tenga más cuidado", "Entregar un solo casco a cada persona", "Evitar la exposición al peligro es más eficaz que depender del cuidado personal o del EPP."),
        ("=", "{F} Si se compra un 10 % más de superficie de cubierta por posibles recortes, ¿cuántos m² se piden?", "2*10*4*110//100", "Se calcula la superficie total y se multiplica por 110 sobre 100.", " m²"),
        ("abc", "{F} Se anuncia viento fuerte para la tarde. ¿Qué es lo más prudente?", "Informar al prevencionista y no realizar trabajos en el techo con ese viento", "Trabajar rápido antes de que el viento aumente", "Trabajar si hay más personas en el techo", "Con viento fuerte aumenta el riesgo de caída; se informa y se posterga el trabajo en altura."),
    ],
    ctx=("abc", "Una persona cae desde un techo y queda en el suelo sin moverse. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Moverla rápido para ver si despierta", "Subir al techo a revisar qué pasó", "Una caída puede dejar riesgos para quien ayuda; se avisa de inmediato a un adulto responsable y a emergencias."),
    sc=[("En Terminaciones: ¿qué es la bajada de aguas lluvia?", "El tubo que conduce el agua desde la canaleta hasta el suelo o el desagüe", "La bajada lleva el agua; la canaleta la recoge en el borde."),
        ("¿Qué se hace si dos documentos del techo se contradicen?", "Anotar la diferencia e informar al supervisor", "No se elige uno al azar porque podría ser el equivocado."),
        ("¿Quién trabaja en techumbres?", "Personal capacitado y autorizado, con norma vigente", "Este cuaderno no habilita para trabajar en altura.")],
    op=("Casa de ejemplo «Villa Los Aromos»: dos paños de 8 m de largo por 5 m de ancho inclinado; riesgos: caída desde altura y viento fuerte. Escribe (a) cuántos m² de cubierta hay, (b) qué documento tiene las indicaciones del fabricante, (c) una medida para reducir la caída según la jerarquía de controles, (d) quién trabaja en el techo.",
        "(a) 2*8*5 son 80 m². (b) La ficha técnica del fabricante. (c) Evitar trabajar en altura cuando se pueda, o proteger de forma colectiva antes que el EPP. (d) Personal capacitado y autorizado.",
        ["calcula 80 m²", "nombra la ficha técnica", "nombra una medida de la jerarquía", "indica que trabaja personal autorizado"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "poner el EPP como primera medida", "decir que él puede subir al techo"],
        "Pregunta: «¿quién puede subir a un techo?». Si no responde, pídele que relea la regla de autorización."),
    reinforce="Escribe tres documentos de una obra de cubierta y, junto a cada uno, una frase que diga para qué sirve.",
    extend="Explica con un ejemplo inventado por qué una cubierta bien elegida en papel puede ser riesgosa si se instala sin personal autorizado.",
)

# ============================================================ OAM-04, clase 2
F = ("Ficha 2 (extracto de ficha técnica de ejemplo, inventada). Cubierta de planchas onduladas de ejemplo. Largo de una plancha: 3 m. Ancho útil de una plancha, es decir, el ancho que cubre una vez puesta: 1 m. "
     "Pendiente mínima recomendada de ejemplo: 15 cm de desnivel por cada metro horizontal. Los valores son de ejemplo y no son valores reales de ningún fabricante ni norma. "
     "Roles de la obra: el instalador autorizado (ejecuta), el supervisor (revisa y decide si cumple) y el prevencionista (revisa las medidas de seguridad).")
build(
    O4, 2, F,
    use="Aprenderé el vocabulario y los roles de las cubiertas: ancho útil, traslapo, pendiente y ficha técnica.",
    prior=["Sé qué es una cubierta y una canaleta.", "Sé multiplicar y dividir números enteros.", "Sé pasar de centímetros a metros."],
    explain=[
        "El ancho útil de una plancha es el ancho que realmente cubre una vez puesta, porque parte de la plancha queda debajo o encima de la vecina. Esa zona donde una pieza se superpone a otra se llama traslapo. La pendiente se expresa como el desnivel (cuánto sube) por cada metro horizontal. Por ejemplo, 15 cm por metro significa que, por cada metro que avanza el techo en horizontal, sube 15 cm. La ficha técnica del fabricante entrega estos valores para cada producto.",
        "Cada persona tiene un rol. El instalador autorizado ejecuta; el supervisor revisa y decide si el trabajo cumple; el prevencionista revisa las medidas de seguridad. Quien lee la ficha no cambia sus valores: si algo no calza con las especificaciones, lo informa. Los valores reales de pendiente y de traslapo los fijan el fabricante y la norma vigente, no este cuaderno.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("ancho útil", "ancho que cubre una plancha ya puesta, descontado el traslapo"), ("traslapo", "zona donde una pieza se superpone a la siguiente"), ("desnivel", "diferencia de altura entre dos puntos"), ("pendiente", "inclinación; aquí se expresa como desnivel por cada metro horizontal"), ("instalador autorizado", "persona capacitada y autorizada que ejecuta el trabajo"), ("supervisor", "persona que revisa y decide si el trabajo cumple"), ("prevencionista", "persona que revisa las medidas de seguridad")],
    worked=[
        ("Calcular un desnivel", "Una pendiente de ejemplo es 10 cm por metro. ¿Cuántos cm sube el techo en 3 m horizontales?", ["Se multiplica el desnivel por metro por los metros horizontales.", "10 por 3 son 30."], "30 cm"),
        ("Elegir al responsable", "En una obra de ejemplo hay que decidir si el trabajo terminado cumple lo pedido. ¿Quién lo decide?", ["Revisar y decidir si cumple es el rol del supervisor.", "El instalador ejecuta y el prevencionista revisa seguridad."], "El supervisor"),
    ],
    mistakes=[("Usar el largo de la plancha como si fuera su ancho útil.", "Se calculan mal las planchas necesarias.", "Usa el ancho útil que indica la ficha técnica."),
              ("Cambiar la pendiente de la ficha porque «se ve bien».", "Los valores los fijan el fabricante, el proyecto y la norma vigente.", "Anota la diferencia e informa al supervisor.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es el ancho útil de una plancha de cubierta?", "El ancho que cubre la plancha ya puesta, descontado el traslapo", "El ancho de la plancha antes de instalarla", "El largo de la plancha", "El ancho útil descuenta la parte que se superpone a la vecina."),
        ("abc", "El traslapo es:", "La zona donde una pieza se superpone a la siguiente", "El tubo que baja el agua", "La firma del supervisor", "El traslapo es la superposición entre piezas; el tubo es la bajada."),
        ("abc", "Una pendiente de «15 cm por metro» significa que:", "Por cada metro horizontal el techo sube 15 cm", "El techo tiene 15 cm de espesor", "La plancha mide 15 cm de ancho", "La pendiente expresa cuánto sube el techo por cada metro horizontal."),
        ("=", "{F} Con esa pendiente de ejemplo, ¿cuántos cm de desnivel hay en 4 m horizontales?", "4*15", "Se multiplica el desnivel por metro por los metros horizontales.", " cm"),
        ("=", "{F} ¿Cuántos m² cubre el ancho útil de una plancha de 3 m de largo?", "3*1", "Se multiplica el largo de la plancha por su ancho útil.", " m²"),
        ("abc", "{F} Según la ficha, ¿qué ancho considera para calcular cuántas planchas se necesitan a lo ancho?", "El ancho útil de 1 m", "El largo de 3 m", "La pendiente de 15 cm", "Para cubrir un ancho se usa el ancho útil, que ya descuenta el traslapo."),
        ("=", "{F} Un paño mide 6 m de ancho. ¿Cuántas planchas de ancho útil caben a lo ancho?", "6//1", "Se divide el ancho del paño por el ancho útil de una plancha.", " planchas"),
        ("abc", "{F} ¿Quién decide si el trabajo terminado cumple lo pedido?", "El supervisor", "El instalador autorizado que lo ejecutó", "El prevencionista, para toda la obra", "El supervisor revisa y decide si cumple; el prevencionista revisa seguridad."),
        ("abc", "{F} Un instalador sin autorización quiere cambiar la pendiente a 5 cm por metro «para ahorrar material». ¿Qué corresponde?", "No hacerlo: la pendiente la fijan el fabricante y el proyecto; se informa al supervisor", "Hacerlo si el material alcanza", "Hacerlo si el dueño lo aprueba", "La pendiente no se cambia por ahorro; el valor lo fijan el fabricante, el proyecto y la norma vigente."),
        ("ab", "{F} Un compañero dice: «el ancho útil es igual al ancho de la plancha». ¿Qué respuesta es correcta?", "No: el ancho útil descuenta el traslapo con la plancha vecina", "Sí: son siempre iguales", "El ancho útil es menor que el ancho total cuando hay superposición entre planchas."),
        ("abc", "{F} Un techo sube 60 cm en 4 m horizontales. ¿Cumple la pendiente mínima de ejemplo?", "Sí: cumple justo, porque 4 m exigen al menos 60 cm", "No cumple, porque 60 cm es poco", "No se puede saber con esos datos", "La pendiente mínima de ejemplo da 4 por 15, es decir 60 cm, y 60 cm cumple justo."),
        ("=", "{F} Si el techo sube 90 cm en 6 m horizontales, ¿cuántos cm por metro tiene de pendiente?", "90//6", "Se divide el desnivel total por los metros horizontales.", " cm por metro"),
        ("abc", "{F} El prevencionista dice que falta una medida de seguridad en el plan. ¿Qué rol cumple?", "Revisa que las medidas protejan a las personas", "Ejecuta el trabajo de cubierta", "Decide si la cubierta cumple las especificaciones", "El prevencionista revisa las medidas de seguridad; no ejecuta ni aprueba la cubierta."),
    ],
    ctx=("abc", "Un trabajador nuevo propone usar una plancha sin traslapo para ahorrar material. ¿Qué responde un compañero?", "Que consulte al supervisor y a la ficha técnica, porque el traslapo lo fijan el fabricante y el proyecto", "Que está bien si queda bonita", "Que está bien si no llueve esa semana", "El traslapo es una exigencia del producto y del proyecto; no se elimina por ahorro."),
    sc=[("En Terminaciones: ¿qué es el traslapo?", "La zona donde una pieza se superpone a la siguiente", "El traslapo evita pasos de agua entre piezas."),
        ("¿Qué significa una pendiente de 20 cm por metro?", "Que por cada metro horizontal el techo sube 20 cm", "La pendiente se expresa como desnivel por metro horizontal."),
        ("¿Quién revisa que el plan proteja a las personas?", "El prevencionista", "Su rol es revisar las medidas de seguridad.")],
    op=("Ficha de ejemplo «Cubierta Norte»: plancha de 2 m de largo y ancho útil de 1 m; pendiente mínima de ejemplo 12 cm por metro. Un paño mide 5 m horizontales y sube 50 cm. Escribe (a) cuántos m² cubre una plancha, (b) el desnivel mínimo en 5 m, (c) si el paño cumple y por qué, (d) a quién informas.",
        "(a) 2*1 son 2 m². (b) 5*12 son 60 cm. (c) No cumple: sube 50 cm y el mínimo es 60 cm. (d) Al supervisor.",
        ["calcula 2 m²", "calcula 60 cm", "concluye que no cumple", "informa al supervisor"],
        ["hoja con las cuatro respuestas"],
        ["usar el ancho en vez del largo", "aceptar 50 cm", "corregir la pendiente por su cuenta"],
        "Pregunta: «¿cuánto debe subir como mínimo en 5 m?». Si no responde, pídele que multiplique 5 por 12."),
    reinforce="Inventa una pendiente en cm por metro y calcula el desnivel en 2, 4 y 6 m horizontales.",
    extend="Explica por qué el ancho útil de una plancha es menor que su ancho total y cómo afecta al número de planchas.",
)

# ============================================================ OAM-04, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Casa ficticia «Casa Los Ciruelos» con techumbre a dos aguas. Dos paños de 12 m de largo por 5 m de ancho inclinado. "
     "Canaleta en el borde bajo de cada paño, a lo largo de los 12 m. Un compañero hizo este pedido de materiales: 100 m² de cubierta y 12 m de canaleta. "
     "Especificaciones: cubierta para todo el techo y canaleta en ambos bordes bajos. Nota del prevencionista: no hay anclajes ni protecciones colectivas descritos en el plan.")
build(
    O4, 3, F,
    use="Aprenderé a analizar un pedido de materiales frente al plano y las especificaciones, y a detectar faltas del plan de seguridad.",
    prior=["Sé calcular la superficie de un rectángulo.", "Sé comparar lo pedido con lo necesario.", "Sé qué riesgos tiene el trabajo en techos."],
    explain=[
        "Para analizar un pedido de materiales se compara lo pedido con lo que necesita la obra. Primero se calcula lo necesario con el plano: la superficie de la cubierta es el largo por el ancho inclinado de cada paño, sumados. El largo de canaleta es la suma de los bordes bajos donde se recoge el agua. Después se resta lo pedido de lo necesario. Si falta material, se informa antes de comprar; si sobra, también, porque un exceso es un gasto.",
        "El plan de prevención de riesgos también se revisa. Un techo sin protecciones descritas es una no conformidad: significa que algo no cumple lo esperado. Quien analiza el caso no resuelve instalando nada: informa al supervisor y al prevencionista. Los números de este cuaderno son de ejemplo y no reemplazan lo que fija el proyecto.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("pedido de materiales", "lista de lo que se compra para una obra"), ("no conformidad", "algo que no cumple lo esperado o lo pedido"), ("protección colectiva", "medida que protege a varias personas a la vez, como una baranda"), ("anclaje", "punto fijo al que se sujeta un sistema de protección contra caídas"), ("borde bajo", "borde del techo por donde baja el agua hacia la canaleta")],
    worked=[
        ("Comparar pedido y necesidad", "Una obra de ejemplo necesita 50 m² de cubierta y el pedido es de 45 m². ¿Cuánto falta?", ["Se resta lo pedido de lo necesario.", "50 menos 45 son 5."], "Faltan 5 m²"),
        ("Largo de canaleta", "Un techo de ejemplo tiene dos bordes bajos de 8 m cada uno. ¿Cuántos metros de canaleta necesita?", ["Se suman los largos de los bordes bajos.", "8 más 8 son 16."], "16 m"),
    ],
    mistakes=[("Aceptar el pedido porque «parece suficiente» sin calcular.", "La falta se descubre cuando ya se está trabajando.", "Calcula la necesidad con el plano y compárala con lo pedido."),
              ("Resolver una falta del plan de seguridad improvisando una protección.", "Una protección improvisada puede fallar.", "Informa al prevencionista y al supervisor.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es una no conformidad en una obra?", "Algo que no cumple lo esperado o lo pedido", "Un pedido de materiales completo", "El nombre de un paño del techo", "Una no conformidad es un incumplimiento que debe informarse."),
        ("abc", "Una protección colectiva es una medida que:", "Protege a varias personas a la vez", "Protege solo a quien la lleva puesta", "Reemplaza al plan de prevención", "La protección colectiva, como una baranda, cubre a varias personas a la vez."),
        ("abc", "Al analizar un pedido de materiales, lo primero es:", "Calcular lo necesario con el plano y compararlo con lo pedido", "Comprar más por si acaso", "Pedir lo que pidió la obra anterior", "Primero se calcula la necesidad real y luego se compara con el pedido."),
        ("=", "{F} ¿Cuántos m² de cubierta necesita el techo?", "2*12*5", "Se multiplican dos paños por su largo y su ancho inclinado.", " m²"),
        ("=", "{F} ¿Cuántos m² faltan respecto del pedido de 100 m²?", "2*12*5-100", "Se resta lo pedido de lo necesario.", " m²"),
        ("=", "{F} ¿Cuántos metros de canaleta necesita la casa, con una canaleta en cada borde bajo?", "2*12", "Se suman los largos de los dos bordes bajos.", " m"),
        ("=", "{F} ¿Cuántos metros de canaleta faltan en el pedido de 12 m?", "2*12-12", "Se resta lo pedido de lo necesario.", " m"),
        ("abc", "{F} ¿Qué se hace con las faltas del pedido?", "Informarlas al supervisor antes de comprar", "Comprar lo que falta sin avisar", "Ignorarlas porque falta poco", "Una falta se informa para que quien decide corrija el pedido."),
        ("abc", "{F} El prevencionista anota que no hay protecciones descritas. ¿Cómo se clasifica esa situación?", "Como no conformidad del plan de seguridad", "Como un detalle sin importancia", "Como un pedido de más materiales", "Un plan sin protecciones para trabajo en altura incumple lo esperado."),
        ("ab", "{F} Un compañero dice: «yo armo una protección con lo que haya y comenzamos». ¿Qué respuesta es correcta?", "No: se informa al prevencionista; las protecciones las define el plan y las instala personal autorizado", "Sí: una protección improvisada es suficiente", "Una protección improvisada puede fallar; el plan las define y las ejecuta personal autorizado."),
        ("abc", "{F} Si el pedido hubiera sido de 130 m², ¿qué habría sobre lo necesario?", "10 m² de más", "30 m² de más", "Nada, porque coincide", "Lo necesario son 120 m²; 130 menos 120 son 10 m² de más."),
        ("=", "{F} Con la cubierta a $8.000 por m² de ejemplo, ¿cuánto cuesta la cubierta necesaria?", "2*12*5*8000", "Se multiplica la superficie necesaria por el precio por m².", " pesos"),
        ("abc", "{F} El supervisor pide un registro de la diferencia de cubierta. ¿Qué debe contener como mínimo?", "Lo necesario, lo pedido, la diferencia, quién lo detectó y la fecha", "Solo el nombre de quien compró", "Solo el precio de la cubierta", "Un registro útil deja constancia de qué, cuánto, quién y cuándo."),
    ],
    ctx=("abc", "Un proveedor ofrece entregar la cubierta directamente sobre el techo con una escalera «sin que nadie sepa». ¿Qué responde el supervisor?", "Que no: el trabajo en altura exige personal autorizado y el plan de seguridad aprobado", "Que sí, si es rápido", "Que sí, si trae casco", "Una entrega en altura fuera del plan agrega riesgos; no se acepta sin autorización."),
    sc=[("¿Cómo se calcula la superficie de un paño rectangular?", "Largo por ancho inclinado", "La superficie del paño usa el ancho medido por la inclinación."),
        ("¿Qué se hace si el pedido es menor que la necesidad?", "Informar la diferencia antes de comprar", "No se decide solo; se informa a quien corresponde."),
        ("¿Qué es una no conformidad?", "Algo que no cumple lo esperado", "Una no conformidad debe registrarse e informarse al responsable.")],
    op=("Caso de ejemplo «Taller El Álamo»: techo de dos paños de 10 m de largo por 4 m de ancho inclinado; pedido de 70 m² de cubierta y 10 m de canaleta; se necesita canaleta en dos bordes bajos de 10 m; el plan no describe protecciones. Escribe (a) la cubierta necesaria, (b) cuánto falta, (c) cuánta canaleta falta, (d) qué haces con la falta de protecciones y a quién informas.",
        "(a) 2*10*4 son 80 m². (b) 80-70 son 10 m². (c) 2*10-10 son 10 m. (d) La registro como no conformidad e informo al prevencionista y al supervisor; no improviso protecciones.",
        ["calcula 80 m²", "calcula 10 m²", "calcula 10 m", "informa a quien corresponde sin improvisar"],
        ["hoja con las cuatro respuestas"],
        ["olvidar un paño", "improvisar protecciones", "no informar la falta"],
        "Pregunta: «¿cuántos paños tiene el techo?». Si no responde, pídele que relea los datos."),
    reinforce="Inventa un pedido de cubierta y canaleta, calcula lo necesario y escribe cuánto falta o cuánto sobra.",
    extend="Explica por qué un plan de prevención incompleto es una no conformidad aunque el pedido de materiales esté bien calculado.",
)

# ============================================================ OAM-04, clase 4
F = ("Ficha 4 (cálculo de cubierta y evacuación, de ejemplo, inventada). Casa ficticia de dos paños de 8 m de largo por 6 m de ancho inclinado. Plancha de ejemplo: 3 m de largo y 1 m de ancho útil, es decir, 3 m² útiles. "
     "Criterio de ejemplo para la planilla: una bajada de aguas lluvia por cada 24 m² de superficie de cubierta. Pérdida por recortes de ejemplo: 10 %. "
     "Precios de ejemplo: plancha $9.500; bajada $14.000. Pendiente de ejemplo: 15 cm por metro horizontal; el ancho horizontal de cada paño es de 6 m (en este ejemplo se toma igual al ancho inclinado, porque la diferencia es pequeña).")
build(
    O4, 4, F,
    use="Aprenderé a calcular en una planilla la cantidad de planchas, de bajadas y el presupuesto de una cubierta con datos de ejemplo.",
    prior=["Sé calcular superficies y costos.", "Sé sumar un porcentaje de pérdida.", "Sé qué es una pendiente."],
    explain=[
        "El cálculo de una cubierta sigue un orden. Primero, la superficie total: largo por ancho inclinado de cada paño, sumados. Segundo, el número de planchas: la superficie total dividida en los m² útiles de una plancha; si la división no es exacta, se sube al entero siguiente porque no se compran fracciones de plancha. Tercero, la pérdida por recortes: se suma un porcentaje de ejemplo y se vuelve a subir al entero siguiente.",
        "La evacuación de aguas lluvia se calcula con un criterio de ejemplo: cuántos m² de cubierta atiende cada bajada. El número de bajadas es la superficie dividida en ese criterio, subiendo al entero siguiente. Finalmente se arma el presupuesto multiplicando cantidades por precios. Todos los números son de ejemplo; los criterios reales los fijan el fabricante, el proyecto y la norma vigente. La planilla no habilita para instalar nada.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("superficie útil", "superficie que cubre una plancha ya puesta"), ("pérdida por recortes", "material que se desperdicia al cortar y que se suma al pedido"), ("criterio de la planilla", "regla de ejemplo para calcular una cantidad"), ("subir al entero siguiente", "redondear hacia arriba porque no se compran fracciones de pieza")],
    worked=[
        ("Número de planchas", "Un techo de ejemplo tiene 20 m² y cada plancha cubre 3 m² útiles. ¿Cuántas planchas se necesitan?", ["Se divide la superficie por la superficie útil.", "20 dividido en 3 da 6,67: se sube a 7."], "7 planchas"),
        ("Bajadas", "Un techo de ejemplo de 50 m² tiene el criterio de una bajada por cada 20 m². ¿Cuántas bajadas hacen falta?", ["Se divide la superficie por el criterio.", "50 dividido en 20 da 2,5: se sube a 3."], "3 bajadas"),
    ],
    mistakes=[("Redondear hacia abajo el número de planchas.", "Quedaría una parte del techo sin cubierta.", "Si la división no es exacta, sube al entero siguiente."),
              ("Olvidar la pérdida por recortes.", "El pedido alcanza menos de lo calculado.", "Suma el porcentaje de pérdida antes de pedir.")],
    T=[
        ("abc", "En una planilla de cubierta: ¿qué significa «subir al entero siguiente»?", "Redondear hacia arriba porque no se compran fracciones de pieza", "Restar una plancha del pedido", "Dividir el precio por la cantidad", "Si sale 6,2 planchas se piden 7, porque no se compran fracciones."),
        ("abc", "La pérdida por recortes se suma al pedido porque:", "Al cortar las piezas se desperdicia algo de material", "Las planchas aumentan de precio", "El supervisor cobra una comisión", "El recorte genera desperdicio, y el pedido debe cubrirlo."),
        ("abc", "El número de bajadas se calcula con:", "La superficie dividida en lo que atiende cada bajada", "El precio de la bajada dividido en los días", "El largo de la plancha por la pendiente", "Cada bajada atiende una cierta superficie; se divide la superficie total por ella."),
        ("=", "{F} ¿Cuántos m² de cubierta tiene el techo?", "2*8*6", "Se multiplican dos paños por su largo y su ancho inclinado.", " m²"),
        ("=", "{F} ¿Cuántas planchas se necesitan, sin considerar pérdida y subiendo al entero siguiente?", "(2*8*6+2)//3", "Se divide la superficie por 3 m² útiles y se sube al entero siguiente.", " planchas"),
        ("=", "{F} Con la pérdida de ejemplo del 10 % sobre el número de planchas, ¿cuántas se piden, subiendo al entero siguiente?", "(32*110+99)//100", "Se multiplica por 110, se divide en 100 y se sube al entero siguiente.", " planchas"),
        ("=", "{F} ¿Cuánto cuestan las planchas pedidas con pérdida?", "36*9500", "Se multiplican las planchas pedidas por el precio de una.", " pesos"),
        ("=", "{F} ¿Cuántas bajadas hacen falta con el criterio de ejemplo?", "(2*8*6+23)//24", "Se divide la superficie por 24 m² y se sube al entero siguiente.", " bajadas"),
        ("=", "{F} ¿Cuánto cuestan las bajadas?", "4*14000", "Se multiplican las bajadas por su precio.", " pesos"),
        ("=", "{F} ¿Cuántos cm de desnivel tiene cada paño con la pendiente de ejemplo?", "6*15", "Se multiplican los 6 metros horizontales por los cm de desnivel por metro.", " cm"),
        ("abc", "{F} Si el techo tuviera 100 m² en vez de 96 m², ¿cuántas bajadas harían falta?", "5 bajadas", "4 bajadas", "100 bajadas", "100 dividido en 24 da 4,17, y se sube al entero siguiente: 5."),
        ("ab", "{F} Un compañero redondea 4,17 bajadas a 4 «porque es el más cercano». ¿Qué respuesta es correcta?", "Es incorrecto: debe subir a 5, porque con 4 una parte del techo quedaría sin atender", "Es correcto: siempre se redondea al más cercano", "En este tipo de cálculo se sube al entero siguiente, no se redondea al más cercano."),
        ("abc", "{F} Un supervisor pide reducir las bajadas a 3 para ahorrar. ¿Qué corresponde?", "Consultar al proyectista y al fabricante: el criterio no se cambia por ahorro", "Reducirlas si el presupuesto sobra", "Reducirlas si no se ve mal", "El número de bajadas depende de un criterio técnico; no se reduce por ahorro."),
    ],
    ctx=("abc", "Una persona propone medir el techo subiéndose a él «para estar segura» porque no confía en el plano. ¿Qué respuesta es la más prudente?", "Pedir al supervisor las medidas del plano; subir al techo lo hace personal autorizado", "Subir con una escalera prestada", "Subir si hace buen tiempo", "Subir sin autorización agrega riesgo de caída; las medidas se consultan al supervisor."),
    sc=[("Si la división da 6,1 planchas, ¿cuántas se piden?", "7 planchas", "No se compran fracciones, por lo que se sube al entero siguiente."),
        ("¿Para qué sirve el porcentaje de pérdida?", "Para cubrir el material que se desperdicia al recortar", "Se suma al pedido para que alcance."),
        ("¿La planilla habilita para instalar la cubierta?", "No: instala personal autorizado", "Este cuaderno no habilita para trabajar en altura.")],
    op=("Planilla de ejemplo «Bodega Los Cedros»: techo de 60 m²; plancha útil de 3 m²; pérdida de 10 %; plancha $9.000; una bajada por cada 20 m². Escribe (a) las planchas sin pérdida, (b) las planchas con pérdida, (c) el costo de las planchas, (d) las bajadas necesarias.",
        "(a) 60 dividido en 3 son 20. (b) 20 por 110/100 son 22. (c) 22*9.000 = $198.000. (d) 60 dividido en 20 son 3 bajadas.",
        ["calcula 20 planchas", "calcula 22 planchas", "calcula $198.000", "calcula 3 bajadas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la pérdida", "redondear hacia abajo", "mezclar planchas con bajadas"],
        "Pregunta: «¿por qué se suma la pérdida?». Si no responde, pídele que relea el recorte de piezas."),
    reinforce="Calcula las planchas y las bajadas de un techo inventado de 45 m² con plancha útil de 3 m² y una bajada cada 20 m².",
    extend="Explica por qué subir al entero siguiente es más seguro para la obra que redondear al más cercano.",
)

# ============================================================ OAM-05, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Casa ficticia con 3 puertas y 5 ventanas. Documentos: cuadro de puertas y ventanas (1 lámina), planos de detalle (2 láminas), especificaciones técnicas (4 páginas), "
     "ficha técnica del fabricante (3 páginas, de ejemplo) y plan de prevención de riesgos (3 páginas). Cada puerta lleva 3 bisagras y 1 cerradura; cada ventana tiene 2 hojas. "
     "Riesgos anotados: corte con vidrio, aprisionamiento de manos, golpe por caída de una hoja o un marco, sobreesfuerzo al mover piezas pesadas y caída desde altura en ventanas altas.")
build(
    O5, 1, F,
    use="Aprenderé el vocabulario de puertas y ventanas, los documentos que las describen y los riesgos de su instalación, sin aprender a instalarlas.",
    prior=["Sé leer una tabla y un plano simple.", "Sé multiplicar y sumar números enteros.", "Sé qué es un plan de prevención de riesgos."],
    explain=[
        "En una casa, el vano es la abertura que se deja en el muro para una puerta o una ventana. El marco es la estructura fija que se une al vano. La hoja es la parte que se abre y se cierra. La quincallería reúne los herrajes: bisagras, cerraduras, manillas y tiradores. Las ventanas llevan vidrio. El cuadro de puertas y ventanas es una tabla con el código, las medidas y la cantidad de cada tipo; el plano de detalle es un dibujo ampliado que muestra cómo se une una pieza al muro.",
        "El trabajo tiene riesgos: corte con vidrio, aprisionamiento de manos, golpe por la caída de una hoja o un marco, sobreesfuerzo (daño por esfuerzo excesivo al mover piezas pesadas) y caída desde altura en ventanas altas. Manipular vidrios y piezas pesadas exige personal capacitado y autorizado, con las medidas del plan. Primero se busca evitar o reducir el peligro; el EPP, como los guantes, es lo último en la jerarquía de controles.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("vano", "abertura que se deja en el muro para una puerta o una ventana"), ("marco", "estructura fija que se une al vano"), ("hoja", "parte de la puerta o ventana que se abre y se cierra"), ("quincallería", "herrajes como bisagras, cerraduras, manillas y tiradores"), ("cuadro de puertas y ventanas", "tabla con el código, las medidas y la cantidad de cada tipo"), ("plano de detalle", "dibujo ampliado que muestra cómo se une una pieza al muro"), ("sobreesfuerzo", "daño por esfuerzo excesivo al mover una pieza pesada"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Elegir el documento", "Una supervisora de ejemplo quiere saber cuántas ventanas de cada tamaño tiene una casa. ¿Qué documento consulta?", ["Los tamaños y cantidades están en una tabla.", "Esa tabla es el cuadro de puertas y ventanas."], "El cuadro de puertas y ventanas"),
        ("Contar bisagras", "Una casa de ejemplo tiene 4 puertas y cada una lleva 2 bisagras. ¿Cuántas bisagras son?", ["Se multiplican las puertas por las bisagras de cada una.", "4 por 2 son 8."], "8 bisagras"),
    ],
    mistakes=[("Recoger con las manos los trozos de un vidrio roto para «limpiar rápido».", "Los bordes pueden cortar gravemente.", "No te acerques a los trozos y avisa a un adulto responsable."),
              ("Creer que leer el cuadro de puertas y ventanas habilita para instalar.", "Instalar exige capacitación, autorización y norma vigente.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es la quincallería de una puerta?", "Los herrajes, como bisagras, cerraduras y manillas", "La abertura que se deja en el muro", "El vidrio de la ventana", "La quincallería son los herrajes; la abertura es el vano."),
        ("abc", "¿Cómo se llama la abertura que se deja en el muro para una ventana?", "Vano", "Hoja", "Marco", "El vano es la abertura; el marco se une a ella y la hoja se abre y se cierra."),
        ("abc", "Una persona manipula un vidrio de ventana. ¿Qué riesgo corre?", "Corte con vidrio", "Intoxicación por polvo de yeso", "Quemadura por pintura", "El vidrio puede cortar; los otros riesgos no corresponden a esa tarea."),
        ("=", "{F} ¿Cuántas aberturas (puertas y ventanas) tiene la casa?", "3+5", "Se suman las puertas y las ventanas.", " aberturas"),
        ("abc", "{F} ¿Dónde se ven los tamaños y las cantidades de cada puerta y ventana?", "En el cuadro de puertas y ventanas", "En el plan de prevención de riesgos", "En la ficha técnica del fabricante", "El cuadro reúne código, medidas y cantidad; el plan trata la prevención."),
        ("=", "{F} ¿Cuántas bisagras llevan las puertas de la casa en total?", "3*3", "Se multiplican las puertas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuántas hojas de ventana hay en total?", "5*2", "Se multiplican las ventanas por las hojas de cada una.", " hojas"),
        ("abc", "{F} Un trabajador sin autorización quiere colocar un vidrio «porque ya lo hizo antes». ¿Qué corresponde?", "No hacerlo: la manipulación de vidrios la hace personal capacitado y autorizado", "Hacerlo si usa guantes", "Hacerlo si otro compañero lo mira", "Los guantes o un observador no reemplazan la capacitación y autorización."),
        ("abc", "{F} El cuadro dice 5 ventanas y los planos de detalle muestran 4. ¿Qué se hace?", "Anotar la diferencia e informarla al supervisor", "Seguir el cuadro y no avisar", "Seguir los planos de detalle y no avisar", "Si dos documentos se contradicen no se elige uno por cuenta propia: se informa."),
        ("ab", "{F} Una estudiante dice: «ya conozco el cuadro, así que puedo instalar las ventanas». ¿Qué respuesta es correcta?", "No: leer el cuadro no habilita; instalar exige personal capacitado y autorizado", "Sí: conocer el cuadro la habilita para instalar", "Entender un cuadro es distinto de estar autorizada para manipular piezas y vidrios."),
        ("abc", "{F} Hay riesgo de sobreesfuerzo al mover una hoja pesada. ¿Qué es lo más prudente?", "Que la mueva personal capacitado con las ayudas y medidas del plan, no una persona sola", "Que la mueva quien sea más fuerte, sin ayuda", "Que se mueva rápido para que pese menos", "El esfuerzo excesivo daña el cuerpo; el plan define quién y cómo se mueve una pieza pesada."),
        ("=", "{F} ¿Cuántas piezas de quincallería suman las bisagras y las cerraduras de las puertas?", "3*3+3*1", "Se suman las bisagras y las cerraduras de las tres puertas.", " piezas"),
        ("abc", "{F} Para reducir el riesgo de caída desde una ventana alta, ¿qué medida es más eficaz según la jerarquía de controles?", "Evitar o reducir la exposición a la altura antes de confiar en el EPP", "Pedir más cuidado a cada persona", "Entregar guantes a todos", "Evitar la exposición es más eficaz que confiar solo en el cuidado o el EPP."),
    ],
    ctx=("abc", "Una ventana se rompe y una persona se corta; quedan trozos de vidrio en el suelo. ¿Qué se hace según las reglas generales?", "No acercarse a los trozos, avisar a un adulto responsable y a emergencias", "Recoger los trozos con las manos", "Caminar sobre ellos para llegar a la persona", "Acercarse a vidrios rotos puede causar más cortes; se avisa a un adulto responsable y a emergencias."),
    sc=[("En Terminaciones: ¿qué es un vano?", "La abertura que se deja en el muro para una puerta o una ventana", "El marco se une al vano; la hoja se abre y se cierra."),
        ("¿Qué se hace si dos documentos se contradicen?", "Anotar la diferencia e informar al supervisor", "No se elige uno al azar porque podría ser el equivocado."),
        ("¿Quién manipula vidrios y piezas pesadas?", "Personal capacitado y autorizado", "Este cuaderno no habilita para instalar puertas ni ventanas.")],
    op=("Casa de ejemplo «Casa Lomas»: 2 puertas y 4 ventanas; cada puerta lleva 3 bisagras; cada ventana tiene 2 hojas; el cuadro dice 4 ventanas y los planos de detalle dibujan 5. Escribe (a) cuántas aberturas hay, (b) cuántas bisagras, (c) qué haces con la diferencia y a quién informas, (d) un riesgo de la instalación y quién la ejecuta.",
        "(a) 2+4 son 6 aberturas. (b) 2*3 son 6 bisagras. (c) Anoto la diferencia (4 en el cuadro y 5 en los planos) y la informo al supervisor. (d) Corte con vidrio; lo ejecuta personal capacitado y autorizado.",
        ["calcula 6 aberturas", "calcula 6 bisagras", "informa la diferencia sin decidir por su cuenta", "reconoce un riesgo y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["sumar bisagras con hojas", "elegir un documento sin avisar", "decir que él instala"],
        "Pregunta: «¿qué haces si el cuadro y los planos no coinciden?». Si no responde, pídele que relea la regla de informar."),
    reinforce="Escribe los términos vano, marco, hoja y quincallería y, junto a cada uno, una frase que diga qué es.",
    extend="Explica con un ejemplo inventado por qué un cuadro bien leído en papel no basta para manipular vidrios con seguridad.",
)

# ============================================================ OAM-05, clase 2
F = ("Ficha 2 (cuadro de puertas y ventanas, de ejemplo, inventado). Casa ficticia, revisión B. Las medidas son del vano, en cm, ancho por alto. "
     "P1: puerta de entrada, 90 por 200, cantidad 1. P2: puerta interior, 80 por 200, cantidad 2. V1: ventana de 2 hojas, 120 por 100, cantidad 3. V2: ventana de baño de 1 hoja, 60 por 60, cantidad 2. "
     "Holgura de ejemplo entre marco y vano: 1 cm por cada lado. El plano de detalle D-1 muestra la unión de un marco con el muro. Todos los valores son de ejemplo y no son valores reales de ninguna norma.")
build(
    O5, 2, F,
    use="Aprenderé a leer un cuadro de puertas y ventanas: códigos, medidas del vano, holgura, cantidades y revisión.",
    prior=["Sé qué es un vano, un marco y una hoja.", "Sé multiplicar y restar números enteros.", "Sé leer una tabla."],
    explain=[
        "El cuadro de puertas y ventanas da, para cada tipo, un código, las medidas del vano (ancho por alto) y la cantidad. Las medidas del vano son las de la abertura del muro, no las del marco. Entre el marco y el vano se deja una holgura: un pequeño espacio por cada lado que permite colocar la pieza. Por eso el marco mide menos que el vano: ancho del marco = ancho del vano menos dos holguras; lo mismo con el alto.",
        "Dos conceptos ayudan a verificar el resultado en una lista de chequeo: el aplomo, que significa que una pieza queda perfectamente vertical, y el nivel, que significa que queda perfectamente horizontal. También se revisa la revisión del cuadro (su versión vigente, identificada con una letra). El supervisor decide si el trabajo cumple; quien lee el cuadro no cambia sus medidas. Las medidas reales las fija el proyecto, no este cuaderno.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("código", "letra y número que identifica un tipo de puerta o ventana, como V1"), ("holgura", "espacio que se deja entre el marco y el vano"), ("aplomo", "condición de una pieza que queda perfectamente vertical"), ("nivel", "condición de una pieza que queda perfectamente horizontal"), ("revisión", "versión del cuadro o plano, identificada con una letra"), ("vano", "abertura en el muro para una puerta o ventana"), ("marco", "estructura fija que se une al vano")],
    worked=[
        ("Medida del marco", "Un vano de ejemplo mide 100 cm de ancho y la holgura de ejemplo es 2 cm por lado. ¿Cuánto mide el ancho del marco?", ["Se restan dos holguras del ancho del vano.", "100 menos 2 por 2 son 96."], "96 cm"),
        ("Total de piezas", "Un cuadro de ejemplo tiene 2 ventanas tipo A y 3 tipo B. ¿Cuántas ventanas hay?", ["Se suman las cantidades de cada tipo.", "2 más 3 son 5."], "5 ventanas"),
    ],
    mistakes=[("Pedir un marco con la misma medida que el vano.", "No cabría en la abertura por falta de holgura.", "Descuenta dos holguras del ancho y del alto del vano."),
              ("Usar una revisión antigua del cuadro «porque es la que tenía impresa».", "La revisión antigua puede tener otras medidas.", "Comprueba la letra de la revisión y usa la vigente.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es la holgura entre marco y vano?", "El espacio que se deja entre el marco y el vano", "El grosor del vidrio", "La cantidad de bisagras de una puerta", "La holgura es un espacio por cada lado que permite colocar el marco."),
        ("abc", "Una pieza que queda perfectamente vertical tiene:", "Aplomo", "Nivel", "Holgura", "El aplomo es la verticalidad; el nivel es la horizontalidad."),
        ("abc", "Las medidas de un cuadro de puertas y ventanas corresponden a:", "El vano, es decir, la abertura del muro", "El vidrio solamente", "El marco ya instalado", "El cuadro de este ejemplo da las medidas del vano; el marco es menor."),
        ("=", "{F} ¿Cuántas ventanas hay en total?", "3+2", "Se suman las ventanas V1 y V2.", " ventanas"),
        ("=", "{F} ¿Cuántas puertas hay en total?", "1+2", "Se suman las puertas P1 y P2.", " puertas"),
        ("abc", "{F} ¿Qué código tiene la ventana de baño?", "V2", "V1", "P2", "V2 es la ventana de baño de 1 hoja; V1 tiene 2 hojas y P2 es una puerta interior."),
        ("=", "{F} ¿Cuánto mide, en cm, el ancho del marco de V1?", "120-2*1", "Se restan dos holguras de 1 cm del ancho del vano.", " cm"),
        ("=", "{F} ¿Cuánto mide, en cm, el alto del marco de P2?", "200-2*1", "Se restan dos holguras de 1 cm del alto del vano.", " cm"),
        ("=", "{F} ¿Cuántas hojas de ventana hay en total, con 2 hojas en V1 y 1 hoja en V2?", "3*2+2*1", "Se multiplican las ventanas de cada tipo por sus hojas y se suman.", " hojas"),
        ("ab", "{F} Un compañero dice: «como el vano de P1 mide 90 cm de ancho, el marco también puede medir 90». ¿Qué respuesta es correcta?", "No: el marco debe descontar las holguras y medir menos que el vano", "Sí: el marco debe medir lo mismo que el vano", "El marco necesita holgura para entrar en el vano, por lo que mide menos."),
        ("abc", "{F} ¿Dónde se ve cómo se une un marco al muro?", "En el plano de detalle D-1", "En el cuadro de puertas y ventanas", "En el plan de prevención de riesgos", "El plano de detalle muestra la unión; el cuadro da códigos, medidas y cantidades."),
        ("abc", "{F} Llega una copia del cuadro en revisión A, pero la vigente es la B. ¿Qué se hace?", "Usar la revisión B y avisar que circula una copia antigua", "Usar la A porque ya está impresa", "Mezclar medidas de ambas", "Debe usarse la revisión vigente y se informa sobre la copia desactualizada."),
        ("abc", "{F} ¿Quién decide si una puerta ya instalada cumple las especificaciones?", "El supervisor", "El que leyó el cuadro", "El proveedor del marco", "El supervisor revisa y decide si el trabajo cumple."),
    ],
    ctx=("abc", "Un trabajador nuevo ve que un vano parece más chico que el del cuadro y propone ensanchar el muro por su cuenta. ¿Qué responde un compañero?", "Que informe al supervisor, porque modificar el muro no le corresponde", "Que lo ensanche rápido antes de que llegue el marco", "Que lo ensanche si tiene herramientas", "Cambiar un muro afecta la obra; se informa y lo decide quien corresponde."),
    sc=[("En Terminaciones: ¿qué es el aplomo?", "La condición de una pieza que queda perfectamente vertical", "El nivel, en cambio, es la horizontalidad."),
        ("Si un vano mide 90 cm y la holgura es 1 cm por lado, ¿cuánto mide el marco?", "88 cm", "Se restan dos holguras de 1 cm."),
        ("¿Qué revisión del cuadro se usa?", "La vigente", "Una revisión antigua puede tener medidas distintas.")],
    op=("Cuadro de ejemplo, revisión C: V3, ventana de 2 hojas, 140 por 110, cantidad 4; P3, puerta de 85 por 200, cantidad 2; holgura de ejemplo 1 cm por lado. Escribe (a) cuántas aberturas hay, (b) el ancho del marco de V3, (c) el alto del marco de P3, (d) qué revisión usas si llega una copia en revisión B.",
        "(a) 4+2 son 6 aberturas. (b) 140-2 son 138 cm. (c) 200-2 son 198 cm. (d) La C, que es la vigente; aviso que circula una copia antigua.",
        ["calcula 6 aberturas", "calcula 138 cm", "calcula 198 cm", "usa la revisión vigente"],
        ["hoja con las cuatro respuestas"],
        ["no restar las holguras", "usar la revisión B", "sumar mal las aberturas"],
        "Pregunta: «¿cuántas holguras se restan?». Si no responde, pídele que dibuje el vano con un espacio a cada lado."),
    reinforce="Con un vano inventado de 110 por 130 cm y holgura de 1 cm por lado, calcula el ancho y el alto del marco.",
    extend="Explica por qué se deja holgura y por qué el cuadro de ejemplo da las medidas del vano y no las del marco.",
)

# ============================================================ OAM-05, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Casa ficticia, cuadro revisión B (medidas del vano en cm): P2 puerta interior 80 por 200, cantidad 2; V1 ventana de 2 hojas 120 por 100, cantidad 3. "
     "Pedido al proveedor hecho por un compañero: 2 puertas con marco de 90 cm de ancho; 4 ventanas con marco de 118 cm de ancho. Holgura de ejemplo: 1 cm por cada lado. "
     "Precio de ejemplo de una ventana V1: $55.000. Nota: el plan de prevención no describe cómo se moverán los vidrios dentro de la obra.")
build(
    O5, 3, F,
    use="Aprenderé a comparar un pedido de puertas y ventanas con el cuadro, detectar diferencias y registrar faltas del plan de seguridad.",
    prior=["Sé leer un cuadro de puertas y ventanas.", "Sé calcular la medida del marco con la holgura.", "Sé qué es una no conformidad."],
    explain=[
        "Para analizar un pedido, se calcula primero lo que el cuadro necesita y se compara con lo pedido. Cada pieza pedida debe tener el código correcto, la cantidad correcta y la medida correcta. La medida del marco se calcula descontando dos holguras al vano. Si un marco pedido es más ancho que lo calculado, no cabe; si la cantidad pedida es mayor, hay exceso y gasto; si es menor, faltan piezas.",
        "También se revisa el plan de seguridad. Si el plan no dice cómo se mueven los vidrios dentro de la obra, es una no conformidad: algo que no cumple lo esperado. Quien analiza el caso no corrige en terreno: registra, informa al supervisor y al prevencionista, y espera la decisión. Los números de este cuaderno son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("pedido", "lista de piezas que se encarga al proveedor"), ("exceso", "cantidad pedida mayor que la necesaria"), ("faltante", "cantidad necesaria que no se pidió"), ("no conformidad", "algo que no cumple lo esperado"), ("proveedor", "empresa de ejemplo que vende las piezas")],
    worked=[
        ("Exceso", "Un cuadro de ejemplo pide 5 ventanas y el pedido es de 6. ¿Cuántas sobran?", ["Se resta lo necesario de lo pedido.", "6 menos 5 es 1."], "1 ventana de más"),
        ("Medida del marco", "Un vano de ejemplo mide 90 cm y la holgura es 1 cm por lado. ¿Cuánto debe medir el marco?", ["Se restan dos holguras.", "90 menos 2 son 88."], "88 cm"),
    ],
    mistakes=[("Aceptar el pedido porque «las medidas se parecen».", "Una diferencia de pocos cm puede impedir instalar la pieza.", "Calcula la medida del marco y compárala con lo pedido."),
              ("Resolver una falta del plan de seguridad improvisando una forma de mover los vidrios.", "La improvisación puede causar cortes o caídas de piezas.", "Informa al prevencionista y al supervisor.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es un exceso en un pedido?", "Una cantidad pedida mayor que la necesaria", "Una pieza con la medida correcta", "Una pieza que falta", "El exceso es lo pedido sobre lo necesario; lo que falta se llama faltante."),
        ("abc", "Un faltante es:", "Una cantidad necesaria que no se pidió", "Una pieza con holgura", "Un marco instalado", "El faltante es lo necesario que no está en el pedido."),
        ("abc", "Al revisar un pedido, ¿qué debe tener cada pieza?", "Código, cantidad y medida correctos", "Solo el código", "Solo el precio", "Cada pieza se verifica en código, cantidad y medida."),
        ("=", "{F} ¿Cuánto debe medir, en cm, el ancho del marco de las puertas P2?", "80-2*1", "Se restan dos holguras del ancho del vano.", " cm"),
        ("=", "{F} ¿Cuántos cm más ancho es el marco pedido para las puertas que el marco calculado?", "90-(80-2*1)", "Se resta el ancho calculado del ancho pedido.", " cm"),
        ("abc", "{F} ¿Qué pasa con las puertas pedidas, con marco de 90 cm, en un vano de 80 cm?", "No caben: el marco es más ancho que el vano", "Caben justo", "Caben con holgura de sobra", "Un marco de 90 cm no cabe en un vano de 80 cm."),
        ("abc", "{F} ¿Qué se concluye de los marcos de 118 cm pedidos para V1?", "Están correctos: 120 menos dos holguras de 1 cm da 118", "Están mal: deberían medir 120", "Están mal: deberían medir 122", "El ancho del marco es 120 menos 2, es decir 118 cm."),
        ("=", "{F} ¿Cuántas ventanas V1 se pidieron de más?", "4-3", "Se resta lo necesario de lo pedido.", " ventanas"),
        ("=", "{F} ¿Cuánto cuesta ese exceso con el precio de ejemplo?", "(4-3)*55000", "Se multiplica el exceso por el precio de una ventana.", " pesos"),
        ("ab", "{F} Un compañero dice: «da lo mismo que sobre una ventana, la guardamos». ¿Qué respuesta es correcta?", "No: el exceso es un gasto y se informa al supervisor antes de recibir el pedido", "Sí: un exceso nunca es un problema", "Una pieza de más cuesta dinero y se informa; el supervisor decide qué hacer."),
        ("abc", "{F} El plan no describe cómo se moverán los vidrios. ¿Cómo se clasifica?", "Como una no conformidad del plan de seguridad", "Como un exceso del pedido", "Como un detalle sin importancia", "Un plan que omite una medida necesaria incumple lo esperado."),
        ("abc", "{F} Un compañero propone mover los vidrios entre dos personas «como se pueda» mientras llega el plan. ¿Qué corresponde?", "No hacerlo: se informa al prevencionista y se espera una medida definida y autorizada", "Hacerlo si usan guantes", "Hacerlo si es de día", "Improvisar con vidrios puede causar cortes; se espera una medida definida por el plan."),
        ("abc", "{F} El supervisor pide un registro de las diferencias del pedido. ¿Qué debe contener como mínimo?", "Qué pieza, qué dice el cuadro, qué dice el pedido, quién lo detectó y la fecha", "Solo el precio de cada pieza", "Solo la firma del proveedor", "Un registro útil deja constancia de qué, cuánto, quién y cuándo."),
    ],
    ctx=("abc", "Un proveedor entrega un vidrio con una esquina astillada y un trabajador propone usarlo igual «porque casi no se nota». ¿Qué responde un compañero?", "Que informe al supervisor, porque una pieza dañada es una no conformidad y puede ser peligrosa", "Que lo use si lo coloca con cuidado", "Que lo use si nadie lo ve", "Una pieza astillada puede romperse o cortar; se informa y se rechaza o cambia según decida el supervisor."),
    sc=[("¿Cómo se calcula el ancho del marco?", "Ancho del vano menos dos holguras", "Se descuenta la holgura de cada lado."),
        ("¿Qué se hace con un exceso en el pedido?", "Informar al supervisor antes de recibir", "Un exceso es un gasto que debe decidirse."),
        ("¿Quién corrige los problemas en terreno?", "Personal autorizado, decidido por el supervisor", "Quien analiza en papel informa y no corrige.")],
    op=("Caso de ejemplo «Casa Quillota»: cuadro: V4 ventana 100 por 100, cantidad 5; holgura 1 cm por lado; pedido: 6 ventanas con marco de 100 cm. Escribe (a) cuánto debe medir el marco, (b) cuántas ventanas sobran, (c) qué problema tiene el marco pedido, (d) a quién informas.",
        "(a) 100-2 son 98 cm. (b) 6-5 es 1 ventana. (c) Es más ancho de lo calculado: puede no caber con holgura. (d) Al supervisor.",
        ["calcula 98 cm", "calcula 1 ventana", "describe el problema del marco", "informa al supervisor"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la holgura", "decir que no sobra ninguna", "corregir el pedido por su cuenta"],
        "Pregunta: «¿cuántos cm se descuentan en total?». Si no responde, pídele que multiplique la holgura por 2."),
    reinforce="Inventa un cuadro de dos tipos de ventana y un pedido con una diferencia; escribe qué exceso o falta hay.",
    extend="Explica por qué un marco apenas más ancho que lo calculado puede impedir instalar la pieza.",
)

# ============================================================ OAM-05, clase 4
F = ("Ficha 4 (presupuesto de puertas y ventanas, de ejemplo, inventado). Casa ficticia con 10 ventanas de 2 m de ancho por 1 m de alto, con un vidrio por ventana, y 6 puertas. "
     "Vidrio: $18.000 por m². Pérdida de ejemplo en vidrios por quiebres y recortes de pedido: 10 %. Quincallería de ejemplo: cada puerta lleva 3 bisagras a $1.200 cada una y 1 cerradura a $8.500. "
     "Todos los precios, medidas y porcentajes son de ejemplo y no son valores reales.")
build(
    O5, 4, F,
    use="Aprenderé a cubicar y presupuestar vidrios y quincallería en una planilla con datos de ejemplo.",
    prior=["Sé calcular el área de un rectángulo.", "Sé sumar un porcentaje.", "Sé multiplicar cantidades por precios."],
    explain=[
        "Cubicar vidrios es calcular su superficie en metros cuadrados: ancho por alto de cada vidrio, multiplicado por la cantidad. Como el vidrio puede quebrarse o necesitar un pedido con exceso, se suma un porcentaje de pérdida de ejemplo. Para la quincallería se cuentan las piezas por puerta o ventana y se multiplican por la cantidad de puertas o ventanas. Cada partida del presupuesto es una cantidad por un precio unitario; el total es la suma de las partidas.",
        "Todos los valores son de ejemplo: los reales los fija el proyecto, el fabricante y el mercado. Una planilla ayuda a presupuestar y pedir, pero no habilita para manipular vidrios ni para instalar piezas, tareas que hace personal capacitado y autorizado con las medidas del plan de prevención.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("cubicar", "calcular la cantidad de material que necesita una obra"), ("partida", "tarea o producto del presupuesto con su cantidad y su precio unitario"), ("precio unitario", "precio por cada unidad de medida o por cada pieza"), ("pérdida", "material que se agrega al pedido por quiebres y recortes"), ("subtotal", "costo de una partida: cantidad por precio unitario")],
    worked=[
        ("Superficie de vidrio", "Un vidrio de ejemplo mide 3 m de ancho por 2 m de alto y hay 2 iguales. ¿Cuántos m² son?", ["Se multiplica ancho por alto y por la cantidad.", "3 por 2 son 6 y 6 por 2 son 12."], "12 m²"),
        ("Subtotal de quincallería", "Una partida de ejemplo tiene 20 manillas a $2.000 cada una. ¿Cuál es el subtotal?", ["Se multiplica la cantidad por el precio unitario.", "20 por 2.000 son 40.000."], "$40.000"),
    ],
    mistakes=[("Olvidar la pérdida al pedir los vidrios.", "Un quiebre deja la obra sin la pieza necesaria.", "Suma el porcentaje de pérdida de ejemplo al pedido."),
              ("Multiplicar las bisagras por las ventanas en vez de por las puertas.", "Se cuenta una pieza que no corresponde.", "Multiplica cada pieza por el elemento al que pertenece.")],
    T=[
        ("abc", "En Terminaciones: ¿qué significa cubicar vidrios?", "Calcular la superficie de vidrio que se necesita, en m²", "Cortar los vidrios a medida", "Colocar los vidrios en los marcos", "Cubicar es calcular cantidades; cortar y colocar son trabajos que no se enseñan aquí."),
        ("abc", "En puertas y ventanas: el subtotal de una partida se calcula como:", "Cantidad por precio unitario", "Cantidad más precio unitario", "Precio unitario menos la pérdida", "Cada unidad cuesta su precio; el subtotal multiplica por la cantidad."),
        ("abc", "La pérdida se suma al pedido de vidrios porque:", "Pueden quebrarse o recortarse algunas piezas", "El vidrio se vuelve más pesado", "El supervisor lo exige siempre", "El quiebre o el recorte puede dejar piezas inservibles; el pedido debe cubrirlo."),
        ("=", "{F} ¿Cuántos m² de vidrio hay en las 10 ventanas?", "10*2*1", "Se multiplican ancho, alto y cantidad de ventanas.", " m²"),
        ("=", "{F} Con la pérdida de ejemplo del 10 %, ¿cuántos m² de vidrio se piden?", "10*2*1*110//100", "Se multiplica la superficie por 110 sobre 100.", " m²"),
        ("=", "{F} ¿Cuánto cuesta el vidrio pedido?", "22*18000", "Se multiplican los m² pedidos por el precio por m².", " pesos"),
        ("=", "{F} ¿Cuántas bisagras se necesitan para las puertas?", "6*3", "Se multiplican las puertas por las bisagras de cada una.", " bisagras"),
        ("=", "{F} ¿Cuánto cuestan todas las bisagras?", "6*3*1200", "Se multiplican las bisagras por su precio unitario.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan todas las cerraduras?", "6*8500", "Se multiplican las cerraduras por su precio unitario.", " pesos"),
        ("=", "{F} ¿Cuál es el total de vidrio, bisagras y cerraduras?", "22*18000+6*3*1200+6*8500", "Se suman los subtotales de las tres partidas.", " pesos"),
        ("abc", "{F} Si el porcentaje de pérdida de ejemplo fuera 20 %, ¿qué ocurriría con los m² pedidos?", "Aumentarían", "Disminuirían", "Quedarían igual", "A mayor pérdida, más material se pide."),
        ("ab", "{F} Un compañero propone no sumar pérdida «porque los vidrios no se rompen». ¿Qué respuesta es correcta?", "No es prudente: puede haber quiebres y recortes, y el pedido debe cubrirlos", "Es correcto: nunca hay pérdida", "Una planilla debe prever pérdidas; omitirlas puede dejar la obra sin material."),
        ("abc", "{F} Un supervisor pide que el instalador «ayude» a descargar los vidrios aunque no esté autorizado. ¿Qué corresponde?", "Recordar que la manipulación de vidrios la hace personal capacitado y autorizado", "Descargarlos si son pocos", "Descargarlos si usa guantes", "Los guantes o la cantidad no reemplazan la autorización para manipular vidrios."),
    ],
    ctx=("abc", "El proveedor ofrece rebajar el precio si se pide menos vidrio del que dice la planilla. ¿Qué corresponde?", "Consultar al supervisor: no se reduce el pedido sin revisar la cubicación", "Aceptar, porque cuesta menos", "Aceptar si el vidrio parece alcanzar", "Reducir el pedido puede dejar piezas sin cubrir; se revisa con quien decide."),
    sc=[("¿Cómo se calcula la superficie de un vidrio rectangular?", "Ancho por alto", "Se multiplican sus dos medidas, el ancho y el alto."),
        ("Si una partida tiene 8 piezas a $500 cada una, ¿cuál es el subtotal?", "$4.000", "Se multiplican la cantidad y el precio unitario."),
        ("¿La planilla habilita para manipular vidrios?", "No: lo hace personal capacitado y autorizado", "Este cuaderno no habilita para trabajar.")],
    op=("Planilla de ejemplo «Taller Lago»: 5 ventanas de 3 m de ancho por 1 m de alto, un vidrio cada una; pérdida de ejemplo del 20 %; vidrio $15.000 por m²; 4 puertas con 2 bisagras a $1.500 cada una. Escribe (a) los m² de vidrio sin pérdida, (b) los m² pedidos con pérdida, (c) el costo del vidrio pedido y (d) el costo de las bisagras.",
        "(a) 5*3*1 son 15 m². (b) 15*120/100 son 18 m². (c) 18*15.000 = $270.000. (d) 4*2*1.500 = $12.000.",
        ["calcula 15 m²", "calcula 18 m²", "calcula $270.000", "calcula $12.000"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la pérdida", "multiplicar las bisagras por las ventanas", "sumar en vez de multiplicar"],
        "Pregunta: «¿cómo se suma el 20 % de pérdida?». Si no responde, pídele que multiplique por 120 y divida en 100."),
    reinforce="Inventa una planilla con 4 vidrios de 2 por 1 m y calcula los m², el pedido con 10 % de pérdida y el costo a $12.000 por m².",
    extend="Explica por qué dos casas con el mismo número de ventanas pueden necesitar distintas cantidades de vidrio.",
)

# ============================================================ OAM-06, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Sala ficticia de una casa que será pintada. Documentos: especificaciones técnicas (3 páginas), ficha técnica del producto de ejemplo (2 páginas), "
     "ficha de datos de seguridad del producto, FDS (4 páginas) y plan de prevención de riesgos (3 páginas). Producto: pintura de ejemplo en envases de 4 litros; hay 12 envases en la bodega. "
     "La etiqueta del envase trae un pictograma de advertencia y la frase «mantener ventilado» (de ejemplo). Riesgos anotados: inhalación de vapores, contacto con la piel y los ojos, incendio por productos inflamables y mezclas indebidas de productos.")
build(
    O6, 1, F,
    use="Aprenderé qué documentos y señales avisan los riesgos de los productos de pintura y de papeles, y qué reglas generales evitan accidentes, sin aprender a aplicarlos.",
    prior=["Sé leer una etiqueta simple.", "Sé multiplicar y sumar números enteros.", "Sé qué es un plan de prevención de riesgos."],
    explain=[
        "En Terminaciones, pintar es cubrir una superficie (un muro o un cielo) con una capa de producto, y colocar papeles es cubrirla con rollos de papel. Muchos productos son químicos y tienen riesgos. La etiqueta del envase trae el nombre, los pictogramas (símbolos que avisan un peligro) y frases de advertencia. La ficha de datos de seguridad, FDS, es un documento más completo que dice qué riesgos tiene el producto y qué medidas generales se recomiendan. La ficha técnica, en cambio, dice cómo rinde y para qué sirve el producto.",
        "Los riesgos principales son la inhalación de vapores, el contacto con la piel y los ojos, el incendio de productos inflamables y las mezclas indebidas, que pueden producir reacciones peligrosas. Reglas generales: no mezclar productos, no pasarlos a envases sin rótulo, leer la etiqueta y la FDS, mantener la ventilación y alejar los productos de fuentes de calor. En la jerarquía de controles es mejor reemplazar un producto por otro menos peligroso, si el proyecto lo permite, que depender de mascarillas. Usar productos exige personal capacitado y autorizado.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("superficie", "muro, cielo o piso sobre el que se aplica un producto o un papel"), ("etiqueta", "rótulo del envase con el nombre del producto, los pictogramas y las advertencias"), ("pictograma", "símbolo que avisa un peligro"), ("FDS", "ficha de datos de seguridad: documento que explica los riesgos de un producto y medidas generales"), ("ficha técnica", "documento que dice para qué sirve un producto y cómo rinde"), ("ventilación", "renovación del aire de un recinto"), ("inflamable", "que se enciende con facilidad"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Elegir el documento", "Una supervisora de ejemplo quiere saber qué riesgos tiene un producto y qué medidas generales se recomiendan. ¿Qué documento consulta?", ["Los riesgos y medidas generales están en un documento propio.", "Ese documento es la ficha de datos de seguridad (FDS)."], "La ficha de datos de seguridad (FDS)"),
        ("Contar litros", "Una bodega de ejemplo tiene 5 envases de 4 litros. ¿Cuántos litros hay?", ["Se multiplican los envases por los litros de cada uno.", "5 por 4 son 20."], "20 litros"),
    ],
    mistakes=[("Pasar un producto a una botella sin rótulo «para usarlo más fácil».", "Nadie sabrá qué contiene ni qué riesgos tiene.", "Guarda los productos en su envase original con la etiqueta visible."),
              ("Mezclar dos productos «para que rindan más».", "Puede producir vapores o reacciones peligrosas.", "No mezcles productos; sigue las indicaciones del fabricante y de la FDS.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es la FDS de un producto?", "Un documento que explica sus riesgos y medidas generales de seguridad", "La lista de precios del producto", "El dibujo del muro donde se usa", "La FDS informa riesgos y medidas; los precios y el dibujo están en otros documentos."),
        ("abc", "El símbolo de una etiqueta que avisa un peligro se llama:", "Pictograma", "Superficie", "Rendimiento", "El pictograma es un símbolo de advertencia; la superficie es donde se aplica el producto."),
        ("abc", "Una persona trabaja en un recinto cerrado con un producto que desprende vapores. ¿Qué riesgo corre?", "Inhalación de vapores", "Corte con vidrio", "Atropello por el producto", "Los vapores en un recinto mal ventilado pueden inhalarse."),
        ("=", "{F} ¿Cuántos litros de pintura hay en la bodega?", "12*4", "Se multiplican los envases por los litros de cada uno.", " litros"),
        ("abc", "{F} ¿Dónde se ven los riesgos del producto y las medidas generales?", "En la ficha de datos de seguridad (FDS)", "En la ficha técnica", "En las especificaciones técnicas", "La FDS describe riesgos y medidas; la ficha técnica indica uso y rendimiento."),
        ("abc", "{F} Un compañero propone mezclar dos productos distintos «para que rindan más». ¿Qué corresponde?", "No hacerlo: mezclar productos puede producir reacciones peligrosas", "Hacerlo si el color queda parecido", "Hacerlo si usa guantes", "Mezclar productos no está permitido; los guantes no evitan una reacción."),
        ("=", "{F} ¿Cuántas páginas escritas suman los cuatro documentos?", "3+2+4+3", "Se suman las páginas de las especificaciones, la ficha técnica, la FDS y el plan.", " páginas"),
        ("abc", "{F} Una persona sin capacitación quiere usar el producto «porque es solo pintura». ¿Qué corresponde?", "No hacerlo: el uso de productos químicos exige personal capacitado y autorizado", "Hacerlo si el envase dice «mantener ventilado»", "Hacerlo si el dueño de la casa lo pide", "La frase de la etiqueta o el permiso del dueño no reemplazan la capacitación."),
        ("abc", "{F} Las especificaciones nombran un producto y la ficha técnica corresponde a otro distinto. ¿Qué se hace?", "Anotar la diferencia e informar al supervisor", "Usar el producto de la ficha sin avisar", "Usar el de las especificaciones sin comparar", "Cuando dos documentos se contradicen no se elige uno por cuenta propia."),
        ("ab", "{F} Una estudiante dice: «leí la FDS, entonces ya puedo usar el producto». ¿Qué respuesta es correcta?", "No: leer la FDS no habilita; usar el producto exige personal capacitado y autorizado", "Sí: leer la FDS la habilita para usarlo", "Leer un documento es distinto de estar capacitada y autorizada para trabajar con productos."),
        ("abc", "{F} Para reducir el riesgo de inhalar vapores, ¿qué medida es más eficaz según la jerarquía de controles?", "Reemplazar el producto por otro menos peligroso, si el proyecto lo permite", "Pedir a cada persona que aguante la respiración", "Confiar solo en una mascarilla", "Reducir el peligro en su origen es más eficaz que depender solo del EPP."),
        ("=", "{F} Si se usan 3 envases en la semana, ¿cuántos litros quedan en la bodega?", "(12-3)*4", "Se restan los envases usados y se multiplican los que quedan por 4.", " litros"),
        ("abc", "{F} Aparece un envase sin etiqueta. ¿Qué es lo más prudente?", "No usarlo e informar al supervisor", "Usarlo si se parece a los otros", "Mezclarlo con otro para identificarlo", "Sin etiqueta no se conocen los riesgos del contenido; no se usa ni se mezcla."),
    ],
    ctx=("abc", "Una persona se marea y le lloran los ojos tras entrar a una pieza con olor fuerte a producto. ¿Qué se hace según las reglas generales?", "Alejarse de la zona de riesgo, avisar a un adulto responsable y a emergencias", "Volver a entrar a terminar el trabajo", "Esperar sin avisar a nadie", "Permanecer en la zona puede empeorar el efecto; se avisa de inmediato a un adulto responsable y a emergencias."),
    sc=[("En Terminaciones: ¿qué es la etiqueta de un envase?", "El rótulo con el nombre, los pictogramas y las advertencias", "La etiqueta debe estar visible y no se retira."),
        ("¿Se pueden mezclar productos para ahorrar?", "No", "Mezclar productos puede producir reacciones peligrosas para las personas."),
        ("¿Quién usa productos químicos de la obra?", "Personal capacitado y autorizado", "Este cuaderno no habilita para trabajar con productos.")],
    op=("Bodega de ejemplo «Obra Los Pinos»: 8 envases de 4 litros; documentos: especificaciones (2 páginas), FDS (3 páginas) y plan (2 páginas). Un compañero propone pasar el contenido de un envase a una botella sin rótulo. Escribe (a) cuántos litros hay, (b) cuántas páginas escritas suman los tres documentos, (c) qué respondes a tu compañero, (d) quién usa los productos.",
        "(a) 8*4 son 32 litros. (b) 2+3+2 son 7 páginas. (c) Que no: un producto sin etiqueta no permite conocer sus riesgos; se guarda en su envase original. (d) Personal capacitado y autorizado.",
        ["calcula 32 litros", "calcula 7 páginas", "explica por qué no pasar a botella sin rótulo", "indica que usa personal autorizado"],
        ["hoja con las cuatro respuestas"],
        ["sumar en vez de multiplicar", "aceptar la botella sin rótulo", "decir que él usa el producto"],
        "Pregunta: «¿qué pasa si nadie sabe qué contiene una botella?». Si no responde, pídele que relea la regla de la etiqueta."),
    reinforce="Escribe tres riesgos de los productos de pintura y, junto a cada uno, una regla general para evitarlo.",
    extend="Explica con un ejemplo inventado por qué una FDS leída en papel no reemplaza la capacitación para trabajar con productos.",
)

# ============================================================ OAM-06, clase 2
F = ("Ficha 2 (ficha técnica de ejemplo, inventada). Pintura para muros de ejemplo. Rendimiento: 8 m² por litro y por mano. Manos recomendadas: 2. Envase: 4 litros. "
     "Condición de la superficie que pide la ficha: seca, limpia y firme, sin partes sueltas. Papel mural de ejemplo: cada rollo cubre 5 m². "
     "FDS de ejemplo: advierte vapores y pide mantener ventilado y lejos de fuentes de calor. Todos los valores son de ejemplo y no son valores reales de ningún fabricante. "
     "Roles: el aplicador autorizado (ejecuta), el supervisor (revisa y decide si cumple) y el prevencionista (revisa las medidas de seguridad).")
build(
    O6, 2, F,
    use="Aprenderé el vocabulario de pintura y papeles: superficie, mano, rendimiento, rollo y condición de la superficie, y los roles de quienes revisan.",
    prior=["Sé qué son la etiqueta y la FDS.", "Sé multiplicar y dividir números enteros.", "Sé qué es una lista de chequeo."],
    explain=[
        "La mano es cada capa de producto que se aplica sobre una superficie. El rendimiento dice cuántos m² cubre un litro de producto en una mano, según la ficha técnica. Con el rendimiento se calcula cuántos litros se necesitan: se multiplica la superficie por el número de manos y se divide por el rendimiento. Los papeles murales se venden en rollos, y cada rollo cubre una cantidad de m² que indica la ficha.",
        "Antes de aprobar un trabajo, el supervisor revisa en una lista de chequeo que la superficie esté en la condición que pide la ficha: por ejemplo, seca, limpia y firme. Si no lo está, se anota y se informa; quien lee la ficha no la cambia. El aplicador autorizado ejecuta, el supervisor decide si cumple y el prevencionista revisa las medidas de seguridad. Los valores reales de rendimiento y de manos los fija el fabricante y el proyecto, no este cuaderno.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("mano", "cada capa de producto que se aplica sobre una superficie"), ("rendimiento", "m² que cubre un litro de producto en una mano"), ("rollo", "unidad en que se vende el papel mural"), ("condición de la superficie", "estado que debe tener un muro o cielo antes del trabajo, según la ficha"), ("lista de chequeo", "tabla que revisa si se cumplen las condiciones"), ("aplicador autorizado", "persona capacitada y autorizada que ejecuta el trabajo"), ("supervisor", "persona que revisa y decide si el trabajo cumple")],
    worked=[
        ("Litros necesarios", "Para una superficie de 40 m², con un rendimiento de ejemplo de 10 m² por litro y por mano y 1 mano, ¿cuántos litros hacen falta?", ["Se divide la superficie por el rendimiento.", "40 dividido en 10 son 4."], "4 litros"),
        ("Rollos de papel", "Una pared de ejemplo de 15 m² se cubre con rollos de 5 m². ¿Cuántos rollos hacen falta, sin considerar pérdida?", ["Se divide la superficie por lo que cubre un rollo.", "15 dividido en 5 son 3."], "3 rollos"),
    ],
    mistakes=[("Calcular litros sin considerar las manos.", "Se compra la mitad de lo necesario si se piden dos manos.", "Multiplica la superficie por el número de manos antes de dividir."),
              ("Aprobar una superficie húmeda porque «ya se ve seca».", "La ficha pide una condición que debe verificarse y registrarse.", "Anota el estado y consulta al supervisor.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es el rendimiento de una pintura?", "Los m² que cubre un litro en una mano", "El precio de un litro", "El número de manos de un muro", "El rendimiento relaciona litros con superficie cubierta."),
        ("abc", "Una «mano» de pintura es:", "Cada capa de producto aplicada sobre la superficie", "El nombre de una herramienta", "El envase de 4 litros", "Mano es el nombre que se da a cada capa de producto."),
        ("abc", "La lista de chequeo de una superficie sirve para:", "Revisar si el muro está en la condición que pide la ficha", "Calcular el sueldo del aplicador", "Elegir el color del muro", "La lista de chequeo compara el estado del muro con lo pedido."),
        ("=", "{F} Con el rendimiento de ejemplo, ¿cuántos m² cubren 3 litros en una mano?", "3*8", "Se multiplican los litros por el rendimiento.", " m²"),
        ("=", "{F} ¿Cuántos litros hacen falta para 48 m² con 2 manos?", "48*2//8", "Se multiplica la superficie por las manos y se divide por el rendimiento.", " litros"),
        ("=", "{F} Con envases de 4 litros, ¿cuántos envases se necesitan para esos litros?", "(48*2//8+3)//4", "Se divide por 4 y se sube al entero siguiente.", " envases"),
        ("=", "{F} Una pared de 20 m² se cubre con papel. ¿Cuántos rollos hacen falta?", "20//5", "Se divide la superficie por lo que cubre un rollo.", " rollos"),
        ("abc", "{F} ¿Qué condición de la superficie pide la ficha?", "Seca, limpia y firme, sin partes sueltas", "Mojada y con polvo", "Solo limpia, aunque tenga partes sueltas", "La ficha pide seca, limpia y firme."),
        ("abc", "{F} Un muro tiene humedad visible. ¿Qué se anota en la lista de chequeo?", "No cumple la condición «seca»; se informa al supervisor", "Cumple, porque se puede pintar igual", "Cumple si es de día", "La humedad incumple la condición pedida y se informa."),
        ("ab", "{F} Un compañero dice: «con una mano alcanza, así que calculo los litros para una sola». ¿Qué respuesta es correcta?", "No: la ficha recomienda 2 manos y los litros se calculan para 2", "Sí: una mano siempre alcanza", "La cantidad de manos la fija la ficha o el proyecto, no la opinión de un compañero."),
        ("abc", "{F} ¿Quién decide si el trabajo terminado cumple?", "El supervisor", "El aplicador autorizado que lo ejecutó", "El prevencionista, para toda la obra", "El supervisor revisa y decide si cumple."),
        ("abc", "{F} Un aplicador quiere cambiar el número de manos a una «para ahorrar». ¿Qué corresponde?", "No hacerlo: lo fijan la ficha y el proyecto; se consulta al supervisor", "Hacerlo si el muro se ve bien", "Hacerlo si el dueño lo aprueba", "Las manos las fija el fabricante o el proyecto, no se cambian por ahorro."),
        ("abc", "{F} El prevencionista dice que falta ventilación en el plan. ¿Qué rol cumple?", "Revisa que las medidas protejan a las personas", "Ejecuta la pintura", "Decide si la pintura cumple con el proyecto", "El prevencionista revisa las medidas de seguridad; no ejecuta ni aprueba el trabajo."),
    ],
    ctx=("abc", "Un trabajador nuevo propone usar un solvente cualquiera para «hacer rendir» la pintura. ¿Qué responde un compañero?", "Que consulte al supervisor y a la ficha, porque agregar productos no indicados puede ser peligroso", "Que lo haga si el color no cambia", "Que lo haga si lo prueba primero", "Agregar productos no indicados cambia el riesgo y el resultado; se consulta antes."),
    sc=[("En Terminaciones: ¿qué es una mano de pintura?", "Cada capa de producto aplicada sobre la superficie", "Las manos se suman al calcular los litros."),
        ("Para 30 m², 1 mano y rendimiento 10 m² por litro, ¿cuántos litros?", "3 litros", "30 dividido en 10 son 3."),
        ("¿Quién ejecuta el trabajo de pintura?", "Personal capacitado y autorizado", "Este cuaderno no habilita para trabajar.")],
    op=("Ficha de ejemplo: pintura con rendimiento de 6 m² por litro y por mano, 2 manos, envases de 3 litros; muro de 36 m²; papel con rollos de 4 m² para 16 m². Escribe (a) los litros, (b) los envases, (c) los rollos y (d) qué haces si el muro está húmedo.",
        "(a) 36*2 son 72, dividido en 6 son 12 litros. (b) 12 dividido en 3 son 4 envases. (c) 16 dividido en 4 son 4 rollos. (d) Lo anoto como no cumple la condición «seca» e informo al supervisor.",
        ["calcula 12 litros", "calcula 4 envases", "calcula 4 rollos", "informa la humedad al supervisor"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las manos", "aprobar el muro húmedo", "decir que decide el aplicador"],
        "Pregunta: «¿cuántas manos pide la ficha?». Si no responde, pídele que relea el enunciado."),
    reinforce="Con una superficie de 24 m², 2 manos y rendimiento de 12 m² por litro, calcula los litros.",
    extend="Explica por qué dos muros del mismo tamaño pueden necesitar distinta cantidad de pintura según el número de manos.",
)

# ============================================================ OAM-06, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Dormitorio ficticio de 5 m por 3 m y 3 m de alto. Perímetro de la pieza: 16 m. Vanos: 1 puerta de 2 m² y 1 ventana de 4 m². "
     "Pintura de ejemplo: rendimiento 7 m² por litro y por mano; 2 manos; envases de 4 litros. Pedido de un compañero: 2 envases. "
     "Lista de chequeo de superficie (datos entregados): muro norte, seco y firme; muro sur, con manchas de humedad. Plan de prevención: no describe ventilación del dormitorio.")
build(
    O6, 3, F,
    use="Aprenderé a calcular la superficie de muros descontando vanos, a comparar el pedido con la necesidad y a registrar condiciones de la superficie y del plan.",
    prior=["Sé calcular el área de un rectángulo.", "Sé calcular litros con rendimiento y manos.", "Sé qué es una no conformidad."],
    explain=[
        "Para pintar los muros de una pieza se calcula primero la superficie de los muros: el perímetro por la altura. Después se descuentan los vanos, que son las puertas y ventanas que no se pintan. Así se obtiene la superficie a pintar. Los litros se calculan multiplicando esa superficie por las manos y dividiendo por el rendimiento. Con los litros se calculan los envases, subiendo al entero siguiente porque no se venden fracciones de envase.",
        "El caso se completa revisando la lista de chequeo de la superficie y el plan de seguridad. Un muro con humedad no cumple la condición «seca», y un plan sin ventilación para un recinto cerrado es una no conformidad. Quien analiza el caso no arregla nada en terreno: registra e informa al supervisor y al prevencionista. Todas las cifras son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("perímetro", "suma de los largos de los lados de una figura, aquí el contorno de la pieza"), ("vano", "puerta o ventana que se descuenta de la superficie de muros"), ("superficie a pintar", "superficie de muros menos los vanos"), ("no conformidad", "algo que no cumple lo esperado"), ("subir al entero siguiente", "redondear hacia arriba porque no se venden fracciones de envase")],
    worked=[
        ("Superficie de muros", "Una pieza de ejemplo tiene perímetro de 12 m y 2 m de alto. ¿Cuántos m² de muros tiene antes de descontar vanos?", ["Se multiplica el perímetro por la altura.", "12 por 2 son 24."], "24 m²"),
        ("Descontar vanos", "En esos muros de ejemplo hay una puerta de 2 m². ¿Cuántos m² quedan para pintar?", ["Se resta la superficie del vano.", "24 menos 2 son 22."], "22 m²"),
    ],
    mistakes=[("Pintar en el cálculo también las puertas y ventanas.", "Se compra más producto del necesario.", "Descuenta los vanos de la superficie de muros."),
              ("Dar por aprobado un muro con humedad porque «igual se pinta».", "La condición de la ficha no se cumple.", "Anota que no cumple e informa al supervisor.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es el perímetro de una pieza?", "El contorno, es decir, la suma de los largos de sus lados", "La altura de los muros", "La superficie del piso", "El perímetro es el contorno; la superficie del piso es otra medida."),
        ("abc", "Al calcular la superficie a pintar, los vanos:", "Se descuentan de la superficie de muros", "Se suman a la superficie de muros", "Se multiplican por las manos", "Las puertas y ventanas no se pintan, así que se restan."),
        ("abc", "Un plan que no describe ventilación para un recinto cerrado con productos químicos es:", "Una no conformidad", "Un plan completo", "Un pedido de más material", "La falta de ventilación incumple lo esperado y debe informarse."),
        ("=", "{F} ¿Cuántos m² de muros hay antes de descontar vanos?", "16*3", "Se multiplica el perímetro por la altura.", " m²"),
        ("=", "{F} ¿Cuántos m² hay que pintar después de descontar la puerta y la ventana?", "16*3-2-4", "A la superficie de muros se le restan los vanos.", " m²"),
        ("=", "{F} ¿Cuántos litros se necesitan con 2 manos?", "(16*3-2-4)*2//7", "Se multiplica la superficie a pintar por las manos y se divide por el rendimiento.", " litros"),
        ("=", "{F} ¿Cuántos envases de 4 litros se necesitan?", "(12+3)//4", "Se divide por 4 y se sube al entero siguiente.", " envases"),
        ("=", "{F} ¿Cuántos envases faltan respecto del pedido de 2?", "3-2", "Se resta lo pedido de lo necesario.", " envase"),
        ("abc", "{F} ¿Qué estado tiene el muro sur según la lista de chequeo?", "No cumple la condición «seca»: tiene humedad", "Cumple, porque está firme", "No se puede revisar", "Las manchas de humedad incumplen la condición de superficie seca."),
        ("ab", "{F} Un compañero dice: «dos envases bastan, porque son 8 litros y el muro es chico». ¿Qué respuesta es correcta?", "No: se necesitan 12 litros, es decir 3 envases, según el cálculo", "Sí: 8 litros alcanzan para cualquier pieza chica", "El cálculo con superficie, manos y rendimiento da 12 litros, más de lo que dan 2 envases."),
        ("abc", "{F} ¿A quién se informan la humedad y la falta de ventilación?", "Al supervisor y al prevencionista", "A nadie, porque se pintará igual", "Solo al proveedor de pintura", "La humedad la decide el supervisor y la falta de ventilación la revisa el prevencionista."),
        ("abc", "{F} Un compañero propone abrir una ventana y trabajar con vapores sin esperar la revisión del plan. ¿Qué corresponde?", "Esperar la revisión: el plan lo define el prevencionista y lo ejecuta personal autorizado", "Hacerlo si la ventana queda abierta", "Hacerlo si trabaja poco tiempo", "Abrir una ventana no reemplaza una medida definida en el plan."),
        ("abc", "{F} ¿Cuál es el registro más completo de la diferencia del pedido?", "Necesidad (3 envases), pedido (2), faltante (1), quién lo detectó y fecha", "Solo «falta pintura»", "Solo el nombre de quien pidió", "Un registro útil dice qué, cuánto, quién y cuándo."),
    ],
    ctx=("abc", "Un joven que visita la obra quiere abrir un envase «para oler qué es». ¿Qué responde un compañero?", "Que no lo abra: los productos los manipula personal capacitado y los vapores pueden dañar", "Que lo abra si es solo un momento", "Que lo abra si está al aire libre", "Abrir un envase sin autorización expone a vapores; solo personal capacitado manipula productos."),
    sc=[("¿Cómo se obtiene la superficie a pintar?", "Superficie de muros menos los vanos", "Las puertas y ventanas no se pintan."),
        ("Si salen 10 litros y los envases son de 4 litros, ¿cuántos envases?", "3 envases", "10 dividido en 4 da 2,5 y se sube al entero siguiente."),
        ("¿Qué se hace con un muro húmedo?", "Anotar que no cumple e informar", "La condición de superficie seca no se cumple.")],
    op=("Caso de ejemplo «Dormitorio Sur»: 4 m por 4 m y 3 m de alto, perímetro 16 m; vanos: puerta 2 m² y ventana 2 m²; rendimiento 8 m² por litro; 2 manos; envases de 4 litros; pedido: 3 envases; muro oeste con humedad. Escribe (a) los m² a pintar, (b) los litros, (c) los envases necesarios y si el pedido alcanza, (d) qué haces con el muro oeste.",
        "(a) 16*3-2-2 son 44 m². (b) 44*2 son 88, dividido en 8 son 11 litros. (c) 11 dividido en 4 son 2,75: se sube a 3 envases; el pedido alcanza. (d) Anoto que no cumple la condición «seca» e informo al supervisor.",
        ["calcula 44 m²", "calcula 11 litros", "calcula 3 envases", "informa la humedad"],
        ["hoja con las cuatro respuestas"],
        ["no descontar vanos", "olvidar las manos", "no subir al entero siguiente"],
        "Pregunta: «¿qué se descuenta de los muros?». Si no responde, pídele que relea las puertas y ventanas."),
    reinforce="Calcula la superficie a pintar de una pieza inventada de perímetro 14 m, altura 3 m y un vano de 3 m².",
    extend="Explica por qué la falta de ventilación en el plan es una no conformidad aunque el cálculo de litros esté perfecto.",
)

# ============================================================ OAM-06, clase 4
F = ("Ficha 4 (presupuesto de pintura y papel, de ejemplo, inventado). Casa ficticia. Pintura: 36 m² de muros, 2 manos, rendimiento 9 m² por litro y por mano, envases de 4 litros a $40.000 cada uno; "
     "alternativa de envases de 1 litro a $12.000 cada uno. Papel mural: 30 m² de pared; cada rollo cubre 5 m²; pérdida de ejemplo del 10 % sobre la superficie; rollo a $14.000. "
     "Todos los precios, rendimientos y porcentajes son de ejemplo y no son valores reales.")
build(
    O6, 4, F,
    use="Aprenderé a calcular y comparar el costo de pintura y de papel mural en una planilla con datos de ejemplo.",
    prior=["Sé calcular litros con rendimiento y manos.", "Sé sumar un porcentaje de pérdida.", "Sé subir al entero siguiente."],
    explain=[
        "La planilla de costos de pintura sigue un orden: superficie, litros, envases y costo. Los litros salen de la superficie por las manos dividida en el rendimiento. Los envases salen de dividir los litros por el contenido de cada envase y subir al entero siguiente. Si hay dos formatos de envase, se comparan sus costos totales: puede convenir uno más grande aunque sobre producto, o uno más chico si el precio por litro es menor. Se elige con criterio, no solo por el precio de un envase.",
        "Para el papel mural se suma una pérdida por recortes a la superficie, luego se divide por lo que cubre un rollo y se sube al entero siguiente. El costo es el número de rollos por su precio. Los valores son de ejemplo: los reales los fija el fabricante y el mercado. La planilla ayuda a presupuestar y a pedir; la aplicación de productos la hace personal capacitado y autorizado, con las medidas del plan.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("formato de envase", "tamaño del envase en que se vende el producto, como 1 litro o 4 litros"), ("pérdida por recortes", "material que se desperdicia al recortar y se suma al pedido"), ("rollo", "unidad en que se vende el papel mural"), ("partida", "producto del presupuesto con su cantidad y su precio unitario"), ("subir al entero siguiente", "redondear hacia arriba porque no se venden fracciones")],
    worked=[
        ("Envases", "Se necesitan 10 litros de una pintura de ejemplo y los envases son de 4 litros. ¿Cuántos envases hay que comprar?", ["Se divide por el contenido de un envase.", "10 dividido en 4 da 2,5 y se sube a 3."], "3 envases"),
        ("Costo de rollos", "Se necesitan 6 rollos de papel de ejemplo a $9.000 cada uno. ¿Cuánto cuestan?", ["Se multiplica la cantidad por el precio unitario.", "6 por 9.000 son 54.000."], "$54.000"),
    ],
    mistakes=[("Elegir el formato solo porque su envase es más barato.", "El costo total depende de cuántos envases se compran.", "Compara el costo total de cada alternativa."),
              ("Redondear hacia abajo los rollos.", "Quedaría parte de la pared sin cubrir.", "Si la división no es exacta, sube al entero siguiente.")],
    T=[
        ("abc", "En Terminaciones: ¿qué es el formato de envase?", "El tamaño del envase en que se vende un producto", "El color del producto", "El número de manos del muro", "El formato es el tamaño del envase, como 1 litro o 4 litros."),
        ("abc", "Al comparar dos formatos de envase, lo más correcto es comparar:", "El costo total de cada alternativa", "Solo el precio de un envase", "El color de cada envase", "El costo total depende de la cantidad que se compra."),
        ("abc", "El número de rollos de papel se redondea:", "Hacia arriba, porque no se venden fracciones", "Hacia abajo, para ahorrar", "Siempre al más cercano", "Si falta papel, quedaría una parte de la pared sin cubrir."),
        ("=", "{F} ¿Cuántos litros de pintura se necesitan?", "36*2//9", "Se multiplica la superficie por las manos y se divide por el rendimiento.", " litros"),
        ("=", "{F} ¿Cuántos envases de 4 litros se necesitan?", "(8+3)//4", "Se divide los litros por 4 y se sube al entero siguiente.", " envases"),
        ("=", "{F} ¿Cuánto cuestan los envases de 4 litros?", "2*40000", "Se multiplican los envases por su precio.", " pesos"),
        ("=", "{F} ¿Cuánto costaría comprar los litros necesarios en envases de 1 litro?", "8*12000", "Se multiplican los litros por el precio de un envase de 1 litro.", " pesos"),
        ("abc", "{F} ¿Qué formato resulta más económico para esa compra?", "El de 4 litros", "El de 1 litro", "Cuestan lo mismo", "Con envases de 4 litros se gasta $80.000 y con los de 1 litro $96.000."),
        ("=", "{F} ¿Cuántos m² de papel se piden con la pérdida de ejemplo del 10 %?", "30*110//100", "Se multiplica la superficie por 110 sobre 100.", " m²"),
        ("=", "{F} ¿Cuántos rollos se necesitan, subiendo al entero siguiente?", "(33+4)//5", "Se divide 33 m² por 5 m² por rollo y se sube al entero siguiente.", " rollos"),
        ("=", "{F} ¿Cuánto cuestan los rollos?", "7*14000", "Se multiplican los rollos por su precio.", " pesos"),
        ("ab", "{F} Un compañero dice: «6 rollos alcanzan porque 30 dividido en 5 son 6, sin pérdida». ¿Qué respuesta es correcta?", "No: con la pérdida de ejemplo se piden 7 rollos", "Sí: la pérdida nunca se considera", "La planilla incluye la pérdida por recortes, por lo que se piden 7 rollos."),
        ("abc", "{F} Un supervisor pide ahorrar comprando menos pintura que la calculada. ¿Qué corresponde?", "Consultar: reducir la cantidad puede dejar muros sin cubrir y no se hace sin revisar el cálculo", "Comprar menos si el muro parece chico", "Comprar menos si el envase es caro", "La cantidad sale del cálculo con rendimiento y manos; no se reduce por ahorro."),
    ],
    ctx=("abc", "Un proveedor ofrece envases de otra pintura «igual de buena» más barata. ¿Qué corresponde?", "Consultar al supervisor: cambiar el producto exige revisar la ficha técnica y la FDS", "Aceptar porque cuesta menos", "Aceptar si el color es parecido", "Otro producto tiene otro rendimiento y otros riesgos; se revisan sus fichas antes de cambiar."),
    sc=[("¿Cómo se calculan los litros de pintura?", "Superficie por manos dividida en el rendimiento", "El rendimiento dice cuántos m² cubre un litro."),
        ("Si salen 3,2 rollos, ¿cuántos se piden?", "4 rollos", "No se venden fracciones, por lo que se sube al entero siguiente."),
        ("¿La planilla habilita para aplicar productos?", "No: lo hace personal capacitado y autorizado", "Este cuaderno no habilita para trabajar con productos.")],
    op=("Planilla de ejemplo «Sala Los Robles»: muros de 54 m², 2 manos, rendimiento 9 m² por litro, envases de 4 litros a $38.000; papel para 20 m² con rollos de 5 m², pérdida de 10 % y rollo a $12.000. Escribe (a) los litros, (b) los envases y su costo, (c) los rollos con pérdida y su costo, (d) quién aplica los productos.",
        "(a) 54*2 son 108, dividido en 9 son 12 litros. (b) 12 dividido en 4 son 3 envases: $114.000. (c) 20*110/100 son 22 m²; 22 dividido en 5 da 4,4: se sube a 5 rollos: $60.000. (d) Personal capacitado y autorizado.",
        ["calcula 12 litros", "calcula 3 envases y $114.000", "calcula 5 rollos y $60.000", "indica quién aplica"],
        ["hoja con las cuatro respuestas"],
        ["olvidar las manos", "olvidar la pérdida", "no subir al entero siguiente"],
        "Pregunta: «¿por qué se suben los rollos al entero siguiente?». Si no responde, pídele que relea esa regla."),
    reinforce="Calcula los litros, envases de 4 litros y costo de una pintura inventada para 72 m², 2 manos y rendimiento de 12 m² por litro.",
    extend="Explica cuándo un envase más grande puede no ser la compra más económica, aunque tenga mejor precio por litro.",
)
