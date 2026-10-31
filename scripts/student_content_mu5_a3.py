"""Student material for 5.º básico Música, OA 02 (respuesta cada vez más elaborada a la música escuchada e interpretada, con medios verbal, corporal, musical y visual).

Las músicas de los ejercicios son descripciones originales inventadas; no hay respuestas «correctas» sobre qué sentir: se evalúa cuánto se apoya la respuesta en lo que se oyó.
"""
from __future__ import annotations

from student_content_mu5_a import LEY, OA2, P, L, pulses
from student_lessons import arith, ex

# ---------------------------------------------------------------- OA 02 · clase 1 (niveles de elaboración)
PZ1 = ("«Tormenta lejana» (música inventada): empieza con un tambor grave y suave; poco a poco el tambor suena más fuerte y más rápido; "
       "entran unos platillos agudos; al final todo baja hasta quedar muy suave.")
RUB = ("Nivel 1: solo dice si le gustó o no. Nivel 2: dice una sensación, emoción o idea, pero sin razón sonora. "
       "Nivel 3: dice la sensación o idea y una razón sonora (algo que se oyó). "
       "Nivel 4: dice la sensación o idea, la razón sonora y en qué momento de la música ocurre")

L(
    OA2, 1,
    f"Lápiz y papel. No necesitas audio: la música de la clase está descrita por escrito. {PZ1} Escala de niveles de la clase: {RUB}.",
    "Aprenderé a expresar lo que me hace sentir una música con cada vez más detalle: sensación, razón sonora y momento. Sirve para explicar mejor lo que escucho.",
    ["Sé nombrar cualidades del sonido: altura, intensidad, timbre y duración.", "Sé decir si un sonido es fuerte o suave.", "Sé que cada persona puede sentir algo distinto con una música."],
    [
        "Una misma música puede hacer sentir cosas distintas a distintas personas, y eso está bien. No hay una emoción «correcta». Lo que cambia es cuánto detalle damos al explicar lo que sentimos o imaginamos. Una respuesta más elaborada dice qué sentí, por qué lo sentí y en qué parte de la música lo sentí.",
        f"Para medir cuánto detalle tiene una respuesta usamos cuatro niveles. {RUB}. Una razón sonora es algo que se oye: un instrumento, un sonido grave o agudo, fuerte o suave, rápido o lento. Con la música «Tormenta lejana»: «Me gustó» es nivel 1; «Sentí miedo» es nivel 2; «Sentí miedo porque el tambor sonaba grave» es nivel 3.",
        "Para subir de nivel no sirve repetir palabras ni alargar la frase: sirve agregar información nueva. De nivel 2 a 3 se agrega una razón sonora. De 3 a 4 se agrega el momento en que ocurre, por ejemplo «sobre todo al final». Además, comentar lo que sentimos es siempre una decisión personal: puedes elegir qué compartir.",
    ],
    [("sensación o emoción", "lo que siento al escuchar, como calma o miedo"), ("idea", "algo que imagino al escuchar, como un barco o una carrera"), ("razón sonora", "algo que se oye y explica lo que sentí"), ("respuesta elaborada", "respuesta con sensación, razón y detalle"), ("momento", "la parte de la música en que ocurre algo")],
    [
        ("Ubicar el nivel", "«Me dio miedo porque el tambor sonaba grave y fuerte, sobre todo cuando entran los platillos.» ¿Qué nivel tiene según la escala de la clase?", ["Dice una emoción: miedo.", "Da razones sonoras: grave y fuerte.", "Dice el momento: cuando entran los platillos.", "Cumple lo del nivel 4."], "Nivel 4"),
        ("Subir de nivel", "«Sentí calma» es nivel 2. ¿Qué hay que agregar para que sea nivel 3: (a) otra emoción o (b) una razón sonora?", ["El nivel 3 pide una razón sonora.", "Agregar otra emoción no da una razón."], "(b)"),
    ],
    [
        ("Pensar que una respuesta larga siempre es de nivel alto.", "El nivel depende de la información nueva, no del largo.", "Revisa si dice una razón sonora y el momento."),
        ("Creer que hay emociones correctas e incorrectas.", "Cada persona puede sentir algo distinto con la misma música.", "Lo que se evalúa es el detalle y la razón, no la emoción."),
    ],
    [
        ex("«Me gustó mucho.» ¿Qué nivel tiene según la escala de la clase?", "Nivel 1", "Solo dice que le gustó."),
        ex("«Sentí calma.» ¿Qué nivel tiene?", "Nivel 2", "Dice una sensación, pero no una razón sonora."),
        ex("¿Cuál de estas respuestas da una razón sonora: (a) «Me dio miedo.» o (b) «Me dio miedo porque sonaba grave y fuerte.»?", "(b)", "Menciona lo que se oyó: grave y fuerte."),
    ],
    [
        ex("«Sentí alegría porque la flauta sonaba aguda y rápida.» ¿Qué nivel tiene?", "Nivel 3", "Tiene emoción y razones sonoras, pero no dice el momento."),
        ex("«Sentí miedo porque el tambor sonaba grave.» Para ser nivel 4, ¿qué le falta?", "Decir en qué momento ocurre", "El nivel 4 agrega el momento a la emoción y la razón."),
        ex("En «Tormenta lejana», ¿qué hace el tambor al comienzo: suena fuerte o suave?", "Suave", "La descripción dice que empieza grave y suave."),
    ],
    [
        ex("«Me imaginé un barco en una tormenta porque el tambor sonaba grave y se aceleraba; lo imaginé sobre todo hacia el final.» ¿Qué nivel tiene?", "Nivel 4", "Tiene una idea, razones sonoras y el momento."),
        ex("«Me gustó porque es linda.» ¿Qué nivel tiene?", "Nivel 1", "Solo dice si le gustó; «linda» no es una razón sonora."),
        ex("Una respuesta dice: «Sentí tristeza porque la música baja y baja». ¿Qué nivel tiene si solo da esa razón y no dice el momento?", "Nivel 3", "Tiene emoción y una razón sonora."),
    ],
    [
        ex("Ana dice: «Sentí calma porque iba lenta y suave». Beto dice: «Sentí calma, calma y más calma». ¿Cuál tiene más elaboración y por qué?", "La de Ana, porque da razones sonoras", "Beto solo repite; Ana explica con lo que oyó."),
        ex("Pedro cree que repetir muchas veces la palabra «bonita» sube una respuesta de nivel. ¿Es cierto?", "No", "El nivel sube con razones sonoras y detalle nuevo, no con repetir."),
    ],
    [
        arith("En un curso de 30 estudiantes, 6 dieron respuestas de nivel 1, 9 de nivel 2 y 8 de nivel 3. Los demás dieron respuestas de nivel 4. ¿Cuántos fueron?", "30-6-9-8", "Se restan los otros tres grupos del total.", " estudiantes"),
        ex("Una respuesta de nivel 3 quiere llegar a nivel 4. ¿Qué debe agregar?", "El momento en que ocurre", "Eso es lo que distingue el nivel 4."),
    ],
    [ex("Al escuchar una canción de cuna lenta y suave, ¿cuál es una respuesta de nivel 3: (a) «Sentí sueño» o (b) «Sentí sueño porque iba lenta y suave»?", "(b)", "Une la sensación con una razón sonora.")],
    [ex("¿Qué es una razón sonora?", "Algo que se oye y explica lo que sentí", "Es la evidencia en el sonido."), ex("¿Hay una emoción correcta para cada música?", "No", "Cada persona puede sentir algo distinto."), ex("¿Qué agrega el nivel 4 que no tiene el nivel 3?", "El momento en que ocurre", "Es el detalle adicional.")],
    (
        f"Escucha o recuerda una música breve (puede ser una canción tranquila que conozcas o la descripción de «Tormenta lejana»). Escribe una respuesta de nivel 4 con una sensación o idea, razones sonoras y el momento. Después escribe cómo quedaría de nivel 2 y de nivel 3. Compartir lo que sientes es opcional: puedes usar «Tormenta lejana».",
        "Nivel 2: Sentí miedo. Nivel 3: Sentí miedo porque el tambor sonaba grave. Nivel 4: Sentí miedo porque el tambor sonaba grave y cada vez más fuerte, sobre todo cuando entran los platillos.",
        ["escribe tres niveles distintos", "el nivel 4 tiene sensación, razón sonora y el momento", "las razones se apoyan en lo que se oye"],
        ["tres frases escritas"],
        ["agregar solo adjetivos sin razón sonora", "olvidar el momento en el nivel 4"],
        "Reconoce cada nivel subido y pregunta: ¿qué escuchaste que te hizo sentir eso? Si falta el momento, pide ubicarlo («al principio», «al final»).",
    ),
    "Di en una frase cómo te hizo sentir el sonido de la lluvia y agrega una razón sonora.",
    "Escribe una respuesta de nivel 4 a una música que hayas escuchado esta semana.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (representar con medios verbal, corporal, musical y visual)
CODIGO = ("Código de la clase: altura = posición (arriba es agudo, abajo es grave); intensidad = tamaño o grosor (gesto grande o línea gruesa es fuerte, "
          "gesto pequeño o línea fina es suave); tempo = velocidad (trazos cortos y seguidos o movimiento veloz es rápido; trazos largos o movimiento pausado es lento)")

L(
    OA2, 2,
    f"Hoja, lápices de colores y espacio para moverte con seguridad (sin objetos en el suelo). {CODIGO}. Las músicas están descritas por escrito.",
    "Aprenderé a expresar lo que escucho con cuatro medios: palabras (verbal), movimiento (corporal), sonidos propios (musical) y dibujo (visual), usando un código claro. Sirve para mostrar una música de varias maneras y comprobar qué se oyó.",
    ["Sé describir un sonido como agudo o grave, fuerte o suave.", "Sé que el tempo es rápido o lento.", "Sé que una respuesta puede tener razones sonoras."],
    [
        "Se puede expresar lo que sugiere una música con distintos medios. El medio verbal usa palabras, habladas o escritas. El medio corporal usa el movimiento del cuerpo. El medio musical usa sonidos propios, con la voz, palmas o instrumentos. El medio visual usa dibujos, colores o líneas. Cada medio muestra la música a su manera y ninguno es mejor que otro.",
        f"Para que un dibujo o un movimiento digan algo de la música, conviene tener un código. {CODIGO}. Así, una línea fina y larga, arriba en la hoja, muestra un sonido agudo, suave y lento. Un movimiento grande, bajo y pausado muestra un sonido grave, fuerte y lento.",
        "Usar un código permite que otra persona entienda tu dibujo o tu movimiento y compruebe que mostraste lo que se oyó. Además, puedes combinar dos medios: por ejemplo, dibujar y luego explicar con palabras. Cuando combines medios, procura que cuenten lo mismo: si el dibujo muestra calma, tu movimiento también debe ser tranquilo.",
    ],
    [("medio verbal", "expresar con palabras"), ("medio corporal", "expresar con movimiento"), ("medio musical", "expresar con sonidos propios"), ("medio visual", "expresar con dibujo, color o línea"), ("código", "regla que dice qué significa cada rasgo del dibujo o movimiento")],
    [
        ("Dibujar un sonido", "Un sonido es agudo, suave y lento. Con el código de la clase, ¿cómo lo dibujas?", ["Agudo: arriba en la hoja.", "Suave: línea fina.", "Lento: trazos largos."], "Línea fina y larga, arriba en la hoja"),
        ("Leer un movimiento", "Una niña mueve los brazos con gestos grandes, a ras del suelo y muy despacio. ¿Qué sonido representa?", ["Gestos grandes: fuerte.", "A ras del suelo: grave.", "Muy despacio: lento."], "Un sonido grave, fuerte y lento"),
    ],
    [
        ("Dibujar sin seguir el código.", "Nadie puede comprobar qué sonido muestra el dibujo.", "Decide antes qué significa la posición, el grosor y el largo."),
        ("Combinar medios que cuentan cosas distintas.", "Un dibujo agitado y un movimiento tranquilo se contradicen.", "Revisa que ambos muestren las mismas cualidades."),
    ],
    [
        ex("Una niña dibuja una línea gruesa en la parte baja de la hoja. Según el código, ¿qué sonido representa?", "Grave y fuerte", "Abajo es grave y gruesa es fuerte."),
        ex("Según el código, mover el cuerpo muy rápido representa un sonido, ¿lento o rápido?", "Rápido", "La velocidad del movimiento muestra el tempo."),
        ex("¿Cuál de estos es un medio visual: (a) bailar, (b) dibujar, (c) cantar?", "(b)", "Dibujar usa líneas y colores."),
    ],
    [
        ex("Un niño responde a la música bailando. ¿Qué medio usa?", "Corporal", "Se expresa con movimiento."),
        ex("Una niña canta «la» siguiendo la música para mostrar lo que sintió. ¿Qué medio usa?", "Musical", "Usa sonidos propios."),
        ex("Un sonido es agudo, suave y lento. ¿Cuál es su dibujo: (a) línea gruesa abajo con trazos cortos, o (b) línea fina arriba con trazo largo?", "(b)", "Agudo es arriba, suave es fina y lento es largo."),
    ],
    [
        ex("¿Cómo mueves los brazos para representar un sonido grave, fuerte y lento?", "Gestos grandes, bajos y despacio", "Grave es bajo, fuerte es grande y lento es despacio."),
        ex("Un dibujo tiene una línea gruesa arriba con trazos cortos y seguidos. ¿Qué sonido representa?", "Agudo, fuerte y rápido", "Arriba es agudo, gruesa es fuerte y trazos cortos y seguidos son rápido."),
        ex("Una música tiene cuatro sonidos: 1) grave y fuerte, 2) agudo y suave, 3) grave y suave, 4) agudo y fuerte. ¿En cuál va una línea gruesa arriba?", "4", "Arriba es agudo y gruesa es fuerte: eso es el sonido 4."),
    ],
    [
        ex("Julia dibuja una línea fina arriba para un trueno grave y fuerte. ¿Qué dos cosas debe cambiar?", "La posición (abajo) y el grosor (gruesa)", "Grave va abajo y fuerte va con línea gruesa."),
        ex("Una niña dibuja y además baila la misma música. ¿Qué debe coincidir entre ambos medios?", "Que muestren las mismas cualidades del sonido", "Si los dos cuentan lo mismo, son coherentes."),
    ],
    [
        arith("Una música tiene 6 sonidos y 4 son agudos. Los demás son graves. ¿Cuántos trazos van en la parte baja de la hoja?", "6-4", "Los graves van abajo y se obtienen restando.", " trazos"),
        ex("Una melodía baja desde un sonido agudo hasta uno grave. En el dibujo con el código, ¿la línea sube o baja en la hoja?", "Baja", "Agudo está arriba y grave abajo, así que la línea desciende."),
    ],
    [ex("Para un cuento de un gigante que camina, ¿qué movimiento sigue mejor el código: (a) pasos pequeños y rápidos o (b) pasos grandes, lentos y fuertes?", "(b)", "Un gigante suena grave, fuerte y lento.")],
    [ex("¿Qué medio usa el dibujo?", "Visual", "Muestra con líneas y colores."), ex("¿Qué indica la posición alta en la hoja?", "Sonido agudo", "Arriba representa agudo."), ex("¿Para qué sirve un código?", "Para que otras personas entiendan lo que mostré", "Dice qué significa cada rasgo.")],
    (
        "Elige una música (puede ser «Tormenta lejana»: tambor grave y suave que crece, platillos agudos, y baja al final). Haz un dibujo de una línea con el código de la clase y un movimiento corporal pequeño y seguro que muestre lo mismo. Escribe una frase verbal que explique qué muestra cada medio. Compartir tu trabajo es opcional.",
        "Dibujo: una línea larga abajo que se va engrosando (el tambor grave que crece), un trazo corto y fino arriba (los platillos agudos) y al final la línea vuelve a afinarse. Movimiento: de pie, brazos pequeños y bajos, luego más grandes, y otra vez pequeños. Frase: la línea que se engrosa abajo muestra el tambor grave que crece.",
        ["el dibujo sigue el código", "el movimiento cuenta lo mismo que el dibujo", "la frase explica los dos medios"],
        ["dibujo", "movimiento", "frase escrita"],
        ["dibujar líneas sin significado", "un movimiento que contradice el dibujo"],
        "Reconoce la coherencia entre medios y pide señalar en el dibujo el momento exacto de un cambio en la música.",
    ),
    "Dibuja en una línea cómo suena una campana aguda que se apaga poco a poco.",
    "Haz un dibujo y un movimiento que muestren una música rápida, aguda y suave, y explica cómo usaste el código.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (responder con sonidos propios)
PAT_A = ("TA", "TA", "ti-ti", "TAA")

L(
    OA2, 3,
    f"Tus palmas, tu voz y objetos seguros (una caja de cartón, una cuchara de madera). Toca a volumen bajo. Leyenda de ritmo: {LEY}. Dinámica: p suave, mf medio fuerte, f fuerte; « < » sube poco a poco.",
    "Aprenderé a expresar una idea o sensación creando una respuesta con sonidos propios, eligiendo altura, intensidad, tempo y duración. Sirve para decir con sonidos lo que la música me sugiere.",
    ["Sé tocar un patrón con palmas.", "Sé leer p, f y las flechas de crescendo y diminuendo.", "Sé usar el código de la clase anterior."],
    [
        "Una respuesta musical expresa con sonidos propios lo que una música o una idea sugiere. Primero decide qué quieres mostrar, por ejemplo un elefante que camina o una lluvia fina. Luego elige qué cualidades del sonido lo muestran mejor: altura (agudo o grave), intensidad (fuerte o suave), tempo (rápido o lento) y duración (sonidos largos o cortos).",
        "Un elefante camina con sonidos graves, fuertes y lentos. Una lluvia fina suena con sonidos agudos, suaves y rápidos. Un cambio repentino de intensidad, de p a f de golpe, sugiere sorpresa. Un crescendo sugiere algo que se acerca o que crece. Un diminuendo sugiere algo que se aleja o se calma. Recuerda cuidar el volumen: la expresión no necesita gritar.",
        f"Para que se entienda, escribe tu respuesta: el patrón de ritmo y la dinámica. Con la leyenda de la clase, el patrón {P(*PAT_A)} ocupa {pulses(*PAT_A)} pulsos. Puedes repetirlo, variarlo o combinarlo con otros. Al final, cuenta a otra persona qué idea quisiste mostrar y qué decisiones tomaste para lograrlo.",
    ],
    [("respuesta musical", "expresar una idea con sonidos propios"), ("cambio repentino", "cambio de intensidad de golpe, sin pasar poco a poco"), ("crescendo", "sube poco a poco"), ("diminuendo", "baja poco a poco"), ("idea musical", "lo que quiero mostrar con mis sonidos")],
    [
        ("Elegir cualidades", "Quieres mostrar un elefante que camina. ¿Qué eliges: (a) sonidos graves, fuertes y lentos o (b) agudos, suaves y rápidos?", ["Un elefante es grande y pesado.", "Lo grande suena grave y fuerte.", "Camina despacio."], "(a)"),
        ("Contar pulsos", f"Un niño toca el patrón {P(*PAT_A)} y lo repite 3 veces. ¿Cuántos pulsos toca?", [f"Una vuelta ocupa 1 + 1 + 1 + 2 = {pulses(*PAT_A)} pulsos.", f"{pulses(*PAT_A)} × 3 = {pulses(*PAT_A) * 3}."], f"{pulses(*PAT_A) * 3} pulsos"),
    ],
    [
        ("Elegir sonidos que no tienen relación con la idea.", "La respuesta no muestra lo que quería mostrar.", "Antes de tocar, decide qué cualidades del sonido muestran tu idea."),
        ("Tocar muy fuerte para que se note.", "El volumen alto cansa y puede dañar el oído.", "Muestra la fuerza con el contraste entre p y mf, sin gritar."),
    ],
    [
        ex("Para imitar gotas de una lluvia fina con los dedos sobre la mesa, ¿conviene tocar suave o fuerte?", "Suave", "Una lluvia fina suena ligera."),
        ex("Responder a una música con palmas y voz, ¿qué medio es?", "Musical", "Usa sonidos propios."),
        ex("Un diminuendo sugiere algo que, ¿se acerca o se aleja?", "Se aleja", "El sonido baja poco a poco, como algo que se va."),
    ],
    [
        ex(f"¿Cuántos pulsos ocupa el patrón {P(*PAT_A)}?", str(pulses(*PAT_A)), "TA 1, TA 1, ti-ti 1 y TAA 2."),
        ex("Quieres mostrar sorpresa con un cambio repentino. ¿Qué eliges: (a) p y luego f de golpe o (b) un crescendo largo?", "(a)", "Un cambio de golpe sorprende; el crescendo es gradual."),
        ex("Un crescendo de p a f sugiere algo que, ¿se acerca o se aleja?", "Se acerca", "El sonido crece poco a poco, como algo que llega."),
    ],
    [
        arith(f"Un niño toca {P(*PAT_A)} tres veces y después un TAA más para cerrar. ¿Cuántos pulsos suenan en total?", f"{pulses(*PAT_A)}*3+2", "Tres vueltas del patrón más los 2 pulsos del TAA final.", " pulsos"),
        ex("¿Qué dinámica expresa «un animal grande que se acerca»: (a) f – > – p o (b) p – < – f?", "(b)", "Crescendo: el sonido crece como algo que se acerca."),
        ex("Para mostrar un pájaro pequeño, ¿conviene un sonido agudo o grave?", "Agudo", "Lo pequeño suena agudo."),
    ],
    [
        ex("Luis quiere mostrar una tormenta que ya está encima, pero la responde con sonidos suaves y lentos. ¿Qué dos cambios la mostrarían mejor?", "Subir la intensidad y acelerar", "Una tormenta encima suena fuerte y agitada."),
        ex("Dos respuestas al «amanecer»: una va de p a f con crescendo y la otra se queda en f todo el tiempo. ¿Cuál muestra mejor algo que va creciendo?", "La que hace crescendo", "El crescendo muestra el crecimiento gradual."),
    ],
    [
        arith("La respuesta musical de un grupo dura 16 pulsos en tres partes. La parte 1 tiene 6 pulsos y la parte 2 también 6. ¿Cuántos pulsos tiene la parte 3?", "16-6-6", "Se restan las dos partes conocidas del total.", " pulsos"),
        arith(f"Un patrón de {pulses('tiri-tiri', 'TAA', 'SIL', 'ti-ti')} pulsos (tiri-tiri – TAA – SIL – ti-ti) se repite 4 veces. ¿Cuántos pulsos suenan?", f"{pulses('tiri-tiri', 'TAA', 'SIL', 'ti-ti')}*4", "Una vuelta ocupa 1 + 2 + 1 + 1 pulsos.", " pulsos"),
    ],
    [ex("Para mostrar con sonidos un tren que se aleja, ¿qué dinámica eliges: (a) f – > – pp o (b) pp – < – ff?", "(a)", "Algo que se aleja suena cada vez más suave: un diminuendo.")],
    [ex("¿Cómo se llama el cambio de intensidad poco a poco hacia fuerte?", "Crescendo", "La flecha se abre."), ex("¿Qué cualidades eliges para un elefante?", "Graves, fuertes y lentos", "Grande y pesado."), ex("¿Qué debes cuidar al tocar?", "El volumen", "Un volumen cómodo protege el oído.")],
    (
        "Elige una idea: «un elefante que camina» o «una lluvia fina». Crea una respuesta musical de 8 pulsos con palmas, voz y un objeto seguro (por ejemplo, una caja de cartón). Escribe tu patrón con los símbolos de la leyenda, la dinámica y qué cualidades elegiste y por qué. Tócala a volumen bajo.",
        "Idea: lluvia fina. Patrón: tiri-tiri – tiri-tiri – ti-ti – ti-ti – TA – TA – TA – SIL (8 pulsos). Dinámica p. Cualidades: sonidos agudos, suaves y rápidos con los dedos.",
        ["la respuesta dura 8 pulsos", "las cualidades elegidas muestran la idea", "escribe el patrón y justifica las decisiones"],
        ["interpretación", "patrón escrito", "justificación breve"],
        ["no ajustar los pulsos al total pedido", "elegir cualidades que no muestran la idea"],
        "Reconoce la idea y pide que cuente los pulsos; pregunta qué cambiaría para mostrar lo contrario.",
    ),
    "Imita con tu voz el sonido de una puerta que se abre muy despacio y descríbelo con dos cualidades del sonido.",
    "Crea una respuesta musical que muestre una idea de tu elección con un crescendo y escribe qué quisiste mostrar.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (ajustar y elaborar la respuesta)
CR4 = ["nombra una sensación, emoción o idea", "da una razón sonora", "dice en qué momento ocurre", "la muestra además con un segundo medio (dibujo, gesto o sonido)"]
BA = "Sentí tristeza."
BB = "Sentí tristeza porque la melodía bajaba lentamente; además la dibujé con una línea que baja."
BC = "Sentí tristeza porque iba lenta y suave, sobre todo al final; además la mostré con un movimiento lento de brazos hacia abajo."
CR4_TXT = "; ".join(f"({i}) {c}" for i, c in enumerate(CR4, 1))

L(
    OA2, 4,
    f"Lápiz y papel. Criterios de la clase: {CR4_TXT}. Respuestas de ejemplo: A: «{BA}». B: «{BB}». C: «{BC}».",
    "Aprenderé a mejorar una respuesta a la música agregando detalle y combinando medios, revisando con criterios y escuchando de nuevo. Sirve para expresar mis ideas con más claridad y precisión.",
    ["Sé que hay niveles de elaboración.", "Sé representar la música con dibujo, movimiento y sonidos.", "Sé dar una razón sonora."],
    [
        f"Mejorar una respuesta es comparar lo que dijiste con criterios y agregar lo que falta. Los criterios de la clase son: {CR4_TXT}. Cada criterio cumplido suma un punto. La respuesta A («{BA}») cumple solo el criterio 1. La respuesta B cumple los criterios 1, 2 y 4: le falta decir el momento.",
        f"La respuesta C cumple los cuatro criterios, porque dice una emoción, una razón (lenta y suave), un momento (al final) y un segundo medio (el movimiento). Para mejorar, no cambies todo: busca el criterio que falta y agrégalo. Después, vuelve a escuchar la música para comprobar que lo que dices realmente se oye.",
        "Si usas dos medios, revisa que sean coherentes: un dibujo con trazos cortos y agitados no combina con una emoción de calma. También respeta las respuestas de otras personas: dos personas pueden sentir cosas distintas, y ambas respuestas son válidas si se apoyan en lo que se oye. Se puede sugerir un detalle a mejorar, siempre con amabilidad.",
    ],
    [("criterio", "pregunta con que se revisa una respuesta"), ("ajustar", "cambiar algo para mejorar"), ("coherente", "que los medios cuentan lo mismo"), ("segundo medio", "otro modo de expresar, como dibujo o gesto"), ("sugerencia", "idea amable para mejorar")],
    [
        ("Contar criterios", f"Respuesta B: «{BB}». Con los criterios de la clase, ¿cuántos cumple y cuál le falta?", ["Emoción: sí, tristeza.", "Razón sonora: sí, bajaba lentamente.", "Momento: no.", "Segundo medio: sí, el dibujo.", "Cumple 3 y le falta el 3."], "Cumple 3 de 4; le falta decir el momento"),
        ("Decidir qué agregar", f"Respuesta A: «{BA}». Si solo puedes agregar una cosa para que sea más elaborada, ¿qué agregas primero según los criterios?", ["Cumple el criterio 1.", "El siguiente es la razón sonora."], "Una razón sonora"),
    ],
    [
        ("Cambiar toda la respuesta al primer problema.", "Se pierde lo que ya estaba bien.", "Agrega solo el criterio que falta."),
        ("Juzgar a otra persona porque sintió algo distinto.", "Cada persona puede sentir algo distinto con la misma música.", "Revisa si la respuesta se apoya en lo que se oye, no si coincide contigo."),
    ],
    [
        ex(f"Respuesta A: «{BA}». ¿Cuántos criterios cumple?", "1", "Solo nombra una emoción."),
        ex(f"Respuesta C: «{BC}». ¿Cuántos criterios cumple?", "4", "Tiene emoción, razón, momento y segundo medio."),
        ex(f"En la respuesta C: «{BC}», ¿qué segundo medio usa?", "Un movimiento de brazos", "Lo dice la frase: movimiento lento de brazos hacia abajo."),
    ],
    [
        ex(f"Respuesta B: «{BB}». ¿Qué segundo medio usa?", "Un dibujo", "Dibuja una línea que baja."),
        ex(f"En la respuesta C: «{BC}», ¿en qué momento ocurre lo que describe?", "Al final", "Lo dice la frase: sobre todo al final."),
        ex("Una persona sintió alegría con una música en que otra sintió calma. ¿Cuál respuesta es válida?", "Las dos, si se apoyan en lo que se oye", "Cada persona puede sentir algo distinto."),
    ],
    [
        ex(f"Respuesta B: «{BB}». ¿Qué dato debes agregarle para cumplir el criterio que le falta?", "El momento en que ocurre, como «al final»", "Lo que falta es ubicar la razón en la música."),
        ex("Una respuesta dice «Sentí calma» y el dibujo muestra trazos cortos, gruesos y muy seguidos. ¿Son coherentes los dos medios?", "No", "Los trazos cortos, gruesos y seguidos son rápido y fuerte, lo contrario de calma."),
        ex("Para dar una sugerencia amable sobre la respuesta A, ¿cuál es mejor: (a) «Estás muy corto» o (b) «Podrías contar qué escuchaste que te hizo sentir eso»?", "(b)", "Es amable y dice qué mejorar."),
    ],
    [
        ex("Una niña revisa su respuesta, cumple los criterios 1, 2 y 3 y no el 4. ¿Qué le falta?", "Mostrarla con un segundo medio", "El criterio 4 es el segundo medio."),
        ex("Un niño dice que su respuesta ya es perfecta porque es muy larga. ¿Qué debe revisar?", "Si cumple los criterios, no el largo", "Una respuesta larga puede no cumplir los criterios."),
    ],
    [
        arith("En un curso de 28 estudiantes, 7 cumplieron 1 criterio, 9 cumplieron 2 criterios y 8 cumplieron 3. Los demás cumplieron los 4. ¿Cuántos fueron?", "28-7-9-8", "Se restan los otros grupos del total.", " estudiantes"),
        arith("Una estudiante cumplía 1 criterio y después de mejorar cumple 4. ¿Cuántos criterios sumó?", "4-1", "Se resta lo que cumplía antes de lo que cumple ahora.", " criterios"),
    ],
    [ex("Una estudiante escribe «Sentí calma porque la música iba lenta y suave». Con el código de la clase, ¿qué dibujo es coherente: (a) trazos largos y finos o (b) trazos cortos, gruesos y seguidos?", "(a)", "Largo es lento y fino es suave: coincide con lo que dice.")],
    [ex("¿Qué haces primero para mejorar una respuesta?", "Compararla con los criterios", "Así sabes qué falta."), ex("¿Se puede comparar quién sintió la emoción «correcta»?", "No", "Todas las emociones apoyadas en lo oído son válidas."), ex("¿Qué haces después de agregar un detalle?", "Volver a escuchar para comprobar", "Debe corresponder con lo que se oye.")],
    (
        f"Escribe una respuesta corta a una música que escuches o a «Tormenta lejana» (tambor grave y suave que crece, platillos agudos y baja al final). Revísala con los cuatro criterios de la clase. Agrega lo que falte, incluyendo un segundo medio (por ejemplo, un dibujo de una línea). Escribe cuántos criterios cumplía al principio y cuántos al final.",
        "Primera versión: «Sentí miedo.» (1 criterio). Final: «Sentí miedo porque el tambor sonaba grave y cada vez más fuerte, sobre todo en el medio; lo dibujé con una línea gruesa que sube.» (4 criterios).",
        ["revisa con los cuatro criterios", "agrega solo lo que falta", "el segundo medio es coherente con la respuesta"],
        ["dos versiones escritas", "dibujo", "conteo de criterios"],
        ["cambiar toda la respuesta en lugar de agregar", "un dibujo que contradice la emoción"],
        "Reconoce el avance y pide mostrar en el dibujo el momento que se menciona en la frase.",
    ),
    "Lee tu respuesta de nivel 2 de la primera clase y agrégale una razón sonora.",
    "Escucha otra música y escribe una respuesta que cumpla los cuatro criterios.",
)
