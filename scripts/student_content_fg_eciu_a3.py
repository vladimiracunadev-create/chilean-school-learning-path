"""Educación Ciudadana 3.º medio FG: OA 05 (defensa y exigibilidad de los derechos humanos) y OA 06 (participación, bien común y tradiciones políticas). Casos de ejemplo inventados."""
from __future__ import annotations

from fg_eciu_common import build

O5 = "FG-ECIU-3M-OAC-05"
O6 = "FG-ECIU-3M-OAC-06"

# ============================================================ OA 05, clase 1
F = ("Ficha 21 (casos de ejemplo): (1) A un joven con silla de ruedas no lo dejan entrar a una sala del liceo porque no hay rampa. "
     "(2) Una estudiante migrante recibe burlas por su acento y el profesor lo permite. "
     "(3) Un vecino pide que se respete su derecho a opinar en una reunión, pero otro dice que «ese derecho solo lo tienen quienes pagan cuotas».")
build(
    O5, 1, F,
    use="Aprenderé qué son los derechos humanos, qué significan sus principios (universalidad, indivisibilidad, inalienabilidad, igualdad y no discriminación) y cómo se reconocen en la vida cotidiana.",
    prior=["Sé qué son las libertades fundamentales.", "Sé que el Estado tiene deberes frente a los derechos.", "Sé qué es discriminar."],
    explain=[
        "Los derechos humanos son derechos que tiene toda persona por el solo hecho de serlo. Se apoyan en la dignidad humana y están reconocidos en tratados internacionales, como la Declaración Universal de Derechos Humanos, y en las constituciones. Incluyen derechos civiles y políticos (por ejemplo, expresarse y votar) y derechos económicos, sociales y culturales (por ejemplo, educación y salud).",
        "Se sustentan en cinco principios. Universalidad: son de todas las personas, sin excepción. Indivisibilidad: los derechos se relacionan entre sí y no se pueden separar ni jerarquizar. Inalienabilidad: no se pueden perder ni ceder. Igualdad: todas las personas valen lo mismo. No discriminación: nadie puede ser tratado peor por su origen, sexo, discapacidad, religión u otra condición.",
        "En la vida cotidiana se reconocen preguntando quién está quedando fuera o recibiendo un trato peor sin una razón válida. Reconocer un derecho implica también exigirlo con medios pacíficos: informar, reclamar ante las instancias y apoyar a quien es afectado. Si ves una situación de discriminación o violencia, lo prudente es avisar a una persona adulta de confianza.",
    ],
    vocab=[("derechos humanos", "derechos que toda persona tiene por ser persona, basados en la dignidad"), ("universalidad", "principio según el cual los derechos corresponden a todas las personas"), ("indivisibilidad", "principio según el cual los derechos están relacionados y no se separan"), ("inalienabilidad", "principio según el cual los derechos no se pueden perder ni ceder"), ("discriminación", "trato peor a una persona por una condición, sin razón válida")],
    worked=[
        ("Identificar un principio", "En un club de ejemplo, un socio dice: «Los derechos de mi grupo valen más que los de los demás». ¿Qué principio se vulnera?", ["Se pone a unas personas por sobre otras.", "Eso contradice la igualdad."], "Igualdad"),
        ("Relacionar derechos", "Una niña de ejemplo falta a clases por falta de atención médica. ¿Qué derechos se relacionan?", ["Salud y educación se afectan entre sí.", "Eso muestra la indivisibilidad."], "Salud y educación; indivisibilidad"),
    ],
    mistakes=[("Pensar que los derechos humanos dependen de que la persona los cumpla todos.", "Son inalienables: no se pierden ni se ceden.", "Distingue derechos de deberes y de sanciones por una falta."),
              ("Creer que son solo derechos para quienes cometen delitos o para un grupo.", "Son universales y protegen a todas las personas.", "Pregunta si corresponde a toda persona.")],
    T=[
        ('abc', '¿Qué significa la universalidad de los derechos humanos?', 'Que los derechos corresponden a todas las personas, sin excepción', 'Que solo se aplican a quienes los conocen y los piden', 'Que cada comunidad decide a quiénes se aplican', 'Los derechos humanos se tienen por ser persona; no dependen de conocerlos, pedirlos ni de la decisión de un grupo.'),
        ('abc', '¿Qué significa la inalienabilidad?', 'Que los derechos no se pueden perder ni ceder', 'Que pueden venderse si la persona está de acuerdo', 'Que se pierden si la persona incumple una ley', 'Inalienable es lo que no se puede quitar ni transferir; una falta puede sancionarse, pero no anula los derechos.'),
        ('abc', '¿Qué significa la indivisibilidad?', 'Que los derechos están relacionados y no se pueden separar ni jerarquizar', 'Que cada persona tiene derechos individuales distintos', 'Que algunos derechos valen más y deben cumplirse primero', 'Los derechos se apoyan unos a otros; no se puede cumplir uno a costa de otro.'),
        ('abc', '{F} ¿Qué principio se vulnera en el caso 1?', 'No discriminación, porque al joven se le excluye por su discapacidad', 'Inalienabilidad, porque se le quita un derecho que puede perderse', 'Universalidad, porque sus derechos no valen en el liceo', 'No poder entrar por falta de rampa es un trato desigual por una condición, sin razón válida.'),
        ('abc', '{F} ¿Qué principio se contradice con mayor claridad cuando el vecino dice que solo opinan quienes pagan cuotas?', 'Universalidad, porque pone un requisito de pago a un derecho de todos', 'Indivisibilidad, porque separa el derecho a opinar de los demás derechos', 'Inalienabilidad, porque obliga a ceder el derecho a cambio de una cuota', 'Un derecho humano no depende de un pago: corresponde a todas las personas.'),
        ('abc', '{F} ¿Qué principios se contradicen en el caso 2?', 'Igualdad y no discriminación, por el trato peor', 'Indivisibilidad, porque separa unos derechos de otros', 'Inalienabilidad, porque se le quita un derecho que no se puede perder', 'Se trata peor a la estudiante por su acento y el profesor lo permite, lo que contradice la igualdad.'),
        ('abc', '{F} En el caso 1, ¿qué derecho se relaciona con la falta de rampa?', 'El derecho a la educación y a participar en igualdad', 'La libertad de asociación, por no poder organizarse con otros', 'El derecho a elegir autoridades, por no poder votar en el liceo', 'No poder ingresar a una sala afecta su acceso a la educación.'),
        ('abc', '{F} ¿Qué haría un estudiante prudente ante el caso 2?', 'Acompañar a la compañera y avisar a una persona adulta de confianza', 'Reírse para no quedar fuera del grupo y evitar problemas con los demás', 'No hacer nada porque el profesor ya lo permite y es mejor no meterse', 'Se busca apoyar a la persona afectada y pedir ayuda a alguien con responsabilidad.'),
        ('abc', '{F} Alguien dice: «Un derecho vale más que otro, así que podemos ignorar los menos importantes». ¿Qué principio contradice?', 'Indivisibilidad, porque los derechos no se jerarquizan', 'Universalidad, porque los derechos son de todos', 'Igualdad, porque todos valen lo mismo', 'La indivisibilidad afirma que los derechos se relacionan y no se separan.'),
        ('abc', '{F} Un compañero dice: «Si cometes una falta, pierdes tus derechos humanos». ¿Qué corresponde?', 'Aclarar que son inalienables, aunque puede haber sanciones legales', 'Aceptarlo, porque quien incumple deja de tener derechos', 'Decir que las sanciones tampoco existen', 'Se pueden sancionar conductas, pero la dignidad y los derechos de la persona se mantienen.'),
        ('abc', '{F} ¿Cuál es una forma pacífica de exigir un derecho?', 'Informar y presentar un reclamo ante la instancia que corresponde', 'Amenazar con difundir fotos hasta que se cumpla lo que se exige', 'Esperar a que otra persona lo haga primero para no tener problemas', 'Es un camino legítimo que respeta los derechos de los demás.'),
        ('abc', '{F} ¿Qué medida resuelve el caso 1 de forma estable?', 'Construir una rampa y fijar normas de accesibilidad', 'Pedirle que use otra sala sin explicarle por qué', 'Ayudarlo a subir cada vez que haya clase', 'Elimina la barrera de forma permanente en lugar de depender de la ayuda de otros.'),
        ('abc', '¿Cuál es un ejemplo de derecho económico, social y cultural?', 'La educación, que es un bien social', 'Votar, que es una acción política', 'Expresar una opinión, que es una libertad civil', 'Votar y expresarse son derechos civiles y políticos; la educación es un derecho social.'),
    ],
    ctx=('abc', 'En un liceo de ejemplo se le niega a una estudiante la inscripción a un taller por el país de origen de su familia. ¿Qué principio está en juego?', 'No discriminación', 'Indivisibilidad', 'Inalienabilidad', 'Se trata peor a una persona por su origen, sin una razón válida.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es la discriminación?', 'Un trato peor a una persona por una condición, sin razón válida', 'Por ejemplo, por su origen, discapacidad o religión.'),
        ('abc', '¿Qué son los derechos humanos?', 'Derechos que toda persona tiene por ser persona', 'Derechos que otorga el Estado a quienes cumplen sus deberes', 'Beneficios que dependen de la edad de cada persona', 'Se apoyan en la dignidad humana, no en una concesión del Estado.'),
        ('abc', '¿Cuál es un ejemplo de derecho civil y político?', 'Votar', 'Recibir educación', 'Atención de salud', 'Votar es un derecho político; educación y salud son derechos sociales.'),
    ],
    op=("Con la {F} escribe una tabla para los tres casos: derecho afectado, principio que se contradice y una acción pacífica para exigirlo. Agrega una frase sobre a quién avisarías en tu liceo (por ejemplo, una persona adulta de confianza).",
        "Caso 1: educación e inclusión; no discriminación; solicitar una rampa. Caso 2: dignidad; igualdad; conversar con el profesor y avisar a una persona adulta. Caso 3: libertad de expresión; universalidad; pedir que se respete la palabra de todos. Aviso: a la orientadora o a un profesor de confianza.",
        ["relaciona derecho y principio", "propone acción pacífica", "incluye avisar a una persona adulta"], ["tabla de tres casos", "frase final"], ["usar la violencia", "confundir derecho con deber"],
        "Pregunta qué principio sería más difícil de defender en su entorno."),
    reinforce="Explica con tus palabras los cinco principios y da un ejemplo de cada uno.",
    extend="Anota una situación de tu entorno donde alguien podría quedar fuera y cómo se podría incluir.",
)

# ============================================================ OA 05, clase 2
F = ("Ficha 22 (caso de ejemplo): en el liceo ficticio San Marcos, la profesora Rojas dejó fuera de una actividad deportiva a Tomás por su discapacidad motora, sin ofrecerle una forma de participar. "
     "Tomás y su familia hablaron con la orientadora; después enviaron una carta al director. Fuentes: (1) la carta de la familia; (2) el reglamento del liceo, que dice que todos los estudiantes deben participar en igualdad con los ajustes necesarios; "
     "(3) la respuesta del director, que reconoce el problema y promete una reunión en 10 días hábiles.")
build(
    O5, 2, F,
    use="Aprenderé a investigar un caso de derechos humanos en la vida cotidiana: qué derecho está en juego, qué instancias existen para defenderlo y cómo se exige.",
    prior=["Sé los principios de los derechos humanos.", "Sé comparar fuentes.", "Sé qué es una norma interna."],
    explain=[
        'Defender un derecho significa protegerlo; exigirlo significa reclamar que se cumpla. Hay varias instancias. En lo cercano: conversar con quien corresponde, con orientación o con el centro de estudiantes. En lo institucional: presentar un reclamo escrito a la dirección y pedir una respuesta con plazo. En lo externo: acudir a instituciones públicas o a tribunales si no se resuelve. Los días hábiles son los días en que una institución funciona con normalidad, de lunes a viernes sin feriados.',
        'Una buena investigación del caso identifica el derecho en juego (aquí, educación e igualdad), la norma que lo respalda (el reglamento), los hechos comprobables y los pasos ya dados. Se revisa si la respuesta de la institución repara el problema, no solo lo reconoce. También se protege la privacidad de la persona afectada.',
        'Los ajustes razonables son cambios concretos para que una persona pueda participar en igualdad, como adaptar una actividad. Un reclamo claro describe los hechos, nombra el derecho, pide una medida precisa y fija un plazo. Se escribe con respeto y sin acusar sin pruebas.',
    ],
    vocab=[("exigibilidad", "posibilidad real de reclamar que un derecho se cumpla"), ("ajuste razonable", "cambio concreto para que una persona participe en igualdad"), ("reclamo", "comunicación formal que pide corregir una situación"), ("instancia", "lugar o persona a quien se acude para resolver"), ("reparación", "medida que corrige el daño causado")],
    worked=[
        ("Redactar un pedido preciso", "Un grupo de ejemplo quiere que el patio tenga sombra. ¿Cuál pedido es más preciso: «arreglen el patio» o «instalen dos toldos antes del verano»?", ["El segundo dice qué y cuándo.", "El primero es vago."], "Instalen dos toldos antes del verano"),
        ("Reconocer un ajuste razonable", "Un estudiante de ejemplo con baja visión recibe el material en letra grande. ¿Qué es eso?", ["Es un cambio concreto.", "Le permite participar en igualdad."], "Un ajuste razonable"),
    ],
    mistakes=[("Quedarse solo con la promesa de reunión.", "Una promesa no repara el daño.", "Pide medidas concretas y plazos."),
              ("Publicar el nombre y el caso de la persona afectada para presionar.", "Se vulnera su privacidad.", "Usa el canal formal y cuida los datos.")],
    T=[
        ('abc', '¿Qué diferencia hay entre defender y exigir un derecho?', 'Defender es protegerlo; exigir es reclamar que se cumpla', 'Defender es reclamar ante un tribunal; exigir es conversar con la persona', 'Son lo mismo: pedir un favor a la autoridad', 'La clase distingue proteger el derecho de reclamar su cumplimiento.'),
        ('abc', '¿Qué orden de instancias propone la clase?', 'Conversar primero, luego un reclamo escrito a la dirección y después instituciones externas', 'Ir primero a los tribunales y después conversar con la dirección del liceo', 'Difundir el caso en redes antes de hablar con nadie en el liceo', 'Se parte por lo cercano y se avanza a lo institucional y lo externo si es necesario.'),
        ('abc', '{F} ¿Qué derecho está en juego en el caso?', 'Educación e igualdad de participación en el liceo', 'Derecho de propiedad sobre los materiales deportivos', 'Libertad de asociación de los estudiantes del curso', 'Se excluyó a Tomás de una actividad por su discapacidad.'),
        ('abc', '{F} ¿Qué fuente respalda el derecho de Tomás?', 'El reglamento del liceo, que exige participar en igualdad con ajustes', 'La respuesta del director, que promete una reunión en diez días hábiles', 'La carta de la familia, que relata los hechos ocurridos en la actividad', 'La norma que lo respalda es el reglamento; las otras fuentes cuentan lo ocurrido o prometen algo.'),
        ('abc', '{F} ¿Qué sería un ajuste razonable en este caso?', 'Adaptar la actividad para que Tomás participe en igualdad', 'Ofrecerle mirar la actividad desde la banca', 'Darle una nota por no participar', 'Un ajuste razonable es un cambio concreto que permite participar.'),
        ('abc', '{F} ¿Qué paso dio primero la familia?', 'Hablar con la orientadora', 'Acudir a un tribunal', 'Enviar una carta a una institución externa', 'La ficha indica que primero usaron una instancia cercana.'),
        ('abc', '{F} ¿Por qué la respuesta del director aún no repara el problema?', 'Porque reconoce el problema y promete una reunión, pero no fija una medida', 'Porque desconoce lo que dice el reglamento sobre la participación en igualdad', 'Porque rechaza el reclamo de la familia y no responde la carta enviada', 'Reconocer no es reparar: falta una medida que permita participar.'),
        ('=', '{F} Si la reunión es en 10 días hábiles y una semana tiene 5 días hábiles, ¿en cuántas semanas se realizaría?', '10//5', 'Se divide el plazo entre los días hábiles de cada semana.', ' semanas'),
        ('abc', '{F} ¿Qué debe incluir un buen reclamo?', 'Los hechos, el derecho en juego, una medida precisa y un plazo', 'Pedir sanciones para todas las personas involucradas', 'Contar la historia completa sin pedir nada concreto', 'Concretar la petición permite exigir su cumplimiento.'),
        ('abc', '{F} Un compañero propone publicar el nombre de Tomás en redes para presionar. ¿Qué se responde?', 'Cuidar su privacidad y usar los canales formales', 'Hacerlo, porque la presión pública acelera las respuestas', 'Hacerlo solo si Tomás no se entera', 'Se protege a la persona afectada y se prefieren vías formales y respetuosas.'),
        ('abc', '{F} Si pasan los 10 días hábiles y no hay respuesta, ¿qué corresponde?', 'Insistir por escrito y acudir a la instancia superior', 'Dar por terminado el reclamo, porque ya se cumplió el plazo', 'Esperar otros 10 días sin avisar y confiar en que responderán', 'La exigibilidad continúa si el derecho no se cumple.'),
        ('abc', '{F} ¿Qué dato falta para evaluar la respuesta del director?', 'Qué medida concreta tomará el liceo y en qué plazo', 'Cuántos estudiantes hay en el liceo y cuántos asistieron a la actividad', 'Qué deporte se practicaba y en qué lugar del liceo se realizó', 'Sin una medida concreta no se puede saber si hay reparación.'),
        ('abc', '{F} ¿Qué frase es más adecuada en el reclamo?', 'Solicitamos que se apliquen los ajustes del reglamento y que se fije una fecha', 'La profesora es discriminadora y debe ser despedida del liceo de inmediato', 'Exigimos que el director pida disculpas públicas hoy ante todo el liceo', 'Describe hechos y pide medidas precisas sin acusar sin pruebas.'),
    ],
    ctx=('abc', 'Una estudiante de ejemplo recibe un trato desigual en una evaluación. ¿Cuál es un buen primer paso?', 'Conversar con su profesor jefe o con una persona adulta de confianza', 'Publicar una crítica en redes sociales antes de hablar con nadie', 'Dejar de asistir a las evaluaciones hasta que cambien al profesor', 'Se busca resolver por una vía cercana y pacífica.'),
    sc=[
        ('¿Qué es la exigibilidad?', 'La posibilidad real de reclamar que un derecho se cumpla', 'Un derecho es exigible cuando existen vías para reclamarlo.'),
        ('abc', '¿Qué es un ajuste razonable?', 'Un cambio concreto que permite participar en igualdad', 'Una sanción para quien discrimina', 'Una excepción que libera a la persona de participar', 'Permite incluir a la persona en la actividad.'),
        ('En Educación Ciudadana: ¿Qué es una reparación?', 'Una medida que corrige el daño causado', 'Corrige lo ocurrido, no solo lo reconoce.'),
    ],
    op=("Con la {F} redacta un reclamo de cinco líneas dirigido al director: hechos, derecho, norma, medida pedida y plazo. Usa un tono respetuoso, sin acusar sin pruebas.",
        "Estimado director: el día de la actividad deportiva se excluyó a Tomás sin ofrecerle una forma de participar. Esto afecta su derecho a la educación y a la igualdad, que el reglamento reconoce. Solicitamos adaptar las actividades y que se nos informe la medida en 10 días hábiles. Agradecemos su respuesta.",
        ["hechos claros", "norma citada", "medida y plazo"], ["reclamo de cinco líneas"], ["tono acusatorio", "falta de medida"],
        "Pregunta a quién acudiría si no hay respuesta."),
    reinforce="Escribe un pedido preciso con qué y cuándo para mejorar algo en tu liceo.",
    extend="Averigua en el reglamento de tu liceo cómo se presenta un reclamo.",
)

# ============================================================ OA 05, clase 3
F = ("Ficha 23 (conflicto de derechos de ejemplo): la radio del liceo ficticio Los Nogales transmitió una broma sobre el acento de un compañero. "
     "Perspectiva 1 (locutor): «Es libertad de expresión; era una broma». "
     "Perspectiva 2 (compañero afectado): «Me dolió; se burlaron de mi origen frente a todo el liceo». "
     "Perspectiva 3 (docente a cargo): «La libertad de expresión tiene límites cuando se ofende la dignidad de otros; propongo una regla y una conversación». "
     "Dato de ejemplo: 12 personas escribieron para decir que sintieron la broma como ofensiva y 3 que no.")
build(
    O5, 3, F,
    use="Aprenderé a contrastar perspectivas cuando dos derechos parecen chocar, y a buscar una solución que respete la dignidad de todas las personas.",
    prior=["Sé los principios de los derechos humanos.", "Sé comparar perspectivas.", "Sé que las libertades pueden limitarse por ley para proteger a otros."],
    explain=[
        "A veces dos derechos parecen entrar en tensión, por ejemplo la libertad de expresión y el derecho a la honra o a no ser discriminado. Los derechos se interpretan juntos (indivisibilidad): ejercer uno no puede anular la dignidad de otras personas. Por eso la libertad de expresión no ampara burlas dirigidas a humillar a alguien por su origen.",
        "Para contrastar se pregunta: qué derecho invoca cada persona, qué daño se produjo, si hay intención de dañar o de informar y qué medida repara sin silenciar. La evidencia incluye hechos (qué se dijo), testimonios y la reacción de la comunidad. Un dato como «12 contra 3» no decide solo lo correcto: indica cómo fue recibido.",
        "Una buena respuesta repara y previene: pedir disculpas sinceras si corresponde, aclarar reglas, educar y evitar castigos desproporcionados. Se cuida también al locutor: un error se corrige con aprendizaje y no con humillación. Si hay riesgo para alguien, se avisa a una persona adulta de confianza.",
    ],
    vocab=[("honra", "buen nombre y dignidad de una persona frente a los demás"), ("ponderar", "pesar con cuidado los derechos en tensión para decidir"), ("desproporcionado", "excesivo respecto del daño o de la falta"), ("intención", "propósito con que se hace algo"), ("prevención", "medidas para que un daño no se repita")],
    worked=[
        ("Identificar derechos en tensión", "Un vecino de ejemplo cuelga un cartel ofensivo sobre su vecina. ¿Qué dos derechos entran en tensión?", ["Su libertad de expresión.", "La honra de su vecina."], "Libertad de expresión y honra"),
        ("Medida proporcionada", "Un estudiante de ejemplo se burló de otro. ¿Qué medida es más proporcionada: expulsarlo del liceo o pedirle disculpas y participar en una conversación?", ["La falta no justifica una sanción máxima.", "La segunda repara y previene."], "Disculpas y conversación"),
    ],
    mistakes=[("Usar la libertad de expresión como excusa para humillar.", "Los derechos se ejercen respetando la dignidad de otros.", "Pregunta si el mensaje daña a una persona por su condición."),
              ("Silenciar a alguien sin explicar la regla.", "Una medida injusta tampoco educa.", "Explica la norma y busca reparar.")],
    T=[
        ('abc', '¿Qué significa ponderar derechos?', 'Pesar con cuidado los derechos en tensión para decidir cómo respetarlos', 'Elegir el derecho que más personas prefieren y descartar el otro', 'Ignorar el derecho que menos se usa en la vida cotidiana', 'Ponderar exige considerar ambos derechos, no elegir uno al azar ni por votación.'),
        ('=', '{F} ¿Qué porcentaje de quienes escribieron sintió ofensiva la broma?', '12*100//15', 'Se compara la parte que la sintió ofensiva con el total de quienes escribieron (12 + 3).', ' %'),
        ('abc', '{F} ¿Qué derecho invoca el locutor?', 'Libertad de expresión', 'Derecho a la honra', 'Libertad de reunión', 'Dice que era libertad de expresión.'),
        ('abc', '{F} ¿Qué derecho reclama el compañero afectado?', 'Honra y no discriminación', 'Libertad de expresión', 'Libertad de asociación', 'Se burlaron de su origen frente a todo el liceo.'),
        ('abc', '{F} ¿Qué propone la docente?', 'Una regla clara y una conversación', 'Expulsar al locutor', 'Prohibir la radio por un mes', 'Su postura busca reparar y prevenir sin una medida desproporcionada.'),
        ('abc', '{F} ¿Qué indica el dato de 12 contra 3?', 'Cómo fue recibida la broma, sin decidir por sí solo qué es correcto', 'Que la mayoría decide qué es una broma aceptable para todos', 'Que el locutor quiso ofender, porque 12 personas lo sintieron así', 'Muestra la recepción de la comunidad, no la regla ni la intención.'),
        ('abc', '{F} ¿Qué medida sería desproporcionada?', 'Expulsar al locutor del liceo por una broma', 'Pedir disculpas sinceras al compañero afectado', 'Fijar una regla sobre burlas y conversar con el curso', 'Una medida es desproporcionada cuando excede la gravedad de la falta.'),
        ('abc', '{F} ¿Qué medida repara sin silenciar?', 'Disculpas sinceras, una regla clara sobre burlas y una conversación', 'Cerrar la radio del liceo hasta que se resuelva la situación', 'Prohibir toda broma en el liceo para evitar que se repita', 'Repara el daño y previene, sin eliminar la libertad de expresión.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'La libertad de expresión no ampara burlas dirigidas a humillar a alguien por su origen', 'La libertad de expresión no existe en un liceo, porque debe prevalecer el orden', 'Toda broma está protegida si el locutor no quiso ofender a nadie', 'Los derechos se interpretan juntos: expresarse no puede anular la dignidad de otros.'),
        ('abc', '{F} Un oyente dice: «Si la mayoría se rió, la broma estuvo bien». ¿Qué error comete?', 'Usa la mayoría para justificar el daño a una persona', 'Cita evidencia suficiente para justificar la broma ante el liceo', 'Confunde honra con intención de dañar a otra persona', 'Los derechos de una persona no dependen de cuántos estén de acuerdo.'),
        ('abc', '{F} Si el locutor no quiso dañar, ¿qué cambia?', 'La intención importa para educar y reparar, pero no borra el daño producido', 'Nada: solo importa la intención y no los efectos de lo dicho', 'Todo: si no quiso dañar, no hay nada que reparar ni aprender', 'Se considera la intención al decidir cómo responder, pero el daño existió.'),
        ('abc', '{F} Si el compañero afectado se siente mal, ¿qué conviene que haga?', 'Contarle a una persona adulta de confianza', 'Responder con otra broma al locutor', 'Quedarse en silencio para no complicar', 'Contarlo a alguien de confianza permite recibir apoyo y proteger su bienestar.'),
        ('abc', 'En un chat de curso alguien manda un meme que ridiculiza a una compañera. ¿Qué corresponde?', 'Dejar de difundirlo y avisar a una persona adulta de confianza', 'Reenviarlo con un comentario en contra para que todos lo rechacen', 'Guardarlo para mostrarlo después a quien corresponda', 'Difundirlo, incluso para criticarlo, aumenta el daño.'),
    ],
    ctx=('abc', 'Un compañero propone que el locutor sea humillado ante el curso para que aprenda. ¿Qué respondes?', 'Que un error se corrige con aprendizaje, no con humillación', 'Que está bien, porque así no lo repetirá nunca más', 'Que es mejor ignorar lo ocurrido y no hablar del tema', 'La clase indica que se cuida también al locutor y se evitan castigos desproporcionados.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es la honra?', 'El buen nombre y la dignidad de una persona frente a los demás', 'Una burla frente a otros puede dañar el buen nombre de una persona.'),
        ('abc', '¿Qué es una medida desproporcionada?', 'Una sanción mayor que la falta cometida', 'Una sanción igual a la falta', 'Una sanción que solo se aplica a un grupo', 'Es desproporcionada porque supera lo necesario para reparar el daño.'),
        ('En Educación Ciudadana: ¿Qué es la prevención?', 'Medidas para que un daño no se repita', 'Se logra con reglas claras y educación.'),
    ],
    op=("Con la {F} haz una tabla de tres columnas (locutor, compañero afectado, docente) con: derecho que invoca, daño o preocupación y medida que propone. Escribe luego una solución que respete a las tres personas.",
        "Locutor: libertad de expresión; teme ser censurado; pide libertad. Compañero: honra y no discriminación; dolor; pide respeto. Docente: dignidad; busca regla; propone conversación. Solución: disculpas, regla sobre burlas y un taller de convivencia.",
        ["identifica derechos", "pondera", "propone reparación y prevención"], ["tabla de tres columnas", "solución"], ["decidir por votos", "humillar al locutor"],
        "Pregunta qué se debe hacer si un nuevo hecho ocurre."),
    reinforce="Explica por qué la libertad de expresión no ampara burlas dirigidas a humillar a alguien.",
    extend="Anota un ejemplo cotidiano donde dos derechos parezcan chocar.",
)

# ============================================================ OA 05, clase 4
F = ("Ficha 24 (tema de deliberación de ejemplo): el liceo ficticio Villa Norte debate crear un protocolo de acción ante casos de discriminación. "
     "Propuesta A: un buzón anónimo de denuncias. Propuesta B: una comisión mixta de estudiantes, docentes y apoderados que escuche a las personas afectadas. "
     "Ventaja de A: protege a quien teme denunciar. Riesgo de A: pueden hacerse acusaciones falsas. Ventaja de B: permite diálogo y reparación. Riesgo de B: puede tardar o incomodar a quien denuncia. "
     "Dato de ejemplo: la comisión se reuniría 2 veces al mes y debe responder en 15 días.")
build(
    O5, 4, F,
    use="Aprenderé a deliberar sobre cómo defender derechos en la vida escolar: comparar vías, escuchar a la persona afectada y proponer pasos claros.",
    prior=["Sé qué es la exigibilidad.", "Sé ponderar derechos.", "Sé estructurar un argumento."],
    explain=[
        "Un protocolo es un conjunto de pasos acordados para actuar ante una situación. Un buen protocolo contra la discriminación protege a la persona afectada, garantiza un trato justo a quien es acusado (presunción de inocencia y derecho a ser escuchado), fija plazos y busca reparar y prevenir. No sustituye la ayuda de una persona adulta de confianza.",
        "En la deliberación se comparan vías. Un buzón anónimo protege del miedo, pero dificulta aclarar los hechos. Una comisión permite diálogo, pero puede tardar. Muchas veces se combinan: una vía confidencial para empezar y una instancia que investiga y propone reparación. También se decide quién recibe la información y cómo se resguarda.",
        "Una propuesta sólida define quién participa, cuántos días tiene para responder, qué hace ante una acusación falsa y cómo evita las represalias. Se escucha a las minorías y se registra el acuerdo. Todo se basa en razones y evidencia, no en quién tiene más amigos.",
    ],
    vocab=[("protocolo", "conjunto de pasos acordados para actuar ante una situación"), ("presunción de inocencia", "principio según el cual nadie es culpable hasta que se demuestre"), ("represalia", "daño que se causa a alguien por haber denunciado"), ("confidencial", "que se mantiene reservado, sin difundirlo"), ("plazo", "tiempo máximo para hacer algo")],
    worked=[
        ("Evaluar una vía", "Un liceo de ejemplo propone solo un buzón anónimo. ¿Qué ventaja y qué riesgo tiene?", ["Ventaja: protege a quien teme.", "Riesgo: acusaciones falsas o dificultad para aclarar."], "Protege, pero es difícil aclarar"),
        ("Plazos", "Una comisión de ejemplo debe responder en 10 días y recibe la denuncia un lunes. ¿Cuántos días tiene?", ["El plazo es de 10 días.", "Se cuenta desde la recepción."], "10 días"),
    ],
    mistakes=[("Creer que una denuncia ya prueba la culpa.", "Existe la presunción de inocencia.", "Escucha a ambas partes con respeto."),
              ("No proteger a quien denuncia.", "Pueden ocurrir represalias.", "Define medidas de resguardo.")],
    T=[
        ('abc', '¿Qué es un protocolo?', 'Un conjunto de pasos acordados para actuar ante una situación', 'Una lista de sanciones para cada falta que se pueda cometer', 'Una reunión entre estudiantes y apoderados al comienzo del año', 'Un protocolo define quién hace qué y en qué plazo.'),
        ('abc', '¿Qué características tiene un buen protocolo contra la discriminación?', 'Protege a la persona afectada, da trato justo al acusado, fija plazos y busca reparar', 'Sanciona rápido al acusado sin escucharlo para evitar que se repita', 'Se aplica solo cuando la persona afectada lo pide por escrito a la dirección', 'Combina protección, garantías, plazos y reparación.'),
        ('=', '{F} Si la comisión se reúne 2 veces al mes y cada reunión revisa 3 casos, ¿cuántos casos alcanza a revisar en 4 meses?', '2*3*4', 'Se multiplica reuniones por mes, casos por reunión y meses.', ' casos'),
        ('abc', '{F} ¿Qué ventaja tiene la propuesta A?', 'Protege a quien teme denunciar', 'Permite el diálogo entre las partes', 'Garantiza una reparación', 'La ficha señala esa ventaja del buzón anónimo.'),
        ('abc', '{F} ¿Qué riesgo tiene la propuesta A?', 'Pueden hacerse acusaciones falsas', 'Puede tardar en responder', 'Puede incomodar a quien denuncia', 'El anonimato dificulta aclarar los hechos.'),
        ('abc', '{F} ¿Qué ventaja tiene la propuesta B?', 'Permite diálogo y reparación', 'Protege el anonimato de la persona', 'Responde de inmediato', 'La comisión escucha a las personas afectadas.'),
        ('abc', '{F} ¿Qué principio protege a quien es acusado?', 'La presunción de inocencia: nadie es culpable hasta que se demuestre', 'La represalia: se castiga a una persona antes de investigar el caso', 'El plazo: se fija una fecha para responder a la denuncia', 'Un trato justo implica no tratar como culpable a quien aún no ha sido escuchado.'),
        ('abc', '{F} ¿Qué propuesta combinada es más sólida?', 'Una vía confidencial para comenzar y una comisión que investigue y repare', 'Solo el buzón, sin seguimiento ni instancia que investigue', 'Solo la comisión, con nombres públicos de quienes denuncian', 'Une protección y diálogo y reduce los riesgos de cada una.'),
        ('abc', '{F} ¿Qué medida evita represalias?', 'Resguardar la identidad y vigilar que nadie hostigue a quien denuncia', 'Publicar quién denunció para que todos lo sepan', 'Pedir a quien denuncia que lo converse a solas con el acusado', 'Protege a la persona afectada de nuevas agresiones.'),
        ('abc', '{F} Un participante dice: «Aprobemos el buzón porque lo propuso mi amigo». ¿Qué error comete?', 'Decide por amistad y no por razones', 'Usa evidencia de otro liceo', 'Responde a una objeción', 'Una buena deliberación se basa en razones y evidencia, no en amistades.'),
        ('abc', '{F} ¿Qué indicador mostraría si el protocolo funciona?', 'Casos atendidos dentro del plazo y satisfacción de las personas afectadas', 'Cantidad de afiches sobre el protocolo pegados en el liceo', 'Número de integrantes que tiene la comisión mixta', 'Mide resultados y no solo actividades.'),
        ('abc', '{F} Si una persona se siente en riesgo por un caso, ¿qué hace primero?', 'Avisar a una persona adulta de confianza', 'Esperar la reunión de la comisión', 'Resolverlo a solas con el acusado', 'La seguridad no espera a un protocolo.'),
        ('abc', '{F} ¿Qué debe prever el protocolo ante una acusación falsa?', 'Una forma de aclarar los hechos y proteger a la persona acusada injustamente', 'Sancionar a todas las personas que denuncian para evitar abusos', 'Ignorar toda denuncia anónima porque no se puede comprobar', 'Garantiza un trato justo sin desalentar las denuncias.'),
    ],
    ctx=('abc', 'En un club deportivo de ejemplo se discute qué hacer ante insultos entre socios. ¿Qué elemento no puede faltar en un protocolo?', 'Escuchar a ambas partes y fijar un plazo de respuesta', 'Sancionar al acusado antes de investigar', 'Resolver el caso sin informar a las partes', 'Un protocolo justo escucha y fija plazos.'),
    sc=[
        ('¿Qué es una represalia?', 'Un daño causado a alguien por haber denunciado', 'Debe evitarse para que las personas se atrevan a denunciar.'),
        ('abc', 'En Educación Ciudadana: ¿Qué es la presunción de inocencia?', 'Nadie es culpable hasta que se demuestre', 'Todos son culpables hasta que prueben lo contrario', 'La culpa se decide por votación', 'Nadie es tratado como culpable mientras no se demuestre su responsabilidad.'),
        ('¿Qué es un plazo?', 'Tiempo fijado para responder o cumplir un paso', 'Evita que un caso quede sin respuesta indefinidamente.'),
    ],
    op=("Con la {F} escribe un protocolo de cinco pasos para tu liceo: cómo se recibe la situación, quién la escucha, plazo, medidas de resguardo y reparación. Indica en cuál paso se avisa a una persona adulta de confianza.",
        "1. Se recibe la situación de forma reservada. 2. La comisión escucha a ambas partes. 3. Responde en 15 días. 4. Se resguarda a quien denuncia. 5. Se acuerda reparación y prevención. Aviso a un adulto de confianza: en el paso 1.",
        ["incluye plazo y resguardo", "respeta presunción de inocencia", "indica el aviso a un adulto"], ["protocolo de cinco pasos"], ["omitir a quien es acusado", "no fijar plazo"],
        "Pregunta cómo evitar que se use el protocolo para acusaciones falsas."),
    reinforce="Explica por qué un protocolo debe incluir plazos.",
    extend="Averigua si tu liceo tiene un protocolo de convivencia y qué pasos incluye.",
)

# ============================================================ OA 06, clase 1
F = ("Ficha 25 (casos de ejemplo de participación en una comuna ficticia): (1) Camila vota en la elección local. (2) Un grupo de vecinos arma una huerta comunitaria. "
     "(3) Estudiantes firman una petición para pedir más bancos en la plaza. (4) Tres amigos organizan una marcha pacífica por el cuidado del río. (5) Una joven dona dos horas semanales a un comedor solidario.")
build(
    O6, 1, F,
    use="Aprenderé a reconocer formas de participación, qué es el bien común y qué ideas centrales tienen el republicanismo, el liberalismo y el comunitarismo.",
    prior=["Sé qué es una acción democrática.", "Sé que hay derechos y responsabilidades ciudadanas.", "Sé distinguir una idea de un partido."],
    explain=[
        "Participar es tomar parte en las decisiones y en la vida de la comunidad. Hay formas diversas: votar, presentar peticiones, formar o integrar organizaciones, manifestarse de forma pacífica, hacer voluntariado y deliberar en espacios comunitarios. Todas pueden contribuir al bien común, que es el conjunto de condiciones que permite que todas las personas de una comunidad desarrollen su vida con dignidad.",
        "Tres tradiciones de pensamiento político ayudan a entenderlo. El republicanismo destaca la participación activa y la virtud cívica (compromiso con lo público) para evitar que alguien domine a otros. El liberalismo destaca las libertades individuales, los derechos y los límites al poder. El comunitarismo destaca los lazos de comunidad, la identidad compartida y los bienes que se construyen juntos.",
        "No son partidos políticos: son enfoques que se pueden combinar. Cada una responde de modo distinto a preguntas como cuánto debe participar una persona y cuánto debe decidir cada quien libremente. Comprender sus ideas ayuda a analizar los casos sin apoyar a una sola.",
    ],
    vocab=[("participación", "tomar parte en las decisiones y en la vida de la comunidad"), ("bien común", "condiciones que permiten a todas las personas de la comunidad vivir con dignidad"), ("republicanismo", "tradición que destaca la participación activa y la virtud cívica"), ("liberalismo", "tradición que destaca las libertades individuales y los límites al poder"), ("comunitarismo", "tradición que destaca los lazos de comunidad y los bienes compartidos")],
    worked=[
        ("Clasificar una forma", "Un grupo de ejemplo reúne firmas para pedir luz en un paso peatonal. ¿Qué forma de participación es?", ["Es una petición a la autoridad.", "Se hace por un medio pacífico."], "Petición"),
        ("Relacionar con una tradición", "Una vecina de ejemplo dice: «Cada persona debe poder decidir libremente cómo vivir sin que el Estado se meta». ¿Qué tradición destaca?", ["Destaca la libertad individual.", "Esa es la mirada liberal."], "Liberalismo"),
    ],
    mistakes=[("Pensar que participar es solo votar.", "Hay formas de participación entre elecciones.", "Revisa petición, voluntariado, organización y deliberación."),
              ("Confundir una tradición con un partido.", "Son enfoques de ideas y no organizaciones.", "Explica la idea central de cada una.")],
    T=[
        ('abc', '¿Qué es el bien común?', 'Las condiciones que permiten a todas las personas de una comunidad vivir con dignidad', 'La suma de lo que cada persona logra por su cuenta en la comunidad', 'Lo que decide la mayoría para su propio beneficio en la comunidad', 'El bien común se refiere a condiciones compartidas para todos, no a intereses de un grupo.'),
        ('abc', '{F} ¿Qué forma de participación es la huerta comunitaria?', 'Organización colectiva para un fin común', 'Petición a una autoridad para que atienda un reclamo', 'Voto para elegir representantes en una elección', 'Un grupo se organiza para un fin común.'),
        ('abc', '{F} ¿Qué forma de participación es firmar una petición?', 'Petición a una autoridad para que atienda un reclamo', 'Voluntariado para ayudar en una causa', 'Manifestación para expresar una causa en la calle', 'Se pide algo a quien decide.'),
        ('abc', '{F} ¿Qué forma de participación es la marcha pacífica por el río?', 'Manifestación en el espacio público', 'Voto para elegir representantes', 'Organización colectiva estable', 'Se expresa una causa en el espacio público.'),
        ('=', '{F} Si la joven mantiene su aporte durante 12 semanas, ¿cuántas horas dona en total al comedor?', '2*12', 'Se multiplican las horas semanales por las semanas.', ' horas'),
        ('abc', '¿Qué destaca el republicanismo?', 'La participación activa y la virtud cívica', 'Las libertades individuales y los límites al poder', 'Los lazos de comunidad y la identidad compartida', 'Cada tradición tiene su idea central; la del republicanismo es el compromiso con lo público.'),
        ('abc', '¿Qué destaca el liberalismo?', 'Las libertades individuales y los límites al poder', 'La participación activa y la virtud cívica', 'Los lazos de comunidad y la identidad compartida', 'El liberalismo se centra en derechos y límites al poder.'),
        ('abc', '¿Qué destaca el comunitarismo?', 'Los lazos de comunidad y los bienes que se construyen juntos', 'Las libertades individuales por sobre todo y los límites al poder', 'La participación como deber de toda persona en la vida pública', 'El comunitarismo subraya identidad y vínculos compartidos.'),
        ('abc', '{F} ¿Qué caso se relaciona más con la idea comunitarista de construir bienes juntos?', 'La huerta comunitaria', 'El voto de Camila', 'La petición de bancos firmada por estudiantes', 'Subraya lo que una comunidad construye en conjunto.'),
        ('abc', '{F} ¿Qué caso expresa mejor la participación activa y el compromiso con lo público?', 'Tres amigos que organizan una marcha pacífica por el río', 'Una persona que no participa porque prefiere no involucrarse', 'Camila al votar sin informarse sobre las propuestas', 'Es compromiso activo con un asunto de interés común.'),
        ('abc', '{F} Un estudiante dice: «Participar es solo votar». ¿Qué respuesta es más ajustada?', 'Hay otras formas, como petición, organización, manifestación y voluntariado', 'Tiene razón, porque votar es la única forma legítima de participar', 'Votar no es una forma de participación, solo una obligación', 'La ficha muestra varias formas de participar además del voto.'),
        ('abc', '{F} Alguien dice: «El comunitarismo es un partido político». ¿Qué corresponde?', 'Aclarar que es un enfoque de ideas que puede combinarse con otros, no un partido', 'Aceptarlo, porque toda tradición política es un partido que compite', 'Decir que solo el republicanismo es un enfoque válido de análisis', 'Las tradiciones son maneras de analizar, no organizaciones políticas.'),
        ('abc', '{F} ¿Cuáles formas de participación pueden contribuir al bien común?', 'Todas las de la ficha, si son pacíficas y respetan los derechos de los demás', 'Solo votar, porque es la única forma de participación formal', 'Solo las que organiza el municipio, porque tienen autorización', 'Todas pueden aportar siempre que respeten derechos.'),
    ],
    ctx=('abc', 'Un centro de estudiantes organiza una jornada para limpiar el patio y otra para pedir un nuevo bebedero. ¿Qué dos formas combina?', 'Voluntariado y petición', 'Voto y manifestación', 'Petición y herencia', 'Una acción de trabajo y un pedido a quien decide.'),
    sc=[
        ('¿Qué es participar?', 'Tomar parte en las decisiones y en la vida de la comunidad', 'Incluye votar, pedir, organizarse, manifestarse y ayudar.'),
        ('abc', '¿Qué es la virtud cívica?', 'El compromiso de una persona con lo público', 'La riqueza de una persona', 'El grado de obediencia a la autoridad', 'Es un valor central del republicanismo.'),
        ('¿Qué es una manifestación pacífica?', 'Una reunión en el espacio público para expresar una causa sin violencia', 'Es una forma de participación protegida por la libertad de reunión.'),
    ],
    op=("Con la {F} haz una tabla con los cinco casos: forma de participación, aporte al bien común y tradición con la que lo relacionas (republicanismo, liberalismo o comunitarismo) con una razón. Termina con una reflexión personal de tres líneas sobre qué forma te sería más fácil.",
        "Caso 1: voto; elige representantes; republicanismo; participación en lo público. Caso 2: huerta; alimentos y encuentro; comunitarismo. Caso 3: petición; mejora un espacio; republicanismo. Caso 4: marcha; cuida el río; liberalismo y derecho a expresarse. Caso 5: voluntariado; ayuda; comunitarismo. Reflexión: me sería más fácil la petición.",
        ["clasifica formas", "relaciona con tradiciones con razones", "reflexiona sin exponer a otros"], ["tabla de cinco casos", "reflexión"], ["decir que una tradición es un partido", "apoyar una sola"],
        "Pregunta qué forma de participación aporta más a su comunidad."),
    reinforce="Explica con tus palabras la diferencia entre republicanismo y liberalismo.",
    extend="Anota una forma de participación que podrías hacer esta semana.",
)

# ============================================================ OA 06, clase 2
F = ("Ficha 26 (caso de ejemplo): en el barrio ficticio Las Acacias, vecinos se organizaron para rescatar una plaza abandonada. En 4 meses: 35 personas participaron en 6 jornadas de limpieza; "
     "se pidió al municipio iluminación; se plantaron 20 árboles con donaciones; una vecina dijo: «Aquí no nos conocíamos; ahora nos saludamos». "
     "Fuentes: acta de la junta de vecinos, un afiche del municipio y el testimonio de la vecina.")
build(
    O6, 2, F,
    use="Aprenderé a investigar un caso de participación y a identificar su aporte al bien común, con evidencia de distintas fuentes.",
    prior=["Sé las formas de participación.", "Sé qué es el bien común.", "Sé interrogar fuentes."],
    explain=[
        "Para investigar un caso de participación se pregunta: quiénes participaron, qué hicieron, qué lograron y qué evidencia lo muestra. Los resultados pueden ser materiales (una plaza limpia, árboles plantados) y sociales (confianza, encuentro, sensación de pertenencia). Ambos pueden aportar al bien común.",
        "Las fuentes aportan distintas cosas. Un acta es un registro de las decisiones de una organización. Un afiche del municipio informa lo que la autoridad quiere comunicar. Un testimonio muestra una experiencia personal. Se anota qué evidencia respalda cada afirmación, por ejemplo cuántas jornadas se hicieron, y qué es opinión o percepción.",
        "También se analizan los límites: quién no pudo participar, qué tareas siguen pendientes y si los resultados son estables. Un caso no se generaliza: una plaza rescatada no prueba que toda la participación funcione. La investigación termina con una conclusión prudente y preguntas para seguir.",
    ],
    vocab=[("resultado material", "logro que se puede ver o contar, como árboles plantados"), ("resultado social", "logro en las relaciones, como confianza o encuentro"), ("acta", "registro escrito de lo que decide una organización"), ("pertenencia", "sentimiento de ser parte de una comunidad"), ("sostenibilidad", "capacidad de mantener algo en el tiempo")],
    worked=[
        ("Resultado material y social", "Un grupo de ejemplo pintó una escuela y ahora se reúne cada mes. ¿Cuál es material y cuál social?", ["Pintar la escuela se ve.", "Reunirse cada mes muestra vínculos."], "Material: pintura; social: reuniones"),
        ("Opinión y dato", "Una nota dice «mucha gente ayudó». Otra dice «ayudaron 40 personas». ¿Cuál es dato?", ["La segunda es un número.", "La primera es vaga."], "La segunda"),
    ],
    mistakes=[("Concluir que toda la participación es exitosa por un solo caso.", "Un caso no prueba una regla.", "Habla del caso y no generalices."),
              ("Medir el éxito solo por lo material.", "También cuentan los resultados sociales.", "Revisa cuánto cambió la relación entre vecinos.")],
    T=[
        ('abc', '¿Cuál es un resultado social de un proceso de participación?', 'Que los vecinos se conozcan y ganen confianza', 'Que se planten 20 árboles', 'Que se pida iluminación al municipio', 'Los resultados sociales son vínculos y confianza; los otros son materiales o gestiones.'),
        ('=', '{F} Si cada jornada de limpieza duró 3 horas, ¿cuántas horas de limpieza hubo en total?', '6*3', 'Se multiplican las jornadas por las horas de cada una.', ' horas'),
        ('abc', '{F} ¿Qué resultado es material?', 'Los 20 árboles plantados', 'Que ahora se saludan', 'El sentimiento de pertenencia', 'Un resultado material se puede contar o ver.'),
        ('abc', '{F} ¿Qué fuente registra las decisiones de la organización?', 'El acta de la junta de vecinos', 'El afiche del municipio', 'El testimonio de la vecina', 'Un acta es el registro escrito de las decisiones de la organización.'),
        ('abc', '{F} ¿Qué tipo de fuente es el testimonio de la vecina?', 'Una experiencia personal que muestra una percepción individual', 'Un registro oficial de decisiones tomadas por la organización', 'Un dato estadístico que describe a toda la comuna', 'Un testimonio cuenta lo vivido por una persona.'),
        ('abc', '{F} ¿Qué puede esperarse de un afiche del municipio?', 'Que informe lo que la autoridad quiere comunicar, no necesariamente todo lo ocurrido', 'Que registre todas las decisiones tomadas por la junta de vecinos', 'Que muestre la experiencia personal de cada vecino de la comuna', 'Cada fuente tiene un propósito; el del afiche es comunicar la postura del municipio.'),
        ('abc', '{F} ¿Qué dato no está claro en la ficha?', 'Si el municipio instaló la iluminación solicitada', 'Cuántos árboles se plantaron gracias a las donaciones', 'Cuántas jornadas de limpieza se realizaron en los cuatro meses', 'La ficha dice que se pidió, pero no que se haya concedido.'),
        ('abc', '{F} Alguien dice: «Todos los vecinos de la comuna participaron». ¿Qué corresponde?', 'Pedir evidencia: la ficha habla de 35 personas de un barrio', 'Aceptarlo, porque el caso fue exitoso en todo el barrio', 'Rechazarlo, porque nadie más que los 35 vecinos participó', 'La afirmación excede lo que muestran las fuentes.'),
        ('abc', '{F} ¿Qué límite podría tener este caso?', 'Algunas personas pudieron no participar por falta de tiempo o de información', 'Que los resultados materiales no tienen valor para la comunidad', 'Que el barrio es demasiado pequeño para que haya participación', 'Una investigación revisa quién queda fuera.'),
        ('abc', '{F} ¿Qué conclusión es prudente?', 'En este caso, la participación mejoró un espacio y la confianza entre vecinos', 'La participación siempre funciona, en cualquier barrio y situación', 'El municipio no cumplió su rol en el proceso de rescate', 'Se limita a lo que muestran las fuentes, sin generalizar.'),
        ('abc', '{F} ¿Qué pregunta ayuda a seguir investigando?', '¿Cómo se mantendrá la plaza en el tiempo?', '¿Quién merece el mérito de la idea?', '¿Cuánto cuesta cada árbol en otra ciudad?', 'Apunta a la sostenibilidad de los resultados.'),
        ('abc', '{F} ¿Qué evidencia respalda la afirmación de que hubo trabajo colectivo sostenido?', 'Las 6 jornadas de limpieza en 4 meses', 'El afiche, que informa lo que el municipio quiere comunicar', 'La percepción de una sola vecina', 'Un dato verificable respalda mejor la afirmación que un comunicado o una percepción.'),
        ('abc', '{F} ¿Cuál de estas frases es una percepción?', '«Ahora nos saludamos»', '«Se plantaron 20 árboles»', '«Hubo 6 jornadas de limpieza»', 'Una percepción es una experiencia personal; las otras son hechos que se pueden contar.'),
    ],
    ctx=('abc', 'Una junta de ejemplo reporta: «Se hicieron 3 reuniones y 12 vecinos aprendieron primeros auxilios». ¿Qué parte es un resultado social?', 'Que los vecinos se reúnen y aprenden juntos como comunidad', 'El número 3, que es la cantidad de reuniones realizadas', 'El número 12, que es la cantidad de vecinos capacitados', 'El resultado social es el encuentro y el aprendizaje compartido; los números son datos materiales.'),
    sc=[
        ('En Educación Ciudadana: ¿Qué es un acta?', 'Un registro escrito de lo que decide una organización', 'Es una fuente que muestra las decisiones tomadas.'),
        ('abc', '¿Qué es la pertenencia?', 'El sentimiento de ser parte de una comunidad', 'Un trámite para inscribirse en una organización', 'El número de personas de un grupo', 'Es un resultado social de participar.'),
        ('¿Qué es la sostenibilidad?', 'La capacidad de mantener algo en el tiempo', 'Mira si un resultado dura más allá de la acción inicial.'),
    ],
    op=("Con la {F} escribe un informe de cinco puntos: quiénes participaron, qué hicieron, dos resultados (uno material y uno social), qué fuente respalda cada uno y un límite.",
        "Participaron 35 personas. Hicieron 6 jornadas de limpieza y plantaron 20 árboles. Resultado material: 20 árboles; fuente: acta. Resultado social: vecinos que se saludan; fuente: testimonio. Límite: no sabemos si se logró la iluminación.",
        ["usa datos", "cita fuentes", "señala un límite"], ["informe de cinco puntos"], ["generalizar", "olvidar la fuente"],
        "Pregunta cómo comprobaría la sostenibilidad de la plaza."),
    reinforce="Explica por qué un resultado social también aporta al bien común.",
    extend="Observa un espacio comunitario y anota quién lo cuida y cómo.",
)

# ============================================================ OA 06, clase 3
F = ("Ficha 27 (caso de ejemplo): una comuna ficticia debe decidir qué hacer con un terreno vacío. "
     "Voz 1 (inspirada en el republicanismo): «Que los vecinos deliberen y decidan juntos, y que cada uno se comprometa con el cuidado». "
     "Voz 2 (inspirada en el liberalismo): «Cada persona debe poder usar el terreno como prefiera, siempre que respete los derechos de los demás; el Estado no debe imponer un solo uso». "
     "Voz 3 (inspirada en el comunitarismo): «El terreno debe servir a lo que identifica a la comunidad, como un espacio de encuentro y de fiestas locales». Opciones: plaza, huertos privados, feria vecinal.")
build(
    O6, 3, F,
    use="Aprenderé a contrastar cómo el republicanismo, el liberalismo y el comunitarismo interpretan un mismo caso, y a ver lo que cada una aporta y lo que deja afuera.",
    prior=["Sé las ideas centrales de las tres tradiciones.", "Sé comparar perspectivas.", "Sé que una tradición no es un partido."],
    explain=[
        "Un mismo caso se puede mirar con distintas tradiciones. El republicanismo pregunta cómo se decide en común y quién asume tareas por la comunidad. El liberalismo pregunta si se respetan las libertades individuales y si el poder está limitado. El comunitarismo pregunta si se fortalecen la identidad y los lazos de la comunidad.",
        "Cada enfoque aporta algo valioso y también tiene riesgos. El republicanismo puede exigir demasiada participación a quien no puede. El liberalismo puede descuidar los bienes compartidos si cada quien actúa solo. El comunitarismo puede presionar a quienes piensan distinto o excluir a quien no comparte la identidad dominante.",
        "Un buen análisis no elige una tradición como «la correcta», sino que usa las tres como lentes. Se pregunta qué ve cada una, qué evidencia usa y qué acuerdo mínimo es posible. En el caso del terreno, una propuesta mixta puede combinar deliberación, libertad de uso y un espacio de encuentro.",
    ],
    vocab=[("lente de análisis", "forma de mirar un caso desde una idea o tradición"), ("virtud cívica", "compromiso de una persona con lo público y con el bien común"), ("identidad compartida", "rasgos y tradiciones que una comunidad reconoce como propios"), ("exclusión", "dejar fuera a personas de una decisión o espacio"), ("acuerdo mínimo", "punto común entre posturas distintas")],
    worked=[
        ("Aplicar un lente", "Un municipio de ejemplo quiere decidir sobre un mural. ¿Qué pregunta haría el comunitarismo?", ["Mira la identidad.", "Pregunta si representa a la comunidad."], "¿Representa a la comunidad?"),
        ("Ver un riesgo", "Una norma de ejemplo exige a todos asistir a las reuniones. ¿Qué riesgo tiene desde el liberalismo?", ["Limita la libertad de quien no quiere o no puede.", "Obliga sin justificar."], "Limita la libertad individual"),
    ],
    mistakes=[("Elegir una tradición como la única correcta.", "Cada una ve algo distinto y tiene riesgos.", "Usa las tres como lentes."),
              ("Atribuir a una tradición ideas de un partido.", "Son enfoques de ideas y no organizaciones.", "Basta explicar la idea central.")],
    T=[
        ('abc', '¿Qué pregunta hace el republicanismo ante un caso?', 'Cómo se decide en común y quién asume tareas por la comunidad', 'Si se respetan las libertades individuales y el poder está limitado', 'Si se fortalecen la identidad y los lazos de la comunidad', 'Cada tradición se pregunta cosas distintas; esta es la del republicanismo.'),
        ('abc', '{F} ¿Qué voz destaca la libertad de uso con respeto por los derechos?', 'Voz 2 (liberalismo)', 'Voz 1 (republicanismo)', 'Voz 3 (comunitarismo)', 'La Voz 2 dice que cada persona usa el terreno como prefiera si respeta derechos.'),
        ('abc', '{F} ¿Qué voz destaca la deliberación vecinal y el compromiso con el cuidado?', 'Voz 1 (republicanismo)', 'Voz 2 (liberalismo)', 'Voz 3 (comunitarismo)', 'La Voz 1 habla de deliberar y decidir juntos.'),
        ('abc', '{F} ¿Qué opción es más coherente con la Voz 2, que no quiere imponer un solo uso?', 'Huertos privados', 'Una plaza decidida por la asamblea', 'Una feria vecinal obligatoria para todos', 'Permite usos individuales en vez de un único destino impuesto.'),
        ('abc', '{F} ¿Qué opción se acerca más a lo que pide la Voz 3?', 'Feria vecinal, como espacio de encuentro y fiestas locales', 'Huertos privados para uso individual de cada vecino', 'Dejar el terreno vacío mientras se decide qué hacer con él', 'La Voz 3 habla de un espacio de encuentro y fiestas locales.'),
        ('abc', '{F} ¿Qué riesgo tiene la Voz 1?', 'Exigir demasiada participación a quien no puede', 'Descuidar los bienes compartidos', 'Excluir a quien no comparte la identidad dominante', 'El republicanismo puede pedir más compromiso del que todos pueden dar.'),
        ('abc', '{F} ¿Qué riesgo tiene la Voz 2?', 'Descuidar los bienes compartidos si cada quien actúa solo', 'Exigir demasiada participación a quien no puede, por trabajo o salud', 'Presionar a quienes piensan distinto de la identidad dominante', 'Si cada persona actúa por separado, se pierde lo común.'),
        ('abc', '{F} ¿Qué riesgo tiene la Voz 3?', 'Presionar o excluir a quienes no comparten la identidad dominante', 'Dejar el uso solo a decisión individual de cada vecino', 'Exigir demasiada participación a quien no puede asistir a las asambleas', 'La identidad compartida puede dejar fuera a quienes piensan distinto.'),
        ('abc', '{F} ¿Qué propuesta mixta combina las tres voces?', 'Una plaza decidida en asamblea, con espacio para huertos y ferias, respetando derechos', 'Elegir solo la opción que prefiera la mayoría del barrio', 'Dejar que cada vecino use una parte del terreno sin acuerdo previo', 'Une deliberación, libertad de uso e identidad compartida.'),
        ('abc', '{F} Alguien dice: «La Voz 2 es del partido tal». ¿Qué error comete?', 'Confunde una tradición de ideas con un partido político', 'Cita evidencia suficiente para sostener su afirmación', 'Usa un lente de análisis para comparar posturas distintas', 'Las tradiciones son enfoques de análisis, no organizaciones.'),
        ('abc', '{F} ¿Qué acuerdo mínimo es posible?', 'Que el terreno beneficie a la comunidad sin vulnerar derechos', 'Que nadie lo use para evitar conflictos', 'Que se use como decida el municipio sin consultar', 'Es un punto que las tres voces pueden compartir.'),
        ('abc', '{F} ¿Qué pregunta ayuda a decidir?', '¿Quiénes quedarían fuera con cada opción?', '¿Qué voz habló con más seguridad?', '¿Qué opción propuso un vecino conocido?', 'Revisa la inclusión y los riesgos de cada alternativa.'),
        ('abc', 'Un liceo debate si el recreo largo debe tener actividades obligatorias. ¿Qué lente cuestiona más la obligación?', 'Liberal, por la libertad de elegir', 'Republicano, por el compromiso con lo público', 'Comunitario, por los lazos compartidos', 'El liberalismo destaca las libertades individuales.'),
    ],
    ctx=('abc', 'Un curso decide su lema entre todos, tras un debate en que cada estudiante asume una tarea. ¿Qué tradición destaca esto?', 'Republicanismo', 'Liberalismo', 'Mercantilismo', 'Destaca la deliberación y el compromiso compartido.'),
    sc=[
        ('¿Qué es un lente de análisis?', 'Una forma de mirar un caso desde una idea o tradición', 'Cada lente ilumina algo distinto del mismo caso.'),
        ('abc', 'En el republicanismo, ¿qué es la virtud cívica?', 'El compromiso de una persona con lo público', 'La riqueza de una persona o de su familia', 'El respeto a un partido político determinado', 'La virtud cívica es una idea central del republicanismo.'),
        ('¿Qué es una identidad compartida?', 'Rasgos y tradiciones que una comunidad reconoce como propios', 'Une a las personas de una comunidad.'),
    ],
    op=("Con la {F} arma una tabla con las tres voces: qué pregunta hace, qué aporta, qué riesgo tiene. Escribe una propuesta mixta de tres líneas que combine lo mejor de cada una y respete a quienes piensan distinto.",
        "Voz 1: ¿cómo decidimos juntos? Aporta deliberación; riesgo, exigir demasiado. Voz 2: ¿se respetan las libertades? Aporta derechos; riesgo, descuidar lo común. Voz 3: ¿fortalece la identidad? Aporta encuentro; riesgo, excluir. Propuesta: plaza decidida en asamblea, con huertos abiertos y una feria vecinal.",
        ["aplica tres lentes", "identifica riesgos", "propone sin tomar partido"], ["tabla de tres voces", "propuesta de tres líneas"], ["elegir una tradición como correcta", "olvidar a quien disiente"],
        "Pregunta quiénes podrían sentirse excluidos."),
    reinforce="Explica un riesgo de cada tradición con tus palabras.",
    extend="Elige un tema de tu liceo y formula una pregunta desde cada tradición.",
)

# ============================================================ OA 06, clase 4
F = ("Ficha 28 (tema de deliberación de ejemplo): en la comuna ficticia de Cerro Alto se propone un presupuesto participativo: los vecinos votan en qué se gastan 12 millones de pesos del municipio. "
     "Razón a favor: acerca las decisiones a la gente. Razón en contra: puede favorecer a quienes más participan. "
     "Dato de ejemplo: en una prueba, votaron 300 de 3.000 habitantes; ganó el proyecto de iluminación con 120 votos; el de juegos infantiles tuvo 90 y el de una cancha 90.")
build(
    O6, 4, F,
    use="Aprenderé a deliberar sobre mecanismos de participación, evaluando su aporte al bien común y sus riesgos de exclusión.",
    prior=["Sé contrastar tradiciones políticas.", "Sé estructurar un argumento.", "Sé calcular porcentajes simples."],
    explain=[
        "Un mecanismo de participación es un procedimiento que permite a la ciudadanía influir en decisiones públicas, como un presupuesto participativo, un cabildo o una consulta. Su valor está en acercar las decisiones, pero depende de cuántas y cuáles personas participan: si participan pocas, el resultado puede no representar a la comunidad.",
        "Para deliberar se examinan criterios: representatividad (quiénes participan), transparencia (cómo se decide), inclusión (cómo se llega a quienes no pueden asistir) y efecto real (si la decisión se cumple). Un dato como «300 de 3.000» muestra una participación del 10 %; no dice por sí solo que el resultado sea injusto, pero invita a ampliar la participación.",
        "Las distintas tradiciones ayudan a argumentar: se puede apreciar el compromiso cívico, cuidar las libertades de quienes no participan y respetar los lazos de la comunidad. Una propuesta sólida combina razones con medidas concretas, por ejemplo votación en línea y presencial, y un seguimiento público de lo ejecutado.",
    ],
    vocab=[("presupuesto participativo", "mecanismo en que la comunidad decide parte del gasto público"), ("representatividad", "grado en que quienes participan reflejan a toda la comunidad"), ("cabildo", "reunión abierta de la comunidad para discutir un tema público"), ("consulta", "mecanismo para conocer la opinión de la ciudadanía"), ("seguimiento", "control de que lo decidido se cumpla")],
    worked=[
        ("Calcular participación", "En una consulta de ejemplo votan 150 de 1.000 personas. ¿Qué porcentaje participa?", ["150 entre 1.000 es 15 de 100.", "Es el 15 %."], "15 %"),
        ("Ampliar la inclusión", "Una votación de ejemplo se hace solo en la sede municipal. ¿Qué medida amplía la inclusión?", ["Llegar a quienes no pueden asistir.", "Agregar puntos de votación en barrios."], "Puntos de votación en los barrios"),
    ],
    mistakes=[("Creer que cualquier votación es representativa.", "Participan pocas personas y pueden ser un grupo específico.", "Revisa cuántas y quiénes participan."),
              ("Descartar un mecanismo por un solo problema.", "Se puede mejorar su diseño.", "Propón ajustes concretos.")],
    T=[
        ('abc', '¿Qué ocurre en un presupuesto participativo?', 'Un mecanismo en que la comunidad decide cómo gastar parte del presupuesto público', 'Un impuesto que paga la comunidad para financiar sus proyectos', 'Una encuesta sobre la opinión del alcalde en la comuna', 'Permite que la ciudadanía influya en el gasto público.'),
        ('=', '{F} ¿Qué porcentaje de los 3.000 habitantes votó en la prueba?', '300*100//3000', 'Se compara la parte que votó con el total de habitantes.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las personas que votaron eligió el proyecto de iluminación?', '120*100//300', 'Se compara los votos de iluminación con el total de votos.', ' %'),
        ('=', '{F} ¿Qué porcentaje de los 3.000 habitantes votó por el proyecto de iluminación?', '120*100//3000', 'Se compara los votos del proyecto ganador con toda la población.', ' %'),
        ('abc', '{F} ¿Qué razón a favor da la ficha?', 'Acerca las decisiones a la gente', 'Garantiza que ganen los proyectos más caros', 'Evita que el municipio tenga que decidir', 'Es la razón a favor registrada en la ficha.'),
        ('abc', '{F} ¿Qué riesgo señala la ficha?', 'Puede favorecer a quienes más participan', 'Hace que siempre pierda la mayoría', 'Impide que haya debate', 'Es la razón en contra registrada en la ficha.'),
        ('abc', '{F} ¿Qué criterio revisa si participan pocas personas?', 'Representatividad', 'Seguimiento', 'Transparencia', 'La representatividad pregunta quiénes participan y si reflejan a la comunidad.'),
        ('abc', '{F} ¿Qué medida aumenta la inclusión?', 'Ofrecer votación en línea y presencial, con apoyo a quienes no pueden asistir', 'Votar en un solo lugar y horario, para ordenar la participación', 'Informar solo a quienes ya participaron antes en otras votaciones', 'Llega a más personas y reduce barreras.'),
        ('abc', '{F} Un asistente dice: «Ganó con 120 votos, así que representa a toda la comuna». ¿Qué corresponde?', 'Señalar que 120 de 3.000 habitantes es una parte pequeña y la participación baja', 'Aceptarlo porque ganó, y por eso representa a la comuna', 'Anular la votación porque ganó con pocos votos y no vale', 'El resultado es legítimo, pero no puede presentarse como la voluntad de toda la comuna.'),
        ('abc', '{F} ¿Qué es el seguimiento?', 'Verificar públicamente que lo decidido se cumpla', 'Cambiar el resultado de la votación si no gusta', 'Contar de nuevo los votos de la elección', 'Controla la ejecución de lo decidido.'),
        ('abc', '{F} ¿Qué propuesta combina razones a favor y en contra?', 'Presupuesto participativo con difusión amplia, varios formatos de voto y seguimiento', 'Cancelar el presupuesto participativo, porque participa poca gente', 'Mantenerlo igual que en la prueba, sin cambios ni difusión', 'Mantiene el acercamiento y reduce el riesgo de exclusión.'),
        ('abc', '{F} Desde el republicanismo, ¿qué se valoraría?', 'La participación y el compromiso cívico, y ampliar quién participa', 'Que decida cada persona sin involucrarse en lo público', 'Que se conserve la identidad sin cambios en la comuna', 'El republicanismo destaca la participación activa.'),
        ('abc', '{F} Desde el liberalismo, ¿qué se cuidaría?', 'Que quienes no participan no pierdan derechos ni libertades', 'Que todos estén obligados a votar sin excepción', 'Que solo vote quien tenga más tiempo disponible', 'El liberalismo respeta las libertades individuales.'),
    ],
    ctx=('abc', 'Un curso decide el destino de $60.000 con una votación en que solo participan quienes asisten ese día. ¿Qué mejora la representatividad?', 'Permitir votar durante toda la semana', 'Contar solo a los presentes del día', 'Decidir por sorteo', 'Con más tiempo para votar, más estudiantes pueden participar y el resultado los refleja mejor.'),
    sc=[
        ('¿Qué es un presupuesto participativo?', 'Un mecanismo en que la comunidad decide parte del gasto público', 'El municipio abre una parte del presupuesto a la decisión de los vecinos.'),
        ('abc', '¿Qué es la representatividad?', 'El grado en que quienes participan reflejan a la comunidad', 'El tamaño de la sala donde se realiza la votación', 'El número de proyectos que se presentaron al concurso', 'Mide cuánto se refleja a todos.'),
        ('¿Qué es un cabildo?', 'Una reunión abierta de la comunidad para discutir un tema público', 'En ella se puede deliberar en común.'),
    ],
    op=("Con la {F} escribe una propuesta de seis líneas: tu postura sobre el presupuesto participativo, una razón con el dato, un riesgo, una medida de inclusión, una medida de seguimiento y una tradición política que respalda tu enfoque.",
        "Postura: conviene hacerlo con mejoras. Razón: acerca decisiones, aunque votó el 10 %. Riesgo: favorece a quienes participan. Inclusión: votación en línea y en barrios. Seguimiento: informe público trimestral. Tradición: republicanismo, por la participación activa.",
        ["usa el dato", "propone inclusión y seguimiento", "vincula una tradición"], ["propuesta de seis líneas"], ["decir que el resultado representa a todos", "olvidar a quienes no participan"],
        "Pregunta cómo llegaría a personas que no se enteran."),
    reinforce="Explica por qué la baja participación afecta la representatividad.",
    extend="Averigua si tu comuna tiene alguna consulta o cabildo y cuándo se realiza.",
)

# ============================================================ OA 06, clase 5
F = ("Ficha 29 (diagnóstico de ejemplo): en el liceo ficticio Santa Elena, una encuesta a 80 estudiantes muestra que 50 nunca han participado en una actividad comunitaria y 30 sí. "
     "Razones de los 50 (de ejemplo): 25 no sabían cómo, 15 no tenían tiempo, 10 no creían que sirviera. "
     "Recursos: 10 estudiantes voluntarios, una sala, 4 semanas. Idea: un «mes de la comunidad» con una actividad pequeña por semana (huerto, apoyo escolar, limpieza de patio, feria de intercambio).")
build(
    O6, 5, F,
    use="Aprenderé a diseñar una acción de participación que fortalezca el bien común y que sea inclusiva, con metas, roles e indicadores.",
    prior=["Sé las formas de participación.", "Sé diseñar una acción con objetivo e indicador.", "Sé leer un diagnóstico."],
    explain=[
        "Diseñar una acción de participación parte de entender por qué la gente no participa. En el diagnóstico de ejemplo hay tres causas: no saben cómo, no tienen tiempo y no creen que sirva. Cada causa pide una respuesta distinta: informar y orientar, ofrecer actividades breves y mostrar resultados visibles.",
        "El diseño incluye un objetivo medible (por ejemplo, que 20 estudiantes nuevos participen), actividades por semana, roles de los voluntarios, recursos, un indicador y un plan de inclusión. También se piensa en el cuidado del grupo: tareas seguras en el liceo, con una persona adulta responsable, sin riesgos innecesarios.",
        "Al final se evalúa: ¿participaron quienes antes no lo hacían?, ¿qué actividades funcionaron?, ¿qué se aprendió? Se comunica el resultado con honestidad y se decide si repetir. Una acción pequeña y bien hecha fortalece la confianza y muestra que participar sirve.",
    ],
    vocab=[("diagnóstico", "descripción del problema con datos"), ("participante nuevo", "persona que antes no había participado"), ("actividad breve", "tarea de corta duración que facilita participar"), ("responsable adulto", "persona adulta que acompaña y cuida la actividad"), ("evaluación", "revisión de resultados para decidir qué mantener o cambiar")],
    worked=[
        ("Medir participantes nuevos", "En un curso de ejemplo, 12 de 40 habían participado y tras la acción lo han hecho 25. ¿Cuántos nuevos hay?", ["Se resta 12 a 25.", "Son los que antes no participaban."], "13 estudiantes nuevos"),
        ("Responder a una causa", "Si la causa es «no tienen tiempo», ¿qué respuesta sirve?", ["Actividades breves y flexibles.", "Evita pedir horas largas."], "Actividades breves"),
    ],
    mistakes=[("Diseñar sin atender las causas del diagnóstico.", "La acción no resuelve por qué no participan.", "Responde a cada causa."),
              ("Planear tareas con riesgo físico sin supervisión.", "Se debe cuidar al grupo.", "Elige tareas seguras y un responsable adulto.")],
    T=[
        ('abc', '¿Qué es un diagnóstico?', 'Una descripción del problema con datos', 'Una lista de actividades por realizar', 'Una evaluación final de resultados', 'El diagnóstico muestra qué ocurre antes de actuar.'),
        ('=', '{F} ¿Qué porcentaje de quienes nunca han participado dijo que no sabía cómo?', '25*100//50', 'Se compara esa razón con el total de quienes no participaron.', ' %'),
        ('=', '{F} Si el objetivo es que 20 estudiantes nuevos participen, ¿qué porcentaje representa de los 50 que nunca han participado?', '20*100//50', 'Se compara la meta con el grupo de partida.', ' %'),
        ('abc', '{F} ¿Cuál es la razón más frecuente para no haber participado?', 'No sabían cómo (25 de 50)', 'No tenían tiempo (25 de 50)', 'No creían que sirviera (15 de 50)', '25 es la mayor cantidad entre 25, 15 y 10.'),
        ('abc', '{F} ¿Qué respuesta atiende «no sabían cómo»?', 'Información clara y orientación sobre cómo sumarse', 'Actividades de todo el día', 'Pedir a los estudiantes que sean más curiosos', 'Informar y orientar resuelve la causa del problema: no saber cómo participar.'),
        ('abc', '{F} ¿Qué respuesta atiende «no tenían tiempo»?', 'Actividades breves y flexibles', 'Una actividad larga de un día completo', 'Una lista de asistencia obligatoria', 'Una actividad breve se ajusta a quien dispone de poco tiempo.'),
        ('abc', '{F} ¿Qué respuesta atiende «no creían que sirviera»?', 'Mostrar resultados visibles de lo que se logra', 'Repetir que participar es importante', 'Exigir participación para que se convenzan', 'La evidencia convence más que la insistencia o la obligación.'),
        ('=', '{F} Si cada una de las 4 actividades necesita 2 voluntarios y hay 10, ¿cuántos voluntarios quedan de apoyo general?', '10-2*4', 'Se calcula cuántos se asignan y se resta del total.', ' voluntarios'),
        ('abc', '{F} ¿Qué indicador mide el objetivo?', 'Número de estudiantes nuevos que participaron en alguna actividad', 'Cantidad de afiches pegados durante las cuatro semanas', 'Cantidad de actividades planificadas para el mes de la comunidad', 'Mide participación nueva y no solo actividad.'),
        ('abc', '{F} ¿Qué cuidado debe haber en el huerto o la limpieza del patio?', 'Tareas seguras y un responsable adulto', 'Usar herramientas del liceo sin supervisión para avanzar más rápido', 'Que cada estudiante decida solo cómo hacerlo', 'Se cuida al grupo con tareas seguras y supervisión.'),
        ('abc', '{F} ¿Qué tradición política destaca específicamente la virtud cívica de comprometerse con lo público?', 'Republicanismo', 'Liberalismo', 'Mercantilismo', 'La virtud cívica es una idea central del republicanismo.'),
        ('abc', '{F} Si solo se suman 5 estudiantes nuevos, ¿qué conviene hacer?', 'Revisar qué actividad no atrajo y ajustar la próxima', 'Cancelar toda participación porque la actividad no resultó', 'Informar que la meta se cumplió igualmente ante el liceo', 'Evaluar permite saber qué falló y corregirlo en la próxima actividad.'),
        ('abc', '{F} ¿Qué medida incluye a quien no puede asistir en el horario de las actividades?', 'Ofrecer una forma de aportar en otro horario o a distancia', 'Pedir justificativo a quien no asista', 'Hacer todas las actividades en horario de clases', 'Ofrecer otro horario o participación a distancia elimina la barrera del horario.'),
    ],
    ctx=('abc', 'Un centro de estudiantes quiere más asistentes a sus asambleas. ¿Qué medida es coherente con las causas del diagnóstico?', 'Dar información previa y hacerlas breves', 'Alargarlas para tratar más temas en cada reunión', 'Citarlas sin aviso para sorprender a los estudiantes', 'Responde a la falta de información y de tiempo.'),
    sc=[
        ('¿Qué es una actividad breve?', 'Una tarea corta que se puede hacer con poco tiempo', 'Permite que más estudiantes se sumen.'),
        ('abc', '¿Qué es un participante nuevo?', 'Una persona que antes no había participado', 'Un docente invitado', 'Un voluntario que ya participaba', 'Es quien suma a la participación.'),
        ('En Educación Ciudadana: ¿Para qué sirve evaluar?', 'Para decidir qué mantener o cambiar', 'Orienta la mejora de la próxima acción.'),
    ],
    op=("Con la {F} diseña el mes de la comunidad: objetivo medible, una actividad por semana, roles para 10 voluntarios, una respuesta a cada causa, un indicador y un cuidado de seguridad.",
        "Objetivo: 20 estudiantes nuevos. Actividades: semana 1 apoyo escolar, 2 huerto, 3 limpieza, 4 feria de intercambio. Roles: 2 por actividad y 2 de apoyo. Respuestas: información, actividades breves, mostrar resultados. Indicador: estudiantes nuevos. Seguridad: tareas livianas con un docente a cargo.",
        ["responde las causas", "objetivo medible", "cuidado de seguridad"], ["diseño del mes"], ["ignorar el diagnóstico", "omitir un responsable adulto"],
        "Pregunta cómo incluiría a quienes no pueden venir en la tarde."),
    reinforce="Escribe una respuesta para cada causa de no participación.",
    extend="Observa en tu entorno una actividad comunitaria y anota cómo se invita a participar.",
)
