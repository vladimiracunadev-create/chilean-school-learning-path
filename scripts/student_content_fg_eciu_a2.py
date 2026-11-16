"""Educación Ciudadana 3.º medio FG: OA 03 (riesgos para la democracia) y OA 04 (relaciones entre Estado y mercado). Casos y cifras de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O3 = "FG-ECIU-3M-OAC-03"
O4 = "FG-ECIU-3M-OAC-04"

# ============================================================ OA 03, clase 1
F = ("Ficha 12 (país ficticio de ejemplo, Costa Verde, con datos inventados): en la última elección votó el 45 % de las personas habilitadas; "
     "solo 2 de cada 10 confían en los partidos; un informe de ejemplo mostró que el 10 % más rico tiene una parte muy superior de los ingresos que el 50 % más pobre; "
     "una funcionaria fue investigada por entregar un contrato a su primo; en un barrio, bandas de tráfico de drogas amenazan a comerciantes.")
build(
    O3, 1, F,
    use="Aprenderé a definir los principales riesgos para la democracia (desafección política, desigualdad, corrupción, narcotráfico y violencia) y a explicar por qué la debilitan.",
    prior=["Sé qué son la democracia y sus atributos.", "Sé qué es una libertad fundamental.", "Sé interpretar un porcentaje simple."],
    explain=[
        "Un riesgo para la democracia es un fenómeno que debilita sus atributos: elecciones libres, igualdad ante la ley, libertades y confianza en las instituciones. La desafección política es el distanciamiento de las personas respecto de la política: desinterés, desconfianza y baja participación. La desigualdad es una distribución muy dispareja de ingresos y oportunidades.",
        "La corrupción es el uso indebido de un cargo o poder para obtener un beneficio privado, como dar un contrato a un familiar. El narcotráfico es el comercio ilegal de drogas; sus redes suelen usar amenazas, dinero ilícito e influencias para controlar territorios. La violencia, política o social, daña la libertad de las personas y la convivencia.",
        "Estos riesgos se conectan: la corrupción aumenta la desconfianza; la desconfianza reduce la participación; la desigualdad alimenta la desafección; el narcotráfico se aprovecha de la debilidad del Estado. Reconocerlos permite estudiar causas y respuestas, sin culpar a todo un grupo y sin pensar que una sola medida resuelve el problema.",
    ],
    vocab=[("desafección política", "distanciamiento de la gente respecto de la política, con desinterés y desconfianza"), ("desigualdad", "distribución muy dispareja de ingresos u oportunidades"), ("corrupción", "uso indebido de un cargo o poder para un beneficio privado"), ("narcotráfico", "comercio ilegal de drogas por redes organizadas"), ("riesgo para la democracia", "fenómeno que debilita sus atributos o la confianza en ella")],
    worked=[
        ("Reconocer corrupción", "En un municipio de ejemplo, una autoridad contrata a una empresa de su hermana sin concurso. ¿Qué riesgo se observa?", ["Usa su cargo para beneficiar a un familiar.", "Eso es corrupción."], "Corrupción"),
        ("Reconocer desafección", "En un liceo de ejemplo, de 100 estudiantes solo 20 votan en el centro de estudiantes y dicen que «da lo mismo». ¿Qué riesgo es?", ["Hay baja participación.", "Y desinterés por la decisión colectiva."], "Desafección política"),
    ],
    mistakes=[("Llamar corrupción a cualquier error de una autoridad.", "La corrupción exige uso indebido del cargo para un beneficio privado.", "Pregunta si hubo beneficio privado."),
              ("Creer que la violencia solo es física.", "También hay violencia verbal y psicológica que daña la convivencia.", "Revisa la afectación de libertades y dignidad.")],
    T=[
        ('abc', '¿Qué es la desafección política?', 'Distanciamiento de las personas respecto de la política, con desinterés y desconfianza', 'El rechazo a un partido concreto por sus propuestas o por sus candidatos', 'El desconocimiento de las reglas del sistema electoral y de las elecciones', 'La desafección es un distanciamiento general frente a la política; rechazar a un partido o ignorar las reglas no lo define.'),
        ('=', '{F} Si en una ciudad de 80.000 personas habilitadas votó el 45 %, ¿cuántas personas no votaron?', '80000-80000*45//100', 'Se calcula cuántas votaron y se resta del total de habilitadas.', ' personas'),
        ('abc', '{F} Si se comprobara que la funcionaria entregó un contrato a su primo para beneficiarlo, ¿qué riesgo sería?', 'Corrupción', 'Desigualdad', 'Desafección política', 'Usar un cargo para un beneficio privado es corrupción; la desigualdad se refiere a ingresos y la desafección al distanciamiento de la política.'),
        ('abc', '{F} ¿Qué riesgo describen juntos el 45 % de votantes y la poca confianza en los partidos?', 'Desafección política, por el distanciamiento de la política', 'Narcotráfico, por el comercio ilegal de drogas', 'Corrupción, por el uso indebido de un cargo', 'Baja participación y desconfianza son los rasgos de la desafección; la ficha no muestra aquí un delito.'),
        ('abc', '¿Qué es el narcotráfico?', 'El comercio ilegal de drogas por redes organizadas que usan amenazas y dinero ilícito', 'El consumo de drogas por parte de jóvenes en un barrio de la ciudad', 'El robo con intimidación a comerciantes por parte de una banda local', 'El narcotráfico es un comercio ilegal organizado; el consumo y el robo son otros fenómenos.'),
        ('abc', '¿Qué daña principalmente la violencia en una democracia?', 'La libertad de las personas y la convivencia', 'El derecho a votar, pero no otros derechos', 'Solo la seguridad de quienes la sufren, sin afectar la vida democrática', 'La violencia amenaza libertades y convivencia de toda la comunidad, no solo de las víctimas directas.'),
        ('abc', '{F} ¿Qué riesgo muestra el informe de ingresos entre el 10 % más rico y el 50 % más pobre?', 'Desigualdad, por una distribución muy dispareja de ingresos', 'Corrupción, por un uso indebido de recursos públicos', 'Violencia, por conflictos entre sectores sociales', 'El informe compara cuánto ingreso tiene cada grupo, que es lo que mide la desigualdad.'),
        ('abc', '{F} ¿Qué riesgos representan las bandas que amenazan a comerciantes?', 'Narcotráfico y violencia', 'Desafección política', 'Desigualdad', 'Las amenazas para controlar un territorio son violencia ejercida por redes de tráfico de drogas.'),
        ('=', '{F} De 50 personas encuestadas, 2 de cada 10 confían en los partidos. ¿Cuántas no confían?', '50-50*2//10', 'Se calcula cuántas confían y se resta del total.', ' personas'),
        ('abc', '{F} ¿Cómo se conectan la corrupción y la desafección?', 'La corrupción aumenta la desconfianza y esta reduce la participación', 'La corrupción aumenta la participación porque la gente se indigna', 'No se conectan: son riesgos independientes', 'La clase explica que la corrupción alimenta la desconfianza y la desconfianza aleja a las personas de la política.'),
        ('abc', '{F} Un estudiante dice: «Todos los políticos de Costa Verde son corruptos». ¿Qué error comete?', 'Generaliza a todos a partir de un caso', 'Usa evidencia suficiente para su afirmación', 'Confunde corrupción con desigualdad', 'Un caso investigado no prueba la conducta de todas las personas que ejercen cargos.'),
        ('abc', '{F} ¿Por qué el narcotráfico se aprovecha de un Estado débil?', 'Donde las instituciones son débiles puede controlar territorios con amenazas e influencias', 'Porque un Estado fuerte necesita su dinero para financiarse y mantener servicios', 'Porque los barrios con más votantes son más fáciles de controlar por las bandas', 'La clase señala que las redes se aprovechan de la debilidad del Estado para imponer su control.'),
        ('abc', '{F} ¿Qué respuesta es más razonable ante estos riesgos?', 'Estudiar sus causas y combinar varias medidas, sin culpar a un grupo', 'Buscar la medida única que resuelva el riesgo más grave', 'Esperar a que los riesgos disminuyan por sí solos', 'Los riesgos se conectan, así que una sola medida no basta; esperar tampoco los resuelve.'),
    ],
    ctx=('abc', 'En una población de ejemplo hay menos gente en las juntas de vecinos porque dicen que «nadie los escucha». ¿Qué riesgo aparece?', 'Desafección política, por la desconfianza y la baja participación', 'Corrupción, por el uso indebido de un cargo público', 'Violencia, por la amenaza hacia las personas del barrio', 'La baja participación por desconfianza es la desafección.'),
    sc=[
        ('¿Qué es la corrupción?', 'El uso indebido de un cargo o poder para obtener un beneficio privado', 'Se trata de beneficiar a alguien, por ejemplo a un familiar, usando un cargo público.'),
        ('abc', '¿Qué relación hay entre la desigualdad y la desafección?', 'La desigualdad puede alimentar la desafección: quien se siente excluido se aleja de la política', 'No hay relación: la desafección depende solo del interés personal de cada uno', 'La desigualdad reduce la desafección porque hay más debate entre las personas', 'La clase conecta ambos riesgos: la sensación de exclusión debilita la confianza en las instituciones.'),
        ('En Educación Ciudadana: ¿qué es la desigualdad?', 'Una distribución muy dispareja de ingresos u oportunidades', 'Se refiere a diferencias grandes en ingresos u oportunidades entre grupos.'),
    ],
    op=("Con la {F} haz una tabla de cinco filas (desafección, desigualdad, corrupción, narcotráfico, violencia): dato de la ficha que lo muestra y una consecuencia para la democracia. Luego escribe una reflexión personal de tres líneas sobre cuál de ellos te parece más cercano a tu entorno, sin nombrar personas.",
        "Desafección: 45 % vota; baja confianza en partidos. Desigualdad: informe de ingresos. Corrupción: contrato al primo. Narcotráfico: amenazas a comerciantes. Violencia: amenazas en el barrio. Reflexión: me parece más cercana la desafección, porque en mi curso pocos votan.",
        ["usa datos de la ficha", "explica consecuencias", "reflexiona sin exponer personas"], ["tabla de cinco filas", "reflexión de tres líneas"], ["generalizar a todos", "nombrar personas reales"],
        "Pregunta qué evidencia necesitaría para afirmar que dos riesgos se relacionan."),
    reinforce="Define con tus palabras tres riesgos y da un ejemplo inventado de cada uno.",
    extend="Conversa con una persona de confianza sobre cómo ve la confianza en las instituciones y anota una idea.",
)

# ============================================================ OA 03, clase 2
F = ("Ficha 13 (indicadores de ejemplo, ciudad ficticia de San Pedro): "
     "Año 1: participación en elecciones locales 60 %, denuncias por corrupción 12, confianza en el municipio 40 %. "
     "Año 2: participación 50 %, denuncias por corrupción 20, confianza 30 %. "
     "Nota de prensa de ejemplo: «Más denuncias pueden indicar más casos o más confianza en denunciar». Los datos no incluyen cuántas denuncias fueron confirmadas.")
build(
    O3, 2, F,
    use="Aprenderé a investigar un fenómeno que amenaza la democracia usando indicadores, y a evitar sacar conclusiones que los datos no permiten.",
    prior=["Sé definir los riesgos para la democracia.", "Sé calcular diferencias y porcentajes simples.", "Sé qué es una fuente."],
    explain=[
        'Un indicador es un dato que resume un fenómeno, como el porcentaje de participación o el número de denuncias. Permite comparar en el tiempo y entre lugares. Para investigarlo se mira la tendencia (si sube o baja), se calcula la diferencia entre períodos y se pregunta qué mide realmente y qué no mide. Si un porcentaje pasa de 60 % a 50 %, bajó 10 puntos porcentuales; su variación relativa se calcula dividiendo esa diferencia por el valor inicial.',
        'Un indicador puede engañar. Más denuncias de corrupción podrían significar más casos o más personas que se atreven a denunciar. Que dos datos cambien al mismo tiempo, por ejemplo menos participación y menos confianza, muestra una relación, pero no prueba por sí solo que uno cause el otro. Por eso se habla de relación o correlación, y no de causa segura.',
        'Para una conclusión sólida se piden más datos: cuántas denuncias se confirmaron, cómo se midió la confianza y qué otros factores cambiaron. También se cuida la forma de comunicarlo: se dice «los datos sugieren…», se indica el período y se evita culpar a personas o grupos concretos.',
    ],
    vocab=[("indicador", "dato que resume un fenómeno y permite compararlo"), ("tendencia", "dirección en que cambia un dato en el tiempo"), ("correlación", "relación entre dos datos que cambian a la vez, sin probar causa"), ("causa", "factor que produce un efecto"), ("dato confirmado", "dato verificado por una fuente confiable")],
    worked=[
        ("Calcular una variación", "Un indicador de ejemplo bajó de 70 % a 55 %. ¿Cuántos puntos porcentuales bajó?", ["Se resta 55 a 70.", "El resultado se expresa en puntos."], "15 puntos porcentuales"),
        ("Evitar la causa segura", "En un barrio de ejemplo bajó la participación en juntas y subió la venta de helados. ¿Una causa a la otra?", ["Cambiaron a la vez.", "No hay motivo para pensar que una causa la otra."], "No; es una coincidencia sin evidencia de causa"),
    ],
    mistakes=[("Decir que si dos datos cambian a la vez, uno causa el otro.", "Puede haber otras razones o ser coincidencia.", "Habla de relación y pide más datos."),
              ("Tomar un número de denuncias como número de delitos.", "Las denuncias miden lo que se informa, no todo lo que ocurre.", "Pregunta qué mide realmente el indicador.")],
    T=[
        ('abc', '¿Qué significa que dos datos tengan una correlación?', 'Que cambian al mismo tiempo, sin que eso pruebe que uno cause al otro', 'Que uno es la causa segura del otro, porque ocurren en el mismo período', 'Que ambos miden lo mismo con distinto nombre y por eso cambian juntos', 'Una correlación describe una relación entre datos; probar una causa exige más evidencia.'),
        ('=', '{F} ¿En qué porcentaje bajó la confianza en el municipio respecto del año 1?', '(40-30)*100//40', 'Se divide la baja (10 puntos) por el valor inicial (40 %).', ' %'),
        ('=', '{F} Si el municipio tiene 12.000 personas habilitadas, ¿cuántas personas menos votaron en el año 2 que en el año 1?', '12000*60//100-12000*50//100', 'Se calcula cuántas votaron cada año y se restan.', ' personas'),
        ('abc', '{F} ¿Cuál afirmación describe bien la tendencia de los tres indicadores entre el año 1 y el año 2?', 'La participación y la confianza bajaron; las denuncias subieron', 'La participación y la confianza subieron; las denuncias bajaron', 'La participación bajó; las denuncias y la confianza subieron', 'Participación pasó de 60 % a 50 %, confianza de 40 % a 30 % y denuncias de 12 a 20.'),
        ('abc', '{F} ¿Qué dato falta para saber si hubo más casos de corrupción?', 'Cuántas denuncias fueron confirmadas', 'El nombre del alcalde de cada año', 'Cuántos años lleva el municipio en funcionamiento', 'Sin saber cuántas denuncias se confirmaron no se sabe si aumentaron los casos o solo las denuncias.'),
        ('abc', '{F} La nota de prensa dice que más denuncias pueden indicar más casos o más confianza en denunciar. ¿Qué enseña?', 'Que un mismo indicador puede interpretarse de más de una manera', 'Que las denuncias son siempre falsas y deben ser descartadas del análisis', 'Que las denuncias no sirven como indicador para estudiar la corrupción', 'Un indicador resume, pero no dice por sí solo por qué cambia.'),
        ('abc', '{F} Un estudiante dice: «La corrupción causó que baje la participación». ¿Qué corresponde?', 'Decir que hay una relación entre los datos, pero que no prueban causa, y pedir más datos', 'Aceptar la causa, porque ambos datos cambiaron en el mismo período', 'Rechazar la relación, porque no hay datos confirmados de corrupción', 'Dos datos que cambian a la vez muestran una relación, no una causa segura.'),
        ('abc', '{F} ¿Qué frase es más prudente?', 'Los datos sugieren que la participación y la confianza bajaron entre el año 1 y el 2', 'Está demostrado que la gente odia al municipio', 'Los datos prueban que la baja de confianza causa la baja de participación', 'La frase prudente describe lo observado y usa «sugieren» sin afirmar causas ni emociones.'),
        ('abc', '{F} Un diario titula: «Subieron las denuncias, el país es más corrupto». ¿Qué problema tiene el título?', 'Concluye algo que el dato no permite: puede haber más casos o más confianza', 'Usa un dato falso para sostener que el país es más corrupto', 'No cita el período de los datos que se están comparando', 'El dato no distingue entre más casos y más personas que se atreven a denunciar.'),
        ('=', '{F} Si de las 20 denuncias del año 2 se confirmaran 8, ¿qué porcentaje sería?', '8*100//20', 'Se compara la parte confirmada con el total de denuncias.', ' %'),
        ('abc', '{F} Supón (dato de ejemplo) que de las 12 denuncias del año 1 se confirmaron 6 y de las 20 del año 2 también 6. ¿Qué conclusión es razonable?', 'Las denuncias aumentaron, pero los casos confirmados no', 'Aumentó la corrupción porque hay más denuncias', 'Disminuyó la corrupción porque bajó la proporción confirmada', 'Con 6 casos confirmados en ambos años, el aumento de denuncias no se tradujo en más casos comprobados.'),
        ('abc', '{F} Antes de recomendar una medida, ¿qué conviene hacer?', 'Obtener los datos que faltan y considerar otros factores', 'Elegir la medida que más gente apoye', 'Aplicar la misma medida que en otra ciudad', 'Una medida adecuada se apoya en causas mejor comprendidas.'),
        ('abc', '{F} ¿Qué mide el indicador de denuncias?', 'Lo que se informa, no necesariamente todo lo que ocurre', 'Todos los casos de corrupción que existen', 'Solo los casos que terminaron en sentencia', 'Una denuncia es un reporte; puede haber casos no informados o no confirmados.'),
    ],
    ctx=('abc', 'En un liceo de ejemplo aumentaron los reportes de acoso escolar. ¿Qué interpretación es prudente?', 'Puede haber más casos o más estudiantes que se atreven a reportar; hacen falta más datos', 'El acoso aumentó seguramente, porque hay más reportes que el año anterior', 'El liceo es peor que antes, porque ahora se informan más casos', 'Igual que con las denuncias, un aumento de reportes admite más de una explicación.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un indicador?', 'Un dato que resume un fenómeno y permite compararlo', 'Permite comparar en el tiempo y entre lugares, como el porcentaje de participación.'),
        ('abc', '¿Qué es la correlación?', 'Una relación entre datos que cambian a la vez, sin probar causa', 'La causa segura de un hecho, demostrada por los datos disponibles', 'La diferencia entre dos porcentajes medidos en años distintos', 'Describe una relación, pero la causa exige más evidencia.'),
        ('¿Qué es la tendencia de un indicador?', 'Si el dato sube o baja a lo largo del tiempo', 'Se observa comparando el indicador en distintos períodos.'),
    ],
    op=("Con la {F} redacta un párrafo de cinco líneas con: (1) las tendencias que ves; (2) dos interpretaciones posibles de las denuncias; (3) un dato adicional que pedirías; (4) una frase prudente que no culpe a nadie.",
        "(1) Bajan la participación y la confianza y suben las denuncias. (2) Más casos o más confianza para denunciar. (3) Cuántas denuncias fueron confirmadas. (4) Los datos sugieren un deterioro de la confianza, pero no permiten saber la causa.",
        ["describe tendencias con números", "ofrece interpretaciones alternativas", "no afirma causas"], ["párrafo de cinco líneas"], ["afirmar causalidad", "culpar a personas"],
        "Pregunta cómo se podría medir la confianza de otra manera."),
    reinforce="Explica con un ejemplo por qué «cambian a la vez» no significa «uno causa al otro».",
    extend="Busca un indicador de un tema de tu comuna y anota qué mide y qué no mide.",
)

# ============================================================ OA 03, clase 3
F = ("Ficha 14 (perspectivas de ejemplo sobre la baja participación juvenil en una comuna ficticia). "
     "Perspectiva 1 (joven): «No voto porque nadie me explica cómo las decisiones me afectan». "
     "Perspectiva 2 (investigadora): «La participación baja cuando las personas perciben que sus votos no cambian nada, pero sube cuando hay proyectos cercanos». "
     "Perspectiva 3 (autoridad local): «Hay que mejorar la información y facilitar el acceso a votar». Dato de ejemplo (dos mediciones distintas): de cada 100 jóvenes, 45 asisten a proyectos barriales y 30 votan en la elección local.")
build(
    O3, 3, F,
    use="Aprenderé a contrastar explicaciones sobre un riesgo para la democracia y a distinguir cuáles tienen evidencia y cuáles son opiniones.",
    prior=["Sé qué es la desafección política.", "Sé leer indicadores.", "Sé comparar perspectivas."],
    explain=[
        "Los fenómenos sociales suelen tener varias causas: personales, institucionales y de contexto. Una explicación única es casi siempre incompleta. Al contrastar, se anota qué factor destaca cada perspectiva (falta de información, falta de confianza, falta de oportunidades de participar) y qué evidencia presenta.",
        "Hay diferentes tipos de evidencia. Un testimonio muestra una experiencia, pero no representa a todos. Una encuesta permite generalizar si la muestra es adecuada. Un registro de asistencia muestra una conducta observable. Un buen contraste pregunta si la evidencia respalda lo que se dice y si hay otras explicaciones posibles.",
        "También conviene preguntar quién habla y desde qué lugar: la autoridad puede enfatizar lo que mejora desde el sistema, el joven su experiencia y la investigadora el patrón. Las tres ayudan. Desde ahí se arma una explicación más completa y se proponen medidas que cubran varias causas, sin culpar a los jóvenes ni al sistema por completo.",
    ],
    vocab=[("causa múltiple", "fenómeno que se explica por varios factores a la vez"), ("testimonio", "relato de una experiencia personal"), ("muestra", "grupo de personas que representa a un conjunto mayor"), ("patrón", "regularidad que se repite en varios casos"), ("explicación incompleta", "que considera un solo factor y deja otros fuera")],
    worked=[
        ("Tipo de evidencia", "Una profesora de ejemplo presenta una lista de asistencia a talleres. ¿Qué tipo de evidencia es?", ["Es un registro de lo que ocurrió.", "Muestra una conducta observable."], "Registro de conducta observable"),
        ("Explicación incompleta", "Se dice «los jóvenes no participan porque son flojos». ¿Por qué es incompleta?", ["Atribuye todo a un rasgo personal.", "Ignora información, confianza y oportunidades."], "Ignora otros factores"),
    ],
    mistakes=[("Quedarse con la explicación de la persona más importante.", "La jerarquía no prueba que la explicación sea mejor.", "Revisa la evidencia que respalda cada una."),
              ("Tomar un testimonio como si representara a todos los jóvenes.", "Un testimonio muestra una experiencia, no una generalidad.", "Busca datos más amplios.")],
    T=[
        ('abc', '¿Por qué los fenómenos sociales se explican mejor con varias causas?', 'Porque suelen influir factores personales, institucionales y de contexto a la vez', 'Porque cada persona tiene su propia explicación y ninguna es mejor', 'Porque una sola causa nunca puede ser verdadera', 'Una explicación única suele ser incompleta; eso no significa que toda causa sea igual de válida.'),
        ('=', '{F} Si en la comuna hay 2.000 jóvenes habilitados y votan 30 de cada 100, ¿cuántos no votarían?', '2000-2000*30//100', 'Se calcula cuántos votan y se resta del total.', ' jóvenes'),
        ('abc', '{F} ¿Qué factor destaca la investigadora?', 'La percepción de que el voto no cambia nada, junto con más participación en proyectos cercanos', 'La falta de transporte para llegar a los locales de votación de la comuna', 'La falta de información que entrega la autoridad sobre cómo votar', 'Es lo que afirma su postura; el transporte no aparece en la ficha y la información es el foco de la autoridad.'),
        ('abc', '{F} ¿Qué tipo de evidencia es el testimonio del joven?', 'Una experiencia personal que no representa a todos', 'Una encuesta que permite generalizar a la comuna', 'Un registro de asistencia que muestra conductas observables', 'Un testimonio cuenta lo vivido por una persona.'),
        ('abc', '{F} ¿Qué mejora propone la autoridad local?', 'Más información y facilidades para votar', 'Hacer obligatoria la asistencia a proyectos barriales', 'Crear una nueva institución para jóvenes', 'Es lo que dice su postura.'),
        ('=', '{F} Si son 2.000 jóvenes, 45 de cada 100 asisten a proyectos barriales y 30 de cada 100 votan, ¿cuántos jóvenes más asisten a proyectos que votan?', '2000*45//100-2000*30//100', 'Se calcula cada grupo con su proporción y se restan.', ' jóvenes'),
        ('abc', '{F} ¿Qué sugiere el dato de 45 contra 30 de cada 100?', 'Que más jóvenes participan en proyectos cercanos que votan, sin explicar la causa', 'Que los jóvenes rechazan la democracia y prefieren no participar', 'Que los proyectos barriales hacen que baje la votación de los jóvenes', 'Compara dos conductas, pero no prueba por qué ocurre.'),
        ('abc', '{F} ¿Qué perspectiva describe un patrón?', 'La de la investigadora, que observa una regularidad en varios casos', 'La del joven, que cuenta su experiencia personal frente a la votación', 'La de la autoridad, que propone medidas para mejorar el acceso a votar', 'Un patrón es una regularidad que se repite en varios casos.'),
        ('abc', '{F} ¿Cuál es una explicación incompleta de la baja participación?', '«Los jóvenes no participan por flojera»', '«Influyen la información, la confianza y las oportunidades»', '«Hay factores personales y también institucionales»', 'Atribuye todo a un rasgo personal y deja fuera los demás factores.'),
        ('abc', '{F} ¿Qué medida cubre más causas?', 'Informar, abrir proyectos cercanos y facilitar el acceso a votar', 'Solo repartir folletos sobre las elecciones en los barrios de la comuna', 'Solo pedir a los jóvenes que se interesen más en la política', 'Atiende falta de información, de confianza y de acceso a la vez.'),
        ('abc', '{F} ¿Por qué no basta el testimonio del joven?', 'Porque muestra una experiencia individual, no el comportamiento de todos', 'Porque los testimonios siempre son falsos y no se pueden considerar', 'Porque solo vale la opinión de las autoridades de la comuna', 'No es representativo, pero sí es una experiencia que ayuda a entender.'),
        ('abc', '{F} Un alumno concluye: «Con proyectos cercanos se soluciona todo». ¿Qué error comete?', 'Simplifica un problema que tiene varias causas', 'Usa evidencia suficiente de una encuesta', 'Ataca a la persona que propuso otra medida', 'Una sola medida no cubre todas las causas.'),
        ('abc', '{F} ¿Qué dato mejoraría el contraste?', 'Una encuesta a jóvenes de distintos barrios sobre por qué votan o no', 'Más testimonios de jóvenes del mismo barrio sobre su experiencia', 'La opinión de otra autoridad local sobre la baja participación', 'Una muestra amplia y variada permite generalizar mejor.'),
    ],
    ctx=('abc', 'En una asamblea alguien culpa solo a las autoridades de la baja participación. ¿Qué respondes?', 'Que probablemente hay varios factores y conviene mirar la evidencia', 'Que tiene razón, porque las autoridades deciden todo', 'Que la culpa es solo de los jóvenes', 'Los fenómenos sociales suelen tener causas múltiples.'),
    sc=[
        ('¿Qué es una causa múltiple?', 'Un fenómeno explicado por varios factores a la vez', 'Es la idea de que un hecho social rara vez tiene una única causa.'),
        ('abc', '¿Cuándo permite una encuesta generalizar?', 'Cuando la muestra es adecuada', 'Cuando responde mucha gente de un mismo grupo', 'Cuando coincide con la opinión de quien encuesta', 'Una muestra adecuada representa a la población.'),
        ('En Educación Ciudadana: ¿qué es un patrón social?', 'Una regularidad que se repite en varios casos', 'Se detecta al observar muchos casos y no uno solo.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: causa que destacan, tipo de evidencia y límite. Luego escribe una explicación propia de tres líneas que combine las tres, y una medida que no culpe a un solo actor.",
        "Joven: falta de información; testimonio; no representa a todos. Investigadora: percepción de ineficacia; patrón; falta de datos amplios. Autoridad: falta de información y acceso; propuesta; sin evidencia. Mi explicación: hay desinformación, desconfianza y falta de espacios. Medida: información, proyectos cercanos y facilidad para votar.",
        ["identifica causas", "distingue tipos de evidencia", "propone una explicación completa"], ["tabla de tres perspectivas", "explicación y medida"], ["quedarse con una sola explicación", "culpar a un actor"],
        "Pregunta qué dato cambiaría su explicación."),
    reinforce="Escribe tres posibles causas de un problema de tu liceo y qué evidencia buscarías.",
    extend="Entrevista a una persona de confianza sobre por qué cree que la gente participa o no, y anota si su respuesta es testimonio o patrón.",
)

# ============================================================ OA 03, clase 4
F = ("Ficha 15 (tema de deliberación de ejemplo): una comuna ficticia estudia dos medidas contra la corrupción en las compras públicas. "
     "Medida 1: publicar en internet todos los contratos y los nombres de las empresas. Medida 2: aumentar las sanciones a quienes incumplan. "
     "Argumento a favor de la 1: la transparencia permite que la ciudadanía vigile. Objeción a la 1: puede exponer datos sensibles. "
     "Argumento a favor de la 2: disuade. Objeción a la 2: si nadie vigila, las sanciones no se aplican. Presupuesto de ejemplo: 10 millones para una sola medida.")
build(
    O3, 4, F,
    use="Aprenderé a deliberar sobre cómo enfrentar un riesgo para la democracia, comparando medidas, sus ventajas y sus costos, y llegando a una propuesta fundamentada.",
    prior=["Sé qué es la corrupción.", "Sé estructurar un argumento con tesis, razón y evidencia.", "Sé reconocer objeciones."],
    explain=[
        "Las medidas contra un riesgo se evalúan con criterios: si atacan una causa, si respetan derechos, si son viables y si tienen costos o efectos secundarios. La transparencia (hacer pública la información) permite el control ciudadano. La sanción disuade, pero depende de que alguien detecte las faltas y de que la justicia actúe.",
        "En una deliberación se examina cada medida junto con su objeción. Para decidir, se pregunta qué ocurre si se aplican juntas, si hay una versión más simple y qué derechos podrían afectarse. Proteger datos personales no se opone a la transparencia: se puede publicar contratos sin exponer datos sensibles de personas.",
        "Una propuesta fundamentada incluye la medida, su razón, la evidencia, cómo se enfrenta la objeción y cómo se sabrá si funciona. Al terminar, quien disiente tiene derecho a que se registre su postura. Deliberar bien no exige unanimidad, sino razones honestas, respeto y decisión informada.",
    ],
    vocab=[("transparencia", "hacer pública la información para que pueda ser revisada"), ("disuadir", "desalentar una conducta por el temor a sus consecuencias"), ("sanción", "castigo previsto para quien incumple una norma"), ("criterio de evaluación", "aspecto que se usa para juzgar una medida"), ("dato sensible", "información personal que debe protegerse")],
    worked=[
        ("Aplicar criterios", "Una medida de ejemplo ataca una causa y es barata, pero afecta la privacidad. ¿Qué criterios cumple y cuál no?", ["Cumple causa y costo.", "No cumple el respeto de derechos."], "Cumple causa y costo; falla en privacidad"),
        ("Ajustar una medida", "Para publicar contratos sin exponer datos personales, ¿qué ajuste sirve?", ["Se publica el contrato y se ocultan datos sensibles.", "Se mantiene el control ciudadano."], "Publicar ocultando datos sensibles"),
    ],
    mistakes=[("Elegir una medida solo por ser más dura.", "Una sanción alta sin control no se aplica.", "Revisa si hay quien detecte las faltas."),
              ("Creer que transparencia y privacidad se oponen siempre.", "Se pueden proteger los datos sensibles y publicar lo demás.", "Busca el ajuste que respete ambos.")],
    T=[
        ('abc', '¿Qué es la transparencia?', 'Hacer pública la información para que pueda ser revisada', 'Guardar la información para que solo la vea la autoridad', 'Publicar los datos personales de todas las personas', 'La transparencia permite el control ciudadano; no obliga a exponer datos personales.'),
        ('abc', '¿Qué busca lograr una sanción, según la clase?', 'Disuadir: desalentar una conducta por temor a sus consecuencias', 'Vigilar: detectar las faltas cuando ocurren', 'Compensar: reparar el daño de quienes lo sufrieron', 'Disuadir es el efecto esperado de una sanción; vigilar es otra función.'),
        ('abc', '{F} El presupuesto alcanza para una sola medida. ¿Qué criterio de evaluación obliga a elegir?', 'Viabilidad: cuál cabe en los recursos disponibles', 'Disuasión: cuál desalienta más las faltas', 'Probidad: cuál es más honesta', 'La viabilidad pregunta si la medida se puede aplicar con los recursos que hay.'),
        ('abc', '{F} ¿Qué permite la transparencia, según la ficha?', 'Que la ciudadanía vigile las compras públicas', 'Que las empresas oculten sus nombres', 'Que se apliquen sanciones sin investigar', 'Es el argumento a favor de la medida 1.'),
        ('abc', '{F} ¿Cuál es la objeción a la medida 1?', 'Puede exponer datos sensibles', 'No permite que la ciudadanía vigile', 'Disuade solo a las empresas pequeñas', 'Es la objeción que registra la ficha.'),
        ('abc', '{F} ¿Cuál es la objeción a la medida 2?', 'Si nadie vigila, las sanciones no se aplican', 'Expone datos sensibles de las personas', 'Reduce la libertad de las empresas para competir', 'La sanción depende de que alguien detecte las faltas.'),
        ('abc', '{F} ¿Qué ajuste responde a la objeción de la medida 1?', 'Publicar los contratos y los montos, protegiendo los datos sensibles de personas', 'Publicar solo los contratos que la autoridad considere convenientes', 'Publicar los datos personales de todas las personas involucradas', 'Mantiene la transparencia sin exponer datos sensibles.'),
        ('abc', '{F} ¿Qué relación hay entre ambas medidas?', 'La transparencia ayuda a detectar faltas que luego pueden sancionarse', 'Son incompatibles: una anula a la otra y hay que elegir una sola', 'La sanción hace innecesaria la transparencia, porque basta con castigar', 'La detección es condición para que la sanción se aplique.'),
        ('abc', '{F} Se elige la medida 2. ¿Qué condición necesita para disuadir?', 'Que alguien detecte las faltas y la justicia actúe', 'Que las empresas conozcan los datos sensibles de los funcionarios', 'Que se publique el presupuesto de la comuna', 'Sin detección y sin actuación de la justicia, la sanción no se aplica.'),
        ('abc', '{F} ¿Qué propuesta es más sólida?', 'Medida 1 ajustada para proteger datos y, si hay recursos, reforzar el control', 'Medida 2 sola, sin ningún mecanismo de vigilancia que detecte las faltas', 'Medida 1 tal como está, sin responder la objeción sobre los datos personales', 'Combina control y consecuencias y responde a las objeciones.'),
        ('abc', '{F} Un participante dice: «Elijamos la 2, que es más dura». ¿Qué le preguntas?', '¿Quién detectará las faltas para que las sanciones se apliquen?', '¿Quién propuso primero la medida y quién la defendió con más fuerza?', '¿Cuántos participantes apoyan la medida más dura y cuántos la rechazan?', 'La pregunta debe responder a la objeción de la medida 2, no al orden ni al apoyo.'),
        ('abc', '{F} ¿Qué indicador mostraría si la medida 1 funciona?', 'Cuántos contratos son revisados por la ciudadanía y cuántas faltas se detectan', 'Cuántos afiches se imprimieron para difundir la medida en la comuna', 'Cuántas empresas aparecen en la lista publicada en internet', 'Mide resultados de la medida y no solo actividades.'),
        ('abc', '{F} Si una minoría no está de acuerdo con la decisión, ¿qué corresponde?', 'Registrar su postura y respetar la decisión informada', 'Repetir la votación hasta que cambie', 'Pedir a la minoría que se retire de la discusión', 'Deliberar bien no exige unanimidad, pero sí respeto por quienes discrepan.'),
    ],
    ctx=('abc', 'Un colegio de ejemplo debe decidir entre vigilar todo el patio con cámaras o fomentar la denuncia anónima de violencia. ¿Qué criterio conviene mirar?', 'Efectos sobre la privacidad y la confianza', 'Solo la rapidez con que se instale cada alternativa', 'Solo el costo de cada alternativa para el colegio', 'Los criterios de evaluación incluyen el respeto de derechos y las consecuencias.'),
    sc=[
        ('¿Qué es la transparencia?', 'Hacer pública la información para que pueda ser revisada', 'Permite que la ciudadanía vigile y exija cuentas.'),
        ('abc', '¿Qué es un criterio de evaluación?', 'Una pregunta con que se juzga una medida, como si es viable o respeta derechos', 'Una opinión sobre cuál medida es la mejor según cada participante', 'El resultado final de una votación sobre las medidas propuestas', 'Los criterios permiten comparar medidas de forma ordenada.'),
        ('¿Qué es un dato sensible?', 'Información personal que debe protegerse', 'Si se expone puede perjudicar a las personas.'),
    ],
    op=("Con la {F} escribe una propuesta de siete líneas: tu medida elegida, razón, evidencia o argumento de la ficha, objeción, tu respuesta, cómo la ajustarías y qué indicador usarías. Evita nombrar partidos o personas.",
        "Elijo la medida 1 ajustada. Razón: permite vigilar. Argumento: la ficha dice que la ciudadanía puede vigilar. Objeción: expone datos. Respuesta: se ocultan datos sensibles. Ajuste: complementar con control. Indicador: revisiones ciudadanas y faltas detectadas.",
        ["responde objeciones", "usa criterios", "propone indicador"], ["propuesta de siete líneas"], ["elegir sin considerar costos", "ignorar derechos"],
        "Pregunta cómo registraría la postura de quien disiente."),
    reinforce="Elige un riesgo y escribe dos medidas con una ventaja y un costo cada una.",
    extend="Anota un ejemplo cotidiano de transparencia en tu liceo.",
)

# ============================================================ OA 04, clase 1
F = ("Ficha 16 (economía ficticia de Valle Dulce, con cifras inventadas): una fábrica de zapatos produce 400 pares al mes con 20 trabajadores. "
     "El mercado fija el precio por oferta y demanda. El Estado cobra un impuesto de 10 % sobre las ventas, fiscaliza condiciones laborales y paga escuelas y hospitales. "
     "Una cooperativa vende café con comercio justo: paga un precio mínimo a las familias productoras.")
build(
    O4, 1, F,
    use="Aprenderé a explicar cómo se relacionan el Estado y el mercado: sueldos, productividad, impuestos, comercio justo, probidad, sustentabilidad y desigualdad.",
    prior=["Sé que hay empresas, trabajadores y consumidores.", "Sé qué es un impuesto.", "Sé calcular un porcentaje simple."],
    explain=[
        "El mercado es el lugar o sistema donde se intercambian bienes y servicios a un precio que depende de la oferta (cuánto se ofrece) y la demanda (cuánto se quiere comprar). El Estado participa de varias formas: regula, fiscaliza, cobra impuestos, entrega servicios como educación y salud, y busca proteger derechos, por ejemplo los laborales.",
        "Algunos conceptos permiten evaluar esa relación. La productividad mide cuánto se produce por trabajador o por hora. Un sueldo justo busca un pago digno por el trabajo. La carga tributaria es el peso de los impuestos. El comercio justo paga precios y condiciones dignas a productores. La probidad es la conducta honesta de quien ejerce una función pública. El desarrollo sustentable satisface necesidades de hoy sin dañar a las generaciones futuras.",
        "La riqueza y la pobreza se relacionan con la distribución de ingresos y oportunidades. No hay una única forma correcta de equilibrar Estado y mercado: distintas posturas valoran de manera diferente la libertad económica, la igualdad y el rol del Estado. Para estudiarlas se usan criterios y evidencias, no etiquetas.",
    ],
    vocab=[("mercado", "sistema de intercambio de bienes y servicios a un precio"), ("productividad", "cantidad producida por trabajador o por hora"), ("carga tributaria", "peso de los impuestos sobre personas o empresas"), ("comercio justo", "comercio que paga precios y condiciones dignas a productores"), ("probidad", "conducta honesta de quien cumple una función pública")],
    worked=[
        ("Calcular productividad", "Una fábrica de ejemplo produce 300 sillas con 10 trabajadores. ¿Cuántas sillas produce por trabajador?", ["Se divide el total de sillas entre los trabajadores.", "300 entre 10."], "30 sillas por trabajador"),
        ("Calcular un impuesto", "Una venta de ejemplo es de 2.000 pesos y el impuesto es 10 %. ¿Cuánto es el impuesto?", ["10 % es una décima parte.", "2.000 entre 10."], "200 pesos"),
    ],
    mistakes=[("Pensar que el mercado funciona sin ninguna regla.", "Las reglas protegen derechos y aseguran la competencia.", "Identifica qué normas lo regulan."),
              ("Confundir productividad con trabajar más horas.", "Se trata de cuánto se produce por trabajador o por hora.", "Divide producción por trabajadores u horas.")],
    T=[
        ('abc', '¿De qué depende el precio en un mercado, según la clase?', 'De la oferta (cuánto se ofrece) y la demanda (cuánto se quiere comprar)', 'Solo de lo que decide el Estado cada año, sin relación con los consumidores', 'Solo del costo de producir cada bien, sin importar cuánto se quiere comprar', 'El precio de mercado resulta de la oferta y la demanda.'),
        ('=', '{F} Si cada par se vende a 20.000 pesos y se venden los 400 pares del mes, ¿cuánto impuesto (10 %) se recauda?', '400*20000*10//100', 'Se calcula el total de ventas y se toma el 10 %.', ' pesos'),
        ('=', '{F} ¿Cuántos pares produce cada trabajador al mes, en promedio?', '400//20', 'La productividad se calcula dividiendo la producción entre los trabajadores.', ' pares'),
        ('abc', '{F} ¿Cuál de estas tareas del Estado aparece en la ficha?', 'Fiscalizar las condiciones laborales', 'Fijar el precio de los zapatos', 'Administrar la fábrica de zapatos', 'La ficha dice que el Estado fiscaliza condiciones laborales y paga escuelas y hospitales; el precio lo fija el mercado.'),
        ('abc', '{F} ¿Qué es el comercio justo en la cooperativa?', 'Pagar un precio mínimo a las familias productoras', 'Vender al precio más bajo posible a los consumidores', 'Pagar un precio que depende solo de la demanda del día', 'Busca precios y condiciones dignas para quienes producen.'),
        ('abc', '¿Qué mide la productividad?', 'Cuánto se produce por cada trabajador o por hora', 'Cuánto gana cada trabajador por su producción', 'Cuánto cuesta producir cada par de zapatos', 'Relaciona la producción con el trabajo empleado.'),
        ('abc', '{F} ¿Qué rol cumple el Estado al fiscalizar condiciones laborales?', 'Proteger los derechos de los trabajadores', 'Fijar el precio de los zapatos', 'Cobrar el impuesto del 10 % a la fábrica', 'Fiscalizar es controlar que se cumplan las normas laborales.'),
        ('=', '{F} Si la fábrica produce 500 pares con los mismos 20 trabajadores, ¿en qué porcentaje subió la productividad?', '(500//20-400//20)*100//(400//20)', 'Se calcula la productividad antes y después y se compara el aumento con la inicial.', ' %'),
        ('abc', '{F} Alguien dice: «Si sube la productividad, el sueldo debe subir automáticamente». ¿Qué corresponde?', 'Es un argumento posible, pero el sueldo también depende de costos, normas y negociación', 'Es una regla obligatoria que el Estado aplica a todas las empresas', 'Es falso, porque la productividad nunca influye en el sueldo', 'El sueldo se define considerando varios factores; la productividad es solo uno de ellos.'),
        ('abc', '{F} ¿Cuál de estos es un ejemplo de falta de probidad?', 'Una autoridad adjudica un contrato a un familiar', 'Una autoridad publica sus cuentas', 'Una autoridad cobra un impuesto autorizado por ley', 'La probidad es la conducta honesta en una función pública; favorecer a un familiar la contradice.'),
        ('abc', '{F} ¿Por qué se dice que no hay una única forma de equilibrar Estado y mercado?', 'Porque distintas posturas valoran de forma diferente la libertad económica y la igualdad', 'Porque el mercado funciona sin ninguna regla y nadie lo estudia', 'Porque los datos económicos siempre son falsos y no sirven para decidir', 'Hay valores distintos en juego; por eso se usan criterios y evidencias.'),
        ('abc', '{F} ¿Qué es el desarrollo sustentable?', 'Satisfacer las necesidades de hoy sin dañar a las generaciones futuras', 'Producir lo máximo posible mientras haya demanda y sin pensar en el futuro', 'Ahorrar todo y no usar ningún recurso para no dañar a nadie', 'La definición incluye pensar en el futuro.'),
        ('abc', 'Una comuna de ejemplo cobra un impuesto a un taller y con ese dinero repara la plaza. ¿Qué relación Estado-mercado muestra?', 'El cobro de un tributo que financia un bien común', 'Un taller que fija precios al Estado', 'Un servicio gratuito del Estado para las empresas', 'El Estado cobra impuestos y entrega bienes públicos.'),
    ],
    ctx=('abc', 'Una autoridad anuncia que no cobrará impuestos a las empresas del barrio por un año. ¿Qué concepto cambia?', 'La carga tributaria', 'La probidad', 'El comercio justo', 'La carga tributaria es el peso de los impuestos.'),
    sc=[
        ('¿Qué es la probidad?', 'La conducta honesta de quien cumple una función pública', 'Implica no usar el cargo para beneficio privado.'),
        ('abc', '¿Qué es la carga tributaria?', 'El peso de los impuestos', 'El precio de las cosas', 'El total de ventas de una empresa', 'Mide cuánto se paga en tributos.'),
        ('¿Qué es el mercado?', 'Lugar o sistema donde se intercambian bienes y servicios a un precio que depende de la oferta y la demanda', 'Allí se encuentran quienes ofrecen y quienes quieren comprar.'),
    ],
    op=("Con la {F} escribe una tabla con tres filas: (1) un rol del Estado y un ejemplo; (2) un rol del mercado y un ejemplo; (3) una relación entre ambos. Calcula también la productividad por trabajador. Termina con una pregunta que quede abierta.",
        "Estado: cobra impuestos y paga escuelas. Mercado: intercambia zapatos por precio. Relación: el impuesto del 10 % financia servicios. Productividad: 400 entre 20 son 20 pares. Pregunta: ¿qué impuesto es justo?",
        ["identifica roles", "calcula con datos", "formula pregunta abierta"], ["tabla de tres filas", "cálculo"], ["confundir Estado y mercado", "dar una sola respuesta correcta a una pregunta de valores"],
        "Pregunta qué valor está detrás de su pregunta abierta."),
    reinforce="Explica con tus palabras qué es productividad y da un ejemplo con cifras de ejemplo.",
    extend="Anota un bien público que usas y quién lo financia.",
)

# ============================================================ OA 04, clase 2
F = ("Ficha 17 (caso de ejemplo): la empresa ficticia «Frutas del Sur» aumentó su producción de 1.000 a 1.200 cajas al mes con los mismos 20 trabajadores. "
     "Los trabajadores piden que el sueldo suba; la empresa responde que sus costos subieron. Datos de ejemplo: sueldo mensual actual por persona 600.000 pesos; ingresos de la empresa por caja 15.000 pesos; "
     "el sindicato pide un reajuste de 5 %. Fuentes: carta del sindicato, informe de costos de la empresa, nota de la inspección del trabajo (indica que se cumplen las normas básicas).")
build(
    O4, 2, F,
    use="Aprenderé a investigar un caso que relaciona trabajo, productividad y sueldos, usando cifras y fuentes, sin tomar partido por anticipado.",
    prior=["Sé qué es productividad.", "Sé calcular porcentajes simples.", "Sé comparar fuentes."],
    explain=[
        "En un caso de empresa se miran varias cifras: producción, productividad, ingresos, costos y sueldos. La productividad por trabajador se calcula dividiendo la producción total entre el número de trabajadores. Si sube, la empresa produce más con el mismo personal, pero eso no define por sí solo cuánto debe subir el sueldo.",
        "El sueldo se negocia considerando varios factores: productividad, costos de la empresa, normas laborales, situación del mercado y el costo de vida de las personas. Un sindicato representa a trabajadores en esa negociación. El Estado fiscaliza que se cumplan los mínimos legales y puede mediar, pero no fija cada acuerdo.",
        "Investigar el caso exige separar hechos de opiniones: «la producción subió» es un hecho; «es injusto» es una valoración que necesita criterios. Se anotan las fuentes, sus propósitos y los datos que faltan, como los costos detallados. Se evita dar por probado que una de las partes miente.",
    ],
    vocab=[("sindicato", "organización de trabajadores que los representa en negociaciones"), ("reajuste", "aumento de un valor, como un sueldo, en un porcentaje"), ("costos", "gastos que la empresa debe pagar para producir"), ("fiscalizar", "controlar que se cumplan las normas"), ("negociación", "diálogo para llegar a un acuerdo entre partes")],
    worked=[
        ("Calcular un reajuste", "Un sueldo de ejemplo de 500.000 pesos sube 10 %. ¿Cuánto es el aumento?", ["10 % de 500.000 es una décima parte.", "500.000 entre 10."], "50.000 pesos"),
        ("Hecho u opinión", "«La empresa produjo más» y «la empresa es injusta». ¿Cuál es hecho?", ["La primera se puede medir.", "La segunda es una valoración."], "La primera"),
    ],
    mistakes=[("Suponer que más productividad obliga a un reajuste exacto.", "El reajuste se negocia con varios factores.", "Considera costos, mercado y acuerdos."),
              ("Dar por probado que una parte miente.", "No hay datos para afirmarlo.", "Pide la información que falta.")],
    T=[
        ('abc', '¿Cómo se calcula la productividad por trabajador?', 'Dividiendo la producción total entre el número de trabajadores', 'Multiplicando la producción por el sueldo promedio', 'Dividiendo los ingresos entre los costos', 'La productividad por trabajador relaciona producción y trabajadores.'),
        ('=', '{F} ¿Cuántas cajas más produce ahora cada trabajador que antes del aumento?', '1200//20-1000//20', 'Se calcula la producción por trabajador antes y después y se resta.', ' cajas'),
        ('=', '{F} ¿En qué porcentaje aumentó la producción total de cajas?', '(1200-1000)*100//1000', 'Se compara el aumento con la producción inicial.', ' %'),
        ('=', '{F} Si se concediera el reajuste de 5 %, ¿cuál sería el nuevo sueldo mensual por persona?', '600000+600000*5//100', 'Se suma al sueldo actual el 5 % de ese sueldo.', ' pesos'),
        ('abc', '{F} ¿Qué informa la nota de la inspección del trabajo?', 'Que se cumplen las normas básicas, sin decir si el sueldo debe subir', 'Que la empresa debe subir el sueldo en 5 % porque aumentó su producción', 'Que la empresa infringió las normas laborales básicas con sus trabajadores', 'La inspección fiscaliza los mínimos legales, no fija cada acuerdo de sueldo.'),
        ('abc', '{F} ¿Cuál de estas frases es un hecho?', '«La producción subió de 1.000 a 1.200 cajas»', '«El reajuste pedido es injusto»', '«La empresa miente sobre sus costos»', 'Un hecho se puede medir; las otras dos son valoraciones o acusaciones sin evidencia.'),
        ('abc', '{F} ¿Qué argumento da la empresa?', 'Que sus costos subieron', 'Que la producción no aumentó', 'Que el sindicato no representa a los trabajadores', 'Lo dice la ficha: la empresa responde que sus costos subieron.'),
        ('abc', '{F} ¿Qué dato falta para evaluar el argumento de la empresa?', 'El detalle de los costos', 'La edad promedio de los trabajadores', 'El nombre de la inspección', 'Sin saber cuánto y en qué subieron los costos no se puede evaluar el argumento.'),
        ('abc', '{F} Alguien dice: «La empresa miente». ¿Qué corresponde?', 'Pedir el detalle de los costos antes de afirmarlo', 'Aceptarlo, porque la empresa tiene más poder', 'Responder que el sindicato exagera', 'No se debe dar por probado que una parte miente sin evidencia.'),
        ('=', '{F} Si cada caja se vende a 15.000 pesos, ¿cuánto más ingresa la empresa por las 200 cajas adicionales?', '200*15000', 'Se multiplica el aumento de producción por el ingreso por caja.', ' pesos'),
        ('=', '{F} ¿Cuánto costaría al mes el reajuste de 5 % para los 20 trabajadores?', '20*600000*5//100', 'Se calcula el 5 % de un sueldo y se multiplica por los trabajadores.', ' pesos'),
        ('abc', '{F} Con 3.000.000 de pesos de ingresos adicionales y un costo de reajuste de 600.000 al mes, ¿qué conclusión es prudente?', 'El reajuste cabría en los ingresos adicionales, pero falta saber cuánto subieron los costos', 'La empresa miente porque sus ingresos subieron y dice que sus costos aumentaron', 'El reajuste es obligatorio por ley porque la producción aumentó en 200 cajas', 'Los ingresos no son lo único: sin el detalle de costos no se puede afirmar nada más.'),
        ('abc', '{F} ¿Qué solución intermedia puede proponerse?', 'Un reajuste menor al 5 % o un bono ligado a la productividad', 'Mantener el sueldo sin conversar mientras no suban los costos', 'Subir el sueldo en 5 % sin revisar los costos', 'Combina el interés de los trabajadores con el de la empresa.'),
    ],
    ctx=('abc', 'Una empresa de ejemplo sube su productividad y el sindicato pide mejor sueldo. ¿Qué paso corresponde?', 'Negociar con datos de ambas partes', 'Imponer una cifra sin diálogo', 'Esperar a que el Estado fije el sueldo', 'La negociación usa evidencia de las partes; el Estado fiscaliza mínimos pero no fija cada acuerdo.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un sindicato?', 'Una organización de trabajadores que los representa', 'Representa a los trabajadores en la negociación con la empresa.'),
        ('abc', '¿Qué significa fiscalizar?', 'Controlar que se cumplan las normas', 'Fijar el precio de un producto', 'Negociar el sueldo con la empresa', 'El Estado fiscaliza que se respeten los mínimos legales.'),
        ('¿Qué es un reajuste?', 'Un aumento de un valor en un porcentaje', 'Por ejemplo, un reajuste de 5 % sube un sueldo en esa proporción.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: (1) cálculo de productividad antes y ahora; (2) dos hechos; (3) una valoración; (4) dos datos que faltan; (5) una propuesta intermedia y qué parte de cada postura recoge.",
        "(1) 50 y 60 cajas por trabajador. (2) Producción subió; la inspección ve normas básicas cumplidas. (3) «Es injusto». (4) Detalle de costos; porcentaje de ganancia. (5) Reajuste de 3 % más bono por productividad: recoge costos y productividad.",
        ["calcula bien", "separa hechos de valoraciones", "propone solución intermedia"], ["informe de cinco puntos"], ["afirmar mentiras sin datos", "no calcular"],
        "Pregunta qué cifras revisaría en la empresa."),
    reinforce="Calcula el 10 % de tres sueldos de ejemplo y explica qué significa.",
    extend="Anota qué datos pedirías para evaluar si el sueldo mínimo debería subir, sin dar una opinión.",
)

# ============================================================ OA 04, clase 3
F = ("Ficha 18 (perspectivas de ejemplo sobre un impuesto a las bebidas azucaradas en un país ficticio). "
     "Perspectiva 1 (productor): «El impuesto sube los precios, reduce las ventas y los empleos». "
     "Perspectiva 2 (médica): «Reduce el consumo de azúcar y financia programas de salud». "
     "Perspectiva 3 (economista): «Su efecto depende de cuánto cambia el consumo; hay que medirlo». "
     "Datos de ejemplo: el impuesto sube el precio de 1.000 a 1.200 pesos; las ventas bajan de 100 a 85 unidades.")
build(
    O4, 3, F,
    use="Aprenderé a contrastar posturas sobre la intervención del Estado en el mercado, presentando sus argumentos y su evidencia sin tomar partido.",
    prior=["Sé qué es un impuesto.", "Sé calcular porcentajes simples.", "Sé comparar perspectivas."],
    explain=[
        'El Estado puede intervenir en el mercado con impuestos, regulaciones o subsidios (ayudas económicas). Algunas posturas valoran más la libertad económica y desconfían de la intervención; otras valoran más la igualdad o la protección social y apoyan una intervención mayor. Ambas buscan el bienestar, pero con prioridades distintas. El efecto distributivo es la forma en que se reparten los costos y beneficios de una medida entre distintos grupos.',
        'Para contrastar, se identifican los valores (libertad económica, salud, empleo), los efectos esperados (precios, consumo, recaudación) y la evidencia que los respalda. Un impuesto puede reducir un consumo y a la vez recaudar dinero, pero también puede afectar el empleo o a personas con menos ingresos, que gastan una mayor proporción en el producto.',
        'La evidencia ayuda a decidir, pero no elimina los desacuerdos de valores. Se pregunta: ¿cuánto cambió el consumo?, ¿quién paga más?, ¿se usa lo recaudado para algo concreto? Una buena discusión reconoce lo que cada postura aporta y evita caricaturas, como decir que alguien «no quiere salud» o «no quiere empleo».',
    ],
    vocab=[("subsidio", "ayuda económica del Estado para aliviar un costo"), ("recaudación", "dinero que obtiene el Estado por impuestos"), ("regulación", "norma que fija reglas a una actividad"), ("efecto distributivo", "forma en que una medida reparte costos y beneficios entre grupos"), ("caricatura", "versión exagerada de la postura del otro")],
    worked=[
        ("Calcular variación de precio", "Un producto de ejemplo sube de 500 a 600 pesos. ¿Cuánto subió?", ["Se resta 500 a 600.", "Aumento de 100 pesos."], "100 pesos"),
        ("Identificar un valor", "Alguien dice «Que el Estado no se meta en mis decisiones de compra». ¿Qué valor defiende?", ["Defiende su libertad de elegir.", "Es libertad económica."], "Libertad económica"),
    ],
    mistakes=[("Presentar la postura contraria como una caricatura.", "Se deforma lo que realmente dice.", "Reformula su argumento con tus palabras y valida su preocupación."),
              ("Creer que la evidencia por sí sola elimina los desacuerdos.", "Los valores influyen en lo que se prioriza.", "Distingue qué se discute: datos o valores.")],
    T=[
        ('abc', '¿Qué diferencia hay entre un impuesto y un subsidio?', 'El impuesto cobra dinero sobre un bien o actividad; el subsidio es una ayuda económica', 'El impuesto es una ayuda económica y el subsidio es un cobro al consumidor', 'Ambos son multas que el Estado aplica a quienes incumplen una norma', 'Se trata de instrumentos distintos que el Estado usa para influir en el mercado.'),
        ('=', '{F} ¿En qué porcentaje subió el precio con el impuesto?', '(1200-1000)*100//1000', 'Se compara el aumento con el precio inicial.', ' %'),
        ('abc', '{F} ¿Qué valor destaca la médica?', 'La salud, al reducir el consumo de azúcar', 'La libertad de comercio sin intervención', 'El empleo en la industria', 'Su postura habla de menor consumo de azúcar y de programas de salud.'),
        ('abc', '{F} ¿Qué efecto teme el productor?', 'Que bajen las ventas y los empleos', 'Que suba el consumo de azúcar', 'Que se recaude demasiado', 'Es la preocupación que expresa su postura.'),
        ('abc', '{F} ¿Qué dice el economista?', 'Que el efecto depende de cuánto cambia el consumo y hay que medirlo', 'Que el impuesto siempre reduce el consumo, sin importar cuánto cambie el precio', 'Que el impuesto nunca afecta el empleo, porque las ventas no cambian', 'El economista pide medir antes de concluir.'),
        ('abc', '{F} ¿Qué dato respalda parcialmente a la médica?', 'La baja de ventas de 100 a 85 unidades, que sugiere menor consumo', 'El alza del precio de 1.000 a 1.200 pesos, que prueba menos azúcar', 'La existencia del impuesto, que financia programas', 'Menos unidades vendidas apuntan a menor consumo, aunque no prueban el efecto en salud.'),
        ('=', '{F} Si el impuesto es de 200 pesos por unidad y se venden 85 unidades, ¿cuánto se recauda?', '200*85', 'Se multiplica el impuesto por las unidades vendidas.', ' pesos'),
        ('abc', '{F} ¿Qué dato respalda la preocupación del productor?', 'La baja de ventas, que podría afectar los empleos', 'La recaudación del impuesto, que financia programas de salud', 'La opinión de la médica sobre el consumo de azúcar', 'Menos ventas pueden reducir ingresos y empleos de la empresa.'),
        ('abc', '{F} ¿Qué es el efecto distributivo del impuesto?', 'Quién paga más del costo, por ejemplo quienes gastan más proporción de sus ingresos', 'Cuánto baja el consumo total del producto en el país', 'Cuánto dinero recauda el Estado con el impuesto en un año', 'Se refiere a cómo se reparten los costos entre grupos.'),
        ('abc', '{F} Alguien dice: «La médica no quiere que haya empleo». ¿Qué error comete?', 'Una caricatura: deforma lo que ella dijo', 'Presenta un dato verificable', 'Responde con una objeción basada en evidencia', 'Su postura habla de salud, no de rechazar el empleo.'),
        ('abc', '{F} ¿Qué pregunta es útil para decidir?', '¿Se destina lo recaudado a los programas de salud que se mencionan?', '¿Quién de los tres participantes habló con más seguridad ante el grupo?', '¿Qué perspectiva tiene más seguidores en las redes sociales?', 'Se relaciona con el objetivo declarado de la medida.'),
        ('abc', '{F} ¿Qué solución intermedia podría combinar los valores en tensión?', 'Impuesto moderado junto con información al consumidor y apoyo a los empleos afectados', 'Eliminar el impuesto y todo programa de salud para no afectar el empleo', 'Subir el impuesto hasta que nadie compre y desaparezca el consumo', 'Combina salud y empleo sin sacrificar del todo ninguno.'),
        ('abc', '{F} ¿Qué diferencia hay entre «el impuesto redujo las ventas» y «el impuesto causó el cierre de empleos»?', 'La primera es un dato observado; la segunda es una causa que el dato no prueba', 'Ninguna: si bajan las ventas, siempre se pierden empleos en la industria', 'La segunda es un dato observado y la primera es una opinión sin evidencia', 'Las ventas se miden; que la baja cause pérdida de empleos requiere más evidencia.'),
    ],
    ctx=('abc', 'Se debate si el Estado debe subsidiar el transporte público. ¿Qué dos valores pueden entrar en tensión?', 'Igualdad de acceso y costo para el Estado', 'Probidad y transparencia, que no pueden convivir', 'Igualdad de acceso y libertad de culto', 'Un subsidio favorece el acceso, pero tiene un costo que otros pagan.'),
    sc=[
        ('¿Qué es la recaudación?', 'El dinero que obtiene el Estado por impuestos', 'Se suma de los tributos pagados por personas y empresas.'),
        ('abc', '¿Qué es una caricatura de una postura?', 'Una versión exagerada o deformada de lo que dice el otro', 'Un resumen fiel y completo de lo que dice la otra persona', 'Un dibujo humorístico que ilustra el tema de la discusión', 'Deformar el argumento impide discutirlo con evidencia.'),
        ('¿Qué es una regulación?', 'Una norma del Estado que fija reglas a una actividad', 'Por ejemplo, reglas sobre publicidad o etiquetado de un producto.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: valor, efecto que esperan, evidencia y pregunta que dejan abierta. Escribe un acuerdo posible que mantenga la neutralidad frente a partidos.",
        "Productor: empleo; menos ventas; baja de 100 a 85; ¿cuántos empleos se perdieron? Médica: salud; menos consumo; baja de ventas; ¿baja el consumo total de azúcar? Economista: medición; efecto variable; datos; ¿cuánto cambia a largo plazo? Acuerdo: medir y ajustar el impuesto.",
        ["identifica valores", "usa evidencia", "evita caricaturas"], ["tabla de tres perspectivas", "acuerdo"], ["tomar partido", "caricaturizar"],
        "Pregunta qué evidencia haría cambiar de opinión."),
    reinforce="Explica con tus palabras un impuesto y un efecto posible.",
    extend="Anota un subsidio o impuesto que conozcas y qué objetivo declarado tiene.",
)

# ============================================================ OA 04, clase 4
F = ("Ficha 19 (tema de deliberación de ejemplo): una comuna ficticia debate si exigir a las empresas que compren a productores locales al menos el 30 % de sus insumos. "
     "A favor: fortalece el empleo local y reduce el transporte. En contra: puede subir los costos si los proveedores locales son más caros. "
     "Datos de ejemplo: una empresa compra insumos por 100 millones de pesos al año; hoy compra 10 millones a proveedores locales.")
build(
    O4, 4, F,
    use="Aprenderé a deliberar sobre una política que relaciona Estado, mercado y desarrollo sustentable, con razones, datos y propuestas viables.",
    prior=["Sé contrastar posturas sobre impuestos y regulaciones.", "Sé estructurar un argumento.", "Sé calcular proporciones."],
    explain=[
        "Una política pública es una decisión del Estado para enfrentar un problema. Se evalúa con criterios: eficacia (si logra el objetivo), eficiencia (si usa bien los recursos), equidad (si trata justamente a los grupos), sustentabilidad (si es viable sin dañar el futuro) y probidad (si se aplica con honestidad).",
        "Una exigencia como comprar localmente tiene beneficios (empleo cercano, menor transporte) y riesgos (costos más altos, menor competencia). La deliberación examina quién gana, quién pierde, qué plazo se da y cómo se compensa. Una propuesta gradual, por ejemplo subir la exigencia por etapas, puede equilibrar ambos efectos.",
        "Para argumentar se plantea la tesis, la razón con datos, la objeción y la respuesta. También se explica cómo se vigilará su aplicación. Se evita presentar la política como mágica: toda decisión tiene costos de oportunidad, es decir, lo que se deja de hacer por elegir otra cosa.",
    ],
    vocab=[("política pública", "decisión del Estado para enfrentar un problema"), ("eficacia", "grado en que se logra el objetivo"), ("eficiencia", "buen uso de los recursos para lograr un objetivo"), ("costo de oportunidad", "lo que se deja de hacer al elegir otra opción"), ("gradualidad", "aplicar una medida por etapas")],
    worked=[
        ("Eficacia", "Una medida de ejemplo buscaba reducir un residuo de 100 a 60 toneladas y logró 70. ¿Cumplió totalmente?", ["La meta era 60.", "Logró 70: avanzó, pero no cumplió."], "No totalmente"),
        ("Costo de oportunidad", "Con 10 millones se puede arreglar una plaza o comprar libros. ¿Qué es el costo de oportunidad de elegir la plaza?", ["Es lo que se deja de hacer.", "En este caso, los libros."], "Dejar de comprar libros"),
    ],
    mistakes=[("Evaluar una política solo por su intención.", "Una buena intención puede tener efectos distintos.", "Revisa resultados y costos."),
              ("Olvidar a quienes pierden con la medida.", "Toda política tiene ganadores y perdedores.", "Pregunta quién asume los costos y cómo se compensa.")],
    T=[
        ('abc', '¿Qué es una política pública?', 'Una decisión del Estado para enfrentar un problema', 'Una ley aprobada por todos los partidos', 'Una opinión del gobierno sobre un tema', 'Es una decisión de acción frente a un problema, que se evalúa con criterios.'),
        ('=', '{F} ¿Cuántos millones más debería comprar localmente la empresa respecto de hoy para cumplir el 30 %?', '100*30//100-10', 'Se calcula el 30 % de los insumos y se resta lo que ya compra localmente.', ' millones'),
        ('=', '{F} Si los insumos subieran a 160 millones y se mantiene la exigencia del 30 %, ¿cuántos millones deberían ser locales?', '160*30//100', 'Se toma el 30 % del nuevo total.', ' millones'),
        ('abc', '{F} ¿Qué beneficio menciona la ficha?', 'Fortalece el empleo local y reduce el transporte', 'Reduce el costo de los insumos', 'Aumenta la competencia con proveedores extranjeros', 'La ficha dice que mejora el empleo local y baja el transporte.'),
        ('abc', '{F} ¿Qué riesgo menciona la ficha?', 'Puede subir los costos si los proveedores locales son más caros', 'Disminuye el empleo local, porque las empresas dejan de contratar', 'Aumenta el transporte de los insumos, porque los proveedores están más lejos', 'Es la objeción registrada en la ficha.'),
        ('abc', '{F} ¿Qué es la gradualidad?', 'Aplicar la medida por etapas para repartir el esfuerzo', 'Aplicarla de golpe para que el efecto sea inmediato', 'Aplicarla solo si todas las empresas están de acuerdo', 'Una propuesta gradual reduce el impacto de un cambio brusco.'),
        ('abc', '{F} ¿Qué propuesta gradual es posible?', 'Subir de 10 % a 20 % el primer año y a 30 % el segundo', 'Exigir el 30 % desde el primer día, sin plazo de adaptación', 'Mantener el 10 % indefinidamente, sin aumentar la exigencia', 'La primera reparte el esfuerzo en etapas hacia la meta.'),
        ('abc', '{F} ¿Qué criterio se afecta si los costos suben mucho?', 'Eficiencia, porque se usarían peor los recursos', 'Probidad, porque habría falta de honestidad', 'Equidad, porque cambiaría el trato entre grupos', 'La eficiencia mide si se usan bien los recursos.'),
        ('abc', '{F} ¿Qué criterio mide si se logra más empleo local?', 'Eficacia: si se logra el objetivo', 'Costo de oportunidad: lo que se deja de hacer', 'Sustentabilidad: si es viable sin dañar el futuro', 'Eficacia es el grado en que se logra el objetivo.'),
        ('abc', '{F} Alguien dice: «Esta política no tiene costos». ¿Qué corresponde?', 'Señalar que toda decisión tiene costos de oportunidad', 'Aceptarlo si la mayoría la apoya', 'Responder que sí tiene costos pero no se pueden medir', 'Elegir una opción implica renunciar a otra.'),
        ('abc', '{F} ¿Qué haría más probo el proceso de compra?', 'Publicar quiénes son los proveedores y cómo se eligen', 'Elegir a proveedores conocidos para evitar demoras', 'Mantener en reserva los nombres para evitar presiones', 'Si todos pueden ver cómo se elige, hay menos espacio para el favoritismo.'),
        ('=', '{F} Si los insumos locales por 40 millones suben un 5 % de precio, ¿cuántos millones más costarían?', '40*5//100', 'Se calcula el 5 % de 40.', ' millones'),
        ('abc', '{F} ¿Qué indicador mostraría si la medida resulta?', 'Porcentaje de insumos locales y costo total de la empresa', 'Cantidad de afiches impresos para difundir la medida en la comuna', 'Número de reuniones que realizó la comuna sobre el tema', 'Mide resultados y no solo actividades.'),
    ],
    ctx=('abc', 'Una comuna de ejemplo debe elegir entre construir una ciclovía o ampliar una calle. ¿Qué concepto describe lo que se deja de hacer al elegir?', 'Costo de oportunidad, por lo que se renuncia al elegir', 'Probidad, por la conducta honesta de los funcionarios', 'Eficacia, por el logro del objetivo propuesto', 'Es lo que se renuncia al elegir una opción.'),
    sc=[
        ('¿Qué es una política pública?', 'Una decisión del Estado para enfrentar un problema', 'Se evalúa con criterios como eficacia, eficiencia y equidad.'),
        ('abc', '¿Qué es la eficiencia?', 'Usar bien los recursos para lograr un objetivo', 'Lograr el objetivo sin importar el costo', 'Tratar a todos los grupos exactamente igual', 'Mide la relación entre recursos usados y resultados.'),
        ('¿Qué es la eficacia?', 'El grado en que se logra el objetivo', 'Mide el cumplimiento de lo propuesto.'),
    ],
    op=("Con la {F} escribe una propuesta de seis líneas: tu postura sobre la exigencia, un beneficio, un riesgo, una forma gradual de aplicarla, un indicador y una medida para asegurar probidad.",
        "Postura: aplicar la exigencia de forma gradual. Beneficio: empleo local. Riesgo: costos. Gradualidad: 20 % el primer año y 30 % el segundo. Indicador: porcentaje de insumos locales y costo total. Probidad: publicar la lista de proveedores.",
        ["incluye beneficio y riesgo", "propone gradualidad", "considera probidad"], ["propuesta de seis líneas"], ["ignorar costos", "ignorar a quienes pierden"],
        "Pregunta qué compensaría a quienes pierden."),
    reinforce="Explica con un ejemplo de tu casa qué es un costo de oportunidad.",
    extend="Anota una política pública de tu comuna y dos criterios para evaluarla.",
)

# ============================================================ OA 04, clase 5
F = ("Ficha 20 (diagnóstico de ejemplo en el liceo ficticio Altos del Valle): 60 estudiantes encuestados; 18 conocen qué es el comercio justo, 42 no. "
     "El quiosco escolar vende 5 productos; 2 provienen de productores locales. Propuesta: una feria de consumo responsable de 1 día con 10 puestos. "
     "Recursos: 14 estudiantes voluntarios, 2 docentes de apoyo y 3 semanas.")
build(
    O4, 5, F,
    use="Aprenderé a diseñar una acción escolar que promueva el consumo responsable y el comercio justo, con objetivos, roles, indicadores y respeto por todas las personas.",
    prior=["Sé qué es comercio justo y desarrollo sustentable.", "Sé diseñar una acción democrática.", "Sé calcular proporciones."],
    explain=[
        "El consumo responsable es elegir qué comprar considerando el impacto social y ambiental: quién produjo, en qué condiciones, cuánta energía y envases se usaron. El comercio justo busca precios y trabajo dignos para los productores. Una acción escolar puede informar y ofrecer alternativas, sin obligar a nadie.",
        "El diseño incluye un diagnóstico con datos, un objetivo medible (por ejemplo, que 40 de 60 estudiantes sepan explicar el comercio justo), roles, pasos con plazos, recursos y un indicador. También conviene un plan de probidad: quién maneja el dinero, cómo se eligen los puestos y cómo se informa de las cuentas.",
        "Se cuida la inclusión: precios accesibles y respeto a quienes no pueden comprar. Se evita prometer más de lo posible (una feria no cambia un mercado) y se evalúa con honestidad. Al final se comunica qué se logró y qué se podría mejorar.",
    ],
    vocab=[("consumo responsable", "elegir qué comprar considerando su impacto social y ambiental"), ("productor local", "persona o empresa que produce cerca del lugar donde se consume"), ("cuenta clara", "registro público de ingresos y gastos de una actividad"), ("inclusión", "medidas para que nadie quede fuera"), ("alcance", "cantidad de personas a las que llega una acción")],
    worked=[
        ("Medir un cambio", "En un curso de ejemplo, 10 de 30 sabían reciclar y luego lo saben 25. ¿Cuántos más lo saben?", ["Se resta 10 a 25.", "Es el aumento."], "15 estudiantes más"),
        ("Plan de probidad", "Una venta solidaria de ejemplo recauda dinero. ¿Qué medida muestra probidad?", ["Registrar ingresos y gastos.", "Publicar la cuenta."], "Publicar una cuenta clara"),
    ],
    mistakes=[("Prometer que una feria cambiará todo el mercado.", "Es una acción pequeña con alcance limitado.", "Plantea un objetivo posible y medible."),
              ("No explicar cómo se manejará el dinero.", "La falta de cuentas genera desconfianza.", "Define un responsable y publica la cuenta.")],
    T=[
        ('abc', '¿Qué es el consumo responsable?', 'Elegir qué comprar considerando el impacto social y ambiental', 'Comprar siempre lo más barato, sin importar quién lo produjo', 'Dejar de comprar cualquier producto para no dañar el ambiente', 'Implica fijarse en quién produjo, en qué condiciones y con qué impacto.'),
        ('=', '{F} ¿Qué porcentaje de los 60 estudiantes encuestados conoce el comercio justo?', '18*100//60', 'Se compara la cantidad que lo conoce con el total.', ' %'),
        ('=', '{F} ¿Qué porcentaje de los productos del quiosco proviene de productores locales?', '2*100//5', 'Se compara la parte con el total de productos.', ' %'),
        ('=', '{F} Si el objetivo es que 40 estudiantes sepan explicar el comercio justo, ¿cuántos más que hoy deben aprenderlo?', '40-18', 'Se resta los actuales a la meta.', ' estudiantes'),
        ('abc', '{F} ¿Cuál es un objetivo medible?', 'Que 40 de los 60 estudiantes expliquen el comercio justo al final de las 3 semanas', 'Que los estudiantes valoren más el comercio justo después de la feria', 'Que la feria tenga mucho público y todos los puestos vendan', 'Un número y un plazo permiten comprobarlo.'),
        ('abc', '{F} ¿Qué indicador sirve para medir el aprendizaje?', 'Número de estudiantes que responden bien una pregunta de control', 'Número de afiches pegados en el liceo durante las tres semanas', 'Número de puestos instalados el día de la feria', 'Los afiches y los puestos miden actividades; la pregunta de control mide el aprendizaje.'),
        ('abc', '{F} ¿Qué medida muestra probidad?', 'Una persona responsable del dinero y una cuenta publicada', 'Que el curso guarde el dinero sin registrar nada', 'Elegir los puestos entre amigos para ahorrar tiempo', 'Un registro de ingresos y gastos permite rendir cuentas con claridad.'),
        ('=', '{F} Si cada puesto necesita 2 voluntarios y hay 14 disponibles, ¿cuántos voluntarios faltan para cubrir los 10 puestos?', '10*2-14', 'Se calcula cuántos se necesitan y se resta los disponibles.', ' voluntarios'),
        ('abc', '{F} ¿Qué medida incluye a quienes no pueden comprar?', 'Ofrecer actividades gratuitas, como charlas y juegos informativos', 'Cobrar entrada para financiar la feria y cubrir los gastos del liceo', 'Vender solo productos de precio alto que den más ganancias', 'Las actividades gratuitas permiten participar a quienes no pueden gastar.'),
        ('abc', '{F} ¿Qué medida reduce el riesgo de que la feria no llegue a todos los cursos?', 'Invitar con carteles y con un voluntario por curso', 'Anunciarla solo el día anterior por altavoz', 'Invitar solo a los cursos que más participan', 'Varios canales y un contacto directo alcanzan a más estudiantes.'),
        ('abc', '{F} Si solo asisten 25 de los 60 estudiantes, ¿qué corresponde?', 'Revisar la difusión y ajustar la próxima acción', 'Culpar a los estudiantes que no fueron', 'Informar que la feria fue un éxito total', 'Se evalúa con honestidad para mejorar.'),
        ('abc', '{F} ¿Qué mensaje final es honesto?', 'Más estudiantes conocen el comercio justo, aunque el alcance fue limitado', 'Cambiamos el mercado de consumo del liceo y de toda la comuna', 'No logramos nada, así que no vale la pena repetir la actividad', 'Reconoce logros y límites sin exagerar.'),
        ('abc', '{F} El quiosco vende 5 productos y 2 son locales. ¿Qué propuesta es coherente con el consumo responsable?', 'Pedir al quiosco, de forma voluntaria, más productos locales con precios accesibles', 'Prohibir al quiosco vender cualquier producto que no sea local', 'Pedir a los estudiantes que no compren más en el quiosco', 'Propone una mejora sin obligar a nadie y cuidando el precio.'),
    ],
    ctx=('abc', 'Un curso de ejemplo quiere vender galletas para financiar un paseo. ¿Qué paso garantiza transparencia?', 'Anotar ingresos y gastos y mostrarlos al curso', 'Guardar el dinero sin avisar hasta el paseo', 'Informar solo el total recaudado', 'Una cuenta clara permite que todos revisen.'),
    sc=[
        ('¿Qué es un productor local?', 'Una persona o empresa que produce en el mismo territorio donde se vende', 'Comprarle acorta distancias y apoya el empleo cercano.'),
        ('abc', '¿Qué es el alcance de una acción?', 'La cantidad de personas a las que llega la acción', 'Su precio total, es decir, cuánto dinero cuesta', 'La cantidad de voluntarios que participan en ella', 'Mide a quiénes llegó la acción.'),
        ('¿Qué es una cuenta clara?', 'Un registro público de ingresos y gastos', 'Un registro de ingresos y gastos permite rendir cuentas con claridad.'),
    ],
    op=("Con la {F} diseña la feria: objetivo medible, roles para 14 voluntarios, tres pasos con semana, una medida de inclusión, un plan de probidad y un indicador. Escribe una frase para comunicar el resultado con honestidad.",
        "Objetivo: 40 de 60 expliquen el comercio justo. Roles: 4 en difusión, 6 en puestos, 4 en cuentas. Pasos: semana 1 invitar productores; semana 2 difundir; semana 3 feria y encuesta. Inclusión: degustaciones gratuitas. Probidad: cuenta publicada. Indicador: control final. Mensaje: más estudiantes conocen el comercio justo.",
        ["objetivo medible", "inclusión", "probidad"], ["diseño de la feria"], ["objetivo vago", "olvidar las cuentas"],
        "Pregunta cómo sabrá si cambió algún hábito de compra."),
    reinforce="Escribe tres criterios para elegir un producto de consumo responsable.",
    extend="Anota un producto que consumas y averigua con una persona adulta de dónde viene.",
)
