"""Filosofía EPJA Media N1 y N2, módulo 3, OAD-12: participar en un diálogo y compartir visiones personales sobre una controversia contemporánea (uso de inteligencia artificial en el trabajo y privacidad de datos), basados en perspectivas filosóficas. Casos originales y neutrales; todo en papel."""
from __future__ import annotations

from epja_filo_c_common import K

O = "EPJA-FILO-NM1y2-OAD-12"

# ====================================================== clase 1
F = ("Ficha 1 (caso de ejemplo, cifras inventadas). Una empresa ficticia de atención a clientes incorporó un programa de inteligencia artificial que redacta respuestas. "
     "El tiempo medio de respuesta bajó de 10 a 4 minutos. Algunas personas del equipo temen que su trabajo cambie. "
     "Posición P1: usar el programa con libertad, porque aumenta la rapidez. "
     "Posición P2: usarlo con aviso al cliente y revisión de una persona, porque las respuestas deben ser confiables y alguien debe responder por ellas. "
     "Posición P3: no usarlo en tareas que cuidan a personas, porque ahí importa la relación humana. "
     "Controversia: pregunta sobre la que personas razonables discrepan, porque dan peso distinto a valores como eficiencia, confianza, cuidado y justicia.")
K(O, 1, F,
  "Hoy aprenderé a reconocer una controversia contemporánea, a separar hechos de valores en ella y a leer sus posiciones con perspectivas filosóficas.",
  ["Una controversia es una pregunta sobre la que personas razonables discrepan, porque dan distinto peso a valores. El uso de la inteligencia artificial en el trabajo es un ejemplo: se discute qué se gana, qué se arriesga y quién responde. En una controversia no se parte de que una persona tiene razón y la otra no: se parte de entender las razones de cada posición.",
   "Para ordenarla se separan hechos y valores. Un hecho se puede comprobar: en la ficha, que el tiempo bajó de 10 a 4 minutos. Un valor es lo que se considera importante: la rapidez, la confianza, el cuidado de las personas, la justicia en el trabajo. Muchas discusiones se enredan porque una persona habla de hechos y otra de valores sin darse cuenta. Los datos de la ficha son inventados.",
   "Las perspectivas éticas ayudan a leer cada posición. El utilitarismo preguntaría por el balance de beneficios y perjuicios para todas las personas afectadas. La deontología preguntaría qué deberes están en juego, como informar con verdad y responder por lo que se hace. La ética de las virtudes preguntaría qué haría una empresa justa, prudente y atenta a las personas. Ninguna decide sola: aportan preguntas para conversar mejor."],
  [("controversia", "pregunta sobre la que personas razonables discrepan por dar distinto peso a valores"), ("hecho", "afirmación que se puede comprobar"), ("valor", "aquello que se considera importante o digno de buscar"), ("responsabilidad", "capacidad de responder por lo que se hace")],
  [("Hecho o valor", "En otro caso de ejemplo se dice: «las respuestas hechas con un programa deberían llevar siempre un aviso». ¿Es un hecho o una valoración?", ["No describe lo que ocurre, dice cómo debería ser.", "No se comprueba con un registro."], "Una valoración"),
   ("Valor de una posición", "{F} ¿Qué valor defiende sobre todo P2 al pedir aviso y revisión?", ["Busca que las respuestas sean confiables.", "También que alguien responda por ellas."], "La confianza y la responsabilidad")],
  [("Creer que en una controversia una posición es obvia y la otra absurda.", "Se omite el valor que defiende cada una.", "Busca el valor y la razón de cada posición antes de evaluar."),
   ("Mezclar un hecho con una valoración como si fueran lo mismo.", "Se pasa de lo que ocurre a lo que debería ocurrir sin avisar.", "Separa lo comprobable de lo valorativo.")],
  [("abc", "En Filosofía: ¿qué es una controversia?", "Una pregunta sobre la que personas razonables discrepan por dar distinto peso a valores", "Una pelea entre personas que no se respetan", "Una pregunta con una respuesta que se busca en un registro", "Las discrepancias vienen de valores pesados de modo distinto."),
   ("ab", "En una controversia conviene partir", "entendiendo las razones de cada posición", "decidiendo quién tiene razón", "Entender primero permite evaluar con fundamento."),
   ("abc", "{F} ¿Cuál de estas afirmaciones es un hecho?", "El tiempo medio de respuesta bajó de 10 a 4 minutos", "Usar el programa es injusto con el equipo", "La relación humana vale más que la rapidez", "Solo la primera se puede comprobar con registros."),
   ("=", "{F} ¿Cuántos minutos bajó el tiempo medio de respuesta?", "10-4", "Se resta el tiempo nuevo al tiempo anterior.", " minutos"),
   ("abc", "{F} ¿Qué valor defiende sobre todo P1?", "La rapidez", "El cuidado de las personas", "La revisión humana", "P1 se apoya en que aumenta la rapidez."),
   ("abc", "{F} ¿Qué valor defiende sobre todo P3?", "La relación humana en tareas de cuidado", "La rapidez de respuesta", "El ahorro de costos", "P3 limita el uso donde importa el cuidado entre personas."),
   ("abc", "{F} ¿Qué pregunta haría el utilitarismo ante el caso?", "¿Qué balance de beneficios y perjuicios hay para todas las personas afectadas?", "¿Qué haría una persona de buen carácter?", "¿Qué deber se infringe en cada caso?", "Mira el balance de consecuencias para todas las personas afectadas."),
   ("abc", "{F} ¿Qué deber destaca la deontología en la posición P2?", "Informar con verdad y responder por lo que se hace", "Obtener la mayor rapidez posible", "Evitar toda conversación", "El aviso y la revisión humana expresan esos deberes."),
   ("abc", "Una persona dice: «Es obvio que P1 es correcta, porque la rapidez siempre es lo mejor». ¿Qué le falta?", "Considerar otros valores en juego, como confianza y cuidado", "Más datos de rapidez", "Atacar a quienes piensan distinto", "Afirmar que un valor siempre gana no responde a los otros."),
   ("abc", "Otra persona dice: «P3 está equivocada porque quienes la defienden temen al cambio». ¿Qué falacia es?", "Ad hominem", "Falso dilema", "Pendiente resbaladiza", "Atribuye un motivo a las personas en vez de examinar su razón."),
   ("abc", "Alguien dice: «O se usa la inteligencia artificial para todo, o no se usa para nada». ¿Qué falacia es?", "Falso dilema", "Apelación a la mayoría", "Ad hominem", "Presenta solo dos opciones aunque hay posiciones intermedias, como P2."),
   ("abc", "{F} ¿Por qué podría una persona razonable apoyar P2 aunque valore la rapidez?", "Porque valora también la confianza y la responsabilidad", "Porque no entiende el programa", "Porque quiere perjudicar a la empresa", "Puede pesar más la confianza sin negar la rapidez."),
   ("ab", "¿Puede alguien comprender bien las razones de P3 y aun así preferir P2?", "Sí: entender una posición no obliga a compartirla", "No: entender obliga a compartir", "Se puede comprender una razón y dar mayor peso a otra.")],
  ("abc", "En un taller ficticio, un compañero dice que usará un programa que redacta cotizaciones, pero revisará cada una antes de enviarla. ¿Qué posición del caso se parece más a la suya?", "P2, uso con revisión humana", "P1, uso libre sin revisión", "P3, no usarlo", "Usa el programa pero conserva la responsabilidad de revisar."),
  [("En Filosofía: ¿qué es una controversia?", "Una pregunta sobre la que personas razonables discrepan", "Surge porque las personas dan distinto peso a los valores."),
   ("¿Qué distingue un hecho de un valor?", "El hecho se comprueba; el valor expresa lo que importa", "Separarlos ordena la conversación y evita confusiones entre datos y valoraciones."),
   ("¿Detectar un ad hominem prueba que la conclusión es falsa?", "No: solo muestra que esa razón no la apoya", "La conclusión podría tener otras razones que sí la apoyen.")],
  ("{F} Escribe (a) dos hechos y dos valores del caso, (b) el valor que defiende cada posición P1, P2 y P3, (c) una pregunta que le harías a alguien que piensa distinto y (d) tu postura personal, con dos razones, una perspectiva ética usada y una razón del otro lado que te parezca fuerte.",
   "(a) Hechos: el tiempo bajó de 10 a 4 minutos; hay temor en el equipo. Valores: rapidez; confianza. (b) P1 rapidez; P2 confianza y responsabilidad; P3 cuidado humano. (c) ¿Qué pasaría con la confianza si el cliente no sabe quién responde? (d) Me parece mejor P2: desde la deontología, informar con verdad es un deber, y revisar permite responder por lo dicho. Reconozco que P1 tiene una razón fuerte: la rapidez ayuda a más clientes.",
   ["separa hechos y valores", "reconoce el valor de cada posición", "formula una pregunta respetuosa", "da una postura con dos razones y una perspectiva", "reconoce una razón fuerte del otro lado"],
   ["cuatro respuestas breves rotuladas (a) a (d)"],
   ["atribuir motivos a quienes piensan distinto", "postura sin razón"],
   "Se evalúa la calidad argumentativa y el respeto, no la postura. Si atribuye motivos a las personas, pide que se centre en la razón. Comprueba que reconozca una razón del otro lado."),
  "Escribe un hecho y un valor sobre el caso de la inteligencia artificial en el trabajo.",
  "Inventa una cuarta posición intermedia y escribe el valor que defiende.")

# ====================================================== clase 2
F = ("Ficha 2 (caso de ejemplo). Una aplicación ficticia de reparto de comida guarda la ubicación de los clientes para entregar los pedidos. "
     "La empresa estudia usar esos datos también para mostrar publicidad de otros negocios. "
     "Posición Q1: permitirlo, porque la persona aceptó las condiciones al instalar la aplicación. "
     "Posición Q2: permitirlo solo si la persona da una autorización específica y puede negarse sin perder el servicio. "
     "Posición Q3: prohibir cualquier uso distinto de entregar el pedido. "
     "Estructura de una intervención: tesis (lo que sostengo), dos razones, una objeción posible con mi respuesta y un cierre que invita a seguir conversando. "
     "Privacidad: ámbito de la vida de una persona que puede decidir mantener reservado.")
K(O, 2, F,
  "Hoy aplicaré lo aprendido a otra controversia, la privacidad de los datos, y prepararé una intervención ordenada para compartir mi visión personal en un diálogo.",
  ["La privacidad es el ámbito de la vida de una persona que puede decidir mantener reservado, como su ubicación o sus compras. Los datos digitales hacen que sea fácil guardarlos y usarlos para otros fines. La controversia aparece porque se pesan valores distintos: la autonomía de decidir sobre los propios datos, la utilidad de un servicio, el negocio de la empresa y la confianza de las personas.",
   "Las posiciones de la ficha dan distinto peso a esos valores. Q1 pone el acento en el consentimiento ya dado, Q2 en una autorización específica y libre, y Q3 en limitar los usos a lo necesario. Para evaluarlas se pregunta si cada razón es verdadera, si es relevante y qué valor sacrifica. Desde la deontología se mira el respeto a la decisión de cada persona; desde el utilitarismo, el balance de beneficios y perjuicios.",
   "Para participar en un diálogo conviene preparar una intervención con estructura: una tesis clara, dos razones, una objeción posible con tu respuesta y un cierre que invite a seguir conversando. Esta estructura vuelve visible tu pensamiento y facilita que otra persona lo examine. En la actividad abierta puedes compartir tu visión personal; lo que se evalúa es la calidad de las razones y el respeto, no la postura elegida."],
  [("privacidad", "ámbito de la vida de una persona que puede decidir mantener reservado"), ("consentimiento", "aceptación libre e informada de que se use algo propio"), ("autonomía", "capacidad de decidir sobre la propia vida y las propias cosas"), ("tesis", "lo que sostengo en una intervención")],
  [("Posición y valor", "{F} ¿Qué valor destaca Q2 al exigir autorización específica y poder negarse?", ["Pide que la persona decida libremente.", "Protege su decisión sobre los datos."], "La autonomía sobre los propios datos"),
   ("Estructura", "¿Qué parte de una intervención presenta lo que se sostiene?", ["Es la idea central de lo que se dice.", "Va al inicio."], "La tesis")],
  [("Confundir aceptar condiciones con comprender cada uso.", "Se asume que el consentimiento general cubre todo.", "Un consentimiento específico y libre es distinto de uno general."),
   ("Compartir una postura sin estructura ni razones.", "Se cree que decir «pienso X» basta.", "Ordena tesis, razones, objeción y cierre para que se pueda examinar.")],
  [("abc", "En Filosofía: ¿qué es la privacidad?", "El ámbito de la vida que una persona puede decidir mantener reservado", "Todo lo que ocurre en una casa", "La lista de todas las compras de un comercio", "Se refiere a lo que cada persona decide reservar."),
   ("abc", "{F} ¿Qué valor destaca sobre todo Q1?", "El consentimiento ya dado al aceptar las condiciones", "La prohibición de cualquier otro uso", "La autorización específica en cada caso", "Q1 se apoya en que la persona ya aceptó."),
   ("abc", "{F} ¿Qué valor destaca sobre todo Q3?", "Limitar los usos a lo necesario para el servicio", "El negocio de la publicidad", "El consentimiento general", "Q3 restringe el uso de datos al reparto."),
   ("abc", "{F} ¿En qué se diferencia Q2 de Q1?", "Q2 exige autorización específica y libre; Q1 se basa en haber aceptado condiciones", "Q2 prohíbe todo y Q1 permite todo", "No hay diferencia", "Q2 pide un consentimiento más específico que Q1."),
   ("abc", "{F} ¿Qué pregunta haría el utilitarismo ante este caso?", "¿Qué balance de beneficios y perjuicios hay para todas las personas afectadas?", "¿Qué haría una persona de buen carácter?", "¿Qué deber es absoluto?", "Mira beneficios y perjuicios para clientes y empresa."),
   ("abc", "{F} Si se pone el acento en el respeto a la decisión libre de cada persona, ¿cuál de estas dos posiciones se ve más reforzada?", "Q2, que exige autorización específica y poder negarse", "Q1, que se basa en haber aceptado condiciones al instalar", "Las dos por igual", "Q2 pide una decisión más específica y libre que Q1."),
   ("abc", "En una intervención ordenada, el cierre debería", "invitar a seguir conversando", "descalificar a quien discrepa", "repetir la tesis más fuerte", "Un cierre abierto mantiene el marco respetuoso."),
   ("abc", "Una persona dice: «Todas las aplicaciones usan los datos así, por eso Q1 es correcta». ¿Qué falacia es?", "Apelación a la mayoría", "Ad hominem", "Falso dilema", "Da por correcto algo porque muchos lo hacen."),
   ("abc", "Otra persona dice: «Si permitimos un uso extra, pronto no habrá nada privado en ninguna parte». ¿Qué falla tiene?", "Anuncia consecuencias extremas sin mostrar que ocurrirían", "Cita un dato comprobable", "Ataca a una persona", "Es una pendiente resbaladiza, pues salta a un extremo sin pruebas."),
   ("abc", "Una intervención dice: «Prefiero Q2 porque la persona debe decidir sobre sus datos y porque así se mantiene la confianza en la aplicación». ¿Cuántas razones tiene?", "Dos razones", "Una razón", "Ninguna razón", "Hay una por autonomía y otra por confianza."),
   ("abc", "Alguien responde a una objeción diciendo: «Entiendo que pedir autorización encarece el servicio; aun así pesa más la decisión de la persona». ¿Qué hace?", "Reconoce la objeción y responde con una razón", "Ataca a la persona", "Ignora la objeción", "Reconoce lo válido y explica por qué mantiene su postura."),
   ("abc", "¿Qué objeción razonable podría hacerse a Q3?", "Que podría impedir servicios útiles que algunas personas quisieran", "Que Q3 permite todo", "Que Q3 ataca a las personas", "Una prohibición total limita usos que alguien aceptaría libremente."),
   ("ab", "En el diálogo sobre este caso, ¿es válido que dos personas distintas elijan Q1 y Q2 con buenas razones?", "Sí: pesan de modo distinto el consentimiento y la autonomía", "No: una sola es correcta y la otra, absurda", "La calidad de las razones y el respeto importan más que coincidir.")],
  ("abc", "Una vecina ficticia prepara su intervención sobre una cámara que la junta quiere instalar en el pasaje. Escribe: tesis, dos razones, una objeción y un cierre. ¿Qué parte falta si solo escribió tesis y razones?", "La objeción con respuesta y el cierre", "Nada falta", "Una tercera razón", "La estructura incluye objeción con respuesta y un cierre."),
  [("En Filosofía: ¿qué es el consentimiento?", "Aceptación libre e informada de que se use algo propio", "Debe ser libre y comprender el uso que se hará."),
   ("¿Qué partes tiene una intervención ordenada?", "Tesis, dos razones, objeción con respuesta y cierre", "Así otra persona puede examinar el razonamiento."),
   ("¿Qué se evalúa en la actividad abierta?", "La calidad de las razones y el respeto, no la postura", "Compartir una visión no exige coincidir.")],
  ("{F} Prepara una intervención para un diálogo sobre este caso. Escribe (a) tu tesis sobre Q1, Q2, Q3 o una posición propia, (b) dos razones, (c) una objeción posible y tu respuesta, (d) qué perspectiva ética te ayudó a pensar y (e) un cierre que invite a seguir conversando.",
   "(a) Prefiero Q2. (b) Razón 1: la persona debe decidir sobre sus datos. Razón 2: pedir autorización específica mantiene la confianza en la aplicación. (c) Objeción: pedir permiso encarece el servicio. Respuesta: la confianza compensa el costo, y puede pedirse una sola vez con claridad. (d) La deontología, porque pone el respeto a cada persona. (e) ¿Qué otras formas de consentimiento les parecen justas?",
   ["tesis clara", "dos razones distintas", "objeción relevante con respuesta", "usa una perspectiva ética", "cierre abierto y respetuoso"],
   ["cinco respuestas breves rotuladas (a) a (e)"],
   ["dos razones que dicen lo mismo", "responder a la objeción atacando a la persona"],
   "Se evalúa la calidad argumentativa y el respeto, no la postura elegida. Si las razones se repiten, pide que busquen un valor distinto. Si no hay objeción, pregunta qué diría quien piensa diferente."),
  "Escribe una tesis y dos razones sobre otra controversia que conozcas, sin temas partidistas.",
  "Escribe una objeción posible a tu propia tesis y cómo la responderías.")
