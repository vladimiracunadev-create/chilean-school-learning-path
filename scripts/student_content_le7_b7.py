"""Cuaderno del estudiante, 7.º básico Lengua y Literatura, OA 16 (oración, sujeto y predicado al servicio de la escritura).

Todas las oraciones y los textos son originales e inventados; cada ejercicio trae escritas las oraciones que necesita.
Nota: los títulos de las clases del repositorio son específicos del eje; este cuaderno los sigue.
Criterio de este cuaderno: una oración exige un verbo conjugado; el sujeto puede estar expreso o tácito.
Quedan fuera (por no estar en el OA) las oraciones impersonales y la clasificación de complementos.
"""
from __future__ import annotations

import re

from student_lessons import arith, ex, register

def E(q, a, why, calc=None):
    """Ejercicio cerrado; en las preguntas de tres opciones (a), (b), (c) reparte la correcta entre las tres posiciones."""
    import zlib
    m = list(re.finditer(r"\(([abc])\) ", q))
    if len(m) == 3 and [x.group(1) for x in m] == ["a", "b", "c"] and a.strip() in ("(a)", "(b)", "(c)"):
        stem = q[:m[0].start()]
        raw = [q[m[0].end():m[1].start()], q[m[1].end():m[2].start()], q[m[2].end():]]
        tail = ""
        last = raw[2].rstrip()
        if last.endswith(("?", ".")) and not (last.startswith(("¿", "¡")) and last.endswith("?") and last.count("?") == last.count("¿")):
            tail = last[-1]
            last = last[:-1]
        raw = [raw[0].strip(), raw[1].strip(), last.strip()]
        opts = []
        for o in raw:
            if o.endswith(".") or (o.endswith("?") and not o.startswith("¿")):
                o = o[:-1]
            opts.append(o.strip())
        if all(opts):
            correct = "abc".index(a.strip()[1])
            want = zlib.crc32((stem + "|".join(sorted(opts))).encode("utf-8")) % 3
            order = list(range(3))
            order.remove(correct)
            order.insert(want, correct)
            new = [opts[i] for i in order]
            mapping = {"abc"[old]: "abc"[pos] for pos, old in enumerate(order)}
            q = stem + " ".join(f"({'abc'[i]}) {t}" for i, t in enumerate(new)) + tail
            a = f"({'abc'[want]})"
            why = re.sub(r"\(([abc])\)", lambda x: f"({mapping[x.group(1)]})", why)
    return ex(q, a, why, calc)


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


OA = "LE07 OA 16"

# ================================================================== clase 1
L(OA, 1,
  "Este cuaderno y un lápiz. Todas las oraciones y fragmentos están escritos en los ejercicios.",
  "Aprenderé a distinguir una oración completa de un fragmento y a completar los fragmentos para que mis textos sean claros.",
  ["Sé qué es un verbo y un sustantivo.", "Sé usar mayúscula y punto."],
  ["Una oración es un conjunto de palabras con sentido completo que tiene un verbo conjugado (un verbo con persona, número y tiempo, como «duerme» o «cantamos»). Al leerla entendemos de qué se habla y qué se dice sin quedar esperando algo más. «Llovía toda la tarde» es una oración. Una oración se escribe con mayúscula al inicio y con punto al final.",
   "Un fragmento es un grupo de palabras que se escribió como si fuera una oración, pero le falta algo. A veces no tiene verbo conjugado: «La casa del abuelo en la colina.» Otras veces comienza con una palabra como porque, cuando, que o aunque, y la idea queda dependiendo de otra: «Porque llovía toda la tarde.» Los fragmentos aparecen mucho en borradores. A veces se usan a propósito en literatura, pero en textos escolares conviene evitarlos.",
   "Para revisar, hazte dos preguntas. Primera: ¿hay un verbo conjugado? Segunda: ¿entiendo la idea sin quedar esperando algo? Si falta el verbo, se agrega. Si es una idea que depende de otra, se une a la oración que la completa: «Se quedaron en casa porque llovía toda la tarde.» Una sola palabra con verbo, como «Cantamos.», también es una oración."],
  [("oración", "grupo de palabras con verbo conjugado y sentido completo"), ("fragmento", "grupo de palabras que parece oración pero está incompleto"), ("verbo conjugado", "verbo con persona, número y tiempo"), ("sentido completo", "idea que se entiende sin quedar esperando algo"), ("unir", "completar una idea dependiente con la oración que le corresponde")],
  [("Distinguir", "¿Cuáles son oraciones? (1) «La casa del abuelo en la colina.» (2) «Llovía toda la tarde.» (3) «Porque llovía toda la tarde.» (4) «Cantamos.»",
    ["La 1 no tiene verbo conjugado: fragmento.", "La 2 tiene verbo («llovía») y sentido completo: oración.", "La 3 empieza con «porque» y deja la idea esperando: fragmento.", "La 4 tiene verbo («cantamos») y sentido completo: oración."], "Son oraciones la 2 y la 4"),
   ("Completar un fragmento", "Arregla: «Los estudiantes del 7.º B en el patio.»",
    ["Le falta un verbo conjugado.", "Agrego uno que tenga sentido: «jugaron».", "Resultado: «Los estudiantes del 7.º B jugaron en el patio.»"], "«Los estudiantes del 7.º B jugaron en el patio.»")],
  [("Escribir una idea dependiente con mayúscula y punto como si fuera independiente.", "«Porque llovía» deja al lector esperando.", "Únela a la oración que la completa."),
   ("Pensar que una oración necesita ser larga.", "Una sola palabra con verbo, como «Corre.», ya tiene sentido.", "Busca el verbo conjugado y el sentido completo.")],
  ([E("«Mi hermana, cuando llegó.» ¿Es oración o fragmento?", "Fragmento", "La idea empieza con «cuando» y queda sin terminar."),
    E("«Estudiamos juntos.» ¿Es oración o fragmento?", "Oración", "Tiene verbo conjugado y sentido completo."),
    E("«El parque de la esquina con los columpios rojos.» ¿Es oración o fragmento?", "Fragmento", "No tiene verbo conjugado.")],
   [E("¿Cuál palabra hace que «Aunque estaba cansado.» sea un fragmento: «aunque» o «estaba»?", "Aunque", "Deja la idea dependiendo de otra."),
    E("¿Qué le falta a «Mis primos de Valparaíso.» para ser oración?", "Un verbo conjugado", "No dice nada de los primos."),
    E("«Corre.» ¿Es oración, aunque tiene una sola palabra?", "Sí", "Tiene verbo conjugado y sentido completo.")],
   [E("Une los fragmentos: «Se quedaron en casa. Porque hacía frío.» Escribe una sola oración.", "Se quedaron en casa porque hacía frío.", "El fragmento dependiente se une a la oración que lo completa."),
    E("Completa el fragmento «La profesora de lenguaje en la sala.» con el verbo adecuado: (a) revisó (b) revisando (c) revisar", "(a)", "Solo (a) es verbo conjugado."),
    E("¿Cuál es una oración completa? (a) Cuando terminó la clase. (b) Terminó la clase. (c) La clase de ayer.", "(b)", "Tiene verbo conjugado y sentido completo.")],
   [arith("En un texto de 10 grupos de palabras puntuados como oraciones, 4 son fragmentos. ¿Cuántos son oraciones completas?", "10-4", "Se restan los fragmentos del total.", " oraciones"),
    E("En una narración, el autor escribe a propósito «Silencio. Solo el viento.» ¿Por qué en un informe escolar conviene evitarlo?", "Porque en un informe se espera claridad y oraciones completas", "En literatura puede ser un recurso, pero en un informe confunde.")],
   [E("Revisa: «El cuaderno de Matías. Estaba sobre la mesa.» ¿Cuál de las dos es el fragmento?", "«El cuaderno de Matías.»", "No tiene verbo conjugado."),
    E("Corrige: «Cuando sonó el timbre. Salimos al patio.» Escribe la oración corregida.", "Cuando sonó el timbre, salimos al patio.", "Se une la idea dependiente con la oración que la completa.")]),
  [E("En tu informe aparece «Los resultados de la encuesta sobre el casino». ¿Cómo lo conviertes en oración? (a) Los resultados de la encuesta sobre el casino fueron buenos. (b) Los resultados de la encuesta sobre el casino y el patio. (c) Sobre el casino.", "(a)", "Agrega un verbo conjugado y da sentido completo.")],
  [E("¿Qué debe tener una oración?", "Un verbo conjugado y sentido completo", "Son las dos condiciones de la clase."),
   E("En Lenguaje: ¿Qué es un fragmento?", "Un grupo de palabras que parece oración pero está incompleto", "Le falta verbo o depende de otra idea."),
   E("¿Cómo se arregla un fragmento que depende de otra idea?", "Uniéndolo a la oración que lo completa", "Así la idea queda completa.")],
  ("Revisa este texto de ejemplo y reescribe los fragmentos para que todas sean oraciones completas: «Ayer fuimos al museo. El museo de la ciudad. Porque nos tocaba la visita. Los guías muy simpáticos. Aprendimos mucho. Aunque llegamos tarde.»",
   "Ayer fuimos al museo de la ciudad porque nos tocaba la visita. Los guías fueron muy simpáticos. Aprendimos mucho, aunque llegamos tarde.",
   ["identifica los fragmentos", "los une o completa", "las oraciones quedan con sentido completo"], ["texto reescrito"],
   ["dejar fragmentos", "cambiar el sentido"], "Lee tu texto a alguien y pregúntale si queda esperando algo en alguna oración."),
  "Escribe un fragmento y arréglalo.",
  "Escribe una oración de una sola palabra y otra de más de quince palabras.")

# ================================================================== clase 2
L(OA, 2,
  "Este cuaderno y un lápiz. Todas las oraciones están escritas en los ejercicios.",
  "Aprenderé a reconocer el predicado y el verbo núcleo de una oración, para saber qué se dice y revisar mis textos.",
  ["Sé distinguir una oración de un fragmento.", "Sé reconocer verbos."],
  ["Toda oración tiene dos partes: el sujeto (de quién o de qué se habla) y el predicado (lo que se dice del sujeto). En «El gato duerme en el sillón», el sujeto es «el gato» y el predicado es «duerme en el sillón». El predicado puede tener una o varias palabras, pero siempre contiene un verbo conjugado.",
   "El verbo núcleo del predicado es la palabra principal: es el verbo conjugado que expresa la acción, el estado o el proceso. En «Mis primos construyeron una casa de ramas», el predicado es «construyeron una casa de ramas» y su núcleo es «construyeron». Los demás elementos (una casa de ramas) completan lo que dice el verbo. A veces el verbo núcleo está formado por dos palabras, como en «han terminado» o «había llegado»: se trata de un solo verbo compuesto.",
   "Para encontrar el verbo núcleo, busca la palabra que puedes cambiar de tiempo: «duerme» pasa a «durmió» o «dormirá». Esa es la prueba. Para separar sujeto y predicado, pregunta: ¿quién o qué realiza la acción? Esa parte es el sujeto; lo demás, el predicado. Saber esto sirve para revisar si la oración está completa y si sus partes concuerdan."],
  [("sujeto", "parte de la oración que dice de quién o de qué se habla"), ("predicado", "parte de la oración que dice algo del sujeto"), ("verbo núcleo", "verbo conjugado principal del predicado"), ("verbo compuesto", "verbo formado por dos palabras, como han terminado"), ("prueba del tiempo", "cambiar el verbo de tiempo para reconocerlo")],
  [("Separar sujeto y predicado", "«Mis primos construyeron una casa de ramas.» Separa sujeto y predicado y marca el verbo núcleo.",
    ["¿Quién construyó? «Mis primos»: es el sujeto.", "Lo demás es el predicado: «construyeron una casa de ramas».", "El núcleo es «construyeron»."], "Sujeto: mis primos; predicado: construyeron una casa de ramas; núcleo: construyeron"),
   ("Verbo compuesto", "«Las vecinas habían llegado temprano.» ¿Cuál es el verbo núcleo?",
    ["«Habían llegado» son dos palabras de un solo verbo.", "Con la prueba del tiempo: «llegarán», «llegaron».", "El núcleo es «habían llegado»."], "«Habían llegado»")],
  [("Marcar un sustantivo como verbo núcleo.", "El núcleo del predicado es un verbo, no un sustantivo.", "Usa la prueba del tiempo."),
   ("Dividir el verbo compuesto en dos núcleos.", "«Han terminado» es un solo verbo.", "Considera ambas palabras como el núcleo.")],
  ([E("«El gato duerme en el sillón.» ¿Cuál es el verbo núcleo?", "Duerme", "Es el verbo conjugado que cambia de tiempo."),
    E("En «El gato duerme en el sillón», ¿cuál es el predicado?", "Duerme en el sillón", "Es lo que se dice del gato."),
    E("En «El gato duerme en el sillón», ¿de quién se habla?", "Del gato", "Es el sujeto.")],
   [E("«Los niños construyeron un fuerte de almohadas.» ¿Cuál es el verbo núcleo?", "Construyeron", "Es la palabra que cambia con el tiempo."),
    E("«Han terminado la tarea.» ¿El verbo núcleo es «han» o «han terminado»?", "Han terminado", "Es un verbo compuesto."),
    E("«El sol brilla.» ¿Cuántas palabras tiene el predicado?", "Una", "El predicado es solo la palabra «brilla».")],
   [E("Separa sujeto y predicado: «La profesora de música reparte los cuadernos». Escribe el sujeto.", "La profesora de música", "Es quien realiza la acción."),
    E("En «Camila y su prima ordenaron los libros», ¿cuál es el predicado?", "Ordenaron los libros", "Es lo que se dice de Camila y su prima."),
    E("Cambia el verbo a futuro en «Pintan el mural» para comprobar el núcleo. ¿Cómo queda?", "Pintarán el mural", "La prueba del tiempo confirma que «pintan» es el verbo.")],
   [E("«Mañana llegarán los invitados.» ¿Cuál es el verbo núcleo?", "Llegarán", "Es el verbo conjugado en futuro."),
    E("Un estudiante marca «mural» como verbo en «Pintaron el mural». ¿Qué error comete?", "Marca un sustantivo en lugar del verbo", "«Mural» no cambia de tiempo.")],
   [E("«La directora de la escuela, que llegó temprano, saludó a todos.» ¿Cuál es el verbo del predicado principal: «llegó» o «saludó»?", "Saludó", "Es lo que se dice de la directora; «que llegó temprano», entre comas, solo aclara quién es ella."),
    arith("Una guía tiene 12 oraciones. Marcas el verbo núcleo en 9. ¿Cuántas te faltan por marcar?", "12-9", "Se restan las marcadas del total.", " oraciones")]),
  [E("En tu cuento escribiste: «Los vecinos del pasaje cuidan el jardín comunitario». ¿Cuál es el núcleo del predicado y por qué?", "Cuidan; es el verbo conjugado que cambia de tiempo", "Con la prueba: cuidaron, cuidarán.")],
  [E("¿Qué dos partes tiene toda oración?", "Sujeto y predicado", "Una dice de quién se habla y otra qué se dice."),
   E("¿Qué es el verbo núcleo?", "El verbo conjugado principal del predicado", "Expresa la acción o el estado."),
   E("¿Qué prueba ayuda a reconocer el verbo?", "Cambiarlo de tiempo", "Un verbo cambia de tiempo.")],
  ("Analiza estas tres oraciones de ejemplo: 1) «Los estudiantes de séptimo prepararon una exposición.» 2) «Mi abuelo ha contado esa historia muchas veces.» 3) «Mañana mis compañeros visitarán el museo.» Para cada una escribe el sujeto, el predicado y el verbo núcleo.",
   "1) Sujeto: los estudiantes de séptimo; predicado: prepararon una exposición; núcleo: prepararon. 2) Sujeto: mi abuelo; predicado: ha contado esa historia muchas veces; núcleo: ha contado. 3) Sujeto: mis compañeros; predicado: mañana visitarán el museo; núcleo: visitarán.",
   ["identifica sujeto y predicado", "identifica el verbo núcleo", "reconoce el verbo compuesto"], ["tabla de tres filas"],
   ["dividir el verbo compuesto", "marcar un sustantivo como núcleo"], "Comprueba cada núcleo cambiando el verbo de tiempo."),
  "Elige tres oraciones de un libro y marca su verbo núcleo.",
  "Escribe tres oraciones con verbos compuestos.")

# ================================================================== clase 3
L(OA, 3,
  "Este cuaderno y un lápiz. Todas las oraciones están escritas en los ejercicios.",
  "Aprenderé a ubicar el sujeto, expreso o tácito, para determinar de qué o de quién se habla.",
  ["Sé reconocer el predicado y el verbo núcleo.", "Sé qué es una persona gramatical."],
  ["El sujeto es de quién o de qué se habla en la oración. Para ubicarlo, primero busca el verbo núcleo y luego pregunta: ¿quién o qué + verbo? En «Los vecinos del pasaje pintaron el muro», preguntas ¿quiénes pintaron? Respuesta: «los vecinos del pasaje». Esa es el sujeto. Su palabra principal (el núcleo del sujeto) es «vecinos»; las demás (los, del pasaje) lo acompañan.",
   "El sujeto no siempre está al comienzo. En «Llegó una carta» el sujeto es «una carta» y va después del verbo. Tampoco siempre está escrito: cuando se omite, es un sujeto tácito, que se deduce de la forma del verbo. En «Pintamos el muro» el verbo termina en -amos, y por eso sabemos que el sujeto tácito es «nosotros». En «Ayer compré pan», el sujeto tácito es «yo». Si el sujeto está escrito, se llama sujeto expreso.",
   "Hay sujetos compuestos, con dos núcleos unidos por «y»: «Camila y Rodrigo estudian». Conocer el sujeto sirve para revisar la escritura: te ayuda a comprobar si el verbo concuerda y a evitar que quede una oración sin saber de quién se habla. Si dudas, vuelve a la pregunta ¿quién o qué + verbo?"],
  [("sujeto expreso", "sujeto que está escrito en la oración"), ("sujeto tácito", "sujeto que no está escrito y se deduce del verbo"), ("núcleo del sujeto", "palabra principal del sujeto"), ("sujeto compuesto", "sujeto con dos núcleos unidos, como Ana y Luis"), ("desinencia", "terminación del verbo que indica persona y número")],
  [("Ubicar un sujeto expreso", "«Los vecinos del pasaje pintaron el muro.» Ubica el sujeto y su núcleo.",
    ["Verbo núcleo: pintaron.", "¿Quiénes pintaron? Los vecinos del pasaje.", "La palabra principal es «vecinos»."], "Sujeto: los vecinos del pasaje; núcleo: vecinos"),
   ("Sujeto tácito", "«Pintamos el muro el sábado.» ¿Cuál es el sujeto?",
    ["Verbo núcleo: pintamos.", "La terminación -amos indica «nosotros».", "El sujeto está omitido: es tácito."], "Sujeto tácito: nosotros")],
  [("Creer que el sujeto siempre va primero.", "En «Llegó una carta» va después del verbo.", "Busca el verbo y pregunta ¿quién o qué + verbo?"),
   ("Decir que una oración sin sujeto escrito no lo tiene.", "El verbo indica quién actúa: es tácito.", "Fíjate en la terminación del verbo.")],
  ([E("«Camila estudia.» ¿Cuál es el sujeto?", "Camila", "Responde ¿quién estudia?"),
    E("«Estudiamos juntos.» ¿El sujeto está escrito o es tácito?", "Es tácito", "No aparece escrito."),
    E("«Llegó una carta.» ¿Dónde está el sujeto: antes o después del verbo?", "Después del verbo", "El sujeto es «una carta».")],
   [E("«Compré pan ayer.» ¿Cuál es el sujeto tácito?", "Yo", "La terminación -é indica primera persona singular."),
    E("«Camila y Rodrigo estudian.» ¿El sujeto es simple o compuesto?", "Compuesto", "Tiene dos núcleos unidos por «y»."),
    E("En «Los vecinos del pasaje pintaron el muro», ¿cuál es el núcleo del sujeto?", "Vecinos", "Es la palabra principal del sujeto.")],
   [E("«Mañana visitarán el museo.» El verbo termina en -arán. ¿Qué sujeto tácito se deduce: ellos o yo?", "Ellos", "La terminación -arán es de tercera persona plural."),
    E("«Los estudiantes de séptimo prepararon la exposición.» ¿Cuál es el sujeto?", "Los estudiantes de séptimo", "Responde ¿quiénes prepararon?"),
    E("«Escribiste una carta preciosa.» ¿Cuál es el sujeto tácito?", "Tú", "La terminación -aste es de segunda persona singular.")],
   [E("Un estudiante dice que en «Cantaron en el coro» no hay sujeto. ¿Es correcto?", "No; hay un sujeto tácito: ellos o ellas", "La terminación del verbo lo indica."),
    E("«Llegaron los invitados.» ¿Cuál es el sujeto y dónde está?", "Los invitados; después del verbo", "Responde ¿quiénes llegaron?")],
   [E("¿En cuál oración el sujeto es tácito? (a) Pedro leyó un cuento. (b) Leímos un cuento. (c) Los niños leyeron un cuento.", "(b)", "En (b) el sujeto «nosotros» no está escrito."),
    arith("Una guía tiene 15 oraciones: 6 con sujeto tácito y las demás con sujeto expreso. ¿Cuántas tienen sujeto expreso?", "15-6", "Se restan las de sujeto tácito del total.", " oraciones")]),
  [E("En tu texto escribiste: «Preparamos la presentación toda la semana». Tu profesor pregunta «¿quién la preparó?». ¿Qué respondes y de dónde lo sabes?", "Nosotros, por la terminación -amos del verbo", "Es un sujeto tácito.")],
  [E("¿Qué pregunta ayuda a encontrar el sujeto?", "¿Quién o qué + verbo?", "Se pregunta al verbo."),
   E("¿Qué es un sujeto tácito?", "El que no está escrito y se deduce del verbo", "Se identifica por la terminación."),
   E("¿Un sujeto puede ir después del verbo?", "Sí", "Por ejemplo, «Llegó una carta».")],
  ("Ubica el sujeto de cada oración de ejemplo y di si es expreso o tácito: 1) «Mis tías prepararon empanadas.» 2) «Prepararemos el escenario.» 3) «Sonó el timbre.» 4) «Sofía y yo ordenamos la sala.» 5) «Terminaste la tarea.»",
   "1) Mis tías (expreso). 2) Nosotros (tácito). 3) El timbre (expreso, después del verbo). 4) Sofía y yo (expreso, compuesto). 5) Tú (tácito).",
   ["ubica los cinco sujetos", "distingue expreso y tácito", "reconoce el compuesto y el que va después del verbo"], ["tabla con cinco filas"],
   ["decir que no hay sujeto", "buscar solo al inicio"], "Explica a otra persona cómo supiste el sujeto tácito en cada caso."),
  "Escribe tres oraciones con sujeto tácito.",
  "Escribe una oración con el sujeto después del verbo.")

# ================================================================== clase 4
L(OA, 4,
  "Este cuaderno y un lápiz. Todas las oraciones están escritas en los ejercicios.",
  "Aprenderé a revisar la concordancia entre el sujeto y el predicado (número y persona) para corregir mis textos.",
  ["Sé ubicar el sujeto y el verbo núcleo.", "Sé que hay singular y plural."],
  ["La concordancia entre sujeto y predicado significa que el verbo debe coincidir con el núcleo del sujeto en número (singular o plural) y en persona (yo, tú, él...). Si el sujeto está en plural, el verbo va en plural: «Los niños juegan». Si está en singular, el verbo va en singular: «El niño juega». Un error común es escribir «Los niños juega», porque no se mira el núcleo del sujeto.",
   "Hay casos que se prestan a error. Cuando entre el sujeto y el verbo hay palabras intermedias: «Los resultados de la encuesta fueron buenos» (el núcleo es «resultados», no «encuesta»). Cuando el sujeto es compuesto: «La directora y el profesor llegaron» (dos núcleos, verbo en plural). Cuando el sujeto va después del verbo: «Llegaron los invitados». Y con el verbo «haber» como existencia, que va en singular: «Había muchos estudiantes» (no «Habían»), «Hubo dos reuniones» (no «Hubieron»).",
   "Para corregir, sigue tres pasos: (1) encuentra el verbo núcleo; (2) pregunta ¿quién o qué + verbo? para ubicar el sujeto y su núcleo; (3) comprueba que verbo y núcleo coincidan en número y persona. Si no coinciden, cambia el verbo, no el sujeto, salvo que el sentido pida otro."],
  [("concordancia", "coincidencia en número y persona entre sujeto y verbo"), ("número", "singular o plural"), ("persona", "primera, segunda o tercera, singular o plural"), ("núcleo", "palabra principal"), ("palabras intermedias", "las que se interponen entre el sujeto y el verbo")],
  [("Corregir con palabras intermedias", "Corrige: «Los resultados de la encuesta fue buenos».",
    ["Verbo: fue.", "¿Qué fue bueno? «Los resultados de la encuesta». Núcleo: resultados (plural).", "El verbo debe ser plural: fueron."], "«Los resultados de la encuesta fueron buenos»"),
   ("Haber de existencia", "Corrige: «Habían muchos estudiantes en el patio».",
    ["«Haber» de existencia no concuerda con lo que existe.", "Va en singular: había.", "Resultado: «Había muchos estudiantes en el patio»."], "«Había muchos estudiantes en el patio»")],
  [("Hacer concordar el verbo con la palabra más cercana.", "La palabra más cercana puede no ser el núcleo del sujeto.", "Ubica el núcleo con ¿quién o qué + verbo?"),
   ("Usar «habían» o «hubieron» para existencia.", "El verbo haber de existencia va en singular.", "Escribe «había» y «hubo».")],
  ([E("Corrige: «Los niños juega en el patio».", "Los niños juegan en el patio", "El sujeto es plural y el verbo también."),
    E("Corrige: «El niño juegan en el patio».", "El niño juega en el patio", "El sujeto es singular."),
    E("«Yo canto» y «Tú cantas». ¿Qué cambia en el verbo: la persona o el significado?", "La persona", "Cambia la terminación según el sujeto.")],
   [E("«Los libros de la biblioteca estaba ordenados.» ¿Qué palabra no concuerda con el núcleo del sujeto («libros») y cómo se corrige?", "Estaba → estaban", "El núcleo «libros» es plural, así que el verbo también."),
    E("«La directora y el profesor llegó.» ¿Cuál es el verbo correcto?", "Llegaron", "El sujeto compuesto es plural."),
    E("«Hubo dos reuniones» o «Hubieron dos reuniones»: ¿cuál es correcta?", "Hubo dos reuniones", "Haber de existencia va en singular.")],
   [E("Corrige: «Las notas del curso fue publicadas».", "Las notas del curso fueron publicadas", "El núcleo es «notas»."),
    E("Corrige: «La banda del colegio tocaron en el desfile». Elige el verbo correcto: (a) tocó (b) tocaron (c) tocan", "(a)", "El núcleo es «banda», singular, y la acción es pasada."),
    E("Revisa: «Ayer vinieron mi hermana y mi prima». ¿Hay error de concordancia?", "No", "El sujeto compuesto lleva verbo plural.")],
   [E("Un estudiante escribe «Los alumnos de la escuela vecina llegó temprano» porque «escuela» está más cerca del verbo. ¿Qué paso omitió?", "Ubicar el núcleo del sujeto, que es «alumnos»", "Hay que mirar el sujeto, no la palabra más cercana."),
    E("Corrige: «Había muchas personas esperando y habían pocas sillas». ¿Qué parte tiene el error?", "«Habían pocas sillas»; debe ser «había pocas sillas»", "Haber de existencia va en singular.")],
   [E("Encuentra el error: «Mis amigos y yo fuimos al parque, pero los demás se quedó en casa». ¿Cuál verbo corriges?", "Se quedó → se quedaron", "El sujeto «los demás» es plural."),
    arith("En una guía hay 20 oraciones y 7 tienen error de concordancia. ¿Cuántas están bien?", "20-7", "Se restan las erróneas del total.", " oraciones")]),
  [E("Tu informe dice: «Los estudiantes del curso presentó el trabajo». ¿Cómo lo corriges?", "Los estudiantes del curso presentaron el trabajo", "El núcleo «estudiantes» es plural.")],
  [E("¿En qué debe coincidir el verbo con el sujeto?", "En número y persona", "Es la regla de concordancia."),
   E("¿Qué se hace primero para corregir la concordancia?", "Ubicar el verbo núcleo y el sujeto", "Así se comprueba la coincidencia."),
   E("¿El verbo haber de existencia va en singular o plural?", "Singular", "Había y hubo.")],
  ("Corrige las oraciones de ejemplo y subraya el núcleo del sujeto: 1) «Los niños de la sala 4 ganó el concurso.» 2) «Había muchos libros nuevos y habían pocas mesas.» 3) «Mis primos y yo fue al museo.» 4) «Las puertas del gimnasio estaba abierta.»",
   "1) Los niños de la sala 4 ganaron el concurso (núcleo: niños). 2) Había muchos libros nuevos y había pocas mesas. 3) Mis primos y yo fuimos al museo. 4) Las puertas del gimnasio estaban abiertas (núcleo: puertas).",
   ["corrige los cuatro errores", "subraya el núcleo", "mantiene el sentido"], ["oraciones corregidas"],
   ["concordar con la palabra más cercana", "usar habían para existencia"], "Pide a alguien que revise tu corrección usando ¿quién o qué + verbo?"),
  "Escribe tres oraciones con sujeto plural y tres con sujeto singular, con su verbo correcto.",
  "Escribe oraciones con «haber» de existencia.")

# ================================================================== clase 5
TEXTO = "Mi abuelo, que tenía fama de cuentero, contaba cosas increíbles. Una vez dijo que había visto una ballena en el río. Nadie le creyó. Pero todos escuchaban igual. Porque sus historias eran buenas. Mientras tomábamos once."
L(OA, 5,
  "Este cuaderno y un lápiz. El texto de ejemplo y las oraciones están escritos en los ejercicios.",
  "Aprenderé a mejorar un texto usando lo que sé de la oración, el sujeto y el predicado, sin borrar mi estilo.",
  ["Sé ubicar sujeto y predicado.", "Sé revisar concordancia."],
  ["Mejorar un texto no es hacerlo igual al de los demás. Cada escritor tiene un estilo: su manera de elegir palabras, de combinar oraciones largas y cortas, de usar el humor o el tono. Al revisar con la gramática, buscamos tres cosas: que las oraciones estén completas (verbo conjugado y sentido), que el sujeto esté claro y que el verbo concuerde con él. Lo demás —el tono, las expresiones propias, el ritmo— es decisión del autor.",
   "Una técnica útil es revisar oración por oración con tres preguntas: ¿tiene verbo conjugado y sentido completo?, ¿puedo ubicar el sujeto?, ¿el verbo concuerda con él? Si una respuesta es no, hay que corregir. Pero si las oraciones están correctas, no es necesario cambiarlas solo porque son distintas de las de otros. Por ejemplo, una oración muy corta puede ser una elección de estilo si tiene verbo y sentido: «Nadie le creyó.»",
   "Al corregir, conserva tu voz. Si escribes con humor, mantén el humor; si usas una expresión propia de tu zona, déjala si el registro la admite. Las correcciones deben servir a la claridad, no a uniformar. Después de corregir, lee en voz alta y compara la versión nueva con la anterior: la idea debe ser la misma y el sentido más claro."],
  [("estilo", "manera personal de escribir"), ("voz", "personalidad que se nota en un texto"), ("claridad", "cualidad de lo que se entiende bien"), ("revisión gramatical", "revisión de oraciones, sujeto y concordancia"), ("uniformar", "hacer que todo suene igual")],
  [("Corregir sin perder la voz", f"Texto de ejemplo: «{TEXTO}» Corrige los dos fragmentos manteniendo el tono de cuentero.",
    ["«Porque sus historias eran buenas.» es fragmento: se une a la oración anterior.", "«Mientras tomábamos once.» es fragmento: se completa con un verbo principal.", "Conservo expresiones como «fama de cuentero» y «once»."], "«Pero todos escuchaban igual porque sus historias eran buenas. Escuchábamos mientras tomábamos once.»"),
   ("Cuándo no cambiar", "«Nadie le creyó.» Un compañero dice que hay que alargarla porque es muy corta. ¿Tiene razón?",
    ["Tiene verbo: creyó.", "Tiene sujeto: nadie.", "Es una oración correcta: la brevedad es una decisión de estilo."], "No; es una oración completa y correcta")],
  [("Reescribir todo para que suene como un manual.", "Pierdes la voz del autor.", "Corrige solo lo que está incompleto o no concuerda."),
   ("No corregir fragmentos porque «así se ve más literario».", "En textos escolares confunden al lector.", "Úsalos solo si buscas un efecto y lo explicas.")],
  ([E(f"Texto: «{TEXTO}» ¿Cuál oración es un fragmento: «Nadie le creyó.» o «Mientras tomábamos once.»?", "«Mientras tomábamos once.»", "Empieza con «mientras» y deja la idea esperando."),
    E("¿Qué es el estilo de un autor?", "Su manera personal de escribir", "Incluye el tono y la manera de combinar oraciones."),
    E("«Nadie le creyó.» ¿Tiene verbo conjugado?", "Sí: creyó", "Por eso es una oración completa.")],
   [E(f"Texto: «{TEXTO}» ¿Cuál es el sujeto de «Nadie le creyó»?", "Nadie", "Responde ¿quién no le creyó?"),
    E("¿Corregir un texto significa hacer que todos suenen igual?", "No", "La corrección sirve a la claridad, no a uniformar."),
    E("Una autora usa «once» para hablar de la comida de la tarde. ¿Debe cambiarla en un texto que dirige a compañeros de Chile?", "No necesariamente; es una expresión propia que su audiencia entiende", "El registro y la audiencia la admiten.")],
   [E("Corrige el fragmento: «Aunque estaba cansada. Siguió caminando». Elige: (a) Aunque estaba cansada, siguió caminando. (b) Aunque estaba cansada siguió. (c) Aunque cansada.", "(a)", "Une la idea dependiente con la oración que la completa."),
    E("Corrige la concordancia sin cambiar el estilo: «Las historias del abuelo era geniales». ¿Cuál queda mejor? (a) Las historias del abuelo eran geniales. (b) Las historias eran muy buenas y notables. (c) Era genial.", "(a)", "Corrige el verbo y mantiene la palabra «geniales»."),
    E("«Mi abuelo, que tenía fama de cuentero, contaba cosas increíbles.» ¿Cuál es el sujeto?", "Mi abuelo", "La parte «que tenía fama de cuentero» lo explica.")],
   [E("Un estudiante cambia todas sus oraciones cortas por largas «para que suene serio», aunque estaban bien. ¿Qué error comete?", "Uniforma su estilo sin necesidad", "Las oraciones correctas no requerían cambio."),
    E("Dos versiones: «Nadie le creyó. Pero todos escuchaban igual.» y «Nadie le creyó, pero todos escuchaban igual.». ¿Son ambas correctas?", "Sí; la diferencia es de ritmo", "Ambas tienen verbo y sentido completo.")],
   [arith(f"Texto: «{TEXTO}» tiene 6 grupos puntuados y 2 son fragmentos. Si cada fragmento se une a otra oración, ¿cuántas oraciones completas quedan?", "6-2", "Los dos fragmentos dejan de ser grupos separados.", " oraciones"),
    E("Reescribe sin perder la voz: «Porque tenía ganas de reír. Contó otra historia». Elige la mejor: (a) Contó otra historia porque tenía ganas de reír. (b) Porque tenía ganas. (c) Contó, reír.", "(a)", "Une el fragmento y conserva el sentido.")]),
  [E("Tu amiga escribe con mucho humor: «Mi perro, el gran Bruno, se comió mi tarea. Lo hizo otra vez. Aunque yo no le creo». ¿Qué corrección mínima sugieres?", "Unir «Aunque yo no le creo» a la oración anterior con una coma", "Corrige el fragmento sin quitar el humor.")],
  [E("¿Qué se corrige y qué se conserva al revisar con la gramática?", "Se corrigen fragmentos y concordancia; se conserva la voz", "La gramática aclara, no uniformiza."),
   E("¿Una oración corta puede ser correcta?", "Sí, si tiene verbo y sentido completo", "La brevedad puede ser una decisión de estilo."),
   E("¿Qué se hace después de corregir?", "Leer en voz alta y comparar con la versión anterior", "Se comprueba que el sentido sea el mismo.")],
  ("Corrige este texto de ejemplo manteniendo su voz: «La tía Marta, que siempre llegaba tarde, trajo una torta gigante. Todos aplaudimos. Aunque la torta estaba medio torcida. Porque la había hecho sola. Los primos comieron tres trozos cada uno». Marca cuáles fragmentos corriges y cuáles oraciones dejas igual, y explica por qué.",
   "Corrijo los fragmentos «Aunque la torta estaba medio torcida» y «Porque la había hecho sola»; las uno así: «Todos aplaudimos, aunque la torta estaba medio torcida, porque la había hecho sola». Dejo igual «Todos aplaudimos» y «Los primos comieron tres trozos cada uno» porque tienen verbo y sentido completo. Mantengo «medio torcida» porque es parte de la voz.",
   ["corrige los dos fragmentos", "deja intactas las oraciones correctas", "explica la decisión"], ["texto corregido y explicación"],
   ["reescribir todo", "dejar fragmentos"], "Lee tu versión con otra persona y verifica que conserve el humor."),
  "Elige un párrafo tuyo y marca una decisión de estilo que mantendrás.",
  "Escribe un párrafo con tres fragmentos a propósito y corrígelo.")
