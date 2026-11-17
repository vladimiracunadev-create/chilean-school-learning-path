"""Construcción TP 4.º medio, mención Edificación: OAM-01 (enfierradura: planos, cuadros y cubicación de acero) y OAM-02 (obras de hormigón: documentos, cubicación y control). Solo conceptos y planillas, con datos de ejemplo."""
from __future__ import annotations

from tp_coed_common import AVISO, EMER, build

O1 = "TP-COED-4-OAM-01"
O2 = "TP-COED-4-OAM-02"

# ============================================================ OAM-01, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Casa Maqui» (ficticia): el plano de estructura muestra 4 elementos: fundación, sobrecimiento, pilar y viga. La armadura de cada elemento aparece en el plano con una marca "
     "(por ejemplo, F1 para la fundación). Riesgos anotados en la especificación: cortes con las barras, golpes, sobreesfuerzo al mover cargas, tropiezos y puntas de barras que sobresalen. "
     "Elementos de protección personal pedidos: casco, guantes, lentes y calzado de seguridad.")
build(
    O1, 1, F,
    use="Aprenderé qué es la enfierradura, para qué sirve en los elementos de hormigón, qué documentos la describen y qué riesgos tiene su manejo.",
    prior=["Sé leer una ficha con datos.", "Sé sumar y multiplicar enteros.", "Sé qué es un EPP."],
    explain=[
        "Los elementos estructurales son las partes de una construcción que reciben y transmiten cargas: fundaciones, sobrecimientos, pilares, cadenas, vigas, losas y muros. Muchos son de hormigón armado: hormigón con barras de acero en su interior. El conjunto de barras se llama armadura o enfierradura, y es el que refuerza al hormigón para que resista mejor. Qué barras llevan, de qué diámetro y dónde van, lo dicen el plano de estructura y las especificaciones técnicas: la armadura se lee en esos documentos.",
        "Las barras de acero y su manejo tienen riesgos: cortes, golpes, sobreesfuerzo al mover cargas, tropiezos y puntas que sobresalen. Se previenen con la jerarquía de controles: primero eliminar o reducir el peligro en su origen, después proteger a todo el grupo con protecciones colectivas (por ejemplo, proteger las puntas expuestas) y al final usar EPP, como casco, guantes, lentes y calzado de seguridad. Esta clase solo explica conceptos: no enseña cómo se arma una enfierradura.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("elemento estructural", "parte de la construcción que recibe y transmite cargas, como un pilar o una viga"), ("hormigón armado", "hormigón con barras de acero en su interior"), ("armadura (enfierradura)", "conjunto de barras de acero que refuerza al hormigón"), ("marca", "código que identifica una armadura en el plano"), ("plano de estructura", "plano que muestra los elementos estructurales y sus armaduras"), ("protección colectiva", "medida que protege a todo el grupo, como cubrir puntas expuestas"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Elegir el documento", "Un ayudante de ejemplo quiere saber qué diámetro de barra lleva un pilar. ¿Qué documento consulta?", ["El diámetro y la disposición se indican en el plano de estructura y en las especificaciones.", "Consulta esos documentos, no el presupuesto."], "El plano de estructura y las especificaciones técnicas"),
        ("Contar EPP", "Una obra de ejemplo entrega 3 EPP a cada uno de 5 trabajadores. ¿Cuántos EPP se entregan?", ["Se multiplican los trabajadores por los EPP de cada uno.", "5 por 3 son 15."], "15 EPP"),
    ],
    mistakes=[("Creer que haber leído un plano de armaduras permite armarlas.", "Leer un plano es distinto de ejecutar el trabajo, que exige autorización.", "Aprende los conceptos y practica solo con instructor autorizado."),
              ("Entregar solo guantes y considerar resuelto el riesgo de las puntas expuestas.", "Los EPP son la última medida; primero se reduce el peligro en su origen.", "Aplica la jerarquía de controles.")],
    T=[
        ("abc", "En Construcción: ¿qué es la armadura (enfierradura) de un elemento de hormigón?", "El conjunto de barras de acero que refuerza al hormigón", "El molde dentro del que se contiene el hormigón fresco", "La mezcla de cemento, arena y agua", "La armadura es el acero interior; el molde y la mezcla son otros componentes."),
        ("abc", "En Construcción: ¿qué es un elemento estructural?", "Una parte de la construcción que recibe y transmite cargas, como un pilar o una viga", "Un adorno que se agrega al terminar la obra", "Cualquier objeto que se guarda en la bodega", "Los elementos estructurales soportan y transmiten cargas."),
        ("abc", "¿Qué documento muestra las marcas y la ubicación de las armaduras?", "El plano de estructura", "El libro de pagos de la obra", "La lista de asistencia de los trabajadores", "Las armaduras se identifican con marcas en el plano de estructura."),
        ("=", "{F} Si cada uno de 6 trabajadores recibe los EPP de la ficha, ¿cuántos EPP se entregan?", "6*4", "La ficha pide 4 EPP por trabajador y se multiplica por 6.", " EPP"),
        ("abc", "{F} ¿Qué riesgos anota la especificación?", "Cortes, golpes, sobreesfuerzo, tropiezos y puntas de barras que sobresalen", "Solo ruido y polvo", "Descarga eléctrica y radiación", "La ficha lista cortes, golpes, sobreesfuerzo, tropiezos y puntas sobresalientes."),
        ("abc", "{F} Para las puntas de barras que sobresalen, ¿qué medida está más arriba en la jerarquía de controles?", "Reducir el peligro en su origen y proteger las puntas con una protección colectiva", "Entregar guantes y confiar en que el personal tenga cuidado", "Pedir que todos caminen despacio", "La protección en el origen o en grupo va antes que los EPP."),
        ("ab", "{F} Una estudiante dice: «ya leí el plano de la viga, así que puedo armar su enfierradura». ¿Qué respuesta es correcta?", "No: leer el plano no habilita para ejecutar; el trabajo exige instructor y autorización", "Sí: quien lee el plano puede ejecutar", "Entender un plano es una competencia distinta de estar autorizado para ejecutar."),
        ("abc", "{F} Un trabajador propone no usar casco «porque no hay nada arriba». ¿Qué corresponde?", "Usarlo igual, porque la especificación lo pide como EPP", "Quitárselo si el supervisor no mira", "Quitárselo solo en la mañana", "El EPP pedido por la especificación se usa siempre, aunque no se vea el peligro."),
        ("=", "{F} Si cada elemento tuviera 3 marcas de armadura (de ejemplo), ¿cuántas marcas habría en total?", "4*3", "Se multiplican los elementos por las marcas de cada uno.", " marcas"),
        ("abc", "Una persona cae sobre barras con puntas expuestas y queda herida. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Moverla rápidamente para ponerla cómoda", "Sacarle las barras sin llamar a nadie", "Acercarse o mover a la persona puede agravar el daño; se avisa a quien corresponde."),
        ("abc", "{F} El plano muestra la marca F1 para la fundación y las especificaciones dicen F2 para el mismo elemento. ¿Qué corresponde?", "Anotar la diferencia e informar al proyectista o al supervisor", "Usar la marca del plano sin avisar", "Usar la de las especificaciones sin avisar", "Cuando los documentos se contradicen no se elige uno por cuenta propia."),
        ("=", "{F} Un juego de EPP cuesta $18.000 (de ejemplo). ¿Cuánto cuestan los de 6 trabajadores?", "6*18000", "Se multiplica el valor de un juego por los trabajadores.", " pesos"),
        ("abc", "{F} Una compañera dice que como la obra es pequeña no hace falta proteger las puntas de barras. ¿Qué corresponde?", "Informar que el riesgo existe en cualquier obra y debe controlarse según la norma vigente", "Estar de acuerdo, porque el tamaño reduce el riesgo", "Esperar a que alguien se corte", "El riesgo de las puntas expuestas no depende del tamaño de la obra."),
    ],
    ctx=("abc", "Un familiar le pide a un estudiante que «arme unos fierros» para un muro de su casa, ya que estudió Construcción. ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere contratar a personal calificado", "Acepta, porque ya conoce los planos", "Acepta si el muro es bajo", "Armar una enfierradura exige autorización y norma vigente; haber estudiado conceptos no basta."),
    sc=[
        ("En Construcción: ¿para qué sirve la armadura de un elemento de hormigón?", "Para reforzar al hormigón con barras de acero", "La armadura mejora la resistencia del elemento."),
        ("¿Dónde se lee qué armadura lleva un elemento?", "En el plano de estructura y en las especificaciones", "Ahí se indican las marcas, los diámetros y las ubicaciones."),
        ("¿Quién ejecuta una enfierradura?", "Personal autorizado, con norma vigente y protección", "Este cuaderno no habilita para trabajar en obras."),
    ],
    op=("Obra de ejemplo «Taller Olivo»: el plano de estructura muestra 3 elementos (fundación, pilar y viga) y las especificaciones piden 4 EPP por trabajador; trabajan 5 personas. Escribe (a) cuántos EPP hay que entregar, (b) qué documento consultas para ver la armadura, (c) qué medida va antes que los EPP para las puntas de barras, (d) qué haces si el plano y las especificaciones se contradicen.",
        "(a) 5 por 4 son 20 EPP. (b) El plano de estructura y las especificaciones. (c) Reducir el peligro en su origen o proteger las puntas con una protección colectiva. (d) Anoto la diferencia e informo al proyectista o supervisor.",
        ["calcula los EPP", "nombra el documento", "aplica la jerarquía", "informa la diferencia"],
        ["hoja con las cuatro respuestas"],
        ["decir que los EPP van primero", "elegir un documento por cuenta propia", "afirmar que puede ejecutar el trabajo"],
        "Pregunta: «¿qué va antes que los EPP?». Si no responde, pídele que relea la jerarquía de controles."),
    reinforce="Escribe tres elementos estructurales y, junto a cada uno, una frase sobre qué hace en una construcción.",
    extend="Explica con un ejemplo inventado por qué un riesgo debe controlarse en su origen y no solo con EPP.",
)

# ============================================================ OAM-01, clase 2
F = ("Ficha 2 (cuadro de fierros descrito por escrito, de ejemplo, inventado). Elemento «Viga V1» (ficticia). Cuadro de armadura: marca A, diámetro 12 (de ejemplo), 8 piezas de 3 m cada una; "
     "marca B, diámetro 8 (de ejemplo), 20 piezas de 1 m cada una. Peso de ejemplo por metro: diámetro 12, 2 kg por metro; diámetro 8, 1 kg por metro. "
     "Roles: el ingeniero calculista diseña la armadura; el jefe de obra organiza el trabajo; el inspector técnico verifica que se cumplan los planos; el maestro enfierrador ejecuta, si está autorizado.")
build(
    O1, 2, F,
    use="Aprenderé a leer un cuadro de armadura (marca, diámetro, cantidad y longitud), a calcular longitud y peso en una planilla y a reconocer los roles.",
    prior=["Sé qué es una armadura y una marca.", "Sé multiplicar y sumar enteros.", "Sé qué es un plano de estructura."],
    explain=[
        "El cuadro de armadura es una tabla del plano de estructura que lista cada marca con su diámetro, su cantidad de piezas y la longitud de cada pieza. El diámetro es el ancho de la barra y se expresa en milímetros; en este cuaderno los diámetros y los pesos son de ejemplo. Con el cuadro se calcula la longitud total de cada marca (cantidad por longitud de cada pieza) y el peso, que es la longitud total por el peso de cada metro. Eso se llama cubicar, en este caso, el acero.",
        "Cada rol tiene su función. El ingeniero calculista diseña la armadura; el jefe de obra organiza el trabajo y las compras; el inspector técnico verifica que la obra cumpla los planos y las especificaciones; el maestro enfierrador ejecuta el trabajo, si está autorizado y sigue la norma vigente. Si el cuadro y el plano no coinciden, no se corrige por cuenta propia: se informa al proyectista o al inspector.",
        f"Los números son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("cuadro de armadura", "tabla del plano con marca, diámetro, cantidad y longitud de cada pieza"), ("diámetro", "ancho de una barra, en milímetros"), ("longitud total", "cantidad de piezas por la longitud de cada una"), ("peso por metro", "peso de un metro de barra de un diámetro dado"), ("cubicar", "calcular cantidades de material a partir de planos y medidas"), ("ingeniero calculista", "profesional que diseña la estructura y su armadura"), ("inspector técnico", "persona que verifica que la obra cumpla planos y especificaciones")],
    worked=[
        ("Longitud total", "Una marca de ejemplo tiene 10 piezas de 2 m. ¿Cuál es su longitud total?", ["Se multiplican las piezas por la longitud de cada una.", "10 por 2 son 20."], "20 m"),
        ("Peso", "Esa marca de ejemplo pesa 3 kg por metro. ¿Cuál es su peso total?", ["La longitud total es 20 m.", "20 por 3 son 60."], "60 kg"),
    ],
    mistakes=[("Multiplicar las piezas por el peso por metro sin considerar su longitud.", "El peso depende de la longitud total, no solo de las piezas.", "Primero calcula la longitud total y luego el peso."),
              ("Cambiar un diámetro del cuadro porque «da lo mismo».", "El diámetro lo define el calculista y afecta la resistencia.", "Informa la duda al proyectista o inspector.")],
    T=[
        ("abc", "En Construcción: ¿qué es un cuadro de armadura?", "Una tabla del plano con marca, diámetro, cantidad y longitud de cada pieza", "El horario de los maestros de la obra", "Una lista de precios del proveedor", "El cuadro describe las armaduras; no trata de horarios ni precios."),
        ("abc", "En Construcción: ¿qué es el diámetro de una barra?", "El ancho de la barra, expresado en milímetros", "El largo de la barra", "El peso de la barra", "El diámetro es el ancho de la barra; el largo y el peso son otras medidas."),
        ("abc", "¿Qué rol verifica que la obra cumpla los planos y las especificaciones?", "El inspector técnico", "El proveedor de acero", "El visitante", "El inspector técnico verifica la conformidad con planos y especificaciones."),
        ("=", "{F} ¿Cuál es la longitud total de la marca A?", "8*3", "Se multiplican las piezas por la longitud de cada una.", " m"),
        ("=", "{F} ¿Cuál es la longitud total de la marca B?", "20*1", "Se multiplican las piezas por la longitud de cada una.", " m"),
        ("=", "{F} ¿Cuál es el peso total de la marca A?", "8*3*2", "Se multiplican la longitud total por el peso por metro de la marca A.", " kg"),
        ("=", "{F} ¿Cuál es el peso total de la marca B?", "20*1*1", "Se multiplican la longitud total por el peso por metro de la marca B.", " kg"),
        ("abc", "{F} ¿Qué marca pesa más en total?", "La marca A, con 48 kg frente a 20 kg de la B", "La marca B, porque tiene más piezas", "Las dos pesan igual", "A pesa 8 por 3 por 2 = 48 kg y B pesa 20 kg."),
        ("=", "{F} ¿Cuántos kg de acero tiene la viga en total, sumando las dos marcas?", "8*3*2+20*1*1", "Se suman los pesos de las dos marcas.", " kg"),
        ("ab", "{F} Un ayudante dice: «cambio el diámetro de la marca B por uno mayor, que da lo mismo». ¿Qué respuesta es correcta?", "No: el diámetro lo define el calculista; se informa antes de cambiar algo", "Sí: un diámetro mayor siempre es mejor", "El diámetro afecta la resistencia y solo lo decide quien diseña."),
        ("abc", "{F} El cuadro de la viga dice 8 piezas, pero el plano dibuja 7 de la marca A. ¿Qué corresponde?", "Anotar la diferencia e informar al proyectista o al inspector", "Usar 7, porque el plano manda", "Usar 8, porque el cuadro manda", "Cuando los documentos se contradicen no se elige uno por cuenta propia."),
        ("=", "{F} Si el acero cuesta $1.200 por kg (de ejemplo), ¿cuánto cuesta el acero de las dos marcas?", "(8*3*2+20*1*1)*1200", "Se multiplica el peso total por el precio de un kg.", " pesos"),
        ("abc", "Una pila de barras se desmorona y atrapa a una persona. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Mover las barras entre varios sin avisar", "Esperar a que la persona salga sola", "Acercarse sin ayuda puede causar otro atrapamiento."),
    ],
    ctx=("abc", "El proveedor de ejemplo entrega barras de un diámetro distinto del pedido y dice que «sirven igual». ¿Qué corresponde?", "Registrar la diferencia e informar al inspector técnico antes de aceptar", "Aceptarlas para no atrasar", "Usarlas y anotar el diámetro pedido", "Cambiar un diámetro sin autorización puede afectar la resistencia."),
    sc=[
        ("En Construcción: ¿cómo se obtiene la longitud total de una marca?", "Piezas por la longitud de cada pieza", "Es una multiplicación del cuadro de armadura."),
        ("¿Quién diseña la armadura?", "El ingeniero calculista", "El inspector verifica y el maestro ejecuta."),
        ("¿Se cambia un diámetro porque da lo mismo?", "No: se informa al proyectista o al inspector", "El diámetro afecta la resistencia y lo decide quien diseña."),
    ],
    op=("Viga de ejemplo V2: marca C, diámetro 10 (de ejemplo), 6 piezas de 4 m, peso de ejemplo 2 kg por metro; marca D, diámetro 6 (de ejemplo), 30 piezas de 1 m, peso de ejemplo 1 kg por metro. Escribe (a) la longitud total de cada marca, (b) el peso total de cada marca, (c) el peso de las dos juntas, (d) a quién informas si el plano dibuja 29 piezas de la marca D.",
        "(a) C: 24 m; D: 30 m. (b) C: 24 por 2 = 48 kg; D: 30 por 1 = 30 kg. (c) 78 kg. (d) Informo la diferencia al proyectista o al inspector técnico.",
        ["calcula las longitudes", "calcula los pesos", "suma el total", "informa sin elegir"],
        ["hoja con las cuatro respuestas"],
        ["multiplicar sin la longitud", "elegir entre 29 y 30", "sumar solo una marca"],
        "Pregunta: «¿qué multiplicas para el peso?». Si no responde, pídele que relea cómo se obtiene el peso."),
    reinforce="Inventa un cuadro de armadura con dos marcas y calcula la longitud total y el peso de cada una.",
    extend="Explica por qué cambiar un diámetro sin consultar puede ser un riesgo para la seguridad de la estructura.",
)

# ============================================================ OAM-01, clase 3
F = ("Ficha 3 (caso en papel, de ejemplo, inventado). Obra «Sede Radal» (ficticia). Pedido de acero: marca P1, diámetro 12 (de ejemplo), 10 barras de 12 m; marca P2, diámetro 8 (de ejemplo), 6 barras de 12 m. "
     "Guía de despacho GD-8 del proveedor de ejemplo: diámetro 12, 10 barras de 12 m; diámetro 10, 6 barras de 12 m. "
     "Regla de recepción de ejemplo: los diámetros y las cantidades de la guía deben coincidir con el pedido; si no coinciden, se deja constancia y se informa al inspector técnico antes de aceptar.")
build(
    O1, 3, F,
    use="Analizaré en papel un pedido de acero contra la guía de despacho, detectaré diferencias y decidiré a quién informar.",
    prior=["Sé qué es un cuadro de armadura.", "Sé qué es una guía de despacho.", "Sé multiplicar enteros."],
    explain=[
        "Cuando llega el acero a la obra, se compara el pedido con la guía de despacho y con lo que realmente llegó. Esta revisión se llama recepción. Se revisan el diámetro, la cantidad y, en general, la identificación que trae el material. Las barras suelen venir en largos comerciales, por ejemplo de 12 m; para saber cuántas barras se necesitan se divide la longitud total pedida entre el largo de cada barra y, si sobra, se cuenta una barra más.",
        "Si algo no coincide, se deja constancia escrita, se separa lo observado a la vista de todos (sin moverlo con maquinaria ni cargarlo a mano si es pesado) y se informa al inspector técnico antes de aceptar. Aceptar un material distinto del pedido sin autorización puede dejar una estructura con menor resistencia. Nadie modifica la guía ni el pedido para que «cuadren».",
        f"Este caso es de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("recepción", "revisión del material que llega, comparándolo con el pedido y la guía"), ("pedido", "lista de lo que la obra solicita al proveedor"), ("largo comercial", "largo en que el proveedor entrega las barras"), ("observación de recepción", "diferencia que se anota al recibir un material"), ("constancia", "anotación escrita de la diferencia y a quién se informó")],
    worked=[
        ("Barras necesarias", "Un pedido de ejemplo necesita 30 m de barras que vienen en largos de 12 m. ¿Cuántas barras se piden?", ["30 dividido por 12 da 2 y sobran 6 m.", "Como sobra, se cuenta una barra más: 3."], "3 barras"),
        ("Detectar diferencia", "Un pedido de ejemplo pide 8 barras de diámetro 10 y la guía trae 8 barras de diámetro 12. ¿Coinciden?", ["La cantidad coincide, pero el diámetro no.", "El diámetro es distinto."], "No coinciden: el diámetro es diferente"),
    ],
    mistakes=[("Aceptar una guía distinta del pedido porque «el acero es acero».", "El diámetro cambia la resistencia y debe coincidir con el diseño.", "Anota la diferencia e informa al inspector técnico."),
              ("Cambiar a mano el diámetro de la guía para que coincida.", "Alterar un documento es una falta y esconde el problema.", "Deja constancia e informa.")],
    T=[
        ("abc", "En Construcción: ¿qué es la recepción de un material?", "La revisión del material que llega, comparándolo con el pedido y la guía", "El pago al proveedor", "El almacenamiento en la intemperie", "La recepción compara lo que llegó con lo pedido y con la guía."),
        ("abc", "En Construcción: ¿qué es un largo comercial de barras?", "El largo en que el proveedor entrega las barras", "El largo que se pinta en el plano", "El largo del camino a la obra", "El largo comercial es el largo estándar de entrega del proveedor."),
        ("abc", "Si lo que llegó no coincide con el pedido, ¿qué se hace?", "Dejar constancia e informar al inspector técnico antes de aceptar", "Aceptarlo para no atrasar", "Corregir el pedido a mano", "Una diferencia se informa antes de aceptar, no se ajusta a mano."),
        ("=", "{F} ¿Cuántos metros de barra de diámetro 12 se piden en total?", "10*12", "Se multiplican las barras pedidas por su largo.", " m"),
        ("abc", "{F} ¿Coincide la guía con el pedido de la marca P1?", "Sí: ambos dicen diámetro 12 y 10 barras de 12 m", "No: la guía trae menos barras", "No: el diámetro es distinto", "La guía y el pedido de P1 indican lo mismo."),
        ("abc", "{F} ¿Qué diferencia hay en la marca P2?", "La guía trae diámetro 10 y el pedido era diámetro 8", "La guía trae menos barras que el pedido", "La guía trae barras de otro largo", "La cantidad (6) y el largo coinciden; el diámetro no."),
        ("=", "{F} ¿Cuántas barras de 12 m recibió en total la obra según la guía?", "10+6", "Se suman las barras de los dos diámetros de la guía.", " barras"),
        ("ab", "{F} Un jefe dice: «aceptemos el diámetro 10 porque es parecido al 8». ¿Qué respuesta es correcta?", "No: el cambio de diámetro lo decide quien diseña; se informa al inspector técnico", "Sí: un diámetro mayor siempre sirve", "El diámetro afecta la resistencia y solo lo autoriza el diseño."),
        ("abc", "{F} ¿A quién se informa la diferencia según la regla de recepción?", "Al inspector técnico", "Al conductor del camión", "Al vecino de la obra", "La regla de la ficha indica informar al inspector técnico."),
        ("=", "{F} Para cubrir 50 piezas de 1 m con barras de 12 m, ¿cuántas barras se necesitan?", "(50+11)//12", "Se divide 50 entre 12 y, como sobran 2 m, se cuenta una barra más.", " barras"),
        ("abc", "{F} Un auxiliar quiere corregir con lápiz el diámetro de la guía a 8 «para cerrar». ¿Qué corresponde?", "No hacerlo: dejar constancia de la diferencia e informar", "Hacerlo, si la diferencia es pequeña", "Hacerlo, si el conductor se va", "Alterar la guía falsea el registro y deja pasar un material no pedido."),
        ("=", "{F} Si la barra de diámetro 10 pesa 2 kg por metro (de ejemplo), ¿cuántos kg tienen las 6 barras de 12 m recibidas?", "6*12*2", "Se multiplican barras, largo y peso por metro.", " kg"),
        ("abc", "Mientras se descarga acero, una barra cae y un trabajador queda atrapado. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Levantar el acero entre varios", "Seguir descargando para despejar", "Mover cargas pesadas sin ayuda puede agravar el accidente."),
    ],
    ctx=("abc", "Un conductor de ejemplo dice que «ya está acordado» cambiar el diámetro y pide la firma de recepción sin más. ¿Qué corresponde?", "No firmar y dejar constancia de la diferencia hasta que informe el inspector técnico", "Firmar para que se retire", "Firmar si anota «conforme» en otra hoja", "Una firma de conformidad a un material distinto puede ser usada como aprobación."),
    sc=[
        ("En Construcción: ¿qué se compara en la recepción del acero?", "El pedido, la guía y lo que llegó", "Así se detectan diferencias antes de aceptar."),
        ("¿Cuántas barras se piden si sobra un trozo?", "Se cuenta una barra más", "Un trozo sobrante igual requiere una barra."),
        ("¿Se cambia la guía para que coincida?", "No: se deja constancia e informa", "Alterar una guía falsea el registro."),
    ],
    op=("Caso de ejemplo «Taller Peumo»: pedido de 5 barras de 12 m de diámetro 10 y 4 barras de 12 m de diámetro 6; la guía trae 5 barras de 12 m de diámetro 10 y 3 barras de 12 m de diámetro 6. Escribe (a) qué marca no coincide y por qué, (b) cuántas barras se recibieron en total, (c) qué haces antes de aceptar y a quién informas.",
        "(a) Las de diámetro 6: se pidieron 4 y la guía trae 3. (b) 5+3 son 8 barras. (c) Dejo constancia de la diferencia e informo al inspector técnico antes de aceptar.",
        ["detecta la diferencia", "suma las barras", "deja constancia e informa", "no altera la guía"],
        ["hoja con las tres respuestas"],
        ["decir que todo coincide", "aceptar sin avisar", "cambiar la guía"],
        "Pregunta: «¿qué barras no coinciden?». Si no responde, pídele que compare cantidad y diámetro por separado."),
    reinforce="Inventa un pedido y una guía de dos marcas con una diferencia y escribe qué hay que informar.",
    extend="Explica por qué detectar una diferencia en la recepción es más barato que corregirla después.",
)

# ============================================================ OAM-01, clase 4
F = ("Ficha 4 (cubicación de ejemplo, inventada). Obra «Bodega Canelo» (ficticia). Acero de la armadura por elemento: fundaciones, 250 kg; sobrecimientos, 140 kg; pilares, 90 kg. "
     "Merma de ejemplo: 5 % sobre el total. Precio de ejemplo: $1.300 por kg. Rendimiento de ejemplo de la cuadrilla: 21 kg por hora. Jornada de ejemplo: 8 horas.")
build(
    O1, 4, F,
    use="Aplicaré criterios de ejemplo para cubicar el acero de una obra, sumar la merma, calcular el costo y estimar las horas y los días de trabajo en una planilla.",
    prior=["Sé calcular longitud y peso con un cuadro de armadura.", "Sé calcular un porcentaje simple.", "Sé multiplicar y dividir enteros."],
    explain=[
        "La cubicación de acero suma los kilos de cada elemento de la obra y da el total teórico. Pero parte del material se pierde o sobra al prepararlo: esa pérdida se llama merma y se expresa como un porcentaje del total. Para saber cuánto pedir se suma la merma al total teórico. Para calcular un porcentaje se multiplica el total por el porcentaje y se divide por 100: el 5 % de 200 es 200 por 5 dividido por 100, que da 10.",
        "Con la cantidad que se pide se calcula el costo: kilos por precio de un kilo. El rendimiento es la cantidad de trabajo que una cuadrilla hace en una hora; con él se estiman las horas de trabajo (kilos divididos por el rendimiento) y los días (horas divididas por la jornada). Todo es una estimación de planilla con valores de ejemplo: los rendimientos y precios reales dependen del proyecto, de la obra y de la norma vigente.",
        f"Esta clase no enseña a preparar ni a instalar armaduras. {EMER} {AVISO}",
    ],
    vocab=[("cubicación", "cálculo de las cantidades de material de una obra"), ("merma", "pérdida de material, expresada como porcentaje del total"), ("porcentaje", "parte de un total expresada sobre 100"), ("rendimiento", "cantidad de trabajo que se hace en una hora"), ("cuadrilla", "grupo de trabajadores que realiza una tarea"), ("jornada", "horas de trabajo de un día")],
    worked=[
        ("Aplicar la merma", "Una obra de ejemplo cubica 200 kg y tiene una merma de 10 %. ¿Cuántos kg se piden?", ["El 10 % de 200 es 200 por 10 dividido por 100, o sea 20.", "200 más 20 son 220."], "220 kg"),
        ("Horas y días", "Un trabajo de ejemplo es de 160 kg con un rendimiento de 20 kg por hora y jornadas de 8 horas. ¿Cuántos días?", ["Las horas son 160 dividido por 20, o sea 8.", "Una jornada es de 8 horas: 1 día."], "1 día"),
    ],
    mistakes=[("Pedir solo el total teórico, sin la merma.", "Parte del material se pierde y faltaría acero.", "Suma la merma al total teórico."),
              ("Calcular el 5 % como 5 veces el total.", "Un porcentaje se divide por 100.", "Multiplica por el porcentaje y divide por 100.")],
    T=[
        ("abc", "En Construcción: ¿qué es la merma de un material?", "La pérdida de material, expresada como porcentaje del total", "El material que se compra de más por gusto", "El precio por kilo del material", "La merma es lo que se pierde al preparar y manejar el material."),
        ("abc", "En Construcción: ¿qué es el rendimiento de una cuadrilla?", "La cantidad de trabajo que hace en una hora", "El número de personas de la cuadrilla", "El costo del acero", "El rendimiento mide trabajo por hora."),
        ("abc", "¿Cómo se calcula un porcentaje de un total?", "Se multiplica el total por el porcentaje y se divide por 100", "Se suma el porcentaje al total", "Se resta el porcentaje a 100", "Un porcentaje es una parte sobre 100 del total."),
        ("=", "{F} ¿Cuántos kg de acero suman los tres elementos?", "250+140+90", "Se suman los kilos de los tres elementos.", " kg"),
        ("=", "{F} ¿Cuántos kg corresponden a la merma del 5 %?", "(250+140+90)*5//100", "Se multiplica el total por 5 y se divide por 100.", " kg"),
        ("=", "{F} ¿Cuántos kg de acero se piden, sumando la merma?", "(250+140+90)+(250+140+90)*5//100", "Se suma la merma al total teórico.", " kg"),
        ("=", "{F} ¿Cuánto cuesta el acero que se pide?", "((250+140+90)+(250+140+90)*5//100)*1300", "Se multiplican los kg pedidos por el precio de un kg.", " pesos"),
        ("=", "{F} ¿Cuántas horas de trabajo se estiman para los kg pedidos?", "((250+140+90)+(250+140+90)*5//100)//21", "Se divide el total pedido entre el rendimiento por hora.", " horas"),
        ("=", "{F} ¿Cuántos días de jornada se estiman para esas horas?", "(((250+140+90)+(250+140+90)*5//100)//21)//8", "Se dividen las horas entre las horas de una jornada.", " días"),
        ("ab", "{F} Un jefe dice: «pidamos solo los 480 kg del total, la merma no existe». ¿Qué respuesta es correcta?", "No: parte del material se pierde y se debe considerar la merma", "Sí: lo que se calcula es lo que se usa", "La merma es una pérdida real que obliga a pedir un poco más que el teórico."),
        ("abc", "{F} Si el precio subiera a $1.500 por kg, ¿cuál sería el costo de los 504 kg?", "$756.000", "$655.200", "$504.000", "Se multiplican los 504 kg por $1.500 cada kg, que da $756.000."),
        ("=", "{F} Si la merma fuera de 10 % en vez de 5 %, ¿cuántos kg se pedirían?", "480+480*10//100", "Se calcula el 10 % del total y se suma.", " kg"),
        ("abc", "Una pila de barras mal apoyada cae y atrapa a una persona. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Mover las barras entre varios sin avisar", "Esperar que se levante sola", "Acercarse sin ayuda puede causar otro accidente."),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo quiere ahorrar y pide quitar la merma de la cubicación. Después faltan 24 kg de acero y se atrasa el trabajo. ¿Cuál fue el error?", "No considerar que parte del material se pierde y debe pedirse de más", "Haber pedido muy pocas horas de trabajo", "Haber comprado muchas señales", "La merma es una pérdida normal; quitarla del cálculo deja el pedido corto."),
    sc=[
        ("En Construcción: ¿cómo se pide el acero considerando la merma?", "Se suma la merma al total teórico", "Así se compensa lo que se pierde."),
        ("¿Cómo se calculan las horas de un trabajo?", "Kilos divididos por el rendimiento", "El rendimiento mide cuántos kilos se hacen por hora."),
        ("¿Qué son los valores de esta clase?", "Valores de ejemplo para calcular en planilla", "Los valores reales los fija el proyecto y la norma vigente."),
    ],
    op=("Obra de ejemplo «Taller Roble»: acero por elemento: fundación 300 kg; viga 100 kg. Merma de ejemplo 10 %; precio de ejemplo $1.000 por kg; rendimiento de ejemplo 22 kg por hora; jornada de 8 horas. Escribe (a) el total teórico, (b) los kg que pides, (c) el costo, (d) las horas y los días estimados.",
        "(a) 400 kg. (b) La merma es 40 kg y se piden 440 kg. (c) 440 por 1.000 son 440.000 pesos. (d) 440 dividido por 22 son 20 horas; con jornadas de 8 horas son 2,5 días, o sea 3 jornadas.",
        ["suma el total", "agrega la merma", "calcula el costo", "estima horas y días"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la merma", "no dividir el porcentaje entre 100", "confundir horas con días"],
        "Pregunta: «¿qué sumas al total teórico?». Si no responde, pídele que relea qué es la merma."),
    reinforce="Inventa tres elementos con sus kilos de acero y calcula el total y el pedido con una merma de 5 %.",
    extend="Explica por qué un cálculo de horas con rendimiento de ejemplo es solo una estimación.",
)

# ============================================================ OAM-01, clase 5
F = ("Ficha 5 (comparación y verificación, de ejemplo, inventadas). Obra «Escuela Notro» (ficticia), 400 kg de acero. Alternativa A: preparar la armadura en la obra: acero a $1.100 por kg más 20 horas de mano de obra a $6.000 la hora. "
     "Alternativa B: recibir la armadura prefabricada de una planta: $1.500 por kg, sin horas de mano de obra en la obra para prepararla. "
     "Lista de verificación previa de ejemplo (la completa el inspector técnico): 1) diámetros según el plano: cumple; 2) cantidad según el cuadro: cumple; 3) recubrimiento según la especificación: no cumple; "
     "4) armadura limpia, sin residuos sueltos: cumple; 5) firma del inspector: pendiente. Regla de ejemplo: no se autoriza continuar con observaciones abiertas.")
build(
    O1, 5, F,
    use="Compararé dos alternativas de abastecimiento de armadura por costo, riesgo y control de calidad, y leeré una lista de verificación previa.",
    prior=["Sé calcular costo con kilos y precio.", "Sé qué es una lista de verificación.", "Sé qué hace el inspector técnico."],
    explain=[
        "Al decidir entre dos alternativas se comparan varios criterios, no solo el costo: el riesgo para las personas, el tiempo y el control de la calidad. Una armadura prefabricada es la que se prepara en una planta y llega a la obra; así se reducen las horas de trabajo expuestas a los riesgos propios de la obra, aunque el precio por kilo suele ser mayor. Una armadura preparada en obra evita transporte, pero exige más horas de trabajo y control.",
        "La verificación de calidad se registra en una lista de verificación: cada ítem queda en cumple, no cumple o pendiente. El recubrimiento es la capa de hormigón que cubre el acero para protegerlo; su valor lo fija la especificación técnica. Una observación abierta es un ítem que no cumple o está pendiente. La regla de la obra impide autorizar la continuación mientras haya observaciones abiertas, y quien autoriza es el inspector técnico con su firma.",
        f"Los valores son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("armadura prefabricada", "armadura preparada en una planta y entregada a la obra"), ("lista de verificación", "tabla donde cada ítem queda en cumple, no cumple o pendiente"), ("recubrimiento", "capa de hormigón que cubre el acero para protegerlo"), ("observación abierta", "ítem que no cumple o está pendiente"), ("criterio de comparación", "aspecto con el que se comparan alternativas, como costo o riesgo")],
    worked=[
        ("Comparar costos", "Alternativa A de ejemplo: $50.000 de material más $30.000 de mano de obra. Alternativa B: $70.000 todo incluido. ¿Cuál cuesta menos?", ["A cuesta 50.000+30.000 = 80.000.", "B cuesta 70.000, que es menos."], "La alternativa B"),
        ("Leer la lista", "Una lista de ejemplo tiene 4 ítems: 2 cumplen, 1 no cumple y 1 pendiente. ¿Cuántas observaciones abiertas hay?", ["Abiertas son las que no cumplen más las pendientes.", "1 más 1 son 2."], "2 observaciones abiertas"),
    ],
    mistakes=[("Elegir siempre la alternativa más barata, sin mirar el riesgo ni la calidad.", "Una alternativa barata puede dejar más horas expuestas o menos control.", "Compara varios criterios antes de decidir."),
              ("Firmar la lista aunque haya un ítem pendiente.", "Una firma con observaciones abiertas autoriza algo que no está verificado.", "Cierra las observaciones antes de firmar.")],
    T=[
        ("abc", "En Construcción: ¿qué es una armadura prefabricada?", "La que se prepara en una planta y llega a la obra", "La que se prepara solo con ayuda del vecino", "La que se pinta antes de usarla", "Prefabricada significa preparada antes, en una planta."),
        ("abc", "En Construcción: ¿qué es el recubrimiento de una armadura?", "La capa de hormigón que cubre el acero para protegerlo", "El papel que envuelve las barras en la bodega", "La pintura de la obra", "El recubrimiento protege al acero y lo fija la especificación."),
        ("abc", "¿Qué es una observación abierta en una lista de verificación?", "Un ítem que no cumple o está pendiente", "Un ítem que ya fue firmado", "Un ítem que cumple", "Abierta significa que aún no está resuelta."),
        ("=", "{F} ¿Cuánto cuesta en total la alternativa A?", "400*1100+20*6000", "Se suman el costo del acero y el de la mano de obra.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta en total la alternativa B?", "400*1500", "Se multiplican los kg por el precio por kg de B.", " pesos"),
        ("=", "{F} ¿Cuántos pesos más cuesta B que A?", "400*1500-(400*1100+20*6000)", "Se resta el costo de A al costo de B.", " pesos"),
        ("abc", "{F} Si se comparan solo los costos, ¿qué alternativa cuesta menos?", "La alternativa A", "La alternativa B", "Cuestan lo mismo", "A cuesta 560.000 y B cuesta 600.000."),
        ("abc", "{F} ¿Qué criterio, además del costo, favorece a la alternativa B?", "Reduce las horas de trabajo expuestas a los riesgos de la obra", "Hace que el acero pese menos", "Elimina la necesidad de un inspector", "B evita las 20 horas de preparación en obra; no cambia el peso ni suprime la verificación."),
        ("=", "{F} ¿Cuántos ítems de la lista quedan como observaciones abiertas?", "1+1", "Se suma el ítem que no cumple y el ítem pendiente.", " ítems"),
        ("ab", "{F} Un supervisor dice: «el recubrimiento no cumple, pero sigamos, ya firmamos el resto». ¿Qué respuesta es correcta?", "No: la regla impide continuar mientras haya observaciones abiertas", "Sí: lo importante es que los otros ítems cumplen", "Un ítem que no cumple debe resolverse antes de autorizar la continuación."),
        ("abc", "{F} ¿Quién completa la lista de verificación según la ficha?", "El inspector técnico", "El proveedor", "El vecino", "La ficha dice que la completa el inspector técnico."),
        ("abc", "{F} Un auxiliar propone cambiar «no cumple» por «cumple» en el ítem 3 para avanzar. ¿Qué corresponde?", "No: se informa la observación y se resuelve antes de autorizar", "Sí, si es solo una vez", "Sí, si lo hace antes de que llegue el inspector", "Alterar una lista de verificación oculta un defecto real."),
        ("abc", "Una persona se cae entre barras ya instaladas y no puede moverse. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Levantarla rápido entre varios", "Mover las barras para llegar a ella", "Acercarse o moverla sin ayuda puede agravar el daño."),
    ],
    ctx=("abc", "Un jefe de obra de ejemplo duda: la alternativa B cuesta más, pero quita horas de trabajo de la obra. ¿Cómo decide mejor?", "Comparando costo, riesgo, plazo y calidad, y dejando la decisión registrada", "Eligiendo la más barata siempre", "Eligiendo la que le recomiende el proveedor", "Una decisión se apoya en varios criterios y se registra por escrito."),
    sc=[
        ("En Construcción: ¿qué es el recubrimiento?", "La capa de hormigón que cubre y protege el acero", "Su valor lo fija la especificación técnica."),
        ("¿Qué pasa si hay observaciones abiertas?", "No se autoriza continuar hasta resolverlas", "Así lo exige la regla de la obra de ejemplo."),
        ("¿Se elige solo por costo?", "No: también por riesgo, plazo y calidad", "Un solo criterio puede dar una mala decisión."),
    ],
    op=("Obra de ejemplo «Taller Mañío»: 200 kg de acero. Alternativa A: $1.200 por kg más 10 horas de mano de obra a $5.000 la hora. Alternativa B: $1.700 por kg. Lista de ejemplo: diámetros, cumple; cantidad, cumple; recubrimiento, pendiente; firma, pendiente. Escribe (a) el costo de cada alternativa, (b) cuál es más barata, (c) un criterio no económico a considerar, (d) cuántas observaciones abiertas hay y qué pasa con ellas.",
        "(a) A: 240.000+50.000 = 290.000 pesos; B: 340.000 pesos. (b) A. (c) El riesgo: B evita las 10 horas de preparación en la obra. (d) Dos: recubrimiento y firma; no se autoriza continuar hasta resolverlas.",
        ["calcula ambos costos", "identifica la más barata", "nombra un criterio no económico", "cuenta las observaciones abiertas"],
        ["hoja con las cuatro respuestas"],
        ["olvidar la mano de obra", "contar los ítems que cumplen como abiertos", "autorizar con observaciones abiertas"],
        "Pregunta: «¿qué incluye el costo de A?». Si no responde, pídele que relea la ficha."),
    reinforce="Inventa dos alternativas para un material con costo y un criterio no económico y escribe cuál elegirías y por qué.",
    extend="Explica por qué una lista de verificación firmada solo vale si cada ítem se revisó de verdad.",
)

# ============================================================ OAM-02, clase 1
F = ("Ficha 1 (obra de ejemplo, inventada). Obra «Casa Quillay» (ficticia): se pide hormigón premezclado para la fundación y el sobrecimiento; llega en camiones mixer de ejemplo. "
     "Riesgos anotados: polvo de cemento, irritación de la piel por contacto con hormigón fresco, atropello o atrapamiento por los camiones, sobreesfuerzo, ruido y caídas al mismo nivel. "
     "EPP pedidos: casco, guantes impermeables, botas de goma y lentes.")
build(
    O2, 1, F,
    use="Aprenderé el vocabulario básico del hormigón, la diferencia entre hormigón premezclado y preparado en obra, y los riesgos de las obras de hormigón.",
    prior=["Sé qué es un elemento estructural.", "Sé qué es la jerarquía de controles.", "Sé qué es un EPP."],
    explain=[
        "El hormigón es una mezcla de cemento, agua y agregados (grava y arena) que, al endurecer, forma un material resistente. Mientras está blando se llama hormigón fresco. El hormigón premezclado se prepara en una planta y llega a la obra en camiones mixer (camiones con un tambor que transporta la mezcla). El hormigón preparado en obra se mezcla en el mismo lugar. En ambos casos las especificaciones técnicas y los planos de estructura indican qué hormigón se pide y para qué elementos: fundaciones, sobrecimientos, pilares, vigas, cadenas, losas y muros.",
        "Los riesgos principales son el polvo de cemento, la irritación de la piel y los ojos por contacto con el hormigón fresco, el atropello o atrapamiento por camiones, el sobreesfuerzo, el ruido y las caídas. Se controlan según la jerarquía: primero eliminar o reducir el peligro en su origen, luego proteger al grupo y, al final, usar EPP. Este cuaderno no enseña a preparar, transportar ni colocar hormigón.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("hormigón", "mezcla de cemento, agua y agregados que endurece y forma un material resistente"), ("agregados", "grava y arena que forman parte del hormigón"), ("hormigón fresco", "hormigón que todavía está blando"), ("hormigón premezclado", "hormigón preparado en una planta y llevado a la obra"), ("hormigón preparado en obra", "hormigón que se mezcla en la misma obra"), ("camión mixer", "camión con tambor que transporta hormigón premezclado"), ("EPP", "elementos de protección personal")],
    worked=[
        ("Distinguir tipos", "Una obra de ejemplo recibe hormigón desde una planta en camiones con tambor. ¿Es premezclado o preparado en obra?", ["Viene de una planta.", "Es hormigón premezclado."], "Hormigón premezclado"),
        ("Contar EPP", "Una obra de ejemplo entrega 4 EPP a cada uno de 7 trabajadores. ¿Cuántos EPP entrega?", ["Se multiplican trabajadores por EPP.", "7 por 4 son 28."], "28 EPP"),
    ],
    mistakes=[("Creer que el hormigón fresco es inofensivo para la piel.", "El contacto puede irritar la piel y los ojos.", "Usa los EPP pedidos y sigue la norma vigente."),
              ("Pensar que quien estudió esta clase ya puede dirigir un hormigonado.", "Esta clase solo explica conceptos; ejecutar exige instructor y autorización.", "Aprende el concepto y practica solo con instructor.")],
    T=[
        ("abc", "En Construcción: ¿qué es el hormigón?", "Una mezcla de cemento, agua y agregados que endurece y forma un material resistente", "Una pintura de color gris para muros", "Un metal que se usa en barras", "El hormigón es una mezcla que endurece; el metal es el acero."),
        ("abc", "En Construcción: ¿qué es el hormigón premezclado?", "El hormigón preparado en una planta y llevado a la obra", "El hormigón que se prepara en la bodega con las sobras", "El hormigón que ya endureció", "Premezclado significa preparado antes, fuera de la obra."),
        ("abc", "¿Qué son los agregados del hormigón?", "La grava y la arena que forman parte de la mezcla", "Los clavos de la obra", "Las señales de seguridad", "Los agregados son los áridos que acompañan al cemento y al agua."),
        ("=", "{F} Si cada uno de 8 trabajadores recibe los EPP de la ficha, ¿cuántos EPP se entregan?", "8*4", "Se multiplican los trabajadores por los 4 EPP.", " EPP"),
        ("abc", "{F} ¿Qué riesgo anota la ficha para el contacto con hormigón fresco?", "Irritación de la piel", "Quemaduras por fuego", "Descargas eléctricas", "La ficha anota irritación de la piel por contacto con hormigón fresco."),
        ("abc", "{F} ¿Qué tipo de hormigón se pide en la ficha?", "Premezclado, entregado en camiones mixer", "Preparado en obra con una mezcladora", "Hormigón ya endurecido", "La ficha dice que se pide premezclado."),
        ("ab", "{F} Un estudiante dice: «ya sé qué es el hormigón, así que puedo dirigir el hormigonado». ¿Qué respuesta es correcta?", "No: conocer conceptos no habilita; dirigir un hormigonado exige instructor y autorización", "Sí: conocer el vocabulario basta", "Entender los conceptos es distinto de estar autorizado para ejecutar."),
        ("abc", "{F} Un camión de la obra retrocede y un trabajador queda atrapado. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Acercarse al camión para ver el daño", "Mover al trabajador entre varios", "Acercarse o mover a la persona puede causar más daño."),
        ("=", "{F} Un juego de EPP cuesta $22.000 (de ejemplo). ¿Cuánto cuestan los de 8 trabajadores?", "8*22000", "Se multiplica el valor de un juego por los trabajadores.", " pesos"),
        ("abc", "{F} Para el riesgo de atropello por camiones, ¿qué medida está más arriba en la jerarquía de controles?", "Separar el paso de personas y de camiones, por ejemplo con zonas delimitadas", "Dar casco y esperar que no ocurra", "Pedir que las personas miren más", "Reducir el peligro en su origen va antes que depender de las personas o los EPP."),
        ("abc", "{F} Un trabajador quiere sacarse los guantes impermeables porque «molestan». ¿Qué corresponde?", "Usarlos, porque la especificación los pide para el contacto con hormigón fresco", "Sacárselos si hace calor", "Sacárselos si el supervisor no mira", "El EPP pedido se usa siempre."),
        ("=", "{F} Si la obra recibe 3 camiones mixer de 6 m³ de ejemplo cada uno, ¿cuántos m³ llegan?", "3*6", "Se multiplican los camiones por los m³ de cada uno.", " m³"),
        ("abc", "{F} Un vecino pide que le «regalen» las sobras de hormigón fresco para una vereda. ¿Qué corresponde?", "Rechazarlo y consultar al jefe de obra por el manejo de sobrantes según la norma vigente", "Entregárselas si las busca él", "Dejarlas en la calle", "Los sobrantes tienen manejo reglado; no se entregan ni se botan en la calle."),
    ],
    ctx=("abc", "Un amigo ofrece pagar a un estudiante por «tirar un poco de hormigón» en su patio. ¿Qué responde?", "Agradece, explica que no está autorizado y sugiere contratar a personal calificado", "Acepta si cobra poco", "Acepta porque conoce el vocabulario", "Colocar hormigón exige autorización y norma vigente; el cuaderno no habilita."),
    sc=[
        ("En Construcción: ¿qué es el hormigón fresco?", "El hormigón que todavía está blando", "Después de un tiempo el hormigón fresco endurece y se vuelve sólido."),
        ("¿Cuál es la diferencia entre premezclado y preparado en obra?", "El premezclado viene de una planta y el otro se mezcla en la obra", "El lugar donde se mezcla distingue los dos tipos."),
        ("¿Quién ejecuta un hormigonado?", "Personal autorizado, con norma vigente y EPP", "Este cuaderno no habilita para ejecutar."),
    ],
    op=("Obra de ejemplo «Taller Litre»: se pide hormigón premezclado para un sobrecimiento; llegan 2 camiones de 7 m³ cada uno; trabajan 6 personas con 4 EPP cada una. Escribe (a) cuántos m³ llegan, (b) cuántos EPP se necesitan, (c) un riesgo del contacto con hormigón fresco y (d) qué haces si ves un trabajador atrapado por un camión.",
        "(a) 2 por 7 son 14 m³. (b) 6 por 4 son 24 EPP. (c) Irritación de la piel o de los ojos. (d) No me acerco a la zona de riesgo, aviso a un adulto responsable y a emergencias.",
        ["calcula los m³", "calcula los EPP", "nombra un riesgo", "aplica la regla ante un accidente"],
        ["hoja con las cuatro respuestas"],
        ["acercarse al accidente", "confundir m³ con camiones", "olvidar los EPP"],
        "Pregunta: «¿qué haces ante un atrapamiento?». Si no responde, pídele que relea la regla de no acercarse."),
    reinforce="Escribe los dos tipos de hormigón que conociste y una diferencia entre ellos.",
    extend="Explica con un ejemplo inventado por qué se separan las zonas de personas y de camiones en una obra.",
)

# ============================================================ OAM-02, clase 2
F = ("Ficha 2 (guía de despacho descrita por escrito, de ejemplo, inventada). Obra «Casa Quillay» (ficticia). Especificación de ejemplo: hormigón tipo H-A. Regla de ejemplo: el hormigón debe descargarse dentro de 90 minutos desde su salida de la planta. "
     "Camión 1: tipo H-A, 6 m³, salida 09:00, llegada 09:40. Camión 2: tipo H-A, 6 m³, salida 10:00, llegada 11:45. "
     "Roles: el proveedor despacha; el conductor entrega la guía; el jefe de obra recibe; el inspector técnico verifica con la especificación y decide con el jefe de obra si se acepta o se rechaza.")
build(
    O2, 2, F,
    use="Aprenderé a leer una guía de despacho de hormigón premezclado, a comparar el tipo y el plazo con la especificación y a reconocer los roles de la recepción.",
    prior=["Sé qué es el hormigón premezclado.", "Sé restar horas en minutos.", "Sé que un documento no se altera."],
    explain=[
        "La guía de despacho de hormigón premezclado acompaña a cada camión y dice, entre otros datos, el tipo de hormigón, el volumen en metros cúbicos (m³), la hora de salida de la planta y la hora de llegada a la obra. El tipo es el nombre con que el proveedor identifica el hormigón pedido; debe coincidir con el que pide la especificación técnica. El plazo de descarga es el tiempo máximo que fija la especificación entre la salida y la descarga, porque el hormigón fresco empieza a endurecer con el paso del tiempo.",
        "Para revisar una guía se comparan tres cosas: tipo, volumen y tiempo transcurrido. Para calcular el tiempo se restan las horas y se expresan en minutos. Si algo no cumple, el conductor no decide; el inspector técnico y el jefe de obra deciden si se acepta o se rechaza el camión, y lo dejan registrado. Las cifras de esta clase son de ejemplo: las reales las fija la norma vigente y el proyecto.",
        f"Esto es solo lectura de documentos. {EMER} {AVISO}",
    ],
    vocab=[("guía de despacho", "documento que acompaña cada camión con tipo, volumen y horas"), ("tipo de hormigón", "nombre con que se identifica el hormigón pedido"), ("m³", "metro cúbico, unidad de volumen"), ("plazo de descarga", "tiempo máximo entre la salida de planta y la descarga"), ("aceptar o rechazar", "decidir si lo entregado cumple o no la especificación"), ("proveedor", "empresa que despacha el hormigón")],
    worked=[
        ("Calcular el tiempo", "Un camión de ejemplo sale a las 08:15 y llega a las 09:05. ¿Cuántos minutos pasaron?", ["De 08:15 a 09:00 son 45 minutos.", "De 09:00 a 09:05 son 5 minutos más: 50."], "50 minutos"),
        ("Comparar el tipo", "Una especificación de ejemplo pide tipo H-C y la guía trae tipo H-D. ¿Coinciden?", ["Se comparan los nombres de tipo.", "H-C y H-D son distintos."], "No coinciden"),
    ],
    mistakes=[("Aceptar un camión porque el conductor dice que «siempre llega así».", "La decisión se toma con la especificación y el registro, no con la palabra del conductor.", "Revisa tipo, volumen y tiempo, e informa al inspector."),
              ("Restar solo las horas e ignorar los minutos.", "El tiempo se cuenta en minutos totales.", "Convierte las horas a minutos antes de restar.")],
    T=[
        ("abc", "En Construcción: ¿qué dice la guía de despacho de un hormigón premezclado?", "Tipo, volumen y horas de salida y llegada del camión", "El nombre de los trabajadores de la obra", "El plano de la fundación", "La guía acompaña al camión con los datos de su carga."),
        ("abc", "En Construcción: ¿para qué sirve el plazo de descarga?", "Para limitar el tiempo transcurrido desde la salida, porque el hormigón fresco empieza a endurecer", "Para decidir la hora del almuerzo", "Para calcular el sueldo del conductor", "El hormigón fresco cambia con el tiempo, por eso se limita."),
        ("abc", "¿Quién decide aceptar o rechazar un camión que no cumple?", "El inspector técnico junto con el jefe de obra, con registro", "El conductor, para ahorrar tiempo", "El proveedor, porque es dueño del hormigón", "La decisión la toman quienes verifican con la especificación."),
        ("=", "{F} ¿Cuántos minutos pasaron entre la salida y la llegada del camión 1?", "(9*60+40)-(9*60)", "De 09:00 a 09:40 hay 40 minutos.", " minutos"),
        ("=", "{F} ¿Cuántos minutos pasaron entre la salida y la llegada del camión 2?", "(11*60+45)-(10*60)", "Se pasan las horas a minutos y se restan.", " minutos"),
        ("abc", "{F} ¿Cumple el camión 1 el plazo de descarga?", "Sí: 40 minutos es menos de 90", "No: 40 minutos es poco tiempo", "No se puede saber", "El plazo máximo es 90 minutos y el camión 1 usó 40."),
        ("abc", "{F} ¿Cumple el camión 2 el plazo de descarga?", "No: 105 minutos pasan los 90", "Sí: la guía dice H-A", "Sí: 105 es mayor que 90", "El tiempo transcurrido supera el plazo, aunque el tipo coincide."),
        ("=", "{F} ¿Cuántos m³ trae la guía de los dos camiones en total?", "6+6", "Se suman los m³ de cada camión.", " m³"),
        ("ab", "{F} El conductor del camión 2 dice: «el hormigón está bien, descárguenlo». ¿Qué respuesta es correcta?", "No: se informa al inspector técnico, que decide con el jefe de obra y deja registro", "Sí: el conductor conoce su camión", "La decisión se toma con la especificación y el registro, no con la opinión del conductor."),
        ("abc", "{F} ¿Qué dato debe coincidir con la especificación además del plazo?", "El tipo de hormigón", "El color del camión", "El nombre del conductor", "La especificación pide el tipo H-A y la guía debe traerlo."),
        ("=", "{F} Si el hormigón cuesta $95.000 por m³ (de ejemplo) y solo se acepta el camión 1, ¿cuánto se paga?", "6*95000", "Se multiplican los m³ aceptados por el precio por m³.", " pesos"),
        ("abc", "{F} Otro camión llega con una guía de tipo H-B. ¿Qué corresponde?", "No descargar, dejar constancia e informar al inspector técnico", "Descargar para no perder tiempo", "Cambiar el tipo en la guía a H-A", "La guía no coincide con la especificación y se informa antes de aceptar."),
        ("abc", "Un talud de un corte cercano se derrumba y atrapa a un trabajador. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Entrar a cavar para sacarlo", "Esperar a que se mueva solo", "Acercarse a la zona de riesgo puede provocar otro derrumbe."),
    ],
    ctx=("abc", "El proveedor de ejemplo pide al jefe de obra que firme la guía sin revisarla porque «el camión se retrasa en otra entrega». ¿Qué corresponde?", "Revisar tipo, volumen y tiempo antes de firmar", "Firmar para no atrasarlos", "Firmar y revisar después", "La firma confirma lo recibido y solo se da después de revisar."),
    sc=[
        ("En Construcción: ¿qué es el tipo de hormigón?", "El nombre con que se identifica el hormigón pedido", "Debe coincidir con el que pide la especificación."),
        ("¿Por qué existe un plazo de descarga?", "Porque el hormigón fresco empieza a endurecer con el tiempo", "Por eso se limita el tiempo desde la salida."),
        ("¿Quién decide si se rechaza un camión?", "El inspector técnico con el jefe de obra", "El conductor no decide por la obra."),
    ],
    op=("Guía de ejemplo: pedido H-C; camión X, tipo H-C, 5 m³, salida 14:00, llegada 14:50; camión Y, tipo H-C, 5 m³, salida 14:20, llegada 16:05. Plazo de ejemplo de 90 minutos. Escribe (a) el tiempo de cada camión, (b) cuál cumple, (c) cuántos m³ se aceptan, (d) a quién informas lo del otro camión.",
        "(a) X: 50 minutos; Y: 105 minutos. (b) X cumple; Y no. (c) 5 m³. (d) Al inspector técnico y al jefe de obra, que deciden y dejan registro.",
        ["calcula los dos tiempos", "compara con el plazo", "acepta solo lo que cumple", "informa a quien decide"],
        ["hoja con las cuatro respuestas"],
        ["no pasar las horas a minutos", "aceptar Y", "decidir sin informar"],
        "Pregunta: «¿cuánto tiempo pasó para Y?». Si no responde, pídele que pase las horas a minutos."),
    reinforce="Inventa una guía de dos camiones con una salida y una llegada y calcula los minutos de cada uno.",
    extend="Explica por qué el plazo de descarga protege la calidad del hormigón y la seguridad de la obra.",
)

# ============================================================ OAM-02, clase 3
F = ("Ficha 3 (registro de recepción de ejemplo, inventado). Obra «Liceo Cardenal» (ficticia). Pedido: 24 m³ de hormigón tipo H-A. Plazo de descarga de ejemplo: 90 minutos. "
     "Camión C1: H-A, 6 m³, 50 minutos, firmado por el jefe de obra. Camión C2: H-A, 6 m³, 95 minutos, firmado. Camión C3: H-B, 6 m³, 40 minutos, sin firma. Camión C4: H-A, 6 m³, 70 minutos, firmado. "
     "Criterio de ejemplo: un camión se acepta si el tipo coincide y el tiempo está dentro del plazo; los demás quedan observados y se informan al inspector técnico.")
build(
    O2, 3, F,
    use="Analizaré en papel un registro de recepción de camiones de hormigón, identificaré cuáles se aceptan y cuántos m³ faltan por completar el pedido.",
    prior=["Sé leer una guía de despacho.", "Sé qué es un camión observado.", "Sé sumar y restar enteros."],
    explain=[
        "El registro de recepción reúne, en una tabla, los camiones que llegan: tipo, volumen, tiempo y firma. Con él se verifica cada camión contra la especificación y se calcula cuánto del pedido se cumplió. Se acepta el camión que cumple los criterios; el que no cumple queda observado, se informa y no se descarga mientras el inspector técnico no decida. También se compara el total aceptado con el pedido: la diferencia es lo que falta por recibir.",
        "Un buen registro permite reconstruir qué se recibió y qué se rechazó. Por eso se anota todo, también lo que se rechaza, y se mantiene la trazabilidad: cada camión puede relacionarse con la parte de la obra donde se usó. Nadie anota por memoria ni cambia datos después. Este análisis se hace en papel y no enseña a descargar ni a colocar hormigón.",
        f"Los datos son de ejemplo. {EMER} {AVISO}",
    ],
    vocab=[("registro de recepción", "tabla con tipo, volumen, tiempo y firma de cada camión que llega"), ("camión observado", "camión que no cumple algún criterio y se informa"), ("pedido", "volumen total solicitado al proveedor"), ("faltante", "diferencia entre lo pedido y lo aceptado"), ("trazabilidad", "posibilidad de relacionar cada camión con la parte de la obra donde se usó")],
    worked=[
        ("Aceptar o no", "Un camión de ejemplo trae tipo H-A, llega a los 80 minutos y el plazo es 90. El pedido es H-A. ¿Se acepta?", ["El tipo coincide.", "80 minutos está dentro de 90: se acepta."], "Sí, se acepta"),
        ("Calcular el faltante", "Un pedido de ejemplo es de 18 m³ y se aceptaron 12 m³. ¿Cuánto falta?", ["Se resta lo aceptado al pedido.", "18 menos 12 son 6."], "6 m³"),
    ],
    mistakes=[("Contar un camión rechazado como recibido.", "Solo cuenta lo aceptado que se usó.", "Suma solo los camiones aceptados."),
              ("No anotar el camión rechazado para que el registro se vea limpio.", "Sin ese registro se pierde la trazabilidad.", "Anota también lo rechazado, con el motivo.")],
    T=[
        ("abc", "En Construcción: ¿qué es el faltante de un pedido de hormigón?", "La diferencia entre lo pedido y lo aceptado", "La suma de todos los camiones", "El volumen que se rechazó", "El faltante es lo que todavía no se recibió bien."),
        ("abc", "En Construcción: ¿qué es la trazabilidad de un camión?", "Poder relacionarlo con la parte de la obra donde se usó", "La velocidad con que viaja", "El color con que se pinta", "La trazabilidad permite saber dónde terminó cada camión."),
        ("abc", "¿Se anota en el registro un camión que fue rechazado?", "Sí, con el motivo", "No, porque no se usó", "Solo si el conductor lo pide", "El registro conserva también lo rechazado para reconstruir los hechos."),
        ("abc", "{F} ¿Qué camiones se aceptan según el criterio?", "C1 y C4", "C1, C2 y C4", "C1, C3 y C4", "C2 pasa el plazo de 90 minutos y C3 es tipo H-B."),
        ("abc", "{F} ¿Por qué queda observado el camión C2?", "Porque pasaron 95 minutos y el plazo es de 90", "Porque trae tipo H-B", "Porque no trae volumen", "C2 es tipo H-A, pero superó el plazo."),
        ("abc", "{F} ¿Por qué queda observado el camión C3?", "Porque es de tipo H-B y se pidió H-A", "Porque llegó muy rápido", "Porque trae muchos m³", "El tipo no coincide con el pedido."),
        ("=", "{F} ¿Cuántos m³ aceptados hay en total?", "6+6", "Se suman los m³ de C1 y C4.", " m³"),
        ("=", "{F} ¿Cuántos m³ faltan para completar el pedido?", "24-(6+6)", "Se resta lo aceptado al pedido.", " m³"),
        ("=", "{F} ¿Cuántos minutos le sobraron al camión C4 respecto del plazo?", "90-70", "Se resta el tiempo usado al plazo de 90.", " minutos"),
        ("ab", "{F} Un compañero dice: «C2 solo se pasó 5 minutos, lo aceptamos y listo». ¿Qué respuesta es correcta?", "No: se informa; la decisión la toman el inspector técnico y el jefe de obra con registro", "Sí: 5 minutos no importan", "Un plazo es un criterio de calidad y su excepción no la decide un compañero."),
        ("abc", "{F} Falta la firma del jefe de obra en C3. ¿Qué corresponde?", "Dejar constancia de que no se firmó porque quedó observado", "Firmar después, aunque se rechace", "Pedir al conductor que firme en su lugar", "La firma confirma la aceptación; un camión observado no se firma."),
        ("=", "{F} Si el hormigón cuesta $95.000 por m³ (de ejemplo) y solo se paga lo aceptado, ¿cuánto se paga?", "(6+6)*95000", "Se multiplican los m³ aceptados por el precio.", " pesos"),
        ("abc", "{F} Para reponer los m³ que faltan, ¿qué se hace?", "Pedir un nuevo despacho al proveedor, con su guía y su registro", "Usar el hormigón rechazado", "Reducir el pedido sin avisar", "El faltante se repone con una nueva entrega que pase por el mismo registro."),
    ],
    ctx=("abc", "El conductor de C3 pide que lo acepten «solo esta vez» porque el tipo es parecido. ¿Qué corresponde?", "Rechazarlo, dejar constancia e informar al inspector técnico", "Aceptarlo y avisar después", "Aceptar la mitad del camión", "El tipo debe coincidir con la especificación; las excepciones no las decide el conductor."),
    sc=[
        ("En Construcción: ¿cómo se calcula el faltante?", "Pedido menos lo aceptado", "Se resta lo aceptado al total pedido."),
        ("¿Qué camiones se aceptan?", "Los que cumplen tipo y plazo", "El criterio exige las dos condiciones."),
        ("¿Se anota lo rechazado?", "Sí, con el motivo", "Así se conserva la trazabilidad completa."),
    ],
    op=("Pedido de ejemplo: 20 m³ tipo H-C. Plazo de 90 minutos. Camión 1: H-C, 5 m³, 60 minutos; camión 2: H-C, 5 m³, 100 minutos; camión 3: H-D, 5 m³, 30 minutos; camión 4: H-C, 5 m³, 85 minutos. Escribe (a) qué camiones se aceptan, (b) cuántos m³ aceptados hay, (c) cuánto falta del pedido, (d) qué haces con los camiones observados.",
        "(a) Los camiones 1 y 4. (b) 10 m³. (c) 20-10 son 10 m³. (d) Dejo constancia del motivo (plazo y tipo), no los descargo e informo al inspector técnico.",
        ["acepta solo los correctos", "suma los m³", "calcula el faltante", "informa lo observado"],
        ["hoja con las cuatro respuestas"],
        ["aceptar el camión 2", "aceptar el camión 3", "olvidar el faltante"],
        "Pregunta: «¿qué dos condiciones se revisan?». Si no responde, pídele que relea el criterio."),
    reinforce="Inventa un registro de tres camiones con un camión observado y calcula el faltante.",
    extend="Explica por qué un registro que anota también lo rechazado protege a la obra ante un reclamo.",
)

# ============================================================ OAM-02, clase 4
F = ("Ficha 4 (cubicación de ejemplo, inventada). Obra «Posta Radal» (ficticia). Volumen de un elemento = largo por ancho por alto. Elementos: fundación, 12 m de largo, 2 m de ancho y 1 m de alto; "
     "sobrecimiento, 12 m de largo, 1 m de ancho y 1 m de alto; 4 pilares, cada uno de 1 m de largo, 1 m de ancho y 1 m de alto. Desperdicio de ejemplo: 5 % sobre el total. "
     "Camión mixer de ejemplo: 6 m³. Precio de ejemplo: $95.000 por m³.")
build(
    O2, 4, F,
    use="Aplicaré criterios de ejemplo para cubicar el hormigón de una obra, agregar el desperdicio, calcular camiones y costo en una planilla.",
    prior=["Sé multiplicar enteros.", "Sé calcular un porcentaje simple.", "Sé qué es un camión mixer."],
    explain=[
        "Cubicar el hormigón es calcular cuántos metros cúbicos (m³) se necesitan. Para un elemento con forma de caja, el volumen es el largo por el ancho por el alto, todos en metros. Se calcula cada elemento, se suman los volúmenes y se obtiene el total teórico. Como en toda obra hay pérdidas y sobrantes, se agrega un desperdicio, que es un porcentaje del total: se multiplica el total por el porcentaje y se divide por 100.",
        "Con el total pedido se calcula cuántos camiones se necesitan: se divide el volumen entre la capacidad de un camión y, si sobra, se cuenta un camión más. El costo es el volumen pedido por el precio por m³. Estos cálculos se hacen en planilla y con datos de ejemplo; los valores reales los fija el proyecto, y la forma de ejecutar el trabajo la define la norma vigente y personal autorizado.",
        f"Esta clase no enseña a preparar ni a colocar hormigón. {EMER} {AVISO}",
    ],
    vocab=[("volumen", "espacio que ocupa un cuerpo; en una caja es largo por ancho por alto"), ("m³", "metro cúbico, unidad de volumen"), ("cubicación", "cálculo de las cantidades de material"), ("desperdicio", "porcentaje extra que se agrega por pérdidas y sobrantes"), ("capacidad de un camión", "volumen que transporta un camión mixer")],
    worked=[
        ("Volumen de una caja", "Un elemento de ejemplo mide 5 m de largo, 2 m de ancho y 1 m de alto. ¿Cuál es su volumen?", ["Se multiplican las tres medidas.", "5 por 2 por 1 son 10."], "10 m³"),
        ("Camiones necesarios", "Una obra de ejemplo necesita 14 m³ y los camiones llevan 6 m³. ¿Cuántos camiones se piden?", ["14 dividido por 6 da 2 y sobran 2 m³.", "Como sobra, se cuenta un camión más: 3."], "3 camiones"),
    ],
    mistakes=[("Sumar largo, ancho y alto en vez de multiplicarlos.", "El volumen es largo por ancho por alto.", "Multiplica las tres medidas."),
              ("Redondear hacia abajo el número de camiones.", "Faltaría hormigón para terminar el elemento.", "Si sobra volumen, cuenta un camión más.")],
    T=[
        ("abc", "En Construcción: ¿cómo se calcula el volumen de un elemento con forma de caja?", "Largo por ancho por alto", "Largo más ancho más alto", "Largo por 3", "El volumen de una caja es el producto de sus tres medidas."),
        ("abc", "En Construcción: ¿qué es el desperdicio en una cubicación?", "Un porcentaje extra que se agrega por pérdidas y sobrantes", "El hormigón que se bota a propósito", "El precio del hormigón", "El desperdicio compensa lo que se pierde."),
        ("abc", "Si al dividir el volumen entre la capacidad de un camión sobra un poco, ¿cuántos camiones se piden?", "Uno más del cociente", "Uno menos del cociente", "Exactamente el cociente", "Si sobra, un camión más evita que falte hormigón."),
        ("=", "{F} ¿Cuál es el volumen de la fundación?", "12*2*1", "Se multiplican largo, ancho y alto.", " m³"),
        ("=", "{F} ¿Cuál es el volumen del sobrecimiento?", "12*1*1", "Se multiplican largo, ancho y alto.", " m³"),
        ("=", "{F} ¿Cuál es el volumen de los 4 pilares juntos?", "4*1*1*1", "Se multiplica la cantidad de pilares por el volumen de cada uno.", " m³"),
        ("=", "{F} ¿Cuál es el volumen total teórico de la obra?", "12*2*1+12*1*1+4*1*1*1", "Se suman los volúmenes de la fundación, el sobrecimiento y los pilares.", " m³"),
        ("=", "{F} ¿Cuántos m³ son el desperdicio del 5 %?", "(12*2*1+12*1*1+4*1*1*1)*5//100", "Se multiplica el total por 5 y se divide por 100.", " m³"),
        ("=", "{F} ¿Cuántos m³ se piden, sumando el desperdicio?", "(12*2*1+12*1*1+4*1*1*1)*105//100", "Se suma el desperdicio al total teórico.", " m³"),
        ("=", "{F} ¿Cuántos camiones de 6 m³ se necesitan para esos m³?", "((12*2*1+12*1*1+4*1*1*1)*105//100+5)//6", "Se divide el pedido entre la capacidad del camión.", " camiones"),
        ("=", "{F} ¿Cuánto cuesta el hormigón pedido?", "(12*2*1+12*1*1+4*1*1*1)*105//100*95000", "Se multiplican los m³ pedidos por el precio por m³.", " pesos"),
        ("ab", "{F} Una compañera pide solo los 40 m³ teóricos, «sin desperdicio». ¿Qué respuesta es correcta?", "No: se agrega el desperdicio, porque siempre hay pérdidas y sobrantes", "Sí: lo teórico basta siempre", "Sin desperdicio puede faltar hormigón al terminar el trabajo."),
        ("abc", "Una pared de un corte se desprende y atrapa a un trabajador. ¿Qué se hace según las reglas generales?", "No acercarse a la zona de riesgo, avisar a un adulto responsable y a emergencias", "Cavar para sacarlo", "Esperar a que salga solo", "Acercarse a la zona de riesgo puede provocar otro desprendimiento."),
    ],
    ctx=("abc", "Una jefa de obra de ejemplo duda entre pedir 6 o 7 camiones de 6 m³ para un pedido de 36 m³. ¿Qué corresponde?", "Pedir 6, porque 36 dividido por 6 da exactamente 6 camiones", "Pedir 7, porque siempre se agrega uno más", "Pedir 5, para ahorrar", "La división es exacta: ni sobra volumen ni falta, y no se agrega un camión sin motivo."),
    sc=[
        ("En Construcción: ¿qué se multiplica para el volumen de una caja?", "Largo, ancho y alto", "Las tres medidas dan el espacio que ocupa."),
        ("¿Cómo se agrega el desperdicio?", "Se calcula el porcentaje del total y se suma", "El pedido final es el total teórico más el desperdicio."),
        ("¿Quién ejecuta el hormigonado?", "Personal autorizado, con norma vigente", "Este cuaderno no habilita para ejecutar."),
    ],
    op=("Obra de ejemplo «Taller Hualle»: un muro de hormigón de 10 m de largo, 2 m de alto y 1 m de espesor (ancho). Desperdicio de ejemplo 10 %; camiones de 6 m³; precio de ejemplo $90.000 por m³. Escribe (a) el volumen teórico, (b) el desperdicio, (c) el volumen pedido, (d) cuántos camiones y cuánto cuesta.",
        "(a) 10 por 2 por 1 son 20 m³. (b) El 10 % de 20 es 2 m³. (c) 22 m³. (d) 22 dividido por 6 da 3 y sobran 4: son 4 camiones; el costo es 22 por 90.000 = 1.980.000 pesos.",
        ["calcula el volumen", "calcula el desperdicio", "suma el pedido", "calcula camiones y costo"],
        ["hoja con las cuatro respuestas"],
        ["sumar las medidas", "olvidar el desperdicio", "redondear camiones hacia abajo"],
        "Pregunta: «¿qué haces si sobra al dividir?». Si no responde, pídele que relea la regla de los camiones."),
    reinforce="Calcula el volumen de una caja de hormigón de 6 m por 3 m por 1 m y cuántos camiones de 6 m³ se necesitan.",
    extend="Explica por qué un error en la cubicación puede producir atrasos o gastos extra en una obra.",
)

# ============================================================ OAM-02, clase 5
F = ("Ficha 5 (comparación y control de calidad, de ejemplo, inventados). Obra «Sede Maitén» (ficticia), 20 m³ de hormigón. Alternativa A: hormigón premezclado a $95.000 por m³. "
     "Alternativa B: hormigón preparado en obra: materiales a $60.000 por m³, 10 jornadas de mano de obra a $30.000 cada una y arriendo de equipos por $250.000. "
     "Control de calidad de ejemplo por camión o por tanda: 1) documento de origen revisado; 2) tipo correcto; 3) tiempo dentro del plazo; 4) muestra rotulada; 5) firma del inspector técnico. "
     "Registro de ejemplo de 4 entregas: 20 ítems revisados; 18 cumplen; 2 no cumplen.")
build(
    O2, 5, F,
    use="Compararé hormigón premezclado y preparado en obra por costo, riesgo y control de calidad, y leeré un registro de control.",
    prior=["Sé qué es el hormigón premezclado y el preparado en obra.", "Sé calcular costos con precio por m³.", "Sé qué es una lista de verificación."],
    explain=[
        "Elegir entre hormigón premezclado y preparado en obra exige comparar varios criterios. El costo incluye el material, la mano de obra y los equipos. El riesgo cambia: con el hormigón preparado en obra hay más personas expuestas al polvo de cemento y al manejo de cargas durante más horas; con el premezclado hay más movimiento de camiones. El control de calidad también cambia: en el premezclado el proveedor entrega una guía, y en el preparado en obra la obra debe documentar más.",
        "El control de calidad se anota en un registro: cada ítem revisado queda en cumple o no cumple. El porcentaje de cumplimiento es la cantidad de ítems que cumplen dividida entre los revisados, por 100. Un ítem que no cumple se informa y se corrige con registro, no se oculta. Los datos y los precios son de ejemplo; este cuaderno no explica cómo preparar hormigón ni sus proporciones.",
        f"{EMER} {AVISO}",
    ],
    vocab=[("jornada", "día de trabajo de una persona"), ("arriendo de equipos", "costo de alquilar equipos por un período"), ("criterio de comparación", "aspecto con que se comparan alternativas"), ("porcentaje de cumplimiento", "ítems que cumplen divididos entre los revisados, por 100"), ("control de calidad", "revisiones registradas para comprobar que se cumple la especificación")],
    worked=[
        ("Comparar costos", "Alternativa A de ejemplo: 10 m³ a $100.000 cada uno. Alternativa B: materiales por $700.000 más mano de obra por $400.000. ¿Cuál cuesta menos?", ["A cuesta 10 por 100.000 = 1.000.000.", "B cuesta 700.000+400.000 = 1.100.000."], "La alternativa A"),
        ("Porcentaje", "En un registro de ejemplo 9 de 10 ítems cumplen. ¿Qué porcentaje de cumplimiento hay?", ["9 dividido por 10 es 0,9.", "Por 100 son 90."], "90 %"),
    ],
    mistakes=[("Elegir la alternativa solo por el costo.", "El riesgo y la calidad también cuentan.", "Compara costo, riesgo, plazo y control de calidad."),
              ("Ocultar un ítem que no cumple para mejorar el porcentaje.", "Un defecto oculto puede dañar la obra después.", "Informa el ítem y corrígelo con registro.")],
    T=[
        ("abc", "En hormigón premezclado: ¿qué es un criterio de comparación?", "Un aspecto con el que se comparan alternativas, como costo o riesgo", "Una herramienta para medir distancias", "El nombre del proveedor", "Un criterio es un aspecto de comparación; no es un instrumento."),
        ("abc", "En Construcción: ¿qué es el control de calidad de un hormigón?", "Revisiones registradas para comprobar que se cumple la especificación", "El precio del hormigón", "El color final del muro", "El control de calidad verifica y deja registro."),
        ("abc", "¿Cómo se calcula el porcentaje de cumplimiento?", "Ítems que cumplen divididos entre los revisados, por 100", "Ítems revisados menos ítems que no cumplen", "Ítems que no cumplen por 100", "El porcentaje relaciona los ítems que cumplen con los revisados."),
        ("=", "{F} ¿Cuánto cuesta el hormigón de la alternativa A?", "20*95000", "Se multiplican los m³ por el precio por m³.", " pesos"),
        ("=", "{F} ¿Cuánto cuestan los materiales de la alternativa B?", "20*60000", "Se multiplican los m³ por el precio de los materiales.", " pesos"),
        ("=", "{F} ¿Cuánto cuesta en total la alternativa B?", "20*60000+10*30000+250000", "Se suman materiales, mano de obra y arriendo.", " pesos"),
        ("abc", "{F} Comparando solo los costos, ¿qué alternativa cuesta menos?", "La alternativa B, con $1.750.000 frente a $1.900.000", "La alternativa A, con $1.750.000", "Cuestan lo mismo", "A cuesta 1.900.000 y B cuesta 1.750.000."),
        ("=", "{F} ¿Cuántos pesos de diferencia hay entre las dos alternativas?", "20*95000-(20*60000+10*30000+250000)", "Se resta el costo de B al de A.", " pesos"),
        ("abc", "{F} ¿Qué criterio, además del costo, debe considerarse en la alternativa B?", "Más horas de personas expuestas al polvo de cemento y al manejo de cargas", "Menos movimiento de personas en la obra", "Una guía de despacho del proveedor", "En B se preparan los materiales en la obra con más horas de trabajo."),
        ("=", "{F} ¿Cuántos ítems revisados no cumplen en el registro?", "20-18", "Se restan los ítems que cumplen a los revisados.", " ítems"),
        ("abc", "{F} ¿Qué porcentaje de cumplimiento tiene el registro?", "90 %", "18 %", "20 %", "18 dividido por 20 es 0,9, o sea 90 sobre 100."),
        ("ab", "{F} Un jefe dice: «borremos los 2 ítems que no cumplen y quedamos en 100 %». ¿Qué respuesta es correcta?", "No: se informan y se corrigen con registro", "Sí: así el porcentaje mejora", "Un defecto oculto puede dañar la obra después y falsea el registro."),
        ("abc", "{F} Un trabajador sugiere ahorrar y no hacer el control de calidad en la alternativa B. ¿Qué corresponde?", "Rechazarlo: el control es parte de la especificación y se registra", "Aceptar si ahorra tiempo", "Aceptar si el equipo es de confianza", "El control de calidad no se elimina para ahorrar."),
    ],
    ctx=("abc", "Una constructora de ejemplo elige la alternativa más barata y descubre que no tiene personal capacitado ni autorizado para ejecutarla. ¿Qué debió hacer antes de decidir?", "Considerar también el riesgo, la autorización del personal y el control de calidad", "Mirar solo el costo", "Confiar en que alguien aprenda sobre la marcha", "Una decisión debe incluir seguridad, personal autorizado y control, no solo el costo."),
    sc=[
        ("En Construcción: ¿qué se compara además del costo?", "El riesgo, el plazo y el control de calidad", "Un solo criterio puede llevar a una mala decisión."),
        ("¿Se oculta un ítem que no cumple?", "No: se informa y se corrige con registro", "Ocultarlo deja un defecto sin controlar."),
        ("¿Quién ejecuta la preparación y colocación?", "Personal autorizado, con norma vigente", "Este cuaderno no habilita para ejecutarlas."),
    ],
    op=("Obra de ejemplo «Taller Avellano»: 10 m³ de hormigón. Alternativa A: premezclado a $100.000 por m³. Alternativa B: preparado en obra, materiales $65.000 por m³, 6 jornadas a $30.000 y arriendo de equipos por $200.000. Registro: 10 ítems revisados, 8 cumplen. Escribe (a) el costo de cada alternativa, (b) cuál es más barata, (c) un criterio no económico a considerar, (d) el porcentaje de cumplimiento y qué haces con los ítems que no cumplen.",
        "(a) A: 1.000.000 pesos; B: 650.000+180.000+200.000 = 1.030.000 pesos. (b) A. (c) El riesgo de más horas de trabajo expuestas al polvo y al manejo de cargas en B. (d) 80 %; informo los 2 ítems que no cumplen y los corrijo con registro.",
        ["calcula ambos costos", "identifica la más barata", "nombra un criterio no económico", "calcula el porcentaje e informa"],
        ["hoja con las cuatro respuestas"],
        ["olvidar el arriendo", "ocultar los ítems", "elegir solo por costo"],
        "Pregunta: «¿qué incluye el costo de B?». Si no responde, pídele que relea la ficha."),
    reinforce="Inventa dos alternativas con costos y un criterio no económico y escribe cuál elegirías y por qué.",
    extend="Explica por qué el control de calidad con registro protege tanto a las personas como al presupuesto.",
)
