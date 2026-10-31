"""Cuaderno del estudiante, 6.º básico Lenguaje y Comunicación: OA 29 (exposiciones orales claras y efectivas)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA29 = "LE06 OA 29"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, ctx, sc, open_args, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=ctx, selfcheck=sc, open_task=task(*open_args), reinforce=reinforce, extend=extend,
    )


AJEDREZ = ("Exposición sobre el ajedrez. [1] Hoy les hablaré del ajedrez, un juego de estrategia que practico desde hace dos años. "
           "[2] En primer lugar, cada jugador empieza con 16 piezas. [3] En segundo lugar, el objetivo es dar jaque mate al rey del rival. "
           "[4] Además, el ajedrez ayuda a concentrarse. [5] En resumen, el ajedrez es un juego que enseña a pensar antes de actuar. Gracias por escuchar.")

# ================================================================ OA 29 · clase 1
reg(
    OA29, 1,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu práctica.",
    "Aprenderé a organizar una exposición oral en introducción, desarrollo y cierre, con ideas coherentes entre sí. Sirve para que quien escucha entienda de qué hablas y recuerde lo importante.",
    ["Sé que un texto tiene inicio, medio y final.", "Sé contar un tema con mis propias palabras."],
    [
        "Una exposición oral es un discurso planificado en que presentas un tema de tu interés a una audiencia. Para que se entienda, se organiza en tres partes. La introducción saluda, presenta el tema y dice por qué es interesante o qué vas a explicar. El desarrollo explica las ideas principales, una después de otra. El cierre resume lo más importante y termina con una idea final o un agradecimiento.",
        "Las ideas deben ser coherentes: todas se relacionan con el tema y siguen un orden lógico. Si hablas del ajedrez, la idea sobre cómo se cocinan las lentejas no es coherente, aunque sea cierta. Cada idea del desarrollo debe aportar algo al tema. Una forma de comprobarlo es preguntarse: ¿esta frase ayuda a explicar el tema central?",
        "Para que el público se oriente, anuncia lo que harás en la introducción («hoy les explicaré tres cosas») y recuerda lo dicho en el cierre («en resumen…»). Así se logra la coherencia entre las partes. Una buena exposición se parece a un mapa: quien escucha siempre sabe dónde está.",
    ],
    [("exposición oral", "discurso planificado para explicar un tema a una audiencia"), ("introducción", "parte inicial que presenta el tema"), ("desarrollo", "parte central con las ideas principales"), ("cierre", "parte final con el resumen y una idea final"), ("coherente", "ordenado y relacionado con el tema")],
    [
        ("Ubicar una frase", "En una exposición sobre el reciclaje, la frase «Hoy les explicaré por qué conviene reciclar papel» ¿pertenece a la introducción, al desarrollo o al cierre?", ["La frase presenta el tema.", "Anuncia lo que se explicará.", "Eso es propio de la introducción."], "Introducción."),
        ("Quitar lo incoherente", "En una exposición sobre el reciclaje se dice: «El papel puede reutilizarse», «Hay que separar los residuos en casa» y «Mi perro duerme en el sofá». ¿Cuál frase no es coherente con el tema?", ["Reviso cada frase frente al tema.", "Las dos primeras hablan del reciclaje.", "La tercera habla de otro asunto."], "«Mi perro duerme en el sofá»."),
    ],
    [("Empezar la exposición sin presentar el tema.", "Se piensa que el público ya sabe de qué hablas.", "Anuncia el tema en la introducción."), ("Terminar con «eso nomás» sin resumen.", "Se cree que el cierre no es importante.", "Resume las ideas y agradece.")],
    [
        E(f"{AJEDREZ} ¿Qué número tiene la frase de la introducción?", "1", "Presenta el tema y saluda."),
        E(f"{AJEDREZ} ¿Cuál frase es el cierre: la 4 o la 5?", "5", "Resume y termina con agradecimiento."),
        E("En una exposición, ¿en qué parte se explican las ideas principales: introducción, desarrollo o cierre?", "Desarrollo", "Es la parte central."),
    ],
    [
        E(f"{AJEDREZ} ¿Cuántas ideas hay en el desarrollo (frases 2, 3 y 4)?", "3", "Son las frases 2, 3 y 4."),
        E("Una exposición sobre el cuidado de una planta incluye estas frases: a) «Hay que regarla con poca agua.» b) «Ayer fui al cine.» c) «Necesita luz.» ¿Cuál no es coherente?", "b", "Habla de otro tema."),
        E("Quien expone dice «hoy explicaré tres cosas sobre la lectura». ¿Qué ayuda a la audiencia con esa frase: a) saber qué vendrá b) olvidar el tema?", "a", "Anuncia la estructura."),
    ],
    [
        E("Ordena las partes de una exposición: a) cierre b) introducción c) desarrollo. Escribe las letras.", "b, c, a", "Se parte por la introducción y se termina con el cierre."),
        E("Para exponer sobre «cómo cuidar los libros», ordena las ideas del desarrollo: a) Por último, guárdalos en un lugar seco. b) Primero, lávate las manos antes de leer. c) Luego, evita doblar las hojas. Escribe las letras.", "b, c, a", "Siguen el orden indicado por «primero», «luego» y «por último»."),
        E(f"{AJEDREZ} ¿Cuál conector ordena las ideas del desarrollo: «en primer lugar» o «gracias por escuchar»?", "En primer lugar", "Marca el orden de la primera idea."),
    ],
    [
        E("Un estudiante dice: «No necesito cierre, pues ya expliqué todo en el desarrollo». ¿Es correcto? Responde sí o no.", "No", "El cierre resume y deja una idea final."),
        arith("Una exposición dura 6 minutos: la introducción 1, el desarrollo 4 y el cierre. ¿Cuántos minutos quedan para el cierre?", "6-1-4", "Se restan introducción y desarrollo del total."),
    ],
    [
        E("Una exposición sobre «el cuidado del patio» tiene cuatro ideas, pero una habla de las vacaciones. Si la audiencia es el curso, ¿qué haces con esa idea: quitarla o ponerla en el cierre?", "Quitarla", "No es coherente con el tema."),
        E(f"{AJEDREZ} ¿Cuál es la idea principal que se recuerda en el cierre: que el ajedrez enseña a pensar antes de actuar o que tiene 16 piezas?", "Que enseña a pensar antes de actuar", "El cierre resume la idea central."),
    ],
    [E("Tu curso hará exposiciones sobre pasatiempos. Un compañero comienza: «Eh… bueno… yo les iba a contar de algo». ¿Qué mejora su introducción: a) «Hoy les hablaré de mi pasatiempo: dibujar historietas.» b) Quedarse en silencio?", "a", "Presenta el tema con claridad.")],
    [
        E("¿Cómo se llama la parte final de una exposición?", "Cierre", "Resume y termina."),
        E("¿La introducción presenta el tema? Responde sí o no.", "Sí", "Orienta a la audiencia."),
        E("¿Todas las ideas del desarrollo deben relacionarse con el tema? Responde sí o no.", "Sí", "Eso las hace coherentes."),
    ],
    ("Elige uno de estos temas: «cómo cuidar una planta», «mi juego favorito» o «un animal doméstico». Escribe una exposición breve con tres partes: una introducción de 2 oraciones, un desarrollo con 3 ideas (usa «en primer lugar», «además» y «por último») y un cierre de 2 oraciones. Ensáyala en voz alta y verifica que ninguna idea se salga del tema.",
     "Introducción: «Hoy les hablaré de mi planta, una menta. Les contaré tres cuidados». Desarrollo: «En primer lugar, riégala poco. Además, necesita luz. Por último, quita las hojas secas». Cierre: «En resumen, la menta necesita agua, luz y atención. Gracias».",
     ["tiene introducción, desarrollo y cierre", "las ideas son coherentes con el tema", "usa conectores para ordenar"], ["texto de tres partes escrito o dicho"], ["ideas fuera del tema", "no tener cierre"],
     "Si una idea se sale del tema, bórrala o cámbiala por otra relacionada."),
    "Escribe la introducción y el cierre de una exposición sobre tu comida favorita.",
    "Escucha una exposición o un noticiero y anota qué parte es introducción, cuál desarrollo y cuál cierre.",
)

# ================================================================ OA 29 · clase 2
reg(
    OA29, 2,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar tu práctica.",
    "Aprenderé a fundamentar lo que digo con ejemplos y datos, y a usar elementos de cohesión (conectores) para unir las partes de la exposición. Sirve para que mis ideas se entiendan y se crean.",
    ["Sé organizar una exposición en introducción, desarrollo y cierre.", "Sé dar una razón con «porque»."],
    [
        "Fundamentar es apoyar cada afirmación con ejemplos y datos. Un ejemplo muestra un caso concreto: «Muchas plantas, como la menta, crecen bien en una maceta». Un dato es información comprobable, a menudo con cifras: «De 30 estudiantes, 18 prefieren el recreo largo». Sin ejemplos ni datos, las afirmaciones quedan como opiniones sueltas.",
        "La cohesión es la unión entre las ideas. Se logra con conectores: «en primer lugar», «además» y «por otra parte» para sumar; «por ejemplo» para ilustrar; «porque» y «por eso» para explicar causas y consecuencias; «sin embargo» para contrastar; «finalmente» y «en conclusión» para cerrar. Los conectores guían a quien escucha de una idea a la siguiente.",
        "Evita dos errores: abusar de un solo conector («y… y… y…») o usarlo mal. «Por eso» lleva a una consecuencia: «Llovió mucho; por eso suspendieron el partido». «Porque» da la causa: «Suspendieron el partido porque llovió». Cuando los uses con cuidado, tu exposición sonará ordenada.",
    ],
    [("ejemplo", "caso concreto que ilustra una idea"), ("dato", "información comprobable, a menudo con cifras"), ("cohesión", "unión entre las ideas de un texto"), ("conector", "palabra que une ideas"), ("consecuencia", "resultado de algo que ocurrió antes")],
    [
        ("Elegir el conector", "Completa: «Llovió toda la mañana; ______ suspendieron el partido». Opciones: porque / por eso.", ["Veo que la segunda parte es el resultado.", "El conector que introduce una consecuencia es «por eso».", "Reviso que se lea bien."], "Por eso."),
        ("Distinguir ejemplo y dato", "«Por ejemplo, la menta crece bien en maceta» y «De 30 estudiantes, 18 prefieren el recreo largo». ¿Cuál es un ejemplo y cuál un dato con cifras?", ["El primero muestra un caso concreto.", "El segundo usa cifras comprobables.", "Los clasifico."], "La primera es ejemplo; la segunda es dato."),
    ],
    [("Usar «y… y… y…» en toda la exposición.", "Se piensa que un conector basta.", "Varía los conectores según lo que quieres expresar."), ("Afirmar sin ejemplo ni dato.", "Se cree que la opinión es suficiente.", "Agrega un caso concreto o una cifra.")],
    [
        E("¿Qué conector introduce un ejemplo: «por ejemplo» o «sin embargo»?", "Por ejemplo", "Presenta un caso que ilustra la idea."),
        E("«En el curso hay 28 estudiantes y 20 usan bicicleta.» ¿Es un ejemplo o un dato con cifras?", "Un dato con cifras", "Da cantidades comprobables."),
        E("¿Qué conector sirve para contrastar: sin embargo o además?", "Sin embargo", "Marca una oposición."),
    ],
    [
        E("Completa: «Faltó el profesor; ______ la clase se suspendió». Opciones: porque / por eso.", "por eso", "La clase suspendida es la consecuencia."),
        E("Completa: «La clase se suspendió ______ faltó el profesor». Opciones: porque / por eso.", "porque", "Introduce la causa."),
        E("¿Cuál es un ejemplo: a) «Por ejemplo, un cuaderno de cien hojas dura un mes.» b) «Hay muchos cuadernos.»", "a", "Presenta un caso concreto."),
    ],
    [
        E("Dato: 17 de 25 estudiantes prefieren el recreo largo. Elige la frase mejor fundamentada: a) «Más de la mitad del curso prefiere el recreo largo: 17 de 25 estudiantes.» b) «Todos quieren recreo largo.»", "a", "Usa datos que se pueden comprobar."),
        arith("En una encuesta del curso, 17 de 25 prefieren el recreo largo. ¿Cuántos NO lo prefieren?", "25-17", "Se restan los que sí lo prefieren del total."),
        E("Ordena con conectores: a) Finalmente, el recreo largo mejora el ánimo. b) En primer lugar, permite jugar más tiempo. c) Además, ayuda a descansar. Escribe las letras.", "b, c, a", "Siguen la secuencia de primer lugar, además y finalmente."),
    ],
    [
        E("Un estudiante dice: «Más conectores siempre es mejor». ¿Es correcto? Responde sí o no.", "No", "Importa usarlos bien, no abusar."),
        E("Un orador dice: «Hablaré del agua y es importante y se debe cuidar y hay que ahorrar y…». ¿Qué problema tiene su uso de conectores: repite siempre «y» o usa demasiados datos?", "Repite siempre «y»", "No varía los conectores ni marca relaciones entre las ideas."),
    ],
    [
        E("Tema: usar bicicleta. Datos: 20 de 28 estudiantes llegan en bicicleta. ¿Qué afirmación está bien fundamentada: a) «La mayoría del curso llega en bicicleta: 20 de 28.» b) «Casi nadie usa bicicleta.»", "a", "20 de 28 es más de la mitad."),
        arith("En el curso hay 28 estudiantes y 20 llegan en bicicleta. ¿Cuántos llegan de otra forma?", "28-20", "Se resta del total a quienes llegan en bicicleta."),
    ],
    [E("Quieres convencer a tu curso de leer 15 minutos diarios. ¿Cuál frase usa un ejemplo y un conector: a) «Por ejemplo, con 15 minutos diarios, en una semana se leen 105 minutos.» b) «Lean todos.»", "a", "Tiene un conector y un ejemplo concreto.")],
    [
        E("Una información comprobable, a menudo con cifras, ¿se llama dato o conector?", "Dato", "Se puede verificar y apoya lo que afirmas."),
        E("¿«Finalmente» sirve para cerrar una idea? Responde sí o no.", "Sí", "Marca el último punto."),
        E("¿Un ejemplo muestra un caso concreto? Responde sí o no.", "Sí", "Ilustra la idea con algo real."),
    ],
    ("Lee este dato: «De los 24 estudiantes de sexto, 15 ya usan la biblioteca escolar cada semana». Escribe un párrafo de cuatro oraciones para convencer al curso de que más personas usen la biblioteca. Usa al menos tres conectores distintos (por ejemplo, además, por eso, finalmente), incluye el dato y un ejemplo propio.",
     "Más de la mitad del curso usa la biblioteca: 15 de 24. Por ejemplo, ahí encontré un libro de aventuras. Además, el préstamo es gratis. Por eso conviene usarla más.",
     ["usa tres conectores distintos", "incluye el dato del enunciado", "incluye un ejemplo propio"], ["párrafo de cuatro oraciones"], ["repetir siempre «y»", "no usar el dato"],
     "Subraya tus conectores; si repites uno, cámbialo."),
    "Escribe dos oraciones sobre el reciclaje: una con «porque» y otra con «por eso».",
    "Fíjate qué conectores se usan en un noticiero y anota tres.",
)

# ================================================================ OA 29 · clase 3
reg(
    OA29, 3,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escuchar frases en voz alta.",
    "Aprenderé a usar un vocabulario variado y preciso, un registro formal adecuado a una exposición y construcciones de oraciones más variadas. Sirve para sonar claro, respetuoso y no repetir siempre las mismas frases.",
    ["Sé organizar una exposición.", "Sé usar conectores."],
    [
        "El vocabulario preciso es el uso de la palabra exacta para lo que quieres decir. Decir «el cosito de la máquina» no explica nada; decir «la palanca de la máquina» sí. Un vocabulario variado evita repetir la misma palabra: en lugar de «cosa», «bueno» o «hacer» en cada frase, puedes usar «elemento», «beneficioso», «construir». Para eso ayuda un diccionario de sinónimos.",
        "Una exposición suele pedir un registro formal. Eso significa usar «usted» o «ustedes» con la audiencia, no usar modismos o palabras de uso muy familiar («chiquillos», «ya po», «onda») y completar las frases: «los niños» en vez de «los chiquillos»; «para» en vez de «pa'». Un registro formal no es difícil ni distante: es claro y cuidado.",
        "También podemos variar la forma de construir las oraciones. En lugar de comenzar siempre con «Yo creo que…», puedes cambiar el orden: «Los estudiantes aprenden mejor cuando descansan» puede decirse «Cuando descansan, los estudiantes aprenden mejor». O usar otra estructura: «Es importante descansar, porque…». Variar hace que la exposición suene más natural y rica.",
    ],
    [("vocabulario preciso", "palabra exacta para lo que se quiere decir"), ("sinónimo", "palabra con significado parecido"), ("registro formal", "forma de hablar cuidada y respetuosa"), ("modismo", "expresión muy familiar o propia de un grupo"), ("construcción", "manera de armar una oración")],
    [
        ("Reemplazar una palabra vaga", "Mejora «La máquina tiene una cosa que sube y baja» con una palabra precisa (la cosa es una palanca).", ["Identifico la palabra vaga: cosa.", "La reemplazo por «palanca».", "Releo para ver que se entienda."], "«La máquina tiene una palanca que sube y baja»."),
        ("Cambiar a registro formal", "Convierte «Los chiquillos van pa' la biblioteca» a registro formal.", ["«Chiquillos» pasa a «niños».", "«Pa'» se reemplaza por la preposición «a».", "Completo la oración."], "«Los niños van a la biblioteca»."),
    ],
    [("Repetir «cosa» y «bueno» en toda la exposición.", "Se piensa que son palabras seguras.", "Busca la palabra exacta: «elemento», «beneficioso», «útil»."), ("Hablar de «tú» a un público en una exposición formal.", "Se confunde cercanía con respeto.", "Dirígete con «ustedes» o usa expresiones neutras.")],
    [
        E("¿Cuál palabra es más precisa para «una cosa que sirve para unir hojas»: a) cosa b) corchetera?", "b", "Nombra el objeto con exactitud."),
        E("¿Cuál es un sinónimo de «bueno» en «un resultado bueno»: beneficioso o lento?", "Beneficioso", "Significa algo parecido en ese contexto."),
        E("¿Cuál frase está en registro formal: a) «Los niños van a la biblioteca.» b) «Los chiquillos van pa' la biblio.»", "a", "No usa modismos ni abreviaturas."),
    ],
    [
        E("Mejora la frase «Hay que hacer un mural»: ¿qué verbo es más preciso: pintar o hacer?", "Pintar", "Dice exactamente la acción."),
        E("Cambia a orden distinto: «Los estudiantes aprenden mejor cuando descansan». ¿Cuál es una versión válida: a) «Cuando descansan, los estudiantes aprenden mejor.» b) «Descansan cuando, aprenden mejor los estudiantes.»", "a", "Cambia el orden y se mantiene claro."),
        E("¿Cuál palabra evita repetir «cosa»: a) elemento b) cosa?", "a", "Es una palabra más precisa."),
    ],
    [
        E("Convierte a registro formal: «Pa' mí, esa onda del reciclaje es bacán.» ¿Cuál versión es mejor: a) «Para mí, el reciclaje es muy valioso.» b) «Pa' mí, el reciclaje es bacán.»", "a", "Evita modismos y completa las palabras."),
        E("Ordena de menos a más preciso para describir un animal: a) un animal de pelo b) un perro labrador c) un perro. Escribe las letras.", "a, c, b", "Cada versión es más específica que la anterior."),
        E("Elige una variación para no repetir «Yo creo que»: a) «Considero que…» b) «Yo creo que…» c) «Yo creo que yo creo…»", "a", "Es una forma distinta de introducir una opinión."),
    ],
    [
        E("Un estudiante dice: «El vocabulario formal es copiar palabras difíciles». ¿Es correcto? Responde sí o no.", "No", "Formal no es difícil: es cuidado y adecuado."),
        E("En «La actividad fue buena y el resultado fue bueno», ¿se repite la palabra «bueno»? Responde sí o no.", "Sí", "Aparece dos veces."),
    ],
    [
        E("Reemplaza una de las repeticiones: «El curso es bueno, el profesor es bueno, el patio es bueno». ¿Cuál versión varía mejor: a) «El curso es entretenido, el profesor es paciente, el patio es amplio.» b) «El curso es bueno, es bueno, es bueno.»", "a", "Cada palabra da información precisa."),
        E("Elige la palabra precisa para completar: «El libro nos entregó una ______ de pasos para plantar» (conjunto ordenado de pasos). Opciones: cosa / secuencia.", "Secuencia", "Es la palabra exacta para pasos ordenados."),
    ],
    [E("Debes exponer ante la directora sobre el cuidado del patio. ¿Qué frase sirve mejor: a) «Les mostraré los pasos para cuidar nuestro patio.» b) «Les voy a contar la onda de cuidar el patio, ya po.»", "a", "Es clara y de registro formal.")],
    [
        E("¿Cómo se llama una palabra con significado parecido a otra?", "Sinónimo", "Permite variar el vocabulario."),
        E("¿Se pueden usar modismos en una exposición formal? Responde sí o no.", "No", "Un registro formal evita los modismos."),
        E("¿Conviene repetir mucho la palabra «cosa»? Responde sí o no.", "No", "Es una palabra poco precisa."),
    ],
    ("Mejora este texto cambiando tres palabras vagas por palabras precisas, dos expresiones familiares por formales y una oración por otra construcción distinta: «Los chiquillos hicieron una cosa para el patio. Yo creo que fue bueno porque quedó bueno. Pa' mí, todos lo hicimos bien». Escribe la versión mejorada en tres oraciones.",
     "Los niños pintaron un mural para el patio. Considero que fue beneficioso, porque quedó colorido. Para mí, todos trabajamos con compromiso.",
     ["cambia palabras vagas", "reemplaza expresiones familiares", "varía la construcción de al menos una oración"], ["texto mejorado de tres oraciones"], ["mantener «cosa» y «bueno»", "dejar «pa'» o «chiquillos»"],
     "Subraya todas las palabras que se repiten y busca sinónimos."),
    "Escribe tres sinónimos de «interesante» para usar en una exposición.",
    "Busca en un texto de ciencias dos palabras precisas que no uses a diario y escríbelas con su significado.",
)

# ================================================================ OA 29 · clase 4
reg(
    OA29, 4,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para leer las oraciones en voz alta.",
    "Aprenderé a conjugar correctamente los verbos y a usar bien los participios irregulares al exponer. Sirve para que mi exposición sea correcta y no cometa errores como «hacido» o «rompido».",
    ["Sé que los verbos cambian según el tiempo y la persona.", "Sé que hay verbos irregulares."],
    [
        "Los verbos cambian según la persona (yo, tú, él), el número y el tiempo. Algunos verbos son irregulares: su forma cambia de un modo especial. Hay errores frecuentes al hablar: «yo cabo» en lugar de «yo quepo», «yo sabo» en lugar de «yo sé», «andé» en lugar de «anduve», «dijieron» en lugar de «dijeron», «tú quisistes» en lugar de «tú quisiste». En el verbo «haber» impersonal se usa siempre el singular: «hubo muchos niños» y no «hubieron».",
        "El participio es la forma del verbo que se usa para los tiempos compuestos: «he comido», «has dicho». Los verbos terminados en -ar forman el participio con -ado (cantar, cantado) y los terminados en -er o -ir con -ido (comer, comido; vivir, vivido). Pero algunos son irregulares: hacer → hecho; decir → dicho; escribir → escrito; ver → visto; poner → puesto; abrir → abierto; romper → roto; volver → vuelto; cubrir → cubierto; morir → muerto; resolver → resuelto; descubrir → descubierto.",
        "Cuando preparas una exposición, revisa tus verbos. Algunos errores aparecen por costumbre al hablar. Si dudas, piensa en el infinitivo (el verbo sin conjugar) y busca la forma correcta. Después, ensaya la frase en voz alta hasta que te suene natural. Una exposición con verbos bien usados transmite seguridad.",
    ],
    [("conjugar", "cambiar un verbo según persona, número y tiempo"), ("verbo irregular", "verbo que no sigue la regla general"), ("participio", "forma del verbo que se usa con «haber», como «hecho»"), ("infinitivo", "forma del verbo terminada en -ar, -er o -ir"), ("impersonal", "verbo sin sujeto que realiza la acción, como «hubo»")],
    [
        ("Corregir un participio", "Corrige: «Ya he escribido el informe».", ["El verbo es escribir.", "Su participio irregular es «escrito».", "Reemplazo la forma incorrecta."], "«Ya he escrito el informe»."),
        ("Corregir una conjugación", "Corrige: «Ayer andé por el parque».", ["El verbo es andar.", "En pasado, yo + andar es «anduve».", "Reescribo."], "«Ayer anduve por el parque»."),
    ],
    [("Decir «hacido» o «rompido».", "Se aplica la regla general a verbos irregulares.", "Usa el participio irregular: «hecho», «roto»."), ("Decir «hubieron muchos niños».", "Se confunde con el plural.", "Con «haber» impersonal usa el singular: «hubo muchos niños».")],
    [
        E("Para completar «Ya he ______ la tarea» con el verbo hacer, ¿qué forma va: hecho o hacido?", "Hecho", "Es el participio irregular de hacer."),
        E("¿Cuál es correcta: «He roto el vaso» o «He rompido el vaso»?", "He roto el vaso", "El participio de romper es «roto»."),
        E("¿Cuál es el participio de «escribir»: escribido o escrito?", "Escrito", "Es el participio irregular."),
    ],
    [
        E("Completa con el participio de «ver»: «Ya he ______ la película». Opciones: visto / vido.", "visto", "El participio de ver es «visto»."),
        E("Completa con el participio de «volver»: «Ha ______ a casa». Opciones: vuelto / volvido.", "vuelto", "El participio de volver es «vuelto»."),
        E("¿Cuál es correcta: «Yo no quepo en esa silla» o «Yo no cabo en esa silla»?", "Yo no quepo en esa silla", "«Quepo» es la forma correcta de «caber»."),
    ],
    [
        E("Corrige: «Ellos dijieron la verdad». ¿Cuál es la forma correcta: a) dijeron b) dijieron?", "a", "El pasado de «decir» en ellos es «dijeron»."),
        E("Corrige: «Hubieron muchos invitados». ¿Cuál es la forma correcta: a) «Hubo muchos invitados.» b) «Hubieron muchos invitados.»", "a", "«Haber» impersonal se usa en singular."),
        E("Completa con el participio de «poner»: «Han ______ la mesa». Opciones: puesto / ponido.", "puesto", "El participio de poner es «puesto»."),
    ],
    [
        E("Un estudiante dice: «Todos los participios terminan en -ado o -ido». ¿Es correcto? Responde sí o no.", "No", "Hay irregulares como hecho, dicho y escrito."),
        E("En «Tú quisistes ir», ¿el error está en el verbo «quisistes»? Responde sí o no.", "Sí", "La forma correcta es «quisiste»."),
    ],
    [
        E("Completa con la forma correcta de «poner» en pasado: «Ayer yo ______ la mesa». Opciones: puse / pusí.", "puse", "Es la forma correcta."),
        E("Elige la oración correcta: a) «He descubierto una solución.» b) «He descubrido una solución.»", "a", "El participio de descubrir es «descubierto»."),
    ],
    [E("Vas a exponer y escribes en tu guion: «Ya hemos resolvido el problema y lo hemos escribido». ¿Cuál es la corrección: a) «Ya hemos resuelto el problema y lo hemos escrito.» b) «Ya hemos resolvido y escribido.»", "a", "Los participios correctos son «resuelto» y «escrito».")],
    [
        E("Completa con el verbo abrir: «Han ______ la puerta del salón». Opciones: abierto / abrido.", "Abierto", "Es un participio irregular."),
        E("Completa con el verbo decir: «Ella ya ha ______ la verdad». Opciones: dicho / decido.", "Dicho", "Es un participio irregular."),
        E("¿Se dice «hubieron muchos niños»? Responde sí o no.", "No", "Se dice «hubo muchos niños»."),
    ],
    ("Corrige estas seis oraciones de una exposición y escríbelas bien: 1) Yo ya he escribido el guion. 2) Ayer yo andé por el centro. 3) Ellos dijieron que habían muchos invitados. 4) Alguien ha rompido la maqueta. 5) Yo sabo la respuesta. 6) Tú quisistes presentar primero. Después, léelas en voz alta y comprueba que suenan bien.",
     "1) Yo ya he escrito el guion. 2) Ayer yo anduve por el centro. 3) Ellos dijeron que había muchos invitados. 4) Alguien ha roto la maqueta. 5) Yo sé la respuesta. 6) Tú quisiste presentar primero.",
     ["corrige las seis oraciones", "usa los participios irregulares correctos", "usa «había» en singular"], ["seis oraciones corregidas"], ["dejar «hacido»-tipo formas", "confundir «había» con «habían»"],
     "Si dudas, piensa en el infinitivo y busca su participio irregular."),
    "Escribe dos oraciones con «he hecho» y «ha dicho».",
    "Escucha cuántas veces oyes «hubieron» o «habían» en una conversación y cómo se corrigen.",
)

# ================================================================ OA 29 · clase 5
reg(
    OA29, 5,
    "Este cuaderno, lápiz y una hoja. Opcional: una persona de tu casa para escucharte y decirte si se te oye bien.",
    "Aprenderé a pronunciar con claridad, usar un volumen audible, y apoyar mi exposición con entonación, pausas, énfasis, gestos y postura. Sirve para que todos me escuchen y entiendan lo que explico.",
    ["Sé organizar una exposición.", "Sé que la voz y el cuerpo comunican."],
    [
        "Cuando expones, importa tanto lo que dices como cómo lo dices. La pronunciación clara significa decir cada sílaba completa, sin comerte letras («estado», no «estao»). El volumen debe ser tal que se oiga hasta quien está en la última fila, sin gritar. La entonación es la subida y bajada de la voz; sin ella, la exposición suena monótona. Las pausas son silencios cortos que ordenan las ideas y dan tiempo para entender. El énfasis es destacar una palabra importante con más fuerza.",
        "Las pausas pueden cambiar el sentido de una frase. No es lo mismo «Vamos a comer, niños» (invitas a los niños) que «Vamos a comer niños» (¡una frase peligrosa!). El énfasis también cambia lo que se destaca: en «Yo traje el pan», si destacas «yo», muestras que fuiste tú y no otra persona; si destacas «pan», muestras que es eso y no otra cosa.",
        "El cuerpo acompaña a la voz. Una postura adecuada es de pie, con la espalda recta, los pies firmes y las manos visibles. Mira a la audiencia, no al suelo ni solo a la pantalla. Evita taparte la boca, dar la espalda o jugar con objetos. Los gestos deben apoyar el mensaje: señalar, contar con los dedos o abrir las manos para invitar, sin exagerar.",
    ],
    [("pronunciación", "manera de decir las palabras"), ("volumen", "fuerza de la voz"), ("entonación", "subida y bajada de la voz"), ("pausa", "silencio breve entre ideas"), ("énfasis", "mayor fuerza en una palabra importante")],
    [
        ("Poner pausas", "Marca con una barra (/) dónde harías una pausa en: «Hoy les hablaré del ajedrez un juego de estrategia».", ["Busco la frase añadida que explica algo.", "«Un juego de estrategia» explica el ajedrez.", "Pauso antes y después."], "«Hoy les hablaré del ajedrez / un juego de estrategia /»."),
        ("Elegir el énfasis", "Quieres destacar que el pan lo trajiste tú y no otra persona. En «Yo traje el pan», ¿qué palabra enfatizas?", ["La información clave es quién lo trajo.", "La palabra que lo señala es «yo».", "La digo con más fuerza."], "«Yo»."),
    ],
    [("Hablar muy rápido sin pausas.", "Se piensa que hay que terminar pronto.", "Haz pausas cortas entre ideas."), ("Mirar solo el papel o la pantalla.", "Se teme olvidar lo que se dirá.", "Mira a la audiencia y usa notas breves.")],
    [
        E("Hablas tan bajo que la última fila no te oye. ¿Qué elemento debes mejorar: volumen o postura?", "Volumen", "Es la fuerza con que sale la voz."),
        E("Decir «estao» en vez de «estado» es un problema de... ¿pronunciación o entonación?", "Pronunciación", "Se omiten sonidos de la palabra."),
        E("¿Qué es mejor para el público: a) mirar a la audiencia b) mirar solo el suelo?", "a", "El contacto visual conecta con quien escucha."),
    ],
    [
        E("La frase «Vamos a comer, niños» tiene una pausa después de «comer». ¿A quién se invita a comer: a los niños o los niños son el alimento?", "A los niños", "La coma separa la invitación de las personas a quienes se habla."),
        E("En «Mi hermano trajo el libro», quieres destacar que fue tu hermano y no otra persona. ¿Qué palabra enfatizas?", "Hermano", "Esa palabra identifica a quien lo trajo."),
        E("¿Qué postura es más adecuada para exponer: a) de pie, espalda recta y manos visibles b) de espaldas al público?", "a", "Es una postura abierta y segura."),
    ],
    [
        E("Marca con pausas lógicas: «En primer lugar el ajedrez ayuda a concentrarse». ¿Dónde harías la pausa: a) después de «lugar» b) después de «ajedrez ayuda»?", "a", "Separa el conector de la idea."),
        E("Para exponer en un salón, ¿qué volumen es el mejor: a) susurro b) voz clara y audible c) grito?", "b", "Se oye hasta atrás sin gritar."),
        E("Mientras expones, juegas con un lápiz y no miras a nadie. ¿Qué dos cosas debes corregir: a) gestos y mirada b) pausas y énfasis?", "a", "El lápiz distrae y la mirada conecta."),
    ],
    [
        E("Un estudiante dice: «Mientras más rápido hable, mejor suena». ¿Es correcto? Responde sí o no.", "No", "La rapidez dificulta entender; se necesitan pausas."),
        E("Quieres que se oiga que «solo una persona» llegó. ¿Qué palabra enfatizas en «Llegó solo una persona»: solo o llegó? Elige la que destaca la cantidad.", "Solo", "Resalta que fue únicamente una."),
    ],
    [
        E("Observas dos exposiciones con el mismo texto. La primera con voz monótona y la segunda con entonación y pausas. ¿En cuál se entiende mejor lo importante?", "En la segunda", "La entonación y las pausas marcan las ideas."),
        E("En «No quiero que vengas hoy», si enfatizas «hoy», se entiende que... a) no quieres que venga hoy, pero quizá otro día b) no quieres que venga nunca? Elige.", "a", "El énfasis en «hoy» marca el día."),
    ],
    [E("Ensayas una exposición en tu habitación y una persona de tu casa te dice que no te oye desde la puerta. ¿Qué haces: a) subes el volumen sin gritar y haces pausas b) hablas más rápido?", "a", "Mejora lo audible sin perder claridad.")],
    [
        E("¿Qué sirve para ordenar las ideas: una pausa o hablar sin parar?", "Una pausa", "Da tiempo para entender."),
        E("¿La entonación hace que la voz suene monótona? Responde sí o no.", "No", "La entonación evita la monotonía."),
        E("¿Conviene mirar a la audiencia al exponer? Responde sí o no.", "Sí", "Conecta con quien escucha."),
    ],
    ("Lee en voz alta esta introducción tres veces: «Buenos días, compañeros. Hoy les hablaré del cuidado de las plantas, un tema que me encanta. Les explicaré tres cuidados básicos». En la primera, léela muy rápido y sin pausas; en la segunda, con voz demasiado baja; en la tercera, con pausas, volumen audible, entonación y énfasis en «tres». Anota qué diferencia notaste y pide a una persona de tu casa que opine.",
     "En la tercera se entendía mejor porque había pausas después de «compañeros» y de «encanta», y la palabra «tres» sonaba más fuerte.",
     ["lee las tres versiones", "marca al menos dos pausas en la tercera", "enfatiza «tres»", "compara las versiones por escrito"], ["tres lecturas y una nota comparativa"], ["mantener la misma voz en las tres", "no anotar lo que notaste"],
     "Si no notas diferencia, exagera las pausas y la entonación."),
    "Escribe dos frases cuyo sentido cambie según dónde pongas la pausa o el énfasis.",
    "Graba tu voz si puedes o pide a alguien que te escuche y anota una mejora.",
)

# ================================================================ OA 29 · clase 6
reg(
    OA29, 6,
    "Este cuaderno, lápiz, una hoja y tarjetas de papel. Opcional: una persona de tu casa para ser la audiencia.",
    "Aprenderé a usar material de apoyo de manera efectiva y a exponer sin leer un texto escrito, usando solo palabras clave. Sirve para que mi exposición sea natural y la audiencia me mire a mí y no a un papel.",
    ["Sé organizar mi exposición y cuidar mi voz y mi cuerpo.", "Sé identificar las ideas principales de un tema."],
    [
        "El material de apoyo es todo lo que ayuda a explicar tu tema: diapositivas, papelógrafo, láminas, objetos o maquetas. Un buen material complementa lo que dices; no lo repite palabra por palabra. Cada diapositiva o lámina debe tener pocas palabras, letra grande, buena separación y una imagen clara. Una lámina con un párrafo largo obliga al público a leer y a no escucharte.",
        "Exponer sin leer significa decir las ideas con tus palabras, mirando a la audiencia. Para no perderte, usa una tarjeta con palabras clave, no con oraciones completas. Por ejemplo: «ajedrez — 16 piezas — jaque mate — concentración». Cada palabra te recuerda una idea que ya ensayaste. Mientras más ensayes, menos necesitarás mirar la tarjeta.",
        "Antes de exponer, ensaya con el material, controla el tiempo y revisa con una lista: ¿hay introducción, desarrollo y cierre?, ¿mis ideas tienen ejemplos o datos?, ¿uso conectores y vocabulario preciso?, ¿se me oye y miro a la audiencia?, ¿el material ayuda y no sobra? Revisar así te permite mejorar antes de presentar.",
    ],
    [("material de apoyo", "recurso visual o físico que ayuda a explicar"), ("palabra clave", "palabra que recuerda una idea importante"), ("papelógrafo", "pliego de papel grande para exponer"), ("lámina", "hoja o cartel con imagen y poco texto"), ("ensayar", "practicar antes de presentar")],
    [
        ("Mejorar una lámina", "Una lámina sobre el ajedrez dice: «El ajedrez es un juego de mesa de estrategia en que dos jugadores mueven 16 piezas cada uno en un tablero de 64 casillas con el objetivo de dar jaque mate». ¿Cómo la mejoras?", ["Veo que tiene demasiado texto.", "Dejo solo palabras clave y datos.", "Agrego una imagen simple."], "Dejar pocas palabras: «Ajedrez: 16 piezas, 64 casillas, jaque mate», con un dibujo de un tablero."),
        ("Pasar a palabras clave", "Convierte «Primero explicaré cómo se mueven las piezas y luego cómo se gana la partida» en palabras clave.", ["Busco las ideas.", "Quedan: movimientos y cómo se gana.", "Las escribo cortas."], "«Movimientos — cómo se gana»."),
    ],
    [("Leer palabra por palabra lo que dice la diapositiva.", "Se piensa que así no se olvida nada.", "Habla con tus palabras y usa la lámina como apoyo."), ("Llenar la lámina de texto.", "Se cree que más información es mejor.", "Deja palabras clave, un dato y una imagen.")],
    [
        E("Una lámina tiene un párrafo de 12 líneas. ¿Qué problema tiene: demasiado texto o falta de color?", "Demasiado texto", "El público leería en lugar de escucharte."),
        E("¿Qué debe tener una buena lámina: pocas palabras y una imagen clara o un párrafo largo?", "Pocas palabras y una imagen clara", "Complementa lo que dices."),
        E("Para exponer sin leer, ¿qué usas: una tarjeta con palabras clave o un guion completo?", "Una tarjeta con palabras clave", "Te recuerda las ideas sin leer."),
    ],
    [
        E("Convierte en palabras clave: «Explicaré por qué el reciclaje de papel ayuda a cuidar los bosques». ¿Cuál es mejor: a) «Reciclaje de papel — bosques» b) toda la oración?", "a", "Las palabras clave recuerdan sin leer."),
        E("¿Qué tamaño de letra conviene en una lámina para que se lea desde atrás: grande o muy pequeña?", "Grande", "Debe verse desde el fondo."),
        E("Ensayar con el material antes de exponer sirve para... ¿controlar el tiempo y mejorar o dejarlo todo igual?", "Controlar el tiempo y mejorar", "El ensayo permite corregir antes."),
    ],
    [
        arith("Tu exposición debe durar 5 minutos. Planeas 1 minuto de introducción y 1 minuto de cierre. ¿Cuántos minutos quedan para el desarrollo?", "5-1-1", "Se restan introducción y cierre del tiempo total."),
        E("Ordena los pasos para preparar la exposición: a) ensayar con el material b) elegir las ideas principales c) crear la lámina con pocas palabras. Escribe las letras.", "b, c, a", "Se ordenan las ideas, se prepara el material y se ensaya."),
        arith("Tienes tres ideas y 3 minutos de desarrollo. Cada idea dura el mismo tiempo. ¿Cuántos minutos para cada una?", "3//3", "Se reparte el tiempo en partes iguales."),
    ],
    [
        E("Un estudiante dice: «La diapositiva debe llevar todo lo que voy a decir». ¿Es correcto? Responde sí o no.", "No", "La lámina apoya, no reemplaza lo que dices."),
        E("Tu tarjeta dice: «Primero hablaré sobre las piezas del ajedrez y después, si me alcanza el tiempo, hablaré sobre la historia». ¿Qué problema tiene como tarjeta de exposición sin leer: está escrita en oraciones largas o tiene pocas palabras? Elige.", "Está escrita en oraciones largas", "Una tarjeta debe llevar palabras clave."),
    ],
    [
        E("Revisa con esta lista: ¿hay introducción?, ¿hay cierre?, ¿hay un dato?, ¿la lámina tiene poco texto? Una exposición tiene introducción, cierre y lámina con poco texto, pero no tiene datos. ¿Qué criterio debes mejorar?", "Incluir un dato", "Falta fundamentar con datos."),
        E("La exposición de Camila tiene todas las partes pero lee de la hoja sin mirar. ¿Qué debe mejorar: exponer sin leer o agregar más conectores? Elige.", "Exponer sin leer", "Mirar a la audiencia y usar palabras clave."),
    ],
    [E("Tu curso hará una feria de exposiciones. Quieres presentar «el cuidado del agua» con un papelógrafo. ¿Cuál es el mejor contenido: a) título, tres palabras clave y un dibujo de una gota b) todo el texto de tu informe", "a", "El papelógrafo debe ser claro y con poco texto.")],
    [
        E("¿Cómo se llaman las palabras que recuerdan las ideas importantes sin leer todo?", "Palabras clave", "Resumen la idea en pocas palabras."),
        E("¿La lámina debe reemplazar lo que dices? Responde sí o no.", "No", "Debe complementar lo que dices."),
        E("¿Sirve ensayar antes de exponer? Responde sí o no.", "Sí", "Permite mejorar y controlar el tiempo."),
    ],
    ("Prepara una mini exposición de 2 minutos sobre «mi pasatiempo favorito» o «cuidado de una mascota». Haz 1) una lámina o dibujo con título, tres palabras clave y una imagen simple, 2) una tarjeta con palabras clave (introducción, tres ideas, cierre), 3) ensaya sin leer. Pide a una persona de tu casa que te escuche y marque con cruz: ¿introducción?, ¿desarrollo?, ¿cierre?, ¿se oye?, ¿miró al público?",
     "Lámina: «Mi bicicleta» — frenos, casco, rutas — dibujo de una bicicleta. Tarjeta: intro — frenos — casco — rutas — cierre.",
     ["la lámina tiene poco texto", "la tarjeta usa palabras clave", "expone sin leer", "revisa con la lista"], ["lámina, tarjeta y lista de revisión"], ["llenar la lámina de texto", "leer palabra por palabra"],
     "Si leíste el papel, reduce cada oración de tu tarjeta a una o dos palabras."),
    "Escribe palabras clave para una exposición sobre el reciclaje del plástico.",
    "Observa una presentación con láminas y anota una cosa que ayude a entender y otra que sobre.",
)
