"""Cuaderno del estudiante, 3.º básico Ciencias Naturales: OA 05 (reducir, reutilizar y reciclar recursos) y OA 06 (alimentos y hábitos saludables)."""
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


OA5, OA6 = "CN03 OA 05", "CN03 OA 06"

# ---------------------------------------------------------------- OA 05
L(OA5, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Mira en tu casa, sin sacar nada de la basura, los envases y restos que se botan en un día.",
  use="Aprenderé la diferencia entre recurso y residuo. Sirve para entender de dónde vienen las cosas que usamos y por qué hay que usarlas con cuidado.",
  prior=["Sé que los materiales como el papel, el plástico y el cartón son distintos.", "Sé que la naturaleza nos da agua, madera y otros materiales."],
  explain=[
      "Un recurso es algo que sacamos de la naturaleza o que está hecho con materiales de la naturaleza, y que usamos para vivir. El agua, la madera, el suelo y los metales son recursos. El papel y el cartón también vienen de un recurso: los árboles. Los recursos no son infinitos, y por eso hay que usarlos bien.",
      "Un residuo es lo que sobra después de usar algo y que ya no usamos. Las cáscaras de fruta, un envase vacío o una hoja de papel arrugada son residuos. Un residuo no es lo mismo que un recurso, pero muchos residuos pueden volver a ser recursos. Un envase limpio puede reutilizarse, y el papel usado puede reciclarse.",
      "Al clasificar algo, pregúntate: ¿viene de la naturaleza y me sirve para vivir o fabricar? Entonces es un recurso. ¿Es lo que queda después de usarlo? Entonces es un residuo. Algunos objetos son las dos cosas según el momento: una botella llena de agua es un envase útil, y cuando está vacía y rota es un residuo.",
  ],
  vocab=[("recurso", "algo de la naturaleza, o hecho con ella, que usamos"), ("residuo", "lo que sobra después de usar algo"), ("material", "sustancia con que está hecho un objeto, como papel o plástico"), ("agotarse", "acabarse porque se usa más rápido de lo que se repone"), ("clasificar", "ordenar según un criterio")],
  worked=[
      ("Clasificar con una pregunta", "¿Es el agua de la llave un recurso o un residuo?", ["Pregunto si viene de la naturaleza: el agua sí.", "Pregunto si es lo que sobra: no, la usamos para beber y lavar.", "Es un recurso."], "Es un recurso"),
      ("Un objeto en dos momentos", "Una botella llena de agua y la misma botella rota y vacía. ¿Cómo se clasifica cada una?", ["Llena, la botella contiene agua que usaremos.", "Rota y vacía, ya no sirve para lo que se usaba.", "Cada momento cambia la clasificación."], "Llena es un envase útil; rota y vacía es un residuo"),
  ],
  mistakes=[
      ("Decir «un residuo siempre es basura inútil».", "Muchos residuos se pueden reutilizar o reciclar.", "Un residuo limpio puede volver a ser un recurso."),
      ("Decir «el agua nunca se acaba».", "Si se usa mal, puede faltar.", "El agua es un recurso que hay que cuidar."),
  ],
  rec=[
      ("¿La madera de un árbol es un recurso o un residuo?", "Un recurso", "Viene de la naturaleza y la usamos."),
      ("Una cáscara de plátano que sobró, ¿es un recurso o un residuo?", "Un residuo", "Es lo que sobra después de comerlo."),
      ("Completa con «recurso» o «residuo»: lo que sobra después de usar algo es un ______.", "Residuo", "Eso es un residuo."),
  ],
  und=[
      ("¿Qué es un recurso?", "Algo de la naturaleza o hecho con ella que usamos", "Es la definición de la clase."),
      ("¿Por qué hay que usar bien los recursos?", "Porque pueden agotarse", "Si se usan más rápido de lo que se reponen, se acaban."),
      ("Un papel usado, ¿puede volver a ser un recurso? Responde Sí o No y explica en pocas palabras.", "Sí, porque se puede reciclar", "El papel usado se puede reciclar para hacer papel nuevo."),
  ],
  app=[
      ("Clasifica con letras: A) agua, B) cáscara de manzana, C) madera, D) envase vacío. Escribe las letras de los residuos.", "B y D", "La cáscara y el envase vacío son lo que sobra."),
      arith("En una casa se botaron 4 envases de yogur y 3 hojas de papel usado en un día. ¿Cuántos residuos hubo?", "4+3", "Se suman los residuos."),
      ("Una persona cierra la llave mientras se enjabona las manos. ¿Está cuidando un recurso o un residuo?", "Un recurso", "El agua es un recurso."),
  ],
  rea=[
      ("Dos niños discuten si un cuaderno viejo es un recurso o un residuo. Uno dice que es residuo porque ya no sirve. Otro dice que el papel se puede reciclar. ¿Quién tiene mejor razón para volver a usar el material?", "El que dice que se puede reciclar", "El papel viejo puede volver a ser material."),
      ("Un niño dice: «Si boto el papel a la basura, el recurso del árbol se pierde». ¿Qué podría hacer con ese papel?", "Reutilizarlo o reciclarlo", "Así el material vuelve a usarse."),
  ],
  cha=[
      ("Explica por qué un trozo de madera puede ser recurso y también residuo, según el momento.", "Es recurso antes de usarlo y residuo si sobra como viruta", "Cambia según si se usa o sobra."),
      ("Escribe dos recursos y dos residuos que haya en una sala de clases.", "Recursos: agua, madera. Residuos: papeles arrugados, restos de lápiz", "Son ejemplos válidos de la clasificación."),
  ],
  context=[("En una escuela se juntaron en un día 9 hojas de papel usado y 6 envases vacíos. ¿Cuántos residuos son en total?", "15", "Se suman papeles y envases. Cálculo: 9 + 6 = 15.")],
  selfcheck=[("¿Qué es un residuo?", "Lo que sobra después de usar algo", "Por ejemplo, una cáscara."), ("¿El agua es un recurso o un residuo?", "Un recurso", "Viene de la naturaleza y la usamos."), ("¿Un residuo puede volver a ser recurso? Responde Sí o No.", "Sí", "Reutilizándolo o reciclándolo.")],
  open_task=task("Mira en tu casa o escuela cinco cosas que se usan o se botan en un día, por ejemplo agua, un envase, papel usado, una cáscara y un lápiz. Haz una tabla con dos columnas, «recurso» y «residuo», y escribe cada una donde corresponda. Al lado, escribe si ese residuo podría reutilizarse o reciclarse. Si no puedes mirar, clasifica estas: agua, madera, envase vacío, cáscara de naranja, papel usado.", "Recurso: agua, madera. Residuo: envase vacío (reutilizar), cáscara de naranja, papel usado (reciclar).", ["clasifica cinco objetos", "escribe qué se puede hacer con cada residuo", "usa la pregunta de la clase"], ["tabla de dos columnas", "frase con una idea para cada residuo"], ["decir que todo residuo es inútil", "clasificar por el tamaño"], "Pregunta por qué clasificó cada objeto así y qué pregunta usó para decidir."),
  reinforce="Dibuja un recurso y un residuo de tu casa y rotula cada uno.",
  extend="Piensa en un objeto de tu casa que primero es un recurso y luego un residuo, y cuenta cuándo cambia.")

L(OA5, 2,
  materials="Este cuaderno, lápiz y lápices de colores. Mira en tu casa objetos que se usan una sola vez y otros que se pueden usar muchas veces.",
  use="Aprenderé por qué conviene primero reducir, luego reutilizar y después reciclar. Sirve para elegir la acción que cuida más los recursos.",
  prior=["Sé qué es un recurso y qué es un residuo.", "Sé que algunos materiales se pueden usar de nuevo."],
  explain=[
      "Hay tres acciones para cuidar los recursos. Reducir es usar menos cosas o menos cantidad, para que se produzcan menos residuos. Reutilizar es usar un objeto otra vez, para lo mismo o para otra cosa. Reciclar es transformar los residuos en materiales nuevos para fabricar otros objetos.",
      "Estas acciones tienen un orden: primero reducir, luego reutilizar y al final reciclar. Reducir es lo mejor porque no gasta recursos nuevos ni genera residuos. Reutilizar usa un objeto de nuevo sin fabricarlo otra vez. Reciclar sirve, pero necesita fábricas y energía, y por eso es la última opción.",
      "Un ejemplo: si llevas una bolsa de tela al comprar, reduces las bolsas de plástico que se botan. Si usas un frasco limpio para guardar botones, lo reutilizas. Si el cartón se lleva a un punto de reciclaje, se recicla. El reciclaje funciona mejor si los residuos están limpios y separados por material.",
  ],
  vocab=[("reducir", "usar menos para generar menos residuos"), ("reutilizar", "usar un objeto otra vez"), ("reciclar", "transformar un residuo en material para fabricar algo nuevo"), ("punto de reciclaje", "lugar donde se entregan residuos para reciclarlos"), ("energía", "lo que se necesita para que las máquinas funcionen")],
  worked=[
      ("Clasificar una acción", "Una niña usa una botella limpia para regar sus plantas. ¿Reduce, reutiliza o recicla?", ["La botella se usa otra vez.", "No se transforma en material nuevo.", "Es reutilizar."], "Reutiliza"),
      ("Elegir la mejor acción", "Una persona puede comprar un jugo en caja cada día o llevar agua en una botella rellenable. ¿Qué acción reduce más residuos?", ["La caja genera un residuo cada día.", "La botella rellenable se usa muchas veces.", "Reducir evita residuos desde el comienzo."], "Llevar agua en una botella rellenable"),
  ],
  mistakes=[
      ("Pensar que «reciclar» es siempre lo mejor.", "Se olvida que reducir evita el residuo.", "Primero reduce, luego reutiliza y al final recicla."),
      ("Llevar al reciclaje envases sucios y mezclados.", "El reciclaje funciona mejor con residuos limpios y separados.", "Enjuaga los envases y sepáralos por material."),
  ],
  rec=[
      ("Usar menos para generar menos residuos, ¿es reducir o reciclar?", "Reducir", "Reducir es usar menos."),
      ("Usar una caja de cartón para guardar juguetes, ¿es reutilizar o reciclar?", "Reutilizar", "Se usa el objeto otra vez."),
      ("Transformar papel usado en papel nuevo, ¿es reducir o reciclar?", "Reciclar", "El papel usado se transforma en material nuevo."),
  ],
  und=[
      ("¿Qué acción va primero: reducir, reutilizar o reciclar?", "Reducir", "Evita generar residuos desde el comienzo."),
      ("¿Por qué reciclar es la última opción?", "Porque necesita fábricas y energía", "Reducir y reutilizar gastan menos."),
      ("¿Para qué sirve enjuagar un envase antes de reciclarlo?", "Para que el reciclaje funcione mejor", "Los residuos limpios se reciclan mejor."),
  ],
  app=[
      arith("Una familia usaba 3 bolsas de plástico a la semana. Con una bolsa de tela pasó a usar 0. ¿Cuántas bolsas de plástico dejó de botar en 4 semanas?", "3*4", "Se multiplica las bolsas por semana por las 4 semanas."),
      ("Acciones: A) tomar agua en un vaso propio en vez de usar un vaso desechable cada vez, B) llevar el cartón a un punto de reciclaje, C) usar un frasco limpio como lápicero. Escribe la letra de reducir.", "A", "Con un vaso propio se usan menos vasos desechables."),
      ("Un niño usa el reverso de una hoja para dibujar. ¿Reduce, reutiliza o recicla?", "Reutiliza", "Usa la hoja otra vez."),
  ],
  rea=[
      ("Dos propuestas: A) comprar un juguete de plástico nuevo y reciclar el envase; B) reparar el juguete que ya tienes. ¿Cuál cuida más los recursos y por qué?", "B, porque usa menos recursos nuevos", "Reparar evita fabricar otro objeto."),
      ("Un niño dice: «Si reciclo todo, ya no tengo que reducir». ¿Qué le respondes?", "Que reducir es mejor porque evita residuos y recursos nuevos", "Reciclar usa energía."),
  ],
  cha=[
      ("Ordena de la mejor a la menos buena para cuidar recursos: A) reciclar, B) reducir, C) reutilizar.", "B, C, A", "El orden es reducir, reutilizar y reciclar."),
      ("Escribe una acción para reducir residuos en el recreo y otra para reutilizar algo en tu sala.", "Por ejemplo: llevar la colación en un recipiente lavable; usar el reverso de las hojas", "Una reduce y la otra reutiliza."),
  ],
  context=[("En un curso, cada niño usaba 2 servilletas de papel al día por 5 días de clases. Con un paño lavable usan 0. Si son 10 niños, ¿cuántas servilletas dejan de botar en una semana? Primero calcula por niño y después por el curso.", "100", "Por niño son 10; por el curso son 100. Cálculo: 2 × 5 × 10 = 100.")],
  selfcheck=[("¿Qué es reutilizar?", "Usar un objeto otra vez", "Se aprovecha sin fabricar otro."), ("¿Qué es reciclar?", "Transformar residuos en material nuevo", "Con ellos se fabrican otros objetos."), ("¿Cuál va primero: reducir o reciclar?", "Reducir", "Evita residuos desde el comienzo.")],
  open_task=task("Haz una tabla de tres columnas: reducir, reutilizar y reciclar. Escribe en cada una dos acciones que puedas hacer en tu casa o escuela. Después marca con un número 1, 2 y 3 el orden de importancia y escribe por qué reducir va primero. Si necesitas ideas: llevar bolsa de tela, usar el reverso de las hojas, llevar el cartón a un punto de reciclaje.", "Reducir: llevar bolsa de tela; tomar agua de la llave. Reutilizar: usar frascos limpios; reverso de hojas. Reciclar: cartón, papel. Reducir va primero porque evita residuos.", ["escribe dos acciones por columna", "ordena de 1 a 3", "explica por qué reducir va primero"], ["tabla de tres columnas", "frase de justificación"], ["poner reciclar primero", "confundir reutilizar con reciclar"], "Revisa que cada acción esté en su columna y que la justificación hable de evitar residuos."),
  reinforce="Dibuja una acción de reducir, una de reutilizar y una de reciclar.",
  extend="Pregunta en tu casa cuál acción de las tres hacen más y cuál podrían hacer más.")

L(OA5, 3,
  materials="Este cuaderno, lápiz, regla y lápices de colores. Si lo haces en casa: un envase de plástico limpio, con una persona adulta que lo corte. No uses vidrio ni latas, porque cortan.",
  use="Aprenderé a diseñar un objeto útil con un residuo. Sirve para practicar cómo la tecnología resuelve un problema de la casa o la escuela reutilizando materiales.",
  prior=["Sé que reutilizar es usar un objeto otra vez.", "Sé que algunos materiales no son seguros para manipular."],
  explain=[
      "Diseñar es pensar cómo será un objeto antes de hacerlo. Se empieza con un problema: por ejemplo, los lápices se pierden en la mesa. Luego se piensa una idea, se elige un residuo limpio y seguro, y se dibuja un boceto con medidas. Por último se hace un prototipo, que es un modelo de prueba.",
      "Un buen diseño cumple criterios. Un criterio es una condición que debe cumplir el objeto. Por ejemplo: que sirva para el problema, que sea seguro, que sea fácil de hacer y que dure. Para que sea seguro, no se usan vidrios ni objetos con filo. Una persona adulta debe hacer los cortes con tijeras o herramientas.",
      "Un ejemplo es un lápicero hecho con un envase de yogur limpio. Resuelve el problema, reutiliza un residuo y es seguro si los bordes se cubren con cinta. Otro ejemplo es un macetero con una botella de plástico cortada por una persona adulta, con agujeros abajo para que salga el agua sobrante.",
  ],
  vocab=[("diseñar", "pensar cómo será un objeto antes de hacerlo"), ("boceto", "dibujo rápido de una idea con medidas"), ("prototipo", "primer modelo para probar si el diseño funciona"), ("criterio", "condición que debe cumplir un objeto"), ("seguro", "que no puede hacer daño")],
  worked=[
      ("De problema a idea", "El problema es que los lápices se pierden en la mesa. Hay un envase de yogur limpio. ¿Qué diseño propones?", ["Pienso para qué sirve el envase: guardar cosas.", "Lo uso como lápicero y cubro el borde con cinta.", "Dibujo el boceto con la altura."], "Un lápicero hecho con el envase de yogur"),
      ("Revisar con criterios", "Criterios: sirve, es seguro y es fácil. Un niño propone un lápicero con una lata cortada. ¿Cumple todos?", ["Sirve para guardar lápices.", "La lata cortada tiene filos, no es segura.", "No cumple todos los criterios."], "No, porque no es seguro"),
  ],
  mistakes=[
      ("Elegir vidrio o una lata cortada para el diseño.", "Tienen bordes que cortan.", "Elige plástico o cartón limpio y deja los cortes a una persona adulta."),
      ("Empezar a pegar sin dibujar antes.", "Sin boceto no se sabe si el diseño funciona.", "Dibuja un boceto con medidas antes de construir."),
  ],
  rec=[
      ("¿Un boceto es un dibujo antes de hacer el objeto, o el objeto terminado?", "Un dibujo antes de hacer el objeto", "El boceto es el dibujo de la idea."),
      ("¿Un criterio es una condición que debe cumplir el objeto? Responde Sí o No.", "Sí", "Por ejemplo: que sea seguro."),
      ("¿Quién hace los cortes en un envase: un niño solo o una persona adulta?", "Una persona adulta", "Cortar es riesgoso para niños."),
  ],
  und=[
      ("¿Para qué sirve un prototipo?", "Para probar si el diseño funciona", "Es el primer modelo de prueba."),
      ("Nombra dos criterios de un buen diseño.", "Que sirva, que sea seguro, que sea fácil o que dure (dos de ellos)", "Son criterios de la clase."),
      ("¿Por qué no se usa vidrio en el diseño?", "Porque se puede quebrar y cortar", "No es seguro."),
  ],
  app=[
      ("Residuos limpios: A) envase de yogur, B) botella de vidrio, C) caja de cartón. ¿Cuáles son seguros para usar en un diseño?", "A y C", "El vidrio puede cortar."),
      arith("Un lápicero de envase mide 9 cm de alto. Los lápices miden 15 cm. ¿Cuántos centímetros de lápiz sobresalen?", "15-9", "Se resta la altura del envase a la del lápiz."),
      ("Un niño necesita un macetero para una planta. ¿Qué residuo usarías: una botella de plástico limpia o un frasco de vidrio roto?", "Una botella de plástico limpia", "El vidrio roto es peligroso."),
  ],
  rea=[
      ("Un niño dice que su diseño es bueno porque «es bonito». ¿Cumple los criterios? Explica.", "No necesariamente; hay que ver si sirve y es seguro", "Bonito no es un criterio de seguridad ni de utilidad."),
      ("Un macetero hecho con una botella no tiene agujeros abajo. ¿Qué problema puede tener la planta?", "El agua se acumula y las raíces se dañan", "Las raíces necesitan que salga el agua sobrante."),
  ],
  cha=[
      ("Escribe un problema de tu sala y qué residuo limpio y seguro usarías para solucionarlo.", "Por ejemplo: los lápices se pierden; un envase de yogur limpio como lápicero", "Une problema y residuo."),
      ("Un niño hace un prototipo de lápicero y se cae porque es muy liviano. ¿Cómo lo mejorarías?", "Poniéndole una base más ancha o más pesada", "Una base más ancha da estabilidad."),
  ],
  context=[("En una sala se diseñan 5 lápiceros con envases limpios. Cada uno guarda 6 lápices. ¿Cuántos lápices guardan en total?", "30", "Se multiplica la cantidad de lápiceros por los lápices de cada uno. Cálculo: 5 × 6 = 30.")],
  selfcheck=[("¿Qué es un prototipo?", "Un modelo para probar el diseño", "Se prueba antes de hacer el definitivo."), ("¿Se pueden usar vidrio o latas cortadas en el diseño? Responde Sí o No.", "No", "Cortan y no son seguros."), ("¿Qué se dibuja antes de construir?", "Un boceto", "Muestra la idea y las medidas.")],
  open_task=task("Elige uno de estos problemas: A) los lápices se pierden en la mesa; B) hay que regar una planta con poca agua; C) las hojas sueltas se desordenan. Elige un residuo limpio y seguro de tu casa. Dibuja un boceto con medidas, escribe tres criterios que debe cumplir y qué parte hará una persona adulta. Si no puedes construirlo, deja el boceto y los criterios.", "Elegí A. Residuo: envase de yogur limpio, 9 cm de alto. Criterios: sirve, es seguro, es fácil. La persona adulta cubre los bordes con cinta.", ["elige un problema y un residuo", "dibuja un boceto con medidas", "escribe tres criterios y quién hace los cortes"], ["boceto con medidas", "lista de tres criterios"], ["usar vidrio o filos", "no pensar en los criterios"], "Revisa que cumpla los criterios y pregunta cómo probaría su prototipo."),
  reinforce="Dibuja cómo reutilizarías una caja de cartón para ordenar algo en tu pieza.",
  extend="Escribe cómo comprobarías, con una prueba sencilla, que tu diseño sirve para el problema.")

L(OA5, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Para la prueba del agua, con una persona adulta: una jarra o un recipiente con marcas de medida y una llave de agua.",
  use="Aprenderé a probar un instrumento que sirve para separar residuos o ahorrar agua. Sirve para comprobar con datos si una idea de cuidado realmente funciona.",
  prior=["Sé que se debe reducir, reutilizar y reciclar.", "Sé hacer una prueba justa y anotar los datos."],
  explain=[
      "Un instrumento tecnológico es un objeto que construimos para resolver un problema. Algunos ayudan a separar los residuos: por ejemplo, tres cajas con rótulos para papel, plástico y restos de comida. Otros ayudan a ahorrar un recurso: por ejemplo, un jarro con marcas para medir cuánta agua usamos.",
      "Para saber si un instrumento funciona, se hace una prueba. Se compara cómo era antes y cómo es después de usarlo. Siempre se anotan los datos en una tabla. Por ejemplo, se pone una tina bajo la llave para juntar el agua que cae y se mide con el jarro. Con la llave abierta mientras te enjabonas las manos se junta más agua que con la llave cerrada. Esa diferencia es lo que se ahorra.",
      "Una prueba justa cambia una sola cosa. Si midimos el agua de lavarse las manos, el tiempo debe ser el mismo en las dos pruebas. Con los datos se escribe una conclusión y también una mejora. Por ejemplo: «Los rótulos con letras ayudaron, pero los niños pequeños no leen; hay que agregar dibujos y colores».",
  ],
  vocab=[("instrumento tecnológico", "objeto construido para resolver un problema"), ("ahorrar", "usar menos de un recurso"), ("prueba", "ensayo para comprobar si algo funciona"), ("mejora", "cambio que hace que algo funcione mejor"), ("rótulo", "etiqueta que dice qué va en un lugar")],
  worked=[
      ("Leer una prueba de ahorro de agua", "Ejemplo: con la llave abierta mientras se enjabonan las manos se juntaron 3 litros. Con la llave cerrada, 1 litro. ¿Cuántos litros se ahorraron?", ["Busco los dos datos: 3 L y 1 L.", "Resto: 3 − 1 = 2.", "La diferencia es el ahorro."], "2 litros"),
      ("Evaluar un instrumento", "Una caja con rótulos de papel, plástico y restos de comida. Después de una semana, 12 residuos de 15 estaban en la caja correcta. ¿Cuántos estaban mal?", ["Total: 15.", "Correctos: 12.", "Resto: 15 − 12 = 3."], "3 residuos"),
  ],
  mistakes=[
      ("Probar el instrumento una sola vez.", "Una sola vez puede ser una casualidad.", "Repite la prueba varios días y anota todos los datos."),
      ("Cambiar el tiempo de lavado entre las dos pruebas.", "Cambia el resultado por otra razón.", "Usa el mismo tiempo en las dos pruebas."),
  ],
  rec=[
      ("Usar menos de un recurso, como el agua, se llama ______. Completa con ahorrar o botar.", "Ahorrar", "Ahorrar es usar menos."),
      ("¿Un rótulo dice qué va en cada caja de separación? Responde Sí o No.", "Sí", "El rótulo indica el residuo que va en la caja."),
      ("¿Se anotan los datos de una prueba en una tabla? Responde Sí o No.", "Sí", "Los datos ordenados permiten comparar."),
  ],
  und=[
      ("¿Para qué sirve una caja con rótulos de papel, plástico y restos?", "Para separar los residuos", "Así se separan por material."),
      ("¿Por qué el tiempo de lavado debe ser igual en las dos pruebas?", "Para que la diferencia se deba solo a la llave", "Es una prueba justa."),
      ("¿Qué hay que escribir además de la conclusión?", "Una mejora del instrumento", "Siempre se puede mejorar."),
  ],
  app=[
      arith("En una prueba de ejemplo, con la llave abierta se juntaron 4 litros y con la llave cerrada, 1 litro. ¿Cuántos litros se ahorraron?", "4-1", "Se resta el agua con llave cerrada a la de llave abierta."),
      arith("Un curso separó residuos durante 5 días y cada día juntó 6 envases de plástico. ¿Cuántos envases juntó en total?", "5*6", "Se multiplica los días por los envases de cada día."),
      ("En una caja rotulada «papel» aparece una cáscara de plátano. ¿Está bien o mal clasificada?", "Mal", "La cáscara es un resto de comida."),
  ],
  rea=[
      ("Al segundo día, 10 de 12 residuos estaban en la caja correcta. Al quinto día, 12 de 12. ¿El instrumento mejoró la clasificación?", "Sí", "Hubo más residuos bien clasificados."),
      ("Un niño dice que el instrumento no sirve porque un día falló. ¿Qué le respondes?", "Que hay que revisar los datos de varios días", "Una sola prueba no basta."),
  ],
  cha=[
      ("Propón una mejora para tres cajas con rótulos que los niños pequeños no pueden leer.", "Por ejemplo: agregar colores y dibujos a cada caja", "Los dibujos ayudan a quienes no leen."),
      ("Diseña una tabla de tres columnas para registrar durante una semana cuántos residuos hubo en cada caja de separación.", "Columnas: papel, plástico, restos de comida", "Una tabla ordena los datos."),
  ],
  context=[arith("Un niño midió el agua al enjabonarse las manos dos veces en el mismo baño y durante el mismo tiempo. Con la llave abierta juntó 6 litros y con la llave cerrada, 2 litros. ¿Cuántos litros se ahorraron al cerrar la llave?", "6-2", "Se resta el agua con la llave cerrada a la de la llave abierta.")],
  selfcheck=[("¿Qué es un instrumento tecnológico?", "Un objeto construido para resolver un problema", "Por ejemplo, una caja de separación."), ("¿Para qué se anotan los datos de una prueba?", "Para comparar antes y después", "Los datos son la evidencia."), ("¿Se puede mejorar un instrumento después de probarlo? Responde Sí o No.", "Sí", "La prueba muestra qué se puede mejorar.")],
  open_task=task("Elige: A) tres cajas rotuladas para separar residuos o B) un jarro con marcas para medir el agua al lavarte las manos, con una persona adulta. Haz una tabla para cinco días y anota tus datos: número de residuos bien y mal separados, o litros usados con la llave abierta y con la llave cerrada. Pon una tina bajo la llave para juntar el agua y mídela con el jarro. Si no puedes probar, usa este ejemplo: llave abierta, 3 litros; llave cerrada, 1 litro. Escribe una conclusión y una mejora.", "Elegí B. Con la llave abierta junté 3 litros; con la llave cerrada, 1 litro. Se ahorran 2 litros. Mejora: cerrar siempre la llave al enjabonarse.", ["hace una tabla con datos", "calcula cuánto se ahorra o cuántos fallan", "escribe una conclusión y una mejora"], ["tabla de cinco días", "conclusión escrita"], ["probar una sola vez", "cambiar el tiempo entre pruebas"], "Revisa que los datos estén ordenados y que la conclusión cite números."),
  reinforce="Dibuja las tres cajas de separación con sus rótulos y colores.",
  extend="Escribe cómo comprobarías en tu casa durante una semana si cerrar la llave al cepillarte los dientes ahorra agua.")

# ---------------------------------------------------------------- OA 06
L(OA6, 1,
  materials="Este cuaderno, lápiz y lápices de colores. Mira los alimentos que hay en tu casa o los que comiste hoy.",
  use="Aprenderé a ordenar los alimentos en grupos según lo que aportan al cuerpo. Sirve para elegir qué comer sin decir que un alimento es «bueno» o «malo» sin pensar.",
  prior=["Sé nombrar alimentos que como todos los días.", "Sé que el cuerpo necesita comer para vivir y crecer."],
  explain=[
      "Los alimentos se pueden ordenar en grupos según lo que aportan al cuerpo. Un nutriente es una sustancia de los alimentos que el cuerpo usa para vivir y crecer. Los grupos son: frutas y verduras; cereales, como pan, arroz y fideos; legumbres, como lentejas y porotos; lácteos, como leche y yogur; carnes, pescados y huevos; y aceites.",
      "También existen alimentos con mucha azúcar, grasa o sal, como las galletas dulces, los dulces y las bebidas azucaradas. Se pueden comer de vez en cuando, pero no son los que deben ocupar la mayor parte de lo que comemos. Si se comen muy seguido, pueden producir caries y dejar poco lugar para otros alimentos que el cuerpo necesita. En Chile, algunos envases traen un sello negro que dice «ALTO EN» azúcares, sodio (sal), grasas saturadas o calorías.",
      "Clasificar por aporte no es decir «este es bueno» y «este es malo». Es preguntar qué aporta cada alimento y cuánto. Una galleta no es «mala» ni una zanahoria es «buena»: cada una aporta algo distinto. La salud depende de qué comemos, cuánto y cada cuánto tiempo, y de comer una variedad de alimentos.",
  ],
  vocab=[("nutriente", "sustancia de los alimentos que el cuerpo usa para vivir y crecer"), ("grupo de alimentos", "conjunto de alimentos que aportan algo parecido"), ("legumbre", "semilla que se come, como la lenteja o el poroto"), ("lácteo", "alimento hecho con leche"), ("sello «ALTO EN»", "etiqueta negra que avisa que un alimento tiene mucha azúcar, sal, grasa saturada o calorías")],
  worked=[
      ("Clasificar un alimento", "¿En qué grupo está el yogur?", ["El yogur se hace con leche.", "Los alimentos hechos con leche son lácteos.", "El yogur es un lácteo."], "Lácteos"),
      ("Clasificar sin juicio", "Una galleta dulce tiene un sello negro «ALTO EN azúcares». ¿Es «mala»? ¿Cómo se clasifica?", ["El sello avisa que tiene mucha azúcar.", "No digo que sea mala: digo que aporta mucha azúcar.", "Se come de vez en cuando."], "Es un alimento con mucha azúcar para comer de vez en cuando"),
  ],
  mistakes=[
      ("Decir «las galletas son malas y las manzanas son buenas».", "Se juzga sin pensar en lo que aporta cada alimento y cuánto se come.", "Clasifica por lo que aportan y piensa cuánto y cada cuánto se comen."),
      ("Decir «los fideos son una fruta».", "Se confunden los grupos.", "Los fideos son cereales."),
  ],
  rec=[
      ("El pan, ¿es cereal o lácteo?", "Cereal", "El pan se hace con harina de cereal."),
      ("Las lentejas, ¿son legumbres o frutas?", "Legumbres", "Son semillas que se comen."),
      ("La leche, ¿es un lácteo o una verdura?", "Un lácteo", "La leche es el origen de los lácteos."),
  ],
  und=[
      ("¿Qué es un nutriente?", "Una sustancia de los alimentos que el cuerpo usa para vivir y crecer", "Es la definición de la clase."),
      ("¿Qué dice un sello negro que dice «ALTO EN azúcares»?", "Que el alimento tiene mucha azúcar", "El sello avisa un exceso."),
      ("¿Por qué no se dice «alimento bueno» o «alimento malo»?", "Porque importa qué aporta, cuánto se come y cada cuánto", "Se clasifica por aporte y no por juicio."),
  ],
  app=[
      ("Alimentos: A) manzana, B) arroz, C) queso, D) lenteja. ¿Cuáles son legumbres o cereales?", "B y D", "El arroz es cereal y la lenteja es legumbre."),
      arith("En una mesa hay 3 frutas, 2 verduras y 4 lácteos. ¿Cuántos alimentos hay en total?", "3+2+4", "Se suman los alimentos de cada grupo."),
      ("Un envase de galletas dice «ALTO EN azúcares». ¿Es un alimento para comer todos los días en grandes cantidades? Responde Sí o No.", "No", "Se come de vez en cuando."),
  ],
  rea=[
      ("Dos niños clasifican un jugo en caja con sello «ALTO EN azúcares». Uno dice «es malo». Otro dice «tiene mucha azúcar, mejor de vez en cuando». ¿Quién clasifica por aporte?", "El segundo", "Dice qué aporta y cada cuánto comerlo."),
      ("Un niño pone una zanahoria en el grupo de frutas y verduras. Otro la pone en cereales. ¿Quién tiene razón?", "El primero", "La zanahoria es una verdura."),
  ],
  cha=[
      ("Clasifica estos cuatro alimentos en sus grupos: huevo, yogur, pan y lechuga.", "Huevo: carnes, pescados y huevos; yogur: lácteos; pan: cereales; lechuga: frutas y verduras", "Cada uno va en su grupo."),
      ("Explica por qué un cuaderno de comida no debería llamarse «de comida buena y mala».", "Porque lo importante es qué aporta cada alimento y cuánto se come", "Los alimentos se clasifican por aporte."),
  ],
  context=[("En un almuerzo hay arroz, lentejas, ensalada de lechuga y una fruta de postre. ¿Cuántos grupos distintos de alimentos hay?", "3", "El arroz es cereal, las lentejas son legumbres, y la lechuga y la fruta son del mismo grupo de frutas y verduras.")],
  selfcheck=[("¿Qué grupo incluye lentejas y porotos?", "Legumbres", "Son semillas que se comen."), ("¿Qué grupo incluye leche y yogur?", "Lácteos", "Se hacen con leche."), ("¿Un alimento con sello «ALTO EN» debe comerse todos los días en grandes cantidades? Responde Sí o No.", "No", "Se come de vez en cuando.")],
  open_task=task("Anota los alimentos que comiste hoy o ayer. Si no los recuerdas, usa esta lista: pan, huevo, manzana, arroz, lentejas, yogur, galletas dulces con sello «ALTO EN azúcares». Clasifícalos en una tabla con los grupos de la clase. En una frase, escribe qué aporta cada grupo, sin usar las palabras «bueno» ni «malo».", "Pan: cereales. Huevo: carnes, pescados y huevos. Manzana: frutas y verduras. Arroz: cereales. Lentejas: legumbres. Yogur: lácteos. Galletas: alimento con mucha azúcar, de vez en cuando.", ["clasifica todos los alimentos", "no usa «bueno» ni «malo»", "escribe qué aporta cada grupo"], ["tabla con grupos", "frase por grupo"], ["usar bueno y malo", "poner un alimento en el grupo equivocado"], "Revisa que cada alimento esté en su grupo y que el lenguaje no juzgue."),
  reinforce="Dibuja un plato con alimentos de al menos tres grupos y rotula el grupo de cada uno.",
  extend="Busca en un envase de tu casa si tiene sellos «ALTO EN» y anota cuáles son.")

L(OA6, 2,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres, mira la mesa de tu casa a la hora de comer.",
  use="Aprenderé para qué le sirve cada grupo de alimentos al cuerpo. Sirve para entender por qué necesitamos comer de todo un poco.",
  prior=["Sé los grupos de alimentos.", "Sé que un nutriente es una sustancia que el cuerpo usa."],
  explain=[
      "El cuerpo usa los alimentos para tres funciones. La primera es dar energía: sirve para moverse, jugar, pensar y mantener el cuerpo caliente. Los cereales, como el pan, el arroz y los fideos, y los aceites dan mucha energía. La segunda es el crecimiento y la reparación: los lácteos, las carnes, los pescados, los huevos y las legumbres ayudan a formar músculos y huesos.",
      "La tercera función es proteger al cuerpo y ayudarlo a funcionar. Las frutas y las verduras tienen vitaminas y minerales que ayudan a que el cuerpo funcione bien y se defienda de enfermedades. También tienen fibra, que ayuda al funcionamiento del intestino. El agua es necesaria para casi todo en el cuerpo. Por eso conviene tomar agua durante el día.",
      "Ningún alimento da todo lo que necesitamos. Por eso hay que comer alimentos de distintos grupos. Si comiéramos solo pan, tendríamos mucha energía, pero faltarían otras sustancias. Una comida variada ayuda a que el cuerpo tenga de todo.",
  ],
  vocab=[("energía", "fuerza que el cuerpo usa para moverse y funcionar"), ("crecimiento", "aumento de tamaño del cuerpo"), ("reparación", "arreglo de partes dañadas del cuerpo"), ("vitaminas y minerales", "sustancias que ayudan al cuerpo a funcionar bien"), ("fibra", "parte de los vegetales que ayuda al intestino")],
  worked=[
      ("Relacionar alimento y función", "El arroz da mucha energía. ¿Para qué le sirve esa energía a un niño?", ["La energía sirve para moverse y pensar.", "Un niño juega y aprende.", "Entonces usa esa energía todo el día."], "Para moverse, jugar y pensar"),
      ("Elegir un alimento para crecer", "Un niño quiere alimentos que ayuden a formar músculos y huesos. Opciones: A) lentejas, B) caramelos. ¿Cuál elige?", ["Las legumbres ayudan al crecimiento y la reparación.", "Los caramelos dan mucha azúcar, no ayudan a formar músculos.", "La opción A cumple."], "A, las lentejas"),
  ],
  mistakes=[
      ("Decir «con comer solo pan tengo todo lo que necesito».", "Ningún alimento da todo lo que el cuerpo necesita.", "Combina alimentos de distintos grupos."),
      ("Decir «la fruta solo sirve para dar sabor».", "Se olvidan las vitaminas, los minerales y la fibra.", "Las frutas y verduras ayudan a que el cuerpo funcione bien."),
  ],
  rec=[
      ("Los cereales y los aceites dan mucha ______. Completa con energía o fibra.", "Energía", "Son alimentos de mucha energía."),
      ("Las frutas y verduras tienen vitaminas y minerales. ¿Ayudan al cuerpo a funcionar bien? Responde Sí o No.", "Sí", "Esa es su función."),
      ("¿Para qué sirve el agua: solo para el sabor o para casi todo en el cuerpo?", "Para casi todo en el cuerpo", "El cuerpo necesita agua para funcionar."),
  ],
  und=[
      ("Nombra dos alimentos que ayudan al crecimiento y a la reparación.", "Lácteos, carnes, huevos o legumbres (dos de ellos)", "Ayudan a formar músculos y huesos."),
      ("¿Por qué necesitamos comer alimentos de distintos grupos?", "Porque ningún alimento da todo lo que el cuerpo necesita", "Cada grupo aporta algo distinto."),
      ("¿Qué función cumple la fibra?", "Ayuda al intestino a funcionar", "Está en frutas y verduras."),
  ],
  app=[
      ("Tabla: A) pan, B) leche, C) lechuga. Escribe la letra del alimento que principalmente da energía.", "A", "El pan es cereal y da energía."),
      arith("Un niño comió 2 frutas en la mañana y 3 verduras en el almuerzo. ¿Cuántas porciones de frutas y verduras comió?", "2+3", "Se suman frutas y verduras."),
      ("Un niño practica fútbol y necesita energía. ¿Qué alimento ayuda más a eso: arroz o agua sola?", "Arroz", "El arroz es un cereal con energía."),
  ],
  rea=[
      ("Una niña come solo pan en todas las comidas. ¿Qué le puede faltar?", "Alimentos de otros grupos, como frutas, verduras y legumbres", "Una sola clase no da todo lo necesario."),
      ("Un niño dice: «Si tomo mucha bebida azucarada, ya no necesito agua». ¿Qué le respondes?", "Que el cuerpo necesita agua y la bebida azucarada tiene mucha azúcar", "El agua es lo mejor para tomar durante el día."),
  ],
  cha=[
      ("Une cada alimento con su función principal: A) pan, B) huevo, C) manzana; 1) energía, 2) crecimiento y reparación, 3) vitaminas, minerales y fibra.", "A1, B2, C3", "Cada alimento aporta algo distinto."),
      ("Escribe un almuerzo que tenga energía, crecimiento y protección.", "Por ejemplo: arroz, lentejas y ensalada de lechuga", "Cada alimento aporta una función."),
  ],
  context=[("En una once hay pan, queso y una manzana. ¿Qué función principal tiene cada uno? Escribe solo el número de funciones distintas que aportan.", "3", "Pan, energía; queso, crecimiento y reparación; manzana, protección. Son 3.")],
  selfcheck=[("¿Qué grupo da mucha energía?", "Los cereales", "Son una fuente de energía."), ("¿Qué grupo ayuda al crecimiento y a la reparación?", "Lácteos, carnes, huevos o legumbres", "Ayudan a formar músculos y huesos."), ("¿Qué aportan las frutas y verduras?", "Vitaminas, minerales y fibra", "Ayudan a que el cuerpo funcione bien.")],
  open_task=task("Completa una tabla de tres columnas con las funciones: energía, crecimiento y reparación, protección y funcionamiento. En cada columna escribe tres alimentos usando solo los grupos de la clase. Después arma un almuerzo con un alimento de cada columna y dibújalo.", "Energía: pan, arroz, fideos. Crecimiento: leche, huevo, lentejas. Protección: manzana, lechuga, zanahoria. Almuerzo: arroz, lentejas y ensalada.", ["escribe tres alimentos por columna", "arma un almuerzo con las tres funciones", "dibuja el almuerzo"], ["tabla de tres columnas", "dibujo del almuerzo"], ["poner el mismo alimento en dos funciones sin explicar", "olvidar una función"], "Pregunta por qué eligió cada alimento y qué función aporta."),
  reinforce="Dibuja un plato y escribe una flecha a cada alimento con su función.",
  extend="Averigua qué alimento de tu casa tiene fibra y qué función cumple.")

L(OA6, 3,
  materials="Este cuaderno, lápiz y lápices de colores. Si quieres, anota lo que comiste durante tres días para usarlo en la actividad.",
  use="Aprenderé qué significan variedad y frecuencia al comer. Sirve para revisar si una semana de comidas es equilibrada.",
  prior=["Sé los grupos de alimentos y sus funciones.", "Sé que ningún alimento da todo lo que necesitamos."],
  explain=[
      "La variedad significa comer alimentos de distintos grupos. Un día con variedad incluye cereales, frutas y verduras, legumbres, lácteos y alimentos del grupo de carnes, pescados y huevos. La frecuencia es cada cuánto tiempo se come un alimento: todos los días, varias veces a la semana o de vez en cuando.",
      "Algunos alimentos conviene comerlos todos los días, como frutas y verduras y agua. Las legumbres y el pescado se pueden comer varias veces a la semana. Los alimentos con mucha azúcar, grasa o sal, como los dulces y las bebidas azucaradas, se comen de vez en cuando. Una porción es la cantidad de un alimento que se come de una vez.",
      "Para comparar semanas, se puede usar una tabla. Se anota cada día qué grupos aparecen y se cuenta cuántos días aparece cada uno. Si una fruta aparece solo un día en la semana, la frecuencia es baja. Al contar grupos, los alimentos con mucha azúcar, grasa o sal se cuentan como un grupo aparte. La tabla sirve para ver qué se puede mejorar sin criticar a nadie.",
  ],
  vocab=[("variedad", "comer alimentos de distintos grupos"), ("frecuencia", "cada cuánto tiempo se come un alimento"), ("porción", "cantidad de un alimento que se come de una vez"), ("equilibrada", "que incluye lo que el cuerpo necesita en cantidades adecuadas"), ("registro de comidas", "tabla donde se anota qué se comió")],
  worked=[
      ("Contar la frecuencia", "Tabla de una semana de ejemplo: fruta aparece lunes, martes, jueves y sábado. ¿Cuántos días aparece la fruta?", ["Cuento los días: lunes, martes, jueves y sábado.", "Son 4 días.", "Esa es la frecuencia de la fruta esa semana."], "4 días"),
      ("Revisar la variedad", "Un día se comió solo pan, galletas y bebida azucarada. ¿Hay variedad?", ["Cuento los grupos: cereales y un alimento con azúcar.", "Faltan frutas, verduras, lácteos y carnes, huevos o legumbres.", "No hay variedad."], "No, hay muy pocos grupos"),
  ],
  mistakes=[
      ("Decir «si como lo mismo todos los días, hay variedad».", "Variedad significa alimentos distintos.", "Cambia los alimentos y los grupos durante la semana."),
      ("Decir «una porción es lo mismo para todos».", "La cantidad depende de la edad y del cuerpo.", "Cada persona necesita una porción distinta."),
  ],
  rec=[
      ("Comer alimentos de distintos grupos se llama ______. Completa con variedad o frecuencia.", "Variedad", "La variedad es comer distintos alimentos."),
      ("¿Cada cuánto tiempo se come un alimento es la variedad o la frecuencia?", "La frecuencia", "La frecuencia es cada cuánto se come algo."),
      ("¿Las frutas y verduras conviene comerlas todos los días? Responde Sí o No.", "Sí", "Aportan vitaminas, minerales y fibra."),
  ],
  und=[
      ("¿Qué es una porción?", "La cantidad de un alimento que se come de una vez", "Cambia según cada persona."),
      ("¿Por qué conviene registrar las comidas de una semana?", "Para ver qué grupos aparecen y qué se puede mejorar", "El registro muestra la variedad y la frecuencia."),
      ("¿Cada cuánto se comen los alimentos con mucha azúcar?", "De vez en cuando", "No deben ser lo principal."),
  ],
  app=[
      arith("En un registro, la fruta aparece 4 días y la verdura 6 días. ¿Cuántos días más aparece la verdura?", "6-4", "Se resta la frecuencia de la fruta a la de la verdura."),
      ("Un día: avena con leche, lentejas con arroz y una manzana. ¿Cuántos grupos distintos hay (cereal, legumbre, lácteo, fruta)?", "4", "Avena y arroz son cereales; lentejas, legumbre; leche, lácteo; manzana, fruta. Son 4 grupos."),
      ("Un niño come siempre las mismas dos cosas. ¿Falta variedad o frecuencia?", "Variedad", "Faltan alimentos distintos."),
  ],
  rea=[
      ("Semana A: fruta 2 días y verdura 3 días. Semana B: fruta 6 días y verdura 7 días. ¿Cuál tiene más frecuencia de frutas y verduras?", "La semana B", "Aparecen más días."),
      ("Un niño dice que una semana con dulces todos los días es equilibrada. ¿Qué le respondes?", "Que los dulces se comen de vez en cuando", "No debería ser lo principal."),
  ],
  cha=[
      ("Un registro de 5 días de ejemplo: lácteos aparecen 5 días y frutas aparecen 2 días. La clase dice que las frutas conviene comerlas todos los días. ¿Qué grupo conviene aumentar?", "Frutas", "Aparecen pocos días y conviene comerlas todos los días."),
      ("Propón un cambio pequeño para que aparezca la fruta más días a la semana.", "Por ejemplo: agregar una fruta a la once", "Es un cambio fácil de hacer."),
  ],
  context=[arith("Una niña anotó cuántos grupos de alimentos comió cada día: lunes, 3; martes, 4; miércoles, 2. ¿Cuántos grupos anotó en total en los tres días?", "3+4+2", "Se suman los grupos de cada día.")],
  selfcheck=[("¿Qué es la frecuencia?", "Cada cuánto se come un alimento", "Puede ser diaria o de vez en cuando."), ("¿Qué es la variedad?", "Comer alimentos de distintos grupos", "Así el cuerpo recibe de todo."), ("¿Se puede mejorar una semana de comidas sin criticar a nadie? Responde Sí o No.", "Sí", "Se hacen cambios pequeños.")],
  open_task=task("Haz un registro de tres días de lo que comes. Si no puedes, usa este: lunes, pan, huevo y manzana; martes, arroz, lentejas y lechuga; miércoles, fideos, yogur y galletas dulces. Cuenta cuántos grupos distintos hay cada día y cuántos días aparecen fruta o verdura. Escribe un cambio pequeño que mejoraría la variedad.", "Lunes: 3 grupos. Martes: 3 grupos. Miércoles: 3 grupos, uno de alimentos dulces. Fruta o verdura: 2 días. Cambio: agregar una fruta el miércoles.", ["cuenta grupos por día", "cuenta días de fruta o verdura", "propone un cambio pequeño"], ["tabla de tres días", "conteos escritos"], ["contar mal los grupos", "criticar a una persona"], "Revisa los conteos y que el cambio sea pequeño y posible."),
  reinforce="Dibuja un plato de un día con al menos cuatro grupos de alimentos.",
  extend="Pregunta a una persona de tu casa qué alimento les gustaría comer más veces por semana.")

L(OA6, 4,
  materials="Este cuaderno, lápiz y lápices de colores. Para la actividad, con una persona adulta de tu casa: un momento para conversar sobre las comidas.",
  use="Aprenderé a proponer hábitos de alimentación saludable que sean posibles y respetuosos. Sirve para cambiar costumbres con ideas pequeñas que cada familia pueda hacer.",
  prior=["Sé qué son variedad y frecuencia.", "Sé que cada familia come según sus gustos y posibilidades."],
  explain=[
      "Un hábito es algo que se hace muchas veces hasta que se vuelve costumbre. Un hábito de alimentación saludable es, por ejemplo, tomar agua durante el día, comer frutas y verduras, desayunar antes de ir a clases y comer sin apuro. Para cambiar un hábito, conviene hacer un cambio pequeño y posible.",
      "Cada familia tiene gustos, costumbres, dinero y horarios distintos. También hay personas con alergias o con alimentación indicada por un profesional de la salud, y eso se debe respetar siempre. Una propuesta respetuosa no critica lo que otros comen. Ofrece una opción posible, como agregar una fruta de estación o cambiar una bebida azucarada por agua.",
      "Una propuesta clara dice qué se hará, cuándo y cómo se comprobará. Por ejemplo: «Agregaré una fruta a la once cuatro días esta semana y marcaré los días en una tabla». Al final de la semana se revisa si funcionó. Si no funcionó, se cambia el plan y se prueba de nuevo.",
  ],
  vocab=[("hábito", "costumbre que se repite muchas veces"), ("alergia", "reacción del cuerpo a un alimento que puede ser peligrosa"), ("respetuoso", "que no critica ni obliga a otros"), ("posible", "que se puede hacer con lo que se tiene"), ("fruta de estación", "fruta que se cosecha en esa época del año")],
  worked=[
      ("Elegir un cambio posible", "Una familia dice que esta semana las frutas están muy caras. ¿Qué cambio pequeño y posible pueden hacer?", ["Pienso en lo más barato: agua de la llave y frutas de estación.", "Elijo un cambio pequeño, como tomar agua en vez de bebida azucarada.", "Lo escribo con una frecuencia."], "Tomar agua en las comidas en vez de bebida azucarada"),
      ("Proponer con respeto", "Un niño dice a su amigo: «Tu colación es mala». ¿Cómo lo podría decir con respeto?", ["No critico lo que come mi amigo.", "Ofrezco compartir algo o contar lo que hago yo.", "Respeto sus costumbres y alergias."], "«Yo llevo una fruta, ¿quieres probar?»"),
  ],
  mistakes=[
      ("Criticar lo que come otra persona.", "Cada familia tiene sus costumbres y posibilidades.", "Ofrece una idea posible sin criticar."),
      ("Proponer un cambio gigante, como cambiarlo todo en un día.", "Es difícil mantenerlo.", "Empieza con un cambio pequeño y revisa a la semana."),
  ],
  rec=[
      ("Una costumbre que se repite muchas veces se llama ______. Completa con hábito o grupo.", "Hábito", "Es la definición de hábito."),
      ("Si un compañero tiene alergia a un alimento, ¿lo respetas o le insistes en que lo coma?", "Lo respeto", "Una alergia puede ser peligrosa."),
      ("¿Un cambio pequeño es más fácil de mantener que uno gigante? Responde Sí o No.", "Sí", "Los cambios pequeños se pueden mantener."),
  ],
  und=[
      ("Nombra dos hábitos de alimentación saludable.", "Tomar agua, comer frutas y verduras o desayunar (dos de ellos)", "Son hábitos de la clase."),
      ("¿Por qué una propuesta debe ser posible para cada familia?", "Porque cada familia tiene distintos gustos, dinero y horarios", "Si no es posible, no se puede cumplir."),
      ("¿Qué debe decir una propuesta clara?", "Qué se hará, cuándo y cómo se comprobará", "Así se puede revisar."),
  ],
  app=[
      arith("Un niño propone agregar una fruta a la once 4 días a la semana. Si cumple 3 de los 4 días, ¿cuántos días no cumplió?", "4-3", "Se resta lo cumplido a lo propuesto."),
      ("Opciones: A) «Cambiaré todo lo que como hoy mismo». B) «Tomaré agua en las comidas tres días esta semana». ¿Cuál es un cambio pequeño y posible?", "B", "Tiene una acción concreta y una frecuencia."),
      ("Una compañera tiene alergia al maní y trae su propia colación. ¿Cómo respetas esa situación?", "No ofreciéndole alimentos con maní ni burlándome", "Una alergia es seria."),
  ],
  rea=[
      ("Dos propuestas: A) «Comer sano». B) «Agregar una fruta a la once cuatro días y marcarlo en una tabla». ¿Cuál se puede comprobar?", "B", "Dice cuántos días y cómo se anota."),
      ("Un niño dice: «Esta semana las manzanas están muy caras». ¿Qué otra opción posible podría proponer?", "Una fruta de estación más barata o agua en vez de bebida azucarada", "Debe adaptarse a lo que la familia puede."),
  ],
  cha=[
      ("Escribe una propuesta de un hábito saludable con qué, cuándo y cómo lo comprobarás.", "Por ejemplo: tomaré agua en las comidas 5 días y marcaré cada día en una tabla", "Tiene acción, frecuencia y comprobación."),
      ("Cuando alguien te dice «no puedo comer eso», ¿qué haces y qué no haces?", "Lo respeto y no le insisto ni me burlo", "Puede tener una alergia o una razón de su cultura o salud."),
  ],
  context=[arith("En una semana de 5 días de clases, una niña se propone tomar agua en la colación todos los días y lo cumple 4 días. ¿En cuántos días no lo cumplió?", "5-4", "Se resta lo cumplido a los días propuestos.")],
  selfcheck=[("¿Qué es un hábito?", "Una costumbre que se repite muchas veces", "Se vuelve parte de la rutina."), ("¿Se debe criticar lo que come otra persona? Responde Sí o No.", "No", "Cada persona tiene sus costumbres y posibilidades."), ("Nombra un cambio pequeño para comer más saludable.", "Tomar agua en las comidas, agregar una fruta o desayunar", "Son cambios pequeños y posibles.")],
  open_task=task("Con una persona adulta de tu casa, conversa y elige un hábito saludable que sea posible para tu familia: A) agregar una fruta a la once, B) tomar agua en las comidas, C) desayunar antes de ir al colegio. Escribe qué harás, cuántos días y cómo lo comprobarás. Marca los días en una tabla. No critiques a nadie y respeta las alergias y costumbres. Al final escribe si funcionó.", "Elegí A. Agregaré una fruta a la once cuatro días esta semana. Marcaré cada día en una tabla. Resultado: lo cumplí 3 días. Para mejorar, dejaré la fruta a la vista.", ["elige un hábito posible", "dice qué, cuándo y cómo lo comprobará", "revisa el resultado sin criticar"], ["tabla de una semana", "frase de resultado"], ["proponer un cambio gigante", "criticar lo que comen otros"], "Valora que el plan sea posible y que la revisión no juzgue a nadie."),
  reinforce="Dibuja el hábito saludable que elegiste y escribe cuántos días lo harás.",
  extend="Escribe una frase respetuosa para invitar a un compañero a probar una fruta.")
