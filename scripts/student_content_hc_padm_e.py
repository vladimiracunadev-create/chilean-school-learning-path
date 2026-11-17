"""Participación y argumentación en democracia (electivo HC, 3.º y 4.º medio): OAC-07 (construir una postura personal a partir de investigaciones y de la confrontación de argumentaciones y evidencias), clases 1 a 4. Casos ficticios; el cuaderno no toma partido en ningún tema."""
from __future__ import annotations

from hc_common import make_build

MATERIALS = ("Lápiz, goma y papel o cuaderno. No se necesita computador ni internet: cada texto, ficha o tabla está escrito en el enunciado. "
             "Todos los casos son ficticios (comuna «Villa Alerce», «Liceo Los Pinos») y los datos son de ejemplo: no son cifras reales. "
             "Este cuaderno no te dice qué postura tener: te enseña a construir la tuya con razones, a confrontarla con la mejor objeción y a revisarla. "
             "Las posturas de los ejemplos son solo modelos de cómo se escribe una postura. Si un tema te afecta personalmente, puedes pasar tu turno y conversarlo con una persona adulta de confianza.")
build = make_build(MATERIALS)

O7 = "LL-PADM-3y4-OAC-07"

# ============================================================ OAC-07, clase 1
F = ("Ficha 1 (tema de ejemplo: ¿debe el Liceo Los Pinos reducir las tareas para la casa?). "
     "Texto 1: «Odio las tareas.» "
     "Texto 2: «Creo que el liceo debería reducir las tareas repetitivas y mantener las de lectura, porque valoro el tiempo de descanso y porque un informe de ejemplo señala que las tareas repetitivas aportan poco; reconozco que reducirlas podría dejar menos práctica en algunos temas.» "
     "Texto 3: «Aún no tengo postura: necesito saber cuánto tiempo dedican realmente los estudiantes a las tareas.»")
build(
    O7, 1, F,
    use="Aprenderé qué es una postura personal fundada, cómo se diferencia de una opinión sin razones, qué partes tiene (tesis, razones, valores, matices) y por qué suspender el juicio puede ser razonable.",
    prior=["Sé construir un argumento con evidencia.", "Sé distinguir desacuerdos de hechos, de valores y de medios.", "Sé evaluar una argumentación con criterios."],
    explain=[
        "Una opinión es lo que alguien piensa o siente sobre un tema, y puede quedar sin razones («odio las tareas»). Una postura personal fundada es una posición que alguien construye después de informarse, evaluar argumentos y evidencias, y que puede explicar. Tiene una tesis (lo que sostiene), razones y evidencia, los valores que la guían y matices que reconocen sus límites. Por eso se puede discutir, revisar y mejorar.",
        "Los valores forman parte de toda postura sobre temas controversiales. Los datos informan sobre lo que ocurre, pero qué hacer depende también de lo que se considera importante, como el descanso, la práctica o la equidad. Una postura honesta nombra sus valores y no se esconde detrás de los datos. También reconoce el costo de lo que propone: en el texto 2, reducir tareas podría dejar menos práctica en algunos temas.",
        "A veces la posición más razonable es suspender el juicio: decir «aún no tengo postura» y precisar qué información falta, como en el texto 3. Eso es distinto de no querer pensar: quien suspende el juicio con razones sabe qué necesita para decidir. Construir una postura toma tiempo, y puede cambiar cuando aparecen mejores razones. Cambiar de postura por buenas razones es una señal de pensamiento crítico, no de debilidad.",
    ],
    vocab=[("postura personal fundada", "posición construida con razones y evidencia que puede explicarse y revisarse"), ("tesis", "lo que una postura sostiene"), ("valor", "aquello que se considera importante, como el descanso o la equidad"), ("matiz", "reconocimiento de los límites o costos de la propia postura"), ("suspender el juicio", "no decidir todavía por falta de información, precisando qué falta"), ("pensamiento crítico", "forma de pensar que evalúa razones y evidencias antes de decidir")],
    worked=[
        ("Distinguir opinión y postura", "En la ficha, ¿por qué el texto 1 no es una postura fundada y el texto 2 sí?",
         ["El texto 1 expresa una emoción sin razones ni evidencia.", "El texto 2 tiene tesis, razones, un valor nombrado, una evidencia y un matiz."],
         "El 1 no tiene razones; el 2 tiene tesis, razones, valor y matiz"),
        ("Identificar el valor", "En el texto 2, ¿qué valor guía la postura?",
         ["Se dice «valoro el tiempo de descanso».", "Ese es un valor que orienta la decisión junto con la evidencia."],
         "El descanso"),
    ],
    mistakes=[("Creer que una postura es solo una opinión firme.", "Se confunde la intensidad con la fundamentación.", "Pregunta qué razones, qué evidencia y qué valores la sostienen."),
              ("Considerar que suspender el juicio es no tener nada que decir.", "Se piensa que hay que tener postura siempre.", "Declara qué información te falta y cómo la conseguirías.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis del texto 2?", "El liceo debería reducir las tareas repetitivas y mantener las de lectura", "Odio las tareas", "No tengo postura", "La tesis es lo que sostiene la persona."),
        ("abc", "{F} ¿Qué parte del texto 2 es un matiz?", "Reducirlas podría dejar menos práctica en algunos temas", "Valoro el tiempo de descanso", "Un informe señala que aportan poco", "Reconoce un costo de la propia postura."),
        ("abc", "{F} ¿Qué evidencia cita el texto 2?", "Un informe de ejemplo sobre el aporte de las tareas repetitivas", "Su cansancio personal", "Una tradición familiar", "Es el respaldo informativo de la postura."),
        ("abc", "{F} Si el texto 1 dijera «odio las tareas porque me quitan tiempo de descanso», ¿ya sería una postura fundada?", "Todavía no: tiene una razón, pero le faltan evidencia y reconocer algún costo", "Sí: toda frase con «porque» es una postura fundada", "Sí: porque expresa una emoción intensa", "Una razón suelta no basta: la postura fundada suma evidencia, valores y matices."),
        ("abc", "{F} ¿Qué hace el texto 3?", "Suspende el juicio y precisa qué información falta", "Defiende una tesis con datos", "Ataca a otra postura", "Dice qué necesita saber antes de decidir."),
        ("abc", "{F} ¿Por qué suspender el juicio en el texto 3 es razonable?", "Porque identifica el dato que necesita para decidir", "Porque no quiere pensar", "Porque nunca tiene opinión", "Hay una razón concreta: le falta información clave."),
        ("ab", "Una postura honesta sobre un tema controversial:", "Nombra sus valores y reconoce sus costos", "Se presenta como si solo dependiera de datos", "Los valores son parte de la postura y deben declararse."),
        ("abc", "Alguien dice: «Mi postura es mía y no tengo que explicarla». ¿Qué le falta para que sea una postura fundada?", "Razones y evidencia que otros puedan examinar", "Más intensidad", "Una firma", "Una postura fundada se puede explicar y discutir."),
        ("abc", "{F} ¿Qué diferencia hay entre los textos 2 y 3?", "El 2 defiende una tesis; el 3 pospone la decisión hasta tener un dato", "El 2 no tiene razones", "El 3 tiene una tesis fuerte", "Cada uno responde de forma distinta a la información disponible."),
        ("abc", "Una estudiante cambia su postura al conocer un informe verificable que contradice su dato. ¿Cómo se valora ese cambio?", "Como una muestra de pensamiento crítico", "Como una debilidad", "Como una derrota", "Cambiar por buenas razones es parte de pensar críticamente."),
        ("abc", "{F} Si el informe del texto 2 resultara tener muestra pequeña, ¿qué sería razonable?", "Revisar la postura y declarar el límite de esa evidencia", "Ignorar el problema", "Cambiar de tema", "Se ajusta la postura a la calidad de la evidencia."),
        ("abc", "{F} ¿Qué dato necesitaría el texto 3 para formar una postura?", "El tiempo real que dedican los estudiantes a las tareas", "Cuántas hojas hay en el cuaderno", "El nombre del director", "Es el dato que ella misma declara como necesario."),
        ("abc", "¿Qué diferencia hay entre una opinión intensa y una postura fundada?", "La fundada tiene razones y evidencia revisables", "La intensa es más correcta", "Ninguna", "La intensidad no sustituye las razones."),
    ],
    ctx=("abc", "En el consejo vecinal ficticio, una vecina dice sobre un nuevo paradero: «Creo que conviene instalarlo, porque un conteo de ejemplo muestra que 80 personas esperan la micro de pie cada día; valoro la comodidad de quienes esperan, aunque implica un costo». ¿Qué parte es el valor?", "La comodidad de quienes esperan", "El conteo de 80 personas", "El costo", "El valor es lo que ella considera importante."),
    sc=[
        ("En Participación y argumentación: ¿qué es una postura personal fundada?", "Una posición construida con razones y evidencia que se puede explicar y revisar", "Se diferencia de una opinión sin razones."),
        ("¿Qué es suspender el juicio?", "No decidir todavía por falta de información, precisando qué falta", "No es lo mismo que no querer pensar."),
        ("¿Qué papel cumplen los valores en una postura?", "Orientan qué se considera importante además de los datos", "Una postura honesta los declara y no los esconde detrás de datos."),
    ],
    op=("Elige uno. Tema 1: ¿debería el liceo tener un espacio de estudio en silencio durante los recreos? Tema 2: ¿debería la plaza tener una feria semanal? "
        "Escribe una postura fundada de cinco a seis oraciones con tesis, dos razones, una evidencia de ejemplo que inventes y rotules como «de ejemplo», un valor nombrado y un matiz sobre un costo. Si crees que no tienes información suficiente, escribe una suspensión razonada del juicio indicando qué dos datos necesitarías.",
        "Tema 1. «Creo que el liceo debería tener un espacio de estudio en silencio en los recreos (tesis), porque hay estudiantes que preparan pruebas (razón 1) y porque ayuda a convivir mejor con quienes quieren jugar (razón 2). Un conteo de ejemplo muestra 30 estudiantes que lo usarían (evidencia de ejemplo). Valoro que todos tengan un lugar adecuado para lo que necesitan (valor). Reconozco que ocuparía una sala que otros podrían usar (matiz).»",
        ["incluye tesis, razones, evidencia rotulada, valor y matiz", "las razones apoyan la tesis", "reconoce un costo real de su postura", "o suspende el juicio precisando qué falta"],
        ["texto de cinco a seis oraciones con las partes marcadas"],
        ["expresar solo un sentimiento", "no nombrar el valor", "presentar una evidencia inventada como real"],
        "Pregunta: «¿qué te haría cambiar de postura?». Si no lo sabe, ayúdale a pensar en un dato."),
    reinforce="Marca en el texto 2 de la ficha la tesis, una razón, el valor y el matiz con cuatro rótulos distintos.",
    extend="Explica una situación en la que suspender el juicio sea más responsable que tomar una postura rápida.",
)

# ============================================================ OAC-07, clase 2
F = ("Ficha 2 (matriz de evidencia, datos de ejemplo). Tema: ¿convertir la mitad del patio del liceo en huerto? "
     "Evidencia a favor: E1, consulta de ejemplo a 100 estudiantes elegidos por sorteo, 55 apoyan (peso 2); E2, informe de ejemplo de un liceo vecino, institución pública, donde los conflictos mensuales bajaron de 20 a 14 tras abrir un huerto (peso 3). "
     "Evidencia en contra: E3, conteo de ejemplo del liceo, 150 estudiantes usan la cancha cada semana (peso 3); E4, testimonio de un docente de educación física que teme falta de espacio para clases (peso 1). "
     "Los pesos se asignaron de 1 a 3 según legitimidad, suficiencia y pertinencia de cada evidencia.")
build(
    O7, 2, F,
    use="Aprenderé a investigar un tema controversial reuniendo evidencias a favor y en contra, ordenándolas en una matriz con pesos justificados, y a usar esa matriz sin convertirla en un veredicto automático.",
    prior=["Sé evaluar la legitimidad de una evidencia.", "Sé calcular porcentajes y sumas simples.", "Sé declarar valores y matices en una postura."],
    explain=[
        "Para construir una postura se investiga. Una matriz de evidencia ordena en dos columnas lo que apoya y lo que cuestiona una propuesta. Cada evidencia se acompaña de su fuente y de un peso que indica cuánto cuenta. El peso no se asigna por gusto: se justifica con los criterios que ya conoces, es decir, legitimidad de la fuente, suficiencia de los datos y pertinencia al problema. Un conteo con método pesa más que un testimonio aislado.",
        "Con los pesos se puede sumar cada columna. En la ficha, los pesos a favor suman 2 + 3 = 5 y los pesos en contra 3 + 1 = 4. La diferencia es pequeña, de modo que la matriz no decide por sí sola. Los números ayudan a ver el panorama, pero no reemplazan el juicio: falta considerar los valores en juego, como el aprendizaje y el juego, y las posibles soluciones intermedias, como dividir el uso por turnos.",
        "Una investigación honesta busca también la evidencia que contradice lo que uno prefiere. Si todas las evidencias de la matriz apoyan una sola posición, hay que sospechar que faltó buscar la otra cara. Por último, se anota qué información falta y qué cambiaría el balance: por ejemplo, saber cuántos estudiantes usan realmente la cancha o qué espacio necesita el huerto.",
    ],
    vocab=[("matriz de evidencia", "tabla que ordena evidencias a favor y en contra con su fuente y peso"), ("peso", "valor que indica cuánto cuenta una evidencia según su calidad"), ("contraevidencia", "dato que cuestiona la postura que uno prefiere"), ("balance", "comparación del conjunto de evidencias"), ("solución intermedia", "propuesta que atiende parte de lo que preocupa a cada lado"), ("juicio", "decisión razonada que va más allá de sumar puntajes")],
    worked=[
        ("Sumar los pesos", "Con la ficha, ¿cuánto suman los pesos de la evidencia a favor?",
         ["Se toman los pesos de E1 y E2: 2 y 3.", "2 + 3 = 5."],
         "5"),
        ("Interpretar el balance", "Con 5 a favor y 4 en contra, ¿qué se puede decir?",
         ["La diferencia es de solo 1 punto, que es pequeña.", "La matriz no decide sola: falta considerar valores y soluciones intermedias."],
         "La matriz inclina levemente, pero no decide sola"),
    ],
    mistakes=[("Asignar pesos según qué evidencia nos gusta más.", "Se mezcla la preferencia con la calidad de la evidencia.", "Justifica cada peso con legitimidad, suficiencia y pertinencia."),
              ("Tomar el resultado de la suma como un veredicto.", "Se olvida que los valores y las alternativas también cuentan.", "Usa la matriz para ver el panorama y decide con juicio.")],
    T=[
        ("=", "{F} Si se suman los pesos de las cuatro evidencias (E1 a E4), ¿cuántos puntos de peso hay en total?", "2+3+3+1", "Se suman los pesos 2, 3, 3 y 1 de las cuatro evidencias.", " puntos"),
        ("=", "{F} ¿Cuántos puntos de peso más tiene la evidencia a favor que la evidencia en contra?", "(2+3)-(3+1)", "A favor suma 5 y en contra suma 4, así que hay un punto más.", " punto"),
        ("abc", "{F} ¿Por qué E2 tiene peso 3?", "Es un informe de una institución pública con datos de antes y después", "Porque dice algo agradable", "Porque es corto", "Es una fuente legítima y pertinente al problema."),
        ("abc", "{F} ¿Por qué E4 tiene peso 1?", "Es un testimonio individual sin datos", "Porque es de un docente", "Porque es muy largo", "Aporta un temor, pero no mediciones."),
        ("=", "{F} Si E1 hubiera consultado a 200 estudiantes con la misma proporción de apoyo (55 de cada 100), ¿cuántos apoyarían?", "200*55//100", "Por cada 100 estudiantes apoyan 55; en 200 son el doble, 110.", " estudiantes"),
        ("abc", "{F} En E2, ¿cuántos conflictos mensuales menos hubo tras el huerto?", "6", "14", "20", "20 menos 14 da 6 conflictos menos por mes."),
        ("abc", "{F} ¿Qué evidencia de la ficha pesa más en contra del huerto?", "E3, el conteo de 150 estudiantes que usan la cancha cada semana", "E4, el temor de un docente", "E1, la consulta por sorteo", "E3 tiene peso 3 y es un conteo; E4 solo pesa 1 y E1 apoya el huerto."),
        ("abc", "{F} ¿Qué faltaría considerar además de la suma?", "Los valores en juego y las soluciones intermedias", "El color del huerto", "El nombre del liceo", "La suma no resuelve qué es más importante."),
        ("abc", "{F} ¿Qué solución intermedia podría proponerse?", "Un huerto más pequeño y turnos de uso de la cancha", "Eliminar todo el patio", "No hacer nada", "Intenta atender parte de lo que busca cada lado."),
        ("abc", "{F} Si la consulta E1 hubiera sido a amigos del autor, ¿cómo cambiaría su peso?", "Bajaría, porque tendría sesgo de selección", "Subiría, porque habría más cercanía", "Quedaría igual", "El método de selección afecta la legitimidad."),
        ("abc", "{F} Se agrega E5: un informe de ejemplo de un liceo vecino indica que los huertos escolares requieren dos docentes de apoyo, y el liceo no los tiene (peso 2). ¿Cómo cambia el balance?", "En contra pasa a 6 y a favor sigue en 5, inclinándose en contra", "A favor sube a 7", "No cambia", "Se suma 2 a la columna en contra: 4 + 2 = 6."),
        ("abc", "Un estudiante busca solo evidencia que apoye su postura. ¿Qué problema tiene su investigación?", "No busca la contraevidencia y su matriz será sesgada", "Es muy larga", "Usa pesos", "Una investigación honesta busca también lo que la contradice."),
        ("abc", "{F} ¿Qué información falta para mejorar el balance?", "Cuántos estudiantes usan realmente la cancha y qué espacio necesita el huerto", "El color del uniforme", "El número de ventanas", "Responde a lo que cambiaría el balance."),
    ],
    ctx=("abc", "Una comisión ficticia compara dos evidencias sobre instalar luminarias: un conteo de accidentes nocturnos con método publicado (peso 3) y un relato de un vecino asustado (peso 1). Otra evidencia en contra es un presupuesto que supera lo disponible (peso 3). ¿Cuál es el balance?", "A favor 4, en contra 3, levemente a favor sin ser concluyente", "A favor 3, en contra 4", "Empate", "3 + 1 es 4 y el presupuesto es 3."),
    sc=[
        ("En Participación y argumentación: ¿qué es una matriz de evidencia?", "Una tabla con evidencias a favor y en contra, su fuente y su peso", "Ordena el panorama antes de decidir."),
        ("¿Con qué criterios se justifican los pesos?", "Legitimidad, suficiencia y pertinencia", "Un peso no se asigna por gusto."),
        ("¿Por qué buscar contraevidencia?", "Para no sesgar la investigación hacia lo que uno prefiere", "Una investigación honesta busca la otra cara."),
    ],
    op=("Elige uno. Tema 1: ¿conviene organizar una jornada de intercambio de libros en el liceo cada mes? Tema 2: ¿conviene que el municipio cierre una calle al tráfico un domingo al mes? "
        "Arma una matriz con al menos dos evidencias a favor y dos en contra (de ejemplo, rotuladas), con fuente y peso de 1 a 3 justificado, suma cada columna, interpreta el balance y escribe qué dato faltaría.",
        "Tema 1. A favor: E1 consulta de ejemplo, 60 de 100 estudiantes apoyan, peso 2 (sorteo, tamaño razonable); E2 informe de biblioteca, 40 libros intercambiados en una prueba, peso 2. En contra: E3 conteo de ejemplo, 3 voluntarios disponibles, peso 3 (falta personal); E4 testimonio de un docente, teme desorden, peso 1. Totales: 4 a favor, 4 en contra, empate. Falta saber cuántos voluntarios se podrían sumar.",
        ["incluye al menos dos evidencias por columna con fuente", "justifica cada peso con un criterio", "suma bien y no trata el resultado como veredicto", "indica un dato faltante"],
        ["matriz, sumas y comentario de tres líneas"],
        ["asignar pesos por gusto", "no incluir contraevidencia", "tomar la suma como veredicto"],
        "Pregunta: «¿por qué esta evidencia pesa más que aquella?». Pide un criterio concreto."),
    reinforce="Recalcula el balance de la ficha si el peso de E3 bajara a 2 y explica cómo cambia la lectura.",
    extend="Explica por qué dos personas con la misma matriz pueden llegar a posturas distintas sin que ninguna sea irracional.",
)

# ============================================================ OAC-07, clase 3
F = ("Ficha 3 (revisión de una postura, de ejemplo). Postura inicial de Laura: «El liceo debería prohibir las bebidas muy azucaradas en el kiosco, porque son malas.» "
     "Objeción 1 (de ejemplo, fuerte): «Prohibirlas no asegura que se consuman menos fuera del liceo, y quienes trabajan en el kiosco perderían ingresos.» "
     "Objeción 2 (de ejemplo, débil): «Laura es muy exagerada.» "
     "Postura revisada: «El liceo debería reducir la oferta de bebidas muy azucaradas y ofrecer opciones sin azúcar a precio similar, y evaluar el efecto en seis meses, porque valoro la salud sin dañar el trabajo de quienes atienden el kiosco.»")
build(
    O7, 3, F,
    use="Aprenderé a confrontar mi postura con la mejor objeción, distinguir objeciones fuertes de débiles y revisar mi postura con matices o cambios cuando las razones lo justifican.",
    prior=["Sé qué es una postura fundada.", "Sé construir una matriz de evidencia.", "Conozco las falacias frecuentes."],
    explain=[
        "Confrontar una postura es ponerla a prueba con la mejor objeción que se le puede hacer. Una objeción fuerte señala un problema real: un costo, un efecto no considerado, una evidencia contraria o un valor importante que se descuidó. Una objeción débil ataca a la persona o deforma lo dicho, como «Laura es muy exagerada», y no merece una respuesta de fondo, aunque sí un llamado a volver a las razones.",
        "Frente a una objeción fuerte hay tres caminos. Se puede mantener la postura y responder con razones o evidencia. Se puede matizarla, reconociendo el límite que la objeción muestra. O se puede cambiarla en parte o del todo. En el ejemplo, Laura pasó de «prohibir» a «reducir y ofrecer alternativas con evaluación», atendiendo los ingresos del kiosco. Revisar una postura no es perder; es mejorarla.",
        "Para confrontar bien, conviene formular la objeción más fuerte con las palabras que usaría quien piensa distinto, y no en versión débil para ganar. Se pregunta: ¿qué dato o argumento me haría cambiar de postura? Si ninguno, quizá no es una postura sino un dogma. Y se evita cambiar solo por presión: se cambia por mejores razones, nunca por cansancio o porque la mayoría lo pida.",
    ],
    vocab=[("objeción fuerte", "razón que señala un problema real de una postura"), ("objeción débil", "ataque a la persona o deformación de lo dicho"), ("matizar", "reconocer límites o costos sin abandonar la postura"), ("revisar una postura", "ajustarla a partir de mejores razones"), ("dogma", "idea que se sostiene sin aceptar que ninguna razón pueda cambiarla"), ("presión", "intento de cambiar una postura sin razones nuevas")],
    worked=[
        ("Distinguir objeciones", "En la ficha, ¿cuál objeción es fuerte y cuál débil?",
         ["La objeción 1 señala efectos reales: consumo fuera del liceo e ingresos del kiosco.", "La objeción 2 ataca a Laura y no responde a su postura."],
         "La 1 es fuerte; la 2 es débil"),
        ("Revisar con matiz", "¿Cómo respondió Laura a la objeción fuerte en su postura revisada?",
         ["Cambió de prohibir a reducir la oferta y ofrecer alternativas a precio similar.", "Agregó una evaluación en seis meses para comprobar el efecto."],
         "Cambió a reducir, ofrecer alternativas y evaluar"),
    ],
    mistakes=[("Responder solo a la objeción más débil para sentirse a salvo.", "Se prefiere ganar a mejorar la postura.", "Formula y responde la objeción más fuerte."),
              ("Cambiar de postura porque otros insisten o son más.", "Se confunde presión con razones.", "Cambia cuando haya un dato o argumento nuevo, no por cansancio ni por mayoría.")],
    T=[
        ("abc", "{F} ¿Qué razón de la postura inicial de Laura es demasiado vaga?", "«porque son malas»", "«en el kiosco»", "«bebidas muy azucaradas»", "No dice en qué sentido son malas ni aporta evidencia."),
        ("abc", "{F} ¿Por qué la objeción 2 es débil?", "Ataca a la persona y no responde a las razones", "Es muy breve", "Usa datos", "No examina la postura de Laura."),
        ("{F} ¿Qué dos problemas señala la objeción 1 contra la prohibición?", "Que quizá no baje el consumo fuera del liceo y que el kiosco perdería ingresos", "Son efectos concretos de la propuesta que Laura no había considerado."),
        ("abc", "{F} ¿Qué valor declara Laura en la postura revisada?", "La salud sin dañar el trabajo de quienes atienden el kiosco", "El precio del azúcar", "La fama", "Ese es el valor que nombra."),
        ("abc", "{F} ¿Qué agrega la postura revisada para comprobar el efecto?", "Una evaluación en seis meses", "Una votación inmediata", "Nada", "Permite revisar con datos si funcionó."),
        ("abc", "{F} ¿Cómo se llama dar razones para mantener la postura ante una objeción?", "Responder con razones o evidencia", "Matizar solo", "Cambiar de tema", "Es una de las tres vías posibles."),
        ("ab", "{F} Si una amiga dice a Laura: «cambia de postura o te dejo de hablar», eso es:", "Presión, no una razón para cambiar", "Una razón para cambiar", "Las razones son datos o argumentos, no amenazas."),
        ("abc", "{F} ¿Cuál es la mejor formulación de la objeción fuerte para una confrontación honesta?", "«Prohibir podría no reducir el consumo fuera del liceo y afectaría los ingresos del kiosco»", "«Laura siempre exagera»", "«No me importa»", "Es la versión más fuerte con las razones de quien piensa distinto."),
        ("abc", "¿Qué pregunta ayuda a saber si una postura es un dogma?", "¿Qué dato me haría cambiar de postura?", "¿Quién me apoya?", "¿Qué postura es más cómoda?", "Si ningún dato podría cambiarla, es un dogma."),
        ("abc", "{F} Después de la objeción 1, Laura mantiene «prohibir», pero agrega datos de otros liceos donde la prohibición redujo el consumo en general. ¿Qué camino tomó?", "Mantuvo la postura y respondió con evidencia", "Cambió totalmente de postura", "Ignoró la objeción", "Responde a la objeción con evidencia nueva."),
        ("abc", "{F} Si Laura recibiera un informe verificable que muestra que la reducción de oferta no cambia el consumo, ¿qué sería razonable?", "Revisar nuevamente su postura", "Ignorar el informe", "Atacar a quien lo trajo", "Una evidencia fuerte nueva justifica ajustar la postura."),
        ("abc", "Un grupo cambia de postura porque «ganó la mayoría» en un chat, sin razones. ¿Qué piensas?", "Es un cambio por presión y no por razones", "Es un cambio razonable", "Es un cambio por evidencia", "La mayoría no es en sí una razón sobre qué es mejor."),
        ("abc", "{F} ¿Qué ganó Laura al revisar su postura?", "Una postura que atiende mejor a las personas afectadas", "Nada, porque cedió", "Dejó de tener valores", "Mejoró su alcance y su precisión."),
    ],
    ctx=("abc", "Un estudiante ficticio defiende cerrar la biblioteca a las 17:00. Le objetan que algunos estudian solo en la tarde. Él responde: «No importa, mi postura es esa». ¿Qué le falta?", "Considerar la objeción y responder con razones o ajustar la postura", "Mantener la postura sin cambios", "Cerrar la discusión", "Una confrontación honesta atiende objeciones reales."),
    sc=[
        ("En Participación y argumentación: ¿qué es una objeción fuerte?", "Una razón que señala un problema real de la postura", "No es un ataque personal sino una razón contra la postura."),
        ("¿Cuáles son los tres caminos ante una objeción fuerte?", "Mantener con razones, matizar o cambiar", "Todos son legítimos si hay razones."),
        ("¿Por qué no se cambia de postura por presión?", "Porque la presión no es una razón sobre el tema", "Se cambia por mejores razones o evidencia."),
    ],
    op=("Elige uno. Postura inicial 1 (de ejemplo): «El curso debería reemplazar el paseo de fin de año por una actividad solidaria, porque es lo más correcto.» Postura inicial 2 (de ejemplo): «El municipio debería prohibir los puestos ambulantes en la plaza, porque ensucian.» "
        "Escribe la objeción más fuerte con las palabras de quien piensa distinto, una objeción débil que no debe responderse y una postura revisada (tesis, razón, valor y matiz) que muestre cuál de los tres caminos tomaste.",
        "Postura 2. Objeción fuerte: «Prohibirlos afectaría los ingresos de familias que trabajan allí y no asegura que la plaza esté más limpia». Objeción débil: «Quien propone eso nunca ha trabajado». Revisada: «El municipio debería exigir un plan de aseo a los puestos y fiscalizar su cumplimiento, porque valoro una plaza limpia y el trabajo de quienes la usan; reconozco que fiscalizar tiene un costo».",
        ["formula una objeción fuerte con fidelidad", "identifica una objeción débil", "revisa su postura con razones y matiz", "nombra el camino elegido"],
        ["objeción fuerte, objeción débil y postura revisada"],
        ["formular la objeción en versión débil", "cambiar de postura sin razones", "mantener la postura ignorando la objeción"],
        "Pregunta: «¿esta es la objeción más fuerte que haría alguien razonable?». Si no, pide reformularla."),
    reinforce="Escribe la objeción más fuerte que podrías recibir contra una postura tuya reciente y una respuesta con razones.",
    extend="Explica la diferencia entre ceder por presión y cambiar de postura por evidencia, con un ejemplo de curso.",
)

# ============================================================ OAC-07, clase 4
F = ("Ficha 4 (modelo de postura comunicada, de ejemplo). «Mi tesis: el liceo debería ofrecer un taller de estudio acompañado en la tarde. Razones: primero, 84 de 120 estudiantes consultados (consulta de ejemplo) no tienen un lugar tranquilo para estudiar; segundo, el taller no requiere obras. "
     "Valor: considero importante que todos tengan oportunidades parecidas de estudiar. Objeción más fuerte: falta de personal; respuesta: comenzar con dos tardes por semana y voluntarios. "
     "Límite: la consulta es de ejemplo y no sabemos si representa a todo el liceo. Qué me haría cambiar de postura: un informe que muestre que el taller no mejora el estudio. Estoy abierta a revisar mi postura si aparecen mejores razones.»")
build(
    O7, 4, F,
    use="Aprenderé a comunicar una postura personal con razones y a escuchar otras con apertura: explicar mi tesis, mis valores, mis límites y qué me haría cambiar, sin imponerla ni descalificar.",
    prior=["Sé construir una postura fundada.", "Sé confrontarla con objeciones fuertes.", "Sé usar un registro respetuoso."],
    explain=[
        "Comunicar una postura es explicarla de modo que otros puedan evaluarla. Un buen texto o intervención incluye la tesis, las razones con su evidencia, los valores que la guían, la objeción más fuerte con su respuesta, los límites de la propia postura y lo que haría cambiar de opinión. Esa transparencia permite una conversación honesta: quienes escuchan saben desde dónde se habla y qué se podría debatir.",
        "Comunicar no es imponer. Una postura se propone, no se obliga. Además de hablar, se escucha: se reformula con fidelidad lo que dijo la otra persona antes de responder, se reconocen sus buenas razones y se pregunta lo que no queda claro. Quien escucha con apertura puede descubrir una razón que no había considerado y ajustar su postura. Eso no es debilidad: es la finalidad de deliberar.",
        "En una comunidad democrática es normal que existan posturas distintas sobre temas controversiales. El objetivo no es que todos piensen igual, sino que cada persona pueda justificar la suya y que las decisiones colectivas se tomen con razones a la vista. Un buen participante cuida el trato, no ridiculiza, no presiona y acepta que, tras escuchar, algunas decisiones colectivas no coincidan con su postura, sin dejar de seguir argumentando.",
    ],
    vocab=[("comunicar una postura", "explicarla de modo que otros puedan evaluarla"), ("transparencia", "decir con claridad razones, valores y límites"), ("apertura", "disposición a considerar razones distintas"), ("reformular", "repetir fielmente lo que otra persona sostiene antes de responder"), ("decisión colectiva", "la que toma un grupo, que puede no coincidir con la postura de cada integrante"), ("imponer", "obligar a otros a aceptar una postura sin razones")],
    worked=[
        ("Identificar las partes", "En la ficha, ¿cuál es el límite que declara la persona?",
         ["Busca la frase que reconoce lo que no se sabe.", "Dice que la consulta es de ejemplo y no se sabe si representa a todo el liceo."],
         "La consulta es de ejemplo y no sabemos si representa a todo el liceo"),
        ("Escuchar con apertura", "Alguien responde: «Con dos tardes por semana no alcanza». ¿Qué debería hacer la autora antes de responder?",
         ["Reformular lo que dijo la otra persona para comprobar que entendió.", "Luego responder con razones, o ajustar su propuesta si la objeción es válida."],
         "Reformular fielmente y luego responder con razones o ajustar"),
    ],
    mistakes=[("Comunicar la postura como una verdad que los demás deben aceptar.", "Se confunde convicción con imposición.", "Propón la postura, muestra tus razones y deja espacio para objeciones."),
              ("Ridiculizar a quien piensa distinto.", "Se busca ganar en vez de dialogar.", "Reconoce las buenas razones del otro y debate sobre ellas.")],
    T=[
        ("abc", "{F} ¿Cuál es la tesis?", "El liceo debería ofrecer un taller de estudio acompañado en la tarde", "No hay lugares tranquilos para estudiar", "El taller no requiere obras", "Es lo que la persona sostiene."),
        ("abc", "{F} ¿Cuál es el valor declarado?", "Que todos tengan oportunidades parecidas de estudiar", "El dinero del liceo", "La fama", "Es lo que la persona considera importante en este tema."),
        ("abc", "{F} ¿Cuál es la objeción más fuerte que menciona?", "La falta de personal", "Que el taller es aburrido", "Que sobran salas", "La falta de personal es un obstáculo concreto."),
        ("abc", "{F} ¿Cómo responde la persona a esa objeción?", "Comenzar con dos tardes por semana y voluntarios", "La ignora", "Dice que no importa", "Propone un ajuste que atiende la objeción."),
        ("=", "{F} ¿Qué porcentaje de los 120 estudiantes consultados no tiene lugar tranquilo para estudiar?", "84*100//120", "84 de 120 equivale a 70 por cada 100.", " %"),
        ("abc", "{F} ¿Qué haría cambiar de postura a la autora?", "Un informe que muestre que el taller no mejora el estudio", "Que alguien insista más", "Que la mayoría se aburra", "Una evidencia relevante es una razón para revisar."),
        ("ab", "{F} ¿Qué logra la autora al declarar el límite de su consulta?", "Transparencia: otros pueden evaluar hasta dónde llega su evidencia", "Debilitar su postura sin ningún beneficio", "Declarar límites permite una conversación honesta."),
        ("abc", "{F} Alguien dice: «Eso es una idea de gente floja». ¿Qué conviene responder?", "Invitar a debatir las razones de la propuesta, no a las personas", "Responder con otro insulto", "Aceptar el insulto", "La conversación debe volver a las razones."),
        ("abc", "¿Qué conviene hacer antes de responder a una objeción?", "Reformular fielmente lo que se escuchó", "Interrumpir para no olvidarlo", "Cambiar de tema", "Asegura que se entendió bien lo que dijo la otra persona."),
        ("abc", "El curso decide por mayoría otra cosa distinta a lo que propone una estudiante. ¿Qué actitud es coherente con la deliberación?", "Aceptar la decisión colectiva y seguir argumentando por su revisión si hay razones nuevas", "Boicotear la decisión", "Dejar de participar", "La democracia admite decisiones distintas a mi postura y espacios para revisarlas."),
        ("abc", "{F} Una compañera comunica su postura así: «Esto es lo que hay que hacer y punto». ¿Qué le falta?", "Razones, evidencia y apertura a objeciones", "Más volumen", "Un título", "Una postura fundada se explica y se puede discutir."),
        ("abc", "{F} Si apareciera un informe verificable que muestre que el taller sí mejora el estudio, ¿qué ocurre con la postura de la autora?", "Se fortalece con nueva evidencia", "Se debilita", "Se vuelve falsa", "Aporta una razón en el mismo sentido."),
        ("abc", "{F} ¿Cuál es una pregunta abierta para comprender mejor a quien tiene otra postura?", "¿Qué razón te preocupa más de esta propuesta?", "¿Por qué eres tan terco?", "¿No te da vergüenza?", "Invita a explicar sus razones sin atacar."),
    ],
    ctx=("abc", "En una asamblea ficticia, un joven comunica su postura sobre cerrar un jardín al público por las tardes, y dos personas la critican con razones. ¿Qué conducta muestra apertura?", "Reformular las críticas, reconocer lo válido y ajustar su propuesta si corresponde", "Ignorarlas", "Ridiculizar a quien critica", "La apertura implica escuchar y estar dispuesto a revisar."),
    sc=[
        ("En Participación y argumentación: ¿qué incluye comunicar una postura de manera transparente?", "Tesis, razones, valores, objeción más fuerte, límites y qué la cambiaría", "Así otras personas pueden evaluar la postura con claridad."),
        ("¿Qué es imponer una postura?", "Obligar a otros a aceptarla sin razones", "Comunicar una postura es distinto de imponerla a los demás."),
        ("¿Qué hace un buen participante si la decisión colectiva difiere de su postura?", "Acepta la decisión y sigue argumentando si hay razones nuevas", "La deliberación continúa tras la decisión."),
    ],
    op=("Elige uno. Tema 1: ¿debería el liceo destinar un día al mes a actividades de servicio en la comunidad? Tema 2: ¿debería el barrio cerrar al tráfico una calle un domingo al mes para ferias? "
        "Escribe una intervención de un minuto (unas ocho oraciones) comunicando tu postura sobre el tema: tesis, dos razones, un valor, la objeción más fuerte con tu respuesta, un límite y qué te haría cambiar de postura. Luego escribe una frase para reformular una postura contraria antes de responder.",
        "Tema 1. «Mi tesis: el liceo debería destinar un día al mes a servicio en la comunidad. Razones: primero, permite aplicar lo aprendido; segundo, mejora la convivencia con el barrio. Valoro la solidaridad. La objeción más fuerte es que se pierden clases; propongo recuperar la materia con una guía. Límite: no tengo datos del efecto. Me haría cambiar un informe que muestre pérdida importante de aprendizaje.» Reformulación: «Entiendo que te preocupa perder horas de clases.»",
        ["incluye todos los elementos de transparencia", "responde a la objeción con una razón o ajuste", "reformula la postura contraria con fidelidad", "mantiene un tono respetuoso"],
        ["intervención de ocho oraciones y una frase de reformulación"],
        ["imponer la postura", "no declarar límites", "reformular en versión débil"],
        "Pregunta: «¿qué le dirías a alguien que piensa distinto para que se sienta escuchado?». Pide la reformulación."),
    reinforce="Escribe una frase que reformule la objeción «falta de personal» de la ficha antes de responderla.",
    extend="Explica por qué una comunidad democrática necesita tanto la discusión como la capacidad de aceptar una decisión colectiva y seguir debatiendo.",
)
