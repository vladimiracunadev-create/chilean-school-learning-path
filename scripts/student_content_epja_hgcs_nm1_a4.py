"""Historia, Geografía y Ciencias Sociales EPJA Media N1, módulo 1 (parte 4): OAD-04, multicausalidad de procesos globales y locales de los siglos XIX y XX y su relación con el presente. Todas las fuentes y los datos de práctica son inventados («de ejemplo») y se leen en papel."""
from __future__ import annotations

from epja_hgcs_nm1_a_common import build, PRIOR_BASE

O = "EPJA-HGCS-NM1-OAD-04"

# ======================================================= clase 1
F1 = ("Ficha 1 (de ejemplo). Una panadería de barrio cerró a fines de año. Cinco hechos anotados por la junta de vecinos: "
      "a) subió mucho el arriendo del local; "
      "b) abrió un supermercado a dos cuadras; "
      "c) la dueña enfermó y no pudo trabajar; "
      "d) los vecinos compraban cada vez más pan envasado; "
      "e) como consecuencia de todo lo anterior, hubo cinco personas sin empleo.")
build(
    O, 1, F1,
    use="Hoy aprendo que casi ningún hecho tiene una sola causa y distingo causas de consecuencias, empezando por un caso de la vida cotidiana.",
    prior=PRIOR_BASE + ["Sé distinguir un cambio de una continuidad y leer una fuente con preguntas."],
    explain=[
        "Cuando una panadería cierra, la gente suele dar una sola razón: «cerró porque no vendía». Pero si lo piensas con calma, hubo varias razones a la vez: costos más altos, competencia, enfermedad y cambios en lo que la gente compra. Eso es la multicausalidad: un hecho tiene muchas causas que actúan juntas.",
        "Una causa es una razón que ayuda a explicar por qué ocurrió algo, y una consecuencia es lo que ocurre después, como resultado. En la ficha, la subida del arriendo es una causa; las cinco personas sin empleo son una consecuencia. Para no confundirlas, pregúntate: ¿esto vino antes o después del cierre?",
        "En Historia pasa lo mismo con procesos grandes, como la industrialización o una guerra. Explicarlos con una sola causa deja afuera personas, economía y decisiones. Por eso se buscan varias causas, se distinguen unas de otras, y se evalúa cuánto pesó cada una según la evidencia.",
    ],
    vocab=[("causa", "razón que ayuda a explicar por qué ocurrió algo"), ("consecuencia", "lo que ocurre después, como resultado de un hecho"), ("multicausalidad", "idea de que un hecho tiene varias causas que actúan juntas"), ("explicación", "texto que dice por qué ocurrió algo, usando evidencia"), ("evidencia", "dato o fuente que respalda una afirmación")],
    worked=[
        ("Distinguir causa y consecuencia", "{F} ¿Cuál de los hechos es una consecuencia?", ["Una consecuencia viene después del cierre y como resultado.", "El hecho e) dice que hubo cinco personas sin empleo como consecuencia."], "El hecho e: cinco personas sin empleo"),
        ("Ver que hay varias causas", "{F} ¿Cuántas causas del cierre hay en la ficha?", ["Reviso los hechos a, b, c y d: son razones del cierre.", "El hecho e es una consecuencia, no una causa."], "Cuatro causas"),
    ],
    mistakes=[("Dar una sola causa para un hecho complejo.", "Es más cómodo y rápido explicar con una razón.", "Busca al menos tres causas y clasifícalas."),
              ("Confundir causa con consecuencia.", "Se mira lo que pasó junto al hecho sin fijarse en el orden.", "Pregunta si ocurrió antes o después del hecho.")],
    T=[
        ("abc", "{F} ¿Cuál de estos hechos es una causa del cierre?", "El arriendo del local subió mucho", "Hubo cinco personas sin empleo", "La junta de vecinos anotó los hechos", "La subida del arriendo ocurrió antes y contribuyó al cierre."),
        ("ab", "{F} ¿Cuál es una consecuencia del cierre?", "Cinco personas quedaron sin empleo", "Abrió un supermercado cerca", "El empleo perdido ocurrió como resultado del cierre."),
        ("En Historia: ¿cómo se llama la idea de que un hecho tiene varias causas?", "Multicausalidad", "La multicausalidad reconoce que varias razones actúan juntas."),
        ("=", "{F} De los 5 hechos anotados, 4 son causas del cierre. ¿Qué porcentaje de los hechos son causas?", "4*100//5", "Se divide 4 entre 5 y se multiplica por 100.", " %"),
        ("=", "{F} Cada persona sin empleo ganaba, en este ejemplo inventado, $400.000 al mes. ¿Cuánto sueldo mensual en total dejaron de recibir las cinco?", "5*400000", "Se multiplica el sueldo por el número de personas afectadas.", " pesos"),
        ("abc", "{F} ¿Qué causa se relaciona con la competencia?", "Abrió un supermercado a dos cuadras", "Subió el arriendo", "La dueña enfermó", "Un supermercado cercano es un competidor del negocio."),
        ("abc", "{F} ¿Qué causa es un cambio en las costumbres de compra?", "Los vecinos compraban más pan envasado", "La dueña enfermó", "Subió el arriendo", "Comprar más pan envasado cambia lo que se pide en la panadería."),
        ("abc", "{F} Un vecino dice: «La panadería cerró solo porque la dueña enfermó». ¿Qué falla en esa explicación?", "Ignora otras causas anotadas, como el arriendo y la competencia", "Nada: es la única causa", "Que la enfermedad es una consecuencia", "La ficha anota cuatro causas; la afirmación deja fuera las demás."),
        ("abc", "{F} ¿Qué explicación respeta la multicausalidad?", "Cerró por el alza del arriendo, la competencia, la enfermedad y los cambios de compra", "Cerró por mala suerte", "Cerró por una sola razón", "Solo esa explicación reúne varias causas de la ficha."),
        ("ab", "{F} Se discute cuál causa pesó más. ¿Qué haría falta para decidirlo?", "Más evidencia, por ejemplo cuentas del negocio", "Nada, basta una opinión", "Para decidir cuánto pesó cada causa se necesitan datos de respaldo."),
        ("abc", "{F} Un vecino afirma: «El supermercado causó el cierre porque abrió el mismo año». ¿Qué respuesta es cuidadosa?", "Pudo contribuir, pero falta evidencia de cuánto influyó", "Es seguro que fue la causa única", "Es imposible que influyera", "Abrir el mismo año muestra relación, no prueba cuánto pesó esa causa."),
        ("abc", "Estudias un proceso histórico y solo hallas una causa en tu fuente. ¿Qué haces?", "Busco otras fuentes para ver si hay más causas", "Concluyo que no hubo otras", "Elijo la causa que más me gusta", "Una fuente suele mostrar una parte; otras fuentes pueden mostrar otras causas."),
        ("abc", "{F} ¿Qué pregunta ayuda a distinguir causa de consecuencia?", "¿Ocurrió antes o después del cierre?", "¿Cuánto cuesta hoy el pan?", "¿Quién tiene más años en el barrio?", "El orden en el tiempo es un buen criterio para separar causas y consecuencias."),
    ],
    ctx=("abc", "En una reunión de la junta de vecinos de ejemplo se discute por qué bajó la asistencia a las reuniones. Se anotan: cambió el horario a las 19 horas; muchos vecinos tienen turnos hasta tarde; el local está lejos; hubo menos avisos. ¿Qué respuesta respeta la multicausalidad?", "Hubo varias razones juntas: horario, turnos, distancia y falta de avisos", "Solo el horario es la causa", "Es culpa de los vecinos", "Varias razones actúan al mismo tiempo, por eso se las considera todas."),
    sc=[("En Historia: ¿cómo se define una causa?", "Una razón que ayuda a explicar por qué ocurrió algo", "Las causas se buscan en lo que ocurrió antes del hecho."),
        ("En Historia: ¿cómo se define una consecuencia?", "Lo que ocurre después, como resultado", "Las consecuencias son lo que viene después del hecho."),
        ("¿Por qué conviene buscar varias causas?", "Porque casi ningún hecho tiene una sola", "La multicausalidad explica mejor los hechos complejos.")],
    op=("Elige uno de estos hechos de ejemplo: a) una feria del barrio dejó de funcionar; b) subió el precio de las verduras en el almacén. Escribe cuatro posibles causas, una consecuencia y una pregunta sobre qué evidencia necesitarías para saber cuál pesó más.",
        "Hecho: la feria dejó de funcionar. Causas posibles: faltaron puestos; cambió el permiso de la municipalidad; subió el costo del transporte; la gente prefirió comprar en el supermercado. Consecuencia: los comerciantes perdieron ingresos. Pregunta: ¿qué registro de ventas y permisos mostraría cuál causa pesó más?",
        ["entrega cuatro causas razonables", "distingue una consecuencia", "plantea qué evidencia haría falta"],
        ["una lista de causas, una consecuencia y una pregunta"], ["dar una sola causa", "confundir causa con consecuencia"],
        "Pregunta: «¿Esto pasó antes o después del hecho?»."),
    reinforce="Piensa en un hecho que hayas visto o escuchado (un cambio de horario, el cierre de un local) y anota dos causas y una consecuencia.",
    extend="Explica con un ejemplo por qué una sola causa casi nunca explica un hecho histórico.",
)

# ======================================================= clase 2
F2 = ("Ficha 2 (hechos estándar de los textos escolares, resumidos). "
      "Revolución Industrial: comenzó en Gran Bretaña a fines del siglo XVIII. Causas que suelen señalarse: había carbón y hierro cerca de las ciudades; se inventaron máquinas, como la máquina de vapor; había mercados dentro del imperio y en las colonias para vender telas; había personas que pasaron del campo a la ciudad y buscaban trabajo; y había dinero disponible para invertir en fábricas. "
      "Guerra del Pacífico (1879-1884): Chile enfrentó a Perú y Bolivia. Causas que suelen señalarse: disputa por los recursos del desierto, como el salitre; límites poco claros en esa zona; una alianza entre Perú y Bolivia firmada en 1873; y, como hecho que desató el conflicto en 1879, la ocupación chilena de Antofagasta tras una disputa por un impuesto boliviano a una empresa.")
build(
    O, 2, F2,
    use="Hoy aprendo a reconocer tipos de causas (económicas, políticas, sociales, tecnológicas) y a distinguir las causas de largo plazo del hecho que desata un proceso.",
    prior=PRIOR_BASE + ["Sé distinguir causa y consecuencia y sé que un hecho puede tener varias causas."],
    explain=[
        "Las causas se pueden clasificar según su tipo. Las económicas tienen que ver con el dinero, los recursos y el comercio. Las políticas, con el poder, las alianzas y las decisiones de gobierno. Las sociales, con los grupos de personas y sus condiciones de vida. Las tecnológicas, con las máquinas y los inventos. Muchas causas son de más de un tipo a la vez.",
        "También se distinguen por el tiempo. Una causa de largo plazo actúa durante años, como la falta de claridad en los límites antes de una guerra. Un detonante, o hecho desencadenante, es el suceso concreto que hace estallar el proceso, como la ocupación de Antofagasta en 1879. Sin las causas de fondo, el detonante habría tenido otro resultado.",
        "Este cuadro de causas ayuda a que una explicación no se quede en un solo aspecto. Para un proceso global, como la Revolución Industrial, y para uno local, como un conflicto en una región, se pueden usar las mismas preguntas: ¿qué causas económicas hubo?, ¿políticas?, ¿sociales?, ¿cuál fue el detonante?",
    ],
    vocab=[("causa económica", "razón relacionada con dinero, recursos y comercio"), ("causa política", "razón relacionada con poder, alianzas y decisiones de gobierno"), ("causa de largo plazo", "razón que actúa durante muchos años"), ("detonante", "hecho concreto que desata un proceso"), ("alianza", "acuerdo entre países para ayudarse")],
    worked=[
        ("Clasificar una causa", "{F} Clasifica la causa «había carbón y hierro cerca de las ciudades».", ["Habla de recursos naturales disponibles para producir.", "Los recursos y la producción son temas económicos."], "Causa económica"),
        ("Reconocer el detonante", "{F} ¿Cuál fue el detonante de la Guerra del Pacífico según la ficha?", ["El detonante es el hecho concreto que desata el conflicto.", "La ficha dice que fue la ocupación chilena de Antofagasta en 1879."], "La ocupación chilena de Antofagasta en 1879"),
    ],
    mistakes=[("Creer que el detonante es la única causa de un proceso.", "Se confunde el hecho que lo desata con todo lo que lo preparó.", "Busca las causas de largo plazo y el detonante por separado."),
              ("Clasificar cada causa en un solo tipo sin matices.", "Se piensa que los tipos son excluyentes.", "Acepta que una causa puede ser económica y política a la vez.")],
    T=[
        ("abc", "{F} ¿Dónde comenzó la Revolución Industrial?", "En Gran Bretaña", "En Chile", "En Bolivia", "La ficha dice que comenzó en Gran Bretaña a fines del siglo XVIII."),
        ("ab", "En Historia: ¿qué es un detonante?", "El hecho concreto que desata un proceso", "Una causa que actúa durante siglos", "El detonante es el suceso que hace estallar un proceso."),
        ("{F} ¿Qué alianza se firmó en 1873?", "Una alianza entre Perú y Bolivia", "La ficha indica una alianza entre Perú y Bolivia firmada en 1873."),
        ("abc", "{F} ¿Qué tipo de causa es la invención de la máquina de vapor?", "Tecnológica", "Política", "Social", "Un invento es una causa tecnológica."),
        ("abc", "{F} ¿Qué tipo de causa es la alianza entre Perú y Bolivia?", "Política", "Tecnológica", "Ambiental", "Una alianza es un acuerdo de poder entre países."),
        ("=", "{F} ¿Cuántos años pasaron entre la alianza de 1873 y el inicio de la guerra de 1879?", "1879-1873", "Se restan los años para saber cuánto tiempo pasó entre ambos hechos.", " años"),
        ("=", "{F} ¿Cuántas causas señala la ficha para la Revolución Industrial?", "5", "Se cuentan las razones enumeradas: carbón y hierro, máquinas, mercados, trabajo y dinero.", " causas"),
        ("abc", "{F} ¿Qué causa se relaciona con la sociedad?", "Personas que pasaron del campo a la ciudad buscando trabajo", "La máquina de vapor", "El carbón y el hierro", "Los movimientos de personas son un cambio social."),
        ("abc", "{F} ¿Qué causa de la guerra es económica?", "La disputa por los recursos del desierto, como el salitre", "La alianza de 1873", "Los límites poco claros", "Los recursos y su explotación son un tema económico."),
        ("abc", "{F} Un compañero dice: «La Guerra del Pacífico ocurrió solo porque Chile ocupó Antofagasta». ¿Qué falla?", "Confunde el detonante con todas las causas del conflicto", "Nada: fue la única causa", "Que la ocupación ocurrió en 1873", "El detonante es solo el hecho que desató un proceso preparado por otras causas."),
        ("ab", "{F} ¿Cuál causa actúa a largo plazo?", "Los límites poco claros en el desierto", "La ocupación de Antofagasta en 1879", "Una situación poco clara durante años es de largo plazo; la ocupación es un hecho concreto."),
        ("abc", "{F} ¿Qué causa de la Revolución Industrial se relaciona con el imperialismo y las colonias?", "Los mercados en el imperio y las colonias", "El carbón cercano a las ciudades", "El invento de la máquina", "Las colonias servían como mercados para vender telas."),
        ("abc", "{F} ¿Qué explicación del inicio de la Guerra del Pacífico es más completa?", "Hubo disputa por recursos, límites poco claros, una alianza y un hecho detonante", "Hubo una causa y ninguna más", "Solo hubo causas económicas", "Solo la primera combina varios tipos de causas y distingue el detonante."),
    ],
    ctx=("abc", "Un sindicato de ejemplo analiza por qué cerró una fábrica: «Bajó el precio internacional del producto; la maquinaria era antigua; hubo una huelga larga; un incendio obligó a detener la producción el mes del cierre». ¿Cuál es el detonante?", "El incendio del último mes", "Que la maquinaria era antigua", "La baja del precio internacional", "El incendio es el hecho concreto que desencadenó el cierre; las otras causas venían de antes."),
    sc=[("¿Qué es una causa económica?", "Una razón relacionada con dinero, recursos y comercio", "Los recursos y el comercio son temas de la economía."),
        ("¿Qué es una causa de largo plazo?", "Una razón que actúa durante muchos años", "Prepara el proceso mucho antes del hecho detonante."),
        ("¿Puede una causa ser de más de un tipo?", "Sí, por ejemplo económica y política a la vez", "Los tipos de causa no se excluyen entre sí nunca.")],
    op=("Analiza este hecho de ejemplo: «Una comunidad dejó de cultivar su ladera». Estas son las razones de ejemplo: a) el suelo se agotó con los años; b) subió el precio de las semillas; c) las personas jóvenes se fueron a trabajar a la ciudad; d) una lluvia fuerte arrastró el último cultivo. "
        "Clasifica cada razón por tipo (económica, social, ambiental) y por tiempo (largo plazo o detonante) y escribe una frase que explique el hecho usando todas.",
        "a) Ambiental y de largo plazo; b) Económica; c) Social y de largo plazo; d) Ambiental y detonante. Frase: la comunidad dejó de cultivar porque el suelo se fue agotando, subieron las semillas y se fueron las personas jóvenes, y una lluvia fuerte arrastró el último cultivo.",
        ["clasifica cada razón con un criterio", "distingue el detonante", "la frase reúne las razones"],
        ["una tabla con tipo y tiempo y una frase"], ["usar una sola causa", "tratar el detonante como la causa única"],
        "Pregunta: «¿Esta razón ya existía antes o fue lo que desató el hecho?»."),
    reinforce="Elige un hecho de la noticias de esta semana y anota una causa económica, una política y una social.",
    extend="Explica con un ejemplo por qué un hecho desencadenante no explica por sí solo un proceso largo.",
)

# ======================================================= clase 3
F3 = ("Ficha 3 (de ejemplo, inventada). Caso: el cierre de la oficina salitrera «Esperanza», ficticia, en 1930. "
      "Una asociación de ejemplo reúne 20 cartas de trabajadores y encargados y anota qué causa menciona cada carta como principal: "
      "12 cartas mencionan la caída del precio del salitre; 5 mencionan la competencia del salitre sintético; 3 mencionan el agotamiento del terreno. "
      "Datos de ejemplo del registro de la oficina: en 1920 trabajaban 1.000 personas y en 1930 trabajaban 200. "
      "Una carta de ejemplo dice: «Antes sacábamos cuatro carretas al día; ahora apenas una». Otra dice: «Los compradores dejaron de pedir nuestro producto».")
build(
    O, 3, F3,
    use="Hoy aprendo un método de cinco pasos para armar y evaluar un cuadro de causas, apoyándome en evidencia y no en opiniones.",
    prior=PRIOR_BASE + ["Sé clasificar causas por tipo y distinguir el detonante de las causas de largo plazo."],
    explain=[
        "Para explicar con varias causas hay un método de cinco pasos. Paso 1: define con claridad el hecho que quieres explicar. Paso 2: lista las causas posibles. Paso 3: clasifícalas por tipo (económicas, políticas, sociales, ambientales). Paso 4: busca evidencia para cada una. Paso 5: ordena las causas según cuánto pesaron y escribe una conclusión.",
        "La evidencia puede ser un dato (como cuántas personas trabajaban), una fuente escrita (como una carta) o un conteo (como cuántas cartas mencionan una causa). Una opinión sin respaldo no cuenta como evidencia. Pero hay que tener cuidado: contar cuántas veces se menciona una causa muestra lo que dicen las fuentes, no siempre cuánto pesó realmente.",
        "Por eso una buena conclusión es matizada: dice qué causa parece haber pesado más, qué otras ayudaron y qué evidencia falta. Esa honestidad es parte del pensamiento crítico y evita las explicaciones apresuradas.",
    ],
    vocab=[("cuadro de causas", "tabla que ordena las causas con su tipo y su evidencia"), ("evidencia", "dato o fuente que respalda una afirmación"), ("jerarquizar", "ordenar según cuánto pesa cada cosa"), ("conclusión matizada", "conclusión que reconoce lo que no se sabe"), ("pensamiento crítico", "forma de juzgar con evidencia y sin apuro")],
    worked=[
        ("Calcular un porcentaje de menciones", "{F} ¿Qué porcentaje de las cartas menciona la caída del precio como causa principal?", ["Leo los datos: 12 cartas de 20.", "Divido 12 entre 20 y multiplico por 100."], "60 %"),
        ("Medir el cambio en el empleo", "{F} ¿Cuántas personas dejaron de trabajar entre 1920 y 1930?", ["Leo los datos del registro: 1.000 y 200.", "Resto 1.000 menos 200."], "800 personas"),
    ],
    mistakes=[("Tomar la causa más mencionada como la única.", "Se confunde cantidad de menciones con prueba total.", "Reconoce que otras causas también ayudaron."),
              ("Usar una opinión como evidencia.", "Una frase convincente parece un dato.", "Pregunta qué dato o fuente respalda cada afirmación.")],
    T=[
        ("abc", "{F} ¿Cuál es el primer paso del método?", "Definir el hecho que se quiere explicar", "Escribir la conclusión", "Opinar sobre las causas", "Sin saber con claridad qué se explica, no se pueden buscar causas."),
        ("ab", "{F} ¿Cuántas cartas se reunieron?", "20", "12", "La ficha dice que se reunieron 20 cartas."),
        ("{F} ¿Cuántas personas trabajaban en la oficina en 1930?", "200", "El registro de ejemplo indica 200 personas en 1930."),
        ("=", "{F} ¿Qué porcentaje de las cartas menciona la competencia del salitre sintético?", "5*100//20", "Se divide 5 entre 20 y se multiplica por 100 para calcular el porcentaje.", " %"),
        ("=", "{F} ¿Qué porcentaje de las cartas menciona el agotamiento del terreno?", "3*100//20", "Se divide 3 entre 20 y se multiplica por 100 para calcular el porcentaje.", " %"),
        ("=", "{F} ¿Qué porcentaje del personal de 1920 seguía trabajando en 1930?", "200*100//1000", "Se divide el personal de 1930 por el de 1920 y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué causa fue mencionada por más cartas?", "La caída del precio del salitre", "La competencia del salitre sintético", "El agotamiento del terreno", "Doce cartas mencionan el precio, más que las otras causas."),
        ("abc", "{F} ¿Qué evidencia respalda la causa «bajaron los compradores»?", "La carta que dice que los compradores dejaron de pedir el producto", "El número de carretas", "El título de la ficha", "Esa carta menciona directamente la baja de compradores."),
        ("abc", "{F} ¿Qué dato respalda que la producción cayó?", "Antes se sacaban cuatro carretas al día y ahora una", "Que 12 cartas mencionan el precio", "Que el registro es de 1920", "La carta compara la producción antes y después."),
        ("abc", "{F} Una persona dice: «Como 12 cartas mencionan el precio, el precio fue la única causa». ¿Qué falla?", "Ignora las otras causas mencionadas por 8 cartas", "Nada: 12 es la mayoría de todo", "Las cartas no sirven como fuente", "Hay 8 cartas que mencionan otras causas, por eso la causa única no se sostiene."),
        ("ab", "{F} ¿Qué conclusión es más cuidadosa?", "La caída del precio parece haber pesado más, pero también influyeron el salitre sintético y el agotamiento", "El precio fue la única causa del cierre", "Las cartas muestran que la causa principal es el precio, pero no son prueba de cuánto pesó cada causa; hay otras."),
        ("abc", "{F} ¿Qué evidencia ayudaría a verificar cuánto pesó el salitre sintético?", "Datos de ventas del producto antes y después de su aparición", "Una opinión sin fuente sobre el salitre sintético", "El número de cartas reunidas", "Los datos de ventas permiten comparar el efecto de la competencia."),
        ("abc", "{F} ¿Qué paso del método corresponde a «buscar cartas y datos para cada causa»?", "Buscar evidencia para cada causa", "Definir el hecho", "Escribir la conclusión", "Ese es el paso 4: buscar evidencia."),
    ],
    ctx=("abc", "Una cooperativa de ejemplo analiza por qué bajaron sus ventas de miel: de 30 respuestas de socios, 15 mencionan el clima, 9 mencionan el precio del transporte y 6 mencionan menos flores. ¿Qué porcentaje menciona el clima?", "50 %", "30 %", "20 %", "15 de 30 es la mitad, es decir, el 50 %."),
    sc=[("¿Cuál es el primer paso para evaluar causas?", "Definir con claridad el hecho a explicar", "Sin ese paso no se sabe qué hecho se explica."),
        ("En un análisis de causas: ¿qué es una conclusión matizada?", "Una que reconoce lo que aún no se sabe", "Muestra honestidad frente a la evidencia que existe."),
        ("Al evaluar causas: ¿una opinión sin respaldo cuenta como evidencia?", "No, hace falta un dato o una fuente", "La evidencia debe poder comprobarse por otras personas.")],
    op=("Arma un cuadro de causas con estos datos de ejemplo sobre un hecho: «Una escuela nocturna de adultos perdió estudiantes entre 2019 y 2022». "
        "Datos de ejemplo: 40 de 100 estudiantes dicen que dejaron la escuela por cambios de turno en el trabajo; 30 por cuidados familiares; 20 por falta de transporte nocturno; 10 por otras razones. "
        "Escribe los porcentajes, ordena las causas, anota qué evidencia faltaría y redacta una conclusión matizada de dos frases.",
        "Porcentajes: turnos de trabajo 40 %, cuidados familiares 30 %, transporte nocturno 20 %, otras 10 %. Orden: turnos, cuidados, transporte, otras. Evidencia que falta: registros de asistencia por mes. Conclusión: los cambios de turno parecen haber pesado más, pero los cuidados familiares y el transporte también influyeron. Falta evidencia para saber cuánto pesó cada uno.",
        ["calcula y ordena las causas", "nombra qué evidencia falta", "la conclusión es matizada"],
        ["una tabla y dos frases"], ["afirmar una causa única", "no mencionar qué falta"],
        "Pregunta: «¿Qué dato respalda cada fila y qué falta para estar seguro?»."),
    reinforce="Ordena tres causas de un cambio de tu barrio según cuánto crees que pesaron y anota qué dato las respaldaría.",
    extend="Explica con un ejemplo por qué contar menciones no es lo mismo que medir el peso de una causa.",
)

# ======================================================= clase 4
F4 = ("Ficha 4 (de ejemplo, inventada). Disputa por una ladera en la localidad ficticia «Valle Robles», hacia 1890. "
      "Fuente A (informe de ejemplo de una oficina del Estado): «Las tierras de la ladera estaban sin uso y se entregaron a familias colonas para producir trigo». "
      "Fuente B (relato de ejemplo de una comunidad indígena vecina): «Esa ladera era nuestro lugar de siembra y de recolección y la usábamos todos los años». "
      "Fuente C (carta de ejemplo de una familia colona): «Llegamos con una autorización y quisimos cultivar para alimentar a nuestros hijos; no sabíamos que había una comunidad que ya la usaba». "
      "Explicación 1 (monocausal): «La disputa ocurrió porque la comunidad no quiso entregar la tierra». "
      "Explicación 2 (multicausal): «La disputa ocurrió por una política estatal de entrega de tierras, por el uso previo de la comunidad, por la llegada de familias colonas y por la falta de acuerdos sobre quién era dueño».")
build(
    O, 4, F4,
    use="Hoy practico con apoyo cómo evaluar explicaciones de un conflicto local con varias causas, escuchando perspectivas distintas con respeto y apertura.",
    prior=PRIOR_BASE + ["Conozco el método de cinco pasos para evaluar causas y sé contrastar fuentes de distintos grupos."],
    explain=[
        "Un conflicto local suele tener causas políticas, económicas y sociales, y cada grupo implicado lo ve desde su situación. Evaluar una explicación significa preguntar si usa varias causas, si tiene evidencia y si incluye las perspectivas de quienes participaron. Una explicación que culpa a un solo grupo suele ser incompleta.",
        "Pensar con apertura es una actitud: no se trata de dar la razón a todos, sino de entender por qué cada grupo vivió el hecho de forma distinta y qué evidencia respalda lo que dice. Se puede reconocer que una comunidad usaba una tierra desde antes y también que una familia llegó con una autorización, sin dejar de analizar las decisiones del Estado.",
        "Para evaluar con rigor, compara las explicaciones con las fuentes. Una explicación es mejor si coincide con más fuentes, si nombra varias causas y si es honesta sobre lo que no sabe. Todas las fuentes de esta ficha son de ejemplo y no representan a ninguna persona ni grupo real.",
    ],
    vocab=[("explicación monocausal", "explicación que usa una sola causa"), ("explicación multicausal", "explicación que usa varias causas"), ("apertura", "actitud de escuchar otras perspectivas con respeto"), ("política estatal", "decisión o plan del Estado sobre un tema"), ("responsabilidad", "parte que le toca a quien toma una decisión")],
    worked=[
        ("Evaluar una explicación monocausal", "{F} ¿Qué falla la explicación 1?", ["Dice que la disputa se debió solo a la actitud de la comunidad.", "Ignora la política estatal, la llegada de colonos y el uso previo de la tierra que aparecen en las fuentes."], "Usa una sola causa y deja fuera lo que muestran las fuentes"),
        ("Contrastar perspectivas", "{F} ¿Qué muestran juntas las fuentes B y C?", ["La fuente B dice que la comunidad usaba la ladera desde antes.", "La fuente C dice que la familia no sabía que había una comunidad que ya la usaba."], "Que la ladera ya tenía un uso previo y que la familia llegó sin saberlo, lo que ayuda a entender la disputa"),
    ],
    mistakes=[("Culpar a un solo grupo de un conflicto con varias causas.", "Es más simple que entender el contexto.", "Revisa qué decisiones y condiciones intervinieron."),
              ("Descartar una fuente porque no coincide con la propia opinión.", "Se confunde juzgar con escuchar.", "Contrasta cada fuente con las otras antes de decidir.")],
    T=[
        ("abc", "{F} ¿Quién escribe la fuente C?", "Una familia colona", "Una oficina del Estado", "Una comunidad indígena", "La ficha dice que es una carta de una familia colona."),
        ("ab", "{F} ¿Qué dice la fuente B sobre la ladera?", "Que la comunidad la usaba todos los años", "Que estaba sin uso", "La fuente B dice que era lugar de siembra y de recolección."),
        ("{F} ¿Para qué se entregaron las tierras a familias colonas, según la fuente A?", "Para producir trigo", "La fuente A dice que se entregaron para producir trigo."),
        ("abc", "{F} ¿Cuál de estas es una explicación multicausal?", "La explicación 2", "La explicación 1", "Ninguna de las dos", "La explicación 2 menciona cuatro causas."),
        ("abc", "{F} ¿Qué causa política aparece en la explicación 2?", "La política estatal de entrega de tierras", "La falta de lluvias", "El tamaño de la ladera", "La entrega de tierras es una decisión del Estado."),
        ("=", "{F} ¿Cuántas causas nombra la explicación 2?", "4", "Se cuentan la política estatal, el uso previo, la llegada de colonos y la falta de acuerdos.", " causas"),
        ("=", "{F} La ladera tiene 300 hectáreas y se entregaron 50 hectáreas a cada una de 4 familias colonas. ¿Cuántas hectáreas siguen sin entregar?", "300-4*50", "Se multiplican las hectáreas por familia y se restan del total.", " hectáreas"),
        ("abc", "{F} ¿Qué falla tiene la fuente A si se la usa sola?", "No muestra la perspectiva de quienes ya usaban la ladera", "No tiene fecha", "No describe ningún hecho", "Una sola fuente deja fuera otras voces."),
        ("abc", "{F} ¿Qué perspectiva muestra la fuente C?", "La de una familia que quería cultivar para alimentar a sus hijos", "La de un historiador actual", "La de la comunidad", "La carta explica el motivo de la familia colona."),
        ("abc", "{F} Una persona dice: «La explicación 1 es mejor porque es más corta y clara». ¿Qué responde un análisis cuidadoso?", "Que una explicación corta puede ser incompleta si omite causas y perspectivas", "Tiene razón: lo corto es mejor", "Las dos son iguales", "La claridad no reemplaza el respaldo en las fuentes."),
        ("ab", "{F} ¿Qué actitud permite evaluar mejor el conflicto?", "Escuchar las perspectivas con respeto y contrastarlas", "Elegir desde el inicio un bando", "La apertura implica escuchar y comparar antes de concluir."),
        ("abc", "{F} ¿Qué evidencia ayudaría a saber quién usaba la ladera antes de 1890?", "Un registro o un relato de épocas anteriores", "Un dibujo de la ladera actual", "Un informe sobre el clima de hoy", "Un registro anterior muestra el uso previo de la tierra."),
        ("abc", "{F} ¿Cuál es una conclusión bien apoyada?", "El conflicto surgió por varias causas, incluidas decisiones del Estado, el uso previo y la falta de acuerdos", "El conflicto fue culpa exclusiva de un grupo", "No hubo conflicto", "Es la que respeta varias fuentes y causas."),
    ],
    ctx=("abc", "En una asamblea de vecinos de ejemplo se discute por qué dos familias pelean por un canal de riego. Una dice: «El canal es mío, lo usaba mi abuela». La otra dice: «La municipalidad nos autorizó a usarlo». ¿Cómo se evalúa mejor el conflicto?", "Escuchando ambas versiones y buscando registros de uso y de autorización", "Dando la razón a la familia con más años en el barrio", "Evitando hablar del tema", "Cada versión es una perspectiva; los registros permiten comparar."),
    sc=[("¿Qué es una explicación monocausal?", "La que usa una sola causa", "Suele ser incompleta cuando el hecho es complejo."),
        ("¿Qué significa pensar con apertura?", "Escuchar perspectivas distintas con respeto", "Escuchar no implica estar de acuerdo con todos."),
        ("¿Qué hace mejor a una explicación?", "Varias causas, evidencia y perspectivas", "Esos tres rasgos le dan solidez a la explicación.")],
    op=("Evalúa estas dos explicaciones de ejemplo sobre por qué cerró una escuela rural de ejemplo en 1960. Explicación 1: «Cerró porque había pocos niños». Explicación 2: «Cerró porque había pocos niños, porque las familias se fueron a la ciudad por trabajo, porque el camino se cortaba en invierno y porque el Estado decidió reunir escuelas». "
        "Escribe cuál es más completa y por qué, qué perspectiva falta (por ejemplo, la de las familias) y qué fuente buscarías.",
        "La explicación 2 es más completa porque nombra cuatro causas de distinto tipo y la 1 usa una sola. Falta la perspectiva de las familias que vivieron el cierre. Buscaría un relato de ellas y un registro de matrícula por año.",
        ["compara las explicaciones con criterios", "reconoce una perspectiva que falta", "propone una fuente razonable"],
        ["tres frases ordenadas"], ["elegir la más corta", "descartar una perspectiva"],
        "Pregunta: «¿Qué causas nombra y qué voz falta?»."),
    reinforce="Piensa en un desacuerdo cotidiano (por ejemplo, por un horario o un espacio compartido) y escribe dos perspectivas distintas, sin usar nombres.",
    extend="Explica con un ejemplo por qué entender las razones de un grupo no obliga a estar de acuerdo con todo lo que hizo.",
)

# ======================================================= clase 5
F5 = ("Ficha 5. Relación entre procesos del pasado y el presente (hechos estándar y datos de ejemplo). "
      "Hecho estándar: durante el siglo XIX la economía de Chile se apoyó en exportar materias primas (trigo, plata, cobre y luego salitre). Hoy el cobre sigue siendo un producto importante de exportación. "
      "Hecho estándar: durante el siglo XIX y primera mitad del XX, muchas personas se trasladaron del campo a la ciudad. Hoy la mayoría de la población de Chile vive en ciudades. "
      "Hecho estándar: el voto de las mujeres en elecciones presidenciales y parlamentarias comenzó en 1949. "
      "Datos de práctica, inventados: la localidad «Villa Roca» tenía 5.000 habitantes en 1920 cuando funcionaba su mina; en 1980 la mina cerró y quedaron 2.000 habitantes; en 2020 tiene 3.000 habitantes, porque se instaló un servicio de turismo.")
build(
    O, 5, F5,
    use="Hoy relaciono procesos del siglo XIX y XX con situaciones del presente en el trabajo, la comunidad y la ciudad, evaluando causas y consecuencias.",
    prior=PRIOR_BASE + ["Sé evaluar un conjunto de causas con evidencia y contrastar perspectivas."],
    explain=[
        "Los procesos del pasado dejan huellas en el presente. Una economía que se organizó para exportar materias primas, como el cobre, sigue hoy teniendo mucho peso en la vida del país. El traslado del campo a la ciudad que comenzó en el siglo XIX es parte de que hoy la mayoría de las personas viva en ciudades. El voto femenino de 1949 es parte de la participación política actual.",
        "Pero relacionar pasado y presente exige cuidado. Que algo ocurra hoy y haya ocurrido antes no prueba que lo de ahora se deba solo a lo de entonces. Para hacerlo bien, se buscan las conexiones, se evalúan las causas y se reconocen otros factores del presente. Se puede decir «el pasado ayuda a explicar» en lugar de «el pasado causó todo».",
        "Un buen caso para practicar es el de una localidad que depende de una actividad. Cuando una mina cierra, las consecuencias llegan a las familias, a los comercios y a la población. Mirar cómo cambió esa localidad permite evaluar causas y ver cómo el pasado condiciona las decisiones de hoy.",
    ],
    vocab=[("huella del pasado", "rasgo del presente que viene de procesos anteriores"), ("dependencia de una actividad", "situación en que una localidad vive de una sola actividad"), ("factor", "elemento que influye en un resultado"), ("conexión", "relación entre dos hechos de distintas épocas"), ("diversificar", "tener varias actividades en lugar de una sola")],
    worked=[
        ("Conectar pasado y presente", "{F} ¿Qué conexión hay entre la economía exportadora del siglo XIX y la actual?", ["En el siglo XIX se exportaba cobre, entre otros productos.", "Hoy el cobre sigue siendo un producto importante de exportación."], "Se mantiene la exportación de materias primas, entre ellas el cobre"),
        ("Medir un cambio local", "{F} ¿Cuántos habitantes perdió Villa Roca entre 1920 y 1980?", ["Leo los datos: 5.000 en 1920 y 2.000 en 1980.", "Resto 5.000 menos 2.000."], "3.000 habitantes"),
    ],
    mistakes=[("Atribuir un problema actual solo a un hecho del pasado.", "Se busca una explicación simple y única.", "Reconoce factores del pasado y del presente a la vez."),
              ("Decir que el pasado «ya no importa» porque fue hace mucho.", "Se piensa que solo importa lo reciente.", "Busca huellas del pasado en el presente.")],
    T=[
        ("abc", "{F} ¿Qué producto sigue siendo importante en las exportaciones hoy?", "El cobre", "El salitre", "El carbón de vapor", "La ficha dice que el cobre sigue siendo un producto importante."),
        ("ab", "{F} ¿Desde qué año votan las mujeres en elecciones presidenciales y parlamentarias?", "Desde 1949", "Desde 1818", "La ficha indica 1949 para el voto presidencial y parlamentario."),
        ("{F} ¿Cuántos habitantes tenía Villa Roca en 1980?", "2.000", "La ficha dice que quedaron 2.000 habitantes en 1980."),
        ("=", "{F} ¿Cuántos habitantes más tiene Villa Roca en 2020 que en 1980?", "3000-2000", "Se resta el dato de 1980 al de 2020 para ver cuánto se recuperó.", " habitantes"),
        ("=", "{F} ¿Cuántos años pasaron entre el cierre de la mina (1980) y el dato de 2020?", "2020-1980", "Se restan las fechas para conocer el tiempo transcurrido.", " años"),
        ("=", "{F} ¿Qué porcentaje de los habitantes de 1920 había en 1980?", "2000*100//5000", "Se divide 2.000 entre 5.000 y se multiplica por 100.", " %"),
        ("abc", "{F} ¿Qué consecuencia tuvo el cierre de la mina en Villa Roca?", "Bajó mucho la población", "Aumentó la población", "No cambió nada", "La población pasó de 5.000 a 2.000 habitantes."),
        ("abc", "{F} ¿Qué factor explica en parte la recuperación de la población en 2020?", "La instalación de un servicio de turismo", "La reapertura de la misma mina", "La falta de actividades", "La ficha dice que el turismo se instaló y la población llegó a 3.000."),
        ("abc", "{F} Una persona dice: «Villa Roca perdió población solo porque cerró la mina». ¿Qué responde un análisis cuidadoso?", "Que el cierre fue un factor central, pero hacen falta fuentes sobre otros factores", "Que fue la única causa comprobada", "Que no tuvo relación con la mina", "La ficha muestra una relación, pero no prueba que no hubiera otros factores."),
        ("ab", "{F} ¿Qué se puede afirmar sobre la economía del cobre?", "Que viene de una larga tradición exportadora", "Que apareció recién en 1980", "El cobre se exportaba ya en el siglo XIX, por lo que hay continuidad."),
        ("abc", "{F} ¿Qué significa «diversificar» en el caso de Villa Roca?", "Tener turismo además de la minería", "Vivir solo de una mina", "Dejar la localidad vacía", "Diversificar es sumar actividades para depender menos de una sola."),
        ("abc", "{F} ¿Qué conclusión sobre el pasado y el presente se sostiene mejor?", "El pasado ayuda a explicar el presente, junto con otros factores actuales", "El pasado explica todo del presente", "El pasado no influye en el presente", "Es una conclusión matizada que no exagera ni niega la relación."),
        ("abc", "{F} Para evaluar bien una relación entre pasado y presente, ¿qué conviene hacer?", "Buscar evidencia de la conexión y otros factores", "Elegir la explicación más cómoda", "Ignorar el presente", "La evidencia y los otros factores evitan una explicación apresurada."),
    ],
    ctx=("abc", "Un comité de ejemplo de un pueblo salinero compara: «En 1950 había 800 trabajadores en las salinas; hoy hay 200 y se suma una cooperativa de turismo con 60 trabajadores». ¿Cuántos puestos de trabajo hay hoy en total entre salinas y turismo?", "260 puestos", "200 puestos", "860 puestos", "Se suman las salinas (200) y el turismo (60): 260."),
    sc=[("¿Qué es una huella del pasado?", "Un rasgo del presente que viene de procesos anteriores", "Esa huella ayuda a conectar épocas distintas."),
        ("¿Qué significa diversificar?", "Tener varias actividades y no solo una", "Así disminuye la dependencia de una sola actividad."),
        ("¿Basta un hecho del pasado para explicar todo el presente?", "No, hay otros factores", "El presente tiene también muchas causas actuales.")],
    op=("Analiza esta localidad ficticia con datos de ejemplo: «Puerto Seco vivía de una salitrera. En 1920 tenía 6.000 habitantes; en 1950, 2.000; hoy, 2.500. La salitrera cerró en 1930 por la competencia del salitre sintético. Hoy hay una caleta de pescadores con 100 familias». "
        "Calcula cuántos habitantes perdió entre 1920 y 1950, escribe dos causas del cambio y una huella del pasado en el presente, y plantea una pregunta que te quede pendiente.",
        "Perdió 4.000 habitantes. Causas: cerró la salitrera por la competencia del salitre sintético; la gente se fue a buscar trabajo en otros lugares. Huella en el presente: la localidad sigue marcada por la historia de la salitrera, aunque hoy vive de la pesca. Pregunta: ¿qué otros factores explican que la población se recuperara parcialmente?",
        ["calcula bien", "nombra causas con respaldo", "conecta con el presente y plantea una pregunta"],
        ["un cálculo, dos causas, una conexión y una pregunta"], ["una sola causa", "exagerar la relación"],
        "Pregunta: «¿Qué dato respalda la relación con el pasado?»."),
    reinforce="Piensa en un lugar de tu entorno que dependía de una actividad y anota cómo cambió y qué huella queda.",
    extend="Explica con un ejemplo por qué diversificar actividades puede proteger a una localidad.",
)

# ======================================================= clase 6
F6 = ("Ficha 6 (de ejemplo). Dos explicaciones del mismo hecho: «el crecimiento de las ciudades chilenas entre 1850 y 1930». "
      "Explicación A: «Las ciudades crecieron porque llegó el ferrocarril». "
      "Explicación B: «Las ciudades crecieron por varias causas: la economía de exportación atrajo trabajo en puertos y minas; el ferrocarril unió zonas; muchas familias dejaron el campo por falta de tierras y de empleo; y el Estado construyó escuelas y servicios en las ciudades. Falta evidencia sobre cuánto pesó cada causa en cada ciudad». "
      "Criterios de evaluación: 1) usa varias causas; 2) incluye evidencia; 3) distingue causas de largo plazo y detonante; 4) reconoce lo que falta; 5) incluye perspectivas de distintos grupos.")
build(
    O, 6, F6,
    use="Hoy evalúo explicaciones con criterios claros, redacto una conclusión multicausal y decido qué repasar de la unidad.",
    prior=PRIOR_BASE + ["He practicado el cuadro de causas, la lectura de fuentes de varios grupos y la conexión entre pasado y presente."],
    explain=[
        "Evaluar una explicación es compararla con criterios. Los criterios de la ficha sirven para cualquier proceso: ¿usa varias causas?, ¿incluye evidencia?, ¿distingue causas de largo plazo y detonante?, ¿reconoce lo que falta?, ¿incluye varias perspectivas? Una explicación que cumple más criterios es más sólida, aunque nunca es perfecta.",
        "Una conclusión multicausal se escribe en pocas frases: nombra las causas principales, dice cuál parece pesar más y por qué, reconoce lo que falta y conecta con el presente. Por ejemplo: «Las ciudades crecieron por la economía de exportación y por la migración del campo; el ferrocarril ayudó a unir zonas, pero falta evidencia de su peso exacto».",
        "Para cerrar la unidad, haz un balance. Revisa qué ideas dominas (cambio y continuidad, causas, evidencia, perspectivas) y cuáles quieres repasar. Una buena decisión de estudio nace de reconocer qué te costó, no de repetir lo que ya sabes.",
    ],
    vocab=[("criterio", "regla que se usa para juzgar algo"), ("explicación sólida", "explicación que cumple varios criterios y está bien respaldada"), ("conclusión multicausal", "conclusión que reúne varias causas y reconoce lo que falta"), ("balance", "revisión de lo logrado y lo pendiente"), ("perspectiva", "punto de vista de un grupo sobre un hecho")],
    worked=[
        ("Aplicar los criterios", "{F} ¿Cuántos criterios cumple la explicación A?", ["Reviso los cinco criterios en el texto de A.", "Solo nombra una causa (el ferrocarril), no incluye evidencia, no distingue plazos, no reconoce lo que falta ni incluye perspectivas."], "Ninguno de los cinco"),
        ("Aplicar los criterios a B", "{F} ¿Qué criterios cumple la explicación B?", ["Usa varias causas (economía, ferrocarril, migración, Estado).", "Reconoce lo que falta: evidencia del peso de cada causa."], "Cumple los criterios de varias causas y de reconocer lo que falta; le falta evidencia concreta y perspectivas"),
    ],
    mistakes=[("Evaluar solo por el largo del texto.", "Se confunde extensión con calidad.", "Aplica los criterios uno por uno."),
              ("Creer que una explicación sólida no necesita reconocer lo que falta.", "Se piensa que dudar es debilidad.", "Reconocer los límites muestra honestidad y rigor.")],
    T=[
        ("abc", "{F} ¿Cuántos criterios de evaluación hay en la ficha?", "Cinco", "Tres", "Ocho", "La ficha enumera exactamente cinco criterios de evaluación."),
        ("ab", "{F} ¿Qué explicación usa varias causas?", "La B", "La A", "La B nombra cuatro causas; la A solo nombra el ferrocarril."),
        ("{F} ¿Qué causa menciona la explicación A?", "El ferrocarril", "La explicación A dice que las ciudades crecieron porque llegó el ferrocarril."),
        ("=", "{F} ¿Cuántas causas enumera la explicación B?", "4", "Se cuentan economía de exportación, ferrocarril, salida del campo y servicios del Estado.", " causas"),
        ("=", "{F} Si una explicación cumple 3 de los 5 criterios, ¿cuántos no cumple?", "5-3", "Se resta lo cumplido al total de criterios para ver los pendientes.", " criterios"),
        ("abc", "{F} ¿Qué criterio cumple la frase «falta evidencia sobre cuánto pesó cada causa»?", "Reconoce lo que falta", "Incluye perspectivas", "Usa una sola causa", "Esa frase reconoce un límite de la explicación."),
        ("abc", "{F} ¿Qué criterio no cumple la explicación A?", "Usar varias causas", "Tener una frase", "Mencionar las ciudades", "A usa solo una causa, el ferrocarril."),
        ("abc", "{F} ¿Qué mejora le harías a la explicación B?", "Agregar evidencia y la perspectiva de grupos como las mujeres y los pueblos indígenas", "Quitarle causas", "Dejar solo el ferrocarril", "Con evidencia y más voces cumpliría más criterios."),
        ("abc", "{F} Un compañero dice: «La B es mejor porque es más larga». ¿Qué responde un análisis cuidadoso?", "Que es mejor por cumplir más criterios, no por su largo", "Tiene razón: lo más largo es mejor", "Que A y B son iguales", "Se evalúa por los criterios y no por la extensión."),
        ("ab", "{F} ¿Qué conclusión multicausal es mejor?", "Las ciudades crecieron por la exportación, la migración y el ferrocarril; falta evidencia de su peso", "Las ciudades crecieron por una sola causa comprobada", "La conclusión que reúne varias causas y reconoce lo que falta es la más sólida."),
        ("abc", "{F} ¿Con qué evidencia podría reforzarse la explicación B?", "Con registros de habitantes por ciudad y relatos de quienes migraron", "Con la opinión de alguien que no vivió ahí", "Con una lista de nombres de ciudades", "Registros y relatos darían respaldo a las causas."),
        ("abc", "Terminas la unidad y haces tu balance. ¿Cuál es la mejor decisión?", "Repasar con un ejemplo el criterio que más me costó", "No repasar nada", "Estudiar solo lo que ya domino", "El balance sirve para decidir qué repasar."),
        ("abc", "{F} ¿Para qué sirve conectar el crecimiento de las ciudades con el presente?", "Para entender que hoy la mayoría de la población vive en ciudades por procesos de larga duración", "Para no tener que estudiar el pasado", "Para negar el cambio", "La conexión muestra cómo el pasado ayuda a explicar el presente."),
    ],
    ctx=("abc", "Una dirigente de la junta de vecinos de ejemplo escribe: «Nuestro barrio creció porque llegó la locomoción colectiva». Una vecina responde: «También influyeron los precios de los terrenos, el trabajo cerca y que llegaron familias de otras regiones». ¿Qué criterio cumple la respuesta de la vecina?", "Usa varias causas", "Usa una sola causa", "No usa ninguna causa", "La vecina agrega otras causas, por eso la explicación gana solidez."),
    sc=[("Al evaluar explicaciones históricas: ¿qué es un criterio?", "Una regla para juzgar algo", "Un criterio permite comparar explicaciones de manera justa."),
        ("¿Qué incluye una conclusión multicausal?", "Varias causas y lo que falta por saber", "Une las causas y además reconoce sus límites."),
        ("¿Qué hago al hacer el balance?", "Reviso qué domino y qué quiero repasar", "El balance orienta el estudio que viene después.")],
    op=("Escribe una conclusión multicausal de cuatro a seis líneas sobre este hecho de ejemplo: «Una población rural perdió habitantes entre 1930 y 1960». Datos de ejemplo: la mina cercana cerró en 1935; el camino a los servicios quedó cortado; las familias jóvenes buscaron trabajo en la ciudad; la escuela cerró en 1950. "
        "Incluye al menos tres causas, cuál parece pesar más y por qué, qué evidencia falta y una conexión con el presente. Termina con una frase de balance sobre qué quieres repasar.",
        "La población perdió habitantes por varias causas: el cierre de la mina en 1935, el camino cortado, la salida de las familias jóvenes a la ciudad y el cierre de la escuela en 1950. La salida de las familias parece pesar más, pues se relaciona con el trabajo. Falta evidencia de cuántas familias se fueron en cada año. Hoy muchos pueblos pequeños enfrentan problemas parecidos. Balance: quiero repasar cómo distinguir causas y consecuencias.",
        ["usa tres o más causas con datos", "reconoce lo que falta", "conecta con el presente y hace un balance"],
        ["un texto breve con balance"], ["una sola causa", "exagerar la conexión con el presente"],
        "Pregunta: «¿Qué dato respalda cada causa y qué falta para estar más seguro?»."),
    reinforce="Elige un hecho de tu trabajo o tu barrio y escribe tres causas, una consecuencia y qué evidencia buscarías.",
    extend="Explica con un ejemplo por qué una buena explicación histórica siempre deja preguntas pendientes.",
)
