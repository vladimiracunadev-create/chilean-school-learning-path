"""Chile y la región latinoamericana 3.º/4.º medio FG: OA 06 clases 2 a 4 (fuentes e indicadores de integración, causas y perspectivas, relaciones y consecuencias). Países, bloques y datos de ejemplo inventados."""
from __future__ import annotations

from fg_chla_common import build

O6 = "FG-CHLA-3y4-OAC-06"

# ============================================================ OA 06, clase 2
F = ("Ficha 2 (datos de ejemplo, inventados; bloque ficticio Unión del Sur, miles de millones de u.m.). Año 1: exportaciones totales de Alto Valle 200, de las cuales 40 van a los otros países del bloque; importaciones 180. "
     "Año 2: exportaciones totales 200, de las cuales 50 van al bloque; importaciones 180. El arancel a los productos de fuera del bloque pasó de 15 % en el año 1 a 10 % en el año 2. "
     "Fuentes: (1) el texto del tratado de la Unión del Sur; (2) un informe de un organismo regional que analiza los datos; (3) un comunicado del ministerio de comercio de Alto Valle que dice «el bloque fue un éxito total»; "
     "(4) una nota de prensa que cita al informe, pero no da las cifras.")
build(
    O6, 2, F,
    use="Aprenderé a interrogar fuentes sobre integración y cooperación y a leer indicadores como el comercio dentro del bloque, la balanza comercial y los aranceles.",
    explain=[
        'Para estudiar la integración regional se usan fuentes de varios tipos: los textos de los tratados (fuentes primarias), estadísticas de aduanas, informes de organismos regionales, comunicados de gobiernos y notas de prensa. Cada una se interroga: ¿quién la produjo?, ¿para qué?, ¿qué datos entrega y cuáles omite? Un comunicado de un gobierno puede destacar logros; un informe técnico suele mostrar cifras con más detalle; una nota de prensa puede resumir sin dar los datos. Lo prudente es contrastar.',
        'Algunos indicadores simples son el porcentaje del comercio que se hace dentro del bloque (exportaciones al bloque ÷ exportaciones totales × 100), la balanza comercial (exportaciones menos importaciones; si es positiva hay superávit y si es negativa, déficit) y el nivel de los aranceles. Estos indicadores describen el comercio, pero no miden por sí solos el bienestar de las personas ni explican las causas del cambio. Cuando un arancel baja de 15 % a 10 %, la baja es de 5 puntos porcentuales. Los datos de esta ficha son inventados.',
    ],
    vocab=[("comercio dentro del bloque", "parte de las exportaciones que se dirige a los otros países del bloque"), ("balanza comercial", "diferencia entre exportaciones e importaciones"), ("superávit", "balanza comercial positiva: se exporta más de lo que se importa"), ("déficit", "balanza comercial negativa: se importa más de lo que se exporta"), ("fuente primaria", "documento original, como el texto de un tratado")],
    worked=[
        ("Calcular la balanza", "Un país de ejemplo exporta 120 e importa 100. ¿Cuál es la balanza comercial?", ["Se resta: 120 − 100.", "El resultado es positivo, hay superávit."], "+20 (superávit)"),
        ("Porcentaje dentro del bloque", "Un país de ejemplo exporta 80 en total y 20 al bloque. ¿Qué porcentaje va al bloque?", ["Se divide 20 por 80.", "Se multiplica por 100."], "25 %"),
    ],
    mistakes=[("Aceptar un comunicado oficial como evaluación completa.", "Un gobierno puede destacar solo los logros.", "Contrasta con informes técnicos y datos."),
              ("Creer que superávit comercial significa que todas las personas están mejor.", "La balanza no mide el bienestar de las personas.", "Complementa con indicadores de empleo, ingresos y servicios.")],
    T=[
        ('¿Qué es la balanza comercial?', 'La diferencia entre lo que un país exporta y lo que importa', 'La suma de todos los impuestos que cobra el Estado', 'El total de empleos que ofrece el sector exportador', 'La balanza compara lo que un país vende y lo que compra al exterior.'),
        ('¿Qué es un superávit comercial?', 'Exportar más de lo que se importa', 'Importar más de lo que se exporta', 'Exportar exactamente lo mismo que se importa', 'Superávit significa balanza positiva: más exportaciones que importaciones.'),
        ('¿Qué tipo de fuente es el texto de un tratado?', 'Una fuente primaria, porque es el documento original', 'Una fuente secundaria, porque resume un informe técnico', 'Una fuente de opinión que no tiene valor documental', 'El texto del tratado es el documento original del acuerdo.'),
        ('=', '{F} ¿Qué porcentaje de las exportaciones de Alto Valle iba al bloque en el año 1?', '40*100//200', 'Se divide lo que se exporta al bloque por el total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Qué porcentaje de las exportaciones iba al bloque en el año 2?', '50*100//200', 'Se divide lo que se exporta al bloque por el total y se multiplica por 100.', ' %'),
        ('=', '{F} ¿Cuál es la balanza comercial de Alto Valle en el año 2?', '200-180', 'Se resta importaciones a exportaciones.', ' mil millones de u.m.'),
        ('=', '{F} ¿En cuántos puntos porcentuales bajó el arancel externo entre el año 1 y el año 2?', '15-10', 'Se resta el arancel del año 2 al del año 1.', ' puntos porcentuales'),
        ('{F} ¿Qué cambió entre los años 1 y 2 en el comercio dentro del bloque?', 'Aumentó de 20 % a 25 % de las exportaciones', 'Disminuyó de 25 % a 20 % del total', 'No cambió, porque el total fue igual', 'Las exportaciones totales no cambiaron, pero la parte que va al bloque subió de 40 a 50.'),
        ('{F} Según el dato de la balanza, ¿qué situación tuvo Alto Valle?', 'Superávit comercial en ambos años', 'Déficit comercial en ambos años', 'Superávit en el año 1 y déficit en el año 2', 'En ambos años exportó 200 e importó 180: superávit de 20.'),
        ('{F} ¿Por qué la Fuente 3 requiere contraste con otras fuentes?', 'Porque es un comunicado de un gobierno que destaca los logros', 'Porque es un tratado firmado por todos los gobiernos del bloque', 'Porque es una nota de prensa sin ninguna cifra', 'Un comunicado oficial puede destacar solo lo favorable.'),
        ('{F} ¿Qué limitación tiene la Fuente 4?', 'Cita al informe pero no entrega las cifras', 'Entrega todas las cifras del bloque con detalle', 'Es el documento original del tratado', 'La ficha dice que no da las cifras, por lo que no permite comprobar.'),
        ('{F} Alguien afirma: «Como el comercio con el bloque subió, las familias de Alto Valle viven mejor». ¿Qué falla?', 'El indicador describe el comercio, no el bienestar de las familias', 'Nada falla, porque el comercio mide siempre el bienestar', 'Falla porque el comercio con el bloque bajó en el año 2', 'Para el bienestar harían falta datos de empleo, ingresos y servicios.'),
        ('{F} ¿Qué fuente consultarías primero para saber qué se acordó sobre aranceles?', 'La Fuente 1, el texto del tratado', 'La Fuente 4, la nota de prensa', 'La Fuente 3, el comunicado del ministerio', 'El tratado es el documento original que fija los compromisos.'),
    ],
    ctx=('Un país de ejemplo exporta 150 en total, 45 de ellos al bloque, e importa 160. ¿Qué porcentaje va al bloque y cuál es su balanza?', '30 % y un déficit de 10 unidades', '45 % y superávit de 10', '30 % y superávit de 10', 'Se calcula 45 ÷ 150 × 100 = 30; la balanza es 150 − 160 = −10, déficit.'),
    sc=[
        ('En Chile y la región, ¿para qué sirven los informes de organismos regionales al estudiar la integración?', 'Para obtener cifras y análisis con más detalle que un comunicado', 'Sirven como fuentes técnicas que se contrastan con otras.'),
        ('=', 'Un país de ejemplo exporta 90 e importa 100. ¿Cuál es su balanza comercial?', '90-100', 'Se resta importaciones a exportaciones; el resultado negativo indica déficit.', ' mil millones de u.m.'),
        ('¿Por qué un indicador comercial no basta para evaluar un bloque?', 'Porque no mide el bienestar de las personas ni las causas', 'Hay que complementar con empleo, ingresos y servicios.'),
    ],
    op=("Usa la {F} Escribe un informe de cuatro oraciones: porcentaje de comercio dentro del bloque en ambos años, balanza comercial, cambio del arancel y una crítica a la Fuente 3 con una fuente que usarías para contrastar.",
        "El comercio dentro del bloque pasó de 20 % a 25 % de las exportaciones. La balanza fue de +20 en ambos años. El arancel externo bajó de 15 % a 10 %. La Fuente 3 es un comunicado que destaca los logros; la contrastaría con el informe del organismo regional (Fuente 2).",
        ["calcula los indicadores", "interpreta el cambio", "critica una fuente"], ["informe de cuatro oraciones"], ["afirmar bienestar con solo datos comerciales", "no contrastar fuentes"],
        "Revisa que cada cifra tenga su unidad y su año."),
    rx=("Calcula el porcentaje de comercio dentro de un bloque con cifras inventadas.", "Pregunta a tu docente dónde consultar el texto de un tratado comercial de tu país."),
)

# ============================================================ OA 06, clase 3
F = ("Ficha 3 (caso de ejemplo, inventado; bloque ficticio Unión del Sur). Cuatro voces opinan sobre profundizar la integración. "
     "Voz 1, una exportadora de fruta: un mercado más grande y sin aranceles permite vender más y crear empleos. "
     "Voz 2, un dueño de una fábrica textil pequeña: los productos de los países vecinos llegan más baratos y su empresa podría perder clientes. "
     "Voz 3, una dirigente sindical: pide que el bloque incluya normas laborales y programas de capacitación para quienes pierdan empleo. "
     "Voz 4, un científico: la cooperación permite compartir equipos y datos para estudiar problemas comunes, como enfermedades y sequías.")
build(
    O6, 3, F,
    use="Aprenderé a comparar las causas que impulsan o frenan la integración latinoamericana y las perspectivas de distintos actores, sin tomar partido político.",
    explain=[
        'Los países se integran por varias razones: acceder a mercados más grandes, negociar juntos frente a otros países, compartir infraestructura y enfrentar problemas comunes, como enfermedades, sequías o migraciones. Pero también hay obstáculos: diferencias de tamaño y de economía entre los países, intereses productivos que compiten, la falta de caminos y puertos que conecten, cambios de gobierno con prioridades distintas y el temor a perder decisiones propias (soberanía). Por eso la integración avanza a distintos ritmos.',
        'Los actores miran la integración desde su lugar. Las empresas exportadoras suelen valorar más mercados; las que compiten con productos importados pueden temer perder clientes; los sindicatos suelen pedir protección de los empleos; los científicos y las universidades valoran el intercambio. Estas perspectivas se comparan con evidencia, identificando quién habla, qué gana o pierde y qué datos presenta. Una integración bien diseñada puede incluir medidas de apoyo para quienes salen perdiendo. Presentar solo beneficios o solo costos da una imagen incompleta.',
    ],
    vocab=[("soberanía", "capacidad de un Estado de decidir por sí mismo sobre su territorio y sus asuntos"), ("mercado", "conjunto de compradores y vendedores de un producto"), ("competencia", "situación en que varias empresas se disputan los mismos clientes"), ("obstáculo", "dificultad que frena un proceso"), ("capacitación", "formación para aprender nuevas habilidades de trabajo")],
    worked=[
        ("Identificar beneficios y costos", "En un bloque de ejemplo bajan los aranceles. Una empresa exportadora vende más y una fábrica local pierde clientes. ¿Qué se observa?", ["Hay quienes ganan y quienes pierden.", "Conviene considerar ambas perspectivas."], "Beneficios y costos distribuidos de forma desigual"),
        ("Comparar razones", "Dos países de ejemplo se integran para enfrentar una sequía y para vender más. ¿Qué tipo de razones son?", ["Combatir la sequía es una razón de cooperación ambiental.", "Vender más es una razón económica."], "Razones ambientales y económicas"),
    ],
    mistakes=[("Presentar la integración solo con beneficios o solo con costos.", "Distintos actores ganan o pierden de forma diferente.", "Haz una lista de quién gana, quién pierde y qué compensación existe."),
              ("Creer que los intereses de un sector representan los de todo el país.", "Cada sector tiene intereses propios.", "Atribuye cada postura al actor que la sostiene.")],
    T=[
        ('¿Qué es la soberanía de un Estado?', 'Su capacidad de decidir por sí mismo sobre su territorio y asuntos', 'Su obligación de aceptar lo que decidan otros países', 'Su derecho a cobrar aranceles más altos que sus vecinos', 'La soberanía se refiere a la capacidad propia de decisión.'),
        ('¿Qué es la competencia entre empresas?', 'Una situación en que varias empresas se disputan clientes', 'Un acuerdo entre empresas para vender al mismo precio', 'Una ayuda que da el Estado para que una empresa crezca más', 'La competencia es la disputa por los clientes.'),
        ('¿Qué es un obstáculo para la integración?', 'Una dificultad que frena el proceso, como la falta de vías', 'Un beneficio que resulta de unir los mercados', 'Una norma que facilita las exportaciones', 'Los obstáculos frenan; los beneficios y las normas facilitadoras no.'),
        ('{F} ¿Qué beneficio destaca la Voz 1?', 'Vender más y crear empleos en un mercado más grande', 'Evitar la competencia de productos de los países vecinos', 'Compartir equipos de laboratorio entre los países', 'La exportadora destaca más ventas y empleos.'),
        ('{F} ¿Qué temor expresa la Voz 2?', 'Perder clientes frente a productos vecinos más baratos', 'Que haya demasiado empleo en el sector textil', 'Que se prohíba el comercio entre los países del bloque', 'El dueño de la fábrica teme la competencia.'),
        ('{F} ¿Qué pide la Voz 3?', 'Normas laborales y capacitación para quien pierda empleo', 'Que se eliminen todos los acuerdos del bloque', 'Que el bloque cobre aranceles más altos a sus miembros', 'La dirigente propone medidas de protección y apoyo.'),
        ('{F} ¿Qué ofrece la cooperación, según la Voz 4?', 'Compartir equipos y datos para estudiar problemas', 'Que ya no haga falta tener científicos propios', 'Reducir el arancel a los productos de fuera', 'El científico valora el intercambio de equipos y datos.'),
        ('{F} ¿Qué voz ve un costo para un sector de la economía?', 'La Voz 2', 'La Voz 1', 'La Voz 4', 'La Voz 2 describe una posible pérdida de clientes.'),
        ('{F} ¿En qué podrían coincidir las Voces 2 y 3?', 'En que hay que apoyar a quienes salgan perdiendo', 'En que la integración debe eliminarse por completo de la región', 'En que las exportaciones de fruta deben crecer sin ningún límite', 'Ambas se preocupan por quienes pierden empleo o clientes.'),
        ('{F} Alguien dice: «Como la Voz 1 es exportadora, su opinión no sirve». ¿Qué respuesta es más adecuada?', 'Todas tienen intereses; se evalúan con evidencia', 'Tiene razón, porque las personas exportadoras no dan datos útiles', 'Debe ser la única voz que se tome en cuenta', 'Las opiniones se contrastan con datos, sin descartar a nadie por su interés.'),
        ('{F} ¿Qué evidencia ayudaría a evaluar la preocupación de la Voz 2?', 'Cuántos clientes y empleos perdió el sector textil', 'Cuántas veces habló la Voz 2 en la reunión', 'El nombre del dueño de la fábrica', 'Se necesitan datos de impacto en el sector.'),
        ('{F} ¿Cómo podría una integración bien diseñada responder a las Voces 2 y 3?', 'Con apoyo y capacitación para los afectados', 'Con la prohibición de exportar productos de fruta a los países vecinos', 'Con la eliminación de las normas laborales de todos los países', 'La compensación reduce los costos para quienes pierden.'),
        ('{F} ¿Qué obstáculo para la integración mencionaría un país pequeño frente a otro mucho más grande?', 'El temor a quedar en desventaja frente a la más grande', 'La seguridad de que ambos tendrán los mismos beneficios', 'La inexistencia de ventajas para exportar fruta', 'Las diferencias de tamaño pueden generar desconfianza.'),
    ],
    ctx=('Un país de ejemplo estudia unirse a un bloque que reduce aranceles. Su industria de zapatos teme la competencia, y su sector de vinos espera vender más. ¿Qué conviene hacer antes de decidir?', 'Evaluar efectos en ambos sectores y apoyar a quien pierda', 'Escuchar solo al sector de vinos porque exporta más que el de zapatos', 'Ignorar la opinión de la industria de zapatos porque es más pequeña', 'Hay beneficios y costos que se reparten distinto.'),
    sc=[
        ('Nombra una razón por la cual los países se integran.', 'Por ejemplo, acceder a mercados más grandes o enfrentar problemas comunes', 'También negocian juntos y comparten infraestructura.'),
        ('Nombra un obstáculo para la integración.', 'Por ejemplo, diferencias de tamaño o falta de infraestructura', 'También los cambios de gobierno y el temor a perder soberanía.'),
        ('¿Por qué conviene considerar a quienes pierden con un acuerdo?', 'Porque se pueden diseñar compensaciones y evitar daños injustos', 'Presentar solo beneficios da una imagen incompleta.'),
    ],
    op=("Usa la {F} Arma un cuadro con las cuatro voces: qué gana o pierde cada una, qué evidencia pedirías y una medida que la beneficie. Cierra con una oración sobre una coincidencia entre dos voces.",
        "Voz 1: gana mercado; evidencia: ventas de fruta al bloque; medida: facilitar trámites aduaneros. Voz 2: puede perder clientes; evidencia: ventas del sector textil; medida: apoyo para modernizar la fábrica. Voz 3: preocupa el empleo; evidencia: empleos perdidos y creados; medida: capacitación. Voz 4: gana cooperación; evidencia: proyectos conjuntos; medida: fondos compartidos. Coinciden las Voces 2 y 3 en pedir apoyo para quienes salgan perdiendo.",
        ["resume cada voz", "pide evidencia concreta", "señala una coincidencia"], ["cuadro de cuatro filas", "una oración"], ["tomar partido político", "mostrar solo beneficios"],
        "Pregunta quién no tiene voz en este debate."),
    rx=("Explica con un ejemplo por qué un acuerdo puede tener ganadores y perdedores.", "Conversa con una persona de tu casa sobre qué productos de otros países de la región se consumen en tu hogar."),
)

# ============================================================ OA 06, clase 4
F = ("Ficha 4 (datos de ejemplo, inventados; país ficticio Alto Valle en el bloque ficticio Unión del Sur). Tras bajar los aranceles dentro del bloque: "
     "empleos del sector de fruta exportable 300 → 420; empleos del sector textil 500 → 450. El bloque creó un programa de capacitación para pasar de un sector a otro. "
     "Además, los países del bloque firmaron: un acuerdo de salud para compartir información sobre enfermedades; un acuerdo para prevenir la violencia contra las mujeres; "
     "y aceptaron que existe un tribunal regional de derechos humanos al que una persona puede recurrir si agotó los recursos en su país.")
build(
    O6, 4, F,
    use="Aprenderé a explicar relaciones y consecuencias de la integración y de los acuerdos regionales sobre economía, empleo, salud, género y derechos humanos.",
    explain=[
        'Los acuerdos de integración producen consecuencias económicas y sociales. Al bajar aranceles, suelen crecer los sectores que exportan y pueden perder los que compiten con productos importados. En total, el empleo puede subir o bajar según los casos, y por eso se diseñan medidas de apoyo, como capacitación. La integración también puede mejorar la infraestructura, el acceso a conocimientos y la capacidad de negociar. Una buena explicación indica magnitudes (cuánto cambió) y quiénes son afectados.',
        'Los acuerdos no son solo económicos. En salud, la cooperación permite compartir información y coordinar respuestas ante enfermedades. En género, existen convenios regionales para prevenir y sancionar la violencia contra las mujeres. En derechos humanos, existe un sistema regional, con una comisión y una corte, al que las personas pueden acudir por los canales que él fija cuando no logran protección en su país. En ciencia y educación se comparten investigaciones y se reconocen estudios. Sus efectos dependen de que los Estados los apliquen en la práctica.',
    ],
    vocab=[("sector productivo", "conjunto de empresas que producen un mismo tipo de bien, como fruta o textiles"), ("capacitación", "formación para cambiar o mejorar habilidades de trabajo"), ("convenio regional", "acuerdo entre Estados de una misma región"), ("tribunal regional de derechos humanos", "instancia internacional a la que una persona puede recurrir si no logra protección en su país"), ("aplicar un acuerdo", "llevarlo a la práctica con leyes y acciones")],
    worked=[
        ("Calcular empleo neto", "Un sector de ejemplo gana 100 empleos y otro pierde 40. ¿Cuál es el cambio neto?", ["Se suman los ganados y se restan los perdidos.", "100 − 40."], "+60 empleos"),
        ("Explicar una consecuencia", "Un país de ejemplo firma un acuerdo de salud y comparte datos sobre una enfermedad. ¿Qué consecuencia es probable?", ["Con más información, se puede actuar antes.", "Eso mejora la coordinación entre países."], "Mejor coordinación frente a enfermedades"),
    ],
    mistakes=[("Decir que un acuerdo beneficia a todos por igual.", "Los sectores se ven afectados de forma distinta.", "Calcula quién gana y quién pierde, y cuánto."),
              ("Pensar que firmar un acuerdo basta para que se cumpla.", "Los Estados deben aplicarlo con leyes y recursos.", "Revisa si hay leyes, presupuesto y fiscalización.")],
    T=[
        ('¿Qué es un sector productivo?', 'Un conjunto de empresas que producen un mismo tipo de bien', 'Una zona del país donde no vive nadie', 'Un impuesto que se cobra a las exportaciones', 'Un sector agrupa actividades similares, como fruta o textiles.'),
        ('¿Para qué sirve la capacitación de trabajadores?', 'Para aprender nuevas habilidades y poder cambiar de empleo', 'Para evitar que cambien las condiciones de la economía', 'Para pagar aranceles más bajos en el bloque', 'La capacitación ayuda a adaptarse a cambios del mercado.'),
        ('¿Qué es aplicar un acuerdo?', 'Llevarlo a la práctica con leyes y acciones', 'Firmarlo y guardarlo en un archivo oficial', 'Esperar a que otros países lo cumplan primero', 'Aplicar es poner en práctica lo acordado.'),
        ('=', '{F} ¿Cuántos empleos más tiene el sector de fruta exportable?', '420-300', 'Se resta el empleo inicial al final.', ' empleos'),
        ('=', '{F} ¿Cuántos empleos menos tiene el sector textil?', '500-450', 'Se resta el empleo final al inicial.', ' empleos'),
        ('=', '{F} ¿Cuál es el cambio neto de empleos entre ambos sectores?', '(420-300)-(500-450)', 'Se restan los empleos perdidos a los empleos ganados.', ' empleos'),
        ('=', '{F} ¿Qué porcentaje bajó el empleo textil (50 de 500)?', '50*100//500', 'Se divide la pérdida por el empleo inicial y se multiplica por 100.', ' %'),
        ('{F} ¿Qué sector ganó empleos tras bajar los aranceles?', 'El sector de fruta exportable', 'El sector textil de la fábrica', 'Ninguno de los dos sectores productivos', 'La fruta pasó de 300 a 420 empleos.'),
        ('{F} Un diario titula: «La integración destruyó empleos». ¿Qué corrección es más precisa?', 'El textil perdió 50 empleos y el de fruta ganó 120 empleos', 'Es cierto, porque ambos sectores perdieron empleos', 'Es falso, porque ningún sector perdió empleos', 'El saldo fue +70, aunque con ganadores y perdedores.'),
        ('{F} ¿Qué puede hacer el programa de capacitación por los trabajadores textiles?', 'Ayudarlos a pasar a empleos de otros sectores', 'Garantizar que el textil recupere sus empleos', 'Impedir que el empleo de fruta siga creciendo', 'La capacitación facilita el paso a sectores con más demanda.'),
        ('{F} ¿Qué consecuencia puede tener el acuerdo de salud?', 'Mejorar la coordinación frente a enfermedades', 'Eliminar los aranceles dentro del bloque', 'Reducir el empleo en el sector textil vecino', 'Compartir datos sanitarios permite actuar antes y coordinar respuestas.'),
        ('{F} ¿Qué permite el acuerdo sobre derechos humanos?', 'Que una persona recurra a un tribunal regional tras agotar su país', 'Que el tribunal regional reemplace a los tribunales nacionales', 'Que los Estados dejen de aplicar sus propias leyes', 'Es una instancia complementaria que se usa cuando no hay protección en el país.'),
        ('{F} Para saber si el acuerdo de violencia contra las mujeres es eficaz, ¿qué se necesita?', 'Ver si hay leyes, recursos y fiscalización', 'Confirmar solo que el acuerdo fue firmado por todos los gobiernos del bloque', 'Comparar cuántos países lo firmaron frente a otros acuerdos regionales de la zona', 'Un acuerdo es eficaz cuando se aplica en la práctica.'),
    ],
    ctx=('Un bloque de ejemplo reduce aranceles: un sector gana 200 empleos y otro pierde 120. El Estado ofrece capacitación. ¿Cuál es el cambio neto y qué falta evaluar?', '+80 empleos; si la capacitación llega a los afectados', '+320 empleos; que no hay ningún perjudicado entre los trabajadores', '−80 empleos; que la capacitación es innecesaria para todos los sectores', 'El cambio neto es 200 − 120 = 80, pero hay que ver si llega a quienes perdieron empleo.'),
    sc=[
        ('En Chile y la región, ¿qué consecuencia puede tener bajar aranceles para un sector que compite con importaciones?', 'Puede perder clientes y empleos', 'Los sectores que compiten con importados enfrentan más competencia.'),
        ('=', 'Un sector de ejemplo pasa de 80 a 100 empleos y otro de 60 a 50. ¿Cuál es el cambio neto?', '(100-80)-(60-50)', 'Se restan los empleos perdidos a los ganados.', ' empleos'),
        ('¿Por qué firmar un acuerdo no basta para que sus objetivos se cumplan?', 'Porque debe aplicarse con leyes, recursos y fiscalización', 'Sin aplicación, el acuerdo queda en el papel.'),
    ],
    op=("Usa la {F} Escribe una cadena de causas y consecuencias de cinco eslabones desde la baja de aranceles hasta el efecto en el empleo, con las cifras de la ficha. Agrega una oración con una medida de apoyo y otra sobre un acuerdo no comercial (salud, género o derechos humanos).",
        "Bajan los aranceles → crecen las exportaciones de fruta → el empleo de fruta sube de 300 a 420 → compite más el textil → el empleo textil baja de 500 a 450. El cambio neto es +70. Medida: capacitación para trabajadores textiles. Acuerdo no comercial: el de salud permite compartir información sobre enfermedades.",
        ["cinco eslabones con cifras", "calcula el cambio neto", "incluye apoyo y un acuerdo no comercial"], ["cadena de cinco eslabones", "dos oraciones"], ["omitir a los perjudicados", "inventar cifras"],
        "Pregunta qué dato mostraría si los trabajadores textiles lograron pasar al sector de fruta."),
    rx=("Explica con un ejemplo cómo un acuerdo puede tener ganadores y perdedores.", "Pregunta a tu docente qué acuerdo regional de salud o de educación afecta a tu comunidad."),
)
