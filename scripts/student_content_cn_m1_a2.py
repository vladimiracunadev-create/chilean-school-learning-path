"""Cuaderno del estudiante, 1.º medio Ciencias Naturales: OA 03 (clasificación biológica y parentesco) y OA 04 (niveles de organización e interacciones en ecosistemas chilenos)."""
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


OA3 = "CN1M OA 03"
OA4 = "CN1M OA 04"

# ---------------------------------------------------------------- OA 03

L(OA3, 1,
  materials="Este cuaderno y lápiz. Los nombres científicos y los niveles de clasificación están escritos en las explicaciones y ejercicios.",
  use="Aprenderé cómo se organizan los seres vivos en grupos y subgrupos con criterios taxonómicos y cómo se escribe un nombre científico. Sirve para formular preguntas que se puedan responder comparando rasgos.",
  prior=["Sé que los seres vivos se parecen y se diferencian.", "Sé que la evolución explica el parentesco entre especies."],
  explain=[
      "La clasificación biológica ordena la diversidad de organismos en grupos y subgrupos según criterios taxonómicos, que son rasgos que se comparan: estructura del cuerpo, forma de desarrollo, tipo de célula o secuencias de ADN. Los grupos se ordenan en niveles que van de lo más amplio a lo más específico: dominio, reino, filo, clase, orden, familia, género y especie.",
      "Cada especie tiene un nombre científico de dos palabras: primero el género y después la especie. El puma se llama Puma concolor y el guanaco, Lama guanicoe. Los dos son del dominio Eukarya, reino Animalia, filo Chordata y clase Mammalia, pero pertenecen a órdenes distintos: el puma al orden Carnivora y el guanaco al orden Artiodactyla. Mientras más niveles comparten dos especies, más emparentadas están.",
      "Una pregunta investigable sobre clasificación indica qué rasgo se compara. «¿Cuántos niveles de clasificación comparten el puma y el guanaco?» se responde con datos. «¿Cuál animal es más importante?» no, porque depende de opiniones.",
  ],
  vocab=[("taxonomía", "ciencia que clasifica a los seres vivos"), ("criterio taxonómico", "rasgo que se compara para formar un grupo"), ("especie", "nivel más específico; grupo de organismos que se reproducen entre sí"), ("género", "grupo de especies muy cercanas"), ("nombre científico", "nombre de dos palabras: género y especie")],
  worked=[
      ("Leer un nombre científico", "El nombre científico del guanaco es Lama guanicoe. ¿Cuál es su género y cuál su especie?", ["El nombre tiene dos palabras.", "La primera palabra es el género y la segunda la especie."], "Género Lama, especie guanicoe"),
      ("Comparar niveles", "El puma y el guanaco comparten dominio, reino, filo y clase, pero no el orden. ¿Cuántos niveles comparten?", ["Cuento los niveles compartidos: dominio, reino, filo y clase.", "El orden es distinto, así que no cuenta."], "Cuatro niveles"),
  ],
  mistakes=[
      ("Escribir el nombre científico con una sola palabra.", "Debe tener género y especie.", "Escribe siempre las dos palabras, la primera con mayúscula."),
      ("Pensar que dos especies son parientes cercanos solo porque viven juntas.", "El parentesco se decide por rasgos compartidos y no por el lugar donde viven.", "Compara rasgos o ADN, no el hábitat."),
  ],
  rec=[
      ("¿De cuántas palabras consta un nombre científico?", "Dos", "Género y especie."),
      ("Completa: el nivel más específico de la clasificación es la ______ (especie o clase).", "Especie", "Es el último nivel de la lista."),
      ("Verdadero o falso: los niveles de clasificación van de lo más amplio a lo más específico.", "Verdadero", "Parten en el dominio y terminan en la especie."),
  ],
  und=[
      ("¿Cuál es el género de Puma concolor? A) Puma; B) concolor.", "A", "La primera palabra del nombre científico es el género."),
      ("Dos organismos comparten dominio, reino, filo, clase y orden. Otros dos solo comparten dominio y reino. ¿Cuáles están más emparentados? A) Los que comparten más niveles; B) Los que comparten menos niveles.", "A", "Más niveles compartidos indican un parentesco más cercano."),
      ("¿Qué es un criterio taxonómico?", "Un rasgo que se compara para formar un grupo", "Puede ser estructura, desarrollo o ADN."),
  ],
  app=[
      ("Se sabe que la araucaria se llama Araucaria araucana. ¿Cuál es su especie?", "araucana", "La segunda palabra es la especie."),
      arith("Un listado de ejemplo ordena 8 niveles de clasificación. Si el puma y el guanaco comparten 4 de ellos, ¿en cuántos niveles se diferencian?", "8-4", "Se resta lo compartido al total de niveles."),
      ("¿Cuál es una pregunta investigable? A) ¿Cuántos de estos rasgos comparten un gato y un lobo: pelo, mamas, cuatro patas y garras?; B) ¿Cuál animal es más bonito, el gato o el lobo?", "A", "La primera se contesta contando rasgos; la otra es de opinión."),
  ],
  rea=[
      ("Un estudiante dice que el guanaco y el puma son de la misma familia porque ambos viven en Torres del Paine. ¿Cuál es el error? A) Confunde el lugar donde viven con el parentesco, que se decide por rasgos; B) La familia no existe como nivel de clasificación.", "A", "El hábitat no es un criterio taxonómico de parentesco."),
      ("Dos especies comparten género. ¿Cuál afirmación es correcta? A) Comparten también todos los niveles superiores; B) No comparten ninguno de los niveles superiores.", "A", "Si comparten un nivel específico, comparten los niveles más amplios que lo incluyen."),
  ],
  cha=[
      ("Especies de ejemplo: Felis alfa, Felis beta, Canis alfa y Canis beta. ¿Cuántas parejas distintas de estas cuatro especies comparten género?", "2", "Felis alfa con Felis beta, y Canis alfa con Canis beta."),
      ("Un grupo quiere clasificar 5 animales de su casa y propone usar «es simpático» como criterio. ¿Qué problema tiene? A) Es una opinión y no un rasgo comparable con datos; B) Es un rasgo muy difícil de ver.", "A", "Un criterio taxonómico debe poder observarse o medirse."),
  ],
  context=[arith("En un zoológico de ejemplo hay tres géneros inventados: el género X tiene 6 especies, el género Y tiene 4 y el género Z tiene 5. ¿Cuántas especies hay en total?", "6+4+5", "Se suman las especies de los tres géneros.")],
  selfcheck=[("¿Qué dos palabras forman un nombre científico?", "Género y especie", "Primero el género y luego la especie."), ("¿Qué indica compartir más niveles de clasificación?", "Un parentesco más cercano", "El ancestro común es más reciente."), ("Nombra tres criterios taxonómicos.", "Estructura del cuerpo, forma de desarrollo y secuencias de ADN", "Son rasgos que se pueden comparar.")],
  open_task=task("Con estos datos: puma (Puma concolor), orden Carnivora; guanaco (Lama guanicoe), orden Artiodactyla; zorro culpeo (Lycalopex culpaeus), orden Carnivora. Los tres son del dominio Eukarya, reino Animalia, filo Chordata y clase Mammalia. Escribe tres preguntas investigables que se respondan con estos datos y responde una de ellas con una frase que cite los niveles compartidos.", "1) ¿Qué dos animales de la lista comparten el orden? Puma y zorro culpeo, ambos Carnivora. 2) ¿Cuántos niveles comparten los tres? Cuatro: dominio, reino, filo y clase. 3) ¿Qué nivel separa al guanaco del puma? El orden, Artiodactyla frente a Carnivora.", ["tres preguntas con datos", "cita niveles compartidos en la respuesta", "usa nombres científicos con dos palabras"], ["tres preguntas y una respuesta"], ["preguntas de opinión", "nombres científicos de una sola palabra"], "Pregunta qué nivel de la clasificación separa al puma del guanaco."),
  reinforce="Escribe el nombre científico del guanaco y marca el género y la especie.",
  extend="Explica por qué las especies de un mismo género se parecen más que dos especies de familias distintas.")

L(OA3, 2,
  materials="Este cuaderno y lápiz. La clave y las descripciones de animales están escritas en los ejercicios.",
  use="Aprenderé a usar una clave dicotómica y una tabla de rasgos para ubicar organismos en grupos. Sirve para clasificar con evidencia observable.",
  prior=["Sé que se clasifica con criterios taxonómicos.", "Sé leer tablas y seguir instrucciones paso a paso."],
  explain=[
      "Una clave dicotómica es una herramienta para identificar organismos. Cada paso ofrece dos opciones (a y b) sobre un rasgo observable; según la que corresponda, la clave dirige al siguiente paso o al nombre del grupo. Siempre se parte de rasgos claros y se avanza hacia los más específicos.",
      "Una tabla de rasgos ordena los datos. Las filas son los organismos y las columnas, los rasgos. Se anota 1 si el rasgo está presente y 0 si no lo está. Con la tabla puedes agrupar los organismos que comparten rasgos y descubrir qué rasgo separa a un grupo de otro.",
      "Para que el criterio funcione, el rasgo debe ser observable y no depender de la opinión. «Tiene pelo» es un buen rasgo; «es bonito» no lo es. Los rasgos más útiles para agrupar son los que tienen un origen común, como la columna vertebral, y no los que aparecen por separado, como las alas del insecto y del ave.",
  ],
  vocab=[("clave dicotómica", "herramienta con pares de opciones para identificar organismos"), ("rasgo", "característica observable de un organismo"), ("presente / ausente", "si el rasgo se ve o no se ve"), ("grupo", "conjunto de organismos que comparten un rasgo"), ("columna vertebral", "serie de huesos que protege la médula espinal")],
  worked=[
      ("Usar una clave", "Clave: 1a. Tiene pelo → mamífero. 1b. No tiene pelo → paso 2. 2a. Tiene plumas → ave. 2b. No tiene plumas → reptil, anfibio o pez. Un animal no tiene pelo y tiene plumas. ¿Qué es?", ["Empiezo en el paso 1: no tiene pelo, voy a la opción b.", "En el paso 2: tiene plumas, opción a."], "Un ave"),
      ("Leer una tabla de rasgos", "Tabla de ejemplo: X (pelo 1, plumas 0); Y (pelo 0, plumas 1); Z (pelo 1, plumas 0). ¿Qué organismos forman un grupo por el rasgo pelo?", ["Busco los que tienen 1 en pelo.", "Son X y Z."], "X y Z"),
  ],
  mistakes=[
      ("Empezar la clave por el paso que parece más interesante.", "La clave se sigue en el orden indicado.", "Parte siempre por el paso 1."),
      ("Agrupar por un rasgo que depende de una opinión.", "Un criterio debe ser observable por cualquier persona.", "Usa rasgos como pelo, plumas o escamas."),
  ],
  rec=[
      ("¿Qué es una clave dicotómica?", "Una herramienta con pares de opciones para identificar organismos", "Cada paso ofrece dos opciones."),
      ("En una tabla de rasgos, el número 1 significa ______ (presente o ausente).", "Presente", "El 0 indica que el rasgo no está."),
      ("Verdadero o falso: «es bonito» es un buen criterio taxonómico.", "Falso", "No se puede observar de manera objetiva."),
  ],
  und=[
      ("¿Por qué una clave dicotómica tiene solo dos opciones por paso? A) Para decidir con un rasgo claro entre dos alternativas; B) Para que sea más larga.", "A", "Cada decisión debe ser simple y sin ambigüedad."),
      ("¿Qué rasgo agrupa mejor a los animales: «tiene columna vertebral» o «es simpático»? A) Tiene columna vertebral; B) Es simpático.", "A", "Se puede observar y tiene origen común."),
      ("En una tabla, si dos organismos tienen el mismo rasgo en 1, ¿qué se puede decir de ellos?", "Comparten ese rasgo", "Los dos lo presentan."),
  ],
  app=[
      ("Clave: 1a. Tiene pelo → mamífero. 1b. No tiene pelo → paso 2. 2a. Tiene plumas → ave. 2b. No tiene plumas → paso 3. 3a. Tiene branquias toda su vida y aletas → pez. 3b. No → paso 4. 4a. Piel con escamas secas y respira por pulmones → lagarto. 4b. Piel húmeda y lisa; la larva vive en el agua → rana. Un animal no tiene pelo ni plumas, no tiene aletas ni branquias de adulto, tiene piel húmeda y lisa, y su larva vive en el agua. ¿Qué es?", "Rana", "Sigue 1b, 2b, 3b y 4b."),
      ("Con la misma clave (1a. pelo → mamífero; 1b. sin pelo → paso 2; 2a. plumas → ave; 2b. sin plumas → paso 3; 3a. branquias toda su vida y aletas → pez; 3b. no → paso 4; 4a. escamas secas y pulmones → lagarto; 4b. piel húmeda y lisa → rana), un animal no tiene pelo ni plumas, tiene branquias toda su vida y aletas. ¿Qué es?", "Pez", "Llega a 3a en el tercer paso."),
      arith("Una tabla de ejemplo tiene 5 organismos y 6 rasgos. ¿Cuántas casillas tiene la tabla?", "5*6", "Se multiplica el número de filas por el de columnas."),
  ],
  rea=[
      ("Tabla de ejemplo (1 presente, 0 ausente) con rasgos [columna vertebral, pelo, plumas]: M 1,1,0; N 1,0,1; O 1,1,0; P 0,0,0. ¿Cuál es el organismo que no tiene columna vertebral? A) P; B) M.", "A", "P es el único con 0 en la primera columna."),
      ("Un compañero propone la clave «1a. Es lindo; 1b. No es lindo». ¿Qué falla tiene? A) El rasgo no es observable: depende de la opinión; B) Tiene solo dos opciones.", "A", "Un buen rasgo debe poder comprobarse por cualquiera."),
  ],
  cha=[
      ("Tabla de ejemplo: Q (pelo 1, plumas 0, escamas 0); R (pelo 0, plumas 1, escamas 0); S (pelo 0, plumas 0, escamas 1); T (pelo 1, plumas 0, escamas 0). ¿Qué par de organismos son más parecidos en esta tabla?", "Q y T", "Tienen exactamente los mismos rasgos."),
      ("Un animal desconocido tiene alas y pelo. Una clave dice «con pelo → mamífero» y «con alas → ave». ¿Qué problema tiene esa clave? A) Los pasos no son excluyentes: un mamífero con alas, como el murciélago, cae en las dos; B) Las claves no pueden tener alas.", "A", "Las opciones de cada paso deben ser excluyentes."),
  ],
  context=[arith("En una feria de ciencias de ejemplo, 3 grupos clasifican cada uno 7 fotos de animales con una clave. ¿Cuántas fotos clasifican entre todos?", "3*7", "Se multiplica el número de grupos por las fotos de cada uno.")],
  selfcheck=[("Explica para qué sirve una clave dicotómica.", "Una herramienta con dos opciones por paso para identificar organismos", "Guía hacia el grupo correcto."), ("¿Qué indica un 0 en una tabla de rasgos?", "Que el rasgo está ausente", "El 1 indica presente."), ("Da un ejemplo de rasgo observable.", "Pelo, plumas o escamas", "Se puede ver sin depender de opiniones.")],
  open_task=task("Con esta clave: 1a. Tiene pelo → mamífero. 1b. No tiene pelo → paso 2. 2a. Tiene plumas → ave. 2b. No tiene plumas → paso 3. 3a. Piel con escamas secas → reptil. 3b. Piel húmeda → anfibio. Úsala para clasificar: (A) un animal con pelo que da leche; (B) un animal con plumas y pico; (C) un animal de piel húmeda y lisa; (D) un animal con escamas secas y sin pelo. Después propón una pregunta investigable sobre un animal que no calza bien con la clave.", "A mamífero; B ave; C anfibio; D reptil. Pregunta: «¿Qué rasgos tiene un pez que la clave no considera?»", ["clasifica los cuatro", "muestra el camino de la clave", "la pregunta indica un rasgo a observar"], ["cuatro clasificaciones y una pregunta"], ["saltarse un paso de la clave", "pregunta de opinión"], "Pregunta qué paso nuevo agregarías a la clave."),
  reinforce="Escribe una clave de dos pasos para separar a un gato, un pez y un ave.",
  extend="Explica por qué la clave dicotómica no sirve si un rasgo es ambiguo.")

L(OA3, 3,
  materials="Este cuaderno y lápiz. Los árboles están escritos en texto con paréntesis dentro de los ejercicios.",
  use="Aprenderé a leer y construir un árbol filogenético que muestra el parentesco con ancestros comunes. Sirve para ver quién está más emparentado con quién.",
  prior=["Sé que mientras más niveles comparten dos especies, más emparentadas están.", "Sé que el ancestro común es una especie antigua de la que descienden varias."],
  explain=[
      "Un árbol filogenético es un diagrama con ramas que muestra el parentesco entre especies. Cada punta es una especie y cada punto donde una rama se divide (nodo) representa a un ancestro común. Dos especies que comparten un nodo cercano están más emparentadas que dos que se unen solo en un nodo más antiguo.",
      "Un árbol puede escribirse con paréntesis. En «(A, B)» las especies A y B comparten un nodo. En «((A, B), C)», A y B se unen primero y luego se unen a C. Eso significa que A está más emparentada con B que con C. El orden de las puntas no importa; importan los nodos.",
      "Un grupo natural incluye a un ancestro común y a todos sus descendientes. El árbol es un modelo: representa hipótesis apoyadas por rasgos y ADN, y puede cambiar si aparecen datos nuevos.",
  ],
  vocab=[("árbol filogenético", "diagrama que muestra el parentesco entre especies"), ("nodo", "punto donde se divide una rama; representa un ancestro común"), ("punta", "extremo de una rama; representa una especie actual"), ("grupo natural", "ancestro común más todos sus descendientes"), ("hipótesis", "explicación que se pone a prueba con datos")],
  worked=[
      ("Leer paréntesis", "Árbol: ((gato, perro), ratón). ¿Qué especie está más emparentada con el gato?", ["El gato y el perro están en el mismo paréntesis, es decir, comparten un nodo.", "El ratón se une después."], "El perro"),
      ("Contar nodos", "Árbol: (((A, B), C), D). ¿Cuántos nodos tiene?", ["Cuento cada par de paréntesis que une ramas.", "Hay tres uniones: (A, B), luego con C y luego con D."], "3 nodos"),
  ],
  mistakes=[
      ("Pensar que las especies que están una al lado de la otra en el dibujo son parientes cercanas.", "Lo que importa son los nodos, no el orden de las puntas.", "Sigue las ramas hasta el nodo que une a las dos especies."),
      ("Creer que las especies actuales descienden unas de otras.", "Todas las puntas son especies actuales que comparten ancestros comunes.", "Interpreta un nodo como un ancestro común, no como una especie de la punta."),
  ],
  rec=[
      ("¿Qué representa un nodo en un árbol filogenético?", "Un ancestro común", "Es el punto donde se dividen las ramas."),
      ("Completa: las puntas del árbol representan ______ (especies actuales o ancestros).", "Especies actuales", "Los ancestros están en los nodos."),
      ("Verdadero o falso: el orden en que se dibujan las puntas indica el parentesco.", "Falso", "El parentesco se lee en los nodos."),
  ],
  und=[
      ("En ((A, B), C), ¿qué especie está más lejos de las otras? A) C; B) A.", "A", "C se une a A y B en un nodo más antiguo."),
      ("¿Qué quiere decir que A y B compartan un nodo reciente? A) Tienen un ancestro común más cercano entre sí que con otras; B) A desciende de B.", "A", "Un nodo es un ancestro común, no una especie actual."),
      ("En un árbol, ¿cuántas puntas tiene ((A, B), (C, D))?", "4", "Las puntas son A, B, C y D."),
  ],
  app=[
      ("Árbol de ejemplo: (((gato, perro), (oveja, vaca)), ratón). ¿Qué especie está más emparentada con la oveja?", "La vaca", "Comparte con ella el nodo más reciente."),
      ("Con el mismo árbol, (((gato, perro), (oveja, vaca)), ratón), ¿qué especie se une al resto en el nodo más antiguo?", "El ratón", "Se une al final, a todas las demás."),
      arith("Un árbol filogenético de ejemplo tiene 7 especies en sus puntas y siempre se divide en dos ramas. En ese caso tiene un nodo menos que puntas. ¿Cuántos nodos tiene?", "7-1", "Para unir 7 puntas hacen falta 6 uniones."),
  ],
  rea=[
      ("En ((A, B), C) y en (A, (B, C)), ¿cambia la lectura del parentesco? A) Sí: en el primero A y B están más emparentadas; en el segundo, B y C; B) No, porque las tres especies son las mismas.", "A", "Cambian los nodos y, con ellos, quién comparte el ancestro más reciente."),
      ("Un compañero dice: «En el árbol, el perro desciende del gato». ¿Qué responderías? A) Ambos comparten un ancestro común; ninguno desciende del otro; B) Tiene razón porque están en el mismo paréntesis.", "A", "Las puntas no son ancestros unas de otras."),
  ],
  cha=[
      ("Árbol de ejemplo: ((A, B), (C, D)). Se descubre un dato nuevo que muestra que B se parece más a C que a A. ¿Cómo cambia el árbol? A) B pasa a unirse con C en un nodo cercano; B) No cambia, porque un árbol no puede corregirse.", "A", "Un árbol se modifica cuando hay datos nuevos."),
      ("¿Cuántos nodos tiene el árbol ((A, B), (C, (D, E)))?", "4", "Los nodos son (A, B), (D, E), (C, (D, E)) y el que une los dos grupos grandes."),
  ],
  context=[arith("Un museo de ejemplo muestra 3 árboles filogenéticos con 6 especies cada uno. ¿Cuántas especies aparecen en los tres árboles?", "3*6", "Se multiplica el número de árboles por las especies de cada uno.")],
  selfcheck=[("¿Qué representa un nodo?", "Un ancestro común", "Es donde se dividen las ramas."), ("¿Cómo se sabe quién está más emparentado con quién?", "Mirando qué especies comparten el nodo más reciente", "El orden de las puntas no importa."), ("¿Qué puede hacer cambiar un árbol filogenético?", "Datos nuevos de rasgos o ADN", "Es una hipótesis.")],
  open_task=task("Con estos datos de ejemplo, escribe un árbol con paréntesis: el perro y el lobo son los más parecidos entre sí; el gato se une después a ellos; el pez se une al final a todos. Después responde: ¿qué especie está más emparentada con el gato y cuál menos?", "Árbol: (((perro, lobo), gato), pez). Más emparentada con el gato: perro y lobo (a la par). Menos: el pez.", ["árbol coherente con los datos", "identifica la especie más y menos emparentada", "usa nodos para justificar"], ["árbol escrito y respuesta"], ["poner el pez junto al perro", "olvidar un paréntesis"], "Pregunta qué dato nuevo cambiaría la posición del gato."),
  reinforce="Dibuja un árbol con cuatro especies y marca el nodo más antiguo.",
  extend="Explica por qué un árbol filogenético es un modelo y no una fotografía del pasado.")

L(OA3, 4,
  materials="Este cuaderno y lápiz. Las tablas de rasgos y de ADN están escritas en los ejercicios.",
  use="Aprenderé a relacionar el número de rasgos compartidos con el parentesco y a distinguir semejanza por ancestro común de semejanza por convergencia. Sirve para no sacar conclusiones apresuradas.",
  prior=["Sé leer una tabla de rasgos con 1 y 0.", "Sé que un árbol agrupa por ancestros comunes."],
  explain=[
      "Si dos especies comparten muchos rasgos que heredaron de un ancestro común, es probable que estén muy emparentadas. Al contar los rasgos en que coinciden dos especies, obtienes una medida de semejanza. En general, más coincidencias significan parentesco más cercano.",
      "Pero hay una trampa: la convergencia. Dos especies no emparentadas pueden desarrollar rasgos parecidos porque viven en ambientes similares. El delfín y el tiburón tienen forma de torpedo y aletas, pero el delfín es un mamífero que amamanta y respira aire, mientras que el tiburón es un pez. Por eso se prefieren los rasgos con origen común y los datos de ADN.",
      "Para analizar la relación entre variables, ordena los datos: variable 1 (número de coincidencias) y variable 2 (cercanía del parentesco). Si al aumentar una también aumenta la otra, hay una relación. Aun así, una relación no prueba la causa; hace falta un modelo y más evidencia.",
  ],
  vocab=[("coincidencia", "rasgo igual en dos especies"), ("convergencia", "parecido que aparece por ambientes similares, sin ancestro común cercano"), ("semejanza", "grado en que dos organismos se parecen"), ("relación entre variables", "cuando un cambio en una acompaña un cambio en la otra"), ("evidencia independiente", "dato que llega por un camino distinto")],
  worked=[
      ("Contar coincidencias", "W = 110100 y X = 110110 (cada cifra es un rasgo; 1 presente, 0 ausente). ¿En cuántos rasgos coinciden?", ["Comparo cifra por cifra: 1-1, 1-1, 0-0, 1-1, 0-1, 0-0.", "Coinciden 5 de 6."], "5 rasgos"),
      ("Detectar convergencia", "El delfín y el tiburón tienen forma de torpedo. ¿Prueba eso que estén muy emparentados?", ["La forma puede venir del ambiente acuático.", "El delfín amamanta y respira aire, rasgos que el tiburón no tiene."], "No, es una convergencia"),
  ],
  mistakes=[
      ("Concluir parentesco por un solo rasgo parecido.", "Un rasgo puede aparecer por convergencia.", "Compara varios rasgos y confirma con ADN."),
      ("Decir que la relación entre variables demuestra una causa.", "Dos variables pueden cambiar juntas sin que una cause a la otra.", "Usa «se asocia con» y declara la limitación."),
  ],
  rec=[
      ("¿Qué indica un mayor número de rasgos compartidos de origen común?", "Un parentesco más cercano", "Se heredaron del ancestro común."),
      ("Completa: un parecido que surge por vivir en ambientes similares se llama ______ (convergencia o herencia).", "Convergencia", "No implica ancestro común cercano."),
      ("Verdadero o falso: la forma de torpedo prueba que el delfín y el tiburón son parientes cercanos.", "Falso", "Es una convergencia."),
  ],
  und=[
      ("¿Por qué es mejor usar varios rasgos y el ADN que un solo rasgo? A) Porque un rasgo aislado puede deberse a convergencia; B) Porque los rasgos no sirven.", "A", "Varios datos independientes reducen el riesgo de error."),
      ("El ala del insecto y el ala del ave sirven para volar. ¿Es una semejanza por parentesco cercano? A) No, es convergencia; B) Sí, comparten el plan de huesos.", "A", "Tienen distinto origen."),
      ("Si al aumentar las coincidencias de rasgos aumenta la cercanía del parentesco, ¿qué se observa entre las variables?", "Una relación", "Las dos cambian juntas."),
  ],
  app=[
      ("Tabla de ejemplo con 6 rasgos: W = 110100; X = 110110; Y = 101001; Z = 001001. ¿En cuántos rasgos coinciden Y y Z?", "5", "Solo difiere el primer rasgo."),
      ("Con la misma tabla (W = 110100; X = 110110; Y = 101001; Z = 001001), ¿en cuántos rasgos coinciden W e Y?", "2", "Coinciden el primero y el quinto."),
      ("Con la misma tabla (W = 110100; X = 110110; Y = 101001; Z = 001001), ¿cuál pareja de especies tiene más coincidencias: Y-Z o W-Z?", "Y-Z", "Y y Z coinciden en 5 rasgos y W y Z en uno solo."),
  ],
  rea=[
      ("Con la tabla de ejemplo (W = 110100; X = 110110; Y = 101001; Z = 001001), un estudiante dice que X está más emparentada con Y que con W. ¿Qué datos lo contradicen? A) X coincide con W en 5 rasgos y con Y en solo 1; B) X y Y tienen el mismo número de rasgos.", "A", "5 coincidencias con W son más que 1 con Y."),
      ("Un murciélago y un ave tienen alas. Un equipo concluye que están muy emparentados. ¿Qué evidencia anatómica y de desarrollo lo contradice? A) El murciélago tiene pelo y amamanta, rasgos de mamíferos; B) Ambos viven en cuevas.", "A", "Los rasgos de origen común lo ubican entre los mamíferos."),
  ],
  cha=[
      ("Diferencias de ADN con una especie base X: especie 1, 3; especie 2, 12; especie 3, 7. Ordena de la más cercana a la más lejana de X escribiendo los números separados por comas.", "1, 3, 2", "Menos diferencias indican un ancestro común más reciente: 3, 7 y 12."),
      ("Un investigador propone usar solo un rasgo para armar un árbol. ¿Qué crítica es más razonable? A) Un solo rasgo puede producir un árbol equivocado si hay convergencia; B) Los árboles necesitan rasgos de colores.", "A", "Hay que contrastar con más datos."),
  ],
  context=[arith("En un laboratorio de ejemplo se comparan 6 rasgos en 4 especies. Cada comparación entre pares da una cifra de coincidencias. ¿Cuántos pares distintos de especies se pueden armar con 4 especies?", "4*3//2", "Se multiplica 4 por 3 y se divide por 2 porque el orden no importa.")],
  selfcheck=[("¿Qué es la convergencia?", "Un parecido que surge por ambientes similares sin parentesco cercano", "Puede engañar al clasificar."), ("¿Qué indica el aumento de rasgos compartidos de origen común?", "Mayor cercanía de parentesco", "Es una relación entre variables."), ("¿Por qué conviene confirmar con ADN?", "Porque aporta una evidencia independiente", "Reduce los errores por convergencia.")],
  open_task=task("Con esta tabla de ejemplo (6 rasgos; 1 presente, 0 ausente): P = 101100; Q = 101101; R = 010010; S = 010011. Cuenta las coincidencias entre P y Q, entre R y S, entre P y R y entre Q y S. Escribe qué pares están más emparentados y qué dato adicional pedirías para confirmarlo.", "P-Q: 5; R-S: 5; P-R: 1; Q-S: 1. Más emparentados P con Q, y R con S. Pediría las secuencias de ADN para confirmarlo.", ["cuatro conteos", "elige los pares con más coincidencias", "propone un dato adicional"], ["cuatro conteos y una conclusión"], ["contar solo los 1", "no pedir ningún dato extra"], "Pregunta qué pasaría si un rasgo fuese convergente."),
  reinforce="Escribe un ejemplo de rasgo parecido por convergencia en dos animales.",
  extend="Explica por qué la semejanza externa puede engañar al clasificar organismos.")

L(OA3, 5,
  materials="Este cuaderno y lápiz. Los cambios históricos de la clasificación están resumidos en los ejercicios.",
  use="Aprenderé por qué la clasificación cambia con el tiempo y cómo pasó de dos reinos a tres dominios con nuevas evidencias. Sirve para entender que la ciencia corrige sus grupos.",
  prior=["Sé qué es un árbol filogenético.", "Sé que el ADN es una evidencia de parentesco."],
  explain=[
      "La clasificación se construye a lo largo del tiempo. Hace siglos se agrupaba a los seres vivos solo en plantas y animales. Con el microscopio se descubrieron los microorganismos y se hicieron más reinos: animales, plantas, hongos, protistas y bacterias. Después, el estudio del ADN y de las moléculas mostró que las bacterias se dividen en dos grupos muy distintos. Así se propusieron tres dominios: Bacteria, Archaea y Eukarya.",
      "El criterio cambió: antes se usaba sobre todo la forma externa; hoy se usan también la estructura de la célula y las secuencias de ADN. Por ejemplo, los hongos se agrupaban con las plantas porque no se mueven, pero el ADN muestra que están más emparentados con los animales que con las plantas, por lo que forman un reino propio.",
      "Un mecanismo de la clasificación moderna es agrupar solo grupos naturales: un ancestro y todos sus descendientes. Si el ADN o un fósil nuevo muestra que un grupo mezcla ramas distintas, se reorganiza. Esto no significa que los científicos se equivocaban sin sentido, sino que se mejora el modelo con nueva evidencia.",
  ],
  vocab=[("dominio", "nivel más amplio de la clasificación"), ("Bacteria", "dominio de las bacterias comunes, formadas por células sin núcleo"), ("Archaea", "dominio de células sin núcleo distintas de las bacterias"), ("Eukarya", "dominio de células con núcleo"), ("reino", "nivel de clasificación bajo el dominio")],
  worked=[
      ("Por qué cambia un grupo", "Los hongos se clasificaban con las plantas porque no se mueven. El ADN mostró que están más cerca de los animales. ¿Qué se hizo?", ["La nueva evidencia contradice el criterio anterior.", "Se reorganizó el grupo."], "Se creó un reino propio para los hongos"),
      ("Contar dominios", "Los tres dominios son Bacteria, Archaea y Eukarya. ¿Cuál agrupa a los organismos con células con núcleo, como plantas y animales?", ["Busco el dominio de células con núcleo.", "Es Eukarya."], "Eukarya"),
  ],
  mistakes=[
      ("Pensar que la clasificación nunca cambia.", "Cambia cuando hay datos nuevos.", "Piensa en la clasificación como un modelo que se mejora."),
      ("Creer que Archaea es igual a Bacteria.", "El ADN y la química muestran que son dominios distintos.", "Recuerda los tres dominios: Bacteria, Archaea y Eukarya."),
  ],
  rec=[
      ("¿Cuántos dominios se proponen en la clasificación actual que se estudia?", "Tres", "Bacteria, Archaea y Eukarya."),
      ("Completa: hoy los hongos forman un reino propio porque el ADN los acerca a los ______ (animales o plantas).", "Animales", "Están más emparentados con los animales."),
      ("Verdadero o falso: la clasificación se modifica cuando aparece evidencia nueva.", "Verdadero", "Es parte del trabajo científico."),
  ],
  und=[
      ("¿Qué herramienta permitió descubrir los microorganismos y ampliar los reinos? A) El microscopio; B) La balanza.", "A", "Mostró organismos que no se veían a simple vista."),
      ("¿Qué criterio se suma hoy a la forma externa? A) Las secuencias de ADN; B) El color de los organismos.", "A", "El ADN aporta evidencia de parentesco."),
      ("¿A qué dominio pertenecen los animales?", "Eukarya", "Sus células tienen núcleo."),
  ],
  app=[
      ("Un grupo de ejemplo reúne a un pez y a un delfín por vivir en el agua. ¿Qué evidencia llevaría a separar al delfín? A) Es un mamífero que amamanta y respira aire; B) Que nada más rápido que el pez.", "A", "Los rasgos de origen común lo ubican con los mamíferos."),
      arith("Un afiche de ejemplo muestra los 5 reinos clásicos y dibuja 4 organismos de cada reino. ¿Cuántos organismos dibuja?", "5*4", "Se multiplica el número de reinos por los organismos de cada uno."),
      ("Un científico descubre un fósil que muestra que dos ramas de un grupo no comparten ancestro cercano. ¿Qué debe hacer con el grupo? A) Reorganizarlo para que sea un grupo natural; B) Mantenerlo igual para no cambiar los libros.", "A", "Un grupo natural incluye a un ancestro y a todos sus descendientes."),
  ],
  rea=[
      ("Una persona dice: «Los científicos cambian la clasificación porque no se ponen de acuerdo». ¿Qué respuesta es mejor? A) Cambia porque aparece evidencia nueva, como el ADN; B) Cambia porque los nombres se aburren.", "A", "El cambio responde a datos, no a capricho."),
      ("Dos grupos de bacterias tienen diferencias en su ADN y su química tan grandes como las que separan a un animal de una bacteria. ¿Qué conclusión de clasificación es razonable? A) Pertenecen a dominios distintos; B) Son la misma especie.", "A", "La gran diferencia molecular justifica separarlos."),
  ],
  cha=[
      ("Línea de tiempo de ejemplo: la clasificación tuvo 2 reinos, luego 5 reinos y luego 3 dominios. ¿Cuántos reinos más había en la etapa de 5 reinos que en la primera?", "3", "5 menos 2 es 3."),
      ("Un museo quiere dibujar la clasificación como una escalera de peldaños de menos a más importante. ¿Qué problema tiene? A) Sugiere que unos grupos son más importantes, pero el árbol solo muestra parentesco; B) Las escaleras no se pueden dibujar.", "A", "Los grupos son ramas, no peldaños de importancia."),
  ],
  context=[arith("En un museo de ejemplo, 12 afiches muestran organismos del dominio Eukarya, 5 del dominio Bacteria y 4 del dominio Archaea. ¿Cuántos afiches hay?", "12+5+4", "Se suman los afiches de los tres dominios.")],
  selfcheck=[("Nombra los tres dominios.", "Bacteria, Archaea y Eukarya", "Son los tres grandes grupos."), ("¿Por qué cambió la clasificación?", "Por nueva evidencia como el microscopio y el ADN", "Se mejora el modelo."), ("¿Qué es un grupo natural?", "Un ancestro común y todos sus descendientes", "Debe incluir a todos.")],
  open_task=task("Escribe una línea de tiempo de tres etapas con estos datos: etapa 1, plantas y animales; etapa 2, cinco reinos; etapa 3, tres dominios. En cada etapa anota qué nueva evidencia o herramienta apoyó el cambio (microscopio, estructura de la célula, ADN) y un ejemplo de grupo que cambió de lugar (hongos). Cierra con una frase que explique por qué la ciencia corrige sus clasificaciones.", "Etapa 1: plantas y animales. Etapa 2: cinco reinos, apoyado por el microscopio. Etapa 3: tres dominios, apoyado por el ADN. Ejemplo: los hongos pasaron de plantas a reino propio. Cierre: porque nuevas evidencias permiten mejorar el modelo.", ["tres etapas en orden", "relaciona etapa y evidencia", "explica por qué se corrige"], ["línea de tiempo y frase final"], ["invertir el orden", "no nombrar la evidencia"], "Pregunta qué evidencia nueva podría cambiar la clasificación en el futuro."),
  reinforce="Escribe un ejemplo de grupo que cambió de reino al descubrirse nueva evidencia.",
  extend="Explica por qué se prefiere un grupo natural a uno que mezcla ramas distintas.")

# ---------------------------------------------------------------- OA 04

L(OA4, 1,
  materials="Este cuaderno y lápiz. Los casos de ecosistemas chilenos y sus datos están escritos en los ejercicios.",
  use="Aprenderé los niveles de organización de los seres vivos (organismo, población, comunidad y ecosistema) con ejemplos de Chile. Sirve para formular preguntas investigables en un ecosistema.",
  prior=["Sé que los seres vivos interactúan con su ambiente.", "Sé que una pregunta investigable se contesta con datos."],
  explain=[
      "Los seres vivos se organizan en niveles. Un organismo es un ser vivo individual, como un guanaco. Una población es el conjunto de organismos de la misma especie que viven en un lugar, como los guanacos de un parque. Una comunidad reúne a todas las poblaciones de distintas especies que conviven allí: guanacos, pumas, pastos y aves. Un ecosistema es la comunidad más el ambiente físico: el suelo, el agua, el aire y el clima.",
      "En Chile hay ecosistemas muy distintos: el desierto de Atacama, el bosque valdiviano, los humedales costeros y las estepas de la Patagonia. En cada uno, la comunidad cambia según el clima. Para estudiarlos se miden datos, como el número de individuos de una población en un área.",
      "Una pregunta investigable sobre un ecosistema indica qué se mide y dónde. «¿Cuántos guanacos hay por kilómetro cuadrado en una estepa de ejemplo?» se contesta contando. «¿Es mejor la estepa que el bosque?» no, porque depende de opiniones. La densidad de población es el número de individuos dividido por el área.",
  ],
  vocab=[("organismo", "ser vivo individual"), ("población", "organismos de la misma especie que viven en un lugar"), ("comunidad", "todas las poblaciones que conviven en un lugar"), ("ecosistema", "comunidad más ambiente físico"), ("densidad de población", "número de individuos por unidad de área")],
  worked=[
      ("Nivel de organización", "«Los 60 guanacos de una estepa de la Patagonia.» ¿Qué nivel es?", ["Son individuos de una misma especie en un lugar.", "Eso es una población."], "Población"),
      ("Calcular una densidad", "En una estepa de ejemplo de 20 km² viven 80 guanacos. ¿Cuál es la densidad?", ["Divido el número de individuos entre el área.", "80 dividido por 20 es 4."], "4 guanacos por km²"),
  ],
  mistakes=[
      ("Llamar comunidad a un grupo de individuos de una sola especie.", "La comunidad incluye varias especies.", "Cuenta cuántas especies hay en el grupo."),
      ("Pensar que el ecosistema solo incluye a los seres vivos.", "También incluye el ambiente físico: suelo, agua, aire y clima.", "Agrega siempre el ambiente a la comunidad."),
  ],
  rec=[
      ("¿Cómo se llama el ser vivo individual?", "Organismo", "Es el nivel más pequeño de la organización."),
      ("Completa: los organismos de una misma especie en un lugar forman una ______ (población o comunidad).", "Población", "La comunidad incluye varias especies."),
      ("Verdadero o falso: el ecosistema incluye la comunidad y el ambiente físico.", "Verdadero", "Esa es su definición."),
  ],
  und=[
      ("«Guanacos, pumas, pastos y aves de un parque.» ¿Qué nivel es? A) Comunidad; B) Población.", "A", "Reúne varias especies que conviven."),
      ("¿Qué agrega el ecosistema respecto de la comunidad? A) El ambiente físico, como suelo, agua y clima; B) Más individuos de la misma especie.", "A", "Es el nivel que integra lo vivo y lo no vivo."),
      ("Un pingüino de Humboldt es un ______ (organismo o población).", "Organismo", "Un individuo es un organismo."),
  ],
  app=[
      arith("En una estepa de ejemplo de 15 km² viven 90 guanacos. ¿Cuántos guanacos hay por km²?", "90//15", "Se divide el número de individuos entre el área.", " por km²"),
      ("Una laguna costera de ejemplo tiene 200 aves de una especie, 50 peces de una especie, 30 cangrejos de una especie y plantas acuáticas. ¿Cuántas poblaciones se mencionan como animales? A) 3 poblaciones (aves, peces y cangrejos); B) 280 poblaciones.", "A", "Cada especie es una población distinta."),
      ("Para saber cuántos zorros culpeo hay en un parque, ¿qué dato se debe medir? A) El número de zorros que se cuentan en un área conocida; B) El color de las flores del parque.", "A", "El tamaño de la población se obtiene contando individuos en un área."),
  ],
  rea=[
      ("Un estudiante dice: «El bosque valdiviano es una población». ¿Cuál es la corrección? A) Es un ecosistema, porque incluye muchas especies y el ambiente; B) Es un organismo grande.", "A", "Incluye comunidades y ambiente."),
      ("Dos parques de ejemplo: el A tiene 120 guanacos en 30 km² y el B tiene 150 guanacos en 50 km². ¿En cuál es mayor la densidad? Responde A o B.", "A", "El A tiene 4 por km² y el B tiene 3 por km²."),
  ],
  cha=[
      ("Un humedal de ejemplo tiene 400 aves de 8 especies. Si hay la misma cantidad de individuos por especie, ¿cuántos individuos tiene cada población?", "50", "400 dividido entre 8 es 50."),
      ("Un equipo mide los peces de una laguna una sola tarde. ¿Qué limitación tiene su conteo? A) Puede no representar la población de todo el año; B) Los peces no se pueden contar.", "A", "Una medición en un día puntual puede variar con la época."),
  ],
  context=[arith("En una excursión escolar de ejemplo se cuentan 12 aves, 8 insectos grandes y 5 plantas con flor en un humedal. ¿Cuántos individuos se anotaron en total?", "12+8+5", "Se suman los individuos de los tres grupos.")],
  selfcheck=[("¿Qué diferencia hay entre población y comunidad?", "La población es de una especie y la comunidad reúne varias especies", "Se diferencian en el número de especies."), ("¿Qué incluye un ecosistema?", "Comunidad y ambiente físico", "Suma lo vivo y lo no vivo."), ("¿Cómo se calcula la densidad de población?", "Dividiendo el número de individuos entre el área", "Es individuos por unidad de área.")],
  open_task=task("Un ecosistema de ejemplo de la Patagonia tiene: 90 guanacos, 4 pumas, mucho pasto, 30 aves de una especie, un río, el viento y el clima frío en un área de 30 km². Clasifica cada elemento como organismo, población, comunidad o ambiente físico y calcula la densidad de guanacos. Escribe una pregunta investigable sobre una población del ecosistema.", "Guanaco: organismo; 90 guanacos: población; guanacos, pumas, pasto y aves: comunidad; río, viento y clima: ambiente. Densidad: 90 dividido entre 30 es 3 guanacos por km². Pregunta: «¿Cuántos pumas hay por km²?»", ["clasifica los elementos", "calcula la densidad con la división", "la pregunta indica qué se mide"], ["clasificación, cálculo y pregunta"], ["llamar comunidad a la población", "olvidar la unidad"], "Pregunta qué cambiaría si el área fuera el doble."),
  reinforce="Escribe un ejemplo de organismo, uno de población y uno de comunidad de un ecosistema chileno.",
  extend="Explica por qué la densidad sirve para comparar poblaciones de áreas distintas.")

L(OA4, 2,
  materials="Este cuaderno y lápiz. Las descripciones de interacciones y los casos chilenos están escritos en los ejercicios.",
  use="Aprenderé a reconocer las interacciones biológicas (depredación, competencia, comensalismo, mutualismo y parasitismo) en casos de Chile. Sirve para interpretar una tabla de observaciones.",
  prior=["Sé los niveles de organización.", "Sé leer una tabla de datos."],
  explain=[
      "Las interacciones biológicas son las relaciones entre organismos de una comunidad. En la depredación, un depredador mata y come a su presa; por ejemplo, el puma y el guanaco. En la competencia, dos organismos usan el mismo recurso limitado y ambos pierden. En el comensalismo, uno se beneficia y el otro no sufre daño ni beneficio, como un helecho que crece sobre un tronco.",
      "En el mutualismo, ambos se benefician: un picaflor se alimenta del néctar de una flor y transporta su polen. Los líquenes son un mutualismo entre un hongo y un alga. En el parasitismo, el parásito se beneficia y el hospedero sufre daño; el quintral, una planta que crece sobre árboles, les quita agua y nutrientes.",
      "Para reconocer una interacción, pregunta: ¿quién gana y quién pierde? Los signos más (+) para el que se beneficia, menos (−) para el que se perjudica y cero (0) para el que no cambia, ayudan a decidir. Una interacción se clasifica con datos observables y no con suposiciones.",
  ],
  vocab=[("depredación", "un organismo mata y come a otro"), ("competencia", "dos organismos usan el mismo recurso limitado"), ("comensalismo", "uno se beneficia y el otro ni gana ni pierde"), ("mutualismo", "ambos se benefician"), ("parasitismo", "uno se beneficia y el hospedero se daña")],
  worked=[
      ("Clasificar con signos", "Un helecho crece sobre el tronco de un árbol y no lo daña. ¿Qué interacción es?", ["El helecho se beneficia (+).", "El árbol no gana ni pierde (0)."], "Comensalismo"),
      ("Reconocer un mutualismo", "Un picaflor toma néctar de una flor y lleva su polen a otra. ¿Qué interacción es?", ["El picaflor se alimenta (+).", "La flor se poliniza (+)."], "Mutualismo"),
  ],
  mistakes=[
      ("Llamar parasitismo a cualquier relación donde uno gana.", "En el parasitismo el otro sufre daño; en el comensalismo no.", "Pregunta siempre cómo le va al otro organismo."),
      ("Confundir depredación con parasitismo.", "El depredador mata y come a su presa; el parásito vive a costa del hospedero, que suele seguir vivo.", "Pregunta si el organismo muere enseguida."),
  ],
  rec=[
      ("¿Cuál interacción beneficia a ambos organismos?", "Mutualismo", "Ambos organismos ganan algo."),
      ("Completa: el quintral que se alimenta de un árbol es un caso de ______ (parasitismo o mutualismo).", "Parasitismo", "El árbol sufre daño."),
      ("Verdadero o falso: en el comensalismo, el otro organismo no sufre daño.", "Verdadero", "No gana ni pierde."),
  ],
  und=[
      ("El puma caza un guanaco. ¿Qué interacción es? A) Depredación; B) Mutualismo.", "A", "Un organismo mata y come a otro."),
      ("Dos plantas de un matorral usan el agua limitada del mismo suelo y ambas crecen menos. ¿Qué interacción es? A) Competencia; B) Comensalismo.", "A", "Ambas pierden por usar un mismo recurso."),
      ("Un liquen está formado por un hongo y un alga que se benefician mutuamente. ¿Qué interacción es?", "Mutualismo", "Ambos organismos ganan algo."),
  ],
  app=[
      ("Tabla de ejemplo: caso 1, un zorro culpeo se come un conejo; caso 2, un musgo crece sobre una roca sin dañarla; caso 3, una garrapata se alimenta de la sangre de un perro; caso 4, un picaflor poliniza una flor. ¿En qué caso hay parasitismo?", "Caso 3", "La garrapata se beneficia y el perro sufre daño."),
      ("Con la misma tabla (caso 1, un zorro culpeo se come un conejo; caso 2, un musgo crece sobre una roca sin dañarla; caso 3, una garrapata se alimenta de la sangre de un perro; caso 4, un picaflor poliniza una flor), ¿en qué caso hay comensalismo?", "Caso 2", "El musgo gana y la roca no cambia."),
      arith("En una tabla de ejemplo se anotaron 7 casos de depredación, 4 de competencia y 3 de mutualismo. ¿Cuántos casos se anotaron en total?", "7+4+3", "Se suman los casos de cada tipo."),
  ],
  rea=[
      ("Un compañero dice que una polilla que se posa sobre un árbol y es comida por un ave es mutualismo. ¿Qué corrección haces? A) Es depredación: el ave se beneficia y la polilla muere; B) Es comensalismo: nadie sufre daño.", "A", "El ave gana y la presa pierde."),
      ("Un compañero clasifica como comensalismo el caso de un ave que construye su nido entre las ramas de un árbol sin dañarlo. ¿Es correcto? A) Sí: el ave gana refugio y el árbol no gana ni pierde; B) No: es depredación porque el ave está sobre el árbol.", "A", "Uno gana y el otro ni gana ni pierde."),
  ],
  cha=[
      ("Un cuadro de ejemplo clasifica 20 interacciones. 8 son mutualismo, 5 son depredación y el resto parasitismo. ¿Cuántas son parasitismo?", "7", "20 menos 8 menos 5 es 7."),
      ("Un estudiante observa a un pájaro que come insectos de la piel de una vaca. El pájaro se alimenta y la vaca se libra de insectos. ¿Qué interacción es probable? A) Mutualismo; B) Depredación.", "A", "Ambos se benefician."),
  ],
  context=[arith("Una guía de campo de ejemplo anota 6 casos de mutualismo, 9 de depredación y 5 de competencia en una semana. ¿Cuántas interacciones anota?", "6+9+5", "Se suman las interacciones de cada tipo.")],
  selfcheck=[("¿Qué diferencia hay entre parasitismo y depredación?", "El parásito vive a costa del hospedero y el depredador lo mata y come", "Cambia el efecto en el otro organismo."), ("¿Qué signos tiene el mutualismo?", "Más para los dos", "Ambos se benefician."), ("Da un ejemplo de comensalismo.", "Un helecho que crece sobre un tronco sin dañarlo", "Uno gana y el otro no cambia.")],
  open_task=task("Clasifica cada caso de ejemplo como depredación, competencia, comensalismo, mutualismo o parasitismo y escribe los signos (+, −, 0) de cada organismo: (1) un picaflor y una flor que poliniza; (2) un puma y un guanaco; (3) dos aves que comen los mismos frutos del mismo árbol cuando hay pocos; (4) un musgo sobre un tronco; (5) un quintral sobre un árbol.", "1 mutualismo (+,+); 2 depredación (+,−); 3 competencia (−,−); 4 comensalismo (+,0); 5 parasitismo (+,−).", ["cinco clasificaciones", "signos correctos", "justifica con quién gana y quién pierde"], ["tabla de cinco filas"], ["confundir parasitismo con comensalismo", "olvidar los signos"], "Pregunta qué cambiaría en el caso 3 si hubiera frutos de sobra."),
  reinforce="Escribe una frase que explique cómo reconocer un mutualismo.",
  extend="Explica por qué una misma pareja de especies puede cambiar de interacción según la situación.")

L(OA4, 3,
  materials="Hojas y lápices de colores. Si no tienes, usa solo lápiz y escribe los nombres en cajas unidas por flechas.",
  use="Aprenderé a construir un modelo de las relaciones alimentarias de un ecosistema chileno y a contrastarlo con la realidad. Sirve para predecir qué ocurre si desaparece una especie.",
  prior=["Sé las interacciones biológicas.", "Sé que los modelos simplifican la realidad."],
  explain=[
      "Una red trófica es un modelo que muestra quién se alimenta de quién. Cada flecha apunta desde el alimento hacia quien lo come, e indica el paso de la energía. Los productores, como los pastos, fabrican su alimento con luz; los consumidores comen a otros; los descomponedores reciclan restos.",
      "Ejemplo de una estepa de la Patagonia: el pasto es comido por el guanaco y el guanaco es cazado por el puma. El cóndor se alimenta de animales muertos. Cada uno de estos pasos es una conexión de la red. Si desaparece un nivel, cambian los demás: si no hay pasto, el guanaco no tiene alimento.",
      "Un modelo siempre simplifica: muchas relaciones reales no aparecen y las flechas no muestran cuánto se come. Contrastar un modelo consiste en compararlo con observaciones y ver qué explica y qué deja afuera. Si no coincide con los datos, se corrige.",
  ],
  vocab=[("red trófica", "modelo de relaciones de alimentación en un ecosistema"), ("productor", "organismo que fabrica su alimento, como el pasto"), ("consumidor", "organismo que se alimenta de otros"), ("descomponedor", "organismo que recicla restos de seres vivos"), ("flecha", "indica el paso de energía desde el alimento hacia quien lo come")],
  worked=[
      ("Dibujar una cadena", "Pasto, guanaco y puma. ¿Cómo se ordenan las flechas?", ["Las flechas van del alimento a quien lo come.", "Pasto → guanaco → puma."], "Pasto → guanaco → puma"),
      ("Predecir un cambio", "Si desaparece el pasto de la estepa, ¿qué ocurre con el guanaco?", ["El pasto es su alimento.", "Sin alimento, su población disminuye."], "Su población disminuye"),
  ],
  mistakes=[
      ("Dibujar la flecha desde el que come hacia el alimento.", "La flecha muestra el paso de la energía, que va del alimento a quien lo come.", "Lee la flecha como «le da energía a»."),
      ("Creer que el modelo muestra todas las relaciones del ecosistema.", "Un modelo siempre simplifica.", "Pregunta qué relaciones dejó afuera."),
  ],
  rec=[
      ("¿Hacia dónde apunta la flecha en una red trófica?", "Desde el alimento hacia quien lo come", "Muestra el paso de la energía."),
      ("Completa: el pasto, que fabrica su alimento con luz, es un ______ (productor o consumidor).", "Productor", "Los productores fabrican su alimento."),
      ("Verdadero o falso: los descomponedores reciclan restos de seres vivos.", "Verdadero", "Devuelven materia al ambiente."),
  ],
  und=[
      ("En la cadena pasto → guanaco → puma, ¿quién es el consumidor que se alimenta del guanaco? A) El puma; B) El pasto.", "A", "El puma recibe la energía del guanaco."),
      ("¿Qué es un modelo de red trófica? A) Un diagrama que simplifica quién se alimenta de quién; B) Una foto de todo el ecosistema.", "A", "Es una representación simplificada."),
      ("¿Qué hace un descomponedor?", "Recicla restos de seres vivos", "Devuelve materia al suelo."),
  ],
  app=[
      ("Red de ejemplo: pasto → guanaco; pasto → liebre; guanaco → puma; liebre → zorro culpeo. ¿Cuántos consumidores hay?", "4", "Son guanaco, liebre, puma y zorro culpeo."),
      ("Con la misma red (pasto → guanaco; pasto → liebre; guanaco → puma; liebre → zorro culpeo), ¿qué dos animales se alimentan directamente del pasto?", "El guanaco y la liebre", "Reciben la flecha del pasto."),
      arith("Una red de ejemplo tiene 6 flechas y se le agregan 3 nuevas relaciones alimentarias. ¿Cuántas flechas tiene ahora?", "6+3", "Se suman las flechas nuevas a las que había."),
  ],
  rea=[
      ("Con la red (pasto → guanaco; pasto → liebre; guanaco → puma; liebre → zorro culpeo), una enfermedad mata a todas las liebres. ¿Qué efecto directo tiene en el zorro culpeo? A) Pierde una fuente de alimento y su población puede disminuir; B) Aumenta porque tiene más pasto.", "A", "El zorro depende de la liebre en este modelo."),
      ("Un compañero dice que su modelo es perfecto porque tiene todas las flechas. ¿Qué respuesta es mejor? A) Ningún modelo tiene todas las relaciones, y siempre hay que compararlo con observaciones; B) Tiene razón si dibujó muchas flechas.", "A", "Un modelo simplifica y debe contrastarse."),
  ],
  cha=[
      ("Observación de ejemplo: los zorros culpeos también comen guanacos jóvenes y no solo liebres. El modelo no lo incluye. ¿Qué debería hacerse? A) Agregar una flecha de guanaco a zorro y revisar las predicciones; B) Ignorar la observación.", "A", "Un modelo se corrige cuando una observación no calza."),
      ("Si en la red (pasto → guanaco; pasto → liebre; guanaco → puma; liebre → zorro culpeo) se agrega la flecha guanaco → zorro culpeo, ¿cuántos alimentos distintos tiene el zorro culpeo?", "2", "Se alimenta de la liebre y del guanaco."),
  ],
  context=[arith("Una guía de ejemplo del parque dibuja 3 redes tróficas de 5 organismos cada una. ¿Cuántos organismos dibuja en total?", "3*5", "Se multiplica el número de redes por los organismos de cada una.")],
  selfcheck=[("¿Qué indica el sentido de cada flecha en el modelo de red trófica?", "Que la energía pasa hacia quien come", "Muestra el paso de la energía del alimento al consumidor."), ("¿Qué es un productor?", "Un organismo que fabrica su alimento", "El pasto es un ejemplo."), ("¿Por qué hay que contrastar un modelo?", "Porque simplifica y puede dejar afuera relaciones reales", "Se compara con observaciones.")],
  open_task=task("Con estos datos de ejemplo de una estepa de la Patagonia, dibuja una red trófica con flechas: el pasto es comido por el guanaco y por la liebre; el puma se alimenta del guanaco; el zorro culpeo se alimenta de la liebre; el cóndor se alimenta de animales muertos de cualquier especie. Luego predice qué pasaría con el puma si las enfermedades redujeran a los guanacos a la mitad.", "Pasto → guanaco, pasto → liebre, guanaco → puma, liebre → zorro, animales muertos → cóndor. Con la mitad de guanacos, el puma tendría menos alimento y su población podría disminuir o cambiar su dieta.", ["dibuja las flechas en la dirección correcta", "incluye los cinco organismos", "predice con una razón"], ["dibujo y predicción"], ["invertir las flechas", "no justificar la predicción"], "Pregunta qué relación del modelo no está en el dibujo."),
  reinforce="Dibuja una cadena de tres organismos de un ecosistema chileno.",
  extend="Explica por qué eliminar un productor afecta a toda la red.")

L(OA4, 4,
  materials="Este cuaderno, lápiz y regla. Los datos de poblaciones están escritos en tablas de ejemplo dentro de los ejercicios.",
  use="Aprenderé a relacionar el tamaño de una población de presas con el de sus depredadores y a leer una tabla en el tiempo. Sirve para describir patrones con datos.",
  prior=["Sé que la depredación beneficia al depredador y perjudica a la presa.", "Sé leer tablas y comparar números."],
  explain=[
      "En un ecosistema, el tamaño de una población cambia con el tiempo. Cuando una población de presas aumenta, los depredadores tienen más alimento y su población también puede aumentar. Luego, al haber más depredadores, las presas disminuyen. Con menos presas, los depredadores disminuyen. Este ciclo muestra una relación entre dos variables.",
      "Para estudiarlo se registra una tabla con el tiempo (años) y el tamaño de cada población. En los datos de ejemplo, si las presas suben de 200 a 300 y luego bajan a 150, y los depredadores suben después, se dice que el cambio de los depredadores va con retraso respecto de las presas.",
      "Una relación entre variables no prueba una causa. Otros factores pueden influir, como la sequía o una enfermedad. Por eso se habla de «patrón» y se declara que se necesita más evidencia para afirmar el mecanismo.",
  ],
  vocab=[("presa", "animal que es cazado por un depredador"), ("depredador", "animal que caza y come a otro"), ("tamaño de población", "número de individuos de la población"), ("retraso", "cambio que ocurre un tiempo después de otro"), ("patrón", "regularidad que se repite en los datos")],
  worked=[
      ("Leer una tabla", "Tabla de ejemplo: año 1, presas 300, depredadores 20; año 2, presas 400, depredadores 25; año 3, presas 250, depredadores 40. ¿En qué año hay más depredadores?", ["Busco el valor más alto en la columna de depredadores.", "El valor 40 está en el año 3."], "Año 3"),
      ("Describir un patrón", "En la tabla, las presas bajan de 400 a 250 cuando los depredadores suben de 25 a 40. ¿Qué relación se observa?", ["Una variable sube mientras la otra baja.", "Más depredadores se asocian con menos presas."], "Cuando aumentan los depredadores, disminuyen las presas"),
  ],
  mistakes=[
      ("Decir que el aumento de depredadores causa siempre el descenso de presas.", "Pueden influir la sequía, las enfermedades u otros factores.", "Usa «se asocia con» y pide más datos."),
      ("Leer la tabla sin fijarse en la unidad de tiempo.", "Los cambios se interpretan según los años o los meses.", "Revisa qué indica cada columna."),
  ],
  rec=[
      ("Si aumentan las presas, ¿qué suele pasar después con los depredadores?", "Pueden aumentar", "Tienen más alimento."),
      ("Completa: un animal que es cazado por otro es una ______ (presa o depredadora).", "Presa", "El que caza es el depredador."),
      ("Verdadero o falso: una relación entre dos variables prueba siempre una causa.", "Falso", "Puede haber otros factores."),
  ],
  und=[
      ("¿Por qué el cambio de los depredadores ocurre con retraso respecto de las presas? A) Porque necesitan tiempo para reproducirse cuando hay más alimento; B) Porque no ven a las presas.", "A", "La reproducción lleva tiempo."),
      ("¿Qué indica una tabla donde las presas bajan mientras los depredadores suben? A) Una relación inversa entre las dos variables; B) Que ambas aumentan juntas.", "A", "Una sube y la otra baja."),
      ("¿Qué indica el término «patrón» en los datos?", "Una regularidad que se repite", "Se observa en varios momentos."),
  ],
  app=[
      ("Tabla de ejemplo: año 1, liebres 500, zorros 20; año 2, liebres 650, zorros 25; año 3, liebres 450, zorros 35; año 4, liebres 300, zorros 30. ¿En qué año hay más liebres?", "Año 2", "El mayor valor de liebres es 650."),
      arith("Con la misma tabla (año 1, liebres 500; año 2, 650; año 3, 450; año 4, 300), ¿cuántas liebres menos hay en el año 4 que en el año 2?", "650-300", "Se resta el valor del año 4 al del año 2."),
      arith("En un humedal de ejemplo, una población de aves aumenta 15 individuos por año durante 4 años, desde 120. ¿Cuántas aves hay al final de los 4 años?", "120+15*4", "Se suma lo que aumenta cada año al valor inicial."),
  ],
  rea=[
      ("Con la tabla (año 1, liebres 500, zorros 20; año 2, 650 y 25; año 3, 450 y 35; año 4, 300 y 30), un compañero concluye que los zorros comen todas las liebres. ¿Qué dato lo contradice? A) Las liebres no desaparecen: en el año 4 aún hay 300; B) Los zorros aumentan.", "A", "Quedan liebres, así que el ciclo continúa."),
      ("Una sequía reduce el pasto en el año 3 de un ecosistema de ejemplo. Un estudiante atribuye toda la baja de presas a los depredadores. ¿Qué crítica es mejor? A) No considera la sequía como otro factor; B) Los depredadores no comen presas.", "A", "Hay más de una explicación posible."),
  ],
  cha=[
      ("Tabla de ejemplo: mes 1, presas 800, depredadores 40; mes 2, 600, 50; mes 3, 400, 55; mes 4, 450, 45. ¿En cuántos individuos bajaron las presas entre el mes 1 y el mes 3?", "400", "800 menos 400 es 400."),
      ("En una tabla de ejemplo, ¿qué gráfico representa mejor los datos de dos poblaciones en el tiempo? A) Un gráfico de líneas con el tiempo en el eje horizontal; B) Un gráfico circular.", "A", "Las líneas muestran cómo cambian las variables en el tiempo."),
  ],
  context=[arith("Un guardaparque de ejemplo cuenta 40 aves el lunes, 55 el martes y 35 el miércoles. ¿Cuántas aves contó en total esos tres días?", "40+55+35", "Se suman los conteos de los tres días.")],
  selfcheck=[("¿Qué ocurre con los depredadores cuando aumentan las presas?", "Pueden aumentar con retraso", "Tienen más alimento."), ("¿Una relación entre variables prueba la causa?", "No", "Pueden influir otros factores."), ("¿Qué gráfico muestra mejor datos en el tiempo?", "Un gráfico de líneas", "Muestra los cambios.")],
  open_task=task("Con esta tabla de ejemplo de un ecosistema, escribe una conclusión de dos oraciones y una limitación. Tabla: año 1, ratones 600, aves rapaces 10; año 2, ratones 800, aves rapaces 12; año 3, ratones 500, aves rapaces 20; año 4, ratones 300, aves rapaces 18.", "Los ratones aumentaron de 600 a 800 y luego bajaron a 300, mientras las aves rapaces subieron de 10 a 20 y después bajaron a 18. La baja de ratones se asocia con más aves rapaces. Limitación: son solo cuatro años y pudo influir el clima.", ["cita al menos dos datos", "describe el patrón", "declara una limitación"], ["conclusión y limitación"], ["afirmar una causa segura", "no citar datos"], "Pregunta qué dato más agregarías para decidir."),
  reinforce="Describe con una frase qué le ocurre a las presas cuando suben los depredadores.",
  extend="Explica por qué el ciclo de depredadores y presas puede repetirse en el tiempo.")

L(OA4, 5,
  materials="Este cuaderno y lápiz. Los casos de interacciones y sus efectos están escritos en los ejercicios.",
  use="Aprenderé a explicar el mecanismo de cada interacción por sus efectos (+, −, 0) y a distinguir interacciones parecidas. Sirve para explicar por qué ocurre un patrón en una comunidad.",
  prior=["Sé nombrar las cinco interacciones.", "Sé usar los signos +, − y 0."],
  explain=[
      "Cada interacción tiene un patrón de efectos sobre los dos organismos. Depredación: (+, −). Competencia: (−, −). Comensalismo: (+, 0). Mutualismo: (+, +). Parasitismo: (+, −). Explicar una interacción es decir qué recurso o beneficio pasa de uno a otro.",
  "La depredación y el parasitismo tienen los mismos signos, pero se distinguen en el modo: el depredador mata a su presa y la come; el parásito vive sobre o dentro de otro organismo y sigue en contacto mucho tiempo, sin matarlo enseguida. La competencia ocurre cuando el recurso es limitado: si hay de sobra, la competencia casi no se nota.",
      "Las interacciones también pueden regular poblaciones. La competencia por alimento limita el tamaño de una población. El mutualismo puede ser necesario: algunas plantas dependen de ciertos animales para polinizarse. Entender el mecanismo permite predecir qué pasa si una especie desaparece.",
  ],
  vocab=[("recurso limitado", "algo que no alcanza para todos, como agua o alimento"), ("hospedero", "organismo del que vive un parásito"), ("polinizar", "llevar polen de una flor a otra"), ("beneficio", "ganancia que recibe un organismo"), ("mecanismo", "forma en que ocurre un proceso")],
  worked=[
      ("Explicar por efectos", "Dos aves comen los mismos frutos y hay pocos. ¿Cómo se explica el signo de cada ave?", ["El recurso es limitado.", "Cada una come menos por la otra, así que ambas pierden."], "Competencia (−, −)"),
      ("Distinguir parecidas", "Una garrapata vive en la piel de un perro y se alimenta de su sangre durante días. ¿Es depredación o parasitismo?", ["El perro no muere enseguida.", "La garrapata vive sobre el perro."], "Parasitismo"),
  ],
  mistakes=[
      ("Pensar que la competencia siempre existe entre especies parecidas.", "Solo ocurre cuando el recurso no alcanza.", "Revisa si el recurso es limitado."),
      ("Creer que el mutualismo es un favor consciente.", "Es un efecto que beneficia a ambos, sin intención.", "Describe qué gana cada uno."),
  ],
  rec=[
      ("¿Qué signos tiene la competencia?", "Menos y menos (−, −)", "Ambos organismos pierden recursos."),
      ("Completa: el organismo del que vive un parásito se llama ______ (hospedero o presa).", "Hospedero", "Sufre daño pero suele seguir vivo."),
      ("Verdadero o falso: la competencia ocurre solo cuando el recurso es limitado.", "Verdadero", "Si hay de sobra, no se nota."),
  ],
  und=[
      ("¿Qué diferencia hay entre depredación y parasitismo? A) El depredador mata y come; el parásito vive a costa del hospedero; B) No hay ninguna diferencia.", "A", "El modo en que obtienen el recurso es distinto."),
      ("¿Qué gana una flor de un picaflor? A) Que lleve su polen a otra flor; B) Que se coma sus hojas.", "A", "Se poliniza, que es su beneficio."),
      ("Un helecho crece sobre un tronco sin dañarlo. ¿Qué signos tiene el árbol?", "Cero", "No gana ni pierde."),
  ],
  app=[
      ("Una planta de ejemplo depende de un solo insecto para polinizarse y desaparece el insecto. ¿Qué es lo más probable que ocurra con la planta? A) Producirá menos semillas; B) Producirá más semillas.", "A", "Sin polinizador, disminuye la reproducción."),
      arith("Un parque de ejemplo tiene 120 aves que dependen de un fruto. Cuando el fruto escasea, la mitad de las aves se va a otro lugar. ¿Cuántas aves se van?", "120//2", "La mitad de 120 es 60."),
      ("Un matorral de ejemplo tiene dos arbustos que dependen del mismo agua escasa. ¿Qué interacción tienen? A) Competencia; B) Mutualismo.", "A", "Comparten un recurso limitado y ambos pierden."),
  ],
  rea=[
      ("Una persona dice que el depredador es siempre el «malo» del ecosistema. ¿Qué respuesta usa evidencia? A) Los depredadores regulan las poblaciones de presas y evitan que consuman todo el pasto; B) Los depredadores no tienen función.", "A", "Mantienen el equilibrio de las poblaciones."),
      ("En una isla de ejemplo desaparece un depredador y la población de su presa se triplica, el pasto se acaba y luego la presa disminuye. ¿Qué mecanismo lo explica? A) La presa agota su alimento al quedar sin control; B) La presa se escapa.", "A", "Sin regulación, la presa agota el recurso."),
  ],
  cha=[
      ("Una población de ejemplo de 30 plantas necesita 3 polinizadores cada una para producir semillas. Hay 60 polinizadores. ¿Cuántas plantas se polinizan?", "20", "60 dividido entre 3 es 20 plantas."),
      ("Un estudiante registra que cuando aumentan los parásitos, el hospedero adelgaza. ¿Qué mecanismo explica esto? A) El parásito consume parte de los nutrientes del hospedero; B) El hospedero se aburre.", "A", "Pierde recursos que el parásito utiliza."),
  ],
  context=[arith("En una laguna de ejemplo, 4 especies de aves compiten por 36 peces diarios. Si reparten los peces por igual, ¿cuántos peces le tocan a cada especie?", "36//4", "Se divide el recurso entre las especies.")],
  selfcheck=[("¿Cuáles son los signos del comensalismo?", "Más y cero", "Uno gana y el otro no cambia."), ("¿Cuándo hay competencia?", "Cuando dos organismos usan un recurso limitado", "El recurso no alcanza para ambos."), ("¿Qué función cumplen los depredadores en el ecosistema?", "Regulan las poblaciones de presas", "Evitan que crezcan sin control.")],
  open_task=task("Elige uno de estos tres casos de ejemplo y explica su mecanismo en cuatro oraciones usando los signos y la palabra «recurso»: (A) dos especies de aves y poco alimento; (B) un picaflor y las flores que poliniza; (C) un árbol y el quintral que crece sobre él.", "Caso C: el quintral se beneficia (+) porque toma agua y nutrientes del árbol, el recurso. El árbol sufre daño (−) porque pierde parte de esos recursos. Es un parasitismo porque el quintral vive sobre él. Si hay muchos quintrales, el árbol puede debilitarse.", ["nombra la interacción", "usa los signos", "explica qué recurso pasa de un organismo al otro"], ["párrafo de cuatro oraciones"], ["no mencionar el recurso", "confundir con depredación"], "Pregunta qué pasaría si desapareciera uno de los organismos."),
  reinforce="Escribe los signos de las cinco interacciones.",
  extend="Explica por qué el mutualismo puede volver vulnerable a una especie.")

L(OA4, 6,
  materials="Este cuaderno y lápiz. Los casos y las medidas están escritos en los ejercicios.",
  use="Aprenderé a evaluar los efectos de una especie introducida y a observar fauna de manera segura y respetuosa. Sirve para tomar decisiones con evidencia y cuidado.",
  prior=["Sé las interacciones y las redes tróficas.", "Sé que un modelo tiene límites."],
  explain=[
      "Una especie introducida es una especie que llegó a un ecosistema desde otro lugar por acción humana. Si se establece y causa daño, se llama especie invasora. En Chile, por ejemplo, el castor se introdujo en Tierra del Fuego y el visón americano se propagó por la Patagonia. Pueden competir con especies nativas, comerlas o cambiar el ambiente, como cuando un castor construye un dique.",
      "Evaluar un problema ambiental exige datos y límites. Un conteo en un solo día no muestra la variación del año. Una medida de control tiene costos y efectos: eliminar una especie introducida puede ayudar a las nativas, pero requiere cuidado y no debe hacerse por cuenta propia. Se informa a las autoridades o a una persona adulta responsable.",
      "Al observar fauna silvestre, se mantiene la distancia, no se alimenta ni se toca a los animales, no se arrancan plantas y se avisa a una persona adulta si se ve un animal herido. Estas normas protegen a las personas y al ecosistema. Observar es una forma de investigar sin alterar lo que se estudia.",
  ],
  vocab=[("especie introducida", "especie llevada a un lugar donde no vivía antes"), ("especie invasora", "especie introducida que causa daño"), ("especie nativa", "especie que vive en un lugar de forma natural"), ("control", "medida para reducir una población dañina"), ("distancia segura", "separación que evita molestar o dañar a un animal")],
  worked=[
      ("Evaluar una medida", "Un grupo propone eliminar una especie invasora. ¿Qué dos preguntas deben hacerse?", ["¿Qué beneficio tiene para las especies nativas?", "¿Qué costos o riesgos tiene la medida?"], "Beneficio para las nativas y costos o riesgos"),
      ("Acción segura", "Una persona ve un zorro que parece enfermo en un parque. ¿Qué hace?", ["No se acerca ni lo toca.", "Avisa a una persona adulta o a un guardaparque."], "No lo toca y avisa a una persona adulta"),
  ],
  mistakes=[
      ("Soltar una mascota exótica en un parque «para liberarla».", "Puede convertirse en especie invasora y dañar a las nativas.", "Consulta a una persona adulta o a un especialista."),
      ("Acercarse a un animal silvestre para fotografiarlo.", "Puede morder, enfermar o estresar al animal.", "Mantén la distancia y observa con calma."),
  ],
  rec=[
      ("¿Qué es una especie invasora?", "Una especie introducida que causa daño", "Compite o altera el ecosistema."),
      ("Completa: una especie que vive de forma natural en un lugar es ______ (nativa o invasora).", "Nativa", "Está en su ecosistema de origen."),
      ("Verdadero o falso: se puede alimentar a un animal silvestre para ayudarlo.", "Falso", "Altera su conducta y puede dañarlo."),
  ],
  und=[
      ("¿Cómo puede dañar el visón americano a las especies nativas? A) Come aves y peces y compite por el alimento; B) Les quita la luz del sol.", "A", "Es un depredador introducido."),
      ("¿Qué hace el castor que cambia el ecosistema? A) Construye diques que inundan zonas; B) Come pasto de las estepas.", "A", "Los diques modifican el agua y el bosque."),
      ("Si ves un animal herido en un parque, ¿qué debes hacer?", "No tocarlo y avisar a una persona adulta", "Evita riesgos para ti y para el animal."),
  ],
  app=[
      ("Un equipo cuenta aves nativas una sola tarde y concluye que hay pocas en todo el año. ¿Qué límite tiene? A) El conteo de un día puede no representar el año; B) Las aves no se pueden contar.", "A", "Falta repetir el conteo en distintas épocas."),
      arith("En una zona de ejemplo había 120 aves nativas y, tras la llegada de una especie invasora, hay 78. ¿Cuántas aves nativas menos hay?", "120-78", "Se resta el valor actual al anterior."),
      ("Para observar un ave en un parque, ¿qué conducta es adecuada? A) Observar a distancia con calma y sin alimentarla; B) Acercarse para fotografiarla de cerca.", "A", "Mantiene la distancia segura."),
  ],
  rea=[
      ("Un grupo propone liberar depredadores de otro país para controlar una plaga. ¿Qué riesgo tiene esa medida? A) Los depredadores nuevos podrían volverse invasores; B) No habría plaga.", "A", "Introducir especies puede crear nuevos problemas."),
      ("Un folleto dice que todas las especies introducidas son dañinas. ¿Qué respuesta es mejor? A) Algunas no se establecen o no causan daño, pero las invasoras sí, y se evalúa caso a caso; B) Tiene razón, sin excepciones.", "A", "Se necesita evidencia en cada caso."),
  ],
  cha=[
      ("Datos de ejemplo: en un humedal había 90 aves nativas por km²; tras la invasión de una especie, bajaron a 54. ¿En qué porcentaje bajó la densidad? Responde con el número de porcentaje.", "40", "La baja es de 36 sobre 90, que equivale a 40 de cada 100."),
      ("Una medida de control propone cazar a la especie invasora. ¿Qué evidencia se necesita para evaluarla? A) Cuántos individuos hay, cuánto daño causan y qué efectos tendría la medida; B) Solo la opinión de una persona.", "A", "La decisión debe apoyarse en datos y no solo en opiniones."),
  ],
  context=[arith("En un parque de ejemplo, un guardaparque anota 18 observaciones de aves nativas en la mañana y 14 en la tarde, a distancia segura. ¿Cuántas observaciones anota en total?", "18+14", "Se suman las observaciones de la mañana y de la tarde.")],
  selfcheck=[("Define especie invasora con tus palabras.", "Una especie introducida que daña el ecosistema", "Puede competir con las nativas."), ("¿Qué normas se siguen al observar fauna?", "Mantener la distancia, no alimentar ni tocar", "Protegen a las personas y a los animales."), ("¿Por qué un conteo de un día tiene límites?", "Porque puede variar según la época", "No muestra el año completo.")],
  open_task=task("Lee este caso de ejemplo: un castor se estableció en un río y construyó un dique que inundó un bosque, y las aves de la zona disminuyeron. Propón una medida a evaluar (por ejemplo, un monitoreo de aves con conteos cada mes), dos datos que medirías y un riesgo. Termina con una acción segura que tomaría un estudiante que observa el lugar.", "Medida: monitorear aves cada mes. Datos: número de aves por km² y superficie inundada. Riesgo: que el conteo mensual no explique el cambio por sí solo. Acción segura: observar desde lejos y avisar a una persona adulta o a un guardaparque.", ["medida evaluable", "dos datos medibles", "acción segura y respetuosa"], ["medida, datos, riesgo y acción"], ["proponer tocar o capturar animales", "no citar datos"], "Pregunta cómo sabrías si la medida funcionó."),
  reinforce="Escribe tres normas para observar fauna silvestre sin dañarla.",
  extend="Explica por qué una medida de control requiere datos antes de aplicarse.")
