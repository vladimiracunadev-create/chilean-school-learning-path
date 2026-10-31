"""Cuaderno del estudiante, 5.º básico Orientación: OA 05 (prevención del consumo de drogas) y OA 06 (solidaridad, respeto y rechazo a la violencia)."""
from __future__ import annotations

from student_lessons import arith, ex
from student_content_or5_a import M, T, W, lesson

OA5, OA6 = "OR05 OA 05", "OR05 OA 06"

# ================================================================ OA 05
lesson(
    OA5, 1,
    "Una hoja y un lápiz. El caso de Noa y las listas están escritos en los ejercicios. No necesitas contar nada privado ni tocar ninguna sustancia: es un trabajo con personajes inventados.",
    "Aprenderé qué causas pueden llevar a consumir tabaco, alcohol o marihuana y qué consecuencias tienen. Sirve para tomar decisiones informadas y cuidar mi salud.",
    ["Sé que mi cuerpo es mío y merece cuidado.", "Sé separar hecho, emoción y suposición."],
    [
        "Una droga es una sustancia que, al entrar al cuerpo, cambia cómo funciona el cerebro y puede crear dependencia. Dependencia significa que el cuerpo o la mente sienten que necesitan la sustancia. Algunas drogas son legales para adultos, como el tabaco y el alcohol. Otras, como la marihuana, están muy reguladas por la ley. Que algo sea legal para un adulto no lo hace sano, y menos para una persona que está creciendo.",
        "Hay varias causas por las que alguien empieza a consumir: la curiosidad, la presión del grupo para «encajar», querer calmar una emoción difícil, copiar lo que ve en otros o tener fácil acceso. Las consecuencias pueden ser inmediatas, como sentirse mal o tener accidentes. También pueden aparecer a largo plazo: se perjudican los pulmones, el aprendizaje, la memoria, las relaciones y la salud emocional. El tabaco contiene nicotina, que genera dependencia. El alcohol afecta el equilibrio y el juicio. La marihuana puede afectar la atención y la memoria, sobre todo en cerebros que aún se están desarrollando.",
        "Piensa en Noa, una estudiante inventada. En la plaza, un joven mayor le ofrece un cigarrillo y le dice «prueba, todos lo hacen». Noa puede analizar el caso: ¿qué pasó?, ¿qué causa lo empuja a probar?, ¿qué consecuencias tendría? Pensar así antes de decidir es parte del autocuidado.",
    ],
    [("droga", "sustancia que cambia cómo funciona el cerebro y puede crear dependencia"), ("dependencia", "sentir que el cuerpo o la mente necesitan la sustancia"), ("consumo", "usar una droga"), ("causa", "razón por la que algo ocurre"), ("consecuencia", "lo que pasa después de una acción")],
    [
        W("Separar causa y consecuencia", "Un joven mayor le ofrece un cigarrillo a Noa «para encajar». ¿«Encajar» es una causa o una consecuencia?", ["La causa es la razón por la que alguien consumiría.", "Quiere encajar en el grupo.", "Es lo que motiva a probar."], "Es una causa"),
        W("Consecuencias distintas", "¿Cuál es una consecuencia a largo plazo del tabaco: «tos esa tarde» o «daño en los pulmones con los años»?", ["A largo plazo significa después de mucho tiempo.", "La tos esa tarde es inmediata.", "El daño de los pulmones ocurre con el uso repetido."], "«Daño en los pulmones con los años»"),
    ],
    [
        M("Pensar que si algo es legal para adultos, no hace daño.", "Se confunde permiso con salud.", "Que sea legal para un adulto no lo hace sano, y menos si estás creciendo."),
        M("Creer que «probar una vez» no cuenta.", "Se piensa que una vez no tiene efecto.", "Una sola vez ya puede tener riesgos y generar curiosidad por repetir."),
    ],
    R=[
        ex("El tabaco, ¿contiene nicotina que genera dependencia?", "Sí", "La nicotina hace que el cuerpo la pida."),
        ex("Querer encajar en un grupo, ¿es una causa o una consecuencia del consumo?", "Una causa", "Es una razón que empuja a probar."),
        ex("El alcohol, ¿afecta el equilibrio y el juicio?", "Sí", "Por eso aumentan los accidentes."),
    ],
    U=[
        ex("¿Por qué «es legal para adultos» no significa que sea sano para ti?", "Porque tu cuerpo está creciendo y puede dañarse", "El cuerpo y el cerebro en desarrollo son más sensibles."),
        ex("En Orientación: ¿qué es la dependencia?", "Sentir que el cuerpo o la mente necesitan la sustancia", "Es cuando cuesta dejar de usarla."),
        ex("La marihuana, ¿puede afectar la atención y la memoria?", "Sí", "Afecta el aprendizaje, sobre todo en cerebros en desarrollo."),
    ],
    A=[
        ex("Lista: 1) curiosidad, 2) presión del grupo, 3) hacer ejercicio, 4) calmar una emoción difícil. ¿Cuántas son causas que pueden llevar a consumir?", "3", "Las causas 1, 2 y 4 pueden empujar; hacer ejercicio no."),
        ex("Lista: 1) pulmones dañados, 2) mejor atención, 3) accidentes, 4) dependencia. ¿Cuántas son consecuencias negativas?", "3", "Las consecuencias 1, 3 y 4 perjudican; mejor atención no."),
        ex("Noa piensa: «¿Qué pasó? Me ofrecieron un cigarro. ¿Qué causa? Querer encajar». ¿Qué falta para analizar el caso completo: las consecuencias o la marca del cigarro?", "Las consecuencias", "Analizar es ver qué pasó, por qué y qué podría pasar."),
    ],
    Z=[
        ex("Alguien dice: «Todos lo hacen, así que no hace daño». ¿Qué error comete?", "Confunde lo que muchos hacen con lo que es sano", "Que muchos lo hagan no cambia el daño."),
        ex("¿Por qué es mejor analizar las consecuencias antes de decidir?", "Porque ayuda a prever lo que pasa después", "Así se decide con información, no por presión."),
    ],
    D=[
        arith("En una encuesta inventada de 40 estudiantes, 5 dicen que alguna vez sintieron presión para consumir. ¿Cuántos no la sintieron?", "40-5", "Se restan los que la sintieron al total."),
        arith("En un cartel de prevención hay 3 filas de 6 dibujos de hábitos saludables. ¿Cuántos dibujos hay?", "3*6", "Son 3 filas con 6 dibujos cada una."),
    ],
    context=[ex("En un cumpleaños, un joven mayor ofrece cerveza a un niño inventado y dice «todos toman». El niño piensa en causas y consecuencias antes de decidir. ¿Qué hizo?", "Analizó el caso", "Pensó en la causa de la presión y en lo que podría pasar.")],
    selfcheck=[ex("En Orientación: ¿el tabaco crea dependencia?", "Sí", "Por la nicotina."), ex("¿La presión del grupo es una causa del consumo?", "Sí", "Algunas personas prueban por encajar."), ex("¿Analizar consecuencias ayuda a decidir?", "Sí", "Permite prever lo que pasa después.")],
    task=T("Lee el caso: «En la plaza, un joven mayor le ofrece un cigarrillo a Noa y le dice que todos lo hacen». Escribe: qué pasó, dos causas por las que Noa podría sentir ganas de probar, y dos consecuencias (una inmediata y una a largo plazo) de consumir tabaco.", "Qué pasó: le ofrecieron un cigarro. Causas: presión del grupo y curiosidad. Consecuencias: sentirse mal ese día; daño a los pulmones con los años.", ["escribe el hecho", "dos causas", "una consecuencia inmediata y una a largo plazo"], ["texto escrito o dicho"], ["mezclar causa con consecuencia", "decir «todos lo hacen» como razón"], "Reconoce el análisis y pregunta qué decisión tomaría Noa."),
    reinforce="Escribe tres causas por las que alguien podría consumir alcohol y una consecuencia de cada una.",
    extend="Explica por qué la edad es importante cuando se habla del consumo de drogas.",
)

lesson(
    OA5, 2,
    "Una hoja y un lápiz. Las frases de presión y los mitos están escritos en los ejercicios.",
    "Aprenderé a distinguir hechos de mitos sobre el consumo, a reconocer lo que siento ante la presión y a poner un límite. Sirve para decidir con claridad.",
    ["Sé analizar causas y consecuencias.", "Sé qué es la dependencia."],
    [
        "Ante una oferta de consumo se mezclan tres cosas. El hecho es lo que pasó: «Me ofrecieron un cigarro». La emoción es lo que sientes: nervios, curiosidad, miedo a quedar fuera. El límite es lo que decides no hacer: «No quiero». Separarlos ayuda a no dejarte llevar por la emoción del momento.",
        "También hay mitos, que son ideas falsas que parecen ciertas. «Todos lo hacen» es falso: la mayoría de los niños de tu edad no consume. «Solo se hace daño quien consume mucho» es falso: incluso poco puede dañar. «Los cigarros electrónicos son seguros» es falso: muchos contienen nicotina. «Si es natural no hace daño» es falso: algunas plantas pueden dañar. Para comprobar un dato, busca una fuente confiable.",
        "Un límite claro se dice con pocas palabras y sin pedir perdón: «No, gracias». No necesitas dar explicaciones largas ni inventar excusas. Si insisten, repites el límite o te vas. Tu decisión es válida aunque otros no la compartan.",
    ],
    [("mito", "idea falsa que parece cierta"), ("presión de grupo", "insistencia de otros para que hagas algo"), ("límite", "lo que decido no hacer"), ("curiosidad", "ganas de probar o saber algo"), ("fuente confiable", "lugar de información con autor identificable")],
    [
        W("Separar hecho, emoción y límite", "Noa dice: «Me ofrecieron un cigarro, me dio curiosidad y miedo a quedar fuera, pero decidí que no». ¿Cuál es el límite?", ["El hecho es la oferta.", "Las emociones son curiosidad y miedo.", "El límite es la decisión de no."], "«Decidí que no»"),
        W("Detectar un mito", "¿«Todos los de mi edad ya lo probaron» es un hecho o un mito?", ["Se puede comprobar con datos confiables.", "La mayoría de los niños de tu edad no consume.", "Es una idea falsa."], "Es un mito"),
    ],
    [
        M("Creer que decir no me deja fuera del grupo.", "Se piensa que solo los que aceptan son parte.", "Un buen grupo respeta tu decisión; puedes seguir con otras actividades."),
        M("Inventar una excusa larga para no consumir.", "Se cree que hay que justificarse.", "Basta con un «no, gracias» claro."),
    ],
    R=[
        ex("«Los cigarros electrónicos son seguros». ¿Es un hecho o un mito?", "Un mito", "Muchos contienen nicotina y pueden dañar."),
        ex("«No, gracias». ¿Es un límite claro?", "Sí", "Dice la decisión con pocas palabras."),
        ex("«Me da curiosidad». ¿Es una emoción o un límite?", "Una emoción", "Dice lo que siente la persona."),
    ],
    U=[
        ex("¿Por qué «solo daña a quien consume mucho» es un mito?", "Porque incluso poco puede dañar", "Incluso poco puede dañar un cuerpo que está creciendo."),
        ex("¿Qué debes hacer si insisten después de decir no?", "Repetir el límite o irme", "Es una forma segura de mantener tu decisión."),
        ex("¿Cómo se comprueba un dato dudoso?", "Con una fuente confiable", "Así se evita creer un mito."),
    ],
    A=[
        ex("Frases: 1) «Me ofrecieron alcohol», 2) «Siento nervios», 3) «No quiero tomar». ¿Cuál es el límite?", "La frase 3", "Dice lo que decide no hacer."),
        ex("Lista: 1) «Todos lo hacen», 2) «Es natural, así que no daña», 3) «Mi cuerpo está creciendo y puede dañarse», 4) «Solo un poco no pasa nada». ¿Cuántos son mitos?", "3", "Las frases 1, 2 y 4 son ideas falsas; la 3 es un hecho."),
        ex("Un amigo insiste: «¿Qué te cuesta probar?». ¿Qué responde Noa con un límite claro: «No, gracias» o «Bueno, pero solo una vez»?", "«No, gracias»", "Mantiene su decisión sin dar vueltas."),
    ],
    Z=[
        ex("Si todos tus amigos dijeran que sí, ¿cambiaría eso el daño que produce la sustancia?", "No", "El daño depende de la sustancia, no de quién la use."),
        ex("¿Por qué es importante distinguir emoción de hecho antes de decidir?", "Porque la emoción puede empujar a decidir sin pensar", "El hecho te ayuda a ver la situación completa."),
    ],
    D=[
        arith("De 25 estudiantes inventados, 22 dicen que no consumirían ante presión. ¿Cuántos no están seguros?", "25-22", "Se restan los seguros al total."),
        arith("Una escala de presión va de 0 a 10. Noa sentía un 8 y bajó 3 puntos al alejarse del grupo. ¿En qué punto quedó?", "8-3", "Se restan los puntos que bajó."),
    ],
    context=[ex("En un cumpleaños, una niña inventada dice «no, gracias» al ofrecerle alcohol y se sienta con otros amigos. ¿Qué hizo?", "Puso un límite claro y se fue con otros amigos", "Dijo no y cambió de lugar.")],
    selfcheck=[ex("En Orientación: ¿«todos lo hacen» es un hecho?", "No", "Es un mito."), ex("¿Basta con decir «no, gracias»?", "Sí", "El límite no necesita excusas."), ex("¿Se comprueba un dato con una fuente confiable?", "Sí", "Así se evitan los mitos.")],
    task=T("Lee tres frases de presión: «Prueba una sola vez», «Todos lo hacen», «No seas cobarde». Para cada una escribe: (a) qué tipo de presión es, (b) una respuesta con límite claro. Después escribe un mito sobre el consumo y el dato correcto.", "«Prueba una sola vez»: insiste. Respuesta: «No, gracias». Mito: «Los vapeadores son seguros»; dato: contienen nicotina y pueden dañar.", ["clasifica tres frases de presión", "escribe tres límites claros", "mito y dato correcto"], ["lista escrita"], ["pedir perdón por decir no", "mito sin dato"], "Reconoce los límites y pregunta cómo le ayudaría un amigo."),
    reinforce="Escribe tres formas de decir no sin dar explicaciones largas.",
    extend="Busca (con un adulto) un dato confiable sobre el tabaco y anota la fuente.",
)

lesson(
    OA5, 3,
    "Una hoja y un lápiz. Las listas de factores y de estrategias para el estrés están escritas en los ejercicios.",
    "Aprenderé a comparar factores que protegen del consumo y estrategias para manejar el estrés, y a prever sus consecuencias. Sirve para fortalecer mi autocuidado.",
    ["Sé separar hecho, emoción y límite.", "Sé reconocer causas y consecuencias del consumo."],
    [
        "Un factor de riesgo es algo que aumenta la probabilidad de consumir, como la presión del grupo, el fácil acceso o el estrés sin apoyo. Un factor protector es algo que la disminuye: hablar con un adulto de confianza, tener amistades que se cuidan, hacer deporte o arte, tener metas, sentirse parte del colegio y conocer formas de decir que no. Tener más factores protectores ayuda, pero no asegura nada: hay que seguir cuidándose.",
        "El estrés es la reacción del cuerpo cuando algo exige mucho: una prueba, una discusión o muchas tareas. Se nota en el cuerpo (cansancio, dolor de cabeza) y en las emociones (nerviosismo, irritación). Hay maneras sanas de manejarlo: dormir lo necesario, comer a las horas, moverte, respirar con calma, conversar con alguien de confianza y organizar el tiempo. Hay maneras que dañan: aislarse, enojarse con todos o intentar calmarlo con alcohol, tabaco u otra droga, porque el problema sigue y se suma otro.",
        "Compara estrategias con dos preguntas: ¿me ayuda de verdad a sentirme mejor después? ¿Me puede hacer daño o crear un nuevo problema? Una estrategia sana alivia sin dañar.",
    ],
    [("factor de riesgo", "algo que aumenta la probabilidad de consumir"), ("factor protector", "algo que disminuye esa probabilidad"), ("estrés", "reacción del cuerpo cuando algo exige mucho"), ("hábito saludable", "costumbre que cuida el cuerpo y la mente"), ("estrategia", "plan de acciones para lograr algo")],
    [
        W("Clasificar factores", "¿«Hacer deporte con amigos» es un factor de riesgo o un factor protector?", ["Un factor protector disminuye la probabilidad de consumir.", "El deporte ocupa el tiempo y cuida el cuerpo.", "Los amigos que se cuidan también ayudan."], "Un factor protector"),
        W("Comparar estrategias para el estrés", "Noa tiene una prueba y siente estrés. Opción A: dormir bien y repasar un rato cada día. Opción B: fumar un cigarro para calmarse. ¿Cuál es mejor y por qué?", ["A alivia sin dañar y avanza el problema.", "B crea dependencia y no resuelve la prueba.", "Una estrategia sana alivia sin dañar."], "A, porque alivia sin crear otro problema"),
    ],
    [
        M("Pensar que el alcohol o el tabaco calman el estrés.", "Se siente alivio corto, pero el problema sigue.", "Elige estrategias sanas como dormir, moverte o conversar."),
        M("Creer que si tengo factores protectores, ya no necesito cuidarme.", "Se piensa que están garantizados.", "Los factores protectores ayudan, pero hay que seguir decidiendo con cuidado."),
    ],
    R=[
        ex("«Presión del grupo». ¿Es factor de riesgo o factor protector?", "Factor de riesgo", "Aumenta la probabilidad de consumir."),
        ex("«Hablar con un adulto de confianza». ¿Es factor de riesgo o factor protector?", "Factor protector", "Da apoyo y reduce la probabilidad de consumir."),
        ex("Dormir bien, ¿es un hábito saludable?", "Sí", "Cuida el cuerpo y ayuda con el estrés."),
    ],
    U=[
        ex("¿Por qué tener factores protectores no asegura que nunca habrá riesgo?", "Porque igual hay que decidir con cuidado", "Ayudan, pero no reemplazan las decisiones."),
        ex("¿Por qué usar alcohol o tabaco para calmar el estrés no resuelve el problema?", "Porque el problema sigue y se suma otro", "El alivio dura poco y crea riesgos."),
        ex("¿Qué dos preguntas sirven para comparar estrategias de estrés?", "Si me ayuda de verdad y si me puede hacer daño", "Así se elige una estrategia sana."),
    ],
    A=[
        ex("Lista: 1) dormir bien, 2) fumar para calmarse, 3) caminar un rato, 4) conversar con una persona de confianza. ¿Cuántas son estrategias sanas?", "3", "Las 1, 3 y 4 alivian sin dañar."),
        ex("Factores: 1) deporte, 2) presión del grupo, 3) metas claras, 4) fácil acceso. ¿Cuántos son protectores?", "2", "Deporte y metas claras protegen; los otros son de riesgo."),
        ex("Noa tiene mucho que hacer. ¿Qué estrategia es mejor: hacer una lista y empezar por lo más urgente o quedarse en la cama todo el día?", "Hacer una lista y empezar por lo más urgente", "Organiza el tiempo y baja el estrés."),
    ],
    Z=[
        ex("Dos niños tienen estrés por una prueba. Uno conversa con su profesor y repasa. El otro se aísla. ¿Cuál tiene más probabilidad de manejar mejor el estrés?", "El que conversa y repasa", "Pedir apoyo y actuar lo ayuda."),
        ex("¿Por qué es útil tener varias estrategias sanas y no solo una?", "Porque no todas sirven en todas las situaciones", "Con más opciones se elige la más adecuada."),
    ],
    D=[
        arith("Noa duerme 9 horas cada noche durante 5 noches. ¿Cuántas horas duerme en total?", "9*5", "Son 9 horas repetidas 5 noches."),
        arith("Una semana tiene 7 días. Noa se movió 30 minutos en 5 de esos días. ¿Cuántos minutos se movió en total?", "30*5", "Son 30 minutos en 5 días."),
    ],
    context=[ex("Antes de exponer, un niño inventado siente nervios. Respira 4 veces, repasa su guion y habla con su profesora. ¿Usó estrategias sanas?", "Sí", "Respirar, repasar y conversar alivian sin dañar.")],
    selfcheck=[ex("En Orientación: ¿hacer deporte es un factor protector?", "Sí", "Cuida el cuerpo y ocupa el tiempo."), ex("¿El tabaco resuelve el estrés?", "No", "Solo crea otro problema."), ex("¿Dormir bien ayuda con el estrés?", "Sí", "Es un hábito saludable.")],
    task=T("Escribe dos columnas: «Factores protectores» y «Factores de riesgo». Escribe tres en cada una usando ideas de la clase. Después escribe tres estrategias sanas para manejar el estrés antes de una prueba y una estrategia que NO ayudaría, con la razón.", "Protectores: deporte, adultos que escuchan, metas. Riesgo: presión del grupo, fácil acceso, estrés sin apoyo. Estrategias sanas: dormir, respirar, repasar. No ayuda: tabaco, porque crea dependencia.", ["tres factores en cada columna", "tres estrategias sanas", "una estrategia que no ayuda y la razón"], ["tabla escrita"], ["mezclar columnas", "no explicar la razón"], "Reconoce las listas y pregunta cuál estrategia usaría primero."),
    reinforce="Escribe dos hábitos saludables que puedas hacer en una semana normal.",
    extend="Explica cómo un hábito saludable puede disminuir el riesgo de consumir.",
)

lesson(
    OA5, 4,
    "Una hoja y un lápiz. Las situaciones y el plan de Noa están escritos en los ejercicios.",
    "Aprenderé a elegir una acción segura ante una oferta de consumo y a armar un plan de hábitos saludables. Sirve para actuar con seguridad y pedir ayuda cuando haga falta.",
    ["Sé reconocer factores protectores y de riesgo.", "Sé decir «no, gracias» con firmeza."],
    [
        "Cuando alguien te ofrece una sustancia, hay cuatro pasos seguros. Primero, di un «no» claro: «No, gracias». Segundo, propone otra actividad: «Mejor juguemos a la pelota». Tercero, si insisten, aléjate y ve con personas que te cuiden. Cuarto, cuéntaselo a un adulto de confianza. Contar no es acusar: es cuidarte y cuidar a otros.",
        "Nunca pruebes algo desconocido, aunque se vea como un dulce o una pastilla. Los medicamentos solo los da un adulto responsable. Si alguien parece estar mal después de consumir, no lo dejes solo: avisa de inmediato a un adulto. Si sientes que tú o alguien cercano consume y no puede parar, hay ayuda: una persona adulta de confianza, el orientador del colegio o un centro de salud.",
        "Un plan de hábitos saludables también protege. Incluye dormir lo necesario, comer a las horas, moverte todos los días, tener tiempo con amigos que te cuidan y practicar algo que te guste. Se puede medir con un registro semanal. Cuanto más claro es el plan, más fácil es cumplirlo.",
    ],
    [("alternativa", "otra actividad que propongo"), ("alejarse", "irse de un lugar para cuidarse"), ("centro de salud", "lugar donde profesionales atienden la salud"), ("plan", "conjunto de acciones para lograr algo"), ("registro", "anotación de lo que hice")],
    [
        W("Los cuatro pasos", "Un compañero ofrece un vapeador a Noa. Ordena: A) contarle a un adulto, B) decir «no, gracias», C) alejarse. ¿Cuál va primero?", ["Primero se dice el límite.", "Si insisten, se aleja.", "Después se cuenta a un adulto."], "B"),
        W("Contar no es acusar", "Noa duda: «Si le cuento a la orientadora, voy a ser una soplona». ¿Qué responde un amigo?", ["Contar busca cuidar.", "El adulto puede ayudar a quien lo necesita.", "No es traicionar."], "Contar es cuidar, no acusar"),
    ],
    [
        M("Aceptar una pastilla de un compañero porque «es solo un dulce».", "No se sabe qué es; se confía sin comprobar.", "No pruebes nada desconocido; los medicamentos los da un adulto."),
        M("Dejar solo a quien parece estar mal.", "Se tiene miedo de meterse en problemas.", "Avisa de inmediato a un adulto."),
    ],
    R=[
        ex("Si te ofrecen una sustancia, ¿el primer paso es decir un «no» claro o aceptarla?", "Decir un «no» claro", "El límite protege tu decisión."),
        ex("Una pastilla desconocida, ¿se puede probar?", "No", "No se sabe qué es ni qué daño puede hacer."),
        ex("Si alguien está mal después de consumir, ¿lo dejas solo o avisas a un adulto?", "Avisas a un adulto", "Puede necesitar ayuda urgente."),
    ],
    U=[
        ex("¿Para qué sirve proponer una alternativa?", "Para cambiar la situación sin pelear", "Da otra opción para estar juntos."),
        ex("¿Por qué contar a un adulto no es acusar?", "Porque busca cuidar", "Es una forma de proteger."),
        ex("¿Quiénes pueden ayudar si alguien no puede dejar de consumir?", "Un adulto de confianza, el orientador o un centro de salud", "Hay personas preparadas para apoyar."),
    ],
    A=[
        ex("Noa dijo «no, gracias» y se fue con otros amigos. ¿Qué dos pasos usó: decir no y alejarse, o proponer una alternativa y contar a un adulto?", "Decir no y alejarse", "Dijo el límite y se fue del lugar."),
        ex("Un compañero le ofrece una pastilla a Noa y dice «es un dulce». ¿Qué hace Noa: decir «no, gracias» y avisar a un adulto, o probar un poco?", "Decir «no, gracias» y avisar a un adulto", "Es la acción segura."),
        ex("Noa propone: «Mejor juguemos a la pelota». ¿Qué paso usó: proponer una alternativa o alejarse?", "Proponer una alternativa", "Ofrece otra actividad sin pelear."),
    ],
    Z=[
        ex("¿Por qué conviene tener un plan de hábitos saludables antes de que ocurra una oferta de consumo?", "Porque ayuda a decidir con calma y ocupa el tiempo", "Un plan previo reduce la presión del momento."),
        ex("Una niña ve a un compañero mareado después de consumir algo. Piensa «no me meto». ¿Qué debería hacer?", "Avisar de inmediato a un adulto", "Puede ser una emergencia."),
    ],
    D=[
        arith("Noa se propuso moverse 30 minutos al día durante 5 días y logró 4 días. ¿Cuántos minutos se movió?", "30*4", "Son 30 minutos en 4 días."),
        arith("Noa durmió 9 horas el lunes, 8 el martes y 9 el miércoles. ¿Cuántas horas durmió en total?", "9+8+9", "Se suman las horas de cada noche."),
    ],
    context=[ex("En una fiesta, un niño inventado recibe una pastilla que le ofrece un desconocido. Dice «no, gracias», se va con personas que lo cuidan y se lo cuenta a un adulto. ¿Cuántos de los cuatro pasos usó?", "3", "Dijo no, se alejó y contó (no propuso alternativa)."),],
    selfcheck=[ex("En Orientación: ¿conviene contar a un adulto una oferta de consumo?", "Sí", "Contar a un adulto cuida a todos."), ex("¿Se prueba una pastilla desconocida?", "No", "Puede ser peligrosa."), ex("¿Un plan de hábitos saludables ayuda?", "Sí", "Protege el cuerpo y la mente.")],
    task=T("Escribe un plan de acción para esta situación inventada: «En la plaza, un joven mayor ofrece alcohol a Noa y a su amigo». Incluye los cuatro pasos seguros con una frase para cada uno. Después escribe un plan semanal de hábitos saludables con cuatro hábitos y cuántas veces los harás.", "No: «No, gracias». Alternativa: «Vamos a jugar». Alejarse: nos vamos al otro lado. Contar: se lo digo a mi profesora. Plan: dormir 9 horas (7 noches), moverme 30 minutos (5 días), comer a las horas (7 días), ver amigos (3 veces).", ["cuatro pasos con una frase cada uno", "cuatro hábitos con frecuencia", "no incluye experiencias personales"], ["texto escrito", "tabla semanal"], ["omitir contar a un adulto", "hábitos sin frecuencia"], "Reconoce el plan y pregunta a qué adulto acudiría."),
    reinforce="Escribe una frase para decir no y una para proponer una alternativa.",
    extend="Haz una lista de tres lugares o personas donde pedir ayuda si alguien necesita apoyo con el consumo.",
)

# ================================================================ OA 06
lesson(
    OA6, 1,
    "Una hoja y un lápiz. El caso de Noa y las frases de buen trato están escritos en los ejercicios.",
    "Aprenderé a ponerme en el lugar del otro (empatía) y a usar un buen trato. Sirve para convivir con respeto y ayudar a quien lo necesita.",
    ["Sé que las emociones se describen con intensidad.", "Sé que cada persona es distinta."],
    [
        "Empatía es ponerse en el lugar de otra persona para entender qué siente y qué necesita. Para practicarla, hazte tres preguntas: ¿qué pasó?, ¿cómo se puede sentir?, ¿qué puedo hacer para ayudar? La empatía no significa estar de acuerdo con todo, sino entender y tratar bien.",
        "El buen trato son gestos simples que muestran respeto: saludar, despedirse, decir «por favor» y «gracias», esperar tu turno, escuchar sin interrumpir y hablar con voz calmada. Un buen trato hace que el curso sea un lugar más amable.",
        "Piensa en Noa, una estudiante inventada. Llega un compañero nuevo, Samir. Habla poco y está empezando en un colegio nuevo. Noa se pone en su lugar: imagina que se siente solo. Le dice «hola», le muestra dónde está el baño y lo invita a sentarse con ellos. Ese es un ejemplo de empatía con buen trato.",
    ],
    [("empatía", "ponerme en el lugar del otro para entender lo que siente"), ("buen trato", "gestos de respeto como saludar y decir por favor"), ("solidaridad", "ayudar a quien lo necesita"), ("convivencia", "vivir y trabajar con otros en armonía"), ("respeto", "tratar a todos con consideración")],
    [
        W("Practicar empatía", "Samir llegó nuevo y está solo en el recreo. ¿Qué pregunta de empatía haces primero: «¿Cómo se puede sentir?» o «¿Qué ropa trae?»", ["La empatía mira lo que siente el otro.", "Samir está solo y es nuevo.", "Puede sentir soledad."], "«¿Cómo se puede sentir?»"),
        W("Un gesto de buen trato", "Noa saluda a Samir y le muestra dónde está el baño. ¿Eso es buen trato?", ["Saludar es un gesto de respeto.", "Mostrar el baño es ayudar.", "Ambos hacen sentir bienvenido."], "Sí, es buen trato"),
    ],
    [
        M("Creer que empatía es estar de acuerdo con todo.", "Se confunde entender con aprobar.", "Empatía es entender lo que siente el otro, aunque no pienses igual."),
        M("Pensar que el buen trato es solo para los adultos.", "Se cree que «por favor» no es para niños.", "El buen trato sirve en todo momento y con todas las personas."),
    ],
    R=[
        ex("Empatía, ¿es ponerse en el lugar del otro o hacer lo que uno quiere?", "Ponerse en el lugar del otro", "Busca entender lo que siente."),
        ex("«Por favor» y «gracias», ¿son gestos de buen trato?", "Sí", "Muestran respeto por la otra persona."),
        ex("Ayudar a alguien que lo necesita, ¿es solidaridad?", "Sí", "Es dar apoyo a otros."),
    ],
    U=[
        ex("¿Por qué empatía no significa estar de acuerdo?", "Porque es entender sin aprobar", "Se puede entender a alguien aunque pienses distinto."),
        ex("¿Qué tres preguntas ayudan a practicar la empatía?", "Qué pasó, cómo se puede sentir, qué puedo hacer", "Ordenan la mirada hacia el otro."),
        ex("¿Por qué el buen trato mejora la convivencia?", "Porque todos se sienten respetados", "El respeto crea un ambiente amable."),
    ],
    A=[
        ex("Gestos: 1) saludar, 2) interrumpir, 3) decir «gracias», 4) esperar tu turno. ¿Cuántos son buen trato?", "3", "Los gestos 1, 3 y 4 son respetuosos; interrumpir no."),
        ex("Samir está callado. Noa se pone en su lugar y piensa «puede sentirse solo». ¿Qué paso de empatía hizo?", "Pensó cómo se puede sentir", "Es la segunda pregunta de empatía."),
        ex("Samir no sabe dónde está la biblioteca. ¿Qué acción es solidaria: acompañarlo hasta allá o decirle que la busque solo?", "Acompañarlo hasta allá", "Es una ayuda concreta y amable."),
    ],
    Z=[
        ex("Un niño dice: «A mí no me importa lo que sienta el nuevo». ¿Qué le falta?", "Empatía", "No intenta entender al otro."),
        ex("¿Por qué ayudar sin humillar es parte del buen trato?", "Porque respeta la dignidad del otro", "Ayudar bien no hace sentir inferior a nadie."),
    ],
    D=[
        arith("En un curso de 30 estudiantes, 12 saludaron a Samir y 8 lo invitaron a jugar. ¿Cuántos gestos en total?", "12+8", "Se suman los dos grupos."),
        arith("Noa saludó a 3 compañeros cada día durante 5 días. ¿Cuántos saludos dio?", "3*5", "Son 3 saludos cada uno de los 5 días."),
    ],
    context=[ex("En el recreo, una niña inventada ve a un compañero con una mochila rota. Le dice «¿Quieres que te ayude a llevar tus cosas?». ¿Qué mostró?", "Empatía y solidaridad", "Pensó en lo que necesitaba y ofreció ayuda.")],
    selfcheck=[ex("En Orientación: ¿la empatía es entender al otro?", "Sí", "Es ponerse en su lugar."), ex("¿Saludar es buen trato?", "Sí", "Es un gesto de respeto."), ex("¿Ayudar es solidaridad?", "Sí", "Es apoyar a quien lo necesita.")],
    task=T("Lee: «Una compañera nueva, Aya, llegó de otro país. No conoce las reglas del patio y se queda sola». Escribe tres respuestas a las preguntas de empatía (qué pasó, cómo se puede sentir, qué puedo hacer) y tres frases de buen trato que le dirías.", "Qué pasó: llegó nueva. Cómo se puede sentir: sola. Qué puedo hacer: invitarla a jugar. Frases: «Hola, soy Noa», «¿Quieres jugar con nosotros?», «Gracias por venir».", ["responde las tres preguntas", "tres frases de buen trato", "no hace preguntas personales"], ["texto escrito o dicho"], ["decir solo «ayudarla» sin explicar cómo", "frases que obligan"], "Reconoce la empatía y pregunta cómo se sentiría Aya."),
    reinforce="Escribe tres gestos de buen trato que puedas hacer cada día en el colegio.",
    extend="Escribe cómo mostrarías empatía con alguien que piensa distinto a ti.",
)

lesson(
    OA6, 2,
    "Una hoja y un lápiz. Los casos de Noa y Sam están escritos en los ejercicios.",
    "Aprenderé a distinguir diferencias de discriminación y violencia, y a poner límites. Sirve para rechazar toda forma de violencia y respetar el derecho de todos a ser diferentes.",
    ["Sé qué es empatía y buen trato.", "Sé separar hecho, emoción y límite."],
    [
        "Las personas somos diferentes en origen, etnia, género, religión, nacionalidad, forma de hablar, familia y gustos. Todas tienen los mismos derechos. Discriminar es tratar peor a alguien por una de esas características. Por ejemplo, no dejar jugar a un niño porque habla otro idioma, reírse de la religión de otro, burlarse de alguien por pertenecer a un pueblo originario o decir que ciertas cosas son «solo de niñas» o «solo de niños».",
        "La violencia es cualquier acción que hiere a otro. Puede ser física (golpear, empujar), verbal (insultar, gritar), psicológica (aislar, amenazar) o por pantalla (burlas o mensajes que hieren, llamado ciberacoso). Una broma es parte de un juego en que todos se ríen. Una burla hiere y se repite. Si alguien se siente mal, deja de ser broma.",
        "Para actuar, separa tres cosas: el hecho (qué pasó), la emoción (cómo se siente la víctima y cómo me siento yo) y el límite (esto no está bien). Todos tienen derecho a opinar y a ser diferentes. Rechazar la violencia es decir con claridad «eso no se hace» y pedir ayuda cuando haga falta.",
    ],
    [("discriminación", "tratar peor a alguien por una característica suya"), ("violencia", "acción que hiere a otra persona"), ("ciberacoso", "agresión repetida por pantalla"), ("etnia", "grupo de personas con cultura y origen común"), ("derecho", "algo que todos pueden tener y exigir")],
    [
        W("Discriminación o no", "Un grupo no deja jugar a Aya porque habla con acento distinto. ¿Es discriminación?", ["Aya recibe un trato peor.", "El motivo es su forma de hablar.", "Eso es discriminar."], "Sí, es discriminación"),
        W("Broma o burla", "Un grupo se ríe de un niño todos los días por su nombre, y el niño no se ríe. ¿Es una broma o una burla?", ["En una broma todos se ríen.", "Aquí el niño se siente mal.", "Se repite cada día."], "Es una burla"),
    ],
    [
        M("Pensar que si es «solo una broma», no hiere.", "Se mide por la intención de quien bromea.", "Si alguien se siente mal, deja de ser broma."),
        M("Creer que ser diferente es un problema.", "Se confunde diferente con peor.", "Las diferencias son parte de ser personas; todos tienen los mismos derechos."),
    ],
    R=[
        ex("Insultar, ¿es violencia verbal o física?", "Verbal", "Hiere con palabras."),
        ex("No dejar jugar a alguien por su religión, ¿es discriminación?", "Sí", "Se trata peor por una característica."),
        ex("Una broma en la que todos se ríen, ¿hiere?", "No", "Una broma es parte del juego para todos."),
    ],
    U=[
        ex("¿Por qué una burla repetida no es broma?", "Porque hiere y se repite", "La víctima se siente mal."),
        ex("En Orientación: ¿qué es el ciberacoso?", "Una agresión repetida por pantalla", "Ocurre en redes o mensajes."),
        ex("¿Qué derecho tienen todos aunque sean diferentes?", "Ser respetados y opinar", "Los derechos son para todas las personas."),
    ],
    A=[
        ex("Situaciones: 1) empujar, 2) saludar, 3) aislar a alguien, 4) mensajes burlescos. ¿Cuántas son violencia?", "3", "Empujar, aislar y burlarse por mensajes hieren."),
        ex("Sam dice: «Eso es solo para niñas, tú no puedes». ¿Es discriminación por género?", "Sí", "Trata peor a alguien por ser niño o niña."),
        ex("Una niña ve que se burlan de la religión de una compañera. ¿Qué límite puede decir: «Eso no se hace; respetemos» o «Es verdad, qué raro»?", "«Eso no se hace; respetemos»", "Rechaza la discriminación con claridad."),
    ],
    Z=[
        ex("Alguien dice: «Yo no discrimino, solo me río». ¿Qué problema tiene?", "Reírse de otros por lo que son es discriminar", "La burla también discrimina."),
        ex("¿Por qué es importante respetar el derecho a opinar aunque pienses distinto?", "Porque todos merecen ser escuchados", "El respeto incluye aceptar opiniones diferentes."),
    ],
    D=[
        arith("En un curso de 28 estudiantes, 4 dicen que han visto una burla esta semana. ¿Cuántos no la vieron?", "28-4", "Se restan los que la vieron al total."),
        arith("En una semana hubo 2 burlas el lunes, 3 el miércoles y 1 el viernes. ¿Cuántas en total?", "2+3+1", "Se suman las burlas de cada día."),
    ],
    context=[ex("En el patio, un niño inventado dice «ese juego es solo de niñas» y no deja jugar a Nico. Nico se va triste. ¿Qué tipo de trato hubo?", "Discriminación por género", "Se trató peor a Nico por ser niño.")],
    selfcheck=[ex("En Orientación: ¿discriminar es tratar peor por una característica?", "Sí", "Es la definición."), ex("¿Una burla repetida hiere?", "Sí", "Deja de ser broma."), ex("¿Todos tienen derecho a ser diferentes?", "Sí", "Los derechos son para todos.")],
    task=T("Lee tres casos: A) no dejan jugar a Aya porque nació en otro país; B) se ríen de la religión de un niño; C) dicen que cocinar es solo de niñas. Para cada caso escribe: el hecho, cómo se puede sentir la persona afectada, el límite que dirías y si es discriminación por etnia, nacionalidad, religión o género.", "A: nacionalidad; ella puede sentir soledad; «todos pueden jugar». B: religión; vergüenza; «no se bromea con eso». C: género; molestia; «cocinar es para todos».", ["hecho, emoción y límite en cada caso", "tipo de discriminación", "lenguaje respetuoso"], ["tabla escrita"], ["usar insultos", "confundir el tipo"], "Reconoce la clasificación y pregunta qué haría alguien que lo ve."),
    reinforce="Explica con tus palabras la diferencia entre broma y burla.",
    extend="Escribe una frase que respete el derecho de otros a opinar distinto.",
)

lesson(
    OA6, 3,
    "Una hoja y un lápiz. Los casos de Sam y Mía están escritos en los ejercicios.",
    "Aprenderé a comparar opciones cuando veo discriminación o violencia y a prever consecuencias. Sirve para elegir una forma de ayudar que sea segura.",
    ["Sé distinguir discriminación y violencia.", "Sé que el buen trato mejora la convivencia."],
    [
        "Cuando ocurre una agresión hay personas que la hacen, personas que la reciben y personas que la ven. Quien la ve puede elegir. Puede sumarse (reírse o participar), quedarse mirando sin hacer nada, o ayudar. Cada opción tiene consecuencias. Sumarse aumenta el daño. Mirar sin hacer nada deja sola a la víctima. Ayudar puede detener o disminuir el daño.",
        "Ayudar no siempre significa enfrentarse. Hay formas seguras: decir «basta, eso no se hace» si te sientes seguro, acompañar a la persona afectada, no reírse, llamar a un adulto del colegio y contar lo que ocurrió. No debes pelear ni ponerte en peligro. Si la situación es muy peligrosa, la opción más segura es pedir ayuda inmediata a un adulto.",
        "Compara opciones con tres preguntas: ¿me ayuda a mí a estar seguro?, ¿ayuda a la persona afectada?, ¿ayuda a detener lo que pasa? La mejor opción es la que cumple las tres.",
    ],
    [("espectador", "persona que ve lo que ocurre sin ser quien agrede ni quien recibe"), ("agredir", "hacer daño a otro"), ("ayudar", "hacer algo para que alguien esté mejor"), ("consecuencia", "lo que pasa después de una acción"), ("acompañar", "estar con alguien para que no se sienta solo")],
    [
        W("Elegir como espectador", "Mía ve que se burlan de un compañero. Opción A: reírse. Opción B: decir «basta, eso no se hace» y acompañarlo. ¿Cuál ayuda a la persona?", ["A suma al daño.", "B detiene y acompaña.", "B muestra apoyo."], "La opción B"),
        W("Opción segura", "Dos niños se pegan fuerte en el patio. Opción A: meterse a separarlos. Opción B: llamar de inmediato a un adulto. ¿Cuál es más segura?", ["Separar puede ser peligroso.", "Un adulto puede detener la pelea.", "Pedir ayuda protege a todos."], "La opción B"),
    ],
    [
        M("Creer que mirar sin hacer nada no es ser parte.", "Se piensa que solo importa quien agrede.", "Quien mira puede ayudar o dejar sola a la víctima."),
        M("Pensar que ayudar es siempre pelear.", "Se confunde ayudar con pelear.", "Ayudar puede ser decir basta, acompañar o llamar a un adulto."),
    ],
    R=[
        ex("Reírse de una burla, ¿ayuda a detenerla o la aumenta?", "La aumenta", "La persona agresora se siente apoyada."),
        ex("Acompañar a quien recibió una burla, ¿es ayudar?", "Sí", "La persona no queda sola."),
        ex("Llamar a un adulto ante una pelea fuerte, ¿es una opción segura?", "Sí", "Un adulto puede detenerla sin que nadie se ponga en riesgo."),
    ],
    U=[
        ex("¿Por qué quedarse mirando sin hacer nada deja sola a la víctima?", "Porque nadie la apoya", "La víctima no recibe ayuda."),
        ex("¿Qué tres preguntas ayudan a comparar opciones?", "Si me protege, si ayuda a la persona y si detiene lo que pasa", "Así se elige la opción más segura."),
        ex("¿Se debe pelear para ayudar?", "No", "Hay formas seguras como decir basta o pedir ayuda."),
    ],
    A=[
        ex("Opciones ante una burla: 1) reírse, 2) mirar sin hacer nada, 3) decir basta, 4) llamar a un adulto. ¿Cuántas ayudan a detener o disminuir el daño?", "2", "Decir basta y llamar a un adulto ayudan; las otras no."),
        ex("Mía ve una pelea fuerte. ¿Qué es mejor: meterse a pelear o llamar a un adulto?", "Llamar a un adulto", "Es más seguro para todos."),
        ex("Un niño se queda solo en el recreo porque lo aislaron. ¿Qué gesto ayuda: invitarlo a jugar o ignorarlo?", "Invitarlo a jugar", "Ayuda a que no se sienta solo."),
    ],
    Z=[
        ex("¿Por qué no es buena idea responder a una agresión con otra agresión?", "Porque aumenta la violencia", "La violencia genera más violencia."),
        ex("Dos niños ven una burla. Uno dice «basta». El otro se ríe. ¿Quién ayuda más?", "El que dice basta", "Pone un límite a la agresión."),
    ],
    D=[
        arith("Seis niños ven una burla y 2 de ellos dicen basta. ¿Cuántos no dicen basta?", "6-2", "Se restan los que dijeron basta al total."),
        arith("Mía acompañó a un compañero 3 recreos por semana durante 4 semanas. ¿Cuántos recreos acompañó?", "3*4", "Son 3 recreos en cada una de las 4 semanas."),
    ],
    context=[ex("Un niño inventado ve que cuatro compañeros esconden la mochila de Samir. Dice «eso no se hace» y llama a la profesora. ¿Qué opciones combinó?", "Decir basta y avisar a un adulto", "Puso un límite y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿reírse suma al daño?", "Sí", "Apoya a quien agrede."), ex("¿Llamar a un adulto es una opción segura?", "Sí", "Protege a todos."), ex("¿Acompañar es ayudar?", "Sí", "La víctima no queda sola.")],
    task=T("Lee: «Cuatro estudiantes se burlan de la forma de hablar de Aya todos los días. Mía lo ve». Escribe tres opciones para Mía y, para cada una, una consecuencia para Aya, otra para el grupo y si es segura para Mía. Elige la mejor aplicando las tres preguntas.", "Opción 1: reírse. Aya: se siente peor; grupo: sigue; Mía: segura pero daña. Opción 2: decir basta y acompañar a Aya. Aya: acompañada; grupo: se frena; Mía: segura. Opción 3: avisar a la orientadora. Elijo 2 y 3 juntas.", ["tres opciones", "consecuencias para Aya, el grupo y Mía", "aplica las tres preguntas"], ["tabla escrita"], ["elegir reírse", "proponer pelear"], "Reconoce la comparación y pregunta qué haría si la burla sigue."),
    reinforce="Escribe tres frases para decir basta con respeto.",
    extend="Escribe qué harías si la agresión es por pantalla y no en el patio.",
)

lesson(
    OA6, 4,
    "Una hoja y un lápiz. Las situaciones de aula están escritas en los ejercicios.",
    "Aprenderé a elegir acciones solidarias y respetuosas: ayudar a quien lo necesita, respetar opiniones distintas y cuidar el ambiente de aprendizaje. Sirve para que todos puedan aprender en paz.",
    ["Sé comparar opciones ante la violencia.", "Sé usar un buen trato."],
    [
        "El ambiente de aprendizaje es el clima de la sala de clases: cómo se sienten las personas, si se escuchan, si hay silencio para trabajar. Respetarlo es una forma de solidaridad. Algunas acciones: esperar tu turno para hablar, no interrumpir, cuidar los materiales, mantener la sala ordenada, no distraer a quien estudia y usar un volumen de voz adecuado.",
        "También es solidario prestar ayuda a quien la necesita, sin burlarse. Por ejemplo, explicar una tarea con paciencia, prestar un lápiz o acompañar a un compañero que se siente mal. Y respetar el derecho de todos a expresar opiniones: escuchar sin interrumpir, decir «no pienso igual, pero te escucho» y no burlarse de ideas distintas.",
        "Una buena acción solidaria es posible, respetuosa y no humilla a nadie. Antes de ayudar, puedes preguntar: «¿Necesitas ayuda con esto?». Así cuidas la dignidad de la otra persona y decides con ella qué hacer.",
    ],
    [("ambiente de aprendizaje", "clima de la sala en que todos pueden aprender"), ("solidaridad", "ayudar a quien lo necesita"), ("opinión", "lo que una persona piensa sobre algo"), ("dignidad", "valor de toda persona que debe respetarse"), ("interrumpir", "hablar cuando otra persona está hablando")],
    [
        W("Cuidar el ambiente", "Mientras el curso trabaja en silencio, Sam hace ruido con la regla. ¿Qué acción cuida el ambiente de aprendizaje: seguir golpeando o dejar la regla?", ["El ruido distrae a otros.", "Dejar la regla ayuda a concentrarse.", "Respetar el ambiente es ser solidario."], "Dejar la regla"),
        W("Respetar una opinión", "Noa no está de acuerdo con la idea de Mía. ¿Qué frase respeta: «No pienso igual, pero te escucho» o «Esa idea es tonta»?", ["La primera reconoce la diferencia.", "La segunda humilla.", "Respetar es escuchar."], "«No pienso igual, pero te escucho»"),
    ],
    [
        M("Pensar que ayudar es hacerle la tarea al otro.", "Se confunde ayuda con reemplazar.", "Ayudar es explicar o acompañar, no hacerlo por él."),
        M("Creer que respetar el ambiente es solo estar callado.", "Se reduce a un silencio total.", "También es escuchar, cuidar materiales y mantener el orden."),
    ],
    R=[
        ex("Esperar tu turno para hablar, ¿cuida el ambiente de aprendizaje?", "Sí", "Permite que todos se escuchen."),
        ex("Prestar un lápiz a quien no tiene, ¿es solidaridad?", "Sí", "Ayuda a quien lo necesita."),
        ex("Interrumpir cuando otro habla, ¿respeta su opinión?", "No", "No lo deja expresarse."),
    ],
    U=[
        ex("¿Por qué preguntar «¿necesitas ayuda?» antes de ayudar es mejor que hacerlo sin avisar?", "Porque respeta lo que la persona quiere", "Cuida su dignidad."),
        ex("¿Por qué cuidar los materiales es solidario?", "Porque todos los usan", "Cuidarlos ayuda a todo el curso."),
        ex("¿Qué dice la frase «no pienso igual, pero te escucho»?", "Respeta la opinión del otro", "Escucha sin estar de acuerdo."),
    ],
    A=[
        ex("Acciones: 1) hablar fuerte mientras otros trabajan, 2) ordenar los lápices del curso, 3) esperar tu turno, 4) burlarte de una idea. ¿Cuántas cuidan el ambiente?", "2", "Ordenar y esperar turno ayudan; las otras no."),
        ex("Mía no entiende una resta y Noa se ofrece: «¿Quieres que te explique con un ejemplo?». ¿Es solidaridad respetuosa?", "Sí", "Ofrece ayuda y deja decidir."),
        ex("Un compañero tiene una opinión distinta. ¿Qué haces: escucharlo hasta el final o cortarlo y decir que está equivocado?", "Escucharlo hasta el final", "Respeta su derecho a opinar."),
    ],
    Z=[
        ex("¿Por qué ayudar a otros mejora el ambiente de aprendizaje?", "Porque todos se sienten apoyados", "Se aprende mejor en un clima de ayuda."),
        ex("Si ayudas a un compañero a hacer su prueba en vez de explicarle, ¿es buena ayuda?", "No", "No le permite aprender y puede ser trampa."),
    ],
    D=[
        arith("Para ordenar la sala, 18 estudiantes guardaron sus útiles y 12 limpiaron las mesas. Nadie hizo las dos cosas. ¿Cuántos estudiantes ayudaron en total?", "18+12", "Se suman los dos grupos."),
        arith("Noa ordenó 15 libros de la biblioteca de aula y Mía 12. ¿Cuántos libros más ordenó Noa?", "15-12", "Se restan los libros de Mía a los de Noa."),
    ],
    context=[ex("En el aula, un niño inventado se pone de pie para pedir silencio y dice: «¿Podemos bajar la voz para que terminemos el trabajo?». ¿Qué cuida?", "El ambiente de aprendizaje", "Pide que todos puedan concentrarse.")],
    selfcheck=[ex("En Orientación: ¿el ambiente de aprendizaje incluye escuchar a otros?", "Sí", "Es parte del respeto."), ex("¿Se puede ayudar sin humillar?", "Sí", "Preguntando antes de ayudar."), ex("¿Se respeta una opinión distinta?", "Sí", "Todos tienen derecho a opinar.")],
    task=T("Escribe cinco acciones concretas para cuidar el ambiente de aprendizaje del curso (por ejemplo: esperar turno). Después escribe una frase para ofrecer ayuda y otra para responder a una opinión distinta, ambas con respeto.", "Acciones: esperar turno, ordenar materiales, bajar la voz, escuchar sin interrumpir, prestar un lápiz. Ayuda: «¿Necesitas ayuda con esto?». Opinión distinta: «No pienso igual, pero te escucho».", ["cinco acciones concretas", "una frase de ayuda", "una frase para opinión distinta"], ["lista escrita"], ["acciones vagas como «portarse bien»", "frases que humillan"], "Reconoce las acciones y pregunta cuál sería más difícil."),
    reinforce="Escribe tres formas de ayudar a un compañero sin hacerle la tarea.",
    extend="Escribe cómo avisarías con respeto a un compañero que hace ruido mientras otros estudian.",
)

lesson(
    OA6, 5,
    "Una hoja y un lápiz. Las situaciones y frases de ayuda están escritas en los ejercicios.",
    "Aprenderé a pedir y dar ayuda ante discriminación o violencia, y a elegir a quién contar. Sirve para actuar con seguridad y rechazar toda forma de violencia.",
    ["Sé comparar opciones ante la violencia.", "Sé que contar a un adulto es cuidar."],
    [
        "Cuando ves o vives discriminación o violencia, pedir ayuda es una forma de rechazarla. Puedes pedir ayuda a un adulto del colegio, como tu profesor, el orientador o el encargado de convivencia, o a una persona de tu casa. Contar no es acusar: es proteger. Si el primer adulto no te escucha, busca a otro.",
        "Para contarlo con claridad, usa cuatro datos: qué pasó, quién estaba, cuándo ocurrió y cómo te sientes o cómo se siente la persona afectada. Por ejemplo: «Ayer en el recreo, tres compañeros se rieron de la manera de hablar de Aya y ella se fue llorando. Quiero que alguien nos ayude». Si hay mensajes o imágenes en una pantalla, guarda una captura y muéstrala a un adulto.",
        "Si eres tú quien recibe la agresión, no es tu culpa. Si eres quien la ve, tu ayuda importa. Y si fuiste tú quien agredió, puedes reconocerlo, pedir perdón y cambiar. Todos pueden aprender a tratar con respeto.",
    ],
    [("convivencia", "vivir y trabajar con otros de forma respetuosa"), ("encargado de convivencia", "adulto del colegio que ayuda a resolver problemas entre estudiantes"), ("captura", "imagen de la pantalla que sirve de evidencia"), ("pedir perdón", "reconocer que hirió y querer reparar"), ("proteger", "cuidar a alguien para que no sufra daño")],
    [
        W("Contar con claridad", "¿Qué frase cuenta mejor lo ocurrido: «Ayer en el recreo, tres compañeros se rieron de Aya y ella se fue llorando» o «Pasó algo malo»?", ["La primera dice cuándo, quiénes y qué pasó.", "La segunda es vaga.", "Un adulto necesita datos para ayudar."], "«Ayer en el recreo, tres compañeros se rieron de Aya y ella se fue llorando»"),
        W("A quién contar", "Aya cuenta lo ocurrido a un profesor y no le hace caso. ¿Qué hace?", ["Un adulto no puede quedar como única opción.", "Busca a otro adulto de confianza.", "Seguir pidiendo ayuda es cuidarse."], "Busca a otro adulto de confianza"),
    ],
    [
        M("Pensar que contar es acusar y que me ven como soplón.", "Se confunde cuidar con traicionar.", "Contar protege a quien sufre; es una forma de rechazar la violencia."),
        M("Guardar silencio si el primer adulto no me hace caso.", "Se cree que no hay otra opción.", "Busca a otro adulto hasta que te escuchen."),
    ],
    R=[
        ex("Contar una agresión a un adulto, ¿es proteger o acusar sin motivo?", "Proteger", "Busca que el daño se detenga."),
        ex("Si un adulto no te escucha, ¿pides ayuda a otro adulto o te quedas en silencio?", "Pides ayuda a otro adulto", "Hay que seguir hasta ser escuchado."),
        ex("Una captura de pantalla de un mensaje que hiere, ¿sirve de evidencia?", "Sí", "Muestra lo que ocurrió."),
    ],
    U=[
        ex("¿Qué cuatro datos ayudan a contar lo ocurrido?", "Qué pasó, quién estaba, cuándo y cómo se siente", "Dan claridad al adulto."),
        ex("¿Quién tiene la culpa cuando alguien recibe una agresión?", "Quien agrede", "La víctima no es responsable."),
        ex("Quien agredió, ¿puede pedir perdón y cambiar?", "Sí", "Todos pueden aprender a tratar con respeto."),
    ],
    A=[
        ex("Lista: 1) profesor, 2) orientador, 3) encargado de convivencia, 4) un desconocido de una red. ¿Cuántos son adultos de confianza del colegio?", "3", "Los tres primeros son adultos del colegio."),
        ex("Completa: «Ayer en el recreo, ____ compañeros se burlaron de ____». ¿Qué dos datos faltan?", "Cuántos compañeros y de quién", "Esos datos hacen clara la denuncia."),
        ex("Mía recibe un mensaje que humilla a un compañero. ¿Qué hace: reenviarlo o guardar una captura y mostrarla a un adulto?", "Guardar una captura y mostrarla a un adulto", "Sirve de evidencia y ayuda a detener el daño."),
    ],
    Z=[
        ex("¿Por qué no es útil esperar a que «se pase solo»?", "Porque la agresión puede continuar", "Sin ayuda no se detiene."),
        ex("Un niño dice «yo no hice nada, solo miré». ¿Qué podría haber hecho?", "Decir basta o avisar a un adulto", "Mirar sin actuar deja sola a la víctima."),
    ],
    D=[
        arith("Aya cuenta lo que pasó a 1 profesor, 1 orientador y 2 compañeros de confianza. ¿A cuántas personas se lo contó?", "1+1+2", "Se suman todas las personas."),
        arith("En un curso de 32 estudiantes, 5 han contado una situación de burla a un adulto. ¿Cuántos no la han contado?", "32-5", "Se restan los que lo contaron al total."),
    ],
    context=[ex("Luz ve en una conversación del curso mensajes que se burlan de Nico. Guarda una captura y se la muestra al profesor jefe. ¿Qué buena práctica siguió?", "Guardar evidencia y avisar a un adulto", "Documentó lo ocurrido y pidió ayuda.")],
    selfcheck=[ex("En Orientación: ¿contar a un adulto cuida a otros?", "Sí", "Busca detener el daño."), ex("¿La víctima tiene la culpa?", "No", "La responsabilidad es de quien agrede."), ex("¿Se puede pedir ayuda a más de un adulto?", "Sí", "Hasta que te escuchen.")],
    task=T("Lee el caso: «En el chat del curso, tres compañeros publican mensajes burlándose de la forma de hablar de Aya». Escribe una frase de cuatro datos (qué pasó, quién, cuándo, cómo se siente) para contárselo a un adulto del colegio, y una lista de a quiénes podrías acudir en orden.", "Ayer, en el chat del curso, tres compañeros se burlaron de la forma de hablar de Aya y ella se siente mal. Primero la profesora jefe; si no, el orientador; luego el encargado de convivencia.", ["los cuatro datos", "lista ordenada de adultos", "no usa nombres reales de personas conocidas"], ["texto escrito o dicho"], ["frase vaga", "omitir pedir a otro adulto"], "Reconoce los datos y pregunta si guardó una captura."),
    reinforce="Escribe una frase para pedir ayuda por una situación de burla.",
    extend="Escribe cómo pedirías perdón si hubieras herido a alguien sin querer.",
)
