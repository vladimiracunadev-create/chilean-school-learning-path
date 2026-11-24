"""Lengua y Literatura EPJA Media Nivel 1, módulo 3: OAD-11, planificar y escribir un reportaje aplicando criterios de coherencia textual. Personas, lugares y fuentes inventados; todo se resuelve en papel."""
from __future__ import annotations

from epja_leli_nm1_c_common import build

O = "EPJA-LELI-NM1-OAD-11"

F1 = ("Texto 1 (inventado), aviso: «El martes 12 la junta de vecinos entregará cajas de útiles de aseo en la sede, entre las 10 y las 13 horas.» "
      "Texto 2 (inventado), noticia: «Ayer, un grupo de vecinos del pasaje Los Aromos limpió el sitio baldío de la esquina. Participaron 18 personas y el trabajo duró tres horas.» "
      "Texto 3 (inventado), reportaje: «El sitio baldío que se volvió huerta. Hace dos años, el terreno de la esquina acumulaba basura. Hoy 25 familias cosechan lechugas y tomates. ¿Cómo lo lograron? "
      "Doña Nora, vecina fundadora, cuenta: “Primero nos juntamos a conversar y después repartimos las tareas”. Don Iván explica que cada familia aporta una hora semanal. "
      "El cuaderno de registro muestra que el grupo creció de 8 a 25 familias.» (Todas las personas son inventadas.)")

F2 = ("Reportaje (inventado) con sus partes marcadas. [Título] Pan para el barrio. "
      "[Bajada] En una panadería comunitaria, 12 vecinas hornean cada madrugada para cuatro comedores. "
      "[Entrada] A las cinco de la mañana, el olor a pan ya llega hasta la esquina. "
      "[Desarrollo 1] La panadería comenzó en 2019 con un horno prestado y seis vecinas (registro de la panadería). "
      "[Desarrollo 2] «Aprendimos probando», cuenta Ximena, panadera (voz de ejemplo). "
      "[Desarrollo 3] Hoy producen 300 panes diarios. "
      "[Cierre] Cuando el último pan sale del horno, las vecinas ya piensan en la próxima fiesta del pasaje.")

F3 = ("Plan de reportaje (inventado) de un grupo de estudio. Tema: el taller comunitario de reparación de bicicletas del barrio. "
      "Enfoque: cómo ayuda a que más vecinos lleguen a su trabajo en bicicleta. Pregunta guía: ¿qué cambió en el barrio con el taller? "
      "Audiencia: personas del barrio que leen el diario mural. "
      "Fuentes: entrevista al encargado del taller (testimonio), registro de atenciones del taller (documento) y entrevista a un usuario. "
      "Datos reunidos: en 2022 se atendieron 60 bicicletas; en 2024, 180. Esquema: 1) cómo nació; 2) quiénes lo usan; 3) qué cambió; 4) cierre.")

F4 = ("Plan y notas (inventados) para un reportaje sobre la huerta del pasaje. Esquema: 1) cómo nació; 2) cómo se organizan; 3) qué cambió. "
      "Notas: (a) en 2022 el terreno acumulaba basura; doña Nora, vecina fundadora, recuerda: «Primero nos juntamos a conversar»; "
      "(b) se reunieron 8 familias para limpiar (cuaderno de registro); (c) hay turnos de riego los sábados y cada familia aporta una hora semanal (testimonio de don Iván); "
      "(d) hoy participan 25 familias (cuaderno de registro); (e) donan la mitad de la cosecha al comedor del barrio (testimonio de don Iván).")

F5 = ("Párrafos desordenados (inventados) de un reportaje titulado «Hilos que unen al barrio», sobre un taller de costura comunitario. "
      "A) «Hoy el taller reúne a 14 costureras que arreglan ropa para el barrio y confeccionan delantales por encargo.» "
      "B) «En 2020, seis vecinas comenzaron a juntarse los jueves con una sola máquina prestada (registro del taller).» "
      "C) «La idea es seguir creciendo: quieren abrir un segundo turno para quienes trabajan de día.» "
      "D) «“Aquí aprendí a coser y también a conversar con mis vecinas”, cuenta Marcela, costurera (voz de ejemplo).» "
      "E) «El taller se sostiene con un aporte mensual de las socias y con los pedidos que reciben.»")

F6 = ("Reportaje (inventado) de una estudiante. Título: «La ruta del reparto». Bajada: «Repartidores del barrio se organizaron para llevar compras a personas mayores». "
      "Texto: «Los repartidores se organizaron en 2021. Al principio eran cinco. Los repartidores se organizaron en 2021 porque había muchos pedidos. Hoy son diez. "
      "El mercado central es muy antiguo. Nadie quiere repartir y todos reparten. “Nos turnamos los días”, dice Hugo, repartidor (voz de ejemplo).» Cierre: «Fin.» "
      "Criterios: 1) todo trata del tema del título; 2) sin repeticiones innecesarias; 3) sin contradicciones; 4) ideas en orden y unidas por conectores; 5) cierre que deje una idea.")

# ============================================================ clase 1
build(
    O, 1, F1,
    use="Hoy parto de los textos que ya leo (avisos, noticias) para reconocer qué es un reportaje y en qué se diferencia.",
    prior=["Leo avisos y noticias cortas.", "Distingo un dato de una opinión.", "Sé que una fuente respalda un dato."],
    explain=[
        "Tú ya lees avisos y noticias en el diario mural, en el celular o en la calle. Un aviso informa algo puntual. Una noticia cuenta un hecho reciente de forma breve: qué pasó, a quién, cuándo y dónde.",
        "Un reportaje es un texto periodístico que investiga un tema a fondo. Además del hecho, explica cómo y por qué ocurrió, incluye datos, el contexto y las voces de las personas. Por eso es más largo y requiere planificación.",
        "Las voces, o testimonios, muestran cómo viven el tema las personas. Los datos lo respaldan. Ambos se citan con su fuente. Un reportaje bien hecho se entiende de principio a fin y cada párrafo aporta algo nuevo.",
    ],
    vocab=[("reportaje", "texto periodístico que investiga un tema en profundidad"), ("noticia", "texto breve que informa un hecho reciente"), ("testimonio", "relato de una persona sobre lo que vivió"), ("contexto", "información que ayuda a entender un hecho")],
    worked=[
        ("Reconocer una noticia", "«Ayer se reunieron 40 vecinos en la sede para elegir directiva» (ejemplo).", ["Informa un hecho reciente.", "Responde qué, quién, cuándo y dónde, sin explicar causas."], "Es una noticia"),
        ("Reconocer un reportaje", "Texto de una página sobre cómo se organizó un comedor solidario, con cifras y testimonios (ejemplo).", ["Investiga el tema en profundidad.", "Tiene datos, voces y contexto."], "Es un reportaje"),
    ],
    mistakes=[("Pensar que un reportaje es solo una noticia más larga.", "Se diferencia por investigar causas, contexto y voces, no solo por la extensión.", "Pregúntate si explica cómo y por qué, no solo qué pasó."),
              ("Creer que un reportaje no necesita fuentes.", "Sin datos ni fuentes, es una opinión larga.", "Respalda los datos con fuentes y cítalas.")],
    T=[
        ("abc", "{F} ¿Cuál de los textos es un reportaje?", "El Texto 3, porque investiga el tema con datos, voces y contexto", "El Texto 1, porque informa una fecha", "El Texto 2, porque nombra a los vecinos", "El reportaje profundiza en un tema; el aviso y la noticia solo informan."),
        ("ab", "{F} ¿Qué tipo de texto es el Texto 2?", "Una noticia: informa un hecho reciente con qué, quién, cuándo y dónde", "Un reportaje: explica en profundidad un tema con varias voces", "El Texto 2 cuenta un hecho reciente de forma breve."),
        ("{F} ¿Cuántas personas participaron en la limpieza según el Texto 2? Escribe solo el número.", "18", "El Texto 2 dice que participaron 18 personas."),
        ("abc", "{F} ¿Qué voces aparecen en el Texto 3?", "Dos vecinos que entregan su testimonio", "Una autoridad y un especialista", "Ninguna: solo habla quien escribe", "Doña Nora y don Iván cuentan lo que vivieron."),
        ("=", "{F} Según el Texto 3, ¿cuántas familias más cosechan hoy que al comienzo del grupo?", "25 - 8", "Se restan las familias iniciales a las actuales para ver el aumento.", "familias"),
        ("abc", "{F} ¿Qué pregunta plantea el Texto 3 para despertar interés?", "«¿Cómo lo lograron?»", "«¿Cuántas personas participaron?»", "«¿Cuándo se entregan las cajas?»", "La pregunta invita a leer el proceso, no solo un hecho."),
        ("abc", "{F} Quieres informar solo que el martes se entregan cajas. ¿Qué formato conviene?", "Un aviso breve, como el Texto 1", "Un reportaje de varias páginas", "Un poema sobre las cajas", "Un aviso entrega lo necesario sin profundizar."),
        ("abc", "{F} Quieres explicar por qué funcionó la huerta vecinal. ¿Qué formato conviene?", "Un reportaje, porque permite contar el proceso con datos y voces", "Un aviso, porque es más corto", "Una noticia de tres líneas con la fecha", "Explicar causas y proceso es propio del reportaje."),
        ("ab", "{F} ¿Qué dato del Texto 3 muestra el crecimiento del grupo?", "Que pasó de 8 a 25 familias", "Que cada familia aporta una hora semanal", "Dos cifras de años distintos permiten comparar el crecimiento."),
        ("abc", "Alguien dice: «Un reportaje es una noticia más larga». ¿Qué diferencia falta?", "El reportaje investiga causas y contexto con varias fuentes; la noticia informa un hecho", "El reportaje no tiene datos", "La noticia siempre lleva testimonios y el reportaje no", "La diferencia está en la profundidad y en las fuentes."),
        ("ab", "{F} ¿Por qué el testimonio de doña Nora enriquece el reportaje?", "Muestra cómo vivieron el proceso las personas, no solo los datos", "Reemplaza los datos del cuaderno de registro", "Las voces dan cercanía y se suman a los datos."),
        ("abc", "{F} ¿Qué elementos tiene el Texto 3 que no tiene el Texto 2?", "Contexto, testimonios y datos que explican cómo y por qué", "Fecha, lugar y cantidad de participantes", "Una fecha exacta y una hora", "El Texto 3 explica el proceso con varias voces."),
        ("{F} ¿Cuántas horas semanales aporta cada familia al trabajo de la huerta? Escribe solo el número.", "1", "Don Iván explica que cada familia aporta una hora semanal."),
    ],
    ctx=("abc", "El centro de estudios te pide un texto sobre una iniciativa de tu comunidad (un taller, un comedor) para el diario mural. Quieres que se entienda cómo funciona y por qué. ¿Qué formato eliges?", "Un reportaje, porque permite explicar con datos y voces", "Un aviso de una línea", "Una lista de nombres", "Para explicar cómo y por qué se necesita un reportaje."),
    sc=[("En Lengua y Literatura: ¿qué es un reportaje?", "Un texto periodístico que investiga un tema en profundidad", "Explica cómo y por qué con datos y voces."),
        ("En Lengua y Literatura: ¿en qué se diferencia una noticia de un reportaje?", "La noticia informa un hecho breve; el reportaje investiga y explica", "La noticia informa; el reportaje profundiza."),
        ("En Lengua y Literatura: ¿qué es un testimonio?", "El relato de una persona sobre lo que vivió", "Aporta la voz de quien vivió el tema.")],
    op=("{F} Elige una de estas iniciativas inventadas y escribe un párrafo de cuatro a cinco líneas que sirva de inicio de un reportaje: A) un taller de reparación de bicicletas con 20 vecinos y tres años de trabajo; B) un comedor solidario que sirve 80 almuerzos; C) una feria vecinal con 15 puestos. Incluye un dato y la voz de una persona inventada, rotulada «de ejemplo».",
        "Opción B: En un salón de la sede, 80 almuerzos salen cada semana de una olla grande. «Aquí cocinamos entre todos», cuenta Rosa, voluntaria (voz de ejemplo). El comedor comenzó con 20 almuerzos hace tres años.",
        ["incluye un dato concreto", "incluye una voz rotulada como de ejemplo", "se entiende que es el inicio de un reportaje, no de un aviso"],
        ["párrafo de cuatro a cinco líneas con un dato y una voz"],
        ["escribir solo un aviso", "inventar datos sin rotularlos como de ejemplo"],
        "Pregunta de revisión: «¿Mi párrafo explica algo más que un hecho puntual?»."),
    reinforce="Escribe una noticia de dos líneas y una oración inicial de reportaje sobre un mismo hecho inventado de tu barrio.",
    extend="Busca dos textos que leas en la semana y anota si son aviso, noticia o reportaje y qué elementos te hicieron decidir.",
)

# ============================================================ clase 2
build(
    O, 2, F2,
    use="Hoy reconozco las partes de un reportaje (título, bajada, entrada, desarrollo y cierre) y su propósito y audiencia.",
    prior=["Distingo un reportaje de una noticia.", "Sé que las voces y los datos se citan.", "Identifico la idea principal de un párrafo."],
    explain=[
        "Un reportaje tiene partes con funciones distintas. El título anuncia el tema. La bajada resume en una o dos oraciones de qué trata. La entrada capta la atención de quien lee. El desarrollo explica con datos y voces. El cierre deja una idea final.",
        "El desarrollo se organiza en párrafos, cada uno con una idea principal. Las voces muestran la experiencia de las personas y los datos respaldan lo que se cuenta. Todo debe tener relación con el tema del título.",
        "Antes de escribir, define el propósito (qué quieres lograr: informar, dar a conocer, convencer) y la audiencia (quiénes lo leerán). Con eso eliges el lenguaje: más cercano para tu comunidad, más técnico para especialistas.",
    ],
    vocab=[("bajada", "resumen breve bajo el título"), ("entrada", "inicio que capta la atención y presenta el tema"), ("desarrollo", "parte central, con datos, voces y explicaciones"), ("audiencia", "personas a quienes se dirige el texto")],
    worked=[
        ("Reconocer la bajada", "Título: «Un taller, una comunidad». Texto debajo: «Veinte vecinas comparten máquinas de coser para arreglar ropa a bajo costo» (ejemplo).", ["La oración resume de qué trata el reportaje.", "Está inmediatamente bajo el título."], "Es la bajada"),
        ("Elegir la audiencia", "Un reportaje para el diario mural de tu población (ejemplo).", ["Las personas lectoras son vecinas y vecinos.", "Uso un lenguaje cercano y ejemplos del barrio."], "Audiencia: la comunidad del barrio"),
    ],
    mistakes=[("Confundir la bajada con la entrada.", "La bajada resume el tema; la entrada comienza el relato.", "La bajada va bajo el título; la entrada abre el texto."),
              ("Escribir sin pensar en quién leerá.", "El lenguaje y los ejemplos pueden no servir a su audiencia.", "Decide primero propósito y audiencia.")],
    T=[
        ("abc", "{F} ¿Qué parte cumple la función de bajada?", "«En una panadería comunitaria, 12 vecinas hornean cada madrugada para cuatro comedores»", "«Pan para el barrio»", "«A las cinco de la mañana, el olor a pan ya llega hasta la esquina»", "La bajada resume el tema en una o dos oraciones, bajo el título."),
        ("ab", "{F} ¿Para qué sirve la entrada?", "Para captar la atención y presentar el tema", "Para dar la lista de referencias", "La entrada abre el texto y engancha a quien lee."),
        ("{F} ¿Cuántas vecinas hornean cada madrugada según la bajada? Escribe solo el número.", "12", "La bajada dice que son 12 vecinas."),
        ("abc", "{F} ¿Qué parte del reportaje presenta la voz de una persona?", "El desarrollo 2, con el testimonio de Ximena", "La bajada", "El título", "Solo el desarrollo 2 incluye lo que dice una panadera."),
        ("=", "{F} ¿Cuántas vecinas más hornean hoy que al comienzo en 2019?", "12 - 6", "Se restan las vecinas de 2019 a las de hoy para ver el aumento.", "vecinas"),
        ("abc", "{F} ¿Qué hace el cierre del reportaje?", "Termina con una imagen que deja una idea a quien lee", "Presenta nuevas cifras sin relacionarlas", "Repite el título completo", "El cierre completa el texto con una idea final."),
        ("abc", "{F} ¿Qué datos respaldan la afirmación de que la panadería creció?", "Pasó de seis vecinas y un horno prestado a 12 vecinas y 300 panes diarios", "El olor llega hasta la esquina", "El cierre habla de la fiesta del pasaje", "Los números de dos momentos distintos muestran el crecimiento."),
        ("ab", "{F} ¿Cuál es el propósito principal del reportaje?", "Dar a conocer a la comunidad cómo funciona la panadería", "Vender pan a precio de oferta", "El texto explica el funcionamiento de la iniciativa."),
        ("abc", "{F} ¿Qué título alternativo mantiene la idea del reportaje?", "Doce vecinas y 300 panes cada día", "El mejor pan de todo el país", "Sobre la harina", "Resume lo central del reportaje sin exagerar."),
        ("ab", "{F} ¿Por qué conviene incluir una voz directa como la de Ximena?", "Da cercanía y respalda lo que se cuenta con una experiencia real", "Reemplaza el dato de los 300 panes", "Las voces acompañan los datos, no los reemplazan."),
        ("abc", "Un reportaje tiene título y desarrollo, pero le falta la entrada. ¿Qué ocurre?", "El texto empieza de golpe y cuesta engancharse con el tema", "No se puede publicar", "Se entiende mejor porque es más corto", "Sin entrada, falta una apertura que presente el tema."),
        ("abc", "{F} ¿Cuál es el orden correcto de las partes?", "Título, bajada, entrada, desarrollo, cierre", "Entrada, título, desarrollo, bajada, cierre", "Cierre, título, bajada, desarrollo, entrada", "Es el orden en que se lee un reportaje."),
        ("{F} ¿Cuántas partes del desarrollo tiene el reportaje? Escribe solo el número.", "3", "La ficha marca Desarrollo 1, 2 y 3."),
    ],
    ctx=("abc", "Escribirás para el boletín de tu comunidad un reportaje sobre un grupo de trabajadoras. ¿Qué defines antes de empezar a escribir?", "El propósito y la audiencia: qué quieres lograr y quiénes lo leerán", "Solo el tamaño de la letra", "El color de la portada", "Propósito y audiencia guían el lenguaje y los datos."),
    sc=[("En Lengua y Literatura: ¿qué es la bajada de un reportaje?", "Un resumen breve del tema, bajo el título", "Resume de qué trata el reportaje."),
        ("En Lengua y Literatura: ¿para qué sirve el cierre?", "Para dejar una idea final a quien lee", "Completa el texto con una idea que queda."),
        ("En Lengua y Literatura: ¿qué es la audiencia?", "Las personas a quienes se dirige el texto", "Se define para escribir con un lenguaje adecuado.")],
    op=("{F} Escribe en tu cuaderno un título, una bajada y una oración de entrada para un reportaje nuevo sobre uno de estos temas inventados: A) un grupo de vecinos que repara juguetes para donar; B) una cooperativa de recicladores de base de un barrio ficticio; C) una escuela nocturna de oficios. Indica en una línea su propósito y su audiencia.",
        "Tema A. Título: Juguetes con segunda vida. Bajada: Un grupo de vecinos repara juguetes viejos para regalarlos a los niños del barrio. Entrada: Los sábados, la mesa de la sede se llena de ruedas, botones y pegamento. Propósito: dar a conocer la iniciativa. Audiencia: vecinos del barrio.",
        ["el título, la bajada y la entrada cumplen funciones distintas", "la bajada resume el tema", "indica propósito y audiencia"],
        ["título, bajada, entrada y una línea de propósito y audiencia"],
        ["repetir el título en la bajada", "olvidar la audiencia"],
        "Pregunta de revisión: «¿Puedo distinguir qué hace cada una de mis tres partes?»."),
    reinforce="Toma un reportaje o texto largo que hayas leído y anota su título, su bajada y cómo termina.",
    extend="Escribe dos entradas distintas para el mismo tema: una que comience con una imagen y otra que comience con un dato. Decide cuál te gusta más y por qué.",
)

# ============================================================ clase 3
build(
    O, 3, F3,
    use="Hoy veo paso a paso cómo planificar un reportaje: tema, enfoque, pregunta guía, audiencia, fuentes y esquema.",
    prior=["Reconozco las partes de un reportaje.", "Sé organizar notas en un esquema.", "Distingo fuentes primarias y secundarias."],
    explain=[
        "Planificar es decidir antes de escribir. Parte por el tema, que es el asunto general. Luego define el enfoque: el ángulo desde el cual lo tratarás. Un mismo tema, como un taller, puede abordarse desde su historia, sus costos o su efecto en el barrio.",
        "La pregunta guía es la que el reportaje responderá. Todo dato debe ayudar a responderla. Define también la audiencia y las fuentes: entrevistas (testimonios), documentos y datos. Prepara preguntas para las entrevistas.",
        "Por último arma el esquema, con las partes y los puntos del desarrollo. Revisa que cada punto responda a la pregunta guía y que cada dato tenga fuente. Lo que no ayude al enfoque, se deja fuera.",
    ],
    vocab=[("tema", "asunto general del que trata el reportaje"), ("enfoque", "ángulo desde el que se trata el tema"), ("pregunta guía", "pregunta que el reportaje responde"), ("plan", "decisiones previas a escribir: tema, enfoque, fuentes y esquema")],
    worked=[
        ("Definir el enfoque", "Tema: un comedor solidario. Un grupo quiere mostrar cómo se organiza el trabajo (ejemplo).", ["El tema es amplio.", "Elijo un ángulo: la organización del trabajo voluntario."], "Enfoque: cómo se organiza el trabajo voluntario del comedor"),
        ("Formular la pregunta guía", "Enfoque: el efecto de una biblioteca comunitaria en la lectura de las personas del barrio (ejemplo).", ["La pregunta debe poder responderse con datos y voces.", "La escribo con «cómo cambió»."], "Pregunta guía: ¿cómo cambió la lectura en el barrio con la biblioteca?"),
    ],
    mistakes=[("Tratar de contarlo todo sobre un tema.", "Un reportaje sin enfoque se dispersa.", "Elige un ángulo y deja fuera lo que no ayude a responder la pregunta guía."),
              ("Salir a escribir sin tener fuentes.", "Sin fuentes, el reportaje queda sin respaldo.", "Decide con quién conversarás y qué documentos revisarás.")],
    T=[
        ("abc", "En Lengua y Literatura: ¿qué es el enfoque de un reportaje?", "El ángulo desde el que se trata el tema", "El título definitivo", "La cantidad de páginas", "El enfoque es la mirada elegida sobre el tema."),
        ("ab", "{F} ¿Cuál es la pregunta guía del plan?", "¿Qué cambió en el barrio con el taller?", "¿Cuánto cuesta una bicicleta nueva?", "La pregunta guía está escrita en el plan."),
        ("{F} ¿Cuántas bicicletas se atendieron en 2024? Escribe solo el número.", "180", "El plan dice que en 2024 se atendieron 180 bicicletas."),
        ("abc", "{F} ¿Qué fuente del plan es un documento?", "El registro de atenciones del taller", "La entrevista al encargado", "La entrevista a un usuario", "Un registro escrito es un documento; las entrevistas son testimonios."),
        ("=", "{F} ¿Cuántas bicicletas más se atendieron en 2024 que en 2022?", "180 - 60", "Se restan las bicicletas de 2022 a las de 2024 para ver el aumento.", "bicicletas"),
        ("abc", "{F} ¿Para quién se escribe el reportaje?", "Para personas del barrio que leen el diario mural", "Para especialistas en mecánica", "Para nadie en particular", "El plan define la audiencia del reportaje."),
        ("abc", "{F} ¿Qué punto del esquema responde a «quiénes usan el taller»?", "El punto 2", "El punto 1", "El punto 4", "El punto 2 del esquema trata de los usuarios."),
        ("abc", "{F} Buscas un dato para el punto 3 (qué cambió). ¿Cuál sirve más?", "El aumento de 60 a 180 bicicletas atendidas", "El color de las paredes del taller", "El nombre de una calle cercana", "El aumento muestra un cambio en el uso del taller."),
        ("ab", "{F} ¿Qué pregunta de entrevista al encargado sirve al punto 1 (cómo nació)?", "¿Cómo y cuándo comenzó el taller?", "¿Qué marca de bicicleta prefiere?", "La pregunta sobre el origen responde al punto 1."),
        ("ab", "{F} El grupo quiere agregar la historia de toda la ciudad. ¿Conviene?", "No: se aleja del enfoque y de la pregunta guía", "Sí: mientras más temas, mejor reportaje", "Lo que no ayuda a responder la pregunta guía se deja fuera."),
        ("abc", "{F} ¿Qué falta en el plan para asegurar que los datos sean confiables?", "Anotar de dónde sale cada dato y contrastarlo con otra fuente", "Agregar más adjetivos al tema", "Cambiar el título del reportaje", "La confiabilidad depende de fuentes anotadas y contrastadas."),
        ("abc", "{F} ¿Cuál es el plan más completo para este reportaje?", "Tema, enfoque, pregunta guía, audiencia, fuentes y esquema con cuatro puntos", "Solo el tema y el título", "Una lista de datos sin orden", "Un plan completo cubre todos esos elementos."),
        ("abc", "{F} Un usuario del taller asegura que en 2022 se atendieron 70 bicicletas y no 60. ¿Qué haces antes de escribir?", "Verifico el dato con el registro o con el encargado y corrijo el plan si hace falta", "Dejo 60, porque ya está escrito", "Quito todos los datos del reportaje", "Un dato dudoso se comprueba antes de usarlo."),
    ],
    ctx=("abc", "Tu comunidad quiere un reportaje sobre el comedor solidario del barrio. Antes de escribir, ¿qué haces?", "Definir el enfoque, la pregunta guía, las fuentes y el esquema", "Escribir de una vez lo que recuerdes", "Copiar un reportaje de otro barrio", "Planificar evita un texto disperso y sin respaldo."),
    sc=[("En Lengua y Literatura: ¿qué es la pregunta guía de un reportaje?", "La pregunta que el reportaje responde", "Todo dato debe ayudar a responderla."),
        ("En Lengua y Literatura: ¿qué diferencia hay entre tema y enfoque?", "El tema es el asunto general; el enfoque es el ángulo elegido", "El enfoque delimita el tema general a un ángulo concreto."),
        ("En Lengua y Literatura: ¿qué incluye un plan de reportaje?", "Tema, enfoque, pregunta guía, audiencia, fuentes y esquema", "Son las decisiones previas a escribir.")],
    op=("{F} Escribe tu propio plan de reportaje sobre uno de estos temas inventados: A) una radio comunitaria; B) un grupo de ahorro vecinal; C) una huerta escolar nocturna. Debe tener tema, enfoque, pregunta guía, audiencia, dos fuentes (una testimonio y una documento) y un esquema de tres puntos. Escribe también dos preguntas para una entrevista.",
        "Tema B: grupo de ahorro vecinal. Enfoque: cómo ayuda a pagar gastos del hogar. Pregunta guía: ¿qué cambió para las familias del grupo? Audiencia: vecinos. Fuentes: entrevista a la tesorera (testimonio) y cuaderno de registro (documento). Esquema: 1) cómo nació; 2) cómo funciona; 3) qué cambió. Preguntas: ¿cómo comenzaron?, ¿qué reglas tienen?",
        ["el plan tiene todos los elementos pedidos", "el enfoque es más específico que el tema", "las preguntas de entrevista se relacionan con el esquema"],
        ["plan completo y dos preguntas de entrevista"],
        ["no distinguir tema de enfoque", "olvidar las fuentes"],
        "Pregunta de revisión: «¿Cada punto de mi esquema ayuda a responder la pregunta guía?»."),
    reinforce="Escribe una pregunta guía para un reportaje sobre una iniciativa de tu comunidad (sin datos personales).",
    extend="Haz una lista de cinco preguntas para entrevistar a una persona fundadora de una organización de tu comunidad y ordénalas según el esquema de tres puntos.",
)

# ============================================================ clase 4
build(
    O, 4, F4,
    use="Hoy practico con apoyo la escritura del reportaje: párrafos con idea principal, voces citadas y conectores que mantienen la coherencia.",
    prior=["Sé qué partes tiene un reportaje.", "Tengo un plan con esquema.", "Uso conectores y cito fuentes."],
    explain=[
        "Con el plan listo, escribes párrafo por párrafo. Cada párrafo tiene una idea principal, que puedes anunciar en la primera oración, y datos o voces que la apoyan. No mezcles ideas distintas en un mismo párrafo.",
        "Cuando incluyas un testimonio, preséntalo con un verbo y el nombre de quien habla: «…», cuenta doña Nora. Así quien lee sabe quién lo dice. Los datos se acompañan de su fuente.",
        "Para mantener la coherencia, cada párrafo debe continuar al anterior. Los conectores como «con el tiempo», «además» o «por eso» muestran esa relación. Evita repetir lo ya dicho: avanza con información nueva.",
    ],
    vocab=[("párrafo", "bloque de oraciones sobre una idea principal"), ("idea principal", "lo central que dice el párrafo"), ("verbo de habla", "verbo que presenta lo dicho por alguien: cuenta, explica, recuerda"), ("progresión", "avance de las ideas, con información nueva en cada párrafo")],
    worked=[
        ("Integrar un testimonio", "Nota: una vecina recuerda que al principio nadie conocía el proyecto (ejemplo).", ["Escribo la frase de la vecina entre comillas.", "La presento con su nombre y un verbo de habla."], "«Al principio nadie lo conocía», recuerda Marta, vecina (voz de ejemplo)."),
        ("Unir dos párrafos", "Párrafo 1 cuenta cómo nació un taller; párrafo 2 explica cómo funciona hoy (ejemplo).", ["Busco la relación: el segundo sigue en el tiempo.", "Empiezo con «Hoy» o «Con el tiempo»."], "Con el tiempo, el taller se organizó en turnos."),
    ],
    mistakes=[("Poner un testimonio sin decir quién habla.", "Quien lee no sabe de dónde viene esa voz.", "Presenta siempre a la persona con un verbo de habla."),
              ("Repetir en el segundo párrafo lo que dijo el primero.", "El texto no avanza y cansa.", "Cada párrafo aporta información nueva.")],
    T=[
        ("abc", "¿Qué debe tener un párrafo del desarrollo?", "Una idea principal y datos o voces que la apoyan", "Cinco ideas distintas sin relación", "Solo una pregunta", "Un párrafo claro trata una idea con apoyos."),
        ("abc", "{F} ¿Cuál es la mejor oración de entrada para el punto 1?", "En 2022, el terreno de la esquina era un basural; hoy es una huerta con 25 familias.", "El pasaje tiene muchas cosas lindas.", "Las huertas son importantes para todo el mundo.", "La mejor entrada presenta el tema con datos del plan."),
        ("{F} ¿Cuántas familias se reunieron para limpiar el terreno? Escribe solo el número.", "8", "La nota (b) dice que fueron 8 familias."),
        ("ab", "{F} ¿Qué nota pertenece al punto 2, cómo se organizan?", "La (c): turnos de riego los sábados", "La (a): el terreno acumulaba basura", "Los turnos y las horas de aporte describen la organización."),
        ("=", "{F} ¿Cuántas familias más participan hoy que cuando se reunieron para limpiar?", "25 - 8", "Se restan las familias iniciales a las actuales para ver el aumento.", "familias"),
        ("abc", "{F} ¿Cómo se integra bien el testimonio de doña Nora?", "«Primero nos juntamos a conversar», recuerda doña Nora, vecina fundadora.", "Doña Nora dijo cosas y nosotros las anotamos.", "Nora, Nora: juntarse y conversar.", "La buena versión presenta a quien habla y cita sus palabras."),
        ("ab", "{F} ¿Qué expresión une bien «se reunieron 8 familias» con «hoy participan 25 familias»?", "Con el tiempo", "Sin embargo", "La relación es de crecimiento a lo largo del tiempo."),
        ("abc", "{F} ¿Cuál párrafo del punto 2 está mejor escrito?", "La huerta se organiza con turnos: cada familia aporta una hora semanal y se riega los sábados (testimonio de don Iván).", "La huerta se organiza. Se riega. Familias. Una hora.", "La huerta se organiza porque es linda y todos la quieren mucho.", "Tiene idea principal, datos y fuente."),
        ("{F} ¿Cuántas horas semanales aporta cada familia? Escribe solo el número.", "1", "La nota (c) dice que aporta una hora semanal."),
        ("abc", "{F} ¿Qué problema tiene empezar el reportaje con la nota (e) y luego la (a)?", "Rompe el orden lógico: se habla de la donación antes de contar cómo nació la huerta", "Ninguno, porque son notas del mismo reportaje", "Que la nota (e) no tiene fuente", "El orden del texto debe seguir el esquema: nació, se organiza, cambió."),
        ("ab", "{F} ¿Por qué conviene que cada párrafo trate de una sola idea?", "Para que quien lee pueda seguir el hilo sin perderse", "Para que el reportaje sea más largo", "Una idea por párrafo da claridad y orden."),
        ("abc", "{F} ¿Cuál es el mejor cierre para este reportaje?", "Hoy, 25 familias comparten el trabajo y la cosecha de lo que antes era un basural.", "En conclusión, las huertas son lo mejor del mundo.", "Eso es todo lo que se sabe.", "El cierre retoma el cambio central con datos del plan."),
        ("abc", "{F} ¿Cuál es la mejor oración que une las notas (d) y (e)?", "Hoy 25 familias participan y donan la mitad de la cosecha al comedor del barrio.", "Hoy 25 familias participan. Donan la mitad. La cosecha. El comedor.", "Hoy participan porque donan sin embargo la mitad.", "Une los datos con claridad y sin cortes bruscos."),
    ],
    ctx=("abc", "Escribes para el boletín de tu comunidad un reportaje sobre un comedor de trabajadores. Tienes la frase de una cocinera. ¿Cómo la incluyes?", "Entre comillas, con su nombre y un verbo como «cuenta» o «explica»", "Sin comillas, como si fuera tuya", "Al final, sin decir quién la dijo", "Una voz citada debe presentarse con su autor."),
    sc=[("En Lengua y Literatura: ¿qué es una idea principal en un párrafo?", "Lo central que dice el párrafo", "El resto de la información la apoya."),
        ("En Lengua y Literatura: ¿cómo se presenta un testimonio?", "Entre comillas, con quien habla y un verbo de habla", "Así se sabe quién lo dice."),
        ("En Lengua y Literatura: ¿por qué un párrafo no debe repetir al anterior?", "Porque el texto debe avanzar con información nueva", "La progresión evita que el texto se estanque.")],
    op=("{F} Escribe en tu cuaderno dos párrafos del desarrollo del reportaje: uno para el punto 1 (cómo nació) y otro para el punto 2 (cómo se organizan). Usa al menos una voz citada con verbo de habla, dos conectores distintos, y no repitas ideas entre los párrafos.",
        "Punto 1: En 2022, el terreno de la esquina era un basural. «Primero nos juntamos a conversar», recuerda doña Nora. Ocho familias se animaron a limpiar (cuaderno de registro). Punto 2: Con el tiempo, el trabajo se ordenó en turnos: cada familia aporta una hora semanal y se riega los sábados (testimonio de don Iván).",
        ["cada párrafo tiene una idea principal", "incluye una voz citada con verbo de habla", "usa dos conectores y avanza sin repetir"],
        ["dos párrafos de tres a cuatro líneas cada uno"],
        ["dejar la voz sin presentar", "repetir el mismo dato en ambos párrafos"],
        "Pregunta de revisión: «¿El segundo párrafo agrega algo nuevo respecto del primero?»."),
    reinforce="Escribe una oración que incluya la frase de una vecina inventada con su nombre y un verbo de habla.",
    extend="Escribe un párrafo de cierre para el mismo reportaje que se relacione con el título y retome la idea central.",
)

# ============================================================ clase 5
build(
    O, 5, F5,
    use="Hoy aplico lo aprendido a un reportaje breve: ordeno los párrafos, uno las ideas y reviso la coherencia del conjunto.",
    prior=["Planifico un reportaje.", "Escribo párrafos con idea principal.", "Uso conectores y citas."],
    explain=[
        "Un reportaje bien armado tiene un hilo: cada párrafo continúa al anterior y se relaciona con el título. Para ordenar párrafos sueltos, busca el que presenta el origen, los que explican el presente y el que mira hacia adelante.",
        "La coherencia del conjunto exige que todo se refiera al mismo tema, que nada contradiga lo dicho y que no se agreguen datos ajenos. La cohesión se logra con conectores, pronombres y expresiones de tiempo que unen un párrafo con el siguiente.",
        "Las voces se ubican donde aporten más: después de un dato, para darle cara humana. El cierre mira hacia lo que viene o retoma la idea central. Siempre revisa que cada dato tenga su fuente.",
    ],
    vocab=[("hilo del texto", "relación lógica que une los párrafos"), ("cohesión", "unión de las oraciones y párrafos con conectores y reemplazos"), ("dato ajeno", "dato que no se relaciona con el tema"), ("progresión temática", "avance del tema con información nueva en cada párrafo")],
    worked=[
        ("Ordenar párrafos", "Tres párrafos de un reportaje: uno cuenta el origen, otro el presente y otro los planes futuros (ejemplo).", ["El origen va primero.", "Luego el presente.", "Al final, lo que viene."], "Orden: origen, presente, futuro"),
        ("Detectar un dato ajeno", "En un reportaje sobre una feria aparece «el precio de la bencina subió ayer» (ejemplo).", ["No se relaciona con la feria.", "Rompe el hilo del texto."], "Se quita porque rompe la coherencia"),
    ],
    mistakes=[("Ubicar el cierre en medio del texto.", "El texto pierde su final natural.", "El cierre va al final y retoma la idea central."),
              ("Agregar datos interesantes pero ajenos al tema.", "Dispersan la atención y rompen la coherencia.", "Incluye solo lo que ayuda a la pregunta guía.")],
    T=[
        ("abc", "{F} Para seguir el orden cronológico, ¿qué párrafo va primero?", "El B, que cuenta cómo comenzó en 2020", "El A, que describe el taller de hoy", "El C, que habla de planes futuros", "El origen del taller va antes que el presente."),
        ("{F} ¿Cuántas costureras reúne hoy el taller? Escribe solo el número.", "14", "El párrafo A dice que reúne a 14 costureras."),
        ("=", "{F} ¿Cuántas costureras más tiene hoy el taller que cuando comenzó?", "14 - 6", "Se restan las costureras del comienzo a las de hoy para ver el aumento.", "costureras"),
        ("abc", "{F} ¿Qué párrafo contiene un testimonio?", "El D", "El A", "El C", "El párrafo D es la voz de Marcela, costurera."),
        ("abc", "{F} ¿Qué párrafo funciona mejor como cierre?", "El C, porque mira hacia adelante y deja una idea final", "El B, porque tiene una fecha", "El A, porque da cifras actuales", "El C proyecta lo que vendrá."),
        ("abc", "{F} ¿Cuál es el orden más coherente de los cinco párrafos?", "B, A, E, D, C", "C, A, B, D, E", "D, C, E, A, B", "Va del origen al presente, luego a la voz y al futuro."),
        ("ab", "{F} ¿Qué expresión sirve para abrir el párrafo A después del B?", "Con el tiempo", "Sin embargo", "El párrafo A muestra la evolución del taller."),
        ("abc", "{F} Falta un conector entre E y D para sumar la voz de una costurera. ¿Cuál conviene?", "Además", "Aunque", "Por lo tanto", "«Además» suma una idea nueva a la anterior."),
        ("ab", "{F} ¿Qué fuente respalda el párrafo B?", "El registro del taller", "Una voz de ejemplo", "El párrafo B indica entre paréntesis su fuente."),
        ("ab", "{F} Alguien propone borrar el párrafo D porque «es solo una opinión». ¿Qué respondes?", "Es un testimonio que da cercanía; acompaña los datos y no los reemplaza", "Tiene razón: un reportaje solo debe tener cifras", "Las voces forman parte del reportaje y se suman a los datos."),
        ("abc", "{F} ¿Por qué el título «Hilos que unen al barrio» es coherente con el contenido?", "Alude a la costura y a la unión entre vecinas, tema de todos los párrafos", "Porque usa muchas palabras", "Porque nombra una ciudad", "El título anuncia el tema que tratan los cinco párrafos."),
        ("abc", "{F} Se agrega la oración «El precio del dólar subió ayer». ¿Qué problema genera?", "Es ajena al tema y rompe la coherencia", "Ninguno, porque agrega un dato", "Mejora el cierre del reportaje", "No tiene relación con el taller ni con su título."),
        ("{F} ¿Qué letra identifica el párrafo que explica cómo se financia el taller? Responde con la letra.", "E", "El párrafo E habla del aporte mensual y de los pedidos."),
    ],
    ctx=("abc", "Debes pasar en limpio un reportaje breve para el boletín de tu comunidad. Tienes cinco párrafos sueltos. ¿Qué haces antes?", "Ordenarlos con un hilo lógico, revisar conectores y verificar las fuentes", "Pasarlos en el orden en que los escribiste", "Quitar los títulos y las citas", "Un buen orden y fuentes claras dan coherencia."),
    sc=[("En Lengua y Literatura: ¿qué es la progresión temática?", "El avance del tema con información nueva en cada párrafo", "Cada párrafo aporta información nueva que hace avanzar el texto."),
        ("En Lengua y Literatura: ¿qué hace un dato ajeno?", "Rompe la coherencia porque no se relaciona con el tema", "No ayuda a responder la pregunta guía."),
        ("En Lengua y Literatura: ¿dónde se ubica el cierre?", "Al final, retomando la idea central o mirando hacia adelante", "Completa el texto con una idea final.")],
    op=("{F} Reescribe en tu cuaderno el reportaje completo en el orden correcto, con una entrada breve de dos líneas antes del párrafo B y agregando un conector al comienzo de al menos tres párrafos. No agregues datos nuevos: solo usa los de la ficha. Al final escribe cuáles son las dos fuentes que citarías.",
        "Entrada: Cada jueves, las máquinas de coser del barrio suenan hasta tarde. B: En 2020, seis vecinas comenzaron a juntarse los jueves con una máquina prestada (registro del taller). A: Con el tiempo, hoy el taller reúne a 14 costureras... Fuentes: registro del taller y entrevista a Marcela (voz de ejemplo).",
        ["ordena los párrafos con el hilo origen, presente, voz y futuro", "agrega una entrada y al menos tres conectores", "no agrega datos nuevos y señala sus fuentes"],
        ["reportaje de siete a ocho líneas con entrada y fuentes"],
        ["agregar datos ajenos", "dejar el cierre en medio"],
        "Pregunta de revisión: «¿Cada párrafo continúa al anterior y se relaciona con el título?»."),
    reinforce="Elige un orden distinto para tres oraciones de un correo que escribas y explica cuál es más claro.",
    extend="Agrega al reportaje un sexto párrafo que se relacione con el título y escribe qué lugar debería ocupar y por qué.",
)

# ============================================================ clase 6
build(
    O, 6, F6,
    use="Hoy reviso un reportaje con criterios de coherencia textual (tema, repetición, contradicción, orden y cierre) y decido qué mejorar.",
    prior=["Escribo reportajes con partes claras.", "Uso conectores.", "Reviso con una lista de criterios."],
    explain=[
        "Revisar la coherencia es comprobar que el texto se entienda de principio a fin. Revisa cinco cosas: que todo trate el tema del título, que no haya repeticiones innecesarias, que no se contradiga, que las ideas estén en orden con conectores y que el cierre deje una idea.",
        "Una contradicción ocurre cuando una oración niega a otra, como «nadie quiere repartir y todos reparten». Una repetición innecesaria dice lo mismo dos veces. Un dato ajeno no se relaciona con el tema y se quita.",
        "Al revisar, marca la oración que no cumple y escribe cómo la corregirías. Después reescribe y vuelve a leer con los mismos criterios. La revisión mejora el texto sin cambiar quién eres como escritor o escritora.",
    ],
    vocab=[("contradicción", "oración que niega lo que dice otra"), ("repetición innecesaria", "idea o palabra repetida que no aporta"), ("dato ajeno", "dato sin relación con el tema"), ("coherencia", "relación lógica de todas las partes con un mismo tema")],
    worked=[
        ("Detectar una contradicción", "Texto: «El taller abre todos los días» y «el taller solo abre los jueves» (ejemplo).", ["Las dos oraciones no pueden ser verdaderas a la vez.", "Hay que verificar el dato y dejar una."], "Hay contradicción: se verifica y se corrige"),
        ("Revisar con criterios", "Reportaje con un párrafo sobre el clima del mes, ajeno al tema de la feria (ejemplo).", ["Criterio 1: todo trata del tema.", "El párrafo del clima no se relaciona."], "Se quita el párrafo ajeno"),
    ],
    mistakes=[("Corregir solo ortografía y dejar el desorden de ideas.", "El texto sigue sin entenderse bien.", "Revisa primero tema, repeticiones, contradicciones y orden."),
              ("Dejar un dato interesante aunque no se relacione con el tema.", "Rompe la coherencia, porque no se relaciona con el tema.", "Quítalo o crea una conexión clara con el tema.")],
    T=[
        ("abc", "{F} ¿Qué oración se aleja del tema y rompe la coherencia?", "«El mercado central es muy antiguo»", "«Hoy son diez»", "«Al principio eran cinco»", "La oración sobre el mercado no se relaciona con los repartidores."),
        ("abc", "{F} ¿Qué oración contradice a otra y debe corregirse?", "«Nadie quiere repartir y todos reparten»", "«Nos turnamos los días»", "«Los repartidores se organizaron en 2021»", "No puede ser que nadie quiera repartir si todos reparten."),
        ("{F} ¿Cuántos repartidores hay hoy según el texto? Escribe solo el número.", "10", "El texto dice que hoy son diez."),
        ("=", "{F} ¿Cuántos repartidores más hay hoy que al principio?", "10 - 5", "Se restan los repartidores del comienzo a los actuales para ver el aumento.", "repartidores"),
        ("ab", "{F} ¿Qué criterio incumple repetir «Los repartidores se organizaron en 2021»?", "El 2: sin repeticiones innecesarias", "El 5: cierre que deje una idea", "Dice dos veces lo mismo sin agregar nada nuevo."),
        ("abc", "{F} ¿Cuál es la mejor reescritura de las dos oraciones repetidas?", "Los repartidores se organizaron en 2021 porque había muchos pedidos; al principio eran cinco.", "En 2021 se organizaron. Los repartidores se organizaron en 2021.", "Se organizaron porque se organizaron en 2021.", "Une las ideas sin repetir y agrega la causa."),
        ("ab", "{F} ¿Qué cierre cumple el criterio 5?", "Hoy diez repartidores se turnan los días para seguir llevando compras a personas mayores.", "Fin.", "El cierre debe dejar una idea y no solo marcar un final."),
        ("abc", "{F} ¿Qué expresión conecta bien «Al principio eran cinco» con «Hoy son diez»?", "Con el tiempo", "Aunque", "Porque", "Muestra un cambio a lo largo del tiempo."),
        ("ab", "{F} ¿Por qué el título es coherente con el contenido?", "Porque el texto trata de repartidores del barrio y su organización", "Porque es corto", "El título anuncia el tema real del texto."),
        ("ab", "Alguien dice que borrar la oración sobre el mercado «quita información». ¿Qué respondes?", "Si no se relaciona con el tema, quitarla mejora la coherencia", "Tiene razón: toda información debe quedarse aunque no se relacione", "Un dato ajeno dispersa al lector."),
        ("abc", "{F} ¿Qué orden conviene para el desarrollo?", "Origen en 2021, tamaño inicial, crecimiento a diez y voz de Hugo", "Voz de Hugo, mercado, 2021 y diez", "Diez, 2021, mercado y cinco", "Va del origen al presente y luego a la voz."),
        ("=", "{F} Hay tres oraciones con problemas (una repetida, una ajena y una contradictoria) entre las seis oraciones del texto, sin contar la voz de Hugo. Si se corrigen o quitan, ¿cuántas oraciones quedan sin problemas?", "6 - 3", "Se restan las tres oraciones con problemas del total de seis.", "oraciones"),
        ("abc", "{F} ¿Qué paso siguiente es mejor?", "Reescribir quitando o corrigiendo esas oraciones, reordenar y mejorar el cierre", "Agregar más datos sin revisar", "Entregar sin cambios", "La mejora se logra atendiendo cada criterio que falló."),
    ],
    ctx=("abc", "Escribiste un reportaje para el boletín de tu comunidad y otra persona lo revisa. ¿Qué le pides?", "Que lo lea con los cinco criterios y marque las oraciones que no cumplen", "Que lo apruebe sin leerlo", "Que lo reescriba por completo", "Una revisión con criterios señala dónde mejorar."),
    sc=[("En Lengua y Literatura: ¿qué es una contradicción en un texto?", "Una oración que niega lo que dice otra", "No pueden ser verdaderas las dos."),
        ("En Lengua y Literatura: ¿qué haces con un dato ajeno?", "Lo quito o lo relaciono con el tema", "Rompe la coherencia, porque no se relaciona con el tema."),
        ("En Lengua y Literatura: ¿qué cinco aspectos revisas en la coherencia de un reportaje?", "Tema, repeticiones, contradicciones, orden con conectores y cierre", "Son los cinco criterios de la lista.")],
    op=("{F} Con los cinco criterios, escribe en tu cuaderno qué oraciones del reportaje incumplen cada criterio. Luego reescribe el reportaje en un texto de siete a ocho líneas con título, bajada, desarrollo y un cierre nuevo. Usa solo los datos del texto (2021, cinco, diez, la voz de Hugo).",
        "Criterio 1: «El mercado central es muy antiguo». Criterio 2: oración repetida de 2021. Criterio 3: «Nadie quiere repartir y todos reparten». Reescritura: Los repartidores se organizaron en 2021 porque había muchos pedidos; al principio eran cinco y con el tiempo son diez. «Nos turnamos los días», dice Hugo (voz de ejemplo).",
        ["identifica oraciones que incumplen criterios", "reescribe sin contradicciones ni repeticiones", "agrega un cierre que deje una idea"],
        ["lista de oraciones con problemas y reportaje reescrito de siete a ocho líneas"],
        ["agregar datos nuevos", "mantener el cierre «Fin»"],
        "Pregunta de revisión: «¿Puede alguien que no conoce el tema entender el reportaje de principio a fin?»."),
    reinforce="Revisa un mensaje largo que hayas enviado: marca una repetición y una frase que sobraba.",
    extend="Pide a otra persona que revise tu reportaje con los cinco criterios y anota dos cambios que harías.",
)
