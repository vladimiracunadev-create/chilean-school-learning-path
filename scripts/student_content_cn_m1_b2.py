"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 12 (oído, ojo, espectros y tecnologías correctivas)."""
from __future__ import annotations

from student_lessons import arith, ex, register


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def _x(items):
    return [ex(*i) if isinstance(i, tuple) else i for i in items]


def L(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, rec, und, app, rea, cha, context, selfcheck, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": w[0], "problem": w[1], "steps": w[2], "answer": w[3]} for w in worked],
        mistakes=[{"wrong": m[0], "why": m[1], "fix": m[2]} for m in mistakes],
        tiers={"recovery": _x(rec), "understand": _x(und), "apply": _x(app), "reason": _x(rea), "challenge": _x(cha)},
        context=_x(context), selfcheck=_x(selfcheck), open_task=open_task, reinforce=reinforce, extend=extend,
    )


OA = "CN1M OA 12"

L(OA, 1,
  materials="Este cuaderno, lápiz y lápices de colores. No necesitas ningún instrumento: las partes y los datos están descritos en los ejercicios.",
  use="Aprenderé cómo el oído recibe las ondas sonoras y las convierte en señales para el cerebro. Sirve para entender cómo oímos y qué partes pueden fallar.",
  prior=["Sé que el sonido es una onda que necesita un medio para viajar.", "Sé que las ondas tienen frecuencia y amplitud."],
  explain=[
      "El sonido es una onda mecánica longitudinal: hace vibrar las partículas del medio en la misma dirección en que avanza la onda. Por eso necesita un medio, como aire, agua o un sólido, y no viaja en el vacío. El oído recibe esas ondas y las convierte en impulsos nerviosos que el cerebro interpreta como sonidos.",
      "El oído externo está formado por el pabellón auricular, que capta las ondas, y el conducto auditivo, que las lleva hasta el tímpano, una membrana que vibra. En el oído medio, tres huesecillos llamados martillo, yunque y estribo transmiten y amplifican la vibración; la trompa de Eustaquio iguala la presión con la garganta. En el oído interno, la cóclea, un tubo enrollado y lleno de líquido, tiene células ciliadas que transforman la vibración en señales nerviosas, y el nervio auditivo las lleva al cerebro. Los canales semicirculares, también del oído interno, no sirven para oír: ayudan al equilibrio.",
      "Una pregunta investigable sobre el oído debe indicar qué se mide. Por ejemplo, «¿a qué distancia deja de oírse un reloj de pulsera si lo cubres con una toalla?» se contesta con una medición en metros. Una pregunta como «¿es agradable oír un reloj?» depende de opiniones y no se puede investigar.",
  ],
  vocab=[("onda longitudinal", "onda en que las partículas vibran en la misma dirección en que avanza"), ("pabellón auricular", "oreja, que capta las ondas sonoras"), ("tímpano", "membrana que vibra al llegar el sonido"), ("huesecillos", "tres huesos del oído medio: martillo, yunque y estribo"), ("cóclea", "tubo enrollado del oído interno donde se producen las señales nerviosas"), ("nervio auditivo", "nervio que lleva las señales del oído al cerebro")],
  worked=[
      ("Ruta del sonido", "Ordena el camino del sonido desde el aire hasta el cerebro: cóclea, tímpano, pabellón auricular, huesecillos, nervio auditivo, conducto auditivo.", ["Parto por la parte más externa: pabellón auricular y conducto auditivo.", "Sigo con el tímpano y los huesecillos.", "Termino en la cóclea y el nervio auditivo."], "Pabellón auricular, conducto auditivo, tímpano, huesecillos, cóclea, nervio auditivo"),
      ("Pregunta investigable", "¿Es investigable «¿cuántos metros se aleja una persona hasta que deja de oír un timbre con las manos tapando sus orejas?»", ["Veo qué se mide: una distancia en metros.", "Se puede repetir y comparar con y sin las manos."], "Sí, porque se contesta midiendo distancias"),
  ],
  mistakes=[
      ("Creer que el sonido llega al cerebro directamente desde el tímpano.", "Después del tímpano hay huesecillos, cóclea y nervio auditivo.", "Recorre la ruta completa en orden."),
      ("Pensar que los canales semicirculares permiten oír.", "Pertenecen al oído interno pero se relacionan con el equilibrio.", "Asocia cóclea con oír y canales semicirculares con equilibrio."),
  ],
  rec=[
      ("¿Qué membrana vibra primero cuando llega el sonido al interior del oído?", "El tímpano", "Está al final del conducto auditivo."),
      ("¿Cuántos huesecillos tiene el oído medio?", "Tres", "Son el martillo, el yunque y el estribo."),
      ("Verdadero o falso: el sonido se propaga en el vacío.", "Falso", "Las ondas sonoras necesitan un medio material."),
  ],
  und=[
      ("¿Cuál es la función de la cóclea? A) Transformar vibraciones en impulsos nerviosos B) Capturar las ondas en el aire", "A", "Sus células ciliadas generan señales para el nervio auditivo."),
      ("¿Qué estructura iguala la presión entre el oído medio y la garganta?", "La trompa de Eustaquio", "Une el oído medio con la garganta."),
      ("¿Cuál es la función del tímpano? A) Vibrar con las ondas sonoras que llegan por el conducto auditivo B) Generar los impulsos nerviosos", "A", "Es una membrana que se mueve con el sonido; los impulsos se generan en la cóclea."),
  ],
  app=[
      arith("Gritas frente a una pared y escuchas el eco 2 segundos después. El sonido viaja a 340 m/s en el aire. ¿A cuántos metros está la pared?", "340*2/2", "El sonido recorre ida y vuelta, así que la distancia a la pared es la mitad de lo recorrido.", " m"),
      ("En un cerro, una persona siente presión en el oído al subir en un vehículo. ¿Qué parte del oído iguala esa presión?", "La trompa de Eustaquio", "Conecta el oído medio con la garganta para equilibrar la presión."),
      ("Se hacen sonar dos timbres idénticos, uno en el aire y otro dentro del agua. ¿Qué es necesario para que el sonido llegue al oído en ambos casos? A) Que exista un medio material que transmita la vibración B) Que el medio sea siempre aire", "A", "El sonido solo se propaga por un medio."),
  ],
  rea=[
      ("Una compañera dice que los canales semicirculares ayudan a oír los sonidos graves. ¿Es correcto? A) No: se relacionan con el equilibrio B) Sí: forman parte de la cóclea", "A", "Los canales semicirculares no participan de la audición."),
      ("¿Qué dato necesitas medir para comprobar si una toalla disminuye el sonido de un reloj? A) La distancia máxima a la que se oye con y sin toalla B) El color de la toalla", "A", "La distancia de audición es una medida que permite comparar."),
  ],
  cha=[
      arith("Un tímpano vibra 440 veces por segundo con una nota musical. ¿Cuántas vibraciones hace en 10 segundos?", "440*10", "Se multiplica la frecuencia por el tiempo."),
      arith("El sonido viaja a 340 m/s en el aire y a 1.500 m/s en el agua. ¿Cuántos metros más recorre en el agua en 2 segundos?", "(1500-340)*2", "Se resta la rapidez en el aire a la rapidez en el agua y se multiplica por el tiempo.", " m"),
  ],
  context=[ex("Después de un resfrío, un estudiante oye menos porque tiene líquido detrás del tímpano. Si sientes dolor de oído, avisa a una persona adulta. ¿En qué parte del oído hay líquido que no debería estar? A) En el oído medio B) En el oído externo", "A", "El tímpano separa el oído externo del medio; el líquido queda detrás de él.")],
  selfcheck=[("¿Por qué el sonido no viaja en el vacío?", "Porque necesita un medio material", "Las ondas sonoras hacen vibrar partículas."), ("¿Qué hacen los huesecillos?", "Transmiten y amplifican la vibración del tímpano", "Llevan la vibración al oído interno."), ("¿Qué parte del oído tiene células ciliadas?", "La cóclea", "Allí se generan las señales nerviosas.")],
  open_task=task("En tu cuaderno dibuja tres recuadros: oído externo, oído medio y oído interno. Ubica en ellos: pabellón auricular, conducto auditivo, tímpano, martillo, yunque, estribo, cóclea, nervio auditivo y trompa de Eustaquio. Con flechas, muestra por dónde viaja el sonido. Escribe una pregunta investigable sobre cómo se oye un reloj de pulsera a distintas distancias.", "Externo: pabellón y conducto. Medio: tímpano, martillo, yunque, estribo y trompa de Eustaquio. Interno: cóclea y nervio auditivo. Pregunta: «¿A cuántos metros deja de oírse un reloj de pulsera en una pieza silenciosa?»", ["ubica las nueve estructuras en el recuadro correcto", "flechas en el orden de la ruta", "pregunta con una medición"], ["dibujo con rótulos", "pregunta escrita"], ["poner la cóclea en el oído medio", "escribir una pregunta de opinión"], "Pregunta qué parte falla si el sonido llega al tímpano pero no se genera la señal nerviosa."),
  reinforce="Escribe en orden las seis estructuras de la ruta del sonido, desde el pabellón auricular hasta el nervio auditivo, sin mirar el ejemplo resuelto.",
  extend="Explica por qué el oído medio necesita huesecillos y no solo un tímpano.")

L(OA, 2,
  materials="Este cuaderno, lápiz, regla y calculadora. Todos los datos de sonidos están escritos en los ejercicios; no necesitas aparatos de medición.",
  use="Aprenderé qué parte del espectro sonoro oímos y cómo se mide la intensidad. Sirve para cuidar la audición y entender por qué algunos animales oyen lo que nosotros no.",
  prior=["Sé que la frecuencia se mide en hertz.", "Sé que la amplitud de una onda se relaciona con su energía."],
  explain=[
      "El sonido tiene dos características principales. La frecuencia, medida en hertz (Hz), es el número de vibraciones por segundo y la percibimos como tono: más frecuencia es un sonido más agudo y menos frecuencia, uno más grave. La amplitud se relaciona con la intensidad, que percibimos como volumen y se mide en decibeles (dB).",
      "El espectro sonoro se divide según la frecuencia. Los infrasonidos tienen menos de 20 Hz y no los oímos. Los sonidos audibles para una persona joven con audición sana están entre 20 Hz y 20.000 Hz. Los ultrasonidos superan los 20.000 Hz; los usan los murciélagos para orientarse y la ecografía médica. Con la edad solemos perder primero los sonidos más agudos.",
      "La escala de decibeles parte de 0 dB, el sonido más débil que oímos, y cada 10 dB más equivale a 10 veces más energía sonora. Un susurro tiene unos 30 dB, una conversación unos 60 dB, una calle con mucho tráfico cerca de 80 dB y un concierto o unos audífonos al máximo, más de 100 dB. Una exposición prolongada a más de 85 dB puede dañar las células ciliadas de la cóclea, y ese daño no se recupera. Para cuidarte, baja el volumen y descansa de los audífonos.",
  ],
  vocab=[("frecuencia", "número de vibraciones por segundo; se mide en hertz"), ("tono", "cualidad que distingue un sonido agudo de uno grave"), ("intensidad", "cantidad de energía del sonido, que percibimos como volumen"), ("decibel (dB)", "unidad con que se mide la intensidad del sonido"), ("infrasonido", "sonido de frecuencia menor que 20 Hz"), ("ultrasonido", "sonido de frecuencia mayor que 20.000 Hz")],
  worked=[
      ("Clasificar por frecuencia", "Clasifica estos sonidos: 15 Hz, 440 Hz y 25.000 Hz.", ["Reviso los límites: audible entre 20 Hz y 20.000 Hz.", "15 Hz está bajo 20 Hz; 440 Hz está dentro; 25.000 Hz está sobre 20.000 Hz."], "15 Hz infrasonido; 440 Hz audible; 25.000 Hz ultrasonido"),
      ("Comparar decibeles", "¿Cuántas veces más energía tiene un sonido de 70 dB que uno de 50 dB?", ["La diferencia es de 20 dB, es decir, dos pasos de 10 dB.", "Cada paso multiplica por 10: 10 × 10."], "100 veces"),
  ],
  mistakes=[
      ("Creer que subir el volumen vuelve más agudo el sonido.", "El volumen se relaciona con la amplitud; el tono depende de la frecuencia.", "Pregunta si cambió la frecuencia o la amplitud."),
      ("Pensar que un sonido de 80 dB es el doble de fuerte que uno de 40 dB.", "La escala de dB no es lineal: cada 10 dB multiplica por 10 la energía.", "Cuenta cuántos pasos de 10 dB hay entre los dos sonidos."),
  ],
  rec=[
      ("¿En qué unidad se mide la frecuencia de un sonido?", "En hertz", "Un hertz es una vibración por segundo."),
      ("Un sonido de 30.000 Hz, ¿es audible, infrasonido o ultrasonido?", "Ultrasonido", "Supera los 20.000 Hz."),
      ("¿En qué unidad se mide la intensidad del sonido?", "En decibeles", "El símbolo es dB."),
  ],
  und=[
      ("El tono de un sonido depende de su: A) frecuencia B) amplitud", "A", "Más frecuencia da un sonido más agudo."),
      ("Un murciélago emite chillidos de 50.000 Hz que una persona no oye. ¿Por qué? A) Porque superan los 20.000 Hz B) Porque son demasiado graves", "A", "Son ultrasonidos, fuera del rango audible."),
      ("¿Qué sonido es más agudo: uno de 200 Hz o uno de 800 Hz?", "El de 800 Hz", "Mayor frecuencia es más agudo."),
  ],
  app=[
      arith("El rango audible va de 20 Hz a 20.000 Hz. ¿Cuántos hertz abarca?", "20000-20", "Se resta el límite inferior al superior.", " Hz"),
      arith("Cada 10 dB más equivale a 10 veces más energía. ¿Cuántas veces más energía tiene un sonido de 85 dB que uno de 65 dB?", "10*10", "Hay dos pasos de 10 dB, y cada paso multiplica por 10.", " veces"),
      ("Cuatro fuentes emiten: A, 40 Hz; B, 15.000 Hz; C, 30.000 Hz; D, 10 Hz. ¿Cuáles se pueden oír?", "A y B", "Solo 40 Hz y 15.000 Hz están entre 20 Hz y 20.000 Hz."),
  ],
  rea=[
      ("Camila dice: «Si subo el volumen, el sonido se hace más agudo». ¿Qué corrección es correcta? A) El volumen cambia la amplitud o intensidad; el tono depende de la frecuencia B) Es correcto, porque más energía siempre da más frecuencia", "A", "Tono e intensidad son cualidades distintas."),
      ("Alguien usa audífonos a 100 dB varias horas al día. ¿Qué consecuencia es posible? A) Daño permanente en las células ciliadas B) Molestia que desaparece siempre sin dejar daño", "A", "Sobre 85 dB y por tiempo prolongado el daño no se recupera."),
  ],
  cha=[
      arith("Un sonido de 20 Hz tiene 20 vibraciones por segundo. ¿Cuántas vibraciones hay en 1 minuto?", "20*60", "Un minuto tiene 60 segundos."),
      arith("Un taladro cercano produce 100 dB y una biblioteca silenciosa 40 dB. Cada 10 dB equivale a 10 veces más energía. ¿Cuántas veces más energía tiene el sonido del taladro?", "10*10*10*10*10*10", "Hay 60 dB de diferencia, es decir, seis pasos de 10 dB.", " veces"),
  ],
  context=[arith("Una persona oye música a 95 dB con audífonos. Como referencia, sobre 85 dB conviene limitar la exposición. ¿Cuántos decibeles sobre esa referencia está?", "95-85", "Se resta la referencia al nivel de la música: conviene bajar el volumen.", " dB")],
  selfcheck=[("¿Qué rango de frecuencias oye una persona joven con audición sana?", "De 20 Hz a 20.000 Hz", "Es el rango audible."), ("¿Qué cualidad del sonido se relaciona con la frecuencia?", "El tono", "Mayor frecuencia, tono más agudo."), ("¿Qué le puede pasar a la cóclea con ruido intenso prolongado?", "Se dañan sus células ciliadas", "El daño no se recupera.")],
  open_task=task("Datos de ejemplo de niveles de sonido: biblioteca, 40 dB; conversación, 60 dB; calle con tráfico, 80 dB; taladro, 100 dB. Dibuja una recta de 0 a 120 dB y ubica los cuatro sonidos. Marca la zona sobre 85 dB como zona de riesgo en exposición prolongada. Escribe tres reglas para cuidar tu audición.", "Los puntos 40, 60 y 80 quedan bajo el límite y el taladro (100 dB) queda en riesgo. Reglas: bajar el volumen de los audífonos, descansar del ruido fuerte y alejarse de fuentes muy intensas.", ["ubica los cuatro sonidos en la recta", "marca la zona sobre 85 dB", "tres reglas coherentes con la evidencia"], ["recta rotulada y tres reglas"], ["poner el taladro bajo 85 dB", "reglas sin relación con la intensidad"], "Pregunta cuánto tiempo cambiaría el riesgo si el sonido baja 10 dB."),
  reinforce="Escribe un ejemplo de infrasonido, uno de ultrasonido y uno audible, con una frecuencia para cada uno.",
  extend="Explica por qué es mejor disminuir el volumen que tapar el ruido con más volumen en los audífonos.")

L(OA, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres comprobar la pupila, usa la luz natural de una ventana y un espejo; nunca apuntes una linterna a los ojos ni mires directamente al Sol.",
  use="Aprenderé cómo el ojo recibe la luz y forma una imagen. Sirve para entender la visión, los colores y por qué a veces vemos borroso.",
  prior=["Sé que una lente convergente forma imágenes reales invertidas.", "Sé que los colores de la luz se mezclan."],
  explain=[
      "La luz entra al ojo por la córnea, una capa transparente que ya refracta los rayos. Pasa por la pupila, una abertura cuyo tamaño regula el iris, la parte coloreada: con mucha luz la pupila se achica y con poca luz se agranda. Luego atraviesa el cristalino, una lente convergente flexible, y el humor vítreo, y forma sobre la retina una imagen real e invertida. El nervio óptico lleva la señal al cerebro, que la interpreta y nos permite percibir el mundo derecho.",
      "La retina tiene células fotorreceptoras. Los bastones son muy sensibles a la luz débil y distinguen luz y sombra, pero no colores. Los conos necesitan más luz y permiten ver colores; hay tres tipos, sensibles al rojo, al verde y al azul, y su combinación produce todos los colores que percibimos. En la zona de la retina donde sale el nervio óptico no hay fotorreceptores: es el punto ciego.",
      "Para enfocar objetos a distintas distancias el ojo hace la acomodación: los músculos ciliares cambian la curvatura del cristalino. Para mirar de cerca el cristalino se abulta y converge más; para mirar de lejos se aplana. Por eso leer mucho rato de cerca cansa la vista.",
  ],
  vocab=[("córnea", "capa transparente del frente del ojo que refracta la luz"), ("pupila", "abertura por donde entra la luz"), ("iris", "parte coloreada del ojo que regula el tamaño de la pupila"), ("cristalino", "lente flexible del ojo que enfoca la luz"), ("retina", "capa del fondo del ojo con células sensibles a la luz"), ("acomodación", "cambio de curvatura del cristalino para enfocar a distintas distancias")],
  worked=[
      ("Ruta de la luz", "Escribe el camino de la luz desde afuera hasta el cerebro.", ["La luz entra por la córnea y atraviesa la pupila.", "El cristalino la enfoca sobre la retina.", "El nervio óptico lleva la señal al cerebro."], "Córnea, pupila, cristalino, retina, nervio óptico, cerebro"),
      ("La pupila", "Entras desde una calle muy soleada a una pieza oscura. ¿Qué pasa con tu pupila?", ["En la oscuridad llega menos luz.", "El iris agranda la pupila para dejar entrar más luz."], "Se agranda"),
  ],
  mistakes=[
      ("Creer que la imagen que se forma en la retina está derecha.", "Se forma invertida; el cerebro la interpreta.", "Recuerda que el cristalino es una lente convergente."),
      ("Pensar que los bastones permiten ver colores.", "Los colores se perciben con conos; los bastones sirven con poca luz.", "Asocia conos con color y bastones con luz débil."),
  ],
  rec=[
      ("¿Qué parte del ojo forma la imagen real?", "La retina", "En ella llegan los rayos enfocados."),
      ("¿Qué estructura regula el tamaño de la pupila?", "El iris", "Ajusta la entrada de luz."),
      ("Verdadero o falso: los bastones permiten ver los colores.", "Falso", "Los colores los detectan los conos."),
  ],
  und=[
      ("El cristalino se comporta como: A) una lente convergente B) un espejo plano", "A", "Refracta los rayos y los hace converger en la retina."),
      ("Sales de un cine oscuro a una calle soleada. ¿Qué hace la pupila? A) Se achica B) Se agranda", "A", "Entra demasiada luz y el iris la reduce."),
      ("¿Qué células permiten ver en un lugar con muy poca luz?", "Los bastones", "Son muy sensibles a la luz débil."),
  ],
  app=[
      arith("Un ojo tiene unos 120 millones de bastones y 6 millones de conos (valores de ejemplo). ¿Cuántos bastones hay por cada cono?", "120/6", "Se divide el número de bastones por el de conos.", " bastones"),
      ("Después de mirar una montaña, lees un libro a 30 cm. ¿Qué hace el cristalino? A) Se abulta B) Se aplana", "A", "Para ver de cerca converge más."),
      ("¿Cómo es la imagen que se forma en la retina? A) Real e invertida B) Virtual y derecha", "A", "El cristalino convergente forma una imagen real sobre la retina."),
  ],
  rea=[
      ("En una pieza casi oscura ves formas grises sin colores. ¿Por qué? A) Hay poca luz y funcionan los bastones, que no distinguen colores B) Los conos desaparecen en la oscuridad", "A", "Los conos necesitan más luz para activarse."),
      ("Una compañera dice que, como la imagen de la retina está invertida, vemos el mundo al revés. ¿Qué respuesta es correcta? A) El cerebro interpreta las señales y percibimos el mundo derecho B) Los ojos giran la imagen antes de verla", "A", "La inversión ocurre en la retina y el cerebro la interpreta."),
  ],
  cha=[
      ("Lees un letrero a 5 m y luego un texto a 25 cm. ¿En qué caso el cristalino está más abultado?", "Al leer el texto a 25 cm", "A menor distancia el cristalino converge más."),
      arith("La pupila mide 2 mm de diámetro con luz intensa y 6 mm en la oscuridad. ¿Cuántas veces es mayor el diámetro en la oscuridad?", "6/2", "Se divide el diámetro mayor por el menor.", " veces"),
  ],
  context=[ex("Un conductor entra a un túnel oscuro y al principio ve muy poco. ¿Por qué? A) La pupila y la retina tardan en adaptarse a la poca luz B) Los ojos dejan de funcionar mientras está en el túnel", "A", "La adaptación a la oscuridad toma un tiempo.")],
  selfcheck=[("¿Qué función cumple el iris?", "Regular el tamaño de la pupila", "Controla cuánta luz entra."), ("¿Qué tres tipos de conos hay?", "Sensibles al rojo, al verde y al azul", "Su combinación produce todos los colores."), ("¿Qué es la acomodación?", "El cambio de curvatura del cristalino para enfocar", "Permite ver nítido a distintas distancias.")],
  open_task=task("Datos de ejemplo del diámetro de la pupila de una persona: con luz de día, 3 mm; en una pieza casi oscura, 7 mm. Dibuja un ojo con las partes: córnea, pupila, iris, cristalino, retina y nervio óptico, y una flecha que muestre el camino de la luz. Explica con los datos qué hace el iris. Si quieres comprobarlo, mira tus ojos en un espejo con luz natural y luego con poca luz (nunca con linterna).", "El dibujo ubica cada parte, con la luz atravesando córnea, pupila y cristalino y llegando a la retina. Con luz de día la pupila mide 3 mm y en la penumbra 7 mm: el iris la agranda para dejar entrar más luz cuando hay poca.", ["seis partes rotuladas", "flecha en el orden correcto", "usa los dos diámetros", "explica el papel del iris"], ["dibujo rotulado y explicación"], ["decir que la pupila se achica en la oscuridad", "poner la retina antes del cristalino"], "Pregunta qué cambiaría si la pupila no pudiera achicarse con mucha luz."),
  reinforce="Escribe las seis partes del ojo por donde pasa la luz hasta el nervio óptico.",
  extend="Explica por qué cuesta ver colores cuando atardece y casi no hay luz.")

L(OA, 4,
  materials="Este cuaderno, regla y calculadora. Todos los datos de longitudes de onda están escritos en los ejercicios.",
  use="Aprenderé qué es el espectro de la luz visible y de qué parte del espectro electromagnético forma parte. Sirve para entender el color, el calor infrarrojo y la radiación ultravioleta.",
  prior=["Sé que la luz blanca se descompone en colores.", "Sé que la longitud de onda y la frecuencia están relacionadas."],
  explain=[
      "La luz es una onda electromagnética: es un campo eléctrico y magnético que se propaga incluso en el vacío. El espectro electromagnético ordena estas ondas por su longitud de onda o frecuencia: ondas de radio, microondas, infrarrojo, luz visible, ultravioleta, rayos X y rayos gamma. La luz visible es solo una parte pequeña: va aproximadamente de 400 nm a 700 nm, donde un nanómetro (nm) es una milmillonésima de metro.",
      "Dentro de la luz visible, el violeta tiene la longitud de onda más corta (unos 400 nm) y el rojo la más larga (unos 700 nm). Pasando por azul, verde, amarillo y naranjo, la longitud de onda aumenta. En el vacío todas las ondas electromagnéticas viajan a la misma rapidez, de modo que si la longitud de onda es mayor la frecuencia es menor. Así, el violeta tiene más frecuencia que el rojo.",
      "Fuera de lo visible hay radiaciones con efectos importantes. La radiación infrarroja tiene longitud de onda mayor que el rojo y la sentimos como calor; la usan los controles remotos y las cámaras térmicas. La radiación ultravioleta (UV) tiene longitud de onda menor que el violeta y puede quemar la piel y dañar los ojos, por eso se usan protector solar y lentes con filtro UV. Parte del UV atraviesa las nubes.",
  ],
  vocab=[("onda electromagnética", "onda formada por campos eléctrico y magnético que viaja incluso en el vacío"), ("espectro electromagnético", "conjunto de todas las ondas electromagnéticas ordenadas por longitud de onda"), ("nanómetro (nm)", "una milmillonésima de metro"), ("infrarrojo", "radiación con longitud de onda mayor que la del rojo"), ("ultravioleta (UV)", "radiación con longitud de onda menor que la del violeta"), ("luz visible", "radiación que percibe el ojo, de unos 400 nm a 700 nm")],
  worked=[
      ("¿Es visible?", "Se tienen tres luces: 500 nm, 900 nm y 300 nm. ¿Cuáles son visibles?", ["Comparo con el rango visible de 400 nm a 700 nm.", "500 nm está dentro; 900 nm está sobre 700 nm; 300 nm está bajo 400 nm."], "Solo la de 500 nm"),
      ("Ordenar por frecuencia", "Ordena de menor a mayor frecuencia las luces de 650 nm, 550 nm y 420 nm.", ["Mayor longitud de onda significa menor frecuencia.", "Ordeno las longitudes de mayor a menor: 650, 550, 420."], "650 nm, 550 nm, 420 nm"),
  ],
  mistakes=[
      ("Creer que el infrarrojo no existe porque no se ve.", "Se detecta con sensores y lo sentimos como calor.", "Recuerda que el ojo solo percibe una parte del espectro."),
      ("Pensar que el rojo tiene la mayor frecuencia de la luz visible.", "El rojo tiene la mayor longitud de onda y la menor frecuencia.", "Relaciona longitud de onda y frecuencia de forma inversa."),
  ],
  rec=[
      ("¿Qué radiación tiene mayor longitud de onda que la luz roja?", "El infrarrojo", "Está al lado del rojo, fuera de lo visible."),
      ("¿En qué unidad se expresa la longitud de onda de la luz visible?", "En nanómetros", "Un nanómetro es una milmillonésima de metro."),
      ("Verdadero o falso: la luz visible es una parte pequeña del espectro electromagnético.", "Verdadero", "Va solo de unos 400 nm a 700 nm."),
  ],
  und=[
      ("¿Qué color visible tiene mayor frecuencia?", "El violeta", "Tiene la menor longitud de onda del rango visible."),
      ("Un control remoto emite luz infrarroja de 940 nm y no ves el destello. ¿Por qué? A) 940 nm supera el rango visible B) El destello es demasiado débil", "A", "Más de 700 nm está fuera del rango que percibe el ojo."),
      ("La radiación ultravioleta tiene: A) longitud de onda menor que el violeta B) longitud de onda mayor que el rojo", "A", "El UV está después del violeta, hacia longitudes de onda más cortas."),
  ],
  app=[
      arith("El rango visible va de 400 nm a 700 nm. ¿Cuántos nanómetros abarca?", "700-400", "Se resta el límite inferior al superior.", " nm"),
      ("Tres luces tienen longitudes de onda de 480 nm, 530 nm y 610 nm. ¿Cuál tiene la menor frecuencia?", "La de 610 nm", "La mayor longitud de onda tiene la menor frecuencia."),
      ("Usa estos límites: ultravioleta, menos de 400 nm; visible, de 400 nm a 700 nm; infrarrojo, más de 700 nm. ¿A qué región pertenece una radiación de 300 nm?", "Ultravioleta", "300 nm es menor que 400 nm."),
  ],
  rea=[
      ("Un estudiante dice: «El infrarrojo no existe porque no se ve». ¿Qué respuesta es correcta? A) Existe: se detecta con sensores y se siente como calor B) Tiene razón, porque lo que no se ve no se puede medir", "A", "Una radiación puede existir y medirse aunque el ojo no la perciba."),
      ("Dos luces A y B viajan en el vacío. A mide 500 nm y B mide 600 nm. ¿Cuál tiene mayor frecuencia?", "A", "Con igual rapidez, menor longitud de onda significa mayor frecuencia."),
  ],
  cha=[
      arith("Una radiación infrarroja mide 1.200 nm. ¿Cuántos nanómetros supera el límite rojo de la luz visible (700 nm)?", "1200-700", "Se resta el límite rojo a la longitud de onda.", " nm"),
      ("Dos luces viajan en el vacío. Una tiene longitud de onda 400 nm y frecuencia F; la otra tiene 800 nm. ¿Qué frecuencia tiene la segunda?", "La mitad de F", "La longitud de onda es el doble, así que la frecuencia es la mitad."),
  ],
  context=[ex("Es un día nublado de verano. ¿Puedes recibir radiación UV suficiente para quemarte? A) Sí, porque parte del UV atraviesa las nubes B) No, porque las nubes detienen todo el UV", "A", "Las nubes reducen pero no eliminan el UV; conviene usar protección.")],
  selfcheck=[("¿Qué rango tiene la luz visible?", "De unos 400 nm a 700 nm", "Es una parte pequeña del espectro."), ("¿Qué color tiene la mayor longitud de onda visible?", "El rojo", "Está en el extremo de unos 700 nm."), ("¿Qué radiación puede quemar la piel?", "La ultravioleta", "Tiene energía suficiente para dañar la piel.")],
  open_task=task("Ordena de mayor a menor longitud de onda estas radiaciones: ondas de radio, microondas, infrarrojo, luz visible, ultravioleta, rayos X. Asocia cada una con un uso o efecto: control remoto, bronceado, radiografía, radio de auto, horno de microondas, ver colores. Escribe una frase que explique por qué no vemos el infrarrojo.", "Orden: radio, microondas, infrarrojo, visible, ultravioleta, rayos X. Usos: radio de auto con ondas de radio, horno con microondas, control remoto con infrarrojo, ver colores con luz visible, bronceado con ultravioleta, radiografía con rayos X. No vemos el infrarrojo porque los conos del ojo solo responden a unos 400 nm a 700 nm.", ["orden correcto de las seis radiaciones", "seis asociaciones correctas", "explica el límite del ojo"], ["lista ordenada y tabla de usos"], ["ordenar por frecuencia en vez de longitud de onda", "poner el UV antes del infrarrojo"], "Pregunta qué instrumento permitiría ver el infrarrojo."),
  reinforce="Escribe el color visible con menor frecuencia y el de mayor frecuencia.",
  extend="Explica por qué los lentes de sol con filtro UV protegen los ojos aunque no cambien mucho lo que ves.")

L(OA, 5,
  materials="Este cuaderno, lápiz y calculadora. Todos los casos están escritos en los ejercicios; no necesitas pruebas ni instrumentos.",
  use="Aprenderé qué defectos pueden tener la visión y la audición y cómo los corrigen los lentes y los audífonos. Sirve para entender la tecnología correctiva y sus consecuencias sociales.",
  prior=["Sé cómo funcionan el ojo y el oído.", "Sé que las lentes convergentes y divergentes desvían la luz de forma distinta."],
  explain=[
      "En la miopía la imagen de los objetos lejanos se forma delante de la retina, por eso se ve borroso de lejos; se corrige con una lente divergente. En la hipermetropía la imagen se forma detrás de la retina, por eso cuesta ver de cerca; se corrige con una lente convergente. En el astigmatismo la córnea tiene una curvatura irregular y la imagen se ve borrosa a cualquier distancia. En la presbicia, que aparece con la edad, el cristalino pierde flexibilidad y cuesta ver de cerca. El daltonismo es una alteración de los conos que dificulta distinguir ciertos colores, sobre todo rojo y verde; los lentes comunes no lo corrigen.",
      "La hipoacusia es la pérdida parcial o total de la audición. Puede deberse a la edad, a infecciones o a daño por ruido en las células ciliadas. Un audífono tiene un micrófono que capta el sonido, un amplificador que aumenta su intensidad y un parlante pequeño que lo entrega al oído; no repara las células dañadas. En casos graves, el implante coclear estimula directamente el nervio auditivo. La lengua de señas y los subtítulos son apoyos para la comunicación.",
      "Ver y oír bien influye en el aprendizaje, la seguridad y el trabajo. Los lentes y los audífonos tienen un costo, por eso es importante el acceso a controles de salud y a programas públicos. Un diseño inclusivo ayuda a todas las personas: señalética que no dependa solo del color, subtítulos en videos y avisos visuales además de sonoros.",
  ],
  vocab=[("miopía", "defecto en que se ve borroso de lejos, por una imagen formada delante de la retina"), ("hipermetropía", "defecto en que se ve borroso de cerca, por una imagen formada detrás de la retina"), ("astigmatismo", "visión borrosa por una córnea de curvatura irregular"), ("presbicia", "dificultad para ver de cerca por pérdida de flexibilidad del cristalino"), ("daltonismo", "alteración de los conos que dificulta distinguir algunos colores"), ("hipoacusia", "pérdida parcial o total de la audición")],
  worked=[
      ("Identificar la miopía", "Una persona ve nítido el cuaderno a 20 cm, pero borroso el pizarrón. ¿Qué defecto tiene y qué lente lo corrige?", ["Ve mal de lejos y bien de cerca.", "La imagen lejana cae delante de la retina: miopía.", "Una lente divergente la desplaza hacia atrás."], "Miopía; lente divergente"),
      ("Partes de un audífono", "Un audífono recibe un sonido débil y lo entrega más fuerte. ¿Qué parte lo aumenta?", ["El micrófono solo capta el sonido.", "El parlante solo lo entrega.", "El amplificador aumenta la intensidad."], "El amplificador"),
  ],
  mistakes=[
      ("Creer que el audífono repara las células ciliadas.", "Solo amplifica el sonido; las células dañadas no se recuperan.", "Distingue entre ayuda tecnológica y recuperación del daño."),
      ("Pensar que unos lentes comunes corrigen el daltonismo.", "El daltonismo se debe a los conos, no a la forma del ojo.", "Revisa si el problema es de enfoque o de percepción del color."),
  ],
  rec=[
      ("¿Qué tipo de lente corrige la miopía?", "Divergente", "Retrasa el punto donde se enfocan los rayos."),
      ("Verdadero o falso: el audífono repara las células ciliadas dañadas.", "Falso", "Solo amplifica el sonido."),
      ("En la presbicia pierde flexibilidad el ______ (cristalino o tímpano).", "Cristalino", "Por eso cuesta enfocar de cerca."),
  ],
  und=[
      ("Si la imagen se forma delante de la retina, la persona tiene: A) miopía B) hipermetropía", "A", "El enfoque queda demasiado adelante."),
      ("¿Qué parte del ojo está alterada en el daltonismo?", "Los conos", "Son las células que distinguen los colores."),
      ("¿Qué parte del audífono aumenta la intensidad del sonido?", "El amplificador", "El micrófono capta y el parlante entrega."),
  ],
  app=[
      ("Luis ve nítido el pizarrón del fondo de la sala, pero el texto a 20 cm lo ve borroso desde niño. ¿Qué defecto es el más probable?", "Hipermetropía", "Ve mal de cerca y bien de lejos desde la infancia."),
      ("Una persona de 50 años aleja el libro para leer, y antes veía bien de cerca. ¿Qué es lo más probable?", "Presbicia", "El cristalino pierde flexibilidad con la edad."),
      arith("En un control de ejemplo de un colegio con 480 estudiantes, 1 de cada 4 necesita lentes. ¿Cuántos estudiantes necesitan lentes?", "480/4", "Se divide el total por 4.", " estudiantes"),
  ],
  rea=[
      ("Un mapa de metro de ejemplo diferencia dos líneas solo con rojo y verde. ¿Qué mejora ayuda a personas con daltonismo? A) Agregar un símbolo o nombre a cada línea B) Usar un rojo más intenso", "A", "El diseño no debe depender solo del color."),
      ("¿Qué dispositivo estimula directamente el nervio auditivo en casos graves de hipoacusia?", "El implante coclear", "A diferencia del audífono, no amplifica el sonido para el oído."),
  ],
  cha=[
      ("Una niña de 12 años usa lentes convergentes para ver de cerca. ¿Cuál es el defecto más probable: miopía o hipermetropía?", "Hipermetropía", "Los lentes convergentes se usan cuando la imagen se forma detrás de la retina."),
      arith("Unos lentes cuestan $30.000 (valor de ejemplo). Una persona ahorra $5.000 al mes. ¿Cuántos meses necesita para reunir ese monto?", "30000/5000", "Se divide el costo por el ahorro mensual.", " meses"),
  ],
  context=[ex("Un compañero entrecierra los ojos para ver el pizarrón y se acerca mucho a la pantalla. ¿Qué es lo más útil? A) Sugerirle que converse con una persona adulta de su casa o del colegio para un control con especialista B) Decirle que ponga más atención", "A", "Un especialista puede evaluar si necesita lentes.")],
  selfcheck=[("¿Cuál es la diferencia entre miopía e hipermetropía?", "En la miopía se ve mal de lejos y en la hipermetropía de cerca", "La imagen cae delante o detrás de la retina."), ("¿Qué hace un audífono?", "Capta el sonido, lo amplifica y lo entrega al oído", "No repara las células dañadas."), ("¿Por qué es útil el diseño inclusivo?", "Porque permite que más personas accedan a la información", "Subtítulos y símbolos ayudan a todas las personas.")],
  open_task=task("Para cada caso, escribe el defecto o situación probable, la ayuda posible y una mejora de diseño inclusivo: (1) ve borroso de lejos y bien de cerca; (2) ve borroso de cerca y bien de lejos desde niña; (3) confunde rojo y verde en láminas escolares; (4) no oye bien las voces agudas y sube mucho el volumen de la tele; (5) tiene hipoacusia y debe comunicarse en un curso. Escribe además una consecuencia social de no tener acceso a lentes o audífonos.", "1 miopía, lente divergente, pizarra con letras grandes. 2 hipermetropía, lente convergente, textos con buen tamaño. 3 daltonismo, los lentes comunes no lo corrigen, láminas con símbolos. 4 hipoacusia, audífono, subtítulos. 5 hipoacusia, audífono o apoyo de lengua de señas, subtítulos. Consecuencia: puede afectar el aprendizaje y la seguridad.", ["cinco casos con defecto", "cinco ayudas coherentes", "una mejora de diseño inclusivo", "una consecuencia social"], ["tabla de cinco filas y una frase"], ["proponer lentes comunes para el daltonismo", "olvidar la consecuencia social"], "Pregunta cómo se podría mejorar el acceso a controles de salud en el colegio."),
  reinforce="Escribe cuál lente corrige la miopía y cuál la hipermetropía.",
  extend="Explica por qué un audífono no devuelve la audición original de una persona con células ciliadas dañadas.")
