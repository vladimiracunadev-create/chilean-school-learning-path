"""Cuaderno del estudiante, 1.º básico Ciencias Naturales: OA 09 (cambios en los materiales) y OA 10 (diseño de instrumentos tecnológicos simples)."""
from __future__ import annotations

from student_content_cn_a import task
from student_lessons import arith, ex, register

OA9, OA10 = "CN01 OA 09", "CN01 OA 10"

# ---------------------------------------------------------------- OA 09
register(
    OA9, 1,
    materials="Este cuaderno con la tabla de una hoja de papel antes y después de arrugarla (datos de ejemplo), lápiz y colores. En casa: una hoja de papel, una regla y un poco de plasticina o masa.",
    use="Aprenderé a mirar cómo estaba un material antes y cómo queda después de aplicarle una fuerza. Sirve para describir cambios con datos.",
    prior=["Sé las propiedades de los materiales.", "Sé medir con una regla."],
    explain=[
        "Una fuerza es un empujón o un tirón. Cuando aplicas una fuerza a un material, puede cambiar su forma. Si aprietas plasticina, se aplasta. Si arrugas una hoja, se hace una bolita. Si estiras una goma, se alarga.",
        "Para describir un cambio, mira el antes y el después. Una hoja de papel mide 21 cm de ancho. Después de arrugarla con fuerza mide 6 cm. El papel cambió su forma, pero sigue siendo papel.",
        "Algunos materiales vuelven a su forma cuando sueltas la fuerza, como la goma; se llaman elásticos. Otros no vuelven, como el papel arrugado o la plasticina aplastada. Anota siempre dos cosas: cómo era antes, cómo quedó después.",
    ],
    vocab=[("fuerza", "empujón o tirón que se aplica a un objeto"), ("cambio", "diferencia entre antes y después"), ("antes", "cómo estaba al comienzo"), ("después", "cómo quedó al final"), ("deformar", "cambiar la forma de algo"), ("elástico", "que vuelve a su forma cuando se suelta")],
    worked=[
        {"title": "Antes y después del papel", "problem": "Hoja de papel: antes 21 cm. Después de arrugarla con fuerza: 6 cm. ¿Cuánto cambió?", "steps": ["Antes: 21 cm.", "Después: 6 cm.", "21 menos 6 son 15."], "answer": "Se achicó 15 cm"},
        {"title": "Una goma que vuelve", "problem": "Una goma de pelo mide 8 cm. La estiras a 14 cm y la sueltas: mide 8 cm. ¿Qué pasó?", "steps": ["Con la fuerza se alargó a 14 cm.", "Al soltar volvió a 8 cm."], "answer": "La goma volvió a su forma porque es elástica"},
    ],
    mistakes=[
        {"wrong": "Decir «el papel arrugado ya es otro material».", "why": "Se confunde la forma con el material.", "fix": "Sigue siendo papel; solo cambió su forma."},
        {"wrong": "Describir el cambio sin decir el antes.", "why": "Se olvida comparar.", "fix": "Escribe cómo estaba antes y cómo quedó después."},
    ],
    tiers={
        "recovery": [
            ex("Aprietas una bolita de plasticina con el dedo. ¿Qué le pasa a su forma?", "Se aplasta", "La fuerza cambia su forma."),
            ex("Arrugas una hoja. ¿Sigue siendo papel?", "Sí", "Solo cambió su forma."),
            ex("¿Qué es una fuerza?", "Un empujón o un tirón", "Así se mueve o cambia un objeto."),
        ],
        "understand": [
            ex("¿Qué dos cosas debes anotar para describir un cambio?", "Cómo era antes y cómo quedó después", "Así se compara."),
            ex("¿Por qué la goma vuelve a su forma?", "Porque es elástica", "Un material elástico recupera su forma al soltarlo."),
            ex("¿Cambia el material si cambia la forma?", "No", "Sigue siendo el mismo material."),
        ],
        "apply": [
            arith("Una hoja de papel medía 21 cm y arrugada mide 6 cm. ¿Cuántos centímetros se achicó?", "21-6", "Se resta lo que mide después a lo que medía antes.", " cm"),
            arith("Una goma mide 8 cm y la estiras hasta 14 cm. ¿Cuántos centímetros se alargó?", "14-8", "Se resta lo que medía antes a lo que mide estirada.", " cm"),
            arith("Una bolita de plasticina tiene 4 cm de alto. Al aplastarla mide 1 cm. ¿Cuántos centímetros bajó?", "4-1", "Se resta la altura final a la inicial.", " cm"),
        ],
        "reason": [
            ex("Tomás dice que la plasticina aplastada tiene menos plasticina. ¿Qué le respondes?", "Que tiene la misma plasticina, solo cambió su forma", "No se perdió material."),
            ex("Una regla de madera se dobla con fuerza y se rompe. Una goma se dobla y vuelve. ¿Qué material es más flexible?", "La goma", "Se dobla sin romperse."),
        ],
        "challenge": [
            ex("Escribe una cosa de tu casa que cambie de forma al aplicarle una fuerza.", "Por ejemplo una esponja", "Se aprieta y se aplasta."),
            ex("Aplastas 3 bolitas de plasticina y 2 de masa. ¿Cuántas bolitas aplastaste?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Para guardar una bolsa, Clara la aprieta y pasa de 30 cm de alto a 12 cm. ¿Cuántos centímetros se achicó?", "18 cm", "Treinta menos doce son dieciocho.")],
    selfcheck=[ex("¿Una fuerza es un empujón o un color?", "Un empujón", "Empuja o tira."), ex("¿Qué material vuelve a su forma: la goma o el papel arrugado?", "La goma", "Es elástica y recupera su forma."), ex("¿Qué se compara en un cambio?", "El antes y el después", "Muestra la diferencia.")],
    open_task=task("Lee esta tabla de tres materiales a los que se les aplicó fuerza: papel, antes 21 cm, después de arrugarlo 6 cm; goma, antes 8 cm, estirada 14 cm, soltada 8 cm; plasticina, antes 4 cm, aplastada 1 cm. Escribe qué cambió en cada uno y cuál volvió a su forma.", "Papel: se achicó 15 cm. Goma: se alargó 6 cm y volvió a 8 cm. Plasticina: bajó 3 cm. Solo la goma volvió a su forma.", ["describe el cambio con números", "dice cuál volvió a su forma", "usa antes y después"], ["tabla", "frases"], ["no usar el antes", "decir que cambió el material"], "Reconoce los cambios y pide los números del antes y el después."),
    reinforce="Aprieta plasticina o masa y mide la altura antes y después.",
    extend="Explica por qué la goma vuelve a su forma y el papel no.",
)

register(
    OA9, 2,
    materials="Este cuaderno con los datos de dos pruebas: hoja seca y hoja mojada, y azúcar en agua (datos de ejemplo), lápiz y colores. En casa: papel, agua, monedas iguales, una cuchara y azúcar.",
    use="Aprenderé cómo el agua y la fuerza cambian los materiales. Sirve para entender por qué el papel mojado se rompe y el azúcar desaparece en el agua.",
    prior=["Sé qué es un cambio antes y después.", "Sé contar hasta 20."],
    explain=[
        "El agua puede cambiar los materiales. El papel mojado se ablanda y se rompe fácil. Una galleta se pone blanda. El azúcar se mezcla con el agua y ya no se ve, aunque sigue ahí: el agua queda dulce.",
        "Una prueba muestra el cambio. Se pone una hoja seca sobre dos vasos y se agregan monedas iguales una por una: la hoja seca aguanta 8 monedas. Con una hoja mojada, aguanta solo 2 monedas.",
        "Con las dos pruebas se ve que el agua hizo el papel más débil. Para la prueba del azúcar, se revuelve una cucharada de azúcar en un vaso con agua hasta que ya no se ve.",
    ],
    vocab=[("prueba", "ensayo que se hace para ver qué pasa"), ("mojado", "con agua"), ("disolverse", "mezclarse con el agua hasta no verse"), ("débil", "que aguanta poco"), ("moneda", "pieza redonda que usamos como peso en la prueba")],
    worked=[
        {"title": "Comparar hoja seca y mojada", "problem": "Hoja seca aguantó 8 monedas. Hoja mojada aguantó 2 monedas. ¿Qué pasó?", "steps": ["8 es mayor que 2.", "La hoja mojada aguanta menos.", "8 menos 2 son 6 monedas menos."], "answer": "El agua debilitó el papel; aguantó 6 monedas menos"},
        {"title": "El azúcar en el agua", "problem": "Pones una cucharada de azúcar en agua y revuelves un buen rato. Ya no se ve. ¿Desapareció?", "steps": ["No se ve el azúcar.", "El agua queda dulce.", "El azúcar sigue ahí, mezclada."], "answer": "No desapareció; se mezcló con el agua"},
    ],
    mistakes=[
        {"wrong": "Decir que el azúcar desapareció del todo.", "why": "No se prueba el agua.", "fix": "El agua queda dulce; el azúcar sigue ahí, mezclada."},
        {"wrong": "Decir que el papel mojado es otro material.", "why": "Se confunde un cambio con ser otro material.", "fix": "Es papel que se ablandó."},
    ],
    tiers={
        "recovery": [
            ex("Hoja seca aguantó 8 monedas y hoja mojada 2. ¿Cuál aguanta más?", "La hoja seca", "8 es mayor que 2."),
            ex("¿El papel mojado se pone fuerte o débil?", "Débil", "El agua lo ablanda y rompe fácil."),
            ex("¿Qué le pasa a la galleta en agua?", "Se ablanda", "El agua la cambia."),
        ],
        "understand": [
            ex("¿Qué significa que el azúcar «se disuelve»?", "Que se mezcla con el agua y ya no se ve", "El azúcar sigue ahí, mezclada."),
            ex("¿Cómo se sabe que el azúcar sigue en el agua?", "Porque el agua queda dulce", "El sabor lo muestra."),
            ex("¿Por qué se usan monedas iguales en la prueba?", "Para que cada una pese lo mismo", "Así la comparación es justa."),
        ],
        "apply": [
            arith("La hoja seca aguantó 8 monedas y la mojada 2. ¿Cuántas monedas menos aguantó la mojada?", "8-2", "Se resta lo que aguantó la mojada.", " monedas"),
            arith("Otra hoja seca aguantó 9 monedas y mojada 3. ¿Cuántas monedas menos aguantó la mojada?", "9-3", "Se resta lo que aguantó la mojada.", " monedas"),
            ex("Tres cucharaditas de sal se mezclan con agua en un vaso. ¿Cuántas cucharaditas hay en el agua?", "3", "La sal sigue en el agua."),
        ],
        "reason": [
            ex("Si la hoja mojada aguanta menos monedas, ¿puedes decir que el agua la cambió? Explica con datos.", "Sí, aguantó 2 monedas en vez de 8", "El único cambio fue el agua."),
            ex("Camila dice que el azúcar se fue del vaso. ¿Qué prueba simple harías con un adulto?", "Probar el agua y ver que está dulce", "Muestra que el azúcar está allí."),
        ],
        "challenge": [
            ex("Escribe un material que se ablande con el agua.", "Por ejemplo el pan o el cartón", "El agua los debilita."),
            ex("En una prueba, 3 hojas secas y 3 mojadas. ¿Cuántas hojas probaron?", "6", "Tres más tres son seis."),
        ],
    },
    context=[ex("Una caja de cartón se moja en la lluvia y sus esquinas se ablandan. Aguantaba 10 libros y ahora aguanta 4. ¿Cuántos libros menos aguanta?", "6", "Diez menos cuatro son seis.")],
    selfcheck=[ex("¿Qué hace el agua con el papel?", "Lo ablanda", "El agua lo debilita y lo rompe fácil."), ex("Si revuelves azúcar en agua, ¿el azúcar se disuelve?", "Sí", "Se mezcla con el agua y deja de verse."), ex("¿Cómo se llama el ensayo para ver qué pasa?", "Prueba", "Se hace para comprobar.")],
    open_task=task("Lee estos datos de una prueba de agua: servilleta seca aguantó 6 monedas, mojada aguantó 1 moneda. Tela seca aguantó 12 monedas, mojada aguantó 11 monedas. Escribe cuál material cambió más con el agua y cómo lo sabes.", "La servilleta cambió más: pasó de 6 a 1 moneda (5 menos). La tela pasó de 12 a 11 (1 menos).", ["compara con números", "dice cuál cambió más", "explica con la resta"], ["tabla", "frase"], ["no hacer la resta", "decir que la tela no cambió"], "Reconoce que cita datos y pide mostrar la resta de cada material."),
    reinforce="Con ayuda de un adulto, prueba una hoja seca y una mojada con monedas.",
    extend="Explica por qué se debe proteger un cuaderno de la lluvia.",
)

register(
    OA9, 3,
    materials="Este cuaderno con los datos de un experimento (cubos de hielo al sol y a la sombra, papel de color en una ventana; datos de ejemplo), lápiz y colores. En casa, con un adulto: dos cubos de hielo, dos platos y un lugar con sol. No uses fuego ni cosas calientes.",
    use="Aprenderé cómo la luz y el calor cambian los materiales, con seguridad. Sirve para entender por qué el hielo se derrite y el color de un papel se apaga.",
    prior=["Sé qué es un cambio antes y después.", "Sé que el Sol da luz y calor."],
    explain=[
        "El calor cambia algunos materiales. El hielo se derrite cuando se calienta y se vuelve agua. La mantequilla se ablanda. El Sol da calor, por eso un cubo de hielo al sol se derrite más rápido que a la sombra.",
        "La luz también cambia algunos materiales. Un papel de color pegado en una ventana durante muchos días se va poniendo más pálido porque la luz del Sol apaga su color. Esto pasa de a poco.",
        "Datos de ejemplo: un cubo de hielo al sol se derritió en 20 minutos y otro a la sombra tardó 50 minutos. Un papel rojo en la ventana tenía color fuerte el día 0 y color pálido el día 14. Seguridad: no uses fuego, planchas ni agua hirviendo; solo el Sol y un adulto cerca.",
    ],
    vocab=[("calor", "energía que hace que algo esté más caliente"), ("derretir", "pasar de hielo a agua por el calor"), ("luz", "lo que nos permite ver"), ("pálido", "con poco color"), ("seguridad", "cuidado para no hacerse daño")],
    worked=[
        {"title": "Hielo al sol y a la sombra", "problem": "Hielo al sol: 20 minutos. Hielo a la sombra: 50 minutos. ¿Dónde se derrite más rápido?", "steps": ["20 es menor que 50.", "Al sol tardó menos."], "answer": "Al sol; tardó 30 minutos menos"},
        {"title": "El papel en la ventana", "problem": "Papel rojo: día 0 color fuerte, día 14 color pálido. ¿Qué cambió y por qué?", "steps": ["El color se apagó.", "Estuvo 14 días con luz del Sol."], "answer": "La luz del Sol apagó su color"},
    ],
    mistakes=[
        {"wrong": "Querer derretir hielo con una plancha o fuego.", "why": "Se busca que pase rápido.", "fix": "Nunca uses cosas calientes sin un adulto; basta el Sol."},
        {"wrong": "Esperar que el color cambie en un minuto.", "why": "Se piensa que todos los cambios son rápidos.", "fix": "Algunos cambios tardan días; anota la fecha."},
    ],
    tiers={
        "recovery": [
            ex("¿El hielo se derrite con calor o con frío?", "Con calor", "El calor lo vuelve agua."),
            ex("¿Dónde se derrite más rápido un hielo: al sol o a la sombra?", "Al sol", "El sol da calor."),
            ex("¿Qué le pasa al color de un papel que está mucho tiempo al sol?", "Se pone pálido", "La luz lo apaga."),
        ],
        "understand": [
            ex("¿Qué es derretir?", "Pasar de hielo a agua por el calor", "El hielo cambia de estado."),
            ex("¿Por qué conviene un adulto cerca?", "Para evitar quemaduras o accidentes", "Cuida tu seguridad."),
            ex("¿Todos los cambios son rápidos?", "No", "Algunos tardan días."),
        ],
        "apply": [
            arith("El hielo tardó 20 minutos al sol y 50 minutos a la sombra. ¿Cuántos minutos más tardó a la sombra?", "50-20", "Se resta el tiempo al sol al tiempo a la sombra.", " minutos"),
            arith("El hielo A se derritió en 20 minutos y el hielo C en 30 minutos. ¿Cuántos minutos más tardó el C?", "30-20", "Se resta el tiempo del A al del C.", " minutos"),
            ex("Tabla: papel azul pegado 10 días en una ventana con sol; día 0 color fuerte, día 10 color pálido. ¿Qué lo cambió: la luz o el agua?", "La luz", "Estuvo en la ventana con sol."),
        ],
        "reason": [
            ex("Ana dice que el hielo se derrite más rápido al sol que a la sombra. ¿Qué dato lo apoya?", "A la sombra tardó 50 minutos y al sol 20", "El sol da más calor."),
            ex("Beto quiere derretir hielo con una vela. ¿Qué le dices?", "Que no, porque el fuego es peligroso y basta el Sol", "La seguridad es primero."),
        ],
        "challenge": [
            ex("Escribe un material que se derrita con el calor.", "Por ejemplo el hielo o la mantequilla", "El calor lo ablanda."),
            ex("Hay 2 cubos al sol y 3 a la sombra. ¿Cuántos cubos hay?", "5", "Dos más tres son cinco."),
        ],
    },
    context=[ex("En un día de verano, un helado de agua se derrite en 15 minutos al sol y en 40 minutos a la sombra (datos de ejemplo). ¿Cuántos minutos tarda más a la sombra?", "25 minutos", "Cuarenta menos quince son veinticinco.")],
    selfcheck=[ex("¿Qué da el Sol?", "Luz y calor", "El Sol entrega las dos cosas."), ex("¿Se usa fuego para el experimento?", "No", "El fuego es peligroso para niños."), ex("¿Cómo cambia el papel al sol por días?", "Se pone pálido", "La luz apaga el color.")],
    open_task=task("Lee estos datos y escribe una conclusión: cubo de hielo A al sol, se derrite en 18 minutos; cubo B a la sombra, 45 minutos; cubo C dentro de un sobre de papel al sol, 30 minutos. Ordena de más rápido a más lento y explica con calor.", "A (18), C (30), B (45). Al sol se derrite más rápido porque recibe más calor; el sobre da algo de sombra.", ["ordena con los números", "explica con calor", "cita los minutos"], ["lista ordenada", "frase"], ["ordenar mal", "no usar números"], "Reconoce el orden y pide explicar por qué C quedó entre A y B."),
    reinforce="Con ayuda de un adulto, pon un hielo al sol y otro a la sombra y mira la hora.",
    extend="Explica por qué se guardan los helados en el congelador.",
)

register(
    OA9, 4,
    materials="Este cuaderno con cuatro historias de cambio (con fuerza, luz, calor o agua) y una pauta para explicar, lápiz y colores.",
    use="Aprenderé a explicar un cambio diciendo qué lo causó. Sirve para comunicar lo que observé con datos y razones.",
    prior=["Sé que la fuerza, la luz, el calor y el agua cambian los materiales.", "Sé comparar el antes y el después."],
    explain=[
        "Para explicar un cambio usa tres frases: «Antes estaba…», «Después quedó…» y «Cambió porque…». Por ejemplo: «Antes la galleta estaba dura. Después quedó blanda. Cambió porque le puse agua».",
        "Elige la causa que corresponda. Si aprietas o estiras, la causa es la fuerza. Si el hielo se derrite, es el calor. Si el color se apaga por días, es la luz. Si algo se moja y se ablanda o se mezcla, es el agua.",
        "Usa datos cuando los tengas. «El hielo tardó 20 minutos al sol» es mejor que «se derritió rápido». Un buen científico dice lo que vio, no lo que le parece.",
    ],
    vocab=[("causa", "lo que hace que algo cambie"), ("explicar", "decir qué pasó y por qué"), ("dato", "número o hecho que observé"), ("conclusión", "lo que aprendo de las observaciones"), ("comunicar", "contar a otros lo que aprendí")],
    worked=[
        {"title": "Explicar con tres frases", "problem": "Un cubo de hielo medía 3 cm y después de 20 minutos al sol era un charquito. Explica.", "steps": ["Antes: hielo de 3 cm.", "Después: agua en el plato.", "Causa: el calor del sol."], "answer": "Antes era hielo; después agua; cambió por el calor"},
        {"title": "Elegir la causa", "problem": "Un resorte estirado se alarga 5 cm. ¿Cuál es la causa?", "steps": ["Estirar es tirar.", "Tirar es aplicar una fuerza."], "answer": "La fuerza"},
    ],
    mistakes=[
        {"wrong": "Explicar sin decir la causa.", "why": "Solo se cuenta qué pasó.", "fix": "Agrega «cambió porque…» con fuerza, luz, calor o agua."},
        {"wrong": "Elegir la causa por una suposición.", "why": "No se revisa la evidencia.", "fix": "Relee tus datos antes de decidir."},
    ],
    tiers={
        "recovery": [
            ex("El hielo se derrite. ¿La causa es el calor o la fuerza?", "El calor", "El calor lo derrite."),
            ex("Aprietas una esponja y se achica. ¿La causa es la fuerza o la luz?", "La fuerza", "Al apretar aplicas fuerza."),
            ex("Un papel se pone pálido al sol por días. ¿La causa es la luz o el agua?", "La luz", "El sol apaga el color."),
        ],
        "understand": [
            ex("¿Cuáles son las tres frases de una buena explicación?", "Antes estaba, después quedó y cambió porque", "Son antes, después y causa."),
            ex("¿Qué es una causa?", "Lo que hace que algo cambie", "Explica el cambio."),
            ex("¿Por qué conviene usar datos?", "Porque dicen lo que realmente observé", "Los números se pueden comprobar."),
        ],
        "apply": [
            ex("El pan duro se ablanda al meterlo en agua. ¿Cuál es la causa?", "El agua", "El agua ablanda el pan."),
            ex("La mantequilla se ablanda al sol. ¿Cuál es la causa?", "El calor", "El sol da calor."),
            arith("Una barra de mantequilla medía 6 cm de alto y, tras un rato al sol, quedó de 2 cm de alto. ¿Cuántos centímetros bajó?", "6-2", "Se resta la altura final a la inicial.", " cm"),
        ],
        "reason": [
            ex("Luz dice que un papel mojado se rompe «porque sí». ¿Qué le falta a su explicación?", "La causa: el agua", "Hay que decir por qué cambió."),
            ex("Dos hielos: uno al sol tarda 20 minutos y otro a la sombra 50. ¿Qué conclusión sale?", "El sol derrite más rápido el hielo", "Hay más calor al sol."),
        ],
        "challenge": [
            ex("Escribe una explicación de tres frases de cómo una galleta se ablanda en leche.", "Antes estaba dura; después blanda; cambió porque le puse leche", "Sigue el esquema."),
            ex("Observas 3 cambios por fuerza y 2 por calor. ¿Cuántos cambios observaste?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("En casa se lava un jabón y se deja en agua; al día siguiente está blando y pegajoso. ¿Qué causa cambió el jabón?", "El agua", "El agua ablandó el jabón.")],
    selfcheck=[ex("¿Qué dos palabras dicen cómo estaba y cómo quedó?", "Antes y después", "Muestran el cambio."), ex("¿Qué causa derrite el hielo?", "El calor", "Lo pasa a agua."), ex("Después de observar un cambio, ¿cómo se llama lo que aprendo y escribo al final?", "Una conclusión", "Cierra la explicación con lo aprendido.")],
    open_task=task("Escribe una explicación de tres frases para cada historia. 1) Una esponja se aprieta y baja de 5 cm a 1 cm. 2) Un papel de color en la ventana pasa de rojo fuerte a rojo pálido en 14 días. 3) Un cubo de hielo al sol se derrite en 20 minutos.", "1) Antes medía 5 cm; después 1 cm; cambió por la fuerza. 2) Antes rojo fuerte; después pálido; cambió por la luz. 3) Antes hielo; después agua; cambió por el calor.", ["usa antes, después y causa", "cita un dato", "elige la causa correcta"], ["tres explicaciones", "tabla"], ["omitir la causa", "causa equivocada"], "Reconoce el esquema y pide citar el dato en cada explicación."),
    reinforce="Cuenta a alguien de tu casa un cambio que viste hoy en la cocina.",
    extend="Explica un cambio en el que participan dos causas, como calor y agua.",
)

# ---------------------------------------------------------------- OA 10
register(
    OA10, 1,
    materials="Este cuaderno con la historia de Luna y su cuaderno mojado, una lista de criterios, lápiz y colores.",
    use="Aprenderé a empezar un diseño pensando en el problema, en quién lo usa y en qué debe cumplir. Sirve para crear algo que de verdad ayude.",
    prior=["Sé las propiedades impermeable y flexible.", "Sé que los objetos se hacen con materiales."],
    explain=[
        "Un instrumento tecnológico es un objeto simple que ayuda a resolver un problema. Para diseñarlo, primero entiendes el problema. El de hoy: la lluvia moja el cuaderno de Luna cuando camina al colegio.",
        "Luego piensas en quién lo usa. Es Luna, una niña de 6 años. Debe poder ponerlo y sacarlo sola. Después escribes los criterios, que son lo que el instrumento debe cumplir: impermeable, flexible para cerrarlo, y hecho con materiales que ya hay en casa.",
        "Con criterios claros, sabrás si tu diseño funciona. Un criterio se puede comprobar. «Que sea lindo» es una opinión, pero «que no pase agua» se puede probar con gotas.",
    ],
    vocab=[("problema", "situación que queremos mejorar"), ("usuario", "persona que va a usar el objeto"), ("criterio", "condición que el objeto debe cumplir"), ("instrumento", "objeto simple que ayuda a hacer algo"), ("diseñar", "pensar y dibujar cómo será un objeto")],
    worked=[
        {"title": "Decir el problema y el usuario", "problem": "La lluvia moja el cuaderno de Luna. ¿Cuál es el problema y quién es el usuario?", "steps": ["Problema: el cuaderno se moja.", "Usuario: Luna, de 6 años."], "answer": "Problema: el cuaderno se moja. Usuario: Luna"},
        {"title": "Elegir criterios comprobables", "problem": "«Que sea lindo» o «que no deje pasar agua». ¿Cuál se puede comprobar con una prueba?", "steps": ["Lindo es una opinión.", "No dejar pasar agua se prueba con gotas."], "answer": "No dejar pasar agua"},
    ],
    mistakes=[
        {"wrong": "Empezar a construir sin saber el problema.", "why": "Se quiere partir rápido.", "fix": "Escribe primero el problema y el usuario."},
        {"wrong": "Poner criterios que son opiniones.", "why": "No se pueden comprobar.", "fix": "Elige criterios que se puedan probar."},
    ],
    tiers={
        "recovery": [
            ex("Luna se moja el cuaderno con la lluvia. ¿Cuál es el problema?", "El cuaderno se moja", "Es lo que se quiere resolver."),
            ex("¿Quién es el usuario del instrumento de la clase?", "Luna", "Ella lo va a usar."),
            ex("¿Es «impermeable» un criterio que se puede probar?", "Sí", "Se prueba con gotas de agua."),
        ],
        "understand": [
            ex("En el diseño de la funda, ¿qué es un criterio?", "Una condición que el objeto debe cumplir", "Dice cómo debe ser el objeto."),
            ex("¿Qué es un instrumento tecnológico simple?", "Un objeto simple que ayuda a resolver un problema", "Por ejemplo una funda."),
            ex("¿Por qué conviene saber quién es el usuario?", "Para que el diseño le sirva a esa persona", "Cambia lo que necesita."),
        ],
        "apply": [
            ex("Criterios: impermeable, fácil de poner, lindo. ¿Cuál no se puede comprobar?", "Lindo", "Es una opinión."),
            arith("Luna tiene 3 cuadernos y 2 libros que proteger. ¿Cuántas cosas debe proteger?", "3+2", "Se suman cuadernos y libros.", " cosas"),
            ex("Un usuario de 6 años debe cerrar la funda sola. ¿Qué criterio agregas?", "Fácil de abrir y cerrar", "Debe poder usarla sin ayuda."),
        ],
        "reason": [
            ex("Teo dice que la funda debe ser de papel porque es barato. ¿Qué criterio se pierde?", "Impermeable", "El papel absorbe agua."),
            ex("¿Por qué conviene escribir los criterios antes de construir?", "Para saber si el diseño funciona", "Se comprueba con ellos."),
        ],
        "challenge": [
            ex("Escribe un problema de tu casa que podría resolver un instrumento simple y quién lo usaría.", "Por ejemplo se cae el lápiz de la mesa; yo", "Dice problema y usuario."),
            ex("Un diseño cumple 3 criterios y le faltan 2. ¿Cuántos criterios tiene en total?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("En el colegio hay 4 niños que se mojan el cuaderno todos los días y 3 que lo hacen a veces. ¿Cuántos niños tienen el problema?", "7", "Cuatro más tres son siete.")],
    selfcheck=[ex("¿Qué se hace primero al diseñar?", "Entender el problema", "Eso guía todo."), ex("¿Qué es el usuario?", "La persona que usa el objeto", "Es quien lo necesita."), ex("¿Un criterio es una opinión?", "No", "Debe poder comprobarse.")],
    open_task=task("Elige uno de estos problemas y escribe el problema, el usuario y tres criterios que se puedan comprobar. A) El lápiz de Mateo rueda de la mesa. B) La merienda de Ema se aplasta en la mochila. C) La planta de Sol se cae con el viento.", "Problema B: la merienda se aplasta. Usuario: Ema. Criterios: rígido por fuera, cabe en la mochila, se abre fácil.", ["dice el problema", "dice el usuario", "escribe tres criterios comprobables"], ["tres líneas", "dibujo"], ["criterios que son opiniones", "no nombrar al usuario"], "Reconoce el problema y pide revisar que cada criterio se pueda probar."),
    reinforce="Elige un problema de tu casa y escribe quién lo tiene.",
    extend="Explica por qué dos personas distintas pueden necesitar un diseño distinto.",
)

register(
    OA10, 2,
    materials="Este cuaderno con los resultados de una prueba de cuatro materiales (bolsa plástica, papel, tela y cartón) y una tabla de criterios, lápiz y colores. En casa: los mismos materiales y una cuchara para las gotas, con un adulto.",
    use="Aprenderé a elegir materiales usando sus propiedades. Sirve para que mi diseño cumpla lo que necesita.",
    prior=["Sé el problema y los criterios del cuaderno de Luna.", "Sé que impermeable es no dejar pasar el agua."],
    explain=[
        "Elegir materiales con propósito es elegir los que tienen las propiedades que necesitas. Para la funda de Luna necesitamos que sea impermeable y flexible. Se prueba con 10 gotas de agua sobre cada material.",
        "Resultados de ejemplo: la bolsa plástica dejó pasar 0 gotas de 10. El papel dejó pasar 10 de 10. La tela dejó pasar 6 de 10. El cartón dejó pasar 8 de 10. Con estos datos, el mejor material es la bolsa plástica.",
        "También hay que mirar otros criterios. La bolsa plástica es flexible y se puede cerrar con cinta. El cartón es rígido y no se dobla bien. Un buen diseño une los datos de varias pruebas.",
    ],
    vocab=[("propiedad", "algo que se observa del material"), ("prueba", "ensayo con datos"), ("resultado", "dato que sale de la prueba"), ("propósito", "para qué se usa algo"), ("cinta", "tira pegajosa para unir")],
    worked=[
        {"title": "Leer los resultados", "problem": "De 10 gotas pasaron: bolsa 0, papel 10, tela 6, cartón 8. ¿Cuál deja pasar menos agua?", "steps": ["Comparo 0, 10, 6 y 8.", "0 es el menor."], "answer": "La bolsa plástica"},
        {"title": "Mirar otro criterio", "problem": "La bolsa es flexible. El cartón es rígido. Luna debe cerrar la funda. ¿Cuál sirve mejor?", "steps": ["La funda debe doblarse para cerrar.", "La bolsa se dobla; el cartón no."], "answer": "La bolsa plástica"},
    ],
    mistakes=[
        {"wrong": "Elegir el material por tenerlo a mano.", "why": "No se mira si cumple.", "fix": "Elige según las propiedades que necesitas."},
        {"wrong": "Usar una sola prueba para decidir todo.", "why": "Hay más de un criterio.", "fix": "Revisa impermeable, flexible y fácil de usar."},
    ],
    tiers={
        "recovery": [
            ex("La bolsa dejó pasar 0 gotas de 10. ¿Es impermeable?", "Sí", "No dejó pasar agua."),
            ex("El papel dejó pasar 10 de 10 gotas. ¿Es impermeable?", "No", "Dejó pasar todo."),
            ex("El cartón es rígido. ¿Sirve para una funda que se dobla?", "No", "No se dobla bien."),
        ],
        "understand": [
            ex("¿Por qué se usan 10 gotas en cada material?", "Para que la prueba sea igual para todos", "Así se compara justo."),
            ex("¿Qué dos propiedades necesita la funda?", "Impermeable y flexible", "Son los criterios."),
            ex("¿Qué es un resultado?", "Un dato que sale de la prueba", "Dice qué pasó."),
        ],
        "apply": [
            arith("La tela dejó pasar 6 gotas de 10. ¿Cuántas gotas no pasaron?", "10-6", "Se resta lo que pasó del total.", " gotas"),
            arith("El cartón dejó pasar 8 gotas de 10. ¿Cuántas gotas más que la tela dejó pasar el cartón?", "8-6", "Se resta lo que pasó por la tela.", " gotas"),
            ex("Resultados: bolsa 0, papel 10, tela 6, cartón 8. Ordena de menos a más gotas que pasan.", "Bolsa, tela, cartón, papel", "0, 6, 8 y 10."),
        ],
        "reason": [
            ex("Sofi dice que la tela es mejor porque es suave. ¿Qué dato la contradice?", "Dejó pasar 6 gotas de 10", "No es impermeable."),
            ex("Si la bolsa no se pega bien, ¿qué criterio puede fallar?", "Que no deje pasar agua por la unión", "La cinta debe sellar."),
        ],
        "challenge": [
            ex("Propón un material de casa que pueda ser impermeable y flexible.", "Por ejemplo una bolsa de plástico limpia", "Cumple los dos criterios."),
            ex("Pruebas 4 materiales y cada uno con 10 gotas. ¿Cuántas gotas usas en total?", "40", "Diez más diez más diez más diez son cuarenta."),
        ],
    },
    context=[ex("Para el cobertor del cuaderno hay 5 bolsas plásticas y 3 de papel en casa. ¿Cuántas bolsas hay?", "8", "Cinco más tres son ocho.")],
    selfcheck=[ex("¿Qué material no dejó pasar gotas?", "La bolsa plástica", "Pasaron 0 de 10."), ex("¿Cuántas gotas por material?", "10", "Siempre las mismas."), ex("¿Se decide con una sola prueba?", "No", "Hay varios criterios.")],
    open_task=task("Con estos resultados de 10 gotas: papel aluminio 0, tela de algodón 7, papel 10, bolsa de plástico 0. Elige dos materiales que cumplan impermeable y explica cuál usarías para una funda que debe doblarse. Dato extra: el aluminio se rompe al doblar muchas veces; la bolsa se dobla sin romperse.", "Impermeables: aluminio y bolsa (0 de 10). Usaría la bolsa porque se dobla sin romperse y el aluminio sí se rompe.", ["nombra los impermeables con datos", "elige una con razón", "usa el criterio de doblar"], ["tabla", "frase"], ["elegir la tela", "no usar el dato del doblez"], "Reconoce el criterio doble y pide justificar con el dato extra."),
    reinforce="Con ayuda de un adulto, prueba una bolsa y un papel con gotas.",
    extend="Explica por qué se usan las mismas gotas en todos los materiales.",
)

register(
    OA10, 3,
    materials="Este cuaderno con las medidas de un cuaderno (21 cm de largo y 15 cm de ancho) y un dibujo con cuadrícula para completar, lápiz y colores.",
    use="Aprenderé a dibujar mi diseño antes de construirlo, con medidas y nombres. Sirve para evitar errores y gastar menos material.",
    prior=["Sé los criterios de la funda.", "Sé medir con una regla."],
    explain=[
        "Un dibujo de diseño muestra cómo será el objeto antes de hacerlo. Debe tener tres cosas: las medidas, los nombres de las partes y los materiales. Así otra persona puede hacerlo.",
        "El cuaderno de Luna mide 21 cm de largo y 15 cm de ancho. La funda debe ser un poco más grande, por ejemplo 2 cm más en cada medida: 23 cm de largo y 17 cm de ancho. Si es más pequeña, el cuaderno no entra.",
        "También anota los pasos: 1) Medir la bolsa. 2) Cortar con tijeras de punta redonda (un adulto ayuda). 3) Pegar los bordes con cinta. 4) Dejar una abertura para meter el cuaderno. Los pasos ordenados ayudan a no equivocarse.",
    ],
    vocab=[("medida", "número con unidad que dice qué tan grande es algo"), ("dibujo de diseño", "dibujo que muestra cómo será un objeto"), ("parte", "pieza del objeto"), ("abertura", "lugar por donde se mete algo"), ("paso", "cada acción que se hace en orden")],
    worked=[
        {"title": "Calcular las medidas", "problem": "Cuaderno: 21 cm de largo y 15 cm de ancho. La funda será 2 cm más grande en cada medida. ¿Cuánto mide?", "steps": ["21 + 2 = 23 cm de largo.", "15 + 2 = 17 cm de ancho."], "answer": "23 cm de largo y 17 cm de ancho"},
        {"title": "Ordenar los pasos", "problem": "Ordena: pegar los bordes, medir la bolsa, cortar con adulto, dejar la abertura.", "steps": ["Primero medir.", "Luego cortar.", "Después pegar.", "Dejar la abertura al final del pegado."], "answer": "Medir, cortar, pegar los bordes y dejar la abertura"},
    ],
    mistakes=[
        {"wrong": "Dibujar sin medidas.", "why": "Se piensa que el dibujo basta.", "fix": "Escribe el largo y el ancho con cm."},
        {"wrong": "Hacer la funda del mismo tamaño que el cuaderno.", "why": "No se deja espacio.", "fix": "Agrega 2 cm en cada medida."},
    ],
    tiers={
        "recovery": [
            ex("¿Qué tres cosas debe tener un dibujo de diseño?", "Medidas, nombres de partes y materiales", "Así se puede construir."),
            ex("¿Para qué sirve dejar una abertura?", "Para meter el cuaderno", "Si no, no entra."),
            ex("¿Con qué se corta con seguridad en esta clase?", "Con tijeras de punta redonda y un adulto", "Es lo seguro para tu edad."),
        ],
        "understand": [
            ex("¿Por qué la funda debe ser más grande que el cuaderno?", "Para que el cuaderno entre", "El cuaderno necesita espacio para entrar."),
            ex("¿Para qué sirven los pasos ordenados?", "Para no equivocarse al construir", "Cada acción tiene su lugar."),
            ex("¿Qué es una parte del objeto?", "Una pieza del objeto", "Por ejemplo la abertura."),
        ],
        "apply": [
            arith("El cuaderno mide 21 cm de largo. La funda será 2 cm más larga. ¿Cuánto mide el largo de la funda?", "21+2", "Se suman los 2 cm de espacio.", " cm"),
            arith("El cuaderno mide 15 cm de ancho. La funda será 2 cm más ancha. ¿Cuánto mide el ancho de la funda?", "15+2", "Se suman los 2 cm de espacio.", " cm"),
            ex("Pasos: pegar bordes, medir, cortar. ¿Cuál va primero?", "Medir", "Antes de cortar se mide."),
        ],
        "reason": [
            ex("Un niño cortó la bolsa de 21 cm por 15 cm, igual que el cuaderno. ¿Qué problema habrá?", "El cuaderno no entrará bien", "Falta espacio para meterlo."),
            ex("Dos diseñadores dibujan la misma funda, uno con medidas y otro sin ellas. ¿Quién tiene un mejor dibujo y por qué?", "El que tiene medidas, porque se puede construir igual", "Las medidas guían."),
        ],
        "challenge": [
            ex("Un libro mide 25 cm de largo y 18 cm de ancho. Si la funda es 2 cm más grande, ¿cuánto mide su largo y ancho?", "27 cm y 20 cm", "Veinticinco más dos y dieciocho más dos."),
            ex("Escribe tres pasos para construir una funda.", "Medir, cortar con adulto y pegar con cinta", "Son pasos ordenados."),
        ],
    },
    context=[ex("Para la funda necesitas cinta en los 2 lados largos de 23 cm. ¿Cuántos centímetros de cinta usas para los dos lados?", "46 cm", "Veintitrés más veintitrés son cuarenta y seis.")],
    selfcheck=[ex("¿Qué número lleva un dibujo de diseño?", "Las medidas", "Dicen el tamaño."), ex("¿Cuánto más grande es la funda?", "2 cm en cada medida", "Eso deja espacio al cuaderno."), ex("¿Qué va primero: cortar o medir?", "Medir", "Se mide antes de cortar.")],
    open_task=task("Dibuja el diseño de una funda para un libro que mide 20 cm de largo y 14 cm de ancho. Calcula la funda con 2 cm más en cada medida, escribe el material (bolsa plástica) y 4 pasos ordenados.", "Funda de 22 cm de largo y 16 cm de ancho, bolsa plástica. Pasos: 1 medir, 2 cortar con adulto, 3 pegar los bordes, 4 dejar la abertura.", ["calcula las medidas", "nombra el material", "ordena cuatro pasos"], ["dibujo con medidas", "lista de pasos"], ["olvidar el espacio extra", "pasos desordenados"], "Reconoce el cálculo y pide ordenar los pasos."),
    reinforce="Dibuja tu diseño con las medidas escritas.",
    extend="Calcula cuánta cinta necesitas para cerrar tres lados de tu funda.",
)

register(
    OA10, 4,
    materials="Este cuaderno con los resultados de una prueba de tres prototipos, una pauta de criterios, lápiz y colores. En casa: una bolsa plástica, cinta y una cuchara para las gotas.",
    use="Aprenderé a construir un prototipo y a probarlo con datos. Sirve para saber si mi diseño funciona.",
    prior=["Sé hacer un dibujo de diseño con medidas.", "Sé que se prueba con gotas de agua."],
    explain=[
        "Un prototipo es la primera versión de tu objeto. No tiene que quedar perfecto. Sirve para probar si funciona. Luna construye una funda con una bolsa plástica de 23 cm por 17 cm y cinta en los bordes.",
        "La prueba se hace con 4 cucharadas de agua que se vierten sobre la funda con un papel seco adentro. Se mira cuánto se mojó el papel. En los datos de ejemplo: prototipo A, papel seco; prototipo B, 3 cm de papel mojado; prototipo C, 8 cm mojado.",
        "Compara con los criterios: ¿es impermeable?, ¿se cierra fácil? Si algún criterio falla, anota por qué. El prototipo A funcionó mejor porque su cinta sellaba bien los bordes.",
    ],
    vocab=[("prototipo", "primera versión de un objeto para probar"), ("verter", "echar un líquido"), ("sellar", "cerrar para que no pase el agua"), ("funcionar", "hacer lo que se necesita"), ("falla", "parte que no funciona")],
    worked=[
        {"title": "Leer la prueba", "problem": "Papel mojado: prototipo A 0 cm, B 3 cm, C 8 cm. ¿Cuál funcionó mejor?", "steps": ["Menos papel mojado es mejor.", "A tiene 0 cm."], "answer": "El prototipo A"},
        {"title": "Buscar la falla", "problem": "El prototipo C se mojó 8 cm. Tenía la cinta suelta en una esquina. ¿Qué falló?", "steps": ["La cinta suelta deja pasar agua.", "El borde no estaba sellado."], "answer": "El borde sin sellar dejó pasar agua"},
    ],
    mistakes=[
        {"wrong": "Pensar que el prototipo debe quedar perfecto a la primera.", "why": "Se piensa que fallar es malo.", "fix": "Una prueba que falla muestra qué mejorar."},
        {"wrong": "Probar cada prototipo con una cantidad distinta de agua.", "why": "Así no se compara justo.", "fix": "Usa 4 cucharadas en todos."},
    ],
    tiers={
        "recovery": [
            ex("¿El prototipo es la primera o la última versión?", "La primera", "Sirve para probar."),
            ex("Prototipo A: papel seco. ¿Funcionó?", "Sí", "No pasó agua."),
            ex("Prototipo C: 8 cm de papel mojado. ¿Funcionó bien?", "No", "Se mojó mucho."),
        ],
        "understand": [
            ex("¿Por qué se usan 4 cucharadas de agua en cada prueba?", "Para comparar de manera justa", "Todos reciben igual."),
            ex("¿Qué significa sellar un borde?", "Cerrarlo para que no pase agua", "La cinta lo sella."),
            ex("¿Qué se hace si un criterio falla?", "Se anota la falla y se busca por qué", "Sirve para mejorar."),
        ],
        "apply": [
            arith("El prototipo B mojó 3 cm de papel y el C 8 cm. ¿Cuántos centímetros más mojó el C?", "8-3", "Se resta lo que mojó el B.", " cm"),
            arith("Pruebas 3 prototipos con 4 cucharadas cada uno. ¿Cuántas cucharadas de agua usas en total?", "4+4+4", "Se suman las 4 cucharadas de cada prototipo.", " cucharadas"),
            ex("Orden de mejor a peor según el papel mojado: A 0 cm, B 3 cm, C 8 cm. ¿Qué lugar tiene B?", "El segundo", "Está entre A y C."),
        ],
        "reason": [
            ex("Si el prototipo C tiene cinta suelta, ¿qué cambio le harías?", "Pegar bien la cinta en la esquina", "Así se sella el borde."),
            ex("Ema dice que su prototipo está bien porque se ve lindo. ¿Qué le falta?", "Una prueba con datos", "Lindo no prueba que funcione."),
        ],
        "challenge": [
            ex("Escribe un criterio y cómo lo probarías.", "Impermeable; con 4 cucharadas de agua", "La prueba entrega un dato."),
            ex("Hay 2 prototipos que funcionan y 3 que fallan. ¿Cuántos prototipos hay?", "5", "Dos más tres son cinco."),
        ],
    },
    context=[ex("Un grupo prueba 5 fundas. Con las mismas cucharadas, 3 no mojan el papel y 2 sí. ¿Cuántas fundas funcionan?", "3", "Las que no mojan el papel funcionan.")],
    selfcheck=[ex("¿Para qué sirve un prototipo?", "Para probar si funciona", "Es una primera versión."), ex("¿Cuánta agua se usa por prueba?", "4 cucharadas", "Siempre la misma."), ex("¿Qué se hace con una falla?", "Se anota y se mejora", "Ayuda a aprender.")],
    open_task=task("Usa estos datos de tres fundas probadas con 4 cucharadas de agua: Funda 1, 0 cm de papel mojado, se cierra fácil. Funda 2, 2 cm de papel mojado, se cierra fácil. Funda 3, 0 cm de papel mojado, no se puede cerrar. Escribe cuál elegirías según los criterios impermeable y fácil de cerrar, y por qué.", "Elegiría la funda 1 porque no se mojó (0 cm) y se cierra fácil. La 2 se mojó 2 cm y la 3 no se cierra.", ["revisa los dos criterios", "elige con datos", "explica por qué descarta las otras"], ["tabla", "frase"], ["elegir la 3 sin ver que no cierra", "no usar los cm"], "Reconoce que cumple ambos criterios y pide nombrar por qué descarta cada otra."),
    reinforce="Con ayuda de un adulto, prueba una funda con 4 cucharadas de agua.",
    extend="Explica qué cambiarías si tu prototipo se moja por una esquina.",
)

register(
    OA10, 5,
    materials="Este cuaderno con los datos del primer y segundo prototipo, un esquema para presentar en cuatro frases, lápiz y colores.",
    use="Aprenderé a mejorar un diseño con lo que aprendí en la prueba y a contarlo a otras personas. Sirve para explicar mi trabajo con datos.",
    prior=["Sé hacer y probar un prototipo.", "Sé usar datos para decidir."],
    explain=[
        "Mejorar es cambiar una parte del diseño para que funcione mejor. Si la funda dejó pasar agua por una esquina, la mejora puede ser poner más cinta en esa esquina. Cambia una sola cosa a la vez para saber qué ayudó.",
        "Datos de ejemplo: el prototipo 1 mojó 8 cm de papel. Después de poner cinta extra, el prototipo 2 mojó 1 cm. Se mojó 7 cm menos. La mejora funcionó, aunque todavía no es perfecta.",
        "Para comunicar, usa cuatro frases: 1) El problema era… 2) Hice… 3) Los resultados fueron… 4) Para mejorar yo… Así otra persona entiende y puede aprender de tu trabajo.",
    ],
    vocab=[("mejorar", "cambiar algo para que funcione mejor"), ("comunicar", "contar a otros lo que hice"), ("resultado", "dato de la prueba"), ("cambio", "diferencia que hago al diseño"), ("presentación", "forma de mostrar mi trabajo")],
    worked=[
        {"title": "Medir la mejora", "problem": "Prototipo 1 mojó 8 cm. Prototipo 2 mojó 1 cm. ¿Cuánto mejoró?", "steps": ["8 menos 1 son 7.", "Mojó 7 cm menos."], "answer": "Mejoró 7 cm"},
        {"title": "Contar en cuatro frases", "problem": "Presenta la funda de Luna.", "steps": ["El problema era que la lluvia mojaba el cuaderno.", "Hice una funda de bolsa con cinta.", "Se mojó 1 cm de papel.", "Para mejorar pondría más cinta."], "answer": "Cuatro frases: problema, qué hice, resultado y mejora"},
    ],
    mistakes=[
        {"wrong": "Cambiar tres cosas a la vez.", "why": "No se sabe cuál ayudó.", "fix": "Cambia una cosa y vuelve a probar."},
        {"wrong": "Presentar sin decir los resultados.", "why": "Se piensa que se nota.", "fix": "Incluye el número, por ejemplo «se mojó 1 cm»."},
    ],
    tiers={
        "recovery": [
            ex("¿Mejorar es empeorar o cambiar para funcionar mejor?", "Cambiar para funcionar mejor", "Es la definición de la clase."),
            ex("El prototipo 1 mojó 8 cm y el 2 mojó 1 cm. ¿Cuál es mejor?", "El 2", "Se mojó menos."),
            ex("¿Cuántas frases tiene la presentación de la clase?", "4", "Problema, qué hice, resultado y mejora."),
        ],
        "understand": [
            ex("¿Por qué conviene cambiar una sola cosa a la vez?", "Para saber qué cambio ayudó", "Si cambias tres, no se sabe."),
            ex("¿Qué dice la frase «El problema era…»?", "Qué quería resolver", "Presenta el problema."),
            ex("¿Para qué sirve comunicar un diseño?", "Para que otros entiendan y aprendan", "Se comparte el trabajo."),
        ],
        "apply": [
            arith("Prototipo 1 mojó 8 cm y prototipo 2 mojó 1 cm. ¿Cuántos centímetros menos mojó el 2?", "8-1", "Se resta lo que mojó el segundo.", " cm"),
            arith("Pusiste 2 cintas extra en un lado y 2 en el otro. ¿Cuántas cintas extra pusiste?", "2+2", "Se suman las cintas.", " cintas"),
            ex("Escribe la frase de resultados: el prototipo 2 mojó 1 cm de papel. ¿Cuál es el dato?", "1 cm", "Es el número de la prueba."),
        ],
        "reason": [
            ex("Si la mejora redujo 8 cm a 1 cm, ¿puede decirse que la cinta ayudó?", "Sí, porque mojó 7 cm menos", "El único cambio fue la cinta."),
            ex("Nico cambió la cinta y el material a la vez y mojó menos. ¿Qué no sabe?", "Cuál de los dos cambios ayudó", "Cambió dos cosas."),
        ],
        "challenge": [
            ex("Escribe una mejora para una funda que se cierra con dificultad.", "Por ejemplo agregar una lengüeta de plástico para tirar", "Esa lengüeta facilita cerrar la funda."),
            ex("Hay 3 mejoras que funcionaron y 2 que no. ¿Cuántas mejoras se probaron?", "5", "Tres más dos son cinco."),
        ],
    },
    context=[ex("Hoy presentan sus fundas 4 grupos y mañana presentan 3 grupos. ¿Cuántos grupos presentan en total?", "7", "Cuatro más tres son siete grupos.")],
    selfcheck=[ex("¿Cuántas cosas cambias al mejorar?", "Una", "Así sabes qué ayudó."), ex("¿Qué incluye una buena presentación?", "El problema, qué hice, el resultado y la mejora", "Son las cuatro frases."), ex("¿Qué dato incluyes?", "El número de la prueba", "Respalda lo que dices.")],
    open_task=task("Escribe una presentación de cuatro frases con estos datos: problema, la lluvia moja el cuaderno de Luna. Hiciste una funda de bolsa plástica con cinta. La primera prueba mojó 8 cm de papel y la segunda con cinta extra mojó 1 cm. Para mejorar, harías la abertura más fácil de cerrar.", "El problema era que la lluvia mojaba el cuaderno de Luna. Hice una funda de bolsa plástica con cinta. La prueba 2 mojó 1 cm, 7 cm menos que la primera. Para mejorar haría una abertura más fácil de cerrar.", ["escribe las cuatro frases", "incluye el dato 8 cm y 1 cm", "propone una mejora"], ["cuatro frases", "dibujo"], ["omitir el dato", "cambiar varias cosas a la vez"], "Reconoce el esquema y pide incluir los dos números en la tercera frase."),
    reinforce="Cuéntale a alguien de tu casa cómo mejoraste tu diseño.",
    extend="Explica qué probarías después de la mejora para estar más seguro.",
)
