"""Cuaderno del estudiante, 7.º básico Ciencias Naturales: OA 03 (infecciones de transmisión sexual) y OA 04 (barreras defensivas del cuerpo humano)."""
from __future__ import annotations

from student_content_cn7_a import L, task
from student_lessons import arith

OA3, OA4 = "CN07 OA 03", "CN07 OA 04"

# ---------------------------------------------------------------- OA 03
L(OA3, 1,
  materials="Este cuaderno y lápiz. Todos los casos son inventados; no necesitas contar nada personal.",
  use="Aprenderé qué son las infecciones de transmisión sexual (ITS) y a separar el agente que las causa, cómo se transmiten y qué manifestaciones pueden tener. Sirve para entender cómo se previenen.",
  prior=["Sé que las bacterias y los virus pueden causar enfermedades.", "Sé que debo informarme en fuentes confiables."],
  explain=[
      "Las infecciones de transmisión sexual (ITS) son infecciones que se transmiten principalmente por contacto sexual sin protección. Las causa un agente patógeno, que puede ser un virus (como el VIH, el herpes genital o el VPH) o una bacteria (como la sífilis, la gonorrea o la clamidia). Las bacterias se tratan con antibióticos; los virus, con antivirales, que controlan la infección pero no siempre la eliminan.",
      "La transmisión es el camino por donde pasa el agente de una persona a otra. En las ITS ocurre por contacto sexual con fluidos, piel o mucosas. Algunas, como el VIH, también se transmiten por sangre (por ejemplo compartiendo jeringas) y de madre a hijo en el embarazo, el parto o la lactancia. No se transmiten por abrazos, saludos, compartir vasos ni por picaduras de mosquitos.",
      "Las manifestaciones son los signos o síntomas que aparecen: ardor al orinar, secreciones, llagas, ampollas o picazón. Muchas ITS pueden no dar ningún síntoma, por lo que una persona puede tener la infección y transmitirla sin saberlo. Por eso el examen médico es la única forma de saber con certeza.",
  ],
  vocab=[("ITS", "infección de transmisión sexual"), ("patógeno", "agente que causa una enfermedad, como un virus o una bacteria"), ("transmisión", "camino por el que el agente pasa de una persona a otra"), ("manifestación", "signo o síntoma que muestra una infección"), ("asintomática", "infección que no produce síntomas")],
  worked=[
      ("Separar los tres elementos", "Lee: «El herpes genital lo causa un virus, se transmite por contacto de piel o mucosas y produce ampollas dolorosas». Identifica el agente, la transmisión y la manifestación.", ["Agente: lo que causa la infección, un virus.", "Transmisión: cómo pasa, por contacto de piel o mucosas.", "Manifestación: lo que se ve o siente, ampollas dolorosas."], "Agente: virus; transmisión: contacto de piel o mucosas; manifestación: ampollas dolorosas"),
      ("Vía posible o imposible", "¿Se puede transmitir el VIH por compartir una jeringa con sangre de otra persona? ¿Y por un abrazo?", ["Reviso las vías: sangre, contacto sexual, madre a hijo.", "La jeringa puede llevar sangre: es una vía posible.", "El abrazo no pasa fluidos: no es una vía."], "Jeringa: sí es posible; abrazo: no"),
  ],
  mistakes=[
      ("Creer que sin síntomas no hay infección.", "Muchas ITS son asintomáticas.", "Recuerda que solo un examen confirma."),
      ("Pensar que el VIH se transmite por saludar, abrazar o compartir un vaso.", "No hay paso de sangre ni de fluidos sexuales.", "Revisa las vías reales de transmisión."),
  ],
  rec=[
      ("¿Las ITS se transmiten principalmente por contacto sexual sin protección: verdadero o falso?", "Verdadero", "Esa es su vía principal."),
      ("¿El agente que causa una infección se llama patógeno u hormona?", "Patógeno", "Puede ser virus o bacteria."),
      ("¿El VIH es causado por un virus o por una bacteria?", "Un virus", "Se trata con antivirales que lo controlan."),
  ],
  und=[
      ("La sífilis es causada por una bacteria. ¿Con qué tipo de medicamento se trata, con antibióticos o con antivirales?", "Con antibióticos", "Los antibióticos actúan contra bacterias."),
      ("¿Cuál NO es una vía de transmisión del VIH? A) Compartir agujas con sangre de otra persona; B) Abrazar a una persona con VIH.", "B", "El abrazo no mezcla sangre ni fluidos sexuales."),
      ("Una persona dice: «No tengo síntomas, así que no tengo ninguna ITS». ¿Es correcto? Responde Sí o No.", "No", "Muchas ITS no dan síntomas."),
  ],
  app=[
      ("Cuatro infecciones: clamidia (bacteria), herpes genital (virus), sífilis (bacteria), VPH (virus). ¿Cuántas son causadas por virus?", "2", "Son el herpes genital y el VPH."),
      ("Tres infecciones: herpes genital (virus), gonorrea (bacteria), sífilis (bacteria). ¿Cuántas se tratan con antibióticos?", "2", "Las dos bacterianas: gonorrea y sífilis."),
      ("Julia lee que el VIH se puede transmitir de madre a hijo. ¿En cuál de estos momentos puede ocurrir? A) Durante el parto; B) Al saludar con un beso en la mejilla.", "A", "El parto es una vía; el saludo no."),
  ],
  rea=[
      ("Una ITS puede pasar de madre a hijo. ¿Qué muestra esto sobre las vías de transmisión? Responde en una frase.", "Que no todas son sexuales: también hay transmisión por sangre y de madre a hijo", "El caso demuestra que existen otras vías."),
      ("Dos personas tienen la misma infección bacteriana: una tiene secreción y la otra ningún síntoma. ¿Qué explica la diferencia? A) Las manifestaciones pueden variar y algunas personas no tienen síntomas; B) Una de ellas tiene un virus distinto.", "A", "La misma infección puede ser asintomática."),
  ],
  cha=[
      ("Lee: «La sífilis, causada por una bacteria, se transmite por contacto sexual y puede mostrar una llaga». ¿Qué parte de la frase es la manifestación?", "Una llaga", "Es lo que se ve; el resto es agente y transmisión."),
      ("Un estudiante dice: «Si hoy mi examen sale negativo, nunca tendré una ITS». ¿Qué error comete?", "El examen muestra solo el momento; la infección puede adquirirse después", "Un resultado negativo no da protección futura."),
  ],
  context=[("Dato de ejemplo. En un taller con 45 estudiantes, 27 sabían que muchas ITS pueden no dar síntomas. ¿Cuántos no lo sabían?", "18", "45 − 27 = 18; ese dato debe reforzarse.")],
  selfcheck=[("¿Qué es un patógeno?", "El agente que causa una infección, como un virus o una bacteria", "Es el origen de la infección."), ("Nombra dos vías de transmisión del VIH.", "Contacto sexual y sangre (o de madre a hijo)", "Son vías reales."), ("¿Por qué ayuda un examen aunque no haya síntomas?", "Porque muchas ITS no dan síntomas", "Es la forma de saber con certeza.")],
  open_task=task("Lee estas cuatro frases inventadas: (1) «La clamidia la causa una bacteria». (2) «Se transmite por contacto sexual». (3) «A veces no produce síntomas». (4) «Se trata con antibióticos». Rotula cada una como agente, transmisión, manifestación o tratamiento, y escribe una frase que explique por qué es útil un examen aunque no haya síntomas.", "(1) Agente. (2) Transmisión. (3) Manifestación. (4) Tratamiento. Es útil porque se puede tener la infección sin síntomas y transmitirla sin saberlo.", ["rotula las cuatro frases", "explica la utilidad del examen", "no culpa a nadie"], ["cuatro rótulos y una frase"], ["confundir agente con transmisión", "decir que sin síntomas no hay riesgo"], "Pregunta qué cambiaría si la infección fuera viral y no bacteriana."),
  reinforce="Escribe la diferencia entre agente y transmisión con un ejemplo.",
  extend="Explica por qué compartir jeringas es una vía de transmisión del VIH aunque no haya contacto sexual.")

L(OA3, 2,
  materials="Este cuaderno y lápiz. La tabla de comparación está escrita en la explicación y en los ejercicios.",
  use="Aprenderé a comparar algunas ITS por su agente, sus síntomas y sus consecuencias, sin asociarlas a ningún grupo de personas. Sirve para entender el riesgo con datos y no con prejuicios.",
  prior=["Sé que una ITS tiene un agente, una vía de transmisión y manifestaciones.", "Sé que algunas ITS no dan síntomas."],
  explain=[
      "El VIH es un virus que ataca a los linfocitos CD4, células de las defensas. Sin tratamiento, puede llegar al sida, que es la etapa en que las defensas están muy bajas. Hoy existe un tratamiento con antivirales que controla el virus y permite una vida larga, aunque no lo elimina. El herpes genital es otro virus: produce ampollas dolorosas que vuelven de tiempo en tiempo; no se cura, pero hay antivirales que alivian. El VPH es un virus muy común; algunos tipos producen verrugas genitales y otros pueden causar cáncer del cuello del útero con los años. Existe vacuna.",
      "La sífilis es una infección bacteriana: aparece una llaga que no duele; si no se trata puede dañar el corazón y el cerebro, pero se cura con antibióticos. La gonorrea y la clamidia también son bacterianas, pueden no dar síntomas y, si no se tratan, pueden dejar secuelas como dificultad para tener hijos. Las secuelas son daños que quedan después de la enfermedad.",
  "Comparar ITS no es acusar a nadie. Cualquier persona que tenga relaciones sexuales sin protección puede contraer una ITS; la identidad, el género o el barrio no son la causa. Lo que cambia el riesgo son las conductas, como usar o no preservativo, y no tener información. Estigmatizar a un grupo es un error y aleja a las personas del examen y del tratamiento.",
  ],
  vocab=[("linfocitos CD4", "células de las defensas que ataca el VIH"), ("sida", "etapa avanzada de la infección por VIH, con defensas muy bajas"), ("secuela", "daño que queda después de una enfermedad"), ("antiviral", "medicamento que controla un virus"), ("estigma", "rechazo injusto hacia una persona o grupo")],
  worked=[
      ("Comparar dos ITS", "Compara VIH y sífilis según agente y tratamiento.", ["VIH: virus, se controla con antivirales.", "Sífilis: bacteria, se cura con antibióticos.", "Agente y tratamiento son distintos."], "VIH: virus con antivirales que controlan; sífilis: bacteria que se cura con antibióticos"),
      ("Sin asociar a identidades", "Alguien dice: «Esas infecciones solo las tiene cierto grupo de personas». ¿Es correcto?", ["Reviso qué determina el riesgo.", "Lo determinan las conductas y la prevención.", "La identidad no causa la infección."], "No: cualquier persona puede contraer una ITS sin protección"),
  ],
  mistakes=[
      ("Pensar que una ITS afecta solo a ciertos grupos de personas.", "El riesgo depende de las conductas y la prevención, no de la identidad.", "Habla de conductas de riesgo y de prevención."),
      ("Creer que el sida y el VIH son lo mismo.", "El VIH es el virus; el sida es la etapa avanzada sin tratamiento.", "Distingue virus y etapa."),
  ],
  rec=[
      ("¿Qué infección causa verrugas genitales y se previene con una vacuna: el VPH o la sífilis?", "El VPH", "Existe vacuna contra los tipos más peligrosos."),
      ("¿La sífilis se cura con antibióticos: verdadero o falso?", "Verdadero", "Es una infección bacteriana."),
      ("¿Qué infección produce ampollas dolorosas que vuelven: el herpes genital o la clamidia?", "El herpes genital", "Es causado por un virus."),
  ],
  und=[
      ("¿Qué es el sida? A) La etapa avanzada de la infección por VIH, con defensas muy bajas; B) Una infección bacteriana.", "A", "El VIH es un virus y el sida es la etapa avanzada."),
      ("Hoy, ¿qué permite el tratamiento con antivirales en el VIH? A) Controlar el virus y vivir muchos años; B) Eliminarlo del cuerpo y dejar de necesitar controles.", "A", "Controla pero no elimina el virus."),
      ("¿Qué causa el riesgo de contraer una ITS: la identidad de una persona o conductas sin protección?", "Conductas sin protección", "El riesgo depende de la exposición, no de quién eres."),
  ],
  app=[
      ("Tabla: VIH (virus, antiviral), herpes genital (virus, antiviral), VPH (virus, vacuna), sífilis (bacteria, antibiótico), clamidia (bacteria, antibiótico). ¿Cuántas son bacterianas?", "2", "Son la sífilis y la clamidia."),
      ("Con la misma tabla, ¿cuál de las cinco infecciones se previene con vacuna?", "El VPH", "Es la única de la tabla que lleva vacuna."),
      ("Con la misma tabla, ¿cuántas se tratan con antivirales?", "2", "El VIH y el herpes genital."),
  ],
  rea=[
      ("Un compañero dice: «Esa infección solo la tiene la gente que vive en cierto barrio». Escribe una frase que lo corrija.", "El riesgo depende de las conductas y la prevención, no del lugar donde vive la gente", "Es un estereotipo."),
      ("¿Por qué el estigma puede aumentar el riesgo de que una infección se propague? Responde en una frase.", "Porque las personas pueden no hacerse el examen ni consultar por miedo a ser juzgadas", "Quien no consulta no se trata."),
  ],
  cha=[
      ("Datos de ejemplo de 20 personas con clamidia en un centro de salud ficticio: 14 no tuvieron síntomas. ¿Qué afirmación está apoyada? A) La mayoría no tuvo síntomas; B) Todas tuvieron síntomas.", "A", "14 de 20 es más de la mitad."),
      ("Una persona no se trató una clamidia por años. ¿Qué secuela podría tener? A) Dificultad para tener hijos; B) Caída del cabello.", "A", "Las infecciones bacterianas no tratadas pueden dañar el aparato reproductor."),
  ],
  context=[("Dato de ejemplo. En un liceo ficticio se vacunaron contra el VPH 52 de 60 estudiantes de un nivel. ¿Cuántos faltan por vacunarse?", "8", "60 − 52 = 8.")],
  selfcheck=[("¿Qué diferencia hay entre VIH y sida?", "El VIH es el virus; el sida es la etapa avanzada sin tratamiento", "Con tratamiento se controla el virus."), ("¿Qué infección se cura con antibióticos?", "La sífilis, por ejemplo, porque es bacteriana", "Los antibióticos actúan contra bacterias."), ("¿Qué determina el riesgo de una ITS?", "Las conductas y la prevención, no la identidad", "El estigma es un error.")],
  open_task=task("Completa una tabla de comparación con estas tres ITS: VIH, sífilis, VPH. Columnas: agente (virus o bacteria), una manifestación, tratamiento o prevención disponible. Escribe después una frase que explique por qué no se debe asociar una ITS a una identidad.", "VIH: virus; defensas bajas si no se trata; antivirales. Sífilis: bacteria; llaga; antibióticos. VPH: virus; verrugas; vacuna. Frase: cualquier persona sin protección puede contraerlas.", ["tabla completa", "datos correctos", "frase sin estigma"], ["tabla y una frase"], ["decir que el VIH se cura con antibióticos", "asociar la ITS a un grupo"], "Pregunta cómo ayuda hablar de conductas y no de identidades."),
  reinforce="Escribe una ITS viral y una bacteriana con su tratamiento.",
  extend="Explica por qué una secuela puede aparecer años después de una infección sin tratar.")

L(OA3, 3,
  materials="Este cuaderno y lápiz. Los casos son inventados; no necesitas contar nada personal.",
  use="Aprenderé cómo se previenen las ITS, cuándo consultar y cómo reconocer información vigente. Sirve para cuidar mi salud y la de otros con datos confiables.",
  prior=["Sé que hay ITS virales y bacterianas.", "Sé que una fuente confiable es un profesional de salud."],
  explain=[
      "La prevención incluye varias medidas. El preservativo, bien usado en cada relación, reduce el riesgo de muchas ITS. La abstinencia evita el riesgo por vía sexual. La vacuna protege contra el VPH y la hepatitis B. No compartir agujas ni jeringas evita la transmisión por sangre. Hablar con la pareja y hacerse exámenes cuando corresponde también cuida a ambos.",
      "Si hay síntomas o una posible exposición, se debe consultar a un centro de salud y contárselo a una persona adulta de confianza, que puede acompañar. Los equipos de salud deben resguardar la reserva de tu información. Las bacterias se tratan con antibióticos indicados por un profesional; tomarlos sin receta puede ocultar el problema y no cura virus. En los virus, el tratamiento controla la infección.",
      "La información sobre salud cambia. Una fuente vigente tiene institución o autor conocido, fecha reciente y datos que se pueden contrastar, como el sitio del Ministerio de Salud o la OMS. Desconfía de las páginas que prometen curas milagrosas, piden dinero o datos personales, o no tienen fecha.",
  ],
  vocab=[("prevención", "medidas que evitan que ocurra una infección"), ("exposición", "situación en que pudo haber contacto con un agente"), ("reserva", "deber de los equipos de salud de proteger tu información"), ("vigente", "actualizada y válida hoy"), ("automedicación", "tomar medicamentos sin indicación profesional")],
  worked=[
      ("Elegir medidas", "¿Cuáles medidas previenen ITS: usar preservativo en cada relación, tomar antibióticos «por si acaso», vacunarse contra el VPH?", ["El preservativo reduce el riesgo.", "Los antibióticos «por si acaso» no previenen y es automedicación.", "La vacuna protege contra el VPH."], "Preservativo y vacuna previenen; antibióticos «por si acaso» no"),
      ("Evaluar una fuente", "Una página dice: «Cura natural de ITS en 3 días. Compra ahora. Sin fecha ni autor». ¿Es una fuente vigente?", ["Busco autor y fecha: no tiene.", "Promete una cura milagrosa y pide comprar.", "Esas son señales de alerta."], "No es una fuente confiable"),
  ],
  mistakes=[
      ("Tomar antibióticos sin receta si se sospecha una ITS.", "Pueden ocultar síntomas y no sirven contra virus.", "Consulta a un profesional de salud."),
      ("Creer que una vacuna protege contra todas las ITS.", "Cada vacuna protege contra infecciones específicas.", "Combina con otras medidas de prevención."),
  ],
  rec=[
      ("¿Qué método de barrera reduce el riesgo de ITS cuando se usa bien en cada relación: el preservativo o la píldora?", "El preservativo", "La píldora no protege contra ITS."),
      ("¿Debe tomarse antibióticos sin receta si se sospecha una ITS: verdadero o falso?", "Falso", "Se necesita indicación profesional."),
      ("¿Dónde conviene consultar: un centro de salud o un foro anónimo?", "Un centro de salud", "Allí hay profesionales y reserva de información."),
  ],
  und=[
      ("¿Qué vacuna ayuda a prevenir infecciones por VPH? A) La vacuna contra el VPH; B) La vacuna contra la gripe.", "A", "Cada vacuna protege contra un agente."),
      ("¿Por qué no se deben compartir agujas ni jeringas? A) La sangre que queda en ellas puede llevar virus como el VIH; B) Se desgastan y no sirven si otra persona las usa después.", "A", "Es una vía de transmisión por sangre."),
      ("Los equipos de salud deben resguardar la reserva de la información de las personas. ¿Verdadero o falso?", "Verdadero", "Proteger la privacidad es parte de su deber."),
  ],
  app=[
      arith("En un colegio ficticio de 60 estudiantes, 54 recibieron la vacuna contra el VPH. ¿Qué porcentaje del grupo está vacunado?", "54*100//60", "Se divide entre el total y se multiplica por 100."),
      ("Alguien tuvo una posible exposición. ¿Cuál acción NO es adecuada? A) Esperar a ver si aparecen síntomas sin consultar; B) Consultar en un centro de salud.", "A", "Esperar puede retrasar el diagnóstico."),
      ("Una página de salud muestra: autor «Ministerio de Salud», fecha de este año, datos con fuentes. ¿Es una fuente vigente?", "Sí", "Tiene institución, fecha reciente y datos contrastables."),
  ],
  rea=[
      ("Una web dice «cura natural en 3 días». Escribe dos criterios para dudar.", "Promete una cura milagrosa y no tiene autor ni fecha", "Son señales de información poco confiable."),
      ("Si el preservativo se usa solo a veces, ¿protege igual que si se usa en cada relación? Responde Sí o No.", "No", "Solo protege cuando se usa bien en cada relación."),
  ],
  cha=[
      ("La vacuna contra el VPH, ¿protege contra el VIH? Responde Sí o No y explica en una frase.", "No; cada vacuna protege solo contra su agente", "Por eso se combinan medidas."),
      ("Un compañero se enteró del resultado del examen de otra persona y quiere contarlo en el curso. ¿Qué principio se rompe y qué debería hacer? Responde en una frase.", "Se rompe la reserva; debe guardar la privacidad y no contarlo", "La información de salud es privada."),
  ],
  context=[("Dato de ejemplo. Un liceo ficticio tiene 180 estudiantes en 7.º y 8.º; 126 ya recibieron una dosis de una vacuna escolar. ¿Cuántos faltan?", "54", "180 − 126 = 54.")],
  selfcheck=[("Nombra tres medidas de prevención de ITS.", "Preservativo bien usado, vacunas y no compartir agujas", "Son medidas reales."), ("¿Cuándo consultar a un centro de salud?", "Ante síntomas o una posible exposición", "Es lo más seguro."), ("¿Qué hace vigente a una fuente?", "Institución o autor conocido, fecha reciente y datos contrastables", "Se pueden verificar.")],
  open_task=task("Revisa estas dos fuentes inventadas sobre prevención. Fuente 1: «Ministerio de Salud, publicada este año, explica cómo se usa el preservativo y qué vacunas existen». Fuente 2: «Blog sin autor ni fecha que vende una cura milagrosa». Decide cuál es más confiable, escribe tres criterios y redacta un consejo para un compañero.", "La fuente 1: tiene institución, fecha y datos. La 2 no tiene autor ni fecha y promete milagros. Consejo: consulta en un centro de salud y desconfía de curas milagrosas.", ["elige la fuente confiable", "tres criterios", "consejo sin datos personales"], ["tres frases"], ["elegir la fuente por lo atractiva", "dar datos personales"], "Pregunta cómo verificaría una tercera fuente."),
  reinforce="Escribe dos señales de alerta en una página de salud.",
  extend="Explica por qué se combinan varias medidas de prevención y no se confía en una sola.")

L(OA3, 4,
  materials="Este cuaderno y lápiz. Las afirmaciones son ejemplos inventados para evaluar.",
  use="Aprenderé a evaluar mitos sobre ITS y a cuidar la privacidad cuando busco o comparto información. Sirve para no difundir errores ni exponer datos de otros.",
  prior=["Sé qué vías de transmisión tienen las ITS.", "Sé reconocer una fuente vigente."],
  explain=[
      "Un mito es una creencia falsa que se repite. Algunos mitos sobre ITS son: «el VIH se contagia con un abrazo o un vaso compartido», «solo ciertos grupos tienen ITS», «si no hay síntomas no hay infección», «lavarse después evita la infección» y «la píldora protege contra ITS». Todos son falsos: lo que se ha comprobado es lo contrario.",
      "Para evaluar una afirmación se hacen cuatro preguntas: ¿quién la dice?, ¿cuándo se publicó?, ¿qué datos o fuentes tiene?, ¿qué quiere de mí (dinero, datos, que la comparta)? Una afirmación sin fuente y con urgencia, como «comparte con 10 amigos», es una señal de alerta.",
      "La privacidad significa cuidar la información personal. No se publica el nombre, el colegio, las fotos ni los resultados de exámenes propios o ajenos en foros o redes. Una duda se puede preguntar de forma general: «¿cómo se previene una ITS?». Si algo te preocupa, se lo cuentas a una persona adulta de confianza o a un centro de salud.",
  ],
  vocab=[("mito", "creencia falsa que se repite"), ("señal de alerta", "rasgo que hace dudar de una información"), ("privacidad", "cuidado de la información personal"), ("contrastar", "comparar con otras fuentes confiables"), ("difundir", "compartir una información con otras personas")],
  worked=[
      ("Mito o hecho", "«Se puede contagiar el VIH por abrazar a una persona que lo tiene». ¿Es mito o hecho?", ["El VIH necesita sangre o fluidos sexuales.", "Un abrazo no los pasa.", "La frase es falsa."], "Es un mito"),
      ("Pregunta segura", "Un estudiante quiere escribir en un foro: «Me llamo Luis, voy en 7.º A de este colegio y creo que tengo una ITS». ¿Qué cambiarías?", ["Los datos personales deben quitarse.", "La pregunta puede ser general.", "Además conviene hablar con un adulto de confianza."], "Quitar nombre y colegio, preguntar de forma general y hablar con un adulto de confianza"),
  ],
  mistakes=[
      ("Compartir un mensaje alarmante sin comprobarlo.", "Si es falso, se difunde un error.", "Contrasta con una fuente confiable antes de compartir."),
      ("Publicar datos personales para pedir ayuda en un foro.", "Cualquiera puede ver esa información.", "Pregunta en general o con un adulto de confianza."),
  ],
  rec=[
      ("¿Una creencia falsa que se repite es un mito o un dato?", "Un mito", "No tiene respaldo."),
      ("«El VIH se contagia por compartir un vaso» es un mito. ¿Verdadero o falso?", "Verdadero", "No hay paso de sangre ni de fluidos sexuales."),
      ("¿Se deben publicar los resultados de exámenes en un foro: sí o no?", "No", "Son información privada."),
  ],
  und=[
      ("De estas dos frases, ¿cuál es un mito? A) «El VIH se contagia por saludar con la mano.» B) «Las vacunas contra el VPH ayudan a prevenir infecciones por VPH.»", "A", "No hay contacto de sangre ni de fluidos."),
      ("¿Cuál es una señal de alerta? A) «Cura milagrosa, comparte con 10 amigos»; B) «Revisado por el Ministerio de Salud este año».", "A", "Pide difundir sin datos y promete milagros."),
      ("¿Qué pregunta es segura para un foro? A) «¿Cómo se previenen las ITS?» B) «Soy Ana de 7.º B, ¿dónde me hago un examen?»", "A", "No revela datos personales."),
  ],
  app=[
      ("Cinco frases: (1) El VIH se contagia por un abrazo. (2) Solo ciertos grupos tienen ITS. (3) Sin síntomas no hay infección. (4) El preservativo bien usado reduce el riesgo. (5) Las ITS se pueden prevenir. ¿Cuántas son mitos?", "3", "Las frases 1, 2 y 3 son falsas."),
      ("Un mensaje dice: «Urgente: el VIH se contagia por tocar manijas. Comparte antes de que lo borren». Señales de alerta posibles: apuro, ninguna fuente nombrada, pide compartir, tiene fecha reciente. ¿Cuántas señales de alerta aparecen realmente?", "3", "Hay apuro, falta de fuente y petición de compartir; no se menciona ninguna fecha."),
      ("Si encuentras una afirmación sin fecha, ¿qué haces primero: la contrastas con una fuente vigente o la compartes?", "La contrastas con una fuente vigente", "Sin contrastar puede ser falsa."),
  ],
  rea=[
      ("Un compañero muestra el resultado de un examen de otra persona. ¿Qué debes hacer y por qué? Responde en una frase.", "No compartirlo, porque es información privada de esa persona", "Respetar la privacidad protege a la persona."),
      ("¿Por qué «solo ciertos grupos tienen ITS» es un mito peligroso?", "Porque hace creer que otras personas no necesitan cuidarse", "Cualquier persona sin protección puede contraerlas."),
  ],
  cha=[
      ("Una página ofrece «un examen secreto» y pide tu nombre, tu colegio y tu dirección. ¿Qué haces? A) No entregar datos y consultar a un adulto de confianza; B) Entregar los datos para ver el resultado.", "A", "Hay riesgo de mal uso de tus datos."),
      ("Redacta un consejo breve para un compañero que cree que «si no hay síntomas no hay ITS».", "Muchas ITS no dan síntomas; solo un examen lo confirma", "Corrige el mito con un dato."),
  ],
  context=[("Dato de ejemplo. En una prueba con 40 estudiantes, 28 identificaron correctamente un mito. ¿Cuántos no lo identificaron?", "12", "40 − 28 = 12.")],
  selfcheck=[("En Ciencias: ¿Qué es un mito?", "Una creencia falsa que se repite", "No tiene respaldo en datos."), ("¿Cuáles son cuatro preguntas para evaluar una afirmación?", "Quién la dice, cuándo, con qué datos y qué quiere de mí", "Ayudan a evaluar la fuente."), ("¿Qué hacer con tus datos personales en un foro?", "No publicarlos", "Se cuida la privacidad.")],
  open_task=task("Evalúa estas tres afirmaciones inventadas y escribe mito o hecho con una razón: (1) «El preservativo bien usado reduce el riesgo de ITS». (2) «El VIH se transmite al compartir el plato». (3) «Un examen negativo hoy protege para siempre». Reescribe la que sea mito como una afirmación correcta.", "(1) Hecho: barrera. (2) Mito: no se transmite por compartir comida. (3) Mito: solo muestra hoy. Reescritura: «El VIH no se transmite por compartir el plato».", ["tres rótulos con razón", "reescritura correcta", "no revela datos personales"], ["tres frases y una reescritura"], ["marcar un hecho como mito", "reescribir con otro error"], "Pregunta cómo verificaría una cuarta afirmación."),
  reinforce="Escribe un mito y su corrección.",
  extend="Explica por qué compartir una información falsa puede dañar a otras personas.")

L(OA3, 5,
  materials="Este cuaderno y lápiz. Los datos son ficticios y no corresponden a ningún centro de salud real.",
  use="Aprenderé a contrastar afirmaciones sobre ITS con datos y a no confundir casos detectados con casos reales. Sirve para leer informes con criterio.",
  prior=["Sé que muchas ITS no dan síntomas.", "Sé evaluar mitos y fuentes."],
  explain=[
      "Contrastar es comparar una afirmación con los datos y decidir si los datos la apoyan, la contradicen o no alcanzan. Por ejemplo, si de 40 personas con una infección, 28 no tuvieron síntomas, se apoya «la mayoría no tuvo síntomas» y se contradice «todas tuvieron síntomas».",
      "Los casos detectados dependen de cuántos exámenes se hacen. Si en un centro se hacen el doble de exámenes, aparecerán más casos aunque la proporción no cambie. Por eso se mira la positividad, que es el porcentaje de exámenes con resultado positivo: casos ÷ exámenes × 100.",
      "Todo informe tiene límites. Los datos de un centro no representan a todo el país, un año no muestra una tendencia y los casos detectados no son todos los casos reales. Una conclusión prudente dice qué muestran los datos y qué no pueden mostrar.",
  ],
  vocab=[("caso detectado", "persona con resultado positivo en un examen"), ("positividad", "porcentaje de exámenes con resultado positivo"), ("tendencia", "dirección en que cambian los datos en varios períodos"), ("proporción", "parte de un total"), ("conclusión prudente", "afirmación que no exagera lo que muestran los datos")],
  worked=[
      ("Calcular la positividad", "En un centro ficticio se hicieron 200 exámenes y 30 salieron positivos. ¿Cuál es la positividad?", ["Positividad = casos ÷ exámenes × 100.", "30 × 100 ÷ 200 = 15."], "15 %"),
      ("Apoyar o contradecir", "Con 40 personas infectadas y 28 sin síntomas, ¿qué pasa con la frase «todas tuvieron síntomas»?", ["28 de 40 no tuvieron síntomas.", "Entonces no es cierto que todas tuvieran síntomas."], "Se contradice"),
  ],
  mistakes=[
      ("Creer que más casos detectados significa siempre más infección real.", "Pueden detectarse más porque se hacen más exámenes.", "Compara la positividad, no solo los casos."),
      ("Generalizar con los datos de un centro.", "Un centro no representa al país.", "Limita la conclusión a lo medido."),
  ],
  rec=[
      ("¿Qué mide la positividad: el porcentaje de exámenes positivos o el total de personas?", "El porcentaje de exámenes positivos", "Es casos ÷ exámenes × 100."),
      ("Si todos los datos muestran lo contrario, ¿la afirmación se apoya o se contradice?", "Se contradice", "No coincide con los datos."),
      ("¿Un año de datos basta para hablar de una tendencia: sí o no?", "No", "Se necesitan varios períodos."),
  ],
  und=[
      ("Un centro hizo 100 exámenes y 10 salieron positivos. ¿Cuál es la positividad? A) 10 %; B) 100 %.", "A", "10 × 100 ÷ 100 = 10."),
      ("¿Por qué pueden subir los casos detectados sin que suba la infección real? A) Porque se hicieron más exámenes; B) Porque los exámenes dejaron de servir.", "A", "Mayor cantidad de pruebas detecta más casos."),
      ("De 50 personas con una infección, 35 no tuvieron síntomas. ¿Qué afirmación se apoya? A) La mayoría no tuvo síntomas; B) Nadie tuvo síntomas.", "A", "35 de 50 es más de la mitad, pero hubo 15 con síntomas."),
  ],
  app=[
      arith("Año 1: 240 exámenes con 36 positivos. ¿Cuál es la positividad en porcentaje?", "36*100//240", "Se divide entre el total y se multiplica por 100."),
      arith("Año 2: 300 exámenes con 45 positivos. ¿Cuál es la positividad en porcentaje?", "45*100//300", "Se calcula igual que en el año 1."),
      arith("Año 1: 36 casos. Año 2: 45 casos. ¿Cuántos casos más hubo en el año 2?", "45-36", "Se resta."),
  ],
  rea=[
      ("Con los datos anteriores, los casos subieron de 36 a 45 y la positividad fue 15 % en ambos años. ¿Qué explica mejor el aumento de casos? A) Se hicieron más exámenes; B) Subió la infección real.", "A", "La positividad no cambió."),
      ("Alguien concluye: «En todo Chile subieron los casos». ¿Qué límite tiene su afirmación?", "Los datos son de un solo centro", "No representan al país."),
  ],
  cha=[
      ("Hay 40 personas con una infección y 28 no tuvieron síntomas. Afirmación 1: «La mayoría no tuvo síntomas». Afirmación 2: «Todas se curaron con antibióticos». ¿Para cuál afirmación no alcanzan los datos? Escribe 1 o 2.", "2", "No hay datos sobre curación en lo que se entregó."),
      ("Redacta una conclusión prudente para el centro ficticio con 15 % de positividad en dos años.", "La positividad se mantuvo en 15 % en dos años en este centro", "Describe sin exagerar."),
  ],
  context=[("Dato de ejemplo. Un centro ficticio hizo 250 exámenes y 25 salieron positivos. ¿Cuántos fueron negativos?", "225", "250 − 25 = 225.")],
  selfcheck=[("¿Qué es la positividad?", "El porcentaje de exámenes con resultado positivo", "Es casos ÷ exámenes × 100."), ("¿Por qué no basta mirar los casos detectados?", "Porque dependen de cuántos exámenes se hacen", "Hay que ver la proporción."), ("¿Qué límite tiene un informe de un solo centro?", "No representa a todo el país", "Hay que declararlo.")],
  open_task=task("Con estos datos ficticios, calcula la positividad de cada año y escribe una conclusión con un límite. Año 1: 200 exámenes, 20 positivos. Año 2: 400 exámenes, 40 positivos. Año 3: 500 exámenes, 75 positivos.", "Año 1: 10 %. Año 2: 10 %. Año 3: 15 %. Conclusión: la positividad subió en el año 3; el límite es que es un solo centro y tres años.", ["tres cálculos correctos", "conclusión prudente", "declara un límite"], ["cálculos y dos frases"], ["usar solo los casos", "generalizar al país"], "Pregunta qué dato nuevo ayudaría a explicar el aumento."),
  reinforce="Calcula la positividad de 60 exámenes con 6 positivos.",
  extend="Explica por qué la positividad es mejor que el número de casos para comparar dos años.")

# ---------------------------------------------------------------- OA 04
L(OA4, 1,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y se escriben en los ejercicios. Opcional: jabón y agua para recordar el lavado de manos.",
  use="Aprenderé cuáles son las barreras primarias del cuerpo y cómo frenan a patógenos como la bacteria Escherichia coli y el virus de la gripe. Sirve para entender el lavado de manos y otros hábitos.",
  prior=["Sé que las bacterias y los virus pueden causar enfermedades.", "Sé que el cuerpo tiene defensas."],
  explain=[
      "El sistema inmune protege al cuerpo con tres barreras. Las barreras primarias evitan que los patógenos entren. Pueden ser físicas, como la piel o el moco con cilios (pelitos que lo mueven en las vías respiratorias); químicas, como el ácido del estómago, las lágrimas y la saliva, que destruyen microorganismos; y biológicas, como la flora normal, bacterias beneficiosas que ocupan el lugar y compiten con las dañinas.",
      "Dos ejemplos de patógenos son la bacteria Escherichia coli y el virus de la influenza (gripe). Algunas cepas de E. coli llegan al intestino con alimentos mal lavados o mal cocidos y causan diarrea; el ácido del estómago y la flora intestinal las frenan. El virus de la gripe entra por la nariz, la boca o los ojos en pequeñas gotitas; el moco y los cilios intentan atraparlo.",
      "Las barreras primarias fallan si se rompen, por ejemplo con una herida, o si se debilitan, como cuando un antibiótico elimina la flora normal. Los hábitos que las apoyan son lavarse las manos, cubrir la tos, cuidar las heridas y manipular bien los alimentos.",
  ],
  vocab=[("barrera primaria", "primera defensa que impide el ingreso de patógenos"), ("cilios", "pelitos del moco que arrastran partículas fuera de las vías respiratorias"), ("flora normal", "bacterias beneficiosas que viven en el cuerpo y protegen"), ("patógeno", "microorganismo que causa enfermedad"), ("cepa", "variedad de un microorganismo")],
  worked=[
      ("Clasificar una barrera", "Clasifica como física, química o biológica: (1) la piel, (2) el ácido del estómago, (3) las bacterias beneficiosas del intestino.", ["La piel es una cubierta que impide el paso: física.", "El ácido destruye microorganismos: química.", "Las bacterias beneficiosas compiten: biológica."], "1 física; 2 química; 3 biológica"),
      ("Barrera y patógeno", "¿Qué barrera primaria frena a una E. coli que llega con un alimento mal lavado?", ["La E. coli va al estómago.", "El ácido del estómago destruye muchos microorganismos.", "La flora intestinal compite con la bacteria."], "El ácido del estómago y la flora intestinal"),
  ],
  mistakes=[
      ("Pensar que la piel solo sirve para cubrir el cuerpo.", "También es una barrera que impide el paso de patógenos.", "Recuerda que una herida abre la barrera."),
      ("Creer que todas las bacterias son dañinas.", "La flora normal protege.", "Distingue bacterias beneficiosas de patógenas."),
  ],
  rec=[
      ("¿Cuál es una barrera primaria que cubre todo el cuerpo: la piel o el estómago?", "La piel", "Forma una cubierta continua."),
      ("Las lágrimas y la saliva contienen sustancias que destruyen microorganismos. ¿Verdadero o falso?", "Verdadero", "Son barreras químicas."),
      ("¿Los cilios de las vías respiratorias mueven el moco o producen lágrimas?", "Mueven el moco", "Así lo sacan con los patógenos atrapados."),
  ],
  und=[
      ("Clasifica el moco con cilios: ¿barrera física, química o biológica?", "Física", "Atrapa y arrastra partículas."),
      ("¿Cuál es una barrera química? A) El ácido del estómago; B) Los pelitos de la nariz.", "A", "El ácido destruye microorganismos."),
      ("¿Qué hace la flora normal frente a un patógeno? A) Compite con él por el espacio y los nutrientes; B) Lo transforma en alimento.", "A", "Impide que se instale."),
  ],
  app=[
      arith("En un cultivo de ejemplo, las manos sin lavar tenían 200 colonias de bacterias (grupos visibles de bacterias). Con agua sola quedaron 120 y con agua y jabón, 20. ¿Cuántas colonias menos hay con jabón que con agua sola?", "120-20", "Se resta lo que queda con jabón."),
      arith("Con los mismos datos, ¿cuántas colonias se eliminaron al lavar con agua y jabón respecto de las manos sin lavar?", "200-20", "Se resta lo que queda de lo inicial."),
      ("Una herida abre la piel. ¿Qué barrera se rompe? A) Una barrera física; B) Una barrera biológica.", "A", "La piel es una cubierta física."),
  ],
  rea=[
      ("Un antibiótico elimina parte de la flora intestinal. ¿Por qué puede aumentar el riesgo de diarreas por patógenos? Responde en una frase.", "Porque se debilita la barrera biológica que compite con los patógenos", "La flora normal protege."),
      ("¿Por qué lavar los alimentos y cocerlos bien ayuda a frenar a E. coli?", "Porque disminuye los patógenos que llegan al intestino", "Se reduce la cantidad que entra."),
  ],
  cha=[
      ("El virus de la gripe entra por la nariz. ¿Qué barrera primaria intenta atraparlo primero? A) El moco con cilios; B) El ácido del estómago.", "A", "El moco está en la nariz; el ácido está mucho más adentro."),
      ("Un compañero dice: «Si me lavo las manos, la piel deja de ser barrera». Corrígelo.", "El lavado reduce los patógenos y la piel sigue siendo una barrera", "Complementan la defensa."),
  ],
  context=[("Dato de ejemplo. Un colegio midió que antes del recreo había 150 colonias de bacterias en una superficie y después de limpiar quedaron 45. ¿Cuántas se eliminaron?", "105", "150 − 45 = 105.")],
  selfcheck=[("¿Qué es una barrera primaria?", "La primera defensa que impide el ingreso de patógenos", "Puede ser física, química o biológica."), ("¿Qué hace el ácido del estómago?", "Destruye microorganismos", "Es una barrera química."), ("¿Qué es la flora normal?", "Bacterias beneficiosas que compiten con las dañinas", "Es una barrera biológica.")],
  open_task=task("Dibuja el cuerpo y marca cuatro barreras primarias: piel, moco con cilios, ácido del estómago y flora intestinal. Al lado de cada una escribe su tipo (física, química o biológica) y un hábito que la cuida.", "Piel (física): cuidar heridas. Moco con cilios (física): cubrir la tos. Ácido del estómago (química): lavar los alimentos. Flora intestinal (biológica): no automedicarse con antibióticos.", ["cuatro barreras", "tipo correcto", "hábito asociado"], ["dibujo rotulado"], ["clasificar el ácido como física", "olvidar un hábito"], "Pregunta qué barrera protege a E. coli y cuál a la gripe."),
  reinforce="Escribe tres barreras primarias y su tipo.",
  extend="Explica por qué un hábito como lavarse las manos apoya a las barreras primarias.")

L(OA4, 2,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo y están escritos en cada ejercicio.",
  use="Aprenderé la respuesta innata o secundaria: inflamación, fagocitos y fiebre. Sirve para entender por qué una herida se hincha y por qué la fiebre puede ayudar.",
  prior=["Sé qué son las barreras primarias.", "Sé que un patógeno puede entrar si la barrera falla."],
  explain=[
      "Si un patógeno atraviesa las barreras primarias, actúa la barrera secundaria o respuesta innata. Es rápida y general: no distingue qué patógeno es. Sus herramientas son la inflamación, los fagocitos y la fiebre. La inflamación produce enrojecimiento, calor, hinchazón y dolor porque llega más sangre con defensas al lugar afectado.",
      "Los fagocitos, como los macrófagos y los neutrófilos, son glóbulos blancos que rodean y se comen a los patógenos; el proceso se llama fagocitosis. Algunas células liberan proteínas llamadas interferones, que avisan a otras células que hay un virus. La fiebre, una temperatura sobre los 38 °C, retarda el crecimiento de muchos microorganismos y acelera las defensas.",
      "La respuesta innata se activa en minutos u horas, pero no deja memoria: la próxima vez responde igual. Si no basta, entra la respuesta adaptativa. Esta clase usa el ejemplo de E. coli en el intestino, donde hay inflamación y fagocitos, y el de la gripe, donde hay fiebre e interferones.",
  ],
  vocab=[("inflamación", "respuesta con enrojecimiento, calor, hinchazón y dolor"), ("fagocito", "glóbulo blanco que se come patógenos"), ("fagocitosis", "proceso por el que un fagocito rodea e ingiere un patógeno"), ("interferón", "proteína que avisa a las células que hay un virus"), ("respuesta innata", "defensa rápida y general, sin memoria")],
  worked=[
      ("Signos de inflamación", "Un corte en la rodilla se pone rojo, caliente e hinchado. ¿Qué respuesta del cuerpo es y por qué?", ["Son los signos de inflamación.", "Llega más sangre con defensas al lugar.", "Es parte de la barrera secundaria."], "Inflamación; llega más sangre con defensas"),
      ("Qué hacen los fagocitos", "Un macrófago rodea una E. coli. ¿Qué proceso ocurre?", ["El fagocito rodea al patógeno.", "Luego lo ingiere.", "Eso se llama fagocitosis."], "Fagocitosis"),
  ],
  mistakes=[
      ("Pensar que la fiebre siempre es dañina.", "Una fiebre moderada ayuda a las defensas, aunque se debe vigilar.", "Avisa a un adulto y consulta si es muy alta o dura varios días."),
      ("Creer que la respuesta innata recuerda al patógeno.", "No tiene memoria.", "La memoria es parte de la respuesta adaptativa."),
  ],
  rec=[
      ("¿La inflamación produce enrojecimiento, calor, hinchazón y dolor: verdadero o falso?", "Verdadero", "Esos son sus cuatro signos."),
      ("¿Qué células se comen a los patógenos: los fagocitos o las neuronas?", "Los fagocitos", "Son glóbulos blancos."),
      ("¿La temperatura de 38,5 °C es fiebre o temperatura normal? (La fiebre es sobre 38 °C.)", "Fiebre", "Supera 38 °C."),
  ],
  und=[
      ("¿Por qué una herida inflamada se ve roja y caliente? A) Porque llega más sangre con defensas; B) Porque la piel se cubre de bacterias.", "A", "Más sangre da el color y el calor."),
      ("¿Qué hacen los interferones? A) Avisan a otras células que hay un virus; B) Se comen a las bacterias.", "A", "Alertan a las células vecinas."),
      ("La respuesta innata, ¿es específica para cada patógeno o general?", "General", "No distingue qué patógeno es."),
  ],
  app=[
      ("Cuatro personas tienen temperaturas de 36,8; 37,5; 38,4 y 39,0 °C. ¿Cuántas tienen fiebre (sobre 38 °C)?", "2", "Son 38,4 y 39,0."),
      arith("Datos de ejemplo: antes de una infección había 500 fagocitos por mm³ de sangre y durante la infección hubo 4 veces más. ¿Cuántos hay durante la infección?", "500*4", "Se multiplica por 4."),
      ("Una persona tiene hinchazón, calor y dolor en un dedo después de una astilla. ¿Qué barrera actúa? A) La secundaria; B) La terciaria.", "A", "La inflamación es parte de la respuesta innata."),
  ],
  rea=[
      ("Un recuento de ejemplo muestra 6.000 glóbulos blancos por mm³ en una persona sana y 14.000 en una persona con una infección. ¿Cuántos más hay en la persona con infección?", "8.000", "14.000 − 6.000 = 8.000: llegan más defensas."),
      ("¿Por qué se dice que la respuesta innata es rápida pero poco específica?", "Porque actúa en horas contra cualquier patógeno", "No requiere reconocer al patógeno."),
  ],
  cha=[
      ("Un niño tiene 38,2 °C por una infección y se siente bien. ¿Qué conviene? A) Avisar a un adulto y consultar si sigue o sube; B) Esperar sin avisar.", "A", "Es una señal que debe vigilarse."),
      ("Explica con tus palabras por qué la fiebre puede ayudar.", "Porque retarda a los microorganismos y acelera las defensas", "Es un efecto de la respuesta innata."),
  ],
  context=[("Dato de ejemplo. Un termómetro marca 37,2 °C el lunes, 38,6 °C el martes y 37,0 °C el miércoles. ¿Cuántos grados bajó del martes al miércoles?", "1,6", "38,6 − 37,0 = 1,6 °C.")],
  selfcheck=[("¿Qué es la inflamación?", "Una respuesta con enrojecimiento, calor, hinchazón y dolor", "Llega más sangre con defensas."), ("¿Qué es la fagocitosis?", "El proceso por el que un fagocito se come un patógeno", "Es una defensa innata."), ("¿Tiene memoria la respuesta innata?", "No", "La memoria es de la adaptativa.")],
  open_task=task("Dibuja una herida con un patógeno entrando. Marca: la inflamación, un fagocito y una flecha de la sangre que lleva defensas. Escribe tres frases que expliquen qué pasa en las dos primeras horas.", "Dibujo con herida, fagocito rodeando una bacteria y flechas. Frases: llega más sangre; el lugar se enrojece y se hincha; los fagocitos se comen a las bacterias.", ["dibujo con tres elementos", "tres frases", "usa los términos de la clase"], ["dibujo y frases"], ["decir que los fagocitos fabrican anticuerpos", "no mencionar la sangre"], "Pregunta qué pasaría si no llegaran más defensas."),
  reinforce="Escribe los cuatro signos de la inflamación.",
  extend="Explica por qué la respuesta innata no basta para todas las infecciones.")

L(OA4, 3,
  materials="Este cuaderno y lápiz. Los datos son ficticios.",
  use="Aprenderé la respuesta adaptativa o terciaria: linfocitos, anticuerpos y memoria. Sirve para entender cómo el cuerpo reconoce a un patógeno específico.",
  prior=["Sé qué hace la respuesta innata.", "Sé que un virus y una bacteria son patógenos distintos."],
  explain=[
      "La barrera terciaria o respuesta adaptativa reconoce a un patógeno específico. Cada patógeno tiene antígenos, moléculas que el sistema inmune detecta como extrañas. Los linfocitos B producen anticuerpos, proteínas que se unen a un antígeno determinado y lo marcan o bloquean. Los linfocitos T colaboran: unos coordinan la respuesta y otros destruyen las células del cuerpo que ya están infectadas por un virus.",
      "Esta respuesta es más lenta, porque debe reconocer al patógeno y fabricar muchos linfocitos: tarda varios días. A cambio es específica y deja células de memoria, que recuerdan al antígeno. Si el mismo patógeno vuelve, la respuesta es más rápida y fuerte.",
      "Por ejemplo, contra el virus de la gripe se producen anticuerpos que bloquean al virus y linfocitos T que destruyen las células infectadas. Contra E. coli, los anticuerpos marcan a la bacteria para que los fagocitos la destruyan. Las tres barreras trabajan juntas: la primera impide la entrada, la segunda actúa pronto y la tercera ataca de forma específica.",
  ],
  vocab=[("antígeno", "molécula del patógeno que el sistema inmune reconoce como extraña"), ("anticuerpo", "proteína que se une a un antígeno y lo bloquea o marca"), ("linfocito B", "célula que fabrica anticuerpos"), ("linfocito T", "célula que coordina o destruye células infectadas"), ("célula de memoria", "linfocito que recuerda un antígeno")],
  worked=[
      ("Quién hace qué", "¿Qué célula fabrica anticuerpos y qué célula destruye células infectadas por un virus?", ["Los linfocitos B fabrican anticuerpos.", "Los linfocitos T destruyen células infectadas."], "Linfocitos B fabrican anticuerpos; linfocitos T destruyen las células infectadas"),
      ("Específico o general", "Un anticuerpo contra el virus de la gripe, ¿sirve para E. coli?", ["Cada anticuerpo se une a un antígeno determinado.", "El virus y la bacteria tienen antígenos distintos."], "No, es específico"),
  ],
  mistakes=[
      ("Pensar que un anticuerpo sirve contra cualquier patógeno.", "Cada anticuerpo reconoce un antígeno particular.", "Piensa en una llave y una cerradura."),
      ("Creer que la respuesta adaptativa es instantánea.", "Tarda varios días la primera vez.", "Por eso la primera infección puede durar días."),
  ],
  rec=[
      ("¿Qué célula fabrica anticuerpos: el linfocito B o el linfocito T?", "El linfocito B", "El linfocito B produce anticuerpos."),
      ("¿Qué es un antígeno: una molécula que el sistema inmune reconoce como extraña o un anticuerpo?", "Una molécula que el sistema inmune reconoce como extraña", "El anticuerpo se une a ella."),
      ("¿La respuesta adaptativa es específica o general?", "Específica", "Reconoce un antígeno determinado."),
  ],
  und=[
      ("¿Qué hacen algunos linfocitos T? A) Destruyen células infectadas; B) Fabrican anticuerpos.", "A", "Los anticuerpos los fabrican los B."),
      ("¿Para qué sirven las células de memoria? A) Para responder más rápido si el patógeno vuelve; B) Para fabricar fiebre.", "A", "Recuerdan el antígeno."),
      ("Un anticuerpo contra la gripe, ¿protege contra E. coli: sí o no?", "No", "Cada anticuerpo es específico."),
  ],
  app=[
      arith("Una persona tarda 7 días en generar anticuerpos en su primera infección. Si la segunda vez tarda 3 días, ¿cuántos días menos tarda?", "7-3", "Se resta el tiempo de la segunda respuesta."),
      ("Ordena: (a) los linfocitos B fabrican anticuerpos, (b) el sistema reconoce el antígeno, (c) los anticuerpos se unen al patógeno. ¿Qué letra va primero?", "b", "Primero se reconoce el antígeno."),
      ("Los anticuerpos se unen a E. coli para que los fagocitos la destruyan. ¿Qué barrera trabaja con la terciaria? A) La secundaria, por los fagocitos; B) Solo la primaria.", "A", "Los fagocitos son parte de la respuesta innata."),
  ],
  rea=[
      ("¿Por qué la primera vez que enfermas de gripe tardas varios días en mejorar? Responde en una frase.", "Porque la respuesta específica tarda en reconocer al virus y fabricar anticuerpos", "La adaptativa es más lenta."),
      ("¿Por qué las células de memoria no sirven contra un patógeno que nunca estuvo en el cuerpo?", "Porque recuerdan solo antígenos ya conocidos", "Cada célula de memoria es específica."),
  ],
  cha=[
      ("Modelo de ejemplo: en la primera infección la cantidad de anticuerpos llega a un máximo de 10 unidades al día 14. En la segunda, a 80 unidades al día 5. ¿Cuántas veces mayor es el máximo?", "8", "80 ÷ 10 = 8."),
      ("En el modelo anterior, ¿en cuántos días menos se alcanza el máximo la segunda vez?", "9", "14 − 5 = 9."),
  ],
  context=[("Dato de ejemplo. Un virus tiene 3 antígenos distintos y una persona tiene un anticuerpo para cada uno. ¿Cuántos tipos de anticuerpo tiene?", "3", "Uno para cada antígeno.")],
  selfcheck=[("¿Qué es un antígeno?", "Una molécula del patógeno reconocida como extraña", "El anticuerpo se une a ella."), ("¿Qué hacen los linfocitos B?", "Fabrican anticuerpos", "Son parte de la respuesta adaptativa."), ("¿Qué dejan las células de memoria?", "Un recuerdo del antígeno para responder más rápido", "Por eso la segunda vez es más rápido.")],
  open_task=task("Dibuja una línea con tres etapas contra el virus de la gripe: (1) barrera primaria, (2) respuesta innata, (3) respuesta adaptativa. Escribe una célula o estructura de cada etapa y el efecto que produce.", "1 Moco con cilios: atrapa el virus. 2 Fagocitos e interferones: destruyen virus y avisan a células. 3 Linfocitos B y T: anticuerpos y destrucción de células infectadas.", ["tres etapas", "una estructura por etapa", "efecto correcto"], ["línea de tiempo rotulada"], ["poner anticuerpos en la etapa 1", "olvidar la memoria"], "Pregunta qué quedó guardado después de la etapa 3."),
  reinforce="Escribe qué hace un anticuerpo con un antígeno.",
  extend="Explica por qué la respuesta adaptativa se llama «específica».")

L(OA4, 4,
  materials="Este cuaderno y lápiz. Los gráficos son datos de ejemplo escritos en los ejercicios.",
  use="Aprenderé cómo las vacunas aprovechan la memoria inmunológica y por qué se usan contra la influenza y la meningitis. Sirve para entender por qué vacunarse protege a una persona y a su comunidad.",
  prior=["Sé que los anticuerpos son específicos.", "Sé que las células de memoria responden más rápido."],
  explain=[
      "Una vacuna contiene una versión inofensiva de un patógeno, como un virus debilitado o inactivado, o fragmentos suyos. No causa la enfermedad, pero el sistema inmune reconoce el antígeno y forma células de memoria. Si más tarde llega el patógeno real, la respuesta es rápida y fuerte.",
      "Hay vacunas contra infecciones comunes. La de la influenza se aplica cada año, porque el virus cambia y las variedades nuevas no son reconocidas por la memoria anterior. Las vacunas contra la meningitis protegen contra bacterias como el meningococo y el neumococo, que pueden causar infecciones graves en las membranas del cerebro. Chile las incluye en el Programa Nacional de Inmunizaciones según edad y riesgo.",
      "Cuando muchas personas están vacunadas, el patógeno circula menos y protege también a quienes no pueden vacunarse, como los recién nacidos; eso se llama inmunidad de la comunidad. Después de vacunarse, es normal un poco de dolor en el brazo o fiebre leve, que muestran que el sistema inmune trabaja. Una reacción fuerte o que preocupa debe consultarse, avisando de inmediato a una persona adulta.",
  ],
  vocab=[("vacuna", "preparado que enseña al sistema inmune a reconocer un patógeno sin causar la enfermedad"), ("memoria inmunológica", "capacidad de responder más rápido a un patógeno conocido"), ("inmunidad de la comunidad", "protección que se logra cuando muchas personas están vacunadas"), ("inactivado", "patógeno muerto o fragmentado que no puede causar enfermedad"), ("refuerzo", "dosis adicional que mantiene la memoria")],
  worked=[
      ("Cómo actúa una vacuna", "¿Qué hace una vacuna con el sistema inmune y por qué no causa la enfermedad?", ["Contiene una versión inofensiva del patógeno.", "El sistema inmune reconoce el antígeno.", "Forma células de memoria."], "Entrena al sistema inmune sin causar la enfermedad"),
      ("Por qué cada año", "¿Por qué se aplica la vacuna contra la influenza cada año?", ["El virus cambia.", "La memoria anterior puede no reconocer la nueva variedad.", "La vacuna se actualiza."], "Porque el virus cambia"),
  ],
  mistakes=[
      ("Creer que la vacuna da la enfermedad.", "Contiene versiones inofensivas o fragmentos.", "La fiebre leve es una respuesta, no la enfermedad."),
      ("Pensar que vacunarse solo protege a uno mismo.", "También reduce la circulación del patógeno.", "Piensa en la protección de la comunidad."),
  ],
  rec=[
      ("¿Qué forma una vacuna en el cuerpo: células de memoria o fiebre alta?", "Células de memoria", "Permiten una respuesta rápida."),
      ("¿Se aplica la vacuna de la influenza cada año: verdadero o falso?", "Verdadero", "El virus cambia."),
      ("¿La vacuna contra la meningitis protege contra bacterias como el meningococo: sí o no?", "Sí", "Es una de sus funciones."),
  ],
  und=[
      ("¿Cuál es la ventaja de la segunda exposición con memoria? A) La respuesta es más rápida y fuerte; B) La respuesta es igual de lenta que la primera vez.", "A", "La memoria acelera la defensa."),
      ("¿Qué es la inmunidad de la comunidad? A) La protección que se logra cuando muchas personas están vacunadas; B) La inmunidad de un solo órgano.", "A", "Beneficia a quienes no pueden vacunarse."),
      ("Un dolor leve en el brazo después de la vacuna, ¿es normal o es la enfermedad?", "Es normal", "Muestra que el sistema inmune trabaja."),
  ],
  app=[
      arith("Datos de ejemplo: sin vacuna, la respuesta de anticuerpos alcanza 10 unidades tras 14 días; con vacuna y exposición, 90 unidades tras 5 días. ¿Cuántas unidades más hay con vacuna?", "90-10", "Se resta."),
      arith("En un curso ficticio de 40 estudiantes, 34 están vacunados. ¿Cuántos no lo están?", "40-34", "Se resta."),
      arith("Con esos 40 estudiantes y 34 vacunados, ¿qué porcentaje del curso está vacunado?", "34*100//40", "Se multiplica por 100 y se divide entre el total.", " %"),
  ],
  rea=[
      ("Un compañero dice: «No me vacuno porque las defensas se acostumbran a todo». Corrígelo en una frase.", "Las vacunas entrenan a las defensas para reconocer un patógeno concreto", "La vacuna forma memoria."),
      ("¿Por qué un recién nacido se beneficia de que su entorno esté vacunado?", "Porque hay menos circulación del patógeno", "Es la inmunidad de la comunidad."),
  ],
  cha=[
      ("Una persona tuvo meningitis bacteriana antes de vacunarse contra el neumococo. ¿Qué conclusión es válida? A) La vacuna puede ayudar a prevenir casos futuros; B) La vacuna cura la meningitis ya declarada.", "A", "Las vacunas previenen, no curan."),
      ("En un gráfico de ejemplo, la respuesta del segundo contacto es 8 veces mayor que la del primero. Explica con la palabra «memoria» por qué ocurre.", "Porque las células de memoria reconocen el antígeno y responden más rápido", "Es el efecto de la memoria inmunológica."),
  ],
  context=[("Dato de ejemplo. Un colegio ficticio tiene 120 estudiantes en 7.º y 8.º; 96 se vacunaron contra la influenza este año. ¿Cuántos no?", "24", "120 − 96 = 24.")],
  selfcheck=[("¿Qué contiene una vacuna?", "Una versión inofensiva del patógeno o fragmentos suyos", "No causa la enfermedad."), ("¿Por qué la vacuna de la gripe se aplica cada año?", "Porque el virus cambia", "La memoria anterior puede no servir."), ("¿Qué es la inmunidad de la comunidad?", "La protección que se logra cuando muchas personas están vacunadas", "Protege a quien no puede vacunarse.")],
  open_task=task("Escribe un afiche de tres frases dirigido a tu curso para explicar por qué conviene vacunarse contra la influenza. Incluye: qué hace la vacuna, por qué se aplica cada año y a quién más protege.", "Una vacuna enseña a tus defensas a reconocer el virus sin causar la enfermedad. Se aplica cada año porque el virus cambia. También protege a quienes no pueden vacunarse.", ["tres ideas", "explicación correcta", "lenguaje claro"], ["afiche de tres frases"], ["decir que la vacuna produce la gripe", "decir que cura"], "Pregunta qué dudas tendría un compañero."),
  reinforce="Escribe una frase que explique qué es la memoria inmunológica.",
  extend="Explica por qué una vacuna no sirve para curar una infección ya declarada.")

L(OA4, 5,
  materials="Este cuaderno y lápiz. Los casos son inventados.",
  use="Aprenderé a integrar las tres barreras y a explicar las alergias, las enfermedades autoinmunes y el rechazo de trasplantes como alteraciones de la respuesta inmune. Sirve para explicar el sistema inmune con un modelo y reconocer sus límites.",
  prior=["Sé que hay tres barreras defensivas.", "Sé que la respuesta adaptativa reconoce antígenos."],
  explain=[
      "El sistema inmune suele funcionar bien, pero a veces su respuesta se altera. En una alergia el sistema reacciona de forma exagerada ante una sustancia inofensiva, como polen o ciertos alimentos. Libera histamina, que produce picazón, estornudos o hinchazón. Una reacción alérgica grave, con dificultad para respirar, es una emergencia médica.",
      "En una enfermedad autoinmune el sistema inmune ataca por error a células del propio cuerpo. Ejemplos son la diabetes tipo 1 (el ataque es contra las células que fabrican insulina), la artritis reumatoide y el lupus. En un rechazo de trasplante, el sistema inmune reconoce un órgano trasplantado como extraño y lo ataca; por eso se usan medicamentos que bajan la respuesta, pero esas personas tienen más riesgo de infecciones.",
      "Un modelo del sistema inmune puede ser un fuerte con tres anillos: murallas (barrera primaria), guardias que atacan a cualquiera (secundaria) y especialistas con memoria (terciaria). El modelo ayuda a explicar, pero no es una copia literal: no muestra las moléculas, ni los tiempos, ni que las barreras se mezclan.",
  ],
  vocab=[("alergia", "reacción exagerada a una sustancia inofensiva"), ("histamina", "sustancia que produce picazón e hinchazón en la alergia"), ("autoinmune", "enfermedad en que el sistema inmune ataca al propio cuerpo"), ("rechazo", "ataque del sistema inmune a un órgano trasplantado"), ("modelo", "representación simple de un fenómeno, con límites")],
  worked=[
      ("Clasificar la alteración", "A) Una persona estornuda y le pica la nariz por el polen; B) El sistema inmune ataca las células del propio cuerpo que fabrican insulina. ¿Cuál es alergia y cuál autoinmune?", ["A reacciona a polen, que es inofensivo.", "B ataca células propias."], "A es alergia; B es autoinmune"),
      ("Límite de un modelo", "El modelo del fuerte con tres anillos, ¿qué no muestra?", ["No muestra las moléculas.", "Tampoco que las barreras se mezclan."], "No muestra moléculas ni la mezcla de las barreras"),
  ],
  mistakes=[
      ("Creer que una alergia es una infección.", "Es una reacción a una sustancia inofensiva, no a un patógeno.", "Pregunta si hay un patógeno."),
      ("Pensar que el modelo es igual a la realidad.", "Los modelos simplifican.", "Declara sus límites."),
  ],
  rec=[
      ("¿La alergia es una reacción exagerada a una sustancia inofensiva: verdadero o falso?", "Verdadero", "Es su definición."),
      ("¿Qué sustancia produce picazón e hinchazón en una alergia: la histamina o la insulina?", "La histamina", "La libera el sistema inmune."),
      ("¿La diabetes tipo 1 es un ejemplo de enfermedad autoinmune: sí o no?", "Sí", "El sistema inmune ataca las células que fabrican insulina."),
  ],
  und=[
      ("En un trasplante, ¿por qué puede haber rechazo? A) El sistema inmune reconoce al órgano como extraño; B) El órgano trasplantado siempre llega con una infección.", "A", "Lo reconoce como extraño."),
      ("¿Qué diferencia hay entre alergia y enfermedad autoinmune? A) La alergia reacciona a algo externo inofensivo; la autoinmune ataca al propio cuerpo; B) La alergia ataca al propio cuerpo y la autoinmune reacciona al polen.", "A", "El blanco del ataque es distinto."),
      ("¿Para qué se usan en un trasplante los medicamentos que bajan la respuesta inmune?", "Para evitar el rechazo", "Reducen el ataque al órgano."),
  ],
  app=[
      ("Tres situaciones: (1) estornudos por polen, (2) ataque a las articulaciones por el propio sistema inmune, (3) un riñón trasplantado es atacado. ¿Cuántas son autoinmunes?", "1", "Solo la 2; la 1 es alergia y la 3 es rechazo."),
      ("Clasifica: «El sistema inmune ataca las células de la piel porque las reconoce como extrañas». ¿Alergia, autoinmune o rechazo?", "Autoinmune", "Ataca células propias."),
      ("Una persona con alergia a un alimento desarrolla dificultad para respirar. ¿Qué debe hacerse? A) Avisar de inmediato a un adulto y pedir ayuda médica; B) Esperar a ver si pasa.", "A", "Es una emergencia."),
  ],
  rea=[
      ("Una persona con trasplante toma medicamentos que bajan sus defensas. ¿Qué riesgo aumenta? Responde en una frase.", "El riesgo de infecciones", "Tiene menos defensas contra patógenos."),
      ("¿Por qué una alergia no es una infección? Responde en una frase.", "Porque no hay patógeno: la sustancia es inofensiva", "El problema es la reacción exagerada."),
  ],
  cha=[
      ("Un modelo representa el sistema inmune como un fuerte. Escribe un límite del modelo.", "No muestra moléculas, tiempos ni que las barreras se mezclan", "Un modelo simplifica."),
      ("Explica con el modelo de los tres anillos cuál anillo está activo cuando la fiebre sube y cuál cuando se forman anticuerpos.", "Fiebre: secundaria; anticuerpos: terciaria", "La fiebre es innata; los anticuerpos son adaptativos."),
  ],
  context=[("Dato de ejemplo. En un curso de 36 estudiantes, 9 declararon alguna alergia. ¿Cuántos no tienen alergia declarada?", "27", "36 − 9 = 27.")],
  selfcheck=[("¿Qué es una alergia?", "Una reacción exagerada a una sustancia inofensiva", "No hay patógeno."), ("¿Qué ataca el sistema inmune en una enfermedad autoinmune?", "Células del propio cuerpo", "Es un error del sistema."), ("¿Qué es el rechazo de un trasplante?", "El ataque del sistema inmune a un órgano que reconoce como extraño", "Se previene con medicamentos.")],
  open_task=task("Construye una tabla con tres columnas (situación, qué hace el sistema inmune, tipo de alteración) para estos tres casos inventados: polen que produce estornudos; ataque a las articulaciones; riñón trasplantado atacado. Escribe además un límite de tu modelo de tres anillos.", "Polen: reacciona a algo inofensivo; alergia. Articulaciones: ataca células propias; autoinmune. Riñón: ataca órgano extraño; rechazo. Límite: no muestra moléculas ni tiempos.", ["tres filas correctas", "tipos bien asignados", "un límite del modelo"], ["tabla y una frase"], ["confundir alergia con infección", "decir que el modelo es la realidad"], "Pregunta cómo explicaría el rechazo a un compañero."),
  reinforce="Escribe una diferencia entre alergia y enfermedad autoinmune.",
  extend="Explica por qué las personas trasplantadas deben cuidarse más de las infecciones.")
