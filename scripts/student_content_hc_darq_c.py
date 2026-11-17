"""Diseño y arquitectura 3.º y 4.º medio HC: OAC-05 (argumentar juicios estéticos) y OAC-06 (evaluar críticamente procesos y resultados). Casos, obras y proyectos inventados; sin imágenes ni software reales."""
from __future__ import annotations

from hc_darq_common import build

O5 = "AR-DARQ-3y4-OAC-05"
O6 = "AR-DARQ-3y4-OAC-06"

# ============================================================ OAC-05, clase 1
F = ("Ficha 20 (obra de ejemplo, inventada). «Mirador del Faro», mirador público de una costa ficticia, época C (de ejemplo): plataforma de hormigón de 8 m por 5 m con baranda de acero; una pasarela de 20 m de largo y 2 m de ancho, sin escalones, que se curva suavemente hacia el mar; una banca continua de madera a lo largo de la baranda; colores grises y madera clara; sin techo. "
     "Comentario 1: «Me gusta». "
     "Comentario 2: «La pasarela se curva suavemente y eso guía la mirada hacia el mar». "
     "Comentario 3: «Es horrible, no sé por qué». "
     "Comentario 4: «Es un buen mirador porque la banca continua permite que varias personas se sienten juntas mirando el mar y la pasarela sin escalones lo hace usable por todas las personas».")
build(
    O5, 1, F,
    use="Aprenderé a distinguir descripción, interpretación, juicio de gusto y juicio estético fundamentado, y a pasar del «me gusta» a una valoración con criterio y evidencia.",
    prior=["Sé describir una obra con rasgos formales.", "Sé interpretar con evidencia.", "Sé respetar opiniones distintas."],
    explain=[
        "Al hablar de una obra de diseño o arquitectura se pueden decir cuatro tipos de cosas. La descripción dice lo que hay (una pasarela de 20 m). La interpretación dice qué sugiere (la curva guía la mirada). El juicio de gusto dice si agrada («me gusta»), y es una vivencia válida, pero no explica nada. El juicio estético fundamentado valora la obra con un criterio y con evidencia observable.",
        "Un juicio fundamentado tiene tres partes: el juicio («es un buen mirador»), el criterio con que se valora (por ejemplo, uso compartido e inclusión) y la evidencia (la banca continua y la pasarela sin escalones). Un criterio es una cualidad que se espera de la obra según su propósito. Dos personas pueden valorar la misma obra con criterios distintos; entonces se conversa sobre cuál pesa más para ese propósito.",
        "Que una obra no nos guste no significa que esté mal hecha, ni que nos guste significa que sea mejor que otras. Por eso se argumenta, y se respeta a quien llega a otra conclusión. Las obras de esta clase son inventadas.",
    ],
    vocab=[("juicio de gusto", "afirmación de si algo agrada, sin razones"), ("juicio estético fundamentado", "valoración con criterio y evidencia observable"), ("criterio", "cualidad esperada de una obra según su propósito"), ("evidencia", "rasgo observable que respalda un juicio"), ("interpretación", "lo que la obra sugiere, apoyado en rasgos")],
    worked=[
        ("Distinguir tipos de enunciado", "En la ficha, ¿«Me gusta» es un juicio fundamentado?", ["«Me gusta» solo dice si agrada, sin criterio ni evidencia.", "Es un juicio de gusto."], "No: es un juicio de gusto"),
        ("Comparar longitudes", "¿Cuántos metros más larga es la pasarela (20 m) que el lado largo de la plataforma (8 m)?", ["Se resta la longitud menor a la mayor.", "20 − 8 = 12."], "12 m"),
    ],
    mistakes=[("Decir «es horrible» y no explicar por qué.", "Nadie puede comprobar ni discutir una afirmación sin razones.", "Nombra qué rasgo te produce esa sensación y con qué criterio lo valoras."),
              ("Creer que si algo no gusta, está mal hecho.", "El gusto personal no mide si la obra cumple su propósito.", "Evalúa propósito, criterios y evidencia, además de tu gusto.")],
    T=[
        ('abc', '¿Qué diferencia un juicio estético fundamentado de un juicio de gusto?', 'El fundamentado da criterios y evidencia observable; el de gusto solo dice si agrada', 'El fundamentado es más largo y usa más adjetivos que el de gusto', 'El de gusto es incorrecto, porque el gusto no puede ser una vivencia válida', 'La diferencia está en las razones observables que sostienen el juicio.'),
        ('abc', '{F} ¿Cuál comentario describe un rasgo y su efecto, sin juzgar?', 'Comentario 2: la pasarela se curva y guía la mirada hacia el mar', 'Comentario 1: me gusta, porque el mirador me parece agradable', 'Comentario 3: es horrible, y por eso nadie querría usarlo', 'Solo el segundo nombra un rasgo observable y un efecto.'),
        ('=', '{F} ¿Cuántos m² tiene la plataforma (8 m por 5 m)?', '8*5', 'El área es largo por ancho.', ' m²'),
        ('abc', '{F} ¿Cuál comentario es un juicio fundamentado?', 'El comentario 4, porque da un criterio (inclusión) y evidencia (banca continua y pasarela sin escalones)', 'El comentario 1, porque dice que le gusta y eso es una vivencia válida', 'El comentario 3, porque es el único que expresa una opinión firme sobre la obra', 'Solo el cuarto combina juicio, criterio y evidencia.'),
        ('=', '{F} ¿Cuántos m² tiene la pasarela (20 m por 2 m)?', '20*2', 'El área es largo por ancho.', ' m²'),
        ('abc', '{F} ¿Qué criterio usa el comentario 4 para su juicio?', 'Uso compartido e inclusión', 'La antigüedad de la obra', 'El precio de los materiales', 'Habla de sentarse juntos y de una pasarela usable por todas las personas.'),
        ('abc', '{F} ¿Cómo se mejora el comentario 3 («Es horrible, no sé por qué»)?', 'Nombrar el rasgo y el criterio: «me parece frío porque casi todo es gris y no hay sombra, y espero comodidad»', 'Repetir «es horrible» con más fuerza y agregar que todos opinan igual', 'Decir «no me gusta y punto», porque el gusto no necesita explicación para argumentar', 'Agrega un rasgo observable y un criterio, lo que permite discutirlo.'),
        ('abc', '{F} ¿Qué evidencia sustenta que la pasarela guía la mirada hacia el mar?', 'Que se curva suavemente hacia el mar a lo largo de 20 m', 'Que el piso tiene ranuras que ayudan a avanzar en línea recta', 'Que la baranda es de acero y rodea toda la plataforma', 'La curva hacia el mar es el rasgo que orienta la mirada.'),
        ('abc', 'Una compañera dice: «que algo no me guste no significa que esté mal hecho». ¿Es correcto?', 'Sí: el gusto personal no basta para juzgar; hay que mirar el propósito, los criterios y la evidencia', 'No, porque si una obra no le gusta a una persona es señal de que está mal hecha', 'Sí, y por eso ninguna persona puede dar razones sobre una obra', 'El gusto es una vivencia; el juicio fundamentado necesita criterios y evidencia.'),
        ('abc', '{F} Dos personas discrepan: una valora la obra por estar abierta al paisaje y otra la critica por no tener techo. ¿Qué enfoque es mejor?', 'Reconocer que usan criterios distintos y revisar con evidencia cuál pesa más para el propósito', 'Decidir que una de las dos se equivoca, según quién tenga más experiencia', 'No opinar más del mirador para evitar discusiones y que cada una piense lo suyo', 'Cada una usa un criterio válido y se decide según el propósito del mirador.'),
        ('abc', '{F} ¿Cuál enunciado es una interpretación?', 'La curva suave de la pasarela sugiere calma y un camino sin apuro', 'La pasarela tiene 20 m de largo y 2 m de ancho, sin escalones', 'Me gusta la pasarela porque me hace sentir cómoda', 'Dice qué sugiere un rasgo; no es una medida ni un gusto.'),
        ('abc', '{F} ¿Qué juicio fundamentado sobre el mirador es más completo?', 'Es un buen mirador inclusivo: la pasarela sin escalones y la banca continua lo muestran, aunque sin techo se usa menos con lluvia', 'El mejor mirador de la costa, porque su plataforma de hormigón es muy resistente', 'Un mirador malo, porque no tiene techo y eso basta para descartar toda la obra', 'Incluye juicio, criterios, evidencia y una limitación.'),
        ('abc', '¿Qué orden facilita argumentar un juicio estético?', 'Describir, interpretar y luego juzgar con criterio y evidencia', 'Juzgar primero para fijar una postura y buscar razones que la sostengan después', 'Interpretar primero y describir solo si alguien lo pide', 'Cada paso se apoya en el anterior.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Pienso que el mirador funciona bien porque la pasarela de 2 m de ancho no tiene escalones (criterio: accesibilidad) y la banca continua permite sentarse en grupo (criterio: uso compartido)». ¿Qué hace bien?', 'Da un juicio con dos criterios y la evidencia de cada uno', 'Solo dice que le gusta', 'Describe sin juzgar', 'El texto combina juicio, criterios y evidencia de la ficha.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué partes tiene un juicio fundamentado?", "Juicio, criterio y evidencia", "Sin ellas, el juicio no se puede discutir."),
        ("¿Es válido un juicio de gusto?", "Sí como vivencia, pero no basta como argumento", "No explica por qué la obra funciona o no."),
        ("¿Qué se hace si dos personas usan criterios distintos?", "Se revisa cuál criterio pesa más para el propósito de la obra", "Así se evita descalificar a una de ellas."),
    ],
    op=("Obra de ejemplo (inventada): «Pasaje de los Faroles», pasaje peatonal de 40 m de largo y 4 m de ancho en un barrio ficticio, época C (de ejemplo): piso de adoquines claros, ocho faroles de metal negro a ambos lados, una hilera de macetas con plantas, tres bancas sin respaldo y una rampa suave en cada entrada. Escribe una descripción de dos rasgos, una interpretación y un juicio fundamentado con dos criterios y dos evidencias.",
        "Descripción: piso de adoquines claros y ocho faroles de metal negro. Interpretación: los faroles repetidos a ambos lados sugieren un recorrido ordenado. Juicio: es un buen pasaje porque las rampas en las entradas lo hacen accesible (criterio: inclusión; evidencia: rampas) y las macetas y bancas invitan a quedarse (criterio: uso compartido; evidencia: bancas y plantas), aunque las bancas sin respaldo son menos cómodas.",
        ["distingue descripción, interpretación y juicio", "usa dos criterios con evidencia", "reconoce un límite"],
        ["hoja con descripción, interpretación y juicio"],
        ["escribir solo «me gusta»", "juzgar sin criterio", "mezclar descripción con opinión"],
        "Pregunta: «¿qué rasgo y qué criterio sostienen tu juicio?». Si falta uno, pídele agregarlo."),
    reinforce="Elige un objeto de tu casa y escribe tres frases: una descripción, una interpretación y un juicio con un criterio.",
    extend="Explica por qué dos juicios fundamentados distintos sobre la misma obra pueden ser ambos válidos.",
)

# ============================================================ OAC-05, clase 2
F = ("Ficha 21 (cuatro bancas de ejemplo de un concurso escolar ficticio). "
     "Pieza «Ola»: curva continua de madera, un solo material y color uniforme; cómoda para 8 de 10 personas que la probaron; difícil de fabricar. "
     "Pieza «Mosaico»: muchos colores y materiales mezclados sin orden; se ve llamativa; cómoda para 5 de 10. "
     "Pieza «Bloque»: cubo de hormigón liso con proporciones muy equilibradas; muy resistente; cómoda para 3 de 10. "
     "Pieza «Reciclada»: tablones reutilizados, líneas rectas y un detalle de color en los bordes; fácil de mantener; cómoda para 7 de 10. "
     "Criterios del concurso: unidad (las partes se ven como un conjunto), contraste (diferencias que llaman la atención), proporción (equilibrio entre las partes), comodidad y sustentabilidad.")
build(
    O5, 2, F,
    use="Aprenderé a usar criterios estéticos, funcionales y ambientales para valorar una pieza de diseño, a darles importancia según el propósito y a leer evidencia con sus límites.",
    prior=["Sé distinguir un juicio de gusto de uno fundamentado.", "Sé calcular porcentajes sencillos.", "Sé que el propósito guía los criterios."],
    explain=[
        "Los criterios son las cualidades con que se valora una pieza. Los criterios estéticos incluyen la unidad (las partes forman un conjunto), la armonía (partes que se combinan bien), el contraste (diferencias que llaman la atención), la proporción (equilibrio entre las partes), el ritmo y la originalidad. Los criterios funcionales incluyen la comodidad, la seguridad, la accesibilidad y la mantención. Los criterios ambientales incluyen el origen del material, la duración y la posibilidad de reutilizar o reciclar.",
        "Ningún criterio es universal: se explicitan antes de juzgar y se les da importancia según el propósito. Para una banca de patio lluvioso y con poco presupuesto, la durabilidad, la mantención y la sustentabilidad pesan más que la originalidad. Cuando hay datos, como una prueba de comodidad con 10 personas, se leen como evidencia con sus límites: una muestra pequeña sirve de indicio, pero no demuestra lo que opina todo un liceo.",
        "Valorar con varios criterios evita quedarse con una sola cualidad, como «se ve llamativa» o «es muy resistente». Una pieza puede destacar en un criterio y fallar en otro, y el juicio honesto lo reconoce. Las piezas de esta clase son inventadas.",
    ],
    vocab=[("unidad", "partes que se ven como un conjunto"), ("contraste", "diferencias que llaman la atención"), ("proporción", "equilibrio entre el tamaño de las partes"), ("ponderar", "dar más o menos importancia a cada criterio"), ("muestra", "grupo de personas que participa en una prueba")],
    worked=[
        ("Leer evidencia", "¿Qué porcentaje de las personas encontró cómoda la pieza «Reciclada» (7 de 10)?", ["Se divide 7 entre 10 y se multiplica por 100.", "7 × 100 ÷ 10 = 70."], "70 %"),
        ("Identificar un criterio", "«Bloque» tiene proporciones muy equilibradas. ¿Qué criterio estético la favorece?", ["Las proporciones equilibradas son un equilibrio entre las partes.", "Es la proporción."], "La proporción"),
    ],
    mistakes=[("Elegir la pieza ganadora mirando un solo criterio.", "Se ignoran cualidades importantes del propósito.", "Valora con todos los criterios y justifica el peso de cada uno."),
              ("Creer que una prueba con 10 personas demuestra lo que opina todo el liceo.", "Una muestra pequeña es un indicio, no una prueba general.", "Declara el límite de la evidencia al citarla.")],
    T=[
        ('abc', '¿Qué es la unidad en una pieza de diseño?', 'Que las partes se vean como un conjunto coherente', 'Que la pieza tenga un solo color y un solo material', 'Que la pieza se fabrique de una sola pieza física, sin uniones', 'La unidad es coherencia entre las partes, no cantidad de colores o piezas.'),
        ('abc', '{F} ¿Qué pieza resultó cómoda para más personas?', '«Ola», que logró 8 de 10', '«Bloque», que logró 3 de 10', '«Reciclada», que logró 7 de 10', 'La ficha da 8 de 10 para «Ola», el mayor valor.'),
        ('=', '{F} ¿Cuántas personas más encontraron cómoda «Ola» que «Bloque»?', '8-3', 'Se resta lo que dijo «Bloque» a lo que dijo «Ola».', ' personas'),
        ('abc', '{F} ¿Qué criterio estético favorece a «Mosaico»?', 'El contraste, porque se ve llamativa', 'La unidad, porque todo se combina como un conjunto', 'La proporción, porque sus partes están equilibradas', 'Mezclar colores y materiales sin orden da contraste, pero resta unidad.'),
        ('abc', '{F} ¿Qué pieza destaca en sustentabilidad según la ficha?', '«Reciclada», hecha con tablones reutilizados', '«Bloque», por ser de hormigón muy resistente y duradero', '«Ola», por su curva continua de madera de un solo material', 'La ficha dice que «Reciclada» usa tablones reutilizados y es fácil de mantener.'),
        ('abc', '{F} ¿Qué se puede decir de «Bloque» con la ficha?', 'Es fuerte en proporción y resistencia, pero débil en comodidad', 'Es fuerte en comodidad y débil en proporción y resistencia', 'Es débil en todos los criterios, porque solo 3 de 10 lo encontraron cómodo', '«Bloque» tiene proporciones equilibradas y es muy resistente, pero solo 3 de 10 lo encontraron cómodo.'),
        ('=', '{F} ¿Qué porcentaje de las personas encontró cómoda la pieza «Ola» (8 de 10)?', '8*100//10', 'Se divide 8 entre 10 y se multiplica por 100.', ' %'),
        ('abc', '{F} Un grupo juzga solo por unidad. ¿Qué problema tiene?', 'Ignora la comodidad y la sustentabilidad, que también son criterios del concurso', 'Ninguno, porque la unidad resume todo lo que importa de una pieza', 'Que la unidad es un criterio funcional y no uno estético', 'El concurso tiene cinco criterios y juzgar con uno deja fuera a los demás.'),
        ('abc', '{F} ¿Qué pieza equilibra mejor comodidad y sustentabilidad?', '«Reciclada»: cómoda para 7 de 10 y hecha con tablones reutilizados', '«Bloque»: cómoda para 3 de 10, muy resistente y de proporciones equilibradas', '«Mosaico»: cómoda para 5 de 10, llamativa y con muchos materiales mezclados', '«Reciclada» tiene buen dato de comodidad y un material reutilizado.'),
        ('abc', '{F} Alguien dice: «“Ola” gana porque 8 de 10 es lo más importante». ¿Qué argumento es más completo?', 'La comodidad importa, pero «Ola» es difícil de fabricar y «Reciclada» es más sustentable: hay que ponderar los criterios', 'Tiene razón: el criterio en que una pieza saca el mayor puntaje siempre decide el ganador', 'Hay que descartar la comodidad, porque depende de las personas y no puede medirse', 'Ponderar los criterios según el propósito evita decidir con uno solo.'),
        ('abc', 'Antes de juzgar con criterios, ¿qué hay que hacer con ellos?', 'Explicitarlos y darles importancia según el propósito', 'Elegirlos al final para que calcen con la pieza favorita', 'Usar solo los que le gustan a una persona', 'Los criterios se definen antes de juzgar para que sean justos.'),
        ('abc', '{F} El propósito es una banca para un patio lluvioso y con poco presupuesto. ¿Qué ponderación es más coherente?', 'Dar más importancia a durabilidad, mantención y sustentabilidad que a la originalidad', 'Dar importancia solo a la originalidad, porque es lo que más distingue a una pieza', 'No ponderar nada y dar el mismo peso a todos los criterios sin mirar el propósito', 'El propósito indica qué criterios pesan más.'),
        ('abc', '¿Qué límite tiene una prueba de comodidad con solo 10 personas?', 'Es una muestra pequeña: sirve como indicio, pero no demuestra lo que opina todo el liceo', 'Ninguno, porque 10 personas son suficientes para conocer la opinión de todo el liceo', 'Que la comodidad no se puede medir con pruebas de uso, solo con opiniones de expertos', 'Una muestra pequeña no representa a toda la comunidad.'),
    ],
    ctx=('abc', 'Un grupo escribe: «Elegimos “Reciclada”: es cómoda para 7 de 10 (indicio con muestra pequeña), usa material reutilizado y es fácil de mantener; “Ola” es más cómoda, pero difícil de fabricar». ¿Qué hace bien?', 'Valora con varios criterios, cita datos y declara el límite de la evidencia', 'Elige por una sola cualidad', 'Decide por gusto personal', 'Usa criterios múltiples y reconoce el límite de la muestra.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué significa ponderar criterios?", "Darles más o menos importancia según el propósito", "No todos los criterios pesan igual."),
        ("¿Qué tipos de criterios se usan al valorar una pieza?", "Estéticos, funcionales y ambientales", "Una valoración completa combina los tres tipos de criterio."),
        ("¿Qué límite tiene una muestra pequeña?", "No demuestra lo que opina toda una comunidad", "Solo da un indicio y no una prueba general."),
    ],
    op=("Cuatro lámparas de escritorio de ejemplo (inventadas) compiten en un concurso escolar. «Faro»: base ancha de metal reciclado, luz regulable, cómoda para 9 de 10 personas, de aspecto sobrio. «Pétalo»: pantalla de papel en forma de flor, muy original, cómoda para 6 de 10, se daña con la humedad. «Cubo»: cubo de madera liso y proporciones equilibradas, cómoda para 4 de 10. «Arco»: brazo curvo de plástico reciclado, cómoda para 7 de 10, fácil de reparar. Define tres criterios para un liceo con poco presupuesto, dales importancia, y escribe tu juicio con evidencia y un límite.",
        "Criterios: comodidad (mayor peso), sustentabilidad y mantención (peso medio) y originalidad (menor peso). Juicio: elijo «Faro»: cómoda para 9 de 10 y de metal reciclado; «Arco» es una buena segunda opción por ser fácil de reparar. Límite: son solo 10 personas, así que es un indicio.",
        ["define criterios antes de juzgar", "da importancia a los criterios según el propósito", "cita evidencia y declara un límite"],
        ["hoja con criterios, pesos y juicio"],
        ["juzgar con un solo criterio", "elegir criterios al final", "no declarar el límite de la muestra"],
        "Pregunta: «¿qué criterio pesa más y por qué?». Si no puede responder, pídele volver al propósito."),
    reinforce="Elige dos sillas de tu casa y compara cuál cumple mejor tres criterios (comodidad, resistencia y apariencia), explicando con qué rasgos.",
    extend="Explica cómo cambiarían los criterios si la misma banca fuera para un gimnasio cerrado en vez de un patio.",
)

# ============================================================ OAC-05, clase 3
F = ("Ficha 22 (obra y argumento modelo de ejemplo, inventados). «Escuela Abierta» (obra ficticia, época C de ejemplo): patio central de 15 m por 15 m rodeado por las salas; corredores cubiertos de 3 m de ancho; muros blancos con ventanas altas; un árbol grande que da sombra a los bancos del patio. "
     "Argumento modelo. Afirmación: «El diseño de Escuela Abierta favorece la convivencia». "
     "Evidencia: «El patio central reúne todas las salas, y los corredores cubiertos permiten cruzar sin mojarse». "
     "Razonamiento: «Por lo tanto, las personas se encuentran con frecuencia y circulan también cuando llueve». "
     "Contraargumento: «Alguien podría decir que el patio puede ser ruidoso para las salas cercanas». "
     "Respuesta: «Las ventanas altas permiten ventilar sin abrir hacia el patio, y los bancos pueden ubicarse lejos de las salas».")
build(
    O5, 3, F,
    use="Aprenderé a estructurar un argumento sobre una obra con afirmación, evidencia, razonamiento, contraargumento y respuesta, y a fortalecer la evidencia.",
    prior=["Sé dar un juicio con criterio y evidencia.", "Sé calcular áreas de cuadrados.", "Sé reconocer un prejuicio."],
    explain=[
        "Un argumento estético tiene partes que se pueden identificar. La afirmación es lo que se sostiene («el diseño favorece la convivencia»). La evidencia son los rasgos observables o los datos que la apoyan. El razonamiento explica por qué la evidencia apoya la afirmación, a menudo con conectores como «por lo tanto» o «porque». El contraargumento es una objeción posible, y la respuesta muestra cómo se atiende esa objeción.",
        "Un buen argumento se apoya en rasgos de la obra, no en la fama, el precio o la opinión de la mayoría. Tampoco generaliza sin datos («a todos les gusta»). Para fortalecer la evidencia se pueden usar conteos, medidas, pruebas de uso o citas de personas usuarias, siempre rotulados con su límite.",
        "Cuando alguien presenta una objeción sólida, lo mejor es reconocer lo que tiene de válido y ajustar la afirmación o la propuesta. Cambiar de postura con buenas razones es parte de pensar con criterio. Las obras de esta clase son inventadas.",
    ],
    vocab=[("afirmación", "idea que se sostiene en el argumento"), ("evidencia", "rasgos o datos que apoyan la afirmación"), ("razonamiento", "explicación de por qué la evidencia apoya la afirmación"), ("contraargumento", "objeción posible a la afirmación"), ("respuesta", "forma de atender una objeción")],
    worked=[
        ("Identificar el razonamiento", "En el argumento modelo, ¿cuál es el razonamiento?", ["El razonamiento explica por qué la evidencia apoya la afirmación.", "«Por lo tanto, las personas se encuentran con frecuencia y circulan también cuando llueve»."], "Las personas se encuentran y circulan también con lluvia"),
        ("Calcular una superficie", "Un corredor cubierto de 3 m de ancho recorre un lado de 15 m del patio. ¿Cuántos m² tiene?", ["El área de un rectángulo es largo por ancho.", "3 × 15 = 45."], "45 m²"),
    ],
    mistakes=[("Fundar un argumento en «a todos les gusta».", "Generaliza sin datos y nadie puede comprobarlo.", "Cita evidencia concreta, como un conteo o un rasgo observable."),
              ("Ignorar una objeción sólida.", "El argumento queda débil y no convence a quien la planteó.", "Reconoce lo válido de la objeción y ajusta la propuesta.")],
    T=[
        ('abc', '¿Cuáles son las partes de un argumento estético completo?', 'Afirmación, evidencia, razonamiento y, si es posible, contraargumento con respuesta', 'Gusto, fama y opinión de la mayoría de quienes ven la obra', 'Título, fecha y firma de quien presenta el argumento ante el curso', 'Esas partes permiten sostener y revisar una idea con razones.'),
        ('abc', '{F} ¿Cuál es la afirmación del argumento modelo?', 'El diseño de Escuela Abierta favorece la convivencia', 'El patio central de la escuela mide 15 m por 15 m de lado', 'El patio puede ser ruidoso para las salas cercanas', 'La afirmación es la idea central que todo lo demás apoya.'),
        ('=', '{F} ¿Cuántos m² tiene el patio central (15 m por 15 m)?', '15*15', 'El área de un cuadrado es lado por lado.', ' m²'),
        ('abc', '{F} ¿Cuál es la evidencia del argumento modelo?', 'El patio reúne todas las salas y los corredores cubiertos permiten cruzar sin mojarse', 'Las personas se encuentran con frecuencia y circulan también cuando llueve', 'El patio puede ser ruidoso para las salas que están cerca de él', 'La evidencia son los rasgos de la obra que apoyan la afirmación.'),
        ('abc', '{F} ¿Qué función cumple el razonamiento?', 'Explica por qué la evidencia apoya la afirmación', 'Repite la afirmación con otras palabras para que quede clara', 'Agrega una opinión nueva sin relación con la evidencia', 'El razonamiento conecta evidencia y afirmación.'),
        ('=', '{F} Los corredores bordean los 4 lados del patio de 15 m. ¿Cuántos metros de largo suma el borde del patio?', '4*15', 'Se multiplica el largo de un lado por los 4 lados.', ' m'),
        ('abc', '{F} ¿Qué es un contraargumento?', 'Una objeción posible a la afirmación, que se considera con seriedad', 'Un insulto o burla hacia quien presenta el argumento', 'Una repetición de la afirmación con otras palabras al final', 'El contraargumento muestra puntos débiles posibles y permite responderlos.'),
        ('abc', '{F} ¿Cuál es una respuesta adecuada a la objeción del ruido?', 'Ubicar los bancos lejos de las salas y usar ventanas altas para ventilar sin abrir hacia el patio', 'Negar que exista ruido, porque nadie lo ha medido ni se ha quejado', 'Cerrar el patio con muros altos y dejarlo solo como paso entre las salas', 'La respuesta propone cambios concretos que atienden la objeción.'),
        ('abc', '{F} ¿Qué falla tiene el argumento «Escuela Abierta es bella porque es famosa»?', 'Apela a la fama y no a rasgos observables de la obra', 'No tiene ninguna falla, porque la fama es un dato verdadero', 'Usa demasiadas medidas y poca descripción de la obra', 'La fama no es un rasgo de la obra.'),
        ('abc', '{F} Un integrante escribe como evidencia: «seguro que a todos les gusta el patio». ¿Qué problema tiene?', 'Generaliza sin datos, porque nadie preguntó a todas las personas', 'Ninguno, porque es una opinión positiva y eso la hace válida', 'Que es demasiado corta para considerarse una evidencia', 'Una generalización sin datos no puede comprobarse.'),
        ('abc', '{F} ¿Qué evidencia nueva fortalecería la afirmación sobre convivencia?', 'Un conteo de cuántos estudiantes usan el patio en cada recreo', 'El color favorito de quien diseñó la escuela y su fama', 'El precio del terreno y el valor de los materiales', 'Un conteo es un dato observable relacionado con la convivencia.'),
        ('abc', '{F} ¿Cuál es el argumento más completo sobre accesibilidad?', 'Afirmación: es accesible. Evidencia: corredores de 3 m sin escalones. Razonamiento: dos personas, una en silla de ruedas, se cruzan. Objeción: puede haber desniveles. Respuesta: se verifica con un recorrido', 'Afirmación: es accesible. Evidencia: a todo el mundo le parece accesible. Razonamiento: por eso lo es. Respuesta: no hay objeciones posibles', 'Afirmación: es accesible porque es una escuela y las escuelas deben serlo. Evidencia: aparece en el plano. Razonamiento: lo exige la norma', 'Incluye las cinco partes del argumento y propone verificar.'),
        ('abc', 'Alguien presenta un contraargumento sólido a tu afirmación. ¿Qué es lo mejor?', 'Reconocer lo válido y ajustar la afirmación o la propuesta', 'Ignorarlo, porque ya tenías claro cuál era tu postura', 'Responder con más fuerza para que nadie insista', 'Ajustar con buenas razones es parte de argumentar bien.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Afirmo que el patio favorece el encuentro, porque reúne todas las salas en 225 m²; por lo tanto circulan por él. Una objeción es el ruido; propongo bancos lejos de las salas». ¿Qué hace bien?', 'Usa afirmación, evidencia con un dato, razonamiento, objeción y respuesta', 'Solo da una opinión', 'Ignora las objeciones', 'El texto contiene las partes de un argumento completo.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un contraargumento?", "Una objeción posible a la afirmación", "Considerarlo fortalece el argumento ante otras personas."),
        ("¿En qué se apoya un buen argumento?", "En rasgos y datos observables de la obra", "No en la fama, el precio ni la mayoría."),
        ("¿Qué se hace ante una objeción sólida?", "Se reconoce lo válido y se ajusta la propuesta", "Cambiar con razones es parte de argumentar."),
    ],
    op=("Obra de ejemplo (inventada): «Biblioteca Móvil», un vehículo-biblioteca de 8 m de largo que visita un barrio ficticio: estantes bajos de 90 cm de altura, rampa al costado, toldo que cubre la entrada, 30 libros por estante y 6 estantes. Elige una afirmación (por ejemplo, «favorece el acceso a la lectura») y escribe un argumento con afirmación, dos evidencias, razonamiento, una objeción y una respuesta.",
        "Afirmación: la biblioteca móvil favorece el acceso a la lectura. Evidencia: tiene rampa y estantes bajos de 90 cm; guarda 180 libros (30 × 6). Razonamiento: así personas de distintas edades y capacidades pueden alcanzar los libros. Objeción: el toldo puede no proteger con viento fuerte. Respuesta: se puede agregar un costado lateral desmontable, a revisar con una persona profesional.",
        ["incluye las cinco partes", "usa evidencia observable o calculable", "responde una objeción con una propuesta"],
        ["hoja con el argumento completo"],
        ["no incluir objeción", "evidencia sin datos", "argumentar por fama"],
        "Pregunta: «¿qué rasgo apoya tu afirmación?». Si no hay rasgo, pídele que lo agregue."),
    reinforce="Escribe un argumento de tres líneas sobre un lugar de tu barrio: afirmación, evidencia y razonamiento.",
    extend="Explica por qué considerar un contraargumento puede hacer más fuerte una propuesta.",
)

# ============================================================ OAC-05, clase 4
F = ("Ficha 23 (obra e interpretaciones de ejemplo, inventadas). «Taller del Cerro», centro de artesanía de un cerro ficticio, época C (de ejemplo): edificio alargado de 30 m por 6 m; techo de una sola agua que baja 60 cm a lo ancho hacia el valle; muros de ladrillo reciclado sin ventanas en el lado del cerro; en el lado del valle, una pared completa de ventanas; un banco de trabajo corrido de 24 m; piso de madera recuperada; entrada por una rampa suave, sin escalones. "
     "Interpretación de Ana: «Me recuerda un puente porque es largo y mira al valle; me transmite calma». "
     "Interpretación de Beto: «Me parece cerrado hacia el cerro y muy abierto hacia el valle: es como un refugio desde donde se observa».")
build(
    O5, 4, F,
    use="Aprenderé a formular una interpretación personal apoyada en rasgos de la obra, a compartirla con respeto y a integrarla en un juicio estético propio.",
    prior=["Sé argumentar con evidencia.", "Sé que una obra puede leerse de varias maneras.", "Sé calcular áreas y diferencias de medidas."],
    explain=[
        "Una interpretación personal es lo que una obra sugiere a una persona: una sensación, una imagen, una idea. Puede nacer de la experiencia de cada quien, pero es válida como parte del análisis cuando se apoya en rasgos que cualquiera puede señalar en la obra. Una buena formulación usa «a mí me transmite…» y «porque…» seguido de un rasgo observable.",
        "Una obra admite varias lecturas. Ana ve un puente que mira al valle; Beto ve un refugio cerrado al cerro: ambas pueden ser válidas porque cada una se apoya en rasgos distintos. Eso no significa que cualquier cosa vale: una interpretación sin apoyo en la obra no se puede discutir. Los hechos de la obra, como sus medidas y materiales, no cambian según la persona.",
        "Al compartir interpretaciones en clase, nadie está obligado a contar experiencias íntimas o dolorosas: se puede usar un ejemplo neutral. Si aparecen nuevas razones, se puede ampliar o cambiar la interpretación. Un juicio estético propio integra la interpretación con un criterio y evidencia. La obra de esta clase es inventada.",
    ],
    vocab=[("interpretación personal", "lo que una obra sugiere a una persona, apoyado en rasgos"), ("lectura", "manera de entender una obra"), ("rasgo observable", "característica que cualquiera puede señalar en la obra"), ("integrar", "combinar interpretación, criterio y evidencia en un juicio"), ("ejemplo neutral", "ejemplo que no expone la vida privada de nadie")],
    worked=[
        ("Calcular un perímetro", "¿Cuántos metros mide el contorno (perímetro) de la planta del Taller, de 30 m por 6 m?", ["El perímetro suma los cuatro lados: 30 + 6 + 30 + 6.", "2 × (30 + 6) = 72."], "72 m"),
        ("Apoyar una interpretación", "Ana ve «un puente que mira al valle». ¿Qué rasgos de la ficha la apoyan?", ["El edificio es alargado, de 30 m por 6 m.", "Una pared completa de ventanas mira al valle."], "La planta alargada y la pared de ventanas hacia el valle"),
    ],
    mistakes=[("Decir «mi interpretación no se discute porque es personal».", "Si no se apoya en rasgos de la obra, nadie puede entenderla ni dialogar.", "Comparte tu interpretación con un rasgo observable que la respalde."),
              ("Obligarse a contar una experiencia íntima para justificar una interpretación.", "No es necesario exponer la vida privada para analizar una obra.", "Usa un ejemplo neutral o solo los rasgos de la obra.")],
    T=[
        ('abc', '¿Qué es una interpretación personal de una obra?', 'Lo que la obra sugiere a una persona, apoyado en rasgos que se pueden señalar', 'Un dato medido de la obra que no cambia según quien la mire', 'La opinión correcta sobre la obra, que todas las personas deben compartir', 'Es una lectura personal con apoyo en lo observable.'),
        ('=', '{F} ¿Cuántos m² tiene la planta (30 m por 6 m)?', '30*6', 'El área de un rectángulo es largo por ancho.', ' m²'),
        ('=', '{F} El banco de trabajo mide 24 m y el edificio 30 m de largo. ¿Cuántos metros de largo quedan sin banco?', '30-24', 'Se resta el largo del banco al largo del edificio.', ' m'),
        ('abc', '{F} ¿Qué rasgos apoyan la interpretación de Ana («un puente que mira al valle»)?', 'La planta alargada y la pared completa de ventanas hacia el valle', 'El piso de madera recuperada y el banco de trabajo corrido', 'La rampa de entrada sin escalones y los muros de ladrillo reciclado', 'La forma alargada y la orientación al valle sostienen la imagen del puente.'),
        ('abc', '{F} ¿Qué rasgos apoyan la interpretación de Beto («cerrado hacia el cerro y abierto hacia el valle»)?', 'Muros sin ventanas en el lado del cerro y una pared completa de ventanas hacia el valle', 'El banco de trabajo corrido de 24 m y el piso de madera recuperada', 'La rampa suave de entrada y el techo de una sola agua', 'Los dos lados opuestos contrastan en apertura.'),
        ('abc', '{F} ¿Pueden ser válidas a la vez las interpretaciones de Ana y Beto?', 'Sí, si cada una se apoya en rasgos de la obra, porque una obra admite varias lecturas', 'No, solo una puede ser correcta y la otra debe corregirse', 'No, porque Ana habla de calma y Beto de refugio, y esas ideas se contradicen', 'Ambas se apoyan en rasgos distintos y no se contradicen.'),
        ('abc', '{F} ¿Cuál es una interpretación personal bien formulada?', 'A mí me transmite recogimiento porque los muros sin ventanas hacia el cerro dan sensación de refugio', 'Es horrible y punto, porque mi sensación no necesita explicación', 'Todos sienten recogimiento al verla, porque los muros cerrados dan esa sensación', 'Usa «a mí» y apoya la sensación en un rasgo observable.'),
        ('abc', 'Al compartir interpretaciones en clase, ¿qué se evita?', 'Obligar a contar experiencias íntimas o dolorosas: se puede usar un ejemplo neutral', 'Mencionar rasgos de la obra para apoyar lo que se siente', 'Decir «a mí me transmite», porque eso expone demasiado a la persona', 'Nadie debe exponer su vida privada para participar.'),
        ('=', '{F} El techo baja 60 cm a lo ancho del edificio, que mide 6 m. ¿Cuántos centímetros baja por cada metro?', '60//6', 'Se divide la bajada total entre los metros de ancho.', ' cm'),
        ('abc', '{F} Beto escucha que la rampa suave y el banco corrido hacen al taller muy inclusivo, y amplía su idea. ¿Qué hizo?', 'Amplió su interpretación con evidencia nueva', 'Abandonó su interpretación porque otra persona la contradijo', 'Descartó la evidencia nueva para no cambiar su lectura', 'Actualizar una interpretación con nuevas razones es parte del análisis.'),
        ('abc', 'Alguien dice: «mi interpretación no puede discutirse porque es personal». ¿Qué respuesta es mejor?', 'Es personal, pero se puede compartir con razones: si se apoya en rasgos observables, otras personas pueden entenderla', 'Tiene razón: lo personal nunca se discute, porque cada persona siente distinto', 'Debe cambiarla por la de la mayoría, porque entre más personas opinen igual, más cierta es', 'Compartirla con razones permite el diálogo sin imponer una lectura.'),
        ('abc', '{F} ¿Qué juicio integra interpretación, criterio y evidencia?', 'Para mí es un refugio que mira al valle: los muros cerrados protegen y la pared de ventanas invita a trabajar viendo el paisaje; lo valoro como espacio de concentración', 'Me parece un espacio lindo y creo que funciona bien para trabajar con otras personas, aunque no sé explicar por qué', 'Es un taller como cualquier otro: tiene 30 m de largo, un banco corrido y una rampa de entrada', 'Une una lectura personal con criterio y rasgos de la ficha.'),
        ('abc', '¿Qué límite tiene una interpretación personal?', 'No puede contradecir los hechos de la obra, como sus medidas y materiales', 'Debe ser igual a la de las demás personas que miran la obra', 'No puede mencionar ningún rasgo de la obra, solo sensaciones personales', 'Los hechos de la obra no cambian según la persona.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «A mí el Taller me transmite concentración porque el banco corrido de 24 m y la pared de ventanas hacia el valle ordenan el trabajo en una sola línea. Entiendo que a Ana le recuerde un puente». ¿Qué hace bien?', 'Formula su interpretación con un rasgo observable y respeta otra lectura', 'Descarta la lectura de Ana', 'No usa ningún rasgo de la obra', 'La interpretación se apoya en rasgos y reconoce otra lectura.'),
    sc=[
        ("En Diseño y arquitectura: ¿cómo se formula una interpretación personal?", "Con «a mí me transmite… porque…» y un rasgo observable", "Así otras personas pueden entender y discutir la idea."),
        ("¿Por qué pueden coexistir dos interpretaciones?", "Porque una obra admite varias lecturas apoyadas en rasgos distintos", "Ninguna contradice los hechos de la obra."),
        ("¿Hay que contar experiencias íntimas para interpretar?", "No: se puede usar un ejemplo neutral", "La privacidad de cada persona se respeta siempre."),
    ],
    op=("Obra de ejemplo (inventada): «Sala del Eco», una sala de música de 12 m por 8 m en un liceo ficticio, época C (de ejemplo): techo curvo de madera, muros con paneles de fieltro gris, una sola ventana alta al norte, escenario circular de 4 m de diámetro y acceso por una rampa suave. Escribe una interpretación personal usando «a mí me transmite… porque…» con un rasgo, un juicio estético propio con un criterio y una evidencia, y una frase que reconozca otra lectura posible.",
        "Interpretación: a mí me transmite recogimiento porque el techo curvo de madera y los paneles de fieltro parecen envolver la sala. Juicio: es una buena sala de música porque los paneles de fieltro ayudan a escuchar con claridad (criterio: función; evidencia: paneles) y la rampa permite entrar a todas las personas. Otra lectura: alguien podría verla como un auditorio solemne por el escenario circular.",
        ["usa «a mí me transmite… porque…» con un rasgo", "integra criterio y evidencia en el juicio", "reconoce otra lectura posible"],
        ["texto de cuatro a seis líneas"],
        ["no apoyar la interpretación en un rasgo", "descalificar otras lecturas", "contar experiencias íntimas innecesarias"],
        "Pregunta: «¿qué rasgo de la obra respalda lo que sientes?». Si no hay rasgo, pídele que lo busque."),
    reinforce="Mira un lugar de tu barrio y escribe una frase «a mí me transmite… porque…» con un rasgo observable.",
    extend="Explica cómo una misma obra puede transmitir sensaciones distintas sin que ninguna lectura sea falsa.",
)

# ============================================================ OAC-05, clase 5
F = ("Ficha 24 (juicios de ejemplo para revisar, inventados). Obra de ejemplo: «Biblioteca Gris», edificio de hormigón de 3 pisos de 4 m de altura cada uno, con grandes ventanas al norte y un jardín de plantas nativas en el techo, época C (de ejemplo). "
     "Juicio J1: «Es bella porque la diseñó un arquitecto famoso». "
     "Juicio J2: «Es fea porque todo el mundo dice que el hormigón es feo». "
     "Juicio J3: «Es valiosa porque su techo con jardín de plantas nativas aporta sombra y refugio a insectos, y las ventanas grandes dan luz natural a la sala de lectura». "
     "Juicio J4: «Es bella porque es muy cara». "
     "Pauta: un juicio sólido cita rasgos observables, nombra el criterio y no se apoya en la fama, el precio ni la opinión de la mayoría. Cada característica cumplida vale 2 puntos y hay 3 características.")
build(
    O5, 5, F,
    use="Aprenderé a revisar juicios estéticos propios y ajenos con una pauta, a reconocer falacias simples (apelar a la fama, al precio o a la mayoría) y a reformularlos con evidencia.",
    prior=["Sé argumentar con partes.", "Sé distinguir rasgos de opiniones.", "Sé dar retroalimentación respetuosa."],
    explain=[
        "Revisar un juicio estético es comprobar si se sostiene. Una pauta simple pregunta: ¿cita rasgos observables?, ¿nombra el criterio con que valora?, ¿evita apoyarse en la fama, el precio o la opinión de la mayoría? Un juicio que cumple las tres características es sólido; si falla alguna, se puede reformular.",
        "Las falacias simples más frecuentes son apelar a la fama («es bella porque la hizo alguien famoso»), apelar al precio («es bella porque es cara»), apelar a la mayoría («es fea porque todos dicen que lo es») y generalizar sin datos. Ninguna dice nada sobre la obra misma: la fama, el precio y la mayoría no son rasgos observables. Reformular consiste en reemplazarlas por rasgos y criterios.",
        "La revisión es respetuosa: se critica el juicio, no a la persona, y se ofrece una mejora. También se aplica a los propios juicios. Cambiar un juicio después de ver nueva evidencia muestra pensamiento crítico y no debilidad. Las obras y juicios de esta clase son inventados.",
    ],
    vocab=[("juicio sólido", "juicio con rasgos, criterio y sin apoyarse en fama, precio ni mayoría"), ("falacia", "razonamiento que parece válido, pero no lo es"), ("apelar a la fama", "justificar algo por quién lo hizo, no por la obra"), ("reformular", "reescribir un juicio con rasgos y criterios"), ("pauta", "lista de preguntas para revisar un juicio")],
    worked=[
        ("Aplicar la pauta", "¿Cuántos puntos obtiene J3, que cumple las tres características de 2 puntos cada una?", ["Se multiplican las características cumplidas por 2.", "3 × 2 = 6."], "6 puntos"),
        ("Calcular una altura", "Si se agregara un cuarto piso de 4 m, ¿cuántos metros de alto tendría la Biblioteca?", ["Pasaría de 3 a 4 pisos de 4 m.", "4 × 4 = 16."], "16 m"),
    ],
    mistakes=[("Reformular «es fea porque todos lo dicen» como «es fea porque la mayoría tiene razón».", "Sigue apoyándose en la mayoría y no en la obra.", "Reemplázalo por un rasgo observable y un criterio."),
              ("Revisar un juicio diciendo «tú no sabes de esto».", "Descalifica a la persona y no ayuda a mejorar el juicio.", "Señala qué falla con una cita y propone una versión mejorada.")],
    T=[
        ('abc', '¿Cuándo un juicio estético es sólido?', 'Cuando cita rasgos observables y nombra el criterio con que valora', 'Cuando lo dice una persona famosa o con mucha experiencia en arquitectura', 'Cuando coincide con lo que opina la mayoría de quienes ven la obra', 'La solidez depende de rasgos y criterios, no de quién lo dice ni de cuántos lo repiten.'),
        ('abc', '{F} ¿Qué falla tiene J1?', 'Se apoya en la fama de quien diseñó y no en rasgos de la obra', 'Cita demasiados rasgos de la obra y poco de la persona', 'No tiene ninguna falla, porque la fama da prestigio a una obra', 'La fama de una persona no es un rasgo de la obra.'),
        ('abc', '{F} ¿Qué falla tiene J2?', 'Se apoya en la opinión de la mayoría sin mirar la obra', 'Cita rasgos del jardín, pero sin nombrar el criterio', 'Usa un criterio de sustentabilidad sin ninguna evidencia', 'Lo que «todo el mundo dice» no es evidencia sobre esta obra.'),
        ('abc', '{F} ¿Qué falla tiene J4?', 'Confunde el precio con la belleza o el valor', 'Cita las ventanas grandes al norte como rasgo observable', 'Compara la biblioteca con otra obra más famosa de la ciudad', 'El precio no es un rasgo estético observable.'),
        ('abc', '{F} ¿Por qué J3 es un juicio sólido?', 'Cita rasgos (jardín en el techo y ventanas grandes) y criterios (sustentabilidad y luz natural)', 'Porque coincide con la opinión de quienes más conocen de arquitectura', 'Porque usa un tono entusiasta y no hace ninguna crítica a la obra', 'Cumple las tres características de la pauta.'),
        ('=', '{F} ¿Cuántos metros de alto tiene la Biblioteca (3 pisos de 4 m)?', '3*4', 'Se multiplican los pisos por la altura de cada uno.', ' m'),
        ('abc', '{F} ¿Cómo se mejora J1 sin perder su sentido?', 'Me parece bella porque las ventanas grandes al norte llenan de luz natural la sala y el techo con jardín da un remate verde', 'Es bella porque es de un arquitecto famoso, y por eso su obra merece ser valorada', 'Es bella, y cualquiera que la vea estará de acuerdo con eso', 'La nueva versión reemplaza la fama por rasgos y criterios.'),
        ('abc', '¿Cómo se llama la falla de usar «todo el mundo lo dice» como prueba?', 'Apelar a la mayoría', 'Apelar a la fama', 'Apelar al precio', 'Se trata de apoyarse en cuántos lo creen y no en la obra.'),
        ('abc', '{F} ¿Qué pregunta sirve para revisar cualquier juicio?', '¿Qué rasgo de la obra y qué criterio lo sostienen?', '¿Quién fue la primera persona en decirlo y cuántas lo repiten?', '¿Cuánto costó construir la obra y quién la diseñó?', 'Esa pregunta lleva el juicio a rasgos y criterios comprobables.'),
        ('=', '{F} J3 cumple las 3 características de la pauta y J2 cumple solo 1. ¿Cuántos puntos de diferencia hay, si cada característica vale 2 puntos?', '(3-1)*2', 'Se calcula la diferencia de características y se multiplica por 2.', ' puntos'),
        ('abc', '{F} Alguien dice: «J2 es válido porque muchas personas lo creen». ¿Qué respuesta es mejor?', 'Que muchas personas lo crean no es evidencia sobre la obra: hay que mostrar rasgos y criterios', 'Tiene razón: si muchas personas lo creen, eso es evidencia suficiente sobre la obra', 'Hay que borrar J2 sin explicar nada, porque es un juicio negativo', 'Lo que cree la mayoría no cambia lo que se puede observar en la obra.'),
        ('abc', '{F} ¿Qué revisión respetuosa de J4 es más útil?', 'J4 relaciona belleza con precio, que no es un rasgo de la obra; podrías citar rasgos como la luz y decir con qué criterio los valoras', 'J4 está mal: nadie puede decir que algo caro es bello; cámbialo', 'J4 está bien tal como está, porque el precio de una obra refleja su valor estético', 'Señala la falla sin juzgar a la persona y propone cómo mejorar.'),
        ('abc', 'Una persona cambia su juicio después de ver nueva evidencia. ¿Qué muestra?', 'Un uso sano del pensamiento crítico: actualizar la opinión con razones', 'Que no tenía convicciones y se dejó llevar por la otra persona', 'Que perdió una discusión y debe aceptar la opinión de quien ganó', 'Cambiar con evidencia es parte de argumentar bien.'),
    ],
    ctx=('abc', 'Una estudiante revisa su propio juicio: «Escribí que la Biblioteca es fea porque es gris. Reviso: el gris es un rasgo, pero no dije el criterio. Reformulo: me parece fría porque el hormigón sin color y sin sombra no invita a quedarse, y espero que una biblioteca sea acogedora». ¿Qué hace bien?', 'Revisa con la pauta y reformula con rasgo y criterio', 'Mantiene el juicio sin cambios', 'Se apoya en que todos piensan lo mismo', 'La autorrevisión añade el criterio que faltaba.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es apelar a la fama?", "Justificar un juicio por quién hizo la obra y no por sus rasgos", "La fama no es un rasgo de la obra."),
        ("¿Qué tres preguntas tiene la pauta de revisión de un juicio?", "Si cita rasgos, si nombra el criterio y si evita fama, precio y mayoría", "Con ellas se decide si el juicio es sólido."),
        ("¿Cómo se critica un juicio ajeno con respeto?", "Señalando qué falla con una cita y proponiendo una mejora", "Se critica el juicio, no a la persona."),
    ],
    op=("Revisa estos juicios de ejemplo sobre una banca llamada «Nube»: J-A: «Es bella porque salió en una revista». J-B: «Es fea porque nadie la quiere». J-C: «Es valiosa porque su respaldo curvo y los tablones reutilizados la hacen cómoda y sustentable». Aplica la pauta de la ficha a cada juicio, di qué característica falla y reformula J-A y J-B con un rasgo y un criterio (inventa los rasgos de la banca y avisa que son de ejemplo).",
        "J-A: falla en rasgos (apela a la fama de una revista). J-B: falla en rasgos y mayoría. J-C cumple las tres características. Reformulación J-A: me parece bella porque su respaldo curvo guía la mirada (rasgo de ejemplo), según el criterio de armonía. Reformulación J-B: me parece poco cómoda porque el asiento es muy alto para sentarse con los pies apoyados (rasgo de ejemplo), según el criterio de comodidad.",
        ["aplica la pauta a cada juicio", "reconoce la falla de cada uno", "reformula con rasgo y criterio rotulados como ejemplo"],
        ["hoja con la revisión y dos reformulaciones"],
        ["criticar a la persona", "reformular sin rasgos", "no rotular los rasgos inventados"],
        "Pregunta: «¿qué rasgo y qué criterio sostienen esta versión?». Si falta alguno, pídele agregarlo."),
    reinforce="Escucha un juicio sobre un objeto (de una conversación o de un video) y anota si cita rasgos, nombra un criterio o se apoya en la fama, el precio o la mayoría.",
    extend="Explica por qué revisar los propios juicios es tan importante como revisar los ajenos.",
)

# ============================================================ OAC-06, clase 1
F = ("Ficha 25 (proyecto de ejemplo, inventado). Proyecto de un equipo ficticio: «Quiosco de Lectura» para el patio. "
     "Propósito comunicativo: invitar a leer en un lugar tranquilo. Propósito funcional: asientos para 12 personas, techo contra el sol y la lluvia y acceso sin escalones. "
     "Presupuesto máximo: 360.000 pesos; gasto real: 340.000 pesos. "
     "Resultado: 12 asientos; techo de plástico reciclado; acceso por una rampa de 1 cm de subida por cada 12 cm de largo (regla de ejemplo, la real la fija la norma vigente); colores cálidos en tonos tierra; dos cubos de madera que sirven de mesa; sin enchufes ni luz propia. "
     "Decisiones registradas: D1 elegir plástico reciclado por menor costo por año; D2 poner la entrada hacia el este, lejos del ruido de la cancha; D3 renunciar a la luz propia por presupuesto.")
build(
    O6, 1, F,
    use="Aprenderé a evaluar críticamente un proyecto relacionando su propósito comunicativo, sus aspectos estéticos y funcionales y las decisiones tomadas en el proceso.",
    prior=["Sé revisar un proyecto contra necesidades.", "Sé argumentar con evidencia.", "Sé calcular diferencias y porcentajes sencillos."],
    explain=[
        "Evaluar críticamente un proyecto es juzgar con criterios y evidencia si el proceso y el resultado cumplieron su propósito. No es poner una nota ni elogiar o criticar por gusto: es entender qué se quiso lograr, qué se logró, qué no se logró y por qué. Un proyecto tiene un propósito comunicativo o expresivo (qué quiere transmitir, por ejemplo calma o invitación) y un propósito funcional (para qué sirve y a quiénes).",
        "Los aspectos estéticos y los funcionales se relacionan con el propósito. Los colores cálidos de un quiosco pueden apoyar el propósito de invitar; una rampa apoya el propósito funcional de acceso. Cada decisión del proceso, como elegir un material o ubicar una entrada, tiene una razón y una consecuencia. Por eso se registran las decisiones: permiten entender por qué el resultado es como es y aprender de ellas.",
        "Una evaluación completa nombra los logros con evidencia, los límites o renuncias (por ejemplo, la falta de luz propia), las decisiones con sus razones y qué se haría distinto. No basta con decir que se cumplió el presupuesto: un proyecto puede cumplir una restricción y fallar en otra. El proyecto de esta clase es inventado.",
    ],
    vocab=[("evaluación crítica", "juicio con criterios y evidencia sobre proceso y resultado"), ("propósito comunicativo", "idea o sensación que el proyecto quiere transmitir"), ("propósito funcional", "uso para el que el proyecto fue pensado"), ("decisión", "elección tomada en el proceso, con una razón y una consecuencia"), ("renuncia", "algo que se deja de lado por una restricción")],
    worked=[
        ("Relacionar propósito y rasgo", "¿Qué rasgo estético apoya el propósito de invitar a leer?", ["El propósito pide un lugar acogedor.", "Los colores cálidos en tonos tierra sugieren acogida."], "Los colores cálidos en tonos tierra"),
        ("Medir el ahorro", "¿Cuántos pesos se ahorraron respecto del presupuesto máximo?", ["Presupuesto máximo 360.000 y gasto real 340.000.", "360.000 − 340.000 = 20.000."], "20.000 pesos"),
    ],
    mistakes=[("Evaluar solo el cumplimiento del presupuesto.", "Un proyecto puede cumplir el costo y fallar en su propósito comunicativo o funcional.", "Evalúa propósito, estética, función, decisiones y renuncias."),
              ("Olvidar registrar por qué se tomó una decisión.", "No se puede aprender de decisiones cuya razón se perdió.", "Anota cada decisión con su razón y su consecuencia.")],
    T=[
        ('abc', '¿Qué significa evaluar críticamente un proyecto?', 'Juzgar con criterios y evidencia si el proceso y el resultado cumplieron el propósito', 'Ponerle una nota general al proyecto sin explicar los criterios', 'Elogiar todo lo que se hizo para que el equipo se sienta motivado', 'La evaluación crítica usa criterios y evidencia para entender lo logrado y lo no logrado.'),
        ('abc', '{F} ¿Cuál es el propósito comunicativo del quiosco?', 'Invitar a leer en un lugar tranquilo', 'Tener asientos para 12 personas en el patio', 'Usar plástico reciclado en el techo', 'El propósito comunicativo es lo que el proyecto quiere transmitir.'),
        ('=', '{F} ¿Cuántos centímetros de largo necesita la rampa para subir 30 cm (1 cm de subida por cada 12 cm de largo)?', '30*12', 'Se multiplica la altura por 12 según la regla de ejemplo.', ' cm'),
        ('abc', '{F} ¿Qué rasgo del quiosco responde al propósito funcional de proteger del sol y la lluvia?', 'El techo de plástico reciclado', 'Los colores cálidos en tonos tierra', 'Los dos cubos de madera que sirven de mesa', 'La ficha pide un techo contra el sol y la lluvia, y el resultado lo cumple con el techo de plástico reciclado.'),
        ('abc', '{F} ¿Qué decisión se relaciona con el propósito de «lugar tranquilo»?', 'D2: poner la entrada hacia el este, lejos del ruido de la cancha', 'D1: elegir plástico reciclado por su menor costo por año', 'D3: renunciar a la luz propia por falta de presupuesto', 'La ubicación de la entrada reduce el ruido, apoyando la tranquilidad.'),
        ('abc', '{F} ¿Cuál es un logro funcional del proyecto?', 'El acceso sin escalones por rampa', 'No tener enchufes para cargar equipos', 'No tener luz propia para usarlo de noche', 'La rampa permite acceder a más personas, y los otros dos son límites.'),
        ('abc', '{F} ¿Qué consecuencia tuvo D3 (renunciar a la luz propia)?', 'El quiosco no se puede usar cómodamente de noche; fue una renuncia por presupuesto', 'El quiosco quedó más cálido y cómodo para leer en las tardes', 'No tuvo ninguna consecuencia, porque la luz no era parte del propósito', 'Toda decisión tiene consecuencias, y aquí se limitó el horario de uso.'),
        ('=', '{F} Si el gasto real hubiera sido 355.000 pesos, ¿cuántos pesos se habrían ahorrado respecto del presupuesto máximo?', '360000-355000', 'Se resta el gasto real hipotético al presupuesto máximo.', ' pesos'),
        ('abc', '{F} ¿Qué prueba permite evaluar si «el acceso funciona»?', 'Un recorrido con una persona que usa silla de ruedas para comprobar que sube sola por la rampa', 'Contar cuántos colores tiene el quiosco y qué tonos predominan', 'Revisar el precio del plástico de la rampa y compararlo con otros materiales', 'La evidencia debe poder probar la función del acceso.'),
        ('abc', '{F} Un integrante dice: «el proyecto es perfecto porque cumplió el presupuesto». ¿Qué respuesta es mejor?', 'Cumplir el presupuesto es un logro, pero también hay que evaluar si invita a leer, si es accesible y qué se renunció', 'Tiene razón: si se cumple el presupuesto, el proyecto cumplió también su propósito', 'Hay que borrar el presupuesto de la evaluación, porque no tiene que ver con el propósito', 'La evaluación crítica mira propósito, función, decisiones y renuncias, no un solo criterio.'),
        ('abc', '{F} ¿Cuál es la mejor evidencia para evaluar el propósito comunicativo?', 'Observar y preguntar a visitantes si se sienten invitados a leer allí', 'Contar los colores y tonos tierra del quiosco', 'Comparar el precio del plástico con el de otros materiales', 'El propósito comunicativo se evalúa mirando cómo lo recibe el público.'),
        ('abc', '{F} ¿Cuál es una evaluación completa del proyecto?', 'Logros (12 asientos, rampa, colores cálidos), límites (sin luz ni enchufes), decisiones D1 a D3 con razones y qué se haría distinto', 'El proyecto es bueno porque cumplió el presupuesto y tiene 12 asientos', 'Se hizo todo bien y no hay nada que cambiar en una próxima versión', 'Incluye logros, límites, decisiones y mejoras.'),
        ('abc', '¿Por qué se registran las decisiones del proceso?', 'Porque permiten entender por qué el resultado es así y aprender de ellas', 'Porque lo exige el presupuesto máximo del proyecto', 'Para que la bitácora se vea más larga y completa ante la persona que evalúa', 'Una decisión sin registro pierde su razón y su aprendizaje.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Propósito: invitar a leer. Logro: colores cálidos y entrada lejos del ruido (D2). Límite: sin luz propia (D3). Evidencia: tres visitantes dijeron que les dieron ganas de leer». ¿Qué hace bien?', 'Relaciona propósito, rasgos, decisiones y evidencia, e incluye un límite', 'Solo dice que quedó bonito', 'Ignora las decisiones del proceso', 'La evaluación usa propósito, evidencia, decisiones y límites.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué dos propósitos tiene un proyecto?", "Uno comunicativo o expresivo y uno funcional", "Ambos propósitos se evalúan con evidencia observable."),
        ("¿Qué es una renuncia en un proyecto?", "Algo que se deja de lado por una restricción", "Debe registrarse con su razón y su consecuencia."),
        ("¿Para qué sirve registrar las decisiones?", "Para entender por qué el resultado es así y aprender", "Sin registro se pierde la razón de cada decisión."),
    ],
    op=("Proyecto de ejemplo (inventado): «Paradero Esperanza», un paradero con techo de 5 m, una banca de 4 m con extremo libre para silla de ruedas, panel de horarios con letra de 2 cm leída a 4 m, colores azul y blanco, y sin protección lateral contra el viento. Propósito comunicativo: dar sensación de orden y seguridad. Decisiones: D1 techo largo, D2 banca con extremo libre, D3 renunciar a la protección lateral por costo. Escribe dos logros con evidencia, un límite, la consecuencia de D3 y qué harías distinto.",
        "Logros: banca con extremo libre (apoya el acceso) y panel legible a 4 m (letra de 2 cm). Límite: sin protección lateral, el viento y la lluvia entran. Consecuencia de D3: menor comodidad con mal tiempo. Qué haría distinto: probar una protección lateral liviana con un costo menor.",
        ["relaciona propósito y rasgos", "cita evidencia", "nombra un límite y una consecuencia"],
        ["hoja con logros, límite, consecuencia y mejora"],
        ["evaluar solo el costo", "no nombrar límites", "no relacionar con el propósito"],
        "Pregunta: «¿qué dato muestra ese logro?». Si no hay dato, pídele que lo agregue."),
    reinforce="Elige un objeto de tu casa y anota para qué fue hecho, un logro y un límite.",
    extend="Explica por qué cumplir una restricción no basta para decir que un proyecto es bueno.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 26 (bitácora de ejemplo, inventada, de un equipo que diseñó una estantería para la sala de estudio). "
     "Entrada 1 (semana 1): se observaron 20 estudiantes; 14 dejan sus mochilas en el suelo. "
     "Entrada 2 (semana 2): boceto de tres estanterías; se elige la de 4 niveles. "
     "Entrada 3: maqueta de cartón a escala 1:10 de la estantería de 160 cm de alto; no tiene fecha ni nombre de quien la escribió. "
     "Entrada 4 (semana 4): prueba de uso con 6 estudiantes; 5 alcanzaron el estante superior sin ayuda y 1, usuaria de silla de ruedas, no lo alcanzó; se decide bajar la altura máxima de uso a 120 cm. "
     "Entrada 5 (semana 5): versión 2 con 3 niveles separados por 40 cm; costo 54.000 pesos por estantería.")
build(
    O6, 2, F,
    use="Aprenderé a reunir y evaluar evidencias del proceso (bitácora, versiones, pruebas, comentarios) y a distinguir una evidencia sólida de una débil.",
    prior=["Sé registrar decisiones.", "Sé calcular escalas y porcentajes sencillos.", "Sé que no se inventa evidencia."],
    explain=[
        "Evaluar un proceso exige evidencias del proceso, no solo del resultado final. La bitácora es un registro con fecha y autoría de lo que se observó, probó y decidió. Otras evidencias son los bocetos, las maquetas y los prototipos, los datos de pruebas de uso, los comentarios recibidos, las versiones sucesivas y las fuentes consultadas. Juntas muestran cómo y por qué cambió el proyecto.",
        "No todas las evidencias valen lo mismo. Una evidencia sólida está fechada, tiene autoría, es específica (con datos medibles), puede verificarse y se relaciona con una decisión. «Quedó linda» es débil; «5 de 6 estudiantes alcanzaron el estante superior» es sólida. Los datos de una muestra pequeña se citan con su límite.",
        "La honestidad es parte de la evidencia: no se inventan pruebas ni se corrigen entradas después para que se vea mejor. Si falta una prueba, se anota como pendiente. Si las fotografías muestran a otras personas, se pide su permiso. La bitácora de esta clase es inventada.",
    ],
    vocab=[("bitácora", "registro fechado y atribuido del proceso"), ("evidencia sólida", "dato fechado, específico y verificable ligado a una decisión"), ("versión", "estado del proyecto tras una serie de cambios"), ("prueba de uso", "ensayo con personas reales que usan el objeto"), ("pendiente", "prueba o dato que falta y se anota como tal")],
    worked=[
        ("Calcular un porcentaje", "En la entrada 1, ¿qué porcentaje de las 20 personas observadas deja su mochila en el suelo (14)?", ["Se divide 14 entre 20 y se multiplica por 100.", "14 × 100 ÷ 20 = 70."], "70 %"),
        ("Evidencia de una necesidad", "¿Qué evidencia muestra la necesidad que originó el proyecto de la estantería?", ["La entrada 1 cuenta cuántos estudiantes dejan la mochila en el suelo.", "Es un dato específico y de la semana 1."], "La observación de la semana 1: 14 de 20 dejan la mochila en el suelo"),
    ],
    mistakes=[("Agregar a la bitácora una prueba que no se hizo para que se vea completa.", "Inventar evidencia quita credibilidad a todo el proyecto.", "Registra solo lo que se hizo y anota lo que falta como pendiente."),
              ("Escribir entradas sin fecha ni nombre.", "No se puede verificar cuándo ni quién hizo cada cosa.", "Agrega fecha y autoría a cada entrada.")],
    T=[
        ('abc', '¿Qué es una bitácora de proyecto?', 'Un registro fechado y atribuido de lo que se observó, probó y decidió', 'Un listado de materiales y costos sin fechas ni autoría', 'Un álbum de fotografías del proyecto sin explicación ni fecha', 'La bitácora conserva el proceso con fecha y autoría.'),
        ('=', '{F} De las 20 personas observadas, 14 dejan su mochila en el suelo. ¿Cuántas personas no la dejan en el suelo?', '20-14', 'Se resta al total de personas observadas las que dejan la mochila en el suelo.', ' personas'),
        ('=', '{F} ¿Cuántos centímetros mide en la maqueta 1:10 la estantería de 160 cm de alto?', '160//10', 'Se divide la medida real por 10.', ' cm'),
        ('abc', '{F} ¿Qué evidencia respalda la decisión de bajar la altura máxima de uso?', 'La prueba de uso: una usuaria de silla de ruedas no alcanzó el estante superior', 'La opinión del equipo de que la estantería se verá mejor más baja', 'El precio de la estantería, que es de 54.000 pesos', 'La prueba de uso es un dato específico y relacionado con la decisión.'),
        ('=', '{F} ¿Cuántos centímetros de altura alcanzan los 3 niveles separados por 40 cm?', '3*40', 'Se multiplica el número de niveles por la separación.', ' cm'),
        ('abc', '{F} ¿Qué entrada muestra una decisión?', 'La entrada 2: se elige la estantería de 4 niveles', 'La entrada 1: se observaron 20 estudiantes en la sala', 'Ninguna entrada muestra decisiones, solo observaciones y datos', 'Elegir una opción entre tres bocetos es una decisión.'),
        ('abc', '{F} ¿Qué le falta a la entrada 3?', 'La fecha y el nombre de quien la escribió', 'Más color y detalles en la maqueta de cartón', 'Un precio más alto para la estantería a escala', 'Sin fecha y autoría no se puede verificar la entrada.'),
        ('abc', '{F} ¿Qué cambió entre la versión 1 (4 niveles) y la versión 2 (3 niveles) y por qué?', 'Se redujeron los niveles porque la prueba mostró que una usuaria no alcanzaba el nivel superior', 'Se cambió el color de la estantería porque a una parte del grupo no le gustaba', 'Se aumentó la altura de la estantería porque en la sala sobraba espacio', 'La razón del cambio está en la prueba de uso de la entrada 4.'),
        ('abc', '{F} Un integrante propone agregar a la bitácora una prueba que no se hizo para que se vea completa. ¿Qué corresponde?', 'No inventar evidencia: registrar solo lo hecho y anotar la prueba como pendiente', 'Agregarla con fecha reciente, porque la bitácora debe verse completa', 'Cambiar las fechas de otras pruebas para que calcen con la nueva', 'Inventar evidencia quita credibilidad al proyecto.'),
        ('abc', '{F} ¿Qué evidencia es más fuerte para decir que la estantería resuelve la necesidad?', 'Una prueba de uso con varios estudiantes, comparada con el problema inicial (14 de 20 con mochilas en el suelo)', 'Una frase del equipo: «quedó linda y nos gustó mucho»', 'La opinión de una sola persona del equipo, que dice que la usó y le sirvió', 'Una evidencia fuerte es específica, verificable y ligada al problema inicial.'),
        ('=', '{F} ¿Cuántos pesos cuestan 3 estanterías de la versión 2 (54.000 pesos cada una)?', '3*54000', 'Se multiplica el costo por el número de estanterías.', ' pesos'),
        ('abc', '{F} ¿Qué mejora haría más verificable el registro?', 'Agregar fecha, autoría, datos medidos y un dibujo o foto de cada etapa con permiso', 'Escribir más adjetivos que describan lo bien que salió cada etapa', 'Borrar las entradas con errores para que la bitácora quede más ordenada', 'Fechas, autoría y datos permiten comprobar el proceso.'),
        ('abc', 'Algunas fotos de la bitácora muestran a compañeros. ¿Qué corresponde?', 'Pedir su permiso o evitar mostrar sus rostros', 'Publicarlas sin avisar', 'Pasarlas por alto, porque es solo una bitácora', 'La imagen de otras personas se usa con su permiso.'),
    ],
    ctx=('abc', 'Una estudiante anota: «Semana 4, escrito por ella, prueba con 6 estudiantes: 5 alcanzan el estante alto y 1 no. Decisión: bajar la altura a 120 cm. Pendiente: probar con 10 estudiantes». ¿Qué hace bien?', 'Registra fecha, autoría, dato, decisión y una prueba pendiente', 'Solo anota que la estantería quedó bien', 'Inventa una prueba para completar', 'La entrada es fechada, específica y honesta sobre lo que falta.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué hace sólida a una evidencia?", "Que esté fechada, sea específica, verificable y ligada a una decisión", "Así se puede comprobar y usar para decidir."),
        ("¿Qué se hace si falta una prueba?", "Se anota como pendiente y no se inventa", "La honestidad protege la credibilidad del proyecto."),
        ("¿Qué se pide antes de mostrar a compañeros en una foto?", "Su permiso", "Las personas controlan el uso de su imagen."),
    ],
    op=("Un equipo ficticio registró estas entradas sobre un banco para el patio. Semana 1: observaron 25 estudiantes y 15 se sentaban en el suelo. Semana 2: dos bocetos, eligieron el de 3 módulos. Semana 3: maqueta 1:10 de un banco de 180 cm de largo (sin nombre de quien la hizo). Semana 4: prueba de uso con 8 personas; 7 dijeron que estaba cómodo. Calcula el porcentaje de la semana 1, la medida de la maqueta, y escribe dos entradas que mejorarías con fecha, autoría y dato, y una prueba pendiente.",
        "Semana 1: 15 ÷ 25 × 100 = 60 %. Maqueta: 180 ÷ 10 = 18 cm. Mejoras: semana 3, agregar fecha y nombre; semana 4, agregar qué personas y cuántas veces lo probaron. Pendiente: probar con personas de distintas alturas y con una usuaria de silla de ruedas.",
        ["calcula correctamente porcentaje y escala", "propone mejoras verificables a las entradas", "anota una prueba pendiente"],
        ["hoja con cálculos, mejoras y pendiente"],
        ["inventar pruebas", "no agregar fecha ni autoría", "no citar datos"],
        "Pregunta: «¿quién y cuándo hizo esta prueba?». Si no hay respuesta, pídele que lo agregue."),
    reinforce="Anota en una hoja con fecha tres cosas que hiciste hoy para un proyecto (aunque sea tarea), con un dato medible.",
    extend="Explica por qué una prueba que falló es una evidencia valiosa para evaluar el proceso.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 27 (rúbrica y datos de ejemplo, inventados). Rúbrica de 4 criterios con 4 niveles cada uno (1 insuficiente, 2 básico, 3 logrado, 4 destacado); máximo 16 puntos. "
     "R1 propósito y necesidad; R2 estética coherente con el propósito; R3 función y accesibilidad; R4 sustentabilidad y proceso registrado. "
     "Proyecto evaluado: «Mesa Plegable» de un equipo ficticio. "
     "Autoevaluación del equipo: R1 4; R2 3; R3 4; R4 3. "
     "Evaluación de un par: R1 3; R2 3; R3 2; R4 3. "
     "Prueba de uso con 10 plegados: la mesa se plegó bien 8 veces y se trabó 2 veces; de 8 personas que la usaron, 7 la encontraron estable.")
build(
    O6, 3, F,
    use="Aprenderé a evaluar un proyecto con una rúbrica, a comparar autoevaluación y coevaluación, y a combinar puntajes con datos de pruebas de uso.",
    prior=["Sé que una evaluación se apoya en evidencia.", "Sé sumar puntajes y calcular porcentajes.", "Sé recibir comentarios con respeto."],
    explain=[
        "Una rúbrica es una tabla de criterios con niveles descritos. Cada nivel dice qué se observa cuando el criterio está insuficiente, básico, logrado o destacado. Con la rúbrica se puede evaluar de forma más justa y explicar el puntaje con evidencia. Los puntajes de cada criterio se suman para obtener un total, pero el total no reemplaza el detalle: no dice qué criterio falló ni qué hacer.",
        "La autoevaluación es la mirada del equipo que hizo el proyecto; la coevaluación es la mirada de un par. Las dos aportan: el equipo conoce el proceso y quien evalúa desde fuera ve el resultado como lo vería otra persona usuaria. Cuando hay diferencias grandes en un criterio, no se promedia sin pensar: se conversa con la evidencia, como los datos de una prueba de uso, y se acuerda con los descriptores.",
        "Los datos de pruebas, como plegados correctos de 10 o personas que la encontraron estable de 8, complementan la rúbrica. Se expresan en porcentajes o razones y se citan con su límite: pocas pruebas dan un indicio, no una certeza. Los datos de esta clase son inventados.",
    ],
    vocab=[("rúbrica", "tabla de criterios con niveles descritos"), ("descriptor", "texto que explica un nivel de la rúbrica"), ("autoevaluación", "evaluación que hace el propio equipo"), ("coevaluación", "evaluación que hace un par"), ("prueba de uso", "ensayo con personas que usan el objeto")],
    worked=[
        ("Leer un dato de prueba", "¿Qué porcentaje de los 10 plegados se trabó (2)?", ["Se divide 2 entre 10 y se multiplica por 100.", "2 × 100 ÷ 10 = 20."], "20 %"),
        ("Comparar un criterio", "¿Cuántos puntos de diferencia hay entre el equipo (4) y el par (3) en R1?", ["Se resta el puntaje menor al mayor.", "4 − 3 = 1."], "1 punto"),
    ],
    mistakes=[("Quedarse con un solo número final.", "El total no dice qué criterio falló ni qué mejorar.", "Mira los puntajes por criterio y su evidencia."),
              ("Promediar puntajes muy distintos sin conversar.", "Se pierde la razón de la diferencia.", "Vuelve a la evidencia y acuerda según los descriptores.")],
    T=[
        ('abc', '¿Qué es una rúbrica?', 'Una tabla de criterios con niveles descritos para evaluar', 'Una nota final sin detalle de los criterios usados', 'Una lista de materiales con sus precios y plazos', 'La rúbrica define criterios y qué se espera en cada nivel.'),
        ('=', '{F} ¿Cuántos puntos suma la autoevaluación del equipo?', '4+3+4+3', 'Se suman los cuatro puntajes del equipo.', ' puntos'),
        ('=', '{F} ¿Cuántos puntos suma la evaluación del par?', '3+3+2+3', 'Se suman los cuatro puntajes del par.', ' puntos'),
        ('abc', '{F} ¿En qué criterio hay mayor diferencia entre el equipo y el par?', 'En R3, función y accesibilidad: 4 frente a 2', 'En R2, estética coherente con el propósito', 'En R4, sustentabilidad y proceso registrado', 'Las diferencias son R1 = 1, R2 = 0, R3 = 2 y R4 = 0.'),
        ('=', '{F} ¿Qué porcentaje de los 10 plegados salió bien (8)?', '8*100//10', 'Se divide 8 entre 10 y se multiplica por 100.', ' %'),
        ('abc', '{F} ¿Qué se hace ante la diferencia en R3?', 'Conversar con la evidencia: revisar la prueba de uso y la accesibilidad, y acordar con los descriptores', 'Promediar los dos puntajes sin discutir, para dejar el criterio en 3', 'Elegir el puntaje más alto, porque el equipo conoce mejor su proyecto', 'La diferencia se resuelve volviendo a la evidencia y a los descriptores.'),
        ('=', '{F} ¿Cuántos puntos le faltan al puntaje del par para llegar al máximo de 16?', '16-11', 'Se resta el total del par al máximo.', ' puntos'),
        ('abc', '{F} ¿Qué dato de la ficha sostiene el puntaje más bajo de R3 del par?', 'La mesa se trabó 2 de 10 veces al plegarla', 'La mesa es estable para 7 de 8 personas', 'El equipo se autoevaluó con 4 puntos en R3', 'Una falla de plegado afecta la función y apoya el puntaje bajo.'),
        ('abc', '{F} ¿Qué conclusión sobre la estabilidad es correcta?', '7 de 8 personas la encontraron estable: es favorable, pero la muestra es pequeña', 'Está demostrado que es estable para todas las personas que la usen', 'La estabilidad no se puede evaluar con una prueba de uso de pocas personas', 'Un dato favorable con pocas personas es un indicio, no una prueba general.'),
        ('abc', '{F} Un integrante dice: «la autoevaluación vale más porque el equipo conoce el proyecto». ¿Qué respuesta es mejor?', 'Ambas miradas aportan: el equipo conoce el proceso y el par ve el resultado desde fuera; se contrastan con evidencia', 'Tiene razón: la del par no importa, porque no conoce cómo se hizo el proyecto', 'La del par vale siempre más, porque no tiene interés en que el proyecto salga bien', 'Las dos miradas se complementan y se contrastan con evidencia.'),
        ('abc', '{F} ¿Qué acción es adecuada para mejorar R3?', 'Revisar el mecanismo de plegado, repetir la prueba de uso con más intentos y registrar el resultado', 'Cambiar el color de la mesa para que se vea mejor al plegarla', 'Quitar R3 de la rúbrica, porque es el criterio con mayor diferencia', 'La acción ataca la falla observada y se comprueba con nuevos datos.'),
        ('abc', '{F} ¿Qué informe de evaluación es más completo?', 'Puntajes por criterio con evidencia, diferencias explicadas, datos de la prueba y acciones de mejora', 'Solo el total de puntos de cada evaluación, con su porcentaje del máximo', 'Solo la opinión del equipo, con una descripción de lo que más le gustó', 'Incluye puntajes, evidencia, diferencias y mejoras.'),
        ('abc', '¿Por qué no basta un solo número final?', 'Porque no dice qué criterio falló ni qué hacer; los puntajes por criterio sí lo muestran', 'Porque los números no sirven para evaluar proyectos de diseño', 'Porque la evaluación debe ser secreta y entregarse solo al equipo evaluador', 'El detalle por criterio orienta la mejora.'),
    ],
    ctx=('abc', 'Una estudiante resume: «Equipo 14 y par 11 de 16. Diferencia mayor en R3 (4 y 2): se trabó 2 de 10 veces. Acuerdo: R3 = 3 y repetir la prueba con 20 plegados». ¿Qué hace bien?', 'Contrasta puntajes con evidencia, acuerda un puntaje y propone una prueba nueva', 'Elige el puntaje más alto sin discutir', 'Ignora los datos de la prueba', 'Usa la diferencia y los datos para acordar y planear.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué es un descriptor de una rúbrica?", "El texto que explica qué se observa en cada nivel", "Permite puntuar con el mismo criterio."),
        ("¿Qué diferencia hay entre autoevaluación y coevaluación?", "La primera la hace el equipo y la segunda un par", "Ambas aportan miradas distintas y se complementan."),
        ("¿Qué límite tiene un dato de pocas pruebas?", "Da un indicio, pero no una certeza general", "Hay que declarar el tamaño de la muestra."),
    ],
    op=("Proyecto de ejemplo (inventado): «Estante Flexible». Autoevaluación del equipo con la rúbrica de la ficha: R1 3, R2 4, R3 3, R4 4. Un par evalúa: R1 3, R2 3, R3 1, R4 3. Prueba de uso: 12 intentos de armado, 9 sin ayuda y 3 con ayuda. Calcula los totales, el criterio con mayor diferencia, el porcentaje de armados sin ayuda y escribe un acuerdo con una acción de mejora.",
        "Equipo: 3 + 4 + 3 + 4 = 14. Par: 3 + 3 + 1 + 3 = 10. Mayor diferencia: R3 (3 frente a 1). Armados sin ayuda: 9 × 100 ÷ 12 = 75 %. Acuerdo: R3 = 2 y mejorar las instrucciones de armado, con una nueva prueba de 12 intentos.",
        ["calcula totales y porcentaje", "identifica diferencias con evidencia", "propone un acuerdo y una acción"],
        ["hoja con cálculos, diferencia y acción"],
        ["promediar sin conversar", "no citar los datos de la prueba", "no proponer acción"],
        "Pregunta: «¿qué dato justifica este puntaje?». Si no cita un dato, pídele que lo agregue."),
    reinforce="Evalúa un objeto de tu casa con tres criterios de 1 a 4 y escribe una evidencia por criterio.",
    extend="Explica por qué dos personas pueden dar puntajes distintos y aun así ponerse de acuerdo con evidencia.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 28 (comentarios de ejemplo a un proyecto de un par, inventados). Proyecto del par: «Refugio del Paradero», un paradero con techo de 5 m de largo, una banca de 4 m, un panel de horarios con letra de 2 cm que se lee a 4 m (regla de ejemplo: 1 cm de altura de letra por cada 2 m de distancia), y sin espacio libre para silla de ruedas. "
     "Comentario K1: «Me encantó». "
     "Comentario K2: «La banca tiene 4 m, pero no deja espacio libre para una silla de ruedas; podrías dejar un extremo libre de 90 cm». "
     "Comentario K3: «El panel está mal». "
     "Comentario K4: «El horario tiene letras de 2 cm y se lee a 4 m según la regla; cumple. Podrías sumar un contraste más fuerte con fondo claro y letra oscura». "
     "Comentario K5: «Tú no sabes diseñar». "
     "Pauta para dar comentarios: ser específico, describir lo observado, ser accionable, respetuoso y centrado en el trabajo.")
build(
    O6, 4, F,
    use="Aprenderé a dar y recibir retroalimentación entre pares: específica, descriptiva, accionable y respetuosa, centrada en el trabajo y no en la persona.",
    prior=["Sé evaluar con evidencia.", "Sé aplicar una pauta.", "Sé recibir un comentario sin tomarlo como ataque."],
    explain=[
        "La retroalimentación entre pares es una evaluación crítica que ayuda a mejorar un proyecto. Una buena retroalimentación es específica (dice qué parte), descriptiva (cuenta lo que se observó y su efecto), accionable (propone un paso posible) y respetuosa (habla del trabajo y no de la persona). «Me encantó» no ayuda a mantener lo bueno y «el panel está mal» no dice qué cambiar.",
        "Un orden útil es nombrar primero un logro con evidencia, luego un problema con su efecto y una sugerencia, y cerrar con una pregunta que invite al diálogo. Quien recibe un comentario escucha completo, pide ejemplos si no entiende, separa el comentario de su valor como persona y decide con evidencia si lo acoge. Un comentario que ataca a la persona («tú no sabes diseñar») no es retroalimentación: se pide reformularlo hacia el trabajo.",
        "Las medidas y reglas de esta clase son de ejemplo y el proyecto es inventado. En un proyecto real, las medidas de accesibilidad las define la normativa vigente y las revisa una persona profesional.",
    ],
    vocab=[("retroalimentación", "comentario que ayuda a mejorar un trabajo"), ("específica", "que señala una parte concreta del trabajo"), ("accionable", "que propone un paso posible"), ("descriptiva", "que cuenta lo observado y su efecto"), ("par", "compañera o compañero que evalúa o es evaluado")],
    worked=[
        ("Reconocer un buen comentario", "¿Qué comentario de la ficha cita un dato del panel y propone una mejora?", ["Se busca un comentario con un dato y una sugerencia.", "K4 cita las letras de 2 cm y sugiere más contraste."], "K4"),
        ("Calcular un espacio", "Si la banca de 4 m se acortara a 3 m, ¿cuántos cm quedarían libres bajo el techo de 5 m?", ["5 m = 500 cm y 3 m = 300 cm.", "500 − 300 = 200."], "200 cm"),
    ],
    mistakes=[("Comentar «tú no sabes diseñar».", "Juzga a la persona y no dice qué mejorar.", "Describe lo observado en el trabajo y propone un paso."),
              ("Responder a un comentario con enojo antes de escuchar completo.", "Se pierde información útil y el diálogo se corta.", "Escucha, pide un ejemplo y decide con evidencia.")],
    T=[
        ('abc', '¿Qué características tiene una buena retroalimentación?', 'Es específica, describe lo observado, propone una mejora y es respetuosa', 'Es breve y entusiasta, y solo dice si el trabajo gustó', 'Es dura y directa, para que quien la recibe no la olvide', 'Una buena retroalimentación orienta la mejora sin dañar a la persona.'),
        ('abc', '{F} ¿Qué comentario indica un problema de accesibilidad y propone cómo resolverlo?', 'K2: la banca no deja espacio libre para una silla de ruedas; sugiere un extremo libre de 90 cm', 'K1: me encantó, se nota que le pusieron mucho esfuerzo', 'K3: el panel está mal, hay que revisarlo con más cuidado', 'K2 señala el problema, su efecto y una propuesta concreta.'),
        ('abc', '{F} ¿Qué falla tiene el comentario K1 («Me encantó»)?', 'No dice qué parte destacó, así que no ayuda a mantener lo bueno', 'Es irrespetuoso, porque no critica ninguna parte del trabajo', 'Es demasiado largo y detallado para ser un comentario útil', 'Un elogio específico ayuda a saber qué conservar.'),
        ('abc', '{F} ¿Qué falla tiene K5 («Tú no sabes diseñar»)?', 'Juzga a la persona y no dice nada del trabajo ni de cómo mejorarlo', 'Da demasiados datos y por eso confunde sobre qué corregir', 'Es muy específico, pero no ofrece ninguna propuesta', 'Un comentario sobre la persona no orienta una mejora.'),
        ('=', '{F} Con el techo de 5 m y la banca de 4 m, ¿cuántos centímetros quedan para el extremo libre?', '500-400', 'Se pasan los metros a centímetros y se restan.', ' cm'),
        ('abc', '{F} ¿Cómo se mejora K3 («El panel está mal»)?', 'El horario se lee a 4 m, pero el contraste es medio; propongo fondo claro y letra oscura', 'El panel está muy mal y no se entiende nada, hay que rehacerlo por completo', 'No hablar del panel para no ofender a quien lo hizo ni desanimar al equipo', 'La versión mejorada describe el efecto y propone un cambio concreto.'),
        ('abc', '{F} ¿Qué dato muestra que K4 se apoya en la regla de ejemplo?', 'Las letras de 2 cm cumplen 1 cm por cada 2 m para una lectura a 4 m', 'El techo mide 5 m de largo y cubre la banca', 'La banca mide 4 m y deja poco espacio libre', 'La regla relaciona la altura de letra con la distancia de lectura.'),
        ('=', '{F} Con la regla de ejemplo, ¿cuál es la altura mínima de letra para leer a 4 m?', '4//2', 'Se aplica 1 cm por cada 2 m de distancia.', ' cm'),
        ('abc', '{F} ¿Qué orden conviene en un comentario?', 'Primero un logro con evidencia, luego un problema con su efecto y una sugerencia', 'Primero los defectos, para que se corrijan pronto, y después nada más', 'Solo una pregunta general, sin mencionar logros ni problemas', 'Ese orden reconoce lo logrado y orienta la mejora.'),
        ('abc', '{F} Quien recibe K2 se siente atacada. ¿Qué respuesta es mejor?', 'Separar el comentario del trabajo: preguntar qué medida propone, probarla y agradecer la observación', 'Rechazar el comentario por la forma en que se dijo y no probar el cambio', 'Dejar de trabajar en el proyecto hasta que el par se disculpe', 'Separar el comentario de la persona permite aprender de él.'),
        ('abc', '{F} El equipo quiere discutir K2 y negarlo sin escuchar. ¿Qué es mejor?', 'Escuchar completo, pedir un ejemplo y decidir con evidencia si se acoge', 'Negarlo para defender el proyecto y mantener la decisión del equipo', 'Aceptarlo sin pensar para evitar un conflicto con el par', 'Escuchar y revisar con evidencia permite decidir bien.'),
        ('abc', '{F} ¿Cuál es un conjunto de comentarios completo para el proyecto?', 'Logro: techo y banca coherentes; problema: sin espacio libre para silla de ruedas; sugerencia: extremo libre de 90 cm; pregunta: ¿cómo se leerá el panel con lluvia?', 'Logro: el proyecto está muy bien. Problema: se puede mejorar. Sugerencia: esforzarse más. Pregunta: ¿pueden revisarlo?', 'Logro: es el mejor proyecto del curso. Problema: ninguno. Sugerencia: no cambiar nada. Pregunta: ¿cuándo se presenta?', 'Reúne logro, problema, sugerencia y pregunta.'),
        ('abc', 'No entiendes un comentario que recibiste. ¿Qué haces?', 'Pedir una aclaración con una pregunta respetuosa', 'Ignorarlo, porque si no se entiende no es importante', 'Responder con otro comentario sobre la persona que lo escribió', 'Una pregunta respetuosa permite entender y decidir.'),
    ],
    ctx=('abc', 'Una estudiante escribe a su par: «Lo logrado: el techo de 5 m cubre la banca. Problema: no hay espacio libre para una silla de ruedas. Sugerencia: dejar un extremo libre de 90 cm; caben, porque sobra 1 m. Pregunta: ¿cómo lo ves?». ¿Qué hace bien?', 'Da logro, problema, sugerencia con dato y una pregunta', 'Solo dice que está mal', 'Habla de la persona y no del trabajo', 'El comentario cumple la pauta de la ficha.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué significa que un comentario sea accionable?", "Que propone un paso posible para mejorar", "Así quien lo recibe sabe qué hacer."),
        ("¿De qué se habla en una buena retroalimentación?", "Del trabajo, no de la persona", "Esto permite mejorar el trabajo sin dañar a nadie."),
        ("¿Qué se hace con un comentario que no se entiende?", "Se pide una aclaración con respeto", "Entenderlo es necesario para decidir si se acoge."),
    ],
    op=("Proyecto de un par (inventado): «Mesón de Biblioteca», de 180 cm de largo y 110 cm de alto, con una sola altura, un cartel con letra de 1 cm para leerse a 4 m y un estante bajo el mesón con cajones. Escribe cuatro comentarios para ese par: un logro con evidencia, un problema con su efecto, una sugerencia accionable (usa las reglas de la ficha) y una pregunta. Luego escribe cómo responderías si recibieras ese mismo comentario.",
        "Logro: el estante bajo el mesón con cajones guarda cosas sin ocupar el espacio de atención. Problema: el mesón tiene una sola altura de 110 cm, lo que dificulta a personas bajas o en silla de ruedas. Sugerencia: agregar un tramo de 80 cm. Cartel: la letra de 1 cm sirve para 2 m y no para 4 m (4 ÷ 2 = 2 cm); sugerir 2 cm. Pregunta: ¿cómo se verá el cartel con luz de ventana? Respuesta mía: gracias, probaré el tramo bajo y el cartel con letra de 2 cm.",
        ["incluye logro, problema, sugerencia y pregunta", "cita datos o reglas de la ficha", "responde con respeto al comentario"],
        ["hoja con comentarios y respuesta"],
        ["comentarios sobre la persona", "no ser específico", "no proponer pasos"],
        "Pregunta: «¿qué parte concreta señalas y qué paso propones?». Si no es concreto, pídele reescribirlo."),
    reinforce="Escribe un comentario con logro, problema y sugerencia sobre un trabajo escolar tuyo de ayer.",
    extend="Explica por qué un elogio específico ayuda tanto como una sugerencia de mejora.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 29 (resumen de evaluación de ejemplo, inventado). Proyecto: «Mesa Plegable». Hallazgos: "
     "H1 la mesa se traba en 2 de 10 plegados (función). "
     "H2 el verde oscuro de la mesa se confunde con el piso para una persona con baja visión (accesibilidad y estética). "
     "H3 el plástico reciclado de las patas viene de un proveedor a 300 km, aunque había otro a 20 km (sustentabilidad). "
     "H4 la bitácora no registró dos pruebas (proceso). "
     "Impacto y esfuerzo (1 a 5, 5 = mucho): H1 impacto 5, esfuerzo 2; H2 impacto 4, esfuerzo 1; H3 impacto 3, esfuerzo 4; H4 impacto 3, esfuerzo 1. "
     "Tiempo disponible: 10 horas. Horas estimadas: H1 4; H2 1; H3 6; H4 2.")
build(
    O6, 5, F,
    use="Aprenderé a pasar de la evaluación a las decisiones: priorizar hallazgos, planificar mejoras y hacer una autoevaluación final del proceso con aprendizajes.",
    prior=["Sé evaluar con rúbricas y evidencia.", "Sé recibir retroalimentación.", "Sé sumar horas disponibles."],
    explain=[
        "Evaluar no termina en un puntaje: sirve para decidir qué mejorar. Los hallazgos se priorizan con dos preguntas: ¿qué impacto tiene resolverlo en el propósito del proyecto? y ¿cuánto esfuerzo (tiempo, costo) pide? Suele convenir empezar por lo que tiene alto impacto y bajo esfuerzo, y poner primero lo que afecta la seguridad o el acceso, aunque no sea lo más fácil.",
        "Un plan de mejora dice qué se hará, quién lo hará, para cuándo y cómo se comprobará que funcionó. Se ajusta al tiempo disponible: si las mejoras suman más horas que las que hay, se deja para después lo de menor prioridad y se anota. Corregir de forma honesta incluye completar la bitácora con lo que sí se hizo, sin inventar lo que faltó.",
        "La autoevaluación del proceso cierra el ciclo: qué decisiones funcionaron, cuáles no, qué se aprendió y qué se haría distinto. Un aprendizaje transferible es una idea que sirve para otros proyectos, como probar con personas usuarias antes de definir un color o un mecanismo. Los datos de esta clase son inventados.",
    ],
    vocab=[("hallazgo", "problema o logro que se encuentra al evaluar"), ("impacto", "cuánto mejora el propósito al resolver un hallazgo"), ("esfuerzo", "tiempo y costo que pide resolverlo"), ("plan de mejora", "acciones ordenadas con responsable, plazo y comprobación"), ("aprendizaje transferible", "idea que sirve para otros proyectos")],
    worked=[
        ("Sumar horas", "¿Cuántas horas suman H1 y H3?", ["Se suman 4 y 6.", "4 + 6 = 10."], "10 horas"),
        ("Revisar si cabe", "Con 10 horas disponibles, ¿cuántas sobran después de H1 y H2?", ["H1 y H2 suman 4 + 1 = 5 horas.", "10 − 5 = 5."], "5 horas"),
    ],
    mistakes=[("Dejar sin corregir lo que afecta el acceso porque pide más trabajo.", "Excluye a personas y no cumple el propósito.", "Pon primero lo que afecta la seguridad y el acceso."),
              ("Completar la bitácora inventando las pruebas que faltaron.", "Se pierde la honestidad del registro.", "Registra lo que sí se hizo y anota que dos pruebas no quedaron documentadas.")],
    T=[
        ('abc', '¿Para qué se priorizan los hallazgos de una evaluación?', 'Para decidir qué mejorar primero con el tiempo y los recursos disponibles', 'Para eliminar de la lista los hallazgos más difíciles y costosos', 'Para dejar la lista más corta y que el plan parezca más simple', 'Priorizar permite usar el tiempo en lo que más mejora el proyecto.'),
        ('=', '{F} ¿Cuántas horas suman H1, H2 y H4?', '4+1+2', 'Se suman las horas estimadas de los tres hallazgos.', ' horas'),
        ('=', '{F} ¿Cuántas horas sobran de las 10 si se hacen H1, H2 y H4?', '10-4-1-2', 'Se restan al total las horas de los tres hallazgos.', ' horas'),
        ('abc', '{F} ¿Cuál hallazgo tiene el mayor impacto?', 'H1, con impacto 5', 'H3, con impacto 3', 'H4, con impacto 3', 'La ficha da impacto 5 a H1, el mayor valor.'),
        ('abc', '{F} ¿Por qué H3 se deja para después?', 'Tiene impacto medio (3) y esfuerzo alto (4, 6 horas), y no cabe junto con las otras mejoras', 'Porque la sustentabilidad no importa en un proyecto escolar', 'Porque es el hallazgo con menor esfuerzo y menos horas', 'Su relación impacto-esfuerzo es la menos favorable.'),
        ('=', '{F} Si se agrega H3 al plan, ¿cuántas horas se pasarían del total disponible?', '4+1+2+6-10', 'Se suman todas las horas y se resta el tiempo disponible.', ' horas'),
        ('abc', '{F} H2 es una barrera de accesibilidad. ¿Qué acción concreta propones?', 'Cambiar a un color con mayor contraste con el piso y probarlo con una persona con baja visión', 'Dejar el color y avisar a las personas con baja visión que tengan cuidado al usarla', 'Pintar la mesa con un verde todavía más oscuro, para que se note más', 'La acción ataca el problema y se comprueba con una persona usuaria.'),
        ('abc', '{F} ¿Cuál es el orden de prioridad más razonable?', 'Primero H1 y H2 (alto impacto y poco esfuerzo; H2 es de acceso), luego H4 y, si queda tiempo, H3', 'Primero H3 (porque es sustentabilidad), luego H4, H2 y al final H1', 'Primero H4, que es la más corta, y dejar H1, H2 y H3 para otro proyecto', 'Pone primero lo de más impacto y menor esfuerzo, y deja lo costoso para el final.'),
        ('abc', '{F} ¿Qué debe tener cada acción de un plan de mejora?', 'Qué se hará, quién, para cuándo y cómo se comprobará', 'Solo el nombre del hallazgo y su nivel de impacto', 'Solo un plazo y un responsable, sin forma de comprobarlo', 'Esos cuatro datos hacen verificable el plan.'),
        ('abc', '{F} Alguien propone dejar H1 porque «2 de 10 es poco». ¿Qué respuesta es mejor?', 'Una falla de 2 en 10 afecta la función en el uso real; con alto impacto y bajo esfuerzo conviene corregirla', 'Tiene razón: 2 de 10 es poco y no justifica gastar horas en el plan', 'Hay que repetir la prueba hasta que la falla ya no aparezca en los registros', 'Una falla frecuente afecta a las personas usuarias y se resuelve con poco esfuerzo.'),
        ('abc', '{F} La bitácora no registró dos pruebas. ¿Qué corrección honesta corresponde?', 'Registrar las pruebas que sí se hicieron y anotar que dos no quedaron documentadas, sin inventarlas', 'Inventar las dos entradas con fechas anteriores, para que la bitácora quede completa', 'Borrar la bitácora y empezar otra desde la última prueba', 'Corregir con honestidad evita falsear el proceso.'),
        ('abc', '{F} ¿Qué cierre de autoevaluación es completo?', 'Qué funcionó (pruebas de uso), qué no (proveedor lejano), qué se aprendió (probar el contraste) y qué se haría distinto', 'Todo estuvo bien y el equipo cumplió el plan sin mayores problemas', 'Faltó tiempo para terminar, y eso explica todos los problemas', 'Incluye decisiones, aprendizajes y mejoras concretas.'),
        ('abc', '¿Qué es un aprendizaje transferible?', 'Una idea que sirve para otros proyectos, como probar con personas usuarias antes de definir un mecanismo', 'Un dato muy específico que solo sirve para el proyecto recién terminado', 'Un resultado final que se copia sin cambios en el siguiente proyecto', 'Un aprendizaje transferible se puede aplicar en nuevos proyectos.'),
    ],
    ctx=('abc', 'Una estudiante escribe: «Plan: H1, 4 horas, la hará Ana, el viernes, y se comprueba con 20 plegados. H2, 1 hora, la hará Beto, y se prueba con una persona con baja visión. H3 queda para después». ¿Qué hace bien?', 'Define acción, responsable, plazo y comprobación, y deja lo costoso para después', 'No indica quién hará cada acción', 'Mezcla todo sin prioridad', 'El plan es verificable y está ajustado al tiempo.'),
    sc=[
        ("En Diseño y arquitectura: ¿qué dos preguntas priorizan un hallazgo?", "Cuánto impacto tiene y cuánto esfuerzo pide", "Se empieza por alto impacto y bajo esfuerzo."),
        ("¿Qué se pone primero en un plan de mejora?", "Lo que afecta la seguridad o el acceso", "Dejar personas fuera no cumple el propósito."),
        ("¿Qué incluye una autoevaluación final?", "Decisiones que funcionaron, las que no, aprendizajes y mejoras", "Cierra el ciclo de aprendizaje del proyecto."),
    ],
    op=("Hallazgos de ejemplo de un proyecto «Banca Modular»: A1 los módulos se separan al moverlos (impacto 5, esfuerzo 2, 3 horas); A2 el color del respaldo se confunde con el suelo para una persona con baja visión (impacto 4, esfuerzo 1, 1 hora); A3 el proveedor de madera está lejos (impacto 3, esfuerzo 4, 5 horas); A4 faltó fechar tres entradas de bitácora (impacto 2, esfuerzo 1, 1 hora). Tiempo disponible: 6 horas. Ordena los hallazgos, elige cuáles caben en 6 horas, redacta una acción con responsable, plazo y comprobación, y escribe un aprendizaje transferible.",
        "Orden: A1, A2, A4, A3. Caben A1 (3 h), A2 (1 h) y A4 (1 h) = 5 horas, y sobra 1 hora; A3 queda para después. Acción A1: reforzar la unión de los módulos, responsable Carla, para el jueves, comprobar moviendo la banca 10 veces. Aprendizaje: probar los movimientos de uso antes de definir las uniones.",
        ["ordena con impacto y esfuerzo", "ajusta el plan al tiempo disponible", "redacta una acción verificable y un aprendizaje"],
        ["hoja con orden, plan y aprendizaje"],
        ["no sumar las horas", "dejar lo de acceso para el final", "no incluir comprobación"],
        "Pregunta: «¿cómo sabrás que funcionó?». Si no responde, pídele definir la comprobación."),
    reinforce="Haz una lista de tres cosas que mejorarías de un trabajo reciente y ordénalas según impacto y esfuerzo.",
    extend="Explica por qué un buen plan de mejora puede dejar fuera una mejora importante, pero igual anotarla.",
)
