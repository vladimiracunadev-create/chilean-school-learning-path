"""Participación y argumentación en democracia (electivo HC, 3.º y 4.º medio): OAC-06 (evaluar críticamente argumentaciones: relaciones lógicas, legitimidad de las evidencias, pertinencia y alcances en la comunidad), clases 1 a 6. Casos ficticios y textos originales."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, ficha o tabla está escrito en el enunciado. "
             "Todos los casos son ficticios (comuna «Villa Alerce», «Liceo Los Pinos») y los datos son de ejemplo: no son cifras reales. "
             "Las posturas se presentan con sus razones y sin tomar partido: se evalúa la calidad de los argumentos, no a las personas ni a los bandos. "
             "Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O6 = "LL-PADM-3y4-OAC-06"

# ============================================================ OAC-06, clase 1
F = ("Ficha 1 (rúbrica y argumento de ejemplo). Criterios para evaluar un argumento: 1) relaciones lógicas: ¿la conclusión se sigue de las premisas?; 2) legitimidad de la evidencia: ¿tiene fuente, método y cantidad suficiente?; "
     "3) pertinencia: ¿trata del tema y del propósito?; 4) alcance en la comunidad: ¿a quiénes afecta y cuánto?; 5) claridad y respeto: ¿se entiende y trata bien a las personas? "
     "Argumento de ejemplo: «Si el liceo cierra el kiosco, bajará el consumo de azúcar. Un registro de ejemplo muestra que el consumo de azúcar es alto en el liceo. Por lo tanto, hay que cerrar el kiosco.»")
build(
    O6, 1, F,
    use="Aprenderé cinco criterios para evaluar críticamente un argumento (relaciones lógicas, legitimidad de la evidencia, pertinencia, alcance en la comunidad y claridad y respeto) y a aplicarlos a un ejemplo.",
    prior=["Sé reconstruir un argumento en premisas y conclusión.", "Sé evaluar una fuente con aceptabilidad, suficiencia y pertinencia.", "Conozco formas válidas e inválidas de razonar."],
    explain=[
        "Evaluar críticamente un argumento no es criticar por criticar: es examinarlo con criterios claros y llegar a un juicio razonado. Cinco criterios ayudan. Las relaciones lógicas: si las premisas fueran verdaderas, ¿se seguiría la conclusión? La legitimidad de la evidencia: ¿tiene fuente identificable, método y cantidad suficiente? La pertinencia: ¿trata del tema y sirve al propósito? El alcance: ¿a quiénes afecta y cuánto? Y la claridad y el respeto.",
        "Aplicados al ejemplo del kiosco: la premisa 1 dice que cerrar el kiosco baja el consumo de azúcar, pero esa relación no está respaldada con datos. La premisa 2 muestra que hay un problema, pero no que cerrar el kiosco sea la mejor solución. Falta una premisa implícita: que cerrar el kiosco es la mejor forma de bajar el consumo y que sus costos son aceptables. Así se ve que la conclusión no se sigue con firmeza.",
        "El alcance también importa: cerrar el kiosco afecta a quienes trabajan en él y a quienes lo usan para otras compras. Un buen evaluador considera esas consecuencias. Su juicio final no es solo «bueno» o «malo»: señala qué criterios cumple el argumento, cuáles no y qué se podría hacer para mejorarlo. Evaluar con generosidad, es decir, leyendo primero la mejor versión del argumento, hace que la crítica sea más justa.",
    ],
    vocab=[("evaluar críticamente", "examinar un argumento con criterios y llegar a un juicio razonado"), ("relación lógica", "vínculo por el que la conclusión se sigue de las premisas"), ("legitimidad de la evidencia", "calidad de la fuente, el método y la cantidad de datos"), ("alcance", "personas afectadas y magnitud del efecto"), ("juicio razonado", "valoración que explica sus criterios"), ("lectura generosa", "interpretar primero la mejor versión del argumento")],
    worked=[
        ("Aplicar el criterio lógico", "En el argumento del kiosco, ¿qué falta para que la conclusión se siga?",
         ["Las premisas muestran que el consumo es alto y que cerrar el kiosco lo bajaría.", "Falta la premisa de que cerrar el kiosco es la mejor forma de bajar el consumo y que sus costos son aceptables."],
         "Una premisa que justifique que cerrar es la mejor opción y con costos aceptables"),
        ("Aplicar el criterio de alcance", "¿A quiénes afectaría cerrar el kiosco además de quienes compran azúcar?",
         ["Afecta a quienes trabajan en el kiosco y a quienes compran allí otros productos.", "Un argumento debe considerar a todas las personas afectadas."],
         "A quienes trabajan en el kiosco y a quienes compran otros productos"),
    ],
    mistakes=[("Evaluar solo si la conclusión nos gusta.", "Se mezcla la postura personal con la calidad del argumento.", "Evalúa primero con los cinco criterios y recién después decide tu postura."),
              ("Decir «es un mal argumento» sin explicar qué criterio falla.", "Se emite un juicio sin razones.", "Nombra el criterio y la razón concreta de la falla.")],
    T=[
        ("abc", "{F} ¿Qué criterio pregunta si la conclusión se sigue de las premisas?", "Relaciones lógicas", "Alcance en la comunidad", "Claridad y respeto", "Ese criterio evalúa la conexión entre premisas y conclusión."),
        ("abc", "{F} ¿Qué criterio pregunta a quiénes afecta una decisión y cuánto?", "Alcance en la comunidad", "Relaciones lógicas", "Legitimidad de la evidencia", "Se refiere a los efectos sobre las personas."),
        ("abc", "{F} ¿Qué criterio revisa si hay fuente, método y cantidad suficiente de datos?", "Legitimidad de la evidencia", "Pertinencia", "Claridad y respeto", "Evalúa la calidad de lo que respalda las premisas."),
        ("abc", "{F} En el ejemplo, ¿qué premisa muestra que hay un problema?", "El consumo de azúcar es alto en el liceo", "Cerrar el kiosco baja el consumo", "Hay que cerrar el kiosco", "Describe una situación de partida sin decir qué hacer."),
        ("abc", "{F} ¿Qué premisa no está respaldada con datos en el ejemplo?", "Que cerrar el kiosco bajará el consumo de azúcar", "Que el consumo es alto", "Que el kiosco existe", "El registro solo muestra el nivel de consumo, no el efecto del cierre."),
        ("abc", "{F} ¿Qué se podría agregar para mejorar la legitimidad de la evidencia?", "Datos de lo que ocurrió en otros liceos que cerraron el kiosco, con fuente", "Una frase enfática", "La opinión de un desconocido", "Aporta datos verificables sobre el efecto del cierre."),
        ("ab", "{F} ¿Cuál es un juicio razonado sobre el argumento?", "Tiene un problema real, pero no muestra que cerrar el kiosco sea la mejor solución ni considera sus costos", "Es un mal argumento", "El primero nombra qué criterios cumple y cuáles no; el segundo no explica su juicio."),
        ("abc", "{F} Una estudiante dice: «El argumento es débil porque no me gusta cerrar el kiosco». ¿Qué falla?", "Mezcla su postura con la evaluación y no nombra ningún criterio", "Aplica bien el criterio lógico", "Evalúa la evidencia", "La evaluación debe basarse en criterios, no en preferencias."),
        ("abc", "¿Qué es una lectura generosa de un argumento?", "Interpretar primero su mejor versión antes de criticarlo", "Aceptarlo sin evaluarlo", "Buscar solo fallas", "Así la crítica se dirige a lo más fuerte del argumento."),
        ("abc", "{F} ¿Qué otra premisa implícita razonable tendría el argumento del kiosco?", "Que el consumo alto de azúcar justifica prohibir su venta", "Que los kioscos son antiguos", "Que el azúcar es dulce", "Conecta el problema con la solución propuesta."),
        ("abc", "{F} Se cambia la conclusión por «hay que estudiar medidas para bajar el consumo de azúcar». ¿Cómo mejora el argumento?", "Se ajusta mejor a lo que las premisas respaldan", "Se vuelve falso", "Pierde pertinencia", "La conclusión se sigue mejor del dato del problema."),
        ("abc", "{F} Un participante dice: «Hay que escuchar también a quienes trabajan en el kiosco». ¿Qué criterio aplica?", "Alcance en la comunidad", "Relaciones lógicas", "Legitimidad de la evidencia", "Considera a quienes se verían afectados."),
        ("abc", "Un texto agrede a quienes piensan distinto con insultos, aunque tenga datos. ¿Qué criterio incumple?", "Claridad y respeto", "Relaciones lógicas", "Alcance", "El trato respetuoso es parte de una buena argumentación."),
    ],
    ctx=("abc", "Una concejala ficticia propone eliminar el estacionamiento frente a un colegio «porque un registro muestra que hay muchos autos a la hora de salida». ¿Qué le falta para evaluarla bien?", "Mostrar que eliminarlo reduce el riesgo y considerar a quienes lo usan", "Más adjetivos", "Otra frase de apoyo sin datos", "Falta evidencia del efecto de la medida y su alcance."),
    sc=[
        ("En Participación y argumentación: ¿cuáles son los cinco criterios para evaluar un argumento?", "Relaciones lógicas, evidencia, pertinencia, alcance y claridad y respeto", "Permiten juzgar con razones y no por simpatía."),
        ("¿Qué es una lectura generosa?", "Interpretar primero la mejor versión del argumento", "Se critica la versión más fuerte, no una caricatura."),
        ("¿Qué debe incluir un juicio razonado?", "Qué criterios cumple, cuáles no y cómo mejorar", "Un juicio sin criterios no ayuda a mejorar."),
    ],
    op=("Elige uno. Argumento 1: «Si el liceo exige uniforme completo, habrá más orden. El orden es importante porque mejora el aprendizaje. Por lo tanto, hay que exigir uniforme completo.» "
        "Argumento 2: «Si el municipio coloca más basureros, habrá menos basura en la calle. Un conteo de ejemplo muestra 30 bolsas semanales de basura en la plaza. Por lo tanto, hay que instalar basureros.» "
        "Evalúa el argumento elegido con los cinco criterios (una oración por criterio) y escribe un juicio razonado final de dos oraciones y una mejora concreta.",
        "Argumento 2. Lógica: la conclusión se sigue en parte, pero falta mostrar que más basureros reducen la basura. Evidencia: el conteo muestra el problema, no el efecto. Pertinencia: trata del tema. Alcance: afecta a quienes usan la plaza y a quienes limpian. Respeto: correcto. Juicio: identifica un problema real, pero no prueba que la medida lo resuelva. Mejora: añadir datos de plazas con basureros.",
        ["aplica los cinco criterios con razones", "distingue lo que el argumento sí respalda", "propone una mejora concreta", "emite un juicio razonado"],
        ["tabla de cinco criterios, juicio de dos oraciones y mejora"],
        ["decir «es bueno» o «es malo» sin criterios", "mezclar la postura personal con la evaluación", "no proponer mejoras"],
        "Pregunta: «¿qué criterio falla más y por qué?». Si no puede responder, vuelve a las definiciones."),
    reinforce="Aplica el criterio de alcance al argumento del kiosco y escribe a quiénes afecta y de qué modo.",
    extend="Explica por qué una persona puede estar de acuerdo con la conclusión de un argumento y aun así evaluar que está mal construido.",
)

# ============================================================ OAC-06, clase 2
F = ("Ficha 2 (columna de opinión de ejemplo, diario mural del Liceo Los Pinos). «Los recreos del liceo deberían acortarse a diez minutos. "
     "Un conteo de ejemplo de inspectoría registró conflictos en 2 de cada 10 recreos del último mes. "
     "Además, un recreo largo es una pérdida de tiempo, porque yo prefiero estar en clases. "
     "Por eso hay que acortar los recreos.»")
build(
    O6, 2, F,
    use="Aprenderé a evaluar críticamente un texto real o de ejemplo paso a paso: reconstruir el argumento, revisar evidencia y relaciones lógicas, considerar su alcance y juzgar con razones.",
    prior=["Sé reconstruir un argumento.", "Conozco los cinco criterios de evaluación.", "Sé calcular porcentajes simples."],
    explain=[
        "Evaluar un texto argumentativo se hace en pasos. Primero se reconstruye el argumento: se separan la conclusión y las premisas, y se anota lo implícito. Segundo, se revisa cada premisa: ¿es verdadera o aceptable, y su evidencia es legítima? Tercero, se revisa la conexión: ¿las premisas apoyan la conclusión? Cuarto, se considera la pertinencia y el alcance. Y quinto, se emite un juicio con razones.",
        "En la columna de ejemplo, la conclusión es acortar los recreos. Hay dos premisas: que hay conflictos en 2 de cada 10 recreos (20 %) y que un recreo largo es una pérdida de tiempo porque el autor prefiere estar en clases. La primera es un dato con fuente, pero no muestra que los conflictos se deban a la duración del recreo; falta la relación. La segunda es una preferencia personal que no puede generalizarse.",
        "Un buen evaluador reconoce lo que el texto hace bien, como citar un conteo de inspectoría, y señala lo que le falta: datos que relacionen duración y conflictos y consideración de quienes usan el recreo para descansar o comer. No basta decir que la columna está equivocada: se indica qué evidencia o razonamiento se necesitaría para sostenerla. El respeto exige criticar el argumento y no a su autor.",
    ],
    vocab=[("premisa aceptable", "premisa que se puede admitir con buenas razones"), ("relación causal", "vínculo por el que una cosa produce otra"), ("preferencia personal", "gusto de quien habla, que no basta como evidencia general"), ("columna de opinión", "texto que defiende una postura con argumentos"), ("tasa", "cantidad por cada cierto total, como 2 de cada 10"), ("criticar el argumento", "examinar las razones, no atacar a quien las dice")],
    worked=[
        ("Reconstruir la columna", "Escribe las premisas y la conclusión de la columna de la ficha.",
         ["Premisa 1: hubo conflictos en 2 de cada 10 recreos. Premisa 2: un recreo largo es una pérdida de tiempo, porque el autor prefiere estar en clases.", "Conclusión: hay que acortar los recreos a diez minutos."],
         "P1 y P2, por lo tanto acortar los recreos"),
        ("Revisar la conexión", "¿Por qué la premisa 1 no basta para sostener la conclusión?",
         ["Muestra que hay conflictos, pero no que se deban a la duración del recreo.", "Falta un dato que relacione la duración con la cantidad de conflictos."],
         "No relaciona la duración con los conflictos"),
    ],
    mistakes=[("Aceptar una cifra como si probara una causa.", "Se confunde que exista un problema con que una medida lo resuelva.", "Pregunta qué dato muestra que la medida cambiaría el problema."),
              ("Criticar al autor en vez del argumento.", "Se evalúa a la persona y no sus razones.", "Dirige la crítica a las premisas, la evidencia y la conexión.")],
    T=[
        ("abc", "{F} ¿Cuál es la conclusión de la columna?", "Hay que acortar los recreos a diez minutos", "Hubo conflictos en 2 de cada 10 recreos", "El autor prefiere estar en clases", "Se anuncia con «por eso» al final."),
        ("=", "{F} Si hubo 40 recreos en el mes, ¿en cuántos hubo conflictos según el conteo de 2 de cada 10?", "40*2//10", "Dos de cada diez equivale a un quinto de los 40 recreos.", " recreos"),
        ("abc", "{F} ¿Qué porcentaje de los recreos tuvo conflictos?", "20 %", "2 %", "10 %", "2 de cada 10 equivale a 20 de cada 100."),
        ("abc", "{F} ¿Qué tipo de premisa es «yo prefiero estar en clases»?", "Una preferencia personal", "Un dato con fuente", "Una norma oficial", "Expresa un gusto de quien habla."),
        ("abc", "{F} ¿Qué falta para relacionar el dato de conflictos con la conclusión?", "Datos que muestren que acortar el recreo reduce los conflictos", "Más adjetivos", "Otra opinión personal", "Se necesita evidencia del efecto de la medida."),
        ("abc", "{F} ¿Qué hace bien la columna?", "Cita un conteo de inspectoría como evidencia", "Prueba su conclusión con certeza", "Considera a todas las personas afectadas", "Aporta un dato con fuente identificable."),
        ("ab", "{F} ¿Cuál es una crítica dirigida al argumento y no a la persona?", "La premisa 2 es una preferencia personal que no puede generalizarse", "El autor siempre quiere estar en clases porque es aburrido", "La primera examina las razones; la segunda ataca al autor."),
        ("abc", "{F} ¿A quiénes afectaría acortar los recreos y la columna no considera?", "A quienes usan el recreo para descansar, comer o hacer actividad física", "A nadie", "Solo a quienes están en clases", "Un buen argumento considera efectos para todas las personas afectadas."),
        ("abc", "{F} ¿Qué evidencia sería más pertinente para apoyar la conclusión?", "Comparar los conflictos en recreos de distinta duración, con datos de varios meses", "Repetir el conteo del mismo mes", "Conocer la hora de término de las clases", "Relaciona la duración del recreo con la cantidad de conflictos."),
        ("abc", "{F} Un compañero dice: «El autor es un flojo, así que nada de lo que dice sirve». ¿Cuál es la mejor respuesta?", "Hay que evaluar las razones del texto, no la persona", "Tienes razón, descartemos todo", "Entonces su dato es verdadero", "La crítica debe dirigirse a las premisas y su conexión."),
        ("abc", "{F} Un compañero cita, como apoyo, un conteo de conflictos ocurridos en las fiestas de un barrio. ¿Qué es esa evidencia para la columna?", "No pertinente: no trata de los recreos del liceo", "Más fuerte, porque cuenta más conflictos", "Una premisa implícita", "No describe cómo funcionan los recreos del liceo, que es el tema de la columna."),
        ("abc", "{F} ¿Qué conclusión se sigue mejor de las premisas?", "Hay que estudiar por qué ocurren los conflictos en los recreos", "Hay que eliminar los recreos", "Hay que acortar los recreos a cinco minutos", "Es la conclusión que el dato apoya sin dar un salto."),
        ("abc", "{F} ¿Cuál es la mejor forma de comunicar la crítica al autor de la columna?", "«Tu dato es útil, pero falta mostrar que acortar el recreo reduce los conflictos»", "«Tu texto es un desastre»", "«No hables de lo que no sabes»", "Reconoce lo valioso y señala lo que falta de modo respetuoso."),
    ],
    ctx=("abc", "En una carta ficticia a la junta de vecinos se lee: «Hay que prohibir las bicicletas en la plaza. Dos vecinos se asustaron al verlas pasar. Yo odio las bicicletas». ¿Qué evaluación es más razonable?", "Las premisas son anécdotas y una preferencia personal; faltan datos de accidentes y una relación con la prohibición", "El argumento es perfecto", "Es falso porque la carta es ficticia", "No hay evidencia suficiente que respalde una prohibición."),
    sc=[
        ("En Participación y argumentación: ¿cuál es el primer paso para evaluar un texto argumentativo?", "Reconstruir su argumento", "Antes de juzgar hay que identificar premisas y conclusión."),
        ("¿Por qué una preferencia personal no basta como evidencia general?", "Porque expresa un gusto de quien habla, no un hecho verificable", "No se puede extender a toda la comunidad."),
        ("¿Qué se critica al evaluar un argumento?", "Las razones, la evidencia y la conexión, no a la persona", "Criticar a la persona es otro asunto."),
    ],
    op=("Elige uno. Texto 1: «Hay que alargar el recreo a veinte minutos. Un registro de ejemplo muestra que 8 de cada 10 estudiantes consultados dicen estar cansados al finalizar la mañana. Yo me siento más feliz con recreos largos. Por eso hay que alargarlos.» "
        "Texto 2: «Hay que instalar cámaras en los pasillos. En el último mes hubo 3 pérdidas de objetos. Además mi amigo dice que en su colegio las cámaras sirven. Por lo tanto, hay que instalarlas.» "
        "Reconstruye el argumento, evalúa cada premisa y la conexión, indica el alcance y escribe una recomendación para mejorar el texto, con un tono respetuoso.",
        "Texto 2. Conclusión: instalar cámaras. Premisas: 3 pérdidas en un mes; un amigo dice que sirven. Evaluación: 3 pérdidas es un dato, pero no muestra cuánto reducirían las cámaras; el testimonio del amigo es un caso. Alcance: afecta la privacidad de todos. Recomendación: pedir datos de otros liceos y considerar alternativas.",
        ["reconstruye el argumento con fidelidad", "evalúa premisas y conexión con razones", "considera el alcance", "formula una recomendación respetuosa"],
        ["reconstrucción, evaluación de premisas, alcance y recomendación"],
        ["evaluar a la persona y no el argumento", "aceptar un dato como prueba de una medida", "no considerar a quienes afecta"],
        "Pregunta: «¿qué dato mostraría que esta medida sirve?». Si no sabe, ayúdale a plantearlo."),
    reinforce="Reconstruye en dos líneas el argumento de la columna de la ficha, marcando cuál premisa es un dato y cuál una preferencia.",
    extend="Escribe una versión mejorada de la columna con evidencia pertinente y un matiz.",
)

# ============================================================ OAC-06, clase 3
F = ("Ficha 3 (cuatro intervenciones de ejemplo en un debate). Intervención 1: «No hay que escuchar su propuesta de reciclaje: él siempre llega tarde a clases.» "
     "Intervención 2: «O se prohíben las pelotas en el patio, o habrá accidentes todos los días.» "
     "Intervención 3: «Si dejamos que el curso elija la música de la actividad, mañana elegirán las notas y el año próximo no habrá profesores.» "
     "Intervención 4: Persona P: «Propongo una zona de silencio en el recreo.» Persona Q: «P quiere que nadie pueda hablar nunca.»")
build(
    O6, 3, F,
    use="Aprenderé a reconocer cuatro errores frecuentes de razonamiento (ataque personal, falso dilema, pendiente resbaladiza y hombre de paja), a explicar por qué fallan y a responder sin caer en ellos.",
    prior=["Sé evaluar relaciones lógicas.", "Sé reconstruir un argumento.", "Sé que criticar el argumento no es criticar a la persona."],
    explain=[
        "Una falacia es un error de razonamiento que parece convincente pero no apoya su conclusión. Reconocerlas ayuda a evaluar argumentos y a mejorar los propios. El ataque personal rechaza una propuesta por características de quien la dice, sin responder a sus razones. El falso dilema presenta solo dos opciones cuando existen más. La pendiente resbaladiza afirma que un paso llevará inevitablemente a una cadena de consecuencias extremas, sin mostrar cada vínculo.",
        "El hombre de paja deforma la postura de la otra persona para refutarla con facilidad: en lugar de responder a «una zona de silencio» responde a «nadie podrá hablar nunca». Cada falacia evita el trabajo de responder a las razones reales. Por eso la respuesta adecuada es volver al argumento original: pedir razones, mostrar otras opciones, preguntar por cada paso de una cadena o reformular fielmente lo que se dijo.",
        "Etiquetar una falacia no refuta una conclusión: que un argumento sea falaz no prueba que su conclusión sea falsa, solo que esa razón no la sostiene. Tampoco se usa la etiqueta como arma. Se explica con calma qué falla, por ejemplo: «tu razón se refiere a quien propone, no a la propuesta», y se invita a ofrecer razones mejores. La finalidad es mejorar la conversación, no ganar puntos.",
    ],
    vocab=[("falacia", "error de razonamiento que parece convincente pero no sostiene su conclusión"), ("ataque personal", "rechazar una propuesta por características de quien la dice"), ("falso dilema", "presentar solo dos opciones habiendo más"), ("pendiente resbaladiza", "afirmar sin mostrar vínculos que un paso lleva a consecuencias extremas"), ("hombre de paja", "deformar la postura ajena para refutarla con facilidad"), ("reformular", "decir con otras palabras y fielmente lo que otra persona sostiene")],
    worked=[
        ("Reconocer una falacia", "¿Qué falacia es la intervención 2?",
         ["Presenta solo dos opciones: prohibir pelotas o accidentes diarios.", "Ignora otras opciones, como turnos o zonas de juego: falso dilema."],
         "Falso dilema"),
        ("Responder sin caer en la falacia", "¿Cómo responderías a la intervención 1?",
         ["Se vuelve a la propuesta de reciclaje y se piden sus razones.", "«Que él llegue tarde no responde a su propuesta. ¿Qué razones da el reciclaje en el liceo?»"],
         "Volver a las razones de la propuesta"),
    ],
    mistakes=[("Pensar que si un argumento es falaz, su conclusión es falsa.", "Se confunde el error del razonamiento con la verdad de la conclusión.", "Di que esa razón no basta y pide razones mejores."),
              ("Usar el nombre de la falacia como insulto.", "Se busca desacreditar a la persona.", "Explica con calma qué falla y cómo mejorarlo.")],
    T=[
        ("abc", "{F} ¿Qué falacia es la intervención 1?", "Ataque personal", "Falso dilema", "Hombre de paja", "Rechaza la propuesta por una característica de quien la dice."),
        ("abc", "{F} ¿Qué falacia es la intervención 3?", "Pendiente resbaladiza", "Ataque personal", "Falso dilema", "Encadena consecuencias extremas sin mostrar los vínculos."),
        ("abc", "{F} ¿Qué falacia es la intervención 4 de Q?", "Hombre de paja", "Pendiente resbaladiza", "Falso dilema", "Deforma «zona de silencio» en «nadie hablará nunca»."),
        ("abc", "{F} ¿Qué característica de quien habla usa la intervención 1 para rechazar su propuesta?", "Que siempre llega tarde a clases", "Que propone reciclar", "Que es estudiante del liceo", "Rechaza la propuesta por un rasgo de la persona y no por sus razones."),
        ("abc", "{F} ¿Cómo se puede reformular fielmente la propuesta de P?", "P propone una zona de silencio en el recreo", "P prohíbe hablar a todos siempre", "P no quiere recreos", "Es lo que P dijo, sin añadir ni deformar."),
        ("ab", "{F} Para responder a la intervención 3, ¿qué conviene hacer?", "Preguntar cómo se llegaría de elegir música a eliminar profesores, paso por paso", "Responder que quien lo dijo es poco inteligente", "Se pide mostrar cada vínculo de la cadena de consecuencias."),
        ("abc", "¿Una falacia prueba que la conclusión del argumento es falsa?", "No: solo muestra que esa razón no la sostiene", "Sí, siempre", "Sí, si es un ataque personal", "La conclusión puede ser verdadera por otras razones."),
        ("abc", "«Esa estudiante dice que hay que ahorrar agua, pero ella tiene un huerto con riego, así que no la escuchemos». ¿Qué falacia es?", "Ataque personal", "Falso dilema", "Pendiente resbaladiza", "Se rechaza la propuesta por conducta de quien la dice."),
        ("abc", "«O dejamos que todos hablen sin límite de tiempo, o se acaba la libertad de expresión». ¿Qué falacia es?", "Falso dilema", "Hombre de paja", "Ataque personal", "Ignora opciones intermedias, como turnos de palabra."),
        ("abc", "Alguien propone limitar el uso de celulares en clases y otro dice «quiere prohibirnos hasta respirar». ¿Qué falacia es?", "Hombre de paja", "Pendiente resbaladiza", "Falso dilema", "Exagera la postura para rechazarla fácilmente."),
        ("abc", "«Si dejan que las bicicletas entren a la plaza, luego entrarán motos, autos y camiones, y se acabará la plaza». ¿Cuál es el problema?", "No muestra por qué un paso llevaría inevitablemente al siguiente", "Menciona vehículos", "Es muy corta", "La cadena de consecuencias no está demostrada."),
        ("abc", "{F} ¿Cuál es la mejor respuesta a Q?", "«Yo propuse una zona de silencio en el recreo, no prohibir hablar siempre»", "«Eres injusto»", "«Hablemos de otra cosa»", "Reformula fielmente la postura y corrige la deformación."),
        ("abc", "¿Cuál es el uso adecuado del término «falacia» en un debate?", "Explicar con calma qué razón falla y pedir razones mejores", "Gritarlo para ganar puntos", "Usarlo para insultar", "El objetivo es mejorar la conversación."),
    ],
    ctx=("abc", "En un consejo de curso ficticio, una persona dice: «No hay que aprobar su propuesta del festival, porque es de los que nunca vienen a las reuniones». ¿Qué debe hacer quien modera?", "Pedir que se discuta el contenido de la propuesta y sus razones", "Aprobar la propuesta", "Rechazar la propuesta", "Se vuelve al fondo del argumento, no a quien lo presenta."),
    sc=[
        ("En Participación y argumentación: ¿qué es un falso dilema?", "Presentar solo dos opciones habiendo más", "Ignora las alternativas intermedias que sí existen en la situación."),
        ("¿Qué es un hombre de paja?", "Deformar la postura ajena para refutarla con facilidad", "Se responde a una versión débil de lo que se dijo."),
        ("¿Qué significa que un argumento falaz no prueba que la conclusión sea falsa?", "Que esa razón no la sostiene, pero puede haber otras", "La conclusión podría ser verdadera por otras razones."),
    ],
    op=("Elige uno. Escribe una respuesta respetuosa y razonada (tres a cinco oraciones) a una de estas intervenciones. A: «No tomes en cuenta su propuesta de ampliar la biblioteca: ella nunca ha leído un libro.» "
        "B: «O cerramos la calle completa o seguimos con los accidentes de siempre.» C: «Quiere moderar el uso del celular, o sea, quiere quitarnos todo.» "
        "Nombra la falacia, explica por qué falla y reformula la postura original o ofrece las opciones omitidas.",
        "B. Falso dilema: ignora opciones como cerrar solo algunas horas, poner reductores de velocidad o ensanchar veredas. Respuesta: «Hay más opciones además de cerrar la calle completa: cerrar solo los sábados o poner reductores. Evaluemos con datos de accidentes cuál sirve más».",
        ["identifica la falacia correcta", "explica por qué falla", "ofrece una respuesta que vuelve a las razones", "mantiene un tono respetuoso"],
        ["respuesta escrita con la falacia nombrada y explicada"],
        ["usar la etiqueta como insulto", "no reformular ni ofrecer alternativas", "atacar a la persona"],
        "Pregunta: «¿qué razón real queda sin responder?». Si ninguna, la respuesta se quedó en la etiqueta."),
    reinforce="Inventa una intervención con hombre de paja sobre el uso del patio y escribe la reformulación fiel.",
    extend="Explica cuándo conviene no nombrar la falacia en un debate y solo preguntar por las razones.",
)

# ============================================================ OAC-06, clase 4
F = ("Ficha 4 (cinco intervenciones de ejemplo). Intervención 1: «Hablé con dos compañeros de 3.º B y no leen; por lo tanto, nadie en el liceo lee.» "
     "Intervención 2: «Desde que pintaron las salas de verde, subió la asistencia; por eso el color verde sube la asistencia.» "
     "Intervención 3: «Todos usan esa aplicación, así que debe ser buena.» "
     "Intervención 4: «Un cantante famoso dice que estas zapatillas son las mejores para correr maratones, así que lo son.» "
     "Intervención 5: «Un registro de ejemplo muestra 12 accidentes en el cruce en un año. Piensen en cada persona que cruzó con miedo: hace falta un semáforo.»")
build(
    O6, 4, F,
    use="Aprenderé a reconocer otras falacias frecuentes (generalización apresurada, falsa causa, apelación a la popularidad y a una autoridad no pertinente) y a distinguir una apelación a la emoción legítima de una falaz.",
    prior=["Sé reconocer ataque personal, falso dilema, pendiente resbaladiza y hombre de paja.", "Sé distinguir correlación y causa.", "Sé evaluar una autoridad."],
    explain=[
        "La generalización apresurada concluye algo sobre todos a partir de muy pocos casos: dos compañeros que no leen no permiten decir que nadie lee. La falsa causa (después de esto, por lo tanto a causa de esto) supone que, porque algo ocurrió después de otra cosa, la primera fue la causa. La asistencia pudo subir por otros motivos. La apelación a la popularidad dice que algo es bueno porque muchos lo usan; la apelación a una autoridad no pertinente cita a alguien famoso que no tiene experticia en ese tema.",
        "La emoción no es siempre una falacia. Los argumentos tratan de asuntos que importan a las personas, y reconocer cómo los afecta una decisión es legítimo. Se vuelve falaz cuando la emoción reemplaza a la evidencia o a las razones. En la intervención 5, hay un dato (12 accidentes) y una invitación a considerar cómo vivieron las personas; si el texto solo dijera «piensen en el miedo», sería débil. Cuando la emoción acompaña a una razón verificable, es legítima.",
        "Al evaluar, conviene preguntarse qué se está pidiendo creer y con qué razón. Para corregir una falacia, se pide más evidencia (¿cuántos casos?), se proponen explicaciones alternativas (¿qué otra cosa cambió?), se verifica la pertinencia de la autoridad (¿es experta en esto?) y se pregunta por la calidad del producto o idea, más allá de cuántos lo usen. Así se mantiene el diálogo y se mejora el argumento.",
    ],
    vocab=[("generalización apresurada", "concluir sobre todos con muy pocos casos"), ("falsa causa", "suponer que lo que ocurrió antes es la causa de lo que ocurrió después"), ("apelación a la popularidad", "decir que algo es bueno solo porque muchos lo hacen o usan"), ("autoridad no pertinente", "cita de alguien famoso sin experticia en el tema"), ("apelación a la emoción", "recurso a lo que sienten las personas, que puede ser legítimo o falaz"), ("explicación alternativa", "otra causa posible de un mismo hecho")],
    worked=[
        ("Reconocer la falacia", "¿Qué falacia es la intervención 2 (el color verde y la asistencia)?",
         ["Dice que, como la asistencia subió después de pintar, el color la causó.", "No considera otras causas posibles: falsa causa."],
         "Falsa causa"),
        ("Distinguir la emoción legítima", "¿Por qué la intervención 5 no es una falacia emocional?",
         ["Incluye un dato verificable: 12 accidentes en un año.", "La referencia a la experiencia de las personas acompaña a la razón y no la reemplaza."],
         "Porque la emoción acompaña a una evidencia"),
    ],
    mistakes=[("Rechazar todo argumento que mencione emociones.", "Se piensa que la emoción siempre reemplaza a la razón.", "Revisa si hay también evidencia o razones verificables."),
              ("Concluir que dos hechos se relacionan solo porque ocurrieron seguidos.", "Se ignora que pudo haber otra causa.", "Pregunta qué otra cosa cambió en ese tiempo.")],
    T=[
        ("abc", "{F} ¿Qué falacia es la intervención 1?", "Generalización apresurada", "Falsa causa", "Apelación a la popularidad", "Concluye sobre todos con solo dos casos."),
        ("abc", "{F} ¿Qué falacia es la intervención 3?", "Apelación a la popularidad", "Generalización apresurada", "Falsa causa", "Afirma que es buena porque todos la usan."),
        ("abc", "{F} ¿Qué falacia es la intervención 4?", "Apelación a una autoridad no pertinente", "Falsa causa", "Falso dilema", "Un cantante no tiene experticia en zapatillas para maratones."),
        ("{F} ¿Con cuántos casos concluye la intervención 1 algo sobre «nadie en el liceo»?", "Dos", "Habló con dos compañeros y de ahí concluye sobre todo el liceo."),
        ("abc", "{F} ¿Qué otra causa posible explicaría el alza de asistencia en la intervención 2?", "Un cambio de horario o una campaña de asistencia al mismo tiempo", "El color verde es más bonito", "Que las salas se pintaron", "Una explicación alternativa distinta de la pintura."),
        ("abc", "{F} ¿Qué pregunta ayuda a corregir la intervención 1?", "¿A cuántas personas consultaste y cómo las elegiste?", "¿Por qué lees tanto?", "¿Qué libros te gustan?", "Examina el tamaño y la selección de la muestra."),
        ("abc", "{F} ¿Qué haría pertinente a la autoridad de la intervención 4?", "Que fuera un especialista en entrenamiento o calzado deportivo, sin conflicto de interés", "Que tuviera más seguidores", "Que cantara mejor", "La experticia en el tema es la condición."),
        ("abc", "{F} ¿Qué parte de la intervención 5 se puede comprobar con un registro?", "Que hubo 12 accidentes en el cruce en un año", "Que las personas cruzaron con miedo", "Que hace falta un semáforo", "El conteo de accidentes es un dato; el miedo y la necesidad son valoraciones."),
        ("ab", "{F} Si la intervención 5 dijera solo «piensen en el miedo de la gente: hace falta un semáforo», sería:", "Una apelación emocional sin evidencia, más débil", "Una evidencia verificable", "Sin dato ni razón, la emoción reemplaza al argumento."),
        ("abc", "Un anuncio dice: «Más de un millón de personas eligieron esta marca, así que es la mejor». ¿Qué falla?", "La cantidad de personas no prueba la calidad", "Usa cifras", "Habla de marcas", "La popularidad de algo no equivale a que tenga calidad."),
        ("abc", "«Después de instalar el bebedero, hubo menos peleas; por lo tanto, el bebedero redujo las peleas». ¿Qué debe preguntarse?", "Si cambió otra cosa en ese tiempo que explique la baja", "Si el bebedero es bonito", "Si la gente toma agua", "Hay que descartar otras explicaciones posibles antes de afirmar causa."),
        ("abc", "«Un compañero tuvo mala suerte con una tienda; por lo tanto, todas esas tiendas son malas». ¿Qué falacia es?", "Generalización apresurada", "Falsa causa", "Apelación a la popularidad", "Un caso no permite concluir sobre todas las tiendas."),
        ("abc", "¿Cuándo una apelación a la emoción es legítima?", "Cuando acompaña a razones o datos verificables", "Cuando reemplaza a los datos", "Nunca", "La emoción tiene lugar si no sustituye la evidencia."),
    ],
    ctx=("abc", "Una vecina ficticia dice: «Desde que cambiaron la ruta de la micro, bajaron las ventas del almacén; por lo tanto, el cambio de ruta bajó las ventas». ¿Qué conviene preguntar?", "Si en ese mismo periodo cambió otra cosa, como el clima o una feria", "Si la micro es azul", "Si el almacén es grande", "Descartar otras causas posibles evita una falsa causa."),
    sc=[
        ("En Participación y argumentación: ¿qué es una generalización apresurada?", "Concluir sobre todos con muy pocos casos", "Los casos son insuficientes para sostener la conclusión general."),
        ("¿Qué es una falsa causa?", "Suponer que lo que ocurrió antes causó lo que ocurrió después", "La secuencia no basta para probar la causa."),
        ("¿Cuándo una apelación a la emoción es falaz?", "Cuando reemplaza a la evidencia o a las razones", "La emoción puede acompañar, pero no sustituir, las razones."),
    ],
    op=("Elige uno. Escribe una crítica respetuosa de cuatro a seis oraciones a una de estas intervenciones. A: «Mi primo probó esa dieta y no funcionó; así que ninguna dieta funciona.» B: «Todos los cursos de 2.º usan el mismo cuaderno, así que es el mejor.» "
        "C: «Después de que el liceo cambió la hora del timbre subieron las notas; el timbre sube las notas.» "
        "Nombra la falacia, explica por qué falla, propone qué evidencia haría falta y formula una conclusión más ajustada.",
        "A. Generalización apresurada: un solo caso no permite hablar de todas las dietas. Evidencia necesaria: datos de muchas personas con seguimiento. Conclusión ajustada: a una persona no le funcionó esa dieta; no se puede concluir sobre las demás.",
        ["nombra la falacia correcta", "explica por qué falla", "indica la evidencia necesaria", "propone una conclusión ajustada"],
        ["texto de cuatro a seis oraciones con la falacia nombrada"],
        ["no explicar por qué falla", "usar la etiqueta como burla", "proponer una conclusión igual de general"],
        "Pregunta: «¿qué dato te haría cambiar de opinión?». Si no hay ninguno, la crítica se quedó incompleta."),
    reinforce="Escribe una versión legítima de una apelación a la emoción sobre la seguridad de un cruce, agregando un dato de ejemplo.",
    extend="Explica por qué «todos lo hacen» puede ser una razón débil y, sin embargo, útil como información en algunos casos.",
)

# ============================================================ OAC-06, clase 5
F = ("Ficha 5 (mensaje en cadena, de ejemplo). «URGENTE: el municipio de Villa Alerce cerrará la plaza todos los fines de semana desde el próximo mes. Compártelo con todos tus contactos. Lo dijo un amigo de un concejal.» "
     "Pasos de verificación: 1) identificar quién lo dice y cómo lo sabe; 2) buscar el documento o aviso oficial original; 3) revisar fecha y contexto; 4) preguntar a la oficina responsable; 5) no reenviar hasta verificar.")
build(
    O6, 5, F,
    use="Aprenderé a diseñar una acción democrática de respuesta a un argumento o mensaje poco sólido: verificar la información, formular preguntas críticas y responder constructivamente sin difundir lo no comprobado.",
    prior=["Sé evaluar la legitimidad de una fuente.", "Sé reconocer falacias frecuentes.", "Sé redactar un mensaje respetuoso."],
    explain=[
        "Responder a un argumento poco sólido es una forma de participar. Cuando llega un mensaje que afirma un hecho público, conviene verificarlo antes de reaccionar o reenviarlo. Se averigua quién lo dice y cómo lo sabe, se busca el documento oficial original, se revisa la fecha y el contexto, y se pregunta a la oficina responsable. Un mensaje que pide compartir con urgencia, sin fuente, merece más cuidado, no menos.",
        "Para responder en forma constructiva se formulan preguntas críticas, que invitan a revisar: ¿cuál es la fuente?, ¿qué documento lo respalda?, ¿desde qué fecha?, ¿a quién afecta? Estas preguntas no atacan a nadie; piden razones. Si el mensaje resulta correcto, se informa con la fuente. Si es falso o dudoso, se comunica con respeto, sin humillar a quien lo difundió, y se indica dónde está la información verificada.",
        "La acción democrática también considera sus propios límites: nadie puede verificarlo todo, y a veces la información oficial tarda. Mientras se espera, se evita difundir lo que no está comprobado y se comunica con prudencia: «he oído esto, pero no está verificado». Verificar y corregir contribuye a que la comunidad decida con información fiable y confíe en las conversaciones públicas.",
    ],
    vocab=[("verificar", "comprobar si algo es cierto usando fuentes confiables"), ("fuente original", "documento o aviso del cual proviene la información"), ("pregunta crítica", "pregunta que pide razones o evidencia sin atacar a nadie"), ("mensaje en cadena", "mensaje que pide ser compartido sin indicar fuente"), ("oficina responsable", "entidad con la responsabilidad del asunto"), ("información fiable", "información respaldada por fuentes verificables")],
    worked=[
        ("Ordenar los pasos", "¿Qué se debe hacer primero con el mensaje de la ficha?",
         ["Antes de reaccionar o compartir hay que saber quién lo dice y cómo lo sabe.", "El mensaje solo cita «un amigo de un concejal»: no es una fuente verificable."],
         "Identificar quién lo dice y cómo lo sabe"),
        ("Formular una pregunta crítica", "Escribe una pregunta crítica para quien envió el mensaje.",
         ["La pregunta debe pedir fuente sin acusar.", "«¿Hay algún aviso oficial del municipio que lo respalde y desde cuándo?»"],
         "¿Hay algún aviso oficial del municipio que lo respalde?"),
    ],
    mistakes=[("Reenviar el mensaje «por si acaso» antes de verificarlo.", "Se piensa que el riesgo de no avisar es mayor que el de difundir un error.", "Verifica primero y comunica con la fuente."),
              ("Responder burlándose de quien lo envió.", "Se busca ganar en vez de aclarar.", "Pregunta por la fuente y entrega información verificada con respeto.")],
    T=[
        ("abc", "{F} ¿Qué dato del mensaje es una fuente débil?", "«Lo dijo un amigo de un concejal»", "El nombre de la comuna", "La palabra «plaza»", "No identifica un documento ni a la persona que lo sabe."),
        ("abc", "{F} ¿Qué hace sospechoso al mensaje?", "Pide compartirlo con urgencia sin mostrar documento", "Menciona la plaza", "Está escrito en mayúsculas", "La urgencia sin fuente es una señal de alerta."),
        ("abc", "{F} ¿Qué paso corresponde después de identificar quién lo dice?", "Buscar el documento o aviso oficial original", "Reenviarlo a todos", "Ignorarlo para siempre", "Es el paso 2 de la verificación."),
        ("abc", "{F} ¿A quién conviene preguntar para verificar si se cerrará la plaza?", "A la oficina responsable de la municipalidad", "A quien más lo reenvió", "A un vecino al azar", "Es quien decide sobre el uso de la plaza."),
        ("abc", "{F} ¿Cuál es una buena pregunta crítica sobre quién sabe de verdad lo del cierre?", "¿Quién del municipio lo dijo y en qué documento consta?", "¿Por qué difundes mentiras?", "¿Cuántos contactos tienes?", "Pide identificar a la persona y el documento, sin atacar."),
        ("abc", "{F} Si la oficina responsable dice que no hay tal decisión, ¿qué conviene hacer?", "Comunicarlo con la fuente y sin burlarse de nadie", "Callar para evitar problemas", "Culpar a quien lo envió", "Corregir con respeto ayuda a que la comunidad se informe bien."),
        ("ab", "{F} Mientras se verifica, ¿qué es más prudente?", "No reenviarlo hasta saber si es cierto", "Reenviarlo por si acaso", "Difundir sin comprobar puede propagar un error."),
        ("abc", "{F} Si un amigo te manda el mensaje y dice «yo no sé si es cierto», ¿cuál es una buena respuesta?", "«Gracias; voy a revisar si hay un aviso oficial antes de compartirlo»", "«Compártelo igual»", "«Eres un mentiroso»", "Reconoce el aviso y propone verificar."),
        ("abc", "{F} ¿Por qué verificar la fecha del mensaje?", "Porque puede ser antiguo o referirse a otro contexto", "Porque las fechas son importantes en sí", "Porque da más color", "Un mensaje antiguo puede circular como si fuera actual."),
        ("abc", "{F} Si el aviso oficial dice que se cerrará la plaza solo una tarde de feria, ¿qué corrección es adecuada?", "Que no será todos los fines de semana, sino una tarde de feria", "Que se cerrará siempre", "Que no existe la feria", "Se corrige la afirmación con lo que el documento dice."),
        ("abc", "¿Qué límite reconoce una acción democrática responsable?", "Que no se puede verificar todo y que la información oficial a veces tarda", "Que nunca se puede verificar", "Que todo se puede verificar al instante", "Reconocer límites evita la falsa certeza."),
        ("abc", "Un mensaje dice «científicos aseguran que esto es peligroso» sin nombres ni estudio. ¿Cuál es el primer paso?", "Buscar quién lo dice y en qué estudio o documento se basa", "Creerlo porque dice científicos", "Descartarlo sin mirar", "Es la forma de saber si hay una fuente legítima."),
        ("abc", "{F} ¿Qué respuesta combina verificación y respeto?", "«Revisé con la oficina del municipio y aún no hay aviso; compartiré el enlace oficial cuando lo publiquen»", "«Todos son mentirosos»", "«No me escribas más»", "Informa con fuente y muestra buena voluntad."),
    ],
    ctx=("abc", "Un grupo de apoderados ficticio recibe un mensaje que dice «Mañana no hay clases por decisión del ministerio» sin firma. ¿Qué es lo más adecuado?", "Confirmar en el comunicado oficial del liceo antes de avisar a otras familias", "Avisar a todos de inmediato", "No hacer nada nunca", "Hay que verificar con la fuente oficial antes de difundir."),
    sc=[
        ("En Participación y argumentación: ¿qué significa verificar un mensaje?", "Comprobar si es cierto con fuentes confiables", "No es lo mismo que aceptarlo o rechazarlo sin mirar."),
        ("¿Qué es una pregunta crítica?", "Una pregunta que pide razones o evidencia sin atacar a nadie", "Invita a revisar el argumento con respeto."),
        ("¿Qué conviene hacer con un mensaje urgente sin fuente?", "No reenviarlo y buscar la fuente original", "La urgencia sin fuente es señal de cuidado."),
    ],
    op=("Elige uno. Mensaje 1 (de ejemplo): «El liceo cobrará $20.000 por el uso de la biblioteca desde la próxima semana; lo dijo una compañera que escuchó a un profesor». Mensaje 2 (de ejemplo): «Cerrarán la feria para siempre; pásalo». "
        "Escribe un plan de cinco pasos para verificar el mensaje, una pregunta crítica y una respuesta respetuosa para quien lo compartió, considerando un límite (por ejemplo, que la oficina no responda a tiempo).",
        "Mensaje 2. Pasos: 1) ver quién lo dice; 2) buscar el aviso oficial de la municipalidad; 3) revisar fecha y contexto; 4) preguntar en la oficina de ferias; 5) no reenviar hasta tener respuesta. Pregunta crítica: ¿hay un aviso oficial que lo respalde? Respuesta: «Gracias por avisar; voy a confirmar con el municipio antes de compartirlo». Límite: si no responden, comunicaré que no está confirmado.",
        ["propone cinco pasos de verificación coherentes", "formula una pregunta crítica no agresiva", "redacta una respuesta respetuosa", "declara un límite o una precaución"],
        ["plan de cinco pasos, una pregunta y una respuesta"],
        ["reenviar antes de verificar", "burlarse de quien compartió", "no declarar límites"],
        "Pregunta: «¿qué harías si nadie te responde?». Pide una precaución concreta."),
    reinforce="Escribe tres preguntas críticas distintas que podrías hacer ante un mensaje en cadena.",
    extend="Explica cómo una comunidad podría crear una costumbre de verificar antes de compartir en un chat de curso.",
)

# ============================================================ OAC-06, clase 6
F = ("Ficha 6 (dos columnas de ejemplo sobre el horario de salida del liceo). Columna X: razona con cuidado, cita un conteo de ejemplo de atrasos y reconoce límites, pero su propuesta afecta solo a un curso. "
     "Columna Y: usa una generalización apresurada y un ataque personal, pero su propuesta afectaría a todo el liceo y a las familias. "
     "Rúbrica: relaciones lógicas, evidencia, pertinencia, alcance, claridad y respeto; cada criterio vale de 0 a 2 puntos. "
     "Puntajes de ejemplo: X: lógica 2, evidencia 2, pertinencia 2, alcance 1, claridad y respeto 2. Y: lógica 0, evidencia 1, pertinencia 1, alcance 2, claridad y respeto 0.")
build(
    O6, 6, F,
    use="Aprenderé a evaluar los efectos y límites de una argumentación: ponderar sus alcances en la comunidad, usar una rúbrica con criterio y reconocer los límites de la propia evaluación.",
    prior=["Conozco los cinco criterios de evaluación.", "Sé reconocer falacias.", "Sé sumar puntajes y comparar."],
    explain=[
        "Evaluar un argumento no termina en encontrar fallas. También importa su alcance: qué tan grande es el efecto en la comunidad si se acepta. Un argumento débil que lleva a una decisión que afecta a mucha gente merece más escrutinio que uno débil sobre un asunto menor. A la vez, un argumento muy bien construido puede referirse a un asunto de pocas personas. Por eso se evalúa la calidad del argumento y la importancia de lo que está en juego, sin mezclarlas.",
        "Una rúbrica ayuda a ordenar el juicio: cada criterio recibe un puntaje y se suman. Pero el total no lo dice todo. Un argumento con puntaje alto en lógica y evidencia, y bajo en alcance, es sólido y acotado. Uno con alcance alto y lógica baja es riesgoso: puede decidir mucho sobre bases débiles. Por eso se leen los puntajes por criterio y no solo el total.",
        "La evaluación también tiene límites. Quien evalúa puede tener sesgos, falta de información sobre el contexto o una lectura apresurada. La buena evaluación declara esos límites, usa la lectura generosa y se somete a revisión de otras personas. Además, un argumento mal construido puede tener una conclusión que luego se apoye con mejores razones: criticar no es descartar, sino invitar a mejorar.",
    ],
    vocab=[("alcance", "cantidad de personas afectadas y magnitud del efecto"), ("escrutinio", "examen cuidadoso de algo"), ("rúbrica", "pauta que asigna puntajes a cada criterio"), ("sesgo del evaluador", "tendencia que afecta el juicio de quien evalúa"), ("revisión por pares", "revisión del juicio por otras personas"), ("sólido y acotado", "bien construido y de efecto limitado")],
    worked=[
        ("Sumar la rúbrica", "Con los puntajes de la ficha, ¿cuál es el total de la columna X?",
         ["Se suman los cinco criterios: 2 + 2 + 2 + 1 + 2.", "2 + 2 + 2 = 6; 6 + 1 = 7; 7 + 2 = 9."],
         "9 puntos de 10"),
        ("Leer por criterio", "¿Por qué un total bajo en Y no es toda la historia?",
         ["Y tiene alcance 2: su propuesta afectaría a todo el liceo.", "Un argumento débil con mucho alcance es riesgoso y requiere más escrutinio."],
         "Porque su alto alcance exige más escrutinio"),
    ],
    mistakes=[("Quedarse solo con el puntaje total de la rúbrica.", "Se piensa que la suma resume todo.", "Lee cada criterio y el alcance para entender fortalezas y riesgos."),
              ("Descartar toda la propuesta de un texto con falacias.", "Se confunde el error de un argumento con el valor de la propuesta.", "Señala qué razón falla y qué evidencia podría sostener la propuesta.")],
    T=[
        ("=", "{F} ¿Cuántos puntos más que la columna Y obtuvo la columna X en total?", "(2+2+2+1+2)-(0+1+1+2+0)", "X suma 9 e Y suma 4; la diferencia es 5.", " puntos"),
        ("=", "{F} ¿Cuál es el total de la columna Y en la rúbrica?", "0+1+1+2+0", "Se suman los puntajes de los cinco criterios.", " puntos"),
        ("abc", "{F} ¿Qué columna tiene mejor construcción lógica?", "La X", "La Y", "Ambas por igual", "X obtuvo 2 puntos en lógica e Y obtuvo 0."),
        ("abc", "{F} ¿Qué columna tiene mayor alcance?", "La Y", "La X", "Ninguna", "La propuesta de Y afecta a todo el liceo y a las familias."),
        ("abc", "{F} ¿Por qué la columna Y merece especial escrutinio?", "Porque combina una construcción débil con un efecto amplio", "Porque su puntaje total es alto", "Porque es breve", "Una decisión de gran alcance necesita bases sólidas."),
        ("abc", "{F} ¿Cómo se describe mejor la columna X?", "Sólida y de alcance acotado", "Débil y de alcance amplio", "Débil y de alcance acotado", "Tiene buena lógica y evidencia pero afecta a un solo curso."),
        ("ab", "{F} ¿Cuál es una conclusión prudente sobre la columna Y?", "Su propuesta no debería adoptarse con estas razones, pero se podría reformular con mejor evidencia", "Su propuesta es falsa por tener falacias", "El error de un argumento no prueba que la propuesta sea mala, solo que esas razones no bastan."),
        ("abc", "¿Qué sesgo puede afectar a quien evalúa?", "Preferir las conclusiones con las que ya está de acuerdo", "Contar los puntos de la rúbrica", "Leer con calma", "Ese sesgo contamina la evaluación porque favorece lo que ya se cree."),
        ("abc", "{F} ¿Qué convendría hacer para reducir el sesgo del evaluador?", "Pedir que otra persona revise el juicio con la misma rúbrica", "Evaluar solo lo que me gusta", "Ignorar los criterios", "La revisión por pares ayuda a detectar sesgos."),
        ("abc", "{F} Si el alcance de X se ampliara a todo el liceo, ¿qué cambiaría?", "Habría que exigir más evidencia por el mayor efecto", "Nada cambiaría", "Dejaría de ser un argumento", "Mayor alcance exige mayor sustento antes de decidir algo."),
        ("abc", "{F} Un compañero dice: «Y tiene 4 puntos y X 9, así que no importa lo que dice Y». ¿Cuál es la mejor respuesta?", "El alcance de Y exige leerla con cuidado y ayudarla a mejorar", "Tiene razón: descartar a Y", "Sumar los puntajes lo resuelve todo", "El total no refleja que el alcance de Y es amplio."),
        ("abc", "¿Qué haría más justa una evaluación?", "Usar la lectura generosa y declarar los límites de lo que se sabe", "Leer solo el título", "Buscar solo los errores", "Así se evalúa lo mejor del argumento y se admiten los límites."),
        ("abc", "{F} ¿Qué recomendación ayudaría a la columna Y?", "Reemplazar la generalización apresurada por datos de varios cursos y eliminar el ataque personal", "Repetir la misma frase más fuerte", "Hacer el texto más largo", "Corrige las fallas lógicas y de respeto."),
    ],
    ctx=("abc", "Un comité ficticio evalúa dos propuestas: una bien argumentada para cambiar el color de una sala y una débilmente argumentada para cambiar el horario de salida de todo el liceo. ¿Qué debería hacer?", "Examinar con más cuidado la segunda por su mayor alcance, sin descartarla y pidiendo mejores razones", "Aprobar la primera y rechazar la segunda sin más", "Aprobar ambas por simpatía", "Mayor alcance exige más sustento, pero se invita a mejorar la propuesta."),
    sc=[
        ("En Participación y argumentación: ¿qué es el alcance de un argumento?", "Cuántas personas afecta y qué tan grande es el efecto", "Importa para decidir cuánto escrutinio merece."),
        ("¿Por qué leer los puntajes por criterio y no solo el total?", "Porque el total esconde fortalezas y riesgos", "Un puntaje igual puede tener perfiles muy distintos."),
        ("¿Qué límite reconoce una evaluación honesta?", "Que quien evalúa puede tener sesgos o información incompleta", "Por eso se declara y se revisa con otras personas."),
    ],
    op=("Elige uno. Evalúa con la rúbrica de la ficha (cada criterio de 0 a 2) una de estas dos propuestas de ejemplo. Propuesta 1: «Instalar un bebedero en el patio, porque 90 de 120 estudiantes consultados dicen que no encuentran agua fría; sirve a todo el liceo.» "
        "Propuesta 2: «Cambiar el horario de todo el liceo, porque mi curso llega cansado; los que no estén de acuerdo no entienden nada.» "
        "Asigna puntajes con una razón por criterio, suma, escribe el alcance de la propuesta y un juicio razonado con una recomendación y un límite de tu evaluación.",
        "Propuesta 1. Lógica 2: la conclusión se sigue del problema. Evidencia 2: dato de 90 de 120 con fuente. Pertinencia 2. Alcance 2: afecta a todo el liceo. Claridad y respeto 2. Total 10. Juicio: sólida y de amplio alcance; falta saber el costo. Límite: la consulta es de ejemplo y no sabemos si representa a todos.",
        ["asigna puntajes con una razón por criterio", "suma bien el total", "considera el alcance", "declara un límite de su evaluación", "formula una recomendación"],
        ["tabla de criterios con puntajes y razones, total, alcance y juicio"],
        ["dar puntajes sin razones", "quedarse con el total", "no declarar ningún límite"],
        "Pregunta: «¿qué haría que otra persona evaluara distinto?». Si no hay respuesta, falta ver sesgos."),
    reinforce="Con los puntajes de la ficha, escribe una oración que describa a la columna Y por su perfil de criterios y no solo por su total.",
    extend="Explica cómo cambiaría tu evaluación de una propuesta si descubrieras que afecta a mucha más gente de lo que pensabas.",
)
