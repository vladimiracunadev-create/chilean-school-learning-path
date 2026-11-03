"""Cuaderno del estudiante, 8.º básico Ciencias Naturales: OA 09 (tecnologías de generación eléctrica)."""
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


OA9 = "CN08 OA 09"

L(OA9, 1,
  materials="Este cuaderno y lápiz. Opcional: una calculadora con panel solar pequeño y una linterna a pilas. Nunca abras pilas ni las calientes, y no hagas experimentos con enchufes.",
  use="Aprenderé cómo se genera energía eléctrica en pilas, paneles fotovoltaicos y generadores, y a plantear preguntas investigables sobre ellos. Sirve para entender de dónde viene la electricidad que usamos.",
  prior=["Sé que la energía se transforma de una forma a otra.", "Sé distinguir variable independiente y dependiente."],
  explain=[
      "La energía eléctrica no se crea: se obtiene transformando otras formas de energía. Una pila o batería transforma energía química en eléctrica, gracias a una reacción química entre sus materiales. Un panel fotovoltaico transforma la energía de la luz en eléctrica. Un generador transforma energía de movimiento en eléctrica: en su interior, un imán gira cerca de una bobina de cable y produce corriente.",
      "Lo que hace girar al generador puede ser el viento (central eólica), el agua que cae o fluye (hidroeléctrica) o el vapor de agua. El vapor se obtiene al calentar agua con la energía de un combustible o con la fisión del uranio en una central nuclear. En todos los casos, una turbina (una rueda con aspas) gira y mueve al generador.",
      "Una pregunta investigable sobre un panel solar es: «¿Sigue mostrando números una calculadora solar cuando se cubre la mitad de su panel?». Se cambia la parte del panel cubierta y se mide si funciona. «¿Cuál tecnología es la más linda?» no es investigable, porque depende de gustos y no de datos.",
  ],
  vocab=[("pila", "dispositivo que transforma energía química en eléctrica"), ("panel fotovoltaico", "dispositivo que transforma luz en energía eléctrica"), ("generador", "dispositivo que transforma movimiento en energía eléctrica"), ("turbina", "rueda con aspas que gira al recibir viento, agua o vapor"), ("fisión nuclear", "división de núcleos de uranio que libera mucho calor")],
  worked=[
      ("Qué transformación ocurre", "¿Qué transformación de energía ocurre en una pila?", ["La pila guarda energía en sus materiales químicos.", "Al conectarse, la transforma en energía eléctrica."], "De energía química a energía eléctrica"),
      ("Pregunta investigable", "¿Es investigable «¿Funciona una calculadora solar con la mitad del panel cubierta?»?", ["Pregunto si se puede observar.", "Se observa si la pantalla sigue mostrando números."], "Sí, porque se observa la pantalla"),
  ],
  mistakes=[
      ("Creer que una pila «guarda electricidad».", "Guarda energía química que se transforma en eléctrica al conectarla.", "Piensa en la reacción química."),
      ("Decir que el panel solar funciona igual de noche.", "Necesita luz; de noche casi no produce.", "Recuerda que transforma la luz."),
  ],
  rec=[
      ("¿Qué transforma un panel fotovoltaico: la luz o el sonido?", "La luz", "La luz se convierte en energía eléctrica."),
      ("¿Qué fuente mueve las aspas de una central eólica: el viento o el agua?", "El viento", "Es la fuente de energía del generador."),
      ("Verdadero o falso: una turbina es una rueda con aspas que gira.", "Verdadero", "Mueve al generador."),
  ],
  und=[
      ("¿Cuál es una pregunta investigable? A) ¿Cuánto tiempo enciende una linterna con pilas nuevas? B) ¿Cuál tecnología es la más linda?", "A", "Se contesta midiendo el tiempo."),
      ("En una central hidroeléctrica, ¿qué mueve la turbina?", "El agua", "El agua que cae o fluye hace girar las aspas."),
      ("¿De dónde viene el calor que produce el vapor en una central nuclear? A) De la fisión del uranio; B) De una pila.", "A", "La fisión libera mucho calor."),
  ],
  app=[
      ("En «¿Funciona la calculadora con la mitad del panel cubierta?», ¿qué variable se cambia?", "La parte del panel cubierta", "Es lo que difiere entre las pruebas."),
      ("En esa misma pregunta, ¿qué variable se observa?", "Si la pantalla sigue mostrando números", "Es el resultado que se registra."),
      arith("Una linterna usa 3 pilas. Una caja de ejemplo trae 12 pilas. ¿Cuántas linternas se pueden equipar con la caja?", "12//3", "Se divide el total de pilas por las que usa cada linterna."),
  ],
  rea=[
      ("Alguien dice: «La pila guarda electricidad, como un balde guarda agua». ¿Qué corrección haces? A) Guarda energía química que se transforma en eléctrica; B) No guarda ninguna energía.", "A", "La reacción química es la fuente."),
      ("¿Por qué un panel solar produce muy poco de noche? Responde en una frase.", "Porque no recibe luz y transforma la luz", "Su fuente de energía es la luz."),
  ],
  cha=[
      ("Si se cubre la mitad de un panel solar de ejemplo, ¿qué se espera que ocurra con la energía que produce? A) Disminuye; B) Aumenta.", "A", "Recibe menos luz."),
      ("¿Cuál es la mejor forma investigable de «¿Sirven las pilas?»? A) ¿Cuántas horas enciende una linterna una pila nueva y una pila usada? B) ¿Son útiles las pilas?", "A", "Indica qué se mide."),
  ],
  context=[arith("Un colegio de ejemplo instala 20 paneles y cada uno produce 2 unidades de energía por hora al mediodía. ¿Cuántas unidades producen entre todos en una hora?", "20*2", "Se multiplica el número de paneles por lo que produce cada uno.")],
  selfcheck=[("¿Qué transforma una pila?", "Energía química en eléctrica", "Por una reacción química."), ("¿Qué transforma un generador?", "Movimiento en energía eléctrica", "Gira un imán cerca de una bobina."), ("¿Qué hace una turbina?", "Gira con el viento, el agua o el vapor y mueve al generador", "Recibe la energía del fluido.")],
  open_task=task("Completa una tabla con cuatro tecnologías (pila, panel fotovoltaico, central eólica, central hidroeléctrica): de qué forma de energía parte cada una y cómo llega a ser eléctrica. Después escribe una pregunta investigable sobre un panel solar de calculadora.", "Pila: energía química por reacción. Panel: luz transformada. Eólica: viento mueve turbina y generador. Hidroeléctrica: agua mueve turbina y generador. Pregunta: ¿Cuántos centímetros del panel se pueden cubrir sin que se apague la calculadora?", ["cuatro filas correctas", "usa transformación de energía", "pregunta con algo que se observa o mide"], ["tabla y pregunta"], ["decir que la pila guarda electricidad", "pregunta de opinión"], "Pregunta qué cambiaría con una luz más débil."),
  reinforce="Escribe una fuente que puede mover una turbina.",
  extend="Explica por qué se dice que la energía no se crea, sino que se transforma.")

L(OA9, 2,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo y están escritas en cada ejercicio.",
  use="Aprenderé a examinar tablas de generación y de funcionamiento de pilas, paneles y turbinas para sacar conclusiones. Sirve para leer evidencia de producción de energía.",
  prior=["Sé qué transformaciones ocurren en cada tecnología.", "Sé leer tablas y calcular diferencias."],
  explain=[
      "Las tablas de producción muestran cuánta energía entrega una tecnología en distintas condiciones. Datos de ejemplo de un panel solar a lo largo del día, en unidades de energía por hora: 8 h, 2; 10 h, 6; 12 h, 9; 14 h, 8; 16 h, 4; 18 h, 1. El patrón es que produce más cuando el sol está alto y casi nada cuando oscurece.",
      "Otra evidencia son los datos de pilas. Una pila de linterna de 1,5 V alimenta una ampolleta pequeña por ciertas horas. Dos pilas conectadas una a continuación de la otra entregan 3 V en total. Con tablas se calcula cuánta energía entrega cada tecnología en un tiempo: se suman los valores por hora.",
      "Al examinar evidencia hay que distinguir el dato (a las 12 h hay 9 unidades) de la interpretación (el sol está más alto), indicar el dato decisivo y declarar una limitación: un solo día no basta para saber el rendimiento de un año. También es importante comparar con la misma unidad.",
  ],
  vocab=[("producción de energía", "cantidad de energía eléctrica que entrega una tecnología"), ("volt (V)", "unidad de la diferencia de potencial eléctrico de una pila"), ("patrón", "regularidad que se observa en los datos"), ("interpretación", "explicación que se da a un dato"), ("unidad de medida", "magnitud con que se expresa un dato")],
  worked=[
      ("Hora de máxima producción", "Un panel produce 3, 7, 10, 8 y 2 unidades a las 8, 10, 12, 14 y 16 h. ¿A qué hora produce más?", ["Busco el mayor valor: 10.", "Corresponde a las 12 h."], "A las 12 h"),
      ("Total del día", "Un panel produce 3, 7, 10, 8 y 2 unidades en esas horas. ¿Cuánto produjo en total?", ["Sumo: 3 + 7 + 10 + 8 + 2.", "El total es 30."], "30 unidades"),
  ],
  mistakes=[
      ("Mezclar unidades distintas al comparar.", "No se pueden comparar unidades por hora con unidades por día.", "Revisa la unidad."),
      ("Concluir sobre un año con un solo día de datos.", "Una muestra pequeña no representa a todo el año.", "Declara la limitación."),
  ],
  rec=[
      ("En la tabla del panel de ejemplo, ¿a qué hora produce más: a las 8 h o a las 12 h?", "A las 12 h", "Tiene el valor mayor, 9 unidades."),
      ("¿Qué unidad mide la diferencia de potencial de una pila: el volt o el metro?", "El volt", "El volt (V) mide la diferencia de potencial."),
      ("Verdadero o falso: un panel solar produce más cuando el sol está alto.", "Verdadero", "Recibe más luz."),
  ],
  und=[
      ("¿Qué patrón muestra la tabla del panel de ejemplo? A) Sube hasta el mediodía y luego baja; B) Es constante.", "A", "Los valores son 2, 6, 9, 8, 4, 1."),
      ("Un dato dice «9 unidades a las 12 h». ¿Cuál es una interpretación? A) El sol está más alto a esa hora; B) La hora es las 12.", "A", "La interpretación explica el dato."),
      ("¿Por qué conviene anotar la unidad de cada dato?", "Para poder comparar valores equivalentes", "No se comparan unidades distintas."),
  ],
  app=[
      arith("Con los datos del panel de ejemplo (2, 6, 9, 8, 4 y 1 unidades por hora), ¿cuántas unidades produjo en total entre las 8 h y las 18 h, en esos seis registros?", "2+6+9+8+4+1", "Se suman los seis valores."),
      arith("Una pila de ejemplo alimenta una ampolleta 8 horas. Otra, 5 horas. ¿Cuántas horas más dura la primera?", "8-5", "Se resta la duración menor a la mayor."),
      arith("Una pila de ejemplo entrega 3 V. Si se conectan tres pilas iguales una a continuación de la otra, ¿cuántos volts entregan en total?", "3*3", "Se suman los voltajes de las pilas conectadas una a continuación de la otra."),
  ],
  rea=[
      ("Alguien concluye: «Como a las 12 h hay más producción, el panel produce igual todo el año». ¿Qué falla tiene? A) Generaliza con datos de un solo día; B) Los paneles no producen.", "A", "Falta evidencia de otras estaciones."),
      ("Explica en una frase por qué no se pueden comparar «unidades por hora» con «unidades por día».", "Porque son unidades de tiempo distintas", "Hay que expresar ambas en la misma unidad."),
  ],
  cha=[
      ("Datos de ejemplo: un día nublado el panel produjo 1, 2, 3, 2 y 1 unidades a las 8, 10, 12, 14 y 16 h. ¿Cuántas unidades menos produjo a las 12 h que el día de la tabla (9)?", "6", "9 − 3 = 6.", "9-3"),
      ("Con esos datos, ¿qué factor explica la diferencia entre el día soleado y el nublado? A) La cantidad de luz que llega al panel; B) La hora del reloj.", "A", "El panel transforma la luz."),
  ],
  context=[("Un liceo de ejemplo mide su panel un día: de 10 a 14 h produjo 6, 9, 8 unidades por hora a las 10, 12 y 14 h. ¿Cuántas unidades produjo en esas tres mediciones?", "23", "6 + 9 + 8 = 23.", "6+9+8")],
  selfcheck=[("¿Cuándo produce más un panel solar?", "Cuando el sol está más alto", "Recibe más luz."), ("¿Qué distingue un dato de una interpretación?", "El dato se mide y la interpretación lo explica", "Se separan para no exagerar."), ("¿Por qué un solo día no basta?", "Porque no representa todo el año", "Es una limitación.")],
  open_task=task("Con la tabla de ejemplo del panel solar (8 h, 2; 10 h, 6; 12 h, 9; 14 h, 8; 16 h, 4; 18 h, 1) responde: ¿a qué hora produce más?, ¿cuántas unidades produce en total?, ¿en qué horas produce menos de 3 unidades? Escribe una interpretación y una limitación.", "Más: 12 h. Total: 30 unidades. Menos de 3: 8 h y 18 h. Interpretación: produce más cuando el sol está más alto. Limitación: es un solo día.", ["tres respuestas correctas", "interpretación coherente", "una limitación"], ["respuestas y frases"], ["confundir el dato con la interpretación", "olvidar la limitación"], "Pregunta qué cambiaría en un día nublado."),
  reinforce="Escribe a qué hora produce más el panel de la tabla de ejemplo.",
  extend="Explica por qué es importante usar la misma unidad al comparar datos.")

L(OA9, 3,
  materials="Este cuaderno y lápiz. Los esquemas están descritos con palabras.",
  use="Aprenderé a construir un modelo de la cadena de transformaciones de energía en una central y en un generador, y a contrastarlo. Sirve para explicar cómo llega la electricidad a un hogar.",
  prior=["Sé qué hace una turbina.", "Sé que un imán que gira cerca de una bobina produce corriente."],
  explain=[
      "Una central eléctrica se puede modelar como una cadena de transformaciones. En una eólica: viento (energía de movimiento) hace girar la turbina; la turbina mueve al generador; el generador produce energía eléctrica. En una hidroeléctrica: agua en movimiento, turbina, generador. En una central térmica o nuclear: calor, vapor de agua, turbina, generador.",
      "En el generador, la electricidad se produce por inducción electromagnética: cuando un imán gira cerca de una bobina (cable enrollado), aparece una corriente en ella. Mientras más rápido gira el imán, más energía se produce. Después, la energía eléctrica se transporta por cables a casas y colegios. En la cadena siempre hay pérdidas en forma de calor.",
      "El modelo simplifica y tiene límites: no muestra pérdidas ni el efecto sobre el ambiente. Al contrastarlo se pueden comparar tecnologías: por ejemplo, la eólica y la hidroeléctrica no usan combustible; la termoeléctrica sí. Un modelo es útil si permite predecir qué pasa al cambiar un elemento: sin viento, la turbina no gira y no hay producción.",
  ],
  vocab=[("inducción electromagnética", "producción de corriente por el movimiento de un imán cerca de una bobina"), ("bobina", "cable enrollado muchas veces"), ("central térmica", "central que usa calor para producir vapor"), ("pérdida de energía", "parte de la energía que pasa como calor y no es útil"), ("cadena de transformaciones", "serie de pasos en que la energía cambia de forma")],
  worked=[
      ("Orden en una eólica", "En una central eólica, ¿qué pasa después de que el viento mueve las aspas?", ["Las aspas giran la turbina.", "La turbina mueve el generador, que produce energía eléctrica."], "Se mueve el generador y se produce energía eléctrica"),
      ("Predecir con el modelo", "Si no hay viento, ¿qué predice el modelo de la central eólica?", ["Sin viento, la turbina no gira.", "Sin giro, el generador no produce."], "No hay producción de energía"),
  ],
  mistakes=[
      ("Creer que el generador es una fuente de energía.", "Solo transforma energía de movimiento en eléctrica.", "Identifica de dónde viene el movimiento."),
      ("Pensar que no hay pérdidas en la cadena.", "Siempre parte de la energía pasa como calor.", "Agrega las pérdidas al modelo."),
  ],
  rec=[
      ("¿Qué se mueve cerca de una bobina en un generador: un imán o un vidrio?", "Un imán", "Su movimiento produce corriente."),
      ("En una central hidroeléctrica, ¿qué mueve la turbina?", "El agua", "El agua en movimiento hace girar las aspas."),
      ("Verdadero o falso: en la cadena de transformaciones hay pérdidas en forma de calor.", "Verdadero", "Parte de la energía no se aprovecha."),
  ],
  und=[
      ("¿Qué produce la corriente en un generador? A) El movimiento de un imán cerca de una bobina; B) El calor de una ampolleta.", "A", "Es la inducción electromagnética."),
      ("¿Qué combustible quema una central eólica? A) Ninguno, usa el viento; B) Carbón.", "A", "El viento mueve las aspas."),
      ("¿Qué paso tienen en común las centrales eólica, hidroeléctrica y térmica?", "Una turbina que mueve un generador", "En todas gira la turbina."),
  ],
  app=[
      ("Cadena de transformaciones de una central nuclear: fisión del uranio, calor, vapor, turbina, generador. ¿Cuántos pasos hay antes de llegar al generador?", "4", "Fisión, calor, vapor y turbina."),
      ("Un generador de ejemplo gira a 50 vueltas por segundo y otro a 25. ¿Cuál produce más energía, si todo lo demás es igual? A) El primero; B) El segundo.", "A", "A mayor velocidad de giro, más energía."),
      arith("Una central de ejemplo recibe 100 unidades de energía y entrega 40 como electricidad. ¿Cuántas unidades se pierden como calor?", "100-40", "Se resta la energía útil a la total."),
  ],
  rea=[
      ("Alguien afirma: «Con un generador se puede producir electricidad sin ninguna fuente». ¿Qué corrección haces? A) Necesita algo que lo mueva, como viento o agua; B) No necesita nada.", "A", "El generador solo transforma movimiento."),
      ("Un compañero dice que el modelo de la central no sirve porque no muestra el ambiente. ¿Qué respuesta es más completa?", "El modelo muestra las transformaciones, y el ambiente se agrega con otros criterios", "Todo modelo simplifica y se completa con otros análisis."),
  ],
  cha=[
      arith("Una central de ejemplo recibe 200 unidades y entrega 80 como electricidad. ¿Qué porcentaje de la energía recibida entrega como electricidad?", "80*100//200", "Se divide la energía útil por la total y se multiplica por 100.", " %"),
      ("Entre una central eólica, una hidroeléctrica y una a carbón, ¿cuál necesita quemar un combustible? Escribe cuál.", "La central a carbón", "Quema carbón para calentar agua y producir vapor."),
  ],
  context=[("En un cerro de ejemplo hay una central eólica con 12 aspas grandes. Una tarde sin viento no se mueven. ¿Qué predice el modelo para esa tarde?", "No hay producción", "Sin viento no gira la turbina.")],
  selfcheck=[("¿Cómo produce corriente un generador?", "Un imán se mueve cerca de una bobina", "Es la inducción electromagnética."), ("¿Qué pasos tienen en común muchas centrales?", "Una turbina que mueve un generador", "Cambia lo que mueve la turbina."), ("¿Qué pasa con parte de la energía?", "Se pierde como calor", "No es útil.")],
  open_task=task("Dibuja o describe una cadena de transformaciones para dos centrales de tu elección entre eólica, hidroeléctrica y nuclear. Escribe los pasos con flechas, una predicción si falta la fuente y una limitación del modelo.", "Hidroeléctrica: agua en movimiento, turbina, generador, electricidad. Nuclear: fisión, calor, vapor, turbina, generador, electricidad. Si falta el agua, no hay producción. Limitación: el modelo no muestra las pérdidas.", ["dos cadenas correctas", "una predicción", "una limitación"], ["dos cadenas y frases"], ["omitir la turbina", "olvidar la limitación"], "Pregunta qué paso sería el más difícil de reemplazar."),
  reinforce="Escribe la cadena de transformaciones de una central eólica.",
  extend="Explica por qué todas las centrales con generador necesitan algo que lo mueva.")

L(OA9, 4,
  materials="Este cuaderno y lápiz. Los datos son de ejemplo.",
  use="Aprenderé a relacionar variables de la generación eléctrica: velocidad del viento, caída del agua, cantidad de luz y número de pilas. Sirve para predecir cuánta energía entrega cada tecnología.",
  prior=["Sé cómo funciona cada tecnología.", "Sé calcular proporciones y diferencias."],
  explain=[
      "En la energía eólica, mientras más rápido sopla el viento, mayor es la energía que produce la turbina. La relación no es proporcional sino que crece muy rápido. Datos de ejemplo de una turbina: con viento de 4 m/s produce 50 unidades; con 6 m/s, 150; con 8 m/s, 350; con 10 m/s, 600. Si el viento es muy débil o muy fuerte, la turbina se detiene.",
      "En una hidroeléctrica, más caudal de agua o mayor altura de caída producen más energía. En un panel solar, más luz significa más producción y más superficie de paneles significa más energía. En las pilas, conectar varias una a continuación de la otra suma sus voltajes: dos baterías de 12 V conectadas así entregan 24 V.",
      "Para analizar la relación se grafica o se escribe una tabla y se describe el patrón. También se calculan diferencias entre registros y se declara una limitación, por ejemplo que los datos vienen de una sola turbina. Una relación entre variables ayuda a predecir, pero la predicción debe quedar dentro del rango medido.",
  ],
  vocab=[("caudal", "cantidad de agua que pasa por un lugar en un tiempo"), ("altura de caída", "desnivel por el que cae el agua"), ("rango medido", "intervalo de valores en que hay datos"), ("predicción", "valor que se espera según un patrón"), ("conexión a continuación", "pilas unidas una tras otra para sumar sus voltajes")],
  worked=[
      ("Leer la relación", "Una turbina produce 50 unidades con 4 m/s y 150 con 6 m/s. ¿Cuántas unidades más produce al subir el viento 2 m/s?", ["Resto 150 − 50.", "150 − 50 = 100."], "100 unidades más"),
      ("Pilas conectadas", "Dos pilas de 3 V conectadas una a continuación de la otra, ¿cuántos volts entregan?", ["Sumo los voltajes.", "3 + 3 = 6."], "6 V"),
  ],
  mistakes=[
      ("Predecir fuera del rango de datos sin avisar.", "Más allá de lo medido no se sabe cómo se comporta.", "Declara el rango."),
      ("Creer que a más viento siempre hay más energía.", "Un viento muy fuerte obliga a detener la turbina.", "Revisa los límites."),
  ],
  rec=[
      ("¿Más viento produce más o menos energía en una turbina, dentro del rango de funcionamiento?", "Más energía", "La turbina gira más rápido."),
      ("¿Más altura de caída del agua produce más o menos energía?", "Más energía", "El agua llega con más fuerza."),
      ("Verdadero o falso: más luz sobre un panel significa más producción.", "Verdadero", "Recibe más energía luminosa."),
  ],
  und=[
      ("¿Por qué se detiene una turbina con un viento extremadamente fuerte? A) Para protegerla de daños; B) Porque deja de producir por falta de viento.", "A", "Los vientos extremos pueden romperla."),
      ("Si la superficie de paneles se duplica, ¿qué ocurre con la energía que producen, con la misma luz? A) Se duplica aproximadamente; B) Se reduce a la mitad.", "A", "Hay más superficie que recibe luz."),
      ("¿Qué significa «rango medido»?", "El intervalo de valores en que hay datos", "Fuera de él no se sabe qué pasa."),
  ],
  app=[
      arith("Con datos de ejemplo, una turbina produce 350 unidades con 8 m/s y 600 con 10 m/s. ¿Cuántas unidades más produce con 10 m/s?", "600-350", "Se resta el menor al mayor."),
      arith("Una turbina produce 600 unidades con 10 m/s. Un parque de ejemplo tiene 4 turbinas iguales con ese viento. ¿Cuántas unidades produce el parque?", "600*4", "Se multiplica por el número de turbinas."),
      arith("Una cadena de tres baterías de 12 V conectadas una a continuación de la otra, ¿cuántos volts entrega?", "12*3", "Se suman los voltajes."),
  ],
  rea=[
      ("Alguien predice que con 20 m/s la turbina producirá 2.000 unidades porque 10 m/s dio 600. ¿Qué falla tiene? A) Predice fuera del rango medido y no considera que la turbina se detiene; B) Los datos no existen.", "A", "No hay datos con 20 m/s."),
      ("¿Por qué se mide la producción con distintas velocidades de viento y no con una sola?", "Para ver cómo cambia la producción con el viento", "Una relación necesita varios valores."),
  ],
  cha=[
      ("Una hidroeléctrica de ejemplo produce 40 unidades con una altura de 10 m y 80 con 20 m, con el mismo caudal. ¿Qué producción se espera con 15 m, si la relación fuera proporcional? Responde con el número.", "60", "Está a mitad de camino entre 40 y 80.", "(40+80)//2"),
      ("Un panel produce 8 unidades con 2 horas de sol fuerte y 16 con 4 horas. ¿Cuántas unidades por hora de sol fuerte produce?", "4", "8 ÷ 2 = 4; 16 ÷ 4 = 4.", "8//2"),
  ],
  context=[arith("Un parque de ejemplo tiene 10 turbinas que producen 350 unidades cada una con viento de 8 m/s. ¿Cuántas unidades produce el parque?", "10*350", "Se multiplica el número de turbinas por la producción de cada una.")],
  selfcheck=[("¿Cómo cambia la energía eólica con el viento?", "Aumenta al aumentar la velocidad", "Dentro de un rango."), ("¿Qué suman las pilas conectadas una a continuación de la otra?", "Sus voltajes", "Dan un voltaje mayor."), ("¿Qué debe cuidar una predicción?", "Quedar dentro del rango medido", "No se extrapola sin datos.")],
  open_task=task("Con estos datos de ejemplo (viento 4 m/s-50 unidades; 6 m/s-150; 8 m/s-350; 10 m/s-600), calcula cuánto aumenta la producción en cada paso de 2 m/s y describe el patrón. Después predice si una turbina con 7 m/s produciría entre 150 y 350 unidades y explica por qué.", "Aumentos: 100, 200 y 250. Cada paso aumenta más que el anterior. Con 7 m/s se espera entre 150 y 350, porque 7 está entre 6 y 8 y la producción crece con el viento. Limitación: pocos datos.", ["tres aumentos correctos", "patrón descrito", "predicción dentro del rango"], ["cálculos, patrón y predicción"], ["predecir fuera del rango", "no calcular los aumentos"], "Pregunta qué otra medición ayudaría."),
  reinforce="Calcula cuántos volts entregan cuatro baterías de 6 V conectadas una a continuación de la otra.",
  extend="Explica por qué una turbina se detiene con un viento extremadamente fuerte.")

L(OA9, 5,
  materials="Este cuaderno y lápiz. Las tablas son de ejemplo. Las pilas usadas no se botan a la basura común: se llevan a un punto de reciclaje.",
  use="Aprenderé a comparar y evaluar tecnologías de generación eléctrica con criterios: fuente, renovabilidad, emisiones, continuidad e impacto. Sirve para decidir con argumentos.",
  prior=["Sé cómo funciona cada tecnología.", "Sé leer una tabla de criterios."],
  explain=[
      "Para evaluar una tecnología se usan criterios. Un recurso renovable se repone de forma natural: sol, viento y agua. Uno no renovable se agota, como los combustibles fósiles y el uranio. Otros criterios son las emisiones de gases de efecto invernadero durante la operación, la continuidad (si produce todo el día), los residuos y el impacto en el ambiente y las comunidades.",
      "Cada tecnología tiene ventajas y desventajas. Los paneles fotovoltaicos y las turbinas eólicas no emiten gases durante la operación, pero dependen del sol y del viento, y por eso se complementan con baterías u otras fuentes. Las hidroeléctricas son renovables, pero los embalses cambian los ecosistemas. Las centrales nucleares no emiten dióxido de carbono al operar, pero generan residuos radiactivos que requieren un manejo seguro. Las centrales que queman combustibles fósiles emiten dióxido de carbono. En Chile, la radiación solar es especialmente alta en el norte del país.",
      "Una evaluación basada en evidencias compara con datos y dice qué criterio pesa más para la decisión. Las pilas también se evalúan: las recargables reducen residuos, y las usadas deben llevarse a puntos de reciclaje porque contienen metales que dañan el ambiente. No hay una tecnología perfecta: se decide según el contexto y se justifica con criterios.",
  ],
  vocab=[("recurso renovable", "recurso que se repone de forma natural"), ("combustible fósil", "recurso formado hace millones de años, como el carbón y el petróleo"), ("emisión", "gas que se libera al ambiente"), ("continuidad", "capacidad de producir sin interrupciones"), ("embalse", "lago artificial que acumula agua para una hidroeléctrica")],
  worked=[
      ("Renovable o no", "Clasifica: sol, uranio, viento. ¿Cuáles son renovables?", ["El sol y el viento se reponen naturalmente.", "El uranio se agota."], "Sol y viento"),
      ("Comparar con criterios", "Tecnología X: renovable, depende del viento. Tecnología Y: no renovable, funciona todo el día. Si el criterio más importante es no agotar recursos, ¿cuál conviene?", ["El criterio es renovabilidad.", "X es renovable."], "La tecnología X"),
  ],
  mistakes=[
      ("Decir que una tecnología es perfecta.", "Todas tienen ventajas y desventajas.", "Compara con varios criterios."),
      ("Botar las pilas usadas a la basura común.", "Contienen metales que dañan el ambiente.", "Llévalas a puntos de reciclaje."),
  ],
  rec=[
      ("¿Cuál es renovable: el viento o el carbón?", "El viento", "Se repone naturalmente."),
      ("¿Dónde se llevan las pilas usadas: a un punto de reciclaje o a la basura común?", "A un punto de reciclaje", "Contienen metales que dañan el ambiente."),
      ("Verdadero o falso: un panel solar produce de noche con la misma intensidad.", "Falso", "Necesita luz para funcionar."),
  ],
  und=[
      ("¿Qué desventaja principal tiene la energía solar y eólica? A) Dependen del sol y del viento; B) Emiten mucho dióxido de carbono al operar.", "A", "No son continuas por sí solas."),
      ("¿Qué impacto tiene un embalse? A) Cambia los ecosistemas del lugar; B) Aumenta las emisiones de dióxido de carbono por la operación.", "A", "Inunda y modifica un territorio."),
      ("¿Qué residuo especial genera una central nuclear?", "Residuos radiactivos", "Requieren manejo seguro."),
  ],
  app=[
      ("Tabla de ejemplo: solar (renovable, sin emisiones, intermitente), carbón (no renovable, emisiones altas, continuo), hidro (renovable, sin emisiones, continuo). ¿Cuál cumple los tres criterios: renovable, sin emisiones y continuo?", "La hidroeléctrica", "Es la única con las tres características en la tabla."),
      arith("Una matriz de ejemplo da 3 puntos a la tecnología P por renovabilidad, 2 por continuidad y 4 por bajo impacto. ¿Cuántos puntos tiene en total?", "3+2+4", "Se suman los puntos de cada criterio."),
      arith("La tecnología Q tiene 4 puntos por renovabilidad, 1 por continuidad y 3 por bajo impacto. ¿Cuántos puntos más que Q tiene P (que suma 9)?", "9-(4+1+3)", "Se resta el total de Q al de P."),
  ],
  rea=[
      ("Alguien afirma: «Como la solar es renovable, es la mejor en todo». ¿Qué falla tiene? A) No considera la continuidad ni el impacto de su fabricación; B) La solar no es renovable.", "A", "Se debe evaluar con varios criterios."),
      ("En una zona sin viento ni sol fuerte, ¿qué tecnología renovable puede ser más adecuada si hay un río con buen caudal?", "Una hidroeléctrica", "Usa el agua disponible."),
  ],
  cha=[
      ("Una comunidad de ejemplo debe elegir entre un parque solar (sin emisiones, no produce de noche) y una central a carbón (produce todo el día, emite mucho dióxido de carbono). ¿Cuál es una decisión mejor justificada para reducir emisiones? A) El parque solar con baterías; B) La central a carbón.", "A", "Reduce emisiones y se complementa con almacenamiento."),
      ("¿Qué dato adicional ayudaría a decidir mejor?", "Cuánta energía necesita la comunidad y los costos", "Las decisiones usan varios datos."),
  ],
  context=[("Un colegio de ejemplo quiere ahorrar energía. Tiene un techo despejado al norte, mucha luz en el día y poco viento. ¿Qué tecnología es más adecuada? A) Paneles fotovoltaicos; B) Turbina eólica grande.", "A", "Hay mucha luz y poco viento.")],
  selfcheck=[("¿Qué es un recurso renovable?", "Uno que se repone de forma natural", "Como el sol y el viento."), ("¿Qué desventaja tiene la energía eólica?", "Depende del viento", "No siempre hay viento."), ("¿Qué debes hacer con las pilas usadas?", "Llevarlas a un punto de reciclaje", "Evita dañar el ambiente.")],
  open_task=task("Elige tres tecnologías entre solar, eólica, hidroeléctrica, nuclear y a carbón. Haz una tabla con cuatro criterios (renovable, emisiones al operar, continuidad, impacto o residuos) y una breve conclusión que diga cuál elegirías para una escuela del norte de Chile y por qué.", "Solar: renovable; sin emisiones al operar; no continua; impacto bajo en el uso. Eólica: renovable; sin emisiones; depende del viento; impacto moderado. Hidroeléctrica: renovable; sin emisiones; continua; cambia ecosistemas. Para una escuela del norte elegiría solar porque hay mucha radiación y es fácil de instalar en el techo.", ["tabla con tres tecnologías", "cuatro criterios", "conclusión justificada"], ["tabla y conclusión"], ["no justificar con criterios", "afirmar que una es perfecta"], "Pregunta qué cambiaría si la escuela estuviera en el sur."),
  reinforce="Escribe una ventaja y una desventaja de la energía eólica.",
  extend="Explica por qué se complementan los paneles solares con baterías.")
