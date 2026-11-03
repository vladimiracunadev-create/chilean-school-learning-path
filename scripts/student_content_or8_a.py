"""Cuaderno del estudiante, 8.º básico Orientación: OA 01 (autoconcepto positivo) y OA 02 (sexualidad integral, intimidad, respeto y fuentes confiables)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA1, OA2 = "OR08 OA 01", "OR08 OA 02"


def T(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def W(title, problem, steps, answer):
    return {"title": title, "problem": problem, "steps": steps, "answer": answer}


def M(wrong, why, fix):
    return {"wrong": wrong, "why": why, "fix": fix}


def lesson(oa, n, materials, use, prior, explain, vocab, worked, mistakes, R, U, A, Z, D, context, selfcheck, task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab, worked=worked, mistakes=mistakes,
        tiers={"recovery": R, "understand": U, "apply": A, "reason": Z, "challenge": D},
        context=context, selfcheck=selfcheck, open_task=task, reinforce=reinforce, extend=extend,
    )


# ================================================================ OA 01
lesson(
    OA1, 1,
    "Una hoja y un lápiz. El caso de Sofía, una estudiante inventada, y todas las frases están escritos en los ejercicios. No necesitas contar nada privado tuyo.",
    "Aprenderé a armar una representación positiva de mí con cuatro partes: características, motivaciones, intereses y capacidades, y a distinguir autoconcepto, autoestima e imagen corporal. Sirve para describirme con justicia mientras mi cuerpo cambia.",
    ["Conozco las cuatro partes del autoconcepto de 7.º básico.", "Sé que la pubertad trae cambios normales que ocurren a ritmos distintos."],
    [
        "Una representación positiva de ti no es una lista de elogios: es un retrato justo y completo. Tiene cuatro partes. Las características son cómo eres (soy constante). Las motivaciones son lo que te mueve (quiero que mi curso se apoye). Los intereses son lo que te gusta (el dibujo, el fútbol). Las capacidades son lo que puedes hacer o aprender a hacer (explicar un tema). Cada frase se vuelve más sólida si la apoyas con un hecho.",
        "Conviene separar tres ideas que se parecen. El autoconcepto es cómo te describes. La autoestima es cuánto te valoras, es decir, el cariño y el respeto que te tienes. La imagen corporal es cómo ves y sientes tu cuerpo. En la pubertad la imagen corporal se mueve mucho porque el cuerpo cambia rápido, pero no define todo tu autoconcepto: eres mucho más que tu apariencia.",
        "También existe una representación colectiva: cómo se describe un grupo, por ejemplo tu curso. Se construye entre todos, con aportes de cada persona, y reconoce fortalezas y cosas por mejorar. Una buena representación colectiva no deja a nadie fuera. Las dos, la individual y la colectiva, se pueden actualizar: lo que fuiste hace dos años no te limita hoy.",
    ],
    [("autoconcepto", "descripción que una persona hace de sí misma"), ("autoestima", "valoración y respeto que una persona se tiene"), ("imagen corporal", "cómo una persona ve y siente su propio cuerpo"), ("representación positiva", "retrato justo de uno mismo, con fortalezas y aspectos por mejorar, apoyado en hechos"), ("representación colectiva", "cómo se describe un grupo, construida entre todos sus miembros")],
    [
        W("Clasificar una frase", "Sofía escribe: «Quiero que mi curso gane el campeonato de debate». ¿Es una característica, una motivación o un interés?", ["La frase dice algo que ella desea lograr.", "Lo que mueve a actuar es una motivación.", "No describe cómo es ni solo lo que le gusta."], "Una motivación"),
        W("Separar tres ideas", "Sofía crece 8 cm en un año y le preocupa cómo se ve su cara con acné. Dice: «Me valoro poco». ¿Qué idea nombra su primera preocupación y cuál la segunda?", ["La preocupación por cómo se ve es sobre su cuerpo: imagen corporal.", "«Me valoro poco» habla de cuánto se valora: autoestima.", "El autoconcepto sería la descripción completa que ella haga de sí."], "Imagen corporal (cómo se ve) y autoestima (cuánto se valora)"),
    ],
    [
        M("Creer que una representación positiva solo incluye lo que otros aplauden.", "Se confunde ser positivo con ser perfecto.", "Incluye fortalezas y aspectos por mejorar, apoyados en hechos."),
        M("Pensar que la imagen corporal es todo el autoconcepto.", "En la pubertad el cuerpo cambia mucho y se le da demasiado peso.", "El cuerpo es una parte; también cuentan intereses, valores y capacidades."),
    ],
    R=[
        ex("«Me gusta dibujar mapas de mi barrio». ¿Es un interés o una característica?", "Un interés", "Dice algo que le gusta hacer."),
        ex("«Soy ordenada con mis cuadernos». ¿Es una característica o una motivación?", "Una característica", "Describe cómo es la persona."),
        ex("¿La autoestima se refiere a cuánto te valoras o a cuánto mides?", "A cuánto te valoras", "La autoestima es la valoración y el respeto que te tienes."),
    ],
    U=[
        ex("La frase «Soy buena para explicar, pero me cuesta hablar en público». ¿Qué tipo de retrato muestra? A) Uno justo, con fortaleza y aspecto por mejorar. B) Uno solo de elogios.", "A", "Reconoce algo que hace bien y algo que le cuesta."),
        ex("Sofía se mira al espejo y le preocupa su acné. ¿Eso pertenece a la imagen corporal o a la capacidad?", "A la imagen corporal", "Habla de cómo ve su cuerpo."),
        ex("Un curso escribe «Somos un curso que se ayuda en matemática». ¿Es una representación individual o colectiva?", "Colectiva", "Describe a un grupo, no a una sola persona."),
    ],
    A=[
        ex("Sofía anotó: 1) «me gusta el ukelele»; 2) «quiero ayudar a mis compañeros»; 3) «soy constante»; 4) «puedo armar un horario semanal sin ayuda». ¿Cuál es la capacidad?", "La 4", "Dice algo que puede hacer; las otras son interés, motivación y característica."),
        ex("Sofía piensa: «Me salió acné, soy fea y nadie me querrá». ¿Qué parte es un hecho? A) Le salió acné. B) Nadie la querrá.", "A", "Que le salió acné se puede observar; lo otro es una predicción sin pruebas."),
        ex("Un curso quiere describirse y escribe: «Somos buenos en deportes y nos cuesta llegar a la hora». ¿Incluye fortaleza y aspecto por mejorar, sí o no?", "Sí", "Deportes es la fortaleza y la puntualidad es lo que mejorar."),
    ],
    Z=[
        ex("Explica por qué «soy mala para todo» no es una representación positiva ni justa.", "Es una etiqueta total que no se apoya en hechos", "Ignora lo que sí hace bien y no distingue casos concretos."),
        ex("Ismael dice: «Si sumo intereses nuevos en la adolescencia, dejo de ser yo». ¿Qué le responderías?", "Que cambiar y sumar intereses es normal y su identidad sigue", "El autoconcepto se actualiza con el crecimiento sin borrar lo que valoras."),
    ],
    D=[
        arith("Sofía anotó 18 frases sobre sí misma: 5 características, 4 intereses, 3 capacidades y 2 sobre su cuerpo. El resto son motivaciones. ¿Cuántas motivaciones anotó?", "18-5-4-3-2", "Al total se le restan las frases de los otros cuatro grupos."),
        arith("En un afiche del curso, 35 estudiantes escribieron 2 fortalezas cada uno y se descartaron 14 repetidas. ¿Cuántas fortalezas distintas quedaron?", "35*2-14", "Primero se calcula el total de frases y luego se quitan las repetidas."),
    ],
    context=[ex("En el Consejo de Curso piden completar el afiche «Somos un curso que…». Julián propone «el mejor curso del colegio». ¿Qué le falta a la frase para ser justa?", "Un hecho que la apoye", "Una representación positiva se apoya en logros o conductas que se puedan comprobar.")],
    selfcheck=[ex("En Orientación: ¿el autoconcepto incluye características, motivaciones, intereses y capacidades?", "Sí", "Son sus cuatro partes."), ex("¿La imagen corporal es lo mismo que todo el autoconcepto?", "No", "Es solo una parte de cómo te ves."), ex("¿Un curso también puede construir una representación colectiva?", "Sí", "Se arma entre todos con fortalezas y aspectos por mejorar.")],
    task=T("Lee el perfil de Ámbar, una estudiante inventada: juega básquetbol hace dos años; ayudó a una compañera a estudiar inglés; se enoja rápido cuando pierde; este año creció 7 cm y no encuentra zapatillas cómodas; quiere que su curso participe más en las actividades. Escribe cinco líneas: una característica, una motivación, un interés, una capacidad y una frase sobre su cuerpo que la trate con respeto. Cada línea debe apoyarse en un dato del perfil.", "Característica: se enoja rápido cuando pierde, y puede aprender a calmarse. Motivación: quiere que su curso participe. Interés: el básquetbol. Capacidad: ayudó a una compañera con inglés. Cuerpo: creció 7 cm, un cambio normal.", ["escribe las cinco líneas pedidas", "cada línea se apoya en un dato del perfil", "no usa etiquetas sin hechos", "no cuenta nada íntimo propio"], ["cuadro escrito", "texto oral"], ["usar una etiqueta sin hecho", "confundir interés con capacidad"], "Reconoce las líneas bien clasificadas y pregunta qué hecho apoya la frase menos clara."),
    reinforce="Escribe tres frases sobre un personaje de cuento: una característica, un interés y una capacidad, cada una con su hecho.",
    extend="Explica con tus palabras la diferencia entre autoconcepto, autoestima e imagen corporal.",
)

lesson(
    OA1, 2,
    "Una hoja y un lápiz. El caso de Bruno, un estudiante inventado, y sus mensajes están escritos en los ejercicios. Nadie cuenta experiencias propias.",
    "Aprenderé a separar hechos, emociones, derechos y límites cuando alguien hace comentarios sobre mi cuerpo o mis cambios. Sirve para cuidar mi autoconcepto sin dejar que una burla lo defina.",
    ["Sé que el autoconcepto y la autoestima no son lo mismo.", "Sé que la pubertad ocurre a ritmos distintos."],
    [
        "Cuando alguien comenta tu cuerpo o tus cambios, puedes ordenar lo que pasa en cuatro pasos. Primero, el hecho: lo que realmente ocurrió y se puede comprobar, como «mi voz cambió este año». Segundo, la emoción: lo que sientes, como vergüenza, rabia o tristeza. Las emociones no son buenas ni malas; avisan que algo importa. Tercero, el derecho: tienes derecho a un trato digno y a no ser burlado por tu cuerpo. Cuarto, el límite: lo que aceptas y lo que no.",
        "Una opinión ofensiva no es un hecho. Si alguien dice «tu voz suena rara», eso es una burla disfrazada de dato. El hecho es que la voz cambia en la pubertad y cada persona lo vive en un momento distinto. Poner un límite es decirlo con claridad y sin insultar: «No me gusta que hables así de mí». Si la burla sigue, no es tu responsabilidad arreglarla solo: avisa a un adulto de confianza.",
        "Las redes sociales muestran fotos con filtros y retoques. Compararte con ellas es injusto: no muestran cuerpos reales ni sus cambios normales. Tu valor no depende de cuántos «me gusta» recibes. Recuerda que también eres responsable de lo que dices de otros: un comentario sobre el cuerpo de alguien puede doler mucho.",
    ],
    [("hecho", "algo que ocurrió y se puede comprobar"), ("emoción", "lo que siente una persona ante una situación"), ("derecho", "algo que toda persona puede exigir por su dignidad"), ("límite", "lo que una persona acepta y lo que no acepta"), ("burla", "comentario que ridiculiza a alguien para herirlo")],
    [
        W("Separar hecho y opinión", "Bruno lee en un chat de curso: «Bruno habla como dibujo animado». ¿Cuál es el hecho y cuál la burla, si su voz cambió hace tres meses?", ["Que su voz cambió hace tres meses se puede comprobar.", "«Habla como dibujo animado» es una burla.", "La burla no es un dato sobre Bruno, sino una forma de herir."], "Hecho: su voz cambió. Burla: «dibujo animado»"),
        W("Poner un límite", "Un compañero repite la burla cada recreo. ¿Qué puede decir Bruno y qué hacer si sigue?", ["Debe decir con claridad que le molesta, sin insultar.", "Si el compañero no para, debe avisar.", "Elige a una persona adulta de confianza del colegio."], "Decir «No me gusta que hables así de mí» y, si sigue, avisar a una persona adulta de confianza"),
    ],
    [
        M("Creer que una burla es la «verdad» sobre el cuerpo de uno.", "Se confunde una opinión ofensiva con un hecho.", "Separa lo que se puede comprobar de lo que es burla."),
        M("Pensar que sentir vergüenza o rabia es malo y hay que ocultarlo.", "Se cree que las emociones deben desaparecer.", "Las emociones avisan que algo importa; se nombran y se cuidan."),
    ],
    R=[
        ex("«Mi voz cambió este año». ¿Es un hecho o una burla?", "Un hecho", "Se puede comprobar y no hiere a nadie."),
        ex("«Tu cara parece una pizza». ¿Es un hecho o una burla?", "Una burla", "Ridiculiza el aspecto de alguien para herirlo."),
        ex("¿Tienes derecho a un trato digno aunque tu cuerpo esté cambiando, sí o no?", "Sí", "El trato digno es un derecho de toda persona."),
    ],
    U=[
        ex("Si te dan vergüenza los comentarios de un compañero, ¿esa emoción es una señal de que algo importa? A) Sí, avisa que algo te afecta. B) No, es una falla personal.", "A", "Las emociones informan de lo que nos importa y no son fallas."),
        ex("Ana mira un perfil con fotos muy retocadas y piensa que su cuerpo es «raro». ¿Qué falla en esa comparación?", "Las fotos retocadas no muestran cuerpos reales", "El retoque cambia la imagen y la comparación resulta injusta."),
        ex("¿«No me gusta que hables así de mí» es un límite claro o una agresión?", "Un límite claro", "Dice lo que no acepta sin insultar."),
    ],
    A=[
        ex("Bruno anotó: 1) «mi voz cambió»; 2) «me da rabia que se rían»; 3) «tengo derecho a que me respeten»; 4) «voy a pedirles que paren». ¿Cuál frase nombra el límite?", "La 4", "Es la acción de decir qué no acepta; las otras son hecho, emoción y derecho."),
        ex("Un chat comenta el estirón de Camila con risas. Ella no responde con insultos y se lo cuenta a su profesora jefe. ¿Eso muestra cuidar su dignidad, sí o no?", "Sí", "Evita la agresión y busca el apoyo de una persona adulta."),
        ex("Tras ver 40 «me gusta» en una foto suya, Lucas se siente más valioso que ayer. ¿Su valor depende de los «me gusta»? A) No, su valor no cambia con ellos. B) Sí, sube con cada uno.", "A", "El valor de una persona no se mide con reacciones en redes."),
    ],
    Z=[
        ex("Explica por qué decir «solo era una broma» no borra el daño de una burla sobre el cuerpo de otro.", "Porque el daño depende de cómo se siente quien la recibe", "La intención no cancela el efecto y el trato digno se mantiene."),
        ex("Un amigo de Bruno se ríe de la burla para no quedar afuera del grupo. ¿Qué otra opción tenía?", "No reírse y decirle a Bruno que le parece injusto", "Reírse refuerza la burla; apoyar al afectado la detiene."),
    ],
    D=[
        arith("En un chat de 28 integrantes, 9 escribieron burlas y 11 se rieron con emojis. El resto no participó. ¿Cuántos no participaron?", "28-9-11", "Al total se le restan quienes escribieron y quienes se rieron."),
        arith("Un grupo envió 6 mensajes de burla por día durante 5 días. ¿Cuántos mensajes de burla se enviaron en total?", "6*5", "Se multiplican los mensajes diarios por los días."),
    ],
    context=[ex("Noelia cambió de peso este año y en el patio un grupo le dice «¿qué te pasó?». Ella se aleja con rabia. ¿Qué hecho, qué emoción y qué derecho puede nombrar? Responde en una frase.", "Hecho: su cuerpo cambió. Emoción: rabia. Derecho: trato digno", "Separar los tres elementos ayuda a decidir qué límite poner.")],
    selfcheck=[ex("En Orientación: ¿una burla sobre el cuerpo es un hecho?", "No", "Es una opinión ofensiva."), ex("¿Puedes poner un límite sin insultar?", "Sí", "Se dice con claridad lo que no aceptas."), ex("¿Si una burla continúa, conviene avisar a un adulto de confianza?", "Sí", "No es tu responsabilidad detenerla solo o sola.")],
    task=T("Lee el caso de Isidora, una estudiante inventada: su grupo de WhatsApp comparte una foto de ella en educación física con el texto «mira cómo corre». Isidora se siente avergonzada. Escribe cuatro líneas: un hecho, una emoción, un derecho y un límite con la frase exacta que ella podría decir. Cierra con a quién avisaría si el grupo sigue.", "Hecho: el grupo compartió una foto suya con un texto burlón. Emoción: vergüenza. Derecho: trato digno y a que no usen su imagen. Límite: «Saquen esa foto del grupo, no me gusta». Avisaría a su profesora jefe.", ["escribe hecho, emoción, derecho y límite", "el límite es una frase clara y sin insultos", "nombra a una persona adulta de confianza", "no cuenta una vivencia propia"], ["cuatro líneas escritas"], ["mezclar opinión con hecho", "responder con insultos"], "Reconoce el límite claro y pregunta qué cambiaría si el grupo no hace caso."),
    reinforce="Escribe un hecho, una emoción y un derecho para un personaje de cuento al que se burlan por su estatura.",
    extend="Explica por qué las fotos retocadas de las redes no sirven para medir el propio cuerpo.",
)

lesson(
    OA1, 3,
    "Una hoja y un lápiz. El caso de Matías, un estudiante inventado, y las opciones están escritos en los ejercicios. Todo se analiza en tercera persona.",
    "Aprenderé a comparar opciones ante comentarios o presiones sobre mi apariencia y a prever las consecuencias para mi autoconcepto. Sirve para decidir con calma y no por impulso.",
    ["Sé separar hechos, emociones, derechos y límites.", "Sé que una burla no define a la persona."],
    [
        "Decidir bien es comparar opciones y mirar sus consecuencias, tanto inmediatas como a largo plazo. Imagina que a Matías le dicen que es «muy bajo». Puede insultar de vuelta, esconderse y dejar el taller de teatro, aceptar la burla con una risa forzada, o poner un límite y buscar apoyo. Cada camino deja huellas distintas en cómo él se ve y en cómo lo tratan los demás.",
        "Una consecuencia inmediata es lo que pasa enseguida, como sentirse aliviado al insultar. Una consecuencia a largo plazo es lo que pasa después, como que el conflicto crezca o que Matías pierda una actividad que le gusta. Una buena opción respeta tu dignidad y la de los demás, tiene en cuenta tus intereses y puede mantenerse en el tiempo. Evitar un taller para no ser molestado parece seguro, pero castiga a quien fue molestado.",
        "También hay opciones que construyen autoconcepto: recordar logros reales, hablar con alguien de confianza, practicar una habilidad que te importa y rodearte de personas que te traten bien. Fortalecer lo que haces bien no significa negar lo que te cuesta; significa dejar de usar un comentario ajeno como medida de tu valor.",
    ],
    [("opción", "camino posible entre varios para actuar"), ("consecuencia", "efecto que sigue a una decisión"), ("a corto plazo", "que ocurre enseguida"), ("a largo plazo", "que ocurre después de un tiempo"), ("impulso", "reacción rápida sin pensar en sus efectos")],
    [
        W("Comparar dos opciones", "Matías recibe la burla «enano». Opción 1: insultar de vuelta. Opción 2: decir «no me gusta ese apodo» y contárselo a su profesor jefe. ¿Cuál cuida mejor su autoconcepto?", ["Insultar puede aliviar un momento, pero aumenta el conflicto.", "Poner un límite respeta su dignidad y busca apoyo.", "Con la opción 2 no se convierte en agresor."], "La opción 2"),
        W("Pensar a largo plazo", "Matías deja el taller de teatro para evitar a quienes lo molestan. ¿Qué pierde a largo plazo?", ["Dejó una actividad que le gusta.", "La burla no se detuvo; solo se retiró él.", "Pierde un interés y una oportunidad de mostrar su capacidad."], "Pierde un interés y no resuelve el problema"),
    ],
    [
        M("Elegir la opción que alivia más rápido sin mirar las consecuencias.", "El impulso del momento tapa el largo plazo.", "Pregúntate qué pasa mañana y en un mes."),
        M("Creer que alejarse de lo que te gusta es la mejor forma de evitar burlas.", "Se piensa que quien se retira queda a salvo.", "Poner límite y buscar apoyo protege sin renunciar a tus intereses."),
    ],
    R=[
        ex("Insultar de vuelta a quien se burló, ¿es una consecuencia a corto plazo de alivio o una solución duradera?", "Un alivio a corto plazo", "No resuelve la burla y puede aumentar el conflicto."),
        ex("Contarle el problema a una persona adulta de confianza, ¿es una opción que busca apoyo, sí o no?", "Sí", "Pedir ayuda es una opción segura."),
        ex("¿Una consecuencia a largo plazo ocurre enseguida o después de un tiempo?", "Después de un tiempo", "Así se define el largo plazo."),
    ],
    U=[
        ex("Matías se ríe junto con quienes se burlan de él. ¿Qué mensaje puede entender el grupo? A) Que la burla no le molesta. B) Que la burla es injusta.", "A", "Reírse da señal de aceptar el trato, aunque por dentro duela."),
        ex("Pía evita todas las clases de gimnasia para que no comenten su cuerpo. ¿Cuál es una consecuencia a largo plazo?", "Pierde actividad física y no resuelve el problema", "Evitar no detiene los comentarios y la afecta a ella."),
        ex("Una buena opción respeta la dignidad de ¿solo quien actúa o de todas las personas involucradas?", "De todas las personas involucradas", "Una opción justa cuida a todos, no solo a uno."),
    ],
    A=[
        ex("Lucía recibe un apodo cruel. Opciones: 1) responder con otro apodo; 2) borrar su cuenta y aislarse; 3) pedir que paren y avisar a la orientadora; 4) hacer como si nada. ¿Cuál cuida su dignidad y busca apoyo?", "La 3", "Pone un límite y pide ayuda; las otras agreden, se aíslan o aguantan."),
        ex("Rafael publica una foto con filtros para recibir elogios. ¿Qué conviene preguntarse antes? A) Si su valor depende de esa reacción. B) Qué elogios recibirá la próxima vez.", "A", "Reflexionar sobre su valor lo ayuda a decidir sin depender de elogios."),
        ex("Un curso decide hacer una «ronda de logros» donde cada uno reconoce un aporte real de otro. ¿Qué efecto tiene en la representación del grupo?", "Fortalece una imagen colectiva positiva y real", "Los aportes reales dan una representación justa del curso."),
    ],
    Z=[
        ex("¿Por qué la opción «aguantar sin decir nada» puede dañar el autoconcepto de una persona con el tiempo?", "Porque la burla se repite y la persona puede creerla", "Callar no detiene la burla y se acumula el malestar."),
        ex("Dos amigas comparan sus respuestas ante un comentario hiriente: una lo ignora y la otra lo conversa con una adulta. ¿Cuál tiene más apoyo para sostener su decisión y por qué?", "La que lo conversó, porque cuenta con ayuda", "El apoyo de una persona adulta fortalece la decisión."),
    ],
    D=[
        arith("De 30 estudiantes encuestados sobre cómo reaccionarían ante un apodo, 12 insultarían, 7 se aislarían y el resto pondría un límite. ¿Cuántos pondrían un límite?", "30-12-7", "Al total se le restan quienes insultarían y se aislarían."),
        arith("Un curso de 32 personas hizo una ronda de logros: cada una reconoció a 3 compañeros. ¿Cuántos reconocimientos hubo en total?", "32*3", "Se multiplican las personas por los reconocimientos de cada una."),
    ],
    context=[ex("En la hora de Orientación, el profesor lee un caso: Camilo escucha que lo llaman «flaco palo» en el recreo. Tiene cuatro opciones: gritar, irse a la sala, pedir que paren o publicar un meme contra quien habla. ¿Cuál opción conviene y por qué?", "Pedir que paren, porque cuida su dignidad sin agredir", "Pone un límite claro y evita ser agresor o aislarse.")],
    selfcheck=[ex("En Orientación: ¿conviene mirar las consecuencias a corto y a largo plazo?", "Sí", "Así se decide sin dejarse llevar por el impulso."), ex("¿Evitar una actividad que te gusta resuelve la burla?", "No", "El problema sigue y pierdes la actividad."), ex("¿Pedir ayuda a un adulto de confianza es una opción válida?", "Sí", "Es una forma segura de enfrentar un problema.")],
    task=T("Lee el caso de Tamara, una estudiante inventada: le dicen «cuerpo de palo» por WhatsApp. Escribe una tabla con tres opciones (por ejemplo, responder con insultos, aislarse, poner un límite y avisar). Para cada una anota la consecuencia a corto plazo, la consecuencia a largo plazo y cómo afectaría el autoconcepto de Tamara. Cierra eligiendo una opción y explicando por qué.", "Insultar: alivio breve, el conflicto crece y se arriesga a sanciones. Aislarse: se evita el chat, pierde amistades y la burla sigue. Poner límite y avisar: es incómodo al comienzo, pero puede detener la burla y reforzar su dignidad. Elijo la tercera.", ["compara tres opciones", "distingue corto y largo plazo", "relaciona cada una con el autoconcepto", "justifica la opción elegida"], ["tabla de tres filas"], ["mirar solo el corto plazo", "elegir una opción que agrede"], "Valora la comparación completa y pregunta qué apoyo adulto elegiría Tamara."),
    reinforce="Escribe dos opciones y sus consecuencias para un personaje de cuento al que le dicen un apodo que no le gusta.",
    extend="Explica por qué una opción que alivia hoy puede no ser la mejor a largo plazo.",
)

lesson(
    OA1, 4,
    "Una hoja y un lápiz. El caso de Valentín y el afiche del curso están escritos en los ejercicios. Todo ocurre con personajes inventados.",
    "Aprenderé a elegir una acción segura que cuide mi autoconcepto y el de mi curso, y a saber a quién pedir ayuda. Sirve para construir una imagen justa de mí y de mi grupo en la adolescencia.",
    ["Sé comparar opciones y consecuencias.", "Sé que el autoconcepto se construye con hechos."],
    [
        "Elegir una acción segura es escoger la opción que cuida tu dignidad, la de otros, y que puedes sostener. Tres preguntas ayudan: ¿me respeta a mí y respeta a los demás?, ¿es realista y la puedo hacer ahora?, ¿tengo apoyo de una persona adulta de confianza si no basta? Si una acción falla alguna de las tres, conviene buscar otra.",
        "Para fortalecer tu autoconcepto, puedes escribir cada semana un logro real, por pequeño que sea, y una cosa por mejorar con un paso concreto. Para el autoconcepto colectivo, el curso puede armar un afiche con fortalezas, cosas por mejorar y un compromiso. La clave es que todos aporten y que ninguna frase humille a una persona o a un grupo.",
        "Si la situación te supera, por ejemplo cuando la burla es constante o te sientes triste mucho tiempo, no la enfrentes a solas. Recurre a tu familia, a tu profesor jefe, al orientador o a la persona encargada de convivencia escolar. Pedir ayuda es una señal de cuidado, no de debilidad. Si necesitas hablar con alguien de inmediato y no sabes con quién, puedes llamar al Fono Niños 147.",
    ],
    [("acción segura", "decisión que protege la dignidad de todos y cuenta con apoyo"), ("compromiso", "promesa concreta que un grupo se hace para mejorar"), ("convivencia escolar", "forma en que se relacionan las personas del colegio y equipo que la cuida"), ("realista", "que se puede hacer con los medios disponibles"), ("logro", "cosa buena que alguien consiguió con esfuerzo")],
    [
        W("Elegir con tres preguntas", "A Valentín le dicen «gordito» en un grupo del curso. Opciones: (1) pedir que paren y avisar al profesor jefe; (2) amenazar a quien lo dijo. Evalúa con las tres preguntas.", ["La opción 1 respeta a todos, es realista y tiene apoyo adulto.", "La opción 2 amenaza y no respeta a los demás.", "Falla la primera pregunta."], "La opción 1"),
        W("Armar un compromiso colectivo", "El curso escribe: «Fortaleza: nos ayudamos. Por mejorar: escuchar. Compromiso: levantar la mano y respetar turnos». ¿Es un compromiso concreto?", ["Dice una acción que se puede observar.", "No humilla a nadie.", "Se puede revisar en una semana."], "Sí, es concreto y observable"),
    ],
    [
        M("Pensar que pedir ayuda a una persona adulta es de débiles.", "Se confunde resolver solo con ser fuerte.", "Pedir ayuda cuida tu bienestar y el de los demás."),
        M("Creer que el afiche del curso debe mostrar solo lo positivo.", "Se evita nombrar lo que se puede mejorar.", "Una representación justa incluye fortalezas, mejoras y un compromiso."),
    ],
    R=[
        ex("Una acción segura, ¿respeta a todos o solo a quien actúa?", "A todos", "La acción segura cuida la dignidad de todas las personas."),
        ex("Si una burla no para, ¿conviene enfrentarla solo o pedir ayuda a una persona adulta de confianza?", "Pedir ayuda", "Un adulto puede intervenir cuando solo no basta."),
        ex("Si necesitas hablar con alguien de inmediato y no sabes con quién, ¿puedes llamar al Fono Niños 147, sí o no?", "Sí", "Esta clase nombra el Fono Niños 147 como línea de ayuda."),
    ],
    U=[
        ex("Rocío evalúa una acción con tres preguntas: respeta, es realista y tiene apoyo. Si la acción no tiene apoyo adulto, ¿cumple las tres, sí o no?", "No", "Falta la tercera pregunta."),
        ex("Un afiche dice «el curso es perfecto y nunca falla». ¿Es una representación justa? A) No, no reconoce nada por mejorar. B) Sí, porque es positiva.", "A", "Una imagen justa incluye también lo que se puede mejorar."),
        ex("Tras semanas de tristeza por comentarios sobre su cuerpo, Dante piensa en callar. ¿Qué es lo más seguro?", "Hablar con una persona adulta de confianza", "La tristeza prolongada necesita apoyo y no debe sostenerse a solas."),
    ],
    A=[
        ex("Valentín tiene cuatro opciones frente a un meme que se burla de su cuerpo: 1) reenviarlo para reírse de sí; 2) pedir que lo saquen del grupo y mostrárselo a su profesor jefe; 3) borrar su cuenta sin contar; 4) subir un meme contra otro. ¿Cuál es la acción segura?", "La 2", "Pone un límite, usa el apoyo adulto y no agrede."),
        ex("El curso quiere un compromiso para mejorar. ¿Cuál es concreto? A) Llegar a la hora a las 8:00. B) Ser mejores personas.", "A", "Se puede observar y revisar; el otro es muy general."),
        ex("Marta anota cada viernes un logro de la semana: «entregué mi trabajo a tiempo». ¿Qué parte del autoconcepto fortalece?", "Sus capacidades, con un hecho", "El logro real respalda lo que puede hacer."),
    ],
    Z=[
        ex("¿Por qué una acción como «amenazar a quien se burló» no es una acción segura aunque detenga la burla por un rato?", "Porque no respeta a todos y puede aumentar la violencia", "Una acción segura no daña a otros ni crea nuevos riesgos."),
        ex("El curso decide escribir una frase para cada estudiante en el afiche, pero omite a Joaquín «porque casi no habla». ¿Qué principio se rompe?", "La inclusión: nadie debe quedar fuera", "Una representación colectiva incluye a todos sus integrantes."),
    ],
    D=[
        arith("Para el afiche, cada estudiante de un curso de 33 aporta 1 fortaleza y 1 cosa por mejorar. ¿Cuántas frases habrá que ordenar?", "33*2", "Se multiplican los estudiantes por las dos frases de cada uno."),
        arith("El curso ordenó 66 frases en grupos de 6 por cartulina. ¿Cuántas cartulinas necesitan?", "66//6", "Se divide el total de frases por las que caben en cada cartulina."),
    ],
    context=[ex("Camila lee en el chat del curso que se ríen de la forma de caminar de Benja. Ella quiere ayudar sin dejarlo en evidencia. ¿Qué acción es segura?", "Escribirle en privado y avisar a un adulto del colegio", "Lo apoya sin exponerlo y busca ayuda de quien puede intervenir.")],
    selfcheck=[ex("En Orientación: ¿una acción segura respeta a todos?", "Sí", "Cuida la dignidad de cada persona."), ex("¿Pedir ayuda a una persona adulta es una señal de cuidado?", "Sí", "Protege tu bienestar."), ex("¿Un afiche del curso debe dejar fuera a quien casi no habla?", "No", "La representación colectiva incluye a todos.")],
    task=T("El curso de 8.º de Valentina, inventado, debe armar un afiche «Así somos». Redacta tres frases del afiche: una fortaleza del curso apoyada en un hecho, una cosa por mejorar y un compromiso con una acción concreta y una fecha de revisión. Agrega una línea que diga a quién se pediría ayuda si alguien recibe burlas por su apariencia.", "Fortaleza: en octubre juntamos 40 libros para la biblioteca. Por mejorar: interrumpimos cuando alguien habla. Compromiso: levantar la mano; lo revisamos el viernes 15. Ayuda: al profesor jefe y a convivencia escolar.", ["incluye fortaleza, mejora y compromiso", "el compromiso es concreto y revisable", "nombra una persona de ayuda", "ninguna frase humilla a alguien"], ["afiche escrito", "texto oral"], ["frases generales sin hechos", "dejar a alguien fuera"], "Reconoce el compromiso observable y pregunta cómo se revisará en la fecha prevista."),
    reinforce="Escribe una fortaleza, una mejora y un compromiso para un equipo deportivo inventado.",
    extend="Explica por qué la representación del curso debe incluir a todos sus integrantes.",
)

# ================================================================ OA 02
lesson(
    OA2, 1,
    "Una hoja y un lápiz. El caso de Emilia, una estudiante inventada, y las frases para clasificar están escritos en los ejercicios. No necesitas contar nada personal.",
    "Aprenderé que la sexualidad tiene cuatro dimensiones que se integran, y que cuidar el cuerpo y la intimidad es parte de ella. Sirve para entender los cambios de la adolescencia con respeto y sin vergüenza.",
    ["Sé que la pubertad trae cambios normales.", "Sé que tengo derecho a un trato digno."],
    [
        "La sexualidad es parte de la vida de toda persona y no se reduce a las relaciones sexuales. Tiene cuatro dimensiones. La biológica es el cuerpo y sus cambios. La afectiva son las emociones y los sentimientos, como el cariño o la vergüenza. La social son las relaciones con otras personas y lo que el entorno espera. La ética son los valores, como el respeto, la responsabilidad y el cuidado de uno mismo y de otros.",
        "Integrar las dimensiones es pensarlas juntas al tomar decisiones. Si a Emilia le gusta un compañero, siente algo (afectiva), su cuerpo reacciona y cambia (biológica), sus amigas comentan (social) y ella decide tratarlo con respeto (ética). Decidir mirando solo una dimensión, por ejemplo solo la emoción del momento, puede llevar a decisiones que después se lamentan.",
        "La intimidad es tu mundo privado: tu cuerpo, tus sentimientos y tus mensajes personales. Tienes derecho a decidir quién se entera de qué y quién te toca. Cada persona vive su desarrollo a su manera y en su tiempo, y todas merecen respeto. Hablar de estos temas con seriedad y sin burlas, con una persona adulta de confianza o con un profesional de salud, es una forma de cuidarte.",
    ],
    [("sexualidad", "parte de la vida que incluye cuerpo, afectos, relaciones y valores"), ("dimensión", "una de las partes que forman un tema"), ("integrar", "considerar varias partes juntas al decidir"), ("intimidad", "mundo privado: cuerpo, sentimientos y mensajes personales"), ("ético", "relacionado con valores como el respeto y la responsabilidad")],
    [
        W("Clasificar por dimensión", "Emilia piensa: «Me sentí nerviosa porque me gusta un compañero». ¿Qué dimensión nombra?", ["Habla de lo que siente: nervios y gusto por alguien.", "Los sentimientos pertenecen a una dimensión.", "Es la dimensión afectiva."], "La dimensión afectiva"),
        W("Integrar dimensiones", "Emilia quiere invitar a un compañero a conversar, pensando en no presionarlo y en cómo lo tomará su grupo de amigas. ¿Qué dimensiones usa?", ["No presionar es un valor: ética.", "Pensar en su grupo de amigas es social.", "Quiere conversar porque le gusta: afectiva."], "La ética, la social y la afectiva"),
    ],
    [
        M("Creer que sexualidad solo significa relaciones sexuales.", "Se reduce un tema amplio a una sola parte.", "Incluye cuerpo, afectos, relaciones y valores."),
        M("Pensar que hablar de intimidad y de cambios del cuerpo es de mal gusto.", "Se confunde cuidar la información con tener vergüenza.", "Se puede hablar con respeto con una persona adulta de confianza o un profesional de salud."),
    ],
    R=[
        ex("«Mi voz cambió y estoy creciendo». ¿Qué dimensión nombra: biológica o ética?", "Biológica", "Habla del cuerpo y sus cambios."),
        ex("«Quiero tratar con respeto a mi amigo». ¿Qué dimensión nombra: ética o biológica?", "Ética", "El respeto es un valor."),
        ex("¿La sexualidad se reduce a las relaciones sexuales, sí o no?", "No", "Incluye cuerpo, afectos, relaciones sociales y valores."),
    ],
    U=[
        ex("¿Por qué la dimensión afectiva incluye la vergüenza además del cariño?", "Porque ambas son emociones", "La dimensión afectiva reúne todo lo que se siente."),
        ex("«En mi grupo se comenta quién pololea con quién». ¿Qué dimensión nombra: social o biológica?", "Social", "Habla de relaciones y de lo que ocurre en el grupo."),
        ex("¿Qué es la intimidad? A) Tu mundo privado: cuerpo, sentimientos y mensajes. B) Todo lo que haces en el colegio.", "A", "La intimidad es lo privado de cada persona."),
    ],
    A=[
        ex("Emilia anotó: 1) «me crecieron las piernas»; 2) «me da vergüenza que me miren»; 3) «mis amigas hablan de pololeo»; 4) «quiero cuidar a los demás». ¿Cuál es la dimensión ética?", "La 4", "Cuidar a los demás es un valor; las otras son biológica, afectiva y social."),
        ex("Un joven decide solo por lo que siente en el momento y no piensa en respeto ni consecuencias. ¿Qué dimensión deja fuera? A) La ética. B) La biológica.", "A", "Dejó de lado los valores como el respeto y la responsabilidad."),
        ex("Emilia escribe un diario privado con sus sentimientos. ¿Quién decide si alguien lo lee?", "Ella", "La intimidad es suya y decide quién se entera."),
    ],
    Z=[
        ex("¿Por qué decidir mirando una sola dimensión puede llevar a equivocarse?", "Porque deja fuera cosas importantes", "Las dimensiones se influyen y deben considerarse juntas."),
        ex("Un compañero dice que hablar de los cambios del cuerpo es «cochino». ¿Qué respuesta respetuosa le darías?", "Que es normal hablar con respeto para cuidarse", "Entender los cambios ayuda a cuidar el cuerpo y la salud."),
    ],
    D=[
        arith("En una lista de 24 frases, 7 son de la dimensión biológica, 6 de la afectiva y 5 de la social. El resto son éticas. ¿Cuántas son éticas?", "24-7-6-5", "Al total se le restan las frases de las otras tres dimensiones."),
        arith("Un cuadro tiene 4 dimensiones y Emilia escribe 3 ideas en cada una. ¿Cuántas ideas escribió?", "4*3", "Se multiplican las dimensiones por las ideas de cada una."),
    ],
    context=[ex("En Orientación, la profesora pregunta qué dimensiones intervienen cuando alguien decide qué publicar de su pololeo en una red social. Marcos responde: «Solo la tecnológica». ¿Cuál es la respuesta más completa?", "Afectiva, social y ética, porque hay sentimientos, relaciones y respeto", "Se involucran sentimientos, vínculos con otras personas y valores como la privacidad.")],
    selfcheck=[ex("En Orientación: ¿la sexualidad tiene dimensiones biológica, afectiva, social y ética?", "Sí", "Son cuatro partes que se influyen."), ex("¿La intimidad incluye tus sentimientos y mensajes personales?", "Sí", "Es tu mundo privado."), ex("¿Decidir solo por lo que siento en el momento integra las dimensiones?", "No", "Deja fuera las demás dimensiones.")],
    task=T("Lee el caso de Elías, un estudiante inventado: a los 13 años le cambió la voz, le gusta una compañera, sus amigos le preguntan si pololea y él quiere tratarla con respeto. Escribe una frase de Elías para cada dimensión: biológica, afectiva, social y ética. No cuentes nada personal tuyo.", "Biológica: mi voz cambió. Afectiva: me gusta una compañera y me da nervios. Social: mis amigos me preguntan si pololeo. Ética: quiero tratarla con respeto y sin presionar.", ["escribe una frase por cada dimensión", "usa los datos de Elías", "no cuenta nada personal", "usa un lenguaje respetuoso"], ["cuadro de cuatro columnas"], ["confundir afectiva con social", "reducir la sexualidad a relaciones sexuales"], "Reconoce las frases bien ubicadas y pregunta qué cambiaría si Elías olvidara la dimensión ética."),
    reinforce="Escribe una frase por dimensión sobre un personaje de cuento que está entrando a la adolescencia.",
    extend="Explica con tus palabras por qué las cuatro dimensiones deben pensarse juntas.",
)

lesson(
    OA2, 2,
    "Una hoja y un lápiz. El caso de Tomás y Valeria, personajes inventados, y las situaciones están escritos en los ejercicios. Nadie cuenta nada propio.",
    "Aprenderé a distinguir hechos, emociones, derechos y límites sobre mi cuerpo y mi intimidad, y a entender el consentimiento. Sirve para cuidarme y respetar a los demás en el pololeo y en la amistad.",
    ["Sé que la sexualidad tiene cuatro dimensiones.", "Sé que la intimidad es mi mundo privado."],
    [
        "Tu cuerpo es tuyo. Tienes derecho a decidir quién te toca, cómo y cuándo. Las partes íntimas son las que cubre la ropa interior o el traje de baño. Nadie debe tocarlas, mirarlas ni pedirte que las muestres, salvo un control de salud con una persona de confianza presente. Esto vale también para ti: no debes tocar ni exigir nada de la intimidad de otra persona.",
        "El consentimiento es aceptar algo de forma libre, informada y sin presión, engaño ni miedo. Un «sí» dicho por miedo, por insistencia o por chantaje no es consentimiento. Puede retirarse en cualquier momento: lo que aceptaste ayer, hoy puedes no querer. Si la otra persona calla, se aleja, baja la mirada o parece incómoda, debes detenerte y preguntar. Respetar un «no» es respetar a la persona, aunque sea tu pololo, tu pareja o tu amigo.",
        "Para decidir, separa los hechos (qué pasó), las emociones (qué sientes), los derechos (qué te corresponde) y los límites (qué aceptas y qué no). Tu incomodidad es una señal que debes tomar en serio. Si alguien insiste, te pide guardar un secreto sobre un contacto que te incomoda o es una persona mucho mayor, avisa a una persona adulta de confianza. La responsabilidad nunca es de quien fue tocado sin su consentimiento.",
    ],
    [("partes íntimas", "partes del cuerpo que cubre la ropa interior o el traje de baño"), ("consentimiento", "aceptar algo de forma libre, informada y sin presión ni miedo"), ("límite", "lo que acepto y lo que no respecto de mi cuerpo y mis cosas"), ("presión", "insistir o chantajear para que alguien acepte lo que no quiere"), ("chantaje", "amenaza o manipulación para obligar a alguien a hacer algo")],
    [
        W("Reconocer falta de consentimiento", "Tomás trata de abrazar a Valeria en el pasillo; ella baja la cabeza y se aleja un paso. ¿Hubo consentimiento?", ["Ella se alejó y bajó la cabeza.", "Esas señales muestran que no quiere.", "Sin consentimiento, él debe detenerse."], "No hubo consentimiento: Tomás debe respetar su señal"),
        W("Distinguir un chantaje", "Un compañero le dice a Valeria: «Si no me das un beso, ya no eres mi amiga». ¿Es consentimiento si ella dice que sí por miedo a perder la amistad?", ["El «sí» sale del miedo.", "El consentimiento debe ser libre.", "Hubo chantaje."], "No: un «sí» por chantaje o miedo no es consentimiento"),
    ],
    [
        M("Pensar que si alguien no dijo «no» en voz alta, aceptó.", "Se ignoran señales como callar, alejarse o bajar la mirada.", "Detente ante cualquier señal de incomodidad y pregunta con respeto."),
        M("Creer que un «sí» dicho por miedo o por insistencia sirve como consentimiento.", "Se confunde decir «sí» con aceptar libremente.", "El consentimiento debe ser libre, sin miedo ni presión."),
    ],
    R=[
        ex("¿Las partes íntimas son las que cubre la ropa interior o el traje de baño, sí o no?", "Sí", "Esa es la definición de partes íntimas."),
        ex("¿Se debe respetar un «no» de una amiga, sí o no?", "Sí", "Respetar un «no» es respetar a la persona."),
        ex("Si alguien se aleja cuando le quieres dar un abrazo, ¿debes insistir o detenerte?", "Detenerte", "Alejarse es una señal de que no quiere."),
    ],
    U=[
        ex("¿Por qué un «sí» dicho por miedo no es consentimiento verdadero?", "Porque no es libre", "El consentimiento exige que no haya presión ni miedo."),
        ex("Ayer Lucía aceptó que le tomaran una foto y hoy dice que no quiere. ¿Se respeta lo de ayer o lo de hoy?", "Lo de hoy", "El consentimiento puede cambiar en cualquier momento."),
        ex("Si te tocan de una manera que te incomoda, ¿tu emoción es una señal importante, sí o no?", "Sí", "Indica que debes poner un límite o pedir ayuda."),
    ],
    A=[
        ex("Situaciones: 1) «¿Puedo darte un abrazo?» y la otra dice que sí contenta; 2) «Si no me dejas, no eres mi amiga»; 3) la otra baja la cabeza y calla; 4) «Cuando quieras, avísame». ¿Cuáles respetan el consentimiento?", "1 y 4", "Preguntan y no presionan; la 2 chantajea y en la 3 se ignora una señal de incomodidad."),
        ex("Un adulto le pide a Tomás guardar el secreto de un contacto que lo incomoda. ¿Qué debe hacer? A) Contárselo a una persona adulta de confianza. B) Guardar el secreto para no meterse en problemas.", "A", "Un secreto que incomoda debe contarse; la responsabilidad es del adulto."),
        ex("Tomás dice «no me gusta» y su compañero responde «era broma». ¿Su límite sigue valiendo?", "Sí", "Aunque sea broma, quien se incomodó tiene derecho a que se respete su límite."),
    ],
    Z=[
        ex("Pía dice: «Como somos pareja, no necesito preguntarle si quiere que lo abrace». ¿Qué error comete?", "Cree que ser pareja reemplaza el consentimiento", "Aun en pareja hay que respetar si la otra persona quiere o no."),
        ex("¿Por qué la responsabilidad nunca es de quien fue tocado sin su consentimiento?", "Porque la responsabilidad es de quien cruzó el límite", "Quien tocó sin permiso decidió hacerlo; no es culpa de la otra persona."),
    ],
    D=[
        arith("En una encuesta ficticia de 32 estudiantes, 26 saben qué es el consentimiento y el resto no. ¿Cuántos no lo saben?", "32-26", "Al total se le restan los que sí lo saben."),
        ex("Nico y Pía juegan a hacerse cosquillas. Pía dice «ya no» entre risas y Nico sigue porque «se estaba riendo». ¿Qué debió hacer Nico y por qué?", "Parar de inmediato, porque ella dijo «ya no»", "Reírse no equivale a aceptar; un «no» claro se respeta aunque haya risa."),
    ],
    context=[ex("En un cumpleaños ficticio, un grupo juega a retar a alguien a tocar a otro compañero. Rafaela no quiere y lo dice. ¿Qué corresponde hacer al grupo?", "Parar el juego y respetar su «no»", "Un reto no reemplaza el consentimiento; nadie debe ser forzado.")],
    selfcheck=[ex("En Orientación: ¿mi cuerpo es mío y decido quién me toca?", "Sí", "Es un derecho de toda persona."), ex("¿Se puede cambiar de opinión después de haber aceptado algo?", "Sí", "El consentimiento puede retirarse en cualquier momento."), ex("¿La culpa es de quien fue tocado sin consentimiento?", "No", "La responsabilidad es de quien tocó.")],
    task=T("Lee los tres casos de personajes inventados: (1) Lucas le pide un abrazo a Emma y ella dice «hoy no»; él responde «está bien»; (2) Tomás insiste en tomarle una foto a Julia mientras ella tapa su cara; (3) Valeria ofrece un saludo con la mano y Marcos acepta. Para cada caso, escribe si se respeta el consentimiento y qué haría una persona respetuosa.", "(1) Sí, respeta el «hoy no». (2) No, Julia mostró que no quiere; Tomás debe parar y pedir permiso. (3) Sí, Valeria ofrece y Marcos acepta libremente.", ["clasifica los tres casos", "explica qué haría una persona respetuosa", "usa lenguaje respetuoso", "no cuenta una vivencia propia"], ["tabla escrita"], ["no respetar el «no»", "ignorar señales como taparse la cara"], "Reconoce la clasificación y pregunta qué otro saludo habría sin contacto físico."),
    reinforce="Escribe una frase para decir «no» con respeto y otra para aceptar un «no» que te dicen.",
    extend="Explica por qué un secreto que te incomoda debe contarse a una persona adulta de confianza.",
)

lesson(
    OA2, 3,
    "Una hoja y un lápiz. El caso de Camila y los mensajes están escritos en los ejercicios; no hay imágenes ni contenido explícito. Todo ocurre con personajes inventados.",
    "Aprenderé a comparar opciones y consecuencias cuando alguien presiona para pedir o enviar fotos o mensajes íntimos. Sirve para protegerme, proteger a otras personas y saber qué hacer si algo se difunde.",
    ["Sé que el consentimiento debe ser libre y puede retirarse.", "Sé que mi cuerpo y mi intimidad son míos."],
    [
        "Una imagen íntima es una foto o video del cuerpo sin ropa o de las partes íntimas. Enviar una por celular o redes es muy riesgoso: una vez enviada, quien la recibe puede reenviarla, guardarla o usarla para presionar, aunque haya prometido no hacerlo. Se pierde el control sobre ella. Pedirla como «prueba de amor» es presión; el cariño no se demuestra con imágenes íntimas.",
        "Compara las opciones ante una petición. Ceder puede parecer fácil, pero deja un riesgo duradero. Burlarse o amenazar al que pidió no resuelve nada. Lo que protege tiene cuatro pasos, en este orden: 1) decir «no» con claridad; 2) guardar la prueba, es decir, sacar una captura de los mensajes de presión; 3) bloquear la cuenta si insiste; 4) contárselo a una persona adulta de confianza. La prueba se guarda antes de bloquear, para no perder los mensajes. Además, guardar o reenviar imágenes íntimas de una persona menor de 18 años es grave y puede tener consecuencias legales.",
        "Si una imagen íntima de alguien se difunde, la culpa no es de quien confió, sino de quien la reenvió. Quien la reciba no debe reenviarla, ni guardarla en su celular, ni mostrarla a otros. Tampoco debe borrar el chat donde llegó, porque puede servir de prueba. Debe avisar enseguida a una persona adulta de confianza. Quien fue afectado necesita apoyo, no burlas. Cuando alguien te presione, recuerda: puedes decir «no», puedes cambiar de opinión y puedes pedir ayuda sin culpa.",
    ],
    [("imagen íntima", "foto o video del cuerpo sin ropa o de partes íntimas"), ("difundir", "enviar algo a muchas personas o hacerlo público"), ("presión", "insistir para que alguien haga algo que no quiere"), ("consecuencia legal", "efecto que establece la ley, como una sanción"), ("bloquear", "impedir que una cuenta nos escriba")],
    [
        W("Comparar opciones", "Un chico le dice a Camila: «Si me quieres, mándame una foto sin ropa». Opción 1: enviarla. Opción 2: decir «no» y avisar a una persona adulta de confianza. ¿Cuál la protege más y por qué?", ["Si envía la foto, pierde el control sobre ella.", "Decir «no» y avisar mantiene su intimidad.", "Pedirlo así es presión."], "La opción 2: protege su intimidad y busca ayuda"),
        W("Qué hacer con una imagen difundida", "A Pablo le llega al celular una imagen íntima de una compañera enviada por el grupo del curso. ¿Qué hace?", ["No debe reenviarla ni guardarla.", "No debe borrar el chat, porque puede servir de prueba.", "Debe avisar a una persona adulta de confianza."], "No reenviarla ni guardarla, no borrar el chat y avisar a una persona adulta de confianza"),
    ],
    [
        M("Creer que enviar una imagen íntima «solo a él» es seguro.", "Se confía en una promesa que no se puede controlar.", "Una vez enviada, se pierde el control."),
        M("Culpar a la persona cuya imagen se difundió.", "Se mira lo que hizo y no lo que hizo quien la reenvió.", "La responsabilidad es de quien difundió sin permiso."),
    ],
    R=[
        ex("Pedir una foto íntima como «prueba de amor», ¿es una presión o una muestra de cariño?", "Una presión", "El cariño no se demuestra con imágenes íntimas."),
        ex("Si te piden una imagen íntima, ¿puedes decir «no», sí o no?", "Sí", "Tienes derecho a negarte siempre."),
        ex("¿Se debe reenviar una imagen íntima de otra persona, sí o no?", "No", "Reenviarla causa daño y puede tener consecuencias legales."),
    ],
    U=[
        ex("¿Por qué se pierde el control de una imagen cuando ya fue enviada?", "Porque quien la recibe puede reenviarla o guardarla", "Aunque prometa no hacerlo, ya no depende de quien la envió."),
        ex("Una foto íntima de Ana se difundió. ¿De quién es la culpa? A) De quien la reenvió sin permiso. B) De Ana por haber confiado.", "A", "Difundir sin permiso es una decisión de quien reenvía."),
        ex("Camila recibe presión para enviar una foto íntima. ¿Cuál es el orden correcto de acciones? A) Bloquear a la persona, borrar el chat y después contar a un adulto. B) Decir «no», guardar una captura de los mensajes, bloquear y contar a un adulto de confianza.", "B", "La captura se guarda antes de bloquear y el chat no se borra, porque sirve de prueba."),
    ],
    A=[
        ex("Camila recibe: «Si no me la mandas, le cuento a todos que eres aburrida». Opciones: 1) enviar la foto; 2) amenazarlo con difundir algo de él; 3) decir «no», sacar una captura del mensaje, bloquearlo y mostrar la captura a una persona adulta de confianza; 4) borrar el chat y callar. ¿Cuál protege mejor?", "La 3", "No cede, no agrede y deja evidencia con apoyo adulto."),
        ex("Un amigo manda a un grupo la foto íntima de una compañera. Ricardo, que pertenece al grupo, ¿qué debe hacer? A) No reenviarla ni guardarla, no borrar el chat y avisar a un adulto. B) Reenviarla a otros para que la vean.", "A", "No reenviar y avisar frena el daño; reenviar lo aumenta."),
        ex("Valentina cuenta a su profesora jefe que le piden fotos íntimas. ¿Qué actitud debe tener la profesora? A) Escuchar sin culparla y actuar según el protocolo. B) Preguntarle por qué las envió.", "A", "La persona afectada necesita apoyo y protección, no culpa."),
    ],
    Z=[
        ex("Un joven dice: «Si ella me mandó la foto, es su problema que se difunda». ¿Qué argumento lo rebate?", "Difundir sin permiso es una decisión suya y es grave", "Quien reenvía es responsable del daño, aunque la imagen se haya enviado en confianza."),
        ex("¿Por qué conviene guardar el mensaje de presión en vez de borrarlo cuando se le muestra a una persona adulta?", "Porque sirve como evidencia para ayudar", "El mensaje permite que el adulto entienda qué pasó y actúe."),
    ],
    D=[
        arith("En un curso de 36 estudiantes, 28 dicen que no enviarían una imagen íntima y 5 no están seguros. ¿Cuántos dicen que sí la enviarían?", "36-28-5", "Al total se le restan quienes dicen que no y quienes dudan."),
        arith("Un mensaje de presión se reenvió a 4 grupos de 25 personas. ¿Cuántas personas recibieron el mensaje, si ninguna estaba en dos grupos?", "4*25", "Se multiplican los grupos por las personas de cada uno."),
    ],
    context=[ex("Un día de recreo, Lautaro ve que varios compañeros miran un celular y se ríen de una imagen íntima de una estudiante de otro curso. ¿Qué acción es más segura para él?", "Alejarse sin mirar y avisar a una persona adulta de confianza", "No participa en el daño y activa una ayuda para la afectada.")],
    selfcheck=[ex("En Orientación: ¿puedes negarte a enviar una imagen íntima?", "Sí", "Tienes derecho a decir no."), ex("¿Se puede controlar una imagen una vez enviada?", "No", "Quien la recibe puede reenviarla."), ex("¿Hay que avisar a un adulto de confianza ante la presión o la difusión?", "Sí", "Un adulto puede protegerte y actuar.")],
    task=T("Lee el caso de Joaquín y Tamara, inventados: un chico mayor le escribe a Tamara que le pida una «foto especial» y le dice que si no la envía le contará mentiras a todos. Escribe un cuadro con tres opciones de Tamara, las consecuencias de cada una y cuál elegirías. Cierra con el nombre de la persona adulta a la que ella avisaría y la frase con la que empezaría la conversación.", "Opciones: enviar la foto (pierde el control); responder con insultos (el conflicto crece); decir no, guardar una captura del mensaje, bloquearlo y avisar a su profesora jefe (queda protegida). Elijo la tercera. Frase: «Alguien me está presionando por mensajes y necesito ayuda».", ["compara tres opciones con sus consecuencias", "elige una opción que protege y no agrede", "nombra una persona adulta de confianza", "la frase inicial es clara y respetuosa"], ["cuadro escrito"], ["culpar a Tamara", "ceder por miedo a la amenaza"], "Reconoce la opción segura y pregunta qué evidencia conviene guardar."),
    reinforce="Escribe una respuesta firme y breve para negarte a enviar una imagen íntima.",
    extend="Explica por qué una persona afectada por una difusión necesita apoyo y no burlas.",
)

lesson(
    OA2, 4,
    "Una hoja y un lápiz. Las cinco fuentes de información del cuadro y los mensajes del caso están escritos en los ejercicios; no hay contenido explícito.",
    "Aprenderé a comparar fuentes de información sobre sexualidad y cuerpo y a elegir las apropiadas para mi edad. Sirve para resolver dudas sin caer en rumores ni en contenido que no corresponde.",
    ["Conozco las cuatro dimensiones de la sexualidad.", "Sé que mi intimidad se cuida."],
    [
        "Una fuente de información es el lugar o la persona de donde viene un dato. Para preguntas sobre sexualidad y cuerpo, conviene elegirlas con cuidado. Una fuente apropiada es de una persona o entidad con formación (un profesional de salud, el orientador del colegio, un libro de la biblioteca escolar, el sitio oficial de un ministerio), explica con respeto, está pensada para tu edad y se puede comprobar en más de un lugar.",
        "Cuatro preguntas ayudan a evaluar una fuente: ¿quién la escribe y qué formación tiene?, ¿para qué la hizo, para informar o para vender o impresionar?, ¿se apoya en evidencia y se puede comprobar?, ¿es adecuada para mi edad? Los rumores de recreo, los foros anónimos, los videos de influencers sin formación y los sitios con contenido para adultos suelen fallar varias de esas preguntas.",
        "El contenido pornográfico está hecho para adultos, no para educar: muestra situaciones irreales y a veces violentas, y puede dar ideas equivocadas sobre el cuerpo y las relaciones. Si te aparece sin buscarlo, ciérralo, no lo reenvíes y cuéntaselo a una persona adulta de confianza; no es tu culpa. Si te quedan dudas sobre pubertad, cuidado del cuerpo o relaciones, pregunta a un profesional de salud o a un adulto de confianza.",
    ],
    [("fuente de información", "persona, texto o sitio de donde viene un dato"), ("confiable", "que merece confianza porque se puede comprobar"), ("rumor", "dato que circula sin comprobarse"), ("evidencia", "pruebas o datos que apoyan una afirmación"), ("contenido para adultos", "imágenes o textos hechos solo para personas adultas")],
    [
        W("Evaluar una fuente", "Una duda: «¿es normal que mi cuerpo cambie distinto al de mis amigos?». Fuente 1: un rumor de recreo. Fuente 2: una profesional de salud del consultorio. ¿Cuál es más confiable?", ["La profesional de salud tiene formación.", "El rumor no se puede comprobar.", "Se prefiere a quien tiene formación y se puede consultar."], "La profesional de salud del consultorio"),
        W("Reaccionar ante contenido inadecuado", "En un grupo de chat aparece un enlace a un video para adultos. ¿Qué hace una persona del grupo?", ["No lo abre ni lo reenvía.", "Sale del enlace y avisa a un adulto.", "No es culpa de quien lo recibió."], "No abrirlo ni reenviarlo, y avisar a una persona adulta de confianza"),
    ],
    [
        M("Creer que lo que dice un video con muchos seguidores es cierto.", "Se confunde popularidad con formación.", "Revisa quién lo escribe, para qué y con qué evidencia."),
        M("Pensar que el contenido para adultos enseña cómo son las relaciones.", "Se toma una producción irreal como si fuera una guía.", "No fue creado para educar; las dudas se preguntan a un profesional."),
    ],
    R=[
        ex("Un rumor de recreo, ¿se puede comprobar o no?", "No", "No tiene un autor ni evidencia a la vista."),
        ex("Un profesional de salud, ¿es una fuente apropiada para dudas de pubertad, sí o no?", "Sí", "Tiene formación y puede orientar según tu edad."),
        ex("Si te aparece un video para adultos sin buscarlo, ¿lo reenvías o lo cierras?", "Lo cierras", "Reenviarlo amplía el daño; cerrarlo y avisar es lo seguro."),
    ],
    U=[
        ex("¿Por qué un influencer sin formación no es una fuente confiable en salud sexual? A) Porque no tiene formación comprobable. B) Porque usa redes sociales.", "A", "Lo que importa es la formación y la evidencia, no el medio."),
        ex("De las cuatro preguntas para evaluar una fuente, ¿cuál se refiere a la edad?", "¿Es adecuada para mi edad?", "Pide revisar que el contenido esté pensado para ti."),
        ex("¿El contenido pornográfico fue hecho para educar, sí o no?", "No", "Está hecho para adultos y muestra situaciones irreales."),
    ],
    A=[
        ex("Camila tiene una duda sobre cambios del cuerpo. Fuentes: 1) un foro anónimo; 2) la orientadora del colegio; 3) un video de alguien que dice ser «experto»; 4) un chat de amigas. ¿Cuál es más apropiada?", "La 2", "Tiene formación y está al alcance de su edad."),
        ex("Un grupo de 8.º revisa una web desconocida sin autor, sin fecha y que vende suplementos. ¿Es confiable? A) No, no tiene autor ni evidencia. B) Sí, porque tiene muchas fotos y se ve profesional.", "A", "Sin autor ni fecha y con ánimo de vender, falla varias preguntas."),
        ex("A Tomás le llega un video que no es para su edad. Opciones: 1) mostrarlo en el recreo; 2) cerrarlo y contárselo a una persona adulta de confianza; 3) guardarlo. ¿Cuál es segura?", "La 2", "Frena la circulación y le da apoyo adulto."),
    ],
    Z=[
        ex("¿Por qué conviene comparar una información en más de una fuente confiable?", "Para comprobar que coincide y no es un error", "Dos fuentes confiables que coinciden dan más seguridad."),
        ex("Un compañero dice: «Todos aprenden de esos videos, es normal». ¿Qué le responderías?", "Que no fueron hechos para educar y dan ideas equivocadas", "El contenido para adultos muestra situaciones irreales."),
    ],
    D=[
        arith("Un curso de 30 estudiantes preguntó de dónde sacan información: 12 de amigos, 7 de redes, 5 de la familia y el resto de profesionales. ¿Cuántos recurren a profesionales?", "30-12-7-5", "Al total se le restan los demás grupos."),
        arith("Una ficha evalúa 4 preguntas por fuente. Si el curso evalúa 5 fuentes, ¿cuántas respuestas escribe en total?", "4*5", "Se multiplican las preguntas por las fuentes."),
    ],
    context=[ex("Valeria tiene una duda sobre las infecciones de transmisión sexual. Un amigo le dice que en un foro anónimo «explican todo». ¿Qué fuente conviene más?", "Un profesional de salud o la orientadora", "Tienen formación y orientan según la edad y el contexto.")],
    selfcheck=[ex("En Orientación: ¿una fuente confiable se puede comprobar?", "Sí", "Debe apoyarse en evidencia."), ex("¿Un foro anónimo es una buena fuente en salud sexual?", "No", "No se sabe quién escribe ni qué formación tiene."), ex("¿Conviene contar a un adulto de confianza si aparece contenido que no es para tu edad?", "Sí", "No es tu culpa y un adulto puede ayudar.")],
    task=T("Lee las cinco fuentes inventadas para una duda sobre cambios del cuerpo: (a) un meme de un perfil anónimo; (b) una profesional de salud del consultorio; (c) un video de una persona que vende vitaminas; (d) un libro de la biblioteca escolar de salud adolescente; (e) un mensaje de cadena que dice «compártelo». Sepáralas en las dos más confiables y las tres menos confiables, y justifica las dos primeras con las cuatro preguntas.", "Más confiables: b y d. La profesional de salud tiene formación, informa y se puede consultar; el libro de biblioteca está pensado para la edad y se puede comprobar. Menos confiables: a, c y e; el meme anónimo, la venta de vitaminas y la cadena no se apoyan en evidencia.", ["separa las cinco fuentes en dos grupos", "usa las cuatro preguntas para justificar", "explica por qué la profesional de salud y el libro son más confiables", "no cuenta una duda personal"], ["lista ordenada con justificación"], ["confiar en la popularidad", "dejar de lado la edad"], "Reconoce las razones y pregunta cómo comprobarían un dato en una segunda fuente."),
    reinforce="Escribe cuatro preguntas para evaluar una fuente de información sobre salud.",
    extend="Explica por qué el contenido para adultos no es una fuente de educación sexual.",
)

lesson(
    OA2, 5,
    "Una hoja y un lápiz. La consulta de Lucas, personaje inventado, y los mensajes están escritos en los ejercicios. Nadie cuenta nada propio.",
    "Aprenderé a plantear una duda sobre mi cuerpo o mis relaciones a una persona adulta o a un profesional, y a usar frases claras para poner límites. Sirve para pedir ayuda a tiempo, sin vergüenza.",
    ["Sé evaluar fuentes de información.", "Sé que el consentimiento debe ser libre."],
    [
        "Comunicarse con respeto y claridad ayuda a cuidar tu intimidad. Una comunicación asertiva dice lo que piensas o sientes sin agredir ni callarte. Tiene tres partes: nombrar la situación, decir lo que sientes o quieres y proponer lo que sigue. Por ejemplo: «Cuando me tocas el pelo sin preguntar me incomoda; por favor, pregúntame antes».",
        "Para pedir ayuda sobre una duda del cuerpo, primero elige a la persona: un familiar de confianza, el orientador, la profesora jefe, una matrona o un médico del Cesfam. Luego prepara tu pregunta en una frase: «Tengo una duda sobre los cambios de mi cuerpo, ¿puede ayudarme?». No necesitas contar más de lo que quieras. Los profesionales de salud cuidan la privacidad, pero si estás en peligro tienen el deber de protegerte.",
        "Si alguien te presiona o te toca de una manera que te incomoda, puedes usar frases breves: «No me gusta», «Para ahora» o «No quiero». Después, aléjate y cuéntale a una persona adulta de confianza. Si la primera persona no te escucha, busca a otra. Puedes seguir buscando hasta que alguien te ayude. Si necesitas hablar con alguien y no sabes con quién, puedes llamar al Fono Niños 147.",
    ],
    [("asertivo", "que dice lo que piensa o siente sin agredir ni callarse"), ("privacidad", "derecho a que lo personal se mantenga en reserva"), ("profesional de salud", "persona con formación en cuidar la salud, como médico o matrona"), ("Cesfam", "centro de salud familiar de atención primaria"), ("proteger", "cuidar a alguien para que no sufra daño")],
    [
        W("Armar un mensaje asertivo", "Un compañero le toca el hombro a Lucas y a él le incomoda. Arma el mensaje en tres partes.", ["Nombra lo que ocurre: «Cuando me tocas el hombro».", "Dice lo que siente: «me incomoda».", "Propone: «por favor, no lo hagas»."], "«Cuando me tocas el hombro me incomoda; por favor, no lo hagas»"),
        W("Pedir ayuda por una duda", "Lucas tiene una duda sobre los cambios de su cuerpo y le da vergüenza. ¿Cómo la plantea?", ["Elige una persona de confianza.", "Prepara una frase corta.", "Dice solo lo que quiere contar."], "«Tengo una duda sobre los cambios de mi cuerpo, ¿puede ayudarme?» a una persona de confianza"),
    ],
    [
        M("Callar una incomodidad para no quedar mal con los demás.", "Se prefiere agradar antes que cuidarse.", "Di lo que sientes con claridad y pide ayuda si hace falta."),
        M("Creer que si una persona adulta no te escucha, el problema no importa.", "Se interpreta la falta de respuesta como falta de importancia.", "Busca a otra persona hasta que alguien te ayude."),
    ],
    R=[
        ex("¿«Para ahora, no me gusta» es una frase asertiva o una agresión?", "Asertiva", "Dice el límite sin insultar."),
        ex("Si una persona adulta no te escucha, ¿te rindes o buscas a otra persona de confianza?", "Buscas a otra persona", "Hay más personas que pueden ayudar."),
        ex("¿El Fono Niños 147 es una línea para pedir ayuda, sí o no?", "Sí", "Es la línea de ayuda que nombra esta clase."),
    ],
    U=[
        ex("¿Cuáles son las tres partes de un mensaje asertivo? A) Nombrar la situación, decir lo que sientes y proponer lo que sigue. B) Insultar, gritar y alejarse.", "A", "Esa es la estructura del mensaje asertivo."),
        ex("¿Por qué una matrona del Cesfam es una persona adecuada para una duda de cuerpo?", "Porque tiene formación en salud", "Su formación permite orientar con información comprobable."),
        ex("Un profesional de salud cuida tu privacidad, pero ¿qué debe hacer si estás en peligro?", "Protegerte", "Su deber es evitar que sufras daño."),
    ],
    A=[
        ex("Escoge el mensaje asertivo ante una broma sobre el cuerpo de Lucas: 1) «Eres un idiota»; 2) «Me incomoda esa broma, por favor para»; 3) silencio; 4) «Nunca me caes bien». ¿Cuál es?", "El 2", "Nombra la situación, dice lo que siente y pide algo concreto."),
        ex("Valentina quiere preguntar algo sobre los cambios del cuerpo. ¿Qué frase le sirve para empezar? A) «Tengo una duda sobre los cambios de mi cuerpo, ¿puede ayudarme?». B) «No sé nada y soy rara».", "A", "Es breve, clara y no se juzga a sí misma."),
        ex("Un compañero sigue molestando después de que Lucas dijo «no me gusta». ¿Qué conviene hacer después? A) Alejarse y contarle a un adulto de confianza. B) Aguantar en silencio.", "A", "Pone distancia y suma ayuda."),
    ],
    Z=[
        ex("¿Por qué no es necesario contar todo para pedir ayuda sobre una duda?", "Porque puedes decir solo lo que quieres contar", "Tienes derecho a cuidar tu intimidad y decidir cuánto compartir."),
        ex("Matías cree que pedir ayuda por un contacto incómodo es «acusar». ¿Qué le responderías?", "Que es cuidarse y proteger a otros", "Avisar a un adulto frena un daño y no es traición."),
    ],
    D=[
        arith("Un curso de 35 estudiantes anotó a quién pedirían ayuda: 14 a familiares, 9 al orientador, 7 a la profesora jefe y el resto a un profesional de salud. ¿Cuántos eligieron a un profesional de salud?", "35-14-9-7", "Al total se le restan los otros grupos."),
        arith("Una guía de ayuda tiene 3 frases asertivas por situación y 6 situaciones. ¿Cuántas frases tiene la guía?", "3*6", "Se multiplican las frases por las situaciones."),
    ],
    context=[ex("En la hora de Orientación, Daniela cuenta de forma ficticia que un compañero le pide el celular todos los días para revisar sus chats y ella se incomoda. ¿Qué dos acciones conviene que haga?", "Decirle que no con una frase asertiva y avisar a una persona adulta de confianza", "Pone el límite y suma ayuda para que no se repita.")],
    selfcheck=[ex("En Orientación: ¿un mensaje asertivo nombra la situación, lo que sientes y lo que propones?", "Sí", "Esas son sus tres partes."), ex("¿Puedes buscar a otra persona si la primera no te escucha?", "Sí", "Puedes seguir buscando ayuda."), ex("¿Hace falta contar todo para pedir ayuda?", "No", "Decides cuánto compartir.")],
    task=T("Lee las tres situaciones inventadas: (1) Sofía tiene una duda sobre los cambios del cuerpo; (2) Mateo recibe bromas sobre su cuerpo de un compañero; (3) Ámbar recibe una invitación a un juego en que debe contar secretos íntimos. Para cada una escribe: a quién recurriría y la frase exacta que diría.", "(1) A la orientadora: «Tengo una duda sobre los cambios del cuerpo, ¿puede ayudarme?». (2) Al compañero: «Me incomoda esa broma, por favor para»; y a su profesor jefe si sigue. (3) A las amigas: «No quiero contar eso»; y avisa a una persona adulta si insisten.", ["completa las tres situaciones", "cada frase es clara y respetuosa", "nombra personas adultas o profesionales", "no cuenta nada personal"], ["tabla escrita"], ["frases agresivas", "no nombrar a quién recurrir"], "Reconoce las frases claras y pregunta qué haría si la primera persona no la escuchara."),
    reinforce="Escribe un mensaje asertivo en tres partes para una situación de tu elección con un personaje de cuento.",
    extend="Explica por qué pedir ayuda a tiempo es una forma de cuidar la propia intimidad.",
)

lesson(
    OA2, 6,
    "Una hoja y un lápiz. Los tres casos nuevos están escritos en los ejercicios y ocurren entre personajes inventados. No hace falta contar experiencias propias.",
    "Aprenderé a aplicar lo aprendido sobre sexualidad, respeto, intimidad y fuentes confiables a casos nuevos. Sirve para reconocer cuándo una relación es respetuosa y cuándo hay control o presión.",
    ["Sé el significado de consentimiento.", "Sé cómo evaluar una fuente y cómo pedir ayuda."],
    [
        "Una relación respetuosa, sea de amistad o de pololeo, se reconoce porque ambas personas se escuchan, deciden juntas, aceptan un «no» y se sienten seguras. Hay señales de alerta cuando una persona controla a la otra: revisa su celular, le exige las claves, le prohíbe ver a sus amistades, se enoja por todo o la hace sentir culpable. El control no es cariño, aunque se justifique con celos.",
        "Transferir es usar lo aprendido en una situación nueva. Cuando te encuentres con un caso distinto, haz tres pasos: identifica los hechos y las dimensiones involucradas; revisa si hay consentimiento libre; y decide qué hacer y a quién pedir ayuda. Así evitas decidir por impulso, por presión del grupo o por lo que viste en un video.",
        "Cuidar la reputación de otras personas es parte del respeto. Un rumor falso sobre la vida íntima de alguien puede dañar mucho. Antes de compartir algo, pregúntate si es verdad, si es necesario y si le haría daño a alguien. Todo esto se puede analizar en tercera persona, con casos inventados, sin exponer la vida propia ni la de nadie.",
    ],
    [("pololeo", "relación afectiva entre dos jóvenes"), ("control", "intento de dominar lo que otra persona hace o con quién se junta"), ("señal de alerta", "indicio de que algo no anda bien"), ("reputación", "opinión que otros tienen de una persona"), ("transferir", "usar lo aprendido en una situación nueva")],
    [
        W("Detectar control", "Rodrigo exige a su polola las claves de su celular y se enoja cuando ella sale con amigas. ¿Es una relación respetuosa?", ["Exigir claves es control.", "Prohibir o enojarse por sus amistades limita su libertad.", "No hay respeto por su intimidad."], "No: hay señales de control"),
        W("Aplicar los tres pasos a un rumor", "Circula en un grupo el rumor de que una compañera «anda con todos». Aplica los pasos.", ["Hecho: es un rumor sin pruebas.", "Hay daño a su reputación y no hay consentimiento ni verdad.", "Acción: no compartirlo, decirle al grupo que pare y avisar a una persona adulta."], "No compartirlo, pedir que se detenga y avisar a un adulto de confianza"),
    ],
    [
        M("Creer que los celos y el control demuestran cuánto se quiere.", "Se confunde cariño con posesión.", "El cariño respeta la libertad y la intimidad de la otra persona."),
        M("Pasar un rumor «porque todos lo pasan».", "Se sigue al grupo sin pensar en el daño.", "Pregúntate si es verdad, necesario y si dañará a alguien."),
    ],
    R=[
        ex("Revisar el celular de otra persona sin permiso, ¿es respeto o control?", "Control", "Invade su intimidad."),
        ex("¿Un rumor falso puede dañar la reputación de alguien, sí o no?", "Sí", "Cambia lo que otros piensan de esa persona."),
        ex("En una relación respetuosa, ¿se acepta un «no», sí o no?", "Sí", "Aceptar un «no» es parte del respeto."),
    ],
    U=[
        ex("Ignacio dice que pide la contraseña a su polola «porque la cuida». ¿Qué falla en esa idea? A) Confunde cuidado con control. B) Nada, es cariño.", "A", "Exigir una clave invade su intimidad."),
        ex("¿Cuál de estas es una señal de alerta: que te prohíban ver a tus amistades o que te inviten a un cumpleaños?", "Que te prohíban ver a tus amistades", "Aislar a alguien es una forma de control."),
        ex("Antes de compartir algo de otra persona, ¿qué conviene preguntarse?", "Si es verdad, si es necesario y si le hará daño", "Son las tres preguntas para cuidar la reputación."),
    ],
    A=[
        ex("Un joven le dice a su polola: 1) «Puedes salir con tus amigas, diviértete»; 2) «Si sales, no me hables más»; 3) «Dame tu clave, quiero revisar»; 4) «Cuéntame si quieres». ¿Cuáles son señales de control?", "2 y 3", "Amenazar con dejar de hablar y exigir la clave controlan a la otra persona."),
        ex("Dos amigas se pelean y una crea un rumor sobre la vida íntima de la otra para vengarse. ¿Qué principio rompe? A) El respeto por la reputación y la verdad. B) Ninguno, es un juego.", "A", "Inventar un rumor daña a otra persona."),
        ex("Una pareja de 8.º toma decisiones juntos, se escuchan y cada uno tiene tiempo con amigos. ¿Es una relación respetuosa, sí o no?", "Sí", "Se escuchan, deciden juntos y mantienen su libertad."),
    ],
    Z=[
        ex("¿Por qué «es por celos» no justifica revisar el celular de la pareja?", "Porque los celos no dan derecho a invadir la intimidad", "La intimidad se respeta aunque se sienta inseguridad."),
        ex("Dos personas pololean y una se siente mal por las exigencias de la otra. ¿Qué conviene hacer, además de decirlo con claridad?", "Contárselo a una persona adulta de confianza", "Un adulto puede orientarla y protegerla si no cambia."),
    ],
    D=[
        arith("De 30 parejas ficticias de una encuesta, 18 dicen decidir juntas, 7 a veces y el resto no. ¿Cuántas parejas no deciden juntas?", "30-18-7", "Al total se le restan las que deciden juntas y las que a veces lo hacen."),
        arith("Un rumor llega a 3 chats de 24 personas cada uno, y cada persona lo reenvía a 2 personas más. ¿Cuántos reenvíos nuevos se hacen?", "3*24*2", "Se multiplican los chats, las personas de cada chat y los reenvíos por persona."),
    ],
    context=[ex("Pía revisa en secreto el celular de Camilo, su pololo, para ver con quién habla. Un día Camilo lo descubre. ¿Qué principio se rompe y qué puede hacer Camilo?", "Se rompe el respeto a la intimidad; puede decirle que no le parece bien y pedir ayuda a un adulto", "Revisar a escondidas invade su mundo privado.")],
    selfcheck=[ex("En Orientación: ¿exigir claves es una señal de control?", "Sí", "Invade la intimidad."), ex("¿Una relación respetuosa acepta un «no»?", "Sí", "Aceptarlo es respeto."), ex("¿Se puede compartir un rumor sobre la intimidad de alguien?", "No", "Daña su reputación y su dignidad.")],
    task=T("Lee los tres casos inventados: (1) Benja prohíbe a su polola subir fotos con compañeros; (2) en el curso circula que una chica «hizo algo» con un chico, sin pruebas; (3) un grupo de amigos comparte un video que una estudiante les pasó en confianza. Para cada caso escribe: qué hay de problema, qué principio se rompe y qué acción segura recomendarías.", "(1) Control: se limita su libertad; hablar con claridad y pedir ayuda adulta si sigue. (2) Rumor: daña su reputación; no compartir y avisar a un adulto. (3) Falta de confianza: se difundió algo privado; no seguir compartiéndolo, no reenviarlo y avisar a un adulto.", ["analiza los tres casos", "nombra el principio que se rompe", "recomienda una acción segura", "no cuenta nada personal"], ["tabla de tres filas"], ["justificar el control por celos", "compartir rumores"], "Reconoce el principio en cada caso y pregunta qué otra acción protegería a la persona afectada."),
    reinforce="Escribe tres señales de alerta de una relación con control para un personaje de cuento.",
    extend="Explica cómo se aplican los tres pasos (hechos, consentimiento y acción) a una situación nueva.",
)
