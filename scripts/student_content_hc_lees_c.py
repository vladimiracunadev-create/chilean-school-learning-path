"""Lectura y escritura especializadas (electivo 3.º y 4.º medio HC): OAC-05 (buscar, evaluar y seleccionar fuentes impresas y digitales, clases 1 a 5)."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz y cuaderno (o un procesador de texto, si lo tienes). Todas las fuentes, fichas, resultados de búsqueda y tablas de los ejercicios están escritos en el enunciado y son originales y de ejemplo: no necesitas internet ni libros. "
             "Si más adelante buscas fuentes reales, usa los criterios de esta unidad y no compartas datos personales en sitios que no conoces ni descargues archivos de origen dudoso.")
build = make_build(MATERIALS)

O5 = "LL-LEES-3y4-OAC-05"

# ============================================================ OAC-05, clase 1
F = ("Ficha 1 (fuentes de ejemplo sobre el sueño de estudiantes). "
     "S1: informe de un equipo de investigación de una universidad de ejemplo, con datos propios de 200 estudiantes, publicado en línea. "
     "S2: capítulo de un libro de texto que explica con palabras propias los resultados de varios estudios. "
     "S3: entrevista grabada de un orientador del liceo, publicada en el sitio del liceo. "
     "S4: nota de opinión de un diario de ejemplo que defiende un horario escolar más tardío. "
     "S5: informe de datos de un organismo público de ejemplo, con tablas de una encuesta nacional.")
build(
    O5, 1, F,
    use="Aprenderé a distinguir tipos de fuentes (primarias y secundarias; académicas, de divulgación, de opinión e institucionales) y soportes (impreso y digital). Sirve para saber qué puede aportar cada fuente a mi texto.",
    prior=["Sé qué es una fuente y por qué se atribuye.", "Sé distinguir un dato de una opinión.", "Sé leer un texto de divulgación."],
    explain=[
        "Una fuente primaria entrega información de primera mano: datos propios de un estudio, un documento original, una entrevista o un informe que presenta una encuesta. Una fuente secundaria analiza, resume o explica fuentes primarias: un libro de texto, un artículo de divulgación, una reseña. Ninguna es mejor en todo: la primaria ofrece los datos originales y la secundaria ayuda a entender el panorama.",
        "También se distinguen por propósito y autoría. Una fuente académica, escrita por especialistas y con referencias, busca generar o comunicar conocimiento. Una fuente institucional, como un organismo público, entrega datos oficiales. La divulgación explica a un público general. La opinión defiende una postura y no pretende ser neutral. Cada tipo sirve para algo distinto: la opinión puede dar argumentos, pero no sirve como dato.",
        "El soporte puede ser impreso, como libros y revistas, o digital, como sitios, bases de datos y archivos. Lo digital cambia con el tiempo y exige anotar la dirección y la fecha de consulta; lo impreso se cita con la página. Clasificar una fuente antes de usarla permite decidir qué rol cumplirá: dato, explicación, contexto o postura.",
    ],
    vocab=[("fuente primaria", "información de primera mano, como datos propios o documentos originales"), ("fuente secundaria", "análisis o resumen de fuentes primarias"), ("fuente académica", "escrita por especialistas, con referencias y método"), ("fuente institucional", "producida por un organismo con datos oficiales"), ("soporte", "medio de la fuente: impreso o digital")],
    worked=[
        ("Clasificar una fuente", "Un informe que presenta los resultados de una encuesta aplicada por sus propios autores. ¿Primaria o secundaria?",
         ["Los autores obtuvieron los datos directamente.", "Se trata de información de primera mano."],
         "Primaria"),
        ("Asignar un rol", "Una nota de opinión que defiende un cambio de horario. ¿Sirve como dato o como postura?",
         ["Defiende una postura y no presenta datos propios.", "Puede dar argumentos, pero no es evidencia empírica."],
         "Sirve como postura, no como dato"),
    ],
    mistakes=[("Pensar que una fuente secundaria nunca sirve.", "Ayuda a comprender y a ubicar el tema.", "Úsala para contexto y compara con fuentes primarias."),
              ("Usar una nota de opinión como si fuera un dato.", "La opinión defiende una postura; no demuestra nada por sí sola.", "Úsala como postura y busca datos que la respalden.")],
    T=[
        ("abc", "{F} ¿Cuál es una fuente primaria porque presenta datos propios?", "S1", "S2", "S4", "S1 contiene datos obtenidos directamente de 200 estudiantes."),
        ("abc", "{F} ¿Cuál es una fuente secundaria porque explica estudios de otros?", "S2", "S1", "S5", "S2 explica con palabras propias resultados de varios estudios."),
        ("ab", "En Lengua: ¿qué es una fuente primaria?", "Una fuente que entrega información de primera mano", "Una fuente que resume otras fuentes", "Los datos propios o documentos originales son fuentes primarias."),
        ("abc", "{F} ¿Cuál es una fuente de opinión?", "S4", "S5", "S1", "S4 defiende una postura sobre el horario sin pretender ser neutral."),
        ("abc", "{F} ¿Cuál es una fuente institucional con datos oficiales?", "S5", "S3", "S4", "S5 viene de un organismo público y presenta tablas de una encuesta nacional."),
        ("abc", "{F} Para un informe que necesita datos originales de estudiantes, ¿qué fuentes conviene priorizar?", "S1 y S5", "S4 y S2", "Solo S4", "S1 y S5 entregan datos; S4 es opinión y S2 es explicación."),
        ("abc", "{F} ¿Qué rol puede cumplir S4 en un ensayo?", "Presentar una postura con la que dialogar", "Ser el dato central", "Reemplazar a S1", "S4 aporta argumentos de un autor, no datos propios."),
        ("ab", "{F} ¿Por qué S3 puede ser primaria?", "Es el testimonio directo de un orientador", "Porque está publicada en un sitio web", "La entrevista recoge la voz directa de quien conoce la situación, aunque es un solo testimonio."),
        ("abc", "{F} ¿Qué soporte tienen S1 y S3, según la ficha?", "Digital", "Impreso", "Ambos", "La ficha dice que S1 está publicada en línea y S3 en el sitio del liceo."),
        ("abc", "Un estudiante cita la nota de opinión S4 como «dato» de que el horario tardío mejora el rendimiento. ¿Qué error comete?", "Usa una opinión como si fuera evidencia empírica", "Cita demasiadas fuentes", "Usa una fuente digital", "Una opinión no prueba un hecho; hace falta evidencia que la respalde."),
        ("abc", "{F} Si el estudiante quiere comprender el panorama general antes de buscar datos, ¿por dónde conviene empezar?", "Por S2, una fuente secundaria que ordena los estudios", "Por S4", "Por S5 sin leer nada más", "Una fuente secundaria da contexto y términos para luego buscar datos."),
        ("abc", "{F} Para un informe sobre el sueño, el estudiante quiere contrastar los datos de S1 con otra fuente de datos de origen distinto. ¿Cuál conviene?", "S5, porque es un organismo público con su propia encuesta", "S4, porque defiende una postura", "S2, porque repite estudios de otros", "S5 aporta datos oficiales independientes de S1; S4 es opinión y S2 es explicación de estudios ajenos."),
        ("abc", "{F} Un estudiante clasifica S5 como secundaria porque «tiene tablas». ¿Cuál es el error?", "La tabla presenta datos obtenidos por el propio organismo en su encuesta", "Las tablas siempre son secundarias", "Las tablas no son datos", "Las tablas son resultados originales de la encuesta del organismo."),
    ],
    ctx=("abc", "Una estudiante busca información para un informe sobre el uso de bicicletas en su liceo y encuentra: un registro de ejemplo de cuántas bicicletas hay en el estacionamiento, una nota de opinión que pide más ciclovías y un libro que resume estudios sobre transporte. ¿Qué rol tiene cada una?", "Registro: dato primario; nota: postura; libro: contexto secundario", "Todas son datos primarios", "Todas son opiniones", "El registro es de primera mano, la nota defiende una postura y el libro explica estudios ajenos."),
    sc=[
        ("En Lengua: ¿qué diferencia hay entre una fuente primaria y una secundaria?", "La primaria es de primera mano; la secundaria analiza o resume otras", "Cada una cumple un rol distinto."),
        ("¿Una nota de opinión sirve como dato?", "No: sirve como postura", "Defiende una idea sin demostrarla con datos propios."),
        ("¿Qué se anota de una fuente digital además del autor?", "La dirección y la fecha de consulta", "Lo digital cambia con el tiempo."),
    ],
    op=("Estas cuatro fuentes son de ejemplo: (1) una encuesta del centro de estudiantes con 120 respuestas sobre el uso de la biblioteca, (2) un artículo de divulgación que explica por qué leer ayuda al estudio, (3) una columna de opinión que pide ampliar el horario de biblioteca, (4) un informe de un organismo público de ejemplo con tablas de uso de bibliotecas escolares. Clasifica cada una (primaria o secundaria; académica, divulgación, opinión o institucional) y escribe qué rol cumpliría en un informe.",
        "(1) Primaria; encuesta propia; dato del liceo. (2) Secundaria; divulgación; contexto. (3) Opinión; postura con la que dialogar. (4) Primaria; institucional; datos oficiales para comparar.",
        ["clasifica las cuatro fuentes con tipo y nivel", "asigna un rol coherente a cada una", "distingue dato de postura"],
        ["tabla de cuatro filas con tipo, nivel y rol"],
        ["tratar la opinión como dato", "confundir primaria y secundaria", "no asignar rol"],
        "Pregunta: «¿esta fuente aporta un dato, una explicación o una postura?»."),
    reinforce="Clasifica como primaria o secundaria: un diario de vida de ejemplo escrito por una persona que vivió un hecho y un libro que resume varios diarios.",
    extend="Explica por qué una investigación seria suele combinar fuentes primarias y secundarias.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 2 (búsqueda de ejemplo). Tema: relación entre horas de sueño y rendimiento escolar en estudiantes de enseñanza media. "
     "Consulta Q1: sueño. Consulta Q2: «horas de sueño» rendimiento escolar adolescentes. Consulta Q3: sueño NOT mascotas. Consulta Q4: sueño OR rendimiento. "
     "Resultados de ejemplo: Q1 12.000; Q2 340; Q3 11.000; Q4 20.000. Filtros disponibles: año de publicación y tipo de documento (informe, artículo, noticia).")
build(
    O5, 2, F,
    use="Aprenderé a buscar fuentes con palabras clave, frases entre comillas, operadores y filtros. Sirve para llegar a fuentes pertinentes sin perder tiempo en resultados irrelevantes.",
    prior=["Sé qué tipos de fuentes existen.", "Sé usar un buscador.", "Sé delimitar un tema con una pregunta."],
    explain=[
        "Buscar bien empieza antes de escribir en el buscador: se identifican las palabras clave del tema y sus sinónimos. Una consulta de una sola palabra, como «sueño», trae miles de resultados de todo tipo. Combinar palabras clave ayuda a acotar: «horas de sueño» rendimiento escolar adolescentes busca un tema más preciso.",
        "En muchos buscadores y bases de datos se pueden usar operadores. Las comillas buscan una frase exacta. AND (o escribir las palabras juntas) exige que aparezcan todas. OR admite que aparezca cualquiera y, por eso, amplía los resultados. NOT, o un signo menos, excluye una palabra. Los filtros por año y tipo de documento reducen los resultados a lo reciente o a un tipo de fuente. Cada buscador puede escribirlos distinto, de modo que conviene revisar su ayuda.",
        "La búsqueda es un proceso de ajuste: si hay demasiados resultados, se agregan términos o filtros; si hay muy pocos, se quitan términos o se usan sinónimos. Conviene registrar las consultas probadas y los resultados útiles. Que una fuente aparezca primero no significa que sea la mejor: el orden lo decide el buscador, no la calidad de la fuente.",
    ],
    vocab=[("palabra clave", "término central del tema que se usa para buscar"), ("operador", "símbolo o palabra que combina o excluye términos"), ("frase exacta", "búsqueda entre comillas, en el orden dado"), ("filtro", "opción que limita los resultados por año o tipo"), ("sinónimo", "palabra con significado parecido que amplía la búsqueda")],
    worked=[
        ("Acotar una consulta", "Una búsqueda con la palabra «agua» trae 50.000 resultados. ¿Cómo acotarla para un informe sobre el consumo de agua en liceos?",
         ["Se agregan términos que precisan el tema.", "Se pueden usar comillas para una frase clave."],
         "«consumo de agua» liceos"),
        ("Interpretar un operador", "La consulta tarea NOT recetas, ¿qué hace?",
         ["NOT excluye la palabra que sigue.", "Se busca «tarea» sin los documentos que mencionan «recetas»."],
         "Excluye los resultados que contengan «recetas»"),
    ],
    mistakes=[("Escribir el tema entero como una pregunta larga y esperar buenos resultados.", "Muchos buscadores funcionan mejor con palabras clave precisas.", "Extrae las palabras clave y combínalas."),
              ("Quedarse con los primeros resultados sin revisar.", "El orden depende del buscador, no de la calidad.", "Evalúa cada fuente aunque aparezca primero.")],
    T=[
        ("abc", "{F} ¿Qué consulta es la más acotada?", "Q2", "Q1", "Q4", "Q2 combina frase exacta y términos que precisan el tema."),
        ("ab", "En Lengua: ¿qué hace escribir una frase entre comillas en un buscador?", "Busca esa frase exacta en ese orden", "Excluye la frase", "Las comillas piden la frase exacta."),
        ("abc", "{F} ¿Qué consulta usa un operador de exclusión?", "Q3", "Q2", "Q4", "Q3 usa NOT para excluir «mascotas»."),
        ("abc", "{F} ¿Qué consulta usa OR y por eso amplía los resultados?", "Q4", "Q3", "Q2", "OR admite que aparezca cualquiera de los términos."),
        ("abc", "{F} Q4 trae 20.000 resultados y Q1 trae 12.000. ¿Por qué Q4 trae más?", "OR admite documentos que tengan «sueño» o «rendimiento», así que suma ambos grupos", "Porque exige que aparezcan todos los términos a la vez", "Porque el filtro de año amplía la búsqueda", "OR acepta cualquiera de los términos y por eso amplía; exigir todos los términos reduce los resultados."),
        ("abc", "{F} Q1 trae 12.000 resultados. ¿Cuál es una mejora razonable?", "Agregar términos como «rendimiento escolar» y adolescentes", "Buscar solo «sueño» otra vez", "Usar OR con más palabras generales", "Agregar términos precisos reduce los resultados y mejora la pertinencia."),
        ("ab", "{F} Un estudiante cree que Q4 es la mejor porque tiene más resultados. ¿Es correcto?", "No: más resultados no significa más pertinentes", "Sí: más resultados es mejor", "Q4 amplía con OR y trae lo relacionado con cualquiera de los dos términos, no lo que más se ajusta."),
        ("abc", "{F} El estudiante quiere solo fuentes recientes de tipo informe. ¿Qué debe hacer?", "Aplicar los filtros de año y de tipo de documento", "Agregar NOT noticia a la consulta", "Cambiar de tema", "Los filtros están disponibles para limitar por año y tipo."),
        ("abc", "{F} Q3 excluye «mascotas» pero trae 11.000 resultados. ¿Qué indica?", "Excluir una palabra no basta para acotar el tema", "Es la mejor consulta", "El tema ya está acotado", "Q3 sigue siendo muy amplia porque solo quita un tema ajeno."),
        ("abc", "Un estudiante busca «adolescente» y no encuentra nada útil. ¿Qué sinónimo puede probar?", "«joven» o «estudiante de enseñanza media»", "«niños de primaria»", "«adultos mayores»", "Un sinónimo del mismo campo puede traer fuentes que usan otro término."),
        ("abc", "{F} ¿Por qué conviene anotar las consultas probadas?", "Para no repetir búsquedas y comparar cuáles dieron mejores resultados", "Porque el buscador lo exige", "Para ocultar las fuentes", "Registrar el proceso permite ajustarlo con evidencia."),
        ("abc", "{F} Para el tema de la ficha, ¿qué secuencia de ajuste es más razonable?", "Partir de Q1, pasar a Q2 y luego aplicar los filtros de año y tipo", "Partir de Q3, pasar a Q4 y volver a Q1", "Partir de Q2 y quitarle todos los términos", "Se parte amplio, se precisan los términos y se filtra; las otras secuencias terminan en consultas más amplias."),
        ("abc", "{F} Si Q2 diera cero resultados, ¿qué ajuste es razonable?", "Quitar un término o probar sinónimos", "Agregar más términos específicos", "Agregar NOT", "Cuando hay muy pocos resultados se amplía la consulta."),
    ],
    ctx=("abc", "Un grupo busca fuentes sobre el reciclaje de papel en liceos. La consulta «reciclaje» trae 30.000 resultados. ¿Cuál es el mejor siguiente paso?", "Probar «reciclaje de papel» liceos y filtrar por informes recientes", "Seguir con «reciclaje»", "Cerrar el buscador", "Combinar términos y usar filtros acota la búsqueda."),
    sc=[
        ("En Lengua: ¿qué hacen las comillas en un buscador?", "Buscan la frase exacta", "Respetan el orden y las palabras."),
        ("¿Qué hace el operador OR?", "Amplía los resultados", "OR admite que aparezca cualquiera de los términos."),
        ("¿Aparecer primero garantiza calidad?", "No", "El orden lo decide el buscador."),
    ],
    op=("Tema: el uso del celular en clases. Escribe cuatro consultas distintas para un buscador, de la más amplia a la más precisa, e indica para cada una el operador o filtro que usarías. Agrega una breve explicación de por qué la última es la mejor.",
        "1. celular. 2. celular clases. 3. «uso del celular» clases adolescentes. 4. «uso del celular» clases adolescentes (filtro: informe, últimos años). La cuarta es la mejor porque usa frase exacta, términos precisos y filtros.",
        ["cuatro consultas ordenadas de amplia a precisa", "usa al menos dos operadores o filtros", "justifica la mejor"],
        ["lista de cuatro consultas y una explicación"],
        ["consultas casi iguales", "no usar operadores", "no justificar"],
        "Pregunta: «¿qué cambió entre una consulta y otra?»."),
    reinforce="Escribe una consulta con frase exacta y un término excluido sobre el tema «ahorro de agua en casas».",
    extend="Explica cómo cambiarías la búsqueda si encontraras demasiado pocos resultados.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 3 (cuatro fuentes de ejemplo sobre un suplemento llamado «EnergiPlus»). "
     "F1: informe de un equipo universitario de ejemplo, con nombre de sus autores, fecha de 2023, 18 referencias y la declaración de que no recibió dinero de empresas. "
     "F2: página de una empresa que vende EnergiPlus; sin autor ni fecha; afirma que «todos mejoran» y no tiene referencias. "
     "F3: nota de una periodista especializada de un diario de ejemplo, de 2022, que cita el informe de F1 con su enlace. "
     "F4: comentario anónimo en un foro, sin fecha, que dice «a mí me funcionó».")
build(
    O5, 3, F,
    use="Aprenderé a evaluar la autoría y la responsabilidad de una fuente: quién la escribe, quién responde por ella, desde qué institución y con qué intereses. Sirve para decidir en qué fuentes confiar.",
    prior=["Sé clasificar una fuente por tipo y soporte.", "Sé buscar fuentes.", "Sé qué es un dato y qué es una opinión."],
    explain=[
        "La autoría responde a quién escribió la fuente. Una fuente con autores identificables, con nombre y especialidad, permite saber quién responde por lo que dice. Una fuente anónima o sin fecha dificulta verificarla. La responsabilidad se refiere a quién respalda la publicación: una universidad, un organismo público, un diario con editores o una empresa. Una institución con procesos de revisión suele ofrecer más garantías que una página personal sin controles.",
        "Hay que preguntarse por los intereses. Si la fuente vende un producto, puede exagerar sus beneficios: tiene un conflicto de interés. Una declaración de financiamiento ayuda a juzgar: una investigación que declara no tener dinero de empresas está menos expuesta a ese conflicto, aunque esto no la hace perfecta. También se mira si la fuente cita referencias que pueden verificarse, y si se identifica la fecha.",
        "Ningún criterio basta por sí solo. Una fuente con autor puede equivocarse, y una anónima puede ser cierta, pero no se puede comprobar. Por eso se combinan criterios y se prefieren las fuentes con autoría clara, responsabilidad institucional, referencias, fecha y bajo conflicto de interés. Un testimonio personal («a mí me funcionó») es una experiencia, no una prueba general.",
    ],
    vocab=[("autoría", "quién escribió la fuente y con qué especialidad"), ("responsabilidad", "quién respalda y responde por lo publicado"), ("conflicto de interés", "situación en que quien informa gana algo con lo que dice"), ("referencias", "fuentes que el texto cita y que pueden verificarse"), ("testimonio", "experiencia personal que no prueba una regla general")],
    worked=[
        ("Evaluar la autoría", "Una página sin autor ni fecha dice que un producto «cura todo». ¿Qué falla tiene respecto de la autoría?",
         ["No se sabe quién responde por lo dicho.", "No se puede verificar ni saber si está actualizada."],
         "Sin autoría ni fecha no se puede verificar quién responde"),
        ("Detectar un conflicto de interés", "La empresa que vende un suplemento publica un informe que dice que funciona. ¿Qué ocurre?",
         ["Gana dinero si el producto se vende.", "Tiene un conflicto de interés y su afirmación debe contrastarse con fuentes independientes."],
         "Hay conflicto de interés"),
    ],
    mistakes=[("Confiar en una fuente solo porque tiene muchos seguidores.", "La popularidad no es autoría ni responsabilidad.", "Pregunta quién escribe, quién respalda y con qué referencias."),
              ("Descartar una fuente solo por ser de una empresa sin revisar sus datos.", "Una fuente con conflicto de interés puede tener datos útiles, pero debe contrastarse.", "Úsala con cautela y compara con fuentes independientes.")],
    T=[
        ("abc", "{F} ¿Cuál fuente tiene autoría identificable y respaldo institucional?", "F1", "F2", "F4", "F1 tiene autores nombrados, una universidad y referencias."),
        ("abc", "{F} ¿Cuál fuente tiene un posible conflicto de interés?", "F2", "F1", "F3", "La empresa que vende el producto gana si se compra."),
        ("ab", "En Lengua: ¿qué es un conflicto de interés?", "Que quien informa gana algo con lo que dice", "Que dos autores discuten", "La ganancia de quien informa puede sesgar el contenido."),
        ("abc", "{F} ¿Qué falta en F4 para poder evaluarla?", "Autoría, fecha y respaldo", "Un título más llamativo", "Más comentarios de otras personas", "F4 es anónima y sin fecha, así que no se puede verificar."),
        ("abc", "{F} ¿Qué rasgo de F3 da confianza?", "Cita el informe F1 con su enlace", "Está en un diario", "Es corta", "Citar una fuente verificable permite comprobarla."),
        ("abc", "{F} ¿Por qué la afirmación «todos mejoran» de F2 es sospechosa?", "Es absoluta y no tiene referencias ni autoría", "Es muy corta", "Es de 2023", "Una generalización sin respaldo ni autoría no se puede verificar."),
        ("ab", "{F} ¿Qué tipo de información es F4?", "Un testimonio personal, que no prueba una regla general", "Un dato oficial", "«A mí me funcionó» es una experiencia individual."),
        ("abc", "{F} ¿Qué dos fuentes conviene priorizar para un informe sobre el suplemento?", "F1 y F3", "F2 y F4", "F2 y F3", "F1 y F3 tienen autoría, fecha y referencias; F2 y F4 no."),
        ("abc", "{F} F3 cita el informe F1. ¿F1 y F3 son dos pruebas independientes del mismo dato?", "No: F3 se apoya en F1 y no agrega datos propios", "Sí: son dos fuentes y por tanto dos pruebas", "Sí, porque F3 tiene una fecha distinta", "Una fuente que repite a otra no aporta evidencia independiente."),
        ("abc", "{F} La periodista de F3 trabaja en un diario con editores. ¿Qué responsabilidad aporta esto?", "Hay un medio que respalda y revisa la publicación", "El diario garantiza que todo es cierto", "No aporta nada", "Un medio con procesos editoriales ofrece más control que un anónimo, aunque no garantiza que todo sea cierto."),
        ("abc", "{F} Un estudiante cita F2 como evidencia principal porque «es la única que tiene el nombre del producto». ¿Qué conviene responderle?", "Que una página que vende el producto no es una fuente independiente y se debe contrastar", "Que está bien", "Que debe usar F4 en su lugar", "Una fuente con interés comercial necesita verificación externa."),
        ("abc", "{F} F1 declara que no recibió dinero de empresas. ¿Qué implica eso?", "Está menos expuesta a un conflicto de interés, pero no por eso es perfecta", "Que sus resultados son necesariamente verdaderos", "Que no necesita referencias", "La declaración de financiamiento ayuda a juzgar, pero no reemplaza los demás criterios."),
        ("abc", "{F} Si F1 hubiera sido pagada por la empresa del suplemento, ¿qué cambiaría?", "Habría conflicto de interés y se debería contrastar con otras fuentes", "Nada", "Sería una fuente anónima", "El financiamiento por quien vende el producto afecta la independencia."),
    ],
    ctx=("abc", "Un grupo encuentra un video que afirma que cierta marca de zapatillas mejora el rendimiento. El video lo publica la propia marca, sin referencias. ¿Qué conviene hacer?", "Buscar un estudio independiente con autores identificables antes de usar la afirmación", "Citar el video como evidencia principal", "Copiar el video", "El video tiene conflicto de interés y no tiene referencias."),
    sc=[
        ("En Lengua: ¿qué dos preguntas básicas evalúan la autoría y la responsabilidad?", "Quién escribe y quién respalda lo publicado", "Autoría y responsabilidad se evalúan con esas preguntas."),
        ("¿Qué es un testimonio personal?", "Una experiencia individual que no prueba una regla general", "Una experiencia aislada no sustituye a un estudio con datos."),
        ("¿Qué ayuda a verificar una fuente?", "Referencias que se puedan comprobar", "Las referencias permiten seguir el rastro de los datos."),
    ],
    op=("Tienes tres fuentes de ejemplo sobre un programa de huertos escolares: (1) un informe de un equipo universitario, con autores, fecha y referencias; (2) una publicación anónima en una red social, sin fecha; (3) un folleto del fabricante de semillas, que afirma que «todos los huertos prosperan». Para cada una escribe: autoría, responsabilidad, posible conflicto de interés y si la usarías como evidencia principal.",
        "(1) Autoría clara, universidad respalda, sin conflicto evidente; sí. (2) Autoría anónima, sin respaldo; no. (3) Autoría de la empresa, interés comercial, afirmación absoluta; solo con contraste.",
        ["analiza autoría y responsabilidad de cada fuente", "identifica el conflicto de interés", "decide con razón si es evidencia principal"],
        ["tabla de tres filas"],
        ["confiar en la fuente más llamativa", "no ver el interés comercial", "decidir sin razón"],
        "Pregunta: «¿quién gana si creo esta fuente?»."),
    reinforce="Escribe dos preguntas que harías sobre autoría y dos sobre responsabilidad ante una página desconocida.",
    extend="Explica por qué una fuente con conflicto de interés puede igualmente tener datos útiles si se contrasta.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 4 (afirmación y fuentes de ejemplo). Afirmación: «Este año se duplicó la cantidad de estudiantes que llega en bicicleta al liceo». "
     "Fuente A (registro del liceo): año pasado, 10 estudiantes; este año, 14. "
     "Fuente B (comunicado de un club de ciclismo): «Se duplicó el uso de la bicicleta», sin datos ni fecha. "
     "Fuente C (encuesta del centro de estudiantes, 40 respuestas, fecha 12 de abril de ejemplo): 14 de 40 llegan en bicicleta este año. "
     "Fuente D (publicación sin autor): imagen de un estacionamiento lleno, sin lugar ni fecha.")
build(
    O5, 4, F,
    use="Aprenderé a evaluar la validez y veracidad de la información: contrastar datos entre fuentes, revisar la fecha y la evidencia, y detectar señales de desinformación. Sirve para no repetir como cierto algo que no está comprobado.",
    prior=["Sé evaluar la autoría y la responsabilidad.", "Sé calcular razones simples.", "Sé qué es una evidencia."],
    explain=[
        "La validez se refiere a si la información está bien respaldada: se obtuvo con un método adecuado, tiene datos verificables y las conclusiones se siguen de ellos. La veracidad se refiere a si lo que dice corresponde a los hechos. Para evaluarlas se contrastan varias fuentes independientes: si dos fuentes confiables coinciden en un dato, la confianza aumenta; si solo una lo dice, o si se contradicen, hace falta indagar más.",
        "Algunas señales de alerta: una afirmación absoluta sin datos («se duplicó»), una imagen sin lugar ni fecha, un titular alarmista, la ausencia de autor, una cifra que no coincide con las demás fuentes o un lenguaje que busca emocionar más que informar. Una cifra puede estar correcta pero mal interpretada: por ejemplo, pasar de 10 a 14 es un aumento, pero no una duplicación (que exigiría llegar a 20).",
        "Contrastar no es votar por mayoría: cinco fuentes que repiten un mismo comunicado no son cinco evidencias independientes. Importa que las fuentes tengan origen distinto y que los datos puedan comprobarse. Cuando no se puede confirmar una afirmación, lo honesto es decir que no está confirmada y no darla por cierta.",
    ],
    vocab=[("validez", "grado en que la información está bien respaldada por un método y datos"), ("veracidad", "coincidencia de lo dicho con los hechos"), ("contrastar", "comparar fuentes independientes sobre un mismo dato"), ("desinformación", "información falsa o engañosa difundida como cierta"), ("señal de alerta", "rasgo que invita a verificar antes de creer")],
    worked=[
        ("Verificar con un cálculo", "Una fuente dice que algo se duplicó de 10 a 14. ¿Se duplicó?",
         ["Duplicar 10 da 20.", "El valor 14 es menor que 20."],
         "No: aumentó, pero no se duplicó"),
        ("Contrastar fuentes", "Dos fuentes independientes dan 14 de 40 y 14 estudiantes. ¿Qué indica?",
         ["Los datos coinciden en el valor 14.", "Que fuentes independientes coincidan aumenta la confianza."],
         "Aumenta la confianza en el dato"),
    ],
    mistakes=[("Creer una afirmación porque se repite en muchos sitios.", "Muchos sitios pueden repetir la misma fuente original.", "Busca fuentes de origen distinto."),
              ("Aceptar una imagen sin lugar ni fecha como prueba.", "No se sabe si es del hecho que se afirma.", "Busca su origen o no la uses como evidencia.")],
    T=[
        ("abc", "{F} ¿Cuál fuente entrega datos de los dos años?", "La fuente A", "La fuente B", "La fuente D", "La fuente A dice 10 el año pasado y 14 este año."),
        ("=", "Un registro de otro liceo (de ejemplo) cuenta 15 estudiantes en bicicleta el año pasado. ¿Cuántos tendrían que llegar este año para afirmar que la cantidad se duplicó?", "15*2", "Duplicar es multiplicar por 2 la cantidad del año pasado.", " estudiantes"),
        ("abc", "{F} Con los datos de A, ¿la afirmación «se duplicó» es correcta?", "No: de 10 a 14 hay aumento, pero no duplicación", "Sí: 14 es más del doble de 10", "No se puede saber", "Duplicar 10 es 20, y 14 no llega a 20."),
        ("=", "{F} Según la fuente A, ¿en qué porcentaje aumentó la cantidad de estudiantes que llegan en bicicleta? Calcula (14 − 10) dividido por 10 y multiplicado por 100.", "(14-10)/10*100", "El aumento de 4 estudiantes sobre una base de 10 es de 40 de cada 100; una duplicación sería un aumento de 100 %.", " %"),
        ("ab", "En Lengua: ¿qué es contrastar fuentes?", "Comparar fuentes independientes sobre un mismo dato", "Copiar lo que dice la primera", "Contrastar permite ver si coinciden y con qué respaldo."),
        ("abc", "{F} ¿Qué dos fuentes coinciden en la cifra de este año?", "A y C", "B y D", "A y B", "Ambas indican 14 estudiantes este año."),
        ("abc", "{F} ¿Qué señal de alerta tiene la fuente B?", "Afirma una duplicación sin datos ni fecha", "Cita un registro", "Tiene fecha precisa", "Una afirmación absoluta sin datos no se puede comprobar."),
        ("abc", "{F} ¿Por qué la fuente D no sirve como prueba?", "No indica lugar ni fecha de la imagen", "Porque las imágenes nunca sirven como evidencia", "Porque no muestra a los estudiantes llegando", "Sin lugar ni fecha no se sabe si corresponde al hecho."),
        ("ab", "{F} Un estudiante dice: «Como A, B y C hablan del tema, hay tres pruebas de duplicación». ¿Qué falla?", "Solo A da datos de ambos años y muestra un aumento, no una duplicación; B no tiene datos y C solo informa este año", "Nada, hay tres pruebas", "B no tiene datos ni fecha y C no compara años, así que no hay tres pruebas de duplicación."),
        ("abc", "{F} ¿Cuál es una conclusión honesta con la evidencia?", "El uso de la bicicleta aumentó de 10 a 14 estudiantes, pero no se duplicó", "El uso se duplicó, según B", "Nadie llega en bicicleta", "Se ajusta a los datos verificables de A y C."),
        ("=", "{F} Según C, ¿qué porcentaje de los 40 estudiantes que respondieron llega en bicicleta? Calcula 14 dividido por 40 y multiplicado por 100.", "14/40*100", "Se divide la cantidad entre el total de respuestas y se multiplica por 100.", " %"),
        ("abc", "{F} Un titular dice «¡La bicicleta desplaza al auto en el liceo!». ¿Qué señal de alerta presenta?", "Lenguaje que busca emocionar más que informar, sin datos", "Cita su fuente", "Es un titular objetivo", "El titular alarmista no entrega datos que lo respalden."),
        ("abc", "{F} Si dos nuevas fuentes repiten el comunicado de B sin datos propios, ¿qué efecto tienen?", "No agregan evidencia independiente", "Duplican la evidencia", "Prueban que se duplicó", "Repetir lo mismo no es contrastar con datos propios."),
    ],
    ctx=("abc", "Un grupo lee: «El 90 % de los estudiantes del país ahorra agua en casa». No hay autor, fecha ni método. ¿Qué conviene hacer?", "Buscar la fuente original y compararla con otra independiente antes de usarla", "Usarla como dato central", "Compartirla en redes", "Una cifra sin método ni fecha debe verificarse antes."),
    sc=[
        ("En Lengua: ¿qué es la desinformación?", "Información falsa o engañosa difundida como cierta", "Se debe verificar antes de aceptarla."),
        ("¿Qué aumenta la confianza en un dato?", "Que fuentes independientes lo confirmen", "La coincidencia entre fuentes distintas lo respalda."),
        ("¿Cinco sitios que repiten un comunicado son cinco evidencias?", "No: provienen de la misma fuente", "Repetir una misma fuente no es contrastar fuentes distintas."),
    ],
    op=("Afirmación de ejemplo: «El consumo de papel del liceo se redujo a la mitad este año». Fuentes de ejemplo: registro de compras (año pasado, 80 resmas; este año, 60 resmas), una publicación sin autor que dice «se redujo a la mitad» y un comunicado del centro de estudiantes con fecha que habla de una «gran baja». Evalúa la afirmación: escribe los cálculos, qué fuentes sirven, qué señales de alerta hay y una conclusión ajustada a la evidencia.",
        "La mitad de 80 son 40, y el registro dice 60, de modo que bajó 20 resmas (25 %) pero no a la mitad. La publicación sin autor no sirve; el comunicado habla de «gran baja» sin cifras. Conclusión: el consumo bajó 20 resmas, pero no se redujo a la mitad.",
        ["calcula la mitad y compara con el registro", "identifica señales de alerta en las otras fuentes", "conclusión ajustada a la evidencia"],
        ["cálculo, lista de señales y conclusión"],
        ["aceptar la afirmación sin calcular", "no ver las señales de alerta", "conclusión exagerada"],
        "Pregunta: «¿qué dato podrías comprobar tú mismo?»."),
    reinforce="Revisa esta afirmación de ejemplo: «Se triplicó la asistencia a talleres: de 12 a 30 estudiantes». ¿Se triplicó?",
    extend="Explica por qué una cifra correcta puede llevar a una conclusión equivocada.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 5 (rúbrica y tres fuentes candidatas, de ejemplo). Tema del informe: el uso del celular en clases. "
     "Rúbrica: cinco criterios con 0, 1 o 2 puntos cada uno: relevancia, actualidad, autoría y responsabilidad, validez de los datos y propósito (neutral o comercial). "
     "Fuente X: relevancia 2, actualidad 2, autoría 2, validez 2, propósito 2. "
     "Fuente Y: relevancia 2, actualidad 1, autoría 1, validez 1, propósito 1. "
     "Fuente Z: relevancia 1, actualidad 0, autoría 0, validez 0, propósito 0.")
build(
    O5, 5, F,
    use="Aprenderé a seleccionar fuentes con una rúbrica de criterios, justificar mi decisión y atribuirlas con una referencia. Sirve para decidir qué fuentes usar en mi texto y cómo reconocerlas.",
    prior=["Sé clasificar, buscar y evaluar fuentes.", "Sé qué es una cita y una paráfrasis.", "Sé sumar puntajes."],
    explain=[
        "Seleccionar es decidir con criterios qué fuentes se usarán. Una rúbrica ayuda: se evalúa cada fuente en varios aspectos y se suman puntos. Los criterios típicos son la relevancia (¿responde a mi tema?), la actualidad (¿es lo bastante reciente?), la autoría y la responsabilidad (¿quién escribe y quién respalda?), la validez de los datos (¿tienen método y se pueden verificar?) y el propósito (¿informa o intenta vender o persuadir?).",
        "El puntaje orienta, pero no reemplaza el juicio. Una fuente con buen puntaje total puede fallar en un criterio decisivo, como la relevancia. Por eso se justifica la decisión por escrito: qué se eligió, por qué, y qué se descarta. También se acepta que a veces una fuente con puntaje medio se use con cautela, como contexto, si se declara su límite.",
        "Una vez seleccionadas, las fuentes se atribuyen. En el texto se usan citas o paráfrasis con autor y año, y al final se incluye una lista de referencias con los datos completos: autor, año, título, tipo de fuente, y para lo digital la dirección y la fecha de consulta. No atribuir, o atribuir mal, es plagio. Una lista de referencias bien hecha permite que otros comprueben el trabajo.",
    ],
    vocab=[("rúbrica", "tabla de criterios con puntajes para evaluar"), ("relevancia", "grado en que la fuente responde al tema"), ("actualidad", "qué tan reciente es la información"), ("lista de referencias", "lista final con los datos completos de las fuentes usadas"), ("atribuir", "reconocer de quién viene una idea o un dato")],
    worked=[
        ("Sumar una rúbrica", "Una fuente tiene relevancia 2, actualidad 1, autoría 2, validez 1 y propósito 2. ¿Cuántos puntos suma de 10?",
         ["Se suman 2 + 1 + 2 + 1 + 2.", "El total es 8."],
         "8 puntos"),
        ("Justificar una decisión", "La fuente Z de la ficha obtiene 1 punto en total. ¿Qué decisión se justifica?",
         ["Casi todos los criterios están en cero.", "No es confiable ni actual."],
         "Descartarla, porque no cumple los criterios mínimos"),
    ],
    mistakes=[("Elegir la fuente por ser la primera que aparece.", "El orden del buscador no mide calidad.", "Evalúa cada fuente con criterios y compara puntajes."),
              ("Poner solo el nombre del sitio como referencia.", "No permite encontrar ni verificar la fuente.", "Anota autor, año, título, tipo, dirección y fecha de consulta.")],
    T=[
        ("abc", "{F} ¿Qué criterio de la rúbrica pregunta si la fuente informa o intenta vender y persuadir?", "Propósito", "Relevancia", "Actualidad", "El propósito distingue entre una fuente neutral y una comercial."),
        ("=", "{F} ¿Cuántos puntos suma la fuente Y?", "2+1+1+1+1", "Se suman los puntajes de relevancia, actualidad, autoría, validez y propósito.", " puntos"),
        ("abc", "{F} ¿En qué criterio las fuentes X e Y obtienen el mismo puntaje?", "Relevancia", "Actualidad", "Validez", "Ambas tienen 2 en relevancia; en los demás criterios Y tiene menos que X."),
        ("abc", "{F} ¿Qué fuente conviene usar como evidencia principal?", "X", "Y", "Z", "X obtiene el puntaje máximo en todos los criterios."),
        ("abc", "{F} ¿Qué decisión se justifica para Z?", "Descartarla", "Usarla como evidencia principal", "Citarla sin verificarla", "Su puntaje casi nulo indica que no cumple los criterios mínimos."),
        ("ab", "{F} ¿Cómo conviene usar la fuente Y, con puntaje medio?", "Con cautela, como contexto y declarando sus límites", "Como prueba definitiva", "Un puntaje medio no es para evidencia principal pero puede aportar contexto."),
        ("ab", "En Lengua: ¿qué es una lista de referencias?", "La lista final con los datos completos de las fuentes usadas", "Un resumen del texto", "Permite encontrar y comprobar cada fuente citada."),
        ("abc", "¿Cuál es una referencia completa de una fuente digital de ejemplo?", "Díaz, A. (2023). El celular en clases. Informe de ejemplo. Dirección de ejemplo. Consultado el 5 de mayo de 2025", "Díaz, A. (2023). El celular en clases. Consultado el 5 de mayo de 2025", "Informe de ejemplo sobre el celular en clases, 2023, sin autor ni dirección", "La primera trae autor, año, título, tipo, dirección y fecha de consulta; las otras omiten datos."),
        ("abc", "{F} Una fuente tiene 9 puntos pero relevancia 0, porque trata otro tema. ¿Qué decisión es más razonable?", "No usarla, porque no responde al tema aunque tenga buen puntaje", "Usarla por su puntaje", "Citar una parte irrelevante", "La relevancia es indispensable: sin ella la fuente no sirve para el texto."),
        ("abc", "{F} Si el criterio de propósito fuera 0 en una fuente porque es publicidad de un producto, ¿qué corresponde?", "Contrastarla con fuentes independientes antes de usarla", "Citarla como evidencia sin más", "Descartarla sin leerla, aunque pueda tener datos útiles", "Un propósito comercial pide verificar con otras fuentes."),
        ("abc", "{F} Se agrega una fuente W con 8 puntos. Ordenadas de mayor a menor puntaje junto con X, Y y Z, ¿cuál queda en segundo lugar?", "W", "Y", "Z", "X tiene 10, W 8 e Y 6, de modo que W queda segunda."),
        ("abc", "Un estudiante parafrasea un dato de la fuente X y no la menciona. ¿Qué incumple?", "La atribución: debe indicar de dónde viene el dato", "La rúbrica", "La búsqueda", "Toda idea o dato ajeno se atribuye, aunque se parafrasee."),
        ("abc", "{F} Un estudiante dice: «Y tiene 6 de 10, así que es mala en todo». ¿Qué responde la rúbrica?", "Y es relevante (2 puntos), pero tiene límites en otros criterios; se usa con cautela", "Y es idéntica a Z", "El puntaje no sirve para decidir nada", "El detalle por criterio muestra en qué es sólida una fuente y en qué no."),
    ],
    ctx=("abc", "Un grupo evalúa dos fuentes para un informe sobre el reciclaje: la fuente 1 suma 9 puntos y la fuente 2 suma 4. ¿Qué decisión es razonable?", "Usar la 1 como evidencia principal y la 2 solo como contexto con cautela o descartarla", "Usar ambas como evidencia principal", "Descartar la 1", "El puntaje orienta, y la 1 es más confiable."),
    sc=[
        ("En Lengua: ¿qué criterios tiene una rúbrica de selección de fuentes?", "Relevancia, actualidad, autoría, validez y propósito", "Cubren qué dice, cuándo, quién, con qué respaldo y para qué."),
        ("¿Qué se hace después de seleccionar las fuentes?", "Se atribuyen en el texto y en la lista de referencias", "Toda fuente usada debe reconocerse en el texto y la lista."),
        ("=", "Una fuente suma 2, 1, 2, 2 y 1 en los cinco criterios. ¿Cuánto suma?", "2+1+2+2+1", "Se suman los cinco puntajes."),
    ],
    op=("Elige el tema «ahorro de energía en el liceo». Describe tres fuentes de ejemplo (por ejemplo, un informe universitario, una nota de opinión y un folleto de una empresa), evalúalas con la rúbrica de cinco criterios (0, 1 o 2 puntos), suma sus puntos, decide cuáles usarás y por qué, y escribe una referencia completa de la mejor fuente.",
        "Informe universitario: 2, 2, 2, 2, 2 = 10. Nota de opinión: 2, 2, 1, 0, 1 = 6. Folleto de empresa: 1, 1, 0, 0, 0 = 2. Uso el informe como evidencia principal, la nota como postura y descarto el folleto. Referencia: Rojas, M. (2023). Ahorro de energía en liceos. Informe de ejemplo. Dirección de ejemplo. Consultado el 5 de mayo de 2025.",
        ["evalúa tres fuentes con los cinco criterios y suma bien", "decide con razón qué usar y qué descartar", "escribe una referencia completa"],
        ["tabla de puntajes, decisión y referencia"],
        ["sumar mal", "decidir sin razón", "referencia incompleta"],
        "Pregunta: «¿qué criterio fue decisivo en tu decisión?»."),
    reinforce="Evalúa con la rúbrica de la ficha una fuente de ejemplo con relevancia 2, actualidad 2, autoría 1, validez 2 y propósito 1, y decide cómo usarla.",
    extend="Explica por qué dos fuentes con el mismo puntaje pueden usarse de manera distinta en un texto.",
)
