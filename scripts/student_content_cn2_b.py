"""Cuaderno del estudiante, 2.º básico Ciencias Naturales: OA 09 (propiedades y cambios del agua) y OA 10 (estados del agua)."""
from __future__ import annotations

from student_lessons import arith, ex, register

OA9, OA10 = "CN02 OA 09", "CN02 OA 10"


def task(statement, example, criteria, evidence, errors, feedback):
    return {"statement": statement, "example": example, "criteria": criteria, "evidence": evidence, "errors": errors, "feedback": feedback}


# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Un vaso alto y angosto, un tazón ancho, una bandeja con borde, una toalla y agua de la llave. Trabaja siempre sobre la bandeja para no mojar el piso.",
    use="Aprenderé que el agua escurre y se adapta a la forma del recipiente. Sirve para entender por qué el agua de un vaso cambia de forma cuando la paso a un plato.",
    prior=["Sé nombrar recipientes como vaso, botella y tazón.", "Sé que una medida en mL dice cuánta agua hay."],
    explain=[
        "El agua escurre: cuando la vierto o cae sobre algo inclinado, baja hacia el lado más bajo y sigue corriendo. Por eso la lluvia que cae en un techo inclinado termina en el suelo y no se queda arriba.",
        "El agua no tiene forma propia. Si está en un vaso, toma la forma del vaso. Si la paso a un tazón ancho, toma la forma del tazón. Cambia su forma, pero la cantidad es la misma: 200 mL en un vaso siguen siendo 200 mL en el tazón.",
        "En un tazón ancho el agua se ve más baja porque se reparte en un espacio más grande. Verla más baja no quiere decir que haya menos agua. Para comparar cantidades debo medir, no solo mirar la altura.",
    ],
    vocab=[("escurrir", "correr hacia abajo, como el agua en una pendiente"), ("recipiente", "objeto que sirve para guardar algo, como un vaso o una botella"), ("forma", "cómo se ve el contorno de algo"), ("cantidad", "cuánto hay de algo, por ejemplo 200 mL"), ("mL", "milílitro, unidad para medir cuánta agua hay")],
    worked=[
        {"title": "Pasar agua de un vaso a un tazón", "problem": "Un vaso alto tiene 200 mL de agua. Se vierte en un tazón ancho. ¿Cuánta agua hay en el tazón y qué cambió?", "steps": ["Antes: 200 mL en un vaso alto y angosto.", "Al verter, el agua toma la forma del tazón y queda más baja y ancha.", "No se perdió agua: en el tazón sigue habiendo 200 mL.", "Cambió la forma, no la cantidad."], "answer": "200 mL; cambió la forma, no la cantidad"},
        {"title": "Agua sobre una bandeja inclinada", "problem": "Pones una bandeja con un lado levantado y dejas caer agua en el lado alto. ¿Hacia dónde va el agua?", "steps": ["Miro cuál lado está más alto y cuál más bajo.", "El agua escurre hacia abajo.", "Se junta en el lado más bajo de la bandeja."], "answer": "Hacia el lado más bajo"},
    ],
    mistakes=[
        {"wrong": "Decir «en el tazón hay menos agua porque se ve más baja».", "why": "Se compara solo la altura y no la cantidad medida.", "fix": "Mide con mL o recuerda cuánta agua pasaste: si no botaste agua, la cantidad es la misma."},
        {"wrong": "Pensar que el agua tiene una forma propia, como una gota.", "why": "Se confunde la forma de una gota suelta con la forma del agua.", "fix": "En un recipiente el agua toma la forma del recipiente; la gota es una forma que aparece cuando cae."},
    ],
    tiers={
        "recovery": [
            ex("Hay agua en un vaso redondo. ¿Qué forma toma el agua?", "La forma del vaso, redonda", "El agua se adapta al recipiente."),
            ex("Echas agua en una bandeja inclinada. ¿Hacia dónde escurre: el lado alto o el lado bajo?", "El lado bajo", "El agua siempre baja por la pendiente."),
            ex("Completa: el agua toma la ___ del recipiente donde está.", "forma", "El agua no tiene forma propia y copia la del recipiente."),
        ],
        "understand": [
            ex("¿Qué significa que el agua «escurre»?", "Que corre hacia abajo", "Escurrir es bajar y correr, como el agua en una pendiente."),
            ex("¿Por qué el agua de una botella no tiene una forma propia?", "Porque toma la forma de la botella", "Si cambio de recipiente, cambia su forma."),
            ex("Una taza tiene 150 mL de agua y la vacías en un plato hondo. ¿Cuántos mL hay en el plato?", "150 mL", "Solo cambió el recipiente, no se agregó ni se quitó agua."),
        ],
        "apply": [
            arith("Un vaso con 250 mL de agua se reparte en dos tazas iguales. ¿Cuántos mL quedan en cada taza?", "250//2", "Repartir en partes iguales es dividir.", " mL"),
            arith("Echas en una jarra el agua de tres vasos de 200 mL cada uno. ¿Cuántos mL hay en la jarra?", "3*200", "El agua no desaparece al cambiar de recipiente, así que se suma.", " mL"),
            ex("Echas agua en un frasco de base cuadrada. Mirando desde arriba, ¿qué forma tiene la superficie del agua?", "Cuadrada", "El agua se adapta a la base del frasco, que es cuadrada."),
        ],
        "reason": [
            ex("Sofía dice: «En el tazón ancho hay menos agua que en el vaso alto porque se ve más baja». Antes había 200 mL en el vaso y no se botó nada. ¿Tiene razón?", "No", "Hay 200 mL en los dos; en el tazón se ve más baja porque se reparte más ancha."),
            ex("La botella A es alta y angosta y la botella B es baja y ancha. Las dos tienen 500 mL de agua. ¿Cuál tiene más agua?", "Ninguna; tienen la misma cantidad", "Las dos tienen 500 mL, aunque el agua se vea distinta."),
        ],
        "challenge": [
            ex("Un balde tiene un agujero en el fondo. Lo llenas de agua. ¿Qué pasa y por qué?", "El agua escurre por el agujero", "El agua baja y sale por la parte baja del balde."),
            ex("Explica por qué la lluvia que cae en un cerro llega abajo, al río.", "Porque el agua escurre hacia abajo por la pendiente", "La pendiente hace que el agua corra desde lo alto hacia lo bajo."),
        ],
    },
    context=[ex("El techo de la casa de Pablo es inclinado y está lloviendo. ¿Hacia dónde escurre el agua del techo y por qué se pone un canal en el borde bajo?", "Hacia abajo; el canal recoge el agua en el borde bajo", "El agua escurre por la pendiente y llega al borde bajo, donde el canal la junta.")],
    selfcheck=[
        ex("¿El agua tiene forma propia?", "No", "Toma la forma del recipiente."),
        ex("Si paso 100 mL de un vaso a un plato, ¿cambia la cantidad de agua?", "No", "Sigue habiendo 100 mL; solo cambia la forma."),
        ex("¿Hacia dónde escurre el agua en una pendiente?", "Hacia abajo", "La pendiente baja y el agua corre hacia el punto más bajo."),
    ],
    open_task=task(
        "Con un vaso, un tazón y una bandeja, echa un vaso pequeño de agua en el vaso, luego pásala al tazón y dibuja la forma del agua en cada uno. Después inclina la bandeja y dibuja hacia dónde escurre una cucharada de agua. Si no puedes hacerlo, usa este dato: 200 mL pasan de un vaso alto a un tazón ancho; dibuja cómo se ve el agua en cada uno y escribe cuántos mL hay en el tazón.",
        "En el vaso el agua es alta y angosta. En el tazón es baja y ancha, pero sigue habiendo 200 mL. En la bandeja inclinada el agua baja hacia el lado bajo.",
        ["dibuja la forma del agua en cada recipiente", "indica que la cantidad no cambió", "señala que el agua escurre hacia el lado bajo"],
        ["dibujos con rotulación", "frase con la conclusión", "registro de lo observado"],
        ["decir que hay menos agua porque se ve más baja", "dibujar el agua con forma propia fuera del recipiente"],
        "Reconoce lo que observó bien y pide que explique por qué el agua se ve más baja en el tazón; guía a que use la palabra «cantidad».",
    ),
    reinforce="Pasa agua entre un vaso y un tazón y repite en voz alta: «cambió la forma, no la cantidad». Dibuja cada paso.",
    extend="Pregunta en casa dónde ves agua que escurre (techos, calles con pendiente, la ducha) y haz una lista de tres lugares.",
)

register(
    OA9, 2,
    materials="Un vaso transparente con agua, un vaso con leche, una moneda, una hoja con una palabra escrita grande, un vaso con agua y un poco de tierra. Sin probar ninguna sustancia.",
    use="Aprenderé que el agua limpia es transparente e inodora. Sirve para reconocer si el agua está limpia sin necesidad de probarla.",
    prior=["Sé que observar es mirar con atención.", "Sé que no se debe probar ni beber líquidos desconocidos."],
    explain=[
        "El agua limpia es transparente: la luz pasa a través de ella y puedo ver lo que hay detrás. Si pongo una moneda al fondo de un vaso con agua limpia, la veo claramente.",
        "El agua limpia también es inodora: no tiene olor. Para oler algo de forma segura, no pongo la nariz pegada. Muevo el aire hacia mí con la mano. Nunca pruebo un líquido para saber qué es.",
        "No todos los líquidos son como el agua. La leche no es transparente: no puedo ver la moneda a través de ella. El agua con tierra se ve turbia. Si el agua huele raro o se ve turbia, no la tomo y aviso a un adulto. Ojo: que el agua se vea transparente no siempre quiere decir que sea segura para tomar; ante la duda, pregunto a un adulto.",
    ],
    vocab=[("transparente", "que deja ver lo que hay detrás"), ("inodora", "que no tiene olor"), ("turbia", "agua que se ve nublada o sucia"), ("observar", "mirar con atención y anotar lo que veo"), ("opaco", "que no deja ver lo que hay detrás")],
    worked=[
        {"title": "La moneda en el vaso", "problem": "Pones una moneda en el fondo de un vaso con agua limpia y miras desde arriba. Otro vaso tiene leche y también tiene una moneda. ¿En cuál se ve la moneda?", "steps": ["Miro el vaso con agua: veo la moneda.", "Miro el vaso con leche: no veo la moneda.", "Si veo lo que hay detrás, el líquido es transparente."], "answer": "Se ve en el vaso con agua; el agua es transparente y la leche no"},
        {"title": "Oler con seguridad", "problem": "Quieres saber si el agua tiene olor. ¿Cómo lo haces sin riesgo?", "steps": ["Dejo el vaso a un brazo de distancia.", "Con la mano muevo el aire desde el vaso hacia mi nariz.", "No pruebo el agua para saber cómo es."], "answer": "Muevo el aire con la mano y no pruebo el líquido"},
    ],
    mistakes=[
        {"wrong": "Probar un líquido para saber si es agua.", "why": "Se piensa que probar es la mejor forma de identificar algo.", "fix": "Identifica con los ojos y con la nariz, de forma segura. Un líquido desconocido puede hacer daño."},
        {"wrong": "Decir que la leche es transparente porque es líquida.", "why": "Se confunde ser líquido con ser transparente.", "fix": "Pon un objeto detrás: si no lo ves bien, no es transparente."},
    ],
    tiers={
        "recovery": [
            ex("Pones una moneda al fondo de un vaso con agua limpia. ¿Se ve la moneda?", "Sí", "El agua limpia deja pasar la luz y es transparente."),
            ex("Completa: el agua limpia no tiene olor, es ___.", "inodora", "Inodora significa que no huele."),
            ex("Un vaso tiene agua con tierra. ¿Se ve transparente o turbia?", "Turbia", "La tierra hace que se vea nublada."),
        ],
        "understand": [
            ex("¿Qué quiere decir que el agua es transparente?", "Que deja ver lo que hay detrás", "Transparente es lo que deja pasar la luz y permite ver."),
            ex("¿Por qué no se debe probar un líquido para saber si es agua?", "Porque puede ser peligroso", "Un líquido desconocido puede enfermar o dañar."),
            ex("¿Cómo se huele un líquido de forma segura?", "Moviendo el aire hacia la nariz con la mano", "Así evito aspirar fuerte algo que pueda ser dañino."),
        ],
        "apply": [
            ex("Hay tres vasos: A tiene agua limpia, B tiene leche y C tiene agua con tierra. Detrás de cada uno hay una palabra escrita. ¿En cuál se lee la palabra con más claridad?", "En el vaso A", "El agua limpia es transparente; la leche no deja ver y la tierra la pone turbia."),
            ex("Un vaso con jugo de color rojo oscuro no deja ver la moneda del fondo. ¿Es transparente?", "No", "Si no veo bien lo que hay detrás, no es transparente."),
            ex("Mueves con la mano el aire de un vaso con agua limpia hacia tu nariz y no sientes ningún olor. ¿Qué anotas en tu tabla: «con olor» o «sin olor»?", "Sin olor", "El agua limpia es inodora."),
        ],
        "reason": [
            ex("Mateo dice: «Este líquido es agua porque es líquido». ¿Por qué esa razón no alcanza?", "Porque hay otros líquidos, como la leche, que no son agua", "Ser líquido no prueba que sea agua; hay que observar transparencia y olor."),
            ex("Dos vasos parecen agua. En uno se ve la moneda del fondo y en el otro no. ¿Cuál tiene más posibilidades de ser agua limpia y por qué?", "El que deja ver la moneda, porque es transparente", "El agua limpia es transparente; el otro líquido puede ser leche o agua sucia."),
        ],
        "challenge": [
            ex("Una amiga te ofrece un vaso con un líquido sin etiqueta. Tiene mal olor y se ve turbio. ¿Qué haces?", "No lo tomo y aviso a un adulto", "Mal olor y turbiedad son señales de que no es seguro."),
            ex("Ayer el agua del vaso era transparente. Hoy se ve turbia. Nombra una cosa que pudo pasarle.", "Que se mezcló algo con ella, como tierra o polvo", "Algo mezclado con el agua la hizo verse nublada."),
        ],
    },
    context=[ex("En un campamento, Camila ve que el agua de una poza es verde y turbia y huele raro. Su papá tiene agua embotellada. ¿Qué agua es más segura de tomar y por qué?", "La embotellada, porque la de la poza está turbia y huele raro", "El agua turbia y con olor no es limpia; la embotellada es transparente y sin olor.")],
    selfcheck=[
        ex("¿El agua limpia es transparente o turbia?", "Transparente", "Deja ver lo que hay detrás."),
        ex("¿El agua limpia tiene olor?", "No", "Es una sustancia inodora."),
        ex("¿Se puede probar un líquido desconocido para saber qué es?", "No", "Puede ser peligroso; se identifica mirando y oliendo con cuidado."),
    ],
    open_task=task(
        "Mira esta tabla. Vaso 1: agua limpia, se ve la moneda, sin olor. Vaso 2: leche, no se ve la moneda, olor suave. Vaso 3: agua con tierra, se ve la moneda apenas, sin olor. Copia la tabla y marca con una cruz qué vasos son transparentes y cuál es agua limpia. Escribe una frase: «Sé que el vaso __ tiene agua limpia porque __».",
        "Es transparente solo el vaso 1. Sé que el vaso 1 tiene agua limpia porque se ve la moneda y no tiene olor.",
        ["marca como transparente solo el vaso 1", "cita la moneda y el olor como evidencia", "no propone probar los líquidos"],
        ["tabla copiada y marcada", "frase completa con la conclusión", "dibujo de los tres vasos"],
        ["decidir probando el líquido", "usar solo la idea de que es líquido para decidir"],
        "Felicita el uso de evidencias y pide que explique con qué dato descartó los vasos 2 y 3.",
    ),
    reinforce="Mira a través de un vaso con agua limpia un objeto pequeño y luego a través de un vaso con agua con un poco de tierra. Dibuja la diferencia.",
    extend="Haz una lista de tres líquidos que conozcas y marca cuáles son transparentes y cuáles no, usando tus ojos y sin probarlos.",
)

register(
    OA9, 3,
    materials="Tres vasos transparentes con 200 mL de agua tibia (no caliente) cada uno, una cucharadita de sal, una cucharadita de azúcar, una cucharadita de arena, tres cucharas. No probar ninguna mezcla.",
    use="Aprenderé que el agua disuelve algunos sólidos, como la sal y el azúcar, pero no otros, como la arena. Sirve para entender qué pasa cuando se prepara una mezcla con agua.",
    prior=["Sé que el agua es transparente.", "Sé que revolver es mover con una cuchara."],
    explain=[
        "Disolver es cuando un sólido se mezcla tan bien con el agua que ya no se ven los granitos. La sal y el azúcar se disuelven en agua. Si revuelvo, el agua queda transparente otra vez.",
        "Disolverse no es desaparecer. La sal y el azúcar siguen estando en el agua, solo que en trocitos tan pequeños que no los veo. Por eso el agua con sal no pesa lo mismo que el agua sola: pesa lo de la sal y el agua juntas.",
        "No todos los sólidos se disuelven. La arena no se disuelve: se queda en el fondo y se sigue viendo. El agua tibia y revolver ayudan a que el sólido se disuelva más rápido. Para saber si algo se disolvió, no pruebo la mezcla. Miro si se ven los granitos y si el agua se ve transparente.",
    ],
    vocab=[("disolver", "mezclar un sólido con agua hasta que ya no se ven sus granos"), ("sólido", "algo duro o en granos que tiene forma propia, como la sal"), ("mezcla", "dos o más cosas juntas"), ("revolver", "mover con una cuchara para mezclar"), ("granos", "partes pequeñas de un sólido, como la sal o la arena")],
    worked=[
        {"title": "Sal en el agua", "problem": "Echas una cucharadita de sal en un vaso con agua, revuelves y esperas. Los granitos ya no se ven y el agua se ve transparente. ¿Qué pasó con la sal?", "steps": ["Miro: no se ven los granos y el agua es transparente.", "La sal se disolvió.", "No desapareció: sigue en el agua en trozos muy pequeños."], "answer": "Se disolvió; sigue estando en el agua"},
        {"title": "Arena en el agua", "problem": "Echas una cucharadita de arena en otro vaso y revuelves. Después de un rato, la arena está en el fondo y se ve. ¿Se disolvió?", "steps": ["Miro el fondo del vaso: la arena se ve.", "Los granos siguen visibles.", "Un sólido que se sigue viendo no se disolvió."], "answer": "No, la arena no se disuelve en agua"},
    ],
    mistakes=[
        {"wrong": "Decir que la sal desapareció porque ya no se ve.", "why": "Se piensa que lo que no se ve ya no existe.", "fix": "La sal está disuelta en el agua. Se puede comprobar porque 200 g de agua más 10 g de sal pesan 210 g."},
        {"wrong": "Probar la mezcla para saber si hay sal.", "why": "Se cree que probar es la forma de comprobar.", "fix": "Comprueba con evidencias seguras, como pesar la mezcla o dejar evaporar el agua (con ayuda de un adulto)."},
    ],
    tiers={
        "recovery": [
            ex("La sal se mezcla con el agua y ya no se ven los granitos. ¿Se disolvió o no se disolvió?", "Se disolvió", "Disolver es que no se vean los granos."),
            ex("La arena queda en el fondo del vaso y se ve. ¿Se disolvió?", "No", "Un sólido que se sigue viendo no se disolvió."),
            ex("Completa: el azúcar se ___ en el agua.", "disuelve", "El azúcar es un sólido que se disuelve en agua."),
        ],
        "understand": [
            ex("¿Qué significa «disolver»?", "Mezclar un sólido con agua hasta que ya no se ven sus granos", "Es la definición de disolver."),
            ex("Después de disolver sal en el agua, ¿la sal sigue estando en la mezcla o desapareció?", "Sigue estando", "Está en trozos tan pequeños que no se ven."),
            ex("¿Por qué no se debe probar una mezcla para saber qué tiene?", "Porque puede ser peligroso", "Probar sustancias desconocidas puede dañar."),
        ],
        "apply": [
            arith("Un vaso con 200 g de agua recibe 10 g de sal que se disuelve. ¿Cuántos gramos pesa la mezcla?", "200+10", "La sal disuelta sigue pesando y se suma al agua.", " g"),
            ex("Tienes tres sólidos: sal, azúcar y arena. ¿Cuál no se disuelve en agua?", "La arena", "La sal y el azúcar se disuelven; la arena no."),
            ex("Un vaso con agua tiene azúcar disuelta. Dejas el vaso y no se ve ningún grano. ¿El agua se ve transparente o turbia?", "Transparente", "Al disolverse bien, no hay granos que la enturbien."),
        ],
        "reason": [
            ex("Valentina dice: «La sal desapareció porque ya no la veo». Una balanza muestra que 200 g de agua más 5 g de sal pesan 205 g. ¿Quién tiene razón?", "No tiene razón; la sal sigue ahí", "Si desapareciera, pesaría 200 g; pesa 205 g, así que la sal sigue en la mezcla."),
            ex("Dos amigos revuelven. En el vaso A los granos desaparecen y en el B quedan en el fondo. ¿Cuál es arena y cuál puede ser azúcar?", "A puede ser azúcar y B es arena", "El azúcar se disuelve y la arena no."),
        ],
        "challenge": [
            ex("Un vaso con agua tibia disuelve el azúcar más rápido que uno con agua fría. ¿Qué dos cosas ayudan a disolver más rápido?", "Agua tibia y revolver", "Más calor y mover la mezcla ayudan a que el sólido se disuelva más rápido."),
            ex("Camilo mezcla piedritas con agua y revuelve mucho. ¿Se disolverán? Explica.", "No", "Las piedritas no se disuelven; seguirán viéndose en el fondo."),
        ],
    },
    context=[ex("En casa preparas un jugo en polvo: echas el polvo en una jarra con agua y revuelves hasta que no se ven granitos. ¿Qué le pasó al polvo y dónde está ahora?", "Se disolvió y está en el agua", "Disuelto significa que está mezclado en el agua, aunque no se vean los granos.")],
    selfcheck=[
        ex("¿La sal se disuelve en agua?", "Sí", "La sal es un sólido que se disuelve."),
        ex("¿Qué sólido de esta lista no se disuelve: sal, arena, azúcar?", "Arena", "Se sigue viendo en el fondo."),
        ex("Si un sólido se disuelve, ¿desaparece del todo?", "No", "Sigue estando en el agua en partes muy pequeñas."),
    ],
    open_task=task(
        "Con tres vasos de agua tibia, prueba con una cucharadita de sal, una de azúcar y una de arena. Revuelve y copia esta tabla: «Sólido / ¿Se ven los granos? / ¿Se disolvió?». Completa tus observaciones sin probar nada. Si no puedes hacerlo, usa esta información: sal, no se ven granos; azúcar, no se ven granos; arena, se ven granos en el fondo.",
        "Sal: no se ven los granos, se disolvió. Azúcar: no se ven los granos, se disolvió. Arena: se ven granos en el fondo, no se disolvió. La sal y el azúcar no desaparecieron, están en el agua.",
        ["completa la tabla con observaciones", "clasifica correctamente cada sólido", "aclara que lo disuelto sigue en el agua"],
        ["tabla completa", "dibujo de los tres vasos", "frase de conclusión"],
        ["decir que lo disuelto desapareció", "probar las mezclas"],
        "Valora que no probó las mezclas y pregunta cómo podría comprobar que la sal sigue en el agua.",
    ),
    reinforce="Revuelve azúcar en agua tibia y en agua fría y mide cuánto tarda en ya no verse en cada caso.",
    extend="Averigua en casa un sólido más y comprueba, sin probarlo, si se disuelve o no en agua; anótalo en una tabla.",
)

register(
    OA9, 4,
    materials="Dos platos iguales, una taza de medir o cuchara, agua de la llave, una cucharadita de sal, un lugar con sol y otro con sombra. Este cuaderno trae los datos del registro por si no puedes hacerlo.",
    use="Aprenderé que el agua se evapora: se va al aire como vapor de agua, más rápido con calor. Sirve para entender por qué se seca la ropa y por qué desaparecen los charcos.",
    prior=["Sé que el agua escurre y se disuelve.", "Sé leer una tabla de datos con números."],
    explain=[
        "Evaporarse es cuando el agua líquida pasa al aire como vapor de agua. El vapor de agua es invisible. Por eso un charco desaparece poco a poco aunque nadie lo recoja.",
        "El agua se evapora más rápido cuando hace calor, cuando hay viento y cuando está en un lugar ancho, como un plato. Si dejo dos platos con la misma cantidad de agua, uno al sol y otro a la sombra, el del sol queda seco antes.",
        "Cuando se evapora agua con sal, el agua se va al aire pero la sal se queda. Eso muestra que la sal no desapareció al disolverse. Ten cuidado: no pruebes lo que queda en el plato.",
    ],
    vocab=[("evaporarse", "pasar el agua líquida al aire como vapor de agua"), ("vapor de agua", "agua en forma de gas, invisible"), ("temperatura", "qué tan caliente o frío está algo"), ("viento", "aire que se mueve"), ("registro", "tabla donde anoto lo que observo")],
    worked=[
        {"title": "Dos platos con 50 mL", "problem": "Dos platos tienen 50 mL de agua. Al sol quedan 30 mL después de 1 día y a la sombra quedan 45 mL. ¿En cuál se evaporó más agua?", "steps": ["Al sol: 50 − 30 = 20 mL evaporados.", "A la sombra: 50 − 45 = 5 mL evaporados.", "20 es mayor que 5."], "answer": "Al sol; se evaporaron 20 mL contra 5 mL"},
        {"title": "Agua con sal", "problem": "Dejas que se evapore toda el agua de un plato con agua salada y queda un polvo blanco. ¿Qué es ese polvo?", "steps": ["El agua se fue al aire como vapor invisible.", "La sal no se evapora.", "Quedó en el plato."], "answer": "Es la sal; el agua se evaporó y la sal se quedó"},
    ],
    mistakes=[
        {"wrong": "Decir que el charco desapareció porque el suelo se lo tomó entero.", "why": "No se considera que el agua pasa al aire.", "fix": "Parte del agua se evapora y sube al aire como vapor invisible, sobre todo con sol y viento."},
        {"wrong": "Creer que la sal también se evapora con el agua.", "why": "Se piensa que todo lo disuelto se va con el agua.", "fix": "Solo el agua se evapora; la sal se queda en el plato."},
    ],
    tiers={
        "recovery": [
            ex("Un charco desaparece después de un día de sol. ¿A dónde fue el agua?", "Al aire, como vapor de agua", "El agua se evaporó."),
            ex("Completa: el agua que pasa al aire como vapor se ___.", "evapora", "Evaporarse es pasar al aire como vapor."),
            ex("¿El vapor de agua se ve o es invisible?", "Es invisible", "El vapor de agua es un gas que no se ve."),
        ],
        "understand": [
            ex("¿Qué significa «evaporarse»?", "Pasar el agua líquida al aire como vapor", "Esa es la definición de evaporarse."),
            ex("¿Por qué la ropa mojada se seca más rápido al sol?", "Porque con calor el agua se evapora más rápido", "El calor ayuda a que el agua pase al aire."),
            ex("¿Qué dos cosas ayudan a que el agua se evapore más rápido?", "El calor y el viento", "Los dos hacen que el agua pase al aire con mayor rapidez."),
        ],
        "apply": [
            arith("Un plato tiene 60 mL de agua. Al final del día quedan 35 mL. ¿Cuántos mL se evaporaron?", "60-35", "Lo evaporado es lo que había menos lo que queda.", " mL"),
            arith("Un plato pierde 10 mL de agua por día. ¿Cuántos mL perdió después de 4 días?", "10*4", "Cada día se evaporan 10 mL, por eso se multiplica por 4.", " mL"),
            ex("Lavas un trapo y lo cuelgas en el patio con sol y viento. Otro igual lo cuelgas en el baño cerrado. ¿Cuál se seca primero?", "El del patio", "El sol y el viento ayudan a evaporar el agua."),
        ],
        "reason": [
            ex("Dos platos con 50 mL: el A al sol queda con 20 mL y el B a la sombra queda con 40 mL. Tomás dice que en el B no se evaporó nada. ¿Es cierto?", "No; se evaporaron 10 mL", "50 − 40 = 10 mL se evaporaron, pero menos que en A, donde fueron 30 mL."),
            ex("Se evapora toda el agua de un plato con agua salada y queda un polvo blanco. Ana dice que la sal desapareció con el agua. ¿Qué evidencia la contradice?", "Que quedó el polvo blanco, que es sal", "La sal no se evapora y queda en el plato."),
        ],
        "challenge": [
            ex("Quieres que se seque rápido un charco pequeño en el patio. Nombra dos condiciones del día que ayudan.", "Sol y viento", "Calor y viento aceleran la evaporación."),
            ex("Tienes un vaso angosto y un plato ancho con 100 mL cada uno al sol. ¿En cuál se evaporará el agua más rápido y por qué?", "En el plato ancho, porque tiene más superficie al aire", "Una superficie ancha deja salir más vapor al aire."),
        ],
    },
    context=[ex("Después de lavar los platos quedan gotas de agua. Si los dejas al aire, a las pocas horas están secos. ¿Qué pasó con esas gotas?", "Se evaporaron", "Las gotas pasaron al aire como vapor de agua invisible.")],
    selfcheck=[
        ex("¿Dónde queda el agua cuando se evapora?", "En el aire", "Como vapor de agua invisible."),
        ex("¿Qué se queda en el plato cuando se evapora agua con sal?", "La sal", "Solo el agua se evapora."),
        ex("¿Se evapora más rápido el agua al sol o a la sombra?", "Al sol", "El calor ayuda a evaporar."),
    ],
    open_task=task(
        "Observa este registro: dos platos con 50 mL de agua, uno al sol y otro a la sombra. Día 1, sol: 40 mL; sombra: 47 mL. Día 2, sol: 30 mL; sombra: 44 mL. Dibuja una tabla con esos datos, calcula cuánto se evaporó en cada plato en dos días y escribe cuál se evaporó más y por qué.",
        "Sol: 50 − 30 = 20 mL. Sombra: 50 − 44 = 6 mL. En el sol se evaporó más porque hay más calor.",
        ["calcula 20 mL y 6 mL", "compara y dice que en el sol se evaporó más", "explica con la idea de calor"],
        ["tabla dibujada", "cálculos escritos", "frase con la explicación"],
        ["restar al revés", "decir que no se evaporó nada en la sombra"],
        "Valora la comparación con números y pide que explique de dónde viene la diferencia entre sol y sombra.",
    ),
    reinforce="Dibuja un charco al sol en tres momentos: por la mañana, al mediodía y en la tarde, mostrando que cada vez es más pequeño.",
    extend="Con ayuda de un adulto, compara cuánto tarda en secarse una toalla de papel mojada dentro de la casa y afuera.",
)

register(
    OA9, 5,
    materials="Una bandeja de cubos de hielo, agua, un vaso de plástico (el vidrio puede quebrarse en el congelador), una marca hecha con cinta en el vaso, un congelador de la casa. Usa el congelador solo con un adulto.",
    use="Aprenderé que el agua se congela con frío y se derrite con calor, y que vuelve a ser la misma agua. Sirve para entender qué pasa con los cubos de hielo y con las heladas.",
    prior=["Sé que el agua se evapora con el calor.", "Sé leer temperaturas en grados Celsius (°C)."],
    explain=[
        "El agua se congela cuando está muy fría: a 0 °C o menos, pasa de líquida a hielo. Las temperaturas bajo cero se escriben con un signo menos: −5 °C se lee «cinco grados bajo cero». El hielo es agua sólida. Si el hielo se calienta sobre 0 °C, se derrite y vuelve a ser agua líquida.",
        "Es la misma agua. Cuando el hielo se derrite, el agua que sale es la misma que se congeló. Lo que cambia es la temperatura y la forma en que se ve el agua: líquida o sólida.",
        "Cuando el agua se congela ocupa un poco más de espacio. Por eso, si lleno un vaso hasta el borde y lo congelo, el hielo sube y se sale. Al congelar agua en un recipiente hay que dejar un espacio. El frío no se convierte en agua: el hielo se derrite porque recibe calor.",
    ],
    vocab=[("congelar", "pasar el agua líquida a hielo por el frío"), ("derretir", "pasar el hielo a agua líquida por el calor"), ("0 °C", "temperatura en que el agua se congela"), ("hielo", "agua en estado sólido"), ("grado Celsius", "unidad para medir la temperatura, se escribe °C")],
    worked=[
        {"title": "Agua en el congelador", "problem": "Un vaso con agua se pone en un congelador a −10 °C. ¿Qué le pasa al agua y por qué?", "steps": ["−10 °C es menos que 0 °C.", "El agua se enfría hasta congelarse.", "Pasa de líquida a hielo."], "answer": "Se congela y queda como hielo"},
        {"title": "Hielo sobre la mesa", "problem": "Un cubo de hielo está en la mesa de una pieza a 20 °C. ¿Qué le pasa?", "steps": ["20 °C es más que 0 °C.", "El hielo recibe calor del aire.", "Se derrite y pasa a agua líquida."], "answer": "Se derrite y queda agua líquida"},
    ],
    mistakes=[
        {"wrong": "Decir que el hielo se derrite porque «el frío se convierte en agua».", "why": "Se cree que el frío es una cosa que se transforma.", "fix": "El hielo se derrite porque recibe calor, y sigue siendo el mismo tipo de agua."},
        {"wrong": "Llenar un vaso hasta el borde antes de congelarlo.", "why": "No se sabe que el hielo ocupa un poco más de espacio.", "fix": "Deja un espacio libre en el recipiente antes de congelar."},
    ],
    tiers={
        "recovery": [
            ex("El agua baja a −5 °C. ¿Se congela o sigue líquida?", "Se congela", "Con 0 °C o menos el agua se congela."),
            ex("Un cubo de hielo recibe calor. ¿Se derrite o se congela más?", "Se derrite", "El calor derrite el hielo."),
            ex("Completa: el hielo es agua en estado ___.", "sólido", "El hielo es agua sólida."),
        ],
        "understand": [
            ex("¿A qué temperatura se congela el agua?", "A 0 °C", "El punto de congelación del agua es 0 °C."),
            ex("Cuando el hielo se derrite, ¿es una sustancia nueva o la misma agua?", "La misma agua", "Solo cambia el estado de líquida a sólida y viceversa."),
            ex("¿Por qué conviene dejar un espacio al congelar agua en un recipiente?", "Porque el hielo ocupa más espacio", "Al congelarse, el agua aumenta un poco de volumen."),
        ],
        "apply": [
            ex("Un vaso con agua está a 4 °C. ¿Está congelada?", "No", "4 °C es más que 0 °C."),
            ex("En una pieza a −3 °C se deja un charco de agua. ¿Qué pasa con el charco?", "Se congela", "−3 °C es menos que 0 °C."),
            arith("Una bandeja tiene 12 cubos de hielo y se derriten 5. ¿Cuántos cubos quedan sin derretir?", "12-5", "Se resta lo que se derritió de lo que había.", " cubos"),
        ],
        "reason": [
            ex("Pedro dice: «El hielo se derrite porque el frío se convierte en agua». ¿Qué le explicas?", "Que se derrite porque recibe calor", "El frío no se transforma; el calor cambia el hielo a agua."),
            ex("En un congelador a −8 °C hay un vaso con agua lleno hasta el borde. Después sale hielo por arriba. ¿Por qué ocurrió?", "Porque el hielo ocupa más espacio que el agua", "Al congelarse, el agua aumenta de volumen y sube."),
        ],
        "challenge": [
            ex("Un cubo de hielo se derrite en un vaso y el agua se pone en el congelador otra vez. ¿Puede volver a ser hielo?", "Sí", "Es la misma agua y se congela de nuevo con frío."),
            ex("Hoy la mañana está a −2 °C y el charco de la calle tiene una capa dura. A mediodía hay 10 °C. ¿Qué le pasa a la capa?", "Se derrite", "Con 10 °C, el hielo recibe calor y vuelve a agua líquida."),
        ],
    },
    context=[ex("Una noche la temperatura del patio baja a −1 °C y en la mañana el agua del balde tiene una capa de hielo. A mediodía el patio está a 12 °C. ¿Qué espera encontrar Lucía a mediodía?", "Que el hielo se derritió", "A 12 °C el hielo recibe calor y pasa a agua líquida.")],
    selfcheck=[
        ex("¿Se congela el agua a 6 °C?", "No", "Solo se congela a 0 °C o menos."),
        ex("¿Qué hace derretirse al hielo?", "El calor", "Al recibir calor, el hielo pasa a líquido."),
        ex("Al derretirse un cubo de hielo, ¿se obtiene la misma agua?", "Sí", "Solo cambió su estado."),
    ],
    open_task=task(
        "Con un adulto, llena hasta tres cuartos un vaso con agua, marca el nivel con cinta y ponlo en el congelador. Al día siguiente dibuja cómo quedó. Después déjalo en la mesa y dibuja qué pasa. Si no puedes, usa estos datos: nivel marcado a 10 cm; congelado llega a 11 cm; derretido vuelve a 10 cm. Escribe qué cambió y qué se conservó.",
        "El agua líquida se congeló y el hielo llegó un poco más alto (11 cm). Al derretirse volvió a 10 cm. Cambió el estado y el espacio que ocupaba; sigue siendo la misma agua.",
        ["describe el congelamiento y la fusión", "nota que el hielo ocupa algo más de espacio", "dice que sigue siendo la misma agua"],
        ["dibujos del antes y después", "registro de alturas", "frase de conclusión"],
        ["decir que el hielo es otra sustancia", "no dejar espacio al congelar"],
        "Reconoce la precisión de las observaciones y pide que explique por qué el hielo subió un poco.",
    ),
    reinforce="Dibuja una secuencia de cuatro cuadros: agua líquida, congelador, hielo, hielo derritiéndose.",
    extend="Pregunta en tu familia si alguna vez una botella llena se rompió en el congelador y explica por qué pudo pasar.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Un cubo de hielo, un plato, una bandeja de cubitos y un vaso con agua. Si no tienes hielo, usa las descripciones de este cuaderno.",
    use="Aprenderé a reconocer el agua sólida y sus características. Sirve para saber qué es el hielo, la escarcha y el granizo.",
    prior=["Sé que el agua se congela a 0 °C.", "Sé comparar forma y tamaño de objetos."],
    explain=[
        "El agua puede estar en tres estados: sólido, líquido y gaseoso. El hielo es el agua en estado sólido. Un cubo de hielo tiene forma propia: si lo paso de un plato a un vaso, sigue siendo cubo.",
        "El agua sólida también aparece en la naturaleza como nieve, escarcha y granizo. El granizo son bolitas de hielo que caen en una tormenta. La escarcha es una capa fina de hielo sobre el pasto o los autos en una mañana muy fría. La nieve cae en copos blancos.",
        "El hielo es duro y frío al tocarlo, y se derrite cuando recibe calor. No se derrite por el frío. El hielo se derrite porque sube su temperatura sobre 0 °C. Cuando se derrite, deja de ser sólido y pasa a líquido.",
    ],
    vocab=[("sólido", "estado en que algo tiene forma propia, como el hielo"), ("hielo", "agua en estado sólido"), ("granizo", "bolitas de hielo que caen en una tormenta"), ("escarcha", "capa fina de hielo sobre superficies en mañanas muy frías"), ("estado", "forma en que está la materia: sólido, líquido o gaseoso")],
    worked=[
        {"title": "Un cubo de hielo cambia de recipiente", "problem": "Pasas un cubo de hielo de un plato plano a un vaso. ¿Cambia su forma?", "steps": ["Miro el cubo en el plato: tiene forma de cubo.", "Lo paso al vaso y vuelvo a mirar.", "Sigue siendo cubo porque es sólido."], "answer": "No cambia su forma; los sólidos tienen forma propia"},
        {"title": "Reconocer agua sólida", "problem": "Una mañana muy fría el pasto está cubierto por una capa blanca que cruje al pisarla. ¿Qué es?", "steps": ["Es blanca y dura, y cruje.", "Aparece cuando hace mucho frío.", "Es agua congelada sobre el pasto."], "answer": "Es escarcha, agua en estado sólido"},
    ],
    mistakes=[
        {"wrong": "Decir que el hielo se derrite «porque el frío se vuelve agua».", "why": "Se cree que el frío es una cosa que se transforma.", "fix": "El hielo se derrite porque recibe calor y su temperatura sube sobre 0 °C."},
        {"wrong": "Pensar que el hielo es otra sustancia distinta del agua.", "why": "Se compara solo la apariencia.", "fix": "El hielo es agua en estado sólido; si se derrite, vuelve a ser la misma agua."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama el agua en estado sólido?", "Hielo", "El hielo es agua sólida."),
            ex("Un cubo de hielo cambia de un plato a un vaso. ¿Conserva su forma?", "Sí", "Un sólido tiene forma propia."),
            ex("Completa: el granizo son bolitas de ___.", "hielo", "El granizo es agua sólida que cae en una tormenta."),
        ],
        "understand": [
            ex("¿Qué quiere decir que un sólido tiene forma propia?", "Que no cambia de forma al cambiarlo de recipiente", "Un sólido conserva su forma sin importar dónde esté."),
            ex("¿Qué diferencia hay entre escarcha y nieve?", "La escarcha es una capa fina sobre las cosas; la nieve cae en copos", "Las dos son agua sólida, pero se forman de manera distinta."),
            ex("¿El hielo y el agua líquida son la misma sustancia?", "Sí", "El hielo es agua en estado sólido."),
        ],
        "apply": [
            ex("Pones un cubo de hielo de 3 cm de lado dentro de una caja grande y redonda. ¿Qué forma tiene el hielo dentro de la caja: la de la caja o la de cubo?", "La de cubo", "Los sólidos mantienen su forma propia."),
            ex("En un registro de temperatura hay: lunes 5 °C, martes 2 °C, miércoles −2 °C, jueves 3 °C. ¿Qué día puede haber escarcha o hielo?", "El miércoles", "Solo el miércoles baja de 0 °C, y ahí el agua puede congelarse."),
            ex("Sacas un cubo de hielo del congelador y lo dejas al sol. Describe en una palabra su forma después de 1 hora.", "Derretido", "Con calor el hielo pasa a líquido."),
        ],
        "reason": [
            ex("Rocío dice que el hielo es una piedra porque es duro y frío. ¿Qué evidencia dice que sí es agua?", "Que al derretirse se convierte en agua líquida", "Una piedra no se derrite; el hielo sí y se vuelve agua."),
            ex("Joaquín dice que el hielo se derritió porque hacía mucho frío. ¿Por qué el razonamiento está equivocado?", "Porque se derrite con calor", "Para derretirse el hielo necesita calor, no frío."),
        ],
        "challenge": [
            ex("Tienes hielo, agua y piedra. Todos son sólidos o líquidos. Nombra cuáles son sólidos.", "El hielo y la piedra", "El agua líquida no tiene forma propia."),
            ex("Una botella de plástico llena de agua se pone en un congelador. Explica qué estado tendrá el agua al día siguiente y por qué conviene dejar espacio.", "Sólido; el hielo ocupa más espacio", "El agua se congela y aumenta de volumen."),
        ],
    },
    context=[ex("En el sur de Chile, Sebastián ve por la ventana bolitas blancas y duras que rebotan en el suelo durante una tormenta. ¿Qué son y en qué estado está el agua?", "Granizo; agua en estado sólido", "El granizo son bolitas de hielo, es decir, agua sólida.")],
    selfcheck=[
        ex("¿En qué estado está el hielo?", "Sólido", "El hielo es agua sólida."),
        ex("¿El hielo se derrite con frío o con calor?", "Con calor", "El calor sube su temperatura sobre 0 °C."),
        ex("¿Un sólido cambia de forma si lo paso de un recipiente a otro?", "No", "Tiene forma propia."),
    ],
    open_task=task(
        "Observa un cubo de hielo (o imagina el de la descripción: 3 cm de lado, duro, transparente y muy frío) y haz una ficha con tres columnas: «Lo que veo», «Lo que toco con cuidado», «Lo que le pasa con calor». Escribe una frase en cada una y dibújalo.",
        "Veo: un cubo transparente. Toco: duro y frío. Con calor: se derrite y se convierte en agua líquida. Es agua en estado sólido.",
        ["describe forma y dureza", "dice que con calor se derrite", "nombra el estado sólido"],
        ["ficha con tres columnas", "dibujo del hielo", "frase de conclusión"],
        ["decir que se derrite por frío", "decir que el hielo no es agua"],
        "Valora la descripción con detalles y pide que explique por qué se derrite en la mano.",
    ),
    reinforce="Haz una lista de tres ejemplos de agua sólida que puedas ver en la naturaleza y dibuja uno.",
    extend="Explica a un familiar la diferencia entre hielo, escarcha y granizo con un dibujo.",
)

register(
    OA10, 2,
    materials="Un vaso, una botella, un plato hondo, una cuchara y agua de la llave. Un recipiente de plástico con tapa, sin usar nada caliente.",
    use="Aprenderé las características del agua líquida: fluye, toma la forma del recipiente y ocupa un lugar. Sirve para entender cómo se comporta el agua al servirla o guardarla.",
    prior=["Sé que el hielo es agua sólida.", "Sé que el agua toma la forma del recipiente."],
    explain=[
        "El agua líquida fluye: se puede verter de un recipiente a otro. No tiene forma propia, pero sí ocupa un lugar. Eso se llama volumen: 300 mL de agua ocupan el mismo lugar en un vaso que en un tazón. Un litro (1 L) son 1.000 mL.",
        "Un líquido se adapta al recipiente. Si lo guardo en una botella, toma la forma de la botella. Pero siempre tiene una superficie plana y horizontal hacia arriba cuando está quieto, y no se aprieta para caber en menos espacio.",
        "Para comparar estados: el hielo (sólido) tiene forma y volumen propios; el agua líquida tiene volumen propio, pero toma la forma del recipiente. Más adelante veremos el vapor, que se esparce por todo el espacio.",
    ],
    vocab=[("líquido", "estado en que algo fluye y toma la forma del recipiente"), ("fluir", "moverse y correr como el agua"), ("volumen", "el lugar que ocupa algo"), ("superficie", "parte de arriba del líquido que queda plana"), ("verter", "echar un líquido de un recipiente a otro")],
    worked=[
        {"title": "Verter y comparar", "problem": "Viertes 300 mL de agua de una botella a una jarra. ¿Qué cambia y qué se conserva?", "steps": ["El agua toma la forma de la jarra.", "El volumen se conserva: siguen siendo 300 mL.", "Cambió la forma, no la cantidad."], "answer": "Cambia la forma; se conserva el volumen de 300 mL"},
        {"title": "Líquido o sólido", "problem": "Un objeto se puede verter, toma la forma del vaso y deja una superficie plana. ¿Es sólido o líquido?", "steps": ["Se vierte y fluye.", "Toma la forma del vaso.", "Eso es propio de un líquido."], "answer": "Es un líquido"},
    ],
    mistakes=[
        {"wrong": "Decir que el agua en el tazón es menos porque cambió de forma.", "why": "Se confunde forma con cantidad.", "fix": "Mide: el volumen se conserva cuando solo cambia de recipiente."},
        {"wrong": "Pensar que se puede apretar el agua para que quepa en un recipiente más chico.", "why": "Se piensa que los líquidos se comprimen fácilmente.", "fix": "Un volumen de agua ocupa siempre su lugar; si no cabe, se rebalsa."},
    ],
    tiers={
        "recovery": [
            ex("¿El agua líquida fluye o es dura como una piedra?", "Fluye", "El líquido se vierte y corre."),
            ex("Echas agua de una botella a un vaso. ¿Qué forma toma el agua?", "La del vaso", "El líquido se adapta al recipiente."),
            ex("Completa: el lugar que ocupa el agua se llama ___.", "volumen", "Volumen es el lugar que ocupa algo."),
        ],
        "understand": [
            ex("Explica con tus palabras qué es un líquido.", "Algo que fluye y toma la forma del recipiente", "Esas son las características del estado líquido."),
            ex("¿El agua cambia de volumen al pasar de la botella a la jarra?", "No", "Solo cambia la forma; el volumen se conserva."),
            ex("¿Cómo se ve la superficie del agua cuando está quieta en un vaso?", "Plana", "El líquido en reposo queda plano."),
        ],
        "apply": [
            arith("Una botella tiene 500 mL de agua. Sirves 3 vasos de 150 mL cada uno. ¿Cuántos mL quedan en la botella?", "500-3*150", "Se resta el total servido, 3 × 150, de lo que había.", " mL"),
            ex("Tienes un frasco de 1 litro (1.000 mL) y echas 400 mL de agua. ¿Qué forma tiene el agua dentro del frasco si el frasco es cuadrado?", "La del frasco, cuadrada", "El agua toma la forma del frasco."),
            ex("Un vaso con 200 mL de agua se vierte en un plato hondo. ¿Cuántos mL de agua hay en el plato?", "200 mL", "El volumen se conserva al cambiar de recipiente."),
        ],
        "reason": [
            ex("Un jugo y una piedra están en la mesa. Rodrigo dice que los dos son sólidos porque están en la mesa. ¿Quién tiene razón?", "No tiene razón; el jugo es líquido", "El jugo fluye y toma la forma del vaso."),
            ex("¿Por qué una jarra de 1 litro no puede guardar 2 litros de agua sin rebalsar?", "Porque el agua ocupa un lugar y 2 litros no caben", "El agua tiene volumen propio y no se comprime."),
        ],
        "challenge": [
            ex("Clasifica en sólido o líquido: hielo, agua, cubo de madera, jugo.", "Sólidos: hielo y cubo de madera; líquidos: agua y jugo", "El hielo y la madera tienen forma propia; el agua y el jugo fluyen."),
            ex("Una botella de 750 mL se llena con el contenido de dos vasos de 300 mL. ¿Cuánto falta para llenarla?", "150 mL", "Dos vasos son 600 mL y 750 − 600 = 150 mL."),
        ],
    },
    context=[ex("En un cumpleaños sirven jugo de una jarra a vasos más chicos. En la jarra hay 1.000 mL y se llenan 4 vasos de 200 mL. ¿Cuántos mL quedan en la jarra?", "200 mL", "4 vasos de 200 mL son 800 mL y 1.000 − 800 = 200 mL.")],
    selfcheck=[
        ex("¿El agua líquida tiene forma propia?", "No", "Toma la forma del recipiente."),
        ex("¿Qué es el volumen?", "El lugar que ocupa algo", "Es lo que ocupa el agua en un recipiente."),
        ex("¿El agua fluye o es rígida?", "Fluye", "Los líquidos corren y se vierten."),
    ],
    open_task=task(
        "Dibuja un vaso con 200 mL de agua, un tazón y una botella. En cada dibujo muestra cómo se ve el agua cuando pasa de uno a otro. Escribe tres frases: una sobre la forma, una sobre el volumen y una sobre la superficie.",
        "En el vaso el agua es alta; en el tazón es ancha y baja. El volumen sigue siendo 200 mL. La superficie siempre queda plana cuando el agua está quieta.",
        ["dibuja el agua adaptada a cada recipiente", "dice que el volumen se conserva", "describe la superficie plana"],
        ["tres dibujos", "tres frases", "rótulos de mL"],
        ["dibujar el agua con forma propia", "decir que el volumen cambia"],
        "Valora los dibujos claros y pide que explique cómo sabe que la cantidad es la misma.",
    ),
    reinforce="Pasa 100 mL entre dos recipientes distintos y repite: «la forma cambia, el volumen no».",
    extend="Compara un líquido espeso, como la miel, con agua: ¿también fluyen? Explica con una frase.",
)

register(
    OA10, 3,
    materials="Un vaso con agua fría, una olla con tapa y agua tibia (solo observar, con un adulto a cargo), un espejo o ventana. Todo calor lo maneja un adulto.",
    use="Aprenderé que el agua también puede estar como gas, llamado vapor de agua, y que no se ve. Sirve para entender por qué se empaña un espejo o un vaso frío.",
    prior=["Sé que el agua se evapora.", "Sé que el hielo es sólido y el agua es líquida."],
    explain=[
        "El agua en estado gaseoso se llama vapor de agua. Es invisible. Cuando el agua se evapora, o cuando hierve, pasa al aire como vapor. Un gas se esparce y llena todo el espacio, como el aire dentro de un globo.",
        "Lo blanco que se ve sobre una taza caliente no es vapor. Son gotitas muy pequeñas de agua líquida que se formaron cuando el vapor se enfrió. Por eso no debo llamar «humo» a todo lo que se ve: el humo viene de quemar algo y el vapor de agua, no.",
        "Si pongo un vaso con agua fría en una pieza tibia, aparecen gotas por fuera. El vapor de agua que hay en el aire se enfría al tocar el vaso y vuelve a ser agua líquida. Esas gotas vienen del aire, no pasan a través del vidrio.",
    ],
    vocab=[("gas", "estado en que algo se esparce y llena el espacio"), ("vapor de agua", "agua en estado gaseoso, invisible"), ("hervir", "calentar el agua hasta que forma burbujas y mucho vapor"), ("gotita", "gota muy pequeña de agua líquida"), ("condensar", "pasar del estado gaseoso al líquido por enfriarse")],
    worked=[
        {"title": "La nube blanca sobre la taza", "problem": "Sobre una taza de agua muy caliente se ve una nube blanca. ¿Es vapor de agua o son gotitas?", "steps": ["El vapor de agua es invisible.", "Lo que se ve es blanco y se mueve.", "Son gotitas de agua líquida que se formaron al enfriarse el vapor."], "answer": "Son gotitas de agua líquida; el vapor es invisible"},
        {"title": "Vaso con gotas por fuera", "problem": "Un vaso con agua fría tiene gotas por fuera después de un rato. ¿De dónde salió esa agua?", "steps": ["El aire de la pieza tiene vapor de agua.", "El vapor toca el vaso frío y se enfría.", "Vuelve a ser agua líquida y forma gotas."], "answer": "Del vapor de agua del aire que se condensó"},
    ],
    mistakes=[
        {"wrong": "Llamar humo al vapor de agua.", "why": "Se parecen a la vista, pero se forman de forma distinta.", "fix": "El humo viene de quemar algo; lo blanco sobre agua caliente son gotitas de agua."},
        {"wrong": "Pensar que el agua pasa por el vidrio del vaso.", "why": "No se considera el vapor del aire.", "fix": "Las gotas de afuera vienen del vapor de agua del aire que se enfrió."},
    ],
    tiers={
        "recovery": [
            ex("¿Cómo se llama el agua en estado gaseoso?", "Vapor de agua", "Vapor de agua es el gas del agua."),
            ex("¿El vapor de agua se ve o es invisible?", "Es invisible", "Los gases como el vapor de agua no se ven."),
            ex("Completa: el agua pasa del estado líquido al gaseoso cuando se ___.", "evapora", "Evaporarse es pasar a gas."),
        ],
        "understand": [
            ex("¿Qué es un gas?", "Algo que se esparce y llena todo el espacio", "Esa es la característica de un gas."),
            ex("La nube blanca sobre agua caliente, ¿es vapor o gotitas de agua líquida?", "Gotitas de agua líquida", "El vapor es invisible; lo blanco son gotitas."),
            ex("¿Por qué no se debe llamar humo al vapor de agua?", "Porque el humo viene de quemar algo", "Son cosas distintas con origen distinto."),
        ],
        "apply": [
            ex("Un espejo de baño se empaña después de una ducha tibia. ¿Qué hizo que se formaran las gotitas?", "El vapor de agua se enfrió al tocar el espejo", "El espejo está más frío que el vapor, y este se condensa."),
            ex("Un vaso con jugo muy frío se deja en la mesa y se moja por fuera. ¿Por qué?", "Porque el vapor de agua del aire se enfría y forma gotas", "El vaso frío condensa el vapor del aire."),
            ex("Una olla con agua hirviendo, a cargo de un adulto, produce mucho vapor. ¿Quién la debe manipular?", "Un adulto", "El vapor y el agua hirviendo pueden quemar."),
        ],
        "reason": [
            ex("Marta dice: «El vapor de agua es blanco como una nube». ¿Qué le explicas?", "Que el vapor es invisible y lo blanco son gotitas", "El vapor de agua es un gas que no se ve."),
            ex("Se abre un frasco con vapor de agua dentro de una pieza cerrada. Valeria dice que el vapor se queda en el fondo como el agua líquida. ¿Qué le respondes?", "Que el vapor, como todo gas, se esparce por toda la pieza", "Un gas llena el espacio disponible; el agua líquida, en cambio, se queda abajo."),
        ],
        "challenge": [
            ex("Clasifica cada caso como sólido, líquido o gas: hielo, vapor de agua, agua de la llave.", "Hielo, sólido; vapor, gas; agua de la llave, líquido", "El hielo es sólido, el vapor es gas y el agua de la llave es líquida."),
            ex("Una ventana está empañada por dentro en un día frío. Explica con tu palabra «vapor» por qué.", "El vapor de agua de la pieza se enfrió en el vidrio frío y formó gotitas", "El vapor del aire se condensa al tocar el vidrio frío."),
        ],
    },
    context=[ex("Mientras tu abuela hace té, ves una nube blanca sobre la tetera. Ella dice que es humo. ¿Qué le explicas?", "Que son gotitas de agua que se formaron al enfriarse el vapor", "El humo viene de quemar algo; aquí hay vapor de agua y gotitas.")],
    selfcheck=[
        ex("¿Qué es el vapor de agua?", "Agua en estado gaseoso", "Es el gas del agua."),
        ex("¿Se ve el vapor de agua?", "No", "Es un gas invisible."),
        ex("¿Qué se forma cuando el vapor se enfría?", "Gotitas de agua líquida", "El vapor se condensa."),
    ],
    open_task=task(
        "Haz una tabla de tres filas: «hielo», «agua líquida» y «vapor de agua». En cada fila escribe el estado (sólido, líquido o gas), si se ve y si tiene forma propia. Si tienes un vaso con agua fría y gotas por fuera, dibújalo y explica de dónde vienen las gotas.",
        "Hielo: sólido, se ve, forma propia. Agua líquida: líquido, se ve, toma la forma del recipiente. Vapor: gas, no se ve, se esparce. Las gotas del vaso vienen del vapor del aire.",
        ["completa bien los tres estados", "dice que el vapor no se ve", "explica el origen de las gotas"],
        ["tabla completa", "dibujo del vaso con gotas", "frase explicativa"],
        ["decir que el vapor se ve", "decir que las gotas salen del vaso"],
        "Reconoce la tabla completa y pide que explique por qué el vapor se confunde con humo.",
    ),
    reinforce="Dibuja un vaso frío con gotas por fuera y escribe «vapor del aire → gotas de agua».",
    extend="Observa un espejo o ventana en un día frío y dibuja cuándo se empaña y cuándo se aclara.",
)

register(
    OA10, 4,
    materials="Una tabla en papel para comparar estados, lápices de colores, un vaso con agua y un cubo de hielo. Sin fuego ni agua caliente: lo caliente lo observa un adulto.",
    use="Aprenderé a comparar los estados sólido, líquido y gaseoso del agua y los cambios entre ellos. Sirve para explicar qué pasa con el agua cuando se enfría o se calienta.",
    prior=["Sé qué es hielo, agua líquida y vapor de agua.", "Sé que el calor y el frío cambian el estado del agua."],
    explain=[
        "El agua puede cambiar de estado. Si se calienta, el hielo se derrite y pasa a líquido. Si se calienta más, el líquido se evapora y pasa a gas. Si se enfría, el vapor se condensa y pasa a líquido, y si se enfría más, el líquido se congela y pasa a sólido.",
        "En cada estado cambian la forma y el espacio que ocupa el agua. El sólido tiene forma propia. El líquido toma la forma del recipiente. El gas se esparce y llena todo el espacio. Pero siempre es agua.",
        "Para comparar estados uso una tabla con tres preguntas: ¿tiene forma propia?, ¿fluye?, ¿se ve? Así veo que el hielo es sólido, el agua líquida fluye y el vapor es un gas invisible.",
    ],
    vocab=[("derretir", "pasar de sólido a líquido por calor"), ("evaporar", "pasar de líquido a gas por calor"), ("condensar", "pasar de gas a líquido por frío"), ("congelar", "pasar de líquido a sólido por frío"), ("cambio de estado", "paso del agua de un estado a otro")],
    worked=[
        {"title": "Completar una tabla de estados", "problem": "Completa: hielo (¿forma propia?, ¿fluye?), agua líquida (¿forma propia?, ¿fluye?).", "steps": ["Hielo: tiene forma propia y no fluye.", "Agua líquida: no tiene forma propia y sí fluye.", "El vapor de agua no tiene forma propia, se esparce y no se ve."], "answer": "Hielo: forma propia, no fluye. Agua líquida: sin forma propia, fluye"},
        {"title": "Nombrar un cambio", "problem": "El agua líquida de una bandeja pasa a cubos de hielo en el congelador. ¿Cómo se llama ese cambio?", "steps": ["Antes era líquida y ahora es sólida.", "Se enfrió hasta 0 °C o menos.", "Pasar de líquido a sólido es congelar."], "answer": "Congelar"},
    ],
    mistakes=[
        {"wrong": "Decir que el vapor se ve como una nube.", "why": "Se confunde el vapor con las gotitas.", "fix": "El vapor de agua es invisible; lo que se ve son gotitas de agua líquida."},
        {"wrong": "Creer que al cambiar de estado el agua se vuelve otra sustancia.", "why": "Se compara solo la apariencia.", "fix": "Siempre es agua; solo cambia el estado."},
    ],
    tiers={
        "recovery": [
            ex("Un cubo de hielo recibe calor y pasa a agua líquida. ¿Cómo se llama ese cambio?", "Derretir", "Pasar de sólido a líquido es derretir."),
            ex("El agua líquida se congela. ¿A qué estado pasa?", "Al sólido", "Congelar es pasar de líquido a sólido."),
            ex("Completa: el vapor de agua es el estado ___ del agua.", "gaseoso", "Vapor de agua es agua como gas."),
        ],
        "understand": [
            ex("¿Qué estado del agua tiene forma propia?", "El sólido", "El hielo mantiene su forma."),
            ex("¿Qué estado del agua se esparce por todo el espacio?", "El gaseoso", "El vapor de agua es un gas."),
            ex("¿Qué tienen en común el hielo, el agua líquida y el vapor?", "Que todos son agua", "Es la misma sustancia en tres estados."),
        ],
        "apply": [
            ex("Nombra el cambio: líquido a gas.", "Evaporar", "El agua líquida se evapora al calentarse."),
            ex("Nombra el cambio: gas a líquido.", "Condensar", "El vapor se enfría y pasa a líquido."),
            ex("En una tabla, para el agua líquida marca cuál es correcta: ¿forma propia: sí o no?", "No", "El líquido toma la forma del recipiente."),
        ],
        "reason": [
            ex("Ignacio dice: «Si calientas hielo mucho tiempo, desaparece». ¿Qué pasa en realidad con el agua?", "Pasa a líquido y luego a vapor, pero no desaparece", "El agua cambia de estado y se esparce como vapor invisible."),
            ex("Una olla tapada con agua caliente tiene gotas de agua bajo la tapa. Explica con tu palabra «vapor» de dónde vienen.", "Vienen del vapor que se enfrió en la tapa", "El vapor choca con la tapa más fría y se condensa."),
        ],
        "challenge": [
            ex("Ordena los pasos si calientas hielo hasta que sea vapor: evaporar, derretir.", "Primero derretir y luego evaporar", "El hielo pasa a líquido y después a gas."),
            ex("Ordena si enfrías vapor hasta tener hielo: congelar, condensar.", "Primero condensar y luego congelar", "El vapor pasa a líquido y después a sólido."),
        ],
    },
    context=[ex("Julieta deja una bandeja con agua en el congelador, luego saca los cubos y los deja al sol. Escribe los dos cambios que ocurren en orden.", "Primero congelar y luego derretir", "El agua se congela en el frío y el hielo se derrite con calor.")],
    selfcheck=[
        ex("¿Cómo se llama pasar de líquido a gas?", "Evaporar", "El agua líquida se evapora."),
        ex("¿Qué estado tiene el hielo?", "Sólido", "El hielo es agua sólida."),
        ex("¿Cómo se llama pasar de gas a líquido?", "Condensar", "El vapor se enfría."),
    ],
    open_task=task(
        "Haz un dibujo en forma de ciclo con cuatro cuadros: hielo, agua líquida, vapor y gotitas en una ventana fría. Entre cada cuadro dibuja una flecha y escribe el nombre del cambio (derretir, evaporar, condensar). Termina con una frase: «En todos los cuadros hay agua porque…».",
        "Hielo → derretir → agua líquida → evaporar → vapor → condensar → gotitas. En todos hay agua porque solo cambia el estado.",
        ["dibuja los cuatro cuadros en orden", "nombra bien los cambios", "explica que siempre es agua"],
        ["dibujo con flechas", "nombres de cambios", "frase de conclusión"],
        ["confundir evaporar y condensar", "decir que el vapor se ve"],
        "Valora la secuencia ordenada y pide que explique qué hace cambiar de estado al agua.",
    ),
    reinforce="Escribe en tarjetas los nombres «derretir», «evaporar», «condensar» y «congelar» y únelos con flechas a cada cambio.",
    extend="Explica por qué una cubeta de hielo en un día de verano se derrite más rápido al sol que en la sombra.",
)
