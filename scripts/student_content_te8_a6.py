"""Cuaderno del estudiante, 8.º básico Tecnología: OA 06 (impactos éticos, ambientales y sociales de la tecnología), clases 1 a 4.

Seguridad: las tareas son de lectura, cálculo y escritura; no se manipulan pilas, baterías, vidrio ni productos químicos.
Todas las cifras de energía, residuos, personas y puntajes son de ejemplo, para practicar; no son estadísticas reales. Cifras enteras.
Ante una situación real de riesgo o de incomodidad, la tarea indica avisar a una persona adulta de confianza.
Simplificación declarada: el plan de clases de la ficha oficial es genérico (mismos títulos en todos los OA); aquí cada clase sigue el contenido del OA.
"""
from __future__ import annotations

from student_content_te8_a import reg
from student_lessons import arith, ex

OA6 = "TE08 OA 06"

# ------------------------------------------------------------------ OA 06, clase 1
reg(
    OA6, 1,
    materials="Hoja, lápiz y los casos escritos en este cuaderno.",
    use="Aprenderé a reconocer los impactos éticos de una solución tecnológica, como la equidad, la privacidad y la transparencia, y a analizar un dilema. Sirve para decidir si una solución es justa y respetuosa además de útil.",
    prior=["Sé qué es un impacto positivo y uno negativo.", "Sé calcular porcentajes.", "Sé que hay datos que se deben proteger."],
    explain=[
        "Un impacto es el efecto que tiene una solución sobre las personas y el entorno; puede ser positivo o negativo, buscado o no. Los impactos éticos se refieren a valores. La equidad es el trato y el acceso justos para todas las personas. La privacidad es el derecho a que tus datos y tu imagen no se usen sin tu permiso. La seguridad es estar a salvo de daños. La transparencia es explicar cómo funciona un servicio y qué datos usa. La responsabilidad es saber quién responde si algo falla.",
        "Un dilema ético aparece cuando dos valores chocan: unas cámaras en un pasaje pueden aumentar la seguridad, pero registran a quienes pasan y afectan su privacidad. Para analizarlo se pregunta a quién beneficia, a quién perjudica, quién queda excluido, si se pidió permiso y quién responde si falla.",
        "Un buen análisis no solo señala el problema; propone una condición que proteja el valor amenazado. Por ejemplo, grabar solo la entrada, avisar con un letrero y borrar las grabaciones a los 7 días (cifra de ejemplo). Si en una situación real alguien usa tus datos sin permiso o te incomoda, avisa a una persona adulta de confianza.",
    ],
    vocab=[("equidad", "trato y acceso justos para todas las personas"), ("privacidad", "derecho a que tus datos no se usen sin permiso"), ("transparencia", "explicar cómo funciona un servicio y qué datos usa"), ("dilema ético", "situación en que dos valores chocan"), ("responsabilidad", "saber quién responde si algo falla")],
    worked=[
        ("Reconocer el valor que falla", "Una aplicación reparte cupos de ayuda con un sistema que no explica sus criterios. ¿Qué valor falla?", ["Nadie sabe cómo se decide ni por qué.", "Falta explicar cómo funciona el servicio."], "La transparencia"),
        ("Proponer una condición", "Un grupo propone cámaras en todo el pasaje. ¿Qué condición protege la privacidad y mantiene la seguridad?", ["Limito lo grabado a la entrada, que es lo necesario.", "Aviso con un letrero y borro lo grabado a los 7 días."], "Grabar solo la entrada, avisar con un letrero y borrar las grabaciones a los 7 días"),
    ],
    mistakes=[
        ("Pensar que una solución útil siempre es ética.", "Puede ser útil y excluir o invadir la privacidad.", "Revisa también quién queda fuera y qué datos usa."),
        ("Decir «no hay problema porque nadie se quejó».", "Quien está excluido a veces no tiene cómo reclamar.", "Pregunta activamente quién podría salir perjudicado."),
    ],
    R=[
        ("La equidad, ¿es dar trato y acceso justos a todas las personas o dar lo mismo a quien paga más?", "Dar trato y acceso justos a todas las personas", "Es el significado de equidad."),
        ("Una aplicación guarda tu ubicación sin avisarte. ¿Qué valor se vulnera principalmente: la privacidad o la seguridad física?", "La privacidad", "Se usan tus datos sin tu permiso."),
        ("Un impacto negativo que nadie buscaba, ¿puede aparecer aunque la intención sea buena?", "Sí", "Los efectos no deseados existen aunque no se busquen."),
    ],
    C=[
        ("Una beca escolar ofrece su formulario solo por internet y varias familias no tienen conexión. ¿Qué valor está en riesgo? A) la equidad B) la seguridad", "A", "Quienes no tienen conexión no pueden postular en igualdad de condiciones."),
        ("¿Cuál es un dilema ético? A) cámaras que aumentan la seguridad de un pasaje pero registran a quienes pasan B) comprar una cámara más barata", "A", "Dos valores, seguridad y privacidad, chocan."),
        ("La transparencia, ¿es explicar cómo funciona un servicio y qué datos usa o mantenerlo en secreto?", "Explicar cómo funciona y qué datos usa", "Permite a las personas decidir con información."),
    ],
    A=[
        ("Une cada situación con el valor afectado (P privacidad, E equidad, T transparencia): (1) una aplicación comparte tus mensajes con otras empresas sin avisar, (2) un servicio de reserva solo atiende por internet y nadie ayuda a quien no tiene, (3) una aplicación de préstamos no explica cómo decide a quién aprueba.", "1 P, 2 E, 3 T", "Cada situación afecta un valor distinto."),
        arith("En un barrio de ejemplo hay 60 familias y 15 no tienen internet. Si un trámite solo se puede hacer por internet, ¿qué porcentaje de familias queda excluido?", "15*100//60", "Se divide las familias sin internet entre el total y se multiplica por 100.", " %"),
        ex("Un sistema de ejemplo aprueba 45 de 50 solicitudes del barrio centro y 20 de 40 del barrio periférico. ¿Qué porcentaje aprueba en cada barrio?", "90 % y 50 %", "Se calcula 45 × 100 ÷ 50 = 90 y 20 × 100 ÷ 40 = 50.", calc="45*100//50"),
    ],
    Z=[
        ("Con la diferencia de 90 % y 50 % entre dos barrios, ¿qué conviene hacer? A) revisar con datos si hay un trato desigual B) concluir que el barrio periférico presenta peores solicitudes", "A", "Una diferencia grande debe investigarse antes de explicarla."),
        ("Un grupo propone cámaras en la entrada del pasaje. ¿Qué condición protege la privacidad sin eliminar el beneficio? A) grabar solo la entrada, avisar con un letrero y borrar a los 7 días B) grabar todo el barrio y guardarlo para siempre", "A", "Limita los datos a lo necesario y por poco tiempo."),
    ],
    D=[
        arith("Una aplicación tiene 1.000 usuarios, de los cuales 150 son mayores de 65 años. De ellos, solo 30 logran completar el registro. ¿Qué porcentaje de los adultos mayores lo logra?", "30*100//150", "Se divide los que lo logran entre el total del grupo.", " %"),
        ("Pesos: seguridad 3, privacidad 3, costo 1. Opción 1: cámaras en todo el pasaje, puntajes 5, 1 y 2. Opción 2: cámaras solo en la entrada con aviso, puntajes 4, 4 y 3. Opción 3: sin cámaras, puntajes 2, 5 y 5. ¿Cuál se recomienda?", "La opción 2, con 27 puntos", "La opción 1 suma 20, la 2 suma 27 y la 3 suma 26."),
    ],
    ctx=ex("Para tu proyecto quieres grabar un video de una prueba con tus compañeros. ¿Qué debes hacer antes de grabarlos?", "Pedir su consentimiento y explicar para qué se usará el video", "Es su imagen: necesitas su permiso y, si son menores, el de su persona adulta responsable."),
    sc=[
        ("¿Qué es un dilema ético?", "Una situación en que dos valores chocan", "Hay que decidir cuál proteger y cómo cuidar el otro."),
        ("¿Qué es la privacidad?", "El derecho a que tus datos no se usen sin tu permiso", "Protege tu información e imagen."),
        ("¿Qué haces si alguien usa tus datos sin tu permiso?", "Aviso a una persona adulta de confianza", "Ella puede ayudarte a resolverlo."),
    ],
    open_task=(
        "Escoge un caso de ejemplo. Caso 1: se propone una cámara en la entrada de un pasaje de 30 familias. Caso 2: un colegio propone pasar la lista con una aplicación que guarda la cara de cada estudiante y ahorra 4 minutos por clase. Caso 3: una plataforma de tareas muestra públicamente las notas de todo el curso. Escribe qué valores chocan, a quién beneficia y a quién perjudica, y una decisión con una condición que proteja el valor amenazado.",
        "Caso 1: chocan seguridad y privacidad; beneficia a las 30 familias y perjudica a quienes pasan; decisión: aprobar, grabando solo la entrada, con letrero y borrando a los 7 días",
        ["nombra los valores en conflicto", "indica a quién beneficia y a quién perjudica", "toma una decisión", "propone una condición concreta"],
        ["ficha del dilema con decisión"],
        ["quedarse en uno de los dos valores", "proponer una condición vaga"],
        "Pregunta: «¿qué condición protege al valor que está amenazado?». Pídele dar una medida concreta.",
    ),
    reinforce="Elige una aplicación que uses y escribe qué datos tuyos podría usar y si te lo explica con claridad.",
    extend="Explica por qué una solución puede ser legal o útil y aun así generar un dilema ético.",
)

# ------------------------------------------------------------------ OA 06, clase 2
reg(
    OA6, 2,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a medir impactos ambientales de una solución con energía en kWh, residuos y punto de equilibrio entre alternativas. Sirve para comparar con números cuál opción cuida más el ambiente.",
    prior=["Sé qué es el ciclo de vida de un producto.", "Sé multiplicar y dividir.", "Sé qué es un residuo."],
    explain=[
        "El impacto ambiental es el efecto de una solución sobre el aire, el agua, el suelo, la energía, los recursos y los seres vivos. Se revisa en todo el ciclo de vida: materias primas, fabricación, transporte, uso y fin de vida. Un recurso renovable se repone en un tiempo razonable, como la madera de un bosque plantado; uno no renovable se agota, como el petróleo.",
        "Para comparar se usan indicadores con unidades: energía en kilowatt-hora (kWh), residuos en kilogramos y agua en litros. La energía se calcula con potencia en kilowatt (kW) × horas de uso. Un calefactor de 2 kW que funciona 3 horas consume 6 kWh. Si la tarifa de ejemplo es $200 por kWh, cuesta $1.200.",
        "Cuando se compara una opción de un solo uso con una reutilizable, la reutilizable tiene un impacto inicial mayor al fabricarse, pero cada uso genera menos. El punto de equilibrio es el número de usos desde el cual la reutilizable resulta mejor: impacto de fabricación ÷ (impacto por uso de la desechable − impacto por uso de la reutilizable). Reparar, reutilizar y reciclar reducen el impacto porque evitan fabricar de nuevo.",
    ],
    vocab=[("kilowatt-hora (kWh)", "unidad de energía: 1 kW durante 1 hora"), ("recurso renovable", "recurso que se repone en un tiempo razonable"), ("recurso no renovable", "recurso que se agota"), ("residuo", "material que se desecha"), ("punto de equilibrio", "usos desde los cuales una opción compensa su impacto inicial")],
    worked=[
        ("Calcular energía y costo", "Un calefactor de 2 kW funciona 3 horas. Con una tarifa de ejemplo de $200 por kWh, ¿cuánta energía consume y cuánto cuesta?", ["Energía: 2 kW × 3 h = 6 kWh.", "Costo: 6 × 200."], "6 kWh, que cuestan $1.200"),
        ("Calcular un punto de equilibrio", "Fabricar una botella reutilizable equivale a 30 unidades de impacto (cifra de ejemplo) y cada botella desechable genera 1 unidad por uso. Lavar la reutilizable genera 0 unidades por uso. ¿Desde cuántos usos conviene la reutilizable?", ["Divido el impacto de fabricación entre lo que se ahorra por uso: 30 ÷ 1.", "Desde 30 usos ambas tienen el mismo impacto."], "Desde 30 usos"),
    ],
    mistakes=[
        ("Decir que una opción reutilizable siempre es mejor.", "Si se usa pocas veces, no compensa el impacto de fabricarla.", "Calcula el punto de equilibrio y compara con los usos reales."),
        ("Mirar solo el uso y olvidar la fabricación y el fin de vida.", "El mayor impacto puede estar en otra etapa.", "Revisa todo el ciclo de vida."),
    ],
    R=[
        ("La energía en kWh se calcula multiplicando la potencia en kW por las horas de uso. ¿Verdadero o falso?", "Verdadero", "Es la fórmula de energía."),
        ("El fin de vida, ¿es la etapa en que se reutiliza, recicla o desecha el producto o la etapa de fabricación?", "La etapa en que se reutiliza, recicla o desecha", "Es la última etapa del ciclo de vida."),
        ("Un recurso renovable, ¿se repone en un tiempo razonable o se agota?", "Se repone en un tiempo razonable", "Esa es su característica."),
    ],
    C=[
        ("¿Cuál es un recurso no renovable? A) el petróleo B) la madera de un bosque plantado", "A", "El petróleo se agota; el bosque plantado se repone."),
        ("Reutilizar un envase en vez de botarlo, ¿en qué etapas reduce el impacto? A) en el fin de vida y en las materias primas B) solo en el transporte", "A", "Se genera menos residuo y no se necesita material nuevo."),
        ("Reparar un objeto en vez de reemplazarlo reduce el impacto porque: A) evita fabricar uno nuevo B) consume más energía", "A", "La fabricación suele ser una etapa de alto impacto."),
    ],
    A=[
        arith("Un calefactor de 2 kW funciona 4 horas. ¿Cuántos kWh consume?", "2*4", "Se multiplica la potencia por las horas.", " kWh"),
        arith("Con una tarifa de ejemplo de $200 por kWh, ¿cuánto cuesta consumir 8 kWh?", "200*8", "Se multiplica la tarifa por los kWh.", " pesos"),
        arith("Fabricar una bolsa reutilizable equivale a 150 unidades de impacto de ejemplo y cada bolsa desechable genera 6 unidades por uso. ¿Desde cuántos usos conviene la reutilizable, si su uso genera 0?", "150//6", "Se divide el impacto de fabricación entre lo que se ahorra por uso.", " usos"),
    ],
    Z=[
        ("Un equipo nuevo ahorra 100 kWh al año, pero fabricarlo equivale a 500 kWh. Si el equipo viejo seguirá funcionando 3 años más, ¿conviene reemplazarlo solo por el ahorro de energía?", "No", "El ahorro tarda 5 años en compensar la fabricación y solo se usará 3 años."),
        ("Una empresa dice «cero residuos» porque su envase es reciclable. ¿Qué dato falta para comprobar el beneficio? A) cuántos envases realmente se recolectan y reciclan B) el precio del envase", "A", "Que sea reciclable no asegura que se recicle."),
    ],
    D=[
        arith("Una escuela de 200 estudiantes bota 3 hojas por persona al día durante 20 días de clases. Si una de cada 4 hojas se reutiliza como borrador, ¿cuántas hojas se evitan botar?", "200*3*20//4", "Se calcula el total de hojas y se toma un cuarto.", " hojas"),
        ("La opción A consume 6 kWh al mes y genera 2 kg de residuo. La opción B consume 4 kWh y genera 5 kg. Con la regla de ejemplo 1 kg de residuo equivale a 3 kWh de impacto, ¿cuál tiene menos impacto total?", "La opción A", "A suma 6 + 6 = 12 y B suma 4 + 15 = 19."),
    ],
    ctx=ex("Una plancha de 1 kW se usa 3 horas por semana. ¿Cuántos kWh consume en 4 semanas?", "12 kWh", "Cada semana consume 1 × 3 = 3 kWh y en 4 semanas, 12.", calc="1*3*4"),
    sc=[
        ("¿Qué indica el punto de equilibrio?", "Los usos desde los cuales una opción compensa su impacto inicial", "Permite comparar una opción reutilizable con una de un solo uso."),
        ("¿Cómo se calcula la energía en kWh?", "Potencia en kW por horas de uso", "Es la unidad de energía."),
        ("¿Cuáles son las etapas del ciclo de vida?", "Materias primas, fabricación, transporte, uso y fin de vida", "Se revisa el impacto en todas."),
    ],
    open_task=(
        "Compara con datos de ejemplo un vaso desechable con un vaso reutilizable. El desechable genera 2 unidades de impacto por uso. El reutilizable genera 80 unidades al fabricarse y 1 unidad por uso al lavarlo. Calcula desde cuántos usos conviene el reutilizable (80 ÷ (2 − 1)) y decide para dos casos: (1) un evento de un día con 50 usos y (2) uso diario durante 200 días. Justifica.",
        "El punto de equilibrio es 80 usos. Evento de 50 usos: conviene el desechable porque 50 es menor que 80. Uso diario por 200 días: conviene el reutilizable porque 200 supera 80",
        ["calcula bien el punto de equilibrio", "decide en cada caso", "compara con los usos reales", "justifica con números"],
        ["cálculo y decisión por caso"],
        ["decir que el reutilizable siempre conviene", "no comparar los usos con el punto de equilibrio"],
        "Pregunta: «¿cuántas veces se usará realmente?». La decisión depende de ese número.",
    ),
    reinforce="Anota la potencia de un aparato de tu casa (está en su etiqueta; no lo abras ni lo muevas si está conectado) y calcula cuántos kWh consume en una semana si lo usas el tiempo que estimes.",
    extend="Explica por qué una opción que parece más ecológica puede no serlo si se usa muy pocas veces.",
)

# ------------------------------------------------------------------ OA 06, clase 3
reg(
    OA6, 3,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a analizar los impactos sociales de una solución: quién gana, quién pierde, en qué plazo y con qué intensidad. Sirve para ver si los beneficios llegan a todas las personas de una comunidad.",
    prior=["Sé qué es un impacto positivo y uno negativo.", "Sé calcular porcentajes.", "Sé qué es un grupo afectado."],
    explain=[
        "El impacto social es el efecto de una solución en la vida de las personas y la comunidad: el acceso a servicios, el empleo, la salud y la seguridad, la educación, la convivencia y el costo de vida. Una solución puede dejar a algunos grupos mejor y a otros peor. La brecha digital es la diferencia de acceso a internet y a dispositivos entre las personas.",
        "Para analizar se hace un mapa de actores: se listan los grupos afectados, cuántas personas son, si el efecto es positivo (+) o negativo (−) y su intensidad del 1 al 3. El impacto de un grupo es personas × intensidad, con su signo. El impacto neto es la suma de todos. Además se distingue el plazo: corto (se nota pronto) o largo (se nota con los años).",
        "Un impacto neto positivo no basta si hay un grupo gravemente perjudicado. Hay que mirar la distribución: quién gana y quién pierde, y proponer una medida para quien pierde. Las conclusiones deben apoyarse en datos reales de la comunidad: una encuesta que solo consulta a quienes ya usan el servicio tiene sesgo.",
    ],
    vocab=[("impacto social", "efecto de una solución en las personas y la comunidad"), ("brecha digital", "diferencia de acceso a internet y dispositivos"), ("mapa de actores", "lista de grupos afectados con el efecto en cada uno"), ("intensidad", "qué tan fuerte es el efecto, de 1 a 3"), ("impacto neto", "suma de los impactos de todos los grupos")],
    worked=[
        ("Armar un mapa de actores", "Se abre un buzón digital en la junta de vecinos. Los 60 vecinos con internet ganan comodidad (+2); los 20 vecinos sin internet quedan peor informados (−2). ¿Cuál es el impacto de cada grupo y el neto?", ["Con internet: 60 × 2 = +120.", "Sin internet: 20 × (−2) = −40. Neto: 120 − 40."], "+120 y −40; neto +80"),
        ("Distinguir el plazo", "Una escuela capacita a 30 personas en reparación de equipos y eso les da empleo al terminar el curso. ¿Qué plazo tiene el beneficio?", ["El empleo llega después de terminar el curso.", "No se nota de inmediato."], "Largo plazo"),
    ],
    mistakes=[
        ("Concluir que una solución es buena porque el impacto neto es positivo.", "Puede haber un grupo muy perjudicado.", "Mira también quién pierde y propone una medida."),
        ("Consultar solo a quienes ya usan el servicio.", "La opinión de quienes quedan fuera no aparece.", "Incluye a quienes no lo usan o no pueden usarlo."),
    ],
    R=[
        ("Un impacto social, ¿afecta a las personas y la comunidad o solo al ambiente?", "A las personas y la comunidad", "Es la definición de impacto social."),
        ("La brecha digital, ¿es la diferencia de acceso a internet y dispositivos entre las personas o la distancia entre dos pantallas?", "La diferencia de acceso a internet y dispositivos", "Esa es su definición."),
        ("Si una solución beneficia a un grupo y perjudica a otro, ¿el impacto es positivo para todos?", "No", "Para el grupo perjudicado es negativo."),
    ],
    C=[
        ("En un pueblo, 40 de 100 personas no tienen conexión y un servicio solo atiende en línea. ¿Qué impacto negativo tiene? A) dificulta el acceso de quienes no tienen conexión B) usa mucha energía", "A", "Afecta el acceso de ese grupo."),
        ("Una máquina reemplaza el trabajo manual de 5 personas en un taller y permite producir el doble. ¿Cuál es un impacto positivo y uno negativo? A) positivo: más producción; negativo: pérdida de empleos B) positivo: pérdida de empleos; negativo: más producción", "A", "Más producción beneficia al taller y la pérdida de empleos perjudica a las personas."),
        ("Una escuela capacita a 30 personas en un oficio que les dará empleo con los años. Eso es: A) un impacto positivo de largo plazo B) un impacto negativo de corto plazo", "A", "El beneficio llega después y es favorable."),
    ],
    A=[
        arith("En un pueblo de ejemplo de 400 personas, 120 no tienen conexión a internet. ¿Qué porcentaje es?", "120*100//400", "Se divide la parte entre el total y se multiplica por 100.", " %"),
        arith("Grupo A: 50 personas con efecto +2. Grupo B: 20 personas con efecto −3. Grupo C: 30 personas con efecto +1. ¿Cuál es el impacto neto?", "50*2-20*3+30*1", "Se suma cada grupo con su signo.", " puntos"),
        ("Escribe el signo (+ o −): (1) la rampa permite a una vecina salir sola, (2) el cobro solo por internet excluye a quienes no tienen conexión, (3) el taller de oficios enseña a reparar equipos.", "1 +, 2 −, 3 +", "Los efectos 1 y 3 benefician; el 2 perjudica."),
    ],
    Z=[
        ("El impacto neto de una solución es +70, pero 20 personas tienen un efecto de −3. ¿Qué conviene hacer? A) proponer una medida para ese grupo, como atención presencial B) ignorarlo porque el neto es positivo", "A", "Un neto positivo no justifica dejar a un grupo perjudicado."),
        ("Una encuesta de ejemplo consultó solo a usuarios de internet y concluyó que el 95 % apoya un trámite en línea. ¿Qué sesgo tiene? A) no consultó a quienes no tienen internet B) usó pocas preguntas", "A", "Las personas excluidas no pudieron opinar."),
    ],
    D=[
        arith("Un grupo de 60 personas tiene efecto +3, otro de 40 tiene −2 y otro de 100 tiene +1. ¿Cuál es el impacto neto?", "60*3-40*2+100*1", "Se multiplica cada grupo por su efecto y se suman con signo.", " puntos"),
        ("La solución S1 beneficia a 80 personas con +2 y perjudica a 20 con −3. La solución S2 beneficia a 60 con +2 y perjudica a 10 con −1. ¿Cuál tiene mayor impacto neto y menos personas perjudicadas?", "S2: neto 110 y 10 perjudicados", "S1 suma 160 − 60 = 100 con 20 perjudicados; S2 suma 120 − 10 = 110 con 10."),
    ],
    ctx=ex("Se instala un punto de reciclaje de ejemplo: 200 personas tienen efecto +1 y 10 vecinos tienen efecto −2 por el ruido de los camiones. ¿Cuál es el impacto neto?", "180 puntos", "Se calcula 200 × 1 − 10 × 2 = 180.", calc="200*1-10*2"),
    sc=[
        ("¿Qué es un mapa de actores?", "Una lista de grupos afectados con el efecto en cada uno", "Permite ver quién gana y quién pierde."),
        ("¿Cómo se calcula el impacto de un grupo?", "Personas por intensidad, con su signo", "Combina cuántas personas y cuánto les afecta."),
        ("¿Qué es la brecha digital?", "La diferencia de acceso a internet y dispositivos", "Puede excluir a algunas personas."),
    ],
    open_task=(
        "Analiza esta propuesta de ejemplo: una biblioteca de herramientas del barrio, donde los vecinos piden prestadas herramientas gratis. 80 vecinos podrían ahorrar dinero (+2); 15 vecinos que venden herramientas en la ferretería del sector podrían vender menos (−2); 5 voluntarios dedicarán tiempo a atenderla (−1). Calcula el impacto de cada grupo y el neto, indica un beneficio de corto plazo y uno de largo plazo, y propone una medida para el grupo más perjudicado.",
        "Vecinos: +160; ferreteros: −30; voluntarios: −5; neto +125. Corto plazo: ahorro de dinero; largo plazo: más cooperación en el barrio. Medida: que la ferretería sea proveedora de las herramientas de la biblioteca",
        ["calcula el impacto de cada grupo", "calcula el neto", "distingue corto y largo plazo", "propone una medida para quien pierde"],
        ["mapa de actores y medida"],
        ["calcular sin considerar el signo", "no proponer una medida para el grupo perjudicado"],
        "Pregunta: «¿quién pierde con esta solución?». Si no lo menciona, pídele revisar el mapa.",
    ),
    reinforce="Piensa en un cambio reciente de tu barrio o escuela y anota un grupo que ganó y uno que pudo perder.",
    extend="Explica por qué un impacto neto positivo puede esconder una injusticia.",
)

# ------------------------------------------------------------------ OA 06, clase 4
reg(
    OA6, 4,
    materials="Hoja, lápiz, calculadora si la necesitas y los casos escritos en este cuaderno.",
    use="Aprenderé a hacer el balance de los impactos éticos, ambientales y sociales de una solución, a decidir con una regla y a proponer medidas de mitigación con un indicador de seguimiento. Sirve para tomar decisiones completas y honestas sobre la tecnología.",
    prior=["Sé analizar impactos éticos, ambientales y sociales.", "Sé calcular puntajes ponderados.", "Sé comunicar con honestidad."],
    explain=[
        "El balance reúne los impactos de las tres dimensiones en una matriz. Cada impacto lleva un signo (+ o −) y una intensidad de 1 a 3. Se suman los impactos de cada dimensión y se multiplican por un peso que depende del contexto: un barrio con problemas de seguridad puede dar más peso a lo social. La suma ponderada es el total del balance.",
        "Con el total se aplica una regla de decisión acordada antes. Por ejemplo: total de 15 o más, aprobar; de 1 a 14, aprobar con condiciones; 0 o menos, rechazar. Si hay un impacto negativo grave, se pide una medida de mitigación antes de aprobar. Una medida de mitigación reduce un impacto negativo; debe tener un indicador y un plazo para comprobar si funciona.",
        "La decisión se comunica con honestidad: se muestran los beneficios y también los impactos negativos y las medidas previstas. Esconder un impacto negativo conocido es faltar a la ética. Una decisión puede revisarse si cambian los datos.",
    ],
    vocab=[("balance de impactos", "suma de los impactos positivos y negativos"), ("mitigación", "medida que reduce un impacto negativo"), ("aprobar con condiciones", "aceptar la solución si se aplican medidas de mitigación"), ("indicador de seguimiento", "dato que muestra si la medida funciona"), ("regla de decisión", "condición acordada antes para aprobar o rechazar")],
    worked=[
        ("Armar el balance", "Una luminaria solar para un pasaje tiene estos impactos: social +3 (se puede caminar de noche), ambiental +2 (energía renovable), ambiental −1 (residuo de la batería al final de su vida) y ético −1 (la luz molesta a una casa). ¿Cuál es la suma sin pesos?", ["Sumo con signo: 3 + 2 − 1 − 1.", "El resultado es 3."], "3 puntos"),
        ("Proponer una mitigación", "Para el residuo de la batería, ¿qué medida y qué indicador propones?", ["Entregar la batería al terminar su vida útil en un punto de recolección autorizado.", "Indicador: 100 % de las baterías entregadas al terminar su vida útil."], "Entrega en un punto de recolección autorizado; indicador: 100 % de baterías entregadas"),
    ],
    mistakes=[
        ("Aprobar solo por el total, sin mirar un impacto negativo grave.", "Un total alto puede esconder un riesgo serio.", "Exige una medida de mitigación antes de aprobar."),
        ("Ocultar un impacto negativo en el informe.", "Engaña a quienes toman decisiones.", "Muéstralo junto con la medida prevista."),
    ],
    R=[
        ("Una medida de mitigación, ¿reduce un impacto negativo o aumenta un beneficio?", "Reduce un impacto negativo", "Esa es su función."),
        ("Aprobar con condiciones, ¿es aceptar la solución si se aplican medidas o rechazarla por completo?", "Aceptarla si se aplican medidas", "Las condiciones son las medidas de mitigación."),
        ("Un indicador de seguimiento, ¿permite comprobar si la medida funciona o solo decora el informe?", "Permite comprobar si la medida funciona", "Entrega un dato verificable."),
    ],
    C=[
        ("Al comunicar la decisión, ¿se muestran solo los impactos positivos o también los negativos?", "También los negativos", "Mostrar solo lo favorable es engañar."),
        ("Un impacto grave en la seguridad de personas y un total positivo grande. ¿Qué se hace? A) exigir una medida de mitigación antes de aprobar B) aprobar por el total", "A", "Un riesgo grave no puede compensarse con otros beneficios."),
        ("¿Cuál es una mitigación de «las personas sin internet quedan excluidas»? A) mantener un mostrador de atención presencial B) cobrar solo a quienes no tienen internet", "A", "Permite que quienes no tienen internet reciban el servicio."),
    ],
    A=[
        arith("Los impactos de una solución son +3, +2, −1 y −2. ¿Cuál es la suma?", "3+2-1-2", "Se suman con su signo.", " puntos"),
        arith("Social pesa 3 y suma +4; ambiental pesa 2 y suma −1; ético pesa 3 y suma +2. ¿Cuál es el total ponderado?", "3*4+2*(-1)+3*2", "Se multiplica cada suma por su peso y se suman.", " puntos"),
        ("Regla: 15 o más, aprobar; de 1 a 14, aprobar con condiciones; 0 o menos, rechazar. El total de una solución es 11. ¿Qué decisión corresponde?", "Aprobar con condiciones", "11 está entre 1 y 14."),
    ],
    Z=[
        ("Dos soluciones tienen el mismo total, +6. En una, el peor impacto es −3 en seguridad; en la otra, es −1. ¿Cuál es preferible? A) la de peor impacto −1 B) la de −3, porque tiene los mismos puntos", "A", "Es más segura aunque el total sea igual."),
        ("Un informe cuenta 5 beneficios y esconde 2 impactos negativos conocidos. ¿Qué principio ético rompe? A) la honestidad al comunicar B) la autoría", "A", "Oculta información relevante."),
    ],
    D=[
        ex("Pesos: social 3, ambiental 2, ético 3. La solución V tiene sumas de +4, −3 y +1; la solución W tiene +2, +3 y +2. ¿Cuál tiene mayor total y cuántos puntos?", "W, con 18 puntos contra 9", "V suma 12 − 6 + 3 = 9 y W suma 6 + 6 + 6 = 18."),
        ex("Pesos: social 3, ambiental 2, ético 3. La solución T tiene sumas de +3, +1 y −2. Regla: 15 o más, aprobar; de 1 a 14, aprobar con condiciones; 0 o menos, rechazar. ¿Qué decisión corresponde?", "Aprobar con condiciones, con 5 puntos", "T suma 9 + 2 − 6 = 5, que está entre 1 y 14."),
    ],
    ctx=ex("Tu curso propone un huerto escolar de ejemplo. Sumas: social +3, ambiental +2 y ético +1, con pesos 3, 2 y 3. ¿Cuál es el total ponderado?", "16 puntos", "Se calcula 3×3 + 2×2 + 3×1 = 16.", calc="3*3+2*2+3*1"),
    sc=[
        ("¿Qué es una medida de mitigación?", "Una medida que reduce un impacto negativo", "Disminuye el daño o el riesgo."),
        ("¿Qué hace una regla de decisión?", "Define con el total si se aprueba, se aprueba con condiciones o se rechaza", "Se acuerda antes de decidir."),
        ("¿Por qué se muestran los impactos negativos?", "Porque comunicar con honestidad exige no ocultarlos", "Quienes deciden necesitan toda la información."),
    ],
    open_task=(
        "Haz el balance de esta propuesta de ejemplo: un bicicletero techado en una escuela. Impactos: (1) social, 40 estudiantes ahorran pasaje (+2); (2) ambiental, menos viajes en vehículo (+2); (3) ambiental, se usan planchas metálicas que luego serán residuo (−1); (4) ético, una cámara que vigila el bicicletero graba también la calle (−2); (5) social, los estudiantes sin bicicleta no se benefician (−1). Pesos: social 3, ambiental 2, ético 3. Regla: 8 o más, aprobar; de 1 a 7, aprobar con condiciones; 0 o menos, rechazar. Calcula el total, decide y propone una medida de mitigación con su indicador.",
        "Social: +2 − 1 = +1, por 3 da 3; ambiental: +2 − 1 = +1, por 2 da 2; ético: −2, por 3 da −6. Total: −1, se rechaza. Mitigación: orientar la cámara solo al bicicletero; con ético en 0 el total sería 5, y se aprobaría con condiciones; indicador: 0 imágenes de la calle grabadas",
        ["calcula las sumas por dimensión", "aplica los pesos y la regla", "toma la decisión", "propone una mitigación con indicador"],
        ["matriz y decisión"],
        ["olvidar multiplicar por el peso", "proponer una mitigación sin indicador"],
        "Pregunta: «¿cómo sabrás si tu medida funcionó?». Pídele escribir un indicador.",
    ),
    reinforce="Elige un producto que usas y escribe un impacto social, uno ambiental y uno ético, cada uno con su signo.",
    extend="Explica cómo cambiarías los pesos si la solución se aplicara en un lugar con escasez de agua.",
)
