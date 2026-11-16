"""Teatro 3.º y 4.º medio FG: OAC-02 (creación de ejercicios dramáticos individuales y colectivos), clases 1 a 3. Escenas inventadas; sin video real."""
from __future__ import annotations

from fg_teat_common import build

O2 = "FG-TEAT-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (registro de observación de ejemplo, inventado). «Eran las 17:30 y había 6 personas en la fila de una panadería. Un señor miraba su reloj tres veces y suspiraba. "
     "Una niña daba saltitos en el lugar y miraba el mostrador. La vendedora hablaba rápido y sonreía poco. Una señora hizo un reclamo en voz baja y se hizo silencio. "
     "Conclusión escrita al final: la gente estaba enojada.»")
build(
    O2, 1, F,
    use="Aprenderé a observar situaciones cotidianas y a registrarlas separando hechos de interpretaciones, cuidando la privacidad de las personas, para tener material con el que crear ejercicios de expresión dramática.",
    prior=["Distingo gesto, voz, postura y nivel.", "Sé armar una situación con personaje, objetivo y obstáculo.", "Sé que una interpretación es una lectura posible, no un hecho."],
    explain=[
        "Un ejercicio dramático puede nacer de la observación. Observar es mirar y escuchar con atención una situación real, por ejemplo una fila, un paradero o un recreo, y anotar lo que ocurre. El registro incluye cuándo y dónde pasa, cuántas personas hay, qué hacen (sus gestos, su postura, sus movimientos) y cómo hablan (volumen, ritmo, pausas). Esos son hechos: cualquiera que hubiera estado allí podría comprobarlos.",
        "Una interpretación, en cambio, es una lectura posible de los hechos: «estaba enojado», «tenía miedo». Se puede anotar, pero rotulada como interpretación y aparte de los hechos. Para crear conviene apoyarse en los hechos, porque son acciones que el cuerpo y la voz pueden reproducir. Del registro se elige un solo elemento para desarrollar: un gesto, una relación entre dos personas, un cambio de ritmo.",
        "Se observa con respeto. No se identifica a nadie con su nombre ni se graba a personas que no lo han consentido, y nunca se imita a una persona real para burlarse de ella. Lo observado se transforma en un personaje inventado. Si ves una situación que te preocupa por la seguridad de alguien, no la conviertas en ejercicio: avisa a una persona adulta de confianza.",
    ],
    vocab=[("observación", "mirar y escuchar con atención para anotar lo que ocurre"), ("hecho", "dato que se puede comprobar mirando o escuchando"), ("interpretación", "lectura posible de los hechos, no un hecho"), ("registro", "anotación ordenada de lo observado"), ("privacidad", "derecho de las personas a no ser identificadas ni grabadas sin su consentimiento")],
    worked=[
        ("Separar hecho e interpretación", "Un compañero anotó: «La profesora entró molesta y dio un portazo». Sepáralo en hecho e interpretación.", ["Hecho: la profesora entró y la puerta golpeó con fuerza al cerrarse.", "Interpretación: estaba molesta; es una lectura posible y puede rotularse aparte."], "Hecho: entró y la puerta golpeó; interpretación: molesta"),
        ("Elegir qué desarrollar", "En tu registro de un paradero hay seis hechos. ¿Cómo eliges uno para el ejercicio?", ["Escoges el que tiene más acción visible, por ejemplo una persona que mira el camino y camina en círculos.", "Le inventas un personaje y un objetivo, sin parecerte a nadie real."], "Un hecho con acción visible, transformado en personaje inventado"),
    ],
    mistakes=[("Escribir «la gente estaba enojada» como si fuera un dato.", "Es una interpretación; otra persona podría haber visto cansancio o apuro.", "Anota los gestos y la voz que te hicieron pensar eso."),
              ("Imitar a una persona real con su nombre o sus rasgos para hacer reír.", "Puede herirla y exponerla sin su consentimiento.", "Crea un personaje inventado que tome solo una acción observada.")],
    T=[
        ('abc', '¿Cuál de estas es una nota de observación que corresponde a un hecho?', 'Un señor miró su reloj tres veces', 'A la gente de la fila ya le daba lo mismo esperar y quería irse', 'La vendedora es antipática', 'Mirar el reloj tres veces se puede comprobar; las otras son opiniones sobre lo que sienten las personas.'),
        ('abc', '{F} ¿Qué parte del registro es una interpretación y no un hecho?', 'La conclusión «la gente estaba enojada»', 'Había 6 personas en la fila', 'La niña daba saltitos en el lugar', 'La conclusión final nombra un estado interno que no se observa directamente.'),
        ('abc', '¿Qué datos conviene anotar al observar una situación?', 'Cuándo y dónde ocurre, cuántas personas hay y qué hacen y dicen', 'Solo lo que más llamó la atención de cada persona', 'Nombres, direcciones y apodos de cada persona, para poder reconocerla después con facilidad', 'Un registro útil incluye los hechos principales sin identificar a nadie.'),
        ('abc', 'Para observar con respeto antes de crear un ejercicio, ¿qué corresponde?', 'No identificar a nadie y transformar lo observado en un personaje inventado', 'Anotar nombre y apellido de cada persona para recordar bien lo que hizo', 'Imitar a la persona tal cual para que el público la reconozca', 'La privacidad exige que el personaje sea inventado y que nadie quede expuesto.'),
        ('abc', '¿Por qué conviene elegir un solo elemento del registro para el ejercicio?', 'Porque un ejercicio breve se entiende mejor si desarrolla una idea clara', 'Porque los otros elementos no sirven y hay que borrarlos del registro para no confundirse', 'Porque así se evita tener que ensayar', 'Un ejercicio corto con una idea definida es más claro que uno con todo mezclado.'),
        ('abc', 'Un grupo dice: «Copiamos lo que vimos, minuto a minuto». ¿Qué le falta para ser un ejercicio dramático?', 'Elegir qué mostrar y transformar la observación con decisiones propias', 'Sumar personas reales que el curso conozca para que el público se identifique más', 'Hacerlo tan largo como la situación real', 'Crear exige seleccionar y transformar; copiar entero no es una decisión teatral.'),
        ('=', 'Una observación dura 15 minutos y se anotan 3 hechos cada 5 minutos. ¿Cuántos hechos se anotan?', '15//5*3', 'Se calculan los tramos de 5 minutos y se multiplican por los hechos de cada uno.', ' hechos'),
        ('abc', '{F} ¿Cuál de estas notas reescribe la interpretación como un hecho observable?', 'Un señor suspiraba y miraba su reloj tres veces', 'Casi todos querían reclamar y no se atrevían a hacerlo', 'Todos pensaban en irse', 'Es la única que describe lo que se ve y se escucha, sin atribuir pensamientos.'),
        ('abc', 'Quieres dramatizar solo el gesto de la niña que daba saltitos. ¿Qué haces?', 'Lo tomas como acción inicial y le inventas un personaje y un objetivo propios', 'Copias exactamente a la niña que viste en la panadería', 'Dices en voz alta «era una niña que saltaba» mientras actúas', 'El gesto es el punto de partida; el personaje y el objetivo se crean después.'),
        ('abc', 'Una compañera dice: «No necesito observar nada, puedo imaginarlo todo». ¿Qué pierde con esa decisión?', 'Detalles reales de gesto y voz que vuelven creíble el ejercicio', 'La posibilidad de usar después su imaginación, porque observar la apaga y la vuelve rígida', 'El permiso para crear escenas con conflicto', 'La observación aporta detalles verificables; no impide imaginar, pero lo vuelve más concreto.'),
        ('abc', 'Un estudiante propone grabar sin avisar a un grupo del patio para tener «material real». ¿Qué respuesta es adecuada?', 'No: se observa y anota sin grabar a personas que no han consentido', 'Sí, mientras el video no salga del curso', 'Sí, ya que el patio es un lugar abierto donde todos pueden verse y nadie se enterará', 'Grabar sin consentimiento vulnera la privacidad aunque el lugar sea común.'),
        ('=', 'Un registro tiene 12 hechos y 3 interpretaciones. ¿Qué porcentaje de las notas son hechos?', '12*100//(12+3)', 'Se divide el número de hechos entre el total de notas y se pasa a porcentaje.', ' %'),
        ('abc', 'Registro uno: «el hombre estaba nervioso». Registro dos: «el hombre se tocaba la nuca y miraba la puerta cada pocos segundos». ¿Cuál sirve más para crear un ejercicio?', 'El dos, porque entrega acciones que se pueden actuar', 'El uno, porque nombra la emoción con exactitud', 'Ambos, porque las dos frases dicen lo mismo', 'El segundo ofrece acciones concretas; el primero solo nombra una emoción.'),
    ],
    ctx=('=', 'Un curso de 24 estudiantes observa en grupos de 4 y cada grupo anota 5 hechos. ¿Cuántos hechos anotan entre todos los grupos?', '24//4*5', 'Se calcula la cantidad de grupos y se multiplica por los hechos de cada uno.', ' hechos'),
    sc=[
        ("En Teatro: ¿qué diferencia hay entre un hecho y una interpretación al observar?", "El hecho se puede comprobar mirando o escuchando; la interpretación es una lectura posible", "Por eso se anotan en lugares separados."),
        ("¿Se escribe el nombre de las personas observadas en el registro?", "No, se transforma lo observado en un personaje inventado", "Se protege la privacidad de las personas."),
        ("Si al observar notas una situación que te preocupa por la seguridad de alguien, ¿qué haces?", "Aviso a una persona adulta de confianza y no la uso para el ejercicio", "La seguridad de la persona importa más que el ejercicio."),
    ],
    op=("Escoge un lugar cotidiano de ejemplo (una fila, un paradero o un recreo) y observa un fragmento breve a distancia prudente, o imagina uno. Escribe un registro con cinco hechos (sin nombres) y una interpretación rotulada aparte. Luego elige un hecho y di qué personaje inventado y qué objetivo le darías para un ejercicio individual.",
        "Paradero: 1) a las 8:00 había 4 personas; 2) una persona miraba el camino cada pocos segundos; 3) otra se acomodaba la mochila; 4) otra caminaba en un círculo corto; 5) el bus pasó de largo. Interpretación: había apuro. Hecho elegido: mirar el camino; personaje inventado: una estudiante que espera una buena noticia.",
        ["cinco hechos comprobables", "interpretación rotulada aparte", "no identifica a nadie", "el personaje es inventado y tiene objetivo"],
        ["registro y elección del hecho"],
        ["mezclar opiniones con hechos", "usar nombres reales"],
        "Pregunta: «¿otra persona podría comprobar esta nota?». Si no, es una interpretación y va aparte."),
    reinforce="Observa dos minutos un lugar de tu casa o del barrio sin identificar a nadie y anota cuatro hechos y una interpretación.",
    extend="Explica por qué un registro de hechos sirve más que uno de opiniones para construir un personaje.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (observación base, inventada). Una persona espera en una fila para entregar un trámite. Revisa sus papeles tres veces y, al final, se da cuenta de que le falta un documento. "
     "Hay otras cuatro personas en la fila y una ventanilla con una funcionaria.")
build(
    O2, 2, F,
    use="Aprenderé a transformar una observación con la pregunta «¿y si…?», a darle inicio, conflicto y cierre y a distinguir ejercicios individuales de colectivos.",
    prior=["Separo hechos de interpretaciones.", "Sé armar una situación con objetivo y obstáculo.", "Sé que un personaje es inventado."],
    explain=[
        "La imaginación toma la observación y la cambia. Una herramienta simple es la pregunta «¿y si…?»: se cambia una condición de lo observado y se ve qué sucede. ¿Y si el espacio fuera una biblioteca silenciosa? ¿Y si el personaje quisiera ocultar algo? ¿Y si fuera de noche? Cada cambio altera el cuerpo, la voz y el conflicto. Conviene cambiar una condición a la vez para saber cuál produjo el efecto.",
        "Un ejercicio breve tiene tres partes. El inicio presenta quién es el personaje, dónde está y qué quiere. El conflicto aparece cuando algo complica el objetivo. El cierre muestra un cambio: el personaje lo consigue, lo pierde o decide otra cosa. Si al final nada cambió respecto del inicio, falta conflicto.",
        "Un ejercicio individual lo realiza una persona, por ejemplo con objetos imaginarios y sin texto. Un ejercicio colectivo se trabaja entre varias personas y requiere acordar roles, turnos y espacio, como una imagen fija grupal o un diálogo breve. En ambos casos el personaje es inventado, no se burla de personas reales y se evita el contacto físico y cualquier riesgo.",
    ],
    vocab=[("¿y si…?", "pregunta que cambia una condición de lo observado para imaginar algo nuevo"), ("inicio", "parte que presenta personaje, lugar y objetivo"), ("conflicto", "choque entre el objetivo y el obstáculo"), ("cierre", "parte que muestra el cambio que dejó la escena"), ("ejercicio colectivo", "ejercicio que se trabaja entre varias personas con roles y turnos acordados")],
    worked=[
        ("Aplicar «¿y si…?»", "Observación: una persona espera el bus y mira el camino. Propón dos «¿y si…?» distintos.", ["Cambio de objetivo: ¿y si esperara a alguien a quien teme ver?", "Cambio de espacio: ¿y si el paradero estuviera en una calle de noche con poca gente?"], "Un cambio de objetivo y uno de espacio"),
        ("Reconocer las tres partes", "Escena: una persona prepara una mesa. Falta una taza. Pide una a una vecina, que se la presta. Ubica inicio, conflicto y cierre.", ["Inicio: prepara la mesa.", "Conflicto: falta una taza. Cierre: la consigue gracias a su vecina."], "Inicio, conflicto y cierre identificados"),
    ],
    mistakes=[("Cambiar tres condiciones a la vez con «¿y si…?».", "No se sabe cuál produjo el efecto en la escena.", "Prueba un cambio por vez y compara."),
              ("Cerrar la escena igual que como empezó.", "Sin cambio no hay un recorrido que el público perciba.", "Haz que el personaje consiga, pierda o decida algo distinto.")],
    T=[
        ('abc', '¿Qué hace la pregunta «¿y si…?» en la creación?', 'Cambia una condición de lo observado para imaginar algo nuevo', 'Comprueba que la observación fue verdadera antes de usarla en el ejercicio dramático', 'Ordena las escenas de una función', 'Es una herramienta de imaginación: modifica una condición y abre posibilidades.'),
        ('abc', 'En un ejercicio breve, ¿qué ocurre en el inicio?', 'Se presenta quién es el personaje, dónde está y qué quiere', 'Se resuelve el conflicto y el personaje se despide', 'Se explica al público la moraleja de la escena', 'El inicio plantea la situación; la resolución va en el cierre.'),
        ('abc', '¿Cuál es un ejercicio individual?', 'Una persona muestra con su cuerpo cómo prepara algo usando objetos imaginarios', 'Cinco personas forman una imagen fija y luego se mueven juntas siguiendo una señal acordada con anterioridad', 'Dos personas sostienen un diálogo con réplicas que se van respondiendo', 'El individual lo hace una sola persona; los otros requieren acuerdos entre varias.'),
        ('abc', '{F} Si el espacio cambia a una biblioteca silenciosa, ¿qué cambia en la voz y el cuerpo?', 'Voz baja y movimientos contenidos, porque el lugar exige silencio', 'Nada, porque el objetivo sigue siendo el mismo', 'La voz sube de volumen y los gestos se agrandan para que se note', 'El nuevo espacio impone restricciones al volumen y a los movimientos.'),
        ('abc', 'Una escena empieza y termina igual, sin que nada cambie. ¿Qué le falta?', 'Un conflicto o un cambio entre el inicio y el cierre', 'Más personajes en escena, para que haya más movimiento entre el inicio y el final', 'Un fondo musical para marcar la emoción', 'Sin conflicto ni cambio no hay recorrido; más personajes o música no lo arreglan.'),
        ('abc', '{F} ¿Cuál «¿y si…?» cambia el objetivo del personaje?', '¿Y si quisiera ocultar que le falta el documento?', '¿Y si la fila estuviera dentro de una biblioteca?', '¿Y si ocurriera de noche?', 'Las otras dos cambian el espacio y el tiempo; solo la primera cambia lo que el personaje quiere.'),
        ('=', 'Seis grupos muestran cada uno una imagen fija de 45 segundos y entre grupo y grupo hay 5 cambios de 15 segundos. ¿Cuántos segundos dura todo?', '6*45+5*15', 'Se suman los segundos de las imágenes y los de los cambios.', ' segundos'),
        ('abc', 'Debes mostrar sin texto que el personaje descubre que le falta un documento. ¿Qué acción es más clara?', 'Revisar de nuevo los bolsillos y quedarse quieta', 'Decir «me falta un documento» y luego buscarlo con calma', 'Sentarse y mirar al público sonriendo', 'La acción visible y el quiebre de movimiento muestran el descubrimiento sin explicarlo.'),
        ('abc', '¿Cuál plan tiene inicio, conflicto y cierre?', 'Un grupo entra a ordenar una sala, descubre que falta una pieza, la encuentra y sale', 'Un grupo entra, ordena la sala, sigue ordenando y sigue ordenando', 'Un grupo entra, descubre que falta una pieza y la escena termina sin cierre', 'El primero tiene las tres partes; el segundo no tiene conflicto y el tercero no tiene cierre.'),
        ('abc', 'Dos equipos parten de la misma observación y crean escenas muy distintas. ¿Qué lo explica?', 'Tomaron decisiones distintas al preguntar «¿y si…?» y al elegir qué desarrollar', 'Uno de los dos observó mal la situación y por eso no pudo imaginar nada parecido', 'Solo uno de los equipos tuvo imaginación', 'La misma observación admite muchos caminos según las decisiones del equipo.'),
        ('abc', 'Un grupo crea una escena en que un personaje se burla de una persona real del curso, con su nombre. ¿Qué corresponde?', 'Cambiar el personaje y los datos para que nadie pueda ser identificado ni herido', 'Dejarla tal cual si el curso se ríe, porque entonces nadie se siente ofendido', 'Preguntar al curso si le parece bien la burla', 'Un ejercicio no puede exponer ni herir a una persona real; se inventa un personaje distinto.'),
        ('=', 'Un taller dura 36 minutos. Cuatro grupos presentan un ejercicio de 5 minutos y hay 3 cambios de 1 minuto entre ellos. ¿Cuántos minutos sobran?', '36-(4*5+3*1)', 'Se calcula el tiempo ocupado por presentaciones y cambios y se resta del total.', ' minutos'),
        ('abc', 'Final 1: el personaje encuentra el documento en su bolsillo. Final 2: se lo presta otra persona de la fila a cambio de pasar primero. ¿Cuál agrega una relación nueva entre personajes?', 'El final 2, porque aparece un trato entre dos personajes', 'El final 1, porque resuelve el problema rápido', 'Ninguno, pues el personaje sigue en la fila', 'En el segundo hay un intercambio entre personas; en el primero el cambio es solo del personaje.'),
    ],
    ctx=('=', 'Diez estudiantes presentan ejercicios individuales de 3 minutos, uno tras otro, con 1 minuto de cambio entre quienes presentan. ¿Cuántos minutos dura todo?', '10*3+9*1', 'Hay diez presentaciones y nueve cambios entre ellas.', ' minutos'),
    sc=[
        ("En Teatro: ¿qué es un conflicto en un ejercicio breve?", "El choque entre el objetivo del personaje y lo que se lo dificulta", "Es lo que mueve el recorrido del inicio al cierre."),
        ("¿Qué partes tiene un ejercicio breve?", "Inicio, conflicto y cierre", "Las tres partes dan un recorrido completo."),
        ("¿Se puede usar a una persona real del curso como personaje para burlarse?", "No, el personaje debe ser inventado y respetuoso", "Burlarse de alguien real lo expone y lo daña."),
    ],
    op=("Parte de esta observación de ejemplo: una persona espera su turno en una oficina y se le cae su carpeta con papeles. Escribe dos «¿y si…?» (uno de objetivo y otro de espacio), elige uno y arma el inicio, el conflicto y el cierre en una oración cada uno. Indica si será individual o colectivo y cómo evitarás cualquier riesgo.",
        "¿Y si quisiera esconder un papel? (objetivo) ¿Y si la oficina fuera una biblioteca? (espacio) Inicio: una persona espera su turno con una carpeta. Conflicto: se cae y otra persona se acerca a ayudar. Cierre: acepta ayuda pero conserva un papel oculto. Colectivo, de dos; sin contacto, a un brazo de distancia.",
        ["dos «¿y si…?» distintos", "inicio, conflicto y cierre completos", "hay un cambio en el cierre", "señala una medida de seguridad"],
        ["hoja con las preguntas y las tres partes"],
        ["cierre igual al inicio", "no indicar medidas de seguridad"],
        "Pregunta: «¿qué cambió entre el inicio y el cierre?». Si nada, falta conflicto."),
    reinforce="Escoge un hecho de una observación anterior y formula tres «¿y si…?» que cambien objetivo, espacio o tiempo.",
    extend="Explica por qué cambiar una sola condición con «¿y si…?» ayuda a decidir qué versión conservar.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (ejercicio colectivo de ejemplo, inventado). «La sala de espera», 4 personas. Espacio: 4 sillas en fila frente al público. Objetos: una revista de papel y un bolso. "
     "Luz: la de la sala, encendida. Sin música. Conflicto: dos personas quieren la misma silla, la del extremo.")
build(
    O2, 3, F,
    use="Aprenderé a usar recursos del lenguaje teatral (expresión, dramatización, espacio, objetos, luz y sonido) para tomar decisiones de puesta en escena que muestren el conflicto de forma segura.",
    prior=["Sé armar inicio, conflicto y cierre.", "Sé usar cuerpo y voz con un propósito.", "Sé probar un cambio por vez y comparar."],
    explain=[
        "La puesta en escena es el conjunto de decisiones sobre cómo se muestra la historia: dónde se ubican las personas y los objetos (espacio), qué objetos se usan (utilería), qué se viste (vestuario), cómo se ilumina y qué sonidos hay. Se suma a la expresión (el trabajo del cuerpo y la voz), a la dramatización (mostrar la historia con acciones) y al trabajo en equipo. Cada decisión debe ayudar a que se entienda el conflicto y el propósito.",
        "Los objetos y la ubicación comunican. Un objeto ayuda cuando muestra una acción o una relación, por ejemplo un bolso que alguien deja en una silla para reservarla. Ubicar a las personas en lados opuestos hace visible una disputa. Poner demasiados objetos distrae de la acción. En una sala de clases se usa la iluminación que ya existe y se evita todo lo que produzca calor o fuego.",
        "La seguridad es una decisión de puesta en escena: un pasillo despejado para el público, sin cables ni objetos en el suelo, sillas estables, nadie sobre muebles y nada de velas ni cosas que se prendan. Para elegir entre dos ideas se prueban ambas y se compara cuál comunica mejor el propósito del grupo.",
    ],
    vocab=[("puesta en escena", "conjunto de decisiones sobre espacio, objetos, luz, sonido y movimiento de una escena"), ("utilería", "objetos que se usan o manipulan en escena"), ("vestuario", "prendas que usan los personajes"), ("dramatización", "mostrar una historia con acciones"), ("recurso", "elemento del lenguaje teatral que se usa para expresar")],
    worked=[
        ("Elegir una ubicación", "Dos personajes se disputan una silla. ¿Cómo ubicarías a las dos personas para que el público vea el conflicto?", ["Las pongo a cada lado de la silla, mirándose, y no de espaldas al público.", "Así el público ve ambos rostros y entiende que la silla es el centro."], "A cada lado de la silla, de frente al público"),
        ("Revisar la seguridad", "Un grupo quiere poner un cable alargador cruzado en el suelo para encender una lámpara. ¿Qué conviene?", ["El cable cruzado es un riesgo de tropiezo.", "Se usa solo la luz de la sala o una fuente que no atraviese el espacio."], "No usarlo; usar la luz que ya existe"),
    ],
    mistakes=[("Llenar la escena de objetos «para que se vea más».", "Los objetos de más distraen de la acción y complican los cambios.", "Deja solo los que ayudan a mostrar una acción o relación."),
              ("Resolver la luz con velas o fuentes de calor.", "Es un riesgo de incendio y quemaduras.", "Usa la iluminación de la sala y comunica el clima con el cuerpo y la voz.")],
    T=[
        ('abc', '¿Qué es la puesta en escena?', 'El conjunto de decisiones sobre espacio, objetos, luz y sonido de una escena', 'El texto escrito que memorizan quienes actúan antes de la función', 'La reacción del público al final de la función en la sala', 'Es lo que se decide para mostrar la historia; no es el texto ni la reacción del público.'),
        ('abc', '{F} ¿Cuál es el conflicto del ejercicio?', 'Dos personas quieren la misma silla', 'Se perdió el bolso del grupo', 'Faltan sillas para las cuatro personas del ejercicio', 'El conflicto está dicho: dos personas buscan la silla del extremo; hay una silla para cada persona.'),
        ('abc', 'La utilería es', 'los objetos que se usan o manipulan en escena', 'las prendas que usa cada personaje para identificarse', 'el espacio vacío entre el público y quienes actúan', 'La utilería son los objetos; las prendas son el vestuario.'),
        ('abc', '{F} ¿Qué decisión de puesta en escena haría más visible la disputa por la silla?', 'Dejar libre solo la silla del extremo y ubicar a las dos personas en lados opuestos', 'Poner sillas de sobra para que nadie quiera la del extremo', 'Apagar las luces de la sala para que se concentren', 'Una sola silla libre y dos personas enfrentadas hacen visible el conflicto.'),
        ('abc', '¿Cuál es el mejor motivo para usar un objeto en escena?', 'Que ayude a mostrar una acción o una relación entre personajes', 'Que llene el espacio vacío para que no se note', 'Que sea el más llamativo que se encuentre a mano', 'Un objeto es un recurso al servicio de la acción, no un relleno.'),
        ('abc', 'Sobre la luz en una sala de clases, ¿qué es seguro?', 'Usar solo la iluminación que ya tiene la sala, sin cables sueltos ni velas', 'Usar velas o encendedores para dar clima a la escena', 'Cubrir las lámparas con telas gruesas de colores para cambiar el ambiente del lugar', 'Las velas y las telas sobre lámparas pueden causar fuego; la luz de la sala no tiene ese riesgo.'),
        ('=', 'En cada ensayo el equipo prueba 3 ubicaciones de sillas de 4 minutos cada una y dedica 3 minutos a comentar. Hace 2 ensayos. ¿Cuántos minutos usa en total?', '2*(3*4+3)', 'Cada ensayo suma las pruebas y el comentario; se multiplica por dos ensayos.', ' minutos'),
        ('abc', '¿Cuál es una ubicación segura del público?', 'Sentado a distancia, con un pasillo despejado y sin cables ni objetos en el suelo', 'Sentado en el borde de la escena para ver de cerca, aunque tengan que esquivar objetos', 'De pie detrás de quienes actúan para ver todo', 'Un público seguro tiene distancia y pasillo libre; los otros arriesgan choques o tropiezos.'),
        ('abc', 'El ejercicio quiere mostrar el cansancio de esperar. ¿Qué decisión ayuda más?', 'Cambiar de postura con lentitud y mirar varias veces el reloj', 'Moverse con rapidez entre las sillas, sin quedarse quieto jamás', 'Agregar música alegre y fuerte durante toda la escena de espera', 'La lentitud y el reloj muestran espera; la rapidez y la música alegre dicen lo contrario.'),
        ('abc', 'El equipo tiene dos ideas de cierre: una persona sale y deja el bolso, o las cuatro quedan inmóviles. ¿Cómo decide?', 'Prueba ambas y compara cuál comunica mejor el propósito', 'Elige la que sea más fácil de ensayar para no perder tiempo del taller', 'Elige la de la persona que dirige, sin probar', 'La decisión se apoya en una prueba y en el propósito, no en la comodidad ni en la autoridad.'),
        ('abc', 'Un grupo llena la escena con ocho objetos distintos. ¿Qué problema puede tener?', 'Que los objetos distraigan de la acción y del conflicto', 'Que no alcance el espacio para que el público se siente', 'Que los personajes hablen demasiado bajo', 'Los objetos de más compiten con la acción; los otros problemas no vienen de ellos.'),
        ('=', 'Una función dura 40 minutos. Cinco equipos presentan 5 minutos cada uno y hay 4 cambios de utilería de 2 minutos. ¿Cuántos minutos quedan para comentarios?', '40-(5*5+4*2)', 'Se restan las presentaciones y los cambios al tiempo total.', ' minutos'),
        ('abc', 'Dos equipos usan las mismas cuatro sillas: el primero en fila frente al público y el segundo en círculo con el público alrededor. ¿Qué cambia?', 'La relación entre las personas y desde dónde se ve cada rostro', 'El texto que dicen los personajes en cada silla', 'La cantidad de sillas que tiene disponibles cada grupo', 'La ubicación cambia la mirada del público y las relaciones; el texto y la cantidad no cambian.'),
    ],
    ctx=('ab', 'A tu equipo le falta un bolso para el ejercicio. ¿Qué conviene hacer?', 'Usar un objeto seguro de la sala parecido al bolso o un objeto imaginario bien definido', 'Cancelar el ejercicio completo porque sin ese bolso exacto no hay escena posible', 'El objeto cumple una función en la escena; se puede reemplazar sin perder la acción.'),
    sc=[
        ("En Teatro: ¿qué es la utilería?", "Los objetos que se usan o manipulan en escena", "No incluye el vestuario ni la luz."),
        ("¿Qué se evita siempre en la luz de una sala de clases?", "Velas, encendedores y todo lo que produzca calor o fuego", "Es un riesgo para las personas y la sala."),
        ("¿Cómo se elige entre dos ideas de puesta en escena?", "Probando ambas y comparando cuál comunica mejor el propósito", "La prueba aporta evidencia para decidir."),
    ],
    op=("Escoge un ejercicio de ejemplo: «La sala de espera», «La fila del banco» o «El paradero». Escribe tus decisiones de puesta en escena: dónde ubicas a las personas, qué dos objetos usas y por qué, qué sonido o silencio eliges y qué medidas de seguridad tomas. Todo debe hacerse sin velas, sin cables en el suelo y sin subirse a muebles.",
        "Sala de espera: cuatro sillas en semicírculo; un bolso y una revista de papel; el bolso reserva una silla y la revista muestra la espera; solo silencio; pasillo despejado y sin cables.",
        ["ubicación con una razón", "dos objetos justificados", "sonido o silencio elegido", "incluye medidas de seguridad"],
        ["hoja con las decisiones y sus razones"],
        ["usar demasiados objetos", "olvidar la seguridad"],
        "Pregunta: «¿qué muestra este objeto que no mostrarían las personas solas?». Si nada, sobra."),
    reinforce="Dibuja o describe la ubicación de tres sillas y dos objetos para un conflicto entre dos personas y explica qué muestra cada decisión.",
    extend="Explica por qué la seguridad es una decisión de puesta en escena y no un trámite aparte.",
)
