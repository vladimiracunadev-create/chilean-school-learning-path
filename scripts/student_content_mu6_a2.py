"""Student material for 6.º básico Música, OA 02 (expresar con grados crecientes de elaboración y detalle lo que sugiere la música, con medios verbal, corporal, musical y visual).

Todas las músicas de los ejercicios son descripciones originales inventadas; las audiciones reales las selecciona y pone el docente.
Las respuestas personales (emociones, imágenes) no se califican por ser «correctas» sino por su elaboración y su evidencia audible; nadie debe contar experiencias privadas.
"""
from __future__ import annotations

from student_content_mu6_a import L, N
from student_lessons import arith, ex

OA2 = "MU06 OA 02"
NIV = ("nivel 1: nombra una sensación o emoción («es calma»); nivel 2: agrega la evidencia audible («porque va lento y suave»); "
       "nivel 3: agrega una idea o imagen («me imagino un lago sin viento»); nivel 4: conecta varios recursos, detalla cómo cambia la música y explica el efecto")
PIEZA = ("Pieza de 12 compases: compases 1 a 4 lentos y suaves con una melodía que baja; compases 5 a 8 cada vez más rápidos y con crescendo; "
         "compases 9 a 12 fuertes (f) con la melodía subiendo hasta lo más agudo")

# ---------------------------------------------------------------- OA 02 · clase 1 (niveles de elaboración)
L(
    OA2, 1,
    f"Lápiz y papel. Niveles de elaboración: {NIV}. Pieza de práctica: {PIEZA}. Si quieres, tararea o marca el pulso con palmas suaves. Cuida el volumen.",
    "Aprenderé a expresar lo que me sugiere una música con cada vez más detalle: desde nombrar una emoción hasta explicar con evidencia audible y una imagen cómo cambia. Sirve para que otras personas entiendan lo que escucho.",
    ["Sé que la dinámica es qué tan fuerte o suave suena y el tempo qué tan rápido va.", "Sé que una melodía puede subir o bajar.", "Sé que una opinión necesita una razón."],
    [
        f"Lo que te sugiere una música puede decirse de modo simple o muy elaborado. En esta clase usamos cuatro niveles: {NIV}. Un nivel más alto no es «más correcto»: es más detallado y se apoya mejor en lo que realmente suena.",
        "Para pasar del nivel 1 al 2 respondes «¿qué escucho que me hace sentir eso?»: el tempo, la dinámica, la dirección de la melodía, los instrumentos. Para pasar al nivel 3 agregas una imagen o una idea, como un lugar, un movimiento o una escena. Para llegar al 4 comparas partes de la pieza y explicas el efecto de los cambios.",
        "La evidencia audible es lo que realmente se oye, no lo que cuenta tu día ni si te gusta. «Me gusta» no es evidencia; «va rápido y fuerte» sí lo es. Nadie tiene que contar nada privado: puedes hablar de colores, paisajes o movimientos. Lo importante es que lo que dices pueda comprobarse escuchando de nuevo.",
    ],
    [("elaboración", "cuánto detalle y cuánta explicación tiene una respuesta"), ("evidencia audible", "lo que realmente se oye: tempo, dinámica, melodía, instrumentos"), ("sensación", "lo que la música te hace sentir, como calma o tensión"), ("imagen musical", "idea o escena que te sugiere la música"), ("conectar recursos", "unir varios rasgos de la música para explicar un efecto")],
    [
        ("Reconocer el nivel", "Una estudiante escribe: «Es misteriosa porque va lento y casi no suena fuerte». ¿Qué nivel de elaboración tiene?", ["Nombra una sensación: misteriosa.", "Agrega evidencia: va lento y casi no suena fuerte.", "No agrega una imagen ni compara partes."], "Nivel 2"),
        ("Subir de nivel", "Una estudiante escribe «Es alegre porque va rápido y fuerte». Para llegar al nivel 3, ¿qué debe agregar?", ["Ya tiene sensación y evidencia (nivel 2).", "El nivel 3 pide una imagen o idea: por ejemplo, una fiesta de pueblo."], "Una imagen o idea, como «me imagino una fiesta de pueblo»"),
    ],
    [
        ("Creer que «me gusta» es una evidencia.", "La evidencia debe ser audible; el gusto no se puede comprobar escuchando.", "Cambia «me gusta» por lo que suena: «va rápido y fuerte»."),
        ("Pensar que el nivel 4 solo es una respuesta más larga.", "El nivel 4 conecta recursos y explica cambios, no solo suma palabras.", "Compara partes y di qué efecto producen los cambios."),
    ],
    [
        ex("«Es calma.» ¿Qué nivel de elaboración tiene?", "Nivel 1", "Solo nombra una sensación, sin evidencia."),
        ex("¿Cuántos niveles de elaboración usa esta clase?", "4", "La clase define los niveles 1, 2, 3 y 4."),
        ex("¿Qué agrega el nivel 2 al nivel 1?", "La evidencia audible", "Dice qué se escucha que produce la sensación."),
    ],
    [
        ex("«Es tensa porque va rápida y fuerte; me imagino a alguien subiendo una escalera en la oscuridad.» ¿Qué nivel tiene?", "Nivel 3", "Tiene sensación, evidencia (rápida y fuerte) e imagen (la escalera), pero no compara partes ni explica cambios."),
        ex("¿Qué diferencia hay entre el nivel 3 y el nivel 4?", "El nivel 4 conecta varios recursos y explica los cambios y su efecto", "El nivel 3 agrega una imagen; el 4 detalla cómo cambia la música y qué produce."),
        ex("Una pieza va lenta y en p. ¿Qué evidencia audible puede usar quien dice que le da calma: (a) «porque va lento y suave» o (b) «porque tiene muchos instrumentos»?", "(a)", "Lento y suave es lo que realmente suena en esa pieza."),
    ],
    [
        ex(f"Escucha la pieza de práctica ({PIEZA}). ¿Cuál es mejor evidencia para decir que en los compases 5 a 8 crece la tensión: (a) «porque se acelera y sube el volumen» o (b) «porque ya llevamos varios minutos»?", "(a)", "El tempo y la dinámica que cambian se oyen en esos compases."),
        ex("¿Cuál de estas respuestas es nivel 2: (a) «Es triste.» o (b) «Es triste porque baja lentamente y suena bajito.»?", "(b)", "Tiene la sensación y la evidencia audible."),
        ex("Una respuesta dice: «Al comienzo va lenta y suave y me imagino un lago sin viento; luego se acelera y sube el volumen y parece que llega una tormenta.» ¿Qué nivel tiene?", "Nivel 4", "Conecta recursos, usa imágenes y detalla el cambio entre las partes."),
    ],
    [
        ex("Luis dice que «Es alegre porque me gusta» es nivel 2. ¿Tiene razón?", "No: «me gusta» no es evidencia audible; es nivel 1", "Falta decir qué se oye, como tempo o dinámica."),
        ex("Ordena de menos a más elaborada: (a) «Es calma.» (b) «Es calma porque va lenta.» (c) «Es calma porque va lenta y suave y me imagino un lago sin viento.»", "a, b, c", "Cada una agrega algo: evidencia en la b e imagen en la c."),
    ],
    [
        ex("Una respuesta nombra tres recursos: «va rápido, suena fuerte y la melodía da saltos». ¿Cuántos recursos musicales nombra?", "3", "Son tempo, dinámica y diseño melódico."),
        ex("Dos respuestas a la misma pieza: A «Es triste, va lento.» y B «Es triste: va lento y baja por grados; me imagino una lluvia suave.» ¿Cuál tiene mayor nivel y qué nivel?", "B, nivel 3", "B agrega una imagen (la lluvia) a la sensación y la evidencia."),
    ],
    [ex("Un video sin voz muestra un barco que se aleja con una música suave y lenta. Una estudiante dice: «Me da nostalgia porque suena suave y lenta, como cuando algo se va lejos». ¿Qué nivel tiene?", "Nivel 3", "Tiene sensación, evidencia (suave y lenta) y una comparación con una imagen, sin comparar partes de la música.")],
    [ex("¿Qué nivel nombra solo una emoción?", "El 1", "El nivel 1 no incluye evidencia."), ex("¿Qué es la evidencia audible?", "Lo que realmente se oye en la música", "Se puede comprobar escuchando otra vez."), ex("¿Es obligatorio contar experiencias privadas para responder?", "No", "Se puede hablar de colores, paisajes o movimientos.")],
    (
        f"Lee la pieza de práctica: «{PIEZA}». Escribe cuatro respuestas, una por cada nivel de elaboración, sobre lo que esta pieza te sugiere. Debes poder señalar qué parte de la pieza justifica cada afirmación. Si quieres, tararea la melodía subiendo y bajando para guiarte.",
        "Nivel 1: es tensa. Nivel 2: es tensa porque se acelera y sube el volumen. Nivel 3: es tensa porque se acelera y sube el volumen; me imagino a alguien que sube una montaña despacio y luego corre. Nivel 4: al comienzo va lenta y suave y baja, como un valle tranquilo; después se acelera y sube con crescendo, y en la parte final suena fuerte y sube hasta lo más agudo, como llegar a la cima.",
        ["escribe los 4 niveles en orden", "usa evidencia audible de la pieza", "el nivel 4 conecta recursos y cambios"],
        ["cuatro respuestas escritas"],
        ["usar «me gusta» como evidencia", "repetir la misma frase en todos los niveles"],
        "Reconoce el esfuerzo de elaborar y pide señalar en la pieza qué compases justifican cada afirmación.",
    ),
    "Escribe una respuesta de nivel 1 y súbela al nivel 2 con una evidencia audible.",
    "Escribe una respuesta de nivel 4 para una pieza inventada por ti que tenga tres partes.",
)

# ---------------------------------------------------------------- OA 02 · clase 2 (medios verbal, corporal, musical y visual)
EQ = ("tempo rápido = movimientos o trazos rápidos; tempo lento = lentos; sonido fuerte = grande y firme (trazo grueso); sonido suave = pequeño y liviano (trazo fino); "
      "sonido agudo = arriba, manos o línea altas; sonido grave = abajo; sonido largo = movimiento o línea continua; sonido corto = golpecito o punto")

L(
    OA2, 2,
    f"Lápiz, papel y espacio libre para moverte con cuidado, sin correr ni saltar sobre superficies resbalosas. Equivalencias de la clase: {EQ}. Todas las músicas están descritas en los ejercicios.",
    "Aprenderé a expresar lo que sugiere una música con distintos medios: palabras (verbal), movimiento (corporal), sonidos (musical) y dibujo (visual). Sirve para elegir el medio que mejor muestra lo que escucho.",
    ["Sé que el tempo es la velocidad y la dinámica es qué tan fuerte suena.", "Sé que una melodía puede ser aguda o grave.", "Sé dibujar líneas y puntos."],
    [
        "Un mismo sentimiento o idea se puede expresar de cuatro maneras: con palabras (medio verbal), con el cuerpo (medio corporal), con sonidos propios (medio musical) y con dibujos o colores (medio visual). No hay un medio mejor que otro: cada uno muestra cosas distintas y se pueden combinar.",
        f"Para traducir la música a otro medio se usan equivalencias entre lo que se oye y lo que se hace: {EQ}. Por ejemplo, una melodía aguda y corta se puede mostrar con manos arriba y golpecitos, o con puntos pequeños en la parte alta de la hoja.",
        "Al expresar con un medio distinto de la palabra, igual puedes explicar lo que hiciste: «dibujé una línea gruesa porque la música sonaba fuerte». Esa explicación es la evidencia. Si algo en tu cuerpo o en tu dibujo no puede relacionarse con lo que suena, se parece más a un adorno que a una expresión de la música.",
    ],
    [("medio expresivo", "forma de expresar algo: verbal, corporal, musical o visual"), ("equivalencia", "relación entre un rasgo del sonido y un rasgo del movimiento o dibujo"), ("trazo", "línea que se dibuja, que puede ser fina o gruesa"), ("agudo y grave", "sonidos de altura alta y baja"), ("traducir", "mostrar la misma idea musical con otro medio")],
    [
        ("Elegir el movimiento", "Una música suena lenta, suave y larga. ¿Qué movimiento la representa mejor: pasos lentos y livianos o saltos rápidos y fuertes?", ["Lento → movimientos lentos.", "Suave → livianos.", "Largo → continuos, no golpecitos."], "Pasos lentos y livianos"),
        ("Elegir el trazo", "Una música tiene sonidos cortos, fuertes y graves. ¿Qué dibujo la representa mejor: puntos grandes y gruesos abajo en la hoja o una línea fina y continua arriba?", ["Corto → puntos.", "Fuerte → grueso.", "Grave → abajo."], "Puntos grandes y gruesos abajo en la hoja"),
    ],
    [
        ("Hacer un movimiento o dibujo sin relación con lo que suena.", "Sin equivalencia con el sonido, el movimiento no expresa esa música.", "Antes de moverte pregúntate: ¿qué hace la música aquí y qué hace mi cuerpo?"),
        ("Pensar que solo vale la palabra.", "Los medios corporal, musical y visual también son formas de expresión válidas.", "Elige el medio que muestre mejor ese rasgo."),
    ],
    [
        ex("¿Cuáles son los cuatro medios expresivos de esta clase?", "Verbal, corporal, musical y visual", "Son palabras, movimiento, sonidos propios y dibujo."),
        ex("Para un sonido muy agudo, ¿las manos van arriba o abajo?", "Arriba", "La equivalencia dice que agudo = arriba."),
        ex("Un sonido largo y suave, ¿se dibuja con una línea fina continua o con puntos gruesos?", "Con una línea fina continua", "Largo = continuo y suave = fino."),
    ],
    [
        ex("Dibujar una línea que sube, ¿es un medio verbal, corporal o visual?", "Visual", "Es un dibujo."),
        ex("Caminar muy lento con pasos suaves, ¿qué medio es y qué dos recursos musicales representa?", "Corporal; tempo lento y dinámica suave", "Es movimiento, lento por el tempo y suave por la dinámica."),
        ex("Escribir un párrafo sobre lo que sugiere una música, ¿qué medio es?", "Verbal", "Se usan palabras."),
    ],
    [
        ex("Una melodía sube de a poco y el volumen crece. ¿Qué dibujo la representa mejor: (a) línea que sube y se va engrosando o (b) línea que baja y se va adelgazando?", "(a)", "Subir = línea que sube; crecer el volumen = trazo más grueso."),
        ex("La música va rápida y fuerte. ¿Qué movimiento la representa mejor: (a) pasos rápidos y grandes o (b) pasos lentos y pequeños?", "(a)", "Rápido y fuerte se corresponde con rápido y grande."),
        arith("Una coreografía tiene 4 movimientos de 8 pulsos cada uno. ¿Cuántos pulsos dura?", "4*8", "Se multiplican los movimientos por los pulsos de cada uno.", " pulsos"),
    ],
    [
        ex("Pedro dibuja puntos gruesos para una música larga y suave. ¿Qué debería cambiar?", "Usar una línea fina y continua", "Largo se representa continuo y suave con trazo fino."),
        ex("Una estudiante dice «mi cuerpo se va haciendo cada vez más rápido». ¿Qué recurso musical representa: accelerando o diminuendo?", "Accelerando", "Que se hace más rápido es un accelerando."),
    ],
    [
        ex("Tres estudiantes muestran lo mismo: «va subiendo» (verbal), estirarse de a poco hacia arriba (corporal) y una línea que sube (visual). ¿Qué rasgo de la música representan los tres?", "Una melodía que sube", "Los tres muestran altura que aumenta."),
        arith("Un dibujo de 12 compases empieza con un primer color y cambia de color cada 3 compases. ¿Cuántas veces cambia de color?", "12//3-1", "Hay 4 colores y entre 4 colores hay 3 cambios.", " cambios"),
    ],
    [ex("Un grupo representa con el cuerpo una música que parte en p y lenta y termina en ff y rápida. ¿Cómo se mueve al principio y cómo al final?", "Al principio con movimientos pequeños y lentos; al final grandes y rápidos", "Suave y lento es pequeño y lento; fuerte y rápido es grande y rápido.")],
    [ex("¿Qué medio usa las palabras?", "El verbal", "Verbal viene de palabra."), ex("¿Con qué trazo se dibuja un sonido fuerte?", "Grueso", "Fuerte = grueso en las equivalencias."), ex("¿Qué es la evidencia cuando expresas con un dibujo?", "Explicar qué parte de la música muestra cada rasgo del dibujo", "La explicación une dibujo y sonido.")],
    (
        "Lee esta música: «Cuatro compases lentos y suaves, con una melodía que baja; luego cuatro compases rápidos y fuertes, con sonidos cortos y agudos.» Representa lo que te sugiere con tres medios: una frase (verbal), un movimiento de 8 pulsos (corporal) y un dibujo con líneas y puntos en la hoja (visual). Escribe qué hiciste en cada medio y qué parte de la música lo justifica.",
        "Verbal: «Primero un anochecer tranquilo y después una fiesta que despierta». Corporal: 4 pulsos con movimientos lentos y pequeños hacia abajo y 4 pulsos con saltitos cortos y manos arriba. Visual: una línea fina y continua que baja en la mitad izquierda y puntos gruesos y altos en la derecha. Cada parte copia el tempo, el volumen, la altura y la duración de los sonidos.",
        ["usa tres medios distintos", "relaciona cada decisión con un rasgo sonoro", "explica la evidencia"],
        ["frase escrita", "movimiento descrito", "dibujo"],
        ["representar sin relación con el sonido", "no explicar"],
        "Reconoce la traducción entre medios y pide mostrar con el dedo en la descripción qué rasgo se refleja en cada decisión.",
    ),
    "Camina siguiendo una música lenta y suave imaginada y luego una rápida y fuerte.",
    "Dibuja la forma ABA de una pieza usando un trazo distinto para cada sección.",
)

# ---------------------------------------------------------------- OA 02 · clase 3 (responder con sonidos propios)
L(
    OA2, 3,
    "Lápiz y papel. Fuentes de sonido seguras: tu voz, palmas, chasquidos y golpes suaves con la yema de los dedos sobre una mesa o un cuaderno. No uses objetos de vidrio, ni pequeños, ni filosos. Cuida el volumen y descansa los oídos entre ensayos.",
    "Aprenderé a responder a una música con sonidos propios: elegir tempo, dinámica, duración y textura para expresar una sensación o idea. Sirve para convertir lo que siento al escuchar en música que otros pueden oír.",
    ["Sé que el tempo es rápido o lento y la dinámica fuerte o suave.", "Sé que un sonido puede ser largo o corto.", "Sé calcular cuánto dura una pieza con pulsos por minuto."],
    [
        "Responder con sonidos propios es crear una pequeña música que expresa lo que otra música te sugiere. Para decidir qué hacer, relaciona la idea con los recursos: calma suele sonar lenta, suave y con sonidos largos; fiesta suele sonar rápida, fuerte y con sonidos cortos; tensión que crece pide crescendo y accelerando; sorpresa pide un silencio seguido de un golpe fuerte.",
        "Con tu voz y tu cuerpo puedes producir sonidos muy distintos: un «uuu» largo y suave, un chasquido corto, palmas fuertes o golpecitos con la yema de los dedos. Combínalos con un pulso estable para que se oiga que son decisiones y no ruidos al azar. Por ejemplo, 8 pulsos de golpecitos suaves y lentos y luego 8 pulsos de palmas rápidas y fuertes cuentan un cambio de calma a energía.",
        "Una respuesta musical necesita un plan: qué sensación expresa, qué recursos usa y cuánto dura. La duración se calcula con el tempo: pulsos × 60 ÷ pulsos por minuto da los segundos. Al terminar, explica en una frase qué recurso representa cada parte, porque esa explicación es la evidencia de que tu respuesta musical fue pensada.",
    ],
    [("respuesta musical", "música propia que expresa lo que otra música sugiere"), ("sonido largo y corto", "sonido que dura mucho o poco"), ("crescendo y accelerando", "volumen y velocidad que aumentan poco a poco"), ("silencio expresivo", "pausa que produce suspenso o sorpresa"), ("plan sonoro", "decisión previa de recursos y duración")],
    [
        ("Elegir recursos", "Quieres expresar «un lago en calma». ¿Qué combinación eliges: tempo lento con p y sonidos largos o tempo rápido con f y sonidos cortos?", ["Calma → lento y suave.", "Un lago en calma no tiene golpes: sonidos largos."], "Tempo lento con p y sonidos largos"),
        ("Calcular la duración", "Tu respuesta tiene 24 pulsos y la tocas a 72 pulsos por minuto. ¿Cuántos segundos dura?", ["Segundos = pulsos × 60 ÷ pulsos por minuto.", "24 × 60 = 1440 y 1440 ÷ 72 = 20."], "20 segundos"),
    ],
    [
        ("Hacer ruido sin plan y decir que expresa algo.", "Sin decisiones de tempo, dinámica y duración no hay respuesta musical.", "Planifica qué recurso representa cada parte."),
        ("Tocar muy fuerte para que «se note».", "Fuerte no siempre expresa mejor y puede dañar el oído; el volumen debe tener razón y ser seguro.", "Usa contrastes de volumen moderados y descansa."),
    ],
    [
        ex("Para expresar calma, ¿suena mejor un tempo lento y suave o uno rápido y fuerte?", "Lento y suave", "La calma se asocia con poca velocidad y poco volumen."),
        ex("¿Qué recurso pide una «tensión que crece»?", "Crescendo y accelerando", "Crecen el volumen y la velocidad poco a poco."),
        ex("¿Qué fuentes de sonido son seguras en esta clase: la voz y las palmas o un vaso de vidrio?", "La voz y las palmas", "El vidrio es peligroso y no se usa."),
    ],
    [
        ex("Una estudiante quiere expresar una sorpresa. ¿Qué combina mejor: un silencio seguido de un golpe fuerte o un sonido suave y continuo?", "Un silencio seguido de un golpe fuerte", "El silencio crea suspenso y el golpe fuerte sorprende."),
        ex("Su plan es: 8 pulsos de golpecitos suaves y lentos, luego 8 de palmas rápidas y fuertes. ¿Qué cambio expresa: de calma a energía o de energía a calma?", "De calma a energía", "Empieza suave y lento y termina fuerte y rápido."),
        ex("Un «uuu» largo y suave con la voz, ¿expresa mejor un amanecer tranquilo o una carrera?", "Un amanecer tranquilo", "Largo y suave corresponde a la calma."),
    ],
    [
        arith("Tu respuesta sonora tiene 6 compases de 4 pulsos y va a 80 pulsos por minuto. ¿Cuántos segundos dura?", "6*4*60//80", "Son 24 pulsos y cada pulso dura 0,75 segundos.", " segundos"),
        arith("Una respuesta tiene una parte de 16 pulsos y otra de 12 pulsos. A 60 pulsos por minuto, ¿cuántos segundos dura toda?", "(16+12)*60//60", "A 60 por minuto cada pulso dura 1 segundo.", " segundos"),
        ex("Quieres que la segunda parte sea el doble de rápida que la primera, que va a 60 pulsos por minuto. ¿A cuántos pulsos por minuto debe ir?", "120", "El doble de 60 es 120."),
    ],
    [
        ex("Julia dice que su respuesta expresa calma porque usó palmas muy fuertes. ¿Qué cambio de dinámica necesita para ser coherente?", "Pasar a una dinámica suave (p)", "La calma se expresa con volumen bajo."),
        ex("Un plan dice: «8 pulsos en pp, 8 pulsos en mf, 8 pulsos en ff». ¿Es un crescendo escalonado o un diminuendo?", "Un crescendo escalonado", "El volumen aumenta en cada parte."),
    ],
    [
        ex("Quieres contar un cambio de «noche tranquila» a «amanecer con pájaros». Diseña la dinámica y el tempo de las dos partes: ¿cuál empieza más suave y más lenta, noche o amanecer?", "La noche", "La noche tranquila es lenta y suave; el amanecer se activa."),
        arith("Una respuesta de 3 partes: 8 pulsos a 60 por minuto, luego 8 pulsos a 120 por minuto, luego 8 pulsos a 60 por minuto. ¿Cuántos segundos dura?", "8*60//60+8*60//120+8*60//60", "Dura 8 s + 4 s + 8 s.", " segundos"),
    ],
    [ex("Para acompañar un cuento donde un gato se acerca despacio y de pronto salta, ¿qué secuencia de sonidos propios eliges: golpecitos suaves y lentos con un golpe fuerte al final o palmas fuertes continuas?", "Golpecitos suaves y lentos con un golpe fuerte al final", "El suspenso se crea con suavidad y la sorpresa final con un golpe fuerte.")],
    [ex("¿Qué se calcula con pulsos × 60 ÷ pulsos por minuto?", "Los segundos que dura la respuesta", "Es la fórmula de duración con el tempo."), ex("¿Qué recurso expresa una sorpresa?", "Un silencio seguido de un golpe fuerte", "Es lo que sugiere la clase."), ex("¿Por qué se debe cuidar el volumen?", "Para proteger los oídos", "El volumen muy alto puede dañar la audición.")],
    (
        "Elige una de estas tres ideas: A) «una tormenta que llega y se va», B) «un gato que se acerca despacio y salta» o C) «un pueblo que despierta». Planifica en una tabla de tres partes qué sonido propio, qué dinámica y qué tempo usarás en cada parte y cuántos pulsos dura cada una. Calcula cuántos segundos dura toda tu respuesta a un tempo que elijas. Ensáyala con tu voz y tus palmas a volumen bajo.",
        "Idea A. Parte 1: golpecitos de dedos en pp, 60 por minuto, 8 pulsos. Parte 2: palmas con crescendo hasta f, ahora a 120 por minuto, 8 pulsos. Parte 3: golpecitos en pp con diminuendo, 60 por minuto, 8 pulsos. Duración: 8 + 4 + 8 = 20 segundos.",
        ["la tabla tiene tres partes con sonido, dinámica y tempo", "los recursos coinciden con la idea", "calcula bien la duración"],
        ["tabla de plan", "respuesta ensayada"],
        ["elegir recursos que no coinciden con la idea", "calcular mal los segundos"],
        "Reconoce el plan y pide explicar con una frase qué recurso representa cada parte.",
    ),
    "Haz 8 pulsos de golpecitos suaves y 8 de palmas fuertes y descríbelos con una frase.",
    "Agrega una cuarta parte a tu respuesta con un silencio expresivo y explica su efecto.",
)

# ---------------------------------------------------------------- OA 02 · clase 4 (ajustar y elaborar la respuesta)
CRI = ("criterios de una buena respuesta: 1) nombra una sensación o idea; 2) da evidencia audible; 3) incluye una imagen o idea; 4) conecta recursos o cambios; cada criterio cumplido vale 1 punto")

L(
    OA2, 4,
    f"Lápiz y papel. {CRI}. Las respuestas que se revisan están escritas en los ejercicios. Trabaja en silencio o en voz baja.",
    "Aprenderé a revisar mi respuesta a una música con una lista de criterios y a mejorarla agregando evidencia y detalle. Sirve para llegar a una expresión más precisa sin cambiar lo que sentí.",
    ["Sé que hay cuatro niveles de elaboración.", "Sé que la evidencia audible es lo que realmente se oye.", "Sé contar puntos de una lista."],
    [
        f"Revisar una respuesta es compararla con criterios y ver qué falta. En esta clase usamos esta lista: {CRI}. Una respuesta con 4 puntos tiene el máximo de elaboración. Revisar no cambia lo que sentiste; ayuda a decirlo mejor.",
        "Para mejorar, primero marca qué criterios ya cumple. Luego elige el criterio que falta y agrega una sola cosa: si falta evidencia, escribe qué se oye (tempo, dinámica, altura); si falta imagen, agrega una escena; si falta conexión, compara dos partes y explica el efecto. Mejorar de a un criterio es más fácil que reescribir todo.",
        "También hay que cuidar que lo agregado sea verdadero con respecto a la música. Si dices que «se acelera» y la música mantiene el mismo pulso, la evidencia es falsa. Escuchar de nuevo, o volver a leer la descripción de la pieza, es la forma de comprobarlo. Revisar con respeto también sirve para ayudar a otros: dices qué criterio cumple y qué podría agregar, sin burlarte.",
    ],
    [("criterio", "regla para revisar si algo está bien hecho"), ("revisar", "leer una respuesta y compararla con los criterios"), ("mejorar", "agregar o corregir algo para que cumpla más criterios"), ("comprobar", "volver a escuchar o leer para ver si lo que dices es verdadero"), ("máximo de elaboración", "respuesta que cumple los 4 criterios")],
    [
        ("Puntuar una respuesta", "Pieza: lenta, en p, con melodía que baja. Respuesta: «Es calma porque va lenta y suave; me imagino una tarde sin viento». ¿Cuántos puntos tiene?", ["Criterio 1: sí, calma.", "Criterio 2: sí, va lenta y suave.", "Criterio 3: sí, una tarde sin viento.", "Criterio 4: no compara partes."], "3 puntos"),
        ("Mejorar un criterio", "Respuesta: «Es calma.» Pieza: lenta, en p. ¿Qué agregar para tener 2 puntos?", ["Solo cumple el criterio 1.", "Falta evidencia audible: lo que se oye en la pieza."], "La evidencia: «porque va lenta y suave»"),
    ],
    [
        ("Agregar evidencia que no es verdadera para la pieza.", "La evidencia debe coincidir con lo que suena.", "Comprueba volviendo a escuchar o leer la descripción."),
        ("Reescribir toda la respuesta cuando falta un solo criterio.", "Basta con agregar lo que falta; reescribir todo gasta tiempo y puede perder lo bueno.", "Mejora un criterio a la vez."),
    ],
    [
        ex("¿Cuántos criterios tiene la lista de revisión de la clase?", "4", "Son sensación, evidencia, imagen y conexión de recursos."),
        ex("Una respuesta cumple 2 criterios. ¿Cuántos puntos tiene?", "2", "Cada criterio cumplido vale 1 punto."),
        ex("Si a una respuesta le falta evidencia audible, ¿qué debes agregar: lo que se oye o lo que te gusta?", "Lo que se oye", "La evidencia es audible, no es gusto."),
    ],
    [
        ex("Pieza: rápida y fuerte. Respuesta: «Es energía porque va rápida y fuerte.» ¿Cuántos puntos tiene?", "2", "Cumple sensación y evidencia; no tiene imagen ni conexión."),
        ex("Pieza: rápida y fuerte. Para sumar el criterio 3, ¿cuál agregas: (a) «Me imagino una fiesta de pueblo.» o (b) «Va a 110 pulsos por minuto.»?", "(a)", "El criterio 3 pide una imagen o idea, y la (a) lo es."),
        ex("Para sumar el criterio 4 en una respuesta sobre una pieza que parte lenta y termina rápida, ¿qué agregas?", "Una comparación entre las dos partes y su efecto", "El criterio 4 conecta recursos y cambios."),
    ],
    [
        ex("Pieza: lenta y en p durante los compases 1 a 4 y rápida y en f durante los compases 5 a 8. Respuesta: «En los compases 1 a 4 es calma por lo lento y suave, y en los 5 a 8 es energía porque va rápida y suena fuerte; el cambio parece un amanecer.» ¿Cuántos puntos tiene?", "4", "Tiene sensación, evidencia, imagen (amanecer) y conexión entre dos partes."),
        ex("Luis cambió «va rápida» por «va lenta» porque quiere sonar más calmado, pero la pieza es rápida. ¿Mejoró su respuesta?", "No: su evidencia ya no coincide con la pieza", "La evidencia debe ser verdadera con respecto a lo que suena."),
        arith("Un curso revisó 5 respuestas con estos puntos: 2, 3, 4, 3 y 3. ¿Cuántos puntos hay en total?", "2+3+4+3+3", "Se suman los puntos de las cinco respuestas.", " puntos"),
    ],
    [
        ex("Una respuesta dice: «Es misteriosa porque va lenta y suave; me imagino un pasillo oscuro.» Pieza: lenta y suave, pero con un golpe fuerte súbito en el compás 7. ¿Qué detalle falta para el criterio 4?", "Mencionar el golpe fuerte del compás 7 y su efecto", "Conectar la sorpresa con el resto es lo que da el cuarto punto."),
        ex("Dos estudiantes revisan: Sara tiene 3 puntos y Tomás 2. ¿Cuántos puntos necesita Tomás para igualar a Sara?", "1", "3 − 2 = 1 punto más."),
    ],
    [
        arith("Un curso de 24 estudiantes revisó sus respuestas: 6 tienen 4 puntos, 10 tienen 3 puntos y el resto tiene 2 puntos. ¿Cuántos puntos suman entre todos?", "6*4+10*3+(24-6-10)*2", "Hay 8 estudiantes con 2 puntos; se multiplican los grupos y se suman.", " puntos"),
        ex("Una respuesta de 3 puntos cumple sensación, evidencia y conexión de recursos. ¿Qué criterio le falta?", "La imagen o idea (criterio 3)", "De los cuatro criterios, falta el que pide una imagen o idea."),
    ],
    [ex("Una compañera te muestra la respuesta «Es feliz.» Para ayudarla con respeto, ¿qué dices: «Tu respuesta tiene un punto; podrías agregar qué se oye» o «Eso es muy poco»?", "Tu respuesta tiene un punto; podrías agregar qué se oye", "Dice qué cumple y qué agregar, sin burlarse.")],
    [ex("¿Cuánto vale cada criterio cumplido?", "1 punto", "La lista usa un punto por criterio."), ex("¿Qué se debe hacer antes de agregar evidencia nueva?", "Comprobar que es verdadera para la pieza", "Volver a escuchar o leer la descripción."), ex("¿Mejorar es lo mismo que cambiar lo que sentiste?", "No", "Mejorar ayuda a decirlo mejor.")],
    (
        "Tienes esta pieza: «Compases 1 a 4: lentos y suaves, melodía que baja. Compases 5 a 8: se acelera con crescendo, melodía que sube. Compás 9: un silencio. Compases 10 a 12: fuertes (f) y rápidos.» Revisa esta respuesta: «Es tensa.» Primero cuenta sus puntos. Luego mejórala agregando un criterio a la vez hasta llegar a 4 puntos. Escribe las cuatro versiones y señala qué agregaste en cada una.",
        "Versión 1 (1 punto): «Es tensa». Versión 2 (2): «Es tensa porque se acelera y sube el volumen en los compases 5 a 8». Versión 3 (3): «… me imagino a alguien subiendo una escalera cada vez más rápido». Versión 4 (4): «… el silencio del compás 9 es como detenerse antes de llegar, y los compases 10 a 12, rápidos y fuertes, son la llegada».",
        ["empieza contando bien los puntos", "agrega un criterio a la vez", "la evidencia coincide con la pieza"],
        ["cuatro versiones escritas"],
        ["agregar evidencia falsa", "reescribir todo en vez de agregar"],
        "Reconoce el proceso de mejora y pide señalar en la pieza dónde se comprueba cada evidencia agregada.",
    ),
    "Puntúa una respuesta tuya anterior con la lista de cuatro criterios.",
    "Revisa la respuesta de una persona de tu casa a una música, solo si ella quiere, y dile un criterio que cumple y uno que podría agregar.",
)
