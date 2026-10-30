"""Cuaderno del estudiante, 1.º básico Orientación: OA 06 (conflictos entre pares), OA 07 (pertenencia a grupos) y OA 08 (hábitos para aprender)."""
from __future__ import annotations

from student_content_ma01_b import task
from student_lessons import arith, ex, register

OA6, OA7, OA8 = "OR01 OA 06", "OR01 OA 07", "OR01 OA 08"

# ================================================================ OA 06
register(
    OA6, 1,
    materials="Una hoja, lápiz y los conflictos ficticios escritos en cada ejercicio.",
    use="Aprenderé a contar un conflicto con tres partes: qué pasó, cómo me sentí y qué necesito, sin insultar. Sirve para que me entiendan y poder resolverlo.",
    prior=["Sé nombrar emociones.", "Sé que puedo pedir lo que necesito con palabras."],
    explain=[
        "Un conflicto es cuando dos personas quieren cosas distintas o se sienten mal por algo que pasó. Los conflictos son normales entre amigos. Lo importante es cómo los resolvemos.",
        "Para contar un conflicto sin insultar, usa tres partes. Primero, el hecho: lo que pasó y se pudo ver o escuchar («Me quitaste el lápiz»). Segundo, la emoción: lo que sentiste («Me enojé»). Tercero, la necesidad: lo que te ayudaría («Necesito que me lo devuelvas»).",
        "Un hecho no incluye insultos ni adivinar lo que el otro pensó. Decir «eres malo» es un juicio, no un hecho. Decir «me quitaste el lápiz» es un hecho. Cuando cuentas los hechos, el otro puede escucharte mejor.",
    ],
    vocab=[("conflicto", "cuando dos quieren cosas distintas o se sienten mal"), ("hecho", "lo que pasó y se puede ver o escuchar"), ("emoción", "lo que siento"), ("necesidad", "lo que me ayudaría"), ("insulto", "palabra que ofende")],
    worked=[
        {"title": "Hecho, emoción y necesidad", "problem": "Beto dice: «Luis es malo porque tomó mi goma». Arma una frase con hecho, emoción y necesidad.", "steps": ["Hecho: «Tomaste mi goma».", "Emoción: «Me enojé».", "Necesidad: «Necesito que me la devuelvas»."], "answer": "«Tomaste mi goma, me enojé, necesito que me la devuelvas»"},
        {"title": "Hecho o juicio", "problem": "¿«Eres un egoísta» es un hecho o un juicio?", "steps": ["No se puede ver ni escuchar que alguien sea egoísta.", "Es una opinión que ofende.", "Es un juicio."], "answer": "Es un juicio"},
    ],
    mistakes=[
        {"wrong": "Insultar para contar lo que pasó.", "why": "La rabia sale en palabras ofensivas.", "fix": "Cuenta el hecho, tu emoción y lo que necesitas."},
        {"wrong": "Decir lo que el otro pensó: «Lo hiciste a propósito».", "why": "Adivinamos las intenciones.", "fix": "Di lo que viste y pregunta qué pasó."},
    ],
    tiers={
        "recovery": [
            ex("«Me empujaste en la fila» ¿es un hecho o un insulto?", "Un hecho", "Dice lo que pasó."),
            ex("«Me sentí triste» ¿es una emoción o una necesidad?", "Una emoción", "Dice lo que siento."),
            ex("«Necesito que me esperes» ¿es una necesidad?", "Sí", "Dice lo que me ayudaría."),
        ],
        "understand": [
            ex("¿Cuáles son las tres partes para contar un conflicto?", "Hecho, emoción y necesidad", "Cuentan qué pasó, cómo me siento y qué pido."),
            ex("¿Por qué conviene contar solo los hechos?", "Para que el otro me escuche sin sentirse atacado", "Un hecho no ofende."),
            ex("¿Es normal tener conflictos con amigos?", "Sí", "Pasa cuando queremos cosas distintas."),
        ],
        "apply": [
            ex("Ana dice: «Dani es pesado porque se llevó mi libro». Escribe el hecho.", "«Se llevó mi libro»", "Es lo que se puede ver."),
            ex("Mía y Tomás quieren el mismo columpio. Escribe una necesidad de Mía.", "Por ejemplo: «Necesito que me des un turno»", "Dice lo que le ayudaría."),
            ex("Rosa dice: «Me ignoraste en el recreo». Escribe una emoción posible.", "Por ejemplo: «Me sentí sola»", "Nombra lo que sintió."),
        ],
        "reason": [
            ex("Pedro dice: «Eres un tramposo». Luis responde: «No es cierto». ¿Qué cambiaría Pedro para que Luis lo escuche?", "Contar el hecho en vez de insultar", "Un hecho no ofende."),
            ex("Carla dice: «Lo hiciste para fastidiarme». ¿Es un hecho?", "No", "No sabemos lo que el otro pensó."),
        ],
        "challenge": [
            ex("Eva dice: «Rompiste mi dibujo; me puse triste; quiero que me ayudes a hacer otro». ¿Cuál es la necesidad?", "«Quiero que me ayudes a hacer otro»", "Es lo que pide."),
            ex("Sofía cuenta: «Beto nunca me deja jugar». Eso incluye «nunca». ¿Es un hecho exacto?", "No", "«Nunca» no es lo que pasó hoy."),
        ],
    },
    context=[ex("En el patio, Dani tomó la pelota de Luis sin pedírsela. Luis dice: «Tomaste mi pelota, me enojé, necesito que me la devuelvas». ¿Usó las tres partes?", "Sí", "Dijo hecho, emoción y necesidad.")],
    selfcheck=[ex("¿Un insulto es un hecho?", "No", "Es una palabra que ofende."), ex("¿Qué parte dice cómo me siento?", "La emoción", "Nombra lo que siento."), ex("¿Qué parte dice lo que quiero?", "La necesidad", "Pide lo que me ayuda.")],
    open_task=task("Lee el caso: «Mía estaba armando un rompecabezas y Tomás sacó una pieza sin preguntar». Escribe o di una frase con hecho, emoción y necesidad para Mía. Puedes empezar así: «Tú ___, yo me sentí ___ y necesito ___».", "«Sacaste una pieza sin preguntar, me enojé y necesito que me la devuelvas».", ["incluye hecho", "incluye emoción", "incluye necesidad y no insulta"], ["frase escrita o dicha", "viñeta con globo de diálogo"], ["usar insultos", "adivinar lo que pensó Tomás"], "Reconoce cada parte y ayuda a cambiar palabras ofensivas por hechos."),
    reinforce="Cuenta algo que pasó hoy usando solo el hecho.",
    extend="Escribe dos hechos y dos juicios sobre una discusión por un juego.",
)

register(
    OA6, 2,
    materials="Una hoja, lápiz y los diálogos escritos en cada ejercicio.",
    use="Aprenderé a escuchar la versión del otro y repetirla con mis palabras antes de responder. Sirve para entender qué pasó de verdad.",
    prior=["Sé contar un conflicto con hecho, emoción y necesidad.", "Sé escuchar sin interrumpir."],
    explain=[
        "En un conflicto cada persona tiene su versión: lo que vio, sintió y quiere. Dos versiones pueden ser distintas y las dos pueden ser verdad para quien las cuenta. Por eso es importante escuchar la otra versión.",
        "Para escuchar de verdad, mira al otro y no lo interrumpas. Después reformula: «Entiendo que tú…, te sentiste… y necesitas…». Si te equivocaste, el otro te corrige. Reformular no significa que tengas que estar de acuerdo.",
        "Después de escuchar, puedes contar tu versión. Así los dos se sienten escuchados y es más fácil buscar una solución. Si hablan muy fuerte, pueden pedir una pausa y a un adulto que los ayude.",
    ],
    vocab=[("versión", "cómo cuenta alguien lo que pasó"), ("reformular", "repetir con mis palabras lo que entendí"), ("estar de acuerdo", "pensar lo mismo"), ("pausa", "detenerse un momento"), ("mediar", "ayudar a que dos se entiendan")],
    worked=[
        {"title": "Reformular", "problem": "Ana dice: «Me enojé porque no me dejaron jugar». ¿Cómo reformula Beto?", "steps": ["Beto repite lo que escuchó con sus palabras.", "Dice: «Entiendo que te enojaste porque no te dejamos jugar».", "Ana confirma."], "answer": "«Entiendo que te enojaste porque no te dejamos jugar»"},
        {"title": "Dos versiones", "problem": "Luis dice: «Yo estaba primero en la fila». Mía dice: «Yo estaba primero». ¿Una miente?", "steps": ["Cada uno cuenta lo que vio.", "Pueden haber visto cosas distintas.", "Hay que escuchar a los dos."], "answer": "No sabemos; hay que escuchar a los dos"},
    ],
    mistakes=[
        {"wrong": "Responder antes de escuchar la versión del otro.", "why": "Queremos defendernos rápido.", "fix": "Escucha, reformula y después habla."},
        {"wrong": "Pensar que reformular es darle la razón.", "why": "Se confunde entender con aprobar.", "fix": "Reformular solo muestra que entendiste."},
    ],
    tiers={
        "recovery": [
            ex("¿Cada persona tiene su versión del conflicto?", "Sí", "Cada uno cuenta lo que vio y sintió."),
            ex("Antes de responder, ¿qué haces: escuchar o interrumpir?", "Escuchar", "Para entender al otro."),
            ex("¿Reformular es repetir con tus palabras?", "Sí", "Muestra que entendiste."),
        ],
        "understand": [
            ex("En Orientación, ¿para qué sirve reformular?", "Para mostrar que entendí al otro", "Así se siente escuchado."),
            ex("¿Reformular significa estar de acuerdo?", "No", "Solo muestra que entendí."),
            ex("¿Qué haces si hablan muy fuerte y no se escuchan?", "Pedir una pausa o ayuda a un adulto", "Con calma se entienden mejor."),
        ],
        "apply": [
            ex("Dani dice: «Me quitaron mi lugar en la fila». Reformula con «Entiendo que…».", "«Entiendo que te quitaron tu lugar en la fila»", "Repite lo esencial."),
            ex("Carla dice: «Me dolió que me gritaras». Reformula con «Entiendo que…».", "«Entiendo que te dolió que te gritara»", "Repite lo esencial con otras palabras."),
            ex("Tomás y Rosa pelean por un lápiz. Escribe una pregunta para escuchar la versión de Rosa.", "Por ejemplo: «Rosa, ¿qué pasó para ti?»", "Pide su versión."),
        ],
        "reason": [
            ex("Eva dijo «no fue así» cuando Luis aún hablaba. ¿Qué hizo mal?", "Interrumpió antes de escuchar", "Debe esperar a que termine."),
            ex("Pedro reformuló y Mía dijo «no, no fue eso». ¿Qué hace Pedro?", "Escucha de nuevo y corrige", "Mía le ayuda a entender mejor."),
        ],
        "challenge": [
            arith("Sofía tiene 3 minutos para escuchar a Ana y luego 3 minutos para contar su versión. ¿Cuántos minutos son en total?", "3+3", "Se suman los dos tiempos."),
            ex("Dos niños cuentan versiones distintas. ¿Qué es lo más justo: creerle solo a uno o escuchar a los dos?", "Escuchar a los dos", "Así hay información completa."),
        ],
    },
    context=[ex("Beto dice: «Dani me pegó con la pelota». Dani dice: «Fue sin querer; estaba jugando». ¿Qué debe hacer la profesora?", "Escuchar a los dos", "Hay dos versiones.")],
    selfcheck=[ex("¿Debo escuchar antes de responder?", "Sí", "Para entender al otro."), ex("¿Qué frase uso para reformular?", "«Entiendo que…»", "Es una forma de repetir con mis palabras."), ex("¿Puedo estar en desacuerdo y reformular?", "Sí", "Reformular no es aprobar.")],
    open_task=task("Practica con un adulto: lee este conflicto. Mía dice: «Tomás se llevó mi pelota y no me la devolvió». Tomás dice: «Mía me la prestó y no me avisó que la quería». Escribe o di una frase que reformule la versión de Mía y otra que reformule la versión de Tomás.", "«Entiendo que tú, Mía, querías tu pelota de vuelta». «Entiendo que tú, Tomás, jugaste con la pelota porque Mía te la prestó».", ["reformula las dos versiones", "usa sus propias palabras", "no toma partido"], ["dos frases", "dibujo con globos"], ["repetir palabra por palabra", "dar la razón a uno"], "Reconoce lo bien reformulado y sugiere cambiar palabras que juzguen."),
    reinforce="Pregunta a alguien en casa su versión de algo que pasó y reformúlala.",
    extend="Escribe una frase para pedir una pausa cuando estén muy enojados.",
)

register(
    OA6, 3,
    materials="Una hoja, lápiz y los conflictos escritos en cada ejercicio.",
    use="Aprenderé a pensar más de una solución para un conflicto y a elegir la que cuida a todos. Sirve para no quedarme con una sola idea.",
    prior=["Sé contar un conflicto y escuchar la otra versión."],
    explain=[
        "Un conflicto casi siempre tiene más de una solución. Si dos niños quieren el mismo juego, pueden turnarse, jugar juntos, sortear quién empieza o elegir otro juego. Pensar varias ideas ayuda a encontrar una buena.",
        "Una buena solución cuida a las dos personas. No lastima a nadie, es justa y se puede cumplir. Una solución que solo le sirve a uno, como «yo me quedo con todo», no es justa. También puedes pedir ayuda a un adulto si no logran acordar.",
        "Para elegir, mira cada idea y piensa: ¿es justa?, ¿es segura?, ¿se puede hacer ahora? Si la respuesta es sí a todo, es una buena opción. Puedes probarla y, si no funciona, elegir otra.",
    ],
    vocab=[("solución", "una forma de resolver un problema"), ("alternativa", "otra opción"), ("justo", "bueno para todos"), ("sortear", "elegir al azar, por ejemplo con una moneda"), ("acordar", "ponerse de acuerdo")],
    worked=[
        {"title": "Varias soluciones", "problem": "Ana y Beto quieren el mismo balde en el arenero. Escribe tres soluciones.", "steps": ["Turnarse: primero uno y luego el otro.", "Jugar juntos con el balde.", "Sortear quién empieza."], "answer": "Turnarse, jugar juntos o sortear"},
        {"title": "Elegir con tres preguntas", "problem": "Luis propone: «Yo uso el balde todo el día». ¿Es una buena solución?", "steps": ["¿Es justa? No, solo sirve a Luis.", "No pasa la primera pregunta.", "Hay que buscar otra."], "answer": "No, porque no es justa"},
    ],
    mistakes=[
        {"wrong": "Quedarse con la primera idea sin pensar otras.", "why": "Parece lo más fácil.", "fix": "Busca al menos dos o tres ideas más."},
        {"wrong": "Elegir una solución que solo le sirve a uno.", "why": "Se piensa en lo que yo quiero.", "fix": "Revisa que sea justa para los dos."},
    ],
    tiers={
        "recovery": [
            ex("¿Turnarse es una solución posible para compartir un juego?", "Sí", "Cada uno usa el juego un rato."),
            ex("¿Sortear con una moneda es una forma justa de decidir?", "Sí", "Los dos tienen la misma oportunidad."),
            ex("¿Hay una sola solución para un conflicto?", "No", "Casi siempre hay varias."),
        ],
        "understand": [
            ex("¿Qué es una solución justa?", "Una que es buena para todos", "Cuida a las dos personas."),
            ex("¿Por qué conviene pensar varias soluciones?", "Para poder elegir la mejor", "Más ideas, mejor elección."),
            ex("¿Qué haces si dos no logran ponerse de acuerdo?", "Pedir ayuda a un adulto", "Un adulto puede mediar."),
        ],
        "apply": [
            ex("Mía y Dani quieren el mismo libro. Escribe dos soluciones.", "Por ejemplo: leerlo juntos o turnarse", "Son dos ideas distintas."),
            ex("Eva y Pedro discuten quién va primero en la fila. Escribe una solución que sea justa.", "Por ejemplo: hoy va uno y mañana el otro", "Es justa para ambos."),
            ex("Carla y Tomás quieren dibujar con el mismo lápiz rojo. Escribe una solución.", "Por ejemplo: usarlo por turnos de un minuto", "Los dos lo usan, uno después del otro."),
        ],
        "reason": [
            ex("Sofía propone: «Yo juego primero siempre». ¿Es justa? ¿Por qué?", "No, porque el otro nunca juega primero", "No cuida a los dos."),
            ex("Beto propone que se turnen y Ana acepta. ¿Es una buena solución?", "Sí", "Es justa y se puede cumplir."),
        ],
        "challenge": [
            arith("Si 2 niños quieren usar un trampolín y cada uno salta 5 veces en su turno, ¿cuántos saltos hacen en total?", "5+5", "Cinco saltos de cada niño."),
            ex("Ana eligió cara y Beto eligió cruz. Acordaron que empieza quien acierta. Lanzan la moneda y sale cruz. ¿Quién empieza?", "Beto", "Sale lo que Beto eligió."),
        ],
    },
    context=[ex("Luis y Rosa quieren el mismo columpio. Luis dice: «Primero yo, después tú». Rosa dice: «Mejor nos columpiamos juntos en los dos columpios». ¿Cuántas soluciones propusieron?", "2", "Turnos y columpiarse juntos.")],
    selfcheck=[ex("¿Una buena solución cuida a las dos personas?", "Sí", "Es justa para todos."), ex("¿Se pueden probar y cambiar las soluciones?", "Sí", "Si no funciona, se elige otra."), ex("¿Cuántas ideas conviene pensar?", "Más de una", "Así se puede elegir.")],
    open_task=task("Lee el conflicto: «Ana y Mía quieren usar el único pegamento para sus trabajos al mismo tiempo». Escribe o dibuja tres soluciones distintas, por ejemplo: turnarse, compartirlo en la mesa o pedir un segundo pegamento a la profesora. Marca con un círculo la que elegirías y explica por qué es justa.", "Soluciones: turnarse, ponerlo al medio de la mesa, pedir otro. Elijo ponerlo al medio porque las dos lo usan.", ["escribe tres soluciones distintas", "elige una", "explica por qué es justa"], ["tres ideas", "círculo en la elegida"], ["escribir tres ideas iguales", "elegir una que no cuida a ambas"], "Reconoce la variedad y pide que revise que sea justa y segura."),
    reinforce="Piensa dos soluciones para un conflicto por un juguete.",
    extend="Inventa una solución para un conflicto entre tres niños con una sola pelota.",
)

register(
    OA6, 4,
    materials="Una hoja, lápiz y los acuerdos escritos en cada ejercicio.",
    use="Aprenderé a elegir un acuerdo, probarlo y revisarlo, y a reparar si hubo daño. Sirve para que la solución dure y la amistad se cuide.",
    prior=["Sé contar un conflicto, escuchar y pensar soluciones."],
    explain=[
        "Un acuerdo es una decisión que toman los dos. Se elige entre las soluciones, se dice con palabras claras («Hoy te toca a ti primero») y se prueba. Un acuerdo claro dice quién hace qué y cuándo.",
        "Después de probar, hay que revisar. Pregúntense: ¿funcionó?, ¿alguien se sintió mal?, ¿hay que cambiar algo? Si no funcionó, no pasa nada: se elige otra solución. Revisar ayuda a que el acuerdo mejore.",
        "Si en el conflicto hubo daño, también es importante reparar. Puede ser disculparse, devolver algo, ayudar a arreglarlo. Reparar es parte del acuerdo y ayuda a recuperar la confianza.",
    ],
    vocab=[("acuerdo", "decisión que toman los dos"), ("probar", "poner en práctica una solución"), ("revisar", "mirar si funcionó"), ("reparar", "arreglar un daño"), ("confianza", "sentir que puedo contar con el otro")],
    worked=[
        {"title": "Un acuerdo claro", "problem": "Ana y Luis quieren el mismo columpio. Acuerdan: «Ana 10 veces y luego Luis». ¿Es claro?", "steps": ["Dice quién va primero.", "Dice cuántas veces.", "Dice quién sigue."], "answer": "Sí, es claro"},
        {"title": "Revisar", "problem": "El acuerdo de turnos no funcionó porque uno se pasó del tiempo. ¿Qué hacen?", "steps": ["Miran qué pasó.", "Agregan una regla: contar en voz alta.", "Prueban otra vez."], "answer": "Cambiar el acuerdo y probar otra vez"},
    ],
    mistakes=[
        {"wrong": "Hacer un acuerdo y no revisarlo.", "why": "Se piensa que ya terminó.", "fix": "Revisa al día siguiente cómo fue."},
        {"wrong": "Hacer un acuerdo sin decir quién hace qué.", "why": "Se habla en general.", "fix": "Di quién, qué y cuándo."},
    ],
    tiers={
        "recovery": [
            ex("¿Un acuerdo lo deciden los dos?", "Sí", "Es una decisión conjunta."),
            ex("Después de probar un acuerdo, ¿qué haces: revisar o olvidarlo?", "Revisar", "Se ve si funcionó."),
            ex("¿Reparar significa arreglar el daño?", "Sí", "Se hace algo para arreglarlo."),
        ],
        "understand": [
            ex("¿Qué dice un acuerdo claro?", "Quién hace qué y cuándo", "Así no hay dudas."),
            ex("¿Por qué conviene revisar el acuerdo?", "Para ver si funcionó y mejorarlo", "Se puede cambiar."),
            ex("¿Qué pasa si un acuerdo no funciona?", "Se elige otra solución", "No es un fracaso."),
        ],
        "apply": [
            ex("Mía y Beto acuerdan turnarse con la pelota. Escribe un acuerdo claro.", "Por ejemplo: «Mía 5 minutos, luego Beto 5 minutos»", "Dice quién y cuánto."),
            ex("Dani rompió sin querer el dibujo de Eva. Escribe una reparación posible.", "Por ejemplo: «Te ayudo a hacer otro»", "Arregla el daño."),
            ex("Pedro y Rosa probaron un acuerdo. Escribe una pregunta para revisarlo.", "Por ejemplo: «¿Funcionó el acuerdo para los dos?»", "Revisa el resultado."),
        ],
        "reason": [
            ex("Tomás y Sofía acordaron «jugar juntos» pero no dijeron a qué. ¿Falta algo?", "Sí, falta decir a qué jugar", "No es un acuerdo claro."),
            ex("Carla y Luis revisaron el acuerdo y vieron que uno se sentía mal. ¿Qué hacen?", "Lo cambian", "Quieren que sirva a los dos."),
        ],
        "challenge": [
            arith("Mía y Luis acuerdan que cada uno use el columpio 10 minutos. ¿Cuántos minutos usan el columpio entre los dos?", "10+10", "Diez minutos para cada uno."),
            ex("Hay tres pasos: elegir, probar y revisar. Ordénalos: A) revisar, B) elegir, C) probar.", "B, C, A", "Primero elijo, luego pruebo y después reviso."),
        ],
    },
    context=[ex("Ana y Beto acordaron turnarse el columpio. Al día siguiente, Beto se quedó mucho tiempo. Ana dijo: «Revisemos el acuerdo». ¿Qué hizo Ana?", "Revisó el acuerdo", "Miró si funcionó.")],
    selfcheck=[ex("¿Debo probar y revisar un acuerdo?", "Sí", "Así el acuerdo puede mejorar."), ex("¿Reparar es parte del acuerdo?", "Sí", "Ayuda a recuperar la confianza."), ex("¿Un acuerdo puede cambiar?", "Sí", "Si no funciona, se mejora.")],
    open_task=task("Lee el conflicto: «Luis y Mía quieren hacer su torre en la misma mesa pequeña y se molestan los brazos». Escribe un acuerdo claro con quién, qué y cuándo (por ejemplo: «Luis a la izquierda, Mía a la derecha, y revisamos mañana»). Agrega cómo lo revisarían.", "«Luis arma su torre a la izquierda y Mía a la derecha. Mañana preguntamos si funcionó».", ["acuerdo con quién, qué y cuándo", "incluye cómo revisar", "cuida a los dos"], ["acuerdo escrito", "dibujo de la mesa dividida"], ["acuerdo vago", "no incluir revisión"], "Reconoce lo claro del acuerdo y sugiere agregar una forma de revisión."),
    reinforce="Haz con un adulto un acuerdo sencillo para hoy y revísalo en la noche.",
    extend="Escribe un acuerdo para tres niños que comparten una caja de lápices.",
)

# ================================================================ OA 07
register(
    OA7, 1,
    materials="Una hoja, lápiz y las descripciones de grupos escritas en cada ejercicio.",
    use="Aprenderé que existen muchos tipos de grupos y que están formados por personas distintas. Sirve para respetar a todos y ubicar mis propios grupos.",
    prior=["Sé que pertenezco a una familia y a un curso.", "Sé que las personas son distintas."],
    explain=[
        "Un grupo es un conjunto de personas que comparten algo. Tu familia es un grupo. Tu curso es otro grupo. También puede haber un grupo de vecinos, un equipo de fútbol o un taller de arte. Una persona puede pertenecer a varios grupos a la vez.",
        "Los grupos están formados por personas diferentes. Hay familias con una mamá y un papá, con una sola persona adulta, con abuelos, con tíos o con otras personas que cuidan. Todas son familias. No podemos suponer cómo es alguien por el grupo al que pertenece.",
        "Un estereotipo es creer que todas las personas de un grupo son iguales, como decir «todos los niños juegan a la pelota». Eso no es cierto: en cada grupo hay personas con gustos distintos. Mirar a cada persona sin etiquetas es parte del respeto.",
    ],
    vocab=[("grupo", "personas que comparten algo"), ("pertenecer", "formar parte de un grupo"), ("diverso", "con personas distintas"), ("estereotipo", "creer que todos los de un grupo son iguales"), ("respeto", "tratar bien a todos")],
    worked=[
        {"title": "Identificar un grupo", "problem": "Ana juega fútbol con sus compañeros de equipo los sábados. ¿Qué grupo es?", "steps": ["Comparten una actividad: fútbol.", "Se juntan los sábados.", "Es un equipo, que es un grupo."], "answer": "Un equipo de fútbol"},
        {"title": "Evitar un estereotipo", "problem": "Beto dice: «Todas las niñas juegan con muñecas». ¿Es cierto?", "steps": ["Hay niñas a quienes les gusta jugar con muñecas, y a otras no.", "Hay niños a quienes sí.", "No todos los de un grupo son iguales."], "answer": "No, es un estereotipo"},
    ],
    mistakes=[
        {"wrong": "Pensar que todas las familias son iguales.", "why": "Se conoce solo la propia.", "fix": "Hay muchas formas de familia y todas valen."},
        {"wrong": "Suponer cómo es alguien por su grupo.", "why": "Se generaliza.", "fix": "Pregunta y conoce a la persona."},
    ],
    tiers={
        "recovery": [
            ex("Tu curso, ¿es un grupo?", "Sí", "Reúne personas con algo en común."),
            ex("¿Tu familia es un grupo?", "Sí", "Comparten la vida diaria."),
            ex("¿Una persona puede estar en más de un grupo?", "Sí", "Puede ser de su familia y de su curso."),
        ],
        "understand": [
            ex("¿Qué es un grupo?", "Personas que comparten algo", "Pueden compartir actividad, lugar o cariño."),
            ex("¿Todas las familias son iguales?", "No", "Hay familias de distintas formas."),
            ex("En Orientación, ¿qué es un estereotipo?", "Creer que todos los de un grupo son iguales", "Es una idea que simplifica."),
        ],
        "apply": [
            ex("De esta lista: familia, curso, equipo de fútbol, nube. ¿Cuál no es un grupo de personas?", "Nube", "No es un conjunto de personas."),
            ex("Mía vive con su abuela y su tío. ¿Es una familia?", "Sí", "Las personas que se cuidan forman una familia."),
            ex("Tomás va a un taller de dibujo con otros niños. ¿Qué tipo de grupo es?", "Un taller o grupo de actividad", "Los niños comparten la actividad de dibujar."),
        ],
        "reason": [
            ex("Eva dice: «Los niños nunca lloran». ¿Es cierto?", "No", "Todos los niños pueden llorar."),
            ex("Pedro cree que todos los vecinos de su calle son iguales. ¿Qué puede hacer para conocerlos?", "Saludarlos y preguntar", "Cada persona es distinta."),
        ],
        "challenge": [
            ex("Sofía está en tres grupos: su familia, su curso y su equipo. ¿En cuántos grupos está?", "3", "Cuenta cada grupo."),
            ex("Un curso tiene 20 niños. Un taller tiene 5 niños que ya están en ese curso. ¿Cuántos niños distintos hay si juntas curso y taller?", "20", "Los del taller ya están contados en el curso."),
        ],
    },
    context=[ex("Carla dice a un compañero nuevo: «Seguro te gusta el fútbol porque eres niño». El compañero dice: «A mí me gusta dibujar». ¿Qué aprendió Carla?", "Que no se puede suponer lo que le gusta a alguien", "Los gustos son personales.")],
    selfcheck=[ex("¿Hay familias de distintas formas?", "Sí", "Todas son familias."), ex("¿Puedo pertenecer a varios grupos?", "Sí", "Una persona tiene muchos grupos."), ex("¿Los estereotipos son ciertos para todos?", "No", "Cada persona es distinta.")],
    open_task=task("Mira estos cuatro grupos: una familia, un curso, un equipo y un taller. Dibuja una carita en cada uno y escribe una cosa distinta que podría tener cada persona del grupo, por ejemplo: «le gusta dibujar» o «le gusta correr». Así muestras que en un grupo hay personas diversas.", "Curso: Ana (le gusta dibujar), Luis (le gusta correr), Mía (le gusta leer).", ["dibuja los cuatro grupos", "muestra al menos dos gustos distintos por grupo", "no usa estereotipos"], ["hoja con cuatro grupos", "frases de gustos distintos"], ["poner a todos iguales", "decir que alguien no pertenece"], "Reconoce la variedad que mostró y pregunta qué grupos le gustan más."),
    reinforce="Cuenta cuántas personas hay en tu familia y qué le gusta a cada una.",
    extend="Escribe dos grupos en los que estás y qué haces en cada uno.",
)

register(
    OA7, 2,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio.",
    use="Aprenderé que en un grupo recibo cosas y también aporto. Sirve para entender que todos ayudamos a que el grupo funcione.",
    prior=["Sé que pertenezco a grupos.", "Sé ayudar."],
    explain=[
        "En un grupo, las personas se dan cosas unas a otras. Esto se llama reciprocidad. Recibes ayuda, compañía o enseñanza, y también aportas: ayudas, compartes ideas, tratas bien a los demás.",
        "Los aportes pueden ser pequeños y valiosos. En el curso puedes aportar prestando un lápiz, contando una idea o escuchando. En tu familia puedes aportar ordenando tu pieza o cuidando a una mascota.",
        "Todos tenemos algo que aportar y algo que recibir. Si solo recibimos y nunca aportamos, el grupo se cansa. Si solo aportamos y nunca recibimos, nos agotamos. Un buen grupo cuida que sea justo.",
    ],
    vocab=[("reciprocidad", "dar y recibir"), ("aporte", "lo que yo doy al grupo"), ("recibir", "tomar lo que otros dan"), ("colaborar", "trabajar juntos"), ("justo", "equilibrado para todos")],
    worked=[
        {"title": "Identificar aportes", "problem": "En el curso, Ana presta lápices, Beto cuenta chistes y Mía ayuda a ordenar. ¿Qué aporta cada uno?", "steps": ["Ana aporta materiales.", "Beto aporta alegría.", "Mía aporta orden."], "answer": "Materiales, alegría y orden"},
        {"title": "Dar y recibir", "problem": "Luis ayudó a Ana con un cordón y ella le prestó su goma. ¿Qué hicieron?", "steps": ["Luis ayudó: aportó.", "Ana prestó: aportó también.", "Los dos dieron y recibieron."], "answer": "Reciprocidad: los dos dieron y recibieron"},
    ],
    mistakes=[
        {"wrong": "Pensar que solo los grandes aportan.", "why": "Se cree que aportar es hacer cosas difíciles.", "fix": "Un gesto pequeño también es un aporte."},
        {"wrong": "Pedir siempre y no dar nunca.", "why": "Es cómodo recibir.", "fix": "Piensa qué puedes dar tú también."},
    ],
    tiers={
        "recovery": [
            ex("Prestar un lápiz, ¿es un aporte?", "Sí", "Es dar algo al grupo."),
            ex("Recibir ayuda de un compañero, ¿es parte de un grupo?", "Sí", "Los grupos se apoyan."),
            ex("¿Escuchar a otros puede ser un aporte?", "Sí", "Ayuda a que todos se sientan tomados en cuenta."),
        ],
        "understand": [
            ex("En Orientación: ¿Qué es la reciprocidad?", "Dar y recibir", "Los dos lados ayudan."),
            ex("¿Todos pueden aportar algo?", "Sí", "Cada persona tiene algo para dar."),
            ex("¿Por qué conviene que todos aporten?", "Para que el grupo funcione mejor", "Cuando todos suman, el trabajo es más fácil."),
        ],
        "apply": [
            ex("En una familia, Tomás pone la mesa. ¿Qué aporta?", "Ayuda en las tareas de la casa", "Es un aporte concreto."),
            ex("Rosa recibió una explicación de su amiga. Escribe un aporte que puede dar a cambio.", "Por ejemplo: prestar su cuaderno", "Corresponde con dar algo."),
            ex("En el equipo, Pedro anima a los demás. ¿Qué aporta?", "Ánimo", "Anima a que todos jueguen."),
        ],
        "reason": [
            ex("Eva siempre recibe ayuda pero nunca ayuda. ¿Qué podría cambiar?", "Ofrecer ayuda a otros", "Así hay equilibrio."),
            ex("Dani aporta mucho y se cansó. ¿Qué puede decir al grupo?", "Que necesita ayuda también", "Todos deben aportar."),
        ],
        "challenge": [
            arith("En un grupo de 3 niños, cada uno trae 2 lápices para compartir. ¿Cuántos lápices tiene el grupo?", "2+2+2", "Dos lápices por cada niño."),
            arith("Sofía trajo 3 hojas y Luis trajo 4 hojas para el trabajo. ¿Cuántas hojas aportaron entre los dos?", "3+4", "Se juntan las hojas de los dos."),
        ],
    },
    context=[ex("En el curso hay que ordenar la biblioteca. Ana trae los libros, Beto los ordena y Mía limpia la mesa. ¿Cuántos aportan?", "3", "Cada uno hace una parte.")],
    selfcheck=[ex("¿Un aporte puede ser pequeño?", "Sí", "Un gesto pequeño también ayuda."), ex("¿En un grupo se da y se recibe?", "Sí", "Eso es reciprocidad."), ex("¿Todos aportan lo mismo?", "No", "Cada uno aporta algo distinto.")],
    open_task=task("Elige un grupo (tu familia, tu curso o tu equipo). Haz una tabla con dos columnas: «Lo que recibo» y «Lo que aporto». En cada columna escribe o dibuja una cosa. Por ejemplo: recibo ayuda con la tarea; aporto buen humor.", "Curso: recibo ayuda de mis compañeros; aporto un lápiz extra.", ["tabla con dos columnas", "al menos un recibo y un aporto", "no compara con otros"], ["tabla escrita o dibujada"], ["solo escribir lo que recibe", "poner aportes imposibles"], "Valora el aporte propuesto y pregunta cómo podría darlo esta semana."),
    reinforce="Haz hoy un aporte pequeño a tu familia.",
    extend="Escribe tres aportes distintos que un niño de 6 años puede dar a su curso.",
)

register(
    OA7, 3,
    materials="Una hoja, lápiz y la lista de tareas escrita en cada ejercicio.",
    use="Aprenderé a asumir un rol concreto en un grupo y cumplirlo. Sirve para que el trabajo salga bien y todos participen.",
    prior=["Sé que en un grupo todos aportan.", "Sé trabajar con otros."],
    explain=[
        "Un rol es una tarea concreta que te toca hacer en un grupo. Por ejemplo, en una actividad en grupo uno reparte los materiales, otro cuenta cuántos vasos hay, otro ordena al final y otro dice cómo se hizo. Cada rol es importante.",
        "Para cumplir un rol, escucha cuál es tu tarea, hazla con cuidado y avisa si necesitas ayuda. Cuando cumples tu tarea, el grupo avanza. Si alguien no cumple, se puede conversar con amabilidad: «¿Necesitas ayuda con tu tarea?».",
        "Los roles se pueden turnar. Hoy te toca repartir y mañana otro. Así todos aprenden y nadie hace siempre lo mismo. Elegir un rol de manera justa y con acuerdo evita discusiones.",
    ],
    vocab=[("rol", "tarea concreta que me toca en un grupo"), ("cumplir", "hacer lo que me tocó"), ("turnar", "cambiar quién hace cada tarea"), ("participar", "ser parte activa del grupo"), ("equipo", "grupo que trabaja junto")],
    worked=[
        {"title": "Asignar roles", "problem": "Un grupo de 3 niños arma un afiche. Roles: dibujar, escribir y pegar. ¿Cómo los asignan?", "steps": ["Cada uno elige un rol distinto.", "Se asegura que alguien haga cada uno.", "Turnan los roles la próxima vez."], "answer": "Cada niño un rol y luego los turnan"},
        {"title": "Cumplir el rol", "problem": "A Mía le tocó repartir las hojas. Se le olvidó una persona. ¿Qué hace?", "steps": ["Se da cuenta del error.", "Entrega una hoja a quien faltó.", "Revisa que todos tengan."], "answer": "Repartir la hoja que faltó"},
    ],
    mistakes=[
        {"wrong": "Querer hacer todos los roles.", "why": "Se cree que así sale mejor.", "fix": "Deja que otros hagan su parte."},
        {"wrong": "No hacer su rol esperando que otro lo haga.", "why": "Se confía en que alguien lo hará.", "fix": "Haz tu rol o avisa que necesitas ayuda."},
    ],
    tiers={
        "recovery": [
            ex("Repartir los materiales, ¿es un rol?", "Sí", "Es una tarea concreta."),
            ex("¿Cada integrante del grupo puede tener un rol?", "Sí", "Así todos participan en el trabajo."),
            ex("Si necesitas ayuda con tu rol, ¿qué haces?", "La pido", "Se avisa al grupo."),
        ],
        "understand": [
            ex("En Orientación, ¿qué es un rol?", "Una tarea concreta en un grupo", "Cada uno tiene la suya."),
            ex("¿Por qué conviene turnar los roles?", "Para que todos aprendan y sea justo", "Así nadie hace siempre lo mismo."),
            ex("¿Qué pasa si nadie cumple su rol?", "El grupo no avanza", "Cada parte es necesaria."),
        ],
        "apply": [
            ex("Un grupo de 4 prepara una exposición. Roles: dibujar, escribir, hablar y ordenar. ¿Cuántos roles hay?", "4", "Hay uno por niño."),
            ex("A Tomás le tocó ordenar. Terminada la tarea, ¿qué hace con los materiales?", "Los guarda en su lugar", "Ese es el rol de ordenar."),
            ex("A Rosa le tocó anotar las ideas. Escribe cómo avisa si necesita ayuda.", "Por ejemplo: «¿Alguien me ayuda a anotar?»", "Pide ayuda con claridad."),
        ],
        "reason": [
            ex("Pedro no hizo su rol y el grupo se atrasó. ¿Qué puede decirle un compañero con amabilidad?", "«¿Necesitas ayuda con tu tarea?»", "Ofrece apoyo sin retar."),
            ex("Ana hizo todos los roles y el grupo no la dejó descansar. ¿Qué falló?", "No repartieron los roles", "Cada uno debe hacer su parte."),
        ],
        "challenge": [
            ex("Tres niños se turnan 3 roles, uno nuevo por día. ¿En cuántos días cada niño habrá hecho los 3 roles?", "3", "Cada día cambia un rol, hasta completar los tres."),
            arith("En un grupo de 4 niños ya hay 3 con rol asignado. ¿Cuántos niños todavía no tienen rol?", "4-3", "Se quitan los que ya tienen rol."),
        ],
    },
    context=[ex("Para plantar porotos, Luis trae la tierra, Eva pone los porotos y Dani los riega con un poco de agua. ¿Cuántos roles hay?", "3", "Cada niño tiene una tarea.")],
    selfcheck=[ex("¿Mi rol es importante?", "Sí", "El grupo lo necesita."), ex("¿Los roles se pueden turnar?", "Sí", "Así todos participan."), ex("¿Qué hago si no entiendo mi rol?", "Pregunto", "Pedir aclaración ayuda.")],
    open_task=task("Imagina un grupo de tres que va a hacer un cartel con el título «Cuidemos el patio». Los roles son: dibujar, escribir y pegar. Escribe quién hace cada rol (puedes usar los nombres Ana, Beto y Mía) y qué pueden decir para turnarse la próxima vez.", "Ana dibuja, Beto escribe, Mía pega. Próxima vez: «Ahora yo dibujo y tú escribes».", ["asigna los tres roles", "usa un rol por persona", "propone cómo turnar"], ["lista de roles", "dibujo del grupo"], ["asignar dos roles a uno solo siempre", "no incluir a un integrante"], "Reconoce el reparto y ayuda a pensar cómo cambiar roles."),
    reinforce="Asume un rol en tu casa hoy, como poner la mesa, y cúmplelo.",
    extend="Escribe tres roles para organizar una fiesta de curso.",
)

register(
    OA7, 4,
    materials="Una hoja, lápices de colores y las fichas de personajes escritas en cada ejercicio.",
    use="Aprenderé a hablar de las semejanzas y diferencias entre grupos con respeto. Sirve para sentirme parte de varios grupos y valorar a otros.",
    prior=["Sé que pertenezco a distintos grupos.", "Sé qué es un estereotipo."],
    explain=[
        "Cada persona pertenece a varios grupos al mismo tiempo. Mía pertenece a su familia, a su curso, a su barrio y a un taller de baile. Cada grupo es una pertenencia. Tener varias pertenencias hace que cada persona sea única.",
        "Entre las personas hay semejanzas y diferencias. Dos niños pueden compartir el curso y tener gustos distintos. Dos niños de cursos distintos pueden compartir el mismo juego favorito. Las semejanzas nos acercan y las diferencias nos enseñan.",
        "Para hablar de diferencias con respeto, usa palabras que no ofendan: «A ti te gusta el baile y a mí el fútbol». No digas «eso es raro». Una pregunta amable ayuda: «¿Me cuentas cómo es tu grupo?».",
    ],
    vocab=[("pertenencia", "grupo al que pertenezco"), ("semejanza", "algo parecido"), ("diferencia", "algo distinto"), ("único", "que no hay otro igual"), ("respetar", "tratar bien lo diferente")],
    worked=[
        {"title": "Semejanza y diferencia", "problem": "Ana y Luis están en el mismo curso. A Ana le gusta dibujar y a Luis jugar a la pelota. ¿Qué es semejanza y qué es diferencia?", "steps": ["Semejanza: los dos están en el mismo curso.", "Diferencia: sus gustos son distintos."], "answer": "Semejanza: el curso. Diferencia: los gustos"},
        {"title": "Hablar con respeto", "problem": "Beto dice: «Tu juego es raro». ¿Cómo puede decirlo con respeto?", "steps": ["La palabra «raro» ofende.", "Puede decir: «No conozco ese juego; ¿me lo explicas?»."], "answer": "«No conozco ese juego; ¿me lo explicas?»"},
    ],
    mistakes=[
        {"wrong": "Decir que algo diferente es malo o raro.", "why": "Nos parece extraño lo que no conocemos.", "fix": "Pregunta con curiosidad."},
        {"wrong": "Pensar que somos de un solo grupo.", "why": "Se piensa solo en el curso.", "fix": "Recuerda tus otras pertenencias."},
    ],
    tiers={
        "recovery": [
            ex("Mía está en su familia y en su curso. ¿Pertenece a un grupo o a más de uno?", "A más de uno", "Tiene varias pertenencias."),
            ex("Dos niños con gustos distintos, ¿tienen una diferencia?", "Sí", "Sus gustos no coinciden."),
            ex("Dos niños que juegan al mismo juego, ¿tienen una semejanza?", "Sí", "Comparten un juego."),
        ],
        "understand": [
            ex("En esta clase, ¿qué significa «pertenencia» (un grupo al que pertenezco o un objeto)?", "Un grupo al que pertenezco", "Puede ser familia, curso o equipo."),
            ex("¿Por qué las diferencias pueden enseñarnos algo?", "Porque conocemos cosas nuevas", "Aprendemos de lo distinto."),
            ex("¿Qué palabra evitas para hablar de algo distinto: «interesante» o «raro»?", "«Raro»", "Esa palabra puede ofender a otros."),
        ],
        "apply": [
            ex("Tomás va a un taller de teatro y Carla a uno de música. Escribe una semejanza.", "Por ejemplo: los dos van a un taller", "Los dos comparten una actividad parecida."),
            ex("Rosa vive con su mamá y Eva vive con sus abuelos. Escribe una diferencia respetuosa.", "Por ejemplo: «Rosa vive con su mamá y Eva con sus abuelos»", "Describe sin juzgar."),
            ex("Dani no conoce el juego de Pedro. Escribe una pregunta amable.", "Por ejemplo: «¿Me enseñas cómo se juega?»", "Muestra interés y curiosidad respetuosa."),
        ],
        "reason": [
            ex("Sofía dice: «Los del otro curso son raros». ¿Qué podría decir mejor?", "«Los del otro curso juegan distinto; me gustaría conocerlos»", "Respeta la diferencia."),
            ex("Luis se siente solo porque sus gustos son distintos al curso. ¿Qué puede recordar?", "Que pertenece a otros grupos también", "Tiene más de una pertenencia."),
        ],
        "challenge": [
            arith("Beto está en 3 grupos: su familia, su curso y su equipo. Mía está en 2 grupos: su familia y su curso. ¿Cuántos grupos más tiene Beto que Mía?", "3-2", "El equipo es el grupo extra."),
            arith("Ana y Dani comparten 2 grupos y cada uno tiene 1 grupo distinto. ¿Cuántos grupos en total tiene cada uno?", "2+1", "Dos compartidos y uno propio."),
        ],
    },
    context=[ex("Un niño nuevo llegó al curso y juega a algo que Carla no conoce. Carla le dice: «Cuéntame cómo se juega». ¿Qué hizo bien?", "Preguntó con respeto", "Mostró interés en lo distinto.")],
    selfcheck=[ex("¿Una persona puede tener varias pertenencias?", "Sí", "Está en varios grupos."), ex("¿Las diferencias se respetan?", "Sí", "Todas las personas valen igual."), ex("¿Qué pregunta amable puedo hacer?", "«¿Me cuentas más?»", "Muestra interés por el otro.")],
    open_task=task("Dibuja tres círculos que se cruzan: «mi familia», «mi curso» y «un grupo que me gusta» (por ejemplo, un equipo, un taller o mis vecinos). En el centro escribe o dibuja una cosa que te une a esos grupos. Al lado escribe una diferencia con una persona de tu curso, usando palabras de respeto.", "En el centro: me gusta ayudar. Diferencia: a Beto le gusta el fútbol y a mí el dibujo.", ["dibuja los tres grupos", "muestra una semejanza o rasgo común", "describe una diferencia sin ofender"], ["dibujo de círculos", "frase con la diferencia"], ["usar «raro» o «malo»", "no incluir ninguna pertenencia"], "Valora la pertenencia múltiple y sugiere preguntas amables sobre las diferencias."),
    reinforce="Cuéntale a alguien de otro grupo algo que tengas en común con él.",
    extend="Escribe tres cosas que te gustaría preguntar a un niño de otro curso para conocerlo.",
)

# ================================================================ OA 08
register(
    OA8, 1,
    materials="Una hoja, lápiz y las listas de útiles escritas en cada ejercicio.",
    use="Aprenderé a seleccionar y cuidar mis útiles para cada actividad. Sirve para empezar rápido y trabajar tranquilo.",
    prior=["Sé qué útiles uso en clase.", "Sé guardar mis cosas."],
    explain=[
        "Los útiles son los materiales que usas para aprender: lápiz, goma, cuaderno, tijera, pegamento, regla, estuche. Cada actividad necesita algunos. Para escribir necesitas lápiz y cuaderno. Para recortar, tijera y papel.",
        "Preparar lo necesario es revisar con anticipación qué materiales usarás y ponerlos en tu mochila o sobre tu mesa. Una lista ayuda: lees cada útil y lo marcas con una cruz cuando lo tienes. Así no se te olvida nada.",
        "Cuidar los útiles es usarlos bien y guardarlos al final. Mantén los lápices afilados, cierra el pegamento y guarda la tijera cerrada en su estuche. Útiles cuidados duran más y se pueden usar todos los días.",
    ],
    vocab=[("útiles", "materiales para aprender"), ("preparar", "dejar todo listo antes de empezar"), ("lista", "papel con cosas que no quiero olvidar"), ("revisar", "mirar si está todo"), ("cuidar", "usar bien y guardar")],
    worked=[
        {"title": "Elegir los útiles", "problem": "Hoy en clase van a pintar con témpera. ¿Qué útiles necesita Ana: pincel y delantal, o regla y calculadora?", "steps": ["Pintar usa pincel y témpera.", "Un delantal protege la ropa.", "Regla y calculadora no son para pintar."], "answer": "Pincel y delantal"},
        {"title": "Usar una lista", "problem": "La lista de Beto dice: lápiz, goma, cuaderno. Tiene en su mochila lápiz y cuaderno. ¿Qué falta?", "steps": ["Marca lápiz: sí.", "Marca cuaderno: sí.", "Falta la goma."], "answer": "La goma"},
    ],
    mistakes=[
        {"wrong": "Armar la mochila de última hora.", "why": "Se deja para después.", "fix": "Prepárala la noche antes con una lista."},
        {"wrong": "Dejar el pegamento abierto.", "why": "Se piensa que es rápido usarlo otra vez.", "fix": "Ciérralo siempre."},
    ],
    tiers={
        "recovery": [
            ex("¿Con qué escribes: lápiz o tijera?", "Lápiz", "El lápiz sirve para escribir."),
            ex("¿Qué útil sirve para recortar?", "La tijera", "Corta el papel."),
            ex("¿Una lista ayuda a no olvidar útiles?", "Sí", "Se revisa cada uno."),
        ],
        "understand": [
            ex("¿Qué es preparar lo necesario?", "Dejar todo listo antes de empezar", "Así no se pierde tiempo."),
            ex("¿Por qué conviene cuidar los útiles?", "Para que duren y se puedan usar siempre", "Un útil dañado ya no sirve."),
            ex("¿Cuándo conviene armar la mochila: la noche antes o a último momento?", "La noche antes", "Hay tiempo para revisar."),
        ],
        "apply": [
            ex("Para una clase de dibujo, Dani elige: lápices de colores, cuaderno y pelota. ¿Cuál no necesita?", "La pelota", "No es un útil de dibujo."),
            ex("La lista dice: estuche, cuaderno, agua y colación. Mía tiene estuche, cuaderno y colación. ¿Qué le falta?", "El agua", "Falta una cosa."),
            ex("Luis termina de pegar. Escribe cómo cuida el pegamento.", "Por ejemplo: lo cierra y lo guarda", "Así no se seca."),
        ],
        "reason": [
            ex("Eva olvidó la regla y no puede hacer la tarea. ¿Qué pudo hacer la noche anterior?", "Revisar la lista y armar la mochila", "Prevenir el olvido."),
            ex("Pedro guarda la tijera con las puntas hacia arriba. ¿Qué puede pasar?", "Alguien podría pincharse", "Es mejor guardarla en su estuche."),
        ],
        "challenge": [
            arith("La lista de la semana tiene 5 útiles y Sofía ya tiene 3. ¿Cuántos le faltan?", "5-3", "Se quitan los que ya tiene."),
            arith("Tomás debe llevar 2 lápices, 1 goma y 1 cuaderno. ¿Cuántos útiles son?", "2+1+1", "Se suman todos los útiles."),
        ],
    },
    context=[ex("Mañana hay clase de ciencias con lupa, cuaderno y lápiz. Ana arma su mochila con lupa y cuaderno. ¿Qué le falta?", "El lápiz", "La lista pide lupa, cuaderno y lápiz.")],
    selfcheck=[ex("¿Una lista ayuda a preparar la mochila?", "Sí", "Se revisa cada útil."), ex("¿Los útiles se cuidan?", "Sí", "Duran más tiempo."), ex("¿Cuándo preparo la mochila?", "Con anticipación", "Hay tiempo para revisar.")],
    open_task=task("Esta es la lista del día: cuaderno, estuche con lápiz y goma, botella de agua y colación. Dibuja tu mochila y las cuatro cosas que van dentro. Marca con una cruz cada una cuando la tengas. Escribe una cosa que harás para cuidar tus útiles.", "Mochila con cuaderno, estuche, agua y colación, todas marcadas. Cuidado: cerrar el estuche.", ["dibuja los cuatro elementos", "usa una marca de revisión", "dice cómo cuidar un útil"], ["dibujo de la mochila", "lista marcada"], ["olvidar una cosa de la lista", "no mencionar cuidado"], "Reconoce lo que preparó y recuerda hacerlo la noche anterior."),
    reinforce="Revisa tu mochila hoy y comprueba que tengas todo lo de la lista.",
    extend="Escribe una lista de cinco útiles para una clase de arte.",
)

register(
    OA8, 2,
    materials="Una hoja, lápiz y las descripciones de espacios escritas en cada ejercicio.",
    use="Aprenderé a ordenar mi espacio y mis materiales antes de trabajar. Sirve para concentrarme y encontrar rápido lo que necesito.",
    prior=["Sé que debo guardar mis útiles.", "Sé qué necesito para una tarea."],
    explain=[
        "Un espacio ordenado ayuda a trabajar. Si tu mesa está llena de cosas, cuesta encontrar lo que necesitas y te distraes. Ordenar significa dejar sobre la mesa solo lo que usarás y guardar lo demás.",
        "Para ordenar, sigue pasos sencillos: primero saca de la mesa lo que no necesitas, luego pon lo que sí usarás al alcance de tu mano y, al final, deja un espacio libre para trabajar. Cuando terminas, guardas todo en su lugar.",
        "Cada cosa tiene su lugar: los lápices en el estuche, los cuadernos en la mochila y los libros en el estante. Tener lugares fijos ayuda a encontrar las cosas sin perder tiempo. Un adulto puede ayudarte a ponerles etiquetas con dibujos.",
    ],
    vocab=[("ordenar", "poner cada cosa en su lugar"), ("espacio", "el lugar donde trabajo"), ("distraerse", "dejar de poner atención"), ("al alcance", "cerca de mi mano"), ("lugar fijo", "sitio donde siempre guardo algo")],
    worked=[
        {"title": "Preparar la mesa", "problem": "Luis va a dibujar. Su mesa tiene un cuaderno de matemática, una botella, lápices de colores y papel. ¿Qué deja sobre la mesa?", "steps": ["Para dibujar usa papel y lápices.", "Guarda el cuaderno de matemática.", "Deja la botella a un lado."], "answer": "Papel y lápices de colores"},
        {"title": "Cada cosa en su lugar", "problem": "Ana termina de trabajar y tiene lápices y un libro sobre la mesa. ¿Dónde los guarda?", "steps": ["Los lápices van al estuche.", "El libro va al estante."], "answer": "Lápices al estuche, libro al estante"},
    ],
    mistakes=[
        {"wrong": "Trabajar con la mesa llena de cosas.", "why": "Se empieza sin preparar el espacio.", "fix": "Deja solo lo necesario."},
        {"wrong": "Guardar todo mezclado.", "why": "Se hace rápido.", "fix": "Cada cosa en su lugar."},
    ],
    tiers={
        "recovery": [
            ex("¿Una mesa ordenada ayuda a concentrarse?", "Sí", "Hay menos distracciones."),
            ex("¿Dónde van los lápices: en el estuche o sueltos en el piso?", "En el estuche", "Es su lugar."),
            ex("Al terminar, ¿guardas todo en su lugar?", "Sí", "Así queda ordenado."),
        ],
        "understand": [
            ex("¿Por qué conviene dejar sobre la mesa solo lo que voy a usar?", "Para no distraerme y encontrar rápido", "Menos cosas, más atención."),
            ex("¿Qué significa «al alcance de la mano»?", "Cerca para tomarlo fácil", "No hay que estirarse ni buscar."),
            ex("¿Para qué sirve tener un lugar fijo para cada cosa?", "Para encontrarlas sin perder tiempo", "Siempre están en el mismo sitio."),
        ],
        "apply": [
            ex("Tomás hará una tarea de lectura. Sobre su mesa hay un libro, una pelota y un estuche. ¿Qué guarda?", "La pelota", "No sirve para leer."),
            ex("Eva ordena su mesa: primero saca lo que no necesita. ¿Qué hace después?", "Pone lo que sí necesita al alcance", "Es el segundo paso."),
            ex("Dani tiene un cuaderno, una tijera y un pegamento. ¿Dónde guarda la tijera cuando termina?", "En el estuche", "Es su lugar y es seguro."),
        ],
        "reason": [
            ex("Rosa no encuentra su cuaderno porque lo deja en distintos lugares. ¿Qué solución propones?", "Un lugar fijo para el cuaderno", "Así sabe dónde está."),
            ex("Pedro dice «ordenar es perder tiempo». ¿Qué le dirías?", "Que ordenar ahorra tiempo después", "Se encuentra rápido lo que se necesita."),
        ],
        "challenge": [
            arith("Hay 8 útiles sobre la mesa y solo 3 se usarán. ¿Cuántos hay que guardar?", "8-3", "Se quitan los que se usarán."),
            arith("Mía guarda 2 lápices, 1 goma y 3 hojas. ¿Cuántas cosas guardó en total?", "2+1+3", "Se suman todas las cosas."),
        ],
    },
    context=[ex("Carla va a pintar con témpera. En su mesa hay un cuaderno, un delantal y los pinceles. Para pintar, ¿qué guarda?", "El cuaderno", "No lo necesita para pintar.")],
    selfcheck=[ex("¿Ordenar el espacio ayuda a trabajar?", "Sí", "Así se evitan las distracciones."), ex("¿Cada cosa tiene su lugar?", "Sí", "Ayuda a encontrarlas."), ex("¿Qué dejo sobre la mesa?", "Solo lo necesario", "Así trabajo mejor.")],
    open_task=task("Dibuja una mesa con estas seis cosas: cuaderno, lápiz, goma, botella de agua, pelota y tijera. Rodea con un círculo las que usarías para escribir y tacha las que guardarías. Escribe dónde guardarías las tachadas.", "Círculo: cuaderno, lápiz, goma. Tacho: botella, pelota, tijera. Las guardo en la mochila y en el estuche.", ["marca lo necesario", "tacha lo que guarda", "dice dónde lo guarda"], ["dibujo de la mesa", "frase con los lugares"], ["circular todo", "no decir dónde guarda"], "Reconoce el orden y sugiere etiquetar los lugares."),
    reinforce="Ordena hoy tu espacio de estudio en tres pasos.",
    extend="Haz etiquetas con dibujos para tres lugares de tu pieza.",
)

register(
    OA8, 3,
    materials="Una hoja, lápiz y los casos escritos en cada ejercicio.",
    use="Aprenderé estrategias para seguir intentando cuando algo me cuesta y a pedir ayuda a tiempo. Sirve para no rendirme y aprender.",
    prior=["Sé que aprender cuesta a veces.", "Sé pedir ayuda."],
    explain=[
        "Cuando algo cuesta, no significa que no puedas. Significa que estás aprendiendo. Puedes seguir intentando con estrategias: respirar, releer las instrucciones, hacerlo por partes, mirar un ejemplo o probar otra manera.",
        "Si después de intentar sigue difícil, pide ayuda. Pide ayuda con claridad: «No entiendo esta parte, ¿me explicas?». Puedes pedirla a tu profesora, a un compañero o a un adulto de tu casa. Pedir ayuda es parte de aprender.",
        "Cuando algo se logra, puedes celebrarlo. Puedes decir: «Lo intenté y lo logré». También puedes decir: «Todavía no lo logro, pero sigo intentando». La palabra «todavía» recuerda que puedes mejorar.",
    ],
    vocab=[("intentar", "probar hacer algo"), ("estrategia", "una forma de lograr algo"), ("por partes", "dividir una tarea en pasos"), ("pedir ayuda", "decir que necesito apoyo"), ("todavía", "palabra que dice que aún puedo aprender")],
    worked=[
        {"title": "Hacerlo por partes", "problem": "Ana debe armar un cuadro con 4 dibujos y no sabe por dónde empezar. ¿Qué puede hacer?", "steps": ["Hace un dibujo a la vez.", "Terminado uno, empieza el siguiente.", "Al final, junta los cuatro."], "answer": "Hacerlo por partes"},
        {"title": "Pedir ayuda con claridad", "problem": "Luis no entiende cómo se arma una figura de papel. ¿Qué dice?", "steps": ["Dice qué parte no entiende.", "«No entiendo el segundo doblez, ¿me lo muestras?»."], "answer": "«No entiendo el segundo doblez, ¿me lo muestras?»"},
    ],
    mistakes=[
        {"wrong": "Decir «no puedo» y dejar la tarea.", "why": "Da vergüenza que cueste.", "fix": "Di «todavía no» y prueba otra estrategia."},
        {"wrong": "Pedir ayuda sin decir qué parte no entiendo.", "why": "Se dice «no entiendo nada».", "fix": "Señala la parte exacta."},
    ],
    tiers={
        "recovery": [
            ex("Cuando algo cuesta, ¿puedes seguir intentando?", "Sí", "Se aprende intentando."),
            ex("¿Pedir ayuda es parte de aprender?", "Sí", "Todos la necesitamos."),
            ex("¿Releer las instrucciones es una estrategia?", "Sí", "Ayuda a entender."),
        ],
        "understand": [
            ex("¿Qué significa «todavía no lo logro»?", "Que puedo seguir aprendiendo", "No es un final."),
            ex("¿Qué es hacer una tarea por partes?", "Dividirla en pasos pequeños", "Cada paso es más fácil."),
            ex("¿Cómo se pide ayuda con claridad?", "Diciendo qué parte no entiendo", "El otro sabe cómo ayudar."),
        ],
        "apply": [
            ex("Dani no puede cortar una forma. Escribe una estrategia que puede probar.", "Por ejemplo: cortar un lado a la vez", "Hace la tarea por partes."),
            ex("Mía no entiende la tarea. Escribe cómo pide ayuda a su profesora.", "Por ejemplo: «No entiendo el paso 2, ¿me explica?»", "Dice qué no entiende."),
            ex("Tomás está muy enojado porque no le sale. Elige una estrategia: respirar o romper el cuaderno.", "Respirar", "Ayuda a calmarse."),
        ],
        "reason": [
            ex("Eva dice «no puedo» y se rinde. ¿Qué frase le ayudaría?", "«Todavía no puedo, voy a intentar otra manera»", "Mantiene abierta la posibilidad."),
            ex("Pedro pidió ayuda y su compañero le dio la respuesta sin explicarle. ¿Aprendió?", "No mucho", "Es mejor que le expliquen."),
        ],
        "challenge": [
            arith("Una tarea tiene 6 pasos y Rosa ya hizo 4. ¿Cuántos le faltan?", "6-4", "Se quitan los pasos hechos."),
            ex("Sofía intentó 3 estrategias en orden: respirar, hacerlo por partes y pedir ayuda. ¿Cuál es la última?", "Pedir ayuda", "Es la tercera."),
        ],
    },
    context=[ex("A Carla le cuesta atar sus cordones. Respira, lo intenta de nuevo y, como sigue difícil, pide ayuda a su papá. ¿Qué estrategias usó?", "Respirar, intentar de nuevo y pedir ayuda", "Probó varias formas.")],
    selfcheck=[ex("¿Intentar de nuevo ayuda a aprender?", "Sí", "La práctica mejora."), ex("¿Puedo pedir ayuda si algo cuesta?", "Sí", "Es parte de aprender."), ex("¿Qué palabra recuerda que aún puedo mejorar?", "Todavía", "Muestra que es posible.")],
    open_task=task("Lee la situación: «A Beto le cuesta recortar un círculo con tijera». Elige tres estrategias de esta lista y ordénalas con 1, 2, 3: respirar, recortar un trozo a la vez, mirar un ejemplo, pedir ayuda a un adulto. Escribe la frase con la que Beto pediría ayuda.", "1) respirar, 2) recortar un trozo a la vez, 3) pedir ayuda. Frase: «No logro recortar la curva; ¿me muestras cómo?».", ["elige tres estrategias", "las ordena", "escribe una petición de ayuda clara"], ["lista numerada", "frase de ayuda"], ["elegir estrategias que no sirven", "pedir ayuda sin decir qué cuesta"], "Reconoce el intento y ayuda a precisar qué parte cuesta."),
    reinforce="Cuando algo te cueste hoy, di «todavía» y prueba una estrategia.",
    extend="Escribe una estrategia para cada una de estas dificultades: tarea larga, instrucción confusa, cansancio.",
)

register(
    OA8, 4,
    materials="Una hoja, lápiz y los cuadernos ficticios descritos en cada ejercicio.",
    use="Aprenderé a decir qué aprendí y cómo lo aprendí. Sirve para darme cuenta de mis avances y saber qué me ayuda a aprender.",
    prior=["Sé que aprender lleva tiempo.", "Sé contar lo que hice."],
    explain=[
        "Reconocer lo que aprendiste es mirar hacia atrás y ver qué sabes ahora que antes no sabías. Por ejemplo: «Antes no sabía atarme los cordones y ahora sí». Eso es un avance.",
        "También puedes decir cómo lo aprendiste. Puede ser practicando, mirando a otro, escuchando una explicación, equivocándote y probando de nuevo o pidiendo ayuda. Saber cómo aprendes te ayuda a aprender mejor la próxima vez.",
        "Para decirlo, usa dos frases: «Aprendí que…» y «Lo aprendí cuando…». Por ejemplo: «Aprendí a sumar con fichas. Lo aprendí cuando practiqué cada día». Compartirlo con alguien de confianza ayuda a celebrarlo.",
    ],
    vocab=[("aprendizaje", "lo que sé ahora y antes no sabía"), ("avance", "mejorar con el tiempo"), ("cómo aprendí", "lo que hice para aprender"), ("celebrar", "alegrarse por un logro"), ("equivocarse", "hacer algo mal y aprender de ello")],
    worked=[
        {"title": "Qué y cómo", "problem": "Ana dice: «Antes me costaba leer. Ahora leo una frase. Practiqué todos los días». ¿Qué aprendió y cómo?", "steps": ["Qué: a leer una frase.", "Cómo: practicando todos los días."], "answer": "Aprendió a leer una frase practicando"},
        {"title": "Aprender de un error", "problem": "Luis se equivocó al pegar una hoja al revés. Ahora pega con cuidado. ¿Cómo aprendió?", "steps": ["Se equivocó.", "Se dio cuenta.", "Lo volvió a intentar."], "answer": "Aprendió equivocándose y probando de nuevo"},
    ],
    mistakes=[
        {"wrong": "Pensar que no aprendí nada.", "why": "Los avances pequeños pasan desapercibidos.", "fix": "Mira qué haces ahora que antes no hacías."},
        {"wrong": "Pensar que equivocarse es malo.", "why": "Nos da vergüenza.", "fix": "Los errores enseñan."},
    ],
    tiers={
        "recovery": [
            ex("«Antes no sabía saltar la cuerda y ahora sí», ¿es un aprendizaje?", "Sí", "Aprendió algo nuevo."),
            ex("¿Practicar ayuda a aprender?", "Sí", "Mejora con repetición."),
            ex("¿Equivocarse puede enseñar?", "Sí", "Se aprende al corregir."),
        ],
        "understand": [
            ex("¿Qué es un avance?", "Mejorar con el tiempo", "Hago hoy algo que antes me costaba."),
            ex("¿Por qué conviene saber cómo aprendo?", "Para aprender mejor la próxima vez", "Repito lo que me funciona."),
            ex("¿Cuáles son las dos frases para contar un aprendizaje?", "«Aprendí que…» y «Lo aprendí cuando…»", "Dicen qué y cómo."),
        ],
        "apply": [
            ex("Dani aprendió a andar en bici practicando con su abuelo. Escribe qué aprendió.", "Aprendió a andar en bici", "Es lo que sabe ahora."),
            ex("Mía aprendió una canción escuchándola varias veces. Escribe cómo aprendió.", "Escuchándola varias veces", "Es lo que hizo para aprender."),
            ex("Completa: «Aprendí que ___. Lo aprendí cuando ___». Usa: Tomás aprendió a cerrar su mochila practicando.", "«Aprendí a cerrar mi mochila. Lo aprendí cuando practiqué»", "Incluye qué y cómo."),
        ],
        "reason": [
            ex("Rosa cree que no avanzó, pero antes no escribía su nombre y ahora sí. ¿Qué le dirías?", "Que sí avanzó", "Ahora escribe su nombre."),
            ex("Pedro aprendió a sumar usando fichas y su amigo usando los dedos. ¿Aprenden igual?", "No, cada uno aprende a su manera", "Cada persona tiene sus formas."),
        ],
        "challenge": [
            arith("Sofía aprendió 2 palabras en la primera semana y 3 en la segunda. ¿Cuántas palabras aprendió en total?", "2+3", "Se suman las dos semanas."),
            arith("En un cuaderno hay 10 hojas y Eva ya usó 4 para practicar. ¿Cuántas hojas le quedan?", "10-4", "Se quitan las hojas usadas."),
        ],
    },
    context=[ex("Beto antes no sabía amarrarse los zapatos. Hoy lo logra después de practicar tres semanas. Su profesora le pregunta qué aprendió y cómo. ¿Qué responde?", "Aprendió a amarrarse los zapatos practicando", "Responde qué y cómo.")],
    selfcheck=[ex("¿Aprender se nota en lo que puedo hacer?", "Sí", "Hago cosas que antes no podía."), ex("¿Se aprende de varias formas?", "Sí", "Practicando, escuchando, probando."), ex("¿Puedo celebrar mis avances?", "Sí", "Reconocer ayuda a seguir.")],
    open_task=task("Elige una de estas cosas que has aprendido: atarte los cordones, cantar una canción, escribir tu nombre, saltar la cuerda o leer una palabra. Completa las dos frases: «Aprendí que…» y «Lo aprendí cuando…». Dibuja cómo lo hiciste.", "«Aprendí a saltar la cuerda. Lo aprendí cuando practiqué todos los días». Dibujo: yo saltando la cuerda.", ["dice qué aprendió", "dice cómo lo aprendió", "dibuja o explica"], ["dos frases escritas o dichas", "dibujo"], ["no decir cómo lo aprendió", "decir que no aprendió nada"], "Reconoce el avance y pregunta qué le gustaría aprender ahora."),
    reinforce="Cuéntale a alguien algo que aprendiste esta semana.",
    extend="Escribe tres cosas que aprendiste este año y cómo las aprendiste.",
)

register(
    OA8, 5,
    materials="Una hoja, lápiz y la rutina ficticia escrita en cada ejercicio.",
    use="Aprenderé a planificar cómo empiezo, trabajo y termino una actividad por mi cuenta. Sirve para ser más autónomo y terminar lo que empiezo.",
    prior=["Sé preparar mis útiles y ordenar.", "Sé pedir ayuda."],
    explain=[
        "Una rutina autónoma es una secuencia de pasos que puedes hacer sin que te la recuerden. Tiene tres partes: inicio, trabajo y cierre. En el inicio, preparas tus útiles y tu espacio. En el trabajo, haces la tarea. En el cierre, revisas y guardas.",
        "Planificar es decidir los pasos antes de empezar. Por ejemplo, para hacer un dibujo: inicio, saco hoja y lápices; trabajo, dibujo con calma; cierre, escribo mi nombre y guardo los lápices. Un plan simple te da seguridad.",
        "Autónomo no significa que lo hagas todo solo. Si te trabas, pides ayuda. Autónomo es que sabes qué hacer primero, qué después y qué al final. Con práctica, la rutina se vuelve un hábito.",
    ],
    vocab=[("autónomo", "que puede hacer cosas por sí mismo"), ("inicio", "los primeros pasos"), ("trabajo", "la parte principal"), ("cierre", "los pasos del final"), ("hábito", "algo que se hace siempre")],
    worked=[
        {"title": "Inicio, trabajo y cierre", "problem": "Ana hará una tarea de dibujo. Ordena: A) guardar los lápices, B) sacar hoja y lápices, C) dibujar.", "steps": ["Inicio: sacar los materiales (B).", "Trabajo: dibujar (C).", "Cierre: guardar (A)."], "answer": "B, C, A"},
        {"title": "Una rutina de tarea", "problem": "Luis hará su tarea de lectura. Inicio: ordenar su mesa. Trabajo: leer una página. Cierre: ¿qué paso falta para terminar bien?", "steps": ["Cierre es revisar y guardar.", "Guarda el libro y cierra su mochila."], "answer": "Guardar el libro y la mochila"},
    ],
    mistakes=[
        {"wrong": "Empezar la tarea sin preparar los materiales.", "why": "Se quiere partir rápido.", "fix": "Primero prepara el inicio."},
        {"wrong": "Terminar sin guardar.", "why": "Se piensa que ya acabó.", "fix": "El cierre incluye guardar."},
    ],
    tiers={
        "recovery": [
            ex("¿Cuáles son las tres partes de una rutina?", "Inicio, trabajo y cierre", "Orden de la actividad."),
            ex("Sacar los materiales, ¿es inicio, trabajo o cierre?", "Inicio", "Es lo primero."),
            ex("Guardar los útiles, ¿es inicio, trabajo o cierre?", "Cierre", "Se hace al final."),
        ],
        "understand": [
            ex("¿Qué es una rutina autónoma?", "Una secuencia de pasos que hago sin que me la recuerden", "Yo sé qué sigue."),
            ex("¿Ser autónomo significa nunca pedir ayuda?", "No", "Pedir ayuda también es parte."),
            ex("¿Para qué sirve planificar?", "Para saber qué hacer primero y qué después", "Da seguridad para trabajar."),
        ],
        "apply": [
            ex("Dani hará una tarea de escritura. Escribe un paso de inicio.", "Por ejemplo: sacar el cuaderno y el lápiz", "Prepara los materiales."),
            ex("Mía hará la misma tarea. Escribe un paso de cierre.", "Por ejemplo: guardar el cuaderno en la mochila", "Termina la actividad."),
            ex("Ordena la rutina de Tomás: A) pintar, B) lavar los pinceles, C) preparar la témpera.", "C, A, B", "Prepara, pinta y limpia."),
        ],
        "reason": [
            ex("Eva empezó sin lápiz y tuvo que parar. ¿Qué parte de la rutina faltó?", "El inicio", "Faltó preparar los materiales."),
            ex("Pedro termina y deja todo sobre la mesa. ¿Qué parte olvidó?", "El cierre", "Falta guardar los materiales."),
        ],
        "challenge": [
            arith("Una rutina tiene 2 pasos de inicio, 3 de trabajo y 2 de cierre. ¿Cuántos pasos tiene en total?", "2+3+2", "Se suman los pasos de las tres partes."),
            arith("Sofía hace su rutina 2 días. Si cada día tiene 3 partes, ¿cuántas partes hace en total?", "3+3", "Tres partes cada día."),
        ],
    },
    context=[ex("Carla hará un cartel. Inicio: pone la cartulina en la mesa y saca los plumones. Trabajo: dibuja. ¿Qué hace en el cierre?", "Guarda los plumones y deja la mesa ordenada", "Cierra la actividad.")],
    selfcheck=[ex("¿Una rutina tiene inicio, trabajo y cierre?", "Sí", "Son sus tres partes."), ex("¿Ser autónomo es poder planificar?", "Sí", "Sabes qué hacer en cada paso."), ex("¿Qué hago si me trabo?", "Pido ayuda", "Es parte de aprender.")],
    open_task=task("Planifica tu rutina para hacer una tarea de dibujo. En tu hoja haz tres cuadros: «Inicio», «Trabajo» y «Cierre». En cada uno escribe o dibuja un paso. Elige de esta lista o usa uno tuyo: preparar lápices, dibujar con calma, guardar los útiles, ordenar la mesa, revisar mi dibujo.", "Inicio: preparar los lápices. Trabajo: dibujar con calma. Cierre: guardar los útiles.", ["tres cuadros completos", "pasos en el orden correcto", "usa su propio plan"], ["hoja con tres cuadros", "dibujo de los pasos"], ["poner el cierre primero", "dejar un cuadro vacío"], "Reconoce el orden y sugiere agregar un paso de revisión."),
    reinforce="Haz hoy tu rutina de tres partes al empezar una tarea.",
    extend="Haz una rutina de tres partes para preparar tu mochila.",
)
