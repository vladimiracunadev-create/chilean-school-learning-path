"""Electricidad TP 3.º y 4.º medio: OAE-01 (leer especificaciones, planos y diagramas), OAE-02 (dibujo asistido en papel) y OAE-03 (alumbrado: documentos y cálculos). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_elec_common import AVISO, EMER, build

O1 = "TP-ELEC-3y4-OAE-01"
O2 = "TP-ELEC-3y4-OAE-02"
O3 = "TP-ELEC-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (proyecto de ejemplo, inventado). Proyecto «Local Aurora» (ficticio): un pequeño local comercial de 48 m². Documentos del proyecto: plano de planta (1 lámina), "
     "diagrama del tablero (1 lámina), especificaciones técnicas (6 páginas), memoria de cálculo (4 páginas), presupuesto (3 páginas) y lista de materiales (2 páginas). "
     "Riesgos anotados en las especificaciones: descarga eléctrica, quemadura e incendio por una instalación mal ejecutada.")
build(
    O1, 1, F,
    use="Aprenderé qué documentos forman un proyecto de instalación eléctrica, qué institución vigila la seguridad y qué riesgos hay que reconocer antes de leer cualquier plano.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y multiplicar.", "Sé que un trabajo se encarga por escrito."],
    explain=[
        "Una instalación eléctrica es el conjunto de cables, equipos y artefactos que llevan la energía hasta donde se usa. Las de casas y locales son de baja tensión: una categoría que fija la norma vigente. Antes de ejecutar una instalación existe un proyecto: un conjunto de documentos. El plano es un dibujo a escala de la planta del recinto. El diagrama es un dibujo con símbolos que muestra cómo se organiza el sistema eléctrico. Las especificaciones técnicas dicen por escrito cómo deben ser los materiales y el trabajo. La memoria de cálculo muestra los cálculos con que se definió el proyecto. El presupuesto reúne los costos y la lista de materiales dice qué piezas se necesitan.",
        "En Chile, la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza la seguridad de las instalaciones eléctricas, y la norma vigente fija lo que se debe cumplir. Los riesgos principales son la descarga eléctrica, la quemadura y el incendio. Cada persona tiene un rol: el proyectista diseña, el instalador autorizado ejecuta, el supervisor revisa y el cliente recibe. Si dos documentos se contradicen, nadie elige uno por su cuenta: se anota la diferencia y se informa al proyectista o al supervisor.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("plano", "dibujo a escala de la planta de un recinto"), ("diagrama", "dibujo con símbolos que muestra cómo se organiza el sistema eléctrico"), ("especificaciones técnicas", "documento escrito que dice cómo deben ser los materiales y el trabajo"), ("memoria de cálculo", "documento que muestra los cálculos con que se definió el proyecto"), ("presupuesto", "documento que reúne los costos del proyecto"), ("baja tensión", "categoría de instalaciones de uso común en casas y locales, cuyos límites fija la norma vigente"), ("SEC", "Superintendencia de Electricidad y Combustibles, que fiscaliza la seguridad eléctrica")],
    worked=[
        ("Elegir el documento", "Una arquitecta de ejemplo necesita saber qué calidad deben tener los materiales de una instalación. ¿Qué documento consulta?", ["La calidad y las características se escriben en un documento específico.", "Ese documento son las especificaciones técnicas."], "Las especificaciones técnicas"),
        ("Contar páginas", "Un proyecto de ejemplo tiene 5 páginas de especificaciones y 3 de presupuesto. ¿Cuántas páginas escritas suman?", ["Se suman las páginas de los dos documentos.", "5 más 3 son 8."], "8 páginas"),
    ],
    mistakes=[("Elegir entre dos documentos que se contradicen y seguir sin avisar.", "Un documento erróneo puede llevar a ejecutar algo riesgoso.", "Anota la diferencia e informa al proyectista o al supervisor."),
              ("Creer que leer un proyecto completo habilita a intervenir un tablero.", "Esa tarea exige personal autorizado y norma vigente.", "Aprende los conceptos aquí y practica solo con instructor autorizado.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la memoria de cálculo de un proyecto de instalación?", "El documento que muestra los cálculos con que se definió el proyecto", "El dibujo a escala de la planta del recinto", "La lista de precios de los materiales", "La memoria de cálculo justifica el proyecto; el dibujo es el plano y los precios van en el presupuesto."),
        ("abc", "En Electricidad: ¿para qué sirven las especificaciones técnicas?", "Para decir por escrito cómo deben ser los materiales y el trabajo", "Para mostrar con símbolos dónde va cada artefacto sobre la planta", "Para registrar cuánto se pagó al instalador", "Las especificaciones describen materiales y trabajo; los símbolos están en el plano y los pagos en otro registro."),
        ("abc", "Un cliente pregunta qué institución del Estado vigila que las instalaciones eléctricas de su local sean seguras. ¿Cuál es?", "La Superintendencia de Electricidad y Combustibles (SEC)", "El Servicio de Impuestos Internos", "La Dirección del Trabajo", "La SEC fiscaliza la seguridad eléctrica; las otras instituciones tienen funciones distintas."),
        ("=", "{F} Entre los documentos escritos (especificaciones, memoria, presupuesto y lista de materiales), ¿cuántas páginas hay en total?", "6+4+3+2", "Se suman las páginas de los cuatro documentos escritos.", " páginas"),
        ("abc", "{F} El cliente quiere saber cuánto costará el proyecto. ¿Qué documento debe consultar?", "El presupuesto", "La memoria de cálculo", "El diagrama del tablero", "Los costos se reúnen en el presupuesto; la memoria justifica cálculos y el diagrama muestra la organización eléctrica."),
        ("abc", "{F} ¿Qué riesgos nombra la ficha para una instalación mal ejecutada?", "Descarga eléctrica, quemadura e incendio", "Solo el retraso en la entrega del local", "Descarga eléctrica y contaminación del agua potable", "La ficha anota exactamente descarga, quemadura e incendio; las otras opciones agregan algo que no nombra."),
        ("=", "{F} Una empresa de ejemplo cotiza el diseño a $2.500 por m². ¿Cuánto cobra por diseñar el local?", "48*2500", "El valor por m² se multiplica por los metros cuadrados del local.", " pesos"),
        ("abc", "{F} Una persona sin autorización quiere revisar el tablero «para ahorrar tiempo». ¿Qué corresponde?", "No hacerlo: lo realiza personal autorizado según la norma vigente (SEC)", "Hacerlo si el cliente se lo permite por escrito", "Hacerlo si lo acompaña un compañero de curso", "El permiso del cliente o la compañía de otro estudiante no reemplazan la autorización ni la norma vigente."),
        ("abc", "{F} Las especificaciones piden un número de puntos de luz distinto del que dibuja el plano. ¿Qué se hace?", "Anotar la diferencia e informar al proyectista o al supervisor", "Seguir el plano porque es un dibujo", "Seguir las especificaciones porque están escritas", "Cuando los documentos se contradicen no se elige uno por cuenta propia: se informa a quien decide."),
        ("ab", "{F} Una estudiante dice: «leí todo el proyecto, así que ya puedo intervenir el tablero». ¿Qué respuesta es correcta?", "No: leer documentos no habilita; intervenir un tablero exige personal autorizado y norma vigente", "Sí: conocer todos los documentos la habilita para intervenir", "Entender un proyecto es una competencia distinta de estar autorizada para trabajar con energía."),
        ("abc", "En un local de ejemplo, un trabajador recibe una descarga y sigue en contacto con la energía. ¿Qué se hace según las reglas generales?", "No tocarlo, cortar el suministro solo si se está autorizado, avisar a un adulto responsable y a emergencias", "Tirar de su ropa para separarlo, aunque nadie haya cortado la energía", "Tocarlo para comprobar si respira antes de avisar a alguien", "Tocar a la persona en contacto puede transmitir la descarga a quien ayuda; se corta el suministro solo si se está autorizado y se avisa."),
        ("=", "{F} Si las especificaciones y la memoria tuvieran el doble de páginas, y el presupuesto y la lista de materiales siguieran iguales, ¿cuántas páginas escritas tendría el proyecto?", "(6+4)*2+3+2", "Se duplican las páginas de especificaciones y memoria y se suman las de los otros dos documentos.", " páginas"),
        ("abc", "{F} Un revisor ve en la lista de materiales un artefacto que no aparece ni en el plano ni en el diagrama. ¿Qué conclusión es la más prudente?", "Hay una diferencia entre documentos: se informa para aclararla antes de comprar o ejecutar", "El artefacto sobra y se borra de la lista sin avisar", "La lista de materiales siempre manda sobre el plano", "Una diferencia entre documentos se informa; ni la lista ni el plano mandan por sí solos."),
    ],
    ctx=("abc", "Un vecino ofrece dinero a un estudiante para que «arregle rápido» el tablero de su casa porque «la electricidad no es difícil». ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere contratar a un instalador autorizado", "Acepta si cobra menos que un instalador", "Acepta, porque ya estudió los documentos de un proyecto", "Intervenir un tablero exige autorización y norma vigente; cobrar menos o haber estudiado no reemplazan eso."),
    sc=[
        ("En Electricidad: ¿qué es un diagrama?", "Un dibujo con símbolos que muestra cómo se organiza el sistema eléctrico", "El diagrama muestra la organización eléctrica con símbolos, no las medidas de la planta."),
        ("En electricidad: ¿qué se hace si el plano y las especificaciones se contradicen?", "Anotar la diferencia e informar al proyectista o al supervisor", "No se elige un documento al azar porque podría ser el equivocado."),
        ("¿Quién interviene un tablero conectado a la red?", "Personal autorizado, con norma vigente (SEC) y protección", "Este cuaderno no habilita para trabajar con energía."),
    ],
    op=("Proyecto de ejemplo «Taller Brisa»: plano (1 lámina), especificaciones (5 páginas), memoria de cálculo (3 páginas) y presupuesto (2 páginas). Las especificaciones indican 6 puntos de luz y el plano dibuja 5. Escribe (a) qué documento consultarías para saber cuánto cuesta, (b) cuántas páginas escritas hay en total, (c) qué haces con la diferencia de puntos de luz y a quién informas, (d) un riesgo de la instalación y quién debe ejecutar el trabajo.",
        "(a) El presupuesto. (b) 5+3+2 son 10 páginas escritas. (c) Anoto la diferencia (6 en las especificaciones, 5 en el plano) y la informo al proyectista o al supervisor; no elijo uno por mi cuenta. (d) Descarga eléctrica o incendio; lo ejecuta personal autorizado según la norma vigente (SEC).",
        ["nombra el documento correcto", "suma bien las páginas", "informa la diferencia sin decidir por su cuenta", "reconoce un riesgo y quién ejecuta"],
        ["hoja con las cuatro respuestas"],
        ["elegir un documento sin avisar", "sumar el plano como página escrita", "decir que puede ejecutar el trabajo"],
        "Pregunta: «¿qué haces si el plano y las especificaciones se contradicen?». Si no responde, pídele que relea la regla de informar la diferencia."),
    reinforce="Escribe los seis documentos de un proyecto y, junto a cada uno, una frase que diga para qué sirve.",
    extend="Explica con un ejemplo inventado por qué una instalación aprobada en papel puede ser riesgosa si se ejecuta sin personal autorizado.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (plano descrito por escrito, de ejemplo, inventado). Dormitorio de práctica de 4 m por 3 m, plano de planta a escala 1:50. Leyenda de ejemplo: L = punto de luz en el techo; "
     "I = interruptor; T = tomacorriente; Q = tablero. Elementos del plano: 2 puntos de luz (L1 y L2); 1 interruptor (I1) junto a la puerta; 4 tomacorrientes (T1 a T4). "
     "El tablero Q1 está en el pasillo, fuera del dormitorio. En el plano, la pared larga mide 8 cm.")
build(
    O1, 2, F,
    use="Aprenderé a leer la planta, la leyenda, las cotas y la escala de un plano de instalación eléctrica descrito por escrito.",
    prior=["Sé qué documentos forman un proyecto.", "Sé multiplicar y dividir por números pequeños.", "Sé pasar de centímetros a metros."],
    explain=[
        "La planta es la vista del recinto desde arriba, como si se le quitara el techo. En ella, cada artefacto se dibuja con un símbolo y se nombra con una letra y un número. La leyenda explica qué significa cada símbolo; sin ella el plano no se puede leer. La cota es un número que indica una medida del dibujo. El rótulo reúne el nombre del proyecto, la escala, la fecha y la revisión del plano. La revisión es la versión del plano, que se identifica con una letra o un número.",
        "El plano se dibuja a escala: una razón fija entre la medida dibujada y la real. A escala 1:50, 1 cm del plano son 50 cm reales. Para pasar de lo dibujado a lo real se multiplica por 50; para pasar de lo real a lo dibujado se divide por 50. Una copia reducida o ampliada sin avisar cambia la escala, por eso se confía en las cotas y en el rótulo, no en la regla.",
        f"Ninguna persona agrega símbolos nuevos ni cambia medidas por su cuenta: eso lo decide el proyectista. {EMER} {AVISO}",
    ],
    vocab=[("planta", "vista del recinto desde arriba"), ("leyenda", "tabla que explica qué es cada símbolo"), ("cota", "número que indica una medida del dibujo"), ("rótulo", "recuadro con nombre del proyecto, escala, fecha y revisión"), ("revisión", "versión del plano, identificada con una letra o número"), ("escala", "razón fija entre la medida dibujada y la real")],
    worked=[
        ("Pasar a medida real", "Un plano de ejemplo está a escala 1:20. Un muro mide 15 cm en el plano. ¿Cuánto mide en la realidad?", ["Cada centímetro del plano son 20 centímetros reales.", "15 por 20 son 300 centímetros, que son 3 metros."], "300 cm (3 m)"),
        ("Leer la leyenda", "Una leyenda de ejemplo dice: E = enchufe; F = foco. En un plano aparecen 3 E y 2 F. ¿Cuántos enchufes hay?", ["La leyenda dice que E significa enchufe.", "Se cuentan los símbolos E."], "3 enchufes"),
    ],
    mistakes=[("Medir con regla una copia reducida y usar la escala del rótulo.", "La copia ya no está a la escala indicada y la medida sale falsa.", "Usa las cotas del plano o pide una copia a escala."),
              ("Contar el tablero como si fuera un punto de luz porque ambos son símbolos.", "Cada símbolo significa algo distinto según la leyenda.", "Cuenta solo los símbolos que la leyenda asigna a lo que buscas.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la planta de un plano?", "La vista del recinto desde arriba, como si se le quitara el techo", "La vista del recinto desde un costado, que muestra la altura de las paredes", "El recuadro con el nombre del proyecto, la fecha y la escala", "La planta es la vista desde arriba; la vista lateral es otra y el recuadro es el rótulo."),
        ("abc", "En Electricidad: ¿qué indica una cota en un plano?", "Un número que indica una medida del dibujo", "La potencia de cada artefacto dibujado", "El número de revisión del plano", "La cota expresa una medida; la potencia y la revisión se anotan en otros lugares."),
        ("abc", "¿Qué reúne el rótulo de un plano?", "El nombre del proyecto, la escala, la fecha y la revisión", "El significado de cada símbolo dibujado", "Todas las medidas del recinto", "Los símbolos se explican en la leyenda y las medidas en las cotas; el rótulo identifica el plano."),
        ("=", "{F} ¿Cuántos símbolos de tomacorriente e interruptor dibuja el plano en total?", "4+1", "Se suman los 4 tomacorrientes y el interruptor que dibuja la ficha.", " símbolos"),
        ("abc", "{F} ¿Qué representa el símbolo Q1 y dónde está?", "El tablero, ubicado en el pasillo fuera del dormitorio", "Un punto de luz en el techo del dormitorio", "Un tomacorriente junto a la puerta", "La leyenda dice que Q es el tablero y la ficha lo ubica en el pasillo."),
        ("=", "{F} ¿Cuántos centímetros mide en el plano la pared corta del dormitorio?", "300//50", "La medida real de 300 cm se divide por la escala 1:50.", " cm"),
        ("=", "{F} Una pared de 5 m de largo se dibuja con la escala de la ficha. ¿Cuántos centímetros mide en el plano?", "500//50", "Los 500 cm reales se dividen por 50 para obtener la medida dibujada.", " cm"),
        ("=", "{F} Un cable dibujado mide 18 cm en el plano. ¿Cuántos metros reales representa?", "18*50//100", "Se multiplica por 50 para pasar a centímetros reales y se divide por 100 para pasar a metros.", " m"),
        ("abc", "{F} El revisor encuentra en el plano un símbolo U1 que no está en la leyenda. ¿Qué corresponde?", "Pedir al proyectista que agregue su significado a la leyenda antes de usarlo", "Suponer que U1 es otro tomacorriente porque se parece", "Ignorar U1 y seguir con el resto del plano", "Un símbolo sin leyenda no se interpreta por parecido: se consulta a quien diseñó."),
        ("abc", "{F} Un compañero cuenta 3 puntos de luz porque suma L1, L2 y el tablero Q1. ¿Cuál es el error?", "Q1 es el tablero, no un punto de luz; los puntos de luz son 2", "Falta contar el interruptor I1 como punto de luz", "Los puntos de luz no se cuentan en la planta", "La leyenda define Q como tablero, así que no se suma a los puntos de luz."),
        ("abc", "{F} Un técnico mide la pared larga con regla en una copia reducida a la mitad y obtiene 4 cm. ¿Qué conclusión es correcta?", "No debe usar esa medida: la copia está reducida; debe usar las cotas o pedir una copia a escala", "La pared mide 200 cm porque 4 por 50 son 200, aunque la copia esté reducida", "La pared mide 4 cm reales, porque la regla siempre da la medida real", "En una copia reducida la escala del rótulo ya no vale; se usan las cotas."),
        ("=", "{F} Se quiere dibujar el mismo dormitorio a escala 1:100. ¿Cuántos centímetros medirá la pared larga en ese plano?", "400//100", "La medida real de 400 cm se divide por la nueva escala 1:100.", " cm"),
        ("abc", "{F} La lista de materiales pide 3 puntos de luz, 1 interruptor y 4 tomacorrientes para este dormitorio. ¿Qué diferencia hay con el plano y qué corresponde?", "Sobra un punto de luz en la lista; se informa al proyectista para corregir un documento", "Falta un tomacorriente en la lista; se compra uno más", "No hay diferencia, porque la lista siempre incluye uno de reserva", "El plano dibuja 2 puntos de luz y la lista pide 3: es una diferencia que se informa, no una reserva."),
    ],
    ctx=("abc", "Un instalador de ejemplo recibe un plano sin leyenda ni escala. ¿Qué corresponde?", "Pedir al proyectista la leyenda y la escala antes de interpretar o medir", "Deducir la escala midiendo con regla y trabajar con esa", "Usar la leyenda de otro proyecto con símbolos parecidos", "Sin leyenda ni escala el plano no se puede leer con seguridad; se pide el dato a quien lo diseñó."),
    sc=[
        ("En Electricidad: ¿cómo se pasa una medida del plano a la medida real?", "Multiplicándola por el número de la escala", "A escala 1:50, cada centímetro dibujado equivale a 50 reales."),
        ("¿Para qué sirve la leyenda de un plano?", "Para saber qué significa cada símbolo", "Sin leyenda, un símbolo puede interpretarse mal."),
        ("En Electricidad: ¿qué muestra la planta?", "El recinto visto desde arriba", "La planta es la vista superior del recinto con sus símbolos."),
    ],
    op=("Plano de ejemplo de una oficina de 6 m por 4 m, escala 1:50. Leyenda: L = punto de luz; T = tomacorriente; I = interruptor. Elementos: 3 L, 6 T, 1 I y un símbolo X1 que no está en la leyenda. Escribe (a) cuántos centímetros mide en el plano la pared de 6 m, (b) cuántos puntos de luz y cuántos tomacorrientes hay, (c) qué haces con el símbolo X1 y por qué, (d) qué medida usarías si la copia estuviera reducida.",
        "(a) 600 dividido por 50 son 12 cm. (b) 3 puntos de luz y 6 tomacorrientes. (c) Pido al proyectista el significado de X1 antes de usarlo, porque no está en la leyenda y no se interpreta por parecido. (d) Usaría las cotas del plano o pediría una copia a escala.",
        ["calcula bien la medida en el plano", "cuenta los símbolos según la leyenda", "no interpreta X1 por su cuenta", "reconoce que la copia reducida no sirve para medir"],
        ["hoja con las cuatro respuestas y el cálculo"],
        ["multiplicar en vez de dividir", "contar X1 como tomacorriente", "medir con regla una copia reducida"],
        "Pregunta: «¿por qué no puedes suponer qué es X1?». Si no responde, pídele que relea el papel de la leyenda."),
    reinforce="Dibuja a mano alzada un croquis de la habitación de la ficha con sus símbolos y escribe la leyenda al lado.",
    extend="Explica con un ejemplo por qué una cota es más confiable que medir con regla un plano impreso.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (cuadro de circuitos de ejemplo, inventado). Proyecto «Librería Mora» (ficticio). Circuito C1, alumbrado: 10 puntos de luz de 20 W cada uno. "
     "Circuito C2, tomacorrientes: 8 tomacorrientes, sin potencia declarada en el cuadro. Circuito C3, letrero exterior: 1 letrero de 300 W. "
     "El plano dibuja 11 puntos de luz y 8 tomacorrientes. Las especificaciones piden rotular cada circuito en el tablero.")
build(
    O1, 3, F,
    use="Aprenderé a leer un cuadro de circuitos, a sumar potencias y a detectar diferencias entre el plano y los demás documentos de un proyecto.",
    prior=["Sé qué documentos forman un proyecto.", "Sé leer un plano y su leyenda.", "Sé multiplicar y sumar."],
    explain=[
        "Un circuito es un camino cerrado por donde circula la corriente y que alimenta un grupo de artefactos. El cuadro de circuitos es una tabla que lista los circuitos del proyecto con sus artefactos y su potencia. La potencia se mide en vatios (W) y dice cuánta energía por segundo usa un artefacto; 1 kW son 1000 W. La potencia de un circuito se obtiene sumando la de cada artefacto: 10 luces de 20 W suman 200 W. Rotular es escribir en el tablero qué alimenta cada circuito, para que cualquiera lo identifique con seguridad.",
        "La revisión cruzada consiste en comparar un documento con otro: el plano con el cuadro, el cuadro con la lista de materiales. Cuando los datos no coinciden aparece un hallazgo: una diferencia o falta que se anota para corregirla. El revisor no corrige por su cuenta: informa al proyectista o al supervisor, que deciden qué documento cambia. Cuando falta un dato, como la potencia de un circuito, no se inventa: se pide.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("circuito", "camino cerrado por donde circula la corriente y que alimenta un grupo de artefactos"), ("cuadro de circuitos", "tabla que lista los circuitos con sus artefactos y potencias"), ("potencia", "energía por segundo que usa un artefacto; se mide en vatios (W)"), ("kW", "kilovatio, que equivale a 1000 W"), ("rotular", "escribir en el tablero qué alimenta cada circuito"), ("hallazgo", "diferencia o falta que se anota para corregirla"), ("sobrecarga", "situación en que un circuito debe llevar más energía que la que su diseño permite")],
    worked=[
        ("Potencia de un circuito", "Un circuito de ejemplo tiene 6 luces de 15 W. ¿Cuántos vatios suma?", ["Se multiplica la potencia de una luz por la cantidad.", "6 por 15 son 90."], "90 W"),
        ("Detectar un hallazgo", "El cuadro de un proyecto de ejemplo dice 4 tomacorrientes y el plano dibuja 5. ¿Qué se anota?", ["Los dos documentos deben coincidir.", "Hay una diferencia de 1 tomacorriente."], "Un hallazgo: el cuadro dice 4 y el plano dibuja 5; se informa al proyectista"),
    ],
    mistakes=[("Rellenar con una potencia supuesta el circuito que no la declara.", "Una cifra inventada puede ocultar una sobrecarga.", "Pide el dato al proyectista y anota que falta."),
              ("Corregir el cuadro para que calce con el plano sin avisar a nadie.", "No se sabe cuál de los dos documentos es el equivocado.", "Informa el hallazgo; el proyectista decide qué corrige.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un circuito de una instalación?", "Un camino cerrado por donde circula la corriente y que alimenta un grupo de artefactos", "El dibujo que muestra dónde va cada artefacto en la planta", "La tabla con los precios de cada artefacto", "El dibujo es el plano y la tabla de precios es el presupuesto; el circuito es el camino de la corriente."),
        ("abc", "En Electricidad: ¿qué mide la potencia de un artefacto, en vatios?", "Cuánta energía por segundo usa", "Cuántos metros de cable necesita", "Cuánto tiempo puede estar encendido", "La potencia expresa energía por segundo; no es largo de cable ni duración."),
        ("abc", "En Electricidad: ¿qué es un cuadro de circuitos?", "Una tabla que lista los circuitos con sus artefactos y potencias", "Una tabla con los precios de los circuitos y los plazos de pago", "Un dibujo que muestra los circuitos vistos desde arriba", "El cuadro lista circuitos y potencias; los precios están en el presupuesto y el dibujo es el plano."),
        ("=", "{F} ¿Cuántos vatios consume el alumbrado del circuito C1?", "10*20", "Se multiplica la potencia de un punto de luz por la cantidad de puntos.", " W"),
        ("abc", "{F} ¿Qué diferencia hay entre el plano y el cuadro de circuitos?", "El plano dibuja 11 puntos de luz y el cuadro indica 10", "El plano dibuja 8 tomacorrientes y el cuadro indica 10", "El letrero tiene 300 W en el cuadro y 200 W en el plano", "Solo coinciden los tomacorrientes y el letrero; los puntos de luz son 11 contra 10."),
        ("abc", "{F} El circuito C2 no declara potencia. ¿Qué corresponde para calcular la potencia total del proyecto?", "Pedir al proyectista la potencia de los tomacorrientes, sin inventar un valor", "Suponer que los tomacorrientes consumen 0 W", "Usar la potencia del letrero como si fuera la de C2", "Un dato que falta se pide; suponerlo puede ocultar una sobrecarga."),
        ("=", "{F} Sumando solo los circuitos con potencia declarada (C1 y C3), ¿cuántos vatios son?", "10*20+300", "Se suma la potencia del alumbrado y la del letrero.", " W"),
        ("=", "{F} El proyecto agrega un calefactor de 1500 W y un hervidor de 500 W. ¿Cuántos kW suman entre los dos?", "(1500+500)//1000", "Se suman los vatios y se pasan a kW dividiendo por 1000.", " kW"),
        ("ab", "{F} Un revisor rotula el circuito C3 como «tomacorrientes». ¿Es correcto?", "No: C3 alimenta el letrero exterior y debe rotularse así", "Sí: el letrero se enchufa a un tomacorriente y por eso es del mismo circuito", "Se rotula según lo que alimenta el circuito en el cuadro, que para C3 es el letrero."),
        ("abc", "{F} Un compañero propone corregir el cuadro a 11 puntos de luz «porque el plano se ve más claro». ¿Qué corresponde?", "Informar al proyectista o al supervisor, que decide qué documento se corrige", "Corregir el cuadro, porque el plano siempre manda", "Dejar los 10, porque un cuadro nunca se corrige", "Ningún documento manda por sí solo; la decisión corresponde a quien diseña o supervisa."),
        ("=", "{F} Si el plano fuera el correcto (11 puntos de luz de 20 W) y el letrero se mantiene, ¿cuántos vatios suman alumbrado y letrero?", "11*20+300", "Se suman 11 luces de 20 W y el letrero de 300 W.", " W"),
        ("abc", "{F} Antes de ejecutar, el supervisor pide un registro de la diferencia de puntos de luz. ¿Qué debe contener como mínimo?", "Qué documentos se contradicen, qué dice cada uno, quién lo detectó y la fecha", "Solo el nombre de quien lo detectó", "La decisión final, aunque no se haya consultado a nadie", "Un registro útil deja constancia de qué, dónde, quién y cuándo."),
        ("abc", "{F} Un compañero dice que no hace falta calcular la potencia total porque «son solo luces y tomacorrientes». ¿Qué respuesta es correcta?", "La potencia total se calcula igual: de ella dependen los cálculos y los riesgos del proyecto", "Es correcto: las luces y los tomacorrientes nunca importan", "Es correcto si el cliente no pregunta", "La potencia total es un dato básico de la memoria de cálculo, aunque los artefactos parezcan simples."),
    ],
    ctx=("abc", "{F} El dueño quiere agregar tres lámparas de 40 W al circuito C1 «porque son pocas». ¿Qué corresponde?", "Informar que un cambio de cargas modifica el cuadro y la memoria, y que lo revisa el proyectista", "Agregarlas, porque 120 W adicionales son pocos", "Agregarlas y corregir el cuadro después si alguien pregunta", "Un cambio de cargas altera los cálculos del proyecto; no se hace sin revisión del proyectista."),
    sc=[
        ("En Electricidad: ¿cómo se obtiene la potencia de un circuito de alumbrado?", "Sumando la potencia de cada punto de luz", "La potencia del circuito es la suma de la de sus artefactos."),
        ("¿Qué se hace si un circuito no declara su potencia?", "Se pide el dato al proyectista, sin inventarlo", "Un dato supuesto puede ocultar una sobrecarga."),
        ("¿Cuántos vatios son 2 kW?", "2000 W", "Un kilovatio equivale a 1000 vatios, así que 2 kW son 2000 W."),
    ],
    op=("Cuadro de ejemplo del proyecto «Panadería Luna» (ficticia, solo alumbrado y letrero): circuito A, alumbrado: 12 luces de 18 W; circuito B, letrero: 1 letrero de 250 W. El plano dibuja 14 luces. Escribe (a) la potencia de cada circuito, (b) la potencia total del cuadro, (c) qué hallazgo anotas y a quién lo informas, (d) la potencia total si el plano fuera el correcto.",
        "(a) A: 12 por 18 son 216 W; B: 250 W. (b) 216+250 son 466 W. (c) El cuadro dice 12 luces y el plano dibuja 14; lo informo al proyectista o supervisor. (d) 14 por 18 son 252 W, más 250 W: 502 W.",
        ["calcula bien la potencia de cada circuito", "suma el total", "anota el hallazgo sin decidir por su cuenta", "recalcula con el otro dato"],
        ["hoja con los cálculos y el registro del hallazgo"],
        ["usar la cantidad equivocada de luces", "sumar mal el total", "corregir un documento sin avisar"],
        "Pregunta: «¿por qué no corriges tú el cuadro?». Si no responde, pídele que relea qué hace el revisor con un hallazgo."),
    reinforce="Inventa un cuadro de tres circuitos con sus artefactos y potencias y calcula la potencia de cada uno y el total.",
    extend="Explica con un ejemplo por qué es peligroso rellenar con una cifra supuesta un dato que falta en un cuadro.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (especificación y catálogo de ejemplo, inventados). Proyecto «Pasillo Sur»: la especificación pide una luminaria de potencia máxima 18 W, tensión 220 V y vida útil de al menos 10.000 horas. "
     "Catálogo de ejemplo: opción A: 18 W, 220 V, 8.000 h, $2.500; opción B: 18 W, 220 V, 15.000 h, $3.200; opción C: 24 W, 220 V, 20.000 h, $3.000; opción D: 15 W, 220 V, 12.000 h, $3.600.")
build(
    O1, 4, F,
    use="Aprenderé a comparar una especificación con un catálogo, a relacionar potencia, tensión y corriente, y a registrar una decisión técnica.",
    prior=["Sé leer una especificación técnica.", "Sé calcular el costo de varias unidades.", "Sé qué es la potencia en vatios."],
    explain=[
        "La tensión se mide en voltios (V) y es el empuje que mueve la corriente. La corriente se mide en amperios (A) y es el flujo de carga eléctrica. La potencia en vatios es la tensión multiplicada por la corriente: P = V × I. Por eso la corriente se calcula dividiendo: I = P ÷ V. Si un artefacto sube su potencia con la misma tensión, su corriente aumenta, y más corriente significa más calentamiento de los conductores. La resistencia, en ohmios (Ω), es la dificultad al paso de la corriente; la ley de Ohm dice que V = I × R.",
        "Para elegir un componente se compara cada opción del catálogo con cada requisito de la especificación, uno por uno. La opción que falla en cualquiera se descarta. Solo entre las que cumplen todo se mira el precio. Si ninguna cumple, se informa; no se baja el requisito por cuenta propia, porque eso lo autoriza el proyectista o el supervisor. Toda decisión se anota en un registro con la opción elegida, los requisitos revisados y el precio.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("tensión", "empuje que mueve la corriente; se mide en voltios (V)"), ("corriente", "flujo de carga eléctrica; se mide en amperios (A)"), ("resistencia", "dificultad al paso de la corriente; se mide en ohmios (Ω)"), ("ley de Ohm", "V = I × R: la tensión es la corriente por la resistencia"), ("requisito", "condición que el componente debe cumplir"), ("catálogo", "lista de opciones con sus características y precios"), ("conductor", "cable o hilo de material conductor por donde circula la corriente")],
    worked=[
        ("Calcular la corriente", "Un artefacto de ejemplo de 880 W funciona a 220 V. ¿Cuántos amperios usa?", ["La corriente es la potencia dividida por la tensión.", "880 dividido por 220 son 4."], "4 A"),
        ("Calcular la resistencia", "Por un artefacto de ejemplo conectado a 12 V circulan 3 A. ¿Cuántos ohmios tiene?", ["La resistencia es la tensión dividida por la corriente.", "12 dividido por 3 son 4."], "4 Ω"),
    ],
    mistakes=[("Elegir la opción más barata aunque incumpla un requisito.", "El precio se mira solo entre las opciones que cumplen todo.", "Descarta primero lo que falla y compara precios después."),
              ("Creer que, si la tensión no cambia, más potencia no cambia la corriente.", "Con P = V × I, más potencia a igual tensión exige más corriente.", "Divide la potencia por la tensión para calcular la corriente.")],
    T=[
        ("abc", "En Electricidad: ¿qué relación une potencia, tensión y corriente?", "La potencia en vatios es la tensión en voltios multiplicada por la corriente en amperios", "La potencia es la tensión dividida por la corriente", "La potencia es la tensión sumada a la corriente", "La potencia se obtiene multiplicando tensión por corriente; dividir o sumar da otra magnitud."),
        ("=", "Un artefacto de ejemplo de 440 W funciona a 220 V. ¿Cuántos amperios de corriente usa?", "440//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("abc", "En Electricidad: si un artefacto aumenta su potencia y la tensión se mantiene, ¿qué ocurre con su corriente?", "Aumenta", "Disminuye", "Se mantiene igual", "Como I = P ÷ V, con la misma tensión una mayor potencia exige mayor corriente."),
        ("abc", "{F} ¿Cuántas opciones del catálogo cumplen la especificación completa?", "Dos: la B y la D", "Una: solo la B", "Tres: la B, la C y la D", "B y D cumplen los tres requisitos; A falla en vida útil y C en potencia."),
        ("abc", "{F} ¿Por qué se descarta la opción C?", "Su potencia de 24 W supera el máximo de 18 W", "Su vida útil de 20.000 horas es menor que la exigida", "Su tensión es distinta de 220 V", "C tiene 220 V y mucha vida útil; falla porque pasa de 18 W."),
        ("abc", "{F} ¿Qué requisito incumple la opción A?", "La vida útil: 8.000 horas es menos que las 10.000 exigidas", "La potencia: 18 W supera el máximo", "La tensión: no es de 220 V", "A tiene 18 W, igual al máximo, y 220 V; falla en las horas de vida útil."),
        ("abc", "{F} De las opciones que cumplen todo, ¿cuál es la más barata?", "La B, de $3.200", "La D, de $3.600", "La A, de $2.500", "Entre B y D gana B; la A es más barata pero no cumple la vida útil."),
        ("=", "{F} El proyecto lleva 12 luminarias de la opción más barata que cumple todo. ¿Cuánto cuestan?", "12*3200", "El precio de la opción B se multiplica por las 12 unidades.", " pesos"),
        ("=", "{F} Si se instalan 20 luminarias de la opción D, ¿cuántos vatios suman?", "15*20", "Se multiplica la potencia de una luminaria D por la cantidad.", " W"),
        ("abc", "{F} Un compañero dice que la opción C es la mejor porque tiene más horas de vida útil. ¿Qué respuesta es correcta?", "Incumple la potencia máxima; un requisito incumplido descarta la opción aunque otro dato sea mejor", "Tiene razón: más vida útil siempre compensa", "Tiene razón si el cliente acepta pagar más", "Un requisito se cumple o no se cumple; otro dato favorable no lo compensa."),
        ("ab", "{F} Un instalador propone cambiar la opción B por la A «porque cuesta menos y la diferencia de vida útil casi no se nota». ¿Qué corresponde?", "No: la A incumple la vida útil exigida; solo quien autoriza el proyecto puede modificar un requisito", "Sí: la diferencia de precio justifica ignorar el requisito", "Un requisito no se cambia por ahorro ni por cuenta propia; lo autoriza el proyectista o el supervisor."),
        ("=", "Un circuito de ejemplo alimenta dos artefactos, uno de 660 W y otro de 440 W, ambos a 220 V. ¿Cuántos amperios usa el circuito en total?", "(660+440)//220", "Se suman las potencias y se divide por la tensión.", " A"),
        ("=", "Un artefacto de ejemplo usa 2 A conectado a 220 V. Según la ley de Ohm, ¿cuántos ohmios tiene su resistencia?", "220//2", "La resistencia es la tensión dividida por la corriente.", " Ω"),
    ],
    ctx=("abc", "{F} En la bodega de un taller de ejemplo solo hay luminarias de 24 W, que «alumbran más». ¿Qué corresponde?", "No usarlas e informar que no cumplen la potencia máxima, pidiendo otras que cumplan", "Usarlas, porque alumbran más que las de 18 W", "Usarlas, porque la tensión coincide con la pedida", "Una luminaria de 24 W incumple el máximo de 18 W aunque coincidan otros datos."),
    sc=[
        ("En Electricidad: ¿cómo se calcula la corriente de un artefacto?", "Dividiendo su potencia por la tensión", "I = P ÷ V, por la relación entre potencia, tensión y corriente."),
        ("¿Qué se hace con una opción que falla en un requisito?", "Se descarta, aunque sea barata", "El precio solo se compara entre opciones que cumplen todo."),
        ("¿Qué se anota al registrar una decisión técnica?", "La opción elegida, los requisitos revisados y el precio", "El registro permite que otra persona repita la revisión."),
    ],
    op=("Especificación de ejemplo para un ventilador de extracción: potencia máxima 44 W, tensión 220 V y vida útil de al menos 20.000 horas. Catálogo de ejemplo: M: 44 W, 220 V, 15.000 h, $12.000; N: 44 W, 220 V, 25.000 h, $15.000; O: 66 W, 220 V, 30.000 h, $14.000; P: 44 W, 220 V, 30.000 h, $18.000. Escribe (a) qué opciones cumplen, (b) cuál eliges y por qué, (c) cuánto cuestan 6 unidades de la elegida, (d) cuántos amperios usan 5 ventiladores de 44 W a 220 V, (e) qué anotas en el registro.",
        "(a) N y P cumplen; M falla en vida útil y O en potencia. (b) N, porque cumple todo y es más barata que P. (c) 6 por 15.000 son 90.000 pesos. (d) 5 por 44 son 220 W; 220 dividido por 220 es 1 A. (e) Opción elegida (N), requisitos revisados (potencia, tensión, vida útil) y precio.",
        ["descarta las opciones que fallan con la razón", "elige la más barata entre las que cumplen", "calcula bien el costo", "calcula bien la corriente", "propone un registro completo"],
        ["hoja con la tabla de comparación, los cálculos y el registro"],
        ["elegir la más barata sin revisar requisitos", "dividir mal la potencia", "no dejar registro"],
        "Pregunta: «¿qué harías si ninguna opción cumpliera?». Si no responde, pídele que relea qué se hace cuando ninguna opción cumple."),
    reinforce="Inventa una especificación con tres condiciones para una lámpara y un catálogo de tres opciones; indica cuál cumple y por qué.",
    extend="Explica con un ejemplo por qué una luminaria de mayor potencia puede obligar a revisar los demás cálculos del circuito.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (archivo de dibujo descrito por escrito, de ejemplo, inventado). Archivo de dibujo «Local Esquina», revisión B, de una planta libre. Capas del archivo: 01-muros, 02-alumbrado, "
     "03-tomacorrientes, 04-cotas y 05-rótulo. Unidad del dibujo: centímetro. El archivo se imprime en papel para entregarlo al revisor.")
build(
    O2, 1, F,
    use="Aprenderé qué es el dibujo asistido por computador, por qué el plano debe cumplir la norma vigente y qué riesgos tiene un dibujo mal hecho, siempre en papel.",
    prior=["Sé leer un plano y su leyenda.", "Sé qué es una escala.", "Sé que un documento tiene versiones."],
    explain=[
        "El dibujo asistido por computador, llamado CAD, es una forma de dibujar planos con un programa en lugar de lápiz y papel. En este cuaderno no se usa ningún programa: se razona sobre archivos de dibujo descritos por escrito. Un archivo de dibujo se ordena en capas: grupos de elementos que se pueden mostrar u ocultar, como los muros o el alumbrado. Una planta libre es una planta sin tabiques interiores fijos, es decir, un espacio abierto. Cada versión del archivo se identifica con una letra de revisión, y el rótulo del plano la repite.",
        "Un plano debe aplicar la norma vigente en símbolos, rotulado y datos, y su fiscalización de seguridad corresponde a la SEC. Un dibujo mal hecho no es solo un error de forma: si una medida o un símbolo están equivocados, se compran materiales distintos y se ejecuta algo que puede causar descarga eléctrica o incendio. Por eso el dibujante no cambia nada aprobado por su cuenta: toda modificación pasa por el proyectista y genera una revisión nueva.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("CAD", "dibujo asistido por computador, forma de dibujar planos con un programa"), ("capa", "grupo de elementos del dibujo que se puede mostrar u ocultar"), ("planta libre", "planta sin tabiques interiores fijos; espacio abierto"), ("revisión", "versión del plano, identificada con una letra"), ("dibujante", "persona que dibuja el plano siguiendo las instrucciones del proyectista"), ("área", "medida de una superficie; el área de un rectángulo es largo por ancho, en metros cuadrados (m²)")],
    worked=[
        ("Elegir la capa", "En un archivo de ejemplo hay capas «01-muros» y «02-luces». ¿En qué capa va el símbolo de una lámpara?", ["Una lámpara es un artefacto de alumbrado.", "Su capa es la de luces."], "En la capa 02-luces"),
        ("Pasar de unidades", "Un archivo de ejemplo usa el centímetro como unidad. Un muro mide 500 unidades. ¿Cuántos metros reales mide?", ["500 centímetros reales.", "100 centímetros son 1 metro, así que 500 son 5 metros."], "5 m"),
    ],
    mistakes=[("Dibujar un símbolo de alumbrado en la capa de muros porque «se ve igual».", "Al ocultar los muros, el símbolo también desaparece y el plano queda incompleto.", "Dibuja cada elemento en su capa."),
              ("Modificar el archivo aprobado sin cambiar la letra de revisión.", "Habría dos planos distintos con el mismo nombre de versión.", "Genera una revisión nueva y regístrala.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una capa en un archivo de dibujo asistido?", "Un grupo de elementos del dibujo que se puede mostrar u ocultar, como los muros o el alumbrado", "Una hoja de papel adicional que se imprime aparte", "Una copia de seguridad del archivo", "La capa organiza los elementos del dibujo; no es una hoja ni una copia."),
        ("abc", "En Electricidad: ¿qué es una planta libre?", "Una planta sin tabiques interiores fijos, es decir, un espacio abierto", "Una planta que no tiene instalación eléctrica", "Una planta que no lleva cotas ni rótulo", "Planta libre se refiere al espacio sin tabiques fijos, no a la ausencia de instalación."),
        ("abc", "¿Para qué sirve la letra de revisión de un plano?", "Para saber cuál es la versión más reciente del plano", "Para indicar la escala de impresión", "Para indicar el orden de los circuitos", "La letra identifica la versión; la escala y los circuitos se indican en otros datos."),
        ("abc", "{F} ¿En qué capa debe dibujarse la posición de los puntos de luz?", "En la capa 02-alumbrado", "En la capa 01-muros", "En la capa 04-cotas", "La capa 02-alumbrado agrupa los elementos de alumbrado; muros y cotas son otros grupos."),
        ("abc", "{F} Un dibujante pone un tomacorriente en la capa 01-muros. ¿Qué problema genera?", "Al ocultar los muros, el tomacorriente también desaparece y el plano queda incompleto", "Ninguno, porque la capa solo cambia el color del símbolo", "El plano deja de poder imprimirse a escala", "Ocultar una capa oculta todo lo que contiene, incluido el tomacorriente mal ubicado."),
        ("abc", "{F} Se corrige un error del archivo y se guarda como revisión C, que luego se aprueba. ¿Cuál debe consultarse para ejecutar el trabajo?", "La revisión C, aprobada", "La revisión B, porque ya estaba impresa", "Ambas, por igual", "La versión aprobada más reciente reemplaza a las anteriores."),
        ("=", "{F} Un muro dibujado mide 800 unidades. ¿Cuántos metros reales mide?", "800//100", "La unidad es el centímetro y 100 cm forman 1 m.", " m"),
        ("=", "{F} Una planta libre de 9 m por 6 m, ¿cuántos m² de área tiene?", "9*6", "El área de un rectángulo es el largo por el ancho.", " m²"),
        ("=", "{F} El archivo se imprime a escala 1:100. Un muro real de 12 m, ¿cuántos centímetros mide en el papel?", "1200//100", "Se pasan 12 m a 1200 cm y se divide por la escala 100.", " cm"),
        ("ab", "{F} Un dibujante dice que no hace falta escribir la revisión en el rótulo porque «el nombre del archivo ya dice B». ¿Qué corresponde?", "Escribirla en el rótulo, porque el plano en papel circula sin el nombre del archivo", "No escribirla: el nombre del archivo basta para identificar el papel", "El papel impreso no muestra el nombre del archivo; por eso la revisión debe estar en el rótulo."),
        ("abc", "{F} Dos personas editan copias distintas de la revisión B y ambas la guardan como B. ¿Cuál es el riesgo?", "Habrá dos planos distintos con la misma identificación y se podría ejecutar el equivocado", "El archivo se vuelve más pequeño y pierde las capas", "Ninguno, porque ambas copias son la revisión B", "Dos versiones con el mismo nombre impiden saber cuál es la vigente."),
        ("=", "{F} El archivo tiene muros de 8 m y 6 m (un rectángulo) y se imprime a escala 1:50. ¿Cuántos centímetros mide el perímetro en el papel?", "2*(800+600)//50", "Se calcula el perímetro real en centímetros y se divide por la escala.", " cm"),
        ("abc", "{F} Un cliente pide agregar tomacorrientes, pero el archivo ya está aprobado. ¿Qué corresponde?", "Crear una nueva revisión, registrar el cambio y someterla a aprobación", "Modificar el archivo aprobado sin cambiar la letra", "Agregarlos a mano sobre el papel impreso", "Todo cambio genera una revisión nueva y se aprueba; el papel corregido a mano no es un plano válido."),
    ],
    ctx=("abc", "Un dibujante de ejemplo nota que un muro del archivo mide 3 m en el dibujo y 4 m en el cuadro de datos del proyecto. ¿Qué corresponde?", "Informar la diferencia al proyectista, que decide qué se corrige", "Dibujarlo en 4 m para que coincida con el cuadro", "Dejarlo en 3 m porque el dibujo es más importante", "Una diferencia entre el dibujo y los datos se informa; no se resuelve por cuenta propia."),
    sc=[
        ("En Electricidad: ¿para qué se usan las capas de un archivo de dibujo?", "Para ordenar los elementos y poder mostrarlos u ocultarlos por grupos", "Las capas organizan el dibujo por tipo de elemento."),
        ("¿Qué se hace al cambiar un plano ya aprobado?", "Se crea una revisión nueva y se somete a aprobación", "Así nunca coexisten dos planos distintos con la misma versión."),
        ("¿Cómo se calcula el área de una planta rectangular?", "Multiplicando el largo por el ancho", "Largo por ancho da los metros cuadrados."),
    ],
    op=("Archivo de ejemplo «Taller Sur», revisión A, planta libre de 10 m por 4 m, unidad del dibujo: centímetro, escala de impresión 1:50. Capas: 01-muros, 02-alumbrado, 03-tomacorrientes. Se dibujó un tomacorriente en la capa 02-alumbrado. Escribe (a) el área de la planta, (b) cuántos centímetros mide en el papel el largo de 10 m, (c) qué problema genera el tomacorriente mal ubicado, (d) qué letra tendría el archivo si se corrige el error y se aprueba.",
        "(a) 10 por 4 son 40 m². (b) 1000 dividido por 50 son 20 cm. (c) El tomacorriente quedaría mezclado con el alumbrado: al ocultar o revisar esa capa el plano se interpretaría mal. (d) Revisión B.",
        ["calcula bien el área", "aplica bien la escala", "explica el problema de la capa", "indica la nueva revisión"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar por la escala en vez de dividir", "decir que la capa no importa", "mantener la letra A"],
        "Pregunta: «¿qué pasaría al ocultar la capa de alumbrado?». Si no responde, pídele que relea qué es una capa."),
    reinforce="Escribe una lista de cuatro capas para un dibujo de planta y, junto a cada una, qué elementos contendría.",
    extend="Explica con un ejemplo por qué una revisión sin registrar puede causar que se ejecute el plano equivocado.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (lista de elementos de un dibujo, de ejemplo, inventada). Dibujo «Sala Común», planta libre de 10 m por 6 m, unidad del dibujo: centímetro. "
     "Bloques insertados: «luz» 12 veces en la capa 02-alumbrado; «toma» 8 veces en la capa 03-tomacorrientes; «interruptor» 2 veces en la capa 02-alumbrado. "
     "Cotas en la capa 04-cotas: largo 1000 y ancho 600. Rótulo: escala 1:50, revisión A.")
build(
    O2, 2, F,
    use="Aprenderé qué son los bloques, las cotas y la escala de impresión de un dibujo, y a leer una lista de elementos de un archivo.",
    prior=["Sé qué es una capa y una revisión.", "Sé aplicar una escala.", "Sé multiplicar y sumar."],
    explain=[
        "Un bloque es un símbolo guardado que se inserta muchas veces en el dibujo, como el de un tomacorriente. Su ventaja es que todos los símbolos quedan iguales y, si se corrige la definición del bloque, se actualizan todos los insertados. Un símbolo dibujado a mano, aunque se vea igual, no es parte del bloque y no se actualiza. Las cotas son números que indican las medidas del recinto; en el archivo de la ficha, 1000 con unidad centímetro son 10 m.",
        "La escala de impresión debe coincidir con la que dice el rótulo. Si se imprime a otra escala sin avisar, quien mide en el papel obtiene valores falsos. Una lista de elementos resume qué bloques hay, cuántos y en qué capa, y sirve para comparar el dibujo con la lista de materiales. Cuando una cantidad no coincide, se informa al proyectista.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("bloque", "símbolo guardado que se inserta muchas veces en el dibujo"), ("cota", "número que indica una medida del recinto"), ("escala de impresión", "razón con que se imprime el dibujo; debe coincidir con el rótulo"), ("lista de elementos", "resumen de qué bloques hay, cuántos y en qué capa"), ("definición del bloque", "dibujo original del que se copian todos los símbolos insertados"), ("conductor", "cable o hilo de material conductor por donde circula la corriente")],
    worked=[
        ("Actualizar un bloque", "Un dibujo de ejemplo tiene 9 bloques «lámpara». Se corrige su definición. ¿Cuántos símbolos quedan corregidos?", ["Todos los bloques insertados dependen de la misma definición.", "Se actualizan los 9."], "9 símbolos"),
        ("Leer una cota", "Una cota de ejemplo dice 450 y la unidad del dibujo es el centímetro. ¿Cuántos metros son?", ["La cota indica 450 centímetros.", "450 dividido por 100 da 4,5 metros."], "4,5 m"),
    ],
    mistakes=[("Pensar que un símbolo dibujado a mano se actualiza con el bloque.", "Solo los bloques insertados comparten la definición.", "Inserta siempre el bloque en lugar de copiar el dibujo."),
              ("Imprimir a otra escala y dejar el rótulo con la escala anterior.", "Quien mida en el papel obtendrá medidas falsas.", "Haz coincidir el rótulo con la escala de impresión o informa el cambio.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un bloque en un archivo de dibujo asistido?", "Un símbolo guardado que se puede insertar muchas veces, como el de un tomacorriente", "Un muro dibujado con grosor especial", "Un candado que impide editar el archivo", "El bloque es un símbolo reutilizable; no es un muro ni una protección del archivo."),
        ("abc", "En Electricidad: ¿qué ventaja tiene usar un bloque en lugar de dibujar cada símbolo a mano?", "Todos los símbolos quedan iguales y, si se corrige el bloque, se actualizan todos", "El dibujo ocupa menos papel al imprimirse", "Los símbolos dejan de necesitar leyenda", "La ventaja es la uniformidad y la actualización conjunta; la leyenda sigue siendo necesaria."),
        ("=", "En un archivo de ejemplo con unidad en centímetros, una cota indica 600. ¿Cuántos metros son?", "600//100", "Cien centímetros forman un metro.", " m"),
        ("=", "{F} ¿Cuántos símbolos de la capa 02-alumbrado tiene el dibujo, sumando luces e interruptores?", "12+2", "Se suman los 12 bloques «luz» y los 2 bloques «interruptor».", " símbolos"),
        ("abc", "{F} ¿Qué medida del recinto marca la cota 1000?", "Los 10 m de largo", "Los 10 cm de largo", "Los 6 m de ancho", "La unidad es el centímetro: 1000 cm son 10 m, y el ancho es la cota 600."),
        ("abc", "{F} El dibujo tiene 8 tomacorrientes y la lista de materiales pide 9. ¿Qué indica?", "Hay una diferencia que debe informarse al proyectista", "El dibujo está bien, porque la lista siempre trae uno de repuesto", "El dibujo está incompleto y se agrega un bloque sin consultar", "Una diferencia entre documentos se informa; no se explica con repuestos supuestos ni se corrige solo."),
        ("=", "{F} Si cada punto de luz de ejemplo usa 18 W, ¿cuántos vatios suman los 12 puntos de luz?", "12*18", "Se multiplica la potencia de un punto por la cantidad de puntos.", " W"),
        ("=", "{F} ¿Cuántos centímetros mide en el papel el largo del recinto a la escala del rótulo?", "1000//50", "El largo real en centímetros se divide por la escala 50.", " cm"),
        ("=", "{F} Se corrige la definición del bloque «luz» y se agrega una luz nueva. ¿Cuántos bloques «luz» quedan en total, todos con el símbolo corregido?", "12+1", "Se suman los 12 existentes y el nuevo, todos comparten la definición.", " bloques"),
        ("abc", "{F} El rótulo dice 1:50 pero se imprimió a 1:100 sin avisar. Un técnico mide 10 cm en el papel para el largo y usa la escala del rótulo. ¿Qué error comete?", "Obtiene 500 cm en vez de los 1000 cm reales, porque la impresión no coincide con el rótulo", "Obtiene 100 cm, porque multiplica los 10 cm por 10", "Ninguno, porque el rótulo siempre manda sobre el tamaño del papel", "Con impresión a 1:100, 10 cm equivalen a 1000 cm; usar 1:50 da 500 cm."),
        ("ab", "{F} Un dibujante cambió 3 de los 8 tomacorrientes por símbolos copiados a mano. Al actualizar el bloque, ¿qué ocurre con esos 3?", "No se actualizan y el dibujo queda con símbolos distintos", "Se actualizan igual que los demás", "Solo los bloques insertados comparten la definición; los símbolos copiados a mano no cambian."),
        ("=", "{F} Cada tomacorriente de ejemplo se alimenta con 3 m de conductor y cada punto de luz con 4 m. ¿Cuántos metros de conductor suman los 8 tomacorrientes y las 12 luces?", "8*3+12*4", "Se suman los metros de los tomacorrientes y los de las luces.", " m"),
        ("abc", "{F} El proyectista cambia el largo a 1200 cm. ¿Qué elementos del archivo deben revisarse además de la cota?", "La escala de impresión, la posición de los bloques y la lista de materiales", "Solo el nombre del archivo", "Ninguno, porque cambiar una cota actualiza todo lo demás automáticamente", "Un cambio de medida puede alterar escala, ubicación de símbolos y cantidades."),
    ],
    ctx=("abc", "Un dibujante de ejemplo no sabe si usar el bloque «interruptor» antiguo o uno nuevo con otro símbolo. ¿Qué corresponde?", "Consultar al proyectista cuál es el vigente según la leyenda aprobada", "Usar el que se vea más claro", "Usar los dos para estar seguro", "El símbolo vigente lo fija la leyenda aprobada; mezclar símbolos confunde al lector."),
    sc=[
        ("En Electricidad: ¿qué es un bloque?", "Un símbolo guardado que se inserta muchas veces", "El bloque permite repetir y actualizar símbolos iguales."),
        ("¿Qué debe coincidir con la escala de impresión?", "La escala escrita en el rótulo", "Si no coinciden, las medidas del papel dan valores falsos."),
        ("¿Qué se hace si el dibujo y la lista de materiales no coinciden?", "Se informa al proyectista", "El proyectista decide cuál documento se corrige."),
    ],
    op=("Lista de ejemplo del dibujo «Bodega Verde»: planta libre de 8 m por 5 m, unidad: centímetro; bloque «luz» 6 veces; bloque «toma» 5 veces; cotas: 800 y 500; rótulo: escala 1:50, revisión A. La lista de materiales pide 6 luces y 6 tomacorrientes. Escribe (a) cuántos centímetros mide en el papel el largo, (b) cuántos metros reales indica la cota 500, (c) qué diferencia hay con la lista de materiales y qué haces, (d) cuántos metros de conductor se estiman si cada luz lleva 4 m y cada tomacorriente 3 m según el dibujo.",
        "(a) 800 dividido por 50 son 16 cm. (b) 500 cm son 5 m. (c) La lista pide 6 tomacorrientes y el dibujo tiene 5: informo la diferencia al proyectista. (d) 6 por 4 son 24 m y 5 por 3 son 15 m: 39 m.",
        ["aplica bien la escala", "convierte bien la cota", "detecta la diferencia y la informa", "calcula bien los metros"],
        ["hoja con las cuatro respuestas y los cálculos"],
        ["no dividir por la escala", "usar la cantidad de la lista", "corregir sin avisar"],
        "Pregunta: «¿por qué informas en lugar de corregir?». Si no responde, pídele que relea qué se hace cuando las cantidades no coinciden."),
    reinforce="Escribe una lista de elementos con tres bloques, sus cantidades y sus capas, para un dibujo imaginario de una sala.",
    extend="Explica con un ejemplo por qué es útil que todos los símbolos iguales de un plano vengan de un mismo bloque.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (informe de revisión de un dibujo, de ejemplo, inventado). Dibujo «Bodega Lila», planta libre de 12 m por 5 m, escala del rótulo 1:50, revisión C. "
     "Hallazgos de la revisión: (1) 6 luces dibujadas en la capa 01-muros; (2) cotas de largo 1200 y de ancho 500, unidad centímetro; (3) la lista de materiales pide 7 luces y el dibujo muestra 6; "
     "(4) el rótulo no tiene fecha. Criterio de ejemplo de la planilla: 1 punto de luz por cada 10 m² de planta.")
build(
    O2, 3, F,
    use="Aprenderé a revisar un dibujo con una lista de hallazgos, a aplicar un criterio de planilla y a decidir qué se corrige antes de aprobar.",
    prior=["Sé qué son capas, bloques y revisiones.", "Sé calcular el área de un rectángulo.", "Sé aplicar una escala."],
    explain=[
        "Revisar un dibujo significa compararlo con la lista de materiales, el cuadro de datos y las reglas del proyecto, y anotar cada hallazgo: una diferencia o falta que se corrige antes de aprobar. Un informe de revisión numera los hallazgos, dice dónde están y quién debe corregirlos. Los datos del rótulo, como la fecha, son parte del plano: sin ellos no se puede distinguir una versión de otra.",
        "Un criterio de planilla es una regla de cálculo que usa el proyecto: aquí, de ejemplo, 1 punto de luz por cada 10 m² de planta. No es una norma: es un valor de ejemplo para practicar. El área de una planta rectangular es largo por ancho, en metros cuadrados. Cuando se corrigen los hallazgos, el archivo pasa a la letra de revisión siguiente (A, B, C, D…) y se vuelve a revisar.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("hallazgo", "diferencia o falta detectada que se anota para corregirla"), ("informe de revisión", "lista numerada de hallazgos con su ubicación y responsable"), ("criterio de planilla", "regla de cálculo de ejemplo que usa el proyecto"), ("área", "medida de una superficie, en metros cuadrados (m²)"), ("aprobar", "dar por correcto un plano para que pase a la etapa siguiente")],
    worked=[
        ("Aplicar un criterio", "Con un criterio de ejemplo de 1 punto de luz cada 8 m², ¿cuántos puntos corresponden a una planta de 6 m por 8 m?", ["El área es 6 por 8, es decir, 48 m².", "48 dividido por 8 son 6 puntos."], "6 puntos de luz"),
        ("Pasar a la letra siguiente", "Un archivo de ejemplo está en revisión E y se corrige y aprueba. ¿Qué letra sigue?", ["Las revisiones siguen el orden del abecedario.", "Después de la E viene la F."], "Revisión F"),
    ],
    mistakes=[("Aprobar un plano sin fecha porque «es solo un detalle del rótulo».", "Sin fecha no se distinguen las versiones.", "Corrige el rótulo antes de aprobar."),
              ("Tomar un criterio de planilla de ejemplo como si fuera una norma.", "Es un valor para practicar el cálculo, no un requisito real.", "Para el requisito real consulta la norma vigente.")],
    T=[
        ("abc", "En Electricidad: ¿qué es un hallazgo en una revisión de planos?", "Una diferencia o falta detectada que se anota para corregirla", "Una medida tomada en obra", "La firma de aprobación del plano", "El hallazgo es lo que se detecta en la revisión; la firma es posterior."),
        ("abc", "En Electricidad: ¿cómo se calcula el área de una planta rectangular?", "Multiplicando el largo por el ancho, en metros cuadrados", "Sumando el largo y el ancho, en metros", "Sumando el doble del largo y el doble del ancho", "El área es largo por ancho; sumar da otra medida, el perímetro."),
        ("abc", "En Electricidad: ¿para qué sirve la fecha del rótulo?", "Para distinguir esa versión del plano de otras", "Para calcular el costo del plano", "Para fijar el plazo en que debe ejecutarse la obra", "La fecha identifica la versión; el costo y el plazo van en otros documentos."),
        ("=", "{F} ¿Cuántos m² de área tiene la planta de la ficha?", "12*5", "El área es el largo por el ancho.", " m²"),
        ("=", "{F} Según el criterio de ejemplo de la planilla, ¿cuántos puntos de luz corresponden a la planta?", "(12*5)//10", "Se calcula el área y se divide por 10 m² por punto.", " puntos"),
        ("abc", "{F} ¿Qué problema tiene el hallazgo (1)?", "Las luces están en la capa de muros y desaparecerían al ocultar los muros", "Las luces son demasiado pequeñas para el plano", "Las luces no están numeradas en el rótulo", "Cada elemento debe ir en su capa; las luces en muros se ocultan con ellos."),
        ("=", "{F} La lista de materiales pide 7 luces a $1.800 cada una y 8 tomacorrientes a $900 cada uno. ¿Cuánto suma lo pedido en la lista?", "7*1800+8*900", "Se suma el costo de las luces y el de los tomacorrientes.", " pesos"),
        ("=", "{F} ¿Cuántos centímetros mide en el papel el largo de la planta, a la escala del rótulo?", "1200//50", "El largo real en centímetros se divide por la escala.", " cm"),
        ("abc", "{F} ¿Quién debe decidir si se corrige la lista de materiales o el dibujo por la diferencia de luces?", "El proyectista o el supervisor del proyecto", "El dibujante, porque conoce el archivo", "El proveedor de los materiales", "La decisión de qué documento cambia la toma quien diseña o supervisa."),
        ("abc", "{F} Un revisor propone aprobar «porque el hallazgo (4) es solo un detalle del rótulo». ¿Qué respuesta es correcta?", "No: sin fecha no se distingue esta revisión de otras; debe corregirse antes de aprobar", "Sí: el rótulo no afecta la seguridad del proyecto", "Sí, siempre que se agregue la fecha después de ejecutar la obra", "La fecha es un dato de identificación del plano y se completa antes de aprobar."),
        ("ab", "{F} Un compañero dice que el criterio de la planilla (1 luz cada 10 m²) es la norma oficial. ¿Qué corresponde?", "Aclarar que es un valor de ejemplo y que el requisito real lo fija la norma vigente", "Aceptarlo, porque si está en una planilla es norma", "Un criterio de planilla de ejemplo sirve para practicar el cálculo y no reemplaza la norma vigente."),
        ("=", "{F} Si la bodega se ampliara a 15 m por 6 m, ¿cuántos puntos de luz corresponderían con el criterio de ejemplo?", "(15*6)//10", "El área ampliada se divide por 10 m² por punto.", " puntos"),
        ("abc", "{F} Se corrigen los cuatro hallazgos y se genera una nueva versión que se aprueba. ¿Qué letra de revisión corresponde, si se sigue la secuencia A, B, C…?", "Revisión D", "Revisión C", "Revisión B", "Después de la C sigue la D en el abecedario."),
    ],
    ctx=("abc", "Una revisora de ejemplo encuentra que un dibujo tiene un muro de 5 m en el plano y 6 m en el cuadro de datos. El cliente le pide aprobarlo igual «para no atrasar la obra». ¿Qué corresponde?", "No aprobarlo y registrar el hallazgo para que el proyectista lo resuelva", "Aprobarlo y corregirlo más adelante", "Aprobarlo si el cliente firma una nota", "Un plano con una diferencia sin resolver no se aprueba; la presión por plazos no la elimina."),
    sc=[
        ("En Electricidad: ¿qué es un informe de revisión?", "Una lista numerada de hallazgos con su ubicación y responsable", "El informe ordena lo que hay que corregir y quién lo corrige."),
        ("¿Qué letra sigue a la revisión C?", "La D", "Las revisiones siguen el orden del abecedario."),
        ("¿Un criterio de planilla de ejemplo es una norma?", "No, sirve para practicar el cálculo", "La norma real la fija la norma vigente."),
    ],
    op=("Informe de revisión de ejemplo del dibujo «Sala Norte», planta libre de 10 m por 8 m, escala del rótulo 1:50, revisión B. Hallazgos: (1) la lista de materiales pide 9 luces; (2) el rótulo no indica la escala; (3) 2 tomacorrientes están dibujados en la capa de alumbrado. Criterio de ejemplo: 1 punto de luz por cada 10 m². Escribe (a) el área de la planta, (b) cuántos puntos de luz corresponden con el criterio, (c) qué hallazgos hay con la cantidad de luces, (d) qué hallazgo corresponde al rótulo y cuál a las capas, (e) qué letra tendría la versión corregida y aprobada.",
        "(a) 10 por 8 son 80 m². (b) 80 dividido por 10 son 8 puntos. (c) La lista pide 9 y el criterio da 8: sobra 1 luz y se informa al proyectista. (d) El hallazgo 2 es del rótulo y el 3 de las capas. (e) Revisión C.",
        ["calcula bien el área", "aplica bien el criterio", "reconoce la diferencia de cantidades", "clasifica los hallazgos", "indica la letra siguiente"],
        ["hoja con las cinco respuestas"],
        ["sumar en vez de multiplicar el área", "tomar el criterio como norma", "aprobar con hallazgos abiertos"],
        "Pregunta: «¿puedes aprobar el plano con el rótulo incompleto?». Si no responde, pídele que relea el papel del rótulo."),
    reinforce="Escribe un informe de revisión de ejemplo con tres hallazgos para un dibujo imaginario, indicando dónde está cada uno.",
    extend="Explica con un ejemplo por qué aprobar un plano con hallazgos pendientes puede traer riesgos en la ejecución.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (criterios de impresión de ejemplo, inventados). Se debe imprimir en una lámina cuya área de dibujo útil mide 40 cm de ancho por 28 cm de alto. "
     "Escalas permitidas por la empresa de ejemplo: 1:20, 1:50 y 1:100. Recinto «Gimnasio Chico»: planta libre de 18 m por 9 m. "
     "Regla de la empresa: se usa la escala más grande (la que dibuja más grande) que permita que todo el recinto quepa en la lámina.")
build(
    O2, 4, F,
    use="Aprenderé a elegir la escala de impresión de un plano con un criterio, a verificar que el dibujo cabe en la lámina y a dejar una lista de verificación.",
    prior=["Sé aplicar una escala.", "Sé qué es una planta libre.", "Sé que un plano debe revisarse antes de aprobarse."],
    explain=[
        "Elegir la escala es decidir cuánto se reduce el recinto para dibujarlo en el papel. Una escala es más grande cuando el dibujo sale de mayor tamaño en el papel: 1:20 es más grande que 1:50, aunque el número de la derecha sea menor. Para saber si un dibujo cabe, se divide cada medida real, en centímetros, por el número de la escala y se compara con el área útil de la lámina. Si no cabe, se elige una escala más reducida o se divide el dibujo en dos láminas.",
        "Una lista de verificación es una tabla de preguntas que se revisa antes de entregar un plano: escala del rótulo igual a la escala de impresión, revisión y fecha visibles, símbolos en su capa, cantidades iguales a las de la lista de materiales. Se marca cada punto y se firma; si uno falla, no se entrega. Las escalas de esta ficha son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("escala más grande", "la que dibuja el recinto de mayor tamaño en el papel, como 1:20 frente a 1:50"), ("área útil", "parte de la lámina donde cabe el dibujo"), ("lista de verificación", "tabla de preguntas que se revisa antes de entregar"), ("lámina", "hoja en que se imprime el plano")],
    worked=[
        ("Ver si cabe", "Un muro real de 6 m, dibujado a 1:20, ¿cuántos centímetros mide en el papel y cabe en una lámina útil de 40 cm?", ["600 cm reales dividido por 20 son 30 cm.", "30 es menor que 40."], "Mide 30 cm y cabe"),
        ("Elegir la escala", "Un recinto de 15 m de largo debe caber en 40 cm útiles. ¿Sirve 1:20 o 1:50?", ["A 1:20 el largo mide 75 cm, más que 40.", "A 1:50 mide 30 cm, que cabe."], "Sirve 1:50"),
    ],
    mistakes=[("Pensar que 1:100 es una escala más grande que 1:20 porque el número es mayor.", "Con 1:100 el dibujo sale más pequeño en el papel.", "Compara el tamaño del dibujo en el papel, no el número."),
              ("Elegir 1:100 siempre «para que nunca falle».", "Puede volver ilegibles los detalles pequeños.", "Usa la escala más grande que permita que todo quepa.")],
    T=[
        ("abc", "En Electricidad: ¿qué significa que una escala sea «más grande»?", "Que el dibujo sale de mayor tamaño en el papel, como 1:20 frente a 1:50", "Que el número después de los dos puntos es mayor", "Que el recinto real es más grande", "Una escala es más grande cuando dibuja más grande; el número mayor indica más reducción."),
        ("=", "Un muro real de 10 m se dibuja a escala 1:50. ¿Cuántos centímetros mide en el papel?", "1000//50", "Se pasa a centímetros y se divide por 50.", " cm"),
        ("abc", "¿Qué ocurre si el dibujo no cabe en el área útil de la lámina?", "Hay que elegir una escala más reducida o dividir el dibujo en dos láminas", "Se mantiene la escala y se acepta que quede cortado", "Se cambia solo el número de la escala en el rótulo, sin tocar el dibujo", "El dibujo debe caber completo; cambiar solo el rótulo dejaría una escala falsa."),
        ("=", "{F} Con la escala 1:20, ¿cuántos centímetros mediría en el papel el largo de 18 m?", "1800//20", "Se divide la medida real en centímetros por 20.", " cm"),
        ("abc", "{F} ¿Por qué no sirve la escala 1:20 para este recinto?", "El largo saldría de 90 cm, más que los 40 cm útiles de la lámina", "El dibujo saldría tan pequeño que no se leería", "La empresa no permite esa escala", "1:20 está permitida, pero el largo no cabe en la lámina."),
        ("=", "{F} Con la escala 1:100, ¿cuántos centímetros mediría en el papel el largo del recinto?", "1800//100", "Se divide la medida real en centímetros por 100.", " cm"),
        ("=", "{F} Con la escala 1:50, ¿cuántos centímetros mediría en el papel el ancho de 9 m?", "900//50", "Se divide el ancho real en centímetros por 50.", " cm"),
        ("abc", "{F} ¿Qué escala corresponde según la regla de la empresa?", "1:50", "1:100", "1:20", "1:50 es la mayor que cabe; 1:20 no cabe y 1:100 cabe pero no es la más grande."),
        ("=", "{F} Con la escala elegida, ¿cuántos centímetros sobran en el alto útil de la lámina?", "28-900//50", "Al alto útil de 28 cm se le resta lo que ocupa el ancho del recinto dibujado.", " cm"),
        ("abc", "{F} El recinto se amplía a 22 m de largo, con el mismo ancho. ¿Qué escala corresponde ahora?", "1:100", "1:50", "1:20", "A 1:50 el largo sería de 44 cm y no cabe en 40 cm; a 1:100 mide 22 cm y cabe."),
        ("abc", "{F} Un compañero dice: «usemos 1:100 siempre, así nunca falla». ¿Qué respuesta es correcta?", "Cabe casi siempre, pero puede volver ilegibles los detalles pequeños; por eso la regla pide la escala más grande que quepa", "Es correcto, porque 1:100 es la única escala permitida", "Es incorrecto, porque 1:100 nunca cabe", "La regla busca el dibujo más grande posible que quepa, para que se lea bien."),
        ("=", "{F} En el papel, un cable dibujado a la escala elegida mide 24 cm. ¿Cuántos metros reales representa?", "24*50//100", "Se multiplica por 50 para pasar a centímetros reales y se divide por 100 para pasar a metros.", " m"),
        ("abc", "{F} Antes de enviar a imprimir, la revisora usa una lista de verificación. ¿Qué punto es útil?", "Que la escala del rótulo sea igual a la de impresión y que la revisión y la fecha se vean", "Que el nombre del archivo tenga menos de 10 letras", "Que el dibujo use el mayor número posible de colores", "La lista comprueba datos que afectan la lectura y la trazabilidad del plano."),
    ],
    ctx=("abc", "{F} El jefe del taller de ejemplo pide imprimir el gimnasio a 1:20 «para que se vea grande». ¿Qué corresponde?", "Explicar que a 1:20 el largo mide 90 cm y no cabe en la lámina; usar 1:50 o dividir en láminas", "Imprimir igual y dejar que se corte el dibujo", "Cambiar el rótulo a 1:50 pero imprimir a 1:20", "Un dibujo cortado o un rótulo falso dejan un plano inseguro; se elige una escala que quepa."),
    sc=[
        ("En Electricidad: ¿cómo se sabe si un recinto cabe en la lámina a una escala?", "Dividiendo cada medida real en centímetros por la escala y comparando con el área útil", "El resultado es la medida en el papel."),
        ("¿Es 1:20 una escala más grande que 1:100?", "Sí, porque dibuja más grande en el papel", "Un número menor después de los dos puntos reduce menos."),
        ("¿Para qué sirve una lista de verificación antes de imprimir?", "Para comprobar escala, revisión, fecha y capas antes de entregar", "Así se detectan errores antes de que lleguen a quien ejecuta."),
    ],
    op=("Datos de ejemplo: lámina con área útil de 40 cm por 28 cm; escalas permitidas 1:20, 1:50 y 1:100; regla: la escala más grande que haga caber todo. Recinto «Taller Alto»: planta libre de 16 m por 6 m. Escribe (a) cuántos centímetros mediría el largo a cada una de las tres escalas, (b) cuáles cabrían en el ancho útil de 40 cm, (c) qué escala eliges y por qué, (d) tres puntos de una lista de verificación para este plano.",
        "(a) 1600 dividido por 20 son 80 cm; por 50, 32 cm; por 100, 16 cm. (b) 1:50 y 1:100. (c) 1:50, porque es la mayor que cabe. (d) Por ejemplo: escala del rótulo igual a la de impresión, revisión y fecha visibles, símbolos en su capa.",
        ["calcula las tres medidas", "compara con el área útil", "aplica la regla de la escala más grande", "propone puntos de verificación útiles"],
        ["hoja con la tabla de cálculos, la decisión y la lista"],
        ["elegir 1:100 por seguridad", "usar el ancho en vez del largo", "proponer puntos no verificables"],
        "Pregunta: «¿por qué no eliges 1:100?». Si no responde, pídele que relea la regla de la escala más grande."),
    reinforce="Inventa un recinto de dos medidas y calcula cuánto medirá en el papel a las tres escalas de la ficha; indica cuál elegirías.",
    extend="Explica con un ejemplo por qué una escala demasiado reducida puede ser un problema para quien lee el plano.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (local de ejemplo, inventado). «Sala de Estudio Alba» (ficticia): alumbrado de un local con 40 luminarias de 25 W cada una. "
     "El OA nombra instalaciones de alumbrado de hasta 10 kW de potencia instalada total. Tensión de ejemplo: 220 V. "
     "Documentos del proyecto: plano, memoria de cálculo y presupuesto con cubicación de materiales y mano de obra.")
build(
    O3, 1, F,
    use="Aprenderé qué es una instalación de alumbrado de baja tensión de hasta 10 kW, qué documentos la respaldan y por qué la ejecuta solo personal autorizado.",
    prior=["Sé qué documentos forman un proyecto.", "Sé qué es la potencia en vatios.", "Sé multiplicar y dividir."],
    explain=[
        "Una instalación de alumbrado es la parte de la instalación eléctrica que alimenta las luminarias de un recinto. El objetivo de aprendizaje habla de baja tensión, hasta 10 kW de potencia instalada total y sin alimentadores. La potencia instalada total es la suma de las potencias de todos los artefactos conectados. Un alimentador es una línea que lleva la energía a un tablero secundario; este objetivo se refiere a instalaciones que no los necesitan. 1 kW son 1000 W.",
        "El proyecto reúne el plano, la memoria de cálculo y el presupuesto con cubicación. La cubicación es el cálculo de las cantidades de materiales y de mano de obra, que es el trabajo humano medido en horas. La ejecución la realiza personal autorizado con la norma vigente de la SEC; el proyecto describe qué se hará, pero no reemplaza esa autorización. Dividir una instalación en partes para que cada una parezca bajo el límite es una forma de eludirlo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("instalación de alumbrado", "parte de la instalación eléctrica que alimenta las luminarias"), ("potencia instalada total", "suma de las potencias de todos los artefactos conectados"), ("kW", "kilovatio, equivalente a 1000 W"), ("cubicación", "cálculo de las cantidades de materiales y de mano de obra"), ("mano de obra", "trabajo humano necesario, medido en horas"), ("alimentador", "línea que lleva la energía a un tablero secundario")],
    worked=[
        ("Potencia instalada", "Un local de ejemplo tiene 30 luminarias de 20 W. ¿Cuál es su potencia instalada?", ["Se multiplica la potencia de una luminaria por la cantidad.", "30 por 20 son 600."], "600 W"),
        ("Pasar a kW", "Un local de ejemplo suma 4500 W. ¿Cuántos kW son?", ["1 kW son 1000 W.", "4500 dividido por 1000 son 4,5."], "4,5 kW"),
    ],
    mistakes=[("Dividir un proyecto de 12 kW en dos de 6 kW para que parezca bajo el límite.", "El criterio es la potencia instalada total de la instalación.", "Suma toda la potencia y informa si supera el límite."),
              ("Pensar que, por ser solo luces, la instalación no tiene riesgos.", "Una instalación mal hecha puede causar descarga o incendio.", "La ejecuta personal autorizado según la norma vigente.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la potencia instalada total de un local?", "La suma de las potencias de todos los artefactos que quedan conectados", "La potencia del artefacto más grande", "La potencia que realmente se usa cada día", "Es la suma de todas las potencias conectadas, no la mayor ni el uso diario."),
        ("=", "Un local de ejemplo tiene 6 artefactos de 250 W cada uno. ¿Cuántos vatios de potencia instalada suman?", "6*250", "Se multiplica la potencia de un artefacto por la cantidad.", " W"),
        ("abc", "En Electricidad: ¿qué documento muestra los cálculos con que se definió una instalación de alumbrado?", "La memoria de cálculo", "El presupuesto", "La lista de rótulos del tablero", "La memoria contiene los cálculos; el presupuesto reúne costos."),
        ("=", "{F} ¿Cuántos vatios de potencia instalada suman las luminarias de la ficha?", "40*25", "Se multiplica la potencia de una luminaria por la cantidad.", " W"),
        ("=", "{F} ¿Cuántas veces cabe la potencia instalada de la ficha en el límite de 10 kW?", "10000//(40*25)", "Se pasa el límite a vatios y se divide por la potencia instalada.", " veces"),
        ("abc", "{F} ¿Qué documento respalda las cantidades de materiales y de mano de obra?", "El presupuesto con cubicación de materiales y mano de obra", "El plano, porque dibuja las luminarias", "La memoria de cálculo, porque contiene precios", "La cubicación y los costos están en el presupuesto."),
        ("=", "{F} El local agrega 20 luminarias más de 25 W. ¿Cuántos vatios de potencia instalada tendrá?", "(40+20)*25", "Se suman las luminarias y se multiplica por la potencia de cada una.", " W"),
        ("=", "{F} El presupuesto de ejemplo estima 25 horas de mano de obra a $4.000 la hora. ¿Cuánto cuesta la mano de obra?", "25*4000", "Se multiplican las horas por el valor de cada hora.", " pesos"),
        ("abc", "Un local ampliado de ejemplo llegaría a 12 kW de potencia instalada. ¿Qué corresponde frente al límite del OA?", "Reconocer que supera los 10 kW y que ya no es el caso del OA, por lo que se informa al proyectista", "Seguir igual, porque 2 kW más no importan", "Dividir la potencia en dos proyectos para que el total parezca menor", "Superar el límite cambia el tipo de proyecto; dividirlo es eludir el criterio."),
        ("abc", "Un dueño dice: «son solo luces de 25 W, así que no hay riesgo y lo hago yo». ¿Qué respuesta es correcta?", "Una instalación fija de alumbrado tiene riesgo de descarga e incendio y la ejecuta personal autorizado según la norma vigente", "Tiene razón: las luces de baja potencia no tienen riesgo", "Tiene razón si se pone un cartel de aviso", "El riesgo existe aunque la potencia de cada luz sea baja; la norma vigente exige personal autorizado."),
        ("ab", "{F} Un compañero dice que se puede ignorar la memoria de cálculo porque «ya sabemos que son 40 luminarias». ¿Qué corresponde?", "No: la memoria justifica los cálculos y permite que otra persona los revise", "Sí: con saber la cantidad de luminarias basta", "La memoria deja constancia de cómo se calculó; sin ella nadie puede comprobar el proyecto."),
        ("=", "{F} Para llegar justo al límite de 10 kW con luminarias de 25 W, ¿cuántas luminarias harían falta en total?", "10000//25", "El límite en vatios se divide por la potencia de cada luminaria.", " luminarias"),
        ("=", "Un local de ejemplo tiene 150 luminarias de 60 W cada una. ¿Cuántos kW de potencia instalada total suman, para compararlos con el límite del OA?", "150*60//1000", "Se multiplica la potencia por la cantidad y se pasa a kW dividiendo por 1000.", " kW"),
    ],
    ctx=("abc", "{F} Una amiga del dueño ofrece ayudar «sin cobrar» a ejecutar la instalación, aunque no es instaladora autorizada. ¿Qué corresponde?", "Agradecer, pero explicar que la ejecuta personal autorizado según la norma vigente", "Aceptar, porque no cobra", "Aceptar, si el dueño firma que asume el riesgo", "Que sea gratis o firmado no reemplaza la autorización ni la norma vigente."),
    sc=[
        ("En Electricidad: ¿qué es la cubicación?", "El cálculo de las cantidades de materiales y de mano de obra", "La cubicación determina cuánto se necesita antes de comprar."),
        ("¿Cuántos vatios son 3 kW?", "3000 W", "Un kilovatio equivale a 1000 vatios."),
        ("¿Quién ejecuta una instalación de alumbrado?", "Personal autorizado, con la norma vigente de la SEC", "Este cuaderno no habilita para ejecutar instalaciones."),
    ],
    op=("Local de ejemplo «Café Roble» (ficticio, solo alumbrado): 28 luminarias de 30 W. Presupuesto de ejemplo: 18 horas de mano de obra a $5.000 la hora. Escribe (a) la potencia instalada en vatios, (b) cuántos vatios faltarían para llegar a 1 kW, (c) el costo de la mano de obra, (d) por qué la ejecuta personal autorizado, (e) qué documento mostraría los cálculos del proyecto.",
        "(a) 28 por 30 son 840 W. (b) 1000 menos 840: faltan 160 W. (c) 18 por 5.000 son 90.000 pesos. (d) Porque una instalación mal hecha puede causar descarga o incendio y la norma vigente (SEC) exige personal autorizado. (e) La memoria de cálculo.",
        ["calcula bien la potencia", "calcula bien la diferencia", "calcula bien el costo", "explica la razón de la autorización", "nombra la memoria de cálculo"],
        ["hoja con las cinco respuestas y los cálculos"],
        ["confundir vatios y kW", "restar mal", "decir que cualquiera puede ejecutar"],
        "Pregunta: «¿por qué no puedes ejecutar tú la instalación?». Si no responde, pídele que relea el papel del personal autorizado."),
    reinforce="Inventa un local con tres tipos de luminarias (cantidad y vatios) y calcula su potencia instalada total en vatios y en kW.",
    extend="Explica con un ejemplo por qué sumar toda la potencia es más seguro que mirar cada parte por separado.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (planilla de cuadro de cargas, de ejemplo, inventada). Local «Taller Verde» (ficticio), tensión de ejemplo 220 V. Circuito A1: 12 luminarias de 20 W. "
     "Circuito A2: 8 luminarias de 55 W. Circuito A3: 5 luminarias de 44 W. Regla de la planilla de ejemplo: ningún circuito de alumbrado puede pasar de 440 W.")
build(
    O3, 2, F,
    use="Aprenderé a leer y completar un cuadro de cargas, a revisar el reparto entre circuitos y a rotular, siempre con datos de ejemplo en una planilla.",
    prior=["Sé calcular la potencia de un circuito.", "Sé qué es un cuadro de circuitos.", "Sé multiplicar, sumar y comparar."],
    explain=[
        "Una carga es un artefacto, o un grupo de artefactos, que consume energía; en el cuadro se expresa en vatios. El cuadro de cargas es una tabla con cada circuito, el número de artefactos, la potencia unitaria, la potencia por circuito y el total. Sirve para repartir las cargas de forma equilibrada entre los circuitos y para detectar uno sobrecargado. La regla de la planilla de esta ficha es de ejemplo: la regla real la fija el proyecto según la norma vigente.",
        "Para revisar un cuadro se calcula la potencia de cada circuito, se compara con la regla y se calcula el total. Si un circuito pasa el límite, no se corrige por cuenta propia: se informa al proyectista para que reparta mejor las cargas. Además, cada circuito debe quedar rotulado en el tablero con lo que alimenta, de modo que cualquiera pueda identificarlo con seguridad.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("carga", "artefacto o grupo de artefactos que consume energía, expresado en vatios"), ("cuadro de cargas", "tabla con cada circuito, sus artefactos, su potencia y el total"), ("potencia unitaria", "potencia de un solo artefacto"), ("reparto de cargas", "distribución de los artefactos entre los circuitos"), ("rotular", "escribir en el tablero qué alimenta cada circuito"), ("sobrecarga", "situación en que un circuito debe llevar más energía que la que su diseño permite")],
    worked=[
        ("Revisar un circuito", "Un circuito de ejemplo tiene 7 luminarias de 60 W y una regla de 450 W. ¿Cumple?", ["7 por 60 son 420 W.", "420 es menor que 450."], "Cumple, con 420 W"),
        ("Total del cuadro", "Un cuadro de ejemplo tiene circuitos de 300 W, 250 W y 180 W. ¿Cuál es el total?", ["Se suman los tres circuitos.", "300 más 250 más 180 son 730."], "730 W"),
    ],
    mistakes=[("Revisar solo el total del cuadro y no cada circuito.", "Un circuito puede pasar su límite aunque el total sea bajo.", "Calcula y compara cada circuito."),
              ("Agregar una luminaria a un circuito que ya está en su límite y corregir después.", "Se crea una sobrecarga mientras tanto.", "Informa al proyectista antes de cambiar el cuadro.")],
    T=[
        ("abc", "En Electricidad: ¿qué es una carga en un cuadro de cargas?", "Un artefacto o grupo de artefactos que consume energía, expresado en vatios", "La cantidad de cables que llegan al tablero", "La cantidad de energía que guarda una batería", "La carga es lo que consume energía y se mide en vatios, no una cantidad de cables."),
        ("abc", "En Electricidad: ¿para qué se rotula cada circuito en el tablero?", "Para identificar qué alimenta cada circuito y evitar errores al mantener la instalación", "Para aumentar la potencia permitida del circuito", "Para reemplazar al plano en la obra", "El rótulo identifica el circuito; no cambia su capacidad ni reemplaza al plano."),
        ("=", "En una planilla de ejemplo, un circuito tiene 10 luminarias de 30 W. ¿Cuántos vatios tiene el circuito?", "10*30", "Se multiplica la potencia unitaria por la cantidad.", " W"),
        ("=", "{F} ¿Cuántos vatios tiene el circuito A1?", "12*20", "Se multiplica la potencia unitaria por el número de luminarias.", " W"),
        ("abc", "{F} ¿Cuál circuito tiene la mayor potencia?", "A2, con 440 W", "A1, con 240 W", "A3, con 220 W", "A2 suma 8 por 55, es decir 440 W, más que A1 y A3."),
        ("=", "{F} ¿Cuál es la potencia instalada total de los tres circuitos?", "12*20+8*55+5*44", "Se suman las potencias de A1, A2 y A3.", " W"),
        ("=", "{F} ¿Cuántos vatios de margen le quedan al circuito A1 respecto del máximo de la planilla?", "440-12*20", "Al máximo permitido se le resta la potencia del circuito.", " W"),
        ("abc", "{F} ¿Se cumple la regla de la planilla en los tres circuitos?", "Sí: A2 llega exactamente a 440 W, que es el máximo, y los otros están por debajo", "No: A2 llega a 440 W y debe quedar por debajo", "No: A1 tiene más luminarias que A2 y por eso pasa el límite", "La regla dice que ningún circuito pase de 440 W; llegar justo a 440 W no pasa."),
        ("=", "{F} Se agrega una luminaria de 55 W al circuito A2. ¿Cuántos vatios tendría A2?", "8*55+55", "Se suma una luminaria más a las 8 que ya tiene el circuito.", " W"),
        ("abc", "{F} Con una luminaria más de 55 W en A2, ¿qué corresponde según la regla de la planilla?", "No agregarla a A2, porque pasaría de 440 W, y pedir al proyectista que la ubique en otro circuito", "Agregarla y rotular que A2 es especial", "Agregarla y quitar una luminaria de A1 sin avisar", "Si un circuito pasaría el límite, se informa al proyectista; no se cambia por cuenta propia."),
        ("ab", "{F} Un compañero dice que, como el total es bajo, ya no importa cómo se reparta entre circuitos. ¿Qué corresponde?", "No: la regla se aplica a cada circuito, no solo al total", "Sí: mientras el total sea bajo, cualquier reparto sirve", "El límite de la planilla es por circuito; un total bajo no impide sobrecargar uno."),
        ("=", "{F} El proyectista propone mover 2 luminarias de 20 W desde A1 hacia A3. ¿Cuántos vatios tendría A3?", "5*44+2*20", "A la potencia de A3 se le suma la de las dos luminarias movidas.", " W"),
        ("=", "{F} Para que A2 quede en 330 W con luminarias de 55 W, ¿cuántas luminarias debe tener?", "330//55", "La potencia deseada se divide por la potencia de cada luminaria.", " luminarias"),
    ],
    ctx=("abc", "{F} Una ayudante de ejemplo nota que el tablero no tiene rótulos y el dueño dice «yo me acuerdo de cuál es cuál». ¿Qué corresponde?", "Explicar que cada circuito debe quedar rotulado para que cualquiera lo identifique con seguridad", "Aceptar, porque el dueño conoce su local", "Rotular solo el circuito más grande", "El rótulo protege a quien mantenga la instalación después, no solo al dueño."),
    sc=[
        ("En Electricidad: ¿qué compara la revisión de un cuadro de cargas con la regla?", "La potencia de cada circuito", "El límite se aplica a cada circuito."),
        ("¿Qué se hace si un circuito pasaría su límite?", "Se informa al proyectista para repartir mejor las cargas", "No se resuelve por cuenta propia."),
        ("¿Cómo se obtiene la potencia total de un cuadro?", "Sumando la potencia de todos los circuitos", "El total es la suma de las potencias de cada circuito."),
    ],
    op=("Cuadro de ejemplo del local «Biblioteca Sol» (ficticio), regla de la planilla: ningún circuito de alumbrado puede pasar de 500 W. Circuito B1: 10 luminarias de 30 W. Circuito B2: 10 luminarias de 55 W. Circuito B3: 4 luminarias de 40 W. Escribe (a) la potencia de cada circuito, (b) cuál no cumple la regla y por cuánto pasa, (c) la potencia total, (d) qué haces con el circuito que no cumple.",
        "(a) B1: 300 W; B2: 10 por 55 son 550 W; B3: 160 W. (b) B2 no cumple: pasa por 50 W. (c) 300+550+160 son 1010 W. (d) Informo al proyectista para que reparta mejor las cargas; no lo corrijo por mi cuenta.",
        ["calcula la potencia de cada circuito", "compara con la regla", "calcula el total", "informa en lugar de corregir por su cuenta"],
        ["hoja con la tabla de cálculos y las respuestas"],
        ["calcular mal B2", "decir que B2 cumple", "corregir por cuenta propia"],
        "Pregunta: «¿qué pasaría si B2 tuviera una luminaria más de 55 W?». Si no responde, pídele que relea qué se hace cuando un circuito pasaría el límite."),
    reinforce="Inventa un cuadro de tres circuitos con una regla de potencia máxima y revisa si cada circuito cumple.",
    extend="Explica con un ejemplo por qué es mejor repartir las cargas entre circuitos en lugar de concentrarlas en uno.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (memoria de cálculo de ejemplo, inventada). Tensión de ejemplo: 220 V. Circuito B1: 880 W. Circuito B2: 1320 W. Circuito B3: 440 W. "
     "La planilla de ejemplo fija como límite de corriente por circuito 6 A (valor de ejemplo, no real).")
build(
    O3, 3, F,
    use="Aprenderé a calcular la corriente de cada circuito en una memoria de cálculo y a compararla con el límite de la planilla para detectar sobrecargas en el papel.",
    prior=["Sé que P = V × I.", "Sé sumar y dividir.", "Sé leer un cuadro de cargas."],
    explain=[
        "La memoria de cálculo toma la potencia de cada circuito y calcula su corriente con I = P ÷ V, donde la potencia está en vatios, la tensión en voltios y la corriente en amperios. Después compara cada corriente con el límite que fija el proyecto. Una sobrecarga ocurre cuando un circuito debe llevar más corriente que la que su diseño permite; el exceso calienta los conductores y puede causar un incendio. En esta ficha el límite de 6 A es de ejemplo; el real lo fija la norma vigente.",
        "Calcular la corriente en el papel sirve para detectar sobrecargas antes de que exista riesgo. Si una carga nueva haría pasar el límite, el proyecto se rediseña con el proyectista; no se sube el límite ni se cambia el diseño por cuenta propia. La memoria debe mostrar los datos, la fórmula, el resultado y la conclusión, para que otra persona repita el cálculo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("sobrecarga", "situación en que un circuito debe llevar más corriente que la que su diseño permite"), ("límite de corriente", "corriente máxima que fija el proyecto para un circuito"), ("memoria de cálculo", "documento que muestra datos, fórmula, resultado y conclusión de los cálculos"), ("amperio (A)", "unidad de la corriente eléctrica")],
    worked=[
        ("Calcular la corriente", "Un circuito de ejemplo tiene 660 W a 220 V. ¿Cuántos amperios usa?", ["I = P ÷ V.", "660 dividido por 220 son 3."], "3 A"),
        ("Comparar con el límite", "Un circuito de ejemplo usa 5 A y su límite es 6 A. ¿Cumple y cuánto margen tiene?", ["5 es menor que 6, cumple.", "6 menos 5 son 1."], "Cumple, con 1 A de margen"),
    ],
    mistakes=[("Anotar «cumple» sin mostrar el cálculo en la memoria.", "Otra persona no puede comprobar el resultado.", "Escribe datos, fórmula, resultado y conclusión."),
              ("Subir el límite de la planilla para que una carga nueva «calce».", "El límite viene del diseño y de la norma vigente, no se ajusta al gusto.", "Informa al proyectista para rediseñar.")],
    T=[
        ("abc", "En Electricidad: ¿qué se entiende por sobrecarga de un circuito?", "Que el circuito debe llevar más corriente que la que su diseño permite", "Que el circuito está apagado por el interruptor", "Que el circuito tiene más rótulos de los necesarios", "La sobrecarga es un exceso de corriente sobre lo que permite el diseño."),
        ("abc", "En Electricidad: ¿cómo se calcula la corriente de un circuito conociendo su potencia y su tensión?", "Dividiendo la potencia en vatios por la tensión en voltios", "Multiplicando la potencia por la tensión", "Restando la tensión a la potencia", "Como P = V × I, la corriente es la potencia dividida por la tensión."),
        ("=", "Un circuito de ejemplo tiene 1100 W y funciona a 220 V. ¿Cuántos amperios usa?", "1100//220", "La corriente es la potencia dividida por la tensión.", " A"),
        ("=", "{F} ¿Cuántos amperios usa el circuito B1?", "880//220", "Se divide la potencia del circuito por la tensión.", " A"),
        ("abc", "{F} ¿Qué circuito alcanza exactamente el límite de la planilla?", "B2, con 6 A", "B1, con 4 A", "B3, con 2 A", "B2 usa 1320 dividido por 220, es decir 6 A, igual al límite."),
        ("=", "{F} ¿Cuántos amperios usarían B1 y B3 si se alimentaran juntos como un solo circuito?", "(880+440)//220", "Se suman las potencias y se divide por la tensión.", " A"),
        ("=", "{F} Se quiere conectar a B3 un artefacto de 440 W más. ¿Cuántos amperios usaría B3 con esa carga?", "(440+440)//220", "Se suman las potencias y se divide por la tensión.", " A"),
        ("abc", "{F} Se agrega un artefacto de 220 W a B2. ¿Qué ocurre respecto del límite?", "Su corriente sube a 7 A y supera el límite de 6 A", "Queda en 6 A y cumple", "Baja a 5 A porque la carga se reparte", "B2 pasaría a 1540 W, que a 220 V son 7 A, más que el límite de 6 A."),
        ("=", "{F} ¿Cuántos amperios de margen tiene B1 respecto del límite?", "6-880//220", "Al límite se le resta la corriente de B1.", " A"),
        ("abc", "{F} Un compañero dice que, para que B2 no pase el límite con el artefacto nuevo, basta «anotar un límite mayor en la planilla». ¿Qué respuesta es correcta?", "No: el límite viene del diseño y de la norma vigente; si se excede, se rediseña con el proyectista", "Sí: el límite es solo una anotación", "Sí, si se informa al cliente", "Cambiar un número en la planilla no cambia lo que soporta el circuito real."),
        ("abc", "{F} ¿Por qué conviene calcular la corriente de cada circuito antes de ejecutar el proyecto?", "Para detectar sobrecargas en el papel, antes de que haya riesgo de calentamiento o incendio", "Para reducir el costo de la mano de obra", "Para evitar rotular los circuitos", "El cálculo anticipa el problema sin exponer a nadie."),
        ("=", "{F} Otro circuito, B4, se diseñaría con el mismo límite de 6 A a 220 V. ¿Cuántos vatios admitiría como máximo?", "6*220", "La potencia máxima es el límite de corriente por la tensión.", " W"),
        ("=", "{F} Un tablero de ejemplo agrupa B1, B2 y B3. ¿Cuántos amperios suman los tres circuitos?", "(880+1320+440)//220", "Se suman las tres potencias y se divide por la tensión.", " A"),
    ],
    ctx=("abc", "{F} El dueño del local pide agregar una estufa de 1100 W al circuito B3 «porque ya hay un enchufe libre». ¿Qué corresponde?", "Calcular primero la corriente del circuito con la estufa y comparar con el límite; si pasa, informar al proyectista", "Agregarla, porque el enchufe está libre", "Agregarla si la estufa tiene un cable largo", "Que haya un enchufe libre no dice nada sobre la corriente que soporta el circuito."),
    sc=[
        ("En Electricidad: ¿qué fórmula calcula la corriente de un circuito?", "I = P ÷ V", "La corriente es la potencia dividida por la tensión."),
        ("¿Qué se hace si un circuito pasaría su límite de corriente?", "Se informa al proyectista para rediseñar", "El límite no se sube por cuenta propia."),
        ("¿Qué debe mostrar una memoria de cálculo?", "Datos, fórmula, resultado y conclusión", "Así otra persona puede repetir el cálculo."),
    ],
    op=("Memoria de ejemplo del local «Tienda Mar»: tensión 220 V; circuito C1: 1100 W; circuito C2: 1540 W; límite de corriente de la planilla de ejemplo: 6 A por circuito. Escribe (a) la corriente de cada circuito, (b) cuál supera el límite y por cuánto, (c) qué conclusión anotas en la memoria, (d) qué haces con el circuito que supera el límite.",
        "(a) C1: 1100 dividido por 220 son 5 A; C2: 1540 dividido por 220 son 7 A. (b) C2 supera el límite en 1 A. (c) C1 cumple con 1 A de margen; C2 no cumple. (d) Informo al proyectista para que rediseñe el reparto; no subo el límite.",
        ["calcula bien las corrientes", "compara con el límite", "escribe una conclusión clara", "no cambia el límite por su cuenta"],
        ["hoja con los cálculos y la conclusión"],
        ["multiplicar en vez de dividir", "decir que C2 cumple", "subir el límite"],
        "Pregunta: «¿qué datos pondrías en la memoria?». Si no responde, pídele que relea qué debe mostrar una memoria de cálculo."),
    reinforce="Inventa tres circuitos con su potencia a 220 V, calcula su corriente y compáralas con un límite de ejemplo.",
    extend="Explica con un ejemplo por qué calcular en el papel es mejor que descubrir una sobrecarga con la instalación terminada.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (verificación de ejemplo, inventada). Tensión de ejemplo: 220 V. Un circuito de alumbrado lleva 5 A. Resistencia total del conductor de ida y vuelta del circuito, de ejemplo: 2 Ω. "
     "Criterio de la planilla de ejemplo: la caída de tensión no debe superar el 5 % de 220 V, es decir, 11 V. No se entregan secciones ni tipos de conductor: los valores son solo para calcular.")
build(
    O3, 4, F,
    use="Aprenderé qué es la caída de tensión, a calcularla con la ley de Ohm y a compararla con un criterio de planilla para decidir si el diseño cumple.",
    prior=["Sé que V = I × R.", "Sé calcular porcentajes sencillos.", "Sé comparar un valor con un límite."],
    explain=[
        "La caída de tensión es la pérdida de tensión a lo largo de un conductor por su resistencia. Se calcula con la ley de Ohm: caída = corriente × resistencia. Si el conductor es más largo, su resistencia es mayor; si es más grueso, es menor. Cuando la caída es grande, los artefactos reciben menos tensión de la prevista, funcionan peor y los conductores se calientan más. Por eso el proyecto fija un máximo, que se suele expresar como porcentaje de la tensión: porcentaje = caída × 100 ÷ tensión.",
        "En la memoria de cálculo se anotan la corriente, la resistencia, la caída calculada, el límite y la conclusión. Si la caída pasa el límite, el diseño se corrige con el proyectista; el instalador no cambia el conductor por cuenta propia. Esta clase no entrega valores de conductores: los datos son de ejemplo para practicar el cálculo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("caída de tensión", "pérdida de tensión a lo largo de un conductor por su resistencia"), ("resistencia", "dificultad al paso de la corriente; se mide en ohmios (Ω)"), ("ley de Ohm", "V = I × R"), ("porcentaje de caída", "caída × 100 ÷ tensión"), ("conductor", "material por el que circula la corriente, como un cable")],
    worked=[
        ("Calcular la caída", "Por un conductor de ejemplo con 3 Ω circulan 4 A. ¿Cuántos voltios cae?", ["Caída = corriente × resistencia.", "4 por 3 son 12."], "12 V"),
        ("Calcular el porcentaje", "En un circuito de ejemplo a 100 V la caída es de 3 V. ¿Qué porcentaje es?", ["Porcentaje = caída × 100 ÷ tensión.", "3 por 100 dividido por 100 son 3."], "3 %"),
    ],
    mistakes=[("Comparar la caída en voltios con un límite en porcentaje sin convertir.", "Son unidades distintas y la comparación sale falsa.", "Convierte el límite a voltios o la caída a porcentaje."),
              ("Cambiar por cuenta propia el conductor cuando la caída da más que el límite.", "El diseño lo corrige el proyectista con sus cálculos.", "Informa el resultado y espera la decisión.")],
    T=[
        ("abc", "En Electricidad: ¿qué es la caída de tensión en un conductor?", "La pérdida de tensión a lo largo del conductor por su resistencia", "El corte de la corriente al apagar el interruptor", "La diferencia de precio entre dos conductores", "La caída de tensión es una pérdida de tensión causada por la resistencia."),
        ("abc", "En Electricidad: ¿cómo se calcula la caída de tensión, en voltios?", "Multiplicando la corriente en amperios por la resistencia en ohmios", "Dividiendo la corriente por la resistencia", "Sumando la corriente y la resistencia", "La ley de Ohm dice V = I × R, y esa es la caída."),
        ("=", "Por un conductor de ejemplo con 5 Ω circulan 3 A. ¿Cuántos voltios cae?", "3*5", "Se multiplica la corriente por la resistencia.", " V"),
        ("=", "{F} ¿Cuántos voltios de caída tiene el circuito de la ficha?", "5*2", "Se multiplica la corriente por la resistencia.", " V"),
        ("=", "{F} ¿Cuántos voltios es el 5 % de 220 V, que es el límite de la ficha?", "220*5//100", "Se calcula el 5 % de la tensión.", " V"),
        ("abc", "{F} ¿Cumple el circuito el criterio de la planilla?", "Sí: la caída es 10 V y el límite es 11 V", "No: 10 V es más que el 5 %", "No: la caída debe ser exactamente 0 V", "10 V es menor que 11 V, así que cumple."),
        ("=", "{F} El circuito se alarga y su resistencia sube a 3 Ω con la misma corriente. ¿Cuántos voltios cae ahora?", "5*3", "Se multiplica la misma corriente por la nueva resistencia.", " V"),
        ("abc", "{F} Con una caída de 15 V, ¿qué corresponde?", "No cumple el límite de 11 V; se informa al proyectista para rediseñar, sin cambiar el conductor por cuenta propia", "Cumple, porque 15 V es solo 5 V más que antes", "Cumple si se aumenta el límite a 15 V", "15 V supera 11 V; el límite no se sube y el diseño lo corrige el proyectista."),
        ("=", "{F} Con 10 V de caída, ¿cuántos voltios llegan al final del circuito?", "220-10", "A la tensión de partida se le resta la caída.", " V"),
        ("abc", "{F} Un compañero dice que, con la misma corriente, reducir la resistencia del conductor reduce la caída. ¿Es correcto?", "Sí: menos resistencia produce menos caída (V = I × R); el rediseño lo decide el proyectista", "No: la caída no depende de la resistencia", "No: solo depende de la tensión de la red", "Con la misma corriente, la caída es proporcional a la resistencia."),
        ("ab", "{F} Un instalador dice: «si la caída da 12 V, igual lo ejecuto, porque 1 V no se nota». ¿Qué corresponde?", "No: 12 V supera el límite de 11 V; se informa para corregir el diseño", "Sí: 1 V de diferencia es despreciable", "El límite se cumple o no se cumple; una diferencia pequeña no autoriza a ignorarlo."),
        ("=", "En otro circuito de ejemplo la tensión es de 200 V y la caída es de 10 V. ¿Qué porcentaje de la tensión representa la caída?", "10*100//200", "El porcentaje es la caída por 100 dividido por la tensión.", " %"),
        ("abc", "{F} ¿Qué datos debe registrar la memoria para que un revisor repita la verificación?", "Corriente, resistencia, caída calculada, límite aplicado y conclusión", "Solo la conclusión «cumple»", "Solo el nombre de quien calculó", "Un revisor necesita los datos y la fórmula para comprobar el resultado."),
    ],
    ctx=("abc", "{F} Un instalador de ejemplo quiere alargar el circuito 10 m «porque queda mejor la lámpara». ¿Qué corresponde?", "Informar al proyectista, porque un conductor más largo aumenta la resistencia y la caída debe recalcularse", "Alargarlo, porque 10 m más no afectan", "Alargarlo y revisar la caída después de terminar", "Más largo significa más resistencia y más caída; el cálculo se rehace antes de cambiar."),
    sc=[
        ("En Electricidad: ¿qué fórmula da la caída de tensión?", "Caída = corriente × resistencia", "Es la ley de Ohm aplicada al conductor."),
        ("¿Qué pasa con la resistencia de un conductor más largo?", "Aumenta", "Cuanto más largo el conductor, más dificultad al paso de la corriente."),
        ("¿Cómo se pasa una caída en voltios a porcentaje?", "Multiplicándola por 100 y dividiendo por la tensión", "El porcentaje compara la caída con la tensión total."),
    ],
    op=("Datos de ejemplo: tensión 220 V; circuito D1 lleva 4 A con una resistencia de 2 Ω; circuito D2 lleva 4 A con una resistencia de 3 Ω; límite de la planilla: 5 % de 220 V, es decir, 11 V. Escribe (a) la caída de D1 y de D2, (b) cuál cumple el límite, (c) cuántos voltios llegan al final de D2, (d) qué haces con el circuito que no cumple.",
        "(a) D1: 4 por 2 son 8 V; D2: 4 por 3 son 12 V. (b) D1 cumple (8 V menor que 11 V); D2 no cumple (12 V mayor que 11 V). (c) 220 menos 12: 208 V. (d) Informo al proyectista para que rediseñe; no cambio el conductor por mi cuenta.",
        ["calcula bien las caídas", "compara con el límite", "calcula la tensión final", "no modifica el diseño por su cuenta"],
        ["hoja con cálculos y conclusión"],
        ["sumar en vez de multiplicar", "decir que D2 cumple", "decidir el cambio de conductor"],
        "Pregunta: «¿por qué no puedes cambiar el conductor de D2 tú?». Si no responde, pídele que relea quién corrige el diseño."),
    reinforce="Inventa un circuito con corriente y resistencia, calcula su caída y compárala con un límite en voltios que tú fijes.",
    extend="Explica con un ejemplo por qué una caída de tensión grande puede ser un riesgo además de una molestia.",
)

# ============================================================ OAE-03, clase 5
F = ("Ficha 5 (alternativas de ejemplo, inventadas). Un pasillo se ilumina 10 horas al día durante 30 días al mes. Alternativa A: 30 luminarias de 40 W cada una, a $2.000 cada una. "
     "Alternativa B: 30 luminarias de 16 W cada una, a $4.500 cada una. Precio de la energía de ejemplo: $150 por kWh. 1 kWh equivale a 1000 Wh (vatios-hora).")
build(
    O3, 5, F,
    use="Aprenderé a calcular el consumo de energía y su costo, a comparar alternativas de un proyecto y a verificar la calidad con una lista.",
    prior=["Sé calcular la potencia de un conjunto de artefactos.", "Sé pasar de W a kW.", "Sé multiplicar y comparar costos."],
    explain=[
        "La energía que consume un artefacto es su potencia multiplicada por las horas que funciona. Si se mide en vatios-hora (Wh), 1000 Wh forman 1 kWh; la cuenta de electricidad cobra por kWh. Para comparar alternativas se calcula la energía mensual de cada una, su costo en pesos y el costo de compra. Una alternativa más cara de comprar puede costar menos en total si ahorra energía durante muchos meses.",
        "Antes de recomendar una alternativa, el proyectista revisa la calidad del proyecto con una lista de verificación: potencias, cantidades y precios coinciden entre plano, memoria y presupuesto; los límites de la planilla se cumplen; las decisiones quedan registradas. La ejecución la hace personal autorizado. Los precios y horas de esta ficha son de ejemplo.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("energía", "potencia multiplicada por el tiempo de uso"), ("vatio-hora (Wh)", "unidad de energía: un vatio durante una hora"), ("kWh", "kilovatio-hora, equivale a 1000 Wh"), ("alternativa", "una de las opciones que se comparan en un proyecto"), ("lista de verificación de calidad", "tabla de puntos que se revisan antes de aprobar un proyecto")],
    worked=[
        ("Calcular la energía", "Un artefacto de ejemplo de 500 W funciona 6 horas. ¿Cuántos Wh consume y cuántos kWh son?", ["500 por 6 son 3000 Wh.", "3000 dividido por 1000 son 3 kWh."], "3000 Wh, es decir, 3 kWh"),
        ("Costo de la energía", "Con una energía de ejemplo a $120 por kWh, ¿cuánto cuestan 8 kWh?", ["Se multiplica el precio por los kWh.", "120 por 8 son 960."], "$960"),
    ],
    mistakes=[("Elegir la alternativa más barata de comprar sin calcular el costo de la energía.", "Puede costar más en total durante el uso.", "Compara compra más energía en el período."),
              ("Usar W donde corresponde Wh al calcular energía.", "La energía necesita el tiempo de uso.", "Multiplica la potencia por las horas.")],
    T=[
        ("abc", "En Electricidad: ¿cómo se calcula la energía que consume un artefacto?", "Multiplicando su potencia por las horas que funciona", "Dividiendo su potencia por las horas", "Sumando su potencia y las horas", "La energía es potencia por tiempo; dividir o sumar no da energía."),
        ("=", "Un artefacto de ejemplo de 500 W funciona 4 horas. ¿Cuántos Wh de energía consume?", "500*4", "Se multiplica la potencia por las horas de funcionamiento.", " Wh"),
        ("=", "Un consumo de ejemplo de 3000 Wh, ¿cuántos kWh son?", "3000//1000", "1000 Wh forman 1 kWh.", " kWh"),
        ("=", "{F} ¿Cuántos vatios suman las 30 luminarias de la alternativa A?", "30*40", "Se multiplica la potencia de una luminaria por la cantidad.", " W"),
        ("=", "{F} ¿Cuántas horas de uso hay en el mes de la ficha?", "10*30", "Se multiplican las horas diarias por los días del mes.", " horas"),
        ("=", "{F} ¿Cuántos kWh consume la alternativa A en el mes?", "30*40*300//1000", "Se multiplica la potencia total por las horas del mes y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuántos kWh consume la alternativa B en el mes?", "30*16*300//1000", "Se multiplica la potencia total por las horas del mes y se pasa a kWh.", " kWh"),
        ("=", "{F} ¿Cuánto cuesta al mes la energía de la alternativa A?", "30*40*300//1000*150", "Se calculan los kWh del mes y se multiplican por el precio de cada kWh.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta comprar las 30 luminarias de la alternativa B?", "30*4500", "Se multiplica el precio de una luminaria por la cantidad.", " pesos"),
        ("=", "{F} ¿Cuántos pesos al mes ahorra B respecto de A solo en energía?", "(30*40-30*16)*300//1000*150", "Se calcula la diferencia de kWh y se multiplica por el precio.", " pesos"),
        ("abc", "{F} Un compañero afirma que A conviene porque la compra cuesta menos. ¿Qué respuesta es correcta?", "Considera solo la compra; falta sumar la energía que se gasta durante el uso", "Tiene razón: el costo de compra es el único criterio", "Tiene razón: A consume menos energía que B", "Una alternativa barata de comprar puede gastar más energía cada mes; hay que comparar compra más energía."),
        ("=", "{F} En 12 meses, ¿cuántos pesos más gasta A que B solo en energía?", "12*(30*40-30*16)*300//1000*150", "Se multiplica el ahorro mensual por los 12 meses.", " pesos"),
        ("abc", "{F} Antes de recomendar B, el proyectista revisa la calidad con una lista. ¿Qué punto corresponde?", "Que potencias, cantidades y precios coincidan entre plano, memoria y presupuesto", "Que se elija la alternativa con más luminarias", "Que el presupuesto no incluya la mano de obra", "La lista comprueba coherencia entre documentos; elegir más luminarias o quitar mano de obra no es verificación."),
    ],
    ctx=("abc", "{F} El dueño elige A y dice: «pago poco ahora y después veremos». ¿Qué le explica el proyectista?", "Que a lo largo de 12 meses B ahorra más energía de lo que cuesta de más, y que la decisión se registra", "Que A es ilegal", "Que B ahorra solo si se enciende menos tiempo", "Con los datos de la ficha el ahorro anual supera la diferencia de compra, y la decisión queda por escrito."),
    sc=[
        ("En Electricidad: ¿cuántos Wh son 2 kWh?", "2000 Wh", "Un kWh equivale a 1000 Wh."),
        ("¿Qué se suma para comparar el costo total de una alternativa?", "El costo de compra y el costo de la energía durante el uso", "Una alternativa barata de comprar puede gastar más energía."),
        ("¿Qué revisa una lista de verificación de calidad?", "Que potencias, cantidades y precios coincidan entre los documentos", "Así se evitan contradicciones antes de aprobar."),
    ],
    op=("Datos de ejemplo: un taller se ilumina 8 horas al día durante 25 días al mes. Alternativa X: 20 luminarias de 50 W a $1.800 cada una. Alternativa Y: 20 luminarias de 20 W a $4.000 cada una. Energía a $140 por kWh. Escribe (a) los kWh mensuales de X y de Y, (b) el costo mensual de energía de cada una, (c) la diferencia de compra entre Y y X, (d) si el ahorro de energía en 12 meses supera esa diferencia, (e) un punto de verificación de calidad.",
        "(a) 200 horas al mes: X usa 1000 W por 200 h = 200 kWh; Y usa 400 W por 200 h = 80 kWh. (b) X: 200 por 140 son 28.000 pesos; Y: 80 por 140 son 11.200 pesos. (c) Compra de X: 36.000; de Y: 80.000; diferencia 44.000 pesos. (d) El ahorro mensual es 16.800 pesos; en 12 meses son 201.600 pesos, más que 44.000. (e) Por ejemplo: cantidades y potencias iguales en plano, memoria y presupuesto.",
        ["calcula bien los kWh", "calcula bien los costos", "calcula la diferencia de compra", "compara el ahorro con la inversión", "propone un punto de verificación válido"],
        ["hoja con la tabla de cálculos y la conclusión"],
        ["olvidar multiplicar por las horas", "usar solo el costo de compra", "no verificar la coherencia"],
        "Pregunta: «¿por qué no basta comparar el precio de compra?». Si no responde, pídele que relea cómo se compara una alternativa."),
    reinforce="Inventa dos alternativas de iluminación de un pasillo y compara su energía mensual y su costo con precios que fijes tú.",
    extend="Explica con un ejemplo por qué el ahorro de energía puede cambiar la mejor decisión de un proyecto.",
)
