"""Electrónica TP 3.º y 4.º medio: OAE-01 (leer información técnica), OAE-02 (diagnóstico lógico de fallas) y OAE-03 (circuitos básicos analógicos y digitales: solo conceptos). Todo en papel, con tensiones bajas y datos de ejemplo."""
from __future__ import annotations

from tp_eltr_common import AVISO, EMER, build

O1 = "TP-ELTR-3y4-OAE-01"
O2 = "TP-ELTR-3y4-OAE-02"
O3 = "TP-ELTR-3y4-OAE-03"

# ============================================================ OAE-01, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). El taller ficticio «Electrónica Sur» recibe el encargo de revisar la documentación de una pequeña alarma de 9 V para una bodega. "
     "Documentos entregados: manual de usuario (8 páginas), esquema de la alarma, lista de componentes (12 ítems) y una hoja de instrucciones. "
     "Riesgos anotados: la alarma se alimenta con un cargador conectado a la red eléctrica y el esquema incluye una batería de respaldo.")
build(
    O1, 1, F,
    use="Aprenderé qué documentos usa quien trabaja en electrónica, qué institución vigila la seguridad eléctrica y qué riesgos hay que reconocer antes de leer un manual o un esquema.",
    prior=["Sé leer una tabla y un dibujo simple.", "Sé sumar y restar cantidades.", "Sé que una empresa entrega encargos por escrito."],
    explain=[
        "La electrónica controla la corriente eléctrica con componentes pequeños para que un equipo cumpla una función: sonar, medir, encender o avisar. Quien trabaja en ella no parte tocando: parte leyendo. El manual explica cómo se usa y se cuida un equipo. El esquema es un dibujo con símbolos que muestra cómo se conectan los componentes. El croquis es un dibujo a mano alzada, rápido y sin medidas exactas. La lista de componentes dice qué piezas hay y cuántas. Todos juntos forman el proyecto. Relevar un dato es encontrarlo en el documento y anotarlo para usarlo bien.",
        "En Chile, la Superintendencia de Electricidad y Combustibles (SEC) fiscaliza la seguridad de las instalaciones eléctricas. Cada documento trae advertencias: mensajes sobre lo que puede dañar a la persona o al equipo. Los riesgos principales son la descarga eléctrica, la quemadura, el incendio y los errores de lectura que llevan a un montaje equivocado. Si dos documentos se contradicen, no se elige uno al azar: se anota la diferencia y se informa a la jefatura o al docente. Al terminar una revisión se deja un registro: una nota escrita con la fecha, quién revisó y qué diferencias encontró.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("manual", "documento que explica cómo se usa y se cuida un equipo"), ("esquema", "dibujo con símbolos que muestra cómo se conectan los componentes"), ("croquis", "dibujo a mano alzada, rápido y sin medidas exactas"), ("lista de componentes", "documento que dice qué piezas hay y cuántas"), ("advertencia", "mensaje sobre lo que puede causar daño"), ("SEC", "Superintendencia de Electricidad y Combustibles, que fiscaliza la seguridad de las instalaciones eléctricas"), ("relevar un dato", "encontrarlo en el documento y anotarlo para usarlo")],
    worked=[
        ("Elegir el documento", "Una técnica de ejemplo necesita saber cuántas unidades de cada pieza lleva un equipo. ¿Qué documento consulta?", ["Las cantidades de cada pieza están en un documento específico.", "Ese documento es la lista de componentes."], "La lista de componentes"),
        ("Piezas que faltan", "Un pedido de ejemplo pide 20 resistores y en bodega hay 14. ¿Cuántos faltan?", ["Se resta lo que hay a lo que se pide.", "20 menos 14 son 6."], "Faltan 6 resistores"),
    ],
    mistakes=[("Elegir uno de dos documentos que se contradicen y seguir adelante sin avisar.", "Un documento erróneo puede llevar a un montaje equivocado y riesgoso.", "Anota la diferencia e informa a la jefatura o al docente para corregirla."),
              ("Creer que, por haber leído un cuaderno, ya se puede abrir un equipo conectado a la red eléctrica.", "Esa tarea exige instructor autorizado y norma vigente.", "Aprende aquí los conceptos y practica solo con personal autorizado.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un croquis?", "Un dibujo a mano alzada, rápido y sin medidas exactas", "Un esquema oficial con medidas exactas aprobadas por la SEC", "Una lista de precios de componentes", "El croquis es un dibujo rápido de apoyo; no reemplaza al esquema ni a la lista de precios."),
        ("abc", "En Electrónica: ¿qué significa «relevar» un dato de un manual?", "Encontrarlo y anotarlo para usarlo en el trabajo", "Copiarlo de memoria sin volver a mirar el manual", "Reemplazarlo por un valor propio si parece mejor", "Relevar es ubicar el dato en el documento y registrarlo tal como está."),
        ("abc", "¿Qué institución fiscaliza la seguridad de las instalaciones eléctricas en Chile?", "La Superintendencia de Electricidad y Combustibles (SEC)", "La Subsecretaría de Telecomunicaciones (Subtel)", "La Dirección del Trabajo", "La SEC fiscaliza la seguridad eléctrica; las otras instituciones tienen otras funciones."),
        ("=", "{F} La lista de componentes tiene 12 ítems. El taller ya revisó 7. ¿Cuántos ítems faltan por revisar?", "12-7", "Se resta lo revisado al total de ítems de la lista.", " ítems"),
        ("abc", "{F} ¿Qué documento de la ficha muestra cómo se conectan los componentes entre sí?", "El esquema de la alarma", "La lista de componentes", "La hoja de instrucciones", "El esquema es el dibujo con símbolos de las conexiones; la lista solo da piezas y cantidades."),
        ("abc", "{F} ¿Qué riesgos permite anticipar la ficha antes de empezar la revisión?", "Descarga eléctrica por el cargador conectado a la red y calentamiento o incendio por la batería", "Solo que se acabe el papel de impresión del manual", "Ninguno, porque una alarma de 9 V nunca tiene riesgos", "El cargador conectado a la red y la batería son fuentes de riesgo eléctrico y de calor."),
        ("=", "{F} La hoja de instrucciones de ejemplo ocupa 2 páginas. Si el taller imprime 6 copias de la hoja y del manual, ¿cuántas páginas imprime?", "6*(2+8)", "Cada copia suma las páginas de la hoja y del manual, y eso se multiplica por 6.", " páginas"),
        ("abc", "{F} El esquema muestra una batería de respaldo, pero el manual no la nombra. ¿Qué corresponde?", "Anotar la diferencia e informar a la jefatura o al docente para aclararla", "Suponer que el manual está bien y olvidar la batería", "Suponer que el esquema está mal y borrar la batería del dibujo", "Cuando dos documentos se contradicen se informa; no se elige uno por cuenta propia."),
        ("ab", "Un estudiante terminó este cuaderno y quiere abrir un cargador conectado a la red para ver su interior. ¿Qué corresponde?", "No hacerlo: exige instructor autorizado y norma vigente, y el cuaderno no habilita", "Hacerlo con cuidado, porque ya conoce los documentos", "Abrir un cargador conectado a la red es una tarea de riesgo reservada a personal autorizado; leer documentos no habilita."),
        ("abc", "Una compañera de curso sufre una descarga eléctrica y sigue en contacto con la energía. ¿Qué corresponde según las reglas generales?", "No tocarla, cortar el suministro solo si estás autorizado, avisar a un adulto responsable y a emergencias", "Jalarla con las manos para separarla lo antes posible", "Esperar a ver si se le pasa antes de avisar a alguien", "Tocar a la persona puede transmitir la descarga a quien ayuda; se corta el suministro solo si se está autorizado y se avisa."),
        ("abc", "{F} Un compañero dice: «con el manual de usuario basta para saber cuántas piezas hay que comprar». ¿Qué respuesta es correcta?", "No siempre: las cantidades están en la lista de componentes y el manual explica el uso y el cuidado", "Sí, porque el manual lo explica todo", "Sí, porque el manual es el documento más largo de los entregados", "El manual explica el uso del equipo; las cantidades de piezas las entrega la lista de componentes."),
        ("=", "{F} El taller cobra $6.000 por hora (de ejemplo) por revisar documentación y la revisión toma 3 horas. ¿Cuánto cobra por la revisión?", "6000*3", "El valor por hora se multiplica por las horas de la revisión.", " pesos"),
        ("abc", "En un trabajo de electrónica, ¿qué debe anotar como mínimo el registro al terminar una revisión de documentos?", "Fecha, quién revisó y qué diferencias encontró", "Solo el nombre del taller", "Solo el costo de los materiales", "Un registro útil deja constancia de cuándo, quién y qué se encontró."),
    ],
    ctx=("abc", "En un taller de ejemplo, un cliente dice: «mi primo sabe de esto; que abra él el cargador enchufado y así ahorramos». Como estudiante, ¿qué respondes?", "Explicar que abrir equipos conectados a la red lo hace personal autorizado y proponer pedirlo al taller", "Aceptar para no discutir con el cliente", "Abrirlo tú, porque estudias electrónica", "Los equipos conectados a la red exigen personal autorizado, norma vigente y protección; estudiar no habilita."),
    sc=[
        ("En Electrónica: ¿para qué sirve la lista de componentes?", "Para saber qué piezas se necesitan y en qué cantidad", "La lista de componentes entrega piezas y cantidades."),
        ("¿Qué se hace si dos documentos del proyecto se contradicen?", "Anotar la diferencia e informar a la jefatura o al docente", "No se elige uno al azar porque podría ser el equivocado."),
        ("¿Quién abre o repara equipos conectados a la red eléctrica?", "Personal autorizado, con norma vigente (SEC) y protección", "Este cuaderno no habilita para trabajar con la red."),
    ],
    op=("El taller de ejemplo «Luz Norte» te entrega estos documentos de un temporizador de 6 V: esquema, lista de componentes (10 ítems), manual de 5 páginas. En la bodega solo hay 6 de los 10 ítems. Escribe (a) qué documento usarías para saber cuántas piezas son, (b) cuántos ítems faltan, (c) un riesgo de la tarea que no harías tú y quién la haría.",
        "(a) La lista de componentes. (b) 10 menos 6: faltan 4 ítems. (c) Abrir un equipo conectado a la red lo haría personal autorizado con norma vigente (SEC) y protección.",
        ["nombra el documento correcto", "calcula bien los ítems que faltan", "reconoce un riesgo y a quién corresponde"],
        ["hoja con el documento, el cálculo y el riesgo"],
        ["decir que ya puede abrir equipos de la red", "restar mal", "no nombrar quién hace la tarea riesgosa"],
        "Pregunta: «¿qué haces si el manual y el esquema se contradicen?». Si no responde, pídele que relea la regla de anotar la diferencia e informar."),
    reinforce="Escribe una lista de componentes de ejemplo para una linterna con 1 batería, 1 interruptor y 1 lámpara, con las cantidades.",
    extend="Explica con un ejemplo inventado por qué anotar en un registro lo que se encontró protege al taller y al cliente.",
)

# ============================================================ OAE-01, clase 2
F = ("Ficha 2 (esquema descrito por escrito, de ejemplo, inventado). Linterna de práctica de 6 V. Leyenda: B1 = batería de 6 V; S1 = interruptor; L1 = lámpara pequeña de 6 V. "
     "Lista de conexiones: el nodo A une el terminal positivo (+) de B1 con un terminal de S1; el nodo B une el otro terminal de S1 con un terminal de L1; "
     "el nodo C une el otro terminal de L1 con el terminal negativo (−) de B1. El plano de la caja está a escala 1:5: 1 cm del plano son 5 cm reales; la caja mide 6 cm de largo en el plano.")
build(
    O1, 2, F,
    use="Aprenderé a leer una leyenda, una lista de conexiones y una escala, y qué hace cada persona del equipo en un proyecto electrónico.",
    prior=["Sé qué es un esquema y una lista de componentes.", "Sé multiplicar y dividir por números pequeños.", "Sé convertir centímetros."],
    explain=[
        "En un esquema cada componente se dibuja con un símbolo y se nombra con una letra y un número: B para batería, S para interruptor, L para lámpara, R para resistor. La leyenda explica qué es cada símbolo; sin ella el esquema no se puede leer. Cuando el esquema se describe por escrito, se usa una lista de conexiones: cada nodo es un punto donde se unen dos o más terminales. La polaridad dice cuál terminal es positivo (+) y cuál negativo (−), y importa en baterías y en otros componentes.",
        "Un circuito cerrado tiene un camino completo para la corriente, de un terminal de la batería al otro. Si un interruptor está abierto, el camino se interrumpe y no circula corriente. El plano se dibuja a escala: una razón fija entre la medida dibujada y la real. A escala 1:5, cada centímetro del plano son 5 centímetros reales.",
        f"Cada rol tiene su función: el proyectista diseña, el técnico ejecuta lo que dice el documento, el supervisor revisa y autoriza los cambios, y el cliente recibe. Ninguna persona cambia un documento por su cuenta. {AVISO}",
    ],
    vocab=[("leyenda", "tabla que explica qué es cada símbolo o código"), ("nodo", "punto donde se unen dos o más terminales"), ("polaridad", "indicación de cuál terminal es positivo (+) y cuál negativo (−)"), ("circuito cerrado", "circuito con un camino completo para la corriente"), ("escala", "razón fija entre la medida del plano y la medida real"), ("proyectista", "persona que diseña el proyecto"), ("supervisor", "persona que revisa y autoriza el trabajo")],
    worked=[
        ("Leer la escala", "Un plano de ejemplo está a escala 1:10. Una placa mide 4 cm en el plano. ¿Cuánto mide en la realidad?", ["Cada centímetro del plano son 10 centímetros reales.", "4 por 10 son 40 centímetros."], "40 cm"),
        ("Leer un símbolo", "La leyenda de un esquema de ejemplo dice: R2 = resistor; D1 = diodo. En la lista de conexiones aparece «nodo X: terminal de R2 con terminal de D1». ¿Qué dos componentes se unen en el nodo X?", ["La leyenda dice qué es cada nombre.", "Se unen un resistor y un diodo."], "El resistor R2 y el diodo D1"),
    ],
    mistakes=[("Suponer que cada símbolo significa lo mismo en todos los esquemas y no mirar la leyenda.", "Cada documento puede usar sus propios nombres; la leyenda manda.", "Lee siempre la leyenda antes de interpretar el esquema."),
              ("Usar en el trabajo la medida dibujada en el plano como si fuera la real.", "La medida del plano hay que convertirla con la escala.", "Multiplica la medida del plano por la escala indicada.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un nodo en una lista de conexiones?", "Un punto donde se unen dos o más terminales de componentes", "Un componente que guarda energía", "La tabla que explica los símbolos", "Un nodo es un punto de unión de terminales; la tabla de símbolos es la leyenda."),
        ("abc", "En Electrónica: ¿para qué sirve la leyenda de un esquema?", "Para saber qué componente representa cada símbolo o nombre", "Para saber cuánto cuesta cada componente", "Para saber quién autorizó el proyecto", "La leyenda explica el significado de los símbolos y de los nombres."),
        ("abc", "En un esquema de ejemplo, ¿qué indica el signo + junto a un terminal de una batería?", "Que es el terminal positivo y fija la polaridad", "Que la batería se puede cargar", "Que esa batería tiene más energía que otra", "El signo + marca el terminal positivo y, con el −, define la polaridad."),
        ("=", "{F} ¿Cuántos centímetros reales mide el largo de la caja?", "6*5", "La medida del plano se multiplica por la escala 1:5.", " cm"),
        ("abc", "{F} ¿Qué dos terminales se unen en el nodo B?", "Un terminal de S1 y un terminal de L1", "El terminal positivo de B1 y un terminal de S1", "Un terminal de L1 y el terminal negativo de B1", "La ficha dice que el nodo B une el otro terminal de S1 con un terminal de L1."),
        ("abc", "{F} Si S1 está abierto, ¿qué ocurre con L1?", "No recibe corriente y no enciende, porque el camino queda interrumpido", "Enciende más fuerte, porque la batería queda libre", "Enciende igual, porque la batería sigue conectada", "Un interruptor abierto interrumpe el camino de la corriente, aunque la batería siga conectada."),
        ("=", "{F} Un pedido de ejemplo es de 4 linternas como la de la ficha. Cada linterna lleva los 3 componentes de la leyenda. ¿Cuántos componentes debe tener la lista de materiales del pedido?", "4*3", "Los componentes de una linterna se multiplican por las 4 linternas.", " componentes"),
        ("abc", "{F} Un proyectista agrega una segunda lámpara, L2, al esquema. ¿Qué debe actualizar además del dibujo para que todo coincida?", "La lista de componentes y la lista de conexiones", "Nada más, porque el dibujo basta", "Solo la portada del proyecto", "Si cambia el dibujo deben cambiar también la lista de piezas y las conexiones, o los documentos se contradicen."),
        ("abc", "{F} Un técnico propone cambiar L1 por una lámpara de mayor tensión. ¿Quién debe revisar y autorizar el cambio?", "El supervisor, con el proyectista", "El cliente, al abrir la caja", "El mismo técnico, porque es quien ejecuta", "El supervisor revisa y autoriza los cambios; el técnico ejecuta lo que dice el documento."),
        ("ab", "{F} Un técnico ve que en la caja el terminal negativo de la batería está unido a S1, pero la ficha dice que va a L1. ¿Qué corresponde?", "Informar la diferencia al supervisor para que se decida si se corrige el documento o la caja", "Cambiar el documento sin avisar, para que coincida con la caja", "Cuando el objeto y el documento no coinciden se informa; nadie cambia uno u otro por su cuenta."),
        ("abc", "{F} Una compañera dice que el nodo A une B1(+) con S1 y un compañero dice que lo une con L1. ¿Quién tiene razón según la ficha?", "La compañera: el nodo A une B1(+) con S1", "El compañero: el nodo A une B1(+) con L1", "Ambos, porque en un circuito todo se une con todo", "La lista de conexiones fija qué se une en cada nodo, y la ficha dice que el nodo A une B1(+) con S1."),
        ("=", "{F} Un cable de 45 cm reales se dibuja en un plano con la escala de la ficha. ¿Cuántos centímetros mide en el plano?", "45//5", "La medida real se divide por la escala 1:5 para obtener la del plano.", " cm"),
        ("abc", "{F} Se quita S1 del esquema y se unen directamente los nodos A y B. ¿Qué cambia en el funcionamiento?", "La lámpara ya no se puede apagar con un interruptor", "La lámpara nunca vuelve a encender", "La lámpara enciende solo la mitad del tiempo", "Sin interruptor el camino queda siempre cerrado, así que la lámpara no puede apagarse con él."),
    ],
    ctx=("abc", "Un técnico de ejemplo lee en un plano a escala 1:10 que un soporte mide 7 cm. Va a pedir una lámina de metal para fabricarlo. ¿Qué medida real debe pedir?", "70 cm, porque cada centímetro del plano son 10 reales", "7 cm, porque es la medida dibujada", "17 cm, porque se suma la escala", "La medida real se obtiene multiplicando la dibujada por la escala: 7 por 10 son 70 cm."),
    sc=[
        ("En Electrónica: ¿qué dice la polaridad de un componente?", "Cuál terminal es positivo (+) y cuál negativo (−)", "La polaridad identifica los terminales positivo y negativo."),
        ("¿Qué ocurre con la corriente si un interruptor está abierto?", "No circula, porque el camino se interrumpe", "Un interruptor abierto corta el camino de la corriente."),
        ("¿Quién revisa y autoriza un cambio en el esquema?", "El supervisor, con el proyectista", "El técnico no cambia documentos por su cuenta."),
    ],
    op=("Ficha para la actividad (de ejemplo): timbre de 6 V. Leyenda: B1 = batería de 6 V; P1 = pulsador; T1 = timbre. Conexiones: nodo A = B1(+) con P1; nodo B = P1 con T1; nodo C = T1 con B1(−). Escala del plano: 1:10. Escribe (a) qué dos terminales se unen en el nodo B, (b) qué pasa con el timbre si P1 no está presionado y por qué, (c) cuánto mide en la realidad un cable que mide 3 cm en el plano.",
        "(a) Un terminal de P1 y un terminal de T1. (b) El timbre no suena: el pulsador sin presionar deja el camino interrumpido, así que no circula corriente. (c) 3 por 10 son 30 cm.",
        ["identifica bien los terminales del nodo B", "explica el efecto del camino interrumpido", "aplica bien la escala"],
        ["hoja con las tres respuestas y el cálculo de la escala"],
        ["decir que el timbre suena sin camino cerrado", "no multiplicar por la escala", "confundir los nodos"],
        "Pregunta: «¿por qué no circula corriente si el pulsador no está presionado?». Si no responde, pídele que relea la idea de circuito cerrado."),
    reinforce="Dibuja a mano alzada un croquis de la linterna de la ficha usando la leyenda, y escribe al lado la lista de conexiones.",
    extend="Explica con un ejemplo por qué importa que el supervisor autorice un cambio en el esquema antes de que se ejecute.",
)

# ============================================================ OAE-01, clase 3
F = ("Ficha 3 (hoja de datos de un resistor inventado, de ejemplo). Resistor de la serie «RX»: valor 1 kΩ (1 kΩ = 1000 Ω, ohmios); tolerancia ±10 %; potencia máxima 250 mW (1 W = 1000 mW, milivatios); "
     "temperatura máxima de trabajo 70 °C. Código de colores: negro 0, marrón 1, rojo 2, naranja 3, amarillo 4, verde 5, azul 6, violeta 7, gris 8, blanco 9; "
     "las dos primeras bandas son dígitos, la tercera dice cuántos ceros se agregan y la cuarta es la tolerancia (dorado ±5 %, plateado ±10 %).")
build(
    O1, 3, F,
    use="Aprenderé a leer una hoja de datos y el código de colores de un resistor, y a decidir si un componente sirve para un caso, siempre en papel.",
    prior=["Sé multiplicar y calcular porcentajes sencillos.", "Sé que un documento técnico trae valores y límites.", "Sé leer una tabla."],
    explain=[
        "Una hoja de datos es el documento del fabricante que dice cómo es un componente y hasta dónde puede trabajar. El resistor limita la corriente y su valor se mide en ohmios (Ω); 1 kΩ son 1000 Ω. La tolerancia dice cuánto puede alejarse su valor real del valor indicado, en porcentaje: un resistor de 1000 Ω con tolerancia ±10 % puede valer entre 900 y 1100 Ω. La potencia máxima es el límite de energía por segundo que soporta sin dañarse; se mide en vatios (W) o milivatios (mW).",
        "Muchos resistores traen el valor en bandas de colores. Se lee así: la primera banda es el primer dígito, la segunda es el segundo dígito, la tercera indica cuántos ceros se agregan y la cuarta es la tolerancia. Por ejemplo, azul, gris y naranja dan 6, 8 y tres ceros: 68.000 Ω. La temperatura máxima de trabajo también es un límite.",
        f"Regla de oro: un componente solo sirve si cumple todos los valores que pide el caso. Si no cumple uno, no se usa y se informa. {AVISO}",
    ],
    vocab=[("hoja de datos", "documento del fabricante con las características y los límites de un componente"), ("resistor", "componente que limita la corriente"), ("ohmio (Ω)", "unidad con que se mide la resistencia"), ("tolerancia", "cuánto puede alejarse el valor real del indicado, en porcentaje"), ("potencia máxima", "límite de energía por segundo que el componente soporta sin dañarse"), ("banda de color", "franja pintada que, según el código, indica un dígito, una cantidad de ceros o la tolerancia")],
    worked=[
        ("Leer bandas", "Un resistor de ejemplo tiene bandas naranja, naranja, marrón y dorado. ¿Qué valor y tolerancia indica?", ["Naranja es 3 y naranja es 3: los dígitos son 33.", "Marrón es 1: se agrega un cero, así que son 330 Ω; dorado es ±5 %."], "330 Ω con tolerancia ±5 %"),
        ("Rango por tolerancia", "Un resistor de 200 Ω tiene tolerancia ±10 %. ¿Entre qué valores puede estar su valor real?", ["El 10 % de 200 es 20.", "Va de 200 menos 20 a 200 más 20."], "Entre 180 Ω y 220 Ω"),
    ],
    mistakes=[("Leer las bandas rojo, violeta y amarillo como «274 Ω» juntando los tres números.", "La tercera banda no es un dígito: indica cuántos ceros se agregan.", "Usa los dos primeros dígitos y agrega tantos ceros como diga la tercera banda."),
              ("Usar un componente porque su valor coincide, sin revisar la potencia máxima ni la temperatura.", "Un componente puede coincidir en valor y fallar en sus límites.", "Compara cada valor del caso con la hoja de datos.")],
    T=[
        ("abc", "En Electrónica: ¿qué es la tolerancia de un resistor?", "Cuánto puede alejarse su valor real del valor indicado, en porcentaje", "La potencia máxima que soporta", "La temperatura a la que se derrite", "La tolerancia es la desviación permitida del valor indicado, no un límite de potencia ni de temperatura."),
        ("abc", "En Electrónica: ¿qué es una hoja de datos?", "El documento del fabricante con las características y los límites de un componente", "El manual de uso que recibe el cliente final", "La factura de compra del componente", "La hoja de datos describe el componente y sus límites; la factura y el manual cumplen otras funciones."),
        ("abc", "Un resistor tiene bandas marrón, negro y rojo. ¿Qué valor indica según el código de colores?", "1000 Ω", "102 Ω", "100 Ω", "Los dos primeros dígitos son 1 y 0, y la banda roja agrega dos ceros: 1000 Ω."),
        ("=", "{F} ¿Cuál es el valor mínimo posible, en ohmios, de un resistor de 1000 Ω con la tolerancia de la ficha?", "1000-1000*10//100", "Se resta del valor el 10 % de tolerancia.", " Ω"),
        ("abc", "{F} Un montaje de ejemplo exige un resistor que soporte al menos 300 mW. ¿Sirve el de la ficha?", "No, porque su máximo es 250 mW, menor que 300 mW", "Sí, porque 250 mW está cerca de 300 mW", "Sí, porque su tolerancia es baja", "El límite de potencia debe ser al menos el exigido; 250 mW no alcanza 300 mW."),
        ("abc", "Un resistor de ejemplo tiene bandas rojo, rojo, naranja y dorado. ¿Qué valor y tolerancia indica?", "22.000 Ω con tolerancia ±5 %", "223 Ω con tolerancia ±5 %", "22.000 Ω con tolerancia ±10 %", "Los dígitos 2 y 2, más tres ceros por el naranja, dan 22.000 Ω; el dorado indica ±5 %."),
        ("=", "{F} Cada resistor de la serie cuesta $30 (de ejemplo). Un pedido es de 150 resistores. ¿Cuánto cuesta?", "30*150", "El precio unitario se multiplica por la cantidad pedida.", " pesos"),
        ("abc", "{F} Un técnico autorizado informa que un resistor del lote vale 1080 Ω. ¿Está dentro de su tolerancia?", "Sí, porque está entre 900 y 1100 Ω", "No, porque supera 1000 Ω", "No, porque la tolerancia es ±5 %", "Con ±10 % el rango va de 900 a 1100 Ω, y 1080 Ω está dentro."),
        ("=", "Un resistor de ejemplo tiene bandas amarillo, violeta, marrón y plateado. Calcula su valor máximo posible en ohmios.", "470+470*10//100", "Bandas: 47 y un cero dan 470 Ω; el plateado indica ±10 %, que se suma al valor.", " Ω"),
        ("abc", "{F} Un manual de ejemplo pide un resistor de 1 kΩ que soporte al menos 500 mW. La bodega solo tiene el de la ficha. ¿Qué decisión es correcta?", "No usarlo, informar que su potencia máxima es insuficiente y pedir otro", "Usarlo, porque el valor coincide", "Usarlo, porque la tolerancia ±10 % compensa la potencia", "La potencia máxima de 250 mW no cumple los 500 mW pedidos; el valor igual no compensa un límite."),
        ("abc", "Un resistor de ejemplo tiene bandas verde, azul, negro y dorado. ¿Qué valor indica?", "56 Ω", "560 Ω", "506 Ω", "La banda negra es 0, así que no se agrega ningún cero a los dígitos 5 y 6: 56 Ω."),
        ("=", "Un taller de ejemplo compra 12 resistores de $25 cada uno y 8 interruptores de $90 cada uno. ¿Cuánto paga en total?", "12*25+8*90", "Se suma el costo de los resistores y el costo de los interruptores.", " pesos"),
        ("abc", "{F} El resistor trabajaría en un lugar de ejemplo que llega a 85 °C. ¿Qué corresponde?", "No usarlo allí y buscar otro con mayor temperatura máxima de trabajo", "Usarlo igual, porque 85 °C está cerca de 70 °C", "Usarlo, porque la tolerancia ±10 % compensa la temperatura", "El límite de 70 °C es menor que 85 °C, por lo que el componente no sirve para ese lugar."),
    ],
    ctx=("abc", "Una técnica de ejemplo recibe un resistor sin etiqueta con bandas amarillo, violeta, rojo y dorado, y la hoja del proyecto pide 4700 Ω con ±5 %. ¿Qué concluye?", "Cumple: 47 más dos ceros son 4700 Ω y el dorado es ±5 %", "No cumple: el valor sería 472 Ω", "No cumple: el dorado indica ±10 %", "Los dígitos 4 y 7 más dos ceros dan 4700 Ω, y el dorado indica ±5 %, igual que lo pedido."),
    sc=[
        ("En Electrónica: ¿qué indica la tercera banda de color de un resistor?", "Cuántos ceros se agregan a los dos primeros dígitos", "La tercera banda funciona como multiplicador de ceros."),
        ("¿Cuándo sirve un componente para un caso?", "Cuando cumple todos los valores que pide el caso", "Si falla un solo valor, el componente no sirve."),
        ("¿Qué mide la potencia máxima de una hoja de datos?", "El límite de energía por segundo que el componente soporta", "Es un límite del componente, no su valor."),
    ],
    op=("Hoja de datos de ejemplo del resistor «RZ»: 2200 Ω, tolerancia ±5 %, potencia máxima 500 mW, temperatura máxima de trabajo 80 °C. El proyecto pide un resistor de 2200 Ω, tolerancia máxima ±5 %, al menos 250 mW y una temperatura de trabajo de al menos 60 °C. Escribe (a) cuál es el rango de valor real posible de RZ, (b) si cumple cada requisito, con la razón, (c) cuántos pesos costarían 40 unidades si cada una vale $35 (de ejemplo).",
        "(a) El 5 % de 2200 es 110: va de 2090 a 2310 Ω. (b) Valor 2200 igual al pedido: cumple. Tolerancia ±5 % igual a la máxima aceptada: cumple. Potencia 500 mW es mayor que 250 mW: cumple. Temperatura 80 °C es mayor que 60 °C: cumple. (c) 35 por 40 son 1400 pesos.",
        ["calcula bien el rango por tolerancia", "compara los cuatro requisitos uno por uno", "calcula bien el costo"],
        ["hoja con el rango, la tabla de requisitos y el costo"],
        ["calcular mal el porcentaje", "olvidar revisar un requisito", "decidir sin comparar"],
        "Pregunta: «¿qué pasaría si la potencia máxima fuera 200 mW?». Si no responde, pídele que relea la regla de oro."),
    reinforce="Escribe tres resistores de ejemplo con bandas de colores inventadas y calcula el valor de cada uno con el código de la ficha.",
    extend="Explica con un ejemplo por qué un componente con el valor correcto igual puede no servir en un caso.",
)

# ============================================================ OAE-01, clase 4
F = ("Ficha 4 (requisito y catálogo de ejemplo, inventados). Requisito del proyecto «Panel de luces de 12 V»: un resistor de 470 Ω, tolerancia máxima aceptada ±5 %, potencia máxima de al menos 500 mW y temperatura de trabajo de al menos 60 °C. "
     "Catálogo (precios de ejemplo): opción P: 470 Ω, ±5 %, 250 mW, 70 °C, $40; opción Q: 470 Ω, ±5 %, 1000 mW, 85 °C, $90; opción R: 470 Ω, ±10 %, 1000 mW, 85 °C, $60; opción S: 680 Ω, ±5 %, 1000 mW, 85 °C, $70.")
build(
    O1, 4, F,
    use="Aprenderé a comparar los requisitos de un proyecto con un catálogo de ejemplo, a elegir con criterio técnico y a dejar la decisión por escrito.",
    prior=["Sé leer una hoja de datos.", "Sé calcular el costo de varias unidades.", "Sé qué es la tolerancia."],
    explain=[
        "Un requisito técnico es una condición que el componente debe cumplir: valor, tolerancia, potencia máxima o temperatura de trabajo. Para elegir se compara cada opción del catálogo con cada requisito, uno por uno, y se descarta la opción que falle en cualquiera. Solo entre las que cumplen todo se mira el precio.",
        "El margen de seguridad es la diferencia entre el límite del componente y lo que realmente va a soportar. Por ejemplo, si el proyecto exige 200 mW y el componente soporta 600 mW, hay 400 mW de margen. Más margen da más tranquilidad, pero suele costar más, por lo que el proyecto fija el mínimo exigido.",
        f"Una decisión técnica se registra: qué opción se eligió, qué requisitos se revisaron y el precio. Así otra persona puede revisarla y repetirla. Si ninguna opción cumple, se informa; no se baja el requisito por cuenta propia. {AVISO}",
    ],
    vocab=[("requisito técnico", "condición que el componente debe cumplir"), ("catálogo", "lista de opciones con sus características y precios"), ("margen de seguridad", "diferencia entre el límite del componente y lo que va a soportar"), ("descartar", "dejar fuera una opción porque no cumple"), ("registro de decisión", "nota escrita de qué se eligió y por qué")],
    worked=[
        ("Revisar una opción", "Un proyecto de ejemplo exige 300 mW. La opción X soporta 400 mW y la opción Y soporta 200 mW. ¿Cuál cumple y cuánto margen tiene?", ["X: 400 es mayor o igual que 300, cumple; Y: 200 es menor que 300, no cumple.", "El margen de X es 400 menos 300."], "X cumple, con 100 mW de margen"),
        ("Costo total", "La opción X cuesta $50 cada una y se necesitan 8. ¿Cuánto cuesta la compra?", ["Se multiplica el precio por la cantidad.", "50 por 8 son 400."], "$400"),
    ],
    mistakes=[("Elegir la opción más barata aunque no cumpla un requisito.", "El precio se mira solo entre las opciones que cumplen todo.", "Descarta primero lo que falla y compara precios después."),
              ("Bajar un requisito por cuenta propia cuando ninguna opción lo cumple.", "Cambiar un requisito exige autorización del proyectista o del supervisor.", "Informa que ninguna opción cumple y espera una decisión.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un requisito técnico de un proyecto?", "Una condición que el componente debe cumplir, como valor, tolerancia o potencia", "Una sugerencia que se puede ignorar", "El precio máximo que acepta el cliente", "Un requisito técnico es una condición obligatoria del componente; el precio es otro criterio."),
        ("abc", "En Electrónica: ¿qué es el margen de seguridad de un componente?", "La diferencia entre su límite y lo que realmente va a soportar", "Un descuento que da el fabricante", "El tiempo de garantía del componente", "El margen mide cuánto sobra entre el límite y la exigencia real."),
        ("abc", "{F} ¿Cuántos requisitos técnicos tiene el proyecto de la ficha?", "Cuatro: valor, tolerancia, potencia y temperatura", "Tres: valor, potencia y precio", "Cinco: los cuatro técnicos más el nombre del catálogo", "La ficha pide valor, tolerancia, potencia y temperatura; el precio no es un requisito técnico."),
        ("abc", "{F} ¿Qué opción del catálogo cumple los cuatro requisitos?", "La opción Q", "La opción P", "La opción R", "Solo Q cumple valor, tolerancia, potencia y temperatura; P y R fallan en alguno."),
        ("abc", "{F} ¿Por qué se descarta la opción S?", "Su valor es 680 Ω y el proyecto pide 470 Ω", "Su potencia máxima es menor que la pedida", "Su temperatura máxima es menor que la pedida", "S tiene 1000 mW y 85 °C, que sí cumplen; falla en el valor del resistor."),
        ("abc", "{F} ¿Qué requisito incumple la opción R?", "La tolerancia: ±10 % es peor que el máximo aceptado de ±5 %", "La potencia máxima: 1000 mW es menor que 500 mW", "El valor: 470 Ω no es el pedido", "R tiene ±10 %, mayor que el ±5 % aceptado; sus demás datos cumplen."),
        ("=", "{F} ¿Cuántos mW de margen de potencia tiene la opción Q respecto de lo exigido?", "1000-500", "El margen es el límite de la opción menos la potencia exigida.", " mW"),
        ("=", "{F} El proyecto necesita 10 resistores. ¿Cuánto cuesta comprar 10 de la opción que cumple todo?", "10*90", "El precio de la opción Q se multiplica por la cantidad.", " pesos"),
        ("abc", "{F} El supervisor pregunta por qué no se compró la opción P, que es la más barata. ¿Cuál es la respuesta técnica correcta?", "Su potencia máxima de 250 mW no alcanza los 500 mW exigidos", "Su tolerancia es peor que la aceptada", "Su valor es distinto de 470 Ω", "P tiene 470 Ω y ±5 %; falla en la potencia máxima."),
        ("abc", "{F} Un compañero propone usar la opción P para ahorrar, porque «250 mW casi alcanza». ¿Qué argumento es correcto?", "Un requisito no cumplido no se compensa con ahorro; si se quiere cambiar, lo autoriza el proyectista o el supervisor", "Es válido, porque la diferencia es pequeña", "Es válido, siempre que se anote el precio", "Un requisito se cumple o no se cumple; solo quien autoriza el proyecto puede cambiarlo."),
        ("=", "{F} Se necesitan 20 resistores. ¿Cuántos pesos más cuesta comprarlos de la opción Q que de la opción P?", "(90-40)*20", "La diferencia de precio por unidad se multiplica por las 20 unidades.", " pesos"),
        ("abc", "{F} El catálogo cambia: Q sube a $120 y aparece la opción T: 470 Ω, ±5 %, 750 mW, 85 °C, $100. Si se debe cumplir todo y gastar lo menos posible, ¿cuál conviene?", "La opción T", "La opción Q", "La opción P", "T cumple todos los requisitos y cuesta menos que Q; P no cumple la potencia."),
        ("abc", "{F} Antes de comprar, el técnico anota la opción elegida, los requisitos revisados y el precio. ¿Para qué sirve ese registro?", "Para que otra persona pueda revisar y repetir la decisión", "Para no tener que leer la ficha otra vez", "Para poder cambiar los requisitos más adelante", "Un registro hace trazable la decisión y permite que otros la comprueben."),
    ],
    ctx=("abc", "Un taller de ejemplo debe elegir un resistor para un cargador de 5 V de juguete. Dos opciones cumplen todos los requisitos: una cuesta $45 y otra $70. ¿Qué criterio corresponde?", "Elegir la de $45 y registrar la decisión, porque ambas cumplen todo", "Elegir la de $70, porque lo más caro siempre es mejor", "Elegir al azar, porque ambas cumplen", "Si todas las opciones cumplen los requisitos, se elige la más conveniente por precio y se deja registro."),
    sc=[
        ("En Electrónica: ¿cómo se compara una opción de catálogo con un proyecto?", "Revisando cada requisito, uno por uno", "Se descarta la opción que falle en cualquier requisito."),
        ("¿Qué se hace si ninguna opción cumple todos los requisitos?", "Informar y esperar la decisión de quien autoriza el proyecto", "No se baja un requisito por cuenta propia."),
        ("¿Qué datos debe tener el registro de una decisión de compra?", "Qué se eligió, qué requisitos se revisaron y el precio", "Esos datos permiten que otra persona repita la revisión."),
    ],
    op=("Ficha de ejemplo: requisito de un sensor de temperatura para una incubadora de juguete de 5 V: valor 1000 Ω, tolerancia máxima ±10 %, potencia máxima de al menos 250 mW. Catálogo de ejemplo: M: 1000 Ω, ±5 %, 125 mW, $50; N: 1000 Ω, ±10 %, 250 mW, $65; O: 1000 Ω, ±10 %, 500 mW, $80. Escribe (a) cuáles opciones cumplen, (b) cuál eliges y por qué, (c) cuánto cuestan 15 unidades de la elegida, (d) qué anotarías en el registro.",
        "(a) N y O cumplen; M falla en potencia (125 mW es menor que 250 mW). (b) N, porque cumple todo y es más barata que O. (c) 65 por 15 son 975 pesos. (d) Opción elegida (N), requisitos revisados (valor, tolerancia, potencia), precio unitario y total.",
        ["descarta la opción que no cumple con la razón", "elige la más barata entre las que cumplen", "calcula bien el costo", "propone un registro completo"],
        ["hoja con la tabla de comparación, la decisión y el registro"],
        ["elegir la más barata sin revisar requisitos", "calcular mal el total", "no dejar registro"],
        "Pregunta: «¿qué harías si N costara más que O?». Si no responde, pídele que relea cómo se elige entre opciones que cumplen todo."),
    reinforce="Inventa un requisito con tres condiciones para un componente y un catálogo de tres opciones; indica cuál cumple y por qué.",
    extend="Explica con un ejemplo por qué elegir siempre el componente con mayor margen no siempre es la mejor decisión de un proyecto.",
)

# ============================================================ OAE-02, clase 1
F = ("Ficha 1 (caso de ejemplo, inventado). Un taller escolar ficticio recibe un radio portátil de 6 V que «no suena». Informe del cliente: ayer funcionaba; hoy el indicador luminoso no enciende y la tapa de las pilas se golpeó. "
     "Documentos disponibles: manual del radio, con su tabla de especificaciones, y esquema del radio. Riesgos anotados: el radio usa pilas y un adaptador que se conecta a la red eléctrica.")
build(
    O2, 1, F,
    use="Aprenderé qué es una falla, qué es un síntoma y cómo se razona un diagnóstico a partir de lo observado y de las especificaciones del fabricante, sin tocar equipos.",
    prior=["Sé leer una ficha técnica.", "Sé qué es un esquema.", "Sé que un informe debe ser claro y ordenado."],
    explain=[
        "Una falla es cuando un equipo deja de hacer lo que debe. El síntoma es lo que se observa de esa falla, por ejemplo «el indicador no enciende». La causa es el origen real del problema, que al comienzo no se conoce. Diagnosticar es razonar desde los síntomas hacia la causa, comparando lo observado con lo que el fabricante indica en sus especificaciones: la tabla de valores con que el equipo debe funcionar. La inspección es la revisión ordenada y registrada de lo que se ve y de lo que se anota.",
        "En electrónica se habla de tres magnitudes básicas: la tensión, que se mide en voltios (V) y es el empuje que mueve la corriente; la corriente, que se mide en amperios (A) y es el flujo de carga eléctrica; y la resistencia, que se mide en ohmios (Ω) y es la dificultad que el material opone al paso de la corriente. La lógica del diagnóstico parte de las causas más simples y menos riesgosas, como la falta de energía, y deja para el final las más complejas. Una suposición no es una causa comprobada: se anota como «probable».",
        f"{EMER} Las revisiones de equipos con energía las hace personal autorizado. {AVISO}",
    ],
    vocab=[("falla", "situación en que un equipo deja de hacer lo que debe"), ("síntoma", "lo que se observa de una falla"), ("causa", "origen real de una falla"), ("diagnóstico", "razonamiento que va de los síntomas a la causa probable"), ("especificaciones del fabricante", "tabla de valores y límites con que el equipo debe funcionar"), ("tensión", "empuje que mueve la corriente; se mide en voltios (V)"), ("corriente", "flujo de carga eléctrica; se mide en amperios (A)"), ("resistencia", "dificultad al paso de la corriente; se mide en ohmios (Ω)")],
    worked=[
        ("Síntoma o causa", "Una técnica de ejemplo anota: «la lámpara de la entrada no enciende». ¿Es un síntoma o una causa?", ["Lo anotado es algo que se observa.", "No dice por qué ocurre."], "Es un síntoma"),
        ("Orden lógico", "Una radio de ejemplo no enciende. Hay dos causas posibles: pilas sin energía o un componente interno dañado. ¿Cuál se considera primero y por qué?", ["Se parte por la causa más simple y menos riesgosa.", "La falta de energía de las pilas es más simple que un componente interno."], "Las pilas sin energía, por ser más simple y menos riesgosa"),
    ],
    mistakes=[("Anotar «causa: pilas agotadas» sin haber revisado nada.", "Es una suposición presentada como una causa comprobada.", "Escribe «causa probable» y anota qué falta para confirmarla."),
              ("Abrir un equipo conectado a la red para «ver qué pasa».", "Esa tarea es de riesgo y exige personal autorizado y norma vigente.", "Registra los síntomas y deriva la revisión a personal autorizado.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un síntoma?", "Lo que se observa de la falla, como que un indicador no enciende", "El origen real de la falla", "La reparación que se propone", "El síntoma es lo observable; la causa es el origen y la reparación viene después."),
        ("abc", "En Electrónica: ¿qué son las especificaciones del fabricante?", "La tabla de valores y límites con que el equipo debe funcionar", "La opinión del cliente sobre el equipo", "El precio de venta del equipo", "Las especificaciones fijan lo esperado, que sirve para comparar con lo observado."),
        ("abc", "¿Con qué unidad se mide la tensión eléctrica?", "Voltio (V)", "Amperio (A)", "Ohmio (Ω)", "La tensión se mide en voltios; los amperios miden corriente y los ohmios, resistencia."),
        ("abc", "{F} ¿Cuál de estas frases de la ficha es un síntoma?", "El indicador luminoso no enciende", "La tapa de las pilas se golpeó", "El adaptador se conecta a la red eléctrica", "El indicador apagado es lo que se observa del problema; los otros datos son contexto."),
        ("abc", "{F} ¿Qué dato de la ficha apunta a una posible causa mecánica?", "La tapa de las pilas se golpeó", "El manual trae una tabla de especificaciones", "El esquema forma parte de los documentos", "El golpe a la tapa es el único dato que sugiere un daño físico."),
        ("abc", "{F} ¿Cuál de estas tareas no corresponde a una persona que solo estudia este cuaderno?", "Abrir el adaptador conectado a la red para revisarlo", "Leer la tabla de especificaciones del manual", "Ordenar por escrito los síntomas informados", "Un adaptador conectado a la red exige personal autorizado; leer y ordenar datos no."),
        ("=", "{F} El taller diagnostica 3 radios por día durante 5 días y cobra $4.000 por diagnóstico (de ejemplo). ¿Cuánto cobra en total?", "3*5*4000", "Se multiplican los radios por día, los días y el valor del diagnóstico.", " pesos"),
        ("abc", "{F} Para el síntoma de la ficha, ¿qué causa conviene considerar primero?", "La falta de energía, como pilas agotadas o mal puestas tras el golpe", "Un defecto en el componente más pequeño del esquema", "Un error de diseño del fabricante", "El diagnóstico parte de las causas más simples y menos riesgosas, y la falta de energía lo es."),
        ("ab", "Una técnica anota solo «el radio está malo» como diagnóstico. ¿Es un buen registro?", "No: debe incluir el síntoma observado, lo que se descartó y la fecha", "Sí: una frase corta basta si el cliente la entiende", "Un diagnóstico útil deja constancia de síntoma, lo descartado y fecha para que otra persona lo repita."),
        ("abc", "Un técnico de ejemplo escribe «causa: no suena». ¿Qué corrige un lector atento?", "«No suena» es un síntoma; la causa es el origen que aún hay que determinar", "Está correcto: la causa de que no suene es que no suena", "«No suena» es la reparación, no la causa", "Lo que se observa es el síntoma; la causa se determina razonando con los datos."),
        ("abc", "{F} Un compañero propone escribir en el informe «causa: pilas agotadas» sin haber revisado nada. ¿Qué falla de método tiene?", "Presenta una suposición como si fuera una causa comprobada", "Las pilas nunca pueden ser la causa de una falla", "Debería anotar primero el precio de las pilas", "Una suposición se anota como causa probable hasta que algún dato la confirme."),
        ("=", "Un taller de ejemplo documenta cada diagnóstico en 2 horas. Recibe 8 radios iguales y trabaja 4 horas por día. ¿En cuántos días termina?", "8*2//4", "Las horas totales se dividen por las horas de trabajo de cada día.", " días"),
        ("abc", "Un cargador de ejemplo echa humo en la sala de clases. ¿Qué corresponde según las reglas generales?", "Alejarse, avisar a un adulto responsable y a emergencias, y cortar el suministro solo si se está autorizado", "Echarle agua para apagarlo cuanto antes", "Sacarlo de la sala con las manos para que no moleste", "Ante un incendio eléctrico no se manipula el equipo; se aleja a las personas y se avisa a emergencias."),
    ],
    ctx=("abc", "En un taller de ejemplo, un cliente dice: «conecta el radio a la red y ábrelo para mirar adentro mientras funciona; yo me hago responsable». ¿Qué respondes como estudiante?", "Explicar que eso lo hace personal autorizado con norma vigente y proponer derivarlo", "Aceptar, porque el cliente asume la responsabilidad", "Hacerlo rápido para que no se enfríe el equipo", "La responsabilidad del cliente no reemplaza la norma ni la autorización; un estudiante no abre equipos con energía."),
    sc=[
        ("En Electrónica: ¿qué es un diagnóstico?", "El razonamiento que va de los síntomas a la causa probable", "El diagnóstico compara lo observado con lo esperado."),
        ("¿Qué magnitud se mide en amperios?", "La corriente", "El amperio es la unidad del flujo de carga eléctrica."),
        ("¿Cómo se anota una causa que aún no se comprobó?", "Como causa probable, indicando qué falta para confirmarla", "Una suposición no se presenta como hecho."),
    ],
    op=("Caso de ejemplo: un timbre de 6 V de una escuela no suena al presionar el pulsador. El conserje informa que ayer sonaba y que hoy se cambiaron las pilas. Documentos: manual del timbre y esquema. Escribe (a) el síntoma, (b) dos causas posibles ordenadas de la más simple a la más compleja, (c) qué documento usarías para comparar con lo esperado, (d) una tarea que no harías tú.",
        "(a) El timbre no suena al presionar el pulsador. (b) Primero una pila mal puesta o sin energía; después un pulsador o un componente interno dañado. (c) La tabla de especificaciones del manual. (d) Abrir o revisar partes con energía, que le corresponde a personal autorizado con norma vigente.",
        ["distingue síntoma de causa", "ordena las causas de lo simple a lo complejo", "nombra el documento de comparación", "reconoce una tarea que no le corresponde"],
        ["hoja con las cuatro respuestas"],
        ["escribir una causa como si estuviera comprobada", "no ordenar las causas", "decir que él mismo abriría el equipo"],
        "Pregunta: «¿qué dato te permitiría confirmar tu causa probable?». Si no responde, pídele que relea la regla de las causas probables."),
    reinforce="Escribe tres síntomas de ejemplo de un equipo electrónico cotidiano y, para cada uno, una causa simple posible.",
    extend="Explica con un ejemplo por qué un diagnóstico escrito protege al taller y al cliente.",
)

# ============================================================ OAE-02, clase 2
F = ("Ficha 2 (especificaciones de ejemplo, inventadas). Lámpara de práctica: tensión de funcionamiento 12 V; resistencia 6 Ω. Fórmulas: corriente (A) = tensión (V) ÷ resistencia (Ω); "
     "potencia (W) = tensión (V) × corriente (A); 1 A = 1000 mA (miliamperios). Cable de práctica: soporta como máximo 1 A (de ejemplo).")
build(
    O2, 2, F,
    use="Aprenderé la ley de Ohm y la potencia eléctrica para calcular en papel los valores esperados de un circuito sencillo y compararlos con un registro.",
    prior=["Sé multiplicar y dividir números enteros.", "Sé qué son tensión, corriente y resistencia.", "Sé qué es una especificación del fabricante."],
    explain=[
        "La ley de Ohm relaciona tres magnitudes: la tensión es igual a la corriente por la resistencia. Se escribe V = I × R. Despejando se obtiene la corriente I = V ÷ R, y la resistencia R = V ÷ I. Si una lámpara de ejemplo tiene 12 V y 4 Ω de resistencia, circulan 3 A. Con la ley de Ohm se calcula el valor esperado y se compara con el registro hecho por personal autorizado.",
        "La potencia eléctrica es la energía que un equipo usa o entrega cada segundo, y se mide en vatios (W). Se calcula multiplicando tensión por corriente: P = V × I. Por eso, con 12 V y 3 A la potencia es 36 W. Si se conoce la potencia y la tensión, la corriente es I = P ÷ V. Las corrientes pequeñas se expresan en miliamperios (mA): 1 A son 1000 mA.",
        f"Cada componente y cada cable tienen un límite de corriente o de potencia; si el circuito exige más, se calienta y es un riesgo de incendio. Solo se trabaja con valores bajos de ejemplo en papel. {AVISO}",
    ],
    vocab=[("ley de Ohm", "relación V = I × R entre tensión, corriente y resistencia"), ("potencia eléctrica", "energía que un equipo usa o entrega cada segundo; se mide en vatios (W)"), ("vatio (W)", "unidad de potencia eléctrica"), ("miliamperio (mA)", "milésima de amperio; 1 A son 1000 mA"), ("valor esperado", "valor que se calcula o que indica el fabricante y se usa para comparar"), ("límite de corriente", "máximo de corriente que un componente o cable soporta sin dañarse")],
    worked=[
        ("Calcular la corriente", "Una lámpara de ejemplo tiene 9 V y 3 Ω de resistencia. ¿Qué corriente circula?", ["Se usa I = V ÷ R.", "9 dividido en 3 son 3 amperios."], "3 A"),
        ("Calcular la potencia", "Un equipo de ejemplo usa 9 V y 3 A. ¿Cuántos vatios usa?", ["Se usa P = V × I.", "9 por 3 son 27."], "27 W"),
    ],
    mistakes=[("Calcular la corriente multiplicando la tensión por la resistencia.", "La corriente se obtiene dividiendo la tensión por la resistencia.", "Usa I = V ÷ R y comprueba que V = I × R."),
              ("Comparar 250 mA con 1 A sin convertir las unidades.", "Las magnitudes deben estar en la misma unidad para compararlas.", "Convierte: 1 A son 1000 mA, y recién entonces compara.")],
    T=[
        ("abc", "En Electrónica: ¿qué dice la ley de Ohm?", "La tensión es igual a la corriente por la resistencia", "La potencia es igual a la tensión dividida por la corriente", "La corriente es igual a la resistencia por la tensión", "La ley de Ohm es V = I × R; las otras fórmulas están mal planteadas."),
        ("abc", "En Electrónica: ¿qué unidad mide la corriente eléctrica?", "Amperio (A)", "Voltio (V)", "Vatio (W)", "La corriente se mide en amperios; el voltio mide tensión y el vatio, potencia."),
        ("abc", "En Electrónica: ¿qué es la potencia eléctrica?", "La energía que un equipo usa o entrega cada segundo", "La carga total que guarda una batería", "La dificultad que un cable opone a la corriente", "La potencia mide energía por segundo; la dificultad al paso de la corriente es la resistencia."),
        ("=", "{F} ¿Cuántos amperios circulan por la lámpara de la ficha?", "12//6", "La corriente es la tensión dividida por la resistencia.", " A"),
        ("=", "{F} Si por la lámpara circulan 2 A a 12 V, ¿cuántos vatios usa?", "12*2", "La potencia es la tensión multiplicada por la corriente.", " W"),
        ("abc", "{F} Si la tensión sube a 24 V con la misma resistencia de 6 Ω, ¿qué pasa con la corriente respecto de la de 12 V?", "Se duplica", "Se reduce a la mitad", "Queda igual", "La corriente es tensión dividida por resistencia: con el doble de tensión y la misma resistencia, se duplica."),
        ("=", "Un componente de ejemplo tiene 20 V entre sus terminales y por él circulan 4 A. ¿Cuál es su resistencia en ohmios?", "20//4", "La resistencia es la tensión dividida por la corriente.", " Ω"),
        ("=", "Un equipo de ejemplo de 5 V usa 3 A. ¿Cuántos vatios consume?", "5*3", "La potencia se obtiene multiplicando tensión por corriente.", " W"),
        ("abc", "{F} Un registro de personal autorizado dice que, con 12 V, la lámpara de la ficha tiene 1 A. ¿Cómo se compara con lo esperado?", "Es la mitad de lo esperado y hay que investigar la causa", "Es igual a lo esperado", "Es el doble de lo esperado", "Lo esperado es 2 A; un registro de 1 A es la mitad y señala un problema por investigar."),
        ("abc", "Un técnico dice que un equipo de ejemplo de 30 W y 10 V usa 3 A; otro dice que usa 300 A. ¿Quién tiene razón?", "El primero, porque la corriente es la potencia dividida por la tensión", "El segundo, porque se multiplican la potencia y la tensión", "Ninguno, porque faltan datos de resistencia", "I = P ÷ V, es decir 30 ÷ 10 = 3 A; no hace falta la resistencia."),
        ("=", "Una fuente de ejemplo de 12 V entrega como máximo 60 W. ¿Cuántos amperios entrega como máximo?", "60//12", "La corriente es la potencia dividida por la tensión.", " A"),
        ("abc", "{F} ¿Sirve el cable de la ficha para alimentar la lámpara a 12 V?", "No, porque la lámpara necesita 2 A y el cable soporta 1 A", "Sí, porque 12 V es una tensión baja", "Sí, porque el cable soporta 1 A y eso es suficiente", "Cada cable tiene un límite; 2 A superan el máximo de 1 A y el cable se calentaría."),
        ("=", "Un sensor de ejemplo consume 250 mA. Una fuente de ejemplo entrega 2 A. ¿Cuántos sensores iguales puede alimentar como máximo?", "2*1000//250", "Se pasan los amperios a miliamperios y se divide por el consumo de cada sensor.", " sensores"),
    ],
    ctx=("abc", "Un técnico de ejemplo lee en la hoja de un módulo: 12 V, 24 W. Necesita saber qué corriente espera encontrar para compararla con un registro. ¿Qué valor calcula?", "2 A, dividiendo 24 W entre 12 V", "288 A, multiplicando 24 por 12", "12 A, restando 12 de 24", "La corriente es I = P ÷ V, es decir 24 ÷ 12 = 2 A."),
    sc=[
        ("En Electrónica: ¿cómo se calcula la corriente con la tensión y la resistencia?", "Dividiendo la tensión entre la resistencia", "I = V ÷ R sale de la ley de Ohm."),
        ("¿Cómo se calcula la potencia eléctrica?", "Multiplicando la tensión por la corriente", "La potencia se calcula como P = V × I."),
        ("¿Cuántos miliamperios son 3 A?", "3000 mA", "Cada amperio equivale a 1000 miliamperios, así que 3 A son 3000."),
    ],
    op=("Ficha de ejemplo: un ventilador pequeño funciona con 24 V y tiene una resistencia equivalente de 8 Ω. Se usa un cable que soporta como máximo 2 A (de ejemplo). Escribe (a) la corriente esperada, (b) la potencia que usa, (c) si el cable sirve y por qué, (d) qué conclusión sacarías si un registro de personal autorizado marcara 1 A.",
        "(a) 24 ÷ 8 = 3 A. (b) 24 × 3 = 72 W. (c) No sirve: se esperan 3 A y el cable soporta 2 A, así que se calentaría. (d) 1 A es menos que lo esperado (3 A): hay que investigar la causa, por ejemplo una resistencia mayor que la indicada.",
        ["calcula bien la corriente", "calcula bien la potencia", "compara con el límite del cable", "interpreta el registro frente a lo esperado"],
        ["hoja con los cálculos y las conclusiones"],
        ["multiplicar en lugar de dividir", "no comparar con el límite del cable", "no relacionar el registro con lo esperado"],
        "Pregunta: «¿qué pasa con el cable si la corriente supera su máximo?». Si no responde, pídele que relea la idea de límite de corriente."),
    reinforce="Calcula en papel la corriente y la potencia de tres lámparas de ejemplo con 12 V y resistencias de 3, 4 y 6 Ω.",
    extend="Explica con un ejemplo por qué un registro menor que el valor esperado también puede ser señal de falla.",
)

# ============================================================ OAE-02, clase 3
F = ("Ficha 3 (caso y tabla de mediciones de ejemplo, inventados; registros hechos por personal autorizado). Luz de aviso de 12 V descrita por escrito: la batería B1 de 12 V, el fusible F1, el interruptor S1 y la lámpara L1 están en serie (un solo camino cerrado). "
     "Funcionamiento normal con S1 cerrado: 0 V entre los terminales de F1 y de S1, y 12 V entre los terminales de L1. Registro del caso con S1 cerrado: B1 = 12 V; F1 = 12 V; S1 = 0 V; L1 = 0 V. La lámpara no enciende.")
build(
    O2, 3, F,
    use="Aprenderé a leer una tabla de mediciones de ejemplo y a deducir, con lógica, qué elemento de un circuito en serie está fallando.",
    prior=["Sé qué son tensión y corriente.", "Sé leer una tabla.", "Sé qué es un interruptor y qué es una lámpara."],
    explain=[
        "Un circuito en serie tiene un solo camino para la corriente: lo recorre un componente tras otro. Un fusible es un componente de protección que se abre, y corta el camino, si pasa más corriente de la que soporta. En un circuito en serie la suma de las tensiones de los componentes es igual a la tensión de la batería. Si todo conduce, la corriente circula y la tensión se reparte según lo esperado.",
        "Cuando un elemento está abierto, no circula corriente por el camino. Entonces los elementos que conducen muestran 0 V entre sus terminales, y el elemento abierto muestra toda la tensión de la batería. Esta regla permite diagnosticar sobre una tabla de mediciones, que son valores registrados por personal autorizado en puntos del circuito. Se comparan con los valores normales y el elemento que no coincide es el sospechoso.",
        f"Un fusible abierto suele indicar que antes hubo una corriente excesiva: antes de proponer uno nuevo hay que buscar esa causa. Este cuaderno solo analiza tablas; medir, abrir o reparar requiere personal autorizado. {AVISO}",
    ],
    vocab=[("circuito en serie", "circuito con un solo camino para la corriente"), ("fusible", "componente de protección que se abre si pasa más corriente de la que soporta"), ("elemento abierto", "componente que interrumpe el camino de la corriente"), ("tabla de mediciones", "lista de valores registrados en puntos del circuito"), ("valor normal", "valor que debería registrarse si el circuito funciona bien")],
    worked=[
        ("Elemento abierto", "En un circuito en serie de ejemplo con batería de 6 V, un fusible, un interruptor cerrado y una lámpara, la lámpara no enciende. El registro muestra 6 V entre los terminales del fusible y 0 V en los demás elementos. ¿Qué elemento está abierto?", ["El elemento abierto muestra toda la tensión de la batería.", "El único con 6 V es el fusible."], "El fusible"),
        ("Suma de tensiones", "En un circuito en serie de ejemplo, la batería es de 9 V; el resistor R1 muestra 4 V y la lámpara muestra el resto. ¿Cuántos voltios hay en la lámpara?", ["La suma de tensiones es igual a la de la batería.", "9 menos 4 son 5."], "5 V"),
    ],
    mistakes=[("Cambiar la pieza que «se ve» más dañada sin mirar la tabla de mediciones.", "El dato de la tabla puede señalar otro elemento.", "Decide con los registros comparados con los valores normales."),
              ("Pensar que un elemento que muestra 0 V está dañado.", "En un circuito en serie con un elemento abierto, los que conducen muestran 0 V.", "El sospechoso es el que muestra toda la tensión de la batería.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un circuito en serie?", "Un circuito con un solo camino para la corriente", "Un circuito con varios caminos separados", "Un circuito sin batería", "En serie los componentes se recorren uno tras otro por un único camino."),
        ("abc", "En Electrónica: ¿qué es un fusible?", "Un componente de protección que se abre si pasa demasiada corriente", "Un componente que guarda energía para después", "Un interruptor que se acciona con la mano", "El fusible protege el circuito abriéndose cuando la corriente supera lo que soporta."),
        ("abc", "En Electrónica: ¿qué muestra una tabla de mediciones en un diagnóstico?", "Valores registrados en puntos del circuito, para compararlos con los normales", "El precio de cada componente del circuito", "El nombre del cliente que pidió el trabajo", "La tabla contiene registros que se comparan con los valores normales para encontrar la falla."),
        ("abc", "{F} ¿Qué elemento del registro muestra los 12 V completos entre sus terminales?", "El fusible F1", "El interruptor S1", "La lámpara L1", "En la tabla solo F1 muestra 12 V; S1 y L1 muestran 0 V."),
        ("abc", "{F} ¿Cuál es la causa más probable de que la lámpara no encienda?", "El fusible F1 está abierto", "La batería B1 está agotada", "El interruptor S1 está abierto", "F1 muestra la tensión completa, lo que indica que interrumpe el camino; B1 marca 12 V y S1 marca 0 V."),
        ("abc", "{F} ¿Por qué se descarta el interruptor S1 como causa?", "Porque marca 0 V, y un interruptor abierto mostraría los 12 V", "Porque los interruptores nunca fallan", "Porque no aparece en el esquema descrito", "Un elemento abierto mostraría toda la tensión; S1 marca 0 V, así que conduce."),
        ("abc", "Registro de ejemplo del mismo tipo de circuito, con el interruptor cerrado: B1 = 0 V; F1 = 0 V; S1 = 0 V; L1 = 0 V. ¿Cuál es la causa más probable?", "La batería no entrega tensión", "El fusible está abierto", "La lámpara está abierta", "Con todos los valores en 0 V falta la tensión de origen; un elemento abierto mostraría la tensión completa."),
        ("abc", "Registro de ejemplo de un circuito en serie con batería de 12 V, con el interruptor cerrado: B1 = 12 V; F1 = 0 V; S1 = 0 V; L1 = 12 V, y la lámpara no enciende. ¿Qué elemento está abierto?", "La lámpara L1", "El fusible F1", "El interruptor S1", "L1 muestra la tensión completa, lo que señala que el camino se interrumpe en ella."),
        ("=", "En un circuito en serie de ejemplo con batería de 12 V, F1 marca 0 V, S1 marca 0 V y un resistor R1 marca 5 V. Si todos conducen, ¿cuántos voltios marca la lámpara L1?", "12-0-0-5", "La suma de las tensiones en serie es igual a la de la batería.", " V"),
        ("abc", "{F} Un compañero propone cambiar primero la lámpara L1 porque «es lo que se ve». ¿Qué respuesta lógica corresponde?", "Los registros señalan a F1, no a L1; hay que decidir con la tabla", "Tiene razón, porque lo visible siempre es lo dañado", "Da igual cuál se cambie, porque el resultado es el mismo", "La tabla muestra 12 V en F1 y 0 V en L1, así que la lámpara conduce y no es la sospechosa."),
        ("abc", "{F} Un fusible abierto suele indicar que antes pasó más corriente de la que soporta. ¿Qué debe plantear el diagnóstico antes de proponer un fusible nuevo?", "Buscar qué causó el exceso de corriente", "Proponer uno de mayor capacidad para que no se abra", "Proponer retirar el fusible del circuito", "Si se repone sin hallar la causa, el exceso de corriente puede repetirse; un fusible mayor o ausente quita la protección."),
        ("=", "Un fusible de ejemplo se abre si pasan más de 3 A. Una lámpara de 12 V tiene 2 Ω de resistencia. ¿Cuántos amperios circulan por ella?", "12//2", "La corriente se calcula dividiendo la tensión entre la resistencia.", " A"),
        ("abc", "{F} ¿Cuál de estos informes de diagnóstico está mejor redactado?", "Con S1 cerrado, F1 marca 12 V y L1 y S1 marcan 0 V. Causa probable: F1 abierto; falta confirmarlo y buscar el exceso de corriente.", "Parece que algo está malo en la luz de aviso.", "La lámpara está quemada: cambiarla.", "Un buen informe cita los registros, plantea una causa probable y dice qué falta confirmar."),
    ],
    ctx=("abc", "Un cliente de ejemplo dice: «el fusible se abrió, pon uno más grande y listo». Como estudiante, ¿qué respondes?", "Que un fusible mayor quita la protección y que hay que buscar primero qué causó el exceso de corriente", "Que sí, porque así no se vuelve a abrir", "Que mejor se quite el fusible para evitar problemas", "El fusible protege el circuito; cambiar su capacidad o quitarlo sin analizar la causa aumenta el riesgo de incendio."),
    sc=[
        ("En Electrónica: ¿cuánta tensión muestra un elemento abierto en un circuito en serie?", "Toda la tensión de la batería", "El elemento abierto interrumpe el camino y concentra la tensión."),
        ("¿Qué muestran los elementos que conducen cuando otro está abierto?", "0 V entre sus terminales", "Sin corriente no hay caída de tensión en ellos."),
        ("¿Qué debe buscarse tras un fusible abierto?", "Qué causó el exceso de corriente", "Cambiar el fusible sin buscar la causa puede repetir el problema."),
    ],
    op=("Caso de ejemplo: luz de un cartel de 12 V en serie con batería B1, interruptor S1, lámpara L1 y resistor R1. Con S1 cerrado, la tabla de personal autorizado dice: B1 = 12 V; S1 = 12 V; L1 = 0 V; R1 = 0 V. El cartel no enciende. Escribe (a) qué elemento es el sospechoso y por qué, (b) por qué se descartan L1 y R1, (c) una frase de informe de diagnóstico con causa probable y qué falta confirmar.",
        "(a) S1, porque muestra los 12 V completos, lo que indica que interrumpe el camino. (b) L1 y R1 marcan 0 V, es decir, conducen. (c) «Con S1 cerrado, S1 marca 12 V y los demás 0 V: causa probable, S1 abierto o sin contacto; falta confirmarlo con personal autorizado.»",
        ["identifica S1 con la razón de la tensión completa", "explica por qué descarta L1 y R1", "redacta una causa probable con lo que falta confirmar"],
        ["hoja con las tres respuestas"],
        ["decir que L1 está dañada por marcar 0 V", "afirmar una causa como segura", "no citar los registros"],
        "Pregunta: «¿qué valor marcaría L1 si fuera ella la abierta?». Si no responde, pídele que relea la regla del elemento abierto."),
    reinforce="Inventa un registro de cuatro valores para un circuito en serie con un resistor abierto y escribe el informe de diagnóstico.",
    extend="Explica con un ejemplo por qué una tabla de mediciones permite diagnosticar sin cambiar piezas al azar.",
)

# ============================================================ OAE-02, clase 4
F = ("Ficha 4 (caso de ejemplo, inventado; registros de personal autorizado). Un sensor de luz de un alumbrado automático se alimenta con 10 V. Su salida es un divisor de tensión: dos resistores en serie, R1 = 6 kΩ y R2 = 4 kΩ; la salida se toma entre ellos, sobre R2. "
     "Fórmula: salida = tensión de entrada × R2 ÷ (R1 + R2). El controlador funciona con una salida entre 3 V y 5 V. Registros con la alimentación de 10 V presente: caso X = 4 V; caso Y = 10 V; caso Z = 0 V.")
build(
    O2, 4, F,
    use="Aprenderé a diagnosticar con lógica un sistema con control automático simple, calculando el valor esperado de un divisor de tensión y comparando con registros de ejemplo.",
    prior=["Sé la ley de Ohm.", "Sé qué es un circuito en serie.", "Sé comparar un registro con un valor esperado."],
    explain=[
        "Un sistema con control automático decide y actúa según señales que recibe de sensores, sin que una persona lo opere cada vez. Un sensor convierte una magnitud del ambiente, como la luz o la temperatura, en una señal eléctrica. El controlador compara esa señal con un rango que el fabricante considera normal y actúa en consecuencia.",
        "Un divisor de tensión es un par de resistores en serie que reparte la tensión de entrada. La salida se toma entre ambos: salida = entrada × R2 ÷ (R1 + R2). Con 12 V, R1 de 3 kΩ y R2 de 9 kΩ, la salida es 12 × 9 ÷ 12 = 9 V. Si R2 se abre, no circula corriente y la salida sube a la tensión de entrada; si R1 se abre, nada alimenta la salida y baja a 0 V.",
        f"Un diagnóstico escrito sigue un orden: síntoma, valor esperado según el fabricante, registros, comparación, causa probable y recomendación. Nunca se anulan ni se puentean las protecciones de un equipo. {AVISO}",
    ],
    vocab=[("sensor", "componente que convierte una magnitud del ambiente en una señal eléctrica"), ("control automático", "sistema que decide y actúa según señales de sensores sin que una persona lo opere cada vez"), ("controlador", "equipo que compara la señal del sensor con un rango y actúa"), ("divisor de tensión", "par de resistores en serie que reparte la tensión de entrada"), ("rango normal", "intervalo de valores en que el fabricante indica que el equipo funciona bien"), ("puentear", "unir dos puntos para saltarse un componente o una protección")],
    worked=[
        ("Calcular la salida", "Un divisor de ejemplo tiene entrada de 8 V, R1 = 2 kΩ y R2 = 6 kΩ. ¿Qué salida entrega?", ["Se usa entrada × R2 ÷ (R1 + R2).", "8 por 6 son 48; 2 más 6 son 8; 48 dividido en 8 son 6."], "6 V"),
        ("Fuera del rango", "El controlador de ejemplo acepta de 2 V a 4 V y el divisor entrega 7 V. ¿Está en el rango?", ["7 es mayor que 4.", "Queda fuera del rango normal."], "No: está fuera del rango y hay que diagnosticar"),
    ],
    mistakes=[("Puentear el sensor para que el equipo «funcione» aunque marque un valor fuera del rango.", "Se pierde la protección y se oculta la falla.", "Informa el registro fuera de rango y deriva a personal autorizado."),
              ("Afirmar una causa cuando el registro admite otras explicaciones.", "Un mismo registro puede venir de varias fallas.", "Anota la causa como probable y usa datos extra, como la alimentación, para descartar otras.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un divisor de tensión?", "Un par de resistores en serie que reparte la tensión de entrada", "Un par de resistores en paralelo que duplica la corriente", "Un fusible doble para dos circuitos", "El divisor reparte la tensión entre dos resistores en serie y entrega una parte a la salida."),
        ("abc", "En Electrónica: ¿qué es un sensor?", "Un componente que convierte una magnitud del ambiente en una señal eléctrica", "Una batería de respaldo", "Un resistor de potencia", "El sensor traduce luz, temperatura u otra magnitud a una señal que el controlador entiende."),
        ("abc", "En Electrónica: ¿qué significa que un equipo tenga control automático?", "Que decide y actúa según señales de sensores sin ser operado cada vez", "Que funciona sin ninguna fuente de energía", "Que solo trabaja con pilas", "El control automático usa las señales del sensor para actuar por sí solo."),
        ("=", "{F} ¿Cuántos voltios entrega la salida del divisor en funcionamiento normal?", "10*4//(6+4)", "Se aplica salida = entrada × R2 ÷ (R1 + R2) con R1 = 6 y R2 = 4.", " V"),
        ("abc", "{F} ¿Cuál de los tres registros está dentro del rango normal?", "El caso X, con 4 V", "El caso Y, con 10 V", "El caso Z, con 0 V", "El rango normal va de 3 V a 5 V, y solo 4 V cae dentro."),
        ("abc", "{F} En el caso Y, la salida marca 10 V. ¿Cuál es la causa más probable?", "R2 está abierto", "R1 está abierto", "No llega alimentación al divisor", "Si R2 se abre, no circula corriente y la salida sube a la tensión de entrada, 10 V."),
        ("abc", "{F} En el caso Z, la salida marca 0 V con la alimentación presente. ¿Cuál de estas causas lo explica?", "R1 está abierto", "R2 está abierto", "El controlador acepta de 3 V a 5 V, y eso baja la salida", "Con R1 abierto nada alimenta la salida y baja a 0 V; con R2 abierto subiría a 10 V."),
        ("=", "Un divisor de ejemplo tiene entrada de 15 V, R1 = 10 kΩ y R2 = 5 kΩ. ¿Cuántos voltios entrega la salida?", "15*5//(10+5)", "Se aplica salida = entrada × R2 ÷ (R1 + R2).", " V"),
        ("abc", "Un controlador de ejemplo acepta señales entre 3 V y 5 V y el divisor entrega 6 V. ¿Qué corresponde?", "Reconocer que está fuera del rango y diagnosticar la causa", "Considerarlo normal porque 6 V está cerca de 5 V", "Ajustar el rango del controlador a 6 V", "Un valor fuera del rango indica falla o desajuste; no se acomoda el rango para ocultarlo."),
        ("abc", "{F} El personal autorizado repite el registro del caso Y y obtiene otra vez 10 V. ¿Qué indica?", "Que el resultado es consistente y respalda la causa probable", "Que el sensor funciona perfectamente", "Que debe cambiarse R1", "Un registro repetido con el mismo valor da más confianza en el diagnóstico."),
        ("abc", "{F} Para el caso Z, un compañero culpa a R1 y otro dice que no llega alimentación. ¿Qué dato de la ficha ayuda a decidir?", "Que la alimentación de 10 V está presente, lo que descarta la falta de alimentación", "Que R2 vale 4 kΩ", "Que el controlador acepta de 3 V a 5 V", "Si la alimentación está presente, el segundo compañero queda descartado."),
        ("=", "Un divisor de ejemplo tiene entrada de 20 V, R1 = 6 kΩ y R2 = 14 kΩ. ¿Cuántos voltios entrega la salida? (Un controlador de 3 V a 5 V no la aceptaría.)", "20*14//(6+14)", "Se aplica salida = entrada × R2 ÷ (R1 + R2).", " V"),
        ("abc", "¿Cuál es el orden lógico de un diagnóstico escrito?", "Síntoma, valor esperado, registros, comparación, causa probable y recomendación", "Recomendación, causa, registros y, al final, el síntoma", "Causa, precio de la reparación y firma del cliente", "Se parte de lo observado y se compara con lo esperado antes de proponer causa y recomendación."),
    ],
    ctx=("abc", "Un portón automático de ejemplo no cierra porque su sensor de posición entrega 10 V cuando lo normal es entre 3 V y 5 V. El dueño pide: «sáltate el sensor para que cierre igual». ¿Qué corresponde?", "No puentear una protección: informar el registro y derivar a personal autorizado con norma vigente", "Puentear el sensor, porque el dueño lo autoriza", "Cerrar a mano y dejar el sensor así hasta que falle del todo", "Saltarse un sensor elimina la protección del portón y oculta la falla; lo decide personal autorizado."),
    sc=[
        ("En Electrónica: ¿qué hace un sensor?", "Convierte una magnitud del ambiente en una señal eléctrica", "El sensor traduce luz, temperatura u otra magnitud."),
        ("¿Qué se hace con un registro fuera del rango normal?", "Se diagnostica la causa; no se ajusta el rango para ocultarlo", "Un valor fuera de rango indica falla o desajuste."),
        ("¿Por qué no se puentea un sensor de seguridad?", "Porque se pierde la protección y se oculta la falla", "Un sensor puenteado deja el sistema sin protección."),
    ],
    op=("Ficha de ejemplo: un sistema de riego automático usa un sensor de humedad con divisor de tensión: entrada 12 V, R1 = 8 kΩ y R2 = 4 kΩ; el controlador acepta de 3 V a 5 V. Registros de ejemplo con la alimentación de 12 V presente: caso 1 = 4 V; caso 2 = 12 V; caso 3 = 0 V. Escribe (a) la salida esperada, (b) qué caso está dentro del rango, (c) la causa probable del caso 2 con su razón, (d) un orden de informe con las seis partes.",
        "(a) 12 × 4 ÷ (8 + 4) = 4 V. (b) El caso 1, con 4 V. (c) R2 abierto: sin corriente, la salida sube a la tensión de entrada de 12 V. (d) Síntoma, valor esperado, registros, comparación, causa probable y recomendación.",
        ["calcula bien la salida esperada", "identifica el caso en rango", "explica la causa probable con la razón", "ordena las seis partes del informe"],
        ["hoja con el cálculo, la clasificación de casos y el orden del informe"],
        ["calcular mal el divisor", "afirmar la causa como segura", "olvidar el valor esperado en el informe"],
        "Pregunta: «¿qué dato extra te ayudaría a descartar otras causas?». Si no responde, pídele que relea la última regla del diagnóstico."),
    reinforce="Calcula en papel la salida de tres divisores de ejemplo con entradas y resistores a tu elección con resultados enteros.",
    extend="Explica con un ejemplo cómo un registro de ejemplo puede venir de dos causas y qué dato permitiría separarlas.",
)

# ============================================================ OAE-03, clase 1
F = ("Ficha 1 (manual de procedimiento de ejemplo, inventado, resumido por secciones). Procedimiento PR-07 «Módulo de alarma de 9 V»: sección 1, Objetivo; sección 2, Materiales y componentes (lista de 14 ítems); "
     "sección 3, Advertencias (calor, humos, herramientas, energía y electricidad estática); sección 4, Orden de trabajo (7 etapas, cada una con responsable y firma); sección 5, Criterios de aceptación; sección 6, Registro de no conformidades.")
build(
    O3, 1, F,
    use="Aprenderé cómo es el trabajo de ensamblar circuitos básicos, cómo se lee un manual de procedimiento, qué riesgos tiene y qué tareas no me corresponden.",
    prior=["Sé qué es una lista de componentes.", "Sé qué es un esquema.", "Sé leer una ficha con secciones."],
    explain=[
        "Armar o ensamblar un circuito es unir sus componentes siguiendo un manual de procedimiento: el documento de la empresa que fija el objetivo, los materiales, las advertencias, el orden de las etapas y los criterios de aceptación. Un circuito analógico trabaja con señales que varían de forma continua, como el volumen de un parlante. Un circuito digital trabaja con dos niveles, 0 y 1, como un interruptor apagado o encendido. Reparar un circuito, cuando corresponde, también se hace con manual y con autorización.",
        "El trabajo de ensamble tiene riesgos: el calor y los humos de la soldadura, las quemaduras con herramientas, la energía eléctrica y la electricidad estática, que puede dañar componentes sin que la persona lo note. Por eso las advertencias se leen antes de la primera etapa y no son opcionales. Al terminar, el producto se compara con los criterios de aceptación. Un resultado que no los cumple es una no conformidad y se anota en el registro.",
        f"Cada etapa tiene un responsable que firma: así se sabe quién hizo qué. {EMER} {AVISO}",
    ],
    vocab=[("manual de procedimiento", "documento de la empresa con objetivo, materiales, advertencias, etapas y criterios de aceptación"), ("circuito analógico", "circuito con señales que varían de forma continua"), ("circuito digital", "circuito con dos niveles de señal, 0 y 1"), ("criterio de aceptación", "condición que el producto debe cumplir para aprobarse"), ("no conformidad", "resultado que no cumple un criterio de aceptación"), ("electricidad estática", "carga que se acumula en el cuerpo o en objetos y puede dañar componentes")],
    worked=[
        ("Ubicar una sección", "Un manual de ejemplo tiene secciones numeradas: objetivo, materiales, advertencias, etapas, aceptación y registro de no conformidades. ¿En qué sección se anota que una pieza no pasó la inspección?", ["La pieza que no cumple es una no conformidad.", "Las no conformidades tienen su propia sección, la de registro."], "En la sección de registro de no conformidades"),
        ("Contar firmas", "Un procedimiento de ejemplo tiene 5 etapas y cada una lleva una firma. Se fabrican 3 módulos. ¿Cuántas firmas se necesitan?", ["Cada módulo necesita 5 firmas.", "5 por 3 son 15."], "15 firmas"),
    ],
    mistakes=[("Pensar que las advertencias del manual son opcionales si el trabajo es corto.", "Los riesgos existen aunque el trabajo dure poco.", "Lee las advertencias antes de la primera etapa."),
              ("Aceptar un módulo que no cumple un criterio «porque casi lo cumple».", "Un criterio se cumple o no se cumple.", "Anota una no conformidad y deriva al responsable.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un manual de procedimiento?", "El documento de la empresa que fija objetivo, etapas, advertencias y criterios de aceptación", "Una lista de precios de los componentes", "Un esquema sin ningún texto", "El manual de procedimiento ordena el trabajo; la lista de precios y el esquema cumplen otras funciones."),
        ("abc", "En Electrónica: ¿qué es una no conformidad?", "Un resultado que no cumple un criterio de aceptación", "Una pieza más cara que las demás", "Una etapa del manual de procedimiento", "La no conformidad es el incumplimiento de un criterio y se registra."),
        ("abc", "En Electrónica: ¿en qué se diferencia un circuito analógico de uno digital?", "El analógico usa señales continuas y el digital usa dos niveles, 0 y 1", "El analógico usa dos niveles y el digital usa señales continuas", "El digital siempre usa más tensión que el analógico", "La señal analógica varía de forma continua; la digital solo toma 0 o 1."),
        ("abc", "{F} ¿En qué sección buscarías qué debe cumplir el módulo para aprobarse?", "En la sección 5, Criterios de aceptación", "En la sección 2, Materiales y componentes", "En la sección 3, Advertencias", "Los criterios de aceptación dicen cuándo el producto se aprueba."),
        ("abc", "{F} ¿En qué sección buscarías los riesgos de calor y de herramientas?", "En la sección 3, Advertencias", "En la sección 6, Registro de no conformidades", "En la sección 1, Objetivo", "Las advertencias reúnen los riesgos que se deben conocer antes de trabajar."),
        ("abc", "{F} La sección 3 menciona la electricidad estática. ¿Qué tipo de riesgo es?", "Un riesgo para los componentes, que puede dañarlos aunque la persona no lo note", "Un riesgo solo para la persona, sin efecto en los componentes", "No es un riesgo", "La electricidad estática puede estropear componentes sin señales visibles."),
        ("=", "{F} Si cada etapa de la sección 4 lleva una firma y se fabrican 5 módulos, ¿cuántas firmas se necesitan en total?", "7*5", "Las etapas por módulo se multiplican por los 5 módulos.", " firmas"),
        ("abc", "{F} Una etapa del módulo no cumple un criterio de aceptación. ¿Dónde se deja constancia?", "En la sección 6, Registro de no conformidades", "En la sección 1, Objetivo", "En la sección 2, Materiales y componentes", "El incumplimiento se anota en el registro de no conformidades."),
        ("=", "{F} La sección 2 pide 14 ítems por módulo. Para 6 módulos, ¿cuántos ítems se necesitan en total?", "14*6", "Los ítems por módulo se multiplican por la cantidad de módulos.", " ítems"),
        ("abc", "{F} Un compañero propone saltarse una etapa porque «ya sé lo que viene». ¿Qué corresponde?", "Seguir el orden del manual y consultar al supervisor si cree que la etapa sobra", "Saltarla, porque conoce el trabajo", "Saltarla y firmarla igual", "El orden del manual se respeta; solo quien autoriza el procedimiento puede cambiarlo."),
        ("ab", "Un estudiante terminó este cuaderno y quiere soldar un módulo en su casa. ¿Qué corresponde?", "No hacerlo: la soldadura requiere docente de la especialidad y norma vigente, y el cuaderno no habilita", "Hacerlo con un soldador de poca potencia, porque ya conoce el manual", "La soldadura implica calor, humos y quemaduras, por lo que se aprende con docente y norma vigente."),
        ("abc", "{F} En una etapa, el responsable no firmó. ¿Qué debe hacer quien revisa el módulo?", "Registrar la etapa como no conformidad hasta que el responsable la firme o explique", "Firmar en su lugar para ahorrar tiempo", "Ignorar la firma si el resultado se ve bien", "La firma deja constancia de quién hizo la etapa; sin ella no se puede dar por cumplida."),
        ("abc", "Una compañera se quema la mano con una herramienta caliente en el taller. ¿Qué corresponde de forma general?", "Avisar de inmediato al docente o a un adulto responsable y a emergencias si hace falta", "Esperar a terminar el trabajo antes de avisar", "Ponerle cualquier crema que haya a mano", "Ante una quemadura se avisa a un adulto responsable y a emergencias; no se improvisan remedios."),
    ],
    ctx=("abc", "Un manual de ejemplo trae la advertencia «usar protección ocular y ventilación». Un estudiante dice que las advertencias son opcionales para trabajos cortos. ¿Qué respondes?", "Que las advertencias son obligatorias y se leen antes de la primera etapa", "Que son opcionales si el trabajo dura menos de una hora", "Que son solo para principiantes", "Los riesgos no dependen de la duración ni de la experiencia; las advertencias del manual se cumplen siempre."),
    sc=[
        ("En Electrónica: ¿qué dice el criterio de aceptación de un manual?", "Qué condición debe cumplir el producto para aprobarse", "El criterio de aceptación fija cuándo el producto está aprobado."),
        ("¿Qué se hace con un resultado que no cumple un criterio?", "Se anota como no conformidad en el registro", "El incumplimiento queda registrado para corregirlo."),
        ("¿Quién enseña a soldar y a usar herramientas de forma segura?", "Un docente de la especialidad, con norma vigente", "Este cuaderno no habilita para soldar ni usar herramientas."),
    ],
    op=("Ficha de ejemplo: manual PR-12 «Cargador de pilas de 6 V»: Objetivo; Materiales (9 ítems); Advertencias (calor, herramientas, energía); Orden de trabajo (4 etapas con firma); Criterios de aceptación; Registro de no conformidades. Se fabrican 8 cargadores en un taller de ejemplo. Escribe (a) en qué sección buscarías cuándo se aprueba un cargador, (b) cuántas firmas se necesitan, (c) qué anotarías si una etapa no cumple, (d) una tarea que no harías tú y quién la haría.",
        "(a) En Criterios de aceptación. (b) 4 por 8 son 32 firmas. (c) Una no conformidad en el Registro, indicando la etapa y el criterio que no se cumplió. (d) Soldar o usar herramientas con calor: lo haría el docente de la especialidad o personal autorizado con norma vigente.",
        ["ubica bien la sección", "calcula bien las firmas", "describe bien la no conformidad", "reconoce una tarea que no le corresponde"],
        ["hoja con las cuatro respuestas"],
        ["decir que ya puede soldar", "no multiplicar por los módulos", "no registrar la no conformidad"],
        "Pregunta: «¿qué dato anotarías para que otra persona entienda la no conformidad?». Si no responde, pídele que relea la sección sobre registro."),
    reinforce="Inventa un manual de procedimiento de seis secciones para un timbre de 6 V y escribe qué dice cada sección en una línea.",
    extend="Explica con un ejemplo por qué la firma de cada etapa ayuda a encontrar el origen de un error.",
)

# ============================================================ OAE-03, clase 2
F = ("Ficha 2 (lista de componentes y conexiones de ejemplo, inventada). Módulo «luz intermitente de 9 V». Componentes: R1, resistor de 1 kΩ (sin polaridad); C1, condensador electrolítico de 100 µF (con polaridad: terminal + y terminal −); "
     "D1, diodo (deja pasar la corriente en un solo sentido, del ánodo al cátodo); LED1, diodo emisor de luz (con polaridad: ánodo y cátodo). "
     "Conexiones: nodo 1 = terminal positivo (+) de la batería, ánodo de D1 y terminal + de C1; nodo 2 = cátodo de D1 y un extremo de R1; nodo 3 = el otro extremo de R1 y ánodo de LED1; "
     "nodo 4 = cátodo de LED1, terminal − de C1 y terminal negativo (−) de la batería.")
build(
    O3, 2, F,
    use="Aprenderé a reconocer en papel los componentes básicos, su polaridad y sus valores, y a revisar una lista de conexiones para detectar errores antes del ensamble.",
    prior=["Sé qué es un nodo.", "Sé qué es la tolerancia de un resistor.", "Sé sumar y convertir unidades sencillas."],
    explain=[
        "El resistor limita la corriente y no tiene polaridad: puede conectarse en cualquier sentido. El condensador almacena energía eléctrica y la entrega después; su capacidad se mide en microfaradios (µF), y 1 µF son 1000 nanofaradios (nF). Los condensadores electrolíticos tienen polaridad: el terminal + y el − no se pueden invertir. Dos condensadores en paralelo tienen una capacidad total igual a la suma de sus capacidades.",
        "El diodo deja pasar la corriente en un solo sentido, del ánodo al cátodo. El LED es un diodo que emite luz y también tiene polaridad. Un error de polaridad, como un diodo o un condensador invertido, puede impedir el funcionamiento o dañar el componente. Por eso, antes del ensamble se revisa la lista de conexiones contra el esquema y se confirma en la hoja de datos qué marca cada terminal.",
        f"Un condensador puede conservar energía aunque el equipo ya se haya desconectado, por lo que su manejo es de personal autorizado. {AVISO}",
    ],
    vocab=[("condensador", "componente que almacena energía eléctrica y la entrega después"), ("microfaradio (µF)", "unidad de capacidad de un condensador; 1 µF son 1000 nF"), ("diodo", "componente que deja pasar la corriente en un solo sentido"), ("ánodo", "terminal por donde entra la corriente en un diodo"), ("cátodo", "terminal por donde sale la corriente en un diodo"), ("LED", "diodo que emite luz y tiene polaridad"), ("polaridad invertida", "error de conectar al revés un componente con polaridad")],
    worked=[
        ("Componentes con polaridad", "Una lista de ejemplo incluye un resistor, un condensador electrolítico y un diodo. ¿Cuáles tienen polaridad?", ["El resistor se puede conectar en cualquier sentido.", "El condensador electrolítico y el diodo tienen un sentido correcto."], "El condensador electrolítico y el diodo"),
        ("Capacidad en paralelo", "Dos condensadores de ejemplo, de 33 µF y 47 µF, se conectan en paralelo. ¿Qué capacidad total tienen?", ["En paralelo las capacidades se suman.", "33 más 47 son 80."], "80 µF"),
    ],
    mistakes=[("Suponer que la banda de un condensador marca el terminal positivo sin mirar la hoja de datos.", "Cada fabricante puede marcar los terminales de forma distinta.", "Confirma en la hoja de datos qué terminal marca la banda."),
              ("Pensar que un condensador desconectado está descargado y es seguro tocarlo.", "Puede conservar energía un tiempo.", "Su manejo es de personal autorizado y con norma vigente.")],
    T=[
        ("abc", "En Electrónica: ¿qué es un condensador?", "Un componente que almacena energía eléctrica y la entrega después", "Un componente que limita la corriente", "Un componente que se abre si pasa demasiada corriente", "El condensador almacena energía; limitar corriente es función del resistor y abrirse es función del fusible."),
        ("abc", "En Electrónica: ¿qué hace un diodo?", "Deja pasar la corriente en un solo sentido", "Aumenta la tensión de la batería", "Guarda la energía para después", "La función del diodo es permitir el paso de la corriente en un solo sentido."),
        ("abc", "¿Cuál de estos componentes no tiene polaridad?", "El resistor", "El condensador electrolítico", "El LED", "El resistor se conecta en cualquier sentido; el electrolítico y el LED tienen terminales + y − o ánodo y cátodo."),
        ("abc", "{F} ¿Qué terminal de LED1 se une a R1?", "El ánodo", "El cátodo", "Ninguno de los dos", "El nodo 3 une el otro extremo de R1 con el ánodo de LED1."),
        ("abc", "{F} ¿Cuál de estas listas describe el nodo 4?", "Cátodo de LED1, terminal − de C1 y terminal negativo de la batería", "Ánodo de D1, terminal + de C1 y terminal positivo de la batería", "Cátodo de D1 y un extremo de R1", "El nodo 4 reúne los terminales negativos y el cátodo del LED, según la ficha."),
        ("abc", "{F} Un revisor ve que el terminal + de C1 está unido al nodo 4 en vez de al nodo 1. ¿Qué tipo de error es?", "Un error de polaridad: el condensador está invertido y podría dañarse", "Un error de valor: C1 debería tener otra capacidad", "No es un error, porque el condensador funciona en cualquier sentido", "C1 es electrolítico y tiene polaridad; invertirlo es un error que puede dañarlo."),
        ("=", "Dos condensadores de ejemplo, de 100 µF y 220 µF, se conectan en paralelo. ¿Qué capacidad total tienen?", "100+220", "En paralelo las capacidades se suman.", " µF"),
        ("=", "Un condensador de ejemplo es de 2 µF. ¿Cuántos nanofaradios son?", "2*1000", "Cada microfaradio equivale a 1000 nanofaradios.", " nF"),
        ("abc", "{F} ¿Qué pasaría si se invirtiera D1?", "Bloquearía el paso de la corriente que viene del terminal + de la batería hacia R1", "La luz sería más intensa", "No cambiaría nada, porque los diodos no tienen sentido", "El diodo solo deja pasar del ánodo al cátodo; invertido, bloquea ese paso."),
        ("abc", "{F} La lista pide R1 de 1 kΩ. En la bodega hay uno de 10 kΩ y uno de 1 kΩ, y un compañero dice que da igual cuál se use. ¿Qué corresponde?", "No da igual: se usa el valor de la lista, 1 kΩ", "Da igual, porque los dos son resistores", "Se usa el de 10 kΩ, porque limita más", "El valor del resistor determina la corriente; el cambio exige autorización del proyectista."),
        ("abc", "{F} C1 estuvo conectado a una batería. ¿Qué regla general corresponde para su manejo?", "Puede conservar energía aunque se haya desconectado, por lo que lo maneja personal autorizado", "Al desconectar la batería queda totalmente descargado", "Solo es riesgoso si es muy pequeño", "Un condensador puede mantener carga; su manejo exige personal autorizado y norma vigente."),
        ("=", "Un lote de ejemplo incluye 25 resistores a $20, 10 condensadores a $150 y 10 diodos a $60. ¿Cuánto cuesta el lote?", "25*20+10*150+10*60", "Se suma el costo de cada tipo de componente.", " pesos"),
        ("abc", "{F} El control de calidad de otro módulo de ejemplo trae la línea «C2: 10 µF, con polaridad». ¿Qué debe confirmar al revisar el módulo?", "Que el terminal + de C2 esté unido donde el esquema indica", "Que C2 tenga el mismo color que C1", "Solo que C2 esté en la bolsa de componentes", "Un componente polarizado debe estar en el sentido que indica el esquema."),
    ],
    ctx=("abc", "Una compañera ve un condensador con una banda en un lado y supone que la banda marca el terminal positivo, sin mirar la hoja de datos. ¿Qué corresponde?", "Confirmar en la hoja de datos del fabricante qué terminal marca la banda", "Confiar en la intuición, porque casi siempre acierta", "Probar los dos sentidos hasta que funcione", "Los fabricantes pueden marcar distinto; la hoja de datos resuelve la duda sin riesgo."),
    sc=[
        ("En Electrónica: ¿qué componentes del taller tienen polaridad?", "El condensador electrolítico, el diodo y el LED", "Esos componentes solo funcionan bien en un sentido."),
        ("¿Cómo se calcula la capacidad de dos condensadores en paralelo?", "Sumando sus capacidades", "En paralelo las capacidades se suman."),
        ("¿Quién maneja un condensador que estuvo conectado?", "Personal autorizado, con norma vigente", "Puede conservar energía aunque se haya desconectado."),
    ],
    op=("Ficha de ejemplo: módulo «aviso sonoro de 9 V». Componentes: R1 de 2200 Ω; C1 electrolítico de 47 µF (terminales + y −); D1 diodo (ánodo y cátodo); B1 batería de 9 V. Conexiones: nodo 1 = terminal + de B1, ánodo de D1 y terminal − de C1; nodo 2 = cátodo de D1 y R1; nodo 3 = el otro extremo de R1, el terminal + de C1 y el terminal − de B1. Escribe (a) qué componentes tienen polaridad, (b) qué error ves en el nodo 1 y por qué, (c) qué capacidad total habría si se añadiera en paralelo un condensador de 22 µF, (d) quién manejaría C1 si estuvo conectado.",
        "(a) C1, D1 y B1. (b) El terminal − de C1 está en el nodo 1, junto al terminal + de B1 (y su terminal + junto al − de la batería): C1 está con polaridad invertida. (c) 47 más 22 son 69 µF. (d) Personal autorizado con norma vigente, porque puede conservar energía.",
        ["identifica los componentes con polaridad", "detecta el error de polaridad con razón", "suma bien las capacidades", "nombra quién maneja un condensador"],
        ["hoja con las cuatro respuestas"],
        ["omitir la batería entre los polarizados", "no detectar el error del nodo 1", "sumar mal"],
        "Pregunta: «¿qué esperarías que pasara con un condensador invertido?». Si no responde, pídele que relea la parte de polaridad invertida."),
    reinforce="Escribe una lista de cinco componentes inventados, indica cuáles tienen polaridad y por qué.",
    extend="Explica con un ejemplo por qué es importante confirmar la polaridad en la hoja de datos y no suponerla.",
)

# ============================================================ OAE-03, clase 3
F = ("Ficha 3 (cálculo de ejemplo, inventado). Alimentación de 12 V. Un LED de ejemplo cae 2 V cuando conduce y debe recibir 10 mA (miliamperios). "
     "Regla: resistor limitador = (tensión de la fuente − caída del LED) ÷ corriente; con voltios y miliamperios el resultado sale en kΩ, y 1 kΩ son 1000 Ω. "
     "Resistores en la bodega de ejemplo: 470 Ω, 1000 Ω y 2200 Ω. En serie las resistencias se suman; dos resistores iguales en paralelo dan la mitad de uno; dos distintos en paralelo dan (R1 × R2) ÷ (R1 + R2).")
build(
    O3, 3, F,
    use="Aprenderé a calcular en papel el resistor limitador de un LED y la resistencia de combinaciones en serie y en paralelo, y a detectar errores en una lista de conexiones.",
    prior=["Sé la ley de Ohm.", "Sé qué es un LED y su polaridad.", "Sé sumar, multiplicar y dividir números enteros."],
    explain=[
        "Un LED se daña si pasa por él demasiada corriente. Por eso se conecta en serie con un resistor limitador. Cuando el LED conduce, su tensión cae un valor fijo; el resto de la tensión de la fuente queda en el resistor. Con la ley de Ohm, el resistor se calcula como la tensión que sobra dividida por la corriente que debe recibir el LED. Con voltios y miliamperios el resultado sale en kΩ.",
        "Las resistencias se combinan de dos maneras. En serie se suman: tres resistores de 100 Ω dan 300 Ω. En paralelo la resistencia total es menor que la de cada resistor: dos resistores iguales dan la mitad de uno, y dos distintos dan (R1 × R2) ÷ (R1 + R2). Combinar resistores sirve para obtener un valor que no está en la bodega. Una lista de conexiones se revisa buscando errores de polaridad, de valor o de unión.",
        f"Todo es cálculo en papel con tensiones bajas de ejemplo: nunca se prueba un circuito sin personal autorizado. {AVISO}",
    ],
    vocab=[("resistor limitador", "resistor en serie con un LED que limita su corriente"), ("caída de tensión", "tensión que se queda en un componente cuando conduce"), ("en serie", "uno a continuación del otro, con un solo camino"), ("en paralelo", "varios caminos que parten y llegan a los mismos puntos"), ("miliamperio (mA)", "milésima de amperio")],
    worked=[
        ("Resistor limitador", "Una fuente de ejemplo de 11 V alimenta un LED que cae 2 V y debe recibir 3 mA. ¿Qué resistor limitador necesita?", ["Sobran 11 menos 2, es decir 9 V.", "9 V dividido en 3 mA son 3 kΩ, es decir 3000 Ω."], "3000 Ω"),
        ("Dos en paralelo", "Dos resistores de ejemplo de 12 Ω y 4 Ω están en paralelo. ¿Qué resistencia total tienen?", ["Se usa (R1 × R2) ÷ (R1 + R2).", "12 por 4 son 48 y 12 más 4 son 16; 48 dividido en 16 son 3."], "3 Ω"),
    ],
    mistakes=[("Calcular el resistor limitador dividiendo toda la tensión de la fuente entre la corriente.", "Una parte de la tensión queda en el LED.", "Resta primero la caída del LED y luego divide."),
              ("Sumar las resistencias de dos resistores en paralelo como si estuvieran en serie.", "En paralelo el total es menor que cada resistor.", "Usa la mitad si son iguales o (R1 × R2) ÷ (R1 + R2) si son distintos.")],
    T=[
        ("abc", "En Electrónica: ¿para qué se conecta un resistor limitador en serie con un LED?", "Para limitar la corriente y no dañar el LED", "Para que el LED cambie de color", "Para guardar energía y devolverla después", "Sin el limitador, la corriente puede ser excesiva y dañar el LED."),
        ("abc", "En Electrónica: ¿qué pasa con la resistencia total al poner resistores en serie?", "Se suma", "Queda igual a la del mayor", "Se reduce a la mitad", "En serie las resistencias se suman."),
        ("abc", "En Electrónica: ¿cómo es la resistencia total de dos resistores iguales en paralelo?", "La mitad de la de uno", "El doble de la de uno", "Igual a la de uno", "En paralelo el total es menor; con dos iguales queda la mitad."),
        ("=", "{F} ¿Qué valor de resistor limitador, en ohmios, necesita el LED de la ficha?", "(12-2)*1000//10", "Se resta la caída del LED a la fuente, se divide por los mA y se pasa de kΩ a Ω.", " Ω"),
        ("abc", "{F} ¿Cuál de los resistores de la bodega sirve para el LED de la ficha?", "El de 1000 Ω", "El de 470 Ω", "El de 2200 Ω", "El cálculo da 1000 Ω; con 470 Ω pasaría demasiada corriente y con 2200 Ω, muy poca."),
        ("=", "Tres resistores de ejemplo de 100 Ω, 220 Ω y 330 Ω están en serie. ¿Qué resistencia total tienen?", "100+220+330", "En serie las resistencias se suman.", " Ω"),
        ("=", "Dos resistores de ejemplo de 6 Ω y 3 Ω están en paralelo. ¿Qué resistencia total tienen?", "6*3//(6+3)", "Se usa (R1 × R2) ÷ (R1 + R2) para dos resistores distintos.", " Ω"),
        ("=", "Una fuente de ejemplo de 9 V alimenta un LED que cae 2 V y debe recibir 4 mA. ¿Qué resistor limitador, en ohmios, necesita?", "(9-2)*1000//4", "Se resta la caída del LED, se divide por los mA y se pasa de kΩ a Ω.", " Ω"),
        ("abc", "{F} Si se usara el resistor de 470 Ω en lugar del de 1000 Ω, ¿qué pasaría con la corriente respecto de los 10 mA previstos?", "Aumentaría más del doble y podría dañar el LED", "Disminuiría y el LED se apagaría", "Quedaría igual", "Con menos resistencia y la misma tensión, la corriente aumenta; 470 Ω es menos de la mitad de 1000 Ω."),
        ("abc", "Un compañero dice que dos resistores de 20 Ω en paralelo dan 40 Ω. ¿Cuál es el error?", "Los sumó como si estuvieran en serie; en paralelo el total es 10 Ω", "Debió multiplicarlos para obtener 400 Ω", "Ninguno: en paralelo se suman", "En paralelo el total es menor que cada resistor; dos iguales dan la mitad."),
        ("=", "Un diseño de ejemplo necesita 1500 Ω y la bodega solo tiene resistores de 500 Ω. ¿Cuántos resistores se deben conectar en serie?", "1500//500", "La resistencia pedida se divide por el valor de cada resistor.", " resistores"),
        ("abc", "Una lista de conexiones de ejemplo dice: el ánodo de LED1 se une al terminal − de la batería, el cátodo de LED1 se une a R1, y R1 se une al terminal + de la batería. ¿Qué error tiene?", "El LED está con la polaridad invertida", "Falta un segundo resistor", "R1 debería ir en paralelo con la batería", "El ánodo debe ir hacia el lado positivo; aquí queda hacia el negativo."),
        ("=", "Un diseño de ejemplo usa un resistor de 1000 Ω en serie con dos resistores de 1000 Ω en paralelo. ¿Qué resistencia total tiene?", "1000+1000//2", "Los dos en paralelo dan la mitad de 1000 Ω y se suman al resistor en serie.", " Ω"),
    ],
    ctx=("abc", "Una técnica de ejemplo necesita 3 Ω y solo tiene resistores de 6 Ω. ¿Cómo puede lograrlo en papel?", "Conectando dos de 6 Ω en paralelo", "Conectando dos de 6 Ω en serie", "Conectando uno solo de 6 Ω", "Dos resistores iguales en paralelo dan la mitad de uno, es decir 3 Ω."),
    sc=[
        ("En Electrónica: ¿cómo se calcula el resistor limitador de un LED?", "Restando la caída del LED a la fuente y dividiendo por la corriente", "La tensión que sobra queda en el resistor."),
        ("¿Cómo es la resistencia total de dos resistores distintos en paralelo?", "Menor que la de cada uno", "En paralelo hay más caminos y el total baja."),
        ("¿Qué se revisa en una lista de conexiones antes del ensamble?", "Errores de polaridad, de valor y de unión", "Esos errores impiden el funcionamiento o dañan componentes."),
    ],
    op=("Ficha de ejemplo: fuente de 12 V; LED que cae 2 V y debe recibir 5 mA; resistores de bodega de 1000 Ω, 2000 Ω y 3300 Ω. Escribe (a) el resistor limitador que se necesita, (b) si alguno de la bodega lo da directamente, (c) cómo lograrlo con dos resistores de la bodega, indicando si van en serie o en paralelo, (d) un error de polaridad posible al revisar la lista de conexiones.",
        "(a) (12 − 2) ÷ 5 = 2 kΩ, es decir 2000 Ω. (b) Sí, el de 2000 Ω. (c) Dos de 1000 Ω en serie dan 2000 Ω. (d) LED1 con el ánodo hacia el terminal negativo de la batería.",
        ["calcula bien el resistor", "elige el resistor correcto", "arma bien la combinación en serie", "describe un error de polaridad"],
        ["hoja con los cálculos y las respuestas"],
        ["no restar la caída del LED", "confundir serie y paralelo", "no mencionar la polaridad"],
        "Pregunta: «¿qué pasaría con un resistor de 1000 Ω?». Si no responde, pídele que relea qué ocurre con la corriente si baja la resistencia."),
    reinforce="Calcula en papel tres resistores limitadores de ejemplo con fuente de 12 V, caída de 2 V y corrientes de 5, 10 y 20 mA.",
    extend="Explica con un ejemplo por qué se puede obtener un mismo valor de resistencia con combinaciones distintas.",
)

# ============================================================ OAE-03, clase 4
F = ("Ficha 4 (alarma de ejemplo, inventada). Sensor A: puerta (1 = abierta, 0 = cerrada). Sensor B: ventana (1 = abierta, 0 = cerrada). Interruptor E: 1 = alarma activada, 0 = desactivada. "
     "La sirena suena (1) solo si E vale 1 y al menos uno de A o B vale 1. Compuertas: NOT invierte la entrada; AND da 1 solo si todas sus entradas valen 1; OR da 1 si al menos una entrada vale 1. "
     "Números binarios: de derecha a izquierda cada cifra vale 1, 2, 4, 8…")
build(
    O3, 4, F,
    use="Aprenderé el lenguaje de los circuitos digitales: compuertas, tablas de verdad y números binarios, y cómo se verifica en papel que un circuito cumple su criterio.",
    prior=["Sé qué es un circuito digital.", "Sé sumar y multiplicar números pequeños.", "Sé qué es un criterio de aceptación."],
    explain=[
        "Una señal digital solo toma dos valores: 0 y 1. Una compuerta lógica es un circuito que combina entradas digitales y entrega una salida. La compuerta NOT invierte la entrada: si entra 1, sale 0. La compuerta AND entrega 1 solo si todas sus entradas valen 1. La compuerta OR entrega 1 si al menos una entrada vale 1. La tabla de verdad enumera todas las combinaciones de entradas y la salida que corresponde a cada una.",
        "Los números binarios usan solo 0 y 1. De derecha a izquierda, cada cifra vale 1, 2, 4, 8, y así sucesivamente. Por eso 101 es 4 + 0 + 1, es decir 5. Con n entradas digitales hay 2 elevado a n combinaciones: con dos entradas hay 4, y con tres, 8. Para verificar un circuito en papel se comparan los casos de su tabla de verdad con los criterios de aceptación.",
        f"Si algún caso falla, se anota una no conformidad y no se acepta el módulo. Este cuaderno solo trabaja en papel. {AVISO}",
    ],
    vocab=[("señal digital", "señal que solo toma los valores 0 y 1"), ("compuerta lógica", "circuito que combina entradas digitales y entrega una salida"), ("AND", "compuerta que da 1 solo si todas sus entradas valen 1"), ("OR", "compuerta que da 1 si al menos una entrada vale 1"), ("NOT", "compuerta que invierte la entrada"), ("tabla de verdad", "lista de todas las combinaciones de entradas con su salida"), ("binario", "sistema de numeración que usa solo 0 y 1")],
    worked=[
        ("Leer una compuerta", "Una compuerta OR de ejemplo recibe las entradas 0 y 1. ¿Qué salida entrega?", ["OR da 1 si al menos una entrada vale 1.", "Una de las entradas vale 1."], "1"),
        ("Convertir un binario", "El número binario 1001 de ejemplo, ¿cuánto vale en decimal?", ["De derecha a izquierda las cifras valen 1, 2, 4 y 8.", "Hay un 1 en el lugar del 1 y otro en el del 8: 1 más 8."], "9"),
    ],
    mistakes=[("Confundir OR con AND y esperar 1 solo si todas las entradas valen 1.", "OR da 1 si al menos una entrada vale 1.", "Repasa la tabla de verdad de cada compuerta."),
              ("Leer el binario 1011 como «mil once».", "Los números binarios usan lugares que valen 1, 2, 4, 8…", "Suma los valores de los lugares donde hay un 1.")],
    T=[
        ("abc", "En Electrónica: ¿qué es una señal digital?", "Una señal que solo toma los valores 0 y 1", "Una señal que varía de forma continua", "Una señal que solo existe con baterías", "La señal digital toma dos niveles; la que varía de forma continua es la analógica."),
        ("abc", "En Electrónica: ¿cuándo entrega 1 una compuerta AND?", "Cuando todas sus entradas valen 1", "Cuando al menos una entrada vale 1", "Cuando todas sus entradas valen 0", "AND exige que todas las entradas valgan 1."),
        ("abc", "En Electrónica: ¿qué hace una compuerta NOT?", "Invierte la entrada: si entra 1, sale 0", "Suma las dos entradas", "Deja pasar la entrada sin cambios", "NOT invierte el valor de la entrada."),
        ("abc", "{F} Con E = 1, A = 0 y B = 1, ¿suena la sirena?", "Sí, porque E vale 1 y la ventana B está abierta", "No, porque la puerta A está cerrada", "No, porque solo suena si A y B valen 1", "La regla pide E = 1 y al menos uno de A o B igual a 1, y B vale 1."),
        ("abc", "{F} Con E = 0, A = 1 y B = 1, ¿suena la sirena?", "No, porque la alarma está desactivada", "Sí, porque la puerta y la ventana están abiertas", "Sí, porque A y B valen 1", "La sirena exige E = 1; con E = 0 no suena aunque haya sensores abiertos."),
        ("ab", "Una compuerta AND de ejemplo recibe las entradas 1 y 0. ¿Qué salida entrega?", "0", "1", "AND da 1 solo si todas valen 1, y una de las entradas vale 0."),
        ("=", "El número binario 1101 de ejemplo, ¿cuánto vale en decimal?", "1*8+1*4+0*2+1*1", "Se suman los valores de los lugares donde hay un 1.", ""),
        ("=", "El número binario 0110 de ejemplo, ¿cuánto vale en decimal?", "0*8+1*4+1*2+0*1", "Se suman los valores de los lugares donde hay un 1.", ""),
        ("=", "{F} ¿Cuántas combinaciones distintas de valores de A, B y E hay?", "2*2*2", "Cada entrada tiene dos valores posibles y se multiplican las posibilidades.", " combinaciones"),
        ("abc", "{F} Un técnico dice: «si A = 1 y E = 0, la sirena debe sonar porque la puerta está abierta». ¿Es correcto según la ficha?", "No: con E = 0 la alarma está desactivada y no suena", "Sí: una puerta abierta siempre hace sonar la sirena", "Sí: porque A vale 1", "La regla exige E = 1; sin ella los sensores no activan la sirena."),
        ("abc", "Ana dice que el binario 1110 vale catorce y Bruno dice que vale mil ciento diez. ¿Quién tiene razón?", "Ana, porque 8 + 4 + 2 es 14", "Bruno, porque se lee cifra por cifra", "Ninguno, porque faltan datos", "Los lugares valen 8, 4, 2 y 1; con unos en 8, 4 y 2 se suma catorce."),
        ("abc", "{F} Se agrega un sensor C (garaje) que también debe activar la sirena. ¿Cómo cambia la regla?", "Suena si E vale 1 y al menos uno de A, B o C vale 1", "Suena si E vale 1 y los tres, A, B y C, valen 1", "Suena si E vale 0 y alguno vale 1", "El nuevo sensor se suma a los otros dentro de la condición OR, que sigue combinándose con E mediante AND."),
        ("abc", "Un módulo digital de ejemplo se revisa con 4 casos de su tabla de verdad y falla en 1. ¿Qué corresponde?", "Registrar una no conformidad con el caso que falló y no aceptar el módulo", "Aceptarlo, porque 3 de 4 casos están bien", "Cambiar el criterio para que el caso que falló sea válido", "Un criterio de aceptación se cumple en todos los casos; el que falla se registra y se devuelve."),
    ],
    ctx=("abc", "Un técnico de ejemplo recibe una tarjeta digital y un manual cuyo criterio de aceptación dice que con E = 1, A = 0 y B = 0 la sirena debe valer 0. La tarjeta entrega 1. ¿Qué corresponde?", "Registrar una no conformidad y devolver la tarjeta para revisión", "Aceptarla, porque casi todos los casos coinciden", "Cambiar el criterio del manual para que la tarjeta pase", "El producto no cumple el criterio; el manual no se cambia por cuenta propia."),
    sc=[
        ("En Electrónica: ¿qué muestra una tabla de verdad?", "Todas las combinaciones de entradas con su salida", "Permite comparar cada caso con el criterio."),
        ("¿Cuánto vale el binario 111 en decimal?", "7", "Los lugares del 4, el 2 y el 1 suman siete."),
        ("¿Qué se hace si un caso de la tabla falla en la verificación?", "Se registra una no conformidad", "El criterio debe cumplirse en todos los casos."),
    ],
    op=("Ficha de ejemplo: luz automática de un pasillo. Sensor P: presencia (1 = hay alguien); sensor O: oscuridad (1 = está oscuro); interruptor M: modo automático (1 = activado). La luz se enciende (1) solo si M vale 1, P vale 1 y O vale 1. Escribe (a) qué compuerta usarías para combinar P, O y M, (b) cuántas combinaciones tiene la tabla, (c) la salida para M = 1, P = 1, O = 0, (d) qué anotarías si una prueba de personal autorizado diera 1 para M = 0, P = 1, O = 1.",
        "(a) Una compuerta AND de tres entradas. (b) 2 por 2 por 2 son 8 combinaciones. (c) 0, porque O vale 0 y AND exige todas en 1. (d) Una no conformidad: con M = 0 la luz debe valer 0.",
        ["elige la compuerta AND", "calcula las combinaciones", "aplica bien la regla", "registra la no conformidad"],
        ["hoja con las cuatro respuestas"],
        ["usar OR en lugar de AND", "calcular mal las combinaciones", "no anotar la no conformidad"],
        "Pregunta: «¿qué pasa si basta con que una entrada valga 1?». Si no responde, pídele que compare AND con OR."),
    reinforce="Convierte a decimal en papel los números binarios 0011, 0101 y 1000.",
    extend="Explica con un ejemplo por qué una tabla de verdad permite comprobar un circuito digital sin ver su interior.",
)
