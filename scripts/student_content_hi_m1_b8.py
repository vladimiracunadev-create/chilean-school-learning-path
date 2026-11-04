"""Cuaderno del estudiante, 1.º medio Historia, Geografía y Ciencias Sociales: OA 17 (riqueza salitrera, Estado e inversión pública)."""
from __future__ import annotations

from hi5_lib import build

OA = "HI1M OA 17"
MAT = "Lápiz y papel. Las fuentes, las tablas y los datos (de ejemplo) están escritos en cada ejercicio; no necesitas libros ni internet."

# ---------------------------------------------------------------- Clase 1
F1 = "Línea de tiempo: 1879-1884, guerra del Pacífico, tras la cual Chile controla las provincias salitreras de Tarapacá y Antofagasta; 1883, se crea la Sociedad de Fomento Fabril, que reúne a industriales; 1886-1891, gobierno de Balmaceda, con fuerte impulso a obras públicas, ferrocarriles y liceos; 1889, se funda el Instituto Pedagógico para formar profesores de enseñanza media; desde las primeras décadas del siglo XX, el salitre natural pierde mercado frente al salitre sintético fabricado en Europa."
build(
    OA, 1, F1,
    use="Aprenderé a ubicar en el tiempo y el espacio el ciclo del salitre y a explicar cómo aumentó los ingresos del Estado y permitió invertir en obras y educación. Sirve para entender el origen de la modernización de fines del siglo XIX y sus límites.",
    prior=["Conozco la guerra del Pacífico y la importancia del salitre.", "Sé qué son impuestos y presupuesto.", "Sé leer una línea de tiempo."],
    explain=[
        "Después de la guerra del Pacífico, Chile controló las provincias salitreras del norte. El salitre se exportaba a los mercados del mundo, donde se usaba como fertilizante y para fabricar explosivos. El Estado chileno no explotaba directamente las oficinas salitreras, que eran de empresas, muchas de capital británico y chileno, pero cobraba un impuesto a la exportación. Ese impuesto pasó a ser una parte muy importante de los ingresos fiscales, es decir, del dinero que recibía el Estado.",
        "Con esos ingresos el Estado pudo aumentar la inversión pública, que es el dinero que el Estado gasta en obras e instituciones para el país. Se construyeron ferrocarriles, puentes, puertos y edificios públicos, y se financió la educación: más escuelas, liceos y el Instituto Pedagógico (1889). También crecieron otros sectores productivos, como la industria y el comercio, que vendían bienes y servicios a las zonas salitreras.",
        "Pero hay que ser precisos. El ingreso salitrero no se distribuyó de modo uniforme: el Estado, los empresarios y los trabajadores recibieron beneficios muy distintos. Y no explica por sí solo toda la modernización: también influyeron otros factores, como la agricultura, otras minas y el crédito. Además, el negocio dependía de un solo producto, y cuando apareció el salitre sintético, la riqueza disminuyó.",
    ],
    vocab=[("ingreso fiscal", "dinero que recibe el Estado, por ejemplo por impuestos"), ("inversión pública", "dinero que el Estado gasta en obras e instituciones para el país"), ("sector productivo", "rama de la economía como la industria, la agricultura o el comercio"), ("infraestructura", "obras como caminos, puertos y ferrocarriles que permiten la actividad económica"), ("salitre sintético", "salitre fabricado en fábricas, sin extraerlo del desierto")],
    worked=[
        ("Ubicar en el tiempo", "Con la línea de tiempo, ¿cuántos años duró el gobierno de Balmaceda que impulsó obras públicas?",
         ["Busco las fechas: 1886 y 1891.", "Resto: 1891 - 1886."], "5 años"),
        ("Relacionar impuesto e inversión", "Explica en una frase cómo el salitre llegó a financiar escuelas y ferrocarriles.",
         ["Las empresas exportaban salitre.", "El Estado cobraba un impuesto a esa exportación.", "Ese dinero se usó en obras públicas y educación."], "Por el impuesto a la exportación que financiaba obras y educación"),
    ],
    mistakes=[
        ("Creer que el Estado explotaba directamente las oficinas salitreras.", "Eran de empresas; el Estado cobraba impuestos.", "Distingue propiedad de las oficinas e impuesto a la exportación."),
        ("Pensar que la riqueza del salitre benefició a todos por igual.", "Estado, empresarios y trabajadores recibieron beneficios distintos.", "Pregunta quién ganó cuánto."),
    ],
    T=[
        ("En Historia: ¿qué es la inversión pública?", "El dinero que el Estado gasta en obras e instituciones para el país", "Fue posible por el impuesto salitrero."),
        ("{F} ¿En qué año se funda el Instituto Pedagógico?", "1889", "La línea de tiempo lo indica."),
        ("{F} ¿Qué se creó en 1883 según la línea?", "La Sociedad de Fomento Fabril", "La línea lo señala."),
        ("En Historia: ¿qué es un ingreso fiscal?", "El dinero que recibe el Estado, por ejemplo por impuestos", "El impuesto salitrero lo aumentó."),
        ("{F} ¿Qué provincias salitreras pasó a controlar Chile? A) Tarapacá y Antofagasta, B) Atacama y Coquimbo, C) Biobío y Arauco.", "A", "La línea lo señala."),
        ("Une cada obra con su tipo: 1) ferrocarril, 2) liceo, 3) puerto. a) obra para educar, b) obra que lleva carga y pasajeros por tierra sobre rieles, c) obra donde los barcos cargan y descargan. Escribe las parejas.", "1-b, 2-a, 3-c", "Cada obra corresponde a un uso de la inversión."),
        ("{F} Ordena de más antiguo a más reciente: fundación del Instituto Pedagógico, inicio del gobierno de Balmaceda, creación de la Sociedad de Fomento Fabril y término de la guerra del Pacífico.", "Sociedad de Fomento Fabril, término de la guerra, gobierno de Balmaceda, Instituto Pedagógico", "Se ordenan por sus años: 1883, 1884, 1886 y 1889."),
        ("{F} ¿Qué obras impulsó el gobierno de Balmaceda según la línea de tiempo?", "Obras públicas, ferrocarriles y liceos", "La línea las nombra junto a su gobierno."),
        ("Una compañera dice: «El Estado chileno era dueño de todas las oficinas salitreras». ¿Qué corrección haces?", "Las oficinas eran de empresas; el Estado cobraba un impuesto a la exportación", "La explicación distingue propiedad e impuesto."),
        ("{F} ¿Qué hecho de la línea muestra una causa del fin del ciclo del salitre?", "La aparición del salitre sintético fabricado en Europa", "Redujo el mercado del salitre natural."),
        ("Explica por qué depender de un solo producto era un riesgo para la economía.", "Porque si el producto perdía mercado, como el salitre frente al sintético, los ingresos del Estado y del país caían", "La dependencia hace vulnerable la economía."),
        ("Evalúa la frase «el salitre explica por sí solo toda la modernización de Chile». A) es excesiva porque también influyeron la agricultura, otras minas y el crédito, B) es correcta, C) es correcta porque había impuestos.", "A", "Una sola causa no explica todo."),
        ("Una persona dice: «Los ingresos del salitre llegaron por igual a todas las familias». Da una razón para dudar usando la clase.", "Porque el Estado, los empresarios y los trabajadores recibieron beneficios distintos", "La distribución fue desigual."),
    ],
    ctx=("Un afiche escolar dice: «El salitre hizo ricos a todos los chilenos». Escribe una frase que lo corrija con lo aprendido.", "El salitre aumentó los ingresos del Estado y permitió invertir en obras y educación, pero los beneficios no se repartieron igual", "La frase debe incluir desigualdad en la distribución."),
    sc=[("En Historia: ¿qué es la infraestructura?", "Obras como caminos, puertos y ferrocarriles que permiten la actividad económica", "Fue un destino de la inversión."),
        ("Nombra dos usos de la inversión pública salitrera.", "Por ejemplo: ferrocarriles y liceos", "Están en la línea y la explicación."),
        ("¿Qué provocó la disminución del ciclo del salitre?", "La aparición del salitre sintético", "Competía con el natural.")],
    op=("{F} Con la línea de tiempo de arriba, escribe cinco líneas que expliquen cómo el salitre transformó las finanzas del Estado. Nombra un impuesto, dos obras, una fecha y un límite de la riqueza salitrera.",
        "El Estado cobraba un impuesto a la exportación de salitre y eso aumentó sus ingresos. Con ese dinero se construyeron ferrocarriles y liceos durante el gobierno de Balmaceda (1886-1891). El Instituto Pedagógico se fundó en 1889. Límite: la riqueza dependía de un solo producto y no se repartió igual.",
        ["un impuesto", "dos obras", "una fecha", "un límite"], ["texto de cinco líneas"], ["decir que el Estado era dueño de las oficinas", "omitir el límite"], "Léele tu texto a alguien de tu casa y pídele que anote las obras que nombraste."),
    reinforce="Escribe las cinco fechas de la línea de tiempo y, junto a cada una, una palabra que la resuma.",
    extend="Escribe una frase que explique por qué es riesgoso que un país dependa de un solo producto de exportación.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 2
F2 = "Fuente A (tabla de ejemplo): ingresos fiscales de un año de ejemplo, 100 millones de pesos, de los cuales 45 millones provienen de impuestos al salitre y 55 millones de otras fuentes. Fuente B (informe de una autoridad, texto de ejemplo): «Con las rentas del salitre se construirán caminos, puentes y escuelas en todo el país.» Fuente C (testimonio de un obrero salitrero, de ejemplo): «Trabajamos al sol; nos pagan con fichas que solo valen en la pulpería de la oficina.» Fuente D (informe de un visitante extranjero, de ejemplo): «El comercio del puerto ha crecido y llegan muchos barcos.» Fuente E (historiadora actual, texto de ejemplo): «El auge salitrero fortaleció al Estado, pero mantuvo desigualdades.»"
build(
    OA, 2, F2,
    use="Aprenderé a leer una tabla fiscal, un informe oficial, un testimonio obrero y un relato de visitante sobre el ciclo del salitre, detectando intención y límites. Sirve para entender que la riqueza se vivió de modos distintos.",
    prior=["Conozco la relación entre salitre, impuestos e inversión.", "Distingo fuentes primarias y secundarias.", "Sé calcular porcentajes sencillos."],
    explain=[
        "Las fuentes sobre el salitre vienen de lugares distintos. Una tabla de ingresos fiscales muestra cuánto dinero recibía el Estado. Un informe oficial expresa lo que las autoridades planeaban hacer. El testimonio de un obrero cuenta cómo se vivía en las oficinas. El relato de un visitante extranjero describe lo que vio en el puerto. Una historiadora actual interpreta el conjunto.",
        "Cada una tiene límites. La tabla muestra proporciones, pero no dice quién se benefició. El informe oficial es una promesa, no prueba que todas las obras se hicieran. El testimonio obrero muestra una experiencia concreta de trabajo y pagos con fichas, que eran vales emitidos por la empresa y válidos solo en su pulpería, es decir, en su almacén. El visitante extranjero mira el puerto, no el desierto.",
        "Al contrastar se obtiene una visión más completa: el Estado recibía ingresos importantes (Fuente A), prometía obras (B), el comercio portuario crecía (D), pero los obreros trabajaban en condiciones duras (C). La Fuente E resume que hubo fortalecimiento del Estado con desigualdades. Un buen análisis combina datos, promesas y experiencias.",
    ],
    vocab=[("ficha salario", "vale entregado por la empresa como pago, válido solo en su propio almacén"), ("pulpería", "almacén de una oficina salitrera donde se compraban los productos con fichas"), ("renta del Estado", "ingreso que recibe el Estado por impuestos u otras fuentes"), ("porcentaje", "cantidad por cada cien"), ("promesa oficial", "compromiso anunciado por una autoridad que aún no se cumple")],
    worked=[
        ("Calcular con la tabla", "En la Fuente A, ¿qué porcentaje de los ingresos fiscales provenía del salitre?",
         ["Ingresos totales: 100 millones; salitre: 45 millones.", "45 de cada 100 es el 45 %."], "El 45 %"),
        ("Detectar un límite", "La Fuente B promete caminos, puentes y escuelas. ¿Qué no permite saber?",
         ["Es una promesa de una autoridad.", "No dice si las obras se hicieron ni a quiénes beneficiaron."], "No prueba que se hicieran las obras ni a quiénes beneficiaron"),
    ],
    mistakes=[
        ("Tomar una promesa oficial como prueba de obras realizadas.", "Necesitas otra fuente que confirme las obras.", "Contrasta la promesa con registros."),
        ("Pensar que una tabla de ingresos muestra el bienestar de la gente.", "Solo muestra cuánto recibía el Estado.", "Busca fuentes sobre la vida de las personas."),
    ],
    T=[
        ("En Historia: ¿qué es una pulpería?", "Un almacén de una oficina salitrera donde se compraba con fichas", "La Fuente C la menciona."),
        ("{F} ¿Con qué se pagaba a los obreros según la Fuente C?", "Con fichas", "El testimonio lo dice."),
        ("En Historia: ¿qué es una promesa oficial?", "Un compromiso anunciado por una autoridad que aún no se cumple", "La Fuente B es un ejemplo."),
        ("{F} ¿La Fuente E es primaria o secundaria?", "Secundaria", "La escribe una historiadora actual."),
        ("{F} ¿Qué construirán las rentas del salitre según la Fuente B? A) caminos, puentes y escuelas, B) fábricas de armas, C) templos.", "A", "El informe lo dice."),
        ("{F} Una compañera dice que la Fuente B prueba que todos los obreros mejoraron su vida. ¿Qué corrección haces?", "La Fuente B es una promesa de obras y no muestra la vida de los obreros", "Es un anuncio, no una prueba."),
        ("{F} ¿Permite la Fuente A saber cuántos obreros trabajaban en el salitre? Justifica.", "No, porque solo muestra ingresos fiscales", "Es un límite de la tabla."),
        ("=", "{F} Si el año siguiente los ingresos por salitre fueron 60 millones de un total de 120, ¿qué porcentaje es el salitre?", "60*100//120", "Se divide el salitre entre el total y se pasa a porcentaje."),
        ("{F} ¿Qué fuente muestra las condiciones de trabajo de los obreros? A) la A, B) la C, C) la D.", "B", "El testimonio obrero lo hace."),
        ("{F} Explica por qué conviene contrastar la Fuente A con la Fuente C.", "Porque la tabla muestra los ingresos del Estado y el testimonio muestra cómo vivían los obreros que producían esa riqueza", "Una es dato general y otra experiencia."),
        ("{F} Redacta una conclusión de una frase con las Fuentes A y C sin exagerar.", "El salitre dio importantes ingresos al Estado, pero los obreros trabajaban pagados con fichas", "Une economía y experiencia."),
        ("{F} Evalúa la frase «la Fuente D demuestra que todos en el puerto vivían bien». A) es excesiva porque solo describe el comercio, B) es correcta, C) es correcta porque llegan barcos.", "A", "No dice nada sobre el bienestar de todos."),
        ("¿Qué otra fuente sumarías para conocer el efecto de las obras públicas en las regiones? Escríbela y explica para qué.", "Por ejemplo: un registro de escuelas construidas por provincia, para ver dónde llegaron las obras", "Completa un vacío del informe."),
    ],
    ctx=("{F} Un compañero copia la Fuente B en un afiche con el título «El salitre mejoró la vida de todos». ¿Qué fuente agregarías para equilibrar?", "La Fuente C, porque muestra las condiciones duras de los obreros", "Hay que contrastar promesas con experiencias."),
    sc=[("En Historia: ¿qué es una ficha salario?", "Un vale entregado por la empresa como pago, válido solo en su propio almacén", "Se usó en oficinas salitreras."),
        ("{F} ¿Qué porcentaje de ingresos aportaba el salitre en la Fuente A?", "El 45 %", "45 millones de 100."),
        ("¿Una promesa oficial prueba que algo se hizo? Responde sí o no y por qué.", "No, porque es un anuncio y no un registro", "Hay que contrastarla.")],
    op=("{F} Con las Fuentes A a E de arriba, escribe un párrafo de siete líneas que responda: «¿Qué muestran y qué ocultan estas fuentes sobre la riqueza del salitre?». Incluye un dato numérico, una promesa, una experiencia obrera y un límite.",
        "La Fuente A muestra que el 45 % de los ingresos fiscales venía del salitre. La Fuente B promete obras, pero no prueba que se hicieran. La Fuente C muestra a obreros pagados con fichas. Límite: ninguna fuente muestra cómo se repartió la riqueza entre todos los grupos.",
        ["dato numérico", "una promesa", "una experiencia obrera", "un límite"], ["párrafo de siete líneas"], ["tomar la promesa como hecho", "omitir la voz obrera"], "Pide a alguien de tu casa que revise que usaste el dato del 45 %."),
    reinforce="Haz una tabla con las Fuentes A a E: quién habla, qué dice y un límite.",
    extend="Escribe una pregunta que la Fuente A no permite responder.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 3
F3 = "Cuadro de ejemplo. Cambio: aumentaron los ingresos fiscales; se construyeron ferrocarriles, puertos, puentes y edificios públicos; se abrieron más escuelas y liceos; crecieron las ciudades del norte, la industria y el comercio. Continuidad: el centro del país seguía con haciendas; la economía dependía de exportar un solo producto; muchas personas vivían en conventillos o en campamentos mineros con pocos servicios; el voto seguía restringido a un grupo."
build(
    OA, 3, F3,
    use="Aprenderé a distinguir qué cambió y qué continuó con la riqueza salitrera, ubicando las transformaciones en el territorio. Sirve para evaluar la modernización sin suponer que alcanzó a todos.",
    prior=["Conozco la relación entre salitre, impuestos e inversión.", "Sé distinguir cambio y continuidad.", "Sé qué es una escala."],
    explain=[
        "La riqueza del salitre cambió el país. Aumentaron los ingresos fiscales y, con ellos, la inversión pública: se construyeron ferrocarriles, puertos y puentes, y se levantaron edificios públicos y escuelas. Crecieron los sectores productivos: la industria, que fabricaba bienes para el consumo, y el comercio. Las ciudades del norte, como Iquique y Antofagasta, aumentaron su población, y en el Pacífico creció el comercio de los puertos.",
        "También hubo continuidades. En el campo central seguían las haciendas y el inquilinaje. La economía dependía de exportar un solo producto, por lo que era vulnerable. Muchas familias vivían en conventillos de las ciudades o en campamentos de las oficinas, con pocos servicios. Y el sistema político seguía siendo restringido, con voto limitado.",
        "La escala territorial muestra diferencias. A escala nacional, el Estado se fortaleció; a escala regional, el norte se transformó; a escala local, las condiciones de cada oficina o conventillo variaron. Así, la modernización fue desigual: algunos lugares y grupos se beneficiaron más que otros.",
    ],
    vocab=[("modernización", "proceso de cambio en la economía y las instituciones con nuevas obras y actividades"), ("industria", "actividad que fabrica bienes en fábricas"), ("campamento minero", "lugar de vivienda de trabajadores cerca de una mina u oficina"), ("vulnerable", "expuesto a sufrir daño si algo cambia"), ("desigualdad territorial", "diferencia entre lugares en el acceso a obras y servicios")],
    worked=[
        ("Clasificar", "Del cuadro de ejemplo: «se construyeron ferrocarriles y puertos» y «el centro del país seguía con haciendas». ¿Cuál es cambio y cuál continuidad?",
         ["Los ferrocarriles y puertos son obras nuevas: cambio.", "Las haciendas siguen existiendo: continuidad."], "Ferrocarriles y puertos: cambio; haciendas: continuidad"),
        ("Cambiar de escala", "A escala nacional se ve un Estado más fuerte. ¿Qué se ve a escala local en un campamento minero?",
         ["Las familias viven en campamentos con pocos servicios.", "La riqueza llegó de modo distinto a cada lugar."], "Condiciones de vida con pocos servicios"),
    ],
    mistakes=[
        ("Describir la modernización como si alcanzara a todos.", "Hubo grupos y lugares con pocos servicios.", "Pregunta quién se benefició y quién no."),
        ("Olvidar la dependencia de un solo producto.", "Es una continuidad clave que explica la crisis posterior.", "Inclúyela en la columna de continuidad."),
    ],
    T=[
        ("En Historia: ¿qué es la modernización?", "El proceso de cambio en la economía y las instituciones con nuevas obras y actividades", "Es el concepto central de la clase."),
        ("{F} ¿Qué obras nombra el cuadro como cambio?", "Ferrocarriles, puertos, puentes y edificios públicos", "El cuadro las lista."),
        ("En Historia: ¿qué es la industria?", "La actividad que fabrica bienes en fábricas", "Creció en este periodo."),
        ("{F} Clasifica como cambio o continuidad: «se abrieron más escuelas y liceos».", "Cambio", "Es una ampliación de la educación."),
        ("{F} Clasifica como cambio o continuidad: «la economía dependía de exportar un solo producto».", "Continuidad", "El cuadro lo lista como continuidad."),
        ("{F} Elige la continuidad. A) crecen las ciudades del norte, B) el voto seguía restringido a un grupo, C) se construyen puertos.", "B", "Las otras son cambios."),
        ("{F} ¿Qué sectores productivos crecieron según el cuadro?", "La industria y el comercio", "El cuadro los menciona entre los cambios."),
        ("{F} ¿Qué condiciones de vida continuaron para muchas personas según el cuadro?", "Vivían en conventillos o en campamentos mineros con pocos servicios", "El cuadro lo lista como continuidad."),
        ("Explica por qué decir que «la modernización llegó a todos por igual» es inexacto.", "Porque hubo lugares y grupos con pocos servicios, como campamentos y conventillos", "La modernización fue desigual."),
        ("{F} Una compañera dice: «Con el salitre desaparecieron las haciendas». Corrige con un dato del cuadro.", "El cuadro dice que el centro del país seguía con haciendas", "La continuidad rural se mantiene."),
        ("{F} ¿Qué riesgo muestra la dependencia de un solo producto?", "Que la economía era vulnerable si el producto perdía mercado", "La dependencia hace frágil al país."),
        ("Evalúa la frase «el salitre transformó el norte y el Estado, pero no cambió todo el país». A) es razonable, B) es falsa porque cambió todo, C) es falsa porque el salitre no tuvo ningún efecto en el Estado.", "A", "Combina cambio y continuidad."),
        ("Propón una pregunta de escala local sobre una oficina salitrera.", "Por ejemplo: ¿qué servicios tenían las familias que vivían en el campamento de una oficina?", "La pregunta se ubica en un lugar concreto."),
    ],
    ctx=("{F} Un video escolar dice: «Gracias al salitre, todo Chile se modernizó por igual». Con el cuadro, escribe una frase que lo matice.", "El salitre financió obras y educación, pero siguieron las haciendas, la dependencia de un solo producto y la desigualdad", "La frase debe incluir cambio y continuidad."),
    sc=[("En Historia: ¿qué significa vulnerable?", "Estar expuesto a sufrir daño si algo cambia", "La economía dependía de un solo producto."),
        ("Nombra dos cambios del cuadro.", "Por ejemplo: se construyeron ferrocarriles y se abrieron más escuelas", "Están en el cuadro."),
        ("Nombra una continuidad del cuadro.", "Por ejemplo: el centro del país seguía con haciendas", "Está en el cuadro.")],
    op=("{F} Con el cuadro de ejemplo de arriba, construye una tabla de dos columnas (cambio y continuidad) con al menos cuatro filas, y escribe una frase final sobre la desigualdad territorial.",
        "Cambio: ferrocarriles y puertos; cambio: más escuelas; cambio: crecen las ciudades del norte; cambio: más industria. Continuidad: haciendas en el centro; continuidad: dependencia de un solo producto; continuidad: voto restringido. La modernización fue desigual: algunos lugares tenían obras y otros pocos servicios.",
        ["dos columnas", "cuatro filas", "frase sobre desigualdad territorial"], ["tabla y frase"], ["poner todo como cambio", "no mencionar desigualdad"], "Revisa con alguien de tu casa que cada dato esté en su columna."),
    reinforce="Escribe cuatro datos del cuadro y clasifícalos como cambio o continuidad.",
    extend="Escribe una pregunta sobre qué ocurrió con las ciudades del norte cuando el ciclo del salitre terminó.",
    materials=MAT,
)

# ---------------------------------------------------------------- Clase 4
F4 = "Voces de ejemplo, redactadas para este cuaderno. Ministro de Hacienda: «Con los impuestos al salitre podemos financiar escuelas y ferrocarriles.» Empresario salitrero: «Mi empresa produce y exporta; necesito que los impuestos sean razonables.» Hacendado del valle central: «Vendo carne y trigo a las oficinas del norte.» Obrero salitrero: «Mi pago son fichas y trabajo sin descanso.» Empleado de una oficina pública: «El Estado crece y necesita más funcionarios.» Dueño de un taller de la ciudad: «Mi industria vende herramientas y ropa a los trabajadores del norte.»"
build(
    OA, 4, F4,
    use="Aprenderé a identificar actores, causas y perspectivas del ciclo del salitre y a escribir un argumento corto sobre sus efectos. Sirve para explicar quién se benefició, quién no y por qué.",
    prior=["Conozco la relación entre salitre, impuestos e inversión.", "Sé qué es la multicausalidad.", "Sé escribir tesis, evidencia y límite."],
    explain=[
        "Alrededor del salitre se movían muchos actores. El Estado cobraba impuestos y los invertía en obras y educación. Los empresarios, chilenos y extranjeros, producían y exportaban. Los obreros extraían y procesaban el salitre en condiciones duras. Los hacendados del valle central vendían alimentos al norte. Los dueños de talleres e industrias vendían productos a las zonas salitreras. Y el Estado empleaba a funcionarios y profesores, que formaron un grupo creciente de sectores medios.",
        "Las causas del auge fueron varias: la demanda mundial de salitre como fertilizante, la guerra del Pacífico que cambió el control de las provincias, el sistema de impuestos a la exportación, el capital extranjero y chileno, y la mano de obra que migró al norte. Hablamos de multicausalidad porque el auge no se explica por una sola razón.",
        "Las perspectivas fueron distintas y a veces opuestas. El ministro veía recursos para el país; el empresario, costos y ganancias; el hacendado, un mercado; el obrero, trabajo duro y bajos pagos. Un argumento sobre el ciclo del salitre puede sostener que fortaleció al Estado y a algunos sectores, pero repartió sus beneficios de modo muy desigual. Su límite es que las fuentes de ejemplo no miden cuánto recibió cada grupo.",
    ],
    vocab=[("capital extranjero", "dinero invertido por empresas o personas de otros países"), ("migración interna", "traslado de personas de una región a otra del mismo país"), ("sectores medios", "grupos de empleados, profesionales y comerciantes que no son ni obreros ni grandes propietarios"), ("mano de obra", "trabajadores que realizan una labor"), ("demanda mundial", "cantidad de un producto que el mundo quiere comprar")],
    worked=[
        ("Emparejar actor e interés", "¿Qué interés expresa el empresario salitrero y cuál el obrero?",
         ["El empresario quiere impuestos razonables para producir y exportar.", "El obrero expresa que su pago son fichas y que trabaja sin descanso."], "Empresario: impuestos razonables; obrero: mejores condiciones de pago y trabajo"),
        ("Pasar de una causa a varias", "Un compañero dice: «el auge del salitre se debió solo a la demanda mundial». Da otra causa.",
         ["La demanda mundial es una causa.", "También influyó el capital extranjero y chileno y la mano de obra que migró al norte."], "El capital extranjero y chileno y la migración de trabajadores"),
    ],
    mistakes=[
        ("Presentar al Estado como único beneficiado.", "También ganaron empresarios, comerciantes, hacendados y sectores medios, y los obreros ganaron mucho menos.", "Compara los beneficios de cada actor."),
        ("Explicar el auge solo por una causa.", "Hubo varias que se combinaron.", "Escribe al menos tres factores."),
    ],
    T=[
        ("En Historia: ¿qué es la mano de obra?", "Los trabajadores que realizan una labor", "Migró al norte para trabajar."),
        ("{F} ¿Qué vende el hacendado a las oficinas del norte?", "Carne y trigo", "Su voz lo dice."),
        ("En Historia: ¿qué son los sectores medios?", "Grupos de empleados, profesionales y comerciantes que no son ni obreros ni grandes propietarios", "Crecieron con el Estado."),
        ("{F} ¿Qué necesita el Estado según el empleado de la oficina pública?", "Más funcionarios", "Su voz lo dice."),
        ("Une cada actor con su interés: 1) ministro de Hacienda, 2) empresario, 3) dueño de taller. a) impuestos razonables, b) vender herramientas y ropa, c) financiar escuelas y ferrocarriles. Escribe las parejas.", "1-c, 2-a, 3-b", "Cada voz expresa un interés distinto."),
        ("{F} Elige el actor que describe condiciones duras de trabajo. A) el obrero salitrero, B) el ministro, C) el empresario.", "A", "Su voz lo dice."),
        ("{F} ¿Qué actor vende herramientas y ropa a los trabajadores del norte?", "El dueño de un taller de la ciudad", "Su voz lo dice."),
        ("{F} Explica por qué el hacendado del valle central se beneficiaba del salitre aunque no trabajaba en el norte.", "Porque vendía carne y trigo a las oficinas del norte, que eran un mercado para sus productos", "El auge del norte creó demanda de alimentos."),
        ("{F} Una compañera dice que el obrero y el empresario tenían el mismo interés. Explica por qué es discutible.", "Porque el empresario busca ganancias y bajos costos mientras el obrero busca mejores pagos y condiciones", "Sus intereses chocaban."),
        ("Explica por qué hablamos de multicausalidad al estudiar el auge del salitre.", "Porque influyeron la demanda mundial, los impuestos, el capital y la mano de obra que migró", "Varias causas se combinaron."),
        ("{F} ¿En qué se diferencian las perspectivas del ministro y del obrero?", "El ministro ve recursos para el país; el obrero ve trabajo duro y pagos en fichas", "Sus lugares son distintos."),
        ("Evalúa la afirmación «el ciclo del salitre benefició por igual a todos los actores». A) es falsa porque los beneficios se repartieron de modo desigual, B) es correcta, C) es correcta porque había impuestos.", "A", "Hubo ganadores y excluidos."),
        ("Redacta una tesis de una frase sobre el ciclo del salitre que incluya un beneficio y un límite.", "Por ejemplo: el salitre fortaleció al Estado y a algunos sectores, pero repartió sus beneficios de modo desigual", "La tesis une avance y límite."),
    ],
    ctx=("{F} En una dramatización escolar todos los personajes dicen «el salitre nos hizo ricos». Con las voces de ejemplo, ¿cómo harías hablar al obrero y al empleado público?", "El obrero hablaría de fichas y trabajo duro y el empleado público de un Estado que crece y necesita funcionarios", "Cada personaje debe hablar desde su situación."),
    sc=[("En Historia: ¿qué es el capital extranjero?", "Dinero invertido por empresas o personas de otros países", "Fue parte del auge salitrero."),
        ("Nombra dos actores del ciclo del salitre.", "Por ejemplo: los empresarios y los obreros", "Ambos participaron en el ciclo."),
        ("¿Qué grupo creció con los empleos públicos?", "Los sectores medios", "Funcionarios y profesores lo integraban.")],
    op=("{F} Con las voces de arriba, escribe un párrafo de siete líneas que responda: «¿Quiénes se beneficiaron del ciclo del salitre y quiénes no?». Usa dos voces de ejemplo, una causa del auge, una tesis y un límite.",
        "El ministro y el empresario se beneficiaron porque el Estado recibía impuestos y la empresa exportaba. El obrero salitrero recibía fichas y trabajaba sin descanso, por lo que se benefició mucho menos. Una causa del auge fue la demanda mundial. Tesis: el salitre fortaleció al Estado, pero repartió desigualmente los beneficios. Límite: las fuentes no miden cuánto recibió cada grupo.",
        ["dos voces", "una causa", "una tesis", "un límite"], ["párrafo de siete líneas"], ["decir que todos se beneficiaron", "no incluir el límite"], "Cuenta tu texto a alguien de tu casa y pídele que identifique tu tesis."),
    reinforce="Haz una tabla con seis actores y un interés para cada uno.",
    extend="Explica por qué los sectores medios crecieron con la expansión del Estado.",
    materials=MAT,
)
