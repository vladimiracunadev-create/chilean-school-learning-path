"""Ambiente y sostenibilidad 3.º y 4.º medio FG: OA 03 clases 4 y 5 (analizar evidencia y comparar soluciones de mitigación). Humedal y comuna ficticios; datos de ejemplo inventados."""
from __future__ import annotations

from fg_cias_common import build

O3 = "FG-CIAS-3y4-OAC-03"

# ============================================================ OA 03, clase 4
F = ("Ficha 4 (datos de ejemplo de Laguna Azul, promedio por década, de la 1.ª a la 4.ª): temperatura del agua en verano (°C): 18, 19, 20, 21. "
     "Oxígeno disuelto en verano (mg/L, unidad de concentración): 10, 9, 8, 7. Parejas de aves que anidan: 120, 118, 100, 90. Nivel del agua (cm): 150, 140, 120, 90. "
     "Otro hecho de ejemplo: en la 3.ª década se construyó un camino que desvió un canal de agua que alimentaba la laguna.")
build(
    O3, 4, F,
    use="Aprenderé a analizar series de datos de un ecosistema: calcular cambios, distinguir asociación de causa, considerar otras explicaciones y declarar incertidumbre.",
    prior=["Sé distinguir observación y proyección.", "Sé calcular porcentajes.", "Sé qué es un modelo y un supuesto."],
    explain=[
        "Analizar una serie de datos empieza por describir el cambio: cuánto subió o bajó cada variable y qué porcentaje es. Luego se miran las relaciones entre variables. Si una sube mientras otra baja, hay una relación inversa; si suben juntas, directa. Una asociación entre variables no prueba por sí sola que una cause la otra: puede haber otra causa o coincidencia.",
        "La causalidad se vuelve más creíble cuando hay un mecanismo (una explicación física o biológica de cómo una variable cambia a la otra) y cuando se descartan otras explicaciones. Por ejemplo, el agua más cálida retiene menos oxígeno disuelto: ese mecanismo respalda la relación entre calor y oxígeno. En cambio, un camino que desvió el agua de la laguna ofrece otra explicación para la baja del nivel, así que no toda la baja se puede atribuir al clima.",
        "Los datos tienen incertidumbre: cada medición varía y una baja pequeña puede ser ruido, mientras que una baja mayor que esa variación es más confiable. Si una tendencia se extiende hacia el futuro con los mismos supuestos, se llama extrapolación, y puede fallar si algo cambia. Para separar causas se comparan con sitios parecidos que no tengan el cambio estudiado. Una conclusión prudente dice qué cambió, qué lo acompaña y qué falta por saber.",
    ],
    vocab=[("relación inversa", "cuando una variable sube mientras la otra baja"), ("mecanismo", "explicación de cómo una variable cambia a otra"), ("explicación alternativa", "otra causa posible del cambio que no se ha descartado"), ("extrapolación", "extender una tendencia hacia el futuro suponiendo que seguirá igual"), ("sitio de comparación", "lugar parecido sin el cambio estudiado, usado para separar causas")],
    worked=[
        ("Describir un cambio", "En un lago de ejemplo, el oxígeno bajó de 8 a 6 mg/L. ¿Cuánto y qué porcentaje bajó?", ["Bajó 8 − 6 = 2 mg/L.", "El porcentaje es 2 ÷ 8 × 100 = 25 %."], "2 mg/L, que es 25 %"),
        ("Separar una causa", "Las aves de un lago de ejemplo bajaron mientras subía la temperatura, pero también hubo una obra ruidosa cerca. ¿Se puede atribuir la baja solo al calor?", ["Hay dos explicaciones posibles: calor y obra.", "Los datos no separan sus efectos."], "No: se necesita comparar con un lago parecido sin obra"),
    ],
    mistakes=[("Afirmar que dos variables que cambian juntas se causan entre sí.", "Puede haber otra causa o una coincidencia.", "Busca un mecanismo y descarta otras explicaciones."),
              ("Prolongar una tendencia sin decir que es un supuesto.", "La tendencia podría cambiar por causas nuevas.", "Escribe «si continúa la tendencia» y declara la incertidumbre.")],
    T=[
        ('abc', 'En Ambiente y sostenibilidad, ¿qué es una relación inversa entre dos variables?', 'Cuando una variable sube mientras la otra baja', 'Cuando las dos suben a la vez', 'Cuando una variable no cambia nunca', 'Inversa significa que se mueven en sentidos opuestos.'),
        ('=', '{F} ¿Qué porcentaje bajó el oxígeno disuelto entre la 1.ª y la 4.ª década?', '(10-7)*100//10', 'Se divide la baja entre el valor inicial y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje bajó el nivel del agua entre la 1.ª y la 4.ª década?', '(150-90)*100//150', 'Se divide la baja entre el nivel inicial y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje bajó el número de parejas de aves entre la 1.ª y la 4.ª década?', '(120-90)*100//120', 'Se divide la baja entre el valor inicial y se multiplica por 100.', ' %'),
        ('abc', '{F} ¿Qué relación hay entre la temperatura del agua y el oxígeno disuelto?', 'Inversa: cuando la temperatura sube, el oxígeno baja', 'Directa: ambos suben juntos', 'No hay ninguna relación en los datos', 'En cada década la temperatura sube y el oxígeno baja.'),
        ('abc', '{F} ¿Qué da más fuerza a la idea de que el calor causa la baja del oxígeno?', 'Que existe una explicación física: el agua más cálida retiene menos oxígeno disuelto', 'Que los dos datos están en la misma tabla de la ficha de ejemplo', 'Que la temperatura se midió en verano, cuando hay más datos', 'Un mecanismo explica cómo una variable cambia a la otra; estar en la misma tabla no lo prueba.'),
        ('abc', '{F} ¿Qué otra explicación existe para la baja del nivel del agua además del clima?', 'El camino que desvió el canal que alimentaba la laguna', 'La presencia de aves en la laguna', 'El color del agua en verano', 'El desvío del canal reduce el agua que llega a la laguna, independiente del clima.'),
        ('=', '{F} Si la temperatura siguiera subiendo lo mismo por década que hasta ahora, ¿cuál sería en la 6.ª década (en °C)?', '21+2*1', 'La temperatura sube 1 °C por década; faltan dos décadas después de la 4.ª.', ' °C'),
        ('abc', '{F} ¿Qué limitación tiene proyectar la temperatura de la 6.ª década de esa forma?', 'Supone que la tendencia seguirá igual, algo que puede cambiar', 'Ninguna, porque las tendencias nunca cambian', 'Que los datos de la ficha son muy pocos para calcular un promedio', 'Extrapolar supone que no cambian las causas; si cambian, el resultado falla.'),
        ('abc', '{F} ¿Se puede afirmar con estos datos que la baja del oxígeno causó la baja de aves?', 'No: las aves se asocian a varios cambios, como nivel, oxígeno y camino, y no están separados', 'Sí, porque ambas bajaron durante el mismo periodo de décadas', 'Sí, porque todos los animales necesitan oxígeno para respirar', 'Cambiaron varias variables a la vez; la asociación no separa cuál influyó.'),
        ('=', '{F} Si el desvío del canal explica 20 cm de la baja del nivel del agua, ¿cuántos cm podrían deberse a otras causas, como el clima?', '(150-90)-20', 'Se calcula la baja total y se resta la parte atribuida al desvío.', ' cm'),
        ('abc', 'Una medición de oxígeno varía ±1 mg/L por error de medición. ¿Qué se concluye de una baja de 3 mg/L entre décadas?', 'Es mayor que la variación de medición, así que probablemente es una baja real', 'Es un error de medición porque todas las mediciones varían', 'No se puede interpretar ningún cambio', 'Un cambio mayor que el error de medición es más confiable; uno de 1 mg/L podría ser ruido.'),
        ('abc', '{F} ¿Qué diseño ayuda a separar el efecto del clima del efecto del camino?', 'Comparar con otra laguna parecida, del mismo clima, que no tenga un camino que desvíe su agua', 'Medir la misma laguna en el mismo mes de cada década durante más años', 'Preguntar a más personas qué creen que pasó con el agua de la laguna', 'Un sitio de comparación comparte el clima y no el cambio local; así se puede atribuir la diferencia.'),
    ],
    ctx=('abc', 'Después de leer sobre los cambios en la laguna sientes mucha angustia y duermes mal. ¿Qué haces?', 'Conversas con una persona adulta de confianza, como un familiar, docente u orientador, y cuidas tu descanso', 'Guardas todo para ti y sigues leyendo noticias toda la noche', 'Dejas de ir al liceo hasta que se resuelva el problema climático', 'Hablar de la angustia con una persona adulta de confianza ayuda; aislarse o leer sin parar suele empeorarla.'),
    sc=[
        ('En Ambiente y sostenibilidad: ¿qué es una extrapolación?', 'Extender una tendencia hacia el futuro suponiendo que seguirá igual', 'Es una estimación que supone que las causas no cambian.'),
        ('abc', '¿Qué hace más creíble una relación de causa?', 'Que haya un mecanismo y se descarten otras explicaciones', 'Que las variables aparezcan juntas en un gráfico', 'Que muchas personas lo crean', 'El mecanismo y el descarte de alternativas dan solidez; la coincidencia o la opinión no.'),
        ('abc', '¿Qué significa que una explicación alternativa no esté descartada?', 'Que todavía podría explicar el cambio observado y debe mencionarse', 'Que ya se probó que es falsa y se puede sacar del informe', 'Que se debe ignorar porque complica la conclusión', 'Mientras no se descarte, hay que mencionarla en la conclusión.'),
    ],
    op=("Usa la {F} Escribe un análisis breve: el porcentaje de baja del oxígeno y del nivel, la relación entre temperatura y oxígeno con su mecanismo, una explicación alternativa para el nivel y una conclusión prudente sin la palabra «siempre».",
        "El oxígeno bajó 30 % y el nivel del agua, 40 %. Cuando la temperatura sube, el oxígeno baja, y hay un mecanismo: el agua cálida retiene menos oxígeno. Para el nivel hay otra explicación, el desvío del canal. Conclusión: el calor probablemente contribuye a la baja del oxígeno, pero falta separar su efecto sobre el nivel.",
        ["calcula cambios", "relaciona variables con mecanismo", "nombra una explicación alternativa", "concluye con prudencia"], ["dos porcentajes", "mecanismo", "conclusión"], ["afirmar causalidad sin mecanismo", "olvidar la explicación alternativa"],
        "Pregunta qué dato nuevo ayudaría a separar el efecto del clima del efecto del canal."),
    reinforce="Explica con un ejemplo por qué dos variables que cambian juntas pueden no causarse entre sí.",
    extend="Calcula el cambio porcentual de otra variable de la ficha 4 entre la 1.ª y la 3.ª década y explica qué indica.",
)

# ============================================================ OA 03, clase 5
F = ("Ficha 5 (comuna ficticia «Valle Claro», datos de ejemplo; «u» son unidades de emisión inventadas por año). "
     "Opción A: ciclovías y mejor transporte público; evita 800 u al año desde el año 4; costo $400.000.000; co-beneficio: menos contaminación del aire. "
     "Opción B: restaurar un humedal y plantar especies nativas; absorbe 300 u al año recién cuando madura, a partir del año 10; costo $60.000.000; co-beneficios: biodiversidad y protección contra inundaciones; incertidumbre alta porque el crecimiento depende de la lluvia. "
     "Opción C: eficiencia energética en edificios públicos; evita 500 u al año desde el año 1; costo $125.000.000. "
     "Opción D (adaptación, no mitigación): muros de contención para crecidas de ríos; no cambia las emisiones; costo $150.000.000.")
build(
    O3, 5, F,
    use="Aprenderé a evaluar soluciones de mitigación del cambio climático con criterios (efecto, costo, tiempo, incertidumbre y co-beneficios) y a distinguir mitigación de adaptación.",
    prior=["Sé calcular costos por unidad y porcentajes.", "Sé qué es una matriz de criterios.", "Sé distinguir observación y proyección."],
    explain=[
        "La mitigación del cambio climático son las acciones que reducen las emisiones de gases de efecto invernadero o que aumentan los sumideros que los absorben, como los bosques y humedales. La adaptación son las acciones que reducen el daño de los efectos que ya llegan, como muros para crecidas o sistemas de alerta. Las dos se complementan: mitigar reduce el cambio futuro y adaptar protege de lo que no se alcanzó a evitar.",
        "Para evaluar soluciones se comparan criterios: cuánto beneficio entregan, cuánto cuestan por unidad evitada, cuándo empiezan a funcionar, qué tan seguras son (incertidumbre) y qué co-beneficios traen, como mejor aire o más biodiversidad. Una solución barata por unidad puede demorar décadas en tener efecto, y otra puede tener un efecto inmediato pero costar más. Por eso conviene mirar el beneficio acumulado en un periodo, no solo el anual.",
        "Elegir entre soluciones implica valores de la comunidad: qué importa más, el costo, la rapidez o la biodiversidad. Un análisis honesto muestra los criterios y los pesos, prueba qué cambia si se modifican y no oculta la incertidumbre. Los datos de esta clase son de ejemplo, no cifras reales de emisiones. Presenta posturas con sus argumentos sin favorecer a ningún partido, y consulta a la comunidad antes de decidir.",
    ],
    vocab=[("mitigación", "acciones que reducen las emisiones o aumentan los sumideros de gases de efecto invernadero"), ("adaptación", "acciones que reducen el daño de los efectos del cambio climático que ya llegan"), ("co-beneficio", "beneficio adicional de una medida, como mejor aire o biodiversidad"), ("beneficio acumulado", "suma del beneficio de todos los años de un periodo"), ("costo por unidad evitada", "costo dividido por las emisiones que evita en un año")],
    worked=[
        ("Mitigación o adaptación", "Una comuna de ejemplo instala un sistema de alerta de inundaciones y plantan árboles que absorben carbono. ¿Cuál es cada acción?", ["La alerta reduce el daño de las inundaciones: adaptación.", "Los árboles absorben carbono: mitigación."], "Alerta: adaptación; árboles: mitigación"),
        ("Beneficio acumulado", "Una opción de ejemplo evita 200 u al año desde el año 3. ¿Cuánto evita acumulado hasta el año 10?", ["Funciona del año 3 al 10: son 8 años.", "8 × 200 = 1.600."], "1.600 u acumuladas"),
    ],
    mistakes=[("Elegir solo la solución con menor costo por unidad.", "Puede tardar mucho en funcionar o tener alta incertidumbre.", "Compara también el tiempo, la incertidumbre y los co-beneficios."),
              ("Pensar que adaptar y mitigar son lo mismo.", "Mitigar reduce el cambio; adaptar reduce el daño de los efectos.", "Pregunta si la acción cambia las emisiones o protege de un efecto.")],
    T=[
        ('abc', 'En Ambiente y sostenibilidad, ¿qué es la mitigación del cambio climático?', 'Acciones que reducen las emisiones o aumentan los sumideros de gases de efecto invernadero', 'Acciones que reducen el daño de los efectos del cambio climático que ya llegan', 'Acciones que solo informan a la población sobre el cambio climático', 'Mitigar es actuar sobre las causas; reducir el daño de los efectos es adaptación.'),
        ('abc', '{F} ¿Por qué la opción D es adaptación y no mitigación?', 'Protege de las crecidas pero no cambia las emisiones', 'Porque es la más cara de todas', 'Porque se construye cerca de un río', 'Adaptar reduce el daño de un efecto; no reduce emisiones ni aumenta sumideros.'),
        ('=', '{F} ¿Cuántos pesos cuesta cada unidad evitada por año con la opción A?', '400000000//800', 'Se divide el costo entre las unidades evitadas por año.', ' pesos'),
        ('=', '{F} ¿Cuántos pesos cuesta cada unidad absorbida por año con la opción B (cuando madura)?', '60000000//300', 'Se divide el costo entre las unidades absorbidas por año.', ' pesos'),
        ('=', '{F} ¿Cuántos pesos cuesta cada unidad evitada por año con la opción C?', '125000000//500', 'Se divide el costo entre las unidades evitadas por año.', ' pesos'),
        ('=', '{F} ¿Cuántas u acumula la opción A hasta el año 10, contando los años 4 al 10?', '800*(10-4+1)', 'Funciona 7 años; se multiplican por lo que evita cada año.', ' u'),
        ('=', '{F} ¿Cuántas u acumula la opción C hasta el año 10, contando los años 1 al 10?', '500*10', 'Funciona 10 años; se multiplican por lo que evita cada año.', ' u'),
        ('abc', '{F} ¿Cuánto aporta la opción B en los primeros 9 años?', 'Casi nada de absorción madura, aunque a largo plazo sí aporta', 'Aporta 300 u al año desde el primer año', 'Aporta más que A en ese periodo', 'B solo absorbe 300 u al año al madurar, desde el año 10; antes el efecto es pequeño.'),
        ('abc', '{F} ¿Por qué la opción B tiene mayor incertidumbre?', 'Porque el crecimiento de las plantas depende de la lluvia, que puede cambiar', 'Porque los humedales no absorben nada de carbono, solo agua', 'Porque cuesta menos que las otras opciones, así que es menos segura', 'La dependencia de la lluvia agrega incertidumbre sobre cuánto absorberá.'),
        ('abc', '{F} ¿Qué ventaja de la opción B no aparece en su costo por unidad?', 'La biodiversidad y la protección contra inundaciones', 'Que sea la más barata en pesos totales', 'Que no necesite ningún cuidado', 'Son co-beneficios de otro tipo que el costo por unidad de carbono no recoge.'),
        ('abc', 'Una persona propone elegir solo la opción con menor costo por unidad. ¿Qué falta considerar además?', 'El tiempo en que funciona, la incertidumbre de sus resultados y los co-beneficios', 'Solo el costo total de cada opción, que ya incluye todo lo anterior', 'Cuántas personas publican sobre cada opción en las redes sociales', 'Un solo criterio no basta; el momento del efecto y la incertidumbre cambian la comparación.'),
        ('abc', 'La comuna debate entre A y C: A evita más pero cuesta más. ¿Cómo decidir de forma transparente?', 'Mostrar los criterios y los pesos, probar qué cambia al modificarlos y consultar a la comunidad', 'Elegir la opción que prefiera la autoridad sin explicar nada', 'Elegir la que más personas comparten en redes sociales', 'La transparencia permite que la comunidad entienda qué se valora; la popularidad en redes no es evidencia.'),
        ('abc', '¿Por qué conviene combinar mitigación y adaptación?', 'Porque mitigar reduce el cambio futuro y adaptar protege de los efectos que ya llegan', 'Porque son lo mismo con dos nombres distintos y se pueden usar igual', 'Porque una de las dos no sirve y hay que probar cuál de ellas es', 'Se complementan: una actúa sobre la causa y la otra sobre el daño que ya no se evita.'),
    ],
    ctx=('abc', 'Un compañero comparte una captura de pantalla que muestra la comuna inundada, sin fecha ni fuente. ¿Qué haces?', 'No la reenvías, verificas con fuentes oficiales y avisas a una persona adulta si causa alarma', 'La reenvías a todo el curso por si acaso', 'La publicas con un mensaje de alarma para que se enteren más rápido', 'Una imagen sin fuente puede ser falsa; se verifica antes de compartir.'),
    sc=[
        ('En Ambiente y sostenibilidad: ¿qué es la adaptación al cambio climático?', 'Acciones que reducen el daño de los efectos que ya llegan', 'La adaptación protege de efectos; la mitigación actúa sobre las causas.'),
        ('abc', '¿Qué es un co-beneficio?', 'Un beneficio adicional de una medida, como mejor aire o más biodiversidad en la comuna', 'El costo adicional de una medida, que se suma al costo por unidad', 'La suma de los beneficios de dos medidas distintas al mismo tiempo', 'Es una ventaja más allá del objetivo principal.'),
        ('abc', '¿Por qué conviene mirar el beneficio acumulado en un periodo?', 'Porque una solución puede evitar mucho al año pero empezar tarde', 'Porque el beneficio anual siempre es falso', 'Porque se puede ignorar el costo', 'El acumulado combina cuánto evita y desde cuándo.'),
    ],
    op=("Usa la {F} Elige tu orden de prioridad para las opciones A, B y C (la D es adaptación) con tres criterios que tú nombres, calcula el costo por unidad de las que uses y escribe una frase que reconozca la incertidumbre. Cierra con a quién consultarías de la comunidad antes de decidir.",
        "Mi orden: C, A, B. Criterios: costo por unidad, tiempo hasta el efecto y co-beneficios. C cuesta $250.000 por unidad y funciona desde el año 1; A cuesta $500.000 pero evita más; B es la más barata, pero demora 10 años y es incierta. Sus cifras son de ejemplo y dependen de supuestos. Consultaría a vecinos, a la municipalidad y a especialistas.",
        ["usa criterios explícitos", "calcula costos por unidad", "reconoce incertidumbre", "consulta a la comunidad"], ["orden con criterios", "cálculos", "frase de incertidumbre"], ["elegir por un solo criterio", "no declarar incertidumbre"],
        "Pregunta cómo cambiaría tu orden si valoraras más la biodiversidad que el costo."),
    reinforce="Explica con tus palabras la diferencia entre mitigación y adaptación con un ejemplo de tu zona.",
    extend="Propón una medida de adaptación y otra de mitigación para un problema de tu barrio y compara sus criterios.",
)
