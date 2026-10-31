"""Cuaderno del estudiante, 2.º básico Tecnología: OA 03 (elaboración segura) y OA 04 (prueba, explicación y mejora)."""
from __future__ import annotations

from student_lessons import ex, register

OA3, OA4 = "TE02 OA 03", "TE02 OA 04"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


def reg(oa, n, *, materials, use, prior, explain, vocab, worked, mistakes, R, C, A, Z, D, ctx, sc, open_task, reinforce, extend):
    register(
        oa, n, materials=materials, use=use, prior=prior, explain=explain, vocab=vocab,
        worked=[{"title": t, "problem": p, "steps": s, "answer": a} for t, p, s, a in worked],
        mistakes=[{"wrong": w, "why": y, "fix": f} for w, y, f in mistakes],
        tiers={"recovery": [ex(*i) for i in R], "understand": [ex(*i) for i in C], "apply": [ex(*i) for i in A], "reason": [ex(*i) for i in Z], "challenge": [ex(*i) for i in D]},
        context=[ex(*ctx)], selfcheck=[ex(*i) for i in sc], open_task=task(*open_task), reinforce=reinforce, extend=extend,
    )




# ------------------------------------------------------------------ OA 03
reg(
    OA3, 1,
    materials="Retazos de papel, cartón fino, una regla, tijeras escolares de punta redonda, pegamento en barra y un adulto cerca. Si no tienes algo, usa lo que describe este cuaderno.",
    use="Aprenderé a probar cada técnica (medir, cortar, plegar, unir, pegar y pintar) en un retazo antes de usarla en mi objeto. Sirve para equivocarme sin estropear el trabajo final.",
    prior=["Sé hacer un plan de trabajo.", "Sé usar la regla en centímetros."],
    explain=[
        "Una técnica es una forma de hacer algo con las manos. Las técnicas de este curso son medir, cortar, plegar, unir, pegar y pintar. Antes de usarlas en el objeto, conviene practicarlas en un retazo, que es un pedazo sobrante.",
        "Medir es leer cuánto mide algo con la regla, empezando en el cero. Cortar es separar con tijeras, siempre lejos del cuerpo y con el adulto cerca. Plegar es doblar marcando bien el doblez. Unir es juntar partes con cinta, un cordón o una pinza. Pegar es fijar con pegamento en barra. Pintar es cubrir con color y dejar secar.",
        "Probar en un retazo muestra si la técnica sale bien. Si el corte sale chueco o el pegamento no agarra, lo notas sin perder tu material. Usa solo tijeras escolares de punta redonda y pasa los objetos al adulto con el mango por delante.",
    ],
    vocab=[("técnica", "forma de hacer algo con las manos"), ("retazo", "pedazo sobrante de material"), ("plegar", "doblar marcando el doblez"), ("unir", "juntar dos partes"), ("secar", "esperar a que no quede húmedo")],
    worked=[
        ("Medir con la regla", "Quieres una tira de 12 cm. La regla empieza en el cero. ¿Dónde marcas?", ["Pongo el cero al borde del papel.", "Busco el número 12.", "Hago una marca en el 12."], "Una marca en el número 12, contando desde el cero"),
        ("Probar un pegado", "Pegaste dos retazos con pegamento en barra y se despegaron al jalar. ¿Qué haces?", ["Anoto que no agarró.", "Pruebo con una capa más pareja y presiono un minuto.", "Espero a que seque y vuelvo a jalar."], "Probar otra vez con más presión y tiempo de secado"),
    ],
    mistakes=[
        ("Cortar mirando hacia otro lado o con las tijeras cerca del cuerpo.", "Puedes cortarte.", "Corta lejos del cuerpo, mirando el corte y con un adulto cerca."),
        ("Medir desde el borde de la regla en vez del cero.", "La medida sale distinta.", "Alinea el cero con el borde del material."),
    ],
    R=[
        ("«Doblar marcando bien» es plegar. ¿Es una técnica o un material?", "Una técnica", "Es una forma de hacer."),
        ("¿Dónde empieza una regla a medir: en el cero o en el 10?", "En el cero", "Se mide desde el cero."),
        ("Las tijeras escolares tienen la punta redonda. ¿Eso las hace más seguras o menos seguras?", "Más seguras", "La punta redonda pincha menos."),
    ],
    C=[
        ("¿Para qué se practica en un retazo antes del objeto?", "Para equivocarse sin perder el material final", "El retazo es para probar."),
        ("Nombra tres técnicas de las seis de esta clase.", "Por ejemplo: medir, cortar, pegar", "Son medir, cortar, plegar, unir, pegar y pintar."),
        ("Pasas unas tijeras a un compañero. ¿Con el mango o con la punta por delante?", "Con el mango por delante", "Así nadie se pincha."),
    ],
    A=[
        ("Un retazo mide 20 cm. Cortas una tira de 12 cm. ¿Cuántos centímetros sobran?", "8 cm", "20 menos 12 es 8."),
        ("Pintaste un retazo y lo tocaste a los 10 segundos: manchó tu dedo. ¿Qué te falta hacer: pintar otra vez o esperar a que seque?", "Esperar a que seque", "La pintura húmeda mancha."),
        ("Quieres plegar un papel por la mitad en un largo de 18 cm. ¿Dónde marcas el doblez: en los 9 cm o en los 18 cm?", "En los 9 cm", "La mitad de 18 es 9."),
    ],
    Z=[
        ("Dani dice: «Corto directo en mi objeto, no necesito practicar». ¿Qué riesgo corre? Responde en una frase.", "Equivocarse y perder el material", "Un error en el objeto no se arregla."),
        ("Al probar en el retazo, el corte salió chueco. ¿Cambias la técnica o sigues igual? Explica.", "Cambio la técnica, por ejemplo marcando antes con lápiz", "Se mejora lo que falló antes de usar el material final."),
    ],
    D=[
        ("Probaste juntar dos retazos con cinta y con pegamento en barra. La cinta aguantó el jalón y el pegamento se soltó. ¿Qué técnica usas y por qué?", "La cinta, porque aguantó el jalón", "Es la que funcionó en la prueba."),
        ("Ordena cuatro técnicas para una tira pintada y doblada: medir, pintar, plegar, cortar. Medir va primero, cortas antes de pintar y plegas al final.", "Medir, cortar, pintar, plegar (después de que seque)", "Se mide, se corta, se pinta, se espera que seque y al final se pliega."),
    ],
    ctx=("Tati debe hacer un marcador de 15 cm de largo. Antes de cortar el cartón, practica en un retazo de 20 cm. ¿Qué técnica practica primero y cuánto debe sobrar del retazo si corta 15 cm?", "Primero medir; sobran 5 cm", "20 menos 15 es 5."),
    sc=[
        ("¿Una técnica es una forma de hacer algo?", "Sí", "Es una forma de hacer con las manos."),
        ("¿El retazo sirve para practicar?", "Sí", "Es material sobrante."),
        ("¿Se corta cerca o lejos del cuerpo?", "Lejos", "Es más seguro."),
    ],
    open_task=(
        "Con un retazo de papel de 20 cm, haz una prueba de cada técnica: mide 10 cm, corta la tira, pliega por la mitad, une con cinta, pega con pegamento en barra y pinta un trozo con lápiz de color. Anota cuál salió bien, cuál no y qué cambiarías.",
        "Medí 10 cm y corté. Plegué por los 5 cm. Uní con cinta y quedó firme. Pegué con pegamento y se soltó, lo repetí. Pinté con lápiz, quedó bien.",
        ["prueba al menos 5 técnicas", "usa las tijeras de forma segura", "anota qué salió bien y qué no", "propone un cambio"],
        ["retazo probado", "nota con resultados"],
        ["usar el material final sin practicar", "cortar sin cuidado"],
        "Pregunta: «¿qué técnica fue la más difícil y qué harías distinto?». Verifica que las tijeras se usen lejos del cuerpo.",
    ),
    reinforce="Practica doblar un papel por la mitad cinco veces y mira cuál doblez quedó más recto.",
    extend="Prueba dos formas de unir dos retazos y anota cuál aguanta más un jalón suave.",
)

reg(
    OA3, 2,
    materials="Muestras de papel, cartón, lana o hilo, plástico limpio y envases limpios. Sirven los descritos en este cuaderno; evita vidrio y latas.",
    use="Aprenderé a escoger el material según lo que necesita el objeto: papeles, fibras, plásticos o desechos limpios. Sirve para que el objeto funcione y sea seguro.",
    prior=["Sé separar materiales y herramientas.", "Sé que cada material se comporta distinto."],
    explain=[
        "Cada material tiene rasgos. El papel es liviano y se rompe con facilidad. El cartón es más firme. Las fibras, como lana o hilo, son flexibles y sirven para atar o colgar. Los plásticos limpios, como un envase de yogur, aguantan el agua.",
        "Los desechos son cosas que ya no se usan pero sirven de nuevo: cajas, tapas, envases limpios. Reutilizarlos cuida el ambiente. Pero deben estar limpios y sin bordes que corten. Nunca uses vidrio, latas, ni envases que tuvieron productos de limpieza.",
        "Para escoger, pregunta qué necesita el objeto. Si debe resistir agua, un plástico limpio sirve más que papel. Si debe colgar, la fibra sirve. Si debe sostener peso liviano, el cartón sirve. Elige el material que cumple el criterio.",
    ],
    vocab=[("papel", "hoja fina, liviana y fácil de doblar"), ("fibra", "hilo, lana o cordón flexible"), ("plástico", "material liviano que no deja pasar el agua"), ("desecho", "cosa usada que se puede reutilizar si está limpia"), ("resistente", "que aguanta sin romperse")],
    worked=[
        ("Escoger por una necesidad", "Un portalápices debe sostener 5 lápices sin doblarse. ¿Sirve mejor una hoja de papel o un tubo de cartón?", ["Los lápices tienen peso.", "El papel se dobla.", "El cartón es más firme."], "El tubo de cartón"),
        ("Revisar un desecho", "Tienes un envase de plástico limpio con el borde sano y una lata con borde cortante. ¿Cuál puedes usar?", ["El envase está limpio y no corta.", "La lata puede cortarte.", "Elijo el envase."], "El envase de plástico limpio"),
    ],
    mistakes=[
        ("Usar una lata o vidrio porque está a mano.", "Tienen bordes que cortan.", "Usa solo desechos limpios y sin bordes filosos, como cartón o envases plásticos."),
        ("Elegir el material por el color.", "El color no dice si cumple.", "Elige por lo que necesita el objeto."),
    ],
    R=[
        ("La lana es una fibra. ¿Es flexible o rígida?", "Flexible", "Las fibras se doblan."),
        ("Un envase de yogur limpio, ¿es un papel o un plástico?", "Un plástico", "Es de plástico."),
        ("¿Se puede usar vidrio como desecho en la sala? Responde sí o no.", "No", "El vidrio corta."),
    ],
    C=[
        ("¿Qué material sirve para atar o colgar: una fibra o un cartón grueso?", "Una fibra", "La fibra es flexible y cuelga."),
        ("Nombra los cuatro tipos de material de esta clase.", "Papeles, fibras, plásticos y desechos", "Son los tipos que nombra el contenido."),
        ("¿Qué dos condiciones debe cumplir un desecho para usarlo?", "Estar limpio y no tener bordes que corten", "Es lo que lo hace seguro."),
    ],
    A=[
        ("Un cartel debe resistir lluvia. ¿Qué material sirve mejor: papel o plástico limpio?", "Plástico limpio", "No deja pasar el agua."),
        ("Quieres colgar un adorno del techo. ¿Qué eliges para colgarlo: lana o cartón?", "Lana", "La lana es una fibra flexible; el cartón no ata."),
        ("Tienes 3 tapas de plástico limpias, 2 trozos de cartón y 1 lata. ¿Cuántos desechos puedes usar?", "5", "La lata no se usa; 3 más 2 son 5."),
    ],
    Z=[
        ("Un niño dice: «Uso la lata, es más resistente». ¿Qué le respondes? Responde en una frase.", "Que no, porque puede cortar y debe elegir otro desecho", "La seguridad va primero."),
        ("Para un barquito que flota se compara papel y botella de plástico limpia. ¿Cuál probablemente se moja menos y por qué?", "La botella, porque no deja pasar el agua", "El plástico no absorbe agua."),
    ],
    D=[
        ("Un llavero necesita ser liviano, colgar y no mojarse con facilidad. Elige dos materiales de este cuaderno y di para qué sirve cada uno.", "Por ejemplo: lana para colgar y plástico limpio para que no se moje", "Cada material cumple un criterio."),
        ("Un desecho tiene tres rasgos: limpio, con borde sano, tamaño de 10 cm. Otro es sucio, con borde cortante, de 10 cm. ¿Cuál usas y por qué?", "El primero, porque está limpio y sin borde cortante", "Primero cuenta la seguridad."),
    ],
    ctx=("Luz hará un portalápices con cartón de una caja limpia y un envase de yogur limpio. Su amigo le ofrece una lata de conserva. ¿Qué materiales usa y qué le dice a su amigo?", "Usa el cartón y el envase de yogur; le dice que la lata corta y no se usa", "Elige desechos limpios y seguros."),
    sc=[
        ("¿Cuál es una fibra: hilo o cartón?", "Hilo", "El hilo es una fibra flexible."),
        ("¿El desecho debe estar limpio?", "Sí", "Por higiene y seguridad."),
        ("¿Elegimos el material por color o por lo que necesita el objeto?", "Por lo que necesita", "Debe cumplir el criterio."),
    ],
    open_task=(
        "Escoge un objeto: un portalápices, un llavero o un barquito. Escribe qué necesita (por ejemplo firme, flexible o no mojarse) y escoge un material de cada tipo: un papel, una fibra, un plástico limpio y un desecho limpio. Di para qué usarías cada uno.",
        "Llavero: necesita colgar y no romperse. Papel: para decorar. Fibra: lana para colgar. Plástico: tapa limpia como colgante. Desecho: cartón firme para la base.",
        ["dice lo que necesita el objeto", "escoge un material de cada tipo", "explica la función de cada uno", "usa solo desechos limpios y sin bordes que corten"],
        ["lista de materiales con su uso"],
        ["elegir por color", "usar vidrio o latas"],
        "Pregunta: «¿por qué ese material y no otro?». Si usa un desecho dudoso, explica por qué no es seguro.",
    ),
    reinforce="Toca un papel, una lana y un envase limpio y di cuál es más firme.",
    extend="Elige un desecho de tu casa que sea seguro y piensa un objeto nuevo con él.",
)

reg(
    OA3, 3,
    materials="Tu plan de trabajo, papel o cartón, regla, tijeras escolares, pegamento en barra y un adulto cerca.",
    use="Aprenderé a construir paso a paso, comprobando cada paso antes de seguir. Sirve para que el objeto salga bien y sin accidentes.",
    prior=["Sé practicar técnicas en un retazo.", "Sé elegir materiales."],
    explain=[
        "Construir con control significa ir paso a paso. Antes de empezar, despeja la mesa y deja las herramientas a mano. Sigue tu plan en orden y marca cada paso que terminas.",
        "Hay una regla útil: mide dos veces y corta una. Si mides mal, el corte no se puede deshacer. También usa poco pegamento y espera a que seque, para que las partes queden firmes. Si algo sale mal, para y revisa con el adulto.",
        "Comprueba con la regla después de cada paso. Si una pieza mide 11 cm y debía medir 12 cm, corrige antes de pegar. Y al terminar de usar una herramienta, guárdala. Así el trabajo es limpio y seguro.",
    ],
    vocab=[("control", "ir con cuidado, paso a paso"), ("comprobar", "revisar que quedó como se quería"), ("despejar", "dejar libre un lugar"), ("seguir el plan", "hacer los pasos en el orden escrito")],
    worked=[
        ("Medir dos veces", "Debes cortar una tira de 12 cm. Mediste 12 cm la primera vez. ¿Qué haces antes de cortar?", ["Vuelvo a medir.", "Comparo las dos medidas.", "Si coinciden, recién corto."], "Medir otra vez y cortar solo si coinciden"),
        ("Comprobar una pieza", "Tu pieza debía medir 12 cm y mide 11 cm. ¿La pegas o la corriges?", ["Mido otra vez.", "Veo que es 1 cm más corta.", "Cambio la pieza antes de pegar."], "La corrijo antes de pegar"),
    ],
    mistakes=[
        ("Cortar sin medir dos veces.", "Un error de medida no se puede deshacer.", "Mide dos veces y corta una."),
        ("Dejar las herramientas sobre la mesa cuando no se usan.", "Alguien puede cortarse o tirarlas.", "Guarda cada herramienta al terminar de usarla."),
    ],
    R=[
        ("La regla útil dice: mide dos veces y... ¿qué más?", "Corta una vez", "Así se evitan errores."),
        ("¿Se guarda la tijera después de usarla?", "Sí", "Guardarla evita accidentes."),
        ("¿Usas mucho pegamento o poco?", "Poco", "El exceso demora el secado."),
    ],
    C=[
        ("¿Por qué se mide dos veces antes de cortar?", "Porque un corte mal medido no se puede deshacer", "Evita perder material."),
        ("¿Qué se hace si una pieza sale mal?", "Se para y se revisa con el adulto", "Corregir a tiempo evita más errores."),
        ("¿Para qué sirve despejar la mesa antes de empezar?", "Para trabajar con más seguridad", "Hay espacio y nada estorba."),
    ],
    A=[
        ("La tira debe medir 15 cm y la tuya mide 13 cm. ¿Cuántos centímetros faltan?", "2 cm", "15 menos 13 es 2."),
        ("Pegas dos partes y tocas a los 5 segundos: se mueven. ¿Esperas o las empujas?", "Espero", "El pegamento necesita secar."),
        ("Tienes tres pasos: cortar, medir, pegar. ¿Cuál haces después de medir?", "Cortar", "El orden es medir, cortar, pegar."),
    ],
    Z=[
        ("Un niño corta una pieza de 10 cm cuando debía ser de 12 cm. ¿Qué no hizo? Explica.", "No comprobó la medida antes de cortar", "Habría visto la diferencia."),
        ("Un compañero deja las tijeras abiertas en el borde de la mesa. ¿Qué le recomiendas?", "Guardarlas cerradas lejos del borde", "Evita caídas y cortes."),
    ],
    D=[
        ("Tu caja necesita 4 lados iguales de 8 cm. ¿Cuántos centímetros de cartón en total necesitas si pegas los lados en fila?", "32 cm", "4 por 8 es 32."),
        ("Una pieza medida dos veces da 12 cm y 13 cm. ¿Qué haces?", "Mido una tercera vez con cuidado y alineo el cero", "Hay un error de lectura."),
    ],
    ctx=("Bruno corta cartón para una caja. La pieza debía medir 14 cm. La mide y da 14 cm, la mide de nuevo y da 15 cm. ¿Qué hace y qué dice la regla de la clase?", "Vuelve a medir con el cero alineado; mide dos veces, corta una", "Hay que resolver la diferencia antes de cortar."),
    sc=[
        ("¿Medimos dos veces antes de cortar?", "Sí", "Así se evitan errores."),
        ("¿Se guarda la herramienta al terminar?", "Sí", "Es más seguro."),
        ("¿Seguimos el plan en orden?", "Sí", "El orden evita errores."),
    ],
    open_task=(
        "Construye un marcador de página. Sigue este plan: 1 medir 15 cm de cartón fino, 2 medir otra vez, 3 cortar, 4 plegar la punta 2 cm, 5 pegar un adorno pequeño con pegamento en barra. Marca cada paso hecho y anota una medida que comprobaste.",
        "Medí dos veces 15 cm y corté. Plegué 2 cm. Pegué un adorno y dejé secar. Comprobé: 15 cm de largo.",
        ["sigue el plan en orden", "mide dos veces", "usa poco pegamento", "guarda las herramientas", "anota una medida comprobada"],
        ["marcador terminado", "plan con marcas"],
        ["cortar sin comprobar", "dejar tijeras abiertas"],
        "Pregunta: «¿qué comprobaste antes de cortar?». Si no midió dos veces, repite el paso con otro retazo.",
    ),
    reinforce="Mide dos veces un libro de tu casa y anota si las medidas coinciden.",
    extend="Prepara un orden de trabajo para una caja y marca cuándo comprobarías las medidas.",
)

reg(
    OA3, 4,
    materials="El objeto casi terminado, el plan, lápiz y hoja para dibujar. No necesitas cámara.",
    use="Aprenderé a terminar el objeto, comprobar si cumple y dejar un registro de lo que hice. Sirve para mostrar y mejorar mi trabajo.",
    prior=["Sé construir paso a paso.", "Sé que un criterio se comprueba."],
    explain=[
        "Terminar no es solo pegar la última parte. Es revisar que el objeto cumple los criterios. Si el criterio dice «mide 15 cm», lo mides. Si dice «sostiene 3 lápices», lo pruebas con lápices de verdad.",
        "Después se documenta. Documentar es dejar un registro de lo que hiciste: un dibujo del objeto terminado con sus medidas y una lista de materiales y pasos. Sirve para repetir el trabajo y para explicarlo a otra persona.",
        "Por último, se deja todo ordenado. Los recortes limpios se guardan para reutilizar. Los restos sucios van al basurero. Las herramientas se guardan. Y te lavas las manos después de pegar o pintar.",
    ],
    vocab=[("documentar", "dejar un registro de lo que se hizo"), ("registro", "dibujo o texto que muestra lo que pasó"), ("terminar", "completar y revisar el objeto"), ("reutilizar", "volver a usar un material")],
    worked=[
        ("Comprobar un criterio", "El criterio dice: «sostiene 3 lápices». Pones 3 lápices y el objeto se mantiene. ¿Cumple?", ["Pruebo con 3 lápices de verdad.", "El objeto no se cae.", "Entonces cumple el criterio."], "Sí, cumple"),
        ("Hacer el registro", "Tu objeto es un portalápices de 10 cm de alto. ¿Qué incluyes en el registro?", ["Un dibujo del objeto.", "Su medida: 10 cm de alto.", "Materiales y pasos."], "Dibujo, medidas, materiales y pasos"),
    ],
    mistakes=[
        ("Decir «terminé» sin probar los criterios.", "No sabes si funciona.", "Prueba cada criterio con una acción concreta."),
        ("Botar todos los recortes sin mirar.", "Algunos sirven de nuevo.", "Guarda los recortes limpios para reutilizar."),
    ],
    R=[
        ("Para probar «mide 15 cm» usas una regla. ¿Se mide o se adivina?", "Se mide", "Se comprueba con la regla."),
        ("Documentar es dejar un registro. ¿Sirve un dibujo con medidas?", "Sí", "Es un registro claro."),
        ("Después de pegar, ¿te lavas las manos?", "Sí", "Se hace por higiene."),
    ],
    C=[
        ("¿Qué incluye un buen registro: dibujo, medidas y pasos, o solo el nombre?", "Dibujo, medidas y pasos", "Permite repetir el trabajo."),
        ("¿Para qué sirve documentar un objeto?", "Para repetirlo y explicarlo a otros", "Deja claro qué se hizo."),
        ("¿Qué se hace con los recortes limpios al final?", "Se guardan para reutilizar", "Así se ahorra material."),
    ],
    A=[
        ("Criterio: mide 12 cm. Tu objeto mide 12 cm. ¿Cumple?", "Sí", "La medida coincide."),
        ("Criterio: sostiene 4 fichas. Probaste con 4 y se cayó una. ¿Cumple?", "No", "Debe sostener las 4."),
        ("Anotas la altura de tu objeto: 9. ¿Qué falta para que el registro esté bien?", "La unidad, cm", "Sin unidad la medida está incompleta."),
    ],
    Z=[
        ("Un compañero no hizo ningún registro. Dentro de una semana quiere repetir el objeto. ¿Qué problema tendrá?", "No recordará medidas ni pasos", "Sin registro se olvida."),
        ("Tu objeto no cumple un criterio. ¿Qué haces: lo escondes o lo anotas y piensas una mejora?", "Lo anoto y pienso una mejora", "Un fallo registrado ayuda a mejorar."),
    ],
    D=[
        ("Haz un registro breve de un portalápices de 10 cm hecho con cartón, cinta y tijeras. Incluye medida, materiales y herramientas.", "Portalápices de 10 cm; materiales: cartón y cinta; herramientas: tijeras", "Registro completo y breve."),
        ("Terminaste con 3 recortes limpios y 2 sucios. ¿Cuántos puedes guardar para reutilizar?", "3", "Solo los limpios."),
    ],
    ctx=("Mati terminó una caja para 5 fichas. El criterio decía que cabían 5 fichas y medía 6 cm de ancho. Probó y caben solo 4. ¿Qué anota y qué hace?", "Anota que no cumple: caben 4 de 5 fichas, y propone agrandar el ancho", "Es honesto con la prueba y piensa una mejora."),
    sc=[
        ("¿Se prueba cada criterio al terminar?", "Sí", "Así sabes si funciona."),
        ("¿Documentar es dejar un registro?", "Sí", "Es la definición."),
        ("¿Los recortes limpios se pueden reutilizar?", "Sí", "Así se ahorra material."),
    ],
    open_task=(
        "Con tu objeto terminado, escoge dos criterios y pruébalos (por ejemplo: mide 15 cm; sostiene 3 lápices). Dibuja el objeto con sus medidas y escribe materiales, herramientas y si cumplió cada criterio. Deja la mesa ordenada.",
        "Marcador: criterios: mide 15 cm (cumple), no rompe las hojas (cumple). Dibujo con 15 cm. Materiales: cartón y cinta. Herramientas: tijeras y regla.",
        ["prueba dos criterios", "dibuja con medidas", "lista materiales y herramientas", "ordena la mesa y se lava las manos"],
        ["dibujo y registro", "mesa ordenada"],
        ["no probar los criterios", "no anotar los fallos"],
        "Pregunta: «¿cómo probaste este criterio?». Si no lo probó, pídele que lo haga ahora.",
    ),
    reinforce="Haz un dibujo con medidas de un objeto de tu casa como registro.",
    extend="Escribe cinco pasos para que otra persona repita tu objeto.",
)

# ------------------------------------------------------------------ OA 04
reg(
    OA4, 1,
    materials="Tu objeto o un puente de papel plegado, fichas o tapas livianas como pesos y una hoja para anotar.",
    use="Aprenderé a hacer una prueba que responde una pregunta clara. Sirve para saber con datos si mi objeto funciona.",
    prior=["Sé que un criterio se puede comprobar.", "Sé contar y medir en centímetros."],
    explain=[
        "Probar es mirar si el objeto cumple lo que se quiere. Una buena prueba empieza con una pregunta clara. Por ejemplo: ¿mi soporte sostiene 5 fichas sin caerse?",
        "Para que la prueba valga, se hace igual cada vez. Usas las mismas fichas, la misma mesa y las cuentas bien. Si cambias algo entre una prueba y otra, no sabes qué pasó.",
        "Al final anota el resultado con un número o una palabra clara: sostuvo 5 fichas, sostuvo 3, se cayó. Un resultado claro permite comparar y mejorar. No digas solo «más o menos»: di cuántas fichas sostuvo.",
    ],
    vocab=[("prueba", "acción para ver si el objeto funciona"), ("pregunta de prueba", "lo que quieres saber con la prueba"), ("resultado", "lo que pasó en la prueba"), ("igual cada vez", "hacer la prueba del mismo modo")],
    worked=[
        ("Formular la pregunta", "Quieres probar un soporte de cartón para fichas. Escribe una pregunta de prueba.", ["Pienso en lo que debe lograr.", "Debe sostener fichas.", "Pregunto con un número."], "¿Mi soporte sostiene 5 fichas sin caerse?"),
        ("Anotar el resultado", "Pusiste fichas una por una y el soporte aguantó 4; con la quinta se cayó. ¿Cuál es el resultado?", ["Conté cuántas aguantó.", "Aguantó 4.", "Con 5 se cayó."], "Sostiene 4 fichas, con 5 se cae"),
    ],
    mistakes=[
        ("Probar de modos distintos cada vez.", "No se puede comparar.", "Haz la prueba igual cada vez."),
        ("Anotar «salió más o menos».", "No es un resultado claro.", "Anota un número: «sostuvo 4 fichas»."),
    ],
    R=[
        ("Una prueba responde una pregunta. ¿La pregunta se escribe antes o después?", "Antes", "Guía lo que haces."),
        ("«Sostuvo 4 fichas», ¿es un resultado claro? Responde sí o no.", "Sí", "Tiene un número."),
        ("Si cambias las fichas entre pruebas, ¿la prueba vale igual?", "No", "Debe hacerse igual cada vez."),
    ],
    C=[
        ("¿Por qué una prueba se hace igual cada vez?", "Para poder comparar los resultados", "Si cambia todo, no se sabe qué pasó."),
        ("¿Cuál pregunta sirve mejor: «¿sostiene 5 fichas?» o «¿está lindo?»", "¿Sostiene 5 fichas?", "Se puede comprobar con un conteo."),
        ("¿Qué debe llevar un resultado claro?", "Un número o una palabra precisa", "Así se puede comparar."),
    ],
    A=[
        ("Pones fichas de a una sobre un soporte: aguantó 6, la séptima lo botó. ¿Cuántas fichas sostuvo?", "6", "La séptima ya lo botó."),
        ("Quieres saber si una caja de 10 cm cabe en una mochila de 12 cm de ancho. ¿Cuál es la pregunta de prueba?", "¿La caja de 10 cm cabe en la mochila de 12 cm de ancho?", "Dice qué comparas."),
        ("Probaste el soporte con 5 fichas y se mantuvo. El criterio decía 5 fichas. ¿Cumple?", "Sí", "5 es igual a 5."),
    ],
    Z=[
        ("Ana probó con fichas pesadas y Beto con fichas livianas, y compararon. ¿Es justa la comparación? Explica.", "No, porque usaron fichas distintas", "Debe probarse igual cada vez."),
        ("Un niño dice: «Probé y funcionó» sin dar números. ¿Qué le pides?", "Que diga cuántas fichas sostuvo", "Un resultado claro lleva un número."),
    ],
    D=[
        ("Escribe una pregunta de prueba, el procedimiento (qué haces igual cada vez) y el resultado esperado para un soporte de fichas.", "Pregunta: ¿sostiene 5 fichas?; procedimiento: poner fichas una a una; resultado esperado: 5", "Tiene pregunta, procedimiento y resultado."),
        ("Un soporte aguantó 4, 5 y 5 fichas en tres pruebas. ¿Cuál fue el máximo?", "5 fichas", "Es el mayor número."),
    ],
    ctx=("Lola hizo un puente de cartón de 20 cm de largo. Quiere saber si aguanta un cuaderno liviano. Escribe la pregunta de prueba y qué anotaría si aguanta.", "¿Mi puente aguanta un cuaderno liviano? Anotaría: aguantó el cuaderno", "Pregunta clara y resultado claro."),
    sc=[
        ("¿La prueba responde una pregunta?", "Sí", "Esa es su función."),
        ("¿Se anota un resultado claro con número?", "Sí", "El número permite comparar."),
        ("¿Se hace la prueba igual cada vez?", "Sí", "Así los resultados valen."),
    ],
    open_task=(
        "Escoge un objeto: un soporte de cartón para fichas o un puente de papel plegado. Escribe una pregunta de prueba, cómo la harás igual cada vez y prueba tres veces con fichas o tapas livianas. Anota el resultado de cada vez con un número.",
        "Pregunta: ¿mi soporte sostiene 5 fichas? Lo hice poniendo fichas una a una. Resultados: 5, 5, 4.",
        ["escribe una pregunta de prueba", "hace la prueba igual cada vez", "anota tres resultados con número"],
        ["pregunta escrita", "tabla con tres resultados"],
        ["cambiar las condiciones", "resultado sin número"],
        "Pregunta: «¿qué pregunta respondió tu prueba?». Si el resultado es vago, pide un número.",
    ),
    reinforce="Prueba qué tan lejos rueda una pelota pequeña y mide la distancia dos veces en tu casa.",
    extend="Escribe dos preguntas de prueba para el mismo objeto.",
)

reg(
    OA4, 2,
    materials="Una hoja para una tabla de cuatro filas, lápiz, y los datos de este cuaderno.",
    use="Aprenderé a registrar todos los resultados de una prueba, también los que salen mal. Sirve para aprender de los fallos y no esconderlos.",
    prior=["Sé hacer una prueba con una pregunta.", "Sé que un resultado lleva un número."],
    explain=[
        "Un registro es una tabla donde anotas cada intento. Lleva el número de intento, lo que probaste y el resultado. También anota si falló. Una falla no es una vergüenza: es información.",
        "Si escondes una falla, no sabrás qué mejorar. Si la anotas, puedes buscar la causa. Por ejemplo: el soporte se cayó a la tercera ficha porque la base era angosta. Eso se escribe tal cual.",
        "Anota también lo que cambió entre intentos y qué pasó. Usa palabras claras y números. Un buen registro lo puede entender otra persona. Si copias solo los intentos buenos, el registro miente.",
    ],
    vocab=[("intento", "cada vez que haces la prueba"), ("falla", "algo que no funcionó como se esperaba"), ("causa", "la razón de lo que pasó"), ("tabla", "cuadro con filas y columnas para ordenar datos")],
    worked=[
        ("Completar una tabla", "Intento 1: 5 fichas, se mantuvo. Intento 2: 6 fichas, se cayó. Escribe el resultado del intento 2 en la tabla.", ["Leo el intento 2.", "Fue con 6 fichas.", "El resultado es que se cayó."], "Intento 2: 6 fichas, se cayó"),
        ("Buscar la causa", "El soporte se cayó con la quinta ficha. La base mide 4 cm y las fichas son de 6 cm. ¿Cuál puede ser la causa?", ["Comparo la base con las fichas.", "La base es más angosta que las fichas.", "Se vuelca por ser angosta."], "La base es muy angosta"),
    ],
    mistakes=[
        ("No anotar los intentos que fallaron.", "Se pierde lo que más enseña.", "Anota todo, incluso lo que sale mal."),
        ("Anotar «se cayó» sin decir cuántas fichas.", "Falta el dato.", "Anota el número de fichas o la medida."),
    ],
    R=[
        ("Una falla, ¿se esconde o se anota?", "Se anota", "La falla es información útil."),
        ("Un intento es cada vez que haces la prueba. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ("En la tabla, ¿puedes escribir un número y una palabra?", "Sí", "Número y palabra aclaran."),
    ],
    C=[
        ("¿Por qué conviene anotar también lo que falla?", "Porque ayuda a encontrar qué mejorar", "Una falla enseña."),
        ("¿Qué tres datos lleva cada fila de tu tabla?", "Número de intento, qué probaste y resultado", "Son lo mínimo."),
        ("¿Qué pasa si copias solo los intentos buenos?", "El registro no cuenta la verdad", "Oculta lo que falló."),
    ],
    A=[
        ("Intentos con fichas: 1 sostuvo 5, 2 sostuvo 5, 3 sostuvo 3. ¿En cuál hubo falla?", "Intento 3", "Sostuvo menos que los otros."),
        ("Los intentos sostuvieron 5, 5 y 3 fichas. ¿Cuántas fichas menos sostuvo el intento 3 que el intento 1?", "2", "5 menos 3 es 2."),
        ("En el intento 3 el soporte se inclinó hacia la derecha. ¿Dónde lo anotas: en la columna «resultado» o en la de «número de intento»?", "En resultado", "Es lo que pasó."),
    ],
    Z=[
        ("Dani borró su intento 2 porque falló. ¿Qué pierde? Responde en una frase.", "Pierde información para mejorar", "La falla mostraba un problema."),
        ("Dos tablas: una tiene 3 intentos con números, otra dice «anduvo bien». ¿Cuál sirve más para mejorar?", "La de números", "Tiene datos que se comparan."),
    ],
    D=[
        ("Completa la tabla con palabras: intento 1 (5 fichas, bien), intento 2 (6 fichas, cae), intento 3 (6 fichas, cae). ¿Cuál es la conclusión sobre 6 fichas?", "Con 6 fichas el soporte cae", "Cayó dos veces."),
        ("Busca una causa posible si el soporte cae siempre con 6 fichas. Responde con una frase.", "La base es angosta o el material es débil", "Dos causas posibles."),
    ],
    ctx=("Pablo probó un puente. Intento 1: aguantó 1 cuaderno. Intento 2: aguantó 2. Intento 3: se hundió con 3. Escribe la tabla en una frase y di qué dato no puede esconder.", "Intento 3 se hundió con 3 cuadernos; no puede esconder esa falla", "Registra todos los intentos, también el que falló."),
    sc=[
        ("¿Se anotan los intentos que fallaron?", "Sí", "Son información útil."),
        ("¿Una falla enseña algo?", "Sí", "Muestra qué mejorar."),
        ("¿Una tabla lleva intento y resultado?", "Sí", "Son datos básicos."),
    ],
    open_task=(
        "Usa estos resultados de un soporte de fichas: intento 1: 4 fichas, bien; intento 2: 5 fichas, bien; intento 3: 6 fichas, se cayó; intento 4: 6 fichas, se cayó. Haz una tabla con intento, fichas y resultado. Escribe la conclusión y una causa posible.",
        "Tabla con cuatro filas. Conclusión: sostiene hasta 5 fichas. Causa posible: la base es angosta.",
        ["hace la tabla con las cuatro filas", "incluye las fallas", "escribe una conclusión con número", "propone una causa"],
        ["tabla completa", "conclusión escrita"],
        ["omitir los intentos fallidos", "conclusión sin dato"],
        "Pregunta: «¿qué aprendiste de las fallas?». Si omitió fallas, pregúntale por qué.",
    ),
    reinforce="Anota tres intentos de equilibrar un lápiz sobre un dedo y cuánto duró cada uno.",
    extend="Agrega una columna con la causa posible de cada falla.",
)

reg(
    OA4, 3,
    materials="Tu objeto o dibujo y una hoja para escribir tus tres partes: qué hice, qué pasó y qué mejoraría.",
    use="Aprenderé a explicar mi trabajo a otra persona, escuchar su opinión y dialogar. Sirve para que me entiendan y para aprender de los demás.",
    prior=["Sé registrar resultados.", "Sé escuchar sin interrumpir."],
    explain=[
        "Explicar es contar a otra persona qué hiciste, qué pasó y qué piensas. Una forma ordenada es decir tres cosas: qué hice, qué pasó en la prueba y qué mejoraría. Usa los datos de tu registro.",
        "También puedes explicar el trabajo de otro compañero. Comienza por algo que funcionó y luego di una sugerencia amable. Por ejemplo: «Tu soporte sostuvo 5 fichas. Quizá una base más ancha lo mejore». Evita decir «está feo».",
        "Dialogar es hablar por turnos. Primero escuchas, luego respondes. Si no estás de acuerdo, di por qué con un dato. Trabajar en equipo es repartir tareas y respetar las ideas de los demás.",
    ],
    vocab=[("explicar", "contar con claridad qué hiciste y qué pasó"), ("sugerencia", "idea amable para mejorar"), ("dialogar", "hablar y escuchar por turnos"), ("evidencia", "dato que muestra algo")],
    worked=[
        ("Explicar con tres partes", "Tu soporte sostuvo 5 fichas. Explica con tres partes: qué hiciste, qué pasó, qué mejorarías.", ["Qué hice: un soporte de cartón.", "Qué pasó: sostuvo 5 fichas.", "Qué mejoraría: una base más ancha."], "Hice un soporte de cartón, sostuvo 5 fichas y haría la base más ancha"),
        ("Dar una sugerencia amable", "El puente de Pía sostuvo 2 cuadernos y se hundió con 3. ¿Cómo lo dices con respeto?", ["Primero algo que funcionó.", "Luego mi sugerencia.", "Sin criticar a la persona."], "Tu puente sostuvo 2 cuadernos. Tal vez un cartón más grueso aguante 3"),
    ],
    mistakes=[
        ("Decir «tu trabajo está malo».", "No ayuda y puede herir.", "Di un dato y una sugerencia amable."),
        ("Explicar sin datos: «salió bien».", "Nadie entiende cuánto.", "Usa números de tu registro."),
    ],
    R=[
        ("Explicar es contar qué hice, qué pasó y qué mejoraría. ¿Son tres partes?", "Sí", "Así se ordena."),
        ("En un diálogo, ¿hablas por turnos o todos a la vez?", "Por turnos", "Así se entiende."),
        ("Decir «eso está feo», ¿es una sugerencia amable?", "No", "Esa frase no ayuda a mejorar."),
    ],
    C=[
        ("¿Con qué empieza una buena sugerencia: con algo que funcionó o con una crítica?", "Con algo que funcionó", "Anima y es respetuoso."),
        ("¿Para qué usar datos al explicar?", "Para que se entienda con claridad", "Los datos dan evidencia."),
        ("¿Qué haces si no estás de acuerdo con una idea?", "Digo por qué con un dato", "Así dialogas con respeto."),
    ],
    A=[
        ("Tu torre aguantó 8 fichas. Completa: «Mi torre aguantó ___ fichas».", "8", "Es el dato de la prueba."),
        ("Beto hizo una repisa que sostuvo 3 libros. ¿Qué dato dirías en tu sugerencia amable?", "Tu repisa sostuvo 3 libros", "Reconoces algo que funcionó."),
        ("Dos compañeros quieren hablar a la vez. ¿Qué regla del diálogo usas?", "Hablar por turnos", "Así se escucha a todos."),
    ],
    Z=[
        ("Eli dice: «Tu soporte es malo». ¿Cómo lo dirías de manera más útil?", "Tu soporte se cayó con 6 fichas; quizá una base más ancha ayude", "Da un dato y una sugerencia."),
        ("En equipo, uno hace todo y los demás miran. ¿Es justo? Responde sí o no y di por qué.", "No, porque el trabajo se reparte", "Todos deben participar."),
    ],
    D=[
        ("Explica el trabajo de un compañero: su torre aguantó 8 fichas, pero se inclinó. Usa tres partes.", "Hizo una torre; aguantó 8 fichas pero se inclinó; podría mejorar la base", "Qué hizo, qué pasó, qué mejorar."),
        ("Dos niños tienen ideas distintas: A base ancha, B base con peso. ¿Cómo deciden? Escribe una forma.", "Prueban las dos y comparan resultados", "Se decide con evidencia."),
    ],
    ctx=("Rafa muestra su barco de papel que flota 3 minutos. A Sofía le pareció que se hunde rápido. Escribe cómo Sofía puede dar su opinión con respeto.", "Tu barco flotó 3 minutos. Quizá un papel más grueso flote más", "Dato y sugerencia amable."),
    sc=[
        ("¿Explicas con datos?", "Sí", "Los datos dan claridad."),
        ("En Tecnología: ¿Se habla por turnos?", "Sí", "Es una regla del diálogo."),
        ("¿La sugerencia es amable?", "Sí", "Debe respetar a la persona."),
    ],
    open_task=(
        "Usa este caso: una compañera hizo un soporte que sostuvo 5 fichas y se inclinó con la sexta. Escribe tres partes para explicar su trabajo (qué hizo, qué pasó, qué mejoraría) y una sugerencia amable. Luego explica el tuyo con tres partes.",
        "Ella hizo un soporte. Sostuvo 5 fichas y se inclinó con la sexta. Podría hacer la base más ancha. Sugerencia: tu soporte sostuvo 5 fichas, quizá una base más ancha ayude.",
        ["explica con tres partes", "usa números", "da una sugerencia amable", "habla de su propio trabajo"],
        ["frases escritas o dichas"],
        ["decir «está malo»", "no usar datos"],
        "Pregunta: «¿qué dato usaste?». Si dice solo «estaba bien», pídele un número.",
    ),
    reinforce="Cuéntale a un familiar cómo hiciste un trabajo en tres partes.",
    extend="Escucha la idea de otra persona y repite con tus palabras lo que dijo antes de opinar.",
)

reg(
    OA4, 4,
    materials="Tu objeto, fichas livianas y una tabla de registro con dos columnas: antes y después.",
    use="Aprenderé a mejorar mi objeto cambiando una sola cosa y probando de nuevo. Sirve para saber qué cambio sí ayuda.",
    prior=["Sé registrar resultados.", "Sé explicar qué pasó."],
    explain=[
        "Para mejorar, elige una sola cosa para cambiar, que se llama variable. Puede ser el ancho de la base, el material o la cantidad de pegamento. Si cambias dos cosas, no sabrás cuál ayudó.",
        "Prueba antes y después del cambio, del mismo modo. Compara los resultados. Si el soporte sostenía 4 fichas y ahora sostiene 6, el cambio ayudó. Si sostiene lo mismo, no ayudó y puedes probar otro cambio.",
        "Anota qué cambiaste y qué pasó. Así tu equipo o tú pueden decir cómo podría mejorar el trabajo en el futuro. Mejorar es un proceso: se prueba, se cambia una cosa y se vuelve a probar.",
    ],
    vocab=[("variable", "lo que cambias en una prueba"), ("mejorar", "hacer algo para que funcione mejor"), ("comparar", "mirar lo de antes y lo de después"), ("futuro", "lo que haremos después")],
    worked=[
        ("Elegir una variable", "Un soporte se cae con 6 fichas. Tiene base de 4 cm. ¿Qué cambias primero?", ["Elijo una sola cosa.", "La base parece angosta.", "Cambio solo el ancho de la base."], "Cambio solo el ancho de la base"),
        ("Comparar antes y después", "Antes sostenía 4 fichas. Después de ensanchar la base a 8 cm sostiene 6. ¿Ayudó el cambio?", ["Antes: 4.", "Después: 6.", "6 es más que 4."], "Sí, ayudó: sostiene 2 fichas más"),
    ],
    mistakes=[
        ("Cambiar la base, el material y el color a la vez.", "No sabes qué cambio ayudó.", "Cambia una sola cosa por vez."),
        ("Cambiar sin volver a probar.", "No hay datos.", "Prueba de nuevo igual que antes."),
    ],
    R=[
        ("Para mejorar, ¿cambias una cosa o muchas a la vez?", "Una cosa", "Así sabes cuál ayudó."),
        ("Lo que cambias se llama variable. ¿Verdadero o falso?", "Verdadero", "Es la definición."),
        ("Después del cambio, ¿pruebas de nuevo o no?", "Pruebas de nuevo", "Hay que comparar."),
    ],
    C=[
        ("En Tecnología: ¿Por qué se cambia solo una variable?", "Para saber cuál cambio ayudó", "Si cambias varias, se mezclan."),
        ("Antes sostenía 3 fichas y ahora 5. ¿Mejoró?", "Sí", "5 es más que 3."),
        ("¿Qué se anota después de mejorar?", "Qué se cambió y qué pasó", "Sirve para el futuro."),
    ],
    A=[
        ("Antes sostenía 4 fichas y después 7. ¿Cuántas fichas más sostiene?", "3", "7 menos 4 es 3."),
        ("Un puente de papel se hunde con un cuaderno. ¿Qué una sola cosa cambiarías: el grosor del papel o todo a la vez?", "El grosor del papel", "Es una sola variable."),
        ("La base de 6 cm no basta. Pruebas con 9 cm. ¿Cuántos cm más ancha es?", "3 cm", "9 menos 6 es 3."),
    ],
    Z=[
        ("Lía cambió la base y el color. El soporte mejoró. ¿Puede saber qué ayudó? Explica.", "No, porque cambió dos cosas", "No se separan los efectos."),
        ("Un cambio no mejoró nada. ¿Fue un fracaso? Responde con una frase.", "No, porque se aprendió que ese cambio no ayuda", "Descartar una idea también enseña."),
    ],
    D=[
        ("Escribe un plan de mejora: variable elegida, cómo la cambiarás y qué esperas que pase.", "Variable: ancho de base; la pasaré de 4 a 8 cm; espero que sostenga más fichas", "Dice qué cambiar, cómo y qué se espera."),
        ("Antes: 3, 4 y 4 fichas. Después del cambio: 6, 6 y 5. ¿Mejoró en las tres pruebas?", "Sí", "Los números de después son mayores en cada una."),
    ],
    ctx=("Nico hizo un barco de papel que se hunde en 1 minuto. Cambió solo el tipo de papel y ahora flota 4 minutos. ¿Qué variable cambió y cuánto mejoró?", "Cambió el tipo de papel y mejoró 3 minutos", "Un solo cambio y comparación."),
    sc=[
        ("¿Se cambia una sola variable?", "Sí", "Para saber qué ayudó."),
        ("¿Se prueba antes y después?", "Sí", "Así se pueden comparar."),
        ("¿Mejorar es un proceso?", "Sí", "Se repite probando."),
    ],
    open_task=(
        "Usa estos datos: un soporte de cartón con base de 4 cm sostiene 4 fichas. Se pregunta si una base de 8 cm sostiene más. Escribe qué variable cambiarás, qué esperas, haz la prueba con tu soporte y compara con 4 fichas. Escribe cómo mejorarías en el futuro.",
        "Variable: ancho de base. Espero que sostenga más. Con 8 cm sostuvo 6 fichas. Mejoró 2 fichas. En el futuro probaría un cartón más grueso.",
        ["elige una sola variable", "prueba antes y después", "compara con números", "propone una mejora futura"],
        ["tabla antes y después", "frase de conclusión"],
        ["cambiar varias cosas", "no volver a probar"],
        "Pregunta: «¿qué cambiaste exactamente?». Si cambió varias cosas, pídele repetir cambiando solo una.",
    ),
    reinforce="Cambia solo una cosa de un juego casero y compara el antes y el después.",
    extend="Propón dos cambios futuros para tu objeto y di cuál probarías primero.",
)
