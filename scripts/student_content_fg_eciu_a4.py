"""Educación Ciudadana 3.º medio FG: OA 07 (territorio, justicia social y ambiental) y OA 08 (ejercicio democrático y convivencia escolar). Casos de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O7 = "FG-ECIU-3M-OAC-07"
O8 = "FG-ECIU-3M-OAC-08"

# ============================================================ OA 07, clase 1
F = ("Ficha 30 (región ficticia de Bahía Alta, con datos inventados): la capital regional concentra los servicios de salud y universidades; una comuna rural queda a 3 horas de un hospital. "
     "Una empresa minera genera empleo y paga impuestos, pero su relave (residuo) está cerca de un barrio de bajos ingresos. "
     "Una comunidad que se reconoce como pueblo originario cuida un humedal y propone protegerlo. Decisiones sobre el uso del suelo las toman el gobierno regional y los municipios.")
build(
    O7, 1, F,
    use="Aprenderé a distinguir las relaciones políticas, económicas y socioculturales que configuran un territorio en distintas escalas, y qué significan la justicia social y la justicia ambiental.",
    prior=["Sé qué es un municipio y una región.", "Sé que las actividades económicas usan el territorio.", "Sé qué es la desigualdad."],
    explain=[
        "El territorio no es solo un lugar: es un espacio construido por las relaciones entre personas, actividades e instituciones. Las relaciones políticas son las decisiones y límites que fijan los gobiernos (comunal, regional, nacional). Las económicas son las actividades que usan el suelo y los recursos, como la minería, la agricultura o el comercio. Las socioculturales son la identidad, las tradiciones y los vínculos de las comunidades con su entorno.",
        "Estas relaciones se miran en distintas escalas: local (un barrio), comunal, regional, nacional y global. Una decisión local puede depender de intereses globales, como el precio de un mineral. Estudiar varias escalas ayuda a entender por qué un lugar tiene más servicios que otro.",
        "La justicia social busca que los recursos y las oportunidades se repartan con equidad. La justicia ambiental busca que las cargas ambientales (contaminación, residuos) y los beneficios (áreas verdes, aire limpio) se repartan de forma justa y que las comunidades participen en las decisiones. Si siempre las mismas personas viven cerca de los riesgos, hay una injusticia. Respecto de pueblos originarios, la forma de entender el territorio la explican sus propias comunidades y educadores tradicionales.",
    ],
    vocab=[("territorio", "espacio construido por las relaciones entre personas, actividades e instituciones"), ("escala", "nivel de observación de un fenómeno, como local, regional o global"), ("justicia social", "reparto equitativo de recursos y oportunidades"), ("justicia ambiental", "reparto justo de cargas y beneficios ambientales con participación de las comunidades"), ("carga ambiental", "contaminación o riesgo ambiental que soporta una comunidad")],
    worked=[
        ("Clasificar una relación", "Una comuna de ejemplo fija con una ordenanza dónde se puede instalar una feria. ¿Qué relación del territorio es?", ["La define una autoridad.", "Es una decisión política."], "Relación política"),
        ("Identificar una carga ambiental", "Un barrio de ejemplo vive junto a una planta de residuos y otro tiene un parque. ¿Qué es la planta para el primer barrio?", ["Es un riesgo ambiental que soporta.", "Es una carga ambiental."], "Una carga ambiental"),
    ],
    mistakes=[("Pensar que la justicia ambiental solo trata de proteger la naturaleza.", "También incluye cómo se reparten cargas y beneficios entre personas.", "Pregunta quién soporta los riesgos y quién recibe los beneficios."),
              ("Mirar un problema territorial solo en una escala.", "Se pierde que las decisiones vienen de varios niveles.", "Analiza al menos dos escalas.")],
    T=[
        ('abc', '¿Qué estudian las relaciones políticas de un territorio?', 'Las decisiones y límites que fijan los gobiernos', 'Las actividades que usan el suelo y los recursos', 'La identidad y las tradiciones de las comunidades', 'Cada tipo de relación mira algo distinto: las políticas, las decisiones de las autoridades.'),
        ('abc', '{F} La actividad de la empresa minera, ¿qué tipo de relación es?', 'Económica', 'Sociocultural', 'Política', 'Usa el suelo y los recursos para producir, lo que corresponde a una relación económica.'),
        ('abc', '{F} El vínculo de la comunidad originaria con el humedal, ¿qué tipo de relación es?', 'Sociocultural, por el vínculo con el entorno', 'Económica, por el uso del suelo y los recursos', 'Política, por las decisiones de las autoridades', 'Expresa identidad y vínculos de una comunidad con su entorno.'),
        ('abc', '{F} Que el gobierno regional y los municipios decidan sobre el suelo, ¿qué relación es?', 'Política', 'Económica', 'Sociocultural', 'Son decisiones de autoridad sobre el territorio.'),
        ('abc', '{F} Para el barrio de bajos ingresos cercano al relave, ¿qué es el relave?', 'Una carga ambiental, porque es un residuo que soportan cerca de sus casas', 'Un recurso económico que el barrio recibe a cambio de convivir con la industria', 'Una decisión del gobierno regional sobre el uso del suelo', 'Una carga ambiental es contaminación o riesgo que soporta una comunidad.'),
        ('abc', '{F} El precio internacional del mineral influye en si la empresa amplía su producción. ¿Qué escala interviene?', 'La global, además de la regional y la local', 'Solo la de un barrio, porque el mineral se vende allí', 'Solo la comunal, porque la empresa paga impuestos en la comuna', 'Una decisión local puede depender de intereses globales, como el precio de un mineral.'),
        ('=', '{F} Si una familia debe ir una vez al mes al hospital y cada viaje toma 3 horas de ida y 3 de vuelta, ¿cuántas horas viaja en un año?', '3*2*12', 'Se calculan las horas por viaje y se multiplican por los viajes del año.', ' horas'),
        ('abc', '{F} ¿Qué desigualdad social muestra la distancia al hospital?', 'Desigual acceso a servicios según dónde se vive', 'Desigual pago de impuestos entre comunas', 'Desigual cantidad de empleo minero', 'Quien vive lejos de los servicios tiene peor acceso, lo que afecta la justicia social.'),
        ('abc', '{F} ¿Qué pide la justicia ambiental ante decisiones sobre el relave?', 'Que la comunidad afectada participe y que las cargas se repartan de forma justa', 'Que decida solo la empresa porque conoce el proyecto', 'Que todas las comunidades reciban la misma cantidad de industrias', 'La justicia ambiental incluye el reparto justo de cargas y la participación de las comunidades.'),
        ('abc', '{F} Alguien dice: «El empleo minero compensa cualquier riesgo». ¿Qué respuesta es más completa?', 'Habría que mirar quién recibe los beneficios y quién soporta las cargas', 'Es correcto, porque el empleo es más importante que el ambiente', 'Es falso, porque la minería nunca genera beneficios', 'La justicia ambiental pregunta por el reparto, no sólo por el total de beneficios.'),
        ('abc', '{F} ¿Por qué conviene mirar más de una escala?', 'Porque decisiones locales pueden depender de intereses regionales o globales', 'Porque la escala global es siempre la más importante y las demás no influyen', 'Porque los barrios no pueden decidir nada sobre su propio territorio', 'Los fenómenos se conectan entre escalas, y cada una explica algo distinto.'),
        ('abc', '{F} ¿Quién puede explicar cómo el pueblo originario entiende su territorio?', 'Sus propias comunidades y educadores tradicionales', 'Cualquier texto que hable de ellos, aunque no lo hayan escrito', 'Una autoridad regional que conozca el uso del suelo', 'Ellos conocen su cultura; la clase no reemplaza esa explicación.'),
        ('abc', '{F} Si los hospitales están todos en la capital regional, ¿qué justicia se afecta principalmente?', 'Justicia social', 'Justicia ambiental', 'Ambas por igual, sin diferencia', 'Se trata del reparto de servicios y oportunidades, que es el centro de la justicia social.'),
    ],
    ctx=('abc', 'En una ciudad de ejemplo, todos los camiones de basura pasan por el barrio más pobre y la basura se acumula allí. ¿Qué concepto se aplica?', 'Justicia ambiental, por el reparto desigual de cargas', 'Justicia social, por la falta de servicios de salud', 'Justicia económica, por el precio de la basura', 'Una carga ambiental se concentra en el barrio con menos recursos.'),
    sc=[
        ('¿Qué es la justicia social?', 'El reparto equitativo de recursos y oportunidades', 'Busca que las oportunidades lleguen de forma justa a todas las personas.'),
        ('abc', '¿Qué es una carga ambiental?', 'Contaminación o riesgo que soporta una comunidad', 'Un beneficio, como un parque que mejora la vida de un barrio', 'El costo de una obra pública que paga el municipio', 'Es un daño o riesgo ambiental que alguien soporta.'),
        ('En Educación Ciudadana: ¿qué es una escala?', 'Un nivel de observación de un fenómeno, como local o regional', 'Permite mirar un mismo hecho desde un barrio hasta lo global.'),
    ],
    op=("Con la {F} haz una tabla con tres filas (política, económica, sociocultural): un hecho de la ficha, la escala en que ocurre y una posible injusticia. Luego escribe una pregunta que haría la comunidad cercana al relave.",
        "Política: gobierno regional y municipios deciden el suelo; escala regional y comunal; injusticia posible: decisiones sin participación. Económica: minería; escala regional y global; injusticia: carga del relave. Sociocultural: cuidado del humedal; escala local; injusticia: que no se escuche a la comunidad. Pregunta: ¿qué medidas reducirán el riesgo del relave?",
        ["clasifica relaciones", "indica escala", "relaciona con justicia"], ["tabla de tres filas", "pregunta"], ["confundir económica con política", "culpar a un grupo"],
        "Pregunta qué escala le parece clave para decidir."),
    reinforce="Explica con tus palabras la diferencia entre justicia social y justicia ambiental.",
    extend="Anota un servicio que esté lejos de tu casa y cómo afecta a las personas.",
)

# ============================================================ OA 07, clase 2
F = ("Ficha 31 (caso de ejemplo): en la comuna ficticia de Los Álamos se propone instalar un relleno sanitario cerca de la población Nuevo Horizonte, de bajos ingresos. "
     "Datos de ejemplo: la comuna tiene 3 sectores (Centro, Lomas y Nuevo Horizonte); el estudio municipal analizó 3 terrenos y propone el más cercano a Nuevo Horizonte porque es más barato. "
     "El estudio dice que el relleno recibirá la basura de 100.000 habitantes de toda la comuna. Fuentes: el estudio municipal, una carta de la junta de vecinos y una nota del diario local.")
build(
    O7, 2, F,
    use="Aprenderé a investigar un caso territorial: quiénes participan, qué intereses hay y cómo se reparten beneficios y cargas entre sectores.",
    prior=["Sé qué es la justicia ambiental.", "Sé interrogar fuentes.", "Sé comparar cifras."],
    explain=[
        "Un conflicto territorial surge cuando personas o grupos tienen intereses distintos sobre un mismo espacio. Para investigarlo se identifican los actores (municipio, vecinos, empresas), sus intereses, el lugar y la escala, y las decisiones que se toman. También se analiza quién se beneficia y quién soporta los costos.",
        "En el caso de ejemplo, la basura es generada por toda la comuna, pero el relleno estaría cerca de un solo sector. Es un reparto desigual de cargas. Se revisan las fuentes: el estudio muestra criterios técnicos y de costo; la carta muestra la preocupación de los vecinos; la nota informa lo que observó un medio. Ninguna es neutral.",
        "Se pregunta si hubo participación informada de la comunidad, qué alternativas se estudiaron y qué medidas reducen el riesgo. Una conclusión prudente dice qué muestra la evidencia y qué falta, sin acusar de mala fe a nadie. Si hay riesgos para la salud, se consulta a especialistas.",
    ],
    vocab=[("actor", "persona o grupo con intereses en una decisión"), ("conflicto territorial", "desacuerdo sobre el uso de un espacio"), ("relleno sanitario", "lugar donde se deposita la basura de forma controlada"), ("participación informada", "intervención de la comunidad con información suficiente"), ("alternativa", "otra opción posible")],
    worked=[
        ("Reconocer actores", "En un caso de ejemplo una empresa quiere cerrar un camino, los vecinos lo usan y el municipio decide. ¿Quiénes son los actores?", ["La empresa, los vecinos y el municipio.", "Cada uno tiene intereses."], "Empresa, vecinos y municipio"),
        ("Reparto de cargas", "En un ejemplo, 5 sectores producen basura y 1 recibe el vertedero. ¿Es un reparto equitativo?", ["Las cargas se concentran en un solo sector.", "No es equitativo."], "No; concentra la carga"),
    ],
    mistakes=[("Culpar a los vecinos por oponerse sin conocer su razón.", "Su preocupación puede tener fundamento.", "Escucha sus argumentos y datos."),
              ("Aceptar el criterio de costo como único.", "Hay también criterios sociales y ambientales.", "Revisa todos los criterios del estudio.")],
    T=[
        ('abc', '¿Qué es un conflicto territorial?', 'Un desacuerdo entre grupos con intereses distintos sobre un mismo espacio', 'Cualquier discusión que ocurre en un barrio entre dos personas', 'Un reclamo ante un tribunal por una deuda impaga entre vecinos', 'Lo propio de un conflicto territorial es disputar el uso de un espacio.'),
        ('abc', '{F} ¿Quiénes son actores del caso?', 'El municipio, la junta de vecinos y las personas que generan la basura', 'Solo el municipio, que es el que toma la decisión final', 'Solo los vecinos de Nuevo Horizonte, que soportarían la carga', 'Cada grupo con intereses en la decisión es un actor.'),
        ('=', '{F} Si todos los habitantes generan la misma cantidad y Nuevo Horizonte tiene 8.000 de los 100.000, ¿qué porcentaje de la basura proviene de ese sector?', '8000*100//100000', 'Se compara la población del sector con la total.', ' %'),
        ('abc', '{F} ¿Qué dato muestra un reparto desigual de cargas?', 'Toda la comuna genera basura, pero la carga estaría concentrada en un sector', 'La comuna tiene 3 sectores y el estudio analizó 3 terrenos', 'El terreno elegido es el más barato de los tres analizados', 'La desigualdad aparece al comparar quién genera el residuo y quién lo soporta.'),
        ('abc', '{F} ¿Qué criterio usa principalmente el estudio municipal?', 'El costo: propone el terreno más barato', 'La justicia ambiental: reparte la carga entre sectores', 'La participación: consultó a las familias antes', 'La ficha dice que elige el terreno por ser más barato.'),
        ('abc', '{F} ¿Qué muestra la carta de la junta de vecinos?', 'La preocupación de los vecinos', 'Los criterios técnicos y de costo del terreno', 'Lo que observó un medio de comunicación', 'Es la postura de los vecinos afectados.'),
        ('abc', '{F} Alguien dice: «El estudio municipal es neutral porque es técnico». ¿Qué corresponde?', 'Revisar sus criterios, porque ninguna fuente es neutral: aquí prioriza el costo', 'Aceptarlo, porque los estudios técnicos no tienen intereses', 'Descartarlo, porque viene del municipio', 'Toda fuente tiene un autor y un propósito; hay que analizar qué criterios usa.'),
        ('abc', '{F} ¿Qué falta averiguar?', 'Qué alternativas y qué medidas para reducir el riesgo se estudiaron', 'Cuántos votos obtuvo el alcalde en la última elección', 'Qué opinan los vecinos de otras regiones', 'Sin conocer alternativas y medidas de reducción no se puede evaluar la decisión.'),
        ('abc', '{F} ¿Qué pregunta ayuda a evaluar la participación?', '¿Los vecinos recibieron información y fueron escuchados antes de decidir?', '¿Cuántos afiches se imprimieron para difundir el estudio municipal?', '¿Quién redactó el informe técnico y cuándo fue publicado?', 'La participación informada exige información y espacio de opinión previos.'),
        ('abc', '{F} Alguien dice: «Los vecinos se oponen por egoísmo». ¿Qué respuesta es más justa?', 'Revisar si sus argumentos tienen fundamento y escucharlos', 'Aceptarlo, porque se oponen a algo que beneficia a la comuna', 'Darles la razón sin revisar el estudio', 'No se descarta una preocupación sin analizarla ni se acepta sin evidencia.'),
        ('abc', '{F} ¿Qué especialistas deberían opinar sobre los riesgos para la salud?', 'Profesionales de salud y medio ambiente', 'Cualquier persona de la junta de vecinos', 'Solo el equipo que hizo el estudio de costos', 'Los riesgos de salud requieren conocimiento especializado.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'El estudio prioriza el costo y la carga quedaría en un sector; faltan alternativas', 'El municipio actúa de mala fe para perjudicar a los vecinos del sector', 'El relleno es seguro porque lo propone un estudio técnico del municipio', 'Se limita a lo que muestran las fuentes, sin acusar de mala fe.'),
        ('abc', '{F} ¿Qué medida reduciría el reparto desigual de la carga?', 'Evaluar otros terrenos con criterios ambientales y sociales, además del costo', 'Instalar el relleno donde el terreno cueste menos, como propone el estudio', 'Aumentar la cantidad de basura que recibe el relleno de la comuna', 'Se amplían los criterios y se escucha a la comunidad.'),
    ],
    ctx=('abc', 'Una comunidad de ejemplo se entera por la radio de que se instalará una antena junto a su escuela. ¿Qué falla se observa?', 'No hubo participación informada', 'Hubo demasiada información', 'Faltó un estudio de costo', 'La comunidad no fue consultada ni informada antes de decidir.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un actor?', 'Una persona o grupo con intereses en una decisión', 'Puede ser el municipio, una empresa o una comunidad.'),
        ('abc', '¿Qué es una alternativa?', 'Otra opción posible para resolver el mismo problema', 'Un castigo que se aplica al final del proceso de decisión', 'La opinión de la mayoría de los vecinos de la comuna', 'Evaluar alternativas permite comparar caminos distintos.'),
        ('¿Qué es la participación informada?', 'Que la comunidad reciba información clara y pueda opinar antes de que se decida', 'Informar después de decidir no cumple esa condición.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: actores y sus intereses, tres hechos, una contradicción o desigualdad, dos preguntas pendientes y una medida que reduzca el daño sin acusar a nadie.",
        "Actores: municipio, vecinos, quienes generan la basura. Hechos: 3 terrenos, el más barato es el cercano, el relleno recibe basura de 100.000 personas. Desigualdad: la carga recae en un sector. Preguntas: ¿hubo consulta?, ¿qué alternativas hay? Medida: monitoreo ambiental y compensación acordada.",
        ["identifica actores", "separa hechos", "propone una medida"], ["informe de cinco puntos"], ["acusar sin pruebas", "usar solo el costo"],
        "Pregunta qué cambiaría si el terreno fuera otro."),
    reinforce="Explica cómo saber si el reparto de cargas en un caso es justo.",
    extend="Anota un lugar de tu comuna que reciba muchas cargas (ruido, residuos) y quién vive cerca.",
)

# ============================================================ OA 07, clase 3
F = ("Ficha 32 (perspectivas de ejemplo sobre ampliar una planta industrial en la comuna ficticia de Puerto Claro). "
     "Perspectiva 1 (empresa): «La ampliación generará 200 empleos y pagará más impuestos». "
     "Perspectiva 2 (junta de vecinos): «El humo ya afecta a la escuela; queremos medidas antes de ampliar». "
     "Perspectiva 3 (municipio): «Aceptamos si hay compromisos ambientales verificables y si parte de los empleos son para la comuna». "
     "Dato de ejemplo: la comuna tiene 2.000 personas en edad de trabajar y 400 están sin empleo.")
build(
    O7, 3, F,
    use="Aprenderé a contrastar perspectivas sobre el uso del territorio, valorando empleo, ambiente y participación, y a proponer alternativas más justas.",
    prior=["Sé qué son las justicias social y ambiental.", "Sé comparar perspectivas.", "Sé calcular porcentajes simples."],
    explain=[
        "Las decisiones sobre el territorio suelen enfrentar valores legítimos: empleo y desarrollo económico, salud y ambiente, identidad de la comunidad. Contrastar significa identificar qué valor defiende cada actor, qué evidencia presenta y qué costos aceptaría. No se trata de elegir un bando, sino de buscar soluciones que respeten derechos.",
        "La evidencia puede ser un dato económico (empleos, impuestos), ambiental (mediciones de contaminación) o social (opiniones, salud). Un dato aislado no basta: 200 empleos importan más si se sabe cuántos son para la comuna y cuánto cuestan en términos de salud. Se exige verificabilidad: medir, informar y revisar.",
        "Una solución justa suele combinar condiciones: medidas ambientales con metas y plazos, empleo local, participación de la comunidad en el seguimiento y compensaciones acordadas. Se evita el dilema falso de «empleo o ambiente», porque se pueden buscar caminos que mejoren ambos aspectos.",
    ],
    vocab=[("desarrollo económico", "crecimiento de la actividad productiva y del empleo"), ("compromiso verificable", "promesa que puede comprobarse con datos"), ("compensación", "medida que repara o equilibra un daño causado"), ("monitoreo", "medición continua de una situación"), ("dilema falso", "presentar solo dos opciones cuando hay más")],
    worked=[
        ("Calcular desempleo", "En una comuna de ejemplo hay 500 personas en edad de trabajar y 100 sin empleo. ¿Qué parte está sin empleo?", ["100 de 500 es una quinta parte.", "Es el 20 %."], "Una quinta parte, el 20 %"),
        ("Compromiso verificable", "¿Cuál compromiso es verificable: «cuidaremos el aire» o «mediremos el aire cada mes y publicaremos el informe»?", ["El segundo se puede comprobar.", "El primero es vago."], "El segundo"),
    ],
    mistakes=[("Plantear que solo hay dos opciones: empleo o ambiente.", "Existen soluciones intermedias.", "Busca medidas que combinen ambas."),
              ("Aceptar una promesa sin forma de verificarla.", "No se sabe si se cumplirá.", "Pide metas, plazos e informes públicos.")],
    T=[
        ('abc', '¿Qué es un dilema falso?', 'Presentar solo dos opciones cuando existen más', 'Elegir la opción que más personas apoyan', 'Negar que un problema exista', 'Simplifica el problema y oculta caminos intermedios.'),
        ('=', '{F} ¿Qué porcentaje de las 2.000 personas en edad de trabajar está sin empleo?', '400*100//2000', 'Se compara la parte sin empleo con el total.', ' %'),
        ('=', '{F} Si la mitad de los 200 empleos fueran para la comuna, ¿qué porcentaje de las 400 personas sin empleo conseguiría trabajo?', '(200//2)*100//400', 'Se calcula la mitad de los empleos y se compara con las personas sin empleo.', ' %'),
        ('abc', '{F} ¿Qué valor defiende la empresa?', 'El empleo y el desarrollo económico de la comuna', 'La salud y el ambiente de los niños de la escuela', 'La identidad local y las tradiciones de la comunidad', 'Su argumento es que la ampliación genera empleos y más impuestos.'),
        ('abc', '{F} ¿Qué valor defiende la junta de vecinos?', 'La salud y el ambiente', 'Los impuestos municipales', 'El desarrollo industrial', 'Menciona el humo que afecta a la escuela.'),
        ('abc', '{F} ¿Qué condición propone el municipio?', 'Compromisos ambientales verificables y empleo local', 'Rechazar toda ampliación sin condiciones', 'Aceptar la ampliación sin pedir nada a cambio', 'Es la postura que registra la ficha.'),
        ('abc', '{F} ¿Qué es un compromiso verificable?', 'Una promesa con metas medibles que pueden comprobarse con datos', 'Una promesa firmada por el gerente', 'Una promesa que la empresa cumplirá lo antes posible', 'Se puede medir y revisar, lo que permite comprobar si se cumple.'),
        ('abc', '{F} ¿Qué solución combina las tres posturas?', 'Ampliar con metas ambientales, empleo local y monitoreo con vecinos', 'Ampliar sin condiciones para generar empleo cuanto antes', 'Impedir la ampliación y no discutir otras alternativas con la empresa', 'Combina empleo local, metas ambientales y participación de la comunidad en el seguimiento.'),
        ('abc', '{F} Alguien dice: «O hay empleo o hay ambiente sano». ¿Qué error comete?', 'Un dilema falso, porque existen caminos intermedios', 'Una conclusión basada en datos de la comuna', 'Una compensación acordada', 'Presenta solo dos salidas cuando pueden combinarse medidas.'),
        ('abc', '{F} ¿Qué dato falta para evaluar el problema del humo?', 'Mediciones de contaminación y de salud en la escuela', 'La cantidad de empleos que ofrece otra empresa', 'Los años de experiencia del gerente', 'Se necesita evidencia ambiental y de salud.'),
        ('abc', '{F} ¿Qué compensación podría acordarse?', 'Mejorar la ventilación de la escuela y financiar controles de salud', 'Entregar dinero al municipio sin un destino definido ni controles', 'Prometer empleos futuros sin plazo ni cantidad comprometida', 'Repara de forma concreta el daño a la comunidad afectada.'),
        ('abc', 'Una empresa de ejemplo promete reducir el ruido «lo antes posible». ¿Qué mejora la promesa?', 'Fijar una meta medible y una fecha', 'Repetirla en un afiche', 'Pedir a los vecinos que confíen', 'Una meta con fecha permite verificar su cumplimiento.'),
        ('abc', '{F} Además de los 200 empleos, ¿qué hay que saber para evaluar el beneficio?', 'Cuántos serían para la comuna y qué costo tendría en salud', 'Cuántos empleos tiene la empresa en otras regiones', 'Qué color tendría la nueva planta', 'Un dato aislado no basta; importa a quiénes beneficia y qué costos trae.'),
    ],
    ctx=('abc', 'Una comunidad acuerda con una empresa que un comité vecinal revise cada mes las mediciones. ¿Qué se aplica?', 'Monitoreo con participación de la comunidad', 'Una compensación económica única, entregada una sola vez', 'Un dilema falso, que presenta solo dos opciones', 'Medir de forma continua con participación permite verificar los compromisos.'),
    sc=[
        ('¿Qué es la compensación?', 'Una medida que repara o equilibra un daño', 'Busca equilibrar lo que la comunidad pierde con la actividad.'),
        ('abc', '¿Qué es el monitoreo?', 'Medición continua de una situación', 'Una opinión sobre un problema', 'Una promesa de mejora', 'Permite saber cómo evoluciona un fenómeno.'),
        ('¿Qué es el desarrollo económico?', 'El crecimiento de las actividades que generan ingresos y empleo', 'Es uno de los valores que compiten en las decisiones territoriales.'),
    ],
    op=("Con la {F} haz una tabla con las tres perspectivas: valor, evidencia y condición que aceptaría. Escribe una solución de cuatro líneas que combine empleo, ambiente y participación.",
        "Empresa: empleo; 200 empleos; acepta ampliar. Vecinos: salud; humo en la escuela; exigen medidas antes. Municipio: desarrollo con condiciones; pide verificación. Solución: ampliar tras medidas ambientales con metas, 100 empleos locales, monitoreo público y mejoras en la escuela.",
        ["identifica valores", "pide verificabilidad", "combina objetivos"], ["tabla", "solución de cuatro líneas"], ["aceptar el dilema falso", "no verificar"],
        "Pregunta quién haría el monitoreo."),
    reinforce="Explica por qué es útil que un compromiso tenga meta y plazo.",
    extend="Anota un conflicto de tu región entre desarrollo y ambiente y los valores en juego.",
)

# ============================================================ OA 07, clase 4
F = ("Ficha 33 (tema de deliberación de ejemplo): la comuna ficticia de Villa Esperanza propone usar un terreno vacío para un parque inundable (que absorbe lluvias) o para 40 viviendas sociales. "
     "A favor del parque: reduce inundaciones y da áreas verdes a un barrio sin plazas. A favor de las viviendas: hay 60 familias esperando casa. "
     "Dato de ejemplo: el terreno cabe 40 viviendas o el parque, no ambos; hay otro terreno, más lejano, que permitiría 40 viviendas con transporte público cada 30 minutos.")
build(
    O7, 4, F,
    use="Aprenderé a deliberar sobre decisiones de uso del territorio, ponderando derechos en tensión (vivienda y ambiente) y buscando alternativas que mejoren la justicia social y ambiental.",
    prior=["Sé contrastar perspectivas territoriales.", "Sé qué es la justicia ambiental.", "Sé estructurar un argumento."],
    explain=[
        "A veces dos necesidades legítimas compiten por un mismo espacio. El derecho a una vivienda adecuada y el derecho a un ambiente sano no se oponen en principio, pero un terreno limitado obliga a decidir. Deliberar es examinar criterios: cuántas personas se benefician, cuán urgente es cada necesidad, qué riesgos hay y qué alternativas existen.",
        "Los costos también se reparten. Mandar las viviendas a un terreno lejano puede aislar a las familias del transporte, el trabajo y los servicios. Dejar el parque inundable puede proteger al barrio de las lluvias. Se pregunta quién gana y quién pierde en cada opción, y cómo se compensa.",
        "Una propuesta sólida combina medidas: por ejemplo, un parque más pequeño con diseño inundable más viviendas en otro terreno bien conectado, con participación de las familias en las decisiones. Se explican los límites (no se resuelve todo), se define un plazo y se acuerda cómo se revisará el resultado.",
    ],
    vocab=[("vivienda adecuada", "casa con seguridad, servicios y buena ubicación"), ("parque inundable", "espacio verde diseñado para absorber agua de lluvia"), ("conectividad", "facilidad de acceder a transporte y servicios"), ("criterio de decisión", "aspecto que se usa para elegir entre opciones"), ("urgencia", "necesidad que no puede esperar")],
    worked=[
        ("Aplicar criterios", "Dos terrenos de ejemplo: uno cerca de servicios con 20 viviendas y uno lejano con 40 viviendas. ¿Qué criterio favorece al segundo?", ["Permite más viviendas.", "Pero tiene peor conectividad."], "Cantidad de viviendas"),
        ("Compensar", "Si un parque se reduce a la mitad, ¿qué compensa a los vecinos?", ["Un diseño que absorba el agua igual.", "Y más árboles en otras calles."], "Diseño inundable y árboles"),
    ],
    mistakes=[("Elegir solo por la cantidad de beneficiados.", "La urgencia y la ubicación también importan.", "Usa varios criterios."),
              ("Olvidar a las familias en la decisión.", "Son quienes viven con el resultado.", "Incluye su participación.")],
    T=[
        ('abc', '¿Qué derechos compiten por el terreno vacío del caso?', 'La vivienda adecuada y un ambiente sano', 'La propiedad privada y la libertad de culto', 'La educación y la libertad de reunión', 'El parque se relaciona con el ambiente sano y las viviendas con el derecho a una vivienda adecuada.'),
        ('=', '{F} Si cada familia tiene 4 integrantes, ¿cuántas personas seguirían esperando vivienda si se construyen las 40?', '(60-40)*4', 'Se calculan las familias sin vivienda y se multiplican por sus integrantes.', ' personas'),
        ('abc', '{F} ¿Qué ventaja tiene el parque inundable?', 'Reduce inundaciones y da áreas verdes a un barrio sin plazas', 'Entrega viviendas a las 60 familias que esperan una casa', 'Mejora el transporte público de todo el barrio', 'Está en los argumentos a favor del parque.'),
        ('abc', '{F} ¿Qué ventaja tienen las viviendas?', 'Responden a la necesidad de las 60 familias que esperan casa', 'Absorben el agua de lluvia y reducen las inundaciones del barrio', 'Reducen la distancia al transporte público para todos los vecinos', 'Es el argumento a favor de la construcción de viviendas.'),
        ('abc', '{F} ¿Qué problema puede tener el terreno más lejano?', 'Puede aislar a las familias del trabajo y los servicios aunque haya transporte', 'No cabe ninguna vivienda en ese terreno, según el estudio', 'Es más barato que el terreno del barrio y por eso no conviene', 'La distancia afecta la conectividad de las familias.'),
        ('abc', '{F} ¿Qué es la conectividad?', 'La facilidad de acceder a transporte y servicios', 'La cantidad de viviendas por terreno', 'El costo de construir en un terreno', 'Es un criterio de decisión: qué tan bien conectado queda un lugar.'),
        ('abc', '{F} ¿Qué propuesta combina ambos derechos?', 'Parque inundable en el terreno vacío y las 40 viviendas en el otro terreno, con transporte', 'Solo viviendas, sin consultar al barrio ni considerar las inundaciones', 'Solo parque, sin responder a la necesidad de las 60 familias', 'Atiende la inundación y la vivienda a la vez, reduciendo el aislamiento.'),
        ('abc', '{F} ¿Qué medida compensaría el aislamiento del terreno lejano?', 'Aumentar la frecuencia del transporte hacia el terreno nuevo', 'Reducir los servicios del terreno nuevo para abaratar la obra', 'Construir sin transporte hacia el terreno nuevo, para ahorrar costos', 'Mejora el acceso al trabajo y a los servicios.'),
        ('abc', '{F} Un asistente dice: «Hay 60 familias, así que construyamos y olvidemos el parque». ¿Qué respuesta es más completa?', 'Considerar también el riesgo de inundaciones y las alternativas', 'Aceptarlo, porque la necesidad de vivienda es más urgente', 'Rechazarlo, porque el ambiente siempre va primero', 'Ambas necesidades son legítimas; se comparan riesgos y alternativas.'),
        ('abc', '{F} ¿Qué participación mejora la decisión?', 'Que las familias y el barrio opinen antes de decidir', 'Que decida el equipo técnico y se informe después', 'Que opine solo quien vive junto al terreno', 'Es una participación informada de quienes se ven afectados.'),
        ('abc', '{F} ¿Qué indicador mostraría si la propuesta resultó?', 'Familias con vivienda y episodios de inundación en el barrio', 'Cantidad de reuniones realizadas con la comunidad durante el proceso', 'Número de planos presentados al municipio para su aprobación', 'Mide el resultado en ambos objetivos.'),
        ('abc', '{F} ¿Qué límite debe reconocer la propuesta?', 'Que solo resuelve la espera de 40 de las 60 familias', 'Que el parque no tendría ningún beneficio', 'Que el transporte sería más lento de lo previsto', 'Una propuesta honesta dice qué no alcanza a resolver.'),
        ('abc', 'Un liceo debe decidir entre usar un patio como estacionamiento o como huerto. ¿Qué criterio conviene mirar?', 'Cuántas personas se benefician y qué riesgos hay', 'Qué opción prefiere la autoridad, aunque no consulte a nadie', 'Qué opción cuesta menos de explicar a los vecinos del liceo', 'Son criterios de decisión que sirven para comparar opciones.'),
    ],
    ctx=('abc', 'Un barrio debe elegir entre ampliar una cancha o una sala de estudio en el mismo terreno. ¿Qué pregunta ayuda a decidir?', '¿Cuántas personas se benefician y cuán urgente es cada necesidad?', '¿Qué opción propuso primero el club y cuántos socios tiene?', '¿Qué opción se ve más desde la calle y llama más la atención?', 'La urgencia y el número de beneficiarios son criterios de decisión.'),
    sc=[
        ('¿Qué es la conectividad?', 'La facilidad de acceder a transporte y servicios', 'Un lugar bien conectado reduce el aislamiento.'),
        ('abc', '¿Qué es un criterio de decisión?', 'Un aspecto que se usa para comparar y elegir entre opciones', 'Una decisión ya tomada que se comunica a la comunidad', 'Una opinión sin argumentos que defiende una persona', 'Orienta la elección de forma ordenada.'),
        ('¿Qué es un parque inundable?', 'Un espacio verde diseñado para absorber agua de lluvia', 'Sirve para reducir los efectos de las lluvias en un barrio.'),
    ],
    op=("Con la {F} escribe una propuesta de seis líneas: opción elegida, dos criterios, un beneficio, un costo, cómo participaría la comunidad y un indicador.",
        "Elijo un parque más pequeño inundable más viviendas en el otro terreno. Criterios: urgencia y riesgo de inundación. Beneficio: reduce inundaciones y avanza en vivienda. Costo: transporte cada 30 minutos. Participación: asambleas con familias. Indicador: familias con vivienda y episodios de inundación.",
        ["usa criterios", "reconoce costos", "incluye participación"], ["propuesta de seis líneas"], ["decidir sin considerar costos", "olvidar a las familias"],
        "Pregunta qué cambiaría si no hubiera otro terreno."),
    reinforce="Explica por qué el derecho a la vivienda y el derecho a un ambiente sano pueden coexistir.",
    extend="Anota un espacio de tu barrio con necesidades distintas y qué usos podría tener.",
)

# ============================================================ OA 08, clase 1
F = ("Ficha 34 (instancias de un liceo ficticio de ejemplo): el curso 3.º A elige directiva con voto secreto; el centro de estudiantes organiza una asamblea al mes; "
     "el consejo escolar reúne a representantes de estudiantes, docentes, apoderados y dirección; el reglamento de convivencia fija normas y consecuencias; "
     "un grupo de mediación escolar ayuda a resolver conflictos entre estudiantes con un acuerdo.")
build(
    O8, 1, F,
    use="Aprenderé qué instancias escolares permiten ejercitar la democracia, por qué hay normas para organizar la vida en comunidad y cómo ayudan a una sana convivencia.",
    prior=["Sé qué es la democracia.", "Sé qué es una norma.", "Sé qué es una votación."],
    explain=[
        "Un liceo es una comunidad y, como toda comunidad, necesita organización. Las instancias escolares democráticas permiten participar y decidir juntos: el consejo de curso, el centro de estudiantes, las asambleas, el consejo escolar y la mediación. Cada una tiene roles y límites. Participar en ellas es una forma de aprender a ejercer derechos y asumir responsabilidades.",
        "Las normas, reunidas en el reglamento de convivencia, ordenan la vida en común. Una norma justa se conoce, se aplica a todos por igual, protege las libertades y el bien común, y tiene consecuencias proporcionadas. Las votaciones deben ser libres, secretas, informadas e igualitarias: una persona, un voto.",
        "La sana convivencia no es ausencia de conflictos, sino capacidad de enfrentarlos con respeto: escuchar, argumentar, acordar y reparar. Ante situaciones de violencia o acoso, lo prudente es avisar a una persona adulta de confianza del liceo, y no resolver solo ni guardar el secreto.",
    ],
    vocab=[("consejo escolar", "instancia que reúne a estudiantes, docentes, apoderados y dirección para conversar sobre la vida del liceo"), ("centro de estudiantes", "organización que representa a los estudiantes del liceo"), ("reglamento de convivencia", "conjunto de normas que ordena la vida en común"), ("voto secreto", "voto que nadie más conoce, para votar libremente"), ("mediación", "proceso en que un tercero ayuda a las partes a llegar a un acuerdo")],
    worked=[
        ("Elegir la instancia", "Los estudiantes de un liceo de ejemplo quieren proponer actividades para todo el liceo. ¿A qué instancia acuden?", ["Quieren representar a los estudiantes.", "Es el centro de estudiantes."], "Centro de estudiantes"),
        ("Norma proporcionada", "Un reglamento de ejemplo castiga con expulsión inmediata llegar tarde una vez. ¿Es proporcionada?", ["La falta es menor.", "La consecuencia es excesiva."], "No; es excesiva"),
    ],
    mistakes=[("Creer que una norma sirve solo para castigar.", "También protege derechos y organiza la convivencia.", "Pregunta qué derecho o bien protege."),
              ("Resolver solo un caso de violencia por no «ser acusete».", "Se pone en riesgo a las personas.", "Avisa a una persona adulta de confianza.")],
    T=[
        ('abc', '¿Qué es el reglamento de convivencia?', 'Un conjunto de normas que ordena la vida en común y fija consecuencias', 'Un listado de actividades extraprogramáticas que ofrece el liceo', 'Un acta de la última asamblea del centro de estudiantes', 'Reúne las normas y consecuencias de la comunidad escolar.'),
        ('abc', '{F} ¿Qué instancia reúne a estudiantes, docentes, apoderados y dirección?', 'El consejo escolar', 'El centro de estudiantes', 'El consejo de curso', 'Así lo indica la ficha; las otras instancias reúnen solo a estudiantes.'),
        ('abc', '{F} ¿Qué hace el grupo de mediación escolar?', 'Ayuda a resolver conflictos con un acuerdo entre las partes', 'Decide la sanción que corresponde a quien causó el conflicto', 'Investiga quién tuvo la culpa y la informa a la dirección', 'La mediación facilita acuerdos; no impone sanciones.'),
        ('abc', '¿Por qué el voto es secreto?', 'Para que cada persona vote libremente, sin presiones', 'Para que el resultado se conozca más rápido', 'Para que no se puedan contar los votos', 'El secreto protege la libertad de elegir.'),
        ('abc', '{F} ¿Qué principio expresa «una persona, un voto»?', 'Igualdad: todos los votos pesan lo mismo', 'Secreto: nadie sabe cómo se vota', 'Transparencia: todos ven el voto de todos', 'Cada persona cuenta lo mismo en la decisión.'),
        ('abc', '{F} ¿Qué instancia usarías para conversar un tema que involucra a las familias?', 'El consejo escolar, porque reúne a apoderados', 'El consejo de curso, porque lo integran los estudiantes', 'La mediación escolar, porque resuelve conflictos', 'Solo el consejo escolar incluye a los apoderados.'),
        ('abc', '{F} ¿Qué rasgos tiene una norma justa?', 'Se conoce, se aplica a todos por igual y tiene consecuencias proporcionadas', 'Se decide caso a caso según quién cometió la falta', 'Es muy estricta para evitar que se repita en el futuro', 'La justicia de una norma exige conocimiento, igualdad y proporcionalidad.'),
        ('abc', '{F} Un estudiante dice: «Mejor no avisar de que me hostigan para no ser acusete». ¿Qué corresponde?', 'Avisar a una persona adulta de confianza del liceo', 'Resolverlo a solas con quien hostiga', 'Guardar el secreto para evitar problemas', 'Pedir ayuda es parte de la protección; los adultos pueden intervenir.'),
        ('abc', '{F} ¿Qué diferencia hay entre conflicto y violencia?', 'El conflicto puede resolverse con diálogo; la violencia daña y requiere ayuda adulta', 'No hay diferencia: todo conflicto es violencia y requiere sanción', 'El conflicto es siempre grave y la violencia nunca lo es', 'No todo conflicto es violencia, y la violencia exige protección.'),
        ('abc', '{F} ¿Qué haría más democrática una asamblea?', 'Que todas las personas puedan hablar y votar con las mismas reglas', 'Que hable solo la directiva y el resto vote', 'Que quienes llegaron antes tengan más tiempo de palabra', 'Una asamblea democrática da igualdad de participación.'),
        ('abc', '{F} ¿Qué consecuencia es proporcionada para un atraso reiterado?', 'Una conversación y un compromiso de mejora, con seguimiento', 'La expulsión inmediata del estudiante, para dar un ejemplo', 'Ninguna consecuencia, para evitar conflictos con la familia', 'La respuesta debe ser acorde a la gravedad de la falta.'),
        ('=', '{F} Si el curso 3.º A tiene 36 estudiantes y votaron 27, ¿qué porcentaje participó?', '27*100//36', 'Se compara la parte que votó con el total del curso.', ' %'),
        ('abc', '{F} En el recreo, dos compañeros discuten por un balón. ¿Qué vía es más adecuada?', 'Mediación con un acuerdo entre ambos', 'Que decida quien tenga el balón', 'Sancionar a ambos sin escucharlos', 'Resuelve con respeto y busca un acuerdo.'),
    ],
    ctx=('abc', 'Un curso de ejemplo quiere elegir su lema. ¿Qué elección respeta mejor los principios del voto?', 'Voto secreto, libre y una persona un voto', 'Voto a mano alzada con el profesor jefe presente', 'Voto en que el delegado vota por todos', 'Cumple las condiciones de un voto libre, secreto e igualitario.'),
    sc=[
        ('abc', '¿Qué es el centro de estudiantes?', 'Una organización que representa a los estudiantes ante el liceo', 'Un curso del liceo que reúne a estudiantes de un mismo nivel', 'Un comité de docentes que decide sobre las actividades', 'Representa a los estudiantes y organiza asambleas.'),
        ('¿Qué es el consejo escolar?', 'Una instancia que reúne a representantes de estudiantes, docentes, apoderados y dirección', 'Permite que distintos integrantes de la comunidad participen.'),
        ('¿Qué significa que una votación sea informada?', 'Que las personas conocen las opciones antes de votar', 'Votar sin conocer las opciones no es una decisión libre.'),
    ],
    op=("Con la {F} escribe una tabla con las cinco instancias: quién participa y para qué sirve. Luego propone una mejora para que más estudiantes participen y una forma de avisar a una persona adulta de confianza ante un caso de acoso.",
        "Consejo de curso: el curso, decide asuntos del curso. Centro de estudiantes: estudiantes, representa. Consejo escolar: toda la comunidad, conversa. Reglamento: normas. Mediación: estudiantes en conflicto. Mejora: asambleas con agenda abierta. Aviso: contar a la orientadora o a un profesor de confianza.",
        ["describe las instancias", "propone mejora", "incluye el aviso a un adulto"], ["tabla de cinco instancias", "mejora"], ["confundir instancias", "no incluir al adulto"],
        "Pregunta quién podría quedar fuera."),
    reinforce="Explica por qué las normas ayudan a vivir juntos.",
    extend="Averigua qué instancias de participación tiene tu liceo.",
)

# ============================================================ OA 08, clase 2
F = ("Ficha 35 (caso de ejemplo): en el liceo ficticio San Rafael, la elección del centro de estudiantes tuvo 240 votantes habilitados. "
     "Resultados: lista Azul 70 votos, lista Verde 85 votos, lista Roja 40, votos nulos 15, blancos 10. "
     "Fuentes: el acta del comité electoral, el reglamento de elecciones (voto secreto, una persona un voto) y una carta de un estudiante que dice que se vio a alguien votar dos veces.")
build(
    O8, 2, F,
    use="Aprenderé a investigar un proceso democrático escolar: leer resultados, comprobar el procedimiento y manejar con respeto una denuncia de irregularidad.",
    prior=["Sé qué es el voto secreto.", "Sé leer una tabla de resultados.", "Sé sumar y calcular porcentajes simples."],
    explain=[
        "Un proceso electoral escolar tiene reglas: padrón de votantes, voto secreto, una persona un voto y recuento público. El acta es el documento donde se anota el resultado. Los votos pueden ser válidos (a una lista), nulos (mal marcados) o blancos (sin marcar). La participación es la parte del padrón que votó.",
        "Para comprobar un resultado se suman todos los votos y se compara con el total de votantes. Si una denuncia dice que alguien votó dos veces, se pide evidencia: lista de firmas, acta y testigos. Se evita acusar a personas sin pruebas y se respeta la privacidad. El comité electoral es el responsable de revisar y responder.",
        "El resultado final se informa a la comunidad con transparencia. Si una irregularidad pudiera cambiar el resultado (una diferencia menor al número de votos dudosos), se corrige o se repite parte de la votación. Quien pierde acepta el resultado si el proceso fue limpio y quien gana gobierna para todos.",
    ],
    vocab=[("padrón", "lista de personas habilitadas para votar"), ("voto nulo", "voto mal marcado que no cuenta para ninguna lista"), ("voto blanco", "voto sin marcar ninguna opción"), ("participación electoral", "parte del padrón que efectivamente vota"), ("comité electoral", "grupo responsable de organizar y revisar una elección")],
    worked=[
        ("Sumar votos", "En una elección de ejemplo, A tuvo 50, B 30, nulos 5 y blancos 5. ¿Cuántos votos se emitieron?", ["Se suman todas las categorías.", "50 más 30 más 5 más 5."], "90 votos"),
        ("Participación", "Si en un padrón de ejemplo de 100 personas votaron 80, ¿cuál es la participación?", ["80 de 100.", "Es el 80 %."], "80 %"),
    ],
    mistakes=[("Contar solo los votos de las listas y olvidar nulos y blancos.", "El total de votos incluye todos.", "Suma todas las categorías."),
              ("Dar por cierta una denuncia sin pruebas.", "Puede ser un error o una acusación falsa.", "Pide evidencia y respeta la privacidad.")],
    T=[
        ('abc', '¿Qué es un voto nulo?', 'Un voto mal marcado, que no cuenta para ninguna lista', 'Un voto sin marcar ninguna opción', 'Un voto emitido por una persona no habilitada', 'Es un voto que no se puede asignar a una lista por estar mal marcado.'),
        ('abc', '¿Qué es un voto blanco?', 'Un voto sin marcar ninguna opción', 'Un voto mal marcado', 'Un voto de una persona ausente', 'Se emite sin elegir ninguna lista.'),
        ('=', '{F} ¿Cuántos votos válidos hubo, es decir, a las listas?', '70+85+40', 'Se suman solo los votos de las tres listas.', ' votos'),
        ('=', '{F} ¿Cuántos votos se emitieron en total, contando listas, nulos y blancos?', '70+85+40+15+10', 'Se suman todos los votos emitidos.', ' votos'),
        ('=', '{F} ¿Cuántos votantes habilitados no votaron?', '240-(70+85+40+15+10)', 'Se resta los votos emitidos al padrón.', ' votantes'),
        ('abc', '{F} ¿Cuál describe la participación de esta elección?', '220 de 240 habilitados votaron', '195 de 240 habilitados votaron', '85 de 240 habilitados votaron', 'Participación es la parte del padrón que votó, incluyendo nulos y blancos.'),
        ('abc', '{F} ¿Qué documento registra los resultados?', 'El acta del comité electoral', 'La carta del estudiante', 'El padrón de votantes', 'El acta es el registro oficial del resultado.'),
        ('abc', '{F} Si se comprobara que una persona votó dos veces, ¿podría cambiar el ganador?', 'No, porque Verde supera a Azul por 15 votos y la irregularidad sería de un voto', 'Sí, porque cualquier irregularidad anula la elección completa', 'Sí, porque con un voto menos Verde tendría menos votos que Azul', 'Restar un voto a Verde la deja con 84, aún sobre los 70 de Azul.'),
        ('abc', '{F} ¿Qué debe hacer el comité con la carta?', 'Pedir evidencia, como las firmas del padrón, y responder con respeto', 'Anular la elección sin revisar la denuncia ni pedir pruebas', 'Ignorarla porque la carta no proviene del comité electoral', 'Se investiga antes de decidir y se responde al estudiante.'),
        ('abc', '{F} Un estudiante dice: «Verde ganó porque hicieron trampa». ¿Qué corresponde?', 'Pedir pruebas antes de afirmarlo', 'Aceptarlo porque hubo una carta', 'Pedir que Verde renuncie', 'Sin evidencia es solo una sospecha que puede dañar a personas.'),
        ('abc', '{F} Para revisar la denuncia sin exponer a nadie, ¿qué conviene?', 'Revisar las firmas del padrón sin publicar los nombres de quienes votaron', 'Publicar en el diario mural quién firmó y quién no lo hizo', 'Preguntar en voz alta a cada curso por quién votó', 'El voto es secreto y se respeta la privacidad al revisar.'),
        ('abc', '{F} ¿Qué actitud demuestra respeto democrático?', 'Aceptar el resultado si el proceso fue limpio y colaborar con la lista ganadora', 'Pedir repetir la elección hasta ganar, aunque el proceso fue limpio', 'Aislar a la lista que ganó para que no pueda gobernar', 'Quien pierde acepta un proceso limpio y quien gana gobierna para todos.'),
        ('abc', '{F} ¿Cuándo se corrige o se repite parte de la votación?', 'Cuando una irregularidad pudiera cambiar el resultado', 'Siempre que haya votos nulos o blancos', 'Cuando la lista ganadora gana por pocos votos sin irregularidades', 'La corrección procede si la irregularidad afecta el resultado.'),
    ],
    ctx=('=', 'En una elección de curso de ejemplo hay 30 habilitados y votan 24. ¿Qué porcentaje participó?', '24*100//30', 'Se compara la parte que votó con el padrón.', ' %'),
    sc=[
        ('¿Qué es el padrón?', 'La lista de personas habilitadas para votar', 'Permite saber quiénes pueden votar y calcular la participación.'),
        ('abc', '¿Qué es un comité electoral?', 'Un grupo que organiza y revisa una elección', 'Una lista de candidatos que participa de la votación', 'Un grupo de votantes que decide por todos los demás', 'Es responsable de que el proceso sea limpio y transparente.'),
        ('En Educación Ciudadana: ¿Qué es la participación electoral?', 'La parte del padrón que efectivamente vota', 'Se mide como votos emitidos sobre habilitados.'),
    ],
    op=("Con la {F} escribe un informe de seis líneas: total de votos emitidos, participación en porcentaje aproximado (sobre 240), ganador, dos pruebas que pedirías por la denuncia y un mensaje de cierre respetuoso a las tres listas.",
        "Votos emitidos: 220. Participación aproximada: 91 %. Ganó Verde con 85 votos. Pruebas: lista de firmas del padrón y testimonios. Mensaje: gracias a todas las listas por participar; el comité informará la revisión y respetaremos el resultado.",
        ["calcula bien", "pide pruebas", "mensaje respetuoso"], ["informe de seis líneas"], ["omitir nulos y blancos", "acusar sin pruebas"],
        "Pregunta cómo se podría mejorar el proceso."),
    reinforce="Explica qué es el voto nulo y el blanco con tus palabras.",
    extend="Averigua cómo se elige el centro de estudiantes en tu liceo.",
)

# ============================================================ OA 08, clase 3
F = ("Ficha 36 (perspectivas de ejemplo sobre una norma para el uso de celulares en clases, liceo ficticio Los Robles). "
     "Perspectiva 1 (estudiante): «El celular sirve para buscar información y organizarme; prohibirlo sería injusto». "
     "Perspectiva 2 (docente): «Distrae y baja la concentración; propongo guardarlo salvo actividades indicadas». "
     "Perspectiva 3 (apoderada): «Quiero poder contactar a mi hijo en una emergencia». "
     "Encuesta de ejemplo: de 100 estudiantes, 70 dicen distraerse con el celular y 60 dicen usarlo para estudiar (algunos hacen ambas cosas).")
build(
    O8, 3, F,
    use="Aprenderé a contrastar perspectivas sobre una norma escolar y a evaluar si protege libertades y bien común de forma proporcionada.",
    prior=["Sé qué es una norma justa.", "Sé comparar perspectivas.", "Sé leer un dato de encuesta."],
    explain=[
        "Una norma escolar puede limitar una libertad (usar el celular) para proteger un bien común (concentración y aprendizaje). Para evaluarla se pregunta si tiene un fin legítimo, si es necesaria, si es proporcionada y si se aplica por igual. Una norma muy dura o muy vaga puede ser injusta.",
        "Cada perspectiva destaca algo: el estudiante, su autonomía y recursos; el docente, la concentración; la apoderada, la seguridad. Una buena solución recoge lo valioso de cada una. La encuesta ayuda a ver qué piensan los estudiantes, pero no sustituye la deliberación: que muchos digan algo no prueba que sea lo mejor.",
        "Además se piensa en cómo se revisará la norma: plazo de prueba, indicadores (por ejemplo, rendimiento y convivencia) y espacio para ajustar. Participar en la creación de las normas favorece que se cumplan, porque las personas las sienten propias.",
    ],
    vocab=[("fin legítimo", "objetivo válido que justifica una norma"), ("proporcionalidad", "equilibrio entre la limitación impuesta y el fin que se busca"), ("autonomía", "capacidad de decidir por uno mismo"), ("período de prueba", "tiempo en que se aplica una norma para evaluarla"), ("sentir propia una norma", "cumplirla porque se participó en crearla")],
    worked=[
        ("Evaluar proporcionalidad", "Un liceo de ejemplo prohíbe llevar mochilas. ¿Es proporcionado el fin de evitar robos?", ["La medida limita mucho.", "Hay formas menos restrictivas, como casilleros."], "No; hay opciones menos restrictivas"),
        ("Buscar un fin legítimo", "Una norma de ejemplo exige silencio en la biblioteca. ¿Cuál es su fin?", ["Permitir concentración.", "Es un fin legítimo."], "Permitir concentración"),
    ],
    mistakes=[("Decidir solo con lo que dice la mayoría.", "Se omite la proporcionalidad y los derechos de las minorías.", "Usa el resultado como un dato, no como la decisión."),
              ("Proponer una norma sin forma de revisarla.", "No se sabe si funciona.", "Define período de prueba e indicadores.")],
    T=[
        ('abc', '¿Qué es la proporcionalidad de una norma?', 'El equilibrio entre la limitación y el fin que se busca', 'Que la norma se aplique solo a una parte de la comunidad', 'Que la sanción sea la mayor posible para evitar la falta', 'Una norma proporcionada limita lo necesario y no más.'),
        ('abc', '¿Qué es un fin legítimo?', 'Un objetivo válido que justifica limitar una libertad, como la concentración', 'Cualquier deseo de quien dirige el liceo, aunque no tenga base', 'Un objetivo que prefieren los adultos del liceo', 'Un fin legítimo es una razón válida de bien común, no una preferencia.'),
        ('abc', '{F} ¿Qué valor defiende el estudiante?', 'Autonomía y acceso a información', 'Silencio y orden en la sala de clases', 'Seguridad en el trayecto al liceo', 'Habla de organizarse y buscar información por sí mismo.'),
        ('abc', '{F} ¿Qué bien común destaca la docente?', 'La concentración y el aprendizaje', 'La autonomía de cada estudiante', 'La comunicación con las familias', 'Su propuesta busca mejorar la concentración.'),
        ('=', '{F} Si 70 estudiantes dicen distraerse, 60 usarlo para estudiar y 40 hacen ambas cosas, ¿cuántos solo se distraen?', '70-40', 'Se resta a los que se distraen quienes también lo usan para estudiar.', ' estudiantes'),
        ('=', '{F} Con esos mismos datos, ¿cuántos estudiantes lo usan para distraerse, para estudiar o para ambas cosas?', '70+60-40', 'Se suman ambos grupos y se resta la parte que se cuenta dos veces.', ' estudiantes'),
        ('abc', '{F} ¿Qué norma es más proporcionada?', 'Guardar el celular salvo en actividades indicadas y permitir llamadas de emergencia', 'Prohibir el celular siempre, sin excepciones, ni siquiera ante emergencias', 'Dejar el uso libre sin ninguna regla ni límite en la sala', 'Equilibra el fin de la norma con las necesidades de los estudiantes.'),
        ('abc', '{F} Un participante dice: «70 estudiantes dicen distraerse, así que prohibamos todo». ¿Qué corresponde?', 'Considerar también el uso para estudiar y otras alternativas', 'Aceptarlo, porque 70 es más que la mitad', 'Ignorar la encuesta, porque las encuestas no sirven', 'La encuesta orienta pero no sustituye la deliberación.'),
        ('abc', '{F} ¿Qué medida atiende la preocupación de la apoderada?', 'Un canal para llamadas de emergencia durante la jornada', 'Pedirle que no llame durante la jornada, salvo que sea grave', 'Permitir el celular libre en clases para todos los estudiantes', 'Responde a su inquietud sin dejar de proteger la concentración.'),
        ('abc', '{F} ¿Qué haría que los estudiantes sientan propia la norma?', 'Participar en su creación y entender sus razones', 'Recibirla sin explicación, para que no haya cuestionamientos', 'Que la norma sea más estricta, para que se respete', 'Participar favorece que las personas la cumplan porque la sienten propia.'),
        ('abc', '{F} ¿Qué indicador mostraría si la norma funciona?', 'Cambios en la concentración percibida y en los conflictos por el celular', 'Cantidad de afiches sobre la norma pegados en el liceo', 'Número de celulares guardados al inicio del año escolar', 'Mide resultados de la norma y no solo actividades.'),
        ('abc', '{F} ¿Qué sanción es proporcionada si alguien usa el celular en clases?', 'Pedir que lo guarde y registrar una conversación con el estudiante', 'Expulsarlo del liceo por usar el celular en una clase', 'Quitarle el celular por todo el año escolar', 'La consecuencia debe ser acorde a la falta.'),
        ('abc', '{F} ¿Por qué una norma muy vaga puede ser injusta?', 'Porque no se sabe qué está permitido y puede aplicarse distinto a cada persona', 'Porque obliga a todos a obedecer sin importar lo que diga', 'Porque exige demasiadas explicaciones a quienes la aplican', 'La claridad es condición de una norma justa.'),
    ],
    ctx=('abc', 'Un curso de ejemplo propone que la limpieza de la sala la haga siempre la misma persona. ¿Qué principio se vulnera?', 'Igualdad en la aplicación de las normas', 'Proporcionalidad de la sanción a la falta', 'Voto secreto en las elecciones del curso', 'Una norma debe aplicarse a todos por igual.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es la autonomía?', 'La capacidad de una persona de decidir por sí misma', 'Es un valor que el estudiante defiende frente a la prohibición.'),
        ('abc', '¿Qué es un período de prueba?', 'Un tiempo en que se aplica una norma para evaluarla y ajustarla', 'Un castigo temporal para quien incumple la norma', 'Una votación para elegir la norma entre varias opciones', 'Permite corregir la norma antes de dejarla definitiva.'),
        ('¿Qué significa sentir propia una norma?', 'Entenderla y haber participado en su creación, por lo que se cumple con mayor facilidad', 'Las normas que se comprenden se cumplen mejor.'),
    ],
    op=("Con la {F} redacta una norma de cuatro líneas que recoja las tres perspectivas: qué se permite, qué se limita, excepciones, consecuencia proporcionada y cómo se revisará en un mes.",
        "Los celulares se guardan durante las clases salvo en actividades indicadas por el docente. Se permite recibir llamadas de emergencia por el canal de dirección. Si alguien lo usa sin autorización, se le pide guardarlo y se conversa. En un mes se revisa con una encuesta y una asamblea.",
        ["equilibra perspectivas", "es proporcionada", "incluye revisión"], ["norma de cuatro líneas"], ["norma sin excepciones", "sanción excesiva"],
        "Pregunta qué evidencia mostraría si la norma resulta."),
    reinforce="Explica qué hace proporcionada a una norma.",
    extend="Averigua qué normas tiene tu liceo sobre celulares y qué fin legítimo persiguen.",
)

# ============================================================ OA 08, clase 4
F = ("Ficha 37 (tema de deliberación de ejemplo): el liceo ficticio Altamira debe decidir cómo actuar cuando se conoce un caso de hostigamiento entre estudiantes. "
     "Propuesta A: mediación entre las partes. Propuesta B: sanción directa por la dirección. Propuesta C: primero hablar con una persona adulta de confianza, evaluar la gravedad y luego decidir entre mediación, medidas de protección o sanción. "
     "Datos de ejemplo: 10 casos del año pasado, 6 resueltos con mediación, 3 con medidas de protección y sanción, 1 con apoyo externo.")
build(
    O8, 4, F,
    use="Aprenderé a deliberar sobre la convivencia escolar con razones, cuidando la dignidad de todas las personas y definiendo cuándo corresponde ayuda adulta.",
    prior=["Sé qué es la mediación.", "Sé ponderar derechos.", "Sé estructurar un argumento."],
    explain=[
        "La convivencia escolar sana se construye con normas claras, diálogo y protección de las personas. No todo conflicto es igual: algunos se resuelven conversando; otros, como el hostigamiento sostenido, requieren medidas de protección y ayuda de personas adultas. Evaluar la gravedad es el primer paso.",
        "La mediación sirve cuando las partes están en condiciones de dialogar de forma segura y quieren un acuerdo. No es adecuada si hay una relación de abuso o miedo, porque la persona afectada podría sentirse presionada. En esos casos se prioriza protegerla, y se actúa con la ayuda de una persona adulta de confianza del liceo.",
        "Una buena deliberación combina vías: primero protección y evaluación; luego mediación si corresponde; sanciones proporcionadas si hay falta grave; y medidas para reparar y prevenir. Se escucha a todas las personas, se evita exponer públicamente a nadie y se registra lo decidido. Los datos de casos pasados orientan, pero no reemplazan el análisis de cada situación.",
    ],
    vocab=[("hostigamiento", "conducta repetida que daña o intimida a una persona"), ("medida de protección", "acción para resguardar a la persona afectada"), ("reparación", "acciones para compensar el daño y restablecer la relación"), ("gravedad", "nivel de daño o riesgo de una situación"), ("registro", "anotación de lo ocurrido y de lo decidido")],
    worked=[
        ("Elegir la vía", "En un caso de ejemplo dos amigos discuten por un trabajo y ambos quieren conversar. ¿Qué vía conviene?", ["No hay riesgo.", "Hay disposición al diálogo: mediación."], "Mediación"),
        ("Priorizar la protección", "En un caso de ejemplo, un estudiante teme a otro que lo ha amenazado varias veces. ¿Qué es lo primero?", ["Cuidar su seguridad.", "Avisar a una persona adulta de confianza."], "Protección y aviso a un adulto"),
    ],
    mistakes=[("Obligar a la mediación en casos de miedo o abuso.", "Puede presionar a quien fue afectado.", "Prioriza la protección."),
              ("Exponer públicamente a las personas involucradas.", "Daña su dignidad.", "Mantén la reserva y el respeto.")],
    T=[
        ('abc', '¿Qué es el hostigamiento?', 'Una conducta repetida que daña o intimida a una persona', 'Una discusión ocasional entre dos compañeros', 'Una broma que todos entienden como juego', 'La repetición y el daño lo distinguen de un conflicto ocasional.'),
        ('abc', '{F} ¿Cuándo no conviene la mediación?', 'Cuando hay abuso o miedo que impide dialogar de forma segura', 'Cuando las partes quieren dialogar en igualdad', 'Cuando el conflicto es muy reciente', 'Podría presionar a la persona afectada.'),
        ('abc', '{F} ¿Qué es una medida de protección?', 'Una acción para resguardar a la persona afectada', 'Una sanción para quien hostiga', 'Una conversación de reconciliación obligatoria', 'Su fin es proteger a quien está en riesgo.'),
        ('abc', '{F} ¿Qué propone primero la propuesta C?', 'Hablar con una persona adulta de confianza y evaluar la gravedad', 'Sancionar directamente a quien hostiga y comunicarlo al curso', 'Reunir a las partes en una mediación inmediata sin evaluar nada', 'Así lo indica la ficha: primero evaluar, luego decidir.'),
        ('=', '{F} ¿Qué porcentaje de los 10 casos no se resolvió solo con mediación?', '(10-6)*100//10', 'Se calcula los casos restantes y se compara con el total.', ' %'),
        ('abc', '{F} ¿Qué dato muestra que no basta una sola vía?', 'Que 4 de los 10 casos requirieron medidas distintas de la mediación', 'Que hubo 10 casos en total durante el año pasado', 'Que 6 de 10 casos se resolvieron con mediación y los demás no', 'Los casos no se resolvieron igual, por lo que conviene combinar vías.'),
        ('abc', '{F} ¿Qué propuesta es más sólida?', 'C, porque evalúa la gravedad y combina vías según el caso', 'A, porque la mediación sirvió en la mayoría de los casos', 'B, porque una sanción directa evita que se repita', 'Se ajusta a cada situación y protege a la persona afectada.'),
        ('abc', '{F} ¿Qué haces si sabes de un caso de hostigamiento?', 'Avisar a una persona adulta de confianza del liceo', 'Resolverlo solo con el grupo de amigos', 'Esperar a que la víctima lo pida', 'Los adultos pueden proteger y actuar con medidas adecuadas.'),
        ('abc', '{F} Un asistente dice: «6 de 10 se resolvieron con mediación, así que siempre hay que mediar». ¿Qué error comete?', 'Generaliza a partir de casos pasados; cada situación debe analizarse', 'Usa evidencia suficiente para afirmar una regla general', 'Confunde la mediación con la sanción directa de la dirección', 'Los datos orientan, pero no reemplazan el análisis de cada caso.'),
        ('abc', '{F} ¿Qué respuesta sería proporcionada ante un hostigamiento leve y reciente?', 'Una advertencia, una reparación y seguimiento', 'La expulsión inmediata', 'Ninguna medida, para no exponer a nadie', 'Debe ser acorde a la gravedad de la falta.'),
        ('abc', '{F} ¿Qué evita daño adicional a las personas involucradas?', 'Reserva y respeto en el manejo del caso', 'Publicar los nombres para que todos sepan', 'Comentar el caso con los cursos para prevenir', 'Protege su dignidad y evita exposición pública.'),
        ('abc', '{F} ¿Qué indicador muestra si la convivencia mejora?', 'Menos casos repetidos y mayor sensación de seguridad en encuestas', 'Más afiches sobre convivencia en el diario mural del liceo', 'Menos reuniones del centro de estudiantes durante el año', 'Mide los efectos en la convivencia.'),
        ('abc', '{F} ¿Por qué evaluar la gravedad es el primer paso?', 'Porque determina si basta el diálogo o se necesitan medidas de protección', 'Porque así se decide el castigo antes de escuchar a las partes', 'Porque todos los casos exigen mediación entre las personas', 'La respuesta depende de qué tan grave y sostenido sea el caso.'),
    ],
    ctx=('abc', 'Un curso de ejemplo se entera de que un compañero recibe mensajes amenazantes. ¿Qué es lo más adecuado?', 'Avisar a una persona adulta de confianza y apoyar al compañero', 'Responder con amenazas a quien las envió para que deje de hacerlo', 'Guardar los mensajes sin mostrarlos a nadie para no complicar a nadie', 'Se protege sin escalar el daño.'),
    sc=[
        ('¿Qué es la gravedad de un caso?', 'Qué tan serio, repetido o riesgoso es lo ocurrido', 'De ella depende si basta el diálogo o se necesitan medidas de protección.'),
        ('abc', '¿Qué es la reparación?', 'Una medida que corrige el daño causado', 'Una sanción que busca castigar', 'Un registro de lo ocurrido', 'Busca restablecer lo dañado, por ejemplo con disculpas y acuerdos.'),
        ('En Educación Ciudadana: ¿Para qué sirve el registro?', 'Para anotar lo ocurrido y lo decidido y darle seguimiento', 'Permite verificar que lo acordado se cumpla.'),
    ],
    op=("Con la {F} escribe un procedimiento de cinco pasos para tu liceo: cómo se recibe un caso, quién evalúa la gravedad, cuándo se usa mediación, qué medidas de protección hay y cómo se registra. Marca el paso en que se avisa a una persona adulta de confianza.",
        "1. Se recibe y se avisa a una persona adulta de confianza. 2. Se evalúa la gravedad. 3. Mediación si hay seguridad y voluntad. 4. Medidas de protección o sanción proporcionada. 5. Registro, reparación y seguimiento. Aviso: paso 1.",
        ["incluye gravedad y protección", "incluye aviso a un adulto", "respeta la dignidad"], ["procedimiento de cinco pasos"], ["obligar a mediar", "exponer a las personas"],
        "Pregunta cómo evitaría las represalias."),
    reinforce="Explica por qué una sola vía no sirve para todos los casos.",
    extend="Averigua con una persona adulta a quién puedes avisar en tu liceo si ves una situación de hostigamiento.",
)
