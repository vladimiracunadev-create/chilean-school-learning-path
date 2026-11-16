"""Danza 3.º y 4.º medio FG: OAC-02 (comunicar ideas, sensaciones y emociones con el movimiento), clases 1 a 4. Fichas inventadas; sin video real."""
from __future__ import annotations

from fg_danz_common import build

O2 = "FG-DANZ-3y4-OAC-02"

# ============================================================ OAC-02, clase 1
F = ("Ficha 1 (palabra-estímulo de ejemplo: «viento»). "
     "Sensaciones que sugiere: ligero, constante, que empuja. "
     "Imágenes: hojas que se arremolinan, una cortina que ondula. "
     "Acciones posibles: ondular un brazo, girar suavemente sobre los dos pies, inclinar el torso hacia un lado y volver.")
build(
    O2, 1, F,
    use="Aprenderé a partir de una palabra, una imagen o una sensación para encontrar movimientos que la comuniquen, y a distinguir entre imitar literalmente y transformar la idea en danza.",
    prior=["Reconozco espacio, tiempo y energía.", "Sé componer una frase breve.", "Sé describir movimientos sin juzgar los cuerpos."],
    explain=[
        "Para comunicar algo con el movimiento se parte de un estímulo: una palabra, una imagen, un objeto, una emoción o un tema. Una sensación es lo que se percibe con el cuerpo (ligero, pesado, tibio). Una emoción es un estado afectivo (alegría, miedo, calma). Una idea o tema es el asunto del que trata la danza (la ciudad, la espera, el agua). Distinguirlos ayuda a elegir qué movimientos explorar.",
        "Hay dos caminos para traducir un estímulo. La imitación literal copia la acción tal como es (mover los brazos como si se barriera). La abstracción toma una cualidad del estímulo (lo suave, lo constante, lo que empuja) y la transforma en movimiento con espacio, tiempo y energía (un brazo que ondula lento y continuo). La danza usa mucho la abstracción, porque no necesita ilustrar una acción para sugerir una sensación.",
        "Un buen método es anotar sensaciones, imágenes y acciones, elegir una cualidad y probar tres versiones con distinta combinación de elementos. Se trabaja en la zona propia, sin tocar a otras personas, sin saltos ni caídas. Si el estímulo evoca algo difícil de tu vida personal, elige otro: nadie tiene que contar ni mostrar vivencias privadas.",
    ],
    vocab=[("imagen", "algo que se representa en la mente, como una cortina que ondula"), ("estímulo", "punto de partida de la exploración: palabra, imagen, tema"), ("sensación", "lo que se percibe con el cuerpo"), ("emoción", "estado afectivo como alegría, miedo o calma"), ("tema", "asunto del que trata la danza"), ("imitación literal", "copiar la acción tal como es"), ("abstracción", "tomar una cualidad de una idea y transformarla en movimiento")],
    worked=[
        ("Imitación o abstracción", "Un grupo propone «agitar las manos como las hojas». Otro propone «hacer un brazo que ondula lento y continuo para sugerir el empuje del viento». ¿Cuál es abstracción?", ["La primera copia el movimiento de la hoja tal cual: imitación literal.", "La segunda toma la cualidad (continuo, empujado) y la convierte en movimiento: abstracción."], "La segunda propuesta es abstracción"),
        ("Elegir la cualidad", "De la ficha, elige una cualidad y propón un movimiento seguro que la exprese.", ["Cualidad: ligero. Movimiento: caminar en puntillas despacio, con los brazos a media altura.", "Se describen nivel (medio), tiempo (lento) y energía (suave)."], "Cualidad ligera: caminar lento en puntillas, brazos a media altura, energía suave"),
    ],
    mistakes=[("Hacer mímica de la acción (por ejemplo, simular soplar) y llamarla danza del viento.", "La mímica copia la acción y no usa los elementos del lenguaje para transformarla.", "Elige una cualidad del viento y exprésala con espacio, tiempo y energía."),
              ("Contar una experiencia personal difícil para «ser más expresivo».", "Nadie debe exponer vivencias privadas para cumplir una tarea de danza.", "Usa un tema ficticio o neutro y, si algo te afecta, avisa a una persona adulta de confianza.")],
    T=[
        ('abc', '¿Qué es una emoción?', 'Un estado afectivo, como alegría, miedo o calma', 'Lo que se percibe en la piel, como el frío', 'El asunto del que trata una obra', 'La emoción es un estado afectivo; lo que se percibe con el cuerpo es una sensación y el asunto es el tema.'),
        ('abc', '{F} ¿Qué elemento de la ficha es una imagen?', 'Una cortina que ondula', 'Constante', 'Inclinar el torso', 'Una imagen es algo que se representa en la mente; «constante» es una sensación y inclinar el torso es una acción.'),
        ('abc', '{F} «Ligero» es', 'una sensación', 'una acción', 'un tema', 'Ligero describe cómo se percibe el viento, es una sensación; las acciones son movimientos concretos.'),
        ('abc', '¿Qué es la abstracción en danza?', 'Tomar una cualidad de una idea y transformarla en movimiento con los elementos del lenguaje de la danza', 'Hacer movimientos sin ningún sentido para que cada persona del público vea lo que quiera', 'Copiar con la mayor exactitud posible una acción cotidiana, como barrer o nadar', 'La abstracción conserva una cualidad de la idea y la traduce al lenguaje de la danza; no es hacer algo sin sentido.'),
        ('abc', 'Un grupo representa el mar moviendo los brazos como si nadara. Eso es', 'imitación literal, porque copia una acción tal cual', 'abstracción, porque usa los brazos y el movimiento es distinto del real', 'composición, porque usa el cuerpo', 'Nadar simula la acción exactamente, así que es imitación; la abstracción toma una cualidad del mar.'),
        ('abc', 'Para pasar de «lluvia» a movimiento, ¿qué cualidad se podría tomar?', 'Lo repetido y liviano de las gotas', 'La acción de abrir un paraguas, copiada tal cual', 'El color gris del cielo, sin transformarlo', 'Se pasa de lo que es la lluvia a una cualidad que puede traducirse a tiempo y energía.'),
        ('abc', '{F} Quieres explorar «empujar» con seguridad. ¿Qué haces?', 'Inclinas el torso lento hacia un lado como si algo te empujara, sin contacto con otra persona', 'Pides a un compañero que te empuje de verdad por la espalda para sentir el empuje de forma real', 'Corres contra un compañero para sentir el empuje', 'Se explora la sensación sin contacto físico riesgoso.'),
        ('abc', '{F} Un estudiante propone «imitar a un barrendero». Quien dirige pregunta cómo hacerlo abstracto. ¿Qué respuesta sirve?', 'Tomar lo repetitivo del barrer y expresarlo en un movimiento continuo de brazo con trayectoria curva', 'Hacerlo más grande y con más fuerza para que el barrido se note desde lejos', 'Barrer más rápido y con movimientos más amplios para que se vea más intenso', 'Se toma la cualidad repetitiva y se transforma; agrandar o acelerar sigue siendo imitación.'),
        ('abc', 'Una compañera quiere representar una pérdida personal muy dolorosa para su danza. ¿Qué corresponde?', 'Elegir otro tema o uno ficticio y conversar con una persona adulta de confianza', 'Contarlo en detalle frente al curso para que el público entienda de dónde viene la danza', 'Insistir con ese tema porque es el más expresivo y así la danza será más sincera', 'Nadie debe exponer vivencias dolorosas; se cambia el tema y se avisa a una persona adulta.'),
        ('=', '{F} Un grupo prueba 3 acciones de la ficha, cada una en 2 versiones de 8 tiempos. ¿Cuántos tiempos suman todas las versiones?', '3*2*8', 'Son 3 acciones por 2 versiones por 8 tiempos cada una.', ' tiempos'),
        ('abc', 'Dos versiones de «ligero»: la primera camina rápido y golpeando el suelo; la segunda camina lento en puntillas. ¿Cuál comunica mejor la sensación?', 'La segunda, porque lento y suave se asocian a lo ligero', 'La primera, porque se escucha más y así se nota el esfuerzo', 'Ninguna, porque ligero no se puede mostrar', 'Los golpes suenan pesados; lentitud y suavidad apoyan lo ligero.'),
        ('abc', 'Quieres comprobar si tu movimiento «ligero» funciona. ¿Qué haces?', 'Lo muestras a una compañera y le preguntas qué sensación observa, sin decirle antes cuál es', 'Le explicas el significado antes de que lo vea para que lo entienda mejor', 'Le preguntas si le gustó el movimiento y si lo encontró bonito', 'Preguntar la sensación sin adelantar el significado muestra si se comunica.'),
        ('=', 'Un curso de 36 estudiantes forma grupos de 4 y cada grupo muestra su exploración de «viento» en 1 minuto. ¿Cuántos minutos tarda en mostrarse todo?', '36//4*1', 'Se calcula la cantidad de grupos y se multiplica por el minuto de cada uno.', ' minutos'),
    ],
    ctx=('abc', 'Un grupo recibe el estímulo «puente». Propone: (1) cruzar el espacio caminando como si hubiera un puente; (2) dos filas que se acercan con pasos lentos y se encuentran a media altura, uniendo las manos en el aire sin tocarse. ¿Qué propuesta usa abstracción?', 'La propuesta 2, porque convierte la idea de unir dos lados en una trayectoria y un nivel', 'La propuesta 1, porque recorre el espacio y eso muestra la idea de un puente', 'Las dos, porque ambas usan el cuerpo para mostrar el puente', 'La propuesta 2 traduce la idea de unir en direcciones y niveles; la 1 representa la acción de cruzar.'),
    sc=[
        ("En Danza: ¿qué es la abstracción?", "Tomar una cualidad de una idea y transformarla en movimiento", "No se copia la acción, se traduce una cualidad."),
        ("¿Qué se hace si un tema evoca una vivencia dolorosa?", "Elegir otro tema y avisar a una persona adulta de confianza", "No hay que exponer experiencias privadas."),
        ("Una cortina que ondula, ¿es sensación, imagen o tema?", "Imagen", "Es algo que se representa en la mente."),
    ],
    op=("Elige un estímulo (viento, agua, puente u otro). Escribe tres sensaciones y tres imágenes. Elige una cualidad y describe un movimiento seguro de 8 tiempos que la exprese, indicando nivel, velocidad y energía. Di si es imitación o abstracción.",
        "Estímulo: agua. Sensaciones: fluido, fresco, continuo. Imágenes: río, olas, gotas. Cualidad: fluido. Movimiento: ondular el torso y los brazos lento, en nivel medio, energía suave y continua durante 8 tiempos. Es abstracción.",
        ["distingue sensación e imagen", "traduce una cualidad a espacio, tiempo y energía", "clasifica correctamente imitación o abstracción"],
        ["hoja con listas y movimiento"],
        ["copiar la acción literalmente", "mezclar sensación e imagen", "usar una vivencia personal difícil"],
        "Pregunta: «¿qué cualidad del estímulo estás mostrando?». Si responde con la acción, pídele una cualidad."),
    reinforce="Escribe una palabra-estímulo, tres sensaciones y un movimiento seguro de 8 tiempos que exprese una de ellas.",
    extend="Explica con un ejemplo inventado la diferencia entre imitar una acción y expresar su cualidad.",
)

# ============================================================ OAC-02, clase 2
F = ("Ficha 2 (tabla de ejemplo, inventada; no son reglas fijas). "
     "Inquietud: direcciones que cambian, tiempo irregular, energía cortada, nivel medio. "
     "Alivio: nivel que sube, tiempo lento, energía suave y continua, dirección hacia arriba. "
     "Alegría tranquila: trayectorias curvas, tiempo medio y parejo, energía suave, nivel medio.")
build(
    O2, 2, F,
    use="Aprenderé a vincular emociones e ideas con decisiones de espacio, tiempo y energía, a verificar que sean coherentes entre sí y a entender que no hay una única forma correcta de expresar una emoción.",
    prior=["Distingo imitación y abstracción.", "Reconozco nivel, dirección, velocidad y energía.", "Sé que una variable cambia el efecto."],
    explain=[
        "Los elementos de la danza no tienen significados fijos, pero algunas combinaciones se asocian con frecuencia a ciertas emociones. Movimientos lentos, suaves y que ascienden suelen leerse como calma o alivio. Movimientos cortados, con direcciones que cambian, suelen leerse como inquietud. Son asociaciones culturales y personales, así que sirven como punto de partida para probar, no como reglas.",
        "Para vincular una emoción con el movimiento se eligen decisiones en espacio, tiempo y energía y se revisa su coherencia: todas deben apuntar en el mismo sentido o contrastar con una razón. Si quiero mostrar alivio y uso energía cortada y direcciones que cambian, el resultado transmite inquietud; hay incoherencia entre la intención y las decisiones. Un contraste puede ser intencional, por ejemplo una pausa quieta después de movimientos inquietos para mostrar alivio.",
        "Comprobar la comunicación implica preguntar a quien observa qué percibió y por qué, y comparar con la intención. Si la lectura es distinta, no es un fracaso: sirve para decidir qué elemento cambiar. En todo ejercicio se trabaja en la zona propia, sin contacto y sin forzar el cuerpo ni la expresión.",
    ],
    vocab=[("coherencia", "acuerdo entre la intención y las decisiones de movimiento"), ("asociación", "relación frecuente, no obligatoria, entre un movimiento y una emoción"), ("contraste intencional", "diferencia buscada para destacar una idea"), ("lectura", "lo que percibe quien observa"), ("intención", "lo que quien baila quiere comunicar")],
    worked=[
        ("Revisar coherencia", "Una estudiante quiere mostrar «alivio» con direcciones que cambian y energía cortada. ¿Qué observas?", ["Esas decisiones se asocian a inquietud en la ficha, no a alivio.", "Hay incoherencia: conviene pasar a nivel ascendente, tiempo lento y energía suave."], "Hay incoherencia; el alivio se apoya mejor en nivel ascendente, lentitud y suavidad"),
        ("Usar un contraste", "Una frase de 16 tiempos muestra inquietud en los primeros 12 y queda quieta en los últimos 4. ¿Qué puede comunicar?", ["Los primeros tiempos usan decisiones de inquietud.", "La pausa final contrasta y puede leerse como alivio o cansancio."], "La pausa final contrasta y sugiere alivio"),
    ],
    mistakes=[("Pensar que hay un movimiento «correcto» para cada emoción.", "Las asociaciones son culturales y personales, no reglas.", "Prueba varias versiones y pregunta qué leen quienes observan."),
              ("Cambiar tres elementos para «mostrar más» una emoción sin comprobar la coherencia.", "Con varios cambios no se sabe qué produjo el efecto ni si hay contradicción.", "Cambia uno por vez y revisa que todos apunten a la misma intención.")],
    T=[
        ('abc', '{F} ¿Qué decisiones de la ficha se asocian a inquietud?', 'Direcciones que cambian, tiempo irregular y energía cortada', 'Nivel que sube, tiempo lento y energía suave', 'Trayectorias curvas, tiempo medio y parejo', 'La primera lista es la de inquietud; las otras describen alivio y alegría tranquila.'),
        ('abc', '¿Qué significa coherencia en una frase de danza?', 'Que las decisiones de movimiento apoyan la intención', 'Que todos los movimientos sean iguales', 'Que la frase dure lo mismo que la música', 'Hay coherencia cuando espacio, tiempo y energía apuntan a lo que se quiere comunicar.'),
        ('abc', 'Las asociaciones entre movimiento y emoción son', 'frecuentes pero no obligatorias', 'reglas que nunca cambian', 'iguales para todas las culturas', 'Dependen de la cultura y de las personas; sirven como punto de partida.'),
        ('abc', '{F} ¿Qué frase se aproxima más a «alivio»?', 'Un brazo que sube lento, con energía suave y continua', 'Pasos cortados que cambian de dirección sin avisar', 'Giros rápidos con golpes al suelo', 'La ficha asocia alivio a nivel ascendente, lentitud y suavidad.'),
        ('abc', 'Una compañera quiere mostrar tristeza con pasos fuertes y rápidos. ¿Qué le dirías?', 'Que revise si esas decisiones se leen como tristeza o más bien como tensión', 'Que la tristeza se muestra siempre con pasos fuertes y rápidos y que no hay que revisar nada', 'Que la danza no puede mostrar tristeza porque solo expresa alegría y fuerza', 'Se invita a revisar la coherencia sin imponer una regla; se invita a probar y preguntar.'),
        ('abc', '{F} ¿Qué es un contraste intencional?', 'Una pausa quieta tras movimientos inquietos para destacar el alivio', 'Cambiar de dirección por descuido, porque el contraste ocurre cuando alguien se equivoca', 'Repetir todo igual para que el contraste no confunda al público', 'Es una diferencia buscada para destacar una idea.'),
        ('=', '{F} Una frase de alegría tranquila tiene 5 conteos de 8 tiempos. Los dos últimos conteos repiten el motivo del primero. ¿Cuántos tiempos son repetición?', '2*8', 'Cada conteo tiene 8 tiempos y son dos conteos de repetición.', ' tiempos'),
        ('abc', 'Una estudiante muestra su frase y dos compañeros leen «calma» y uno lee «tristeza». ¿Qué conclusión es sensata?', 'La lectura varía; conviene preguntar qué rasgos vieron y decidir qué ajustar según su intención', 'La frase está mal hecha porque no se entiende lo mismo en las tres lecturas', 'Hay que repetir la frase muchas veces hasta que los tres lean exactamente lo mismo y no queden dudas', 'La lectura de varias personas es información para decidir; no hay una única respuesta correcta.'),
        ('abc', '{F} Quieres pasar de inquietud a alivio en una misma frase. ¿Qué cambia primero?', 'La energía, de cortada a suave, y el tiempo, de irregular a lento', 'El nivel, de alto a bajo, y la dirección, que cambia cada vez más seguido', 'La energía, de cortada a más cortada, y el tiempo, de lento a rápido', 'La ficha asocia la inquietud con energía cortada y tiempo irregular, y el alivio con suavidad y lentitud.'),
        ('abc', 'Para comprobar si una frase comunica «alegría tranquila», ¿cuál es la mejor pregunta a quien observa?', '«¿Qué sensación te dio y qué viste que te la sugirió?»', '«¿Te gustó mi baile y se notó cuánto me esforcé?»', '«¿Notaste cuánto me esforcé y qué tan perfecta me salió la frase?»', 'Pide la lectura y la evidencia observable.'),
        ('abc', 'Una frase de inquietud termina con 4 tiempos de quietud y respiración. ¿Qué puede comunicar el final?', 'Un posible alivio, por el contraste con lo anterior', 'Que el grupo olvidó la coreografía y se quedó quieto sin saber qué hacer', 'Que la frase no tiene intención, porque terminó sin movimiento', 'La pausa tras movimiento inquieto es un contraste que puede sugerir alivio.'),
        ('=', 'Para probar una emoción, un grupo hace 4 versiones de 8 tiempos y luego comenta 15 segundos cada una. Cada tiempo dura 2 segundos. ¿Cuántos segundos dura todo?', '4*(8*2+15)', 'Cada versión dura 16 segundos más 15 de comentario, y son 4.', ' segundos'),
        ('abc', 'Un grupo quiere mostrar «miedo» sin contacto ni caídas. ¿Qué propuesta es segura?', 'Retroceder dos pasos pequeños, encoger los brazos cerca del pecho y mirar rápido a los lados', 'Empujar a un compañero hacia atrás para mostrar de manera realista cómo se huye', 'Dejarse caer al suelo de golpe, porque así se nota que hay miedo de verdad', 'Los pasos cortos y los brazos recogidos comunican miedo sin riesgo físico.'),
    ],
    ctx=('abc', 'Un grupo quiere mostrar «esperanza» con una frase de 16 tiempos. Probaron A) pasos cortados, dirección cambiante, nivel bajo; B) nivel que sube, tiempo lento, energía suave. ¿Cuál es más coherente y qué conviene hacer?', 'B es más coherente; conviene preguntar a quien observe si leyó esperanza y por qué', 'A es más coherente por tener más cambios, porque la esperanza es una emoción inquieta', 'Ambas son iguales, así que no hay que decidir ni preguntarle a nadie más', 'B reúne decisiones que apuntan en el mismo sentido; validar con la lectura de otros afina la elección.'),
    sc=[
        ("En Danza: ¿qué es la coherencia?", "Que las decisiones apoyan la intención", "Todas las decisiones van en el mismo sentido."),
        ("¿Las asociaciones entre movimiento y emoción son reglas?", "No, son asociaciones que sirven de punto de partida", "Cambian con la cultura y las personas."),
        ("¿Qué se hace si la lectura de quien observa difiere de tu intención?", "Preguntar qué rasgos vio y ajustar un elemento", "La diferencia entre lecturas orienta qué elemento conviene cambiar."),
    ],
    op=("Elige una emoción (calma, inquietud, esperanza u otra). Describe una frase de 8 tiempos con decisiones de espacio, tiempo y energía. Revisa su coherencia y escribe una pregunta que harías a quien la observe.",
        "Emoción: esperanza. Frase: nivel que sube de bajo a alto en 8 tiempos, brazos que se abren lento, energía suave y continua. Coherente: todo asciende y es suave. Pregunta: «¿qué sensación te dio y qué viste que la sugirió?»",
        ["relaciona la emoción con decisiones", "revisa la coherencia", "formula una pregunta que pide evidencia"],
        ["hoja con frase, revisión y pregunta"],
        ["afirmar que existe una única forma correcta", "no revisar la coherencia"],
        "Pregunta: «¿qué decisión apunta a la emoción?». Si responde «todo», pídele una decisión concreta."),
    reinforce="Describe dos versiones de 8 tiempos para «alegría tranquila» y anota cuál crees que se lee mejor y por qué.",
    extend="Explica con un ejemplo inventado un contraste intencional que cambie el sentido de una frase.",
)

# ============================================================ OAC-02, clase 3
F = ("Ficha 3 (mapa de ideas de ejemplo, inventado). Tema: «la ciudad en hora punta». "
     "Imágenes: personas que se cruzan, semáforos que cambian, ruido que se acumula. "
     "Motivos de movimiento: caminar con prisa cruzando trayectorias; detenerse de golpe y mirar a un lado; pasar entre otros sin tocarse. "
     "Estructura propuesta de 4 conteos: 1 y 2 motivo de prisa, 3 detención, 4 retomar la marcha más lento.")
build(
    O2, 3, F,
    use="Aprenderé a convertir un tema en una frase o pieza breve usando un mapa de ideas, motivos de movimiento y una estructura, y a revisar si la propuesta comunica el tema.",
    prior=["Distingo sensación, emoción y tema.", "Sé hacer repetición, variación y contraste.", "Conozco espacio, tiempo y energía."],
    explain=[
        "Un tema es el asunto del que trata una danza. Un mapa de ideas ordena el trabajo: en el centro el tema, a su alrededor imágenes y sensaciones, y luego los motivos de movimiento que se derivan de ellas. Un motivo debe poder describirse con acciones y elementos concretos: caminar con prisa cruzando trayectorias, nivel medio, energía cortada.",
        "Para componer a partir de un tema se eligen pocos motivos, se decide su orden y se usan recursos como repetición, variación y contraste. La estructura da forma a la idea: por ejemplo, 2 conteos de un motivo, 1 conteo de contraste (una detención) y 1 de cierre. Es mejor desarrollar pocos motivos con claridad que mostrar muchos sin relación.",
        "Se revisa si la propuesta comunica el tema pidiendo a otra persona que describa lo que vio. Para seguridad, las trayectorias que se cruzan en el espacio se ensayan despacio, con distancias claras y sin contacto, y se acuerda quién pasa primero. Se usan temas neutros o ficticios, sin exponer vivencias personales.",
    ],
    vocab=[("mapa de ideas", "esquema que ordena tema, imágenes y motivos"), ("motivo", "idea de movimiento que se puede describir y repetir"), ("estructura", "orden en que se presentan los motivos"), ("trayectoria cruzada", "caminos de dos o más personas que se atraviesan sin tocarse"), ("selección", "elegir pocos motivos y desarrollarlos")],
    worked=[
        ("Pasar de imagen a motivo", "De la imagen «semáforos que cambian», propón un motivo.", ["Rasgo: cambios bruscos entre moverse y detenerse.", "Motivo: caminar 4 tiempos y detenerse 4, en nivel medio y energía cortada."], "Caminar 4 tiempos y detenerse 4 en energía cortada"),
        ("Contar la estructura", "La estructura de la ficha tiene 4 conteos de 8 tiempos. ¿Cuántos tiempos dura y cuántos son de prisa?", ["Total: 4 × 8 = 32 tiempos.", "Prisa: conteos 1 y 2, o sea 2 × 8 = 16 tiempos."], "32 tiempos en total; 16 de prisa"),
    ],
    mistakes=[("Incluir todos los motivos del mapa en una frase corta.", "Se pierde claridad y nada se desarrolla.", "Elige dos o tres motivos y trabaja repetición, variación y contraste."),
              ("Cruzar trayectorias a toda velocidad para que «se note la ciudad».", "Aumenta el riesgo de choques.", "Ensaya despacio, con distancias claras, y acuerda quién pasa primero.")],
    T=[
        ('abc', '¿Qué es un mapa de ideas en composición?', 'Un esquema que ordena tema, imágenes y motivos', 'Un plano del teatro con las filas de butacas y las salidas de emergencia', 'La lista de personas que participan', 'Un mapa de ideas conecta el tema con imágenes y motivos que se van a mover.'),
        ('abc', '{F} ¿Cuál es el tema?', 'La ciudad en hora punta', 'Pasar entre otros sin tocarse', 'Caminar con prisa', 'El tema es el asunto general; los otros son motivos.'),
        ('abc', '{F} «Detenerse de golpe y mirar a un lado» es', 'un motivo de movimiento', 'un tema', 'una estructura completa', 'Se puede describir y repetir, así que es un motivo.'),
        ('=', '{F} La estructura tiene 4 conteos de 8 tiempos. ¿Cuántos tiempos no son de prisa?', '4*8-2*8', 'Se resta del total los 16 tiempos de prisa (conteos 1 y 2).', ' tiempos'),
        ('abc', '¿Cuál es una ventaja de elegir pocos motivos?', 'Se pueden desarrollar con claridad usando repetición y variación', 'La frase resulta más corta que cualquier otra', 'Se evita ensayar mucho, porque con pocos motivos la frase ya está lista', 'Pocos motivos bien desarrollados se entienden mejor.'),
        ('abc', '{F} En la estructura propuesta, ¿qué conteo funciona como contraste?', 'El 3, la detención', 'El 1, el primer motivo de prisa', 'El 2, la repetición de la prisa', 'La detención contrasta con el movimiento anterior.'),
        ('abc', '{F} Quieres variar el motivo «caminar con prisa cruzando trayectorias» en el conteo 2. ¿Qué cambio es una variación?', 'Hacerlo en nivel bajo con rodillas flexionadas', 'Hacerlo exactamente igual, con el mismo nivel, la misma velocidad y la misma energía', 'Quitar el conteo y dejar solo el primero para que quede más ordenado', 'La variación cambia un elemento (nivel).'),
        ('abc', 'Dos personas cruzarán trayectorias en el ensayo. ¿Qué medida de seguridad es adecuada?', 'Ensayar despacio, acordar quién pasa primero y mantener distancia', 'Cruzarse a la mayor velocidad posible, para que se note que es una ciudad apurada', 'Tomarse de las manos para guiarse y no chocar al cruzar trayectorias', 'La seguridad pide lentitud, acuerdos y distancia, sin contacto.'),
        ('abc', 'Un grupo tiene seis motivos y solo 16 tiempos. ¿Qué decisión es más acertada?', 'Elegir dos o tres y desarrollarlos con repetición, variación y contraste', 'Meter los seis motivos, cada uno una sola vez y en el orden en que se propusieron', 'Alargar la frase hasta 100 tiempos para que quepan todos los motivos', 'Seleccionar permite desarrollar; mostrar todo una vez no construye una idea.'),
        ('abc', 'Quien observa describe: «veo mucha gente apurada que de pronto se detiene». ¿Qué indica sobre el tema?', 'Que la propuesta comunica la idea de hora punta, aunque no use esas palabras', 'Que el tema no se entiende porque nadie nombra la ciudad en su descripción', 'Que la frase está mal hecha porque la gente apurada no se parece a una danza', 'La descripción coincide con la intención.'),
        ('abc', 'Una compañera quiere un tema basado en una situación muy personal. ¿Qué es lo mejor?', 'Elegir un tema ficticio o neutro y avisar a una persona adulta si algo le afecta', 'Contarla completa al curso para que el público entienda de dónde viene la danza', 'Obligarla a usarla porque «es expresiva» y así la danza tendría más verdad', 'No se debe exigir exponer lo privado.'),
        ('=', 'Un curso de 30 personas forma grupos de 5. Cada grupo muestra 2 minutos y hay 1 minuto de comentarios entre grupos (solo entre uno y otro). ¿Cuántos minutos dura la ronda?', '30//5*2+(30//5-1)*1', 'Son 6 grupos de 2 minutos, más 5 pausas de 1 minuto.', ' minutos'),
        ('abc', 'Un grupo repite el motivo de prisa cuatro veces igual y dice que «ya desarrolló el tema». ¿Qué falta?', 'Variación o contraste que muestren cómo evoluciona la idea', 'Más repeticiones del mismo motivo, hasta que el público lo reconozca bien', 'Otro título más claro, que explique el tema antes de empezar', 'Con repetición sola no hay desarrollo.'),
    ],
    ctx=('abc', 'Tema ficticio: «el mercado por la mañana». Imágenes: puestos que se arman, voces que se mezclan, gente que se mueve entre cajones. Un grupo debe armar 4 conteos. ¿Qué propuesta tiene estructura clara?', 'Conteo 1 armar puestos, 2 repetirlo variado, 3 cruce de trayectorias lento, 4 pausa y cierre', 'Los cuatro conteos iguales, sin cambio, para que el público reconozca el tema', 'Cada conteo con un motivo distinto y sin relación entre sí, para mostrar mucha variedad', 'Combina repetición, variación, contraste y cierre alrededor del mismo tema.'),
    sc=[
        ("En Danza: ¿qué es un motivo?", "Una idea de movimiento que se puede describir y repetir", "Se puede trabajar con repetición y variación."),
        ("¿Cuántos tiempos tienen 4 conteos de 8 tiempos?", "32", "4 por 8 da 32 tiempos."),
        ("¿Qué se acuerda antes de cruzar trayectorias en un ensayo?", "Quién pasa primero y la distancia, ensayando despacio", "Evita choques sin necesidad de contacto."),
    ],
    op=("Elige un tema ficticio o neutro. Escribe un mapa con tres imágenes y dos motivos de movimiento. Propón una estructura de 4 conteos con repetición, variación y cierre, y cuenta cuántos tiempos dura.",
        "Tema: la biblioteca. Imágenes: páginas que pasan, silencio, pasos suaves. Motivos: pasar la mano en el aire lento (páginas) y caminar de puntillas. Estructura: 1 páginas, 2 repetición, 3 puntillas con cambio de dirección, 4 pausa y cierre. Duración: 32 tiempos.",
        ["tema con imágenes y motivos", "estructura con repetición, variación y cierre", "cuenta correcta de tiempos"],
        ["hoja con mapa y estructura"],
        ["incluir demasiados motivos", "no incluir cierre", "elegir un tema personal doloroso"],
        "Pregunta: «¿qué motivo se repite y cuál varía?». Si no puede, pídele reescribir la estructura."),
    reinforce="Escribe un tema, tres imágenes y dos motivos. Compón en papel una estructura de 4 conteos.",
    extend="Explica por qué mostrar menos motivos puede comunicar un tema con más claridad.",
)

# ============================================================ OAC-02, clase 4
F = ("Ficha 4 (comentarios de ejemplo, inventados, después de que un grupo mostró una frase con el tema «espera»). "
     "Comentario 1: «Me dio la sensación de cansancio porque los pasos eran lentos y los brazos caían». "
     "Comentario 2: «Me gustó mucho». "
     "Comentario 3: «Me pareció alegre, porque se movían con soltura». "
     "Comentario 4: «Vi que la mirada iba siempre al suelo, y eso me hizo pensar en tristeza».")
build(
    O2, 4, F,
    use="Aprenderé a comunicar con intención ante un público: usar mirada, respiración, foco y energía de manera coherente, comprobar con comentarios qué se entendió y recibir lecturas distintas con respeto.",
    prior=["Sé vincular emoción con espacio, tiempo y energía.", "Sé componer a partir de un tema.", "Sé describir lo observado."],
    explain=[
        "Comunicar con el movimiento no depende solo de los pasos: la mirada, el foco (hacia dónde se dirige la atención del cuerpo y de los ojos), la respiración y la presencia (estar atento y con intención) cambian lo que se percibe. Una misma frase con la mirada al suelo se lee diferente a la misma frase con la mirada al frente.",
        "Para saber qué se comunicó, se piden lecturas a quienes observan. Un comentario útil dice qué sintió o pensó la persona y qué vio que se lo sugirió (en la ficha, los comentarios 1 y 4). Un comentario como «me gustó mucho» es amable pero no ayuda a decidir qué mantener o cambiar. Las lecturas pueden diferir de la intención; se las analiza sin discutir con quien las dio.",
        "Quien presenta puede elegir hacerlo en grupo pequeño o con ensayo privado previo; nadie debe ser forzado a exponerse. Se evita la comparación de cuerpos y se respeta el rango de cada persona. Si una presentación genera incomodidad, se detiene y se avisa a una persona adulta.",
    ],
    vocab=[("foco", "hacia dónde se dirige la atención del cuerpo y la mirada"), ("presencia", "estar atento y con intención al bailar"), ("lectura", "lo que percibe quien observa"), ("comentario descriptivo", "dice qué se vio y qué sugirió"), ("intención", "lo que quien baila quiere comunicar")],
    worked=[
        ("Distinguir un comentario útil", "De la ficha, ¿qué comentarios dicen qué se vio y qué sugirió?", ["El 1 dice pasos lentos y brazos que caen, que sugirieron cansancio.", "El 4 dice mirada al suelo, que sugirió tristeza."], "Los comentarios 1 y 4"),
        ("Interpretar una lectura distinta", "El grupo quería mostrar espera y el comentario 4 leyó tristeza. ¿Qué hace el grupo?", ["Revisa qué rasgo causó esa lectura (la mirada al suelo).", "Decide si cambia el foco (mirar al frente o arriba) para acercar la lectura a su intención."], "Revisar la mirada y decidir si cambia el foco"),
    ],
    mistakes=[("Responder a un comentario diciendo «no, eso no es lo que quise mostrar».", "La lectura de otra persona es información, no un error.", "Pregunta qué vio y úsalo para decidir qué ajustar."),
              ("Dar solo comentarios como «me gustó» o «no me gustó».", "No dicen qué se vio ni qué sugirió.", "Di qué rasgo viste y qué te hizo pensar o sentir.")],
    T=[
        ('abc', '¿Qué es el foco en danza?', 'Hacia dónde se dirigen la atención del cuerpo y la mirada', 'El lugar donde se cuelga la luz principal para iluminar a quien baila', 'La parte del cuerpo que más trabaja en cada movimiento de la frase', 'El foco es la dirección de la atención y la mirada.'),
        ('abc', '{F} ¿Qué comentario es más útil?', 'El 1, porque dice qué se vio y qué sugirió', 'El 2, porque es amable y deja contento al grupo que presentó', 'Ninguno, porque todos son opiniones y las opiniones no sirven para mejorar', 'El 1 vincula rasgos observables con una sensación.'),
        ('abc', '{F} ¿Qué rasgo mencionó el comentario 4?', 'La mirada hacia el suelo', 'La velocidad de los pasos', 'La caída de brazos', 'El comentario 4 habla de la mirada al suelo.'),
        ('abc', '{F} El grupo quería mostrar espera. ¿Qué ajuste podría acercar la lectura a su intención?', 'Cambiar el foco a la mirada al frente o hacia arriba', 'Repetir el mismo foco con más fuerza para que la lectura cambie sola', 'Pedir que no se hagan comentarios en la próxima presentación para evitar lecturas distintas', 'El foco ayuda a cambiar la lectura de tristeza a espera.'),
        ('abc', 'La presencia en escena significa', 'estar atento y con intención mientras se baila', 'ubicarse siempre al centro del espacio para que todas las personas lo vean', 'hacer movimientos más grandes que los de las demás personas', 'Es una actitud de atención, no una ubicación.'),
        ('abc', 'Una estudiante respira de forma suave antes de comenzar y mantiene la mirada al frente. ¿Qué logra?', 'Mayor claridad y calma para comunicar su intención', 'Que su frase se vea más rápida y enérgica', 'Que sus movimientos queden más grandes sin esfuerzo', 'Respiración y foco ayudan a estar presente.'),
        ('abc', '{F} El comentario 3 dice «alegre, porque se movían con soltura». ¿Qué conviene hacer?', 'Preguntar qué rasgos vio y analizar si coincide con la intención', 'Ignorarlo porque no coincide con el tema de espera que quería mostrar el grupo', 'Corregirle diciendo que está equivocado, porque el grupo sabe cuál es la lectura correcta', 'Una lectura distinta se analiza sin discutir.'),
        ('=', '{F} El grupo presenta 3 veces su frase de 32 tiempos, y cada tiempo dura 2 segundos. Después pide 4 comentarios de 20 segundos. ¿Cuántos segundos pasan en total?', '3*32*2+4*20', 'Se suman las tres presentaciones y los cuatro comentarios.', ' segundos'),
        ('abc', 'Alguien no quiere presentar delante de todo el curso. ¿Cuál es la opción adecuada?', 'Presentar en grupo pequeño o ensayar en privado y entregar una descripción', 'Obligarlo a presentar ante todo el curso para que supere su timidez', 'Quitarle la nota por no presentarse frente a todas las personas', 'La exposición no se fuerza; se evalúa con otras evidencias.'),
        ('abc', 'Un comentario dice «tu cuerpo no se ve como el de una bailarina». ¿Qué corresponde?', 'Responder que los comentarios hablan del movimiento y no del cuerpo, y avisar a la persona docente', 'Aceptarlo como una crítica válida y pedirle a la persona que cambie su cuerpo', 'Contestar con otra burla para que se den cuenta de lo que se siente', 'Se comenta el movimiento, nunca el cuerpo de la persona.'),
        ('abc', 'Dos personas leen cosas distintas de una misma frase. ¿Qué conclusión es la más razonable?', 'Que la lectura depende de quien observa y sirve para decidir qué ajustar', 'Que una de las dos se equivoca y hay que averiguar cuál es la correcta', 'Que la frase no tiene sentido porque cada persona ve algo distinto', 'Las lecturas varían y aportan información.'),
        ('abc', 'Después de mostrar una frase, ¿qué pregunta aporta más información al grupo?', '«¿Qué viste y qué te hizo pensar?»', '«¿Estuvo bien o hubo algo que haya salido mal?»', '«¿Te gustó mi frase, y qué tan bien me salió?»', 'La pregunta pide descripción de lo visto y su interpretación.'),
        ('abc', 'Un grupo quiere mostrar «calma tensa» con una frase. ¿Qué combinación comunica esa idea?', 'Movimiento lento, respiración visible y mirada fija con pequeñas detenciones', 'Movimiento rápido y fuerte, con saltos', 'Movimiento continuo con la mirada al suelo y sin pausas', 'Lentitud con detenciones pequeñas y mirada fija producen tensión contenida.'),
    ],
    ctx=('abc', 'Un grupo presentó su frase «espera». Cuatro personas comentaron: dos vieron cansancio, una vio tristeza, una vio alegría. El grupo quería «espera con esperanza». ¿Qué decisión es más fundada?', 'Revisar qué rasgos produjeron cansancio y tristeza, y cambiar la energía y el foco hacia arriba', 'Cambiar todo el tema para que no haya más lecturas distintas', 'Mantener la frase igual porque ellos saben lo que quisieron decir y el público se equivocó', 'Se usan las lecturas como evidencia para ajustar decisiones concretas.'),
    sc=[
        ("En Danza: ¿qué es el foco?", "Hacia dónde se dirigen la atención y la mirada", "Cambia lo que se percibe de la frase."),
        ("¿Qué hace un comentario descriptivo?", "Dice qué se vio y qué sugirió", "Sirve para decidir qué mantener y qué cambiar en la frase."),
        ("¿Se comenta el cuerpo de la persona que baila?", "No, se comenta el movimiento", "El respeto al cuerpo ajeno es una regla del trabajo."),
    ],
    op=("Escribe tres comentarios de ejemplo (inventados) sobre una frase de espera: uno descriptivo con evidencia, uno vago y uno sobre el cuerpo de la persona. Identifica cuál es útil, cuál no y cuál no se debe decir. Reescribe el vago como descriptivo.",
        "1: «Vi pasos lentos y me dio cansancio». 2: «Estuvo bien». 3: «Tu cuerpo no sirve para bailar». Útil: 1. No ayuda: 2. No se debe decir: 3. Reescritura de 2: «Vi la mirada al frente y me dio calma».",
        ["clasifica los tres comentarios", "reescribe uno vago de forma descriptiva", "no repite comentarios sobre el cuerpo"],
        ["hoja con comentarios y reescritura"],
        ["aceptar comentarios sobre el cuerpo", "no dar evidencia observable"],
        "Pregunta: «¿qué viste exactamente?». Si responde con una opinión, pídele un rasgo del movimiento."),
    reinforce="Describe en dos líneas una frase de danza que hayas visto o imaginado, con un rasgo observado y lo que te sugirió.",
    extend="Explica por qué una lectura distinta a la intención puede ayudar a mejorar una frase.",
)
