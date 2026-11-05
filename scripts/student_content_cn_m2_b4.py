"""Cuaderno del estudiante, 2.º medio Ciencias Naturales: OA 17 (carbono, biomoléculas e hidrocarburos) y OA 18 (estereoquímica e isomería de compuestos orgánicos)."""
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


OA17 = "CN2M OA 17"
OA18 = "CN2M OA 18"
MAT = "Este cuaderno y lápiz. Todas las fórmulas y datos están escritos en el cuaderno y son de ejemplo; no necesitas manipular sustancias."

# ---------------------------------------------------------------- OA 17

L(OA17, 1,
  materials=MAT,
  use="Aprenderé por qué el carbono puede formar tantas moléculas, qué son las biomoléculas y los hidrocarburos, y cómo escribir una pregunta investigable sobre ellos.",
  prior=["Sé que los átomos se unen formando moléculas.", "Sé que los símbolos C, H, O y N representan carbono, hidrógeno, oxígeno y nitrógeno."],
  explain=[
      "El carbono es un átomo con cuatro electrones de valencia, que son los electrones que usa para unirse a otros átomos. Por eso forma cuatro enlaces covalentes, es decir, comparte electrones. Puede unirse a hidrógeno, oxígeno, nitrógeno y a otros carbonos, y así forma cadenas, ramas y anillos. Esa capacidad explica que existan millones de compuestos de carbono.",
      "Los enlaces entre átomos pueden ser simples, dobles o triples. Un enlace doble cuenta como dos y uno triple como tres. En cualquier compuesto, cada carbono suma cuatro enlaces en total. En el metano, CH4, un carbono se une a cuatro hidrógenos. En el etano, C2H6, dos carbonos se unen entre sí y cada uno completa sus enlaces con tres hidrógenos.",
      "Las biomoléculas son compuestos de carbono que forman a los seres vivos: carbohidratos, lípidos, proteínas y ácidos nucleicos. Los hidrocarburos son compuestos formados solo por carbono e hidrógeno, como los que hay en el petróleo y sus derivados. Una pregunta investigable nombra algo que se puede contar o medir. «¿Cuántos hidrógenos se unen a un carbono con cuatro enlaces simples?» se contesta con un modelo; «¿Cuál molécula es más linda?» no.",
  ],
  vocab=[("enlace covalente", "unión en la que dos átomos comparten electrones"), ("electrón de valencia", "electrón que un átomo usa para formar enlaces"), ("biomolécula", "compuesto de carbono que forma a los seres vivos"), ("hidrocarburo", "compuesto formado solo por carbono e hidrógeno"), ("cadena", "serie de átomos de carbono unidos entre sí")],
  worked=[
      ("Completar enlaces", "Un carbono está unido a 3 hidrógenos por enlaces simples. ¿Cuántos enlaces más necesita para completar los cuatro?", ["Tiene 3 enlaces simples con hidrógeno.", "Necesita 4 − 3 = 1 enlace más."], "1 enlace más, por ejemplo con otro carbono"),
      ("Reconocer un hidrocarburo", "¿Es el compuesto C2H6 un hidrocarburo?", ["Un hidrocarburo tiene solo carbono e hidrógeno.", "La fórmula C2H6 tiene solo C y H."], "Sí, es un hidrocarburo (etano)"),
  ],
  mistakes=[
      ("Decir que el carbono puede formar cinco enlaces si uno es doble.", "Un enlace doble cuenta como dos y el total sigue siendo cuatro.", "Suma los enlaces de cada carbono y comprueba que den cuatro."),
      ("Llamar hidrocarburo a cualquier compuesto con carbono.", "Un hidrocarburo tiene solo carbono e hidrógeno.", "Revisa si hay otros elementos en la fórmula."),
  ],
  rec=[
      ("¿Cuántos enlaces forma un átomo de carbono en total?", "Cuatro", "Tiene cuatro electrones de valencia para compartir."),
      ("Verdadero o falso: el metano CH4 tiene un carbono unido a cuatro hidrógenos.", "Verdadero", "La fórmula indica un C y cuatro H."),
      ("¿Qué dos elementos forman un hidrocarburo?", "Carbono e hidrógeno", "Esa es la definición de hidrocarburo."),
  ],
  und=[
      ("¿Por qué existen tantos compuestos de carbono? A) Porque forma cuatro enlaces y puede unirse en cadenas y anillos; B) Porque es el elemento más abundante de la Tierra.", "A", "La variedad viene de sus enlaces y sus uniones entre carbonos."),
      ("¿Cuál de estas fórmulas es un hidrocarburo? A) CH4; B) CH4O.", "A", "CH4 tiene solo carbono e hidrógeno; la otra tiene oxígeno."),
      ("¿Cuál de estos es una biomolécula? A) Una proteína; B) Un trozo de cobre.", "A", "Las proteínas son compuestos de carbono de los seres vivos."),
  ],
  app=[
      arith("Una cadena se escribe CH3–CH2–CH2–CH2–CH3. ¿Cuántos hidrógenos tiene en total?", "3+2+2+2+3", "Cada CH3 tiene 3 H y cada CH2 tiene 2 H.", " hidrógenos"),
      arith("Un carbono tiene un doble enlace con un oxígeno y un enlace con un hidrógeno. ¿Cuántos enlaces más necesita para completar cuatro?", "4-(2+1)", "El doble enlace cuenta 2 y el enlace con H cuenta 1."),
      ("¿Cuál pregunta es investigable? A) ¿Cuántos hidrógenos tiene la molécula CH3–CH2–CH3?; B) ¿Es el petróleo una sustancia molesta?", "A", "La que pregunta por los hidrógenos se contesta contando átomos; la otra es una opinión."),
  ],
  rea=[
      ("Un compañero dice: «Un carbono con un enlace doble forma cinco enlaces». ¿Qué le respondes? A) El doble enlace cuenta como dos, y el total sigue siendo cuatro; B) Tiene razón.", "A", "El carbono siempre suma cuatro enlaces."),
      ("¿Por qué «¿Cuál molécula es más linda?» no es una pregunta investigable? A) Porque depende de gustos y no se puede medir; B) Porque las moléculas son pequeñas.", "A", "Una pregunta investigable debe poder responderse con datos."),
  ],
  cha=[
      arith("En la cadena CH3–CH2–CH2–CH3, ¿cuántos enlaces carbono–carbono hay?", "4-1", "Cuatro carbonos en fila se unen por tres enlaces."),
      ("Un compuesto tiene un carbono unido a un oxígeno, tres hidrógenos y ningún otro átomo. ¿Es un hidrocarburo? A) No, porque tiene oxígeno; B) Sí, porque tiene carbono.", "A", "Un hidrocarburo no puede tener oxígeno."),
  ],
  context=[("Gas de uso doméstico de ejemplo: una etiqueta dice que contiene butano, C4H10. ¿Es un hidrocarburo? A) Sí, porque tiene solo C y H; B) No, porque es un gas.", "A", "La fórmula solo tiene carbono e hidrógeno.")],
  selfcheck=[("¿Cuántos enlaces suma cada carbono?", "Cuatro", "Un enlace doble cuenta como dos."), ("¿Qué es un hidrocarburo?", "Un compuesto formado solo por carbono e hidrógeno", "No tiene otros elementos."), ("Nombra dos biomoléculas.", "Proteínas y lípidos", "También hay carbohidratos y ácidos nucleicos.")],
  open_task=task("Mira estas fórmulas: CH4, C3H8, C2H6O y C6H12O6. Indica cuáles son hidrocarburos y cuáles no, con una razón. Luego escribe una pregunta investigable sobre cuántos hidrógenos tiene una cadena de carbonos con enlaces simples.", "CH4 y C3H8 son hidrocarburos porque solo tienen C y H; C2H6O y C6H12O6 tienen oxígeno. Pregunta: ¿Cuántos hidrógenos tiene una cadena de 4 carbonos unidos por enlaces simples?", ["clasifica las cuatro fórmulas", "da una razón por la clasificación", "la pregunta se puede contestar contando"], ["una clasificación y una pregunta"], ["llamar hidrocarburo a todo lo que tenga carbono", "escribir una pregunta de opinión"], "Pregunta cómo comprobarías tu respuesta con un modelo de bolas y palitos dibujado."),
  reinforce="Dibuja la molécula CH4 con un carbono al centro y cuatro hidrógenos unidos.",
  extend="Explica por qué la capacidad del carbono de formar cadenas permite tantos compuestos.")

TBIO = "Tabla de ejemplo de biomoléculas: carbohidratos, elementos C, H y O, función principal energía; lípidos, C, H y O, reserva de energía y componentes de membranas; proteínas, C, H, O y N, estructura y aceleración de reacciones; ácidos nucleicos, C, H, O, N y P, información genética. "

L(OA17, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla sobre biomoléculas, a ver qué elementos tienen y qué funciones cumplen, y a reconocer las limitaciones de una tabla simplificada.",
  prior=["Sé que el carbono forma cuatro enlaces.", "Sé qué es una biomolécula."],
  explain=[
      "Las biomoléculas tienen siempre carbono e hidrógeno y casi siempre oxígeno. Los carbohidratos y los lípidos tienen carbono, hidrógeno y oxígeno. Las proteínas añaden nitrógeno. Los ácidos nucleicos, como el ADN, añaden nitrógeno y fósforo. Leer en una tabla qué elementos aparecen permite reconocer a qué tipo de biomolécula corresponde un dato.",
      "Muchas biomoléculas son grandes porque se forman al unir unidades pequeñas. La glucosa, de fórmula C6H12O6, se une con otras glucosas y forma el almidón. Los aminoácidos se unen y forman proteínas. Cada unidad de glucosa aporta seis carbonos, así que se puede estimar cuántos carbonos tiene una cadena contando sus unidades.",
      "Una tabla simplifica: dice una función principal de cada grupo, pero cada grupo cumple varias funciones. Por eso una conclusión debe decir «función principal» y no «única función». También hay que fijarse en qué dice la tabla y en qué no dice, sin agregar datos que no estén escritos.",
  ],
  vocab=[("carbohidrato", "biomolécula con C, H y O que aporta energía"), ("lípido", "biomolécula con C, H y O que reserva energía"), ("proteína", "biomolécula con C, H, O y N"), ("ácido nucleico", "biomolécula con C, H, O, N y P que guarda información genética"), ("unidad", "molécula pequeña que se une a otras para formar una grande")],
  worked=[
      ("Elegir por elementos", "Una biomolécula de ejemplo tiene C, H, O y N pero no P. ¿Cuáles de la tabla podría ser?", ["Necesita nitrógeno: proteínas o ácidos nucleicos.", "No tiene fósforo, así que no es ácido nucleico."], "Proteína"),
      ("Contar carbonos", "Una cadena de ejemplo de almidón tiene 20 unidades de glucosa. ¿Cuántos átomos de carbono aportan las unidades?", ["Cada glucosa aporta 6 carbonos.", "20 × 6 = 120."], "120 átomos de carbono"),
  ],
  mistakes=[
      ("Decir que cada biomolécula tiene una sola función.", "La tabla da la función principal, pero hay otras.", "Escribe «función principal» en la conclusión."),
      ("Agregar a la tabla datos que no aparecen.", "Una conclusión se apoya en lo que dicen los datos.", "Cita la fila de la tabla que usas."),
  ],
  rec=[
      (TBIO + "¿Qué biomolécula contiene fósforo?", "Los ácidos nucleicos", "Solo esa fila incluye P."),
      (TBIO + "¿Qué elementos tienen los carbohidratos?", "C, H y O", "Se lee en la primera fila."),
      ("Verdadero o falso: la glucosa tiene la fórmula C6H12O6.", "Verdadero", "Esa es la fórmula de la glucosa."),
  ],
  und=[
      (TBIO + "¿Cuál es la función principal de los ácidos nucleicos? A) Guardar información genética; B) Aportar energía.", "A", "Así lo indica la tabla."),
      (TBIO + "¿Qué elemento distingue a las proteínas de los carbohidratos? A) El nitrógeno; B) El oxígeno.", "A", "Las proteínas tienen N y los carbohidratos no."),
      ("¿Con qué unidades pequeñas se forman las proteínas?", "Con aminoácidos", "Los aminoácidos se unen para formar proteínas."),
  ],
  app=[
      arith("Una cadena de ejemplo de almidón tiene 35 unidades de glucosa. ¿Cuántos átomos de carbono aportan?", "35*6", "Cada unidad aporta 6 carbonos.", " carbonos"),
      (TBIO + "Una molécula de ejemplo tiene C, H, O y N pero no P. ¿Qué biomolécula podría ser? A) Una proteína; B) Un lípido.", "A", "Tiene nitrógeno y no fósforo."),
      arith(TBIO + "¿Cuántos elementos más tienen los ácidos nucleicos que los carbohidratos?", "5-3", "Los ácidos nucleicos tienen 5 elementos y los carbohidratos 3."),
  ],
  rea=[
      (TBIO + "Un compañero dice: «Los lípidos solo sirven para reservar energía». ¿Qué le respondes? A) La tabla también les asigna ser componentes de membranas; B) Tiene razón.", "A", "La fila de lípidos menciona dos funciones."),
      ("¿Por qué una tabla sencilla tiene límites? A) Resume funciones y deja fuera otras; B) Siempre tiene errores.", "A", "Una tabla simplifica la información."),
  ],
  cha=[
      arith("Una cadena tiene 12 glucosas y otra tiene 30. ¿Cuántos carbonos más tiene la segunda?", "(30-12)*6", "Se calcula la diferencia de unidades y se multiplica por 6.", " carbonos"),
      (TBIO + "¿Qué conclusión es válida? A) Los carbohidratos tienen C, H y O y su función principal es la energía; B) Todos los lípidos tienen N.", "A", "La afirmación sobre carbohidratos es la que dice la tabla; la otra la contradice."),
  ],
  context=[("Un alimento de ejemplo es rico en almidón, formado por muchas unidades de glucosa. ¿Qué biomolécula es el almidón? A) Un carbohidrato; B) Un ácido nucleico.", "A", "El almidón es un carbohidrato hecho de glucosas.")],
  selfcheck=[("¿Qué elementos tienen en común todas las biomoléculas de la tabla?", "C, H y O", "Aparecen en las cuatro filas."), ("¿Qué elemento extra tienen las proteínas?", "Nitrógeno", "Se agrega N."), ("¿Por qué conviene decir «función principal»?", "Porque cada grupo cumple varias funciones", "La tabla simplifica.")],
  open_task=task("Con la tabla de ejemplo de esta clase, construye una tarjeta para cada biomolécula con sus elementos y su función principal. Luego escribe una oración que diga qué elementos distinguen a un ácido nucleico de un carbohidrato y un límite de la tabla.", "Ácido nucleico: C, H, O, N y P, información genética. Carbohidrato: C, H y O, energía. El ácido nucleico tiene además N y P. Límite: la tabla da solo una función principal.", ["cuatro tarjetas completas", "compara los elementos", "declara un límite"], ["cuatro tarjetas y dos oraciones"], ["inventar funciones que no están en la tabla", "olvidar el límite"], "Pregunta qué información agregarías a la tabla."),
  reinforce="Escribe una biomolécula, sus elementos y su función principal.",
  extend="Explica cómo se forma una molécula grande a partir de unidades pequeñas.")

L(OA17, 3,
  materials=MAT,
  use="Aprenderé a representar moléculas de carbono con un modelo de bolas y palitos, a distinguir enlaces simples, dobles y triples y a decir los límites de un modelo.",
  prior=["Sé que cada carbono suma cuatro enlaces.", "Sé leer una fórmula como C2H6."],
  explain=[
      "En un modelo de bolas y palitos, cada bola es un átomo y cada palito es un enlace. Un palito es un enlace simple, dos palitos juntos son un enlace doble y tres son un enlace triple. Con el modelo se puede comprobar que cada carbono tiene cuatro enlaces y contar cuántos hidrógenos caben en una molécula.",
      "El etano, CH3–CH3, tiene solo enlaces simples y fórmula C2H6. El eteno, CH2=CH2, tiene un enlace doble entre los carbonos y fórmula C2H4. El etino, CH≡CH, tiene un enlace triple y fórmula C2H2. Mientras más enlaces hay entre los carbonos, menos hidrógenos caben.",
      "Un buen modelo explica los datos. Si un modelo dice que el carbono forma solo dos enlaces, no explica por qué el metano tiene cuatro hidrógenos. Los modelos también tienen límites: los palitos no existen en la realidad y las moléculas reales no son planas como el dibujo.",
  ],
  vocab=[("enlace simple", "un par de electrones compartido, un palito"), ("enlace doble", "dos pares compartidos, dos palitos"), ("enlace triple", "tres pares compartidos, tres palitos"), ("fórmula semidesarrollada", "fórmula que muestra cómo se unen los carbonos"), ("modelo de bolas y palitos", "representación con bolas para átomos y palitos para enlaces")],
  worked=[
      ("Hidrógenos en un doble enlace", "En CH2=CH2, ¿cuántos hidrógenos tiene cada carbono y por qué?", ["Cada carbono tiene un doble enlace, que cuenta 2.", "Necesita 4 − 2 = 2 enlaces más, que son con 2 hidrógenos."], "2 hidrógenos por carbono; fórmula C2H4"),
      ("Contrastar modelos", "Modelo A: el carbono forma 2 enlaces. Modelo B: forma 4. Dato: el metano es CH4. ¿Qué modelo apoya el dato?", ["Con 2 enlaces, el carbono no podría unirse a 4 hidrógenos.", "Con 4 enlaces, sí puede."], "Modelo B"),
  ],
  mistakes=[
      ("Dibujar un carbono con tres palitos totales.", "Cada carbono debe sumar cuatro enlaces.", "Cuenta los palitos de cada carbono."),
      ("Creer que el modelo muestra la forma real exacta.", "Es una representación con límites.", "Anota al menos un límite del modelo."),
  ],
  rec=[
      ("¿Cuántos palitos representan un enlace doble?", "Dos", "Un enlace doble son dos pares compartidos."),
      ("Verdadero o falso: en el etino hay un enlace triple entre los carbonos.", "Verdadero", "Su fórmula semidesarrollada es CH≡CH."),
      ("¿Qué representa cada bola en un modelo de bolas y palitos?", "Un átomo", "Los palitos representan los enlaces."),
  ],
  und=[
      ("¿Cuál es la fórmula del etino, CH≡CH? A) C2H2; B) C2H6.", "A", "Cada carbono tiene un hidrógeno y un enlace triple."),
      ("En CH3–CH3, ¿qué tipo de enlace une los carbonos? A) Simple; B) Doble.", "A", "Hay un solo palito entre ellos."),
      ("¿Qué pasa con la cantidad de hidrógenos al pasar de enlace simple a doble entre dos carbonos?", "Disminuye", "El enlace extra ocupa lugares que serían de hidrógeno."),
  ],
  app=[
      arith("El propeno se escribe CH3–CH=CH2. ¿Cuántos hidrógenos tiene?", "3+1+2", "Los grupos CH3, CH y CH2 tienen 3, 1 y 2 hidrógenos.", " hidrógenos"),
      arith("El butino se escribe CH≡C–CH2–CH3. ¿Cuántos hidrógenos tiene?", "1+0+2+3", "El primer carbono tiene 1 H, el segundo ninguno y luego 2 y 3.", " hidrógenos"),
      ("En CH2=CH2, ¿cuántos enlaces suma cada carbono? A) Cuatro; B) Seis.", "A", "Un doble enlace cuenta 2 y los dos hidrógenos suman 2."),
  ],
  rea=[
      ("Un estudiante dibuja CH3–CH2 con un carbono con solo tres enlaces. ¿Qué error tiene? A) El segundo carbono suma tres enlaces y le falta uno; B) El primer carbono tiene demasiados hidrógenos.", "A", "Cada carbono debe sumar cuatro enlaces."),
      ("¿Por qué el modelo «el carbono forma dos enlaces» falla con el CH4? A) No explica los cuatro hidrógenos; B) El CH4 no existe.", "A", "Un modelo debe coincidir con la fórmula observada."),
  ],
  cha=[
      arith("En CH≡C–CH3, ¿cuántos hidrógenos tiene? Cuenta el CH y el CH3.", "1+0+3", "El carbono central del triple enlace no tiene H."),
      ("¿Qué límite tiene un dibujo plano de CH4? A) No muestra su forma en el espacio; B) Muestra todos los enlaces reales.", "A", "La molécula real es tridimensional."),
  ],
  context=[("Un estudiante de ejemplo dibuja CH2=CH2 como una cadena con enlace simple. ¿Qué debe corregir? A) El enlace entre carbonos es doble; B) Los hidrógenos son demasiados.", "A", "La fórmula C2H4 se logra con un enlace doble.")],
  selfcheck=[("¿Cuántos palitos tiene un enlace triple?", "Tres", "Cada palito es un par de electrones compartido."), ("¿Cuántos enlaces suma cada carbono?", "Cuatro", "Sin importar si son simples, dobles o triples."), ("Nombra un límite de un modelo de bolas y palitos.", "No muestra la forma real ni el movimiento", "Es una simplificación.")],
  open_task=task("Dibuja con bolas y palitos las moléculas etano, eteno y etino y escribe la fórmula de cada una (C2H6, C2H4, C2H2). Comprueba que cada carbono tenga cuatro enlaces y escribe un límite del modelo.", "Etano: CH3–CH3; eteno: CH2=CH2; etino: CH≡CH. Cada carbono suma 4. Límite: el dibujo es plano y la molécula no lo es.", ["tres dibujos correctos", "cada carbono suma cuatro", "declara un límite"], ["tres dibujos con fórmulas"], ["dejar carbonos con menos de cuatro enlaces", "olvidar el límite"], "Pregunta cuántos hidrógenos tendría una molécula con enlace doble entre dos carbonos y una cadena más larga."),
  reinforce="Dibuja el propeno CH3–CH=CH2 y cuenta los enlaces de cada carbono.",
  extend="Explica por qué los hidrógenos disminuyen al aumentar los enlaces entre los carbonos.")

TALC = "Tabla de ejemplo de alcanos (hidrocarburos con enlaces simples): metano, 1 carbono, gas a temperatura ambiente; etano, 2, gas; propano, 3, gas; butano, 4, gas; pentano, 5, líquido; hexano, 6, líquido; octano, 8, líquido. "

L(OA17, 4,
  materials=MAT,
  use="Aprenderé la relación entre el número de carbonos de un hidrocarburo, su cantidad de hidrógenos y su estado físico, y cómo se usa esa relación en el petróleo.",
  prior=["Sé que los hidrocarburos tienen solo C y H.", "Sé contar átomos en una fórmula."],
  explain=[
      "Los alcanos son hidrocarburos con solo enlaces simples. Si tienen n átomos de carbono en cadena, tienen 2n + 2 átomos de hidrógeno. El metano (n = 1) tiene 4 hidrógenos, el etano (n = 2) tiene 6 y el propano (n = 3) tiene 8. Esta relación permite escribir la fórmula de cualquier alcano de cadena abierta.",
      "El estado físico cambia con el tamaño de la molécula. A temperatura ambiente, los alcanos de 1 a 4 carbonos son gases y los de 5 a 8 carbonos que usamos como ejemplo son líquidos. En general, a mayor número de carbonos, mayor es el punto de ebullición, porque las moléculas más largas se atraen más.",
      "El petróleo es una mezcla de muchos hidrocarburos. En una refinería se separan por destilación, porque cada grupo hierve a una temperatura distinta. Los hidrocarburos más livianos, con pocos carbonos, hierven a menor temperatura y los más pesados, con muchos carbonos, hierven a mayor temperatura. Así se obtienen combustibles y otros derivados.",
  ],
  vocab=[("alcano", "hidrocarburo con solo enlaces simples"), ("punto de ebullición", "temperatura a la que un líquido hierve"), ("destilación", "separación de una mezcla por distintos puntos de ebullición"), ("derivado del petróleo", "producto que se obtiene del petróleo"), ("cadena abierta", "cadena de carbonos sin formar anillo")],
  worked=[
      ("Hidrógenos de un alcano", "¿Cuántos hidrógenos tiene un alcano de cadena abierta con 5 carbonos?", ["La relación es 2n + 2.", "Con n = 5: 2 × 5 + 2 = 12."], "12 hidrógenos; fórmula C5H12"),
      ("Relación con el estado", "Con la tabla de alcanos, ¿qué ocurre con el estado físico a medida que aumentan los carbonos?", ["Del 1 al 4 son gases.", "Desde el 5 son líquidos."], "A más carbonos, pasan de gases a líquidos"),
  ],
  mistakes=[
      ("Usar la relación 2n + 2 para moléculas con enlaces dobles.", "Esa relación es solo para alcanos, que tienen enlaces simples.", "Revisa que la cadena tenga solo enlaces simples."),
      ("Pensar que el petróleo es una sola sustancia.", "Es una mezcla de muchos hidrocarburos.", "Recuerda que se separa por destilación."),
  ],
  rec=[
      ("Verdadero o falso: un alcano tiene solo enlaces simples.", "Verdadero", "Esa es la definición de alcano."),
      (TALC + "¿En qué estado está el pentano a temperatura ambiente?", "Líquido", "Se lee en la tabla."),
      ("¿Cómo se llama la separación del petróleo según los puntos de ebullición?", "Destilación", "Cada grupo de hidrocarburos hierve a distinta temperatura."),
  ],
  und=[
      ("¿Cuántos hidrógenos tiene un alcano con 3 carbonos? A) 8; B) 6.", "A", "Con n = 3, 2 × 3 + 2 es 8."),
      (TALC + "¿Qué relación muestra la tabla entre el número de carbonos y el estado? A) A más carbonos se pasa de gas a líquido; B) El estado no depende del tamaño.", "A", "Hasta 4 carbonos son gases y desde 5 son líquidos."),
      ("¿Qué hidrocarburos hierven a menor temperatura en el petróleo? A) Los de pocos carbonos; B) Los de muchos carbonos.", "A", "Las moléculas pequeñas se separan con menos calor."),
  ],
  app=[
      arith("¿Cuántos hidrógenos tiene un alcano de cadena abierta con 7 carbonos?", "2*7+2", "Se usa 2n + 2 con n = 7.", " hidrógenos"),
      arith("Un alcano de cadena abierta tiene 22 hidrógenos. ¿Cuántos carbonos tiene?", "(22-2)//2", "Se despeja n en 2n + 2 = 22.", " carbonos"),
      (TALC + "Un alcano de ejemplo tiene 3 carbonos. ¿En qué estado está a temperatura ambiente? A) Gas; B) Líquido.", "A", "Los alcanos de 1 a 4 carbonos son gases."),
  ],
  rea=[
      ("Un compañero dice: «Un alcano de 10 carbonos tiene 20 hidrógenos». ¿Qué le respondes? A) Debe tener 22, porque es 2n + 2; B) Tiene razón.", "A", "2 × 10 + 2 es 22."),
      ("¿Por qué la destilación sirve para separar el petróleo? A) Porque cada hidrocarburo hierve a distinta temperatura; B) Porque todos hierven a la misma temperatura.", "A", "Las diferencias de ebullición permiten separarlos."),
  ],
  cha=[
      arith("Un alcano de cadena abierta tiene 26 hidrógenos. ¿Cuántos carbonos tiene?", "(26-2)//2", "Se despeja n en 2n + 2 = 26.", " carbonos"),
      (TALC + "Un compañero afirma que el hexano es gas porque tiene muchos hidrógenos. ¿Qué corriges? A) Según la tabla, el hexano es líquido; B) Es gas porque tiene 6 carbonos.", "A", "La tabla indica que el hexano es líquido."),
  ],
  context=[("Una refinería de ejemplo separa por destilación una mezcla en dos grupos: uno de moléculas de 4 carbonos y otro de 8 carbonos. ¿Cuál hierve a mayor temperatura? A) El de 8 carbonos; B) El de 4 carbonos.", "A", "Mayor número de carbonos implica mayor punto de ebullición.")],
  selfcheck=[("¿Cuántos hidrógenos tiene un alcano con n carbonos?", "2n + 2", "Es la relación de los alcanos de cadena abierta."), ("¿Qué pasa con el punto de ebullición al aumentar los carbonos?", "Aumenta", "Las moléculas largas se atraen más."), ("¿Por qué se destila el petróleo?", "Para separar hidrocarburos según su punto de ebullición", "Cada grupo hierve a otra temperatura.")],
  open_task=task("Completa una tabla de ejemplo con n = 1, 2, 3, 4, 5 y 6 carbonos: escribe 2n + 2 hidrógenos y la fórmula de cada alcano (por ejemplo, C2H6). Luego escribe una conclusión que relacione carbonos y estado físico usando la tabla de esta clase.", "n = 1: CH4; 2: C2H6; 3: C3H8; 4: C4H10; 5: C5H12; 6: C6H14. Hasta 4 carbonos son gases y desde 5 son líquidos.", ["seis fórmulas correctas", "usa 2n + 2", "relaciona carbonos y estado"], ["tabla de seis filas y una conclusión"], ["usar 2n en vez de 2n + 2", "olvidar que es solo para alcanos"], "Pregunta cuántos hidrógenos tendría una cadena de 10 carbonos."),
  reinforce="Escribe la fórmula de un alcano de 8 carbonos usando 2n + 2.",
  extend="Explica por qué el petróleo se separa por destilación y no por filtración.")

L(OA17, 5,
  materials=MAT,
  use="Aprenderé a explicar la combustión de hidrocarburos y la respiración de la glucosa con ecuaciones balanceadas, y a evaluar sus implicancias para el ambiente.",
  prior=["Sé contar átomos en fórmulas.", "Sé que los átomos se reordenan en una reacción."],
  explain=[
      "En una reacción química los átomos no se crean ni se destruyen: se reordenan. Por eso una ecuación está balanceada cuando hay la misma cantidad de cada átomo a ambos lados de la flecha. La combustión del metano es CH4 + 2 O2 → CO2 + 2 H2O: a la izquierda hay 1 C, 4 H y 4 O, y a la derecha también.",
      "En la combustión completa de un hidrocarburo, el carbono se une al oxígeno y forma dióxido de carbono, y el hidrógeno forma agua. La reacción libera energía. La respiración celular es una reacción parecida: C6H12O6 + 6 O2 → 6 CO2 + 6 H2O. Allí la glucosa libera energía para las células.",
      "Quemar combustibles fósiles libera CO2, un gas que aumenta el efecto invernadero. Si hay poco oxígeno, la combustión puede producir gases peligrosos como el monóxido de carbono. Por seguridad, los artefactos a gas se usan con ventilación y nunca se hacen experimentos con fuego en casa. Una evaluación debe considerar beneficios, riesgos y alternativas.",
  ],
  vocab=[("combustión", "reacción de una sustancia con oxígeno que libera energía"), ("ecuación balanceada", "ecuación con la misma cantidad de cada átomo a ambos lados"), ("respiración celular", "reacción en que la glucosa libera energía en las células"), ("combustible fósil", "combustible que viene del petróleo, el gas o el carbón"), ("efecto invernadero", "retención de calor en la atmósfera por ciertos gases")],
  worked=[
      ("Verificar una ecuación", "Verifica que CH4 + 2 O2 → CO2 + 2 H2O está balanceada.", ["Izquierda: 1 C, 4 H, 2 × 2 = 4 O.", "Derecha: 1 C, 2 × 2 = 4 H, 2 + 2 = 4 O."], "Está balanceada"),
      ("Respiración", "En C6H12O6 + 6 O2 → 6 CO2 + 6 H2O, ¿cuántos CO2 produce una glucosa?", ["El coeficiente de CO2 es 6.", "Cada glucosa produce 6 moléculas de CO2."], "6 moléculas de CO2"),
  ],
  mistakes=[
      ("Cambiar los subíndices para balancear.", "Cambiar C2H6 por C2H4 cambia la sustancia; se ajustan los coeficientes.", "Cambia solo los números delante de las fórmulas."),
      ("Decir que la combustión crea átomos nuevos de carbono.", "Los átomos se reordenan y se conservan.", "Cuenta los átomos antes y después."),
  ],
  rec=[
      ("¿Qué gas se produce al quemar completamente un hidrocarburo, además de agua?", "Dióxido de carbono", "El carbono se une al oxígeno."),
      ("Verdadero o falso: en una reacción química los átomos se conservan.", "Verdadero", "Solo se reordenan."),
      ("¿Qué gas del aire se consume en la combustión?", "Oxígeno", "Reacciona con el hidrocarburo."),
  ],
  und=[
      arith("En C3H8 + 5 O2 → 3 CO2 + 4 H2O, ¿cuántos átomos de oxígeno hay en los reactantes?", "5*2", "Cinco moléculas de O2 tienen dos átomos cada una.", " átomos"),
      arith("En C3H8 + 5 O2 → 3 CO2 + 4 H2O, ¿cuántos átomos de oxígeno hay en los productos?", "3*2+4*1", "Hay 3 CO2 con 2 O y 4 H2O con 1 O.", " átomos"),
      ("¿Qué hace la combustión con la energía? A) La libera; B) La absorbe.", "A", "La combustión es una reacción que libera energía."),
  ],
  app=[
      arith("En la respiración, una glucosa produce 6 CO2. Si se usan 4 glucosas de ejemplo, ¿cuántas moléculas de CO2 se producen?", "4*6", "Se multiplican las glucosas por 6.", " moléculas"),
      arith("En 2 C4H10 + 13 O2 → 8 CO2 + 10 H2O, ¿cuántos átomos de oxígeno hay en los reactantes?", "13*2", "Trece moléculas de O2 aportan 26 átomos.", " átomos"),
      ("¿Cuál es el producto gaseoso que más se relaciona con el efecto invernadero? A) El dióxido de carbono; B) El agua líquida.", "A", "El CO2 retiene calor en la atmósfera."),
  ],
  rea=[
      ("Un compañero dice: «En la combustión se crean átomos de carbono». ¿Qué le respondes? A) Los átomos se reordenan y se conservan; B) Tiene razón.", "A", "No se crean ni se destruyen átomos."),
      ("¿Por qué quemar combustibles fósiles aumenta el CO2 en la atmósfera? A) Porque el carbono del combustible sale como CO2; B) Porque el oxígeno se transforma en nitrógeno.", "A", "Cada carbono del combustible termina en una molécula de CO2."),
  ],
  cha=[
      arith("En 2 C2H6 + 7 O2 → 4 CO2 + 6 H2O, ¿cuántos átomos de hidrógeno hay en los reactantes?", "2*6", "Dos moléculas de C2H6 tienen 6 hidrógenos cada una.", " átomos"),
      ("¿Está balanceada C2H4 + 3 O2 → 2 CO2 + 2 H2O? A) Sí: hay 2 C, 4 H y 6 O a ambos lados; B) No: sobran carbonos.", "A", "Los conteos de C, H y O coinciden."),
  ],
  context=[("Una estufa a gas de ejemplo funciona en una pieza cerrada. ¿Por qué debe haber ventilación? A) La combustión consume oxígeno y, si falta, puede producir gases peligrosos; B) El gas se enfría con el aire.", "A", "La ventilación evita la falta de oxígeno y los gases peligrosos.")],
  selfcheck=[("¿Qué dos productos tiene la combustión completa de un hidrocarburo?", "Dióxido de carbono y agua", "El C forma CO2 y el H forma H2O."), ("¿Por qué una ecuación debe estar balanceada?", "Porque los átomos se conservan", "No se crean ni destruyen."), ("¿Qué reacción libera energía en las células?", "La respiración celular", "La glucosa reacciona con oxígeno.")],
  open_task=task("Con la combustión del propano de ejemplo, C3H8 + 5 O2 → 3 CO2 + 4 H2O, cuenta los átomos de C, H y O a cada lado y escribe si está balanceada. Luego escribe dos ventajas y dos riesgos de usar combustibles de hidrocarburos, y una medida de seguridad.", "Izquierda: 3 C, 8 H y 10 O; derecha: 3 C, 8 H y 6 + 4 = 10 O. Está balanceada. Ventajas: energía y transporte. Riesgos: CO2 y gases peligrosos sin ventilación. Medida: usar artefactos a gas con ventilación.", ["cuenta los átomos de ambos lados", "concluye que está balanceada", "nombra ventajas y riesgos", "incluye una medida de seguridad"], ["conteos y cuatro frases"], ["contar mal los oxígenos", "olvidar la seguridad"], "Pregunta qué alternativa de energía conoces."),
  reinforce="Cuenta los átomos de cada lado de CH4 + 2 O2 → CO2 + 2 H2O.",
  extend="Explica en qué se parecen la combustión y la respiración celular.")

# ---------------------------------------------------------------- OA 18

L(OA18, 1,
  materials=MAT,
  use="Aprenderé qué son los isómeros y la estereoquímica, y escribiré una pregunta investigable sobre isómeros de compuestos orgánicos como la glucosa.",
  prior=["Sé contar átomos en una fórmula.", "Sé que el carbono forma cuatro enlaces."],
  explain=[
      "Los isómeros son compuestos que tienen la misma fórmula molecular pero distinta estructura, es decir, sus átomos están ordenados de otra manera. Aunque tienen los mismos átomos, sus propiedades pueden ser distintas. Por ejemplo, el butano, CH3–CH2–CH2–CH3, y el metilpropano, CH3–CH(CH3)–CH3, tienen ambos la fórmula C4H10 y son isómeros.",
      "Otro ejemplo es el etanol, CH3–CH2–OH, y el éter dimetílico, CH3–O–CH3, con la misma fórmula C2H6O. La glucosa y la fructosa también son isómeros, con fórmula C6H12O6. La estereoquímica estudia cómo se ubican los átomos en el espacio, y es clave para entender las moléculas de los seres vivos.",
      "Una pregunta investigable sobre isómeros nombra qué se compara y qué se mide o se cuenta. «¿Tienen el mismo estado físico a temperatura ambiente el etanol y el éter dimetílico?» se puede contestar con datos. «¿Cuál molécula es más importante?» no se puede investigar. Los compuestos orgánicos no se prueban ni se huelen en un experimento.",
  ],
  vocab=[("isómeros", "compuestos con la misma fórmula molecular y distinta estructura"), ("fórmula molecular", "indica cuántos átomos de cada elemento tiene la molécula"), ("estructura", "forma en que se ordenan los átomos"), ("estereoquímica", "estudio de la disposición de los átomos en el espacio"), ("glucosa", "carbohidrato de fórmula C6H12O6")],
  worked=[
      ("Reconocer isómeros", "¿Son isómeros CH3–CH2–CH3 y CH2=CH–CH3?", ["Primero: C3 y 3+2+3 = 8 H, o sea C3H8.", "Segundo: C3 y 2+1+3 = 6 H, o sea C3H6.", "Las fórmulas moleculares son distintas."], "No son isómeros"),
      ("Mejorar una pregunta", "Mejora «¿Cuál isómero es mejor?» para poder investigarla.", ["Quito la palabra de opinión, «mejor».", "Elijo qué comparar: el estado físico a temperatura ambiente."], "«¿Tienen el mismo estado físico a temperatura ambiente el butano y el metilpropano?»"),
  ],
  mistakes=[
      ("Pensar que los isómeros tienen distinta fórmula molecular.", "Tienen la misma fórmula molecular y distinta estructura.", "Cuenta los átomos de cada elemento en ambas moléculas."),
      ("Creer que la misma fórmula implica las mismas propiedades.", "El orden de los átomos cambia las propiedades.", "Compara además la estructura."),
  ],
  rec=[
      ("¿Cómo se llama a los compuestos con la misma fórmula molecular y distinta estructura?", "Isómeros", "Esa es la definición de isómeros."),
      ("Verdadero o falso: la glucosa tiene la fórmula C6H12O6.", "Verdadero", "Es la fórmula de la glucosa."),
      ("¿Qué estudia la estereoquímica?", "La disposición de los átomos en el espacio", "Se ocupa de la forma tridimensional de las moléculas."),
  ],
  und=[
      ("El etanol, CH3–CH2–OH, y el éter dimetílico, CH3–O–CH3, tienen la fórmula C2H6O. ¿Qué son entre sí? A) Isómeros; B) La misma sustancia.", "A", "Tienen la misma fórmula pero distinto orden de átomos."),
      ("¿Qué tienen igual dos isómeros? A) La fórmula molecular; B) La estructura.", "A", "La estructura es lo que cambia."),
      ("¿Cuál pregunta es investigable? A) ¿Tienen el mismo estado físico a temperatura ambiente el etanol y el éter dimetílico?; B) ¿Cuál molécula es más importante?", "A", "La que compara el estado físico se contesta con datos; la otra no indica qué medir."),
  ],
  app=[
      arith("¿Cuántos hidrógenos tiene la cadena CH3–CH2–CH2–CH3?", "3+2+2+3", "Los grupos CH3, CH2, CH2 y CH3 aportan 3, 2, 2 y 3.", " hidrógenos"),
      arith("Un isómero del butano se escribe CH3–CH(CH3)–CH3. ¿Cuántos hidrógenos tiene?", "3+1+3+3", "Los grupos CH3, CH, CH3 y CH3 aportan 3, 1, 3 y 3.", " hidrógenos"),
      ("¿Son isómeros C3H8 y C3H6? A) No: sus fórmulas moleculares son distintas; B) Sí: ambos tienen tres carbonos.", "A", "Tienen distinta cantidad de hidrógenos."),
  ],
  rea=[
      ("Un compañero dice: «Si dos compuestos tienen la misma fórmula, son la misma sustancia». ¿Qué le respondes? A) Pueden ser isómeros con distinta estructura y propiedades; B) Tiene razón.", "A", "La fórmula igual no garantiza la misma estructura."),
      ("¿Por qué «¿Cuál isómero es más importante?» no sirve? A) Porque no dice qué medir o comparar; B) Porque todos los isómeros son la misma sustancia.", "A", "Una pregunta investigable necesita algo medible."),
  ],
  cha=[
      arith("El pentano es CH3–CH2–CH2–CH2–CH3. ¿Cuántos hidrógenos tiene?", "3+2+2+2+3", "Se suman los hidrógenos de cada grupo.", " hidrógenos"),
      ("La glucosa y la fructosa tienen la fórmula C6H12O6. ¿Qué se puede afirmar? A) Son isómeros: igual fórmula y distinta estructura; B) Son iguales.", "A", "Misma fórmula molecular, distinto orden de átomos."),
  ],
  context=[("Una etiqueta de ejemplo dice que un alimento contiene glucosa y fructosa, ambas C6H12O6. ¿Qué relación hay entre ellas? A) Son isómeros; B) Son la misma sustancia.", "A", "Tienen la misma fórmula y distinta estructura.")],
  selfcheck=[("¿Qué tienen igual y qué distinto dos isómeros?", "Igual fórmula molecular y distinta estructura", "Esa es la definición."), ("Nombra dos isómeros de fórmula C2H6O.", "Etanol y éter dimetílico", "Tienen distinto orden de átomos."), ("¿Qué debe tener una pregunta investigable?", "Algo que se compare y se pueda medir", "Permite reunir datos.")],
  open_task=task("Observa estas moléculas: A, CH3–CH2–CH2–CH3; B, CH3–CH(CH3)–CH3; C, CH3–CH2–CH3. Cuenta los átomos de C y H de cada una, indica cuáles son isómeros y por qué, y escribe una pregunta investigable que compare dos de ellas.", "A: C4H10; B: C4H10; C: C3H8. A y B son isómeros. Pregunta: ¿tienen el mismo estado físico a temperatura ambiente A y B?", ["cuenta bien los átomos", "identifica los isómeros con razón", "la pregunta compara y se puede medir"], ["tres fórmulas y una pregunta"], ["contar mal los hidrógenos", "escribir una pregunta de opinión"], "Pregunta qué propiedad compararías además del estado físico."),
  reinforce="Escribe la fórmula molecular de una molécula que sea isómero del etanol.",
  extend="Explica por qué dos isómeros pueden tener propiedades distintas.")

TPAR = "Tabla de ejemplo de pares de moléculas: par 1, CH3–CH2–CH2–CH3 y CH3–CH(CH3)–CH3, ambas C4H10; par 2, C3H8 y C3H6; par 3, etanol y éter dimetílico, ambos C2H6O, el etanol líquido y el éter dimetílico gas a temperatura ambiente; par 4, C2H6 y C2H4. "

L(OA18, 2,
  materials=MAT,
  use="Aprenderé a leer una tabla de pares de moléculas y a decidir con datos cuáles son isómeros y qué propiedades cambian entre ellos.",
  prior=["Sé qué son los isómeros.", "Sé contar átomos en una fórmula."],
  explain=[
      "Para decidir si dos moléculas son isómeros se comparan sus fórmulas moleculares. Si la cantidad de cada átomo es igual y la estructura es distinta, son isómeros. Si las fórmulas moleculares son distintas, no lo son, aunque se parezcan. Por eso el primer paso es contar los átomos de cada elemento.",
      "Los isómeros pueden tener propiedades distintas. En la tabla de esta clase, el etanol es líquido y el éter dimetílico es gas a temperatura ambiente, aunque ambos son C2H6O. En cambio, los isómeros del butano son parecidos entre sí porque su estructura difiere poco. Una tabla permite comparar propiedades de pares distintos.",
      "Al leer una tabla se separan los datos de las conclusiones. Un dato dice «el etanol es líquido». Una conclusión dice «el orden de los átomos puede cambiar el estado físico». La conclusión debe apoyarse en la fila de la tabla y declarar su límite: unos pocos pares no demuestran una regla general.",
  ],
  vocab=[("par", "dos moléculas que se comparan"), ("dato", "información observada o medida"), ("conclusión", "afirmación apoyada en los datos"), ("propiedad", "característica que se puede observar o medir"), ("estado físico", "sólido, líquido o gaseoso")],
  worked=[
      ("Decidir con la fórmula", "¿Son isómeros las moléculas del par 4 de la tabla, C2H6 y C2H4?", ["Las fórmulas moleculares son distintas: 6 H y 4 H.", "Los isómeros deben tener la misma fórmula."], "No son isómeros"),
      ("Conclusión con límite", "Escribe una conclusión sobre el par 3 con su límite.", ["Dato: ambos son C2H6O, uno es líquido y el otro gas.", "Conclusión: el orden de los átomos puede cambiar el estado físico.", "Límite: es un solo par."], "El orden de los átomos puede cambiar el estado físico; un solo par no prueba una regla general"),
  ],
  mistakes=[
      ("Decidir que son isómeros porque se parecen.", "Se necesita la misma fórmula molecular.", "Cuenta los átomos antes de decidir."),
      ("Generalizar una regla desde un solo par.", "Un par no demuestra una regla general.", "Escribe el límite de la conclusión."),
  ],
  rec=[
      (TPAR + "¿Qué par de la tabla tiene la fórmula C2H6O?", "El par 3", "Etanol y éter dimetílico."),
      (TPAR + "¿En qué estado está el etanol a temperatura ambiente?", "Líquido", "Se lee en la fila del par 3."),
      ("Verdadero o falso: dos moléculas con distinta fórmula molecular no son isómeros.", "Verdadero", "Los isómeros tienen igual fórmula molecular."),
  ],
  und=[
      (TPAR + "¿Qué pares de la tabla son isómeros? A) Los pares 1 y 3; B) Los pares 2 y 4.", "A", "Los pares 1 y 3 tienen igual fórmula en ambas moléculas."),
      (TPAR + "¿En qué se diferencian las moléculas del par 3? A) En la estructura y en el estado físico; B) En la fórmula molecular.", "A", "Tienen igual fórmula pero distinta estructura y estado."),
      (TPAR + "¿Qué dato tienen en común las moléculas del par 1?", "La fórmula C4H10", "Ambas se escriben C4H10."),
  ],
  app=[
      arith(TPAR + "En el par 2, ¿cuántos hidrógenos más tiene la molécula de C3H8 que la de C3H6?", "8-6", "Se restan las cantidades de hidrógeno de cada fórmula.", " hidrógenos"),
      arith(TPAR + "Si se suman los carbonos de las dos moléculas del par 1, ¿cuántos carbonos son?", "4+4", "Cada molécula tiene 4 carbonos.", " carbonos"),
      (TPAR + "Una molécula de ejemplo es CH3–O–CH3. ¿Con cuál del par 3 es isómero? A) Con el etanol; B) Con el C2H6.", "A", "Ambas son C2H6O con distinto orden de átomos."),
  ],
  rea=[
      (TPAR + "Un compañero dice: «Los isómeros siempre tienen el mismo estado físico». ¿Qué dato lo contradice? A) El par 3, con un líquido y un gas; B) El par 2.", "A", "En el par 3 el etanol y el éter dimetílico tienen distinto estado."),
      (TPAR + "Otro compañero dice: «Con estos datos ya sé que todos los isómeros cambian de estado». ¿Qué le respondes? A) Son pocos pares y no alcanzan para una regla general; B) Tiene razón.", "A", "Una conclusión debe declarar su límite."),
  ],
  cha=[
      arith(TPAR + "Un par nuevo de ejemplo une dos moléculas con 5 carbonos y 12 hidrógenos cada una. ¿Cuántos átomos de hidrógeno hay entre ambas?", "12*2", "Cada molécula tiene 12 H y son dos.", " hidrógenos"),
      (TPAR + "¿Qué dato adicional ayudaría a confirmar que el orden de los átomos cambia las propiedades? A) Más pares de isómeros con sus propiedades; B) Cambiar el color de la tabla.", "A", "Más pares darían más evidencia."),
  ],
  context=[("En una etiqueta de ejemplo aparece una molécula CH3–O–CH3. Una persona adulta dice que es lo mismo que el etanol. ¿Qué dato de la tabla lo contradice? A) Una es gas y la otra líquida a temperatura ambiente; B) Ambas tienen C2H6O.", "A", "Tienen propiedades distintas aunque compartan la fórmula.")],
  selfcheck=[("¿Qué se compara primero para decidir si son isómeros?", "La fórmula molecular", "Debe ser la misma."), ("¿Qué muestra el par 3 sobre las propiedades?", "Que el orden de los átomos puede cambiarlas", "Un isómero es líquido y el otro gas."), ("¿Por qué un par no basta para una regla general?", "Porque son muy pocos datos", "Se necesitan más casos.")],
  open_task=task("Con la tabla de pares de esta clase, escribe para cada par si son isómeros y por qué, y redacta una conclusión sobre el par 3 con su límite. Añade una tabla de dos columnas con la fórmula y el estado físico del etanol y del éter dimetílico.", "Par 1: isómeros (C4H10); par 2: no (C3H8 y C3H6); par 3: isómeros (C2H6O); par 4: no (C2H6 y C2H4). Etanol: C2H6O, líquido; éter dimetílico: C2H6O, gas. Límite: solo un par.", ["clasifica los cuatro pares", "da la razón", "escribe la conclusión con su límite"], ["clasificación, tabla y conclusión"], ["no justificar con la fórmula", "olvidar el límite"], "Pregunta qué otro par de isómeros te gustaría comparar."),
  reinforce="Cuenta los átomos de C y H de los pares 1 y 2 y decide cuáles son isómeros.",
  extend="Explica por qué el estado físico del etanol y del éter dimetílico es distinto.")

L(OA18, 3,
  materials=MAT,
  use="Aprenderé el modelo de carbono quiral y de enantiómeros, y cómo se aplica a la glucosa y a los seres vivos.",
  prior=["Sé qué son los isómeros.", "Sé que el carbono tiene cuatro enlaces."],
  explain=[
      "Un carbono quiral es un carbono unido a cuatro grupos distintos. Las moléculas con un carbono quiral pueden existir en dos formas que son imágenes especulares una de la otra y no se pueden superponer, como la mano derecha y la izquierda. Esas dos formas se llaman enantiómeros y son isómeros espaciales, estudiados por la estereoquímica.",
      "Por ejemplo, un carbono unido a H, F, Cl y Br es quiral porque tiene cuatro grupos distintos. En cambio, un carbono unido a dos H, un Cl y un Br no es quiral, porque tiene dos grupos iguales. En la glucosa de cadena abierta hay cuatro carbonos quirales. La forma que usan principalmente los seres vivos es la llamada D-glucosa.",
      "Los modelos explican por qué la forma importa: una molécula del organismo, como una enzima, reconoce solo cierta forma de otra molécula, como una llave que calza en una cerradura. Este modelo tiene límites: la realidad es más compleja que una llave y una cerradura. Por eso la forma de una molécula puede ser la diferencia entre ser útil o no serlo.",
  ],
  vocab=[("carbono quiral", "carbono unido a cuatro grupos distintos"), ("enantiómeros", "pareja de imágenes especulares no superponibles"), ("imagen especular", "reflejo, como el de un espejo"), ("D-glucosa", "forma de la glucosa que usan principalmente los seres vivos"), ("enzima", "proteína que acelera reacciones en los seres vivos")],
  worked=[
      ("Reconocer un carbono quiral", "Un carbono está unido a H, CH3, OH y COOH. ¿Es quiral?", ["Los cuatro grupos son distintos entre sí.", "Cuatro grupos distintos hacen quiral al carbono."], "Sí, es quiral"),
      ("Descartar", "Un carbono está unido a H, H, CH3 y OH. ¿Es quiral?", ["Hay dos grupos iguales: dos H.", "Para ser quiral deberían ser distintos los cuatro."], "No es quiral"),
  ],
  mistakes=[
      ("Llamar quiral a cualquier carbono con cuatro enlaces.", "Se necesitan cuatro grupos distintos.", "Compara los cuatro grupos uno a uno."),
      ("Creer que dos enantiómeros son la misma molécula.", "No se pueden superponer, como las manos.", "Piensa en imágenes en espejo."),
  ],
  rec=[
      ("Verdadero o falso: un carbono quiral está unido a cuatro grupos distintos.", "Verdadero", "Esa es la definición."),
      ("¿Cómo se llama la pareja de imágenes especulares no superponibles?", "Enantiómeros", "Son como la mano derecha y la izquierda."),
      ("¿Qué forma de la glucosa usan principalmente los seres vivos?", "La D-glucosa", "Las enzimas reconocen esa forma."),
  ],
  und=[
      ("Un carbono está unido a H, F, Cl y Br. ¿Es quiral? A) Sí; B) No.", "A", "Tiene cuatro grupos distintos."),
      ("Un carbono está unido a H, H, Cl y Br. ¿Es quiral? A) No; B) Sí.", "A", "Tiene dos hidrógenos iguales."),
      ("¿Con qué objeto se compara la relación entre dos enantiómeros? A) Con la mano derecha y la izquierda; B) Con dos monedas iguales.", "A", "Son imágenes en espejo que no se superponen."),
  ],
  app=[
      ("Un carbono está unido a H, OH, CH3 y COOH. ¿Qué se espera de la molécula? A) Que tenga dos enantiómeros; B) Que no tenga isómeros espaciales.", "A", "Un carbono quiral produce dos formas especulares."),
      ("En CH3–CH2–OH, el segundo carbono está unido a H, H, CH3 y OH. ¿Es quiral? A) No; B) Sí.", "A", "Tiene dos H, que son iguales."),
      ("¿Cuántos grupos distintos debe tener un carbono para ser quiral?", "Cuatro", "Un carbono quiral está unido a cuatro grupos distintos entre sí."),
  ],
  rea=[
      ("Un compañero dice: «Como L-glucosa y D-glucosa tienen la misma fórmula, el cuerpo las usa igual». ¿Qué le respondes? A) La forma importa: las enzimas reconocen principalmente la D-glucosa; B) Tiene razón.", "A", "La forma espacial determina si la molécula encaja."),
      ("¿Qué límite tiene el modelo de llave y cerradura? A) Simplifica la realidad, que es más compleja; B) Explica todo exactamente.", "A", "Un modelo es una simplificación."),
  ],
  cha=[
      ("Una molécula de ejemplo tiene un carbono unido a F, F, H y Cl. ¿Es quiral? A) No: dos grupos son iguales; B) Sí: tiene cuatro enlaces.", "A", "Tiene dos flúor iguales."),
      ("Dos enantiómeros de un fármaco de ejemplo: uno actúa y el otro no. ¿Qué modelo lo explica? A) La forma espacial encaja o no con la molécula del cuerpo; B) El color de las moléculas.", "A", "La forma determina el reconocimiento."),
  ],
  context=[("Una molécula de ejemplo tiene un carbono con cuatro grupos distintos. Un estudiante dice que existe en dos formas. ¿Qué nombre reciben esas dos formas especulares? A) Enantiómeros; B) Hidrocarburos.", "A", "Son imágenes en espejo no superponibles.")],
  selfcheck=[("¿Qué es un carbono quiral?", "Un carbono unido a cuatro grupos distintos", "Por eso la molécula tiene dos formas."), ("¿Qué son los enantiómeros?", "Imágenes especulares no superponibles", "Como las manos."), ("¿Qué límite tiene el modelo de llave y cerradura?", "Simplifica la realidad", "Es una analogía.")],
  open_task=task("Analiza estos tres carbonos: (1) unido a H, F, Cl y Br; (2) unido a H, H, Cl y Br; (3) unido a H, OH, CH3 y COOH. Indica cuáles son quirales y por qué, y dibuja en palitos la imagen especular del caso 1. Añade un límite del modelo de llave y cerradura.", "Quirales: 1 y 3, porque tienen cuatro grupos distintos; el 2 no, porque tiene dos H. Límite: la analogía simplifica cómo se reconocen las moléculas.", ["clasifica los tres con razón", "dibuja la imagen especular", "declara un límite"], ["clasificación y un dibujo"], ["llamar quiral al caso 2", "olvidar el límite"], "Pregunta qué relación hay entre los enantiómeros y las manos."),
  reinforce="Escribe un ejemplo de carbono quiral y otro que no lo sea, con sus grupos.",
  extend="Explica por qué los seres vivos usan principalmente la D-glucosa.")

L(OA18, 4,
  materials=MAT,
  use="Aprenderé a relacionar el número de carbonos quirales con el número de estereoisómeros, y la estructura de la glucosa con su utilidad para los seres vivos.",
  prior=["Sé reconocer un carbono quiral.", "Sé que los isómeros tienen igual fórmula y distinta estructura."],
  explain=[
      "Cuando una molécula tiene n carbonos quirales, puede tener hasta 2 elevado a n estereoisómeros. Con 1 carbono quiral hay 2, con 2 hay 4 y con 3 hay 8. En el modelo, cada carbono quiral duplica el número de formas posibles. Esta relación es una cuenta máxima: algunas moléculas con simetría tienen menos.",
      "La glucosa de cadena abierta tiene 4 carbonos quirales, así que puede tener hasta 16 estereoisómeros. Aun así, los seres vivos usan principalmente una forma, la D-glucosa. La glucosa y la fructosa tienen la misma fórmula, C6H12O6, pero estructuras distintas: son isómeros. La glucosa es un sólido blanco que se disuelve bien en agua, lo que facilita su transporte por la sangre, y es una fuente de energía para las células. La fructosa está presente en muchas frutas.",
      "Para investigar una relación entre variables hay que decir cuál se cambia y cuál se cuenta. Aquí, la variable que cambia es el número de carbonos quirales y la que se cuenta es el número de estereoisómeros. Una conclusión indica el rango de los datos y el límite del modelo. Por ejemplo, la regla 2 elevado a n sirve como máximo, no como valor exacto.",
  ],
  vocab=[("estereoisómero", "isómero que difiere en la disposición espacial de los átomos"), ("máximo", "valor más alto posible"), ("fructosa", "isómero de la glucosa presente en muchas frutas"), ("fuente de energía", "sustancia de la que el organismo obtiene energía"), ("simetría", "repetición de una forma que reduce el número de isómeros")],
  worked=[
      ("Contar estereoisómeros", "Una molécula de ejemplo tiene 3 carbonos quirales. ¿Cuántos estereoisómeros puede tener como máximo?", ["Cada carbono quiral duplica el número.", "2 × 2 × 2 = 8."], "8 estereoisómeros como máximo"),
      ("Glucosa y fructosa", "¿Qué relación hay entre la glucosa y la fructosa?", ["Ambas son C6H12O6.", "Su estructura es distinta."], "Son isómeros"),
  ],
  mistakes=[
      ("Pensar que 2 elevado a n es siempre el número exacto.", "Es un máximo; la simetría puede reducirlo.", "Escribe «hasta» antes del número."),
      ("Decir que glucosa y fructosa son la misma sustancia.", "Tienen la misma fórmula y distinta estructura.", "Compara la estructura, no solo la fórmula."),
  ],
  rec=[
      ("¿Cuántos estereoisómeros puede tener como máximo una molécula con 1 carbono quiral?", "2", "Cada carbono quiral duplica el número."),
      ("Verdadero o falso: glucosa y fructosa son isómeros.", "Verdadero", "Ambas son C6H12O6 con distinta estructura."),
      ("¿Para qué sirve la glucosa a las células?", "Como fuente de energía", "Se usa en la respiración celular."),
  ],
  und=[
      ("¿Cuántos carbonos quirales tiene la glucosa de cadena abierta? A) Cuatro; B) Seis.", "A", "El modelo de esta clase indica cuatro."),
      ("¿Qué relación hay entre carbonos quirales y estereoisómeros? A) Cada carbono quiral duplica el número posible; B) No hay relación.", "A", "El máximo es 2 elevado a n."),
      ("¿Por qué es un máximo el número 2 elevado a n? A) Porque la simetría puede reducirlo; B) Porque siempre es exacto.", "A", "Algunas moléculas con simetría tienen menos."),
  ],
  app=[
      arith("Una molécula de ejemplo tiene 5 carbonos quirales. ¿Cuántos estereoisómeros puede tener como máximo?", "2*2*2*2*2", "Se multiplica 2 cinco veces.", " estereoisómeros"),
      arith("Una molécula de ejemplo tiene 2 carbonos quirales. ¿Cuántos estereoisómeros puede tener como máximo?", "2*2", "Se multiplica 2 dos veces.", " estereoisómeros"),
      ("Una molécula tiene como máximo 8 estereoisómeros. ¿Cuántos carbonos quirales tiene? A) Tres; B) Cuatro.", "A", "2 × 2 × 2 es 8."),
  ],
  rea=[
      ("Un compañero dice: «La glucosa tiene 16 estereoisómeros, así que el cuerpo usa los 16 por igual». ¿Qué le respondes? A) Los seres vivos usan principalmente una forma, la D-glucosa; B) Tiene razón.", "A", "Que existan formas posibles no significa que se usen todas."),
      ("¿Por qué la glucosa y la fructosa pueden ser distintas aunque tengan la misma fórmula? A) Porque sus átomos están ordenados de otro modo; B) Porque tienen distinto número de carbonos.", "A", "Son isómeros con distinta estructura."),
  ],
  cha=[
      arith("Si la glucosa tiene 4 carbonos quirales, ¿cuántos estereoisómeros puede tener como máximo?", "2*2*2*2", "Se multiplica 2 cuatro veces.", " estereoisómeros"),
      ("Una conclusión dice: «Todas las moléculas con 3 carbonos quirales tienen exactamente 8 estereoisómeros». ¿Qué corriges? A) Es un máximo; algunas con simetría tienen menos; B) Son siempre 3.", "A", "Hay que escribir «hasta 8»."),
  ],
  context=[("Una etiqueta de ejemplo muestra una fruta con fructosa y otro alimento con glucosa. ¿Qué afirmación es correcta? A) Son isómeros con la misma fórmula; B) Son sustancias con fórmulas distintas.", "A", "Ambas son C6H12O6.")],
  selfcheck=[("¿Cuál es el máximo de estereoisómeros con n carbonos quirales?", "2 elevado a n", "Cada carbono quiral lo duplica."), ("¿Qué relación hay entre glucosa y fructosa?", "Son isómeros", "Igual fórmula y distinta estructura."), ("¿Por qué ese número es un máximo?", "Porque la simetría puede reducirlo", "Algunas formas se repiten.")],
  open_task=task("Completa una tabla con 1, 2, 3, 4 y 5 carbonos quirales y escribe el máximo de estereoisómeros. Luego escribe una conclusión que mencione la relación, el rango de datos, un límite y la utilidad de la glucosa para los seres vivos.", "1 → 2; 2 → 4; 3 → 8; 4 → 16; 5 → 32. Cada carbono quiral duplica el máximo; el rango va de 1 a 5; es un máximo porque la simetría puede reducirlo. La glucosa es una fuente de energía para las células.", ["cinco valores correctos", "enuncia la relación", "declara un límite", "menciona la utilidad de la glucosa"], ["tabla y un párrafo breve"], ["tomar el máximo como exacto", "olvidar la utilidad"], "Pregunta por qué los seres vivos usan principalmente una sola forma."),
  reinforce="Calcula el máximo de estereoisómeros para 3 carbonos quirales.",
  extend="Explica por qué la forma espacial de una molécula importa para los seres vivos.")
