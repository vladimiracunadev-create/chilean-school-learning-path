"""Cuaderno del estudiante, 3.º básico Tecnología: OA 03 (elaborar un objeto) y OA 04 (probar y evaluar).

Materiales del OA 03 tocados: papeles, cartones, fibras, plásticos, cerámicos (arcilla que se seca al aire, sin horno) y desechos.
Técnicas: medir, marcar, cortar, plegar, unir, pegar, pintar.
Seguridad: tijeras de punta roma; nada de cortadores, fuego, vidrio, alfileres ni objetos pequeños sueltos; los cortes difíciles los hace una persona adulta.
"""
from __future__ import annotations

from student_content_te3_a import reg
from student_lessons import arith

OA3, OA4 = "TE03 OA 03", "TE03 OA 04"

# ------------------------------------------------------------------ OA 03, clase 1
reg(
    OA3, 1,
    materials="Hoja y lápiz. La tabla de materiales está escrita en el cuaderno; si quieres, mira papel, cartón, cordel, una bolsa o envase plástico limpio y arcilla que se seca al aire, si tienes.",
    use="Aprenderé a comparar papeles, cartones, fibras, plásticos, cerámicos y desechos según lo que cada uno hace bien. Sirve para elegir el material que cumple la función del objeto.",
    prior=["Sé que un material es de lo que está hecho un objeto.", "Sé escribir criterios comprobables."],
    explain=[
        "Cada material tiene propiedades, que son sus rasgos. El papel es liviano y se dobla fácil, pero se rompe y se moja. El cartón es más firme y sostiene más peso. Las fibras, como lana, hilo o cordel, son delgadas y sirven para atar o tejer. Los plásticos, como bolsas o botellas, no dejan pasar el agua. Las bolsas no son juguete: nunca las pongas sobre la cabeza. Los cerámicos se hacen con arcilla: al secar se endurecen y no se doblan, pero se pueden quebrar si caen.",
        "Los desechos son cosas que se botarían, como cajas, tubos de cartón o envases limpios. Reutilizarlos cuida el medioambiente y es barato, siempre que estén limpios y no tengan bordes que corten. Para elegir, mira la función: si el objeto debe sostener peso, sirve cartón; si debe atar, sirve cordel; si debe proteger del agua, sirve plástico.",
        "Elige con una pregunta: ¿qué debe hacer mi objeto? Luego compara dos materiales según esa función. Aquí hay una simplificación: en la vida real, los materiales tienen más propiedades que las que usamos. Para la arcilla, en clase se usa la que se seca al aire; la cerámica verdadera se cuece en un horno especial y eso lo hace un taller con personas adultas, no se hace en casa.",
    ],
    vocab=[("propiedad", "rasgo de un material, como ser firme o impermeable"), ("fibra", "hilo delgado, como lana, cordel o tela"), ("plástico", "material de bolsas y botellas; muchos no dejan pasar el agua"), ("cerámico", "material hecho con arcilla que se endurece al secar"), ("desecho reutilizable", "cosa que se botaría y se usa de nuevo si está limpia")],
    worked=[
        ("Elegir según la función", "Debes hacer un soporte que sostenga 12 fichas. ¿Qué material sirve: papel suave o cartón?", ["El soporte debe sostener peso.", "El papel suave se dobla.", "El cartón es más firme."], "Cartón"),
        ("Material para proteger del agua", "Una funda debe proteger un cuaderno de la lluvia. ¿Qué sirve más: una bolsa plástica limpia o una hoja de papel?", ["La lluvia moja el papel.", "El plástico no deja pasar el agua."], "La bolsa plástica limpia"),
    ],
    mistakes=[
        ("Elegir el material por el color.", "El color no dice si sirve para la función.", "Elige por la propiedad que necesitas: firme, impermeable, flexible."),
        ("Reutilizar un envase sin lavarlo.", "Puede tener restos y dar mal olor o suciedad.", "Lávalo y sécalo; que no tenga bordes que corten."),
    ],
    R=[
        ("El cordel ¿es una fibra o un cerámico?", "Una fibra", "Es un hilo grueso."),
        ("La arcilla de secado al aire, cuando se seca, ¿se endurece o se queda blanda?", "Se endurece", "Al secar se pone dura."),
        ("Una caja de cartón limpia que se iba a botar ¿es un desecho reutilizable o un cerámico?", "Un desecho reutilizable", "Se vuelve a usar."),
    ],
    C=[
        ("¿Qué propiedad tiene una bolsa plástica que el papel no tiene?", "No deja pasar el agua", "Es impermeable al agua."),
        ("¿Por qué el cartón sostiene más peso que el papel suave?", "Porque es más firme", "Su firmeza resiste el peso."),
        ("¿Por qué reutilizar cajas limpias cuida el medioambiente?", "Porque se gastan menos materiales nuevos", "Se bota menos."),
    ],
    A=[
        ("Debes atar un paquete. ¿Qué material eliges: cordel o arcilla?", "Cordel", "Una fibra sirve para atar."),
        ("Necesitas una pieza dura que no se doble y que se moldee con las manos. ¿Qué eliges: lana o arcilla?", "Arcilla", "Se moldea y al secar se endurece."),
        ("Una tapa de caja de cartón sirve de base. ¿Es un papel, un cartón o una fibra?", "Un cartón", "Es firme y grueso."),
    ],
    Z=[
        ("Rita dice: «Haré el soporte de papel porque es más lindo». ¿Es buena razón? Explica brevemente.", "No, porque debe elegir por la función de sostener peso", "El gusto no mide si sostiene."),
        ("Una maceta de arcilla seca cae al suelo desde una mesa. ¿Qué puede pasar: que se quiebre o que rebote como pelota?", "Que se quiebre", "Los cerámicos son duros pero frágiles."),
    ],
    D=[
        ("Reto: la tabla dice papel: liviano; cartón: firme; plástico: no deja pasar agua; fibra: sirve para atar. Elige un material para cada necesidad: A llevar 4 libros, B atar una caja.", "A cartón; B fibra (cordel)", "Cada material cumple la función."),
        arith("Tienes 3 envases limpios y 5 tubos de cartón para reutilizar. ¿Cuántos desechos reutilizables tienes?", "3+5", "Se suman los envases y los tubos."),
    ],
    ctx=("Pía hará una funda para su cuaderno. Debe cuidarlo de la lluvia, ser liviana y reutilizar algo. Tiene una bolsa plástica limpia, una hoja de papel y cartón. Elige y explica con la propiedad.", "Bolsa plástica limpia, porque no deja pasar el agua y es un desecho reutilizado", "Elige por propiedad y reúso."),
    sc=[
        ("¿Se elige el material por la función o por el color?", "Por la función", "La función dice qué propiedad necesitas."),
        ("¿La cerámica verdadera se cuece en horno?", "Sí", "Lo hace un taller con personas adultas."),
        ("¿Un envase reutilizado debe estar limpio?", "Sí", "Así es higiénico y seguro."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: funda impermeable para un cuaderno. Objeto 2: soporte para 12 fichas. Compara dos materiales de esta lista: papel, cartón, fibra, plástico, arcilla seca, desecho limpio. Escribe una propiedad de cada uno y elige uno según la función.",
        "Objeto 1: plástico (no deja pasar agua) y papel (se moja). Elijo bolsa plástica limpia.",
        ["compara dos materiales", "escribe una propiedad de cada uno", "elige según la función", "dice si es reutilizado"],
        ["comparación de dos materiales con elección"],
        ["elegir por el color", "no decir la propiedad"],
        "Pregunta: «¿qué debe hacer tu objeto y qué material lo logra?». Si responde con el color, vuelve a la función.",
    ),
    reinforce="Mira tres materiales de tu casa y di una propiedad de cada uno.",
    extend="Escribe cuál usarías para un posavasos y explica con una propiedad.",
)

# ------------------------------------------------------------------ OA 03, clase 2
reg(
    OA3, 2,
    materials="Retazos de papel y cartón, un trozo de cordel, un trozo de bolsa plástica limpia, arcilla que se seca al aire, cola fría, témpera, pincel, regla, lápiz y tijeras de punta roma. Delantal para pintar.",
    use="Aprenderé a practicar en retazos las técnicas de medir, marcar, cortar, plegar, unir, pegar y pintar. Sirve para equivocarme en un trozo pequeño y no en el objeto final.",
    prior=["Sé qué propiedades tienen papel, cartón, fibras, plásticos y arcilla.", "Sé que un plan dice qué técnica usar en cada tarea."],
    explain=[
        "Practicar en retazos es probar una técnica en un trozo sobrante. Medir: pon el cero de la regla en el borde y mira el número. Marcar: dibuja un punto en cada extremo y une los puntos con la regla. Cortar: sigue la línea con tijeras de punta roma y aleja los dedos. Plegar: pasa la punta del lápiz por la línea y dobla.",
        "Unir y pegar son parecidos pero distintos. Unir es juntar dos piezas, y puedes hacerlo con cola, cinta, o atando con cordel; pegar es unir con adhesivo. Con la cola fría pon una capa delgada, junta las piezas, presiona y espera que seque. Pintar: moja el pincel, quita el exceso de témpera y pasa en una sola dirección, con delantal puesto.",
        "Con otros materiales cambia un poco. En la bolsa plástica, la cola fría no pega bien; usa cinta. En la arcilla de secado al aire puedes moldear, marcar con un palito y unir con un poco de agua; después se deja secar varios días. Al terminar, limpia, guarda y lávate las manos. La arcilla no se come ni se pone en la cara; al terminar, lávate las manos y no botes restos por el lavamanos. Seguridad: nada de fuego ni cortadores; los cortes difíciles los hace una persona adulta.",
    ],
    vocab=[("retazo", "trozo sobrante de un material"), ("marcar", "dibujar puntos o líneas de guía"), ("plegar", "doblar sobre una línea marcada"), ("unir", "juntar dos piezas"), ("exceso", "lo que sobra, como pintura de más")],
    worked=[
        ("Medir bien", "Quieres medir 8 cm en un cartón. ¿Dónde pones el cero de la regla?", ["Pongo el cero justo en el borde.", "Miro el número 8.", "Hago un punto ahí."], "El cero va en el borde y marco en el 8"),
        ("Elegir cómo unir", "Debes unir dos trozos de bolsa plástica. ¿Cola fría o cinta?", ["La cola fría no pega bien al plástico.", "La cinta sí se adhiere."], "Cinta"),
    ],
    mistakes=[
        ("Empezar a medir desde el número 1 de la regla.", "Todas las medidas salen mal por 1 cm.", "Pon el cero en el borde."),
        ("Echar mucha cola fría.", "Se sale por los bordes y demora en secar.", "Usa una capa delgada."),
    ],
    R=[
        ("Para medir con la regla, ¿pones el cero en el borde o en el número 5?", "En el borde", "Así parte la medida."),
        ("Doblar sobre una línea marcada ¿es plegar o cortar?", "Plegar", "Plegar es doblar."),
        ("Pasar el pincel con témpera ¿es pintar o unir?", "Pintar", "Se aplica color."),
    ],
    C=[
        ("¿Qué técnica usas para dibujar la línea de guía antes de cortar: marcar o plegar?", "Marcar", "La línea de guía se marca."),
        ("¿Por qué conviene practicar en retazos primero?", "Para equivocarse sin perder el material bueno", "Evita errores en el objeto final."),
        ("¿La cola fría pega bien una bolsa plástica?", "No", "Con plástico conviene usar cinta."),
    ],
    A=[
        ("Quieres atar dos tiras de cartón con cordel. ¿Es una técnica de unir o de pintar?", "Unir", "Juntas las piezas con la fibra."),
        ("En un retazo de arcilla, ¿unes dos trozos con un poco de agua o con fuego?", "Con un poco de agua", "El fuego no se usa en clase."),
        arith("Mides un cartón y la marca está en 8 cm. Quieres cortar otro trozo de 5 cm más largo. ¿A qué medida marcas?", "8+5", "Se suma el largo extra.", " cm"),
    ],
    Z=[
        ("Ema recortó fuera de la línea. ¿Qué técnica debe practicar de nuevo en un retazo: medir o cortar siguiendo la línea?", "Cortar siguiendo la línea", "El error fue al cortar."),
        ("Don Aldo pinta con el pincel muy mojado y la témpera chorrea. ¿Qué paso falta? Responde con una frase.", "Quitar el exceso de pintura", "El exceso hace que chorree."),
    ],
    D=[
        ("Reto: ordena las técnicas para una pieza: pintar, medir, cortar, marcar, pegar. Escribe el orden lógico.", "Medir, marcar, cortar, pegar, pintar", "Primero se prepara, luego se arma y al final se pinta."),
        arith("Practicas con 3 retazos de papel, 2 de cartón y 1 de bolsa limpia. ¿Cuántos retazos usas?", "3+2+1", "Se suman todos los retazos."),
    ],
    ctx=("Tienes un retazo de cartón de 10 cm. Debes practicar medir 6 cm, marcar, cortar, y pegar una tira con cola fría. Escribe en orden qué haces y qué cuidado tienes con las tijeras.", "Poner el cero en el borde, marcar el 6, unir los puntos con la regla, cortar alejando los dedos, pegar con capa delgada", "Pasos ordenados y cuidado de seguridad."),
    sc=[
        ("¿Se pone el cero de la regla en el borde?", "Sí", "Así se mide desde cero."),
        ("¿La cola fría se pone en capa gruesa o delgada?", "Delgada", "La capa gruesa se sale."),
        ("¿Para qué sirve un retazo?", "Para practicar", "Permite equivocarse sin perder el objeto."),
    ],
    open_task=(
        "Escoge tres retazos de esta lista: papel, cartón, cordel, bolsa plástica limpia, arcilla que se seca al aire. Practica una técnica en cada uno (por ejemplo: medir y cortar el papel, plegar el cartón, unir con cinta la bolsa, atar el cordel, moldear la arcilla). Anota qué hiciste y qué descubriste.",
        "Papel: medí 8 cm y corté; cartón: plegué sobre una línea; bolsa: la uní con cinta. Descubrí que la cola no pega la bolsa.",
        ["practica tres técnicas en tres materiales", "usa la herramienta correcta", "anota qué descubrió", "cuida la seguridad"],
        ["tres retazos practicados y nota de lo descubierto"],
        ["practicar solo con el material bueno", "usar mal la regla"],
        "Pregunta: «¿qué hiciste distinto en este material?». Si dice nada, muestra cola frente a cinta con la bolsa.",
    ),
    reinforce="Practica doblar una hoja sobre una línea marcada tres veces seguidas.",
    extend="Prueba pegar dos retazos de cartón con cola fría y con cinta, y anota cuál quedó más firme.",
)

# ------------------------------------------------------------------ OA 03, clase 3
reg(
    OA3, 3,
    materials="Cartón limpio reutilizado, regla, lápiz, tijeras de punta roma, cola fría, cinta. Cuaderno para anotar.",
    use="Aprenderé a construir mi objeto siguiendo el plan y revisando en puntos de control. Sirve para corregir a tiempo y no repetir todo.",
    prior=["Sé practicar técnicas en retazos.", "Sé que un punto de control es un momento para revisar."],
    explain=[
        "Construir es seguir el plan paso a paso. Antes de empezar, reúne materiales, herramientas y un lugar despejado. Lee el plan completo. Cada tarea se hace con la técnica que practicaste.",
        "En cada punto de control, compara lo que hiciste con el plan. Si el plan dice 15 cm, mide con la regla. Si la medida está mal, corrige ahí, no después. Es mejor cortar una pieza de más para ajustarla que cortar de menos. Anota lo que corriges, porque servirá para mejorar después.",
        "Cuida la seguridad todo el tiempo: tijeras de punta roma con los dedos lejos de la línea, mesa despejada, cola fría sin tocar la cara, pelo amarrado. Si algo no sale, no te frustres: pide ayuda o prueba de nuevo en un retazo. Al terminar, guarda las sobras que sirvan y bota el resto en el lugar correcto.",
    ],
    vocab=[("punto de control", "momento para comparar con el plan"), ("ajustar", "cambiar un poco algo para que calce"), ("sobras", "trozos de material que quedaron"), ("calzar", "encajar bien una pieza en otra")],
    worked=[
        ("Usar un control", "El plan dice una tira de 15 cm. La cortaste y mide 16 cm. ¿Qué haces?", ["Comparo con el plan en el control.", "Sobra 1 cm.", "Recorto 1 cm con cuidado."], "Recorto 1 cm para llegar a 15 cm"),
        ("Cortar de más y ajustar", "Una pieza debe calzar en un espacio de 10 cm. ¿Es mejor cortar a 9 cm o a 11 cm primero?", ["Si corto 9 cm, no puedo agregar.", "Con 11 cm puedo recortar."], "11 cm, porque se puede recortar"),
    ],
    mistakes=[
        ("Armar todo y recién revisar al final.", "Si hay un error pequeño, afecta todo.", "Revisa en cada control."),
        ("Cortar de menos para ir más rápido.", "No se puede agregar material cortado.", "Corta un poco de más y ajusta."),
    ],
    R=[
        ("¿Se lee el plan completo antes o después de empezar a construir?", "Antes", "Así sabes qué hacer."),
        ("En un punto de control, ¿comparas con el plan o con otro objeto cualquiera?", "Con el plan", "El plan dice qué debe cumplirse."),
        ("¿Cuidas los dedos al cortar con tijeras de punta roma alejándolos de la línea?", "Sí", "Así evitas cortarte."),
    ],
    C=[
        ("¿Por qué es mejor cortar un poco de más?", "Porque se puede recortar después", "Lo que se corta de menos no se agrega."),
        ("¿Para qué anotas lo que corriges?", "Para mejorar después", "Sirve en la próxima vez."),
        ("¿Qué haces si una técnica no sale?", "Pruebas de nuevo en un retazo o pides ayuda", "Es seguro y evita perder el material."),
    ],
    A=[
        arith("El plan pide una tira de 15 cm. La tuya mide 17 cm. ¿Cuántos cm debes recortar?", "17-15", "Se resta la medida del plan a la que cortaste.", " cm"),
        ("El plan pide una pieza de 12 cm y mides 12 cm. ¿La corrección es recortar, agregar o nada?", "Nada", "Ya cumple el plan."),
        ("Un corte de cartón muy duro se complica. ¿Lo haces tú o pides ayuda a una persona adulta?", "Pides ayuda a una persona adulta", "Es más seguro."),
    ],
    Z=[
        ("Mía armó todo sin revisar y no calza una tapa. ¿Qué control olvidó? Responde con una frase.", "Medir las piezas antes de pegarlas", "Así habría visto el error a tiempo."),
        ("Dos niños: A mide en cada control, B solo al final. ¿Cuál tiene menos riesgo de repetir todo?", "A", "Detecta los errores a tiempo."),
    ],
    D=[
        ("Reto: el plan tiene 4 tareas y 3 controles. Escribe qué revisas en cada control para un portalápices de 12 cm.", "Medida de 12 cm; que las piezas calcen; que la cola esté firme", "Tres revisiones concretas."),
        arith("Tienes 40 cm de cinta. Usas 12 cm en la base y 15 cm en las paredes. ¿Cuántos cm de cinta te quedan?", "40-12-15", "Se restan los usados.", " cm"),
    ],
    ctx=("Bruno construye un soporte de 15 cm de alto para 12 fichas. Al medir en el control, mide 14 cm. El plan pide 15 cm. ¿Qué observa y qué decide? Escribe qué hace.", "Falta 1 cm; revisa la pieza y la cambia por una de 15 cm", "Compara con el plan y corrige."),
    sc=[
        ("¿Se revisa en cada punto de control?", "Sí", "Así se corrige a tiempo."),
        ("¿Es mejor cortar de más o de menos?", "De más", "Se puede recortar."),
        ("¿Se anota lo que se corrige?", "Sí", "Ayuda a mejorar después."),
    ],
    open_task=(
        "Construye el portalápices de cartón de 12 cm de alto, siguiendo estas tareas: medir y marcar, cortar, plegar, pegar. Usa tijeras de punta roma. Haz dos puntos de control con medida y anota qué corriges.",
        "Control 1: medí 12 cm en el cartón. Control 2: la tapa calzó. Corregí 1 cm que me sobraba.",
        ["sigue el plan", "hace dos controles con medida", "anota lo que corrige", "cuida la seguridad"],
        ["objeto construido (o un dibujo de él) y notas de control"],
        ["no hacer controles", "cortar de menos"],
        "Pregunta: «¿qué decía el plan y qué mediste?». Si no coinciden, ayúdale a corregir en ese punto.",
    ),
    reinforce="Mide tres objetos de tu casa y anota cada medida con unidad.",
    extend="Construye una cajita de cartón siguiendo un plan de cinco tareas y dos controles.",
)

# ------------------------------------------------------------------ OA 03, clase 4
reg(
    OA3, 4,
    materials="Tu objeto de cartón o papel, témpera, pincel, trozo de lija suave de papel (con ayuda), cola fría, delantal y diario para cubrir la mesa.",
    use="Aprenderé a dar un acabado sin ocultar las fallas. Sirve para que el objeto quede bien y yo vea qué mejorar.",
    prior=["Sé construir con puntos de control.", "Sé pintar con pincel quitando el exceso."],
    explain=[
        "El acabado es lo último que se hace al objeto: limpiar bordes, pegar mejor, pintar o decorar. Un buen acabado protege y deja el objeto cómodo, sin bordes que lastimen. No es solo para que se vea lindo.",
        "No debes tapar las fallas. Una falla es algo que no salió como en el plan, como una pieza torcida o una medida corrida. Si pintas encima sin decir nada, no podrás mejorar. Primero señala la falla con un lápiz, anótala y recién después pinta. Así el objeto queda honesto y aprendes más.",
        "Pintar con cuidado: cubre la mesa, usa delantal, pon poca témpera y pasa el pincel en una sola dirección. Deja secar antes de tocar. Si el cartón tiene un borde áspero, pide a una persona adulta que lo lije con papel de lija fino, en un lugar con aire y sin soplar el polvo; limpia después con un paño húmedo. O recórtalo con tijeras de punta roma. Lava el pincel con agua y lávate las manos.",
    ],
    vocab=[("acabado", "último trabajo que se hace al objeto"), ("falla", "algo que no salió como en el plan"), ("borde áspero", "borde irregular que puede lastimar"), ("lijar", "pasar papel de lija para alisar")],
    worked=[
        ("Decidir antes de pintar", "Tu soporte quedó torcido 1 cm. ¿Qué haces primero: pintar encima o anotar la falla?", ["Si pinto sin anotar, se me olvida.", "Anoto la falla y recién pinto."], "Anotar la falla y después pintar"),
        ("Cuidar el borde", "El borde de una tapa de cartón raspa la mano. ¿Qué haces?", ["Puede lastimar.", "Lo recorto o pido que lo lijen."], "Recortar o lijar con ayuda"),
    ],
    mistakes=[
        ("Pintar mucho para que no se note la falla.", "Se pierde la información para mejorar.", "Anota la falla antes de pintar."),
        ("Tocar la pintura húmeda para ver si secó.", "Se mancha y se arruina el acabado.", "Espera el tiempo de secado."),
    ],
    R=[
        ("Algo que no salió como en el plan ¿es una falla o un acabado?", "Una falla", "Es un error o diferencia con el plan."),
        ("Un borde áspero ¿puede lastimar o es seguro?", "Puede lastimar", "Raspa la piel."),
        ("Para pintar, ¿cubres la mesa con diario o la dejas descubierta?", "La cubres con diario", "Se evitan manchas."),
    ],
    C=[
        ("¿Por qué no se debe tapar una falla con pintura?", "Porque así no se puede mejorar", "Se pierde la información."),
        ("¿Para qué sirve un buen acabado además de verse lindo?", "Para proteger y no lastimar", "Deja el objeto seguro y cómodo."),
        ("¿Cuánta témpera pones en el pincel: poca o mucha?", "Poca", "Evita que chorree."),
    ],
    A=[
        ("Tu portalápices tiene una tira torcida de 1 cm. Escribe la anotación de la falla.", "Tira torcida 1 cm", "Dice qué falla y cuánto."),
        ("Debes lijar un borde de cartón. ¿Lo haces tú solo con una herramienta cortante o con papel de lija suave y ayuda?", "Con papel de lija suave y ayuda", "Es lo seguro."),
        ("Terminaste de pintar. ¿Qué haces con el pincel: lavarlo con agua o dejarlo con pintura?", "Lavarlo con agua", "Así no se endurece."),
    ],
    Z=[
        ("Lía dice: «Pinté todo de negro para que no se vean los errores». ¿Qué pierde? Responde con una frase.", "Pierde ver los errores para mejorar", "Sin ver las fallas no mejora."),
        ("Dos objetos: A con fallas anotadas y B pintado sin anotar. ¿Cuál es mejor para aprender?", "A", "Las fallas anotadas guían la mejora."),
    ],
    D=[
        ("Reto: escribe tres pasos del acabado de un portalápices: limpiar borde, pintar, secar, en el orden correcto y con un cuidado.", "Limpiar borde con ayuda, pintar con poca témpera y delantal, secar sin tocar", "Orden lógico con cuidados."),
        arith("Tu pintura tarda 30 minutos en secar y han pasado 12. ¿Cuántos minutos faltan?", "30-12", "Se resta lo que ya pasó.", " minutos"),
    ],
    ctx=("Tomás terminó su soporte de 15 cm. Una pared quedó 1 cm más baja y un borde raspa. Escribe qué anotas, qué haces con el borde y cuándo pintas.", "Anoto pared 1 cm más baja; recorto o lijo el borde con ayuda; pinto después y dejo secar", "Anota, arregla y pinta."),
    sc=[
        ("¿Se anota la falla antes de pintar?", "Sí", "Así se puede mejorar."),
        ("¿Se toca la pintura húmeda para ver si secó?", "No", "La pintura húmeda se mancha."),
        ("¿El acabado solo sirve para decorar?", "No", "También protege a quien lo usa."),
    ],
    open_task=(
        "Toma tu objeto de cartón o usa este caso: un soporte pintado que quedó con una pared 1 cm más baja y un borde áspero. Escribe una lista de fallas, di cómo arreglas el borde con seguridad y cómo pintas con cuidado.",
        "Fallas: pared 1 cm más baja; borde áspero. Pido que lijen el borde. Pinto con poca témpera, con delantal y dejo secar.",
        ["anota al menos una falla", "arregla el borde con seguridad", "pinta con cuidado", "no oculta la falla"],
        ["lista de fallas y descripción del acabado"],
        ["pintar para tapar la falla", "no cuidar el borde"],
        "Pregunta: «¿qué falla ves y cómo la anotaste?». Si no anotó ninguna, mira el objeto con él.",
    ),
    reinforce="Mira un objeto hecho en casa y busca un borde que podría lastimar.",
    extend="Pinta un trozo de cartón con dos capas y anota cuánto demora en secar cada una.",
)

# ------------------------------------------------------------------ OA 03, clase 5
reg(
    OA3, 5,
    materials="Hoja, lápiz y tu objeto o el caso del cuaderno.",
    use="Aprenderé a documentar las decisiones que tomé y a explicar el uso seguro del objeto. Sirve para que otras personas lo usen sin riesgo y para que yo recuerde por qué lo hice así.",
    prior=["Sé comparar materiales según su función.", "Sé anotar las fallas del acabado."],
    explain=[
        "Documentar es dejar por escrito lo que hiciste y por qué. Una ficha del objeto dice: nombre, para quién es, material elegido y por qué, técnicas usadas, medidas, fallas y mejoras. Así, otra persona puede entender y repetir tu trabajo.",
        "Las decisiones deben llevar una razón. No basta con decir «usé cartón». Escribe «usé cartón porque debía sostener 12 fichas y es firme». También anota qué desechos reutilizaste y cómo cuidaste el medioambiente: por ejemplo, qué sobras guardaste.",
        "El uso seguro dice cómo usar el objeto sin lastimarse y cómo cuidarlo: no mojarlo si es de papel, no usarlo si se rompe y avisar a una persona adulta. Una instrucción clara tiene verbos y números: «Pon como máximo 12 fichas». Revisa la ficha con otra persona para ver si se entiende.",
    ],
    vocab=[("documentar", "dejar por escrito lo que hiciste y por qué"), ("ficha del objeto", "hoja con datos del objeto y de cómo se hizo"), ("decisión", "elección que haces con una razón"), ("uso seguro", "forma de usarlo sin riesgo")],
    worked=[
        ("Escribir una decisión con razón", "Elegiste cartón reutilizado. Escribe la decisión con su razón.", ["Digo qué elegí.", "Digo por qué.", "Uso «porque»."], "Usé cartón reutilizado porque es firme y cuida el medioambiente"),
        ("Instrucción de uso seguro", "Tu soporte aguanta 12 fichas. Escribe una instrucción de uso con número.", ["Debo decir el máximo.", "Uso un verbo de acción."], "Pon como máximo 12 fichas"),
    ],
    mistakes=[
        ("Escribir «usé cartón» sin razón.", "No explica la decisión.", "Agrega «porque…»."),
        ("Olvidar poner un cuidado del objeto.", "Otra persona podría romperlo o lastimarse.", "Escribe el uso seguro con un verbo y un número."),
    ],
    R=[
        ("Dejar por escrito qué hiciste y por qué ¿se llama documentar o pintar?", "Documentar", "Es registrar el trabajo."),
        ("«Usé cartón porque es firme» ¿lleva una razón?", "Sí", "La palabra «porque» introduce la razón."),
        ("«Pon como máximo 12 fichas» ¿tiene un número?", "Sí", "Dice el número 12."),
    ],
    C=[
        ("¿Qué datos lleva una ficha del objeto? Nombra tres.", "Nombre, material con razón, medidas (u otros datos de la ficha)", "Son datos básicos de la ficha."),
        ("¿Por qué conviene anotar las fallas en la ficha?", "Para poder mejorarlas", "Sin anotarlas no se mejoran."),
        ("¿Para qué sirve el uso seguro?", "Para usar el objeto sin lastimarse", "Evita riesgos al usarlo."),
    ],
    A=[
        ("Elegiste una bolsa plástica limpia para una funda. Escribe la decisión con razón.", "Usé bolsa plástica limpia porque no deja pasar el agua", "Lleva la razón por la propiedad."),
        ("Tu portalápices guarda 6 lápices. Escribe una instrucción de uso con número.", "Guarda como máximo 6 lápices", "Dice el máximo con número."),
        arith("Reutilizaste 3 tubos de cartón y 2 cajas. ¿Cuántos desechos reutilizaste?", "3+2", "Se suman los tubos y las cajas."),
    ],
    Z=[
        ("Dos fichas: A dice «usé cartón», B dice «usé cartón porque es firme». ¿Cuál documenta mejor la decisión?", "B", "B da la razón."),
        ("Una ficha no dice el uso seguro y el objeto tiene un borde áspero. ¿Qué falta anotar?", "El cuidado con el borde", "Es un riesgo que debe decirse."),
    ],
    D=[
        ("Reto: escribe una ficha corta de un soporte de cartón con nombre, material con razón, una falla y un uso seguro.", "Soporte de fichas; cartón porque es firme; falla: pared 1 cm baja; usar máximo 12 fichas", "Cuatro datos con razón."),
        arith("Documentaste 4 fichas el lunes y 3 el martes. ¿Cuántas fichas tienes?", "4+3", "Se suman las fichas."),
    ],
    ctx=("Elena termina un portalápices de cartón reutilizado que guarda 6 lápices. Una pared quedó 1 cm más baja. Escribe su ficha: nombre, material con razón, una falla y una instrucción de uso seguro.", "Portalápices; cartón reutilizado porque es firme y cuida el medioambiente; falla: pared 1 cm baja; guarda como máximo 6 lápices", "Cumple los cuatro datos."),
    sc=[
        ("¿Una decisión lleva razón?", "Sí", "Debe explicar por qué."),
        ("¿La ficha debe anotar las fallas?", "Sí", "Ayuda a mejorar."),
        ("¿El uso seguro tiene números y verbos?", "Sí", "Así es claro."),
    ],
    open_task=(
        "Toma tu objeto o usa este caso: un guardalápices de cartón que guarda 6 lápices, hecho con un tubo reutilizado, con una falla de 1 cm. Haz su ficha con nombre, para quién es, material con razón, técnicas, medidas, una falla, un cuidado del medioambiente y una instrucción de uso seguro.",
        "Guardalápices para Dani; cartón reutilizado porque es firme; técnicas: medir, cortar y pegar; falla: 1 cm; reutilizó un tubo; guarda como máximo 6 lápices.",
        ["completa todos los datos", "da una razón por la decisión", "anota una falla", "escribe uso seguro con número"],
        ["ficha completa del objeto"],
        ["decisiones sin razón", "faltar el uso seguro"],
        "Pregunta: «¿por qué elegiste ese material?». Si no da razón, pídele usar «porque».",
    ),
    reinforce="Haz una ficha de un objeto de tu casa con nombre, material y para qué sirve.",
    extend="Escribe tres instrucciones de uso seguro para un objeto de cartón.",
)

# ------------------------------------------------------------------ OA 04, clase 1
reg(
    OA4, 1,
    materials="Hoja y lápiz. Los criterios están escritos en el cuaderno.",
    use="Aprenderé a escribir criterios técnicos, medioambientales y de seguridad antes de probar. Sirve para evaluar con reglas y no con gustos.",
    prior=["Sé que un criterio se puede comprobar.", "Sé que probar es mirar si el objeto cumple su función."],
    explain=[
        "Evaluar es juzgar qué tan bien cumple el objeto, usando criterios. Se deben escribir antes de probar. Si los escribes después, puedes cambiarlos para que te salga bien. Los criterios técnicos hablan de la función y las medidas: «sostiene 12 fichas», «mide menos de 20 cm». Los medioambientales hablan del cuidado de la naturaleza: «usa material reutilizado», «no genera sobras que no se puedan usar». Los de seguridad hablan de cuidar a las personas: «sin puntas ni bordes que corten».",
        "Un buen criterio se comprueba con una prueba clara, con un número cuando se pueda. Escribe, junto al criterio, cómo lo comprobarás. Si dos personas prueban, deben obtener el mismo resultado. Eso hace justa la evaluación.",
        "Se puede evaluar el trabajo propio y el de otros, solos o en equipo. Cuando evalúas el trabajo de otros, mira el objeto y no a la persona. Dices qué cumple y qué podría mejorar, con respeto. Así ayudas y no ofendes.",
    ],
    vocab=[("evaluar", "juzgar qué tan bien cumple algo con criterios"), ("criterio técnico", "habla de la función y las medidas"), ("criterio medioambiental", "habla del cuidado de la naturaleza"), ("criterio de seguridad", "habla del cuidado de las personas"), ("prueba", "acción para comprobar un criterio")],
    worked=[
        ("Clasificar criterios", "Clasifica: A «mide menos de 20 cm», B «usa cartón reutilizado», C «sin bordes que corten». ¿De qué tipo es cada uno?", ["A habla de medida: técnico.", "B habla de reutilizar: medioambiental.", "C habla de no cortar: seguridad."], "A técnico, B medioambiental, C seguridad"),
        ("Decir cómo comprobar", "El criterio es «sostiene 12 fichas». ¿Cómo lo comprobarás?", ["Necesito una acción.", "Pongo las fichas y miro."], "Poniendo 12 fichas y mirando que no se caiga"),
    ],
    mistakes=[
        ("Escribir los criterios después de probar.", "Se pueden ajustar para que parezca que salió bien.", "Escríbelos antes de probar."),
        ("Evaluar a la persona y no al objeto: «eres malo para esto».", "No ayuda y puede ofender.", "Habla del objeto: «el soporte se inclinó con 12 fichas»."),
    ],
    R=[
        ("«Sin puntas que corten» ¿es un criterio de seguridad o medioambiental?", "De seguridad", "Cuida a las personas."),
        ("«Usa cartón reutilizado» ¿es medioambiental o técnico?", "Medioambiental", "Reutilizar cuida la naturaleza."),
        ("¿Los criterios se escriben antes o después de probar?", "Antes", "Así la evaluación es justa."),
    ],
    C=[
        ("¿Por qué se escriben los criterios antes de probar?", "Para que no se cambien según el resultado", "Así la evaluación es justa."),
        ("¿Qué debe acompañar a un criterio para saber si se cumple?", "Cómo se comprobará", "Dice la acción de la prueba."),
        ("Al evaluar el trabajo de otro, ¿hablas del objeto o de la persona?", "Del objeto", "Así es respetuoso y útil."),
    ],
    A=[
        ("Escribe un criterio técnico con número para un soporte de 12 fichas.", "Sostiene 12 fichas sin caerse", "Tiene función y número."),
        ("Escribe un criterio de seguridad para un portalápices de cartón.", "Sin bordes ni puntas que corten", "Cuida a las personas."),
        ("Quieres comprobar «mide menos de 20 cm». ¿Qué herramienta usas: regla o pincel?", "Regla", "La regla mide."),
    ],
    Z=[
        ("Un compañero dice: «Mi soporte es perfecto porque me gusta». ¿Qué le falta para evaluar bien?", "Criterios comprobables", "Gustar no es medir."),
        ("Dos evaluaciones: A «el soporte se inclinó con 12 fichas» y B «eres lento». ¿Cuál es respetuosa y útil?", "A", "Habla del objeto con un dato."),
    ],
    D=[
        ("Reto: escribe un criterio técnico, uno medioambiental y uno de seguridad para una funda de cuaderno, cada uno con su forma de comprobar.", "Técnico: cabe un cuaderno de 30 cm (regla); medioambiental: usa bolsa reutilizada (mirar); seguridad: sin bordes que corten (tocar con cuidado)", "Tres criterios con comprobación."),
        arith("Un soporte cumple 4 de 6 criterios. ¿Cuántos criterios no cumple?", "6-4", "Se resta lo cumplido del total."),
    ],
    ctx=("Valeria evaluará un portalápices de 12 cm que debe guardar 6 lápices, usar cartón reutilizado y no tener puntas. Escribe los tres criterios, uno de cada tipo, y cómo comprobar cada uno.", "Técnico: guarda 6 lápices (ponerlos); medioambiental: cartón reutilizado (mirar el material); seguridad: sin puntas (revisar con cuidado)", "Tres criterios y su comprobación."),
    sc=[
        ("¿Se puede juzgar un objeto con criterios escritos antes de probar?", "Sí", "Eso hace justa la evaluación."),
        ("¿Un criterio técnico habla de función y medidas?", "Sí", "Es su definición."),
        ("¿Evaluar el trabajo de otros se hace con respeto?", "Sí", "Se habla del objeto, no de la persona."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: soporte para 12 fichas. Objeto 2: funda impermeable de cuaderno. Escribe tres criterios, uno técnico, uno medioambiental y uno de seguridad, y al lado cómo comprobarás cada uno. Hazlo antes de probar.",
        "Objeto 1: técnico: sostiene 12 fichas (poniéndolas); medioambiental: cartón reutilizado (mirar); seguridad: sin bordes que corten (tocar con cuidado).",
        ["escribe tres criterios de tipos distintos", "dice cómo comprobar cada uno", "los escribe antes de probar"],
        ["tabla de criterios y comprobación"],
        ["criterios que no se pueden comprobar", "criterios escritos después de probar"],
        "Pregunta: «¿cómo sabrás si cumple?». Si no puede decirlo, ayúdale a escribirlo con una acción.",
    ),
    reinforce="Escribe dos criterios para evaluar una mochila de tu casa.",
    extend="Elige un objeto de tu casa y escribe un criterio técnico, uno medioambiental y uno de seguridad.",
)

# ------------------------------------------------------------------ OA 04, clase 2
reg(
    OA4, 2,
    materials="Tu soporte o torre de cartón, 12 fichas o botones grandes de plástico (más grandes que una moneda), regla y hoja para anotar.",
    use="Aprenderé a hacer una prueba repetible: la misma en las mismas condiciones, varias veces. Sirve para que el resultado sea confiable.",
    prior=["Sé escribir criterios técnicos, medioambientales y de seguridad.", "Sé que cada criterio se comprueba con una acción."],
    explain=[
        "Una prueba repetible se hace igual cada vez. Si pruebas hoy con 12 fichas sobre la mesa y mañana con 8 fichas sobre la cama, no puedes comparar. Para que sea repetible, decide antes y deja por escrito: qué se prueba, con qué cantidad, en qué lugar, quién la hace y cuántas veces.",
        "Se repite la prueba, por ejemplo 3 veces, porque una sola vez puede ser casualidad. Si sale igual las 3 veces, el resultado es confiable. Si sale distinto, algo cambió en la prueba o el objeto es inestable. No cambies nada entre una prueba y otra, salvo lo que quieras estudiar.",
        "Cuida la seguridad: prueba sobre una mesa despejada, sin acercar la cara, y no uses objetos pequeños que puedan tragar los más chicos. Usa fichas grandes o botones más grandes que una moneda. Si algo se cae, no lo recojas corriendo; avisa si hay algo roto.",
    ],
    vocab=[("prueba repetible", "prueba que se hace igual cada vez"), ("condición", "dato de la prueba que debe mantenerse, como el lugar"), ("confiable", "que se puede creer porque sale igual"), ("casualidad", "algo que ocurre una vez sin razón")],
    worked=[
        ("Detectar un cambio", "Lunes: 12 fichas sobre la mesa. Martes: 8 fichas sobre la cama. ¿Se puede comparar?", ["La cantidad cambió.", "El lugar también.", "No es igual."], "No, porque cambió la cantidad y el lugar"),
        ("Repetir la prueba", "El soporte se cae a la 3.ª ficha en el 1.er intento. ¿Basta con un intento?", ["Puede ser casualidad.", "Repito 2 veces más."], "No, se repite al menos 3 veces"),
    ],
    mistakes=[
        ("Cambiar la cantidad de fichas entre una prueba y otra.", "No se puede comparar.", "Usa siempre 12 fichas."),
        ("Confiar en un solo intento.", "Puede ser casualidad.", "Repite al menos 3 veces."),
    ],
    R=[
        ("Una prueba que se hace igual cada vez ¿es repetible o casual?", "Repetible", "Se hace del mismo modo."),
        ("Para probar, ¿usas fichas más grandes que una moneda o cosas muy pequeñas?", "Más grandes que una moneda", "Las pequeñas se pueden tragar."),
        ("¿La prueba se hace sobre una mesa despejada o sobre un lugar con cosas?", "Sobre una mesa despejada", "Así es seguro."),
    ],
    C=[
        ("¿Por qué se repite la prueba 3 veces?", "Para ver si el resultado se repite y no es casualidad", "Un solo intento puede ser casual."),
        ("Si cambias el lugar entre pruebas, ¿puedes comparar?", "No", "Cambia una condición."),
        ("Antes de probar, ¿escribes la cantidad, el lugar y cuántas veces, o lo decides sobre la marcha?", "Lo escribes antes", "Así la prueba queda repetible."),
    ],
    A=[
        ("Escribe las condiciones de una prueba para el soporte: cantidad, lugar y número de intentos.", "12 fichas, sobre la mesa, 3 intentos", "Tres condiciones claras."),
        ("En el intento 1 aguanta 12 fichas, en el 2 aguanta 12 y en el 3 aguanta 12. ¿El resultado es confiable?", "Sí", "Salió igual las tres veces."),
        arith("Haces la prueba 3 veces por día durante 2 días. ¿Cuántas pruebas haces?", "3*2", "Se multiplican las pruebas por los días."),
    ],
    Z=[
        ("Dos niños prueban el mismo soporte: Ana con 12 fichas y Beto con 15. ¿Pueden comparar? Explica.", "No, porque usaron distinta cantidad", "La cantidad debe ser igual."),
        ("En 3 intentos, el soporte aguanta 12, 6 y 12 fichas. ¿Es confiable? Responde con una frase.", "No, porque un resultado fue distinto", "Cambió algo o el soporte es inestable."),
    ],
    D=[
        ("Reto: escribe un protocolo de 4 puntos para probar una torre de cartón: qué, cantidad, lugar, intentos.", "Torre de cartón; 12 fichas; sobre la mesa; 3 intentos", "Incluye los cuatro datos pedidos."),
        arith("Cada prueba demora 5 minutos y haces 3. ¿Cuántos minutos demoras en total?", "5*3", "Se multiplica el tiempo por las pruebas."),
    ],
    ctx=("Rafa quiere probar su soporte de 12 fichas. Hoy lo hará sobre la mesa de la cocina. Escribe las condiciones que mantendrá igual y cuántas veces repetirá, sin usar objetos pequeños.", "12 fichas grandes, mesa de la cocina, misma persona, 3 intentos", "Condiciones fijas y repeticiones."),
    sc=[
        ("¿Se repite la prueba?", "Sí", "Para evitar casualidades."),
        ("¿Las condiciones cambian entre pruebas?", "No", "Deben ser iguales."),
        ("¿La seguridad incluye mesa despejada?", "Sí", "Evita golpes y caídas."),
    ],
    open_task=(
        "Escoge un objeto. Objeto 1: soporte para 12 fichas. Objeto 2: torre de cartón de 15 cm. Escribe el protocolo de la prueba con qué pruebas, cantidad, lugar, quién y cuántos intentos, y haz la prueba tres veces. Anota los resultados.",
        "Objeto 1: 12 fichas grandes, mesa, yo, 3 intentos: aguantó, aguantó, aguantó.",
        ["escribe el protocolo", "mantiene las condiciones", "repite 3 veces", "anota los resultados"],
        ["protocolo y tres resultados"],
        ["cambiar la cantidad entre intentos", "probar una sola vez"],
        "Pregunta: «¿hiciste todo igual en cada intento?». Si cambió algo, repite.",
    ),
    reinforce="Prueba tres veces cuántas fichas sostiene una torre de cartón, siempre con las mismas condiciones.",
    extend="Escribe un protocolo para probar si una bolsa plástica protege una hoja de unas gotas de agua, con ayuda de una persona adulta.",
)

# ------------------------------------------------------------------ OA 04, clase 3
reg(
    OA4, 3,
    materials="Hoja y lápiz. Las tablas con resultados están escritas en el cuaderno.",
    use="Aprenderé a registrar los resultados de una prueba y las fallas en una tabla. Sirve para ver qué pasó con datos y no con recuerdos.",
    prior=["Sé hacer una prueba repetible.", "Sé que una falla es lo que no salió como en el plan."],
    explain=[
        "Registrar es anotar lo que ocurrió mientras ocurre. Una tabla ordena los datos: cada fila es un intento y cada columna es un dato, como el número del intento, cuántas fichas aguantó y qué falla hubo. Anota en la prueba, no después, porque se olvida.",
        "Anota lo que ves, sin opinar. «Se inclinó a la izquierda con 9 fichas» es un dato. «Quedó fatal» es una opinión. También anota las fallas: dónde se quebró, qué pieza se despegó. Una falla anotada ayuda a mejorar.",
        "Para leer la tabla, compara los intentos. Mira cuál fue el máximo, el mínimo y si se repite. También puedes sumar o restar: si aguantó 12, 12 y 9, la diferencia entre el mejor y el peor es 3. Una tabla clara tiene títulos, unidades y datos completos.",
    ],
    vocab=[("registrar", "anotar lo que ocurre"), ("tabla", "cuadro de filas y columnas con datos"), ("fila", "línea horizontal de la tabla"), ("columna", "línea vertical de la tabla"), ("dato", "información anotada, sin opinión")],
    worked=[
        ("Leer una tabla", "Intento 1: aguantó 12 fichas. Intento 2: aguantó 12. Intento 3: aguantó 9, se inclinó a la izquierda. ¿Cuál fue el peor intento?", ["Comparo los números.", "9 es el menor.", "El peor es el 3."], "El intento 3"),
        ("Dato u opinión", "Compara A «se despegó la base en el intento 2» y B «quedó feo». ¿Cuál es un dato?", ["A dice qué ocurrió.", "B es una opinión."], "A"),
    ],
    mistakes=[
        ("Anotar una opinión como «salió mal».", "No dice qué ocurrió ni dónde.", "Anota el dato: «se inclinó con 9 fichas»."),
        ("Dejar de anotar por confiar en la memoria.", "Se olvidan los datos.", "Anota durante la prueba."),
    ],
    R=[
        ("En una tabla, ¿cada intento va en una fila o en una columna?", "En una fila", "Cada fila es un intento."),
        ("«Se despegó la base» ¿es un dato o una opinión?", "Un dato", "Dice qué ocurrió."),
        ("«Quedó horrible» ¿es un dato o una opinión?", "Una opinión", "No dice qué pasó."),
    ],
    C=[
        ("¿Por qué conviene anotar durante la prueba?", "Para no olvidar los datos", "La memoria falla."),
        ("¿Qué ayuda a mejorar: anotar las fallas o ignorarlas?", "Anotarlas", "Se ve qué cambiar."),
        ("Una tabla con títulos y unidades ¿es más clara o más confusa?", "Más clara", "Se entiende cada dato."),
    ],
    A=[
        arith("Tabla: intento 1 aguantó 12 fichas, intento 2 aguantó 10 y intento 3 aguantó 12. ¿Cuántas fichas más aguantó el 1 que el 2?", "12-10", "Se resta lo del intento 2 al del intento 1."),
        ("En el intento 2 la base se despegó. Escribe cómo lo anotas como dato.", "Intento 2: se despegó la base", "Dice dónde y cuándo."),
        arith("Tabla: aguantó 12, 12 y 9 fichas en tres intentos. ¿Cuántas fichas más aguantó el mejor intento que el peor?", "12-9", "Se resta el peor resultado al mejor."),
    ],
    Z=[
        ("Ana anotó: «salió fatal». Mía anotó: «se inclinó con 9 fichas». ¿Cuál ayuda más a mejorar?", "La de Mía", "Es un dato concreto."),
        ("En una tabla, el intento 1 aguantó 12, el 2 aguantó 12 y el 3 aguantó 4. ¿Qué intento conviene mirar para encontrar la falla?", "El 3", "Es el distinto."),
    ],
    D=[
        ("Reto: completa una tabla de 3 intentos con columnas intento, fichas aguantadas y falla. Datos: 12 y sin falla; 12 y sin falla; 8 y base se despegó.", "1: 12, ninguna; 2: 12, ninguna; 3: 8, base se despegó", "Los datos van en las columnas."),
        arith("Un soporte debe aguantar 12 y en el intento 3 aguantó 8. ¿Cuántas fichas le faltaron?", "12-8", "Se resta lo que aguantó a lo pedido."),
    ],
    ctx=("Dani probó su soporte tres veces. El 1.º aguantó 12 fichas, el 2.º aguantó 12 y el 3.º aguantó 7 y la pared se dobló. Haz la tabla con intento, fichas y falla, e indica el peor intento.", "1: 12 sin falla; 2: 12 sin falla; 3: 7, pared doblada. El peor es el 3", "Tabla completa y análisis."),
    sc=[
        ("¿Se anotan datos u opiniones?", "Datos", "Los datos se pueden comprobar."),
        ("¿Se anota durante o después de la prueba?", "Durante", "Así no se olvida."),
        ("¿Una tabla tiene filas y columnas?", "Sí", "Así se organiza."),
    ],
    open_task=(
        "Usa estos datos de tres intentos con una torre de cartón de 15 cm: intento 1 aguantó 10 fichas y quedó firme; intento 2 aguantó 10 fichas y quedó firme; intento 3 aguantó 6 fichas y se inclinó a la derecha. Haz una tabla con intento, fichas y falla, y escribe cuál fue el mejor y cuál el peor intento.",
        "1: 10 firme; 2: 10 firme; 3: 6 se inclinó a la derecha. El mejor 1 y 2; el peor 3.",
        ["hace la tabla con datos correctos", "distingue datos de opiniones", "dice el mejor y el peor intento"],
        ["tabla con análisis"],
        ["anotar opiniones", "tabla incompleta"],
        "Pregunta: «¿esto es un dato o una opinión?». Si es opinión, pídele escribir qué se vio.",
    ),
    reinforce="Anota tres datos de una prueba que hagas en casa con una torre de papel.",
    extend="Haz una tabla de cinco intentos y calcula la diferencia entre el mejor y el peor resultado.",
)

# ------------------------------------------------------------------ OA 04, clase 4
reg(
    OA4, 4,
    materials="Hoja y lápiz. Los diálogos están escritos en el cuaderno.",
    use="Aprenderé a conversar sobre los resultados usando evidencia y respeto. Sirve para ponernos de acuerdo en qué mejorar.",
    prior=["Sé registrar datos de una prueba en una tabla.", "Sé que se evalúa el objeto y no a la persona."],
    explain=[
        "Dialogar desde evidencia es conversar usando los datos de la tabla. La evidencia es lo que se vio y se anotó. En vez de decir «creo que está mal», dices «en el intento 3 aguantó 9 fichas y el plan pedía 12». Así la conversación se basa en datos.",
        "Un buen diálogo tiene turnos: uno habla, los demás escuchan. Para opinar, usa frases como «Vi que…», «Según la tabla…», «Podemos mejorar…». Para responder, di «Estoy de acuerdo porque…» o «Yo vi otra cosa en…». Si no están de acuerdo, vuelven a mirar la tabla.",
        "Las críticas al trabajo propio y al ajeno se dicen con respeto: primero lo que cumple, luego lo que se puede mejorar, y al final una idea concreta. «El soporte aguantó 12 fichas. La base se despegó. Podemos pegarla con más cola». Cuida el tono y no hables de la persona.",
    ],
    vocab=[("evidencia", "lo que se vio y se anotó"), ("turno", "momento en que cada persona habla"), ("estar de acuerdo", "pensar lo mismo por una razón"), ("crítica respetuosa", "comentario que ayuda a mejorar")],
    worked=[
        ("Opinar con evidencia", "La tabla dice que en el intento 3 aguantó 9 fichas y el plan pedía 12. Escribe una frase con evidencia.", ["Empiezo con «Vi que».", "Uso los números."], "Vi que en el intento 3 aguantó 9 fichas y el plan pedía 12"),
        ("Crítica respetuosa", "Un compañero hizo un soporte que aguantó 12 fichas, pero su base se despegó. Dile una crítica en tres partes.", ["Primero lo que cumple.", "Luego lo que mejorar.", "Al final una idea."], "Tu soporte aguantó 12 fichas. La base se despegó. Podrías pegarla con más cola"),
    ],
    mistakes=[
        ("Decir «no sirve» sin datos.", "No dice qué falló ni cómo mejorar.", "Usa un dato de la tabla."),
        ("Hablar de la persona: «eres desordenado».", "Ofende y no ayuda.", "Habla del objeto."),
    ],
    R=[
        ("Lo que se vio y se anotó ¿es evidencia o un deseo?", "Evidencia", "Son datos registrados."),
        ("En un diálogo, ¿todos hablan a la vez o por turnos?", "Por turnos", "Así se escucha."),
        ("«Vi que aguantó 12 fichas» ¿usa un dato?", "Sí", "Tiene un número."),
    ],
    C=[
        ("¿Por qué dialogar con evidencia es mejor que opinar sin datos?", "Porque se basa en lo que realmente ocurrió", "Los datos son comprobables."),
        ("En una crítica respetuosa, ¿qué se dice primero: lo que cumple o lo que falla?", "Lo que cumple", "Ese orden ayuda y respeta."),
        ("Si dos personas no están de acuerdo, ¿qué hacen: pelear o mirar la tabla?", "Mirar la tabla", "La evidencia resuelve la duda."),
    ],
    A=[
        ("La tabla dice: intento 2 aguantó 8 fichas y el plan pedía 12. Escribe una frase con «Según la tabla».", "Según la tabla, en el intento 2 aguantó 8 fichas y el plan pedía 12", "Usa los datos."),
        ("Responde a un compañero que dice «la base se despegó» estando de acuerdo, con una razón.", "Estoy de acuerdo porque en el intento 2 se despegó la base", "Da una razón con evidencia."),
        arith("El plan pedía 12 fichas y el soporte aguantó 8. ¿Cuántas fichas le faltaron?", "12-8", "Se restan las fichas."),
    ],
    Z=[
        ("Pedro dice: «Tu torre no sirve». ¿Qué le falta para ser útil? Responde con una frase.", "Un dato y una idea para mejorar", "Sin dato no ayuda."),
        ("Dos comentarios: A «la torre es fea» y B «la torre aguantó 10 fichas y se inclinó; pega mejor la base». ¿Cuál es mejor?", "B", "Tiene dato e idea."),
    ],
    D=[
        ("Reto: escribe una crítica respetuosa en tres partes para un soporte que aguantó 12 fichas pero tiene un borde áspero.", "Aguantó 12 fichas; el borde está áspero; podrías lijarlo con ayuda", "Cumple, mejora, idea."),
        arith("En un equipo de 4, 3 están de acuerdo con una mejora. ¿Cuántos no están de acuerdo?", "4-3", "Se resta a los que están de acuerdo."),
    ],
    ctx=("En equipo, Sol dice que su torre es la mejor. La tabla muestra que aguantó 12, 12 y 7 fichas. Escribe qué responderías con respeto, usando la evidencia, y una idea de mejora.", "Aguantó 12 fichas dos veces, pero 7 en el tercer intento; podemos revisar qué cambió en ese intento y reforzar la base", "Respeto, evidencia e idea."),
    sc=[
        ("¿Se dialoga con evidencia?", "Sí", "Así es objetivo."),
        ("¿Se habla de la persona o del objeto?", "Del objeto", "Así es respetuoso con todos."),
        ("¿Una crítica incluye una idea de mejora?", "Sí", "Ayuda a avanzar."),
    ],
    open_task=(
        "Usa este caso: la tabla del soporte de Dani dice intento 1: 12 fichas; intento 2: 12 fichas; intento 3: 7 fichas, pared doblada. Escribe un diálogo de cuatro frases: una de evidencia, una de acuerdo, una de desacuerdo respetuoso y una idea de mejora.",
        "Vi que el intento 3 aguantó 7. Estoy de acuerdo porque la pared se dobló. Yo vi otra cosa: en los dos primeros aguantó 12. Podemos reforzar la pared.",
        ["usa evidencia de la tabla", "habla del objeto", "incluye acuerdo y desacuerdo respetuoso", "propone una mejora"],
        ["diálogo escrito de cuatro frases"],
        ["opinar sin datos", "hablar de la persona"],
        "Pregunta: «¿en qué dato te basas?». Si no tiene uno, vuelve a la tabla.",
    ),
    reinforce="Comenta a una persona de tu casa algo bueno y algo por mejorar de un objeto, con respeto.",
    extend="Escribe un diálogo de seis frases entre dos niños que evalúan una funda de cuaderno.",
)

# ------------------------------------------------------------------ OA 04, clase 5
reg(
    OA4, 5,
    materials="Hoja y lápiz. Los datos de las pruebas están en el cuaderno.",
    use="Aprenderé a mejorar el objeto cambiando solo una variable y a volver a probar. Sirve para saber qué cambio hizo la diferencia.",
    prior=["Sé hacer una prueba repetible.", "Sé registrar resultados y dialogar con evidencia."],
    explain=[
        "Para mejorar un objeto, cambia solo una cosa a la vez. Esa cosa es la variable: por ejemplo, el grosor del cartón, la cantidad de cola o el largo de la base. Si cambias dos cosas a la vez, no sabrás cuál produjo el cambio.",
        "Los pasos son: mirar la falla, elegir una variable que podría explicarla, cambiarla, mantener todo lo demás igual y probar de nuevo con el mismo protocolo. Después compara la tabla nueva con la antigua. Si mejoró, anota el cambio; si empeoró, vuelve atrás y prueba otro.",
        "Anota los dos resultados juntos: antes y después. Escribe el cambio con un número: «base de 20 cm a 25 cm». También revisa si el cambio respeta los criterios de seguridad y medioambiente: aumentar la base no debe dejar bordes que corten, y debe gastar poco material. La mejora vale si cumple todos los criterios.",
    ],
    vocab=[("variable", "cosa que cambias para ver qué efecto tiene"), ("mejorar", "cambiar para que cumpla mejor"), ("antes y después", "resultado anterior y resultado nuevo"), ("mantener igual", "no cambiar las demás condiciones")],
    worked=[
        ("Elegir una sola variable", "Una torre se cae con 9 fichas. Quieres probar base de 25 cm en vez de 20 cm y cartón más grueso. ¿Es buena idea cambiar las dos?", ["Si cambio dos cosas, no sé cuál sirvió.", "Cambio una por vez."], "No, se cambia solo una a la vez"),
        ("Comparar antes y después", "Antes aguantó 9 fichas. Con la base más ancha aguantó 12. ¿Mejoró? ¿Cuánto?", ["Comparo 12 con 9.", "Resto: 12 menos 9."], "Sí, mejoró en 3 fichas"),
    ],
    mistakes=[
        ("Cambiar tres cosas a la vez.", "No se sabe cuál fue la que mejoró.", "Cambia una variable por vez."),
        ("Probar el cambio con otra cantidad de fichas.", "No se puede comparar.", "Mantén igual el protocolo."),
    ],
    R=[
        ("Cuando mejoras, ¿cambias una cosa o muchas a la vez?", "Una cosa", "Así sabes cuál sirvió."),
        ("Lo que cambias en una prueba se llama variable. ¿La base más ancha es una variable?", "Sí", "Es lo que cambias."),
        ("Después de cambiar, ¿vuelves a probar con el mismo protocolo?", "Sí", "Así se puede comparar."),
    ],
    C=[
        ("¿Por qué no se cambian dos cosas a la vez?", "Porque no se sabe cuál produjo el cambio", "Se mezclan los efectos."),
        ("Si la mejora no resultó, ¿qué haces?", "Vuelves atrás y pruebas otra variable", "Así sigues aprendiendo."),
        ("¿La mejora debe respetar los criterios de seguridad?", "Sí", "La seguridad va primero."),
    ],
    A=[
        arith("Antes aguantó 8 fichas y después aguantó 12. ¿Cuántas fichas más aguantó?", "12-8", "Se resta el antes al después."),
        ("Una torre se inclina por una base estrecha de 15 cm. ¿Qué variable cambias: el ancho de la base o el color?", "El ancho de la base", "La base explica la inclinación."),
        ("Cambiaste la base de 15 cm a 20 cm. Escribe cómo anotas el cambio con número.", "Base de 15 cm a 20 cm", "Muestra el antes y el después."),
    ],
    Z=[
        ("Eli cambió el grosor del cartón y también la cantidad de cola, y mejoró. ¿Sabe cuál ayudó? Responde sí o no y por qué.", "No, porque cambió dos cosas", "No puede separar los efectos."),
        ("Una base más ancha mejoró la estabilidad pero ahora tiene una punta que corta. ¿Vale la mejora? Explica.", "No, hasta corregir la punta", "La seguridad también cuenta."),
    ],
    D=[
        ("Reto: antes aguantó 9 fichas y después 12 con base de 25 cm. Escribe el cambio, el resultado y si cumple el criterio de 12 fichas.", "Base de 20 a 25 cm; de 9 a 12 fichas; sí cumple", "Cambio, resultado y conclusión."),
        arith("Antes tu torre se caía a las 9 fichas. La meta es 12. ¿Cuántas fichas más debes lograr?", "12-9", "Se resta lo que aguanta a la meta."),
    ],
    ctx=("Mía probó su soporte y aguantó 9 fichas; la meta es 12. Piensa que la causa es la base angosta de 15 cm. Escribe qué variable cambia, qué mantiene igual y qué vuelve a hacer.", "Cambia la base de 15 a 20 cm; mantiene igual el cartón, las fichas y el lugar; vuelve a probar 3 veces", "Una variable y mismo protocolo."),
    sc=[
        ("¿Se cambia una variable a la vez?", "Sí", "Así se entiende el efecto."),
        ("¿Se vuelve a probar igual?", "Sí", "Para poder comparar."),
        ("¿Se anotan el antes y el después?", "Sí", "Se ve la mejora."),
    ],
    open_task=(
        "Usa este caso: un soporte aguantó 8 fichas y la meta es 12. Escribe qué falla ves, qué variable cambiarías (base más ancha, cartón más grueso o más cola), qué mantienes igual, cómo vuelves a probar y cómo comparas.",
        "Falla: se inclina. Variable: base de 15 a 20 cm. Igual: cartón, fichas, mesa. Pruebo 3 veces. Comparo 8 con el nuevo resultado.",
        ["elige una sola variable", "mantiene lo demás igual", "vuelve a probar", "compara antes y después"],
        ["plan de mejora y comparación"],
        ["cambiar varias variables", "no volver a probar"],
        "Pregunta: «¿qué cambiaste y qué dejaste igual?». Si cambió más de una cosa, pídele elegir una.",
    ),
    reinforce="Mejora una torre de papel cambiando solo su base y prueba de nuevo.",
    extend="Cambia otra variable de tu objeto y compara los dos resultados en una tabla.",
)
