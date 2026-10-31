"""Cuaderno del estudiante, 3.º básico Lenguaje y Comunicación, OA 03 (repertorio literario) y OA 04 (comprensión profunda de narraciones).

Todos los textos son originales, escritos para este cuaderno; cada ejercicio trae el texto que necesita.
"""
from __future__ import annotations

from student_lessons import arith, ex, register

OA3, OA4 = "LE03 OA 03", "LE03 OA 04"
E = ex


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def L(oa, n, materials, use, prior, explain, vocab, worked, mistakes, tiers, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers=dict(zip(("recovery", "understand", "apply", "reason", "challenge"), tiers)),
        context=ctx, selfcheck=sc, open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )


# ------------------------------------------------------------------ OA 03
ZORRO = ("Había una vez un zorro flaco que quería cruzar el río. Le pidió ayuda a una tortuga. "
         "—Sube a mi caparazón —dijo la tortuga—, pero no te muevas. El zorro subió. "
         "A la mitad del río empezó a rascarse las pulgas y la tortuga se hundió un poquito. "
         "Desde entonces, cuentan los abuelos, el zorro cruza el río solo por el puente.")

L(OA3, 1,
  "Este cuaderno, lápiz y el cuento escrito en esta clase. Si quieres, pide a una persona de tu casa que cuente un cuento que le contaron cuando era niña o niño.",
  "Aprenderé a reconocer un cuento folclórico, que pasa de voz en voz entre generaciones, y a explicar qué guarda de la memoria de un pueblo.",
  ["Sé distinguir quiénes son los personajes de un cuento.", "Sé contar qué pasa al principio, en el medio y al final."],
  ["Un cuento folclórico es un cuento que se cuenta de generación en generación. Los abuelos se lo cuentan a los padres, los padres a los niños, y así por muchos años. Casi nunca se sabe quién lo inventó primero: por eso se dice que es anónimo.",
   "Estos cuentos suelen empezar con frases como «Había una vez» y terminar con frases como «Desde entonces…». Sus personajes pueden ser animales que hablan. Como se cuentan de boca en boca, cada persona los cuenta un poco distinto. A esas diferencias se les llama variantes.",
   "Los cuentos folclóricos guardan la memoria de un pueblo: lo que le preocupaba, cómo explicaba el mundo y qué enseñanzas quería dejar. Al leerlos, no solo nos entretenemos, también conocemos cómo pensaban y vivían quienes los contaron antes que nosotros."],
  [("folclórico", "que pertenece a la tradición de un pueblo y se transmite por generaciones"), ("anónimo", "de autor desconocido"), ("variante", "una forma un poco distinta de contar el mismo cuento"), ("tradición", "lo que un pueblo conserva y pasa de unos a otros")],
  [("Reconocer rasgos folclóricos", f"Lee el cuento: «{ZORRO}» ¿Qué rasgos de cuento folclórico tiene?", ["Empieza con «Había una vez».", "Los personajes son animales que hablan.", "Termina con «Desde entonces, cuentan los abuelos»: se transmite de boca en boca."], "Inicio con fórmula, animales que hablan y final que alude a los abuelos"),
   ("Entender una variante", "Una abuela cuenta el cuento con una tortuga y un zorro. Otra abuela lo cuenta con una tortuga y un conejo. ¿Qué son estas diferencias?", ["El cuento es el mismo, con algo distinto.", "Pasa cuando se cuenta de boca en boca.", "Esas diferencias se llaman variantes."], "Son variantes del mismo cuento")],
  [("Pensar que todo cuento con animales es folclórico.", "Se mira solo a los personajes.", "Pregunta también si se transmite de generación en generación y si el autor es anónimo."), ("Creer que hay una sola forma correcta de contar un cuento folclórico.", "Se olvida que se cuenta de boca en boca.", "Acepta que existen variantes.")],
  ([E(f"Lee el cuento: «{ZORRO}» ¿Qué animal quería cruzar el río?", "El zorro", "El primer personaje que aparece es un zorro flaco."),
    E(f"Lee el cuento: «{ZORRO}» ¿Quién le ofreció ayuda al zorro?", "La tortuga", "El zorro le pidió ayuda a la tortuga."),
    E("¿Con qué frase comienza el cuento del zorro y la tortuga?", "Había una vez", "Es la frase con que se abre este cuento folclórico.")],
   [E("Los cuentos folclóricos se cuentan de abuelos a nietos. ¿Qué significa que sean anónimos: (a) que no se sabe quién los inventó primero o (b) que no tienen personajes?", "(a)", "Anónimo es de autor desconocido."),
    E("¿Qué frase indica que el cuento viene de la tradición: «Había una vez» o «Mañana a las ocho»?", "«Había una vez»", "Esa frase es típica del inicio de cuentos tradicionales."),
    E("¿Cuál es el problema del zorro al comienzo del cuento?", "Quería cruzar el río y no podía", "Por eso le pide ayuda a la tortuga.")],
   [E("¿Qué hizo el zorro a la mitad del río?", "Se rascó las pulgas", "El texto lo dice con esas palabras."),
    E("¿Por qué se hundió un poquito la tortuga?", "Porque el zorro se movió", "La tortuga había pedido que no se moviera y el zorro se rascó."),
    E("Ordena estos hechos con letras: (a) la tortuga se hundió un poquito, (b) el zorro subió al caparazón, (c) el zorro pidió ayuda.", "c, b, a", "Primero pidió ayuda, luego subió y después se hundió la tortuga.")],
   [E("Dos abuelas cuentan el cuento: una dice «zorro y tortuga» y la otra «zorro y pato». ¿Cómo se llaman esas diferencias?", "Variantes", "Se cuentan de boca en boca y cada versión cambia un poco."),
    E("¿Qué enseñanza deja el cuento: (a) hay que seguir lo que pide quien nos ayuda o (b) los zorros nadan muy bien?", "(a)", "El zorro se movió aunque la tortuga se lo pidió, y por eso hubo problemas.")],
   [E("¿Cuántos personajes tiene el cuento del zorro y la tortuga?", "2", "Los personajes son el zorro y la tortuga."),
    E("Marca V si es verdadero o F si es falso: 1) Se transmite de boca en boca. 2) Siempre tiene un autor conocido.", "1 V, 2 F", "Los cuentos folclóricos pasan de generación en generación y casi siempre son anónimos.")]),
  [E("Una persona de tu casa te cuenta un cuento que le contaron cuando era pequeña y empieza con «Había una vez». ¿Qué rasgo de cuento folclórico tiene esa situación?", "Se transmite de generación en generación", "El cuento pasó de boca en boca hasta llegar a ti.")],
  [E("¿Cómo se llama un cuento que pasa de generación en generación?", "Cuento folclórico", "Ese es el nombre de este tipo de cuento."),
   E("¿Quién escribió primero un cuento folclórico: se conoce siempre o casi nunca?", "Casi nunca", "Casi siempre son anónimos."),
   E("¿Cómo se llaman las pequeñas diferencias entre versiones de un mismo cuento?", "Variantes", "Se producen al contarlo de boca en boca.")],
  ("Elige uno de estos comienzos y cuéntale un cuento folclórico breve a una persona, de memoria o inventado por ti: «Había una vez un gallo que…» o «Había una vez una hormiga que…». Después responde en tu cuaderno: ¿qué frase de inicio y qué frase de cierre usaste? ¿Qué enseñanza dejó tu cuento? Si lo conoces por tradición de tu familia, recuerda que cada familia lo cuenta a su manera.", "«Había una vez una hormiga que quería subir a un árbol. Nadie creía que pudiera. Subió poco a poco y llegó. Desde entonces, cuentan, las hormigas no se rinden». Inicio: «Había una vez». Cierre: «Desde entonces». Enseñanza: perseverar.", ["usa una frase de inicio y una de cierre tradicionales", "tiene personajes y un problema", "dice la enseñanza"], ["cuento oral o escrito", "tres respuestas escritas"], ["contar solo una escena sin problema", "no decir la enseñanza"], "Pide a quien te escuchó que cuente cómo contaría él o ella esa misma historia; así verás una variante."),
  "Pregunta a una persona mayor qué cuento le contaban de niña o niño y cuéntalo a otra persona.",
  "Compara tu versión con la de otra persona y escribe dos diferencias (variantes).")

TEXTO_A = ("Matías encontró una llave oxidada bajo el columpio. Probó abrir el candado del galpón, pero no giraba. "
           "Entonces la limpió con un paño y un poco de aceite. Esta vez giró. Dentro del galpón había una bicicleta azul con un lazo. "
           "Un papel decía: «Para quien cuide la llave».")
TEXTO_B = ("Encontré una llave oxidada bajo el columpio. Probé abrir el candado del galpón, pero no giraba. "
           "Entonces la limpié con un paño y un poco de aceite. Esta vez giró.")

L(OA3, 2,
  "Este cuaderno, lápiz y los dos textos escritos en esta clase.",
  "Aprenderé a leer un cuento de autor y a notar las decisiones que toma quien lo escribe: quién narra, qué cuenta y qué deja sin decir. También conoceré la novela, un relato de autor mucho más largo.",
  ["Sé reconocer personajes y lo que hacen.", "Conozco los cuentos folclóricos."],
  ["Un cuento de autor es un cuento que escribió una persona conocida, que lo firma. El autor decide cómo contar la historia: elige el título, los personajes, el lugar, el final y quién la narra.",
   "El narrador es la voz que cuenta lo que pasa. Puede ser un personaje que dice «yo», como en «Encontré una llave». Entonces es un narrador en primera persona. O puede ser alguien que está fuera de la historia y habla de «él» o «ella», como en «Matías encontró una llave». Entonces es un narrador en tercera persona.",
   "El autor también decide qué no contar. Si no dice quién dejó una bicicleta en un galpón, el lector queda con una pregunta y quiere seguir leyendo. Esas decisiones dan forma a la historia y hacen que dos cuentos con la misma idea suenen muy distintos.",
   "Una novela es un relato de autor mucho más largo que un cuento. Se divide en capítulos y se lee durante varios días. En una novela, los personajes viven varias aventuras y el problema se resuelve poco a poco. Por ejemplo, el hallazgo de la llave podría ser solo el capítulo 1 de una novela sobre Matías."],
  [("autor", "la persona que escribe el cuento"), ("narrador", "la voz que cuenta lo que pasa"), ("primera persona", "narrador que dice «yo» o «nosotros»"), ("tercera persona", "narrador que cuenta sobre «él», «ella» o «ellos»"), ("novela", "relato largo de un autor, dividido en capítulos")],
  [("Reconocer el narrador", f"Lee: «{TEXTO_B}» ¿Qué narrador tiene?", ["Veo verbos como «encontré» y «probé».", "Esos verbos dicen «yo».", "Es un narrador en primera persona."], "Narrador en primera persona"),
   ("Reconocer lo que el autor no dice", f"Lee: «{TEXTO_A}» ¿Qué pregunta le deja el autor al lector?", ["El papel dice «Para quien cuide la llave».", "No dice quién dejó la bicicleta.", "El lector queda preguntándose quién la dejó."], "¿Quién dejó la bicicleta?")],
  [("Creer que el narrador y el autor son siempre la misma persona.", "Se confunde la voz que cuenta con quien escribe.", "El narrador es una voz que el autor crea."), ("Pensar que el cuento de autor no tiene decisiones.", "Se lee sin fijarse en cómo está contado.", "Pregúntate qué decidió el autor: título, narrador, final.")],
  ([E("En Lenguaje: ¿Qué es un autor?", "La persona que escribe el cuento", "Es quien crea y firma el texto."),
    E("¿Cómo se llama la voz que cuenta lo que pasa en un cuento?", "Narrador", "El narrador relata los hechos."),
    E(f"Lee: «{TEXTO_A}» ¿Quién encontró la llave?", "Matías", "El texto dice que Matías encontró la llave.")],
   [E(f"Lee: «{TEXTO_B}» Fíjate en «encontré». ¿El narrador es de primera o de tercera persona?", "De primera persona", "Dice «yo» al narrar sus acciones."),
    E(f"Lee: «{TEXTO_A}» ¿El narrador es de primera o de tercera persona?", "De tercera persona", "Cuenta sobre Matías, que es «él»."),
    E("En Lenguaje: ¿Cómo se llama el relato de autor largo, dividido en capítulos, que se lee durante varios días?", "Novela", "La novela es más larga que un cuento y se organiza en capítulos.")],
   [E(f"Lee: «{TEXTO_A}» ¿Dónde estaba la llave?", "Bajo el columpio", "El texto lo dice al comienzo."),
    E(f"Lee: «{TEXTO_A}» ¿Qué usó Matías para limpiar la llave?", "Un paño y un poco de aceite", "El texto dice con qué la limpió."),
    arith("Una novela tiene 12 capítulos y ya leíste 5. ¿Cuántos capítulos te faltan?", "12-5", "Se restan los capítulos leídos del total de capítulos.")],
   [E(f"Lee: «{TEXTO_A}» El autor no dice quién dejó la bicicleta. ¿Qué efecto tiene en el lector: (a) se pregunta quién fue o (b) sabe toda la historia?", "(a)", "Lo que no se cuenta despierta curiosidad."),
    E("El autor escribe «Matías sonrió». ¿Quién cuenta esto: (a) un narrador que cuenta desde fuera o (b) Matías hablando de sí mismo?", "(a)", "Está en tercera persona, no dice «yo».")],
   [E(f"Lee: «{TEXTO_A}» ¿Cuántas acciones de Matías ocurren antes de que la llave gire?", "3", "Encontró la llave, probó abrir el candado y la limpió."),
    E("Reescribe con narrador en primera persona: «Matías encontró una llave».", "Encontré una llave", "En primera persona el verbo dice «yo».")]),
  [E("En la portada de un libro de la biblioteca dice «Cuentos de la luna, escritos por Elisa Verde». ¿Es un cuento de autor o un cuento folclórico anónimo?", "De autor", "Tiene el nombre de la persona que lo escribió.")],
  [E("¿Quién decide cómo se cuenta un cuento de autor?", "El autor", "Elige narrador, título y final."),
   E("Si el narrador dice «yo», ¿es de primera o de tercera persona?", "De primera persona", "«Yo» indica primera persona."),
   E("Si el autor no cuenta algo, ¿qué siente el lector?", "Curiosidad", "Quiere saber lo que no se dice.")],
  (f"Lee este texto: «{TEXTO_A}» Escribe en tu cuaderno cuatro oraciones: la primera dice el título que le pondrías; la segunda, si el narrador es de primera o de tercera persona; la tercera, algo que el autor no cuenta; la cuarta, cómo cambiarías el final.", "Título: «La bicicleta del galpón». El narrador es de tercera persona. El autor no dice quién dejó la bicicleta. Yo agregaría que Matías devuelve la llave a su dueño.", ["escribe un título pertinente", "identifica bien al narrador", "señala algo no contado", "propone un final con relación al texto"], ["cuatro oraciones escritas"], ["confundir primera y tercera persona", "cambiar la historia por completo"], "Lee tu final a otra persona y pregúntale si tiene sentido con el resto del texto."),
  "Busca un cuento de autor en tu casa o biblioteca y anota quién lo escribió y si el narrador dice «yo».",
  "Reescribe el texto de Matías con narrador en primera persona y compara qué cambió.")

GALLO = ("Un gallo subió al tejado y cantó: —¡Yo hago salir el sol! Todos los animales de la granja lo escuchaban. "
         "Un día el gallo amaneció con la voz ronca y no pudo cantar. Esa mañana el sol salió igual, como siempre. "
         "El gallo bajó la cabeza y entendió que el sol no lo necesitaba a él.")

L(OA3, 3,
  "Este cuaderno, lápiz y la fábula escrita en esta clase.",
  "Aprenderé a leer fábulas, a mirar cómo los hechos llevan a una enseñanza y a explicar esa enseñanza con mis palabras.",
  ["Sé reconocer personajes, problema y final.", "Conozco cuentos con animales."],
  ["Una fábula es un relato breve en que los personajes suelen ser animales que piensan, hablan y se comportan como personas. Cuenta un hecho que lleva a una enseñanza para la vida, que se llama moraleja.",
   "La moraleja no está sola: sale de lo que les pasa a los personajes. Por eso, para entenderla, primero hay que entender la historia. En la fábula del gallo, el gallo presume de algo que no depende de él. Cuando no puede cantar, el sol sale igual, y eso le muestra que se equivocó.",
   "Una misma fábula puede dejar más de una enseñanza, y se puede decir de varias maneras. «No presumas de lo que no depende de ti» y «Valora lo que haces sin creerte imprescindible» dicen algo parecido. Lo importante es poder explicar qué hechos de la historia las apoyan."],
  [("fábula", "relato breve con animales que se comportan como personas y dejan una enseñanza"), ("moraleja", "enseñanza que deja una fábula"), ("presumir", "mostrarse como mejor de lo que uno es"), ("imprescindible", "que no puede faltar")],
  [("Mirar los hechos", f"Lee: «{GALLO}» ¿Qué hecho muestra que el sol no dependía del gallo?", ["Busco qué pasó cuando el gallo no cantó.", "El texto dice que el sol salió igual.", "Ese hecho prueba que el gallo no hacía salir el sol."], "El sol salió igual aunque el gallo no cantó"),
   ("Proponer una moraleja", "A partir de esa fábula, ¿qué moraleja puede decirse: (a) no presumas de lo que no depende de ti o (b) madruga siempre?", ["La fábula trata de presumir.", "El gallo presumió y se equivocó.", "La moraleja (a) se apoya en los hechos."], "(a) No presumas de lo que no depende de ti")],
  [("Decir la moraleja sin explicar qué hechos la sostienen.", "Se aprende una frase de memoria.", "Siempre agrega «porque el gallo…» y señala el hecho."), ("Pensar que la fábula solo puede dejar una enseñanza con las mismas palabras.", "Se cree que hay una única frase correcta.", "Acepta frases distintas si se apoyan en los mismos hechos.")],
  ([E(f"Lee: «{GALLO}» ¿Qué decía el gallo desde el tejado?", "Que él hacía salir el sol", "Es lo que anuncia en su canto."),
    E(f"Lee: «{GALLO}» ¿Qué le pasó al gallo un día?", "Amaneció con la voz ronca y no pudo cantar", "El texto dice que no pudo cantar."),
    E(f"Lee: «{GALLO}» ¿Salió el sol cuando el gallo no cantó?", "Sí", "El texto dice que salió igual.")],
   [E("En una fábula los animales hablan y actúan como personas. ¿Qué rasgo humano tiene el gallo: presumir o poner huevos?", "Presumir", "Presumir es una conducta humana; poner huevos es de las gallinas."),
    E("¿Cómo se llama la enseñanza que deja una fábula?", "Moraleja", "Es el nombre de esa enseñanza."),
    E(f"Lee: «{GALLO}» ¿Qué hizo el gallo al final: subió más alto o bajó la cabeza?", "Bajó la cabeza", "Es la última acción antes de entender.")],
   [E(f"Lee: «{GALLO}» ¿Qué hecho prueba que el sol no dependía del gallo?", "Que el sol salió aunque el gallo no cantó", "Ese es el hecho que lo muestra."),
    E(f"Lee: «{GALLO}» Escribe con letras el orden: (a) el sol salió igual, (b) el gallo cantó que hacía salir el sol, (c) el gallo no pudo cantar.", "b, c, a", "Primero presumió, luego no pudo cantar y después salió el sol."),
    E(f"Lee: «{GALLO}» ¿Cuántos animales aparecen nombrados: solo el gallo o también otros animales de la granja?", "También otros animales de la granja", "El texto dice que todos los animales de la granja lo escuchaban.")],
   [E("¿Qué moraleja se apoya en la fábula del gallo: (a) no presumas de lo que no depende de ti o (b) hay que comer temprano?", "(a)", "El gallo presumió de algo que no dependía de él."),
    E("Alguien dice que la moraleja es «Hay que levantarse temprano». ¿Se apoya en lo que pasó en la fábula?", "No", "En la historia no se habla de levantarse temprano.")],
   [E("Dos niñas dicen la moraleja de dos maneras: «No presumas de lo que no depende de ti» y «No te creas imprescindible si no lo eres». ¿Son iguales, parecidas o muy distintas?", "Parecidas", "Ambas se apoyan en el mismo hecho: el gallo no hacía salir el sol."),
    E("¿Qué hecho es la causa de que el gallo bajara la cabeza: (a) ver que el sol salió sin su canto o (b) que le dolía la pata?", "(a)", "El texto dice que entendió que el sol no lo necesitaba.")]),
  [E("Una amiga te dice: «Yo gano siempre en todo y nadie me ayuda». Después se resfría y la ayudan sus compañeros. ¿Con qué moraleja de la fábula del gallo se parece: no presumas de lo que no depende de ti o nunca juegues en equipo?", "No presumas de lo que no depende de ti", "Se parece porque presume y luego se da cuenta de que no lo hacía todo ella.")],
  [E("¿Qué es una fábula?", "Un relato breve con animales que dejan una enseñanza", "Los animales actúan como personas."),
   E("¿La moraleja sale de los hechos de la historia o aparece sola?", "Sale de los hechos", "Se explica con lo que les pasa a los personajes."),
   E("¿Una fábula puede tener una moraleja dicha de formas distintas?", "Sí", "Lo importante es que se apoye en los hechos.")],
  (f"Lee la fábula del gallo: «{GALLO}» Completa tres frases en tu cuaderno: «El problema del gallo fue…», «Lo que pasó cuando no pudo cantar fue…», «La moraleja que yo veo es…, porque…». Luego dile tu moraleja a una persona y pregúntale si está de acuerdo.", "El problema del gallo fue que presumía de hacer salir el sol. Cuando no pudo cantar, el sol salió igual. La moraleja que yo veo es no presumir de lo que no depende de uno, porque el sol salió sin él.", ["describe el problema con el texto", "cuenta el hecho clave", "explica la moraleja con un porque"], ["tres frases completadas"], ["moraleja sin explicar por qué", "inventar hechos que no están"], "Compara tu moraleja con la de otra persona: ¿se apoyan en el mismo hecho de la fábula?"),
  "Cuenta la fábula del gallo con tus palabras a una persona de tu casa y explica qué te enseña.",
  "Escribe tres líneas sobre una situación de tu vida que se parezca a la del gallo.")

MITO = ("Cuentan que al principio del mundo solo había noche. Una anciana poderosa guardaba el sol en una vasija. "
        "Un zorro astuto la distrajo y rompió la vasija, y el sol salió volando al cielo. Desde entonces hay día y noche.")

CERRO = ("Cuentan en el valle que, hace mucho tiempo, un gigante bueno cuidaba a los pastores. "
         "Una noche de tormenta los guió hasta una cueva y los salvó del frío. "
         "Al amanecer, el gigante estaba tan cansado que se acostó junto al valle y no se levantó más. "
         "Por eso, dicen, el cerro que se ve desde el pueblo parece una persona acostada.")

L(OA3, 4,
  "Este cuaderno, lápiz, la leyenda y el mito escritos en esta clase. Aviso: ambos relatos son inventados para este cuaderno, no son relatos reales de ningún pueblo.",
  "Aprenderé a reconocer una leyenda, que explica el origen de un lugar, a distinguirla de un mito y a ver cómo se vincula con un territorio real.",
  ["Conozco cuentos folclóricos y fábulas.", "Sé reconocer lugares en un texto."],
  ["Una leyenda es un relato que se cuenta de boca en boca y que explica el origen de un lugar, de una forma natural o de una costumbre. Mezcla hechos que podrían ser reales con elementos fantásticos, como gigantes o seres mágicos.",
   "Lo que distingue a la leyenda es su vínculo con un lugar. La gente la cuenta mirando un cerro, un lago o una piedra, y dice «allí pasó». Así, el paisaje guarda la historia y la historia le da sentido al paisaje.",
   f"Un mito es otro relato muy antiguo. Explica cómo empezó el mundo o algo muy grande, como el día, el fuego o el mar, y en él actúan seres poderosos, como dioses o espíritus. Suele hablar del origen de todo y no de un lugar en particular. Este es un mito inventado: «{MITO}»",
   "Cada comunidad tiene sus propias leyendas y mitos, y los cuenta a su manera. Los de los pueblos originarios son parte de su cultura: la forma tradicional de contarlos la enseñan quienes los conocen en cada comunidad. La leyenda y el mito de hoy son inventados para este cuaderno."],
  [("leyenda", "relato que explica el origen de un lugar o de algo de la naturaleza"), ("territorio", "lugar o región donde vive una comunidad"), ("fantástico", "que no puede pasar en la realidad"), ("paisaje", "lo que se ve de un lugar: cerros, ríos, árboles"), ("mito", "relato muy antiguo que explica cómo empezó el mundo o algo muy grande, con seres poderosos")],
  [("Encontrar el lugar", f"Lee: «{CERRO}» ¿Qué lugar explica la leyenda?", ["Busco qué se ve desde el pueblo.", "El texto dice que es un cerro.", "El cerro parece una persona acostada."], "El cerro que parece una persona acostada"),
   ("Separar lo real de lo fantástico", "En esa leyenda, ¿qué elemento es fantástico: el valle o el gigante?", ["Un valle puede existir de verdad.", "Un gigante que se acuesta y se vuelve cerro no existe.", "Lo fantástico es el gigante."], "El gigante")],
  [("Creer que una leyenda es un hecho comprobado.", "Se mezcla con una noticia.", "Reconoce que explica el origen de un lugar con elementos fantásticos."), ("Contar la leyenda sin decir de qué lugar habla.", "Se olvida el vínculo con el territorio.", "Menciona el lugar que la leyenda explica.")],
  ([E(f"Lee: «{CERRO}» ¿Quién cuidaba a los pastores?", "Un gigante bueno", "El texto lo dice en la primera oración."),
    E(f"Lee: «{CERRO}» ¿Adónde guió el gigante a los pastores?", "A una cueva", "Los guió hasta una cueva en la tormenta."),
    E(f"Lee: «{CERRO}» ¿Qué parece el cerro desde el pueblo?", "Una persona acostada", "Así lo dice el final de la leyenda.")],
   [E("¿Qué explica una leyenda: el origen de un lugar o la receta de una comida?", "El origen de un lugar", "Es lo propio de una leyenda."),
    E("En una leyenda, ¿hay elementos fantásticos o todo es real?", "Hay elementos fantásticos", "Mezcla hechos posibles con elementos imposibles."),
    E(f"Lee el mito inventado: «{MITO}» ¿Qué explica este mito: cómo empezó el día o el origen de un cerro?", "Cómo empezó el día", "El mito habla del origen del día y de la noche, no de un lugar concreto.")],
   [E(f"Lee: «{CERRO}» ¿Cuándo se acostó el gigante: al amanecer o al atardecer?", "Al amanecer", "El texto dice «Al amanecer»."),
    E(f"Lee: «{CERRO}» ¿Cómo salvó el gigante a los pastores?", "Los guió a una cueva y los salvó del frío", "Eso hizo durante la tormenta."),
    E(f"Lee el mito inventado: «{MITO}» ¿Quién rompió la vasija?", "El zorro", "El texto dice que el zorro rompió la vasija.")],
   [E("¿Qué elemento hace diferente a una leyenda de una noticia: (a) un gigante que se vuelve cerro o (b) un pueblo?", "(a)", "Es fantástico, y las noticias cuentan hechos reales."),
    E("Dos amigos leen la leyenda. Uno dice «es un hecho real que ocurrió». Otro dice «explica de forma fantástica el origen de un cerro». ¿Quién tiene razón?", "El segundo", "Una leyenda es un relato tradicional, no un hecho comprobado.")],
   [E("Hay dos relatos inventados: la leyenda del gigante y el mito del sol. ¿Cuál está unido a un cerro que se ve desde el pueblo?", "La leyenda del gigante", "La leyenda se une a un paisaje concreto; el mito habla del origen del día."),
    E(f"Lee: «{CERRO}» ¿Qué dato podría ocurrir en la vida real: una noche de tormenta o un gigante que se vuelve cerro?", "Una noche de tormenta", "Las tormentas existen; los gigantes que se vuelven cerros no.")]),
  [E("En tu escuela cuentan que una piedra grande en el patio «cayó de la luna». ¿Qué tipo de relato sería: una leyenda que explica el origen de un lugar o una receta?", "Una leyenda", "Explica el origen de algo del lugar con un elemento fantástico.")],
  [E("¿Qué explica una leyenda?", "El origen de un lugar", "Une el relato con el paisaje."),
   E("¿La leyenda mezcla elementos reales y fantásticos?", "Sí", "Por eso parece posible y mágica a la vez."),
   E("¿A quién le corresponde enseñar la forma tradicional de una leyenda de un pueblo originario?", "A quienes la conocen en cada comunidad", "Son quienes guardan su versión.")],
  ("Imagina que en tu barrio o escuela hay un lugar (una piedra, un árbol, un cerro, una plaza). Escribe cuatro oraciones con una leyenda inventada por ti que explique cómo apareció ese lugar. Incluye un elemento fantástico y nombra el lugar. Aclara al final: «Esta leyenda es inventada».", "En la plaza hay un árbol torcido. Dicen que una nube se cansó de volar y se quedó a descansar sobre la tierra. Al secarse, se volvió árbol. Por eso a la sombra siempre hay brisa. Esta leyenda es inventada.", ["nombra un lugar", "incluye un elemento fantástico", "explica el origen del lugar", "aclara que es inventada"], ["cuatro oraciones escritas"], ["no nombrar el lugar", "sin elementos fantásticos", "presentarla como real"], "Léela a alguien y pregúntale qué lugar explica; si lo adivina, vas bien."),
  "Mira un lugar de tu barrio y escribe una pregunta sobre cómo se formó.",
  "Escribe la misma leyenda cambiando el personaje fantástico y compara el efecto.")

LUNA = ("La luna es una moneda / que se cayó del cielo. / La busca el viento en la calle, / la busca el río en su vuelo. / "
        "Los grillos tocan campanas / en la hierba del jardín, / y la noche, muy atenta, / los escucha hasta el fin.")

L(OA3, 5,
  "Este cuaderno, lápiz y el poema escrito en esta clase. Las barras / separan los versos.",
  "Aprenderé a leer un poema, a reconocer versos, estrofas y rimas, y a ver las imágenes que crea con las palabras.",
  ["Sé leer con pausas y entonación.", "Reconozco sonidos que se repiten al final de las palabras."],
  ["Un poema es un texto escrito en versos. Cada línea se llama verso. Un grupo de versos que forman una unidad se llama estrofa. Entre una estrofa y otra suele haber un espacio.",
   "La rima es la repetición de los sonidos finales de las palabras, desde la última vocal con más fuerza. Por ejemplo, «cielo» y «vuelo» riman. Los versos que riman dan música al poema. En el poema de hoy riman cielo con vuelo y jardín con fin.",
   "Los poemas también crean imágenes, que son palabras que nos hacen ver, oír o sentir algo. Cuando el poema dice que la luna es una moneda que se cayó del cielo, vemos una moneda brillante y redonda. Al leer un poema, hay que cerrar los ojos un momento y preguntarse qué imagina uno."],
  [("verso", "cada línea de un poema"), ("estrofa", "grupo de versos que forman una unidad"), ("rima", "repetición de los sonidos finales de dos palabras"), ("imagen", "palabras que nos hacen ver, oír o sentir algo")],
  [("Contar versos y estrofas", f"Lee el poema (las barras / separan los versos): «{LUNA}». La primera mitad es una estrofa y la segunda mitad es otra. ¿Cuántos versos y estrofas hay?", ["Cuento los versos hasta la primera pausa: 4.", "La segunda parte tiene otros 4: 8 versos.", "Hay dos grupos: 2 estrofas."], "8 versos y 2 estrofas"),
   ("Encontrar la rima", "En la primera estrofa, ¿qué palabras riman: cielo con vuelo o calle con viento?", ["Miro el final de los versos 2 y 4.", "Terminan en «cielo» y «vuelo».", "Esos sonidos finales se repiten."], "Cielo y vuelo")],
  [("Contar las estrofas como si fueran versos.", "Se confunde la línea con el grupo.", "Cuenta cada línea para los versos y cada bloque para las estrofas."), ("Decir que riman palabras que solo empiezan igual.", "La rima se produce al final.", "Compara cómo terminan las palabras.")],
  ([E(f"Lee el poema: «{LUNA}» ¿Cuántos versos tiene en total?", "8", "Son cuatro versos en cada una de las dos estrofas."),
    E(f"Lee el poema: «{LUNA}» ¿Cuántas estrofas tiene?", "2", "Hay dos bloques de cuatro versos."),
    E(f"Lee el poema: «{LUNA}» ¿Con qué se compara la luna?", "Con una moneda", "El primer verso dice que la luna es una moneda.")],
   [E("¿Qué palabras riman en la segunda estrofa: jardín con fin o atenta con campanas?", "Jardín con fin", "Terminan en el mismo sonido, -ín."),
    E("¿Quiénes buscan la luna en la primera estrofa: el viento y el río o los grillos y la noche?", "El viento y el río", "Así lo dicen los versos 3 y 4."),
    E("¿Qué sonido imagina el poema en la segunda estrofa: campanas o tambores?", "Campanas", "Los grillos tocan campanas.")],
   [arith("Cada estrofa del poema tiene 4 versos. Hay 2 estrofas. ¿Cuántos versos tiene el poema?", "4+4", "Se suman los versos de las dos estrofas."),
    E("¿Qué imagen te hace ver el verso «La luna es una moneda»: algo redondo y brillante o algo cuadrado y oscuro?", "Algo redondo y brillante", "La luna llena se parece a una moneda."),
    E(f"Lee: «{LUNA}» ¿Quién escucha a los grillos hasta el final?", "La noche", "El texto dice que la noche los escucha hasta el fin.")],
   [E("¿Qué parte del poema nos hace oír algo: «Los grillos tocan campanas» o «La busca el viento en la calle»?", "«Los grillos tocan campanas»", "El verso menciona un sonido: las campanas."),
    E("¿Por qué el poema dice que la noche «muy atenta» escucha: (a) para mostrar que hay silencio o (b) porque la noche tiene orejas?", "(a)", "El poeta usa una imagen para mostrar que todo se queda en silencio.")],
   [E("¿Cuántos versos del poema riman al final con otro verso? Cuenta los versos 2 y 4 de cada estrofa.", "4", "Dos versos riman en la primera estrofa y otros dos en la segunda."),
    E("Si agregáramos una tercera estrofa de cuatro versos, ¿cuántos versos tendría el poema?", "12", "Ocho versos más cuatro son doce.")]),
  [E("Quieres leer el poema a tu curso. ¿Conviene hacer una pausa más larga entre estrofas o entre cada palabra?", "Entre estrofas", "Así se muestra dónde termina una unidad.")],
  [E("¿Cómo se llama cada línea de un poema?", "Verso", "Es la unidad de línea."),
   E("¿Cómo se llama un grupo de versos?", "Estrofa", "Reúne varios versos en una unidad."),
   E("¿Qué es la rima?", "Repetición de sonidos finales", "Se produce al final de los versos.")],
  (f"Lee en voz alta el poema de la luna: «{LUNA}» Luego haz esto en tu cuaderno: 1) copia el verso que más te gustó; 2) escribe qué imagen te hizo ver; 3) dibuja esa imagen; 4) escribe dos palabras que riman en el poema.", "1) «Los grillos tocan campanas». 2) Vi un jardín oscuro con grillos tocando campanitas. 3) Dibujo del jardín. 4) Cielo y vuelo.", ["copia un verso del poema", "explica la imagen que vio", "dibuja la imagen", "señala dos palabras que riman"], ["verso copiado", "dibujo", "dos palabras con rima"], ["copiar algo que no está en el poema", "elegir palabras que no riman"], "Compara tu dibujo con el de otra persona: ¿ven lo mismo?"),
  "Lee en voz alta el poema a otra persona y pídele que cierre los ojos y te diga qué imagina.",
  "Escribe dos versos que rimen sobre el sol o la lluvia.")

VINETAS = ("Viñeta 1: un niño bajo la lluvia, junto a un perro mojado. El niño dice: «¡Qué lluvia!». "
           "Viñeta 2: el niño abre un paraguas grande. Dice: «Ven, Pipo». "
           "Viñeta 3: el perro se sacude y salpica al niño. Se lee «¡PLAF!». El niño dice: «¡Ay!». "
           "Viñeta 4: los dos, empapados, se ríen. El niño dice: «¡Igual nos mojamos!».")

L(OA3, 6,
  "Este cuaderno, lápiz y la historieta descrita en esta clase. Puedes dibujar las viñetas en un papel dividido en cuatro cuadros.",
  "Aprenderé a leer una historieta, ordenando las viñetas, entendiendo lo que dicen los globos y lo que muestran los dibujos.",
  ["Sé seguir la secuencia de una historia.", "Entiendo lo que dice un diálogo."],
  ["Una historieta cuenta una historia con dibujos y palabras. Cada cuadro se llama viñeta. Se leen de izquierda a derecha y de arriba abajo. Cada viñeta muestra un momento de la historia.",
   "Lo que dicen los personajes va en globos de diálogo. Los sonidos se escriben como onomatopeyas, por ejemplo «¡PLAF!» o «¡PUM!». El dibujo también cuenta: puede mostrar cómo se sienten los personajes, dónde están y qué hacen, aunque no lo diga el texto.",
   "Para entender una historieta hay que unir las viñetas en orden. Primero pasa algo, luego algo cambia y al final hay un cierre. Si alteras el orden de las viñetas, la historia pierde sentido."],
  [("viñeta", "cada cuadro de una historieta"), ("globo de diálogo", "espacio donde se escribe lo que dice un personaje"), ("onomatopeya", "palabra que imita un sonido"), ("secuencia", "orden en que ocurren los hechos")],
  [("Leer la secuencia", f"Lee la historieta descrita: «{VINETAS}» ¿Qué pasa en la viñeta 3?", ["Busco la tercera viñeta.", "El perro se sacude y salpica al niño.", "Hay una onomatopeya: ¡PLAF!."], "El perro se sacude y salpica al niño"),
   ("Entender lo que dice el dibujo", "En la viñeta 4, los dos están empapados y se ríen. ¿Cómo se sienten?", ["El dibujo muestra que se ríen.", "Se ríen aunque están mojados.", "Se sienten contentos."], "Contentos")],
  [("Leer las viñetas en desorden.", "No se sigue el orden de la historieta.", "Lee de izquierda a derecha y de arriba abajo."), ("Pensar que la historieta solo cuenta con el texto.", "Se ignora el dibujo.", "Mira también lo que muestra el dibujo.")],
  ([E(f"Lee la historieta descrita: «{VINETAS}» ¿Cuántas viñetas tiene?", "4", "Están numeradas del 1 al 4."),
    E(f"Lee la historieta descrita: «{VINETAS}» ¿Cómo se llama el perro?", "Pipo", "El niño dice «Ven, Pipo»."),
    E(f"Lee la historieta descrita: «{VINETAS}» ¿Qué abre el niño en la viñeta 2?", "Un paraguas grande", "Así dice la viñeta 2.")],
   [E("En Lenguaje: ¿Qué es una viñeta?", "Cada cuadro de una historieta", "Cada cuadro muestra un momento."),
    E("«¡PLAF!» imita un sonido. ¿Cómo se llama ese tipo de palabra?", "Onomatopeya", "Es una palabra que imita un sonido."),
    E("¿Dónde se escribe lo que dice un personaje: en un globo de diálogo o en el título?", "En un globo de diálogo", "El globo contiene sus palabras.")],
   [E(f"Lee la historieta descrita: «{VINETAS}» ¿Qué hace el perro en la viñeta 3?", "Se sacude y salpica al niño", "Eso muestra el dibujo."),
    E(f"Lee la historieta descrita: «{VINETAS}» ¿Qué dice el niño al final?", "«¡Igual nos mojamos!»", "Es lo que dice en la viñeta 4."),
    E("Ordena estas viñetas con números: (a) los dos se ríen, (b) el niño abre el paraguas, (c) el perro salpica al niño, (d) llueve y el perro está mojado.", "d, b, c, a", "Sigue el orden de las viñetas 1, 2, 3 y 4.")],
   [E("En la viñeta 3, el niño dice «¡Ay!» y se escucha «¡PLAF!». ¿Qué ocurrió: el perro se sacudió o el niño se cayó?", "El perro se sacudió", "La viñeta 3 muestra que el perro salpicó al niño."),
    E(f"Lee la historieta descrita: «{VINETAS}» Al final, ¿el paraguas evitó que se mojaran? Responde sí o no.", "No", "En la viñeta 4 están empapados y el niño dice «¡Igual nos mojamos!».")],
   [E("¿Cuántos globos de diálogo del niño hay en total en las cuatro viñetas?", "4", "El niño habla en cada viñeta: «¡Qué lluvia!», «Ven, Pipo», «¡Ay!» y «¡Igual nos mojamos!»."),
    E("Si cambias el orden y lees primero la viñeta 4, ¿se entiende bien por qué están empapados?", "No", "Falta ver antes qué pasó.")]),
  [E("En una historieta de una revista infantil aparece «¡PUM!» sobre un dibujo de una puerta cerrándose. ¿Qué te dice «¡PUM!»?", "El sonido de un golpe fuerte", "Imita el ruido de la puerta.")],
  [E("En Lenguaje: ¿En qué orden se leen las viñetas?", "De izquierda a derecha y de arriba abajo", "Es el orden de lectura."),
   E("¿Para qué sirven los globos?", "Para mostrar lo que dicen los personajes", "Contienen sus palabras."),
   E("¿Qué cuenta además del texto: el dibujo o nada?", "El dibujo", "Muestra acciones y sentimientos.")],
  ("Dibuja en tu cuaderno una historieta de cuatro viñetas. Usa esta idea: una niña planta una semilla, la riega, espera y sale una flor. Incluye al menos un globo de diálogo y una onomatopeya (por ejemplo, ¡PLOP! o ¡SPLASH!). Numera las viñetas.", "V1: una niña con una semilla («¡Hola, semilla!»). V2: la riega (¡SPLASH!). V3: espera con un reloj. V4: sale una flor («¡Qué linda!»).", ["cuatro viñetas numeradas", "secuencia con sentido", "un globo de diálogo", "una onomatopeya"], ["historieta dibujada"], ["viñetas desordenadas", "no usar globos ni onomatopeyas"], "Pide a otra persona que lea tu historieta sin explicarle nada y mira si entiende la secuencia."),
  "Mira una historieta de una revista y cuenta cuántas viñetas tiene y qué onomatopeyas usa.",
  "Cambia el final de la historieta del perro Pipo en una nueva viñeta.")

# ------------------------------------------------------------------ OA 04
CAMILA = ("Camila llegó a casa con los zapatos llenos de barro. Dejó el paraguas cerrado junto a la puerta y se sacó el abrigo mojado. "
          "Sus botas de agua estaban en la entrada, secas. Camila miró el cielo por la ventana y suspiró.")

L(OA4, 1,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a distinguir lo que el texto dice con todas sus letras (información explícita) de lo que puedo deducir con pistas (información implícita).",
  ["Sé encontrar datos escritos en un texto.", "Sé releer para buscar pistas."],
  ["En un texto hay información explícita, que está escrita tal cual. Por ejemplo, «Camila llegó con los zapatos llenos de barro» está dicho directamente. Para encontrarla basta con buscar la oración que lo dice.",
   "También hay información implícita, que no está escrita pero se puede deducir con pistas. Eso se llama inferir. Si el texto dice que Camila se sacó el abrigo mojado, podemos inferir que había llovido, aunque no lo diga.",
   "Una buena inferencia siempre se apoya en una pista del texto y en lo que sabes del mundo. Por eso, cuando infieras, di siempre «Porque el texto dice…». Si no hay ninguna pista, no es una inferencia sino una invención."],
  [("explícito", "que está escrito directamente en el texto"), ("implícito", "que no está escrito, pero se puede deducir"), ("inferir", "deducir algo a partir de pistas"), ("pista", "dato del texto que ayuda a deducir")],
  [("Información explícita", f"Lee: «{CAMILA}» ¿Dónde dejó Camila el paraguas?", ["Busco la palabra paraguas.", "La oración dice «junto a la puerta».", "Está escrito directamente."], "Junto a la puerta"),
   ("Información implícita", f"Con el mismo texto, ¿había llovido?", ["El texto no dice «llovió».", "Dice que el abrigo estaba mojado y los zapatos con barro.", "Con esas pistas, puedo inferir que sí."], "Sí, porque el abrigo estaba mojado y había barro")],
  [("Responder una inferencia sin mostrar la pista.", "Se cree que basta con adivinar.", "Agrega «porque el texto dice…»."), ("Inventar un dato que no tiene pista.", "Se mezcla la imaginación con la inferencia.", "Pregunta qué parte del texto apoya tu idea.")],
  ([E(f"Lee: «{CAMILA}» ¿Qué tenía llenos de barro Camila al llegar a casa?", "Los zapatos", "El texto lo dice al comienzo."),
    E(f"Lee: «{CAMILA}» ¿Dónde estaban las botas de agua?", "En la entrada", "El texto dice «Sus botas de agua estaban en la entrada»."),
    E(f"Lee: «{CAMILA}» ¿Qué hizo Camila al final?", "Miró el cielo por la ventana y suspiró", "Es la última oración del texto.")],
   [E("¿Cómo se llama la información que está escrita directamente en el texto?", "Explícita", "Se encuentra tal cual en el texto."),
    E("¿Cómo se llama deducir algo con pistas?", "Inferir", "Se pasa de pistas a una conclusión."),
    E(f"Lee: «{CAMILA}» El texto dice «el abrigo mojado». Que el abrigo estaba mojado, ¿es información explícita o implícita?", "Explícita", "La frase «abrigo mojado» está escrita.")],
   [E(f"Lee: «{CAMILA}» ¿Había llovido? Responde con la pista: sí, porque…", "Sí, porque el abrigo estaba mojado y había barro", "Las pistas apoyan la inferencia."),
    E(f"Lee: «{CAMILA}» ¿Camila usó sus botas de agua? Responde sí o no.", "No", "Estaban secas en la entrada."),
    E(f"Lee: «{CAMILA}» ¿Camila usó el paraguas? Responde sí, no o no se puede saber.", "No se puede saber", "El texto dice que lo dejó cerrado, pero no si lo usó.")],
   [E(f"Lee: «{CAMILA}» El texto dice que Camila suspiró al mirar el cielo. ¿Qué pista da sobre cómo se sentía: (a) quizá estaba cansada o preocupada por la lluvia o (b) estaba bailando?", "(a)", "Suspirar suele expresar cansancio o preocupación."),
    E(f"Lee: «{CAMILA}» Alguien dice «Camila vive lejos del colegio». ¿Es explícito, implícito o inventado?", "Inventado", "El texto no da ninguna pista de eso.")],
   [E(f"Lee: «{CAMILA}» ¿Cuántos datos explícitos hay en la primera oración? Cuenta: llegó a casa y tenía zapatos con barro.", "2", "Son dos datos escritos."),
    E(f"Lee: «{CAMILA}» ¿Cuántas pistas apoyan que había llovido: abrigo mojado, barro en los zapatos y botas secas?", "2", "Abrigo mojado y barro apoyan la lluvia; las botas secas solo indican que no las usó.")]),
  [E("Un cartel de la escuela dice: «Hoy, los alumnos entran por la puerta lateral». ¿Qué está dicho de forma explícita?", "Que los alumnos entran por la puerta lateral", "Es lo que se lee en el cartel.")],
  [E("¿La información explícita está escrita en el texto o hay que deducirla?", "Está escrita en el texto", "Es el significado de explícita."),
   E("¿Qué se necesita para inferir bien: una pista o una invención?", "Una pista", "Toda inferencia se apoya en una pista."),
   E("Si el texto dice «Tomás llegó con paraguas mojado», ¿se puede inferir que había llovido?", "Sí", "El paraguas mojado es una pista de lluvia.")],
  (f"Lee el texto: «{CAMILA}» Escribe: 1) un dato explícito, 2) una inferencia con su pista («porque el texto dice…»), 3) algo que NO se puede saber con ese texto.", "1) Camila dejó el paraguas junto a la puerta. 2) Había llovido, porque el abrigo estaba mojado. 3) No sabemos cuántos años tiene Camila.", ["dato explícito correcto", "inferencia apoyada en pista", "reconoce algo que no se puede saber"], ["tres respuestas escritas"], ["inferir sin pista", "dar una invención como inferencia"], "Marca en el texto la pista que usaste y revísala con otra persona."),
  "Lee un párrafo de un cuento y escribe una cosa explícita y otra que se infiera.",
  "Escribe un texto de tres oraciones que permita inferir qué estación del año es sin decirla.")

SARA = ("Sara quería ver las estrellas. Como había nubes, esperó a que se despejara. Mientras esperaba, preparó un jugo. "
        "Cuando el cielo se despejó, salió al patio con una frazada. Vio tantas estrellas que no quiso entrar hasta la medianoche.")

L(OA4, 2,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a reconstruir la secuencia de acciones de un cuento y a explicar por qué ocurrió cada hecho (causa y consecuencia).",
  ["Sé distinguir el principio, el medio y el final.", "Sé qué es una inferencia."],
  ["La secuencia es el orden en que ocurren los hechos de una narración. Para reconstruirla, busca palabras que indiquen orden, como «primero», «luego», «mientras», «cuando» y «al final», y pregúntate qué pasó antes y qué pasó después.",
   "Los hechos de un cuento suelen estar unidos por causa y consecuencia. La causa es el motivo por el que algo ocurre. La consecuencia es lo que pasa por esa causa. En el texto de Sara, había nubes (causa) y por eso Sara esperó (consecuencia).",
   "Palabras como «porque», «como», «por eso» y «entonces» ayudan a descubrir la relación. A veces la causa no está escrita y hay que inferirla. Pregúntate siempre: ¿por qué pasó esto?"],
  [("secuencia", "orden en que ocurren los hechos"), ("causa", "motivo por el que ocurre algo"), ("consecuencia", "lo que ocurre por una causa"), ("conector", "palabra que une ideas, como «porque» o «entonces»")],
  [("Ordenar los hechos", f"Lee: «{SARA}» Ordena: (a) salió al patio, (b) preparó un jugo, (c) esperó a que se despejara.", ["Primero esperó porque había nubes.", "Mientras esperaba, preparó el jugo.", "Cuando se despejó, salió al patio."], "c, b, a"),
   ("Causa y consecuencia", "¿Por qué esperó Sara?", ["Busco la palabra «como» o «porque».", "Dice «Como había nubes, esperó».", "La causa son las nubes."], "Porque había nubes")],
  [("Contar los hechos en cualquier orden.", "No se fija en las palabras de orden.", "Subraya palabras como primero, mientras y cuando."), ("Confundir causa con consecuencia.", "Se invierte la relación.", "Pregunta ¿qué pasó primero y qué pasó por eso?")],
  ([E(f"Lee: «{SARA}» ¿Qué quería ver Sara?", "Las estrellas", "El texto dice «Sara quería ver las estrellas»."),
    E(f"Lee: «{SARA}» ¿Con qué salió Sara al patio?", "Con una frazada", "Así lo dice el texto."),
    E(f"Lee: «{SARA}» ¿Hasta cuándo no quiso entrar?", "Hasta la medianoche", "Lo dice la última oración.")],
   [E("¿Cómo se llama el orden en que ocurren los hechos?", "Secuencia", "Es el orden de la historia."),
    E(f"Lee: «{SARA}» ¿Qué hizo Sara mientras esperaba?", "Preparó un jugo", "El texto lo dice con «Mientras esperaba»."),
    E("¿Qué palabra marca la causa en «Como había nubes, esperó»?", "Como", "Introduce el motivo.")],
   [E(f"Lee: «{SARA}» ¿Qué ocurrió primero: preparó un jugo o salió al patio?", "Preparó un jugo", "Lo hizo mientras esperaba, antes de salir."),
    E(f"Lee: «{SARA}» ¿Por qué no quiso entrar hasta la medianoche?", "Porque había tantas estrellas", "El texto dice que vio tantas estrellas que no quiso entrar."),
    E(f"Lee: «{SARA}» Ordena con letras: (a) salió al patio, (b) esperó, (c) vio muchas estrellas.", "b, a, c", "Primero esperó, luego salió y después vio las estrellas.")],
   [E("¿Cuál es la consecuencia de que hubiera nubes: que Sara esperó o que Sara se fue a dormir?", "Que Sara esperó", "El texto dice «Como había nubes, esperó»."),
    E("¿Qué causa tiene que Sara no quisiera entrar: el frío o ver muchas estrellas?", "Ver muchas estrellas", "El texto lo une con «tantas… que».")],
   [E(f"Lee: «{SARA}» Cuenta cuántas acciones de Sara aparecen en orden: quería ver, esperó, preparó, salió, vio.", "5", "Son cinco acciones seguidas."),
    E("Si Sara hubiera salido antes de que se despejara el cielo, ¿habría visto estrellas? Responde con la causa.", "No, porque había nubes", "Las nubes tapaban el cielo.")]),
  [E("Una receta dice: «Primero mezcla la harina. Luego agrega el huevo. Al final, hornea». ¿Qué paso va en segundo lugar?", "Agregar el huevo", "La receta lo ubica con «Luego».")],
  [E("¿Qué palabras indican orden: «primero», «luego», «al final» o «rojo», «grande», «bonito»?", "Primero, luego, al final", "Estas palabras marcan la secuencia."),
   E("¿La causa es el motivo o lo que pasa después?", "El motivo", "La consecuencia es lo que pasa después."),
   E("En «Llovió, por eso saltó en los charcos», ¿cuál es la consecuencia?", "Saltó en los charcos", "Es lo que pasó por la lluvia.")],
  (f"Lee el texto: «{SARA}» Escribe: 1) los hechos en orden, con números; 2) una causa y su consecuencia; 3) qué habría pasado si el cielo no se hubiese despejado esa noche.", "1) Quería ver estrellas. 2) Esperó. 3) Preparó un jugo. 4) Salió. 5) Vio estrellas. Causa: había nubes; consecuencia: esperó. Si no se despejaba, no habría visto estrellas.", ["ordena correctamente", "relaciona causa y consecuencia", "propone una hipótesis coherente"], ["lista numerada", "dos frases sobre causa y consecuencia"], ["cambiar el orden", "invertir causa y consecuencia"], "Verifica tu orden volviendo a leer el texto con tus números."),
  "Cuenta con tus palabras lo que hiciste ayer de la mañana a la noche, usando primero, luego y al final.",
  "Escribe un texto de tres oraciones con una causa y una consecuencia y marca los conectores.")

ISMAEL = ("Don Ismael prestó su martillo al vecino y no se lo pidió de vuelta. Cuando el vecino lo devolvió roto, Ismael dijo: —No importa, lo arreglaré. "
          "Esa tarde, sin que nadie se lo pidiera, ayudó a levantar la reja del vecino que el viento había botado.")

L(OA4, 3,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a describir cómo es un personaje usando lo que hace y lo que dice, y a apoyar mi descripción en evidencia del texto.",
  ["Sé quién es el personaje principal de un cuento.", "Sé inferir con pistas."],
  ["Los personajes se conocen por lo que hacen, lo que dicen y lo que piensan. Un narrador no siempre dice «es generoso» o «es valiente». Muchas veces solo cuenta lo que hizo y el lector lo deduce.",
   "Una característica de un personaje es una cualidad: generoso, paciente, curioso, mentiroso. Para describirla, busca una acción o una frase del texto que la muestre. Por ejemplo, si don Ismael dice «No importa, lo arreglaré» cuando su martillo se rompe, muestra paciencia.",
   "Una buena descripción tiene dos partes: la característica y la evidencia. Se puede decir: «Don Ismael es solidario, porque ayudó a levantar la reja del vecino sin que se lo pidieran». Sin evidencia, es solo una opinión sin respaldo."],
  [("personaje", "quien participa en la historia"), ("característica", "cualidad que describe cómo es alguien"), ("evidencia", "dato del texto que apoya una idea"), ("solidario", "que ayuda a otros sin que se lo pidan")],
  [("Característica con evidencia", f"Lee: «{ISMAEL}» ¿Cómo es don Ismael y qué lo muestra?", ["Busco lo que hace.", "Prestó el martillo, no se enojó y ayudó con la reja.", "Eso muestra que es generoso y solidario."], "Es solidario, porque ayudó con la reja sin que se lo pidieran"),
   ("Distinguir evidencia de opinión", "«Don Ismael es antipático.» ¿Hay evidencia en el texto?", ["Busco una acción antipática.", "El texto no muestra ninguna.", "No hay evidencia."], "No, el texto muestra lo contrario")],
  [("Decir cómo es un personaje sin mostrar lo que hizo.", "Se opina sin buscar pruebas.", "Agrega «porque» y una acción del texto."), ("Usar una acción que no corresponde a la característica.", "No se compara acción y cualidad.", "Pregunta ¿esta acción muestra esa cualidad?")],
  ([E(f"Lee: «{ISMAEL}» ¿A quién prestó don Ismael su martillo?", "Al vecino", "El texto lo dice en la primera oración."),
    E(f"Lee: «{ISMAEL}» ¿Cómo estaba el martillo cuando lo devolvieron?", "Roto", "El texto dice que el vecino lo devolvió roto."),
    E(f"Lee: «{ISMAEL}» ¿Qué había botado el viento?", "La reja del vecino", "Así lo dice la última oración.")],
   [E("¿Qué es una característica de un personaje?", "Una cualidad que dice cómo es", "Por ejemplo, ser generoso o paciente."),
    E("¿Cómo se llama el dato del texto que apoya una idea?", "Evidencia", "Es la prueba de lo que decimos."),
    E(f"Lee: «{ISMAEL}» Ismael dijo «No importa, lo arreglaré». ¿Eso muestra que es paciente o apurado?", "Paciente", "No se enojó con el vecino.")],
   [E(f"Lee: «{ISMAEL}» ¿Qué hizo don Ismael cuando el vecino devolvió el martillo roto?", "Dijo que no importaba y que lo arreglaría", "Es lo que dice en el texto."),
    E(f"Lee: «{ISMAEL}» ¿Qué hecho muestra que don Ismael es solidario: ayudar a levantar la reja o prestar el martillo?", "Ayudar a levantar la reja", "Lo hizo sin que nadie se lo pidiera."),
    E(f"Lee: «{ISMAEL}» ¿Qué evidencia apoya «Don Ismael es paciente»: (a) dijo que no importaba cuando el martillo volvió roto o (b) ayudó a levantar la reja?", "(a)", "Esa acción muestra que no se enojó.")],
   [E(f"Lee: «{ISMAEL}» Alguien dice «Don Ismael es enojón». ¿Se apoya en el texto?", "No", "El texto muestra que no se enojó."),
    E(f"Lee: «{ISMAEL}» ¿Qué característica muestra más que prestó el martillo: generosidad o miedo?", "Generosidad", "Prestar es compartir lo propio.")],
   [E(f"Lee: «{ISMAEL}» El texto tiene tres oraciones. ¿En cuántas de ellas don Ismael hace algo amable?", "3", "En la primera presta el martillo, en la segunda dice que lo arreglará y en la tercera ayuda con la reja."),
    E("Si un personaje devuelve una billetera que encontró, ¿qué característica muestra: honestidad o egoísmo?", "Honestidad", "Devolver lo que no es suyo muestra honestidad.")]),
  [E("En tu curso, una compañera presta su lápiz y comparte su colación sin que se la pidan. ¿Qué característica muestra: solidaria o egoísta?", "Solidaria", "Ayuda sin que se lo pidan.")],
  [E("¿Cómo se conocen los personajes en un cuento?", "Por lo que hacen y dicen", "Esas acciones muestran cómo son."),
   E("¿Qué debe acompañar a una característica: una evidencia o una invención?", "Una evidencia", "Toda descripción necesita prueba."),
   E("Si un personaje ayuda sin que se lo pidan, ¿es solidario o descuidado?", "Solidario", "Ayudar sin que lo pidan muestra solidaridad.")],
  ("Elige uno de estos personajes y escribe tres oraciones. Opción 1: Mara, una niña que devuelve una billetera que se encontró en la calle. Opción 2: Joaquín, un niño que se burla de un compañero que se cayó. Escribe una característica, la evidencia («porque…») y si te gustaría ser como ese personaje.", "Mara es honesta, porque devuelve la billetera que se encontró. Me gustaría ser como ella porque hizo lo correcto.", ["dice una característica", "da una evidencia con porque", "da una opinión relacionada"], ["tres oraciones"], ["describir sin evidencia", "dar una evidencia que no corresponde"], "Pide a otra persona que diga si tu evidencia muestra la característica."),
  "Describe a un personaje de tu cuento favorito con una característica y una evidencia.",
  "Escribe una historia de tres oraciones donde un personaje muestre ser valiente sin decir la palabra valiente.")

NOCHE = ("Era una noche sin luna en el bosque. El viento movía las ramas y las hojas crujían. Pablo caminaba despacio, apretando la linterna. "
         "Cada sombra le parecía un animal. Cuando por fin vio la luz de su casa, echó a correr.")

L(OA4, 4,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a describir el ambiente de una narración (lugar y momento) y a explicar cómo influye en lo que hacen o sienten los personajes.",
  ["Reconozco dónde y cuándo ocurre una historia.", "Describo personajes con evidencia."],
  ["El ambiente es el lugar y el momento en que ocurre la historia, y también el clima o la sensación que se percibe, como silencio, frío o peligro. Para descubrirlo, busca palabras que digan dónde y cuándo.",
   "El ambiente influye en los personajes. En el texto del bosque, la noche sin luna, el viento y las sombras hacen que Pablo camine despacio y se asuste. Si la misma escena fuera en una plaza a mediodía, Pablo no se comportaría igual.",
   "Para explicar el efecto del ambiente, usa esta fórmula: «En… (ambiente), el personaje… (acción) porque…». Esto muestra que el ambiente no es un adorno: cambia lo que pasa y lo que sienten los personajes."],
  [("ambiente", "lugar, momento y sensación en que ocurre la historia"), ("lugar", "sitio donde pasa la acción"), ("momento", "cuándo ocurre la acción"), ("sombra", "zona oscura que se forma cuando algo tapa la luz")],
  [("Describir el ambiente", f"Lee: «{NOCHE}» ¿Cuál es el ambiente?", ["Busco el lugar: el bosque.", "Busco el momento: una noche sin luna.", "Hay viento y hojas que crujen."], "Un bosque de noche, sin luna, con viento"),
   ("Efecto del ambiente", "¿Por qué Pablo caminaba despacio y apretaba la linterna?", ["El ambiente es oscuro.", "Cada sombra le parecía un animal.", "Por eso tenía miedo."], "Por el miedo que le daba la noche en el bosque")],
  [("Decir solo el lugar y olvidar el momento y la sensación.", "Se mira solo una parte.", "Busca dónde, cuándo y cómo se siente."), ("Pensar que el ambiente no afecta al personaje.", "Se lee el ambiente como adorno.", "Pregunta qué hace o siente el personaje por ese ambiente.")],
  ([E(f"Lee: «{NOCHE}» ¿Dónde ocurre la historia?", "En un bosque", "El texto dice «en el bosque»."),
    E(f"Lee: «{NOCHE}» ¿Cuándo ocurre la historia?", "De noche", "Dice que era una noche sin luna."),
    E(f"Lee: «{NOCHE}» ¿Qué apretaba Pablo en la mano?", "La linterna", "El texto lo dice en la tercera oración.")],
   [E("¿Qué incluye el ambiente: el lugar y el momento o solo los nombres de los personajes?", "El lugar y el momento", "Y también la sensación del lugar."),
    E(f"Lee: «{NOCHE}» ¿Qué se oía en el bosque: hojas que crujían o música?", "Hojas que crujían", "El texto lo dice."),
    E(f"Lee: «{NOCHE}» ¿Había luna esa noche?", "No", "El texto dice «sin luna».")],
   [E(f"Lee: «{NOCHE}» ¿Por qué Pablo caminaba despacio?", "Porque tenía miedo en la oscuridad", "Cada sombra le parecía un animal."),
    E(f"Lee: «{NOCHE}» ¿Qué hizo Pablo cuando vio la luz de su casa?", "Echó a correr", "Es lo que dice la última oración."),
    E(f"Lee: «{NOCHE}» ¿Qué le parecía cada sombra a Pablo?", "Un animal", "Lo dice el texto.")],
   [E("Si la misma escena ocurriera en una plaza con sol a mediodía, ¿Pablo tendría el mismo miedo: sí o no?", "No", "El ambiente de la plaza con sol no asusta."),
    E(f"Lee: «{NOCHE}» ¿Qué parte del ambiente hace pensar que hay peligro: el viento y las sombras o la casa?", "El viento y las sombras", "Son los elementos que asustan a Pablo.")],
   [E(f"Lee: «{NOCHE}» ¿En cuántas de estas frases del texto se habla del ambiente? 1) «Era una noche sin luna en el bosque.» 2) «Pablo caminaba despacio, apretando la linterna.» 3) «El viento movía las ramas y las hojas crujían.»", "2", "Las frases 1 y 3 describen el lugar y el momento; la 2 cuenta lo que hace Pablo."),
    E("¿Cuál completa bien «En un bosque oscuro, Pablo camina despacio porque…»: (a) tiene miedo de las sombras o (b) quiere bailar?", "(a)", "Es el efecto del ambiente en el personaje.")]),
  [E("Un cartel de la escuela dice: «Hoy el patio está resbaloso por la lluvia». ¿Qué debes hacer al caminar: correr o caminar con cuidado?", "Caminar con cuidado", "El ambiente del patio mojado cambia lo que conviene hacer.")],
  [E("¿Qué dos cosas dice el ambiente de una historia?", "Dónde y cuándo ocurre", "El lugar y el momento."),
   E("¿Puede el ambiente cambiar lo que sienten los personajes?", "Sí", "Una noche oscura puede dar miedo."),
   E("¿Qué fórmula usas para explicar el efecto del ambiente?", "En… el personaje… porque…", "Une ambiente, acción y razón.")],
  (f"Lee el texto: «{NOCHE}» Haz tres cosas: 1) escribe el ambiente en una oración; 2) explica con «porque» cómo influyó en Pablo; 3) cambia el ambiente a una plaza soleada y escribe una oración sobre cómo habría caminado Pablo.", "1) Era una noche sin luna en el bosque, con viento. 2) Pablo caminaba despacio porque tenía miedo. 3) En una plaza soleada, Pablo habría caminado tranquilo y sin apretar la linterna.", ["describe lugar, momento y sensación", "explica el efecto", "propone un cambio coherente"], ["tres oraciones"], ["describir solo el lugar", "no explicar el efecto"], "Revisa si tu tercera oración muestra un cambio real respecto de la segunda."),
  "Mira por la ventana o recuerda un lugar y escribe tres palabras que describan su ambiente.",
  "Escribe una escena de tres oraciones en una playa por la tarde y señala cómo afecta el ambiente al personaje.")

LUCIA = ("En el recreo, Lucía vio que a Tomás se le cayeron las galletas al suelo. Varios compañeros se rieron. "
         "Lucía fue hasta él y le ofreció la mitad de las suyas. Tomás sonrió y se las comieron juntos.")

L(OA4, 5,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a dar una opinión sobre lo que pasa en una narración y a fundamentarla con datos del texto.",
  ["Sé encontrar información explícita.", "Sé describir personajes con evidencia."],
  ["Una opinión es lo que tú piensas sobre algo. Puede ser que te parezca bien o mal que un personaje haga algo. Una opinión fundamentada es la que explica por qué, usando datos del texto.",
   "Compara dos opiniones sobre Lucía. La primera: «Lucía hizo bien». La segunda: «Lucía hizo bien porque compartió sus galletas con Tomás cuando otros se rieron de él». La segunda es mejor porque tiene una razón que se puede comprobar en el texto.",
   "Una opinión fundamentada tiene tres partes: lo que piensas, la palabra «porque» y un dato del texto. También puedes agregar lo que tú sabes, por ejemplo: «Es amable ayudar a quien lo pasa mal». Otra persona puede pensar distinto, pero debe dar razones."],
  [("opinión", "lo que pienso sobre algo"), ("fundamentar", "dar razones para apoyar una idea"), ("dato", "información concreta del texto"), ("razón", "motivo que explica por qué pienso algo")],
  [("Opinión con razón", f"Lee: «{LUCIA}» ¿Cuál opinión es mejor: «Lucía hizo bien» o «Lucía hizo bien porque compartió sus galletas con Tomás»?", ["La primera no da razón.", "La segunda dice porque y un dato.", "La segunda es una opinión fundamentada."], "La segunda"),
   ("Razón que viene del texto", "Para apoyar «Los compañeros hicieron mal», ¿qué dato del texto sirve: «Varios compañeros se rieron» o «Lucía tenía galletas»?", ["Busco qué hicieron los compañeros.", "Se rieron de Tomás.", "Ese dato apoya la opinión."], "«Varios compañeros se rieron»")],
  [("Dar una opinión sin ninguna razón.", "Se cree que basta con decir lo que se piensa.", "Agrega «porque» y un dato del texto."), ("Usar un dato que no apoya la opinión.", "No se revisa si el dato corresponde.", "Pregunta si el dato prueba lo que dices.")],
  ([E(f"Lee: «{LUCIA}» ¿Qué se le cayó a Tomás?", "Las galletas", "El texto lo dice en la primera oración."),
    E(f"Lee: «{LUCIA}» ¿Qué hicieron varios compañeros?", "Se rieron", "Así dice la segunda oración."),
    E(f"Lee: «{LUCIA}» ¿Qué le ofreció Lucía a Tomás?", "La mitad de sus galletas", "Es lo que dice la tercera oración.")],
   [E("¿Qué es una opinión fundamentada?", "Una opinión con razones del texto", "Explica por qué se piensa algo."),
    E("¿Qué palabra introduce una razón: «porque» o «también»?", "Porque", "Se usa para dar el motivo."),
    E(f"Lee: «{LUCIA}» «Lucía fue amable.» ¿Es una opinión o un dato explícito?", "Una opinión", "El texto no usa la palabra amable; es una valoración.")],
   [E(f"Lee: «{LUCIA}» Elige el dato que apoya «Lucía fue amable»: «le ofreció la mitad de sus galletas» o «vio que se cayeron las galletas».", "Le ofreció la mitad de sus galletas", "Compartir muestra amabilidad."),
    E(f"Lee: «{LUCIA}» Elige el dato que apoya «A Tomás le dolió que se rieran»: «Tomás sonrió al final» o «Varios compañeros se rieron».", "Varios compañeros se rieron", "Es el hecho que lo afectó."),
    E(f"Lee: «{LUCIA}» ¿Cómo terminó la escena: Tomás sonrió y comieron juntos, o se fue enojado?", "Tomás sonrió y comieron juntos", "Así termina el texto.")],
   [E("Dos niños opinan: Ana dice «Me parece bien lo que hizo Lucía». Beto dice «Me parece bien lo que hizo Lucía porque ayudó a Tomás cuando se burlaron de él». ¿Quién fundamenta mejor su opinión?", "Beto", "Da una razón del texto."),
    E("Un niño opina «Los compañeros hicieron bien en reírse, porque es divertido». ¿Esa razón se apoya en el texto?", "No", "El texto no dice que fuera divertido ni que a Tomás le gustara.")],
   [E(f"Lee: «{LUCIA}» ¿Qué razón apoya mejor «Lucía hizo bien»: (a) compartió sus galletas con Tomás o (b) vio lo que pasó en el recreo?", "(a)", "Compartir es la acción que ayuda a Tomás."),
    E(f"Lee: «{LUCIA}» ¿Cuántos datos del texto usa esta opinión: «Lucía hizo bien porque vio lo que pasó, fue hasta Tomás y compartió»?", "3", "Son tres hechos del texto.")]),
  [E("Un compañero se cae en el patio y varios se ríen. Tú le ofreces ayuda. ¿Qué opinión fundamentada podrías dar sobre tu acción: «Hice bien porque ayudé a quien lo necesitaba» o «Hice bien»?", "«Hice bien porque ayudé a quien lo necesitaba»", "Incluye una razón.")],
  [E("¿Una opinión sin razón está fundamentada?", "No", "Falta el porque y el dato."),
   E("¿De dónde se saca el dato para fundamentar la opinión sobre un cuento?", "Del texto", "El texto es la prueba."),
   E("¿Dos personas pueden opinar distinto si dan razones?", "Sí", "Lo importante es que expliquen por qué.")],
  (f"Lee el texto: «{LUCIA}» Escribe dos opiniones fundamentadas: una sobre lo que hizo Lucía y otra sobre lo que hicieron los compañeros. Usa «Creo que… porque…» e incluye un dato del texto en cada una.", "Creo que Lucía hizo bien porque compartió sus galletas con Tomás. Creo que los compañeros hicieron mal porque se rieron de Tomás cuando se le cayeron las galletas.", ["usa «creo que… porque…»", "incluye un dato del texto", "sus razones son comprobables"], ["dos opiniones escritas"], ["opinión sin razón", "dato que no corresponde"], "Intercambia con otra persona y comprueba si el dato del texto apoya la opinión."),
  "Piensa en un cuento que hayas leído y da una opinión sobre un hecho con una razón.",
  "Escribe una opinión que sea distinta a la de Lucía y apóyala con un dato del texto.")

IGNACIO = ("Ignacio rompió sin querer la lámpara de la sala. Se asustó y escondió los pedazos detrás del sillón. Esa noche no pudo comer. "
           "Al día siguiente le contó la verdad a su abuelo y le ofreció pagar con sus ahorros. Su abuelo le dijo que lo importante era haber dicho la verdad.")

L(OA4, 6,
  "Este cuaderno, lápiz y el texto escrito en esta clase.",
  "Aprenderé a opinar sobre los personajes reconociendo que pueden hacer cosas buenas y malas en una misma historia, y a justificar mi juicio con el texto.",
  ["Describo personajes con evidencia.", "Doy opiniones fundamentadas."],
  ["Los personajes no siempre son totalmente buenos o totalmente malos. Muchos hacen algo mal y luego algo bien. Opinar sobre ellos exige mirar las dos cosas: lo que hicieron y por qué lo hicieron.",
   "En el texto, Ignacio rompió sin querer una lámpara y escondió los pedazos. Eso no estuvo bien, porque ocultó lo que pasó. Pero al día siguiente dijo la verdad y se ofreció a pagar. Eso sí estuvo bien. Un juicio con matices dice las dos partes.",
   "Una forma de decirlo es: «Ignacio hizo mal en…, pero hizo bien en…, porque…». Los matices ayudan a ser justos. También ayuda pensar en las razones del personaje: Ignacio se asustó, y por eso escondió los pedazos."],
  [("juicio", "opinión que valora lo que hace alguien"), ("matiz", "detalle que muestra que algo no es solo bueno ni solo malo"), ("culpa", "sensación de haber hecho algo malo"), ("reparar", "arreglar un daño que se hizo")],
  [("Un juicio con dos partes", f"Lee: «{IGNACIO}» ¿Qué hizo mal y qué hizo bien Ignacio?", ["Mal: escondió los pedazos.", "Bien: contó la verdad y se ofreció a pagar.", "Mi juicio tiene las dos partes."], "Mal: escondió los pedazos. Bien: dijo la verdad y se ofreció a pagar"),
   ("Entender sus razones", "¿Por qué escondió Ignacio los pedazos?", ["Busco qué sintió.", "Dice que se asustó.", "Por miedo a las consecuencias."], "Porque se asustó")],
  [("Decir que un personaje es solo malo por un error.", "Se mira una sola acción.", "Revisa también lo bueno que hizo después."), ("Decir que todo estuvo bien porque se arrepintió.", "Se olvida el error.", "Reconoce el error y también la reparación.")],
  ([E(f"Lee: «{IGNACIO}» ¿Qué rompió Ignacio?", "La lámpara de la sala", "El texto lo dice en la primera oración."),
    E(f"Lee: «{IGNACIO}» ¿Dónde escondió los pedazos?", "Detrás del sillón", "El texto lo dice en la segunda oración."),
    E(f"Lee: «{IGNACIO}» ¿A quién le contó la verdad?", "A su abuelo", "Así lo dice el texto.")],
   [E("¿Qué es un matiz en un juicio sobre un personaje?", "Un detalle que muestra que no es solo bueno ni solo malo", "Permite ser más justo."),
    E(f"Lee: «{IGNACIO}» ¿Esconder los pedazos estuvo bien o mal?", "Mal", "Ocultó lo que había pasado."),
    E(f"Lee: «{IGNACIO}» ¿Decir la verdad al día siguiente estuvo bien o mal?", "Bien", "Reparó su error siendo honesto.")],
   [E(f"Lee: «{IGNACIO}» ¿Qué se ofreció a hacer Ignacio para arreglar el daño?", "Pagar con sus ahorros", "El texto lo dice."),
    E(f"Lee: «{IGNACIO}» ¿Qué le dijo el abuelo que era lo importante?", "Haber dicho la verdad", "Es lo que dice el final."),
    E(f"Lee: «{IGNACIO}» ¿Qué le pasó a Ignacio esa noche?", "No pudo comer", "El texto lo dice.")],
   [E(f"Lee: «{IGNACIO}» Alguien dice «Ignacio es un niño malo». ¿Considera todo lo que hizo?", "No", "Olvida que dijo la verdad y quiso reparar."),
    E(f"Lee: «{IGNACIO}» Otro dice «Ignacio no hizo nada mal». ¿Es correcto?", "No", "Escondió los pedazos, lo que estuvo mal.")],
   [E(f"Lee: «{IGNACIO}» ¿Cuál juicio tiene matices: (a) «Ignacio hizo mal en esconder los pedazos, pero hizo bien en contar la verdad» o (b) «Ignacio es malo»?", "(a)", "Reconoce el error y también la reparación."),
    E(f"Lee: «{IGNACIO}» Ignacio rompió la lámpara. ¿Lo hizo a propósito: sí o no?", "No", "El texto dice que la rompió sin querer, y eso cambia cómo lo juzgamos.")]),
  [E("Si rompes sin querer el libro de un compañero, ¿qué sería lo mejor según lo aprendido: esconderlo o decírselo y ofrecer arreglarlo?", "Decírselo y ofrecer arreglarlo", "Es lo que hace Ignacio al reparar el error.")],
  [E("¿Un personaje puede hacer algo malo y algo bueno?", "Sí", "Los personajes tienen matices."),
   E("¿Qué se debe mirar para un juicio justo: una acción o todas?", "Todas", "Así se ve el matiz."),
   E("¿Qué palabra ayuda a unir lo malo y lo bueno en un juicio: «pero» o «también»?", "Pero", "«Pero» contrasta ambas partes.")],
  (f"Lee el texto: «{IGNACIO}» Escribe un juicio de tres oraciones: la primera dice qué hizo mal; la segunda, qué hizo bien; la tercera, qué habrías hecho tú y por qué.", "Ignacio hizo mal en esconder los pedazos. Pero hizo bien en contar la verdad y ofrecerse a pagar. Yo habría dicho la verdad de inmediato porque es más tranquilo.", ["dice lo malo con datos", "dice lo bueno con datos", "explica qué haría y por qué"], ["tres oraciones"], ["juicio de una sola cara", "no usar el texto"], "Pregunta a otra persona si tu juicio es justo con Ignacio."),
  "Piensa en un personaje de tu cuento favorito y escribe una cosa buena y una mala que hizo.",
  "Escribe un cuento de tres oraciones sobre un personaje que se equivoca y luego lo repara.")
